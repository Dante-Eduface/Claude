# Framer-beperkingen (marketingsite)

**Lees dit alleen als Dante expliciet zegt dat iets naar Framer gaat.** De standaard bouwmanier is React met Tailwind (zie `components.md`), dat is sneller. Framer is de uitzondering, geen uitgangspunt.

Framer kan geen HTML/CSS/JS importeren, alles wordt nagebouwd als native nodes. Gaat iets naar Framer, dan moet het binnen dit model passen, anders is de overzetting een herontwerp in plaats van nabouwen.

Stond eerder alleen in memory en in `Design/Website/website-building/FRAMER-BRIEF.md`. Hier vastgelegd zodat het meekomt met het design system.

## Layout
- Alleen flex-stacks en grids. Absolute positionering alleen bij bewuste overlap, en dan beide assen pinnen. In Framer werkt left/top niet op `position: relative`.
- **Nooit margins op children.** Die bestaan niet in Framer. Ruimte via `gap` op de parent of padding op een wrapper. Geen negatieve marges.
- `gap` niet combineren met `space-between`.
- Tekstnodes kunnen zelf geen padding hebben. Padding hoort op de parent.
- Hoogtes op auto. Geen vaste px-hoogtes om dingen gelijk te trekken.
- Grids met `minmax()` of min-width per kolom, niet met een vast kolomaantal.

Deze eerste regel valt samen met `core/compositie.md` punt 7 (elke witruimte heeft één eigenaar). Wat daar een kwaliteitsregel is, is hier een harde bouwbeperking.

## Styling
- Geen globale custom CSS-file, geen Tailwind-classes. Styling moet per element uitdrukbaar zijn.
- Beperkte set kleurtokens (light plus dark per token) en een handvol tekststijlen (H1/H2/H3/body/small). Niet per element een eigen hex of maat.
- Framer Styles zijn de tokenlaag: Color Styles en Text Styles zijn de tokens, Components met varianten zijn de componentlaag. Zie `roadmap-naar-topniveau.md`.

## Code en animatie
- Alleen wat Framer native heeft, plus **framer-motion** als enige JS-library. Geen GSAP, three.js, Lenis, Lottie, ScrollMagic, Locomotive.
- Codecomponenten mogen alleen importeren uit react, react-dom, framer, framer-motion.
- Geen backend, geen eigen routing.

## Wat dit betekent voor de andere bestanden
`web/components.md` is Tailwind/JSX en dat blijft zo, want dat is de snelste manier om te bouwen. Gaat een component naar Framer, dan lees je hem als **specificatie**: welke tokens, welke maten, welke states. De ruimte staat daar al als `gap` op de parent, dus die vertaalt één op één naar Framer-stacks.

shadcn/ui werkt niet in Framer, want er is geen Tailwind-buildstap. Zie `internal/components.md`.

## Blogs en covers
Blogs bouw je met de `blog-builder` skill, niet met de hand. De covervoorschriften (flat icon op licht `#f3f7f8`, navy outlines, groene vlakken, 4:3) staan daar en zijn leidend.
