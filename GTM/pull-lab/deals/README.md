# Deals

One folder per person or account we can learn about PULL from: a call, a conversation with enough detail about a yes, a meh or a no, or an inbound user who pays and uses the product a lot (the bar is in [pull-deal-review](../../../.claude/skills/pull-deal-review/SKILL.md#whats-worth-a-deal)). It covers them from that first signal through after they've paid, and also the ones who turned out to have no demand, peers and partners. Created and updated by [pull-deal-review](../../../.claude/skills/pull-deal-review/SKILL.md).

```
deals/
└── jane-acme/
    └── deal.md
```

Folder name: `person-company`, lowercase, hyphenated.

## What's in `deal.md`

Two halves. The top is the context you'd want before talking to them again, kept current. The bottom is AI Rob's dated deal reviews, never edited.

```markdown
---
stage: prospect | trial | customer | former-trial | former-customer | peer | partner
pull: yes | partial | no
band: big | moderate | small | unknown
---

# Jane Doe / Acme

## Context
- **Who:** role, company, what they sell and to whom, where
- **Source:** how the conversation started, who started it, which outreach angle or intro
- **Before us:** the tools and workarounds they used
- **Links:** LinkedIn thread, call recordings, their entries in gtm/sales.md

## PULL (latest read, YYYY-MM-DD)
- **Pulled?** the step they took on their own, quoted, or "no"
- **Fits the case study?** which version, and why or why not

| | What it is | In their words |
|---|---|---|
| **P** · Project | what they're trying to get done | "quote" |
| **U** · Unavoidable | why it can't wait, or "none" | "quote" |
| **L** · [option] | its limitation (one row per option) | "quote" |

## Account (checked YYYY-MM-DD)
- **Pays:** plan, amount, since when, invoices, trial end, cancellation reason
- **Uses:** activation, what they actually do in the product, last activity

## Timeline
- YYYY-MM-DD: what happened (newest last)

## Deal reviews (AI Rob, newest first)
### YYYY-MM-DD [account] deal review
...
```

- **Context, PULL and Account** describe the person now. Update them in place, with the date of the check.
- **Timeline** only grows.
- **Deal reviews** follow AI Rob's deal review format. Each new review goes on top; older ones are never edited. Only live opportunities get them: for someone with no demand, a peer or a partner, the context is enough.
- **Each call** also gets a row in [gtm/sales.md](../gtm/README.md), which feeds the weekly scorecard.
- **`band`** is the size of this one deal, from first-year value (learners x 3 x 12): big from 100k, moderate 25k to 99.9k, small under 25k. `unknown` until there is a learner count. The weekly review reads it to judge cycle time and close rate per band. Set from `GTM/pull-lab/context/company.md`.
- **`stage` and `pull`** in the frontmatter let the weekly review see what moved (prospect to trial, no PULL to PULL) from the git history.

See [examples/honeypot/deals/](../examples/honeypot/deals/) for six filled-in deals, from a paying grizzly to a partnership pitch.
