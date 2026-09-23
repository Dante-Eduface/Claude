---
name: grading-calibration
description: Kalibreert Eduface's AI-beoordeling (beoordelingsformulier/rubric + modelinstructies) per vak tegen het echte oordeel van een nakijker, zonder zelf feedback te schrijven, en levert waar nodig een printbaar vakdossier op voor een testdag met de instelling. Trigger bij "fine-tune dit vak", "de AI beoordeelt te streng/te soepel bij [vak]", "kalibreer de modelinstructies", "doe hetzelfde als bij manuele therapie voor [vak]", "vakdossier", "testdag voorbereiden", of wanneer Dante een Eduface-output en een ingevuld beoordelingsformulier aanlevert.
---

# Kalibreren: Eduface naast de nakijker

Eduface's AI beoordeelt via twee losse instellingen per vak: het **beoordelingsformulier** (rubric, Voldoende/Onvoldoende-tekst per criterium) en de **modelinstructies** (context, toon, beoordelingsstrengheid).

Het doel is niet aantonen dat het model gelijk heeft. Het doel is **erachter komen welke norm de opleiding hanteert**, door precies de plekken op te zoeken waar het model en de nakijker uit elkaar lopen, en daar een vraag of een fix van te maken.

Een verschil is bijna nooit een fout van een van de twee. Het is bijna altijd een **aanname**: het model leest iets in de rubriek dat er letterlijk wel staat maar zo niet bedoeld is, of het legt een standaard aan die in dit vak niet geldt. Die aanname is de hele opbrengst van dit traject. Vind hem, en maak er een fix of een vraag van.

**Kernregel (Dante, 22-09-2026): we schrijven nooit zelf feedback. We schrijven instructies voor het model die zo goed mogelijk aansluiten bij de content van het vak.**

**Lees eerst `LEERPUNTEN.md` in deze map voordat je begint.** Elk vak levert inzicht op dat de methode scherper maakt, dat landt daar. Sla het niet over omdat het "vast wel hetzelfde is als vorige keer".

## Wanneer gebruiken

- Dante wil de AI-beoordeling van een vak scherper krijgen ("fine-tune dit vak", "de AI is te streng/soepel bij [vak]")
- Een nieuw vak start met dit traject: materiaal plus een nakijker om tegen te toetsen
- Eduface's huidige AI-uitkomst wijkt zichtbaar af van wat de nakijker zelf zou geven
- Er komt een testdag aan en er moet een vakdossier geprint worden

## Wat er moet liggen

Minimaal:
- **de rubriek of het beoordelingsformulier** van de opleiding, blanco of ingevuld
- **minstens een ingevuld formulier** van een nakijker over concreet studentwerk
- **de Eduface-output** over datzelfde studentwerk

Ontbreekt de Eduface-output, dan kun je de vergelijking niet maken. Zeg dat, en lever het standaardblad in plaats van een dossier (stap 7). Verzin geen kolom.

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

### Ook voor de koppen

Kort en plat. "Feedback van Eduface", niet "De volledige feedback van Eduface". "Aannames van het model", niet "De aannames die het model doet". Een kop die uitlegt wat eronder staat is een kop te veel, en leest als machinetekst.

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

Vaste opbouw per student:

| Blad | Wat erop staat |
|---|---|
| 1 | De beoordeling naast elkaar met de verschillen gemarkeerd, drie totalen, de letterlijke feedback van de nakijker, plus ruimte voor aantekeningen |
| 2 | De volledige feedback van het model, per criterium, letterlijk |
| 3 | Waar het uiteenloopt: twee of drie plekken, beide teksten eronder, een vraag per plek |
| 4 | De aannames van het model, met de vriendelijke vragen en schrijfruimte |

Kop: **Eduface testdag** als titel, daaronder de opleiding, daaronder het vak, de student en de datum van de oorspronkelijke beoordeling. Geen naam van de nakijker.

Kolomkoppen in de tabel: **Nakijker** en **Eduface**. Niet "wat jullie zeiden".

Bouwen doe je volgens `Design/System/core/` plus `internal/`, en renderen met headless Chromium naar A4. Een werkende, geteste opzet staat sinds 23-09-2026 (Breederode, manuele therapie) in `GTM/Accounts/breederode-hogeschool/testdag/`: `blad.html` + `dossier.css`/`base.css` voor de bron, `bouw-map.py` voor de doorlopende nummering en de beoordelingsoptie op blad 1. Begin daar, niet blanco. Die map staat op branch `claude/confident-planck-9s4spe`, nog niet samengevoegd naar main — haal hem op voor je opnieuw bouwt.

## Stap 7-bis: het formulier volgt de rubriek, niet een sjabloon

Het aantal rubriekcriteria verschilt per vak. Acht bij de een, tien of twintig bij de ander, en soms heet het geen rubriek maar een lijst criteria. **Tel ze in het echte beoordelingsformulier en bouw het blad daarop.**

- Ken je de criteria, druk ze dan voor. Dat scheelt schrijfwerk en voorkomt dat twee mensen hetzelfde criterium anders noemen.
- Ken je ze niet, zet dan genummerde regels neer met ruimte om het criterium zelf op te schrijven, en zeg erbij dat je ze niet had.
- Nooit acht rijen neerzetten omdat het vorige vak er acht had.

## Stap 7a: de beoordelingsoptie hoort op blad 1

Eduface heeft per opdracht een beoordelingsoptie aanstaan, en die bepaalt hoe de feedback eruitziet. Staat dat er niet bij, dan weet de lezer niet waar hij naar kijkt en gaat het gesprek over de verkeerde dingen.

Zet onder de naamregel op blad 1 van elk mapje:

| Regel | Wat erin staat |
|---|---|
| **Gekozen** | de optie, in het Nederlands, nooit in het Engels |
| **Wat dat doet** | een zin over wat het model dan wel en niet uitspreekt |
| **Waarom deze** | **alleen bij descriptief beoordelen**, zie hieronder |

### De opties in het Nederlands

De tool noemt ze in het Engels. Op papier gaan ze in het Nederlands, in de woorden die de opleiding zelf gebruikt.

| In de tool | Op papier | Wanneer |
|---|---|---|
| pass/fail grading | **voldaan of niet voldaan**, per rubriekcriterium | als de rubriek van de opleiding zelf ook maar twee standen kent |
| descriptive grading | **onvoldoende, voldoende, goed of uitstekend**, per rubriekcriterium | als de rubriek kwaliteitsniveaus onderscheidt |

Vertaal ook de labels binnen het dossier mee: geen PASS en FAIL in de tabel, maar voldaan en niet voldaan.

### Waarom alleen bij descriptief

Bij voldaan of niet voldaan is de keuze vanzelfsprekend, want de rubriek doet het zelf al zo. Daar hoort geen uitleg bij, die leest als verantwoording voor iets wat niemand betwist.

Bij descriptief beoordelen is de keuze wel uitlegbaar, en die uitleg hoort erbij. Baseer hem op de rubriek van die opleiding zelf, nooit op een algemeen verhaal:
- wat onderscheidt hun rubriek dat een vinkje zou weggooien
- hoeveel niveaus hun rubriek kent, en hoeveel de tool kent

**Lopen die aantallen uiteen, zeg dat er dan bij.** Kent de tool vier niveaus en de rubriek drie, dan is dat geen detail maar de eerste vraag van die ochtend.

## Stap 7b: de oplage, per vak en per student

Reken nooit in een totaal. Een totaal is niet te sorteren op de ochtend zelf. Reken per vak, en lever de tabel op.

Per vak heb je twee getallen nodig:

- **P** = het aantal mensen dat bij dit vak hoort en die dag aansluit
- **S** = het aantal studenten van wie werk beoordeeld is, meestal twee

Daaruit volgt:

| Wat | Aantal | Waarom |
|---|---|---|
| **mapjes** | P | een per persoon, niet per student |
| **bladen per mapje** | (S x 4) + (aantal andere vakken) | vier bladen per studentdossier, plus een beoordelingsformulier per andere opdracht |
| **studentenopdrachten** | P x S | los erbij, iedereen krijgt het werk van elke student |
| **reserve** | +1 mapje per vak | voor wie onaangekondigd aansluit |

Wie bij geen vak hoort krijgt geen mapje maar losse beoordelingsformulieren, een per opdracht.

Is van een student de output van het model er niet, dan telt die student niet mee in S. Verzin geen dossier, zie stap 5. Ontbreekt het dossier voor een heel vak, dan gaat dat vak die ochtend met het losse standaardblad (`beoordelingsformulier-testochtend.pdf` in het Breederode-voorbeeld), niet met een verzonnen mapje.

Lever het als een tabel met een regel per vak, niet als een zin. Dante print hiervan en moet het in een oogopslag kunnen stapelen. **Reken de opgave altijd na tegen het echte, gerenderde PDF-bestand** (paginacount, niet de aanname in dit document): de formule hierboven is de vuistregel, het gerenderde bestand is de waarheid.

## Stap 7c: het mapje

Een mapje is wat een deelnemer in handen krijgt: een nette stapel op volgorde, doorlopend genummerd, met de opdracht van de student er los naast.

| Blad | Wat |
|---|---|
| 1 tot 4 | Het dossier van student 1. Blad 1 draagt ook de naamregel en de beoordelingsoptie. |
| 5 tot 8 | Het dossier van student 2 |
| daarna | Een beoordelingsformulier per andere opdracht van die dag |
| los | De opdracht van de student zelf, ongenummerd |

- **Geen voorblad.** Een inhoudsopgave van zes bladen is een blad dat niemand leest. Begin bij de beoordeling.
- **Doorlopende nummering over het hele mapje**, als "pagina 3 van 10". Niet per onderdeel opnieuw beginnen, want dan valt de stapel uit elkaar zodra iemand hem neerlegt.
- **Links in de voet de opleiding**, zodat een los blad terug te vinden is.
- **De opdracht van de student blijft los.** Die is te dik om in te binden en wordt ernaast gelegd.

## Stap 8: terug naar het model

Wat de testdag oplevert gaat weer het model in. Per vak leg je vast:

- welke aannames de opleiding **bevestigt** (die mag het model houden)
- welke aannames de opleiding **afwijst** (die gaan in de feedbackstijl of de modelinstructie)
- welke feitelijke beweringen **niet klopten** (dat is een modelprobleem, geen instellingsprobleem)

Dat landt in `GTM/Accounts/<instelling>/` en, als het breder geldt dan een instelling, als voorstel in `Platform/`.

Hoe je een afgewezen aanname omzet in een concrete rubric-fix of modelinstructies-tekst, en hoe je dat test met varianten (alleen rubric, alleen instructies, allebei, tegen een vaste baseline): dat is een ander soort werk dan dit dossier, met eigen valkuilen. Zie **Kritieke valkuilen** hieronder en de volledige aanpak in `reference.md`.

## Kritieke valkuilen (kosten anders een testronde)

- **Eduface's eigen PDF-naar-rubric vertaling is niet deterministisch.** Hetzelfde bronbestand twee keer uploaden geeft andere bewoording, soms met een net strengere lezing erin (bijv. "navolgbaar" of "expliciet" die er zelf bij komen). Plak dus altijd een vaste, eigen tekst in elke opdracht, vertrouw nooit op een verse auto-generatie als controle-basis.
- **Modelinstructies zijn nooit direct bewerkbaar**, alleen via "Beschrijf je feedbackstijl" + "Opnieuw genereren", en die stap comprimeert. Concrete voorbeeldzinnen en de Inline-opmerkingen-sectie overleven dat zelden, ook niet met een expliciete "gebruik dit letterlijk"-instructie. Zie `reference.md` voor wat wel overleeft en hoe je daar het meeste uithaalt.
- **Het eindoordeel (Voldaan/Onvoldoende) is een handmatige keuze van de docent in Eduface**, geen automatische optelsom van de gewogen criteria. Optimaliseer dus op de losse criteria, niet op de weging.
- **Het echte gat is meestal geen kennisgat maar een drempelgat.** De AI ziet vaak precies wat de nakijker ook ziet, maar zet elk gevonden verbeterpunt om in een fail, waar de nakijker het als groeifeedback binnen een voldoende behandelt. Dat is dezelfde soort aanname als "een hogere standaard aanleggen" in stap 4, alleen dan structureel. Neem dit niet aan, check het via de nakijker's eigen conceptcommentaar op de inzending zelf, als dat bestaat (zie `reference.md`, sectie annotaties uitlezen).

## Wat je nooit doet

- **Een kolom verzinnen omdat de output ontbreekt.** Geen Eduface-output betekent geen dossier voor dat vak.
- **Een naam op papier zetten.** De nakijker heet nakijker.
- **Een onverifieerde bewering van het model als feit printen.** Zie stap 5.
- **De nakijker het onderwerp van de zin maken.** Zie stap 6.
- **Meer dan drie vragen per pagina.** Drie worden beantwoord, tien worden overgeslagen.
- **Een verschil wegpoetsen omdat het ongemakkelijk is.** Een groot verschil is de reden dat je er zit.
- **De beoordelingsoptie in het Engels op papier zetten.** Pass/fail en descriptive zijn schermtaal, geen printtaal.
- **Een oplage als totaal opgeven.** Per vak, anders is het niet te stapelen.
- **Een mapje zonder doorlopende nummering.** Een ongenummerde stapel raakt in de eerste tien minuten door elkaar.
- **Een vast aantal criteria overnemen van een ander vak.** Tel ze in het echte formulier.
- **Een voorblad met een inhoudsopgave.** Begin bij de beoordeling.

## Waar het landt

- Rubric-tekst en modelinstructies: plakklaar in de chat, Dante zet ze zelf in Eduface (geen MCP-toegang tot Eduface, dus geen directe API-actie mogelijk).
- Vakdossier en mapje: als PDF in `GTM/Accounts/<instelling>/testdag/`, plus de HTML/CSS-bron en het bouwscript erbij zodat het volgende vak of de volgende testdag hergebruikt in plaats van opnieuw bouwt.
- Bevindingen die de methode zelf verbeteren, ook uit een volgend vak: in `LEERPUNTEN.md`, met datum en vak.
- Volledig uitgewerkte voorbeelden met echte teksten en vergelijkingstabellen: `examples/`.

## Klaar is

Twee mogelijke eindpunten, afhankelijk van waar je in het traject zit:

- **Kalibreren:** een rubric-tekst en modelinstructies-tekst waarvan de AI-uitkomst, zowel het oordeel als de toon, overeenkomt met wat de nakijker op minstens 2 studenten deed, gedocumenteerd en klaar om te plakken.
- **Testdag:** een geverifieerd, geteld en gerenderd vakdossier per vak (of het standaardblad waar dat niet kan), een oplagetabel per vak op basis van het echte PDF-bestand, en een mapje met doorlopende nummering.
