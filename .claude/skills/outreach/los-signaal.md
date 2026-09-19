# Stand 2 — los signaal of losse lijst

Opgenomen uit de vroegere skill `outreach`. Gebruik deze stand wanneer
de aanleiding buiten de SHIFT-pijplijn om komt: een aanmelding, een lijst
opleiders, of een vraag als "wie moet ik mailen bij deze school".

# Targeted Outreach

De orkestrator voor persoonlijke outreach richting het hoger onderwijs. Neemt Dante's input en levert per instelling: de juiste contactpersoon, de juiste insteek, en een mail die volledig klopt en nooit als bulk voelt.

Dit is Dante's werk tot de **Discovery-gate** (`scope-discovery-gate`). Doel van elke mail = een gesprek/SQL. Daarna hand-off naar Jeroen.

## Roept deze skills aan (dat is de kracht)

- **`stakeholder-mapping`** — de juiste persoon en de org-structuur vinden (manager, faculteit, Head of Digital Education).
- **`person-research`** — diep, bronnen-gevalideerd onderzoek op de gekozen contactpersoon. Geen aannames.
- **`cro`** — de sales-logica: welke stage, wat is de taak van de mail, welke pijn/why-now.
- **`schrijven`** — de mail in de juiste stem schrijven, insteek-eerst, niet vaag, geen AI-taal.
- **`marketing-creatives`** (optioneel) — een visual meesturen als dat de mail sterker maakt (bv. een mockup).

## De loop

```
1. SCOPE      welke input? (aanmelders / accounts / schoolnaam / koud), welk segment, en het doel
2. KWALIFICEER  poort 0 per instelling: beoordelen ze zelf werk van lerenden? (1-2 zoekopdrachten)
3. HISTORIE   eerst Gmail EN Close doorzoeken: wat is de echte contacthistorie? (mails, deal, notities)
4. ROUTE      per instelling: wie is de JUISTE persoon om te mailen, wie om mee te connecten?
5. RESEARCH   persoon EN instelling diep onderzoeken -> research-gate afvinken (verplicht)
6. ANGLE      pas NA de gate: 2-4 insteken voorleggen -> Dante kiest (nog geen proza)
7. WRITE      mail (juiste persoon) of LinkedIn-connectieverzoek (connect-waardig), opent concreet
8. FINISH     max 1-2 tweaks + verzendadvies (Gmail, geen tracking, beeld inline)
```

**Discipline: ren niet vooruit.** De grootste terugkerende fout is stappen overslaan onder momentum: naar insteek voordat de research-gate af is, naar de mail voordat Dante de hook koos, schrijven voordat Gmail/Close gecheckt is. Regels:
- **Niet doorlopen naar de volgende stap zonder dat de vorige echt af is.** Stap 5 (ANGLE) pas na de research-gate. Stap 6 (WRITE) pas nadat Dante een insteek koos. Geen proza voor die keuze.
- **Hou vast wat al in het gesprek is vastgesteld.** Gaf Dante eerder een feit (bv. "dit is een webinar-aanmelder", of een gekozen insteek), dan verlies je dat niet halverwege. Herlees kort wat al bepaald is voor je een mail bouwt.
- **Bij twijfel: vraag, schrijf niet.** Eén regel vragen welke kant Dante op wil is beter dan een mail die hij helemaal moet terugdraaien.

## Bij een lange lijst: twee passes, nooit alles diep

Bij meer dan circa 15 organisaties werkt de loop hierboven niet één-voor-één. De research-gate kost 15 tot 30 minuten per account. Splits:

**Pass 1, routing (alle accounts, ondiep, parallel).** Per organisatie alleen: bestaat het nog, poort 0 (wie neemt het examen af, met citaat), wie is de directeur/eigenaar, LinkedIn-URL, mailadres, grove omvang. Levert een tabel plus een stapel afvallers. Dit is geen research, dit is filteren.

**Pass 2, diep (alleen de overlevers).** Dante bepaalt hoeveel er doorgaan. Pas hier draait de volledige research-gate, `person-research` en de mail.

Regels bij volume:
- **Leg de afvallers vast met reden en citaat**, in `GTM/Campaigns/shift/master/dossiers/`. Anders onderzoekt de volgende ronde ze opnieuw.
- **Kijk eerst in `dossiers.md`** of een organisatie al onderzocht is. Doe geen werk over.
- **Rapporteer wat je hebt laten vallen.** Een lijst van 150 waarvan je er 30 deed is prima, zolang je dat zegt. Stilzwijgend afkappen leest als volledige dekking.
- **Vertrouw geen automatische score als kwalificatie.** Trefwoordscores vangen "er wordt getoetst", niet "wij toetsen zelf". Gebruik ze hooguit om de volgorde te bepalen.

## Stap 1: bepaal eerst het segment (dit stuurt alles daarna)

Twee segmenten, met een andere doelpersoon, andere research en een andere mail. Kies expliciet voordat je iets anders doet.

**A. Publiek bekostigd hoger onderwijs** (hogeschool, universiteit, ROC). Grote organisatie, veel lagen, de aanmelder is zelden de koper. Route: docent -> manager -> faculteit -> Head of Digital Education. Zie stap 4A.

**B. Particuliere opleider** (NRTO/CRKBO-lid, bedrijfsopleider, vakopleider, particuliere academie). Meestal 5 tot 50 mensen. Er is geen onderwijskundige laag: de **directeur of eigenaar** is champion, budgethouder en beslisser in één, en kijkt vaak zelf mee na. Route: recht op de directeur. Zie stap 4B.

Twijfel je? De registers beslissen: staat de organisatie in NRTO of CRKBO, dan is het segment B. Voor segment B geldt bovendien `GTM/Campaigns/shift/markets/nl/icp.md` als kwalificatiekader, en staat wat al onderzocht is in `GTM/Campaigns/shift/master/dossiers/`. **Kijk daar eerst, doe geen werk over.**

## Stap 2: poort 0, wie neemt het examen af? (voor segment B, vóór al het andere)

De duurste fout is diep onderzoek doen naar een organisatie die het product niet kan gebruiken. Eén zoekopdracht, `"[naam] examen"` of `"[naam] examenreglement"`, beslist dat in een minuut.

- **Eigen docenten of examinatoren beoordelen het werk** -> door naar stap 3. URL plus letterlijk citaat vastleggen.
- **Een externe instantie examineert** (CBR, CCV, TCVT, Het Oranje Kruis, IBKI, CerTech, een branche-examenbureau, een stichting die het certificaat uitgeeft) -> **stop**. Daar ligt het nakijkbudget, niet hier.
- **Losse trainingsdagen zonder beoordeeld schrijfwerk** -> stop.
- **Niet te vinden** -> "onbekend", niet afwijzen, maar benoem het tegen Dante voor je verder graaft.

Zie `icp.md` voor de volledige uitsluitingslijst (normzetters, uitgevers, praktijkopleidingsbedrijven, eenmanszaken zonder volume). Getest op 2026-07-22: van vijf hoogscorende NRTO-leden vielen er twee hier meteen af, en die score voorspelde dat niet. Vertrouw de score niet, stel de examenvraag.

## Stap 3: Gmail EN Close eerst (nooit overslaan, nooit gokken)

Voor je iets naar buiten stuurt: zoek de **echte contacthistorie** op. Nooit een mail schrijven met een gok als "ik wilde je alvast bereiken" terwijl de werkelijke thread iets anders zegt. Check beide bronnen:

**Gmail (doe dit altijd, niet alleen Close).** Zoek op de **naam én het e-mailadres** van elke persoon. Gmail bevat vaak contact dat Close niet toont: hun **antwoorden**, eerdere heen-en-weer, wat er letterlijk is beloofd of gevraagd. Lees de echte thread (`get_thread`), niet alleen het onderwerp. Heeft de persoon geantwoord? Dan bouw je de mail op dat antwoord, niet op een aanname.
- Zoektips: zoek op achternaam, op het adres (`from:` en `to:`), en op de instelling.

**Close CRM.** 
- Zoek de **lead/instelling** en de **personen**: bestaan ze al als contact?
- Is er een **opportunity/deal**, en in welke stage? Wie is de owner?
- Lees **notities en activiteit**: eerdere mails, calls, meetings, wie waarmee sprak, wat er is beloofd.
- Zit iemand al in een **Lemlist-sequence** of eerdere touch? Dan niet als eerste contact doen (`hot-lead-outreach`-logica: echo geen eerdere touches).

Wat je hier vindt, voedt zowel de mail (hun echte Eduface-interactie, in hun eigen woorden) als de LinkedIn-noot (hoe we ze kennen). Vind je niks, dan is het echt koud, benoem dat. Maar concludeer dat pas **na** Gmail én Close, niet op gevoel.

## Stap 4A: de juiste persoon vinden bij een hogeschool of universiteit

De aanmelder is niet altijd de juiste ontvanger. Routeer per instelling:

- **Aanmelder is al AI / digitaal onderwijs / onderwijstech** (bv. informatiespecialist AI, ICTO-coach, projectleider digitaal toetsen). Dan is dit vaak al een goede ingang (coach/champion-kandidaat). Onderzoek deze persoon.
- **Aanmelder is een gewone docent uit een specifieke faculteit.** Dan map je omhoog met `stakeholder-mapping`:
  1. Wie is de **manager** van die docent (teamleider / opleidingsmanager)?
  2. Onder welke **faculteit / academie** valt die?
  3. Zoek binnen díe faculteit de eigenaar van digitaal/AI-onderwijs: **Head of Digital Education**, ICTO-lead, onderwijstechnoloog, of teamleider onderwijsinnovatie.
  Die faculteits-eigenaar van digitaal onderwijs is meestal het echte doelwit, niet de docent.
- **Bepaal ook de "hoogste in de boom"** (CvB-portefeuille onderwijs/digitalisering, CDO of Chief AI Officer) voor het grotere plaatje en multithreading. Voor de Discovery-gate mik je meestal op de operationele/faculteits-eigenaar; de EB is voor later met Jeroen.
- **Beslis de aanpak per instelling:** de aanmelder zelf mailen, omhoog naar de digitaal-onderwijs-eigenaar, of allebei (multithread). Leg dit kort aan Dante voor.
- **Koude introductie:** geen aanmelder, dan begin je direct bij de digitaal-onderwijs-eigenaar / hoogste in de boom van de genoemde instelling.

Splits elke persoon in een van twee sporen:
- **Mailen** = de juiste, relevante contactpersoon voor Discovery. Krijgt de volledige gepersonaliseerde mail.
- **Connecten** = niet direct de juiste ontvanger, maar wel goed om mee te connecten (bv. een aanmelder-docent die niet het doelwit is). Krijgt een LinkedIn-connectieverzoek, geen mail.

## Stap 4B: de juiste persoon vinden bij een particuliere opleider

Hier is de route kort: **de directeur of eigenaar, direct**. Geen multithreading, geen faculteitslaag, geen zoektocht naar een Head of Digital Education, die bestaat niet. Die ene persoon is champion, budgethouder en EB tegelijk.

Waar je hem of haar vindt, in deze volgorde:
1. **Team- of "over ons"-pagina** van de site. Levert bijna altijd naam plus functie, vaak van het hele docententeam.
2. **Register-vermeldingen**: CPION, SNRO, CRKBO, NRTO, het EVC-register. Die noemen contactpersonen.
3. **KVK** voor de formele bestuurder als de site vaag blijft.
4. **LinkedIn** pas als vierde, niet als eerste. Bij deze doelgroep is het profiel vaak leeg, verouderd of dubbel.

Let op twee dingen die hier structureel spelen:
- **Naamgenoten zijn een reëel risico.** Kleine ondernemers hebben vaak meerdere profielen en gedeelde namen. Verifieer via de eigen praktijk of het bedrijf dat op beide plekken genoemd wordt.
- **De directeur is vaak zelf ook docent of praktijkeigenaar.** Check dat expliciet, want als hij zelf nakijkt is dat de sterkste opening die er is: je praat met iemand die het probleem met de hand heeft.

Bij een organisatie met meerdere merken of vestigingen onder één moeder: mik op de moeder, niet op het merk.

## Stap 5: research (persoon EN instelling) — DIT IS HET ZWAARSTE STUK

Dit is waar de skill staat of valt. Ondiep onderzoek + snel naar insteek = de klassieke fout. **Je mag pas door naar stap 6 (ANGLE) als je de research-gate hieronder kunt afvinken.** Kun je dat niet, dan is het onderzoek nog niet klaar: graaf door of vraag Dante gericht om wat je mist (bv. een LinkedIn-profiel dat jij niet kunt laden). Insteek bedenken vóór dit fundament is verboden.

Twee sporen, beide gevalideerd met bronnen (`person-research`-regels, `claims-need-sources`). Roep `person-research` echt aan per mail-ontvanger; leun niet op titel + aanname.

**Welke gate je gebruikt hangt van het segment af.** Segment A (hogeschool/universiteit) gebruikt de gate hieronder. Segment B (particuliere opleider) gebruikt de gate daaronder: die is anders, want deze organisaties hebben geen lectoren, geen publicaties en geen AI-beleid. De A-gate afvinken bij een particuliere opleider levert vier keer "niet gevonden" en nul inzicht.

### Research-gate segment A: hogeschool en universiteit (moet af vóór insteek)

**Persoon** — per MAIL-ontvanger, niet alleen de aanmelder:
- [ ] **LinkedIn daadwerkelijk gelezen** (profielpagina + recente activiteit/posts). LinkedIn blokkeert vaak automatisch ophalen (HTTP 999). Dat is **geen excuus om over te slaan**: probeer Google/Bing-snippets, cache, andere bronnen, én vraag Dante expliciet of hij het profiel voor je openplakt. Noteer wat je wél en niet hebt kunnen lezen.
- [ ] **Wat vindt deze persoon aantoonbaar belangrijk?** Hun thema's, waar ze zich voor inzetten, wat ze zelf zeggen/schrijven. Niet "wat is hun functie" maar "wat drijft ze". Met bron.
- [ ] **Publicaties / scripties / talks / posts / redes actief geopend en gelezen**, niet op titel geciteerd. De waarde zit in de inhoud, niet in de titel. Repository blokkeert (SPA/403/999/login)? Probeer de REST-API, `curl` met browser-`User-Agent`, cache, HBO-kennisbank, of vraag Dante het te openen, vóór je "niet leesbaar" concludeert. Zie `person-research` regel 2 voor waar je scripties vindt ([studenttheses.uu.nl](https://studenttheses.uu.nl), [hbo-kennisbank.nl](https://www.hbo-kennisbank.nl), uni-repositories, Scholar).
- [ ] **Naamgenoten uitgesloten** (zelfde naam, andere persoon).

**Instelling** — verplichte checks, geen optionele:
- [ ] **AI-strategie / AI-beleid gelezen?** Heeft de instelling een vastgestelde visie op (generatieve) AI in onderwijs/toetsing? Citeer letterlijk als je iets vindt; zeg expliciet "niet gevonden / bestaat mogelijk niet" als je niks vindt. Verzin geen beleid.
- [ ] **Hebben ze al een AI-feedback- of AI-nakijktool?** (concurrentie-check, cruciaal). Zoek FeedbackFruits, Ans, Grasple, Turnitin-AI, Revisely, eigen tools, pilots, aanbestedingen. Dit bepaalt of de mail "eerste kennismaking" of "waarom wij ipv wat je al hebt" is.
- [ ] **Toets-/feedback-landschap:** welke systemen draaien er (LMS, digitaal toetsen, plagiaat), en waar zou een AI-feedbacktool op geschreven werk landen.
- [ ] **Recent, relevant nieuws/project/vacature** dat raakt aan AI/toetsing/feedback.

Vaak zit de sterkste hook in de combinatie: iets van de instelling (hun AI-stand, een tool, een project) dat precies raakt aan wat déze persoon belangrijk vindt. Zonder de gate hierboven kun je die combinatie niet eens zien — vandaar de volgorde.

### Research-gate segment B: particuliere opleider (moet af vóór insteek)

Andere bronnen, andere vragen. Getest op vijf NRTO-leden op 2026-07-22, dit is wat wél oplevert.

**Organisatie:**
- [ ] **Poort 0 dubbel bevestigd.** Stap 2 mag afwijzen op één bron, maar een JA vraagt een tweede: de procedure-, reglement- of studiegidspagina, niet alleen de examenpagina. Bureau STERK leek op de examenpagina extern geëxamineerd en bleek op de procedurepagina zelf te beoordelen met eigen assessoren.
- [ ] **Welke accreditatie hangt aan hun beoordeling, en willen ze omhoog?** CRKBO, CPION, SNRO, NRTO, NLQF, NVAO, branchestandaarden. Dit is de geldregel van dit segment: erkenning valt of staat bij aantoonbare, consistente beoordeling. Een opleider die naar NLQF of NVAO wil, of net een standaard verloor, heeft een gefinancierd probleem.
- [ ] **Wat wordt er precies geschreven en nagekeken, door hoeveel mensen?** Scriptie, casusverslag, portfolio, praktijkverslag, ingestuurde moduleopdrachten. Citeer uit hun eigen studiegids of procedurebeschrijving. Dit bepaalt of er een product is.
- [ ] **Hoe groot zijn ze?** Teampagina tellen, aantal opleidingen, diploma-uitreikingen, vestigingen, prijs per traject. Ruwe schatting is genoeg, maar zonder dit weet je de dealgrootte niet.
- [ ] **Draait er al iets?** LMS of portfolio-omgeving (Moodle, aNewSpring, Remindo, TOA, eigen bouw) en of er een AI-nakijktool in beeld is. Check inlogpagina's, privacyverklaring, cookiebanner en bron-HTML, niet alleen de marketingpagina's.

**Persoon (de directeur/eigenaar):**
- [ ] **Naam en rol bevestigd op hun eigen site of in een register.** Niet op LinkedIn alleen.
- [ ] **Kijkt deze persoon zelf na of geeft die zelf les?** Zo ja, dat is je opening.
- [ ] **Eén uitspraak van deze persoon zelf gevonden, met bron.** Zoek gericht op `"[naam]" interview`, `"[organisatie]" klantverhaal`, `"[organisatie]" subsidie`, vakbladen, podcasts, en nieuwsberichten van hun brancheorganisatie. **Hier zit het goud, niet op hun homepage.** De sterkste hook van de testronde kwam uit een klantverhaal bij hun subsidiebureau.
- [ ] **Naamgenoten uitgesloten.**

**Wat je hier NIET hoeft te doen:** publicaties, scripties en lectorale redes zoeken (bestaan niet), een AI-strategiedocument zoeken (bestaat niet), of de gate laten stuklopen op LinkedIn. LinkedIn geeft in dit segment structureel HTTP 999 of een leeg profiel. Noteer dat en ga door, mits je elders wel een uitspraak vond.

### Als research geblokkeerd is
Doe niet alsof. Benoem hard wat je niet kon verifiëren (bv. "LinkedIn zat dicht, ik heb haar posts niet gezien"), en kies: (a) graaf verder om de blokkade heen, of (b) leg Dante gericht voor wat je mist en laat hem het aanvullen. Ga **niet** door naar insteek met een gat op de gate.

## De mail: nooit bulk, altijd concreet

**Lees eerst `gold-standard-mail.md` in deze map.** Dat is de lat: één anker diep uitgewerkt, echte reactie op hun werk (geen personaliseer-dan-pitch), Eduface subtiel ingeweven via hún idee, social proof natuurlijk verweven, lopende zinnen, elke zin door de lezer-test. Schrijf daar naartoe.

Niet-onderhandelbaar:
- **Is de persoon een webinar-aanmelder? Dan opent de mail 100% met die aanmelding.** Dat is de reden van contact en de warme aanleiding ("ik mail je omdat je je hebt aangemeld voor ons webinar met De Haagse Hogeschool"). Vergeet dit nooit en schuif het niet naar paragraaf 2. Een andere hook (scriptie, project) mag daarna volgen, niet ervoor.
- **Anders: open met een concreet "ik las ..." of "ik zag ..."** met een specifiek ding (een rede, een project, een pagina, een uitspraak). Nooit vaag ("ik zag dat jullie met AI bezig zijn" is te zwak).
- **Kort. Snijd elke overbodige zin eruit.** Context mag, maar focus op zo min mogelijk. Geen lege verbindingszinnen ("dat sluit precies aan op ..."); zeg het concreet. Zie `schrijven`.
- **Herhaal geen info die de persoon al in een eerdere mail kreeg** (bv. dat het webinar is uitgesteld, of "je hoort van ons als de datum staat"). Uit de Gmail-historie weet je wat ze al hebben gelezen. Verwijs kort naar de aanleiding, leg niks opnieuw uit.
- **Elke mail moet volledig kloppen** en aantoonbaar over déze persoon/instelling gaan. Als het ook naar 100 anderen had gekund, is het niet goed genoeg.
- **Eén duidelijke CTA** naar een gesprek (Discovery). Zacht en concreet.
- Stem en anti-vaagheid via `schrijven`. Sales-logica via `cro`.

**Extra voor segment B (particuliere opleider):**
- **Schrijf naar een ondernemer, niet naar een onderwijskundige.** Deze persoon runt de tent, kijkt vaak zelf na en betaalt zelf. Geen onderwijskundig jargon, geen visiestukken.
- **Hang de mail aan hun erkenning of aan wat hun beoordeling bedreigt**, niet aan "AI in het onderwijs". Een NLQF-ambitie, een ingetrokken branchestandaard, een audit: dat is de geldregel.
- **Nooit pitchen als vervanging van de beoordelaar.** Bij mensen die zelf lesgeven en nakijken is dat een directe aanval op hun vak. Het frame is: dezelfde beoordelaar, meer tijd voor het gesprek, consistentere onderbouwing.
- **Dealgrootte klopt met de omvang.** €10K tot €40K bij smaak 1. Zie `small-deals-still-count`: niet afwijzen op dealwaarde.

## Het tweede spoor: LinkedIn connectieverzoek

Voor de connect-mensen (niet de mail-ontvangers): een kort, persoonlijk connectieverzoek, geen mail en geen pitch.
- **Verankerd aan hoe Dante ze kent of hun Eduface-interactie** (uit Close of de aanmeldlijst): "je meldde je aan voor ons webinar met De Haagse Hogeschool", "we spraken bij [event]".
- **Max ~300 tekens**, licht, warm, met een echte reden (zelfde vakgebied, elkaars werk volgen). Geen "laten we bellen".
- Stem en regels: zie het type **LinkedIn connectieverzoek** in `schrijven`.

## Verzenden (deliverability)

- Handmatig vanuit Gmail/Workspace, **niet** via Lemlist/Close voor 1-op-1 persoonlijke mails (DKIM-alignment faalt anders, eduface.me staat op DMARC `quarantine`).
- Geen open/click-tracking, geen linktrackers.
- Beeld inline in de body, niet als losse bijlage.
- Stuur bij een lijst niet meerdere bijna-identieke mails vlak achter elkaar; los en gespreid.

## Done

- Segment bepaald (A hogeschool/universiteit of B particuliere opleider) voordat er geroute of onderzocht werd.
- Bij segment B: **poort 0 gesteld en met citaat vastgelegd** voordat er diep onderzoek in ging. Afvallers met reden weggeschreven in `dossiers.md`.
- Close CRM doorzocht: bekende deal/contacten/notities meegenomen, niemand koud benaderd die al in een deal zit.
- Per instelling: de juiste contactpersoon bepaald en waarom, plus wie mailen vs. wie connecten.
- **De juiste research-gate afgevinkt** vóór er een insteek kwam (A of B, niet de verkeerde). Blokkades (bv. LinkedIn dicht) benoemd, niet weggemoffeld.
- Bij een lange lijst: in twee passes gewerkt en gerapporteerd wat er is afgevallen en wat er niet is aangeraakt.
- Persoon + instelling onderzocht, hook is concreet en gevalideerd met bron.
- Insteek door Dante gekozen voor er proza kwam.
- Mail klopt volledig, opent met een specifiek "ik las ...", voelt niet als bulk, één CTA.
- Connect-mensen kregen een kort, persoonlijk LinkedIn-verzoek (geen pitch).
