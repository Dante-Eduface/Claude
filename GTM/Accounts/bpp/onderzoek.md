# BPP — pain-onderzoek voor het gesprek met Phil Anthony

**Gesprek:** Dante met Phil Anthony, bij BPP (datum/tijd niet in de repo, gesprek is op korte termijn).
**Contact:** Phil Anthony. Let op titel: hij heet zelf **"Head of Digital Learning (Education & AI)"**, niet exact "AI Lead and Digital Education Head". Zelfde functie-inhoud, andere officiële bewoording.
**Eerder contact:** Dante heeft al eerder gesproken met **Joe Harris** en **Joel Mills** bij BPP (22-09-2026, uit de chat). Joe Harris is BPP Product & Technology, zijn Medium-quote over marking-snelheid staat in sectie 1. Joel Mills nog niet losstaand onderzocht.
**Close CRM:** geen BPP-lead gevonden bij een eerste zoekopdracht. Nog checken/aanmaken.

**Belangrijke kanttekening bij dit hele document:** alle vijf deelonderzoeken liepen tegen een geblokkeerde egress-proxy aan (WebFetch/curl geweigerd op vrijwel elk extern domein: bpp.com, linkedin.com, medium.com, qaa.ac.uk, kent.ac.uk, timeshighereducation.com, trustpilot.com, officeforstudents.org.uk, change.org, researchgate.net, discoveruni.gov.uk, zelfs wikipedia.org en google.com als test). Bijna alle bevindingen komen daarom uit **WebSearch-samenvattingen**, niet uit zelf gelezen brontekst — dat is zwakker bewijs dan de eigen regel van deze skill ("een snippet is geen bron") normaal toestaat. Twee documenten zijn wel volledig gelezen (BPP's eigen "Academic Practice"-beleid en het GenAI-studentendocument, beide op S3 gehost, niet op bpp.com zelf). De rest: behandel als plausibel, niet als geverifieerd, tot iemand met werkende toegang de pagina's zelf opent.

---

## 0. Wie is Phil Anthony — het belangrijkste voor het gesprek zelf

- **Sinds juli 2026 bij BPP**, dus zo'n **twee maanden in de rol**. Kwam over van University of Kent, waar hij sinds 2018 Head of AI / hoofd van het e-Learning Team was (daarvoor Canterbury Christ Church).
- Landelijk bekend als **oprichter van de "Digitally Enhanced Education"-webinarreeks** (gestart 2020, 3.400+ volgers) en **ALT Learning Technologist of the Year 2021**. De reeks is meeverhuisd naar BPP; eerstvolgende editie **14 oktober 2026, "Teaching with AI"**, met een oproep aan sprekers om praktijkvoorbeelden van AI in assessment aan te dragen — een signaal dat hij dit thema nú bij BPP oppakt, geen bewijs van een bestaande BPP-pilot.
- Zijn consistente publieke lijn (allemaal uit zijn Kent-periode, geen BPP-specifieke uitspraken gevonden): AI herframen als **"additional intelligence"** in plaats van "artificial intelligence" — een ondersteuningslaag die het denken van studenten versterkt, niet vervangt. Citaat: *"Rather than thinking of AI as artificial intelligence, we should start seeing it as additional intelligence, a support layer that helps students build on their own thinking, not replace it."* (kent.ac.uk, 2026, geparafraseerd via zoekresultaat, niet zelf gelezen)
- Citaat over ongeautoriseerd gebruik: *"Students are already using AI. The question is whether they are learning to use it well"* — bij het punt dat 94% van studenten generatieve AI gebruikt voor beoordeeld werk. En: *"if AI only appears in a module as a rule, a warning or a line in the assessment guidance, students may learn that it is something to manage quietly."* (edtechinnovationhub.com, 2025/2026)
- Bij Kent bouwde hij een **AI-vivavoorbereidingstool voor promovendi**, met de expliciete ontwerpregel dat de AI géén vivauitkomsten mag voorspellen — studenten moeten zelf bewijs identificeren en verdedigen. Sterk haakje: hij heeft zelf al ervaring met AI + mondelinge verificatie combineren, precies het terrein van Eduface's Academic Integrity-module.
- **Correctie op onze eigen data:** de SHIFT-master noemt Jeremy Bodey "Managing Director of BPP Digital Education". Alle vijf bronnen die zijn functie noemen zeggen consequent **"Director of Strategy, Innovation and Technology"** bij BPP (sinds 2012). Geen bron bevestigt een rapportagelijn tussen Phil Anthony en Jeremy Bodey. Dit mag gecorrigeerd worden in `GTM/ICP/shift/master/people.csv`, maar dat is aan de lead/contact-sourcing-agent, niet hier gedaan.
- **Grote structuurwijziging:** BPP Holdings is in 2026 herbrand tot **"Lyceum Education Group"**, een groep van 11 training providers waaronder BPP, Acsenda en Firebrand (edtechinnovationhub.com, 2026). Onze eigen orgs.csv kent BPP nog als "BPP Holdings" — ook een punt voor de volgende SHIFT-ronde.

---

## 1. Marking time & operational efficiency

**Antwoord in het kort:** BPP's eigen tech-team erkent expliciet dat marking sneller kan met AI. Er is een harde marking-SLA (10 werkdagen) die volgens Trustpilot-reviews niet altijd gehaald wordt. Onafhankelijke kwaliteitsmetrics (TEF, THE) wijzen op organisatorische zwakte. De eigenaar (TDR Capital/Lyceum) zit financieel onder druk na een mislukte verkooppoging.

- **BPP's eigen Product & Technology-team zegt het hardop:** Joe Harris (BPP Product & Technology) schrijft dat marking *"could definitely be done faster with some AI help"* en dat AI tijd moet vrijmaken van taken die niet de expertise van tutoren vragen. Bron: medium.com/bpp-technology (2024, primair — BPP's eigen medewerker, niet zelf gelezen door blokkade, wel expliciet geciteerd door de subagent).
- **Harde marking-SLA van 10 werkdagen**, o.a. voor CIPD-programma's, staat in BPP's terms and conditions (bpp.com/terms-and-conditions, 2023-2026, primair). Dat is een gemeten/beloofde KPI — een concreet aanknopingspunt om over versnelling te beginnen.
- **Trustpilot-reviews (2025)** bevestigen praktijkpijn: een student wachtte na inlevering op 7 juli nog op feedback op 14 juli; het nakijkteam reageerde pas op 21 juli na administratieve verwarring over bestandsformaat. Algemenere klachten over lange, onduidelijke wachttijden. (secundair/anekdotisch, niet geverifieerd als representatief)
- **TEF 2023:** BPP University kreeg "Requires improvement" op Student Experience (ondanks Bronze algemeen). Een THE-analyse van recente NSS-data plaatst BPP bij instellingen met een gat van **meer dan 10 procentpunt** tussen benchmark en score op het thema "organisation and management" (timeshighereducation.com, jaartal niet met zekerheid vastgesteld, waarschijnlijk 2024-2026).
- **Vendor-case study (Build Circle):** BPP's content-/ontwikkelcycli daalden van 13+ dagen naar 2-3 dagen na een digitaliseringsproject tegen legacy-IT en data-silo's — bevestigt dat "trage doorlooptijd door verouderde systemen" een erkend thema is, niet 1-op-1 over marking maar wel over operationele efficiëntie. Behandel als marketing (leverancier verkoopt eigen succesverhaal), jaartal niet hard, waarschijnlijk 2024-2025.
- **Financiële context:** BPP is eigendom van private equity firm TDR Capital (sinds 2021), die BPP in 2024/2025 probeerde te verkopen voor ~£2,5 miljard. Die verkoop mislukte; BPP zit nu in een herfinancieringstraject (cityam.com, 2025, secundair). Kostenreductie/efficiency is dus niet alleen een onderwijskundig thema maar ook een aandeelhoudersthema.

**Tegenspraak:** BPP's eigen "Externally validated"-pagina toont hoge positieve NSS-cijfers (91-95% op losse items), terwijl TEF en THE onafhankelijk een "requires improvement" en een fors benchmark-gat rapporteren. Zelfde patroon als onze eigen data (87,3% tegen benchmark 88,8%): BPP's externe communicatie kiest de gunstige cijfers, de strengere externe beoordelingen laten iets anders zien.

---

## 2. Consistency in grading

**Antwoord in het kort:** QAA vond in 2017/2018 geen probleem — maar dat is vóór de AI-periode en voegt dus weinig toe. De sterkere signalen zijn recenter: TEF 2023 "Requires improvement" op Student Experience terwijl concurrent University of Law Gold haalde op exact dezelfde categorie, en een lopende studentenpetitie van **mei 2026** die een structurele 15%-cijfercorrectie eist wegens een vermeend systematisch verschil tussen BPP (proctored) en ULaw (niet-proctored) examens.

- **Change.org-petitie, 14 mei 2026:** BPP Law School-studenten eisen een structurele 15%-cijfercorrectie t.o.v. University of Law, met als argument dat BPP-examens proctored zijn en ULaw's niet, wat tot systematisch lagere cijfers bij BPP zou leiden. Eenzijdig (student-geïnitieerd, geen onderbouwde data), maar een sterk en **actueel** signaal van een klantgevoel over oneerlijke/inconsistente beoordeling. (primair maar eenzijdig, 2026)
- **TEF 2023:** BPP "Requires improvement" op Student Experience, University of Law "Gold" op dezelfde categorie (officialstudents.org.uk / law.ac.uk, 2023, primair).
- **BPP Business School zelf publiceerde in 2014 een working paper** over inconsistenties tussen nakijkers bij essay-marking, inclusief gender-gerelateerde bias, met pogingen tot standaardisatie in één module (researchgate.net, 2014, primair — BPP's eigen personeel). Gedateerd, maar toont dat het instituut dit probleem intern al eens onderzocht en erkend heeft.
- **QAA-rapporten (december 2017, december 2018):** BPP voldeed op alle beoordeelde gebieden, met een expliciet beschreven moderation-beleid en gekalibreerde steekproef van nakijkers. Geen kritiek op marking/consistentie gevonden. Dit **ondergraaft** de aanname voor het QAA-kanaal specifiek — maar is ook het laatste publiek gevonden QAA-rapport over BPP, dus dateert van vóór de AI-periode en vóór de recente NSS-daling.
- **Kleine steekproef, richting-consistent:** Discover Uni toont voor één BPP-cursus (BSCAF3) 87% op "assessment and feedback" (n=20, 2024/25) — consistent met ons eigen instellingsbrede cijfer van 87,3%, maar te klein om als bevestiging te gelden.
- **Oudere incidenten (2010-2022, buiten hoofdvenster maar wel een patroon):** RollOnFriday-berichten over foutieve uitslagen en examenchaos; Corporate Law Academy-forumposts over een fout gemarkeerd tort-summatief met niet-passende feedback en een gelekte mark-scheme-video. Anekdotisch en ongeverifieerd.

**Tegenspraak:** BPP's officiële kwaliteitskader (marking policy, moderation code, kalibratie-oefeningen, zoals beschreven in QAA 2018) claimt structurele consistentie-borging, terwijl de petitie van mei 2026 stelt dat er een onopgelost, structureel cijferverschil bestaat met een directe concurrent — met gevolgen voor training contracts en pupillages. QAA zelf bekritiseerde in een vroege review (rond 2013-2015) BPP's eigen taalgebruik ("consistently outstanding student satisfaction") als mogelijk misleidend door gebrek aan onderbouwing — hetzelfde patroon van claim-versus-bevinding, maar buiten het gevraagde tijdvak.

---

## 3. Unauthorized AI use

**Antwoord in het kort:** BPP heeft sinds juli 2024 een expliciet, actueel AI-misconduct-beleid en een apart studentendocument met een acceptable/unacceptable-tabel. BPP behandelt AI-misbruik zwaarder dan gewoon plagiaat. Er zijn geen publieke, BPP-specifieke fraudecijfers of mediaschandalen — BPP is een privaat bedrijf en valt niet onder de Freedom of Information Act, dus die cijfers zijn structureel niet publiek te vinden.

- **"Academic Practice" University Policy v3.0** (effectief september 2024, eigenaar Office for University Academic Quality), artikel 5.3(k): **"Misuse of Artificial Intelligence"** is een expliciete, eigen categorie academic misconduct/plagiaat. Volledig gelezen door de subagent (S3-gehoste PDF, niet geblokkeerd). (primair, 2024)
- **Penalty-matrix (6.2.5):** een eerste overtreding "Misuse of AI" bij minder dan 30% van het werk gaat direct naar het zwaardere Academic Misconduct Panel, terwijl een eerste plagiaat-/collusiegeval onder dezelfde grens via de lichtere desk-based afhandeling loopt. **BPP behandelt AI-misbruik dus zwaarder dan gewoon plagiaat.** (primair, 2024)
- **Apart studentendocument "Acceptable and Unacceptable Uses of GenAI Tools"** (S3-gehost, gekoppeld aan beleidsversie 3.0, volledig gelezen): onacceptabel is o.a. knip-plak van AI-output, parafraseren van AI-output om detectie te ontlopen, AI gebruiken waar mondelinge/schriftelijke taalvaardigheid zelf wordt getoetst (**incl. vivas en advocacy exams**), en voor apprentices: AI-output in het EPA-portfolio mag nooit. Contactpunt: GenAI@bpp.com. (primair, vermoedelijk 2024)
- **BPP valt niet onder de UK Freedom of Information Act** (bevestigd via WhatDoTheyKnow-correspondentie met BPP zelf) — dus geen publieke route naar eigen misconduct-cijfers, en BPP zit vrijwel zeker niet in de landelijke Guardian FOIA-dataset (bijna 7.000 bewezen AI-fraudegevallen op UK-universiteiten in 2023/24, gepubliceerd juni 2025).
- **Sectorcontext, relevant voor BPP Professional Education:** ACCA — de grootste accountancy-body wereldwijd, waarvoor BPP een van de grootste UK-opleiders is — stopt vanaf **maart 2026** met online/remote examens, expliciet omdat AI-fraude sneller gaat dan detectiemethoden (Lexology, the-decoder.com, cityam.com, 2025/2026, consistent bericht over meerdere bronnen).
- **Niet gevonden, dus niet gebruiken:** een claim dat BPP essays volledig zou hebben afgeschaft ten gunste van live oral interviews (die vervolgens weer omzeild werden met AI-luister-apps) kon niet geverifieerd worden. Staat mogelijk in dezelfde Joe Harris Medium-post als een illustratief toekomstscenario, niet als beschrijving van de huidige praktijk — dat past ook beter bij wat het officiële beleid zegt (doorlopend gebruik van geschreven summatieve assessments met AI-declaratieplicht op het coversheet, viva voce als aanvullend instrument bij verdenking, geen algehele vervanging).

**Tegenspraak:** de essay-afschaffingsclaim (indien echt) zou lijnrecht ingaan tegen het officiële beleidsdocument. Zonder toegang tot de Medium-bron blijft dit onopgelost — niet citeren in het gesprek zonder eigen verificatie.

---

## 4. AI grading tool pilots / implementaties

**Antwoord in het kort:** Geen bewijs van een BPP-pilot of -samenwerking met een externe AI-marking-vendor (Turnitin/Gradescope/Graide/FeedbackFruits/Cogniti/Studiosity/Ello). BPP heeft wel eigen GenAI-toepassingen gebouwd, maar die zitten in **contentcreatie** (vraag-generatie), niet in het beoordelen zelf. Het feitelijke nakijken bij BPP Professional Education was in oktober 2025 nog volledig mensenwerk.

- **BPP + Build Circle:** custom generatieve-AI-tool voor het **genereren van meerkeuzevragen voor de SQE** (Solicitors Qualifying Exam), reviewtijd per vraag van ~60 naar ~15 minuten (buildcircle.co.uk, vendor case study, jaartal niet hard, waarschijnlijk medio 2024).
- **Joe Harris (BPP Product & Technology), juli 2024:** stelt dat BPP zich "in de vroege fase" bevindt van GenAI-verkenning voor assessment. Bevestigt: geen volwassen AI-marking-implementatie, wel actieve verkenning. (primair, 2024)
- **BPP-vacature "Marking Executive"** (laatste versie 8 oktober 2025, eerdere versie september 2024): beschrijft een volledig **mensen-gedreven** marking-proces — spreadsheets, markers boeken, facturen verwerken. Geen AI genoemd. Sterkste harde aanwijzing dat het ACCA-mock-marking-proces (het bewijs uit de 2021-prijslijst dat we al hadden) medio oktober 2025 nog steeds mensenwerk was. Geen bewijs van AI-vervanging daarna.
- **BPP Adapt** (mei 2020, met CENTURY TECH): AI-powered adaptive learning platform voor postgraduate law-studenten. Oud, en gaat over adaptieve feedback op oefenvragen, niet over het vervangen van summatief nakijken.
- **Geen deelname gevonden aan de Jisc "AI in Marking and Feedback"-pilot** (Graide, Keath, TeacherMatic; 14 colleges + 21 universiteiten) — wel London South Bank University en Ayrshire College als deelnemers genoemd.
- **e-Assessment Association 2026 Awards, categorie "AI in Marking":** Henley Business School als voorbeeld-finalist genoemd, BPP niet.
- **Phil Anthony's vacaturetekst** ("Head of Digital Learning, Education & AI") beschrijft strategische inbedding van AI in learning/teaching/assessment als opdracht — bevestigt dat dit nu pas structureel wordt opgepakt, niet dat er al een lopende marking-pilot is.

**Voor Eduface relevant:** dit is een wit vlak. BPP heeft AI ingezet voor vraag-generatie en adaptief oefenen, maar (voor zover publiek te vinden) niet voor het daadwerkelijk beoordelen van studentwerk. Geen incumbent-vendor om tegen te concurreren op dit specifieke terrein.

---

## Wat dit betekent voor Eduface

BPP heeft de pijn op alle drie de gevraagde vlakken zelf al zichtbaar erkend of extern bevestigd gekregen: het eigen tech-team zegt hardop dat marking sneller kan met AI, een harde 10-dagen-SLA wordt volgens reviews niet altijd gehaald, TEF/THE bevestigen een organisatorisch zwak punt, en een actuele studentenpetitie (mei 2026) maakt beoordelingsconsistentie een levend, ongemakkelijk thema. Tegelijk heeft BPP sinds juli 2024 een ongewoon volwassen en streng AI-misconduct-beleid, inclusief het gebruik van viva/mondelinge toetsing als instrument bij verdenking — dat ligt dicht bij Eduface's Academic Integrity-module. Er is geen bewijs van een concurrerende AI-marking-vendor bij BPP: het enige gevonden AI-gebruik in assessment zit bij vraag-generatie, niet bij nakijken. De timing is dubbel: Phil Anthony is pas twee maanden in zijn rol en actief op zoek naar praktijkvoorbeelden van AI in assessment (zijn eigen webinar op 14 oktober vraagt er letterlijk om), wat een kans is om mee te bouwen aan zijn strategie voor die het vastligt — maar het betekent ook dat hij mogelijk nog geen budget-mandaat of BPP-specifiek standpunt heeft, dus dit gesprek is waarschijnlijker een verkennend/relatiegesprek dan een dealgesprek.

---

## Gaten (wat niet hard te krijgen was)

- Geen directe uitspraak van een BPP (Group/Lyceum) CEO over marking time of nakijkkosten.
- Geen directe quote van Phil Anthony zelf over BPP specifiek (alleen zijn Kent-periode) — logisch, hij is er net.
- Geen QAA-rapport na 2018 gevonden.
- Geen officiële, per-vraag uitgesplitste NSS-tabel voor BPP (zoals we voor University of Law wel hebben).
- Geen extern-examinatorrapport met inhoud/bevindingen.
- Geen cijfers over personeelskosten of aantal markers bij BPP/Lyceum (jaarrekeningen van Bright Topco/BPP University Limited zijn gevonden als URL maar niet gelezen — kan in een vervolgronde alsnog).
- Geen bevestiging of BPP meedoet aan enige landelijke AI-in-marking-pilot (Jisc of anderszins).
- De essay-afschaffing-claim (zie sectie 3) blijft onopgelost.
- **Structurele beperking:** vrijwel alle bevindingen komen uit zoekresultaat-samenvattingen, niet uit zelf geopende bronnen, door een geblokkeerde egress-proxy in deze sessie. Bij een vervolgronde met werkende toegang kunnen bovenstaande claims alsnog zelf op de brontekst geverifieerd worden.

---

## Bronnenlijst

**Primair**
- BPP "Academic Practice" University Policy v3.0 (sept 2024) — volledig gelezen — https://bppassets.s3.eu-west-1.amazonaws.com/public/assets/pdf/governance-finance/upp/22.+Academic+Practice.pdf
- BPP "Acceptable uses of GenAI tools - STUDENTS" — volledig gelezen — https://aipowerpoint.s3.eu-west-2.amazonaws.com/Acceptable+uses+of+GenAI+tools+-+STUDENTS.pdf
- BPP terms and conditions (marking-SLA 10 werkdagen) — https://www.bpp.com/terms-and-conditions/december-2023-onwards
- BPP-vacature "Marking Executive" (8-10-2025) — https://vacancies.bpp.com/jobs/job/Marking-Executive/898
- BPP-vacature "Head of Digital Learning (Education & AI)" — https://careerscentre.bpp.com/members/modules/job/detail.php?record=1308
- TEF 2023 panel statement BPP University Limited — https://tef2023.officeforstudents.org.uk/... (zie sectie 1/2)
- University of Law TEF 2023 persbericht — https://www.law.ac.uk/about/press-releases/tef2023/
- QAA Higher Education Review BPP, dec 2017 — https://www.qaa.ac.uk/docs/qaa/reports/bpp-university-ltd-her-ap-17.pdf
- QAA monitoring visit BPP, dec 2018 — https://www.qaa.ac.uk/docs/qaa/reports/bpp-university-ltd-scd-am-18.pdf
- BPP Business School working paper over marker-inconsistenties (2014) — https://www.researchgate.net/publication/261877280
- Change.org-petitie BPP Law School grade adjustment (14-05-2026) — https://www.change.org/p/bpp-law-school-award-a-15-grade-adjustment-to-level-the-playing-field-with-ulaw
- BPP "Externally validated" / graduate outcomes-pagina — https://www.bpp.com/about-bpp/bpp-university/graduate-outcomes
- Phil Anthony LinkedIn — https://www.linkedin.com/in/phil-anthony-sfhea-60015a1a2/
- Phil Anthony Substack (Digitally Enhanced Education) — https://philanthony1.substack.com/p/a-new-home-for-the-digitally-enhanced, https://philanthony1.substack.com/p/teaching-with-ai-a-reminder-about
- Joe Harris (BPP Product & Technology), "Generative AI at BPP" — https://medium.com/bpp-technology/generative-ai-at-bpp-the-future-of-assessment-in-education-5d958e6b0a1b (2024, niet zelf gelezen)
- WhatDoTheyKnow-correspondentie (BPP valt niet onder FOIA) — whatdotheyknow.com

**Secundair**
- edtechinnovationhub.com: Phil Anthony vertrekt Kent naar BPP; Lyceum Education Group-lancering
- timeshighereducation.com: TEF-Bronze-analyse (2023); NSS "organisation and management" gat-analyse
- cityam.com: TDR Capital herfinanciering BPP (2025)
- Lexology / the-decoder.com: ACCA stopt met online examens vanaf maart 2026
- eandt.theiet.org e.a.: Guardian FOIA AI-fraude-onderzoek UK-universiteiten (juni 2025)
- kent.ac.uk nieuwsprofielen Phil Anthony (2021, 2025/2026)
- rollonfriday.com: diverse BPP-examenincidenten (2010-2020)
- discoveruni.gov.uk: NSS-cijfer BSCAF3 (2024/25)

**Tertiair**
- buildcircle.co.uk: twee case studies (content-cyclusversnelling; SQE MCQ-generatie) — vendor-marketing
- uk.trustpilot.com/review/www.bpp.com — klantreviews, ongefilterd
- thecorporatelawacademy.com forum — anonieme studentenposts (2020-2021)
- nationalcentreforai.jiscinvolve.org — Jisc AI-in-marking-pilot
- e-assessment.com — EAA Awards 2026 finalisten

_Onderzocht 22-09-2026 door 5 parallelle subagents (standaard diepte), egress-proxy blokkeerde directe bronraadpleging voor vrijwel alle domeinen behalve twee S3-gehoste PDF's._
