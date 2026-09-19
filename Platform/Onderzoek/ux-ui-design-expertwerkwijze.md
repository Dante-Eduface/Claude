# Hoe expert UX/UI designers zorgen dat een design goed is

Onderzoek 29-08-2026. Zeven parallelle onderzoekslijnen: visuele principes, werkwijze, klantvragen, validatie, tegenspraak, B2B SaaS-praktijk, shadcn/ui.

---

## Het antwoord in vijf punten

1. **Het verschil tussen amateuristisch en professioneel is bijna volledig systematisch, niet artistiek.** Wat een design "goed" laat ogen zijn consistente wiskundige relaties: een type-schaal op een ratio, spacing op een 8pt-familie, een vaste radius-schaal met de concentrische regel voor geneste hoeken, drie schaduwniveaus. Niet elke keuze opnieuw verzinnen is het hele mechanisme. Dit is aanleerbaar en afdwingbaar in tokens.

2. **Er is geen uniform expertproces, en de beste teams doen het tegenovergestelde van wat de vakliteratuur voorschrijft.** De standaardroute (lo-fi wireframes → hi-fi in Figma → handoff) staat tegenover hoe Linear en Vercel werken: Linear ontwerpt bovenop een screenshot van de live app met een bewust minimaal systeem, Rauno Freiberg (Vercel) slaat mockups vaak over en gaat direct in code. Wat wél universeel is: critique als vast ritueel met een tijdslimiet, en iteratie op basis van een expliciet doel.

3. **De klantvragen die er echt toe doen zijn niet de smaakvragen maar de scope- en succesvragen.** Alle bruikbare briefs vragen naar hetzelfde: wat moet dit bereiken, hoe meten we dat, voor wie, wie keurt goed, welke content bestaat er echt, en wat doen we expliciet níet. Dat laatste (Shape Up's "No-gos") is het meest onderschatte veld. Bij smaakvragen is de enige die werkt de negatieve met een waarom erbij: welke voorbeelden vind je slecht, en waarom precies.

4. **Mooi en bruikbaar zijn twee verschillende dingen, en de causaliteit loopt andersom dan iedereen aanneemt.** Tuch e.a. (2012, N=80) vonden geen effect van esthetiek op waargenomen bruikbaarheid, wel het omgekeerde: wat goed werkt wordt mooier gevonden. Esthetiek verandert wel hoe bruikbaar iets *voelt* en maskeert daarmee problemen in tests. Praktische gevolg: WCAG-contrast, Core Web Vitals en een usability-test zijn ondergrenzen die je afvinkt vóórdat een smaakdiscussie mag beginnen.

5. **Regels voorkomen lelijk, ze maken niet onderscheidend.** Websites zijn tussen 2010 en 2016 meetbaar meer op elkaar gaan lijken (layout-afstand -30%+, ~200.000 screenshots), oorzaak: gedeelde libraries en defaults. Dat is nu erger geworden door shadcn-defaults en AI-generatie. Onderscheid moet uit een andere laag komen: eigen beeldtaal, eigen woorden, en het echte product tonen.

---

## Waar de bronnen elkaar tegenspreken

**Prototypisch versus origineel.** Tuch e.a. (2012, Google-gefinancierd) vonden dat lage visuele complexiteit plus hoge prototypicaliteit wint bij de eerste indruk binnen 17-50ms. Silvennoinen e.a. (2025, N=108) vonden juist dat novelty aesthetic appeal sterker voorspelt dan typicality, vooral bij dienstensites. Mijn weging: het verschil zit in tijdsvenster. In de eerste halve seconde wint herkenbaarheid, bij bewuste beoordeling wint eigenheid. Voor een site die zowel snel moet landen als moet bijblijven: conventionele structuur, eigen invulling. Dat is precies wat Linear en Stripe doen.

**"5 gebruikers vindt 85% van de problemen."** Nielsen & Landauer (1993) is een wiskundig model met een aanname van 31% detectiekans per gebruiker. Spool & Schroeder (2001, 49 gebruikers, 4 productiesites) vonden dat de eerste 5 slechts ~35% vonden. Faulkner (2003, 60 gebruikers) vond gemiddeld 80% maar met uitschieters naar beneden tot 55%. Weging: bruikbaar als iteratieve stap, waardeloos als eindoordeel na één ronde.

**Design system: fundament of keurslijf.** Figma's eigen content verkoopt uitgebreide design systems; Linear zegt expliciet dat hun systeem bewust minimaal blijft. Weging: Linear heeft gelijk voor kleine teams. Het punt van een systeem is niet volledigheid maar dat je niet elke keer opnieuw kiest. Bouw componenten organisch, op het moment dat je iets voor de tweede keer nodig hebt.

**Data versus smaak.** Douglas Bowman verliet Google in 2009 omdat een team 41 blauwtinten liet testen en hij een randbreedte van 3, 4 of 5 pixels moest bewijzen. Daartegenover: bij Microsoft haalt slechts ~1 op de 3 goed doordachte experimenten de doelmetriek, bij Google en Bing 10-20%. Beide kanten hebben gelijk over de ander. Praktische lijn: test wat meetbaar is en veel oplevert (koppen, CTA's, paginastructuur), beslis de rest op vakmanschap zonder erover te vergaderen.

**De harde CRO-cijfers die rondgaan zijn onbetrouwbaar.** "202% betere CTA's", "+22% social proof", "3566% conversiestijging": geen van deze was terug te voeren op een origineel testrapport met methodologie. Ze circuleren tussen bureaus die redesigns verkopen. Niet gebruiken.

**De redesign-rampen bewijzen niet wat men denkt.** M&S verloor 8,1% online omzet na een redesign van ~£150M (2014); Sonos verloor ~$100M omzet en zijn CEO na de app-redesign (2024-25). In beide gevallen waren de klachten functioneel (kapotte checkout, verdwenen functies), niet esthetisch. Ze bewijzen dat een redesign zonder gedragsvalidatie duur is, niet dat schoonheid schaadt.

---

## De concrete regels die overeind bleven

Verwerkt in `Design/Design system/core/regels.md`. De belangrijkste, met bron:

- **Contrast:** 4.5:1 normale tekst, 3:1 grote tekst. [WCAG 2.2, W3C, 2023](https://www.w3.org/TR/WCAG22/). Enige regel hier met normatieve status.
- **Regellengte:** 45-90 tekens. [Butterick, Practical Typography](https://practicaltypography.com/line-length.html). Refactoring UI zegt 60-80; overlappende banden, beide vakmeningen zonder experimenteel bewijs.
- **Max 2 fonts, max 2-3 groottes of gewichten per scherm.** [Hobday, Visual design rules, 2023](https://anthonyhobday.com/sideprojects/saferules/) en [NN/g, 2020](https://www.nngroup.com/articles/principles-visual-design/).
- **Verlaag nooit contrast om te de-emphasizen.** NN/g, 2020.
- **Geen puur zwart of wit; grijzen licht verzadigen (<5%).** Hobday, 2023.
- **Geneste radius:** binnen = buiten min de tussenruimte, anders lopen de bogen niet parallel. Formule en CSS in `core/regels.md`.
- **Overshoot:** ronde vormen moeten iets groter dan vierkante om optisch gelijk te ogen. Geldt voor letters en voor UI-vormen.
- **8pt-grid:** breed geadopteerd (Material, Carbon, Apple), maar let op: ik vond hier géén empirische onderbouwing voor, en ook géén serieuze kritiek. Het is een coördinatieconventie, geen wet. Dat is genoeg reden om hem te volgen.

---

## De vragenlijst voor een briefing

De set die na het schrappen van overlap overbleef. Bronnen: [NN/g Stakeholder Interviews, 2022](https://www.nngroup.com/articles/stakeholder-interviews/), [Shape Up hfst. 6, Singer 2019](https://basecamp.com/shapeup/1.5-chapter-06), JTBD switch-interviews, en de overlap van bureau-questionnaires.

**Doel en succes**
- Wat is het primaire doel van dit ding, in één zin?
- Welke actie moet iemand ondernemen?
- Hoe ziet succes eruit over zes maanden? Welke metriek?
- Waarom bouwen we dit nu? Wat werkt er niet aan het huidige?

**Doelgroep**
- Voor wie is dit primair? Is er een secundaire groep, en hoe anders zijn hun behoeften?
- Welk probleem proberen ze op te lossen als ze hier komen?
- Wat gebruiken ze nu? Wat ging daaraan mis? Wanneer dachten ze "zo kan het niet langer"?

**Merk en smaak**
- Noem drie voorbeelden die je goed vindt, en zeg per stuk waarom.
- Noem twee die je slecht vindt, en zeg waarom. *Deze levert meer op dan de vorige.*
- Welke drie woorden beschrijven hoe het moet voelen?
- Zijn er kleuren, stijlen of elementen die absoluut niet mogen?

**Scope en beslissing**
- Wat bouwen we expliciet níet? (No-gos)
- Hoeveel tijd is hiervoor, en wat betekent dat voor de oplossing? *Tijd begrenst de oplossing, niet andersom.*
- Wie is aanspreekpunt en wie keurt uiteindelijk goed?
- Wat is het budget, en ligt dat vast?

**Content**
- Wie levert de teksten, en wanneer?
- Welke beelden, video of assets bestaan er al echt?
- Welke integraties of systemen moeten erin?

**De techniek achter de vragen.** Bij vage feedback ("het voelt niet lekker") is de sterkste bron, NN/g's Rachel Krause (2021), expliciet dat er géén vraagtruc bestaat. Wat wel werkt: vooraf afspreken waarop je feedback wilt, en binnengekomen feedback achteraf sorteren in *to do* / *to persuade* / *to clarify*. Krause verklaart vaagheid uit vocabulaireverschil: wat een designer als regelafstand ziet, noemt een ander "rommelig". Monteiro's regel is de conversie: de vraag is niet "vind ik dit mooi" maar "haalt dit ons doel".

**Let op:** "wat is het ergste dat kan gebeuren" is geen designvakregel. De enige onderbouwing is Klein's premortem ([HBR, 2007](https://hbr.org/2007/09/performing-a-project-premortem)), die claimt dat vooruitblikkende hindsight het correct benoemen van oorzaken met 30% verhoogt. Geleende techniek, prima bruikbaar, maar niet presenteren als designstandaard.

**Tegengeluid dat blijft staan:** een deel van de top verwerpt het brief-als-formulier. Yves Béhar: "I don't believe in briefs. I believe in relationships." David Rockwell: als student is de brief God, later is het je taak hem te bevragen ([AIGA Eye on Design, 2014](https://eyeondesign.aiga.org/famous-creatives-on-how-to-write-the-perfect-design-brief/)). Relevant als je ooit een designer inhuurt: iemand die je brief bevraagt is niet lastig.

---

## Wat dit betekent voor Eduface

Het bestaande design system was al goed op de laag die telt (tokens, één accentkleur, twee fonts, 8pt). Wat ontbrak is de laag daarboven: het systeem was impliciet een websysteem, terwijl er ook slides en interne tools uit moeten komen. Dat is nu gesplitst in `core/` plus drie oppervlakken, zodat een type-schaal een keuze over kijkafstand wordt in plaats van een merkkeuze, en zodat een taak nooit de verkeerde context meesleept.

Het scherpste openstaande punt is niet craft maar onderscheid. De hele B2B SaaS-referentiegroep (Linear, Stripe, Vercel, Attio) verschilt onderling op elk punt waarvan men aanneemt dat het een formule is: aantal CTA's (1 tot 3), productvisualisatie (screenshot, video, of helemaal geen product zoals bij Stripe), licht versus donker. Er is geen winnende anatomie. Wat ze delen is typografische discipline, weinig kleur, en dat ze het product zelf tonen in plaats van beschrijven. Voor Eduface betekent dat: het product laten zien (feedback op een echt stuk werk van een student), niet illustreren.

---

## Gaten

- **8pt-grid heeft geen empirische basis** die ik kon vinden, en ook geen serieuze kritiek. Zoektermen: "8pt grid research evidence", "8pt grid criticism cargo cult". Behandel als conventie.
- **Geen enkele studie koppelt design-system-gebruik aan slechtere uitkomsten.** De "design systems doden creativiteit"-literatuur is volledig meningsstuk, geschreven door mensen die boeken of diensten verkopen. De enige harde meting (Goree 2021) toont convergentie aan maar oordeelt er niet over.
- **Geen gemeten studie naar visuele uniformiteit van AI-gegenereerde interfaces.** Wel gemeten voor tekst en ideeën (Anderson e.a., C&C 2024). De extrapolatie naar UI is inferentie, geen bevinding.
- **Geen EdTech-specifiek designonderzoek gevonden.** De vergelijkingsbasis blijft generiek B2B SaaS. Zoekterm: "higher education SaaS website design conversion demo request university".
- **Geen onafhankelijke A/B-data voor Linear, Stripe, Vercel of Attio.** Hun makers beschrijven hun keuzes expliciet als ongemeten "taste en craft" (Freiberg, Saarinen). Er is dus geen natrekbare causale keten tussen die stijl en conversie.
- **Enkele veelgeciteerde cijfers bleken niet natrekbaar:** Bailey & Wolfson's "87% first-click", de 202%/22%/68% CRO-cijfers, en het "$500M marktwaarde"-cijfer bij Sonos. Niet gebruiken.
- **Paywalled, niet volledig gelezen:** Tuch e.a. 2012 (Computers in Human Behavior) en Silvennoinen 2025 (IJHCI). Bevindingen komen uit abstracts en onafhankelijke samenvattingen.

---

## Bronnen

**Primair (origineel onderzoek, normatieve documenten, makers zelf)**
- [WCAG 2.2, W3C, 2023](https://www.w3.org/TR/WCAG22/)
- [Nielsen & Molich, Heuristic evaluation of user interfaces, CHI 1990](https://dl.acm.org/doi/10.1145/97243.97281)
- [Spool & Schroeder, Five users is nowhere near enough, CHI 2001](https://dl.acm.org/citation.cfm?id=634236)
- [Faulkner, Beyond the five-user assumption, Behavior Research Methods 35, 2003](https://link.springer.com/article/10.3758/BF03195514)
- [Tractinsky, Katz & Ikar, What is beautiful is usable, Interacting with Computers 13, 2000](https://www.ise.bgu.ac.il/faculty/noam/papers/00_nt_ask_di_iwc.pdf)
- [Tractinsky, Aesthetics and apparent usability, CHI 1997](https://dl.acm.org/doi/10.1145/258549.258626)
- [Lindgaard e.a., 50 milliseconds to make a good first impression, Behaviour & IT 25(2), 2006](https://doi.org/10.1080/01449290500330448)
- [Tuch e.a., Visual complexity and prototypicality, IJHCS 70(11), 2012](https://research.google/pubs/the-role-of-visual-complexity-and-prototypicality-regarding-first-impression-of-websites-working-towards-understanding-aesthetic-judgments/) — mede door Google gefinancierd
- Silvennoinen, Kotkajuuri & Kujala, IJHCI, 2025, doi 10.1080/10447318.2025.2576633 — paywalled
- [Goree e.a., Investigating the homogenization of web design, CHI 2021](https://dl.acm.org/doi/10.1145/3411764.3445156)
- [Reinecke & Gajos, Quantifying visual preferences around the world, CHI 2014](https://dl.acm.org/doi/10.1145/2556288.2557052)
- [Roth e.a., Design thinking and project performance, Creativity and Innovation Management, 2020](https://onlinelibrary.wiley.com/doi/full/10.1111/caim.12408)
- [Naini, The golden ratio myth, Maxillofacial Plastic and Reconstructive Surgery, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC10792139/)
- [Klein, Performing a Project Premortem, HBR, 2007](https://hbr.org/2007/09/performing-a-project-premortem)
- [Singer, Shape Up hfst. 6 (Write the Pitch), 2019](https://basecamp.com/shapeup/1.5-chapter-06)
- [Figma, Design critiques at Figma](https://www.figma.com/blog/design-critiques-at-figma/)
- [Karri Saarinen over Linear's designproces, okt 2023](https://x.com/karrisaarinen/status/1715085201653805116)
- [Freiberg, Invisible Details of Interaction Design, 2023](https://every.to/p/invisible-details-of-interaction-design)
- [Bowman, Goodbye Google, 2009](https://stopdesign.com/journal/2009/03/20/goodbye-google.html)
- [Kohavi e.a., Online controlled experiments, KDD keynote 2015](https://exp-platform.com/Documents/2015-08OnlineControlledExperimentsKDDKeynoteNR.pdf)
- [Gronier, Testing the validity of the 5 second test, JUS 12(1), 2016](https://www.guillaumegronier.com/resources/2016_JUS_Gronier.pdf)
- shadcn/ui: [LICENSE 2023](https://github.com/shadcn-ui/ui/blob/main/LICENSE.md), [theming](https://ui.shadcn.com/docs/theming), [components.json](https://ui.shadcn.com/docs/components-json), [MCP](https://ui.shadcn.com/docs/mcp), [Base UI default, 2026](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default), [Tailwind v4, 2025](https://ui.shadcn.com/docs/changelog/2025-02-tailwind-v4)
- Live sites gefetcht 29-08-2026: linear.app, stripe.com, vercel.com, attio.com, retool.com

**Secundair (onafhankelijke analyse, vakpers)**
- [NN/g, Stakeholder Interviews 101, Gibbons, 2022](https://www.nngroup.com/articles/stakeholder-interviews/)
- [NN/g, Principles of Visual Design, 2020](https://www.nngroup.com/articles/principles-visual-design/)
- [NN/g, Derailed Design Critiques, Krause, 2021](https://www.nngroup.com/articles/derailed-design-critiques/)
- [NN/g, Aesthetic-Usability Effect, Moran, 2024](https://www.nngroup.com/articles/aesthetic-usability-effect/)
- [UXPA Magazine over de validiteit van Nielsens heuristieken](http://uxpamagazine.org/nielsens-heuristic-evaluation/)
- [Connor & Irizarry, Discussing Design, UIE-seminar 2012](https://archive.uie.com/brainsparks/2012/07/13/adam-connor-aaron-irizarry-discussing-design-the-art-of-critique/)
- [Monteiro, Design Is a Job, hoofdstuk Managing Feedback (UXmatters, 2019)](https://www.uxmatters.com/mt/Archive/2019/12/sample-chapter-design-is-a-job.php)
- [AIGA Eye on Design, Famous creatives on the design brief, 2014](https://eyeondesign.aiga.org/famous-creatives-on-how-to-write-the-perfect-design-brief/)
- [Brownlee, The golden ratio: design's biggest myth, Fast Company 2015](https://web.archive.org/web/20251006173630/https://www.fastcompany.com/3044877/the-golden-ratio-designs-biggest-myth)
- [Econsultancy over de M&S-relaunch, 2014](https://econsultancy.com/where-did-the-marks-spencer-website-relaunch-go-wrong/)
- [Fast Company over Sonos' CEO-vertrek na de app-redesign, 2025](https://www.fastcompany.com/91259432/sonos-ceo-steps-down-following-a-disastrous-app-redesign)
- [Rauno Freiberg interview, ui.land](https://ui.land/interviews/rauno-freiberg)
- [Saarinen interview, Lenny's Newsletter](https://www.lennysnewsletter.com/p/inside-linear-building-with-taste)

**Tertiair (blogs, vendorcontent, praktijkregels zonder onderzoek)**
- [Hobday, Visual design rules you can safely follow every time, 2023](https://anthonyhobday.com/sideprojects/saferules/)
- [Butterick, Practical Typography, line length](https://practicaltypography.com/line-length.html)
- [Apple Human Interface Guidelines, typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [Material Design elevation](https://m1.material.io/material-design/elevation-shadows.html) en [IBM Carbon spacing](https://carbondesignsystem.com/elements/spacing/overview/)
- Refactoring UI (Wathan & Schoger, 2018)
- [De concentrische border-radius-regel, dev.to 2026](https://dev.to/sgbp/the-concentric-border-radius-rule-why-nested-rounded-corners-look-slightly-wrong-3hog)
- [Kennedy, The Reframe Technique, 2017](https://www.learnui.design/blog/the-reframe-technique.html)
- [Tweakcn, visuele theme-editor voor shadcn](https://tweakcn.com/)
- Bureau-questionnaires: [Ybug 2026](https://ybug.io/blog/web-design-client-questionnaire), [Content Snare 2026](https://contentsnare.com/graphic-design-questionnaire/), [GoDaddy 2024](https://www.godaddy.com/resources/skills/the-ultimate-web-design-client-questionnaire)
- [Natasha Jen, Design Thinking is Bullshit (Core77-verslag, 2017)](https://www.core77.com/posts/68499/Natasha-Jens-Design-Thinking-is-Bullshit-Argument) en [Iskander, HBR 2018](https://hbr.org/2018/09/design-thinking-is-fundamentally-conservative-and-preserves-the-status-quo)

**Geblokkeerd, niet kunnen lezen:** aiga.org (Cloudflare), 99designs, uxdesign.cc, CXL, Marketing Week (alle 403).
