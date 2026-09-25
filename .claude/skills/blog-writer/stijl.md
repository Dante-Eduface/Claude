# De Eduface-blogstem

_Opgesteld 25-09-2026 op basis van de vier blogs die Dante als beste aanwees. Kalibratiestatus onderaan: lees die eerst._

De vier referentieblogs:

| Blog | Type | Wat je er vooral uit leert |
|---|---|---|
| `/resources/blog/ai-grading-tools-higher-education-guide` | koopgids, vergelijking | eerlijk over concurrenten, getallen uit eigen test, per tool dezelfde opbouw |
| `/resources/blog/ai-essay-grader-canvas-lms-lti` | integratiepagina | stap voor stap hoe het werkt in hún systeem, in hún woorden (SpeedGrader, Developer Keys) |
| `/resources/blog/ai-essay-grader-moodle-lti` | integratiepagina, hub | een stelling durven innemen ("not a plugin") en die onderbouwen |
| `/resources/blog/eu-ai-act-higher-education-assessment` | regelgeving-uitlegger | eerst de wet uitleggen met artikelnummers, dan pas wat Eduface doet |

## De stem in vijf zinnen

1. **Je schrijft als de collega die het al heeft uitgezocht**, niet als verkoper. De koopgids zegt het zelf: geschreven voor wie het landschap wil begrijpen "without being sold to".
2. **Eerst het antwoord, dan de uitleg.** Elke sectie opent met een zin die op zichzelf klopt en citeerbaar is.
3. **Getallen dragen het argument.** Geen "aanzienlijk sneller", wel "on a 6.5 case study it returned 8.1".
4. **Een stelling durven innemen.** "Eduface is not a Moodle plugin." "Accuracy is the right question to ask first." Geen "it depends" zonder te zeggen waarvan.
5. **Eerlijk over de grens.** Waar een concurrent beter is, staat dat er. Waar AI iets niet kan, staat dat er. Dat is precies waarom de rest geloofd wordt.

## Patronen uit de referentieblogs (met voorbeeld)

De citaten hieronder zijn uit zoekresultaten gereconstrueerd, zie kalibratiestatus. Gebruik ze als patroon, kopieer ze niet.

**Definitie-opener.** De eerste zin onder een kop zegt wat iets is, met de eigennaam erin.
> "Eduface is not a Moodle plugin. It connects to Moodle as an External Tool using the LTI 1.3 standard."
> "Gradescope, owned by Turnitin, is the most widely deployed grading platform in higher education, and it is strong for STEM."

**Contrast in één zin.** Twee dingen naast elkaar, zodat de lezer het verschil in één keer ziet.
> "A model trained on general text responds to linguistic polish, whereas a model trained on academic assessments responds to disciplinary argument quality."
> "For exams with definitive answers this is powerful; for open-ended essays with nuanced criteria it is less applicable."

**Het korte oordeel na de uitleg.** Een alinea met feiten, dan één korte zin die zegt wat het betekent.
> "It responds to how well the student writes, not how well they reason."
> "Feedback that is faster but systematically wrong is worse than no change at all."

**De concrete meting.** Een getal met zijn context: wat, hoeveel, onder welke omstandigheden.
> "On a constitutional law essay (with a real grade of 4.4), it returned 7.1, a gap of 2.7 points."

**De workflow als één lopende zin.** Integratiestappen zo beschreven dat een learning technologist ze herkent.
> "Students submit via Moodle, LTI 1.3 routes the submission to Eduface, the lecturer approves the grade, and it returns automatically to the Moodle Gradebook."

**Hun woorden, niet de onze.** De Canvas-blog praat over SpeedGrader en Developer Keys, de Moodle-blog over External Tools, Assignment activities en de Gradebook. Een lezer die zijn eigen menu terugziet, vertrouwt de rest.

**De docent beslist, altijd expliciet.** Niet als disclaimer onderaan, maar als mechanisme in de tekst.
> "Grades never reach students automatically. The lecturer sees the AI suggestions, can edit any score or comment, and releases grades only when satisfied."

**Per item dezelfde opbouw.** In de koopgids krijgt elke tool: wat hij goed doet, waar hij tekortschiet, waarvoor je hem wel en niet gebruikt. Vaste volgorde maakt vergelijken makkelijk, voor mensen en voor een AI die een tabel wil maken.

**Een zelfbewuste nuance over het eigen soort product.**
> "Free and freemium LTI tools are useful for individual lecturers ... However, they are generally not suitable for summative assessment at institutional scale, because the audit trail, the data processing terms and the support model are not built for it."

## Taal en register

- **Brits Engels.** marking, programme, organisation, personalised, judgement, sceptical. Doelmarkt is primair UK.
- **UK- en US-termen bewust kiezen.** Primaire term volgt de zoekvraag. Grading en marking allebei gebruiken is prima, maar per artikel één als hoofdterm. Zie de tabel in `seo-geo.md`.
- **Instellingswoorden:** lecturer, module leader, programme director, learning technologist, assessor, marker, cohort, VLE of LMS, gradebook, rubric of mark scheme.
- **"We" voor Eduface** alleen waar Eduface iets doet of test. De lezer is "you" of de rol ("the lecturer", "your learning technologist").
- **Zinslengte gevarieerd.** Gemiddeld 15 tot 20 woorden, met af en toe een korte zin als oordeel. Geen reeksen van drie korte zinnen achter elkaar.
- **Alinea's van twee tot vier zinnen.** Een alinea die op een scherm langer is dan zes regels, splitsen.
- **Geen em-dashes.** Komma, punt, dubbele punt of een nieuwe zin. Huisstijl, en een bekende AI-tell.

## Hoe Eduface in de tekst staat

- **Niet in de opening.** De eerste twee alinea's gaan over het probleem van de lezer. Eduface komt pas in beeld als het antwoord op iets dat al uitgelegd is.
- **Als voorbeeld van een principe, niet als claim los in de lucht.** Eerst "wat moet een goede tool doen", dan "zo doet Eduface het".
- **Hoogstens één productsectie** per artikel, plus de CTA. In een koopgids mag Eduface een van de profielen zijn, met dezelfde eerlijke opbouw als de rest.
- **Kernzin die altijd mag:** "The AI assists. The academic decides." Niet in elk artikel, wel als het om toezicht gaat.
- **Elke productclaim komt uit `Platform/product.md`.** Staat het daar niet, dan schrijf je het niet, ook niet als het al op een andere blog staat. Zie de lijst hieronder.

### Claims die op de live blogs staan maar NIET in `product.md`

Gevonden op 25-09-2026. Niet gebruiken tot Dante ze bevestigt (staat als W7 in `Context/open-vragen.md`):

- "used by 5,000+ lecturers"
- "Jisc-approved" en "approved supplier on the Jisc/CHEST framework"
- "±0.15 average deviation from lecturer grades"
- "markers changed on average just 5% of each AI grade"
- "proprietary GPU infrastructure in the Netherlands"
- een losse "Feedback Tool" als vierde module (volgens `product.md` bestaat die sinds 08-09-2026 niet los, dat is de Paper Grader)
- "blind mode" en "AI-visible mode"
- "A Data Processing Agreement is available on request"

Wel toegestaan en sterk: de Bath Spa-meting zoals `product.md` hem formuleert (435 submissions, 13 markers, gemiddeld 94% accuraatheid, 98% bij afgestemde modellen, met de definitie erbij).

## Wat nooit

- **AI-tells** (volledige lijst in `seo-geo.md` onder "Menselijk klinken"). De ergste: delve, landscape, crucial, pivotal, transformative, seamless, robust, "in today's fast-paced", "it's not just X, it's Y", een slotalinea die alles herhaalt.
- **"Genuinely", "well known", "it's worth noting".** De oudere concepten in `GTM/Campaigns/blog-launch/markdown-sources/` gebruiken "genuinely" soms drie keer per alinea. Die concepten zijn géén stijlvoorbeeld; de vier referentieblogs wel.
- **Komma-treinen.** Zinnen van 45 woorden met vijf bijzinnen. Knippen.
- **Hype.** revolutionary, game-changing, unlock, empower, cutting-edge.
- **Een getal zonder context of bron.** Liever geen getal dan een los getal.
- **Angst als hefboom.** Geen "institutions that don't act now will fall behind". Een wet uitleggen mag streng zijn, dreigen niet.

## Kalibratiestatus

- **25-09-2026:** eduface.me was vanuit deze omgeving niet bereikbaar (netwerkbeleid). De patronen hierboven komen uit citaten die via zoekresultaten zijn teruggehaald, niet uit de volledige pagina's. Koppen, lengte en de FAQ-blokken van de vier blogs zijn daardoor niet exact bekend.
- **Hercalibreren** zodra de volledige tekst beschikbaar is (Dante plakt hem, of eduface.me staat open in de netwerkinstellingen): lees de vier blogs helemaal, vul per blog de echte H2-lijst, woordtelling en FAQ in hieronder, en pas de patronen aan waar ze afwijken. Meld wat er veranderd is.

| Blog | Woorden | H2's | FAQ | Bronnenlijst |
|---|---|---|---|---|
| ai-grading-tools-higher-education-guide | onbekend | onbekend | onbekend | onbekend |
| ai-essay-grader-canvas-lms-lti | onbekend | onbekend | onbekend | onbekend |
| ai-essay-grader-moodle-lti | onbekend | onbekend | onbekend | onbekend |
| eu-ai-act-higher-education-assessment | onbekend | onbekend | minstens 1 | onbekend |
