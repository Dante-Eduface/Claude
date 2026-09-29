# Briefing: RFP-radar voor een AI-beoordelingsplatform (Eduface)

Je onderzoekt één deelvraag (regio) voor een groter onderzoek. Je rapport gaat naar een orkestrator, niet naar een mens. Lever data, geen verhaal.

## Wat we zoeken
Openbare aanbestedingen / RFP / RFQ / ITT / tenders / framework-agreements / dynamic purchasing systems / prior-information-notices (vooraankondigingen) / contract award notices voor een oplossing zoals Eduface: een AI-platform dat docenten helpt bij **beoordelen en feedback** in het hoger onderwijs (papers en tentamens nakijken op schaal, rubric-scoring, feedback per concept, mondeling toetsen/oral exams met realtime transcriptie, academic integrity via mondelinge verantwoording). Koppelt aan LMS (Moodle, Blackboard, Brightspace, Canvas). Docent keurt elke uitkomst goed.

## Wie telt als koper
Universiteiten, hogescholen, colleges (HE en FE/tertiary/TAFE/community colleges), inkoopconsortia en frameworks voor onderwijs, ministeries/onderwijsagentschappen die voor instellingen inkopen, private/professionele opleiders en examen-/certificeringsorganisaties (awarding bodies, exam boards, professional bodies). K-12/basis- en middelbaar onderwijs is buiten ICP: zoek er niet gericht naar, maar noteer wat je toevallig tegenkomt met label OUT-OF-ICP.

## Tijdvak
Alle aanbestedingen gepubliceerd vanaf 2024-01-01 tot vandaag (2026-09-29), plus alles wat nog open staat ongeacht publicatiedatum, plus vooraankondigingen/geplande tenders. Afgesloten en gegunde tenders zijn welkom als marktbewijs (wie kocht wat, van wie, voor hoeveel), maar OPEN en UPCOMING zijn de prioriteit.

## Relevantieladder (label elk item)
- **A** = expliciet AI/automated/machine-assisted marking, grading, scoring of feedback
- **B** = digitale toets-/e-marking-/assessment-/exam-platform waarvan de scope AI-nakijken kan omvatten of waar Eduface op kan inschrijven
- **C** = aangrenzend (academic integrity/plagiarisme, oral assessment, proctoring, LMS/VLE) MAAR ALLEEN als de scope-tekst assessment, marking, feedback of AI noemt. Kale LMS/VLE-tenders zonder assessment-scope niet opnemen.
- **OUT-OF-ICP** = K-12 of anders niet-passend, alleen noteren als je het toevallig zag.

## Zoekvocabulaire (gebruik ALLE relevante varianten, in de taal van het land, en stel bij op woorden die de bronnen zelf gebruiken)
EN: AI marking, AI grading, automated marking, automated grading, e-marking, on-screen marking, computer-assisted assessment, digital assessment, digital examination, online exams, assessment platform, feedback platform, formative feedback, summative assessment, essay scoring, rubric, oral examination, viva, academic integrity, authentic assessment, generative AI assessment, learning analytics, EdTech framework, Dynamic Purchasing System, digital learning, VLE/LMS assessment tools, question bank, exam management, e-assessment, proctoring, plagiarism detection, similarity detection.
NL: digitaal toetsen, digitale toetsing, toetsplatform, toetssoftware, nakijken, beoordelen, AI-beoordeling, e-assessment, tentamensoftware, examinering, mondeling tentamen, fraudepreventie, plagiaatdetectie, aanbesteding, uitvraag, inschrijving, gunning.
CPV-codes (EU/UK/IE/MT/NL/BE en TED/Find a Tender): 48190000 (educational software package), 48000000, 72212190, 72261000, 80420000 (e-learning), 80000000, 80500000, 80530000, 72000000 (IT services), 48311000, 48517000 (IT-specific software), en UNSPSC 43232xxx / 86xxxxxx voor US/CA/AU.
Vendors die in gunningen opduiken (zoek ook op hun naam + "contract award"/"tender"/"notice"): Turnitin, Gradescope, Cadmus, FeedbackFruits, Graide, WISEflow/UNIwise, Inspera, Cirrus/Learnosity, Möbius, Ans, TestReach, Digiexam, Examity, ProctorU, Respondus, Exam.net, Hypergrade, CoGrader, Learnwise, Kritik, Marking.ai, Cerego, Codio, Pearson, Cambridge Assessment, RM Assessment, Emarking.

## Hoe je werkt
1. Begin met 2 tot 4 zoekopdrachten tegelijk, met verschillende formuleringen. Niet één query en dan stoppen.
2. Lees de resultaten en **stel je zoektermen bij** op de woorden die de bronnen zelf gebruiken. De eerste zoekterm is bijna nooit de goede.
3. **Open de bronnen echt.** Een zoekresultaat-snippet is geen bron. Fetch de tenderpagina/notice en lees scope, deadline, waarde, koper. Citeer nooit op basis van een titel of snippet. Een item dat je alleen als snippet zag krijgt Verified=nee en gaat in de aparte lijst "onbevestigd".
4. Loopt een bron vast (403, loginmuur, JS-only), probeer curl (via Bash) met een browser-User-Agent, een andere URL-vorm (bijv. de API- of RSS-variant, `site:`-zoekopdracht op de portal-domeinnaam), een aggregator die dezelfde notice spiegelt, of TED/Find a Tender/Contracts Finder als bron-van-waarheid. Pas daarna: "niet toegankelijk" met vermelding wat je probeerde. HTTPS gaat via de vooraf geconfigureerde proxy; zet nooit TLS-verificatie uit.
5. Zoek zowel via de webzoekmachine (WebSearch, US-only, dus vooral bruikbaar om URL's te vinden) als door portalen direct te bevragen (WebFetch/curl op zoek-URL's en publieke API's als die bestaan). Doorzoek per land ook de eigen inkoop-/tenderpagina van instellingen (bijv. "university X tenders", "procurement opportunities", "current tenders") voor de grotere instellingen, want veel universiteiten publiceren daar los van de nationale portalen.
6. Ga door tot nieuwe zoekopdrachten niks nieuws meer opleveren. Dan ben je klaar. Dekking telt meer dan snelheid: de opdrachtgever wil GEEN enkele relevante tender missen.

## Harde regels
- Elke claim krijgt een **URL en een jaartal**. Geen jaartal betekent geen claim.
- Kun je iets niet vinden: schrijf letterlijk "niet publiek vindbaar". Nooit invullen of afleiden zonder label INFERENTIE.
- Label per bron het type: **primair** (de notice zelf op de officiële portal, wetgeving), **secundair** (journalistiek, onafhankelijke aggregator), **tertiair** (blog, vendorcontent).
- Noem wie de bron publiceerde als dat uitmaakt (een aggregator die tenders doorverkoopt heeft belang bij clicks).
- Vind je iets dat de aanname ondergraaft (bijv. dat er expliciete AI-grading-tenders bestaan), rapporteer dat prominent.
- Wees eerlijk over onzekerheid. Bekende-onbekenden (portalen die je niet kon doorzoeken) horen in je rapport, want de opdrachtgever wil weten waar het overzicht gaten heeft.
- Bewaar je volledige register ook als bestand in de map /tmp/claude-0/-home-user-Claude/1b2b48ce-cbf1-5659-8b2c-d2393bc3d004/scratchpad/rfp/ met bestandsnaam `<regio-code>.md` (bijv. `uk1.md`), zodat het niet verloren gaat.

## Wat je teruggeeft (dit vervangt het generieke format van de subagent-prompt)
Alleen dit, geen inleiding en geen procesverslag:

**Antwoord:** 2 tot 5 bullets: hoeveel relevante tenders in jouw regio, hoeveel open/upcoming, wat valt op.

**Register (verifieerd, dus notice zelf geopend):** één regel per tender, pijpteken-gescheiden:
`Land | Koper | Titel | Referentie/ID | URL | Status (OPEN/UPCOMING/CLOSED/AWARDED) | Gepubliceerd | Deadline | Waarde | Winnaar | Relevantie (A/B/C) | Toelichting in max 15 woorden`

**Onbevestigd:** dezelfde regel, maar alleen gezien in snippet of via secundaire bron, niet zelf geopend, met reden.

**Dekking:** lijst van portalen/bronnen die je WEL doorzocht (met zoektermen) en lijst die je NIET kon bereiken (met reden: login, blokkade, JS-only). Dit is even belangrijk als het register.

**Tegenspraak:** bronnen die elkaar tegenspreken, allebei genoemd.

**Niet gevonden:** wat je zocht en niet vond, met de gebruikte zoektermen.
