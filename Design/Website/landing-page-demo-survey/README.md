# Demo-landingspagina met kwalificatievragen

Gestart 11-09-2026. Eén doel: een geboekte demo. Eén conversiepunt: het `#demo`-blok (drie knopvragen, dan de Calendly-kalender inline).

- `index.html` + `styles.css`: de interactieve preview. Openen in Chrome (`open -a "Google Chrome" index.html`).
- `onderzoek.md`: het onderzoek met bronnen, plus de aanbevolen structuur en het surveyontwerp.
- `brand_assets/`: kopie van `Design/Website/website-building/brand_assets/` (logo's, schoollogo's, LMS-logo's).

## Opbouw van de pagina (en waarom)

1. **Hero**: één belofte, één groene CTA (de enige groene knop op de pagina), productpaneel dat het mechanisme laat zien (AI stelt voor, docent keurt goed), logobalk.
2. **Sound familiar**: drie kaarten in docententaal.
3. **How it works**: drie stappen, nadruk op stap 3 (jij beslist), met het rubric-paneel.
4. **Proof**: de Bath Spa-cijfers als sectorvalidatie (435 / ~6 pt / ~2 pt), met de uitleg dat het afstand is, geen overeenstemmingspercentage.
5. **Trust**: AI Act, GDPR, LMS. Het blok dat ho-inkopers zoeken en de meeste vendors overslaan.
6. **Demo**: drie vragen → kalender, of zachte landing.
7. **FAQ**: wat er in de demo gebeurt, pilot, LMS, rubric, accuraatheid, data.
8. **Herhaalde CTA** (navy, scrollt naar het demoblok) en footer.

## De survey

| Stap | Vraag | Opties | Routing |
|---|---|---|---|
| 1 | What best describes you? | Lecturer / Head of assessment / Dean / Learning technologist / Student | Student → zachte landing (video + link doorsturen) |
| 2 | Where do you work? | UK university / UK college / Dutch hogeschool-universiteit / Other institution / Not at an institution | Not at an institution → zachte landing (mail) |
| 3 | How many assignments per year in your area? | <500 / 500-2k / 2k-10k / 10k+ / Not sure | Blokkeert nooit, reist mee als tag |
| 4 | Pick a time | Calendly inline, antwoorden als `utm_content` op de boeking | |

Regels uit het onderzoek die hierin zitten: knoppen in plaats van dropdowns, één vraag per stap, auto-doorgaan, e-mail pas in de kalender, kalender direct na de laatste vraag, geen dood spoor voor afgewezen bezoekers, geen budgetvraag.

## Naar Framer

De hele pagina behalve de survey is native Framer: stacks, grids, tekststijlen, kleurstijlen. De CSS is al zo geschreven (gap op de parent, geen margins op children, geen vaste hoogtes, minmax-grids).

De survey wordt **één codecomponent** (React + framer-motion, alleen imports uit react/framer/framer-motion):

- State: `{ role, inst, volume, step }`. Elke vraag is een variant, de knoppen zijn `<button>`s met een `on`-staat.
- Overgang tussen stappen: `motion.div` met opacity 0→1 en y 10→0, spring stiffness 165 damping 25 (preset SnelleSpring).
- Stap 4 rendert de Calendly inline embed als iframe met `utm_content=role | inst | volume`.
- Routing zit in het component, niet in Calendly. Dat scheelt de betaalde routing forms.
- Property controls: Calendly-URL, de labels van de opties, de teksten van de zachte landingen.

Wat Framer niet kan en wat er nog bij moet voordat dit live gaat:

- **Close-writeback.** Framer heeft geen server-side logica. De antwoorden komen nu alleen als UTM op de Calendly-boeking. Wil je ze als custom fields op de lead in Close, dan loopt dat via een webhook (Calendly → Zapier/Make → Close) of via de Calendly-integratie in Close.
- **Tracking-events.** In Framer via de ingebouwde analytics of GA: `demo_cta_click`, `survey_q1`, `survey_q2`, `survey_q3`, `survey_calendar_shown`, `survey_soft_landing`, `booking_made` (Calendly event via postMessage).
- **Video voor studenten.** De zachte landing verwijst naar een drie-minuten-walkthrough die er nog niet is. Tot die tijd scrollt de knop naar "How it works".

## Open punten (bevestigen voor livegang)

- Compliance-teksten (AI Act, GDPR, DPA) zijn de teksten van de huidige live site. Nalopen met Jeroen of ze nog kloppen.
- "Review time two to three minutes per submission" komt uit de Bath Spa-pilotnotities. Bevestigen voordat het live gaat.
- Geen testimonials op de pagina: er zijn geen vrijgegeven citaten. Drie echte quotes met toestemming en ze passen erin.
- Footer-links naar privacy en voorwaarden zijn placeholders.
- De H1 is de hero uit `Design/Website/website-building` (augustus 2026). Bij een ad-campagne: H1 exact laten matchen met de advertentietekst.

## Besluiten en bronnen (bijgewerkt 11-09-2026, middag)

- Proces: stap voor stap. Onderzoek (goedgekeurd) → secties → wireframe → proef → uitrol. De eerder gebouwde `index.html` is een scratch-draft, geen oplevering. De quiz/survey is geparkeerd.
- **Dragend woord: consistentie** (Dante, 11-09). Niet navolgbaarheid, niet tijd.
- Pijnbron: `GTM/ICP/pijn-oplossing/HANDOFF-landingspagina.md` (50 goedgekeurde uitspraken uit Close). Productclaims uitsluitend uit `Platform/product.md`.
- Analytics huidige pagina `/ai-for-grading-papers` (28 aug tot 11 sep): 59 bezoekers, 27% klikt Book a demo, 0 boekingen, 67% bounce, 88% desktop, slechts 9 uit GB.
- Design-inspiratie voor later: https://habitline-wbs.framer.website/ (Dante: "fantastische website"). Patroon: grote typografie in de hero, feature-kaarten met mockups, metrics-blok, FAQ, centrale eind-CTA.

## Hero-besluit (11-09-2026, na hero-onderzoek)

Onderzoek: zie de aanvulling onderaan `onderzoek.md`.

- **Eén primaire knop** ("Book a demo") plus een **tekstlink** ("See how it works", scrollt naar beneden), in plaats van twee gelijkwaardige knoppen. Geaggregeerde data: 1 CTA 13,5% vs 2 CTA's 11,9% [vendor, correlationeel]. De tekstlink houdt de attention ratio dicht bij 1 en geeft de meerderheid die niet boekt toch een pad.
- **Bewijsregel in de hero**, direct onder de CTA, in plaats van een losse logostrook eronder. NN/g 2018: 57% van de kijktijd zit boven de vouw. Sectie 2 (logostrook) is daarmee vervallen.
- **Gestapeld en gecentreerd** blijft. Er bestaat geen publieke test die gecentreerd met split vergelijkt; de keuze is dus smaak, en Dante koos gestapeld naar het Habitline-voorbeeld.
- **Productbeelden onder de vouw**: drie vlakken (submission 1, submission 140 groot, batch) die doorlopen. "Afsnijden nodigt uit tot scrollen" is een heuristiek zonder bewijs, maar kost niets.
- **Geen video, geen stockfoto.** Video-cijfers zijn vendor-ruis; stockfoto's worden aantoonbaar genegeerd (Nielsen eye-tracking).

Sterkste hefboom volgens het onderzoek zit niet in de layout maar in de **kop**: message match met de advertentiegroep, onder 12 woorden, spreektaal (Unbounce 2024: 11,1% vs 5,3%). Dat is copy-werk voor de volgende stap.

Testen heeft pas zin bij meer volume. Bij ~10 klikken per dag duurt een test op 15 tot 20% verschil maanden. Voorlopig meten we kliks op de CTA, niet boekingen.

## Sectie 5, producten (uitgewerkt 11-09-2026)

Onderbouwing: `research/product-tonen-en-beta.md`.

- **Twee live producten, elk één uitvergroot UI-fragment**, niet een heel dashboard. NN/g: alleen beelden met taakrelevante informatie worden bekeken; een volle UI bij koud verkeer wekt twijfel.
- **Paper Grader = het feedbackmoment.** Passage in de inzending gemarkeerd, commentaarkaart met criterium ernaast, Approve / Edit / Discard, daaronder de score per criterium met één "needs you", en het voorgestelde cijfer met "pending approval".
- **Exam Grader = de triage.** 142 antwoorden, 122 gescoord, 20 gemarkeerd, een raster waarin de gemarkeerde eruit springen, en één gemarkeerd antwoord opengeklapt met het correctiemodel ernaast, "uncertain", punten, Approve / Adjust, en "to gradebook".
- De twee fragmenten overlappen bewust niet: het ene zoomt in op één document, het andere op een hele batch. De hero toont de vergelijking (inzending 1 naast 140), sectie 4 toont dezelfde stappen klein. Drie zoomniveaus, één verhaal.
- **Bijschrift onder elk fragment** ("what you are looking at"), want een informatief beeld heeft context nodig en het balanceert de split.
- **De twee beta's: twee kleine cellen, badge "Beta", één zin, geen beeld, geen datum.** Ze staan er zodat een opleiding met veel mondeling niet afhaakt, niet om te verkopen. Reden om ze klein te houden: het enige gevonden ho-geval van een AI-gradingfunctie die niet volwassen aanvoelde liep stuk (Montclair State, Canvas, juli 2026), en een inkoper leest "beta" als "nog geen conformiteitsbeoordeling" onder de AI Act.
- Nog te testen, niet nu: een productvideo van 30 tot 60 seconden of een interactieve demo. Alle conversiecijfers daarover komen van partijen die dat formaat verkopen.

## Eén wireframe, forks samengevoegd (11-09-2026, eind)

Er liepen drie forks plus de hoofdsessie naast elkaar. Ze hebben elkaar niet overschreven, elk pakte een ander stuk. Samengevoegd in `wireframe.html`:

| Bron | Wat er in zit |
|---|---|
| hoofdsessie | hero (één CTA plus tekstlink, bewijsregel in de hero), secties 3 en 6 tot 11 |
| sessie in hoofdmap | sectie 4 herzien naar één geannoteerd beoordeelscherm (v6) |
| fork `great-brahmagupta` | sectie 5 volledig uitgewerkt, plus `research/product-tonen-en-beta.md` |
| fork `beautiful-keller` | `wireframe-proof-varianten.html` (drie varianten A/B/C voor het bewijsblok) plus `research/proof.md` |
| fork `sweet-mendeleev` | niets, lege fork |

**`wireframe.html` is vanaf nu het enige levende bestand.** `wireframe-v1.html` en `wireframe-v3.html` zijn historie. `wireframe-proof-varianten.html` is een keuzedocument: Dante kiest A, B of C, daarna gaat die variant in sectie 6 van `wireframe.html` en kan het losse bestand weg.

**Werkafspraak om dit te voorkomen:** één sessie schrijft in `wireframe.html`. Wil je parallel aan een sectie werken, doe dat in een eigen bestand `wireframe-sectie-<n>.html` en voeg het daarna samen. Anders lopen forks op hetzelfde bestand uit elkaar.

## Boekflow: besluit (11-09-2026)

**Keuze: de agenda staat inline op de landingspagina zelf, onderaan, als sectie 11. Geen popup, en geen aparte `/book-a-demo` zonder inhoud. Alle CTA's op de pagina zijn ankerlinks die daarheen scrollen.**

### Waarom niet de popup
Formulieren die direct zichtbaar zijn halen 45,53% completion tegen 25,96% in een modal (enkele duizenden sites, geen zuivere A/B-test). Een popup verliest bovendien de context van de pagina precies op het moment dat iemand nog twijfelt.

### Waarom niet een kale `/book-a-demo`
Dit is de belangrijkste afwijking van de voorlopige voorkeur. De analytics zeggen dat onze content al werkt: 27% van de bezoekers klikt op "Book a demo". Dat is hoog voor koud zoekverkeer. Wat faalt is de stap daarna, niet de overtuiging ervoor. Een pagina die alleen een agenda toont gooit dus het enige weg dat aantoonbaar werkt. Iemand die "essay grader" googelt kent ons niet en heeft eerst een reden nodig om dertig minuten te geven.

Dat gezegd: de inline-winst blijft overeind, want de agenda staat gewoon op de pagina en is niet verstopt achter een klik die een overlay opent. Het modal-nadeel gaat over onderbreking en contextverlies, niet over moeten scrollen.

### Waarom dit de Chili Piper-bevinding respecteert
Bijna vier miljoen B2B-submissions: wie direct na het formulier kan boeken, boekt in 66,7% van de gevallen, tegen ongeveer 30% zonder directe scheduling. In onze flow is er geen formulier dat eerst verstuurd wordt. Je kiest een tijd, vult drie velden plus één optioneel, en het staat. Niemand wacht op contact, niemand vult twee keer hetzelfde in.

### De flow in sectie 11
- **Links:** korte kop, één regel, het citaat van Els Stapersma, drie trust-cues (docent tekent af, EU-data, in je eigen LMS).
- **Rechts:** de Calendly inline embed. Stap 1 is de agenda met tijden, stap 2 zijn de velden: naam, zakelijk e-mailadres, onderwijsinstelling, functie of use-case (optioneel).
- **Mobiel:** de twee kolommen stapelen, korte introductie boven, agenda direct daaronder.
- **Daaronder:** het zelf-inschrijven-blok, zie hieronder.

### Techniek en meting
- **Calendly Standard**, $10 per gebruiker per maand bij jaarlijkse betaling. Teams ($16) is niet nodig zolang we geen routing naar meerdere mensen doen en geen uitgebreid kwalificatieformulier vooraf.
- **Close CRM** via de native Calendly-integratie: boeking maakt een contact aan, formuliervelden en UTM-data gaan mee.
- **Google Ads:** `calendly.event_scheduled` naar GTM, GA4 en Ads. Alleen `demo_booked` is de primaire conversie. CTA-klik en tijdselectie zijn secundaire funnel-events, niet om op te bieden.
- **Default valt af.** Goedkoopste pakket $15.000 per jaar met enrichment, routing en GTM-workflows die we niet gebruiken.

### Wat dit betekent voor de kwalificatievragen
De vier velden staan ná de tijdselectie en zijn tegelijk onze kwalificatie. Daarmee is een aparte survey vóór de agenda voorlopig van tafel: die zou een tweede invulmoment toevoegen en dat is precies wat het onderzoek afraadt. Blijkt uit de eerste boekingen dat er te veel studenten doorheen komen, dan is de goedkoopste ingreep een verplicht keuzeveld "rol" met een routing-regel, niet een aparte quiz.

## Zelf inschrijven (11-09-2026)

Direct onder het boekblok, als aparte strook: "Not ready for a call? Create a free account." met een secundaire knop naar `app.eduface.me/signup`.

- **Waarom hier en nergens anders.** Twee gelijkwaardige CTA's kosten conversie (1 CTA 13,5%, 2 CTA's 11,9%, vendor-data, correlationeel). Daarom niet in de hero en niet in de nav. Onder het boekblok is het een de-escalatie op het moment dat iemand afhaakt op "dertig minuten met een verkoper", niet een concurrent van de hoofdknop.
- **Welk gat dit dicht.** De docent die op "essay grader" zoekt is vaak niet de koper. Die had tot nu toe maar één uitgang. Nu kan hij het zelf proberen en intern doorsturen.

## Bewijs verwerkt in de wireframe (11-09-2026)

Het volledige plan uit `research/proof.md` zit nu in `wireframe.html`, op drie plekken:

- **A, in de hero:** één strook onder de CTA met 94% en 79% plus vier dunne logo's zonder kop. Het sterkste getal staat nu in het eerste scherm in plaats van op positie 6.
- **B, sectie 6:** het bewijsblok op twee benen. Been 1 is de meting (94% naar 98% na afstemmen, 435 opdrachten, 13 markers, 6 vakken, Bath Spa juni 2026). Been 2 is de case (79% van de studenten positief of neutraal, ronde 2 beter dan ronde 1 na het verfijnen van de rubric, BDK Hogeschool Rotterdam). Twee bronnen die hetzelfde mechanisme aanwijzen.
- **C, sectie 11:** het citaat van Els Stapersma naast de boekflow, niet in een rij van drie.

Bijbehorende regels die nu gelden: geen "95% accuraat", geen "30.000 studenten", Bath Spa alleen als pilot en nooit als klant of met citaat, en de definitie van accuraatheid hoort in de FAQ en niet in het bewijsblok.

## CTA-verdeling (11-09-2026)

Zeven knoppen, grootste gat 2321 pixels (was 5080). Nav, hero, na "hoe het werkt", na de producten, na het bewijs, na trust, en het boekblok zelf. De logo-rij in sectie 4 is weg: die stond dubbel met de hero-strook.

## Inkorting doorgevoerd (11-09-2026)

Van 9355 naar 7959 pixels, van 10,4 naar 8,8 schermen. Tien secties werden er acht.

| Ingreep | Opbrengst |
|---|---|
| Sectiepadding 120 naar 88 pixels | 576 px |
| Sectie "Opbrengst" geschrapt | 793 px |
| LMS en Trust samengevoegd tot "Fit & trust" | 337 px |
| Bewijs vóór de producten gezet | 0 px, wel het grootste effect |

**Waarom "Opbrengst" eruit kon.** Drie van de vier kaarten herhaalden iets: diepere feedback stond al bij de producten, één standaard over het team stond al bij het bewijs, en minuten per inzending was nog onbevestigd. Alleen doorlooptijd was nieuw. Die staat nu als één regel onder de twee benen van het bewijsblok, onder het kopje "wat dat oplevert".

**Waarom LMS en Trust samen kunnen.** Beide beantwoorden dezelfde vraag van de lezer: kunnen we dit kopen en draaien. Links de LMS-logo's met de stroom van inleveren tot gradebook, rechts AI Act, GDPR en de handtekening van de docent.

**De verplaatsing is de belangrijkste wijziging.** Het bewijsblok stond op 5196 pixels, scherm 5,8. Het staat nu op 2739, scherm 3,0. NN/g meet 81% van de kijktijd in de eerste drie schermen, dus het sterkste bewijs zit nu binnen dat bereik. De producten, de langste sectie, komen erna, bij lezers die al overtuigd zijn dat het werkt.

**Nieuwe volgorde:** hero, pijn, hoe het werkt, bewijs, producten, fit & trust, FAQ, boeken.

**CTA's:** acht stuks, grootste gat 2225 pixels. Het boekblok staat op scherm 7,6, was 9,0.

Wat ik bewust heb laten staan: het vouwen van "hoe het werkt" in de eerste productrij. Dat had nog eens 900 pixels opgeleverd, maar haalt inhoud weg die overtuigt in plaats van herhaling.

## Poort 2, proef: het bewijsblok (11-09-2026)

Bestand: `proef-bewijsblok.html`. Eén sectie volledig af, als patroon voor de rest.

**Wat vastligt als dit akkoord is**
- Type: League Spartan voor de kop (44px, weight 600), Inter voor de rest. Cijfers in League Spartan 72px met -0,04em tracking. Drie tekstgroottes per blok, niet meer.
- Kleur: navy als grond, `ink-900` voor de kaarten, wit voor de cijfers, wit op 62% voor bijschrift en bron. Groen alleen op de eyebrow.
- Ruimte: 96px sectiepadding, 56px tussen de blokken binnen de sectie, 24px tussen de kaarten, 36px padding in een kaart. Allemaal 8pt-familie.
- Radius: 20px op de kaarten, vol rond op de knop.
- Knop op donker: wit vlak met navy tekst, niet groen. Groen is op deze pagina alleen de hero-CTA.

**Vier dingen die uit het design system volgen en die ik expliciet heb toegepast**
1. **Geen groen op een gunstig getal.** 94, 98 en 79 zijn wit. Kleur codeert een toestand, geen mening over de uitkomst. Groen staat alleen op de eyebrow, met een bolletje ernaast zodat het ook zonder kleur werkt.
2. **Contrast.** Eerste versie had twee tekstkleuren op 4,1 en 4,3 tegen een norm van 4,5. Opgelost door de zelfverzonnen waarde van 45% te schrappen. Core kent alleen 62%. Nadruk komt nu van gewicht, niet van minder contrast, precies zoals `regels.md` voorschrijft.
3. **Gelijke kaarthoogte zonder vaste hoogte.** De bronregel wordt met `margin-top: auto` naar beneden geduwd. Framer-proof, want daar bestaan geen vaste hoogtes.
4. **Mobiel.** De twee cijfers stapelen en de pijl draait mee naar beneden, zodat het verband van 94 naar 98 blijft kloppen.

**Copy-besluiten**
- "94% accuracy" mag, mét de dragers erbij, volgens `Platform/product.md`. De definitie van accuraatheid hoort in de FAQ, niet hier.
- Bath Spa staat er als pilot ("Piloted at Bath Spa University"), niet als klant, en zonder citaat. Dat is feitelijk juist en houdt het risico klein.
- Geen "95% accuraat", geen "30.000 studenten", geen balk bij de 79%.
- De regel over doorlooptijd, overgebleven uit de geschrapte sectie Opbrengst, staat onderaan onder "what that gives you back".

**Nog open:** de eyebrow staat op de reflexen-lijst in `compositie.md` (kapitalen-labeltjes boven koppen). Hij staat er omdat het design system zelf een eyebrow-patroon kent (`eyebrow-preview.html`). Wil je hem weg, dan haal ik hem overal weg, niet alleen hier.

## Proef v2 na Dante's feedback (11-09-2026)

Verwerkt:
- **Logo's in plaats van namen.** Hogeschool Rotterdam staat er als logo, wit uitgesneden op de donkere kaart. Bath Spa ontbreekt nog, zie hieronder.
- **Beeld in de kaart.** Elke kaart krijgt een beeldstrook van 16:6 bovenin met het logo dat eroverheen hangt. Nog te vullen met campusfoto's.
- **Nummerbadges weg.** "1" en "2" op twee losse kaarten lazen als stappen, alsof kaart 2 het vervolg was van kaart 1. Het logo identificeert de bron nu, en dat is meteen sterker bewijs.
- **Groen mag weer.** Staat op de 98%, op de sprong van ronde 1 naar 2, en op de knop. De regel dat kleur nooit de enige drager mag zijn laten we los, deze pagina hoeft niet toegankelijk te zijn.
- **Eyebrow zonder bolletje.** Nu een pill met een staafdiagram-icoon. Het losse bolletje las als AI-sjabloon.
- **Minder tekst.** Kop is vier woorden. De dragers zijn chips geworden, dus scanbaar in plaats van een zin. Het blok "what that gives you back" is geschrapt.
- **"Accurate", niet "correct".**
- **Methode achter een knop** ("How we measured this") in plaats van in een alinea. Dat is ook wat een klant zelf vroeg, zie `research/proof.md`.

**Nog aan te leveren voor dit blok af is**
- Logo van Bath Spa University.
- Twee campusfoto's in 16:6. In de repo zit geen bruikbaar beeld: de enige foto's zijn portretten en twee stockfoto's van een klaslokaal. Stockbeeld wordt aantoonbaar genegeerd (Nielsen eye-tracking) en staat op de reflexen-lijst, dus dat gebruiken we niet.

**Volgorde van werken, besluit:** aankleding en copy tegelijk, met de vormgeving leidend. De container bepaalt hoeveel woorden erin passen. Schrijf je eerst en ontwerp je daarna, dan wordt de copy te lang voor het vak. Ontwerp je met blindtekst en schrijf je daarna, dan breekt de layout. Daarom eerst het vak vaststellen, dan de copy daarop schrijven. Zo is deze proef gemaakt.

## Proef v3: één boodschap, accuraatheid (11-09-2026)

Dante: "Met deze sectie zouden we willen zeggen dat ons model accuraat is." Dat is nu de enige boodschap.

- **Rotterdam-kaart weg.** Die 79% ging over tevredenheid van studenten, niet over accuraatheid, en er zat geen aantal opdrachten of beoordelaars onder. Twee verschillende beweringen in één blok maakten de boodschap zwak.
- **Rotterdam blijft als logo** in de partnerregel, samen met Den Haag, Tilburg en Radboud, zonder cijfer. Herkenningswerk, geen bewijswerk.
- **Bath Spa draagt het blok**: logo als crest op de campusfoto, 94% en 98%, met de dragers als chips.
- **Lopende koppen.** Geen "tekst punt tekst punt" meer. De subkop zet het onderscheid neer waar concurrenten op vallen: gemeten op werk dat docenten zelf al hadden nagekeken, niet op een demoset.
- **Groene gloed weg**, was afleidend. Het stippenraster blijft.
- **"How we measured this" weg.**
- De regel van maximaal vier woorden in de kop is vervallen.

Logo van Bath Spa staat in `Design/Merk/logo-van-scholen/bath-spa.svg`. Er moest een viewBox in, anders schaalde hij niet mee.

**Nog nodig:** de campusfoto van Bath Spa. Die staat wel in het gesprek maar niet op schijf. Opslaan als `Design/Merk/logo-van-scholen/bath-spa-campus.jpg` en ik zet hem erin.

## Proef v4 (11-09-2026)

- **"Whisker" weg.** Kop is nu "An AI model that marks like your own team", met het sleutelwoord in groen. Dat is ook precies wat 94% betekent, hoe dicht ons voorstel bij het cijfer van de docent ligt.
- **Geen herhaling meer.** De subkop noemde eerst dezelfde aantallen als de dragers eronder. Hij doet nu iets anders: gemeten op werk dat markers zelf al hadden nagekeken, niet op een demoset. Dat is het onderscheid waar concurrenten op vallen.
- **Dragers als icoontegels.** 435, 13 en 6 met een gekleurd icoon, in plaats van grijze chips met woorden. Kleuren uit de bestaande set van de site: sky, violet, amber.
- **Herkomst op de foto.** Logo plus "Bath Spa University, Pilot June 2026" linksonder op het beeld. Dat koppelt de claim aan de plek, en het scheelt een vierde tegel die niet hetzelfde soort ding was als de andere drie.
- **Campusfoto erin**, verkleind naar 1800px en gecomprimeerd. Navy sluier eroverheen zodat het beeld bij het merk hoort.
- **Logo-rij weg**, die staat in de hero.

Bestanden: `Design/Merk/logo-van-scholen/bath-spa.svg` (viewBox toegevoegd) en `bath-spa-campus.jpg`.

## Proef v5: rust in het paneel (11-09-2026)

Dante vond de twee percentages en de feiten samen in één paneel te druk. De feiten staan nu **onder de kaart**, op de sectie-achtergrond, en zijn kleiner dan de percentages.

- Icoon van 40 naar 34 pixels, getal van 26 naar 20 pixels. Ze zijn ondersteuning, geen claim.
- Op een rij met dunne scheidingslijntjes ertussen, geen grid van tegels meer.
- Het cijferpaneel heeft nu alleen de twee percentages, met meer lucht eromheen.

Daarmee heeft de sectie drie leesniveaus in plaats van twee: de kop, dan de twee percentages, dan de onderbouwing. Dat is precies de hiërarchie die compositie.md vraagt, één dominant object per leesmoment.

## Proef v6: pill weg, één schaal (11-09-2026)

Twee terechte punten van Dante, allebei uit de reflexen-lijst in `core/compositie.md`:

1. **De pill "ACCURACY" was een badge om gewone metadata**, plus een kapitalen-labeltje boven een kop. Nu een gewoon sectielabel: icoon plus het woord in normale schrijfwijze, geen vlak.
2. **94% en 98% stonden als twee losse metric-boxjes**, terwijl het één verband is: een verandering over een stap. Nu één schaal met de sprong erin. De as is afgesneden op 90 om het verschil zichtbaar te maken, dus beide uiteinden staan er expliciet bij. Het rechteruiteinde heeft betekenis: 100% is het cijfer dat het team zelf gaf.

### Botsing met een andere sessie, 19:06

Tijdens dit werk heeft een andere sessie `proef-bewijsblok.html` overschreven met een eigen versie. Bewaard als `proef-bewijsblok-andere-sessie.html`.

Die versie loste dezelfde twee punten op, en met een goede vondst: twee balken op één as met een betekenisvol nulpunt ("0, de mark die je team gaf"). Maar hij draaide drie besluiten van Dante terug:
- terug naar 6 en 2 punten in plaats van 94% en 98%
- "How we measured it" weer erin
- campusfoto en Bath Spa-logo eruit

Ik heb Dante's besluiten teruggezet en het goede idee overgenomen: het rechteruiteinde van de as heeft nu betekenis, net als dat nulpunt.

**Open vraag voor Dante: punten of procenten.** De andere sessie had een argument dat klopt. `Platform/product.md` zegt dat "94% accuraatheid" de vorm is voor korte outreach, en dat "ongeveer 6 punten van het cijfer van de docent af" de juiste vorm blijft zodra er ruimte is, dus in alles wat een onderwijskundige rustig doorleest. Een landingspaginasectie met een schaal is zoiets. Dante koos eerder vandaag expliciet voor 94/98, dus dat staat er nu, maar het is het overwegen waard.

## Proef v7: de term bij het cijfer (11-09-2026)

- **"Accurate" staat nu bij de percentages**, als eerste regel van het bijschrift onder elk cijfer. Eerst als los woord naast het getal geprobeerd, maar dat liep over de 98% heen.
- **De as definieert de term zonder methodeblok**: "100% is the same mark your team gave". Daarmee weet de lezer wat accuraat hier betekent, zonder dat er een uitleg-alinea bij hoeft.
- Kop en subkop ongewijzigd, die waren goed.

## Proef v8: de sprong zichtbaar maken (11-09-2026)

- **"100% is the mark your team gave" is weg.** Terecht: het cijfer van een menselijk team is zelf ook subjectief, dus dat als norm neerzetten klopt niet. De as heeft nu gewoon 90% en 100% als uiteinden.
- **"Straight out of the box" is vervangen** door wat er feitelijk gebeurt: "before the lecturer instructs it" en "after the lecturer instructs it". Instrueren is ook de term uit het productdocument, waar de docent de opdrachtbeschrijving, de rubric en de feedbackinstructies aanlevert.
- **Icoon bij "accurate".** Een schietschijf, bij 94% open en bij 98% met een gevulde roos. Dat is een niet-numeriek signaal dat het beter is geworden.
- **De sprong is nu expliciet**: een groene badge met pijl omhoog en "4 points closer", midden op het groene segment.
- **Boven en onder even veel lucht**, allebei 68 pixels. Stond eerder op 60 boven en 128 onder.
- De zwevende labels boven de balk zijn vervangen door een raster van twee kolommen. Die absolute positionering liep bij langere bijschriften over elkaar heen.

Drie dingen zeggen nu samen dat het beter wordt: de parallelle bijschriften voor en na, de gevulde roos, en de badge met het verschil.

## Proef v9: dragers naar de foto (11-09-2026)

De losse feitenrij onder de kaart is weg. 435, 13 en 6 staan nu linksonder op de foto, onder het logo en de regel "Bath Spa University, Pilot June 2026", gescheiden door een dunne lijn.

Reden: het zijn allemaal antwoorden op dezelfde vraag, welke pilot is dit. Die horen bij elkaar. Het cijferpaneel gaat nu alleen nog over de meting zelf.

De foto is iets hoger geworden (440 in plaats van 380) en de sluier loopt onderaan donkerder door, zodat de dragers leesbaar blijven zonder een eigen vlak.

## Proef hero (11-09-2026)

Bestand: `proef-hero.html`. Volgende sectie na het bewijsblok, op hetzelfde patroon.

**Waarom de hero als tweede proef.** Het is de sectie die bepaalt of iemand de rest leest, 57% van de kijktijd zit boven de vouw. Het is ook de plek waar de message match met de advertentie zit, en dat is volgens het onderzoek de sterkste hefboom op de hele pagina. En het is de lastigste sectie, dus die nu doen maakt de rest goedkoper.

**De kop.** "Grade essay 140 like you graded essay one". "Grade" en "essay" staan erin omdat bijna al het advertentieverkeer op die woorden binnenkomt: essay grader 43 kliks, ai essay grader 28, ai grading 16. Het groene deel draagt de belofte en begint op een eigen regel.

**Eén knop.** Groen mag hier, dit is de enige plek op de pagina waar "kijk hier" en "klik hier" samenvallen. Daaronder een tekstlink naar beneden, geen tweede knop.

**De bewijsregel** staat direct onder de knop: "94% accurate in a UK pilot" plus de vier logo's. Boven de vouw, zoals het onderzoek aanraadt, en de logo's doen hier hun herkenningswerk in plaats van in het bewijsblok.

**Het beeld, drie panelen die onder de vouw doorlopen.** Links essay 1, al afgetekend. Midden essay 140, wacht op de docent, met de voorgestelde opmerking en Approve. Rechts de hele lichting. Samen: zelfde criteria, zelfde behandeling, jij tekent af. Het label "Lecturer + AI" komt uit de marketingtekst.

**Regels van het app-herontwerp toegepast** (`Design/Website/app-homepage-redesign`): Inter met drie groottes, geen League Spartan in een fragment, geen voortgangsring of balk, geen ratio zoals 12/32 maar één held-getal met zijn woord ("20 to grade"), kleur alleen op de afwijking. Dat laatste is hier het criterium waar het model onzeker is, in rood met waarschuwingsteken.

## Hero v2 (15-09-2026)

- **Tweede zin uit de subkop weg** en de regel "94% accurate in a UK pilot" weg. Allebei stonden ze al in `hero.png` ("You sign off" en "94% accurate"), dus dat was dubbel.
- **Book a demo is navy**, ook in de hero. Dat vervangt de oude regel dat de hero-CTA groen mocht zijn.
- **Lijn onder de navigatie weg.**
- **`creatives/product-images/hero.png` verwerkt** in plaats van de drie zelfgebouwde panelen. 3120x1320, transparant. De losse paneel-CSS is opgeruimd.
- De bewijsregel is nu alleen nog "Used by teaching teams at" plus de vier logo's.

## Proef pijn, sectie 2 (15-09-2026)

Bestand: `proef-pijn.html`. Licht, als tegenhanger van het donkere bewijsblok.

- **Kop:** "The same essay gets a different grade depending on who opens it", sleutelwoord groen. Subkop zegt waarom dat pijn doet: de student twijfelt aan de beoordelaar, niet aan het werk.
- **Bento met één dominant geval.** De 7-tegen-6 krijgt het grote vak met beeld, de twee andere zijn ondersteunend.
- **Het beeld:** twee beoordelaarskaartjes voor dezelfde inzending, met een chip erboven die zegt dat het om hetzelfde werk en dezelfde rubric gaat. Zonder die chip is het verschil niet het punt.
- **Kleur:** rood alleen op de afwijking, het gat tussen de cijfers en de vier beoordelaars die uit de pas lopen. Groen alleen op het sectielabel.
- **Bronnen onderaan elke kaart**, instellingen zonder namen van personen. Alles uit de 50 goedgekeurde uitspraken in `GTM/ICP/pijn-oplossing`.

## pagina.html: de hele pagina in één bestand (15-09-2026)

Afgewerkte secties in kleur, de rest nog als wireframe met een badge rechtsboven.

| # | Sectie | Staat |
|---|---|---|
| 1 | Hero | afgewerkt |
| 2 | Pijn | afgewerkt |
| 3 | How it works | wireframe |
| 4 | Proof | afgewerkt |
| 5 | Products | wireframe |
| 6 | Fit & trust | wireframe |
| 7 | FAQ | wireframe |
| 8 | Book | wireframe |

Gebouwd met `build-pagina.mjs`. Dat script pakt uit elk proef-bestand de stijl en de sectie, scopet de CSS onder een eigen wrapper-class (`.s-hero`, `.s-pijn`, `.s-bewijs`, `.s-wire`) en plakt er de nog niet uitgewerkte wireframe-secties tussen. Zonder die scoping overschrijven `.card` en `.h2` uit verschillende secties elkaar.

**Bijwerken:** pas het losse proef-bestand aan en draai `node build-pagina.mjs`. Nooit direct in `pagina.html` werken, dat wordt overschreven.

Is een sectie af, zet hem dan in `build-pagina.mjs` op `klaar: true` met zijn proef-bestand erbij.
