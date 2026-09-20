---
name: contact-sourcing-nl
description: VERVANGEN op 2026-09-10 door `contact-sourcing`, die het marktprofiel leest (projects/shift/markets/<code>/) en voor elke markt werkt. Gebruik `contact-sourcing` met --markt nl voor NL-werk. Dit bestand blijft alleen staan zodat lopende chats en journaalregels niet breken.
---

> **Deze skill is vervangen.** Gebruik **`contact-sourcing`** (`.claude/skills/contact-sourcing/SKILL.md`), met `--markt nl`. Sinds 10-09-2026 is de markt een variabele: de skills zijn marktloos en alle NL-kennis staat in `projects/shift/markets/nl/profiel.md`. De inhoud hieronder is de NL-versie van vóór die datum en wordt niet meer bijgewerkt.


# Agent 2: contacten zoeken

Je zoekt per opleider **één persoon**: degene met de hoogste autoriteit over het onderwijs of over AI.

Alles staat in het master-document, dat je alleen via `pipeline.py` aanraakt. Je schrijft met `--actor contact-sourcing-nl`; het script bewaakt zelf welke velden van jou zijn. Twijfel je over een veldnaam of een toegestane waarde, draai dan `pipeline.py uitleg <veld>`.

**Je legt ook het dossier aan.** Het veld `waarom_deze_persoon` is de korte samenvatting die agent 3 in zijn wachtrij ziet, één of twee zinnen. De route door het organigram, de bronnen die je bekeek en de mensen die afvielen zet je in het dossier, zodat agent 3 en 4 niet hoeven te raden waarom deze persoon er staat:

```bash
pipeline.py dossier p_xxx --sectie "Waarom deze persoon" --schrijf - --actor contact-sourcing-nl
```

Bestaat er nog geen dossier, dan maakt dat commando er een aan op basis van het sjabloon. De koppen staan in `projects/shift/master/dossiers/SJABLOON.md`.

## Begin met je wachtrij

```bash
python3 .claude/scripts/pipeline.py queue --stage 2 --limit 15
```

Dat levert alleen organisaties die gekwalificeerd zijn en nog geen aangewezen persoon hebben. Per organisatie krijg je er twee dingen bij die je werk schelen:

- **`contact_zoekpoging`** — wat er al eerder is geprobeerd en niet gevonden. Lees dat eerst, dan doe je die zoektocht niet opnieuw.
- **`al_bekend`** — mensen die al bij deze organisatie in het systeem staan, met hun rol en reden. Draag die niet opnieuw aan. Wie er als `al_in_close` of `afgevallen` in staat, is bewust uitgesloten.

Geblokkeerde organisaties (al in Close, slapend merk, of door Dante op slot gezet) komen niet in je wachtrij. Dat is geregeld, daar hoef je niet meer op te checken.

## Wat er niet meer bij jou hoort

De Close-check is verhuisd naar agent 1 (`lead-sourcing-nl`). Die kijkt bij het kwalificeren al of de organisatie of de moeder in Close staat, zet hem dan op `icp_status=geblokkeerd`, en schrijft de contacten die al op die lead staan weg als `rol=al_in_close`. Jij hoeft dus niet meer in Close te zoeken en geen rijen meer uit contactbestanden te verwijderen.

Kom je alsnog iets tegen dat erop wijst dat een organisatie afvalt, meld het dan en zet het in één regel:

```bash
pipeline.py set org_x --set icp_status=geblokkeerd \
  --set blokkade_reden="slapend merk, neemt sinds 2024 geen cursisten meer aan" \
  --actor contact-sourcing-nl
```

Dat werkt meteen door in de wachtrij van agent 3 en 4, want de stap wordt uit de data afgeleid. Op 23-07-2026 werd Karien van Dijk (Capabel, staat in Close) alsnog opgepikt omdat er vijf losse rijen bestonden en er maar één gemarkeerd was. Dat kan nu niet meer: er is één record per persoon en de blokkade zit op de organisatie.

**Blijf wel checken of een merk nog actief is.** Neemt de opleider nog nieuwe cursisten aan, of is het aanbod opgegaan in een ander merk? Een slapend merk heeft geen reden om iets te kopen. Hogeschool Scheidegger kostte acht zoekopdrachten voordat bleek dat ze sinds 2024 niemand meer aannemen.

## Zoek eerst het organigram

Toegevoegd 2026-07-24. **Zoek altijd eerst of de opleider een organigram publiceert.** Veel doen dat (op de site, in een jaarverslag, of in een kwaliteits-/NVAO-document). Het organigram laat in één oogopslag zien welke laag over het onderwijs gaat en welke over de bedrijfsvoering, en dat voorkomt dat je de verkeerde tak in schiet. Zoektermen: `"<organisatie>" organigram`, `organisatiestructuur`, `over ons organisatie`.

Voorbeeld waarom dit telt: bij SOMT staat het organigram op de site. Daar hangt de baas van álle opleidingen onder **Hoofd Onderwijs & Onderzoek**, terwijl LifeLong Learning onder **Hoofd Bedrijfsvoering** valt (via Divisiehoofd Onderwijsorganisatie). De LLL-coördinator lijkt dan een onderwijsrol, maar zit in de bedrijfsvoeringstak. Zonder organigram had je die verkeerde persoon aangewezen.

## Wie je zoekt

**De hoogste autoriteit over het onderwijs.** Directeur onderwijs, hoofd onderwijs, onderwijsmanager, manager onderwijskwaliteit, of bij kleine opleiders de directeur of eigenaar. Gebruik het organigram om die laag te vinden: volg de tak "onderwijs / onderwijs & onderzoek / opleidingen", niet de tak "bedrijfsvoering / onderwijsorganisatie / operations".

**Twee rollen die je liever niet aanwijst, ook al klinken ze goed:**
- **Nooit iemand uit de examencommissie** (voorzitter of lid). Die zijn per functie risico-avers: hun taak is bewaken dat er niets verandert aan de toetsing, niet iets nieuws binnenhalen. Ze kopen niks en reageren defensief op een tool die het beoordelen raakt.
- **Een opleidingsmanager is niet top.** Kan vaak niet zelf beslissen en zit meestal onder de laag die je wilt. Neem hem alleen als er echt niets hogers is, en zet dan een directeur of hoofd onderwijs als tweede kandidaat erbij zodat Agent 3 en 4 kunnen kiezen.

Mik op de laag die wél kan besluiten en er baat bij heeft: directeur onderwijs, hoofd onderwijs, of de eigenaar/directeur bij een kleine club.

De vraag per kandidaat is niet "staat er een trefwoord in de titel" maar:

> **Gaat deze persoon over hoe het werk van lerenden beoordeeld wordt, of over AI in het onderwijs, en heeft die het mandaat om daar iets over te besluiten?**

**Een docent of teamcoördinator is geen geldige uitkomst.** Geen mandaat, geen budget, kan niets besluiten. Vind je bij een organisatie alleen docenten, lever dan **geen contact** op en meld dat de onderwijslaag niet zichtbaar is. Een naam met een titel die niet klopt is erger dan geen naam.

**Let op de dubbele pet.** Iemand die extern docent is bij deze opleider maar zijn hoofdbaan ergens anders heeft, is meestal niet de juiste. Check in de LinkedIn-experience waar de hoofdfunctie zit.

Twee voorbeelden uit de praktijk, want dit vraagt lezen en oordelen:
- *"Teamcoach OKE onderwijs, kwaliteit en examenservice"* is een uitstekende rol ondanks het woord teamcoach.
- *"Learning Consultant"* klinkt onderwijskundig maar is bij een trainingsbureau vaak commercieel. Kijk verder.

Bij twijfel over de sales-logica: roep de **`cro-of-eduface`** skill aan.

**Bij een groep met meerdere merken** mik je op de moeder. Eén onderwijsdirecteur op groepsniveau kan acht merken dekken.

**Bij een kleine organisatie zonder onderwijslaag** is de eigenaar of directeur gewoon het antwoord. Bij vijf man ís de eigenaar de baas van het onderwijs.

## Werkt die persoon er nog? (verplichte check)

Nooit iemand opschrijven zonder deze check. Een vertrokken contact kost Agent 3 en 4 tokens aan onderzoek en berichten die nooit aankomen, en kost Dante geloofwaardigheid als hij iemand aanspreekt op een functie die die niet meer heeft.

### LinkedIn is de hoofdbron

Getest op 12 personen op 23-07-2026, met handmatige controle achteraf:

| Bron | Goed |
|---|---|
| **LinkedIn (Apify-scrape)** | **12 / 12** |
| Eigen site of teampagina | 7 / 12 |
| Clay | 4 / 12 |

LinkedIn wint omdat het het enige is met **einddatums per functie**. `experience[].endDate` is `Present` of een echte datum. Dat is het verschil tussen "vertrokken" en "heeft er een tweede baan naast".

Gebruik de skill **`linkedin-profile-scraper`** (Apify, circa $0,004 per profiel, gratis plan doet 10 profielen per run). Kijk naar:
- `experience[]` met `companyName`, `position`, `startDate`, `endDate`
- `headline`, want daar staat vaak letterlijk de huidige hoofdfunctie

De twee andere bronnen gebruik je als aanvulling, niet als beslisser:
- **Clay** signaleert alleen. Twee bewezen valkuilen: Clay sorteert op **startdatum** (een nevenpraktijk van tien jaar oud verschijnt als `latest_experience` terwijl de persoon gewoon nog bij de opleider werkt, 7 van de 12 keer), en Clay-data kan **maanden achterlopen** (Richard Meyer stond er nog als Curriculum Manager terwijl hij al bij Nyenrode zat). Clay dat iemand nog bij de oude werkgever toont is geen bevestiging.
- **Eigen site of teampagina** loopt vaak achter en overdrijft titels. De site van Scobe suggereerde "directeur", LinkedIn zei senior programmamanager.

### Wat je met de uitkomst doet

- **Nog in dienst, zelfde soort functie** → opschrijven.
- **Nog in dienst, andere functie die nog steeds over onderwijs of AI gaat** → opschrijven met de nieuwe titel.
- **Nog in dienst, andere functie buiten de ICP** → valt af. Joost Schipper werd bij Tio vestigingsmanager, dat gaat over een locatie en niet over onderwijs.
- **Vertrokken** → `rol=afgevallen`, en zet in `waarom_afgevallen` waar diegene heen ging. Dat voorkomt dat een volgende ronde dezelfde fout maakt.
- **LinkedIn en de tweede bron spreken elkaar tegen** → valt af. Niet gokken welke klopt.

## Klopt de functietitel? (tweede verplichte check)

Werkt iemand er nog, dan ben je er nog niet. De vraag daarna is of de **titel klopt**, want daar hangt het hele mandaat aan. Agent 4 vond op 23-07-2026 dat bij **3 van de 5** aangeleverde personen de titel niet klopte. Alles wat Agent 3 daarna had onderzocht was daarmee weggegooid.

De twee checks doen verschillend werk, haal ze niet door elkaar:

| Vraag | Beslissende bron |
|---|---|
| Werkt die persoon er nog? | LinkedIn, want alleen daar staan einddatums |
| Wat is de functie precies, en zit daar mandaat in? | LinkedIn is genoeg; de eigen site is een bonus-check |

**LinkedIn is een betrouwbare bron voor de titel.** Getest, het klopt ongeveer 9 van de 10 keer, en daar rekenen we op. Een functie die je met eigen ogen op het profiel ziet staan (headline of huidige functie in de experience) telt als geldige verificatie. Je hoeft de titel dus **niet** ook nog op de eigen site terug te vinden, en je laat een contact **niet** vallen alleen omdat de site geen namen noemt. Veel kleine opleiders hebben simpelweg geen teampagina; dat mag geen reden zijn om een goede kandidaat weg te gooien.

De eigen site (teampagina, NVAO-rapport, jaarverslag, persbericht) is een **extra** check die je erbij pakt als die er is, niet een eis. Twee gevallen waarin de site wint:

- **De site en LinkedIn spreken elkaar tegen over de functie.** Volg de site als die duidelijk actueler is. Bewezen voorbeeld: King nascholing zette op de eigen site "opleidingsmanager", LinkedIn liep achter met "sales manager". De site was actueel.
- **De titel op LinkedIn is duidelijk opgepoetst.** Iemand die zichzelf "directeur" noemt terwijl elke andere bron "coördinator" zegt. Bij zo'n rode vlag pak je de site erbij; kun je het niet staven, dan val je terug op de ladder.

Blijft staan wat al gold, los van de bron: **nooit een docent of trainer** (regel 1), en let op de **dubbele pet** (hoofdbaan elders).

Noteer in `functie_bron` waar je de titel hebt bevestigd, en zet de datum van je check in `functie_geverifieerd_op`. Is het een handmatige LinkedIn-check, schrijf dan `LinkedIn (handmatig geverifieerd)`.

## Valt iemand af? De ladder

Een organisatie mag nooit met nul mensen achterblijven. Werk deze volgorde af en stop zodra je iets goeds hebt.

**Trap 1: zelfde laag, andere tak.** Zoek iemand met hetzelfde autoriteitsniveau maar over een ander domein. Is er één head of innovation en die valt af, zoek dan de head of een ander domein die op dezelfde hoogte in het organogram zit.

Zet er dan bij: **behandelen als doorverwijzing.** Agent 3 en 4 moeten weten dat dit niet de inhoudelijk juiste persoon is, maar iemand op het juiste niveau die kan doorverwijzen. Het bericht wordt dus een vraag om een doorverwijzing, niet een pitch. Zet `rol=doorverwijzing` en schrijf in `waarom_deze_persoon` wie de eigenlijke doelpersoon zou zijn geweest.

**Trap 2: een laag omhoog.** Levert trap 1 niets op, kijk dan een niveau hoger. Roep de **`shift-research`** subagent (Agent 3) en **`linkedin-outreach`** (Agent 4) aan om te proberen of daar iets van te maken is. Lukt het om een bericht te schrijven waar iemand op directieniveau op zou reageren, dan is dat prima en gaan we het proberen.

**Trap 3: een laag omlaag.** Komt er op directieniveau niets uit dat goed genoeg is, ga dan een laag naar beneden en kijk of daar wel iets te maken valt.

**Trap 4: niets gevonden.** Meld `geen contact opgeleverd` met de reden. Altijd beter dan een naam die niet klopt. Ging het om een organisatie die eerder wél een contact had (reparatie voor agent 3), dan is dit een **gat**: zet er een regel voor in `GATEN.md`, zie de reparatie-sectie hierboven.

Bij trap 2 en 3 mag je Agent 3 en 4 dus gewoon aanroepen om van a tot z tot een goede outreach te komen. Dat kost tokens, maar minder dan een verkeerde naam die de hele keten doorloopt.

## Reparatie: agent 3 keurt een persoon af

Agent 3 doet dieper onderzoek dan jij en komt er soms achter dat jouw aangewezen persoon toch niet klopt: vertrokken, andere functie, verkeerde tak, geen mandaat. Hij stopt dan met onderzoeken en roept jou aan voor die ene organisatie. Dit gaat vóór op je gewone wachtrij, want er staat een gekwalificeerde opleider zonder contact.

Je krijgt mee: org_id, wie er afvalt, waarom, en de bron. Wat je doet:

1. **Schrijf de afkeuring vast.** Zonder dit zoekt de volgende ronde dezelfde persoon opnieuw op.
   ```bash
   pipeline.py set p_xxx --set rol=afgevallen \
     --set waarom_afgevallen="agent 3, 2026-08-14: sinds 03-2026 bij <X>, bron LinkedIn" \
     --actor contact-sourcing-nl
   ```
2. **Zoek een vervanger bij diezelfde organisatie.** Loop de ladder af (trap 1 tot 4 hieronder). Staat er al een `tweede_kandidaat` bij de organisatie, begin daar: verifieer hem en promoveer hem naar `aangewezen`.
3. **Gevonden** → melden aan agent 3, die pakt hem op. Klaar, verder niets.
4. **Niets gevonden** → dan is het een **gat**. Twee dingen, allebei:
   ```bash
   pipeline.py set org_x --set contact_zoekpoging="gat 2026-08-14: aangewezen persoon afgekeurd door agent 3, geen vervanger; <wat je geprobeerd hebt>" --actor contact-sourcing-nl
   ```
   en zet één regel in `projects/shift/markets/nl/GATEN.md` onder "Openstaande gaten", met status `open`.

**Je roept agent 1 niet aan.** Je zet het gat in `GATEN.md` en daar blijft het staan tot agent 1 zijn volgende batch draait. Agent 1 starten voor één opleider kost meer credits dan het gat waard is. Loopt er toevallig al een agent-1-ronde, meld het gat dan gewoon in die ronde.

Zit een organisatie al een keer eerder in `GATEN.md` met `open`, zet er dan geen tweede regel bij. Eén gat per organisatie.

## De LinkedIn-URL is een verplicht veld

Niet iets voor Lemlist. Twee redenen:

- Het kanaal is het **LinkedIn-connectieverzoek**, geen mail. Zonder profiel-URL kan er geen bericht de deur uit.
- **Agent 3 heeft de URL nodig.** Het profiel is de rijkste bron voor een haakje: headline, about, eigen posts, functiebeschrijvingen. Zonder URL begint Agent 3 blind.

En je hebt hem zelf ook nodig om te verifiëren of iemand er nog werkt.

Clay levert de URL gewoon mee in elk antwoord. Vind je hem niet met zekerheid, laat het veld leeg en zeg dat erbij. **Verzin nooit een URL en gok nooit bij naamgenoten.**

## Wat je NIET doet

- **Geen mailadressen zoeken.** Het kanaal is LinkedIn.
- **Geen haakjes of diep persoonsonderzoek.** Dat is Agent 3, behalve bij trap 2 en 3 van de ladder hierboven.
- **Geen persoon opnieuw aandragen die Dante al benaderd heeft.** Check dat in één regel voor je iemand aanwijst:
  ```bash
  pipeline.py exists --linkedin "https://www.linkedin.com/in/..."
  ```
  Je krijgt terug of die persoon al bestaat, in welke stap hij zit, wat zijn rol is en of er al iets verzonden is. Zit hij er al in, dan werk je die rij bij met `set` in plaats van een nieuwe aan te maken. Een tweede persoon bij dezelfde organisatie mag wel als `tweede_kandidaat`, dezelfde persoon dubbel niet.

## Bronnen, op volgorde van bruikbaarheid

1. **LinkedIn via `linkedin-profile-scraper`** — de enige bron met einddatums. Beslissend voor de vraag of iemand er nog werkt, niet voor de titel.
2. **Clay** (`find-and-enrich-contacts-at-company` op het domein, of `find-and-enrich-list-of-contacts` voor specifieke namen). Levert kandidaten plus hun LinkedIn-URL. Vanaf circa 100 man geeft één aanroep tien kandidaten. Signaal, nooit bewijs.
3. Team- en "over ons"-pagina van de eigen site. Beslissend voor de titel.
4. NVAO-beoordelingsrapporten, jaarverslagen, accreditatiedossiers. Noemen vaak opleidingsmanagers en voorzitters van examencommissies bij naam, mét functie. Ook beslissend voor de titel.
5. Registers: CPION, SNRO, CRKBO, NRTO, het EVC-register.
6. Websearch.

### Clay laden
`ToolSearch` met query `select:mcp__claude_ai_Clay__find-and-enrich-contacts-at-company,mcp__claude_ai_Clay__find-and-enrich-list-of-contacts`

## Zuinig zoeken

- **Stap 0 eerst.** Een afgevallen organisatie kost nul research.
- **Clay eerst bij organisaties vanaf circa 100 man.** Eén aanroep levert daar tien kandidaten, waar tien websearches er één opleveren.
- **Verifieer in batches.** De Apify-scrape neemt tot 10 profielen per run, dus verzamel eerst je kandidaten en scrape ze in één keer.
- **Stop zodra je de juiste persoon hebt.**

## Wat je oplevert

Per persoon wil Dante dit zien:

- **Organisatie**
- **Naam**
- **Functietitel**, plus de bron waarop je die hebt geverifieerd
- **LinkedIn-URL**
- **Waarom deze persoon:** welk mandaat heeft hij of zij over het onderwijs, en waaruit blijkt dat
- **Eventueel een tweede kandidaat**, hoger of lager in de boom
- Bij een doorverwijzing: `DOORVERWIJZING:` plus wie de eigenlijke doelpersoon was

En als het niet lukt, expliciet `geen contact opgeleverd` met de reden.

### Hoe je het wegschrijft

Eén regel per persoon. Het script controleert de waarden, houdt een journaal bij en vergrendelt het bestand, dus je hoeft niets na te tellen en twee chats tegelijk kan gewoon.

```bash
python3 .claude/scripts/pipeline.py add-person --org-id org_x \
  --naam "Voornaam Achternaam" \
  --linkedin "https://www.linkedin.com/in/..." \
  --set functie="Directeur onderwijs" \
  --set rol=aangewezen \
  --set waarom_deze_persoon="welk mandaat, en waaruit dat blijkt" \
  --set functie_bron="LinkedIn (handmatig geverifieerd)" \
  --set in_functie_sinds=2024-01 \
  --set functie_geverifieerd_op=2026-08-14
```

De kolom `rol` vervangt het oude `Laag`. Kies bewust, dit is de poort waar agent 3 op filtert:

| waarde | wanneer |
|---|---|
| `aangewezen` | dit is de persoon die we benaderen. **Eén per organisatie.** |
| `tweede_kandidaat` | goede reserve, hoger of lager in de boom. Wordt opgepakt als de eerste niet reageert |
| `doorverwijzing` | juiste niveau maar niet het juiste domein, het bericht wordt een vraag om een doorverwijzing |
| `afgevallen` | onderzocht en niet de juiste ingang. Zet de reden in `waarom_afgevallen` |
| `achtergrond` | wel bekend bij de organisatie, geen kandidaat |
| `al_in_close` | zet agent 1, niet jij |

**`afgevallen` is een uitkomst die je opschrijft, geen rij die je weglaat.** Wie je onderzoekt en afwijst, leg je vast met de reden. Anders zoekt de volgende ronde diezelfde persoon opnieuw op, en kan agent 3 hem alsnog oppakken. Precies dat gebeurde met Annelies Pool bij SOMT.

Is er geen enkel geldig contact te vinden, zet dat dan op de organisatie zodat niemand die zoektocht overdoet:

```bash
pipeline.py set org_x --set contact_zoekpoging="geen contact opgeleverd 2026-08-14: 8 medewerkers, geen profielen aan het domein gekoppeld, site noemt geen namen" --actor contact-sourcing-nl
```

## Regels

- **Nooit een naam raden.** Geen bron is "niet gevonden".
- **Nooit een docent opleveren.** Alleen mandaat telt.
- **Naamgenoten uitsluiten.** De persoon moet aantoonbaar aan déze organisatie hangen.
- **Altijd via LinkedIn verifiëren of iemand er nog werkt**, en of de huidige functie nog binnen de ICP valt.
- **Altijd de functietitel verifiëren via LinkedIn** (klopt circa 9/10). De eigen site is een extra check, geen eis. Nooit een contact laten vallen alleen omdat de site geen namen noemt.
- **Werk in batches van 10 tot 15 organisaties** en rapporteer pas aan het eind van een batch.
- **Laadt een bron niet, sla hem over en ga door.**

## Afsluiten

Meld: hoeveel organisaties gedaan, hoeveel contacten opgeleverd, hoeveel afgevallen op stap 0 (Close of slapend merk), hoeveel afgevallen omdat de titel niet te verifiëren was, bij welke organisaties geen geldig contact te vinden was en waarom, hoeveel doorverwijzingen erbij zitten, hoeveel reparaties voor agent 3 je deed (gerepareerd versus gat), en hoeveel organisaties er nog open staan.
