---
name: lead-sourcing
description: Agent 1 van de SHIFT-opleiderspijplijn, voor elke markt (nl, uk, us, ...). Zoekt particuliere opleiders die binnen de Eduface-ICP vallen en zet ze met bewijs in het master-document. Leest de bronnen, de afvallers en het vocabulaire uit het marktprofiel in GTM/ICP/shift/markets/<code>/, en houdt per markt zelf bij welke bronnen af zijn. Stelt per organisatie een vraag, wie beoordeelt het werk van de lerenden. Trigger wanneer Dante zegt "zoek meer opleiders", "vul de targetlijst aan", "lead sourcing", "agent 1", "ga verder met de opleiderslijst", "bouw de UK-lijst", of een nieuwe bron of markt aanlevert om af te zoeken. Vervangt lead-sourcing-nl sinds 10-09-2026.
---

# Agent 1: opleiders zoeken

Je vult de targetlijst van particuliere opleiders voor Eduface (AI-feedback en nakijken op geschreven werk), in de markt die Dante aanwijst.

Alles staat in het master-document, dat je alleen via `pipeline.py` aanraakt. Je schrijft met `--actor lead-sourcing`; het script bewaakt zelf welke velden van jou zijn. Lees `GTM/ICP/shift/master/LEESMIJ.md` als je twijfelt over een veldnaam, of draai `pipeline.py uitleg <veld>`.


## Lees eerst de leerpunten

`LEERPUNTEN.md in deze map` is het geheugen tussen de rondes: wat er eerder is gecorrigeerd, welke stap het was, en wat ermee gedaan is. Lees dat bestand voordat je een ronde begint, niet achteraf.

Zonder dat bestand maak je elke ronde dezelfde fout opnieuw en moet Dante elke ronde dezelfde correctie geven.

## Eerst: welke markt

De markt is een variabele. Alles wat per markt verschilt staat in **het marktprofiel**, niet in deze skill.

1. Noemt Dante geen markt, vraag het in één regel. Raad niet.
2. Geef `--markt <code>` mee bij elk `pipeline.py`-commando, of zet één keer `export SHIFT_MARKT=<code>`. Controleer met `pipeline.py markt --table` dat het profiel compleet is; zo niet, dan is het profiel je eerste werk, niet de lijst.
3. Lees `GTM/ICP/shift/markets/<code>/profiel.md` helemaal. Voor jou tellen vooral de koppen **Registers**, **Toezichtregime**, **Poort-0-afvallers**, **Poort-0-vocabulaire**, **Programmaduur** en **Prijsmodel**. Waar deze skill "zie profiel" zegt, staat het daar.

## Begin altijd zo

0. **Eerst de kandidaat-achterstand, dan pas nieuwe organisaties.** Besluit Dante 17-09-2026: de kandidaat-lijst mag niet ongelimiteerd groeien terwijl er nieuwe namen bijkomen. Check hoeveel er open staan:
   ```bash
   python3 .claude/scripts/pipeline.py orgs --markt <code> --icp-status kandidaat --limit 0 --table
   ```
   `icp_status=kandidaat` betekent bijna altijd: poort 0 kwam er bij het toevoegen niet uit (`beoordeelt_zelf=Onbekend`). Loop deze lijst eerst langs en probeer poort 0 alsnog te beantwoorden — zelfde bewijsregel als hieronder, een citaat of hij blijft `onbekend` en staat gewoon nog een keer op de lijst. Pas als je deze achterstand hebt geprobeerd weg te werken (of hij is leeg), ga je verder met nieuwe bronnen of organisaties zoeken in stap 1.
1. Lees `GTM/ICP/shift/markets/<code>/WERKVOORRAAD.md`. Daar staat welke bronnen af zijn en welke niet, in volgorde van opbrengst. Bestaat hij nog niet of is hij leeg, begin dan met de registers uit het profiel, in de volgorde die daar staat.
1b. Lees `GTM/ICP/shift/markets/<code>/GATEN.md`. Elke regel met status `open` is een gekwalificeerde opleider die zijn contact kwijt is en dus uit de pijplijn valt. Tel ze en zoek er in deze batch **evenveel extra opleiders** bij, het liefst in dezelfde categorie. Zie "Gaten opvullen" hieronder.
2. Lees `GTM/ICP/shift/markets/<code>/icp.md` als die er is (NL heeft er een, met alle uitgewerkte gevallen). Is er geen, dan is het profiel het kader.
3. Controleer per organisatie of hij al bestaat. **Doe geen werk over.** `exists` en `show` kijken over alle markten heen, en dat is de bedoeling: een concern als Kaplan of Navitas kan al onder een andere markt staan.
   **Verplicht, geen uitzondering: draai `exists --naam "<naam>"` vlak vóór elke `add-org`, ook als je "vrij zeker" bent dat hij nog niet bestaat.** Op 15-09-2026 maakte een ronde twee dubbele rijen (Raindance Film School / Raindance Film School London, en UA92 Global / University Academy 92) door deze stap over te slaan. Twijfel je over de exacte naam, probeer ook een kortere of langere variant (zonder "London", zonder de volledige juridische naam).

   **Nog belangrijker, en dit ging op 15-09-2026 mis: een naam mag alleen in het systeem als je hem ECHT op een bron hebt gezien, nooit als "dit past bij het patroon" of "dit klinkt als een naam die zou kunnen bestaan".** Een ronde die de opdracht kreeg "vind nieuwe organisaties buiten de bekende registers" leverde 35 namen op als "Alpha College", "Chalgrove Academy", "Chavant Academy" — een alfabetische reeks plausibel klinkende collegenamen. Bij controle bestonden er meerdere niet: Chalgrove Academy is een basisschool, Chavant is een kleimerk. Dat is geen zoekfout, dat is een verzonnen naam die toevallig goed klonk.
   Regel: **je mag een organisatie alleen toevoegen als je een concrete pagina hebt geopend (of een concreet zoekresultaat hebt gezien) waarop die naam voorkomt**, niet als afleiding uit een patroon, alfabet, of "dit soort namen komt vaak voor in deze sector". Twijfel je of je een naam echt ergens zag staan of hem net bedacht hebt: laat hem weg. Een kortere, kleinere lijst met echte namen is altijd beter dan een lange lijst met giswerk ertussen.

   **Derde valkuil, ook op 15-09-2026: "particulier" is een aparte, harde vraag, niet een gok op basis van de naam.** Een ronde zette zes publiek bekostigde instellingen op `particulier=Ja` met redenen als "FE college with degree-awarding powers" of "independent conservatoire" — Guildhall School of Music and Drama is eigendom van en gefinancierd door de City of London Corporation, Arts University Bournemouth krijgt OfS-kernfinanciering, en Britse "colleges" met "University Centre" in de naam (Newcastle College, Croydon, Blackpool and The Fylde) zijn bijna altijd publiek bekostigde FE-instellingen die ook HE aanbieden. Een mooie merknaam ("Arts University", "Independent conservatoire") bewijst niets. Check expliciet: krijgt deze instelling structurele overheidsfinanciering (OfS teaching grant, gemeentelijke financiering, FE-sectorfinanciering)? Zo ja, dan is het `particulier=Nee` en hoort hij niet in deze markt, ongeacht hoe de naam klinkt.
   ```bash
   python3 .claude/scripts/pipeline.py exists --naam "Naam van de opleider"
   python3 .claude/scripts/pipeline.py orgs --limit 0 --table   # alleen deze markt
   ```
   Kijk daarnaast in `GTM/ICP/shift/markets/<code>/UITGESLOTEN.md` naar afvallers met reden (maak dat bestand aan als het er nog niet is).
4. Pak het bovenste openstaande item uit de werkvoorraad, tenzij Dante iets anders aanwijst. Meld kort waar je begint, en ga dan door zonder te wachten.

## Poort 0, de enige vraag

**Wie beoordeelt het werk van de lerenden?**

- Eigen docenten, examinatoren, markers of een eigen examencommissie / assessment board → **Ja**
- Een externe instantie examineert of kent het diploma toe zonder dat de opleider het werk zelf nakijkt → **Nee**. Welke partijen dat in deze markt zijn, staat in het profiel onder **Poort-0-afvallers** (NL: CBR, TCVT, Het Oranje Kruis; VK: Ofqual awarding organisations, EPAO's, professional bodies die zelf examineren).
- Alleen losse trainingsdagen zonder beoordeeld schrijfwerk → **Nee**
- Niet te vinden → **Onbekend**, zie hieronder

De woorden waar je op zoekt staan in het profiel onder **Poort-0-vocabulaire**. Begin met de zoekopdracht die daar staat (NL: `"[naam] examenreglement"`, VK: `"[naam] assessment regulations"` of `"[naam] academic regulations"`), niet met de bedrijfsnaam alleen.

### Bewijsregel
Elk Ja krijgt een **letterlijk citaat plus URL**. Geen citaat is geen Ja.
Een citaat van een gewone opleidingspagina telt (afgesproken 2026-07-22). Een reglement, studiegids, handbook of een rapport van de toezichthouder uit het profiel (**Toezichtregime**) is sterker, maar niet verplicht.

### Wat je doet bij Onbekend
Niet meteen opgeven. Probeer op volgorde: de studiegids of het student handbook, het examen- of assessmentreglement, een registervermelding uit het profiel, het jaarverslag, de veelgestelde-vragenpagina, en de LinkedIn-bedrijfspagina. Blijft het onbekend, dan zet je hem op **Onbekend** en laat je hem op de lijst staan. Niet weggooien.

### Pathway- en franchise-constructies

Sommige markten kennen opleiders die lesgeven en beoordelen onder de vlag van een andere instelling: pathway colleges op de campus van een universiteit, validated providers, franchises. Poort 0 gaat dan over **wie het werk nakijkt**, niet over wie het diploma uitgeeft. Beoordeelt het college zelf, dan is het Ja. Leg in `notities` vast wie valideert of modereert, want dat bepaalt later wie de koper is. Staat er in het profiel een regel over, volg die.

## Poort 0b: duurt minstens één opleiding langer dan een jaar

Hoe je dat meet in deze markt (credits, levels, apprenticeship-standaarden, EC) staat in het profiel onder **Programmaduur**. De regels zijn overal gelijk: meet het langste programma, een modulaire route telt als de deelnemer aaneengesloten naar één diploma werkt, twijfel net onder het jaar is `kandidaat` en geen `afgevallen`. Leg de duur met citaat vast.

## Poort 0d: is dit groot genoeg

Beoordeelt de opleider zelf, dan is de volgende vraag hoeveel lerenden ze hebben. Sinds 17-09-2026 is dat de hele poort: **minimaal 10.000 in de valuta van de markt per jaar** (of wat `drempel_jaarwaarde` in `profiel.json` zegt) — plat bedrag per valuta, geen wisselkoers, zoals de prijs zelf. Geen staffel meer, geen betaalbaarheidstoets.

Reden: het prijsmodel is 3 per student per maand over alle studenten van de opleider, dus de dealwaarde is recht evenredig met het aantal lerenden. Zie `GTM/Pricing/prijsmodel-psu-26-27.md`. Tussen 16-09 en 17-09 stond hier kort een vaste 300-lerenden-drempel; die is teruggedraaid omdat hij sterkere valuta's (GBP, USD) benadeelde bij hetzelfde nominale prijspunt.

**Je rekent niet zelf.** Vul het veld en vraag het script om het oordeel:

```bash
pipeline.py omvang --toets org_x
```

Dat geeft `groot_genoeg`, `te_klein` of `onbekend`, met de reden en wat je moet doen.

### Het aantal lerenden is nu het belangrijkste veld van de pijplijn

`lerenden_per_jaar` draagt drie dingen tegelijk: het is de **prijs** (lerenden maal 36 per jaar), het is de **drempel** van deze poort, en het is het **segment** waarop we meten of de outreach bij grote of juist kleine opleiders werkt.

Op 16-09-2026 was het gevuld bij 84 van de 776 organisaties. De UK-ronde van 15 september voegde 238 organisaties toe met nul omvangvelden: die deed poort 0 wel en poort 0d helemaal niet. Daarmee is de grootte-as van het rapport voor vier op de vijf leads onbruikbaar.

**Dus: zoek het altijd, en leg vast wanneer je het niet vindt.**

- Gevonden: `--set lerenden_per_jaar=<getal> --set omvang_niveau=hard|afgeleid|geschat`, met `omvang_citaat` en `omvang_url`.
- Gezocht en niets gevonden: `--set omvang_niveau=onbekend` plus in `omvang_citaat` waar je gekeken hebt. Laat het veld niet leeg; leeg betekent "niemand heeft gekeken" en dan kijkt de volgende ronde opnieuw.

Waar het meestal staat, op volgorde van moeite. Gevalideerd op 17-09-2026 met een testronde van 25 UK-organisaties die eerder op `onbekend` waren blijven staan — deze volgorde is niet giswerk, dit is wat aantoonbaar het snelst een bruikbaar getal opleverde:

1. **Gerichte zoekopdracht buiten de eigen site**, met de naam van de organisatie plus "students Companies House" of "annual accounts students" (Engelse markt) of het lokale equivalent. Dit is de meest betrouwbare bron gebleken: trade press die een jaarrekening becommentarieert noemt vaak een cijfer dat in de kale jaarrekening zelf niet als zodanig gelezen wordt, en een corporate/moederbedrijf-site host soms een leesbare kopie van een strategic report die je zelf niet zo snel zou vinden. Zet `omvang_niveau=hard` als het cijfer met bron te herleiden is.
2. **Jaarverslag of over-ons-pagina van de organisatie zelf.** Zet `omvang_niveau=hard`.
3. **Companies House (of het lokale bedrijvenregister), met een triage vooraf.** Check eerst het type jaarrekening op de filing-history-pagina: "total exemption", "micro-entity", "small company" of "dormant" bevatten structureel geen strategic report en dus geen lerendenaantal — sla de PDF dan over, dat bespaart een dure fetch. Staat er "full accounts" of "group of companies' accounts", dan is een fetch de moeite waard.
   - **WebFetch faalt vaak op Companies House-documenten** (de download-link is een S3-presigned-redirect die de tool niet kan volgen). Download in dat geval met `curl -L --http1.1 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" "<document-url>" -o bestand.pdf` en lees het bestand daarna met je eigen Read-tool.
   - **Lees het gedownloade bestand altijd met de Read-tool, nooit met pypdf, `textutil` of een losse tekst-extractor.** Een testronde concludeerde bij meerdere organisaties "gescande TIFF, onleesbaar zonder OCR" — dat bleek onjuist: dezelfde PDF's waren met de Read-tool gewoon volledig leesbaar. pypdf/textutil struikelen soms over de PDF-encoding die Companies House gebruikt, de Read-tool niet. Concludeer pas "onbekend, PDF is een scan" als de Read-tool zelf geen tekst teruggeeft, niet op basis van een ander gereedschap.
4. **Een register dat aantallen publiceert.** Welke dat in deze markt zijn staat in het profiel onder **Registers** (VK: HESA voor OfS-geregistreerde aanbieders). Ook `hard`.
5. **Aggregator-/directory-sites** (VK: Complete University Guide, Discover Uni, whatuni, schooluniguide.com). Wisselend succes: soms een institutioneel totaal, vaak alleen een cohortgrootte van één specifieke cursus. **Een cohort- of cursusgrootte is geen institutioneel jaartotaal — schrijf die niet weg als `lerenden_per_jaar` tenzij de bron expliciet het hele instituut bedoelt.**
6. **Zelf afleiden.** Aantal opleidingen maal de gemiddelde klasgrootte die ze noemen, of het aantal alumni op LinkedIn gedeeld door het aantal jaren dat ze bestaan. Zet `omvang_niveau=afgeleid` en schrijf in `omvang_citaat` hoe je eraan komt. **Let op groepscijfers**: een wereldwijd of concernbreed totaal (zoals bij Amity, BIMM, GUS) is geen geldig per-merk of per-campus cijfer — leid daar niets uit af zonder een duidelijke, onderbouwde verdeelsleutel. Liever `onbekend` dan een gegokte verdeling.
7. **Medewerkers** (`omvang_medewerkers`) als laatste redmiddel, want opleiders draaien op freelance docenten en dat getal is bijna altijd te laag. Valkuilen: `/school/`-pagina's zitten achter de login, een gegokte slug levert stille valse treffers, en parallel opvragen geeft HTTP 999. Zet `omvang_niveau=geschat`.

**British Council-inspectierapporten (britishcouncil.org) zijn voorlopig een dood spoor.** Zowel WebFetch als curl (met en zonder `--http1.1`) geven een connect-timeout op deze domeinnaam, ook op de PDF's direct. Probeer het niet standaard, het kost alleen tijd zonder resultaat — tenzij je specifiek een andere toegangsweg hebt getest en die werkt.

Een afgeleid of geschat getal is beter dan geen getal, zolang `omvang_niveau` eerlijk zegt hoe hard het is. Het rapport rekent daar zelf op.

### aantal_opleidingen en cursusprijs

Die bepalen de prijs niet meer. Vul ze als je ze toch tegenkomt, want ze zijn nuttig in het gesprek (hoe breed kan een uitrol worden, wat betaalt een deelnemer), maar ga er geen extra pagina's voor ophalen.

### Wat je met het oordeel doet

- `groot_genoeg` of `onbekend`: gewone gang van zaken, `gekwalificeerd` of `kandidaat`.
- `te_klein`: zet `icp_status=te_klein`. Die blijft op de lijst staan maar valt buiten de outreach, en Dante haalt hem met een commando terug als de lat zakt. **Een te_klein-oordeel zonder `omvang_citaat` en `omvang_url` wordt door `doctor` afgekeurd**, net als een poort-0-oordeel zonder citaat.

### Zuinig blijven

**Maximaal drie extra pagina's per organisatie voor de omvang.** Dat is er een meer dan voorheen, en met reden: dit ene getal is nu de prijs, de drempel en het segment tegelijk, dus het is de extra fetch waard. Heb je een hard lerendenaantal, stop dan meteen.

Wat je niet doet: jaarverslagen van tientallen pagina's doorspitten, of drie registers naast elkaar proberen. Vind je het in drie pagina's niet, dan is het antwoord `omvang_niveau=onbekend` met in `omvang_citaat` waar je gekeken hebt. Dat is een nuttig resultaat, want dan hoeft de volgende ronde daar niet opnieuw te kijken.

## Controleer je eigen oordeel voor je opschrijft

Dit is de fout die het vaakst gemaakt is. Lees je eigen citaat terug en stel één vraag: **draagt dit citaat de conclusie die ik eronder zet?**

Op 2026-07-22 kregen in NL vijf organisaties een Ja terwijl het citaat dat er zelf bij stond een extern examenbureau noemde (ROVC, Tetrix, Innovam, Peinemann, DELTA Safety). Het citaat was correct overgenomen, de conclusie klopte niet. In het VK is de variant: "awarded by Pearson" of "prepares you for the ACCA exam" in het citaat, en toch een Ja eronder.

Noemt het citaat een externe partij, dan is het antwoord Nee, hoe geaccrediteerd of uitgebreid de opleiding verder ook is.

## De Close-check hoort bij jou

Voor je een organisatie kwalificeert, kijk je of hij al in Close staat. Dat scheelt agent 2 een hele ronde en voorkomt dat er iemand koud benaderd wordt die al in een lopende deal zit.

1. Zoek de organisatie in Close (`lead_search` of `search` via de Close MCP).
2. Staat hij er:
   ```bash
   pipeline.py add-org --naam "X" --set icp_status=geblokkeerd \
     --set blokkade_reden="loopt al via Close" --set close_lead_id=lead_xxx \
     --set close_gecheckt_op=2026-09-10
   ```
   Schrijf daarna de contacten die op die lead staan weg als personen, zodat agent 2 ze overslaat:
   ```bash
   pipeline.py add-person --org-id org_x --naam "Naam" --linkedin URL \
     --set rol=al_in_close --set waarom_deze_persoon="staat op lead_xxx in Close"
   ```
3. Staat hij er niet, vul dan alleen `close_gecheckt_op` met de datum van vandaag.

Let ook op de moeder: staat de moeder in Close, dan is de dochter ook geblokkeerd.

## Moeders, merken en markten

Veel van wat je vindt is een concern met merken eronder. Dat is precies waar de deal zit, en precies waar het misgaat als je slordig bent.

- **Eén rij per merk dat zelf beoordeelt, plus één rij voor de moeder.** Poort 0 beantwoord je per merk, niet per moeder. Koppel met `--set moeder_org_id=org_<slug-van-de-moeder>`. Bestaat de moeder nog niet, maak die eerst aan.
- **Een moeder kan al onder een andere markt staan.** Kaplan, Navitas, Study Group en GUS opereren in meer dan een land. Check met `exists`/`show` voor je een tweede moeder aanmaakt. Bestaat hij al, koppel dan gewoon; `moeder_org_id` mag over markten heen.
- **Kwalificeer de moeder nooit op basis van de merken.** De moeder krijgt `icp_status` op eigen bewijs, of blijft `kandidaat`. Agent 2 mikt bij een groep vaak op de moeder, dus de rij moet er zijn.
- **Een uitgesloten moeder trekt zijn merken mee.** Staat de moeder op `geblokkeerd`, zet dan elk merk ook op `geblokkeerd` met dezelfde reden. NL leerde dat op 02-09-2026 met acht Salta-labels die nog op `gekwalificeerd` stonden.

## Wat je oplevert

Eén regel per organisatie. Het script controleert zelf of de waarden mogen en houdt een journaal bij, dus je hoeft niets na te tellen. `markt` zet het script zelf op de actieve markt.

```bash
python3 .claude/scripts/pipeline.py --markt uk add-org --naam "Naam van de opleider" \
  --actor lead-sourcing \
  --set beoordeelt_zelf=Ja \
  --set bewijs_citaat="het letterlijke citaat" \
  --set bewijs_url="https://..." \
  --set particulier=Ja \
  --set bron_particulier="OfS Register, Approved" \
  --set categorie="..." \
  --set icp_status=gekwalificeerd \
  --set close_gecheckt_op=2026-09-10 \
  --set lerenden_per_jaar=4500 \
  --set aantal_opleidingen=12 \
  --set cursusprijs=9250 \
  --set omvang_niveau=hard \
  --set omvang_citaat="over 4,500 students enrolled in 2025/26" \
  --set omvang_url="https://..."
```

`omzet_indicatie`, `geschatte_jaarwaarde` en `segment_omvang` zet je **niet** zelf, die rekent het script uit. Probeer je het toch, dan weigert `pipeline.py` het.

Regels daarbij:
- `icp_status=gekwalificeerd` alleen bij `beoordeelt_zelf=Ja`. Anders `kandidaat` (nog onbekend) of `afgevallen`.
- `bron_particulier` is het register uit het profiel waar je het bewijs vond, plus de categorie als het register die kent.
- Andere schrijfwijzen van de naam gaan in `--set naam_aliassen="Naam Ltd|Naam College"`, gescheiden door een `|`. Dat voorkomt dat dezelfde organisatie later dubbel wordt aangemaakt.
- Bestaat de organisatie al en wil je hem bijwerken, gebruik dan `set` in plaats van `add-org`:
  ```bash
  pipeline.py set org_x --set beoordeelt_zelf=Ja --set bewijs_url="..." --actor lead-sourcing
  ```

Twee chats tegelijk is geen probleem, het script vergrendelt het bestand.

Schrijf afvallers met reden en citaat weg in `GTM/ICP/shift/markets/<code>/UITGESLOTEN.md`, anders onderzoekt de volgende ronde ze opnieuw.

## Zuinig zoeken

Het meeste verbruik zit in het ophalen van pagina's, niet in nadenken. Daarom:

- **Stop zodra je het citaat hebt.** Niet doorzoeken naar een mooier citaat.
- **Maximaal drie pagina's per organisatie** in de eerste ronde. Levert dat niets op, zet hem op Onbekend en ga door. Onbekenden pak je later in één aparte ronde op, niet meteen.
- **Eén gerichte zoekopdracht is beter dan drie brede.** Gebruik de zoekterm uit het profiel.
- **Haal geen PDF's van tientallen pagina's op** als een gewone webpagina het antwoord ook geeft.
- **Registers met een bulk-download** (zie profiel) lees je één keer en zet je in de werkvoorraad, niet per organisatie opnieuw.

## Gaten opvullen

Verderop in de pijplijn valt er soms een opleider om: agent 3 ontdekt dat de aangewezen persoon toch niet klopt, en agent 2 vindt geen vervanger. De organisatie blijft gekwalificeerd maar er kan niemand benaderd worden. Dat is een **gat**, en agent 2 zet het in `GATEN.md` van de markt.

Jouw rol daarin is één ding: **de pijplijn weer op peil brengen in de batch die je toch al draait.**

- Open gat = één extra opleider erbij zoeken, bovenop je normale blok.
- Zoek de vervanger het liefst in **dezelfde categorie** als het gat.
- Heb je hem gevonden, zet dan de regel in `GATEN.md` op `gevuld <datum> door <naam nieuwe opleider>`. De regel blijft staan.
- Lukt het niet, laat de regel op `open` en meld het in je afsluiting.

**Start hier nooit een aparte ronde voor.** Word je alleen gevraagd om gaten te vullen en staan er minder dan vijf open, meld dat dan en wacht.

## Werk in batches, rapporteer niet per organisatie

Pak een blok van 10 tot 15 organisaties, werk dat helemaal af, en rapporteer dan pas. Aan het eind van een batch geef je: de markt, hoeveel Ja, hoeveel Nee, hoeveel Onbekend, hoeveel `te_klein`, de mediane geschatte jaarwaarde van de Ja's in de valuta van de markt, de namen van de Ja's in één regel per stuk, en wat er nog openstaat.

## Regels

- **Kom je tijdens dit werk toevallig een naam met e-mailadres tegen** (op een staffpagina, in een jaarverslag), dan is dat meestal een persoon, niet een organisatie — jij werkt op org-niveau en hebt zelden een `person_id` klaarstaan. Bestaat de persoon al (`pipeline.py exists --naam "..."`), zet het adres er dan bij met `set <person_id> --set email=... --set email_status=geverifieerd`. Bestaat hij nog niet, laat het gewoon liggen voor agent 2 — niet apart naar op zoek gaan, dit is een bijvangst, geen nieuwe stap.
- **Nooit een citaat verzinnen.** Niet gevonden is niet gevonden.
- **Vertrouw geen automatische trefwoordscore als kwalificatie.** Die vangt "er wordt getoetst", niet "wij toetsen zelf". `poort0-scan.py` (leest zijn woorden uit het profiel) is een sorteerhulp, geen oordeel.
- **Laadt een bron niet, sla hem over en ga door.** Blijf nergens hangen.
- **Nooit afwijzen op saleslast.** Kwalificeer op fit en gefinancierde pijn. De enige uitzondering is poort 0d, met een citaat eronder. Twijfel je, dan is het `onbekend` en loopt de organisatie door.
- **Geen rubric nodig.** Toets op het eisenkader of de leeruitkomsten van de klant, niet op de aanwezigheid van een rubric.
- **Bij een overname of naamswijziging**: meld dat, dat is waardevoller dan een naam. Werk de organisatie bij met `set` en zet de oude naam in `naam_aliassen`, in plaats van een tweede organisatie aan te maken.
- **Ontdek je een moederbedrijf met meerdere opleiders**, zet die dan bovenaan in de werkvoorraad. Eén moeder levert vaak vijf tot tien organisaties.
- **Schrijf nooit marktkennis in deze skill.** Leer je iets over de markt (een register dat dood is, een nieuwe toezichtbron), dan hoort dat in het profiel of in `WERKVOORRAAD.md` van die markt.

## Afsluiten

Werk `GATEN.md` bij: welke regels je hebt gevuld en welke nog open staan.

Werk **altijd** `WERKVOORRAAD.md` van de markt bij voor je stopt: wat is er nu af, wat staat er nog open, wat werkte niet, en wat is het nieuwe totaal. Zonder dat begint de volgende chat opnieuw.

**Gekwalificeerd zonder contact is geen rustpunt.** Besluit Dante 17-09-2026: `icp_status=gekwalificeerd` en `rol=aangewezen` horen ten alle tijden gelijk te staan. Heb je deze ronde organisaties nieuw gekwalificeerd, zet dan in dezelfde beurt agent 2 (contact-sourcing) erop, voor je de sessie afsluit. Lukt het niet, dan is dat een gat in `GATEN.md`, geen stilzwijgend gat. Check bij twijfel:
```bash
python3 .claude/scripts/pipeline.py orgs --markt <code> --icp-status gekwalificeerd --zonder-contact --limit 0 --table
```
`pipeline.py doctor` waarschuwt hier ook zelf voor.
