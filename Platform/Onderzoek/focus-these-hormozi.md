# Klopt de focus-these van Hormozi, en klopt hij voor onze fase?

_Onderzoek 13-09-2026. Aanleiding: Dante keek de video "busy but broke" van Alex Hormozi en wil weten of het punt hout snijdt voor Eduface nu._

## Deel 1 — De interne meting (repo, Close, Todoist, 13-09-2026)

Voor het web opgegaan is, eerst wat er aantoonbaar bij ons gebeurt.

### Aantal gelijktijdige werkstromen
`projects/` bevat 35 mappen. Gewijzigde bestanden per map in de laatste 30 dagen (bestandsdatums, niet commits: op 11-09 is er een reddingscommit van 1.571 bestanden gedaan waardoor commitgeschiedenis geen bruikbare maat is):

| Map | Bestanden geraakt (30 dgn) | Laatst |
|---|---|---|
| shift | 260 | 11-09 |
| blog-launch | 130 | 08-09 |
| breederode-hogeschool | 119 | 11-09 |
| windesheim | 103 | 13-09 |
| sales-coach | 78 | 05-09 |
| landing-page-demo-survey | 61 | 11-09 |
| action-learning-demo | 34 | 11-09 |
| website-building | 29 | 14-08 |
| targetlijst-nl | 22 | 10-09 |
| usability-test | 20 | 26-08 |
| cold-calling | 18 | 10-09 |
| uti | 14 | 08-09 |
| app-homepage-redesign | 12 | 11-09 |

Zestien mappen geraakt in dertig dagen, dertien daarvan met meer dan een paar bestanden. Dat is de maat voor "hoeveel feestjes tegelijk".

### De SHIFT-pijplijn: gebouwde voorraad tegenover verstuurd werk
Uit `GTM/ICP/shift/master/` op 13-09-2026:

| Stap | Aantal |
|---|---|
| Organisaties gesourced | 466 (430 NL, 36 UK) |
| Daarvan gekwalificeerd | 264 |
| Contactpersonen in het bestand | 340 |
| Onderzocht met haakje gevonden | 169 |
| Bericht goedgekeurd | 57 |
| Daarvan ooit verstuurd | **0** |
| Ooit iemand benaderd (alle batches) | 45 |
| Reacties | 2 |
| Uitkomsten vastgelegd | 1 (geen interesse) |

Laatste verstuurmoment: **11-08-2026** (LinkedIn) en 13-08-2026 (mail). Daarna een maand lang geen enkel bericht de deur uit, terwijl er in diezelfde maand 261 commits op de pijplijn zijn gedaan en de hele machine internationaal is gemaakt (besluit 10-09-2026). Op 11-09 zijn er weer nieuwe UK-contacten toegevoegd aan de wachtrij.

Kanttekening bij de cijfers: `linkedin_geaccepteerd_op` staat op 0 voor alle 340 rijen. Dat is vermoedelijk niet bijgehouden, niet echt nul acceptaties. De 45 verstuurd en 2 reacties zijn wel hard.

### De stilstaande voorraad, preciezer
- 88 berichten staan op goedgekeurd of concept, waarvan er 85 voor het laatst zijn bijgewerkt op 02-09-2026.
- 23 daarvan zitten in een Lemlist-campagne die op draft staat en wacht tot Dante hem start.
- 43 hebben in Lemlist nog de oude tekst van voor de herschrijfronde van 02-09 en moeten eerst bijgewerkt worden.
- Twee campagnes bevatten samen 55 leads (`cam_EdWwoX8hQEYcocLbc` 41, `cam_sjhBnYPdNqMQBvKYZ` 14).

### Wat er tegenover staat in Close
19 actieve opportunities, bruto €883.500, gewogen €313.850.

| Fase | Deals | Waarde |
|---|---|---|
| Contracting | Bath Spa (€80k, 75%), Haagse Hogeschool (€30k, 65%), Hogeschool Rotterdam (€20k, 65%) | €130k |
| Scoping | UTI (€150k, 50%), BSN (€18k, 50%), Notenboom (€8k, 20%) | €176k |
| Pilot | Tilburg, Radboud, UMCG | €55k |
| Discovery / Interested | RUG, Windesheim, Bristol, Goldsmiths, UADE, Breederode, CMI, HBMSU, Noordhoff, Academica | €522k |

Vier opportunities zijn sinds 20-21 juli niet meer aangeraakt (Radboud, Tilburg, UMCG, RUG). Windesheim heeft een verwachte closedatum van 22-09-2026 en staat op 0% confidence.

### Belangrijke nuance: het bedrijf staat niet stil
Geregistreerde activiteiten in Close (mails, calls, meetings) per maand:

| Maand 2026 | Activiteiten |
|---|---|
| maart | 380 |
| april | 450 |
| mei | 330 |
| juni | 242 |
| juli | 227 |
| augustus | 230 |
| september (13 dgn) | 115 |

Verschillende leads die per maand zijn aangeraakt: 31 (maart), 44, 43, 46, 32, 34 (augustus), 26 in de eerste 13 dagen van september. Ruwweg 230 activiteiten over 34 accounts is zeven aanrakingen per account per maand.

Het beeld is dus niet "er gaat niets uit". Er gaat maandelijks ruim 230 keer iets uit, stabiel sinds juni, na een piek in maart-april. Wat stilstaat is specifiek de nieuwe koude pijplijn: die produceert voorraad en geen verzonden berichten. De accountkant loopt door.

### Attributie ontbreekt
Close heeft geen bronveld op leads (custom fields zijn: Authority found, Webinar presences, Business school, Nurturing list, Company Website, Owner). Er is dus **geen enkele manier om uit het CRM te halen welk kanaal die 19 opportunities heeft opgeleverd**. Dat is precies het cijfer dat je nodig hebt om te bepalen welke "party" werkt.

## Deel 2 — Het bewijs onder het algemene principe

### Wat hard is
- **Taakwisselkosten bij individuen** zijn een van de best gerepliceerde effecten in de cognitieve psychologie. Rubinstein, Meyer & Evans (2001, *J. Exp. Psychol.* 27(4), vier gecontroleerde experimenten, https://pubmed.ncbi.nlm.nih.gov/11518143/): wisselen verhoogt reactietijd en fouten, sterker naarmate de taak complexer is. Bevestigd in het overzicht van Kiesel et al. (2010, *Psychological Bulletin* 136).
- **Attention residue** (Leroy 2009, *OBHDP* 109(2), https://www.sciencedirect.com/science/article/abs/pii/S0749597809000399): een onafgemaakte taak A verslechtert je prestatie op taak B. Sterkst bij onafgemaakt werk onder tijdsdruk. Dit is het mechanisme onder "57 goedgekeurde berichten die blijven liggen".
- **Multi-project overload** (Zika-Viktorsson et al. 2006, *IJPM* 24(5), survey n=392): een derde van de respondenten rapporteert overload, significant samenhangend met stress en achterstand op schema. Cross-sectioneel en zelfrapportage, dus samenhang, geen bewezen oorzaak.

### Wat folklore is dat zich voordoet als onderzoek
- **De "20% verlies per extra project"-regel** (Weinberg 1991) is een consultantvuistregel zonder steekproef of meting. Wordt overal geciteerd alsof het een meting is.
- **"23 minuten om te herstellen van een onderbreking"** komt uit een interview met Gloria Mark (2006), niet uit een peer-reviewed paper. Haar eigen geobserveerde data (Mark et al., CHI 2005, https://ics.uci.edu/~gmark/CHI2005.pdf) laat zelfs zien dat onderbroken werknemers taken *sneller* afmaken (20,3 min tegen 22,8 min), maar met meer stress.
- **Theory of Constraints**: het vaakst geciteerde bewijs is Mabin & Balderstone (1998, 77 bedrijven, gemiddeld 68% meer doorvoer, https://www.tocinstitute.org/uploads/1/2/7/9/12796657/toc_impact_study.pdf), gepubliceerd door het TOC Institute zelf, cases zelf-gerapporteerd door TOC-consultants, geen controlegroep. Watson et al. (2007, *Journal of Operations Management*) noemt de onderzoeksbasis zwak tegenover de populariteit.
- **WIP-limieten**: Little's Law is wiskunde, geen empirische claim. De enige directe test bij een softwarebedrijf (ACM/IEEE ESEM 2018, 8.000+ items, 4 jaar, https://dl.acm.org/doi/10.1145/3239235.3239238) vond dat lagere WIP wel de doorlooptijd verkort maar de productiviteit *verlaagt*. In Accelerate (Forsgren et al. 2018) zijn WIP-limieten op zichzelf geen significante voorspeller van performance, alleen in combinatie met zichtbaarheid en een feedbackloop.

### Gat
Er bestaat geen gecontroleerde studie die meet wat er gebeurt als een bedrijf van N werkstromen naar 1 gaat. Het labbewijs gaat over seconden en minuten, de bedrijfsclaim over weken en maanden. Die brug legt niemand hard.

## Deel 3 — Hoe hard zijn Hormozi's eigen claims

- **De 20%-regel** ("elke verandering kost je eerst 20% voordat je enige upside ziet") is zijn eigen vuistregel uit zijn Scaling Workshop. Geen data, geen bron, geen onderzoek erachter te vinden (samenvattingen: https://dickiebush.substack.com/p/12-takeaways-from-alex-hormozis-scaling, 2024). Behandel het als intuïtie, niet als een getal waar je op rekent.
- **De priority-etymologie klopt in de kern.** De OED dateert de betekenis "iets dat belangrijker is dan andere dingen, vaak in het meervoud" op 1936 (https://www.oed.com/dictionary/priority_n; bevestigd via https://grammarphobia.com/blog/2016/09/priority.html, 2016). De popversie komt uit Greg McKeown's *Essentialism* (2014), niet van Hormozi. Geen taalkundige weerlegging gevonden. Leuk weetje, geen bewijs voor de bedrijfsclaim.
- **Zijn eigen geschiedenis weerspreekt de boodschap gedeeltelijk.** Gym Launch (2016), Prestige Labs (2019), ALAN (2020) en Acquisition.com (2020) liepen tegelijk, met een gezamenlijke exit in 2021. Er was taakverdeling met Leila, maar hij was mede-oprichter van alle drie tegelijk. De pagina waarop hij focus verkoopt heet letterlijk acquisition.com/just-crush-one.
- **De cijfers zijn zelf opgegeven.** $250M+ portfolio-omzet, de $46,2M exit, het vermogen van $100M tot $350M: allemaal uit eigen posts en podcasts, nergens onafhankelijk geverifieerd. Het persbericht van de koper was niet op te halen.
- **De bekendste kritiek is survivorship bias**: de regels zijn gegeneraliseerd uit één geslaagd traject. Daar komt bij dat hij zowel aan bedrijven verdient als aan het publiek (boeken, workshops, cursussen), dus er zit een prikkel op het verkopen van advies los van of het generaliseert.

**Wat dit betekent voor het wegen van de video:** de onderliggende mechanismen (taakwisselkosten, attention residue, doorstroom) zijn echt. De specifieke getallen in de video zijn dat niet. Neem het denkraam serieus, de cijfers niet.

## Deel 4 — De volumewiskunde van onze markt

- **Doorlooptijd is de harde beperking, niet kanaalkeuze.** Inkoop bij hogescholen en universiteiten loopt 6 tot 18 maanden; een departementale deal kan in weken, campusbreed is 12 tot 18 maanden (https://tamtotarget.com/higher-education-sales-guide/, 2025, GTM-bureau, dus vendorcontent). UK-instellingen draaien een boekjaar van 1 augustus tot 31 juli, en voor een septemberstart is maart de cut-off om naar de markt te gaan (https://litmuspartnership.co.uk/the-tender-cycle-when-to-act-and-why-timing-matters/, inkoopadviesbureau). Wie je vandaag benadert is dus pipeline voor Q2/Q3 2027, niet voor dit kwartaal.
- **Antwoordpercentages zijn hard gedaald.** Platformbreed 3,43% in 2026 tegen 5,1% in 2025 (https://instantly.ai/cold-email-benchmark-report-2026). Belkins meet op strikt koude lijsten 0,45% over 7,5 miljoen mails in 2025 (https://belkins.io/blog/cold-email-response-rates). Smalle, echt gepersonaliseerde lijsten halen 5,8% tot 18% (Lemlist/Woodpecker-analyse). Alle bronnen zijn verkopers van outreach-software, dus gekleurd, maar ze wijzen dezelfde kant op.
- **LinkedIn-acceptatie** ligt volgens zeven vendorstudies tussen 26% en 51%, met 30-45% als gezond bij scherpe targeting.
- **Coverage.** Gemiddelde B2B-winrate zakte naar 19% in 2025 (van 29% in 2024, Ebsta x Pavilion via https://www.gradient.works/blog/2025-b2b-sales-performance-benchmarks). De vuistregel 1/winrate geeft dan 4 tot 6 keer coverage: voor 4 closes heb je ruwweg 20+ gekwalificeerde kansen nodig.
- **Doorgerekend:** met 2026-conversies (5-8% reply op een smalle gepersonaliseerde lijst, waarvan grofweg een derde substantieel) heb je honderden tot laag-duizenden benaderingen nodig om die 20 kansen te voeden. Met de oudere, optimistischere RAIN Group-cijfers uit 2017 (52% contact-naar-meeting bij topperformers) zou 40 tot 170 volstaan. Die twee ramingen liggen een orde van grootte uit elkaar, en RAIN dateert van voor de AI-outreachverzadiging. Neem de pessimistische.
- **Koopgroepen** zijn 5 tot 16 mensen over maximaal 4 functies, en 74% van de koopteams laat ongezond conflict zien tijdens het besluit (Gartner, 632 kopers, veldwerk aug-sep 2024, gepubliceerd mei 2025).

**Wat dit doet met de focus-these:** 45 benaderde mensen is onder elke aanname te weinig. De wiskunde duwt richting meer doorstroom, niet richting minder. "Focus" kan hier dus niet betekenen "benader minder mensen". Het kan alleen betekenen: één segment, één kanaal, veel meer volume daarbinnen.

## Deel 5 — Zoekfase tegenover schaalfase: wat bepaalt de juiste breedte

Dit is het deel waar Hormozi's advies het meest bijgesteld moet worden. De literatuur zegt niet "pre-PMF mag breed, post-PMF moet smal". Hij zegt iets preciezers.

- **Breedte hangt af van drie parameters, niet van je fase.** Loch, Terwiesch & Thomke (2001, *Management Science* 47(5), https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/P12.pdf): dure tests horen serieel, trage tests horen parallel, en ruisige tests maken parallel juist minder aantrekkelijk. Voor ons trekken die tegen elkaar in: een HE-verkooptraject is traag (pleit voor parallel) maar ook duur in oprichterstijd en extreem ruisig (één gesprek bij één hogeschool zegt bijna niets), wat voor serieel pleit.
- **Het "veel kleine bets"-bewijs gaat over portefeuilles, niet over jouw bedrijf.** Kerr, Nanda & Rhodes-Kropf (2014, *JEP* 28(3), https://www.nber.org/system/files/working_papers/w20358/w20358.pdf) meet VC-portefeuilles: 55% van de investeringen wordt geliquideerd, 6% levert de helft van het rendement. Dezelfde auteurs schrijven binnen de firma juist sequentiële staging voor: per ronde precies de ene onzekerheid oplossen die die ronde moet oplossen. Wie dit paper gebruikt om tien werkstromen in één startup te verdedigen, gebruikt het verkeerd.
- **Het optimum ligt in het midden, niet op één.** Camuffo et al. (2024, *SMJ* 45(6), 759 bedrijven over 4 RCT's, https://openaccess.city.ac.uk/id/eprint/32437/): een wetenschappelijke aanpak verhoogt de kans op één of twee radicale pivots en verlaagt zowel de kans op nul als op meer dan twee. Dat patroon hangt samen met betere performance. Startup Genome (2011) vond dezelfde vorm, maar met een veel zwakkere methode en een commercieel belang, dus leun op Camuffo.
- **Het scherpste bewijs voor kleine bedrijven pleit tegen tegelijk doen.** Meta-analyse van 5.488 mkb-bedrijven over 34 studies (Wenke, Zapkau & Schwens 2021, *JBR* 132:653-665): ambidexteriteit, dus exploreren en exploiteren tegelijk, hangt *minder* positief samen met performance dan exploreren alleen of exploiteren alleen. Bij kleine bedrijven is tegelijk-doen meetbaar slechter dan kiezen. Dit is het enige gevonden bewijs dat specifiek op bedrijfsgrootte snijdt, en het is het meest relevante voor een team van vier.
- **Te vroeg vastleggen is wel gemeten, te vroeg focussen niet.** Lee & Kim (2024, *SMJ* 45(9), 6,3 miljoen vacatures, 38.000+ startups): vroeg opschalen verhoogt de kans op falen zonder aantoonbaar voordeel bij exit, omdat je leren afkapt voordat je PMF hebt. March (1991) noemt de andere kant expliciet een faalmodus: te veel onontwikkelde ideeën en te weinig onderscheidend vermogen.
- **A/B-testonderzoek laat zien dat testen loont maar de staarten verbreedt.** Koning, Hasan & Chatterji (2022, *Management Science* 68(9), 35.262 startups): wie gaat A/B-testen presteert na een jaar 30 tot 100% beter, maar heeft zowel meer nulweken als meer topweken.
- **Het Bullseye-framework** uit *Traction* (Weinberg & Mares 2014), test drie kanalen parallel en focus daarna op de winnaar, is een boekframework met anekdotes. Geen dataset, geen peer review. Bruikbaar als denkraam, niet als bewijs.
- **Hormozi's doelgroep is een andere dan de onze.** Acquisition.com richt zich op bedrijven met ongeveer $1-10M EBITDA of $3-10M+ omzet (alleen op tertiaire bronnen gevonden, niet op acquisition.com zelf). Zijn advies is geschreven voor iemand met een draaiende motor die hij verstoort door eraan te sleutelen.

### De geschreven prioriteiten lopen achter
`Context/current-priorities.md` is voor het laatst bijgewerkt op 08-06-2026, ruim drie maanden geleden. Het noemt de Haagse Hogeschool-webinar van 23 juni nog als tijdgevoelig en zegt niets over UTI, Bath Spa of de internationale SHIFT-uitbreiding, de drie dingen waar nu het meeste geld en werk in zit. Er is dus geen actueel document dat zegt wat nummer een is.

## Deel 6 — De tegenspraak

Expliciet gezocht naar bewijs dat de focus-these onderuit haalt. Wat er is, en wat het waard is.

- **Survivorship bias is formeel aangetoond voor precies dit soort advies.** Denrell (2003, *Organization Science* 14(2), https://pubsonline.informs.org/doi/10.1287/orsc.14.2.227.15164) laat zien dat riskante en geconcentreerde middelenallocatie superieur *lijkt* in een steekproef van overlevers, ook als het in de volledige populatie niets met prestatie te maken heeft. Een YouTube-video van een geslaagde ondernemer is per definitie zo'n steekproef.
- **Parallel testen is soms wel optimaal**, en daar is een toetsbare regel voor in plaats van een mening: volledig parallel als de kosten per test laag zijn ten opzichte van de tijdskosten, serieel als tests duur zijn (Loch, Terwiesch & Thomke). Let op: het working paper uit 1999 zegt dat ruis parallel *aantrekkelijker* maakt, de gepubliceerde versie uit 2001 zegt het omgekeerde. Gebruik de gepubliceerde versie, en dan wijst ruis bij ons richting serieel.
- **Maar de tegenspraak slaat deels op zichzelf terug.** Barnett & Freeman (2001, *Organization Science* 12(5), https://doi.org/10.1287/orsc.12.5.539.10095) meten dat gelijktijdige introductie van meerdere producten de kans op marktuittreding met ruim 40% verhoogt. En Cao, Gedajlovic & Zhang (2009, *Organization Science* 20(4)) vinden dat juist middelen-arme bedrijven baat hebben bij *balans* tussen exploreren en exploiteren, niet bij meer van allebei.
- **Multi-channel outreach is geen goede tegenspraak.** Er is geen peer-reviewed of gerandomiseerd bewijs dat multi-channel koude outreach beter presteert dan één kanaal. Alles wat er is komt van outreach-leveranciers. Gong's "+130% winstkans bij meer contacten" (https://www.gong.io/win-rates) geeft geen steekproefgrootte en geen jaartal. Daartegenover meet CEB met n=3.000 (2015) dat de koopkans *daalt* naarmate de koopgroep groter wordt: 81% bij 1 stakeholder, 55% bij 2, 31% bij 6 of meer.
- **Theory of Constraints houdt als denkmodel maar half stand.** Trietsch (2005, *Human Systems Management* 24(1)) noemt het een bruikbare focusheuristiek maar "geen theorie en zeker niet verplicht", met een interne inconsistentie. Lawrence & Buss (1994, *POM* 3(1)) laten zien dat bottlenecks verschuiven, en dat gangbare managementreacties die verschuiving juist vergroten. Een bottleneck-aanpak van zes weken loopt reëel risico dat het knelpunt al verschoven is voor je klaar bent.
- **Waar iedereen het over eens is:** breed toetsen en daarna hard snoeien. Camuffo's RCT's vinden dat een wetenschappelijke aanpak leidt tot *meer* beëindigde ideeën en tot enkele in plaats van geen of herhaalde pivots. Het onderscheid dat telt is testen tegenover committen, niet breed tegenover smal.

---

## Conclusie

**1. Het mechanisme klopt, de cijfers niet.** Taakwisselkosten, attention residue en overload bij te veel gelijktijdige projecten zijn echt gemeten. De 20%-regel uit de video is zijn eigen vuistregel zonder enige onderbouwing, het TOC-bewijs komt van TOC-consultants zelf, en WIP-limieten zijn in de enige directe test niet eens productiviteitsverhogend. Neem het denkraam serieus, reken niet op de getallen.

**2. Het sterkste argument voor zijn punt geeft hij zelf niet.** Dat is de meta-analyse van 5.488 mkb-bedrijven (Wenke et al. 2021): bij kleine bedrijven hangt exploreren en exploiteren tegelijk *minder* positief samen met prestatie dan één van de twee kiezen. Plus Barnett & Freeman (2001): gelijktijdig meerdere dingen uitrollen verhoogt de uittredekans met ruim 40%. Voor een team van vier is dat het echte bewijs.

**3. Voor onze fase moet zijn advies op drie punten bijgesteld.**
- *Testen is niet committen.* Breedte hoort in het goedkoop toetsen, niet in het bouwen en uitrollen. Hormozi gooit die twee op één hoop.
- *Focus kan hier niet "minder mensen benaderen" betekenen.* Met een winrate van 19% en 4 tot 6 keer coverage heb je 20+ gekwalificeerde kansen nodig voor 4 closes. 45 benaderingen is onder elke aanname te weinig. Focus betekent: één segment, één kanaal, veel meer volume daarbinnen.
- *De feestjes-metafoor werkt niet in hoger onderwijs.* Zijn model leunt op kritieke massa en mond-tot-mondreclame binnen één groep. Onderwijsinkoop loopt via koopgroepen van 5 tot 16 mensen waarbij de koopkans juist *daalt* naarmate de groep groter wordt. Er is geen kritieke massa die je misloopt door meerdere accounts parallel te doen.

**4. Onze eigen diagnose is een andere dan die van de video.** Niet "vier feestjes tegelijk", maar:
- *Voorraad zonder doorstroom.* 340 onderzochte contacten, 88 geschreven berichten, 85 daarvan sinds 2 september onaangeraakt, 23 wachtend op een campagne die gestart moet worden. De machine bouwt sneller dan hij verstuurt.
- *De bovenkant is te smal, niet te breed.* Ongeveer 34 accounts per maand aangeraakt en 19 actieve opportunities, tegen 20+ benodigde kansen voor de kwartaaldoelen.
- *Geen attributie.* Zonder bronveld in Close is niet vast te stellen welk kanaal die 19 opportunities opleverde. Kiezen welk feestje je houdt is dan gokken.

**5. Waar de echte parallelle werkstromen zitten** is niet in de verkoop maar in het bouwen: blog-launch, sales-coach, website-building, app-homepage-redesign, landing-page-demo-survey, usability-test, design system. Dat is waar snoeien het minste kost en het meeste tijd vrijmaakt.

---

## Bronnen

**Primair (origineel onderzoek, peer reviewed)**
- Rubinstein, Meyer & Evans, *J. Exp. Psychol.: HPP* 27(4), 2001 — https://pubmed.ncbi.nlm.nih.gov/11518143/
- Leroy, *OBHDP* 109(2), 2009 — https://www.sciencedirect.com/science/article/abs/pii/S0749597809000399
- Mark, Gonzalez & Harris, CHI, 2005 — https://ics.uci.edu/~gmark/CHI2005.pdf
- Zika-Viktorsson, Sundström & Engwall, *IJPM* 24(5), 2006 — https://www.sciencedirect.com/science/article/abs/pii/S0263786306000329
- Loch, Terwiesch & Thomke, *Management Science* 47(5), 2001 — https://pubsonline.informs.org/doi/10.1287/mnsc.47.5.663.10480
- March, *Organization Science* 2(1), 1991 — http://www.iot.ntnu.no/innovation/norsi-pims-courses/Levinthal/March%20(1991).pdf
- Barnett & Freeman, *Organization Science* 12(5), 2001 — https://doi.org/10.1287/orsc.12.5.539.10095
- Denrell, *Organization Science* 14(2), 2003 — https://pubsonline.informs.org/doi/10.1287/orsc.14.2.227.15164
- Cao, Gedajlovic & Zhang, *Organization Science* 20(4), 2009 — https://pubsonline.informs.org/doi/abs/10.1287/orsc.1090.0426
- Lawrence & Buss, *POM* 3(1), 1994 — https://journals.sagepub.com/doi/10.1111/j.1937-5956.1994.tb00107.x
- Trietsch, *Human Systems Management* 24(1), 2005 — https://journals.sagepub.com/doi/10.3233/HSM-2005-24109
- Kerr, Nanda & Rhodes-Kropf, *JEP* 28(3), 2014 — https://www.nber.org/system/files/working_papers/w20358/w20358.pdf
- Ewens, Nanda & Rhodes-Kropf, *JFE* 128(3), 2018 — https://www.nber.org/system/files/working_papers/w24523/w24523.pdf
- Camuffo et al., *Management Science* 66(2), 2020 — https://doi.org/10.1287/mnsc.2018.3249
- Camuffo et al., *SMJ* 45(6), 2024 — https://openaccess.city.ac.uk/id/eprint/32437/
- Lee & Kim, *SMJ* 45(9), 2024 — https://doi.org/10.1002/smj.3596
- Koning, Hasan & Chatterji, *Management Science* 68(9), 2022 — https://dash.harvard.edu/server/api/core/bitstreams/8d40a8f4-ec5f-4dbf-8018-3d3d8be39a1a/content
- Wenke, Zapkau & Schwens, *JBR* 132, 2021 — https://ideas.repec.org/a/eee/jbrese/v132y2021icp653-665.html
- Junni et al., *AMP* 27(4), 2013 — https://journals.aom.org/doi/10.5465/amp.2012.0015
- ACM/IEEE ESEM, WIP in Kanban teams, 2018 — https://dl.acm.org/doi/10.1145/3239235.3239238
- Kohavi, KDD keynote, 2015 — https://exp-platform.com/Documents/2015-08OnlineControlledExperimentsKDDKeynoteNR.pdf
- Gartner B2B buyer survey (632 kopers, veldwerk 2024), 2025 — https://www.gartner.com/en/newsroom/press-releases/2025-05-07-gartner-sales-survey-finds-74-percent-of-b2b-buyer-teams-demonstrate-unhealthy-conflict-during-the-decision-process
- CEB, Challenger Customer learning lab (n=3.000), 2015 — https://smandh.com/wp-content/uploads/2017/08/virtual_learning_labs_november_12_15.pdf
- OED, priority — https://www.oed.com/dictionary/priority_n

**Secundair**
- Watson, Blackstone & Gardiner, *Journal of Operations Management*, 2007 — https://onlinelibrary.wiley.com/doi/abs/10.1016/j.jom.2006.04.004
- Grammarphobia over priority, 2016 — https://grammarphobia.com/blog/2016/09/priority.html
- Blank, search versus execute, 2012 — https://steveblank.com/2012/03/05/search-versus-execute/

**Tertiair (belanghebbend, met voorzichtigheid gebruikt)**
- Mabin & Balderstone TOC-review, TOC Institute, 1998 — https://www.tocinstitute.org/uploads/1/2/7/9/12796657/toc_impact_study.pdf
- Instantly cold email benchmark, 2026 — https://instantly.ai/cold-email-benchmark-report-2026
- Belkins reply rates, 2025 — https://belkins.io/blog/cold-email-response-rates
- Lemlist reply rates, 2026 — https://www.lemlist.com/blog/cold-email-response-rate
- Gradient Works B2B benchmarks, 2025 — https://www.gradient.works/blog/2025-b2b-sales-performance-benchmarks
- Tam to Target, higher-ed sales guide, 2025 — https://tamtotarget.com/higher-education-sales-guide/
- Litmus Partnership, tendercyclus UK, geraadpleegd 2026 — https://litmuspartnership.co.uk/the-tender-cycle-when-to-act-and-why-timing-matters/
- Startup Genome, premature scaling, 2011 — https://innovationfootprints.com/wp-content/uploads/2015/07/startup-genome-report-extra-on-premature-scaling.pdf (verkoper van de meettool, gebruik Lee & Kim in plaats hiervan)
- Samenvattingen van Hormozi's Scaling Workshop, 2024-2025 — https://dickiebush.substack.com/p/12-takeaways-from-alex-hormozis-scaling

## Wat ik niet hard kreeg

- **Geen enkele studie** meet het optimale aantal gelijktijdige werkstromen binnen één kleine startup. Alles gaat over portefeuilles, R&D-projecten in grote bedrijven, of individuele taakwisseling in een lab. Die brug legt niemand.
- **Geen niet-leveranciersbewijs** over de daling van koude-outreachrespons sinds AI-outreach normaal werd. Alle cijfers komen van partijen die outreachsoftware verkopen.
- **Geen peer-reviewed bewijs** dat multi-channel koude outreach beter werkt dan één kanaal.
- **Geen HE-specifiek cijfer** voor hoeveel benaderingen er nodig zijn per gesloten pilot van 4 tot 10k.
- **Intern:** geen bronveld in Close, LinkedIn-acceptaties niet bijgehouden (0 van 340 rijen gevuld), en de Lemlist-connector is niet gekoppeld, dus campagnecijfers ontbreken.
