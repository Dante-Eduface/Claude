"""Bouwt de schrijfopdrachten voor de SURF 2026-demo naar pdf.

Elke map hier (bijvoorbeeld mbo-1-sociaal-werk/) bevat opdracht.md,
beoordelingsformulier.md en inzending.md. Dit script maakt er pdf's van in
../uitvoer/<course>/<titel>/. Het beoordelingsformulier komt liggend.

Draaien: python3 build.py            (alles)
         python3 build.py mbo-1      (alleen mappen die zo beginnen)
"""
import subprocess
import sys
from pathlib import Path

HIER = Path(__file__).parent
UIT = HIER.parent / "uitvoer"
CHROMIUM = "/opt/pw-browsers/chromium"

# map: (course, titel van de assignment in Eduface met " - " in plaats van ":",
#       bestandsnamen voor opdracht, formulier, inzending)
OPDRACHTEN = {
    "mbo-1-sociaal-werk": ("MBO", "1. Social work - stageverslag jongerencentrum (1 tot 10)",
                           ("Opdracht stageverslag", "Beoordelingsformulier stageverslag", "Inzending Yasmina El Idrissi")),
    "hbo-1-psychologie": ("HBO", "1. Psychologie - scriptie over jongeren en social media (1 tot 10)",
                          ("Opdracht scriptie", "Beoordelingsformulier scriptie", "Inzending Noor Hendriks")),
    "wo-1-sociale-wetenschappen": ("WO", "1. Sociale wetenschappen - scriptie over social media en slaap (1 tot 10)",
                                   ("Opdracht scriptie", "Beoordelingsformulier scriptie", "Inzending Lisa van Dijk")),
    "wo-en-1-social-sciences": ("WO English", "1. Social sciences - thesis on social media and sleep (1 to 10)",
                                ("Assignment thesis", "Rubric thesis", "Submission Lisa van Dijk")),
}

CSS = """@page {{ size: A4 {orientatie}; margin: {marge}mm; }}
body {{ font-family: Calibri, Carlito, Arial, sans-serif; font-size: {grootte}pt; line-height: 1.45; color: #000; }}
h1 {{ font-size: 17pt; margin: 0 0 4px; }} h2 {{ font-size: 13pt; margin: 18px 0 6px; page-break-after: avoid; }}
table {{ border-collapse: collapse; width: 99.6%; font-size: {tabel}pt; margin: 8px 0 12px; }}
th, td {{ border: 1px solid #000; padding: 4px 6px; text-align: left; vertical-align: top; }}
th {{ background: #d9d9d9; }} tr {{ page-break-inside: avoid; }}
"""


def pdf(bron, doel, liggend):
    doel.parent.mkdir(parents=True, exist_ok=True)
    css = doel.parent / "_stijl.css"
    css.write_text(CSS.format(orientatie="landscape" if liggend else "", marge=15 if liggend else 22,
                              grootte=10 if liggend else 11, tabel=9 if liggend else 10), encoding="utf-8")
    html = doel.with_suffix(".html")
    subprocess.run(["pandoc", str(bron), "-s", "--metadata", f"title={doel.stem}", "-V", "title=",
                    "-c", css.name, "-o", str(html)], check=True)
    subprocess.run([CHROMIUM, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    f"--print-to-pdf={doel}", html.as_uri()], check=True, capture_output=True, timeout=180)
    html.unlink()
    css.unlink()


if __name__ == "__main__":
    filter_ = sys.argv[1] if len(sys.argv) > 1 else ""
    for map_, (course, titel, namen) in OPDRACHTEN.items():
        if not map_.startswith(filter_):
            continue
        uit = UIT / course / titel
        for bron, naam in zip(("opdracht", "beoordelingsformulier", "inzending"), namen):
            pdf(HIER / map_ / f"{bron}.md", uit / f"{naam}.pdf", liggend=(bron == "beoordelingsformulier"))
        print(f"{course}: {titel}")
