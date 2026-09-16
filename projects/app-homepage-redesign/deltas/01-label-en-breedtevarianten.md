> **Vervallen per 04-09-2026.** De cursusrij is vervangen door cards. Gebruik `bouwprompt-cards.md`.
> Dit bestand blijft staan als vastlegging van de redenering, niet als opdracht.

# Delta 01 op de bouwprompt cursusrij

Aanvulling op de bouwprompt die je al hebt verwerkt. **Alleen wat hieronder staat verandert.** Alles wat er niet in staat blijft precies zoals je het gebouwd hebt.

Zes wijzigingen. Eerst één scopemededeling.

**Scope is Enterprise.** We ontwerpen voor instellingen die accounts uitzetten bij hun docenten, niet voor zelf-aanmeldende gebruikers. Alles wat specifiek is voor product-led growth valt buiten deze opdracht.

---

## Wijziging 1: de tweede regel wordt een label naast de titel

Haal de tweede regel onder de cursusnaam weg. Eén regel per rij. Naast de titel komt alleen een label **als de cursus afwijkt van de norm**. Zie de volledige tabel bij wijziging 3, want die voegt er een staat aan toe.

**Waarom `Active` verdwijnt.** In je huidige scherm staat `Active` op zeven van de acht rijen. Een label dat bijna nooit verandert draagt geen informatie, kost wel aandacht, en staat precies op de weg die het oog aflegt van de naam naar de getallen. Onze `compositie.md` zegt het voor kolommen en het geldt hier net zo: verspil geen kolom aan dezelfde categorie voor een reeks rijen. De norm hoeft geen naam.

**Waarom het aantal opdrachten helemaal uit de rij gaat.** Niet als kolom, niet als label. Het woord "open" heeft maar twee mogelijke betekenissen en allebei zijn ze kapot. Betekent het "deadline nog niet verstreken", dan kan een cursus `0 of 4 open` tonen terwijl To grade op 20 staat: de twee cellen spreken elkaar tegen en een docent leest "0 open" als "hier hoef ik niks" bij de drukste cursus op het scherm. Betekent het "er ligt nog werk in", dan zegt het hetzelfde als To grade maar vager en minder nauwkeurig. Een derde betekenis die iemand uit zichzelf goed raadt bestaat niet.

De vraag die de verdeling moest beantwoorden, of een cursus loopt of afgerond is, wordt vanaf nu beantwoord door het `Completed`-label uit wijziging 3. Het kale aantal opdrachten hoort op de cursuspagina, want het verandert niet welke cursus je opent.

De verhouding degenereert bovendien aan de uiteinden: in je eigen scherm staat nu `1 of 1 assignments open` bij Marketing plan, inclusief meervoudsfout.

**Vorm.** Gewone tekst, kleiner dan de titel, geen badge en geen pill. Een pill om gewone metadata staat bij ons op de lijst waaraan je sjabloonwerk herkent. Klikbare labels krijgen een pijltje, zoals `Not set up →` nu al doet. Niet dempen met grijs: kleiner en lichter van gewicht mag, contrast blijft boven 4.5:1.

**Winst.** Alle rijen worden even hoog en één regel hoog. Lagere rijhoogte, meer cursussen in beeld, rustiger raster.

---

## Wijziging 2: bouw twee breedtevarianten

Dante wil beide zien voor hij kiest. Lever ze in **één bestand** met een kleine schakelaar.

**Wat verschilt is precies één ding: de breedtestrategie.** Al het andere moet identiek zijn, anders zegt de vergelijking niets. Zelfde data, zelfde kolommen, zelfde labels, zelfde kleurregel, zelfde rijhoogte.

**Variant A, smallere kaart.** Kaart op circa 900 px, links uitgelijnd in de pagina. Naam en getallen staan weer bij elkaar en de leegte in het midden verdwijnt.

**Variant B, volle breedte verdiend.** Kaart blijft volle breedte. Cursusnaam krijgt een maximumbreedte, de drie metriekkolommen staan daar direct achter, en de overgebleven ruimte rechts is voor de rij-acties die nu al op hover verschijnen. Dan is de breedte gebruikt in plaats van leeg.

**In beide varianten:** een hover-highlight over de volle rij, zodat de koppeling tussen naam en getallen dicht is op het moment dat je wijst.

**Geen zebrastrepen.** Het bewijs is zwak: het serieuze onderzoek van Jessica Enders (A List Apart, 244 deelnemers) vond geen significante snelheidswinst en een kleine winst in nauwkeurigheid, en zij concludeerde zelf dat het beeld er onduidelijker op werd. Het probleem hoort bij de bron opgelost, niet met strepen gedempt.

**De schakelaar** is tijdelijk gereedschap, geen productfunctie. Klein, buiten de kaart, rechtsboven op de pagina, met de letterlijke tekst `Layout A / B`. Hij gaat eruit zodra de keuze valt.

---

## Wijziging 3: voeg een afgerond-toestand toe

**Het probleem.** In je huidige scherm staan Law, Social Work en Geneeskunde alledrie op `0` en `–`. Dat kan drie verschillende dingen betekenen: er is nooit iets ingeleverd, het ligt stil tussen twee opdrachten in, of de cursus is echt klaar. Die drie zijn nu niet te onderscheiden. Dat is een informatiefout.

**De definitie, en wijk hier niet van af.** Een cursus is afgerond wanneer **alle deadlines in de cursus verstreken zijn én alles nagekeken en afgetekend is.**

Gebruik nadrukkelijk **niet** `To grade = 0` als voorwaarde. Nul te beoordelen zegt vandaag niets, want morgen levert er iemand in. Een label dat de volgende dag weer uit gaat is ruis, en een toestand die kan terugflippen kun je geen afrondingsbetekenis geven. Alleen een stabiele toestand verdient dit label.

**De volledige labelreeks**, precedentie van boven naar beneden, de eerste die past wint:

| Situatie | Label naast de titel | Klikbaar |
|---|---|---|
| Cursus gearchiveerd | `Archived` | nee |
| Setup niet af | `Setup incomplete →` | ja |
| Nul opdrachten | `No assignments yet →` | ja |
| Alles ingeleverd verwerkt en alle deadlines voorbij | `Completed ✓` in green-deep | nee |
| Alle overige | geen label | n.v.t. |

NL: `Gearchiveerd`, `Setup niet af`, `Nog geen opdrachten`, `Afgerond`.

### Eerst één gedeelde definitie, en dit is de belangrijkste regel hier

Alles op deze rij steunt op één begrip. Definieer dat één keer en gebruik het overal, anders krijg je opnieuw cellen die elkaar tegenspreken.

**Een inzending "wacht" zolang de docent hem niet heeft goedgekeurd.**

Dus: ingeleverd door de student, en nog niet afgetekend. Een inzending waarvan de AI de feedback al klaar heeft maar die de docent nog niet heeft bekeken, **wacht nog steeds**. Dat volgt uit hoe het product werkt: elke opmerking wordt door de docent bekeken en goedgekeurd voordat de student iets ziet. Niet-goedgekeurd betekent dat de student nog niets heeft.

Uit die ene definitie volgt de hele rij:

- `To grade` = aantal wachtende inzendingen in de cursus.
- `Oldest waiting` = van alle wachtende inzendingen, de oudste, gemeten vanaf het moment dat de student inleverde.
- `Completed` = er wacht niets meer, en er kan niets meer binnenkomen.

Daardoor kunnen de drie elkaar per definitie niet tegenspreken. Dat is precies wat er mis was met `2 of 4 open`.

### Per staat, precies

**`Archived`**
- **Voorwaarde:** de cursus is gearchiveerd.
- **Precedentie:** hoogste. Is een cursus gearchiveerd, dan geen enkel ander label, ongeacht wat er in de cursus staat.
- **Klik:** niet klikbaar.
- **Cellen:** toon gewoon de echte waarden. Niet leegmaken. Het label zegt al dat de cursus buiten je werkstroom staat, en de waarden verzwijgen zou een onwaarheid zijn.

**`Setup incomplete →`**
- **Voorwaarde:** de cursus heeft minstens één opdracht, en minstens één van die opdrachten is nog niet volledig ingericht.
- **Belangrijk:** verzin hier geen nieuwe definitie van "volledig ingericht". Gebruik exact dezelfde conditie die de bestaande actie `Complete setup` al controleert. Eén bron, anders gaan de twee uit elkaar lopen.
- **Klik:** naar de opdrachtenlijst van die cursus, met de onvolledige opdracht aangewezen, en met de melding **wat** er precies mist. Dat laatste is geen extraatje: in onze eigen usability-test werd op `Complete setup` geklikt en gebeurde er niets bruikbaars.
- **Cellen:** echte waarden. Er kan tegelijk gewoon werk liggen te wachten.

**`No assignments yet →`**
- **Voorwaarde:** de cursus bestaat en heeft nul opdrachten.
- **Sluit `Setup incomplete` uit:** zonder opdrachten kan er ook geen onvolledige opdracht zijn. De twee kunnen elkaar dus niet overlappen.
- **Klik:** naar het aanmaken van een opdracht in die cursus.
- **Cellen:** alle drie `–`. Er is niets om te tellen.

**`Completed ✓`**
- **Voorwaarde, alle drie tegelijk:**
  1. de cursus heeft minstens één opdracht,
  2. van elke opdracht ligt de deadline in het verleden, en
  3. er wacht geen enkele inzending meer, dus alles is door de docent goedgekeurd.
- **Randgeval, opdracht zonder inzendingen:** die blokkeert niet. Een student die nooit heeft ingeleverd mag niet voorkomen dat de cursus ooit afrondt.
- **Randgeval, late inzending na afronding:** het label gaat weer uit en de cursus komt terug in de gewone staat. Dat is correct, want er ligt weer werk. Dit is iets anders dan een label dat elke dag aan en uit gaat: een te late inzending is een uitzondering, geen dagelijks ritme.
- **Tijdzone:** "deadline in het verleden" beoordeel je tegen de tijdzone van de instelling, niet die van de browser. Anders zie twee collega's een verschillende staat.
- **Klik:** niet klikbaar. Er valt niets te doen.
- **Cellen:** `To grade` op `0`, `Oldest waiting` op `–`, `Last submission` op de echte datum.

**Geen label**
- **Voorwaarde:** alle overige gevallen. De cursus loopt gewoon.
- Dit is de norm en de norm krijgt geen naam.

**Kleur.** Dit is de enige plek in deze tabel waar groen mag. Ons `core/regels.md` staat groen op twee plekken toe en de tweede is letterlijk "een bevestigde positieve status in een tool: klaar, goedgekeurd, loopt op schema". Dit is dat geval. Drie voorwaarden uit diezelfde regel:

1. **Gebruik `green-deep` (#007b54), niet de felle `#00e075`.** Groen als tekst op wit heeft anders te weinig contrast. De felle werkt alleen als vlak met navy tekst erop.
2. **Zet er een signaal naast dat geen kleur is.** Het vinkje én het woord, nooit alleen een groene stip.
3. **Het codeert een toestand, geen mening.** Bij de strikte definitie klopt dat. Bij `To grade = 0` zou het onze mening zijn dat nul gunstig is, en dan valt het onder het verbod op groen omdat een waarde goed uitkomt.

Met de strikte definitie kleurt één of twee van de acht rijen groen. Dat is een signaal. Met `To grade = 0` waren het er drie geweest en werd groen behang.

**De rij blijft staan waar hij staat.** Afgerond is niet hetzelfde als gearchiveerd. Niet laten zakken, niet verbergen. Archiveren is een aparte, bewuste handeling van de gebruiker.

**Geen viering op deze pagina.** Geen confetti, geen animatie. Het label is een rustige toestand in een lijst die je later een keer opent. Het gevoel van afronden hoort bij het moment waarop de laatste inzending wordt afgetekend, en dat gebeurt in het nakijkscherm. Dat wordt een aparte opdracht, loop er hier niet op vooruit.

---

## Wijziging 4: de data is bevestigd, bouw Oldest waiting

De oorspronkelijke bouwprompt bevatte een terugvalladder omdat onduidelijk was welke data bestond. Die onduidelijkheid is weg. Beide datapunten bestaan:

- Een opdracht heeft een deadline: het moment waarop elke student ingeleverd moet hebben.
- Per inzending is bekend wanneer de student heeft ingeleverd.

Dus: **bouw `Oldest waiting`.** Geen `Overdue`, geen terugval.

**Reken vanaf het moment van inleveren door de student**, niet vanaf het moment dat de verwerking klaar was. Dat is wat de student ervaart en dat is de belofte die we verkopen. Zet die definitie in een tooltip op de kolomkop.

---

## Wijziging 5: Education Level weg uit Create Course

Haal het veld `Education Level` uit de Create Course-modal. Het verhuist naar Manage rubric, een ander scherm. Create Course houdt alleen `Title` over.

**Bouw voor het gevolg.** Er kan nu een cursus bestaan zonder dat het niveau gezet is, terwijl dat veld de toon en het niveau van de feedback stuurt. Create Course mag niet stilzwijgend een niveau kiezen zonder dat iemand het weet. Zorg dat het niveau niet als verborgen standaardwaarde de feedback gaat sturen.

---

## Wijziging 6: de zijbalk blijft zoals hij is

Billing, referrals en tokens blijven staan. Bij Enterprise hoeven die er niet uit. Ontbreekt `tokens` nog, zet hem er dan bij naast billing en referrals. Bij product-led growth zou dit anders liggen, maar daar werken we nu niet aan.

---

## Wat expliciet blijft zoals het is

- De kolomset `Course | To grade | Oldest waiting | Last submission`.
- Rechts uitlijnen van de getalkolommen inclusief de kop.
- `–` bij niets wachtend, `today` onder een dag, geen nepprecisie.
- De kleurregel voor Oldest waiting: kleur alleen als het oudste wachtende werk voorbij de deadline van zijn eigen opdracht ligt, met het waarschuwingsicoon ernaast.
- Geen `Next due` en geen `Students` op de cursusrij.
- Het lege-staat-blok `No courses yet` blijft onaangeroerd. De eerste ervaring van een gloednieuw account valt buiten de Enterprise-scope en wordt later apart opgepakt.

## Lever op

Het bijgewerkte bestand met beide varianten achter de schakelaar, plus drie regels over wat je hebt gewijzigd.
