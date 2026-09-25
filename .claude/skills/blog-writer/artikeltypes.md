# Artikeltypes en hun skelet

Kies eerst het type, dat bepaalt de opbouw. Elk type hieronder komt uit een referentieblog of uit wat aantoonbaar converteert (zie `seo-geo.md`, "Welke artikelen je schrijft").

Voor alle types geldt dezelfde anatomie (uitgewerkt met voorbeelden in `stijl.md`, "Anatomie van een pagina"):

```
EYEBROW: ONDERWERP · SUBONDERWERP
# H1: hoofdterm vooraan: reikwijdte
*Dek: een of twee zinnen, wat het is plus de kernbelofte*
By Eduface · <Month YYYY> · <X> min read · Written for <rol>

Openingsscène (2-5 zinnen, tweede persoon, situatie van de lezer)

> **<De hoofdvraag letterlijk>**
> Antwoordblok, 60-90 woorden, entiteiten bij naam

## H2's als de vragen die de lezer stelt      elk opent met een zin die los klopt
   om de 2-3 secties een visueel blok: flow, tabel, figuur, genummerde stappen
   callouts met label waar een doelgroep iets aparts moet weten
## Vergelijkingstabel                          alle opties op dezelfde kolommen
## Frequently asked questions                 5 vragen, antwoord begint met Yes/No/de stelling
## Slot-H2 met stelling                       alleen bij regelgeving en gids
[CTA]                                          standaard via blog-builder
## References                                 genummerd, met [Key finding: ...]
```

## 1. Koopgids of vergelijking (bottom of funnel)

Referentie: `referentie/ai-grading-tools-higher-education-guide.md`. Ook `eduface-vs-ai-grading-tools`, `best-ai-grading-tools-moodle-2026`.
Zoekvraag: "best AI grading tool for X", "X vs Y", "X alternative", "how to choose".

Opbouw van de referentie, zo overnemen:
1. "Quick answer for busy readers" als antwoordblok, met het belangrijkste testresultaat én de waarschuwing.
2. `## Why this guide exists` : de druk op de lezer, voor wie de gids is, en de eigen positie ("We are Eduface [...] we have a position in this market").
3. `## What [X] actually is, and what it isn't` : de begrippen scherp, met vetgedrukte criteria die de kwaliteit bepalen.
4. `## What the research says` : met tabel en **met bronnen** (de referentie mist die, zie `stijl.md`).
5. `## The [N]-tool landscape` : korte profielen, gegroepeerd.
6. `## How we tested` : wie testte, wat de referentie was, dezelfde input voor elk, wat gemeten, en `### Limitations`. Dit is de informatiewinst.
7. `## Tool-by-tool findings` : per tool `### [Tool]: [oordeel]`, "Grade accuracy: ...", sterk, zwak, "**Best use:** ... Not for ...". Eduface ook, met "**What it doesn't do:**".
8. `## What the results tell us` : genummerde lessen met vet begin.
9. `## A framework for choosing` : stappen met beslistabellen ("If you primarily grade... | Consider...").
10. `## What to ask a vendor` : vragen per thema met vet begin.
11. FAQ (tot 9), slot-H2 met lessen, References.

Regels: eerlijk over concurrenten (die eerlijkheid is het verkoopargument), elk getal met testcontext, concurrentclaims alleen uit hun eigen publieke bronnen met datum.

## 2. Integratiepagina (bottom of funnel)

Referenties: `referentie/ai-essay-grader-moodle-lti.md` (hub), `referentie/ai-essay-grader-canvas-lms-lti.md`.
Zoekvraag: "AI grader [LMS]", "[LMS] AI marking LTI", "is there an AI grading plugin for [LMS]".

Opbouw van de referenties:
1. Openingsscène vanuit de learning technologist of de docent in dat LMS.
2. Antwoordblok: "What AI assessment tools are available for [LMS]?" met de tools, LTI 1.3, gradebook, geen aparte login.
3. `## How does Eduface connect to [LMS] via LTI 1.3?` (of de stelling-vraag, "Is Eduface a [LMS] plugin or an LTI integration?"), met een definitie van LTI 1.3, een **flowdiagram** met onderschrift en **genummerde stappen** met vet begin in de menunamen van dat LMS.
4. Callout voor IT ("For IT and learning technology teams"): wie, hoe lang, welke gegevens.
5. Per module een H2 in de vorm "How does the [module] work inside [LMS]?". Alleen modules en functies uit `product.md`.
6. `## Comparing the [N] Eduface tools for [LMS]` : tabel met kolommen doel, toetstype, wanneer de docent goedkeurt, grade passback.
7. Compliance-callout, alleen met claims uit `product.md`.
8. FAQ met de vragen die IT en docenten echt stellen: bestaat er een ingebouwde AI-grader, GDPR, moeten studenten iets anders doen, hoe lang duurt de setup, vervangt het [SpeedGrader / de native grader], werkt het met versie X.

Regels: de hub (`ai-essay-grader-moodle-lti`) heeft de volledige setup. Spokes (Moodle-quiz, Moodle-oral enz.) linken naar de hub en herhalen de setup niet. Een tweede LMS-pagina is **geen kopie met een andere naam**: elke LMS-pagina moet de eigen menu's, eigen beperkingen en eigen vragen van dat LMS behandelen, anders is het dunne, bijna-dubbele content (zie `seo-geo.md`, risico's).

## 3. Regelgeving-uitlegger (midden van de funnel)

Referentie: `referentie/eu-ai-act-higher-education-assessment.md`. Ook de Ofqual-reeks, `gdpr-ai-assessment-compliance`.
Zoekvraag: "does the EU AI Act apply to AI grading", "is AI allowed to mark assignments Ofqual".

Opbouw van de referentie, zo overnemen:
1. Byline met de lezer: "Written for HE compliance leads & DVCs".
2. Openingsscène: het moment waarop niemand het antwoord weet.
3. Antwoordblok met de wet bij naam en nummer, de bijlage en het punt, en wat het wel en niet betekent ("does not prohibit use: it requires ...").
4. `## What exactly does [the law] cover in [sector]?` : de indeling, het relevante punt, de sleutelzin tussen aanhalingstekens en wat daar wel en niet onder valt. **Figuur** met de risiconiveaus.
5. `## What obligations does [classification] create for institutions?` : per artikel een H3, met wat het in de praktijk betekent. Callout "Compliance risk:" voor de ene fout die je niet mag maken.
6. `## Where are most institutions right now?` : een cijfer uit een primaire bron, met **figuur** en superscript.
7. `## What should an institution do to prepare?` : stappen met vet begin, elk een handeling.
8. `## How does Eduface meet [the law]?` : pas hier, met een tabel verplichting, eis, Eduface-aanpak. Alleen claims uit `product.md`.
9. FAQ met de juridische vervolgvragen (UK na Brexit, tijdlijn, wat telt als X, moeten studenten het weten).
10. Slot-H2 met een stelling, CTA, References met de wettekst als eerste bron.

Voeg toe wat de referentie mist: een `## Timeline`-**tabel** met alle data, en elke datum getoetst tegen de huidige stand (Bijlage III: 2 december 2027 sinds de Digital Omnibus, zie `bronnen.md`).

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
| Koopgids | 3.000 tot 5.000 woorden (referentie: 4.763), want de test, de tabellen en de profielen zijn het werk |
| Integratiepagina | 1.400 tot 1.900 (referenties: 1.528 en 1.758) |
| Regelgeving | 1.700 tot 2.300 (referentie: 2.082) |
| Vak / werkwijze | 1.000 tot 1.800 |

Stop zodra de vraag beter beantwoord is dan wat nu op pagina 1 staat. Opvulling om een lengte te halen is precies wat de kwaliteitssystemen afstraffen.
