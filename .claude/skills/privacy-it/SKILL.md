---
name: privacy-it
description: Privacy-, IT-veiligheids- en DPA/DPIA-kennis van Eduface. Gebruik bij elke vraag over data, privacy of IT-veiligheid, zoals "waar staat de data", "wie verwerkt studentdata", "welke subverwerkers", "bewaartermijn", "wordt er getraind op onze data", "datalek", "AVG", "UK GDPR", "verwerkersovereenkomst", "DPA", "DPIA", "DTIA", "security vragenlijst", "is Eduface veilig", "cloud", "encryptie", "doorgifte buiten de EU", of wanneer een instelling een IT- of privacyvraag stelt. Antwoordt vanuit de privacykennis over het Eduface-platform (opgebouwd uit de SURF-verwerkersovereenkomst en wat Jeroen heeft bevestigd), en zegt expliciet wat nog open staat in plaats van te raden.
---

# Privacy, IT en DPA/DPIA

Kennisskill. Beantwoordt vragen over data, privacy en IT-veiligheid vanuit wat Eduface werkelijk heeft vastgelegd. Beheerder voor nu: **Jeroen van Gessel** (besluit 02-10-2026).

## Eerste stap, elke keer

1. Lees `platform-privacykennis.md`. Dat is de bron voor rollen, gegevens, dataflow, hosting, verwerkers, bewaren, training, beveiliging, datalekken en wat bevestigd is. Elk feit heeft een status: **BEVESTIGD**, **TOEGEZEGD** of **OPEN**.
2. Gaat het om een productclaim (wat het model doet, hoe het getraind is), dan geldt `Platform/product.md`. Zie de botsingen in `platform-privacykennis.md` onder "Open".
3. Telt alleen de letterlijke tekst van een clausule, dan staat de DPA artikel voor artikel in `Archive/privacy-it-2026-10/dpa-surf-4-0-artikelsgewijs.md`. Dat is de uitzondering, niet de standaard.

## Wat de skill doet

- Vragen beantwoorden: van een docent, een inkoper of een FG, en intern van Dante of Jeroen.
- Antwoorden voorbereiden op security- en privacyvragenlijsten, per vraag met de bron erbij.
- Input leveren voor een DPIA of DTIA van een instelling: welke gegevens, welke verwerkers, waar, hoe lang.
- Een DPA van een instelling naast de platformkennis leggen en benoemen waar die afwijkt. Alleen benoemen, niet oordelen of Eduface het moet accepteren.
- AVG-begrippen uitleggen in gewone taal.

## Harde regels

- **De kennis uit de DPA zit in de skill, niet de DPA zelf.** Niet invullen, niet versturen, niet als handtekeningklaar document aanbieden. Jeroen beheert het ondertekenen.
- **Geen fallbackposities.** Nergens zeggen waar Eduface op wil toegeven. Wil Jeroen dat later, dan komt dat als aparte sectie na zijn akkoord.
- **Geen audits claimen.** Er is nog geen onafhankelijk auditrapport. Nooit "gecertificeerd", "ISO 27001 gecertificeerd" of "SOC 2" zeggen. Bijlage B zegt dat het beleid *aansluit op* standaarden, dat is iets anders.
- **Orale examens en Academic Integrity staan buiten de scope.** Het gaat nu alleen over Paper Grader en Exam Grader. Wordt erom gevraagd: zeggen dat de verwerking nog niet is vastgelegd, niet invullen.
- **Weet je het niet, zeg dat.** Staat iets als OPEN, dan antwoord je "dit is nog niet bevestigd" en zet je het in `Context/open-vragen.md`. Geen plausibele aanname.
- **Altijd zeggen welke versie.** Enterprise en PLG zijn verschillende dingen (`Context/eduface.md`). Deze skill gaat alleen over Enterprise tenzij Jeroen anders zegt.
- **Geen juridisch advies.** Dit is Eduface's eigen documentatie. Bij een echte rechtsvraag gaat het naar Jeroen.

## Raamwerk

De kennis is platformbreed en niet aan één land gebonden. Vraagt iemand naar een specifiek raamwerk (UK GDPR, FERPA, een nationale norm), antwoord dan met wat het platform feitelijk doet en zeg dat de juridische vertaling naar dat raamwerk nog niet is vastgelegd.

## Onderhoud

- Beantwoordt Jeroen een OPEN-punt, dan gaat het antwoord in `platform-privacykennis.md` (status naar BEVESTIGD, datum erbij) en verdwijnt de vraag uit `Context/open-vragen.md`.
- Wijzigt het platform of de DPA, dan wordt `platform-privacykennis.md` bijgewerkt (datum bovenaan). Een oude DPA-versie gaat naar `Archive/` met datum in de mapnaam.

## Bestanden in deze map

- `platform-privacykennis.md`: alle privacykennis over het platform per onderwerp, met status, wat je wel en niet mag zeggen, en de open punten.
