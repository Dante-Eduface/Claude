# Dealwaarde berekenen bij betalen per actieve student

_Aangelegd 2026-11-16. Voorstel, nog niet bevestigd door Dante. Tot dat zo is, geldt `prijsmodel-psu-26-27.md`._

## Het probleem

Nu: **dealwaarde = alle studenten × 3 × 12.** Dat gaat ervan uit dat elke student vanaf maand 1 het hele jaar betaalt. Het contract (art. 5) rekent iets anders af: alleen studenten van wie minstens één inlevering door het platform is gegaan, en alleen vanaf die maand. Het huidige getal is dus het **plafond**, niet de verwachte omzet.

## De formule

**Jaarwaarde = N × p × m × 3**

| Symbool | Wat | Waar het vandaan komt |
|---|---|---|
| N | totaal studenten van de instelling | openbare cijfers, zoals nu |
| p | aandeel studenten dat dit jaar minstens één inlevering via Eduface doet | hoeveel vakken/docenten meedoen, uit het gesprek |
| m | gemiddeld aantal factureerbare maanden per bereikte student in dat jaar | startmaand, toetsmomenten, en hoe de student weer uit de telling gaat (zie hieronder) |
| 3 | prijs per student per maand | `prijsmodel-psu-26-27.md` |

Het huidige model is het speciale geval p = 1 en m = 12.

## Wat m bepaalt volgens het contract

- **Start:** een student telt vanaf de maand van zijn eerste verwerkte inlevering (5.2). Een vak dat pas in december toetst, levert voor die studenten september tot november niets op.
- **Stop met LMS-koppeling (5.4, eerste zin):** de student blijft tellen zolang hij actief staat in het LMS, **ook als hij niets meer inlevert.** Dus wie in oktober één paper indient, telt door tot hij afstudeert of uitschrijft.
- **Stop zonder koppeling (5.4, tweede zin):** de student telt tot zes maanden na zijn laatste inlevering. Een vak van drie maanden levert dan zo'n negen factureerbare maanden op, niet drie.
- **Uitstroom:** afstudeerders vallen in de zomer weg, dat drukt m in het laatste kwartaal van het jaar.

Belangrijk: het idee "sommige studenten zitten maar 3 maanden op het platform" klopt voor het gebruik, maar door 5.4 niet voor de factuur. Zie de open vraag onderaan.

## Drie scenario's, voorbeeld 5.000 studenten, jaar 1

| Scenario | p | m | Jaarwaarde | % van plafond |
|---|---|---|---|---|
| Voorzichtig (één faculteit, late start) | 10% | 6 | 9.000 | 5% |
| Basis (een paar opleidingen, start na eerste kwartaal) | 25% | 8 | 30.000 | 17% |
| Sterk (instellingsbrede uitrol in het eerste semester) | 50% | 10 | 75.000 | 42% |
| Plafond (huidige rekensom) | 100% | 12 | 180.000 | 100% |

De getallen voor p en m zijn aannames om mee te rekenen, geen benchmark. Er bestaat geen betrouwbaar openbaar cijfer voor welk deel van de vakken een tool in jaar 1 oppakt; een vendor-bron noemt onder 20% docentadoptie voor institutionele AI-tools. Zodra de eerste klanten een jaar draaien, vervangen hun echte p en m deze aannames.

## Wat ik zou vastleggen per deal in Close

1. **Plafond** (N × 36): hoe groot de klant kan worden. Voor prioriteren.
2. **Verwachte jaar-1-waarde** (N × p × m × 3, basisscenario): dit wordt de opportunity-waarde.
3. **Committed** (Annual Commitment, art. 6): het enige deel dat vast is. Zodra een klant committeert, is dat de harde ondergrens.

Dat volgt de gangbare praktijk bij usage-based SaaS: committed en verwachte consumptie apart houden, de rest in scenario's.

## Gevolg voor de prioriteit

`current-priorities.md` gaat uit van gemiddeld 50.000 per deal. Met de basisaannames (p 25%, m 8) is daarvoor een instelling van ruim **8.300 studenten** nodig in jaar 1, tegen 1.389 in de huidige rekensom. Óf de gemiddelde dealwaarde gaat over meerdere jaren, óf het doel hoort bij het plafond en niet bij jaar 1. Niet zelf aangepast, ligt bij Dante.

## Open

- Zie `Context/open-vragen.md`, P-vragen van 16-11-2026.
