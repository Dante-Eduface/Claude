# Interne tools en agent-UI's

Voor wat je voor jezelf bouwt: dashboards, agent-interfaces, werkschermen. Andere regels dan de website, want je kijkt er uren naar in plaats van 8 seconden.

## Wat anders is dan web
- **Dichtheid boven lucht.** Rijen van 36px, controls van 32px, panelpadding 16px. Geen sectieritme van 96px.
- **Geen overtuigingswerk.** Geen hero, geen CTA-taal, geen social proof. Labels zijn beschrijvend, niet verkopend.
- **Status is de hoofdkleur-functie.** Groen betekent hier klaar of goed, niet "klik hier". Zie de status-tokens in core.
- **Toetsenbord eerst.** Alles wat je vaak doet moet zonder muis kunnen.
- **Dark mode telt mee.** De `.dark` mapping staat in `tokens.css` en is niet optioneel.

## shadcn/ui als basis

Gebruik shadcn voor de standaardcomponenten. Het is geen library maar broncode die je in je repo kopieert: MIT-licentie, geen account, geen abonnement, geen runtime-dependency op shadcn zelf ([LICENSE, 2023](https://github.com/shadcn-ui/ui/blob/main/LICENSE.md)).

**Opzetten:**
```bash
npx shadcn@latest init
```
Daarna per component:
```bash
npx shadcn@latest add button table dialog
```

**Belangrijke keuzes bij init, die je achteraf niet meer kunt wijzigen:** `style` en `cssVariables` liggen na init vast in `components.json`. Zet `cssVariables` op `true`, anders werkt de merkmapping hieronder niet ([shadcn docs, components.json](https://ui.shadcn.com/docs/components-json)).

**Sinds juli 2026** is Base UI de standaard primitive-laag in plaats van Radix. Radix blijft ondersteund via `npx shadcn@latest init -b radix` ([changelog, 2026](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default)).

**MCP-server**, zodat ik componenten direct kan opzoeken en installeren:
```bash
npx shadcn@latest mcp init --client claude
```
([shadcn docs, MCP](https://ui.shadcn.com/docs/mcp))

## Hoe je voorkomt dat het generiek wordt

Dit is een reëel risico, geen theoretische zorg: apps zien er identiek uit omdat iedereen dezelfde shadcn-defaults draait. De oplossing is niet shadcn vermijden maar de merklaag echt zetten.

1. **Importeer `internal/tokens.css`.** Daar staat de mapping van shadcn's variabelen (`--primary`, `--accent`, `--ring`, `--sidebar-*`, `--chart-*`) op de Eduface-kleuren. Elke shadcn-component komt er dan meteen als Eduface uit.
2. **Verbouw de component niet, verf hem.** Werkt iets niet, kijk eerst of het een token is dat verkeerd staat.
3. **Vervang het font.** shadcn draait op de default sans. Zet `--font-sans` op Inter en koppen op League Spartan. Dit alleen al haalt het grootste deel van de "AI-gebouwde site"-look weg.
4. **Kies je eigen dichtheid.** De defaults zijn ruimer dan onze `--row-h` / `--control-h`. Zet die door.
5. **Iconen consistent houden.** Eén set, één stroke-breedte.

## Het onderhoudsnadeel, expliciet
Omdat de code van jou wordt, krijg je geen automatische updates. Verbetert shadcn een component, dan moet je die wijziging zelf opnieuw toepassen op jouw aangepaste kopie. Dat is de prijs van volledige controle. Voor tools die je zelf gebruikt is die prijs laag, dus prima.

## Framer
shadcn werkt **niet** in Framer code components: Framer heeft geen Tailwind-buildstap, dus classnames doen niks. Voor Framer blijft de aanpak uit `framer-audit-en-migratie.md` gelden. Gebruik shadcn voor de Next.js-app, niet voor de marketingsite.
