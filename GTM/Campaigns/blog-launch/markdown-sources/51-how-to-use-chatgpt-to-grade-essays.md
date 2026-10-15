---
title: "How to Use ChatGPT to Grade Essays With a Rubric: Prompts, Limits and a Better Workflow"
seo_title: "How to Use ChatGPT to Grade Essays (Prompts) | Eduface"
meta_description: "How to use ChatGPT to grade essays with a rubric: three copy-ready prompts, a consistency test, what happens to student data, and when a grading tool fits."
slug: how-to-use-chatgpt-to-grade-essays
primary_query: "how to use chatgpt to grade essays"
secondary_queries: ["chatgpt grading prompt", "how to use chatgpt to grade essays with a rubric", "chatgpt grading papers", "can chatgpt grade essays", "chatgpt essay grading accuracy"]
type: werkwijze
category: Product
hub: /resources/blog/grading-papers-with-ai
related: [/resources/blog/ai-grading-tools-higher-education-guide, /resources/blog/how-to-write-a-rubric-ai-can-mark-against]
review_by: 2027-01-15
status: concept
components: "10 figures, 6 tables, 4 card grids, 9 callouts (3 copy-ready prompts). Card grids use the [CARDS: n] ... [/CARDS] notation below, one item per line as '- **Title** | text'."
---

EYEBROW: CHATGPT · ESSAY GRADING

# How to Use ChatGPT to Grade Essays With a Rubric: Prompts, Limits and a Better Workflow

*Three copy-ready grading prompts, a ten-minute consistency test, what happens to student work when you paste it in, and a clear line between the assignments where ChatGPT is fine and the ones where it is not.*

By Eduface · October 2026 · 19 min read · Written for instructors and program directors at private and for-profit colleges

You have 34 essays due back on Monday and a rubric you trust. A colleague mentions that she pastes her rubric into ChatGPT and gets a grade and a paragraph of feedback in under a minute. You try it on one essay you already graded. The grade comes back four points higher than yours, the feedback reads well, and you cannot tell which of the two you should believe.

> **How to use ChatGPT to grade essays**
> Yes, you can use ChatGPT to grade essays, if the prompt is anchored to your rubric: score each criterion separately, quote evidence from the essay for every score, forbid invented content, and fix the output format. Three limits remain. The same essay can get a different grade on a second run, pasting student work into a personal account raises privacy questions under FERPA and your college's policy, and nothing records how the grade was reached. Treat every ChatGPT grade as a draft and review it yourself.

## What does ChatGPT do well, and where does it break, when it grades an essay?

ChatGPT is a strong reader of text and a weak judge of academic quality. It summarizes an argument, spots a missing citation and drafts a clear comment in seconds. It is less reliable at weighing those observations into a grade, and it tends to reward how well a student writes over how well they reason.

[CARDS: 3]
- **What ChatGPT does well** | Summarizing the argument, finding passages that match a descriptor, spotting surface problems (missing citations, a thesis that drifts), and turning your notes into readable feedback.
- **Where it breaks** | Grades that run high on fluent but thin essays, different scores for the same essay on different runs, quotes that are not in the essay, and rubric weights it quietly ignores.
- **What you still own** | The grade, the decision on borderline essays, what happens to the student's work, and the record of how you got there. No prompt moves any of these to the tool.
[/CARDS]

[FIGUUR: A horizontal spectrum titled "Where ChatGPT is reliable, and where it drifts". Left end, green, labelled "Reliable": "Summarize the thesis", "Find passages for a descriptor", "Check citation format", "Draft feedback from your notes". Middle, amber, labelled "Needs checking": "Score a single criterion", "Name the weakest section", "Suggest a level between two descriptors". Right end, red, labelled "Drifts": "Overall grade on a fluent but weak essay", "Same grade on a second run", "Weighting criteria the way your rubric does", "Quotes copied exactly". A small arrow under the spectrum reads "the further right, the more you review".]
*Figure 1: The closer a task gets to a final judgment, the more ChatGPT drifts and the more of your review it needs.*

That split decides how to use it. Ask ChatGPT for what it reads well (evidence, structure, a draft comment) and keep the weighing for yourself. The prompts below are built that way.

## How do you use ChatGPT to grade essays, step by step?

Grading essays with ChatGPT takes six steps, and the prompt is only one of them. The steps around it are what make the grade defensible: checking the account, calibrating on essays you already graded, testing consistency and reviewing every result.

[FLOWDIAGRAM] 1 Check the account (approved for student data? identifiers removed) → 2 Turn the rubric into a prompt (criteria, levels, evidence rule, fixed format) → 3 Calibrate (3 to 5 essays you already graded) → 4 Grade one essay per fresh chat (same prompt every time) → 5 Test consistency (3 runs on a sample) → 6 Review and record (you decide, the gradebook holds your grade)
*Figure 2: ChatGPT drafts in step 4. Steps 1, 3, 5 and 6 are where the instructor keeps control.*

1. **Check the account before the essay.** Ask whether your college has approved a ChatGPT plan for student work. If it has not, use ChatGPT only for rubric drafting and model answers, and keep student essays out. More on this below.
2. **Turn your rubric into a prompt.** Paste the criteria, the weight of each, and the descriptor for every level. "Good analysis" in your head becomes "compares two explanations and says why they differ" on the page. Our guide on [how to write a rubric AI can mark against](/resources/blog/how-to-write-a-rubric-ai-can-mark-against) covers this in detail.
3. **Calibrate on essays you already graded.** Run three to five graded essays from last term and compare per criterion. If ChatGPT is more than one level off on the same criterion in most of them, rewrite that descriptor before going further.
4. **Grade one essay per fresh chat.** Several essays in one conversation can bleed into each other: the third essay gets compared to the first instead of to the rubric.
5. **Test consistency on a sample.** Run a handful of essays three times each. The protocol is further down.
6. **Review and record.** Read each essay against the output, check the quotes, set the grade yourself and enter it in your LMS gradebook. Keep a short note of the prompt version you used.

## What does a good ChatGPT grading prompt look like?

A good grading prompt gives ChatGPT the rubric, a scale, a rule to quote evidence, a rule not to invent, and an output format it cannot drift from. Most prompts shared online stop at "grade this essay using this rubric", which invites a fluent paragraph and a generous number.

[FIGUUR: An annotated prompt card, drawn as a single white card with eight colored brackets on its left edge, each with a label on the right. 1 "Role" (navy): "You are a careful second reader, not the final grader." 2 "Context" (navy): assignment prompt and learning outcomes. 3 "Rubric" (green): criteria, weights, descriptors for every level. 4 "Scale" (green): points per criterion and grade boundaries. 5 "Evidence rule" (mint): "Quote 1 to 3 passages per criterion, word for word." 6 "No-invent rule" (mint): "Do not invent quotes, sources or facts." 7 "Tie-break rule" (amber): "Between two levels, choose the lower and explain." 8 "Output format" (amber): fixed table plus TOTAL, WEAKEST CRITERION, CHECK THESE. A footer strip reads "The essay goes last, with name and ID removed."]
*Figure 3: Eight parts make a grading prompt checkable; the evidence and no-invent rules are what let you verify the output.*

> **Copy-ready prompt 1: Rubric grading with evidence and confidence**
> You are grading one student essay against the rubric below. You are a careful second reader, not the final grader.
>
> ASSIGNMENT: [paste the assignment prompt and the learning outcomes]
> RUBRIC: [paste every criterion with its weight and the descriptor for every level]
> SCALE: [for example: each criterion scored 0 to its maximum; total out of 100; A = 90 and above, B = 80 to 89]
>
> Rules:
> 1. Score each criterion separately, using only the rubric descriptors. Do not reward length, vocabulary or polish unless a criterion asks for it.
> 2. For every criterion, quote one to three short passages from the essay, word for word, that support your score. If you find no evidence, write "No evidence found" and score accordingly.
> 3. Do not invent quotes, sources, page numbers or facts. If something is unclear, say so instead of guessing.
> 4. If the essay sits between two levels, choose the lower level and say what would move it up.
> 5. Give a confidence note per criterion: High, Medium or Low, with one sentence on why.
>
> Output exactly this format and nothing else:
> CRITERION | LEVEL | POINTS (of max) | EVIDENCE (quotes) | REASON (max 40 words) | CONFIDENCE
> [one row per criterion]
> TOTAL: [points] of [max]
> WEAKEST CRITERION: [name], because [one sentence]
> CHECK THESE: [anything a human grader should verify]
>
> ESSAY: [paste the essay text with the student's name and ID removed]

Rule 4 is the one most prompts leave out. In the test described below, ChatGPT's errors ran high, not low, so a tie-break toward the lower level pushes against its known tendency. You still decide where the essay lands; the rule only changes where the draft starts.

The fixed format does two jobs. It stops ChatGPT from answering in a paragraph that hides a weak score behind kind words, and it gives you output you can paste straight into a spreadsheet or into the consistency check further down. Put the essay last, after the rules, so the instructions are not buried under 2,000 words of student text.

| Rubric element | What the prompt should say | Why it matters |
|---|---|---|
| Criterion name | The name plus one sentence on what it covers | Stops two criteria from blending into one judgment |
| Weight | "Thesis: 20 of 100 points" | Without it, ChatGPT tends to weigh every criterion equally |
| Level descriptors | The full descriptor for every level, not only the top one | It needs the boundary between B and C, not just a picture of an A |
| Evidence expectation | "Quote the passage that shows this" | Turns a score into something you can check in seconds |
| Common errors | "A summary of sources is not analysis" | Names the shortcut a fluent essay takes |
| Grade boundaries | Points per letter grade | Lets the total map onto your gradebook without guessing |

*Table 1: Translating a rubric into a prompt. Each row closes a gap ChatGPT would otherwise fill with its own judgment.*

[FIGUUR: An annotated example of a good output, drawn as a table excerpt with three rows (Thesis, Use of evidence, Organization) and callout bubbles. Row "Use of evidence | Level 2 | 12 of 25 | 'Studies show social media is bad for teens' | Claims cited without data or source | Medium". Bubble 1 points to the quote: "Ctrl+F this in the essay. Found? Keep. Not found? Discard the whole row." Bubble 2 points to the confidence column: "Medium or Low = read this criterion yourself." Bubble 3 points to a row with "No evidence found": "Honest gap, not a failure of the prompt." All content labelled EXAMPLE.]
*Figure 4: Structured output turns review into checking: search each quote, read every Low-confidence criterion, and discard any row whose evidence you cannot find.*

## Which ChatGPT grading prompt should you use for which assignment?

Use the rubric-grading prompt for summative essays, the feedback-only prompt for drafts, and adjust the evidence rule to what the assignment type rewards. A lab report and a reflective journal need ChatGPT to look for different things, and the prompt has to say so.

| Assignment type | Prompt to start from | Change this in the prompt | Watch for |
|---|---|---|---|
| Argumentative essay | Prompt 1 | Add "A summary of sources is not analysis" | High scores for fluent, thin arguments |
| Case study or business report | Prompt 1 | Ask it to quote where each recommendation is justified by the case facts | Credit for frameworks named but not applied |
| Lab or technical report | Prompt 1 | Ask for evidence per section (method, results, discussion) | It cannot check whether the data are correct |
| Reflective writing | Prompt 2 | Ask for quotes that show reflection, not description | Identifiable personal details in the text |
| Draft or outline | Prompt 2 | Limit feedback to the two criteria that matter most now | Feedback so long the student acts on none of it |

*Table 2: Prompt variants by assignment type. The evidence rule changes with what the assignment rewards.*

[CARDS: 3]
- **Prompt 1: Rubric grading** | Summative essays where you need per-criterion scores. Outputs a fixed table with quoted evidence, a total and a confidence note per criterion.
- **Prompt 2: Feedback only** | Drafts and formative work. No grade, two priorities for revision, one strength, every point tied to a quote. The lowest-risk use of ChatGPT in grading.
- **Prompt 3: Consistency check** | Run after three separate grading runs of the same essay. Compares scores and evidence per criterion and flags the criteria that move.
[/CARDS]

> **Copy-ready prompt 2: Feedback only, no grade**
> You are writing formative feedback on a student's draft. Do not give a grade, score or level.
>
> ASSIGNMENT: [paste the assignment prompt]
> RUBRIC: [paste the criteria and descriptors]
> FEEDBACK STYLE: [for example: direct and constructive, plain language, maximum 200 words]
>
> Rules:
> 1. Pick the two criteria where revision would improve the draft most.
> 2. For each, quote the passage you are commenting on, word for word, then say what to change and why, tied to the rubric descriptor.
> 3. Name one thing that works, with a quote.
> 4. Do not rewrite the student's text. Do not invent sources, facts or quotes.
> 5. Address the student as "you".
>
> Output exactly this format:
> WHAT WORKS: "[quote]" [one sentence]
> REVISE FIRST: [criterion] "[quote]" [what to change and why]
> REVISE NEXT: [criterion] "[quote]" [what to change and why]
> ONE QUESTION TO THINK ABOUT: [one question]
>
> DRAFT: [paste the draft with the student's name and ID removed]

## How accurate is ChatGPT at grading essays?

ChatGPT's essay grades were close on average but ran high on weak papers in the one test we can point to. In a small test published in our [guide to AI grading tools in higher education](/resources/blog/ai-grading-tools-higher-education-guide), ChatGPT averaged about 0.9 points from the lecturer's grade across five psychology papers, on the Dutch 10-point scale.¹ That average hides the cases that matter most.

On a developmental psychology case study the lecturer graded 6.5, ChatGPT returned 8.1, and it praised the section the lecturer had flagged as the weakest. On a constitutional law essay graded 4.4, below a pass, it returned 7.1. On that same law essay, Eduface returned 5.5.¹

[FIGUUR: Grouped bar chart titled "ChatGPT against the lecturer's grade, Dutch 10-point scale". Group 1 "Psychology case study": Lecturer 6.5 (navy), ChatGPT 8.1 (amber), annotation "praised the weakest section". Group 2 "Constitutional law essay": Lecturer 4.4 (navy, annotated "below a pass"), ChatGPT 7.1 (amber), Eduface 5.5 (green). Side panel: "Five psychology papers: ChatGPT on average about 0.9 points from the lecturer". Footer: "Two students, eight tools, six papers with known lecturer grades. Directional, not a ranking."]
*Figure 5: The average looked acceptable; the misses were on the weakest papers, where a generous grade does the most harm.*

> **How the test was set up**
> Two students in the Netherlands, one in psychology and one in law, ran six papers through eight tools. Every paper came with the lecturer's final grade and the official rubric, so the right answer was known in advance. Each tool got the full paper and rubric and was asked to grade per criterion. Six papers point in a direction; they do not make a ranking, and the test reflects ChatGPT as it was in July 2026. Run your own calibration.

The pattern is more useful than the numbers. ChatGPT responded to how well the student wrote: a fluent essay with a weak argument read as a strong one. That is why the prompt above asks for quoted evidence per criterion and breaks ties downward, and why calibration on essays you already graded comes before any live use.

## How consistent is ChatGPT when you grade the same essay twice?

ChatGPT can give the same essay a different grade on a second run, so test it on your own assignment before trusting a single run. There is no general consistency figure you can rely on, because the spread depends on your prompt, your rubric and the assignment. A ten-minute test tells you more than any general claim.

[FIGUUR: Three side-by-side cards labelled "Run 1", "Run 2", "Run 3", same essay, same prompt, fresh chat each time. All numbers labelled EXAMPLE. Run 1: Thesis 16/20, Evidence 18/25, Analysis 19/30, Organization 12/15, Mechanics 8/10, TOTAL 73. Run 2: 17, 21, 22, 12, 8, TOTAL 80. Run 3: 16, 17, 20, 13, 9, TOTAL 75. Below, a strip: "Spread per criterion: Thesis 1, Evidence 4, Analysis 3, Organization 1, Mechanics 1. Total spread: 7 points (C to B-)". Evidence and Analysis highlighted in amber.]
*Figure 6: In this example, one essay lands at 73, 80 and 75 on three runs; the spread sits in the criteria that need judgment, not in mechanics.*

**A consistency protocol you can run on one assignment:**

1. **Pick five essays across the range.** One you graded high, one low, one borderline and two in the middle.
2. **Run Prompt 1 three times per essay, each in a new chat.** Use a Temporary Chat or a fresh conversation so nothing from an earlier essay carries over. Do not edit the prompt between runs.
3. **Paste the three outputs into Prompt 3.** It returns the spread per criterion and flags evidence that changes between runs.
4. **Search every quote in the essay.** Use Ctrl+F. A quote that is not in the essay disqualifies that row, whatever the score.
5. **Read the result against thresholds you set beforehand.** Table 3 has an EXAMPLE set for a 100-point scale.

> **Copy-ready prompt 3: Consistency check across three runs**
> Below are three grading outputs for the same essay. Each was produced in a separate chat with the same prompt and rubric. Compare them. Do not grade the essay yourself and do not add opinions about it.
>
> Rules:
> 1. For each criterion, report the three scores and the spread (highest minus lowest).
> 2. For each criterion, say whether the three runs quoted the same evidence: Yes, Partly or No.
> 3. List every quote that appears in only one run.
> 4. List the criteria where the spread is larger than [X] points.
> 5. Use only the three outputs below. Do not invent scores or quotes.
>
> Output exactly this format:
> CRITERION | RUN 1 | RUN 2 | RUN 3 | SPREAD | SAME EVIDENCE?
> TOTALS: [run 1], [run 2], [run 3], spread [n]
> QUOTES IN ONE RUN ONLY: [list]
> UNSTABLE CRITERIA: [list]
>
> RUN 1: [paste]
> RUN 2: [paste]
> RUN 3: [paste]

| Total spread across 3 runs (EXAMPLE, 100-point scale) | What it means | What to do |
|---|---|---|
| 0 to 3 points | Stable on this assignment | Use single runs, keep full review |
| 4 to 6 points | Stable on mechanics, moving on judgment criteria | Tighten the descriptors that move, rerun the sample |
| 7 points or more, or crosses a letter boundary | Not stable enough for a recorded grade | Use Prompt 2 for feedback only, grade by hand |
| Any quote not found in the essay | The output is not grounded | Discard that row; if it repeats, stop using it for grades |

*Table 3: Reading the consistency test. Set the thresholds before you look at the runs, not after.*

## What happens to student work when you paste an essay into ChatGPT?

What happens depends on the ChatGPT plan, and on a personal plan the essay leaves your college's control. OpenAI states that on ChatGPT Free, Plus and Pro, data sharing for model training is on by default, and users can turn it off in Data Controls with the "Improve the model for everyone" setting.² Temporary Chats are not used for training and are deleted after 30 days, although OpenAI notes that legal developments may affect that retention.³ For ChatGPT Business, Enterprise and Edu, and for its API, OpenAI states that it does not use inputs or outputs for training by default.²

[FIGUUR: Two-lane data flow titled "Where an essay goes when you paste it". Top lane "Personal account (Free, Plus, Pro)": Student essay in your LMS → copied to your clipboard → pasted into ChatGPT under your personal login → stored in your chat history → training on by default unless you opt out; no agreement between your college and OpenAI. A red marker on the arrow leaving the LMS: "leaves college control here". Bottom lane "College-licensed plan (Edu, Enterprise, Business)": Student essay → pasted into a workspace your college administers → no training by default per OpenAI → retention and access set under your college's agreement. A green marker: "covered by an agreement your college signed". Both lanes end in the same box: "The grade still has to be copied into your gradebook by hand."]
*Figure 7: The plan decides whether an agreement covers the essay; neither plan connects the grade to your gradebook.*

Opting out of training is not the same as an agreement. For a US college, FERPA lets an institution share personally identifiable information from education records with an outside party without consent under the school official exception, provided that party performs a service the college would otherwise use employees for, is under the college's direct control with respect to the use and maintenance of education records, and is bound by the rules on use and redisclosure.⁴ A personal chatbot account has no contract with your college, so the direct-control condition is hard to meet. A college-licensed plan may meet it, depending on what the agreement says. That is your registrar's or privacy office's call, not ours.

Removing the name helps less than it seems. A reflective essay about a workplace, a family situation or a health condition can identify a student without a name on it.

> **Before you paste a single essay**
> Check four things. Has your college approved this ChatGPT plan for student work? Is the student's name, ID and any identifying detail removed? Does the assignment fall under a policy on AI use in grading that students have been told about? Will you record the grade yourself, after review, in the LMS gradebook? If any answer is no, use ChatGPT for rubric drafting and model answers only.

## Where does ChatGPT go wrong when grading essays, and how do you fix it?

Most ChatGPT grading errors come from a short list of failure modes, and each has a prompt or process fix. None of the fixes removes the need to review, but together they make the errors easier to see.

| Failure mode | What it looks like | Fix |
|---|---|---|
| Leniency on fluent writing | A 6.5 paper scored 8.1, weakest section praised | Evidence rule, tie-break downward, calibrate on graded essays |
| Invented evidence | A quote that is not in the essay | Ctrl+F every quote; discard the row if it is missing |
| Ignored weights | A 10-point criterion moves the total as much as a 30-point one | State points per criterion; check the arithmetic yourself |
| Drift across a batch | Essay 12 graded against essay 11, not the rubric | One essay per fresh chat, same prompt every time |
| Merged criteria | One comment covers "argument and evidence" | One thing per criterion in the rubric and the output table |
| Length bias | Longer essays score higher on every criterion | "Do not reward length" in the rules; spot-check a short strong essay |
| Hedged grades | "Somewhere between B and B+" | Fixed output format with a single number per criterion |

*Table 4: Failure modes with fixes. The process fixes (fresh chats, quote checks, calibration) matter as much as the prompt fixes.*

There is one failure that sits with the grader rather than the tool. When you see ChatGPT's grade before forming your own, your grade tends to move toward it. That is anchoring, and it gets stronger over a long stack.

[FIGUUR: Three-step illustration titled "Anchoring, in one essay". All numbers labelled EXAMPLE. Step 1, card "Your first read, no AI": 72. Step 2, card "ChatGPT's suggestion shown": 84, amber. Step 3, card "Your final grade after seeing it": 78, with a curved arrow from 72 to 78 labelled "pulled 6 points toward the suggestion". Footer: "Blind first, then compare: grade, then open the output."]
*Figure 8: When the suggestion comes first, it becomes the starting point; grading blind on part of every batch keeps your own standard visible.*

> **Watch for anchoring**
> Grade a few essays in every batch before you open ChatGPT's output: the borderline ones, the likely fails and one at random. If you find you have accepted a dozen suggestions in a row without changing anything, grade the next three blind.

## Should you use ChatGPT for this assignment?

Use ChatGPT for low-stakes formative comments and small batches on an approved account, and stop when grades count, student data is not covered or several graders share a rubric. The decision tree below puts that into four questions.

[FIGUUR: Decision tree titled "Should you use ChatGPT for this assignment?". Q1 diamond "Does the result count toward a recorded grade?" No → green box "Formative comments: Prompt 2 on de-identified drafts, approved account". Yes → Q2 "Has your college approved this ChatGPT plan for student work?" No → red box "Keep essays out. Use ChatGPT for rubric drafting and model answers only". Yes → Q3 "More than about 30 essays, or more than one grader or section?" Yes → blue box "A dedicated grading tool earns its place: calibration, audit trail, gradebook return". No → Q4 "Did your consistency test pass your thresholds?" Yes → green box "Prompt 1, one essay per chat, full review". No → grey box "Grade by hand this term; fix the rubric before next".]
*Figure 9: Two questions about stakes and data decide most cases before the question of accuracy comes up.*

[CARDS: 2]
- **When ChatGPT is fine** | Formative feedback on drafts with Prompt 2. A single section of 15 to 30 essays on an approved account, after a passed consistency test. Drafting rubric descriptors and model answers. Rewording your own comments.
- **When a dedicated tool earns its place** | Several sections or part-time instructors on one rubric. Grades that must flow back to the LMS gradebook. An appeal process that needs a record per grade. Student data that must stay under an agreement your college signed.
[/CARDS]

Even when the answer is no, ChatGPT still has a place in your grading week. It can draft level descriptors from your notes, write a model answer to test the rubric against, or turn your shorthand comments into full sentences. None of that needs a student essay.

## What does a better workflow look like across a whole program?

Across a program, the work shifts from writing prompts to keeping one standard across graders, sections and terms, and that is where ChatGPT has no tools. For the full instructor workflow, from rubric to audit trail, see our hub on [grading papers with AI](/resources/blog/grading-papers-with-ai). This section compares the three options a program director usually weighs.

| Question | ChatGPT, personal account | ChatGPT Edu, Enterprise or Business | Dedicated grading tool (Eduface here) |
|---|---|---|---|
| Training on student work | On by default, can be turned off² | Off by default² | Never used to train AI models |
| Agreement with your college | None | Your college's agreement with OpenAI | Data Processing Agreement with every institution |
| Rubric and consistency | Pasted each session; you test consistency | Pasted each session; you test consistency | Rubric-grounded scoring per criterion, grader comparison dashboard |
| Record and gradebook | Chat history, grade copied by hand | Chat history, grade copied by hand | Audit trail for summative assessment, grade returned to the LMS gradebook after approval |

*Table 5: ChatGPT on a personal plan, ChatGPT on a college plan, and a dedicated grading tool. The college plan fixes the data question; it does not add a grading workflow.*

The time difference is small for one class and large for a program. The example below uses EXAMPLE assumptions, except the review time for the dedicated tool, which comes from a June 2026 pilot at Bath Spa University where instructors reviewed each submission in 2 to 3 minutes.⁵

[FIGUUR: Two panels of horizontal bars, all numbers EXAMPLE except the review time noted. Panel A "30 essays": By hand 10 h (30 × 20 min). ChatGPT workflow 6.75 h (prompt setup 45 min, calibration 30 min, 10 min per essay for de-identifying, pasting, checking quotes and entering the grade, consistency test 30 min). Dedicated tool 4.5 h (setup and calibration 2 h, 3 min review × 25 routine essays based on the Bath Spa pilot, 5 full reads × 12 min, 1 h return and checks). Panel B "300 essays across 6 sections": By hand 100 h (300 × 20 min). ChatGPT workflow about 52 h (same setup, calibration and consistency test, 300 × 10 min). Dedicated tool 22.5 h (setup and calibration 2 h, 270 routine essays × 3 min, 30 full reads × 12 min, 1 h return and checks). Caption strip: "At 30 essays the gap is about 2 hours. At 300 it is about 30."]
*Figure 10: For one class, careful ChatGPT use costs little extra; at program scale, the per-essay copying and checking adds up.*

[CARDS: 3]
- **Blind mode** | In Eduface, instructors can grade first and see the AI suggestion afterwards, which works against anchoring. AI-visible mode shows it from the start, and an institution can make either mode mandatory.
- **Grader comparison dashboard** | Shows when an individual grader departs from the rest of the team or from the AI suggestion, without opening individual submissions. Useful when part-time instructors grade the same assignment.
- **Approval and gradebook return** | Every comment and suggested grade is held until the instructor approves it. The approved grade goes back to the LMS gradebook, and the audit trail records how it was reached.
[/CARDS]

Eduface's Paper Grader scores each essay against your rubric with an explainable grade breakdown per criterion and annotations in the text, using one of six subject models (Law, Economics, Social Sciences, STEM, Humanities, Health Sciences). It flags uncertainty instead of smoothing it over. Eduface runs its own model, not an API from OpenAI or another provider, processes student data in the EU, and never uses student work to train AI models. Individual instructors can start free with about 20 assignments a month, or use the Lecturer plan at $25 a month for about 200. The AI assists. The academic decides.

> **What Eduface doesn't do**
> Eduface does not decide grades, and it does not make a vague rubric precise on its own: a rubric it generates from your brief is a first draft. For a single class of 20 essays, the setup and calibration are a real share of the work, and careful ChatGPT use on an approved account with the prompts above may be all you need.

| Check for program directors | Why it matters | Who owns it |
|---|---|---|
| Which ChatGPT plans are approved for student work, in writing | Instructors otherwise decide account by account | Registrar or privacy office |
| A shared, versioned grading prompt per assignment | Two sections with different prompts have two standards | Course lead |
| A consistency test before first use on each assignment | Spread varies by rubric and assignment type | Course lead |
| A rule that every AI-suggested grade is reviewed and entered by the instructor | The gradebook must hold the instructor's decision | Program director |
| A syllabus line telling students how AI is used in grading | Heads off the appeal that starts with "a computer graded this" | Instructor |
| A point at which the program moves to a dedicated tool | Volume, number of graders or appeal records make the case | Program director |

*Table 6: A checklist for program directors before instructors use ChatGPT for grading.*

> **For program directors**
> The risk in a multi-section program is not one bad grade. It is six instructors using six versions of a prompt on six accounts, with no record of which produced which grade. Approve the plan, share the prompt, and decide in advance at what volume you move to a tool with an audit trail.

## Frequently asked questions

**Can ChatGPT grade essays accurately?**
It can come close on average and still miss badly on individual essays. In a small published test, ChatGPT averaged about 0.9 points from the lecturer on five psychology papers (Dutch 10-point scale) but scored a 4.4 law essay at 7.1. Calibrate it on essays you already graded and review every grade.

**Is it a FERPA problem to paste student essays into ChatGPT?**
It can be, and your college decides. FERPA's school official exception requires, among other conditions, that an outside party is under the college's direct control for the use and maintenance of education records. A personal ChatGPT account has no agreement with your college; ask your registrar or privacy office which plan, if any, is approved.

**Does ChatGPT Edu use student essays to train its models?**
No, not by default, according to OpenAI. OpenAI states that it does not use data from ChatGPT Edu, Enterprise, Business or its API for training by default. Training is on by default for personal Free, Plus and Pro accounts unless the user turns it off.

**Can I use ChatGPT to check whether an essay was written by AI?**
No, do not use it for that. ChatGPT is not a detection tool, and its opinion on whether a student used AI is not evidence of misconduct. Keep grading and integrity questions separate.

**How many essays can I grade in one ChatGPT chat?**
Grade one essay per chat. Essays in the same conversation get compared to each other instead of to the rubric, and the drift is hard to spot afterwards. Paste the same prompt into a fresh chat for every essay.

## References

<!-- OPEN POINT for Dante: references 2 and 3 are OpenAI pages that returned HTTP 403 to automated fetches on 15-10-2026. The wording in the text comes from OpenAI's own text as quoted in search results that day. Open both pages in a browser and confirm the wording before publishing. -->

1. Eduface. (2026). *The Complete Guide to AI Grading Tools for Higher Education.* eduface.me/resources/blog/ai-grading-tools-higher-education-guide. [Key finding: two students, eight tools, six papers with known lecturer grades and official rubrics; ChatGPT averaged about 0.9 points from the lecturer on five psychology papers, returned 8.1 on a 6.5 case study while praising the weakest section, and 7.1 on a 4.4 law essay, where Eduface returned 5.5. Directional, not a ranking.]
2. OpenAI. *Business data privacy, security, and compliance.* openai.com/business-data. Accessed October 15, 2026. [Key finding: by default OpenAI does not use data from ChatGPT Enterprise, Business, Edu or its API platform, including inputs and outputs, for training; on personal Free, Plus and Pro plans data sharing is on by default and users can opt out.]
3. OpenAI. *Data Controls FAQ.* help.openai.com/en/articles/7730893-data-controls-faq. Accessed October 15, 2026. [Key finding: turning off "Improve the model for everyone" stops chats from being used to improve ChatGPT; Temporary Chats are not used for training and are deleted after 30 days, with a note that legal developments may affect retention.]
4. 34 CFR § 99.31(a)(1)(i)(B). *Family Educational Rights and Privacy Act regulations.* Read via Cornell Law School, Legal Information Institute, October 15, 2026. [Key finding: an outside party may be considered a school official if it performs an institutional service for which the institution would otherwise use employees, is under the institution's direct control with respect to the use and maintenance of education records, and is subject to § 99.33(a) on use and redisclosure.]
5. Eduface. (2026). *Pilot at Bath Spa University, June 2026.* Internal pilot data. [Key finding: 435 submissions, 6 subjects, 13 markers; review took 2 to 3 minutes per submission.]
