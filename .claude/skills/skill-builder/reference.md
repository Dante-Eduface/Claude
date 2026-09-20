# Skill Builder — Technical Reference

The rules and schema behind a Claude Code skill. The `SKILL.md` in this folder is the process; this is the spec. Read this when you're actually writing the files.

## What a skill is

A skill is a folder under `.claude/skills/` containing a `SKILL.md` file. The folder name is how the skill is invoked (`/folder-name`). Claude reads every skill's `description` at session start and decides when to trigger one. The body and any sibling files are loaded only when the skill is actually used (progressive disclosure), so they don't cost context until needed.

```
.claude/
  skills/
    skill-builder/
      SKILL.md        <- required, the entry point
      reference.md    <- optional, this file
      examples/       <- optional, templates/sample outputs
      scripts/        <- optional, helper scripts
```

## Frontmatter schema

`SKILL.md` must start with a YAML frontmatter block. Two fields are required.

```yaml
---
name: skill-builder
description: One or two sentences. What it does + the exact trigger phrases/situations.
---
```

| Field | Required | Notes |
|-------|----------|-------|
| `name` | yes | Display name. Keep it aligned with the folder. Folder name (kebab-case) is what drives `/invocation`. |
| `description` | yes | The single most important field. This is what Claude matches against to fire the skill. Lead with the action, then list real trigger phrases and *when* to use it. |
| `allowed-tools` | no | Comma-separated allowlist to restrict which tools the skill may use (e.g. `Read, Edit, Bash`). Omit to inherit all available tools. Use only when you want to sandbox the skill. |

Rules for the frontmatter:
- It must be valid YAML between two `---` lines, at the very top of the file, nothing above it.
- `description` should be specific. Vague descriptions ("helps with sales") trigger unpredictably. Concrete triggers ("use when Dante says 'run the hot leads'") fire reliably.
- Don't stuff the whole procedure into the description. It's a router, not the manual.

## Writing a description that triggers well

The description does double duty: it tells Claude **what** the skill does and **when** to reach for it. Pattern that works:

> `<Action / what it produces>. Use when <trigger phrase 1>, <trigger phrase 2>, or <situation>. <One line on scope or what it anchors to>.`

Example (from `hot-lead-outreach`):
> "Daily hot-lead engine. Each morning, find hot leads in Lemlist, draft the perfect LinkedIn DM + email per lead... Trigger on the morning cron, or when Dante asks to 'run the hot leads' / 'check Lemlist for hot leads'."

Good description traits:
- Names the **literal phrases** Dante uses.
- States the **situation** (a cron, a stage of work, a kind of request).
- Says what it's **anchored to** if it depends on other files/skills.

## Progressive disclosure (keep SKILL.md lean)

Claude loads the SKILL.md body when the skill fires, and sibling files only when the body tells it to read them. So:
- Put the **procedure, key IDs, and done-state** in SKILL.md.
- Push **schemas, long examples, large data, edge cases** into `reference.md` or other files.
- Reference siblings **by name** from SKILL.md, e.g. "Read `reference.md` in this folder for the schema." Relative-to-the-skill-folder naming is the safe convention.

A SKILL.md that runs past ~150–200 lines is usually a sign detail should move into a reference file.

## Naming conventions

- Folder: `kebab-case`, specific, action-or-domain clear. This is the `/command`.
- One responsibility per skill. If a skill is doing two unrelated jobs, split it.
- Don't collide with existing skill names. Check `.claude/skills/` first.

## Linking to other skills and context

- Skills can lean on other skills. `hot-lead-outreach` defers message voice to `cro`. State the dependency in the body ("read that skill's logic when drafting").
- Skills can point at repo context: handbooks in `GTM/Knowledge/`, project READMEs in `GTM/` en `Design/`, context files in `Context/`. Reference them by path so the skill stays the single source of the workflow, not a copy of the data.

## Testing a skill

1. **Frontmatter parses** — valid YAML, `name` + `description` present, `---` fences correct.
2. **It appears** — skills are picked up on a fresh Claude Code session. Restart/reopen, then check the skill list or type `/<folder-name>`.
3. **It triggers** — read the description back as if you were routing: would it fire on the phrases Dante actually says? Tighten if not.
4. **It runs** — walk the body once on a real example. Fix any missing IDs, paths, or steps.

## Common mistakes

- **Empty or missing frontmatter.** A `SKILL.md` with no `name`/`description` won't behave as a skill (it shows up as a placeholder, e.g. description "Skill").
- **Vague description.** It either never fires or fires on the wrong things. Add concrete triggers.
- **Everything in SKILL.md.** Long skills bloat context and bury the procedure. Split into reference files.
- **Folder name mismatch / not kebab-case.** Breaks or confuses invocation.
- **Building skills nobody asked for.** Per CLAUDE.md, build organically from repeated requests, not speculatively.
- **Em-dashes / hype / padding.** House style (see `.claude/rules/communication-style.md`): concise, bulleted, no em-dashes.
- **Copying data instead of pointing at it.** Reference the handbook/CRM/context by path; don't duplicate it into the skill where it'll go stale.

## Minimal skeleton to copy

```markdown
---
name: my-skill
description: <action>. Use when Dante says "<phrase>" or "<phrase>", or when <situation>. <scope/anchor>.
---

# My Skill

One line on what this does and when.

## The loop
1. ...
2. ...

## Key IDs / paths
- ...

## Done
- What a successful run looks like.
```
