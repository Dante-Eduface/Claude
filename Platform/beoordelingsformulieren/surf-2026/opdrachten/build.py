"""Bouwt de schrijfopdrachten voor de SURF 2026-demo naar pdf.

Elke map hier (bijvoorbeeld mbo-1-sociaal-werk/) bevat inzending.md en
beoordelingsformulier.md. Eduface heeft alleen die twee nodig; de
opdrachtomschrijving voor de student is vervallen (feedback Dante 10-11-2026).

Per opdrachtnummer is de student op alle niveaus dezelfde (alleen een voornaam),
met dezelfde opdrachtgever. Alleen de moeilijkheid verschilt.

Draaien: python3 build.py            (alles)
         python3 build.py mbo-1      (alleen mappen die zo beginnen)
Uitvoer: ../uitvoer/<course>/<titel met " -" in plaats van ":">/
"""
import subprocess
import sys
from pathlib import Path

HIER = Path(__file__).parent
UIT = HIER.parent / "uitvoer"
CHROMIUM = "/opt/pw-browsers/chromium"

NL, EN = ("Beoordelingsformulier", "Inzending"), ("Rubric", "Submission")

# map: (course, titel in Eduface, student, taal)
OPDRACHTEN = {
    "mbo-1-sociaal-werk": ("MBO", "1. Social work: stageverslag jongerencentrum (1 tot 10)", "Lisa", NL),
    "hbo-1-psychologie": ("HBO", "1. Psychologie: scriptie over jongeren en social media (1 tot 10)", "Lisa", NL),
    "wo-1-sociale-wetenschappen": ("WO", "1. Sociale wetenschappen: scriptie over social media en slaap (1 tot 10)", "Lisa", NL),
    "wo-en-1-social-sciences": ("WO English", "1. Social sciences: thesis on social media and sleep (1 to 10)", "Lisa", EN),

    "mbo-2-rechten": ("MBO", "2. Rechten: brief aan een klant met een kapotte e-bike (onvoldoende tot uitstekend)", "Daan", NL),
    "hbo-2-rechten": ("HBO", "2. Rechten: adviesbrief over een kapotte e-bike (onvoldoende tot uitstekend)", "Daan", NL),
    "wo-2-rechtsgeleerdheid": ("WO", "2. Rechtsgeleerdheid: juridisch advies over een kapotte e-bike (onvoldoende tot uitstekend)", "Daan", NL),
    "wo-en-2-law": ("WO English", "2. Law: legal advice on a faulty e-bike (descriptive)", "Daan", EN),

    "mbo-3-nederlands": ("MBO", "3. Nederlands: betoog over koloniale roofkunst in musea (onvoldoende tot uitstekend)", "Emma", NL),
    "hbo-3-journalistiek": ("HBO", "3. Journalistiek: opiniestuk over koloniale roofkunst in musea (onvoldoende tot uitstekend)", "Emma", NL),
    "wo-3-geschiedenis": ("WO", "3. Geschiedenis: essay over koloniale roofkunst in musea (onvoldoende tot uitstekend)", "Emma", NL),
    "wo-en-3-history": ("WO English", "3. History: essay on colonial looted art in museums (descriptive)", "Emma", EN),

    "mbo-4-techniek": ("MBO", "4. Techniek: onderzoeksverslag over een warmtepomp (1 tot 10)", "Sem", NL),
    "hbo-4-techniek": ("HBO", "4. Techniek: onderzoeksverslag over een warmtepomp (1 tot 10)", "Sem", NL),
    "wo-4-natuurkunde": ("WO", "4. Natuurkunde: onderzoeksverslag over het rendement van een warmtepomp (1 tot 10)", "Sem", NL),
    "wo-en-4-physics": ("WO English", "4. Physics: research report on the efficiency of a heat pump (1 to 10)", "Sem", EN),

    "mbo-5-zorg": ("MBO", "5. Zorg en welzijn: reflectie op een patiënt met pijn op de borst (onvoldoende/voldoende)", "Sophie", NL),
    "hbo-5-verpleegkunde": ("HBO", "5. Verpleegkunde: reflectieverslag stage (onvoldoende/voldoende)", "Sophie", NL),
    "wo-5-geneeskunde": ("WO", "5. Geneeskunde: reflectie op een coschap met een patiënt met pijn op de borst (onvoldoende/voldoende)", "Sophie", NL),
    "wo-en-5-medicine": ("WO English", "5. Medicine: reflection on a clinical rotation with a patient with chest pain (pass/fail)", "Sophie", EN),

    "mbo-6-ondernemen": ("MBO", "6. Ondernemen: wat is een earn-out? (onvoldoende/voldoende)", "Tim", NL),
    "hbo-6-economie": ("HBO", "6. Economie: analyse van een earn-out bij een overname (onvoldoende/voldoende)", "Tim", NL),
    "wo-6-economie": ("WO", "6. Economie: analyse van een earn-out bij een overname (onvoldoende/voldoende)", "Tim", NL),
    "wo-en-6-economics": ("WO English", "6. Economics: analysing an earn-out in an acquisition (pass/fail)", "Tim", EN),
}

CSS = """@page {{ size: A4 {orientatie}; margin: {marge}mm; }}
body {{ font-family: Calibri, Carlito, Arial, sans-serif; font-size: {grootte}pt; line-height: 1.45; color: #000; }}
h1 {{ font-size: 17pt; margin: 0 0 4px; }} h2 {{ font-size: 13pt; margin: 18px 0 6px; page-break-after: avoid; }}
h3 {{ font-size: 11.5pt; margin: 12px 0 4px; page-break-after: avoid; }}
table {{ border-collapse: collapse; width: 99.6%; font-size: {tabel}pt; margin: 8px 0 12px; }}
th, td {{ border: 1px solid #000; padding: 4px 6px; text-align: left; vertical-align: top; }}
th {{ background: #d9d9d9; }} tr {{ page-break-inside: avoid; }} img {{ max-width: 100%; }}
"""


def mapnaam(titel):
    return titel.replace(":", " -")


def liggend(bron):
    """Een formulier met een tabel van vier of meer kolommen komt liggend."""
    for regel in bron.read_text(encoding="utf-8").splitlines():
        if regel.startswith("|") and regel.count("|") >= 6:
            return True
    return False


def pdf(bron, doel, ligt):
    doel.parent.mkdir(parents=True, exist_ok=True)
    css = doel.parent / "_stijl.css"
    css.write_text(CSS.format(orientatie="landscape" if ligt else "", marge=15 if ligt else 22,
                              grootte=10 if ligt else 11, tabel=9 if ligt else 10), encoding="utf-8")
    html = doel.with_suffix(".html")
    subprocess.run(["pandoc", str(bron), "-s", "--metadata", f"title={doel.stem}", "-V", "title=",
                    "--resource-path", str(bron.parent), "-c", css.name, "-o", str(html)], check=True)
    for plaatje in bron.parent.glob("*.png"):
        (doel.parent / plaatje.name).write_bytes(plaatje.read_bytes())
    subprocess.run([CHROMIUM, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    f"--print-to-pdf={doel}", html.as_uri()], check=True, capture_output=True, timeout=180)
    html.unlink()
    css.unlink()
    for plaatje in bron.parent.glob("*.png"):
        (doel.parent / plaatje.name).unlink(missing_ok=True)


if __name__ == "__main__":
    filter_ = sys.argv[1] if len(sys.argv) > 1 else ""
    for map_, (course, titel, student, (formulier, inzending)) in OPDRACHTEN.items():
        if not map_.startswith(filter_) or not (HIER / map_ / "inzending.md").exists():
            continue
        uit = UIT / course / mapnaam(titel)
        f = HIER / map_ / "beoordelingsformulier.md"
        pdf(f, uit / f"{formulier}.pdf", liggend(f))
        pdf(HIER / map_ / "inzending.md", uit / f"{inzending} {student}.pdf", False)
        print(f"{course}: {titel}")
