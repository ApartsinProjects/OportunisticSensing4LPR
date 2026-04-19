"""
Generate a publication-quality schematic infographic for Fig 1 using Gemini.

The image is a conceptual diagram for a CEUS paper on opportunistic license-plate
recognition: a minimalist flat illustration showing diverse urban cameras (ATM,
body-worn, dashcam, pole-mounted CCTV, smartphone) capturing a vehicle from
uncontrolled viewing angles, with a stylised arrow or inset showing AI-enabled
restoration producing a readable license plate.
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
assert api_key, "GEMINI_API_KEY not found"

OUT_PATH = os.path.join(os.path.dirname(__file__), "figures",
                         "city_opportunistic_sensing.png")

PROMPT = """Design a clean, minimalist SCHEMATIC INFOGRAPHIC suitable for a
scientific journal (CEUS / Elsevier) — not a photorealistic image. Flat vector
aesthetic, muted academic color palette (soft blues, warm yellows, muted grays,
minimal saturation). White or very light background.

Central subject: an urban street scene viewed from above at a slight angle
(three-quarter isometric view), showing a single car from the rear.

Around the car, position FIVE labeled sensor icons with dashed sight lines
pointing toward the car's rear license plate:
 1. ATM machine (small labeled rectangle on the sidewalk)
 2. Body-worn camera on a pedestrian figure
 3. Dashboard camera inside a nearby vehicle
 4. Pole-mounted CCTV camera
 5. Smartphone held by another pedestrian

Each dashed sight line should approach the plate at a DIFFERENT severe angle
(lateral, elevational, and oblique), emphasizing that the captures are at
uncontrolled viewing angles.

On the right side, add a small labeled INSET BOX showing the transformation:
 [ distorted plate ] --> [ AI restoration block ] --> [ readable plate '341672' ]
with a thin arrow between them. Include a small neural-network icon.

Typography: sans-serif; concise labels beside each sensor (ATM, Body-cam,
Dashcam, CCTV, Phone). Add a small caption title at the top: "Opportunistic
License Plate Recognition — AI-Enabled Recovery from Uncontrolled Viewing Angles"

Style references: Nature Methods / Science Magazine infographics, flat vector
illustration, editorial/technical diagrams, Edward Tufte style clarity.
No photorealism, no shadows, no 3D rendering, no gradients.
Aspect ratio: 16:9 (landscape). High resolution."""


def main():
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"gemini-2.5-flash-image:generateContent?key={api_key}")
    payload = {
        "contents": [{"parts": [{"text": PROMPT}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data,
                                  headers={"Content-Type": "application/json"})
    print("Sending request to Gemini...")
    with urllib.request.urlopen(req, timeout=120) as resp:
        body = resp.read().decode("utf-8")
    parsed = json.loads(body)

    candidates = parsed.get("candidates", [])
    saved = False
    for cand in candidates:
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and "data" in inline:
                img_bytes = base64.b64decode(inline["data"])
                with open(OUT_PATH, "wb") as f:
                    f.write(img_bytes)
                print(f"Saved: {OUT_PATH}  ({len(img_bytes)} bytes)")
                saved = True
                break
        if saved:
            break

    if not saved:
        print("No image returned. Response:")
        print(json.dumps(parsed, indent=2)[:2000])


if __name__ == "__main__":
    main()
