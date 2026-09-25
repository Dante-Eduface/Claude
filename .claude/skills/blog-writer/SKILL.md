---
name: blog-writer
description: Schrijft Engelstalige blogs voor eduface.me/resources/blog in de Eduface-blogstem (gekalibreerd op de volledige tekst van de vier beste blogs: de koopgids AI grading tools, de Canvas- en Moodle-integratiepagina's en de EU AI Act-uitlegger) en zo dat ze ranken in Google en opgepikt worden door AI-zoekmachines (SEO en GEO, onderbouwd met onderzoek en zonder de trucs die niet werken). Levert een markdown-concept op dat `blog-builder` daarna live zet. Trigger wanneer Dante zegt "schrijf een blog over", "maak een blogartikel", "blog voor de website", "schrijf een artikel dat rankt op", "we moeten gevonden worden op [zoekterm]", "update/ververs deze blog", "herschrijf deze blog", of een onderwerp of zoekterm voor eduface.me aanlevert. NIET voor LinkedIn-posts (linkedin-content), mails of losse sitecopy (schrijven), of het bouwen en publiceren in Framer (blog-builder).
---

# Blog writer

Schrijft het beste antwoord op een echte vraag van een lecturer, programme director, learning technologist of inkoper in het hoger onderwijs, in de Eduface-stem, in een vorm die mensen en machines makkelijk lezen. Dat is de hele SEO- en GEO-strategie; `seo-geo.md` legt uit waarom.

Deze skill schrijft. `blog-builder` bouwt en publiceert. De grens: deze skill levert een `.md` in `GTM/Campaigns/blog-launch/markdown-sources/`, en pas als Dante zegt "zet live" of "bouw hem" gaat het naar `blog-builder`.

## Eerst lezen, elke keer

1. `stijl.md` : de stem, de anatomie van een pagina, en wat je uit de referenties niet overneemt.
2. `referentie/` : de vier referentieblogs letterlijk. Lees minstens de referentie van het type dat je schrijft, helemaal.
3. `seo-geo.md` : welke regels werken en welke niet.
4. `artikeltypes.md` : het skelet per type.
5. `LEERPUNTEN.md` : eerdere feedback van Dante op blogs.
6. `Platform/product.md` : de enige bron voor claims over Eduface.
7. `bronnen.md` : alleen als je iets citeert.

## De loop

```
1. BRIEF       onderwerp, zoekvraag, lezer, type
2. BESTAAT HET bestaande blog op dezelfde zoekintentie? dan updaten, niet nieuw
3. VERKEN      wat staat er nu, wat ontbreekt, welke deelvragen
4. POORT       titel, koppen, informatiewinst en claims aan Dante voorleggen
5. SCHRIJF     het volledige concept
6. ZELFCHECK   de vier checks hieronder
7. LEVER       bestand plus korte toelichting plus open punten
```

### 1. Brief

Haal uit de vraag van Dante:
- **Zoekvraag:** de zin die de lezer intypt of aan ChatGPT vraagt. Niet het onderwerp, de vraag.
- **Lezer:** welke rol, en wat moet die na het lezen kunnen beslissen of doen.
- **Markt:** standaard UK (Brits Engels). NL of US alleen als Dante het zegt.
- **Type:** koopgids, integratiepagina, regelgeving, vak of toepassing, werkwijze. Zie `artikeltypes.md`.

Mist er iets dat je niet kunt afleiden, vraag het in één regel. De rest vul je zelf in en noem je bij de poort.

**Toets aan de prioriteit.** De staande prioriteit is 20 salesprocessen per maand (`Context/current-priorities.md`). Een blog verdient zijn plek als hij een koper helpt kiezen of een gesprek opent: vergelijking, integratie, compliance, business case. Een puur informatief stuk ("what is AI grading") levert door AI-samenvattingen weinig clicks op. Zeg dat in één zin als de vraag die kant op gaat, en stel een handelingsgerichte hoek voor.

### 2. Bestaat het al?

Goedkoop eerst, zoals `.claude/rules/credits.md` vraagt:
- `ls GTM/Campaigns/blog-launch/markdown-sources/` en de slugs in `GTM/Campaigns/blog-launch/covers/MANIFEST.md`.
- Eén `WebSearch` met `allowed_domains: ["eduface.me"]` op de zoekvraag.

Bestaat er een blog op dezelfde zoekintentie: **stel een update voor in plaats van een nieuw artikel.** Twee bijna-gelijke pagina's concurreren met elkaar en lijken op het spampatroon "scaled content abuse". Een LMS- of vakvariant mag alleen als hij echt eigen inhoud heeft.

### 3. Verken

Hoogstens vijf zoekopdrachten, dan stoppen:
- De zoekvraag zelf, in twee of drie formuleringen (UK en US). Wat staat er bovenaan, wie schrijft het, welk type pagina wint?
- Wat ontbreekt er in die resultaten? Dat wordt het informatiewinst-blok.
- Welke deelvragen heeft deze lezer (kosten, integratie, compliance, accuraatheid, wie keurt goed, wat als het misgaat)? Dat worden de H2's.
- Heb je een feit nodig uit regelgeving of onderzoek: eerst `bronnen.md`, dan pas het web. Open de bron en lees de passage. Lukt openen niet, citeer dan niet en meld het.

### 4. Poort: eerst de opzet, dan de tekst

Schrijf een blog nooit meteen helemaal uit. Leg Dante dit voor, kort:

- **Titel**: je voorstel plus twee alternatieven
- **SEO-titel** (onder 60 tekens, eindigt op `| Eduface`), **meta** (140 tot 160 tekens), **slug**
- **H2's**, in volgorde
- **Informatiewinst**: wat staat hier dat nergens anders staat
- **Claims over Eduface**, elk met de regel uit `product.md` waar hij vandaan komt
- **Interne links**: de hub en één of twee zijartikelen

Dante kiest of past aan, dan schrijf je één keer. Zegt hij "gewoon schrijven", sla de poort over en lever de opzet mee bovenaan het concept.

### 5. Schrijf

Het format dat `blog-builder` verwacht, met frontmatter erboven. De opbouw volgt de anatomie uit `stijl.md`.

```markdown
---
title: <H1>
seo_title: <onder 60 tekens> | Eduface
meta_description: <140-160 tekens, mag gelijk zijn aan de dek>
slug: <kort-met-hoofdterm>
primary_query: <de zoekvraag>
secondary_queries: [<deelvragen>]
type: <koopgids | integratie | regelgeving | vak | werkwijze>
category: <Product | Integrations | Compliance | Research | Thought Leadership>
hub: </resources/blog/...>
review_by: <JJJJ-MM-DD, eerder bij regelgeving en tools>
status: concept
---

EYEBROW: <ONDERWERP · SUBONDERWERP>

# <H1: hoofdterm vooraan: reikwijdte>

*<Dek: een of twee zinnen>*

By Eduface · <Month YYYY> · <X> min read · Written for <rol>

<Openingsscène, 2 tot 5 zinnen>

> **<De hoofdvraag letterlijk>**
> <Antwoordblok, 60 tot 90 woorden>

## <Vraag die de lezer stelt, met de entiteit erin>
<Eerste zin beantwoordt de vraag.> ...¹

[FLOWDIAGRAM] Stap (toelichting) → Stap (toelichting) → ...
*<Onderschrift dat de flow in één zin vertelt.>*

> **<Label, bijv. For IT and learning technology teams>**
> <Eén gedachte.>

## Frequently asked questions

**<Vraag zoals hij ingetypt wordt?>**
<Yes./No./De stelling.> <Twee tot vier zinnen.>

## References

1. <Auteur/uitgever>. (<jaar>). <Titel>. <Uitgever>. [Key finding: <het feit dat in de tekst staat>]
```

- Figuren (`[FLOWDIAGRAM]`, `[FIGUUR: ...]`) beschrijf je als tekst met inhoud en onderschrift. `blog-builder` of `marketing-creatives` maakt er een afbeelding van.
- Superscript ¹ ² in de tekst verwijst naar het nummer in References. Elke referentie draagt een feit in de tekst, geen opvulling.
- Bestandsnaam: volgend nummer plus slug, bijvoorbeeld `32-<slug>.md`.
- Leestijd = woorden gedeeld door 230, afgerond.
- Links in de lopende tekst als markdown-link met beschrijvende ankertekst. `blog-builder` zet ze om.
- Een tabel als markdown-tabel. `blog-builder` maakt er een navy-zebratabel van, hoogstens vier kolommen.

### 6. Zelfcheck (alle vier, voor je oplevert)

**A. Claims.** Elke zin over Eduface staat in `Platform/product.md`. Niets uit de lijst "claims die op de live blogs staan maar niet in product.md" in `stijl.md`. Elk extern getal heeft een bron met jaar die je zelf gezien hebt. Elke datum uit regelgeving is getoetst tegen de huidige stand.

**B. Stem.** Draai deze check en haal elke treffer weg of verdedig hem:

```bash
grep -n -i -E "delve|landscape|crucial|pivotal|transformative|seamless|robust|leverage|navigate|realm|tapestry|foster|holistic|empower|unlock|game.chang|cutting.edge|genuinely|it's worth noting|in today's|not just .*, (it's|but)|in conclusion|ultimately,|—" <bestand>
```

Lees daarna de opening en de eerste zin van elke H2 hardop: klinkt het als een collega die het uitgezocht heeft, of als een folder?

**C. SEO en GEO.**
- [ ] Antwoordblok bovenaan beantwoordt de hoofdvraag in 60 tot 90 woorden, met de entiteiten bij naam
- [ ] Elke H2 zegt zelf de inhoud en opent met een zin die los klopt
- [ ] Minstens één tabel waar er iets te vergelijken valt
- [ ] Minstens één informatiewinst-blok (eigen meting, uitgewerkt voorbeeld, checklist, testopzet)
- [ ] Eduface en het LMS bij naam in citeerbare zinnen, niet "it"
- [ ] SEO-titel onder 60 tekens met het onderwerp vooraan; meta 140 tot 160
- [ ] Twee of drie interne links, naar de hub en zijartikelen
- [ ] FAQ met vragen die de koppen niet al beantwoorden
- [ ] Geen woordtarget-opvulling: elke alinea voegt iets toe

**D. Eerlijkheid.** Staat er ergens waar AI of Eduface tekortschiet, of waar een alternatief beter past? Zo nee, dan leest het als een folder. De referentieblogs danken hun geloofwaardigheid aan precies die zinnen.

### 7. Lever

- Het pad naar het bestand.
- **Per niet-vanzelfsprekende keuze één regel waarom** (hoek, titel, waarom deze tabel, waarom dit getal). Dat is standaard, zie `schrijven`.
- **Open punten**: claims die je wilde gebruiken maar niet mocht, bronnen die je niet kon openen, datums die getoetst moeten worden.
- Geen Artifact, tenzij Dante erom vraagt (`.claude/rules/output-format.md`).

## Een bestaande blog verversen

Trigger: "update deze blog", "klopt deze nog", of een `review_by`-datum die verstreken is.

1. Lees de huidige versie (markdown-bron, of de live pagina als die bereikbaar is).
2. Toets elke datum, elk getal en elke claim tegen `bronnen.md`, `product.md` en de huidige stand.
3. Lever een lijst van wat verandert, met reden. Pas na akkoord herschrijven.
4. Na een inhoudelijke wijziging: "Last updated" met datum en in één zin wat er veranderde. Alleen de datum veranderen zonder nieuwe inhoud doen we niet.

## Feedback

Feedback van Dante op een blog volgt `.claude/rules/feedback.md`:
- Een losse opmerking is een correctie op dit ene artikel. Pas aan en log hem in `LEERPUNTEN.md`.
- Twee keer hetzelfde: zeg het en stel een regel voor, met de tekst erbij.
- Pas na akkoord verandert `stijl.md` of deze `SKILL.md`, en dat meld je.

Feedback op een blog verandert niet de stem van mails of LinkedIn, en andersom.

## Done

- Brief rond, en getoetst aan de prioriteit
- Gecheckt op een bestaande blog met dezelfde zoekintentie
- Poort gehaald, of expliciet overgeslagen op Dante's woord
- Concept in `markdown-sources/` met volledige frontmatter
- Alle vier de zelfchecks gedaan, grep schoon of verdedigd
- Opgeleverd met toelichting en open punten
