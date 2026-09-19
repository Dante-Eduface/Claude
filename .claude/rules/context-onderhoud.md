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

**Nooit een aanname invullen die ik kan navragen.** Weet ik het niet zeker, dan zet ik het als OPEN in het bestand met de datum, en zet ik de vraag in `context/open-vragen.md`.

**Komt een persoonlijk onderwerp ter sprake, dan controleer ik het bijbehorende bestand.** Gaat het gesprek over sport, geld, relatie, wonen of leren, dan open ik `context/personal.md` en kijk ik of wat daar staat nog klopt. Zo ja, niks zeggen. Zo nee, of twijfel, dan vraag ik het.

De maat daarbij:

- **Hoogstens twee of drie vragen per gesprek.** Meer is een formulier, en dat vult niemand in.
- **Alleen vragen die passen bij waar het gesprek toch al over gaat.** Een vraag over zijn relatie tijdens een outreachsessie is fout getimed, ook als hij openstaat.
- **Een feit ouder dan 90 dagen mag getoetst worden** met één zin: "hier staat nog X, klopt dat nog?"
- **Geen vraag stellen die ik zelf kan opzoeken.** Zijn agenda, Close en de repo staan open. Eerst kijken, dan pas vragen. Zie ook `.claude/rules/credits.md`.

Geeft hij antwoord, dan gaat het antwoord meteen naar het juiste bestand, verhuist de vraag naar de sectie "Beantwoord en verwerkt", en meld ik dat in één regel.

## 4. Waar wat landt

| Wat | Bestand |
|---|---|
| Wie Dante is, rol, weekritme | `context/me.md` |
| Wat Eduface is, mensen, tools | `context/eduface.md` |
| Doelen en de leidende maat | `context/current-priorities.md` |
| Sport, geld, relatie, wonen, leren | `context/personal.md` |
| Wat ik niet zelf mag invullen | `context/open-vragen.md` |
| Een keuze met gevolgen, plus de redenering | `decisions/log.md` |
| Productclaims, prijs, salesmethode | het bestand in `references/`, niet een contextbestand |

Twijfel je tussen werk en persoonlijk: staat het in zijn agenda als werkafspraak, dan is het werk.

## 5. Elke aanpassing krijgt een datum

Bovenaan elk contextbestand staat `_Laatst bijgewerkt: JJJJ-MM-DD._`, en die zet ik bij elke wijziging om. Bij een los feit dat gedateerd is (een bedrag, een target, iets dat uit de agenda komt) zet ik de datum erbij in de zin zelf.

Zonder datum kun je niet zien of iets oud is, en dan wordt alles even betrouwbaar behandeld. Dat is precies hoe die football-regel er maanden in bleef staan.

## 6. De maandelijkse ronde

Eén keer per maand, of als een sessie er toch al langs komt:

1. Loop de vier werkcontextbestanden door op dingen die je niet meer herkent uit de afgelopen maand chats, agenda en Close.
2. Kijk in `context/open-vragen.md` welke vragen er langer dan 90 dagen staan.
3. Leg Dante hoogstens drie dingen voor: wat volgens mij niet meer klopt, en wat ik zou schrappen.
4. Schrappen mag altijd voorgesteld worden. Een leeg vak is beter dan een verkeerd ingevuld vak.

## 7. Wat ik nooit doe

- **Een gat opvullen met iets plausibels.** Niet afleiden dat hij wel verhuisd zal zijn omdat het kantoor verhuisde. Vragen.
- **Twee versies van hetzelfde feit laten staan.** Nieuw wint, oud gaat weg. Zie het inkomen in `context/personal.md`: twee getallen naast elkaar betekent dat geen van beide bruikbaar is.
- **Een bestand verwijderen.** Verplaatsen naar `archives/` met een datum in de mapnaam, zodat de oude versie na te lezen is.
- **Een aanpassing doorvoeren zonder hem te melden.**
- **Een persoonlijk feit in werkcontext zetten, of andersom.**
