# Home page redesign, app.eduface.me

Losstaand klikbaar prototype. Raakt de productiecode niet.

- Bestand: `home-redesign.html`. Open hem in Chrome (bestand naar een tabblad slepen).
- Techniek: Tailwind via CDN plus gewone JavaScript, alles in één bestand. Geen build, geen server.
- Gebouwd naar `bouwprompt-cards.md` (versie 04-09-2026 13:48, inclusief de filter-delta).
- Scope: Enterprise. De lege staat van een gloednieuw account blijft onaangeroerd.

## De gedeelde definitie

> Een inzending **wacht** zolang de docent hem niet heeft goedgekeurd.

Daaruit volgt: `to grade` is het aantal wachtende inzendingen, `oldest waiting` is de oudste daarvan geteld vanaf het moment dat de student inleverde, en `Completed` betekent dat er niets meer wacht en er niets meer bij kan komen.

## De card

Drie zones:

1. **Identiteit.** Alleen de cursusnaam. Rechtsboven `Archived` of `Completed ✓` als die gelden.
2. **Status.** Eén held-getal met zijn woord op dezelfde regel (`20 to grade`), daaronder één gewone regel (`Oldest waiting 12 days`). Kan er niets wachten, dan staat er alleen `No submissions yet`.
3. **Voet.** `Last submission 1 day ago`. Nooit iets ingeleverd, dan blijft de voet leeg.

**Typografie ligt vast op drie groottes**: naam 17px/600, held-getal 24px/600, al het andere 14px/400, alles in Inter. Geen League Spartan op de card, dat is typografie van het web-oppervlak.

**Kleur.** `Oldest waiting` is het enige element op de card dat kleur mag krijgen, en alleen rood plus waarschuwingsteken wanneer dat oudste werk voorbij de deadline van zijn eigen opdracht ligt. Groen komt alleen voor bij `Completed ✓`, in `green-deep`, met het vinkje ernaast.

**Afgerond** is streng: minstens één opdracht, elke deadline verstreken, en er wacht niets meer. Nadrukkelijk niet `to grade = 0`, want dat kan morgen omslaan en een label dat terugflipt is ruis.

**Opdracht-cards** staan op de cursuspagina, zelfde drie zones, met in de voet de echte deadline: `Due 30 Aug` met daaronder `5 days ago` of `in 9 days`.

## Zoeken, filteren, sorteren

De balk staat er altijd, vanaf één cursus. Geen drempel, want een interface die verandert zonder dat de gebruiker iets deed breekt zijn mentale model.

- **Zoeken** op cursusnaam en opdrachtnaam. Sneltoets `/`.
- **Status**: All, Needs grading, No submissions yet, Completed, Archived, met het aantal achter elke optie in het uitklapmenu. Een optie die nul oplevert blijft staan en blijft aanklikbaar.
- **Waiting**: Any, Over 3 days, Over 7 days, Over 14 days.
- **Overdue only**: schakelaar.
- Rechts staat het sorteren, apart van de filters: langst wachtend, meeste te beoordelen, laatst actief, naam.

`10 of 10 courses` staat er altijd, niet alleen bij een actief filter, met `Clear filters` ernaast zodra er iets aanstaat. Lege uitkomst is een ontworpen staat met een knop om te wissen. Filters resetten per sessie, de sorteerkeuze blijft bewaard, en de filterstand staat in de URL zodat je een gefilterd overzicht kunt doorsturen.

Gearchiveerd staat altijd onderaan in het raster. De losse archiefschakelaar is weg, dat zit nu in de statusfilter.

## Archiveren en verwijderen

Archiveren zit in het menu op de card, verschijnt op hover en op toetsenbordfocus. Op een afgeronde card staat `Archive` als zichtbare knop in de voet. Na archiveren een melding met `Undo`, geen dialoog vooraf.

Verwijderen staat niet op de card maar onderaan de cursuspagina, in rode tekst zonder vlak. De bevestiging schaalt mee: lege cursus is een gewone bevestiging, een cursus met inzendingen benoemt wat er verdwijnt in aantallen en laat je de naam overtypen.

## Wat er bewust niet is

- Geen voortgangsring, geen balk, geen urgentiemeter. De rangschikking loopt via de volgorde van het raster.
- Geen `12/32 graded`, geen `All graded` in het groen, geen `Active`-label, geen verhouding als `2 of 4 open`.
- Geen setup-status op dit scherm.
- Geen onderwijsniveau op de card en ook niet als filter. Het wordt gezet in Manage rubric.
- Geen Favorites, geen Tags, geen Creators, geen `Mine / Everyone`, geen semester- of opleidingsfilter.
- Geen badges of pills om gewone metadata, geen kaartjes in kaartjes.

## Zijbalk

Enterprise-vorm: logo van de instelling linksboven (Universiteit Leiden, als data-URI in het bestand), de in- en uitklapknop ernaast, Courses met de cursuslijst, en onderin het account met Profile en Sign Out.

Billing, Referrals, de tokenbadge en Personalised learning zijn er op 03-09-2026 uit gehaald op verzoek van Dante. Personalised learning staat nu als brede balk onderaan het hoofdscherm. De bouwprompt zegt dat billing, referrals en tokens bij Enterprise konden blijven; dat is bewust overruled.

## Wat de backend moet leveren

Per opdracht: de deadline, het aantal wachtende inzendingen, het inlevermoment van de oudste wachtende, de laatste inzending. De cursus telt die op.

`Oldest waiting` telt vanaf het inleveren door de student, niet vanaf het einde van de verwerking. Die definitie staat in een tooltip. "Deadline verstreken" beoordeel je tegen de tijdzone van de instelling, niet die van de browser.

## Openstaand

- **Bulk archiveren** aan het eind van een semester: nu niet gebouwd, wel de vraag of het nodig is.
- **Een cursus zonder opdrachten leest als `No submissions yet`.** Dat klopt, maar het wijst niet naar de volgende stap. Als daar een zetje bij moet, is dat de plek.
- **Meten na een echte nakijkperiode:** staan er dan vier of vijf van de zeven cards rood, dan werkt het signaal niet meer en klopt de drempel niet.
- De afbeelding in de Personalised learning-balk is een getekende voorbeeldweergave, geen screenshot.
- Het aanmeldformulier stuurt niets door.
- Dark mode zit er niet in.
- `--color-ring` staat in het design system op groen. Groen haalt 1,76:1 op wit, WCAG vraagt 3:1 voor een focusrand. In het prototype staat hij op navy. `--color-warning` (#b26a00) haalt 4,24:1 en zakt onder de 4,5:1, daarom staat "voorbij de deadline" in `--color-danger`.
