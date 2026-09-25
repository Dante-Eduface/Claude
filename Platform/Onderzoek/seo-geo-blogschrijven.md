# SEO en GEO voor Eduface-blogs

_Onderzoek 25-09-2026, via `/deep-research` (zes parallelle lijnen plus een tegenspraakronde). Basis voor de skill `.claude/skills/blog-writer/`._

**Beperking vooraf:** in deze omgeving waren eduface.me, developers.google.com, arxiv.org, nngroup.com en de meeste andere sites geblokkeerd voor direct ophalen. Bijna alles hieronder komt uit zoekresultaat-samenvattingen, niet uit zelf gelezen bronnen. Dat staat haaks op de regel "bron echt openen" uit `deep-research`. De conclusies zijn consistent over onafhankelijke bronnen heen, maar **controleer elk los getal in de bron voordat het in een blog of deck belandt.**

## Het antwoord

1. **Voor Google is GEO gewoon SEO.** Google's AI-optimalisatiegids (15-05-2026) en Danny Sullivan (2025-26): geen llms.txt, geen chunking, geen speciale schema, geen AI-herschrijvingen nodig. De AI-functies draaien op de gewone index.
2. **De bekende GEO-tactieken houden niet stand buiten het lab.** GEO-paper (KDD 2024): +30 tot 40% door statistieken en citaten, in een simulatie. Replicatie C-SEO Bench (NeurIPS 2025): 3 van 54 combinaties significant, geen bij vraag-antwoord. Of je opgehaald wordt weegt zwaarder dan hoe je formuleert.
3. **Wat aantoonbaar werkt, is gewoon goed schrijven:** het antwoord eerst, koppen die de inhoud zeggen, tabellen voor vergelijkingen (enige causale studie: CITECHOICE 2026), eigen informatie die niemand anders heeft, deelvragen als eigen secties (query fan-out).
4. **Blogs zijn niet de grootste hefboom voor AI-zichtbaarheid.** Merkvermeldingen elders correleren 0,664 met zichtbaarheid in AI Overviews, backlinks 0,218, aantal eigen pagina's zwak (Ahrefs, 75.000 merken; vendor, correlatie).
5. **Het grootste risico zit in de bestaande aanpak:** een reeks bijna-gelijke artikelen per LMS en per vak lijkt op het spampatroon "scaled content abuse". Minder en sterker wint.

## Waar bronnen elkaar tegenspreken

- **Hoe groot de klikdaling door AI Overviews is.** Ahrefs -58% CTR op positie 1 (dec 2025), Seer -61 tot -65% met herstel naar 2,4% CTR in februari 2026, Pew 15% naar 8% (juli 2025). Ze meten verschillende dingen. Richting eenduidig, grootte niet. Google (Liz Reid, aug 2025) zegt dat clicks "relatively stable" zijn, zonder data en met belang.
- **Of een Google-toppositie tot AI-citaties leidt.** Seer 92%, Ahrefs 76% naar 38%, BrightEdge 16,7%, Ahrefs voor ChatGPT 12%. C-SEO Bench zegt dat retrieval-positie de dominante factor is. Beide kunnen kloppen: Google-ranking en retrieval binnen een AI-systeem zijn niet hetzelfde. Ik weeg het zo: vindbaar zijn in de gewone index is voorwaarde, niet garantie.
- **Of AI-verkeer beter converteert.** Semrush 4,4x (vendor, marketingonderwerpen), Seer 15,9% tegenover 1,76% (agency), Amsive geen verschil, 973 e-commercesites -13% (Marketing Science, academisch). Ik weeg de academische studie het zwaarst: geen reden om aan te nemen dat AI-verkeer beter is.
- **Schema en AI-citaties.** Ahrefs: geen effect, AI Overviews -4,6%. BrightEdge: +44%, maar verkoopt schema-tooling. Ahrefs weegt zwaarder: grotere steekproef, controlegroep, en het resultaat gaat tegen hun eigen belang in.
- **Lengte.** Correlatiestudies laten zien dat lange artikelen beter scoren, Google zegt dat lengte geen factor is. Het verband loopt via backlinks en diepgang, niet via woordaantal.
- **Chunking.** GEO-gidsen raden zelfstandige blokken aan, Google raadt het af. Opgelost in de skill: gewone alinea's met één punt en entiteiten bij naam, geen kunstmatig opknippen.

## Wat dit betekent voor Eduface

Blogs zijn ondersteunend aan de prioriteit (20 salesprocessen per maand), geen pijplijnmotor. Hun waarde zit in de onderzoeksfase van een koper: B2B-kopers gebruiken bijna allemaal generatieve AI tijdens de aankoop (Forrester 2026, via zoekresultaat), en de winnende leverancier stond in 95% van de gevallen al op de shortlist van dag één (6sense 2025, vendor). Schrijf dus vooral wat een koper helpt kiezen: vergelijkingen, integratie, compliance, business case. Niet meer definitie-artikelen. En de bestaande reeks nalopen op bijna-dubbele pagina's en verouderde feiten (de EU AI Act-datum), voordat er nieuwe bij komen. Dat laatste is een inferentie, geen gemeten effect.

## Gaten

- Geen publiek onderzoek naar welke bronnen AI-zoekmachines citeren voor vragen over AI-nakijken in het hoger onderwijs. Alleen sector-onafhankelijke data.
- Geen onafhankelijk bewijs over SEO tegenover outbound in een kleine B2B-niche.
- Geen conversiedata voor AI-verkeer bij enterprise B2B met lange salescycli.
- Of eduface.me al door ChatGPT of Perplexity geciteerd wordt: niet vastgesteld. Wel dat het in gewone zoekresultaten staat voor Moodle, Canvas en "AI grading tools".
- Of Framer de blogpagina's server-rendered levert: generiek bevestigd, niet voor de blog getest.
- ~~De volledige tekst van de vier referentieblogs~~: door Dante geplakt op 25-09-2026, staat in `.claude/skills/blog-writer/referentie/`.

## Bronnen

### Primair
- Google, Spam policies update (scaled content abuse, site reputation abuse), 2024. developers.google.com/search/blog/2024/03/core-update-spam-policies
- Google, AI optimization guide, 15-05-2026. developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google, AI features and your website, 2025. developers.google.com/search/docs/appearance/ai-features
- Aggarwal et al., GEO: Generative Engine Optimization, KDD 2024. arxiv.org/abs/2311.09735
- C-SEO Bench, NeurIPS 2025 Datasets & Benchmarks. arxiv.org/abs/2506.11097
- CITECHOICE, causale audit van gestructureerde weergave, 2026 (preprint). arxiv.org/abs/2609.15164
- What Gets Cited, competitive GEO, 252.000 trials, 2026 (preprint). arxiv.org/abs/2605.25517
- Kritisch overzicht van 45 GEO-studies, 2026 (preprint). arxiv.org/abs/2607.14035
- Recency bias bij LLM-rerankers, SIGIR-AP 2025. arxiv.org/abs/2509.11353
- Kobak et al., LLM-sporen in 15 mln biomedische abstracts, Science Advances 2025. doi.org/10.1126/sciadv.adt3813
- Pew Research, Google users are less likely to click when an AI summary appears, 22-07-2025. pewresearch.org/short-reads/2025/07/22/
- Conversie van LLM-verwijzingen, 973 e-commercesites, Marketing Science 2025. pubsonline.informs.org/doi/10.1287/mksc.2025.0489
- Vercel/MERJ, The rise of the AI crawler, 2024. vercel.com/blog/the-rise-of-the-ai-crawler
- EU AI Act Bijlage III. artificialintelligenceact.eu/annex/3/
- Digital Omnibus on AI, in werking 27-07-2026: Bijlage III uitgesteld naar 02-12-2027 (via Gibson Dunn, Cloud Security Alliance, DLA Piper, 2026)
- Ofqual, Principles of AI use in marking, januari 2026
- HEPI, Student Generative AI Survey 2026 (Report 199), maart 2026. hepi.ac.uk

### Secundair (vakpers, analisten)
- Search Engine Journal, Google drops FAQ rich results, 2026
- Search Engine Land, Sullivan: good SEO is good GEO, 2025-26
- Search Engine Land, Google changed 76% of title tags in Q1 2025
- Kevin Indig, Growth Memo, The science of how AI pays attention, 2026
- Hobo Web, analyse Content Warehouse-lek, 2024
- SparkToro met Gumshoe, AI-aanbevelingen inconsistent, januari 2026
- NN/g, F-pattern en layer-cake scanning (2006, doorlopend)

### Tertiair of vendor (belang meewegen)
- Ahrefs: AI Overviews en CTR (2025), schema en AI-citaties (2026), merkcorrelaties (2025-26), overlap top-10 (2025-26)
- Seer Interactive: AIO en CTR, updates 2025 en 2026; Bing-overlap SearchGPT
- Semrush: meest geciteerde domeinen, AI Mode zero-click, AI-verkeer 4,4x
- Grow & Convert: pain point SEO, conversie per zoektermtype (2024-25)
- OtterlyAI: llms.txt-experiment, 2025
- BrightEdge: YouTube-citaties, schema +44%
- Clearscope: information gain
- derivatex.agency: B2B SaaS-citatiestudie, 2026
