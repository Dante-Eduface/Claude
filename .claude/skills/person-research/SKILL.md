---
name: person-research
description: Diepgaand, bronnen-gevalideerd onderzoek naar één persoon (prospect, stakeholder, champion, beslisser). Leest niet alleen nieuwsartikelen maar ook hun echte publicaties en onderzoek (PDF's, Google Scholar, HBO-kennisbank, repositories, lectorale redes), denkt na over WAAROM iemand iets zegt, deelt nuances, en flagt onzekerheid expliciet aan Dante in plaats van aan te nemen. Trigger wanneer Dante zegt "onderzoek [persoon]", "research [naam]", "wie is [naam]", "zoek uit wie [naam] is", "diepgaand onderzoek naar [persoon]", of vraagt om een hook / personalisatie / "hoogste in de boom" voor een specifiek persoon.
---

# Person Research

Diep onderzoek naar één persoon, zodat Dante ze scherp kan benaderen (outreach, gesprek, stakeholder-map). De lat: **elke claim is gevalideerd met een bron. Geen aannames.**

Dit is een onderzoeksmethode-skill. Voor de sales-vertaling van wat je vindt, leun op `cro`. Voor het in kaart brengen van meerdere mensen bij één instelling, zie `stakeholder-mapping`. Deze skill gaat over de **diepte per persoon**.

## Twee modi: bepaal deze eerst

**Diepte-modus (standaard).** Eén persoon, je loopt de hele ladder af tot je ze echt begrijpt. Voor een champion, een EB, een gesprek dat je moet voorbereiden. Alles hieronder geldt onverkort.

**Batch-modus.** Een wachtrij van mensen, en per persoon is één bruikbaar haakje genoeg. Je **stopt bij de eerste treffer waar een bericht op kan staan**, ook als dat trap 1 is. De CRM-check en de AI-scan doe je dan per organisatie in plaats van per persoon, en de bronnenlijst blijft verplicht maar wordt korter.

Twijfel je welke modus het is: vraagt Dante om één naam, dan diepte. Levert hij een lijst of een bestand aan, dan batch.

Voor het SHIFT-project (koude outreach naar particuliere opleiders) bestaat een aparte subagent, `shift-research`, die deze skill in batch-modus aanroept met de projectcontext erbij. Werk je aan SHIFT, gebruik die.

## De vier regels (niet-onderhandelbaar)

1. **Geen aannames.** Alles wat je zegt is een feit met een bron, of je labelt het expliciet als inferentie/aanname. Nooit een gok als feit presenteren.
2. **Lees het echte werk, niet alleen artikelen. En nooit een titel citeren alsof je het gelezen hebt.** Elke scriptie, lectorale rede, paper, blog of pagina die aan de persoon hangt, ga je **actief openen en lezen**. De waarde zit in de inhoud, niet in de titel. "Haar scriptie ging over X" op basis van alleen de titel is verboden: open het document en zeg wat er ín staat.
   - **Blokkade is geen eindpunt.** Als een repository/pagina je tegenhoudt (SPA die niet rendert, HTTP 403/999, loginmuur), probeer je het via een andere route voor je "onleesbaar" concludeert: de **DSpace/repository REST-API** (bv. `…/server/api/discover/search/objects?query=`), `curl` met een browser-`User-Agent`, Google Scholar/cache, ResearchGate, de HBO-kennisbank. Kan Dante de pagina zelf openen (bv. een LinkedIn-profiel achter login), vraag hém dat. Falen alle routes, dan is de eerlijke conclusie simpel: **"niet online te vinden."** Meer niet.
   - **Stel nooit voor om een koude prospect zelf om research-materiaal te vragen.** "Vraag haar scriptie op" bij iemand met wie Dante nog geen contact heeft is geen research-route, het is onzin-advies. Is iets niet publiek, zeg dat gewoon en ga door met wat je wél hebt.
   - **Copy vertelt alleen waarheden, letterlijk.** Deze eerlijkheid loopt door tot in élke mail of tekst die je uit de research schrijft. Refereer precies aan wat je echt hebt gelezen: las je alleen de abstract, schrijf dan "ik las de abstract van je scoping review", niet "ik las je scoping review" of "je paper". Nooit lezing, diepte of instemming suggereren die je niet hebt geverifieerd. Bij twijfel: zwakker en waar boven sterker en gegokt.
   - Nieuwsberichten zijn een startpunt, niet de bron. Zie `reference.md` voor de bron-hiërarchie en hoe je PDF's uitleest.
3. **Denk na over het WAAROM.** Bij alles wat iemand publiek zegt: reconstrueer de context en het motief. Tegen wie zei die dit, waarop reageerde die, wat wil die bereiken? Een citaat zonder context leidt tot de verkeerde hook. (Voorbeeld: "ik wil niet verrast worden door leveranciers" ging over hun huidige leveranciers, niet over een cold outreach van ons.)
4. **Flag onzekerheid, verzin niks.** Kun je iets niet hard maken, of kan een interpretatie meerdere kanten op? Zeg dat, en leg het aan Dante voor: **"Dante, lees dit: [bron/citaat]. Wat zie of versta jij hieruit?"** Dante ként de context vaak beter. Papier onzekerheid nooit dicht met een zelfverzekerde gok.

## De loop

```
1. SCOPE     wie precies (naam + instelling + rol), en waarvoor (outreach / map / hook)
2. CRM-CHECK Close doorzoeken op de persoon ÉN op de instelling/collega's — bestaat de lead al, wie is er al gesproken, wat staat er in de notities? (altijd, eerst)
3. FAN-OUT   parallelle web-searches: naam+instelling, naam+rol, naam+onderwerp, naam+publicaties
4. VERIFY    identiteit vaststellen — juiste persoon? (naamsverwarring is regel 1 van de fouten)
5. DEEP READ hun eigen bronnen: bio's, instituutpagina, publicaties, redes, posts, interviews
6. AI-SCAN   welke AI-toepassingen, tools, LMS, beleid en werkgroepen draaien er al bij de instelling? (altijd doen)
7. WHY       per uitspraak/positie: context + motief reconstrueren
8. DELIVER   samenvatting + hooks (met bron + fact/inferentie-label) + CRM-historie + AI-landschap + expliciete onzekerheden
```

## CRM-check: kijk eerst in Close én Gmail (altijd)

Voor je iemand als "koud" behandelt, doorzoek **altijd** Close **en Gmail**, op twee niveaus:
1. **De persoon zelf** — bestaat er al een contact/lead? Is er al gemaild, gebeld, een meeting geweest? Zoek in Gmail ook op het maildomein van de organisatie.
2. **De instelling en collega's** — zoek op de organisatienaam. Vaak zit de persoon in een account waar Dante al collega's van heeft gesproken. Lees die lead: welke contacten staan erop, wie is de relatie-eigenaar, welke status, welke open taken.

Lees de **notities en activiteiten** en leer eruit: wat is er afgesproken, welke timing is genoemd ("interessant vanaf eind september"), welk project loopt er, wie toonde interesse, wie is de product owner / beslisser. Dit bepaalt of je iemand koud mag benaderen of dat je juist moet aansluiten op een lopende relatie en afspraak. **Iemand koud pitchen die al in een warme deal zit, is de grootste fout** (zie ook de bron-hiërarchie in `reference.md`: intern eerst). Botst je outreach met wat een collega al heeft afgesproken, stem dat af met Dante voor je stuurt.

## AI-scan van de instelling (altijd meenemen)

Bij elk persoon-onderzoek breng je **altijd** ook de bestaande AI-voetafdruk van hun instelling in kaart. Reden: Eduface komt bijna nooit in een greenfield binnen, en de verkeerde aanname ("ze doen nog niks met AI") maakt je meteen ongeloofwaardig bij een poortwachter. Zoek gericht op:

- **LMS / digitale leeromgeving** — Brightspace, Canvas, Moodle? Noem in outreach nooit het verkeerde systeem.
- **Bestaande AI/feedback/toets-tools** — CodeGrade, FeedbackFruits, Ans, Turnitin, eigen gebouwde GenAI-tools, etc. Wat doen ze wél en wat is het gat dat Eduface vult?
- **AI-beleid & richtlijnen** — mag AI in toetsing? Formatief vs. summatief? Data/soevereiniteit-standpunt?
- **AI-groepen & mensen** — taskforces, special interest groups, TLC/CILT/ICTO-teams, hackathons, wie trekt AI in het onderwijs?

Vertaal dit naar positionering: het gat dat de incumbents openlaten, het juiste LMS om te noemen, en de rode lijnen (bv. "AI niet voor summatieve shortcuts") die je niet moet raken. Elke bevinding met bron.

## Visitatierapporten: bij opleiders bijna altijd de beste vindplaats

Bij elke Nederlandse onderwijsinstelling zoek je **actief** naar het meest recente NVAO-visitatierapport. Dit is geen optioneel extraatje: het is het enige openbare document waarin een onafhankelijk panel opschrijft hoe de toetsing er echt aan toegaat, en het levert citaten op die geen enkele prospect kan wegwuiven. Even waardevol voor mail en LinkedIn als voor een cold call.

Zoek op `NVAO visitatierapport "<organisatie>" toetsing`. De PDF's staan op `publicaties.nvao.net` en zijn via een gewone zoekopdracht vindbaar. De instellingspagina's op `nvao.net` geven vaak 404, zeker na een naamswijziging. Uitlezen gaat via `reference.md`, inclusief de waarschuwing over afgebroken woorden.

Waar je op grept, meestal in het hoofdstuk Toetsing:

| Zoekwoord | Waarom |
|---|---|
| `feedback` | vooral waar studenten zeggen dat ze het níet krijgen |
| `matief` | formatief werken, en wat zij daar zelf onder verstaan |
| `navolgbaar` | consistentie van cijfers, een veelvoorkomend aandachtspunt |
| `kalibr` | kalibratiesessies, meestal "we zijn ermee bezig" |
| `\bAI\b` | staat AI in de aanbevelingen, dan is dat je haakje |
| `afstudeer`, `scriptie` | omvang en aantal eindwerken |
| `leeromgeving` | het LMS staat meestal bij Voorzieningen |
| `werkdruk`, `capaciteit` | zelden raak, maar goud als het er staat |

Let daarbij op:
- **Rapporten zijn per opleiding, niet per instelling.** Zeg "in het rapport van opleiding X", niet "bij jullie", tenzij je ze allemaal hebt gelezen.
- **Kijk naar de accreditatiehistorie** op de besluitenpagina. Een oude onvoldoende die inmiddels hersteld is, is nuttig om te weten en dodelijk om te noemen.
- **Een panelbevinding is niet van de persoon.** Zoek de naam van je contact in het rapport. Staat die er niet, dan is het "de opleiding" en schrijf je "jullie", nooit "jij hebt".
- **Een NVAO-vakterm is geen gewone taal.** `studeerbaarheid`, `studielast` en `toetslast` gaan over de **student**, niet over de docent. Noteer bij elk citaat wie de last draagt (student, beoordelaar, organisatie, panel) en zet die drager erbij. De vaste betekenissen staan in `Platform/Product/onderwijs-vaktermen.md`. Dit kostte op 13-08-2026 de THIM-lead.
- Bij particuliere opleiders zonder NVAO-erkenning: zoek in plaats daarvan naar het **NRTO-keurmerk, CRKBO, CEDEO, NLQF-inschaling** en het jaarverslag of verslag van werkzaamheden.

## Drie dingen die je bij een opleider altijd opzoekt

**1. De onderwijsvisie.** Zoek `"<organisatie>" onderwijsvisie` of `onderwijsconcept` of `visie op toetsing`. Veel opleiders publiceren in hun eigen woorden hoe ze naar leren en beoordelen kijken, en dat sluit verrassend vaak recht op Eduface aan. De ASRE-visie zet bijvoorbeeld letterlijk formatieve toetsing met de nadruk op feedback centraal. Dit levert bovendien het grootste deel van de woordenlijst.

**2. Het organigram.** Zoek het organogram of de organisatiestructuur op. Volg daarbij de **onderwijstak**, niet de bedrijfsvoeringstak. Bij SOMT valt Leven Lang Leren onder Bedrijfsvoering terwijl de baas van de opleidingen het Hoofd Onderwijs & Onderzoek is. Wie de verkeerde tak volgt, komt bij iemand uit die niets te zeggen heeft over onderwijs.

**3. Het LMS.** Welk systeem draaien ze: Brightspace, Canvas, Moodle, itslearning, Fronter, of iets eigens? Integratie bepaalt adoptie, dus dit is geen detail. Staat het niet in het visitatierapport bij Voorzieningen, dan is het vaak te vinden in een vacature, een studentenhandleiding of de inlogpagina. Vind je het niet, meld dat als open vraag in plaats van te gokken. De beheerder van dat systeem is een aparte stakeholder (`lms-integratie-altijd-meenemen`).

## Werkt deze persoon er nog?

Voor je iemand benadert: check of ze er nog werken **en** of hun functie nog binnen de ICP valt. Verifieer via LinkedIn, dat is de enige bron met einddatums (`verify-contact-still-employed`, `linkedin-is-hoofdbron`). Een eigen site die geen namen noemt is geen reden om een contact te laten vallen, maar een LinkedIn-profiel met een einddatum wel.

## Het toetsprogramma: leg dit per organisatie vast

Voor elke opleider noteer je drie dingen, want zonder die drie kun je geen enkel bericht schrijven dat ergens over gaat (`toetsprogramma-eerst`):

1. **Wat leveren lerenden in?** Scripties, beroepsproducten, portfolio's, reflectieverslagen, meerkeuze-examens, praktijkopdrachten
2. **Hoeveel en hoe vaak?** Per module, per blok, per jaar
3. **Wie kijkt het na?** Vaste docenten, freelancers, examinatoren, praktijkbegeleiders, een externe beoordelaar

## De zoekladder (waar je zoekt, in welke volgorde)

Goedkoop eerst. Anders dan in batch-modus (`shift-research`) stop je hier **niet** bij de eerste treffer: je loopt de ladder af tot je de persoon echt begrijpt. Wel in deze volgorde, zodat je niet begint met de duurste route.

| Trap | Wat | Kosten |
|---|---|---|
| 1 | Websearch op `"naam" + instelling`, en op `"naam" interview` | gratis |
| 2 | LinkedIn-profiel: headline, about, beschrijvingen onder de functies | een directe `WebFetch`/curl op `linkedin.com/in/...` geeft vrijwel altijd HTTP 999 (LinkedIn's bot-blokkade), dat is de norm, geen uitzondering. Bij 999 ga je meteen door naar trap 7, niet pas na trap 3-6 |
| 3 | Teampagina / "over ons" / instituutpagina van de eigen site | gratis |
| 4 | De instelling: AI-pagina, visiestuk, handboek, jaarverslag, NVAO-rapport, nieuws | gratis |
| 5 | **Hun echte werk**: publicaties, scriptie, lectorale rede, papers, repositories, Scholar, HBO-kennisbank. Openen en lezen, zie regel 2 | gratis |
| 6 | Vakbladen, congresprogramma's, podcasts, brancheorganisatie | gratis |
| 7 | **Apify**, via de `linkedin-profile-scraper` skill. Voor het LinkedIn-profiel zelf (trap 2) is dit geen laatste redmiddel maar de normale route zodra je de 999 ziet. Voor de rest van de ladder (trap 1, 3-6) blijft het wel: alleen inzetten als die te weinig opleverden | circa 0,4 cent per profiel |

Bij Apify: eerst het profiel (headline → about → functiebeschrijvingen). Levert dat niks op, dan pas de eigen posts, met `includeReposts` en `includeQuotePosts` op false. Vacatureposts negeer je meteen, die zeggen niks over wat iemand belangrijk vindt.

## Elke hook krijgt een niveau

Een hook zonder niveau is niet af. De ladder staat uitgewerkt in `.claude/skills/linkedin-outreach/haakje-zoeken.md`, lees dat als je hooks gaat opleveren. Kort:

- **Niveau 3** — je maakt iets op basis van hun eigen idee en geeft het weg, krediet volledig naar hen
- **Niveau 2** — je ziet iets in hun situatie dat zij zelf niet hebben gezegd, en trekt daar een consequentie uit
- **Niveau 2b** — de eerlijke non-sequitur: iets menselijks en zichtbaars, waarbij je zelf toegeeft dat het niks met je reden te maken heeft
- **Niveau 1** — citeren en dan pitchen. Niet goed genoeg, iedereen doet dit

Twee tests voor je een niveau toekent:
1. **Had dit ook naar honderd anderen gekund?** Ja → geen niveau 2.
2. **Waarom stuurt uitgerekend Dante dit, en waarom nu?** Kun je dat niet in één zin, dan ontbreekt de why-now.

Lever een niveau 1 gewoon aan met het label erbij. Niet weggooien, Dante haalt er soms nuance uit. Maar schrijf het niet mooier op dan het is.

## Identiteit eerst (voorkomt de grootste fout)

Voor je iets over "de persoon" zegt: bevestig dat de LinkedIn/bron echt die persoon is. Veelvoorkomend: een aangeleverde LinkedIn-URL blijkt iemand anders met dezelfde naam. Check functie + instelling + locatie tegen elkaar. Twijfel je, flag het.

### De functietitel komt uit twee bronnen

**Nooit de titel overnemen die Dante of een lijst aanlevert.** Die klopte bij vier van de eerste negen contacten niet. Maak hem hard uit **twee** onafhankelijke bronnen, en noem het verschil expliciet als die er is:

- **LinkedIn is hoofdbron** (`verify-title-on-org-source`, `linkedin-is-hoofdbron`). Gebruik de headline plus de huidige functie mét datums, niet een skill-tag.
- **Tweede bron:** hun eigen site (teampagina, persruimte, bestuurspagina), een persbericht, of een NVAO-rapport.
- Verschillen komen vaak door een **reorganisatie of overname**: iemand was algemeen directeur en is na een overname directeur onderwijs geworden. Zeg dat, dan weet Dante dat hij het in het gesprek moet checken.
- Twee bronnen die elkaar tegenspreken is geen probleem, één bron die je als zekerheid presenteert wel.

**Check ook de organisatienaam.** Namen op een aangeleverde lijst zijn regelmatig fout of verouderd: HAEBO+ bleek Habeo+, UE Amsterdam heette eerder IC University en daarvoor Inter College, Avans+ heet sinds oktober 2025 Habeo+. Corrigeer het meteen en zeg het erbij.

**Verwar een dochter niet met de moeder.** Habeo+ is niet Avans Hogeschool, UE Amsterdam is niet Avans, Notenboom valt sinds maart 2025 onder BSN. Het beleid van de moeder toeschrijven aan de dochter is een van de duurste fouten die je kunt maken, juist omdat de verzelfstandiging vaak het project van je contactpersoon is.

## Wat je oplevert

- **CRM-historie:** wat Close al weet over deze persoon en hun instelling — bestaande lead/status, eerder contact met collega's, notities, afgesproken timing, lopende projecten. Áltijd checken en meeleveren, zodat Dante niemand koud benadert die al in een lopende relatie zit.
- **Persoons-samenvatting:** rol, mandaat, achtergrond, waar ze echt over gaan.
- **Functietitel met twee bronnen**, en het verschil benoemd als de aangeleverde titel afwijkt.
- **Hoogste in de boom** (indien gevraagd): wie is de echte beslisser boven/rond deze persoon, met namen + functies + bron. Kijk daarbij specifiek of er een **laag onderwijs of kwaliteit** onder de directie zit. Bestaat die niet, zeg dat, want dan is de directeur alsnog de juiste ingang maar met een andere vraag. **Examencommissie is een harde nee**, opleidingsmanager alleen als er niets hogers is (`never-examencommissie-opleidingsmanager-meh`).
- **Toetsprogramma**: wat leveren lerenden in, hoeveel, en wie kijkt het na.
- **Woordenlijst**: een tabel met links het woord dat Dante zou gebruiken en rechts het woord dat zij zelf gebruiken, uit hun eigen materiaal. Toets versus examen, student versus deelnemer versus cursist, opdracht versus beroepsproduct, consistentie versus navolgbaarheid. Dit is wat een bericht of gesprek laat landen, en het is even hard nodig voor een mail of LinkedIn-bericht als voor een telefoontje.
- **Hooks:** 1-2 concrete, te-verifiëren haken per persoon, elk met **bron + jaartal**, een **fact vs. inferentie**-label en een **niveau** (1 / 2 / 2b / 3). Sluit aan op `claims-need-sources`.
- **AI-landschap van de instelling:** bestaande AI-toepassingen, LMS, beleid en groepen, plus wat dit betekent voor de Eduface-insteek (het gat, het juiste LMS, de rode lijnen). Altijd meeleveren.
- **Bronnenlijst:** áltijd een expliciete lijst met de gebruikte bronnen (links), gesplitst naar primair / secundair / tertiair. Dante wil elke keer kunnen doorklikken en zelf checken. Geen research-oplevering zonder bronnen. Sluit aan op `claims-need-sources`.
- **Onzekerheden:** een apart lijstje van wat je niet hard kreeg, met de "lees dit, wat zie jij?"-vraag aan Dante.

Broneerlijkheid boven volledigheid. Vind je niks over iemand, zeg dat gewoon. Een eerlijke "niks gevonden" is meer waard dan een verzonnen hook.

**Waar het heen gaat.** Een oplevering die alleen in de chat staat, bestaat na afloop niet meer. Dat is precies waarom er van diep onderzoek zo weinig overbleef voor de volgende stap.

- Zit de persoon in de NL-opleiderspijplijn, dan schrijf je het weg als dossier: `pipeline.py dossier <person_id> --schrijf - --actor <skill>`. De koppen hierboven mappen één op één op de koppen in `GTM/Campaigns/shift/master/dossiers/SJABLOON.md`, inclusief de bronnenlijst en de onzekerheden.
- Gaat het om een cold call, dan geldt de oplevering uit `cold-call-prep` (`GTM/Campaigns/cold-calling/<naam>.md`).
- **Elk citaat krijgt zijn drager mee** (student, beoordelaar, organisatie, panel). Zie `Platform/Product/onderwijs-vaktermen.md`. Zonder dat label kan de volgende stap er de verkeerde kant aan geven, en dat is bij THIM gebeurd.

## Diepte-technieken

Zie `reference.md` in deze map voor: de bron-hiërarchie (primair/secundair/tertiair), waar je academisch werk vindt (Scholar, HBO-kennisbank, ResearchGate, SURF, instituut-repositories), hoe je PDF's uitleest (pypdf), de WHY-analyse in detail, en het onzekerheid-protocol.

## Done

- Elke claim heeft een bron of een expliciet aanname-label.
- **Elk aan de persoon gekoppeld document/pagina (scriptie, rede, paper, profielpagina) actief geprobeerd te openen en gelezen** — niet op titel geciteerd. Blokkades via een alternatieve route geprobeerd (REST-API, curl+UA, cache, Dante) en pas daarna als "niet openbaar" gelabeld.
- Nuances en onzekerheden apart benoemd en aan Dante voorgelegd waar nodig.
- Hooks zijn concreet en bruikbaar in een mail/gesprek, met een niveau erbij. Kom je niet boven niveau 1 uit, zeg dat dan gewoon.
- **Close én Gmail gecheckt op de persoon ÉN de instelling/collega's** — bestaande lead, status, eerder contact, notities en afgesproken timing gelezen en meegewogen. Nooit iemand koud benaderen die al in een lopende relatie zit.
- **Functietitel uit twee bronnen**, organisatienaam geverifieerd, moeder en dochter niet verward.
- **Visitatierapport gezocht** en, als het bestaat, zelf uitgelezen. Toetsprogramma en woordenlijst vastgelegd.
- **AI-scan van de instelling gedaan en meegeleverd** — bestaande tools, LMS, beleid en groepen, vertaald naar de Eduface-insteek. Nooit overslaan.
- **Bronnenlijst meegeleverd** — expliciete links, gesplitst primair/secundair/tertiair. Nooit een oplevering zonder bronnen.
