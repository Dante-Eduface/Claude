---
title: "AI Grading Software for Law School Assignments: What It Should Do and How to Choose"
seo_title: "AI Grading Software for Law School Assignments | Eduface"
meta_description: "What AI grading software should do for law school assignments, what our test on a real law essay showed, and how to run a pilot before you commit."
slug: ai-grading-software-law-school-assignments
primary_query: "AI grading software for law school assignments"
secondary_queries: ["AI marking law problem questions", "AI grading law exams", "can AI mark law essays accurately", "AI grading OSCOLA", "AI assessment tool law faculty"]
type: koopgids
category: Product
hub: /resources/blog/ai-grading-tools-higher-education-guide
related: [/resources/blog/best-ai-feedback-tool-law-essays, /resources/blog/ai-essay-grader-law-students, /resources/blog/ai-grading-law-essays]
review_by: 2027-03-01
status: concept
---

EYEBROW: LAW · AI GRADING SOFTWARE

# AI Grading Software for Law School Assignments: What It Should Do and How to Choose

*AI grading software can take the first pass on problem questions, essays and exam scripts in a law school, but only if it reasons against your rubric and leaves the final mark with the lecturer. Here is what to look for, what our test on a real law essay showed, and how to pilot it.*

By Eduface · September 2026 · 16 min read · Written for law school leadership, module leaders and learning technologists

It is the second week of January. Your contract law module has 280 problem-question scripts waiting, four markers, a moderation deadline and an external examiner who will sample twenty of them. Two of your markers are new this year. Last year, a second-marking sample showed a spread of eight marks between markers on the same script. Nobody thinks AI should set law grades. But everybody is asking whether it could take the first pass.

> **What should AI grading software for law school assignments do?**
> AI grading software for law school assignments should read each submission against your own rubric, score every criterion with written reasoning, and hold that draft until a lecturer approves or changes it. For law, it must also separate structure from substance: spotting the issues and citing the right authority is not the same as applying the law convincingly to the facts. In our test on a real law essay graded 4.4, general AI tools returned between 6.8 and 10.0. A purpose-built tool returned 5.5.

## Why are law school assignments hard to mark consistently?

Law assessment asks markers to judge reasoning, not recall. A problem question gives the student a set of facts and asks them to advise a party. A strong answer identifies every legal issue, states the governing rule, applies it to the specific facts and reaches a conclusion a client could act on. A weak answer can do three of those four things and still read well.

That gap between polish and reasoning is where markers diverge. One marker rewards clear structure and accurate citation. Another looks straight past them to the application, because that is where the legal thinking happens. Both are defensible. Across 280 scripts and four markers, the result is inconsistency the external examiner will notice.

Three features of legal writing make this harder:

**Contested application.** Two students can reach opposite conclusions on the same facts and both deserve a first, as long as each engages with the strongest counter-argument. A rubric that rewards "the right answer" misses what the assessment is testing.

**Authority and citation.** Law students are expected to support every proposition with a case, a statute or a secondary source, cited in a consistent format. In the UK that is usually OSCOLA, the Oxford University Standard for Citation of Legal Authorities. Its fifth edition, published by the Oxford Faculty of Law in March 2026, now includes guidance on citing output from generative AI.¹

**Structure that can hide weak thinking.** Most law students are taught some version of IRAC (issue, rule, application, conclusion). It makes an answer easy to follow. It does not make it right. A textbook-perfect IRAC structure can contain very thin analysis.

The QAA's Subject Benchmark Statement for Law, revised in March 2023, describes what a law graduate should be able to do, including applying knowledge to complex situations and making critical judgements about legal argument.² Those are exactly the criteria that are hardest to mark consistently at scale.

## What does AI grading software actually do in a law school workflow?

Good AI grading software does not replace the marking process you already have. It adds a first pass to it. With Eduface, the workflow looks like this:

[FLOWDIAGRAM] Module leader (uploads brief, rubric, feedback instructions) → Student (submits through Moodle, Canvas, Blackboard or Brightspace) → Eduface (scores each criterion with reasoning, annotates the script) → Marker (reviews, edits, approves) → Gradebook (approved mark returned via LTI)
*The draft mark is held until a marker approves it. Nothing reaches the student before that.*

Setting up a law module takes three things from the module leader: the assignment brief, the rubric, and instructions for how feedback should be written for this assignment. If the module has no formal rubric, Eduface generates one from the brief for the module leader to edit.

From there, every submission that arrives through the LMS is annotated in the text itself, scored per rubric criterion, and given a written explanation for each score. The marker opens the script, reads the reasoning, changes whatever they disagree with, and approves. Only then does the grade pass back to the gradebook through LTI 1.3. Students do not need a separate login.

Two review modes matter for law schools in particular:

**Blind mode.** The marker marks the script first without seeing the AI's suggestion. Only after they finish does Eduface reveal its draft for comparison. This protects against anchoring, which is the main worry an exam board will raise.

**AI-visible mode.** The marker sees the draft from the start and edits it. Faster, and suited to formative work or experienced markers.

The institution can make one mode mandatory. Many law schools will want blind mode for summative assessment in the first year of use.

> **For programme leads and exam boards**
> A grader comparison dashboard shows at a glance when one marker drifts from the rest of the team or from the AI draft, without you having to pull individual scripts. That turns second-marking from a random sample into a targeted one.

## What should you require from AI grading software for a law school?

Not every tool that claims to grade essays is built for law. These are the five requirements we would put in any tender or pilot plan.

| Requirement | Why it matters in law | What to ask the vendor |
|---|---|---|
| **A model trained for the discipline** | General models reward fluent prose. Legal markers reward correct application of authority. | Which model scores the work, and what was it trained on? |
| **Criterion-level reasoning** | A single overall mark cannot be moderated or defended at appeal. | Can every score be traced to a criterion and a written reason? |
| **Enforced lecturer approval** | Under the EU AI Act, AI that evaluates learning outcomes is high-risk and requires effective human oversight. | Is approval structurally required before release, or optional? |
| **Consistency across markers** | Law schools are judged by external examiners on consistency. | How do you show drift between markers? What is your run-to-run variance? |
| **Data and procurement** | Student scripts are personal data under UK GDPR. | Where is data processed? Is there a DPA? Are you on Jisc/CHEST or HEAnet? |

Eduface is built around those five. The Paper Grader runs on one of six discipline models, and Law is one of them, so a law module is scored by a model trained on the conventions of legal writing rather than a general-purpose assistant. Every score comes with its reasoning. Lecturer approval cannot be switched off. Eduface runs its own model on its own GPU infrastructure in the Netherlands, uses no third-party AI APIs such as OpenAI, signs a Data Processing Agreement with each institution, and is an approved supplier on the Jisc/CHEST framework in the UK and the HEAnet framework in Ireland.

## What did our test on a real law essay show?

The question that matters to a law school is simple: how close does the AI get to what an experienced law lecturer would give? We tested that directly.

As part of our guide to AI grading tools, two students in the Netherlands, unaffiliated with and unpaid by any vendor, ran eight tools against papers that already had a lecturer's grade, written feedback and the official rubric. One of those papers was a Dutch-language constitutional law essay. The lecturer had graded it 4.4 on the Dutch 1-10 scale, a fail. Every tool received the same input: the full paper plus the full rubric.

[FIGUUR: Grade returned for a constitutional law essay graded 4.4 by the lecturer]
- Horizontal bar chart, one bar per tool, a vertical reference line at 4.4 labelled "Lecturer grade"
- CoGrader 10.0 · Claude 7.2 · ChatGPT 7.1 · Gemini 6.8 · Eduface 5.5
- Bars in navy, the reference line in green

*Figure 1: Grades returned by five tools for the same constitutional law essay. The lecturer graded it 4.4. Source: Eduface independent student test, July 2026.*

| Tool | Grade returned | Gap to lecturer (4.4) | What it did with the paper's weaknesses |
|---|---|---|---|
| CoGrader | 10.0 | +5.6 | Awarded maximum marks on every criterion |
| Claude | 7.2 | +2.8 | Spotted the missing bridging sentence and the unanswered research question, then still graded it 7.2 |
| ChatGPT | 7.1 | +2.7 | Fluent feedback, but graded the writing rather than the reasoning |
| Gemini | 6.8 | +2.4 | Occasional sharp observations, but inconsistent between runs |
| Eduface | 5.5 | +1.1 | Caught the typos, the weak link between sources and argument, the missing bridging sentence and the non-committal conclusion |

Two things stand out for a law school.

The first is the direction of the error. Every general tool marked a failing legal essay as a comfortable pass. The paper was well written in places. It restated its research question six times, cited sources without applying them to the legal criteria, and ended without a legal determination. A human law marker sees that immediately. A general model responds to the writing.

The second is that Claude saw most of the problems and still over-marked. Its individual observations were right. Its judgement of what those problems cost in a law grade was not. A structural weakness that costs 0.3 points in a general model's weighting can cost two full points with a university assessor. That is the difference between an AI that can read and an AI calibrated for assessment.

There is a related finding from the United States. In 2023, four professors at the University of Minnesota Law School had ChatGPT sit four of their real exams and graded the answers blind alongside student scripts. It averaged a C+: a low pass in every course.³ The same fluent, mediocre legal prose that earns a C+ as a student is what a general model tends to reward when it marks.

> **Limitations**
> One law paper in one language is a small sample. Read these results as directional, not as a ranking. The point for a law school is not the exact numbers. It is that you should test any tool on your own graded scripts before trusting it with a cohort.

## Where does AI grading help in law, and where does the lecturer stay essential?

AI grading is most useful where law marking is repetitive and criterion-driven, and least useful where it depends on professional judgement about contested law. A sensible split looks like this:

| AI draft is strong at | The lecturer stays essential for |
|---|---|
| Checking whether each issue in the facts has been identified | Judging whether a novel argument is persuasive |
| Checking that a rule is stated and supported by authority | Deciding whether a contested application deserves full credit |
| Flagging application that restates the rule without engaging with the facts | Weighing policy arguments and law reform points |
| Flagging a conclusion that does not answer the question asked | Borderline and fail decisions |
| Annotating the text so feedback points to the exact passage | Academic misconduct concerns |
| Applying the same standard to script 1 and script 280 | The final mark |

For a deeper look at the structure-versus-substance problem, see our article on [where AI grading helps with law essays and where it doesn't](/resources/blog/ai-grading-law-essays).

## Which law school assessments can AI grading software handle?

A law school assesses in more formats than the essay. Here is how each maps onto Eduface.

| Assessment | What the AI does | Eduface module | Status |
|---|---|---|---|
| Problem questions (coursework) | Scores issue spotting, rule, application and conclusion per criterion, with annotations | Paper Grader | Live |
| Essays and research papers | Scores argument, use of authority, structure and critical analysis against the rubric | Paper Grader | Live |
| Open-answer exam scripts | Three independent AI agents score each answer against the mark scheme; a fourth compares them and flags disagreement for the lecturer | Exam Grader | Live |
| Dissertation vivas and moots | An AI examiner holds a structured spoken conversation and evaluates it against the rubric | Oral Examination | Early access |
| Authenticity checks on written work | The student answers critical questions about their own paper, as in a thesis defence | Academic Integrity | Beta |

The Exam Grader deserves a note for law exams. Open-answer scripts are where marker inconsistency is worst. Three agents score each answer without seeing each other's results, and a fourth reconciles them. Strong agreement is shown as high confidence. Divergence is flagged for the lecturer to look at first. In practice, Eduface has measured this as 48% more consistent than unaided human marking, with under four minutes from upload to suggested grade.

For the oral side, a law school can configure the examiner as a strict dissertation examiner or an opposing counsel. Because the conversation adapts to each answer, it is hard to prepare for with generic AI-written responses. That makes it useful both for assessment and for checking that a submitted essay is the student's own work.

## How do you set up AI grading for a law module?

Most of the work is in the rubric, not the software. A pilot on one module typically looks like this:

**1. Choose one module and one assignment.** A second-year problem question works well: clear criteria, a large cohort, and marks you already have from last year.

**2. Write the rubric as if a new marker had to use it.** Spell out what separates a 2:1 application from a first-class application. "Application: 30%" produces inconsistent output from humans and AI alike.

**3. Add feedback instructions.** Tell the model how you want feedback phrased. Law teaching often suits the Reflective and Socratic feedback style, which asks the student questions rather than giving answers. We compare feedback tools for law in detail in [the best AI feedback tool for law essays](/resources/blog/best-ai-feedback-tool-law-essays). The other styles are Constructive and Direct, Went Well and Needs Improvement, and Supportive and Encouraging.

**4. Select the Law model.** This is the discipline model the Paper Grader uses to score the work.

**5. Calibrate on scripts you have already marked.** Run five to ten of last year's scripts through Eduface and compare the draft with the agreed final mark. Adjust the rubric wording where the draft and the mark disagree.

**6. Run the live cohort in blind mode.** Markers mark first, then compare. After one cycle you will know where the AI helps and where your team wants to rely on it.

The LMS connection itself is done once by a learning technologist through LTI 1.3, typically in an afternoon. See our guides for [Moodle](/resources/blog/ai-essay-grader-moodle-lti) and [Canvas](/resources/blog/ai-essay-grader-canvas-lms-lti).

## How accurate is AI grading once it is calibrated?

Two measurements from UK pilots are useful, and they measure different things.

**How much markers changed the draft.** In UK pilots, lecturers changed an average of 5% of each final grade. The AI draft sat within the range a professional reviewer would accept most of the time.

**How close the draft came to the marker's grade.** In a pilot at one UK university covering 435 submissions, six modules and 13 markers, the AI's suggested grade came within 94% of the marker's grade on average. For markers who had spent time tuning the model to their own standards, that rose to 98%. Accuracy here means how small the gap is between the suggestion and the marker's grade, not how often they matched exactly. Reviewing each submission took two to three minutes.

The 98% is the more important number. It shows that the lecturer steers the model. The more precisely a law school defines what it rewards, the closer the draft gets.

[FIGUUR: Where marking time goes, before and after]
- Two stacked horizontal bars, "Unaided marking" and "With an AI first pass"
- Segments: reading and annotating · scoring per criterion · writing feedback · moderation
- With the AI first pass, the reading and annotating and feedback-writing segments shrink; a new "review and approve, 2-3 min" segment appears; moderation becomes targeted
- Label as illustrative, no numbers on the axis

*Figure 2: Illustration of where an AI first pass changes the marking workload. The marker still reads and approves every script.*

## What about the EU AI Act, GDPR and procurement?

Three rules shape how a law school can use AI grading.

**The EU AI Act.** AI systems intended to evaluate learning outcomes are classified as high-risk under Annex III, point 3(b), of Regulation (EU) 2024/1689. High-risk does not mean prohibited. It means effective human oversight, transparency about how outputs are produced, and documentation. After the Digital Omnibus on AI, which entered into force on 27 July 2026, the obligations for these Annex III systems apply from 2 December 2027.⁴ Law schools in the EU, and UK schools buying from EU providers, should design their workflow for it now. Eduface requires lecturer approval for every grade and keeps a full audit trail per criterion.

**UK GDPR.** A law script is personal data about an identifiable student's performance. The institution is the controller and the tool is a processor. You need a Data Processing Agreement, processing in the UK or EU or under a proper transfer mechanism, and a guarantee that scripts are not used to train anyone else's model. Eduface does not send student work to external AI providers and never uses it to train external models.

**Procurement.** Eduface is an approved supplier on Jisc/CHEST (UK) and HEAnet (Ireland), so a law school can buy through an existing framework instead of running its own tender. See our guides to [buying through Jisc/CHEST](/resources/blog/jisc-chest-ai-assessment-procurement) and [the HEAnet framework](/resources/blog/heanet-framework-ai-assessment-procurement).

> **What to check before you sign**
> Run three of your own marked scripts through the tool. Compare the draft to your agreed mark, not to how convincing the feedback sounds. Ask where the data is processed, whether a DPA is standard, and whether lecturer approval can be switched off. If it can, walk away.

If your students are asking whether they can check their own essays with AI, point them to [AI essay graders for law students](/resources/blog/ai-essay-grader-law-students).

## Frequently asked questions

**Can AI grading software mark law problem questions accurately?**
Yes, as a first pass, if it is trained for legal writing and calibrated to your rubric. It is strong at checking whether each issue is identified, whether rules are supported by authority and whether the conclusion answers the question. The judgement on contested application stays with the lecturer, who approves every mark before release.

**Does AI grading software check OSCOLA citations?**
It can flag authority that is missing or not applied to the facts, which is where most marks are lost. Line-by-line OSCOLA formatting is better checked with your library's referencing guidance. Note that OSCOLA's fifth edition, published in March 2026, now covers how to cite output from generative AI.

**Will external examiners accept AI-assisted marking?**
External examiners review the marks your markers approve, not the AI's draft. What they will want to see is that every mark was reviewed by a qualified marker, that marking is consistent, and that there is an audit trail. Blind mode and a full audit trail per criterion make that easy to show.

**Is AI grading allowed under the EU AI Act?**
Yes. The EU AI Act classifies AI that evaluates learning outcomes as high-risk, which means it must operate under effective human oversight with transparent outputs and documentation. It does not ban it. For Annex III systems, those obligations apply from 2 December 2027. A workflow where a lecturer approves every grade is built for that requirement.

**How much does AI grading software cost for a law school?**
Individual lecturers can start with Eduface for free, with about 20 assignments a month, or use the Lecturer plan at $25 a month for about 200. For a whole law school, Eduface offers institutional licences through Jisc/CHEST in the UK and HEAnet in Ireland.

**Can students tell that AI was involved in marking?**
They should be told. Institutions using AI in assessment should say so in the module handbook or assessment brief, explain what role it plays, and confirm that a qualified marker reviewed and approved every mark. Eduface labels feedback as "Lecturer + AI" so students can see it was reviewed.

## References

1. Goudkamp, J. (ed.). (2026). *OSCOLA: The Oxford University Standard for Citation of Legal Authorities* (5th ed.). Oxford Faculty of Law and Hart Publishing. [Published 25 March 2026; includes guidance on citing output from generative AI.]
2. Quality Assurance Agency for Higher Education. (2023). *Subject Benchmark Statement: Law*. QAA. [Revised statement published March 2023.]
3. Choi, J. H., Hickman, K. E., Monahan, A., & Schwarcz, D. (2023). ChatGPT goes to law school. *Journal of Legal Education*, 71(3). [Across 95 multiple-choice and 12 essay questions on four real exams, ChatGPT averaged a C+.]
4. European Parliament and Council of the EU. (2024). Regulation (EU) 2024/1689 (Artificial Intelligence Act), Annex III, point 3(b); as amended by the Digital Omnibus on AI (in force 27 July 2026). [High-risk obligations for Annex III systems apply from 2 December 2027.]
5. Eduface. (2026). *The Complete Guide to AI Grading Tools for Higher Education*. [Independent student test of eight tools on six papers with known lecturer grades.]
