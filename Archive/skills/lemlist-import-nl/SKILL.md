---
name: lemlist-import-nl
description: VERVANGEN op 2026-09-10 door `lemlist-import`, die het marktprofiel leest (projects/shift/markets/<code>/) en voor elke markt werkt. Gebruik `lemlist-import` met --markt nl voor NL-werk. Dit bestand blijft alleen staan zodat lopende chats en journaalregels niet breken.
---

> **Deze skill is vervangen.** Gebruik **`lemlist-import`** (`.claude/skills/lemlist-import/SKILL.md`), met `--markt nl`. Sinds 10-09-2026 is de markt een variabele: de skills zijn marktloos en alle NL-kennis staat in `projects/shift/markets/nl/profiel.md`. De inhoud hieronder is de NL-versie van vóór die datum en wordt niet meer bijgewerkt.


# Lemlist-import NL

De vaste, herhaalbare manier om nieuwe NL-connectieverzoeken en opvolgmails in Lemlist te zetten. Dante
hoeft alleen te zeggen "voeg de leads toe aan Lemlist". Jij haalt ze van de vaste bron, checkt de regels
hieronder, en zet ze in de juiste campagne.

## Welke campagne?

**De campagnenamen in Lemlist zijn hernoemd. Gecontroleerd op 2026-08-18, ga op de ID af, niet op de naam.**

- **`cam_qpkMQ2axpN7wt7HZt`, "Shift NL - invite, mail, reminder, call", status draft** — **nieuwe batches gaan hierin** (gebouwd 2026-08-24, sequence `seq_SkhvuDrvujbykzjnY`). Vier stappen, één reminder en één belmoment, uitgesmeerd over elf dagen:
  1. `stp_v73CebovE6NTmdnfJ` LinkedIn-invite, dag 0, `{{linkedInConnectionRequest}}`
  2. `stp_CMnSGWFcoib3ohphq` mail 1, +2 dagen, `{{firstEmailSubject}}` + `{{firstEmail}}`
  3. `stp_9NFYys9oMBPnjhyij` reminder, +5 dagen, **leeg onderwerp** (gaat als reply in dezelfde thread), `{{reminder1}}`
  4. `stp_p225fKzkB9GghMLug` belafspraak-taak, +4 dagen, prioriteit hoog

  Er zit **geen afsluitmail** in, bewust: het belmoment vervangt de breakup. Het onderwerp van stap 3 moet leeg blijven, anders breekt de thread en verliest de reminder zijn context.

- **`cam_sjhBnYPdNqMQBvKYZ`, nu "Li + mail", status running** — de vorige campagne. Bevat de batches van 13-08 en 18-08 die nog lopen. **Niet ombouwen en niet verwijderen**, laat die leads hun sequence afmaken. Geen nieuwe leads meer in.
  Hier zit de batch van 13-08 in en de batch van 18-08. Sequence: connectieverzoek direct, mail na 2 dagen,
  belafspraak-taak na nog 1 dag. Eén rechte lijn, geen conditional.
- **`cam_WL8HctM3hFxiHBpos`, nu "Mail flow", status running** — heette eerder "Shfit warm call". Bevat de
  oudere batch van 12-08 en heeft wél de conditional al-verbonden-check. Niet meer gebruiken voor nieuwe
  NL-opleiders tenzij Dante er expliciet om vraagt.
- **`cam_snpX4Mjz5dMRKyANb`, nu "Test ronde", ended** — heette eerder "Shift". Niet gebruiken.

Draai `get_campaigns` voor je begint. De namen zijn al twee keer veranderd terwijl de ID's gelijk bleven,
dus vertrouw op de ID plus een `get_campaign_sequences`-check dat de stappen nog kloppen.

## Sequence van "Shfit warm call" (niet zelf opnieuw uitvinden)

```
conditional (linkedinNetworkCheck: al 1e-graads verbonden?)
├─ JA  (seq_kRuaBSBnnxs7eQDFX) → mail direct → belafspraak-taak 2 dagen later
└─ NEE (seq_wbabbSeeSRJpTnhdm) → connectieverzoek direct → mail 5 dagen later → belafspraak-taak 2 dagen later
```
Let op: dit is de sequence van "Mail flow" (`cam_WL8HctM3hFxiHBpos`), niet die van "Li + mail". Bij twijfel
`mcp__claude_ai_Lemlist__get_campaign_sequences` draaien om te bevestigen dat de structuur nog klopt voor
je een sequence-wijziging doet.

## Bron

Alles komt uit het master-document, via één commando:

```bash
python3 .claude/scripts/pipeline.py export lemlist --out /tmp/lemlist-batch.csv
```

Dat levert precies de mensen met `bericht_status=goedgekeurd` die nog niet geïmporteerd zijn, in de
kolomnamen die Lemlist verwacht: `Voornaam Achternaam, Organisatie, Domein, Email, EmailStatus,
linkedInUrl, linkedInConnectionRequest, firstEmailSubject, firstEmail, person_id`. De `<br>`-fix hieronder
is al toegepast op `firstEmail`.

De kolom `person_id` is er zodat je na de import kunt terugschrijven welke lead waar terecht is gekomen.
Die kolom haal je eruit voor je naar Lemlist stuurt.

Concepten die Dante nog niet heeft goedgekeurd komen hier niet in. Wil je zien wat er klaarstaat:
`pipeline.py status`, regel `stage_5_klaar_voor_lemlist`.

## KRITIEKE BUG: opvolgmails renderen kapot zonder handmatige `<br>`-tags

Lemlist's e-mailstap wrapt de variabele in `<p>{{firstEmail}}</p>`. HTML negeert kale `\n`/`\n\n`
regeleinden binnen die ene paragraaf, dus de hele mail wordt één tekstbrei zonder enige witregel. Getest
en bevestigd op 2026-08-12 (Dante zag het zelf in de Lemlist-preview).

- **De Liquid-filter `{{firstEmail | newline_to_br}}` werkt NIET** in Lemlist — geprobeerd, gaf letterlijk
  de tekst "newline_to_br" terug in plaats van 'm toe te passen. Niet opnieuw proberen.
- **De enige werkende fix: zet de line breaks al in de brondata.** Voor je `firstEmail` in een custom
  variable zet, vervang in de tekst zelf `\n\n` (alinea-einde) door `<br><br>` en losse `\n` (bv. in de
  sign-off) door `<br>`. Dus niet `Hi Naam,\n\nAlinea 1...` maar `Hi Naam,<br><br>Alinea 1...`.
- **Altijd verifiëren met `mcp__claude_ai_Lemlist__preview_email`** (leadId + stepId) voor je een hele
  batch erdoorheen jaagt — dat rendert exact zoals Lemlist het zou versturen, kost geen credits. Test op
  één lead, zie de witregels echt terug, dan pas de rest.
- Geldt voor **elke** e-mailstap in **elke** campagne die `{{firstEmail}}` of soortgelijke multi-paragraaf
  variabelen gebruikt, niet alleen deze ene.

## E-mailadres: niet vooraf nodig

Een lead zonder e-mailadres mag gewoon toegevoegd worden. De LinkedIn-tak werkt sowieso zonder e-mail, en
voor de mailstap kan Dante achteraf zelf de Lemlist-enrichment-feature (`findEmail`) draaien in de UI, of
jij draait 'm via `mcp__claude_ai_Lemlist__enrich_lead` met `findEmail: true` — **dat kost credits, dus
vraag eerst expliciet akkoord voor je 'm aanzet**, voeg de lead nooit zomaar zonder e-mail weg omdat je
"toch geen adres hebt". Naam en LinkedIn-URL zo compleet en correct mogelijk meegeven (volledige achternaam,
juiste LinkedIn-slug) helpt de enrichment een betere hit te vinden.

## Dedupe: geef altijd een sterk identifier mee

`add_leads_to_campaign` dedupt server-side, maar alleen op wat je meestuurt. Een lead met alleen
`firstName`+`lastName` en een lead met dezelfde naam + e-mail/LinkedIn-URL worden als **twee losse leads**
gezien als de identifiers niet overlappen. Zo ontstond op 2026-08-12 een dubbele Joan Janssens-lead (twee
sessies voegden haar toe, met net andere velden). Geef dus altijd op zijn minst `linkedinUrl` mee, en
`email`+`companyDomain` als je die hebt. Kom je een dubbele lead tegen: check welke van de twee een
e-mailadres of de meeste data heeft, hou die aan, verwijder de andere met
`mcp__claude_ai_Lemlist__delete_campaign_leads` (verplicht eerst preview zonder `confirmed`, dan pas
`confirmed: true` na akkoord van Dante — nooit stilzwijgend verwijderen).

## Stappen

1. **Check eerst twee dingen per lead voor je toevoegt:**
   - [[one-send-per-org]] — staat er al iemand anders van dezelfde organisatie in de batch of al in de
     campagne? Dan maar 1 versturen, de hoogste in de boom.
   - [[single-channel-per-lead]] — loopt er al een cold call of ander kanaal op deze persoon/organisatie
     (check Close)? Dan niet zomaar een tweede kanaal openen, eerst aan Dante voorleggen.
2. **Bouw de leads** met `firstName`, `lastName`, `companyName` (+ `companyDomain` als bekend), `linkedinUrl`,
   `jobTitle`, en `customVariables`: `linkedInConnectionRequest` (letterlijk, niet herschrijven),
   `firstEmailSubject`, `firstEmail` (met de `<br>`-fix hierboven toegepast).
3. **Importeer** met `mcp__claude_ai_Lemlist__add_leads_to_campaign`, in batches van max 100. Zet **geen**
   enrichment aan tenzij Dante er expliciet om vraagt (kost credits). `deduplicate` op default (false).
4. **Verifieer de eerste paar met `preview_email`** dat de opmaak goed staat voor je het rapporteert als klaar.
5. **Rapporteer kort:** hoeveel added / skipped / failed, en de namen van eventuele duplicate/failure-gevallen.
6. **Schrijf terug naar het master-document**, per geïmporteerde lead:
   ```bash
   pipeline.py set p_xxx --actor lemlist-import-nl \
     --set lemlist_status=geimporteerd \
     --set lemlist_campagne_id=cam_xxx \
     --set lemlist_lead_id=lea_xxx \
     --set bericht_status_toelichting="in campagne [naam] gezet [datum], wacht op start door Dante"
   ```
   Mislukt een lead, zet dan `--set lemlist_status=fout` met de reden in de toelichting, zodat hij
   zichtbaar blijft in plaats van stil te verdwijnen.

## Harde regels

- **Niet laten herschrijven of personaliseren door Lemlist.** De tekst is exact zoals Dante goedkeurde; dat
  breekt de zorgvuldig gekozen haakjes. Zie [[outreach-plain-language]] en [[haakje-must-be-in-source]].
- **Verzenden doet Dante.** De campagne staat op draft. Jij zet leads erin, jij zet hem niet live.
- **Spreiden.** Uitnodigingen met noot (300 tekens) tellen strenger bij LinkedIn. Als Dante vraagt te
  verzenden: adviseer spreiden over meerdere dagen, niet in één bak.
- Verzenden loopt via Dante's eigen LinkedIn (Premium). Check dat de LinkedIn-stap op dat account staat.
- **Structuurwijzigingen aan de sequence** (stap toevoegen/verwijderen/aanpassen) zijn confirmation-required
  tools — nooit zonder expliciet akkoord van Dante, en bij content-wijzigingen (`update_sequence_step`)
  altijd eerst `preview_sequence_update` draaien en de diff laten zien.

## Nieuwe batch van Agent 4 / linkedin-outreach

Als een nieuwe batch opvolgmails opgeleverd wordt, komen die pas in beeld zodra ze in `berichten-nl.csv`
op Status "klaar"/"goedgekeurd door Dante" staan. Twijfel je of een net-afgeleverde batch al goedgekeurd
is: check die Status-kolom, niet zomaar concepten importeren. Zie ook de opvolgmail-stemregels in
[[content-voice]] (`voice-by-type.md`, sectie "Opvolgmail na LinkedIn-connectieverzoek") — die bepalen HOE
de mail geschreven wordt, deze skill bepaalt alleen hoe 'm technisch in Lemlist komt.

## Kanaal

De NL-opleiderscampagne draait op [[outreach-kanaal-linkedin]] als eerste touch, met een e-mail en
belafspraak als opvolging in de warm-call-flow. LinkedIn-URL blijft het belangrijkste identifier-veld per lead.
