---
name: grading-calibration
description: Legt de beoordeling van Eduface naast die van een nakijker van de instelling en levert een printbaar vakdossier op. Leest de ingevulde beoordelingsformulieren, de rubriek en de Eduface-output zelf uit, haalt de verschillen eruit, benoemt welke aanname het model doet, en schrijft daar vriendelijke vragen bij die de instelling op de testdag kan beantwoorden. Gebruik deze skill bij "kalibreren", "vakdossier", "feedback van Eduface naast die van de docent", "testdag voorbereiden" of wanneer Dante een Eduface-output en een ingevuld formulier aanlevert.
---

# Kalibreren: Eduface naast de nakijker

Het doel is niet aantonen dat het model gelijk heeft. Het doel is **erachter komen welke norm de opleiding hanteert**, door precies die plekken op te zoeken waar het model en de nakijker uit elkaar lopen, en daar een vraag van te maken die de opleiding wil beantwoorden.

Een verschil is bijna nooit een fout van een van de twee. Het is bijna altijd een **aanname**: het model leest iets in de rubriek dat er letterlijk wel staat maar zo niet bedoeld is, of het legt een standaard aan die in dit vak niet geldt. Die aanname is de hele opbrengst van een testdag. Vind hem, en stel hem als keuze voor.

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

Zet er ook een totaal onder: hoeveel criteria voldaan bij de nakijker, hoeveel onderdelen PASS bij het model, en op hoeveel van de criteria ze het eens zijn. Dat laatste getal is de kalibratiescore.

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

Meer niet. Geen oordeel over wie gelijk heeft.

## Stap 5: controleren voordat het op papier gaat

Elke feitelijke bewering van het model gaat eerst door een controle tegen het studentwerk zelf. Klopt de rekenfout? Ontbreekt de zoekdatum echt? Staat die passage er echt?

- **Klopt het:** het mag op papier, als feit, met de vindplaats erbij.
- **Klopt het niet:** het mag op papier, als bevinding over het model. Dat is nuttige informatie, geen schaamte.
- **Kun je het niet controleren:** het gaat **niet** op papier. Je meldt het wel aan Dante, zodat hij weet dat het op het scherm kan opduiken.

Beweringen over de herkomst van tekst, zoals "dit is met AI geschreven", zijn extra gevoelig. Die gaan nooit als feit op papier. Hoogstens als vraag: wil de opleiding dat het model hier iets over zegt.

## Stap 6: de vragen schrijven

Per aanname een vraag. Dit is het onderdeel waar de skill op staat of valt, want een verkeerd geformuleerde vraag maakt van een gesprek een afrekening.

### De regels

- **Het model is het onderwerp, nooit de nakijker.** "Het model vraagt om X" kan. "De nakijker heeft X niet gedaan" kan niet.
- **Eindig in een keuze, niet in een oordeel.** De vraag gaat over wat de opleiding wil, niet over wie gelijk had.
- **Geen namen.** In alles wat geprint wordt heet de beoordelaar "nakijker". Dante noemt er in de zaal wel bij wie het was. Zo blijft het transparant zonder dat er iemand voor de groep wordt gezet.
- **Geen tegenstellende voegwoorden.** Geen "maar", "echter", "terwijl", "toch". Die zetten de twee tegenover elkaar.
- **Maximaal twee zinnen.** De eerste stelt de aanname vast, de tweede stelt de vraag.
- **Tutoyeren.** Jij en je, niet u.
- **Geen versterkers.** Geen "opvallend", "duidelijk", "eigenlijk", "gewoon". Die leggen er een oordeel in.

### Zo wel, zo niet

| Niet | Wel |
|---|---|
| "De nakijker keurde dit goed, terwijl er duidelijk een rekenfout in zit." | "Het model wijst hier een rekenfout aan in de tabel. Klopt die, en is dit iets wat jullie zelf ook zouden willen zien?" |
| "Marloes eist geen differentiaaldiagnose, de rubriek wel." | "Het model leest 'hypotheses' in de rubriek als meervoud en vraagt om een vergelijking tussen meerdere oorzaken. Verwachten jullie dat ook, of is een goed onderbouwd spoor genoeg?" |
| "Hier is de student te kort door de bocht gegaan en is dat niet opgemerkt." | "Het model vraagt om de afgewezen bronnen erbij. Is dat wat jullie van een student verwachten op dit niveau?" |
| "Het model was hier strenger dan jullie." | "Op dit onderdeel legt het model de lat hoger dan in deze beoordeling is gebeurd. Waar zou hij volgens jullie moeten liggen?" |

### Waar het model milder was

Dat is geen verwijt aan het model en al helemaal geen compliment aan de nakijker. Schrijf het als: "Hier zag de nakijker iets dat het model niet noemt. Wat was dat, zodat we het kunnen meenemen?"

## Stap 7: het dossier bouwen

Een vakdossier is een printbare A4-stapel per vak, niet per persoon. Iedereen die bij dat vak hoort krijgt hetzelfde exemplaar, ook wie zelf niets beoordeeld heeft. Dan heeft de hele groep hetzelfde voor zich.

Vaste opbouw:

| Pagina | Wat erop staat |
|---|---|
| 1 | Kop, naam- en datumregel, de beoordeling naast elkaar met de verschillen gemarkeerd, drie totalen, de letterlijke feedback van de nakijker |
| 2 | De volledige feedback van het model, per criterium, letterlijk |
| 3 | Waar het uiteenloopt: twee of drie plekken, beide teksten eronder, een vraag per plek |
| 4 | De aannames van het model, met de vriendelijke vragen en schrijfruimte |

Kop: **Eduface testdag** als titel, daaronder de opleiding, daaronder het vak, de student en de datum van de oorspronkelijke beoordeling. Geen naam van de nakijker.

Kolomkoppen in de tabel: **Nakijker** en **Eduface**. Niet "wat jullie zeiden".

Bouwen doe je volgens `Design/System/core/` plus `internal/`, en renderen met headless Chromium naar A4. De werkende opzet staat in `GTM/Accounts/breederode-hogeschool/testdag/`.

## Stap 8: terug naar het model

Wat de testdag oplevert gaat weer het model in. Per vak leg je vast:

- welke aannames de opleiding **bevestigt** (die mag het model houden)
- welke aannames de opleiding **afwijst** (die gaan in de feedbackstijl of de modelinstructie)
- welke feitelijke beweringen **niet klopten** (dat is een modelprobleem, geen instellingsprobleem)

Dat landt in `GTM/Accounts/<instelling>/` en, als het breder geldt dan een instelling, als voorstel in `Platform/`.

## Wat je nooit doet

- **Een kolom verzinnen omdat de output ontbreekt.** Geen Eduface-output betekent geen dossier voor dat vak.
- **Een naam op papier zetten.** De nakijker heet nakijker.
- **Een onverifieerde bewering van het model als feit printen.** Zie stap 5.
- **De nakijker het onderwerp van de zin maken.** Zie stap 6.
- **Meer dan drie vragen per pagina.** Drie worden beantwoord, tien worden overgeslagen.
- **Een verschil wegpoetsen omdat het ongemakkelijk is.** Een groot verschil is de reden dat je er zit.
