# Geldplan

_Laatst bijgewerkt: 20-09-2026._

**Wat is dit:** Dante's eigen geldplan-app. Potjes, een dagelijkse saldo-check, een maandoverzicht en een projectie naar 10.000 euro vermogen. Eén zelfstandig HTML-bestand, geen build en geen dependencies: openen in een browser en het werkt.

**Fase:** in gebruik. Draait sinds 20-09-2026 op `localStorage` in plaats van de Claude-artifactruntime.

**Volgende stap:** G16 en G17 uit `Context/open-vragen.md` beantwoorden, dan `reizen` en het doel van het zorgpotje bijstellen.

## Hoe het werkt

- **Opslag:** `localStorage`, sleutel `eduface.geldplan.v1`. Namespaced omdat Chrome bij `file://` alle lokale bestanden als dezelfde origin ziet. Safari blokkeert `localStorage` op `file://`; werkt het daar niet, serveer het bestand dan via een lokale server.
- **Startwaarden** staan hardcoded in het object `D`, met een `seed`-vlag die ze eenmalig forceert. Nu `seed7`, op de stand van 18-09-2026. Wil je opnieuw seeden, hernoem de vlag naar `seed8` en zet de nieuwe bedragen erin.
- **Maandcijfers** staan als `MAANDEN`-constante in de code. Bewust geen import van afschriften: categoriseren gebeurt buiten de app, dat houdt hem dom en voorspelbaar.
- **Rekeningkoppeling** staat in `POTREK`. Trade Republic heeft geen ABN-nummer en vul je met de hand in.

| Potje | ABN-rekening | Naam in de ABN-app |
|---|---|---|
| Betaalrekening | 882235753 | DE TORBED |
| Uit huis fonds | 884479609 | Savings |
| Curaçao | 118499882 | Curacao |
| Zorgtoeslag | 142509299 | Zorgverzekering |
| Aandelen | Trade Republic | handmatig |

Rekening 147953219 staat op expired en doet niet mee.

## Wat hier niet staat

De ruwe ABN-afschriften. Die blijven buiten de repo. De cijfers die eruit volgen staan in `Context/financien.md`.

## Leest hieruit

`Context/financien.md` is de bron voor de standen en de verdeling. Bij tegenspraak wint dat bestand, niet de app.
