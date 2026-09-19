---
name: hot-lead-outreach
description: Daily hot-lead engine. Each morning, find hot leads in Lemlist, draft the perfect LinkedIn DM + email per lead (cro-of-eduface handbook logic), and drop them into Todoist for Dante to review, send manually, and complete. Trigger on the morning cron, or when Dante asks to "run the hot leads" / "check Lemlist for hot leads".
---

# Hot Lead Outreach

Runs the daily draft-review loop for warm Lemlist leads. Built from Dante's choices: **Todoist** review surface, **manual** send by Dante (only a handful of hot leads per day, so no auto-send into Lemlist), **both** LinkedIn DM + email.

This skill works hand in hand with `cro-of-eduface` (the handbook + message voice). Read that skill's logic when drafting.

## The loop

```
MORNING (cron)         find hot leads -> dedupe -> draft -> create Todoist tasks -> notify
DANTE (anytime)        read task -> edit copy if needed -> SEND it himself (LinkedIn DM / email) -> COMPLETE
                       label `skip` = don't send
```

## Key IDs

- Todoist project: **Hot Lead Outreach** = `6h7fMcFgJ7GHGvCr` (under Eduface `6g45VgPCC6MHp22p`). (Corrected 2026-08-05 — the old ID `6gqR7Q5Gj9MgjVVg` no longer resolves; if a run can't find the project, verify via `find-projects` before creating tasks.)
- Lemlist hot campaigns: `cam_Ss9Es6ayPFtGAtiNa` (Linkedin + email), `cam_3vg5T7GS4qNqXyoxP` (Linkedin + email #2)
- Task label: `lemlist-hot`

## Where the automation lives

- **Scheduler:** launchd agent `~/Library/LaunchAgents/me.eduface.hotleads.plist`, fires daily 07:30 local (Amsterdam).
- **Wrapper script (live):** `~/Library/Application Support/eduface/run-hot-leads.sh` — LOCAL disk on purpose. launchd's shell cannot open a script stored on the Google Drive CloudStorage path (exit 127), so the executable must be local. It then `cd`s into the Drive project, which launchd CAN read once the script itself is local.
- **Wrapper script (source of truth):** `.claude/scripts/run-hot-leads.sh` in the project (version controlled). **If you edit it, re-copy to the local path** or launchd keeps running the old one: `cp ".../Claud AE/.claude/scripts/run-hot-leads.sh" "$HOME/Library/Application Support/eduface/run-hot-leads.sh" && chmod +x "$HOME/Library/Application Support/eduface/run-hot-leads.sh"`.
- **Logs:** `~/Library/Logs/eduface-hotleads.log` (run output), `.err.log` / `.out.log` (launchd stdio).
- **Manual fire:** `launchctl start me.eduface.hotleads`. **Pause:** `launchctl unload ~/Library/LaunchAgents/me.eduface.hotleads.plist`.
- **Runtime:** one run takes ~12-13 min headless. Needs the Mac awake and Google Drive mounted at 07:30.

## "Hot" definition (the filter)

A lead qualifies when ALL are true:
- LinkedIn invite accepted (`linkedinInviteAccepted`)
- Email opened at least once (or `lastActionType` = `linkedinOpened`)
- No reply yet (not replied / not interested / not unsubscribed)
- Not already in the Todoist project (open OR completed) — dedupe on lead ID

**Score note (learned 2026-06-09 first run):** Lemlist's lead `score` is NOT exposed through any live API endpoint (activities, leads, contacts, stats). The scores in the original CSV came from a Clay/Lemlist enriched export, not the API. So do NOT gate on a score threshold in the automated run — qualify on engagement signals above. Stronger engagement (invite accepted AND multiple opens, recent activity) = higher priority.

## Step 1: Find hot leads

**Important data note (learned 2026-06-09):** `search_campaign_leads` in LIST mode returns only the lead's template/variable data, NOT engagement. The hot signals (`linkedinInviteAccepted`, email opens, `score`, `lastState`) live in Lemlist's **activities data**, which in this MCP is only reachable via the generic `call_api` tool (e.g. `GET` the campaign activities/export endpoint). `call_api` is in the project `ask` permission list, so an unattended run needs it explicitly allowed (see Permissions below).

1. List leads in each hot campaign with `search_campaign_leads` (campaignId only, paginate) to get the lead IDs + variables.
2. Pull engagement per lead via `call_api` against the Lemlist activities endpoint (read-only GET). Use it ONLY for reads, never POST/PUT. Note: score is not available here (see Score note), so qualify on engagement events.
3. Filter to the "hot" definition above (accepted + opened + no reply).
4. Pull existing Todoist tasks in project `6gqR7Q5Gj9MgjVVg` (open + recently completed). Each task footer carries `Lead: lea_xxx`. Build a set of already-handled lead IDs.
5. Drop any lead whose ID is already handled. The remainder is today's batch. If empty, notify "no new hot leads today" and stop.

## Permissions (for the unattended local run)

The 07:30 local job runs the bundled CLI headless and cannot answer prompts. It needs these allowed: `mcp__lemlist__call_api` (read-only, for activities), `mcp__lemlist__search_campaign_leads`, and the Todoist task tools. The genuinely dangerous Lemlist tools stay gated in `ask` and must NEVER be allowed for the cron: `send_message`, `add_leads_to_campaign`, `set_campaign_state`, and all deletes. That keeps the "never send" guarantee even though `call_api` is open: the agent has no instruction or reason to POST, and Dante sends every message manually himself, so the automation never sends at all.

## Step 2: Draft per lead (handbook voice)

Map cold/warm re-engage to **Discovery** logic. Goal of the message = a micro-yes -> SQL -> discovery call. Lead with pain + Bath Spa proof + a why-now, soft CTA. No hype, no em-dashes, casual.

**Why-now anchor (current):** NSS fieldwork runs Jan-April, results publish in summer. So to move A&F on next year's NSS, the change must be live for the autumn cohort.

**Mind the academic calendar (important).** Always factor in where the UK HE year sits. June-August is wind-down then summer break: staff are buried in exam boards and then largely out, and September is when they actually engage. So in this window do NOT push "this quarter is the window" or "let's meet next week" urgency, and don't preach "good to prepare for summer". Instead frame the timing as getting it scoped/lined up so it's READY TO RUN from the start of the new academic year, and keep the CTA low-pressure and summer-proof ("whenever suits, even once new-year planning starts"). In term-time, a tighter near-term CTA is fine. Adjust the framing to the season each run.

**Don't echo prior touches (critical).** These leads already received the campaign sequence: read the lead's `firstEmail`, `reminder1`, `reminder2` variables. Those all said the same thing (NSS score + Bath Spa pilot + "want more info?"). A re-engage that repeats that reads as "the same email, version 4" and kills the reply. So:
- Open on something genuinely NEW vs those emails. The timing/why-now angle above is the freshest hook (they never got it). Do NOT lead with their score again.
- Briefly acknowledge prior contact ("I've dropped you a couple of notes") instead of pretending it's a first touch.
- Make the DM and the email DIFFERENT from each other, not the same text twice. Same intent, different angle and wording.
- CTA should pull toward a short call (the SQL), not another "shall I send info?".

**2-pager note:** if offering a breakdown, frame it as a teaser that earns the call, not a complete case (real cost justification needs discovery first). Most relevant content for this stage: Bath Spa before/after on the NSS A&F drivers (feedback speed, usefulness, clarity of criteria, consistency); VLE/SITS integration + low faculty lift; data protection/GDPR + human-in-the-loop (security is the first UK HE procurement filter); what a pilot actually requires + that it can run via Jisc/CHEST.

**Role tiers** (drives the framing):
- **Tier A — education / teaching leaders** (Heads of L&T, Deputy Deans Education, Heads of Digital/Educational Development, Student Experience). Potential champions. Frame on owning teaching + feedback. CTA: "send the 2-page Bath Spa breakdown?"
- **Tier B — registrars / quality / strategy** (Academic Registrars, Directors of Quality). Coaches with influence on evaluation + procurement. Frame on NSS reporting + quality, "shift with the right process, not more staff hours." CTA: "send the short write-up?"
- **Tier C — learning technology** (Learning Tech Managers). Coaches. Frame on integration + faculty adoption being make-or-break. CTA: "want the breakdown?"

Each draft = a **LinkedIn DM** (primary, they're connected) + an **email** (subject + body). Reference templates: the tasks created 2026-06-09 in the project. Personalize line 1 per role; add a "below sector average" note where the NSS score is a clear outlier.

Never invent Bath Spa metrics. Keep proof qualitative + offer the breakdown.

## Step 3: Create Todoist tasks

One task per lead in project `6gqR7Q5Gj9MgjVVg`, label `lemlist-hot`:
- **Title:** `{Name} · {University}`
- **Priority:** by engagement strength. Invite accepted + multiple opens (or very recent activity) = p1; accepted + a single open = p2; weaker/older signal = p3.
- **Description:** role/score/NSS line, then the approve instructions, then `**LINKEDIN DM**` block, then `**EMAIL** · Subject: ...` block, then footer `Lead: lea_xxx | Campaign: cam_xxx | Email: ... (or "No email on file")`.

Approve instructions line (verbatim):
`**Send this yourself (LinkedIn DM / email), then complete the task. Edit the copy first if you want. Label \`skip\` = don't send.**`

Then send Dante one notification (Todoist handles it; or a one-line summary if run interactively).

## Step 4: Send (manual, by Dante)

The automation never sends. Dante reviews each task, sends the DM/email himself (copy-paste into LinkedIn / email), then completes the task. Decided 2026-06-10: keep this manual — there's only a handful of hot leads a day, which doesn't justify a brittle Lemlist auto-send (especially for LinkedIn DMs to leads who already finished the sequence). No `update_lead_variables` push, no `sent` automation. The send tools stay gated.

- Completing a task = Dante has sent it (or otherwise handled it). `skip` label = not sent.
- LinkedIn-only leads (no email on file): just the DM.
- If hands-off send is ever wanted later, that's a separate build; until then, drafting + queuing into Todoist is the whole job.

## Notes

- Outward-facing: never send without an approved (completed) task. Drafting + queuing is always safe; sending requires the approval gesture.
- Refresh the why-now anchor when the NSS cycle moves on, or when there's a real Bath Spa result to quote (that becomes the proof point).
- Log meaningful changes (threshold, tier logic, Phase 2 go-live) in `decisions/log.md`.
