# Hoe je kiest als twee designopties allebei verdedigbaar zijn

Onderzoek 03-09-2026. Drie parallelle onderzoekslijnen: het bewijs rond gewoontes en change aversion, de bestaande afwegingskaders, en het goedkoop verkleinen van onzekerheid plus uitrollen naar bestaande gebruikers.

Aanleiding: de spanning tussen een interface waar bestaande gebruikers aan gewend zijn en een aanpak die cognitief beter onderbouwd is maar afwijkt.

---

## Het antwoord in vijf punten

1. **Vrijwel elke beroemde "gebruikers haten verandering"-case is een kapotte functie, geen gewenningsprobleem.** Sonos verloor alarmen, sleep timers en wachtrijbeheer. M&S dwong 2,8 miljoen klanten tot herregistratie en zag de online omzet 8,1% dalen. Dat zijn muren, geen leercurves. Voordat je de omschakelkosten als argument accepteert, splits je de klacht: is iets stuk, of is iets onbekend. Die vraag beslist bijna de hele discussie.

2. **Voor nieuwe gebruikers is de prijs van afwijken in het enige goede directe experiment nul.** Scarr, Cockburn, Gutwin & Bunt (CHI 2012) zetten een vlakke, afwijkende commandokaart tegenover Microsofts Ribbon. Ervaren gebruikers waren 25% sneller (1,57 s tegen 2,11 s) met 0,6% fouten tegen 5%. Novicen: 4,45 s tegen 4,38 s, geen significant verschil. Het cognitief sterkere ontwerp kostte beginners niets. De omschakelprijs valt op bestaande gebruikers, niet op nieuwe.

3. **Het gevaarlijkste ontwerp is het bijna-gelijke.** Woltz, Gardner & Bell (2000) vonden dat méér training tot een hógere foutkans leidde wanneer nieuwe sequenties leken op geoefende. Die fouten werden even snel uitgevoerd als correcte responses en bleven onopgemerkt. Kies dus: houd het hetzelfde, of maak het duidelijk anders. Het midden is de slechtste plek.

4. **Er bestaat geen formule die de cognitieve winst tegen de omschakelkosten weegt.** Het dichtstbijzijnde is Budiu (NN/g 2016) met drie vragen, geen model met parameters. Niemand heeft frequentie van gebruik, aantal getroffen gebruikers en leerbaarheid in een gevalideerde formule gebracht. Wie zo'n formule laat zien, heeft hem zelf bedacht.

5. **Van de negen bestaande afwegingskaders houden er twee stand.** De omkeerbaarheidstoets (hoe zwaar moet ik hier over nadenken) en de criteria-vooraf-regel (waarop beoordeel ik, en scoor ik voordat er gepraat wordt). De rest is bruikbaar als checklist en waardeloos als bewijs.

---

## Wat het bewijs zegt over gewoontes

**Change aversion is een begrip zonder cijfers.** Sedley & Müller, [Minimizing Change Aversion for the Google Drive Launch](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41221.pdf), CHI 2013 Extended Abstracts. Definitie: ongemak wanneer iets bekends wordt vervangen door iets onbekends. Vier pagina's, geen N, geen effectgrootte, geen duur. De conclusie "significantly more positive" is niet onderbouwd. Dit is de meest geciteerde bron over het onderwerp en het is een anekdote met een literatuurlijst. Bruikbaar is alleen hun figuur met zeven mogelijke verlopen, van volgehouden verrukking tot aversie zonder herstel. Een tekening, geen meting.

**Hoe lang de dip duurt: één echte meting.** Santa-Maria & Dyson, [The Effect of Violating Visual Conventions of a Website on User Performance and Disorientation](https://dl.acm.org/doi/10.1145/1456536.1456547), ACM SIGDOC 2008, N=28. Aanvankelijk slechter presteren en meer desoriëntatie bij het conventieschendende ontwerp, maar het verschil verdween al binnen deel 1 en was in deel 2 volledig weg. Kleine steekproef, één site, maar het is het beste directe bewijs dat conventiekosten snel verdampen.

**De cue verslaat de voorkeur.** Neal, Wood, Wu & Kurlander, [PSPB 2011](https://journals.sagepub.com/doi/abs/10.1177/0146167211419863): bioscoopbezoekers met een sterke popcorngewoonte aten evenveel oude als verse popcorn. Alleen buiten die context, of etend met de niet-dominante hand, verdween het. Een geautomatiseerde route wordt door de omgeving getriggerd, niet door een oordeel. Dat is precies waarom "maar ze vinden het nieuwe mooier" niet voorspelt wat ze doen.

**De leercurve vlakt sneller af dan het klassieke verhaal.** Newell & Rosenbloom (1981) claimden een machtsverband tussen oefening en tijd. Heathcote, Brown & Mewhort, [The Power Law Repealed](https://link.springer.com/article/10.3758/BF03212979), Psychonomic Bulletin & Review 2000, herfitten 40 datasets, 7.910 leerreeksen, 475 proefpersonen: de exponentiële functie won in álle niet-gemiddelde datasets. Middelen over personen creëert de machtsvorm kunstmatig. Individuele leercurves vlakken dus sneller af, wat pleit vóór doorpakken bij een echte verbetering.

**Hoeveel herhalingen een nieuwe route kost voordat hij weer automatisch is: onbekend.** Geen enkele traceerbare studie meet dit voor interfaces. Logan (1988) definieert automatisme als geheugenophaling zonder een vast herhalingsgetal. Elk specifieker cijfer dat je tegenkomt is verzonnen.

## Consistentie als regel, en de grenzen

**Jakob's Law is een assertie.** Nielsen, [End of Web Design](https://www.nngroup.com/articles/end-of-web-design/), NN/g 2000: gebruikers besteden de meeste tijd op andere sites. Geen studie, geen steekproef. De rondzingende bewering dat afwijken je "ongeveer 80% van je klantenbasis" kost heeft geen bron.

**Het onderliggende mechanisme is wél gemeten, door anderen.** Roth, Tuch, Mekler, Bargas-Avila & Opwis, [Location matters, especially for non-salient features](https://www.researchgate.net/publication/236630044), IJHCS 2013, N=40 eye-tracking, within-subject: objecten op de verwachte plek werden 300 ms tot ruim 2 seconden sneller gevonden. Reëel effect, maar klein en per handeling. Dat is de juiste maat: externe consistentie levert honderden milliseconden op, geen bekeringen.

**Het klassieke tegenargument.** Grudin, [The Case Against User Interface Consistency](https://dl.acm.org/doi/10.1145/67933.67934), CACM 32(10), 1989: consistentie die het leren makkelijker maakt kan botsen met gebruiksgemak. Zijn sterkste voorbeeld is het alfabetische toetsenbord, dat het consistente ontwerp is en verliest. Analytisch betoog, geen eigen data, maar het argument staat.

---

## De kaders, en wat ze waard zijn

| Kader | Herkomst | Wat het je geeft | Bewijs |
|---|---|---|---|
| Omkeerbaarheid, one-way tegen two-way doors | [Bezos, aandeelhoudersbrief 2015](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm) | De bewijslast schaalt met de terugdraaikosten, niet met de zichtbaarheid | Doctrine, nul studies. Bruikbaar als heuristiek |
| Criteria vooraf, QOC | [MacLean e.a., HCI 6(3-4), 1991](https://www.tandfonline.com/doi/abs/10.1080/07370024.1991.9667168) | Schrijf de vraag en de beoordelingscriteria op vóór je de opties bekijkt | Capture-probleem sinds [1994](https://www.sciencedirect.com/science/article/abs/pii/S1071581984710299) onopgelost, maar de discipline zelf kost niets |
| Beslishygiëne | Kahneman, Sibony & Sunstein, Noise, 2021; [mediating assessments](https://www.theuncertaintyproject.org/tools/the-mediating-assessments-protocol) | Iedereen scoort onafhankelijk en schriftelijk vóór de discussie. Senior spreekt niet eerst | Getest op selectie en taxatie, niet op design. Relatief het best onderbouwd |
| Vier risico's | [Cagan, 2017](https://www.svpg.com/four-big-risks/) | Welk risico verschilt: value, usability, feasibility of viability | Indeling uit consultancy-praktijk, nooit gevalideerd |
| Appetite en no-gos | [Shape Up, Singer 2019](https://basecamp.com/shapeup/1.2-chapter-03) | Tijd begrenst de oplossing, en je benoemt wat je niet doet | Eén bedrijfsverslag, nul vergelijkende metingen |
| Confidence-factor | [RICE, Intercom 2018](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/) | Onder de 50% zekerheid kies je niet, dan test je | Vier geschatte getallen vermenigvuldigen geeft schijnprecisie. De auteur zegt zelf dat het geen regel is |
| Premortem | [Klein, HBR 2007](https://hbr.org/2007/09/performing-a-project-premortem) | Stel dat het mislukt is, wat is er gebeurd | Zie waarschuwing hieronder |
| Beslissing vastleggen | [Nygard, ADR 2011](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | De verliezende optie blijft weerlegd, zodat niemand hem over een jaar opnieuw voorstelt | Adoptie groeit, geen studie toont betere uitkomsten |
| Beslissing tegen uitkomst | Duke, Thinking in Bets, 2018 | Beoordeel je redenering op het moment van kiezen, niet achteraf het resultaat | Logisch geldig, empirisch niets |

**Waarschuwing bij de premortem.** De rondgaande claim dat prospective hindsight het correct benoemen van oorzaken met 30% verhoogt, klopt niet. Klein verwijst naar [Mitchell, Russo & Pennington, JBDM 1989](https://onlinelibrary.wiley.com/doi/abs/10.1002/bdm.3960020103), en die studie mat het *aantal* gegenereerde redenen, beoordeelde de juistheid ervan niet, en het effect kwam vooral van zekerheid over de uitkomst. [Veinott, Klein & Wiggins (2010, n=178)](https://idl.iscram.org/files/veinott/2010/1049_Veinott_etal2010.pdf) laten zien dat een premortem het vertrouwen in een plan verlaagt, niet dat uitkomsten verbeteren. Gebruik de techniek, laat het cijfer weg.

---

## De vragenlijst

Loop deze langs bij een spanning tussen twee verdedigbare opties. De eerste vier zijn specifiek voor de gewoontespanning, de rest is algemeen.

**Eerst de klacht ontleden**

1. Is er iets **stuk**, of is er iets **onbekend**? Verloren functionaliteit is geen gewenningsprobleem en wordt nooit vanzelf beter.
2. **Wie heeft die gewoonte echt, en hoeveel zijn het?** Een gewoonte ontstaat alleen bij frequentie. Een handeling die iemand twee keer per semester doet, is geen gewoonte en kost dus niets om te veranderen.
3. Is de nieuwe route **bijna hetzelfde of duidelijk anders**? Bijna hetzelfde is de gevaarlijkste variant (Woltz 2000). Kies een kant.
4. Blijven deze gebruikers **lang genoeg** om de leercurve terug te verdienen? (Budiu, NN/g 2016)

**Dan het proces kalibreren**

5. Wat kost het om dit **terug te draaien**, in dagen én in vertrouwen? Goedkoop terug te draaien betekent: kies vandaag, vergader niet. (Bezos 2015)
6. Wie is **eigenaar** van deze keuze en wanneer valt hij uiterlijk?

**Dan de keuze scherpstellen**

7. Welke vraag beantwoorden A en B allebei? Zet die vraag bóven de opties. (QOC 1991)
8. Op welke criteria beoordeel ik, en staan die op papier **vóór** ik de opties bekeek? (QOC 1991, beslishygiëne 2021)
9. Welk risico verschilt er feitelijk: willen ze het, snappen ze het, kunnen we het bouwen, past het bij de business? (Cagan 2017)
10. Welke aanname moet waar zijn om A te laten winnen, en welk bewijs heb ik daarvoor?
11. Hoe zeker ben ik, in procenten? Onder de 50% kies ik niet, dan toets ik. (RICE-confidence)

**Dan de begrenzing en de tegendruk**

12. Hoeveel tijd is dit me waard, en welke optie past daarin? (Shape Up)
13. Wat doe ik in **beide** opties expliciet niet? (no-gos)
14. Het is zes maanden later en dit is mislukt. Wat is er gebeurd? (premortem, zonder het cijfer)
15. Wat zou de verliezende optie moeten laten zien om alsnog te winnen?
16. Staat mijn redenering ergens waar de volgende persoon hem vindt? (ADR)

---

## Welke toets beantwoordt welke vraag

| Vraag | Goedkoopste toets | Wat je moet weten |
|---|---|---|
| Snappen mensen wat dit is? | 5-second test | Werkt alleen bij schermen met één doel |
| Vinden ze het terug? | tree testing (structuur), first-click test (scherm) | Tree testing: minimaal 30, liefst 100 per gebruikerstype |
| Hoe zouden ze het zelf ordenen? | cardsorting, 20-30 deelnemers | Correlatie met eindresultaat 0,75 bij n=5 en 0,95 bij n=30 ([NN/g 2004](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/)) |
| Waar lopen ze vast en waarom? | moderated usability test, **minimaal 10** | Zie hieronder waarom niet 5 |
| Welke vinden ze prettiger? | preference test | Lees het als werklast-signaal, niet als gedragsvoorspelling |
| Wil iemand dit überhaupt? | fake door | Meet interesse op het klikmoment, niet betaalbereidheid |
| Waar vallen ze nu af? | funnelanalyse | Zegt wat en waar, nooit waarom |
| Wordt het beter of slechter over weken? | diary study of gefaseerde uitrol met holdout | 4-11 deelnemers, 1 dag tot 2 weken |
| Hoeveel beter is B dan A? | A/B-test | Alleen als je de gebruikers hebt. Meestal heb je ze niet |

**Waarom niet vijf gebruikers.** [Nielsen & Landauer, CHI 1993](https://dl.acm.org/doi/10.1145/169059.169166) is een Poisson-model met een aangenomen detectiekans van 31%, geen meting. [Faulkner 2003](https://pubmed.ncbi.nlm.nih.gov/14587545/), 60 gebruikers, is het scherpste bewijs: sommige willekeurige sets van 5 vonden 99% van de problemen, andere 55%. Bij 10 gebruikers steeg de ondergrens naar 80%, bij 20 naar 95%. Je weet nooit in welke set je zit, dus 5 is een gok en 10 is een ondergrens.

**Waarom A/B voor de meeste producten dood is.** Uit [Kohavi e.a., DMKD 2009](https://ai.stanford.edu/~ronnyk/2009controlledExperimentsOnTheWebSurvey.pdf), n = 16σ²/Δ² per variant bij 80% power: bij een basisconversie van 5% kost het aantonen van een 5% relatieve verandering circa 122.000 gebruikers per arm, en een 20% relatieve verandering circa 8.000. Sensitiviteit zit in het kwadraat: tien keer gevoeliger meten kost honderd keer meer gebruikers. Kohavi's eigen ondergrens is "at least thousands of active users". En zelfs met dat verkeer haalt maar ongeveer een derde van de goed doordachte ideeën bij Microsoft de beoogde metriek, bij Google en Bing minder.

**Consequentie voor een klein product:** de keuze wordt beslecht op vakmanschap plus tien moderated sessies plus alarmbellen in de data. Niet op experimenten. Wie in die situatie om "de cijfers" vraagt, vraagt om iets dat niet bestaat, en het eerlijke antwoord is dat je de onzekerheid verlaagt door beter te kijken, niet door te meten.

---

## Uitrollen naar bestaande gebruikers

- **Opt-in preview met terugzetknop.** Gmail 2018 is de enige volledig gedocumenteerde kalender: opt-in vanaf 25 juli, automatische migratie vanaf 18 september, geen weg terug na 16 oktober. Circa drie maanden naast elkaar. [Google Workspace Updates, 2018](https://workspaceupdates.googleblog.com/2018/07/new-gmail-ga.html). Microsoft doet hetzelfde in drie fases met naam, opt-in naar opt-out naar cutover, met minimaal 12 maanden aankondiging per fase. [Microsoft Learn, 2024](https://learn.microsoft.com/en-us/microsoft-365-apps/outlook/get-started/guide-product-availability)
- **Gefaseerde uitrol met guardrails.** [Xu, Duan & Huang, LinkedIn 2018](https://arxiv.org/abs/1801.08532): ramps voor risicobeheersing, dan een Maximum Power Ramp op 50/50 voor de meting, minstens een week erop blijven. Bing houdt permanent 10% van de gebruikers buiten elk experiment als controle. Een long-term holdout van circa 5% loopt langer dan een maand en alleen met een expliciet leerdoel.
- **Dual-run.** GitHub Scientist draait beide codepaden in productie, geeft de gebruiker altijd het oude resultaat en logt alleen het verschil. [GitHub, 2016](https://github.blog/2016-02-03-scientist/)
- **Uitleg op het moment zelf, niet vooraf.** Tours vooraf onderbreken mensen die iets anders willen doen, worden overgeslagen en verbeteren de taakprestatie niet. [NN/g, 2023](https://www.nngroup.com/articles/onboarding-tutorials/)
- **Snap, Sonos en Windows 8 hadden bij lancering geen terugzetknop.** Alle drie moesten terugdraaien. Dat is het goedkoopste patroon dat ze hadden kunnen kopen.

## Het meetprobleem bij verandering

1. **Segmenteer per dag en per bezoek.** Een coach mark bij Microsoft leek de clicks met 0,96% te verhogen, maar de winst zat volledig in het bezoek waarin hij werd getoond, daarna nul. [Dmitriev e.a., KDD 2017](https://exp-platform.com/Documents/2017-08%20KDDMetricInterpretationPitfalls.pdf)
2. **Bereken de metriek apart voor nieuwe gebruikers.** Die hebben geen oude gewoonte, dus geen gewenningseffect. Dat is de schoonste vergelijking die je hebt.
3. **Meet minstens een volle week, en reken op drie.** Een MSN-experiment ging van -5,07% in de eerste drie dagen naar -1,23% en niet-significant in week 3. [Sadeghi e.a., 2021](https://arxiv.org/abs/2102.12893)
4. **Voor echte leereffecten: een A/A-nameting.** Google draaide long-term studies van circa drie maanden en gebruikte een periode ná de behandeling waarin alleen leereffecten het verschil nog kunnen verklaren. [Hohnhold, O'Brien & Tang, KDD 2015](https://research.google/pubs/focus-on-the-long-term-its-better-for-users-and-business/)
5. **Vertrouw zelfrapportage niet.** [Webb & Sheeran, Psychological Bulletin 2006](https://pubmed.ncbi.nlm.nih.gov/16536643/), 47 experimenten: een medium tot grote verandering in intentie (d = 0,66) levert een kleine tot medium verandering in gedrag (d = 0,36). [Nielsen & Levy, CACM 1994](https://dl.acm.org/doi/10.1145/175276.175282): in 25% van de gevallen prefereerden mensen het systeem waarmee ze slechter presteerden. [Hertzum, IJHCS 2025](https://forskning.ruc.dk/da/publications/understanding-preference-a-meta-analysis-of-user-studies), 144 studies: voorkeur hangt sterker samen met ervaren werklast dan met snelheid of foutkans.

**Alarmbellen bij een ingrijpende wijziging:** afhaakratio bij de kernactie, tijd tot die kernactie, terugkeer in sessie 2, supporttickets, foutratio, latency, en het aandeel gebruikers dat een automatisch aangemaakt object hernoemt of weggooit. Alarmeer pas als een verschil zowel significant als groot genoeg is om iets te betekenen.

---

## Waar de bronnen elkaar tegenspreken

- **Sedley tegen Spool.** Google behandelt aversie als een eigenschap van de gebruiker die je moet managen. [Spool (2012)](https://archive.uie.com/brainsparks/2012/07/16/googles-take-on-change-aversion-misses-the-point/) zegt: mensen haten niet verandering maar plotseling incompetent zijn, dus het is jouw fout. Geen van beiden levert data. Onbeslist.
- **Duur van de dip.** Sedley suggereert een lange transitieperiode met aanhoudende onvrede, Santa-Maria & Dyson meten dat het verschil binnen één sessie verdwijnt. Dat is een orde-van-grootteverschil dat niemand heeft opgelost.
- **Nielsen tegen Grudin.** Volg externe conventies, tegenover: consistentie is een onbetrouwbare gids. Grudin heeft het betere argument, Nielsen het zwakkere bewijs, en Roth (2013) geeft Nielsen gedeeltelijk gelijk met een klein effect.
- **Snelheid tegen structuur.** Bezos zegt: bij een omkeerbare keuze beslist één persoon snel. Kahneman zegt: eerst onafhankelijke oordelen verzamelen. Verzoening: het ruisprotocol alleen bij onomkeerbare keuzes.
- **Eén scherm tegen stappen.** [Rodríguez e.a., JMIR Human Factors 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8190652/) (n=20) vonden het eenpaginaformulier het beste op tevredenheid, snelheid en fouten, terwijl de onboardingliteratuur juist opsplitsen aanraadt.

## Gaten

- **Geen post-launch effectdata voor de Office-Ribbon.** Microsoft publiceerde uitgebreid over de telemetrie vooraf (1,3 miljard sessies, Paste is 11% van alle commando's in Word), maar nooit een gemeten productiviteitsdip of hersteltijd erna. De Ribbon-case is dus half bewijs.
- **CommandMaps is lab.** 18 deelnemers, één uur, zes doelen. Geen veldvalidatie over weken.
- **Snap en Sonos zijn niet uit te splitsen.** Niemand heeft ooit gescheiden welk deel van de daling aan verwarring lag en welk deel aan verloren functionaliteit.
- **Geen enkel kwantitatief model** dat winst tegen omschakelkosten weegt. Het bestaat niet.
- **Geen originele bron voor de aanbevolen n** bij preference tests, first-click tests en 5-second tests. Alles wat circuleert is tool-marketing.
- **Geen kostenrapport per onderzoeksmethode** met methodologie. Elk bedrag online komt van een leverancier.

## Cijfers die je niet moet gebruiken

Deze kwamen we tegen en zijn niet terug te voeren op een origineel rapport met methodologie:

- **"45% van dagelijks gedrag is gewoonte."** De gemeten waarden zijn 35%, 43% en 47% (Wood, Quinn & Kashy, JPSP 2002; Quinn & Wood 2005). De 45% is een afronding in een review zonder eigen data.
- **"21 dagen om een gewoonte te vormen."** Maxwell Maltz, Psycho-Cybernetics, 1960. Klinische observatie, geen studie. De 66 dagen uit [Lally e.a. 2010](https://onlinelibrary.wiley.com/doi/abs/10.1002/ejsp.674) bestaat wel, maar rust op 39 bruikbare curvefits met een spreiding van 18 tot 254 dagen.
- **Jakob's Law "80% van je klantenbasis".** Geen bron.
- **Alle Dvorak-toetsenbordcijfers.** [Liebowitz & Margolis 1990](https://personal.utdallas.edu/~liebowit/keys1.html) laten zien dat de originele experimenten door Dvorak zelf zijn uitgevoerd en methodologisch niet houdbaar zijn.
- **"Premortems verbeteren foutopsporing met 30%."** Zie de waarschuwing hierboven.
- **"Spool & Schroeder: de eerste 5 gebruikers vonden 35%."** Niet te herleiden tot het originele CHI-2001-paper. Alleen via secundaire bronnen.
- **"Bailey & Wolfson 87% first-click."** Niet te herleiden tot het originele HCII-2009-paper.
- **Ramp-percentages 1 naar 5 naar 20 naar 50.** Geen primaire bron. LinkedIns 50/50 en Bings 10% holdout zijn wel primair.
