# Business case: referentie

Bronnen waar dit op leunt: `GTM/Knowledge/sales-handbook-v1.md` (Step 5), `GTM/Knowledge/meddpicc-states-and-gates.md` (Metrics en Identify Pain), MEDDICC M1/M2/M3. Staat hier iets dat die bronnen tegenspreekt, dan winnen de bronnen.

## M1, M2, M3

- **M1**: een resultaat bij een bestaande klant. Zie de M1-bank onderaan.
- **M2**: die M1 doorgerekend met de cijfers van deze klant. Dit is wat stand 1 opbouwt.
- **M3**: de M2 na go-live, als KPI. Is die gehaald, dan komt hij als nieuwe M1 in de bank.

## De blokken en wat we per blok moeten weten

| Blok | Wat we moeten weten | Minimaal voor een eerste concept |
|---|---|---|
| **1. Probleem** | De pijn in hun woorden, de oorzaak (proces, systemen, mensen), wat er recent veranderde, of het één opleiding is of de hele instelling | Eén letterlijk citaat plus de oorzaak |
| **2. As-is in cijfers** | Studenten of lerenden in scope, inzendingen per jaar, minuten per inzending, wie nakijkt en tegen welke kosten, doorlooptijd van feedback, herbeoordelingen en bezwaren, huidige feedbackscores (NSS, NSE), wat ze nu al uitgeven aan tools of inhuur | Volume, minuten per inzending, aantal nakijkers |
| **3. Hun prioriteiten** | Instellingsplan of strategie, onderwijsvisie, werkdruk-afspraken, accreditatie (NVAO, OfS, QQI), KPI's van de EB | Eén prioriteit uit hun eigen document, met link |
| **4. To-be plus kostenonderbouwing** | Verwachte minuten per inzending, doorlooptijd, scope jaar 1, waar de vrijgekomen tijd naartoe gaat, wat het oplevert tegenover licentie plus implementatie | Bespaarde uren × uurkosten tegenover de prijs. Onder ongeveer 3x de kosten is het geen sterke case |
| **5. Waarom nu** | Deadline: semester- of blokstart, accreditatie, begrotingsronde, contract van een concurrent dat afloopt. Wie tekent en wanneer het budgetbesluit valt | Eén datum met bron |
| **R. Risico's en ons antwoord** | Wat hen tegenhoudt: AI Act, GDPR/AVG, dataopslag, acceptatie door docenten, academische integriteit, LMS-koppeling, vendor lock-in | Hun grootste zorg, in hun woorden |

## Fase-matrix: wat vraag je wanneer

Fases volgen het handboek. "Later" betekent: toon het gat, maar zet de vraag op later.

| Fase | Nu vragen | Later, en waarom |
|---|---|---|
| **Discovery (Step 1)** | Blok 1 helemaal. Blok 2 grof (volume, wie nakijkt). Blok 3 alleen als ze het zelf aansnijden. De grootste zorg (R). | Uurkosten, budget, wie tekent: te vroeg, dan klinkt het als een verkoopgesprek. Precieze minuten: eerst het probleem erkennen. |
| **Scoping (Step 2)** | Blok 2 precies. Blok 4 samen schatten. Blok 5 (waarom nu). R uitdiepen. | EB en budget alleen via de champion, niet rechtstreeks aan een coach. |
| **EB-meeting (Step 3)** | Niets meer uitvragen, alles moet dan al bekend zijn. Wel: prioriteit, of er budget is als de POV slaagt, wie er nog meer tekent. | |
| **POV (Step 4)** | De as-is en to-be cijfers opnieuw bevestigen. Het bewijs vastleggen tegen dezelfde cijfers. | |
| **Business case (Step 5)** | Validatie door de champion: "klopt dit, kun je dit intern gebruiken?" | |

**Gevoelig, altijd indirect** (formuleringen in `.claude/skills/question-builder/reference.md`): budget ("if"), besluitvorming (vraag naar gewoontes, niet naar bevoegdheid), tegenstanders (vraag om hulp bij een bezwaar), uurkosten van personeel (vraag naar het workload-model, niet naar salarissen).

## Metric-ladder (kwaliteit)

Uit `meddpicc-states-and-gates.md`:

`UNKNOWN` → `CURRENT STATE` (as-is uit hun eigen data) → `TARGET STATE` (kostenonderbouwing, bevestigd door de champion) → `POV VALIDATED` → `EB AGREED` → `INSTITUTION OWNED`

Per metric beoordeel je ook de **herkomst**, van zwak naar sterk:
1. ons sectorcijfer (bijvoorbeeld 15 minuten per paper uit Saxion of Kingston)
2. hun schatting, mondeling
3. hun schatting, op papier of in een mail
4. hun eigen data: workload-model, roosters, LMS-export, NSS
5. gemeten in de POV

Regel: een cijfer dat niet uit hun eigen data komt, telt niet hoger dan `CURRENT STATE`.

Typische manieren om een metric sterker te maken:
- **Kwantificeren:** "veel werk" wordt "hoeveel uur per blok, bij hoeveel docenten"
- **Herkomst omhoog:** van een schatting naar hun workload-model of een LMS-export
- **Tijdsbasis erbij:** per opdracht, per blok, per jaar
- **Doorrekenen naar geld of capaciteit:** uren × uurkosten, of het aantal fte dat vrijkomt
- **Aan hun prioriteit koppelen:** van "tijd" naar "de werkdruk-afspraak uit hun cao" of "de NSS-score op assessment and feedback"

## Wie weet wat

Standaardvermoeden. Het transcript of Close wint altijd.

| Informatie | NL | UK / IE |
|---|---|---|
| Volumes, inzendingen, vakken | opleidingsmanager, onderwijsbureau, LMS-beheer | programme leader, registry, learning technologist |
| Minuten per opdracht, taakbelasting | teamleider, het taakbelastingsmodel (HR/P&O) | head of department, workload allocation model |
| Uurkosten, inhuur, student-assistenten | controller, afdeling financiën | faculty finance business partner |
| Kwaliteit en consistentie van beoordelen | examencommissie, toetscommissie, kwaliteitszorg | external examiners, quality office, academic registrar |
| Feedbackscores | kwaliteitszorg (NSE) | planning, NSS-team |
| Strategie en KPI's van de EB | instellingsplan, bestuursverslag | strategic plan, annual report |
| Privacy, DPIA, verwerkersovereenkomst | FG/DPO, privacy officer, IT-security | DPO, information governance |
| Budget en wie tekent | faculteitsdirecteur, CvB | PVC Education, COO, procurement |

## Risico-antwoorden (alleen uit `Platform/product.md`)

| Zorg | Wat we mogen zeggen | Wat nog open is |
|---|---|---|
| **AI Act** | Eduface voldoet aan de AI Act. Audit trail die voldoet aan de AI Act, voor alle summatieve beoordelingen. De docent keurt goed, de AI assisteert. | Welke risicoklasse en welke documentatie we kunnen overleggen: navragen bij Menno. |
| **GDPR** | Voldoet aan de UK GDPR. Studentdata gaat nooit naar externe AI-aanbieders. Geen training op hun data. De instelling blijft eigenaar. Versleuteld tijdens transport, doelgebonden verwerking, bewaartermijn volgens afspraak. | EU-GDPR en AVG staan niet expliciet in `product.md`. Ook DPIA, verwerkersovereenkomst en hostinglocatie niet. Tot dat er staat: `[OPEN: navragen bij Menno]`. |
| **Docenten verliezen de regie** | "The AI assists. The academic decides." De instelling kiest hoeveel menselijk toezicht er is. Het grader comparison dashboard laat afwijkingen tussen beoordelaars zien. | |
| **Kwaliteit van het cijfer** | Bath Spa: gemiddeld ongeveer 6 punten van het docentcijfer af, en ongeveer 2 punten bij docenten die het model hadden afgestemd. Zes vakmodellen, geen generiek model. | Of het docentcijfer voor of na het AI-voorstel is vastgesteld: nog niet uitgezocht. Pas in een business case zetten als Menno of Samuel het bevestigd heeft. |
| **LMS** | Integreert met hun LMS, cijfer terug naar het gradebook. | Noem alleen hún LMS, som nooit alle koppelingen op. |

Nieuwe zorg die hier niet staat: vraag het na, beweer het niet. Komt het antwoord binnen, dan wordt het eerst in `Platform/product.md` gezet en daarna hier.

## M1-bank

Label een M1 altijd als referentie of sectorcijfer, nooit als hun cijfer.

| M1 | Cijfers | Bron | Let op |
|---|---|---|---|
| **Bath Spa University, pilot juni 2026** | 435 inzendingen, 6 vakken, 13 nakijkers. Reviewtijd 2 tot 3 minuten per inzending. Gemiddeld 94% accuraatheid (ongeveer 6 punten van het docentcijfer af), 98% bij docenten die het model hadden afgestemd, 96% in de OBM-vakken. | `Platform/product.md`, `GTM/Accounts/rug-groningen/meeting-playbook-30-juni.md` | Het opdrachttype en de onafhankelijkheid van de meting zijn nog niet uitgezocht. Accuraatheid is geen overeenstemmingspercentage. Een voormeting van de nakijktijd ontbreekt. |
| **Sectoranker nakijktijd (geen klant)** | 15 minuten per inzending (range 10 tot 20). NL: Saxion, Hogeschool Rotterdam. UK: Kingston 20 minuten, Reading 30 minuten per essay. | `GTM/Accounts/rug-groningen/dossier-cost-justification-en-datalek.md` | Sectorcijfer. Vervangen door hun eigen cijfer zodra dat er is. |

**Gat in de bank:** er is nog geen klant met een gemeten voor- en na-meting van de nakijktijd, of met een resultaat in geld of fte. Leg dat vanaf nu bij elke implementatie vast (M3).

## Format `business-case-gaten.md`

```
# Business case: <instelling>
_Laatst bijgewerkt: JJJJ-MM-DD. Bronnen: <welke transcripts, mails, Close-items>._

**Fase:** <fase volgens bewijs> (Close zegt: <fase>)
**Gesprekspartner(s):** <naam, rol, coach/champion/EB>

## Wat we weten en wat ontbreekt
### 1. Probleem
- ✓ <feit> (bron, datum)
- ✗ GAT: <wat ontbreekt>
... blok 2 t/m 5 en R

## Metrics
| Metric | Waarde | Herkomst | Ladder | Sterker door |

## Vragen voor het volgende gesprek
_Aantal: <één zin waarom dit aantal, op basis van fase en hoe warm de persoon is>._

### Mail vooraf (genummerd, kort)
1. <directe vraag> , <halve zin waarom> , <bij wie het vermoedelijk ligt>

### Live in de meeting
**[nu]** <vraag in de spreektaal van het gesprek>
  gat: <welk gat dit dicht>
  anker: <citaat of feit, bron>
  wie weet het: <persoon, of rol/afdeling> , doorvraag als hij het niet heeft
  door: <doorvraaglaag>

**[later: <reden>]** <vraag>
  ...
```

## Template stand 2: `business-case.md`

Geschreven als de instelling, in hun taal. Volgorde uit het handboek:

1. Samenvatting (als laatste schrijven, maximaal vijf zinnen)
2. Onze doelen en strategische initiatieven
3. Het probleem, en hoe het die initiatieven tegenhoudt
4. Huidige situatie in cijfers
5. Voor en na: use-case-scenario's
6. Kostenonderbouwing (as-is tegenover to-be, in hun termen: uren, fte, doorlooptijd, feedbackscores)
7. Risico's en hoe die gedekt zijn
8. Implementatieplan met data: module live op A, faculteiten geïnformeerd op B, eerste opdracht nagekeken op C, resultaat op D, dus contract rond op E
9. Wat we meten na go-live (de M3's)

Daaronder, apart en voor Dante: **wat nog zwak of open is**.
