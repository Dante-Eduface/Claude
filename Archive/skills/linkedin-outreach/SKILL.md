---
name: linkedin-outreach
description: VERVANGEN op 2026-09-10 door `outreach`, die het marktprofiel leest (projects/shift/markets/<code>/) en voor elke markt werkt. Gebruik `outreach` met --markt nl voor NL-werk. Dit bestand blijft alleen staan zodat lopende chats en journaalregels niet breken.
---

> **Deze skill is vervangen.** Gebruik **`outreach`** (`.claude/skills/outreach/SKILL.md`), met `--markt nl`. Sinds 10-09-2026 is de markt een variabele: de skills zijn marktloos en alle NL-kennis staat in `projects/shift/markets/nl/profiel.md`. De inhoud hieronder is de NL-versie van vóór die datum en wordt niet meer bijgewerkt.


# LinkedIn Outreach (koud)

Dante's outreachkanaal voor de NL-markt is LinkedIn, niet mail. Elk contact krijgt een handgemaakt bericht, want de markt is klein en er is geen tweede lane om achter te schuilen.

Er worden twee dingen opgeleverd per persoon: het **connectieverzoek** van maximaal 300 tekens (met de vraag er al in) én de **opvolgmail** die verstuurd wordt zodra iemand het verzoek accepteert. Het oude besluit om geen opvolgbericht te schrijven (Dante, 2026-07-23) is **niet meer geldig** (herzien 2026-08-12): elk connectieverzoek krijgt nu standaard een opvolgmail erbij, klaar om in Lemlist te zetten.

Dit is Dante's werk tot de Discovery-gate (`scope-discovery-gate`). Daarna hand-off naar Jeroen.

**Voor mails is dit niet de skill.** Gebruik `targeted-outreach`. Deze skill is specifiek voor koud LinkedIn.

## Pijplijn-modus: als Agent 4 in een eigen chat

Roept Dante deze skill aan zonder een specifieke persoon te noemen, dan ben je **Agent 4** van de NL-opleiderspijplijn en werk je een wachtrij af. De keten is: `/lead-sourcing-nl` → `/contact-sourcing-nl` → `shift-research` → deze skill.

Alles staat in het master-document, dat je alleen via `pipeline.py` aanraakt. Je schrijft met `--actor linkedin-outreach`; het script bewaakt zelf welke velden van jou zijn. Twijfel je over een veldnaam of een waarde: `pipeline.py uitleg <veld>`.

### Je wachtrij

```bash
python3 .claude/scripts/pipeline.py queue --stage 4 --limit 15
```

Je krijgt alleen mensen met een haakje op niveau 2, 2b of 3 die nog geen bericht hebben. Niveau 1, al benaderde mensen, geblokkeerde organisaties en tweede kandidaten komen er niet in. Is de wachtrij leeg, zeg dat en stop. Ga niet zelf haakjes zoeken, dat is Agent 3.

Wil je zien wat er op niveau 1 ligt om aan Dante voor te leggen:
```bash
pipeline.py queue --stage 4 --fields person_id,naam,haakje_niveau --limit 0
pipeline.py show <person_id> --full
```

### Het onderzoek zit in het dossier, niet in de wachtrij

De velden `opvallend`, `haakje`, `toetsprogramma` en `schrijfwerk` die je in de wachtrij ziet zijn **samenvattingen van 200 tekens**. Het echte onderzoek van Agent 3 staat in een dossier per persoon, en dat is wat je leest voor je schrijft.

```bash
pipeline.py dossier <person_id>                    het hele dossier
pipeline.py dossier <person_id> --sectie Citaten   alleen de citaten
```

**Lees het dossier van persoon N vlak voordat je zijn bericht schrijft, niet de hele batch vooraf.** Zo blijft je context gelijk of je nu 5 of 15 mensen doet. Heb je alleen een opening nodig, dan is `--sectie Citaten` genoeg; `--sectie Onzekerheden` erbij als je twijfelt of iets wel hard is.

Staat er geen dossier (`dossier_pad` leeg in de wachtrij), dan is het record niet af. Zelfde route als hieronder: terug naar Agent 3, niet zelf gaan zoeken.

### Alleen schrijven uit een AFGEMAAKTE rij (verplichte poort, 2026-08-07)

Voor je een bericht schrijft: check in het dossier (`--sectie Toetsprogramma`) dat er een **bevestigd toetsprogramma en schrijfwerk** ligt. Staat daar of in de samenvatting iets als *"niet gespecificeerd"*, *"niet in deze bron"*, *"niet publiek"*, *"onbekend"*, of is er helemaal geen dossier → het record is **niet af**. Dan:

- **Niet zelf gaan web-searchen** om het gat te vullen. Dat is Agent 3's werk, niet dat van Agent 4. (Vastgesteld met Dante 2026-08-07: Agent 4 haalt alles uit Agent 3's onderzoek; als dat niet kan, is de rij het probleem, niet jouw zoekopdracht.)
- **Niet gokken.** Een schrijfwerk-veld invullen dat de bron niet noemt is dezelfde fout als een citaat verzinnen (Noortje-geval: "masteropdrachten" gegokt, bleek een casestudy met presentatie).
- **Terug naar Agent 3** met een specifieke vraag: open de curriculum-/toets-/OER-pagina en leg vast wat lerenden inleveren, hoeveel, wie nakijkt, met letterlijk citaat.

Zonder hard toetsprogramma kun je geen gegrond bericht maken. Zie `toetsprogramma-eerst`, `one-row-per-person`, `deep-research-before-agent4`.

**Datum-toets bij een why-now.** Zeg nooit "net", "recent", "pas aangetreden" zonder de datum te checken. Staat er alleen "per 1 juni" zonder jaar, dan weet je het niet. Een aanstelling van meer dan ~6 maanden geleden is geen why-now (Noortje: directeur sinds juni 2025, ruim een jaar, dus "net" was fout).

De niveau-1-gevallen schrijf je **niet**. Die verzamel je en leg je aan het eind van de batch aan Dante voor, volgens het protocol in `haakje-zoeken.md`.

### Wat je wegschrijft

```bash
python3 .claude/scripts/pipeline.py set p_xxx --actor linkedin-outreach \
  --set connectieverzoek="..." \
  --set opvolgmail_onderwerp="..." \
  --set opvolgmail="..." \
  --set waarom_dit_bericht="welke insteek gekozen en waarom die, welke toets toegepast" \
  --set afgevallen_openers="opener A: reden; opener B: reden" \
  --set twijfels="..." \
  --set bericht_status=concept
```

`bericht_status` blijft `concept` tot Dante hem goedkeurt. Je hoeft geen tekens te tellen: het script weigert een connectieverzoek boven de 300.

**`waarom_dit_bericht` is verplicht.** Dat blok komt letterlijk op Dante's reviewkaart te staan: welke insteek je koos, waarom die en niet de andere, welke toetsen je hebt toegepast (drager-toets, omkeertoets, alma-mater). `doctor` geeft een waarschuwing bij elk bericht zonder dat veld of zonder `haakje_bron_url`.

**Schrijf het bericht ook terug in het dossier**, zodat de volgende ronde ziet wat er al geprobeerd is en waarom:

```bash
pipeline.py dossier p_xxx --sectie Berichten --schrijf - --actor linkedin-outreach << 'EOF'
**Connectieverzoek 2026-08-14** (289 tekens)
...

**Waarom deze insteek** — welk citaat, welke drager, welke toets doorstaan.
**Afgevallen** — opener A: reden. Opener B: reden.
EOF
```

Alleen die kop wordt vervangen, de rest van het dossier blijft staan.

**Twijfel je, schrijf dat op in `twijfels`.** Dat is geen zwakte, het is precies wat Dante wil zien. Zet erin: wat je niet zeker weet in één zin, en wat hij zou moeten checken om het op te lossen (welke pagina, welk profiel), zodat hij weet of het twee minuten of twintig minuten werk is. Kun je niet kiezen tussen twee insteken, zet ze er dan allebei in met hun bron, dan kiest hij.

### Tempo
Batches van 10 tot 15 personen. Rapporteer pas aan het eind van een batch, en lever de berichten in de chat zodat Dante ze kan lezen zonder een bestand te openen.

## Lees eerst

- `voorbeelden-dante.md` in deze map. Dante's echte berichten met warmte-label. Dat is de lat, niet mijn eigen smaak.
- `haakje-zoeken.md` in deze map. De originaliteitsladder, waar je zoekt, en wanneer je stopt.
- `content-voice` voor de stem, en het type LinkedIn connectieverzoek daarbinnen.
- `cro-of-eduface` voor de sales-logica als de context onduidelijk is.

## De loop

```
1. CHECK      is dit echt koud? Close + Gmail op persoon en organisatie
2. MATERIAAL  ruwe observaties verzamelen uit de bron, alles met citaat
3. REAGEREN   vijf lenzen langs, vijf openers schrijven, er een kiezen
4. GATE       staat er iets in wat je VINDT? alleen feiten -> terug naar 3
5. SCHRIJVEN  het verzoek afmaken, max 300 tekens
6. LEVEREN    aan Dante, met de bron en de afgevallen openers erbij
```

**Stap 3 is de kern van deze skill.** Daar ontstaat het bericht. Het is verleidelijk om onder momentum het eerste feit dat je vindt netjes op te schrijven. Doe dat niet. In een kleine markt kost een middelmatig bericht je de enige persoon die je bij die organisatie hebt.

## Stap 1: is het echt koud?

Doorzoek Close en Gmail op de persoon **en** op de organisatie en collega's. Zit er al contact, dan is dit geen koude outreach en hoort het bericht ergens anders thuis. Zie `person-research` voor de CRM-check. Iemand koud benaderen die al in een lopende relatie zit is de duurste fout die er is.

**Twee harde regels, vastgesteld met Dante 2026-08-12:**

1. **Loopt er al een cold call bij deze organisatie of persoon (bijv. een voicemail, een belpoging), dan schrijf je geen LinkedIn-verzoek.** Dante benadert die persoon dan zelf via het andere kanaal met een eigen bericht. Zet dan `--set bericht_status=vervallen --set bericht_status_toelichting="lopende cold call bij [org] ([naam contact], [datum]), Dante benadert zelf"` in plaats van een connectieverzoek te schrijven.
2. **Is er al een andere persoon bij dezelfde organisatie benaderd, wacht dan minimaal 2 weken vanaf die verzenddatum.** Twee mensen bij één org kort na elkaar valt op als campagne.

Beide checks doe je bij **elke** persoon vóór je schrijft, niet achteraf. De organisatiecheck is één commando:

```bash
python3 .claude/scripts/pipeline.py show org_xxx
```

Dat geeft iedereen bij die organisatie met hun rol, hun `bericht_status` en hun `verzonden_linkedin`. Staat daar een datum binnen twee weken, dan:

```bash
pipeline.py set p_xxx --actor linkedin-outreach \
  --set bericht_status=gepauzeerd \
  --set gepauzeerd_tot=2026-08-26 \
  --set bericht_status_toelichting="[naam eerste contact] bij dezelfde organisatie benaderd op [datum], 2-wekenregel"
```

Schrijf het bericht wel, want dan ligt het klaar. Is de twee weken al om, zet dan in `waarom_dit_bericht` welke eerdere verzending je hebt gecheckt en op welke datum, zodat de redenering zichtbaar blijft.

Zoek daarnaast in Close en Gmail op lopende cold-call-activiteit.

## Stap 2: materiaal, geen conclusies

Zoekvolgorde staat in `haakje-zoeken.md`: hun eigen LinkedIn-profiel → wat ze het afgelopen jaar deelden → **de onderwijsvisie of het onderwijsconcept van de organisatie** → iets wat net veranderde bij de organisatie → hun toets- en examenmateriaal.

**Zoek altijd de onderwijsvisie op** (toegevoegd 2026-07-24). Veel opleiders publiceren een onderwijsvisie of onderwijsconcept waarin ze in hun eigen woorden zeggen hoe ze naar leren en beoordelen kijken. Dat sluit verrassend vaak recht op Eduface aan en is dan een sterk, goed te citeren haakje. De ASRE-onderwijsvisie zet bijvoorbeeld letterlijk formatieve toetsing met de nadruk op feedback centraal. Zoektermen: `"<organisatie>" onderwijsvisie`, `onderwijsconcept`, `visie op toetsing`.

**Verzamel losse observaties, geen afgeronde haakje-zin.** Citaten, getallen, rare details, dingen die niet bij elkaar lijken te passen. Ongefilterd, alles met bron. Een afgeronde haakje-zin is al een conclusie, en op een conclusie valt niets meer te reageren. Dat is precies waarom het voorgekauwde haakje van Agent 3 leidt tot nette, dode berichten.

Krijg je van Agent 3 tóch een uitgeschreven haakje, behandel dat als één observatie tussen de andere en ga zelf terug naar de bron.

## Stap 3: reageren, en dit is waar het bericht ontstaat

**Een feit is geen haakje. Jouw reactie op dat feit is het haakje.** "Studenten schrijven een onderzoeksverslag" is saai. "Dat verraste me bij jullie creatieve opleidingen" is een mens. Zelfde feit.

Beantwoord daarom eerst één vraag, hardop: **wat is hier raar, verrassend of grappig aan?** Kun je daar niets op zeggen, dan is het materiaal saai en ga je terug naar stap 2.

### De vijf lenzen

Loop ze alle vijf langs. Vaag advies als "wees creatief" levert niets op, een lijstje wel.

| Lens | Wat je zoekt | Voorbeeld |
|---|---|---|
| **Tegenstelling** | X terwijl Y | een creatieve opleiding die laat schrijven; een opleider die AI doceert en zelf met de hand nakijkt; een school die anderen leert toetsen |
| **Verrassing** | dit had ik hier niet verwacht | een onderzoeksverslag bij een stylingopleiding |
| **Het getal** | een aantal dat blijft hangen | 12 reflectieverslagen per student per jaar, 250 freelance examinatoren |
| **Herkenning** | dat probleem kennen wij ook | en dan geef je er iets van jezelf bij weg |
| **Eerlijke non-sequitur** | iets menselijks van hun profiel | de hond op Kens banner, meteen toegeven dat het er niks mee te maken heeft |

### Vijf openers, er één houden

Schrijf per persoon **vijf openers vanuit vijf lenzen**, nog zonder je aan de 300 tekens te houden. Kies daarna. De selectievraag is niet "welke is correct" maar **welke zou ik zelf openen als ik Femke was**.

Dit is geen kwestie van beter je best doen, het is volume plus selectie. Één opener schrijven en die oppoetsen levert altijd het nette, dode bericht op. De afgevallen vier lever je mee aan Dante, want hij kiest regelmatig een andere.

### Wat humor betreft

Zie de sectie hieronder. Verbazing en een lichte grap werken, spot met hun keuzes niet, en check of een label dat je gebruikt door henzelf gedragen wordt.

## Stap 4: de levendheidsgate

**Staat er in de eerste twee zinnen iets wat je vindt, of alleen wat je hebt gelezen?**

Alleen constateringen, dan terug naar stap 3. Deze toets vangt precies het patroon dat drie berichten lang misging: feit, feit, feit, en dan een aanbod. Correct en volstrekt vergeetbaar.

Daarnaast blijft de originaliteitsgate uit `haakje-zoeken.md` gelden: kom je niet boven niveau 1 (citeren en dan pitchen) uit, dan schrijf je niets en leg je het aan Dante voor. Twintig goede berichten en tien voorgelegde twijfelgevallen is beter dan dertig waarvan tien slap zijn.

Gebruik **één** haakje in het verzoek. Een tweede is ruis in 300 tekens. Alles met bron en letterlijk citaat, zie `claims-need-sources`.

## Stap 5: schrijven

### Eerst: de brontoets (verplicht, voor je één woord schrijft)

Dit is de belangrijkste stap in de hele skill, en de reden dat hij bestaat: op 2026-07-23 ging er een bericht de deur bijna uit waarin stond dat iemand reflectief vermogen opbouwt "door te schrijven en herschrijven met feedback". Het woord feedback kwam in zijn hele stuk niet voor. Het was erin geslopen omdat het naar Eduface leidt, niet omdat hij het zei.

**De brontoets geldt twee kanten op, ook op wat je over Eduface zelf beweert.** Het product staat in `references/eduface-product.md` (AI Feedback, AI Paper Grader, AI Exam Grader, Oral Examination beta). Staat een functie daar niet, dan noem je hem niet, ook niet als hij perfect op de pijn van deze prospect aansluit. Juist dán verzin je hem.

**Kun je een bron niet lezen, dan is dat een gat, geen bewijs dat hij leeg is.** Een afbeelding-PDF of een pagina die niet rendert lijkt leeg maar kan juist het beste haakje bevatten (ASRE's onderwijsvisie, 2026-07-24: onleesbaar via de tool, maar met de hele Eduface-these erin). Meld "niet te lezen" als onzekerheid en vraag Dante de bron te sturen, precies zoals bij een profiel achter een loginmuur.

**Vertrouw de citaten, vertrouw de interpretatie niet.** Herzien 14-08-2026, want de oude regel ("open altijd zelf de bron") botste met de regel dat je niet zelf mag web-searchen. Die twee kunnen alleen samen als het dossier compleet is, en dat is nu de opzet.

- Wat onder `## Citaten` staat is letterlijk, met vindplaats, datum en drager. Dat neem je aan. Agent 3 had de bron open, jij niet.
- Het veld `haakje` en alles wat naar een conclusie riekt neem je **niet** aan. Daar zit de aanname al in, en Agent 3 trekt consequenties die niet altijd gegrond zijn.
- Mist er iets wat je echt nodig hebt, dan is dat een gat in het dossier. Terug naar Agent 3 met een specifieke vraag, niet zelf gaan zoeken.
- Alleen als een citaat je niet klopt (een woord dat te mooi aansluit, een drager die je niet gelooft) haal je die ene bron er alsnog bij. Meld dat dan in `twijfels`.

Leg dan elke inhoudelijke bewering in je concept naast de brontekst en label hem:

- **FEIT** = staat er letterlijk, of is een directe parafrase zonder nieuwe inhoud. Alleen dit mag je als hun woorden presenteren.
- **GEVOLG** = jouw gevolgtrekking. Toegestaan, maar alleen als **elk feit eronder in de bron staat** én je gevolg **geen nieuw begrip introduceert dat er niet staat**. "Feedback", "nakijklast", "weinig tijd", "consistentie" zijn zulke begrippen: als de bron ze niet noemt, mag jouw gevolg ze niet als vanzelfsprekend neerzetten.

Twee harde controles:
1. **Woordtoets.** Elk zelfstandig naamwoord dat de kern van je haakje draagt: staat dat woord, of een echt synoniem, in de bron? Zo niet, schrappen. Zoek desnoods letterlijk (Ctrl-F) in de brontekst.
2. **Tegenspraaktoets.** Spreekt de bron je gevolg ergens tegen? In het Marrewijk-geval beweerde het haakje dat zijn studenten weinig tijd hadden, terwijl hij juist schreef dat ze op tijd inleverden zonder dat hij ze achter de broek zat. Een gevolg dat de bron tegenspreekt is geen zwak haakje, het is een verkeerd haakje.

3. **Omkeertoets, op de brug naar Eduface.** Vervang het detail waarop je haakt door een ander detail dat in dezelfde situatie had gekund. Klopt je zin dan nog steeds, dan haak je er niet echt op en is de brug vals. Voorbeeld: "twee afstudeeronderzoeken bepaalden of SDO de licentie hield, op geschreven werk staat dan alles" blijft kloppen als het mondelinge examens waren geweest. Dus de brug ging over "er stond veel op het spel", niet over schrijven, en dat geldt voor elke opleider. Gezakt.

4. **Drager-toets, wie draagt de last.** Schrijf letterlijk op wie in de **bron** de last draagt: de **student**, de **beoordelaar/docent**, de **organisatie**, of het **panel**. Schrijf daarna op wie de last draagt in **jouw zin**. Zijn dat niet dezelfde, dan is je haakje ongeldig. Ook als elk getal klopt. Ook als elk woord in de bron staat.

   Eduface neemt werk weg bij de **beoordelaar**. Een bron die een last bij de student legt is dus geen haakje voor ons, hoe mooi het citaat ook klinkt. De enige legitieme brug is een **apart feit uit de bron dat zelf over de beoordelaarskant gaat** (wie kijkt na, met hoeveel mensen, hoe vaak) en dat feit moet er letterlijk staan. Twee citaten dus, niet één citaat en een aanname.

   **Heb je dat tweede citaat niet, stel dan de vraag in plaats van de aanname te doen.** "Cursisten schrijven een reflectieverslag per les" plus "wie leest dat nu allemaal?" is geldig, want je beweert niets over de docent. "Dus dat is een flinke klus voor je docenten" is niet geldig. Dit is meestal het betere bericht sowieso, want het eindigt op een open vraag.

   Let extra op **vaktermen**: die hebben een vaste betekenis met een vaste drager, en je mag ze niet als gewone taal lezen. De lijst staat in `references/onderwijs-vaktermen.md`. Staat je woord daarin, dan gebruik je het alleen in de betekenis uit die tabel.

   > **Wat er misging (THIM, 13-08-2026).** Het NVAO-rapport beveelt aan "te blijven waken over de studeerbaarheid, met het oog op de vele herhalingsactiviteiten, feedbackmomenten en toetsen". De opvolgmail maakte daarvan: "ik kan me voorstellen dat het nakijken daarvan een flinke klus is voor de docenten". Woordtoets, tegenspraaktoets en omkeertoets gaven alle drie groen, want de woorden stonden er en de getallen klopten. Toch was het haakje fout: studeerbaarheid is een NVAO-standaard over de **student**. Thim van der Laan corrigeerde het zelf en wees de mail af: *"Dit is de studeerbaarheid voor de student. De oplossing die jij aanbiedt probeert meer de organisatie in efficiëntie e.d. te ondersteunen. Dat zijn twee verschillende dingen."* Het juiste haakje lag er wél: het fysio-rapport zegt letterlijk dat twee onafhankelijke beoordelaars de scriptie nakijken. Dat is de beoordelaarskant, en dat stond al in het connectieverzoek van 07-08.

Komt je haakje deze toets niet door, dan val je terug op een feit dat er wél staat, ook als dat minder mooi aansluit op Eduface. Een waar en saaier haakje verslaat altijd een mooi en verzonnen haakje. Lukt zelfs dat niet, dan geldt de gate uit stap 4: niet schrijven, voorleggen aan Dante.

#### Een LinkedIn-profiel lezen: structuur is betekenis

Een profiel is geen lopende tekst, het is een structuur. Lees hem als structuur, anders verzin je een loopbaan.

- **Een skill-tag is geen functie.** Onder een rol staan vaardigheden (bijv. "Procesverbetering, Moodle, +6"). Die horen bij díe rol en zeggen alleen dat de persoon er in die rol mee werkt. Nooit lezen als een vorige baan. Op 2026-07-23 ging er een bericht bijna uit met "je bent van het beheer van Moodle doorgegroeid naar Manager Digitale Innovatie", terwijl Moodle als skill onder haar **huidige** rol stond. Ze werkte er nú mee; het bericht zette haar precies verkeerd neer.
- **Datums bepalen wat verleden is.** "sep 2025 - heden" is de huidige rol, lopend. Alleen een functie met een einddatum is verleden. Je mag pas "doorgegroeid van X naar Y" of "je hebt X achter je gelaten" schrijven als X aantoonbaar een afgesloten eerdere functie is, met de datums ernaast. Een tag of een detail onder de huidige rol is per definitie heden.
- **Volgorde van betrouwbaarheid op het profiel:** functietitel + datums, dan headline, dan about, dan de beschrijving onder een rol, dan skill-tags. Een haakje bouw je op de bovenste lagen, niet op een losse tag.

### Het connectieverzoek (max 300 tekens)

**Er is geen sjabloon.** De drie berichten die Dante op 2026-07-23 goedkeurde hebben alle drie een andere vorm. Wat ze delen is een ritme, geen invulschema.

#### Het ritme, afgeleid uit Dante's eigen herschrijvingen

```
1. Hi [voornaam], ik las [hun woorden of een feit uit hun materiaal]
2. [WAT JIJ ERVAN VINDT]              <- de stap die ik steeds oversla
3. [wie wij zijn, vastgemaakt aan die reactie, met bewijs]
4. [een RELEVANTE OPEN VRAAG]
```

**Stap 4 is altijd een relevante open vraag, nooit een ja/nee-slot** (regel van Dante, 2026-08-07). Dus niet "Ook iets voor jullie?", "Wil je er meer over weten?", "Moeite waard om te connecten?". Een open vraag nodigt uit tot een antwoord en start het gesprek; een ja/nee-vraag geeft een makkelijke uitweg. Kies een vraag die aansluit op wat je aanhaalde. Voorbeelden van Dante:

- Zou je willen weten hoe we dit bij Radboud Universiteit inzetten?
- Hoe richten jullie dat momenteel in?
- Welk onderdeel van het [nakijken / formatieve feedback / summatieve feedback] kost voor docenten het meeste tijd?
- Wat waren de resultaten van het onderzoek?
- Is het inmiddels gelukt om te komen tot de ideale workflow?
- Hoe staan jullie er nu voor?

De social-proofregel eromheen: "bij [betaalde klant] zetten wij AI in waardoor de kwaliteit van de feedback omhoog gaat", en dan de open vraag.

Stap 2 is het verschil tussen dood en levend, en het is precies wat ik zelf niet doe. Ik schrijf 1, 3, 4 en lever iets correct en vergeetbaars op.

#### De drie goedgekeurde berichten

**Marcel van Marrewijk, SDO** — reactie zit in de doorgetrokken lijn, vraag is een doorverwijzing.

> Hi Marcel, ik las hoe een afstudeerder van je met zijn begeleider een zelfbewuste professional werd. Bij Hogeschool Rotterdam geeft ons AI-model formatieve feedback op schrijfopdrachten, wat uitval kan tegengaan. Weet jij wie hier over gaat? Het is me helaas niet gelukt om die persoon te vinden.

**Femke Bex, Artemis** — reactie is verbazing plus humor, uitnodiging is licht.

> Hi Femke, ik las in jullie visitatierapport dat studenten naast een visueel eindexamenproject ook een onderzoeksverslag schrijven. Dat verraste me bij jullie creatieve opleidingen :) Met ons onderwijskundig AI-model ondersteunen wij docenten bij het geven van feedback. Wil je er meer over weten?

**Conny Spijker, Schouten & Nelissen** — reactie is instemming, bewijs zijn de universiteiten.

> Hi Conny, je schreef dat de kracht van AI in het empoweren van de mens zit, niet in het vervangen. Helemaal mee eens, dat is de basis van ons onderwijskundig AI-model, gebouwd met Universiteit Leiden. Lijkt het je leuk om te horen hoe Tilburg University en de Radboud Universiteit het inzetten?

Let op wat er in twee van de drie **niet** in staat: geen uitval, geen opleider-klant, geen letterlijke productformulering. Ze zijn toch goedgekeurd. Dat is het bewijs dat de checklist een hulpmiddel is en geen eis.

#### Wat Dante anders doet dan ik

Uit zijn herschrijvingen, want dat is de kalibratie:

- **Hij vindt iets.** "Voor mij een verrassing", "Helemaal mee eens". Ik constateer alleen.
- **Hij legt het product niet uit, hij claimt een identiteit.** "Dat is de basis van ons model" in plaats van een beschrijving van het mechanisme. Uitleggen kost tekens en overtuigt minder.
- **Zijn slot is een uitnodiging, geen opgave.** "Wil je er meer over weten?", "Lijkt het je leuk om te horen hoe X het inzet?" Dat kost de ander niets.
- **Hij schrijft korter over onszelf en langer over hen.**
- **Een smiley mag,** ook koud.

#### De opening

Altijd `Hi [voornaam]`, nooit "Hoi" en nooit "Beste". Openen met **"ik las"** of **"je schreef"**. Geen aanloopje (`no-opviel-filler-openers`).

#### De waarde

**Zeg concreet wat Eduface doet, niet alleen "ons AI-model".** Een lezer die "dat is de basis van ons AI-model" leest, denkt: oke, maar wat dóen jullie dan? Elk bericht moet ergens de daad benoemen: **docenten ondersteunen bij het nakijken en feedback geven op studentopdrachten** (of schrijfopdrachten). Vastgesteld met Dante 2026-07-24 op het Conny-bericht.

**Wat vastligt is de claim, niet de woorden:**
- de lezer weet na afloop concreet wat Eduface doet
- het klopt inhoudelijk: formatieve feedback op schrijfopdrachten, nooit "vragen beantwoorden" of "sneller nakijken"
- geen harde belofte over uitval, "kan tegengaan" mag, "zodat er minder afhaken" niet
- alleen functies die in `references/eduface-product.md` staan

**Twee toetsen die originaliteit afdwingen:**
1. **Uitwisseltoets.** Plak je waarde-zin in het bericht van iemand anders bij dezelfde organisatie. Past hij daar net zo goed, dan is het een sjabloon en zakt hij.
2. **Echo-toets.** Bevat de waarde-zin minstens één woord of artefact uit het haakje? Bij Marcel: begeleider → begeleiding. Bij Conny: empoweren → de basis van ons model. Zo niet, dan heb je de waarde eraan geplakt in plaats van eraan verbonden.

Loop je vast, dan kun je langs deze vier: AI-model, wat het doet, de pijn, bewijs. **Geen verplichte vakjes.**

**De pijn hoort niet in het connectieverzoek** (besluit Dante 2026-07-23). Uitval of werkdruk noemen voelt geforceerd bij een eerste contact, en het kost 30 tot 40 tekens die beter naar het haakje gaan. Geen van Dante's eigen berichten heeft het. Bewaar het voor het gesprek.

Wil je het toch, dan geldt: lang traject → uitval, kort traject → werkdruk van de beoordelaars. Maar de standaard is: weglaten.

**Welke naam je als bewijs noemt, is een personalisatie, geen vaste keuze** (de alma-mater-toets, Dante 2026-07-24). Voor je een klantnaam invult:

1. **Waar heeft deze persoon gestudeerd?** Staat vaak op hun LinkedIn onder `education`. Studeerde hij bij een van onze klanten of partners (Radboud, Leiden, Tilburg, Den Haag, Rotterdam), noem dan díe. Thijs Groenen studeerde aan de Radboud en ons model draait daar, dus noem de Radboud, niet Rotterdam.
2. **Waar woont of werkt hij?** Woont iemand in Leiden maar studeerde hij elders, dan kent hij Universiteit Leiden ook. Noem dan Leiden.
3. **Heeft hij die band, dan mag de afkorting.** Normaal voluit, want "RU" of "UL" zegt een vreemde niets. Maar wie er studeerde of vlakbij woont kent de afkorting wel, en "de Radboud" klinkt als iemand uit hun eigen wereld. Scheelt bovendien tekens.
4. **Geen band gevonden, dan val je terug op een betaalde klant, voluit.**

De volledige lijst en logica staat in `references/eduface-product.md`.

#### Het slot

Naast de doorverwijsvraag en de simpele uitnodiging is er een derde vorm die op 2026-07-24 werkte: **"Is dit het soort innovatie waar je open voor staat om er meer over te leren?"** Die geeft ze een makkelijke ja, en het woord "innovatie" verwijst impliciet naar hun rol zonder die te benoemen.

**Benoem iemands functie niet in het bericht.** Die kent hij zelf. "Als manager digitale innovatie ben jij vast degene die..." is te sturend en te sales. Laat de functie impliciet, of laat hem weg.



Twee vormen, allebei goedgekeurd:

**De keuze hangt af van wie het is** (bevestigd door Dante 2026-07-23):

- **Zit deze persoon hoog in de boom en kan hij het doorschuiven → de doorverwijsvraag.** "Weet jij wie hier over gaat? Het is me helaas niet gelukt om die persoon te vinden." De tweede zin is niet optioneel, die maakt het zacht en geeft ze een reden om te helpen. Zo bij Marcel, bestuurder.
- **Is deze persoon aantoonbaar zelf de juiste → de uitnodiging.** "Wil je er meer over weten?" of "Lijkt het je leuk om te horen hoe X het inzet?" Zo bij Femke (hoofd onderwijs) en Conny (teamlead L&D). Doorverwijzen vragen aan iemand die het zelf is, leest als lui.

Vraag nooit om tijd of een meeting in het connectieverzoek. Dat komt later.

#### Humor en verbazing

**"Goeie humor werkt 100% goed"** (Dante, 2026-07-23). Verbazing over iets interessants werkt, spot met hun keuzes niet.

**Let op labels die zij zelf afwijzen.** Bij Artemis lag "art school" voor de hand, maar hun eigen rapport zegt "De opleiding van Artemis is geen kunstacademie". Dan werkt de grap tegen je. Check of het label dat je gebruikt door henzelf gedragen wordt.

#### Het moet klinken als een mens

Zodra je op tekens gaat optimaliseren ga je telegramstijl schrijven: losse fragmenten en blokjes die je achter elkaar plakt. "Ook bij Hogeschool Rotterdam." is geen zin, dat is een voetnoot.

**Toets:** lees het hardop. Zijn het hele, lopende zinnen? Staat er een fragment zonder werkwoord? Dan herschrijven.

- Verwerk de klantnaam ín de zin, niet als aanhangsel erachter.
- Zacht formuleren waar het kan. "Het is me helaas niet gelukt om die persoon te vinden" klinkt menselijker dan "Ik kan die persoon niet vinden".
- De regel "bondig, geen opsmuk" uit `communication-style` geldt voor hoe je met Dante praat, **niet** voor outreach. Daar mag het ademen.

#### Het LMS is bijna nooit een haakje

Vastgesteld met Dante 2026-07-24. In een eerste connectieverzoek praat je bijna nooit over het LMS.

- **Dat iemand het LMS beheert is geen haakje.** Dat boeit ze niet in een koud bericht. De integratie op zichzelf ook niet.
- **Het enige geldige moment** om het LMS te noemen is oprechte interesse in hún specifieke systeem ("we zijn benieuwd hoe jullie Moodle gebruiken"). Dat mag, meer niet.
- **Noem het bij naam, hun eigen systeem** ("integreert in jullie Moodle"), nooit het generieke "het LMS" of "leeromgeving". Som de systemen nooit op waar Eduface mee integreert.


#### Twee soorten namen

- **De organisatie van de ontvanger: afkorten** naar de korte vorm die ze zelf voeren. Dirksen, ASRE, SDO.
- **Onze klanten en partners: voluit.** Hogeschool Rotterdam, Tilburg University, Universiteit Leiden. "HR" of "Tilburg" alleen zegt te weinig en dan valt het bewijs weg.

#### Vorm, mechanisch te checken

- **Tekens.** Het script weigert boven 300, maar schrijf niet richting de grens: kort is beter.
- **Getallen.** Staat er een getal in dat van hun website komt? Weghalen, die zijn vaak verouderd.
- **Eén haakje**, niet twee. Een tweede is ruis in 300 tekens.

### De opvolgmail: nu standaard onderdeel van de oplevering

**Herzien met Dante, 2026-08-12** (vervangt het besluit van 2026-07-23 om geen opvolgbericht te schrijven). Elk connectieverzoek krijgt een opvolgmail erbij, die verstuurd wordt zodra iemand accepteert. In Lemlist gaat dat in de velden `firstEmailSubject` en `firstEmail`.

**Vorm, afgeleid van de eerste goedgekeurde batch (Irma/Joan/Erwin, 2026-08-12):**

```
Hi [voornaam],

Ik las [een specifiek, gedateerd detail uit de bron — een rapport, reglement, procedure — met de datum erbij]. Ik kan me voorstellen dat [een eerlijke, voorstelbare consequentie voor hen, geen verzonnen pijnwoord]. Hierom stuurde ik je een LinkedIn-connectieverzoek.

Wij hebben een zelf getraind Nederlands onderwijskundig AI-model gebouwd, ontwikkeld met hulp van de Universiteit Leiden en de Radboud Universiteit, dat formatieve en summatieve feedback geeft op studentopdrachten. Onze tool wordt momenteel ingezet bij onder andere Hogeschool Rotterdam en Tilburg University.

[Een tweede, specifieke vraag die voortbouwt op de datum van de bron — "dat rapport/reglement is van [datum], dus ik ben benieuwd hoe jullie dat nu oppakken" — of een andere concrete vervolgvraag.]

Met vriendelijke groet,

Dante Torbed
Customer success manager, Eduface
```

- De Eduface-alinea is vast en mag letterlijk hergebruikt worden (klanten/partners kloppen met `references/eduface-product.md`: Leiden + Radboud bouwden mee, Hogeschool Rotterdam + Tilburg University + Radboud Universiteit zijn betaalde klanten). Wissel `Radboud Universiteit` in voor de alma-mater-toets zoals bij het connectieverzoek.
- De opvolgmail mag **een ander, dieper detail uit dezelfde bron** gebruiken dan het connectieverzoek — het hoeft niet hetzelfde citaat te herhalen. Vaak werkt: de datum van het rapport/reglement noemen en vragen hoe de situatie er nu voor staat.
- Schrijf ook een korte, specifieke **firstEmailSubject** (geen clickbait, geen "Vraag over..." generiek): een paar woorden uit de bron zelf.
- Zelfde brontoets en niet-onderhandelbaar-regels als het connectieverzoek: geen woord dat niet uit de bron komt, geen verzonnen pijn.

Bij een niveau-3-haakje (je hebt iets gemaakt op basis van hun idee) bewaar je dat voor na de acceptatie. Bouwen via `marketing-creatives`.

## Niet-onderhandelbaar

- **Geen enkel woord dat niet uit de bron komt.** Doe de brontoets uit stap 5. Introduceer nooit een begrip (feedback, nakijklast, tijdsdruk, consistentie) dat de persoon zelf niet noemde, ook niet als het perfect naar Eduface leidt. Juist dán is de kans het grootst dat je het verzint.
- **Nooit meer lezing claimen dan je hebt gedaan.** Las je de abstract, schrijf "ik las de abstract". Zie `person-research` regel 2.
- **Altijd eerlijk over hoe je bij iemand kwam**, ook als de route omslachtig is. Dat maakt het geloofwaardig in plaats van eng.
- **Nooit zeggen dat je je in een persoon hebt verdiept.** In een organisatie mag wel ("ik ben me in Avans gaan verdiepen"), in een persoon niet.
- **Geen AI-tells, geen lege verbindingszinnen, geen em-dashes.** Gewone spreektaal (`outreach-plain-language`). Zie `content-voice`.
- **Uitnodigend formuleren, niet sturend** (`mails-friendly-not-directive`). Dante is niet hun manager.
- **Verzin nooit een persoonlijk feit.** Het Italië-anker van Dante werkte omdat het waar was.

## Stap 6: oplevering aan Dante

Per persoon, in deze vorm. Dante leest de bron zelf en haalt er nuance uit die ik mis, dus de bron is geen bijlage maar onderdeel van de oplevering.

**Altijd de redenering erbij** (regel van Dante, 2026-08-07): Dante wil per lead zien waar je het op baseert en waarom je het zo schrijft. Nooit alleen het bericht opleveren. Concreet betekent dat:

- **Naam, functie, organisatie, LinkedIn-link**
- **Waar ik het op baseer**: het haakje met niveau, **letterlijk citaat en bron-URL** (klikbaar). Meerdere citaten als het bericht op meerdere feiten leunt.
- **Waarom ik het zo schrijf**: waarom dit haakje de reactie is en geen kaal feit, waarom deze persoon de juiste is, welke social proof je koos en waarom (alma-mater-toets), welke pijn je raakt.
- **Afgevallen haakjes / afgevallen kandidaten**, één regel elk met de reden (verkeerde persoon, buiten ICP, fit zwak, examencommissie, enz.). Ook als iemand afvalt: geef de redenering.
- **Connectieverzoek**, met tekenaantal.
- **Twijfels**, expliciet. Wat je niet hard kreeg, en waar je Dante's oordeel op wil.

Bij een lijst: lever in batches, niet alles in één keer. Dan kan Dante bijsturen voor je dertig berichten de verkeerde kant op hebt geschreven.

## Verzenden

- Verzoeken gaan handmatig vanuit Dante's eigen LinkedIn (Premium).
- Lemlist kan LinkedIn-stappen draaien, maar de **lemlist MCP was op 2026-07-22 nog niet geautoriseerd** in deze werkomgeving. Controleer dat voor je iets in Lemlist belooft.
- Spreid de verzoeken. Een bak tegelijk is zichtbaar als campagne en raakt de limieten.

## Done

- Close en Gmail gecheckt, persoon is aantoonbaar koud.
- Haakje op niveau 2 of hoger, met letterlijk citaat en bron. Anders voorgelegd aan Dante in plaats van doorgeschreven.
- Eén haakje in het verzoek, niet twee.
- Verzoek onder de 300 tekens, tekenaantal erbij.
- De vraag zit in het verzoek zelf, en het is er een die deze persoon vanuit zijn rol kan beantwoorden.
- **HARDE REGEL: nooit alleen het bericht opleveren.** Bij ELK bericht (ook een herschrijving, ook een enkel bericht, ook onder tijdsdruk) leveren: "Waar ik het op baseer" met klikbare bron-URL('s) + letterlijk citaat, en "Waarom ik het zo schrijf". Vastgesteld met Dante 2026-08-07 nadat een kort NOB-bericht zonder onderbouwing werd opgeleverd. Lever je alleen de tekst, dan is de oplevering incompleet.
