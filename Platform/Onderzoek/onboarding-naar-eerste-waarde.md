# Van eerste contact naar het eerste waardemoment

Onderzoek 01-09-2026. Vier parallelle onderzoekslijnen: activatiepatronen in B2B SaaS, first-run-UX van AI-producten, onboarding en adoptie bij edtech, en het bewijs rond het verbergen tegenover het tonen van verplichte opzetstappen.

Aanleiding was het scherm voor een gloednieuw account, maar de kennis is breder bruikbaar: pilot-onboarding bij een instelling en landingspagina's lopen tegen dezelfde vragen aan. Zie onderaan.

---

## Het antwoord in zes punten

1. **De cijfers zijn genadeloos en dat is de reden om hier moeite in te steken.** Mediane dag-1-activatie in B2B SaaS ligt rond 5%, de top 10% haalt 21%. Bij de helft van alle producten is na twee weken meer dan 98% van de nieuwe gebruikers weg. En 69% van de producten die in de top zitten op week-1-activatie zitten ook in de top op drie-maands-retentie. Wat er in de eerste sessie gebeurt, bepaalt de rest. [Amplitude Product Benchmark Report](https://info.amplitude.com/rs/138-CDN-550/images/the-product-benchmark-report.pdf)

2. **Verbergen wat een beginner niet nodig heeft versnelt niet alleen, het verbetert ook zijn begrip.** Carroll en Carrithers blokkeerden functies voor nieuwe gebruikers van een tekstverwerker. Die groep leerde sneller, presteerde beter én scoorde hoger op een begripstest achteraf. De controlegroep besteedde bijna een kwart van de tijd aan het herstellen van fouten die in de vereenvoudigde versie niet konden ontstaan. [Training Wheels in a User Interface, CACM 1984](https://dl.acm.org/doi/10.1145/358198.358218)

3. **Maar volledig automatiseren kost je later.** Endsley en Kiris maten dat het out-of-the-loop-probleem groter is bij volledige automatisering dan bij tussenniveaus. Wie passief toekeek, kon het daarna zelf slechter. [Human Factors 1995](https://journals.sagepub.com/doi/10.1518/001872095779064555) Samen met punt 2 wijst dat niet naar verbergen en niet naar expliciet laten doen, maar naar **automatisch uitvoeren met een zichtbaar benoemde uitkomst en een omkeerbare actie**.

4. **Zelf moeite doen betaalt alleen als het lukt.** Het IKEA-effect is echt, maar de grens staat in hetzelfde artikel: het verdwijnt zodra de taak mislukt of niet wordt afgemaakt. Een opzetstap die iemand halverwege afbreekt levert geen binding op, die kost dubbel. [Norton, Mochon & Ariely, JCP 2012](https://myscp.onlinelibrary.wiley.com/doi/abs/10.1016/j.jcps.2011.08.002)

5. **Te snel klaar leest als oppervlakkig.** Bij een time-to-first-token van 2 seconden beoordeelden deelnemers de output als mínder doordacht en minder bruikbaar dan bij 9 tot 20 seconden. Wachttijd werd gelezen als nadenken. [Tan e.a., CHI 2026](https://arxiv.org/pdf/2604.06183) Generatietijd is dus geen probleem, mits je benoemt wat er gebeurt in plaats van een lege spinner te tonen.

6. **Docenten haken af op tijd, niet op interesse.** Bij 402 universitaire docenten voorspellen performance expectancy en effort expectancy de intentie, en facilitating conditions en habit het feitelijke gebruik. Kost de eerste keer moeite, dan komt er geen tweede. [Xu, Chen & Zhang 2024](https://journals.sagepub.com/doi/full/10.1177/21582440241290013)

---

## De patronen die producten gebruiken

**Container stil vooraf aanmaken.** Slack voegt iedereen automatisch toe aan `#general` ([Slack help](https://slack.com/help/articles/217626298-getting-started-for-workspace-creators)), Figma noemt elk nieuw bestand "Untitled" en laat je later hernoemen ([Figma help](https://help.figma.com/hc/en-us/articles/360038511473-Rename-files-and-projects)). Nul beslissingen vóór de waarde. Risico: blijft de container onzichtbaar, dan snapt de gebruiker het datamodel later niet.

**Demo-object naast het echte object.** Grammarly zet een demo-document op het dashboard, vol fouten, met hotspots die je langs de suggesties leiden ([Appcues GoodUX](https://goodux.appcues.com/blog/grammarlys-demo-document), teardown is enkele jaren oud). Trello's Welcome Board laat je de handeling zelf doen in plaats van toekijken ([Appcues GoodUX](https://goodux.appcues.com/blog/trellos-demo-kanban-board)).

**Eigen materiaal als eerste scherm.** Dit is het sterkste patroon voor ons soort product. Gamma opent op drie knoppen: *Generate*, *Paste in text*, *Import file*, en geen enkele stijl- of toonkeuze staat ervoor ([help.gamma.app](https://help.gamma.app/en/articles/7838093-how-do-i-create-a-new-presentation-document-or-webpage-in-gamma)). NotebookLM opent op "add sources" en je kunt niets anders tot er een bron in zit. Otter vraagt bij import niets en genereert meteen ([Otter help](https://help.otter.ai/hc/en-us/articles/360047733574-Import-an-audio-or-video-file)). Descript belooft in de docs een concrete verwachting: 30 minuten video meestal binnen vijf minuten ([Descript help](https://help.descript.com/hc/en-us/articles/33828899550989-Upload-a-file-from-your-computer)).

**Configuratie ná de eerste run.** Gamma houdt thema, toon en lengte weg uit de eerste stap en zet de bijstuur-affordance op het resultaat zelf. Risico: de eerste output is generiek en de gebruiker weet niet dat hij kan sturen. De reparatie is de knop op de output zetten, niet in een instellingenmenu.

**Configuratie afleiden en laten goedkeuren.** Gamma genereert eerst een outline die je mag bewerken voordat het deck gebouwd wordt. ChatGPT Deep Research toont een onderzoeksplan dat je mag aanpassen. MagicSchool positioneert zijn gegenereerde rubric expliciet als "editable starting point" ([MagicSchool](https://www.magicschool.ai/tools/rubric-generator)). De gebruiker kiest niets, maar keurt wel goed. Dat geeft eigenaarschap zonder invulwerk.

**Voortgang met een voorsprong.** Een kaart met twaalf vakjes waarvan er twee al zijn afgestempeld leidt tot snellere aankopen dan een kaart met tien lege vakjes, terwijl er in beide gevallen tien aankopen nodig zijn. [Kivetz, Urminsky & Zheng, JMR 2006](https://home.uchicago.edu/ourminsky/Goal-Gradient_Illusionary_Goal_Progress.pdf) Toepassing: doet het systeem stap 1 en 2 zelf, laat dan zien dat ze al afgevinkt zijn.

**Waarde vóór registratie.** Duolingo draait de eerste les vóór het account. Gina Gotthilf, destijds VP Growth, meldt ongeveer 20% meer DAU, en belangrijker: meerdere overslaanbare zachte muren vóór de harde muur, want zonder die zachte muren presteerden de harde significant slechter ([First Round Review](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker/)). Zelfrapportage van het bedrijf, geen gepubliceerde methodologie.

**De lege staat als les, niet als nepdata.** NN/g geeft drie richtlijnen: systeemstatus communiceren, leercues geven, en een directe route naar de kerntaak. Ze adviseren nergens om lege schermen met dummy-data te vullen. [Kaplan, NN/g 2021](https://www.nngroup.com/articles/empty-state-interface-design/)

---

## Wachttijd ontwerpen

De AI-generatie duurt tientallen seconden. Dat is een ontwerpprobleem met een verrassend goede bewijsbasis.

- 0,1 seconde voelt instant, 1 seconde houdt de gedachtegang intact, 10 seconden is de grens van de aandachtsspanne. [NN/g, Response Times](https://www.nngroup.com/articles/response-times-3-important-limits/)
- Boven 10 seconden hoort er een percent-done indicator met **tekstuitleg** ("3 van de 50"), een tijdsindicatie en een annuleeroptie. Gebruikers met een bewegende feedbackbalk wachtten gemiddeld drie keer zo lang. [NN/g, Progress Indicators](https://www.nngroup.com/articles/progress-indicators/)
- Een balk met achterwaarts bewegende, vertragende ribbels verkort de waargenomen duur met ongeveer 11%. [Harrison, Yeo & Hudson, CHI 2010](https://www.chrisharrison.net/projects/progressbars2/ProgressBarsHarrison.pdf) Balken die naar het einde toe versnellen worden als sneller ervaren. [Harrison e.a., UIST 2007](https://chrisharrison.net/projects/progressbars/ProgBarHarrison.pdf)
- Te snel is een probleem op zich, zie punt 5 hierboven.

**De praktische lijn:** vul de wachttijd met echte tussenstand ("criterium 2 van 5") in plaats van een spinner, en gebruik hem als het moment om te laten zien waarop de uitkomst gebaseerd wordt.

---

## Edtech: wie doet het hoe

**Cursus eerst, waarde later.** Gradescope, Turnitin Feedback Studio, FeedbackFruits en Packback vragen allemaal eerst structuur (cursus, roster, LTI-koppeling) voordat er iets zichtbaar wordt. Verdedigbaar bij een instellingsbrede uitrol met IT erbij, dodelijk bij een docent die zelf een account aanmaakt. [Gradescope: Creating a Course](https://guides.gradescope.com/hc/en-us/articles/22011729587597-Creating-Editing-and-Deleting-a-Course)

**Waarde eerst, structuur later of nooit.** MagicSchool geeft een gratis account in minuten zonder klas ([FAQ](https://www.magicschool.ai/faq)). Brisk is een Chrome-extensie die bovenop het Google Doc werkt dat de docent al open heeft, dus het eigen materiaal is er voordat het product er is ([Brisk help](https://help.briskteaching.com/hc/en-us/articles/38789769509524-Installing-the-Brisk-Chrome-extension)). Kahoot zet je meteen in de templatebibliotheek.

**Oefenomgevingen.** Quill heeft de scherpste vorm: een knop "Explore a demo teacher account" met demo-studenten en een banner dat wijzigingen niet bewaard worden ([Quill support](https://support.quill.org/en/articles/5837102-how-do-i-use-the-demo-account-when-i-sign-up-for-quill)). Moodle heeft Mount Orange (gevuld) en een lege Sandbox, allebei elk uur gereset. Canvas en Brightspace kennen "sandbox course" als vaste term, meestal aan te vragen per instelling.

**Let op deze correctie.** Gradescope had automatisch aangemaakte demo-cursussen met vooraf geladen roster en inzendingen, maar volgens hun eigen helppagina zijn dat **legacy** cursussen die alleen nog in oudere docentaccounts verschijnen. Een directe concurrent heeft dit patroon dus gehad en voor nieuwe accounts laten vallen. Waarom is niet gedocumenteerd. [Gradescope Guides](https://guides.gradescope.com/hc/en-us/articles/21589292998797-What-are-my-Gradescope-Demo-Courses)

**De rubric als blokkade of niet.** Turnitin Clarity (maart 2025) koppelt formatieve feedback aan de opdrachtinstructies én de rubric, dus die moet je hebben ([persbericht](https://www.turnitin.com/press/turnitin-launches-turnitin-clarity-bringing-transparency-and-integrity-insights-to-education)). Brisk draait het om met een losse rubric-generator, geen rubric nodig om te beginnen ([Brisk](https://www.briskteaching.com/ai-tools/rubric-generator)). KEATH vraagt de rubric expliciet op tijdens onboarding en traint op instellingsspecifieke criteria ([KEATH FAQ](https://keath.ai/faq)). Graide heeft geen rubric-upload als startpunt maar leert uit eerdere correcties ([Jisc](https://nationalcentreforai.jiscinvolve.org/wp/2023/06/14/national-centre-for-ai-graide-pilot-overview/)).

**Het UK-referentiekader.** Jisc draait sinds september 2025 een jaar lang een AI-in-assessment-pilot met precies drie nakijktools, Graide, KEATH en TeacherMatic, over acht instellingen. [Jisc](https://nationalcentreforai.jiscinvolve.org/wp/2025/05/14/ai-in-assessment-pilot/)

---

## Vertrouwen, en waarom dat een ontwerpvraag is

- **Identieke feedback wordt lager beoordeeld zodra er "AI" boven staat** dan wanneer er een mens boven staat. [Nazaretsky e.a., JCAL 2026](https://onlinelibrary.wiley.com/doi/10.1111/jcal.70153)
- De kernstudie over docentvertrouwen laat zien dat het hangt aan menselijke factoren en AI-specifieke misvattingen, en dat een gerichte interventie vertrouwen en bereidheid verhoogt. [Nazaretsky, Ariely, Cukurova & Alexandron, BJET 2022](https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13232)
- Reviewliteratuur noemt vier terugkerende bronnen van wantrouwen: ondoorzichtige besluitvorming waarbij docenten expliciet vragen om openheid over hoe de feedback tot stand komt, dataprivacy, bias, en de angst dat automatische feedback het gesprek vervangt. Wat vertrouwen wél opbouwt: uitlegbaarheid, en de eindbeslissing bij de docent. [Frontiers in Education 2025](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1704820/full)
- Studenten vinden docentfeedback betrouwbaarder maar AI-feedback toegankelijker en begrijpelijker. Complementair, niet concurrerend. [Assessment & Evaluation in Higher Education 2025](https://www.tandfonline.com/doi/full/10.1080/02602938.2025.2502582) (bron gaf 403 bij ophalen, cijfers niet geverifieerd)

**Drie ontwerphendels die hieruit volgen:** laat per feedbackpunt zien op welk criterium en welke passage het steunt, houd de docent-in-de-lus zichtbaar, en benoem zelf waar het model onzeker is in plaats van dat weg te poetsen.

---

## Institutionele context

- **Tijd is de blokkade, niet de interesse.** Jisc ondervroeg 462 stafleden: staf experimenteert vooruit op instellingsbeleid maar is grotendeels zelf-opgeleid, en slechts 44% van de FE- en 37% van de HE-instellingen leverde staf-ontwikkeling op AI. [Staff perceptions of AI 2025](https://nationalcentreforai.jiscinvolve.org/wp/2025/09/02/staff-perceptions-of-ai-2025/) (403 bij ophalen)
- **EDUCAUSE 2025**, bijna 800 respondenten: 57% noemt AI een strategische prioriteit, en docenttraining is het meest voorkomende element in AI-plannen, maar training is tijd- en resource-intensief. [2025 AI Landscape Study](https://www.educause.edu/content/2025/2025-educause-ai-landscape-study/introduction-and-key-findings)

---

## Waar de bronnen elkaar tegenspreken

- **Demo-data of niet.** Leveranciersblogs prijzen sample content aan als dé oplossing voor de lege staat. NN/g geeft een fundamenteel ander antwoord op hetzelfde probleem: leg uit en bied een pad, vul niet met nepdata. Er is geen gecontroleerd experiment dat de twee tegen elkaar zet.
- **Vragen stellen bij signup.** Amplitude beveelt rolvragen aan maar zegt erbij dat het progressief moet. Duolingo's bevinding wijst juist op alles vóór de waarde als kostenpost. Te verzoenen door pas ná het aha-moment te vragen, maar zo staat het in geen van beide bronnen.
- **Carroll tegen Endsley.** Weghalen wat de novice niet nodig heeft versterkt het begrip, tegenover: passief toekijken vermindert het vermogen om later zelf te handelen. Verzoening: Carroll blokkeerde functies die de gebruiker nooit wilde gebruiken, Endsley automatiseerde de kerntaak. Iets dat op termijn een kerntaak wordt, mag je niet permanent verbergen.
- **Eén scherm tegen meerdere stappen.** [Rodríguez e.a., JMIR Human Factors 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8190652/) (n=20, gecounterbalanceerd) vonden het eenpaginaformulier het beste op tevredenheid (SUS 76 tegen 67 en 57), snelheid en fouten (21 tegen 35 en 83), terwijl de onboardingliteratuur juist opsplitsen aanraadt.

## Gaten

- **Geen enkele A/B-test** waarin automatisch aangemaakte containers tegen handmatige setup zijn getest. Dat patroon rust volledig op observatie van producten.
- **Het IKEA-effect is nooit getest op software-setup**, alleen op fysieke objecten.
- **Geen bewijs over de docentpopulatie specifiek** in de onboardingliteratuur, terwijl die groep afwijkt: institutionele context, lage tolerantie voor rommel in accounts, gebruik per semester in plaats van dagelijks.
- **Vrijwel al het onboardingbewijs meet korte-termijnconversie**, niet gebruik in maand drie.
- **Geen cijfers over first-session drop-off bij AI-nakijktools.** Die bestaan wel, niemand publiceert ze.
- **Achter de login kon niet gekeken worden** bij Gradescope, Turnitin, KEATH, Graide, Packback en de meeste andere. Alles komt uit helpcentra en handleidingen, niet uit eigen waarneming.
- **Onbekend of "we hebben cursus X voor je gemaakt" wantrouwen wekt** bij een AI-nakijksysteem, waar wantrouwen al hoog is. Dat is een test waard, want geen literatuur dekt hem.

## Cijfers die je niet moet gebruiken

Niet terug te voeren op een origineel rapport met methodologie:

- **Alle "X formuliervelden = Y% conversie"-cijfers.** De meest genoemde bron is een HubSpot-blogpost uit een webinar rond 2011, met grafieken zonder dataset of methode. Latere "benchmarks" lezen percentages van die grafieken af.
- **Het Expedia-verhaal over één veld en 12 miljoen dollar.** Anekdote uit een presentatie, zonder gepubliceerde data, en het ging over een verwarrend label en niet over lengte.
- **"84% haakt af in de eerste sessie bij lege staten", "rol-flows verhogen activatie met 30 tot 50%", "78% haakt af bij stap 3 van een product tour", "90% churn bij geen gebruik in 3 dagen".** Statistiekenlijsten van onboardingleveranciers zonder traceerbare bron.
- **"Sked Social verdrievoudigde conversie met een checklist".** Vergelijkt voltooiers met niet-voltooiers, dat is een selectie-effect en geen test.
- Wat je **wel** mag gebruiken: de Amplitude-percentielen, met de kanttekening dat het exacte aantal deelnemende bedrijven niet uit het rapport zelf te halen is.

---

## Wat dit betekent, op drie plekken

### In het product
Eerste scherm is geen opzetformulier maar een plek om eigen materiaal neer te zetten. Verplichte tussenstappen worden stil uitgevoerd, en pas ná het waardemoment benoem je in één regel wat er is aangemaakt, met hernoemen en weggooien erbij. De wachttijd vul je met de afgeleide rubric, want dat is tegelijk voortgangsinformatie, transparantie over waar de feedback op steunt, en het eerste kalibratiemoment. De tweede keer krijgt de gebruiker de volledige flow, want begeleiding die een beginner helpt gaat een gevorderde in de weg zitten ([Kalyuga 2009](https://link.springer.com/article/10.1007/s11251-009-9102-0)).

### In pilot-onboarding
Dezelfde vraag, andere schaal. De eerste sessie met een docent in een pilot moet eindigen met feedback op werk dat hij herkent, niet met een ingerichte omgeving. Alles wat je vóór dat moment vraagt, is uitstel. Wat je daarna vraagt is meestal geen probleem, want dan is de waarde bewezen. Reken erop dat vertrouwen een apart spoor is: uitlegbaarheid, docent-in-de-lus, en zelf benoemen waar het model onzeker is.

### Op landingspagina's
Het product laten zien op echt werk, niet illustreren. De patronen hierboven zijn ook paginapatronen: eigen tekst laten plakken werkt op een landingspagina net zo goed als in een product. En de statistiekenlijst hierboven is een waarschuwing voor de eigen copy, want de meeste cijfers die in dit veld circuleren zijn onbruikbaar en bij navraag een blamage.

---

## Verwant

- `Platform/Onderzoek/ux-ui-design-expertwerkwijze.md` — wat een ontwerp goed maakt, en waar de vakliteratuur elkaar tegenspreekt.
- `Platform/Onderzoek/designkeuzes-bij-spanning.md` — kiezen als twee opties allebei verdedigbaar zijn, wat gewoontes doorbreken kost, en welke toets welke vraag beantwoordt.
- `Design/System/core/informatie.md` — de regels die uit dit werk zijn gedestilleerd, in toepasbare vorm.
