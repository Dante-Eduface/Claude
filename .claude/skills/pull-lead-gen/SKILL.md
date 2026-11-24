---
name: pull-lead-gen
description: Turn the current case study in GTM/pull-lab/gtm/case-study.md into the week's quota of people to contact, warmest first. Works out the quota from the funnel (contacted to first meeting rates in GTM/pull-lab/gtm/pipeline.md, capped by what the founder can send in a week), then fills it down a waterfall. First come signups and trials the founder hasn't had a call with, then leads buried in the inbox and follow-ups owed (unanswered replies, positive replies never booked, stalled deals). Then warm people who engaged with the founder's content or viewed their profile and fit the case study. Then people posting about the situation. Then cold prospects by role and company size until the quota is met. Scores them, returns the list for the founder to approve, then runs pull-outbound-setup on the approved list in the same session so the drafts are ready to review. Use for "find leads", "find and draft leads for next week", "prep next week's outreach", "who should I contact this week", "source people for my case study", "I need more leads", or when the weekly review's move needs a new batch.
---

# Lead gen

Fill the week's quota of people to contact, warmest first, all of them in the case study's shape. Signals decide who comes first; the quota decides how far down the list you go.

Follow the rules in [GTM/pull-lab/outbound/playbook.md](../../../GTM/pull-lab/outbound/playbook.md). The short version: start from the case study, pair every need signal with an urgency signal, wide in and 90 to 99% out, by hand before automating.

## 1. Read the case study

Read the current version in `GTM/pull-lab/gtm/case-study.md`: who, the PULL sentence, P, U, L+L, and the proof. Read the `GTM/pull-lab/gtm/sales.md` entries of the buyers who pulled: their own words are the best source of search terms. Read the case study's section in `GTM/pull-lab/outbound/playbook.md` if one exists, and the "angles tried" in `GTM/pull-lab/gtm/pipeline.md`.

If the founder asks for leads for a different situation than the current version, say so and ask whether to test it as a separate sprint.

If the current version's block in the playbook is parked, read its reopen condition. When the condition is met, or the block doesn't say, tell the founder in one line why it was parked and ask whether to unpark it before searching. Never run only part of lead gen without saying so up front.

## 2. Set the week's quota

Work out how many people to contact this week, and show the math in one short table:

1. **Meeting target:** the first-meetings bar in `GTM/pull-lab/gtm/pipeline.md` (the founder can set a lower one for the week).
2. **Rates, last 4 to 6 weeks, from `GTM/pull-lab/gtm/pipeline.md`** (or the outreach tool's own report): contacted to first meeting held, per source when the file splits it (signups, warm hand-picked sends, cold). Fall back on the playbook's benchmarks when a source has fewer than 20 contacts, and say so.
3. **Quota per source** = the meetings each source should bring ÷ its rate. Total quota = their sum.
4. **Cap:** new connection requests or cold emails can't exceed what the founder's accounts can send safely in a week (on LinkedIn, about 100 connection requests a week on a free account). People already connected, signups and follow-ups get a message, not a request, so they don't count against the cap. When the quota is above the cap, say how many meetings the gap costs and fill to the cap.

The quota is a floor for the search, not a reason to lower the bar: someone who is out (a seller, a competitor, no fit) stays out even when the quota isn't met.

## 3. Write the signals

If the playbook has no signals table for the current version yet, draft one and show it to the founder before searching:

- **Need** (+2 each): they're doing the Project, or the option they use is failing them. Use the words buyers used.
- **Urgency** (+3 each): the U in the case study happened in the last 30 to 60 days. Older counts 0.
- **Out:** competitors, people who sell the same thing as a service, anyone the evidence says isn't the buyer.

Load AI Rob (see [Loading AI Rob](../../../GTM/pull-lab/AGENTS.md#loading-ai-rob)) and check that the urgency signal is the case study's U, not just something recent. If AI Rob is unavailable, stop and say so.

## 4. Find them

The lead gen waterfall. Go down it in order. Steps 1 to 3 always run in full: these people already know the founder, and trust and a first reply, the hardest steps, are done. Steps 4 and 5 run until the quota is met. Paying customers are never leads: they belong to the weekly review's success work.

1. **Signups and trials with no call yet**, from the last 60 days. Match each signup to a person (email to LinkedIn or company), check `GTM/pull-lab/deals/` and `GTM/pull-lab/gtm/sales.md` for a call, and keep the ones in the case study's Who. What they did in the product counts as evidence. They get a personal note asking what was going on the week they signed up, not a sequence.
2. **Leads buried in the inbox, and follow-ups owed.** Read the founder's inboxes (LinkedIn, email) and `GTM/pull-lab/deals/` for:
   - replies the founder never answered (the thread is waiting on the founder), from the last 60 days, including replies to old sequences, inbound DMs and connection notes;
   - positive replies that never booked a meeting, and meetings offered with no slot taken;
   - deals with no new timeline line in 14+ days and no next meeting booked;
   - trials that ended with no card.

   Keep only the people whose own words fit the current case study, or who showed PULL before. Warm isn't PULL: someone with no Project or no deadline gets nothing, because following up would be pushing. An unanswered reply is the exception: it always gets an answer, and fits or not, the answer goes in the list so nothing stays buried. Each time the case study gets a new version, re-check the past "no fit" deals against it.
3. **Warm: people who engaged with the founder's content or viewed their profile** in the last 30 days, and whose profile and company fit the case study's Who. They already know the founder. The engagement is +2 (warm), not a need signal: score the rest from their profile, company and recent posts.
4. **People posting about the situation, and who comments on those posts.** Search posts from the last 30 days with the buyers' own words. Keep authors writing in the first person about the Project or a failing option, and commenters adding their own story.
5. **Cold, by role and company size**, to fill what's left of the quota. Translate the case study's Who into filters (title, seniority, company size, industry, location), exclude the Out list (competitors, agencies and sellers of the same service), then read each person's headline and company before keeping them. Demographics aren't a signal: check recent posts for a need or urgency signal when the budget allows, and mark the rest "cold, no signal" so the weekly review can compare them with the warmer steps.

The other sources in "Where signals live" in the playbook (job ads, review sites, news, public threads) can feed any step.

**With the TalkToHumans MCP (recommended):** load its `ground-rules` skill and follow its credit rules: say the cost and check the balance before more than one page.

1. Signups: TalkToHumans doesn't hold your product's signups. Pull them from your product analytics or billing tool (see "With anything else" below), then use `list_contacts` with `query` to find each one in your LinkedIn contacts.
2. Inbox and follow-ups: `list_conversations` with `conversation.reply_state` `waiting_for_my_reply` (buried replies; its `reply-triage` skill), then `waiting_for_their_reply` with the last message over 14 days old (follow-ups owed), then `list_messages` on each to read the last exchange. Skip vendors, investors and automated messages. No credits used.
3. Warm: `list_contacts` with `member.signals` (`commented_on_my_post`, `reacted_to_my_post`, `viewed_profile`) and `member.last_signal_at` in the last 30 days, plus the "Engaged with me" view. Check when they last synced.
4. Posts: `search_posts` with the buyers' words as keywords and `posted_within` `month`. Keep each query simple (one OR group at most). Read the authors, then import the commenters of the best posts with `content-engagers`, after the founder's OK on its estimate.
5. Cold: `search_people` (25 people a page), following its `import-and-prep-list` skill, with `exclude` for competitors and service sellers. Check a shortlisted person's recent posts with `find_content`.

Its searches run on credits, not on the founder's LinkedIn account. Skip its `icp-scoring` skill: the playbook's score decides here, not demographics. `get_activity_summary` gives the accept and reply rates for the quota.

**With anything else:** the same waterfall, with the tools the founder has.

1. Signups: the product's analytics or billing tool (signups, trials, what they did, who paid), matched to a person by email with web search.
2. Inbox and follow-ups: the founder's LinkedIn inbox and email, read by hand or through their CRM, plus `GTM/pull-lab/deals/`.
3. Warm: the founder's post analytics and profile viewers, read by hand on LinkedIn at a human pace.
4. Posts: a scraping tool the founder connected (post search, post comments) or web search for public threads.
5. Cold: a people database or a company search (job ads, review sites, company pages), then the person by role.

Check a tool's inputs before running it, and give the founder a cost estimate before any batch above a few dollars. Never scrape LinkedIn while logged in as the founder. When credits run out, stop and report.

Read the survivors in full: keep first-person evidence of the situation, not keyword matches, vendors, or people commenting a keyword to get a lead magnet.

## 5. Score and cut

**Follow-ups first.** The people from steps 1 and 2 aren't scored. Keep for each: the deal, the last touch date, their last words, why they fit the case study, the next step, and any date that matters (a trial end, an event). Buried replies first, then positive replies that never booked, then signups, then stalled deals.

Score everyone else with the playbook's rules. 5 or more (a need and an urgency signal, or the version's own exception) goes on the list, 2 to 4 to a watch list, the rest out. Cold leads from step 5 go on their own block, below the scored one, marked "cold, no signal" unless a post gave them one. Keep for each: company, link, found via (signups, inbox, warm, posts, cold, so the weekly review can compare steps), each signal with its date and link, and the score.

## 6. Hand back, in the chat

**No file.** Don't write a lead-list file. The list lives in the chat, and once approved, on the contacts in the outreach tool (tag, signals, notes), or in the CSV pull-outbound-setup writes when there's no tool. The only write is the playbook recipe after the founder's yes.

The founder reads this on a screen, fast. Structure over sentences: no paragraphs, every quote 10 words or fewer, every number with its unit, icons always next to a label (never color alone). Always this layout, in this order:

1. **Headline**, one line: `Week of {date} · {case study version} · {n} people · expected {m} of {target} meetings · short {gap}`.
2. **Visual 1 · the quota.** One meter per source (follow-ups, signups, posts, cold): expected meetings against the target, with the rate it used and its sample size. Beside it: connection requests planned against the weekly cap.
3. **Visual 2 · the waterfall.** One bar per step: looked at, kept, and the main cut reason in 5 words or fewer. Tool costs at the end.
4. **The people, one card or row each, in blocks with a header:** Reply first · Yes, not booked · Signups · Stalled and fit · Scored · Cold. This order is the review order: with TalkToHumans, pull-outbound-setup numbers the contacts in it, so the review view lists them the same way. Each shows:
   - name (linked) and company;
   - the score as blocks, not prose: `▲` per need, `⚡` per urgency, `♨` warm, then the number (`▲▲▲ · 6`, `▲ ⚡ · 5`);
   - why, in 8 words or fewer;
   - their last words, 10 words or fewer (follow-ups only);
   - the next step, 6 words or fewer;
   - the date that matters, with a ⏰.
5. **Watch list**: one line of names with their score. **Out**: one line of counts per reason.
6. **What I'd change in sourcing**, at most 3 bullets, only when the run taught something.
7. **One question:** approve the list, with any cuts?

How to show it: when the agent can render visuals inline (a widget or chart tool), put items 1 to 5 in one visual, as large as it needs to be: meters, bars and a card per person, grouped by block. Then keep the chat reply to items 6 and 7. Otherwise (a terminal), show the meters and bars as text bars in a code block, and the people as one table per block.

- Save the recipe that worked (tool, query, filters, cost) in the case study's section of `GTM/pull-lab/outbound/playbook.md`, after the founder's yes.
- **Then draft, in the same session.** As soon as the founder approves the list (with any cuts), run [pull-outbound-setup](../pull-outbound-setup/SKILL.md) on the approved rows. Don't stop to offer it, and pass on what this run already read so it isn't read again. Signups and follow-ups get a personal note there, not a sequence: its only job is to get them on a call by asking what changed in their situation, never to pitch. Approving the list is the founder's one stop before the drafts; nothing is sent.
