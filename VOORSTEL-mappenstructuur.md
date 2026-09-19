# Voorstel mappenstructuur — versie 2

Verwerkt jouw feedback. Schrijf nieuwe opmerkingen achter **Feedback:**.
Dit bestand verdwijnt zodra we het uitvoeren.

---

## Wat er veranderd is t.o.v. versie 1

| Jouw feedback | Verwerkt |
|---|---|
| vu-amsterdam mag weg | Verwijderd, niet gearchiveerd |
| `markt/` → `ICP` | ✓ |
| `events/` → `Event manager` | ✓ — dit is ook je Todoist-sectienaam |
| `playbooks/` → `Knowledge` | ✓ |
| `prijzen/` → `Pricing` | ✓ |
| Go-live-plan niet onder pricing | Verplaatst naar `Knowledge/` |
| Spaties en hoofdletters mogen | ✓ — zie naamregels hieronder, met één uitzondering |
| Skills samenvoegen (4×) | ✓ — zie skill-blok |
| SHIFT | **Gevonden** in de zip die je net uploadde: 261 bestanden |

---

## 1. De eerste laag

```
CLAUDE.md          moet in de root
.gitignore         moet in de root
.claude/           skills, rules, agents, scripts, hooks, settings
Context/           wie je bent, Eduface, team, prioriteiten, doelen, kaart
GTM/               alles sales & marketing
Design/            design system, merk, website
Platform/          het product zelf
Personal/          fitness, privécontext
Decisions/         besluitenlog + feedback
Archive/           afgerond en vervangen
```

Acht mappen, nul losse bestanden op de twee die moeten.

**Feedback:**
-

---

## 2. GTM/ — zes submappen

### GTM/Accounts/ — 12 instellingen

breederode-hogeschool · rug-groningen · windesheim · notenboom · uti · tu-delft · capabel · icm-opleidingen · hbmsu · salta · cmi-ireland · business-school-nederland

`vu-silvester-draaijer` is geschrapt.

### GTM/Campaigns/ — wat je uitstuurt

uk-outreach · au-outreach · lt-outreach-nl · cold-calling · paid-ads · linkedin-content · blog-launch · momentum

### GTM/Event manager/

haagse-hogeschool-webinar · altc-conference

### GTM/ICP/ — wie moet je hebben

**shift/** (261 bestanden uit je nieuwe zip: master met orgs.csv, people.csv, journal.csv en de dossiers, plus markets) · targetlijst-nl · market-sizing-international · landingspagina-icp · discovery-kennis · pijn-oplossing · shift-cockpit

### GTM/Knowledge/ — hoe je verkoopt

sales-handbook · meddpicc-states-and-gates · q-points-scorecard · crm-playbook · gtm-abm-motion · cold-call-roleplay · 3 podcastnotities · **go-live-plan** (template)

### GTM/Pricing/

prijsmodel-psu-26-27

### En sales-coach?

Die stond los in versie 1. Voorstel: `GTM/sales-coach/`, want het is je levende CRM plus coachingsapp — dat hoort onder GTM, niet ernaast.

**Feedback:**
-

---

## 3. Design/

| Submap | Inhoud |
|---|---|
| `Design system/` | core, web, slides, internal |
| `Merk/` | brand-assets, brand-guidelines, Logo van scholen |
| `Website/` | website-building, landing-page-demo-survey, app-homepage-redesign, calendly-cta-migration |

**`creatives/` schrap ik als map.** Er zit één PNG in. De README bevat wel een nuttige regel — losse creatives hier, projectcreatives bij het project — die zet ik in `Context/kaart.md`. Die ene PNG gaat naar `Design/Merk/`.

**Feedback:**
-

---

## 4. Platform/

`product.md` (negen bestanden lezen hieruit — je belangrijkste bronbestand) · `onderwijs-vaktermen.md` · `product-brief-ui-beelden.md` · `usability-test/` · `Onderzoek/`

**Feedback:**
-

---

## 5. Skills — van 32 naar 28

### De vier samenvoegingen

| Wordt | Uit | Waarom |
|---|---|---|
| `cro` | `cro-of-eduface` + `giving-sales-advice-` | Allebei John de CRO. De tweede heeft een typefout in de naam en één regel beschrijving. |
| `schrijven` | `goed-teksten-schrijven` + `content-voice` | Allebei overtuigend schrijven in de juiste stem. |
| `outreach` | `outreach` + `targeted-outreach` | **Let op:** `outreach` is agent 4 van de SHIFT-pijplijn. Ik houd die rol intact en bouw targeted-outreach erin als tweede stand: los signaal in plaats van pijplijn. |
| `meddpicc` | `meddpicc-sales-grid` + `meddpicc-qualifier` + `sso-grid` | Ik las jouw "maak er maar één van" als de MEDDPICC-skills. **Klopt dat?** `sso-grid` is puur de plaatjesstap met een eigen Close-script; die wordt dan de laatste stand binnen `meddpicc`. |

### Wat overblijft, 28 skills

**Sales (11)** — cro · sales-coach · meddpicc · kunnen-we-winnen · stakeholder-mapping · organogram · cold-call-prep · question-builder · deal-status-update · meeting-prep-tasks · person-research

**SHIFT-pijplijn (5)** — lead-sourcing (1) · contact-sourcing (2) · shift-research (3, agent) · outreach (4) · lemlist-import (5)

**Marketing en content (5)** — linkedin-content · schrijven · marketing-creatives · blog-builder · linkedin-profile-scraper

**Bouwen (3)** — design-loop · scroll-film-studio · pitch-deck

**Overig (4)** — deep-research · task-planning · skill-builder · fitness-coach

Plus `grammar-check` = 28. Die laat ik apart: taalfoutjes checken is iets anders dan schrijven.

**Feedback:**
-

---

## 6. Naamregels — aangepast op jouw voorkeur

**Mappen die jij en ik lezen: spaties en hoofdletters mogen.** Kort en duidelijk.
`GTM/Event manager/`, `Design/Design system/`, `Platform/Onderzoek/`

**Eén uitzondering, en die is hard:** alles onder `.claude/` blijft kleine letters met streepjes.
Reden: de mapnaam van een skill *is* het commando. `/task-planning` werkt, `/task planning` niet.
Hetzelfde voor `shift/master/people.csv` — daar leest `pipeline.py` uit, dus die paden blijven exact zoals ze zijn.

**Verder:**
- Geen apostrofs of spaties aan het eind. Nu fout: `Logo van scholen /`, `Kings's college London.png`
- Geen backup-achtervoegsels — git is je backup. Weg met `.bak`, `-backup-voor-*`, `.oud-*`
- Datums alleen als het bestand een datum ís, en dan `2026-09-19`. Nu drie stijlen: `30-juni`, `0902`, `2026-08-14`
- Eén wegwijzer per map, altijd `README.md`. Nu vier woorden voor hetzelfde: README, LEESMIJ, HANDOFF, OVERDRACHT
- Elke map krijgt een README van max 10 regels: wat is dit, welke fase, volgende stap, wat leest hieruit

**Feedback:**
-

---

## 7. Wat weg gaat

| Wat | Hoeveel |
|---|---|
| node_modules | 30 MB |
| temporary screenshots | 77 MB |
| 13 × .DS_Store | |
| `CLAUDE (1).md` | duplicaat met Windows-paden |
| 50 lege JSON's in pijn-oplossing | |
| 4 dubbele merkassetmappen | logo staat nu 5× |
| Backupvarianten | .bak, .voor-bewijsfix.html, pagina.backup.html |
| `Claude-AE/` | leeg |
| `vu-silvester-draaijer/` | jouw besluit |
| 15 zips | 8 uitpakken, 7 zijn .git-binnenwerk |
| `hub.html` | 16 links naar artifacts, 0 naar deze repo — `Context/kaart.md` neemt het over |

Alles blijft in de git-geschiedenis, dus niets is echt weg.

**Feedback:**
-

---

## 8. Nog open

**Documenten in drie formaten.** RUG-pitchdeck bestaat als html + pdf + pptx + bewerkbaar.pptx. Zelfde bij Windesheim. Voorstel: bron + de versie die je deelt houden, rest naar Archive. Lijst volgt vóór ik het doe.

**Twaalf documenten over afgelopen momenten** (RUG-meeting 30 juni, webinar 23 juni). Naar Archive of laten staan?

**`Context/current-priorities.md` en `goals.md` zijn van 8 juni** en worden elke sessie automatisch geladen. Los oppakken, zei je — akkoord, maar zolang dat niet gebeurt start elke sessie met verouderde prioriteiten.

**Feedback:**
-

---

## 9. Volgorde

1. ~~Sleutels uit git~~ ✓ gedaan
2. Zips uitpakken naar `.claude/` en `GTM/ICP/shift/`
3. Afval weg (110 MB)
4. Nieuwe indeling met `git mv`
5. Skills samenvoegen (4 stuks)
6. Verwijzingen repareren — 16 naar `.claude/`, 6 naar shift (lost zichzelf op), 3 naar verhuisde prijsmodellen, 9 naar bestanden die nooit gemaakt zijn
7. `Context/kaart.md` en `Decisions/feedback.md`

Eén commit per stap, elk los terug te draaien.

**Feedback:**
-
