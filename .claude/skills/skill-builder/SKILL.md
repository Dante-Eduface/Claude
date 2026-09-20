---
name: skill-builder
description: Build a new Claude Code skill, or fix/upgrade an existing one. Use when Dante says "make this a skill", "turn this into a skill", "build a skill for X", "update deze skill", "klopt deze skill nog", or when you notice a workflow being repeated and want to capture it. Walks the full loop: scope the workflow, wire it to the living sources it reads, write the SKILL.md frontmatter + body, add reference files, and test that it triggers. Anchors to the Eduface "build skills organically" rule, the source rule below, and `.claude/rules/skill-onderhoud.md` for keeping skills alive after they ship.
---

# Skill Builder

_Laatst bijgewerkt: 2026-09-20._

This is the meta-skill: it builds other skills. Use it whenever a recurring workflow is ready to be captured as a reusable `.claude/skills/<name>/SKILL.md`, and whenever an existing skill needs repair.

Read `reference.md` (in this folder) for the full technical spec: frontmatter schema, the Bronnen block, anti-triggers, budgets, directory layout, and common mistakes. This file is the *process*. `reference.md` is the *rules*.

Keeping a skill current after it ships is a separate rule that applies in every session: `.claude/rules/skill-onderhoud.md`. Read it before you repair an existing skill.

## When to build a skill

Build one when **all three** are true:
- The same request has come up **2+ times** (or Dante explicitly asks for a skill).
- There's a **repeatable procedure** worth writing down, not a one-off.
- It ladders up to the one priority in `Context/current-priorities.md`.

Per CLAUDE.md, skills at Eduface are built **organically**. Don't pre-build skills nobody has asked for. The backlog of candidate workflows lives in CLAUDE.md under "Skills to Build". When you finish one, suggest crossing it off.

If it's a one-off, don't make a skill. Just do the task.

## The source rule (the most important thing in this file)

**A skill is a procedure, not a copy of the data it runs on.** Every fact that lives somewhere else gets **pointed at by path**, never written into the skill.

Why this matters more here than anywhere else: a skill is only opened when it fires. A copied fact rots in silence, and the skill keeps giving confident advice on information that stopped being true months ago. Measured on 20-09-2026: 2 of the 29 skills referenced anything in `Context/`. `fitness-coach` was still steering on WHOOP, InBody and a weight goal, all three dead. `week-plannen` had transcribed the deep-work table instead of linking it.

| Belongs IN the skill | Belongs at the end of a path |
|---|---|
| The steps, in order | Who Dante is, his week, his rhythm (`Context/me.md`) |
| The judgement calls and the guardrails | The priority and the leading measure (`Context/current-priorities.md`) |
| The shape of the output and the done-state | Who works at Eduface, which tools (`Context/eduface.md`) |
| Which file to read, and at which step | Product claims (`Platform/product.md`) |
| Style rules that are specific to this one skill | Prices (`GTM/Pricing/`) |
| IDs the procedure literally cannot run without | Method, playbooks, gates (`GTM/Knowledge/`) |
| | Pipeline and deal state (Close, never a file) |
| | Visual rules (`Design/System/core/` plus the one surface) |

Two nuances:
- **IDs are the exception, not the escape hatch.** A campaign ID or a Todoist section ID has to be in the skill or the step can't run. Put them in one block, under one heading, with the date they were checked. Everything that varies per market or per client goes in a profile file the skill reads, not in the skill.
- **Pointing at a path is not enough on its own.** Say *what* the skill must take from it and *when*: "read `Context/current-priorities.md` for the block schedule before you plan anything" beats "see Context".

## The build loop

```
1. SCOPE      what triggers it, what it does, what "done" looks like
2. NAME       kebab-case folder name = how it's invoked (/name)
3. BRONNEN    which living files it reads, and what it may therefore NOT remember
4. WRITE      SKILL.md frontmatter (name + description) then the body
5. SPLIT      move deep detail / data / long examples into reference files
6. TEST       confirm it shows up and triggers
7. LOG        decision log + suggest removing it from the backlog
```

### 1. Scope (ask before writing)

Don't write a skill from a vague ask. Pin down, in 1-2 quick questions if needed:
- **Trigger** - what words or situation should fire it? (This becomes the description.)
- **Steps** - the actual procedure, in order.
- **Inputs/IDs** - campaign IDs, project IDs, file paths, MCP servers it touches.
- **Output + review surface** - what it produces and where Dante reviews it.
- **Done** - what a successful run looks like.

If the answers are already obvious from context, skip the questions and write it (Dante prefers fewer questions).

### 2. Name

- Folder name is **kebab-case** and **is the invocation**: `.claude/skills/week-plannen/` → `/week-plannen`.
- Make it specific and verb/noun-clear. `weekly-ad-builder` beats `ads`.
- One skill = one folder = one `SKILL.md`.
- Check `.claude/skills/` first for a skill that already covers this. Overlapping skills get **merged, not parked next to each other** (feedback 19-09-2026).

### 3. Bronnen (do this before you write a word of the body)

Walk the source rule above and answer two questions out loud:
- **Which files must this skill read before it starts?** Those become the Bronnen block at the top of the body: a short list of path plus what to take from it. Spec and example in `reference.md`.
- **Which facts did I almost type into this skill?** Every one of those is a path instead. If the fact doesn't live anywhere yet, that's a gap: put it in the right `Context/` or `GTM/` file first, then point at it.

If a fact is genuinely unknown, it does not go in as a guess. It goes to `Context/open-vragen.md` and the skill gets a `> **Te toetsen (datum):**` line.

### 4. Write SKILL.md

Two required frontmatter fields: `name` and `description`. **The description is the most important line in the whole skill** because it's what Claude reads to decide whether to trigger. Get it right:
- Start with what it does, then list the **trigger phrases Dante actually uses**, in the language he uses them in. Most of his triggers are Dutch.
- Add **anti-triggers** where a neighbouring skill could steal the call ("NIET triggeren op X, dat is skill Y"). The `meddpicc` / `sso-grid` pair is the worked example.
- Be concrete about *when* to use it, not just what it is.
- Body stays **concise and skimmable**: Bronnen block, procedure, key IDs, done-state. Bullets over paragraphs. No em-dashes (house style).
- Put `_Laatst bijgewerkt: JJJJ-MM-DD._` under the H1, same convention as the context files. Without a date you can't tell an old skill from a current one.

Real templates in this repo, pick the closest shape:
- `cro/SKILL.md` - persona plus method, reads a handbook first.
- `week-plannen/SKILL.md` - a guided session that reads `Context/` and writes to Todoist.
- `lead-sourcing/SKILL.md` - an agent step with a market profile, a page budget and a `LEERPUNTEN.md`.
- `meddpicc` next to `sso-grid` - how two neighbouring skills fence each other off.

### 5. Split out detail (progressive disclosure)

The SKILL.md stays lean. Anything long or rarely-needed goes in a **separate file in the same folder** that the SKILL.md points to by name:
- `reference.md` - technical spec, schemas, edge cases.
- `examples/` - sample outputs, templates.
- `LEERPUNTEN.md` - for a skill that runs repeatedly and gets corrected (see `reference.md`).
- data files, scripts, market profiles.

Claude only pulls these in when the task needs them, so the main skill loads fast.

### 6. Test it triggers

- Confirm the folder + `SKILL.md` exist and the frontmatter parses (valid YAML, `name` + `description` present).
- The skill list refreshes on a new Claude Code session. Tell Dante to start a fresh session and type `/<name>` to confirm it appears.
- Read the description back as a router: would it fire on the phrases Dante uses, and would it stay quiet on a neighbouring skill's phrases?
- **Follow every path in the Bronnen block.** A dead path in a brand new skill is the most common defect.

### 7. Log + tidy

- Append a one-line entry to `Decisions/log.md` (per CLAUDE.md format) when the skill is a meaningful addition.
- If the new skill matches an item in the CLAUDE.md "Skills to Build" backlog, point that out so Dante can cross it off.
- Replacing an older skill? Archive it, don't delete it, and leave a pointer. See `reference.md`.

## Keep it alive after it ships

Building the skill is half the job. The rule that keeps it true is `.claude/rules/skill-onderhoud.md`, and it applies in every session, not only inside this skill. The short version:

- **Runs a skill, or the conversation touches its subject? Test it against what you now know.**
- **Paths, IDs and facts that demonstrably moved:** fix them the same turn, report in one line.
- **Procedure, triggers, output, splitting or merging:** lay the exact text in front of Dante first.
- **Not sure:** mark it with `> **Te toetsen (datum):**`, never guess, and put the question in `Context/open-vragen.md`.
- **Never** change a skill silently, and never delete one.

When you're repairing rather than building, run the same loop from step 3: the fix is almost always "this fact should have been a path".

## Quick checklist before calling it done

- [ ] Folder is kebab-case, matches the intended `/command`, no overlap with an existing skill.
- [ ] `SKILL.md` has valid frontmatter: `name` + a trigger-rich `description`, with anti-triggers where a neighbour could steal it.
- [ ] `_Laatst bijgewerkt:_` date sits under the H1.
- [ ] Bronnen block at the top: every living source by path, with what to take from it.
- [ ] No fact copied in that already lives in `Context/`, `Platform/`, `GTM/` or Close.
- [ ] Every path in the skill actually exists (check them, don't assume).
- [ ] Body is concise, bulleted, no em-dashes, has the steps + key IDs + done-state.
- [ ] Deep detail lives in `reference.md` / sibling files, not crammed into SKILL.md.
- [ ] You told Dante how to confirm it shows up (`/name` in a fresh session), and named every change you made.
