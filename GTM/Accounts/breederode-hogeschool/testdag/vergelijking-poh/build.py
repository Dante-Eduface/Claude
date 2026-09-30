# -*- coding: utf-8 -*-
"""Document voor Kas van Kruining en Selma de Nijs: hun beoordeling naast het model.

Twee CAT-inzendingen van juni 2025, acht criteria. Opent met hun drie vragen.
Opmaak in stijl.py.
"""
import pathlib
from stijl import (sectie, kaart, qa, vs, rail, track, pagina,
                   I_HOOGTE, I_ZIEN, I_FORM, I_INZET)

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

def bandtabel(rijen, totaal):
    kop = "".join(f'<th class="sk">{v}</th>' for v in ["Onvoldoende", "Voldoende", "Goed", "Uitstekend"])
    body = "".join(f'<tr><td class="s">{n}</td><td class="p">{p}</td>'
                   f'<td class="tr" colspan="4">{track(w, punten=p)}</td></tr>' for n, p, w in rijen)
    return (f'<table><thead><tr><th class="s">Criterium</th><th class="p">Punten</th>{kop}</tr></thead>'
            f'<tbody>{body}<tr class="tot"><td colspan="6">{totaal}</td></tr></tbody></table>')

# ---------------------------------------------------------------- pagina 1
antwoorden = sectie("Jullie drie vragen, hier beantwoord", (
  qa(I_HOOGTE,
     "Kas: kwam mijn feedback overeen met die van het model, of zaten er duidelijke verschillen in?",
     "<b>Over de vraag of iets geslaagd is, zijn jullie het zestien van de zestien keer eens.</b> Bij geen enkel "
     "criterium, bij geen van de twee inzendingen, komt het model onder jouw punten uit. Er is dus geen inzending "
     "en geen criterium waarover jullie het oneens zijn over voldoen.",
     "<b>Het verschil zit in de hoogte, en het is systematisch.</b> Van de vijftien criteria die je 4 of 2 punten "
     "gaf, koos het model elf keer het laagste van de twee vakjes die bij die punten passen, en vier keer het "
     "hoogste. Waar jij 4 punten gaf, kwam het model zeven keer op Goed en een keer op Uitstekend. Drie verschillen "
     "zijn groot genoeg om uit te werken: criterium 3, 5 en 7.")
  + qa(I_ZIEN,
     "Kas: kan ik hier als examinator iets van leren?",
     "<b>Op twee plekken zag het model iets dat niet in jouw beoordeling staat.</b> Beide in de inzending van "
     "student 2, beide nagekeken in het verslag zelf: een data-extractietabel waarvan twee rijen elkaar "
     "tegenspreken, en een verklaring voor vertekening die niet bij het studiedesign past.",
     "<b>Op drie plekken was jouw beoordeling concreter dan het model.</b> Ook die staan erin. Waar het model goed "
     "in is, is elk criterium even consequent langslopen. Waar jouw beoordeling goed in is, is weten wat in dit vak "
     "is afgesproken en dat bij naam noemen.")
  + qa(I_INZET,
     "Selma: waar zouden wij dit kunnen inzetten?",
     "<b>Op de concepten, niet op het eindoordeel.</b> Het model loopt alle acht criteria even consequent langs en "
     "vindt tegenstrijdigheden in de tekst zelf. Dat is waarde in de ronde v&oacute;&oacute;r het inleveren. Het "
     "eindcijfer blijft een keuze van de examinator.",
     "<b>En het zakt ook echt.</b> Het verslag dat Selma als onvoldoende voorbeeld gebruikt is er inmiddels ook "
     "doorheen gehaald. Daar komt wel een Onvoldoende uit, op criterium 7, en onder jullie cesuur is dat zakken. "
     "Dat staat in een apart stuk, met wat er aan die feedback nog niet deugt.")))

kernbeeld = sectie("De zestien oordelen in één beeld", kaart(
  '<p class="lead">Twee inzendingen van acht criteria. Per oordeel is gekeken of het vakje van het model past bij '
  'de punten op het formulier, en zo ja: koos het model dan het laagste of het hoogste van de twee passende '
  'vakjes?</p>'
  '<div class="kern">'
  + rail("Eens, model koos het laagste passende vakje", 11)
  + rail("Eens, model koos het hoogste passende vakje", 4)
  + rail("Een score die de rubriek niet kent (3 punten)", 1, licht=True)
  + rail("Oneens: model onder de gegeven punten", 0)
  + '</div>'
  '<p style="margin-top:4mm">De onderste balk is de belangrijkste: nul keer. Nergens komt het model onder het '
  'oordeel van de examinator uit. De bovenste twee laten zien waar het verschil wel zit, en die verhouding, elf '
  'tegen vier, is de kern van dit hele document.</p>'))

# ---------------------------------------------------------------- pagina 2
schalen = sectie("De twee inzendingen, criterium voor criterium", (
  '<p class="lead">Het formulier kent drie standen, het model vier vakjes. Daarom staat hieronder niet de ene '
  'uitkomst naast de andere, maar de ruimte die bij jullie punten hoort met daarin de keuze van het model.</p>'
  '<p class="legend">De balk <span class="k"></span> is de ruimte die bij de gegeven punten hoort: 4 punten past in '
  'de bovenste twee vakjes, 2 punten in de middelste twee. De stip <span class="d"></span> is het vakje dat het '
  'model koos. Staat de stip in de balk, dan spreken de twee beoordelingen elkaar niet tegen.</p>'
  + kaart('<h3>Student 1 &middot; effect van kurkumacapsules op de cholesterolwaarde bij volwassen vrouwen</h3>'
          + bandtabel(S1, "26 van 32 punten, cijfer 8,1, voldaan"))
  + kaart('<h3>Student 2 &middot; effect van vitamine D-suppletie op gewichtsverlies bij obesitas en een tekort</h3>'
          + bandtabel(S2, "23 van 32 punten, cijfer 7,2, voldaan"))
  + kaart('<p>Alle zestien stippen staan in de balk, en bijna altijd links erin. Bij criterium 8 van student 2 '
          'staan 3 punten op het formulier, een stand die de rubriek niet kent; die balk is daarom gestippeld.</p>'
          '<p class="q"><b>De vraag die hieronder ligt:</b> staat 4 punten bij jullie gelijk aan Uitstekend, of '
          'dichter bij Goed? Zolang dat niet vastligt is elk hoogteverschil hier deels een vertaalverschil.</p>')))

# ---------------------------------------------------------------- pagina 3
def verschil(kop, mv, links, rechts, vraag):
    return kaart(f'<h3>{kop} <span class="mv">{mv}</span></h3>' + vs(links, rechts) + f'<p class="q">{vraag}</p>')

verschillen = sectie("De drie verschillen die ertoe doen", (
  verschil("Criterium 3 &middot; databanken en weging", "beide studenten, model hoger",
    "Bij student 1: een wat summiere uiteenzetting van MeSH- en vrije zoektermen, bij de P ontbreken varianten als "
    "high cholesterol en lipid disorder. Wel voldoende herhaalbaar, drie artikelen, keuze onderbouwd. 2 punten. "
    "Bij student 2: gezocht in PubMed, maar geen van de zoekstrings bevat de C. 2 punten.",
    "Bij student 1: de PICO-zoektabel en de drie artikelen zijn goed gekozen, je weegt design, steekproef, duur en "
    "generaliseerbaarheid. Bij student 2: je zoekactie is grotendeels reconstrueerbaar door het gebruik van "
    "MeSH-termen, vrije termen, synoniemen en criteria. Beide Goed.",
    "Het model noemt een zoekstrategie navolgbaar zodra de zoektabel, de zoekstrings en de onderbouwde artikelkeuze "
    "er staan; de beoordeling telt daarnaast de volledigheid per PICO-element. <b>Waar ligt bij jullie de grens "
    "tussen een voldoende en een goede zoekstrategie?</b>")
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

eens = sectie("Waar jullie elkaar wel aan de top vonden", kaart(
  '<h3>Criterium 6 &middot; kritische inhoudelijke discussie '
  '<span class="mv">student 2, allebei het hoogste niveau</span></h3>'
  + vs("Vat kernachtig en correct de belangrijkste nieuwe inzichten samen. Benoemt en verkent de tegenstrijdige "
       "resultaten, inclusief oorzaken als supplementvorm, studieduur en populatieverschillen. Goed onderbouwde "
       "kritische noot. 4 punten.",
       "Je koppelt tegenstrijdige resultaten aan studieduur, dosering, supplementvorm, populatie en "
       "dieetinterventie. Je kritische slotconclusie over mager en inconsistent bewijs is overtuigend. Uitstekend.")
  + '<p class="q">Het enige van de zestien oordelen waar het model het hoogste vakje koos, en de argumenten lopen '
    'bijna gelijk op. <b>Wat maakte dit hoofdstuk anders dan de andere zeven?</b> Dat antwoord zegt meer over waar '
    'jullie lat ligt dan de drie verschillen hierboven.</p>'))

# ---------------------------------------------------------------- pagina 4
tweezijdig = sectie("Wat de een zag en de ander niet", (
  kaart(f'<h3>{I_ZIEN} Twee dingen die het model zag en die niet in de beoordeling staan</h3>'
        '<p>Beide zijn nagekeken in de inzending zelf en kloppen.</p>'
        '<ul>'
        '<li><b>Student 2, data-extractietabel bij artikel 2.</b> De rij Sterke punten noemt een IPD-meta-analyse '
        'en de databases MEDLINE, EMBASE en CENTRAL, terwijl de rij Dataverzameling in diezelfde tabel Google '
        'Scholar, Web of Science, PubMed en Scopus noemt. Dat zijn kenmerken van artikel 3 die in de rij van '
        'artikel 2 terecht zijn gekomen.</li>'
        '<li><b>Student 2, samenvatting van artikel 2.</b> De mogelijke vertekening wordt verklaard doordat '
        'deelnemers zelf voor suppletie kozen. Dat past niet bij een meta-analyse van gerandomiseerde trials, '
        'waarin de toewijzing juist niet aan de deelnemer is.</li>'
        '</ul>')
  + kaart(f'<h3>{I_FORM} Drie dingen die de beoordeling zag en die niet in de feedback van het model staan</h3>'
        '<ul>'
        '<li><b>De ontbrekende zoektermen bij naam.</b> De beoordeling noemt high cholesterol, elevated cholesterol '
        'en lipid disorder letterlijk. Het model bleef bij de constatering dat dat blok smaller is dan de andere.</li>'
        '<li><b>De kolom Setting in de data-extractietabel.</b> De beoordeling toetst die aan wat in de les is '
        'afgesproken. Het model kwam daar pas op nadat die afspraak expliciet in de rubriektekst was gezet.</li>'
        '<li><b>De plaatsing van de bronverwijzing.</b> Dat de APA-verwijzing bij artikel 1 niet overal achter de '
        'bewering staat waar hij bij hoort, staat alleen in de beoordeling.</li>'
        '</ul>'
        '<p>Dat verschil is geen toeval. Het model kent de rubriek en de inzending, verder niets. Alles wat in dit '
        'vak is afgesproken maar niet in de rubriektekst staat, ziet het niet. Dat is precies de knop waar wij aan '
        'draaien.</p>')))

eindoordeel = sectie("Wat je moet weten over het eindoordeel in Eduface", kaart(
  '<p><b>Het eindoordeel in Eduface is niet jullie cesuur.</b> Jullie zakregel is hard: minimaal 18 punten '
  '&eacute;n elk onderdeel minimaal 2 punten. Eduface zet daar een eigen eindoordeel naast dat op een weging van '
  'de acht criteria berust en niet op die twee voorwaarden.</p>'
  '<p>Een inzending met &eacute;&eacute;n onvoldoende onderdeel kan daar dus als voldoende verschijnen terwijl hij bij jullie zakt. Dat gebeurt ook echt: bij het onvoldoende-voorbeeld van Selma staat criterium 7 op Onvoldoende en het eindoordeel op Voldoende. Ga dus niet op dat ene woord af.</p>'))

verantwoording = sectie("Hoe dit tot stand is gekomen", kaart(
  '<ul>'
  '<li><b>Wat erin is gegaan.</b> De twee CAT-verslagen, de twee door Kas ingevulde beoordelingsformulieren van '
  'juni 2025, en bijlage 6 versie 3.0 als rubriek. Het model heeft de ingevulde formulieren nooit gezien.</li>'
  '<li><b>Wat ik heb bijgesteld.</b> De tekst van de rubriekvakjes in Eduface, in drie ronden, plus de instructie '
  'over de feedbackstijl. Ik heb de rubriek dus geijkt op jullie oordeel, niet de feedback zelf geschreven.</li>'
  '</ul>'))

body = (antwoorden + kernbeeld + schalen + verschillen + eens
        + tweezijdig + eindoordeel + verantwoording)

html = pagina("CAT POH-6: de beoordeling en het model naast elkaar", body,
              "logo-breederode.png", "logo-eduface.png")
pathlib.Path("vergelijking-cat-poh.html").write_text(html, encoding="utf-8")
print("html:", len(html) // 1024, "KB")
