# Blog covers — manifest

**Style (current, light — 2026-06-25):** flat-icon on light background (`#f3f7f8`). Navy outlines (`#002333`, stroke 14–20), flat green fills (`#00d563`, accents `#00b85f`/`#00c95c`), white shapes always get a navy outline so they read on the light bg, grounding shadow ellipse (`#dbe6ea`), all corners rounded. No text, no logo. 1200×900 (4:3), rendered @2x. Cards are navy; the light cover tile sits on the navy card. Reference icon = the dart-in-bullseye (`ai-marking-accuracy-human-alignment`).

Generator: `gen_light.py` holds all 25 scenes → writes `final/<slug>.html`. Render: copy HTML to a LOCAL dir (Chrome screenshots hang on the Google Drive mount), `Google Chrome --headless=new ... --screenshot`, then copy PNGs back. File name = CMS slug.

CMS upload (no third-party host): Framer agent `framer.uploadImage({image: dataURI})` returns a `framerusercontent.com` URL, then MCP `upsertCMSItem` sets the Cover field (`MmADoQVy1`). NOTE: upsert re-validates the enum Category, so always send Category as its case ID alongside Cover (Thought Leadership `U9HvLhCd3`, Compliance `s4j7NfOqR`, Research `O1w2U3_Z9`, Product `UR9EMdHPS`, Integrations `oc48O75w5`).

**Previous style (navy):** flat-icon on solid navy (`#002333`), white outlines + green fills. Backed up in `final-navy-backup/`.

| # | Blog title | Slug | Live URL | Cover file | Scene |
|---|-----------|------|----------|-----------|-------|
| 1 | GDPR and AI Assessment: Keeping Student Data Compliant | `gdpr-ai-assessment-compliance` | /resources/blog/gdpr-ai-assessment-compliance | `final/gdpr-ai-assessment-compliance.png` | Document with green text lines + EU & UK flag-lock badge (UK & EU law) |
| 2 | How Accurate Is AI Marking, Really? | `ai-marking-accuracy-human-alignment` | /resources/blog/ai-marking-accuracy-human-alignment | `final/ai-marking-accuracy-human-alignment.png` | Dart in the bullseye |
| 3 | How Faster Feedback Turnaround Affects NSS Scores | `feedback-turnaround-nss-scores` | /resources/blog/feedback-turnaround-nss-scores | `final/feedback-turnaround-nss-scores.png` | Stopwatch + rising bars + upward arrow |

## Status (2026-06-25)
Alle 24 CMS-blogposts hebben de **nieuwe light-cover** gekregen, gezet via MCP `upsertCMSItem` op branch `main`. Eén scène per blog, content-gedreven (dartboard=accuracy, weegschaal=fairness, EU-sterren+gavel=EU AI Act, klok+papers=marking time, puzzel/plug/ringen/sync-vensters=LMS-integraties). Rotterdam blijft `draft=true`, NSS-feedback-scores blijft `featured=true`.

`gdpr-ai-assessment-compliance` is een **losse statische pagina** (geen CMS-item); de nieuwe light-cover-PNG staat klaar in `final/` maar is nog niet op de pagina geplaatst (vereist canvas-edit op die pagina).

Niet gepubliceerd — staat in de CMS op `main`, gaat live bij de volgende Framer publish.

## Toegevoegd (2026-07-01) — 2 nieuwe AI-grading-tools blogs
Scenes 26-27 toegevoegd aan `gen_light.py`:
- `ai-grading-tools-higher-education-guide` — evaluatie-checklist (klembord + groene vinkjes) = "how to choose / buyer's guide".
- `eduface-vs-ai-grading-tools` — oplopende vergelijkings-staafjes met groene winnaar + check = head-to-head.

Beide gebouwd als volledige native Framer-pagina's (hero/content/CTA, Desktop/Tablet/Phone), CMS-cards (categorie **Product**, Eduface Team) + covers geüpload, op branch `velvet-isle`. Gepubliceerd als **branch preview** (productie niet geraakt). Merge naar `main` + productie-deploy wacht op Dante's go.

## Toegevoegd (2026-07-09) — 3 blogs
Scenes 28-30 in `gen_light.py`:
- `formative-vs-summative-assessment-ai` — klok (tijdige formatieve feedback) vs baret (summatief). Categorie **Research**.
- `academic-integrity-ai-assessment-design` — schild met groene vink (integriteit). Categorie **Thought Leadership**.
- `jisc-chest-ai-assessment-procurement` — document met groen approved-zegel. Categorie **Compliance**.

Volledige native pagina's (hero/content/CTA, Desktop/Tablet/Phone) + CMS-cards + covers, op branch `velvet-isle`, in dezelfde branch preview als de vorige 2. Samen = 5 nieuwe blogs wachtend op Dante's go voor merge naar `main` + productie-deploy.
