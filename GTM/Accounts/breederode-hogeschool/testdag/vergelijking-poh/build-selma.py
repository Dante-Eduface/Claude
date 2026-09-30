# -*- coding: utf-8 -*-
"""Document voor Selma de Nijs: haar onvoldoende-voorbeeld door het model.

Voorbeeld 1 (rode gist rijst, 17 maart 2025), het verslag dat zij als onvoldoende
voorbeeld gebruikt. Er is geen ingevuld beoordelingsformulier bij, dus dit is geen
vergelijking maar een controle van de modelfeedback tegen het verslag zelf.
Opmaak in stijl.py.
"""
import pathlib
from stijl import sectie, kaart, qa, track, pagina, I_ZAK, I_INZET, I_ZIEN, I_BETER

C = ["1. Aanleiding van de klinische vraag",
     "2. Onderzoeksvraag op basis van PICO",
     "3. Databanken en weging van informatie",
     "4. Analyse binnen de praktijkcontext",
     "5. Conclusie uit de resultaten",
     "6. Kritische inhoudelijke discussie",
     "7. Klinische relevantie en toepasbaarheid",
     "8. Reflectie en rolontwikkeling"]

UITKOMST = ["Goed", "Goed", "Goed", "Voldoende", "Voldoende", "Voldoende", "Onvoldoende", "Voldoende"]

def uitkomsttabel():
    kop = "".join(f'<th class="sk">{v}</th>' for v in ["Onvoldoende", "Voldoende", "Goed", "Uitstekend"])
    body = "".join(f'<tr><td class="s">{n}</td>'
                   f'<td class="tr" colspan="4">{track(w, grens=True)}</td></tr>'
                   for n, w in zip(C, UITKOMST))
    return (f'<table class="zonderpunten"><thead><tr><th class="s">Criterium</th>{kop}</tr></thead>'
            f'<tbody>{body}<tr class="tot"><td colspan="5">Eindoordeel in Eduface: Voldoende. '
            f'Onder jullie cesuur: gezakt.</td></tr></tbody></table>')

# ---------------------------------------------------------------- de antwoorden
antwoorden = sectie("Je twee vragen, hier beantwoord", (
  qa(I_ZAK,
     "Doet het model wat jullie doen bij een verslag dat niet voldoet?",
     "<b>Ja. Op het verslag dat jij als onvoldoende voorbeeld gebruikt komt het model op een Onvoldoende uit, bij "
     "criterium 7, klinische relevantie en toepasbaarheid.</b> Onder jullie cesuur is dat zakken, want elk "
     "onderdeel moet minimaal 2 punten halen, hoe goed de rest ook is. Dit is de eerste keer dat het model op dit "
     "vak een Onvoldoende geeft, en het gebeurt op de inzending waar dat hoort.",
     "<b>Let wel op wat Eduface er zelf van maakt.</b> Het eindoordeel bovenaan staat op Voldoende, want dat is "
     "een weging over de acht criteria en niet jullie cesuur. De examinator zet het cijfer zelf, dus aan de "
     "uitkomst verandert het niets, maar ga niet op dat ene woord af.")
  + qa(I_INZET,
     "Waar zouden jullie dit kunnen inzetten?",
     "<b>Op de concepten, in de ronde v&oacute;&oacute;r het inleveren.</b> Het model loopt alle acht criteria "
     "even consequent langs en zet veertien opmerkingen in de tekst zelf, op de zin waar ze over gaan. Drie "
     "daarvan raken precies de redeneerfouten die dit verslag onvoldoende maken. Die staan hieronder.",
     "<b>Niet op het eindoordeel, en nog niet zonder nalezen.</b> Op vier plekken is deze feedback nog niet goed "
     "genoeg om zo naar een student te gaan. Ook die staan hieronder, met wat eraan zou moeten veranderen.")))

# ---------------------------------------------------------------- de uitkomst
uitkomst = sectie("Wat het model op dit verslag doet", (
  '<p class="lead">Voorbeeld 1, rode gist rijst tegenover statines bij hypercholesterolemie, 17 maart 2025.</p>'
  '<p class="legend">De stip <span class="d"></span> is het vakje dat het model koos. De dikke lijn '
  '<span class="z"></span> is jullie zaklijn per onderdeel: alles links daarvan haalt de 2 punten niet.</p>'
  + kaart(uitkomsttabel())
  + kaart('<p><b>Wat dit niet is: een vergelijking.</b> Jouw ingevulde beoordelingsformulier bij dit verslag heb '
          'ik niet, dus criterium voor criterium naast elkaar leggen kan hier niet. Wat hierboven staat is wat het '
          'model doet. Wat hieronder staat is mijn eigen controle van die feedback tegen het verslag zelf, dus '
          'niet tegen jullie oordeel.</p>')))

# ---------------------------------------------------------------- wat het goed zag
goed = sectie("Wat het model goed zag", (
  kaart(f'<h3>{I_ZIEN} Drie redeneerfouten, alle drie nagekeken in het verslag</h3>'
        '<ul>'
        '<li><b>De conclusie beantwoordt de onderzoeksvraag niet.</b> De vraag is wat rode gist rijst doet '
        '<i>in vergelijking met statines</i>. De conclusie zegt alleen dat rode gist rijst een positief effect '
        'heeft op het LDL-cholesterol. Het model benoemt dat bij criterium 5 en verbindt het aan artikel 1, dat '
        'de combinatie van rode gist rijst met statines onderzocht en dus geen vergelijking oplevert.</li>'
        '<li><b>Het conflicterende perspectief is er geen.</b> De student zet twee bevindingen tegenover elkaar '
        'die allebei een LDL-verlaging beschrijven. Het model zegt dat, en zegt erbij wat w&eacute;l een '
        'tegenstelling zou zijn: werkzaamheid als alternatief voor statines tegenover onzekerheid over de '
        'veiligheid.</li>'
        '<li><b>De plek in de evidencepiramide is geen kwaliteitsbewijs.</b> De student gebruikt bij alle drie de '
        'artikelen "staat bovenaan in de piramide" als argument. Het model zet daar heterogeniteit, dosering, '
        'aansluiting op de PICO en de Nederlandse toepasbaarheid tegenover.</li>'
        '</ul>')))

# ---------------------------------------------------------------- de verbeterpunten
def vb(kop, *alineas):
    return kaart(f'<h3>{kop}</h3>' + "".join(f"<p>{a}</p>" for a in alineas))

beter = sectie("Wat er aan deze feedback nog niet deugt", (
  '<p class="lead">Vier punten, op volgorde van wat ze kosten. Het eerste raakt het niveau van een criterium, '
  'de andere drie de bruikbaarheid van de opmerkingen.</p>'
  + vb("1. Criterium 3 staat op Goed terwijl de zoektabel zichzelf tegenspreekt",
       "In de zoekstrategietabel loopt het aantal hits van 375 naar 9.391.035, dan naar 134, en daarna weer naar "
       "1.528.289. Een zoekregel die met AND wordt uitgebreid kan niet meer resultaten opleveren dan de regel "
       "ervoor. Er is dus iets mis met de opbouw van de zoekactie zelf, en dat is precies waar criterium 3 over "
       "gaat.",
       "Het model ziet de oorzaak wel: het schrijft <i>plaats haakjes rond PICO-elementen en licht AND/OR toe</i>. "
       "Maar het behandelt dat als een vormkwestie en laat het niveau op Goed staan. Wat er zou moeten staan: dat "
       "het aantal hits na het toevoegen van de C-regel van 134 naar ruim anderhalf miljoen springt, dat de OR "
       "daardoor breder bindt dan bedoeld, en dat de zoekactie zoals opgeschreven niet te herhalen is.")
  + vb("2. Er is in &eacute;&eacute;n databank gezocht en dat wordt nergens benoemd",
       "Het criterium heet gebruik van wetenschappelijke databanken, meervoud. Er is alleen in PubMed gezocht. De "
       "student ziet het zelf: in haar reflectie schrijft ze dat ze een volgende keer meerdere databanken zou "
       "gebruiken. Het model noemt PubMed wel, maar nergens als beperking, en prijst de zoekstrategie juist.")
  + vb("3. Hetzelfde punt staat vier keer",
       "Dat artikel 1 rode gist rijst m&eacute;t statines onderzoekt en dus geen directe vergelijking oplevert, "
       "staat bij criterium 2, bij criterium 5, en twee keer als losse opmerking op dezelfde alinea in het "
       "hoofdstuk Resultaten. Die twee opmerkingen zeggen bijna hetzelfde ding op dezelfde plek.",
       "E&eacute;n plek waar het het niveau bepaalt, plus &eacute;&eacute;n opmerking in de tekst, is genoeg. Vier "
       "keer leest als drammen en haalt de aandacht weg bij de andere punten.")
  + vb("4. Twee dingen in de data-extractietabellen blijven onbesproken",
       "Bij artikel 1 en artikel 2 staat als sterk punt: <i>auteur heeft vaker onderzoek gedaan, dit zegt iets "
       "over de betrouwbaarheid</i>. Dat is geen kwaliteitscriterium voor een studie, en criterium 4 gaat juist "
       "over de methodologische analyse.",
       "Bij artikel 3 staat in de tabel level of evidence 1B, terwijl de tekst erboven zegt dat ook dit artikel "
       "bovenaan de piramide staat. Het model gaat op geen van beide in.")))

verantwoording = sectie("Hoe dit tot stand is gekomen", kaart(
  '<ul>'
  '<li><b>Wat erin is gegaan.</b> Het verslag Voorbeeld 1 en bijlage 6 versie 3.0 als rubriek. Dat is dezelfde '
  'rubriek als op jouw blanco formulier staat: acht criteria, 4, 2 of 0 punten, cesuur 18 punten plus minimaal 2 '
  'per onderdeel.</li>'
  '<li><b>Waarop de rubriek is geijkt.</b> Op twee CAT\'s uit juni 2025 met de ingevulde formulieren van Kas '
  'ernaast. Die kalibratie is hier ongewijzigd toegepast: aan de rubriek is voor dit verslag niets veranderd.</li>'
  '</ul>'))

body = (antwoorden + '<div style="break-before:page"></div>'
        + uitkomst + goed + beter + verantwoording)
html = pagina("CAT POH-6: het onvoldoende-voorbeeld door het model", body,
              "logo-breederode.png", "logo-eduface.png")
pathlib.Path("onvoldoende-voorbeeld-cat-poh.html").write_text(html, encoding="utf-8")
print("html:", len(html) // 1024, "KB")
