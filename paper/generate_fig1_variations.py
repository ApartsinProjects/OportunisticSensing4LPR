"""
Generate multiple Fig 1 variations from Gemini with different prompt styles.
Saves to paper/figures/fig1_candidates/ for the user to pick from.
"""

import os
import io
import sys
import base64
import json
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ENV_FILE = os.path.join(os.path.dirname(__file__), "..", ".env.all")
api_key = None
with open(ENV_FILE, "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("GEMINI_API_KEY="):
            api_key = line.strip().split("=", 1)[1]
            break

OUT_DIR = os.path.join(os.path.dirname(__file__), "figures", "fig1_candidates")
os.makedirs(OUT_DIR, exist_ok=True)

# Five different prompt variants (different styles and compositions)
VARIANTS = {
    "v1_schematic_infographic": """Clean minimalist SCHEMATIC INFOGRAPHIC for a scientific journal (CEUS/Elsevier).
Flat vector style, muted academic palette (soft blues, warm yellows, grays), white background.
Three-quarter isometric view of an urban street with one car.
Around the car, 5 labeled sensor icons with dashed sight lines to the license plate:
ATM machine, body-worn camera on a pedestrian, dashboard camera in a nearby vehicle, pole-mounted CCTV, smartphone.
Each sight line approaches the plate at a different severe angle.
On the right: small labeled inset box showing [distorted plate] -> [AI restoration neural net icon] -> [readable plate '341672'].
Concise sans-serif labels beside each sensor. Small caption title at top:
"Opportunistic License Plate Recognition — AI-Enabled Recovery from Uncontrolled Viewing Angles"
Style: Nature Methods / Science infographics, Edward Tufte clarity. No photorealism, no shadows, no 3D rendering. 16:9 landscape, high resolution.""",

    "v2_top_down_diagram": """Clean TOP-DOWN DIAGRAM infographic for a scientific publication.
Bird's-eye view of a city street intersection drawn in flat vector style, muted professional palette.
Show a single car as a simple shape, with 5 sensor positions labeled around it:
1) ATM on sidewalk, 2) body-worn camera (pedestrian icon), 3) dashcam (inside nearby car),
4) pole CCTV, 5) smartphone (held by pedestrian icon).
Thin arrows from each sensor converge on the car's license plate at different incidence angles.
Include angle markers showing alpha and beta to illustrate viewing-angle diversity.
Right-side inset: a neural network symbol transforming a blurred plate into a readable '341672'.
Typography sans-serif. Title: "Opportunistic LPR from Urban Imaging Sensors".
No photorealism, no gradients, no shadows. Landscape 16:9.""",

    "v3_pipeline_centered": """Horizontal flow-diagram infographic for a scientific paper.
Left-to-right composition showing the opportunistic sensing pipeline.
LEFT BLOCK: Cluster of 5 camera types labeled (ATM, Body-cam, Dashcam, CCTV, Phone) with small icons.
CENTER: A car with distorted license plate captures approaching it from varied angles.
RIGHT BLOCK: AI neural-network symbol producing a readable plate '341672'.
Flat vector style, soft academic colors (pale blue, yellow, gray, white).
Arrows connecting the blocks. Labels in sans-serif.
Clean, uncluttered. No photorealism, no shadows.
Caption at top: "AI-enabled license plate recovery from opportunistic urban sensors".
16:9 landscape, high resolution.""",

    "v4_isometric_scene": """ISOMETRIC scientific illustration, flat vector style, muted palette.
An isometric urban block with buildings corners trimmed.
Key elements visible:
- One parked/moving car with license plate.
- Mounted CCTV camera on a post.
- ATM machine on sidewalk with small camera.
- Pedestrian walking with body-worn camera.
- Dashcam visible inside another car.
- Pedestrian holding up a smartphone.
All 5 cameras have dashed vision cones pointing toward the car's plate.
Small callout box on the side showing: distorted plate becomes readable '341672' via AI.
Title at bottom: "Opportunistic LPR: recovery from uncontrolled viewing angles".
Style: clean isometric, like Figma illustration kits or technical diagrams.
No photorealism, minimal shadows OK, flat surfaces. Landscape orientation.""",

    "v5_conceptual_minimalist": """MINIMALIST conceptual illustration for a scientific journal cover.
Simple iconographic composition on white background.
Central element: stylized car outline showing a foreshortened license plate.
Surrounding: 5 small pictograms of camera types (ATM, body cam, dashcam, CCTV, phone)
each with thin radial lines indicating their viewing angle toward the plate.
One stylized arrow transforms the distorted plate into a readable one '341672' through
a small neural-network motif.
All in a limited 3-color palette: deep blue, warm yellow, soft gray.
Thin strokes, flat design, editorial style.
Sparse text labels only where needed.
No photorealism, no gradients, no 3D. 16:9 landscape.""",
}


def generate(prompt_name, prompt_text):
    out_path = os.path.join(OUT_DIR, prompt_name + ".png")
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"gemini-2.5-flash-image:generateContent?key={api_key}")
    payload = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data,
                                  headers={"Content-Type": "application/json"})
    print(f"  [{prompt_name}] requesting...")
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            body = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  [{prompt_name}] FAILED: {e}")
        return False
    parsed = json.loads(body)
    for cand in parsed.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and "data" in inline:
                img_bytes = base64.b64decode(inline["data"])
                with open(out_path, "wb") as f:
                    f.write(img_bytes)
                print(f"  [{prompt_name}] saved {out_path} ({len(img_bytes)} bytes)")
                return True
    print(f"  [{prompt_name}] no image in response")
    return False


if __name__ == "__main__":
    print(f"Output dir: {OUT_DIR}")
    for name, prompt in VARIANTS.items():
        generate(name, prompt)
    print("\nDone. Listing candidates:")
    for f in sorted(os.listdir(OUT_DIR)):
        print(f"  {f}")
