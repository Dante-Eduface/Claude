import base64, pathlib
H = pathlib.Path(".")
def b64(p): return base64.b64encode((H/p).read_bytes()).decode()

CSS = """
:root{ --bar:#0B4F6C; --soft:#EEF3F5; --ink:#1C1C1C; --line:#C7D6DD;
       --ok:#2E7D32; --mid:#8A6D1F; --muted:#5A6B72; }
@page{ size:A4; margin:13mm 13mm 12mm 13mm; }
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact; print-color-adjust:exact}
body{ font-family:Georgia,"Times New Roman",serif; color:var(--ink);
      font-size:9pt; line-height:1.38; margin:0; }
.head{display:flex;align-items:center;justify-content:space-between;margin:0 0 4mm 0}
.head img.b{height:12mm} .head img.e{height:5.5mm}
h1{font-size:13.5pt;margin:0 0 1mm 0;color:var(--bar);line-height:1.2}
.sub{font-size:8.2pt;color:var(--muted);margin:0 0 4mm 0}
.block{break-inside:avoid; margin:0 0 3.2mm 0}
.block>.bar{background:var(--bar);color:#fff;font-weight:bold;font-size:9.4pt;
  padding:1.4mm 2.6mm;border-radius:2px 2px 0 0}
.block>.body{border:1px solid var(--line);border-top:none;padding:2.2mm 2.6mm 1.6mm 2.6mm;border-radius:0 0 2px 2px}
.block>.body>*:last-child{margin-bottom:0}
p{margin:0 0 1.8mm 0}
ol.kern{margin:0;padding-left:5mm} ol.kern li{margin:0 0 1.2mm 0}
table{width:100%;border-collapse:collapse;font-size:8.4pt;margin:0}
th{background:var(--soft);text-align:left;font-weight:bold;padding:1.2mm 2mm;
   border-bottom:1px solid var(--line);font-size:7.8pt;letter-spacing:.02em}
td{padding:1mm 2mm;border-bottom:1px solid #E4ECEF;vertical-align:top}
tr:last-child td{border-bottom:none}
td.n,th.n{text-align:center;width:13%}
tr.tot td{background:var(--soft);font-weight:bold;border-bottom:none}
.ok{color:var(--ok);font-weight:bold} .mid{color:var(--mid);font-weight:bold}
.cas{font-size:8pt;color:var(--muted);font-style:italic;margin:0 0 1.4mm 0}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:2.4mm;margin:0 0 1.8mm 0}
.vs div{background:var(--soft);border-left:2px solid var(--bar);padding:1.6mm 2.2mm;font-size:8.2pt}
.vs .lab{display:block;font-size:7.6pt;letter-spacing:.06em;text-transform:uppercase;
  color:var(--bar);font-family:Arial,sans-serif;font-weight:bold;margin-bottom:1mm;border:0;padding:0;background:none}
.q{font-weight:bold}
.note{font-size:8.1pt;color:var(--muted);margin-top:1.4mm}
h3{font-size:9.4pt;margin:0 0 1.2mm 0;color:var(--bar)}
h3+ul{margin-top:0}
ul{margin:0 0 2mm 0;padding-left:4.2mm} li{margin:0 0 1.1mm 0}
"""

def blok(titel, inhoud):
    return f'<div class="block"><div class="bar">{titel}</div><div class="body">{inhoud}</div></div>'

def tabel(casus, rijen, totaal):
    r = "".join(
        f'<tr><td>{n}</td><td class="n">{b}</td><td class="n">{e}</td>'
        f'<td class="n"><span class="{c}">{v}</span></td></tr>' for n, b, e, v, c in rijen)
    return (f'<p class="cas">{casus}</p><table><thead><tr><th>Criterium</th>'
            f'<th class="n">Beoordeling</th><th class="n">Eduface</th>'
            f'<th class="n">Binnen bandbreedte</th></tr></thead><tbody>{r}'
            f'<tr class="tot"><td>{totaal}</td><td class="n"></td><td class="n"></td><td class="n"></td></tr>'
            f'</tbody></table>')

C = ["1. Aanleiding van de klinische vraag", "2. Onderzoeksvraag op basis van PICO",
     "3. Databanken en weging van informatie", "4. Analyse binnen de praktijkcontext",
     "5. Conclusie uit de resultaten", "6. Kritische inhoudelijke discussie",
     "7. Klinische relevantie en toepasbaarheid", "8. Reflectie op werkwijze en rolontwikkeling"]

s1 = list(zip(C, ["4","4","2","4","2","4","2","4"],
              ["Goed","Goed","Goed","Goed","Voldoende","Goed","Voldoende","Goed"],
              ["ja"]*8, ["ok"]*8))
s2 = list(zip(C, ["4","2","2","2","2","4","4","3"],
              ["Goed","Voldoende","Goed","Voldoende","Goed","Uitstekend","Goed","Voldoende"],
              ["ja"]*8, ["ok"]*8))

def vs(a, b):
    return (f'<div class="vs"><div><span class="lab">Beoordeling</span>{a}</div>'
            f'<div><span class="lab">Eduface</span>{b}</div></div>')

kern = blok("Wat eruit komt", """
<ol class="kern">
<li><b>Op geslaagd of niet zijn jullie het volledig eens.</b> Bij zestien van de zestien criteria komen de beoordeling en het model allebei op geslaagd uit. Geen van beide komt ergens op een onvoldoende.</li>
<li><b>Het verschil zit in de hoogte.</b> Waar de beoordeling vier punten gaf, komt het model meestal een stap lager uit. Op twee criteria waar de beoordeling twee punten gaf, komt het model juist een stap hoger.</li>
<li><b>De beoordeling gebruikt de uiteinden van de schaal, het model blijft in het midden.</b> De beoordeling gaf negen van de zestien keer de hoogste score, het model één keer.</li>
</ol>
<p class="note">Het formulier kent drie standen (4, 2 of 0 punten), het model vier. De laatste kolom zegt of het oordeel van het model past bij de punten: vier punten hoort in de bovenste twee vakjes, twee punten in de middelste twee, nul in het onderste. Geen enkele rij valt daarbuiten.</p>
<p class="note">Op een paar criteria heb ik de formulering van het model bijgeschaafd voordat ik hem opstuurde, bijvoorbeeld waar het model twee keer hetzelfde zei. De oordelen zijn daarbij ongewijzigd gebleven.</p>""")

pag1 = (kern
  + blok("Student 1 &middot; kurkuma bij verhoogd cholesterol",
         tabel("Beoordeeld juni 2025. Effect van kurkumacapsules op de cholesterolwaarde bij volwassen vrouwen.",
               s1, "Totaal 26 van 32 punten, cijfer 8,1, voldaan"))
  + blok("Student 2 &middot; vitamine D bij obesitas",
         tabel("Beoordeeld juni 2025. Effect van vitamine D-suppletie op gewichtsverlies bij volwassenen met obesitas en een tekort.",
               s2, "Totaal 23 van 32 punten, cijfer 7,2, voldaan")))

v1 = blok("Verschil 1 &middot; Zoekstrategie, beide studenten &middot; model een stap hoger",
  vs("Bij student 1: een wat summiere uiteenzetting van MeSH- en vrije zoektermen, bij de P ontbreken varianten als high cholesterol en lipid disorder. Wel voldoende herhaalbaar, drie artikelen, keuze onderbouwd. Twee punten. Bij student 2: gezocht in PubMed, maar geen van de zoekstrings bevat de C. Twee punten.",
     "Bij student 1: PubMed, PICO-zoektabel en drie artikelen zijn goed gekozen, je weegt design, steekproef, duur en generaliseerbaarheid. Bij student 2: je zoekactie is grotendeels reconstrueerbaar door het gebruik van MeSH-termen, vrije termen, synoniemen en criteria. Beide goed.")
  + '<p class="q">Het model noemt een zoekstrategie navolgbaar zodra de zoektabel, de zoekstrings en de onderbouwde artikelkeuze er staan. In de beoordeling telt daarnaast hoe volledig de termen per PICO-element zijn. Waar ligt bij jullie de grens tussen een voldoende en een goede zoekstrategie?</p>')

v2 = blok("Verschil 2 &middot; Conclusie, student 2 &middot; model een stap hoger",
  vs("De conclusie had een stuk stellender geformuleerd mogen worden; je haalt al zaken aan die eigenlijk in de discussie aan bod mogen komen. Twee punten.",
     "Je verwerkt de tegenstrijdige bevindingen en onderscheidt afvallen van het corrigeren van een tekort. Maar je conclusie kan compacter en stelliger: schrap de methodologische toelichtingen. Goed.")
  + '<p class="q">Beide teksten wijzen hetzelfde aan: de conclusie mag stelliger en er staat methodologie in die er niet hoort. Het model weegt dat als een verbeterpunt binnen een goede conclusie, de beoordeling als het verschil tussen twee niveaus. Wat maakt dat onderscheid bij jullie?</p>')

v3 = blok("Verschil 3 &middot; Klinische relevantie, student 2 &middot; model een stap lager",
  vs("Er wordt een concrete monitoringfrequentie genoemd, jaarlijks. Ook wordt verwezen naar bestaande NHG-criteria, wat de aanbeveling goed integreerbaar maakt in bestaande werkwijzen. Vier punten.",
     "Je noemt een jaarlijkse bepaling; maak expliciet dat dit geldt bij een NHG-indicatie en niet als algemene screening bij obesitas. Benoem per keuze het evaluatiemoment en de vervolgstap bij een afwijkende waarde. Goed.")
  + '<p class="q">De beoordeling rekent de genoemde frequentie als pluspunt, het model wil daarnaast weten wie wanneer welke uitkomst beoordeelt. Hoort dat detailniveau bij een CAT op dit niveau, of is een genoemde frequentie genoeg?</p>')

v4 = blok("Verschil 4 &middot; Discussie, student 2 &middot; allebei het hoogste niveau",
  vs("Vat kernachtig en correct de belangrijkste nieuwe inzichten samen. Benoemt en verkent de tegenstrijdige resultaten, inclusief oorzaken als supplementvorm, studieduur en populatieverschillen. Goed onderbouwde kritische noot. Vier punten.",
     "Je koppelt tegenstrijdige resultaten aan studieduur, dosering, supplementvorm, populatie en dieetinterventie. Je kritische slotconclusie over mager en inconsistent bewijs is overtuigend. Uitstekend.")
  + '<p class="q">Dit is het enige criterium waar jullie allebei op het hoogste niveau uitkomen, en de argumenten lopen bijna gelijk. Wat maakte dit hoofdstuk anders dan de andere zeven?</p>')

v5 = blok("Verschil 5 &middot; de schaal zelf",
  '<p>Het beoordelingsformulier werkt met 4, 2 of 0 punten. Het model werkt met vier standen. Bij criterium 8 van student 2 is drie punten gegeven, een stand die op het formulier niet bestaat.</p>'
  + '<p class="q">Welke vertaling willen jullie: staat vier punten gelijk aan uitstekend, of ligt jullie vier dichter bij goed? Zolang dat niet vastligt is elk hoogteverschil hierboven deels een vertaalverschil.</p>')

pag3 = (blok("Wat het model zag dat niet in de beoordeling staat", """
<p>Twee inhoudelijke constateringen. Beide zijn nagekeken in de inzending en kloppen.</p>
<ul>
<li><b>Student 2, data-extractietabel artikel 2.</b> De rij Sterke punten noemt een IPD-meta-analyse en de databases MEDLINE, EMBASE en CENTRAL, terwijl de rij Dataverzameling in diezelfde tabel Google Scholar, Web of Science, PubMed en Scopus noemt. Dat zijn kenmerken van artikel 3 die in de rij van artikel 2 terecht zijn gekomen.</li>
<li><b>Student 2, samenvatting artikel 2.</b> De mogelijke vertekening wordt verklaard doordat deelnemers zelf voor suppletie kozen. Dat past niet bij een meta-analyse van gerandomiseerde trials.</li>
</ul>""")
  + blok("Wat de beoordeling zag dat niet in de feedback van het model staat", """
<ul>
<li><b>De ontbrekende zoektermen bij naam.</b> De beoordeling noemt high cholesterol, elevated cholesterol en lipid disorder letterlijk. Het model bleef bij de constatering dat het blok smaller is dan de andere.</li>
<li><b>De kolom Setting.</b> De beoordeling toetst die aan wat in de les is afgesproken. Het model kwam daar pas op nadat die regel expliciet in de rubriek was gezet.</li>
<li><b>De plaatsing van de bronverwijzing.</b> Dat de APA-verwijzing bij artikel 1 niet overal achter de bewering staat waar hij bij hoort, staat alleen in de beoordeling.</li>
</ul>
<p>Waar het model sterk in is, is elk criterium even consequent langslopen en niets overslaan. Waar de beoordeling sterk in is, is weten wat in dit vak is afgesproken en dat bij naam kunnen noemen.</p>""")
  + blok("De vijftig minuten van donderdag", """
<table><thead><tr><th class="n" style="width:18%">Tijd</th><th>Wat</th></tr></thead><tbody>
<tr><td class="n">10:00</td><td>Wat er gedaan is en wat de tabellen laten zien</td></tr>
<tr><td class="n">10:05</td><td>De vier verschillen, een voor een</td></tr>
<tr><td class="n">10:20</td><td>De schaalvraag: drie standen tegenover vier</td></tr>
<tr><td class="n">10:30</td><td>Wat het model zag en wat de beoordeling zag</td></tr>
<tr><td class="n">10:40</td><td>Waar zouden jullie dit inzetten, en de vervolgstap</td></tr>
</tbody></table>
<p class="note" style="margin-top:3mm"><b>Voorstel voor de vervolgstap.</b> Beide geteste CAT's zijn geslaagd. Daarmee weten we dat het model niemand onterecht laat zakken, maar nog niet of het zakt wat jullie laten zakken. Selma heeft een verslag dat als onvoldoende voorbeeld wordt gebruikt. Dat door het model halen, met jullie eigen beoordeling ernaast, is de enige meting die de ondergrens echt toetst.</p>"""))

html = f"""<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8">
<title>CAT POH-6: beoordeling en model naast elkaar</title><style>{CSS}</style></head><body>
<div class="head">
  <img class="b" src="data:image/png;base64,{b64('logo-breederode.png')}" alt="Breederode Hogeschool">
  <img class="e" src="data:image/png;base64,{b64('logo-eduface.png')}" alt="Eduface">
</div>
<h1>CAT POH-6: de beoordeling en het model naast elkaar</h1>
<p class="sub">Breederode Hogeschool &middot; opleiding Praktijkondersteuner Huisartsenzorg &middot; twee inzendingen, acht criteria<br>
Opgesteld 30 september 2026, door Dante Torbed, Eduface</p>
{pag1}
<div style="break-before:page"></div>
{v1}{v2}{v3}{v4}{v5}
<div style="break-before:page"></div>
{pag3}
</body></html>"""
pathlib.Path("vergelijking-cat-poh.html").write_text(html, encoding="utf-8")
print("html:", len(html)//1024, "KB")
