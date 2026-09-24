# Prijsmodel: per student per maand (vanaf 16-09-2026)

Besluit Dante, 16-09-2026. Vervangt `prijsmodel-nl-opleiding-26-27.md` (staffel A-E plus toolfee), dat is verplaatst naar `Archive/`.

## Het model

**3 per student per maand, in de valuta van de markt.** Drie euro in Nederland, drie pond in het Verenigd Koninkrijk, drie dollar in de Verenigde Staten. Hetzelfde getal, geen omrekening: het is een prijspunt, geen wisselkoers.

Gerekend over **12 maanden**, dus 36 per student per jaar.

**Alle studenten die de opleider heeft**, niet alleen de studenten van de opleidingen die met Eduface werken. Instellingsbreed dus.

## De drempel

**Minimaal 500 lerenden per jaar** (verhoogd van 300 op 24-09-2026, besluit Dante, geldt voor alle klanten en markten).

Bij 500 studenten is dat 18.000 per jaar.

Waarom 500: per instelling richten we AI-capaciteit in, en onder de 500 studenten komen we met de inkoop daarvan niet uit (claim bevestigd door Dante, staat in `Platform/product.md`). Daarnaast maken we per instelling vaste kosten die niet meegroeien met het aantal studenten, zoals de koppeling met het LMS, het afstemmen van het model op hun rubrics en de begeleiding bij de start. Onder de 500 wegen die te zwaar. Zo is het ook aan Academica uitgelegd (mail 24-09-2026).

Waarom in lerenden en niet in geld: 500 lerenden is in elke markt hetzelfde getal. Let op: `pipeline.py` rekent sinds 17-09-2026 met een omzetdrempel (`DREMPEL_JAARWAARDE = 10000` in de valuta van de markt), niet met lerenden. Die staat nog niet op de nieuwe drempel.

**OPEN (24-09-2026):**
- Betaalt een klant onder de 500 lerenden de prijs van 500 (een minimumprijs van 18.000), of valt hij af?
- Gaat de drempel in de pijplijn ook omhoog naar 18.000 per jaar? Dat haalt alle opleiders tussen ongeveer 280 en 500 lerenden uit de outreach.

## Wat hiermee verdwenen is

- **De staffel A tot E.** De prijs schaalt nu vloeiend met het aantal studenten in plaats van in vijf sprongen.
- **De toolfee van 7.500 per opleiding.** Daarmee is `aantal_opleidingen` geen prijsfactor meer. Het blijft een nuttig veld om te zien hoe breed een uitrol kan worden, maar het bepaalt de dealwaarde niet.
- **De betaalbaarheidstoets** (onze fee mag hoogstens 10% van de programma-omzet zijn). Die was nodig omdat een vaste fee van 10.000 een kleine opleider kon verpletteren. Bij een prijs per student schaalt de rekening vanzelf mee met de omvang van de klant, dus de toets doet niets meer. `cursusprijs` blijft als context voor het gesprek, maar is geen poort.

## Waar het in de code staat

`.claude/scripts/pipeline.py`:

- `PRIJS_PER_STUDENT_MAAND = 3`, `MAANDEN_PER_JAAR = 12`, `DREMPEL_LERENDEN = 300` (verouderd, zie de drempel hierboven)
- `bereken_jaarwaarde(lerenden)` is nu een vermenigvuldiging, geen staffel-opzoeking
- `omvang_oordeel()` (poort 0d) vergelijkt het aantal lerenden met de drempel, meer niet
- `SEGMENT_GRENZEN = [(300, "micro"), (1000, "klein"), (3000, "midden")]`, daarboven `groot`

Per markt overschrijfbaar in `GTM/ICP/shift/markets/<code>/profiel.json` onder `prijs_per_student_maand`, `maanden_per_jaar`, `drempel_lerenden` en `segment_grenzen`.

## Wat dit betekent voor het sourcen

`lerenden_per_jaar` is hiermee het belangrijkste veld van de hele pijplijn geworden: het is de prijs, het is de drempel, en het is het segment waarop we meten of de outreach werkt. Op 16-09-2026 was het bij 84 van de 776 organisaties gevuld. Dat is de eerste achterstand om in te lopen.
