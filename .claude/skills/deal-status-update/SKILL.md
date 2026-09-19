---
name: deal-status-update
description: Schrijft een korte status-update per deal/account uit Close CRM en zet die in het note-veld van de opportunity. Graaft diep (emails, notes, taken EN meeting-summaries + user notes via de REST API, die de MCP-tool weglaat) maar schrijft maximaal 8 regels: huidige stand, next steps, wat het geld raakt, en de gaten. Geen dagboek van mailtjes. Trigger wanneer Dante zegt "schrijf een status update voor [account]", "update de opportunities", "hoe staat [deal] ervoor in Close", "zet de stand in Close", of een lijst accounts noemt om bij te werken.
---

# Deal status update

Je schrijft een status-update die onder een Close opportunity komt. Doel: Jeroen of Dante opent de kaart en ziet binnen twee regels of de deal in de problemen zit en wat er moet gebeuren.

## Stap 1: haal de volledige waarheid op

Per account MOET je alle vier de bronnen raadplegen. Sla er nooit een over.

1. **Lead + contacten** — `mcp__claude_ai_Close__fetch_lead`
2. **Opportunity** — `mcp__claude_ai_Close__find_opportunities` met `lead_id` (fase, waarde, confidence, huidige note)
3. **Activiteiten** — `mcp__claude_ai_Close__activity_search` met `lead_ids` (emails, notes, statuswijzigingen, taken)
4. **Meeting-summaries en user notes** — `scripts/close_meetings.py` (zie hieronder)

### Kritiek: de MCP-tool laat meeting-inhoud weg

`activity_search` geeft bij een meeting alleen het `note`-veld, en dat is de **agenda uit de agenda-uitnodiging** (Teams-link, disclaimer, bla). De echte inhoud zit in twee andere velden die de MCP-tool niet teruggeeft:

- `summary.text` — de AI notetaker-samenvatting (in de Close UI: `app.close.com/notetaker-summary/<id>`)
- `user_note` — wat Jeroen of Dante zelf na afloop heeft getypt. Vaak het waardevolste van de hele deal: budgethouders, deadlines, wie tekent, wat er echt speelt.

Draai daarom altijd:

```bash
python3 .claude/skills/deal-status-update/scripts/close_meetings.py <lead_id> [<lead_id> ...]
```

Dat script gebruikt `CLOSE_API_KEY` uit `.claude/settings.local.json` en print per meeting de titel, deelnemers, `summary.text` en `user_note`.

**Schrijf nooit "uitkomst niet vastgelegd" voordat je dit script hebt gedraaid.** Die conclusie is bijna altijd fout als je hem op de MCP-output baseert.

## Stap 2: schrijf kort

Leidend principe (Dante, 20 jul 2026):

> "Ik instrueer mijn team om CRM-updates high-level te houden en alleen op wat noodzakelijk is. Sales stage, deal value, close date, confidence, current status en next steps zijn table stakes. Daarbuiten hoef ik geen regel dat je Bob hebt gemaild en dat hij volgende week terugkomt. Ik weiger het CRM als kindermeisje te gebruiken."

Je onderzoekt dus veel en schrijft weinig. De note is **maximaal 8 regels**. Alles wat je opzoekt maar niet opschrijft is geen verspilling, dat is de filter.

De kaart toont al fase, bedrag, confidence en contactpersoon. **Herhaal die nooit.**

```
**Status:** <de huidige stand in één regel. De conclusie, niet het proces.>

**Wat er gebeurde:** <de uitkomst in 2 tot 4 zinnen. Alleen wat het geld raakt: budget, wie tekent, wat de klant als succes ziet, harde datums.>

**Next action:** <actie> | <naam> | <datum> | <prioriteit>

**Next action:** <tweede actie, als die er is>

**Risk:** <de blocker>

**Action required:** <wat er nodig is, en van wie>
```

### Lege regels zijn verplicht
Twee opeenvolgende `**Next action:**` regels zonder witregel worden één onleesbare brij. **Tussen elk blok hoort een lege regel**, ook tussen twee next actions onderling en tussen Risk en Action required. Elk vetgedrukt label begint een nieuw blok met een witregel ervoor.

### Markdown werkt niet in Close
Het `note`-veld van een opportunity is platte tekst. Schrijf je daar `**Status:**` naartoe, dan staan de sterretjes er letterlijk in. Vet werkt alleen via het rich-text veld `note_html`, dat moet beginnen met `<body>` en eindigen met `</body>`; Close vult het platte `note`-veld daarna zelf.

`close_write_note.py` doet die conversie al: schrijf gewoon markdown in het bronbestand, het script maakt er `<p>` en `<b>` van. Schrijf nooit rechtstreeks naar `note` via de MCP-tool of de API, dan verlies je de opmaak.

(Handmatig in de Close-editor plakken werkt wel met markdown, die editor converteert tijdens het plakken. Dat verklaart waarom het soms wel en soms niet lijkt te werken.)

Het "wat er gebeurde"-blok is een uitkomst, geen logboek. Niet "gemaild op 12 juni, gebeld op 18 juni, meeting op 7 juli". Wel "Eric heeft eigen budget en wil zelf leiden, tekent mee met de IT manager".

Elke note eindigt met een next action met datum, anders stalt de deal. Staat er geen vervolgstap, dan is dat zelf het risico.

### Datums verzin je nooit
Een datum in een next action komt uit een bron: een open taak in Close, een agenda-item, een deadline die in een mail of meeting-note is afgesproken. Vind je er geen, zet dan `<datum onbekend>` en vraag het aan Dante. Een plausibel ogende datum die je zelf hebt bedacht komt in het CRM terecht en gaat een eigen leven leiden.

Zoek in deze volgorde: taken op de lead (`/api/v1/task/?lead_id=`), close date op de opportunity, deadlines genoemd in meeting user notes, dan Todoist en Google Calendar.

### Wel opnemen
Alles wat de uitkomst van de deal bepaalt: budgethouder en of die eigen budget heeft, wie tekent, harde go-datums, wat de klant als succes ziet, een LMS-migratie die alles op hold zet, een bedrag dat niet klopt met wat er is voorgesteld.

### Niet opnemen
- Chronologie van mailtjes en wie wanneer heeft gereageerd. Dat is het dagboek dat het CRM onbruikbaar maakt.
- Overdue taken. Dante ziet zijn eigen taken wel.
- Dat een webinar is uitgesteld, tenzij het de deal raakte.
- Alles wat je zou schrijven om te laten zien dat je hebt gewerkt.

### De eerste regel
Geen "Fase: Pilot". Wel: "Go-deadline 15 aug, IT manager als mede-ondertekenaar nog niet in kaart" of "On hold tot NWU hun LMS-migratie heeft afgerond". Inverted pyramid: wie scant moet in regel 1 zien of dit wankelt.

## Stap 3: zet het in Close

Het note-veld van de opportunity (niet een losse lead-note):

```bash
python3 .claude/skills/deal-status-update/scripts/close_write_note.py <opportunity_id> <bestand-met-de-tekst>
```

Dit **overschrijft** de bestaande note. Dat is de bedoeling, de note is een levend statusveld en geen logboek. Bij twijfel of er andermans tekst in staat: eerst tonen aan Dante.

## Toon en regels

- Nederlands, kort, feitelijk. Geen em-dashes. Geen opsmuk.
- **Niets verzinnen.** Alleen wat aantoonbaar in Close staat. Geen aannames over waarom een status is veranderd.
- Als een statuswijziging geen toelichting heeft, is dat zelf een gat. Benoem het.
- Bedragen die niet kloppen met wat er is voorgesteld: benoemen (zoals een opportunity van €40k terwijl het voorstel €4.000 was).
- Duplicaat-leads: benoemen, en zeggen welke de echte is.
- Dante's scope loopt tot de Discovery gate. Bij deals die verder zijn is de eigenaar Jeroen, schrijf de actie dan ook op zijn naam.

## Wat Dante hier eerder over zei

- "Fase, bedrag, confidence en contact staan al op de kaart, die hoef je er niet boven te zetten." (20 jul 2026)
- "Dat drie taken overdue zijn hoef je niet te benoemen, dat is niet belangrijk." (20 jul 2026)
- "Weet waar je meeting-informatie kan vinden." Na twee keer ten onrechte "geen uitkomst vastgelegd" terwijl de notetaker-summary er gewoon was. (20 jul 2026)
- Geen dagboek. Zie het citaat bij stap 2. Diep onderzoeken, kort opschrijven.
- Conclusie bovenaan. Inverted pyramid.
