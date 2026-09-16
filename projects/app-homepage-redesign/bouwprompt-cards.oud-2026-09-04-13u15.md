# Bouwprompt: cards voor cursussen en opdrachten

Plak dit als geheel. Het is zelfstandig leesbaar.

**Dit vervangt `bouwprompt-cursusrij.md` en `delta-01`.** Die gingen over een tabel met rijen. Die opzet is losgelaten: het overzicht wordt cards. Wat uit dat werk blijft gelden staat onderaan, wat vervalt ook.

**Scope: de docent-omgeving van Enterprise.** Er bestaan twee Enterprise-omgevingen: een admin-omgeving voor de instelling en deze docent-omgeving. Alles wat beheer is hoort in de admin-omgeving, niet hier. Instellingen zetten accounts uit bij hun docenten. Alles wat specifiek is voor zelf-aanmeldende gebruikers valt buiten deze opdracht. De lege staat voor een gloednieuw account laat je ongemoeid.

---

## 1. Begin hier: één gedeelde definitie

Alles op een card steunt op één begrip. Definieer dat één keer en gebruik het overal, anders krijg je vakjes die elkaar tegenspreken.

**Een inzending wacht zolang de docent hem niet heeft goedgekeurd.**

Dus: ingeleverd door de student, en nog niet afgetekend. Een inzending waarvan de AI de feedback al klaar heeft maar die de docent nog niet heeft bekeken, **wacht nog steeds**. Dat volgt uit hoe het product werkt: de student ziet pas iets nadat de docent het heeft goedgekeurd.

Daaruit volgt:

- **To grade** = aantal wachtende inzendingen.
- **Oldest waiting** = de oudste daarvan, gemeten vanaf het moment dat de student inleverde.
- **Completed** = er wacht niets meer, en er kan niets meer bij komen.

---

## 2. Wat er verandert nu het cards worden

Vier dingen die in een tabel gratis waren en op een card betaald moeten worden. Dit is de kern van deze opdracht.

**Een card heeft geen kolomkop, dus elk getal draagt zijn eigen label.** In een tabel doet de kop dat werk één keer voor de hele kolom. Op een card betaal je het per card. Gevolg: minder getallen per card, en elk getal met een woord ernaast. Op de huidige card staat onderaan `1 day ago` zonder label. Dat kan van alles zijn, laatste inzending of laatste keer dat jij nakeek.

**De volgorde van het raster ís de rangschikking.** In een tabel klik je op een kolomkop om te sorteren. In een raster is er niets om op te klikken, dus de standaardvolgorde moet zelf het antwoord zijn op "waar moet ik nu heen". Zie punt 5.

**Cards maken vergelijken moeilijker, en dat is de prijs die je betaalt.** Een tabel laat je met je oog één kolom aflopen. Een raster niet. NN/g deelt tabelgebruik op in drie taken: iets specifieks vinden, records vergelijken, en handelen op een record ([Data Tables, NN/g](https://www.nngroup.com/articles/data-tables/)). Cards zijn goed in de eerste en de derde, slechter in de tweede. Compenseer dat met de volgorde, niet met meer vulling per card.

**Eén feit, één weergave.** Op de huidige card staat dezelfde informatie drie keer: de ring, `12/32 graded`, en `20 to grade`. 32 min 12 is 20. Dat is één feit in drie coderingen. In ons systeem staat "herhaalde metric-boxjes waar één samengesteld verband duidelijker was" op de lijst waaraan je sjabloonwerk herkent.

---

## 3. Wat er van de huidige card af moet, en waarom

- **De voortgangsring.** Hij codeert proportie, en proportie is niet de beslissing. De docent vraagt zich af hoeveel er nog ligt en hoe dringend, niet hoe ver hij procentueel is. De ring trekt het meeste gewicht naar het minst bruikbare getal. Als je toch een visuele vergelijker over het raster wilt, moet die urgentie coderen en geen voortgang, want anders geef je mensen precies de verkeerde vergelijking terug. Zie de variant in punt 8.
- **`12/32 graded`.** Weg. `20 to grade` is het getal waar iemand naar handelt. De noemer hoort op de cursuspagina, niet op de card.
- **De lege ring bij `No submissions yet`.** Een voortgangsring op nul leest als nul procent gedaan, dus als achterstand. Er is niets ingeleverd, er ís geen voortgang om te tonen. Teken geen voortgangsindicator voor een toestand die geen voortgang heeft.
- **`✓ All graded` in het groen.** Dit is de belangrijkste correctie van deze opdracht. Zie punt 4.
- **De ondertitel `View and manage your courses`.** Die zegt niets. Weg, of vervang hem door iets dat werk doet, bijvoorbeeld de uitleg van de sorteervolgorde uit punt 5.

---

## 4. `All graded` is niet hetzelfde als `Completed`

Nu kleurt de card groen zodra er niets meer te beoordelen is. Dat is fout, en het is precies de val die we eerder hebben dichtgezet.

**Nul te beoordelen zegt vandaag niets, want morgen levert er iemand in.** Een groen label dat de volgende dag weer uit gaat is ruis. Een toestand die kan terugflippen kun je geen afrondingsbetekenis geven.

**De juiste voorwaarde voor `Completed`, alle drie tegelijk:**

1. de cursus heeft minstens één opdracht,
2. van elke opdracht ligt de deadline in het verleden, en
3. er wacht geen enkele inzending meer.

**Randgevallen:**

- Een opdracht zonder inzendingen blokkeert het afronden niet. Anders rondt een cursus nooit af zodra één student nooit inlevert, en dat is juist het normale geval.
- Heeft de hele cursus nul inzendingen, dan wint `No submissions yet` van `Completed`. "Afgerond" zeggen terwijl er nooit iets is gebeurd, is misleidend.
- Een te late inzending zet `Completed` weer uit. Dat is correct, er ligt dan weer werk. Dit is een uitzondering, geen dagelijks ritme.
- "Deadline in het verleden" beoordeel je tegen de tijdzone van de instelling, niet die van de browser.

**Kleur.** Dit is de enige plek op de card waar groen mag. Ons `core/regels.md` staat groen toe op een bevestigde positieve status in een tool: klaar, goedgekeurd, loopt op schema. Drie voorwaarden uit diezelfde regel:

1. Tekstkleur is `green-deep #007b54`, niet de felle `#00e075`. Die heeft als tekst op wit te weinig contrast en werkt alleen als vlak.
2. Het vinkje staat er altijd bij. Naast kleur hoort een signaal dat geen kleur is.
3. Kleur codeert een toestand, geen mening. Bij de strikte voorwaarde is `Completed` een feit. Bij `to grade = 0` zou het onze mening zijn dat nul gunstig is, en dat valt onder het verbod op groen omdat een waarde goed uitkomt.

---

## 5. De cursus-card

Drie zones. Meer niet.

**Zone 1, identiteit**
- Cursusnaam, de grootste tekst op de card. Verder niets.
- Rechtsboven: `Archived` of `Completed ✓` als die gelden. Zie de statuslijst.

Onderwijsniveau komt **niet** op de card. Het wordt nog steeds gezet in Manage rubric, want het stuurt de toon en het niveau van de feedback, maar het verandert niet op welke cursus je gaat handelen en het is dus geen kaartinhoud.

**Zone 2, status**
Hier staat óf wat er wacht, óf waarom er niets kan wachten. Nooit allebei.

Wachten er inzendingen, dan twee getallen met een woord erbij:

```
20            12 days ⚠
to grade      oldest waiting
```

Het aantal is het grootste getal op de card na de naam. De wachttijd staat ernaast, iets kleiner. Het waarschuwingsteken verschijnt alleen als het oudste wachtende werk voorbij de deadline van zijn eigen opdracht ligt. Dat is een feit van de instelling, geen drempel die wij verzinnen.

Kan er niets wachten, dan één regel die zegt waarom:

- `No submissions yet`

Dat is de enige, en hij is niet klikbaar. Een cursus zonder opdrachten valt hier vanzelf onder, want dan is er ook nooit iets ingeleverd.

**Zone 3, voet**
`Last submission 1 day ago`, met het label erbij. Is er nooit iets ingeleverd, laat de voet dan leeg in plaats van een streepje zonder betekenis.

### De statuslijst, precedentie van boven naar beneden

| Situatie | Voorwaarde | Waar op de card | Klik |
|---|---|---|---|
| `Archived` | de cursus is gearchiveerd | markering rechtsboven, getallen blijven gewoon staan | geen |
| `No submissions yet` | er is nog nooit iets ingeleverd in deze cursus | vervangt de getallen | geen |
| `Completed ✓` | zie punt 4 | markering rechtsboven, getallen tonen `0` en `–` | geen |
| geen markering | alle overige, de cursus loopt gewoon | getallen | geen |

**De regel achter die tabel:** heeft de card een getal, dan toont hij het getal. Kan er geen getal zijn, dan zegt hij waarom niet. Een markering rechtsboven is een eigenschap van een verder normale cursus, een vervangende regel is een reden dat er niets te tellen valt.

**Er is geen setup-status op dit scherm.** Een cursus of opdracht heeft hier geen inrichtingsstaat die de docent moet oplossen, dus bouw er ook geen label voor.

---

## 6. De opdracht-card

Zelfde drie zones, met één verschil dat er echt toe doet: **een opdracht heeft wél een eigen deadline.** Op de cursus was elke deadline afgeleid, hier is hij echt. Gebruik hem.

**Zone 1** Opdrachtnaam groot. Daaronder de cursusnaam, tenzij je al binnen die cursus zit, dan laat je hem weg.

**Zone 2** Zelfde twee getallen, `to grade` en `oldest waiting`, met dezelfde regels.

**Zone 3** `Due 12 Sep` met daaronder `in 3 days` of `5 days ago`. Dit heet hier gewoon `Due`, niet `Next due`, want hij is van deze opdracht zelf.

Statussen: `No submissions yet` en `Completed ✓`. Meer niet.

---

## 7. Het raster

**De standaardvolgorde is het belangrijkste ontwerpbesluit op deze pagina**, want er is geen kolomkop om op te sorteren.

Sorteer op: eerst de cursussen waar iets wacht, daarbinnen op `oldest waiting` aflopend, daarna op `to grade` aflopend. Cursussen zonder wachtend werk komen daarna. `Archived` altijd onderaan, of verborgen achter de bestaande schakelaar.

Zet er één regel bij zodat de volgorde niet als willekeur leest, bijvoorbeeld `Sorted by longest waiting`. Dat is meteen een betere ondertitel dan `View and manage your courses`.

Geef daarnaast een simpele sorteerkeuze: langst wachtend, meeste te beoordelen, laatst actief, naam. Meer smaken zijn niet nodig.

---

## 8. Bouw twee varianten

Eén schakelaar, één verschil, verder alles identiek. Anders zegt de vergelijking niets.

**Variant A, alleen typografie.** Geen ring, geen balk. De twee getallen doen het werk, hiërarchie met grootte en gewicht.

**Variant B, één urgentiemeter.** Zelfde card, plus een dunne horizontale balk onderin die **urgentie** codeert en niet voortgang: hoe langer het oudste werk wacht ten opzichte van de deadline van zijn opdracht, hoe verder gevuld. Voorbij de deadline kleurt hij `danger #b3261e`, daarvoor navy. Geen deadline bekend, geen balk.

De schakelaar is tijdelijk gereedschap, klein, buiten het raster, met de tekst `Variant A / B`. Hij gaat eruit zodra de keuze valt.

---

## 9. Zoeken en filteren

### De balk staat er altijd

Vanaf één cursus. Geen drempel op het aantal cards, geen versie met en zonder.

Waarom dit expliciet in de opdracht staat: een balk die bij 25 cursussen verschijnt en bij 24 weer weg is, is een interface die verandert zonder dat de gebruiker iets deed. Dat breekt zijn mentale model precies zoals beschreven in het werk over automation surprise (Sarter, Woods & Billings), en het raakt een handeling die door de omgeving getriggerd wordt in plaats van door een afweging: je grijpt naar de plek waar de filter altijd zat. Een scherm dat soms wel en soms geen controls heeft is bovendien de gevaarlijkste variant, bijna-hetzelfde, waar de foutkans juist stijgt met ervaring.

Een drempel is hier ook niet eens eenduidig te definiëren: telt hij het totaal of de gefilterde stand? Bij de gefilterde stand verdwijnt de balk terwijl je hem gebruikt.

Bij weinig cursussen werkt de balk trouwens gewoon: met de aantallen in het uitklapmenu is de statusfilter ook bij drie cursussen een samenvatting van het account.

**Twee gevolgen, want het is dezelfde fout op kleinere schaal:**

- Geen enkele filteroptie wordt verborgen of uitgezet omdat hij nul oplevert. `Completed (0)` blijft staan en blijft aanklikbaar. Dat nul is informatie.
- De regel met `12 of 34 courses` staat er altijd, niet alleen wanneer er gefilterd is.

**De enige uitzondering is geen drempel maar een ander scherm:** bij nul cursussen is er geen raster maar een lege staat, en daar hoort geen filterbalk omdat er niets te filteren valt.

### Wat er in de balk komt

Vier dingen, in deze volgorde van links naar rechts. Meer niet.

**1. Zoeken.** Zoekt op cursusnaam en opdrachtnaam. De placeholder zegt wat hij doorzoekt, dus `Search courses and assignments`, niet `Search...`. Sneltoets `/` zet de cursor erin.

**2. Status.** Exact dezelfde begrippen als de statuslijst op de card. Eén vocabulaire door het hele scherm, dus geen aparte filternamen verzinnen:

`Needs grading` · `No submissions yet` · `Completed` · `Archived`

Zet in het uitklapmenu het aantal achter elke optie, dus `No submissions yet (2)`. Daarmee is de filter zelf meteen een samenvatting van het account: je ziet zonder klikken dat er twee cursussen niet zijn ingericht. Zet die aantallen niet op de gesloten knop, dan wordt het een metric-balk en dat is het niet.

**3. Waiting.** Banden op de hoofdmetriek: `Any` · `Over 3 days` · `Over 7 days` · `Over 14 days`. Dit is de enige filter die direct op urgentie snijdt, en urgentie is waar dit product over gaat.

**4. Overdue only.** Een schakelaar, geen uitklapmenu. Aan betekent: alleen cursussen waarvan het oudste wachtende werk voorbij de deadline van zijn eigen opdracht ligt. Dat is een feit van de instelling, geen drempel die wij verzinnen.

Archived zit al in de statusfilter, dus de losse archief-schakelaar kan weg.

### Hoe de controls zich gedragen

- **De knop toont zijn eigen stand**, zoals `Status: All` en `Status: Needs grading`. Dat patroon van Lemlist is goed, neem het over.
- **Een actief filter valt op met rand en gewicht, niet met een kleurvlak.** Groen is hier verboden: dit is geen bevestigde positieve status en al helemaal geen "klik hier". Inactief wordt niet weggedempt met grijs, dat is dezelfde contrastregel als overal.
- **Filters staan links, sorteren staat rechts.** Het zijn twee verschillende dingen: filteren snijdt weg, sorteren rangschikt. Zet ze niet in dezelfde groep.
- **Toon altijd hoeveel er overblijft**, bijvoorbeeld `12 of 34 courses`, met daarnaast `Clear filters` zodra er iets aanstaat. Zonder die twee filtert iemand, vergeet het, en denkt volgende week dat zijn cursussen weg zijn.
- **Lege uitkomst is een ontworpen staat.** Geen leeg raster, maar één regel die zegt welke filters actief zijn en één knop om ze te wissen.
- **Filters resetten per sessie, de sorteerkeuze blijft bewaard.** Een filter is een tijdelijke versmalling, een sortering is een voorkeur. Iemand die volgende week terugkomt in een gefilterd dashboard denkt dat er werk verdwenen is.
- **Zet de filterstand in de URL.** Een coordinator moet een gefilterd overzicht kunnen doorsturen. Kost weinig, levert veel.

### Wat er bewust niet in zit

- **Favorites.** Lemlist heeft het, wij hebben er niets aan. Met acht cursussen markeer je niets, en met tweehonderd wil je niet je favorieten maar je eigen werk. Zie de openstaande vraag over markers.
- **Tags en Creators.** Die bestaan in ons datamodel niet, dus die verzinnen we niet.
- **Education level als filter.** Staat wel op de card als identiteit, maar verandert niet op welke cursus je gaat handelen.

## 10. Archiveren en verwijderen

Nu staan ze samen in één menu, direct onder elkaar, met een roze vlak achter Delete. Dat is de riskantste combinatie die je kunt maken: twee items van gelijke grootte, veertig pixel uit elkaar, waarvan de één omkeerbaar is en de ander niet.

**Het uitgangspunt: laat de wrijving meeschalen met wat er verloren gaat.** Archiveren is omkeerbaar en gebeurt elk semester. Verwijderen vernietigt inzendingen van studenten en goedgekeurde feedback, en gebeurt bijna nooit.

**Archiveren**
- Blijft bereikbaar vanaf de card, in het menu rechtsboven. Dat menu verschijnt op hover en op toetsenbordfocus, en is altijd zichtbaar op touch. Acht identieke puntjes-iconen permanent in beeld is dezelfde ruis als een label dat op elke card hetzelfde is.
- **Op een `Completed`-card zet je `Archive` als zichtbare actie in de voet**, niet weggestopt in het menu. Dat is het enige moment waarop archiveren de vanzelfsprekende volgende stap is, dus dan mag de actie zich laten zien. Zelfde principe als bij de labels: iets verschijnt op het moment dat het betekenis heeft.
- Na archiveren een korte melding met `Undo`. Omkeerbare actie, dus lage drempel, geen bevestigingsdialoog vooraf.

**Verwijderen**
- **Haal `Delete` van de card af.** Het hoort in de instellingen van de cursus zelf, waar je bewust naartoe navigeert. Het overzicht is er om te trieëren en te handelen op werk, niet om cursussen op te ruimen. Eén klik naast `Archive` is precies hoe je per ongeluk een semester aan studentwerk weggooit.
- In de cursusinstellingen: geen roze vlak, alleen rode tekst `#b3261e`. Een permanent gevuld vlak leest als selectie of hover, en een vlak verdien je pas als het selectie, interactie, waarschuwing of een echte groepering uitdrukt.
- **De bevestiging schaalt mee met de schade.** Lege cursus zonder inzendingen: gewone bevestiging. Cursus met inzendingen: benoem in de dialoog wat er verdwijnt, in aantallen, bijvoorbeeld "4 opdrachten en 32 inzendingen met goedgekeurde feedback", en laat de gebruiker de cursusnaam overtypen om te bevestigen.
- Dit sluit aan op wat Dante zelf al vastlegde in de usability-test over het verwijderen van een rubriccriterium: eerst een bevestiging, want nu is het meteen weg en niet terug te halen.

---

## 11. Wat blijft gelden uit het eerdere werk

- De gedeelde definitie van wachten, en dat `to grade`, `oldest waiting` en `Completed` er alledrie uit volgen.
- Geen `Active`-label. Dat zou op zeven van de acht cards staan, en een markering die bijna nooit verandert draagt geen informatie.
- Geen verhouding als `2 of 4 open`. Het woord "open" heeft twee mogelijke betekenissen die allebei fout uitpakken: óf het spreekt `to grade` tegen, óf het herhaalt het vager.
- Geen badge of pill om gewone metadata. Gewone tekst.
- Nooit contrast verlagen om iets minder nadruk te geven. Gebruik grootte, gewicht en ruimte.
- Geen kaartjes in kaartjes. De card is al een kaartje, zet er geen omkaderde vakjes in.
- `Oldest waiting` rekent vanaf het moment dat de student inleverde, niet vanaf het moment dat de verwerking klaar was. Zet die definitie in een tooltip.
- `Education Level` staat niet meer in de Create Course-modal, dat verhuist naar Manage rubric. Create Course houdt alleen `Title`.
- De zijbalk blijft zoals hij is: billing, referrals en tokens blijven staan.
- De labels `to grade`, `oldest waiting`, `last submission`, `due` en de statusnamen liggen vast. Verander ze niet zonder het door te geven.

## 12. Wat vervalt

- De twee breedtevarianten voor de tabel. Er is geen tabel meer.
- De hover-highlight over de rij en het punt over zebrastrepen.
- Het label naast de titel als plaatsingsregel. Op een card gaat de markering rechtsboven en de vervangende regel in de statuszone.

---

## 13. Wat je aan Dante teruglegt

- Wil hij bulk archiveren aan het eind van een semester? Nu niet bouwen, wel weten.
- Een cursus zonder opdrachten leest straks als `No submissions yet`. Dat klopt, maar het wijst niet naar de volgende stap. Als daar later een zetje bij moet, is dat de plek.

**Al beantwoord, niet opnieuw vragen:**

- Het toewijzen van een nakijker aan een opdracht gebeurt in de **admin-omgeving** van Enterprise, niet hier. Dus geen `Mine / Everyone`-filter op dit scherm.
- Er bestaat geen niveau boven de cursus, dus geen opleiding-, programma- of afdelingsfilter.
- Semester en collegejaar bestaan wel als begrip, maar wij vragen die data niet uit en halen die niet uit het LMS. Dus daar kun je niet op filteren en bouw je er niets voor.

## 14. Lever op

Het bijgewerkte bestand met beide varianten achter de schakelaar, en drie regels over wat je hebt gewijzigd en waar je van deze prompt bent afgeweken.
