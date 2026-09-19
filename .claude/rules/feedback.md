# Feedback verwerken

Dante geeft dagelijks feedback op het werk. Deze regel gaat over wat ik daarmee doe, want feedback die verkeerd landt is erger dan geen feedback: hij wordt een regel die overal geldt terwijl hij over één geval ging.

## De trap: correctie, patroon, regel

**1. Een losse opmerking is een correctie.** "Deze mail is te lang" betekent: maak déze mail korter. Ik pas dat ene ding aan en schrijf niets op. Verreweg het meeste blijft hier.

**2. Twee keer dezelfde opmerking is een patroon.** Dan zeg ik dat hardop: *"dit is de tweede keer dat je hierop wijst, zal ik er een regel van maken?"* Ik maak hem nog niet.

**3. Pas na akkoord wordt het een regel.** En dan leg ik eerst de tekst voor, letterlijk zoals hij in de skill of de rule komt te staan. Dante kan dan zien wat er precies vastligt, want een regel die ik zelf samenvat is bijna nooit wat hij bedoelde.

Zegt Dante zelf "altijd" of "nooit" of "vanaf nu", dan slaat het patroon over en gaan we direct naar stap 3.

## Wat ik nooit doe

- **Een aanname invullen die ik kan navragen.** Snap ik niet waar de feedback over gaat, dan vraag ik het in één regel. Een verkeerd geraden regel kost weken voor iemand het merkt.
- **Een regel breder maken dan de feedback was.** Feedback op een cold-callscript is geen regel voor alle outreach. Feedback op een mail aan een particuliere opleider is geen regel voor universiteiten. De scope van de regel is de scope van het voorbeeld, tenzij Dante hem zelf breder trekt.
- **Stilletjes een skill wijzigen.** Elke wijziging in een skill of rule wordt genoemd in mijn antwoord, met wat er verandert en waarom.
- **Oude feedback laten staan die de nieuwe tegenspreekt.** Nieuwe feedback wint, en de oude regel gaat weg in plaats van ernaast te blijven staan. Twee regels die elkaar tegenspreken zijn erger dan geen regel.

## Waar het landt

| Soort | Plek |
|---|---|
| Correctie op één bericht of lead | het record zelf, via `pipeline.py` |
| Feedback op wat een SHIFT-agent oplevert | het leerpuntenbestand van die agent, zie hieronder |
| Een vastgelegde regel over stijl | `.claude/skills/schrijven/feedback-log.md`, gescheiden per content-type |
| Een besluit met gevolgen | `Decisions/log.md`, met de redenering erbij |
| Iets dat elke sessie moet gelden | de memory-map, één bestand per feit |

## De leerpuntenbestanden

Elke SHIFT-agent heeft er een, en leest hem voordat hij begint:

| Agent | Bestand |
|---|---|
| 1 lead-sourcing | `.claude/skills/lead-sourcing/LEERPUNTEN.md` |
| 2 contact-sourcing | `.claude/skills/contact-sourcing/LEERPUNTEN.md` |
| 3 shift-research | `.claude/agents/LEERPUNTEN-shift-research.md` |
| 4 outreach | `.claude/skills/outreach/LEERPUNTEN.md` |

**Het meeste van die feedback komt in de chat, niet in de cockpit.** Zegt Dante "die organisatie is publiek bekostigd" of "dit haakje gaat over de student", dan is dat feedback op agent 1 of 3 en hoort het daar. Ik schrijf hem daar zelf naartoe, in het format van dat bestand, en meld in mijn antwoord in één regel dat ik dat gedaan heb. Wachten tot Dante zegt "schrijf dat op" betekent dat het nooit gebeurt.

Wat er níet in gaat: een correctie op één record die nergens een patroon van is ("deze naam is verkeerd gespeld"). Dat gaat naar het record en verder nergens heen.

In elk leerpuntenbestand staat een tabel met de stappen van die agent. Feedback die een stap aanwijst is te verwerken; feedback op het eindresultaat niet. Wijst Dante geen stap aan en is het niet duidelijk welke het was, dan vraag ik het in één regel in plaats van te gokken.

## De dagelijkse ronde

De cockpit-pagina verzamelt feedback per bericht en per agent. Ik lees die 's ochtends terug en behandel hem volgens de trap hierboven: losse punten verwerk ik in de betreffende records, herhaalde punten leg ik als voorstel voor.

Wat ik daarbij altijd meld: **hoeveel feedback er lag, wat ik ermee gedaan heb, en wat ik heb laten liggen omdat ik het niet zeker wist.** Dat laatste is het belangrijkste onderdeel. Feedback waar ik niks mee kon moet zichtbaar blijven, niet verdwijnen in een stapel verwerkte punten.
