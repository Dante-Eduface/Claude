# Extractie-instructie (voor subagents)

Je leest Close-dumps in `GTM/Knowledge/pijn-oplossing/close-dump/<bestand>.md` en haalt eruit wat de prospect
zelf zei over zijn situatie. Output: één JSON-array per dossier in `GTM/Knowledge/pijn-oplossing/extractie/<zelfde-naam>.json`.

## Wat je eruit haalt (één item per uitspraak)
- **pijn**: een probleem dat de prospect zelf benoemt (werkdruk, inconsistentie, uitval, fraude, traagheid, ...).
- **uitkomst**: wat ze willen bereiken of veranderd willen zien.
- **bezwaar**: twijfel, tegenwerping of blokkade tegen Eduface of AI-beoordeling in het algemeen.
- **huidig**: hoe ze het nu doen of welke tool ze nu gebruiken (incl. concurrent).
- **oplossing_verwoord**: hoe wij (Dante/Jeroen) de oplossing in dat gesprek verwoordden, alleen als dat in de bron staat.

## Wat je NIET opneemt
- Planning, agenda, wie belt wie, follow-ups, prijsonderhandeling zonder pijninhoud.
- Dante's eigen reflectie op zijn belgedrag ("ik liet hem niet praten").
- Alles wat wij zeggen over ons product (behalve als `oplossing_verwoord`).
- Meta-regels: `[...afgekapt...]`, boilerplate.

## Velden per item
```json
{
  "id": "<bestandsnaam-zonder-md>-<volgnummer>",
  "org": "naam organisatie zoals bovenaan het dossier",
  "lead_id": "lead_...",
  "close_url": "https://app.close.com/lead/<lead_id>/",
  "persoon": "naam of null",
  "functie": "titel uit Contacten-lijst of null",
  "datum": "YYYY-MM-DD van de bron",
  "bron_type": "meeting | call | note | email",
  "bron_id": "acti_... of meet_... uit de kop (id=...)",
  "segment": "nl-ho | uk-he | particulier | intl",
  "thema": "een van de startthema's, of een nieuw thema in dezelfde stijl",
  "type": "pijn | uitkomst | bezwaar | huidig | oplossing_verwoord",
  "citaat": "zo letterlijk mogelijk uit de bron, max 60 woorden, in de taal van de bron",
  "samenvatting": "één zin NL, max 20 woorden, wat dit voor ons betekent",
  "zekerheid": "letterlijk | parafrase"
}
```
- `zekerheid`: "letterlijk" alleen als de bron een echte uitspraak bevat (user note, citaat in summary, email van de prospect). AI-samenvattingen van meetings zijn "parafrase".
- `segment`: nl-ho = NL hogeschool/universiteit/UMC; uk-he = UK/IE universiteit of college; particulier = NL particuliere opleider, business school, NRTO/CRKBO-partij, uitgever; intl = alles buiten NL/UK/IE.
- Liever 6 scherpe items dan 25 vage. Sla dossiers zonder inhoud over met een lege array `[]`.

## Startthema's (gebruik deze slugs waar ze passen)
- `nakijklast` — tijd en werkdruk van nakijken en feedback geven
- `consistentie` — verschillen tussen beoordelaars, kalibratie, kwaliteit van feedback
- `snelheid-feedback` — doorlooptijd, studenten wachten te lang
- `uitval` — studiesucces, retentie, doorstroom in lange trajecten
- `ai-gebruik-studenten` — fraude, integriteit, weten of het eigen werk is
- `docentacceptatie` — vertrouwen, angst, weerstand bij docenten tegen AI-beoordeling
- `privacy-compliance` — AVG, AI Act, security, procurement, DPIA
- `lms-it` — integratie, IT-landschap, beheer
- `budget` — geld, wie betaalt, bekostiging, prijs
- `besluitvorming` — examencommissie, traagheid, wie beslist, pilotstructuur
- `schaal` — groei studentaantallen, grote cohorten, weinig docenten
- `onderwijsvisie` — formatief toetsen, feedbackcultuur, programmatisch toetsen
- `mondeling` — verschuiving naar mondelinge toetsing
- `bestaande-tools` — Turnitin, FeedbackFruits, Cogniti, Grammarly, eigen bouw, LMS-native AI
- `rubric-kwaliteit` — rubrics ontbreken of zijn slecht, beoordelingscriteria onduidelijk
- `taal` — meertaligheid, NT2, Engels/Nederlands
