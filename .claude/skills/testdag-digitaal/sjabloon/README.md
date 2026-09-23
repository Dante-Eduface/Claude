# Het sjabloon

Drie bestanden en een map met fonts. Samen maken ze een los HTML-bestand dat offline opent.

| Bestand | Wat het is |
|---|---|
| `sjabloon.html` | de opmaak en de opbouw. Hier kom je alleen als het ontwerp verandert |
| `bouw.py` | plakt de fonts en de inhoud in het sjabloon en schrijft er een los bestand van |
| `voorbeeld-cat-diagnostiek.json` | een gevuld voorbeeld, het echte materiaal van CAT diagnostiek |
| `fonts/` | Inter en League Spartan, als woff2, samen 72 KB |

## Bouwen

```bash
python3 bouw.py <vak>.json <uitvoer>.html
```

Het resultaat is ongeveer 130 KB en heeft niets nodig: geen internet, geen server, geen tweede bestand.

## De velden

Op het hoogste niveau:

| Veld | Verplicht | Wat erin staat |
|---|---|---|
| `titel` | nee | staat bovenaan, standaard "Eduface testdag" |
| `opleiding` | ja | de instelling |
| `vak` | ja | het vak, zoals de opleiding het noemt |
| `datum_beoordeling` | nee | wanneer de nakijker het werk beoordeelde |
| `notitie` | nee | een regel over dit bestand zelf, klein en gedempt onder de uitleg |
| `beoordelingsoptie` | ja | zie hieronder |
| `studenten` | ja | zie hieronder |
| `vragen_over_het_vak` | nee | vragen die niet over een student gaan |
| `voetregel` | nee | onderaan de pagina |

### `beoordelingsoptie`

| Veld | Wat erin staat |
|---|---|
| `gekozen` | de optie in het Nederlands, bijvoorbeeld "Voldaan of niet voldaan, per rubriekcriterium" |
| `wat_dat_doet` | een zin over wat het model wel en niet uitspreekt |
| `rangorde` | de oordelen van laag naar hoog, kleine letters. Hieruit volgt of het model strenger of milder is |
| `waarschuwing` | alleen als er iets is dat het hele dossier raakt |

`rangorde` is het enige veld dat rekent. `["niet voldaan", "voldaan"]` bij twee standen,
`["onvoldoende", "voldoende", "goed", "uitstekend"]` bij descriptief beoordelen. Kent de nakijker
een tussenstand die het model niet heeft, zet die er dan tussen. Een oordeel dat niet in de rangorde
staat (bijvoorbeeld `onbekend`) telt nergens in mee en krijgt het label "niet te vergelijken".

### `studenten[]`

| Veld | Wat erin staat |
|---|---|
| `label` | "Student 1". Nooit een echte naam |
| `casus` | een halve regel over de casus |
| `criteria[]` | `naam`, `nakijker`, `eduface`. De drie totalen volgen hieruit |
| `tabel_voet` | uitleg onder de tabel, bijvoorbeeld over een ontbrekende uitkomst |
| `eindoordeel_nakijker` | het eindoordeel, in een zin |
| `feedback_nakijker` | de geschreven eindfeedback, letterlijk |
| `feedback_eduface[]` | `criterium` en `tekst`, letterlijk zoals het model het schreef |
| `verschillen[]` | `criterium`, `richting`, `nakijker_tekst`, `eduface_tekst`, `vraag` |
| `aannames[]` | `kop`, `vraag`, `model_zegt`, `rubriek_zegt`, `nakijker_deed` |
| `opdracht` | `{"los": "..."}` als het werk een apart bestand is, of `{"tekst": "..."}` om het op te nemen |

### Vraagnummers

Die zet je niet zelf. Het bestand nummert elke `vraag` door in de volgorde waarin hij staat:
eerst de verschillen en aannames van student 1, dan die van student 2, dan de vragen over het vak.
Verschuif je iets in de JSON, dan verschuiven de nummers mee. Bouw dus niet opnieuw nadat het
antwoordblad geprint is.

## Controleren voor je oplevert

```bash
python3 bouw.py voorbeeld-cat-diagnostiek.json /tmp/proef.html
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-sandbox --disable-gpu \
  --window-size=1440,1000 --virtual-time-budget=4000 --screenshot=/tmp/proef.png file:///tmp/proef.html
```

Loop daarna langs:

- staat er nergens een naam van een nakijker of een student
- klopt de rangorde, dus staan "model strenger" en "model milder" de goede kant op
- zijn het er hoogstens drie vragen per onderdeel
- opent het bestand met wifi uit
