# Adoptie, dealwaarde en de gewogen pipeline

_Onderzoek 26-09-2026 met `/deep-research`, stand standaard: vijf agents plus één in de gatenronde. Aanleiding: Dante wil een kloppend cijfer voor de gewogen pipeline in Close._

## De vraag

Eerst: welk adoptiepercentage hoort er op "alle studenten x prijs", want 100% adoptie is onrealistisch. Daarna verscherpt door Dante (26-09-2026): **hoe krijgen we een accuraat cijfer in Close voor de gewogen pipeline?**

Gegeven:
- Deals starten met een klein aantal studenten dat de klant zelf kiest, en rollen daarna gefaseerd uit.
- Er is nog geen gebruiksdata. Tot nu toe alleen pilots van maximaal 300 studenten, tegen pilotbedragen.

## Het antwoord

- **Een adoptiepercentage is niet de knop.** De gewogen pipeline gaat op twee plekken mis: de waarde is de potentie bij volledige uitrol, en de kans wordt per deal op gevoel ingevuld. Stand 26-09-2026: 18 actieve deals, €2,06M ongewogen, €510k gewogen. Zes deals van €200k of meer leveren 86% van het gewogen cijfer, UTI alleen al 49%.
- **Waarde = het eerste contract.** Elke echte offerte of pilot tot nu toe lag tussen €3k en €20k, op 175 tot 500 studenten. Tot er een prijsvoorstel ligt geldt een startwaarde van 500 studenten x 36 = €18.000, daarna het voorstel zelf.
- **Kans = vast per fase.** Een gemeten kanstabel per fase bestaat publiek niet, voor geen enkele sector. Wel twee ankers: van gekwalificeerd naar gewonnen haalt 20-25% bij deals van €10-50k, van offerte naar gewonnen gemiddeld 47%. Daarop een oplopende tabel die elk kwartaal gekalibreerd wordt op wat echt sloot.
- **Uitbreiding is een eigen opportunity, potentie een eigen veld.** Wat na het eerste contract komt hangt aan adoptie, en die is in het hoger onderwijs traag en onzeker. Dus niet vooraf meetellen.
- **Met deze regels komt de gewogen pipeline op ongeveer €60k in plaats van €510k.** Dat is het echte getal: wat de huidige deals in hun eerste contractjaar waarschijnlijk opleveren.

## Voorstel voor Close

### 1. De waarde

| Situatie | Waarde in Close |
|---|---|
| Nog geen prijsvoorstel (Qualified, Discovery) | 500 studenten x 36 = €18.000, of alle studenten x 36 als het er minder zijn |
| Prijsvoorstel ligt er (de gate uit Scoping vraagt er een) | het bedrag van dat voorstel: studenten in de eerste fase x 36 |
| Contract getekend | het contractbedrag |

- Altijd **per jaar** (value period `annual`) en altijd het eerste contractjaar. Geen totale looptijd, geen potentie.
- Waarom 500: de offertes die er zijn zaten op 175 studenten (Rotterdam), 60 tot 500 (Business School Nederland) en minimaal 500 (Academica), de pilots op maximaal 300. Na tien gewonnen deals vervangen door ons eigen gemiddelde.
- Alle studenten x 36 gaat naar een apart veld, **Potentie volledige uitrol**. Nuttig om te prioriteren en voor het verhaal naar investeerders, niet voor de forecast. Dat sluit aan bij `GTM/ICP/market-sizing-international/README.md`, dat hetzelfde bedrag al "prijskaartje bij volledige penetratie" noemde.

### 2. De kans per fase

| Fase in Close | Kans | Waar het op rust |
|---|---|---|
| Qualified | 10% | vóór discovery, dus onder het gekwalificeerde anker |
| Discovery | 15% | tussenwaarde |
| Scoping | 20% | gekwalificeerd naar gewonnen: 20-25% bij deals van €10-50k (Winning by Design, Optifai) |
| EB meeting | 30% | tussenwaarde |
| Pilot | 40% | geen cijfer voor het hoger onderwijs vindbaar; Bath Spa ging na de pilot verloren |
| Contracting | 60% | offerte naar gewonnen: gemiddeld 47% (RAIN Group), hier plus EB-commitment uit de gate |

- **Het oordeel zit in de fase, niet in het percentage.** Twijfel over een deal betekent dat hij in een eerdere fase hoort. De gates staan al in `GTM/Knowledge/meddpicc-states-and-gates.md`. Voorbeeld: Rotterdam staat op 85% in Contracting terwijl het beslisproces volgens de eigen note onbekend is. Volgens de gate hoort hij daar nog niet.
- Het zijn **startwaarden, geen meting.** Elk kwartaal per fase tellen hoeveel deals er sindsdien gewonnen of verloren zijn, en de tabel bijstellen zodra een fase er tien heeft.
- **De commit-forecast blijft apart.** De regel uit het handboek geldt nog steeds: alleen deals met bevestigde business case, EB-commitment en een afgesproken tekendatum. De gewogen pipeline is breder en ruwer.

### 3. Uitbreiding

- Na go-live een nieuwe opportunity per uitbreidingsstap ("[Instelling], uitbreiding [faculteit of jaar 2]"), met een eigen waarde (extra studenten x 36) en een eigen kans.
- Nooit uitbreiding vooraf in de waarde van het eerste contract.

### 4. Hygiëne die het cijfer ook scheeftrekt

- **Een closedatum op elke deal.** Nu ontbreekt die bij 9 van de 18, en Windesheim staat op 22-09-2026, al voorbij. Reken in het hoger onderwijs op 6 tot 18 maanden van eerste contact tot handtekening.
- **Deals zonder klantcontact eruit.** Radboud staat op Pilot terwijl er volgens de eigen CRM-note nooit contact is geweest.
- **Value period gelijktrekken.** Nu staan zeven deals op `one_time` en elf op `annual`.

## Rekenvoorbeeld

Deals die al op €20k of minder staan houden hun waarde, want die zitten al op offerte- of pilotniveau. De rest krijgt de startwaarde. Kans volgens de tabel hierboven. Het is een illustratie van de regels, geen herziene forecast: bij UTI hoort in Scoping al een eerste scope bekend te zijn, en die kan groter zijn dan 500.

| Deal | Fase | Nu gewogen | Voorstel |
|---|---|---:|---:|
| UTI | Scoping | 250.000 | 18.000 x 20% = 3.600 |
| BPP | Qualified | 40.000 | 18.000 x 10% = 1.800 |
| RUG | Discovery | 60.000 | 18.000 x 15% = 2.700 |
| UADE | Qualified | 50.000 | 18.000 x 10% = 1.800 |
| Windesheim | Discovery | 20.000 | 18.000 x 15% = 2.700 |
| Bristol | Qualified | 20.000 | 18.000 x 10% = 1.800 |
| Goldsmiths | Qualified | 18.000 | 18.000 x 10% = 1.800 |
| Tilburg | Pilot | 3.000 | 20.000 x 40% = 8.000 |
| Haagse Hogeschool | Contracting | 10.000 | 20.000 x 60% = 12.000 |
| Breederode | Discovery | 14.000 | 20.000 x 15% = 3.000 |
| Radboud | Pilot | 2.250 | 15.000 x 40% = 6.000 |
| UMCG | Pilot | 7.500 | 15.000 x 40% = 6.000 |
| Academica | Discovery | 1.260 | 12.600 x 15% = 1.890 |
| Rotterdam UAS | Contracting | 8.500 | 10.000 x 60% = 6.000 |
| CMI | Qualified | 1.000 | 10.000 x 10% = 1.000 |
| Notenboom | Scoping | 2.000 | 10.000 x 20% = 2.000 |
| HBMSU | Qualified | 1.000 | 10.000 x 10% = 1.000 |
| Noordhoff | Qualified | 1.000 | 10.000 x 10% = 1.000 |
| **Totaal** | | **509.510** | **64.090** |

Zonder Radboud: 58.090. De potentie bij volledige uitrol blijft zichtbaar in het aparte veld.

## Wat de adoptiecijfers zeggen

Voor het eerste contract is een adoptiepercentage niet nodig: de klant kiest zelf de groep, en kiest daarbij de docenten die willen. Voor uitbreiding en verlenging telt adoptie wel.

**Hoeveel ingekochte software gebruikt wordt**
- Algemene B2B SaaS: 54% van de licenties gebruikt in 2025, 47% in 2024 (Zylo 2026). Andere leveranciers noemen 25 tot 53% ongebruikt. Allemaal eigen klantdata van leveranciers die licentiebeheer verkopen, zonder gepubliceerde definitie van "gebruikt".
- K-12 edtech in de VS: mediaan 30% van de licenties gebruikt, 97,6% nooit intensief (Baker/BrightBytes, 2018). 67% ongebruikt volgens Glimpse K12 (2019, leverancier).
- Hoger onderwijs: licentiebenutting is nergens gemeten, in het VK niet, in NL niet en in de VS niet.

**Hoe ver instellingsbrede tools komen in het Britse hoger onderwijs** (UCISA 2024, 57-58 instellingen)
- VLE en tekst-matching (Turnitin): bij 93-98% van de instellingen gebruikt in meer dan de helft van de cursussen.
- E-assessment, formatief en summatief: bij 98% centraal aangeboden, maar bij 60-62% gebruikt in meer dan de helft van de cursussen. Dat plafond staat er al acht jaar.
- Lecture capture: bij 89% aangeboden, bij 76% gebruikt in meer dan de helft van de cursussen, sterk aangejaagd door covid.
- UCISA zelf: *"high levels of central provision does not generally equate to high levels of use except for VLEs and Text matching tools."*
- Een Gradescope-uitrol bij één Amerikaans technisch instituut groeide vooral onder covid-dwang, en viel deels terug toen die wegviel (ASEE-paper, data tot en met 2021-22).

**AI bij nakijken specifiek**
- Ongeveer 15% van de docenten gebruikt AI om feedback op studentwerk te maken: 61% gebruikt AI, van hen 24% voor feedback (Digital Education Council 2025, 1.681 docenten in 28 landen; het product van die twee is zelf berekend).
- Maar 46% staat positief tegenover AI bij beoordelen en feedback, de laagste score van negen toepassingen (zelfde bron).
- Van de Amerikaanse docenten die AI gebruiken, gebruikt ongeveer een op de tien de AI die in het LMS of de courseware zit. De rest pakt losse tools als ChatGPT (Tyton Partners 2025).

**Waar adoptie op afgewogen wordt: is het de moeilijkheid?**
- Nee. Nut weegt ongeveer 2,7 keer zo zwaar als gebruiksgemak: padcoëfficiënt .505 tegen .186 in een meta-analyse van 88 TAM-studies (King & He 2006). Gebruiksgemak werkt vooral via nut: een makkelijke tool wordt nuttiger gevonden.
- Standaard-aan (opt-out) verhoogt de keuze voor een optie met gemiddeld 27 procentpunt (meta-analyse van 58 studies, Jachimowicz e.a. 2019). Dat komt door "dit wordt aanbevolen" en "dit is de norm", niet door gemak.
- Of gebruik verplicht of vrijwillig is, verandert hoe zwaar nut en gemak wegen (Wu & Lederer 2009, alleen het abstract kon gelezen worden).
- Integratie in het LMS verhoogt de tevredenheid, maar niet vanzelf het gebruik: ingebouwde AI scoort een NPS van 27 tegen 2 zonder, en toch gebruikt maar een op de tien docenten hem (Tyton 2025).

**Wat dat betekent voor de pipeline**
- Eerste contract: geen correctie nodig. De klant kiest zelf de groep.
- Uitbreiding: traag en onzeker. Zelfs gevestigde e-assessment blijft in het VK steken op 60% van de instellingen. Daarom apart boeken, en pas zodra het eerste cohort het echt gebruikt.
- Verlenging: ook bij volwassen edtech groeit de omzet binnen bestaande klanten langzaam. PowerSchool haalde in 2023 een net revenue retention van 106,7%, dus netto 6,7% groei per jaar binnen bestaande klanten (10-K; K-12 schoolsoftware, dus een indirecte vergelijking).
- De aanname "jaar 1 = 30% adoptie" in de Windesheim- en RUG-analyses heeft geen bron. Dit onderzoek levert er ook geen: er bestaat geen gemeten jaar-1-cijfer voor AI-nakijken in het hoger onderwijs.

## Tegenspraak en weging

- **Dealgrootte tegenover win rate.** Optifai (939 SaaS-bedrijven, 2025-26) ziet de win rate dalen naarmate deals groter worden, Winning by Design (868 bedrijven, 2016-22) ziet hem stijgen. Op €10-50k komen beide uit op 20-25%. Ik gebruik alleen dat punt, niet de trend.
- **Integratie en gebruik.** UCISA ziet VLE en Turnitin bijna overal gebruikt, Tyton ziet ingebouwde AI nauwelijks gebruikt. Verschillende categorieën, geen echte tegenspraak. Voor Eduface: integratie is een voorwaarde, geen garantie.
- **Pilot naar contract.** Generieke betaalde pilots zouden 60-90% converteren (SaaStr, ongedateerd en vermoedelijk van rond 2011), tegenover K-12-pilots die zelden doorzetten door inkoopregels, budget en wisselende beslissers (Education Intel, 2026). Ik weeg de onderwijscontext en onze eigen Bath Spa zwaarder: 40%.
- **Licentiebenutting.** Leveranciers spreken elkaar en zichzelf tegen: Zylo noemt in hetzelfde rapport 54% gebruikt en 36% onbenut. Alleen bruikbaar als ordegrootte.

## Gaten

- **Geen gemeten kans per fase**, voor geen enkele sector. De tabel is een verdedigbaar startpunt, geen meting. Hij wordt pas goed met eigen data.
- **Geen cijfer voor pilot naar contract in het hoger onderwijs.** Gezocht, niet publiek vindbaar.
- **Geen eigen historie.** Close telt 0 gewonnen en 8 verloren deals.
- **De omvang van een eerste contract bij een grote universiteit is onbekend.** Geen enkele grote universiteit kwam bij ons tot een prijsvoorstel. Graide noemt £150-250k voor een volledige universiteitslicentie, met afdelingsprijzen op aanvraag, maar dat is het eindplaatje.
- **Geen gebruiksdata van Eduface zelf.** Zodra er klanten live zijn: per klant docenten uitgenodigd tegenover actief, en studenten met minstens één beoordeling via Eduface.

## Bronnen

**Intern**
- Close, actieve en verloren opportunities, opgehaald 26-09-2026.
- `GTM/Knowledge/meddpicc-states-and-gates.md` (gates per fase en de forecastregel).
- `GTM/Accounts/windesheim/financiele-analyse.md` en `GTM/Accounts/rug-groningen/dossier-cost-justification-en-datalek.md` (de 30%-aanname).

**Primair**
- UCISA, Digital Education Survey Report 2024: https://www.ucisa.ac.uk/-/media/2024-Digital-Education-Survey-Report.pdf (2024)
- UCISA, TEL Survey 2016: https://www.ucisa.ac.uk/-/media/Files/UCISA/Publication-files/Surveys/TEL-surveys/TEL-Survey-2016_PDF-only.pdf (2016)
- Digital Education Council, Global AI Faculty Survey 2025: https://cdn.prod.website-files.com/65f1d299b87bcc50550a6398/678a9e0aa38a44fdac1d53a8_Digital%20Education%20Council%20Global%20AI%20Faculty%20Survey%202025-1.pdf (2025; ledenorganisatie met partnerships met onder meer Instructure)
- Tyton Partners, Time for Class 2025: https://4213961.fs1.hubspotusercontent-na1.net/hubfs/4213961/Publications/Time%20for%20Class/Tyton%20Partners_Time%20for%20Class%202025.pdf (2025; mede gefinancierd door edtech-partners, de editie van 2024 door Turnitin)
- PowerSchool Holdings, 10-K over 2023 (NRR 106,7%): https://www.sec.gov/Archives/edgar/data/1835681/000183568124000016/pwsc-20231231.htm (2024)
- PowerSchool Holdings, S-1 (salescyclus 3 tot 18 maanden): https://www.sec.gov/Archives/edgar/data/1835681/000119312521107673/d24413ds1.htm (2021)
- Ebsta x Pavilion, B2B Sales Benchmarks 2024: https://www.ebsta.com/wp-content/uploads/2024/02/B2B-Sales-Benchmarks-2024_.pdf (2024; verkoopt zelf pipelinesoftware)
- InsightSquared, State of Sales Forecasting (47% sluit op de voorspelde datum): https://www.insightsquared.com/blog/2021-state-of-sales-forecasting-press-release/ (2021; verkoopt zelf forecastsoftware)
- Sales Management Association met Vantage Point, forecastnauwkeurigheid: https://salesmanagement.org/blog/6-skills-necessary-to-take-charge-of-sales-forecasting-accuracy/ (2015)
- Find a Tender, Coventry University en Turnitin (£69.673 per jaar): https://www.find-tender.service.gov.uk/Notice/045815-2025 (2025)
- Find a Tender, De Montfort University en Studiosity (£1,2M over bijna vijf jaar, geen jaarbedrag): https://www.find-tender.service.gov.uk/Notice/050801-2025 (2025)
- Jisc, banding methodology (telt inkomen, geen FTE): https://subscriptionsmanager.jisc.ac.uk/about/banding-methodology (2024)

**Secundair**
- King & He, meta-analyse van 88 TAM-studies: https://doi.org/10.1016/j.im.2006.05.003 (2006)
- Jachimowicz, Duncan, Weber & Johnson, meta-analyse van defaults: https://doi.org/10.1017/bpp.2018.43 (2019)
- Wu & Lederer, meta-analyse over vrijwillig gebruik: https://misq.umn.edu/a-meta-analysis-of-the-role-of-environment-based-voluntariness-in-information-technology-acceptance.html (2009)
- Ibrahim, Howarth & Stone, lecture capture-beleid in Britse universiteiten: https://link.springer.com/article/10.1007/s42438-020-00102-x (2020)
- ASEE, Case Study: Encouraging Faculty Adoption of New Grading Software: https://peer.asee.org/case-study-encouraging-faculty-adoption-of-new-grading-software.pdf (data tot en met 2021-22)
- Penn GSE over Baker/BrightBytes, gebruik van ingekochte apps: https://www.gse.upenn.edu/news/schools-aren%E2%80%99t-using-apps-they-are-paying-study-finds (2018)
- The Markup, Turnitin-kosten per student in Californië: https://themarkup.org/artificial-intelligence/2025/06/26/plagiarism-detector-costs-california (2025, data 2021-22)

**Tertiair**
- Winning by Design, The Bowtie (win rate per dealgrootte): https://winningbydesign.com/wp-content/uploads/2026/02/The-Bowtie-A-Proposed-Standard.pdf (2026, data 2016-22; verkoopt eigen trainingen)
- Optifai, win rate per dealgrootte: https://optif.ai/learn/questions/b2b-saas-win-rate-by-deal-size/ (data 2025-26; verkoopt pipelinesoftware)
- RAIN Group, gemiddelde win rate op offertes: https://www.rainsalestraining.com/blog/average-sales-win-rates-how-do-you-compare (jaar van meting onbekend; salestrainingsbureau)
- SaaStr, conversie van betaalde pilots: https://www.saastr.com/what-is-the-typical-conversion-from-paid-pilot-to-annual-contract-in-b2b-saas/ (ongedateerd)
- Education Intel, waarom edtech-pilots zelden districtscontracten worden: https://educationintel.substack.com/p/why-edtech-pilots-rarely-become-district (2026)
- Zylo, SaaS-statistieken 2026: https://zylo.com/blog/saas-statistics (2026; verkoopt licentiebeheer)
- Glimpse K12, persbericht ongebruikte licenties: https://www.globenewswire.com/news-release/2019/05/15/1825260/0/en/Glimpse-K12-Analysis-of-School-Spending-Shows-that-Two-Thirds-of-Software-License-Purchases-Go-Unused.html (2019; verkoopt licentiemonitoring)
- Graide, prijspagina: https://www.graide.co.uk/pricing (bezocht 26-09-2026)
- Cadmus, prijspagina met pilot, pay-per-user en enterprise: https://cadmus.io/pricing/ (bezocht 26-09-2026)
