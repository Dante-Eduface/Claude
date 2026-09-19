---
name: skill-builder
description: Build a new Claude Code skill, or fix/upgrade an existing one. Use when Dante says "make this a skill", "turn this into a skill", "build a skill for X", or when you notice a workflow being repeated and want to capture it. Walks the full loop: scope the workflow, write the SKILL.md frontmatter + body, add reference files, and test that the skill triggers. Anchors to the Eduface "build skills organically" rule and the skills backlog in CLAUDE.md.
---

# Skill Builder

This is the meta-skill: it builds other skills. Use it whenever a recurring workflow is ready to be captured as a reusable `.claude/skills/<name>/SKILL.md`.

Read `reference.md` (in this folder) for the full technical spec: frontmatter schema, directory layout, progressive disclosure, naming, and common mistakes. This file is the *process*. `reference.md` is the *rules*.

## When to build a skill

Build one when **all three** are true:
- The same request has come up **2+ times** (or Dante explicitly asks for a skill).
- There's a **repeatable procedure** worth writing down, not a one-off.
- It ladders up to the work that matters (pipeline, pilots, webinar, website).

Per CLAUDE.md, skills at Eduface are built **organically**. Don't pre-build skills nobody has asked for. The backlog of candidate workflows lives in CLAUDE.md under "Skills to Build". When you finish one, suggest crossing it off.

If it's a one-off, don't make a skill. Just do the task.

## The build loop

```
1. SCOPE      what triggers it, what it does, what tools/IDs it needs, what "done" looks like
2. NAME       kebab-case folder name = how it's invoked (/name)
3. WRITE      SKILL.md frontmatter (name + description) then the body
4. SPLIT      move deep detail / data / long examples into reference files
5. TEST       confirm it shows up and triggers
6. LOG        decision log + suggest removing it from the backlog
```

### 1. Scope (ask before writing)

Don't write a skill from a vague ask. Pin down, in 1–2 quick questions if needed:
- **Trigger** — what words or situation should fire it? (This becomes the description.)
- **Steps** — the actual procedure, in order.
- **Inputs/IDs** — campaign IDs, project IDs, file paths, MCP servers it touches.
- **Output + review surface** — what it produces and where Dante reviews it.
- **Done** — what a successful run looks like.

If the answers are already obvious from context, skip the questions and write it (Dante prefers fewer questions).

### 2. Name

- Folder name is **kebab-case** and **is the invocation**: `.claude/skills/hot-lead-outreach/` → `/hot-lead-outreach`.
- Make it specific and verb/noun-clear. `weekly-ad-builder` beats `ads`.
- One skill = one folder = one `SKILL.md`.

### 3. Write SKILL.md

Two required frontmatter fields: `name` and `description`. **The description is the most important line in the whole skill** because it's what Claude reads to decide whether to trigger. Get it right:
- Start with what it does, then list the **trigger phrases** Dante actually uses.
- Be concrete about *when* to use it, not just what it is.
- Keep the body **concise and skimmable**: short procedure, key IDs, where the automation lives. Bullets over paragraphs. No em-dashes (house style).

Look at the two existing skills in this project as your templates:
- `.claude/skills/cro/SKILL.md` — a "persona + method" skill that reads a handbook first.
- `.claude/skills/hot-lead-outreach/SKILL.md` — an "operational loop" skill with IDs, cron, and a clear done-state.

### 4. Split out detail (progressive disclosure)

The SKILL.md should stay lean. Anything long or rarely-needed goes in a **separate file in the same folder** that the SKILL.md points to by name:
- `reference.md` — technical spec, schemas, edge cases.
- `examples/` — sample outputs, templates.
- data files, scripts, etc.

Claude only pulls these in when the task needs them, so the main skill loads fast. See `reference.md` for how to reference sibling files correctly.

### 5. Test it triggers

- Confirm the folder + `SKILL.md` exist and the frontmatter parses (valid YAML, `name` + `description` present).
- The skill list refreshes on a new Claude Code session. Tell Dante to start a fresh session (or reopen Claude Code) and type `/<name>` to confirm it appears.
- Sanity-check the description: would it actually fire on the phrases Dante uses? If not, tighten it.

### 6. Log + tidy

- Append a one-line entry to `decisions/log.md` (per CLAUDE.md format) when the skill is a meaningful addition.
- If the new skill matches an item in the CLAUDE.md "Skills to Build" backlog, point that out so Dante can cross it off.

## Quick checklist before calling it done

- [ ] Folder is kebab-case, matches the intended `/command`.
- [ ] `SKILL.md` has valid frontmatter: `name` + a trigger-rich `description`.
- [ ] Body is concise, bulleted, no em-dashes, has the steps + key IDs.
- [ ] Deep detail lives in `reference.md` / sibling files, not crammed into SKILL.md.
- [ ] You told Dante how to confirm it shows up (`/name` in a fresh session).
