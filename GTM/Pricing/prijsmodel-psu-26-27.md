# Prijsmodel: per student per maand (vanaf 16-09-2026, herzien 22-11-2026)

Besluit Dante, 16-09-2026. Vervangt `prijsmodel-nl-opleiding-26-27.md` (staffel A-E plus toolfee), dat is verplaatst naar `Archive/`.

## Het model

**3 per student per maand, in de valuta van de markt.** Drie euro in Nederland, drie pond in het Verenigd Koninkrijk, drie dollar in de Verenigde Staten. Hetzelfde getal, geen omrekening: het is een prijspunt, geen wisselkoers.

Gerekend over **12 maanden**, dus 36 per student per jaar. **Exclusief btw** (licentiesjabloon art. 5.6 en Bijlage 1: alle bedragen in euro en exclusief btw).

**Minimum: 1.500 per maand** (Dante, 22-11-2026). Dat is 500 studenten maal 3 en dekt dus 500 studenten. Het sjabloon heeft hiervoor de regel "Minimumvergoeding" in het Orderformulier. Of het minimum in pond en dollar ook 1.500 is staat open (A12).

**Alle studenten die de opleider heeft**, niet alleen de studenten van de opleidingen die met Eduface werken. Instellingsbreed dus.

## De drempel

**Minimaal 500 lerenden per jaar** (was 300, Dante 22-11-2026). Daaronder gaat een opleider niet de outreach in.

Bij 500 studenten is dat 18.000 per jaar, 1.500 per maand, precies het minimum hierboven.

**Nog niet doorgevoerd in de code.** `pipeline.py` toetst sinds 17-09-2026 op een jaarwaarde van 10.000 in de valuta van de markt (dat is 278 lerenden), niet op een lerendenaantal. 500 lerenden is 18.000. Zie A13 in `Context/open-vragen.md`.

## Wat hiermee verdwenen is

- **De staffel A tot E.** De prijs schaalt nu vloeiend met het aantal studenten in plaats van in vijf sprongen.
- **De toolfee van 7.500 per opleiding.** Daarmee is `aantal_opleidingen` geen prijsfactor meer. Het blijft een nuttig veld om te zien hoe breed een uitrol kan worden, maar het bepaalt de dealwaarde niet.
- **De betaalbaarheidstoets** (onze fee mag hoogstens 10% van de programma-omzet zijn). Die was nodig omdat een vaste fee van 10.000 een kleine opleider kon verpletteren. Bij een prijs per student schaalt de rekening vanzelf mee met de omvang van de klant, dus de toets doet niets meer. `cursusprijs` blijft als context voor het gesprek, maar is geen poort.

## Waar het in de code staat

`.claude/scripts/pipeline.py`:

- `PRIJS_PER_STUDENT_MAAND = 3`, `MAANDEN_PER_JAAR = 12`, `DREMPEL_JAARWAARDE = 10000` (sinds 17-09-2026 een omzetdrempel, geen lerendenaantal)
- `bereken_jaarwaarde(lerenden)` is nu een vermenigvuldiging, geen staffel-opzoeking
- `omvang_oordeel()` (poort 0d) vergelijkt de jaarwaarde (lerenden maal prijs) met de drempel, meer niet
- `SEGMENT_GRENZEN = [(300, "micro"), (1000, "klein"), (3000, "midden")]`, daarboven `groot`

Per markt overschrijfbaar in `GTM/ICP/shift/markets/<code>/profiel.json` onder `prijs_per_student_maand`, `maanden_per_jaar`, `drempel_jaarwaarde` en `segment_grenzen`.

## Wat dit betekent voor het sourcen

`lerenden_per_jaar` is hiermee het belangrijkste veld van de hele pijplijn geworden: het is de prijs, het is de drempel, en het is het segment waarop we meten of de outreach werkt. Op 16-09-2026 was het bij 84 van de 776 organisaties gevuld. Dat is de eerste achterstand om in te lopen.
