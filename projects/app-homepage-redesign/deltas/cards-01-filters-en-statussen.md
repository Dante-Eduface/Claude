# Delta cards-01 op de bouwprompt cards

Aanvulling op `bouwprompt-cards.md`. **Alleen wat hieronder staat verandert.** Alles wat er niet in staat blijft precies zoals het in die prompt staat.

Vier wijzigingen, plus een aantal vastgelegde antwoorden die je niet opnieuw hoeft te stellen.

---

## Wijziging 1: de scope is de docent-omgeving

Er bestaan **twee** Enterprise-omgevingen: een admin-omgeving voor de instelling, en deze docent-omgeving. Alles wat beheer is hoort in de admin-omgeving, niet hier.

Dat is geen detail: het verklaart waarom een aantal voor de hand liggende functies bewust ontbreken op dit scherm. Verzin ze er niet bij.

---

## Wijziging 2: de statuslijst gaat van vijf naar drie

**Weg: `Setup incomplete`.** Een cursus of opdracht heeft op dit scherm geen inrichtingsstaat die de docent moet oplossen. Er is geen setup, dus bouw er ook geen label voor.

**Weg: `No assignments yet`.** Laat die situatie vanzelf onder `No submissions yet` vallen, want een cursus zonder opdrachten heeft ook nooit een inzending gehad. Dat klopt feitelijk en scheelt een label.

**Wat overblijft**, precedentie van boven naar beneden, de eerste die past wint:

| Situatie | Voorwaarde | Waar op de card | Klik |
|---|---|---|---|
| `Archived` | de cursus is gearchiveerd | markering rechtsboven, getallen blijven gewoon staan | geen |
| `No submissions yet` | er is nog nooit iets ingeleverd in deze cursus | vervangt de getallen | geen |
| `Completed ✓` | alle deadlines voorbij én er wacht niets meer | markering rechtsboven, getallen tonen `0` en `–` | geen |
| geen markering | alle overige, de cursus loopt gewoon | getallen | geen |

De regel achter die tabel blijft ongewijzigd: heeft de card een getal, dan toont hij het getal. Kan er geen getal zijn, dan zegt hij waarom niet. Een markering rechtsboven is een eigenschap van een verder normale cursus, een vervangende regel is een reden dat er niets te tellen valt.

Op de **opdracht-card** blijven alleen `No submissions yet` en `Completed ✓` over.

---

## Wijziging 3: onderwijsniveau gaat van de card af

Zone 1 wordt alleen de cursusnaam, plus de markering rechtsboven als die geldt. Verder niets.

Het niveau blijft wel bestaan en wordt nog steeds gezet in Manage rubric, want het stuurt de toon en het niveau van de feedback. Het staat alleen niet meer op de card, omdat het niet verandert op welke cursus je gaat handelen.

---

## Wijziging 4: zoeken en filteren

Nieuwe sectie, hieronder in zijn geheel.

### De balk staat er altijd

Vanaf één cursus. Geen drempel op het aantal cards, geen versie met en zonder.

Waarom dit expliciet in de opdracht staat: een balk die bij 25 cursussen verschijnt en bij 24 weer weg is, is een interface die verandert zonder dat de gebruiker iets deed. Dat breekt zijn mentale model precies zoals beschreven in het werk over automation surprise (Sarter, Woods & Billings), en het raakt een handeling die door de omgeving getriggerd wordt in plaats van door een afweging: je grijpt naar de plek waar de filter altijd zat. Een scherm dat soms wel en soms geen controls heeft is bovendien de gevaarlijkste variant, bijna-hetzelfde, waar de foutkans juist stijgt met ervaring.

Een drempel is hier ook niet eenduidig te definiëren: telt hij het totaal of de gefilterde stand? Bij de gefilterde stand verdwijnt de balk terwijl je hem gebruikt.

**Twee gevolgen, want het is dezelfde fout op kleinere schaal:**

- Geen enkele filteroptie wordt verborgen of uitgezet omdat hij nul oplevert. `Completed (0)` blijft staan en blijft aanklikbaar. Dat nul is informatie.
- De regel met `12 of 34 courses` staat er altijd, niet alleen wanneer er gefilterd is.

**De enige uitzondering is geen drempel maar een ander scherm:** bij nul cursussen is er geen raster maar een lege staat, en daar hoort geen filterbalk omdat er niets te filteren valt.

### Wat er in de balk komt

Vier dingen, in deze volgorde van links naar rechts. Meer niet.

**1. Zoeken.** Zoekt op cursusnaam en opdrachtnaam. De placeholder zegt wat hij doorzoekt, dus `Search courses and assignments`, niet `Search...`. Sneltoets `/` zet de cursor erin.

**2. Status.** Exact dezelfde begrippen als op de card. Eén vocabulaire door het hele scherm, dus geen aparte filternamen verzinnen:

`Needs grading` · `No submissions yet` · `Completed` · `Archived`

Zet in het uitklapmenu het aantal achter elke optie. Daarmee is de filter zelf meteen een samenvatting van het account. Zet die aantallen niet op de gesloten knop, dan wordt het een metric-balk en dat is het niet.

**3. Waiting.** Banden op de hoofdmetriek: `Any` · `Over 3 days` · `Over 7 days` · `Over 14 days`. Dit is de enige filter die direct op urgentie snijdt, en urgentie is waar dit product over gaat.

**4. Overdue only.** Een schakelaar, geen uitklapmenu. Aan betekent: alleen cursussen waarvan het oudste wachtende werk voorbij de deadline van zijn eigen opdracht ligt. Dat is een feit van de instelling, geen drempel die wij verzinnen.

Archived zit in de statusfilter, dus de losse archief-schakelaar kan weg.

### Hoe de controls zich gedragen

- **De knop toont zijn eigen stand**, dus `Status: All` en `Status: Needs grading`.
- **Een actief filter valt op met rand en gewicht, niet met een kleurvlak.** Groen is hier verboden: dit is geen bevestigde positieve status en al helemaal geen "klik hier". Inactief wordt niet weggedempt met grijs.
- **Filters staan links, sorteren staat rechts.** Filteren snijdt weg, sorteren rangschikt. Niet in dezelfde groep zetten.
- **Toon altijd hoeveel er overblijft**, met `Clear filters` ernaast zodra er iets aanstaat.
- **Lege uitkomst is een ontworpen staat.** Geen leeg raster, maar één regel die zegt welke filters actief zijn en één knop om ze te wissen.
- **Filters resetten per sessie, de sorteerkeuze blijft bewaard.** Een filter is een tijdelijke versmalling, een sortering is een voorkeur. Wie volgende week terugkomt in een gefilterd dashboard denkt dat er werk verdwenen is.
- **Zet de filterstand in de URL**, zodat een gefilterd overzicht door te sturen is.

### Wat er bewust niet in zit

- **Favorites.** Met acht cursussen markeer je niets, en met tweehonderd wil je niet je favorieten maar je eigen werk.
- **Tags en Creators.** Bestaan niet in ons datamodel, dus verzinnen we niet.
- **Education level als filter.** Verandert niet op welke cursus je gaat handelen.

---

## Vastgelegde antwoorden, niet opnieuw vragen

- **Het toewijzen van een nakijker aan een opdracht** gebeurt in de admin-omgeving van Enterprise, niet hier. Dus geen `Mine / Everyone`-filter op dit scherm.
- **Er bestaat geen niveau boven de cursus**, dus geen opleiding-, programma- of afdelingsfilter.
- **Semester en collegejaar** bestaan wel als begrip, maar die data vragen we niet uit en halen we niet uit het LMS. Dus daar kun je niet op filteren en bouw je er niets voor.

---

## Wat expliciet blijft zoals het is

Alles uit `bouwprompt-cards.md` dat hierboven niet wordt genoemd. In het bijzonder:

- De gedeelde definitie: een inzending wacht zolang de docent hem niet heeft goedgekeurd, en `to grade`, `oldest waiting` en `Completed` volgen daar alledrie uit.
- De drie zones van de card, en dat `to grade` het grootste getal is na de naam.
- De strikte voorwaarde voor `Completed` en de drie kleurregels voor groen.
- Weg met de voortgangsring, met `12/32 graded` en met `✓ All graded` in het groen.
- De standaardvolgorde van het raster als rangschikking, en de zichtbare uitleg daarvan.
- De twee varianten achter de schakelaar, A zonder meter en B met een urgentiemeter.
- Archiveren blijft op de card en verschijnt zichtbaar in de voet van een `Completed`-card. Verwijderen gaat van de card af naar de cursusinstellingen, met een bevestiging die meeschaalt met wat er verloren gaat.

## Lever op

Het bijgewerkte bestand, plus drie regels over wat je hebt gewijzigd en waar je van deze delta bent afgeweken.
