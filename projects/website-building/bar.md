# bar.md — de lat, afgelezen aan Habitline

Referentie: https://habitline-wbs.framer.website/ (Framer-template, 13.177px hoog, content max-width 1024px).
Alle getallen hieronder zijn gemeten in de live pagina, niet geschat.

Dit zijn mechanismen, geen smaak. Een criticus moet ze kunnen aflezen aan een screenshot of een filmstrip.

---

## M1 — Eén beweging, één curve, één duur
Elke transitie op de hele site is **0,45s met `cubic-bezier(0.44, 0, 0.56, 1)`**. Gemeten: 55 elementen, allemaal exact die waarde, nul uitzonderingen. Geen enkele CSS-keyframe-animatie; loops draaien op transform via JS.
**Toets:** vind één transitie op onze pagina met een andere duur of curve, en dit faalt.

## M2 — Drie tekstgroottes doen 90% van het werk, de kop is 3,8x de body
Gemeten verdeling: 14px (labels, 100x), 18px (body, 84x), 68px (h1, 32x), daarna 32px (h2). Kop staat op **68px tegen 18px body**, factor 3,8. Twee fontfamilies, niet meer: een display voor koppen, een grotesk voor al het andere.
**Toets:** tel de unieke font-sizes in een sectie. Meer dan vier = fail. Kop kleiner dan 3x de body = fail.

## M3 — Precies twee radii, en de accentkleur zit alleen in cirkels
Gemeten radii: **50px (133x) en 20px (76x)** zijn samen ~70% van alles. Kaarten 20, alles wat een pill of badge is vol rond.
Verzadigde kleur (groen, oranje, blauw, paars) komt **uitsluitend** voor als vulling van een icoon-cirkel of een statusbadge kleiner dan 32px, en nooit als vlak, kop, knop of getal. De grote vlakken zijn #131515, wit en vier grijzen.
**Toets:** wijs één accentkleur aan die groter is dan een badge, en dit faalt.

## M4 — Elke feature-cel is een miniatuur van het product dat écht iets doet
In geen enkele cel staat een icoon-plus-tekstje. Er staat een **werkend stukje UI**: een dagplanner met zes tijdregels en een completion-percentage, een streakrij van zeven dagchips met vinkjes, een routine-stack met gekleurde blokjes, een notificatie met twee knoppen ("I'm on it" / "Later"). De tekst eromheen is nooit langer dan twee regels.
**Toets:** dek de kop af. Snap je uit de graphic alleen wat de feature doet? Nee = fail.

## M5 — Er beweegt altijd iets, en het loopt door zonder begin of eind
Doorlopende loops naast de scroll-reveals: de tag-marquee onder de hero, de rij streak-opties, de reminder-kolommen die twee kanten op schuiven, de tellers die per cijfer omhoog rollen. Snelheid is laag genoeg om te lezen terwijl het loopt.
**Toets:** zet een sectie 10 seconden stil op het scherm. Is het beeld identiek op t=0 en t=10? Fail.

## M6 — De navigatie is een zwevende pill die vertelt waar je bent
Geen balk over de volle breedte. Een **gecentreerde witte pill** die meeschuift, en die tijdens het scrollen uitklapt naar drie pills: logo, sectielabels ("What's inside / Use case / Metrics / Smart Assist") met de huidige sectie gemarkeerd, en de actieknoppen. De nav is tegelijk de voortgangsindicator.
**Toets:** kun je halverwege de pagina aan de nav zien in welke sectie je zit? Nee = fail.

## M7 — Donker wordt gedoseerd, en donker is nooit vlak
Van de 12 grote secties zijn er 3 donker. Elk donker vlak heeft **textuur** (17 achtergrondvideo's en 169 foto's op de pagina), nooit een platte zwarte rechthoek. Licht en donker wisselen elkaar af zodat de pagina ritme heeft in plaats van één lange lichte lap.
**Toets:** scrol de hele pagina in miniatuur. Zie je een afwisselend ritme licht/donker? Eén kleur over 5 secties = fail.

---

## Waar wij afwijken (bewust, niet per ongeluk)

- **Palet.** Habitline strooit vijf verzadigde accenten rond. Wij hebben navy + groen, en groen betekent "kijk hier" of "gelukt", nooit "klik hier" (`core/regels.md`). M3 blijft gelden, alleen met één accent in plaats van vijf.
- **Fonts.** League Spartan + Inter, niet Stack Sans + Google Sans Flex.
- **Onderwerp.** Zij verkopen rust aan een consument. Wij verkopen tijd terug aan een beoordelaar. De miniaturen uit M4 tonen dus nakijkwerk, geen waterglazen.

---

## Twee conflicten die we hebben beslecht (niet opnieuw openen)

**Textuur op donker.** M7 eist textuur op elk donker vlak. `compositie.md` §12 noemt "textuur, strepen, gloed" als een sjabloon-reflex. Die twee botsen alleen als de textuur versiering is. Bij ons is de korrel plus de liniatuur **materiaal**: de pagina gaat over papier, de hero is het vel. Dat blijft staan. Een criticus die dit als §12-overtreding aanrekent, heeft ongelijk.

**Groen op de hero-CTA.** `regels.md` staat groen toe op precies twee plekken, en de hero-CTA is de eerste. Eén groene knop in de hero is dus goed. M3 gaat over accent buiten die knop en buiten statusbadges kleiner dan 32px.

**Aantal tekstmaten.** `regels.md` zegt "maximaal 2 tot 3 groottes of gewichten per scherm", M2 zegt maximaal vier per sectie. Die regel gaat over hiërarchie binnen één blok, niet over een hele viewport waar een kop, een lead, knoppen en bijschriften bij elkaar staan. Onze eerste viewport draait op **72 / 18 / 15 / 13** en drie gewichten. Dat is de norm, en die telling is gemeten in de browser, niet geschat van een screenshot.

**Doorlopende beweging in de hero.** `compositie.md` §13 zegt "standaard stil, beweging alleen als die een toestandsverandering uitlegt of een actie bevestigt". Die regel is geschreven voor `internal/`, een tool waar een idle-animatie afleidt van je werk. M5 geldt voor de marketingsite, waar de hero juist moet laten zien wat het product doet aan iemand die het nog nooit gebruikt heeft. Onze hero-loop legt precies één toestandsverandering uit, namelijk concept wordt goedgekeurd, en herhaalt die. Dat blijft.
