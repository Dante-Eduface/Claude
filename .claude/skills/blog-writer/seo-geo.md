# SEO en GEO: wat werkt, wat niet

_Opgesteld 25-09-2026 uit zes parallelle onderzoekslijnen plus een tegenspraakronde. Volledig verslag met alle bronnen: `Platform/Onderzoek/seo-geo-blogschrijven.md`. Hier staan alleen de regels._

## De drie dingen die je moet weten voor je iets optimaliseert

1. **Voor Google is GEO gewoon SEO.** Google's eigen AI-optimalisatiegids (15-05-2026) zegt het letterlijk: geen llms.txt nodig, geen chunking, geen speciale schema, geen AI-specifieke herschrijvingen. De AI-functies van Google draaien op de gewone zoekindex. Wat niet rankt, wordt ook niet opgehaald.
2. **De bekende GEO-trucs houden niet stand.** Het GEO-paper (Aggarwal et al., KDD 2024) vond +30 tot 40% door statistieken, citaten en bronvermelding toe te voegen, maar in een nagebootste opzet. De replicatie onder echte omstandigheden (C-SEO Bench, NeurIPS 2025) vond in 3 van 54 combinaties een significant effect, en geen enkele bij vraag-en-antwoord. Of je in de set zit die het systeem ophaalt, weegt veel zwaarder dan hoe je formuleert.
3. **Blogs zijn niet de grootste hefboom voor AI-zichtbaarheid.** Vermeldingen van het merk op andere sites correleren het sterkst met zichtbaarheid in AI-antwoorden (Ahrefs, 75.000 merken: 0,664, backlinks 0,218, aantal eigen pagina's zwak). Meer blogs publiceren is dus niet vanzelf meer zichtbaarheid. Minder en beter wel.

Gevolg voor deze skill: **we schrijven het beste antwoord op een echte vraag, in een vorm die mensen én machines makkelijk kunnen lezen.** Dat is de hele strategie. De rest van dit bestand is de uitwerking.

## Welke artikelen je schrijft

- **Handelingsgerichte vragen boven definities.** Bij informatieve vragen ("what is AI grading") geeft de AI-samenvatting het antwoord en klikt bijna niemand door (Pew, juli 2025: klikratio 15% naar 8%, 1% klik op de bron in de samenvatting). Vergelijkingen, integratievragen, implementatie en regelgeving met een beslissing eraan houden hun waarde.
- **Bottom of funnel converteert het best.** Grow & Convert (bureau-eigen data, 2024-25): vergelijkings- en alternatievenzoektermen 8,4% bezoeker naar lead, "versus" 5,5%, algemene top-of-funnel onder 1%. Richting betrouwbaar, exacte cijfers niet onafhankelijk getoetst.
- **Eén sterke pagina per zoekintentie.** De reeks bijna-gelijke artikelen per LMS en per vak is het patroon dat Google's spambeleid "scaled content abuse" noemt ("many pages where the content is only slightly different"). Een nieuwe variant mag alleen als hij echt eigen inhoud heeft: eigen menu's en beperkingen van dat LMS, een eigen rubricvoorbeeld voor dat vak, eigen data. Anders: een sectie toevoegen aan de bestaande pagina.

## Per artikel: de regels die de tekst raken

Gerangschikt op bewijssterkte.

**Sterk bewijs**

1. **Information gain.** Elk artikel bevat iets dat een taalmodel niet zelf kan verzinnen: een eigen meting, een uitgewerkt voorbeeld, een testopzet, een checklist, een standpunt met naam. De koopgids met acht getoetste tools is het model. Google's rater-richtlijnen (januari 2025) geven de laagste score aan content die grotendeels AI-gegenereerd is en niets toevoegt.
2. **Tabellen voor vergelijkingen, stappen en tijdlijnen.** De enige gecontroleerde causale studie (CITECHOICE, 2026) vond dat gestructureerde weergave de citaties naar het doeldocument verhoogt (+0,50 per antwoord). Ook voor mensen de snelste manier om te vergelijken.
3. **Koppen die zelf de inhoud zeggen.** Lezers scannen de koppen (NN/g, layer-cake-patroon). Een kop als "What the EU AI Act says about grading" werkt. "Background" werkt niet.
4. **Het antwoord eerst.** Het antwoordblok direct na de openingsscène beantwoordt de hoofdvraag in 60 tot 90 woorden (zo doen alle vier de referentieblogs het), en elke H2 opent met een zin die op zichzelf klopt. 44% van de ChatGPT-citaties komt uit het eerste derde van de pagina (Kevin Indig, 18.012 citaties, 2026), en een lezer die zijn antwoord meteen ziet, blijft.
5. **Subvragen als eigen secties, geformuleerd als vraag.** De referentieblogs doen dit al: "How does Eduface connect to Canvas via LTI 1.3?", "Does Eduface work with Moodle 4.x?". AI Mode splitst een vraag op in deelvragen (query fan-out, bevestigd door Google). Een artikel dat de deelvragen die een koper echt heeft (kosten, integratie, compliance, accuraatheid, wie keurt goed) elk een eigen kop geeft, wordt op meer daarvan gevonden.

**Redelijk bewijs**

6. **Noem de entiteit bij naam in zinnen die los gelezen kunnen worden.** "Eduface returns the approved grade to the Moodle Gradebook", niet "it sends it back". Goed schrijven, en een passage die los wordt opgehaald blijft begrijpelijk. **Maar niet opknippen in kunstmatige blokjes:** Google zegt letterlijk dat het geen chunking wil. Schrijf gewone alinea's die elk één punt maken.
7. **Bronnen met naam en jaar.** Een getal met bron is geloofwaardiger voor de lezer en de enige GEO-tactiek die in elk onderzoek minstens niet schaadt. Primaire bronnen (de wettekst, Ofqual, HEPI) boven vendorblogs. Zie `bronnen.md`.
8. **Een echte auteur en een datum.** Byline, `datePublished`, en `dateModified` alleen bij een inhoudelijke update (zie Versheid).
9. **Titel met het onderwerp vooraan, onder de 60 tekens.** Google herschrijft de getoonde titel vaak (76% in Q1 2025), maar rankt op de echte. Formaat: `<Specifiek onderwerp>: <belofte> | Eduface`. Meta description 140 tot 160 tekens, het antwoord plus voor wie.
10. **Interne links met beschrijvende ankertekst.** Naar de hub van het cluster en naar één of twee zijartikelen, in de lopende tekst.

**Zwak bewijs, doe het omdat het niets kost**

11. **Slug kort en leesbaar**, hoofdterm erin, geen jaartal tenzij het artikel echt jaargebonden is (dan wel bijwerken).
12. **FAQ-sectie met vragen die de koppen niet al beantwoorden.** Niet voor rich results (FAQ rich results zijn sinds 07-05-2026 weg), wel omdat het echte vervolgvragen afvangt. Antwoord in 2 tot 4 zinnen, eerste zin is het antwoord.
13. **Geen tekst achter JavaScript.** AI-crawlers voeren geen JavaScript uit (Vercel/MERJ, 2024). Geen belangrijke tekst in accordeons of tabbladen die pas client-side laden.

## Wat je NIET doet, ook al staat het in elke GEO-gids

| Advies | Waarom niet |
|---|---|
| llms.txt | Google gebruikt het niet (Mueller, 2025). Gemeten: 0,1% van de AI-bezoeken vroeg het bestand op (OtterlyAI, 90 dagen). |
| Schema toevoegen "voor AI" | Geen effect op AI-citaties, in AI Overviews zelfs -4,6% (Ahrefs, 2026). Article, BreadcrumbList en Organization blijven als hygiëne, via `blog-builder`. |
| FAQ-schema voor rich results | Rich results bestaan niet meer (07-05-2026). |
| Statistieken of citaten toevoegen om het toevoegen | Replicatie mislukt (C-SEO Bench). Alleen als het getal het argument echt draagt. |
| Content opknippen in chunks | Google ontraadt het expliciet. |
| Aparte markdown-pagina's voor bots | Cloaking-risico (Google en Bing, 2026). |
| Keyword stuffing, zoekterm X keer herhalen | Negatief in het GEO-paper, en onleesbaar. |
| Woordtarget halen | Lengte is geen rankingfactor. Opvulling wordt afgestraft. |
| Veel publiceren om het publiceren | Publicatiefrequentie is geen signaal (Mueller). |
| "Updated 2026" zonder nieuwe inhoud | Misleiding. Werkt op korte termijn bij sommige LLM's (SIGIR 2025), wordt afgestraft zodra het opvalt. |

## Versheid

- Een artikel over regelgeving of tools heeft een houdbaarheidsdatum. Zet bij oplevering in de frontmatter wanneer het opnieuw getoetst moet worden (`review_by`).
- Update bij een echte verandering (nieuwe wetsdatum, nieuwe tool, nieuwe meting), en zet dan een zichtbare "Last updated"-regel plus wat er veranderd is.
- LLM-rerankers geven de voorkeur aan recente content (SIGIR-AP 2025), Perplexity het sterkst, Google AI Overviews het zwakst. Voor ons betekent dit: de artikelen over EU AI Act, Ofqual en tools elk half jaar toetsen.

## Menselijk klinken

Lezers die vermoeden dat een tekst door AI geschreven is, vertrouwen hem tot de helft minder (meerdere studies 2024-25). Voor een publiek van sceptische docenten die over AI-beoordeling lezen is dat fataal.

Schrappen bij de zelfcheck:

- **Woorden** (Kobak et al., Science Advances 2025, en de huisstijl): delve, landscape, crucial, pivotal, transformative, unparalleled, invaluable, seamless, robust, leverage, navigate, realm, tapestry, foster, holistic, empower, unlock, game-changer, cutting-edge, genuinely, "it's worth noting", "in today's fast-paced".
- **Constructies:** "It's not just X, it's Y." Reeksen van drie bijvoeglijke naamwoorden. Een retorische vraag als opener. Een slotalinea die alles samenvat ("In conclusion", "Ultimately"). Em-dashes.
- **Ritme:** geen drie korte zinnen achter elkaar, geen zinnen van 40+ woorden met vijf komma's.

## UK tegenover US

Primaire term volgt de zoekvraag. Voor de UK-markt meestal de linkerkolom.

| UK | US |
|---|---|
| marking | grading |
| coursework, assessment | assignment |
| module leader, lecturer | instructor, professor |
| VLE (LMS mag ook) | LMS |
| cohort | class |
| exam script | exam |
| mark scheme, rubric | rubric |
| programme | program |

Titels van bestaande pagina's gebruiken vaak "grading" omdat die term meer zoekvolume heeft, ook in de UK. Dat is prima; gebruik "marking" in de lopende tekst wanneer het artikel op de UK gericht is.

## Wat buiten het artikel ligt (niet deze skill, wel melden aan Dante)

Eenmalig op siteniveau, door wie de site beheert:
- robots.txt: OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot en Claude-User toelaten (die bepalen citaties). Of GPTBot en ClaudeBot (training) geweerd worden is een aparte keuze.
- Controleren dat Framer de blogpagina's als server-rendered HTML levert (curl op een blog-URL, tekst moet in de HTML staan).
- Bing Webmaster Tools plus IndexNow: ChatGPT-search leunt deels op de Bing-index.
- GA4: een eigen kanaalgroep voor AI-verwijzers (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai). Het ingebouwde kanaal mist Perplexity.
- Meten op aanwezigheid over veel prompts en op "hoe hoorde je van ons" in gesprekken, niet op "positie in ChatGPT". AI-aanbevelingen herhalen zich in minder dan 1% van de runs (SparkToro, januari 2026).
- Vermeldingen buiten de eigen site (G2 en Capterra, sites van instellingen, Jisc, conferenties, LinkedIn, YouTube) wegen zwaarder voor AI-zichtbaarheid dan nog een blog.
