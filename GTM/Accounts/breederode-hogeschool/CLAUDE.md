# Breederode Hogeschool — kennisbank

Alles wat we weten over Breederode Hogeschool, op 09-09-2026. Bedoeld om als eigen Claude Code-venster te gebruiken: open deze map en je hebt het hele account in context.

## Wat is dit account
Particuliere hogeschool in Rotterdam, zorg en welzijn, deeltijd voor werkende professionals. Sinds 2024/2025 onderdeel van **Calder Holding**. **Lopende deal met Eduface**, fase Discovery, testochtend op locatie op **woensdag 23 september 2026, 9:00-12:30**.

## Bestanden
- [01-organisatie.md](01-organisatie.md) — wie ze zijn, eigenaar, locaties, keurmerken, omvang
- [02-mensen.md](02-mensen.md) — iedereen met naam, rol, mailadres en positie in de deal
- [03-opleidingen.md](03-opleidingen.md) — het hele portfolio met niveau, duur en prijs
- [04-toetsing.md](04-toetsing.md) — hoe ze toetsen en beoordelen, met citaten uit de NVAO-rapporten. Dit is het Eduface-hart
- [05-eduface-deal.md](05-eduface-deal.md) — tijdlijn, MEDDPICC, succescriteria, prijs, open punten
- [06-taal-en-haakjes.md](06-taal-en-haakjes.md) — hun vocabulaire en de haakjes met bron
- [07-beloofde-features.md](07-beloofde-features.md) — alles wat we ze over de tool hebben verteld, met een inschatting of het al bestaat
- `transcripts/` — uitgeschreven gesprekken van 01-09 en 03-09 (Close Notetaker)
- `bronnen/` — de twee NVAO-visitatierapporten als PDF en als tekst
- `raw/` — alle 106 pagina's van breederode.nl (WordPress REST-dump van 09-09-2026)

## Regels voor dit account
- Elke claim over Breederode moet terug te voeren zijn op `bronnen/`, `raw/` of Close. Staat het er niet, dan beweer je het niet.
- Productclaims over Eduface komen uit `references/eduface-product.md`, nergens anders vandaan.
- Hun woord is **navolgbaarheid**, niet consistentie. Zie 06.
- De site verversen: `python3` script in de projectgeschiedenis, of opnieuw via `https://breederode.nl/wp-json/wp/v2/posts?per_page=50`.
