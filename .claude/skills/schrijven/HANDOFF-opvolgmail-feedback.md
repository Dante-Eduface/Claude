# Handoff: feedback op de opvolgmails (Shift-pipeline)

Losgetrokken van de master-chat voor de Agent 1-4 Shift-pipeline, zodat die chat overzichtelijk blijft voor pipeline-status en niet vervuilt met stem/copywriting-feedback.

## Waar dit over gaat
Dante gaf net 27 opvolgmails (na een geaccepteerd LinkedIn-connectieverzoek) terug met de vraag om feedback op de schrijfstijl één keer te geven en structureel te verwerken, niet steeds opnieuw. Deze chat is bedoeld om die feedback op te vangen.

## Wat er al staat
- `.claude/skills/schrijven/voice-by-type.md` heeft nog GEEN aparte sectie voor "opvolgmail na geaccepteerd LinkedIn-verzoek". De dichtstbijzijnde secties zijn "Cold outreach" en "LinkedIn connectieverzoek", maar een opvolgmail is een ander moment (warm, ze hebben al geaccepteerd) dus verdient een eigen sectie.
- De 27 voorbeeldmails staan in `projects/targetlijst-nl/lemlist-opvolgmails-batch1.csv` (kolom `firstEmail`), met per mail de onderbouwing waarom die hoek gekozen is (zie transcript van de master-chat als je de redenering nodig hebt, niet herhaald hier).
- Vast format voor deze mails: aanhef altijd "Hi [voornaam],", afsluiting "Met vriendelijke groet, Dante Torbed, Customer success manager, Eduface" (Engels voor buitenlandse contacten).

## Wat hier te doen is
1. Vraag Dante zijn feedback op de 27 mails (of een subset).
2. Volg de bestaande schrijven-flow: principe uit de instantie halen, loggen in `feedback-log.md` onder een nieuw of bestaand type, sectie bijwerken in `voice-by-type.md`.
3. Laat de andere types (formele mail, marketingtekst, LinkedIn connectieverzoek) met rust tenzij Dante zegt dat het overal geldt.

## Wat dit niet moet doen
- Geen pipeline-status bijwerken (`WERKVOORRAAD.md`, `berichten-nl.csv`) — dat gebeurt in de master-chat.
- Geen nieuwe mails de deur uit sturen, dit is alleen de stem-regels bijschaven.
