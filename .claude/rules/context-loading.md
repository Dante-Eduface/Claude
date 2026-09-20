# Context laden, werk tegenover persoonlijk

Houd werk en persoonlijk gescheiden. Niet door elkaar halen, en geen tokens verspillen aan de verkeerde.

## Werk (standaard)

Deze laden elke sessie automatisch, via `CLAUDE.md`:

| Bestand | Wat erin staat |
|---|---|
| `Context/me.md` | Wie Dante is, zijn rol, zijn weekritme |
| `Context/eduface.md` | Wat Eduface is, wie er werken, welke tools |
| `Context/current-priorities.md` | De twee doelen en de leidende maat. Wint van alle andere bestanden. |
| `Context/open-vragen.md` | Wat ik niet zelf mag invullen |

Bij werktaken blijf je in werkcontext. Geen persoonlijke context erbij halen.

**Vervallen op 19-09-2026:** `Context/work.md`, `Context/team.md` en `Context/goals.md`. Werk en team zijn samengevoegd tot `Context/eduface.md`, en de doelen staan in `Context/current-priorities.md`. De oude versies staan in `Archive/context-2026-09/`. Kom je een verwijzing naar die drie bestanden tegen, dan is dat een overblijfsel dat weg mag.

## Persoonlijk (alleen op verzoek)

- Persoonlijke context staat in `Context/personal.md` en `Context/financien.md`. Die zijn **bewust geen `@import`**, dus ze laden nooit vanzelf mee.
- Lees ze alleen als de taak echt persoonlijk is. Sport, eten en leren staan in `personal.md`; alles met geld in `financien.md`.
- Werk je aan een persoonlijke taak, houd werkcontext er dan buiten.

## Diepere bronnen

Niet elke sessie laden, wel naartoe verwijzen in plaats van uit het hoofd beweren:

- Product: `Platform/product.md`
- Prijs: `GTM/Pricing/prijsmodel-psu-26-27.md`
- Deep work en de agenda-indeling: `Context/deep-work.md`
- Trainingsschema's en de caloriebepaling: `Personal/fitness/schema/`
- Focus en prioriteit: `Platform/Onderzoek/focus-these-hormozi.md`

## Onderhoud

Hoe deze bestanden actueel blijven staat in `.claude/rules/context-onderhoud.md`. Kort: wat Dante in de chat vertelt over zijn werk of leven, verwerk ik dezelfde beurt in het juiste bestand. Ik wacht niet tot hij zegt "schrijf dat op".
