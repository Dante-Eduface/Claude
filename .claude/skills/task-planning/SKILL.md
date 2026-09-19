---
name: task-planning
description: Daily / weekly / monthly task planning + prioritisation for Dante across Todoist. Pulls his open + overdue tasks, ranks them against Context/current-priorities.md + Context/goals.md (everything ladders up to UK university adoption), produces a focused plan, and applies the reprioritise / reschedule / add changes in Todoist. Trigger when Dante says "plan mijn dag", "wat moet ik vandaag doen", "wat staat er vandaag", "weekplanning", "plan mijn week", "maandoverzicht", "prioriteer mijn taken", or on a morning planning cron.
---

# Task Planning

Dante's planning engine. Turns a pile of Todoist tasks into a focused, prioritised plan and tidies the list while it's at it. Three modes, one skill. This is hand-off priority #1.

Everything ladders up to the #1 priority: **get UK universities to adopt Eduface.** Pipeline, pilots, the webinar, and the website all serve that. Score every task against it.

## Modes (detect from the request)

- **daily** (default) — today + overdue. "plan mijn dag", "wat moet ik vandaag doen".
- **weekly** — this week + a quick look back at last week. "weekplanning", "plan mijn week".
- **monthly** — the month against the quarterly goals. "maandoverzicht", "wat moet er deze maand af".

If the mode is ambiguous, assume **daily**. Don't ask.

## The loop

```
1. LOAD     read Context/current-priorities.md + Context/goals.md (the anchor)
2. PULL     get tasks from Todoist for the mode's window (Eduface + sub-projects)
3. SCORE    rank each task on the priority ladder below
4. PLAN     write the plan in Dante's voice (template in reference.md)
5. APPLY    reprioritise / reschedule overdue / add missing priority-linked tasks in Todoist
6. GAPS     flag priorities with no task behind them, and report what changed
```

## The priority ladder (the heart of this skill)

Anchor = UK university adoption. Map every task to a Todoist priority:

- **P1 — top, do now.** Directly moves UK pipeline or a live pilot forward (outreach/follow-up to UK universities, a discovery/EB/POV step, a pilot blocker), OR a hard external deadline inside the current window (a dated webinar deliverable while it's live, a runway-critical revenue item).
- **P2 — important.** NL + Ireland pipeline, paid ads buildout/optimisation, high-converting website work, warm lead follow-ups. Feeds pipeline but a step removed from a UK close.
- **P3 — supporting.** SEO/GEO, content, general marketing, nice-to-have improvements.
- **P4 — admin / low-leverage.** Batch it or drop it.

Tie-breakers, in order: deadline proximity → deal stage (later-stage deal beats a cold one) → impact-per-effort. Read `reference.md` for the full rubric, edge cases, and the per-mode output templates.

## Scope of what to pull

- **Include:** the **Eduface** project `6g45VgPCC6MHp22p` (all sections) and its sub-projects: Hot Lead Outreach `6gqR7Q5Gj9MgjVVg`, Webinar HHS aanmeldingen `6gqRR6gxjxr7FCpx`, Webinar HHS replies `6gqRcf77j2PrvRP6`. Plus the Inbox `6M5QRjwfxMV42g4Q`.
- **Exclude by default:** the **Personal** project `6R32RmpH44VRMGJv`. Only include it if Dante asks for a personal/combined plan (and then read `Context/personal.md` per the context-loading rule).
- Use `find-tasks-by-date` with `startDate: today` and `overdueOption: include-overdue` for daily; widen `daysCount` to 7 for weekly. For monthly, also pull `find-completed-tasks` / `get-productivity-stats` to review what shipped.

## Eduface sections (for placing new tasks)

Sales `6g45W5JMF3H83JPG` · Marketing `6g45W5Q3pFC6FGjG` · Framer `6g45W5QRj6vVpCMG` · Lemlist `6gjJV3MrffqvVggp` · PLG `6gmCPmpwCmMgv8fp` · GEO/SEO `6g45W5PPHHG7fFhp` · Event manager `6g45W5PgFV3fcWVp` · Eduface platform `6g45WXVxh35HMW8j`.

## Applying changes (default to acting)

Todoist changes are internal and reversible, so apply them rather than asking each time:
- **Reprioritise** tasks whose Todoist priority doesn't match the ladder (use `update-tasks`, `p1`–`p4` strings).
- **Reschedule overdue** tasks that still matter onto a realistic day (use `reschedule-tasks`, never `update-tasks`, so recurrence + time-of-day survive).
- **Add** a task when a top priority from `current-priorities.md` has nothing behind it. Put it in the right Eduface section.
- Then **report every change** in the plan so Dante can eyeball it. Don't silently delete or complete tasks. Only complete a task if Dante says it's done.

## Output

Write the plan in Dante's voice: casual, bullets, no em-dashes, no hype, in Dutch unless he wrote in English. Lead with the single most important thing today/this week. See `reference.md` for the exact template per mode.

## Done

- A prioritised plan is in front of Dante, top item first, grounded in the current priorities.
- Todoist now matches the plan (priorities set, overdue rescheduled, missing top-priority tasks added).
- Gaps are flagged: any priority with no task, anything slipping vs the revenue targets / runway.

## Notes

- This can run on a morning cron like `hot-lead-outreach`. Not wired up yet; build it only if Dante asks.
- Re-read the anchor files every run. When focus shifts they get updated, and the plan must follow.
- Log a meaningful change to the prioritisation logic in `Decisions/log.md`.
