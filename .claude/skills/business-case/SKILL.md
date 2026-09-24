---
name: business-case
description: Bouwt per deal de business case op, in twee standen. Stand 1 (standaard) haalt alles op wat er over de klant bekend is (Close, meeting-transcripts, Gmail, de accountmap), bepaalt in welke fase de deal zit, toont ALLE gaten voor de business case, beoordeelt de kwaliteit van elke metric, en schrijft per gat een klant-specifieke vraag met timing (nu of later, en waarom) en wie het antwoord waarschijnlijk heeft. Stand 2 schrijft de business case zelf, ALLEEN als Dante letterlijk zegt "maak een business case" of iets gelijkwaardigs. Trigger stand 1 bij "wat mis ik nog voor de business case", "welke vragen moet ik stellen voor de business case", "business case vragen voor [account]", "waar staan we met de business case", "check de metrics van [account]", of een transcript met de vraag wat er nog ontbreekt. Trigger stand 2 bij "maak een business case", "schrijf de business case voor [account]".
---

# Business case

Het doel: per deal een business case die de instelling zelf als intern document kan gebruiken (handboek Step 5), opgebouwd over meerdere gesprekken heen. De meeste runs maken **nog geen** business case. Ze laten zien wat er ontbreekt en wat Dante in het volgende gesprek moet vragen.

**Lees eerst `LEERPUNTEN.md` in deze map.** Daar staat de feedback van eerdere runs. Lees daarna `reference.md` voor de blokken, de fase-matrix, de metric-ladder, wie wat weet, de risico-antwoorden en de M1's.

## Stand 1: gaten en vragen (standaard)

### Stap 1. Alles ophalen, geen bron overslaan
1. **Accountmap** `GTM/Accounts/<slug>/`: lees de README, eerdere `business-case-gaten.md` en onderzoek. Geen map? Maak er een aan met de naam van de instelling.
2. **Close:** `fetch_lead`, `find_opportunities` (fase, waarde), `activity_search` (mails, notities, taken).
3. **Meetings:** draai `python3 .claude/skills/deal-status-update/scripts/close_meetings.py <lead_id>` voor de samenvattingen en user notes. Is er een transcript, haal het op met `fetch_meeting_transcript` en bewaar het met `GTM/sales-coach/scripts/save_transcript.py`. **Lees het hele transcript**, niet de samenvatting.
4. **Gmail:** `search_threads` op het domein van de instelling en de namen van de contacten.
5. Heeft Dante een transcript of notitie geplakt, dan is dat de eerste bron.

Zuinig: ophalen stopt zodra de bron niets nieuws meer oplevert. Webonderzoek alleen voor blok 3 (hun strategische prioriteiten), en maximaal drie pagina's.

### Stap 2. Fase bepalen
Leg het bewijs naast de gates uit `GTM/Knowledge/sales-handbook-v1.md`, niet naast de fase in Close. Staat Close verder dan het bewijs toelaat, dan meld je dat. Benoem ook **met wie** Dante praat: rol, en of het een coach, champion of EB is.

### Stap 3. Alle gaten tonen
Loop de vijf blokken plus het risicoblok uit `reference.md` door. Per onderdeel: **wat we weten** (met bron en datum) of **gat**. Toon altijd alle gaten, ook de gaten die pas later aan de beurt zijn.

### Stap 4. Metric-oordeel
Per metric die we hebben: de stand op de ladder, waar hij vandaan komt (hun eigen data, hun schatting, of ons sectorcijfer), en **één zin over wat hem sterker maakt**. Bijvoorbeeld: "Goed dat we 15 minuten per paper hebben, maar het is hun schatting. Vraag of hun workload-model een norm per opdracht heeft, dan wordt het hun eigen cijfer."

### Stap 5. Vragen
Per gat één vraag, met:
- **timing:** `nu` of `later`, met de reden (fase, gevoelig, de verkeerde persoon, eerst vertrouwen nodig)
- **wie weet het:** deze persoon, of welke rol of afdeling (zie `reference.md`). Heeft de gesprekspartner het niet, geef dan ook de doorvraag: "Bij wie zou ik dat kunnen vinden, en zou jij dat voor ons kunnen opvragen?"
- **anker:** het citaat of feit uit de bron waar de vraag op leunt

Vorm en toon: volg `question-builder` (de vijf toetsen, ankeren, geen ja/nee-vragen). Schrijf zoals Dante praat: neem zijn eigen formuleringen uit de transcripts over als voorbeeld.

**Kanaal: mail vooraf of live.** Per gat bepaal ik het kanaal.
- **Mail vooraf** voor feiten die iemand moet opzoeken: volumes, tijden, kosten, bestaande data. Doel: ze komen voorbereid, en de meeting gaat over hun cijfers in plaats van over het ophalen ervan.
  - Direct en concreet, zodat ze het in één keer kunnen opzoeken of doorsturen: "Hoeveel schriftelijke opdrachten kijken jullie per jaar na binnen de opleiding?"
  - Per vraag in een halve zin waarom je het vraagt, zodat ze het juiste cijfer pakken.
  - Genummerd, in een mail die kort blijft.
  - Weten ze het zelf niet, dan zeg je bij wie het vermoedelijk ligt: "dit staat mogelijk in jullie taakbelastingsmodel".
- **Live in de meeting** voor pijn, prioriteit, oorzaak, en alles wat gevoelig is. Vorm volgens `question-builder`: open vraag, anker, doorvragen, kantelen.
- **Het mailantwoord wordt het anker in de meeting:** "Je noemde zo'n 4.000 opdrachten per jaar. Hoe landt dat bij het team in de piekweken?"
- Budget, wie tekent en tegenstanders gaan nooit per mail.

**Hoeveel vragen: geen vast maximum.** Het aantal volgt uit de situatie, niet uit een getal. Weeg de fase van de deal en hoe warm deze persoon is: uit het transcript of de mails (reageert snel en uitgebreid, deelt zelf cijfers, stelt zelf vragen, of juist kort en afwachtend). Een warme champion in scoping kan veel hebben, een koele eerste kennismaking weinig. Je hoeft niet alles tegelijk te vragen. Zeg in één zin waarom je voor dit aantal kiest.

**Taal.** Alles wat ik tegen Dante zeg, inclusief uitleg, labels en toelichting, is in de taal waarin hij schrijft, standaard Nederlands. Alleen de letterlijke vragen die hij aan de prospect stelt of mailt zijn in de taal van dat gesprek: Nederlands bij een Nederlandse prospect, Engels alleen als het gesprek met de prospect in het Engels gaat.

### Stap 6. Wegschrijven
Werk `GTM/Accounts/<slug>/business-case-gaten.md` bij (format in `reference.md`), met een datum bovenaan. In de chat: de fase, de top 3 gaten, en de vragen voor het volgende gesprek. Niet het hele bestand plakken.

## Stand 2: de business case maken

Alleen op expliciet verzoek. Schrijf `GTM/Accounts/<slug>/business-case.md` vanuit het perspectief van de instelling, alsof zij het zelf geschreven hebben. Gebruik het template in `reference.md`.
- Elk getal heeft een bron. Sectorcijfers en M1's worden gelabeld als sector of referentie, nooit als hun cijfer.
- Het risicoblok gebruikt alleen claims uit `Platform/product.md`. Ontbreekt een antwoord, dan zet je er `[OPEN: navragen bij Menno]` neer.
- De prijs komt uit `GTM/Pricing/prijsmodel-psu-26-27.md`, nooit uit het hoofd.
- Onder de business case een lijst met wat nog zwak of open is. Een gat vul je niet op met iets dat aannemelijk klinkt.

## Feedback verwerken (altijd, ongevraagd)

Geeft Dante feedback op een run, dan schrijf ik die **dezelfde beurt** in `LEERPUNTEN.md`, bij de schakel waar het misging. Dat meld ik in één regel. Komt dezelfde feedback een tweede keer, dan leg ik de regeltekst voor die ik in deze SKILL.md of in `reference.md` wil zetten. Pas na zijn akkoord pas ik de skill aan. Zie `.claude/rules/feedback.md`.

## Wat deze skill niet doet
- Niets terugschrijven naar Close. Dat doet `deal-status-update`.
- De deal niet scoren op MEDDPICC. Dat doet `meddpicc`, of `sales-coach` review.
- Geen compliance-claim die niet in `Platform/product.md` staat.
