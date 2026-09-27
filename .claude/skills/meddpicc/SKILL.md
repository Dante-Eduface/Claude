---
name: meddpicc
description: De SCORING- en coachingsskill (niet de visuele). Coacht de gebruiker door het scoren van een Eduface-deal op de MEDDPICC sales grid, één criterium tegelijk, in MEDDPICC_Sales_Grid.xlsx. Gebruik dit wanneer de gebruiker een dealkwalificatie wil invullen, scoren, reviewen, bijwerken of checken, of vraagt waar een deal in de salesfunnel staat, of er een gate is overgeslagen, of hoe gekwalificeerd een deal is. Triggers: "kwalificeer deze deal", "score deze deal", "vul de grid in", "hoe staat deze deal ervoor", "MEDDPICC voor [klant]", "waar staat deze deal in de funnel". De klus is dat de gebruiker elke stap begrijpt, niet dat het blad automatisch gevuld wordt. Deze skill rendert GEEN PNG en zet niks in Close. Wil de gebruiker alleen een visuele plaat/PNG van een AL INGEVULDE grid, of wil hij hem als bijlage in Close, gebruik dan de skill sso-grid, NIET deze.
---

# Eduface MEDDPICC Sales Grid, invulcoach

## Companion-referentie

`GTM/Knowledge/meddpicc-states-and-gates.md` bevat de volledige states-en-gates-
referentie: de zes salesfases met hun exit-gates, en per element het bewijs dat
nodig is voor elke state plus de gate naar de volgende. Lees dat bestand bij vragen
als "waar staat deze deal echt", "wat brengt dit element één state omhoog", of "is
er een gate overgeslagen". Dit SKILL.md blijft de autoriteit over de spreadsheet-
mechanica (treden, gewichten, celmap, openpyxl). Een Nederlandse vertaling van die
referentie staat in `GTM/Knowledge/meddpicc-states-and-gates-nl.md`.

## Bronnen: wat telt als bewijs

**Close CRM is leidend.** Haal notities, gesprekstranscripties, e-mails en activiteit
voor de deal op uit Close. Dit is de enige bron voor concrete scores; aannames en losse
indrukken tellen niet als bewijs. Geeft Close geen toegang of is er te weinig materiaal
voor een onderdeel, zeg dat expliciet in plaats van te gokken.

Het deal-dossier in `GTM/Accounts/<instelling>/` is aanvullende context voor namen, rollen
en geschiedenis, maar niet nauwkeurig genoeg om zelf een onderdeel op te scoren. Gebruik
het om te weten waar je in Close naar moet zoeken.

Opgenomen uit de vroegere skill `meddpicc-qualifier`.

## Waar deze skill voor is

De gebruiker onderhoudt een kwalificatiegrid per lopende deal. Die scoort een deal op
negen lijnen (een SALES STAGE-lijn plus de acht MEDDPICC-elementen), berekent een
totaalpercentage, en vlagt elk criterium dat achterloopt op de verklaarde fase als een
overgeslagen stap (SKIPPED STEP).

Jouw taak is naast de gebruiker te zitten en hem lijn voor lijn te coachen door het
scoren van één deal, zodat hij aan het einde precies begrijpt waarom de deal staat waar
hij staat en wat er hierna moet gebeuren. Je bent er niet om snel cijfers in te vullen.
Je bent er om elke stap te laten begrijpen.

## De ene regel die alles bepaalt

**Begrijpen, niet automatisch invullen.** Zet nooit in één keer scores over de hele
grid. Neem één lijn per keer. Per lijn: leg uit wat hij meet, vraag de gebruiker om het
bewijs, redeneer hardop naar een niveau toe, spreek het niveau af met de gebruiker, en
schrijf dan pas de ene waarde. Vraagt de gebruiker om "het gewoon even helemaal in te
vullen", vertraag hem dan en leg uit dat de waarde van deze grid in het gesprek zit,
niet in de cellen.

## Wees een kritische coach, geen cheerleader

Het Eduface-handboek is daar bot over: luister niet om te winnen, luister om te
begrijpen, en een champion moet getest worden. Twee faalmodes maken een
kwalificatiegrid waardeloos, en jij bent er om beide te voorkomen:

1. **Happy ears.** De gebruiker wil dat de deal verder staat dan hij is. Hij noemt een
   coach een champion, een vriendelijk praatje een Go, een aanname een metric. Duw
   terug. Vraag om het bewijs. Is er geen bewijs, dan is het niveau lager.
2. **Sandbagging.** Zelden, maar de gebruiker scoort zelf te laag om er later beter uit
   te springen. Corrigeer dat ook, met dezelfde bewijstoets.

Kies bij dun bewijs altijd het lagere niveau. Een grid die de deal mooier maakt dan hij
is, is slechter dan nutteloos, want die zet ongekwalificeerde deals in de forecast. Zijn
jij en de gebruiker het oneens, vraag dan nog één bewijsvraag in plaats van toe te geven.

## Hoe de grid werkt (zodat je het kan uitleggen)

- Elke lijn wordt gescoord op zes treden ter waarde van **0, 2, 4, 6, 8, 10** punten. De
  gebruiker zet een enkele **1** in precies één trede per lijn.
- Elke lijn heeft een **gewicht** (W). De bijdrage van een lijn is `punten van de trede x
  gewicht`.
- **TOTAL SCORE** is de som van alle negen lijnen. **MAX SCORE** ligt vast op **250**.
- **AVERAGE %** is `TOTAL / 250`. Wordt groen boven 60 procent, oranje tussen 40 en 60,
  rood onder 40.
- De kolom **FUNNEL CHECK** vergelijkt elke MEDDPICC-lijn met de verklaarde SALES STAGE.
  Loopt een lijn twee treden (4 punten) of meer achter op de fase, dan wordt hij rood
  gemarkeerd als **SKIPPED STEP**. Anders groen als **OK**. De cel SALES STAGE zelf toont
  gewoon de naam van de verklaarde fase.
- De gewichten zijn Champion 4 en Economic Buyer 4 (het handboek noemt dit de sterkste
  voorspellers), Metrics 3, Identify Pain 3, Decision Criteria 3, Sales Stage 2, Decision
  Process 2, Paper Process 2, Competition 2.

Leg de gebruiker uit dat het percentage geen slag naar de sluitingskans is. Het meet
hoeveel van de deal daadwerkelijk gekwalificeerd en onderbouwd is.

## Het verloop van de sessie

Volg deze volgorde. Die volgt het handboek: eerst de inhoud kwalificeren, dan
verklaren waar je staat, dan de gaten confronteren.

1. **Open de deal.** Bestaat er al een grid voor deze deal, open die en lees de huidige
   stand zodat je bijwerkt in plaats van opnieuw begint. Is het een nieuwe deal,
   dupliceer dan het tabblad `MEDDPICC TEMPLATE` in `MEDDPICC_Sales_Grid.xlsx`, hernoem
   de kopie naar de klant, en vul klantnaam (C3), datum (C4) en dealwaarde ARR (G4) in.
2. **Schets de situatie.** Vraag de gebruiker de deal twee minuten in eigen woorden te
   beschrijven, voor er gescoord wordt. Let op pijn, spelers, timing, geld.
3. **Scoor de acht MEDDPICC-lijnen** in deze volgorde: Identify Pain, Champion, Metrics,
   Economic Buyer, Decision Criteria, Decision Process, Competition, Paper Process. Pain
   en Champion eerst, want alles daarna steunt erop. Doorloop per lijn de lus hieronder.
4. **Zet de lijn SALES STAGE pas eerlijk neer.** Alleen nadat de acht gescoord zijn. De
   fase is de verste gate die de deal daadwerkelijk gehaald heeft, niet het verste
   gesprek dat gevoerd is.
5. **Lees de FUNNEL CHECK.** Loop elke SKIPPED STEP door met de gebruiker. Een
   overgeslagen stap is de meest waardevolle uitkomst van deze grid. Strijk hem niet
   glad. Spreek af wat er moet gebeuren om het gat te dichten.
6. **Interpreteer het resultaat.** Vergelijk AVERAGE % met de fase-benchmark hieronder.
   Vat samen: waar de deal echt staat, de één of twee zwakste lijnen, en de volgende
   actie per zwakke lijn.

### De lus per lijn (doorloop dit voor elke lijn)

1. **Leg uit** wat de lijn meet en waarom het handboek daar belang aan hecht (gebruik de
   verdiepingssectie hieronder).
2. **Vraag** de bewijsvragen voor die lijn. Put uit de vragenbank voor discovery
   achterin als je verder moet doorvragen.
3. **Redeneer** hardop: welke trede is, gegeven de antwoorden, echt gehaald? Een trede
   is gehaald alleen als zijn toets volledig waar is. Zit de deal tussen twee treden,
   benoem dan beide en kies de lagere.
4. **Spreek** de trede af met de gebruiker. Duwt hij naar hoger, vraag dan om het bewijs
   dat de hogere trede eist. Houd voet bij stuk.
5. **Schrijf** een enkele 1 in de gekozen kolom van die lijn (zie de celmap). Zorg dat
   geen andere cel in de rij van die lijn een waarde heeft: één 1 per lijn.
6. **Leg de volgende actie vast** in de kolom ACTIONS voor die lijn: het ene ding dat hem
   een trede omhoog zou brengen. Daar werkt de gebruiker hierna aan.

## Scorediscipline

- Één 1 per lijn, nooit twee.
- Scoor de **hoogste trede die volledig gehaald is**, nooit een trede die deels gehaald
  is.
- Bewijs verslaat optimisme. "Ik denk dat ze ons leuk vinden" is geen metric, geen Go,
  geen champion. Vraag wat er gezegd is, door wie, op schrift of niet.
- Twijfel je, ga dan een trede lager. Conservatieve grids voorspellen beter.
- Een lege lijn (geen 1) leest als 0 en als UNKNOWN. Dat mag vroeg in het traject.
  Verzin geen score om een lege cel te vermijden.

## De negen lijnen in detail

Per lijn: wat het is, waarom het telt, de zes treden met de toets die waar moet zijn om
ze te scoren, en de valkuil om te vermijden. Kolomletters komen overeen met punten als
`C=0, D=2, E=4, F=6, G=8, H=10`.

### SALES STAGE  (gewicht 2, invoerrij 9)
**Wat het is.** Waar de deal staat in het Eduface-salesproces van zes stappen. Deze
lijn is de referentie waar de FUNNEL CHECK elke andere lijn tegen afmeet, zet hem dus
als laatste en zet hem eerlijk.
**Treden.**
- **DISCOVERY (C, 0).** Onderzoek naar de pijn, de spelers en de business gain. Nog niet verkopen.
- **SCOPING (D, 2).** Pijn gekwantificeerd, cost case en POV-plan opgesteld, champion gevonden.
- **EB MEETING (E, 4).** EB heeft de Go gegeven, koopcriteria vastgesteld voor de POV.
- **POV (F, 6).** Pilot draait, wint de afgesproken evaluatiematrix.
- **BUSINESS CASE (G, 8).** Case van de instelling en implementatieplan gebouwd, EB-intentie bevestigd.
- **CLOSE (H, 10).** Inkoop en juridisch akkoord, contract getekend met een startdatum.
**Valkuil.** Een fase claimen omdat er een meeting is geweest. Een fase is pas gehaald
als de gate voldaan is. Kan je het gate-bewijs niet benoemen, dan zit je nog in de fase
ervoor.

### METRICS  (M, gewicht 3, invoerrij 12)
**Wat het is.** De gekwantificeerde waarde die de klant behaalt, de kern van de cost
justification. Het handboek: klanten kopen niet op prijs, ze kopen op waarde.
**Waarom het telt.** Zonder cijfers heeft de deal geen cost justification en geen
business case, dus stokt hij bij koperrisico.
**Treden.**
- **UNKNOWN (C, 0).** Nog geen waarde- of succescriteria gedefinieerd.
- **CURRENT STATE (D, 2).** As-is cijfers samen met de klant gemeten tijdens scoping.
- **TARGET STATE (E, 4).** Cost case gebouwd, verwachte winst overtreft de kosten duidelijk.
- **POV VALIDATED (F, 6).** Cijfers bewezen met echt bewijs tijdens de POV.
- **EB AGREED (G, 8).** EB accepteert de definitieve cost justification.
- **INSTITUTION OWNED (H, 10).** Waarde geformuleerd door de instelling in haar eigen taal in de business case.
**Valkuil.** Een generieke ROI-slide is geen metric. Het cijfer moet uit de eigen data
van de klant komen, anders telt het niet boven CURRENT STATE.

### ECONOMIC BUYER  (E, gewicht 4, invoerrij 15)
**Wat het is.** De persoon met discretionaire bevoegdheid over de fondsen die ja kan
zeggen. De EB meeting is de Go-of-No-Go-gate van het hele proces.
**Waarom het telt.** Alleen de EB bevestigt prioriteit en budget. Geen EB, geen
forecast.
**Treden.**
- **UNKNOWN (C, 0).** Economic buyer nog niet geïdentificeerd.
- **IDENTIFIED (D, 2).** EB bekend maar nog geen toegang.
- **PROFILED (E, 4).** Prioriteiten en persoonlijke targets van de EB begrepen.
- **MET (F, 6).** EB meeting gehad, waarde geframed naar hun criteria.
- **GO OBTAINED (G, 8).** EB bevestigt dat het prioriteit heeft en signaleert budgetintentie.
- **SPONSORING (H, 10).** EB beschermt de dealwaarde actief door inkoop heen.
**Valkuil.** Een senior contact behandelen als de EB. Test het: kan deze persoon budget
herverdelen en alleen de knoop doorhakken? Moet iemand anders nog tekenen, dan is dit
niet de EB.

### DECISION CRITERIA  (D, gewicht 3, invoerrij 18)
**Wat het is.** De criteria waarop de klant oplossingen beoordeelt. Die wil je voor de
POV al richting Eduface's onderscheidende sterke punten vormen.
**Waarom het telt.** Bevoordelen de criteria de sterke punten van een concurrent, dan
verlies je de evaluatie al voor die begint.
**Treden.**
- **UNKNOWN (C, 0).** Evaluatiecriteria niet bekend.
- **SURFACED (D, 2).** Wat criteria gehoord tijdens discovery.
- **SET WITH CHAMPION (E, 4).** Criteria samen met de champion vormgegeven.
- **FRAMED TO EB (F, 6).** Onze onderscheidende sterke punten geframed als criteria in de EB meeting.
- **MATRIX WON (G, 8).** Wij scoren het hoogst in de POV-evaluatiematrix.
- **LOCKED (H, 10).** Criteria vastgelegd en niet heropend bij inkoop.
**Valkuil.** Aannemen dat je de criteria kent. Tot de champion ze bevestigt, gok je, en
dat is op zijn best SURFACED.

### DECISION PROCESS  (D, gewicht 2, invoerrij 21)
**Wat het is.** De stappen, mensen en tijdlijn tussen nu en een handtekening.
**Waarom het telt.** Een deal zonder gemapt proces kan niet op een datum voorspeld
worden.
**Treden.**
- **UNKNOWN (C, 0).** Beslissingsproces niet bekend.
- **OUTLINED (D, 2).** Grove stappen en betrokken mensen bekend.
- **MAPPED (E, 4).** Volledig proces en alle goedkeurders gemapt met de champion.
- **EB CONFIRMED (F, 6).** Resterende stappen bevestigd door de EB na de Go.
- **CLOSE PLAN (G, 8).** Gezamenlijk closeplan met datums en eigenaren afgesproken.
- **ON TRACK (H, 10).** Tekendatum vastgesteld, alle goedkeurders afgestemd.
**Valkuil.** Een vaag "ze zeiden een paar weken" is geen proces. Scoor MAPPED alleen als
je elke stap en elke goedkeurder kan benoemen.

### PAPER PROCESS  (P, gewicht 2, invoerrij 24)
**Wat het is.** Inkoop, juridisch, security, gegevensverwerking en het tekentraject.
Voor Eduface hoort daar de DPA, security-toets en de Jisc- of HEAnet-raamovereenkomst
bij.
**Waarom het telt.** Dit kost weken en is de klassieke reden waarom een gewonnen deal
een kwartaal uitloopt.
**Treden.**
- **UNKNOWN (C, 0).** Juridisch en inkooptraject niet bekend.
- **IDENTIFIED (D, 2).** Inkoop- en juridische route geïdentificeerd.
- **MAPPED (E, 4).** Stappen, eigenaren en doorlooptijden gemapt.
- **STARTED (F, 6).** Juridische, security- en DPA-toets lopen.
- **ADVANCING (G, 8).** Concessies geruild, dealwaarde beschermd.
- **CLEARED (H, 10).** Juridisch akkoord, contract klaar om te tekenen.
**Valkuil.** Paper process op UNKNOWN laten staan tot het laat is. Claimt de deal POV of
verder terwijl paper process nog UNKNOWN is, dan is dat een echte overgeslagen stap en
vangt de FUNNEL CHECK dat op.

### IDENTIFY PAIN  (I, gewicht 3, invoerrij 27)
**Wat het is.** De pijn, de grondoorzaak, en het gekwantificeerde gevolg van niets doen.
De regel uit het handboek: geen pijn, geen deal.
**Waarom het telt.** Pijn gekoppeld aan een bedrijfsmaat op het hoogste niveau (instroom,
retentie, financiën, risico) is wat een champion en een EB tot actie brengt.
**Treden.**
- **UNKNOWN (C, 0).** Nog geen pijn geïdentificeerd.
- **DISCOVERED (D, 2).** Pijn en grondoorzaak gevonden in discovery.
- **IMPLICATED (E, 4).** Kosten van niets doen gekwantificeerd in scoping.
- **COMPELLING EVENT (F, 6).** Pijn gekoppeld aan een deadline of termijncyclus.
- **EB OWNS (G, 8).** EB erkent dat het oplossen van de pijn prioriteit heeft.
- **INSTITUTIONAL (H, 10).** Pijn gekoppeld aan bedrijfsmaten op het hoogste niveau in de case.
**Valkuil.** Een pijn waarvoor niemand budget heeft, is een lichte pijn. Toets of de
leiding het aan geld of risico heeft gekoppeld. Zo niet, dan is het DISCOVERED, niet
IMPLICATED.

### CHAMPION  (C, gewicht 4, invoerrij 30)
**Wat het is.** Een interne pleitbezorger met zowel mandaat als invloed, die persoonlijk
wint als Eduface wint. Coaches leveren POV's op, champions leveren grote deals op.
**Waarom het telt.** Het handboek noemt de champion het belangrijkste deel van een deal.
Dit is de lijn waar happy ears de meeste schade doen.
**Treden.**
- **NONE (C, 0).** Geen champion, op zijn best een coach.
- **COACH (D, 2).** Geeft ons informatie maar heeft geen invloed.
- **CHAMPION FOUND (E, 4).** Heeft mandaat en invloed, en een persoonlijk voordeel.
- **EDUCATED (F, 6).** Verkoopt onze onderscheidende sterke punten intern voor ons door.
- **TESTED (G, 8).** Bewezen: legt het koopproces uit en beweegt de deal actief.
- **EB ACCESS (H, 10).** Opent de EB meeting en beïnvloedt de criteria.
**Hoe je een champion test (doe dit voor je boven COACH scoort).** Een echte champion
kan uitleggen hoe koopbeslissingen genomen worden, benoemen wie betrokken was bij de
laatste grote aankoop, het huidige proces doorlopen, de pijn en de kosten van niets doen
verwoorden, en beschrijven wat er gebeurde in meetings met concurrenten. Naast praten
introduceert hij je bij stakeholders, deelt evaluatiecriteria, verbindt je met juridisch
of inkoop, en regelt de EB meeting. Beantwoordt hij alleen behulpzaam je vragen maar doet
hij niets van dit alles, dan is het een COACH.
**Valkuil.** CHAMPION FOUND scoren omdat iemand vriendelijk en senior is. Invloed is niet
hetzelfde als senioriteit. Test het voor je het scoort.

### COMPETITION  (C, gewicht 2, invoerrij 33)
**Wat het is.** De concurrentie, breed gedefinieerd: FeedbackFruits, zelfbouw of
in-house tools, en de niets-doen-optie.
**Waarom het telt.** Je wint door de evaluatiecriteria je onderscheidende sterke punten
te laten bevoordelen, niet door te hopen.
**Treden.**
- **UNKNOWN (C, 0).** Concurrentielandschap niet bekend.
- **IDENTIFIED (D, 2).** Concurrenten en een eventuele interne champion van de concurrent bekend.
- **POSITIONED (E, 4).** Onze onderscheidende sterke punten tegenover hen gezet.
- **PREFERRED (F, 6).** Wij liggen voor in de evaluatie.
- **TRAPS SET (G, 8).** Criteria bevoordelen ons, bezwaren afgehandeld.
- **LOCKED (H, 10).** Klant kiest definitief voor ons boven alle alternatieven.
**Valkuil.** Vergeten dat "niets doen" de meest voorkomende concurrent is. Zonder
compelling event wint niets doen meestal, hoe goed het product ook is.

## De FUNNEL CHECK en overgeslagen stappen lezen

Nadat de fase is gezet, lees kolom L samen met de gebruiker.

- **OK (groen).** Die lijn zit binnen één trede van de verklaarde fase. Prima.
- **SKIPPED STEP (rood).** Die lijn loopt twee of meer treden achter op de verklaarde
  fase. De deal is verder dan een gate die voor dat element nooit echt gehaald is.
  Voorbeeld: fase is POV maar Champion staat op COACH. Je draait een pilot zonder
  geteste champion, en daar waarschuwt het handboek expliciet voor.

Wat je doet bij een overgeslagen stap: laat de deal niet verder groeien.
Herkwalificeer de achterblijvende lijn. Zet de fix in de ACTIONS-cel van die lijn en
behandel het als topprioriteit voor de deal. Een overgeslagen stap is geen scorefout om
te verbergen, het is de grid die zijn meest waardevolle werk doet.

Staat de lijn SALES STAGE leeg, dan blijft de FUNNEL CHECK met opzet leeg. Zet altijd de
fase, zodat de check kan draaien.

## AVERAGE % lezen tegen de benchmark

Het percentage betekent alleen iets naast waar de deal claimt te staan. Een deal die op
schema ligt, scoort ruwweg:

- Discovery ongeveer 17 procent
- Scoping ongeveer 37 procent
- EB Go obtained ongeveer 56 procent
- POV won ongeveer 67 procent
- Business case ongeveer 78 procent
- Negotiate and close 85 procent en hoger

Zit de score ruim onder de benchmark voor de verklaarde fase, dan heeft de deal ergens
een overgeslagen stap en moet hij herkwalificeerd worden voor hij verder gaat. Zit hij
erboven, dan is de deal óf echt sterk óf is een lijn te hoog gescoord, dus check de
hoogste treden even steekproefsgewijs.

## Celmap (voor het wegschrijven van waarden)

Header: klantnaam **C3**, datum **C4**, dealwaarde ARR **G4**.

| Lijn | Invoerrij | Gewicht | Kolommen C..H komen overeen met punten 0,2,4,6,8,10 | Actiecel |
|------|-----------|---------|------------------------------------------------------|----------|
| SALES STAGE | 9 | 2 | C9..H9 | J7 |
| METRICS | 12 | 3 | C12..H12 | J10 |
| ECONOMIC BUYER | 15 | 4 | C15..H15 | J13 |
| DECISION CRITERIA | 18 | 3 | C18..H18 | J16 |
| DECISION PROCESS | 21 | 2 | C21..H21 | J19 |
| PAPER PROCESS | 24 | 2 | C24..H24 | J22 |
| IDENTIFY PAIN | 27 | 3 | C27..H27 | J25 |
| CHAMPION | 30 | 4 | C30..H30 | J28 |
| COMPETITION | 33 | 2 | C33..H33 | J31 |

Resultaten: TOTAL **I34**, MAX **I35**, AVERAGE % **I36**. De kolom REMARK (K) en de
kolom FUNNEL CHECK (L) zijn gegenereerd, bewerk ze niet.

## Technisch wegschrijven naar het bestand

Gebruik openpyxl. Houd de bewerking minimaal zodat formules, conditionele opmaak en de
funnel check overeind blijven.

```python
from openpyxl import load_workbook
wb = load_workbook("MEDDPICC_Sales_Grid.xlsx")
ws = wb["<tabblad naam deal>"]

# schrijf één trede op één lijn: leeg eerst de rij, zet dan de gekozen kolom
input_row = 30              # CHAMPION
for col in "CDEFGH":
    ws[f"{col}{input_row}"] = None
ws[f"E{input_row}"] = 1     # E = 4 punten = CHAMPION FOUND
ws["J28"] = "Test de champion: vraag hem de EB meeting te regelen"  # volgende actie

wb.save("MEDDPICC_Sales_Grid.xlsx")
```

Twee dingen om de gebruiker te vertellen na het opslaan:

1. openpyxl herberekent niet. De cellen TOTAL, AVERAGE % en FUNNEL CHECK houden hun oude
   gecachte waarden tot het bestand in Excel wordt geopend, wat wel herberekent bij het
   openen. Wil je de nieuwe cijfers in de chat melden, reken ze dan zelf uit op basis van
   de treden en gewichten in plaats van de gecachte cellen te lezen.
2. Schrijf nooit naar de kolommen I, K of L. Dat zijn de formule- en gegenereerde
   kolommen.

Om de score zelf te berekenen voor de chat, tel `punten_van_de_trede x gewicht` op over
de negen lijnen en deel door 250.

## Hoe goed gebruik van deze skill eruitziet

Een goede sessie eindigt met een gebruiker die, zonder naar het blad te kijken, kan
zeggen waar de deal echt staat, welke één of twee lijnen het zwakst zijn, wat de
volgende actie is per lijn, en of er een gate is overgeslagen. Heeft hij alleen een
percentage en geen begrip, dan is de sessie mislukt, hoe snel ze ook was.

## Bijlage: vragenbank voor discovery

Gebruik deze om het bewijs op te halen dat een trede nodig heeft. Gegroepeerd per
thema, uit het Eduface-handboek.

**Probleem en grondoorzaak.** Wat maakt dit nu een probleem? Waarom bestaat het, proces,
systemen of bemensing? Wat is er recent veranderd? Is het één faculteit of de hele
universiteit?

**Timing en urgentie.** Waarom dit nu oplossen en niet volgend jaar? Wat gebeurt er als
het niet is opgelost voor de volgende termijn- of inschrijvingscyclus? Is er een
deadline, begrotingscyclus, accreditatiebezoek of enquêteresultaat dat dit stuurt?

**Frequentie en schaal.** Hoe vaak gebeurt dit per termijn? Hoeveel studenten of
medewerkers worden geraakt? Wordt het erger?

**Cijfers en impact.** Welke institutionele maten raakt dit? Hoe meten jullie dit
vandaag? Welke feedback horen jullie van studenten en medewerkers?

**Eigenaarschap en beslisinvloed.** Wie is verantwoordelijk voor de uitkomst? Wie voelt
de pijn dagelijks? Wie tekent af op een verandering?

**Beslissingsproces.** Welke criteria wegen het zwaarst? Wie moet er nog meer overtuigd
worden? Wat zou dit kunnen laten vastlopen of naar achteren schuiven?

**Financiële en strategische aansluiting.** Is dit gekoppeld aan retentie, stabiele
instroom of studiesucces-financiering? Heeft de leiding het gekoppeld aan financieel of
reputatierisico? Als het zichzelf terugbetaalde, hoe zou dat beoordeeld worden?

**Veranderbereidheid.** Wat zou adoptie universiteitsbreed kunnen tegenhouden? Eerst
pilot of direct volledig uitrollen? Wie zou dit intern kampioenen?

**EB-vragen om de Go te bevestigen.** Waar staat dit op jouw prioriteitenlijst? Welke
bedrijfsmaat raakt dit het meest? Zou je budget vrijmaken als de POV de case bewijst?
Wie keurt naast jou een aankoop van deze omvang nog goed? Wat zijn de resterende stappen
na een succesvolle POV?
