#!/usr/bin/env python3
"""Erzeugt einen QR-Code zur finalen URL der Paris-Geburtstagsseite.

Nutzung:
  python generate_qr.py https://dein-link.netlify.app/

Ausgabe:
  paris-reise-qr.png
"""
import sys
from pathlib import Path

try:
    import qrcode
except ImportError as exc:
    raise SystemExit("Bitte zuerst installieren: pip install qrcode[pil]") from exc

if len(sys.argv) != 2 or not sys.argv[1].startswith(("http://", "https://")):
    raise SystemExit("Bitte eine echte URL angeben, z. B.: python generate_qr.py https://dein-link.netlify.app/")

url = sys.argv[1].rstrip("/") + "/"
img = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=14,
    border=4,
)
img.add_data(url)
img.make(fit=True)
out = img.make_image(fill_color="black", back_color="white").convert("RGB")
path = Path("paris-reise-qr.png")
out.save(path)
print(f"QR-Code gespeichert: {path.resolve()}")
