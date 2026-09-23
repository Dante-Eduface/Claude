#!/usr/bin/env python3
"""Bouwt een printbaar vakdossier voor de Eduface-testdag en rendert het naar A4-PDF.

Gebruik:  python3 build.py data-mmt.py
Uitvoer:  out/<slug>-mapje.html en out/<slug>-mapje.pdf

Opzet volgens Design/System/core/ plus internal/. Geen Tailwind-build nodig:
de tokenwaarden staan hier als CSS-variabelen, gelijk aan core/tokens.css.
"""
import html
import importlib.util
import pathlib
import subprocess
import sys

HIER = pathlib.Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@import url("assets/fonts.css");

:root{
  --navy:#002333; --green-deep:#007b54;
  --ink-900:#0a2c3b; --ink-700:#2c4a57; --ink-500:#5b7480;
  --ink-300:#a9bcc4; --ink-200:#cdd9de; --ink-100:#e7eef0; --ink-50:#f3f7f8;
  --white:#fff;
  --font-sans:"Inter",system-ui,sans-serif;
  --font-display:"League Spartan",var(--font-sans);
}

@page{ size:A4; margin:0 }
*{ box-sizing:border-box }
html,body{ margin:0; padding:0 }
body{
  font-family:var(--font-sans); color:var(--navy);
  font-size:9.6pt; line-height:1.45;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
}

.blad{
  width:210mm; height:297mm; padding:16mm 15mm 11mm;
  display:flex; flex-direction:column; break-after:page; position:relative;
}
.blad:last-child{ break-after:auto }

/* ---- kop ---------------------------------------------------------------- */
.titel{
  font-family:var(--font-display); font-weight:700; font-size:19pt;
  letter-spacing:-.01em; margin:0 0 2mm;
}
.naamregel{
  display:flex; flex-wrap:wrap; gap:0 6mm;
  font-size:8.6pt; color:var(--ink-700);
  padding-bottom:2.5mm; border-bottom:1px solid var(--ink-200);
}
.naamregel b{ color:var(--navy); font-weight:600 }

.optie{
  margin-top:3mm; padding:3mm 3.5mm;
  background:var(--ink-50); border-radius:8px;
  font-size:8.6pt; line-height:1.4;
}
.optie div + div{ margin-top:1.2mm }
.optie b{ font-weight:600 }

h2{
  font-family:var(--font-display); font-weight:600; font-size:12pt;
  margin:6mm 0 2.5mm; letter-spacing:-.005em;
}
h2:first-of-type{ margin-top:5mm }
h3{
  font-family:var(--font-display); font-weight:600; font-size:10pt;
  margin:0 0 1.5mm;
}

/* ---- tabel -------------------------------------------------------------- */
table{ width:100%; border-collapse:collapse; font-size:9pt }
th{
  text-align:left; font-weight:600; font-size:8.2pt;
  color:var(--ink-700); padding:0 2.5mm 1.8mm 0;
  border-bottom:1.5px solid var(--navy); vertical-align:bottom;
}
td{
  padding:2mm 2.5mm 2mm 0; border-bottom:1px solid var(--ink-100);
  vertical-align:top;
}
td.c,th.c{ text-align:center; padding-right:0 }
.crit{ width:44% }
.gew{ width:8%; color:var(--ink-500) }
.uit{ width:22% }

tr.verschil td{ background:var(--ink-50) }
tr.verschil td.crit{ font-weight:600 }

.stand{ font-weight:500 }
.stand.niet{ color:var(--navy); font-weight:600 }
.stand.niet::before{ content:"\\2715\\00a0"; color:var(--ink-500) }
.stand.deels::before{ content:"\\00bd\\00a0"; color:var(--ink-500) }
.eens{ color:var(--green-deep); font-weight:600 }
.eens::before{
  content:""; display:inline-block; width:6px; height:6px; border-radius:50%;
  background:var(--green-deep); margin-right:2mm; vertical-align:middle;
}
.milder{ font-weight:600 }
.milder::before{ content:"\\2192\\00a0" }

/* ---- totalen ------------------------------------------------------------ */
.totalen{ display:flex; gap:4mm; margin-top:4mm }
.totaal{
  flex:1; padding:3mm 3.5mm; border:1px solid var(--ink-200); border-radius:8px;
}
.totaal .cijfer{
  font-family:var(--font-display); font-weight:700; font-size:16pt;
  line-height:1.1; display:block;
}
.totaal .wat{ font-size:8pt; color:var(--ink-700); margin-top:1mm; display:block }

/* ---- citaat ------------------------------------------------------------- */
.citaat{
  border-left:2.5px solid var(--navy); padding:0 0 0 3.5mm;
  margin:2.5mm 0 0; font-size:9pt; line-height:1.5;
}
.detail{ font-size:8.6pt; color:var(--ink-700); margin-top:2mm }

/* ---- feedbackblokken --------------------------------------------------- */
.fb{ margin-bottom:3.2mm }
.fb .kop{
  font-family:var(--font-display); font-weight:600; font-size:9.2pt;
  margin-bottom:.8mm;
}
.fb p{ margin:0; font-size:8.8pt; line-height:1.42 }

/* ---- divergentie / aanname -------------------------------------------- */
.plek{
  border:1px solid var(--ink-200); border-radius:10px;
  padding:3.5mm 4mm; margin-bottom:3.5mm;
}
.plek .bovenop{
  display:flex; justify-content:space-between; align-items:baseline;
  gap:4mm; margin-bottom:2mm;
}
.plek .bovenop h3{ margin:0 }
.regel{ display:flex; gap:3mm; font-size:8.8pt; margin-top:1.8mm }
.regel .wie{
  flex:0 0 26mm; color:var(--ink-700); font-weight:600;
}
.regel .wat{ flex:1; line-height:1.42 }
.regel .wat.leeg{ color:var(--ink-500); font-style:italic }
.vraag{
  margin-top:3mm; padding:2.8mm 3.2mm;
  background:var(--ink-50); border-radius:8px;
  font-size:9pt; line-height:1.45;
}
.vraag b{ font-weight:600 }

/* ---- schrijfruimte ----------------------------------------------------- */
.lijnen{
  margin-top:auto; padding-top:3mm;
  flex:1 1 auto; display:flex; flex-direction:column; min-height:0;
}
.lijnen .label{
  font-size:8pt; color:var(--ink-700); font-weight:600; margin-bottom:2mm;
}
.lijnen .veld{
  flex:1 1 auto;
  background-image:repeating-linear-gradient(
    to bottom, transparent 0 28px, var(--ink-200) 28px 29px);
}

/* ---- voet -------------------------------------------------------------- */
.voet{
  position:absolute; left:15mm; right:15mm; bottom:6mm;
  display:flex; justify-content:space-between;
  font-size:7.6pt; color:var(--ink-500);
  padding-top:2mm; border-top:1px solid var(--ink-100);
}

/* ---- blanco formulier -------------------------------------------------- */
.leeg-crit td{ padding:2.6mm 2.5mm }
.vak{
  display:inline-block; width:5mm; height:5mm;
  border:1px solid var(--ink-300); border-radius:3px; vertical-align:middle;
}
.toelichting{
  height:11mm;
  background-image:repeating-linear-gradient(
    to bottom, transparent 0 20px, var(--ink-200) 20px 21px);
}
"""


def e(s):
    return html.escape(str(s))


def stand_cel(w):
    if w == "voldaan":
        return '<span class="stand">voldaan</span>'
    if w == "deels":
        return '<span class="stand deels">deels</span>'
    return '<span class="stand niet">niet voldaan</span>'


def uitkomst(nak, mod):
    if nak == mod:
        return "eens", '<span class="eens">eens</span>'
    if nak in ("niet voldaan", "deels") and mod == "voldaan":
        return "milder", '<span class="milder">model milder</span>'
    return "strenger", '<span class="milder">model strenger</span>'


def voet(vak, n, totaal):
    return (f'<div class="voet"><span>Mapje: {e(vak["opleiding"])}</span>'
            f'<span>pagina {n} van {totaal}</span></div>')


def lijnen(label, hoogte_mm):
    return (f'<div class="lijnen"><div class="label">{e(label)}</div>'
            f'<div class="veld" style="min-height:{hoogte_mm}mm"></div></div>')


def blad1(vak, s, n, totaal, eerste):
    kop = ""
    if eerste:
        kop = f'<div class="titel">Eduface testdag</div>'
    rijen = []
    eens_n = 0
    nak_n = 0
    mod_n = 0
    for i, (crit, gew) in enumerate(vak["criteria"]):
        nak, mod = s["nakijker"][i], s["model"][i]
        soort, cel = uitkomst(nak, mod)
        if soort == "eens":
            eens_n += 1
        if nak == "voldaan":
            nak_n += 1
        if mod == "voldaan":
            mod_n += 1
        cls = ' class="verschil"' if soort != "eens" else ""
        rijen.append(
            f'<tr{cls}><td class="crit">{e(crit)}</td><td class="gew c">{e(gew)}</td>'
            f'<td class="c">{stand_cel(nak)}</td><td class="c">{stand_cel(mod)}</td>'
            f'<td class="uit">{cel}</td></tr>')
    n_crit = len(vak["criteria"])
    return f"""<section class="blad">
{kop}
<div class="naamregel">
  <span><b>Opleiding</b> {e(vak["opleiding"])}</span>
  <span><b>Vak</b> {e(vak["vak"])}</span>
  <span><b>Student</b> {e(s["label"])}</span>
  <span><b>Beoordeeld op</b> {e(s["datum_beoordeling"])}</span>
</div>
<div class="optie">
  <div><b>Gekozen</b> {e(vak["optie_gekozen"])}</div>
  <div><b>Wat dat doet</b> {e(vak["optie_doet"])}</div>
</div>

<h2>De beoordeling naast elkaar</h2>
<table>
<thead><tr><th class="crit">Criterium</th><th class="gew c">Gewicht</th>
<th class="c">Nakijker</th><th class="c">Eduface</th><th class="uit">Uitkomst</th></tr></thead>
<tbody>{''.join(rijen)}</tbody>
</table>

<div class="totalen">
  <div class="totaal"><span class="cijfer">{nak_n} van {n_crit}</span>
    <span class="wat">voldaan bij de nakijker</span></div>
  <div class="totaal"><span class="cijfer">{mod_n} van {n_crit}</span>
    <span class="wat">voldaan bij Eduface</span></div>
  <div class="totaal"><span class="cijfer">{eens_n} van {n_crit}</span>
    <span class="wat">criteria waarop ze het eens zijn</span></div>
</div>

<h2>Wat de nakijker schreef</h2>
<p class="citaat">{e(s["nakijker_feedback"])}</p>
<p class="detail">{e(s["nakijker_detail"])} Eindoordeel van de nakijker:
{e(s["nakijker_eindoordeel"])}. Eindoordeel van Eduface: {e(s["model_eindoordeel"])}.</p>

{lijnen("Aantekeningen", 32)}
{voet(vak, n, totaal)}
</section>"""


def blad2(vak, s, n, totaal):
    blokken = "".join(
        f'<div class="fb"><div class="kop">{i+1}. {e(crit)}</div>'
        f'<p>{e(s["model_feedback"][i])}</p></div>'
        for i, (crit, _) in enumerate(vak["criteria"]))
    return f"""<section class="blad">
<div class="naamregel"><span><b>Feedback van Eduface</b></span>
<span>{e(vak["vak"])}</span><span>{e(s["label"])}</span></div>
<h2>Per criterium, letterlijk</h2>
{blokken}
{voet(vak, n, totaal)}
</section>"""


def plek_blok(d):
    rub = (f'<div class="wat">{e(d["rubriek"])}</div>' if d["rubriek"]
           else f'<div class="wat leeg">{e(d["rubriek_reden"])}</div>')
    return f"""<div class="plek">
  <div class="bovenop"><h3>{e(d["criterium"])}</h3>
    <span class="milder">{e(d["uitkomst"])}</span></div>
  <div class="regel"><div class="wie">Nakijker</div><div class="wat">{e(d["nakijker"])}</div></div>
  <div class="regel"><div class="wie">Eduface</div><div class="wat">{e(d["model"])}</div></div>
  <div class="regel"><div class="wie">Rubriek</div>{rub}</div>
  <div class="vraag">{e(d["vraag"])}</div>
</div>"""


def blad3(vak, s, n, totaal):
    return f"""<section class="blad">
<div class="naamregel"><span><b>Waar het uiteenloopt</b></span>
<span>{e(vak["vak"])}</span><span>{e(s["label"])}</span></div>
<h2>De plekken met een verschil</h2>
{''.join(plek_blok(d) for d in s["divergenties"])}
{lijnen("Aantekeningen", 26)}
{voet(vak, n, totaal)}
</section>"""


def aanname_blok(a):
    return f"""<div class="plek">
  <h3>{e(a["kop"])}</h3>
  <div class="regel"><div class="wie">Eduface zegt</div><div class="wat">{e(a["model"])}</div></div>
  <div class="regel"><div class="wie">De rubriek zegt</div><div class="wat">{e(a["rubriek"])}</div></div>
  <div class="regel"><div class="wie">In de praktijk</div><div class="wat">{e(a["nakijker"])}</div></div>
  <div class="vraag">{e(a["vraag"])}</div>
</div>"""


def blad4(vak, s, n, totaal):
    return f"""<section class="blad">
<div class="naamregel"><span><b>Aannames van het model</b></span>
<span>{e(vak["vak"])}</span><span>{e(s["label"])}</span></div>
<h2>Wat het model aanneemt, en wat jullie willen</h2>
{''.join(aanname_blok(a) for a in s["aannames"])}
{lijnen("Antwoorden en aanvullingen", 44)}
{voet(vak, n, totaal)}
</section>"""


def blanco(vak, ander, n, totaal):
    standen = ander["standen"]
    kopjes = "".join(f'<th class="c">{e(x)}</th>' for x in standen)
    rijen = "".join(
        f'<tr class="leeg-crit"><td class="crit">{i+1}. {e(c)}</td>'
        + "".join('<td class="c"><span class="vak"></span></td>' for _ in standen)
        + '<td><div class="toelichting"></div></td></tr>'
        for i, c in enumerate(ander["criteria"]))
    return f"""<section class="blad">
<div class="naamregel"><span><b>Beoordelingsformulier</b></span>
<span>{e(ander["opleiding"])}</span><span>{e(ander["vak"])}</span>
<span><b>Student</b> ................</span></div>
<div class="optie"><div><b>Gekozen</b> {e(ander["optie_gekozen"])}</div></div>
<h2>Per criterium</h2>
<table>
<thead><tr><th class="crit">Criterium</th>{kopjes}<th>Toelichting</th></tr></thead>
<tbody>{rijen}</tbody>
</table>
{lijnen("Opmerkingen over het geheel", 22)}
{voet(vak, n, totaal)}
</section>"""


def bouw(mod):
    vak, studenten, andere = mod.VAK, mod.STUDENTEN, mod.ANDERE_VAKKEN
    totaal = len(studenten) * 4 + len(andere)
    bladen, n = [], 1
    for idx, s in enumerate(studenten):
        bladen.append(blad1(vak, s, n, totaal, idx == 0)); n += 1
        bladen.append(blad2(vak, s, n, totaal)); n += 1
        bladen.append(blad3(vak, s, n, totaal)); n += 1
        bladen.append(blad4(vak, s, n, totaal)); n += 1
    for ander in andere:
        bladen.append(blanco(vak, ander, n, totaal)); n += 1
    return (f'<!doctype html><html lang="nl"><head><meta charset="utf-8">'
            f'<title>Eduface testdag, {e(vak["opleiding"])}</title>'
            f'<style>{CSS}</style></head><body>{"".join(bladen)}</body></html>'), totaal


def main():
    spec = importlib.util.spec_from_file_location("data", HIER / sys.argv[1])
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    slug = sys.argv[1].replace("data-", "").replace(".py", "")
    uit = HIER / "out"
    uit.mkdir(exist_ok=True)
    htm, totaal = bouw(mod)
    hpad = uit / f"{slug}-mapje.html"
    hpad.write_text(htm)

    ppad = uit / f"{slug}-mapje.pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={ppad}",
                    "--virtual-time-budget=6000", hpad.as_uri()],
                   check=True, capture_output=True)
    print(f"{ppad}  ({totaal} bladen)")


if __name__ == "__main__":
    main()
