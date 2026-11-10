"""Bouwt de tentamens micro-economie voor de SURF 2026-demo.

Per niveau drie documenten, elk als docx en pdf:
  1. het tentamen (de vragen, wat de student krijgt)
  2. het correctiemodel (context voor de AI, antwoordmodel, criteria met halve punten)
  3. een ingevulde inzending van een fictieve student

Draaien: python3 build.py
Uitvoer: ../uitvoer/<course>/<assignment>/
"""
import importlib
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

HIER = Path(__file__).parent
UIT = HIER.parent / "uitvoer"
CHROMIUM = "/opt/pw-browsers/chromium"
sys.path.insert(0, str(HIER))

COURSES = {
    # Mapnaam = de titel in Eduface, met " - " in plaats van ":" (Windows staat geen dubbele punt toe).
    "mbo": ("MBO", "7. Tentamen micro-economie"),
    "hbo": ("HBO", "7. Tentamen micro-economie"),
    "wo": ("WO", "7. Tentamen micro-economie"),
    "wo_en": ("WO English", "7. Microeconomics exam"),
}

TEKST = {
    "nl": {
        "vraag": "Vraag", "punt": "punt", "punten": "punten", "tijd": "Tijd", "totaal": "Totaal",
        "instructie": "Beantwoord alle vragen. Laat bij rekenvragen je berekening zien. Een antwoord zonder berekening levert niet alle punten op.",
        "context": "Context voor de beoordelaar", "antwoord": "Antwoordmodel", "criteria": "Beoordelingscriteria",
        "kop": ["Criterium", "Max.", "Alle punten als", "Deel van de punten"],
        "algemeen": "Algemene instructies voor de beoordelaar",
        "regels": [
            "Geef per criterium alle punten, een deel van de punten (in stappen van 0,5) of 0 punten, zoals in de tabel staat.",
            "Een fout die doorwerkt in een volgende deelvraag wordt maar één keer bestraft. Rekent de student correct verder met een eigen foute uitkomst, dan krijgt die de punten voor de vervolgstap.",
            "Andere formuleringen zijn goed als de economische inhoud klopt.",
            "Bij een invultabel is elke kolom één criterium. Alle cellen in een kolom juist: alle punten. Eén cel fout: de helft. Twee of meer fout: 0.",
            "Cijfer = 1 + 9 × (behaalde punten / totaal aantal punten), afgerond op één decimaal.",
        ],
        "correctiemodel": "Correctiemodel", "uitwerking": "Uitwerkingen", "naam": "Naam", "nummer": "Studentnummer",
    },
    "en": {
        "vraag": "Question", "punt": "point", "punten": "points", "tijd": "Time", "totaal": "Total",
        "instructie": "Answer all questions. Show your working for calculations. An answer without working will not earn full marks.",
        "context": "Context for the marker", "antwoord": "Model answer", "criteria": "Marking criteria",
        "kop": ["Criterion", "Max.", "Full points if", "Partial points"],
        "algemeen": "General instructions for the marker",
        "regels": [
            "For each criterion, award full points, partial points (in steps of 0.5) or 0 points, as set out in the table.",
            "An error carried forward into a later sub-question is penalised only once. If the student correctly continues with their own wrong result, they earn the points for the next step.",
            "Different wording is fine as long as the economics is correct.",
            "In a fill-in table each column is one criterion. All cells in a column correct: full points. One cell wrong: half. Two or more wrong: 0.",
            "Grade = 1 + 9 × (points earned / total points), rounded to one decimal.",
        ],
        "correctiemodel": "Marking scheme", "uitwerking": "Answers", "naam": "Name", "nummer": "Student number",
    },
}


def getal(x, taal):
    s = f"{x:g}"
    return s.replace(".", ",") if taal == "nl" else s


def pnt(x, t, taal):
    return f"{getal(x, taal)} {t['punt'] if x == 1 else t['punten']}"


def cel(s):
    return s.replace("|", "/").replace("\n", " ")


def kop_tentamen(tn, t, totaal):
    return (f"# {tn['titel']}\n\n{tn['niveau']}\n\n"
            f"**{t['tijd']}:** {tn['tijd']} · **{t['totaal']}:** {pnt(totaal, t, tn['taal'])}\n\n").replace(" · ", "   ")


def md_tentamen(tn, t, totaal):
    md = kop_tentamen(tn, t, totaal) + f"{t['instructie']}\n\n"
    for v in tn["vragen"]:
        md += f"## {t['vraag']} {v['nr']} ({pnt(v['punten'], t, tn['taal'])})\n\n{v['vraag']}\n\n"
    return md


def md_correctiemodel(tn, t, totaal):
    taal = tn["taal"]
    md = f"# {t['correctiemodel']}: {tn['titel'].lower() if taal == 'nl' else tn['titel']}\n\n{tn['niveau']}\n\n"
    md += f"**{t['totaal']}:** {pnt(totaal, t, taal)}\n\n## {t['algemeen']}\n\n"
    md += "".join(f"- {r}\n" for r in t["regels"]) + "\n"
    for v in tn["vragen"]:
        md += f"## {t['vraag']} {v['nr']}. {v['onderwerp']} ({pnt(v['punten'], t, taal)})\n\n"
        md += f"{v['vraag']}\n\n**{t['context']}**\n\n{v['context']}\n\n**{t['antwoord']}**\n\n{v['antwoord']}\n\n"
        md += f"**{t['criteria']}**\n\n| " + " | ".join(t["kop"]) + " |\n|------------|--|--------------------|--------------------|\n"
        for naam, p, vol, deel in v["criteria"]:
            md += f"| {cel(naam)} | {getal(p, taal)} | {cel(vol)} | {cel(deel)} |\n"
        som = sum(c[1] for c in v["criteria"])
        assert abs(som - v["punten"]) < 1e-9, f"{tn['code']} vraag {v['nr']}: criteria {som} != {v['punten']}"
        md += "\n"
    return md


def md_inzending(tn, t):
    md = f"# {t['uitwerking']} {tn['titel'].lower() if tn['taal'] == 'nl' else tn['titel'].lower()}\n\n"
    md += f"**{t['naam']}:** {tn['student']}   **{t['nummer']}:** {tn['studentnummer']}\n\n{tn['niveau']}\n\n"
    for v in tn["vragen"]:
        md += f"## {t['vraag']} {v['nr']}\n\n{v['student']}\n\n"
    return md


CSS = """@page { size: A4; margin: 20mm; }
body { font-family: Calibri, Carlito, Arial, sans-serif; font-size: 10.5pt; line-height: 1.4; color: #000; }
h1 { font-size: 17pt; margin: 0 0 4px; } h2 { font-size: 12.5pt; margin: 18px 0 6px; page-break-after: avoid; }
table { border-collapse: collapse; width: 99.6%; font-size: 9.5pt; margin: 6px 0 10px; }
th, td { border: 1px solid #000; padding: 3px 6px; text-align: left; vertical-align: top; }
th { background: #d9d9d9; } tr { page-break-inside: avoid; }
"""


def randen(pad):
    """Pandoc zet tabellen zonder lijnen in Word; dit geeft elke tabel een rand."""
    doc = Document(pad)
    for tabel in doc.tables:
        tblPr = tabel._tbl.tblPr
        rand = OxmlElement("w:tblBorders")
        for kant in ("top", "left", "bottom", "right", "insideH", "insideV"):
            e = OxmlElement(f"w:{kant}")
            e.set(qn("w:val"), "single")
            e.set(qn("w:sz"), "4")
            e.set(qn("w:color"), "000000")
            rand.append(e)
        tblPr.append(rand)
    doc.save(pad)


def schrijf(md, basis):
    """basis zonder extensie; maakt basis.docx en basis.pdf."""
    basis.parent.mkdir(parents=True, exist_ok=True)
    bron = basis.with_suffix(".md")
    bron.write_text(md, encoding="utf-8")
    subprocess.run(["pandoc", str(bron), "-o", str(basis.with_suffix(".docx"))], check=True)
    randen(basis.with_suffix(".docx"))
    css = basis.parent / "_stijl.css"
    css.write_text(CSS, encoding="utf-8")
    html = basis.with_suffix(".html")
    subprocess.run(["pandoc", str(bron), "-s", "--metadata", f"title={basis.name}", "-V", "title=",
                    "-c", css.name, "-o", str(html)], check=True)
    subprocess.run([CHROMIUM, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                    f"--print-to-pdf={basis.with_suffix('.pdf')}", html.as_uri()],
                   check=True, capture_output=True, timeout=180)
    for f in (bron, html, css):
        f.unlink()


def bestandsnamen(tn):
    niveau = COURSES[tn["code"]][0].replace(" English", "")
    if tn["taal"] == "nl":
        return (f"Tentamen micro-economie {niveau}", f"Correctiemodel micro-economie {niveau}",
                f"Inzending {tn['student']}")
    return (f"Microeconomics exam {niveau}", f"Marking scheme microeconomics {niveau}",
            f"Submission {tn['student']}")


if __name__ == "__main__":
    for code in COURSES:
        tn = importlib.import_module(code).TENTAMEN
        t = TEKST[tn["taal"]]
        totaal = sum(v["punten"] for v in tn["vragen"])
        course, assignment = COURSES[code]
        map_ = UIT / course / assignment
        n_tent, n_corr, n_inz = bestandsnamen(tn)
        schrijf(md_tentamen(tn, t, totaal), map_ / n_tent)
        schrijf(md_correctiemodel(tn, t, totaal), map_ / n_corr)
        schrijf(md_inzending(tn, t), map_ / n_inz)
        verwacht = sum(tn["verwacht"].values())
        cijfer = 1 + 9 * verwacht / totaal
        print(f"{course}: {len(tn['vragen'])} vragen, {getal(totaal, 'nl')} punten, "
              f"verwachte score inzending {getal(verwacht, 'nl')} (cijfer {cijfer:.1f})")
