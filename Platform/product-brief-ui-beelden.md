# Productbriefing voor wie UI- en productbeelden maakt

Geschreven op 11-09-2026 voor de sessie die UI-images en product-images maakt. Alles hieronder is wat er nu echt is, plus waar de bronbestanden staan.

**Lees dit bestand vanuit de hoofdmap.** Het staat niet in elke worktree; wie in een worktree zit die van een oudere commit aftakt vindt het niet.

**De hoofdregel:** `Platform/product.md` is de enige bron voor productclaims. Staat een functie daar niet in, dan teken je hem ook niet. Een verzonnen knop in een beeld is hetzelfde als een verzonnen claim in een mail.

---

## 1. Wat het product doet

Eduface is een AI-platform voor beoordelen en feedback in het hoger onderwijs. Vier modules:

| Module | Staat | Wat het doet |
|---|---|---|
| **AI Paper Grader** | live | Leest elke inzending, markeert passages, schrijft criterium-specifieke opmerkingen gegrond in de rubric, plus volledige rubric-scoring met uitlegbare cijferopbouw en annotaties in de tekst |
| **AI Exam Grader** | live | Scoort open en gesloten antwoorden tegen het correctiemodel, markeert onzekerheid, geeft het cijfer terug aan het gradebook van het LMS |
| **Academic Integrity** | beta | Student krijgt kritische vragen over zijn eigen paper en verantwoordt zich mondeling |
| **Oral Examination** | beta | Mondelinge afname met realtime transcriptie en beoordeling |

"AI Feedback" bestaat niet als losse module, dat is de Paper Grader.

### Het mechanisme dat in élk beeld zichtbaar moet zijn

**De AI stelt voor, de docent tekent af.** Elke opmerking en elk cijfer wordt door de docent bekeken en goedgekeurd voordat de student iets ziet. Dat is letterlijk hoe het werkt en het is ons sterkste argument bij examencommissies. Een beeld waarin de AI autonoom beoordeelt is dus niet alleen lelijk, het is fout.

Twee dingen die je daarom mag laten zien: onzekerheid die gemarkeerd wordt in plaats van weggepoetst, en een goedkeur-moment van de docent.

---

## 2. Hoe de echte app eruitziet

Uitgelezen op `app-dev.eduface.me` op 03-09-2026. Dit is de huidige productie-UI.

**De schil**
- Zijbalk 240px op een lichte achtergrond: workspace-schakelaar (`EduLMS / Lecturer`), sectielabel `Platform`, dan `Courses` (uitklapbaar, toont alle cursussen), `Billing`, `Referrals`, `Profile`. Onderin een tokenbadge `2,000` en de accountregel met avatar, naam en e-mail.
- Topbalk 48px wit: knop om de zijbalk in te klappen, breadcrumb `EduLMS / Courses`, taalkeuze met vlaggetje (Dutch / English).
- Inhoud op een lichte achtergrond, content max ~1180px.

**Courses (de landingspagina na inloggen)**
- `Courses` + `View and manage your courses.`
- Groene knop `Create Course`, daarnaast een tandwiel met een popover `Show archived courses`.
- Cursussen als cards in een raster: titel, opleidingsniveau met een bul-icoon, datum met een kalender-icoon, kebab-menu met `Archive` en `Delete`.
- Rechtsonder een Guide-paneel: pil `Courses — Open a course or ask where to go next`, opent een lade met `Activation checklist 3/4 complete +2,000 tokens` (Upload submission ✓, Manage rubric ✓, Download submission ✓, Invite another teacher = next), snelknoppen Upload / Open latest course / Create another course, en een invoerveld `Ask about this page or pick an option`.

**Opdrachtpagina**
- Breadcrumb `EduLMS / Courses / <cursus> / <opdracht>`, titel van de opdracht, `View and manage submissions for this assignment.`
- Groene knop `Manage Rubric` plus een instellingen-icoon.
- Zoekveld `Search submissions`, `Download all (2 files)`, `Filters`.
- Tabel met kolommen `STUDENT`, `DOCUMENT`, `SUBMITTED AT`, `AI DETECTION` (groen bolletje plus label), paginering `10 per page`.

**Billing**
- `Billing & Tokens`, beschikbare tokens met voortgangsbalk, `Period usage: 0 / 2,000`, huidig plan `Free / Starter Capacity`.
- Drie plannen met maand/jaar-schakelaar: Free $0 (2.000 tokens), Teacher `Best Value` $25/maand (20.000 tokens, $1,25 per 1k), Enterprise op een navy card met `Contact sales`.

**Inlogscherm**
- Links het formulier met een groene `Sign in` en Google-login.
- Rechts een navy paneel: `AI feedback and grading for teachers`, daaronder `Generate clear rubric-based comments, feedback and consistent grading for student submissions.`, een collage van productschermen en onderaan logo's van universiteiten.

**Overige echte schermen** staan als screenshot in `Platform/usability-test/afbeeldingen/`: feedbacktab met regenerate, grading-tab, rubriccriteria bewerken, het paneel dat inzendingen verwerkt, de taal-dropdown. Dat is de beste referentie voor hoe het product er nu echt uitziet.

---

## 3. Het herontwerp, en wat daarvan geldt

In `Design/Website/app-homepage-redesign/` ligt een klikbaar prototype van een nieuwe home page (`home-redesign.html`), plus de bouwprompts. Dat is **een voorstel, geen productie**. Als je een beeld maakt van "hoe het eruit gaat zien", gebruik dat. Moet het beeld de huidige app tonen, gebruik de screenshots.

**De card**
- Drie zones: naam, dan óf één held-getal `20 to grade` met daaronder `Oldest waiting 12 days`, óf `No submissions yet`, dan een voet met `Last submission 1 day ago`.
- Precies drie tekstgroottes: naam 17px/600, held-getal 24px/600, al het andere 14px/400. Alles in Inter, **geen League Spartan op een card**. Een card in een dashboard is geen marketingpagina.
- Kleur alleen waar het iets codeert. Op de card mag alleen `Oldest waiting` kleur krijgen, rood met een waarschuwingsteken, en alleen als dat werk voorbij de deadline van zijn eigen opdracht ligt. De primaire knop is navy, groen is alleen `Completed` met een vinkje.

**De schil eromheen is óók veranderd.** Wie de nieuwe app tekent met de oude zijbalk tekent iets dat niet meer bestaat:

1. **De zijbalk is enterprise white-label.** Linksboven staat het logo van de instelling (in het prototype Universiteit Leiden), niet `EduLMS / Lecturer`, en het is geen schakelaar. De in- en uitklapknop staat in de zijbalk zelf, rechts naast het logo, en blijft op die plek staan als hij ingeklapt is.
2. **Billing, Referrals en de tokenbadge zijn eruit.** Wat overblijft is Courses met de cursuslijst, en onderin het account met Profile en Sign Out. Profile staat dus niet meer in de navigatie.
3. **Onderaan het hoofdscherm een brede balk voor Personalised learning**, met een preview, de regel `Track student growth over time` en een knop `Request access`. Dat is een teaser voor iets dat nog niet bestaat, dus teken het herkenbaar als aankondiging, niet als werkend scherm.
4. **Boven het raster een vaste zoek- en filterbalk:** zoekveld, `Status`, `Waiting`, `Overdue only`, rechts het sorteren, daaronder een regel `10 of 10 courses`. Die balk hoort in elk beeld van de nieuwe home page, hij is niet optioneel.

---

## 4. Merk en design system

Bron: `Design/Design system/`. Laad `core/` plus het oppervlak dat je maakt (`web/`, `slides/` of `internal/`), nooit de hele map.

**Kleur**
- Navy `#002333`, dat is de zwart-vervanger en de primaire knop.
- Groen `#00e075` als accent, `green-deep #007b54` voor groene tekst op wit.
- Navy-getinte neutralen: ink-900 `#0a2c3b`, 700 `#2c4a57`, 500 `#5b7480`, 300 `#a9bcc4`, 200 `#cdd9de`, 100 `#e7eef0`, 50 `#f3f7f8`.
- Danger `#b3261e`. Let op: warning `#b26a00` haalt maar 4,24:1 op wit en mag dus niet als tekst.

**De groenregel, belangrijkste kleurregel die we hebben**
Groen betekent "kijk hier" of "dit is goed afgelopen", **nooit "klik hier"**. De primaire knop is altijd navy. Groen mag op precies twee plekken: de hero-CTA van een pagina, en een bevestigde positieve status in een tool. Zet naast groen altijd een signaal dat geen kleur is, een vinkje of een label.

Let op de spanning: de echte app gebruikt nu groen voor `Create Course`, `Sign in` en `Choose plan`. Dat wijkt af van het systeem. Maak je nieuw werk, doe het navy. Teken je de huidige app na, dan is groen wat er staat.

**Type**: League Spartan voor koppen, Inter voor de rest. Nooit meer dan twee fonts.
**Radius**: 6 / 8 / 10 / 12 / 20 / vol rond, één radius per componenttype.
**Ruimte**: 8pt-familie. Interne schermen zijn dicht: rijen 36px, controls 32px, panelpadding 16px, zijbalk 240px.
**Schaduw**: drie niveaus, subtiel, navy-getint, nooit zwart en nooit gestapeld.

**Assets**: `Design/Merk/` heeft `logos/logo_navy.png`, `logos/logo_white.png`, drie productscreenshots in `product/` en de font-bestanden. Logo's niet roteren, stretchen of herkleuren.

---

## 5. Harde regels voor beelden

1. **Verzin geen functies.** Geen knop, scherm of grafiek die het product niet heeft.
2. **Geen nepscreenshot die zich voordoet als echt.** Een getekende weergave mag, maar dan als illustratie herkenbaar, en zeg erbij dat het een weergave is.
3. **Groen nooit als "klik hier"** en nooit op een getal omdat de waarde gunstig uitkomt.
4. **Klantnamen die mogen:** Hogeschool Rotterdam, De Haagse Hogeschool, Tilburg University, Radboud Universiteit. Universiteit Leiden en Radboud bouwden mee aan het model. Bij Hogeschool Rotterdam draait het bij de lerarenopleiding, claim geen andere opleiding.
5. **TIO Business School en ICM Opleidingen mogen nergens genoemd of getoond worden.** Geldt ook voor beeld.
6. **Het accuraatheidscijfer:** 94% betekent hoe dicht ons cijfervoorstel bij dat van de docent ligt, niet hoe vaak we hetzelfde cijfer geven. Komt uit de Bath Spa-pilot van juni 2026, 435 inzendingen en 13 nakijkers, 98% bij docenten die het model hadden afgestemd. Zet het nooit als "94% van de gevallen" in een beeld.
7. **Geen decoratieve gradiënten, glows of blobs**, geen pills om gewone metadata, geen kaartjes in kaartjes. Die staan op de reflexenlijst in `core/compositie.md`.

---

## 6. Waar je verder kijkt

- `Platform/product.md` — de bron voor elke claim
- `Design/Design system/core/` — tokens, regels, compositie, en `voorbeelden.html` met fout naast goed
- `Design/Design system/internal/` — als je app- of dashboard-UI tekent
- `Design/Merk/` — logo's, fonts, productscreenshots
- `Platform/usability-test/afbeeldingen/` — echte schermen van de huidige app
- `Design/Website/app-homepage-redesign/` — het herontwerp plus de bouwprompts
- `Design/Merk/brand-guidelines.md` — merk breed
