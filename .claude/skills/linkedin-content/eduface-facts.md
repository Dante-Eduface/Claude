# Eduface facts (canoniek voor content)

Bron: eduface.me (gescrapet 2026-06-18) + door Dante bevestigde cijfers. Gebruik dit voor claims in posts. `(site)` = staat op de website. `(team)` = door Dante/team bevestigd. ⚠ = eerst verifieren voor publiek gebruik.

## Product
- "AI essay grader built for universities. Consistent, rubric-aligned marking across every submission." (site)
- Complete AI assessment platform met 4 tools: **Feedback** (formatief), **Exam Grader** (open exam-vragen tegen marking scheme), **Paper Grader** (papers tegen rubric), **Oral Examination** (viva op schaal, **nog in development, niet posten als live feature**). (site)
- Voor UK + EU hoger onderwijs: gratis tier voor losse lecturers, enterprise voor instellingen/faculteiten. 6 disciplines: Law, Economics, Social Sciences, STEM, Humanities, Health Sciences. (site)

## Model
- Eigen model, gebouwd voor onderwijs, niet aangepast van een algemeen model. Getraind op o.a. onderwijskundig/didactisch materiaal. (team + site)
- **6 discipline-specifieke submodellen**, elk getraind als domein-expert. (site)
- Gehost op **eigen GPU-infra in Nederland / strikt in de EU**. Gebruikt **geen third-party APIs zoals OpenAI**. (site)
- Traint **niet** op data/opdrachten van klanten. (site)
- ⚠ **Overclaim-waarschuwing (Menno 2026-06-18):** een eigen/self-hosted model is NIET automatisch "transparant" of "uitlegbaar". Een LLM blijft een black box, of je 'm huurt of zelf traint. Niet claimen dat we de interne werking kunnen zien. Verantwoording zit in het proces (rubric-gekoppelde onderbouwing, logging, menselijke sign-off, audit trail).
- **Parameters: 120B** (actueel + mag publiek, bevestigd Dante 2026-06-18). LET OP: de site zegt nog ~70B, dat is verouderd en moet op eduface.me aangepast worden.
- **SQuAD-NL / F1-claim: NIET meer geldig** (bevestigd Dante). Niet gebruiken.

## Proof / cijfers
- **~95-96% alignment**: AI-cijfers komen in ~95% van de gevallen overeen met die van de lecturer (UK pilots, site); Bath Spa-pilot 96% (team). LET OP (feedback 2026-06-18): gebruik dit cijfer en klant-instellingen (ook Bath Spa) NIET als bewijs in thought-leadership posts, dat klinkt commercieel. Voor sales/decks wel bruikbaar.
- **~48% tijdsbesparing** op nakijken (site + team). De school NIET noemen bij dit cijfer (team).
- **~48% consistenter** dan ongeholpen menselijk nakijken over dezelfde cohort met meerdere markers. (site)
- Markers passen gemiddeld maar **~5%** van een eindcijfer aan / binnen 5% van menselijk nakijken. (site)
- **< 4 min** van upload tot voorgesteld cijfer (incl. rubric-analyse + 3 AI-agents die elk scoren + 4e die verzoent en verschillen flagt). (site)
- Feedback-doorlooptijd in pilot: **1-2 dagen incl. lecturer-review vs 2-4 weken handmatig**. (site)
- **5000+ lecturers** (bevestigd Dante, actueel; de oude 500+ is verouderd).
- ⚠ Energie: "80-95% minder energie per submission vs algemene AI". Sterke claim (site), verifieer voor je 'm prominent gebruikt.
- ⚠ Oral exam: "89% van 200 pilot-deelnemers beoordeelde hun AI-orale toets positief". (site, verifieer)

## Integraties
- Canvas, Moodle, Brightspace (D2L), Blackboard, via native **LTI 1.3**. Inzendingen stromen automatisch in, goedgekeurde cijfers gaan terug naar de gradebook, eenmalige setup door een learning technologist. (site)

## Security / compliance (sterk voor IT/procurement-posts)
- EU & UK GDPR-compliant. Data in de EU, verlaat de EU niet. DPA op aanvraag. (site)
- **EU AI Act**: AI-assessment = high-risk (Annex III, 3(b), Reg. 2024/1689). De high-risk-VERPLICHTINGEN zijn UITGESTELD: noem augustus 2026 NIET als vaststaande datum (Menno-feedback 2026-06-18). De classificatie high-risk bestaat wel; de timing wordt nog vastgesteld. Wat de Act vraagt: human oversight + traceerbaarheid, GEEN inzage in het model zelf.
- **Human-in-the-loop (Art. 14)**: geen autonoom cijferen, elke mark vereist review + sign-off van de lecturer. Blind mode (lecturer eerst) of AI-visible mode. Volledige audit trail. (site)
- **Transparantie (Art. 13)**: elk cijfer uitlegbaar en auditeerbaar, criterium-gebaseerde redenering per score. (site)

## Positionering (hun eigen woorden, bruikbaar)
- "Made for education" / "AI that works specifically for education"
- "Human is always in the loop" / "The educator is always in control"
- "Drafted by AI, reviewed by you"
- "Every grading decision is explainable"
- "No fatigue, no drift between the first and last essay" (sterk tegen de Cambridge central-tendency/drift-bevinding)
- "AI in assessment works best as an assistant to human judgment rather than a replacement"
- "Feedback is a tool for learning. Grading is a certification of attainment."

## Genoemde pilots / partners
- Bath Spa University (UK), Tilburg University (NL), De Haagse Hogeschool (NL), Hogeschool Rotterdam (NL). NIET als bewijs/naam-drop in thought-leadership posts gebruiken (feedback 2026-06-18); ze staan wel publiek op de site.
- Procurement: Jisc / CHEST-framework (UK, approved supplier). HEAnet-framework (Ierland).

## Taal
- Site is volledig Engels. Geen NL-versie. Model-taalondersteuning niet vermeld, dus geen meertaligheid claimen zonder bevestiging.

## Open punten voor Dante (verifieren)
- Pilot-jaren (UK 2023-24 vs Rotterdam 2025/26) kloppend maken voor je ze noemt.
- "80-95% minder energie"-claim: hard genoeg onderbouwd voor prominent gebruik?
- Site-fix: parameter-getal op eduface.me staat op ~70B, moet 120B worden.
