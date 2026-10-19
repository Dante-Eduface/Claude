---
title: "AI Grading in Blackboard Ultra: What Blackboard AI Does and What Eduface Adds"
seo_title: "Blackboard Ultra AI Grading: What Exists | Eduface"
meta_description: "Does Blackboard Ultra have AI grading? What the AI Design Assistant and AVA do, what needs a license since July 2026, and where a dedicated tool adds value."
slug: blackboard-ultra-ai-grading
primary_query: "blackboard ultra ai grading"
secondary_queries: ["blackboard ultra ai", "blackboard ai feedback", "blackboard ai design assistant", "blackboard ai rubric generator", "does blackboard have ai grading", "anthology blackboard ai"]
type: integratie
category: Integrations
hub: /resources/blog/ai-essay-grader-blackboard-lti
related: [/resources/blog/ai-essay-grader-blackboard-lti, /resources/blog/how-to-grade-assignments-in-blackboard-ultra, /resources/blog/how-to-create-and-use-a-rubric-in-blackboard-ultra, /resources/blog/how-to-write-a-rubric-ai-can-mark-against, /resources/blog/ai-grading-tools-higher-education-guide]
review_by: 2026-12-15
status: concept
outline: "H2s: What AI features does Blackboard Ultra have today? / Can Blackboard AI give feedback or a grade on a student's work? / What can the AI Design Assistant do for grading? / What does Blackboard AI cost, and what do you need to switch it on? / Where does student data go when you use Blackboard AI? / What is coming next in Blackboard AI? / What does Eduface add inside a Blackboard Ultra course? / How do Blackboard AI and Eduface compare side by side? / When is Blackboard's own AI enough? / How do you pilot the two? / What to do next / FAQ. Information gain: every documented Blackboard AI feature in one table with what it does not do, a licensing table with the dated status, a decision table and a pilot protocol with a worked time example (labeled EXAMPLE)."
note: "Spoke van de Blackboard-hub, zusterblog van 56 en 57. Alle Blackboard-feiten uit Anthology-pagina's gelezen op 19-10-2026 (zie References). Licentiestatus verandert snel: zie het HTML-commentaar boven References. De hub-FAQ en blog 45 beschrijven de AI Design Assistant te smal, zie het rapport."
components: "6 figures, 5 tables, 3 card grids, 8 callouts plus the answer block. Card grids use the [CARDS: n] ... [/CARDS] notation, one item per line as '- **Title** | text'."
---

EYEBROW: BLACKBOARD ULTRA · AI GRADING

# AI Grading in Blackboard Ultra: What Blackboard AI Does and What Eduface Adds

*Blackboard's AI can draft a rubric, write a test question and polish your feedback comments. Whether it can grade is a different question. Here is what each feature does, what needs a license since July 2026, where the data goes, and when a dedicated tool earns its place.*

By Eduface · October 2026 · 23 min read · Written for instructors, instructional designers and program directors at private and for-profit colleges on Blackboard Ultra

Your admin switched on the AI Design Assistant, and instructors found the Generate button for rubrics. Then an email arrived about something called AVA, a colleague said Blackboard now helps write feedback, and someone mentioned that AI in Blackboard needs a license. Your program director asks the question you expected: does Blackboard grade with AI now, and if it does, why would we look at anything else?

> **Does Blackboard Ultra have AI grading?**
> Not in the documentation we read. Blackboard's AI helps instructors build and word things: the AI Design Assistant generates rubrics, prompts and test questions, and AVA, which has needed a specific license since July 1, 2026, can summarize or rewrite feedback from the rubric levels and comments you have already entered. None of these reads a student submission and proposes a grade or a rubric rating. Scoring and drafting feedback against your rubric is what a dedicated tool such as Eduface adds through LTI 1.3.

> **Key takeaways**
> - Blackboard's documented AI helps you build (rubrics, prompts, test questions) and word (summarize or rewrite feedback). It does not score a submission.
> - AVA, which includes the feedback Summarize and Rewrite options, has needed a specific license since July 1, 2026. The AI Design Assistant is listed separately.
> - Both run on Microsoft's Azure OpenAI Service, hosted primarily in the United States, and Anthology says your data is not used to train the models.
> - For rubric and prompt drafting and for polishing comments, Blackboard's own AI is often enough.
> - Scoring against your rubric, draft feedback, consistency across graders and an audit trail are where a dedicated tool earns its place.

[CARDS: 3]
- **What Blackboard AI does** | Every documented feature in one table, what it does not do, and where Anthology documents it.
- **License, data and what is coming** | What needs an AVA license today, where the data goes, and what Anthology has announced for the rest of 2026.
- **Blackboard versus Eduface** | A side-by-side table, a decision table and a pilot you can run on 25 to 40 submissions.
[/CARDS]

## What AI features does Blackboard Ultra have today?

Blackboard Ultra has three families of AI features: tools that help you build a course, an AI persona your students talk to, and helpers in the feedback panel while you grade. Anthology's help pages call the first family the AI Design Assistant. It generates course structure, discussions, journals, assignment prompts, test questions, question banks, rubrics, AI Conversations, images and document layouts, at ten complexity levels from early primary school to advanced PhD.¹

The second family is the AI Conversation activity, where students practice Socratic questioning or role-play with a persona you design.² The third belongs to AVA, Anthology's AI Virtual Assistant: a rubric feedback summary, a feedback rewrite, automatic replies to student messages and an AI Playground.³ Notice what the list is built around. Every item supports the instructor's own work, the student's practice or open exploration. None is built around reading a submission and judging it.

[FIGUUR: A horizontal band titled "The assessment cycle in Blackboard Ultra, and where Blackboard AI touches it (schematic)". Four columns, left to right, each a rounded card with a header. Column 1 "Build" (navy header): chips "Rubric draft", "Assignment prompt", "Test questions and question banks", with a small label "AI Design Assistant". Column 2 "Practice" (navy header): chips "AI Conversation: Socratic, Role-play", "Pulse Quiz (AVA license)". Column 3 "Score the submission" (amber header, dashed border, the card is visually empty except for the line "No documented Blackboard AI feature"). Column 4 "Word the feedback" (navy header): chips "Summarize rubric feedback", "Rewrite", with a small label "AVA". Under the band, one bracket spans columns 1, 2 and 4 labeled "Blackboard AI helps here" and an arrow points at column 3 labeled "Instructor today; a dedicated tool via LTI 1.3". Highlight: the dashed amber card.]
*Figure 1: Blackboard's documented AI sits before and after the scoring step; the step in the middle stays with the instructor.*

| Feature | What it does | What it does not do | Documented in |
|---|---|---|---|
| AI Design Assistant: rubric generation | Drafts a rubric from your description, in one of five rubric types; you edit each cell⁴ | Does not apply the rubric to student work | Create or Generate Rubrics |
| AI Design Assistant: prompts and test items | Generates assignment prompts, discussions, journals, test questions and question banks¹ | Does not review or grade responses | AI Design Assistant |
| AI Conversation, including Pulse Quiz | Students talk with a persona you set up; you review the transcript and the student's reflection² | A Pulse Quiz result is not passed to the gradebook; you give the feedback and grade² | AI Conversation |
| AVA: Summarize rubric feedback | Drafts overall feedback from the rubric levels you selected, their descriptions and your criterion comments³ | Does not list the submission among its inputs | AVA – AI Virtual Assistant |
| AVA: Rewrite | Rewords your own overall or per-question feedback, once you have typed at least 30 characters³ | Does not write feedback from nothing | AVA – AI Virtual Assistant |
| AVA: Responses to student messages | Answers common questions from course content the student can see³ | Does not grade; replies about due dates, grades and content the student can see | AVA – AI Virtual Assistant |
| AVA: AI Playground | Chat with selected AI models inside Blackboard³ | Per the help page, not connected to assessments, grades or instructor workflows | AVA – AI Virtual Assistant |

*Table 1: Every Blackboard AI feature we found in Anthology's help pages, with its limit. Read October 19, 2026.*

## Can Blackboard AI give feedback or a grade on a student's work?

No. Blackboard AI can help you write feedback about a submission, but none of the inputs the help page lists is the student's submission, and it never proposes a score. The Summarize option works from the rubric criteria, the performance levels you selected, their descriptions, any criterion-level feedback you wrote, and whatever is already in the overall feedback box.³

Here is the path in Flexible Grading. From the assignment's Submissions page you select a student, open the feedback panel, complete the rubric, and select Summarize rubric feedback (the AVA page calls the same option Summarize). A banner marks the suggestion as AI-generated, and you accept, reject or regenerate it.⁵ ³ Rewrite works the same way on text you typed yourself.³

[FLOWDIAGRAM] Instructor reads the submission and rates each rubric criterion (instructor judgment) → Adds criterion-level comments (instructor text) → Selects Summarize rubric feedback (inputs: rubric criteria, selected levels, descriptions, your comments, existing overall feedback) → Suggested overall feedback with an AI-generated banner → Accept, reject or regenerate → Edit if needed → Post grades
*Figure 2: The Summarize workflow in Flexible Grading (schematic). The judgment about the work happens before the AI step, and the instructor still decides what students see.*

Anthology is explicit that this is by design. The transparency note for these features says Blackboard has "intentionally omitted potentially high-stakes functionalities", and that the feature "does not include any automated decision-making that could have a legal or otherwise significant effect on learners or other individuals."⁶ That is a reasonable position for an LMS vendor, and it answers the question this guide started with.

> **A practical reading**
> Because Summarize is built from your rubric selections and criterion comments, its output can only be as specific as the notes you give it. Our reading, not Anthology's claim: it saves you writing time, not reading time. You still read every submission and rate every criterion yourself.

What do Rewrite and Summarize look like in practice? Anthology says Rewrite turns "rough notes, bullet points, or complete sentences" into more polished, student-friendly language, and that you can run it several times on the same feedback.³ The example below is illustrative wording, not captured output, so your results will differ.

> **EXAMPLE: the kind of rewrite Rewrite aims at**
> *Instructor's rough notes:* "Method clear. No error analysis. Units missing table 2. Conclusion just repeats intro."
> *A polished version might read:* "Your method section is clear and easy to follow. To strengthen the report, add an error analysis, include units in Table 2, and use the conclusion to say what your results show instead of repeating the introduction."
> *What stays with you:* deciding the notes are right. Rewrite changes the wording, not the judgment.

## What can the AI Design Assistant do for grading?

The AI Design Assistant helps before grading starts: it drafts the rubric, the assignment prompt and the test items you will grade against. Anthology describes rubric generation as one of its common classroom tasks, available if your institution has turned the AI Design Assistant on.¹ ⁴

[CARDS: 3]
- **Good use** | A first-draft rubric for a new assignment, with the criteria and level structure already in place.⁴ Choose a rubric type, set the number of rows and columns, and generate.
- **Needs you** | The level descriptors. Anthology's own instruction is to review each cell for accuracy and edit as needed, and the editor limits criterion and description cells to 1,000 characters of plain text.⁴
- **Not its job** | Reading student work, rating it against the rubric, or drafting comments about it. It generates the instrument, not the judgment.
[/CARDS]

The click path is short:

1. **Open the Course Rubrics page** from Gradebook Settings (Manage Course Rubrics) or from Assignment Settings (Add Rubric, in the Grading & Submissions section).
2. **Describe the rubric.** Enter a description to narrow the focus, then pick the rubric type: percentage, percentage range, points, point range, or no points.
3. **Set the shape.** Adjust the complexity, the number of columns and rows, and optionally the output language under Advanced options.
4. **Select Generate,** review each cell, then select Continue to save the rubric.⁴

Only one rubric can be associated with an item, so the rubric you attach to the assignment is the one a human or an AI will be held to.⁴ Our guide to [creating and using a rubric in Blackboard Ultra](/resources/blog/how-to-create-and-use-a-rubric-in-blackboard-ultra) covers the rubric types and the grading screen in detail. If the rubric will also be read by an AI grader, [how to write a rubric AI can mark against](/resources/blog/how-to-write-a-rubric-ai-can-mark-against) shows what level descriptors need to say.

## Is the AI Conversation a way to assess students?

The AI Conversation is a practice and reflection activity, not a grading tool. Anthology describes three types: Socratic Questioning, Role-play and Pulse Quiz, each with a reflection question where students can say what they thought and flag any bias or errors from the AI.² It is a formative assessment by default. On submission you read the conversation transcript and the student's reflection, then give the feedback and the grade yourself.²

Pulse Quiz needs a closer look. Its questions are generated during the conversation, so each student gets a slightly different set and you do not review them in advance. The quiz reports how many questions a student answered correctly, but that result is not passed to the gradebook.² Anthology's own advice is that if you need to verify specific questions in advance, you should use a test. For a formal oral assessment, where you need a rubric-based evaluation of what a student can explain, that is a different job. Eduface's Oral Examination (in beta) is built for it, with realtime transcription and assessment of a configured scenario.

## What does Blackboard AI cost, and what do you need to switch it on?

Blackboard AI is not one license: AVA has needed a specific license since July 1, 2026, and the pages we read do not say the AI Design Assistant needs one. If you heard that Blackboard's AI tools were free until June 2026, that is accurate for AVA. Anthology announced AVA on July 15, 2025 as a free trial for current Blackboard customers through June 30, 2026.⁷ Its administrator documentation says AVA features are included in your license until that date and that "a specific AVA license will be required to continue using these features."⁸

On September 23, 2026, Anthology repeated it in plain terms: "As of 1st July 2026, AVA is a premium capability that requires a specific license," and institutions without one can still try the tools in their test or stage environment until the end of 2026.⁹ The same post says the Socratic Questioning and Role-play AI Conversations remain part of the core license, while Pulse Quiz is exclusive to AVA institutions.⁹

[FIGUUR: A horizontal timeline titled "Blackboard AVA licensing, as documented (schematic)". Five markers on a line. 1: "July 15, 2025", label "AVA announced as a free trial for current customers". 2: "June 30, 2026", label "Trial period ends" (red marker). 3: "July 1, 2026", label "AVA becomes a premium capability that needs a specific license" (red marker, bold). 4: "September 23, 2026", label "Anthology restates the license requirement; Pulse Quiz, Virtual Assistant and Formative Feedback announced for AVA institutions". 5: "End of 2026", label "Test and stage access to AVA ends for institutions without a license". Below the line, a green bar spanning the whole timeline labeled "Socratic and Role-play AI Conversations: core license". A grey bar labeled "AI Design Assistant: not tied to the AVA license in the pages we read".]
*Figure 3: The June 30, 2026 date belongs to AVA. It is not a date for the AI Design Assistant or the core AI Conversation activities.*

| Feature | Status in the pages we read | Admin switch |
|---|---|---|
| AI Design Assistant, including rubric generation | Not tied to the AVA license in the pages we read. The Documents version was announced as part of the core license in 2025.⁷ ⁸ ⁹ | Building block AI Design Assistant and Unsplash; privilege Use AI Design Assistant¹⁰ |
| AI Conversation: Socratic, Role-play | Part of the core license⁹ | Not covered in the pages we read |
| AI Conversation: Pulse Quiz | Requires an AVA license; off by default² ⁹ | Ask your Blackboard administrator² |
| AVA: Summarize and Rewrite feedback | Specific AVA license since July 1, 2026⁶ ⁸ ⁹ | Same building block, AVA section, off by default; privilege Generate AI Feedback Changes⁸ |
| AVA: Responses to student messages, AI Playground | Specific AVA license since July 1, 2026⁸ ⁹ | Same building block, AVA section, off by default⁸ |

*Table 2: What each feature needs, according to Anthology's pages as read October 19, 2026.*

> **For Blackboard administrators**
> The switches sit in the Administrator Panel: in the Integrations section under Building Blocks, select Installed Tools, then AI Design Assistant and Unsplash. You can turn features on one by one, and you must assign the matching privilege to course roles such as Instructor. AVA settings are in the same building block under an AVA section.⁸

> **Licensing status as of October 19, 2026, and what we could not confirm**
> We found no price for AVA in any Anthology page we read. We could not confirm whether your contract treats the AI Design Assistant as included, because the pages we read tie the June 30, 2026 end date to AVA only. We did not open the October 2026 release notes. Ask your Anthology account representative to confirm in writing which AI features your contract includes and what they cost at your enrollment.

## Where does student data go when you use Blackboard AI?

Both Blackboard AI families send limited course information to Microsoft's Azure OpenAI Service, which Anthology says does not train on your data.¹⁰ ⁶ What differs is what they send, and in both cases the AI also processes whatever an instructor chooses to type in.

[CARDS: 3]
- **What is sent** | AI Design Assistant: limited course information, such as the course title and description, plus any extra context the instructor adds to the prompt.¹⁰ AVA Assisted Feedback: limited course, rubric and feedback information.⁶
- **Where it runs** | Multiple global Azure OpenAI instances. The primary one is hosted in the United States, and at times Blackboard uses resources in Canada, the United Kingdom or France. Input and output are stored in your Blackboard LMS database.¹⁰ ⁶
- **What is promised** | No retraining on your input or output. Microsoft reviews prompts and output for content filtering and stores them for up to 30 days.¹⁰ ⁶
[/CARDS]

For most US colleges this is a familiar profile: a general-purpose model, reached through a vendor you already contract with. If your policies or your learners' country call for EU processing, that is a question for your privacy officer, not something the documentation settles either way.

One more thing changes the picture. A grading tool reads the whole submission, so its data terms deserve a closer look than a feature that sees rubric entries. Eduface processes student data in the EU, never uses student work to train AI models, uses no third-party AI API such as OpenAI's, and signs a data processing agreement with every institution.

> **Questions for your privacy officer**
> Which Azure region will serve our requests? Do instructors type student names or identifiers into prompts or feedback? Who can see the stored input and output in our Blackboard database, and for how long? What is our policy if we add a tool that reads full submissions?

## What is coming next in Blackboard AI?

Anthology has announced three more AVA capabilities for the rest of 2026, and one of them touches draft feedback. AVA Formative Feedback would let students check their work against the grading rubric before they submit, while the instructor still grades the final submission and can see how the draft evolved.⁹ The September post labels it "Next: 3-6 months", behind the Pulse Quiz ("Now: 1-3 months") and alongside an AVA Virtual Assistant for students; the July roadmap lists AI Flashcards as part of the core license.⁹ ¹¹ Anthology notes that release timings and details are subject to change, and we found no release notes confirming any of the three has shipped.

For readers weighing a dedicated tool, this is the one to watch. It would cover part of the ground that draft-by-draft feedback covers today, for institutions that buy an AVA license. Anthology has not published details we can compare yet, such as who writes the feedback instructions, which feedback styles exist, or whether subject-specific models are involved. The right time to compare is when it reaches your test environment, using the pilot below.

## What does Eduface add inside a Blackboard Ultra course?

Eduface adds the step Blackboard's AI leaves to the instructor: reading each submission, scoring it against your rubric and drafting feedback, with the instructor approving before anything reaches a student or the gradebook. It connects to Blackboard through LTI 1.3. The instructor works from inside Blackboard to open Eduface, reviews the suggestions in the Eduface interface, and the approved grade returns to the Blackboard gradebook through LTI Grade Services. Students need no separate login. The setup steps live in our guide to the [AI essay grader for Blackboard via LTI 1.3](/resources/blog/ai-essay-grader-blackboard-lti), so we do not repeat them here.

- **Scoring against your rubric, criterion by criterion.** The Paper Grader reads each submission, marks specific passages, scores each criterion with an explainable breakdown, adds annotations in the text and flags where it is uncertain. You bring your rubric criteria and levels; if you have none, Eduface can generate a rubric.
- **Feedback on drafts.** The Paper Grader's formative feedback covers the first draft, the second draft and the final version, and tracks progress across drafts. The instructor writes the feedback instructions, picks a style (Reflective and Socratic, Constructive and Direct, Went Well and Needs Improvement, or Supportive and Encouraging) and decides whether feedback goes to the student directly or after approval.
- **Exam answers at scale.** In the Exam Grader, three independent AI agents grade each answer without seeing each other's result, and a fourth compares them. Agreement means high confidence; disagreement is flagged for the instructor. Eduface reports this is 48% more consistent than unaided human marking, with under 4 minutes from upload to suggested grade; the measurement setup is not public.
- **Subject models.** The Paper Grader has six subject models: Law, Economics, Social Sciences, STEM, Humanities and Health Sciences.
- **Consistency across graders.** A grader comparison dashboard shows when an individual grader departs from the team or from the AI suggestion. Blind mode lets the instructor grade first and see the AI suggestion afterward; AI-visible mode shows it from the start. The institution can require one.
- **A record.** Eduface keeps an audit trail per submission that meets AI Act requirements for summative assessments.

[FLOWDIAGRAM] Student submits in Ultra as usual → Eduface receives the work via LTI 1.3 → Scores each rubric criterion with an explainable breakdown, annotations and flagged uncertainty → Instructor reviews in the Eduface interface, opened from Blackboard (blind mode or AI-visible mode) → Instructor approves → Approved grade returns to the Blackboard gradebook via LTI Grade Services
*Figure 4: How Eduface sits next to Ultra (schematic). Nothing reaches the student or the gradebook until the instructor approves.*

> **What Eduface doesn't do**
> Eduface is not a course-design assistant: it does not draft modules, question banks or AI Conversations, and Blackboard's AI Design Assistant is the right tool for that. Instructors review suggestions in the Eduface interface, not inside Blackboard's Flexible Grading page. It is one more vendor for IT and procurement to review. Academic Integrity and Oral Examination are still in beta. If Blackboard's tools already cover what your instructors need, those costs are not worth paying.

## How do Blackboard AI and Eduface compare side by side?

Blackboard's AI builds and words; Eduface scores and drafts. The two answer different questions, and the table puts them on the same rows.

| | Blackboard AI (AI Design Assistant and AVA) | Eduface via LTI 1.3 |
|---|---|---|
| Main job | Draft course content, rubrics and prompts; reword or summarize feedback¹ ³ | Score submissions against your rubric and draft feedback |
| Rating or grade for a submission | None documented | Per criterion, with an explainable breakdown |
| Draft-to-draft feedback for students | Announced for AVA, not yet released as far as we read⁹ | Paper Grader's formative feedback; four styles; progress across drafts |
| Where the instructor works | Inside Blackboard | In Eduface, opened from Blackboard |
| Consistency across graders | No AI feature documented for comparing graders | Grader comparison dashboard; blind or AI-visible mode |
| Record of AI use | Output metadata flags auto-generated content and whether the instructor edited it⁶ | Audit trail per submission for summative assessments |
| Model and data | Azure OpenAI, primarily hosted in the US; no retraining⁶ ¹⁰ | Own model, no third-party AI API; EU processing; DPA with every institution |
| License | AVA features need a specific AVA license; AI Design Assistant not tied to it in the pages we read⁸ ⁹ | Ask for pricing at your volume |

*Table 3: Blackboard AI and Eduface on the same rows. Blackboard facts from Anthology, read October 19, 2026.*

## When is Blackboard's own AI enough?

For many instructors it is enough, and that is where to start. A rubric first draft, an assignment prompt, a set of test questions and a rewrite of rough comments all live where your instructors already work, and none of them adds a vendor to review. Blackboard's own AI fits when:

- **One instructor grades one section** against a rubric they wrote, so consistency between graders is not the problem.
- **The pain is in writing, not scoring.** The instructor knows the grade at a glance and loses the time turning notes into comments. That is what Summarize and Rewrite are for, if your institution has the AVA license.
- **The work is low-stakes:** reflections, discussion posts, practice assignments.
- **You are building a new course** and want first drafts of rubrics and prompts.
- **There is no budget for another tool this year.** A feature instructors use beats a better tool nobody approves.

A dedicated tool earns its place when the problem moves from one instructor's time to the program's consistency, evidence and feedback loop. That is common at private and for-profit colleges: several campuses or intakes a year, part-time instructors grading the same capstone, accreditors asking how a grade was reached.

Here is how that can look in practice. EXAMPLE scenario: a multi-campus technical college runs the same capstone at four campuses, with nine part-time instructors and three intakes a year. Instructional designers use the AI Design Assistant to draft rubrics and assignment prompts for new courses (build). Full-time faculty use Summarize and Rewrite on weekly assignments, if the college buys the AVA license (word). The program director pilots a dedicated tool only on the capstone, because the problem there is not speed but whether nine graders give the same grade for the same work (score).

| If your situation is | Start with |
|---|---|
| Building rubrics, prompts and test questions for a new course | Blackboard AI Design Assistant |
| Instructors who know the grade but spend the time on wording | AVA Summarize and Rewrite, if licensed |
| Many part-time instructors grading the same assessment across campuses | A dedicated tool with grader comparison |
| Open-answer exams at volume | Eduface Exam Grader |
| Feedback on drafts before the final submission | Eduface's formative feedback; compare with AVA Formative Feedback when it ships |
| Summative work where you must show how each grade was reached | A dedicated tool with an audit trail |

*Table 4: A starting point by situation, not a verdict. Many programs will use both.*

[FIGUUR: A decision tree titled "Which AI do you need for this assessment? (schematic)". Start node "Assessment to support". Question 1 (diamond): "Is the pain building the instrument (rubric, prompt, questions)?" Yes → green end node "Blackboard AI Design Assistant". No → Question 2: "Is the pain turning your own notes into comments?" Yes → green end node "AVA Summarize and Rewrite (needs AVA license)". No → Question 3: "Do you need a score or draft feedback on the submission itself?" Yes → Question 4: "Do several graders, a regulator or an accreditor need consistency and a record?" Yes → navy end node "Dedicated tool via LTI 1.3, such as Eduface". No → amber end node "Pilot both on 25 to 40 submissions". Question 3 No → grey end node "Keep grading by hand with a clear rubric". Highlight the navy end node.]
*Figure 5: Start from the pain, not the product. Two of the four exits are Blackboard's own tools.*

## How do you pilot the two side by side?

Run each tool on the job it claims to do, record the instructor's own work first, and compare a few numbers. A demo cannot answer this; your submissions and your rubric can.

1. **Pick one real assessment** with a rubric whose levels have descriptors. Twenty-five to forty submissions is enough to see a pattern.
2. **Use submissions you are allowed to use,** within your policy and each vendor's data agreement.
3. **Record the instructor's ratings and grade first,** before anyone sees an AI output. Otherwise you measure agreement with a number the instructor has already seen.
4. **Test Blackboard's wording tools** on a sample of the submissions: note minutes per submission and the share of AI-drafted comments sent without edits.
5. **Test the dedicated tool** on the same submissions and rubric: note the points difference from the instructor, the share of criteria where the rating matches, and minutes per submission including review.
6. **Add a second grader if you can.** If two instructors differ more than either tool does, consistency is the bigger problem.

| Measure | How to record it | Applies to |
|---|---|---|
| Minutes per submission | Stopwatch from opening the submission to approving the feedback | Both |
| Comments sent unedited | Count of AI-drafted comments posted without changes | Both |
| Points difference from the instructor | AI suggestion minus the instructor's grade, per submission | Scoring tools only |
| Criterion match rate | Share of criteria where the AI rating equals the instructor's | Scoring tools only |
| Second-grader gap | Difference between two instructors on the same submissions | Reference point |

*Table 5: A pilot recording sheet. Blackboard's wording tools do not produce a grade, so only the first two rows apply to them.*

[FIGUUR: A horizontal stacked bar chart titled "EXAMPLE: where the minutes go on one 1,500-word essay (illustrative numbers, not a measurement)". Three bars. Bar 1 "Grading by hand in Flexible Grading, 20 min": segments "Read the essay 7", "Rate the rubric 4", "Write the comments 9". Bar 2 "With Summarize and Rewrite, 17 min": segments "Read the essay 7", "Rate the rubric 4", "Short criterion notes 4", "Accept or edit the summary 2". Bar 3 "Dedicated tool: measure it in your pilot": an empty dashed bar with the text "your numbers". Highlight: in bars 1 and 2 the "Read the essay" and "Rate the rubric" segments are the same length and colored grey; only the writing segments differ and are colored teal.]
*Figure 6: EXAMPLE numbers. A wording tool can only shrink the writing segment; reading and rating stay with you, which is the segment a scoring tool targets.*

On evidence, be careful with every vendor claim, including ours. In the pages we read, Anthology publishes no accuracy figures for its feedback features, which is expected for tools that do not grade. Eduface's evidence is one pilot at one institution: at Bath Spa University in June 2026, across 435 submissions in 6 subjects and 13 markers, Eduface's suggested grade was on average about 6 points from the lecturer's grade, and about 2 points for lecturers who had tuned the model. Review took 2 to 3 minutes per submission. It is not known whether lecturers graded before or after seeing the suggestion, which is why step 3 above records the instructor's work first. Our [guide to AI grading tools](/resources/blog/ai-grading-tools-higher-education-guide) covers what else to compare.

## What should you tell students about AI in grading?

Tell them which tools touch their work, who decides the grade, and where their data goes. Blackboard's documentation helps with the first part: the Summarize and Rewrite suggestions carry an AI-generated banner for the instructor, and the output metadata records that content was auto-generated and whether the instructor edited it.³ ⁶ We did not find a student-facing label in the pages we read, so the disclosure is yours to write. Anthology encourages institutions to be transparent about AI use with instructors and other stakeholders.⁶ In Eduface, the interface shows a "Lecturer + AI" label to make clear that each feedback point was reviewed by the instructor before the student sees it.

> **Copy-ready syllabus wording (adapt it)**
> "In this course, your instructor may use [tool name] to draft or reword feedback on your work. Your instructor reads every submission and decides every grade. [Tool name] processes [what is sent] in [where]. If you have a question about a grade, contact [name] within [number] days."

## What to do next

Four actions will settle most of this inside a month.

1. **Ask your Anthology account representative for the license position in writing:** which AI features your contract includes, whether AVA is licensed or in the test environment only, and the price at your enrollment.
2. **Switch on the AI Design Assistant for one program** and have an instructional designer generate a rubric for one real assignment. Review every cell, then compare it with the rubric your instructors already trust.
3. **Decide which problem you actually have:** building, wording, or scoring and consistency. Use Table 4 and Figure 5.
4. **If scoring or consistency is the problem, run the pilot above** with success criteria agreed before you start, and read our guide to [grading assignments faster in Blackboard Ultra](/resources/blog/how-to-grade-assignments-in-blackboard-ultra) first so the baseline is a well-run manual process.

## Frequently asked questions

**Does Blackboard Ultra have AI grading?**
No, not in the Anthology documentation we read on October 19, 2026. Blackboard's AI generates course content and rubrics, and the AVA feedback options summarize or rewrite feedback from the rubric levels and comments you entered. None proposes a grade or a rubric rating for a submission. Anthology says it has "intentionally omitted potentially high-stakes functionalities" from these feedback tools.

**Is Blackboard AI free?**
Not all of it. AVA, which includes the Summarize and Rewrite feedback options, was free for current customers through June 30, 2026 and has needed a specific license since July 1, 2026. The pages we read do not say the AI Design Assistant needs that license, but we found no price or contract terms, so confirm with your Anthology account representative.

**Can the Blackboard AI Design Assistant generate a rubric?**
Yes. If your institution has turned the AI Design Assistant on, you can generate a rubric from the Course Rubrics page by describing it, choosing the type (percentage, percentage range, points, point range or no points), setting the size and selecting Generate. Anthology tells you to review each cell for accuracy before saving.

**Does Blackboard use student data to train its AI?**
No, according to Anthology. Its transparency notes say Microsoft contractually commits not to use input or output of the Azure OpenAI Service to retrain the models, and that Blackboard does not fine-tune the models with client data. Microsoft stores prompts and output for up to 30 days for content filtering, and the primary instance is hosted in the United States.

**Can we use AVA and Eduface in the same Blackboard course?**
Yes, split by job. AVA Summarize or Rewrite can polish comments on assignments an instructor grades by hand, and Eduface can handle the major paper or exam through LTI 1.3, with the approved grade returning to the Blackboard gradebook. Agree in advance which tool handles which assessment so students see one consistent process.

**Does Eduface work in Blackboard Ultra Course View?**
Yes. Eduface connects to Blackboard through LTI 1.3, and approved grades return to the gradebook through LTI Grade Services. Students need no separate login. The one-time setup for your administrator is covered in our guide to the [AI essay grader for Blackboard](/resources/blog/ai-essay-grader-blackboard-lti).

**What is Anthology adding to Blackboard AI next?**
Anthology's roadmap lists AVA Formative Feedback, which lets students check their work against the rubric before submitting, plus an AVA Virtual Assistant and the Pulse Quiz, with timings from one to six months out as of September 2026. Anthology says timings are subject to change, and we found no release notes confirming that any of the three has shipped.

<!-- RE-CHECK BEFORE PUBLISHING (review_by 2026-12-15). Blackboard AI licensing and features change fast.
1. AVA price and terms: no price found in any page read on 2026-10-19. Ask Anthology or check a current contract. Confirm whether Blackboard AI Design Assistant (incl. rubric generation) is included in every license; the pages read only tie the 2026-06-30 end date to AVA.
2. October 2026 release notes (4001.2) and later: NOT opened. Check for any change to AVA feedback, AI Design Assistant, or new grading-related AI.
3. Roadmap items (AVA Formative Feedback, Virtual Assistant, Pulse Quiz): "subject to change". If any has shipped, update the "What is coming next" section, Table 3 row 3, Table 4 row 5 and the last FAQ.
4. The Trust Center "List of generative AI features" page returned 404; check it for any grading-related feature we missed.
5. UI label: the Flexible Grading page calls the button "Summarize rubric feedback", the AVA page calls it "Summarize". The admin page lists an "AI Summarization" setting for both Summarize and Rewrite. Confirm in a test environment.
6. Sept 23, 2026 Community post: header says September 23, its "Related" box says Sep 7. Cited as September 23 (the header date).
7. Eduface claims to confirm with Dante: whether Eduface feedback can appear inside Blackboard's own feedback panel or Bb Annotate (NOT claimed); whether an existing Blackboard rubric can be imported (NOT claimed).
-->

## References

1. Anthology. (2026). "AI Design Assistant." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/course-and-content-management/ai-design-assistant.html. Accessed October 19, 2026. [Key finding: the AI Design Assistant generates course structure, discussions, journals, assignment prompts, test questions, question banks, rubrics, AI Conversations, images and document layouts, at ten complexity levels from early primary school to advanced PhD; partnered with Microsoft.]
2. Anthology. (2026). "AI Conversation." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/course-and-content-management/add-content/ai-conversation.html. Accessed October 19, 2026. [Key finding: Socratic Questioning, Role-play and Pulse Quiz; Pulse Quiz requires an AVA license and is off by default; Pulse Quiz results are not graded automatically or passed to the gradebook; instructors review the transcript and reflection.]
3. Anthology. (2026). "AVA – AI Virtual Assistant." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/course-and-content-management/ava---ai-virtual-assistant.html. Accessed October 19, 2026. [Key finding: AI Playground, responses to student messages, Summarize from a completed rubric (inputs: criteria, selected levels, descriptions, criterion feedback, existing overall feedback), Rewrite (at least 30 characters); accept, reject or regenerate; the Playground is not connected to assessments or grades.]
4. Anthology. (2026). "Create or Generate Rubrics." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/rubrics/create-or-generate-rubrics.html. Accessed October 19, 2026. [Key finding: rubric generation steps, five rubric types (percentage, percentage range, points, point range, no points), review each cell, only one rubric per item, 1,000-character cell limit, plain text only.]
5. Anthology. (2026). "Grade Assessments With Flexible Grading." Blackboard Help for Instructors. help.anthology.com/blackboard/instructor/en/grading/grading-assessments/grade-assessments-with-flexible-grading.html. Accessed October 19, 2026. [Key finding: the grading path from the Submissions page to the feedback panel and the Summarize rubric feedback option.]
6. Blackboard Trust Center. (2026, last updated February 27). "AVA Assisted Feedback – Transparency Note." anthology.com/trust-center/ava-assisted-feedback-transparency-note. Accessed October 19, 2026. [Key finding: premium capabilities license; Azure OpenAI Service; hosted primarily in the United States, at times Canada, the UK or France; stored in the client's Blackboard database; Microsoft stores prompts and output up to 30 days; no retraining; "intentionally omitted potentially high-stakes functionalities"; no automated decision-making with significant effect.]
7. Anthology. (2025, July 15). "Anthology Unveils Next-Generation AI and Immersive Learning Innovations in Blackboard." anthology.com/news. Accessed October 19, 2026. [Key finding: AVA capabilities offered as a free trial to current Blackboard customers through June 30, 2026; AI Design Assistant for Documents part of the core license.]
8. Anthology. (2026). "AI Design Assistant and Unsplash Configuration." Blackboard Help for Administrators. help.anthology.com/blackboard/administrator/en/integrations/ai-design-assistant-and-unsplash-configuration.html. Accessed October 19, 2026. [Key finding: "AVA features are included in your Blackboard LMS license until 30 June 2026. After that date, a specific AVA license will be required"; settings in the AI Design Assistant and Unsplash building block, off by default; privilege Generate AI Feedback Changes.]
9. Blackboard Community. (2026, September 23). "The latest in AI-powered pedagogy: Three great new capabilities on the way for AVA." community.blackboard.com. Accessed October 19, 2026. [Key finding: as of July 1, 2026 AVA is a premium capability needing a specific license; test and stage access until end of 2026; Socratic and Role-play remain core; Pulse Quiz AVA-only; AVA Formative Feedback lets students check work against the rubric before submission; timings subject to change.]
10. Anthology. (n.d.). "Blackboard AI Design Assistant." Blackboard Help for Administrators. help.anthology.com/blackboard/administrator/en/tools-management/blackboard-ai-design-assistant.html. Accessed October 19, 2026. [Key finding: Azure OpenAI Service; limited course information plus instructor-added prompt context; primary instance in the United States; no retraining; opt-in; privilege Use AI Design Assistant.]
11. Blackboard Community. (2026, July 31). "Doubling Down on Usability: Major Enhancements in the Blackboard LMS Roadmap." community.blackboard.com. Accessed October 19, 2026. [Key finding: AVA Formative Feedback listed as Next: 3-6 months; AI Flashcards part of the core license; dates subject to change.]
