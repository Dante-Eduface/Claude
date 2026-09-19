# Stakeholder Mapping — Techniques

The detailed how-to per step. SKILL.md is the process, this is the method. All techniques are generalized from the RUG deal so they apply to any education institution. No institution-specific names are hardcoded.

---

## Step 1 — Find & verify the people

Goal: a verified list of the people who touch this decision, each with exact function and team.

**Sources, in order of trust:**
- **Staff / profile pages** (e.g. `<university>.nl/staff/<initials>`). Quote the function title verbatim. Note department and team if listed.
- **Department / team roster pages** (e.g. `<university>.nl/staff/departments/<id>`). These show who sits in which team, the teamlead, and colleagues.
- **Contact / "about the team" pages.** Often name team membership that the person's own profile leaves out.

**Verification rules:**
- A profile page frequently lists only the umbrella department, not the specific team. When the team is not on the person's own page, **confirm it from a second source** (a roster page and/or a contact page) before you state it.
- Watch for the same unit appearing under two names (a Dutch and an English label, or a recent rename with the same ID and teamlead). Treat same-ID + same-lead as the same team, and flag the naming discrepancy rather than inventing two teams.
- Some rosters are JavaScript-rendered and will not load via a plain fetch. If a page won't render, say so honestly and fall back to a search-indexed version or a second source. Do not guess the roster.

**Adversarial validation (for contested membership):**
- When it matters which team someone is in, spawn parallel sub-agents to check *every* candidate team's roster for that name, plus the person's own page and the contact page. Require two independent confirmations before locking the team. This is exactly how a wrong "not in any team" assumption gets caught.

---

## Step 2 — Determine each person's role in the deal

Goal: turn the verified name list into a role map using handbook vocabulary.

**Reporting line first.** Reconstruct who reports to whom, up to the likely economic buyer. Role only makes sense inside the hierarchy (a coordinator three levels down is not your EB, however friendly).

**Public signals (LinkedIn + institutional posts):**
- Read recent posts and stated expertise for leanings. Someone publicly enthusiastic about the problem you solve is a champion candidate; someone who is the public face of a competing internal approach is an enemy candidate.
- Note dual-role risk: the person who leads the team that builds the internal tool is either your strongest champion (sees buying as the smart route) or your biggest enemy (wants to keep building). Their public tone tells you which way they lean. That person is priority #1 to pull your way.

**Classify to handbook roles** (see `cro`): EB, champion, coach, enemy, ally (e.g. privacy/security gate you can win), fan (interested but no line authority, e.g. a data scientist), swing/decision-maker (holds the build-vs-buy call).

**Second champion route (do this deliberately):**
- Do not stop at the core IT / edtech department. Look for an academic sponsor in a faculty who owns the outcome (student success, retention, assessment quality). A prize-winning learning-analytics lead, a vice-dean of education, a data scientist. Work this route in parallel to the IT route.

---

## Step 3 — Mine strategic fit (their own words)

Goal: the hooks that make each stakeholder care, pulled from the institution's own documents so it is their language, not our pitch.

- **Instellingsbegroting (institutional budget):** find strategic priorities and any AI / digital-sovereignty language. If leadership has committed to "AI en digitale soevereiniteit" or similar, that is the EB-level hook to align to.
- **Faculty plans:** scan for their own phrasing of the pain, e.g. "minder arbeidsintensieve vormen", "inzet AI", "bezuinigingen". Quote it back to them.
- Map each hook to the stakeholder it speaks to (sovereignty → CIO/EB; workload → faculty; assessment quality → academic champion).

Keep this qualitative here. Turning a budget line into a euro case is the future figures module, not this one.

---

## Step 4 — Detect a self-built tool (generalized, no hardcoded names)

Goal: find out whether the institution already runs an internal, homegrown assessment/grading tool, because that shapes the whole buy-vs-build dynamic and reveals the enemy. **Never search for a specific product name from a previous deal.** Test for the pattern.

**The aspects to establish for any such tool:**
- **Homegrown or bought?** Internally built (by an in-house scrum/dev team) vs an external vendor product they license.
- **Manual or AI?** Does it actually do AI feedback/grading, or is it a manual rubric/workflow tool with an "AI" label? Verify, do not assume from the name.
- **Scope and limits.** What does it cover (e.g. multiple-choice, structured rubrics) and, crucially, where does it stop (e.g. open-text marking and real feedback still fall on lecturers)? The gap is the opening.
- **Public face = enemy.** Find who publicly represents the self-build. Vendor case studies and edtech-conference pages (e.g. D2L, OEB and similar) name the institution's spokesperson for its homegrown stack. That person's portfolio is threatened by an external tool, so they are the likely enemy.
- **Separate build tracks.** There may be more than one: an IT-department tool and a separate academic/faculty experiment. Note both.

**How to test:** vendor case-study pages, edtech-conference talks, the institution's own IT/education-services pages, and a direct question to your contact ("you mentioned you built X yourselves, how did that start, who owns it, and where does it stop?"). Confirm manual-vs-AI explicitly, it is the most common wrong assumption.

Detecting the tool and its owner is in scope. Costing it or building its business case is not.

---

## Output format

- Reuse `GTM/Accounts/rug-groningen/onderzoek/organogram.html` as the visual template: tiers (directie → domain managers → teams), clean role-color-coded cards, optional faces, a legend, and a short CRO-assessment box.
- Render HTML to PDF with headless Chrome (`--print-to-pdf`), landscape A4 for a wide org.
- If Dante wants it fast, a role table (person | function | role | why) is a fine lighter output.

## What NOT to do here

- No cost figures, ROI, jaarverslag spend analysis, or savings formula. Wrong module.
- No every-figure-must-be-cited rigor. That discipline is for the numbers module and burns credits this task does not need.
- No hardcoded product/tool/person names carried over from a prior institution.
