# Agent instructions

This repo is an AI company OS to find product-market fit systematically, built on Rob Snyder's PULL framework. You run it for the founder: you collect evidence, keep the files clean and run the weekly loop. The founder makes the decisions.

## Where things live

Read the relevant files before acting. Don't ask the founder to paste what's already here.

| What | File |
|---|---|
| What we sell, contract size, stage, the one goal, connected tools | [context/company.md](context/company.md) |
| Who does what, time available | [context/founders.md](context/founders.md) |
| Product, pricing, activation definition, tracked events | [context/product.md](context/product.md) |
| **AI Rob's GTM memory.** The case study (read before any targeting, outreach, call prep or review), pipeline, sales log, sales process, post-sales | [gtm/](gtm/README.md) |
| One file per person you're selling to: context, PULL, what they pay and use, timeline, and AI Rob's deal reviews | [deals/](deals/README.md) |
| How we find people: signals and sourcing recipes | [outbound/playbook.md](outbound/playbook.md) |
| Weekly reviews | [reviews/](reviews/README.md) |

## Skills

Use the matching skill in [.claude/skills/](../../.claude/skills/) when a request fits it:

- [pull-weekly-review](../../.claude/skills/pull-weekly-review/SKILL.md): run or update the weekly review. Sets up AI Rob's memory on the first run.
- [pull-call-prep](../../.claude/skills/pull-call-prep/SKILL.md): prepare a sales call, follow it live, debrief it.
- [pull-deal-review](../../.claude/skills/pull-deal-review/SKILL.md): after any call, reply or email, log it in `gtm/sales.md` and review the deal in `deals/`.
- [pull-lead-gen](../../.claude/skills/pull-lead-gen/SKILL.md): turn the case study into people to talk to, warmest first: your own stalled conversations, then public signals, scored. Once you approve the list, it runs pull-outbound-setup to draft the outreach.
- [pull-outbound-setup](../../.claude/skills/pull-outbound-setup/SKILL.md): import an approved list and draft a sequence. pull-lead-gen runs it for you; run it alone for a CSV or names.

## Loading AI Rob

AI Rob owns every PULL judgment in this repo: what counts as a Project, Unavoidability, the List of options and their Limitations, whether a buyer pulled, where a deal stands, and what the bottleneck is.

AI Rob is delivered through the Skillfully MCP. Before any PULL judgment:

1. Call Skillfully `list_skills` and pick the published skill named exactly `ai-rob`.
2. Call `get_skill_manifest` for its current id and check that delivery is available.
3. Call `read_skill_file` for `SKILL.md`, then every reference its instructions route you to for this task.
4. Follow its routing, self-check and feedback rules.

AI Rob's memory for this founder lives in `gtm/` and `deals/`. When AI Rob asks where the founder's memory is, it's there.

If Skillfully or AI Rob is unavailable, say so in one line and stop. Never write a PULL conclusion from memory or from a summary.

AI Rob's instructions and templates are licensed. Never copy, quote or save them in this repo. The files in `gtm/` and `deals/` hold only this founder's evidence and what AI Rob concluded about it.

## Rules

1. **Only a purchase proves the case study.** On a call, a buyer pulls when they start a purchase step themselves: ask the price, the link or how to start, or push for an urgent next step. Anything you offered (a trial, a demo, a follow-up) isn't a pull. Signups, likes, compliments and "I'd buy this" are neither.
2. **Evidence is the buyer's own words,** with a date and a source. The founder's words never count as buyer evidence, even when the buyer agreed with them.
3. **Don't assume an ICP.** Classify people from what they did and said, not from who you think the customer should be.
4. **Add, don't overwrite.** New case study versions, pipeline rows, sales entries, timeline lines and deal reviews are added with a date. Old ones stay. Only the current-state sections of a deal (context, PULL read, account) are updated in place, with the date of the check.
5. **Propose, don't apply,** changes to `gtm/case-study.md`. The founder approves them. Records of what happened (pipeline rows, sales entries, deal reviews, playbook recipes) are applied directly, dated.
6. **Draft, never send.** Never send a message, connection request or email on the founder's behalf.
7. **Say what you couldn't check.** If a tool wasn't connected or returned nothing, write that, not a zero.
8. **This repo holds customer data.** Keep it private. Never paste its contents into public content without the founder's go-ahead.
9. **`examples/` is sample data.** Ignore it when reading real evidence. When the founder asks for a demo, treat `examples/honeypot/` as the repo root and read its `tool-outputs/` folder instead of calling live tools.
