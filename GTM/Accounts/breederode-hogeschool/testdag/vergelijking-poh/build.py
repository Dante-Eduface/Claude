# -*- coding: utf-8 -*-
"""Bouwt het vergelijkingsdocument CAT POH-6 voor Kas van Kruining en Selma de Nijs.

Opmaak volgt het Breederode Go Live Plan (sectiebalken, lichte vulling),
compositie en informatiedichtheid volgen Design/System/core.
Letter: Arial, op verzoek van Dante (30-09-2026).
"""
import base64, pathlib

H = pathlib.Path(".")
def b64(p): return base64.b64encode((H / p).read_bytes()).decode()

# ---------------------------------------------------------------- iconen
def ico(d, extra=""):
    return (f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{d}{extra}</svg>')

I_HOOGTE = ico('<path d="M12 3v18"/><path d="M7.5 7.5L12 3l4.5 4.5"/><path d="M7.5 16.5L12 21l4.5-4.5"/>')
I_ZIEN   = ico('<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/>')
I_FORM   = ico('<rect x="4.5" y="4" width="15" height="17" rx="2"/><path d="M9 3.5h6v2.5H9z"/>'
               '<path d="M8.5 11h7"/><path d="M8.5 15h4.5"/>')
I_INZET  = ico('<path d="M6 3.5h8l4.5 4.5v12.5H6z"/><path d="M14 3.5V8h4.5"/>'
               '<path d="M9 14.5l2.3 2.3L15.5 12"/>')

# ---------------------------------------------------------------- css
CSS = """
:root{
  --bar:#0B4F6C; --soft:#EEF3F5; --band:#DCE8ED;
  --ink:#1C1C1C; --line:#C7D6DD; --muted:#4F6269;
}
@page{ size:A4; margin:15mm 15mm 14mm 15mm; }
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact; print-color-adjust:exact}
body{ font-family:Arial,Helvetica,sans-serif; color:var(--ink);
      font-size:9.8pt; line-height:1.48; margin:0; }

/* kop van het document */
.head{display:flex;align-items:center;justify-content:space-between;margin:0 0 7mm 0}
.head img.b{height:13mm} .head img.e{height:6mm}
h1{font-size:16pt;font-weight:bold;margin:0 0 6mm 0;color:var(--bar);line-height:1.22}

/* secties: balk, daaronder lucht in plaats van een kader */
section{break-inside:auto; margin:0 0 6mm 0}
section>.bar{background:var(--bar);color:#fff;font-weight:bold;font-size:10.5pt;
  padding:1.8mm 3mm;margin:0 0 3.2mm 0;break-after:avoid}
p{margin:0 0 3mm 0} p:last-child{margin-bottom:0}
.lead{max-width:60em}

/* de drie antwoorden bovenaan */
.qa{display:grid;grid-template-columns:6mm 1fr;column-gap:3mm;margin:0 0 5mm 0;break-inside:avoid}
.qa:last-child{margin-bottom:0}
.qa .ico{width:5.4mm;height:5.4mm;color:var(--bar);margin-top:0.6mm}
.qa .vraag{font-weight:bold;color:var(--bar);margin:0 0 1.4mm 0}
.qa p{margin:0 0 2mm 0} .qa p:last-child{margin-bottom:0}

/* bandtabel */
table{width:100%;table-layout:fixed;border-collapse:collapse;font-size:9.2pt;margin:0 0 2.4mm 0}
caption{caption-side:top;text-align:left;font-weight:bold;padding:0 0 2mm 0;font-size:9.8pt}
th{text-align:left;font-weight:bold;padding:0 0 1.6mm 0;border-bottom:1px solid var(--line);
   font-size:8.6pt;color:var(--muted)}
td{padding:1.5mm 0;border-bottom:1px solid #E8EEF1;vertical-align:middle}
tr:last-child td{border-bottom:none}
th.p,td.p{text-align:right;width:14mm;padding-right:6mm}
th.s,td.s{width:70mm;font-size:9pt}
th.sk,td.sk{width:24mm}
.sk{text-align:center;font-size:8.6pt;color:var(--muted);font-weight:bold;
    padding:0 0 1.6mm 0;border-bottom:1px solid var(--line)}

.track{display:grid;grid-template-columns:repeat(4,1fr);height:5mm;align-items:center}
.track .c{height:5mm;position:relative}
.track .c.band{background:var(--band)}
.track .c.l{border-radius:2.5mm 0 0 2.5mm} .track .c.r{border-radius:0 2.5mm 2.5mm 0}
.track .c.aanname{background:none;border-top:1px dashed #9FB6BF;border-bottom:1px dashed #9FB6BF}
.track .c.aanname.l{border-left:1px dashed #9FB6BF} .track .c.aanname.r{border-right:1px dashed #9FB6BF}
.track .dot{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);
  width:3mm;height:3mm;border-radius:50%;background:var(--bar);display:block}
tr.tot td{padding-top:2.6mm;font-weight:bold;border-bottom:none}

/* twee kolommen naast elkaar */
.vs{display:grid;grid-template-columns:1fr 1fr;column-gap:7mm;margin:0 0 2.4mm 0}
.vs>div:last-child{padding-left:7mm;border-left:1px solid var(--line);margin-left:-7mm}
.vs .lab{display:block;font-weight:bold;color:var(--bar);margin:0 0 1.4mm 0}
.vs p{margin:0}
h3{font-size:10pt;font-weight:bold;margin:0 0 2mm 0}
h3 .mv{font-weight:normal;color:var(--muted)}
.verschil{break-inside:avoid;margin:0 0 4.6mm 0}
.verschil:last-child{margin-bottom:0}
.q{margin:0}
ul{margin:0 0 3mm 0;padding-left:5mm} li{margin:0 0 1.8mm 0} ul:last-child{margin-bottom:0}
li:last-child{margin-bottom:0}
.ico{width:4.4mm;height:4.4mm;vertical-align:-0.8mm}
.legend{font-size:9pt;color:var(--muted);margin:0 0 3.4mm 0}
/* kernbeeld: vier uitkomsten op een raster van zestien */
.kern{display:grid;grid-template-columns:78mm 1fr 9mm;column-gap:4mm;row-gap:2.2mm;align-items:center;
  margin:0 0 3mm 0}
.kern .lb{font-size:9.4pt}
.kern .rail{height:4.4mm;background:var(--soft);border-radius:2.2mm;overflow:hidden}
.kern .fill{height:4.4mm;background:var(--bar);border-radius:2.2mm}
.kern .fill.licht{background:var(--band)}
.kern .val{text-align:right;font-weight:bold;font-size:9.4pt}
.kern .val.nul{color:var(--bar)}
h3 .ico{color:var(--bar);margin-right:1.4mm}
.legend .k{display:inline-block;width:6mm;height:3mm;background:var(--band);
  border-radius:1.5mm;vertical-align:-0.3mm;margin:0 0.6mm}
.legend .d{display:inline-block;width:2.6mm;height:2.6mm;border-radius:50%;
  background:var(--bar);vertical-align:-0.2mm;margin:0 0.6mm}
"""

# ---------------------------------------------------------------- bandtabel
VAKJES = ["Onvoldoende", "Voldoende", "Goed", "Uitstekend"]
BAND = {4: (2, 3), 3: (1, 2), 2: (1, 2), 0: (0, 0)}   # 3 punten bestaat niet op het formulier

def track(punten, woord):
    lo, hi = BAND[punten]
    aanname = " aanname" if punten == 3 else ""
    cellen = []
    for i, v in enumerate(VAKJES):
        cls = []
        if lo <= i <= hi:
            cls.append("band" + aanname)
            if i == lo: cls.append("l")
            if i == hi: cls.append("r")
        dot = '<span class="dot"></span>' if v == woord else ""
        cellen.append(f'<div class="c {" ".join(cls)}">{dot}</div>')
    return '<div class="track">' + "".join(cellen) + "</div>"

def bandtabel(caption, rijen, totaal):
    kop = "".join(f'<th class="sk">{v}</th>' for v in VAKJES)
    body = ""
    for naam, punten, woord in rijen:
        body += (f'<tr><td class="s">{naam}</td><td class="p">{punten}</td>'
                 f'<td colspan="4">{track(punten, woord)}</td></tr>')
    return (f'<table><caption>{caption}</caption><thead><tr>'
            f'<th class="s">Criterium</th><th class="p">Punten</th>{kop}</tr></thead>'
            f'<tbody>{body}<tr class="tot"><td class="s">{totaal}</td>'
            f'<td class="p"></td><td colspan="4"></td></tr></tbody></table>')

C = ["1. Aanleiding van de klinische vraag",
     "2. Onderzoeksvraag op basis van PICO",
     "3. Databanken en weging van informatie",
     "4. Analyse binnen de praktijkcontext",
     "5. Conclusie uit de resultaten",
     "6. Kritische inhoudelijke discussie",
     "7. Klinische relevantie en toepasbaarheid",
     "8. Reflectie en rolontwikkeling"]

S1 = list(zip(C, [4, 4, 2, 4, 2, 4, 2, 4],
              ["Goed", "Goed", "Goed", "Goed", "Voldoende", "Goed", "Voldoende", "Goed"]))
S2 = list(zip(C, [4, 2, 2, 2, 2, 4, 4, 3],
              ["Goed", "Voldoende", "Goed", "Voldoende", "Goed", "Uitstekend", "Goed", "Voldoende"]))

# ---------------------------------------------------------------- bouwstenen
def sectie(titel, inhoud):
    return f'<section><div class="bar">{titel}</div>{inhoud}</section>'

def qa(icoon, vraag, *alineas):
    tekst = "".join(f"<p>{a}</p>" for a in alineas)
    return f'<div class="qa"><div>{icoon}</div><div><p class="vraag">{vraag}</p>{tekst}</div></div>'

def verschil(kop, mv, links, rechts, vraag):
    return (f'<div class="verschil"><h3>{kop} <span class="mv">{mv}</span></h3>'
            f'<div class="vs"><div><span class="lab">Beoordelingsformulier</span><p>{links}</p></div>'
            f'<div><span class="lab">Eduface</span><p>{rechts}</p></div></div>'
            f'<p class="q">{vraag}</p></div>')

# ---------------------------------------------------------------- pagina 1
antwoorden = sectie("Jullie drie vragen, hier beantwoord", (
  qa(I_HOOGTE,
     "Kas: kwam mijn feedback overeen met die van het model, of zaten er duidelijke verschillen in?",
     "<b>Over de vraag of iets geslaagd is, zijn jullie het zestien van de zestien keer eens.</b> "
     "Bij geen enkel criterium, bij geen van de twee inzendingen, komt het model onder jouw punten uit. "
     "Er is dus geen inzending en geen criterium waarover jullie het oneens zijn over voldoen.",
     "<b>Het verschil zit in de hoogte, en het is systematisch.</b> Van de vijftien criteria die je 4 of 2 punten gaf, "
     "koos het model elf keer het laagste van de twee vakjes die bij die punten passen, en vier keer het hoogste. "
     "Waar jij 4 punten gaf, kwam het model zeven keer op Goed en een keer op Uitstekend. "
     "Drie verschillen zijn groot genoeg om uit te werken: criterium 3, 5 en 7. Die staan op pagina&nbsp;3.")
  + qa(I_ZIEN,
     "Kas: kan ik hier als examinator iets van leren?",
     "<b>Op twee plekken zag het model iets dat niet in jouw beoordeling staat.</b> Beide in de inzending van student 2, "
     "beide nagekeken in het verslag zelf: een data-extractietabel waarvan twee rijen elkaar tegenspreken, en een "
     "verklaring voor vertekening die niet bij het studiedesign past. Ze staan uitgewerkt op pagina&nbsp;4.",
     "<b>Op drie plekken was jouw beoordeling concreter dan het model.</b> Ook die staan er, in hetzelfde blok. "
     "Waar het model goed in is, is elk criterium even consequent langslopen. Waar jouw beoordeling goed in is, "
     "is weten wat in dit vak is afgesproken en dat bij naam noemen.")
  + qa(I_INZET,
     "Selma: waar zouden wij dit kunnen inzetten?",
     "<b>Op de concepten, niet op het eindoordeel.</b> Het model loopt alle acht criteria even consequent langs en "
     "vindt tegenstrijdigheden in de tekst zelf. Dat is waarde in de ronde vóór het inleveren. Het eindcijfer blijft "
     "een keuze van de examinator; Eduface telt de punten niet op zoals jullie cesuur dat doet.",
     "<b>Wat deze test niet kan aantonen, is de ondergrens.</b> Beide geteste CAT's zijn geslaagd. We weten dus dat het "
     "model niemand onterecht laat zakken, maar nog niet of het zakt wat jullie laten zakken. Daarvoor heb ik één "
     "inzending nodig die jullie onvoldoende hebben beoordeeld, met het ingevulde formulier erbij. Dat is de "
     "vervolgstap die ik zou voorstellen.")))

# ---------------------------------------------------------------- kernbeeld
def rail(label, n, licht=False):
    breedte = n / 16 * 100
    vulling = (f'<div class="fill{" licht" if licht else ""}" style="width:{breedte:.4g}%"></div>'
               if n else "")
    return (f'<div class="lb">{label}</div><div class="rail">{vulling}</div>'
            f'<div class="val{" nul" if not n else ""}">{n}</div>')

kernbeeld = sectie("De zestien oordelen in één beeld", (
  '<p class="lead">Twee inzendingen van acht criteria. Per oordeel is gekeken of het vakje van het model past bij '
  'de punten op het formulier, en zo ja: koos het model dan het laagste of het hoogste van de twee passende '
  'vakjes?</p>'
  + '<div class="kern">'
  + rail("Eens, model koos het laagste passende vakje", 11)
  + rail("Eens, model koos het hoogste passende vakje", 4)
  + rail("Een score die de rubriek niet kent (3 punten)", 1, licht=True)
  + rail("Oneens: model onder de gegeven punten", 0)
  + '</div>'
  + '<p>De onderste balk is de belangrijkste: nul keer. Nergens komt het model onder het oordeel van de examinator '
    'uit. De bovenste twee laten zien waar het verschil wel zit, en die verhouding, elf tegen vier, is de kern van '
    'dit hele document.</p>'))

# ---------------------------------------------------------------- pagina 2
legenda = ('<p class="legend">De balk <span class="k"></span> is de ruimte die bij de gegeven punten hoort: '
           '4 punten past in de bovenste twee vakjes, 2 punten in de middelste twee. '
           'De stip <span class="d"></span> is het vakje dat het model koos. '
           'Staat de stip in de balk, dan spreken de twee beoordelingen elkaar niet tegen.</p>')

schalen = sectie("De twee inzendingen, criterium voor criterium", (
  '<p class="lead">Het formulier kent drie standen, het model vier vakjes. Daarom staat hieronder niet de ene uitkomst naast de andere, maar de ruimte die bij jullie punten hoort met daarin de keuze van het model.</p>'
  + legenda
  + bandtabel("Student 1 &middot; effect van kurkumacapsules op de cholesterolwaarde bij volwassen vrouwen",
              S1, "26 van 32 punten, cijfer 8,1, voldaan")
  + bandtabel("Student 2 &middot; effect van vitamine D-suppletie op gewichtsverlies bij obesitas en een tekort",
              S2, "23 van 32 punten, cijfer 7,2, voldaan")
  + '<p>Alle zestien stippen staan in de balk, en bijna altijd links erin. Bij criterium 8 van student 2 staan 3 punten op het formulier, een stand die de rubriek niet kent; die balk is daarom gestippeld.</p>'
  + '<p class="q"><b>De vraag die hieronder ligt:</b> staat 4 punten bij jullie gelijk aan Uitstekend, of dichter bij Goed? Zolang dat niet vastligt is elk hoogteverschil hier deels een vertaalverschil.</p>'))

# ---------------------------------------------------------------- pagina 3
verschillen = sectie("De drie verschillen die ertoe doen", (
  verschil("Criterium 3 &middot; databanken en weging", "beide studenten, model hoger",
    "Bij student 1: een wat summiere uiteenzetting van MeSH- en vrije zoektermen, bij de P ontbreken varianten als "
    "high cholesterol en lipid disorder. Wel voldoende herhaalbaar, drie artikelen, keuze onderbouwd. 2 punten. "
    "Bij student 2: gezocht in PubMed, maar geen van de zoekstrings bevat de C. 2 punten.",
    "Bij student 1: de PICO-zoektabel en de drie artikelen zijn goed gekozen, je weegt design, steekproef, duur en "
    "generaliseerbaarheid. Bij student 2: je zoekactie is grotendeels reconstrueerbaar door het gebruik van "
    "MeSH-termen, vrije termen, synoniemen en criteria. Beide Goed.",
    "Het model noemt een zoekstrategie navolgbaar zodra de zoektabel, de zoekstrings en de onderbouwde "
    "artikelkeuze er staan; de beoordeling telt daarnaast de volledigheid per PICO-element. "
    "<b>Waar ligt bij jullie de grens tussen een voldoende en een goede zoekstrategie?</b>")
  + verschil("Criterium 5 &middot; conclusie", "student 2, model hoger",
    "De conclusie had een stuk stellender geformuleerd mogen worden; je haalt al zaken aan die eigenlijk in de "
    "discussie aan bod mogen komen. 2 punten.",
    "Je verwerkt de tegenstrijdige bevindingen en onderscheidt afvallen van het corrigeren van een tekort. Maar je "
    "conclusie kan compacter en stelliger: schrap de methodologische toelichtingen. Goed.",
    "Beide wijzen hetzelfde aan. Het model weegt het als een verbeterpunt binnen een goede conclusie, de "
    "beoordeling als het verschil tussen twee niveaus. <b>Wat maakt dat onderscheid bij jullie?</b>")
  + verschil("Criterium 7 &middot; klinische relevantie", "student 2, model lager",
    "Er wordt een concrete monitoringfrequentie genoemd, jaarlijks. Ook wordt verwezen naar bestaande NHG-criteria, "
    "wat de aanbeveling goed integreerbaar maakt in bestaande werkwijzen. 4 punten.",
    "Je noemt een jaarlijkse bepaling; maak expliciet dat dit geldt bij een NHG-indicatie en niet als algemene "
    "screening bij obesitas. Benoem per keuze het evaluatiemoment en de vervolgstap bij een afwijkende waarde. Goed.",
    "De beoordeling rekent de frequentie als pluspunt, het model wil ook weten wie wanneer welke uitkomst "
    "beoordeelt. <b>Hoort dat detailniveau bij een CAT op dit niveau?</b>")))

eens = sectie("Waar jullie elkaar wel aan de top vonden", (
  '<div class="verschil">'
  '<h3>Criterium 6 &middot; kritische inhoudelijke discussie <span class="mv">student 2, allebei het hoogste '
  'niveau</span></h3>'
  + '<div class="vs"><div><span class="lab">Beoordelingsformulier</span><p>Vat kernachtig en correct de belangrijkste '
    'nieuwe inzichten samen. Benoemt en verkent de tegenstrijdige resultaten, inclusief oorzaken als supplementvorm, '
    'studieduur en populatieverschillen. Goed onderbouwde kritische noot. 4 punten.</p></div>'
    '<div><span class="lab">Eduface</span><p>Je koppelt tegenstrijdige resultaten aan studieduur, dosering, '
    'supplementvorm, populatie en dieetinterventie. Je kritische slotconclusie over mager en inconsistent bewijs is '
    'overtuigend. Uitstekend.</p></div></div>'
  + '<p class="q">Het enige van de zestien oordelen waar het model het hoogste vakje koos, en de argumenten lopen bijna gelijk op. <b>Wat maakte dit hoofdstuk anders dan de andere zeven?</b> Dat antwoord zegt meer over waar jullie lat ligt dan de drie verschillen hierboven.</p></div>'))

# ---------------------------------------------------------------- pagina 4
tweezijdig = sectie("Wat de een zag en de ander niet", (
  f'<h3>{I_ZIEN} Twee dingen die het model zag en die niet in de beoordeling staan</h3>'
  '<p>Beide zijn nagekeken in de inzending zelf en kloppen.</p>'
  '<ul>'
  '<li><b>Student 2, data-extractietabel bij artikel 2.</b> De rij Sterke punten noemt een IPD-meta-analyse en de '
  'databases MEDLINE, EMBASE en CENTRAL, terwijl de rij Dataverzameling in diezelfde tabel Google Scholar, '
  'Web of Science, PubMed en Scopus noemt. Dat zijn kenmerken van artikel 3 die in de rij van artikel 2 terecht '
  'zijn gekomen.</li>'
  '<li><b>Student 2, samenvatting van artikel 2.</b> De mogelijke vertekening wordt verklaard doordat deelnemers zelf '
  'voor suppletie kozen. Dat past niet bij een meta-analyse van gerandomiseerde trials, waarin de toewijzing juist '
  'niet aan de deelnemer is.</li>'
  '</ul>'
  f'<h3>{I_FORM} Drie dingen die de beoordeling zag en die niet in de feedback van het model staan</h3>'
  '<ul>'
  '<li><b>De ontbrekende zoektermen bij naam.</b> De beoordeling noemt high cholesterol, elevated cholesterol en '
  'lipid disorder letterlijk. Het model bleef bij de constatering dat dat blok smaller is dan de andere.</li>'
  '<li><b>De kolom Setting in de data-extractietabel.</b> De beoordeling toetst die aan wat in de les is afgesproken. '
  'Het model kwam daar pas op nadat die afspraak expliciet in de rubriektekst was gezet.</li>'
  '<li><b>De plaatsing van de bronverwijzing.</b> Dat de APA-verwijzing bij artikel 1 niet overal achter de bewering '
  'staat waar hij bij hoort, staat alleen in de beoordeling.</li>'
  '</ul>'
  '<p>Dat verschil is geen toeval. Het model kent de rubriek en de inzending, verder niets. Alles wat in dit vak is '
  'afgesproken maar niet in de rubriektekst staat, ziet het niet. Dat is precies de knop waar wij aan draaien.</p>'))

afwijkingen = sectie("Twee dingen die nog niet kloppen met jullie formulier", (
  '<ul>'
  '<li><b>Het eindoordeel in Eduface is niet jullie cesuur.</b> Jullie zakregel is hard: minimaal 18 punten '
  '&eacute;n elk onderdeel minimaal 2 punten. Eduface zet daar een eigen eindoordeel naast dat op een weging van de '
  'acht criteria berust en niet op die twee voorwaarden. Een inzending met &eacute;&eacute;n onvoldoende onderdeel kan daar dus als voldoende verschijnen terwijl hij bij jullie zakt. De examinator zet het cijfer zelf, dus aan de uitkomst verandert het niets, maar ga niet op dat ene woord af.</li>'
  '<li><b>De weging staat niet gelijk verdeeld.</b> Op het formulier telt elk criterium even zwaar: 4 van de 32 '
  'punten, 12,5 procent. In Eduface staat reflectie nu op 16 procent en staan de andere zeven op 12. Dat wijkt af '
  'van jullie eigen formulier en ik trek het gelijk, tenzij jullie zeggen dat reflectie zwaarder hoort te tellen.</li>'
  '</ul>'))

verantwoording = sectie("Hoe dit tot stand is gekomen", (
  '<ul>'
  '<li><b>Wat erin is gegaan.</b> De twee CAT-verslagen, de twee door Kas ingevulde beoordelingsformulieren van '
  'juni 2025, en bijlage 6 versie 3.0 als rubriek. Het model heeft de ingevulde formulieren nooit gezien.</li>'
  '<li><b>Wat ik heb bijgesteld.</b> De tekst van de rubriekvakjes in Eduface, in drie ronden, plus de instructie '
  'over de feedbackstijl. Ik heb de rubriek dus geijkt op jullie oordeel, niet de feedback zelf geschreven.</li>'
  '<li><b>Wat ik met de hand heb aangepast.</b> Op een paar criteria heb ik de formulering bijgeschaafd, bijvoorbeeld waar het model twee keer hetzelfde zei. De oordelen zijn ongewijzigd gebleven.</li>'
  '<li><b>Waarvoor dit geldt.</b> Het blanco beoordelingsformulier dat Selma stuurde is inhoudelijk gelijk aan versie 3.0 waarop dit is ingericht: acht criteria, 4, 2 of 0 punten, dezelfde cesuur. Wat hier staat geldt dus ook voor haar groepen.</li>'
  '<li><b>Wat dit niet is.</b> Geen toets van jullie beoordeling. De punten op de formulieren zijn hier het '
  'uitgangspunt waaraan het model is gemeten, niet omgekeerd.</li>'
  '</ul>'))

# ---------------------------------------------------------------- pagina
html = f"""<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8">
<title>CAT POH-6: de beoordeling en het model naast elkaar</title>
<style>{CSS}</style></head><body>
<div class="head">
  <img class="b" src="data:image/png;base64,{b64('logo-breederode.png')}" alt="Breederode Hogeschool">
  <img class="e" src="data:image/png;base64,{b64('logo-eduface.png')}" alt="Eduface">
</div>
<h1>CAT POH-6: de beoordeling en het model naast elkaar</h1>
{antwoorden}
{kernbeeld}
<div style="break-before:page"></div>
{schalen}
<div style="break-before:page"></div>
{verschillen}
{eens}
<div style="break-before:page"></div>
{tweezijdig}
{afwijkingen}
{verantwoording}
</body></html>"""

pathlib.Path("vergelijking-cat-poh.html").write_text(html, encoding="utf-8")
print("html:", len(html) // 1024, "KB")
