<a href="https://www.talktohumans.app/?utm_source=github&utm_medium=readme&utm_campaign=pull-lab"><img src="assets/banner.png" alt="PULL Lab: an AI company OS to find product-market fit, using Rob Snyder's PULL framework and the ai-rob skill. A sample weekly review names the bottleneck: repeating the grizzly case study." width="100%"/></a>

# PULL Lab

Pre-PMF, you know the pain cave: lots of "wow, this is amazing", nobody buys, so you build another feature.

But you don't need a GTM strategy. You need ONE customer who actually wants to buy, then another one just like them.

PULL Lab is an AI company OS that runs that loop with you, every week, using Rob Snyder's PULL framework and ai-rob skill:

- **You find who would be weird NOT to buy.** Your case study gets sharper every week, in your buyers' own words.

- **Your learning compounds.** Every week starts from what the last one proved.

Built with [Rob Snyder](https://robsnyder.org/) and [TalkToHumans](https://www.talktohumans.app/?utm_source=github&utm_medium=readme&utm_campaign=pull-lab).

**Want to see it before you set it up?** Read [the sample week](examples/honeypot/reviews/2026-10-17.md): a startup selling to bears, where the review catches a signup spike made of raccoons.

## How it works

### The weekly loop

<img src="assets/weekly-loop.png" alt="The weekly loop: 1. case study (Claude), 2. find leads (/lead-gen, TalkToHumans), 3. start outreach (/outbound-setup, TalkToHumans), 4. have calls (/call-prep, Granola), 5. track every deal (/deal-review, Stripe and PostHog), 6. weekly review (/weekly-review, AI Rob), 7. fix the bottleneck, update the case study, repeat." width="100%"/>

1. **Case study.** The one situation you're trying to serve, written as PULL in `gtm/case-study.md`. It starts as a guess and gets sharper every week.
2. **Leads.** `/lead-gen` works out how many people you need to contact this week from your funnel, then fills that quota warmest first: signups you haven't had a call with, leads buried in your inbox and follow-ups owed, people engaging with your content, people posting about the situation, then cold. You approve the list.
3. **Outreach.** `/outbound-setup` runs right after you approve the list: it imports it and drafts a short sequence. You review and send every message.
4. **Calls.** `/call-prep` builds a one-screen call script with AI Rob, updates it live as you paste the transcript, and debriefs.
5. **Memory.** `/deal-review` keeps one file per person in `deals/`: context, PULL, what they pay and use, a timeline, and AI Rob's dated deal reviews. Every call is also logged in `gtm/sales.md`.
6. **Review.** `/weekly-review`, every Friday: outreach, calls, deals, activation and revenue go to AI Rob, which scores the week and names the one bottleneck.
7. **Iterate.** Fix the bottleneck, update the case study, repeat.

### What it looks like

<table>
  <tr>
    <td width="50%" valign="top"><img src="assets/weekly-review.png" alt="The weekly review in chat, on the sample week: where you are, the scorecard against the bar, why it's the bottleneck, first meetings week over week, then the one move for today."/></td>
    <td width="50%" valign="top"><img src="assets/call-prep.png" alt="Call-prep mid-call, on the sample week: the call rail, what to say now, the PULL sheet filled from the buyer's words, and the playback sentence with the missing slot."/></td>
  </tr>
  <tr>
    <td align="center"><em>Weekly review, in chat</em></td>
    <td align="center"><em>Call-prep, mid-call</em></td>
  </tr>
</table>

### What you need

| Slot | Why | Required? | What I use | Also works |
|---|---|---|---|---|
| **Agent** | Runs the skills, reads your tools and keeps the files up to date | Yes | [Claude Code](https://claude.com/claude-code) or Claude Cowork | Codex, Cursor (they read `AGENTS.md`) |
| **PULL brain** | Judges every call and every week against the PULL framework: is there a real Project, can it wait, which options fail and why | Yes | [AI Rob](https://airobsnyder.com), delivered through the Skillfully MCP | — |
| **Lead sourcing** | A weekly quota from your funnel, filled warmest first: signups you haven't had a call with, leads buried in your inbox, then people showing your case study's situation right now (who engages with your posts, who posts about it and who comments), then cold leads by role and company size | Optional | [TalkToHumans](https://www.talktohumans.app/?utm_source=pull-lab&utm_medium=github&utm_campaign=readme) MCP | Any web search or scraping tool |
| **LinkedIn outreach** | Import leads with the signals that found them, draft sequences, and see who accepted, replied and booked, per outreach angle | Optional | [TalkToHumans](https://www.talktohumans.app/?utm_source=pull-lab&utm_medium=github&utm_campaign=readme) MCP | A CSV and sending by hand |
| **Call recording** | Keep buyers' exact words. They're the evidence, and your memory of a call isn't | Optional | Granola MCP | Fathom, Fireflies, any transcript you paste |
| **Billing** | See who actually paid, trialed or churned. Only a purchase proves the case study | Optional | Stripe MCP | Paste your numbers |
| **Product analytics** | Understand signups, activation and retention, and what's actively used or not | Optional | PostHog MCP | Mixpanel MCP |

*Every skill runs without the optional tools. It asks you for what it can't fetch and says so in the review.*

### What's inside

```
pull-lab/
├── AGENTS.md              # instructions for your agent (CLAUDE.md imports it)
├── context/               # company, founders, product: read before every task
├── gtm/                   # AI Rob's memory: case study, pipeline, sales log, sales process, post-sales
├── deals/                 # one file per person: context, PULL, account, timeline, AI Rob's reviews
├── outbound/              # signals and sourcing recipes
├── reviews/               # one weekly review per Friday
├── assets/                # README images
├── .claude/skills/        # weekly-review, call-prep, deal-review, lead-gen, outbound-setup
└── examples/honeypot/     # a complete sample week for a fictional startup. Delete when ready.
```

## Get started

### Set up (once)

1. **Fork it, privately.** Click **Use this template** → **Create a new repository** → **Private**.\
   *(A regular fork of a public repo stays public, and your copy will hold your customers' words.)*
2. **Clone it locally.**
   ```bash
   git clone git@github.com:<you>/pull-lab.git
   ```
3. **Open the folder as a project** in Claude Code or Claude Cowork (or Codex, if that's what you use). In agents without slash commands, ask in plain words (*"find leads"*): `AGENTS.md` points them to each skill.
4. **Connect the tools.** AI Rob first ([airobsnyder.com](https://airobsnyder.com)), then the MCPs from [What you need](#what-you-need) that you don't have yet.
5. **Fill in `context/`.** Ask your agent: *"Help me fill in context/"*. It will ask what you sell, your stage and your one goal with a date.
6. **Run a first weekly review.** Say *"run my weekly review"*. AI Rob sets up its memory in `gtm/` and `deals/`, loads what your tools already know (past calls, customers, signups, revenue), helps you write the first version of your case study, and names where to start. Want to see a finished week first? Say *"Run /weekly-review on examples/honeypot as a demo."*

### Then, every week

7. **Find leads.** *"Find and draft leads for next week"* (`/lead-gen`), or say yes when the weekly review offers it. You approve the list.
8. **Start outreach.** `/outbound-setup` drafts the messages right after, in the same run. You review and send. For a list from somewhere else, say *"Launch outreach for this list"*.
9. **Have calls, and record them.**
   - **Before:** *"Prep my call with Jane"* (`/call-prep`) gives you a one-screen script.
   - **During:** put your call on the left and the chat on the right. Every few minutes, paste the transcript so far (Granola lets you copy it mid-call), or just say *"update"*. The screen tells you what to say next.
   - **After:** *"call's over"*, then *"review this call"* (`/deal-review`). Do the same after every reply or email.
10. **Next Friday, run the weekly review.** It updates your pipeline, deals and playbook itself, and asks before changing the case study. Iterate on the bottleneck it names.
11. **Find product-market fit,** after many iterations.

### Watch the 3-minute walkthrough

<a href="https://youtu.be/brofjNE3kTg"><img src="assets/video-thumbnail.jpg" alt="Watch the 3-minute PULL Lab walkthrough on YouTube: Rob Snyder's PULL Framework, Run by Claude Code." width="100%"/></a>

## Make it yours

The choices behind this repo, and how to change them.

Every skill is a plain markdown file in `.claude/skills/`: edit it yourself, or ask your agent to.

- **LinkedIn for outreach.** Nothing to set up (no domains, warm-up or deliverability to manage), you already have an account and a network to start from, and 20 to 30% of accepted connections replying is reachable once the opener is tuned. Cold email works too, it's just more to run before you've found PULL. To switch, edit `/outbound-setup` to draft for your email tool.
- **One case study at a time.** Growth comes from repeating one situation, not serving many. To test a second one, run it as a separate sprint (`/lead-gen` asks).
- **Only a purchase proves the case study.** On a call, a buyer pulls when they start the next step themselves, like asking the price. A trial you offered, signups and compliments don't count. This is the core of the method, so keep it.
- **AI Rob makes every PULL judgment.** The skills gather and file the evidence, AI Rob scores it. Without it, they stop instead of guessing.
- **Folder and file names.** `deals/`, `gtm/`, `reviews/` and the rest are just names. If you prefer different terms, ask your agent to rename them and update every link and skill that points to them.
