# Van niks naar een draaiende app in Eduface-stijl

Voor als Dante zegt: bouw een app, een tool, een dashboard, een agent-interface, iets voor mezelf. Volg dit, verzin geen eigen opzet.

Check eerst of `~/Projects/eduface-app` al bestaat (Next.js + Supabase, zie `STATUS.md` daar). Zo ja, bouw daarin verder in plaats van iets nieuws te beginnen.

## 1. Project

```bash
npx create-next-app@latest mijn-tool --typescript --tailwind --app --eslint
cd mijn-tool
npx shadcn@latest init
```

Bij `shadcn init`:
- **cssVariables: yes.** Verplicht, en achteraf niet meer te wijzigen. Zonder dit werkt de Eduface-mapping niet.
- baseColor maakt niet uit, die overschrijven we in stap 3.
- Sinds juli 2026 kiest shadcn standaard Base UI. Prima. Wil je Radix, dan `npx shadcn@latest init -b radix`.

## 2. Fonts

In `app/layout.tsx`:

```tsx
import { League_Spartan, Inter } from "next/font/google";

const display = League_Spartan({
  subsets: ["latin"], weight: ["400","500","600","700"], variable: "--font-display",
});
const sans = Inter({
  subsets: ["latin"], weight: ["400","500","600"], variable: "--font-sans",
});

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="nl" className={`${display.variable} ${sans.variable}`}>
      <body>{children}</body>
    </html>
  );
}
```

Dit is de goedkoopste ingreep met het grootste effect. shadcn draait standaard op de systeemfont; zodra Inter en League Spartan erin zitten, is de generieke look grotendeels weg.

## 3. Tokens

Kopieer `core/tokens.css` en `internal/tokens.css` uit dit design system naar `app/` in je project, en zet in `app/globals.css` bovenaan:

```css
@import "tailwindcss";
@import "./eduface-core.css";
@import "./eduface-internal.css";
```

Haal daarbij de regel `@import "tailwindcss";` uit de gekopieerde `eduface-core.css` weg (die staat nu in globals.css) en haal de regel `@import "../core/tokens.css";` uit `eduface-internal.css` weg. Verder niets wijzigen.

Kopieer, verwijs niet naar de Google Drive-map. Een app moet zelfstandig kunnen builden.

## 4. Componenten toevoegen

```bash
npx shadcn@latest add button input table dialog select badge card
```

Wil je dat ik componenten zelf kan opzoeken en installeren, zet dan eenmalig de MCP-server aan:

```bash
npx shadcn@latest mcp init --client claude
```

## 5. Controleren dat het klopt

Loop deze vijf langs voor je verder bouwt:

- Is de primaire knop **navy**, niet groen? Groen betekent status, niet "klik hier". Zie `core/regels.md`.
- Staan de koppen in League Spartan en de rest in Inter?
- Is de dichtheid van jou en niet van shadcn? Rijen 36px, controls 32px, panelpadding 16px. Zie `--row-h` en `--control-h`.
- Werkt het in dark mode? Die komt gratis mee, dus even omzetten en kijken of niets onleesbaar wordt.
- Gebruik je nergens `text-muted` voor gedempte tekst? Binnen `internal/` is `muted` een **vlakkleur** (shadcn-conventie). Gedempte tekst is `text-muted-foreground` of `--color-text-muted`.

## 6. Wat je hier niet doet

Een interne tool is geen marketingpagina. Niet meenemen uit `web/`:

- Geen hero, geen 72px-koppen, geen sectieritme van 96px.
- Geen CTA-taal ("Boek een demo", "Ontdek hoe"). Labels zijn beschrijvend.
- Geen social proof, geen logo-balken, geen overtuigingswerk.
- Geen scroll-animaties.

Wat je wel meeneemt uit `core/`: de kleuren, de fonts, de radius-schaal, en alle regels uit `regels.md` en `compositie.md`. Vooral de reflexen-lijst in `compositie.md` punt 12, want die vangt precies de generieke look af.
