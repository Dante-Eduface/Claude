"""Maakt van de .md-bestanden in deze map een docx. Draaien: python3 build.py"""
import re
from pathlib import Path
from docx import Document
from docx.shared import Pt

HIER = Path(__file__).parent
BESTANDEN = ["beoordelingsformulier.md", "cat-student-met-fouten.md"]


def inline(p, tekst):
    for i, deel in enumerate(re.split(r"\*\*", tekst)):
        deel = deel.replace("`", "")
        if deel:
            p.add_run(deel).bold = i % 2 == 1


def bouw(md):
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)
    regels = md.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(regels):
        r = regels[i].rstrip()
        if r.startswith("|"):
            rijen = []
            while i < len(regels) and regels[i].startswith("|"):
                cellen = [c.strip() for c in regels[i].strip("|").split("|")]
                if not all(re.fullmatch(r"-+", c) for c in cellen):
                    rijen.append(cellen)
                i += 1
            t = doc.add_table(rows=len(rijen), cols=len(rijen[0]))
            t.style = "Table Grid"
            for ri, rij in enumerate(rijen):
                for ci, c in enumerate(rij):
                    cel = t.cell(ri, ci)
                    inline(cel.paragraphs[0], f"**{c}**" if ri == 0 and c else c)
            doc.add_paragraph()
            continue
        if r.startswith("# "):
            doc.add_heading(r[2:], 0)
        elif r.startswith("## "):
            doc.add_heading(r[3:], 1)
        elif r.startswith("_") and r.endswith("_"):
            pass  # interne notitie, niet in de docx
        elif r:
            inline(doc.add_paragraph(), r)
        i += 1
    uit = md.with_suffix(".docx")
    doc.save(uit)
    print(uit.name)


for naam in BESTANDEN:
    bouw(HIER / naam)
