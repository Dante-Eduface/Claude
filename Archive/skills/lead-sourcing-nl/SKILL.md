---
name: lead-sourcing-nl
description: VERVANGEN op 2026-09-10 door `lead-sourcing`, die het marktprofiel leest (projects/shift/markets/<code>/) en voor elke markt werkt. Gebruik `lead-sourcing` met --markt nl voor NL-werk. Dit bestand blijft alleen staan zodat lopende chats en journaalregels niet breken.
---

> **Deze skill is vervangen.** Gebruik **`lead-sourcing`** (`.claude/skills/lead-sourcing/SKILL.md`), met `--markt nl`. Sinds 10-09-2026 is de markt een variabele: de skills zijn marktloos en alle NL-kennis staat in `projects/shift/markets/nl/profiel.md`. De inhoud hieronder is de NL-versie van vóór die datum en wordt niet meer bijgewerkt.


# Agent 1: opleiders zoeken

Je vult de Nederlandse targetlijst van particuliere opleiders voor Eduface (AI-feedback en nakijken op geschreven werk).

Alles staat in het master-document, dat je alleen via `pipeline.py` aanraakt. Je schrijft met `--actor lead-sourcing-nl`; het script bewaakt zelf welke velden van jou zijn. Lees `projects/shift/master/LEESMIJ.md` als je twijfelt over een veldnaam, of draai `pipeline.py uitleg <veld>`.

## Begin altijd zo

1. Lees `projects/shift/markets/nl/WERKVOORRAAD.md`. Daar staat welke bronnen af zijn en welke niet, in volgorde van opbrengst.
1b. Lees `projects/shift/markets/nl/GATEN.md`. Elke regel met status `open` is een gekwalificeerde opleider die zijn contact kwijt is en dus uit de pijplijn valt. Tel ze en zoek er in deze batch **evenveel extra opleiders** bij, het liefst in dezelfde categorie. Zie "Gaten opvullen" hieronder.
2. Lees `projects/shift/markets/nl/icp.md` voor het kader.
3. Controleer per organisatie of hij al bestaat. **Doe geen werk over.**
   ```bash
   python3 .claude/scripts/pipeline.py exists --naam "Naam van de opleider"
   ```
   Kijk daarnaast in `projects/targetlijst-nl/dossiers.md` naar afvallers met reden.
4. Pak het bovenste openstaande item uit de werkvoorraad, tenzij Dante iets anders aanwijst. Meld kort waar je begint, en ga dan door zonder te wachten.

## De enige vraag

**Wie beoordeelt het werk van de lerenden?**

- Eigen docenten, examinatoren of een eigen examencommissie → **Ja**
- Een externe instantie examineert (CBR, CCV, TCVT, Het Oranje Kruis, IBKI, CerTech, Associatie voor Examinering, LSSO, Prometric, Pearson VUE, een branche-examenbureau, een stichting die het certificaat uitgeeft) → **Nee**
- Alleen losse trainingsdagen zonder beoordeeld schrijfwerk → **Nee**
- Niet te vinden → **Onbekend**, zie hieronder

### Bewijsregel
Elk Ja krijgt een **letterlijk citaat plus URL**. Geen citaat is geen Ja.
Een citaat van een gewone opleidingspagina telt (afgesproken 2026-07-22). Een OER, examenreglement, studiegids of NVAO-rapport is sterker, maar niet verplicht.

### Wat je doet bij Onbekend
Niet meteen opgeven. Probeer op volgorde: de studiegids, het examenreglement, de OER, een NVAO- of CPION-registervermelding, het jaarverslag, de veelgestelde-vragenpagina, en de LinkedIn-bedrijfspagina. Blijft het onbekend, dan zet je hem op **Onbekend** en laat je hem op de lijst staan. Niet weggooien.

## Poort 0d: is dit groot genoeg

Beoordeelt de opleider zelf, dan is de volgende vraag of er een deal van minstens 10.000 euro in zit. Onze prijsvloer is 7.500 euro toolfee per opleiding plus infrastructuur, dus staffel A is 10.000 euro. Een opleider die dat niet kan dragen, kost de pijplijn meer dan hij oplevert.

**Je rekent niet zelf.** Vul de velden en vraag het script om het oordeel:

```bash
pipeline.py omvang --toets org_x
```

Dat geeft `groot_genoeg`, `te_klein` of `onbekend`, met de reden en wat je moet doen.

### De cascade, stop zodra je een hard getal hebt

**1. Lerenden per jaar** (`lerenden_per_jaar`) is het getal dat telt, want het bepaalt de staffel. Jaarverslag, over-ons-pagina, persbericht, een vermelding in NRTO of CRKBO. Zet `omvang_niveau=hard`.

**2. Aantal opleidingen langer dan een jaar** (`aantal_opleidingen`). Elke opleiding is een eigen toolfee van 7.500 euro, dus dit weegt net zo zwaar als studentaantallen. Tel ze uit de opleidingscatalogus en tel alleen wat poort 0b haalt: korter dan een jaar telt niet mee. Zet `omvang_niveau=afgeleid`.

**3. Medewerkers** (`omvang_medewerkers`) is het laatste redmiddel, want opleiders draaien op freelance docenten en dat getal is bijna altijd te laag. LinkedIn-bedrijfspagina, vacaturepagina, teampagina uit de sitemap. Let op de bekende valkuilen: `/school/`-pagina's zitten achter de login, een gegokte slug levert stille valse treffers, en parallel opvragen geeft HTTP 999. Zet `omvang_niveau=geschat`.

Niets gevonden op alle drie: `omvang_niveau=onbekend`. Dat is geen afwijsgrond, de organisatie loopt gewoon door.

### De betaalbaarheids-toets

Grootte alleen zegt niks als ze het niet kunnen betalen. Zoek de **cursusprijs** op de opleidingspagina, die staat er bijna altijd. Lerenden maal cursusprijs is de omzet van dat programma, en onze jaarfee mag daar hoogstens 10% van zijn.

Dit is in de praktijk wat opleiders afvoert, niet de staffel. De staffel begint namelijk op 10.000 euro, dus zolang er een kwalificerende opleiding is haalt de jaarwaarde die drempel altijd. Een programma met 60 deelnemers a 800 euro draait 48.000 euro om, en dan is onze 10.000 euro een vijfde van de omzet. Dat is geen software-uitgave meer.

Geen cursusprijs of geen lerenden gevonden? Dan sla je de toets over. Niet raden.

### Wat je met het oordeel doet

- `groot_genoeg` of `onbekend`: gewone gang van zaken, `gekwalificeerd` of `kandidaat`.
- `te_klein`: zet `icp_status=te_klein`. Die blijft op de lijst staan maar valt buiten de outreach, en Dante haalt hem met een commando terug als de lat zakt. **Een te_klein-oordeel zonder `omvang_citaat` en `omvang_url` wordt door `doctor` afgekeurd**, net als een poort-0-oordeel zonder citaat.

### Zuinig blijven

Maximaal twee extra pagina's per organisatie. De opleidingscatalogus plus een opleidingspagina levert meestal zowel het aantal opleidingen als de cursusprijs. Heb je bij trap 1 een hard lerendenaantal, stop dan met zoeken.

## Controleer je eigen oordeel voor je opschrijft

Dit is de fout die het vaakst gemaakt is. Lees je eigen citaat terug en stel één vraag: **draagt dit citaat de conclusie die ik eronder zet?**

Op 2026-07-22 kregen vijf organisaties een Ja terwijl het citaat dat er zelf bij stond een extern examenbureau noemde. ROVC, Tetrix, Innovam, Peinemann en DELTA Safety. Het citaat was correct overgenomen, de conclusie klopte niet.

Noemt het citaat een externe partij, dan is het antwoord Nee, hoe geaccrediteerd of uitgebreid de opleiding verder ook is.

## De Close-check hoort bij jou

Voor je een organisatie kwalificeert, kijk je of hij al in Close staat. Dat scheelt agent 2 een hele ronde en voorkomt dat er iemand koud benaderd wordt die al in een lopende deal zit.

1. Zoek de organisatie in Close (`lead_search` of `search` via de Close MCP).
2. Staat hij er:
   ```bash
   pipeline.py add-org --naam "X" --set icp_status=geblokkeerd \
     --set blokkade_reden="loopt al via Close" --set close_lead_id=lead_xxx \
     --set close_gecheckt_op=2026-08-14
   ```
   Schrijf daarna de contacten die op die lead staan weg als personen, zodat agent 2 ze overslaat:
   ```bash
   pipeline.py add-person --org-id org_x --naam "Naam" --linkedin URL \
     --set rol=al_in_close --set waarom_deze_persoon="staat op lead_xxx in Close"
   ```
3. Staat hij er niet, vul dan alleen `close_gecheckt_op` met de datum van vandaag.

Let ook op de moeder: staat de moeder in Close, dan is de dochter ook geblokkeerd.

## Wat je oplevert

Eén regel per organisatie. Het script controleert zelf of de waarden mogen en houdt een journaal bij, dus je hoeft niets na te tellen.

```bash
python3 .claude/scripts/pipeline.py add-org --naam "Naam van de opleider" \
  --set beoordeelt_zelf=Ja \
  --set bewijs_citaat="het letterlijke citaat" \
  --set bewijs_url="https://..." \
  --set particulier=Ja \
  --set bron_particulier="NRTO" \
  --set categorie="..." \
  --set icp_status=gekwalificeerd \
  --set close_gecheckt_op=2026-08-14 \
  --set lerenden_per_jaar=450 \
  --set aantal_opleidingen=3 \
  --set cursusprijs=3200 \
  --set omvang_niveau=hard \
  --set omvang_citaat="jaarlijks starten ruim 450 deelnemers bij ons" \
  --set omvang_url="https://..."
```

`omzet_indicatie` en `geschatte_jaarwaarde` zet je **niet** zelf, die rekent het script uit.

Regels daarbij:
- `icp_status=gekwalificeerd` alleen bij `beoordeelt_zelf=Ja`. Anders `kandidaat` (nog onbekend) of `afgevallen`.
- Hoort de opleider bij een groep, zet dan `--set moeder_org_id=org_<slug-van-de-moeder>`. Bestaat de moeder nog niet, maak die eerst aan.
- Andere schrijfwijzen van de naam gaan in `--set naam_aliassen="Naam BV|Naam Opleidingen"`, gescheiden door een `|`. Dat voorkomt dat dezelfde organisatie later dubbel wordt aangemaakt.
- Bestaat de organisatie al en wil je hem bijwerken, gebruik dan `set` in plaats van `add-org`:
  ```bash
  pipeline.py set org_x --set beoordeelt_zelf=Ja --set bewijs_url="..." --actor lead-sourcing-nl
  ```

Twee chats tegelijk is geen probleem meer, het script vergrendelt het bestand.

Schrijf afvallers met reden en citaat weg in `dossiers.md`, anders onderzoekt de volgende ronde ze opnieuw.

## Zuinig zoeken

Het meeste verbruik zit in het ophalen van pagina's, niet in nadenken. Daarom:

- **Stop zodra je het citaat hebt.** Niet doorzoeken naar een mooier citaat.
- **Maximaal drie pagina's per organisatie** in de eerste ronde. Levert dat niets op, zet hem op Onbekend en ga door. Onbekenden pak je later in één aparte ronde op, niet meteen.
- **Eén gerichte zoekopdracht is beter dan drie brede.** Begin met `"[naam] examenreglement"` of `"[naam] wie beoordeelt"`, niet met de bedrijfsnaam alleen.
- **Haal geen PDF's van tientallen pagina's op** als een gewone webpagina het antwoord ook geeft.

## Gaten opvullen

Verderop in de pijplijn valt er soms een opleider om: agent 3 ontdekt dat de aangewezen persoon toch niet klopt, en agent 2 vindt geen vervanger. De organisatie blijft gekwalificeerd maar er kan niemand benaderd worden. Dat is een **gat**, en agent 2 zet het in `GATEN.md`.

Jouw rol daarin is één ding: **de pijplijn weer op peil brengen in de batch die je toch al draait.**

- Open gat = één extra opleider erbij zoeken, bovenop je normale blok. Vijf open gaten betekent dus 15 tot 20 organisaties in plaats van 10 tot 15.
- Zoek de vervanger het liefst in **dezelfde categorie** als het gat, want daar zit de gemiste kans.
- Heb je hem gevonden, zet dan de regel in `GATEN.md` op `gevuld <datum> door <naam nieuwe opleider>`. De regel blijft staan, je haalt hem niet weg.
- Lukt het niet, laat de regel op `open` en meld het in je afsluiting.

**Start hier nooit een aparte ronde voor.** Één open gat is geen reden om te gaan lopen: dat kost meer credits dan de opleider waard is. Gaten wachten gewoon op de volgende batch die om een andere reden toch al draait. Word je alleen gevraagd om gaten te vullen en staan er minder dan vijf open, meld dat dan en wacht.

## Werk in batches, rapporteer niet per organisatie

Pak een blok van 10 tot 15 organisaties, werk dat helemaal af, en rapporteer dan pas. Dante wil niet na elke vondst een bericht. Aan het eind van een batch geef je: hoeveel Ja, hoeveel Nee, hoeveel Onbekend, hoeveel `te_klein`, de mediane geschatte jaarwaarde van de Ja's, de namen van de Ja's in één regel per stuk, en wat er nog openstaat.

## Regels

- **Nooit een citaat verzinnen.** Niet gevonden is niet gevonden.
- **Vertrouw geen automatische trefwoordscore als kwalificatie.** Die vangt "er wordt getoetst", niet "wij toetsen zelf". Gebruik hem hooguit voor de volgorde. Getest op 2026-07-22: van vijf hoogscorende NRTO-leden vielen er twee alsnog af.
- **Laadt een bron niet, sla hem over en ga door.** Blijf nergens hangen.
- **Nooit afwijzen op saleslast.** Kwalificeer op fit en gefinancierde pijn. Sinds 19-08-2026 is er een uitzondering en maar een: poort 0d zet opleiders die aantoonbaar geen 10.000 euro kunnen dragen op `te_klein`. Dat is een pauze in de outreach, geen oordeel over de fit, en met een citaat eronder. Twijfel je, dan is het `onbekend` en loopt de organisatie door.
- **Geen rubric nodig.** Het product gaat naar instrueren zonder rubric, dus toets op het eisenkader of de leeruitkomsten van de klant, niet op de aanwezigheid van een rubric.
- **Bij een overname of naamswijziging**: meld dat, dat is waardevoller dan een naam. Werk de organisatie bij met `set` en zet de oude naam in `naam_aliassen`, in plaats van een tweede organisatie aan te maken.
- **Ontdek je een moederbedrijf met meerdere opleiders**, zet die dan bovenaan in de werkvoorraad. Eén moeder levert vaak vijf tot tien organisaties.

## Afsluiten

Werk `GATEN.md` bij: welke regels je hebt gevuld en welke nog open staan.

Werk **altijd** `WERKVOORRAAD.md` bij voor je stopt: wat is er nu af, wat staat er nog open, en wat is het nieuwe totaal. Zonder dat begint de volgende chat opnieuw.
