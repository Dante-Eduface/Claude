# Adoptie, dealwaarde en de gewogen pipeline

_Onderzoek 26-09-2026 met `/deep-research`, stand standaard: vijf agents plus één in de gatenronde, samen ~1,6M tokens (de skill schat standaard op 300-500k). Aanleiding: Dante wil een kloppend cijfer voor de gewogen pipeline in Close._

## De vraag

Eerst: welk adoptiepercentage hoort er op "alle studenten x prijs", want 100% adoptie is onrealistisch. Daarna verscherpt door Dante (26-09-2026): **hoe krijgen we een accuraat cijfer in Close voor de gewogen pipeline?**

Gegeven:
- Deals starten met een klein aantal studenten dat de klant zelf kiest, en rollen daarna gefaseerd uit.
- Er is nog geen gebruiksdata. Tot nu toe alleen pilots van maximaal 300 studenten, tegen pilotbedragen.

## Het antwoord

- **Een adoptiepercentage is niet de knop.** De gewogen pipeline gaat op twee plekken mis: de waarde is de potentie bij volledige uitrol, en de kans wordt per deal op gevoel ingevuld. Stand 26-09-2026: 18 actieve deals, €2,06M ongewogen, €510k gewogen. Zes deals van €200k of meer leveren 86% van het gewogen cijfer, UTI alleen al 49%.
- **Waarde = het eerste contract.** Elke echte offerte of pilot tot nu toe lag tussen €3k en €20k, op 175 tot 500 studenten. Tot er een prijsvoorstel ligt geldt een startwaarde van 500 studenten x 36 = €18.000, daarna het voorstel zelf.
- **Kans = vast per fase.** Een gemeten kanstabel per fase bestaat publiek niet, voor geen enkele sector. Wel twee ankers: van gekwalificeerd naar gewonnen haalt 20-25% bij deals van €10-50k, van offerte naar gewonnen gemiddeld 47%. Daarop een oplopende tabel die elk kwartaal gekalibreerd wordt op wat echt sloot.
- **Adoptie telt pas bij uitbreiding en verlenging, dus die boek je apart.** Er is geen instelling gevonden die AI-nakijken verplicht of standaard aanzet, dus uitbreiding gaat vrijwillig en traag. En bij rond 10% gebruik zeggen instellingen op bij de verlenging (Duke 2025, Colorado State 2026).
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
- Alle studenten x 36 gaat naar een apart veld, **Potentie volledige uitrol**. Nuttig om te prioriteren en voor het verhaal naar investeerders, niet voor de forecast. `GTM/ICP/market-sizing-international/README.md` noemde hetzelfde bedrag al "prijskaartje bij volledige penetratie".
- **Wat de eerste scope bepaalt bij AI-nakijken.** Vier vragen die per instelling verschillen en de scope kleiner kunnen maken dan de klant wil:
  1. Staat het beleid AI-ondersteund summatief beoordelen toe, of alleen formatief?
  2. Op welke grondslag mag studentwerk verwerkt worden: expliciete toestemming van de student, of een andere grondslag?
  3. Moet de vakbond of de medezeggenschap instemmen?
  4. Staat Eduface op de lijst van goedgekeurde tools?

### 2. De kans per fase

| Fase in Close | Kans | Waar het op rust |
|---|---|---|
| Qualified | 10% | vóór discovery, dus onder het gekwalificeerde anker |
| Discovery | 15% | tussenwaarde |
| Scoping | 20% | gekwalificeerd naar gewonnen: 20-25% bij deals van €10-50k (Winning by Design, Optifai) |
| EB meeting | 30% | tussenwaarde |
| Pilot | 40% | geen cijfer voor het hoger onderwijs vindbaar; Bath Spa ging na de pilot verloren op instellingsgereedheid, en Jisc noemt summatief gebruik van AI-nakijken "a long way off" |
| Contracting | 60% | offerte naar gewonnen: gemiddeld 47% (RAIN Group), hier plus EB-commitment uit de gate |

- **Het oordeel zit in de fase, niet in het percentage.** Twijfel over een deal betekent dat hij in een eerdere fase hoort. De gates staan al in `GTM/Knowledge/meddpicc-states-and-gates.md`. Voorbeeld: Rotterdam staat op 85% in Contracting terwijl het beslisproces volgens de eigen note onbekend is. Volgens de gate hoort hij daar nog niet.
- Het zijn **startwaarden, geen meting.** Elk kwartaal per fase tellen hoeveel deals er sindsdien gewonnen of verloren zijn, en de tabel bijstellen zodra een fase er tien heeft.
- **De commit-forecast blijft apart.** De regel uit het handboek geldt nog steeds: alleen deals met bevestigde business case, EB-commitment en een afgesproken tekendatum. De gewogen pipeline is breder en ruwer.

### 3. Uitbreiding en verlenging

- Na go-live een nieuwe opportunity per uitbreidingsstap ("[Instelling], uitbreiding [faculteit of jaar 2]"), met een eigen waarde (extra studenten x 36) en een eigen kans.
- Nooit uitbreiding vooraf in de waarde van het eerste contract.
- Zodra er klanten zijn: **verlenging als eigen opportunity**, ruim voor de einddatum, met een kans die op gebruik leunt. Spreek de gebruiksmeting vóór de start af met de klant: docenten actief tegenover uitgenodigd, en studenten met minstens één beoordeling via Eduface.

### 4. Hygiëne die het cijfer ook scheeftrekt

- **Een closedatum op elke deal.** Nu ontbreekt die bij 9 van de 18, en Windesheim staat op 22-09-2026, al voorbij. Reken in het hoger onderwijs op 6 tot 18 maanden van eerste contact tot handtekening. Governance-stappen rond AI (DPIA, toestemming van studenten, vakbond of medezeggenschap) maken dat eerder langer dan korter.
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

**Adoptie is een beleidskeuze**
- Opt-in haalt zelden meer dan 10-15% (Manchester, Senate-stuk uit 2013). Na de overstap op opt-out daalde het aandeel opt-outs voor lecture capture in Manchester van 36% (2013/14) naar 6% (2023/24). In Sheffield werd 60% van het onderwijs opgenomen in 2017-18 en 89% in 2022-23 (bron is leverancier Echo360). Dat kostte vijf tot tien jaar.
- Verplicht tegenover eigen keuze, onder 1.704 UCU-leden (2024): de LMS gebruikt 81,7% omdat het moet en 35,6% uit eigen keuze. Losse nakijksystemen: 14,5% verplicht, 4,8% uit eigen keuze.
- De voorwaarde bij Manchester: standaard aan zonder extra werk voor de docent, *"no buttons to press"*.

**AI-nakijken is de uitzondering**
- Tussen 2023 en 2026 is geen instelling gevonden die AI-ondersteund nakijken verplicht of standaard aanzet. Waar het mag, is het vrijwillig: LSE en KCL zijn neutraal, bij de HvA is "niemand verplicht".
- Vaak moet de student toestemming geven of zich kunnen afmelden (LSE, KCL, De Haagse Hogeschool, de Jisc-pilots). Vakbonden eisen opt-out of overleg vooraf (UCU 2026, AAUP 2025). Examinatoren of een vakgroep kunnen het helemaal blokkeren (Cambridge, de vakgroep geschiedenis van Northwestern in 2026).
- In de Britse pilots blijft het bij formatief werk. Jisc noemt summatief gebruik *"a long way off"* (Times Higher Education, 2026).
- Houding: 71% van 1.057 Amerikaanse docenten noemt essays nakijken met AI "cheat" (Elon/AAC&U 2025). Ongeveer 10% vertrouwt AI bij nakijken (Ulster, drie metingen 2024-2026, preprint).
- Gebruik: ongeveer 15% van de docenten maakt al feedback op studentwerk met AI (61% gebruikt AI, van hen 24% voor feedback; Digital Education Council 2025, 1.681 docenten, het product is zelf berekend). Maar 46% staat positief tegenover AI bij beoordelen, de laagste score van negen toepassingen. Van de Amerikaanse docenten die AI gebruiken, gebruikt ongeveer een op de tien de AI die in het LMS of de courseware zit (Tyton Partners 2025).
- De tegenkant: er is geen sectorbreed verbod. Een model waarin de docent elk voorstel goedkeurt is expliciet toegestaan: Birmingham, LSE en KCL, Ofqual voor gereguleerde kwalificaties, en in Nederland via de examinator uit de WHW. Dat is het model van Eduface.

**Waar adoptie op afgewogen wordt: is het de moeilijkheid?**
- Nee. Nut weegt ongeveer 2,7 keer zo zwaar als gebruiksgemak: padcoëfficiënt .505 tegen .186 in een meta-analyse van 88 TAM-studies (King & He 2006). Gebruiksgemak werkt vooral via nut: een makkelijke tool wordt nuttiger gevonden.
- Standaard-aan (opt-out) verhoogt de keuze voor een optie met gemiddeld 27 procentpunt (meta-analyse van 58 studies, Jachimowicz e.a. 2019). Dat komt door "dit wordt aanbevolen" en "dit is de norm", niet door gemak.
- Of gebruik verplicht of vrijwillig is, verandert hoe zwaar nut en gemak wegen (Wu & Lederer 2009, alleen het abstract kon gelezen worden).
- Integratie in het LMS verhoogt de tevredenheid, maar niet vanzelf het gebruik: ingebouwde AI scoort een NPS van 27 tegen 2 zonder, en toch gebruikt maar een op de tien docenten hem (Tyton 2025).

**Verlenging: daar gaat het geld verloren**
- Instellingsbrede licenties met rond 10% gebruik worden opgezegd: Duke stopte in 2025 met LinkedIn Learning (10% gebruik), Colorado State in 2026 (minder dan 11%).
- Ook LMS-geïntegreerde feedbacktools: Delaware zegt FeedbackFruits op per juni 2026 (*"overall adoption has been limited"*), VIU in Canada Studiosity (*"usage not sufficient"*).
- Zelfs de grote LMS-leveranciers verliezen bruto 5 tot 8% van hun terugkerende omzet per jaar: gross revenue retention Instructure 93% (2023), D2L 92,1% (boekjaar 2026). De netto groei binnen bestaande klanten is klein: net revenue retention Instructure 103% (2023), D2L 100,9% (boekjaar 2026), PowerSchool 106,7% (2023).
- Nuance: maar 46% van de instellingen meet de ROI van edtech (EDUCAUSE QuickPoll 2025, 124 respondenten). Opzeggen op gebruik gaat dus niet automatisch.

**Wat dat betekent voor de pipeline**
- Eerste contract: geen correctie nodig. De klant kiest zelf de groep, en daarin zitten de docenten die willen.
- Uitbreiding: vrijwillig, dus traag. Apart boeken, pas zodra het eerste cohort het echt gebruikt.
- Verlenging: het grootste geldrisico zit hier, niet bij het tekenen. Gebruik meten vanaf dag één.
- De aanname "jaar 1 = 30% adoptie" in de Windesheim- en RUG-analyses heeft geen bron, en dit onderzoek levert er ook geen: er bestaat geen gemeten jaar-1-cijfer voor AI-nakijken in het hoger onderwijs. Een vast percentage is bovendien aan beide kanten fout, want de spreiding per instelling loopt van verboden (Cambridge-examinatoren) tot toegestaan met docentreview (Birmingham).

## Tegenspraak en weging

- **Dealgrootte tegenover win rate.** Optifai (939 SaaS-bedrijven, 2025-26) ziet de win rate dalen naarmate deals groter worden, Winning by Design (868 bedrijven, 2016-22) ziet hem stijgen. Op €10-50k komen beide uit op 20-25%. Ik gebruik alleen dat punt, niet de trend.
- **Integratie en gebruik.** UCISA ziet VLE en Turnitin bijna overal gebruikt, Tyton ziet ingebouwde AI nauwelijks gebruikt. Verschillende categorieën, geen echte tegenspraak. Voor Eduface: integratie is een voorwaarde, geen garantie.
- **Pilot naar contract.** Generieke betaalde pilots zouden 60-90% converteren (SaaStr, ongedateerd en vermoedelijk van rond 2011), tegenover K-12-pilots die zelden doorzetten door inkoopregels, budget en wisselende beslissers (Education Intel, 2026). Ik weeg de onderwijscontext, de AI-governance en onze eigen Bath Spa zwaarder: 40%.
- **Licentiebenutting.** Leveranciers spreken elkaar en zichzelf tegen: Zylo noemt in hetzelfde rapport 54% gebruikt en 36% onbenut. Alleen bruikbaar als ordegrootte.
- **Verbieden of toestaan binnen dezelfde groep.** Cambridge verbiedt examinatoren om studentwerk in GenAI te zetten, terwijl Birmingham, LSE en KCL het onder voorwaarden toestaan, allemaal Russell Group. Bij Northwestern verkent de provost AI-nakijken terwijl de vakgroep geschiedenis het verbiedt. Weging: het beleid van de instelling, soms van de faculteit, beslist. Per deal uitvragen.
- **Nederland.** Het ministerie staat AI-nakijken met een mens in de lus toe (NOS, 6-4-2026, over het voortgezet onderwijs). De HvA en De Haagse Hogeschool noemden GenAI in 2024 geen valide of toereikend beoordelingsinstrument. De regels van de instelling wegen zwaarder dan de landelijke lijn.
- **Opzeggen op gebruik.** Duke en Colorado State zeiden op na een gebruiksanalyse, terwijl maar 46% van de instellingen de ROI meet. Opzeggen op gebruik is dus geen automatisme, maar bij rond 10% gebruik gebeurt het wel.

## Gaten

- **Geen gemeten kans per fase**, voor geen enkele sector. De tabel is een verdedigbaar startpunt, geen meting. Hij wordt pas goed met eigen data.
- **Geen cijfer voor pilot naar contract in het hoger onderwijs.** Gezocht, niet publiek vindbaar.
- **Geen eigen historie.** Close telt 0 gewonnen en 8 verloren deals.
- **De omvang van een eerste contract bij een grote universiteit is onbekend.** Geen enkele grote universiteit kwam bij ons tot een prijsvoorstel. Graide noemt £150-250k voor een volledige universiteitslicentie, met afdelingsprijzen op aanvraag, maar dat is het eindplaatje.
- **Geen gebruiksdata van Eduface zelf.** Zodra er klanten live zijn: per klant docenten uitgenodigd tegenover actief, en studenten met minstens één beoordeling via Eduface.
- **Geen instelling die AI-nakijken verplicht of standaard aanzet, en geen teruggedraaide uitrol van AI-nakijken** in het hoger onderwijs gevonden.
- **Geen churncijfers van losse nakijk- of feedbacktools** (Graide, KEATH, Gradescope, FeedbackFruits). Het zijn private bedrijven.
- **Niet onderzocht:** het instemmingsrecht van de Nederlandse medezeggenschap bij AI-nakijktools, en wat de AI-verordening met de doorlooptijd doet. "Het evalueren van leerresultaten" is hoog risico, met regels vanaf 2-12-2027.

## Bronnen

**Intern**
- Close, actieve en verloren opportunities, opgehaald 26-09-2026.
- `GTM/Knowledge/meddpicc-states-and-gates.md` (gates per fase en de forecastregel).
- `GTM/Accounts/windesheim/financiele-analyse.md` en `GTM/Accounts/rug-groningen/dossier-cost-justification-en-datalek.md` (de 30%-aanname).

**Primair**
- UCISA, Digital Education Survey Report 2024: https://www.ucisa.ac.uk/-/media/2024-Digital-Education-Survey-Report.pdf (2024)
- UCISA, TEL Survey 2016: https://www.ucisa.ac.uk/-/media/Files/UCISA/Publication-files/Surveys/TEL-surveys/TEL-Survey-2016_PDF-only.pdf (2016)
- University of Manchester, Senate-stuk over opt-out lecture capture: https://documents.manchester.ac.uk/display.aspx?DocID=29418 (2013)
- University of Manchester, opnamestatistieken 2013-2024: https://www.mypodcasts.manchester.ac.uk/technical-information/ (reeks 2013-2024)
- UCU, AI-enquête onder leden: https://www.ucu.org.uk/media/15202/Artificial-Intelligence-survey-of-members/pdf/UCU_-_Artificial_Intelligence_survey_of_members.pdf (2024/2025; vakbond, zelfselectie)
- UCU, principes voor AI: https://www.ucu.org.uk/media/15656/Principles-for-use-of-artificial-intelligence/pdf/UCU_AI_principles_March_26.pdf (2026)
- University of Birmingham, principes voor AI: https://www.birmingham.ac.uk/libraries/education-excellence/gai/principles-on-the-use-of-ai (2024)
- LSE, AI-assisted marking and feedback: https://info.lse.ac.uk/staff/divisions/Eden-Centre/Assets-EC/Documents/AI-assisted-marking-Nov-2025/AI-assisted-marking-and-feedback-revised-post-EC-Nov-2025-Exec-Summary.pdf (2025)
- King's College London, AI-assisted marking and feedback: https://www.kcl.ac.uk/about/strategy/learning-and-teaching/ai-guidance/ai-assisted-marking-and-feedback (2025)
- University of Cambridge, generative AI and assessment: https://blendedlearning.cam.ac.uk/artificial-intelligence-and-education/generative-ai-and-assessment (ongedateerd, vermoedelijk 2023-24)
- Jisc, AI in marking and feedback pilot: https://nationalcentreforai.jiscinvolve.org/wp/2025/12/11/ai-in-marking-and-feedback-pilot-early-stage-reflections/ (2025)
- Digital Education Council, Global AI Faculty Survey 2025: https://cdn.prod.website-files.com/65f1d299b87bcc50550a6398/678a9e0aa38a44fdac1d53a8_Digital%20Education%20Council%20Global%20AI%20Faculty%20Survey%202025-1.pdf (2025; ledenorganisatie met partnerships met onder meer Instructure)
- Tyton Partners, Time for Class 2025: https://4213961.fs1.hubspotusercontent-na1.net/hubfs/4213961/Publications/Time%20for%20Class/Tyton%20Partners_Time%20for%20Class%202025.pdf (2025; mede gefinancierd door edtech-partners, de editie van 2024 door Turnitin)
- Elon University en AAC&U, docentenenquête over AI: https://imaginingthedigitalfuture.org/wp-content/uploads/2026/01/TOPLINE-ITDF-facultyAI-survey-11.26.25.pdf (2025/2026)
- Ulster University, vertrouwen in AI bij nakijken: https://arxiv.org/pdf/2607.16223 (2026, preprint)
- HvA, generatieve AI in onderwijs, regels en adviezen: https://community-data-ai.npuls.nl/file/download/65b4c781-3c02-40a0-a922-0801a9b486be/generatieve-ai-in-onderwijs-regels-en-adviezen.pdf (2024)
- De Haagse Hogeschool, regels voor AI: https://community-data-ai.npuls.nl/attachment/entity/1855cef0-68ae-4e11-b101-5b67ef449129 (2024)
- Npuls, Handreiking 4 over de AI-verordening: https://www.npuls.nl/_assets/c46a36b7-2ec5-4fe1-a7c1-7d50b43edb94/Npuls-Handreiking-4-AI-B5.pdf (2025)
- Europese Commissie, AI Omnibus: https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force (2026)
- Duke OIT, einde LinkedIn Learning: https://oit.duke.edu/news/access-linkedin-learning-ending-july-31-2025/ (2025)
- Colorado State University, einde LinkedIn Learning: https://source.colostate.edu/linkedin-learning-access-ends-sept-24-steps-for-current-users/ (2026)
- University of Delaware, FeedbackFruits verdwijnt: https://sites.udel.edu/canvas/2025/10/feedback-fruits-tool-removal/ (2025)
- VIU, einde Studiosity: https://libguides.viu.ca/studiosity (2026)
- Instructure Holdings, 10-K over 2023 (NRR en GRR): https://www.sec.gov/Archives/edgar/data/1841804/000095017024017904/inst-20231231.htm (2024)
- D2L, jaarcijfers boekjaar 2026: https://www.newswire.ca/news-releases/d2l-inc-announces-fourth-quarter-and-fiscal-2026-financial-results-834480911.html (2026)
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
- Times Higher Education, AI marking trial: https://www.timeshighereducation.com/news/ai-marking-trial-not-looking-replace-humans (2026)
- EDUCAUSE Review, ROI van edtech: https://er.educause.edu/articles/2025/12/establishing-roi-for-evaluating-edtech-tools (2025; gesponsord door Jenzabar)
- NOS, docenten kijken na met AI: https://nos.nl/artikel/2609282-docenten-kijken-na-met-ai-slimme-tijdsbesparing-of-risicovol (2026)
- Penn GSE over Baker/BrightBytes, gebruik van ingekochte apps: https://www.gse.upenn.edu/news/schools-aren%E2%80%99t-using-apps-they-are-paying-study-finds (2018)
- The Markup, Turnitin-kosten per student in Californië: https://themarkup.org/artificial-intelligence/2025/06/26/plagiarism-detector-costs-california (2025, data 2021-22)

**Tertiair**
- Winning by Design, The Bowtie (win rate per dealgrootte): https://winningbydesign.com/wp-content/uploads/2026/02/The-Bowtie-A-Proposed-Standard.pdf (2026, data 2016-22; verkoopt eigen trainingen)
- Optifai, win rate per dealgrootte: https://optif.ai/learn/questions/b2b-saas-win-rate-by-deal-size/ (data 2025-26; verkoopt pipelinesoftware)
- RAIN Group, gemiddelde win rate op offertes: https://www.rainsalestraining.com/blog/average-sales-win-rates-how-do-you-compare (jaar van meting onbekend; salestrainingsbureau)
- SaaStr, conversie van betaalde pilots: https://www.saastr.com/what-is-the-typical-conversion-from-paid-pilot-to-annual-contract-in-b2b-saas/ (ongedateerd)
- Education Intel, waarom edtech-pilots zelden districtscontracten worden: https://educationintel.substack.com/p/why-edtech-pilots-rarely-become-district (2026)
- Echo360, case study Sheffield: https://echo360.com/case-study/the-university-of-sheffield/ (ca. 2023; leverancier)
- Zylo, SaaS-statistieken 2026: https://zylo.com/blog/saas-statistics (2026; verkoopt licentiebeheer)
- Glimpse K12, persbericht ongebruikte licenties: https://www.globenewswire.com/news-release/2019/05/15/1825260/0/en/Glimpse-K12-Analysis-of-School-Spending-Shows-that-Two-Thirds-of-Software-License-Purchases-Go-Unused.html (2019; verkoopt licentiemonitoring)
- Graide, prijspagina: https://www.graide.co.uk/pricing (bezocht 26-09-2026)
- Cadmus, prijspagina met pilot, pay-per-user en enterprise: https://cadmus.io/pricing/ (bezocht 26-09-2026)
