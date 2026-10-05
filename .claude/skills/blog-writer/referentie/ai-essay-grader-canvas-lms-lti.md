<!--
Referentieblog, door Dante geplakt op 25-09-2026. Letterlijk overgenomen, alleen de opmaak is naar markdown gezet.
Gebruik voor STIJL en OPBOUW. Niet als bron voor feiten of claims:
- losse "Feedback Tool", vier feedbackstijlen, drie-agent Exam Grader, "48% more consistent", "Under 4 min", "95% alignment",
  blind/AI-visible mode, GPU in NL, Jisc/CHEST en HEAnet staan niet in Platform/product.md (W7)
-->

EYEBROW: CANVAS · LTI 1.3

# AI Essay Grader for Canvas LMS: Grading, Feedback and Oral Exams via LTI 1.3

*Connect Eduface to Canvas via LTI 1.3 to add AI grading, formative feedback, exam marking and oral exams. Submissions flow in automatically, approved grades pass back to the Canvas gradebook, and no separate student login is needed.*

By Eduface · June 2026 · 8 min read

Your institution has Canvas. Lecturers are spending hours marking the same type of essay, week after week. Students are waiting days for feedback that arrives too late to improve their next draft. And you are being asked to find AI tools that work inside Canvas rather than asking staff to learn a separate platform. That pressure is real, and it is arriving at institutions across the UK and Ireland right now.

> **What AI assessment tools are available for Canvas LMS?**
> Eduface is an AI assessment platform that connects to Canvas via LTI 1.3, adding four tools directly to your existing workflow: an essay and paper grader, a formative feedback generator, a written exam grader, and an oral examination tool. Submissions flow in from Canvas automatically, and approved grades pass back to the Canvas gradebook without any manual export. No separate student login is required.

## How does Eduface connect to Canvas via LTI 1.3?

LTI 1.3 (Learning Tools Interoperability) is the standard protocol that allows external applications to embed securely inside a learning management system. Canvas has supported LTI 1.3 since 2019, and it is now the required standard for any new integration.

Eduface connects to Canvas as an LTI 1.3 external tool. Setup is completed once by the institution's learning technologist: the LTI credentials are added to Canvas's Developer Keys panel, and the tool appears as an available external app across courses. From that point, lecturers can add any Eduface tool to a Canvas assignment without any IT involvement.

[FLOWDIAGRAM] Student (Submits via Canvas) → Eduface (AI processes submission) → Lecturer (Approves grade or edits) → Canvas Gradebook (Updated)
*Every grade requires explicit lecturer approval before it is recorded in the Canvas gradebook.*

Crucially, students do not need a separate Eduface login. They submit their work through Canvas as normal. The LTI integration handles authentication silently in the background.

The setup process works like this:

1. **One-time setup by the learning technologist.** LTI 1.3 credentials are added to Canvas Developer Keys. Eduface appears as an available external tool across all courses.
2. **Lecturer configures the assignment.** The lecturer uploads the rubric and assignment brief once inside Eduface. Subsequent submissions are processed automatically.
3. **Student submits via Canvas as normal.** No new login, no change to the student-facing workflow. Eduface receives the submission through the LTI channel.
4. **Lecturer reviews and approves.** The AI draft is held until the lecturer explicitly approves. On approval, the grade passes back to the Canvas gradebook automatically.

## What does the Paper Grader do inside Canvas?

The Paper Grader is designed for essays, reports, and other written coursework submitted at scale. The lecturer uploads a rubric and assignment brief once. From that point, every submission that arrives from Canvas is annotated directly: Eduface marks up the text, assigns a score for each rubric criterion, and provides the reasoning behind each score.

The suggested grade is held in draft. It is not visible to the student, and it is not recorded anywhere, until the lecturer opens the submission, reviews the annotation and scoring, and explicitly clicks to approve. In UK pilots, lecturers adjusted an average of just 5% of each final grade, indicating 95% alignment between the AI suggestion and the marker's own judgement. The grade then passes back directly to the Canvas gradebook without any manual export step.

The Paper Grader supports two operating modes. In blind mode, the lecturer sees only the submission and makes their own mark before any AI suggestion is revealed. In AI-visible mode, the AI suggestion is displayed alongside the submission from the start. Institutions can set which mode applies by default, or leave it as a per-assignment choice for the lecturer.

## How does AI formative feedback work for Canvas assignments?

Formative feedback is one of the most evidence-backed interventions in higher education. Hattie and Timperley's landmark review found feedback to be among the most powerful influences on student achievement, but only when it is specific, timely, and actionable.

The Eduface Feedback Tool generates personalised, rubric-aligned formative feedback for every Canvas submission. The AI drafts the feedback for each student; the lecturer can review and edit it before it is released. This tool does not attach a grade unless the lecturer chooses to do so, keeping formative and summative functions clearly separate.

The feedback style is configurable. Lecturers can choose from Reflective and Socratic, Constructive and Direct, Went Well and Needs Improvement, or Supportive and Encouraging. The tool also tracks student skill progression across multiple drafts, so a student submitting a second version of an assignment can receive feedback that explicitly references where they have improved since the first attempt.

Six domain-specific submodels power the feedback generation: Law, Economics, Social Sciences, STEM, Humanities, and Health Sciences.

## How does the Exam Grader handle written questions in Canvas?

Open-ended written exam questions present a specific challenge for consistency. When the same cohort is marked by multiple human markers, score variation between markers is common and well-documented. The Eduface Exam Grader addresses this with a three-agent architecture designed to replicate the rigour of a double-blind marking process, at scale.

Three independent AI agents each evaluate a student's answer against the grading scheme without seeing one another's results. A fourth reconciliation agent then compares the three scores. Where the agents reach strong agreement, the system flags high confidence. Where there is significant divergence, the submission is flagged for the lecturer's direct attention.

| Key performance stat | Figure |
|---|---|
| More consistent than unaided human marking across the same cohort | 48% |
| From upload to suggested grade per assignment | Under 4 min |
| Alignment between AI suggestion and lecturer final grade in UK pilots | 95% |

The lecturer sees the suggested grade alongside the per-criterion reasoning from all three agents. They fill in the final score themselves and confirm before any grade is recorded. A full audit trail is maintained per submission, covering every agent's reasoning and the lecturer's decision. This satisfies the human oversight requirements of Article 14 of the EU AI Act.

## What is the Oral Examination tool and how does it support academic integrity in Canvas?

The Oral Examination tool is currently in early access with pilot institutions. Lecturers configure a character and a structured situation. The AI then conducts a spoken conversation with the student and provides consistent, rubric-aligned evaluation at the end.

Two use cases are emerging clearly from early pilots. The first is formal oral assessment: structured vivas, presentations, and professional role-play scenarios. The second is academic integrity verification: using a follow-up oral conversation to check whether a submitted piece of written work is genuinely the student's own. A student who wrote the essay can typically answer questions about it. A student who did not write it often cannot.

This is a meaningful addition to Canvas workflows, where submissions arrive digitally but there is no native mechanism for follow-up verification.

## Comparing the four Eduface tools for Canvas

| Tool | Primary purpose | Assessment type | When the lecturer approves | Grade passback to Canvas |
|---|---|---|---|---|
| Paper Grader | Grade essays and written coursework at scale | Summative | Before any grade is recorded or shown to the student | Yes, automatic on approval |
| Feedback Tool | Generate personalised formative feedback per submission | Formative (grade optional) | Before feedback is released to the student | Optional (if grade is attached) |
| Exam Grader | Grade open-ended written exam questions consistently | Summative | Lecturer fills final score and confirms | Yes, automatic on confirmation |
| Oral Examination | Conduct structured oral assessment and integrity checks | Summative / integrity | Lecturer reviews rubric-aligned evaluation before recording | Yes (early access) |

> **Compliance note**
> All four tools are built to comply with the EU AI Act (Regulation 2024/1689). Educational assessment is classified as high-risk AI under Annex III. Eduface's architecture enforces mandatory human oversight at every grade decision point, with a full audit trail per criterion. Eduface operates on proprietary GPU infrastructure in the Netherlands and does not use third-party AI APIs such as OpenAI. It is an approved supplier on the Jisc/CHEST framework (UK) and the HEAnet framework (Ireland).

## Frequently Asked Questions about AI assessment in Canvas

**Does Canvas have a built-in AI grader?**
Canvas does not include a built-in AI grading tool as a standard feature. Canvas does offer some AI-assisted features for quiz creation and course content, but there is no native AI that grades essays, open-ended exam answers, or oral examinations and writes back to the gradebook. AI grading capability comes from external tools connected via LTI 1.3, such as Eduface.

**Is Eduface GDPR-compliant for Canvas users?**
Yes. Eduface is GDPR-compliant and EU AI Act compliant. It runs on proprietary GPU infrastructure located in the Netherlands and does not send student data to external AI APIs. For UK institutions, Eduface is an approved supplier on the Jisc/CHEST framework, which means it has passed the procurement and data security checks required for use in UK higher education.

**Do students need to do anything differently in Canvas when Eduface is active?**
No. Students submit their work through Canvas exactly as they do today. The LTI 1.3 integration operates in the background. Students do not need a separate Eduface account or login, and they do not interact with the Eduface interface directly. From the student's perspective, the submission process is unchanged.

**How long does it take to set up Eduface in Canvas?**
The LTI 1.3 integration is configured once by the institution's learning technologist, typically in a single session. Eduface's team provides setup documentation and support. After the initial configuration, individual lecturers can add any of the four tools to their Canvas assignments without involving IT.

**Does Eduface replace SpeedGrader in Canvas?**
Eduface works alongside Canvas SpeedGrader rather than replacing it. Lecturers review AI-suggested grades and feedback inside the Eduface interface, then approve them. The approved grade passes back to the Canvas gradebook automatically, so it appears in SpeedGrader as a normal recorded grade. The two tools complement each other: Eduface handles the analytical work; SpeedGrader remains the source of record inside Canvas.
