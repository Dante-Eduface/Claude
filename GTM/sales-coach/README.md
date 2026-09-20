# Sales Coach

Levend CRM plus persoonlijke salescoach. Close blijft de administratie, dit is waar je beter wordt.

**Openen:** `sales-coach.html` in Chrome. Eén bestand, geen server, werkt op de trein.

## Werkwijze

| Wat je zegt | Wat er gebeurt |
|---|---|
| `/sales-coach prep <account>` | Voorbereiding met een advance als doel, vragen uit de MEDDPICC-gaten, plus de focusvaardigheid van deze maand |
| `/sales-coach zelfscore <account>` | Vier vragen over hoe jij denkt dat het ging. Poort: de analyse blijft dicht tot je dit hebt gedaan |
| `/sales-coach debrief <account>` | Transcript uit Close, praatratio, zes scores, missers met citaat, drills |
| `/sales-coach review <account>` | Diagnose van de hele deal tegen MEDDPICC, de handboek-gates en Q-Points |

## Schermen

- **Vandaag** wat aandacht vraagt: openstaande zelfscores, niet gedebriefte gesprekken, deals zonder volgende actie, stil geworden deals
- **Deals** per account: diagnose, volgende actie, voorbereiding, MEDDPICC, tijdlijn met coaching per gesprek, stakeholders
- **Focus** de vaardigheid van deze maand plus alle drills uit je eigen calls
- **Coach** trend per dimensie, terugkerende patronen, laatste missers over alle deals

Toetsen: `1` `2` `3` `4` voor de schermen, `/` voor zoeken.

## Onderhoud

```bash
python3 GTM/sales-coach/scripts/sync_close.py   # Close ophalen
python3 GTM/sales-coach/scripts/build.py        # app opnieuw bouwen
```

`sync_close.py` overschrijft alleen de `close`-zone in elk dealbestand. De `coach`-zone blijft altijd staan.

## Waarom het zo werkt

- **Advance, geen gesprek.** Rackham, 35.000 calls: een volgende afspraak zonder klantactie is een continuation. Situatievragen die je vooraf kon opzoeken verlagen je succeskans.
- **Praatratio is een vlag.** Gong, 326.000 calls (2025): gewonnen 57% reptijd, verloren 62%. Klein verschil, dus signaal en geen norm.
- **Eén vaardigheid tegelijk.** Wekelijks gecoacht 76% quota tegen 47% per kwartaal (MySalesCoach, 3.700 reps). Effectieve coaches pakken één ding per maand.
- **Zelf eerst scoren.** De gap tussen jouw inschatting en de transcript is de coaching. Dat is ook de vaardigheid die een rep tot coach maakt.
