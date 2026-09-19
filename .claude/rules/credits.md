# Zuinig werken

Een agent ziet zijn eigen verbruik niet. Hij weet niet dat hij bij de derde zoekopdracht duurder is dan de eerste, en hij krijgt geen seintje als het budget op raakt. "Let op de credits" in een prompt zetten doet dus niets. Wat wel werkt zijn harde grenzen en de goedkope variant als standaard.

## Waar het geld zit

Niet in nadenken, maar in ophalen. Een webpagina, een PDF, een Lemlist-respons: alles wat binnenkomt telt mee, en blijft de rest van de sessie meetellen. Twee vuistregels:

- **Een pagina die je ophaalt en niet gebruikt, kost hetzelfde als een pagina die je wel gebruikt.** Denk eerst welke pagina het antwoord waarschijnlijk heeft.
- **Een lange sessie is duurder dan twee korte.** Alles wat je eerder ophaalde reist mee in elke volgende stap. Daarom werkt de pijplijn in batches en niet in een marathon.

## De vier goedkoopste gewoontes

1. **Vraag het script, niet het web.** `pipeline.py status`, `queue`, `show` en `rapport` kosten niets en weten de stand al. Een agent die zelf gaat tellen wat het script kan opzoeken, betaalt voor iets wat gratis was.
2. **Stop zodra je het antwoord hebt.** Een hard lerendenaantal gevonden? Dan hoef je de andere twee bronnen niet meer. Dit staat als paginabudget in elke skill.
3. **Peil voor je ophaalt.** Eén kleine aanroep die zegt of er iets veranderd is, is honderd keer goedkoper dan de volledige ophaal. Zo werkt `pipeline.py peiling` voor de Lemlist-sync: op een stille dag kost de meetlus vrijwel niets.
4. **Zeg dat je het niet vindt.** Drie pagina's gezocht en niets? Dan is `onbekend` het antwoord, met in het citaatveld waar je gekeken hebt. Dat is goedkoper dan een vierde poging én het voorkomt dat de volgende ronde daar opnieuw zoekt.

## Het model past bij het werk

| Werk | Model |
|---|---|
| Registers afzoeken, poort 0 scannen, mechanisch overtypen | Haiku |
| Contacten zoeken, berichten importeren, sync | Sonnet |
| Onderzoek dat een oordeel vraagt, berichten schrijven | Opus |

Agent 1 draait op Haiku, agent 3 en 4 op Opus (besluit 15-09-2026). Twijfel je, kies dan het goedkoopste model dat het werk aankan en zeg erbij waarom.

## Grenzen die echt werken

Niet: "wees zuinig". Wel:

- een **paginabudget** per record, zoals in `lead-sourcing`
- een **batchgrootte**, zodat een sessie niet volloopt
- een **tijdbudget** voor de hele ronde (`SHIFT_UREN`), zodat een nacht niet ontspoort
- een **peiling** voor elke dure operatie

Die staan in de skills en in `run-shift-nacht.sh`, niet hier. Dit bestand legt uit waarom ze er zijn, zodat niemand ze weghaalt omdat ze in de weg zitten.

## Wat een dure nacht kost

Ter kalibratie, gemeten op 16-09-2026: het ophalen van 105 Lemlist-leads met hun activiteiten kostte 271.000 tokens, terwijl de data zelf maar 22.000 tokens was. Het verschil zat in het aantal aanroepen. Dat is precies waarom er nu een peiling voor zit.
