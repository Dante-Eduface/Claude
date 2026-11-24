# Example: Honeypot

A complete sample week for a fictional startup, so you can see the whole system run before you put your own company in.

**Honeypot** is a stockpile tracker for bears: log every food cache, and see whether you'll reach den weight before hibernation. $49 a month per den. Two founders, three months in, $2,940 MRR.

Everything here is made up. Any resemblance to real bears is a coincidence.

## What's in it

| File | What it shows |
|---|---|
| [context/](context/company.md) | A filled-in company, founders and product file |
| [gtm/case-study.md](gtm/case-study.md) | The case study: grizzlies short on weight before their den date (v2), after pandas (v1) |
| [gtm/pipeline.md](gtm/pipeline.md) | Two weeks of first meetings, per channel and per outreach angle |
| [gtm/sales.md](gtm/sales.md) | Every call since Sep 29, from a clear PULL purchase to a polite "so cute!" |
| [deals/](deals/) | Six bears with their context, PULL, account and timeline. The three live deals also have AI Rob's reviews: Grizzly Pete (paid), Ursula's sloth (trial), Mei Mei (trial, no PULL) |
| [tool-outputs/2026-10-17.md](tool-outputs/2026-10-17.md) | What the tools returned for the week (outreach, calls, analytics, billing), so the demo runs with nothing connected |
| [reviews/2026-10-17.md](reviews/2026-10-17.md) | The finished weekly review |

## Run the demo

Open the repo in Claude Code (or Cowork) with AI Rob connected and say:

> Run /pull-weekly-review on examples/honeypot as a demo.

It reads the files and `tool-outputs/` instead of live tools, runs the evidence through AI Rob, and writes the review in the chat. Compare it with [the finished one](reviews/2026-10-17.md). AI Rob won't word it the same way twice, but it should find the same bottleneck.

## What to notice

- **A false signal gets caught.** Signups jumped, but most came from a viral video of a raccoon. Raccoons are not bears.
- **Urgency sorts the buyers.** Grizzlies have a den date and a failed berry crop. Pandas eat bamboo all year and loved the demo, and none of them bought.
- **The bottleneck isn't "more outreach".** Pipeline missed its bar, but the review says the gate is repeating the grizzly case study first.
- **Last week's plan gets checked.** The panda calls ran, showed 0 of 2 on PULL, and the review proposes closing v1 for good. It doesn't edit the case study itself.
