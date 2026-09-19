# Marktprofiel nl

<!-- Veertien slots. Elke kop moet inhoud hebben, anders weigert `queue`.
     Dit is het NL-profiel, samengesteld op 10-09-2026 uit wat er al lag. De uitgebreide
     versies staan in de bestanden waarnaar verwezen wordt; dit profiel is de ingang. -->

## Registers
Waar agent 1 aanbieders vindt, op volgorde van opbrengst. Stand en dode sporen in `WERKVOORRAAD.md` in deze map.
- **NRTO-ledenlijst** (nrto.nl): kwaliteitskeurmerk particuliere opleiders. Lidmaatschap = bewijs van particulier.
- **CRKBO-register** (crkbo.nl): btw-vrijgestelde beroepsopleiders. Groot, veel eenmanszaken, filteren op omvang.
- **DUO-register erkende niet-bekostigde mbo-opleidingen** (duo.nl/open_onderwijsdata, xlsx): 148 instellingen, aggregeren per BRIN. BRIN 30xx/31xx/32xx zijn particulier, 0xxx/25xx/27xx vrijwel altijd bekostigd.
- **CPION / SNRO / NLQF** voor post-hbo en geaccrediteerde particuliere programma's.
- Dood spoor: bedrijvenregisters op SBI-code (geen crawlbare lijst), awards en ranglijsten (kleine aanbieders), LinkedIn-bedrijfspagina's (HTTP 999).

## Toezichtregime
- **NVAO** (nvao.net): accreditatierapporten van geaccrediteerde particuliere hogescholen en post-hbo. Panels schrijven letterlijk op waar de beoordeling rammelt (NOVI: feedback "vaak wat minimaal"). PDF-route uit `WERKVOORRAAD.md`, want WebFetch faalt op PDF's.
- **Onderwijsinspectie** voor niet-bekostigd mbo, zelden bruikbaar voor beoordelingsdetail.
- Eigen documenten: OER, examenreglement, studiegids. Daar staat wie beoordeelt.

## Poort-0-afvallers
Wie normen stelt of examineert in plaats van zelf te beoordelen. Volledige lijst met gevallen in `icp.md`, kop "Marktgroepen die je kunt negeren".
- Externe examinerende instanties: CBR, CCV, TCVT, Het Oranje Kruis, CerTech, IBKI, SVPB, EXIN, SVH, SVM NIVO, Prometric, Pearson VUE.
- Normzetters en certificeerders zonder eigen lerenden (DSI), koepels en brancheorganisaties, uitgevers en platforms (Wolters Kluwer, Sdu).
- BBL-praktijkopleidingsbedrijven (het ROC toetst), praktijkbeoordelaars zonder geschreven werk (NBZ), eenmanszaken in coaching en therapie.
- Publiek bekostigde instellingen: andere ICP.
- Nuance 07-08-2026: een beroepsvereniging die zelf een verplichte beroepsopleiding draait met eigen beoordeeld werk is functioneel een opleider (NOB, RB Academy, FB).

## Poort-0-vocabulaire
De enige vraag per organisatie: **wie neemt het examen af?** Zoek `"[naam] examen"` of `"[naam] examenreglement"`.
- Eigen beoordeling: "wordt beoordeeld door de docent/examinator/examencommissie", "onze examencommissie", "scriptie", "afstudeeropdracht", "eindwerkstuk", "proeve van bekwaamheid", "portfolio wordt", "beoordelingscriteria", "nakijk", "feedback op je opdracht/verslag".
- Extern: "extern examenbureau", "externe examinator", "onafhankelijk exameninstituut", "staatsexamen", plus de namen onder Poort-0-afvallers.
- Duur: "N maanden/jaar", "studiebelasting", "EC/ECTS/SBU", "lesdagen". De regexes staan in `.claude/scripts/poort0-scan.py`.

## Student-signaal
- **NSE (Nationale Studenten Enquête)** bestaat, maar particuliere opleiders doen er zelden aan mee. Geen betrouwbaar per-aanbieder getal in dit segment.
- Praktisch bruikbaarder: het NVAO-rapport (paneloordeel over feedback) en het toetsprogramma uit de studiegids (wat leveren lerenden in, hoeveel, wie kijkt na). Dat veld maakt structureel een bericht mogelijk; zie de agent-3-instructie.

## Doorlooptijdnorm
Geen sectorbrede gepubliceerde norm in NL. Sommige OER's noemen een nakijktermijn (vaak 10 tot 15 werkdagen), citeer die alleen als hij letterlijk in hun eigen reglement staat. Niet gevonden = niet noemen.

## Vaktermen
De volledige tabel met betekenis en drager staat in `references/onderwijs-vaktermen.md`. De kern:
- **Student** draagt: studeerbaarheid, studielast, toetslast/toetsdruk, herhalingsactiviteiten, leertaken. Nooit ons haakje.
- **Beoordelaar** draagt: beoordelingslast/nakijklast, docentbelasting, tweede beoordelaar/vier-ogen-principe, kalibratie, doorlooptijd van de beoordeling. Wel ons haakje.
- **Panel/organisatie**: borging van de toetskwaliteit (examencommissie, nooit framen als "het rammelt"), robuuste toetsing (compliment, geen pijn).
- Waarom dit bestaat: THIM wees op 13-08-2026 een mail af omdat "studeerbaarheid" als docentlast gelezen was.

## Programmaduur
Poort 0b: minstens één opleiding **langer dan een jaar** (aangescherpt 18-08-2026, was 2 weken). Meet het langste programma. Losse lesdagen verspreid over meer dan een jaar tellen mee; een modulaire route telt als de deelnemer aaneengesloten naar één diploma werkt. Twijfel net onder het jaar = kandidaat, niet afgevallen. Eenheid: maanden, EC/SBU als beschikbaar.

## Prijsmodel
EUR. Toolfee 7.500 per opleiding plus infrastructuurstaffel op studentplaatsen per opleiding: A tot 500 = 10.000, B tot 1.500 = 15.000, C tot 3.000 = 21.500, D tot 6.000 = 33.500, E daarboven = 51.500. Drempel 10.000 jaarwaarde, en onze fee hoogstens 10% van de programma-omzet. Bron: `references/pricing/prijsmodel-nl-opleiding-26-27.md`. Harde waarden in `profiel.json`.

## Titelrangorde
Onderwijstak boven bedrijfsvoeringstak. College van bestuur en bestuurder bovenaan, dan algemeen directeur en eigenaar, dan directeur onderwijs/opleidingen/kwaliteit, dan hoofd onderwijs, lector/decaan, manager onderwijs, opleidingsmanager, teamleider, adviseur, coördinator, docent. Nooit de examencommissie als ingang; opleidingsmanager alleen als er niets hogers is, dan een directeur als tweede kandidaat erbij. Regexes in `profiel.json`.

## Taal en register
nl-NL. Aanhef "Hi [voornaam]", nooit "Hoi" of "Beste". Openen met "ik las" of "je schreef", nooit "wat me opviel". Gewone spreektaal, geen vaktermen die de prospect zelf niet gebruikt. Productnaam als er ruimte is: "Nederlandse onderwijskundige AI-model". Elk bericht eindigt op een open vraag (hoe/wat/wie/hoeveel), nooit "klopt dat?" of "herkenbaar?". Regels in `.claude/skills/linkedin-outreach/SKILL.md`.

## Klantnamen
Toegestaan als bewijs: Radboud Universiteit, Universiteit Leiden, Tilburg University, De Haagse Hogeschool, Hogeschool Rotterdam. Bij particuliere opleiders ook TIO en ICM (ICM sinds 21-08-2026). Kies de instelling waar de prospect zelf studeerde of dichtbij zit, daarom noteert agent 3 opleiding en woonplaats.

## Kanaal
LinkedIn-connectieverzoek (max 300 tekens, met de vraag erin) plus opvolgmail (~110 woorden, één haakje, gesloten CTA) zodra het verzoek geaccepteerd is, plus reminder als reply. Agent 4 levert per persoon `connectieverzoek`, `opvolgmail_onderwerp`, `opvolgmail` en `reminder`. Lemlist-campagne "Shift NL - invite, mail, reminder, call" (`cam_qpkMQ2axpN7wt7HZt`), ga op de ID af, niet op de naam. Geen LinkedIn-verzoek bovenop een lopende cold call.

## Seizoen
Collegejaar september tot juli. Slechte weken: zomervakantie (half juli tot eind augustus), kerst, meivakantie. Goede momenten: september/oktober (nieuwe programma's gestart, nakijkpieken komen eraan), januari (tussenevaluatie), april/mei (voorbereiding volgend jaar, NVAO-visitaties). Particuliere opleiders hebben vaak ook een januari- en septemberinstroom.
