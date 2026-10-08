# Leerpunten agent 4

Append-only. Elke afkeuring of opmerking op een bericht komt hier terecht, ook als er nog geen regel uit volgt. Agent 4 leest dit bestand voordat hij schrijft.

Format: `[JJJJ-MM-DD] persoon of batch: wat er mis was | waar in de keten het misging | wat ermee gedaan is`

## Waarom dit bestand bestaat

Feedback op een bericht verdwijnt normaal in dat ene bericht. De volgende ronde maakt dezelfde fout, en dan geef je dezelfde feedback nog een keer. Dit bestand is het geheugen tussen de rondes in.

Niet elke opmerking wordt een regel in de skill. Losse punten blijven hier staan tot ze zich herhalen; pas dan gaan ze naar `SKILL.md`, en dan met de tekst vooraf voorgelegd. Zie `.claude/rules/feedback.md`.

## Feedback die werkt

Een bericht is het einde van een keten van vijf beslissingen. "Deze mail is niet goed" zegt niet welke schakel het was, dus daar kan agent 4 niets mee. Wijs de schakel aan:

| Schakel | Wat er dan mis is | Voorbeeld van bruikbare feedback |
|---|---|---|
| **De bron** | het citaat klopt niet, of is er niet | "dit staat niet in dat rapport, hij zegt iets anders" |
| **De drager** | de last ligt bij de student, niet bij de beoordelaar | "studeerbaarheid gaat over de student, dit is niet onze pijn" |
| **Het haakje** | de observatie klopt maar raakt ons niet | "dat ze een nieuw gebouw hebben zegt niks over nakijken" |
| **De opening** | het haakje is goed maar de eerste zin landt niet | "dit leest als een compliment, niet als een observatie" |
| **De vraag** | de opening is goed maar de vraag is dicht of loos | "hier kan hij ja of nee op zeggen en dan is het gesprek dood" |
| **De toon** | alles klopt maar het klinkt niet als Dante | "dit is te formeel, hij zou dit nooit zo zeggen" |

De review loopt in de chat (sinds 16-09-2026, geen cockpit-artifact meer). Daar toon ik bij elk bericht `waarom_dit_bericht` en `afgevallen_openers`: welke keuze agent 4 maakte en wat hij verwierp. Feedback op díe redenering is het meest waard: dan weet hij niet alleen dát het fout was, maar waar zijn afweging scheefging.

Een afkeuring zonder reden is beter dan niets, maar levert alleen een teller op.

## Log

- [2026-08-13] THIM van der Laan: mail gebruikte een NVAO-citaat over studeerbaarheid om iets over de nakijklast van docenten te zeggen. | Drager: de bron legt de last bij de student, wij bij de beoordelaar. Alle woorden klopten, alle getallen klopten. | Dragertoets verplicht gemaakt, met de vaktermentabel per markt. Staat als waarschuwing in SKILL.md.
- [2026-07-23] onbekende batch: bericht beweerde dat iemand reflectief vermogen opbouwt "door te schrijven en herschrijven met feedback", terwijl het woord feedback in zijn hele stuk niet voorkwam. | Het haakje: een begrip ingevuld dat de bron niet noemt, omdat het naar Eduface leidt. | Regel "geen enkel woord dat niet uit de bron komt" in SKILL.md.
- [2026-10-06] AACSB-proef (8 berichten, ALT-webinar): alle stukken noemden "with Jisc and ALT", terwijl niet zeker is dat die partners meedoen. Daarbij miste de vaste titel. | De opening: een feit over het event dat niet klopte, overgenomen uit het campagnesjabloon. | Sjabloon en eventbeschrijving in SKILL.md aangepast (partners eruit, titel "The Business Outcomes of AI Marking and Feedback" erin), berichten.md als verouderd gemarkeerd. Dante vroeg daarnaast om een volledige flow voor één persoon met haakje en één zonder; de fallback zonder haakje moet even sterk zijn.
- [2026-10-06] Flow-voorbeeld Finn en Daly: stap 2b zei hetzelfde als het verzoek ("which is why you came to mind"), alleen anders verwoord. Daarnaast hoeft 2a niet om een e-mailadres te vragen: de uitnodiging kan via LinkedIn. | De opening van het vervolg: een herhaling in nieuwe woorden is geen nieuw element. | Correctie, nog geen regel. Elke stap moet een echt nieuwe observatie dragen, dus agent 3 moet per persoon meerdere losse vondsten leveren. 2a krijgt een paar varianten met de link direct in LinkedIn.
- [2026-10-08] AACSB-campagne: in de eerste 20 mails stond "Best, Dante Torbed, Eduface" terwijl Lemlist een handtekening toevoegt (dubbele afsluiting), en "I'm Dante from Eduface" klopt niet meer nu Lemlist leads ook aan Jeroen toewijst. | De opening en de afsluiting: afzender-specifieke tekst in een variabele die door meerdere afzenders wordt verstuurd. | Opgelost in de 16 mails in Lemlist (afsluiting verwijderd). Regel in SKILL.md (campagnekop) en SCHRIJFOPDRACHT.md: geen afsluiting en geen afzendernaam.
