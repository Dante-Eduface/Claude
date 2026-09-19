# Task Planning — Reference

The full rubric, edge cases, and output templates. The `SKILL.md` is the loop; this is the detail. Read it when you're actually scoring tasks and writing the plan.

## The scoring rubric in full

Anchor: **UK university adoption** (pilots → institutional licenses, before runway ends). Score each task, then map to a Todoist priority.

Ask, in order:

1. **Does it move a UK university toward a pilot or license?** (outreach, follow-up, discovery/EB/POV step, a live-pilot blocker, anything feeding a UK deal) → **P1.**
2. **Is it a hard external deadline inside the current window?** (a dated webinar deliverable while the webinar is still live, a runway-critical revenue commitment, a promised send-by date) → **P1.**
3. **Does it feed pipeline a step removed from a UK close?** (NL/Ireland outreach, paid ads buildout + optimisation, high-converting website work, warm follow-ups) → **P2.**
4. **Is it supporting marketing / discoverability?** (SEO, GEO, content, brand, general marketing) → **P3.**
5. **Is it admin or low-leverage?** (process, tidying, low-impact errands) → **P4, batch or drop.**

### Tie-breakers (when two tasks land in the same tier)

1. **Deadline proximity** — sooner wins.
2. **Deal stage** — a later-stage deal (POV, business case) beats a cold/early one. Use the `cro-of-eduface` 6-stage map if a task is tied to a specific deal.
3. **Impact per effort** — a 20-minute task that unblocks a deal beats a 3-hour task that nudges a metric.

### Watch-outs

- **Een gedateerd evenement is tijdgebonden.** Staat er een webinar of beurs in `current-priorities.md`, dan zijn de gedateerde deliverables P1 tot de datum. Daarna valt alles behalve de opvolging weg. Het HHS-webinar van 23 juni 2026 is geweest en staat sinds 19-09-2026 niet meer in de prioriteiten.
- **Seasonality.** Per the outreach-seasonality memory, the UK HE calendar shifts what "urgent" means. June–August is wind-down + summer break, so heavy "let's meet next week" outreach pushes are lower-yield than scoping work that's ready to run in September. Weight outreach tasks with that in mind and say so if you down-rank one.
- **Don't inflate.** Not everything is P1. If five tasks are P1, the plan isn't prioritised. Force a ranking: there is always a single top task.
- **Wie erbij betrokken wordt, bepaalt Dante.** Sinds 19-09-2026 is de regel vervallen dat Menno en Samuel standaard buiten de deur bleven. Stel gerust een taak voor die langs hen loopt, maar leg de keuze bij Dante.

## Pulling tasks (Todoist specifics)

- **Daily:** `find-tasks-by-date` with `startDate: "today"`, `overdueOption: "include-overdue"`, `daysCount: 1`. Set `responsibleUser` to Dante (get it from `user-info`) so collaborators' tasks don't leak in, or leave the default `unassignedOrMe`.
- **Weekly:** same call with `daysCount: 7`. Also glance at last week with `find-completed-tasks` to see what shipped.
- **Monthly:** `daysCount: 30` for what's ahead, plus `find-completed-tasks` and `get-productivity-stats` / `get-project-activity-stats` for the look-back. Compare against `context/current-priorities.md` (`goals.md` bestaat niet meer sinds 19-09-2026).
- If a project has many tasks, use `get-overview` with a `projectId` to see them grouped by section.

## Output templates

Write in Dante's voice: casual, Dutch (unless he wrote English), bullets, no em-dashes, no hype. Lead with the one thing that matters most.

### Daily

```
**Vandaag — [datum]**

Belangrijkste: [de #1 taak, 1 regel waarom]

P1 (nu doen)
- [taak] — [waarom / deadline]
- ...

P2 (als P1 af is)
- [taak]
- ...

Achterstallig → verzet
- [taak] → [nieuwe dag] (waarom)

Bijgewerkt in Todoist
- [wat je hebt aangepast: prioriteit, verzet, toegevoegd]

Gaten
- [prioriteit zonder taak / iets dat dreigt te slippen]
```

### Weekly

```
**Week van [datum]**

Focus deze week: [1–2 zinnen, gekoppeld aan de prioriteiten]

Vorige week af: [korte terugblik, wat verschoof de naald]

Per prioriteit
- UK pipeline: [taken deze week]
- NL/IE + ads + site: [taken]
- Support (SEO/GEO/content): [taken]

Verzet / opgeruimd in Todoist
- ...

Gaten + risico's vs de targets
- [bijv. nog geen taak richting de 2 UK pilots / runway]
```

### Monthly

```
**Maand — [maand]**

Tegen de doelen (context/current-priorities.md):
- [doel] → [status: op koers / loopt achter] — [waarom]
- ...

Wat is er gebeurd: [highlights uit completed]

Wat moet deze maand af om op koers te blijven:
- ...

Bijgewerkt in Todoist + grootste risico
- ...
```

## Worked example (daily, illustrative)

Input: 9 open tasks, 3 overdue. Anchor says UK pipeline + webinar (live) + ads.

- "Follow-up DVC University of X re pilot" → P1 (UK deal, later stage).
- "Webinar landing page af" → P1 (dated deliverable, webinar still live).
- "Nieuwe Meta ad set NL lecturers" → P2 (feeds pipeline, a step removed).
- "SEO meta descriptions homepage" → P3 (discoverability).
- "Onkostendeclaratie indienen" → P4 (admin, batch).
- Overdue "LinkedIn DM 3 koude UK leads" → keep, reschedule to today, P2 (seasonality: summer, so scoping-ready framing, not hard CTA).

Top task = the one that most moves a UK deal with the nearest deadline. Here: the DVC follow-up (live deal) over the landing page (deadline further out). State that choice in one line.

## When the lists are empty or thin

- No tasks for today and nothing overdue: don't pad. Say the day's clear, then propose 2–3 high-leverage tasks pulled straight from `current-priorities.md` and offer to add them.
- A whole priority area has zero tasks (e.g. nothing on the 2 UK pilots): that's the headline gap. Flag it first.
