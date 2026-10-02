# Eduface privacyfeiten

_Laatst bijgewerkt: 2026-10-02. Beheerder: Jeroen van Gessel._

Elk feit heeft een status. **BEVESTIGD** = door Jeroen in de chat bevestigd, met datum. **DPA** = staat in de conceptovereenkomst maar is niet apart bevestigd. **OPEN** = niet te beantwoorden zonder Jeroen.

## Bevestigd

| Onderwerp | Feit | Status |
|---|---|---|
| Juridische entiteit | Eduface is handelsnaam van Blockbook B.V., Europalaan 93, Utrecht. Vertegenwoordigd door Jeroen van Gessel. | DPA |
| Rol | Eduface is Verwerker, de instelling is Verwerkingsverantwoordelijke (Enterprise). | DPA |
| Contact privacy en datalekken | Jeroen van Gessel, CEO / Legal, jeroen.van.gessel@eduface.me | DPA |
| Google Cloud OCR | Wordt echt gebruikt om opdrachten uit te lezen. Verwerking in de EU (europe-west4, Eemshaven/Rotterdam). | BEVESTIGD 02-10-2026 |
| Feedback | De gegenereerde feedback bevat geen persoonsgegevens. | BEVESTIGD 02-10-2026 |
| Bewaartermijn | Standaard 8 jaar, om aan lokale regelgeving te voldoen. Verwijderd op verzoek en na afloop van de samenwerking. | BEVESTIGD 02-10-2026 |
| Audits | Er is nog geen onafhankelijke audit of certificering. | BEVESTIGD 02-10-2026 |
| Scope DPA | Alleen Paper Grader en Exam Grader. Orale examens en Academic Integrity (beta) zijn er bewust buiten gelaten. | BEVESTIGD 02-10-2026 |
| Status DPA | Het SURF-document is een kennisdocument, geen sjabloon. | BEVESTIGD 02-10-2026 |
| Fallbackposities | Er zijn er nog geen vastgelegd. | BEVESTIGD 02-10-2026 |

## Verwerkers volgens de DPA (Bijlage A)

| Verwerker | Wat | Waar | Status |
|---|---|---|---|
| Microsoft Azure | Hosting van de AI-verwerking: compute, database, opslag. Ook feedback genereren. Documenten, rubrics, feedbacktekst, audit logs. | "Nederland + EU", geen doorgifte buiten de EU | DPA, exacte regio OPEN |
| Google Cloud | OCR. Geuploade documenten en afbeeldingen. | Eemshaven/Rotterdam, europe-west4 | BEVESTIGD 02-10-2026 |
| Railway | Databasehosting voor ondersteunende diensten. Interne metadata, tijdelijke verwerkingsgegevens. | Amsterdam | DPA |

Doorgiftetabel naar derde landen in de DPA: leeg.

## Wat je wel mag zeggen

- Verwerking en opslag vinden plaats in de EU.
- De docent keurt elk feedbackpunt goed voordat de student het ziet (`Platform/product.md`).
- Gegenereerde feedback bevat geen persoonsgegevens.
- Data wordt standaard 8 jaar bewaard en verwijderd op verzoek en na afloop van de samenwerking.
- Een datalek wordt binnen 48 uur na ontdekking aan de instelling gemeld (art. 7 van de DPA). Eduface meldt niet zelf aan de Autoriteit Persoonsgegevens, tenzij de instelling dat schriftelijk vraagt.
- Bijlage B beschrijft 14 beveiligingsmaatregelen, waaronder versleuteling in opslag en transport, least privilege en incident response.

## Wat je niet mag zeggen

- "ISO 27001 gecertificeerd", "SOC 2", "NOREA-verklaring" of welke certificering dan ook.
- "Alles staat in Nederland". Alleen "EU" tot de Azure-regio bevestigd is.
- "Er is geen toegang vanuit de VS" of "geen Amerikaanse partijen". Microsoft, Google en Railway hebben een Amerikaanse moeder, en daar is geen uitspraak over gedaan.
- "Studentdata gaat nooit naar externe AI-aanbieders", zolang de botsing hieronder niet is opgelost.
- Iets over orale examens of Academic Integrity en gegevensverwerking.

## Open

Dit staat ook in `Context/open-vragen.md`.

| # | Punt | Waarom het uitmaakt |
|---|---|---|
| V1 | **Welke Azure-regio('s)?** De DPA zegt "Nederland + EU" en elders "gehost in Nederland", met een gele markering dat de regio nog bevestigd moet worden. | Een instelling vraagt dit als eerste. |
| V2 | **Amerikaanse moederbedrijven.** Microsoft, Google en Railway Corp vallen onder Amerikaanse wetgeving, ook met EU-locatie. Is hier een DTIA over gedaan, en wat zeggen we? | Art. 3.1 van de DPA belooft hulp bij DTIA's. Een FG vraagt hier vrijwel zeker naar. |
| V3 | **Botsing met `Platform/product.md`.** Die zegt "Studentdata gaat nooit naar externe AI-aanbieders" en "geen training op jouw data, nooit". De DPA stuurt documenten naar Google Cloud (OCR) en zegt dat resultaten "niet zonder toestemming" voor training worden hergebruikt. Welke tekst is leidend, en is Google OCR een "externe AI-aanbieder"? | Elke instelling leest beide en ziet het verschil. |
| V4 | **Feedback zonder persoonsgegevens, maar de DPA noemt "feedbacktekst" onder gegevens die Azure verwerkt.** Klopt de bewering dat feedback geen persoonsgegevens bevat, ook als de docent een naam in de opmerking zet? | Bepaalt of feedback buiten de AVG valt of niet. |
| V5 | **Waar geldt de 8 jaar voor?** Voor de feedback, of ook voor de geuploade opdrachten met naam? De DPA zegt dat opdrachten bewaard worden "zolang de docent de opdracht actief gebruikt" en verwijderd worden zodra de docent ze verwijdert, en art. 12.3 eist verwijdering binnen een maand na afloop van de overeenkomst. | Acht jaar studentwerk met namen is voor een instelling een groot verschil met "zolang het nodig is". |
| V6 | **UK.** Wat geldt er voor UK-universiteiten (UK GDPR, eigen DPA van de instelling, doorgifte van de EU naar het VK of andersom)? `Platform/product.md` zegt "Voldoet aan de UK GDPR". Waar rust dat op? | De prioriteit is UK-universiteiten, en de kennisbron is Nederlands. |
| V7 | **Wie is plaatsvervanger?** Jeroen is enige contact voor datalekken met een melding binnen 48 uur. | Eén persoon op vakantie is een gemiste termijn. |
| V8 | **Railway.** Wat staat er precies in "interne metadata, tijdelijke verwerkingsgegevens"? Zit er studentdata of een identificeerbare gebruiker in? | Bepaalt of Railway een volwaardige subverwerker is of niet. |
