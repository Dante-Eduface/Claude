---
name: pull-outbound-setup
description: Import a founder-approved lead list and draft a short outreach sequence for the current case study, with the message from AI Rob and the buyers' own words. With the TalkToHumans MCP it imports the contacts with their signals, groups them under the case study version and sets up the sequence as a draft for the founder to review and launch; without it, it writes a CSV with the drafted messages. Use for "launch outreach", "set up a sequence for this list", or "draft messages for these people". pull-lead-gen runs it right after the founder approves a list; run it on its own for a CSV or names from elsewhere.
---

# Outbound setup

Get an approved list into a sequence the founder can review and launch, grouped under the case study version it tests so the weekly review can count it.

**Draft, never send.** This skill never sends a message, connection request or email. The founder reviews and launches everything.

## 1. Inputs

- An approved list (from [pull-lead-gen](../pull-lead-gen/SKILL.md), a CSV, or names). If it's missing, ask. When pull-lead-gen hands over in the same session, reuse what it already read (the case study, the buyers' words, the playbook section, the angles tried) instead of reading it again.
- The current version of `GTM/pull-lab/gtm/case-study.md`, and its section in `GTM/pull-lab/outbound/playbook.md`.
- The `GTM/pull-lab/gtm/sales.md` entries of buyers who pulled: their words are the raw material for the message.
- The "angles tried" in `GTM/pull-lab/gtm/pipeline.md`: what already worked and what didn't.

## 2. The message

Load AI Rob and ask for the outbound message for this case study. Give it the case study, the buyers' own words, the angles already tried, and the founder's background from `GTM/pull-lab/context/founders.md`. Keep:

- One line that's interesting to the reader, and a short ask for a chat.
- No quoting the signal back at them ("saw your account got restricted"), no feature list, no pitch.
- A one-word bump two to three days later.

Show the founder the message and the sequence before setting anything up. Default sequence (from the playbook):

1. Day 0: connection request, no note.
2. Day after accept: the message.
3. Two to three days later: the bump.
4. Stop. On a positive reply, don't answer with your booking link alone: ask whether they have a calendar you can book into, and offer a slot today, with your own link only as a fallback. No booking after a day: a short nudge. Two days later, one last follow-up, then stop.

## 3. Set it up

Whatever the tool:

- Before importing, check that nobody on the list already has a folder in `GTM/pull-lab/deals/` or a conversation with the founder. Those get a personal note, not a sequence: draft it from their last words in the thread and ask what changed in their situation, to get them back on a call. No pitch.
- Group the contacts under the case study version so the weekly review can count them: one short tag per version (e.g. `pull-v3`), and a list or view with the full name (e.g. `case study v3 · grizzlies, berry crop failed · 2026-10-17`).
- Keep each lead's signals from pull-lead-gen (what happened, date, link) on the contact, so the founder sees why and when to write.

**With the TalkToHumans MCP (recommended):** load its `ground-rules` skill, then `import-and-prep-list` for the import and `write-linkedin-messages` for the drafts, and follow them. Ask before creating the tag. Push the signals with `create_signals`, all of the list in one call, with a stable key per person and signal so a re-run adds nothing. Set the sequence up as a draft and tell the founder where to review and launch it.

TalkToHumans, the review view: sort it so the founder reviews from the top down. Create a number field `Review order` once (`list_field_definitions`, then `create_field_definition` if it's missing) and set it on every contact of the batch with `update_contact`: 1 for the first to review, following pull-lead-gen's hand-back blocks in order (Reply first, Yes not booked, Signups, Stalled and fit, Scored, any test block, then Cold). Within a block, the soonest date that matters comes first, then the highest score, then the most connections. Then create the review view on the batch's contacts (`member.specific_contacts`), sorted by `member.custom_fields.Review order` ascending, with the columns `member.custom_fields.Review order`, `member.full_name`, `member.headline`, `member.notes`, `member.signals` and `member.relationship_status`. Don't sort by an existing score field such as `ICP Score`: follow-ups and cold leads have no score, and it measures profile fit, not who to write first.

**With anything else:** write `GTM/pull-lab/outbound/leads/YYYY-MM-DD.csv` with name, link, company, signals, score and the drafted messages, and give the founder the sending order. If the founder uses a CRM, offer to import that CSV with the tag.

## 4. Record

- Add the angle as a new row on top of the angles table in `GTM/pull-lab/gtm/pipeline.md`, with its start date, the number sent and "too early to tell" as the result. The weekly review fills the result.

## 5. Hand back, in the chat

No file beyond the CSV that the no-tool path needs. Same style as pull-lead-gen's hand-back: structure over sentences, no paragraphs, quotes 10 words or fewer. Always this layout:

1. **Headline**, one line: `{n} drafts staged · {k} sequences · {p} personal notes · nothing sent`.
2. **One card per template or variant:** its name, how many people it goes to, then each step with its day offset (`D0 request` · `D+1 message` · `D+3 bump`), and the first message filled in for one real lead. When two variants are tested, put their cards side by side with the one word that differs highlighted.
3. **Personal notes:** one row each with name, their last words (10 words or fewer), and the drafted note.
4. **Checks**, as a checklist with ✓ or ✗: nobody already in `GTM/pull-lab/deals/` or in a conversation, the tag, the template used, people already in another sequence. Every ✗ names who to fix and how.
5. **What to watch:** the three benchmarks as targets (30%+ accept, 20%+ of accepted reply, 50%+ of replies positive), and that the weekly review reports against them.
6. **Where to review the drafts** and **one question:** anything to change before you launch?

How to show it: when the agent can render visuals inline, items 1 to 5 go in one visual, and the chat keeps the review link and the question. Otherwise, use a table per block.
