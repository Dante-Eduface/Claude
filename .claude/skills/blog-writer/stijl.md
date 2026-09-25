# De Eduface-blogstem

_Opgesteld 25-09-2026, dezelfde dag gekalibreerd op de volledige tekst van de vier blogs die Dante als beste aanwees. Die staan letterlijk in `referentie/`. Lees bij twijfel de referentie zelf, niet alleen deze samenvatting._

| Blog | Type | Woorden | H2's | FAQ | Wat je er vooral uit leert |
|---|---|---|---|---|---|
| `referentie/ai-grading-tools-higher-education-guide.md` | koopgids | 4.763 (18 min) | 13 | 9 | eerlijk over concurrenten, eigen test met opzet en beperkingen, per tool een oordeel in de kop |
| `referentie/ai-essay-grader-canvas-lms-lti.md` | integratie | 1.758 (8 min) | 7 | 5 | stappen in de menunamen van Canvas, SpeedGrader-vraag beantwoord |
| `referentie/ai-essay-grader-moodle-lti.md` | integratie, hub | 1.528 (8 min) | 7 | 5 | een stelling innemen ("not a plugin") en onderbouwen, callout voor IT |
| `referentie/eu-ai-act-higher-education-assessment.md` | regelgeving | 2.082 (7 min) | 8 | 5 | eerst de wet met artikelnummers, dan wat de instelling moet, dan pas Eduface |

**De referenties zijn een stijlvoorbeeld, geen feitenbron.** Ze bevatten een verouderde deadline en claims die niet in `Platform/product.md` staan. Zie "Wat je niet overneemt" onderaan.

## De stem in zes zinnen

1. **Je schrijft als de collega die het al heeft uitgezocht.** De koopgids zegt het zelf: voor wie het landschap wil begrijpen "without being sold to".
2. **Eerst het antwoord, dan de uitleg.** Elke pagina heeft een antwoordblok bovenaan, en elke sectie opent met een zin die los klopt.
3. **Getallen en details dragen het argument.** Niet "ChatGPT is te mild", wel "On the 6.5 case study it returned 8.1, praising the exact section the lecturer flagged as weakest."
4. **Een stelling durven innemen.** "Eduface is not a Moodle plugin." "The human oversight requirement is structural, not optional."
5. **Eerlijk over de grens, met een eigen kopje.** "Limitations", "What it doesn't do", "What the research does not tell us yet", "Best use: ... Not for ...". Die eerlijkheid maakt de rest geloofwaardig.
6. **Hun woorden, niet de onze.** Developer Keys en SpeedGrader bij Canvas, External Tools en Site Administration bij Moodle, DVC en compliance lead bij de AI Act.

## Anatomie van een pagina

Zo zijn alle vier gebouwd. `blog-builder` kan elk onderdeel renderen.

| # | Onderdeel | Hoe het er in de referenties uitziet | blog-builder |
|---|---|---|---|
| 1 | **Eyebrow** | `CANVAS · LTI 1.3`, `AI GRADING TOOLS · 2026 GUIDE`. Onderwerp · subonderwerp, hoofdletters. | `hero.eyebrow` |
| 2 | **H1** | Hoofdterm vooraan, dan dubbele punt en de reikwijdte. "AI Essay Grader for Moodle: Grading, Feedback and Oral Exams via LTI 1.3". Title Case. Mag lang. | `hero.h1` |
| 3 | **Dek** | Eén of twee zinnen: wat het is, plus de kernbelofte. Werkt ook als meta description. | `hero.subtitle` |
| 4 | **Byline** | "By Eduface · June 2026 · 8 min read". De AI Act-blog voegt de lezer toe: "Written for HE compliance leads & DVCs". Doe dat altijd. | `hero.meta` |
| 5 | **Openingsscène** | Twee tot vijf korte zinnen in de tweede persoon die de situatie van de lezer schetsen, en een slotzin met spanning. Zie hieronder. | `p` |
| 6 | **Antwoordblok** | De hoofdvraag letterlijk als titel, daaronder 60 tot 90 woorden direct antwoord met Eduface, het LMS of de wet bij naam. In de gids: "Quick answer for busy readers". | `callout` |
| 7 | **H2's als vragen** | De vragen die de lezer echt stelt, met de entiteit erin: "How does Eduface connect to Canvas via LTI 1.3?", "What obligations does high-risk classification create for institutions?". De gids gebruikt stellingen ("Why this guide exists", "How we tested"); dat mag bij een lang, verhalend stuk. | `h2` |
| 8 | **Visueel blok per 2 à 3 secties** | Flowdiagram met onderschrift, tabel, figuur met "Figure N:"-onderschrift, genummerde stappen met vetgedrukt begin. | `img`, `table`, `p` met runs |
| 9 | **Callouts** | Kort, met een label: "For IT and learning technology teams", "Compliance risk:", "Why this matters", "What to check when evaluating a tool", "Compliance note". Eén gedachte per callout. | `callout` |
| 10 | **Vergelijkingstabel** | Aan het eind van het inhoudelijke deel: alle opties op dezelfde kolommen. In de LMS-pagina's met kolommen "When the lecturer approves" en "Grade passback". | `table` (max 4 à 5 kolommen fluid) |
| 11 | **FAQ** | Vijf vragen (negen in de gids), geformuleerd zoals iemand ze intypt: "Does Canvas have a built-in AI grader?", "Does Eduface work with Moodle 4.x?". Antwoord begint met "Yes." of "No." of de directe stelling, drie tot vijf zinnen, noemt de entiteit opnieuw. | `pb` + `p` |
| 12 | **Slot** | Regelgeving en gids: een eigen slot-H2 met een stelling ("Compliance is not optional, but it is achievable") of vetgedrukte lessen ("Where AI grading is heading"). Integratiepagina's eindigen op de FAQ. | `h2` + `p` |
| 13 | **CTA-blok** | "Talk to Eduface about [onderwerp]" + één zin + "Request a demo". De standaard-CTA bouwt `blog-builder` zelf; schrijf alleen een eigen titel en zin als het onderwerp erom vraagt. | CTA-sectie |
| 14 | **References** | Genummerd, APA-achtig, met tussen haken de kernbevinding: "[Key finding: only 23% of institutions ...]". In de tekst een superscript ¹ bij het feit. | `h2` + `p` |

## Openingsscène: drie werkende varianten

**De herkenbare situatie** (Canvas):
> "Your institution has Canvas. Lecturers are spending hours marking the same type of essay, week after week. Students are waiting days for feedback that arrives too late to improve their next draft. [...] That pressure is real, and it is arriving at institutions across the UK and Ireland right now."

**Het scenario dat vastloopt** (AI Act):
> "A new AI tool arrives on your institution's radar. A department wants to pilot it for essay marking. Your legal or compliance team asks whether it falls under the EU AI Act. You ask your Learning Technologist, who checks with IT, and nobody quite knows the answer."

**De vraag die iedereen stelt, en het verrassende antwoord** (Moodle):
> "When a learning technologist is asked to find an AI assessment tool that works inside Moodle, the first question is almost always the same: is there an AI grading plugin for Moodle? The short answer is that the most capable AI assessment tools do not work as Moodle plugins at all."

Een reeks korte zinnen mag **alleen hier**, om een situatie neer te zetten. In de rest van de tekst wisselt de zinslengte.

## Patronen op zinsniveau

**Definitie-opener onder een kop.** "LTI 1.3 (Learning Tools Interoperability) is the standard protocol that allows external applications to embed securely inside a learning management system."

**De stelling, dan de uitwerking in twee alinea's die elkaar spiegelen.** Moodle: "A Moodle plugin lives inside the Moodle codebase. [...]" tegenover "An LTI 1.3 External Tool lives entirely outside Moodle. [...]"

**Het korte oordeel na de feiten**, vaak met "That is" of "This":
- "That is not a minor calibration issue."
- "That is an actively harmful outcome."
- "This distinction matters more than it might initially seem."

**Contrast in één zin, met dubbele punt of puntkomma:**
- "High-risk classification does not prohibit use: it requires institutions and tool providers to meet obligations around human oversight, transparency, and accountability."
- "The individual observations were right; the aggregated academic judgment was not."

**"X, not Y" als afsluiter.** "Request documentation, not just assurances." "Requirements to verify, not features to consider." Sterk, maar hoogstens één per sectie. De referenties gebruiken hem vaak; bij elke alinea wordt het een tic.

**Vetgedrukt begin voor lijsten van gelijksoortige punten.** "**Training data.** Was the model trained on academic assessments or on general internet text?" Zo zijn ook de stappen, de lessen en de leveranciersvragen gebouwd ("**On accuracy:** ...").

**Het concrete detail uit de praktijk.** "correctly spotted the missing bridging sentence, the inconsistent heading numbering, and a conclusion that did not answer the research question". Zo'n opsomming van echte observaties overtuigt meer dan elk bijvoeglijk naamwoord.

**Per item dezelfde opbouw.** Elke tool in de gids: kop met naam en oordeel ("ChatGPT: fluent but overgenerous"), dan "Grade accuracy: ..." met het getal, dan wat hij goed doet, dan waar hij faalt, dan "**Best use:** ... Not for ...".

**Eduface over zichzelf, met de eigen positie erbij.** "We are Eduface, an AI grading platform for higher education, and we have a position in this market. [...] Where a competitor does something better than us, we say so." En bij Eduface zelf een "**What it doesn't do:**"-regel.

## Taal en register

- **Brits Engels, consequent.** judgement (de gids schrijft soms "judgment", niet overnemen), behaviour, licence, programme, scrutinised, sceptical, personalised, rigour.
- **Grading en marking** staan allebei in de referenties. Titel en H1 volgen de zoekterm (meestal "grading"), de lopende tekst mag "marking" gebruiken voor de UK-lezer.
- **Rollen bij naam:** lecturer, learning technologist, programme director, compliance lead, DVC, marker, assessor.
- **"You" en "your institution"** voor de lezer. **"We"** alleen als Eduface iets doet, test of toegeeft.
- **Zinslengte** gemiddeld 15 tot 22 woorden, met korte oordeelszinnen ertussen. Alinea's van twee tot vier zinnen.
- **Geen em-dashes.** De referenties gebruiken ze niet in de lopende tekst; houd dat zo.

## Hoe Eduface in de tekst staat

- **Niet in de openingsscène.** Wel mag Eduface in het antwoordblok staan als de vraag over Eduface zelf gaat (integratiepagina's). Bij regelgeving en de gids komt Eduface pas na de uitleg.
- **Na het principe, niet ervoor.** AI Act: eerst wat art. 14 eist, dan "How does Eduface meet the EU AI Act requirements?" met een tabel verplichting, eis, Eduface-aanpak.
- **Het mechanisme, niet het bijvoeglijk naamwoord.** "The suggested grade is held in draft. It is not visible to the student, and it is not recorded anywhere, until the lecturer [...] explicitly clicks to approve." Geen "secure", "powerful", "seamless".
- **Kernzin als het om toezicht gaat:** "The AI assists. The academic decides." (uit `product.md`).
- **Elke productclaim uit `Platform/product.md`.** Ook als het al op een live blog staat.

## Wat je niet overneemt uit de referenties

De referenties zijn sterk in stem en opbouw en zwak op een paar punten. Deze fouten niet kopiëren:

**1. Verouderde en te stellige regelgeving**
- **"August 2026" als deadline voor hoog-risico.** Sinds de Digital Omnibus (in werking 27-07-2026) is dat **2 december 2027** voor Bijlage III. Staat in de AI Act-blog en in de gids.
- **"Tools that don't meet these cannot legally be deployed"** en "automated decisions without review are prohibited": stelliger dan de wettekst. Schrijf wat de wet eist, niet wat eruit zou volgen.
- **Art. 13 als plicht richting studenten.** Art. 13 regelt transparantie van de aanbieder naar de gebruiker (de instelling). Het informeren van studenten valt onder de plichten van de gebruiksverantwoordelijke (art. 26, lid 11) en het recht op uitleg (art. 86). Toets elk artikelnummer in de wettekst voor je het koppelt aan een plicht.
- **De Brexit-FAQ** ("any tool provided by an EU-based company [...] falls within scope") is juridisch te kort door de bocht. Laat zo'n antwoord toetsen of formuleer het voorzichtiger.

**2. Onderzoekscijfers zonder bron.** In de gids staan "Research from 2025 and 2026 shows [...] 85-92%", "A May 2026 study", "A 2025 study found only 35%" zonder bronvermelding. Wij noemen bij elk extern cijfer auteur, titel en jaar, en de gids heeft geen References-sectie. Onze artikelen wel, altijd.

**3. Opvulling in de References.** In de AI Act-blog staan Hattie & Timperley en UCU 2016 wel in de lijst maar nergens in de tekst. Elke referentie moet een feit in de tekst dragen.

**4. Productclaims: sinds 25-09-2026 bevestigd.** Dante bevestigde dat de claims in de referenties kloppen; ze staan nu in `Platform/product.md` (onderaan). Twee aandachtspunten blijven:
- **"The Feedback Tool" niet als losse module noemen.** Formatieve feedback is onderdeel van de Paper Grader (`product.md`, 08-09-2026). Schrijf "the Paper Grader's formative feedback".
- **Twee maten, nooit door elkaar.** "Lecturers changed an average of 5% of each final grade" (UK-pilots) is iets anders dan de 94% accuraatheid uit de Bath Spa-meting. Zeg bij elk getal welke maat het is.
- "5,000+ lecturers" kwam alleen uit zoekresultaten, niet uit de geplakte tekst. Niet gebruiken tot bevestigd.

**5. Kleine stijlglippers.** "Crucially," (Canvas) en "genuinely" (Canvas) staan op onze schraplijst. "Moodle Gradebook" en "Canvas gradebook" wisselend met en zonder hoofdletter: volg de schrijfwijze van het LMS zelf.

## Wat nooit

- **AI-tells:** delve, landscape, crucial(ly), pivotal, transformative, seamless, robust, leverage, navigate, realm, foster, holistic, empower, unlock, game-changer, cutting-edge, genuinely, "it's worth noting", "in today's fast-paced", "it's not just X, it's Y", een slotalinea die alles samenvat. Volledige lijst en onderbouwing in `seo-geo.md`.
- **Komma-treinen** van 40+ woorden. De oudere concepten in `GTM/Campaigns/blog-launch/markdown-sources/` (juli 2026) doen dat vaak, met "genuinely" tot drie keer per alinea. Dat zijn geen stijlvoorbeelden.
- **Hype:** revolutionary, game-changing, cutting-edge.
- **Een getal zonder context of bron.**
- **Angst als hefboom.** "Compliance risk:" als feitelijke waarschuwing mag; "institutions that don't act will fall behind" niet.
