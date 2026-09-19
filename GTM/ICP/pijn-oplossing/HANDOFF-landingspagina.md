# Overdracht: pijn voor de landingspagina

Stand 2026-09-11. Dante heeft 576 uitspraken uit Close doorgelopen en er 50 als "klopt" gemarkeerd (49 pijn, 1 gewenste uitkomst) en 64 als "weg". Dit bestand bevat alleen wat klopt, plus de conclusie. Volledige data: `items.json` en `besluiten.json` in deze map. Productclaims mogen uitsluitend uit `Platform/product.md`.

## De pijn in één zin per segment

**Particuliere opleiders (22 van 50, het zwaartepunt)**
Beoordelen gebeurt door wisselende (zzp-)docenten, kost per student uren die in het docenttarief verdwijnen, en levert cijfers op die niet consistent en niet navolgbaar zijn. Dat wordt zichtbaar bij studenten (een 7 bij de een, een 6 bij de ander) en bij de NVAO (navolgbaarheid als terugkerend aandachtspunt). Accreditatieverlies is voor deze scholen existentieel.
- Harde getallen: 2 uur per student per periode (Notenboom); een directeur die zelf ~100 studenten nakijkt (SDO); drie docenten voor tientallen werken met 1 tot 2 uur kalibratie per jaar (Breederode).
- Doorlooptijd: beloofde twee weken worden niet gehaald (BSN); nakijktermijnen sneuvelen op capaciteit (Breederode).
- Kwaliteitsbewaking is steekproef of klachtgedreven (Notenboom, BSN).

**NL hogescholen en universiteiten (12)**
Minder docenten, meer studenten, en de feedback die overblijft is te dun. Formatie krimpt 20% met vacaturestop (Windesheim); een pensioen wordt niet vervangen terwijl de instroom groeit (Den Haag). Docenten die wel tijd steken in feedback vinden hem zelf te summier (Maartje Sijm). Inconsistentie tussen docenten wordt erkend (Windesheim). Generieke LLM's geven niet de feedback die de docent zelf zou geven (Rotterdam). Elke extra tool is een adoptiedrempel.

**UK en Ierland (11)**
Consistentie tussen markers binnen één cohort is het eerste probleem (Sunderland, Bristol, CMI met 1.000 opdrachten over 20+ docenten). Daarna doorlooptijd: van twee weken naar één week, wat op de TA's drukt (Bristol). De koopreden op instellingsniveau is governance: er is geen goedgekeurde AI-tool terwijl docenten al AI gebruiken (Bath Spa). Staff is time-poor; tijdwinst moet meteen zichtbaar zijn of het wordt niet gebruikt. Een business case met case studies opent de deur ondanks beleid (Sunderland).

**Overig internationaal (5)**
Instructeurs die 2 tot 4 uur per dag nakijken bovenop 8 tot 10 uur lesgeven, en daardoor vertrekken (UTI, VS). Eindprojecten van 100+ pagina's die in enkele weken nagekeken moeten worden (UADE, Argentinië).

## Wat over alle segmenten heen hetzelfde is
1. **Tijd** is de zichtbare pijn, **consistentie en navolgbaarheid** is de pijn waar de beslisser voor betaalt (directeur, examencommissie, NVAO, PVC).
2. De pijn wordt pas urgent als hij **zichtbaar wordt voor een derde**: studenten die verschillen zien, een klacht, een NVAO-rapport, een gemiste termijn.
3. **Krimp** is de why-now in NL ho (formatie, vacaturestop); **governance** is de why-now in UK; **accreditatie** is de why-now bij particulier.
4. Docenten zeggen niet "ik wil minder werk", ze zeggen "ik kom niet toe aan de feedback die ik wil geven" (Maartje, Noordhoff, Tio). Dat is de toon voor de pagina.

## Wat NIET op de pagina mag
- Niets uit de thema's Productervaring, Bezwaar of Huidige aanpak: dat is sales- en productinput, geen websitecopy.
- TIO Business School en ICM Opleidingen nooit noemen. Bath Spa alleen als geanonimiseerde UK-pilot tenzij Dante toestemming heeft. Klantnamen die mogen: Hogeschool Rotterdam (lerarenopleiding), De Haagse Hogeschool, Tilburg University, Radboud Universiteit.
- Citaten van prospects niet met naam op een publieke pagina. Gebruik ze als bron voor de formulering, niet als testimonial.
- Geen claims buiten `Platform/product.md`. Geen "minder uitval" beloven, geen implementatietijd, geen NSS-effect.
- Schrijfstijl: `.claude/rules/communication-style.md` en de skill `schrijven`. Design: `Design/System/core/` plus `web/`, via de drie poorten uit `core/proces.md`.

## De 50 goedgekeurde uitspraken, per segment en thema


### Particuliere opleiders (NL) (22)

**Nakijklast en werkdruk**
- "Nakijken was voor mij altijd één van de minst favoriete klussen; het is tijdrovend en studenten lijken de feedback vaak pas echt serieus te nemen als ze een onvoldoende krijgen." (Tio Business School, Gideon Hummel, 2025-09-29, letterlijk) `Tio-Business-School-01`
  - Nakijken kost tijd en de feedback landt pas bij een onvoldoende.
- "De signalen vanuit docenten laten vooral een duidelijke behoefte zien rondom begeleiding tijdens het schrijfproces van studenten. Docenten geven aan dat dit in de praktijk veel tijd kost, terwijl studenten hier aantoonbaar baat bij hebben." (Noordhoff, Harald Grasdijk, Learning & Innovation specialist - Strategisch adviseur, 2026-05-22, letterlijk) `Noordhoff-01`
  - Begeleiden tijdens het schrijven kost docenten veel tijd, dat is de erkende pijn.
- "Hij kijkt zelf na en beoordeelt het werk van ongeveer 100 studenten, dit kost hem heel veel tijd." (SDO Hogeschool, Marcel van Marrewijk, directeur SDO Hogeschool, 2026-08-03, parafrase) `SDO-Hogeschool-1`
  - Directeur kijkt zelf ongeveer 100 studenten na en verliest daar veel tijd aan.
- "Zij noemt zelf "Dit is een heel erg arbeids intensieve proces"" (Business School Notenboom, Barbara Suijkerbuijk, Directeur onderwijs, 2026-08-11, letterlijk) `Business-School-Notenboom-01`
  - Afstudeerproces met meerdere deelproducten en verdedigingen is arbeidsintensief.
- "Docenten besteden ongeveer twee uur per student per periode aan beoordeling van schrijfopdrachten. De organisatie heeft onvoldoende capaciteit voor grondige analyses en kwaliteitsverbeteringen door de hoge werkdruk." (Business School Notenboom, Barbara Suijkerbuijk, Directeur onderwijs, 2026-08-18, parafrase) `Business-School-Notenboom-12`
  - Twee uur per student per periode, het enige harde nakijkcijfer dat we hebben.
- "Formatief beoordelen van ALPs is chaotisch omdat studenten niet weten welke docent het voorstel moet beoordelen." (Business school Nederland, Arthur van Gemert, Studiebegeleider / onderwijs en innovatie, 2026-08-31, parafrase) `Business-school-Nederland-4`
  - Routering van formatieve beoordeling is chaotisch.
- "Ivonne benadrukte dat elk jaar 1-2 uur kalibrering nodig is, terwijl zij met z'n drieën tientallen studentenwerk moeten beoordelen." (Breederode Hogeschool, Ivonne Duiser, 2026-09-01, parafrase) `Breederode-Hogeschool-18`
  - Drie docenten beoordelen tientallen werken met minimale kalibratietijd.
- "Werkdruk leidt tot onvrede bij zowel studenten als docenten, wat motivatie en betrokkenheid beïnvloedt. ZZP-ers die meebeordelingen doen hebben vaak meer tijd nodig omdat zij minder frequent met studenten contact hebben." (Breederode Hogeschool, 2026-09-03, parafrase) `Breederode-Hogeschool-22`
  - Werkdruk raakt motivatie van docenten en studenten, zzp-beoordelaars zijn trager.

**Consistentie en kwaliteit van feedback**
- "De school worstelt met consistentie in beoordelingen vanwege wisselende docenten die als zelfstandig opereren. Docenten hebben beperkte inhoudelijke voorbereiding voor het geven van beoordelingen zonder onderwijskundige kennis." (Business School Notenboom, Barbara Suijkerbuijk, Directeur onderwijs, 2026-08-18, parafrase) `Business-School-Notenboom-10`
  - Wisselende zzp-docenten zonder onderwijskundige basis maken beoordelen inconsistent.
- "Grootste uitdaging is dat het voor opleidingsmanager Marloes moeilijk is overzicht te bewaren over verschillende docenten, op het gebied van beoordelen, onderlinge samenwerking en het aanbieden van modulair onderwijs." (Breederode Hogeschool, Marloes de Graaf, 2026-08-25, parafrase) `Breederode-Hogeschool-02`
  - Opleidingsmanager mist overzicht op hoe docenten beoordelen.
- "Inconsistentie tussen beoordelaars: een beoordelaar geeft een 7, ander geeft een 6 voor identieke werk." (Business school Nederland, Arthur van Gemert, Studiebegeleider / onderwijs en innovatie, 2026-08-31, parafrase) `Business-school-Nederland-3`
  - Zelfde werk krijgt een 7 of een 6, afhankelijk van de beoordelaar.
- "Beoordelingen worden continu gemonitord, maar alleen reactief via studentenklachten en niet proactief." (Business school Nederland, Arthur van Gemert, Studiebegeleider / onderwijs en innovatie, 2026-08-31, parafrase) `Business-school-Nederland-7`
  - Kwaliteitsbewaking start pas bij een klacht van een student.
- "Een recente situatie (april) toonde aan dat docenten subjectieve verschillen in beoordeling hadden die studenten influenceerden in hun perceptie van docenten." (Breederode Hogeschool, Marloes de Graaf, 2026-09-01, parafrase) `Breederode-Hogeschool-17`
  - Beoordelingsverschillen tussen docenten zijn zichtbaar bij studenten.

**Accreditatie en borging**
- "De examencommissie voert momenteel alleen steekproefswijs controles uit, waardoor veel kan worden gemist." (Business School Notenboom, Barbara Suijkerbuijk, Directeur onderwijs, 2026-08-18, parafrase) `Business-School-Notenboom-11`
  - Kwaliteitscontrole is steekproef, dus gaten blijven onzichtbaar.
- "De NVAO stelt steeds strengere eisen aan verifieerbare kwaliteitsborging. Het risico bestaat dat onvoldoende kwaliteitsborging leidt tot afkeuring en daarmee verlies van accreditatie. Accreditatie-verlies zou het hele bedrijfsmodel van de school in gevaar brengen." (Business School Notenboom, Barbara Suijkerbuijk, Directeur onderwijs, 2026-08-18, parafrase) `Business-School-Notenboom-13`
  - Accreditatieverlies is existentieel, dat is hun zwaarste risico.
- "Ik las in de NVAO-rapporten van Verpleegkunde en Manuele Therapie dat de navolgbaarheid van het cijfer op afstudeerwerk bij Breederode een terugkerend aandachtspunt was, en dat jullie dat nu oplossen met kalibratiesessies, het vier-ogenprincipe en een eigen toetsexpertcommissie." (Breederode Hogeschool, 2026-08-25, parafrase) `Breederode-Hogeschool-01`
  - NVAO-kritiek op navolgbaarheid van cijfers is de gedocumenteerde ingang.
- "Calibratiesessies zijn momenteel niet-verplicht maar voor accreditatievisitaties wel nodig, wat tijdsintensief is. Het grootste risico is dat deze kennis in één persoon zit." (Breederode Hogeschool, Irma van der Velden, Directeur, 2026-09-09, parafrase) `Breederode-Hogeschool-28`
  - Kalibratie kost tijd en de kennis hangt aan één persoon, dat is het risico.

**Moment en snelheid van feedback**
- "BSN belooft studenten beoordeling binnen twee weken, maar dit wordt niet altijd gehaald." (Business school Nederland, Arthur van Gemert, Studiebegeleider / onderwijs en innovatie, 2026-08-31, parafrase) `Business-school-Nederland-2`
  - Belofte van twee weken doorlooptijd wordt niet gehaald.
- "Jochem van Schalkwijk benadrukte dat responstijd en feedback-kwaliteit veel kunnen helpen, vooral voor collega's met beperkte beschikbaarheid." (Breederode Hogeschool, Jochem van Schalkwijk, 2026-09-03, parafrase) `Breederode-Hogeschool-20`
  - Responstijd op feedback is de pijn bij deeltijd- en zzp-docenten.
- "Sanne Toonen-Zwinkels vermeldde dat nakijktermijnen niet altijd kunnen worden nageleefd vanwege capaciteitsproblemen." (Breederode Hogeschool, Sanne Toonen, 2026-09-03, parafrase) `Breederode-Hogeschool-21`
  - Afgesproken nakijktermijnen worden door capaciteitstekort niet gehaald.

**Rubrics en beoordelingscriteria**
- "Goede beoordelingscriteria schrijven is lastig en vereist alignment tussen competentieprofiel, leerresultaten, modules en eindtermen. Docenten worden hierin niet getraind via standaard docenten-BKE-opleiding, wat een gat veroorzaakt." (Breederode Hogeschool, Irma van der Velden, Directeur, 2026-09-09, parafrase) `Breederode-Hogeschool-29`
  - Docenten kunnen geen goede beoordelingscriteria schrijven, BKE dekt dat niet.

**Privacy, compliance en inkoop**
- "Universiteiten leggen toenemend nadruk op gegevenssoevereiniteit en lokale hosting. Universiteit Twente onderzoekt alternatieven als Nextcloud voor beter databestuur." (Atvica, Arnout Vree, Directeur & oprichter Avetica, 2026-09-08, parafrase) `Atvica-1`
  - Datasoevereiniteit en lokale hosting wegen zwaarder bij universiteiten.


### NL hogescholen en universiteiten (12)

**Nakijklast en werkdruk**
- "Begin januari heeft Sco (schriftelijke communicatie) haar eerste grote schrijfopdracht voor zes klassen. Dat is echt heel veel nakijkwerk.... Ik wil natuurlijk graag Eduface daarbij gebruiken." (Haagse Hogeschool, Els Stapersma, Docent taalvaardigheid, opleiding IVK, 2025-11-05, letterlijk) `Haagse-Hogeschool-04`
  - Een grote schrijfopdracht over zes klassen is het concrete piekmoment waar de pijn zit.
- "Het kost mij namelijk veel tijd, maar ik vind ik het nog te summier en te weinig diepgaand voor een student om er echt vooruit mee te kunnen. Ik geef vooral aan wat er niet goed is, maar kan niet ook nog rijke voorbeelden, extra uitleg of concrete tips geven." (Haagse Hogeschool, Maartje Sijm, Docent IVK, lid AI-sleutelteam lectoraat, 2026-03-23, letterlijk) `Haagse-Hogeschool-21`
  - Zelfs veel tijd levert te dunne feedback op, verdieping sneuvelt als eerste.
- "Docenten hebben grote behoefte aan efficientere en kwalitatief betere feedback op studentenwerk." (Windesheim, Geert van der Wijk, Product Owner-Educational Systems, 2026-08-19, parafrase) `Windesheim-01`
  - Docenten willen sneller en beter feedback geven, breed gedragen behoefte.
- "Jaarplannen tot 2028 voorzien daling studentenaantallen met 9% en onderwijsformatie met 20%. Er is een vacaturestop voor docenten. Met minder docenten wordt meer werk verwacht." (Windesheim, Geert van der Wijk, Product Owner-Educational Systems, 2026-09-09, parafrase) `Windesheim-08`
  - Formatie krimpt 20% met vacaturestop, werk per docent stijgt, harde bezuinigingspijn.

**Bestaande tools, zelf bouwen en alternatieven**
- "Hij heeft expliciet aangegeven dat ze niet de capaciteit hebben om in huis wat zelf te bouwen." (Avans Hogeschool, Luiz Alberto Canalle, Senior lecturer & AI-Innovation coordinator, 2026-04-15, letterlijk) `Avans-Hogeschool-3`
  - Geen eigen bouwcapaciteit, dus ze moeten inkopen.
- "Ook met de grote LLMs is het heel moeilijk om de feedback te krijgen zoals je het zelf zou geven." (Rotterdam University of Applied Sciences, 2026-06-08, parafrase) `Rotterdam-University-of-Applied-Sciences-01`
  - Generieke LLMs geven niet de feedback die de docent zelf zou geven.
- "Implementatie van nieuwe tools zoals OPAL, Schedule en Brightspace Creator Plus vormt grote belasting voor docenten naast onderwijs geven. Docenten moeten vele applicaties managen." (Windesheim, Geert van der Wijk, Product Owner-Educational Systems, 2026-08-19, parafrase) `Windesheim-02`
  - Stapel nieuwe tools drukt op docenten, elke extra tool is een adoptiedrempel.

**Schaal en organisatie van het beoordelen**
- "Het argument is dat er een medewerker in het taaldocenten team met pensioen gaat terwijl deze niet wordt vervangen. Daarnaast is er een grotere instroom dus moet er ook meer werk worden geleverd. Eduface kan de uitkomst zijn." (Haagse Hogeschool, 2026-04-24, parafrase) `Haagse-Hogeschool-30`
  - Krimpend docententeam plus grotere instroom is het interne argument voor aankoop.

**Consistentie en kwaliteit van feedback**
- "Geert beaamt dat inconsistentie begrijpelijk is omdat elke docent anders feedback geeft en docenten beoordeling verschillend invullen." (Windesheim, Geert van der Wijk, Product Owner-Educational Systems, 2026-09-09, parafrase) `Windesheim-07`
  - Inconsistentie tussen beoordelaars wordt erkend als kernpijn.

**Accuratesse en modelkwaliteit**
- "Drie studenten vonden de feedback te omvangrijk, te veel tekst. Vijf studenten zeiden dat de feedback in de comments niet in overeenstemming was met de algemene feedback. Twee studenten merkten op dat de formulering van het model zelf ook niet foutloos is." (Haagse Hogeschool, Maartje Sijm, Docent IVK, lid AI-sleutelteam lectoraat, 2026-04-14, letterlijk) `Haagse-Hogeschool-24`
  - Studenten melden te veel tekst, tegenstrijdige feedback en taalfouten van het model zelf.

**LMS en IT-landschap**
- "Wel zag ik dat het model nu aan zal staan vanaf 9.15 tot ergens in de avond. De docenten starten hier een stuk vroeger met de eerste assessments in de ochtend." (UMCG, Marin Groothengel, 2026-07-16, letterlijk) `UMCG-05`
  - Beschikbaarheidsvenster van de tool sluit niet aan op wanneer docenten echt beoordelen.

**Taal en meertaligheid**
- "Docenten beoordelen werkstukken en antwoorden op tentamenvragen doorgaans vooral op inhoud en geven vaak geen feedback op taalvaardigheid. Docenten zelf vinden dat ze daar te weinig tijd en expertise voor hebben." (Haagse Hogeschool, Maartje Sijm, Docent IVK, lid AI-sleutelteam lectoraat, 2026-01-30, letterlijk) `Haagse-Hogeschool-12`
  - Prospect onderbouwt met literatuur dat feedback op taal wegvalt door tijd en expertise.


### UK en Ierland (11)

**Consistentie en kwaliteit van feedback**
- "Consistency and standardization in feedback between multiple markers is a significant issue. Variation in marking and feedback quality between different tutors marking the same cohort affects student experience negatively." (University of Sunderland in London, Erika Keizere, Senior Lecturer (Academic Development - Digital Learning and Pedagogy), 2026-04-30, parafrase) `University-of-Sunderland-in-London-1`
  - Verschil tussen markers binnen een cohort is hun grootste klacht.
- "The institute corrects approximately 1,000 assignments per year across approximately 200 students. Manual assessment is time-consuming and requires consistent feedback quality across 20+ teaching staff members." (CMI - Communications & Management Institute (IE), John O'Toole, Founder & Managing Director, 2026-07-24, parafrase) `CMI-Communications-Management-Institute-IE-2`
  - 1.000 opdrachten per jaar, consistentie over 20+ losse docenten is het probleem.
- "Feedbackconsistentie: consistentere feedback tussen meerdere markers en tussen verschillende vakken." (Bristol University, Julio Hermosilla Elgueta, Senior Digital Education Developer, 2026-08-07, parafrase) `Bristol-University-1`
  - Consistentie tussen markers en tussen vakken is hun eerste prioriteit.

**Moment en snelheid van feedback**
- "High staff workload due to marking volume creates delays in assessment turnaround and feedback provision." (University of Sunderland in London, Erika Keizere, Senior Lecturer (Academic Development - Digital Learning and Pedagogy), 2026-04-30, parafrase) `University-of-Sunderland-in-London-2`
  - Nakijkvolume vertraagt de doorlooptijd van feedback.
- "De huidige nakijktermijn is twee weken; ze willen mogelijk naar een week. Dit verhoogt de druk op teaching assistants." (Bristol University, Julio Hermosilla Elgueta, Senior Digital Education Developer, 2026-08-07, parafrase) `Bristol-University-5`
  - Van twee weken naar een week nakijken drukt op de TA's.

**Besluitvorming en examencommissie**
- "if we are able to make a compelling business case, showing that lecturers are currently in a negative situation, there would be possibilities to set up a pilot. Case studies should be included in that document." (University of Sunderland in London, Erika Keizere, Senior Lecturer (Academic Development - Digital Learning and Pedagogy), 2026-06-08, letterlijk) `University-of-Sunderland-in-London-11`
  - Een business case met case studies opent de deur ondanks het beleid.

**Vertrouwen en weerstand bij docenten**
- "Staff at Bath Spa are time-poor and under pressure, making steep learning curves a barrier to adoption. The university continuously adds new systems, creating additional burden on staff unless clear time benefits are demonstrated." (Bath Spa University, 2026-07-16, parafrase) `Bath-Spa-University-50`
  - Elk nieuw systeem is extra last tenzij de tijdwinst meteen zichtbaar is.

**Nakijklast en werkdruk**
- "I can mark all the other ones first (NP3-NP7) which will take me a few days with all the other things I've got on." (Bath Spa University, Nicholas Peatfield, 2026-05-07, letterlijk) `Bath-Spa-University-37`
  - Nakijken schuift tussen al het andere werk door; dagen doorlooptijd per set.

**LMS en IT-landschap**
- "Dit heeft ook nog geen integratie met Canvas en geen mogelijkheden om formatieve feedback mee te nemen." (Queens University Belfast, Judy Williams, Pro Vice Chancellor Education and Students, 2026-04-30, letterlijk) `Queens-University-Belfast-6`
  - Eigen tool mist Canvas-integratie en formatief gebruik.

**Bestaande tools, zelf bouwen en alternatieven**
- "Gets to a point where I can only play with it for so long. Getting this automated on Eduface would further improve the process efficiency-wise, but I cant get it to that point on my own." (CMS Vocational Training, Gareth Luke, 2026-02-13, letterlijk) `CMS-Vocational-Training-09`
  - Zijn eigen bouwsel loopt vast, hij komt er alleen niet verder mee.

**Privacy, compliance en inkoop**
- "No BSU-approved AI tool for assessment/feedback exists yet; unmanaged AI use by staff risks academic standards, data protection, and policy/Student T&C violations." (Bath Spa University, 2026-09-10, parafrase) `Bath-Spa-University-58`
  - De echte driver is governance: docenten gebruiken al AI, zonder goedgekeurde route.


### Overig internationaal (5)

**Nakijklast en werkdruk**
- "Our main challenge is that professors typically have only a few weeks to grade a large number of these projects, each of them being quite extensive. These are usually lengthy submissions, often over 100 pages." (UADE, Lucas Cortinez, Digital education and innovation manager, 2026-03-16, letterlijk) `UADE-05`
  - Eindprojecten van 100+ pagina's moeten in enkele weken nagekeken worden.
- "UTI instructors spend two to four hours daily on manual grading of short-answer questions in lab documents." (Universal Technical Institute, Robert Jordan, Associate Vice President of Instructional Design, 2026-08-26, parafrase) `Universal-Technical-Institute-01`
  - Instructeurs kwijt 2 tot 4 uur per dag aan handmatig nakijken van labs.
- "UTI instructors face long teaching hours (8-10 hours daily) followed by 3-4 hours of grading. UTI instructor shortage is exacerbated by industry pay rates exceeding teaching compensation, making workload reduction critical for recruitment and retention." (Universal Technical Institute, Robert Jordan, Associate Vice President of Instructional Design, 2026-09-01, parafrase) `Universal-Technical-Institute-08`
  - Nakijklast bovenop lange lesdagen drijft instructeurs weg, werving is het knelpunt.

**Buiten de huidige scope**
- "Filippo highlighted the absence of learning analytics from current AI tools, making it difficult to identify which topics students struggle with or need clarification." (University of Ferrara, Filippo Carnevali, Ufficio Digital Learning, 2026-07-10, parafrase) `University-of-Ferrara-05`
  - Ze missen zicht op waar studenten vastlopen, dat is zijn eigen haakje.

**Consistentie en kwaliteit van feedback**
- "Students currently upload fillable PDF lab documents to Blackboard and receive minimal written feedback." (Universal Technical Institute, Robert Jordan, Associate Vice President of Instructional Design, 2026-08-26, parafrase) `Universal-Technical-Institute-03`
  - Studenten krijgen nu nauwelijks geschreven feedback terug op hun labs.
