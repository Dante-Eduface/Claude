# -*- coding: utf-8 -*-
"""Document voor Selma de Nijs: het onvoldoende-voorbeeld, zelf beoordeeld.

Voorbeeld 1 (rode gist rijst tegenover statines, 17 maart 2025) beoordeeld tegen
bijlage 6 versie 3.0, 4/2/0 punten, cesuur 18 punten plus minimaal 2 per onderdeel.
Het oordeel in dit document is van ons, niet van Eduface. Wat Eduface ervan maakte
staat alleen in de sectie die laat zien waar het model te mild is.
Opmaak in stijl.py.
"""
import pathlib
from stijl import sectie, kaart, qa, track, pagina, I_ZAK, I_INZET, I_HOOGTE, I_FORM

# criterium, punten, oordeel in een zin
OORDEEL = [
 ("1. Aanleiding van de klinische vraag", 2,
  "Casus, concrete vraag en de NHG-standaarden staan er. De aanvulling vanuit de eigen expertise, met "
  "implicaties, gevolgen en kansen, ontbreekt."),
 ("2. Onderzoeksvraag op basis van PICO", 2,
  "Alle vier de PICO-elementen zijn herkenbaar in de vraag. De kenmerken uit de casus en de veiligheidsvraag "
  "uit de aanleiding zijn er onderweg uit gevallen."),
 ("3. Databanken en weging van informatie", 2,
  "Zoektabel, in- en exclusiecriteria, drie artikelen en een onderbouwde keuze zijn er. Herhaalbaar is de "
  "zoekactie niet: de hits lopen na een AND op van 134 naar 1.528.289."),
 ("4. Analyse binnen de praktijkcontext", 0,
  "De beoordelingsformulieren voor betrouwbaarheid, validiteit en generaliseerbaarheid zijn op geen enkel "
  "artikel toegepast, en de genoemde sterke punten zijn niet methodologisch."),
 ("5. Conclusie uit de resultaten", 0,
  "De onderzoeksvraag is vergelijkend, de conclusie vergelijkt niet. Bovendien generaliseert zij artikel 1, "
  "dat de combinatie met statines onderzocht."),
 ("6. Kritische inhoudelijke discussie", 2,
  "Alle onderdelen zijn behandeld en de methodologische kanttekeningen zijn raak. Het opgevoerde "
  "conflicterende perspectief is geen tegenstelling."),
 ("7. Klinische relevantie en toepasbaarheid", 0,
  "De twee aanbevelingen vragen om vervolgonderzoek en zijn geen handelingsalternatief. Implicaties, "
  "haalbaarheid en monitoring ontbreken alle drie."),
 ("8. Reflectie en rolontwikkeling", 2,
  "De vijf gevraagde onderdelen staan er, inclusief de verwerkte feedback. Het alternatief, weer op deze "
  "manier, is niet kritisch."),
]
TOTAAL = sum(p for _, p, _ in OORDEEL)

MODEL = ["Goed", "Goed", "Goed", "Voldoende", "Voldoende", "Voldoende", "Onvoldoende", "Voldoende"]

def oordeeltabel():
    rijen = "".join(
        f'<tr><td class="s">{n}</td>'
        f'<td class="p"><b class="{"nul" if p == 0 else ""}">{p}</b></td><td>{t}</td></tr>'
        for n, p, t in OORDEEL)
    return (f'<table class="oordeel"><thead><tr><th class="s">Criterium</th><th class="p">Punten</th>'
            f'<th>Waarom</th></tr></thead><tbody>{rijen}'
            f'<tr class="tot"><td class="s">Totaal</td><td class="p">{TOTAAL}</td>'
            f'<td>{TOTAAL} van de 32 punten, cijfer {TOTAAL/32*10:.1f}. Drie onderdelen onder de twee '
            f'punten. Gezakt op beide voorwaarden van de cesuur.</td></tr></tbody></table>'
            .replace("cijfer 3.1", "cijfer 3,1"))

def gaptabel():
    kop = "".join(f'<th class="sk">{v}</th>' for v in ["Onvoldoende", "Voldoende", "Goed", "Uitstekend"])
    rijen = "".join(
        f'<tr><td class="s">{n.split(".")[0]}. {n.split(". ",1)[1]}</td><td class="p">{p}</td>'
        f'<td class="tr" colspan="4">{track(m, punten=p)}</td></tr>'
        for (n, p, _), m in zip(OORDEEL, MODEL))
    return (f'<table><thead><tr><th class="s">Criterium</th><th class="p">Punten</th>{kop}</tr></thead>'
            f'<tbody>{rijen}</tbody></table>')

# ---------------------------------------------------------------- antwoorden
antwoorden = sectie("Je twee vragen, hier beantwoord", (
  qa(I_ZAK,
     "Doet het model wat jullie doen bij een verslag dat niet voldoet?",
     "<b>Voor een deel.</b> Ik heb het verslag zelf tegen bijlage 6 versie 3.0 gelegd en kom uit op "
     f"<b>{TOTAAL} van de 32 punten</b>, met drie onderdelen op nul: de analyse, de conclusie en de klinische "
     "relevantie. Gezakt op allebei de voorwaarden van jullie cesuur, dus niet nipt.",
     "<b>Het model zakt ook, maar op &eacute;&eacute;n onderdeel in plaats van drie.</b> Het geeft alleen bij "
     "criterium 7 een Onvoldoende. Onder jullie cesuur is dat genoeg om te zakken, dus de eindconclusie klopt. "
     "Maar bij criterium 4 en 5 komt het op Voldoende uit waar het nul hoort te zijn, en dat maakt het verschil "
     "tussen een verslag dat op &eacute;&eacute;n punt tekortschiet en een verslag dat er ver vandaan zit.")
  + qa(I_INZET,
     "Waar zouden jullie dit kunnen inzetten?",
     "<b>Op de concepten, in de ronde v&oacute;&oacute;r het inleveren.</b> Het model loopt alle acht criteria "
     "even consequent langs en zet veertien opmerkingen in de tekst zelf, op de zin waar ze over gaan. De "
     "inhoudelijke observaties kloppen: het ziet dat de conclusie de vergelijking niet maakt, dat het opgevoerde "
     "conflicterende perspectief er geen is, en dat de plek in de evidencepiramide geen kwaliteitsbewijs is.",
     "<b>Niet op het eindoordeel.</b> Het probleem zit niet in wat het model ziet, maar in wat het er vervolgens "
     "aan hangt. Op criterium 4 en 5 schrijft het de reden voor een onvoldoende op en geeft dan een voldoende. "
     "Dat is een kwestie van de rubriektekst en dus op te lossen, maar het is er nu nog.")))

# ---------------------------------------------------------------- mijn oordeel
oordeel = sectie("Mijn beoordeling, criterium voor criterium", (
  '<p class="lead">Voorbeeld 1, rode gist rijst tegenover statines bij hypercholesterolemie, 17 maart 2025. '
  'Beoordeeld tegen bijlage 6 versie 3.0: per criterium 4, 2 of 0 punten.</p>'
  + kaart(oordeeltabel())
  + kaart('<p><b>Waarom gezakt, twee keer.</b> Jullie cesuur vraagt minimaal 18 punten in totaal '
          f'&eacute;n minimaal 2 punten op elk onderdeel. Dit verslag haalt {TOTAAL} punten en heeft drie '
          'onderdelen op nul. Elk van die twee is op zichzelf al genoeg.</p>'
          '<p><b>Wat dit niet is: een vergelijking met jullie oordeel.</b> Jouw ingevulde beoordelingsformulier '
          'bij dit verslag heb ik niet. Dit is mijn eigen beoordeling, gemaakt met de rubriek in de hand en '
          'onderbouwd met de tekst van het verslag. Wijkt hij af van die van jullie, dan is dat precies het '
          'gesprek dat ik zou willen voeren.</p>')))

# ---------------------------------------------------------------- de drie nullen
def nul(kop, eist, staat, waarom):
    return kaart(f'<h3>{kop}</h3>'
                 f'<p><b>Wat de rubriek vraagt.</b> {eist}</p>'
                 f'<p><b>Wat er staat.</b> {staat}</p>'
                 f'<p><b>Waarom dat nul is.</b> {waarom}</p>')

nullen = sectie("De drie onderdelen die op nul staan", (
  nul("Criterium 4 &middot; analyse binnen de praktijkcontext",
      "Ook voor twee punten: de artikelen analyseren op level of evidence &eacute;n op methodologische kwaliteit "
      "met behulp van de beoordelingsformulieren voor betrouwbaarheid, validiteit en generaliseerbaarheid, en per "
      "artikel benoemen welke onderdelen relevant zijn voor de CAT.",
      "Drie data-extractietabellen en per artikel een korte toelichting. Als sterke punten staan er: de auteur "
      "heeft vaker onderzoek gedaan, het onderzoek is van 2024 en het staat hoog in de piramide. Bij artikel 3 is "
      "het veld Interventie leeg gelaten.",
      "Het beoordelingsformulier uit bijlage 5.1 is op geen enkel artikel toegepast, en betrouwbaarheid, "
      "validiteit en generaliseerbaarheid komen per artikel niet voor. Productiviteit van de auteur, het jaartal "
      "en de plek in de piramide zijn geen methodologische kwaliteit. Daarmee is de onderbouwing van de sterke en "
      "zwakke punten niet alleen beperkt, maar gaat zij over iets anders dan wat het criterium vraagt.")
  + nul("Criterium 5 &middot; conclusie uit de resultaten",
      "Een kort en bondig antwoord op de klinische vraagstelling dat logisch voortvloeit uit de resultaten en "
      "alleen eerder genoemde informatie bevat. Onvoldoende is het onder meer als er onvoldoende antwoord is "
      "gegeven om de volledige onderzoeksvraag te beantwoorden.",
      "De conclusie is dat rode gist rijst een positief effect heeft op de verlaging van het lipidenprofiel en "
      "het LDL-cholesterol, en dat er verder onderzoek nodig is naar de bijwerkingen.",
      "De onderzoeksvraag luidt: wat is het effect van rode gist rijst op een daling van het LDL-cholesterol "
      "<i>in vergelijking met statines</i>. Over die vergelijking zegt de conclusie niets, terwijl het de kern van "
      "de vraag is. Daar komt bij dat artikel 1 de combinatie van rode gist rijst m&eacute;t statines onderzocht, "
      "zodat het bewijs de uitspraak over rode gist rijst alleen niet draagt.")
  + nul("Criterium 7 &middot; klinische relevantie en toepasbaarheid",
      "Concrete, actiegerichte handelingsalternatieven die uit het bewijs voortvloeien, met de implicaties voor "
      "patiënt en praktijk, de haalbaarheid, en hoe de aanbeveling gemonitord wordt. Twee of meer daarvan "
      "ontbreken is onvoldoende.",
      "Dat de POH de resultaten bespreekbaar kan maken als bekend is dat een patiënt rode gist rijst gebruikt, en "
      "twee aanbevelingen: vervolgonderzoek naar de veiligheid en vervolgonderzoek naar de bijwerkingen.",
      "Alle vier ontbreken. Vervolgonderzoek is een aanbeveling aan de wetenschap, niet een handelingsalternatief "
      "voor de praktijk. Er staat niet wat de POH bespreekt, wanneer, met welke informatie, wat dat voor de "
      "patiënt betekent, of dat binnen een spreekuur haalbaar is, en er staat geen evaluatiemoment.")))

# ---------------------------------------------------------------- waar het model te mild is
mild = sectie("Waar het model te mild is", (
  '<p class="lead">Dezelfde acht criteria, met mijn punten en het vakje dat Eduface koos. De balk is de ruimte '
  'die bij mijn punten past. Staat de stip rechts van de balk, dan is het model milder dan de rubriek toelaat.</p>'
  + kaart(gaptabel())
  + kaart(f'<h3>{I_HOOGTE} Twee keer buiten de band, en allebei op dezelfde manier</h3>'
        '<p>Op zes van de acht criteria valt het model binnen de ruimte die bij mijn punten past. Op criterium 4 '
        'en 5 niet: daar geeft het Voldoende waar het nul hoort te zijn.</p>'
        '<p><b>Het bijzondere is dat het model de reden zelf opschrijft.</b> Bij criterium 5 staat er letterlijk: '
        '<i>daardoor beantwoord je de volledige PICO-vraag onvoldoende</i>. Dat is bijna woordelijk de voorwaarde '
        'waaronder de rubriek nul punten voorschrijft. Bij criterium 4 staat er: <i>zonder methodologische '
        'koppeling blijven kwaliteit en toepasbaarheid onduidelijk</i>. Ook daar is de constatering raak en het '
        'vakje te hoog.</p>'
        '<p>Dat is goed nieuws voor de oplossing. Het model mist de observatie niet, het verbindt er de verkeerde '
        'stand aan. Dat zit in de tekst van de rubriekvakjes en is dus aan te passen, net zoals we dat op de twee '
        'inzendingen van Kas hebben gedaan.</p>')
  + kaart(f'<h3>{I_FORM} En &eacute;&eacute;n plek waar het model niet ver genoeg kijkt</h3>'
        '<p>Bij criterium 3 loopt het aantal hits in de zoektabel van 375 naar 9.391.035, dan naar 134, en daarna '
        'weer naar 1.528.289. Een zoekregel die met AND wordt uitgebreid kan niet meer resultaten opleveren dan de '
        'regel ervoor.</p>'
        '<p>Het model ziet de oorzaak: het schrijft <i>plaats haakjes rond PICO-elementen en licht AND/OR toe</i>. '
        'Maar het trekt de conclusie niet dat de zoekactie daardoor niet herhaalbaar is. Dat verschil, tussen een '
        'opmerking over de vorm en een oordeel over de zoekactie, is waarom ik hier op twee punten uitkom.</p>')))

verantwoording = sectie("Waarop dit oordeel rust", kaart(
  '<ul>'
  '<li><b>Waartegen is beoordeeld.</b> Bijlage 6 versie 3.0, hetzelfde formulier als jouw blanco exemplaar.</li>'
  '<li><b>Wie het oordeel gaf.</b> Ik, met de rubriek naast het verslag. Elke score in dit stuk is terug te voeren '
  'op een zin in het verslag en een voorwaarde in de rubriek.</li>'
  '<li><b>Wat Eduface ermee deed.</b> Hetzelfde verslag is door de rubriek gehaald die op de twee inzendingen van Kas is geijkt. Daaraan is voor dit verslag niets veranderd.</li>'
  '</ul>'))

body = (antwoorden + verantwoording + '<div style="break-before:page"></div>'
        + oordeel + nullen + mild)
html = pagina("CAT POH-6: het onvoldoende-voorbeeld beoordeeld", body,
              "logo-breederode.png", "logo-eduface.png")
pathlib.Path("onvoldoende-voorbeeld-cat-poh.html").write_text(html, encoding="utf-8")
print("punten:", [p for _, p, _ in OORDEEL], "totaal", TOTAAL, "cijfer", round(TOTAAL/32*10, 1))
print("html:", len(html) // 1024, "KB")
