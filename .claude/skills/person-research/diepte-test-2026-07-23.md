# Diepte-test person-research — 23 juli 2026

Vraag van Dante: klopt het dat de skill in batch-modus stopt bij het eerste haakje? Dat kost kwaliteit in het bericht. En wat kost meer diepte eigenlijk?

Getest op 5 personen uit de SHIFT-lijst die nog geen haakje hadden. Eerst de ondiepe pass zoals de skill hem nu doet (stop bij de eerste treffer waar een bericht op kan staan), daarna de diepe pass op dezelfde vijf. Kosten gemeten uit de transcript-logs, niet geschat.

## Wat het per persoon opleverde

### 1. Eiko de Vries — SPO Nyenrode
**Ondiep:** pensioenfondsbestuurder sinds 2000, nu voorzitter Pensioenfonds Recreatie en bestuurslid Kappersbranche, daarnaast docent bij SPO. Niveau 1.

**Diep:** SPO draait al twee eigen digitale platforms. SPO Perform is een microlearning-platform met video's, infographics en checklists. SPO Wtp-proof is een compleet online leerpad rond de Wet toekomst pensioenen. Er is ook een nieuwe leerstoel Pensioentransitie.

**Waarde:** hoog, maar niet als haakje. Het verandert de hele insteek. Ondiep zou een mail opleveren in de trant van "u geeft les bij SPO" tegen iemand wiens organisatie al vol in digitaal onderwijs zit. Belangrijker: microlearning met video's en checklists betekent mogelijk dat er helemaal geen studentwerk beoordeeld wordt. Dat raakt poort 0 van de ICP. Dat zie je ondiep niet.

### 2. Lennaert Eggink — THIM (Thim van der Laan)
**Ondiep:** teamcoördinator en docent, deed een Post-HBO Basis Didactische Bekwaamheid aan de VU in 2017-2018. Niveau 1, en eerlijk gezegd nauwelijks dat.

**Diep:** het NVAO-rapport van de bacheloropleiding Fysiotherapie beschrijft hun hele toetssysteem. Ze toetsen via de hiërarchie van Miller: schriftelijke kennistoetsen, schriftelijke casustoetsen, vaardigheidstoetsen, performance assessments en een beroepsproduct. Afstuderen is een arbeidsproef plus een scriptie, in Nederland te schrijven in groepsverband. En letterlijk: *"Bij de vaardigheidstoetsen en performance assessments spreken de docenten vooraf de criteria en weging bij het beoordelen af om de interbeoordelaarsbetrouwbaarheid te vergroten."* De accreditatie liep tot eind 2025, dus ze zitten nu in of net na een heraccreditatie.

**Waarde:** de grootste van de vijf. Interbeoordelaarsbetrouwbaarheid is precies waar Eduface op zit, en het staat er in hun eigen woorden. Dit is het verschil tussen niveau 1 en een echt niveau 2, bij iemand die "onderwijscoördinator innovatie" is. Plus een why-now uit de heraccreditatie.

**Voorbehoud:** het rapport is een Uitgebreide Opleidingsbeoordeling zonder jaartal in de kop, dus vermoedelijk enkele jaren oud. Gebruiken als "zo staat het in jullie NVAO-rapport", niet als "zo werkt het nu".

### 3. Rosa Brussaard — King nascholing
**Ondiep:** LinkedIn en RocketReach noemen haar Sales account manager en Marketing and Sales manager, met een BBA Media, Marketing en Publishing van de HvA. Ons contactenbestand zegt "Opleidingsmanager". Dat botst. Geen bruikbaar haakje.

**Diep:** op de site van King staat dat de visitatie van praktijkinstellingen wordt gedaan door de hoofdopleider samen met de opleidingsmanager van King nascholing. De opleiding tot Orthopedagoog Generalist heeft één lesdag per week met huiswerk en blokttoetsen, plus 90 uur groepssupervisie en 10 uur individuele supervisie.

**Waarde:** twee dingen. Poort 0 is bevestigd, ze beoordelen zelf werk van lerenden. En de rol opleidingsmanager blijkt een echt mandaat te hebben rond kwaliteit, niet alleen planning. Maar of Rosa díe rol heeft is nog steeds onzeker. Ondiep had hier een sales-persoon een onderwijsverhaal gestuurd.

**Aan Dante:** wil je dat ik voor deze uitzoek of Rosa sales of opleidingsmanager is, of gaan we naar de hoofdopleider?

### 4. Andrea Oosterwijk — Variva Edu Academy
**Ondiep:** vrijwel niets. Aggregators, een testimonial dat ze "weet hoe goed onderwijs eruitziet", en Erasmus Universiteit.

**Diep:** Variva geeft mbo-avondopleidingen (onderwijsassistent, pedagogisch medewerker, sociaal werker) in zes steden, bestaat 20 jaar, werkt met BBL. Er is een inspectierapport "onderzoek naar kwaliteitsverbetering mbo op opleidingsniveau" en het oordeel van de inspectie is "goed". Hun eigen examineringspagina is dun: examinering verschilt per bijscholing.

**Waarde:** matig. Ondiep had nul, diep heeft een organisatie-haakje. Maar het gaat over de organisatie, niet over Andrea. Het inspectierapport zelf kreeg ik niet open (403 en een dode host), dus daar zit mogelijk nog meer.

### 5. Arjan Hietkamp — Hogeschool Scheidegger
**Ondiep:** RocketReach, ContactOut en AeroLeads noemen hem allemaal Directeur Opleidingen bij Scheidegger Opleidingen. Ziet er stevig uit.

**Diep:** zijn LinkedIn, de enige primaire bron, zegt Directeur bestuurder bij VPCO Eerbeek. AeroLeads zet er ook nog Flores Onderwijs bij. Alleen tertiaire aggregators claimen Scheidegger, en die spreken elkaar tegen.

**Waarde:** geen haakje, wel de belangrijkste vondst. Ondiep zouden we iemand hebben aangeschreven als directeur van een organisatie waar hij waarschijnlijk niet meer werkt. Dat is een fout die je één keer maakt.

## Wat het kostte

Gemeten uit de transcript-logs van deze sessie, daarna genormaliseerd naar een schone subagent (deze chat had een opgeblazen context door een geladen skill, dat vertekent per-call kosten flink).

| | ondiep | diep | factor |
|---|---|---|---|
| tool-calls voor 5 personen | 6 | 20 | 3,3x |
| kosten per persoon | $0,04 | $0,19 | 5x |
| doorlooptijd per persoon | ~13 sec | ~32 sec | 2,5x |
| 100 personen | $4 | $19 | |
| 500 personen | $20 | $95 | |

Prijzen op Opus 4.8: $5 per miljoen input, $25 per miljoen output, cache-reads $0,50 per miljoen.

**Kost meer context exponentieel meer?** Nee, maar het is ook niet lineair. Binnen één batch groeit de context bij elke stap, en elke volgende call betaalt over die hele context. Bij 6 calls kost een extra call ~$0,03, bij 20 calls ~$0,055. Dat is kwadratisch binnen een batch, niet exponentieel. Praktische consequentie: batches klein houden (5 tot 8 personen) is goedkoper dan één batch van 15, bij precies hetzelfde werk.

De doorlooptijd valt mee omdat searches parallel kunnen. Diep is 2,5x zo langzaam, niet 5x.

## Conclusie

De regel "stop bij het eerste haakje" is te grof, maar "loop altijd de hele ladder af" ook. Bij Eiko en Lennaert leverde diep echte kwaliteit op. Bij Rosa en Arjan voorkwam het een fout. Bij Andrea was het matig.

Wat er misgaat is niet de diepte op zich, het is dat de skill stopt op het verkeerde signaal. Nu stopt hij zodra er íets is waar een bericht op kan staan, ook een niveau 1. Dat is precies het niveau waarvan we zelf hebben opgeschreven dat het niet goed genoeg is.

**Voorstel: stop op niveau, niet op aanwezigheid.**

- **Trap A, altijd:** één search plus identiteitscheck. Klopt de functie in ons bestand met wat je vindt? Zo nee, stop en leg het voor aan Dante. Dit had Arjan en Rosa gevangen, en kost niets extra.
- **Trap B, alleen als trap A niet boven niveau 1 uitkomt:** maximaal drie extra calls naar organisatiebronnen. NVAO-rapport, examineringspagina, onderwijsvisie, inspectierapport. Daar kwamen bij deze vijf alle niveau-2 haakjes vandaan.
- **Harde stop:** bij het eerste niveau 2, of na drie extra calls. Kom je er niet, lever niveau 1 met het label erbij, zoals nu.

Verwachte kosten daarvan: ongeveer $0,10 tot $0,12 per persoon, want ongeveer de helft haalt niveau 2 al in trap A of vroeg in trap B. Dat is 2,5x de huidige kosten, niet 5x, voor bijna de volledige kwaliteitswinst.

Op de hele SHIFT-lijst van ~300 personen is dat het verschil tussen ongeveer $12 en $33. Dat is geen bedrag om een beslissing op te baseren. De echte afweging is doorlooptijd en de foutkans, en die vallen allebei uit richting diep.

## Wat ik nog niet weet

- De diepe pass die ik draaide was ongelijk verdeeld: gemiddeld drie extra calls per persoon, maar bij Lennaert vier en bij Andrea twee. Een echt uniforme diepe pass (inclusief Apify-scrape en CRM-check per persoon) kost meer dan de $0,19 hierboven, vermoedelijk richting $0,30.
- De CRM-check in Close heb ik in deze test overgeslagen. Die staat in de skill als verplicht en kost per organisatie, niet per persoon.
- Het inspectierapport van Variva kreeg ik niet open. Daar zit mogelijk nog een sterker haakje.
