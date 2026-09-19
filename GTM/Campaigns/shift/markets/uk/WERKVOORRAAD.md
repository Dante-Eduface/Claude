# Werkvoorraad uk: welke bronnen zijn af, welke niet

Stand van zaken voor agent 1. Bijwerken na elke ronde.

Laatst bijgewerkt: 2026-09-11

## Af

- **Zaadlijst Dante (10-09-2026)**, 36 organisaties: elf moederconcerns plus merken. Poort 0/0b/0d en Close-check gedaan op 10-09. Uitkomst: 15 gekwalificeerd (Arden, LCCA, BPP University, BPP Professional Education, QA HE, GBS, BIMM Music Institute, MetFilm, Performers College, MetStudios, Study Group, Kaplan Intl Pathways, INTO, ONCAMPUS, Navitas UK Holdings), 3 geblokkeerd via Close (University of Law, LSBF, The College Swansea), 1 afgevallen (CEG Digital), rest kandidaat (holdings en losse pathway-colleges).

## Wat werkte als bron

- Eigen assessment/moderation policies als PDF (Arden QA21, GBS Assessment and Feedback Policy, BPP GARs Section E). **WebFetch geeft PDF's als binair terug; lokaal uitlezen met PyMuPDF of pypdf.** Niet opgeven na één mislukte fetch.
- QAA-rapporten per pathway-college uit 2016: `qaa.ac.uk/docs/qaa/reports/<slug>-her-ec-16.pdf`, werkt zonder `sfvrsn`.
- QAA Educational Oversight Reviews (2024-2025) voor Kaplan, QAHE, INTO.
- BAC interim reports (LCCA).

## Wat niet werkte

- st-patricks.ac.uk gooit een ASP.NET Runtime Error op elke pagina (poort 0 daardoor Onbekend).
- Navitas fee- en studentenpagina's zijn JS-dropdowns: geen hard lerendenaantal of GBP-fee te vinden, omvang overal onbekend.
- `bpp.com/courses/acca` 404; BPP-tuition marking-bewijs staat alleen in een prijslijst uit 2021.
- `qa.com/en-gb/qa-higher-education/` 404; werkend domein is `qahighereducation.com`.
- Zaadlijst had `lcca.org.uk`; het is `lcca.ac.uk`.
- HESA: Cloudflare 403 op elke fetch.

## Valkuilen voor de volgende ronde

- "Awarded by <universiteit>" of "awarded by Pearson" is geen poort-0-afvaller bij pathway/franchise: het centre kijkt zelf na. Lees door tot je ziet wie markt.
- NSS-respondentenaantallen zijn geen instroom (ULaw 755 was een respondentenaantal).
- Deze batch is per ongeluk dubbel uitgezet (twee agent-1-runs parallel); waarden zijn gemerged, journaal toont beide.

## Open

1. **OfS-lijst van 49 private aanbieders** (profiel, kop Registers: `Category = Approved` × charity `Not applicable`). Verwacht: circa 30 nieuwe kandidaten buiten de zaadlijst (Regent's, Istituto Marangoni, Richmond American, Northeastern London, Pearson College, ...).
2. Ontbrekende merken van de zaadlijst-groepen: Northern Ballet School (BIMM), Edinburgh International College / ICRGU / ICWS (Navitas), losse INTO- en Kaplan-centra alleen als koopeenheid.
3. Onbekenden oplossen: St Patrick's (site kapot), The Language Gallery, MMUIC (nieuw, geen beleid online), UA92 Global, Oxford International HE-poot.
4. Omvang bij pathway-groepen via jaarrekeningen (Companies House) in plaats van sites.
