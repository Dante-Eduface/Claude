# Case study: CAT EBP (POH), oude rubric v3.0

_Aangelegd 23-09-2026. Status: **stap 1 t/m 3 gedeeltelijk af, stap 4 t/m 7 geblokkeerd.** Zie "Wat er nog moet komen"._

Tweede vak waarop `grading-calibration` wordt losgelaten, na manuele therapie. Dit bestand is het werkdocument: materiaal, ground truth, de vaste rubric-basistekst en de openstaande gaten.

- **Opleiding:** POH (praktijkondersteuner huisarts), NLQF niveau 6
- **Opdrachttype:** CAT (Critically Appraised Topic), literatuuronderzoek naar een vraag uit de eigen huisartsenpraktijk. Zes stappen, verslag van max 6000 woorden
- **Beoordelaar (ground truth):** K.J. van Kruining, juni 2025
- **Bronrubric:** Bijlage 6 Beoordelingsformulier CAT **versie 3.0** (in de uploads: "Beoordelingsformulier Selma oude rubric"). Dante 23-09-2026: versie 4.0 expliciet **niet** gebruiken.
- **Studenten:** Eduface-labels "Student 1" (casus: kurkuma/curcumine bij verhoogd cholesterol) en "Student 2" (casus: vitamine D-suppletie bij obesitas)

> **Let op, privacy.** De aangeleverde bestanden heten "anoniem" maar zijn dat niet: de beoordelingsformulieren bevatten de echte naam en groep van de student. Ze staan daarom **niet** in deze repo, alleen in de sessie-scratchpad. Gebruik in Eduface en in dit bestand alleen "Student 1" en "Student 2".

## 1. Wat er is en wat ontbreekt

Tegen de checklist uit `reference.md` punt 2:

| # | Materiaal | Status | Bron |
|---|---|---|---|
| 1 | Origineel beoordelingsformulier | ✅ | Bijlage 6 CAT v3.0 (de "oude rubric") |
| 2 | Schrijfformat/instructiedocument met voorbeeld | ✅ | Bijlage 1 opdrachtbeschrijving v3, Bijlage 2 PICO-formulier, Bijlage 5.1 beoordelingsformulier betrouwbaarheid/validiteit/generaliseerbaarheid, Bijlage 7 schema kwalitatief/kwantitatief, plus 2 voorbeelddocumenten |
| 3 | Minstens 2 echte inzendingen | ✅ | Student 1 (5.436 woorden), Student 2 (5.383 woorden), beide compleet en beide geslaagd |
| 4 | Officiële beoordeling van de docent op diezelfde inzendingen | ✅ | Twee ingevulde beoordelingsformulieren, per criterium punten plus geschreven feedback |
| 5 | Losse conceptcommentaar van de docent (Word-comments) | ❌ | Geen enkel aangeleverd bestand bevat comments. Gecontroleerd op `word/comments.xml` en op PDF-annotaties: nul. |
| 6 | Huidige live rubric + modelinstructies in Eduface | ⚠️ half | Rubric aangeleverd 23-09-2026 (Descriptive, 4 vakjes), zie sectie 6. **Modelinstructies ontbreken nog.** |
| 7 | Huidige AI-uitkomst op diezelfde inzendingen | ❌ | **Blokkerend** |

Materiaal 5 is hier minder erg dan bij manuele therapie, want het officiële beoordelingsformulier bevat zélf per criterium uitgeschreven `+` / `+/-` / `-`-commentaar. Dat levert het drempelbewijs dat bij manuele therapie alleen uit de Word-comments te halen was. Zie sectie 4.

## 2. Ground truth: wat de docent gaf

Bronrubric scoort per criterium **4, 2 of 0 punten**. Acht criteria, dus maximaal 32 punten. Cesuur: **minimaal 18 punten totaal én elk individueel onderdeel minimaal 2 punten**.

| # | Criterium | Student 1 | Student 2 |
|---|---|---|---|
| 1 | Aanleiding klinische vraag vanuit EBP-principe | 4 | 4 |
| 2 | Eenduidige methodologische onderzoeksvraag (PICO) | 4 | 2 |
| 3 | Wetenschappelijke databanken en weging van informatie | 2 | 2 |
| 4 | Analyseert onderzoeksresultaten in eigen praktijkcontext | 4 | 2 |
| 5 | Formuleert een conclusie uit de resultaten | 2 | 2 |
| 6 | Kritische inhoudelijke discussie | 4 | 4 |
| 7 | Klinische relevantie en toepasbaarheid | 2 | 4 |
| 8 | Reflectie op werkwijze en rolontwikkeling | 4 | 3 |
| | **Totaal** | **26 → 8,1** | **23 → 7,2** |

Beide totalen kloppen precies met `punten / 32 × 10`. Daaruit volgt dat de acht criteria in de bron **gelijk wegen**, 12,5% elk. Eduface staat nu op 12% voor de eerste zeven en 16% voor reflectie, zie sectie 6.

**De ground truth: 16 van de 16 criteriumoordelen zijn geslaagd.** Geen enkel criterium is bij geen van beide studenten gezakt. Elke Unsatisfactory die de AI op deze twee inzendingen produceert is dus per definitie een fout.

Twee kanttekeningen bij dit testset:
- Het detecteert alleen **overstrengheid**, niet oversoepelheid. Daarvoor is een inzending nodig die de docent wél liet zakken, mét haar beoordeling.
- Bij criterium 8 gaf de docent Student 2 een **3**, een score die niet in de 4/2/0-schaal bestaat. Ze houdt zich dus niet strikt aan haar eigen schaal.

## 3. Het structurele probleem: drie niveaus in, vier niveaus uit

Dit vak brengt een probleem mee dat manuele therapie niet had.

De bronrubric heeft **drie** niveaus: 4, 2 en 0 punten. Dante heeft in Eduface bewust het **Descriptive**-rubrictype met **vier** vakjes gekozen: Unsatisfactory, Satisfactory, Good, Great (23-09-2026). Drie niveaus moeten dus over vier vakjes verdeeld worden, en dat gaat niet zonder een keuze.

De cesuur van de bron is hard: **elk individueel onderdeel minimaal 2 punten**, plus minimaal 18 punten totaal. Vertaald naar vier vakjes kan de zaklijn maar op één plek liggen:

> **Unsatisfactory = 0 punten = zakken. Satisfactory, Good en Great zijn alle drie een voldoende (2 of 4 punten in de bron).**

Er is geen vierde niveau in de bron, dus Good is een geïnterpoleerd vakje. Dat is niet erg, zolang Satisfactory maar de ondergrens van "geslaagd" blijft en niet stiekem de 0-puntenkolom beschrijft. Precies daar gaat het in de huidige Eduface-rubric mis, zie sectie 6.

## 4. Ground truth vertaald naar de vier Eduface-vakjes

De harde eis, afgeleid uit sectie 2: **geen van de 16 criteriumoordelen mag Unsatisfactory zijn.** Elke Unsatisfactory op deze twee inzendingen is een fout, punt.

Daarnaast is er een zachtere eis: het vakje zou de punten van de docent moeten volgen. Door haar geschreven commentaar naast de vier Eduface-teksten te leggen valt per criterium af te leiden welk vakje ze feitelijk beschrijft:

| # | Criterium | Student 1 (punten → verwacht vakje) | Student 2 (punten → verwacht vakje) |
|---|---|---|---|
| 1 | Aanleiding | 4 → Great | 4 → Great |
| 2 | PICO | 4 → Great | 2 → Satisfactory |
| 3 | Zoekstrategie | 2 → **Good** | 2 → **Good** |
| 4 | Analyse | 4 → Great | 2 → Satisfactory |
| 5 | Conclusie | 2 → **Good** | 2 → **Good** |
| 6 | Discussie | 4 → Great | 4 → Great |
| 7 | Klinische relevantie | 2 → Satisfactory | 4 → Great |
| 8 | Reflectie | 4 → Great | 3 → Satisfactory/Good |

Let op de vetgedrukte rijen. Bij criterium 3 en 5 gaf de docent 2 punten, maar beschrijft haar eigen commentaar letterlijk het **Good**-vakje, niet Satisfactory:

- **Criterium 3.** Satisfactory eist "minimaal één wetenschappelijke databank en **één** relevant wetenschappelijk artikel... herhaalbaarheid of onderbouwing van de artikelkeuze is beperkt". Good eist "minimaal **drie** relevante artikelen... keuze onderbouwd... grotendeels herhaalbaar". De docent schreef bij beide studenten: "Er zijn 3 artikelen geselecteerd en keuze wordt onderbouwd" en "Zoekstrategie is wel voldoende herhaalbaar". Dat is Good.
- **Criterium 5.** Good luidt "kort en duidelijk antwoord dat grotendeels aansluit, uitsluitend eerder beschreven informatie, maar **niet volledig stellig geformuleerd**". De docent schreef bij beide studenten: "Duidelijk antwoord op de vraagstelling", "De conclusie vloeit logisch op vanuit eerdere informatie", "De conclusie is nu niet in stellende vorm geformuleerd". Dat is woord voor woord Good.

De schaal loopt dus niet gelijk met de bron: de docent haar "2 punten" valt soms op Satisfactory en soms op Good. Dat is op zichzelf geen probleem, zolang geen van beide een Unsatisfactory oplevert.

## 5. Het drempelbewijs, al vóór de baseline

Bij manuele therapie kostte het de Word-comments van de docent om aan te tonen dat het gat een drempelgat is en geen kennisgat. Hier levert het officiële beoordelingsformulier dat bewijs zelf.

**Criterium 7, Student 1, scoorde 2 punten = geslaagd.** De docent schreef er zelf bij:

> `--Er is geen expliciete onderbouwing waarom deze aanpak haalbaar is in de praktijk (bijv. "laag in kosten", "vrij verkrijgbaar bij apotheek/natuurwinkel" of "geen recept nodig").`
>
> `--Onderbouwing hoe aanbeveling gemonitord kan worden niet of te beperkt beschreven (...)`

De bron vraagt bij dit criterium vier dingen: aanbevelingen, implicaties, haalbaarheid, monitoring. De docent stelt vast dat **twee van die vier ontbreken**. De 0-puntenkolom van diezelfde bronrubric zegt letterlijk "bij 2 of meer vastgestelde criteria = onvoldoende". Ze past haar eigen regel dus niet toe en laat het slagen.

Hetzelfde patroon elders:

- **Criterium 4, Student 2 (2 punten):** drie `+/-`-punten met stevige inhoudelijke kritiek. "Setting" is fout toegepast en "mist nu in zijn geheel op correcte wijze in analyse", auteursvermelding klopt niet bij twee artikelen, APA-verwijzingen staan niet altijd op de juiste plek. Toch geslaagd.
- **Criterium 8, Student 2 (3 punten):** vier van de vijf reflectieonderdelen krijgen een `+/-`, en op één vereist onderdeel staat "er wordt niet expliciet gereflecteerd op wat de aanpak in de toekomst beter of anders zou zijn". Toch geslaagd.
- **Criterium 3, Student 1 (2 punten):** zoektermen summier, gedachtegang niet toegelicht. Toch geslaagd.

Conclusie: deze docent behandelt een ontbrekend onderdeel als **groeifeedback binnen een voldoende**, niet als een fail. Dat is mechanisme 2 uit `reference.md` punt 4, en het is hier hard aantoonbaar zonder de AI-uitkomst gezien te hebben.

## 6. De huidige Eduface-rubric, en wat eraan mankeert

Aangeleverd door Dante op 23-09-2026. Type Descriptive, vier vakjes. Gewichten: 12% voor criterium 1 tot en met 7, **16% voor criterium 8 (reflectie)**, samen 100%.

Dit is materiaal 6 uit de checklist, het rubricdeel. De modelinstructies ontbreken nog.

### Drie tekstproblemen, alle drie uit de vergelijking met de bron

Dit zijn geen vermoedens over de AI, het zijn verschillen tussen de Eduface-tekst en de bronrubric die je kunt aanwijzen. Of ze ook echt bijten blijkt pas uit de baseline.

**Probleem 1, en het grootste: op drie criteria beschrijft het Satisfactory-vakje de 0-puntensituatie uit de bron.** Daarmee is Satisfactory geen ondergrens van geslaagd meer, maar een verkapte onvoldoende, en schuift de hele schaal een vakje omhoog.

| Criterium | Wat Satisfactory nu zegt | Wat de bron daarover zegt |
|---|---|---|
| 3 Zoekstrategie | "minimaal één wetenschappelijke databank en **één** relevant wetenschappelijk artikel gebruikt" | 2 punten eist **minimaal 3** artikelen. "1 of minder" staat in de 0-puntenkolom. |
| 5 Conclusie | "omslachtig en/of bevat informatie die niet eerder is beschreven" | Dat is letterlijk de 0-puntentekst: "bevat ook informatie die nog niet eerder is benoemd. Het antwoord is omslachtig beschreven." |
| 2 PICO | "PICO-elementen zijn onvolledig, onduidelijk of niet allemaal herkenbaar opgenomen" | "niet herkenbaar in de onderzoeksvraag opgenomen" staat in de 0-puntenkolom. Bij 2 punten zijn **alle** elementen herkenbaar. |

Gevolg: een student die volgens de docent een dikke voldoende haalt, kan bij deze drie criteria niet lager dan Good scoren zonder dat het feitelijk onjuist is. Er is geen ruimte meer tussen "geslaagd" en "gezakt".

**Probleem 2: de "bij 2 of meer = onvoldoende"-regel is verdwenen.** De bron zet die drempel expliciet bij criterium 3, 6 en 7: pas als twee of meer tekortkomingen zijn vastgesteld, is het onvoldoende. In de Eduface-tekst staat die regel nergens. Zonder die regel kan één ontbrekend onderdeel al een Unsatisfactory opleveren, terwijl de bron er twee eist. Dit is dezelfde drempel die de docent in sectie 5 aantoonbaar zelf toepast.

**Probleem 3: reflectie weegt 16% terwijl de bron alle acht criteria gelijk weegt.** In de bron is elk criterium maximaal 4 punten van de 32, dus 12,5%. Beide studentcijfers kloppen exact met die gelijke weging (26/32 = 8,1 en 23/32 = 7,2). Dat 16% is dus een afwijking van de bron. Weegt minder zwaar dan de andere twee, omdat het eindoordeel in Eduface een handmatige keuze van de docent is en geen optelsom (`reference.md` punt 1), maar het klopt niet met het bronformulier.

### De voorgestelde tekstwijzigingen

Nog niet doorvoeren. Dit zijn de exacte, minimale ingrepen die klaarstaan zodra de baseline bevestigt dat ze nodig zijn. De rest van de rubric blijft ongemoeid.

**Criterium 3, Satisfactory.** Vervang "minimaal één wetenschappelijke databank en één relevant wetenschappelijk artikel gebruikt" door "minimaal één wetenschappelijke databank gebruikt en minimaal drie wetenschappelijke artikelen geselecteerd". Reden: de bron eist drie artikelen op het laagste geslaagde niveau.

**Criterium 5, Satisfactory.** Haal "en/of bevat informatie die niet eerder is beschreven" weg; dat hoort bij Unsatisfactory en staat daar ook al. Laat staan: "De conclusie geeft gedeeltelijk antwoord op de klinische vraagstelling, maar is onvoldoende volledig of niet duidelijk logisch afgeleid uit de resultaten. Het antwoord is omslachtig."

**Criterium 2, Satisfactory.** Vervang "De PICO-elementen zijn onvolledig, onduidelijk of niet allemaal herkenbaar opgenomen" door "De PICO-elementen zijn herkenbaar opgenomen, maar niet alle elementen zijn even volledig in de onderzoeksvraag doorgetrokken". Reden: bij 2 punten eist de bron dat alle elementen herkenbaar zijn; de tekortkoming zit in de uitwerking, niet in de herkenbaarheid. Dit dekt precies wat Student 2 deed: de C zat wel in de PICO maar niet in de onderzoeksvraag.

**Criterium 3, 6 en 7, Unsatisfactory.** Zet aan het begin van elk van deze drie Unsatisfactory-teksten: "Dit niveau geldt pas wanneer twee of meer van de onderstaande punten zijn vastgesteld." Reden: die drempel staat letterlijk in de bron en is nu weg.

**Gewichten.** Zet alle acht op 12,5%, of laat het zoals het is en noteer dat het bewust afwijkt. Keuze van Dante.

## 7. De toon van de docent, en de modelinstructies-tekst

Uit haar eigen feedback op beide formulieren:

- **Bullets met een expliciete markering per bevinding:** `+` sterk, `+/-` deels, `-` of `--` tekort. Geen lopende tekst, geen kopjes.
- **Tweede persoon, direct en informeel.** "Je trekt zélf de conclusie dat...", "al had je beschrijvende wijs nog wel meer mogen stilstaan", "je haalt al zaken aan die eigenlijk in de discussie aan bod mogen komen..".
- **Elk tekort krijgt een concreet voorbeeld of een concrete suggestie**, vaak tussen haakjes. "bijvoorbeeld bij 'P' mis ik 'high cholesterol/elevated cholesterol/lipid disorder/total cholesterol'". "(bijv. via bloedonderzoek naar cholesterolwaarden, bijwerkingen navragen, medicatiegebruik checken, etc.)". Nooit een kale constatering.
- **Sterk en zwak staan naast elkaar binnen hetzelfde criterium**, en een tekort verlaagt het vakje niet automatisch.
- **Kort compliment waar verdiend**, los op een regel: "Complimenten!", "dat is sterk".
- **Geen vaste openingszin.** Ze varieert per criterium. Lengte loopt van één zin tot ongeveer 120 woorden.
- **Vakinhoudelijk concreet.** Ze noemt MeSH-termen, de C uit de PICO, level of evidence, NHG-richtlijnen en APA-plaatsing bij naam.

In te voeren via "Beschrijf je feedbackstijl" en dan "Opnieuw genereren". Dat is de enige route; modelinstructies zijn niet rechtstreeks bewerkbaar. Reken op verlies, zie `reference.md` punt 7: voorbeeldzinnen en de sectie Inline opmerkingen overleefden bij manuele therapie nooit.

```
BELANGRIJK: vat het onderstaande niet samen en laat geen van de onderdelen weg.

Context: dit is een CAT (Critically Appraised Topic) van een student van de opleiding
praktijkondersteuner huisarts (POH), NLQF niveau 6. Een literatuuronderzoek van maximaal
6000 woorden naar een vraag uit de eigen huisartsenpraktijk, met PICO, zoekstrategie,
data-extractietabel, conclusie, discussie, klinische relevantie en reflectie.

Algemene feedback: schrijf per criterium een lijst losse bevindingen, geen lopende tekst
en geen kopjes. Markeer elke bevinding met + wanneer het goed is, +/- wanneer het er is
maar beter kon, en - wanneer het ontbreekt. Spreek de student aan met je. Schrijf
informeel en vakinhoudelijk concreet: noem MeSH-termen, PICO-elementen, level of
evidence, NHG-richtlijnen en APA bij naam. Geef bij elk tekort een concreet voorbeeld of
een concrete suggestie tussen haakjes, nooit een kale constatering. Benoem sterke en
zwakke punten binnen hetzelfde criterium naast elkaar. Maximaal 80 woorden per criterium.
Varieer de opening, gebruik nooit twee keer dezelfde openingszin.

Beoordelingsstrengheid: Satisfactory is al een voldoende, niet een waarschuwing. Kies
Unsatisfactory alleen wanneer de Unsatisfactory-tekst van dat criterium als geheel van
toepassing is. Een onderdeel dat aanwezig is maar beknopt, of dat op onderdelen beter had
gekund, is minimaal Satisfactory. Een ontbrekend detail is groeifeedback binnen een
voldoende, geen reden om een vakje lager te gaan. Bij de criteria zoekstrategie, discussie
en klinische relevantie geldt Unsatisfactory pas wanneer twee of meer tekortkomingen uit
die tekst zijn vastgesteld.
```

## 8. Wat er nog moet komen

**Blokkerend, van Dante:**

1. **De huidige modelinstructies in Eduface** voor dit vak, via "Bekijk modelinstructies", letterlijk overgenomen. De rubric is er nu wel, de instructies nog niet.
2. **De huidige AI-uitkomst op deze twee inzendingen** onder die configuratie: de `Feedback_Summary.pdf` per student via de knop "Inzendingen". Dat is de baseline waar stap 2 en 3 op draaien. Dante heeft aangekondigd deze aan te leveren.

**Vragen, niet zelf ingevuld:**

3. Blijft reflectie op 16%, of gaan alle acht naar 12,5% zoals in de bron? Zie sectie 6, probleem 3.
4. Horen de randvoorwaarden (APA-7, max 6000 woorden, inhoudsopgave, lettertype, Word-format) als extra criterium in Eduface, of blijven ze bij de docent? Ze staan in de bron als aparte poortlijst die niet meetelt in het cijfer, en de helft ervan kan de AI niet vaststellen. Nu staan ze nergens in de Eduface-rubric.
5. "Voorbeeld 1 verslag resultaat onvoldoende" en "Voorbeeld 2 beoordeling goed" horen niet bij elkaar: het eerste is een verslag zonder beoordelingsformulier, het tweede een beoordelingsformulier (30 punten, 9,4) zonder verslag. Klopt dat, en is "Voorbeeld 1" een afgekeurde CAT of een CAT met een zwak hoofdstuk Resultaten?
6. Is er een inzending die de docent **wel** heeft laten zakken, met haar beoordeling erbij? Zonder die kan dit testset alleen overstrengheid aantonen, geen oversoepelheid.
7. Is K.J. van Kruining dezelfde docent als "Selma" uit de bestandsnaam van de rubric, of zijn dat twee mensen?

**Daarna, zodra 1 en 2 er zijn:**

Vier Eduface-opdrachten, allemaal vanuit exact dezelfde vaste rubrictekst (baseline, alleen rubric, alleen instructies, beide). Beide studenten door elke variant halen en vergelijken op twee assen apart: klopt het oordeel (harde eis: nul keer Unsatisfactory; zachte eis: het vakje volgt de tabel in sectie 4), en klopt de toon.

**Let op bij het opzetten van de varianten.** De rubric uit sectie 6 is vanaf nu de vaste basistekst. Nooit een verse auto-generatie uit het bronbestand als controle gebruiken, die is elke keer anders (`reference.md` punt 6). Plak in elke opdracht dezelfde letterlijke tekst.
