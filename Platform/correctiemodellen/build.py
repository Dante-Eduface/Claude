"""Maakt uit elk correctiemodel-bestand (.md) een pdf die Eduface goed kan uitlezen.

Draaien: python3 build.py

Opbouw van de bron:
- '# titel' en een regel die begint met 'Source:'
- optioneel '## Context' met '- Label: tekst'-regels
- '## Exercise ...' per opgave, met per vraag:
  - 'Q (label):' de letterlijke vraag aan de student (label '1' wordt 'Question <code>.1')
  - 'O:' een antwoordoptie bij meerkeuze, een regel per optie
  - 'A:' het modelantwoord
  - '| ... |' regels: een tabel als (deel van het) modelantwoord, eerste regel is de kop
  - 'N:' een opmerking, bijvoorbeeld dat het antwoord niet uit de officiele key komt
De pdf komt uit headless Chromium, net als in Platform/beoordelingsformulieren/.
"""
import html
import re
import subprocess
from pathlib import Path

HIER = Path(__file__).parent
CHROMIUM = "/opt/pw-browsers/chromium"


def lees(pad):
    titel, bron, context, opgaven = "", "", [], []
    in_context = False
    for regel in pad.read_text(encoding="utf-8").splitlines():
        regel = regel.strip()
        vraag = re.match(r"Q \((.+?)\):\s*(.*)", regel)
        if regel.startswith("# "):
            titel = regel[2:]
        elif regel.startswith("Source:"):
            bron = regel
        elif regel.startswith("## "):
            in_context = regel == "## Context"
            if not in_context:
                opgaven.append((regel[3:], []))
        elif in_context and regel.startswith("- "):
            label, _, tekst = regel[2:].partition(":")
            context.append((label.strip(), tekst.strip()))
        elif vraag:
            opgaven[-1][1].append(
                {"label": vraag[1], "vraag": vraag[2], "opties": [], "antwoord": "", "tabel": [], "noot": ""}
            )
        elif regel.startswith("O:"):
            opgaven[-1][1][-1]["opties"].append(regel[2:].strip())
        elif regel.startswith("A:"):
            opgaven[-1][1][-1]["antwoord"] = regel[2:].strip()
        elif regel.startswith("|"):
            opgaven[-1][1][-1]["tabel"].append([c.strip() for c in regel.strip("|").split("|")])
        elif regel.startswith("N:"):
            opgaven[-1][1][-1]["noot"] = regel[2:].strip()
    return titel, bron, context, opgaven


SJABLOON = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{titel}</title>
<style>
  @page {{ size: A4; margin: 20mm; }}
  body {{ font-family: Calibri, Carlito, Arial, sans-serif; font-size: 11pt; color: #000; margin: 0; line-height: 1.35; }}
  h1 {{ font-size: 16pt; margin: 0 0 4px; }}
  .bron {{ font-size: 9.5pt; margin: 0 0 16px; }}
  h2 {{ font-size: 13pt; margin: 18px 0 8px; border-bottom: 1px solid #000; padding-bottom: 2px; break-after: avoid; }}
  .vraag {{ margin: 0 0 12px; break-inside: avoid; }}
  .vraag p {{ margin: 0 0 2px; }}
  .opties {{ margin: 0 0 2px 16px; }}
  .label {{ font-weight: 700; }}
  .noot {{ font-style: italic; font-size: 9.5pt; }}
  .context p {{ margin: 0 0 6px; }}
  table {{ border-collapse: collapse; margin: 4px 0 4px; font-size: 10pt; }}
  th, td {{ border: 1px solid #000; padding: 2px 10px; text-align: right; }}
  th {{ background: #d9d9d9; }}
  td:nth-child(2), th:nth-child(2) {{ text-align: left; }}
</style></head><body>
<h1>{titel}</h1>
<p class="bron">{bron}</p>
{inhoud}
</body></html>
"""

e = html.escape


def tabel_html(rijen):
    kop, *rest = rijen
    return (
        "<table><tr>" + "".join(f"<th>{e(c)}</th>" for c in kop) + "</tr>"
        + "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rest)
        + "</table>"
    )


def bouw(pad):
    titel, bron, context, opgaven = lees(pad)
    delen = []
    if context:
        delen.append('<h2>Context</h2><div class="context">')
        delen += [f'<p><span class="label">{e(k)}:</span> {e(v)}</p>' for k, v in context]
        delen.append("</div>")
    for opgave, vragen in opgaven:
        code = opgave.replace("Exercise ", "")
        delen.append(f"<h2>{e(opgave)}</h2>")
        for v in vragen:
            kop = f"Question {code}.{v['label']}" if v["label"].isdigit() else f"{code} {v['label']}"
            stukken = [f'<div class="vraag"><p class="label">{e(kop)}</p><p>{e(v["vraag"])}</p>']
            stukken += [f'<p class="opties">{e(o)}</p>' for o in v["opties"]]
            stukken.append(f'<p><span class="label">Model answer:</span> {e(v["antwoord"])}</p>')
            if v["tabel"]:
                stukken.append(tabel_html(v["tabel"]))
            if v["noot"]:
                stukken.append(f'<p class="noot">{e(v["noot"])}</p>')
            stukken.append("</div>")
            delen.append("".join(stukken))
    htmlpad = pad.with_suffix(".html")
    htmlpad.write_text(SJABLOON.format(titel=e(titel), bron=e(bron), inhoud="\n".join(delen)), encoding="utf-8")
    pdfpad = pad.with_suffix(".pdf")
    subprocess.run(
        [CHROMIUM, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdfpad}", htmlpad.as_uri()],
        check=True, capture_output=True,
    )
    htmlpad.unlink()
    return pdfpad


if __name__ == "__main__":
    for bron in sorted(HIER.glob("correctiemodel-*.md")):
        print(bouw(bron))
