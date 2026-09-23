# Case study: CAT EBP (POH), oude rubric v3.0

_Aangelegd 23-09-2026, bijgewerkt 23-09-2026. Status: **ronde 3 gemeten. 16 van 16 binnen bandbreedte. Klaar om te gebruiken, met één bekende beperking.**_

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
| 6 | Huidige live rubric + modelinstructies in Eduface | ⚠️ half | Rubric aangeleverd 23-09-2026 (Descriptive, 4 vakjes), zie sectie 6. Modelinstructies zijn door Dante aangepast maar de **tekst ervan is nog niet aangeleverd**. |
| 7 | Huidige AI-uitkomst op diezelfde inzendingen | ✅ | Export `Inzendingen_CAT_23-09-2026_3.zip`: per student een Feedback_Summary.pdf plus een Comments.docx met de inline opmerkingen. Zie sectie 8. |

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

## 7. De toon van de docent

Uit haar eigen feedback op beide formulieren:

- **Bullets met een expliciete markering per bevinding:** `+` sterk, `+/-` deels, `-` of `--` tekort. Geen lopende tekst, geen kopjes.
- **Tweede persoon, direct en informeel.** "Je trekt zélf de conclusie dat...", "al had je beschrijvende wijs nog wel meer mogen stilstaan", "je haalt al zaken aan die eigenlijk in de discussie aan bod mogen komen..".
- **Elk tekort krijgt een concreet voorbeeld of een concrete suggestie**, vaak tussen haakjes. "bijvoorbeeld bij 'P' mis ik 'high cholesterol/elevated cholesterol/lipid disorder/total cholesterol'". "(bijv. via bloedonderzoek naar cholesterolwaarden, bijwerkingen navragen, medicatiegebruik checken, etc.)". Nooit een kale constatering.
- **Sterk en zwak staan naast elkaar binnen hetzelfde criterium**, en een tekort verlaagt het vakje niet automatisch.
- **Kort compliment waar verdiend**, los op een regel: "Complimenten!", "dat is sterk".
- **Geen vaste openingszin.** Ze varieert per criterium. Lengte loopt van één zin tot ongeveer 120 woorden.
- **Vakinhoudelijk concreet.** Ze noemt MeSH-termen, de C uit de PICO, level of evidence, NHG-richtlijnen en APA-plaatsing bij naam.

Dit is het kalibratiedoel voor de modelinstructies. De tekst zelf staat in sectie 10, variant I, nu de baseline laat zien wat er precies misgaat.

## 8. De baselinemeting

Export van 23-09-2026 (`Inzendingen_CAT_23-09-2026_3.zip`), op de rubric uit sectie 6 met door Dante aangepaste modelinstructies. Dit is de baseline.

De PDF toont de vakjes in het Nederlands. Unsatisfactory verschijnt als "Onvoldoende", Satisfactory als "Voldoende", Good als "Goed". **Het label voor Great hebben we nog niet gezien, want dat vakje is geen enkele keer gebruikt.**

| # | Criterium | Docent S1 | AI S1 | Docent S2 | AI S2 |
|---|---|---|---|---|---|
| 1 | Aanleiding | Great | Good | Great | Good |
| 2 | PICO | Great | Satisfactory | Satisfactory | Good |
| 3 | Zoekstrategie | Good | Satisfactory | Good | **Good ✓** |
| 4 | Analyse | Great | Satisfactory | Satisfactory | **Satisfactory ✓** |
| 5 | Conclusie | Good | **Good ✓** | Good | **Good ✓** |
| 6 | Discussie | Great | Good | Great | Good |
| 7 | Klinische relevantie | Satisfactory | **Satisfactory ✓** | Great | Satisfactory |
| 8 | Reflectie | Great | Satisfactory | Satisfactory/Good | **Satisfactory ✓** |

Totaalcijfer in beide PDF's: "SOUND". Dat lijkt een onvertaald label, en het is bij beide studenten gelijk.

### Wat goed gaat

**De zaklijn klopt. Nul keer Unsatisfactory, op 16 van de 16 criteriumoordelen.** Dat was de harde eis uit sectie 4 en die is gehaald. De rubric laat beide studenten overal slagen, net als de docent. Dat is het belangrijkste en het is meteen raak.

### Wat niet goed gaat

**1. Het plafond wordt nooit aangeraakt.** De AI gaf 0 keer Great. De docent gaf 9 van de 16 keer 4 punten, dus Great. Alle 16 AI-oordelen zitten in de twee middelste vakjes. Van een vierpuntsschaal blijven er feitelijk twee over.

**2. De rangorde klapt om.** De docent zette Student 1 duidelijk boven Student 2: 26 tegen 23 punten, 8,1 tegen 7,2. De AI geeft Student 1 drie keer Good en vijf keer Satisfactory, en Student 2 vijf keer Good en drie keer Satisfactory. De AI zet de zwakkere CAT dus hoger. Het model onderscheidt de twee studenten niet alleen verkeerd, het draait ze om.

**3. Systematische onderschatting, sterker bij de betere student.** In vakjesstappen geteld (Unsatisfactory 1 tot Great 4) zit Student 1 negen stappen te laag over acht criteria, Student 2 ongeveer drie. Hoe beter de inzending, hoe groter het gat. Dat volgt uit punt 1: wie een 4 verdient kan die niet krijgen.

## 9. Diagnose, uit de eigen tekst van de AI

Conform `reference.md` punt 4: niet raden waaróm het model afwijkt, maar het uit zijn eigen feedback halen. Drie mechanismen, en ze vragen verschillende fixes.

### A. De AI toetst aan een systematic-review-standaard die nergens in de opdracht staat

Wat de AI eist, letterlijk uit de feedback en de inline opmerkingen:

- "Voeg per artikel effectgroottes, betrouwbaarheidsintervallen, uitvalpercentages en een biasbeoordeling toe" (S1, criterium 4)
- "Specificeer voor elke lipidenparameter de effectgrootte, het betrouwbaarheidsinterval en de p-waarde" (S1, inline)
- "Noteer per zoekactie syntax, termen, filters, datum en hits" (S1, criterium 3)
- "vermeld veldlabels, Booleaanse operatoren, filters, zoekdatum en het aantal resultaten per zoekactie" (S1, inline)
- "controleer per zoekstring haakjes, MeSH-termen, filters, hitcijfers en datum" (S2, criterium 3)

**Geen van deze eisen staat in de rubric, en geen enkele staat in Bijlage 5.1**, het beoordelingsformulier dat de opleiding zelf voorschrijft voor de methodologische kwaliteit. Bijlage 5.1 stelt kwalitatieve vragen: is de steekproef voldoende groot, is die representatief, is data-saturatie bereikt, is er rekening gehouden met vertekening. Nergens een effectgrootte, een betrouwbaarheidsinterval of een formele risk-of-bias-beoordeling.

Dit is mechanisme 1 uit `reference.md` punt 4 in zijn scherpste vorm: het model vult de rubric aan met een externe standaard. **Fix: rubric-tekst, met een expliciete afbakening van wat niet vereist is.**

### B. De AI beoordeelt de klinische juistheid van het advies in plaats van de aanwezigheid van het rubriekonderdeel

Het scherpste voorbeeld is criterium 7 bij Student 2. De docent gaf hier 4 punten en schreef:

> `+ Er wordt een concrete monitoringfrequentie genoemd (jaarlijks). Ook wordt verwezen naar bestaande NHG-criteria, wat de aanbeveling goed integreerbaar maakt in bestaande werkwijzen.`

De AI ziet exact hetzelfde en rekent het aan als tekort:

> "schrap de ononderbouwde jaarlijkse controle als algemene aanbeveling" (inline)
>
> "De controlefrequentie en praktische uitvoering blijven onvoldoende eenduidig" (criterium 7, verdict Satisfactory)

Zelfde feit, tegengestelde weging. Het is dus geen leesfout. De rubric vraagt bij Good alleen dat "een wijze van monitoring in de praktijk" **beschreven** is. De AI eist dat die monitoring medisch-inhoudelijk verdedigbaar is. Hetzelfde gebeurt bij "Vervang 'alternatief' door 'mogelijke aanvullende optie'" (S1) en bij de GLP-1-claim (S2): dat is klinische redactie, geen rubriekoordeel.

**Fix: rubric-tekst en de Context-sectie van de modelinstructies.**

### C. Het Great-vakje is zoals geschreven onbereikbaar

Alle vier Great-teksten stapelen absoluten: "volledig en samenhangend", "volledig en overtuigend beschreven", "overtuigend onderbouwd", "aantoonbaar", "volledig en herkenbaar". Een model dat die letterlijk leest vindt altijd wel iets dat niet volledig is, zeker in combinatie met mechanisme A. Dat verklaart nul keer Great op 16 oordelen.

Dat het aan de tekst ligt en niet aan de inzendingen blijkt uit de docent: zij gaf negen keer een 4, met motiveringen als "alle onderdelen van de analyse zijn op correcte wijze geanalyseerd. Complimenten!" en "Je reflectie voldoet aan alle gestelde eisen". Volledigheid binnen de gevraagde onderdelen, niet meer dan gevraagd.

**Fix: rubric-tekst, Great-kolom.**

### D. De toon is een sjabloon

Alle zestien feedbackblokken hebben exact dezelfde driedelige vorm: een lofzin, dan "Echter," met een tekortkoming, dan een gebiedende wijs. "Je deed goed werk door..." opent er vier. Dat is precies de sjabloonopener die bij manuele therapie door de woordlimiet verdween (`LEERPUNTEN.md`, 22-09-2026).

Naast de docent gelegd: zij schrijft losse bullets met `+`, `+/-` en `-`, informeel, met een concreet voorbeeld tussen haakjes bij elk tekort, en een los compliment waar het verdiend is. Nul overeenkomst met het sjabloon.

**Fix: modelinstructies.**

## 10. De varianten

Twee teksten, allebei nog niet getest. Voer ze in aparte Eduface-opdrachten in, naast de ongewijzigde baseline.

### Variant R: de rubric-wijzigingen

Vier ingrepen. De rest van de rubric blijft letterlijk zoals in sectie 6.

**R1. Afbakening bij criterium 3 (zoekstrategie).** Voeg toe aan het einde van zowel de Good- als de Great-tekst:

> Herhaalbaar betekent dat een lezer de zoekactie kan reconstrueren uit de zoektabel en de zoekstrings. Het vermelden van de zoekdatum, het aantal hits per zoekactie, veldlabels of filterinstellingen is niet vereist.

**R2. Afbakening bij criterium 4 (analyse).** Voeg toe aan het einde van zowel de Good- als de Great-tekst:

> De methodologische beoordeling volgt het beoordelingsformulier betrouwbaarheid, validiteit en generaliseerbaarheid van de opleiding en is kwalitatief van aard. Het rapporteren van effectgroottes, betrouwbaarheidsintervallen, p-waarden, uitvalpercentages of een formele risk-of-bias-beoordeling is niet vereist.

**R3. Het plafond bereikbaar maken.** Voeg aan alle vier de Great-teksten dezelfde slotzin toe:

> Dit niveau vraagt dat de onderdelen van het Good-niveau volledig en onderbouwd aanwezig zijn, niet dat er onderdelen buiten de opdracht worden toegevoegd. Kleine onvolkomenheden die de kern niet ondermijnen staan dit niveau niet in de weg.

**R4. De drempelregel terugzetten bij criterium 3, 6 en 7.** Zet vooraan in elk van die drie Unsatisfactory-teksten:

> Dit niveau geldt pas wanneer twee of meer van de onderstaande punten zijn vastgesteld.

De drie Satisfactory-correcties uit sectie 6 blijven ook staan; die raken de zaklijn, die nu goed zit, maar ze kloppen inhoudelijk nog steeds niet met de bron. Doorvoeren kan geen kwaad, maar verwacht er geen verschuiving van.

### Variant I: de modelinstructies

In te voeren via "Beschrijf je feedbackstijl" en dan "Opnieuw genereren". Reken op verlies: bij manuele therapie overleefden voorbeeldzinnen en de sectie Inline opmerkingen nooit (`reference.md` punt 7).

```
BELANGRIJK: vat het onderstaande niet samen en laat geen van de onderdelen weg.

Context: dit is een CAT (Critically Appraised Topic) van een student van de opleiding
praktijkondersteuner huisarts (POH), NLQF niveau 6. Een literatuuronderzoek van maximaal
6000 woorden naar een vraag uit de eigen huisartsenpraktijk. Dit is geen systematische
review en geen wetenschappelijke publicatie. Beoordeel uitsluitend tegen de rubric.
Vraag niet om effectgroottes, betrouwbaarheidsintervallen, p-waarden, uitvalpercentages,
risk-of-bias-beoordelingen, zoekdata of hitaantallen: die horen niet bij deze opdracht.
Beoordeel of het gevraagde onderdeel aanwezig en onderbouwd is, niet of het klinische
advies van de student medisch-inhoudelijk de beste keuze is.

Algemene feedback: schrijf per criterium een lijst losse bevindingen, geen lopende tekst
en geen kopjes. Markeer elke bevinding met + wanneer het goed is, +/- wanneer het er is
maar beter kon, en - wanneer het ontbreekt. Spreek de student aan met je. Schrijf
informeel en vakinhoudelijk concreet: noem MeSH-termen, PICO-elementen, level of
evidence, NHG-richtlijnen en APA bij naam. Geef bij elk tekort een concreet voorbeeld of
een concrete suggestie tussen haakjes, nooit een kale constatering. Benoem sterke en
zwakke punten binnen hetzelfde criterium naast elkaar. Maximaal 80 woorden per criterium.
Begin nooit met "Je deed goed werk" en gebruik nooit het woord "Echter" als scharnier.
Varieer de opening, gebruik nooit twee keer dezelfde openingszin.

Beoordelingsstrengheid: gebruik de volle schaal, ook het hoogste vakje. Een inzending die
alle gevraagde onderdelen volledig en onderbouwd bevat verdient het hoogste vakje, ook
wanneer er nog iets beter had gekund. Satisfactory is al een voldoende, niet een
waarschuwing. Kies Unsatisfactory alleen wanneer die tekst als geheel van toepassing is.
Een ontbrekend detail is groeifeedback binnen het huidige vakje, geen reden om een vakje
lager te gaan.
```

### Wat we van de uitkomst verwachten

Op grond van manuele therapie (`reference.md` punt 9) en de diagnose hierboven:

- **Variant R** lost naar verwachting het plafond op (mechanisme A en C) en daarmee ook de omgeklapte rangorde, want die komt voort uit het ontbreken van het bovenste vakje.
- **Variant I** verandert naar verwachting de toon wel en de oordelen nauwelijks.
- **Variant RI** wint waarschijnlijk op beide assen.

Neem dat niet aan, meet het. Bij manuele therapie klopte dit patroon, maar dat is één vak.

## 11. Wat er nog moet komen

**Van Dante:**

1. **De huidige modelinstructies**, letterlijk, via "Bekijk modelinstructies". Zonder die tekst weten we niet wat deze baseline heeft geproduceerd, en dus ook niet wat variant I precies verandert.
2. De drie varianten draaien (R, I, RI) op dezelfde twee studenten, en de exports aanleveren.

**Vragen, niet zelf ingevuld:**

3. Blijft reflectie op 16%, of gaan alle acht naar 12,5% zoals in de bron?
4. Horen de randvoorwaarden (APA-7, max 6000 woorden, inhoudsopgave, lettertype, Word-format) als extra criterium in Eduface, of blijven ze bij de docent?
5. Is er een inzending die de docent **wel** heeft laten zakken, met haar beoordeling erbij? De baseline laat zien dat de zaklijn nu goed zit voor geslaagde studenten, maar of hij niet te laag ligt is met dit testset niet te meten.
6. Wat betekent "Totaal Cijfer: SOUND" in de export, en is dat instelbaar? Het staat bij beide studenten gelijk terwijl de docent 8,1 en 7,2 gaf.
7. Is K.J. van Kruining dezelfde docent als "Selma" uit de bestandsnaam van de rubric?

## 12. Meting variant RI, ronde 1

Export `Inzendingen_CAT_23-09-2026_6.zip`. Zowel de rubric uit `cat-poh-plakteksten.md` als de modelinstructies zijn doorgevoerd; te zien aan het woord "reconstrueerbaar" uit de nieuwe Good-tekst bij criterium 3, en aan de bulletvorm uit de instructies. Variant R en variant I zijn dus niet los gemeten, alleen de combinatie.

Schaal: Onvoldoende 1, Voldoende 2, Goed 3, Uitstekend 4.

| # | Criterium | Docent S1 | Baseline S1 | RI S1 | Docent S2 | Baseline S2 | RI S2 |
|---|---|---|---|---|---|---|---|
| 1 | Aanleiding | Uitstekend | Goed | Goed | Uitstekend | Goed | Goed |
| 2 | PICO | Uitstekend | Voldoende | Voldoende | Voldoende | Goed | **Voldoende ✓** |
| 3 | Zoekstrategie | Goed | Voldoende | Voldoende | Goed | Goed ✓ | Goed ✓ |
| 4 | Analyse | Uitstekend | Voldoende | **Goed ↑** | Voldoende | Voldoende ✓ | Voldoende ✓ |
| 5 | Conclusie | Goed | Goed ✓ | Goed ✓ | Goed | Goed ✓ | Goed ✓ |
| 6 | Discussie | Uitstekend | Goed | Goed | Uitstekend | Goed | Goed |
| 7 | Klinische relevantie | Voldoende | Voldoende ✓ | Voldoende ✓ | Uitstekend | Voldoende | **Uitstekend ✓** |
| 8 | Reflectie | Uitstekend | Voldoende | **Goed ↑** | Voldoende/Goed | Voldoende ✓ | Voldoende ✓ |
| | **Som** | **28** | 19 | **21** | **24,5** | 21 | **22** |

- **Exacte treffers: 8 van 16, was 6 van 16.** Vier verbeteringen, nul regressies.
- **Nul keer Onvoldoende**, net als in de baseline. De zaklijn blijft goed.

### Wat de fixes aantoonbaar hebben gedaan

- **Uitstekend bestaat nu.** Eén keer, bij Student 2 criterium 7. Dat was precies de scherpste fout uit de baseline: de docent gaf daar 4 punten voor de jaarlijkse monitoring, de baseline gaf Voldoende omdat de AI die monitoring klinisch afkeurde. De regel "een genoemde controlefrequentie telt als beschreven monitoring" heeft dat omgedraaid. Het model schrijft nu zelf: *"NHG-criteria en €20-30 onderbouwen gericht testen; monitoring omvat relevante uitkomsten en jaarlijkse evaluatie."*
- **De systematic-review-eisen zijn weg.** Geen effectgroottes, betrouwbaarheidsintervallen, p-waarden, zoekdata of hitaantallen meer. Bij Student 2 criterium 4 vraagt het model nu letterlijk om de begrippen uit Bijlage 5.1: *"level of evidence, gevolgen voor betrouwbaarheid, validiteit, generaliseerbaarheid, representativiteit, setting, dataverzameling, belangenverstrengeling."* De afbakening stuurt het model naar het juiste instrument in plaats van het alleen iets te verbieden.
- **De toon is om.** Bullets met `+`, `+/-` en `-`, tweede persoon, concrete suggestie bij elk tekort, vaak met een voorbeeld tussen haakjes. Geen "Je deed goed werk" meer. Blokken van 50 tot 70 woorden. Dit is de stijl van de docent.

### Wat er nog niet goed is

**1. De rangorde staat nog steeds omgekeerd, maar half zo erg.** De docent zette Student 1 3,5 punt boven Student 2. De baseline zette hem 2 punten eronder, RI nog 1 punt eronder. Student 1 wordt nog structureel onderschat.

**2. Criterium 1 en 6 komen bij geen van beide studenten boven Goed uit**, terwijl de docent daar vier keer Uitstekend gaf. Dat is vier van de zeven resterende missers. Twee oorzaken:
- Bij criterium 1 werkt mechanisme B nog door. De twee `+/-`-punten bij Student 1 gaan over klinische inhoud, niet over het rubriekonderdeel: *"Presenteer kurkuma niet vooraf als statinealternatief"*. De afbakening "aanwezigheid boven klinische juistheid" staat nu alleen bij criterium 7.
- De Great-teksten van 1, 2 en 6 stapelen nog absoluten in de hoofdzin ("volledig en samenhangend", "overtuigend verbonden", "volledig en herkenbaar"). De toegevoegde slotzin weegt daar niet tegenop.

**3. Criterium 2 vraagt een controleconditie die de opdracht niet eist.** Student 1 schreef in haar PICO-tabel letterlijk `Comparison: Niet van toepassing` en kreeg van de docent 4 punten. De AI noemt dat een gebrek: *"De controle ontbreekt in de PICO; voeg 'geen supplement of gebruikelijke zorg' toe"*, en zet het op Voldoende. Student 2 had de C juist wél in de PICO maar trok hem niet door naar de vraag, en kreeg daarvoor 2 punten. De docent beoordeelt dus op **consistentie**, niet op aanwezigheid van een C. De Great-tekst eist nu expliciet alle vier de PICO-elementen.

### De drie vervolgfixes

Zes vakjes, alle andere blijven zoals ze zijn. Volledige teksten staan in `cat-poh-plakteksten.md`, sectie "Ronde 2".

- **Criterium 2, Good en Great:** een beargumenteerd "niet van toepassing" bij de controle-interventie telt als volledig; beoordeeld wordt de consistentie tussen casus, PICO en onderzoeksvraag.
- **Criterium 1 en 6, Good en Great:** dezelfde afbakening als bij criterium 7 toevoegen, aanwezigheid en onderbouwing boven klinische juistheid.
- **Criterium 1, 2 en 6, Great:** de absoluten in de hoofdzin verzachten, zodat de slotzin niet tegen de rest van de tekst in hoeft te werken.

**Waarschuwing bij deze ronde.** We duwen nu het plafond omlaag zonder een gezakte inzending om de zaklijn tegen te ijken. Het risico op oversoepelheid is vanaf hier reëel en met dit testset niet te meten. Een inzending die de docent heeft laten zakken, mét haar beoordeling, is het volgende dat nodig is.

### Losse observatie

"Totaal Cijfer" staat bij Student 1 op **SOUND** en bij Student 2 op **Goed**. In de baseline stonden beide op SOUND. Dat lijkt een onvertaald label dat er soms wel en soms niet doorheen komt. Melden bij Menno of Samuel.

## 13. Meting ronde 2

Export `Inzendingen_CAT_23-09-2026_7.zip`, met de zes vervangen vakjes uit ronde 2.

### Eerst een correctie op de meetlat

In sectie 4 heb ik de punten van de docent omgezet naar één verwacht vakje per criterium, bijvoorbeeld "2 punten bij criterium 3 = Good". **Dat was mijn eigen afleiding uit haar geschreven commentaar, geen ground truth.** De ground truth zijn de punten: 4, 2 of 0. Met vier vakjes heeft 2 punten geen enkel juist vakje, maar een bandbreedte.

Vanaf nu twee meetlatten naast elkaar:

- **Strikt:** het vakje uit de tabel in sectie 4. Streng, en deels gebaseerd op mijn interpretatie.
- **Bandbreedte:** 4 punten mag Goed of Uitstekend zijn, 2 punten mag Voldoende of Goed, 0 punten moet Onvoldoende. Dit volgt rechtstreeks uit de bron en is niet betwistbaar.

De bandbreedte is de maat die telt. De strikte maat laat zien hoeveel fijnregeling er nog in zit.

### De cijfers

| Meting | Strikt | Bandbreedte | Rangorde S1 vs S2 |
|---|---|---|---|
| Docent | — | — | 28 tegen 24,5, S1 boven |
| Baseline | 6/16 | 12/16 | 19 tegen 21, **omgekeerd** |
| Ronde 1 (RI) | 8/16 | 15/16 | 21 tegen 22, **omgekeerd** |
| Ronde 2 | 8/16 | **15/16** | 22 tegen 21, **klopt** |

| # | Criterium | Docent S1 | R1 S1 | R2 S1 | Docent S2 | R1 S2 | R2 S2 |
|---|---|---|---|---|---|---|---|
| 1 | Aanleiding | 4 | Goed | Goed | 4 | Goed | Goed |
| 2 | PICO | 4 | Voldoende | **Voldoende ✗** | 2 | Voldoende | Voldoende |
| 3 | Zoekstrategie | 2 | Voldoende | **Goed ↑** | 2 | Goed | **Voldoende ↓** |
| 4 | Analyse | 4 | Goed | Goed | 2 | Voldoende | Voldoende |
| 5 | Conclusie | 2 | Goed | Goed | 2 | Goed | Goed |
| 6 | Discussie | 4 | Goed | Goed | 4 | Goed | **Uitstekend ↑** |
| 7 | Klin. relevantie | 2 | Voldoende | Voldoende | 4 | Uitstekend | **Goed ↓** |
| 8 | Reflectie | 4 | Goed | Goed | 3 | Voldoende | Voldoende |

De vier bewegingen vallen alle vier binnen de bandbreedte, dus geen van de pijlen is een echte regressie. Op de strikte maat wegen ze tegen elkaar weg.

### Wat ronde 2 heeft opgelost

**De omgekeerde rangorde is weg.** Dit was het laatste van de drie restpunten. De docent zette Student 1 boven Student 2; baseline en ronde 1 zetten hem eronder, ronde 2 zet hem er weer boven. Dat kwam van criterium 3, dat bij Student 1 naar Goed ging.

**Criterium 6 haalde voor het eerst Uitstekend** bij Student 2, waar de docent 4 punten gaf. De verzachting van de hoofdzin werkte daar.

### Wat er nog fout is: criterium 2 bij Student 1

Het enige oordeel dat buiten de bandbreedte valt. De docent gaf 4 punten met alleen twee plussen: *"De PICO vloeit geheel logisch uit de casuïstiek en patient vraag"* en *"Onderzoeksvraag vloeit volledig logisch vanuit PICO"*. De AI geeft Voldoende met drie `+/-`-punten:

> `+/- 'Cholesterolwaarde' is te vaag; definieer LDL primair en totaalcholesterol, HDL en triglyceriden afzonderlijk.`
>
> `+/- Onderbouw 'geen controle' in PICO, vraag en zoekstrategie.`
>
> `+/- Populatie en conclusies verschillen; specificeer de doelgroep.`

Twee van die drie zijn eisen die de docent niet stelt:

1. **De granulariteit van de uitkomstmaat.** Zij accepteert "cholesterolwaarde" zonder opmerking.
2. **Mijn eigen fix heeft dit deels veroorzaakt.** Ik schreef "een **beargumenteerd** 'niet van toepassing' telt als volledig". Student 1 schreef in haar PICO-tabel kaal `Comparison: Niet van toepassing`, zonder argument, en kreeg 4 punten. Het woord "beargumenteerd" heeft dus een eis toegevoegd die de docent niet heeft. De AI is van "voeg een controle toe" naar "onderbouw dat je er geen hebt" gegaan, precies zoals ik het opschreef, en dat is nog steeds te streng.

Dat is leerzaam: een ontsnappingszin die een voorwaarde bevat, wordt die voorwaarde.

### Advies

Eén gerichte ronde op criterium 2, dan stoppen met fijnregelen. De reden om te stoppen: 15 van 16 binnen bandbreedte, rangorde klopt, toon klopt, nul keer Onvoldoende. Verder duwen aan het plafond zonder een gezakte inzending om de zaklijn tegen te ijken levert meer risico dan winst op.

De compressie blijft wel bestaan: 1 keer Uitstekend op 16, terwijl de docent 9 keer 4 punten gaf, en het verschil tussen de twee studenten is 1 punt waar de docent 3,5 punt zag. De AI zet ze nu in de goede volgorde maar ziet het verschil als kleiner dan het is. Dat is acceptabel zolang de docent het eindcijfer zelf zet, maar het is de resterende beperking.

## 14. Meting ronde 3, en de eindstand

Export `Inzendingen_CAT_23-09-2026_10.zip`, met de twee vervangen vakjes bij criterium 2.

| # | Criterium | Docent S1 | R2 S1 | R3 S1 | Docent S2 | R2 S2 | R3 S2 |
|---|---|---|---|---|---|---|---|
| 1 | Aanleiding | 4 | Goed | Goed | 4 | Goed | Goed |
| 2 | PICO | 4 | Voldoende ✗ | **Goed ✓** | 2 | Voldoende | Voldoende |
| 3 | Zoekstrategie | 2 | Goed | Goed | 2 | Voldoende | **Goed** |
| 4 | Analyse | 4 | Goed | Goed | 2 | Voldoende | Voldoende |
| 5 | Conclusie | 2 | Goed | **Voldoende** | 2 | Goed | Goed |
| 6 | Discussie | 4 | Goed | Goed | 4 | Uitstekend | Uitstekend |
| 7 | Klin. relevantie | 2 | Voldoende | Voldoende | 4 | Goed | Goed |
| 8 | Reflectie | 4 | Goed | Goed | 3 | Voldoende | Voldoende |

| Meting | Strikt | Bandbreedte | Rangorde S1 vs S2 |
|---|---|---|---|
| Docent | — | — | 28 tegen 24,5 |
| Baseline | 6/16 | 12/16 | omgekeerd |
| Ronde 1 | 8/16 | 15/16 | omgekeerd |
| Ronde 2 | 8/16 | 15/16 | klopt, 22 tegen 21 |
| **Ronde 3** | 8/16 | **16/16** | gelijk, 22 tegen 22 |

**Criterium 2 is opgelost.** Het weghalen van het woord "beargumenteerd" was genoeg. De AI schrijft nu zelf: *"je PICO is overzichtelijk en 'Comparison: niet van toepassing' past."* Precies de lezing van de docent.

### Wat de bandbreedte-maat niet bewijst

Eerlijk over de eigen meetlat: de bandbreedte laat per criterium twee van de vier vakjes toe. **Een model dat overal "Goed" invult haalt daarmee ook 16 van 16.** De maat is dus een ondergrens die gehaald moet worden, geen bewijs dat het model onderscheid maakt.

Wat wél onderscheid laat zien:

- **Binnen een student werkt het.** Bij Student 2 gaf de docent 4 punten op criterium 1, 6 en 7; de AI zet daar Goed, Uitstekend en Goed. Op de criteria waar zij 2 punten gaf staat twee keer Voldoende en twee keer Goed. De vorm van de verdeling klopt.
- **Tussen studenten werkt het niet.** De docent zag 3,5 punt verschil, de AI ziet er nul: beide studenten komen op 22. In ronde 2 stond Student 1 er één punt boven, nu staan ze gelijk. Dat is geen regressie binnen de bandbreedte, maar het laat zien dat dit niet stabiel gestuurd wordt.
- **Het plafond blijft bijna dicht.** Eén keer Uitstekend op 16, waar de docent negen keer 4 punten gaf.

### De resterende beperking

De AI comprimeert naar Goed. Dat is met rubric-tekst niet verder op te lossen zonder het risico dat de zaklijn meezakt, en die zaklijn is met dit testset niet te controleren: beide studenten zijn geslaagd, er is geen gezakte inzending met een beoordeling om tegen te ijken.

Praktisch gevolg: de AI zet de criteria van één student in de goede verhouding en gaat nooit onterecht zakken, maar hij is geen betrouwbare cijfergever tussen studenten onderling. Voor het beoogde gebruik is dat acceptabel, want het eindoordeel is in Eduface een handmatige keuze van de docent (`reference.md` punt 1).

### Eén losse tekstfout die geen niveaukwestie is

Bij criterium 5 lezen de AI en de docent hetzelfde woord tegengesteld. De bron vraagt dat de conclusie "in een stellende vorm" is geformuleerd, dus als bevestigende uitspraak in plaats van een samenvatting. De Eduface-tekst maakte daar "stellig" van, en de AI leest dat als "te zeker":

> Docent bij Student 1: *"De conclusie is nu niet in stellende vorm geformuleerd."*
>
> AI bij Student 1, ronde 3: *"De conclusie is te stellig; vervang 'overtuigend bewijs' door 'beperkt bewijs'."*

Precies het omgekeerde advies op dezelfde tekst. Het verdict blijft binnen de bandbreedte, dus dit is geen kalibratieprobleem maar een woordbetekenis die fout is overgenomen. Die blijft elke volgende student verkeerd sturen. Voorstel in `cat-poh-plakteksten.md`, sectie "Losse correctie criterium 5".

### Advies

Klaar. Doorvoeren wat er nu staat, plus eventueel de correctie bij criterium 5. Niet verder fijnregelen op niveaus.

Het volgende dat echt iets toevoegt is geen rubric-ronde maar materiaal: **een CAT die de docent heeft laten zakken, met haar beoordelingsformulier.** Daarmee is de zaklijn te controleren, en pas dan is te zien of de compressie naar Goed ook betekent dat een zwakke inzending te hoog uitkomt.
