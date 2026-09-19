# Framer-audit + migratieplan (eduface.me)

Op basis van een volledige uitlezing van je live Framer-project (juni 2026). Dit is het bewijs waarom de site nu inconsistent voelt, plus het schone systeem dat we ervoor in de plaats zetten.

## Wat er nu staat (en waarom het rommelt)

**Knoppen: 5 losse componenten voor in feite 1 ding.**
`Knoppen oud`, `Buttion primary` (typo), `Button Link`, `Button`, `Buttion primary`. Eén heet letterlijk "oud", één heeft een typefout. Dit is dé bron van knop-inconsistentie. Ook 2 componenten heten allebei `Animaties`.

**Kleuren: platte lijst, geen systeem.**
- Geen lagen (primitief/semantisch), gewoon 15 losse kleuren door elkaar.
- NL/EN-mix in namen: `Wit`, `Licht grijs`, `Donker grijs`, `Blauw & grijs` naast `Accent`, `BG`, `border light`, `Hover BG`.
- Duplicaat: `/Linear` is exact dezelfde kleur als `/Primary` (rgb 0,35,51).
- De grijzen (200, 158) zijn neutraal grijs, niet navy-getint. Daardoor oogt het iets goedkoper/vlakker dan een samenhangend palet zoals Default.
- Goede basis is er wel: `/Primary` = navy #002333 en `/Accent` = groen #00E075 kloppen met je merk.

**Tekststijlen: geen schaal, gemengde eenheden.**
- Maten staan willekeurig: 3.09rem, 2.6rem, 2.37rem, 2.09rem, 1.5rem. Geen modulaire ladder.
- Eenheden door elkaar: fontSize in rem én px, lineHeight in em én px. Inconsistentie ingebakken.
- Koppen deels League Spartan (`New H1/H2/H3`), deels Inter (`Blog H2`, `CTA Title`, `Box Title`). Twee koppenstemmen.
- Naamgeving waaiert uit: `New H1`, `Blog H1`, `Hero H1 White`, `H3 sm`. Het woord "New" verraadt dat er ook oude waren.
- Alignment zit ín de stijl gebakken (`Description` = center, `Body 16` = left voor dezelfde maat). Dat verdubbelt je stijlen onnodig.

## Het nieuwe systeem (wat we aanmaken)

### Color Styles, in 2 lagen (folders = de tiers)
**`/Primitief/`** (ruwe waarden, veranderen bijna nooit)
- Navy 950 #002333 · Navy 900 #0A2C3B · Navy 700 #2C4A57 · Navy 500 #5B7480 · Navy 300 #A9BCC4 · Navy 200 #CDD9DE · Navy 100 #E7EEF0 · Navy 50 #F3F7F8
- Groen 500 #00E075 · Groen 600 #00B85F · Groen Deep #007B54 · Wit #FFFFFF

**`/Semantisch/`** (dit pas je toe, niet de ruwe kleur)
- Licht: Background (wit) · Surface (Navy 50) · Foreground (Navy 950) · Foreground Soft (Navy 500) · Border (Navy 100) · Border Strong (Navy 200) · Primary (Navy 950) · Primary Text (Wit) · Accent (Groen 500) · Accent Text (Navy 950)
- Donkere secties: Background Inverse (Navy 950) · Surface Inverse (Navy 900) · Foreground Inverse (Wit) · Foreground Inverse Soft (wit 62%) · Border Inverse (wit 12%)

### Text Styles, op één modulaire schaal
**`/Display/`** (alle koppen League Spartan, één stem)
- XL 4.5rem · L 3.5rem · M 2.75rem · S 2rem · XS 1.5rem (lh + tracking vast per trap)

**`/Text/`** (Inter)
- Lead 1.25rem · Body 1rem · Body Medium 1rem · Small 0.875rem · Eyebrow 0.75rem (uppercase, tracking) · Button 0.875rem

Alignment niet meer in de stijl; per node zetten. Scheelt de helft van de stijlen.

### Componenten: 5 knoppen → 1
Eén `Button`-component met varianten (Primary / Secondary / Ghost) + maat + optioneel icoon. De rest (Card, Badge, Section, Hero, Nav, Footer, Testimonial, Feature grid) volgt hetzelfde patroon.

## Migratie (veilig, niks breekt)
1. **Additief aanmaken.** Nieuwe styles + componenten ernaast. Bestaande pagina's blijven naar de oude verwijzen, dus de live site verandert niet.
2. **Pagina voor pagina omzetten** naar de nieuwe styles/componenten, beginnend bij de belangrijkste (home, product, pricing).
3. **Oude opruimen.** Pas als alles over is, verwijderen we de oude styles en de 4 overbodige knop-componenten.
4. **Audit-check.** Ik kan daarna het project scannen op elk element dat géén gedeelde stijl gebruikt.

## Mapping oud → nieuw (kort)
- `/Primary` → `/Semantisch/Foreground` + `/Semantisch/Primary` (zelfde navy)
- `/Linear` (duplicaat) → vervalt, wordt `/Semantisch/Primary`
- `/BG`, `/Blauw & grijs`, `/Hover BG` → `/Semantisch/Surface`
- `/Licht grijs`, `/Donker grijs` → `/Primitief/Navy 300` / `Navy 500` (navy-getint)
- `/border light`, `/border dark` → `/Semantisch/Border`, `/Semantisch/Border Inverse`
- `New H1/H2/H3` → `/Display/L`, `/Display/M`, `/Display/XS`
- `Blog H1/H2` → `/Display/S` + `/Display/XS` (League Spartan, niet meer Inter)
- `Description`, `Body 16` → `/Text/Body` (alignment per node)
