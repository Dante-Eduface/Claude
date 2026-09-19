# Werkvoorraad: welke bronnen zijn af, welke niet

Dit bestand is de **stand van zaken voor `/lead-sourcing-nl`**. Werk hem bij na elke ronde, anders doet de volgende chat het werk over.

Laatst bijgewerkt: 2026-09-02 (Agent 1: omzet-, eigendoms- en overnameroute).

## Sourcing-ronde 2026-09-02 (Agent 1) - lane BEDRIJVENKANT (SBI-codes / werknemersklasse)

**Opdracht:** de kop van de markt vinden vanuit de bedrijvenkant in plaats van de onderwijskant. Welke onderwijsbedrijven zijn simpelweg groot als bedrijf? SBI 85.5 (85.52/85.53/85.59), 85.42, 85.32, 85.6. Ondergrens 50 medewerkers of duidelijk 1.000+ lerenden per jaar.

**DE BELANGRIJKSTE VONDST VAN DEZE RONDE, LEES DIT EERST.**
**Acht Salta-labels staan nog op `gekwalificeerd` terwijl Salta uitgesloten hoort te zijn.** Dat is een outreach-risico, want die kunnen zo de pijplijn in lopen. Het gaat om: `org_bestuursacademie-nederland`, `org_hogeschool-markus-verbeek-praehep`, `org_hogeschool-scheidegger`, `org_loi`, `org_ncoi-opleidingen`, `org_nibe-svv-opleidingen`, `org_salta-group`, `org_schoevers`. NTI, Luzac en Computrain staan wel goed op `geblokkeerd`. Ik heb dit NIET zelf omgezet omdat het 8 gekwalificeerde organisaties uit de pijplijn haalt; dat is een besluit voor Dante.

**Wat wel en niet werkt op deze route, zodat de volgende ronde het niet overdoet.**
- **DOODLOPEND: bedrijvenregisters op SBI-code.** company.info en drimble geven geen crawlbare lijst per SBI-code (404 op elke geprobeerde index-URL). CBS 81588NED/81589NED geeft alleen AANTALLEN per grootteklasse, geen bedrijfsnamen. LinkedIn-bedrijfspagina's blijven HTTP 999. Zonder KvK-abonnement is de directe SBI-route niet af te lopen.
- **DOODLOPEND: awards- en ranglijsten.** Beste Opleider van Nederland (Springest/BOVNL) en de opleiderslijst van opleiding.nl leveren vooral KLEINE aanbieders op; de winnaars zijn trainingsbureaus van een handvol mensen. Geen omvangssignaal. MT1000 zit achter een betaalmuur.
- **DIT WERKT WEL, EN IS DE OPBRENGST VAN DEZE RONDE: het DUO-register van erkende niet-bekostigde mbo-opleidingen.** Dat is het complete 85.32-register, 6.705 regels, 148 instellingen, downloadbaar als xlsx: https://duo.nl/open_onderwijsdata/images/03.-erkende-niet-bekostigde-opleidingen-nieuwer.xlsx (peildatum 01-08-2026). Aggregeren per BRIN geeft een harde ranglijst op aantal erkenningen.
- Voor 85.42 bestaat GEEN vergelijkbaar open bestand. DUO verwijst voor het erkenningenoverzicht HO naar ico@duo.nl. Alleen telefonisch of per mail op te vragen.

**Uitkomst van het DUO-mbo-register: die tak is nu vrijwel dicht.** Van de 148 instellingen is de niet-bekostigde kop op twee na al op de lijst gezet in een eerdere ronde, en die eerdere ronde heeft `aantal_opleidingen` bovendien al poort-0b-gefilterd ingevuld (lagere getallen dan de ruwe crebo-telling). Die heb ik daarom expres NIET overschreven met de ruwe registertelling.

**De twee gaten die er nog in zaten, zijn nu gedicht:**
- **Marlijn Academie** (BRIN 30UW, Langeweg) stond op `kandidaat` met `beoordeelt_zelf=Onbekend`, terwijl het met **728 erkenningen de grootste niet-bekostigde mbo-aanbieder van Nederland** is, ruim het dubbele van NCOI (327). Nu `gekwalificeerd`, poort 0 Ja op de eigen OER: eigen examencommissie, instellingsexamens, lesopdrachten met herkansing.
- **Maas College** (BRIN 31KE, Rotterdam, 77 erkenningen) stond op `kandidaat`. Nu `gekwalificeerd`. Bonus: hun over-ons-pagina voert een expliciet **AI-beleid richting studenten**, direct bruikbaar als haakje.

**De val uit de opdracht is twee keer echt opgetreden.** Bekostigde instellingen staan gewoon in het niet-bekostigde register:
- **Talland College** (145 erkenningen, zou nr 5 zijn) = de fusie van Horizon College en Regio College, publiek bekostigd ROC.
- **SVO vakopleiding food** (26 erkenningen) = bekostigd, OCW betaalt een groot deel.
Filteren op licentie geeft dus echt valse treffers. Praktische vuistregel: BRIN-reeksen 0xxx/25xx/27xx zijn vrijwel altijd bekostigd, 30xx/31xx/32xx zijn de particulieren.

**Nieuw toegevoegd deze ronde (4 rijen):**
- **RINO Groep** (Utrecht, postacademisch GGZ) - gekwalificeerd, poort 0 Ja uit de eigen studiegids GZ: toetsdocent maakt en beoordeelt de toets, inleveren en feedback via het eigen Onderwijsportaal. 125 medewerkers.
- **NSPOH** (public health) - poort 0 Ja, sterk: docenten kijken moduleopdrachten na in MijnNSPOH met feedback- en teruggeefknop, drie eigen examencommissies. 150 medewerkers. Staat op **geblokkeerd**: al een lead in Close (status Prospect), eerst afstemmen.
- **AIHR** (Rotterdam, online HR-certificering) - kandidaat, 100+ medewerkers. Poort 0 bewust NIET op Ja: nergens staat wie de capstone nakijkt, en "retry as often as you like" wijst eerder op geautomatiseerd nakijken. De 85.000 alumni is cumulatief, geen jaarcijfer.
- **RINO Amsterdam** - kandidaat, aparte organisatie van RINO Groep. Poort 0 niet af te maken, rino.nl gaf herhaald socket hang up.

**Wat deze lane nog kan halen, in volgorde van opbrengst.**
1. **Het erkenningenoverzicht HO opvragen bij DUO** (ico@duo.nl, 070 757 51 33). Dat is het enige complete 85.42-register en het bestaat wel, alleen niet als download. Eén mail.
2. **RINO Amsterdam afmaken** via de OER-PDF rino.nl/sites/default/files/2022-09/OER GZ definitief 14 oktober 2021.pdf zodra de site weer laadt.
3. **AIHR poort 0** door de capstone-beoordelingsprocedure na te vragen. Grootste onbesliste naam op medewerkers.
4. **NIPA Eindhoven** is de enige uit het mbo-register zonder `aantal_opleidingen`. Ruwe registertelling is 21, moet nog poort-0b-gefilterd worden.
5. Nog ongecheckt in het postacademische hoekje: **PAO Techniek en Management, GITP, PBLQ, IMK Opleidingen, Merlijn Groep, IVM (Instituut voor Veiligheid en Milieu), SkillsTown**. Allemaal plausibel 50+ medewerkers, poort 0 onzeker.

**Wat deze lane NIET meer moet proberen:** SBI 85.52 (cultuuronderwijs), 85.53 (rijscholen) en 85.6 (dienstverlening voor het onderwijs). 85.53 valt af want het CBR examineert; 85.6 is per definitie de externe examinator of het adviesbureau, dus poort 0 Nee; 85.52 is versnipperd in muziek- en dansscholen zonder beoordeeld schrijfwerk. Zie dossiers.md.

## Sourcing-ronde 2026-09-02 (Agent 1) - GELD EN EIGENDOM: investeerders, overnames, jaarcijfers

Opdracht: de kop van de markt in kaart brengen via **het geld en het eigenaarschap**, niet via opleiderslijsten. Stand master ging van 404 naar **429 organisaties** (+23 uit deze lane, +4 uit een parallelle lane). `doctor` geeft 0 fouten.

### De hoofdconclusie: de aanname klopt, met een nuance

Waar een investeerder of overname in het spel is, komen er cijfers naar buiten die de eigen site nooit noemt. Deze ronde opgeleverd: Westpoort 7 miljoen euro omzet en 20 medewerkers (via Antea), Computrain 20.000 cursisten per jaar, Lindenhaeghe 120.000 financieel professionals per jaar, Moovs 75 vaste medewerkers plus 150 freelancers.

**De nuance:** het zijn vaker omzet-, medewerker- en vestigingscijfers dan lerendenaantallen, en dealbedragen worden vrijwel nooit genoemd. "Financiele details over de deal zijn niet bekendgemaakt" staat in bijna elk bericht.

**Wat NIET werkt, niet opnieuw proberen.** Brede zoekopdrachten op jaarrekeningen, omzetranglijsten en KvK-data leveren niets. Bedrijvenregisters zetten omzet achter een betaalmuur (Creditsafe, Graydon, PitchBook, privateequityinfo). Brookz geeft alleen branchebrede EBITDA-multiples. De EW-500 bevat geen opleiders. **De enige gratis harde bron is het overname- of investeerdersbericht zelf: MenA.nl, consultancy.nl en de portfoliopagina van de investeerder.** Begin daar de volgende keer meteen.

### De vangst die de moedercheck rechtvaardigt

**Computrain is een Salta-label.** Noemt zichzelf de grootste IT-opleider van Nederland, draait 20.000+ cursisten per jaar, en stond nog niet op de lijst. Zonder de eigendomsroute was dit koud benaderd naar een bestaande relatie. Op `geblokkeerd` gezet. Citaat: "Computrain is onderdeel van Salta Group." (computrain.nl/over-ons).

**Certify360 EdTech Group = het voormalige Eikk Onderwijsgroep** (opgericht 2019, Baarn), eigenaar **Capital A Investment Partners** (Fund IV, vintage 2019). Dat was nog niet vastgelegd. Gevolg: er zijn zes labels die alleen in de Eikk-persberichten staan en NIET op de Capital A-portfoliopagina, en die stonden geen van alle op de lijst: **Kenneth Smit, MyCademy, icttrainingen.nl, Match and More Opleidingen, Florens Opleidingen en Dolphiq**. Alle zes toegevoegd als kandidaat onder org_certify360-edtech-group. **Open vraag:** zitten die zes na de rebrand nog in de groep, of zijn ze afgestoten? Dat is alleen met een KvK-uittreksel met concernrelaties af te maken.

**Habeo+ Hogeschool is Avans+.** Stond al op de lijst maar zonder de alias, waardoor "Avans+" bij elke volgende zoekronde als nieuwe organisatie zou opduiken. Aliassen toegevoegd. Per 1 juli 2025 zelfstandige onbekostigde particuliere hbo-instelling, los van Avans Hogeschool, sinds oktober 2025 onder de naam Habeo+.

### Nieuwe eigendomsblokken

- **De Complementair Groep** (buy-and-build, zeer actief). Zeven merken: **Vijfhart** ("de grootste onafhankelijke IT-opleider van Nederland"), **Cibit**, **AT Computing**, **Coach+Result**, Sonnevelt (stond al op de lijst), **Vijfhart ARBO-opleidingen** en Winc Academy (stond al op de lijst). Plus **Master IT** (okt 2024), Spiegel en Reflex Opleidingen (jan 2024), Safety First Opleidingen en Decisco (2019). Zes merken nieuw toegevoegd. **Eigenaar/investeerder NIET gevonden**: geen investeerder op de eigen site, niet in de nagelopen PE-portfolios. Alleen met KvK af te maken.
- **Nedvest (family office)** kocht op 27-05-2026 **Schouten & Nelissen** van de familie Schouten, na 46 jaar. Dochterbedrijven in de deal: **Relevance, Competence, New Dawn en Thema** (alle vier toegevoegd). Directie blijft, Steven Steenbergen topman. Ixly was in 2022 al binnengehaald. Relevant voor outreach: nieuwe eigenaar betekent doorgaans nieuw investeringsbudget.
- **Ergon Capital (BE)** bezit **Lyceo Education Group**, grootste bijlesbedrijf van NL, met **44 handelsnamen** waaronder Studiekring (80+ vestigingen), juffrouwjulia en Schoolkitchen. Lyceo en Studiekring vallen af op poort 0 (zij begeleiden, de school beoordeelt), maar als eigendomsblok vastgelegd zodat die 44 namen niet los opduiken.
- **Antea Participaties** heeft 90 procent van **Opleidingscentrum Westpoort** (7 miljoen euro omzet 2022, 5 vestigingen). Valt af op poort 0.
- **Lepaya** (NL edtech, VC-gefinancierd) kocht **Krauthammer**. Let op: Lepaya is zelf een leerplatform en dus eerder concurrent dan klant.
- **Beeckestijn Business School** (stond al gekwalificeerd) kocht in januari 2025 **Growth Tribe** uit faillissement.
- **NPM Capital** kocht Futurewhiz/**Squla** van het Amerikaanse LLCP. Platform, geen opleider, afgevallen.

### Buitenlandse concerns: gericht gecheckt, niets gevonden

**Galileo Global Education** (Parijs, eigenaar Montagu, grootste for-profit HO-aanbieder van Europa) heeft geen Nederlandse instelling. **Study Group** richt zich op de VS en Azie. Voor **Wilmington** is geen NL-opleider gevonden. Niet opnieuw uitzoeken zonder een nieuw overnamebericht. Wel bevestigd: **Wolters Kluwer** verkocht zijn Belgische opleidingstak aan NCOI (Salta). AcadeMedia, Navitas en Cegos/Euroforum stonden al op de lijst uit eerdere rondes.

### Investeerders die NIET uitgeklapt zijn, en wat daarvoor nodig is

1. **De Complementair Groep** - eigenaar onbekend. Nodig: KvK-uittreksel met concernrelaties.
2. **Nedvest** - portfoliopagina niet gevonden; alleen de S&N-deal is publiek. Nodig: nedvest.nl doorlopen of KvK.
3. **Ergon Capital** - de 44 handelsnamen van Lyceo zijn nergens als lijst gepubliceerd. Nodig: KvK-handelsnamenregister op Lyceo Onderwijsgroep. Lage prioriteit want poort 0 is Nee.
4. **Antea Participaties** - de participatiepagina gaf HTTP 404. Nodig: antea.nl/category/nieuws doorbladeren op meer opleiders in portefeuille.
5. **Capital A** - portfolio is compleet doorgelopen, Certify360 is het enige onderwijsbedrijf. Boertiengroep en Kiwa staan in de historische lijst en zijn niet nagelopen op een opleidingstak.
6. **Waterland, Bencis, Egeria, Gilde, NPM** - geen NL-opleider in portefeuille gevonden buiten Squla. Nodig: hun portfoliopagina's een voor een openen, niet via zoekmachine.

### Nog open in deze lane

- **Poort 0 ontbreekt** bij alle 13 nieuwe kandidaten uit deze ronde. Bewust: de eigendomskaart was de opdracht, en gokken is verboden. IT-merken (Vijfhart, Cibit, AT Computing, Master IT, icttrainingen.nl) en veiligheidsmerken (Vijfhart ARBO) wijzen richting Nee vanwege externe certificering, maar geen enkele site zegt het letterlijk.
- **Vijfhart poort 0**: twee pagina's geprobeerd (over-vijfhart en de examenpagina), geen uitsluitsel. Bellen of doorvragen. Omvang: 500.000 is CUMULATIEF, geen jaarcijfer, niet overnemen.
- **Twee dubbele rijen op te ruimen** (stond al open): org_euroforum-bv-cegos-group naast org_euroforum-bv, en org_nationale-academie-voor-media-maatschappij naast org_nationale-academie-voor-media-en-maatschappij.
- **NCOI Opleidingen (org_ncoi-opleidingen) staat op `gekwalificeerd`** terwijl het een Salta-label is en dus uitgesloten hoort te zijn. Nakijken en op geblokkeerd zetten.

## Eerdere rondes


Laatst bijgewerkt: 2026-09-02 (Agent 1: opleidingsgroepen en holdings uitgeklapt naar hun merken)
Vorige update: 2026-08-18 (Agent 1: CPION gerichte oogst afgemaakt, CRKBO-midden score 2 volledig mechanisch doorgelopen, NRTO-restlijst leeggeveegd).
Stand master: **347 organisaties, 219 gekwalificeerd (Ja), 111 kandidaat, 6 geblokkeerd** (`pipeline.py status`).

## Sourcing-ronde 2026-09-02 (Agent 1) - GROEPEN EN HOLDINGS UITGEKLAPT

Omgekeerde opdracht: niet opleiders zoeken en daarna de omvang meten, maar de grootste particuliere opleiders top-down vinden door **opleidingsgroepen uit te klappen naar hun merken**. Ondergrens 1.000 lerenden per jaar, alles boven 3.000 is prioriteit. Stand master ging van 316 naar **347 organisaties** (+31 rijen), 219 gekwalificeerd, 111 kandidaat, 6 geblokkeerd.

**Vijf moeder-correcties: merken die als "zelfstandig" op de lijst stonden maar onder een groep vallen.** Dit was het echte risico van deze ronde, want zo n merk kan zomaar bij een bestaande Close-relatie horen.
- **HTI Amsterdam** -> KPE Groep (divisies KPE Bouw en Infra, KPE Vastgoed, KPE Lab)
- **OVD Opleidingen** -> Opleidingsgroep Gilde-BT
- **STOC** -> dyo people solutions (zustermerk van VAPRO)
- **NHA** -> Maxwell Holding (familie Frencken, Panningen)
- **IVA Driebergen** en **Winford** -> beide AcadeMedia (Zweeds, beursgenoteerd)

**Twee openstaande vragen uit eerdere rondes beantwoord.**
1. *Laudius en NHA, zelfde familielijn?* Ja maar als CONCURRENTEN, niet als zustermerken. Een Frencken-broer is voor 16 miljoen uitgekocht uit Maxwell Holding en startte Laudius in Venlo tegenover NHA. Laudius blijft dus zelfstandig.
2. *Inspiring Generations-portfolio.* Nog steeds niet hard, maar er is nu een richting: in bedrijvenregisters staat de holding (KvK 77134699) naast CompaNanny Nederland en Family Services, dus het portfolio wijst naar KINDEROPVANG. Variva blijft de enige bevestigde onderwijsdeelneming. Alleen af te maken met een KvK-uittreksel met concernrelaties; verwacht er geen opleiders meer.

**Nieuw gevonden groepen die nog niet op de lijst stonden.**
- **KMM Groep** (Kennis, Marketing en Media), moeder van de hele IVIO-familie. Zestien bedrijven, ruim 700 medewerkers. IVIO-merken: Wereldschool, IVIO@School, IVIO-Opleidingen, IVIO-Examenbureau, IVIO-Boeken, LanguageOne, Edufax, Infinity College.
- **Opleidingsgroep Gilde-BT**, vijf instituten: GBT Opleidingen, OVD Opleidingen, Response Instituut, Hypnose Zorg Nederland, Mentaal Vitaal Sterk. Plus platform UQ Learn en 12 partners.
- **Euroforum BV** (Cegos Group, via Bridgepoint), drie merken: Euroforum, SBO (stond al op de lijst) en Secretary Management Institute. Portfolio van 300+ programma s, maar veel congressen en losse dagen, dus poort 0b per opleiding toetsen.
- **AcadeMedia**, **Maxwell Holding**, **KPE Groep**, **Inspiring Generations Holding** als aparte moederrijen toegevoegd.

**Uitgesloten en waarom.**
- **Luzac Onderwijs** is de grootste particuliere VO-aanbieder van NL (14 vestigingen), maar is sinds 2016 van de NCOI Opleidingsgroep = **Salta**. Op geblokkeerd gezet, niet benaderen.
- **IVIO-Examenbureau** en **Examenadviesburo** (Certify360) vallen af op poort 0: dat zijn zelf de externe examinatoren, ze nemen examens af voor derden.
- **SUAS** is geen apart merk meer, suas.nl redirect naar sn.nl, opgegaan in Schouten en Nelissen.

**Relaties rond geblokkeerde accounts vastgelegd** (Capabel, Tio, Business School Notenboom lopen al). Genoteerd bij de buren: TMO Fashion valt onder dezelfde Calder Holding als Capabel, en Business School Nederland deelt de moeder-slug met Notenboom. Beide zijn gekwalificeerd en mogen benaderd, maar stem eerst af.

**Wat er in deze lane nog open staat.**
1. **Poort 0 per merk** bij de nieuw aangemaakte kandidaten: IVIO@School, de vier Gilde-BT-merken, KPE Groep, FOI, Euroforum en SMI, Winford. Ze staan er nu met moeder en bron, maar zonder bewijscitaat.
2. **Winford** blijft hangen op poort 0: de site zegt wel "erkende particuliere onderwijsinstelling" en "je maakt je schoolexamens en centraal examen gewoon bij ons op school", maar noemt nergens wie het werk beoordeelt. Particulier vo kan via staatsexamen lopen. Bellen of doorvragen, niet gokken.
3. **Lerenden per jaar ontbreekt bij bijna alle groepen.** Groepen publiceren zelden een totaal. Wereldschool heeft 140 docenten (a circa 80 leerlingen), Winford 600 leerlingen, Calder 750 medewerkers. Gilde-BT s "100.000 opgeleid" is cumulatief en dus NIET bruikbaar als jaarcijfer.
4. **Schouten Company** heeft nog labels die niet los getoetst zijn: Competence, New Dawn, Relevance, Realise, New Heroes, Thema, Archipel, Someone. Waarschijnlijk training en coaching, dus poort 0 twijfelachtig.
5. **Dubbele rij om op te ruimen**: org_nationale-academie-voor-media-maatschappij en org_nationale-academie-voor-media-en-maatschappij zijn dezelfde organisatie.

## Sourcing-ronde 2026-09-02 (Agent 1) — de KOP op omvang: NRTO-leden en brancheopleiders

**Opdracht was omgedraaid**: niet opleiders zoeken en dan meten, maar top-down op omvang. Ondergrens 1.000 lerenden per jaar, prioriteit boven 3.000. Doel: elke grote particuliere opleider in NL moet benaderd zijn, dus de lijst moet aan de bovenkant compleet zijn.

Buiten beschouwing: alle Salta-labels (NCOI, LOI, NTI, Schoevers, ISBW, Markus Verbeek Praehep, Bestuursacademie, Scheidegger, De Baak, NIBE-SVV, EVC Centrum) plus Capabel, Tio en Business School Notenboom (lopende relatie).

**Wat is af.**
- **NRTO-ledenlijst mechanisch op omvang gescand — AF.** Alle 780 leden gededupeerd tegen master, 564 domeinen die er niet in stonden gescand op deelnemersaantallen. De kop van die lijst is hiermee in beeld; wat er niet uit kwam publiceert geen cijfer.
- **Brancheopleiders/thuisstudie apart gescand** (SRA, NBA, evofenedex, TVVL, NSPOH, Volandis, Wij Techniek, IW, NHA, Laudius, IVIO, Mikrocentrum, SOMA, ICM, SkillsTown, SBI Formaat, GITP, STC Next, Berghauser Pont, SBO, Euroforum e.a.). Vrijwel niemand publiceert een deelnemersaantal; zie de restpunten hieronder.
- **Alle 209 master-orgs zonder omvangcijfer mechanisch gescand.** Leverde de bestaande Ja-opleiders op die wel een cijfer publiceren.

**Nieuw op de lijst (4, allemaal poort 0 nog Onbekend, wel groot):** IPC Groene Ruimte 15.000/jaar, BTR Trainingen 94.750/jaar, Thinq Academy / Logistic Force 10.500/jaar, MYOS Opleidingen 1.000/jaar.

**Omvang ingevuld op bestaande records (8):** OSR 4.500, Stichting Wateropleidingen 4.334, Wittenborg 1.500, Evangelisch College 1.500, Thomas More Hogeschool 1.000, Kyden 922 (instroom, 3-jarig traject dus circa 2.700 tegelijk), Sonnevelt 830 (afgeleid), NHA expliciet op onbekend.

**Nee met citaat, dus niet opnemen ondanks omvang:** BLOM 30.000/jaar (examenbureau Pontifex), Özel 18.000 (VCA/TCVT/Code 95), Trafieq 15.000/jaar (CBR), IMK Opleidingen 7.000/jaar (Nipex), STE Languages 5.000/jaar (geen beoordeeld schrijfwerk), ABC Opleiding 1.000/jaar (Curaçao). **SRM blijkt een Salta/NCOI-label** (srm.nl redirect naar ncoi.nl/srm).

**Twee methodelessen, staan uitgeschreven in `dossiers.md`:**
1. Knip zinnen niet op punten als je Nederlandse getallen zoekt; "2.000.000 cursisten" valt dan weg. Pak een venster rond het trefwoord.
2. **WebSearch-samenvattingen verzinnen deelnemersaantallen.** Mikrocentrum "7000 cursisten" en SOMA "14000 cursisten" waren met curl én WebFetch niet op de bronpagina terug te vinden. Beide niet overgenomen. Verifieer elk getal op de bronpagina zelf.

**Wat er in deze bak nog openstaat.**
1. ~~**Poort 0 voor de vier nieuwe grote namen** (IPC, BTR, Thinq, MYOS).~~ **AF 2026-09-02.** BTR, IPC en Thinq/Logistic Force op Nee en `afgevallen` (extern examen of helemaal geen examen), MYOS op Ja en `gekwalificeerd` maar zonder beoordeeld schrijfwerk. Citaten in `dossiers.md` onder "Poort 0 uitgezocht op 2026-09-02". Les: grote deelnemersaantallen bij dit type opleider zijn bijna altijd veiligheids- of transportcertificering, en die gaat per definitie extern.
2. **De grote brancheopleiders publiceren geen cijfers.** NHA, Laudius, IVIO, Nevi, VAPRO, Schouten & Nelissen, SRA, NBA Opleidingen, evofenedex, TVVL, NSPOH, Volandis, ICM, SOMA en Mikrocentrum staan wel op de lijst maar zonder getal. Route is bellen of het jaarverslag opvragen, niet nog een zoekronde. TIAS gaf drie tegenstrijdige cijfers uit derde bronnen en is leeg gelaten.
3. **Cumulatieve cijfers zijn niet omgezet.** Een reeks opleiders publiceert alleen een totaal sinds oprichting (Gilde-BT >100.000, Vijfhart 500.000, ExplainiT 350.000, NLtraining 85.000, De Academies 30.000, ITIP 29.000). Die zeggen wel iets over schaal maar niets over de drempel van 1.000 per jaar.

## Sourcing-ronde 2026-08-18 (Agent 1) - wat is gedaan

+30 nieuwe Ja, plus Stichting BOB-KOB van kandidaat naar gekwalificeerd. Alle citaten in `dossiers.md` onder de kop "Ronde 2026-08-18".

- **Bak 10b, CPION gerichte oogst - AF.** 142 instituten uit `cpion-targeted-2026-08-13.json`, na dedupe en het uitfilteren van publieke instellingen 63 namen over. 12 Ja (o.a. Instituut Mentoris met eigen examencommissie, Credit Management Instituut, Melior Advies, 1801, PAO Psychologie, Hollands College), 4 Nee met citaat (SOBA/SVPB, Riskforum/externe examinator, Gladwell/Scrum.org, Marnix = publieke pabo), rest Onbekend omdat de site JS-gerenderd is of geen toetsinformatie publiceert.
- **Bak 6, CRKBO-midden score 2 - voor het eerst volledig doorgelopen.** 679 rijen, na filteren 482 domeinen, alle 482 mechanisch gescand. 18 Ja (circa 4 procent), 13 Nee met citaat, de rest ruis. Deze bak is hiermee AF.
- **Bak 5, NRTO middenmoot score 1-4 - praktisch AF.** Resterende namen opnieuw tegen de master gehouden: 42 unieke domeinen, vrijwel allemaal taal-, veiligheid-, rijschool- of ICT-certificering. Geen plausibele eigen-nakijkprofielen meer. Geen werkvoorraad meer, alleen ruis.

**Nieuwe methode, gebruik deze voortaan.** De dunne staart is mechanisch af te werken: sitemap.xml -> alle opleiding/examen/toets/reglement/studiegids-URL's -> tekst platslaan -> per zin matchen op een OWN-regex (scriptie, eindopdracht, proeve van bekwaamheid, eindgesprek, portfolio wordt beoordeeld, examencommissie, beoordeeld door docent) en een EXTERN-regex (CBR, CCV, TCVT, SVPB, IBKI, SVH, TCI, Scrum.org, EXIN, staatsexamen). Externe treffer wint van eigen treffer. Circa 10 organisaties per minuut, alleen curl, geen model-tokens. Script `scan2.py`, beschreven in `dossiers.md`.

**Bug in `pipeline.py`:** `exists --naam` zoekt in `people.csv`, niet in `orgs.csv`, en is dus onbruikbaar voor organisatie-dedupe (gaf 40x "bestaat: false" terwijl BKOU, Variva en Scobe op de lijst stonden). Dedupe voorlopig met een genormaliseerde grep tegen `master/orgs.csv` op naam + naam_aliassen + domein. Fixen wanneer iemand toch in het script zit.

**Wat er nu open staat.** De echt kansrijke bakken zijn op. Wat resteert:
1. De volledige CPION-register-enumeratie (nooit afgemaakt, zie punt 7 hieronder).
2. CRKBO score 0 (2.758 rijen) en de 442 met score -3: nooit aangeraakt, per definitie zwak, alleen doen met de mechanische scan en alleen als er weer een volumedoel is.
3. Inspiring Generations-portfolio via een KvK-uittreksel.
4. De belroute-lijsten (44 CRKBO-Onbekenden en de mbo-belroute): geen citaat online, wel bevestigd eigen traject. Bellen, niet zoeken.

## Sourcing-ronde 2026-08-13b (Agent 1, tweede ronde) — wat is gedaan

Alle citaten en afvallers in `dossiers.md` onder de "Ronde 2026-08-13b"-koppen. Totaal: ~130 organisaties onderzocht, +25 Ja, +30 Onbekend.

- **Bak 1, postacademische restlijst — gerichte namen AF, CPION deels.** Nieuw Ja: NSOB, Kyden (uitvoerder Beroepsopleiding Advocaten) en BKOU (Bedrijfskunde Opleiding Utrecht, twee assessoren op het adviesrapport). De dossiers-claim "postacademisch nog niet afgezocht" bleek grotendeels verouderd: Grotius, Nevi, Actuarieel Instituut, SPO, Beroepsopleiding Notariaat, ASRE, Habeo+, Schouten & Nelissen, NCI, Nyenrode stonden er al. Nee met citaat: mediation-sector (Intop examineert, sectorbreed), Full-Finance, Fiscount, Academie voor Vastgoed (SVMNIVO), Artra (SEU). Treasury = alleen VU (publiek). **CPION: de volledige register-enumeratie (recursieve substring-search op cpion.nl/Opleiding/Search, cap ~98 per query) is na ~2,5 uur afgebroken zonder resultaat; wel is een gerichte oogst met 31 domeintermen gedaan: 283 opleidingen / 142 instituten in `cpion-targeted-2026-08-13.json`.** Daaruit rolt een nieuwe werkbak (zie punt 11 hieronder).
- **Bak 2, particuliere rijkserkende mbo — AF.** Verse DUO RIO-trek (mbo_onderwijslicenties + onderwijsinstellingserkenningen): 92 niet-publieke instellingen met actieve niet-bekostigde mbo-licenties, 49 nog nergens vastgelegd, allemaal getrieerd. +15 Ja (o.a. Dentallect, Auxilio, EuroCollege, GOC, Litop, ORGB, GO-College, VanDoen, Educared*, i4healthcare*, Flair*, HaKa* — *deze vier kwamen via het NRTO-blok maar zijn ook DUO-erkende mbo), 11 Onbekend (belroute), afvallers met citaat of sector-grond in dossiers (beveiliging = SVPB, uiterlijke verzorging vaak TCI/Exuive, kappers = ambacht-filter, BOA = ExTH). Restblokje van 5 technieknamen ook gedaan: SVT, Technicom en De Voshaar = Ja; Vakopleiding Afbouw en TOI = Onbekend. **Bak 2 volledig AF.**
- **Bak 3, NRTO middenmoot 1-4 — blokken 2 t/m 6 gedaan (ca. 95 namen), ~60 resterend.** Nieuw Ja: NHA, Laudius, Auxilium Academy, EVC Centrum Nederland, Educared, i4healthcare, Flair Scholing, IVIO-Opleidingen, HaKa Nederland, Dental Best Practice. Dichtheid ~1 Ja op 10 (beter dan blok 1 dankzij de thuisstudie-instituten en zorg-mbo's). Herbruikbare patronen: TCI/Exuive = externe examinering uiterlijke verzorging (4x bevestigd), taleninstituten = staatsexamens extern, PRINCE2/LSS/scrum = externe certificering, thuisstudie-instituten met docent-nakijkwerk (NHA/Laudius/LOI-model) = Ja. Resterende ~60 namen (score 1-2) staan onderaan het zesde-blok-dossier.

## Sourcing-ronde 2026-08-13 (Agent 1) — wat is gedaan

Details en alle citaten in `dossiers.md` onder de vier "Ronde 2026-08-13"-koppen.

- **De Complementair Groep volledig af**: 8 merken. Nieuw Ja: **Sonnevelt Opleidingen**. Nee: Vijfhart, Cibit, AT Computing, Coach+Result, Vijfhart ARBO, Master IT (allemaal externe certificering of losse trainingen). Winc stond al op Ja.
- **Eduro Groep af**: T Gear = lesmethode/uitgever, Nee. Daarmee is Eduro helemaal afgerond.
- **CS Opleidingen (Certify360) gevonden en Ja**: casemanagement verzuim (CROV/RCCM), eigen schriftelijk examen + assessment door eigen examinator. Site: cs-opleidingen.nl (was eerder onvindbaar).
- **Inspiring Generations: portfolio niet publiek vindbaar.** Holding (KvK 77134699) zonder site of merkenlijst; enige bevestigde deelneming is Variva (al Ja). Route: KvK-concernrelaties opvragen. Verder niets mogelijk zonder KvK-uittreksel.
- **Navitas / The Hague Pathway College: Ja** — eigen Assessment Policy: assessments "first marked independently by an experienced member of the teaching team". Mogelijk bruggetje naar Navitas wereldwijd/UK.
- **Particuliere HO-restlijst AF**: DUO ho_erkenningen_rio opnieuw getrokken (128 niet-bekostigde instellingen), alles gefilterd. Nieuw Ja: **Academie voor Geesteswetenschappen** en **HTI Amsterdam**. Onbekend: Saba University School of Medicine, IUA Amsterdam (i-ua.nl). Nee: IHE Delft (functioneel publiek gefinancierd), Hogeschool KPZ (publiek), Nederlandse Loodsencorporatie (publiekrechtelijk). Pro Education blijft eraf (belroute-besluit 2026-07-22).
- **Salta-merken los geverifieerd (alleen dossier, geen CSV-rijen — blokkade "niet los benaderen" blijft)**: Hogeschool NCOI, LOI, NTI, Schoevers Ja met citaat; ISBW en Markus Verbeek Ja structureel (NVAO/WHW); De Baak Nee (geen beoordeling). Vondst voor de dealstrategie: Salta heeft één **Centrale Examencommissie Hoger Onderwijs** over de hogescholen heen.
- **NRTO middenmoot 1-4, eerste blok (20 namen, alle score 4) af**: 1 Ja (**OVD Opleidingen**, erkende mbo retail), 3 Onbekend (Detex, Helix Academy, NL Mode Academie), 14 Nee met citaat, NIBE-SVV overgeslagen (Salta). Resterend in deze bak: ~157 namen (score 1-3 plus rest score 4), dichtheid laag (1 Ja op 20).

**Gefixt (2026-08-13):** rijen 122 en 127 van `targetlijst-nl.csv` (STOC, Medivus) hadden 8 velden door een ongeëscapte komma in de Categorie-kolom. Samengevoegd tot 7 velden, geen data verloren.

## Diepteronde 2026-08-12: 24 contacten heronderzocht op person-research-niveau

Alle 24 al eerder onderzochte contacten (grotendeels al benaderd, zie `berichten-nl.csv`) kregen een diepere, bronnen-geverifieerde tweede ronde. Resultaat in `haakjes-nl.csv` (backups: `haakjes-nl-backup-voor-diepteronde-0812.csv`, `haakjes-nl.backup-2026-08-12.csv`, `haakjes-nl-backup-voor-feedback-0812.csv`).

- **Twee ICP-afvallers vervangen door de juiste persoon, blijven zelf toch afvallen**: Jeroen van Dam (Intop) → Louis van Dam onderzocht, maar Intop levert zelf geen geschreven werk (dat zit bij de ziekenhuizen in de praktijkleerweg) — Intop blijft afgevoerd. Tamar Schats (I AM College) → Patrick Molenaar (Onderwijs directeur, boven haar) toegevoegd als sterker primair contact, wel bruikbaar.
- **Vijf contacten op niveau 1 gezet (geen bericht)**: Ernst Eijsvogel (Freia), Jeroen van Dam (vervangen, zie boven), Rosa de Boer (SOMT), Femke Bex (Artemis, wel met een gedekt maar ouder organisatiehaakje - Dante akkoord het toch te gebruiken), Laura van Driel (BTSG).
- **Twee bronfouten gecorrigeerd**: NOVI/Larissa Petrus-citaat (was "feedback te mager", moet "vaak wat minimaal"/"erg summier" zijn, ook gefixt in `.claude/agents/shift-research.md`); PHOV/Corné Bulkmans-citaat (was twee pagina's samengeknipt).
- **Zorg-uitsluiting blijft staan** (zie punt 9 hieronder en `decisions/log.md` 2026-08-12): SOMT/Rosa de Boer blijft een prima lead, geen aanpassing nodig.
- **Afgerond 2026-08-12**: outreach-bericht voor Patrick Molenaar toegevoegd aan `berichten-nl.csv` (connectieverzoek, 293 tekens, haakje = tegenstelling examinering/kwaliteitszorg bij Tio vs. "geen onnodige theorie-examens"-pitch bij I AM College). Status "klaar, nog niet verzonden".

## Tracking-kolommen `berichten-nl.csv` (toegevoegd 2026-08-12)

`Verzonden` is vervangen door drie aparte kolommen: `LinkedIn connectieverzoek verzonden`, `Email verstuurd`, `Cold call gedaan` (elk een datum). Alleen de eerste is nu gevuld (uit een Lemlist-export). `Email verstuurd` en `Cold call gedaan` staan bewust leeg: de NL-opleiderscampagne loopt via LinkedIn (zie `outreach-kanaal-linkedin` in memory), geen mail of cold call gebruikt tot nu toe. Niet zelf invullen zonder dat Dante bevestigt dat een contact via die kanalen benaderd is.

## Ronde 2026-08-13 (Agent 2) — contacten bij de nieuwe Agent-1-oogst

35 rijen toegevoegd aan `contacten-linkedin-nl.csv` (nu 365 rijen). 29 organisaties uit de rondes 2026-08-13 en 2026-08-13b behandeld, plus 6 Salta-merken op stap 0 geblokkeerd.

- **22 contacten aangewezen**, allemaal met LinkedIn-URL behalve Gelders Opleidingsinstituut (Monique Bosch, alleen via site/KvK, eerst handmatig opzoeken).
- **7 keer geen contact**: Laudius, The Hague Pathway College, Dentallect, ORGB Opleidingen, EVC Centrum Nederland, Stichting Vakopleiding Techniek, plus de zes Salta-merken (NIBE-SVV, Bestuursacademie, Markus Verbeek Praehep, Schoevers, LOI, Scheidegger) die op stap 0 afvallen.
- **Twee vondsten voor Agent 1:** Dentallect is een product van Bohn Stafleu van Loghum (uitgever, raakt poort 0), en er bestaan twee entiteiten met de naam EVC: EVC Nederland Hilversum (zelfstandig) en EVC Centrum Nederland dat onder NCOI/Salta valt. Uitzoeken welke op de lijst hoort.
- **Moeder-correcties:** HTI Amsterdam valt onder KPE Groep (stond als Zelfstandig). Laudius heeft een Frencken-directie, dezelfde familielijn als NHA; eigendomsrelatie nog niet bevestigd.

## Stand contactenlijst (`/contact-sourcing-nl`, Agent 2) — bijgewerkt 2026-08-07 avond

Van de **158 Ja-opleiders** hebben nu **alle** organisaties een aangewezen contact of een expliciete "geen contact" met reden. Contactenbestand: `contacten-linkedin-nl.csv`, 330 rijen.

**STOC en Medivus zijn afgehandeld (2026-08-07, zelfde sessie als deze update).** Ze stonden sinds 22-07 gedropt wegens geen citaat; de mbo-workflow vond alsnog bewijs (eigen examencommissie, CREBO-erkend). Dante gaf akkoord om ze terug te zetten. Contacten gevonden: Arnold van Duijn (Directeur STOC, LinkedIn bevestigd) en Simone Pieterson (eigenaar/oprichter Medivus — **LinkedIn-URL nog niet gevonden ondanks meerdere pogingen, eerst handmatig opzoeken voor outreach**).

**De koepel-vraag is beantwoord.** Dante gaf akkoord (2026-08-07): een beroepsvereniging die zelf een verplichte beroepsopleiding draait met eigen beoordeeld werk telt als opleider, ook al is het org-vorm een koepel. Vastgelegd in `icp.md`. NOB, RB Academy en FB Academy blijven op de lijst. Twee restpunten die overblijven, geen ICP-vraag meer maar contactkwaliteit:
1. **NOB-contact (Paulien Geerdink) is algemeen directeur van de héle NOB, niet specifiek van de Beroepsopleiding.** Overwegen een gerichter contact bij de Beroepsopleiding zelf te zoeken.
2. **Federatie Belastingadviseurs (FB) en Stichting BV/BmS Opleidingen** hebben nog geen publiek vindbare directeursnaam — staan op GEEN CONTACT, KvK-route nodig.

**Nog openstaand, geen ICP-vraag maar wel aandacht waard:**
- **Nyenrode (Universiteit Nyenrode B.V.)** — enige aangewezen contact is Michael Erkens, Rector Magnificus. EB-niveau bij een grote universiteit, waarschijnlijk te hoog/te formeel voor een koude LinkedIn-benadering. Overwegen een programmadirecteur Finance & Control te zoeken in plaats van de rector.
- **Stichting Postdoctorale Beroepsopleiding GGZ Amsterdam** wordt uitgevoerd door RINO Amsterdam; geen eigen stichtingsdirecteur publiek vindbaar, alleen hoofdopleiders per deeltraject (bv. OG-opleiding: drs. E.S. Luycx / prof. dr. H.M.Y. Koomen). Staat op **GEEN CONTACT**. Nader uitzoeken alleen bij concrete interesse.
- Nog circa 10 organisaties uit de +50-batch staan op GEEN CONTACT met een KvK-route genoteerd in de "Waarom deze persoon"-kolom van `contacten-linkedin-nl.csv` (o.a. Fundashon Mariadal, Oranjestad Academy, S.e.T. Academie, In Service voor ZorgOnderwijs, Mij een zorg, Medischinstituut, Het Volwassenen College, Wedding Business Academy, HBO Academy). Route staat er telkens bij.

**Kleinere aandachtspunten, geen actie nodig tenzij gevraagd:**
- Contacten zonder bevestigde LinkedIn-URL ondanks bevestigde naam+functie: Kicozo/Madeleine Kerkhof, Simone Pieterson/Medivus, en een paar uit eerdere batches — zoek even na als je Agent 3/4 op deze personen zet. **Nooit een URL verzinnen.**
- **Kennisinstituut Complementaire Zorg** staat op de targetlijst onder die naam, maar de organisatie heet officieel **Kicozo**. Check bij gebruik welke naam klopt.
- Google Drive-sync heeft tijdens deze sourcing-sessie een paar keer tussentijdse schrijfacties teruggedraaid. Na elke schrijfactie op `contacten-linkedin-nl.csv` een stabiliteitscheck (md5 + rijentelling, 2-3x met een paar seconden ertussen) doen voordat je verdergaat.
- **Nederlands Talen Instituut (NTI)** bleek tijdens contactonderzoek sinds 2014 onderdeel van Salta Group (al in Close). Geblokkeerd, zie `UITGESLOTEN.md`. Check bij toekomstige losse Salta-merken altijd even het moederschap voor je contactonderzoek start.

Bronnen van de +50 sessie (2026-08-07), start was 108 Ja:
- **+29** particuliere rijkserkende mbo (DUO-register niet-bekostigde mbo-opleidingen, 149 instellingen → 59 schone kandidaten na uitfilteren publieke ROC's/AOC's en zwakke-sector ambacht → 29 Ja, vooral zorg/welzijn en medisch-administratief). Zie `mbo-tequalificeren.csv`, `mbo-ja.json`.
- **+10** particuliere HO + postacademisch (DUO ho_erkenningen_rio.csv gefilterd op NIET_BEKOSTIGD/AANGEWEZEN → Nyenrode, Wittenborg, Tyndale, GGZ VS, Thomas More, BV/BmS, NOB, RB Academy, Sioo, FB). Zie `ho-postac-ja.json`.
- **+10** laatste ronde uit CRKBO-midden (score 2, hard gefilterd op sterke sector + NOISE-uitsluiting coaching/therapie/spiritueel) + NRTO score 1-4. Twee randgevallen erbij (Kennisinstituut Complementaire Zorg, Vitacademie) — beide hebben een echte tweede beoordelaar/scriptie, gemarkeerd `[RANDGEVAL - check zelf]` in de Categorie-kolom.
- Twee dubbelen onderweg gevonden en genegeerd (SOMT, SRH Haarlem stonden al op de lijst onder andere rechtsvorm) en één dedupe-bug gefixt vóór toevoeging (Thomas More Hogeschool werd door het "Stichting"-prefix niet herkend als dubbel; nu bidirectionele matching i.p.v. prefix-only).
- **Restjes voor een volgende ronde:** publieke universiteiten met één los niet-bekostigd programma (Erasmus, VU, UvA, Leiden, Maastricht, Radboud, Twente) zijn NIET meegenomen (verkeerde ICP, ze zijn zelf bekostigd). CRKBO-midden (score 2, ~630 resterend na deze sessie) en NRTO 1-4 (~185 resterend) zijn nog grotendeels ongebruikt, maar leverden bij hard filteren maar een dunne, coaching/therapie-zware staart op — lage dichtheid, alleen doen als er weer een concreet volumedoel is.

De lijst is voor het eerst volledig gekwalificeerd: elke naam staat erop met een citaat.

Capabel en Tio zijn er op verzoek van Dante uitgehaald, daar loopt al contact.

## Af

| Bron | Omvang | Resultaat |
|---|---|---|
| NRTO-ledenlijst, mechanische voorsortering | 780 leden, 684 sites opgehaald | Score toegekend in `nrto-gescoord.csv` |
| NRTO score >= 15 en 8-14 | 88 leden | Gekwalificeerd, zit in `targetlijst-nl.csv` |
| NRTO middenmoot score 5 | 18 leden | 7 Ja, rest Nee met citaat |
| Particuliere HO-instellingen | circa 31 van de 56 | In de lijst |
| Close CRM check | - | Capabel, Tio en NCOI stonden er al in |
| NRTO middenmoot score 6-7 | 14 leden | 3 Ja, 6 Nee met citaat, 5 Onbekend (2026-07-22) |
| Freia Groep | 10 merken | 3 Ja (Freia zelf, AOG, NIVE), 3 Nee, 2 Onbekend, 1 overgeslagen, 1 opgegaan in AOG |
| Calder Holding | 7 NL-merken | TMO bijgewerkt naar Ja, Capabel stond er al, SBK Nee, SOMT overgeslagen |
| Certify360 EdTech Group (Lindenhaeghe) | 11 labels | Groep + NCI + WWZ op Ja, Lindenhaeghe zelf Nee, FOI/LearnCare/CS Onbekend |
| Eduro Groep | 4 merken | Intop Ja, Techniekschool/WTB Nee, T Gear open |
| Global University Systems | - | Geen NL-opleider, doorgegeven aan de UK-lijst |
| AcadeMedia NL | 1 | IVA Driebergen bijgewerkt naar Ja |
| Lemlist-export losse kandidaten | 4 | IVA Ja, AvdR Nee, Winc + Segment Onbekend |
| Particuliere HO-instellingen, de 11 bekende namen | 11 | Dirksen + BSN Ja, ISBW/NTI/Notenboom al gedaan, TIAS/HTF/SRH nu ook Ja, Pro Education open |
| Onbekend-bak, volledig doorgewerkt | 41 rijen | 14 naar Ja, 6 naar Nee, 15 van de lijst gehaald, 6 verwijderd (Capabel, Tio, Unknown UAS e.a.) |
| De vier private hogescholen | 4 | TNS, UE Amsterdam en Webster naar Ja; Unknown UAS eraf |

## Nog te doen, in volgorde van opbrengst

1. ~~**Restje opleidingsgroepen**~~ — **AF (2026-08-13).** DCG, Eduro/T Gear en CS Opleidingen gedaan. Enige restje: **Inspiring Generations-portfolio** vergt een KvK-uittreksel (concernrelaties), online niet vindbaar.
2. ~~**Losse kandidaten uit een Lemlist-export**~~ — **AF (2026-08-13).** Navitas/THPC = Ja.
3. ~~**De ontbrekende particuliere HO-instellingen**~~ — **AF (2026-08-13).** Hele DUO-lijst gefilterd; AvG en HTI Ja, Saba en IUA Onbekend, rest publiek/al gedaan.
4. ~~**De Salta-merken los verifieren**~~ — **AF (2026-08-13)**, dossier-niveau (geen losse CSV-rijen zolang de Salta-blokkade staat).
5. **NRTO middenmoot score 1-4** — blokken 1 t/m 6 gedaan (2026-08-13, ~115 namen), **~60 resterend** (vrijwel alleen score 1-2, namenlijst in dossiers onder "zesde blok"). Dichtheid ronde b: ~1 Ja op 10.
6. **CRKBO-register** — 4.771 instellingen, MECHANISCH GEKWALIFICEERD op 2026-07-22 (`crkbo-gescoord.csv`). 448 waren al gedaan, 93 harde + sector-ruis eruit, 3.339 ruis (score <= 0), 690 midden. De **201 schone kansrijke opleiders** (`crkbo-shortlist-hoog.csv`) zijn op **2026-08-05 volledig door de poort-0-workflow gehaald** (2 runs, samen alle 201 rijen; batch 9 en batch 10 vielen elk in 1 run weg op een verbindingsfout maar zijn door de andere run gedekt). Uitkomst: **13 Ja, ~132 Nee, ~44 Onbekend**. 12 schone Ja's toegevoegd aan `targetlijst-nl.csv` (met CRKBO als bron): 3Masters, Conducto, PostMDopleidingen, MKPC, Beldman, Breederzorg, De Broedplaats, Droomritme, ExpertCollege-Nightingale, NIPA/Zorgdidact, Land van Rouw, PPO. Scheidegger Opleidingen B.V. viel als Ja uit maar is NCOI/Salta → UITGESLOTEN. **Twee nog voor te leggen aan Dante:** AS-opleidingen B.V. (had hij eerder bewust laten vallen, workflow vond nu wel bewijs) en VONK cursussen/bedrijfsopleidingen (mogelijk publiek bekostigd groen onderwijs, particulier-status checken). De 44 Onbekend bevatten een aparte bel-lijst (Basic Trust, Bolwerk, De Roos, Forta, Hoogendijk, SAGHO e.a.): eigen langlopend traject bevestigd maar geen citaat over wie beoordeelt → bellen, niet zoeken. Gemergede resultaten in `crkbo-merged-final.json` (te bouwen) / `crkbo-workflow-resultaten.json` + task `wakl22wj0.output`. **Deze bak is AF.**
7. ~~**Postacademische restlijst**~~ — **gerichte namen AF (2026-08-13b)**: NSOB en Kyden erbij, mediation/accountancy-PE/vastgoed afgevallen met citaat. **Enige restpunt: de volledige CPION-register-enumeratie** (zie ronde-2026-08-13b-blok bovenaan; script/aanpak staat beschreven, uitkomst nog verwerken).

8. ~~**Particuliere rijkserkende mbo-opleiders**~~ — **AF (2026-08-13b)** via verse DUO RIO-trek; alleen het restblokje van 5 technieknamen staat nog open (zie ronde-blok bovenaan).

9. **Zorg-uitsluiting: beslist, blijft voorlopig staan (2026-08-12, zie decisions/log.md).** Inmiddels drie afvallers: SOMT University of Physiotherapy (NVAO-geaccrediteerde particuliere hogeschool, vier hbo-masters, dus masterscripties), ISPP en Synergos (post-hbo haptonomie, CPION). Dante bevestigde dat SOMT gewoon een prima lead blijft en er niets aan de uitsluiting hoeft te veranderen "voor nu". Niet meer als blokkerende beslissing behandelen, alleen nog als iets om later opnieuw te bekijken.
10b. **NIEUW - CPION-oogst kwalificeren (uit ronde 2026-08-13b).** Twee subgroepen, namen en ruwe data in `dossiers.md` (kop "CPION gerichte oogst") en `cpion-targeted-2026-08-13.json`:
   a. **Onderwijsadviesbureaus met post-hbo registeropleidingen** (Expertis, Bureau Meesterschap, ZIEN in de Klas, OnderwijsConnected, Helder Onderwijsadvies, Metis, Ceto, Steengoed, Slim! Educatief, Wizz, St. 1801, Bazalt, ATTC, Excellent, Melior, ECNO) - zelfde model als OMJS, waarschijnlijk hoge Ja-dichtheid.
   b. **Losse postinitiële instituten** (Coniche, Credit Management Instituut, DNV, DataExpert, Vestigo, IACA, SOBA, Harvest, PCO Kennis, Riskforum, AethiQs, WTW Academy, PHOE, PAO T&M, KOB-bouwfysica/bouwprocesmanagement-stichtingen, TVVL, evofenedex, Frijlande e.a.).
   Daarnaast staat de **volledige CPION-enumeratie** nog open als iemand hem opnieuw wil draaien (aanpak: substring-search recursief; duurde >2,5u en is afgebroken, gerichte oogst dekt de sterke domeinen al).

11. **UK-doorgeefpunt: Global University Systems.** Holding met statutaire zetel in Amsterdam, eigenaar van University of Law en Arden University, allebei bij naam genoemd in Jeroens ICP-document onder smaak 2. Hoort niet op de NL-lijst maar wel bovenaan de UK-lijst.

## Bak "onbekend"

32 rijen in `targetlijst-nl.csv` staan op Onbekend. Nieuw uit ronde b: Centrum voor Conflicthantering, STOC, Medivus, SocialLane/Dutch Marketing Academy, Synergos. Nieuw uit ronde c: Comenius Leergangen, Wagner & Company, Winc Academy, Segment Opleidingen, FOI, LearnCare Academy. Uit ronde e zijn HTF, TIAS, SRH, Winc en LearnCare omgezet naar Ja. **De bak is leeg.** Veertien opleiders zijn op 2026-07-22 op verzoek van Dante van de lijst gehaald omdat hun site de beoordelaar niet noemt en zoeken niets meer opleverde. Ze staan met reden in `dossiers.md`. **Komen ze terug, dan is de route bellen, niet zoeken.**

## Markt-groepen die je kunt overslaan

Staat in `icp.md` onder "Marktgroepen die je kunt negeren". Kort: normzetters en certificeerders, brancheorganisaties en koepels, uitgevers en platforms, exameninstituten die voor derden toetsen, VCA- en BHV-aanbieders, rijinstructeuropleidingen (IBKI), particulier vo, en zorg/psychologie/postmaster (bewust laten vallen).

## Zoek op de vorige naam (toegevoegd 2026-07-22, ronde g)

Private hogescholen worden vaak overgenomen en hernoemd, maar hun NVAO-rapport blijft onder de **oude** naam in het archief staan. UE Amsterdam was onvindbaar en stond binnen een minuut op tafel onder InterCollege Business School. Zelfde patroon: Notenboom (nu Business School Nederland), IVA (nu AcadeMedia), Emmius (opgegaan in AOG), Scheidegger (nu Salta).

**Geen NVAO-rapport te vinden? Zoek eerst de vorige naam.**

## De PDF-route (toegevoegd 2026-07-22, ronde e)

`WebFetch` faalt op PDF's: 403 of binaire rommel. Haal ze lokaal op en lees ze uit:

```
curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36" -o r.pdf "<url>"
python3 -c "import fitz; print('\n'.join(p.get_text() for p in fitz.open('r.pdf')))"
```

`pymupdf` (fitz) en `pypdf` staan lokaal. Werkt op NVAO-rapporten, OER's en examenreglementen van 40+ paginas. Faalt alleen op scans zonder tekstlaag.

**Bij NVAO-geaccrediteerde instellingen is dit de snelste route naar een citaat.** De rapporten bevatten bovendien de beste outreach-hooks: panels schrijven letterlijk op waar de beoordeling rammelt.

## Vaste stap voor je begint (toegevoegd 2026-07-22 na een dedupe-ronde)

Grep **elke** organisatienaam eerst tegen de lijst voordat je hem onderzoekt:
```
grep -i "naam" targetlijst-nl.csv dossiers.md
```
In ronde c zijn TMO, NCI en WWZ Academie gedupliceerd, in ronde e opnieuw Winc Academy en Intop Zorgsector. De regel geldt voor **elke** naam, ook als hij uit een moederlijst rolt. Check ook op genormaliseerde naam (lowercase, zonder leestekens): "Nive Opleidingen (HOFAM)" stond naast "NIVE Opleidingen" en glipte door een exacte-naam-check heen.

## AF: DUO-registers op omvang (2026-09-02, agent 1)

De DUO-lane is nu **op omvang** doorlopen, niet alleen op poort 0 zoals in ronde 2026-08-13b.

**Hoe je de juiste universe trekt (doe dit niet opnieuw fout):**
Filter op `BEKOSTIGINGSCODE` in `onderwijsinstellingserkenningen.csv`, **niet** op de `BEKOSTIGD`-vlag per licentie. ROC's houden ook niet-bekostigde licenties voor contractonderwijs en komen dan vals naar boven (Talland, Yonder, Firda, Scalda, Noorderpoort).
- niet-bekostigd mbo = `BEKOSTIGINGSCODE = ERKEND` → 202 instellingen, waarvan **96 met een actieve licentie**
- niet-bekostigd ho = `RECHTSPERSOON_HO` → 54 instellingen, waarvan **51 actief**
- plus `AANGEWEZEN` (9): Nyenrode, Nyenrode New Business School, Tias, tUL, Azusa, Europe Islamic UAS, HES Consultancy, CEDLA, Fontys Aangewezen Opleidingen

CKAN-API werkt: `https://onderwijsdata.duo.nl/api/3/action/package_show?id=rio_nfo_po_vo_vavo_mbo_ho`

**De harde conclusie over studentaantallen:** die zijn voor niet-bekostigde instellingen structureel **niet publiek**. Getest op circa 20 opleiders. DUO's studentenbestand bevat alleen de 55 bekostigde. SBB publiceert het niet per instelling. Het wettelijk verplichte *verslag van werkzaamheden* staat bij vrijwel iedereen alleen "op te vragen via e-mail". Eigen sites noemen zelden een getal.

**Daarom is de bruikbare omvangsmaat: het aantal van elkaar verschillende erkende opleidingen per instelling uit RIO.** Hard, uniform, voor alle 147 te berekenen, en het sluit aan op trap 2 van de cascade (elke opleiding is een eigen toolfee). Dat is deze ronde op alle gematchte organisaties weggeschreven als `aantal_opleidingen` met `omvang_niveau=afgeleid`.

**Nog open, als iemand echt lerendenaantallen wil:** het verslag van werkzaamheden per mail opvragen bij de top-10 (Maas College, GO-College, ORGB, BRAVE MINDS, CRAFT Education). Dat is de enige route naar een hard getal, en het is een mailtje per opleider.

**Niet meer doen:** DUO afzoeken op omvang. Deze ronde heeft alles opgeleverd wat er publiek in zit.

---

## Vlaanderen (nieuw, gestart 2026-09-02)

Nieuwe markt naast de NL-lijst. Alle Vlaamse rijen zijn te herkennen aan het woord
VLAANDEREN aan het begin van `notities`. Franstalig Belgie valt buiten scope.

**Stand: 59 organisaties weggeschreven.** 42 gekwalificeerd (poort 0 = Ja), 17 kandidaat.

### Af
- Syntra-netwerk (5 centra, alle vijf poort 0 = Ja)
- Vlaamse hogescholen (13, compleet)
- Vlaamse universiteiten (5, compleet)
- CVO's (16 van de 29 grootste; volledige lijst van 29 staat op
  onderwijskiezer.be/v2/volwassen/volw_secundair_instellingen2.php)
- Business schools (AMS, Vlerick)
- Particuliere instituten (Centrum voor Avondonderwijs / Afstandsonderwijs / Beroepskwalificatie)
- Sectorfondsen (Cevora, Educam, Volta, Constructiv, Alimento, Febelfin Academy)

### Open, in volgorde van opbrengst
1. **NCOI Learning Belgie**: grootste private opleider van Belgie (1.500 opleidingen,
   geaccrediteerde MBA). Poort 0 nog niet hard, geen openbaar examenreglement gevonden.
   Hoogste prioriteit om te verifieren.
2. **Studentenaantallen** voor AP, KdG, Erasmushogeschool, PXL, UGent, VUB, UHasselt.
   Bron: het PDF-rapport Oktobertelling 2025 van de Vlaamse Hogescholenraad, plus Dataloep.
3. **Instellingseigen OER-citaten** voor de hogescholen, universiteiten en CVO's. Nu staat
   daar het decreetkader als bewijs, met een expliciete LET OP in de notities. Alleen Howest,
   Syntra West, Syntra AB, Syntra Brussel, AMS, Centrum voor Avondonderwijs en Centrum voor
   Afstandsonderwijs hebben een instellingseigen citaat.
4. **Eigen examenreglement** van SyntraPXL en Syntra Midden-Vlaanderen (nu het gedeelde kader).
5. **Resterende 13 CVO's** uit de lijst van 29.
6. **Hogeronderwijsregister** (hogeronderwijsregister.be/instellingen) voor de private
   geregistreerde instellingen. Pagina laadt dynamisch, WebFetch krijgt hem niet; via browser.
7. **Opleidingsdatabank** van de Vlaamse overheid (register opleidingscheques en Vlaams
   Opleidingsverlof). Beheerd door VDAB. Nog niet ontsloten, geen open API gevonden.

### Structuurcorrecties die tijd besparen
- **Graduaatsopleidingen zitten sinds 2019-2020 bij de HOGESCHOLEN, niet bij de CVO's.**
  De hypothese dat CVO's de graduaten hebben klopt niet meer.
- **Escala, SBM en Portilog zijn merken van Groep Syntra West** (koepel Skilliant), geen
  eigen ingangen. Benader via Syntra West.
- **EHSAL Management School is per januari 2026 opgegaan in Odisee.** emsbrussel.be
  redirect naar odisee.be. Geen aparte ingang meer.
- **Syntra Limburg heet SyntraPXL** (samenwerking met Hogeschool PXL). Hogeschool PXL is
  een aparte organisatie.
- **Solvay is Franstalig** (ULB) en valt buiten scope.
