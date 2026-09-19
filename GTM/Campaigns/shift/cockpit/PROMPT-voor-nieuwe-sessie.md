Ik wil de SHIFT-cockpit bouwen: één pagina waarop Jeroen en ik elke ochtend de outreach-pijplijn afhandelen. Publiceer hem als Artifact.

## Wat SHIFT is

Een keten van vijf agents die particuliere opleiders vindt, de juiste persoon opzoekt, onderzoekt waar we op kunnen aanhaken, en daar berichten bij schrijft. Alles staat in `GTM/Campaigns/shift/master/` en wordt beheerd door `.claude/scripts/pipeline.py`. Lees `GTM/Campaigns/shift/CLAUDE.md` en `GTM/Campaigns/shift/master/LEESMIJ.md` voordat je begint.

## De databron

```bash
python3 .claude/scripts/pipeline.py --markt nl cockpit --out /tmp/cockpit-nl.json
```

Ongeveer 130 kB met vier blokken. Draai het commando zelf en kijk in het bestand; de vorm staat daar, niet in deze prompt.

- `stand` + `assen` → het dashboard. Vier meetassen (omvang, functie, haakje, markt) met per segment verstuurd, geaccepteerd, gereageerd, plus `accept` en `reactie` als percentage.
- `goedkeuren` → de berichten die op goedkeuring wachten, met het haakje, de bron, alle drie de berichten, de redenering (`waarom_dit_bericht`) en de twijfels.
- `reacties` → wie er antwoordde, met de tekst die ze schreven. Ongeduide eerst.
- `agents` → per agent voorraad, klaar, en waar het blijft liggen.

De pagina leest deze export en praat zelf niet met het master-document.

## Wat de pagina moet kunnen

**1. Dashboard.** Waar staat de pijplijn, en werkt het. Elke as-rij heeft een veld `oordeel` dat "te weinig volume (n van 30)" zegt als er te weinig data is. Toon dat letterlijk in plaats van een percentage; het is de rem tegen conclusies op zes leads.

**2. Goedkeuren.** Het hoofdscherm, hier zit Jeroen elke ochtend. Per bericht: goedkeuren, afkeuren, of aanpassen. Belangrijker dan het oordeel is de **feedback op agent 4**, de agent die de berichten schrijft. Geef die feedback echte ruimte: `waarom_dit_bericht` staat in de data, en een reactie op die redenering is bruikbaarder dan een oordeel over de uitkomst. Denk aan: wat klopt er niet aan het haakje, waarom landt deze opening niet, wat had hij moeten zien.

**3. Reacties.** Prospects die antwoordden. Per reactie de tekst die ze schreven plus het bericht waarop ze reageerden, en een veld om vast te leggen wat de uitkomst was en waarom, in hun eigen woorden. Op dit moment wachten er elf op duiding.

**4. Agents.** Hoe doet elke agent het, wat zijn de gaten, en ruimte voor verbetervoorstellen op basis van de cijfers.

## Technische randvoorwaarden

- **Gebruik de `db`-capability**, niet localStorage. Wat Jeroen invult moet ik in een volgende sessie kunnen terugzetten in het master-document. Laad de `artifact-capabilities` skill voor je begint.
- **`person_id` is de sleutel** in beide richtingen. Een goedkeuring wordt straks `pipeline.py set <person_id> --set bericht_status=goedgekeurd`.
- **Er is geen `user`-capability op dit account**, dus de pagina weet niet wie er kijkt. Voor "wie gaf deze feedback" is een handmatige keuze nodig die in localStorage blijft.
- **Declareer geen `mcp`-capability.** De data komt via de export, en die verversen we één keer per 24 uur om credits te sparen.

## Design

Verplicht, voordat je iets bouwt: `Design/System/core/proces.md` en de drie poorten daarin. Dit is een interne tool, dus laad `core/` plus `internal/`, nooit `web/` of `slides/`.

Let op de spanning die daar zit: `internal/starten.md` schrijft Next.js met shadcn voor, maar dit wordt een Artifact, dus één zelfstandig HTML-bestand. Neem de tokens, de dichtheid (rijen 36px, controls 32px, panelpadding 16px) en de regel dat de primaire knop navy is en groen alleen status betekent. Neem de stack niet over.

Twee bestaande pagina's zijn het bekijken waard als vorm: `Archive/targetlijst-nl-oud/berichten-review.html` (de reviewkaarten die we eerder hadden) en `GTM/sales-coach/sales-coach.html` (de sidebar-app die nu in gebruik is).

## Wat ik niet wil

- Geen herbouw van wat Lemlist of Close al laten zien.
- Geen percentages op segmenten met te weinig volume.
- Geen automatisch verzenden of importeren vanuit de pagina. Goedkeuren is een besluit, versturen blijft een aparte handeling.

Begin bij poort 1: twee richtingen in woorden, met je eigen voorkeur erbij.
