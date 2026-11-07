# Geldplan

_Laatst bijgewerkt: 07-11-2026._

**Wat is dit:** Dante's uitgavenagenda. Blader per maand of per week en zie per dag waar zijn geld heen ging. Eén zelfstandig HTML-bestand, geen build en geen dependencies.

**Fase:** in gebruik. Alleen om naar te kijken, niet om in te werken (besluit 28-09-2026: het geldwerk loopt via de chat).

**Volgende stap:** de potjes, Curaçao met de twee salarismomenten, en de weg naar 10.000 onder de kalender zetten. Die stonden op de vorige versie.

## Code hier, data niet

`geldplan.html` in deze map heeft een **lege** `DAG`-constante. Transactieregels horen niet in de repo; dat is vastgelegd op 19-09-2026 en op 07-11-2026 bevestigd toen een commit met 50 transactieregels terecht geweigerd werd.

De gepubliceerde pagina wordt gemaakt met:

```
python3 bouw.py <map-met-ABN-exports> <uitvoer.html>
```

`bouw.py` leest `.TAB` (tabgescheiden) en `.STA` (MT940), ontdubbelt over elkaar overlappende exports, gooit overboekingen tussen eigen rekeningen eruit, en zet elke post in een groep. De uitvoer gaat naar een pad buiten de repo en die wordt gepubliceerd.

## De drie groepen

| Groep | Wat erin valt |
|---|---|
| **Vast** | Komt elke maand hoe dan ook: NS, 100 huur aan zijn moeder, 129,45 zorgpremie, Trainmore, en de kapper die hij contant pint |
| **Boodschappen** | Eten en huishouden: supermarkt, bakker, Picnic, drogist, apotheek |
| **Rest** | Alles waar hij per keer voor kiest: uit eten, café, tanken, bol.com, kleermaker, een dagje weg |

De pinopname bij Geldmaat is de kapper. Dat weet ik van Dante, niet uit het afschrift, en het staat daarom expliciet in de mapping in `bouw.py`.

## Wat de pagina doet

- Pijlen vorige en volgende, een knop Vandaag, en een schakelaar Maand/Week.
- **Maand:** per dag de drie groepen, met weeknummer en weektotaal in de linkerkolom.
- **Week:** per dag de losse posten met hun categorie, want daar is ruimte voor.
- Een maand zonder dagdata toont het maandtotaal uit `MAANDTOT` plus de melding dat er een export nodig is.

## Wat hier niet staat

De ruwe ABN-afschriften en de gevulde pagina. De standen en de conclusies staan in `Context/financien.md`, dat de bron blijft. Bij tegenspraak wint dat bestand, niet de pagina.
