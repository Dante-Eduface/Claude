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
