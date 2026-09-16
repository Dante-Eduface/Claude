# Onderzoek: hoe toon je het product, en toon je de beta's

Datum 11-09-2026. Stand: snel (3 subagents, één ronde, geen gatenronde want geen onderlinge tegenspraak). Vraag van Dante: hoe laat je een product het best zien op de demo-landingspagina, en moeten de twee beta's (Academic Integrity, Oral Examination) erop.

Labels: [P] primair, [S] secundair, [T] tertiair/vendor.

## Antwoord

1. **Toon het echte product, gecropt op het moment dat de belofte bewijst.** Er bestaat geen onafhankelijke A/B-test die screenshot, gestileerde UI, interactieve demo, video en illustratie tegen elkaar zet. Wat wél overeind blijft: NN/g vindt dat alleen beelden met taakrelevante informatie bekeken en onthouden worden, decoratieve beelden worden genegeerd of schaden. Een product-UI die het mechanisme laat zien (voorstel per criterium, "needs you", Approve) is informatief. Een illustratie van een robot is decoratief.
2. **Niet het volledige scherm.** Cluttered UI bij koud verkeer wekt twijfel, en NN/g waarschuwt dat grote beelden de kernfunctie verdringen. Dus: uitvergrote fragmenten (rubric-paneel, één comment met Approve/Edit, de batch-teller), geen dashboard-screenshot met twintig knoppen. Dat is precies wat de v4-wireframe doet.
3. **Interactieve demo en video: alleen vendor-cijfers, dus niet als argument gebruiken.** Navattic (+20 tot 25% conversie), Walnut (+81%), Wistia (16% CTA-conversie) verkopen allemaal het formaat dat ze meten. Eén onafhankelijke CRO-bron zegt dat video-hero's sinds begin jaren 2020 niet meer automatisch winnen. Conclusie: statische gecropte UI in de hero is de laagste-risico-keuze. Een korte productvideo of interactieve demo is een tweede test, niet de basis.
4. **De beta's tonen: ja, klein, eerlijk gelabeld, en zonder de pagina erop te bouwen.** Vrijwel elke SaaS toont beta's publiek met een "Beta"-badge naast de naam. Er is geen data dat het conversie kost of oplevert. Wél twee redenen om ze klein te houden: (a) het enige gevonden ho-geval van een AI-gradingfunctie die "niet volwassen" aanvoelde (Montclair State, Canvas, 2026) eindigde in een advies om te stoppen; (b) AI die leeruitkomsten beoordeelt is hoog-risico onder de AI Act, dus een inkoper leest "beta" als "nog geen conformiteitsbeoordeling".
5. **Dus voor Eduface:** twee live producten groot, met gecropte product-UI en de docent-keurt-goed-stap in beeld. De twee beta's als twee kleine cellen met badge "Beta", één zin wat het doet, geen productbeeld, geen belofte over wanneer. Ze staan er zodat een opleiding met veel mondeling niet afhaakt, niet om te verkopen.

## Waar bronnen elkaar tegenspreken

- **Vendors vs. onafhankelijk.** Navattic, Walnut, Wistia, Vidyard: grote lifts voor hun eigen formaat. CXL (onafhankelijk): "geen enkel hero-type wint universeel". Ik weeg CXL en NN/g zwaarder. Vendorcijfers zijn richting, geen bewijs.
- **Beta-label.** Product Marketing Alliance: eerlijk zeggen wat iets niet doet bouwt vertrouwen. Emilie Schario (opinie): het label zelf is een "uncertainty tax" die adoptie remt. Beide zonder data. Voor een demopagina (niet een adoptiepagina) weegt eerlijkheid zwaarder: de inkoper vindt het toch.
- **Kannibalisatie door interactieve demo.** De aanname dat mensen de demo bekijken en dan niet boeken is nergens onafhankelijk gedocumenteerd. Alleen Walnut spreekt het tegen, en die heeft belang. Onbeslist.

## Wat dit betekent voor de wireframe

- Hero: gecropte product-UI met de drie vlakken (submission 1, submission 140, batch) blijft. Geen volledig dashboard.
- Sectie 5 (producten): Paper Grader en Exam Grader als volle rijen met een uitvergroot UI-fragment per product, elk met de goedkeurstap zichtbaar. Academic Integrity en Oral Examination als twee kleine cellen met "Beta"-badge, geen beeld.
- Sectie 4 (how it works): de drie UI-crops per stap zijn precies het NN/g-type "informatief beeld". Houden.
- Later te testen, niet nu: een video van 30 tot 60 seconden (Wistia: engagement piekt daar) als tweede hero-variant.

## Gaten

- Geen onafhankelijke A/B-test tussen de vijf formaten. Alleen via eigen meting te sluiten.
- Geen kwantitatief effect van een beta-badge op demo-aanvragen. Idem.
- Concurrenten (CoGrader, Kami, Graide, FeedbackFruits, Brisk): geen beta-labels gevonden op hun sites, en niet vastgesteld hoe zij hun productbeelden opzetten. Turnitin/Gradescope zetten "coming soon" in blog en changelog, niet op de productpagina.
- Jisc: niets gevonden over beta-features als inkooprisico. Wel algemeen: DPIA-documentatie moet de vendor kunnen leveren, ongeacht productstatus.
- Twee bronnen gaven 403 (Chronicle "Jagged Intelligence" 28-07-2026, Jisc AI-marking pilot 11-12-2025): alleen op snippet gelezen.

## Bronnen

**Primair / onafhankelijk onderzoek**
- NN/g, Image-Focused Design: https://www.nngroup.com/articles/image-focused-design/ (doorlopend bijgewerkt)
- NN/g, Why No Graphics / eyetracking: https://www.nngroup.com/articles/why-no-graphics/
- Jakob Nielsen over fotografie en geloofwaardigheid: https://jakobnielsenphd.substack.com/p/photography
- GitLab issue over Beta-badge in de UI: https://gitlab.com/gitlab-org/gitlab/-/issues/409874
- ScienceDirect, AI Act en GDPR in onderwijs (2026): https://www.sciencedirect.com/science/article/pii/S2212473X26000581

**Secundair**
- CXL, hero image guide: https://cxl.com/blog/hero-image/ (403 bij openen, claim via samenvattende bron)
- Chronicle of Higher Education, Jagged Intelligence, Montclair State Canvas AI-grading pilot (28-07-2026, 403, alleen snippet)
- Fibr, A/B-testvoorbeelden (Groove 2,3% naar 4,3%): https://fibr.ai/ab-testing/ab-testing-examples
- TechTarget, Vaporware explained: https://www.techtarget.com/searchcio/feature/Vaporware-explained-What-CIOs-need-to-know

**Tertiair / vendor**
- Navattic, State of the Interactive Product Demo 2025: https://www.navattic.com/report/state-of-the-interactive-product-demo-2025
- Walnut, interactive demos conversion 2026: https://www.walnut.io/blog/product-demos/interactive-demos-conversion-rates-b2b-2026-data/
- Wistia, video marketing statistics 2025/2026: https://wistia.com/learn/marketing/video-marketing-statistics
- Vidyard, video CTA case: https://www.vidyard.com/blog/video-call-to-action/
- spell.sh, hero section best practices (mening, geen data): https://spell.sh/blog/hero-section-best-practices
- Attio changelog "(Beta)": https://attio.com/changelog/meeting-and-call-recording-apis-beta
- Vercel changelog "public beta": https://vercel.com/changelog/vercel-flags-is-now-in-public-beta
- Loom roadmap/beta: https://www.loom.com/community/product-roadmap
- Figma, features in beta: https://forum.figma.com/product-updates-3/what-figma-features-are-in-beta-32882
- Emilie Schario, Stop shipping beta features: https://emilie.substack.com/p/stop-shipping-beta-features
- Product Marketing Alliance, AI feature launches: https://www.productmarketingalliance.com/what-b2b-marketers-get-wrong-about-ai-feature-launches/
- Turnitin blog, Gradescope features and what's to come (2025): https://www.turnitin.com/blog/the-latest-innovative-gradescope-features-and-a-look-ahead-at-whats-to-come
- EU AI Compass, AI Act for education: https://euaicompass.com/eu-ai-act-for-education.html
- FeedbackFruits, AI Act en edtech: https://feedbackfruits.com/blog/from-regulation-to-innovation-what-the-eu-ai-act-means-for-edtech
- Pixaura, landing pages voor koud verkeer: https://www.pixaura.com/designing-landing-pages-that-convert-cold-traffic/
