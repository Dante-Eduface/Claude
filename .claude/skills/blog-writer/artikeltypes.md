# Artikeltypes en hun skelet

Kies eerst het type, dat bepaalt de opbouw. Elk type hieronder komt uit een referentieblog of uit wat aantoonbaar converteert (zie `seo-geo.md`, "Welke artikelen je schrijft").

Voor alle types geldt hetzelfde raamwerk:

```
# Titel (H1)                          onderwerp vooraan, belofte erachter
*By Eduface Team · <Month YYYY> · X min read*
*Last updated: <D Month YYYY>*        alleen bij een inhoudelijke update

Opening, 2 alinea's                   alinea 1 = het directe antwoord (40-60 woorden)
                                      alinea 2 = voor wie dit is en wat je na het lezen weet

## H2's als vragen of stellingen      elk opent met een antwoord dat los klopt
...
## Frequently asked questions         4 tot 6 vragen die de H2's niet al beantwoorden
## Sources                            primaire bronnen, met jaar
```

De CTA-sectie bouwt `blog-builder` (vaste navy CTA met Calendly en signup). Schrijf hem dus niet in de tekst, tenzij Dante er een specifieke zin voor wil.

---

## 1. Koopgids of vergelijking (bottom of funnel)

Voorbeeld: `ai-grading-tools-higher-education-guide`, `eduface-vs-ai-grading-tools`, `best-ai-grading-tools-moodle-2026`.
Zoekvraag: "best AI grading tool for X", "X vs Y", "X alternative", "how to choose".

1. Opening: het antwoord in één alinea, plus wie dit schreef en hoe er getest is.
2. `## How we evaluated` : de criteria en de testopzet. Dit is je information gain, maak hem concreet (aantal papers, vakken, wat gemeten).
3. `## The short answer` : een **tabel** met alle tools op dezelfde criteria. Kolommen = criteria die de koper echt afweegt (integratie, wie keurt het cijfer, bewijs van accuraatheid, dataverwerking, soorten toetsen, inkoopkanaal).
4. Per tool een `###` met steeds dezelfde drie alinea's: goed in, schiet tekort in, gebruik hem voor.
5. `## Which one fits your situation` : per type instelling of toets een aanbeveling. Hier mag Eduface winnen, alleen waar het echt wint.
6. FAQ, bronnen.

Regels: eerlijk over concurrenten (die eerlijkheid is het verkoopargument), elk getal met testcontext, concurrentclaims alleen uit hun eigen publieke bronnen met datum.

## 2. Integratiepagina (bottom of funnel)

Voorbeeld: `ai-essay-grader-moodle-lti` (hub), `ai-essay-grader-canvas-lms-lti`.
Zoekvraag: "AI grader [LMS]", "[LMS] AI marking LTI", "[LMS] plugin for AI feedback".

1. Opening: wat het is en hoe het koppelt, in de eerste zin ("X connects to Canvas via LTI 1.3").
2. `## How it works in [LMS]` : de workflow als één lopende zin plus een genummerde lijst van 4 tot 6 stappen, in de menunamen van dat LMS.
3. `## What the lecturer sees` : het goedkeuringsmoment, concreet.
4. `## Setup` : wie het doet (learning technologist), hoe lang, wat er nodig is. Geen stap noemen die niet bevestigd is.
5. `## Data and compliance` : alleen claims uit `product.md`.
6. FAQ met de vragen die IT en docenten écht stellen (student login, gradebook, versies, kosten).

Regels: de hub (`ai-essay-grader-moodle-lti`) heeft de volledige setup. Spokes (Moodle-quiz, Moodle-oral enz.) linken naar de hub en herhalen de setup niet. Een tweede LMS-pagina is **geen kopie met een andere naam**: elke LMS-pagina moet de eigen menu's, eigen beperkingen en eigen vragen van dat LMS behandelen, anders is het dunne, bijna-dubbele content (zie `seo-geo.md`, risico's).

## 3. Regelgeving-uitlegger (midden van de funnel)

Voorbeeld: `eu-ai-act-higher-education-assessment`, de Ofqual-reeks, `gdpr-ai-assessment-compliance`.
Zoekvraag: "does the EU AI Act apply to AI grading", "is AI allowed to mark assignments Ofqual".

1. Opening: het antwoord op de vraag (ja/nee/onder welke voorwaarde), met de bron in de zin.
2. `## What the [law] actually says` : artikelnummers, bijlagen, letterlijke kernzin tussen aanhalingstekens, datum van kracht.
3. `## What this means for [rol]` : per rol (instelling, docent, leverancier) wat er moet.
4. `## Timeline` : een **tabel** met data. Controleer elke datum tegen de actuele stand, regelgeving verschuift (zie de EU AI Act-datum in `bronnen.md`).
5. `## Questions to ask a vendor` : een checklist. Dit is het informatiewinst-blok.
6. Pas dan: hoe Eduface het oplost, één sectie.
7. FAQ, bronnen (primair: de wettekst zelf).

Regels: geen juridisch advies beloven, wel precies zijn. Een verouderde datum in een compliance-artikel is erger dan geen artikel.

## 4. Vak- of toepassingsuitlegger (midden van de funnel)

Voorbeeld: de vakreeks (law, nursing, psychology, history, accounting), `ai-marking-accuracy-human-alignment`.
Zoekvraag: "AI grading law essays", "can AI mark nursing case studies".

1. Opening: het eerlijke antwoord (waar het helpt, waar niet) in twee zinnen.
2. `## What makes [vak] hard to mark` : de vakconventie bij naam (IRAC, SOAP-notitie, enz.).
3. `## Where AI marking helps` en `## Where it is harder` : allebei concreet.
4. `## What good practice looks like` : aparte criteria, rubricvoorbeeld (een **tabel** met criterium, wat AI checkt, wat de docent checkt).
5. FAQ, bronnen.

Regels: de zes vakmodellen mag je noemen; wat elk vakmodel precies kent **niet** (staat als niet vastgelegd in `product.md`).

## 5. Werkwijze of rekenmodel (midden tot onder)

Voorbeeld: `cost-per-assignment-ai-grading-savings`, `what-to-automate-first-assessment-team`.

1. Opening: wat de lezer na afloop zelf kan uitrekenen of beslissen.
2. De methode in stappen, met een **uitgewerkt voorbeeld** met duidelijk gelabelde voorbeeldgetallen.
3. Wat de methode bewust weglaat.
4. Een template of checklist als download-waardig blok.
5. FAQ, bronnen.

---

## Lengte

Geen woordtarget (woordaantal is geen rankingfactor, zie `seo-geo.md`). Wel een richting:

| Type | Richting |
|---|---|
| Koopgids | 2.000 tot 3.500 woorden, want de tabel en de profielen zijn het werk |
| Integratiepagina | 1.000 tot 1.800 |
| Regelgeving | 1.500 tot 2.500 |
| Vak / werkwijze | 1.000 tot 1.800 |

Stop zodra de vraag beter beantwoord is dan wat nu op pagina 1 staat. Opvulling om een lengte te halen is precies wat de kwaliteitssystemen afstraffen.
