#!/usr/bin/env python3
"""Bouwt uit een dossier-JSON een los HTML-bestand dat offline opent.

    python3 bouw.py <dossier.json> [uitvoer.html]

Alles zit in het resultaat: fonts, opmaak, inhoud. Geen internet, geen server,
geen tweede bestand. Dubbelklikken is genoeg.
"""
import base64
import json
import sys
from pathlib import Path

HIER = Path(__file__).parent

FONTS = [
    ("Inter", "fonts/Inter-var.woff2", "100 900", "normal"),
    ("League Spartan", "fonts/LeagueSpartan-var.woff2", "100 900", "normal"),
]


def font_css() -> str:
    regels = []
    for familie, pad, gewicht, stijl in FONTS:
        bestand = HIER / pad
        if not bestand.exists():
            raise SystemExit(f"font ontbreekt: {bestand}")
        data = base64.b64encode(bestand.read_bytes()).decode("ascii")
        regels.append(
            f"@font-face{{font-family:'{familie}';font-style:{stijl};"
            f"font-weight:{gewicht};font-display:block;"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}"
        )
    return "\n".join(regels)


def bouw(json_pad: Path, uit_pad: Path) -> Path:
    dossier = json.loads(json_pad.read_text(encoding="utf-8"))
    for veld in ("opleiding", "vak", "beoordelingsoptie", "studenten"):
        if veld not in dossier:
            raise SystemExit(f"veld ontbreekt in {json_pad.name}: {veld}")
    if "rangorde" not in dossier["beoordelingsoptie"]:
        raise SystemExit("beoordelingsoptie.rangorde ontbreekt (laag naar hoog)")

    sjabloon = (HIER / "sjabloon.html").read_text(encoding="utf-8")
    titel = f"{dossier['vak']} — {dossier.get('titel', 'Eduface testdag')}"
    # </script> in de data zou het script afbreken, dus onschadelijk maken
    data = json.dumps(dossier, ensure_ascii=False, indent=2).replace("</", "<\\/")

    html = (
        sjabloon.replace("__TITEL__", titel)
        .replace("/*__FONTS__*/", font_css())
        .replace("/*__DATA__*/", data)
    )
    uit_pad.write_text(html, encoding="utf-8")
    return uit_pad


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    bron = Path(sys.argv[1])
    doel = Path(sys.argv[2]) if len(sys.argv) > 2 else bron.with_suffix(".html")
    pad = bouw(bron, doel)
    kb = pad.stat().st_size / 1024
    print(f"{pad}  ({kb:.0f} KB)")
