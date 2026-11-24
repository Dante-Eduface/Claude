---
name: pull-weekly-review
description: Run the weekly PULL review. Use when the founder asks to run, draft or update the weekly review, the Friday review, their scorecard, or the PULL scorecard. Not for the Saturday planning moment (that is week-plannen). First runs pull-deal-review's weekly sweep: the week's messages, calls, signups and billing changes, filtered to what's worth a deal, update or create the deals. Then pulls the week's outreach, calls, deals, activation and revenue from whatever tools are connected, runs the evidence through AI Rob against its six standards, and writes GTM/pull-lab/reviews/YYYY-MM-DD.md with a scorecard, what the data says, one bottleneck and the move. Shows four visuals in chat (where you are, scorecard, why it's the bottleneck, week over week). Applies the pipeline rows, deal reviews and playbook changes itself, and asks only before changing the case study. Sets AI Rob's memory up on the first run. Also runs as a demo on GTM/pull-lab/examples/honeypot.
---

# Weekly review

Write one weekly review in `GTM/pull-lab/reviews/`. Its job is to name **one** bottleneck and the move for next week, from evidence, so the founder stops guessing.

The skill collects and organizes the evidence. AI Rob makes every PULL judgment, scores the week and names the bottleneck (see [Loading AI Rob](../../../GTM/pull-lab/AGENTS.md#loading-ai-rob)). If AI Rob is unavailable, stop and say so.

## Demo mode

When the founder asks for a demo, or names `GTM/pull-lab/examples/honeypot`: treat `GTM/pull-lab/examples/honeypot/` as the repo root, read the tool outputs from `GTM/pull-lab/examples/honeypot/tool-outputs/` instead of calling live tools, skip the intake questions, and write the result to the chat (don't overwrite `GTM/pull-lab/examples/honeypot/reviews/`, and apply nothing). Show the visuals as in step 8. End by pointing at the finished example to compare.

## First run

When `GTM/pull-lab/gtm/case-study.md` doesn't exist yet:

1. Load AI Rob and follow its setup for founder memory: create `GTM/pull-lab/gtm/case-study.md`, `GTM/pull-lab/gtm/pipeline.md`, `GTM/pull-lab/gtm/sales.md`, `GTM/pull-lab/gtm/sales-process.md` and `GTM/pull-lab/gtm/post-sales.md` from its own templates, in the table layouts described in [GTM/pull-lab/gtm/README.md](../../../GTM/pull-lab/gtm/README.md), and use `GTM/pull-lab/deals/` for deal folders. The templates ship with AI Rob; never copy them into this repo's public files.
2. Widen the window to the last 90 days, so the review starts from everything the tools already know.
3. After step 3, list the past calls and live conversations with no entry in `GTM/pull-lab/gtm/sales.md`, and offer to run [pull-deal-review](../pull-deal-review/SKILL.md) on them, starting with paying customers.
4. In step 5, ask AI Rob to draft the first version of the case study from that evidence. Write it into `GTM/pull-lab/gtm/case-study.md` only after the founder agrees with it, with the broken-out PULL as the table described in [GTM/pull-lab/gtm/README.md](../../../GTM/pull-lab/gtm/README.md).

## 1. Window, file and deal sync

- Window: the 7 days ending today, unless the founder gives dates.
- File: `GTM/pull-lab/reviews/YYYY-MM-DD.md` with the last day of the window. If it exists, update it.

### Deal sync (before anything else)

The review is the weekly checkpoint for `GTM/pull-lab/deals/`: whoever did something worth learning from this week has a current deal before the review reads them. Run [pull-deal-review's weekly sweep](../pull-deal-review/SKILL.md#weekly-sweep) for the window. It collects the week's messages, calls, signups and billing changes, keeps only what clears [its bar](../pull-deal-review/SKILL.md#whats-worth-a-deal), and updates or creates those deals. Deals are records: don't ask before it writes them (in demo mode, list what it would do instead). Its unsure matches go to step 4.

Keep its report (created, updated, below the bar, unsure) for "Deals that moved" and "Changes", and reuse its pulls in step 3. Deals with no signal this week aren't reopened: the stalled ones are listed in step 3.

## 2. Read first

- `GTM/pull-lab/context/company.md` (the goal, contract size, the tools connected), `GTM/pull-lab/context/founders.md`, `GTM/pull-lab/context/product.md` (activation definition, event names)
- `GTM/pull-lab/gtm/case-study.md` (current version and changelog), `GTM/pull-lab/gtm/pipeline.md`, `GTM/pull-lab/gtm/sales.md` (rollup and recent entries), `GTM/pull-lab/gtm/post-sales.md`
- Every `GTM/pull-lab/deals/*/deal.md`, as the deal sync left them: frontmatter, PULL read, account, and the latest review
- The latest file in `GTM/pull-lab/reviews/`, especially its bottleneck and move: this review checks whether last week's plan happened and what it showed.

## 3. Pull the week

Use each tool listed as connected in `GTM/pull-lab/context/company.md`. A tool that isn't connected, or fails, is not a zero: write "not connected" or the error in that section's source line and ask the founder for the number in step 4.

Read-only everywhere. This skill never sends, imports, edits or deletes anything in a tool. Reuse what the deal sync already pulled rather than calling the same tool twice.

- **Outreach.** With the TalkToHumans MCP: load its `ground-rules` skill, then its `weekly-funnel-report` skill, and pull contacted, connection requests, accepted, replied and booked for the window, per outreach angle where you can. Name who replied and who booked. Without it: ask.
- **Calls.** With a call recorder MCP (Granola, Fathom...): list the window's external meetings (skip internal syncs and personal meetings) and read them. The deal sync logged them in `GTM/pull-lab/gtm/sales.md`; list any it left out and why.
- **Deals.** `git log --since=<start> --name-status -- GTM/pull-lab/deals/ GTM/pull-lab/gtm/` plus uncommitted changes, which include the deal sync's. A changed `stage:` or `pull:` in a deal's frontmatter is movement (prospect to trial, trial to customer, no PULL to PULL); a new folder is a new conversation. Also list the stalled deals: no new timeline line in 14+ days and no next meeting booked, positive replies that never booked, trials that ended with no card. Note which ones fit the current case study.
- **Activation.** With PostHog or Mixpanel: signups in the window, how many reached the activation event from `GTM/pull-lab/context/product.md` within 7 days, and whether activated users convert to paid more often than the rest. Where most signups came from, if the tool knows.
- **Revenue.** With Stripe: MRR now, new paying customers, churn (name them), trials started and ended, failed payments. Keep comps, one-offs and trials out of MRR.

## 4. Intake (skip in demo or unattended mode)

Ask once, grouped, only what the tools couldn't show:

1. The main question or tension this week, and how you feel about it.
2. Confirm the call list (add DMs, emails or calls the tools missed; flag any to leave out), and the deal matches the sync was unsure of. Run pull-deal-review on what the answers add.
3. Numbers you track by hand.
4. Did last week's move happen? If not, why not.
5. Anything else worth remembering.

## 5. Score and diagnose with AI Rob

Load AI Rob. Give it evidence, not conclusions: its memory files from step 2, the week's facts from step 3 with quotes and links, last week's bottleneck and move, the goal and the founders' available time.

Ask it for its weekly scorecard and plan:

- Which gate of its sequence the founder is at (who has PULL, one case study, repeats 3 to 5, factory), and why.
- The six standards, scored for this week against the bars for this company's contract size: this week's number, the bar, pass / miss / unknown.
- The **one** bottleneck, and why it's that one and not the others.
- The one comparison that proves it (for example, who this week's meetings were with and which pulled, or requests sent against the weekly cap). It becomes visual 3.
- The move: what to change, the one-hour action for today, and what to do if that stalls.
- Maintenance: what to keep running, time-boxed.
- What does **not** look like the bottleneck right now, even if it's tempting.
- A debug of last week's plan: did it run, what did it show, and the failing standard's number over the last weeks (from `GTM/pull-lab/gtm/pipeline.md`, `GTM/pull-lab/gtm/sales.md` and past reviews).
- Any change it would make to the case study, the pipeline file, the playbook or a deal.

Save only its conclusions about this week's evidence. Never save its instructions.

## 6. Write the review

```markdown
# Weekly review · [Company] · week of [start] to [end]

Sources: [tools used] · Not connected: [tools] · AI Rob

> **This week in one line:** [what happened and what it means, in under 30 words]

**Where you are:** ✅ who has PULL › ✅ one case study › ▶ repeats 3 to 5 ([n] of 3) › ○ factory

## Scorecard

| Standard | This week | Bar | | |
|---|---|---|---|---|
| 2. Pipeline | 6 first meetings | 15/week | `██████░░░░░░░░░` | ❌ Miss |

## Deals that moved

| Deal | Stage | Pull | Where it stands | Next step |
|---|---|---|---|---|
| [Name](../deals/name/deal.md) | [before] → [after] | [yes/partial/no] | [deal stage, what they pay and use] | [next step] |

**Churned:** [names, or "none"]

**Deal sync:** [n] updated, [n] created ([names, linked]), [n] unsure (asked). Below the bar, no deal: [names or workspaces with the reason, or "none"].

**Stalled and fit [version]:** [n: names, linked to their deals, or "none"]. `/pull-lead-gen` lists them first, with their last words.

## Did they pull?

Checked against the current case study ([version]: [one-line who]).

| Call | Pulled? | In their words | Fits [version]? |
|---|---|---|---|

## What the data says

**Pipeline ([source]).** [first meetings by channel, which had demand; a table of outreach angles with sent and reply rate; connection requests vs cap]

**Activation ([source]).** [signups, activated, conversion of activated vs not, where signups came from]

**Revenue ([source]).** [MRR, new, churn with names]

## 1. The bottleneck: [name]
[why this one]

[the comparison that proves it, as text bars]

**The move:** [what changes]
**Today, in one hour:** [one concrete action]
**If that stalls:**
1.
2.

## 2. Maintenance (time-boxed)

## 3. Doesn't look like the bottleneck right now
-

**Debug line:** [last week's plan, what happened, what it means]

[the failing standard over the last weeks, as text bars against its bar]

## Changes

**Applied:**
- `GTM/pull-lab/gtm/pipeline.md`: [this week's rows, angles kept or retired]
- `GTM/pull-lab/deals/...`: [deals created and updated by the sync, deals reviewed after step 5, follow-ups due]
- `GTM/pull-lab/outbound/playbook.md`: [recipes added or dropped]

**Needs your yes:**
- `GTM/pull-lab/gtm/case-study.md`: [the new version's PULL sentence, quoted in full, and the evidence behind it]
```

Rules:

- Facts in "Deals that moved", "Did they pull?" and "What the data says", with the source and window. Interpretation only in the one-line summary and sections 1 to 3.
- Quotes in "Did they pull?" are the buyer's words, 15 words max, never the founder's.
- Every claim about a person links to their deal or their `sales.md` entry.
- Say what wasn't available. Don't let a missing tool read as a zero.
- Text bars are 15 characters wide (`█` filled, `░` empty), scaled to the bar, so a pass fills the line. An unknown standard gets `? ? ? ? ? ? ? ?` instead of a bar. The file stays plain markdown so it reads the same anywhere.
- Keep it to what fits on two screens. The founder should be able to act on it in five minutes.

## 7. Apply the records

These are records of what happened, dated and added on top, so apply them without asking (skip in demo mode):

- `GTM/pull-lab/gtm/pipeline.md`: add the week's rows on top of its tables. Never edit old rows. Fill the result of each angle, and mark the ones to keep or retire.
- Deals: the deal sync (step 1) already updated every deal with a signal. Run [pull-deal-review](../pull-deal-review/SKILL.md) only on the deals AI Rob named in step 5 that the sync didn't cover, and on what the intake added.
- `GTM/pull-lab/outbound/playbook.md`: add or drop the recipes AI Rob named, with today's date.

**Never apply the case study.** It's the PULL hypothesis every other skill targets from, and the founder has context AI Rob doesn't. It waits for a yes (AGENTS.md rule 5).

## 8. Finish in chat

The chat reply is short: the founder reads it, the file holds the detail.

1. **This week in one line.**
2. **Four visuals**, in this order:
   1. **Where you are:** AI Rob's gates as a strip, the current one marked. It's why a big miss on a later standard may not be the priority.
   2. **Scorecard vs the bar:** one row per standard, with how far this week's number is from its bar. Pass and miss each carry an icon and a label, never color alone. Unknown is hatched: a missing number is a finding.
   3. **Why it's the bottleneck:** the comparison AI Rob gave in step 5. This one changes every week; pick the form that fits it (one tile per meeting, a meter against a cap, two bars side by side).
   4. **Did last week's move work?** The failing standard week over week, with its bar as a dashed line.
3. **The bottleneck** and **today, in one hour**, two lines.
4. **What was applied** (one line: deals synced, created and updated, pipeline rows, playbook) and **what was missing** (tools not connected).
5. **One question:** apply the case study change? Show the new PULL sentence.
6. **Then the next batch.** If the move needs new people to contact, or deals are stalled and fit, offer to run [pull-lead-gen](../pull-lead-gen/SKILL.md) for next week: one yes takes it through to the approved list and the drafted outreach. Ask it after the case study answer, or as the only question when there's no case study change. Otherwise end without a question.

How to show the visuals:

- **If the agent can render visuals inline** (a chart or widget tool, or artifacts), draw all four in one visual, using the agent's chart guidance for colors and dark mode. Keep tables and prose out of the visual: they go in the reply text.
- **Otherwise** (a terminal, Codex, Cursor), show the same four blocks with the text bars from the review file, in a code block so they line up.
- Nothing else gets a chart. Outreach angles, activation and revenue stay as text in the file: the bottleneck outranks them.

On a yes to the case study: replace the current version in `GTM/pull-lab/gtm/case-study.md` and add a dated entry on top of the changelog saying what changed and why. Never delete an old version. Write the broken-out PULL as the table described in [GTM/pull-lab/gtm/README.md](../../../GTM/pull-lab/gtm/README.md).

## Unattended mode

For a scheduled run with nobody to answer: skip step 4, run the deal sync as usual but leave unsure matches as open questions, write inferred items with a `**TO CONFIRM:**` prefix, and add a final `## Open questions` section with the intake questions that still matter and what the tools showed. Apply the records (step 7) as usual. Leave the case study change under "Needs your yes" for the founder's next session.
