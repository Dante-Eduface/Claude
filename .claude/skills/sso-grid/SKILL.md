---
name: sso-grid
description: ALLEEN de visuele output-stap. Maakt van een AL INGEVULDE MEDDPICC/SSO deal-kwalificatiegrid een strakke Eduface-styled PNG en hangt die als bijlage onder een note in Close op de juiste lead. Deze skill scoort of kwalificeert de deal NIET zelf, hij rendert alleen een bestaande grid naar een plaat. Wil Dante de deal juist SCOREN, invullen, reviewen of doorlopen (line-by-line coaching, waar staat de deal, is er een stap overgeslagen), gebruik dan de skill meddpicc, NIET deze. Werkt op drie manieren: (1) uit de MEDDPICC SSO.xlsx in Google Drive, tab per klant, (2) Dante levert een ingevulde grid aan (screenshot, CSV of tekst) en ik lees het uit, of (3) Dante beschrijft de stand van de deal in gewone taal en ik stel de grid zelf samen. Trigger ALLEEN wanneer Dante een visuele plaat/PNG wil: "maak een SSO grid", "maak een sales grid", "render de grid", "maak er een plaat van", "zet de grid in Close", "hang de grid als bijlage", of een ingevulde grid/scoring matrix aanlevert om te visualiseren. NIET triggeren op "kwalificeer deze deal", "score deze deal", "vul de grid in", "hoe staat deze deal ervoor" (dat is meddpicc).
---

# MEDDPICC / SSO Grid

Zet een deal-kwalificatie om in één heldere plaat. De keten loopt van **Google Drive → PNG → Close**. De **PNG is de deliverable**, en die hoort als **bijlage onder een note op de lead in Close** te belanden. Stop dus niet bij de PNG.

## Drie input-routes

**Route 0 (default): Google Drive.** De bron is **`MEDDPICC SSO.xlsx`** in Drive (eigenaar Jeroen, gedeeld met Dante). Eén tab per account: BSU, HR, HHS, Uni Tilburg, Radboud, RUG, ICM, Capabel (2x).

1. Zoek het bestand: `search_files` met `title contains 'MEDDPICC SSO'`.
2. `read_file_content` op het `fileId`. Dat geeft alle tabs achter elkaar als één platte tekst.
3. Knip de juiste tab eruit: begin bij `CUSTOMER NAME:,,<KLANT>` en stop bij de volgende `CUSTOMER NAME:`.
4. Lees per criterium af waar de `1` staat. De rij ná elk criteriumblok ziet er zo uit: `,,,1,,,,,8,,,` → de positie van de `1` is de gekozen schaalwaarde (0/2/4/6/8/10), het losse getal erachter is de punten (weging × score).
5. Reken na dat de som van de punten klopt met de `TOTAL SCORE` in het blad. Wijkt het af, meld dat en render niet blind.

**Route 1: aangeleverde grid.** Dante plakt een screenshot van de Excel, een CSV, of tekst. Lees per criterium de **weging** en de **gekozen score** uit en reken na.

**Route 2: prompt.** Dante beschrijft de stand van de deal. Stel de grid zelf samen op basis van die beschrijving + Close + de projectcontext. **Laat je scores eerst zien met een korte onderbouwing** voordat je rendert, zodat Dante kan corrigeren.

**Krijg je maar een deel van de grid?** Reken na of de wegingen optellen tot 25 en het totaal klopt. Zo niet, vraag het ontbrekende stuk op. Nooit criteria verzinnen.

**Ziet de grid er verouderd uit** (bijv. champion op 0 terwijl je uit Close of de projectmap weet dat er wél een champion is), render dan wat er in de tab staat, maar **zeg tegen Dante dat het blad achterloopt** en wat er niet klopt.

## De 9 criteria

Vaste criteria, vaste wegingen, score 0/2/4/6/8/10. De volledige niveau-labels per criterium staan in `reference.md`. **Lees dat altijd voor je scoort.**

| Criterium | Weging |
|---|---|
| Sales Stage | 2 |
| Metrics | 3 |
| Economic Buyer | 4 |
| Decision Criteria | 3 |
| Decision Process | 2 |
| Paper Process | 2 |
| Identify Pain | 3 |
| Champion | 4 |
| Competition | 2 |

**Sales Stage zet de funnelpositie.** Zet die als aparte chip in de header.

## Rekenregels

- **Punten per criterium** = weging × score
- **Som wegingen** = 25, dus **max = 250**
- **Win-kans %** = totaalscore / 250

Reken altijd na en check dat je totaal klopt met de som van de rijen. Klopt het niet met de aangeleverde grid, meld dat.

## Salestaal

Anker aan `cro`. Belangrijkste: **we sturen op de uitrol, niet de pilot**, en de **EB is de uitrol-budgethouder**, niet de manager die een pilot kan goedkeuren. Beschrijf Economic Buyer en Metrics dus in uitrol-termen.

## Bouwen

1. Kopieer `template.html` uit deze skill-map.
2. Vul klant, type, deal value (ARR), datum, funnel-stage, en per criterium: weging, statuslabel, één zin NL-uitleg, de gemarkeerde schaalwaarde, en de punten.
3. Kleurcodeer de linkerrand van elke rij: **rood `#e05a4f`** bij score 0, **oranje `#e0a43b`** bij 2-6, **groen `#1fb98a`** bij 8-10.
4. Render naar PNG:
   ```
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
     --hide-scrollbars --force-device-scale-factor=2 --window-size=1180,1010 \
     --screenshot="<naam>.png" "<naam>.html"
   ```
5. **Lees de PNG terug** om te checken dat er niks is afgekapt. Past het niet, verhoog de window-hoogte en render opnieuw.
6. Opslaan in `projects/<deal>/` als `sso-grid-<klant>.png`.

## In Close zetten (laatste stap, altijd doen)

De PNG hoort als **bijlage onder een note** op de juiste lead. De note-titel is **`SSO grid 1`**. Staat er al een `SSO grid 1`, tel dan op: `SSO grid 2`, `SSO grid 3`, enzovoort. Zo blijft de historie van de deal zichtbaar.

1. Zoek de lead: `lead_search` met de instellingsnaam (let op, zoek op de **volledige naam**, niet op de afkorting uit de tab; "RUG" geeft niks, "Groningen" geeft "Rijksuniversiteit Groningen").
2. Check met `find_notes` op die lead of er al een `SSO grid N` staat, en bepaal het volgnummer.
3. Hang de PNG eronder met het script in deze skill-map:

```
CLOSE_API_KEY=$CLOSE_API_KEY python3 .claude/skills/sso-grid/scripts/close_attach.py \
  --lead-id <lead_id> \
  --png projects/<deal>/sso-grid-<klant>.png \
  --title "SSO grid 1" \
  --note "MEDDPICC/SSO grid <klant>, stand <datum>. Stage <stage>, <score>/250 (<pct>%)."
```

**Waarom een script en niet de MCP:** de Close MCP-server heeft `create_note`, maar dat kent geen `attachments`-veld. Bijlagen kunnen alleen via de REST API (signed S3 upload, dan de note met `attachments[]`). Het script doet die drie stappen.

**Setup, eenmalig:** het script heeft `CLOSE_API_KEY` nodig (Close → Settings → API Keys). Zet die in `.claude/settings.local.json` onder `env`, dan blijft hij lokaal en gaat hij niet mee in git. Ontbreekt de key, maak dan **geen** halve note aan: zeg tegen Dante dat de key mist en lever de PNG aan zodat hij hem zelf kan slepen.

## Niet doen (harde regels, feedback van Dante)

- **Geen "grootste hefbomen"-blok.**
- **Geen sterk/zwak-tekst in de scorebalk.**

Houd het puur: header + meta-chips + de grid + totaalscore + win-kans + footer. Verder niks.

## Done

- [ ] Alle 9 criteria staan erin met weging, status, schaal en punten.
- [ ] Wegingen tellen op tot 25, totaal en win-kans nagerekend en kloppend tegen de bron.
- [ ] Kleurcodes correct (rood 0, oranje 2-6, groen 8-10).
- [ ] PNG teruggelezen, niks afgekapt.
- [ ] Opgeslagen in `projects/<deal>/`.
- [ ] In Close gezet: note `SSO grid N` op de juiste lead, met de PNG als bijlage.
