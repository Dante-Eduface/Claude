# Context actueel houden

Vastgelegd 19-09-2026, op verzoek van Dante: *"in de chats praat ik over de veranderingen die ik doorbreng in mijn dagelijks leven, die verandering moet je ook gelijk toepassen in deze files. Dat moet automatisch gaan, je moet gewoon aan mijn chat zien of herkennen."*

Het probleem dat deze regel oplost: een contextbestand dat niet meer klopt is erger dan geen contextbestand. Het klinkt betrouwbaar en het is het niet. Op 19-09-2026 stond er nog in dat Dante 19 was, SDR, en drie keer per week naar Düsseldorf reisde voor American football. Alle drie fout, maanden lang, omdat niemand het bestand opendeed.

## 1. Meebewegen zonder dat het gevraagd wordt

**Zegt Dante in de chat iets dat een contextbestand tegenspreekt of aanvult, dan pas ik dat bestand dezelfde beurt aan.** Ik wacht niet tot hij zegt "schrijf dat op". Dat moment komt namelijk nooit.

Signalen waar ik op let, ook als ze terloops vallen in een gesprek over iets anders:

- **Stoppen en beginnen:** "ik ben gestopt met", "ik doe nu", "ik ben begonnen met", "dat doen we niet meer"
- **Rol en verantwoordelijkheid:** "mijn rol is nu", "ik ben verantwoordelijk voor", "dat doet iemand anders nu"
- **Plaats en ritme:** "we zijn verhuisd", "ik werk nu vanaf", "ik train nu op"
- **Correctie op wat er staat:** "dat klopt niet meer", "dat is achterhaald", "dat was vorig jaar"
- **Getallen:** een bedrag, een target, een aantal dat afwijkt van wat er vastligt
- **Mensen:** een naam die ik niet ken, of een naam die ik ken in een andere rol

In mijn antwoord meld ik in **één regel** wat ik heb bijgewerkt. Niet uitweiden, wel altijd noemen: een stille wijziging is net zo onbetrouwbaar als een verouderd bestand.

## 2. De grens met de feedbackregel

Deze twee regels lijken op elkaar en gaan over verschillende dingen. Door elkaar halen levert of te trage of te gretige aanpassingen op.

| Soort uitspraak | Voorbeeld | Wat ik doe |
|---|---|---|
| **Een feit over Dante of Eduface** | "ik ben gestopt met football", "mijn rol is nu CSM", "we verkopen ook mondelinge examens" | Direct verwerken in het contextbestand, één regel melden. Deze regel. |
| **Een regel over hoe ik moet werken** | "deze mail is te lang", "noem ons altijd een onderwijskundig AI-model" | De trap uit `.claude/rules/feedback.md`: correctie, dan patroon, dan pas een regel, met de tekst vooraf voorgelegd. |

Kort: een feit verandert een bestand, een oordeel verandert een werkwijze. Het eerste gaat vanzelf, het tweede gaat met akkoord.

## 3. Vragen stellen in plaats van invullen

**Nooit een aanname invullen die ik kan navragen.** Weet ik het niet zeker, dan zet ik het als OPEN in het bestand met de datum, en zet ik de vraag in `Context/open-vragen.md`.

**Komt een persoonlijk onderwerp ter sprake, dan controleer ik het bijbehorende bestand.** Gaat het gesprek over gym, eten of geld, dan open ik het bestand in `Personal/` dat erover gaat en kijk ik of wat daar staat nog klopt. Zo ja, niks zeggen. Zo nee, of twijfel, dan vraag ik het.

De maat daarbij:

- **Hoogstens twee of drie vragen per gesprek.** Meer is een formulier, en dat vult niemand in.
- **Behalve in het bestand zelf.** Daar mag de hele lijst staan: Dante beantwoordt ze het liefst in één keer door in `open-vragen.md` te schrijven (afgesproken 19-09-2026). Verwerk zijn antwoorden daarna naar het juiste contextbestand en haal de vraag uit de lijst.
- **Alleen vragen die passen bij waar het gesprek toch al over gaat.** Een vraag over zijn relatie tijdens een outreachsessie is fout getimed, ook als hij openstaat.
- **Een feit ouder dan 90 dagen mag getoetst worden** met één zin: "hier staat nog X, klopt dat nog?"
- **Geen vraag stellen die ik zelf kan opzoeken.** Zijn agenda, Close en de repo staan open. Eerst kijken, dan pas vragen. Zie ook `.claude/rules/credits.md`.

Geeft hij antwoord, dan gaat het antwoord meteen naar het juiste bestand, verhuist de vraag naar de sectie "Beantwoord en verwerkt", en meld ik dat in één regel.

## 4. Waar wat landt

| Wat | Bestand |
|---|---|
| Wie Dante is, zijn rol, hoe hij werkt | `Context/me.md` |
| Een tijd: wanneer hij iets doet | `Context/schema.md`, en daar alleen |
| Wat Eduface is, mensen, tools | `Context/eduface.md` |
| Doelen en de leidende maat | `Context/current-priorities.md` |
| Gym en trainen | `Personal/gym/gym.md` |
| Eten, calorieën, koken | `Personal/koken/koken.md` |
| Alles met geld | `Personal/geld/geld.md` |
| Wat ik niet zelf mag invullen | `Context/open-vragen.md` |
| Een keuze met gevolgen, plus de redenering | `Decisions/log.md` |
| Productclaims | `Platform/product.md` |
| Prijs | `GTM/Pricing/` |
| Salesmethode en playbooks | `GTM/Knowledge/` |

Twijfel je tussen werk en persoonlijk: staat het in zijn agenda als werkafspraak, dan is het werk.

## 5. Elke aanpassing krijgt een datum

Bovenaan elk contextbestand staat `_Laatst bijgewerkt: JJJJ-MM-DD._`, en die zet ik bij elke wijziging om. Bij een los feit dat gedateerd is (een bedrag, een target, iets dat uit de agenda komt) zet ik de datum erbij in de zin zelf.

Zonder datum kun je niet zien of iets oud is, en dan wordt alles even betrouwbaar behandeld. Dat is precies hoe die football-regel er maanden in bleef staan.

## 6. De maandelijkse ronde

Eén keer per maand, of als een sessie er toch al langs komt:

1. Loop de vier werkcontextbestanden door op dingen die je niet meer herkent uit de afgelopen maand chats, agenda en Close.
2. Kijk in `Context/open-vragen.md` welke vragen er langer dan 90 dagen staan.
3. Leg Dante hoogstens drie dingen voor: wat volgens mij niet meer klopt, en wat ik zou schrappen.
4. Schrappen mag altijd voorgesteld worden. Een leeg vak is beter dan een verkeerd ingevuld vak.

## 7. Het schema bijhouden vanuit de agenda

Afgesproken 20-09-2026. Dante: *"ik vind het helemaal niet erg als je af en toe mijn agenda kijkt, en als je ziet dat er een aantal dingen aangepast zijn in de basis, dan kun je ook aan mij vragen: deze aanpassingen zijn gemaakt, zou ik dat ook aanpassen in het schema?"*

**De agenda is de bron, `Context/schema.md` is de samenvatting.** Wijken ze af, dan klopt het bestand niet, niet de agenda.

### Wanneer kijken

- Bij de maandelijkse ronde hierboven.
- Bij het week plannen op zaterdag, want dan ligt de agenda toch open.
- Als een gesprek over zijn planning gaat.

Niet vaker. Elke sessie de agenda ophalen kost geld en levert meestal niets op, zie `.claude/rules/credits.md`.

### Wat wel en niet telt

**Alleen terugkerende afspraken vormen de basis.** Een gymsessie die structureel verschuift is een schemawijziging. Een verjaardag in het weekend waardoor hij alles opschuift is dat niet.

| Wat ik zie | Wat ik doe |
|---|---|
| Een terugkerende afspraak is verplaatst, toegevoegd of verwijderd | Vragen of het schema mee moet |
| Dezelfde verschuiving twee weken op rij | Vragen of het de nieuwe basis is |
| Eén losse week die anders loopt | Niets. Niet noemen, niet vastleggen |
| Een losse afspraak in Eduface Meetings | Niets. Dat is geen ritme |

### Hoe ik het voorleg

Eén regel, met wat ik zie en wat ik zou aanpassen: *"Je gym staat sinds twee weken op 18:00 in plaats van 17:00. Zal ik dat in het schema zetten?"*

**Nooit stil aanpassen.** Het schema is van hem, niet van mij. Ook niet als de agenda duidelijk lijkt.

De kalender-ID's staan in `Context/schema.md`, zodat je ze niet hoeft op te zoeken.

## 8. Wat ik nooit doe

- **Een gat opvullen met iets plausibels.** Niet afleiden dat hij wel verhuisd zal zijn omdat het kantoor verhuisde. Vragen.
- **Twee versies van hetzelfde feit laten staan.** Nieuw wint, oud gaat weg. Twee getallen naast elkaar betekent dat geen van beide bruikbaar is.
- **Hetzelfde feit op twee plekken zetten.** Elk feit heeft één huis, zie de tabel hierboven. Heeft een tweede bestand het ook nodig, verwijs dan in plaats van te kopiëren. Dit ging op 20-09-2026 mis: naam, rol en schema stonden in twee bestanden tegelijk.
- **Een vraag stellen die al beantwoord is.** Lees eerst de tabel "Beantwoord en verwerkt" onderaan `Context/open-vragen.md`.
- **Een bestand verwijderen.** Verplaatsen naar `Archive/` met een datum in de mapnaam, zodat de oude versie na te lezen is.
- **Een aanpassing doorvoeren zonder hem te melden.**
- **Een persoonlijk feit in werkcontext zetten, of andersom.**
- **Het schema aanpassen op basis van zijn agenda zonder het te vragen.** Zie punt 7.

