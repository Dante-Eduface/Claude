# Pijn en oplossing uit Close

Eén pagina met alles wat prospects en klanten in Close hebben gezegd over hun pijn, gewenste uitkomst, bezwaren en huidige aanpak, per thema, met onze oplossing eronder (alleen claims uit `references/eduface-product.md`).

## Bestanden
- `pijn-oplossing.html` — de pagina. Open via `node projects/website-building/serve.mjs` vanuit de repo-root en ga naar `http://localhost:3000/projects/pijn-oplossing/pijn-oplossing.html` (of dubbelklik, werkt ook zonder server). Dante beoordeelt hier per uitspraak: klopt (y) of weg (n), met notitie (o). Knop "Kopieer besluiten" zet zijn besluiten als JSON op het klembord.
- `besluiten.json` — daar plakt Dante (of ik) de gekopieerde besluiten in. Formaat: `{stand, klopt:[ids], weg:[ids], notities:{id:tekst}}`. Dit is wat het volgende Claude-venster leest.
- `items.json` — alle uitspraken, één object per regel-item, machine-leesbaar. Veldnamen staan in `EXTRACTIE-INSTRUCTIE.md`.
- `pijn-bibliotheek.md` — dezelfde inhoud als de pagina, leesbaar zonder browser.
- `themas.json` — thema's, definities, oplossingsteksten en de mapping van agent-slugs naar eindthema's.
- `extractie/*.json` — ruwe extractie per Close-lead (door subagents, één bestand per dossier).
- `close-dump/*.md` — de Close-bron per lead (meetings met summary en user_note, calls met notitie, notes, inbound mails). `_index.tsv` = overzicht.
- `close_alles.py` — dumpt alle leads met inhoud opnieuw (hervatbaar). `build.py` — bouwt items.json, de html en de md opnieuw uit extractie/ en themas.json.

## Verversen
```bash
python3 projects/pijn-oplossing/close_alles.py projects/pijn-oplossing/close-dump   # nieuwe Close-data (slaat al gedumpte leads over; verwijder _index.tsv voor een volledige refresh)
python3 projects/pijn-oplossing/build.py                                            # pagina + md opnieuw
```
Nieuwe dossiers moeten opnieuw door de extractie (zie `EXTRACTIE-INSTRUCTIE.md`), dat doet build.py niet zelf.

## Voor het volgende venster
Lees `besluiten.json` en `items.json`. Alles in `weg` negeren. Alles in `klopt` is door Dante bevestigd. Items zonder besluit zijn niet beoordeeld. Notities zijn Dante's correcties op een item.
