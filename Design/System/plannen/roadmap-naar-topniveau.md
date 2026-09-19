# Roadmap naar een top-design-system (Default-niveau)

Doel: niet je huidige site oplappen, maar een logisch, overzichtelijk systeem opbouwen dat fris voelt en consistent blijft over de hele website. Gebaseerd op research (zie bronnen onderaan) + de Default-analyse.

---

## 1. Wat een site écht naar "dat niveau" tilt
Niet de tool. Niet mooiere prompts. Drie dingen:
1. **Eén bron van waarheid.** Elke kleur, maat en font komt uit een vastgelegd systeem. Niks wordt per pagina opnieuw verzonnen. Dit is precies wat Default heeft en Replit/jouw huidige site mist.
2. **Een paar systemen i.p.v. losse keuzes.** Een type-schaal, een spacing-schaal, een kleurensysteem. Je kiest niet "welke grootte hier", je pakt de volgende trap op de ladder.
3. **Discipline (governance).** De regel: nieuwe waarde nodig? Voeg eerst een token toe, gebruik die daarna. Een afwijking is een bug, geen uitzondering.

Fris voelt het door beperking: weinig kleuren (1 accent dat iets betekent), strakke typografie, veel witruimte, het product tonen i.p.v. beschrijven.

## 2. Het fundament: design tokens in lagen
De industriestandaard is een token-systeem in tiers. Voor een soloteam zijn **2 lagen** genoeg (de 3e is enterprise-overkill):

- **Primitieven** = ruwe waarden. `navy-950 = #002333`, `green-500 = #00E075`. Veranderen bijna nooit.
- **Semantisch** = betekenis. `background`, `foreground`, `primary`, `accent`, `border`. Dit pas je toe in het ontwerp, niet de ruwe kleur.

Waarom de semantische laag het belangrijkst is: daar leg je vast *waarom* een waarde bestaat. Verander je later het merk, dan wijs je de semantische token naar een andere primitief en de hele site verandert mee. (Bron: token-tier research.)

Dit staat al uitgewerkt in `tokens.css`. Dat bestand is je canonieke spec, ongeacht de tool.

## 3. De systemen (de ladders)
- **Type-schaal:** modulair, gebouwd op een ratio, niet willekeurig. Display-trappen (League Spartan) + tekst-trappen (Inter). Line-height en tracking liggen vast per trap.
- **Spacing:** 8pt-grid. Alles is een veelvoud van 8 (8, 16, 24, 32, 48, 64...). Geeft vanzelf ritme en uitlijning. (Geldt voor spacing/maten, niet voor type.)
- **Radius:** vaste schaal (6/8/10/12/20px + pill). Per componenttype één radius.
- **Kleur:** near-monochroom (navy + grijstinten) met groen als enige accent.
- **Schaduw:** 2-3 subtiele niveaus, niet meer.

## 4. Van tokens naar pagina's (het 3-lagen model)
1. **Tokens** (kleur/type/spacing/radius) — het fundament.
2. **Componenten** — knop, card, badge, sectie, hero, nav, footer, testimonial. Eén keer bouwen met varianten (primair/secundair, maten) en eigenschappen (label, icoon). Wijzig de bron, alle instanties updaten.
3. **Patronen/templates** — pagina's samengesteld uit componenten. Nieuwe pagina = bouwstenen combineren, niks from scratch.

Bouw componenten **organisch**: maak je eerste pagina, en zodra je iets hergebruikt, maak er meteen een component van. Niet vooraf 50 componenten ontwerpen.

## 5. Architectuurkeuze voor Eduface
Je houdt Framer als CMS. Dan is dit de juiste opzet:

**Bron van waarheid = Framer Styles, aangedreven door Claude Code.**
- Framer heeft dit al ingebouwd: **Color Styles + Text Styles = je tokens**, **Components met varianten = je componentlaag**. Wijzig een stijl en de hele site verandert mee. Precies het 3-lagen model.
- Claude Code (ik) doet via de Framer-koppeling het zware werk: stijlen aanmaken, componenten bouwen, pagina's opzetten, en de site auditen op afwijkingen.
- Folderstructuur in Framer mirrort de tiers: `/Primitief/...` en `/Semantisch/...` voor kleur, `/Display/...` en `/Tekst/...` voor type.

**Waarom niet een losse Next.js-site:** dat wordt een tweede wereld naast Framer. Twee plekken om te onderhouden = meer inconsistentie, niet minder. Code is rigoureuzer, maar voor een marketingsite met één bouwer weegt dat niet op tegen de versnippering. Eén wereld (Framer) met een streng systeem erin wint.

**Eerlijk over de grens:** Framer Styles kennen geen echte aliasing (een semantische stijl die naar een primitief verwijst zoals in code). In Framer maak je de stijlen die je toepast (de semantische), met de waarden uit de spec, en de tiers leven in de folderstructuur + dit document. Het effect (één plek wijzigen) blijft.

## 6. Governance: zo blijft het consistent
- **Regel:** bouw alleen met bestaande styles/componenten. Nieuwe waarde nodig? Eerst token toevoegen.
- **Audit:** ik kan het hele Framer-project uitlezen en elk element markeren dat géén gedeelde stijl gebruikt (de inconsistentie-jager). Zo trek je consistentie over de bestaande pagina's.
- **De spec leeft hier** in `Design/System/`. Bij elke nieuwe pagina lees ik die en blijf ik binnen het systeem.

## 7. Stappenplan
- **Fase 0 — Beslissen (kort):** licht of donker thema, type-schaal vastzetten, primaire knopkleur. (1 sessie)
- **Fase 1 — Tokens in Framer:** alle Color + Text Styles aanmaken volgens de spec, in tier-folders.
- **Fase 2 — Componentbibliotheek:** kerncomponenten met varianten + eigenschappen.
- **Fase 3 — Templates:** 2-3 paginatemplates (landing, product, blog) uit de componenten.
- **Fase 4 — Uitrol + audit:** nieuwe pagina's bouwen, bestaande pagina's op het systeem trekken.

## 8. Wat ik nodig heb van jou
- Je **Framer-project open** met de MCP-koppeling actief, zodat ik kan lezen en bouwen.
- **Fase 0-beslissingen** (paar keuzes, ik geef opties).
- Reviewen op het canvas terwijl ik bouw.

## Bronnen
- [Token tier system architecture](https://designsystemproblems.com/token-management/token-tier-system/)
- [Design tokens: complete guide (UXPin)](https://www.uxpin.com/studio/blog/what-are-design-tokens/)
- [Build a design system from scratch (UXPin, 7 stappen)](https://www.uxpin.com/studio/blog/build-a-design-system-from-scratch-in-7-steps/)
- [Framer: how to build a design system](https://launchnow.design/blog/framer-components-how-to-build-a-design-system)
- [The 8pt grid system](https://www.rejuvenate.digital/news/designing-rhythm-power-8pt-grid-ui-design)
- [Default.com analyse](../website-analyses/default-com-analyse.md)
