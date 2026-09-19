# Het dossier

Het master-document bewaart de **stand**, het dossier bewaart de **inhoud**. Eén bestand per persoon (`<person_id>.md`) en per organisatie (`orgs/<org_id>.md`). Op id, niet op naam, want namen veranderen en id's niet.

Je schrijft er nooit met de hand in, net als bij de CSV's:

```bash
pipeline.py dossier <id> --sjabloon > /tmp/d.md          lege kopstructuur
pipeline.py dossier <id> --schrijf /tmp/d.md --actor shift-research
pipeline.py dossier <id>                                 lezen
pipeline.py dossier <id> --sectie Citaten                alleen die kop, scheelt tokens
pipeline.py dossier <id> --sectie Berichten --schrijf -  alleen die kop bijwerken
```

## Waarom dit bestaat

Het onderzoek van agent 3 moest passen in vier CSV-velden, samen zo'n 1.050 tekens per persoon. Een cold-call-dossier voor dezelfde soort prospect is 11 tot 18 KB. Wat verdween: de bronnenlijst, de woordenlijst, elk citaat buiten de top-3, en de reden waarom iets opviel. Agent 4 kreeg de samenvatting en moest de bron dan zelf opnieuw ophalen.

Daarbovenop een praktisch probleem: één `opvallend` van 3.000 tekens maakte `queue --table` onleesbaar. Het veld dat het onderzoek moest dragen was precies het veld dat de wachtrij sloopte.

## De regels

- **Maximaal 250 regels.** Een dossier dat alles bewaart is net zo onbruikbaar als een dossier dat niets bewaart. Het script weigert erboven.
- **Alleen de vaste koppen.** Een verzonnen kop wordt geweigerd, zodat elke agent weet waar hij moet kijken.
- **Geen conclusie, geen uitgeschreven haakje-zin.** Lever materiaal. Op een conclusie kan agent 4 niet meer reageren, en dan komt er een correct en volstrekt vergeetbaar bericht uit.
- **`opvallend`, `haakje`, `toetsprogramma` en `schrijfwerk` blijven bestaan in het master-document**, maar zijn vanaf nu een samenvatting van hooguit 200 tekens voor de wachtrij. De lading zit hier.

## Elk citaat draagt zijn drager

Dit is de belangrijkste regel in het bestand, en de reden dat `doctor` erop valt.

```
> "letterlijk citaat, precies zoals het er staat"
  bron: <url of document, pagina> · datum: JJJJ-MM-DD · drager: student|beoordelaar|organisatie|panel
```

De **drager** is wie in die bron de last draagt. Eduface neemt werk weg bij de **beoordelaar**. Een last die de bron bij de student legt is dus geen haakje voor ons, hoe mooi het citaat ook klinkt.

Vaktermen hebben een vaste drager en mag je niet als gewone taal lezen. De tabel per markt staat in `GTM/Campaigns/shift/markets/<code>/profiel.md` onder de kop **Vaktermen** (NL uitgebreid in `Platform/Product/onderwijs-vaktermen.md`). NL: `studeerbaarheid`, `studielast` en `toetslast` gaan over de student, `nakijklast`, `tweede beoordelaar` en `kalibratie` over de beoordelaar. VK: `student workload` en `feedback literacy` over de student, `marking load`, `turnaround` en `moderation` over de beoordelaar; `assessment load` is ambigu.

> **Waarom dit een regel is.** Op 13-08-2026 wees THIM een mail af die het NVAO-citaat over studeerbaarheid gebruikte om iets over de nakijklast van docenten te zeggen. Thim van der Laan: *"Dit is de studeerbaarheid voor de student. De oplossing die jij aanbiedt probeert meer de organisatie in efficientie e.d. te ondersteunen. Dat zijn twee verschillende dingen."* Alle woorden stonden in de bron en alle getallen klopten. Het goede haakje lag er ook: twee onafhankelijke beoordelaars op de scriptie. Agent 4 kon dat verschil alleen niet zien, want hij kreeg één samengevatte cel in plaats van beide citaten met hun drager.

Weet je de drager niet, dan zet je dat in `## Onzekerheden`: *"de bron noemt nergens wie beoordeelt"*. Dat is bruikbare informatie, want dan stelt agent 4 de vraag in plaats van de aanname te doen.

## De koppen

**Persoon**

| Kop | Wie vult hem | Wat erin hoort |
|---|---|---|
| Waarom deze persoon | agent 2 | de route door het organogram, met bron |
| Bronnen | agent 3 | gelezen en niet gelezen, met reden. Primair boven secundair |
| Citaten | agent 3 | letterlijk, met vindplaats en drager |
| Toetsprogramma | agent 3 | wat leveren lerenden in, hoeveel, wie kijkt na, met citaat |
| Getallen | agent 3 | losse cijfers die opvielen, elk met bron |
| Rare details | agent 3 | wat niet bij elkaar past |
| Persoon | agent 3 | rol, datums, opleiding, woonplaats, hoe hij praat |
| Onzekerheden | agent 3 | wat niet hard is, en waar Dante naar moet kijken |
| Berichten | agent 4 | wat er geschreven is, met de redenering erbij |

**Organisatie:** Status · Bekostiging · Aanbod · Beoordeling · De pijn · Onderwijsvisie · Organogram · LMS · Rechtsvorm · Studentenaantal

## Gemigreerde dossiers

Dossiers met de regel `<!-- gemigreerd uit het master-document op 2026-08-14 -->` zijn mechanisch overgezet uit de oude CSV-velden. De tekst is niet herschreven, dus **de dragers staan er nog niet bij**. Lees daar geen last van de beoordelaar in die er niet staat. Kom je er een tegen die je gaat gebruiken, ken dan alsnog de dragers toe.
