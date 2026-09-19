# Leerpunten agent 3

Append-only. Elke correctie op een haakje of een dossier komt hier, ook als er nog geen regel uit volgt. Lees dit bestand voordat je een batch begint.

Format: `[JJJJ-MM-DD] persoon of batch: wat er mis was | welke stap het was | wat ermee gedaan is`

## Waarom dit bestand bestaat

Jouw haakje is waar het hele bericht op staat. Is het haakje mis, dan is het bericht mis, hoe goed agent 4 ook schrijft. Dit bestand is het geheugen tussen de rondes.

## Feedback die werkt

| Stap | Wat er dan mis is | Bruikbare feedback klinkt als |
|---|---|---|
| **De bron openen** | geciteerd op titel zonder het stuk te lezen | "dat rapport zegt iets anders, je hebt alleen de samenvatting gezien" |
| **Het citaat** | letterlijk onjuist, of samengevat alsof het een citaat is | "dat staat er niet zo, dat is jouw parafrase" |
| **De drager** | de last ligt bij de student, niet bij de beoordelaar | "studeerbaarheid gaat over de student, dat is niet onze pijn" |
| **Het niveau** | te zwak om een bericht op te bouwen | "dit is algemene organisatie-info, daar kun je niets mee openen" |
| **Het toetsprogramma** | onbekend gelaten terwijl het te vinden was | "de studiegids noemt het gewoon, je hebt er niet gekeken" |
| **Het vermoeden** | een begrip ingevuld dat de bron niet noemt | "het woord feedback komt in zijn hele stuk niet voor" |
| **Niet gevonden** | iets verzonnen in plaats van te melden dat het er niet is | "zeg dan gewoon dat het niet online staat" |

Een haakje dat je niet vertrouwt hoort in `## Onzekerheden` van het dossier, niet weggelaten. Agent 4 kan met een gemelde twijfel werken, met een verzwegen twijfel niet.

## Log

- [2026-08-13] THIM van der Laan: een NVAO-citaat over studeerbaarheid gebruikt om iets over de nakijklast van docenten te zeggen. Thim wees de mail af met precies dat verschil: *"Dit is de studeerbaarheid voor de student. De oplossing die jij aanbiedt probeert meer de organisatie in efficientie e.d. te ondersteunen. Dat zijn twee verschillende dingen."* | De drager: alle woorden stonden in de bron en alle getallen klopten. Het goede haakje lag er ook, twee onafhankelijke beoordelaars op de scriptie, maar dat stond niet in het dossier. | Dragertoets verplicht, elk citaat draagt zijn drager, vaktermentabel per markt.
- [2026-07-22] algemeen: Agent-4-leads krijgen diep documenten-lezend onderzoek (NVAO-rapport, visiedocument, OER), niet de summiere skim. | De bron openen: de skim veranderde regelmatig van niveau en ICP-fit zodra iemand het stuk echt las. | Bevindingen naar het dossier, samenvatting van 200 tekens naar de velden.
- [2026-xx-xx] algemeen: een scriptie of pagina die je niet kunt openen, citeer je niet op de titel. | Niet gevonden: zeg "niet online te vinden" en vraag een koude prospect nooit om materiaal. | Vaste regel, zie memory not-findable-say-so.
- [2026-09-17] Besluit Dante: e-mailadres actief zoeken (één standaardpagina per persoon), niet alleen noteren als je het toevallig tegenkomt. Eerste versie van deze regel (eerder diezelfde dag) was te passief, teruggedraaid. | Het e-mailadres. | Sectie "Het e-mailadres: actief zoeken, één keer per persoon" toegevoegd: check eerst of `email` al gevuld is (dedup met agent 2), zo niet bezoek één standaardpagina, zo niet dan `email_status=niet gevonden` en geen tweede poging. Reden: Lemlist's enrichment kost Dante credits die een gerichte zoekactie hier niet kost.
- [2026-09-17] Besluit Dante: telefoonnummer meenemen als bijvangst, géén aparte zoekactie zoals bij e-mail — wel meeschrijven als je het toevallig ziet op een profiel- of staffpagina. | Nieuw veld `telefoon` (na `email_status`). | Regel toegevoegd direct na de e-mailsectie. Veld toegevoegd aan PERSON_COLS in pipeline.py.
