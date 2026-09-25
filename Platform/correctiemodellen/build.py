"""Maakt uit elk correctiemodel-bestand (.md) een pdf die Eduface goed kan uitlezen.

Draaien: python3 build.py
Opbouw van de bron: '# titel', een bronregel, optioneel '## Context' met '- Label: tekst'-regels,
'## Exercise ...' per opgave, en per vraag een 'Q (label):'-regel met de letterlijke vraag,
een 'A:'-regel met het modelantwoord en optioneel een 'N:'-regel met een opmerking.
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
    for regel in pad.read_text(encoding="utf-8").splitlines():
        regel = regel.strip()
        vraag = re.match(r"Q \((.+?)\):\s*(.*)", regel)
        if regel.startswith("# "):
            titel = regel[2:]
        elif regel.startswith("Source:"):
            bron = regel
        elif regel == "## Context":
            opgaven.append(None)
        elif regel.startswith("## "):
            opgaven.append((regel[3:], []))
        elif regel.startswith("- ") and opgaven and opgaven[-1] is None:
            context.append(regel[2:].partition(":")[::2])
        elif vraag:
            opgaven[-1][1].append({"label": vraag[1], "vraag": vraag[2], "antwoord": "", "noot": ""})
        elif regel.startswith("A:"):
            opgaven[-1][1][-1]["antwoord"] = regel[2:].strip()
        elif regel.startswith("N:"):
            opgaven[-1][1][-1]["noot"] = regel[2:].strip()
    return titel, bron, context, [o for o in opgaven if o]


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
  .label {{ font-weight: 700; }}
  .noot {{ font-style: italic; font-size: 9.5pt; }}
  .context p {{ margin: 0 0 6px; }}
</style></head><body>
<h1>{titel}</h1>
<p class="bron">{bron}</p>
{context}
{inhoud}
</body></html>
"""


def bouw(pad):
    titel, bron, context, opgaven = lees(pad)
    contexthtml = ""
    if context:
        contexthtml = '<h2>Context</h2><div class="context">' + "".join(
            f'<p><span class="label">{html.escape(k.strip())}:</span> {html.escape(v.strip())}</p>'
            for k, v in context
        ) + "</div>"
    delen = []
    for opgave, vragen in opgaven:
        code = opgave.replace("Exercise ", "")
        delen.append(f"<h2>{html.escape(opgave)}</h2>")
        for v in vragen:
            kop = f"Question {code}.{v['label']}" if v["label"].isdigit() else f"{code} {v['label']}"
            noot = f'<p class="noot">{html.escape(v["noot"])}</p>' if v["noot"] else ""
            delen.append(
                f'<div class="vraag"><p class="label">{html.escape(kop)}</p>'
                f"<p>{html.escape(v['vraag'])}</p>"
                f'<p><span class="label">Model answer:</span> {html.escape(v["antwoord"])}</p>{noot}</div>'
            )
    htmlpad = pad.with_suffix(".html")
    htmlpad.write_text(
        SJABLOON.format(titel=html.escape(titel), bron=html.escape(bron), context=contexthtml, inhoud="\n".join(delen)),
        encoding="utf-8",
    )
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
