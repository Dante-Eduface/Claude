"""Maakt de twee pdf's van de verkorte dissertation uit dissertation-verkort.md.

Draaien: python3 build.py   (eenmalig: pip install markdown fonttools)

Alleen wat tussen <!-- pdf:opdracht --> en <!-- pdf:formulier --> staat gaat de
pdf in, de notities voor Eduface eromheen niet. Tekst aanpassen doe je in de .md,
nooit in de pdf. De gewichten staan twee keer in de bron (tabel in de opdracht,
kop per criterium in het formulier), dus het script stopt als die uiteenlopen.

Opmaak volgens Design/System: core/ volledig, type-schaal geleend van web/
(bodyschaal, geen heroformaten), want dit is een document op armlengte. Papier,
dus geen kleur als enige drager en blokken die niet over een pagina breken.
"""
import base64
import io
import re
import subprocess
from datetime import date
from pathlib import Path
from string import Template

import markdown
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

HIER = Path(__file__).resolve().parent
REPO = HIER.parents[2]
BRON = HIER / "dissertation-verkort.md"
FONTS = REPO / "Design" / "Merk" / "fonts"
CHROMIUM = "/opt/pw-browsers/chromium"

MAANDEN = ["januari", "februari", "maart", "april", "mei", "juni", "juli",
           "augustus", "september", "oktober", "november", "december"]

# Waarden uit Design/System. Hier niets verzinnen, alleen overnemen.
TOKENS = {
    # core/tokens.css, semantisch
    "foreground": "#002333",      # --color-foreground (ink-950)
    "background": "#ffffff",      # --color-background
    "border": "#e7eef0",          # --color-border (ink-100)
    "border_strong": "#cdd9de",   # --color-border-strong (ink-200)
    # web/tokens.css, tekst- en display-schaal
    "display_sm": "2rem",         # --text-display-sm, lh 1.1, tracking -0.01em, 600
    "text_xl": "1.25rem",         # --text-xl, lh 1.4
    "text_base": "1rem",          # --text-base, lh 1.6
    "text_xs": "0.75rem",         # --text-xs, lh 1.4
    # regels.md, 8pt-familie
    "s1": "8px", "s2": "16px", "s3": "24px", "s4": "32px",
    "s6": "48px", "s8": "64px", "s12": "96px",
}

CSS = Template("""
@font-face { font-family: "Inter"; src: url("$inter_400") format("truetype");
  font-weight: 400; font-style: normal; }
@font-face { font-family: "Inter"; src: url("$inter_600") format("truetype");
  font-weight: 600; font-style: normal; }
@font-face { font-family: "League Spartan"; src: url("$spartan_600") format("truetype");
  font-weight: 600; font-style: normal; }

@page {
  size: A4;
  margin: $s8 $s12 $s12 $s12;
  @bottom-left { content: "$voet"; font-family: "Inter"; font-size: $text_xs;
    color: $foreground; vertical-align: top; padding-top: $s3; }
  @bottom-right { content: "pagina " counter(page) " van " counter(pages);
    font-family: "Inter"; font-size: $text_xs; color: $foreground;
    vertical-align: top; padding-top: $s3; }
}

html { -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }
body { margin: 0; background: $background; color: $foreground;
  font-family: "Inter", ui-sans-serif, system-ui, sans-serif;
  font-size: $text_base; line-height: 1.6; font-weight: 400; }
h1, h2 { font-family: "League Spartan", "Inter", sans-serif; font-weight: 600;
  color: $foreground; text-wrap: balance; margin: 0; }
h1 { font-size: $display_sm; line-height: 1.1; letter-spacing: -0.01em; }
h2 { font-size: $text_xl; line-height: 1.4; break-after: avoid; }
p { text-wrap: pretty; }
strong { font-weight: 600; }

/* Eén eigenaar per witruimte: de documentstroom zet de afstanden. */
.doc > * { margin: 0; }
.doc > * + * { margin-top: $s2; }
.doc > .blok, .doc > .criterium { margin-top: $s4; }
.blok { break-inside: avoid; }
.blok > * { margin: 0; }
.blok > * + * { margin-top: $s2; }
.blok > h2 + * { margin-top: $s1; }
.doc > .ondertitel { margin-top: $s1; }
.doc > .ondertitel + * { margin-top: $s6; }

ul, ol { padding-left: $s3; }
li + li { margin-top: $s1; }

table { width: 100%; border-collapse: collapse; }
tr { break-inside: avoid; }
th, td { text-align: left; vertical-align: top; padding: $s1 $s2 $s1 0; }
th:last-child, td:last-child { padding-right: 0; }
th { font-weight: 600; border-bottom: 1px solid $border_strong; }
td { border-bottom: 1px solid $border; }
th[style*="right"], td[style*="right"] { white-space: nowrap;
  font-variant-numeric: tabular-nums; }

.criterium { break-inside: avoid; border-top: 1px solid $border_strong; padding-top: $s2; }
.criterium-kop { display: flex; justify-content: space-between; align-items: baseline;
  gap: $s2; }
.gewicht { font-family: "League Spartan", "Inter", sans-serif; font-size: $text_xl;
  line-height: 1.4; font-weight: 600; font-variant-numeric: tabular-nums;
  white-space: nowrap; }
.eisen { display: grid; grid-template-columns: max-content 1fr; column-gap: $s3;
  row-gap: $s2; margin: $s2 0 0; }
.eisen dt { font-weight: 600; }
.eisen dd { margin: 0; }
.eisen ul { margin: 0; padding-left: 0; }
""")

HTML = Template("""<!doctype html>
<html lang="nl"><head><meta charset="utf-8"><title>$titel</title>
<style>$css</style></head>
<body><main class="doc">
$inhoud
</main></body></html>
""")


def deel(tekst, naam):
    gevonden = re.search(rf"<!-- pdf:{naam} -->\n(.*?)\n<!-- /pdf:{naam} -->", tekst, re.S)
    if not gevonden:
        raise SystemExit(f"markering pdf:{naam} niet gevonden in {BRON.name}")
    return gevonden.group(1).strip()


def kop_omhoog(md):
    """## wordt #, ### wordt ##: in de pdf is de documenttitel de h1."""
    return re.sub(r"^#(#+) ", r"\1 ", md, flags=re.M)


def ontsnap(tekst):
    return tekst.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(tekst):
    tekst = ontsnap(tekst)
    tekst = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", tekst)
    return re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"<em>\1</em>", tekst)


def titelblok(md):
    """Eerste kop plus de cursieve regel eronder. Geeft (titel, ondertitel, rest)."""
    gevonden = re.match(r"# (.+)\n+_(.+)_\n+(.*)", md, re.S)
    if not gevonden:
        raise SystemExit("verwacht een titel met daaronder een cursieve ondertitel")
    return gevonden.group(1).strip(), gevonden.group(2).strip(), gevonden.group(3)


def opdracht_html(md):
    titel, ondertitel, rest = titelblok(kop_omhoog(md))
    body = markdown.markdown(rest, extensions=["tables", "smarty"])
    body = "\n".join(f"<section class=\"blok\">{stuk.strip()}</section>"
                     for stuk in re.split(r"(?=<h2>)", body) if stuk.strip())
    kop = f"<h1>{ontsnap(titel)}</h1>\n<p class=\"ondertitel\">{inline(ondertitel)}</p>"
    return titel, kop + "\n" + body


def lees_criteria(md):
    """[(nummer, naam, gewicht, [voldoende-regels], onvoldoende), ...]"""
    criteria = []
    for blok in re.split(r"^### ", md, flags=re.M)[1:]:
        kop, _, rest = blok.partition("\n")
        gevonden = re.fullmatch(r"(\d+)\. (.+) \((\d+)%\)", kop.strip())
        voldoende = re.search(r"\*\*Voldoende:\*\*\n((?:- .+\n?)+)", rest)
        onvoldoende = re.search(r"\*\*Onvoldoende:\*\* (.+)", rest)
        if not (gevonden and voldoende and onvoldoende):
            raise SystemExit(f"criterium niet te lezen: {kop.strip()}")
        regels = [r[2:].strip() for r in voldoende.group(1).strip().splitlines()]
        criteria.append((gevonden.group(1), gevonden.group(2), int(gevonden.group(3)),
                         regels, onvoldoende.group(1).strip()))
    return criteria


def formulier_html(md, criteria):
    titel, ondertitel, _ = titelblok(kop_omhoog(md))
    delen = [f"<h1>{ontsnap(titel)}</h1>", f"<p class=\"ondertitel\">{inline(ondertitel)}</p>"]
    for nummer, naam, gewicht, regels, onvoldoende in criteria:
        lijst = "".join(f"<li>{inline(r)}</li>" for r in regels)
        delen.append(
            f"<section class=\"criterium\">"
            f"<div class=\"criterium-kop\"><h2>{nummer}. {ontsnap(naam)}</h2>"
            f"<span class=\"gewicht\">{gewicht}%</span></div>"
            f"<dl class=\"eisen\"><dt>Voldoende</dt><dd><ul>{lijst}</ul></dd>"
            f"<dt>Onvoldoende</dt><dd>{inline(onvoldoende)}</dd></dl></section>")
    return titel, "\n".join(delen)


def controleer(opdracht_md, formulier_md, criteria):
    """De gewichten moeten in beide documenten gelijk zijn en optellen tot 100."""
    tabel = {naam.strip().lower(): int(pct) for naam, pct in
             re.findall(r"^\| ([^|]+?) \| (\d+)% \|$", opdracht_md, flags=re.M)}
    formulier = {naam.lower(): gewicht for _, naam, gewicht, _, _ in criteria}
    if tabel != formulier:
        raise SystemExit(f"gewichten lopen uiteen:\nopdracht  {tabel}\nformulier {formulier}")
    if sum(formulier.values()) != 100:
        raise SystemExit(f"gewichten tellen op tot {sum(formulier.values())}, niet 100")
    for naam, md in (("opdracht", opdracht_md), ("formulier", formulier_md)):
        if re.search("[\u2013\u2014]", md):
            raise SystemExit(f"streepje (en- of em-dash) in de {naam}, herschrijf de zin")


def font_url(bestand, gewicht):
    """Vast gewicht uit het variabele merkfont. Een variabel font zet Chromium
    als Type 3 in de pdf, en dat rendert in sommige viewers wazig."""
    font = TTFont(FONTS / bestand)
    ligging = {a.axisTag: a.defaultValue for a in font["fvar"].axes}
    ligging["wght"] = gewicht  # overige assen (Inter heeft ook opsz) op hun standaard
    font = instantiateVariableFont(font, ligging)
    buffer = io.BytesIO()
    font.save(buffer)
    return "data:font/ttf;base64," + base64.b64encode(buffer.getvalue()).decode()


def bouw_pdf(titel, inhoud, voet, pad):
    css = CSS.substitute(TOKENS, voet=voet,
                         inter_400=font_url("Inter-Regular.ttf", 400),
                         inter_600=font_url("Inter-Regular.ttf", 600),
                         spartan_600=font_url("LeagueSpartan-Bold.ttf", 600))
    pad_html = pad.with_suffix(".html")
    pad_html.write_text(HTML.substitute(titel=ontsnap(titel), css=css, inhoud=inhoud),
                        encoding="utf-8")
    try:
        subprocess.run(
            [CHROMIUM, "--headless", "--disable-gpu", "--no-sandbox",
             "--no-pdf-header-footer", f"--print-to-pdf={pad}", pad_html.as_uri()],
            check=True, capture_output=True, timeout=180)
    finally:
        pad_html.unlink(missing_ok=True)
    info = subprocess.run(["pdfinfo", str(pad)], capture_output=True, text=True).stdout
    paginas = re.search(r"Pages:\s+(\d+)", info)
    print(f"{pad.name}: {paginas.group(1) if paginas else '?'} pagina's")


if __name__ == "__main__":
    tekst = BRON.read_text(encoding="utf-8")
    opdracht_md, formulier_md = deel(tekst, "opdracht"), deel(tekst, "formulier")
    criteria = lees_criteria(formulier_md)
    controleer(opdracht_md, formulier_md, criteria)

    vandaag = date.today()
    versie = f"versie {vandaag.day} {MAANDEN[vandaag.month - 1]} {vandaag.year}"

    titel, inhoud = opdracht_html(opdracht_md)
    bouw_pdf(titel, inhoud, f"{titel} · {versie}",
             HIER / "dissertation-verkort-opdracht.pdf")

    titel, inhoud = formulier_html(formulier_md, criteria)
    bouw_pdf(titel, inhoud, f"{titel} dissertation (verkorte versie) · {versie}",
             HIER / "dissertation-verkort-beoordelingsformulier.pdf")
