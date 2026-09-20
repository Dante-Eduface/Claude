# Brief: bouw de site zo dat hij naar Framer kan

_Aangeleverd door Dante, 2026-08-14. Dit is bindend voor alles in deze map._

De site wordt straks overgezet naar Framer. Framer heeft **geen HTML/CSS/JS-import**: alles wordt handmatig nagebouwd als native Framer-nodes. Hoe dichter de build bij dit model blijft, hoe minder er bij de overzetting sneuvelt. Het doel is **nabouwen, geen herontwerp**.

---

## 1. Layout: alleen stacks en grids, geen absolute positionering

- Bouw alles als flex-column / flex-row of CSS grid. Absolute positionering **alleen bij bewuste overlap**.
- In Framer werken `left/right/top/bottom` **niet** op `position: relative` (anders dan in CSS). Ze werken alleen bij `absolute`/`fixed`, en dan moet je **beide assen pinnen**.
- Verticale ruimte tussen elementen: altijd via `gap` op de parent of `padding` op een wrapper. **Nooit via margins op de children.** Margins bestaan niet in het Framer-model.
- `gap` combineren met `space-between` / `space-around` / `space-evenly` wordt **niet ondersteund**. Kies één van beide.
- **Negatieve marges bestaan niet.** Een element dat breder is dan zijn tekstkolom: centreren via de parent en breedte zetten, niet via een negatieve offset.
- Full-width sections krijgen een `max-width` op de binnenwrapper (bv. 1080px). Alleen horizontale padding is niet genoeg.

## 2. Tekst

- Tekstnodes kunnen zelf **geen padding** hebben. Padding hoort altijd op de parent-container. Dus nooit `<p style="padding:...">`, maar wrappen.
- Buttons: horizontale padding 16-24px, verticale 4-12px. Cards: 8-16px.

## 3. Sizing

- Denk in drie rollen: `auto` (hug content), `100%` (vul bounded parent), `1fr` (vul resterende ruimte).
- Hoogtes: laat content de hoogte bepalen (`auto`). **Vaste pixelhoogtes om dingen gelijk te maken worden bij de overzetting weggegooid.**
- Grids: gebruik `minmax()`-achtige flexibele kolommen (min-width per kolom) in plaats van een vast kolomaantal. Vertaalt direct naar Framer's `gridColumnMinWidth`.
- Op mobiel wordt een 1-koloms grid in Framer een **verticale stack**, geen grid. Bouw hem zo dat dat kan.

## 4. Animatie (belangrijkste beperking)

Framer heeft native animatie die dit dekt:
- Transitions: spring (stiffness/damping/mass), spring-duration (duration/bounce), tween met cubic-bezier, inertia. Plus delay en stagger.
- Appear/enter/exit effects, scroll-triggered reveals, hover, tap, in-view.
- Variant-based interactie (menu open/dicht, toggles, tabs).
- Ingebouwde WebGL-shaders voor zware visuele effecten.

**Vermijden als je wil dat het overkomt:**
- GSAP, three.js, Lenis, Lottie, ScrollMagic, Locomotive. Framer-codecomponenten mogen alleen importeren uit `react`, `react-dom`, `framer`, `framer-motion`. Verder niets. (Er is een omweg via ESM-CDN-imports `https://jspm.dev/pkg@versie`, maar dat kost pagespeed en is fragiel.)
- Custom scroll-timelines, SVG path morphing, canvas-animaties. Die moeten alsnog als codecomponent, dus met dezelfde importbeperking.
- Gebruik `framer-motion` als je JS-animatie nodig hebt. Dat is het enige dat 1-op-1 meegaat.

## 5. Codecomponenten (als je toch custom React schrijft)

- Eén bestand, één default export, function-syntax, geen named exports.
- Root-element `position: relative`. `fixed` is verboden op de root.
- Alle `window`/`document`-toegang achter `if (typeof window !== "undefined")` (SSR).
- Geen `defaultProps`, geen build-step, geen config, geen NodeJS-types.

## 6. Wat Framer sowieso niet heeft

- Geen backend. Geen API-routes, geen server functions, geen database. Bouw geen serverlogica in.
- Geen globale custom CSS-file. **Tailwind-classes komen niet mee.** Styling moet per element uitdrukbaar zijn (kleur, border, radius, shadow, spacing). Houd het simpel en meetbaar.
- Geen eigen routing. Pagina's zijn Framer-pagina's. Dynamische pagina's (blog) via Framer CMS.
- Geen custom response headers, rewrites/proxy of static/well-known files via de agent.

## 7. Kleur en type

- Werk met een **beperkte set kleurtokens** (light + dark waarde per token), niet met tientallen losse hex-waardes per element. Die tokens worden Framer color styles.
- Zelfde voor typografie: definieer een handvol tekststijlen (H1/H2/H3/body/small) met expliciet font-weight. Niet per element een eigen size/weight.

---

**Kortom:** een statische, stack-gebaseerde marketingsite met framer-motion voor beweging, een kleine tokenset voor kleur en type, en geen enkele externe animatielibrary.
