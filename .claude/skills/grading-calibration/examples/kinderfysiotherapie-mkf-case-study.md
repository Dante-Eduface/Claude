# Case study: Master Kinderfysiotherapie (CAT)

Tweede vak waarop `grading-calibration` is losgelaten. **Status: afgerond op 23-09-2026. 14/14 criteria gelijk aan de docent over twee duo's, en de toon ligt dicht bij de hare.** Eén voorbehoud staat nog open, zie sectie 12.

- **Opleiding:** master Kinderfysiotherapie (MKF), Breederode Hogeschool. Zelfde hogeschool als manuele therapie, andere opleiding en andere docent.
- **Opdrachttype:** CAT over een onzekerheid of zorgprobleem uit de kinderfysiotherapeutische praktijk, 6 stappen, in een **duo** geschreven, max 1000 woorden, toetscode MKF26-WO1-CAT-1-5. Beoordeeld met voldaan / niet voldaan.
- **Docent:** Ivonne Duiser
- **Duo's:** duo 1 (invloed van krachttraining op fysieke functies van adolescenten met hypermobiliteit), duo 2 (schedelmeting bij zuigelingen met een positionele schedeldeformatie: digitale apps vs plagiocefalometrie)

## 1. Materiaal

Alle zeven materialen lagen er, met één gat.

| # | Materiaal | Status |
|---|---|---|
| 1 | Origineel beoordelingsformulier | Ja, maar in **twee verschillende versies**, zie sectie 2 |
| 2 | Schrijfformat / instructiedocument | Deels: de handleiding beschrijft de 6 stappen, zonder uitgewerkt voorbeeld |
| 3 | Minstens 2 echte inzendingen | Ja, 2 duo's |
| 4 | Officiële beoordeling van de docent | Deels: geschreven feedback per criterium, **geen Voldaan/Niet voldaan per criterium en geen eindoordeel** |
| 5 | Conceptcommentaar van de docent in de inzending | Ja, en rijk: 53 Word-comments van Ivonne over twee inzendingen, plus gele arceringen voor spreektaal |
| 6 | Huidige live rubric | Ja, 7 criteria, ongewijzigd |
| 7 | Huidige AI-uitkomst op deze inzendingen | Ja, Eduface-export van 23-09-2026 |

Het gat in 4 is het enige dat nog telt: Ivonne schrijft nergens "niet voldaan". Haar taalregister is overal groeifeedback, maar dat is een lezing, geen oordeel.

## 2. Er zijn twee beoordelingsformulieren, en Eduface gebruikt het andere

De handleiding bevat een blanco formulier. De twee ingevulde formulieren van Ivonne zijn een **ander** formulier, met kopregel "Toetsen Minor". De live rubric in Eduface is gegenereerd uit het **handleiding**-formulier, niet uit dat van Ivonne.

| Handleiding-formulier → de live rubric | Formulier dat Ivonne feitelijk invult |
|---|---|
| Algemeen: taalgebruik, samenhang, APA | Algemeen: taalgebruik, **1000 woorden**, samenhang, **titel**, APA |
| Onzekerheid in de kinderfysiotherapeutische praktijk | **Klinisch scenario** (patiëntpresentatie, anamnese, lichamelijk onderzoek, diagnostische hypotheses) |
| Onderzoeksvraagstelling en **-doelstelling** | Klinische vraag (doelstelling valt weg) |
| Zoekstrategie en scopesearch | Zoekstrategie (+ "voldoet **eigen patiënt** aan de in- en exclusiecriteria") |
| Beoordelen van de kwaliteit van artikelen | Kritische evaluatie kwaliteit |
| Conclusies en aanbevelingen: aanbevelingen **voor de praktijk** | Conclusies en aanbevelingen: aanbevelingen **voor kind en ouders** |
| Implicaties voor de kinderfysiotherapiepraktijk | idem |

Dat de live rubric uit het handleiding-formulier komt is een gelukkige uitkomst: Ivonnes formulier bevat een patiëntpresentatie, anamnese, algemeen lichamelijk onderzoek en een "eigen patiënt", allemaal overgenomen uit een **diagnostische CAT over één patiënt** (precies het type van manuele therapie). Deze CAT gaat niet over een patiënt maar over een doelgroep, beide duo's leverden een inleiding over een doelgroep, en Ivonne heeft bij geen van beide een patiëntpresentatie gevraagd of gemist. Was de rubric uit háár formulier gegenereerd, dan zou elk duo op twee criteria zijn gezakt voor iets wat het vak niet vraagt.

**Twee verschillen om aan Ivonne terug te geven** (los van de kalibratie): de live rubric eist een **doelstelling** die haar formulier niet kent, en Eduface heeft twee van haar vijf Algemeen-regels laten vallen (1000 woorden en titelpagina). Die eerste kostte hier niets, zie sectie 4.

## 3. De 1000-woordengrens gaat alleen over lopende tekst

Niet in de live rubric terechtgekomen, maar vastgelegd voor als de regel terugkomt bij een hergeneratie.

Ivonne, over beide duo's: *"Jullie zijn mooi onder 1000 woorden gebleven door goed gebruik te maken van tabellen."*

| | Lopende tekst (excl. tabellen, titels, bronnenlijst) | In tabellen | Hele document |
|---|---|---|---|
| Duo 1 | **1062** | 1722 | 3066 |
| Duo 2 | **921** | 1164 | 2138 |

Tabellen, figuren, tabel- en figuurtitels en de bronnenlijst tellen niet mee. En 1062 woorden lopende tekst was voor haar nog "mooi onder 1000", dus er zit tolerantie op de grens zelf. Een model dat het hele document telt ziet 3066 tegen een grens van 1000 en faalt een duo waarop de docent expliciet complimenteert.

## 4. Baseline: AI tegenover docent

Eduface-export 23-09-2026, ongewijzigde rubric en default modelinstructies.

| Criterium | Gewicht | AI duo 1 | Ivonne duo 1 | AI duo 2 | Ivonne duo 2 |
|---|---|---|---|---|---|
| 1. Algemeen | 14% | **FAIL** | groei | **FAIL** | groei (twijfelgeval) |
| 2. Onzekerheid in de kinderfysiotherapeutische praktijk | 14% | PASS | groei | PASS | groei |
| 3. Onderzoeksvraagstelling en -doelstelling | 14% | PASS | schoon | PASS | groei |
| 4. Zoekstrategie en scopesearch | 14% | **FAIL** | groei | **FAIL** | groei |
| 5. Beoordelen van de kwaliteit van artikelen | 14% | **FAIL** | groei | **FAIL** | schoon |
| 6. Conclusies en aanbevelingen | 14% | **FAIL** | groei | PASS | schoon |
| 7. Implicaties voor de kinderfysiotherapiepraktijk | 16% | PASS | groei | **FAIL** | schoon |

"groei" = ze benoemt een echt gat in de taal waarin ze de rest ook passeert ("had mogen", "jammer", "probeer", of als vraag). "schoon" = geen kritiek.

**4 van 7 criteria falen bij duo 1, 4 van 7 bij duo 2.** Drie daarvan falen bij **beide** duo's, dat zijn de zekere hotspots: **Algemeen, Zoekstrategie en scopesearch, Beoordelen van de kwaliteit van artikelen.** Conclusies (duo 1) en Implicaties (duo 2) zijn elk bij één duo fout.

Twee criteria matchen bij beide duo's: Onzekerheid en Onderzoeksvraagstelling. Die zijn bewust **niet** aangepast.

**Doodlopende hypothese, vóór de baseline:** de rubric eist "De doelstelling van de CAT is duidelijk en expliciet beschreven", geen van beide duo's beschrijft een aparte doelstelling, en Ivonnes eigen formulier kent de doelstelling niet. Voorspeld als valse onvoldoende. **Kwam niet uit:** criterium 3 haalde PASS bij beide duo's, en bij duo 2 schreef de AI zelfs "het onderzoeksdoel expliciet te maken". De rubric vraagt daar dus wel meer dan de docent, maar zonder gevolg. Niet aangepast. (Zelfde les als het onderwijsniveau bij manuele therapie: een plausibele hypothese is geen bevinding tot de meting hem bevestigt.)

## 5. Diagnose per mismatch, uit de AI's eigen tekst

### Hotspot 1, Algemeen: twee mechanismen tegelijk

**Drempel.** AI duo 1: *"taal- en APA-fouten schaden de professionaliteit."* Ivonne duo 1 over precies die APA: *"Jullie hebben correct gerefereerd en goed gebruik gemaakt van de literatuur."* Een directe tegenspraak, geen weging. Over taal zegt zij *"overwegend zakelijk en professioneel. Soms is er wat spreektaal ingeslopen, dat heb ik geel gearceerd"* en arceert, waar de AI zakt.

**Criterium-lekkage, nieuw mechanisme.** De AI haalt onder Algemeen kritiek binnen die bij andere criteria hoort. Duo 1: *"wisselende doelgroepen en een protocol zonder resultaten verzwakken de conclusie"* (dat is criterium 5 en 6). Duo 2: *"Stem daarna flowchart en onderzoeksbeschrijving exact op elkaar af"* (dat is criterium 4). Het woord "samenhangend" in de rubric wordt gelezen als inhoudelijke samenhang van het betoog, niet als opbouw en leesbaarheid van de tekst. Zo wordt Algemeen een tweede beoordeling van het hele werk, en zakt het criterium op gronden die elders al meewegen.

### Hotspot 2, Zoekstrategie en scopesearch

AI duo 1: *"De scopesearch en definitieve zoekstrategie zijn echter onvoldoende controleerbaar... Voeg voor de scopesearch databank, datum, termen, string en opbrengst toe."*
Ivonne duo 1: *"Jullie hebben de scopesearch opgenomen in jullie CAT, waardoor het hele proces vanaf de start te volgen is. De scopesearch hebben jullie gebruikt om termen te genereren en om te kijken of er voldoende literatuur te vinden was."* Zij zegt letterlijk dat het te volgen is.

AI duo 2: *"De onderbouwing van artikelkeuze ontbreekt... Koppel per artikel populatie, meetmethode, vergelijkingsmethode en betrouwbaarheiduitkomst aan criteria en onderzoeksvraag."*
Ivonne duo 2: *"Het hele proces hebben jullie weergegeven, waardoor het te volgen is, de stappen lopen alleen wat door elkaar."*

Oorzaak: de Voldoende-tekst eist dat de scopesearch "volledig en controleerbaar" is beschreven, met dezelfde audit trail als de definitieve zoekactie. In de handleiding is de scopesearch alleen een verkennende stap om zoektermen vast te stellen. Daarnaast wordt "motivatie voor de keuze van de artikelen" gelezen als een verantwoording per artikel.

### Hotspot 3, Beoordelen van de kwaliteit van artikelen

AI duo 1: *"De interpretatie ontbreekt... Leg per studie uit hoe bias de interne validiteit beïnvloedt en vergelijk populatie, steekproef en design met de PICO."*
AI duo 2: *"Bespreek per artikel validiteit, betrouwbaarheid, bias en generaliseerbaarheid, en pas daarna je kwaliteitsindeling en conclusie aan."*
Ivonne duo 2: geen enkele kritiek op dit onderdeel, alleen de suggestie om drie tabellen samen te voegen.

Oorzaak: de Voldoende-tekst eist dat de vijf aspecten "**afzonderlijk** aan bod komen" en gebruikt het woord "**navolgbaar**". Dat is exact het woord dat bij manuele therapie door Eduface's eigen hergeneratie werd binnengesmokkeld (`LEERPUNTEN.md`, 22-09-2026), en het doet hier hetzelfde werk: een checklistbeoordeling (JBI, SANRA) dekt de vijf aspecten impliciet via de items, maar de AI wil vijf aparte besprekingen per artikel.

### Mismatch 4, Conclusies en aanbevelingen (duo 1)

Het scherpste drempel-bewijs van deze case. Zelfde observatie, tegengestelde conversie:

| | Tekst |
|---|---|
| **AI** (FAIL) | "De koppeling met bewijskracht en toepasbaarheid is echter zwak. Daardoor is de claim over krachttraining te stellig." |
| **Ivonne** (groei) | "Jullie hebben de methodologische kwaliteit weergegeven zonder hier conclusies aan te verbinden... Ten aanzien van de methodologische kwaliteit hadden jullie explicieter mogen zijn." |

Geen kennisverschil. Alleen de omzetting van een gevonden gat naar een verdict.

### Mismatch 5, Implicaties (duo 2), en de omkering

AI duo 2 (FAIL): *"De praktische uitwerking blijft te algemeen... Werk een stappenplan uit met gestandaardiseerde meetcondities en scholing. Leg vast wie resultaten bespreekt, waar ze worden geregistreerd."*
Ivonne duo 2: *"Dit is een kant en klaar advies aan de praktijk."* Onverdeeld positief.

En omgekeerd bij duo 1: daar gaf de AI PASS terwijl Ivonne juist iets miste (*"Hier had een algemene, overkoepelende tekst bij gemogen"*). De AI-as staat op dit criterium dus omgekeerd op die van de docent.

Oorzaak: "hoe eventuele aanpassingen in de praktijk kunnen worden geïmplementeerd" wordt gelezen als een organisatorisch implementatieplan (stappenplan, registratie, scholing, taakverdeling). De handleiding bedoelt stap 6 als *"wat je CAT analyse betekent voor het handelen in de praktijk"*, dus het eigen handelen.

## 6. De toon-as, gemeten

| | Ivonne | Eduface (baseline) |
|---|---|---|
| Inline opmerkingen | 53 | 21 |
| Mediaan lengte | **8 woorden** | **38 woorden** |
| Gemiddelde lengte | 12,0 | 39,6 |
| Bevat een vraagteken | **51%** | **0%** |
| Korter dan 10 woorden | 55% | 0% |
| Aanspreekvorm | "jullie" (duowerk) | "jouw" |
| Spreektaal | geel arceren, geen opmerking | opmerking |

Bijna exact hetzelfde profiel als bij manuele therapie (Marloes ~8-10 woorden en vaak een vraag, AI ~40 woorden). Twee docenten, twee opleidingen, hetzelfde beeld: de **korte vraag** is de vorm van vakdocentfeedback, de lange dicterende paragraaf is wat het model er standaard van maakt.

Voorbeelden naast elkaar, allebei over een onvermelde bron:

- Ivonne: *"Wie zegt dit?"* (3 woorden)
- Ivonne: *"Waar komt dit vandaan?"* (4 woorden)
- Eduface: *"Beschrijf hier concreet hoe de scopesearch is uitgevoerd: vermeld de databank, zoekdatum, zoektermen of zoekstring en het aantal gevonden artikelen. Zonder deze informatie kan de lezer de zoekactie niet controleren of herhalen."* (35 woorden)

Ook hier weer de grammaticales in een lange opmerking, net als bij manuele therapie: *"Formuleer deze conclusie voorzichtiger en verbeter de grammatica naar 'de stabiliteit verbetert'..."*, in een opmerking van 78 woorden.

## 7. De vaste basistekst

De live rubric-tekst zoals Dante hem aanleverde is de vaste basistekst, letterlijk, in alle vier de opdrachten. Geen verse hergeneratie als controle (`reference.md` punt 6).

## 8. De rubric-variant

Vijf van de zeven criteria aangepast (1, 4, 5, 6, 7). Criterium 2 en 3 ongemoeid: die matchen bij beide duo's.

Bij alle vijf is ook de **Onvoldoende**-tekst versmald, wat normaal niet gebeurt (`reference.md` punt 5). Hier moest het wel: de Onvoldoende-teksten bevatten de formuleringen die de overstrengheid uitlokken ("Eén of meer van de vereiste onderdelen ontbreken of zijn niet controleerbaar", "niet volledig of niet navolgbaar", "één of meer onderdelen onvoldoende uitgewerkt"). Zo'n "één of meer"-constructie maakt van elk gaatje een onvoldoende, wat precies het drempelprobleem is.

Volledige plakklare teksten: geleverd aan Dante in de chat van 23-09-2026.

Kern per criterium:

1. **Algemeen** — samenhang afgebakend tot opbouw en leesbaarheid, met de expliciete regel dat inhoudelijke en methodologische kritiek bij het eigen criterium hoort en hier niet meeweegt (tegen de lekkage). Spreektaal, losse typefouten en kleine APA-onvolkomenheden als verbeterpunt.
4. **Zoekstrategie en scopesearch** — scopesearch mag kwalitatief beschreven zijn, zonder eigen databank, datum, string en opbrengst. Motivatie op het niveau van in- en exclusiecriteria plus flowchart volstaat. Sneeuwbal en citatiezoeken alleen vermelden als ze gebruikt zijn.
5. **Beoordelen van de kwaliteit van artikelen** — een erkende checklist geldt als navolgbare beoordeling; de vijf aspecten hoeven niet elk een eigen apart onderdeel. Eigen beargumenteerde kwaliteitsindeling voldoende, officiële afkapwaarden niet vereist.
6. **Conclusies en aanbevelingen** — drie onderdelen herkenbaar aanwezig is genoeg; de methodologische samenvatting mag beknopt en in een tabel. Een te stellige formulering is een verbeterpunt.
7. **Implicaties** — implementatie betekent het eigen handelen, niet een organisatorisch plan met stappenplan, registratie en scholing.

Plus op alle vijf de generieke drempelregel: *"Kleine onvolkomenheden die de kern niet ondermijnen, staan een voldoende niet in de weg."*

## 9. De modelinstructies-tekst

Volgens `reference.md` punt 7: lopende tekst, "vat niet samen"-instructie vooraan, één voorbeeld, harde woordlimiet van 50 woorden voor Algemene feedback.

Nieuw ten opzichte van manuele therapie en vak-specifiek:
- aanspreken met **"jullie"**, want het is duowerk (de AI gebruikt nu "jouw")
- tabellen zijn de normale plek voor detail en tellen niet als omvang
- **criterium-discipline**: beoordeel elk criterium alleen op zijn eigen onderwerp (tegen de lekkage uit sectie 5)
- inline opmerkingen van gemiddeld acht woorden, bij voorkeur als vraag

## 10. Resultaat over drie rondes

Twee duo's, zeven criteria, dus 14 oordelen per ronde. "Goed" = gelijk aan het oordeel van de docent, waarbij haar taalregister overal groeifeedback binnen een voldoende is.

| Ronde | Wat er aanstond | Oordeel-as |
|---|---|---|
| 1, baseline | ongewijzigde rubric, default modelinstructies | **6/14** |
| 2 | rubric-variant (criterium 1, 4, 5, 6, 7) plus modelinstructies | **10/14** |
| 3 | idem, plus caps op criterium 2, 3 en 4 | **14/14** |

Per criterium in de eindronde: alle zeven PASS bij beide duo's.

Wat ronde 2 naar 3 bracht, alle drie in de rubric en geen van de drie in de modelinstructies:

- **criterium 3** (Onderzoeksvraagstelling en -doelstelling) zakte bij beide duo's op de eis van een expliciete doelstelling. Cap: de doelstelling mag blijken uit aanleiding en onderzoeksvraag samen en hoeft geen apart gelabelde doelzin te zijn.
- **criterium 2** (Onzekerheid) zakte bij duo 1 omdat de AI de onzekerheid als concrete behandelkeuze met dosering wilde. Cap: een inleiding over doelgroep en probleem volstaat, veiligheid en dosering horen bij de conclusie en de implicaties.
- **criterium 4** (Zoekstrategie) zakte bij duo 2 op mijn eigen cap uit ronde 2, die bevestigend was geformuleerd ("een beschrijving van functie en opbrengst volstaat") en daardoor als eis werd gelezen. Herschreven als ontkenning.

## 11. Toon-as over drie rondes

| | Docent | Ronde 1 | Ronde 2 | Ronde 3 |
|---|---|---|---|---|
| Inline opmerkingen, mediaan | 8 woorden | 38 | 9 | **10** |
| Bevat een vraagteken | 51% | 0% | 58% | **32%** |
| Algemene feedback boven 50 woorden | n.v.t. | 6/14 | 1/14 | **0/14** |
| Aanspreekvorm | jullie | je / jouw | jullie | **jullie**, met "je" in 5 van 19 inline opmerkingen |

Twee restjes, allebei cosmetisch: het aandeel vragen zakte van 58% naar 32% terwijl de docent op 51% zit, en in de inline opmerkingen glipt "je" er nog in bij ongeveer een op de vier, terwijl de algemene feedback consequent "jullie" gebruikt.

**Advies: niet repareren.** De modelinstructies zijn door een lossy generatiestap gekomen waarin voor het eerst de Inline-opmerkingen-sectie bleef staan. Opnieuw genereren om "je" te repareren zet dat op het spel, en dat is het zwaarst bevochten deel van de hele kalibratie. De winst is een voornaamwoord, het risico is de hele toon-as.

## 12. Het openstaande voorbehoud

**De docent heeft nergens per criterium Voldaan of Niet voldaan opgeschreven**, en ook geen eindoordeel per duo. De 14/14 is dus gemeten tegen mijn lezing van haar taalregister, niet tegen haar oordeel.

Dat voorbehoud weegt nu zwaarder dan aan het begin. In ronde 1 was het risico dat de AI te streng was, en dan is elke opgeloste onvoldoende winst. Nu alles passeert is het risico gekanteld naar te soepel: als zij op een van de veertien wel Niet voldaan gaf, dan is de rubric daar nu te ruim gemaakt. Twee gevallen om expliciet aan haar voor te leggen:

- duo 2 leverde **geen titel** in, waarop zij schreef "probeer een titel te bedenken die de lading van jullie CAT volledig dekt"
- duo 2 had echte **APA-fouten** met tweemaal de vraag "willen jullie dit aanpassen?"

Beide klinken als groeifeedback, maar een herstelverzoek kan bij haar net zo goed Niet voldaan betekenen.
