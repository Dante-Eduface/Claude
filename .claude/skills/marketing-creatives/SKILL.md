---
name: marketing-creatives
description: Maakt on-brand Eduface marketingmateriaal — afbeeldingen, banners, ads, social visuals. Trigger wanneer Dante zegt "maak een afbeelding/banner/visual", "genereer een creative", "maak een ad", "maak een visual voor [project]", of een logo/product-shot in een visual wil. Voor slides en decks: gebruik de skill `pitch-deck`. Anchored op de Eduface brand-assets, het design-system en de render-pipeline. Zorgt dat elke creative klopt qua kleur, font, logo en stijl, en op de juiste plek wordt opgeslagen.
---

# Marketing Creatives

Maakt visueel marketingmateriaal voor Eduface dat altijd on-brand is. Output: **statische beelden** (ads, banners, social, covers). Slides en decks gaan via de skill `pitch-deck`, die heeft een eigen bouwmachine en levert bewerkbare pptx. De generatie zelf gaat al goed — deze skill borgt consistentie (kleur, font, logo, stijl) en routing (waar het bestand belandt).

## Voor je begint: laad de basis
Lees altijd eerst, in deze volgorde:
1. `Design/Merk/brand-guidelines.md` — kleuren, fonts, logo-regels, toon.
2. `Design/Design system/tokens.css` — exacte design-tokens (kleur, type-schaal, radius, schaduw). **Verzin nooit losse waarden, lees ze hier.**
3. `reference.md` (in deze skill-folder) — slide-designpatronen, render-methodes, en gotchas.

Brand-assets (logo's, product-shots, fonts) staan centraal in `Design/Merk/`. Gebruik altijd die, niet kopieën uit een project.

## Merk-anker (snel)
- **Kleuren:** navy `#002333` (primair/tekst), groen `#00E075` (accent/highlight), leesbaar groen `#007B54` op wit. Volledige set: `tokens.css`.
- **Fonts:** League Spartan (koppen/display), Inter (body). Niet Roboto.
- **Logo:** `Design/Merk/logos/logo_navy.png` (op licht) + `logo_white.png` (op navy/donker). Niet roteren/stretchen/herkleuren, houd clear space.
- **Product-shots:** `Design/Merk/product/` (app, grading, criteria).
- **Toon:** casual, menselijk, plain taal, geen hype, geen em-dashes (`.claude/rules/communication-style.md`).

## Waar het bestand heen gaat (routing — belangrijk)
Volg de creatives-folder conventie:
- **Projectgebonden** (bv. banner voor de HS webinar) → `projects/<project>/creatives/` (maak die map aan als die nog niet bestaat).
- **Los / algemeen** (bv. Google Maps banner, test-render) → top-level `creatives/`.
- **Paid ads** blijven in `GTM/Campaigns/paid-ads/` — die structuur niet verplaatsen.

## De loop
```
1. SCOPE    wat, welk formaat/afmeting, projectgebonden of los? (1 vraag max, anders gewoon doen)
2. BASIS    lees brand-guidelines + tokens.css + reference.md, pak assets uit Design/Merk/
3. KIES     statisch beeld -> PIL of HTML->PNG (zie reference.md) | slide/deck -> stop, gebruik `pitch-deck`
4. BOUW     on-brand: navy+groen, League Spartan/Inter, echt logo, tokens-waarden
5. RENDER   naar PNG op de juiste afmeting
6. ROUTE    sla op volgens de routing-regel hierboven
7. TOON     laat Dante het resultaat zien, vraag of er een variant/aanpassing moet
```

## Twee render-methodes (detail in reference.md)
- **PIL / Python** — pixel-perfecte ads/banners met exacte controle. Werkend voorbeeld: `GTM/Campaigns/paid-ads/creatives/render_png.py` (helpers voor cards, schaduw, logo, glow, tekst-wrap, multi-formaat export).
- **HTML → PNG** — rijkere layouts, slides en decks. Schrijf HTML met de design-tokens, render naar beeld. Beste keuze voor slides.

## Slides / decks
- **Stijl = de Eduface-branded slides** (navy `#002333` + groen `#00E075`, clean witte/navy cards, eyebrow-tags, fluide 16:9 layout, logo's linksboven). NIET een instellings-template-stijl (bv. de BSU-slides waar dit op gebaseerd was).
- Patronen, slide-types en HTML-skeletten: zie `reference.md`.

## Done
- Creative is on-brand (juiste kleuren/font/logo, tokens gevolgd), op de juiste afmeting, opgeslagen op de juiste plek per de routing-regel, en aan Dante getoond.
