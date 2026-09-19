# Kaart van deze map

Wat hoort waar, wat leest waaruit, en hoe dingen heten. Bijwerken zodra de indeling verandert.

## De eerste laag

Alleen mappen. `CLAUDE.md` en `.gitignore` zijn de enige losse bestanden, omdat Claude Code
ze daar moet vinden. `.claude/` en `.vscode/` zijn configuratie.

| Map | Wat hier hoort | Wat hier **niet** hoort |
|---|---|---|
| `Context/` | Wie Dante is, wat Eduface is, het team, prioriteiten, doelen, deze kaart | Projectwerk |
| `GTM/` | Alles sales & marketing | Productkennis, designwerk |
| `Design/` | Design system, merk-assets, websitewerk | Campagnemateriaal (dat is GTM) |
| `Platform/` | Het product zelf: claims, vaktermen, onderzoek, usability | Accountspecifieke stukken |
| `Personal/` | Privé. Wordt niet auto-geladen | Alles wat met Eduface te maken heeft |
| `Decisions/` | `log.md` (append-only) en `feedback.md` | Werkbestanden |
| `Archive/` | Afgerond en vervangen materiaal | Iets waar nog aan gewerkt wordt |

## GTM van binnen

| Submap | Wat |
|---|---|
| `Accounts/` | Eén map per instelling met een lopende deal |
| `Campaigns/` | Wat je uitstuurt: outreach, ads, content, blog |
| `Event manager/` | Webinars en conferenties |
| `ICP/` | Wie moet je hebben. Inclusief `shift/`, de opleiderspijplijn |
| `Knowledge/` | Playbooks, handboeken en templates |
| `Pricing/` | Prijsmodellen |
| `sales-coach/` | Levend CRM plus coachingsapp |

## Wat waaruit leest

- **`Platform/product.md`** is de bron van waarheid voor productclaims. Negen bestanden lezen
  hieruit. Klopt een claim ergens niet, corrigeer hier, niet in de kopie.
- **`Design/Design system/`** is verplicht bij alles wat een mens bekijkt. Start bij
  `core/proces.md`, laad daarna alleen `core/` plus het oppervlak dat je bouwt.
- **`Design/Merk/`** is de enige bron voor logo's, fonts en schoollogo's. Kopieer ze niet
  een project in; verwijs ernaar. Dat ging eerder mis: het Eduface-logo stond vijf keer in de repo.
- **`GTM/ICP/shift/master/`** wordt gelezen door `.claude/scripts/pipeline.py` en
  `dashboard.py`. De mapnamen en bestandsnamen daaronder liggen dus vast.
- **`GTM/Knowledge/sales-handbook-v1.md`** is het anker voor `/cro` en de dealfasen.

## Losse creatives

Hoort een afbeelding bij een project, dan gaat hij in `<projectmap>/creatives/`. Is hij
algemeen (Google Maps banner, losse social post, testrender), dan in `Design/Merk/`.
Paid-ads-materiaal blijft in `GTM/Campaigns/paid-ads/` met zijn eigen structuur.

## Naamregels

Mappen die jij en ik lezen mogen spaties en hoofdletters hebben, als de naam maar kort en
duidelijk is: `GTM/Event manager/`, `Design/Design system/`.

**Eén uitzondering, en die is hard.** Alles onder `.claude/` blijft kleine letters met
streepjes, want de mapnaam van een skill *is* het commando: `/task-planning` werkt,
`/task planning` niet. Hetzelfde geldt voor `GTM/ICP/shift/master/`, waar scripts uit lezen.

Verder:

- Geen apostrofs en geen spaties aan het eind van een naam.
- Geen backup-achtervoegsels. Git is de backup. Dus geen `.bak`, `-backup-voor-...`, `.oud-...`, `-v2`.
- Datums alleen als het bestand een datum ís, en dan als `2026-09-19`.
- Eén wegwijzer per map, altijd `README.md`. Niet LEESMIJ, HANDOFF of OVERDRACHT door elkaar.
- Een README is maximaal tien regels: wat is dit, welke fase, volgende stap, wat leest hieruit.

## Skills

Staan in `.claude/skills/`, want Claude Code vindt ze alleen daar. Aanroepen met `/naam`.

### Sales

- **`/cro`** — Act as John CRO, Eduface's internal sales leader.
- **`/sales-coach`** — Dante's persoonlijke salescoach en levend CRM.
- **`/meddpicc`** — The SCORING and coaching skill (not the visual one).
- **`/sso-grid`** — ALLEEN de visuele output-stap.
- **`/kunnen-we-winnen`** — Bid/no-bid go-no-go check voor een nieuwe kans, uitvraag of tender, op basis van een 10-vragen...
- **`/stakeholder-mapping`** — Map and verify the key stakeholders at an education institution for a deal, and classify each...
- **`/organogram`** — Build a clean, print-perfect organogram / org chart / stakeholder map as HTML then PDF, with...
- **`/cold-call-prep`** — Zet het onderzoek naar een contact om in een uitgeschreven belscript in Dante's vaste template,...
- **`/question-builder`** — Maakt vragen die een gesprek openen in plaats van een formulier invullen.
- **`/deal-status-update`** — Schrijft een korte status-update per deal/account uit Close CRM en zet die in het note-veld van...
- **`/meeting-prep-tasks`** — Zet de voorbereidingstaken voor een aankomende meeting automatisch in Todoist.
- **`/person-research`** — Diepgaand, bronnen-gevalideerd onderzoek naar één persoon (prospect, stakeholder, champion,...

### SHIFT-pijplijn

- **`/lead-sourcing`** — Agent 1 van de SHIFT-opleiderspijplijn, voor elke markt (nl, uk, us, ...).
- **`/contact-sourcing`** — Agent 2 van de SHIFT-opleiderspijplijn, voor elke markt (nl, uk, us, ...).
- **`/outreach`** — Agent 4 van de SHIFT-pijplijn, voor elke markt.
- **`/lemlist-import`** — Agent 5 van de SHIFT-pijplijn, voor elke markt.

### Marketing en content

- **`/linkedin-content`** — Schrijft LinkedIn-posts in 4 stemmen (Dante, Jeroen, Menno, Eduface company page) vanuit...
- **`/schrijven`** — Schrijft en reviseert alles wat naar buiten gaat — mails, offertes, website copy, presentaties,...
- **`/marketing-creatives`** — Maakt on-brand Eduface marketingmateriaal — afbeeldingen, banners, ads, social visuals.
- **`/blog-builder`** — Bouwt een Eduface-blog van markdown → volledig live op eduface.me/resources/blog.
- **`/linkedin-profile-scraper`** — Haalt via Apify een LinkedIn-profiel op (headline, about, functiebeschrijvingen, opleiding,...
- **`/grammar-check`** — Controleert door Dante geplakte tekst (mails, berichten, agenda-onderwerpen, korte zinnen) in NL...

### Bouwen

- **`/design-loop`** — Takes a goal and a real-world reference, extracts what actually makes the reference good, then...
- **`/scroll-film-studio`** — Build a genuinely beautiful animated scroll-film website — the whole page is one continuous...
- **`/pitch-deck`** — Bouwt Eduface-slides en decks die er af uitzien en die bewerkbaar zijn in Canva of PowerPoint.

### Overig

- **`/deep-research`** — Diep onderzoek naar een open vraag (markt, concurrent, beleid, trend, technologie, "hoe zit X in...
- **`/task-planning`** — Daily / weekly / monthly task planning + prioritisation for Dante across Todoist.
- **`/skill-builder`** — Build a new Claude Code skill, or fix/upgrade an existing one.
- **`/fitness-coach`** — Dante's strength and nutrition coach for his Greek god V-taper lean bulk.

### Buiten de repo

Deze staan in Dante's account, niet in deze map: `eduface-cfo` (geschreven voor Jeroen),
`morning`, `learn`, `import-memory`, plus de standaard Anthropic-skills.
`giving-sales-advice-` en `meddpicc-qualifier` zijn hier opgenomen in `/cro` en `/meddpicc`
en kunnen uit het account weg.
