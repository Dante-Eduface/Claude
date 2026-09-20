# Skill Builder - Technical Reference

_Laatst bijgewerkt: 2026-09-20._

The rules and schema behind a Claude Code skill. The `SKILL.md` in this folder is the process; this is the spec. Read this when you're actually writing the files.

## What a skill is

A skill is a folder under `.claude/skills/` containing a `SKILL.md` file. The folder name is how the skill is invoked (`/folder-name`). Claude reads every skill's `description` at session start and decides when to trigger one. The body and any sibling files are loaded only when the skill is actually used (progressive disclosure), so they don't cost context until needed.

```
.claude/
  skills/
    skill-builder/
      SKILL.md        <- required, the entry point
      reference.md    <- optional, this file
      LEERPUNTEN.md   <- optional, corrections this skill must read first
      examples/       <- optional, templates/sample outputs
      scripts/        <- optional, helper scripts
```

That "only loaded when it fires" property is also the reason skills rot quietly. Nobody opens a skill between runs, so a wrong fact inside one survives far longer than a wrong fact in a context file. Everything below about sources exists because of that.

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

Good description traits:
- Names the **literal phrases** Dante uses, in the language he uses them in. Most of his triggers are Dutch, so write them in Dutch even if the body is English.
- States the **situation** (a cron, a stage of work, a kind of request).
- Says what it's **anchored to** if it depends on other files or skills.

### Anti-triggers

When two skills sit next to each other, the description has to fence them off explicitly, or the wrong one fires and does confident work on the wrong job. Say what it must **not** trigger on and name the neighbour:

> "NIET triggeren op 'kwalificeer deze deal', 'score deze deal', 'vul de grid in' (dat is meddpicc)."

That line is from `sso-grid`, and the pair `meddpicc` / `sso-grid` is the worked example in this repo: one scores the deal, the other only renders an already-filled grid. Same vocabulary, different jobs. Without the anti-trigger they ate each other's calls.

Where an anti-trigger is not enough because the skills genuinely overlap, **merge them instead of parking them side by side**. On 19-09-2026 `cro`, `schrijven`, `outreach` and `meddpicc` each swallowed their duplicate. `sso-grid` stayed separate because the split is deliberate.

## The Bronnen block

Every SKILL.md opens its body with a short block naming the living files it reads. It is the mechanism behind the source rule in `SKILL.md`: the skill holds the procedure, the block holds the pointers, and nothing gets transcribed.

```markdown
## Bronnen, lees deze eerst

- `Context/current-priorities.md` - het blokkenschema en de leidende maat. Wint van alles hieronder.
- `Context/me.md` - zijn weekritme, de treintijden.
- `GTM/Pricing/prijsmodel-psu-26-27.md` - nooit een prijs uit het hoofd noemen.
- `LEERPUNTEN.md` (deze map) - wat er de vorige rondes misging.
```

Rules for the block:
- **Path plus what to take from it.** "see Context" is useless; "the block schedule, before you plan anything" is actionable.
- **Only what this skill actually needs.** Every path costs context when the skill runs. `fitness-coach` reads `Context/personal.md`, not `Context/eduface.md`, and the other way round for a sales skill. See `.claude/rules/context-loading.md`.
- **Say which source wins** when two could disagree. `Context/current-priorities.md` beats every other context file; `Platform/product.md` beats any product claim in the skill; Close beats any deal state written down anywhere.
- **Check each path exists** before you call the skill done. A dead path in a brand new skill is the most common defect.

### What may stay in the skill

Only three things:
1. **The procedure.** Steps, order, judgement calls, guardrails, done-state.
2. **IDs the step cannot run without.** Campaign IDs, Todoist section IDs, pipeline IDs. Collect them under one heading with the date they were verified, so a repair is one block instead of a hunt. Anything that varies per market or per client goes into a profile file the skill reads.
3. **Style rules specific to this skill.** House style lives in `.claude/rules/communication-style.md`, not in each skill.

## Dating a skill

Put `_Laatst bijgewerkt: JJJJ-MM-DD._` directly under the H1, same convention as the context files. Update it on every change.

Without a date you can't tell a current skill from one that was written against a world that no longer exists, so everything gets treated as equally reliable. That is exactly how `fitness-coach` kept coaching on WHOOP data months after Dante stopped wearing one.

## One skill with a parameter beats N copies

When a workflow varies along one axis (market, language, client), build **one** skill that takes the axis as an argument and reads a profile file, not one skill per value.

The SHIFT pipeline is the worked example. It used to be `lead-sourcing-nl`, `contact-sourcing-nl`, `linkedin-outreach`, `lemlist-import-nl`. Since 10-09-2026 it is five market-agnostic skills that each take `--markt <code>` and read `GTM/ICP/shift/markets/<code>/profiel.json` for the sources, the title ranking, the vocabulary and the Lemlist campaign ID. Adding the UK meant adding a folder, not cloning four skills.

Signs you're about to build a copy instead of a parameter: the two skills differ only in nouns, or you find yourself pasting a block and changing three words.

## Budget, batch size and model

A skill that fetches things (web pages, PDFs, CRM records, Lemlist activity) states its limits in the body. Per `.claude/rules/credits.md`, "be frugal" does nothing; hard numbers do:

- **Page budget per record** - how many sources before the answer is `onbekend`.
- **Batch size** - so a session doesn't fill up. Everything fetched earlier travels along in every later step.
- **Stop condition** - the moment the answer is found, stop. Name it explicitly.
- **Which model the step runs on** - mechanical scanning on Haiku, sourcing and imports on Sonnet, research and writing on Opus. If the skill runs as a subagent, say so in the body.
- **A cheap probe before an expensive fetch** - `pipeline.py peiling` is the pattern: one small call that answers "did anything change" before pulling everything.

Calibration, measured 16-09-2026: pulling 105 Lemlist leads with their activities cost 271.000 tokens while the data itself was 22.000. The difference was the number of calls.

## LEERPUNTEN.md

A skill that runs repeatedly and gets corrected repeatedly gets a `LEERPUNTEN.md` next to its `SKILL.md`, and the body's first instruction is to read it. Without it, every round repeats last round's mistake.

Give one to a skill when all of these hold: it runs in batches or on a schedule, Dante reviews the output, and the corrections are about *how the step works* rather than about one record. The four SHIFT agents have one (`lead-sourcing`, `contact-sourcing`, `shift-research` via `.claude/agents/`, `outreach`).

Structure: a table of the skill's steps at the top, then entries filed against a step. Feedback that points at a step is actionable; feedback about the end result is not, so ask which step it was instead of guessing. Corrections about a single record go to the record, never here.

## Progressive disclosure (keep SKILL.md lean)

Claude loads the SKILL.md body when the skill fires, and sibling files only when the body tells it to read them. So:
- Put the **Bronnen block, procedure, key IDs, and done-state** in SKILL.md.
- Push **schemas, long examples, large data, edge cases** into `reference.md` or other files.
- Reference siblings **by name** from SKILL.md, e.g. "Read `reference.md` in this folder for the schema." Relative-to-the-skill-folder naming is the safe convention.

A SKILL.md that runs past ~150-200 lines is usually a sign detail should move into a reference file.

## Naming conventions

- Folder: `kebab-case`, specific, action-or-domain clear. This is the `/command`. Lowercase with hyphens is mandatory under `.claude/` because commands and scripts depend on it (`Context/kaart.md`).
- One responsibility per skill. If a skill is doing two unrelated jobs, split it.
- Don't collide with existing skill names. Check `.claude/skills/` first.

## Replacing, archiving and repairing

**Never delete a skill.** Move the folder to `Archive/skills/`, or to `Archive/skills-<jaar-maand>/` when a batch goes at once, and name its replacement. `/task-planning` sits in `Archive/skills-2026-09/` since 19-09-2026, replaced by `/week-plannen`; the entry in the CLAUDE.md backlog was struck through rather than removed, so the history stays readable.

**Leave a pointer inside the archived skill**, because the old name still gets typed and the old `SKILL.md` still gets read. `Archive/skills/lead-sourcing-nl/SKILL.md` is the model: the `description` itself starts with "VERVANGEN op 2026-09-10 door `lead-sourcing`", and the body opens with one blockquote saying which skill to use instead, with which argument, and that everything below is frozen.

**When the ground under a skill disappears but a rewrite wasn't asked for**, mark it instead of rewriting it. A warning header at the top of the body: what no longer holds, and which file wins. That is how `fitness-coach` was handled on 20-09-2026. A rewrite Dante didn't ask for is scope creep; leaving a confident wrong skill in place is worse than both.

**Repair, not rebuild, is usually right.** When `/task-planning` was found broken on 19-09-2026 it was broken on four axes at once: it read a context file that no longer existed, its whole priority ladder hung on goals that had been dropped, three of four Todoist projects were gone, and four of eight section IDs were wrong. A search-and-replace would have fixed the references and left the ladder wrong, which is worse than an obviously broken skill: it prioritises convincingly against the wrong goals. Check all four kinds of rot, not the one that showed up.

The full rule for keeping skills current after they ship is `.claude/rules/skill-onderhoud.md`.

## Testing a skill

1. **Frontmatter parses** - valid YAML, `name` + `description` present, `---` fences correct.
2. **It appears** - skills are picked up on a fresh Claude Code session. Restart/reopen, then check the skill list or type `/<folder-name>`.
3. **It triggers** - read the description back as if you were routing: would it fire on the phrases Dante actually says, and stay quiet on a neighbour's?
4. **The paths resolve** - open every file in the Bronnen block and every ID block. Dead paths are the most common defect.
5. **It runs** - walk the body once on a real example. Fix any missing IDs, paths, or steps.

## Common mistakes

- **Copying data instead of pointing at it.** The big one. Reference the handbook, CRM or context by path; don't duplicate it into the skill where it will go stale in silence. On 20-09-2026 only 2 of 29 skills referenced anything in `Context/`.
- **Pointing at a path that no longer exists.** `skill-builder` itself pointed at `.claude/skills/hot-lead-outreach/` long after that folder was gone.
- **No date on the skill.** You can't tell current from ancient, so everything reads as equally trustworthy.
- **Empty or missing frontmatter.** A `SKILL.md` with no `name`/`description` won't behave as a skill (it shows up as a placeholder, e.g. description "Skill").
- **Vague description.** It either never fires or fires on the wrong things. Add concrete triggers.
- **No anti-trigger next to a lookalike skill.** The neighbour steals the call.
- **Cloning a skill per market or client** instead of taking a parameter and reading a profile.
- **Everything in SKILL.md.** Long skills bloat context and bury the procedure. Split into reference files.
- **Folder name mismatch / not kebab-case.** Breaks or confuses invocation.
- **Building skills nobody asked for.** Per CLAUDE.md, build organically from repeated requests, not speculatively.
- **No budget on a skill that fetches.** It will run until the session is full.
- **Em-dashes / hype / padding.** House style (see `.claude/rules/communication-style.md`): concise, bulleted, no em-dashes.

## Minimal skeleton to copy

```markdown
---
name: my-skill
description: <action>. Use when Dante says "<phrase>" or "<phrase>", or when <situation>. NIET triggeren op "<phrase>" (dat is <neighbour>). <scope/anchor>.
---

# My Skill

_Laatst bijgewerkt: JJJJ-MM-DD._

One line on what this does and when.

## Bronnen, lees deze eerst
- `<pad>` - <wat je eruit haalt, en wanneer>
- `<pad>` - <wat je eruit haalt>

## De loop
1. ...
2. ...

## ID's (gecontroleerd JJJJ-MM-DD)
- ...

## Budget
- <paginabudget / batchgrootte / stopvoorwaarde / model>

## Klaar als
- What a successful run looks like.
```
