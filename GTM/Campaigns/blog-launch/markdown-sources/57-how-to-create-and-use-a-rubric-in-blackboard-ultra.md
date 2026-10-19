---
title: "How to Create and Use a Rubric in Blackboard Ultra: Points, No-Points Rubrics, Grading and AI Generation"
seo_title: "Create a Rubric in Blackboard Ultra, Step by Step | Eduface"
meta_description: "How to create a rubric in Blackboard Ultra, pick a type (points, percentage, no points), attach it, grade with it, copy it and generate one with AI."
slug: how-to-create-and-use-a-rubric-in-blackboard-ultra
primary_query: "create rubric blackboard ultra"
secondary_queries: ["create rubric in blackboard ultra", "blackboard ultra rubrics", "blackboard ultra import rubric", "blackboard ultra copy rubric", "blackboard ultra grading rubric", "grade with rubric blackboard ultra", "blackboard ultra rubric points", "blackboard ultra rubric types", "ai rubric generator blackboard", "blackboard ultra edit rubric"]
type: werkwijze
category: Product
hub: /resources/blog/ai-essay-grader-blackboard-lti
related: [/resources/blog/how-to-grade-assignments-in-blackboard-ultra, /resources/blog/blackboard-ultra-ai-grading, /resources/blog/how-to-write-a-rubric-ai-can-mark-against]
review_by: 2026-12-15
status: concept
components: "10 figures, 6 tables, 4 card grids, 7 callouts. Card grids use the [CARDS: n] ... [/CARDS] notation, one item per line as '- **Title** | text'. All figures are schematic diagrams, not Blackboard screenshots."
note: "Every click path, limit and setting name comes from Anthology's Blackboard Help for Instructors, read October 19, 2026. Blackboard AI licensing after June 30, 2026 could not be confirmed; see the comment above References. Series: 56 (grading), 57 (this post), 58 (AI grading)."
---

EYEBROW: BLACKBOARD ULTRA · RUBRICS

# How to Create and Use a Rubric in Blackboard Ultra: Points, No-Points Rubrics, Grading and AI Generation

*Every step from a blank Course Rubrics page to a graded submission: which of the five rubric types to pick, how to attach, copy, export and reuse a rubric, what the AI Design Assistant can draft for you, and a worked example you can copy.*

By Eduface · October 2026 · 29 min read · Written for instructors, instructional designers and program directors at private and for-profit colleges that run Blackboard Ultra

You teach one of six sections of the same course, and four of those sections have different instructors. Everyone uses Blackboard Ultra, everyone has "a rubric", and nobody can say whether the rubrics match. One instructor typed a rubric into the course last year. Another pastes criteria into the assignment instructions. A third grades from a Word table on a second monitor. When a student asks why a colleague's section got a higher mark for the same work, you have no document to point to.

> **How do you create a rubric in Blackboard Ultra?**
> Open the Course Rubrics page, either from Gradebook Settings (Manage Course Rubrics) or from an assignment's Settings (Add Rubric in Grading & Submissions). Select Create, name the rubric, choose a type (percentage, percentage range, points, points range or no points), edit the criteria rows and achievement level columns, and select Save. Attach it to the assignment before you grade, because a rubric you have graded with can only be changed by making a copy. Each item takes one rubric.

> **Key takeaways**
> - Ultra has five rubric types: percentage, percentage range, points, points range and no points. Pick the type before you write a single descriptor, because changing it later clears text.
> - A rubric attaches to assignments, discussions and journals, one rubric per item. It does not attach to tests or to assignments that contain questions.
> - Once you have graded with a rubric you cannot edit it. You copy it, edit the copy, and the earlier grades become overrides that you can regrade.
> - The AI Design Assistant can draft a rubric if your administrator turned it on. Treat the output as a first draft and review every cell.
> - Ultra has no rubric import from Word or Excel. It exports and imports rubrics as zip files between Blackboard courses, and copies them between courses.

**In this guide**

[CARDS: 3]
- **1. Choose and build** | The five rubric types, a decision tree, and the exact click path to create a rubric, with every character limit.
- **2. Write and generate** | How to draft descriptors that two graders read the same way, a worked example, and what the AI Design Assistant does and does not do.
- **3. Attach and grade** | Associating a rubric, scoring a submission, criterion feedback, overrides, and what changes when you edit after grading.
[/CARDS]

[CARDS: 3]
- **4. Reuse and report** | Copying, exporting, importing, printing, the Rubric Evaluation Report, and parallel grading for consistency.
- **5. Fix problems** | A table of the errors people hit most and the fix for each.
- **6. Where Eduface fits** | What Blackboard handles natively, what a dedicated tool adds, and where it does not help.
[/CARDS]

## What rubric types does Blackboard Ultra offer, and which should you pick?

Blackboard Ultra offers five rubric types: percentage-based, percentage-range, points-based, points-range and no-points.² Anthology's overview page still says "four types" and leaves out no-points, but the Types of Rubrics page and the rubric generator both list five, so this guide uses five.¹ ² ³

The difference is how a performance level turns into a score. In a percentage-based rubric each criterion gets a weight, the weights must total 100%, and one performance level must be set to 100%. A level set to 80% awards 80% of that criterion's weight.² In a points-based rubric you assign points to each level instead, using whole numbers, and the total across the rubric must stay at or below 99,999.²

The two "range" types let you pick a value inside a band when you grade, for example 16 to 20 points for the top level. That helps when two submissions both belong in the top level but one is clearly stronger. Point ranges must progress from lower to higher values.²

| Rubric type | How the score works | Use it when | Watch out for |
|---|---|---|---|
| Percentage-based | Each criterion has a weight (total 100%); a level awards its percentage of that weight | The assignment point value may change, or you want weights visible | One level must be 100%; use Balance Criteria if weights do not total 100% |
| Percentage-range | Each level is a percentage band; you pick a value inside it | Strong work needs room to be distinguished | Copying a percentage-based rubric and switching to this type clears all descriptions |
| Points-based | Points sit on each level; whole numbers only | You want fixed, easy-to-explain point values | Total across the rubric must be 99,999 or less |
| Points-range | Each level is a band of points; you pick a value | Large point scales with graders who need discretion | Ranges must progress from lower to higher |
| No-points | Levels and feedback only, no numerical value | Formative work, or criteria you track without a grade | Produces no score on its own |

*Table 1: The five rubric types in Blackboard Ultra. Source: Anthology's Types of Rubrics and Manage Rubrics pages.*² ⁵

[FIGUUR: A decision tree titled "Which rubric type?" drawn as four question nodes joined by arrows, ending in five colored leaf cards. Node 1: "Does this work need a numerical grade?" No → leaf "No-points rubric" (gray). Yes → Node 2: "Will the assignment's point value change, or do you want weights to show?" Yes → Node 3: "Do you need room inside a level?" No → leaf "Percentage-based" (navy), Yes → leaf "Percentage-range" (navy outline). From Node 2 No → Node 4: "Do you need room inside a level?" No → leaf "Points-based" (green), Yes → leaf "Points-range" (green outline). A footer strip reads "Decide before writing descriptors: switching type later can clear them."]
*Figure 1: Two questions pick the rubric type: do you need a number, and do you need room to choose a value inside a level.*

A practical default for most summative writing assignments is percentage-based, because the weights stay readable and the rubric still works if you later change the points on the assignment. Use no-points for drafts. A no-points rubric lets you give criterion-by-criterion feedback on a first version without anything reaching the gradebook as a score.²

## How do you create a rubric in Blackboard Ultra, step by step?

You create a rubric on the Course Rubrics page, which you reach either from Gradebook Settings or from an assignment's Settings, and it takes six steps.³ Both routes land on the same page, so it makes no difference which one you use. The route from the assignment is handy because you can attach the rubric straight away.

[FLOWDIAGRAM] Route A: Gradebook → gear icon (Gradebook Settings) → Course Rubrics section → Manage Course Rubrics. Route B: Assignment → Settings icon → Grading & Submissions → Add Rubric. Both → Course Rubrics page → Create → name + type → edit cells → Save
*Figure 2: Two routes to the Course Rubrics page (schematic click path). From Route B you can also select a rubric and attach it with Save & Close.*

1. **Open the Course Rubrics page.** From Gradebook Settings, select Manage Course Rubrics in the Course Rubrics section. Or, from Assignment Settings, select Add Rubric in the Grading & Submissions section.³
2. **Select Create.** The page also offers generate, copy, edit, delete, import, export and print actions for existing rubrics.³ ⁵
3. **Name the rubric.** Titles can be up to 255 characters. If you leave the title empty, Blackboard names it "New Rubric" plus the date.³
4. **Select the rubric type.** Use Figure 1 if you are unsure.
5. **Edit the cells.** Hover over a column header or cell to see the edit icon. New rubrics start with four criteria rows and four achievement level columns. Select the plus sign where you want a new row or column, and delete what you do not need. You can delete all but one row and one column.¹ ³
6. **Select Save.** Select anywhere on the rubric to save your changes to a cell.³

When you add a level between two others, Blackboard assigns it a percentage automatically. A new level between 100% and 75% gets 88%, which you can change.³ Columns always run from the highest score to the lowest, and you cannot change that order.³

[FIGUUR: A schematic rubric grid titled "Anatomy of an Ultra rubric (schematic, not a screenshot)". Header row: a blank corner cell, then four column headers "Level 1 (highest)", "Level 2", "Level 3", "Level 4 (lowest)" with a bracket labeled "Achievement title: 40 characters max". Left column: four row headers "Criterion 1" to "Criterion 4" with a bracket labeled "Criteria and description cells: 1,000 characters max". A top banner reads "Rubric title: 255 characters max". Callout markers: (1) "Default size: 4 rows x 4 columns; no upper limit on rows or columns", (2) "Plain text only: pasted formatting is dropped", (3) "Enter confirms and exits edit mode, it does not start a new line", (4) "Columns always run highest to lowest". Optional "Align with goals" shown as a small tag on a criterion, labeled "Students cannot see aligned goals".]
*Figure 3: The limits that shape how you write a rubric cell: 40 characters for a level title, 1,000 for a description, plain text, and no line breaks.*

| Limit or behavior | What Anthology documents |
|---|---|
| Rubric title | 255 characters |
| Achievement level title | 40 characters |
| Criteria and description cells | 1,000 characters each |
| Formatting | Plain text only; pasted formatting does not carry over |
| Enter key | Confirms and leaves edit mode; no new paragraph in a cell |
| Size | Four rows and four columns by default; no limit on rows or columns |
| Devices | Rubrics are read-only on mobile and cannot be created at small screen widths |

*Table 2: Limits you will hit while building a rubric. Source: Anthology's Create or Generate Rubrics and Rubrics pages, read October 19, 2026.*¹ ³

Two limits matter more than they look. A 40-character level title forces short labels such as "Meets standard", so put the explanation in the description. And because the Enter key ends editing, a descriptor has to be one block of text. Write it as two or three sentences separated by semicolons or full stops, not as a list.³

> **Tip: align with goals**
> If your institution tracks learning goals, select Align with goals on a criterion to connect it. Anthology notes that students cannot see the goals you align with criteria in a rubric, so the connection is for your reporting, not for student guidance.³

## How do you generate a rubric with the AI Design Assistant?

If your institution has turned on the AI Design Assistant, you can generate a rubric from a short description, then review and edit every cell.³ If the option is missing, the cause is usually administrative: the assistant is opt-in, and administrators must activate it and give instructor roles the privilege to use it.¹³

Anthology's help page lists the steps:³

1. Open the Course Rubrics page (same two routes as above).
2. Enter a description to narrow the focus of the rubric.
3. Select the rubric type: percentage, percentage range, points, point range or no points.
4. Adjust the complexity of the rubric.
5. Define the number of columns and rows.
6. Optional: open Advanced options to change the output language.
7. Select Generate.
8. Review each cell for accuracy and edit as needed.
9. Select Continue to save the rubric.

The help page does not name the control that opens the generator, so look for it on the Course Rubrics page next to Create. The AI Design Assistant offers ten complexity levels, from early primary school to advanced PhD level, so set it to the level of your course, usually undergraduate lower or upper division.¹² It can write the rubric in many languages, including American English.¹²

[FLOWDIAGRAM] 1 Describe (assignment, outcome, audience) → 2 Choose type, complexity, rows and columns → 3 Generate → 4 Review every cell (observable? distinguishable? matches your outcomes?) → 5 Edit (shorten level titles to 40 characters, tie descriptors to your assignment) → 6 Continue to save → 7 Test on two sample submissions
*Figure 4: Generating a rubric is the start of the work, not the end. Steps 4, 5 and 7 are yours.*

What the assistant does is limited, and Anthology says so. Blackboard's administrator documentation describes the function as suggesting "a grading rubric with structure and criteria against a given assessment", and tells instructors to review text output before use.¹³ It states that the assistant works from limited course information, such as the course title and description, plus any extra context you type. It also warns against asking for sources or references, because testing found accuracy problems with such output.¹³

[FIGUUR: A horizontal time bar chart titled "Time to a usable rubric (EXAMPLE minutes, yours will differ)". Three bars on a shared 0 to 50 minute axis. Bar 1 "Write from scratch": 45 minutes, all navy ("write 16 cells"). Bar 2 "Generate, then review and edit": 3 minutes teal ("describe and generate") + 22 minutes navy ("review, rewrite, test") = 25 minutes. Bar 3 "Copy an existing rubric and adjust": 8 minutes. A note on the right of bar 2: "Review time is not optional: the 22 minutes is where the rubric becomes yours."]
*Figure 5: Generation can save time, but the review step is where the quality comes from. All minutes are illustrative.*

Two practical points follow from Anthology's documentation. First, keep personal information out of the prompt: Anthology's administrator page suggests that institutions advise instructors not to put personal or other confidential information in prompts, and Microsoft's Azure OpenAI service reviews prompts and output for content filtering and stores them for up to 30 days.¹³ A rubric prompt never needs a student's name. Second, ask the assistant for a rubric against your own learning outcomes. Paste the outcomes into the description rather than trusting it to guess what your program values.

> **Check before you plan around it: AI licensing**
> We could confirm what Anthology says about its Blackboard AI tools, but not what they cost today. A July 2025 Anthology release said all Anthology Virtual Assistant (AVA) capabilities would be a free trial for current Blackboard customers through June 30, 2026, and that the AI Design Assistant for Documents would be part of the core license.¹⁵ We found no published statement on whether rubric generation or AVA became a paid option after June 30, 2026. Ask your Anthology account team or administrator before you build a workflow on them.

## How do you write rubric descriptors that two graders read the same way?

A descriptor works when a second grader can read it, look at a submission and pick the same level without talking to you. That means observable features, a threshold you can check, and a clear step between one level and the next. Words like "good", "adequate" and "insightful" fail that test.

[FIGUUR: A two-panel comparison titled "Same criterion, two descriptors". Left panel, red header "Hard to apply": criterion "Use of evidence", level "Proficient: Uses good evidence to support the argument." Annotation arrows: "What is good?", "How much is enough?", "Two graders, two answers." Right panel, green header "Easier to apply": same criterion, level "Proficient (75%): Uses two or three sources from the course packet; each main claim has a source, but one claim has none." Annotation arrows: "Countable: 2 to 3 sources", "Checkable: claim without a source", "Next level up: all claims sourced." Footer: "EXAMPLE descriptors for a policy memo."]
*Figure 6: A descriptor with a number or a checkable feature leaves less to interpretation, which is what lets a second grader, or an AI tool, reach the same level.*

[CARDS: 3]
- **Name what you can see** | "States a recommendation in the first paragraph" beats "clear argument". If you cannot point at it in the submission, it is not observable.
- **Count or check where you can** | "Two to three sources", "one claim without a source", "all entries in one citation style". Numbers and checks settle disputes between graders.
- **Describe the step, not the adjective** | Each level should differ from the one above by one specific thing, not by swapping "excellent" for "good".
[/CARDS]

Here is a complete rubric you can adapt. It is a percentage-based rubric for a 100-point policy memo, with three of the usual four levels shown so that it fits on the page. Each level title is under the 40-character limit, and each descriptor is plain text that fits in one cell.

| Criterion (weight) | Meets standard (100%) | Partly meets (75%) | Not yet (50%) |
|---|---|---|---|
| Argument (40%) | States a recommendation in the first paragraph and defends it with a reason tied to the case facts. | States a recommendation; the reason is general and not tied to the case facts. | The recommendation is missing, or it changes between sections. |
| Evidence (30%) | Uses at least four sources from the course packet; every claim carries a source. | Uses two or three sources; one claim has no source. | Uses one source, or lists sources without tying them to claims. |
| Structure (20%) | Headings for issue, options and recommendation; each section opens with its main point. | Has headings; one section buries its main point. | No headings, or sections are out of order. |
| Citations (10%) | All sources cited in one style; no missing entries. | One to three formatting errors. | Style is inconsistent, or entries are missing. |

*Table 3: EXAMPLE percentage-based rubric for a 100-point policy memo. Add a fourth, lower level in Blackboard if you need one.*

Scoring that rubric is arithmetic. Suppose a submission lands at 75% on Argument, 50% on Evidence, 100% on Structure and 100% on Citations. That is 40 × 0.75 = 30, plus 30 × 0.50 = 15, plus 20 × 1.00 = 20, plus 10 × 1.00 = 10, for 75 of 100 points (EXAMPLE numbers).² Because the criteria are separate, the student can see exactly where the 25 missing points went.

The same habits matter even more when a tool, not a colleague, reads the rubric. Our guide on [how to write a rubric AI can mark against](/resources/blog/how-to-write-a-rubric-ai-can-mark-against) covers gateway criteria, testing a rubric on past work and fixing vague criteria, and it applies to Blackboard rubrics as much as to any other.

## How do you attach a rubric to an assignment?

You attach a rubric from the assignment's Settings panel: select Add Rubric in the Grading & Submissions section, select the radio button next to the rubric, and select Save & Close.⁴ Do this before the first student submits, because that is when it behaves most predictably.

1. **Open the assignment, discussion or journal** and select the Settings icon.
2. **In Grading & Submissions, select Add Rubric.** The Course Rubrics page opens.
3. **Select the radio button** next to the rubric you want.
4. **Select Save & Close.** When you view a submission, the grade pill now shows a rubric icon.⁴

Three rules apply. Only one rubric can be associated with each item.³ ⁴ Rubrics attach only to assignments, discussions and journals, and you cannot associate a rubric with an assignment that has questions.¹ ⁶ And students can see the rubric: they select "This item is graded with a rubric" in the Details & Information section, before they open the assignment and after they start.¹

Anthology's pages are not fully consistent about attaching a rubric after grading has begun. The association page says you can associate a rubric "unless you've already graded the item", while the Grade with Rubrics page describes associating one after grading starts, which turns existing grades into overrides that you can regrade with the rubric.⁴ ⁶ Test it in a sandbox course if you need to do it, and where you can, attach the rubric before the first submission arrives.

## How do you grade with a rubric in Blackboard Ultra?

You grade with a rubric by opening a student's submission from the Submissions page, opening the rubric next to the grade pill, and selecting a performance level for each criterion.⁶ The rubric score and your feedback save automatically as you click.⁶ Our companion guide on [how to grade assignments in Blackboard Ultra faster](/resources/blog/how-to-grade-assignments-in-blackboard-ultra) covers the rest of the grading flow; this section covers the rubric itself.

[FLOWDIAGRAM] Gradebook → select the assessment → Submissions → select a student name → rubric icon beside the grade pill (side panel) or expand icon (separate, movable window) → select a score pill per criterion → optional criterion feedback → close the panel (X) → feedback icon for overall feedback → menu → Post
*Figure 7: The click path for grading with a rubric (schematic). Scores and criterion feedback save automatically; nothing reaches the student until you post.*

1. **Open the submission.** In the Gradebook, select the assessment, select Submissions, then select the student's name.⁶
2. **Open the rubric.** Select the rubric icon next to the grade pill for a stacked view in the side panel, or the expand icon for a grid view in a separate, moveable window.⁶
3. **Select a performance level per criterion.** Select the score pill you want. The grade pill updates as you go, and you can deselect a level and choose another.⁶
4. **Show the descriptions if you need them.** Descriptions are hidden by default. The Show descriptions toggle turns them on for every submission in the assessment.⁶
5. **Add criterion feedback.** Each criterion has a text box. There is no character limit, and the editor is plain text.⁶
6. **Add overall feedback.** Select the feedback icon on the submission page, type your notes and save.⁶
7. **Post.** Open the menu and select Post when you want the student to see the grade. You can come back and change the grade even after posting.⁶

You can keep your hands on the keyboard. Tab moves between criteria, and the up and down arrows select a performance level.⁶ Use the arrow icons to collapse or expand a criterion, including one you have already scored.⁶ For a percentage-range rubric you select a value inside the band, and Blackboard calculates points from the weight, the percentage you chose and the item's points.⁶

After scoring, Ultra can draft the overall feedback for you if AVA is available at your institution. In the flexible grading view, the Summarize option reads your selected levels, their descriptions and any criterion feedback, then proposes an overall summary that you can accept, reject or regenerate. A Rewrite option polishes feedback you have already typed, as long as it is at least 30 characters.⁸ ¹⁴ Both are labeled as AI-generated, and Anthology tells instructors to review the output before it reaches students.¹⁴ Remember the licensing caveat above.

> **Do not type into the grade pill**
> If a rubric is associated with an item and you type a number into the grade pill instead of using the rubric, that is an override, and the submission continues to display as Needs Grading.⁶ Use Undo Override on the Submissions page to remove it and return to the rubric.⁶

## Can you edit, copy, export, import or print a rubric?

You can copy, export, import and print rubrics, and you can edit one only until you have graded with it.⁵ After that, you make a copy and edit the copy.⁵ ⁶

[FIGUUR: A four-state lifecycle diagram titled "What happens when you change a rubric (schematic)". State 1 "Draft rubric" (editable) → arrow "Attach to assignment" → State 2 "In use, nothing graded yet" (editable) → arrow "Grade with it" → State 3 "Used for grading" (locked, shown with a lock symbol) → arrow "Create a Copy (item Settings) or Duplicate (ellipsis menu)" → State 4 "New rubric, associated with the item". Below State 4, a note: "Earlier grades are preserved but converted to overrides; regrade with the new rubric to restore rubric scoring." A side branch from State 3: "Delete rubric → grades remain as manually added grades".]
*Figure 8: A used rubric is locked. Copying it creates an editable version, and the old grades turn into overrides until you regrade.*

| Task | How, according to Anthology | The catch |
|---|---|---|
| Copy a rubric | Course Rubrics page, ellipsis, Duplicate; or from an item's Settings, open the rubric and select Create a Copy⁵ | Copying a rubric you graded with associates the copy with the item, and earlier grades become overrides⁵ |
| Copy between courses | Course Content, plus sign, Copy Content (or More options, Copy Items); open the Rubrics folder and select Start copy⁵ | Copied rubrics appear in Gradebook Settings under Course Rubrics⁶ |
| Export | Ellipsis, Export; downloads a zip file named with the rubric and course title⁵ | The zip is for importing into another course; it is not a viewable document⁵ |
| Import | Import icon on the Course Rubrics page; select the zip⁵ | Only rubrics exported from Blackboard LMS can be imported; a duplicate in the course triggers an error⁵ |
| Print | Ellipsis, Print (blank), or the Print icon in an open rubric (scored)⁵ | A scored rubric needs at least one level selected; useful for accreditation or review files⁵ |
| Delete | Ellipsis, Delete⁵ | Grades remain but become manually added grades⁵ |

*Table 4: Managing rubrics in Ultra. Source: Anthology's Manage Rubrics page, read October 19, 2026.*

This answers a question people type often: there is no documented way to import a rubric into Ultra from Word, Excel or a CSV file. The only import is a zip exported from Blackboard. Because rubric cells are plain text, pasting text from a document does work, but the formatting will not carry over.³ ⁵

> **Migrating from the Original Course View**
> Anthology's Original Course View page on importing and exporting rubrics, which is a different page from the Ultra one, says that a rubric larger than 15 x 15 carries over to an Ultra course only up to its first fifteen rows or columns.¹⁷ If you are converting courses, check your largest rubrics.

## How do you keep rubric grading consistent across instructors?

Ultra gives you three tools for consistency: a shared rubric, parallel grading with a reconciler, and the Rubric Evaluation Report for spotting criteria that do not discriminate. None of them is automatic, and none replaces a short calibration session where graders score the same three submissions and compare.

**Parallel grading** lets two graders mark each submission without seeing each other's grades, feedback, annotations or rubrics. You enable it by selecting the 2 graders per student check box in the Evaluation options section of the assessment Settings, then assigning graders and a reconciler. Anthology says it works best with multiple graders and at least one reconciler.¹⁰ ¹⁶ The reconciler reviews the provisional grades and sets the final one, and students see only the reconciler's grade, feedback and rubric.⁹ ¹¹ One limit matters for rubric work: you cannot enable parallel grading for group work, or add questions to an assessment that uses it.⁹

When graders disagree, the reconciler can score each attempt individually. Or the reconciler can use Reconcile All to apply the average, highest or lowest of the graders' grades in one irreversible action, which labels the grades as overrides on the Submissions list when a rubric is associated.¹¹

**The Rubric Evaluation Report** shows how a class performed against each criterion. From the Gradebook grid view, select the item's column header, open the download icon in the Assessment Details panel, select Download rubric report, choose PDF or CSV and select Run Report.⁷ It is based on posted grades only and refreshes every 24 hours overnight.⁷

[FIGUUR: A report schematic titled "Rubric Evaluation Report: what to look for (EXAMPLE data)". Left: four horizontal bars, one per criterion, each showing "points possible" as a light bar and "average earned" as a dark bar: Argument 40 possible, 29 average; Evidence 30 possible, 17 average; Structure 20 possible, 18 average; Citations 10 possible, 9 average. Right: a frequency distribution table for "Structure" with columns "Level", "Share of students": "100%: 78%", "75%: 17%", "50%: 5%". A highlighted note on Structure: "Ceiling effect: 78% at the top level. Is the descriptor too easy, or is the class strong?" A second highlighted note on Evidence: "Lowest average (57%). Check the descriptor before you re-teach." Footer: "The report sections: Overview, Rubric Overall Performance, Rubric Analysis, Frequency Distribution."]
*Figure 9: The report shows where students cluster. A criterion nearly everyone passes, or one almost nobody passes, is a prompt to check the descriptor.*

Be careful about what the report can prove. Anthology describes it as an aggregated view of how students performed against each criterion, with average, median, mode and standard deviation per criterion.⁷ We found no breakdown by grader in the page. Use it to find criteria that do not separate students, and use parallel grading, or a calibration session on shared submissions, to find graders who do not agree.

[CARDS: 3]
- **A shared rubric** | One Course Rubrics entry copied into every section, so all instructors start from the same document.
- **Parallel grading** | Two blind graders per submission and a reconciler, for assessments where the grade carries weight.
- **The evaluation report** | A per-criterion view of the whole class, to find descriptors that do not discriminate between levels.
[/CARDS]

## What goes wrong with rubrics in Blackboard Ultra, and how do you fix it?

Most rubric problems in Ultra come from three causes: changing a rubric after use, entering a grade outside the rubric, and expecting a feature to exist that does not. The table lists the ones the help pages explain.

| What you see | Cause | Fix |
|---|---|---|
| The rubric is read-only or cannot be edited | You have already graded with it⁵ ⁶ | Create a copy and edit the copy; regrade if needed |
| Submission still says Needs Grading | You entered a grade in the grade pill instead of using the rubric⁶ | Use Undo Override, then grade with the rubric |
| No option to add a second rubric | One rubric per item³ ⁴ | Combine criteria into one rubric |
| Cannot attach a rubric to a test or an assignment with questions | Rubrics attach to assignments, discussions and journals only; not to assignments with questions¹ ⁶ | Use the test's own question scoring |
| Pasted text lost its bullets and bold | Rubrics support plain text only³ | Rewrite as plain sentences |
| Pressing Enter closed the cell | Enter confirms and leaves edit mode³ | Write one block of text, no line breaks |
| Import fails | Only rubrics exported from Blackboard LMS can be imported; duplicates are rejected⁵ | Export from the source course; rename or delete the duplicate |
| Descriptions disappeared after changing type | Switching a percentage-based rubric to percentage-range clears all descriptions⁵ | Choose the type first; copy descriptions into a document before switching |
| Cannot create a rubric on a phone | Creation is unavailable at small screen widths; rubrics are read-only on mobile¹ | Use a laptop or tablet in a wider browser window |

*Table 5: Common rubric problems in Ultra and their documented fixes.*

## Where does Eduface fit next to Blackboard's rubrics?

Blackboard's native rubrics handle building, attaching, scoring and posting, and they do that well; Eduface is for the part where the instructor does the reading and the scoring for every submission. Eduface connects to Blackboard through LTI 1.3, and the instructor reviews suggestions in the Eduface interface, opened from Blackboard.¹⁸ The setup is a one-time task for your administrator, and the [Eduface hub for Blackboard](/resources/blog/ai-essay-grader-blackboard-lti) covers it, so we do not repeat the steps here.

Eduface's Paper Grader scores each submission per criterion against your rubric and shows an explainable breakdown for each criterion, with annotations in the text and flagged uncertainty. The instructor reviews and approves each suggestion before the student sees anything. The Paper Grader's formative feedback works the same way for drafts. After approval, the grade returns to the Blackboard gradebook through LTI Grade Services, and students need no separate login.¹⁸ If you do not have a rubric, Eduface can generate one. This post does not claim that Eduface reads an existing Blackboard rubric automatically: plan on bringing your criteria and level descriptors across, which is simple because both are plain text.

| Task | In Blackboard Ultra | With Eduface | Who decides |
|---|---|---|---|
| Build the rubric | Course Rubrics: create, generate or copy | Bring your criteria and levels; Eduface can generate a rubric if you have none | Instructor |
| Score a submission | Select a level for each criterion | Suggests a score per criterion with an explainable breakdown, annotations and flagged uncertainty | Instructor approves |
| Check graders against each other | Parallel grading and reconcile | Grader comparison dashboard; blind mode and AI-visible mode | Program director, instructor |
| Keep a record | Gradebook | Audit trail for summative assessment | Institution |
| Post the grade | Post from the menu | Approved grade returns to the Blackboard gradebook via LTI Grade Services | Instructor |

*Table 6: What Blackboard Ultra does natively and what Eduface adds on the same rubric.*¹⁸

[FLOWDIAGRAM] Student submits in Blackboard Ultra → Instructor opens Eduface from Blackboard (LTI 1.3) → Eduface suggests a score per criterion against your rubric, held as a draft → Instructor reviews, edits, approves → Approved grade returns to the Blackboard gradebook
*Figure 10: The grade reaches the Blackboard gradebook only after the instructor approves it.*¹⁸

When native is enough, use native. If one instructor teaches a section with a few dozen submissions, a good rubric, a calibration session and the shortcuts in the [Ultra grading guide](/resources/blog/how-to-grade-assignments-in-blackboard-ultra) will take you most of the way, and you do not need another vendor. A dedicated tool starts to earn its place when volume is high, when part-time instructors apply the same rubric differently, or when you need an audit trail for summative grades. If you are comparing what Blackboard's own AI offers with a dedicated tool, [AI grading in Blackboard Ultra](/resources/blog/blackboard-ultra-ai-grading) sets the two side by side.

> **What Eduface doesn't do**
> Eduface does not replace Blackboard's rubric builder, and it does not make a vague rubric precise: a descriptor that two instructors read differently will be read differently by any tool. It works in its own interface, which you open from Blackboard, so ask in a demo exactly where feedback lands before you design your workflow around it. It is one more vendor for IT and procurement to review. Academic Integrity and Oral Examination are in beta. If native rubrics already give your program the consistency it needs, those costs are not worth paying.

> **For program directors**
> Eduface processes student data in the EU, never uses it to train AI models, and uses no third-party AI APIs such as OpenAI. The institution signs a Data Processing Agreement. Blackboard's rubric generator is a different case: it is instructor-facing, runs on Microsoft's Azure OpenAI service from limited course information, and is documented as such.¹⁸ ¹³ Ask both vendors the same data questions.

## What to do next

Five actions turn this guide into a rubric your graders can use before the next assignment.

1. **Pick one live assignment** and choose the rubric type with Figure 1. Default to percentage-based for a summative writing task and no-points for a draft.
2. **Write or generate the rubric, then review every cell.** Use Table 3 as the template and keep each level title under 40 characters.
3. **Test it on two past submissions** with a colleague. Where you land on different levels, rewrite that descriptor.
4. **Attach it before the first submission arrives,** from Settings, Grading & Submissions, Add Rubric. Copy it to the other sections.
5. **Run the Rubric Evaluation Report after grades post.** Look for a criterion where almost everyone sits in one level, and fix it in a copy before the next term.

<!-- OPEN POINTS for Dante before publishing (checked October 19, 2026):
1. Blackboard AI licensing. Sources read: Anthology release, July 2025 (via silicon.co.uk syndication; the Business Wire original carries 2025-07-15 in its URL and was NOT opened): AVA free trial to current Blackboard customers through June 30, 2026; AI Design Assistant for Documents part of the core license. NOT found: any statement of what rubric generation or AVA (Summarize/Rewrite) costs after June 30, 2026. Re-check with Anthology or a Blackboard admin and edit the licensing callout.
2. Anthology help-page inconsistencies (re-check in a sandbox Ultra course): (a) Rubrics overview says "four types", Types of Rubrics and the generator list five incl. no-points; (b) Associate page says you cannot associate once the item is graded, Grade with Rubrics describes associating after grading (grades become overrides); (c) the Points-based description says the criterion total is the sum of the points in its performance levels, which reads oddly, so the worked example uses a percentage-based rubric; (d) the generate steps do not name the control that opens the generator.
3. Eduface claims: nothing is claimed about Eduface comments appearing inside the Blackboard rubric panel, Bb Annotate or the native feedback box, and nothing about Eduface importing a Blackboard rubric (not confirmed). Please confirm: (i) which rubric formats Eduface accepts as input, (ii) where feedback lands for the instructor after approval, so the 'What Eduface doesn't do' callout can be made specific.
4. The live hub ai-essay-grader-blackboard-lti still names a 'Formative Feedback Tool' and says the AI Design Assistant 'cannot assess or grade student work'. Anthology's AVA page documents Summarize and Rewrite for overall feedback in flexible grading, so the hub sentence is incomplete (it does not grade, but it does draft feedback text).
5. Rubric generation requires the administrator to activate the AI Design Assistant (admin help page, read via http://help.anthology.com/blackboard/administrator/en/...). Brief said admin pages may 403; this one opened.
6. The 'EXAMPLE' minutes in Figure 5 and the scoring example are illustrative, not measured. -->

## Frequently asked questions

**Can I use more than one rubric on a Blackboard Ultra assignment?**
No. Anthology's help pages say only one rubric can be associated with each item. If you need two sets of criteria, combine them into one rubric with more rows, or use a separate assignment for the second set.³ ⁴

**Can I edit a rubric after I have graded with it in Blackboard Ultra?**
No, not the original. After you use a rubric for grading, you can make a copy and edit the copy. Grades calculated with the original rubric are preserved but converted to overrides, and you can regrade those submissions with the new rubric.⁵

**Can I import a rubric into Blackboard Ultra from Word or Excel?**
Not through a documented import. The only import accepts a zip file previously exported from Blackboard LMS, and it rejects a rubric that already exists in the course. Rubric cells accept pasted plain text, so you can paste descriptors from a document, but the formatting does not carry over.³ ⁵

**Does Blackboard Ultra have an AI rubric generator?**
Yes, if your institution has turned on the AI Design Assistant. You enter a description, choose the type, complexity, rows and columns, select Generate, then review each cell and select Continue to save. Anthology does not state in the pages we read what rubric generation costs after the June 30, 2026 end of the AVA trial, so check with your administrator.³ ¹³ ¹⁵

**Can students see the rubric in Blackboard Ultra?**
Yes. Students can view the rubric before they open an assignment or discussion and after they start, by selecting "This item is graded with a rubric" in the Details & Information section. After you post grades, they see their awarded levels highlighted.¹ ⁶

**Can I use a rubric on a Blackboard Ultra test?**
No. Anthology says you can only associate rubrics with assignments, discussions and journals, and you cannot associate a rubric with an assignment that has questions. For tests, use the question scoring.¹ ⁶

**Does Eduface use the rubric I built in Blackboard?**
Eduface scores against the rubric you set up in Eduface, which is why you bring your criteria and level descriptors across; if you have no rubric, it can generate one. Approved grades return to the Blackboard gradebook, and the instructor reviews every suggestion first.¹⁸

## References

1. Anthology. (2026). "Rubrics." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/rubrics.html. Accessed October 19, 2026. [Key finding: rubrics can be associated only with assignments, discussions and journals; new rubrics have four rows and four columns; students view the rubric through "This item is graded with a rubric" in Details & Information; rubrics are read-only on mobile; the overview lists four types.]
2. Anthology. (2026). "Types of Rubrics." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/rubrics/types-of-rubrics.html. Accessed October 19, 2026. [Key finding: five types (percentage-based, percentage-range, points-based, points-range, no-points); weights total 100% with one level at 100%; points must be whole numbers with a rubric total of 99,999 or less.]
3. Anthology. (2026). "Create or Generate Rubrics." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/rubrics/create-or-generate-rubrics.html. Accessed October 19, 2026. [Key finding: two routes to the Course Rubrics page; title limit 255 characters, level title 40, criteria and description cells 1,000; plain text only; Enter exits edit mode; one rubric per item; generation steps if the AI Design Assistant is on.]
4. Anthology. (2026). "Associate a Rubric to an Assessment." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/rubrics/associate-a-rubric-to-an-assessment.html. Accessed October 19, 2026. [Key finding: Settings, Grading & Submissions, Add Rubric, then radio button and Save & Close; an existing rubric can be associated unless the item is already graded; removing a rubric keeps grades as manual grades.]
5. Anthology. (2026). "Manage Rubrics." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/rubrics/manage-rubrics.html. Accessed October 19, 2026. [Key finding: duplicate, copy between courses, export as zip, import only rubrics exported from Blackboard LMS, print blank or scored; a used rubric cannot be edited, but can be copied, and earlier grades become overrides.]
6. Anthology. (2026). "Grade with Rubrics." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/grading-assessments/grade-with-rubrics.html. Accessed October 19, 2026. [Key finding: grading click path, Show descriptions toggle, criterion feedback with no character limit, auto-save, overrides keep the item at Needs Grading, no rubric on assignments with questions.]
7. Anthology. (2026). "Rubric Evaluation Report." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/rubrics/rubric-evaluation-report.html. Accessed October 19, 2026. [Key finding: aggregated per-criterion view of class performance, based on posted grades only, refreshed every 24 hours; PDF or CSV; four sections including frequency distribution.]
8. Anthology. (2026). "Grade Assessments With Flexible Grading." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/grading-assessments/grade-assessments-with-flexible-grading.html. Accessed October 19, 2026. [Key finding: the feedback and rubrics side panel; AVA can generate overall feedback summaries from the rubric criteria and selected levels, which the instructor accepts, rejects or regenerates.]
9. Anthology. (2026). "Parallel Grading." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/types-of-grading/parallel-grading.html. Accessed October 19, 2026. [Key finding: graders cannot see each other's grades, feedback, annotations or rubrics; the reconciler sets final grades; not available for group work or assessments with questions.]
10. Anthology. (2026). "Enable Parallel Grading." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/types-of-grading/parallel-grading/enable-parallel-grading.html. Accessed October 19, 2026. [Key finding: select 2 graders per student in Evaluation options, then assign graders and reconcilers; each student has two graders.]
11. Anthology. (2026). "Reconcile Grades." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/types-of-grading/reconcile-grades.html. Accessed October 19, 2026. [Key finding: students see only the reconciler's grade, feedback and rubric; Reconcile All applies the average, highest or lowest grade, is irreversible, and shows an Override label when a rubric is associated.]
12. Anthology. (2026). "AI Design Assistant." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/course-and-content-management/ai-design-assistant.html. Accessed October 19, 2026. [Key finding: rubric generation is one of the listed tasks; ten complexity levels from early primary school to advanced PhD level; many output languages including American English; partner is Microsoft.]
13. Anthology. (2026). "Blackboard AI Design Assistant." Blackboard Help for Administrators. help.anthology.com/blackboard/administrator/en/tools-management/blackboard-ai-design-assistant.html. Accessed October 19, 2026. [Key finding: opt-in, administrators activate it and assign the privilege; the rubric function "suggests a grading rubric with structure and criteria against a given assessment"; powered by Azure OpenAI from limited course information; do not ask for sources or references; prompts and output stored by Microsoft for up to 30 days for content filtering; client data not used for retraining.]
14. Anthology. (2026). "AVA – AI Virtual Assistant." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/course-and-content-management/ava---ai-virtual-assistant.html. Accessed October 19, 2026. [Key finding: Summarize generates overall feedback from a completed rubric in flexible grading; Rewrite needs at least 30 characters; suggestions are labeled AI-generated and can be accepted, rejected or regenerated.]
15. Anthology. (2025). "Anthology Unveils Next Generation AI and Immersive Learning Innovations in Blackboard." Press release, syndicated on silicon.co.uk (Business Wire release dated July 15, 2025 in its URL). Accessed October 19, 2026. [Key finding: AVA capabilities offered as a free trial to current Blackboard customers through June 30, 2026; AI Design Assistant for Documents part of the core Blackboard license. Nothing on pricing after June 30, 2026 was found.]
16. Anthology. (2026). "Grading & Submissions." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/assessments/assessment-settings/grading---submissions.html. Accessed October 19, 2026. [Key finding: Evaluation options include 2 graders per student, peer review and delegated grading; grades can post automatically when graded.]
17. Anthology. (2026). "ORIGINAL Import and Export Rubrics." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/original-course-view/grading/rubrics/import-and-export-rubrics.html. Accessed October 19, 2026. [Key finding: for rubrics larger than 15 x 15, only the first fifteen rows or columns carry over to an Ultra course.]
18. Eduface. (2026). "AI Essay Grader for Blackboard Learn and Ultra: Grading and Feedback via LTI 1.3." eduface.me/resources/blog/ai-essay-grader-blackboard-lti. Accessed October 19, 2026. [Key finding: LTI 1.3 integration with Blackboard; the rubric and brief are uploaded once; per-criterion scores with reasoning and annotations; grades held until the lecturer approves, then returned to the Blackboard gradebook; EU infrastructure and a Data Processing Agreement.]
