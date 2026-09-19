# Voorstel mappenstructuur

Schrijf je feedback direct onder elk blok, achter **Feedback:**. Kort mag: "ja", "nee, moet X", "snap ik niet".
Dit bestand verdwijnt zodra we het uitvoeren.

---

## 1. De eerste laag: 7 mappen

Alleen mappen. De enige losse bestanden zijn `CLAUDE.md` en `.gitignore` — die moeten in de root staan, anders leest Claude Code ze niet.

| Map | Wat erin hoort | Komt uit |
|---|---|---|
| `.claude/` | skills, rules, agents, scripts, hooks, settings | de 14 zips |
| `context/` | wie je bent, Eduface, team, prioriteiten, doelen, kaart | `context/` |
| `gtm/` | alles sales & marketing | `projects/` (28 mappen), `references/sops`, `references/pricing`, `templates/` |
| `design/` | design system, merk, website, creatives | `references/design-system`, `references/brand-assets`, `creatives/`, 4 website-projecten |
| `platform/` | het product zelf: claims, vaktermen, onderzoek | `references/` losse bestanden, `usability-test` |
| `persoonlijk/` | fitness, privécontext | `projects/fitness`, `context/personal.md` |
| `besluiten/` | besluitenlog + feedback | `decisions/` |
| `archief/` | afgerond en vervangen | `archives/` |

Dat zijn er 8 als je `.claude/` meetelt. `templates/`, `creatives/`, `references/` en `projects/` verdwijnen als losse top-level map.

**Waarom deze woorden:** ze komen uit je Todoist. Jij zet sales en marketing samen onder GTM, en je hebt Design en Eduface platform als aparte secties. Google Drive gebruikt Sales/Marketing/Branding apart — daar wijk ik bewust van af omdat je zelf zei dat GTM de plek is waar het samenkomt.

**Feedback:**
-

---

## 2. gtm/ — 7 submappen

### gtm/accounts/ — de instellingen waar een deal loopt

| Nieuw | Nu |
|---|---|
| `breederode-hogeschool/` | projects/breederode-hogeschool |
| `rug-groningen/` | projects/rug-groningen |
| `windesheim/` | projects/windesheim |
| `notenboom/` | projects/action-learning-demo |
| `uti/` | projects/uti |
| `tu-delft/` | projects/tu-delft |
| `capabel/` | projects/capabel |
| `icm-opleidingen/` | projects/icm-opleidingen |
| `hbmsu/` | projects/hbmsu |
| `salta/` | projects/salta |
| `cmi-ireland/` | projects/cmi-ireland |
| `business-school-nederland/` | projects/business-school-nederland |
| `vu-amsterdam/` | projects/vu-silvester-draaijer (nu genoemd naar de persoon, niet de instelling) |

### gtm/campagnes/ — wat je uitstuurt

uk-outreach-campaign · au-outreach · lt-outreach-nl · cold-calling · paid-ads-buildout · linkedin-content · blog-launch · momentum

### gtm/events/ — webinars en conferenties

haagse-hogeschool-webinar · altc-conference

### gtm/markt/ — wie moet je hebben

targetlijst-nl · market-sizing-international · landingspagina-icp · discovery-kennis · pijn-oplossing · shift · shift-cockpit

### gtm/playbooks/ — hoe je verkoopt

Uit `references/sops/`: sales-handbook · meddpicc-states-and-gates · q-points-scorecard · crm-playbook · gtm-abm-motion · cold-call-roleplay · de 3 podcastnotities

### gtm/prijzen/

`references/pricing/` + `templates/go-live-plan/` (jouw voorbeeld: templates met één bestand kan naar GTM)

### gtm/sales-coach/

Blijft zoals het is.

**Feedback:**
-

---

## 3. design/ — 4 submappen

| Submap | Inhoud |
|---|---|
| `design-system/` | references/design-system (core, web, slides, internal) |
| `merk/` | brand-assets, brand-guidelines.md, "Logo van scholen" |
| `website/` | website-building, landing-page-demo-survey, app-homepage-redesign, calendly-cta-migration |
| `creatives/` | creatives/ |

**Feedback:**
-

---

## 4. platform/ — het product

`product.md` (nu `references/eduface-product.md` — negen bestanden lezen hieruit, dit is je belangrijkste bronbestand) · `onderwijs-vaktermen.md` · `product-brief-ui-beelden.md` · `usability-test/` · `onderzoek/` (references/research + website-analyses)

**Feedback:**
-

---

## 5. Je 32 skills

Ze blijven allemaal in `.claude/skills/` staan — Claude Code vindt ze alleen daar. Deze indeling is zodat jij weet wat je hebt.

**Sales — deals voeren (14)**
cro-of-eduface · sales-coach · meddpicc-sales-grid · sso-grid · kunnen-we-winnen · stakeholder-mapping · organogram · cold-call-prep · question-builder · deal-status-update · meeting-prep-tasks · person-research · targeted-outreach · goed-teksten-schrijven

**SHIFT-pijplijn — opleiders vinden en benaderen (5, genummerd)**
lead-sourcing (1) · contact-sourcing (2) · shift-research (3, is een agent) · outreach (4) · lemlist-import (5)

**Marketing en content (6)**
linkedin-content · content-voice · marketing-creatives · blog-builder · linkedin-profile-scraper · grammar-check

**Bouwen (3)**
design-loop · scroll-film-studio · pitch-deck

**Overig (4)**
deep-research · task-planning · skill-builder · fitness-coach

### Overlap die ik zie

| Overlap | Wat er speelt |
|---|---|
| `cro-of-eduface` vs `giving-sales-advice-` | Allebei "John de CRO". De tweede zit in je account-skills, heeft een typefout in de naam en één regel beschrijving. Voorstel: weg. |
| `meddpicc-sales-grid` vs `sso-grid` vs `meddpicc-qualifier` | Drie MEDDPICC-dingen. De eerste twee vullen elkaar aan (scoren vs plaatje). De derde zit in je account-skills en doet hetzelfde als de eerste. |
| `outreach` vs `targeted-outreach` | Allebei outreach schrijven. De eerste is agent 4 van SHIFT, de tweede staat los. Samenvoegen of duidelijker uit elkaar trekken? |
| `goed-teksten-schrijven` vs `content-voice` vs `grammar-check` | Drie schrijfskills. Grammar-check is duidelijk apart, de andere twee overlappen. |
| `deep-research` vs `person-research` | Overlappen niet echt — onderwerp vs persoon. Laat ik staan. |

**Feedback:**
-

---

## 6. Naamregels

- Kleine letters, kebab-case, Nederlands
- Geen spaties of apostrofs. Nu fout: `Logo van scholen /`, `temporary screenshots/`, `Kings's college London.png`
- Geen `snake_case` ernaast. Nu: `brand_assets/` naast `brand-assets/`
- Geen backup-achtervoegsels — git is je backup. Weg met `.bak`, `-backup-voor-*`, `.oud-*`, `-v1/-v2`
- Datums alleen als het bestand een datum ís, en dan `2026-09-19`. Nu drie stijlen: `30-juni`, `0902`, `2026-08-14`
- Eén wegwijzer per map, altijd `README.md`. Nu vier woorden voor hetzelfde: README, LEESMIJ, HANDOFF, OVERDRACHT
- Elke projectmap krijgt een README van max 10 regels: wat is dit, welke fase, volgende stap, wat leest hieruit

**Feedback:**
-

---

## 7. Wat ik weggooi

| Wat | Hoeveel |
|---|---|
| node_modules | 30 MB |
| temporary screenshots | 77 MB, 162 PNG's |
| 13 × .DS_Store | |
| `CLAUDE (1).md` | duplicaat met Windows-paden |
| 50 lege JSON's in pijn-oplossing/extractie | |
| 4 dubbele merkassetmappen | logo staat nu 5× |
| Backupvarianten | .bak, .voor-bewijsfix.html, pagina.backup.html |
| `Claude-AE/` | leeg |
| 7 van de 14 zips | per ongeluk meegezipt .git-binnenwerk |

Alles blijft in de git-geschiedenis staan, dus niets is echt weg.

Apart voorleggen, nog geen besluit: documenten die in 3 formaten bestaan (RUG-pitchdeck als html + pdf + pptx + bewerkbaar.pptx), en 12 documenten over afgelopen momenten (RUG-meeting 30 juni, webinar 23 juni).

**Feedback:**
-

---

## 8. Twee dingen die ik niet kan oplossen zonder jou

**`projects/shift/` is leeg.** Ook op GitHub. Zes bestanden noemen het "de actuele stand" en `targetlijst-nl/LEESMIJ.md` stuurt je er expliciet heen. De oude data staat in `archives/targetlijst-nl-oud/` (68 bestanden). Waar staat de echte SHIFT-data?

**`context/current-priorities.md` en `goals.md` zijn van 8 juni** en noemen het webinar van 23 juni als aanstaand. Die worden elke sessie automatisch geladen, dus ik start nu elke keer met verouderde prioriteiten. Los oppakken na het opruimen, zei je — akkoord, maar dit is wel de duurste fout in de map.

**Feedback:**
-

---

## 9. Volgorde van uitvoeren

1. Sleutels uit tracking, `.gitignore`
2. Zips uitpakken naar `.claude/`
3. Afval weg (110 MB)
4. Nieuwe indeling met `git mv`
5. Verwijzingen repareren (16 naar `.claude/`, 6 naar shift, 3 naar verhuisde prijsmodellen, 9 naar bestanden die nooit gemaakt zijn)
6. `context/kaart.md` en `besluiten/feedback.md`

Eén commit per stap, dus je kunt elke stap los terugdraaien.

**Feedback:**
-
