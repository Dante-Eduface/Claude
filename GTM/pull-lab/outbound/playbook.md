# Outbound playbook

How we find people in the case study's situation. The case study itself lives in [gtm/case-study.md](../gtm/README.md), and the weekly numbers and outreach angles in `gtm/pipeline.md`; refer to them here, don't copy them.

## Six rules

1. **Start from the case study, not a list.** Write the PULL statement first. Then ask: what would this situation leave behind in public? Those traces are your signals.
2. **Company first, people last.** Qualify the company (site, job ads, stack, team shape, reviews) before looking up the person.
3. **Skip the obvious signals, stack the quiet ones.** "Looking for a tool" posts are seen by every vendor. Three weak hints on the same company beat one loud one.
4. **Always pair a need signal with an urgency signal.** Need: they're doing the Project and their option is failing. Urgency: something happened in the last 30 to 60 days. Need without urgency goes to a watch list, not to outreach.
5. **Wide in, 90 to 99% out.** Start with the biggest pool you can get, exclude fast with cheap checks, and give only the top few percent a human look.
6. **Manual before machine.** Run a new recipe by hand on 20 to 50 companies. Automate it only once it produced real conversations.

## Where signals live

The lead gen waterfall, warmest first, until the week's quota is met: signups and trials you haven't had a call with; then leads buried in your inbox and follow-ups owed; then people who engaged with your content or viewed your profile and fit the case study; then people posting about the situation and their commenters; then cold leads by role and company size. The quota comes from your funnel (contacted to first meeting, last 4 to 6 weeks in `gtm/pipeline.md`), capped by what your accounts can send in a week. How it's computed is in the [pull-lead-gen skill](../../../.claude/skills/pull-lead-gen/SKILL.md).

| Source | What to look for |
|---|---|
| Your own signups and trials | People who signed up in the last 60 days and never had a call, what they did in the product, and whether they fit the case study's Who |
| Your own inbox | Replies you never answered, positive replies never booked, deals gone quiet, trials ended with no card |
| Your own posts and profile | Who commented, reacted or viewed your profile lately, and what their comment or profile says about the situation |
| Job ads | Roles and tools named in the ad |
| Company websites | New careers pages, new sales or partner pages, new scripts in the page source |
| Review sites (1 and 2 stars) | Named reviewers leaving a competitor, with the reason |
| Public threads (Reddit, communities, LinkedIn comments) | Someone stuck on the exact Project, recently |
| Posts | First-person "here's what I tried" posts, and who comments with their own story |
| News | Events that create a deadline for a whole group at once |

## Scoring (keep it dumb)

- +2 per need signal, +3 per urgency signal (older than 60 days counts 0)
- +2 warm: commented on, reacted to or viewed your profile or posts in the last 30 days. It's not a need signal: a warm lead still needs one in their own words to pass 5
- Your own exclusions: -5 or out (competitors, people who sell the same thing as a service...)
- Outreach at 5 or more (a need and an urgency signal). 2 to 4 goes on a watch list, re-checked monthly.
- Cold leads found by role and company size alone go on their own list, marked "cold, no signal", to fill the week's quota. The weekly review compares how they convert with the warmer sources.

## Message and sequence (default)

Signals decide **who** and **when**. The message only earns the call. Don't quote the signal back at them ("saw your account got restricted"): it reads as surveillance. Ask AI Rob for the outbound message, then keep it to one line that's interesting to them and a short ask.

1. Day 0: connection request, no note. Your profile is the landing page.
2. Day after accept: the message.
3. Two to three days later: a one-word bump.
4. Stop. On a positive reply, don't answer with your booking link alone: ask whether they have a calendar you can book into, and offer a slot today, with your own link only as a fallback. No booking after a day: a short nudge. Two days later, one last follow-up, then stop.

**Benchmarks per stage:** 30%+ of requests accepted (under 20% is a profile or list problem), 20%+ of accepted connections reply (under 5% is a message problem), 50%+ of replies positive, and most positive replies book a call. Fix only the stage furthest below its benchmark.

## Per case study version

<!-- Add a block when a new version of the case study gets sourcing. Keep the old blocks: they show which recipes worked for which version. -->

### v1 · <!-- short name, date -->

**Signals**

| Type | Signal | Points |
|---|---|---|
| Need | | +2 |
| Urgency | | +3 |
| Out | | out |

**Sourcing recipe** (tool, query, filters, cost per batch):

1.
