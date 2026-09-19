---
name: stakeholder-mapping
description: Map and verify the key stakeholders at an education institution for a deal, and classify each person's role (EB, champion, coach, enemy, ally, fan, swing). Produces an organogram / stakeholder map. Trigger when Dante says "map de stakeholders bij [instelling]", "key stakeholder analyse", "wie is wie bij [instelling]", "maak een organogram voor [instelling]", or "stakeholder mapping". This is stakeholder mapping ONLY, no figures, ROI or cost work (that is a separate future module). Reusable across institutions, generalized from the RUG deal.
---

# Stakeholder Mapping

Map who matters at a target institution and what role each person plays in the deal. Output is an **organogram / stakeholder map**, not a numbers dossier.

**Scope boundary (important):** this skill does stakeholder mapping only. Do NOT go researching cost figures, ROI, jaarverslag spend, or a self-built tool's business case here. Detecting *that* a self-built assessment tool exists (and who owns it) is in scope; costing it is not. If Dante wants numbers, that is a separate module, say so and stop.

Role vocabulary (EB, champion, coach, enemy, ally, fan, swing) follows the `cro` handbook. Read that skill's role definitions if unsure.

## The loop

1. **Confirm the target.** Institution name + which faculty/department the deal centers on (if known). If genuinely unclear, ask one question, else proceed.
2. **Find & verify the people.** Staff pages, department/team roster pages, contact pages. When a person's own profile omits their team, confirm the team from a second source before stating it. See `reference.md` step 1.
3. **Reconstruct the reporting line.** Who reports to whom, up to the likely economic buyer. This is what turns a name list into a map.
4. **Classify each role.** LinkedIn public signals + position + reporting line, mapped to handbook roles. Deliberately hunt for a **second champion route outside the core IT department** (e.g. an academic sponsor in a faculty). See `reference.md` step 2.
5. **Mine strategic fit.** Pull the institution's own words from its instellingsbegroting (strategic priorities, AI / digitale-soevereiniteit language) and faculty plans ("minder arbeidsintensief", "inzet AI"). These become the hooks to align stakeholders to. See `reference.md` step 3.
6. **Detect a self-built tool (generalized).** Test whether the institution runs an internal, homegrown assessment/grading tool. Do NOT look for any specific product name. Characterize it by aspects: homegrown yes/no, manual vs AI, scope and limits, and who is its public face (that person is the likely enemy). See `reference.md` step 4.
7. **Build the map.** Render the visual by invoking the **`organogram` skill** (do not hand-roll the HTML here). Pass it the verified people list: name, title, reporting line, deal-role, and confirmed-vs-inferred + source per node. The organogram skill owns the print-perfect output (real validated photos, cards that never break across a page, members-only, inferred = reason + source). Optionally also give Dante a role table. NB: the self-build detection from step 6 informs role classification (who is the enemy) but does NOT go on the organogram itself — the chart is members-only.

## Always-on discipline (cheap, keep it on)

- Honest "not found" beats guessing. If a role or team can't be verified, say so.
- Verify before assuming (a tool being "AI" or a person being "the owner" must be checked, not inferred).
- Do NOT apply source-rigor-for-numbers here (every-figure-cited, estimates-labeled). That belongs to the future figures module and costs credits this task does not need.

## Running it efficiently

- Single focused ask ("map de stakeholders") = run inline, tight scope, no tool-costing detours.
- Full new-account map = fan out the reference.md steps as **parallel sub-agents** (person-finding, role-classification, strategic-fit, tool-detection), then merge into one organogram. Use adversarial validation for any contested team membership (see reference.md step 1).

## Output

- An organogram/stakeholder map, rendered via the **`organogram` skill** (it enforces the print/photo/inference rules), OR a role table if Dante wants it fast.
- Reporting line + role per person + a short CRO-style read (who to win, who to protect against).

## Done

- Every key player named, verified, placed in the reporting line, and role-classified.
- A second champion route considered (not just the core IT department).
- Any internal self-built tool flagged with its aspects + likely owner, without costing it.
