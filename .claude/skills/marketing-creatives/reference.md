# Marketing Creatives — Reference

Render-methodes, slide-designpatronen en gotchas. SKILL.md is het proces; dit zijn de details.

## Welke methode wanneer

| Output | Methode | Waarom |
|--------|---------|--------|
| Ad / banner met exacte pixels, multi-formaat (1:1, 9:16, 1.91:1) | **PIL / Python** | Pixel-controle, herhaalbaar, batch-export per formaat |
| Slide / deck | **HTML → PNG** | Layout, flex/grid, cards, fluide tekst — veel sneller dan PIL |
| Rijke social visual / cover met foto's, mockups, gradients | **HTML → PNG** | Makkelijker stylen dan in PIL |
| Snelle losse banner | Beide kan | Pak wat sneller af is voor de taak |

## Methode 1: PIL / Python

Werkend, geanker voorbeeld: `GTM/Campaigns/paid-ads/creatives/render_png.py`. Het bevat herbruikbare helpers — hergebruik ze, schrijf niet opnieuw:
- `head(size)` / `body(size)` — League Spartan / Inter laden uit `fonts/`.
- `card(...)`, `shadow(...)`, `glow(...)` — cards met schaduw en groene glow.
- `logo(...)` — plakt het witte logo, crop op bbox, schaalt op hoogte.
- `paste_img(...)` — product-shots met optionele browser-chrome.
- `wrap(...)`, `tblock(...)`, `justify(...)` — tekst-wrap en verticale verdeling.
- Kleur-constanten staan bovenin (NAVY, GREEN, TEAL, etc.) — exact de merkkleuren.

Afmetingen die het script al draait: 1080x1080 (1:1), 1080x1920 (9:16), 1200x628 (1.91:1).

Run: `python3 render_png.py` vanuit de map (heeft Pillow nodig). Fonts en assets leest het relatief uit `fonts/` en `assets/`. Voor nieuw werk: wijs naar de centrale `Design/Merk/fonts/` en `.../logos/` + `.../product/`, of kopieer de nodige files mee in de werkmap.

## Methode 2: HTML → PNG

Voorbeelden in de repo: `GTM/Campaigns/paid-ads/creatives/maps-cover-banner.html`, `.../assets/listing.html`.

Aanpak:
1. Schrijf een standalone HTML-bestand met inline CSS, op exacte slide-/canvas-afmeting (16:9 slide = 1280x720 of 1920x1080).
2. Gebruik de design-tokens uit `Design/System/core/tokens.css` (kleuren, type-schaal, radius, schaduw). Laad League Spartan + Inter via de Google Fonts `@import` die bovenin tokens.css staat.
3. Render naar PNG. Opties: een headless browser (Playwright/Chromium screenshot van de `.html`), of een bestaand screenshot-pad. Wacht tot fonts geladen zijn voor je schiet.

## Eduface slide-stijl (de stijl die Dante wil)

Gebaseerd op de Eduface-branded slides (navy + groen, clean cards). NIET de strakke instellings-template-stijl. Kenmerken:
- **Achtergrond:** licht (wit / `--color-ink-50` `#f3f7f8`) of navy-blok voor accent-slides. Subtiele groene dot-patronen mogen op cover/closing.
- **Logo's linksboven:** Eduface + eventuele partner-logo's (bv. Jisc, universiteit) op een rij.
- **Titel:** League Spartan bold, navy, met soms één woord in groen (bv. "**Good** feedback requires", "Our **own** AI model").
- **Eyebrow-tags:** kleine pill-labels (groene of navy pill, bv. "Formative", "Open questions", genummerd "01 / 02 / 03").
- **Cards:** witte cards met subtiele schaduw (`--shadow-md`) en `--radius-2xl`, of navy cards met witte tekst voor contrast. Vaak 2- of 3-koloms grid.
- **Accent-balk onderaan:** brede groene of navy balk met een kernzin (bv. "That is why we built Eduface").
- **Bron-voetnoten:** klein, gedempt (`--color-muted`), met jaartal — past op de "claims need sources" regel.

### Veelgebruikte slide-types (uit de deck)
- **Cover** — groot logo + partner-logo's, titel, naam/rol/datum, dot-patroon.
- **3-card intro** — "X requires" met 01/02/03 genummerde witte cards + accent-balk eronder.
- **Two-column proof** — links bullets/steps, rechts een mockup/visual (bv. essay + feedback-bubbles).
- **6-card grid** — domeinen/features in 2x3 met icoon + label + logo's.
- **Comparison bars** — gelabelde balken die Eduface afzetten tegen alternatieven.
- **Split two-mode** — navy card vs witte card naast elkaar (bv. Formative vs Summative), elk met goal-balk onderaan.
- **Process / flow** — genummerde stappen met groene cijfer-badges, verbindingslijnen.
- **Product mockup** — UI-screenshot in een card met browser/app-chrome.
- **Pricing / licensing** — tekstkolom links, product-card rechts.
- **Closing** — logo's + "Thanks for joining!" + dot-patroon.

### HTML-skelet (slide, 16:9)
```html
<!doctype html><html><head><meta charset="utf-8">
<style>
  @import url("https://fonts.googleapis.com/css2?family=League+Spartan:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap");
  :root{ --navy:#002333; --green:#00e075; --green-deep:#007b54; --ink-50:#f3f7f8; --muted:#5b7480; }
  *{margin:0;box-sizing:border-box}
  .slide{width:1280px;height:720px;background:var(--ink-50);font-family:Inter,sans-serif;color:var(--navy);padding:64px;position:relative}
  .logos{display:flex;gap:20px;align-items:center;margin-bottom:48px}
  h1{font-family:"League Spartan";font-weight:700;font-size:64px;letter-spacing:-.02em;line-height:1}
  h1 .hl{color:var(--green)}
  .grid{display:flex;gap:24px;margin-top:48px}
  .card{flex:1;background:#fff;border-radius:20px;box-shadow:0 4px 16px rgba(0,35,51,.08);padding:32px}
  .card.dark{background:var(--navy);color:#fff}
  .eyebrow{font-weight:700;font-size:14px;color:var(--green-deep);text-transform:uppercase;letter-spacing:.04em}
  .bar{position:absolute;left:64px;right:64px;bottom:48px;background:var(--green);color:var(--navy);
       font-family:"League Spartan";font-weight:700;font-size:28px;text-align:center;padding:24px;border-radius:16px}
  .src{position:absolute;left:64px;bottom:20px;font-size:13px;color:var(--muted)}
</style></head>
<body><div class="slide">
  <div class="logos"><img src="Design/Merk/logos/logo_navy.png" height="44"></div>
  <h1><span class="hl">Good</span> feedback requires</h1>
  <div class="grid">
    <div class="card"><div class="eyebrow">01</div><h3>Clear criteria</h3><p>...</p></div>
    <div class="card"><div class="eyebrow">02</div><h3>Relevant feedback</h3><p>...</p></div>
    <div class="card"><div class="eyebrow">03</div><h3>Consistency</h3><p>...</p></div>
  </div>
  <div class="bar">That is why we built Eduface</div>
</div></body></html>
```

## Gotchas
- **Groen op wit:** fel groen `#00E075` is slecht leesbaar als tekst op wit. Gebruik voor groene tekst op licht het diepere `#007B54` (`--color-green-deep`). Fel groen is voor accenten, highlights, pills en balken.
- **Logo-keuze:** navy logo op licht, wit logo op navy/donker. Nooit herkleuren of stretchen.
- **Fonts laden:** bij HTML→PNG, wacht tot de webfonts geladen zijn voor de screenshot, anders valt het terug op een systeemfont.
- **Tokens, geen losse waarden:** kleur/radius/schaduw/type uit `tokens.css`. Niet zelf hex-codes verzinnen.
- **Claims:** elke harde claim (cijfer, %) krijgt een bron met jaartal in een voetnoot (regel: claims need sources). Verzin geen Bath Spa-metrics.
- **Plain taal:** koppen en copy in gewone spreektaal, geen hype, geen em-dashes.
- **Afmeting eerst vaststellen:** weet je het kanaal/afmeting niet, vraag of pak een veilige default (slide 1280x720; social 1:1 1080x1080; story 9:16 1080x1920; LinkedIn single image 1.91:1 1200x628).
