# Blog design system, CMS, cover pipeline, gotchas, schema

## Project + architectuur
- Framer project: `rHz5Bx9iyHzFybv35vaj` (zie [[framer-project-link]]). Dante werkt alleen in dit project.
- Elke blog = een `WebPageNode` op `/resources/blog/<slug>`, met layout-template `default` (id `Ezs45gtGY`, "Standaard") die nav + footer levert. NIET per pagina nav/footer bouwen.
- Pagina = Desktop-breakpoint (1200px, height auto) met 3 sectie-kinderen: **Hero** (navy) → **Content** (maxWidth 720) → **CTA** (navy). Daarna Tablet (810) + Phone (390) via `CREATE_VARIANT`.
- Referentie-blog om patroon te bevestigen: page `jHWeiLUf5` = `/resources/blog/ai-marking-accuracy-human-alignment`.

## Kleuren (letterlijke rgb, geen tokens)
- Navy hero/CTA fill: `rgb(0, 35, 51)`
- Accent groen (primaire knop): `rgb(0, 224, 117)`
- Pill-achtergrond: `rgba(0, 224, 117, 0.15)`
- Mint callout/stat: `rgb(240, 250, 247)`
- Kaart wit `rgb(255,255,255)`, kaartrand `1px solid rgb(214, 228, 235)`
- Tabel zebra: `rgb(235, 242, 245)` / `rgb(242, 250, 247)`; header = navy

## Text style presets (hergebruiken op naam, NIET opnieuw maken)
`Hero H1 White` (hero H1) · `Description Wit` (witte hero-subtitel/meta, CTA-desc, secundaire knop) · `Box Title` (groene uppercase pill-eyebrow) · `Blog H2` (sectiekop) · `Body 16` (alinea — NIET Body 19, dat leest te dik) · `Body 16 bold` (bold lead, kaarttitel, tabel-eerste-cel, callout-titel, primaire knop) · `Body 14` (tabelcellen, klein) · `New H2` (grote stat) · `Description` (gedempte stat-body) · `CTA Title` · `Cell Head` (witte bold tabelheader).

Inline links: `LinkStylePreset` genaamd **"Body Link"** (groen `rgb(0,160,84)` + underline, hover `rgb(0,53,40)`). Maak eenmalig aan:
```
+LinkStylePresetNode blk name="Body Link"; SET blk link.textColor="rgb(0,160,84)" link.textDecoration="underline" link.hover.textColor="rgb(0,53,40)";
```

## Fonts (zie [[brand-fonts]])
Primair League Spartan (headlines), secundair Inter (body). Niet Roboto.

## CMS-kaart (BlogPosts)
Collectie `QOSeMeN0X`. Maak per blog een item; velden (agent-API zet enum op case-NAAM, niet id):
```
+CollectionItemNode <id> parent="QOSeMeN0X";
SET <id> $control__title="<kaarttitel>" $control__slug="<slug>" $control__body="<excerpt>"
  $control__category="Compliance"        // Thought Leadership | Compliance | Research | Product | Integrations
  $control__read_time="9 min read" $control__cover.src="<framerusercontent-url>"
  $control__author="Eduface Team"
  $control__author_avatar.src="https://framerusercontent.com/images/oqqj6zbhfnR1AGLCWg6TtDut1Ew.png"
  $control__published_date="2026-07-09T00:00:00.000Z"
  $control__seo_title="<... | Eduface>" $control__seo_description="<meta>"
  $control__featured="false" $control__article_path.href="/resources/blog/<slug>" draft="false";
```
`article_path` (link-veld) laat de kaart naar de losse WebPageNode wijzen. `.src` voor image-velden, `.href` voor link-velden.

## Cover pipeline (light flat-icon)
Generator: `projects/blog-launch/covers/gen_light.py` — bevat ALLE scenes en schrijft `final/<slug>.html`. Stijl (zie [[blog-cover-style]]): licht `#f3f7f8`, navy outlines `#002333` (stroke 14-20), groene vlakken `#00d563` (accent `#00b85f`), witte vormen krijgen altijd navy outline, grond-schaduw-ellips `#dbe6ea`, ronde hoeken, GEEN tekst/logo, 1200×900 @2x. Voeg per blog één content-passende scene toe (`SCENES["<slug>"] = '''...svg...'''`), voor de `for slug, scene in SCENES.items()`-loop.

Renderen (Chrome hangt op de Google Drive mount → naar LOKALE map):
```
python3 gen_light.py
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# per slug: cp final/<slug>.html naar /private/tmp/.../scratchpad/covers/ , dan:
"$CHROME" --headless=new --disable-gpu --force-device-scale-factor=2 --window-size=1200,900 --hide-scrollbars --screenshot=<slug>.png <slug>.html
# PNG terug naar final/ kopiëren
```
Inline infographic-SVG's (door Dante aangeleverd) render je op dezelfde manier: schrijf de .svg weg, render met `--window-size=<viewBox w>,<h>`, upload de PNG, plaats als `img`-blok met `aspect = w/h`.

Uploaden: `framer.uploadImage({image: "data:image/png;base64,"+b64, altText})` → geeft framerusercontent-URL. (Third-party hosts als catbox worden geblokkeerd.)

## Verplichte verificatie na build (kost anders live bugs)
- **Fixed-height bug**: de content-sectie krijgt soms `height=100px` i.p.v. `auto` (vooral als de CLI mid-build een update deed) → alles na de eerste alinea valt weg. Loop alle breakpoints langs en `SET <sectie> height="auto"` waar niet auto.
- **Dubbele pagina**: als het pad al bestond (mislukte/herstarte build) maakt Framer `<slug>-2`. Check op duplicaten. Framer laat de agent GEEN pagina's verwijderen → vraag Dante die in de editor te deleten.
- **Block-count** klopt met de spec.
- Voeg Tablet + Phone toe: `CREATE_VARIANT <dt>_t from="<dt>"; SET <dt>_t name="Tablet" width="810px" left="1320px" top="0px"; CREATE_VARIANT <dt>_p from="<dt>"; SET <dt>_p name="Phone" width="390px" left="2210px" top="0px";`

## Overige gotchas
- **Agent CLI, niet de MCP-plugin.** De MCP-plugin viel constant weg, ging view-only (rolde pagina's stil terug), en hernoemde node-IDs. De agent CLI kan alles wat nodig is (breakpoints, per-pagina SEO via `metadata.title`/`metadata.description`, screenshots, publish).
- **Sessie verloopt vaak** → `session new` opnieuw (geeft meestal id `1`), `switchBranch` naar de juiste branch.
- **Scratchpad + /var/folders tmp worden tussen turns opgeschoond.** Schrijf compiler + specs elke sessie opnieuw weg. De compiler staat in deze skill (`reference/build-page.js`).
- **idPrefix uniek per build** (`state.idPrefix`). Temp-ids `k0,k1...` botsen anders met bestaande canonieke nodes ("Cannot add node with an existing id").
- **Interne links naar een pagina die nog niet bestaat worden gedropt.** Framer smelt de drie runs dan tot 1 TextRun zonder href. Bij een cluster: bouw alle pagina's eerst, herstel daarna de vooruitwijzende links (`DEL v:<richtext>:0:0;` + 3x `+TextRun parent="v:<richtext>:0"`). De TextBlock-id is `v:<RichTextNode-id>:0`, niet de RichTextNode zelf.
- **overflowX="auto" wordt gedropt** op stack-wrappers → brede tabellen fluid houden (width 100%, fr-kolommen), niet scrollen.
- **Timeout**: builds kunnen >2 min duren → ruime bash-timeout, één pagina per call. Bij een lokale timeout kan de relay serverside dóórbouwen (deels), wat rare halve/dubbele pagina's geeft — daarom altijd verifiëren.
- **Branches**: Framer maakt bij elke edit een branch (`[FRAMER_BRANCH_CHANGE]`). Agent kan branches NIET deleten (gated) → Dante ruimt ze op. NOOIT een oude branch mergen die verwijderde junk bevat.
- **Productie-publish** is geblokkeerd door de safety-classifier tenzij Dante expliciet "live" zei. Anders branch-preview publiceren en de review-URL geven.

## Schema (JSON-LD) — handmatig plakken
Per-pagina head-code kan NIET via de API (alleen site-brede `setCustomCode`, wat voor unieke per-artikel schema fout is). Genereer per blog een `.html` met 3 blokken:
- **Article** (headline, description, image=cover-url, author Organization Eduface, publisher, datePublished/dateModified, mainEntityOfPage)
- **FAQPage** (mainEntity uit de FAQ — antwoordtekst LETTERLIJK gelijk aan de zichtbare pagina, anders negeert Google het)
- **BreadcrumbList** (Home > Blog > artikel)

Genereer met een node-script dat de FAQ uit de spec-blocks haalt (pb=vraag, volgende p=antwoord, tussen "Frequently asked questions" en "Sources"). Zie `projects/blog-launch/ofqual-schema/` voor voorbeelden. Dante plakt per blog in **Page Settings → Custom Code → End of `<head>`** en checkt met Google Rich Results Test.

## SEO/GEO (zie [[geo-title-strategy]])
Titel begint met het specifieke onderwerp + ` | Eduface`, < ~55-60 tekens (anders truncatie). Meta 1-2 concrete zinnen ~150-160 tekens.
