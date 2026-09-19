# ICP Scoremodel v1 — universiteiten scoren op publieke signalen

_Doel: bepalen welke universiteiten outreach-prioriteit krijgen, uitsluitend op basis van publiek verifieerbare informatie. Eerst getest op Australië, herbruikbaar voor andere markten._

## Harde regels (belangrijker dan de gewichten)

1. **Elk signaal heeft een bron.** URL + datum + letterlijk feit/quote. Geen bron = geen punten.
2. **Niet gevonden = niet gevonden.** Wordt expliciet zo gerapporteerd, nooit ingevuld met logica of aannames ("het is een grote uni dus waarschijnlijk...").
3. **Verouderd telt niet.** Signalen ouder dan 24 maanden alleen meenemen als expliciet gemarkeerd verouderd, triggers ouder dan 18 maanden vervallen.
4. **Per signaal een confidence:** `bevestigd` (primaire bron: eigen site, officieel document) / `indicatief` (secundaire bron: nieuws, vacature, LinkedIn).

## Laag 0 — Gates (binair; zakt de uni hier, dan geen score maar een nee)

| # | Gate | Waar te vinden |
|---|---|---|
| G1 | LMS = Canvas, Moodle, Brightspace of Blackboard (incl. eigen Moodle-variant) | IT/library-pagina's, studenthandleidingen, edtech-vacatures, LMS-migratienieuws |
| G2 | Substantieel volume schrijf-/open opdrachten: opleidingen als business, education, nursing, law, humanities aanwezig op schaal | Opleidingsaanbod op de site |
| G3 | Erkende instelling (publieke universiteit of geregistreerde private provider), ≥ ~5.000 studenten (private opleiders: uitzondering mogelijk, kleinere dealsize accepteren) | TEQSA-register, jaarverslag |

## Laag 1 — Gewogen signalen (0–100)

| # | Signaal | Gewicht | Waar te vinden (AU) |
|---|---|---|---|
| S1 | **Formeel aankoop-/bouwtraject rond AI assessment/feedback zichtbaar** (tender, projectvoorstel, werkgroep met mandaat, pilot met andere tool) | 30 | AusTender, uni-tenderportalen, academic board / council minutes, strategie-documenten, nieuws |
| S2 | AI-in-assessment beleid gepubliceerd of in consultatie (TEQSA gen-AI action plans, assessment reform agenda) | 10 | TEQSA-publicaties, uni policy libraries, L&T-blogs |
| S3 | Lopende herziening van toets-/feedbackbeleid | 10 | Academic board minutes, policy review pages |
| S4 | Nieuwe DVC/PVC Education of Head of Learning & Teaching (< 18 mnd) | 10 | Persberichten, LinkedIn, uni-nieuws |
| S5 | Lage scores op feedback/assessment in studentenquête (QILT SES: "feedback" items onder sectorgemiddelde) | 10 | qilt.edu.au / ComparED |
| S6 | Onderwijsgericht profiel (geen Group of Eight / onderzoeksintensief; ATN, regional, post-92-equivalent) | 10 | Publieke classificatie |
| S7 | Recente edtech-adoptie of LMS-migratie (< 3 jaar) — bewijs dat ze kunnen en willen kopen | 10 | Vendornieuws, vacatures, conferentiepresentaties (bijv. ASCILITE) |
| S8 | Werkdruk-/nakijkdruk-signalen (NTEU-acties, casualisation-nieuws, workload disputes) | 5 | Nieuws, NTEU |
| S9 | Toegankelijk inkoopkanaal (CAUDIT-lidmaatschap of vergelijkbaar framework) | 5 | CAUDIT-ledenlijst |

**Tiers:** A = ≥ 60 punten **én** S1 aanwezig · B = 40–59 · C = < 40.
S1 is dominant by design: bij Bath Spa en RUG was een lopend formeel traject mét budget de sterkste voorspeller.

## Laag 2 — Diskwalificatoren (overrulen elke score)

| # | Diskwalificator |
|---|---|
| D1 | Eigen AI grader breed uitgerold en (publiek) tevreden → bouwt zelf, koopt niet |
| D2 | Expliciet moratorium/freeze op nieuwe software-inkoop of gen-AI tools |
| D3 | LMS exotisch/eigen systeem buiten de 4 ondersteunde |
| D4 | Publiek anti-AI-in-assessment standpunt van bestuur |

## Discovery-laag (NIET scoren — checklist voor het eerste gesprek)

Deze zaken zijn online niet betrouwbaar vindbaar (Jeroens punt) en worden in Discovery gevalideerd:

- Is er budget gekoppeld aan het traject (S1)?
- Wie zit er in de DMU, is er een champion hoog in de boom?
- Why-now intern: wat is de echte trigger?
- Volwassenheid IT/learning tech team
- Interne houding tegenover bouwen vs kopen

## Output-format per universiteit

```
## [Universiteit] — Score: XX/100 — Tier [A/B/C]
Gates: G1 ✓/✗/? · G2 ✓/✗/? · G3 ✓/✗/?
Diskwalificatoren: geen / [welke]

| Signaal | Punten | Feit | Bron (URL) | Datum bron | Confidence |
|---|---|---|---|---|---|
| S1 | .. | .. | .. | .. | bevestigd/indicatief |
...

Niet gevonden: [expliciete lijst van signalen waar niets over te vinden was]
Discovery-checklist: [wat in het eerste gesprek gevalideerd moet worden]
```

## Status / changelog

- v1 (2026-07-16): eerste opzet, gewichten zijn aannames. Testprotocol: 1 uni → review → 3 unis → fine-tunen → skill bouwen (`uni-scoring`; contacten zoeken wordt een aparte skill).
