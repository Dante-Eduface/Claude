# ICP — particuliere onderwijsinstellingen (NL)

_Bron: `ICP document (1).pdf`, aangeleverd door Dante 2026-07-21._

## In het kort
- Betalende deelnemers, geen publieke bekostiging, geen aanbestedingsplicht
- Beoordeelt **dezelfde lerende over tijd**, via **meerdere opdrachtvormen** en **meerdere beoordelaars**, tegen een **vastgelegd eisenkader**, op **voldoende volume**
- Twee subsegmenten, beide binnen dit ICP
- Gebruikt Moodle of een ander LMS

## Smaak 1 — klein tot middelgroot
- Beperkt aantal programma's, korte doorlooptijd
- Sales complexity laag, dealgrootte €10K tot €40K per jaar
- Voorbeelden: Schoevers, ICM, Capabel, MCI Ireland, Babel

## Smaak 2 — groot
- Institution wide, vaak meerdere merken of vestigingen onder één moeder, nakijkvolume raakt de kern van het verdienmodel
- Sales complexity gemiddeld, vooral schaalpilots en security review
- Dealgrootte €50K tot €150K per jaar
- Voorbeelden: NCOI, BPP, Kaplan, QA Higher Education, Open Universiteit, Open University, Arden, University of Law

## Beslisboom

**Poort 0 (eerst, binair): beoordeelt deze organisatie zelf werk van lerenden?**
Er moeten eigen deelnemers zijn, eigen beoordelaars, en werk dat door die beoordelaars heen gaat. Nee → buiten het ICP, ongeacht hoe goed de rest scoort. Geen nakijkwerk betekent geen product, geen budgetregel en geen koper.

Drie archetypes die hierop afvallen, ze lijken alle drie op een opleider:
- **Normzetter/certificeerder** — stelt eindtermen vast, accrediteert examens van derden, houdt een register bij. Voorbeeld: DSI (checkte 2026-07-21: *"DSI biedt zelf geen opleidingen aan, maar laat dit uitvoeren voor externe opleiders"*). Het nakijkvolume zit bij de geaccrediteerde opleiders, dáár ligt de deal.
- **Brancheorganisatie/koepel** — vertegenwoordigt leden, organiseert kennisdeling, beoordeelt niets.
- **Uitgever/platform** — levert lesmateriaal of software aan opleiders, heeft geen eigen deelnemers.

Deze partijen kunnen wel waardevol zijn als **ecosysteem-stakeholder**: hun eisenkader is de norm waartegen hun opleiders beoordelen, en hun goedkeuring opent de hele lijst. Zet ze in een aparte lane, nooit in de targetlijst als account.

**Poort 0b (duur, binair): duurt minstens één opleiding langer dan een jaar?**
Nee → buiten het ICP. **Aangescherpt door Dante op 2026-08-18** (was: langer dan 2 weken, 2026-07-22). Reden: bij de batch van 18 augustus vielen 3Masters, Auxilio en de Academie voor Geesteswetenschappen af omdat hun trajecten kort zijn, terwijl ze de oude tweewekengrens ruim haalden. Een traject van elf maanden of korter levert te weinig herhaald schrijfwerk van dezelfde lerende op, en dat is precies wat het product nodig heeft.

Regels bij het meten:
- Meet het **langste** programma, niet een losse module. Eén opleiding boven het jaar is genoeg.
- Losse lesdagen verspreid over meer dan een jaar tellen mee (bijvoorbeeld 15 lesdagen over vier onderwijsperioden).
- Een modulaire leerroute telt als één traject als de deelnemer de modules aaneengesloten doet richting één diploma (VanDoen: zes modules in 18 maanden = ja).
- Twijfel of het net onder het jaar zit → **kandidaat**, niet afgevallen. Leg de duur met citaat vast en laat Dante beslissen.
- **Deze aanbieders mogen niet in de outreach-workflow komen, ook niet met een contactpersoon erbij.**

**Poort 0d (omvang, zachte poort): is er een deal van 10.000 euro?**
_Aangescherpt 19-08-2026. Was sorterend, is nu een zachte poort._

Onder de drempel gaat een opleider naar `icp_status=te_klein`, niet naar `afgevallen`. Hij blijft op de lijst en valt buiten de outreach, tot Dante de lat verlaagt met `pipeline.py omvang --drempel X --herzien` of `--aandeel X --herzien`.

Je rekent dit niet zelf uit. Vul de velden en vraag `pipeline.py omvang --toets org_x` om het oordeel: `groot_genoeg`, `te_klein` of `onbekend`.

**Waar de drempel vandaan komt** (zie `Archive/prijsmodel-nl-opleiding-26-27.md`): 7.500 euro toolfee per opleiding plus een infrastructuurstaffel op studentplaatsen **per opleiding**, niet op het instellingstotaal.

| Staffel | Studentplaatsen per opleiding | Jaarfee |
|---|---|---|
| A | tot 500 | 10.000 |
| B | 500 tot 1.500 | 15.000 |
| C | 1.500 tot 3.000 | 21.500 |
| D | 3.000 tot 6.000 | 33.500 |
| E | 6.000 en meer | 51.500 |

Vijf opleidingen van 400 plaatsen zijn dus 5 x staffel A = 50.000 euro, niet een staffel C op 2.000 plaatsen.

**De cascade, stop zodra je een hard getal hebt:**
1. **Lerenden per jaar** (`lerenden_per_jaar`) bepaalt de staffel en is dus het getal dat er echt toe doet. Staat in jaarverslagen, persberichten en op over-ons-pagina's ("meer dan 1.000 studenten"). Niveau `hard`.
2. **Aantal opleidingen langer dan een jaar** (`aantal_opleidingen`). Elke opleiding is een eigen toolfee, dus dit weegt even zwaar als het studentaantal. Tellen uit de opleidingscatalogus, alleen wat poort 0b haalt. Niveau `afgeleid`.
3. **Medewerkers** (`omvang_medewerkers`), laatste redmiddel en het zwakste signaal, want opleiders werken veel met freelancers. Zoekvolgorde: de **LinkedIn-bedrijfspagina** (`nl.linkedin.com/company/<slug>` geeft zonder inloggen een medewerkersband plus het aantal profielen; let op dat opleiders vaak een `/school/`-pagina hebben die achter de login zit, dat een gegokte slug stille valse treffers geeft zoals `/company/technicom` in Mandelieu, en dat parallel opvragen HTTP 999 oplevert), dan **de vacaturepagina van de opleider zelf** (de onderschatte bron, Technicom: "Ons team bestaat uit ongeveer 50 vaste medewerkers"), dan **teampagina's tellen uit de sitemap** (hard en gratis, NSOB 65, 1801 151). Niveau `geschat`.
4. Niets gevonden op alle drie → `omvang_niveau=onbekend`, niet gokken. Geen afwijsgrond.

**De betaalbaarheids-toets.** Lerenden per jaar maal `cursusprijs` (staat bijna altijd op de opleidingspagina) is de omzet van dat programma. Onze jaarfee mag daar hoogstens 10% van zijn. Dit is in de praktijk wat opleiders afvoert, want de staffel begint op 10.000 euro en die drempel haalt iedereen met een kwalificerende opleiding. Een programma met 60 deelnemers a 800 euro draait 48.000 euro om, en dan is 10.000 euro een vijfde van de omzet. Ontbreekt de prijs of het aantal lerenden, dan wordt de toets overgeslagen en is het `onbekend`.

**Bewijsregel:** een `te_klein`-oordeel krijgt net als poort 0 een letterlijk citaat plus URL, in `omvang_citaat` en `omvang_url`. `pipeline.py doctor` keurt een te_klein zonder citaat af.

**Bewijsregel:** elk poort-0-oordeel krijgt een URL plus letterlijk citaat van hun eigen site. Geen citaat = geen oordeel, dan staat er "niet gevonden". Namen die in het ICP-document staan zijn hypotheses, geen gevalideerde targets.

**Daarna:**
1. Particuliere instelling (betalende deelnemers, privaat bekostigd)? Nee → buiten dit segment, zie hogeschool-ICP.
2. Ja → schaal en nakijkvolume? Kleinschalig → bedrijfsopleiders en particulier, laag complex, €10-40K/jr. Grootschalig → grote particuliere groepen, gemiddeld complex, €50-150K/jr.

## Extra check
Ongeacht schaal: hoe sterker de fit met "dezelfde lerende over tijd beoordelen op voldoende volume", hoe hoger de prioriteit.

---

## Wat we toetsen bij het bouwen van de lijst

_Vastgesteld met Dante op 2026-07-21, teruggebracht naar één vraag op 2026-07-22._

**Eén vraag per organisatie: wie neemt het examen af?**

Zoek `"[naam] examen"` of `"[naam] examenreglement"` en lees wie het werk beoordeelt.
- **Eigen docenten of examinatoren** → in de lijst. Citaat + URL vastleggen.
- **Een externe instantie** (CBR, CCV, TCVT, Het Oranje Kruis, CerTech, IBKI, een branche-examenbureau) → eruit. Daar ligt het nakijkbudget, niet bij hen.
- **Niet te vinden** → "onbekend", niet afwijzen. Pas checken als de organisatie daadwerkelijk outreach krijgt.

**Vervallen: de aparte particulier-toets** (2026-07-22). De lijst komt uit NRTO en CRKBO, en lidmaatschap van die registers ís het bewijs van particulier. Los nazoeken leverde nooit een andere uitkomst en kostte de helft van de tijd per organisatie. Komt een naam van buiten die registers, dan check je het alsnog handmatig.

**Bewust overgeslagen bij het bouwen van de lijst:** voldoende volume, dezelfde lerende over tijd, meerdere opdrachtvormen, meerdere beoordelaars, vastgelegd eisenkader, LMS.

Reden: die zes kosten samen 20 tot 40 minuten per organisatie (ze vragen om OER, examenreglement of NVAO-rapport) terwijl ze de uitkomst vrijwel nooit veranderen. Een erkende particuliere opleider die zelf beoordeelt, voldoet er in de praktijk altijd aan. De examenvraag kost circa één minuut en beslist wel degelijk wie erin komt.

Ze zijn niet waardeloos, alleen verkeerd getimed. Doe ze pas voor organisaties die daadwerkelijk outreach krijgen, want dan leveren ze tegelijk de inhoud voor de messaging. Bij NOVI gaf precies dat NVAO-rapport de zin dat de feedback te mager is en de cijferonderbouwing een aandachtspunt: geen vinkje, maar de opening van een mail. Wat al onderzocht is staat in `dossiers.md` en hoeft niet opnieuw.

## Marktgroepen die je kunt negeren

_Vastgesteld 2026-07-21 op basis van circa 15 gekwalificeerde organisaties uit de NRTO- en CRKBO-registers. Elke groep hieronder is met echte gevallen getest, niet aangenomen._

**De snelste diskwalificatievraag: wie neemt het examen af?** Ligt het examen bij een externe certificerende instantie, dan ligt het nakijkbudget daar ook. Dat is in één zoekopdracht te checken en scheelt al het andere werk.

1. **Veiligheids- en certificaattrainers** (VCA, BHV, EHBO, offshore). Externe partijen beoordelen. Gezien bij DELTA Safety ("examen wordt afgenomen (…) onder toezicht van Het Oranje Kruis") en Peinemann.
2. **Rijbewijs-, machine- en transportopleiders** (heftruck, kraan, code 95). CBR, CCV en TCVT doen de examinering. Gezien bij Van Buuren ("praktijkgedeelte leg je af onder toezicht van het CBR"), SOMA ("onafhankelijk examenbureau (…) TCVT-certificatieschema"), LOC, Vervoerscollege Venlo.
3. **Technische vakopleiders die examinering uitbesteden.** ROVC toetst "onder verantwoordelijkheid van CerTech", Innovam examineert als IBKI met praktijkexamens. Let op: dit is geen sectoroordeel maar een modeloordeel. KOB (bouw) en Wateropleidingen komen er juist wél door, omdat hun docenten het werk zelf nakijken.
4. **BBL-praktijkopleidingsbedrijven.** Zij leveren praktijkuren, het ROC doet de formele toetsing. Gezien bij Tetrix en IW Nederland.
5. **Praktijkbeoordelaars zonder geschreven werk.** NBZ beoordeelt "een zwemles in de praktijk". Geen tekst betekent geen product.
6. **Normzetters, certificeerders en brancheorganisaties.** Geen eigen lerenden. Gezien bij DSI.
7. **Uitgevers en kennisbedrijven met losse trainingsdagen.** Wolters Kluwer, Sdu, Berghauser Pont, Euroforum.
8. **Eenmanszaken in coaching en therapie.** Staan massaal in het CRKBO, geen volume en geen tweede beoordelaar.
9. **Publiek bekostigde instellingen.** Hogescholen, universiteiten, ROC's en de Open Universiteit. Andere ICP, andere sales complexity.
10. **Particulier voortgezet onderwijs.** Eerder afgevallen op besluit van Dante.

**Nuance (2026-08-07): koepel/brancheorganisatie sluit niet automatisch uit.** Marktgroep 6 hierboven ("brancheorganisatie/koepel — vertegenwoordigt leden, beoordeelt niets") gaat over partijen zoals DSI die zelf geen opleiding aanbieden. Draait een beroepsvereniging zelf een verplichte beroepsopleiding met eigen beoordeeld werk (examens, opdrachten), dan is het functioneel een opleider en telt de gewone poort-0-toets. Bevestigd bij NOB Beroepsopleiding Belastingadviseurs, Register Belastingadviseurs RB Academy en Federatie Belastingadviseurs FB (akkoord Dante 2026-08-07). Check bij twijfel: biedt de vereniging zelf de opleiding aan met eigen beoordeling, of accrediteert ze enkel opleidingen van derden (dan blijft het marktgroep 6, zoals DSI)?

**Vervallen (2026-07-23): de uitsluiting van zorg, psychologie en postmaster.** Besluit van Dante: die mogen blijven. Ze worden gewoon op poort 0 beoordeeld als elke andere organisatie. Dat scheelt 14 opleiders op de huidige lijst, waaronder de zwaarste fits qua geschreven werk (SOMT, Thim van der Laan, Breederode, King nascholing). Let op: punt 8 hierboven blijft wel gelden, eenmanszaken in coaching en therapie vallen nog steeds af op volume en op het ontbreken van een tweede beoordelaar. De uitsluiting gold dus feitelijk alleen voor die onderkant, niet voor geaccrediteerde zorgopleiders met een thesis of portfolio.

**Waar het wél zit:** NVAO-geaccrediteerde particuliere hogescholen en postacademische of post-hbo instituten met een thesis, eindwerkstuk of open examenonderdelen. Alle bewezen gevallen tot nu toe komen daarvandaan.

## Namen uit het ICP-document zijn hypotheses
Instellingen die in Jeroens ICP-document genoemd worden, worden **niet** automatisch toegevoegd of afgewezen. Elke naam gaat langs poort 0 en de particulier-toets, net als elke andere. De Open Universiteit staat er bijvoorbeeld als voorbeeld in, maar valt af op publieke bekostiging.
