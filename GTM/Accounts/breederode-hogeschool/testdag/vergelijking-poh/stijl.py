# -*- coding: utf-8 -*-
"""Gedeelde opmaak voor de Breederode-documenten over de CAT POH-6.

Opmaakfamilie: het Breederode Go Live Plan (sectiebalken #0B4F6C, lichte vulling).
Letter Arial, kaarten om losse tekstblokken, lijnen in de tabellen, ruime witregels
tussen onderdelen. Vastgelegd na feedback van Dante op 30-09-2026.
"""
import base64, pathlib

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()

# ---------------------------------------------------------------- iconen
def ico(d):
    return (f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{d}</svg>')

I_HOOGTE = ico('<path d="M12 3v18"/><path d="M7.5 7.5L12 3l4.5 4.5"/><path d="M7.5 16.5L12 21l4.5-4.5"/>')
I_ZIEN   = ico('<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/>')
I_FORM   = ico('<rect x="4.5" y="4" width="15" height="17" rx="2"/><path d="M9 3.5h6v2.5H9z"/>'
               '<path d="M8.5 11h7"/><path d="M8.5 15h4.5"/>')
I_INZET  = ico('<path d="M6 3.5h8l4.5 4.5v12.5H6z"/><path d="M14 3.5V8h4.5"/>'
               '<path d="M9 14.5l2.3 2.3L15.5 12"/>')
I_ZAK    = ico('<path d="M12 3.5L21 19.5H3z"/><path d="M12 9.5v4.5"/><path d="M12 16.8v.2"/>')
I_BETER  = ico('<path d="M4 16.5L9.5 11l3.5 3.5L20 7.5"/><path d="M14.5 7.5H20v5.5"/>')

# ---------------------------------------------------------------- css
CSS = """
:root{
  --bar:#0B4F6C; --soft:#EEF3F5; --band:#D6E4EA; --kaart:#F7FAFB;
  --ink:#1C1C1C; --line:#C2D4DC; --raster:#DDE7EB; --muted:#4F6269;
}
@page{ size:A4; margin:15mm 15mm 14mm 15mm; }
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact; print-color-adjust:exact}
body{ font-family:Arial,Helvetica,sans-serif; color:var(--ink);
      font-size:9.8pt; line-height:1.5; margin:0; }

.head{display:flex;align-items:center;justify-content:space-between;margin:0 0 8mm 0}
.head img.b{height:13mm} .head img.e{height:6mm}
h1{font-size:16pt;font-weight:bold;margin:0 0 8mm 0;color:var(--bar);line-height:1.22}

section{margin:0 0 8mm 0}
section:last-child{margin-bottom:0}
section>.bar{background:var(--bar);color:#fff;font-weight:bold;font-size:10.5pt;
  padding:2mm 3.2mm;margin:0 0 4.5mm 0;break-after:avoid}

/* kaart: het enige omhulsel dat dit document kent, nooit genest */
.kaart{background:var(--kaart);border:1px solid var(--raster);border-radius:4px;
  padding:4mm 4.5mm;margin:0 0 4.5mm 0;break-inside:avoid}
.kaart:last-child{margin-bottom:0}
.kaart>*:last-child{margin-bottom:0}

p{margin:0 0 3.2mm 0} p:last-child{margin-bottom:0}
.lead{margin:0 0 4.5mm 0}
ul{margin:0 0 3.2mm 0;padding-left:5mm} li{margin:0 0 2.4mm 0}
ul:last-child{margin-bottom:0} li:last-child{margin-bottom:0}
h3{font-size:10pt;font-weight:bold;margin:0 0 2.6mm 0}
h3 .mv{font-weight:normal;color:var(--muted)}
h3 .ico{color:var(--bar);margin-right:1.6mm}
.ico{width:4.6mm;height:4.6mm;vertical-align:-0.9mm}
.q{margin:0}

/* vraag en antwoord */
.qa{display:grid;grid-template-columns:6.4mm 1fr;column-gap:3.2mm}
.qa .ico{width:5.6mm;height:5.6mm;color:var(--bar);margin-top:0.5mm}
.qa .vraag{font-weight:bold;color:var(--bar);margin:0 0 2.4mm 0}

/* tabellen met raster */
table{width:100%;table-layout:fixed;border-collapse:collapse;font-size:9.2pt;margin:0}
th{text-align:left;font-weight:bold;padding:1.6mm 2mm;background:var(--soft);
   border:1px solid var(--line);font-size:8.6pt;color:var(--bar)}
td{padding:2mm;border:1px solid var(--raster);vertical-align:middle}
th.p,td.p{text-align:right;width:15mm}
th.s,td.s{width:66mm;font-size:9pt}
th.sk,td.sk{width:24mm;text-align:center}
td.tr{padding:0}

/* het vakjesbandje */
.track{display:grid;grid-template-columns:repeat(4,1fr);height:7.4mm;align-items:stretch}
.track .c{position:relative;border-right:1px solid var(--raster)}
.track .c:last-child{border-right:none}
.track .c .vul{position:absolute;left:0;right:0;top:1.2mm;bottom:1.2mm;background:var(--band)}
.track .c.l .vul{left:1.2mm;border-radius:2.5mm 0 0 2.5mm}
.track .c.r .vul{right:1.2mm;border-radius:0 2.5mm 2.5mm 0}
.track .c.aanname .vul{background:none;border:1px dashed #8FAAB5}
.track .c.aanname.l .vul{border-right:none} .track .c.aanname.r .vul{border-left:none}
.track .dot{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  width:3.2mm;height:3.2mm;border-radius:50%;background:var(--bar);display:block}
.track .dot.leeg{background:#fff;border:1.2px solid var(--bar)}
.grens{position:relative}
.grens::after{content:"";position:absolute;left:0;top:-2.4mm;bottom:-2.4mm;border-left:2px solid var(--bar)}
tr.tot td{background:var(--soft);font-weight:bold}
table.oordeel th.s,table.oordeel td.s{width:52mm}
table.oordeel th.p,table.oordeel td.p{width:14mm;text-align:center}
td.p .nul{color:#B71C1C}
table.zonderpunten th.s,table.zonderpunten td.s{width:84mm}
table.zonderpunten th.sk,table.zonderpunten td.sk{width:24mm}
.legend .z{display:inline-block;width:0;height:3.4mm;border-left:2px solid var(--bar);
  vertical-align:-0.5mm;margin:0 1.4mm}

.legend{color:var(--muted);margin:0 0 4.5mm 0}
.legend .k{display:inline-block;width:7mm;height:3.2mm;background:var(--band);
  border-radius:1.6mm;vertical-align:-0.4mm;margin:0 0.6mm}
.legend .d{display:inline-block;width:2.8mm;height:2.8mm;border-radius:50%;
  background:var(--bar);vertical-align:-0.2mm;margin:0 0.6mm}

/* twee kolommen naast elkaar, binnen een kaart */
.vs{display:grid;grid-template-columns:1fr 1fr;column-gap:7mm;margin:0 0 3mm 0}
.vs>div:last-child{padding-left:7mm;border-left:1px solid var(--line);margin-left:-7mm}
.vs .lab{display:block;font-weight:bold;color:var(--bar);margin:0 0 1.6mm 0}
.vs p{margin:0}

/* balkenraster */
.kern{display:grid;grid-template-columns:78mm 1fr 9mm;column-gap:4mm;row-gap:2.6mm;align-items:center}
.kern .rail{height:4.6mm;background:#fff;border:1px solid var(--raster);border-radius:2.3mm;overflow:hidden}
.kern .fill{height:4.4mm;background:var(--bar);border-radius:2.2mm}
.kern .fill.licht{background:var(--band)}
.kern .val{text-align:right;font-weight:bold}
"""

# ---------------------------------------------------------------- bouwstenen
def sectie(titel, inhoud):
    return f'<section><div class="bar">{titel}</div>{inhoud}</section>'

def kaart(inhoud):
    return f'<div class="kaart">{inhoud}</div>'

def qa(icoon, vraag, *alineas):
    tekst = "".join(f"<p>{a}</p>" for a in alineas)
    return kaart(f'<div class="qa"><div>{icoon}</div><div><p class="vraag">{vraag}</p>{tekst}</div></div>')

def vs(links, rechts, links_lab="Beoordelingsformulier", rechts_lab="Eduface"):
    return (f'<div class="vs"><div><span class="lab">{links_lab}</span><p>{links}</p></div>'
            f'<div><span class="lab">{rechts_lab}</span><p>{rechts}</p></div></div>')

def rail(label, n, basis=16, licht=False):
    vulling = f'<div class="fill{" licht" if licht else ""}" style="width:{n/basis*100:.4g}%"></div>' if n else ""
    return (f'<div class="lb">{label}</div><div class="rail">{vulling}</div>'
            f'<div class="val">{n}</div>')

VAKJES = ["Onvoldoende", "Voldoende", "Goed", "Uitstekend"]
BAND = {4: (2, 3), 3: (1, 2), 2: (1, 2), 0: (0, 0)}

def track(woord, punten=None, grens=False):
    lo, hi = BAND[punten] if punten is not None else (None, None)
    aanname = " aanname" if punten == 3 else ""
    cellen = []
    for i, v in enumerate(VAKJES):
        cls, vul = [], ""
        if lo is not None and lo <= i <= hi:
            cls.append("band" + aanname)
            if i == lo: cls.append("l")
            if i == hi: cls.append("r")
            vul = '<span class="vul"></span>'
        if grens and i == 1:
            cls.append("grens")
        dot = '<span class="dot"></span>' if v == woord else ""
        cellen.append(f'<div class="c {" ".join(cls)}">{vul}{dot}</div>')
    return '<div class="track">' + "".join(cellen) + "</div>"

def pagina(titel, body, logo_b, logo_e):
    return f"""<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8">
<title>{titel}</title><style>{CSS}</style></head><body>
<div class="head">
  <img class="b" src="data:image/png;base64,{b64(logo_b)}" alt="Breederode Hogeschool">
  <img class="e" src="data:image/png;base64,{b64(logo_e)}" alt="Eduface">
</div>
<h1>{titel}</h1>
{body}
</body></html>"""
