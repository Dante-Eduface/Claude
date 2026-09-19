> **Vervallen per 04-09-2026.** De cursusrij is vervangen door cards. Gebruik `bouwprompt-cards.md`.
> Dit bestand blijft staan als vastlegging van de redenering, niet als opdracht.

# Bouwprompt: cursusrij op de home page

Plak dit als geheel. Het is zelfstandig leesbaar, je hoeft er geen ander gesprek bij te hebben.

---

Je werkt aan `Design/Website/app-homepage-redesign/home-redesign.html`, de home page voor docenten die **al** cursussen en opdrachten hebben.

**Scope: Enterprise.** We ontwerpen nu voor instellingen die accounts uitzetten bij hun docenten, niet voor zelf-aanmeldende gebruikers. Alles wat specifiek is voor product-led growth valt buiten deze opdracht. De kolommen van de cursusrij zijn nu vastgesteld. Hieronder staat wat je bouwt, waarom, en wat je expliciet niet doet.

## De uitkomst

```
Course  |  To grade  |  Oldest waiting  |  Last activity
```

Onder de cursusnaam één tweede regel met de toestand van de cursus. Zie het blok "De tweede regel" hieronder voor de exacte staten.

Drie metriekkolommen, niet vier. Vier voelt druk en de vierde verdiende zijn plek niet.

## Waarom deze set

De toets per kolom was: verandert hij welke cursus ik nú open, is hij waar op cursusniveau of alleen afgeleid, heeft hij een fatsoenlijke lege staat, is hij berekenbaar, en doet hij hetzelfde werk als zijn buurman.

- **Oldest waiting** is het hoofdsignaal. Eduface verkoopt snelle formatieve feedback. De pijn is bij lange trajecten uitval en bij korte de werkdruk van beoordelaars, en allebei gaan over de wachttijd, niet over de planningskalender. Zie `Platform/product.md`. Een kolom die iets anders meet dan de belofte van het product, meet het verkeerde ding.
- **To grade** staat ervóór, want volume en urgentie zijn niet inwisselbaar. Twaalf dagen met één inzending is een ander karwei dan twaalf dagen met veertig. Je hebt de poort nodig voor de kwalificatie betekenis krijgt.
- **Last activity** blijft, want die is op cursusniveau echt waar. Wel het label preciezer maken: `Last activity` is dubbelzinnig (activiteit van de student of van mij). Maak er `Last submission` van, of zet er een tooltip bij. In onze eigen usability-test scoorde het criterium "uitleg bij instellingen en keuzes" een 3 met precies die klacht: je snapt de term, niet het effect in de tool.
- **Assignments** wordt geen kolom. Het aantal opdrachten verandert bijna nooit welke cursus je opent, dus het is context en geen signaal. Het staat op de tweede regel onder de naam.

## Het label naast de titel

Geen tweede regel onder de cursusnaam. Eén regel per rij, en naast de titel alleen een label **als de cursus afwijkt van de norm**.

Precedentie, de eerste die past wint:

| Situatie | Label naast de titel | Klikbaar |
|---|---|---|
| Cursus gearchiveerd | `Archived` | nee |
| Setup niet af, bijvoorbeeld geen rubric | `Setup incomplete →` | ja, naar wat er mist |
| Nul opdrachten | `No assignments yet →` | ja, naar opdracht toevoegen |
| Alle deadlines verstreken en alles nagekeken | `Completed ✓` in green-deep | nee |
| Alle overige | geen label, alleen de titel | n.v.t. |

NL: `Gearchiveerd`, `Setup niet af`, `Nog geen opdrachten`, `Afgerond`.

**Over `Completed`.** De definitie is strikt: alle deadlines in de cursus verstreken **én** alles nagekeken en afgetekend. Gebruik nadrukkelijk niet `To grade = 0`, want dat zegt vandaag niets en gaat morgen weer uit zodra iemand inlevert. Een label dat kan terugflippen is ruis. Zonder deadlines per opdracht kan dit label niet, bouw het dan niet half maar meld het.

Dit is de enige plek in deze tabel waar groen mag, en het is precies de uitzondering waarvoor onze regel geschreven is: groen mag op een bevestigde positieve status in een tool. Gebruik `green-deep` (#007b54), niet de felle `#00e075`, want groen als tekst op wit heeft anders te weinig contrast. Zet het vinkje én het woord neer, nooit alleen een groene stip. Bij de strikte definitie kleurt één of twee van de acht rijen groen. Bij `To grade = 0` waren het er drie geweest en werd groen behang.

Afgerond is niet hetzelfde als gearchiveerd: de rij blijft staan waar hij staat, niet laten zakken en niet verbergen. En geen viering op deze pagina, geen confetti en geen animatie. Het gevoel van afronden hoort bij het moment waarop de laatste inzending wordt afgetekend, en dat gebeurt in het nakijkscherm. Dat is een aparte opdracht.

**`Active` bestaat niet als label.** Dat is de norm, en de norm hoeft geen naam. In het huidige scherm staat `Active` op zeven van de acht rijen. Een label dat bijna nooit verandert draagt geen informatie, kost wel aandacht, en staat precies op de weg van de naam naar de getallen. Onze eigen `compositie.md` zegt het voor kolommen en het geldt hier net zo: verspil geen kolom aan dezelfde categorie voor een reeks rijen.

**Het aantal opdrachten staat niet in de rij.** Niet als kolom en niet als label. Het verandert bijna nooit welke cursus je opent, dus het hoort op de cursuspagina. Bouw geen `2 of 4 open` of enige andere verhouding: het woord "open" heeft twee mogelijke betekenissen die allebei fout uitpakken (of het spreekt To grade tegen, of het herhaalt To grade vager), en een verhouding degenereert aan de uiteinden. `0 of 4` leest als een tekort terwijl het meestal een afgeronde cursus is, en `1 of 1 assignments open` is ruis met een meervoudsfout erin.

Of een cursus loopt of afgerond is, lees je al af aan `To grade` op nul plus een oude `Last submission`. Dat zijn gemeten feiten. Een `open`-label zou een afgeleid oordeel zijn dat we erbovenop verzinnen, en dat is dezelfde fout als een deadline op de cursusrij zetten.

**Vorm:** gewone tekst, kleiner dan de titel, geen badge en geen pill. Een pill om gewone metadata staat bij ons op de lijst waaraan je sjabloonwerk herkent. Klikbare labels krijgen een pijltje, zoals `Not set up →` nu al doet.

**Alle rijen worden even hoog.** Dat is de winst van deze opzet: één regel per rij houdt de rijhoogte laag, er passen meer cursussen in beeld, en het raster wordt rustiger. `compositie.md`: label, waarde en detail identiek over alle gelijken heen.

## Deadlines

Een cursus heeft geen deadline, een opdracht wel.

- De due date hoort op de **opdrachtweergave**, daar is hij echt.
- Op de cursusrij zou hij alleen afgeleid zijn. Zet hem daar niet neer. Komt hij er ooit toch, dan heet hij `Next due` en nooit `Due`, anders suggereer je dat de cursus zelf een deadline heeft.

## Opmaak, en dit gaat bijna altijd mis

Uit `Design/Design system/core/compositie.md` en `core/regels.md`:

- **Getalkolommen rechts uitlijnen, inclusief de kolomkop.** Dit is letterlijk de regel waarvan in ons systeem staat dat hij bijna altijd fout gaat.
- **Geen nepprecisie.** `9 days`, niet `9.2 days`. Onder een dag wordt `today`.
- **Niets wachtend is `–`, niet `0 days`.** Dat zijn verschillende toestanden, en een nul suggereert dat er iets is dat nul dagen wacht.
- **Verlaag nooit contrast om iets minder nadruk te geven.** Gebruik grootte, gewicht of ruimte. De tweede regel onder de cursusnaam krijgt dus een kleinere graad en minder gewicht, maar blijft boven 4.5:1. Bron in ons systeem: NN/g, Principles of Visual Design, 2020. Kleine grijze tekst om dichtheid passend te maken staat bij ons ook op de lijst waaraan je sjabloonwerk herkent.
- Consistente eenheden over alle rijen.

## Kleur in Oldest waiting

Kleur codeert een toestand, geen mening over de uitkomst. Twaalf dagen amber maken omdat wij twaalf dagen lang vinden, is een mening, en er is geen sectornorm om die drempel aan op te hangen.

Dus: **kleur alleen wanneer de instelling zelf de grens heeft gezet**, dus wanneer het oudste wachtende werk voorbij de deadline van zijn eigen opdracht ligt. Dat is een feit. Heeft de opdracht geen deadline, dan gewoon navy, geen kleur.

Zet naast de kleur altijd een signaal dat geen kleur is, een label of een icoon, zodat het ook werkt voor wie kleur slecht onderscheidt. En groen komt hier niet voor: groen betekent bij ons "kijk hier" of "dit is goed afgelopen", nooit "klik hier", en zeker niet "dit getal is gunstig".

## De data is bevestigd

Beide datapunten bestaan:

- Een opdracht heeft een deadline: het moment waarop elke student ingeleverd moet hebben.
- Per inzending is bekend wanneer de student heeft ingeleverd.

Daarmee zijn `Oldest waiting` en de `Completed`-toestand allebei bouwbaar. Geen terugval nodig.

**Reken `Oldest waiting` vanaf het moment van inleveren door de student**, niet vanaf het moment dat de verwerking klaar was. Dat is wat de student ervaart en dat is de belofte die we verkopen. Zet die definitie in een tooltip op de kolomkop, anders herhaal je de labelvaagheid uit onze eigen usability-test.

## Bouw twee breedtevarianten

Dante wil beide zien voor hij kiest. Lever ze in **één bestand** met een kleine schakelaar, zodat dezelfde data in beide layouts staat en er niets anders verschilt.

**Wat er verschilt tussen A en B is precies één ding: de breedtestrategie.** Al het andere moet identiek zijn, anders zegt de vergelijking niets. Zelfde data, zelfde kolommen, zelfde labels, zelfde kleurregel, zelfde rijhoogte.

**Variant A, smallere kaart.** Kaart op circa 900 px, links uitgelijnd in de pagina. Naam en getallen staan weer bij elkaar, de leegte in het midden verdwijnt. Dit is de goedkoopste ingreep.

**Variant B, volle breedte verdiend.** Kaart blijft volle breedte. Geef de cursusnaam een maximumbreedte, zet de drie metriekkolommen daar direct achter, en gebruik de overgebleven ruimte rechts voor de rij-acties die nu al op hover verschijnen. Dan is de breedte gebruikt in plaats van leeg.

**In beide varianten:** een hover-highlight over de volle rij. Op het moment dat je wijst is de koppeling tussen naam en getallen visueel dicht. Geen zebrastrepen: het bewijs daarvoor is zwak (Enders, A List Apart, 244 deelnemers, geen significante snelheidswinst) en het probleem hoort bij de bron opgelost.

**De schakelaar** is een tijdelijk hulpmiddel, geen productfunctie. Klein, buiten de kaart, rechtsboven op de pagina, met de letterlijke tekst `Layout A / B`. Hij gaat er weer uit zodra de keuze valt.

## Zijbalk en Create Course

**De zijbalk blijft zoals hij is.** Billing, referrals en tokens blijven staan. Bij Enterprise hoeven die er niet uit. Ontbreekt `tokens` nog, zet hem er dan bij naast billing en referrals. Bij product-led growth zou dit anders liggen, maar daar werken we nu niet aan.

**Haal `Education Level` weg uit de Create Course-modal.** Dat veld verhuist naar Manage rubric, een ander scherm. Create Course houdt alleen `Title` over.

Let op het gevolg, en bouw daarvoor: een cursus kan nu bestaan zonder dat het niveau is gezet. Zorg dat Create Course niet stilzwijgend een niveau kiest zonder dat iemand het weet. Toon in Manage rubric zichtbaar welk niveau geldt, zodat het niet als verborgen standaardwaarde de feedback stuurt.

## Wat je expliciet niet doet

- Geen `Next due` op de cursusrij.
- Geen `Students`-kolom. Puur context, geen actie.
- Geen `Assignments` als eigen kolom.
- Geen vierde metriekkolom erbij verzinnen.
- Geen aparte `Status`-kolom.
- Geen tweede regel onder de cursusnaam.
- Geen `Active`-label.
- Geen `2 of 4 open` of enige andere verhouding.
- Geen badge of pill om een label.
- Geen zebrastrepen.
- Geen grijstint om iets rustiger te maken.

## De lege staat staat stil

Het blok `No courses yet / Create a course, add an assignment, and upload your first submissions` niet verder uitwerken. De eerste ervaring van een gloednieuw account valt buiten de Enterprise-scope en wordt later apart opgepakt. Laat het staan zoals het is en steek er geen werk in.

## Woorden liggen vast

De labels `To grade`, `Oldest waiting`, `Last submission` en de drie labelstaten worden één op één overgenomen op het nieuw-account-scherm. Verander ze niet zonder het door te geven, want twee schermen die voor tachtig procent op elkaar lijken zijn erger dan twee die duidelijk verschillen. Bij bijna-gelijke routes stijgt de foutkans juist met meer ervaring, en die fouten worden even snel gemaakt als de goede en blijven onopgemerkt (Woltz, Gardner & Bell, 2000).

## Wat eerlijk gezegd vakmanschap is en geen bewijs

Dat `To grade` vóór `Oldest waiting` staat en dat `Assignments` naar de tweede regel zakt, is een oordeel. Niemand heeft dat gemeten. De opmaakregels, de contrastregel en de kleurregel liggen wel vast in ons systeem. Presenteer het verschil niet als hetzelfde.

## Lever op

De aangepaste `home-redesign.html`, plus drie regels over wat je hebt gewijzigd en welke van de drie terugvalopties je hebt gebouwd.
