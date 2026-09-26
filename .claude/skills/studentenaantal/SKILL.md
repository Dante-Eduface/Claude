---
name: studentenaantal
description: Zoekt per Close-lead het juiste studentenaantal en rekent daaruit de Deal value (studenten × €3 × 12, afgerond) voor het veld "Deal value" in Close. Bronvolgorde van Dante, de klant zelf gaat voor, anders officiële bronnen, en niets betrouwbaars is leeg laten. Werkt voor één lead of de hele CRM in één run. Trigger wanneer Dante zegt "zoek het studentenaantal", "hoeveel studenten heeft [lead]", "vul de Deal value in", "reken de dealwaarde uit", "loop de CRM door", "doe dit voor alle leads", of een lead noemt waarvan de omvang onbekend is. Gebruik NOOIT de AI Enrichment van Close hiervoor.
---

# Studentenaantal en Deal value

Het studentenaantal bepaalt de Deal value, dus het moet kloppen. Liever leeg dan fout. De AI Enrichment van Close gaf op 26-09-2026 Bath Spa 8.305 (HESA: 28.970) en Breederode 3.000 (de school zelf: 800). Daarom doe ik het zelf, volgens deze regels.

## Wat telt

- **Alle studenten van de organisatie achter de lead**, instellingsbreed, alle opleidingen.
- **Niet:** pilot- of startgroepen, cohorten, eerstejaars of instroom, één opleiding of faculteit, inzendingen, alumni, medewerkers, en onze eigen prijsstaffels ("laagste staffel 500 studenten").
- **Niet:** zustermerken in dezelfde groep en franchisepartners die onder de naam van de instelling lesgeven. UTI is de UTI-divisie, zonder Concorde. Bath Spa is zonder Global Banking School.
- **Geen school** (uitgever, ziekenhuis, partner): leeg, en op de lijst voor Dante.

## Bronvolgorde

Van meest naar minst betrouwbaar (Dante, 26-09-2026). Elk contact waarin de klant zelf het getal noemt, gaat voor.

1. **Transcript.** Wat iemand van de instelling zegt in een meeting of call, in de ruwe tekst. Niet de AI-samenvatting van Close: die wijst de weg, het transcript is het bewijs.
2. **Wat wij zelf opschreven, en de mail.** Notities en velden in Close, eigen onderzoek van Dante, onze bestanden in de repo, mails in Close en Gmail. Een getal dat de klant in een mail laat staan terwijl hij andere getallen verbetert, telt mee.
3. **Online, alleen officieel.** Registers (DUO, HESA, IPEDS, SEC) en jaarverslagen. Een afgerond getal op een website ("bijna 26.000", "meer dan 3.000") telt niet.
4. **Niets betrouwbaars: leeg.** Met in het bewijsbestand waar ik gezocht heb.

## Als bronnen botsen

- **Een exact getal van de klant wint.**
- **Een schatting van de klant** ("close to", "ongeveer", "bij benadering") telt alleen als geen officieel cijfer er meer dan 25% van afwijkt. Wijkt het wel af, dan de volgende bron.
  - Voorbeeld: Robert (UTI) zei op 26-08 "close to 20,000 students". De SEC-cijfers geven 14.767 gemiddeld actieve studenten in de UTI-divisie, 35% lager. Dus niet 20.000, maar Dantes eigen onderzoek: 14.000.
- **Wat Dante zelf heeft uitgezocht** wint van wat ik online vind. Verschil laten zien, nooit stil overschrijven.

## Werkwijze, één lead

1. **Lokale kopie van Close scannen**, gratis: `python3 .claude/skills/studentenaantal/scan_dump.py --lead "<naam>"`. Leest notities, calls, inkomende mails en meeting-samenvattingen uit `GTM/ICP/pijn-oplossing/close-dump/` en geeft elk getal naast een studentwoord.
2. **Eigen bestanden in de repo:** `GTM/Accounts/<lead>/`, `GTM/sales-coach/data/deals/<lead>.json` en `GTM/ICP/shift/master/orgs.csv` (`lerenden_per_jaar`). Daar staat vaak al uitgezocht werk, zoals RUG 34.314 (DUO) en Windesheim 25.885 (jaarverslag).
3. **Nieuwer dan de kopie:** `activity_search` op de lead vanaf de datum van de dump.
4. **Duikt er een getal op in een meeting of call:** open het transcript (`fetch_meeting_transcript`, bij calls `fetch_call`) en zoek de letterlijke zin. Wie zei het, van welke kant, over welk deel van de organisatie?
   - Alleen meetings die met een samenvatting in de lokale kopie staan, of nieuwer zijn dan de kopie, hebben een transcript. De rest niet openen. Getest op 26-09-2026: De Haagse 15 meetings en Bath Spa 33, samen precies 1 transcript, en dat was de enige die in de kopie stond.
5. **Gmail:** `search_threads` op het domein van de lead plus studenten of students.
6. **Online, alleen als 1 tot 5 niets opleveren:** hoogstens drie opvragingen.
   - Nederland: DUO open onderwijsdata, aantal studenten hoger onderwijs (hbo en wo), meest recente peildatum 1 oktober, opgeteld per instelling. Particuliere opleiders staan daar vaak niet in: dan hun jaarverslag of accreditatierapport.
   - Verenigd Koninkrijk: HESA, inschrijvingen per provider, meest recente jaar. Grote franchise? Dan het deel dat de instelling zelf lesgeeft, uit het jaarverslag of het OfS-dashboard "size and shape of provision".
   - Verenigde Staten: IPEDS, of SEC-filings bij beursgenoteerde scholen.
7. **Oordeel** volgens de regels hierboven. Eén getal of leeg.
8. **Bewijsbestand bijwerken** (zie onder).

## Werkwijze, de hele CRM

- Stap 1 in één keer over alle leads: `scan_dump.py` zonder `--lead`.
- Transcripts alleen openen waar de scan een getal in een meeting of call vindt, plus meetings van na de datum van de kopie. Nooit alle meetings aflopen: de meeste zijn niet opgenomen.
- Registers één keer per markt ophalen (het DUO-bestand, de HESA-tabel) en alle leads van die markt daarin opzoeken, in plaats van per lead te zoeken.
- De rest verdelen over 4 subagents (Sonnet, parallel, ongeveer 5 tot 20 leads elk). De prompt staat in `subagent-prompt.md` in deze map; geef per lead de kandidaten uit de scan mee. Botsingen en schattingen beoordeel ik zelf.
- Volgende run: leads die niet in het bewijsbestand staan, die leeg zijn gebleven, of die een nieuwe meeting hebben sinds `gecheckt_op`.

## Deal value en Close

- **Deal value = studenten × 3 × 12, in euro voor elke markt** (Dante, 26-09-2026: Close rekent in euro). Dezelfde prijs als `GTM/Pricing/prijsmodel-psu-26-27.md`, alleen altijd in euro.
- **Afronden op het eindbedrag, niet op het studentenaantal** (Dante, 26-09-2026): twee significante cijfers, half naar boven. Het studentenaantal blijft exact, want dat is het bewijs. Rekenen met `python3 .claude/skills/studentenaantal/dealwaarde.py <studenten>`: 14.767 wordt €530.000, 800 wordt €29.000, 34.314 wordt €1.200.000.
- Veld: **Deal value** op de lead, type number, id `cf_ARZgGMDLy9SKpqgHhkd1ePYSjin693PjBasUkXzv76q`. Schrijven met `update_lead`, `custom_fields`.
- **Ook de opportunity** (Dante, 26-09-2026): heeft de lead een actieve opportunity, dan krijgt die dezelfde Deal value als waarde per jaar (`update_opportunity`, `value` in centen, `value_period` annual). Gewonnen en verloren opportunities niet aanraken. De oude waarde komt in het bewijsbestand, zodat hij terug te zetten is.
- **Pas schrijven na akkoord van Dante** op de lijst van die run. Leeg is niets schrijven. Een bestaande waarde leegmaken of vervangen alleen na akkoord.
- Nooit `enrich_field`. Nooit statussen wijzigen of leads diskwalificeren, ook niet onder de 300 studenten.

## Bewijsbestand

`GTM/Pricing/studentenaantallen.csv`, één regel per lead:

`lead, lead_id, studenten, deal_value, bron_niveau, bron, citaat, datum_bron, gecheckt_op, opmerking`

- `studenten`: exact. `deal_value`: afgerond, zoals het in Close komt.
- `bron_niveau`: transcript, eigen tekst, mail, officieel of leeg.
- `bron`: activity-id uit Close, Gmail-thread, pad in de repo of url.
- `citaat`: letterlijk, ook bij leeg (dan: waar gezocht).

## Grenzen

- Draai deze skill in een omgeving met volledige netwerktoegang (Dante, 26-09-2026). Zonder die toegang werkt alleen WebSearch: registers en jaarverslagen zijn dan niet te openen en veel leads blijven leeg.
- De lokale kopie verversen kan met `GTM/ICP/pijn-oplossing/close_alles.py`, daar is de Close API-sleutel voor nodig.

## Klaar

- Elke lead heeft een getal met bewijs, of staat leeg met waar gezocht is.
- Kort verslag aan Dante: hoeveel gevuld, hoeveel leeg, en de botsingen en schattingen die hij moet zien, vóór er iets naar Close gaat.
