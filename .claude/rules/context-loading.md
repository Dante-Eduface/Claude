# Context laden, werk tegenover persoonlijk

Houd werk en persoonlijk gescheiden. Niet door elkaar halen, en geen tokens verspillen aan de verkeerde.

## Werk (standaard)

Deze laden elke sessie automatisch, via `CLAUDE.md`:

| Bestand | Wat erin staat |
|---|---|
| `context/me.md` | Wie Dante is, zijn rol, zijn weekritme |
| `context/eduface.md` | Wat Eduface is, wie er werken, welke tools |
| `context/current-priorities.md` | De twee doelen en de leidende maat. Wint van alle andere bestanden. |
| `context/open-vragen.md` | Wat ik niet zelf mag invullen |

Bij werktaken blijf je in werkcontext. Geen persoonlijke context erbij halen.

**Vervallen op 19-09-2026:** `context/work.md`, `context/team.md` en `context/goals.md`. Werk en team zijn samengevoegd tot `context/eduface.md`, en de doelen staan in `context/current-priorities.md`. De oude versies staan in `archives/context-2026-09/`. Kom je een verwijzing naar die drie bestanden tegen, dan is dat een overblijfsel dat weg mag.

## Persoonlijk (alleen op verzoek)

- Persoonlijke context staat in `context/personal.md`. Dat bestand is **bewust geen `@import`**, dus het laadt nooit vanzelf mee.
- Lees het alleen als de taak echt persoonlijk is (sport, geld, relatie, persoonlijke administratie).
- Werk je aan een persoonlijke taak, houd werkcontext er dan buiten.

## Diepere bronnen

Niet elke sessie laden, wel naartoe verwijzen in plaats van uit het hoofd beweren:

- Product: `references/eduface-product.md`
- Prijs: `references/pricing/prijsmodel-psu-26-27.md`
- Deep work en de agenda-indeling: `references/deep-work.md`
- Focus en prioriteit: `references/research/focus-these-hormozi.md`

## Onderhoud

Hoe deze bestanden actueel blijven staat in `.claude/rules/context-onderhoud.md`. Kort: wat Dante in de chat vertelt over zijn werk of leven, verwerk ik dezelfde beurt in het juiste bestand. Ik wacht niet tot hij zegt "schrijf dat op".
