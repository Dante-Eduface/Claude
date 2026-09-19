---
name: deep-research
description: Diep onderzoek naar een open vraag (markt, concurrent, beleid, trend, technologie, "hoe zit X in elkaar"), via parallelle subagents die elk een deelvraag uitzoeken en een synthese met bronnen. Dit is de Claude Code-versie van de Research-modus in de Claude-app. Trigger wanneer Dante zegt "doe diep onderzoek naar", "research dit", "zoek dit helemaal uit", "deep research", "wat weten we over [onderwerp]", "hoe zit [markt/beleid/concurrent] in elkaar", of een vraag stelt die duidelijk meerdere zoekrondes nodig heeft. Vier standen van goedkoop naar duur (verkenning / snel / standaard / diep); Dante kan die zelf noemen ("doe dit even snel", "ga hier echt diep op in", "/deep-research diep <vraag>"), anders kiest de skill zelf en zegt welke. NIET voor één persoon (dat is person-research) of een lijst personen (dat is de shift-research subagent).
---

# Deep Research

Een open vraag uitzoeken zoals de Research-modus in de Claude-app dat doet: opdelen in deelvragen, parallelle subagents die elk hun eigen zoekloop draaien, en één synthese met bronnen. De winst zit niet in een betere zoekmachine, maar in de orkestratie: fan-out, iteratief bijstellen, en een synthesepass die tegenspraak en gaten expliciet maakt.

## Eerst: is deze skill wel de juiste?

| Vraag gaat over | Gebruik |
|---|---|
| Eén persoon | `person-research` |
| Meerdere personen uit de NL-pijplijn | subagent `shift-research` |
| Wie is wie bij één instelling | `stakeholder-mapping` |
| Een deal, of sales-advies | `cro` |
| Alles wat je in één of twee searches beantwoordt | gewoon zelf `WebSearch`, geen skill |
| **Een open vraag met meerdere onafhankelijke deelvragen** | **deze skill** |

Laatste regel is de test: kun je de vraag opdelen in 3+ stukken die je parallel kunt uitzoeken zonder dat het ene het andere nodig heeft? Zo niet, dan is dit overkill. Zeg dat en doe het gewoon zelf.

## Diepte kiezen (dit bepaalt de kosten)

Vier standen. Dante kan er zelf een noemen (`/deep-research snel <vraag>`, of gewoon "doe dit even snel" / "ga hier echt diep op in"). Zegt hij niks, kies je zelf met de beslisregel hieronder.

| Stand | Subagents | Model | Rondes | Ruwe kosten | Wanneer |
|---|---|---|---|---|---|
| **Verkenning** | 0 | zelf | 2 tot 4 searches | ~10k | Je wilt alleen weten of de vraag de moeite waard is |
| **Snel** | 3 | `sonnet` | 1 | ~100k tot 200k | Oriëntatie, "wat speelt hier ongeveer" |
| **Standaard** | 5 | `sonnet`, tegenspraak op `opus` | 1 + gatenronde | ~300k tot 500k | Default. Iets waar een beslissing op volgt |
| **Diep** | 8 | `opus` | 2 + gatenronde | ~800k tot 1.5M | Markt betreden, concurrent doorgronden, strategie |

De kostenkolom is een grove schatting, geen belofte. Wat een subagent echt verbruikt hangt op het aantal pagina's dat hij opent, en een PDF van 80 pagina's is in zijn eentje al tienduizenden tokens.

### De beslisregel

Kies **niet** op hoe belangrijk het onderwerp voelt, maar op deze twee vragen:

1. **Hangt er een beslissing aan?** Nee → snel. Ja → minimaal standaard.
2. **Is het antwoord verspreid over veel bronnen, of staat het in één document?** Eén document → snel, ook als het onderwerp groot is. Verspreid → diep.

Een groot onderwerp met een centraal document (bijvoorbeeld: "wat staat er in het nieuwe Jisc-framework") is een snelle vraag. Een klein onderwerp waar niemand het hele plaatje heeft opgeschreven (bijvoorbeeld: "welke UK-universiteiten kochten sinds 2024 AI-nakijktools, en via welk kanaal") is diep werk.

### Altijd eerst verkennen bij twijfel

Twijfel je tussen twee standen, draai dan de verkenning: 2 tot 4 searches die je zelf doet, zonder subagents. Kost bijna niks en beantwoordt de enige vraag die telt, namelijk of het antwoord al ergens compleet opgeschreven staat. Staat het er, dan ben je klaar voor 10k in plaats van 500k. Staat het er niet, dan weet je nu welke deelvragen echt open zijn en wordt de fan-out veel scherper.

Dit is de belangrijkste besparing in deze skill. Sla hem niet over omdat de vraag groot lijkt.

### Onderweg afschalen of opschalen

De stand ligt niet vast als je eenmaal loopt.

- Komen drie subagents terug met hetzelfde antwoord en geen tegenspraak, **sla de gatenronde over**. Klaar is klaar.
- Komt de fan-out grotendeels leeg terug, **schaal niet automatisch op**. Vaak is "hier is publiek weinig over te vinden" het echte antwoord. Leg dat aan Dante voor voordat je een tweede ronde start.
- Blijkt de vraag halverwege veel groter dan gedacht, meld dat in één regel en vraag of hij door wil (`/deep-research diep`), in plaats van er stilletijgend 1M tokens tegenaan te gooien.

### Kosten drukken zonder kwaliteit te verliezen

- **Model per subagent.** Feiten verzamelen kan op `sonnet`. Zet `opus` alleen op de deelvragen die oordeel vragen: de tegenspraak, en de vertaling naar Eduface. Dat scheelt makkelijk de helft.
- **Subagents leveren compact terug.** Het formaat in `subagent-prompt.md` is expres kaal: bullets met links, geen procesverslag. Een subagent die zijn hele zoektocht navertelt kost je twee keer zoveel context voor hetzelfde antwoord.
- **Nooit twee subagents op overlappende deelvragen.** Overlap is de grootste verspilling: je betaalt twee keer voor dezelfde pagina's. Splits scherp (zie stap 4).
- **Verkenning eerst.** Zie hierboven.

## De loop

## De loop

```
1. HERFORMULEER  wat is de echte vraag, en waarvoor gebruikt Dante het antwoord
2. INTERN EERST  Close, Gmail, Drive, en de repo (GTM/, Platform/, Design/, Decisions/log.md)
3. VERKEN        2 tot 4 eigen searches, staat het antwoord al ergens compleet? zo ja: stop hier
4. SPLITS        3 tot 8 deelvragen die elkaar niet overlappen
5. FAN-OUT       alle subagents in EEN bericht, parallel, model per deelvraag
6. SYNTHESE      conclusie eerst, dan tegenspraak, dan gaten
7. GATENRONDE    1 tot 3 subagents op wat er nog ontbreekt of botst, overslaan mag
8. LEVER         antwoord + bronnenlijst + wat je niet weet
```

### Stap 2: intern eerst

Voor je het web opgaat, kijk wat er al is. Dit wordt structureel overgeslagen en dat kost dubbel werk. Check:
- `GTM/`, `Platform/` en `Design/` in deze repo, en `Decisions/log.md`
- Close op de betrokken accounts
- Gmail en Drive op het onderwerp

Vind je een eerder onderzoek naar hetzelfde, zeg dat en bouw erop verder in plaats van opnieuw te beginnen.

### Stap 4: splitsen

Goede deelvragen zijn **onafhankelijk** en **beantwoordbaar**. Elke deelvraag moet iets zijn waar een los persoon een middag aan kan werken zonder de anderen te hoeven vragen.

Slecht gesplitst (overlap, en te vaag):
- "Wat doen concurrenten" / "Wie zijn de spelers" / "Hoe ziet de markt eruit"

Goed gesplitst:
- "Welke AI-feedbacktools zijn sinds 2024 aanbesteed door UK-universiteiten, en via welk kanaal (Jisc, direct, framework)?"
- "Wat schrijven de vier grootste UK-universiteitsverenigingen in hun publieke AI-beleid over summatief beoordelen?"
- "Welke prijsmodellen hanteren Turnitin, FeedbackFruits en Graide publiek?"

Standaard-assen om langs te splitsen, pak wat past: spelers, geld, beleid/regelgeving, techniek, tijdlijn, tegenargument.

**Eén deelvraag is altijd de tegenspraak.** Zet minstens één subagent expliciet op "zoek wat deze aanname onderuit haalt". Zonder die is een research-oplevering een echokamer.

### Stap 5: fan-out

Alle `Agent`-calls in **één bericht**, anders lopen ze niet parallel. Gebruik `subagent_type: "general-purpose"` tenzij een specifieke agent past, en zet `model` per agent volgens de tabel bij Diepte: feitenverzameling op `sonnet`, oordeelswerk (tegenspraak, vertaling naar Eduface) op `opus`. De prompt per subagent staat in `subagent-prompt.md` in deze map. Vat die niet samen, gebruik hem letterlijk met de deelvraag erin.

Subagents leveren **bevindingen met links terug, geen samenvatting van hun proces**. Hun rapport zie je zelf wel, Dante niet, dus jij bent degene die het naar buiten vertaalt.

### Stap 6: synthese

Dit is het werk, niet het plakken van vijf rapporten onder elkaar. In deze volgorde:

1. **Het antwoord**, in maximaal 5 bullets. De vraag beantwoord, niet "hier is wat ik vond".
2. **Waar bronnen elkaar tegenspreken.** Noem beide, met bron en datum, en zeg welke je zwaarder weegt en waarom. Nooit stilletjes de mooiste kiezen.
3. **Wat dit betekent voor Eduface.** Eén alinea, concreet. Weet je dat niet, sla over in plaats van het te vullen.
4. **Gaten.** Wat je niet hard kreeg.

### Stap 7: gatenronde

Sla deze over als de fan-out eensgezind terugkwam zonder tegenspraak, dat scheelt een dure ronde voor niks. In alle andere gevallen bij standaard en diep wel draaien. Zet 1 tot 3 subagents op precies de tegenspraak en de gaten uit stap 6. Levert dat niks op, dan is "dit is niet publiek vindbaar" het eindantwoord en dat schrijf je gewoon op.

## De regels (overgenomen uit person-research, gelden onverkort)

1. **Geen aannames.** Elke claim is een feit met bron, of expliciet gelabeld als inferentie.
2. **Bron echt openen.** Nooit een rapport of pagina citeren op basis van de titel of het zoekresultaat-snippet. Openen en lezen. Lukt dat niet, probeer curl met browser-User-Agent, cache, of een andere route. Daarna is "niet online te vinden" het eerlijke antwoord (`not-findable-say-so`).
3. **Datum bij elke bron.** Een marktcijfer uit 2021 is geen marktcijfer van nu. Noem het jaar altijd (`claims-need-sources`).
4. **Denk na over het waarom.** Wie publiceerde dit, met welk belang? Een vendor-whitepaper over marktgroei is marketing, geen onderzoek. Label dat.
5. **Onzekerheid flaggen, niet dichtpapieren.** Kan iets meerdere kanten op, leg het aan Dante voor: "lees dit: [bron]. Wat zie jij hier?"

## Wat je oplevert

- **Antwoord** op de vraag, conclusie eerst, max 5 bullets
- **Tegenspraak** tussen bronnen, met jouw weging
- **Betekenis voor Eduface**, één alinea, alleen als je het echt kunt zeggen
- **Bronnenlijst** met links en jaartallen, gesplitst primair (originele documenten, cijfers van de bron zelf) / secundair (journalistiek, analyses) / tertiair (blogs, vendorcontent)
- **Gaten**: wat je niet hard kreeg, en wat er nodig is om het wel hard te krijgen

Schrijf het weg naar `<map van het project>/research/<onderwerp>.md` als het bij een lopend project hoort, anders `Platform/Onderzoek/<onderwerp>.md`. Een oplevering die alleen in de chat staat, bestaat na afloop niet meer.

Artifact alleen als Dante er expliciet om vraagt (`deliver-as-artifact`).

## Done

- Diepte genoemd, met de reden, voor je begon
- Intern gecheckt (repo, Close, Gmail, Drive) voor de eerste websearch
- Verkenning gedraaid bij twijfel over de diepte, en gestopt als het antwoord er al stond
- Alle subagents in één bericht gestart, dus echt parallel
- Minstens één subagent stond op de tegenspraak
- Gatenronde gedraaid, of expliciet overgeslagen omdat er geen tegenspraak was
- Bij een veel grotere vraag dan gedacht: gemeld en gevraagd, niet stilletjes opgeschaald
- Elke claim heeft bron + jaartal, of een inferentie-label
- Bronnen zelf geopend, niet op snippet geciteerd
- Bronnenlijst gesplitst primair/secundair/tertiair
- Weggeschreven naar een bestand, niet alleen de chat
