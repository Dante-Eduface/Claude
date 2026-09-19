---
name: outreach
description: Agent 4 van de SHIFT-pijplijn, voor elke markt. Schrijft uit het dossier van agent 3 per persoon het LinkedIn-connectieverzoek (max 300 tekens), mail 1 (onderwerp plus ~110 woorden) en de reminder, in de taal en het register van het marktprofiel. Levert altijd het haakje met bron en de redenering erbij. Komt het niet boven "citeren en dan pitchen" uit, dan schrijft de skill niets en legt het aan Dante voor. Trigger wanneer Dante zegt "schrijf de berichten", "agent 4", "maak outreach voor deze lijst", "schrijf een connectieverzoek voor [naam]", "write the UK messages", of een wachtrij aanwijst. Vervangt linkedin-outreach sinds 10-09-2026 voor de pijplijn; voor losse NL-mails buiten de pijplijn blijft outreach bestaan.
---

# Agent 4: de berichten

Elk contact krijgt een handgemaakt bericht, want per organisatie is er maar één persoon en er is geen tweede lane om achter te schuilen.

## Twee standen

Deze skill heeft twee ingangen. Bepaal altijd eerst welke van toepassing is.

- **Stand 1 — pijplijn (dit document).** Agent 4 van SHIFT. De aanleiding is een dossier
  dat agent 3 heeft opgeleverd. Je schrijft het LinkedIn-connectieverzoek, mail 1 en
  de reminder, en schrijft ze terug naar het master-document.
- **Stand 2 — los signaal.** Zie `los-signaal.md`. De aanleiding komt buiten de pijplijn
  om: een aanmelding, een lijst opleiders, of "wie moet ik mailen bij deze school".
  Daar doe je de research zelf via `person-research` en `stakeholder-mapping`,
  en bepaal je eerst het segment en poort 0.


Per persoon lever je drie stukken, allemaal in de taal van de markt:
1. het **connectieverzoek** van maximaal 300 tekens, met de vraag er al in;
2. **mail 1**: onderwerp plus een mail van ongeveer 110 woorden, één haakje, gesloten CTA;
3. de **reminder**: twee tot drie zinnen die als reply in dezelfde thread gaan, zonder onderwerp.

Dit is Dante's werk tot de Discovery-gate (`scope-discovery-gate`). Daarna hand-off naar Jeroen.

## Huidige campagne (vanaf 17-09-2026): event-uitnodiging, geen productpitch

**Geldt alleen voor de VK-markt, en alleen voor dit ene event (het ALT-webinar).** In NL en US speelt dit niet: daar schrijf je gewoon volgens de rest van dit bestand (de productpitch-sjablonen), niet deze event-versie. Dit is geen generieke "webinar-modus", het is specifiek de sessie hieronder.

**Zolang deze kop hier staat, schrijf je geen productpitch maar een persoonlijke uitnodiging.** Besluit Jeroen, 17-09-2026. De onderzoeksmethode in de rest van dit bestand (Stap 1 t/m 4, de brontoets, de dragertoets, `haakje-zoeken.md`) blijft ongewijzigd: je zoekt nog steeds naar wat er in het dossier klopt en van henzelf komt. Wat verandert is het **doel** van het bericht en de **drie sjablonen** in Stap 5, die voor deze campagne door de onderstaande versies vervangen worden.

**Het event.** Een online, invite-only sessie die Eduface organiseert met de Association for Learning Technology (ALT) en Jisc, over *the business outcomes of AI marking and feedback for institutions*. Verwacht rond de 60 deelnemers. **Noem het daarom nergens een kleine of intieme sessie en zeg nergens dat het "geen webinar" is** (dat ging op 17-09-2026 al een keer fout), dat is feitelijk onjuist en wordt afgestraft zodra iemand het doorheeft. De exclusiviteit zit in "invite-only" en "op uitnodiging, geen open inschrijving", niet in de omvang van de groep.

**Lemlist-campagnenaam: "ALT Webinar".** Agent 5 (`lemlist-import`) gebruikt deze naam voor de campagne in het VK-marktprofiel, niet een andere spelling.

**Wat er verandert ten opzichte van Stap 3 en 4 hieronder:**
- **Een rol is nu op zichzelf een geldig "waarom jij".** Niveau 2 uit `haakje-zoeken.md` hoeft niet uit een citaat te komen: "als Provost ligt academic standards bij jou" is genoeg basis om iemand uit te nodigen, want de rol is hier letterlijk de reden voor de uitnodiging. Heb je wél een sterk, specifiek detail uit het dossier (een citaat, een beleidsregel, een getal), gebruik dat dan om de rol-redenering concreet te maken, niet om hem te vervangen.
- **Geen vage vulzinnen.** "push the discussion further", "your unique perspective", "given your seniority" zonder onderbouwing: allemaal verboden (Jeroen, 17-09-2026). Weet je iets specifieks over hun rol of hun materiaal, zeg dan concreet wat het is.
- **De CTA mag overal gesloten zijn, ook in het connectieverzoek.** Dit is een RSVP-vraag, geen sales-vraag, dus "Can I send you the details?" en "Worth the details?" mogen hier, in tegenstelling tot de open-vraag-regel bij de productpitch verderop in dit bestand.
- **Geen dubbele punten (colons) in de berichttekst.** Net als em-dashes: schrap ze, herformuleer met een punt of komma (Jeroen, 17-09-2026).

### Sjabloon connectieverzoek (max 300 tekens)
```
1. Hi [voornaam], a personal invite.
2. We're hosting an online, invite-only session with ALT and Jisc on the business outcomes of AI marking and feedback for institutions.
3. [waarom jij: hun rol plus, als het er is, het concrete detail uit het dossier]
4. [gesloten vraag: Worth the details? / Can I send you the details?]
```

### Sjabloon mail 1 (onderwerp plus ~110 woorden)
```
Hi [voornaam],

We're hosting an online, invite-only session with the Association for Learning Technology and Jisc on the business outcomes of AI marking and feedback for institutions, [wat het concreet betekent: kosten, consistentie, risico op institutioneel niveau, niet de losse beoordelaar].

I'm inviting you personally. [rol-redenering, verrijkt met het concrete dossierdetail als dat er is].

[Sluitzin over de exclusiviteit, bijvoorbeeld "It's by invitation rather than open registration." of "Registration is capped and by invitation."] Can I send you the details?

Best,
[naam]
```

### Sjabloon reminder (twee tot drie zinnen, maar opgemaakt als volledige e-mail)

**De reminder-stap in Lemlist is een e-mailstap, geen LinkedIn-bericht** (besluit Dante, 17-09-2026). Schrijf hem dus ook zo: aanhef op een eigen regel, de kern in een eigen alinea, de vraag apart, en een sign-off. Niet één dichtgetimmerde paragraaf van voornaam-tot-vraagteken, dat leest als een LinkedIn-bericht en is precies de fout die op 17-09-2026 gecorrigeerd is.
```
Hi [voornaam],

[schaarste: a few seats left / close to capacity]. [herhaling van de rol-redenering of het dossierdetail, in andere woorden].

[gesloten vraag]

Best,
[naam]
```
Geldt voor elke reminder die als los e-mailbericht verstuurd wordt, niet alleen voor deze campagne.

**Kalibratievoorbeelden nog niet vastgelegd.** Drie uitgewerkte voorbeelden (Nick Pape, Mike Walsh, Kelly Coate) zijn met Jeroen besproken op 17-09-2026, maar staan nergens in een bestand. Geef ze door zodat ik ze in dit skill-mapje vastleg (bijv. `voorbeelden-alt-webinar.md`), anders is de kalibratieset weg zodra dit gesprek sluit en herhaalt de volgende ronde dezelfde fouten die Jeroen er net uit haalde.

## Lees eerst de leerpunten

`LEERPUNTEN.md` in deze map is het geheugen tussen de rondes: wat er eerder is afgekeurd, waar in de keten het misging, en wat ermee gedaan is. Lees dat bestand voordat je begint te schrijven, niet achteraf.

Zonder dat bestand maak je elke ronde dezelfde fout opnieuw en krijgt Dante elke ronde dezelfde feedback te geven.

## Eerst: welke markt, welke taal

1. Noemt Dante geen markt, vraag het in één regel. Raad niet.
2. Geef `--markt <code>` mee bij elk commando, of zet `export SHIFT_MARKT=<code>`.
3. Lees `GTM/ICP/shift/markets/<code>/profiel.md`. Voor jou tellen **Taal en register** (taal, aanhef, toon, wat je niet zegt), **Klantnamen** (wat je als bewijs mag noemen, en of dat "geen" is), **Vaktermen** (de drager-toets in deze taal), **Kanaal** (welke stukken je oplevert), **Doorlooptijdnorm** en **Student-signaal** (waar in deze markt de organisatie-haakjes zitten) en **Seizoen** (of dit een goed moment is).

**Uitleg aan Dante in het Nederlands, elke zin die de prospect leest in de taal van de markt.** Hij moet hem kunnen oefenen en versturen zonder te vertalen. In een Engelstalige markt schrijf je dus Engels, en je hanteert de spelling en het register uit het profiel (VK: Britse spelling, "VLE" in plaats van "LMS", geen "I noticed", geen "reaching out").

## Pijplijn-modus

Roept Dante deze skill aan zonder een specifieke persoon te noemen, dan werk je een wachtrij af. De keten is: `lead-sourcing` → `contact-sourcing` → `shift-research` → deze skill → `lemlist-import`.

Alles staat in het master-document, dat je alleen via `pipeline.py` aanraakt. Je schrijft met `--actor outreach`; het script bewaakt zelf welke velden van jou zijn. Twijfel je over een veldnaam: `pipeline.py uitleg <veld>`.

### Je wachtrij

```bash
python3 .claude/scripts/pipeline.py --markt <code> queue --stage 4 --limit 15
```

Je krijgt alleen mensen met een haakje op niveau 2, 2b of 3 die nog geen bericht hebben. Is de wachtrij leeg, zeg dat en stop. Ga niet zelf haakjes zoeken, dat is agent 3.

### Het onderzoek zit in het dossier, niet in de wachtrij

De velden `opvallend`, `haakje`, `toetsprogramma` en `schrijfwerk` zijn **samenvattingen van 200 tekens**. Het echte onderzoek staat in het dossier, en dat is wat je leest voor je schrijft.

```bash
pipeline.py dossier <person_id>                    het hele dossier
pipeline.py dossier <person_id> --sectie Citaten   alleen de citaten
```

**Lees het dossier van persoon N vlak voordat je zijn bericht schrijft, niet de hele batch vooraf.** Staat er geen dossier (`dossier_pad` leeg), dan is het record niet af: terug naar agent 3, niet zelf gaan zoeken.

### Alleen schrijven uit een AFGEMAAKTE rij (verplichte poort, 2026-08-07)

Check in het dossier (`--sectie Toetsprogramma`) dat er een **bevestigd toetsprogramma en schrijfwerk** ligt. Staat daar iets als *"niet gespecificeerd"*, *"not stated"*, *"onbekend"*, of is er geen dossier → het record is **niet af**. Dan:

- **Niet zelf gaan web-searchen** om het gat te vullen. Dat is agent 3.
- **Niet gokken.** Een schrijfwerk-veld invullen dat de bron niet noemt is dezelfde fout als een citaat verzinnen (Noortje-geval: "masteropdrachten" gegokt, bleek een casestudy met presentatie).
- **Terug naar agent 3** met een specifieke vraag.

**Datum-toets bij een why-now.** Zeg nooit "net", "recent", "just", "newly" zonder de datum te checken. Een aanstelling van meer dan ~6 maanden geleden is geen why-now.

De niveau-1-gevallen schrijf je **niet**. Die verzamel je en leg je aan het eind van de batch aan Dante voor, volgens `haakje-zoeken.md`.

### Wat je wegschrijft

```bash
python3 .claude/scripts/pipeline.py --markt <code> set p_xxx --actor outreach \
  --set connectieverzoek="..." \
  --set opvolgmail_onderwerp="..." \
  --set opvolgmail="..." \
  --set reminder="..." \
  --set waarom_dit_bericht="welke insteek gekozen en waarom, welke toetsen toegepast" \
  --set afgevallen_openers="opener A: reden; opener B: reden" \
  --set twijfels="..." \
  --set bericht_status=concept
```

`bericht_status` blijft `concept` tot Dante hem goedkeurt. Het script weigert een connectieverzoek boven de 300.

**`waarom_dit_bericht` is verplicht.** Dat blok komt letterlijk op Dante's reviewkaart: welke insteek, waarom die en niet de andere, welke toetsen (drager-toets, omkeertoets, klantnaam-keuze). `doctor` waarschuwt bij elk bericht zonder dat veld.

**Schrijf de berichten ook terug in het dossier**, kop `Berichten`:

```bash
pipeline.py dossier p_xxx --sectie Berichten --schrijf - --actor outreach << 'EOT'
**Connectieverzoek 2026-09-10** (289 tekens)
...
**Mail 1** onderwerp: ...
...
**Reminder**
...
**Waarom deze insteek**: welk citaat, welke drager, welke toets doorstaan.
**Afgevallen**: opener A: reden. Opener B: reden.
EOT
```

**Twijfel je, schrijf dat op in `twijfels`.** Wat je niet zeker weet in één zin, en wat Dante zou moeten checken om het op te lossen.

### Tempo
Batches van 10 tot 15 personen. Rapporteer pas aan het eind van een batch, en lever de berichten in de chat zodat Dante ze kan lezen zonder een bestand te openen.

## Lees eerst

- `voorbeelden-dante.md` in deze map. Dante's echte berichten, Engels en Nederlands, met warmte-label. Dat is de lat, niet je eigen smaak. Het Ken-bericht (Engels, koud, kreeg reactie) is het model voor een Engelstalige markt.
- `haakje-zoeken.md` in deze map. De originaliteitsladder, waar je zoekt, en wanneer je stopt.
- `schrijven` voor de stem.
- `Platform/product.md`: de enige bron voor wat je over Eduface beweert.

## De loop

```
1. CHECK      is dit echt koud? Close + Gmail op persoon en organisatie, en de 2-wekenregel
2. MATERIAAL  ruwe observaties uit het dossier, alles met citaat en drager
3. REAGEREN   vijf lenzen langs, vijf openers schrijven, er een kiezen
4. GATE       staat er iets in wat je VINDT? alleen feiten -> terug naar 3
5. SCHRIJVEN  invite, mail 1, reminder; elk door de brontoets
6. LEVEREN    aan Dante, met de bron, de redenering en de afgevallen openers
```

**Stap 3 is de kern van deze skill.** Het is verleidelijk om het eerste feit netjes op te schrijven. Doe dat niet. In een kleine markt kost een middelmatig bericht je de enige persoon die je bij die organisatie hebt.

## Stap 1: is het echt koud?

Doorzoek Close en Gmail op de persoon **en** op de organisatie. Zit er al contact, dan is dit geen koude outreach.

**Twee harde regels (Dante, 2026-08-12):**

1. **Loopt er al een cold call bij deze organisatie of persoon, dan schrijf je geen bericht.** Zet `--set bericht_status=vervallen --set bericht_status_toelichting="lopende cold call bij [org] ([naam], [datum]), Dante benadert zelf"`.
2. **Is er al een andere persoon bij dezelfde organisatie benaderd, wacht dan minimaal 2 weken vanaf die verzenddatum.** Kijk ook naar de moeder en naar andere markten, want een concern is één organisatie:

```bash
python3 .claude/scripts/pipeline.py show org_xxx
```

Staat daar een datum binnen twee weken: schrijf het bericht wel, maar zet `bericht_status=gepauzeerd` met `gepauzeerd_tot` en de reden in de toelichting.

## Stap 2: materiaal, geen conclusies

Alles komt uit het dossier. De zoekvolgorde die agent 3 volgde staat in `haakje-zoeken.md`. **Verzamel losse observaties, geen afgeronde haakje-zin.** Een afgeronde zin is al een conclusie, en op een conclusie valt niets meer te reageren.

Krijg je van agent 3 tóch een uitgeschreven haakje (het veld `haakje`), behandel dat als één observatie tussen de andere en ga naar de citaten in het dossier.

## Stap 3: reageren, en dit is waar het bericht ontstaat

**Een feit is geen haakje. Jouw reactie op dat feit is het haakje.** "Students write a research report" is saai. "That surprised me at a performing-arts school" is een mens. Zelfde feit.

Beantwoord eerst één vraag, hardop: **wat is hier raar, verrassend of grappig aan?** Niets? Dan is het materiaal saai en ga je terug naar stap 2.

### De vijf lenzen

| Lens | Wat je zoekt | Voorbeeld |
|---|---|---|
| **Tegenstelling** | X terwijl Y | een creatieve opleiding die laat schrijven; een opleider die AI doceert en zelf met de hand nakijkt; een school die anderen leert toetsen |
| **Verrassing** | dit had ik hier niet verwacht | een onderzoeksverslag bij een stylingopleiding |
| **Het getal** | een aantal dat blijft hangen | 12 reflectieverslagen per student per jaar; een 15-day feedback turnaround naast 35.000 studenten |
| **Herkenning** | dat probleem kennen wij ook | en dan geef je er iets van jezelf bij weg |
| **Eerlijke non-sequitur** | iets menselijks van hun profiel | de hond op Kens banner, meteen toegeven dat het er niks mee te maken heeft |

### Vijf openers, er één houden

Schrijf per persoon **vijf openers vanuit vijf lenzen**, nog zonder je aan de 300 tekens te houden. Kies daarna. De selectievraag is niet "welke is correct" maar **welke zou ik zelf openen als ik die persoon was**. De afgevallen vier lever je mee aan Dante, want hij kiest regelmatig een andere.

## Stap 4: de levendheidsgate

**Staat er in de eerste twee zinnen iets wat je vindt, of alleen wat je hebt gelezen?** Alleen constateringen, dan terug naar stap 3.

Daarnaast blijft de originaliteitsgate uit `haakje-zoeken.md` gelden: niet boven niveau 1, dan niet schrijven maar voorleggen.

Gebruik **één** haakje per stuk. Alles met bron en letterlijk citaat (`claims-need-sources`).

## Stap 5: schrijven

### Eerst: de brontoets (verplicht, voor je één woord schrijft)

Op 2026-07-23 ging er een bericht bijna de deur uit waarin stond dat iemand reflectief vermogen opbouwt "door te schrijven en herschrijven met feedback". Het woord feedback kwam in zijn hele stuk niet voor. Het was erin geslopen omdat het naar Eduface leidt.

**De brontoets geldt twee kanten op, ook op wat je over Eduface beweert.** Het product staat in `Platform/product.md`. Staat een functie daar niet, dan noem je hem niet.

**Vertrouw de citaten, vertrouw de interpretatie niet.** Wat onder `## Citaten` staat is letterlijk, met vindplaats, datum en drager. Dat neem je aan. Het veld `haakje` en alles wat naar een conclusie riekt neem je **niet** aan. Mist er iets, dan is dat een gat in het dossier: terug naar agent 3.

Leg elke inhoudelijke bewering naast de brontekst en label hem **FEIT** (staat er letterlijk) of **GEVOLG** (jouw gevolgtrekking, toegestaan als elk feit eronder in de bron staat én je geen nieuw begrip introduceert). Vier controles:

1. **Woordtoets.** Elk zelfstandig naamwoord dat de kern van je haakje draagt: staat dat woord, of een echt synoniem, in de bron? Zo niet, schrappen.
2. **Tegenspraaktoets.** Spreekt de bron je gevolg ergens tegen? Een gevolg dat de bron tegenspreekt is geen zwak haakje, het is een verkeerd haakje (Marrewijk: "weinig tijd" terwijl hij schreef dat ze op tijd inleverden).
3. **Omkeertoets, op de brug naar Eduface.** Vervang het detail waarop je haakt door een ander detail dat in dezelfde situatie had gekund. Klopt je zin dan nog, dan is de brug vals.
4. **Drager-toets, wie draagt de last.** Schrijf op wie in de **bron** de last draagt (student, beoordelaar, organisatie, panel) en wie in **jouw zin**. Niet dezelfde? Dan is je haakje ongeldig, ook als elk woord in de bron staat. Eduface neemt werk weg bij de **beoordelaar**. De enige legitieme brug is een **apart feit uit de bron over de beoordelaarskant**; twee citaten dus, niet één citaat en een aanname. **Heb je dat tweede citaat niet, stel dan de vraag in plaats van de aanname te doen.**

   Vaktermen hebben een vaste drager en lees je nooit als gewone taal. De tabel voor deze markt staat in het profiel onder **Vaktermen** (NL: studeerbaarheid = student; VK: "assessment load" is ambigu, "marking load" = marker, "feedback literacy" = student).

   > **Wat er misging (THIM, 13-08-2026).** Het NVAO-rapport beveelt aan "te blijven waken over de studeerbaarheid, met het oog op de vele herhalingsactiviteiten, feedbackmomenten en toetsen". De mail maakte daarvan "een flinke klus voor de docenten". Woordtoets, tegenspraaktoets en omkeertoets gaven groen. Toch fout: studeerbaarheid gaat over de **student**. Thim wees de mail af met precies dat verschil.

Komt je haakje deze toets niet door, val dan terug op een feit dat er wél staat, ook als het minder mooi aansluit. Een waar en saaier haakje verslaat altijd een mooi en verzonnen haakje.

#### Een LinkedIn-profiel lezen: structuur is betekenis

- **Een skill-tag is geen functie.** Nooit lezen als een vorige baan.
- **Datums bepalen wat verleden is.** Alleen een functie met een einddatum is verleden.
- **Volgorde van betrouwbaarheid:** functietitel + datums, dan headline, dan about, dan de beschrijving onder een rol, dan skill-tags.

### Het connectieverzoek (max 300 tekens)

**Er is geen sjabloon.** Wat de goedgekeurde berichten delen is een ritme:

```
1. Hi [voornaam], ik las / I read [hun woorden of een feit uit hun materiaal]
2. [WAT JIJ ERVAN VINDT]              <- de stap die een model steeds overslaat
3. [wie wij zijn, vastgemaakt aan die reactie, met bewijs als het profiel dat toestaat]
4. [een RELEVANTE OPEN VRAAG]
```

**Stap 4 is altijd een open vraag, nooit een ja/nee-slot** (Dante, 2026-08-07). Dus niet "Interested?", "Worth a chat?", "Ook iets voor jullie?". Een vraag met hoe/wat/wie/hoeveel die aansluit op wat je aanhaalde: "How do you handle that at the moment?", "Which part of the marking takes your tutors the most time?", "Wat waren de resultaten?".

**De opening:** de aanhef uit het profiel (NL: "Hi [voornaam]", VK: "Hi [first name]"). Openen met "ik las" / "je schreef" / "I read" / "you wrote". Geen aanloopje, geen "wat me opviel", geen "I noticed" (`no-opviel-filler-openers`).

**De waarde.** Zeg concreet wat Eduface doet: **docenten ondersteunen bij het nakijken en feedback geven op studentopdrachten**, in de woorden van de markt. Wat vastligt is de claim, niet de woorden: de lezer weet na afloop wat Eduface doet, het klopt inhoudelijk (formatieve feedback op schrijfopdrachten, nooit "sneller nakijken"), geen harde belofte over uitval, alleen functies uit `Platform/product.md`. Twee toetsen: de **uitwisseltoets** (past je waarde-zin ook in het bericht van iemand anders bij dezelfde organisatie? dan is het een sjabloon) en de **echo-toets** (bevat de waarde-zin minstens één woord uit het haakje?).

**De pijn hoort niet in het connectieverzoek** (Dante, 2026-07-23). Bewaar die voor het gesprek.

**Klantnamen als bewijs** komen uit het profiel, kop **Klantnamen**. Staat daar "geen", dan noem je er geen en bouw je het bewijs anders (een verifieerbaar feit over ons, zoals het Jisc-framework in het Ken-bericht, mits dat in `Platform/product.md` of het profiel staat). Staat er een lijst, dan kies je de naam die het dichtst bij deze persoon staat (waar hij studeerde, waar hij woont; agent 3 noteert dat onder `## Persoon`). Onze klanten en partners noem je voluit; de organisatie van de ontvanger kort je af naar de vorm die ze zelf voeren.

**Het slot.** Twee vormen: zit de persoon hoog in de boom en kan hij het doorschuiven, dan de doorverwijsvraag ("Do you know who looks after this? I couldn't quite work out who that was myself."). Is hij aantoonbaar zelf de juiste, dan de uitnodiging. Vraag nooit om tijd of een meeting in het verzoek. **Benoem iemands functie niet in het bericht.**

**Humor en verbazing.** Verbazing over iets interessants werkt, spot met hun keuzes niet. Check of een label dat je gebruikt door henzelf gedragen wordt (Artemis: "geen kunstacademie").

**Het moet klinken als een mens.** Lees het hardop. Hele, lopende zinnen, geen telegramstijl. Zacht formuleren waar het kan. De regel "bondig, geen opsmuk" geldt voor hoe je met Dante praat, niet voor outreach.

**Het VLE/LMS is bijna nooit een haakje.** Alleen bij oprechte interesse in hún systeem, bij naam. Som nooit op waar we mee integreren.

**Vorm.** Kort is beter dan richting de 300. Geen getallen van hun website (vaak verouderd). Eén haakje.

### Mail 1 (onderwerp plus ~110 woorden)

Herzien 2026-08-12 en 2026-08-21: korter en minder precies dan het onderzoek. **De precisie van het onderzoek is de AI-tell.** Geen datums en cijfers als bewijs opgestapeld, één haakje, gesloten CTA.

```
Hi [voornaam],

[Een specifiek detail uit de bron, in gewone taal, zonder datumbombardement.] [Een eerlijke, voorstelbare consequentie, geen verzonnen pijnwoord.] Daarom stuurde ik je een connectieverzoek / That's why I sent you a connection request.

[Eén alinea over ons, in de woorden van het profiel: wat we doen, met of zonder klantnaam volgens kop Klantnamen.]

[Een concrete, gesloten vraag die voortbouwt op het detail.]

[Afsluiting uit het profiel]
Dante Torbed
Eduface
```

**Sign-off is altijd "Best,\nDante Torbed\nEduface", nooit een functietitel erbij** (besluit Dante, 17-09-2026). Geen "Customer success manager" of iets anders tussen naam en bedrijfsnaam, in geen enkele e-mail in deze skill.

- **Invite en mail mogen niet dezelfde zin gebruiken.** Ze komen binnen twee dagen bij dezelfde persoon binnen. Gebruik in de mail een ander, dieper detail uit dezelfde bron, of dezelfde observatie in andere woorden.
- Het onderwerp: een paar woorden uit de bron zelf, geen clickbait, geen generiek "Question about...".
- Zelfde brontoets en dragertoets als het verzoek.

### De reminder (twee tot drie zinnen)

Gaat als reply in dezelfde thread, dus zonder onderwerp en zonder de context te herhalen. Eén nieuw element (een ander detail, of de vraag anders gesteld), en één vraag. Geen "just checking in", geen "bumping this". Toon uit het profiel.

**Is het kanaal e-mail, dan is dit een e-mail, geen LinkedIn-bericht** (besluit Dante, 17-09-2026). Aanhef op een eigen regel, de inhoud in een eigen alinea, de vraag apart, sign-off eronder. Nooit alles in één dichtgetimmerde paragraaf proppen, ook al is de tekst zelf kort. Zie het sjabloon onder "Huidige campagne" hierboven voor het exacte format.

## Niet-onderhandelbaar

- **Geen enkel woord dat niet uit de bron komt.** Introduceer nooit een begrip (feedback, nakijklast, marking load, tijdsdruk) dat de persoon zelf niet noemde.
- **Nooit meer lezing claimen dan je hebt gedaan.**
- **Altijd eerlijk over hoe je bij iemand kwam.**
- **Nooit zeggen dat je je in een persoon hebt verdiept.** In een organisatie mag wel.
- **Geen AI-tells, geen lege verbindingszinnen, geen em-dashes.** Gewone spreektaal (`outreach-plain-language`). De verboden woorden van de markt staan in het profiel.
- **Uitnodigend, niet sturend** (`mails-friendly-not-directive`).
- **Verzin nooit een persoonlijk feit.**
- **Schrijf nooit marktkennis in deze skill.** Een nieuwe aanhef, een woord dat in deze markt verkeerd valt: dat hoort in het profiel.

## Stap 6: oplevering aan Dante

Per persoon, in deze vorm. **Nooit alleen het bericht opleveren** (Dante, 2026-08-07):

- **Naam, functie, organisatie, LinkedIn-link**
- **Waar ik het op baseer**: het haakje met niveau, **letterlijk citaat en bron-URL**, met de drager.
- **Waarom ik het zo schrijf**: waarom dit haakje de reactie is en geen kaal feit, welke klantnaam of welk bewijs je koos en waarom, welke toetsen je deed.
- **Afgevallen openers**, één regel elk met reden.
- **Connectieverzoek** met tekenaantal, **mail 1** met onderwerp, **reminder**. Alle drie in de taal van de markt.
- **Twijfels**, expliciet.

Bij een lijst: lever in batches, niet alles in één keer.

## Done

- Close en Gmail gecheckt, persoon is aantoonbaar koud; 2-wekenregel gecheckt op de organisatie én de moeder.
- Haakje op niveau 2 of hoger, met letterlijk citaat, bron en drager. Anders voorgelegd.
- Eén haakje per stuk; invite en mail delen geen zin.
- Verzoek onder de 300 tekens, tekenaantal erbij; mail rond de 110 woorden; reminder twee tot drie zinnen.
- Elk stuk eindigt op een vraag die deze persoon vanuit zijn rol kan beantwoorden.
- Alles in de taal van het profiel, uitleg in het Nederlands.
- `waarom_dit_bericht`, `afgevallen_openers` en `twijfels` gevuld, dossier-kop `Berichten` bijgewerkt.
