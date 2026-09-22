"""Maakt van criteria-cat-diagnostiek.md een leeg beoordelingsformulier (docx + pdf).

Draaien: python3 build.py
De pdf komt via headless Chromium uit dezelfde criteria, dus docx en pdf lopen niet uiteen.
"""
import re
import subprocess
from pathlib import Path

from docx import Document
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

HIER = Path(__file__).parent
BRON = HIER / "criteria-cat-diagnostiek.md"
TITEL = "Beoordelingsformulier CAT diagnostiek"
UIT = HIER / "beoordelingsformulier-cat-diagnostiek.docx"
CHROMIUM = "/opt/pw-browsers/chromium"

KOPVELDEN = ["Datum", "Naam student", "Beoordelaar"]
SLOTVELDEN = ["Beoordeling", "Feedback"]


def lees_criteria(pad):
    """Geeft [(sectietitel, [criterium, ...]), ...] terug."""
    secties = []
    for regel in pad.read_text(encoding="utf-8").splitlines():
        regel = regel.rstrip()
        if regel.startswith("## "):
            secties.append((regel[3:].strip(), []))
        elif regel.startswith("- ") and secties:
            secties[-1][1].append(regel[2:].strip())
    return secties


def arceer(cel, hex_kleur):
    vulling = OxmlElement("w:shd")
    vulling.set(qn("w:val"), "clear")
    vulling.set(qn("w:fill"), hex_kleur)
    cel._tc.get_or_add_tcPr().append(vulling)


def zet_tekst(cel, tekst, vet=False, grootte=10, midden=False):
    alinea = cel.paragraphs[0]
    alinea.paragraph_format.space_before = Pt(2)
    alinea.paragraph_format.space_after = Pt(2)
    if midden:
        alinea.alignment = WD_ALIGN_PARAGRAPH.CENTER
    stuk = alinea.add_run(tekst)
    stuk.bold = vet
    stuk.font.size = Pt(grootte)
    stuk.font.name = "Calibri"
    cel.vertical_alignment = WD_ALIGN_VERTICAL.CENTER


def bouw(secties):
    doc = Document()
    for sectie in doc.sections:
        sectie.top_margin = Cm(2)
        sectie.bottom_margin = Cm(2)
        sectie.left_margin = Cm(2)
        sectie.right_margin = Cm(2)

    standaard = doc.styles["Normal"]
    standaard.font.name = "Calibri"
    standaard.font.size = Pt(11)

    kop = doc.add_paragraph()
    kop.paragraph_format.space_after = Pt(10)
    stuk = kop.add_run(TITEL)
    stuk.bold = True
    stuk.font.size = Pt(16)

    for veld in KOPVELDEN:
        alinea = doc.add_paragraph()
        alinea.paragraph_format.space_after = Pt(2)
        alinea.add_run(f"{veld}: ").bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(0)

    tabel = doc.add_table(rows=1, cols=2)
    tabel.style = "Table Grid"
    tabel.autofit = False
    breedtes = (Cm(13.2), Cm(3.8))

    koprij = tabel.rows[0]
    zet_tekst(koprij.cells[0], "Beoordelingscriteria", vet=True)
    zet_tekst(koprij.cells[1], "Voldaan / Niet voldaan", vet=True, midden=True)
    for cel in koprij.cells:
        arceer(cel, "D9D9D9")

    for sectietitel, criteria in secties:
        rij = tabel.add_row()
        cel = rij.cells[0].merge(rij.cells[1])
        zet_tekst(cel, sectietitel, vet=True)
        arceer(cel, "F2F2F2")
        for criterium in criteria:
            rij = tabel.add_row()
            zet_tekst(rij.cells[0], criterium)
            zet_tekst(rij.cells[1], "")

    for rij in tabel.rows:
        for cel, breedte in zip(rij.cells, breedtes):
            cel.width = breedte

    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    for veld in SLOTVELDEN:
        alinea = doc.add_paragraph()
        alinea.paragraph_format.space_after = Pt(18)
        alinea.add_run(f"{veld}: ").bold = True

    doc.save(UIT)
    return UIT


HTML_SJABLOON = """<!doctype html>
<html lang="nl"><head><meta charset="utf-8"><title>{titel}</title>
<style>
  @page {{ size: A4; margin: 20mm; }}
  body {{ font-family: Calibri, Carlito, Arial, sans-serif; font-size: 10pt; color: #000; margin: 0; }}
  h1 {{ font-size: 16pt; margin: 0 0 12px; }}
  .veld {{ font-size: 11pt; margin-bottom: 3px; }}
  .veld b {{ font-weight: 700; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 14px; table-layout: fixed; }}
  th, td {{ border: 1px solid #000; padding: 4px 6px; vertical-align: middle; text-align: left; }}
  th {{ background: #d9d9d9; font-weight: 700; }}
  td.oordeel, th.oordeel {{ width: 22%; text-align: center; }}
  tr.sectie td {{ background: #f2f2f2; font-weight: 700; }}
  tr.sectie {{ break-after: avoid; page-break-after: avoid; }}
  tr {{ page-break-inside: avoid; }}
  .slot {{ margin-top: 18px; font-size: 11pt; }}
  .slot p {{ margin: 0 0 24px; }}
</style></head><body>
<h1>{titel}</h1>
{velden}
<table>
<tr><th>Beoordelingscriteria</th><th class="oordeel">Voldaan / Niet voldaan</th></tr>
{rijen}
</table>
<div class="slot">{slot}</div>
</body></html>
"""


def ontsnap(tekst):
    return tekst.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def bouw_pdf(secties, pad_pdf):
    velden = "\n".join(f'<div class="veld"><b>{v}:</b></div>' for v in KOPVELDEN)
    rijen = []
    for sectietitel, criteria in secties:
        rijen.append(f'<tr class="sectie"><td colspan="2">{ontsnap(sectietitel)}</td></tr>')
        for criterium in criteria:
            rijen.append(f'<tr><td>{ontsnap(criterium)}</td><td class="oordeel"></td></tr>')
    slot = "\n".join(f"<p><b>{v}:</b></p>" for v in SLOTVELDEN)
    html = HTML_SJABLOON.format(
        titel=ontsnap(TITEL), velden=velden, rijen="\n".join(rijen), slot=slot
    )
    pad_html = pad_pdf.with_suffix(".html")
    pad_html.write_text(html, encoding="utf-8")
    try:
        subprocess.run(
            [CHROMIUM, "--headless", "--disable-gpu", "--no-sandbox",
             "--no-pdf-header-footer", f"--print-to-pdf={pad_pdf}", pad_html.as_uri()],
            check=True, capture_output=True, timeout=180,
        )
    except Exception as fout:
        print(f"geen pdf gemaakt: {fout}")
        return None
    finally:
        pad_html.unlink(missing_ok=True)
    return pad_pdf


if __name__ == "__main__":
    secties = lees_criteria(BRON)
    aantal = sum(len(c) for _, c in secties)
    pad = bouw(secties)
    print(f"{len(secties)} secties, {aantal} criteria -> {pad.name}")
    pdf = bouw_pdf(secties, UIT.with_suffix(".pdf"))
    if pdf:
        print(f"-> {pdf.name}")
