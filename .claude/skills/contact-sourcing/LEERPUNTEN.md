# Leerpunten agent 2

Append-only. Elke correctie op een aangewezen persoon komt hier, ook als er nog geen regel uit volgt. Lees dit bestand voordat je een ronde begint.

Format: `[JJJJ-MM-DD] persoon of organisatie: wat er mis was | welke stap het was | wat ermee gedaan is`

## Waarom dit bestand bestaat

Wijs je de verkeerde persoon aan, dan onderzoekt agent 3 hem en schrijft agent 4 een bericht aan iemand die er niet over gaat. Het bericht kan perfect zijn en toch nergens landen. Dit bestand is het geheugen tussen de rondes.

## Feedback die werkt

| Stap | Wat er dan mis is | Bruikbare feedback klinkt als |
|---|---|---|
| **De route** | verkeerde tak van het organogram | "je zit in de bedrijfsvoeringstak, het onderwijs valt onder iemand anders" |
| **Het niveau** | te laag of te hoog in de boom | "een examencommissie koopt nooit iets, die is risico-avers" |
| **De titel** | de functietitel is verkeerd gelezen of verouderd | "hij is daar weg sinds mei, kijk naar de einddatum op LinkedIn" |
| **De verificatie** | niet gecheckt of hij er nog werkt | "dit contact komt uit een oude export, niet geverifieerd" |
| **De tiebreak** | de verkeerde van twee kandidaten | "die ander staat hoger en is al eens benaderd" |
| **Het kanaal** | er liep al iets bij deze persoon | "hier loopt een cold call, geen connectieverzoek erbovenop" |

## Log

- [2026-07-23] algemeen: nooit een docent aanwijzen als ingang. | Het niveau: een docent gaat niet over de inrichting van het beoordelen. | Vaste regel in SKILL.md.
- [2026-08-xx] algemeen: examencommissie is een harde nee, opleidingsmanager alleen als er niets hogers is en dan met directeur of hoofd onderwijs als tweede kandidaat. | Het niveau: een examencommissie is risico-avers en koopt niets. | Vaste regel, zie memory never-examencommissie-opleidingsmanager-meh.
- [2026-09-xx] algemeen: verifieer de functietitel via LinkedIn, niet via de eigen site. | De verificatie: LinkedIn klopte 12 van de 12 keer op werkgever, de site 7 van de 12, en alleen LinkedIn heeft einddatums. | Vaste regel, zie memory linkedin-is-hoofdbron.
- [2026-09-16] 21 van de 185 aangewezen NL-contacten: functietitels als Opleidingsdirecteur, Director, Owner, Rector en Academic Director scoorden 50 in de titelrangorde, lager dan een gewone manager. | De tiebreak: de rangorde in profiel.json kende die titels niet, dus de vergelijking tussen kandidaten klopte niet. | Rangorde aangevuld met de Engelse titels en de samenstellingen. Onbekende titels van 68 naar 2.
- [2026-09-17] Besluit Dante: e-mailadres actief zoeken (één standaardpagina per persoon), niet alleen noteren als je het toevallig tegenkomt. Eerste versie van deze regel (eerder diezelfde dag) was te passief, teruggedraaid. | Mailadres. | Sectie "Mailadres" herschreven: check eerst of `email` al gevuld is (dedup met agent 3, wie de persoon het eerst tegenkomt zoekt), zo niet bezoek één standaardpagina (staffpagina/teampagina van de organisatie), zo niet dan `email_status=niet gevonden` en geen tweede poging. Reden: Lemlist's enrichment kost Dante credits die een gerichte zoekactie hier niet kost.
- [2026-09-17] Besluit Dante: telefoonnummer meenemen als bijvangst, net als e-mail vóór de correctie hierboven — géén aparte zoekactie, wel meeschrijven als je het toevallig ziet. | Nieuw veld `telefoon` (na `email_status`). | Regel toegevoegd bij "Mailadres" in SKILL.md. Veld toegevoegd aan PERSON_COLS in pipeline.py, met uitleg via `pipeline.py uitleg telefoon`.
- [2026-09-18] structureel, geen sessie-fout: in een sessie zonder de LinkedIn-scraper-skill en zonder Clay-MCP geladen (alleen WebSearch/WebFetch) is de verplichte in-dienst-check op de meeste UK-stage-2-organisaties niet uit te voeren. WebFetch op LinkedIn-bedrijfspaginas geeft alleen een paar willekeurige medewerkers zonder titel; WebSearch vindt bij veelvoorkomende namen alleen naamgenoten. Getest op 6 organisaties (The Language Gallery, Amity University London, Kaplan Financial UK, Cambridge Muslim College, First Intuition, Engineering College of Technology), telkens dezelfde uitkomst als de vorige ronde. | Alle stappen die LinkedIn-verificatie vereisen. | Geen regelwijziging, wel een seintje voor Dante: start deze skill met de linkedin-profile-scraper-skill of Clay-MCP geladen, anders is de wachtrij op resterende harde gevallen niet vooruit te helpen.
