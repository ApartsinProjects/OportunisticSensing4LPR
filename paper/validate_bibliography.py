"""
Validate paper bibliography and citations against Crossref / OpenAlex.

Pipeline:
  1. Parse paper/index.html:
     - Extract bibliography entries: <li id="rN">...</li>  (N = 1..28)
     - Extract in-text citations: <a href="#rN">...</a>
  2. For each bib entry, query Crossref (via habanero) by title; verify the
     top hit matches the claimed author(s) and year.
  3. Flag orphans: citations pointing to missing IDs, and bib entries never
     cited.
  4. Report suspected hallucinated / fabricated entries.

Output: paper/bibliography_report.md
"""

import io
import os
import re
import sys
import json
import time
from html.parser import HTMLParser

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

try:
    from habanero import Crossref
    HAS_CROSSREF = True
except Exception as e:
    HAS_CROSSREF = False
    print(f"habanero unavailable: {e}")


HTML_PATH = os.path.join(os.path.dirname(__file__), "index.html")
OUT_PATH  = os.path.join(os.path.dirname(__file__), "bibliography_report.md")


class BibExtractor(HTMLParser):
    """Extract bibliography <li id="rN"> entries and anchor citation refs."""
    def __init__(self):
        super().__init__()
        self.bib = {}            # id -> plain text body
        self.cites = []          # list of (rid, context)
        self.in_li = None        # current rN id or None
        self.buf = []
        self.recent_text = []    # for context window around citations

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "li" and attrs.get("id", "").startswith("r"):
            # Only capture numeric ids
            rid = attrs["id"]
            if re.fullmatch(r"r\d+", rid):
                self.in_li = rid
                self.buf = []
        elif tag == "a":
            href = attrs.get("href", "")
            m = re.fullmatch(r"#(r\d+)", href)
            if m:
                rid = m.group(1)
                ctx = " ".join(self.recent_text[-30:])[-200:]
                self.cites.append((rid, ctx))

    def handle_endtag(self, tag):
        if tag == "li" and self.in_li is not None:
            text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
            self.bib[self.in_li] = text
            self.in_li = None
            self.buf = []

    def handle_data(self, data):
        if self.in_li is not None:
            self.buf.append(data)
        self.recent_text.append(data)


def parse_entry(text):
    """Rough parse: extract first author surname, year, title."""
    year_m = re.search(r"\((\d{4})\)", text)
    year = int(year_m.group(1)) if year_m else None
    # Authors before the year
    if year_m:
        pre = text[:year_m.start()].strip(" .,")
        # First author is before the first comma-and-initial or before "&"
        # Surname is the first word before a comma, typically
        m = re.match(r"([A-Z][a-zA-Z\-']+)", pre)
        first_author = m.group(1) if m else pre.split()[0] if pre else ""
        # Title: between closing paren of year and next period
        rest = text[year_m.end():].strip(" .,")
        # Often looks like ". Title of paper. Journal, vol(issue), pp."
        title_m = re.match(r"([^.]+)", rest)
        title = title_m.group(1).strip() if title_m else rest
    else:
        first_author = ""
        title = text
    return first_author, year, title


def query_crossref(cr, title, rows=3):
    try:
        res = cr.works(query_title=title, limit=rows)
        items = res.get("message", {}).get("items", [])
        return items
    except Exception as e:
        return {"error": str(e)}


def match_entry(item, expected_author, expected_year, title):
    """Return (score, note)."""
    t = " ".join((item.get("title") or [""])).lower()
    expected_t = title.lower()[:80]
    notes = []

    # Title similarity: Jaccard on tokens >=4 chars
    def tok(s): return {w for w in re.findall(r"[a-z]{4,}", s.lower())}
    ta, tb = tok(t), tok(expected_t)
    title_sim = len(ta & tb) / max(len(ta | tb), 1)
    notes.append(f"title_sim={title_sim:.2f}")

    # Year match
    parts = item.get("issued", {}).get("date-parts", [[None]])[0]
    yr = parts[0] if parts else None
    year_ok = (yr == expected_year) if expected_year and yr else None
    if year_ok is True:
        notes.append(f"year_ok=yes({yr})")
    elif year_ok is False:
        notes.append(f"year_MISMATCH(expected {expected_year}, got {yr})")

    # Author match
    authors = item.get("author", [])
    first_au = authors[0].get("family", "") if authors else ""
    au_ok = expected_author.lower() in first_au.lower() or first_au.lower() in expected_author.lower()
    notes.append(f"first_author={first_au!r} " + ("OK" if au_ok else "MISMATCH"))

    score = title_sim + (0.4 if year_ok else -0.3 if year_ok is False else 0) \
            + (0.3 if au_ok else -0.2)
    return score, "; ".join(notes), item.get("DOI"), item.get("URL")


def main():
    print(f"Reading: {HTML_PATH}")
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    ex = BibExtractor()
    ex.feed(html)

    bib = ex.bib
    cites = ex.cites

    cited_ids = set(r for r, _ in cites)
    bib_ids   = set(bib.keys())
    orphan_cites = sorted(cited_ids - bib_ids)
    uncited_bib  = sorted(bib_ids - cited_ids)

    print(f"Bibliography entries found: {len(bib)}")
    print(f"Unique in-text citation IDs: {len(cited_ids)}")
    print(f"Orphan citations (cited but no entry): {orphan_cites}")
    print(f"Uncited bibliography entries:          {uncited_bib}")

    # Validate against Crossref
    report_rows = []
    if HAS_CROSSREF:
        cr = Crossref(mailto="review@example.com")
    for rid in sorted(bib.keys(), key=lambda x: int(x[1:])):
        entry_text = bib[rid]
        first_au, year, title = parse_entry(entry_text)
        print(f"\n[{rid}] author={first_au!r} year={year} title[:80]={title[:80]!r}")

        result = {
            "id": rid,
            "author": first_au,
            "year": year,
            "title": title[:120],
            "entry": entry_text,
            "crossref": None,
            "verdict": "unchecked",
        }

        if HAS_CROSSREF and title and len(title) > 10:
            try:
                items = query_crossref(cr, title, rows=3)
            except Exception as e:
                items = {"error": str(e)}
            if isinstance(items, dict) and "error" in items:
                result["verdict"] = f"error: {items['error']}"
            elif not items:
                result["verdict"] = "NOT_FOUND_in_crossref"
            else:
                ranked = []
                for it in items:
                    score, notes, doi, url = match_entry(it, first_au, year, title)
                    ranked.append((score, notes, doi, url, it.get("title", [""])[0]))
                ranked.sort(reverse=True)
                best = ranked[0]
                result["crossref"] = {
                    "score": round(best[0], 3),
                    "notes": best[1],
                    "doi": best[2],
                    "url": best[3],
                    "matched_title": best[4][:120],
                }
                if best[0] > 1.1:
                    result["verdict"] = "MATCH"
                elif best[0] > 0.4:
                    result["verdict"] = "PARTIAL_MATCH"
                else:
                    result["verdict"] = "WEAK_or_HALLUCINATED?"
            # be nice to crossref
            time.sleep(0.4)
        report_rows.append(result)

    # Write markdown report
    lines = ["# Bibliography Validation Report", ""]
    lines.append(f"- Bibliography entries: **{len(bib)}**")
    lines.append(f"- Unique citation IDs used in text: **{len(cited_ids)}**")
    lines.append(f"- Orphan citations (text references missing bib entry): **{orphan_cites}**")
    lines.append(f"- Uncited bibliography entries: **{uncited_bib}**")
    lines.append("")
    lines.append("## Per-entry validation")
    lines.append("")
    for r in report_rows:
        lines.append(f"### [{r['id']}] {r['author']} ({r['year']}) — {r['verdict']}")
        lines.append(f"- Title (parsed): _{r['title']}_")
        lines.append(f"- Entry text: {r['entry']}")
        if r["crossref"]:
            cx = r["crossref"]
            lines.append(f"- Crossref best match: **{cx['matched_title']}**")
            lines.append(f"  - DOI: `{cx['doi']}`")
            lines.append(f"  - Score: {cx['score']} — {cx['notes']}")
        lines.append("")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"\nReport written: {OUT_PATH}")


if __name__ == "__main__":
    main()
