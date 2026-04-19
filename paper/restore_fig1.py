"""
Use current cropped Fig 1 as image input to Gemini, ask it to restore
the clipped top and bottom so the image is complete.
"""
import os, io, sys, base64, json, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ENV = os.path.join(os.path.dirname(__file__), "..", ".env.all")
api_key = None
for line in open(ENV, "r", encoding="utf-8"):
    if line.startswith("GEMINI_API_KEY="):
        api_key = line.strip().split("=", 1)[1]; break

SRC = os.path.join(os.path.dirname(__file__), "figures",
                    "city_opportunistic_sensing.png")
OUT = os.path.join(os.path.dirname(__file__), "figures",
                    "city_opportunistic_sensing_restored.png")

with open(SRC, "rb") as f:
    src_b64 = base64.b64encode(f.read()).decode("ascii")

PROMPT = """This is a scientific infographic showing opportunistic license plate recognition with cameras around a car. The image was cropped too aggressively at the top and bottom — content is cut off.

Please EXTEND this image VERTICALLY (outpaint) so it has natural space above and below the current content. DO NOT alter the existing content. DO NOT crop further. Produce a complete, uncut version that:
- Adds back the top area with a title bar showing: "Opportunistic License Plate Recognition — AI-Enabled Recovery from Uncontrolled Viewing Angles"
- Adds natural white/light background padding at the bottom
- Keeps the exact same style, colors, and elements as the input
- Returns a nicely-framed 16:9 or 4:3 landscape infographic

Style: flat vector, muted academic palette, clean scientific publication look. Match the input image exactly."""

url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
       f"gemini-2.5-flash-image:generateContent?key={api_key}")
payload = {
    "contents": [{
        "parts": [
            {"text": PROMPT},
            {"inline_data": {"mime_type": "image/png", "data": src_b64}}
        ]
    }],
    "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
}
data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(url, data=data,
                              headers={"Content-Type": "application/json"})
print("Sending image + prompt to Gemini...")
with urllib.request.urlopen(req, timeout=180) as resp:
    parsed = json.loads(resp.read().decode("utf-8"))

for cand in parsed.get("candidates", []):
    for part in cand.get("content", {}).get("parts", []):
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and "data" in inline:
            img_bytes = base64.b64decode(inline["data"])
            with open(OUT, "wb") as f:
                f.write(img_bytes)
            print(f"Saved: {OUT}  ({len(img_bytes)} bytes)")
            sys.exit(0)

print("No image returned")
print(json.dumps(parsed, indent=2)[:1500])
