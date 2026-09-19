# Onderzoek: hoe tonen we bewijs op de landingspagina

Datum: 2026-09-11. Stand: snel (3 subagents). Aanleiding: Dante vindt het bewijs op de wireframe dun en weggestopt.
Label per bron: **primair** (origineel onderzoek/document), **secundair** (journalistiek, onafhankelijke analyse), **tertiair** (blog, vendorcontent).

## Het antwoord

1. **Het sterkste bewijsblok is één stuk dat naam, cijfer en context combineert**, niet een rij logo's en niet een losse quote. Het enige gecontroleerde experiment met een harde metriek dat we vonden (comScore via Optimizely, n ≈ 2.500) liet een testimonial mét klantlogo +69% demo-aanvragen scoren tegenover dezelfde testimonial zonder logo.
2. **Onze pilotcijfers zijn sterker bewijs dan onze logo's**, zeker bij deze doelgroep. Onderzoek naar edtech-inkoop in UK HE noemt demo's en pilots de zwaarstwegende bewijsvorm en testimonials expliciet "questionable rigour".
3. **Het cijfer mét methode is onze onderscheidende zet.** "6 punten van het docentcijfer, 435 opdrachten, 13 markers" is geloofwaardiger dan "95% accuraat", en precies waar concurrenten onderuit gaan: EssayGrader onderbouwt met een externe dataset van 22.000 essays, CoGrader claimt ~5% variantie op eigen testen zonder gepubliceerde benchmark. Dat verschil is zichtbaar voor een academicus.
4. **Bewijs hoort bij de CTA, niet onderaan de pagina.** Daar is geen gecontroleerde test voor (zie gaten), wel consensus. Wat wél hard is: bewijs dat generiek en decoratief is wordt genegeerd (banner blindness op logo-walls), bewijs dat specifiek en gekwantificeerd is werkt.
5. **Social proof werkt niet universeel.** Een veldexperiment op open-source repo's (arXiv 2026) vond geen effect van zichtbare sterren en downloadaantallen op downloadgedrag. GoodUI's eigen set van 22 A/B-tests over 148 miljoen bezoekers laat winst én verlies zien, afhankelijk van context.

## Waar bronnen elkaar tegenspreken

**Werkt social proof of niet?**
- Voor: comScore/Optimizely (+69% met logo bij testimonial), WorkZone/VWO (+34% demo-aanvragen na logo's naar grijstinten, 99% significantie).
- Tegen: arXiv-veldexperiment 2026 (geen effect), GoodUI (gemengd), CXL (banner blindness op logo-walls; noemt minstens één test waar wéghalen van social signals de conversie verhoogde).
- **Mijn weging:** de scheidslijn is niet "social proof ja of nee" maar generiek versus specifiek. Een logo-strip zonder context is decoratie. Een naam plus een meetbaar resultaat is bewijs. De WorkZone-case wijst dezelfde kant op: de logo's werden juist minder opvallend gemaakt zodat het formulier won.

**Telt bewijs überhaupt bij onderwijsbeslissers?**
- Een Europese edtech-marktstudie (2024) stelt dat maar 11% van onderwijsbeslissers bewijs meeweegt in de aankoopbeslissing; netwerk en verhaal wegen zwaarder.
- Jisc, UCISA, SURF, DfE en EEF bouwen juist formele evidence-eisen in procurement.
- **Mijn weging:** dit spreekt elkaar niet echt tegen, het gaat over twee fases. De landingspagina spreekt een individuele lecturer of head of assessment aan, niet een inkoopcommissie. Voor hem telt herkenning en een demo. De bewijslast van de tender komt later, en die hoort niet op deze pagina uitgestald.

**Eigen citaten of externe validatie?**
- NN/g: bezoekers lezen site-eigen testimonials met scepsis en vertrouwen externe bronnen meer.
- TrustRadius 2026: 74% van B2B-kopers gebruikt reviews, 53% sprak een peer die het product al gebruikt. Maar 47% vertrouwt online bronnen minder dan vorig jaar, door AI-contentverzadiging.
- **Mijn weging:** wij hebben geen G2-profiel en geen reviews. De externe route die wél openstaat is een onafhankelijke partij als Jisc: hun case study met Graide noemt zelf ook de beperkingen van de pilot, en juist daardoor leest het als onderzoek in plaats van marketing.

## Wat dit betekent voor Eduface

Ons bewijsprobleem is geen tekort, het is presentatie. We hebben precies wat deze doelgroep zwaar laat wegen: een pilot met een echte n, een meetmethode, en vier instellingen die het draaien. Wat we missen is een citaat en een onafhankelijke bevestiging. De pagina moet het bewijs dus niet spreiden over een logobalk hier en een cijferblok daar, maar één blok maken dat de meting draagt: wat is gemeten, bij hoeveel opdrachten, door hoeveel beoordelaars, wat kwam eruit, en waar dat níet geldt. De zelf benoemde beperking is hier een geloofwaardigheidswinst, geen zwakte. Daarnaast: haal minstens één benoembaar citaat op bij de 13 markers uit de pilot, en één bij een NL-klant. Zonder naam werkt het alleen als het citaat heel specifiek is (rol, vak, context).

## Concrete aanbevelingen voor de demopagina

1. **Verplaats het bewijsblok naar direct onder de hero, of laat de hero zelf één bewijsregel dragen.** Nu staat het op positie 6, ver onder de vouw. De pilotmeting is ons sterkste stuk en staat het verst weg.
2. **Maak van het cijferblok een meetkaart, geen drie losse getallen.** Eén blok met: wat gemeten is (afstand tot het cijfer van de beoordelaar), n (435 opdrachten, 13 markers, 6 modules, één UK-universiteit, juni 2026), de uitkomst (~6 punten, ~2 na afstemmen), en één regel over wat het níet zegt.
3. **Schrijf een aparte methodiekpagina en link ernaar vanuit dat blok.** "Hoe we dit gemeten hebben." Dat is wat één pilot laat dragen als onderzoek. Kost ons niets en is precies waar academische lezers op klikken.
4. **Logo's blijven, maar dun en zonder claim.** Een strook zonder kop, niet als bewijssectie opgetuigd. Ze doen herkenningswerk, geen bewijswerk.
5. **Zet één bewijselement naast de eind-CTA.** Niet de hele meetkaart, één regel met het kerngetal en de n.
6. **Toon echte productoutput als bewijsvorm.** Een screenshot van een echte gegenereerde opmerking met de criteriumkoppeling erbij is voor deze lezer controleerbaarder dan een quote. Dat zit al in de wireframe, maar staat daar als uitleg en niet als bewijs.
7. **Nooit meer "95% accuraat" of "30.000 studenten" zonder bron.** Dat is het patroon waarop concurrenten worden afgeschoten, en onze eigen productbron kent die cijfers niet.
8. **Vraag Jisc of een pilotpartner om een publiceerbare bevestiging.** Dat is de enige externe validatieroute die voor ons realistisch openligt.

## Gaten

- **Geen enkele gecontroleerde test** die hero versus onder-de-hero versus naast-de-CTA versus eigen sectie tegen elkaar zet. Alle "34 tot 42% lift door trust signals"-cijfers die rondgaan komen uit blogs zonder methodologie. De aan Baymard toegeschreven cijfers zijn niet bij Baymard zelf terug te vinden.
- **Geen norm voor hoe vaak** bewijs herhaald moet worden op een pagina.
- **Geen academische studie** over geanonimiseerde versus benoemde testimonials in B2B SaaS. Wat er is, komt van reviewbedrijven met een eigen belang.
- **Geen enquête onder UK HE-beslissers** specifiek over de vraag wat hen als edtech-koper overtuigt.
- Eigen meting is dus de enige echte benchmark. De huidige pagina haalt 27% CTA-kliks en 0 boekingen, dat is het getal om tegen af te zetten.

## Bronnen

**Primair**
- GoodUI Pattern #4, testimonials: 22 A/B-tests, 148 miljoen bezoekers, gemengde uitkomsten. https://goodui.org/patterns/4/
- Veldexperiment zichtbare social proof bij open-source software, geen effect op downloads. https://arxiv.org/pdf/2603.07919 (2026)
- Stanford Web Credibility Project, Fogg e.a.: amateurisme en te veel verkooptaal schaden geloofwaardigheid het meest. https://credibility.stanford.edu/guidelines/index.html (ca. 2002, nog steeds primaire bron)
- NN/g, Trustworthy Design: site-eigen testimonials worden met scepsis gelezen, externe bronnen wegen zwaarder. https://www.nngroup.com/articles/trustworthy-design/
- Jisc, framework for digital transformation in higher education: ISO, databeveiliging, interoperabiliteit als leverancierseisen. https://www.jisc.ac.uk/guides/framework-for-digital-transformation-in-higher-education
- SURF, edtech-update: toetsing op privacy, security, inclusiviteit, onderwijsvisie, roadmap. https://www.surf.nl/files/2024-03/edtech-update-surf-en-npuls-ellena-papageorgiou-surf.pdf (2024)
- EEF en DfE, EdTech Testbed: tot 100 snelle evaluaties, tot 15 RCT's. https://educationendowmentfoundation.org.uk/news/partnership-department-for-education-impact-of-edtech-tools (2023-2024)
- Jisc Digital Experience Insights 2023/24, 3.287 docenten. https://digitalinsights.jisc.ac.uk/reports-and-briefings/our-reports/2023-24-uk-higher-education-teaching-staff-digital-experience-insights-survey-findings/
- Unbounce Conversion Benchmark Report, 41.000+ pagina's. https://unbounce.com/conversion-benchmark-report/ (2024)
- Peer-reviewed studie over onderbouwing van steekproefgrootte in servicesmarketing: minder dan 15% doet het. https://www.tandfonline.com/doi/full/10.1080/02642069.2026.2612706 (2026)

**Secundair**
- comScore A/B-test via Optimizely: testimonial met logo +69% t.o.v. zonder. https://github.com/optimizely/scribe/blob/master/content/stories/comscore.md
- Jisc National Centre for AI, case study met Graide: negen universiteiten fase 1, vijf fase 2, plus expliciete beperking bij kleine cohorten. https://www.e-assessment.com/resource-hub/case-study/jiscs-national-centre-for-ai-ncai-case-study-with-graide (2025-2026)
- TrustRadius 2026 B2B Buying Disconnect: 74% gebruikt reviews, 47% vertrouwt online bronnen minder dan vorig jaar. https://hginsights.com/news/trustradius-2026-b2b-buying-disconnect-report-reveals-ai-has-changed-how-buyers-research-but-not-what-they-trust/
- G2 2026 Buyer Behavior: 56% raadpleegt bestaande gebruikers, 71% bij enterprise. https://company.g2.com/news/buyer-behavior-2026
- Studie over inconsistentie van AI-detectietools in HE, inclusief het Texas A&M-incident. https://www.mdpi.com/2078-2489/16/10/905 (2025)
- Times Higher Education: academici geven lagere cijfers bij vermoeden van AI-gebruik. https://www.timeshighereducation.com/news/academics-marking-students-down-when-they-suspect-ai-use

**Tertiair (vendorcontent of blog, met voorbehoud)**
- WorkZone via VWO: logo's naar grijstinten, +34% demo-aanvragen. https://vwo.com/success-stories/workzone/
- Graide impact report: 235 responses, "up to 99% accuracy", Birmingham 89% minder nakijktijd, zonder betrouwbaarheidsintervallen. https://www.graide.co.uk/blog/graides-impact-report-understanding-the-roi-of-ai-driven-grading-solutions (2026)
- Vergelijking EssayGrader (externe dataset van 22.000 essays) versus CoGrader (intern, 500+ essays). https://fiveable.me/fiveable-vs-cograder-vs-essaygrader (2026)
- Digital Promise ESSA Tier 3 en 4 certificering. https://digitalpromise.org/product-certifications/evidence-based-edtech-essa-tier-3/

---

# Aanvulling 2026-09-11: wat we echt in handen hebben

Dante leverde de case study-concept van Hogeschool Rotterdam (BDK) aan en gaf het citaat van Els Stapersma vrij. Daarmee verandert de conclusie hierboven: we hebben meer bewijs dan ik dacht, maar het zit verspreid over materiaal dat niet voor de website is geschreven.

## Bruikbaar, in volgorde van kracht

**1. Hogeschool Rotterdam, BDK-pilot (case study-concept, nog niet goedgekeurd door Rotterdam)**
- 79% van de studenten positief of neutraal (57% positief, 22% neutraal), zonder aanvullende docentbegeleiding.
- Tweede feedbackronde werd merkbaar beter ervaren dan de eerste, na verfijning van de rubricconfiguratie.
- Rapporten van meer dan 20 pagina's, feedback op samenhang en modelkwaliteit, niet op schrijfkwaliteit.
- Zes feedbackcategorieën die studenten het hoogst waardeerden, waaronder APA-controle, onderbouwing van kernpunten en opmerkingen in het document zelf.
- Slotcitaat uit de eindevaluatie: "We moeten als opleiding blijven werken met AI in ons onderwijs. Studenten verwachten het... Niets doen is geen optie."
- **Dit is onze enige echte case study met een tweede meetmoment.** Dat tweede moment is het interessantste stuk: het laat zien dat afstemmen werkt, precies wat de Bath Spa-cijfers ook zeggen. Twee onafhankelijke bronnen die hetzelfde mechanisme aanwijzen is sterker dan één groot getal.
- **Blokkade:** het is een concept. Zonder akkoord van Rotterdam mag er niets van naar buiten.

**2. Els Stapersma, De Haagse Hogeschool (vrijgegeven door Dante)**
- Sterkste voor de pagina: "Bovendien wordt die tool nooit moe en geeft hij in sommige opzichten betere feedback dan ik." (05-11-2025)
- Alternatief, meer pijn dan lof: "Begin januari heeft Sco haar eerste grote schrijfopdracht voor zes klassen. Dat is echt heel veel nakijkwerk. Ik wil natuurlijk graag Eduface daarbij gebruiken." (05-11-2025)
- **Dit is ons eerste benoembare citaat.** Onderzoek hierboven: benoemd verslaat anoniem, en specifiek verslaat vaag. Dit is allebei.
- **Twee aandachtspunten:** de pagina is Engels en zij spreekt Nederlands, dus vertalen of als NL-citaat met vertaling tonen. En één check of zij akkoord is met publicatie mét naam en instelling op een publieke pagina.

**3. Bath Spa, alleen als geanonimiseerde pilot**
- Helen King, 30-03-2026: "I'll share my experiences of the pilot (which have been positive so far) but I won't be specifically endorsing Eduface."
- 25-06-2026: de business case wordt door Bath Spa zelf geschreven, zonder Eduface, wegens belangenverstrengeling.
- 29-03-2026: zij corrigeerde de webinartitel van "introducing" naar "exploring", omdat implementatie nog niet vaststaat.
- **Conclusie: Bath Spa is geen referentie en wordt dat voorlopig niet.** Blijft "one UK university". Nooit de naam, nooit een citaat, ook niet indirect.

## Een probleem met ons kerncijfer dat ik eerder niet zag

De ~6 punten en ~2 punten komen uit de Bath Spa-pilot. In datzelfde materiaal zeggen markers iets anders:
- Niamh McGrogan (PGCE, 11-05-2026): "the marking isn't any more accurate, it's a little less so in fact... tutors will just need to ensure they trust their own judgment rather than be influenced by the AI pass/fail."
- Andy Gray (04-06-2026): "The system was missing the mark in regards to feedback. So I opted to do the feedback myself."
- Judith Holby (14-05-2026): stijl en beoordeling botsten met hun eigen beleid, kostte tijd om te herschrijven.

Dat is geen tegenspraak van het cijfer, het is programma-afhankelijkheid: PGCE is een professionele pass/fail-opleiding met ander opdrachtontwerp, en daar werkte het minder goed dan in de OBM-vakken. Maar het betekent wel:
- **Het cijfer moet zijn grens meedragen op de pagina.** Precies wat de Jisc-case study met Graide ook doet (werkte minder goed bij kleine cohorten) en wat die bron geloofwaardig maakt.
- **Nooit "95% accuraat".** Als een prospect ooit met een marker uit die pilot spreekt, valt een kale claim direct om.
- Susana Romans-Roca vroeg er zelf om (25-06-2026): "would it be possible to include an explanation of how the average time spent on marking is calculated and a definition of 'accuracy' in this context." De klant vraagt dus letterlijk om de methodiekpagina uit aanbeveling 3.

## Bijgestelde aanbevelingen

Aanbevelingen 1 tot 8 hierboven blijven staan. Hierbij:

9. **Bouw het bewijsblok op twee benen, niet één.** Been 1 is het cijfer met methode (UK-pilot, anoniem). Been 2 is de Rotterdam-case met het tweede meetmoment. Samen zeggen ze: het werkt, en het wordt beter naarmate je het afstemt. Eén been is een claim, twee benen is een patroon.
10. **Het Els-citaat komt naast de CTA, niet in een testimonial-rij.** Eén benoemd citaat in een rij van drie leest als "we hadden er maar één". Naast de knop leest het als bewijs op het moment van beslissen, en dat is de plek die het comScore-experiment aanwijst.
11. **Vraag Rotterdam om akkoord op de case study.** Dat is de snelste bewijswinst die we kunnen boeken, en het materiaal ligt er al.
12. **Zet de grens van het cijfer op de pagina zelf.** Eén regel: waar het minder goed werkte en waarom. Dat kost geen conversie bij deze doelgroep, het wint vertrouwen.

## Wat nog ontbreekt

- Akkoord van Rotterdam op de case study.
- Bevestiging van Els op publicatie met naam.
- Een UK-referentie. Bath Spa valt af, dus die moet uit een andere pilot komen.
- De methodiekpagina, die zowel het onderzoek als de klant zelf vraagt.

---

# Besluiten van Dante, 2026-09-11

1. **Rotterdam heeft akkoord gegeven** op de BDK-case study. Blokkade weg, het materiaal mag naar de pagina.
2. **Bath Spa mag bij naam.** Vervangt de anonimiseringsregel hierboven. Zie risico hieronder.
3. **De methode van het cijfer hoeft niet op de pagina.**

## Hoe besluit 3 uitpakt

Dit botst niet met `Platform/Product/product.md`, het volgt de regel voor korte copy daar: "In korte outreach mag je gewoon 94% accuraatheid zeggen, met de dragers erbij: over 435 opdrachten en 13 nakijkers." De dragers zijn geen methode, dat is de identiteit van het getal.

Dus op de pagina: **94% accuraatheid, over 435 opdrachten en 13 markers.** Niet: de definitie van accuraatheid, niet de 6-punten-formulering, niet de grens per programma.

Twee dingen die daar wel uit volgen:
- **"~6 pts" vervalt als hoofdgetal.** Zonder definitie is dat niet te lezen: 6 punten waarvan af, op welke schaal. 94% is zelfdragend, 6 punten niet. Het bewijsblok wordt dus 94% en 98% (na afstemmen), niet 6 en 2.
- **De definitie verhuist naar de FAQ**, niet naar het bewijsblok. Dezelfde bron zegt: nooit blijven staan op het kale percentage als iemand ernaar vraagt. Een FAQ-regel is geen methodeblok en kost geen aandacht in de scan.

## Risico bij besluit 2, één keer genoteerd

Helen King schreef op 30-03-2026: "I'll share my experiences of the pilot (which have been positive so far) but I won't be specifically endorsing Eduface." Op 29-03-2026 liet zij de webinartitel wijzigen van "introducing" naar "exploring" omdat implementatie niet vaststaat, en op 25-06-2026 schrijft Bath Spa de business case bewust zonder ons wegens belangenverstrengeling. Bath Spa als klant opvoeren terwijl de licentiebeslissing nog loopt kan die deal raken. Dante's besluit, genoteerd, we gaan door.

Praktische uitwerking die het risico klein houdt zonder het besluit terug te draaien: Bath Spa noemen als **pilot** ("piloted at Bath Spa University"), niet als klant of referentie, en geen citaat van Helen of de markers gebruiken. Dat is feitelijk juist en het is precies wat zij zelf publiek al zegt.

## Het bewijsblok zoals het nu wordt

- **Been 1, de meting:** 94% accuraatheid, 98% bij markers die het model hadden afgestemd. Over 435 opdrachten, 13 markers, 6 vakken. Bath Spa University, juni 2026.
- **Been 2, de case:** Hogeschool Rotterdam, BDK. 79% van de studenten positief of neutraal, en de tweede feedbackronde werd merkbaar beter gevonden na het verfijnen van de rubric.
- **Het citaat, naast de CTA:** Els Stapersma, De Haagse Hogeschool. "Bovendien wordt die tool nooit moe en geeft hij in sommige opzichten betere feedback dan ik."
- Beide benen zeggen hetzelfde: het werkt, en het wordt beter naarmate je het afstemt. 94 naar 98 aan de ene kant, ronde 1 naar ronde 2 aan de andere.

## Nog open

- Bevestiging van Els op publicatie met naam en instelling.
- Vertaling van haar citaat, de pagina is Engels.

## Besluiten 2026-09-11, vervolg

- **Balk uit het Rotterdam-been.** Alleen 79% blijft staan. De 57/22/21-verdeling gaf een naamloos restant en dat was informatie zonder label.
- **Els Stapersma mag bij naam en instelling op de pagina.** Bevestigd door Dante. Engelse vertaling zoals die nu op de pagina staat: "It never gets tired, and in some ways it gives better feedback than I do." Origineel: "Bovendien wordt die tool nooit moe en geeft hij in sommige opzichten betere feedback dan ik." (05-11-2025)
