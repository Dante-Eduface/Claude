---
title: "AI Oral Examinations in Higher Education: The Complete Guide (2026)"
seo_title: "AI Oral Exams in Higher Education: 2026 Guide | Eduface"
meta_description: "AI-conducted oral exams in higher education: how they work, what the evidence says about vivas, fairness, the EU AI Act, and how to run one in your LMS."
slug: ai-oral-examinations-higher-education-guide
primary_query: "AI oral examinations higher education"
secondary_queries: ["AI viva", "AI oral exam", "oral assessment AI proof", "interactive oral assessment", "verify authorship oral exam", "AI conducted viva"]
type: koopgids
category: Product
hub: /resources/blog/ai-oral-examinations-higher-education-guide
related: [/resources/blog/ai-oral-exams-moodle-verify-authorship, /resources/blog/are-oral-exams-ai-proof-canvas, /resources/blog/ai-oral-examiner-styles-brightspace, /resources/blog/beyond-ai-detection-oral-verification-blackboard, /resources/blog/ai-proof-oral-exam-practice-moodle]
review_by: 2027-01-15
status: concept
note: "Hub voor het oral-cluster. De vier LMS-spokes linken hiernaar terug (bij het bouwen toevoegen)."
---

EYEBROW: ORAL ASSESSMENT · 2026 GUIDE

# AI Oral Examinations in Higher Education: The Complete Guide (2026)

*Oral examination is back on the agenda because a written submission no longer proves that a student can do the work. The problem has always been scale. This guide covers how AI-conducted oral exams work, what the research on vivas says about making them reliable and fair, what the law requires, and how to run one in your LMS.*

By Eduface · September 2026 · 15 min read · Written for heads of assessment, module leaders, academic integrity leads and learning technologists

A module leader suspects that a strong essay was not written by the student who submitted it. The AI detector gives a probability score she cannot explain to a panel. The obvious test is to ask the student about the essay: why this argument, why these sources, what would change if one assumption were different. For one student, she can do that in ten minutes. For a cohort of 400, it would take around 67 hours of academic time before anyone books a room. So it does not happen, and the question stays open.

> **What is an AI oral examination?**
> An AI oral examination is a structured spoken assessment in which an AI examiner asks the student questions, often based on the student's own submitted work, adapts its follow-up questions to each answer, and then produces a transcript and a rubric-aligned evaluation. A lecturer reviews the transcript and evaluation and approves the result. It makes oral assessment possible at cohort scale, for three purposes: verifying authorship, assessing spoken reasoning, and letting students practise before a live viva.

## Why are oral exams coming back?

For decades, most UK universities used oral assessment sparingly outside the doctoral viva, languages and clinical subjects. Generative AI has changed the reason to use it.

The QAA's 2023 guidance on assessment in the ChatGPT era named oral examination as one response. It described "oral examinations in the form of structured interviews conducted by two or more examiners with clearly set out rubrics and appropriate safeguards for vulnerable students", used formatively or summatively, and "mini-vivas, in which small groups of students are interviewed together about their written submissions", which "can serve both to authenticate the work and contribute to its assessment" and act as "a powerful deterrent to students considering contract cheating".¹

The same guidance is candid about why orals fell out of use: many providers discontinued them "on the grounds that they are unreliable and unnecessarily stressful", and accessibility and inclusion (speech impairments, accents) have to be considered.¹ Any serious approach to AI oral assessment has to answer both points, not only the integrity case.

Universities are already experimenting. At the University of Sussex, a master's module in molecular research methods moved to 65% coursework and a 15-minute oral worth 35%, with a four-question structure, two markers per viva and a written alternative as a reasonable adjustment.² The University of Warwick's guidance, developed through an AI in mathematics project, recommends vivas for key assessments and capstone projects rather than everything, with trained examiners and "transparent and consistent grading rubrics", and warns that "without clear criteria and training, different examiners may assess students unevenly".³

## What does the research say about making vivas reliable?

The strongest evidence comes from health professions education, where structured and unstructured vivas have been compared directly. A 2023 systematic review and meta-analysis in *BMC Medical Education* found a clear difference:⁴

| Measure | Structured viva | Traditional (unstructured) viva |
|---|---|---|
| Internal consistency (Cronbach's alpha) | 0.80 and 0.75 in included studies | 0.50 |
| Reliability coefficients | 0.7 to 0.8 | 0.3 to 0.4 |
| Inter-rater reliability | r = 0.78 to 0.91 | Not reported as comparable |
| Correlation with structured written exams | r = 0.442, significant | r = 0.202, not significant |
| Learner acceptability (12 studies) | 79.8% overall | |

*Table 1: Structured vs traditional vivas. Source: Abuzied & Nabag, BMC Medical Education, 2023.*

[FIGUUR: Structure is what makes a viva reliable]
- Paired bar chart, "Reliability coefficient range"
- Structured viva: bar from 0.7 to 0.8, in green
- Traditional viva: bar from 0.3 to 0.4, in navy
- Annotation: "Same format, different design. Structure, not speaking, drives reliability."

*Figure 1: Reliability of structured and traditional vivas. Source: Abuzied & Nabag, 2023.*

The lesson for AI oral assessment is direct. Speaking is not what makes a viva fair or reliable. Structure is: consistent question design, clear criteria, and evaluation against a rubric. An AI examiner that runs every student through the same structure and evaluates against the same rubric addresses exactly the weakness that made orals unreliable. An AI examiner that improvises freely would repeat it.

## How does an AI oral exam work?

With Eduface's Oral Examination tool, currently in early access, an oral exam has four stages, with academic judgement at both ends.

[FLOWDIAGRAM] Lecturer configures the session (mode, rubric or question parameters, examiner character and style, linked submission) → Session published to the student through the LMS (LTI 1.3) → Student speaks answers in the browser; the AI asks follow-ups based on their work and their previous answer → Lecturer receives transcript and criterion-by-criterion evaluation → Lecturer reviews, changes what they disagree with, approves → Result and transcript sync to the gradebook
*The AI conducts the conversation. The lecturer decides the outcome.*

**1. Configure.** The lecturer chooses a mode, sets the rubric or question parameters, links the session to the student's submission where relevant, and sets the examiner's character and dialogue style.

**2. Publish.** The session reaches students through Moodle, Canvas, Blackboard or Brightspace via LTI 1.3. No separate login, no room booking, no scheduled slot.

**3. Converse.** The student opens the session and speaks their answers in the browser. A session typically runs 15 to 20 minutes and records automatically. Where the session is linked to a submission, the questions come from the student's own work: their argument, their sources, their method. The next question depends on the last answer, so there is no fixed question set to prepare against.

**4. Review and approve.** The lecturer receives the full transcript and a criterion-by-criterion evaluation with its reasoning, forms their own judgement, changes anything they disagree with and approves. Only then does the result sync back to the gradebook.

## What are the three modes, and when do you use each?

| Mode | Purpose | Typical use |
|---|---|---|
| **Integrity Check** | Confirm that the student can account for work they submitted | After a written submission, for a sample or for every student |
| **Oral Exam** | A complete oral assessment, graded against your rubric | Where spoken reasoning, clinical communication or professional judgement is the learning outcome |
| **Practice Viva** | Let students rehearse against the kind of questions they will face in a live session, as often as they want | Before a dissertation viva, OSCE-style communication or an assessed pitch |

*Table 2: The three modes of Eduface's Oral Examination tool.*

**Integrity Check** can be used in three increasingly strong patterns: on a random sample of the cohort, where the possibility of selection deters; as a gateway on every submission before the written mark is confirmed; or replaced entirely by an Oral Exam where the spoken reasoning is the point. Our guides on [verifying authorship in Moodle](/resources/blog/ai-oral-exams-moodle-verify-authorship) and [oral follow-up questions in Blackboard](/resources/blog/beyond-ai-detection-oral-verification-blackboard) go into this in detail.

**Oral Exam** is the assessment itself, graded criterion by criterion against the lecturer's rubric. See [running consistent vivas in Canvas](/resources/blog/are-oral-exams-ai-proof-canvas).

**Practice Viva** removes much of the fairness objection to oral assessment: that confident speakers are advantaged by familiarity with the format rather than by knowing more. See [AI-proof oral exam practice in Moodle](/resources/blog/ai-proof-oral-exam-practice-moodle).

## How do you choose the examiner's style and character?

Tone changes what a student can show you. Eduface offers four dialogue styles, set per session:

| Style | How the examiner behaves | Best for |
|---|---|---|
| **Socratic** | Open, probing questions that build toward deeper reasoning | Formative vivas, early-stage assessment |
| **Confrontational** | Pushes back on every claim; the student must defend a position | Assessments that test performance under pressure, such as a dissertation defence or negotiation |
| **Supportive** | Encourages and guides to draw out the best answer | Building confidence with the format, first-year students |
| **Formal** | Strict academic tone and procedural structure | High-stakes summative orals where tone should be a non-factor |

*Table 3: The four examiner dialogue styles.*

The character can be set to the discipline as well as the register: a strict dissertation examiner, a sceptical investor reviewing a business plan, or a distressed patient in a simulated clinical encounter. We explain how to choose in [AI oral examiner styles in Brightspace](/resources/blog/ai-oral-examiner-styles-brightspace).

The style changes how questions are asked, not how the answer is graded. Grading is always against the lecturer's rubric.

## Where does oral assessment fit by discipline?

| Discipline | Oral use | Suggested mode and style |
|---|---|---|
| **Law** | Defending a legal argument; opposing counsel; dissertation viva | Oral Exam, Confrontational or Formal |
| **Nursing and health** | Communication with a distressed patient; explaining a care decision | Practice Viva, then Oral Exam; Supportive for early practice |
| **Medicine** | Breaking bad news; history taking; clinical reasoning out loud | Practice Viva before OSCE-style assessment |
| **Business** | Pitch to a sceptical investor; client meeting | Oral Exam, Confrontational |
| **Humanities and social sciences** | Defending an interpretation in an essay | Integrity Check after submission; Socratic |
| **STEM** | Explaining the method and choices in a project or lab report | Integrity Check or Oral Exam, Formal |
| **Any dissertation** | Rehearsal before the live viva | Practice Viva, Formal |

*Table 4: Oral assessment by discipline. Illustrative starting points.*

## How do you make AI oral exams fair?

Oral assessment has its own equity profile. It is different from written assessment, not uniformly better. Plan for it before you deploy.

**Reasonable adjustments.** Students with speech differences, anxiety disorders or who are assessed in an additional language may be disadvantaged in ways written work does not disadvantage them. Apply the same adjustments framework as for a human viva: extra time, alternative formats, and a documented route to an equivalent assessment where the format itself is the barrier. Sussex's written alternative is a good example.²

**Evaluate content, not delivery.** Grading should assess what a student says against the rubric. Any system that scored fluency, hesitation or accent would be measuring something other than the learning outcome. Put that question to every vendor in writing.

**Let students practise.** Unfamiliarity with the format disadvantages some students more than others. Practice Viva mode lets every student rehearse as often as they need.

**Structure every session.** The reliability evidence above is about structure. Use a rubric, consistent question design and the same style for every student taking the same assessment.

**Keep the lecturer's judgement at the end.** The AI's evaluation is a draft. The lecturer reads the transcript, forms their own view and approves. Where an Integrity Check raises a concern, it enters the institution's existing misconduct process as a transcript a member of staff can read and explain.

> **Before your first oral exam**
> Agree the adjustments route and the alternative format · write the rubric with observable descriptors · choose one mode and one style for the whole cohort · offer a Practice Viva first · tell students they will be speaking with an AI examiner and that a lecturer decides the outcome · agree the retention period for recordings and transcripts in your Data Processing Agreement.

## What does the law require?

**The EU AI Act.** Systems used to evaluate learning outcomes are high-risk under Annex III, point 3(b), of Regulation (EU) 2024/1689, which requires effective human oversight and logging. Following the Digital Omnibus on AI, the obligations for these Annex III systems apply from 2 December 2027.⁵ Two further points apply to oral assessment specifically:

- **Transparency.** People must be told when they are interacting with an AI system. That obligation under Article 50 applies from 2 August 2026, so students should be told clearly that the examiner is an AI.
- **Emotion recognition.** The AI Act restricts emotion recognition in education. That is another reason an oral assessment tool should evaluate the content of what a student says, not infer their emotional state from how they say it.

**Data protection.** Recordings and transcripts are personal data. Eduface processes on its own GPU infrastructure in the Netherlands, uses no third-party AI APIs, never uses student data to train external models and signs a Data Processing Agreement with each institution. Set the retention period for recordings and transcripts explicitly.

**Procurement.** Eduface is an approved supplier on the Jisc/CHEST framework (UK) and HEAnet (Ireland).

## What does the lecturer see when reviewing an oral?

The review is where academic judgement happens, so it is worth knowing what is in front of the lecturer.

**The full transcript.** Every question the AI examiner asked and every answer the student gave, in order. Because follow-up questions depend on the previous answer, the transcript shows how the student's reasoning developed, not only whether each answer was right.

**A criterion-by-criterion evaluation.** For each rubric criterion, the evaluation and the reasoning behind it, pointing to the parts of the conversation that support it.

**The link to the submission.** For an Integrity Check, the questions were generated from the student's own work, so the lecturer can compare what the student said with what they wrote.

**The decision.** The lecturer forms their own view, changes anything they disagree with, and approves. For an Integrity Check that raises a concern, the lecturer decides whether it goes into the misconduct process, with the transcript as evidence a colleague or a panel can read.

A practical approach to review time is to read in full where it matters most: any Integrity Check that raised a concern, any borderline result, and the first ten or twenty sessions of a new assessment while you check that the evaluation matches your own judgement. Where the evaluation is clear and consistent with the rubric, a lighter review is usually enough.

## What are the most common mistakes with oral assessment?

| Mistake | What goes wrong | What to do instead |
|---|---|---|
| **Using orals for everything** | Students and staff burn out; the format loses its value | Use orals where spoken reasoning or authorship is the question, as Warwick recommends for key assessments and capstones |
| **No rubric, or a vague one** | Evaluation depends on impressions; reliability falls to the level of an unstructured viva | Observable descriptors per criterion, the same for every student |
| **Different styles for the same assessment** | Some students face a harder conversation than others | One style and character per assessment |
| **No practice** | Students unfamiliar with the format are disadvantaged | Offer a Practice Viva before any assessed oral |
| **Adjustments decided late** | Students who need an alternative are identified after the event | Agree the adjustments route and alternative format before the assessment opens |
| **Not telling students it is an AI** | Breaches transparency obligations and trust | Say it in the handbook and at the start of the session |
| **Treating the AI evaluation as the decision** | The lecturer's judgement becomes a formality | Review transcripts, especially concerns and borderline results, and own the outcome |

*Table 5: Common mistakes when introducing oral assessment, and what to do instead.*

## What does it cost in academic time?

The human version is the benchmark. A ten-minute oral for 400 students is around 67 hours of academic time, before scheduling, rooms, second examiners and adjustments. With two examiners per viva, as the QAA guidance and the Sussex example describe, that doubles.

[FIGUUR: Where the time goes for 400 ten-minute orals]
- Left stacked bar, "Human vivas": conducting 67 hours · second examiner 67 hours · scheduling and rooms (unquantified, hatched)
- Right stacked bar, "AI-conducted orals": students take the session in their own time · lecturer reviews transcripts and evaluations (hatched, "depends on depth of review")
- No invented numbers on the right bar; label as illustrative

*Figure 2: Human vivas at cohort scale compared with AI-conducted orals. Illustrative; only the human figure is calculated.*

With an AI-conducted oral, the conversation no longer needs an academic in the room or a timetable slot. The lecturer's time moves to reviewing transcripts and evaluations, which can be prioritised: full review for flagged cases and borderline results, lighter review where the evaluation is clear.

## How do you run a first oral exam in your LMS?

**1. Pick one module and one purpose.** An Integrity Check on a sample of essays is the lightest start. A Practice Viva before an existing live viva is the lowest-risk start.

**2. Write or adapt the rubric.** Observable descriptors, as for written work. See [how to write a rubric AI can mark against](/resources/blog/how-to-write-a-rubric-ai-can-mark-against).

**3. Choose the mode, style and character.** One of each for the whole cohort.

**4. Connect through LTI 1.3.** A learning technologist adds Eduface as an external tool once. Setup guides: [Moodle](/resources/blog/ai-essay-grader-moodle-lti), [Canvas](/resources/blog/ai-essay-grader-canvas-lms-lti), [Brightspace](/resources/blog/ai-essay-grader-brightspace-d2l) and [Blackboard](/resources/blog/ai-essay-grader-blackboard-lti).

**5. Tell students,** in the module handbook and in the session itself, that they will speak with an AI examiner, what it assesses, how adjustments work, and that a lecturer decides the outcome.

**6. Review the first cohort's transcripts closely.** Check the evaluation against your own judgement on the first ten or twenty. Adjust the rubric where they differ.

## Frequently asked questions

**Can an AI conduct an oral exam fairly?**
It can conduct a structured oral consistently, which is what the research links to reliability. Fairness also needs reasonable adjustments, evaluation of content rather than delivery, a chance to practise, and a lecturer who reviews the transcript and decides the outcome.

**Are oral exams AI-proof?**
They are much harder to fake than written work, because the questions come from the student's own submission and adapt to each answer. No format is completely proof against misuse; Warwick's guidance notes that hidden devices could in future assist students in real time. Oral assessment verifies understanding better than detection estimates authorship.

**How long does an AI oral exam take?**
Typically 15 to 20 minutes for the student. The session runs in the browser through the LMS, with no scheduled slot or room.

**Does the AI decide whether a student has cheated?**
No. It produces a transcript and a rubric-aligned evaluation. The lecturer forms the academic judgement, and any concern goes into the institution's existing misconduct process.

**Do students need to be told the examiner is an AI?**
Yes. Under Article 50 of the EU AI Act, people must be told when they interact with an AI system, from 2 August 2026. It is also simply fair: tell students in the module handbook and at the start of the session.

**Is Eduface's Oral Examination tool generally available?**
It is in early access with pilot institutions. If you are considering oral assessment for a module, we can set up a pilot with your rubric.

**Can AI oral exams replace OSCEs or placement assessment?**
No. OSCEs and placement assessment test clinical skills in person, observed by trained assessors. AI oral exams are useful alongside them: as practice for difficult conversations such as breaking bad news, or for assessing how a student explains their reasoning. They do not replace hands-on assessment.

**Can a student retake an AI oral exam?**
That is a decision for the module leader and the assessment regulations. Practice Viva mode is designed for unlimited rehearsal. For assessed orals, apply the same rules on resits and mitigating circumstances as for any other assessment.

## References

1. Quality Assurance Agency for Higher Education. (2023). *Reconsidering assessment for the ChatGPT era: QAA advice on developing sustainable assessment strategies*. [Structured oral interviews with clear rubrics and safeguards; mini-vivas to authenticate and assess written work; historical concerns about reliability and stress; accessibility.]
2. Newnham, L. (2024, August). *Oral assessment (viva) as an AI-proof assessment tool*. University of Sussex, Learning Matters. [65% coursework and 15-minute oral worth 35%; four-question structure; two markers; written alternative as a reasonable adjustment.]
3. University of Warwick. (2024). *Implementing oral examinations (VIVAs)*. AI in Mathematics project outputs. [Use for key assessments and capstones; transparent, consistent rubrics; risk of uneven examiners; equity considerations; future risk of real-time assistance.]
4. Abuzied, A. I. H., & Nabag, W. O. M. (2023). Structured viva validity, reliability, and acceptability as an assessment tool in health professions education: a systematic review and meta-analysis. *BMC Medical Education*. [Structured vivas: alpha 0.80/0.75 vs 0.50; reliability 0.7-0.8 vs 0.3-0.4; inter-rater r 0.78-0.91; acceptability 79.8%.]
5. European Parliament and Council of the EU. (2024). Regulation (EU) 2024/1689 (Artificial Intelligence Act), Annex III, point 3(b), and Article 50; as amended by the Digital Omnibus on AI (in force 27 July 2026). [High-risk obligations for Annex III systems apply from 2 December 2027; Article 50 transparency from 2 August 2026.]
