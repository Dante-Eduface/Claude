---
name: linkedin-content
description: Schrijft LinkedIn-posts in 4 stemmen (Dante, Jeroen, Menno, Eduface company page) vanuit gekalibreerde stem-profielen + content-pijlers, plak-klaar voor Buffer. Trigger wanneer Dante zegt "schrijf een LinkedIn post", "maak content voor Jeroen/Menno/Eduface", "linkedin batch", "content kalender", "thought leadership post", of een post in iemands stijl vraagt. Stemmen worden gekalibreerd op echte posts in voice-samples/. Anchored aan voice-profiles.md, content-pillars.md en het cro handboek.
---

# LinkedIn Content

Schrijft LinkedIn-posts in de 4 Eduface-stemmen en levert ze plak-klaar voor Buffer (Dante's scheduler). Geen autoposting: de skill schrijft, Dante plant in Buffer.

Handboek-lens: elke post is top-of-funnel demand-gen die Stage 1 (Discovery) voedt. De taak is institutionele pijn zichtbaar maken bij de juiste mensen, niet likes scoren. Koppel waarde aan pijn op instituutsniveau (retention, financiele gezondheid, risk), of zet een buying-criterion (differentiatie vs de Enemy). Zie de `cro` skill.

## De 4 stemmen (detail in `voice-profiles.md`)

- **Dante** (SDR -> CRO): observaties uit gesprekken met UK HE-instellingen, zonder vertrouwelijke info. Scherpe takes over feedback + AI-hype. Bouwt sector-autoriteit en maakt zijn outreach geloofwaardiger.
- **Jeroen** (CEO): milestones/momentum (events, partnerships, product) + AI-ethiek & vertrouwen. Spreekt de economic buyer en procurement aan.
- **Menno** (CTO): technisch-wetenschappelijke kant van het model (sparse activation, output-validatie, generatieve AI vs classificatie). Bereikt IT, data officers, procurement. Beantwoordt de Sureness/Easyness-vragen van de EB. **Tijd beschermen:** ghostwrite, max 1 korte intake, nooit zelf laten produceren (team-rule: protect the builders).
- **Eduface** (company page): brand-stem. Versterkt de drie persoonlijke thema's + product-proof, klant-stories, webinars/events. Polished, geen ego.

## De loop

1. Bepaal per post: WIE (stem) + WELKE pijler/invalshoek (`content-pillars.md`) + TAAL + FORMAT.
2. Schrijf vanuit het stem-profiel. Neem een scherp standpunt in (zie House rules). Geen generieke AI-tekst.
3. Lever per post: hook (regel 1), body, optionele zachte CTA, format-notitie, hashtags. Plak-klaar voor Buffer.
4. Bij een batch: spreid pijlers en stemmen, hou de UK HE-kalender aan (zie `cro` seizoens-logica), lever als markdown-lijst.

## House rules

- **Taal:** alle content in het Engels, voor alle 4 de stemmen (besluit Dante 2026-06-18).
- **Scherp, niet neutraal.** Neutrale content presteert slecht. Schrijf posts waar mensen "daar ben ik het niet mee eens" op willen reageren. Voorbeeld-take: "Feedback turnaround in UK HE is structureel te traag. Dat is geen capaciteitsprobleem, het is een prioriteitsprobleem." AI in onderwijs altijd genuanceerd, nooit mee in de hype.
- **Stijl:** plain, gesproken taal. Geen hype, geen buzzwords, GEEN em-dashes (gebruik komma of punt). Korte zinnen. 1 idee per post.
- **Eerlijk:** nooit pilot-cijfers of klant-claims verzinnen. Kwalitatief blijven of echte cijfers uit `GTM/` en `Platform/` gebruiken.
- **Per post 1 doel:** welke Discovery-pijn of welk buying-criterion raakt deze post? Is het antwoord "geen", herschrijf.

## Stem-kalibratie

De stem-profielen zijn **GEIJKT** op echte posts (2026-06-18, corpus in `voice-samples/`). Lees altijd `voice-profiles.md` voor je schrijft.
- **Cruciaal:** niet elke echte post is een goede norm. Een deel is overduidelijk met AI geschreven. Emuleer de posts getagd ✅ in de samples, niet de posts getagd ⚠️. De AI-tells staan opgesomd in `voice-profiles.md` (bold-unicode, emoji per regel, "excited to announce", feature-dumps).
- Nieuwe echte posts toevoegen aan `voice-samples/` houdt de kalibratie scherp. LinkedIn is niet te scrapen vanuit deze tools, dus dat gaat handmatig (copy-paste, `Shares.csv`-export, of Buffer-historie).

## Intake via werkbestanden

Elke stem heeft een self-contained HTML-werkbestand in `GTM/Campaigns/linkedin-content/werkbestanden/` (1 per persoon, Eduface = master + gedeelde CTA). De persoon vult het in op zijn laptop, downloadt een `.md` en stuurt die naar Dante. Doel: Jeroen/Menno (kritisch, willen controle) zien de input en houden de pen.
- Krijg je een ingevulde `.md`: verwerk de stem-markers, onderwerpen, rode lijnen en feiten in `voice-profiles.md` voor die persoon, en gebruik de voorbeeldpost-reactie om de toon bij te stellen.
- Niets wordt geplaatst zonder OK van de persoon. Concept -> persoon keurt -> Buffer.

## Research-stap (voor je schrijft)
- Onderbouw posts met echte, actuele feiten. Gebruik een research-subagent (Agent tool, general-purpose) die het opzoekwerk doet en alleen de kale feiten teruggeeft: cijfer, bron, jaar, URL. Zo blijft de hoofd-context licht en kosten posts weinig tokens.
- Eduface-feiten staan in `eduface-facts.md` (van de site + team). Externe claims (studies, regelgeving, sector-cijfers) via de subagent ophalen, altijd met bron + jaar + link.
- Vind je een Eduface-intern getal niet, vraag het Dante/team en verwerk het antwoord.

## CTA-strategie (huidige fase: accounts moeten nog actief worden op LinkedIn)
- De "stel een vraag, lok discussie uit"-CTA werkt pas met een actieve, reagerende following. Die hebben de accounts nog niet.
- Begin met CTA's die simpele engagement of clicks/impressies opleveren: link in de comments (geeft meteen de bron-onderbouwing), iets dat makkelijk te liken/delen is.
- Niet elke post hoeft een CTA. Een sterke, deelbare post zonder CTA mag.
- Doel deze fase: deelbare, potentieel virale posts die bereik opbouwen. Sterke hook, breed herkenbaar, makkelijk te lezen, vaak een scherp/verrassend datapunt. Tag relevante mensen/organisaties (@) voor bereik.

## Output + review

- Default review-surface: een markdown-batch in `GTM/Campaigns/linkedin-content/` (maak de map als die er niet is), die Dante naar Buffer kopieert.
- Elke post als los blok:
  ```
  ## [Stem] · [Pijler] · [Taal]
  <hook = regel 1>
  <body>
  <optionele zachte CTA>
  Format: <single text / carousel / image / poll>
  Doel: <welke Discovery-pijn of buying-criterion>
  #hashtags
  ```

## Done

- Posts staan klaar in de gevraagde stem(men), scherp, plain, geen em-dashes, elk met een duidelijk Discovery- of buying-doel, plak-klaar voor Buffer.
- Bij een nieuwe of meaningful wijziging: log het in `Decisions/log.md`.
