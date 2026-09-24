# Leerpunten business-case

Append-only. Elke opmerking van Dante op een run komt hier terecht, ook als er nog geen regel uit volgt. De skill leest dit bestand voordat hij begint.

Format: `[JJJJ-MM-DD] account: wat er mis was | welke schakel | wat ermee gedaan is`

## Hoe dit werkt

- Feedback uit de chat schrijf ik hier zelf naartoe, dezelfde beurt, en ik meld dat in één regel.
- Eén keer is een correctie: hij staat hier en wordt verwerkt in de run waar hij over ging.
- Twee keer hetzelfde is een patroon: ik leg de regeltekst voor die ik in `SKILL.md` of `reference.md` wil zetten. Pas na akkoord pas ik de skill aan. Zie `.claude/rules/feedback.md`.
- Nieuwe feedback die oude tegenspreekt wint. De oude regel gaat dan weg.

## De schakels

Feedback die een schakel aanwijst kan ik verwerken. "Dit is niet goed" niet: dan vraag ik in één regel welke schakel het was.

| Schakel | Wat er dan mis is | Voorbeeld |
|---|---|---|
| **Bronnen** | een bron gemist of verkeerd gelezen | "dit stond in de mail van 12 september, dat had je moeten zien" |
| **Fase** | de fase verkeerd ingeschat | "we zitten nog in discovery, niet in scoping" |
| **Gat** | iets als gat gezien dat we al weten, of een gat gemist | "het volume weten we al, dat zei ze in het eerste gesprek" |
| **Metric-oordeel** | de kwaliteit of de verbetertip klopt niet | "dat is geen schatting, dat komt uit hun workload-model" |
| **Timing** | nu of later verkeerd | "dit kan ik haar prima nu vragen" |
| **Wie weet het** | de verkeerde persoon of afdeling | "dat weet de examencommissie niet, dat ligt bij het onderwijsbureau" |
| **Formulering** | de vraag klinkt niet als Dante, of is dicht of loos | "zo zou ik dit nooit vragen" |
| **Risico-antwoord** | de claim klopt niet of mist | "de AVG dekken we ook, zet dat erbij" (dan eerst in `product.md`) |
| **Business case (stand 2)** | toon, opbouw, getal | "dit leest als onze pitch, niet als hun document" |

## Log

- [2026-09-24] academica: vragen niet gesplitst in mail vooraf en live, geen onderbouwing van het aantal, en Engelse labels in de toelichting | Formulering / Timing | Dante heeft zelf de regels voor kanaal, aantal en taal geschreven; overgenomen in SKILL.md stap 5 en het format in reference.md. Run Academica opnieuw ingedeeld.
