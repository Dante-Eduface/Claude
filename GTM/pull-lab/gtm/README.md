# GTM memory

AI Rob's memory of your go-to-market. AI Rob reads these files before it advises you, and the skills update them as the week goes.

They're created from AI Rob's own templates the first time you run `/pull-weekly-review` (or ask *"set up my AI Rob memory"*). The templates belong to AI Rob, so this repo doesn't ship them. See [examples/honeypot/gtm/](../examples/honeypot/gtm/) for filled-in versions.

| File | What it holds | Updated by |
|---|---|---|
| `case-study.md` | The one situation you're trying to serve, written as PULL, with every past version in a dated changelog | pull-weekly-review (proposed, you approve) |
| `pipeline.md` | First meetings per week, and the numbers per channel and per outreach angle | pull-weekly-review, pull-outbound-setup |
| `sales.md` | One row per sales call: did they pull, their words, fit, next step, outcome. Feeds the Pull, Close rate and Cycle time standards | pull-deal-review (after pull-call-prep) |
| `sales-process.md` | Your call scripts and sales steps | pull-call-prep, on request |
| `post-sales.md` | What success looks like after the sale, and whether customers reach it | pull-weekly-review, on request |

Rules for these files:

- **Add, don't overwrite.** New versions and entries go on top with a date. The old ones stay: they're how you see what changed and why.
- **Never paste AI Rob's instructions here.** Only what it concluded about your evidence.
- **Tables, newest row first.** AI Rob's templates use bullets; these files use tables so you can read across weeks and calls at a glance:
  - **`case-study.md`:** under the one-sentence PULL, one row each for P, U and Supply, one row per option with its limitation, and the buyer's own words in the last column.
  - **`pipeline.md`:** a top-line table (week, first meetings, bar, with demand and a fit, notes), a weekly numbers table per channel, and an angles table (started, angle, sent, reply rate, result).
  - **`sales.md`:** the rollup on top, then one Calls table: date, buyer (linked to the deal), pulled?, in their words, fits the case study?, next step, outcome, cycle, do differently. P, U and L+L live in the [deal file](../deals/README.md), not here.

  See the [samples](../examples/honeypot/gtm/).
