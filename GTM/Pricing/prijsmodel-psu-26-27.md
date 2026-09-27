# Prijsmodel: per student per maand (vanaf 16-09-2026)

Besluit Dante, 16-09-2026. Vervangt `prijsmodel-nl-opleiding-26-27.md` (staffel A-E plus toolfee), dat is verplaatst naar `Archive/`.

## Het model

**3 per student per maand, in de valuta van de markt.** Drie euro in Nederland, drie pond in het Verenigd Koninkrijk, drie dollar in de Verenigde Staten. Hetzelfde getal, geen omrekening: het is een prijspunt, geen wisselkoers.

Gerekend over **12 maanden**, dus 36 per student per jaar.

**Alle studenten die de opleider heeft**, niet alleen de studenten van de opleidingen die met Eduface werken. Instellingsbreed dus.

## De drempel

**Minimaal 300 lerenden per jaar.** Daaronder gaat een opleider niet de outreach in.

Bij 300 studenten is dat 10.800 per jaar, ongeveer waar de oude staffel A op uitkwam. De drempel is dus niet strenger geworden, alleen uitgedrukt in iets dat je kunt opzoeken.

_27-09-2026: als prijs achterhaald. Het kleinste contract is 500 studenten, zie hieronder. Of 300 de outreachdrempel blijft staat open._

Waarom in lerenden en niet in geld: 300 lerenden is in elke markt hetzelfde getal. De oude geldvloer moest per markt omgerekend worden (NL 10.000 euro, UK 8.500 pond), en dan zijn de markten niet meer naast elkaar te leggen.

## De kleinste staffel

Dante, 27-09-2026: *"onze kleinste staffel is minimaal 500 studenten."* Het kleinste contract is dus 500 x 36 = **18.000 per jaar**. Dat bedrag staat in Close ook op elke Deal-kaart waarvan de dealwaarde nog onduidelijk is.

OPEN: blijft 300 lerenden de outreachdrempel, en moet `bereken_jaarwaarde` met de ondergrens van 500 rekenen? Tot dat beantwoord is rekent `pipeline.py` zonder ondergrens. Zie W6 in `Context/open-vragen.md`.

## Wat hiermee verdwenen is

- **De staffel A tot E.** De prijs schaalt nu vloeiend met het aantal studenten in plaats van in vijf sprongen.
- **De toolfee van 7.500 per opleiding.** Daarmee is `aantal_opleidingen` geen prijsfactor meer. Het blijft een nuttig veld om te zien hoe breed een uitrol kan worden, maar het bepaalt de dealwaarde niet.
- **De betaalbaarheidstoets** (onze fee mag hoogstens 10% van de programma-omzet zijn). Die was nodig omdat een vaste fee van 10.000 een kleine opleider kon verpletteren. Bij een prijs per student schaalt de rekening vanzelf mee met de omvang van de klant, dus de toets doet niets meer. `cursusprijs` blijft als context voor het gesprek, maar is geen poort.

## Waar het in de code staat

`.claude/scripts/pipeline.py`:

- `PRIJS_PER_STUDENT_MAAND = 3`, `MAANDEN_PER_JAAR = 12`, `DREMPEL_LERENDEN = 300`
- `bereken_jaarwaarde(lerenden)` is nu een vermenigvuldiging, geen staffel-opzoeking
- `omvang_oordeel()` (poort 0d) vergelijkt het aantal lerenden met de drempel, meer niet
- `SEGMENT_GRENZEN = [(300, "micro"), (1000, "klein"), (3000, "midden")]`, daarboven `groot`

Per markt overschrijfbaar in `GTM/ICP/shift/markets/<code>/profiel.json` onder `prijs_per_student_maand`, `maanden_per_jaar`, `drempel_lerenden` en `segment_grenzen`.

## Wat dit betekent voor het sourcen

`lerenden_per_jaar` is hiermee het belangrijkste veld van de hele pijplijn geworden: het is de prijs, het is de drempel, en het is het segment waarop we meten of de outreach werkt. Op 16-09-2026 was het bij 84 van de 776 organisaties gevuld. Dat is de eerste achterstand om in te lopen.
