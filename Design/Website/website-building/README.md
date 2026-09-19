# Website Building

Frontend-workflow voor het bouwen/aanpassen van standalone websites (single `index.html`, Tailwind CDN, puppeteer-screenshotvergelijking tegen een referentie).

Zie `CLAUDE.md` in deze map voor de vaste regels (server starten, screenshot-workflow, anti-generic guardrails). Werkt samen met de `frontend-design` plugin-skill: die levert het designdenken (tokensysteem, anti-clichés, copy), dit bestand levert de concrete tooling om te bouwen en te verifiëren.

Tooling in deze map:
- `node serve.mjs` — statische server op localhost:3000
- `node screenshot.mjs http://localhost:3000 [label]` — hele pagina, naar `temporary screenshots/`
- `node shot_parts.mjs "<selector>" naam [...]` — scrollt eerst de hele pagina door zodat de
  in-view reveals gespeeld hebben, en schiet daarna losse secties. Gebruik deze voor alles
  wat pas zichtbaar wordt na scrollen, anders sta je naar een leeg blok te kijken.
