---
name: blog-builder
description: Bouwt een Eduface-blog van markdown → volledig live op eduface.me/resources/blog. Native Framer-pagina (hero/content/CTA, responsive), on-brand light cover, CMS-kaart, SEO-titel+meta, en kant-en-klare JSON-LD schema. Trigger wanneer Dante zegt "zet deze blog(s) online/live", "bouw deze blog", "maak er een blog van", een of meer blog-markdownbestanden aanlevert, of een bestaande blogpagina wil aanpassen. Vervangt de oude MCP-plugin-aanpak uit [[framer-blog-building]].
---

# Eduface blog builder

Bouwt blogs **native in Framer via de agent CLI** (niet de MCP-plugin, niet Figma). Één blog = een `WebPageNode` onder `/resources/blog/<slug>` met fluid auto-layout stacks + een kaart in de `BlogPosts` CMS-collectie. Data-driven: je schrijft de blog om naar een **spec-JSON** en een **compiler** (`reference/build-page.js`) genereert alle Framer-DSL.

Lees ook `reference/design-system.md` (kleuren, text styles, CMS-velden, cover-pipeline, gotchas, schema).

## Vooraf (elke sessie opnieuw)
1. Laad de `framer` skill. Precondition: `npx @framer/agent@latest setup` één keer laten draaien.
2. `npx @framer/agent@latest session new "rHz5Bx9iyHzFybv35vaj"` → geeft session-id (meestal `1`). Draai alle `npx @framer/agent` commando's met sandbox uit (netwerk + fs nodig).
3. Laad de gegenereerde `framer-project-rHz5Bx9iyHzFybv35vaj` skill.
4. Check `getActiveBranch()`. Framer maakt bij elke edit **automatisch een branch** aan (`[FRAMER_BRANCH_CHANGE]`). Bouwen mag op die branch; aan het eind `mergeBranch('main')` + publiceren.
5. **Sessie verloopt vaak.** Bij "Session invalid" gewoon `session new` opnieuw en `switchBranch` naar de juiste branch.

## Stap voor stap
1. **Inspecteer eenmalig** (alleen bij twijfel): serialize een recente fluide blog (bv. page `jHWeiLUf5` = ai-marking-accuracy) om het patroon te bevestigen. Structuur = Desktop-breakpoint (1200px) met 3 kinderen: Hero (navy), Content (maxWidth 720), CTA (navy). Layout-template `default` levert nav+footer — die NIET per pagina toevoegen.
2. **Covers**: voeg per blog een scene toe aan `GTM/Campaigns/blog-launch/covers/gen_light.py` (light flat-icon stijl, zie design-system.md), render lokaal met Chrome, bekijk ze. Zie design-system.md → "Cover pipeline".
3. **Maak de link-stijl** (eenmalig per project, al aanwezig): een `LinkStylePreset` genaamd **"Body Link"** voor inline-links. Check met `getNodesOfTypes({types:['LinkStylePresetNode']})`; bestaat 'ie al, niets doen.
4. **Schrijf per blog een spec-JSON** (zie `reference/spec-example.json` + blok-types hieronder). Sla ze op in een stabiele scratchpad-map, bv. `.../scratchpad/blogbuild/`. LET OP: die map wordt tussen turns opgeschoond — schrijf de compiler + specs elke sessie opnieuw weg (compiler staat in deze skill).
5. **Kopieer `reference/build-page.js`** naar de scratchpad-map.
6. **Bouw per blog**: zet `state.specFile` + een **unieke** `state.idPrefix` (bv. `q8a`), dan `exec -f build-page.js`. Eén pagina per call, ruime timeout (tot 420000 ms).
7. **Verifieer + fix** (verplicht, zie gotchas):
   - Elke sectie-hoogte `= "auto"` op alle breakpoints (de content-container krijgt soms `height=100px` → alles na de eerste alinea valt weg).
   - Geen dubbele pagina (`-2`-suffix) en block-count klopt.
   - Voeg Tablet + Phone breakpoints toe via `CREATE_VARIANT` (810px @ left 1320, 390px @ left 2210).
8. **Cover uploaden + CMS-kaart**: `framer.uploadImage({image: dataURI})` → framerusercontent-URL, dan één `applyChanges` die per blog een `+CollectionItemNode parent="QOSeMeN0X"` aanmaakt met alle velden (zie design-system.md).
9. **Publiceren**: `mergeBranch('main')` → `publish({action:'preview'})` → `publish({action:'confirm_publish', confirmationHash})`. Productie-publish is geblokkeerd door de safety-classifier tenzij Dante expliciet "zet live"/"live" zei. Anders: branch-preview publiceren en de review-URL geven.
10. **Schema (JSON-LD)**: genereer per blog een `.html` met Article + FAQPage + BreadcrumbList (FAQ-tekst letterlijk gelijk aan de pagina). Kan NIET via de API (alleen site-brede custom code bestaat; per-pagina head-code is UI-only). Lever de bestanden op in `GTM/Campaigns/blog-launch/*-schema/`; Dante plakt ze in **Page Settings → Custom Code → End of `<head>`** en checkt met Google Rich Results Test.
11. **QA**: screenshot 1 pagina via `readProject({type:'screenshot', url})` + curl de 4 live-URL's op HTTP 200.

## Blok-types in de spec (`blocks: [...]`)
- `{"t":"h2","x":"..."}` — sectiekop (Blog H2, tag h2)
- `{"t":"p","x":"..."}` — alinea (Body 16). Of met runs voor bold/links: `{"t":"p","runs":[["Bold lead. ",true],["gewone tekst",false],["linktekst",true,"/resources/blog/slug"]]}` (run = `[text, bold, href?]`)
- `{"t":"pb","x":"..."}` — hele alinea bold (Body 16 bold), gebruikt voor FAQ-vragen en subkoppen
- `{"t":"callout","title":"...","x":"..."}` — mint highlight-kaart (ook `runs` mogelijk)
- `{"t":"cards","cols":2,"items":[{"title":"...","x":"..."}]}` — grid van witte kaarten
- `{"t":"table","weights":[1.4,1,1],"head":[...],"rows":[[...]]}` — navy-header zebra-tabel. **Brede tabellen (>4 kol): NIET scrollen — houd `width 100%` met fr-kolommen** (overflowX auto wordt gedropt door Framer).
- `{"t":"img","src":"<framer-url>","aspect":1.875,"alt":"..."}` — inline afbeelding (bv. infographic-SVG als PNG geüpload), width 100% + aspectRatio.

## Vaste content-conventies
- Hero eyebrow = korte uppercase label ("COMPLIANCE · OFQUAL"). Meta-regel = "By Eduface · <maand> 2026 · X min read".
- Auteur op de kaart = "Eduface Team" (Dante wil geen echte naam invullen tenzij gevraagd).
- CTA-knoppen: primair groen → Calendly `https://calendly.com/eduface/30min?back=1`; secundair outline → `https://app.eduface.me/signup`. **Naast elkaar** (horizontale stack, gecentreerd), niet gestapeld.
- SEO-titel (GEO): begin met het **specifieke onderwerp** + ` | Eduface`, < ~55-60 tekens. Zie [[geo-title-strategy]].
- FAQ als `pb`(vraag) + `p`(antwoord). Sources als `h2 "Sources"` + `p`-regels (geen externe links tenzij gevraagd).

## Hub-and-spoke (indien van toepassing, bv. Moodle-cluster)
Hub = `/resources/blog/ai-essay-grader-moodle-lti`. Spokes linken in de lopende tekst naar de hub + relevante siblings (via inline-link runs). Herhaal LTI-setupstappen NIET in spokes — die staan alleen in de hub.
