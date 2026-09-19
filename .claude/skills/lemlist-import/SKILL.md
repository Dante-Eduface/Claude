---
name: lemlist-import
description: >
  Agent 5 van de SHIFT-pijplijn, voor elke markt. Zet goedgekeurde berichten (LinkedIn-invite, mail 1, reminder)
  uit het master-document in de Lemlist-campagne van de markt. De campagne-ID staat in
  GTM/Campaigns/shift/markets/<code>/profiel.json onder lemlist_campagne_id; ga altijd op de ID af, nooit op de naam.
  Trigger wanneer Dante zegt "voeg de leads toe aan Lemlist", "zet ze in Lemlist", "importeer de nieuwe leads",
  "de UK-batch mag naar Lemlist", of iets in die geest. Weet zelf: geen e-mailadres nodig vooraf, en de mails
  moeten met <br>-tags anders valt de opmaak weg. Vervangt lemlist-import-nl sinds 10-09-2026.
---

# Lemlist-import

## Altijd de connector, nooit de API

**Besluit Dante 16-09-2026: al het Lemlist-verkeer loopt via de claude.ai-connector.** Niet via `curl`, niet via `call_api`, niet via een Python-script met de API-sleutel.

Reden: de REST API geeft op dit account op elk endpoint en elke versie `403 error code 1010`, ook met een verse sleutel. Dat is geen sleutelprobleem maar een accountprobleem, REST-toegang zit niet in het abonnement. De connector werkt wel. Een script dat het toch over HTTP probeert faalt dus altijd, en kost alleen tijd om erachter te komen.

Gevolg voor `pipeline.py sync-lemlist`: dat commando praat zelf niet met Lemlist. Jij haalt de leads op met de connector, zet ze in een JSON-bestand, en het script leest dat bestand.

**Let op bij het ophalen: de connector kapt `activities` af bij grote batches.** Bij `limit: 50` kwamen de laatste leads van elke pagina terug met een lege of half afgekapte activiteitenreeks, en de sorteervolgorde is niet stabiel tussen aanroepen. Haal in vensters van **10** op, en controleer daarna dat je evenveel unieke leads hebt als de campagne zegt.

```
search_campaign_leads(campaignIds=[...], include=["activities"], limit=10, offset=N)
python3 .claude/scripts/pipeline.py --markt <code> sync-lemlist --invoer /tmp/leads.json --droog
python3 .claude/scripts/pipeline.py --markt <code> sync-lemlist --invoer /tmp/leads.json
```

De vaste, herhaalbare manier om goedgekeurde berichten in Lemlist te zetten. Dante hoeft alleen te zeggen "voeg de leads toe aan Lemlist" en welke markt. Jij haalt ze uit het master-document, checkt de regels hieronder, en zet ze in de campagne van die markt.

## Eerst: welke markt, welke campagne

1. Noemt Dante geen markt, vraag het in één regel.
2. Lees `GTM/Campaigns/shift/markets/<code>/profiel.json`: `lemlist_campagne_id` is de campagne. Is die leeg, dan **stop je** en meld je dat de campagne voor deze markt nog niet bestaat. Bouw hem alleen na expliciet akkoord van Dante, met de vaste vier stappen hieronder, en zet daarna de ID in `profiel.json` (actor dante).
3. Draai `get_campaigns` en `get_campaign_sequences` op die ID om te bevestigen dat de stappen nog kloppen. Campagnenamen worden hernoemd, ID's niet.
4. Lees in `profiel.md` de kop **Kanaal**: welke stappen deze markt gebruikt en wat er per lead in moet.

## De vaste sequence, per markt één campagne

Drie stappen over zeven dagen:

1. LinkedIn-invite, dag 0, `{{linkedInConnectionRequest}}`
2. mail 1, +2 dagen, `{{firstEmailSubject}}` + `{{firstEmail}}`
3. reminder, +5 dagen, **leeg onderwerp** (gaat als reply in dezelfde thread), `{{reminder1}}`

Het onderwerp van stap 3 moet leeg blijven, anders breekt de thread.

**Geen belafspraak-taak meer** (besluit Dante 16-09-2026). Die stond als stap 4 in de oude NL-campagne en verving de breakup-mail, maar bellen loopt via `/cold-call-prep` met een echt belscript, niet via een taak zonder voorbereiding. Er zit ook geen afsluitmail in.

Markten met alleen `linkedin` als kanaal gebruiken stap 1 en 4. De oude NL-campagnes en hun geschiedenis staan in `GTM/Campaigns/shift/markets/nl/profiel.md` onder **Kanaal**; nooit ombouwen, nooit verwijderen.

## Bron

Alles komt uit het master-document, via één commando:

```bash
python3 .claude/scripts/pipeline.py --markt <code> export lemlist --out /tmp/lemlist-batch.csv
```

Dat levert precies de mensen van deze markt met `bericht_status=goedgekeurd` die nog niet geïmporteerd zijn, in de kolomnamen die Lemlist verwacht: `Voornaam Achternaam, Organisatie, Domein, Email, EmailStatus, linkedInUrl, linkedInConnectionRequest, firstEmailSubject, firstEmail, reminder1, person_id`. De `<br>`-fix hieronder is al toegepast op `firstEmail` en `reminder1`.

De kolom `person_id` is er zodat je na de import kunt terugschrijven welke lead waar terecht is gekomen. Die haal je eruit voor je naar Lemlist stuurt.

Concepten die Dante nog niet heeft goedgekeurd komen hier niet in. Wil je zien wat er klaarstaat: `pipeline.py --markt <code> status`, regel `stage_5_klaar_voor_lemlist`.

## KRITIEKE BUG: mails renderen kapot zonder `<br>`-tags

Lemlist wrapt de variabele in `<p>{{firstEmail}}</p>`. HTML negeert kale regeleinden, dus de hele mail wordt één tekstbrei. Getest en bevestigd op 2026-08-12.

- **De Liquid-filter `newline_to_br` werkt NIET** in Lemlist. Niet opnieuw proberen.
- **De enige werkende fix: de line breaks in de brondata.** `export lemlist` doet dat al. Zet je zelf iets in een custom variable, vervang dan `\n\n` door `<br><br>` en `\n` door `<br>`.
- **Altijd verifiëren met `preview_email`** (leadId + stepId) op één lead voor je een hele batch erdoorheen jaagt. Kost geen credits.

## Na de import: de lus sluiten

De import is niet klaar als de leads erin staan. Wat de campagne vervolgens doet moet terug het master-document in, anders blijft er staan dat er 45 berichten uit zijn gegaan en nul geaccepteerd (dat was letterlijk de stand op 16-09-2026).

```bash
python3 .claude/scripts/pipeline.py --markt <code> sync-lemlist
python3 .claude/scripts/pipeline.py --markt <code> rapport --table
```

`sync-lemlist` zet `linkedin_geaccepteerd_op` en `reactie_gekregen_op`, meer niet. Wat een reactie betekende legt Dante vast met `pipeline.py uitkomst`, in de woorden van de prospect zelf. De nachtronde draait de sync automatisch; na een import met de hand draai je hem zelf.

## E-mailadres: niet vooraf nodig

Een lead zonder e-mailadres mag gewoon toegevoegd worden. De LinkedIn-stap werkt zonder e-mail, en voor de mailstap kan Dante achteraf de Lemlist-enrichment (`findEmail`) draaien, of jij via `enrich_lead` met `findEmail: true`. **Dat kost credits, dus vraag eerst expliciet akkoord.**

## Dedupe: geef altijd een sterk identifier mee

`add_leads_to_campaign` dedupt server-side, maar alleen op wat je meestuurt. Geef altijd op zijn minst `linkedinUrl` mee, en `email`+`companyDomain` als je die hebt. Kom je een dubbele lead tegen: hou de meest complete, verwijder de andere met `delete_campaign_leads` (eerst preview zonder `confirmed`, dan pas `confirmed: true` na akkoord van Dante).

## Stappen

1. **Check per lead voor je toevoegt:**
   - één verstuurmoment per organisatie: staat er al iemand van dezelfde organisatie in de batch of in de campagne? Dan maar één, de hoogste in de boom. Kijk ook over markten heen (`pipeline.py show org_x`), want een concern kan in twee markten staan.
   - één kanaal per lead: loopt er al een cold call of ander kanaal (check Close)? Dan eerst aan Dante voorleggen.
2. **Bouw de leads** met `firstName`, `lastName`, `companyName` (+ `companyDomain`), `linkedinUrl`, `jobTitle`, en `customVariables`: `linkedInConnectionRequest` (letterlijk, niet herschrijven), `firstEmailSubject`, `firstEmail`, `reminder1`.
3. **Importeer** met `add_leads_to_campaign`, in batches van max 100. Geen enrichment tenzij Dante erom vraagt.
4. **Verifieer de eerste paar met `preview_email`.**
5. **Rapporteer kort:** hoeveel added / skipped / failed, en de namen van duplicate- of failure-gevallen.
6. **Schrijf terug naar het master-document**, per geïmporteerde lead:
   ```bash
   pipeline.py set p_xxx --actor lemlist-import \
     --set lemlist_status=geimporteerd \
     --set lemlist_campagne_id=cam_xxx \
     --set lemlist_lead_id=lea_xxx \
     --set bericht_status_toelichting="in campagne [naam] gezet [datum], wacht op start door Dante"
   ```
   Mislukt een lead: `--set lemlist_status=fout` met de reden in de toelichting.

## Harde regels

- **Niet laten herschrijven of personaliseren door Lemlist.** De tekst is exact zoals Dante goedkeurde.
- **Verzenden doet Dante.** De campagne staat op draft. Jij zet leads erin, jij zet hem niet live.
- **Spreiden.** Uitnodigingen met noot tellen strenger bij LinkedIn. Adviseer spreiden over meerdere dagen.
- Verzenden loopt via Dante's eigen LinkedIn. Check dat de LinkedIn-stap op dat account staat.
- **Structuurwijzigingen aan de sequence** zijn confirmation-required: nooit zonder expliciet akkoord van Dante, en bij content-wijzigingen eerst `preview_sequence_update` draaien en de diff laten zien.
- **De Lemlist-connector moet geautoriseerd zijn.** Is hij dat niet, zeg dat meteen en stop; Dante koppelt hem opnieuw in zijn connector-instellingen.
