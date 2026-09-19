# Meeting-playbook RUG / CIT — 30 juni 2026

_Discovery-meeting. Doel: kwalificeren, de juiste mensen + het beslisproces in kaart brengen, en een logische vervolgstap afspreken. Niet hard pitchen. Discovery is onderzoeken._

---

## 1. Introductie (herschreven + jouw versie eronder)

**Voorstel (strakker, eindigt met een brug naar hen):**

> "Hoi, ik ben Dante Torbed, pilot manager bij Eduface. Even kort over mezelf: naast mijn werk ben ik veel met sport bezig, American football en de gym, zo'n zes keer per week op het veld of in de sportschool. Ons kantoor staat in Utrecht, letterlijk naast de deur bij NPULS en SURF, en we hebben een tweede vestiging in Leiden, waar ik zelf geboren en getogen ben.
>
> Ik ben ruim drieënhalf jaar geleden als eerste bij Eduface gehaald, toen de oprichters net begonnen met bouwen, en ik werk nog steeds nauw met ze samen. Daardoor ken ik onze missie en visie van binnenuit, die laat ik straks in de slides kort zien.
>
> Maar voordat ik iets vertel, hoor ik vooral graag van jullie hoe het er nu bij de RUG voorstaat. Dan maak ik het verhaal straks meteen relevant voor jullie situatie."

**Waarom deze versie werkt:**
- Persoonlijk stuk kort → rapport zonder monoloog.
- NPULS/SURF + Leiden + "eerste medewerker" blijven staan (geloofwaardigheid).
- Eindigt met "eerst hoor ik graag van jullie" = je opent de discovery en komt naast ze te staan, niet erboven.

---

## 2. Discovery-vragen
_Vraag naar proces en geschiedenis, niet naar meningen over collega's. Dan rollen de namen en de politiek er vanzelf uit. Per vraag staat het doel cursief._

**Context / why-now**
1. "Hoe zijn jullie eigenlijk bij ons uitgekomen, en wat maakte dat dit nú relevant werd om te verkennen?" _(hoe gevonden + waarom nu)_
2. "Loopt er al een initiatief waar wij op aanhaken, of zijn we het beginpunt van iets nieuws?" _(waar in het proces zitten we)_

**As-is / de pijn**
3. "Jullie hebben de UG Grader zelf gebouwd, knap. Hoe is dat ontstaan, wie is er nu eigenaar van, en waar houdt het op, bijvoorbeeld bij open geschreven werk en uitgebreide feedback?" _(as-is + eigenaar = enemy + de gap = onze opening; prijs het eerst)_
4. "Je noemde dat faculteiten nu al zelf met AI nakijken, zonder centrale grip. Hoe groot is dat inmiddels, en wat is daar voor jullie het grootste risico?" _(shadow-AI pijn concreet maken)_

**Spelers / beslisproces**
5. "Als jullie dit universiteitsbreed willen aanbieden, hoe loopt zo'n beslissing hier? Wie kijkt mee, en wie hakt uiteindelijk de knoop door?" _(beslisproces + economic buyer)_
6. "Hebben jullie hiervoor een formele opdracht gekregen, en van wie? Wat is de scope?" _(de crux: wie schrijft de aanbeveling = de facto champion / wie is de EB)_
7. "Wie zou er intern overtuigd moeten zijn voordat dit kan, en wie zou er juist kritisch op zijn?" _(champion + enemy, gevraagd als 'wie moet mee', heel normaal)_

**Timing / criteria / gewenste uitkomst**
8. "Is er een moment of deadline waarop dit echt moet draaien? De EU AI Act geldt vanaf augustus 2026 voor AI bij toetsing, speelt dat mee?" _(timing + plant urgentie)_
9. "Waar moet een oplossing aan voldoen om voor jullie te werken? Denk aan privacy/AVG, een eigen LLM, integratie in Brightspace." _(buying criteria, zet onze sterktes als norm)_
10. "Als dit over een jaar precies werkt zoals jullie willen, wat is er dan anders, voor docenten, studenten en bestuur?" _(gewenste uitkomst)_

---

## 3. Cheat sheet voor de slides (ken dit koud)

**Wat Eduface is (positioneer als platform, niet als losse nakijktool)**
- AI-feedback + nakijken op geschreven werk, in de leeromgeving (Brightspace). Uit de data van schrijfopdrachten, presentaties en open tentamenvragen brengen we leerlijnen in kaart → gepersonaliseerd leren.
- **Human-in-the-loop:** de docent verifieert en blijft eindverantwoordelijk. (Sluit aan op RUG's eigen AI-beleid, Rule 8.)

**Bewijs / referenties**
- **Bath Spa University (pilot, juni 2026):** 435 submissions, 6 vakken, 13 markers, 94% nauwkeurigheid (96% in OBM-vakken), reviewtijd 2-3 min. → label als **sectorvalidatie**, niet RUG.
- **Tilburg University:** lopende pilot, NL, open vragen in het LMS. → zeg "we draaien al een pilot bij Tilburg", **geen** afgerond succesverhaal (eerlijk blijven).

**Cost justification (per submissie, RUG vult volume zelf in)**
- Formule: `Huidige kosten = (T/60) × U` · `Besparing = (T × 48% / 60) × U`
- T = 15 min (NL sector-norm, **expliciet zo benoemen**), U = uurkostprijs.
- Academisch (€50/u): huidige kosten **€12,50**/submissie → besparing **€6,00** → resteert €6,50.
- Student-assistent (€22,50/u): **€5,63** → besparing **€2,70**.
- Opschalen: × N (aantal submissies/jaar) — **laat de RUG N invullen.** Vb: €6 × 100.000 = €600.000/jaar.
- 15 min is conservatief; met echte feedback loopt het naar 30-45 min. Het écht accurate getal komt uit een pilot.

**Compliance (jouw sterkste hoek)**
- EU AI Act: AI die leerresultaten beoordeelt = **hoog-risico** (Annex III), verplichtingen vanaf **2 aug 2026**.
- RUG's eigen AI-beleid (dec 2023): Rule 8 = human-in-the-loop verplicht; Rule 6 = verwerkersovereenkomst + AVG. Eduface voldoet 1-op-1.
- Eduface = EU-bedrijf, eigen LLM, EU-gehost, data-soeverein.

**Risico / datalek (de HAN-case)**
- SQL-injectie via één webformulier → ~530.000 mensen (incl. BSN + medische data), 4.381 wachtwoorden plaintext. €165k losgeld geweigerd → data online. **AP-boete €175.000.** Rechter: **€300 p.p.** voor gelekte gevoelige data. AVG-plafond €20M / 4% omzet.
- Koppeling: ongecontroleerd AI-gebruik op studentwerk = exact dezelfde art. 32-blootstelling. **Niet** claimen dat studenten wegbleven (instroom steeg juist).

**Buy-vs-build (hun centrale vraag)**
- UG Grader = handmatige rubric-tool (geen AI-feedback). Exam Analysis = alleen MC. De open-tekst nakijklast ligt nog volledig bij docenten.
- Zelf een AI-nakijksysteem bouwen = nieuw product + volledige EU AI Act-last + structurele kosten, midden in een **€45M-bezuiniging** (Instellingsbegroting 2026).
- RUG koopt al extern in waar dat sneller is (FeedbackFruits). Buy is geen taboe.

**Strategische fit (uit hun eigen stukken)**
- Instellingsbegroting 2026: strategische inzet op **"AI en digitale soevereiniteit"**. Eduface past daar exact in.
- FEB noemt zelf "bezuinigingen (bijv. inzet AI)"; GMW zoekt "minder arbeidsintensieve vormen". Jij levert dat instrument.

**Wie is wie (in je hoofd, niet hardop)**
- Tessa = coach/ingang · Reinard van Dalen (haar manager) = champion-kandidaat/pivot · van der Duim = beslist build-vs-buy · Tipping-Griffioen = CIO/EB · Vera Hommes = privacy/security-gate (te winnen als ally).

---

## 4. Afsluitende vraag 1 — ruimte voor vragen

> "Dat was het verhaal van mijn kant. Voordat we het over een vervolg hebben: **zijn er vragen, of dingen die ik nog kan verduidelijken?**"

_Luister hier goed. Wie nu "ja maar wij kunnen dit zelf" zegt = je enemy. Wie doorvraagt op resultaten/compliance = je champion of fan._

---

## 5. Afsluitende vraag 2 — voorstel logische vervolgstap

> "Een logische vervolgstap lijkt me een **korte, afgebakende pilot bij één schrijfintensieve faculteit**, bijvoorbeeld Rechten of Letteren. Dan meten we op jullie eigen opdrachten de werkelijke nakijktijd en nauwkeurigheid, lossen we meteen een stuk van het ongecontroleerde gebruik gecontroleerd op, en hebben jullie harde cijfers voor de bredere afweging. **Zouden jullie daarvoor openstaan, en wie zou daar dan bij betrokken moeten zijn?**"

_Doel: commitment op een concrete next step + de beslisser/privacy-persoon aan tafel krijgen. Na de meeting: bevestigingsmail met pijn + spelers + why-now + vervolgstap = de Discovery-gate is dan door._

---

_Bronnen voor alle cijfers: zie dossier-cost-justification-en-datalek.md en de ROI-analyse in deze map._
