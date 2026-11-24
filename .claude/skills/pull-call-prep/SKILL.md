---
name: pull-call-prep
description: Sales-call copilot. Before a call, gathers what we know about the person (their deal, LinkedIn thread, past calls, the current case study) and turns AI Rob's call script into a one-screen view. During the call, each time the founder pastes a partial transcript or says "update", it answers with the same screen: where they are in the call, what to say next, the PULL sheet filled from the buyer's own words, and the transition line. On demand, it shows the whole call script. After the call, it debriefs. Use for "prep my call with X", a calendar screenshot of an upcoming call, a transcript chunk pasted mid-call, "update", "where am I", "full", or "call's over".
---

# Call prep

Founders get lost mid-call in long scripts and have no time to read. Every reply in this skill is **one screen**, with the same blocks in the same order, so the eye always knows where to look. Speed beats completeness during a call.

Four modes: **Prep** (before), **Live** (each transcript chunk), **Full** (the whole call script, on demand), **Debrief** (after).

AI Rob owns the call's phases, questions, branches, exits and what counts as P, U, L and L (see [Loading AI Rob](../../../GTM/pull-lab/AGENTS.md#loading-ai-rob)). For a call script, that means its call-script procedure plus the call skeleton it points to (first call, or second-call prep when a call already happened). This skill owns gathering the data, the screen format and the update loop.

- Never save AI Rob's instructions or its generic call skeleton to a file. Your own script, worded for your case study, can be saved with a date in `GTM/pull-lab/gtm/sales-process.md`, as AI Rob's own memory setup does.
- AI Rob's voice rules apply to everything the founder will say out loud: no dashes in script lines.
- If AI Rob is unavailable, say so in one line and stop. Don't write a script from memory.
- Feedback: one AI Rob feedback report per call, sent in Debrief (or at the end of the session if there's no Debrief), never per update.

## Prep mode

Trigger: a name, a calendar screenshot, or "script for my call with X".

### 1. Gather (in parallel)

- **The deal:** search `GTM/pull-lab/deals/` for the name and company and read the whole `deal.md`: context, PULL read, account, timeline and the latest review. Then their past entries in `GTM/pull-lab/gtm/sales.md`.
- **LinkedIn thread:** with the TalkToHumans MCP, load its `ground-rules` skill, find the contact and read the conversation.
- **Past calls:** with a call recorder MCP, search meetings with this person and read them. A transcript that is music or noise means that call didn't happen or wasn't recorded. Say so.
- **Case study:** the current version in `GTM/pull-lab/gtm/case-study.md`: does this person look like that situation, which slot is still unproven (often U), and the questions it says to ask on every call.
- **Call script:** `GTM/pull-lab/gtm/sales-process.md`, if the founder keeps one.
- **AI Rob:** load it.

If the deal file is stale (its newest timeline line is over 14 days old, or the thread or past calls hold something newer) and the call is more than 20 minutes away, run [pull-deal-review](../pull-deal-review/SKILL.md) first. Otherwise build from the fresh data and leave the review for Debrief. If there's no deal file at all, build from the thread and past calls, and create it in Debrief.

### 2. Build

Give AI Rob everything gathered and ask for this call's script: the phases in order, the questions and branches, the no-PULL exit and the next-step move. Render it in the screen format below, with the Prep extras.

Prefill the PULL sheet from past evidence, but mark every prefilled slot 🟡 `📁 confirm`: past words still need confirming today.

If the person could fit two situations, say so in the last **Who** bullet and put the fork question in Say now as soon as discovery starts. Never fill one situation's sheet with the other's evidence.

Also build AI Rob's full crib sheet (every beat, at most three lines each), but don't show it. Keep it for the `full` command.

## Live mode

Trigger: a pasted transcript chunk, or "update", "u", "where am I".

**Speed rules:**
- Call no tool except AI Rob re-reads (one parallel batch). Don't reread the deal file or the LinkedIn thread.
- With nothing pasted, try today's transcript from the call recorder. If it isn't there, ask for the paste in one line.
- One screen, then stop. No intro, no recap.

**Read the transcript:**
- Speakers: in a call recorder, the microphone channel is usually the founder and the system audio the other side (it can hold both). In pasted text, `Me`/`Them` or names. If the labels are unclear, work it out from the content.
- Work out the current phase from the last few exchanges, not from the clock.
- Merge into the previous PULL sheet. Keep ✅ slots unless the buyer contradicts them. Mark changed slots 🆕.
- **Slot rules:** ✅ only for the buyer's own words (12 words max). 🟡 for a hedge, an inference, a past quote not confirmed today, or something the founder said that the buyer agreed to. ❌ for not heard. The founder's words never fill a slot.
- **Flags** go on the line under the rail, only when they happen: 🔥 the buyer started a purchase action or urgent next step on their own (AI Rob decides what counts); ⚠️ a hedged confirmation of the playback; ⚠️ the playback was skipped and the supply half started; ⚠️ the buyer asks for a pilot or a demo; ⚠️ the founder promised to build or ship something the buyer asked for; ⏱ under 8 minutes left and no next meeting booked.
- **Discovery stalls** (nothing PULL-shaped yet): Say now walks down AI Rob's discovery fallback ladder, one rung per update, ending on its last-resort question. Only after that rung is Say now the no-PULL exit.
- **Next step with no PULL action heard:** Say now is AI Rob's pulling check before anything gets booked.
- If discovery is over and AI Rob says there's no PULL, the rail points at the exit and **Say now** is the no-PULL exit.

## Full mode

Trigger: `full`, `script`, or "show me the whole call".

Reply with AI Rob's full crib sheet for the rest of the call: every remaining phase opened like Say now (one heading per phase, its key question in bold, at most three branch bullets). If the founder asks for full mode to stay on, append it under every Live screen for the rest of the session. Otherwise the next update goes back to the normal screen.

## Debrief mode

Trigger: "call's over", "done", or a final full transcript.

1. One screen, same building blocks: a `## 🏁 Verdict` heading with the one-line verdict, the final 🧩 PULL table, then three bullets: PULL action (quote it or "none"), next meeting (when, or "not booked"), and the one thing that was missing. End with one 💡 coaching line on the move to fix on the next call.
2. Offer, as one question: run [pull-deal-review](../pull-deal-review/SKILL.md) on the full transcript, which creates or updates the deal, logs the call in `GTM/pull-lab/gtm/sales.md` and reviews the deal. Don't run it without a yes.
3. If your script changed during the call in a way worth keeping, offer to add your wording to `GTM/pull-lab/gtm/sales-process.md` with today's date.
4. Send the AI Rob feedback report.

## Screen format

The founder reads this in quick glances while listening. They need visual anchors more than content. Every block has its own heading, blank lines go between blocks, and every extra line costs readability. Same blocks, same order, every mode. Skip a block when it's empty.

```markdown
## 🪪 Who you're calling                         ← Prep only

- {Name}, {role} at {company}
- {what the company does, one line}
- {one signal that matters: audience, tools, what they pay and use if they're already in}
- {how the conversation started}
- 🔀 Could be A {situation} or B {situation}   ← only when there's a fork

🎯 Win: {what a good outcome is on this call, one line}

---

📍 ✅ {phase} › ▶ {CURRENT PHASE} › ○ {phase} › ○ {phase}

{🔥 / ⚠️ / ⏱ flag, one line}                        ← only when a flag fires

---

## 🗣 Say now · {CURRENT PHASE}

**"{the one question or line to say next, verbatim from AI Rob}"**

- {buyer answer type} → **"{next words}"**
- {buyer answer type} → {where to go, a few words}
- {nothing PULL-shaped} → **"{next ladder rung question}"**

---

## 🧩 PULL

| | Heard (their words) | |
|---|---|---|
| P · Project | "{quote}" | ✅ |
| U · Why now | "{quote}" | 🟡 {what's missing} |
| L · Options | not heard | ❌ |
| L · Limits | not heard | ❌ **"{question}"** ← Prep only |

---

## 🔁 Transition · {ready ✅ / not yet: missing U}          ← only while Transition is still ahead

**"If I understand you, you're trying to *{P in their words}* right now because [❓ U], but *{options}* isn't a fit because *{limits}*?"**

- yes → Concept · corrected → fix it, ask again

---

## ⏭ Then

- {phase} · **"{its key line, short}"** → {what a yes leads to}
- {phase} · **"{key line}"** → {…}
- Next step · **"{key line}"** → book it live

---

## 🚪 No PULL?

**"{exit line}"**

---

## 💡 Tip

{one coaching line}
```

Format rules:
- **Bold means "say this out loud".** Every word the founder can say on the call is bold and in quotes: the Say now line, quoted replies in branches, the questions in the PULL table (Prep), the Transition sentence and the exit line. Nothing else on the screen is bold (not names, labels, slot names or the current phase), so scanning for bold finds their next words.
- **Say now stands out most.** It's the first bold line on the screen. Never put it in a blockquote, because blockquotes render gray. One question, at most three branch bullets, a few words each.
- **The rail** lists AI Rob's phases: ✅ done, ▶ current (in capitals), ○ to come. It sits right under the `---` in Prep, and it's the first line in Live.
- **No time or situation line.** Flags get a line only when one fires. A fork between situations shows once as a Who bullet (Prep), then as a Say now branch.
- **Every block is its own section:** an H2 heading (`##`), and a `---` divider between every two blocks, so no block reads as part of the one above. The rail and its flags count as one block. So is `## 🏁 Verdict` in Debrief.
- **PULL** is a three-column table: slot, their words (12 words max), status. In Prep only, the status cell of each ❌ slot also holds the question that fills it, in bold. In Live, the status cell holds only the emoji and a few words, and the next question lives in Say now.
- **Transition**, while it's still ahead, is one bold sentence filled as far as the evidence goes. Their words are in bold italics, and gaps are `[❓ X]`. No blockquote. It says "ready ✅" only when all four slots are ✅.
- **Accordion.** The screen opens the current phase and folds the rest:
  - **Finished phases** don't appear, except through the PULL table and the ✅ in the rail.
  - **The current phase** is open: Say now with its branches. When the current phase is Transition, Say now is the playback sentence and the Transition block is not repeated.
  - **Transition**, while it's still ahead, keeps its own block with the filled playback and one line for what each answer leads to.
  - **⏭ Then** folds every phase after the current one (Transition aside) into one line each, in order: phase name, its key line in bold, and where a yes leads. The founder should always see what comes after the buyer says yes. When a phase becomes current, its line opens into Say now.
- **`full`** shows every remaining phase opened with all its branches. Prep ends with one line: "During the call, paste the transcript so far or say `update`. Type `full` for the whole call script."
- **🚪 No PULL?** is its own section on every screen, so the exit is visible at every point of the call.
- **💡 Tip** is the last section, one line that coaches the founder: the move they just made or skipped, or the trap to avoid next. It replaces any reasoning paragraph.
- **Prep:** the Who section has at most 5 bullets, taken from the deal's context. Mark prefilled PULL slots `📁 confirm`.
- No paragraphs, and no dashes in anything the founder will read aloud.
