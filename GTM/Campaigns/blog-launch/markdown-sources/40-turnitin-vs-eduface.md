---
title: "Turnitin vs Eduface: Similarity Checking, Feedback and AI Grading Compared (2026)"
seo_title: "Turnitin vs Eduface: What Each Does (2026) | Eduface"
meta_description: "Turnitin checks where text came from. Eduface drafts rubric-based grades for lecturers to approve. What each does, where they overlap, and how to use both."
slug: turnitin-vs-eduface
primary_query: "Turnitin vs Eduface"
secondary_queries: ["Turnitin alternative for grading", "Turnitin Feedback Studio AI grading", "Turnitin Clarity vs AI grader", "does Turnitin grade essays", "Turnitin AI detection false positives UK"]
type: koopgids
category: Product
hub: /resources/blog/ai-grading-tools-higher-education-guide
related: [/resources/blog/ai-paper-grader-vs-plagiarism-checker, /resources/blog/gradescope-review-2026-higher-education, /resources/blog/ai-plagiarism-detection-failing-higher-education]
review_by: 2027-01-15
status: concept
---

EYEBROW: COMPARISON · 2026

# Turnitin vs Eduface: Similarity Checking, Feedback and AI Grading Compared (2026)

*Turnitin tells you where a piece of writing came from and gives lecturers tools to mark it. Eduface reads the work against your rubric, drafts a criterion-level grade and feedback, and waits for the lecturer to approve. They answer different questions, which is why many institutions end up asking whether they need one, the other or both.*

By Eduface · September 2026 · 17 min read · Written for learning technologists, academic integrity leads and heads of assessment

Almost every UK university already pays for Turnitin. So when a department asks for an AI grading tool, the first question from IT, procurement or the academic integrity office is predictable: doesn't Turnitin already do that? Sometimes the answer is yes. Often it is no. And the confusion costs months, because the two products are bought for different reasons, by different people, and judged against different criteria.

> **What is the difference between Turnitin and Eduface?**
> Turnitin is an academic integrity platform: it compares submissions against a large database of existing text to produce a similarity report, offers AI writing detection, and gives lecturers tools such as QuickMarks and rubrics to mark by hand. Eduface is an AI assessment platform: it reads each submission against the lecturer's rubric, drafts a score and written feedback for every criterion, and holds that draft until the lecturer approves it. Turnitin answers "where did this text come from?". Eduface answers "how good is this work against our criteria?".

We are Eduface, so we have a position here. We have tried to be accurate about Turnitin and to describe its products the way Turnitin itself does. Where Turnitin is the better tool for a job, we say so. Turnitin's product line changes often, so check the current state with Turnitin before you decide; everything below reflects public information as of September 2026.

## What does Turnitin actually do?

Turnitin is a family of products, not one tool. The names matter, because "we have Turnitin" can mean very different things depending on the licence.

| Turnitin product | What it is for | Who uses it |
|---|---|---|
| **Similarity / Originality** | Matches submitted text against internet content, published periodicals and journals, and a repository of previously submitted student papers; Originality adds AI writing detection | Academic integrity, every lecturer who receives a similarity report |
| **Feedback Studio** | Marking and feedback on coursework: QuickMarks (reusable comments), rubrics and grading forms, voice comments, PeerMark for peer review | Lecturers marking by hand |
| **Turnitin Clarity** | A student writing workspace, announced in March 2025, where students compose their work; instructors can switch on AI-generated writing feedback and see the writing process | Courses that want visibility of how work was written |
| **Gradescope** | Grading platform for structured exams, problem sets and handwritten work, with answer grouping | STEM departments |
| **iThenticate** | Similarity checking for research and publication | Researchers, journals, doctoral schools |

*Table 1: Turnitin's main products for higher education, as Turnitin describes them. Source: Turnitin product pages and March 2025 announcement.¹*

**The similarity report** is what most people mean by "Turnitin". It shows the percentage of a submission that matches existing sources and highlights the matching passages. Turnitin is explicit that the similarity score is not a plagiarism verdict. A lecturer still has to decide whether a match is properly quoted, common phrasing, or copying.

**Feedback Studio** is where marking happens for many UK institutions. It is a set of tools that make human marking faster and more consistent: a library of reusable comments, rubrics attached to the assignment, voice comments and peer review. The lecturer does the reading and the judging.

**Turnitin Clarity** is the newest piece and the one most often confused with AI grading. Turnitin launched it as a paid add-on to Feedback Studio. Students write inside a Turnitin workspace, instructors choose whether AI can give students writing feedback while they compose, and instructors can see how the work was produced. Turnitin's chief product officer described the aim at launch: "Students will need to use AI in their future careers. With Turnitin Clarity, educators can begin to understand how students use it."¹

For Gradescope specifically, see our separate [Gradescope review](/resources/blog/gradescope-review-2026-higher-education).

## What does Eduface do?

Eduface is built for one job: getting a consistent, rubric-grounded first reading of every submission in front of the lecturer, so the lecturer can approve or change it rather than start from a blank page.

| Eduface module | What it does | Status |
|---|---|---|
| **Paper Grader** | Reads each essay or report against the rubric, annotates the text, scores every criterion with written reasoning, and gives formative feedback on drafts | Live |
| **Exam Grader** | Three independent AI agents score each open exam answer; a fourth reconciles them and flags disagreement for the lecturer | Live |
| **Oral Examination** | An AI examiner holds a structured spoken conversation with the student and evaluates it against the rubric | Early access |
| **Academic Integrity** | The student answers critical questions about their own submitted paper, as in a thesis defence | Beta |

*Table 2: Eduface's modules.*

Three things define how Eduface works:

**The rubric is the standard.** The lecturer sets up an assignment with the brief, the rubric and instructions for how feedback should be written. If there is no rubric, Eduface generates one from the brief for the lecturer to edit. Every score traces back to a criterion.

**Discipline models, not a general assistant.** The Paper Grader runs on one of six models (Law, Economics, Social Sciences, STEM, Humanities and Health Sciences), each trained on the conventions of its field. Eduface runs its own model on its own GPU infrastructure in the Netherlands and does not send student work to third-party AI providers such as OpenAI.

**The lecturer approves everything.** No grade reaches a student until a lecturer has approved it. In blind mode, the lecturer marks first and only then sees the AI draft. In AI-visible mode, the draft is shown from the start. Reviewed feedback carries a "Lecturer + AI" label.

[FLOWDIAGRAM] Student submits through the LMS → Turnitin: similarity report and AI writing indicator (integrity question) · Eduface: criterion scores, annotations and feedback draft (quality question) → Lecturer reviews both → Lecturer approves the grade → Gradebook
*The same submission can go through both tools. They answer different questions, and the lecturer makes both decisions.*

## Does Turnitin grade essays?

Not in the sense of drafting a grade for the lecturer. Feedback Studio's tools help a lecturer mark faster: the lecturer reads the essay, applies QuickMarks, fills in the rubric and writes the summary comment. Turnitin Clarity adds AI-generated feedback to students while they write, if the instructor switches it on. As Turnitin describes these products publicly, neither reads a finished submission against your rubric and proposes a criterion-by-criterion grade with reasoning for you to approve. That is the specific gap AI grading tools fill.

This is not a criticism of Turnitin. It is a different product category. A plagiarism checker and an AI grader answer different questions, and treating them as substitutes causes more procurement confusion than any other single mistake we see. We wrote about this in more depth in [AI paper grader vs plagiarism checker](/resources/blog/ai-paper-grader-vs-plagiarism-checker).

## Where do Turnitin and Eduface compare directly?

Here is the side-by-side on the questions institutions actually ask.

| Question | Turnitin | Eduface |
|---|---|---|
| Checks text against existing sources | **Yes**, core product, very large database | No |
| Detects AI-generated writing | Yes (Originality), with an AI writing indicator | No; verifies authorship through oral follow-up instead (Academic Integrity, beta) |
| Drafts a grade per rubric criterion for lecturer approval | Not as described in Turnitin's public product information | **Yes**, core product |
| Written feedback per criterion, anchored to passages | Lecturer writes it, helped by QuickMarks | AI drafts it; lecturer edits and approves |
| Feedback on drafts before submission | Clarity (paid add-on): AI writing feedback during composition, if enabled | Paper Grader: feedback on first draft, second draft and final, tracking progress between drafts |
| Discipline-specific models | Not described | Six discipline models |
| Consistency across many markers | Shared rubrics and comment banks | Same criterion-level first reading for every script, plus a grader comparison dashboard |
| Oral assessment | No | Oral Examination (early access) |
| Handwritten maths and structured exams | Gradescope | No handwritten scripts; Exam Grader for typed open answers |
| LMS integration | Moodle, Canvas, Blackboard, Brightspace | Moodle, Canvas, Blackboard, Brightspace via LTI 1.3 |
| Where AI processing happens | Ask Turnitin for your contract's processing locations | Eduface's own GPU infrastructure in the Netherlands, no third-party AI APIs |
| Public pricing | No; quoted per institution | Free to start for lecturers; Lecturer plan $25/month; institutional licences via Jisc/CHEST and HEAnet |

*Table 3: Turnitin and Eduface compared on the questions institutions ask most. Turnitin information as described in its public materials, September 2026.*

[FIGUUR: Two questions, two tools]
- A single student essay in the centre
- Left arrow labelled "Where did this text come from?" pointing to a panel: "Similarity report · AI writing indicator · Turnitin"
- Right arrow labelled "How good is it against our criteria?" pointing to a panel: "Criterion scores · reasoning · feedback · Eduface"
- Beneath both panels: "Lecturer decides"
- Navy for Turnitin panel outline, green for Eduface panel outline

*Figure 1: The two questions every submission raises, and which tool answers which.*

## What about AI writing detection?

This is where many UK institutions are most uncertain, so it is worth being precise about what Turnitin says and what others have found.

**What Turnitin claims.** Turnitin reports that its AI writing detection has a document-level false positive rate below 1% for documents where 20% or more of the text is flagged as AI-written, and has said that the false positive rate at the level of individual sentences is around 4%.² Turnitin's own guidance is that the AI writing score should not be used as the sole basis for action against a student; it is one piece of information alongside the assignment's policy, the student's drafting history and a conversation with the student.

**What institutions have done.** In April 2023, before the feature launched, the University of Cambridge was among institutions reported to be opting out of Turnitin's new AI detection service.³ Several universities outside the UK have since switched AI detection off. In July 2026, HEPI published an analysis of AI detection and international students, noting that UK universities have not followed those international peers in disabling it.⁴

**Why it matters for grading.** Detection and grading are separate decisions. A student can write an entirely original essay that is weak, or a strong essay that a detector flags. Neither result tells the lecturer what the work deserves against the rubric. For more on why detection struggles as evidence, see [why AI plagiarism detection is failing higher education](/resources/blog/ai-plagiarism-detection-failing-higher-education).

**Eduface's approach is verification rather than detection.** Instead of estimating whether text was machine-generated, Eduface's Academic Integrity tool (in beta) asks the student critical questions about their own submission, as in a thesis defence. A student who wrote the essay can usually explain it. A student who did not, usually cannot. The result is a transcript a member of staff can read and explain, rather than a probability score.

> **Before you rely on any AI detection score**
> Ask the vendor for the false positive rate on writing like your students' (including students writing in a second language), whether the score can be explained to a misconduct panel, and what the vendor itself says the score should and should not be used for. Then decide what else you need, such as drafts, an oral follow-up or a conversation, before any case goes forward.

## Do you need both Turnitin and Eduface?

For most UK universities, the honest answer is: keep Turnitin for similarity checking, and add Eduface where marking load, feedback quality or marker consistency is the problem.

**Keep Turnitin if** you rely on similarity reports in your academic integrity process. Eduface does not check text against external sources and does not try to. Turnitin's database and its place in institutional integrity policy are hard to replace, and there is no reason to.

**Add Eduface if** your problem is one of these:
- Marking takes too long for the turnaround you promise students.
- Feedback is thin or inconsistent between markers or seminar groups.
- Students get little or no feedback on drafts.
- External examiners or exam boards question consistency across markers.
- You want oral verification of authorship at a scale human vivas cannot reach.

**Use both on the same assignment.** Both connect to the same LMS through LTI. A submission can produce a Turnitin similarity report for the integrity question and an Eduface criterion-level draft for the quality question. The lecturer sees both and makes both decisions.

| Your main problem | Best fit |
|---|---|
| "We need to know if work is copied from existing sources" | **Turnitin** Similarity |
| "We want to see how students wrote their work, and give AI writing help during composition" | **Turnitin** Clarity |
| "We need to mark 400 essays consistently and on time, with detailed feedback" | **Eduface** Paper Grader |
| "Students need feedback on drafts, and we have no time to give it" | **Eduface** Paper Grader, formative feedback |
| "Our markers disagree too much" | **Eduface**, grader comparison dashboard and blind mode |
| "We need to verify authorship without relying on a detector" | **Eduface** Academic Integrity or Oral Examination |
| "We mark handwritten STEM exams" | **Gradescope** (Turnitin) |

*Table 4: Which tool fits which problem.*

## What does a combined Turnitin and Eduface workflow look like?

Here is how one assignment on a 300-student module runs when both tools are in place. Nothing in the student's experience changes: they submit once, through the LMS.

| Stage | What happens | Tool | Who acts |
|---|---|---|---|
| **Before the assignment opens** | Module leader sets up the brief, rubric and feedback instructions; chooses the discipline model | Eduface | Module leader |
| | Similarity settings and repository options are applied as usual | Turnitin | Learning technologist |
| **Drafts (optional)** | Students submit a first draft and receive criterion-level formative feedback; a second draft gets feedback that refers to their progress | Eduface | Students, with lecturer oversight |
| **Final submission** | Student submits once through the LMS | LMS | Student |
| **Integrity check** | Similarity report generated; any high matches reviewed | Turnitin | Marker or integrity lead |
| **Marking** | AI draft of criterion scores, annotations and feedback for every script; marker reviews in blind or AI-visible mode, edits and approves | Eduface | Marker |
| **Moderation** | Grader comparison dashboard shows marker drift; moderator samples the largest disagreements | Eduface | Moderator |
| **Concerns about authorship** | Where the similarity report or the marker raises a concern, an oral follow-up about the student's own submission | Eduface Academic Integrity (beta) | Lecturer decides |
| **Release** | Approved marks and feedback pass back to the gradebook | LMS via LTI | Automatic after approval |

*Table 5: One assignment, both tools. Illustrative; adapt to your policies.*

Two practical points make this work. First, decide in advance which tool's output goes into which process: similarity into the integrity process, criterion scores into marking and moderation. Mixing them, for example by lowering a mark because of a similarity score, confuses two decisions that policy usually keeps apart. Second, tell students what each tool does. "Your work is checked for similarity by Turnitin, and a lecturer marks it with AI assistance and approves every mark" is a sentence that belongs in every module handbook that uses both.

For how moderation changes when every script has an AI reading, see [AI in moderation and second marking](/resources/blog/ai-moderation-second-marking-external-examiners).

## What should you ask before your next Turnitin renewal?

Renewal is a good moment to check whether each part of your licence still does the job you are paying for.

**Ask your academic integrity lead:**
- How often are similarity reports actually used in misconduct cases, and how often do they decide one?
- What is our policy on the AI writing indicator, and does it match Turnitin's own guidance that it should not be the sole basis for action?
- Do we need Clarity's view of the writing process, or would an oral follow-up give stronger evidence?

**Ask your markers:**
- How long does marking an essay in Feedback Studio take, from opening the script to approving the mark?
- How much of that time is reading and scoring, and how much is writing feedback?
- Where do marker disagreements show up, and how are they found?

**Ask your students (or your NSS and module evaluation data):**
- Is feedback timely, specific and consistent across markers?

If the integrity answers are strong and the marking answers are not, the case is not to replace Turnitin. It is to add a marking tool alongside it. See [how much AI grading actually saves](/resources/blog/cost-per-assignment-ai-grading-savings) for a way to put numbers on the marking side.

## How accurate is Eduface's grading?

Turnitin's accuracy question is about detection. Eduface's accuracy question is about how close the draft grade is to what an experienced lecturer would give.

**In UK pilots**, lecturers changed an average of 5% of each final grade the AI drafted.

**In a pilot at one UK university** covering 435 submissions, six modules and 13 markers, the AI's suggested grade came within 94% of the marker's grade on average, and within 98% for markers who had tuned the model to their standards. Accuracy here means how small the gap is between the suggestion and the marker's grade. Review took two to three minutes per submission.

**In an independent student test** of eight grading tools on papers with known lecturer grades, Eduface averaged ±0.15 deviation from the lecturer's grade across five psychology papers, against ±0.7 to ±1.2 for general AI assistants.⁵

[FIGUUR: Where marking time goes with Turnitin alone, and with Turnitin plus Eduface]
- Two horizontal stacked bars per script
- "Turnitin Feedback Studio": check similarity report · read the script · apply QuickMarks · fill in rubric · write summary feedback
- "Turnitin + Eduface": check similarity report · review Eduface draft (criterion scores, annotations, feedback) · edit · approve
- Label as illustrative, no time axis values

*Figure 2: How the lecturer's work per script changes when an AI draft is added. Illustrative.*

## What about data protection and procurement?

**Data.** Both tools process personal data on behalf of the institution. For Turnitin, ask for the processing locations and repository settings that apply to your contract, including whether submissions are added to Turnitin's repository of student papers or checked without being stored. For Eduface, processing runs on Eduface's own GPU infrastructure in the Netherlands, student work is never used to train external models, and Eduface signs a Data Processing Agreement with each institution.

**Regulation.** AI that evaluates learning outcomes is high-risk under Annex III, point 3(b), of the EU AI Act. Following the Digital Omnibus on AI, the obligations for those systems apply from 2 December 2027.⁶ AI grading falls squarely in that category, which is why Eduface requires lecturer approval for every grade and keeps a full audit trail.

**Procurement.** Eduface is an approved supplier on the Jisc/CHEST framework in the UK and the HEAnet framework in Ireland. See [how to buy through Jisc/CHEST](/resources/blog/jisc-chest-ai-assessment-procurement).

## Frequently asked questions

**Is Eduface a Turnitin alternative?**
For grading and feedback, yes. For similarity checking, no. Eduface drafts rubric-based grades and feedback for lecturers to approve, which Turnitin's marking tools leave to the lecturer. Eduface does not check submissions against external sources, so most institutions keep Turnitin for that and add Eduface for marking.

**Does Turnitin use AI to grade essays?**
As Turnitin describes its products publicly, Feedback Studio provides tools that help lecturers mark by hand, and Turnitin Clarity offers AI writing feedback to students while they compose, if the instructor enables it. We have not seen Turnitin describe a feature that drafts a criterion-by-criterion grade on a final submission for lecturer approval. Check the current product with Turnitin, as it changes often.

**Can Turnitin and Eduface run on the same assignment?**
Yes. Both connect to Moodle, Canvas, Blackboard and Brightspace. The same submission can produce a Turnitin similarity report and an Eduface grading draft. The lecturer reviews both.

**Is Turnitin's AI detection reliable enough for misconduct cases?**
Turnitin reports a document-level false positive rate below 1% for documents with 20% or more flagged text, and around 4% at sentence level, and advises that the score should not be the sole basis for action. Many institutions treat it as a prompt for a conversation rather than as evidence. Oral verification produces evidence a panel can examine.

**Is Eduface cheaper than Turnitin?**
They are priced for different jobs, and Turnitin does not publish its prices. Eduface is free to start for individual lecturers (about 20 assignments a month) and $25 a month for the Lecturer plan (about 200). Institutions license Eduface through Jisc/CHEST or HEAnet.

**Does Eduface detect AI-written work?**
No. Eduface verifies authorship instead of estimating it. Its Academic Integrity tool, in beta, asks students critical questions about their own submission, and its Oral Examination tool can run a structured viva. A lecturer reviews the transcript and decides.

## References

1. Turnitin. (2025, 4 March). *Turnitin launches Turnitin Clarity, bringing transparency and integrity insights to education* [Press release]. [Paid add-on to Feedback Studio; student composition workspace; instructor-controlled AI writing feedback; quote from Turnitin's chief product officer.]
2. Turnitin. *Understanding the false positive rate for sentences of our AI writing detection capability*; and Turnitin AI writing report guidance. [Document-level false positive rate below 1% for documents with at least 20% AI writing; sentence-level rate around 4%; score not to be used as the sole basis for adverse action.]
3. Techzine. (2023, 4 April). *Universities doubtful about Turnitin's new AI detection tool*. [Cambridge among institutions reported as opting out.]
4. Higher Education Policy Institute. (2026, 20 July). *Catching the wrong students: AI detection, international students and the fairness crisis in UK universities*. [UK universities have not followed international peers that disabled AI detection.]
5. Eduface. (2026). *The Complete Guide to AI Grading Tools for Higher Education*. [Independent student test of eight tools on six papers with known lecturer grades.]
6. European Parliament and Council of the EU. (2024). Regulation (EU) 2024/1689 (Artificial Intelligence Act), Annex III, point 3(b); as amended by the Digital Omnibus on AI (in force 27 July 2026). [High-risk obligations for Annex III systems apply from 2 December 2027.]
