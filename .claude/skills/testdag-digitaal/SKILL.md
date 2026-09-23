---
name: testdag-digitaal
description: Bouwt het vakdossier voor een Eduface-testdag als een los HTML-bestand dat op elke laptop offline opent, in plaats van als printstapel. Zelfde analyse als de printskill (beoordeling van de nakijker naast de Eduface-output, de verschillen, de aannames, de vragen), andere drager. Gebruik deze skill bij "digitale versie", "we kunnen niet printen", "bouw het dossier voor de testdag", "testdag zonder printer", "zet het vakdossier op de laptop", of wanneer Dante een Eduface-output en een ingevuld formulier aanlevert voor een testdag waar niet geprint wordt.
---

# Testdag, digitaal: Eduface naast de nakijker op het scherm

Dit is de digitale tegenhanger van de printskill. **De analyse is identiek, alleen de drager verschilt.** Stap 1 tot en met 6 hieronder zijn hetzelfde werk: uitlezen, koppelen, het verschil vaststellen, de aanname erachter zoeken, controleren, de vragen schrijven. Vanaf stap 7 gaat het over een bestand in plaats van een stapel papier.

Het doel is niet aantonen dat het model gelijk heeft. Het doel is **erachter komen welke norm de opleiding hanteert**, door precies die plekken op te zoeken waar het model en de nakijker uit elkaar lopen, en daar een vraag van te maken die de opleiding wil beantwoorden.

Een verschil is bijna nooit een fout van een van de twee. Het is bijna altijd een **aanname**: het model leest iets in de rubriek dat er letterlijk wel staat maar zo niet bedoeld is, of het legt een standaard aan die in dit vak niet geldt. Die aanname is de hele opbrengst van een testdag. Vind hem, en stel hem als keuze voor.

**De printskill blijft bestaan en wordt niet aangepast.** Is er wel een printer, dan is die skill de juiste. Deze is voor de dag dat je daar niet op kunt rekenen.

## Wanneer

Er ligt minimaal:
- **de rubriek of het beoordelingsformulier** van de opleiding, blanco of ingevuld
- **minstens een ingevuld formulier** van een nakijker over concreet studentwerk
- **de Eduface-output** over datzelfde studentwerk

Ontbreekt de Eduface-output, dan kun je de vergelijking niet maken. Zeg dat, en lever het standaardblad in plaats van een dossier. Verzin geen kolom.

## Stap 1: zelf uitlezen, niet laten aanleveren

Ga zelf op zoek voordat je iets vraagt. In deze volgorde:

1. **De repo.** `GTM/Accounts/<instelling>/` heeft een bestand met het aangeleverde materiaal en een met de beoordelingsstijlen. Lees die eerst, die vertellen je welk bestand waar staat.
2. **Google Drive.** `search_files` op de naam van de instelling en op het vak. `read_file_content` geeft schone tekst uit docx en pdf, inclusief tabellen. Gebruik dat, geen download.
3. **Gmail.** De bijlagen zitten in de mailwisseling met de opleiding. Gmail geeft je alleen metadata, geen bytes, dus gebruik de mail om te zien wat er bestaat en haal het bestand daarna uit Drive.

Vraag pas iets aan Dante als je het echt niet kunt vinden. Zie `.claude/rules/credits.md`: eerst kijken, dan pas vragen.

Leg per vak vast wat je gevonden hebt en wat niet, zodat de volgende ronde niet opnieuw zoekt.

## Stap 2: de criteria op elkaar leggen

De nakijker en het model gebruiken zelden dezelfde namen. Maak eerst een koppeling.

- Tel hoeveel criteria de rubriek heeft en hoeveel onderdelen het model beoordeelt. Zijn die aantallen ongelijk, dan is dat zelf al een bevinding.
- Koppel op inhoud, niet op nummer. "Stap 3" bij de een kan "Zoekstrategie" bij de ander zijn.
- Is de rubriek in een andere versie beoordeeld dan de versie die nu geldt, controleer dan of de criteria echt verschillen of alleen de puntentelling. Dat scheelt een vals verschil.
- Lukt een koppeling niet, laat de regel dan leeg staan met de reden erbij. Een leeg vak is beter dan een gegokt vak.

## Stap 3: het verschil vaststellen

Per gekoppeld criterium drie mogelijke uitkomsten:

| Uitkomst | Wat het betekent |
|---|---|
| **eens** | beiden voldaan, of beiden niet |
| **model strenger** | de nakijker keurde goed, het model keurt af |
| **model milder** | de nakijker keurde af, het model keurt goed |

"Model milder" is het waardevolste geval en wordt het vaakst over het hoofd gezien. Daar zag de nakijker iets dat het model mist, en dat is precies wat er in het model moet.

Zet er ook een totaal onder: hoeveel criteria voldaan bij de nakijker, hoeveel onderdelen voldaan bij het model, en op hoeveel van de criteria ze het eens zijn. Dat laatste getal is de kalibratiescore. In het sjabloon rekent het bestand die drie zelf uit, jij vult alleen de oordelen in.

## Stap 4: de aanname erachter zoeken

Dit is de stap die de skill zijn waarde geeft, en de stap die je niet mag overslaan.

Neem elk verschil en vraag: **waarom komt het model tot een ander oordeel?** Zoek het antwoord in de tekst van het model zelf, niet in je eigen mening. Terugkerende soorten:

| Soort aanname | Hoe je hem herkent |
|---|---|
| **Letterlijk lezen van de rubriek** | de rubriek zegt "hypotheses", meervoud, en het model vraagt om een vergelijking tussen meerdere oorzaken terwijl de opleiding een goed onderbouwd spoor genoeg vindt |
| **Een hogere standaard aanleggen** | het model vraagt om onderbouwing van de afgewezen bronnen, de opleiding vindt een gemotiveerde keuze voldoende |
| **Iets eisen dat in de rubriek niet staat** | het model vraagt naar taalgebruik, herkomst van de tekst of opmaak terwijl de rubriek daar niets over zegt |
| **Compensatie anders toepassen** | het model laat een onderdeel zakken waar de opleiding het tegen de rest wegstreept |
| **Een controleerbare bewering doen** | het model noemt een concrete rekenfout, een ontbrekende datum, een verkeerde formule |

Die laatste is een ander soort dan de eerste vier: dat is geen normverschil maar een feit. Behandel hem apart, zie stap 5.

Schrijf per aanname drie regels op:
1. wat het model zegt, letterlijk, tussen aanhalingstekens
2. wat de rubriek er letterlijk over zegt
3. wat de nakijker in de praktijk deed

Meer niet. Geen oordeel over wie gelijk heeft. Die drie regels worden in het bestand het uitklapblok onder de vraag.

## Stap 5: controleren voordat het in het bestand gaat

Elke feitelijke bewering van het model gaat eerst door een controle tegen het studentwerk zelf. Klopt de rekenfout? Ontbreekt de zoekdatum echt? Staat die passage er echt?

- **Klopt het:** het mag erin, als feit, met de vindplaats erbij.
- **Klopt het niet:** het mag erin, als bevinding over het model. Dat is nuttige informatie, geen schaamte.
- **Kun je het niet controleren:** het gaat er **niet** in. Je meldt het wel aan Dante, zodat hij weet dat het op het scherm kan opduiken.

Beweringen over de herkomst van tekst, zoals "dit is met AI geschreven", zijn extra gevoelig. Die gaan nooit als feit in het bestand. Hoogstens als vraag: wil de opleiding dat het model hier iets over zegt.

## Stap 6: de vragen schrijven

Per aanname een vraag. Dit is het onderdeel waar de skill op staat of valt, want een verkeerd geformuleerde vraag maakt van een gesprek een afrekening.

### De regels

- **Het model is het onderwerp, nooit de nakijker.** "Het model vraagt om X" kan. "De nakijker heeft X niet gedaan" kan niet.
- **Eindig in een keuze, niet in een oordeel.** De vraag gaat over wat de opleiding wil, niet over wie gelijk had.
- **Geen namen.** In het hele bestand heet de beoordelaar "nakijker" en heten studenten "Student 1" en "Student 2". Dante noemt er in de zaal wel bij wie het was. Zo blijft het transparant zonder dat er iemand voor de groep wordt gezet. Digitaal weegt dit zwaarder dan op papier: een bestand kan doorgestuurd worden, een vel papier neem je aan het eind van de dag mee.
- **Geen tegenstellende voegwoorden.** Geen "maar", "echter", "terwijl", "toch". Die zetten de twee tegenover elkaar.
- **Maximaal twee zinnen.** De eerste stelt de aanname vast, de tweede stelt de vraag.
- **Tutoyeren.** Jij en je, niet u.
- **Geen versterkers.** Geen "opvallend", "duidelijk", "eigenlijk", "gewoon". Die leggen er een oordeel in.

### Ook voor de koppen

Kort en plat. "Feedback van Eduface", niet "De volledige feedback van Eduface". "Aannames van het model", niet "De aannames die het model doet". Een kop die uitlegt wat eronder staat is een kop te veel, en leest als machinetekst.

### Zo wel, zo niet

| Niet | Wel |
|---|---|
| "De nakijker keurde dit goed, terwijl er duidelijk een rekenfout in zit." | "Het model wijst hier een rekenfout aan in de tabel. Klopt die, en is dit iets wat jullie zelf ook zouden willen zien?" |
| "De nakijker eist geen differentiaaldiagnose, de rubriek wel." | "Het model leest 'hypotheses' in de rubriek als meervoud en vraagt om een vergelijking tussen meerdere oorzaken. Verwachten jullie dat ook, of is een goed onderbouwd spoor genoeg?" |
| "Hier is de student te kort door de bocht gegaan en is dat niet opgemerkt." | "Het model vraagt om de afgewezen bronnen erbij. Is dat wat jullie van een student verwachten op dit niveau?" |
| "Het model was hier strenger dan jullie." | "Op dit onderdeel legt het model de lat hoger dan in deze beoordeling is gebeurd. Waar zou hij volgens jullie moeten liggen?" |

### Waar het model milder was

Dat is geen verwijt aan het model en al helemaal geen compliment aan de nakijker. Schrijf het als: "Hier zag de nakijker iets dat het model niet noemt. Wat was dat, zodat we het kunnen meenemen?"

## Stap 7: het bestand bouwen

Een vakdossier is **een HTML-bestand per vak**, niet per persoon. Iedereen die bij dat vak hoort krijgt hetzelfde bestand, ook wie zelf niets beoordeeld heeft. Dan heeft de hele groep hetzelfde voor zich.

Je schrijft geen HTML. Je vult een JSON en draait het script:

```bash
cd .claude/skills/testdag-digitaal/sjabloon
python3 bouw.py <vak>.json ../../../<uitvoer>/<vak>.html
```

Wat eruit komt is **een los bestand** met de fonts, de opmaak en de inhoud erin. Geen internet, geen server, geen tweede bestand. Dubbelklikken is genoeg. Het sjabloon, het script en een gevuld voorbeeld staan in `sjabloon/`, de velden staan in `sjabloon/README.md`.

Vaste opbouw per student, dezelfde vier onderdelen als de vier bladen op papier:

| Onderdeel | Wat erin staat |
|---|---|
| Beoordeling | De oordelen naast elkaar met de verschillen gemarkeerd, en de drie totalen. Plus het eindoordeel en de letterlijke eindfeedback van de nakijker |
| Feedback Eduface | De volledige feedback van het model, per criterium, letterlijk |
| Waar het uiteenloopt | Twee of drie plekken, beide teksten naast elkaar, een vraag per plek |
| Aannames van het model | De aannames met de vriendelijke vragen, en de onderbouwing eronder ingeklapt |

Kop: **Eduface testdag**, met de opleiding, het vak en de datum van de oorspronkelijke beoordeling in de zijbalk. Geen naam van de nakijker.

Kolomkoppen in de tabel: **Nakijker** en **Eduface**. Niet "wat jullie zeiden".

Het ontwerp volgt `Design/System/core/` plus `internal/`. Verzin geen eigen kleuren of maten: het sjabloon heeft ze al.

## Stap 7-bis: het formulier volgt de rubriek, niet een sjabloon

Het aantal rubriekcriteria verschilt per vak. Acht bij de een, tien of twintig bij de ander, en soms heet het geen rubriek maar een lijst criteria. **Tel ze in het echte beoordelingsformulier en vul de JSON daarop.**

- Ken je de criteria, zet ze er dan letterlijk in. Dat voorkomt dat twee mensen hetzelfde criterium anders noemen.
- Ken je ze niet, zeg dat dan in het bestand in plaats van een rij te verzinnen.
- Nooit acht rijen neerzetten omdat het vorige vak er acht had.

Kent de nakijker een tussenstand die het model niet kent (een criterium met losse vinkjes eronder), zet die dan in `beoordelingsoptie.rangorde` tussen de andere in en leg het uit in `tabel_voet`. Het bestand rekent de richting van het verschil uit die rangorde uit.

## Stap 7a: de beoordelingsoptie staat in de zijbalk

Eduface heeft per opdracht een beoordelingsoptie aanstaan, en die bepaalt hoe de feedback eruitziet. Staat dat er niet bij, dan weet de lezer niet waar hij naar kijkt en gaat het gesprek over de verkeerde dingen. In het bestand staat het in de zijbalk, dus het blijft de hele tijd in beeld.

| Veld | Wat erin staat |
|---|---|
| `gekozen` | de optie, in het Nederlands, nooit in het Engels |
| `wat_dat_doet` | een zin over wat het model dan wel en niet uitspreekt |
| `waarschuwing` | alleen als er iets is dat het hele dossier raakt |

### De opties in het Nederlands

De tool noemt ze in het Engels. In het bestand gaan ze in het Nederlands, in de woorden die de opleiding zelf gebruikt.

| In de tool | In het bestand | Wanneer |
|---|---|---|
| pass/fail grading | **voldaan of niet voldaan**, per rubriekcriterium | als de rubriek van de opleiding zelf ook maar twee standen kent |
| descriptive grading | **onvoldoende, voldoende, goed of uitstekend**, per rubriekcriterium | als de rubriek kwaliteitsniveaus onderscheidt |

Vertaal ook de labels in de tabel mee: geen PASS en FAIL, maar voldaan en niet voldaan. Die staan letterlijk in `rangorde`, van laag naar hoog.

### Waarom alleen bij descriptief een uitleg

Bij voldaan of niet voldaan is de keuze vanzelfsprekend, want de rubriek doet het zelf al zo. Daar hoort geen uitleg bij, die leest als verantwoording voor iets wat niemand betwist.

Bij descriptief beoordelen is de keuze wel uitlegbaar, en die uitleg hoort erbij. Baseer hem op de rubriek van die opleiding zelf, nooit op een algemeen verhaal:
- wat onderscheidt hun rubriek dat een vinkje zou weggooien
- hoeveel niveaus hun rubriek kent, en hoeveel de tool kent

**Lopen die aantallen uiteen, zet dat in `waarschuwing`.** Kent de tool vier niveaus en de rubriek drie, dan is dat geen detail maar de eerste vraag van die ochtend.

## Stap 7b: de verspreiding, per vak en per persoon

Reken nooit in een totaal. Reken per vak, en lever de tabel op.

Per vak heb je twee getallen nodig:

- **P** = het aantal mensen dat bij dit vak hoort en die dag aansluit
- **S** = het aantal studenten van wie werk beoordeeld is, meestal twee

Daaruit volgt:

| Wat | Aantal | Waarom |
|---|---|---|
| **bestanden** | 1 per vak | iedereen bij dat vak opent hetzelfde bestand |
| **kopieën** | P | elke laptop zijn eigen kopie, niemand hoeft mee te kijken |
| **studentwerk** | S losse bestanden | die staan naast het dossier, niet erin |
| **blanco vellen** | P x 2 | om op te schrijven, plus pennen |

Is van een student de output van het model er niet, dan telt die student niet mee in S. Verzin geen dossier, zie stap 5.

**Hoe het op de laptops komt, in deze volgorde:**

1. **USB-stick.** Werkt altijd, ook zonder wifi. Neem er twee mee.
2. **Drive-link** als reserve. Ze downloaden het en openen het lokaal, niet in de viewer van Drive.
3. **Een PDF van hetzelfde bestand** als laatste vangnet voor een laptop die dwarsligt. Maak die met `chrome --headless --print-to-pdf`, en weet dat je dan het antwoordblad krijgt en niet het dossier.

Mail het bestand niet als bijlage: een los `.html`-bestand wordt door veel mailservers geblokkeerd.

## Stap 7c: hoe het bestand zich gedraagt

- **Eén doorlopende pagina met een zijbalk.** Niet in tabbladen, want dan werkt zoeken op de pagina niet meer en dat is juist de winst van een scherm.
- **Doorlopende vraagnummers over het hele vak**, V1, V2, V3. Het bestand nummert zelf, in de volgorde waarin de vragen staan. Die nummers zijn de brug naar het papier.
- **Geen voorblad.** Begin bij de beoordeling. Een inhoudsopgave is de zijbalk al.
- **De onderbouwing staat ingeklapt.** Wat het model letterlijk zei, wat de rubriek zegt en wat de nakijker deed: dat is bewijs voor wie doorvraagt, geen leesvoer voor iedereen.
- **Het werk van de student blijft een apart bestand.** Ze openen het in een tweede venster naast het dossier. Dat is de digitale versie van "los ernaast op tafel".

## Stap 7d: schrijven doet de groep op papier

**Kies één vangkanaal en zeg dat aan het begin.** Papier is de standaard. Typen tijdens een gesprek zet mensen achter hun scherm, en de helft op papier plus de helft op het scherm betekent dat je de helft van je oogst kwijtraakt.

- Iedereen krijgt **blanco vellen en een pen**. Ze schrijven het vraagnummer op en daarachter hun antwoord.
- Is er toch een printer, dan levert de knop **Antwoordblad printen** in het bestand een vel met alle vragen en schrijfruimte, twee of drie A4 in plaats van vier per student.
- Dante neemt de vellen mee. Die zijn na afloop terug te leggen op het dossier, want de nummers staan in allebei.

## Stap 8: terug naar het model

Wat de testdag oplevert gaat weer het model in. Per vak leg je vast:

- welke aannames de opleiding **bevestigt** (die mag het model houden)
- welke aannames de opleiding **afwijst** (die gaan in de feedbackstijl of de modelinstructie)
- welke feitelijke beweringen **niet klopten** (dat is een modelprobleem, geen instellingsprobleem)

Dat landt in `GTM/Accounts/<instelling>/` en, als het breder geldt dan een instelling, als voorstel in `Platform/`. Gaat het over de rubriektekst of de modelinstructies zelf, dan is de skill `grading-calibration` de volgende stap.

## Wat je nooit doet

- **De printskill aanpassen.** Die blijft zoals hij is. Verandert de methode, dan verandert hij in allebei, en dat meld je.
- **Een kolom verzinnen omdat de output ontbreekt.** Geen Eduface-output betekent geen dossier voor dat vak.
- **Een naam in het bestand zetten.** De nakijker heet nakijker, de student heet Student 1.
- **Een onverifieerde bewering van het model als feit opnemen.** Zie stap 5.
- **De nakijker het onderwerp van de zin maken.** Zie stap 6.
- **Meer dan drie vragen per onderdeel.** Drie worden beantwoord, tien worden overgeslagen.
- **Een verschil wegpoetsen omdat het ongemakkelijk is.** Een groot verschil is de reden dat je er zit.
- **De beoordelingsoptie in het Engels opnemen.** Pass/fail en descriptive zijn schermtaal.
- **Het bestand online zetten.** Er staat studentwerk en een beoordeling in. Dat hoort niet op een publieke URL, ook niet achter een onvindbare link.
- **Het bestand van internet laten afhangen.** Geen CDN, geen Google Fonts, geen externe afbeelding. Alles zit erin of het hoort er niet in.
- **Twee vangkanalen tegelijk.** Papier of scherm, niet allebei.
