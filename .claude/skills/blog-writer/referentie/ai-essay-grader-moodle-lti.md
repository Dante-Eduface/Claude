<!--
Referentieblog, door Dante geplakt op 25-09-2026. Letterlijk overgenomen, alleen de opmaak is naar markdown gezet.
Dit is de HUB van het Moodle-cluster.
Gebruik voor STIJL en OPBOUW. Niet als bron voor feiten of claims:
- losse "Feedback Tool", vier feedbackstijlen, drie-agent Exam Grader, "48%", "Under 4 min", "5% / 95% alignment" (als citaat),
  blind/AI-visible mode, GPU in NL, DPA met elke instelling, Jisc/CHEST en HEAnet staan niet in Platform/product.md (W7)
-->

EYEBROW: MOODLE · LTI 1.3

# AI Essay Grader for Moodle: Grading, Feedback and Oral Exams via LTI 1.3

*Connect Eduface to Moodle via LTI 1.3 for AI grading, formative feedback, exam marking and oral exams. No plugin, no IT overhead, and grades return to the Moodle Gradebook after lecturer approval.*

By Eduface · June 2026 · 8 min read

When a learning technologist is asked to find an AI assessment tool that works inside Moodle, the first question is almost always the same: is there an AI grading plugin for Moodle? The short answer is that the most capable AI assessment tools do not work as Moodle plugins at all. They connect via LTI 1.3, and this turns out to be a better fit for institutions in almost every respect.

> **What AI assessment tools are available for Moodle?**
> Eduface provides four AI assessment tools that connect to Moodle via LTI 1.3 External Tool: a Paper Grader for essays and written assignments, a Feedback Tool for personalised formative feedback, an Exam Grader for open-ended exam questions, and an Oral Examination tool for structured AI-conducted oral assessments. No plugin installation is required. All four tools return grades to the Moodle Gradebook automatically after the lecturer approves them.

## Is Eduface a Moodle plugin or an LTI integration?

Eduface is not a Moodle plugin. It connects to Moodle as an External Tool using the LTI 1.3 standard. This distinction matters more than it might initially seem.

A Moodle plugin lives inside the Moodle codebase. Every time Moodle releases a new version, institutions must wait for the plugin to be updated, test it against their instance, and manage the upgrade themselves. Plugins require IT involvement for installation and carry a security surface that institutions must audit.

An LTI 1.3 External Tool lives entirely outside Moodle. A learning technologist enters the LTI credentials Eduface provides, and the connection is established. From that point on, Eduface updates independently without any changes to Moodle. There is no version dependency, no plugin update cycle, and no IT overhead. Students submit through Moodle Assignment activities exactly as they normally would, and approved grades return to the Moodle Gradebook automatically.

> **For IT and learning technology teams**
> Eduface LTI 1.3 setup typically takes one afternoon. The institution receives a Client ID, Deployment ID, and endpoint URLs, entered once in Moodle's External Tools settings. No code changes, no server access, no infrastructure modifications.

LTI 1.3 is the current standard for connecting external tools to any major LMS, giving institutions the reliability of a maintained external service without tying them to one vendor's internal architecture.

[FLOWDIAGRAM] Student (Submits via Moodle) → LTI 1.3 (Routes to Eduface) → Eduface (Processes and grades) → Lecturer (Reviews and approves) → Grade returned (To Moodle Gradebook)
*Students submit via Moodle, LTI 1.3 routes the submission to Eduface, the lecturer approves the grade, and it returns automatically to the Moodle Gradebook.*

## How does the AI Paper Grader work inside Moodle?

The Paper Grader is designed for essays, reports, and other long-form written assignments. The lecturer uploads the assignment brief and rubric once. Eduface then processes each submission against that rubric, annotates the text, assigns per-criterion scores with written reasoning, and holds the grades in draft until the lecturer explicitly approves them.

Grades never reach students automatically. The lecturer sees the AI suggestions, can edit any score or comment, and releases grades only when satisfied. Explicit human approval before release is required under the EU AI Act for high-risk AI systems in education.

> "In UK pilots, lecturers changed an average of just 5% of each final grade. That is a 95% alignment rate between the AI suggestion and the lecturer's considered judgement."
> Eduface Paper Grader pilot data, UK higher education institutions

Two modes are available. In AI-visible mode, the lecturer sees the suggested scores upfront. In blind mode, the AI suggestion is withheld until after the lecturer has formed their own assessment, eliminating anchoring bias. Both modes pass the approved grade to the Moodle Gradebook via LTI Grade Services.

## How does AI formative feedback work for Moodle assignments?

The Feedback Tool generates personalised, rubric-aligned formative feedback for every submission before the final grade is set. The AI drafts the feedback; the lecturer reviews and can edit it before it reaches the student.

Four feedback styles are available:

- Reflective and Socratic
- Constructive and Direct
- Went Well and Needs Improvement
- Supportive and Encouraging

The tool runs on six domain-specific submodels covering Law, Economics, Social Sciences, STEM, Humanities, and Health Sciences. It also tracks student skill progression across successive drafts, giving lecturers a longitudinal view of how each student is developing.

## How does the Exam Grader handle open-ended questions in Moodle?

Moodle handles multiple-choice and short-answer formats automatically, but written exam answers require human judgement. The Exam Grader brings AI assistance to this task without sacrificing consistency.

Three independent AI agents evaluate each answer against the grading scheme without seeing each other's results. A fourth agent reconciles the scores: strong agreement raises confidence, disagreement is flagged for the lecturer. The lecturer confirms every score before it is recorded, and a full audit trail supports any grade appeal.

| Exam Grader stat | Result |
|---|---|
| More consistent than unaided human marking across multiple markers | 48% |
| From upload to suggested grade per assignment | Under 4 min |
| Full audit trail, required under EU AI Act Annex III | 100% |

## How does Oral Examination support academic integrity in Moodle?

The Oral Examination tool is currently in early access. Lecturers configure an AI examiner with a specific character: a sceptical investor, a distressed patient, or a strict academic examiner, depending on the learning context. The AI conducts a structured conversation that adapts in response to each student's answers rather than following a fixed script.

This makes it significantly harder to prepare for with generic AI-generated responses, which is why institutions are using it for both formal oral assessment and academic integrity verification. Consistent, rubric-aligned evaluation is provided across six academic fields.

## Comparing all four Eduface tools for Moodle

| Tool | Purpose | Assessment type | Lecturer approves | Grade passback to Moodle |
|---|---|---|---|---|
| Paper Grader | AI-assisted marking of essays and written assignments | Summative | Each grade and annotation before release | Yes, via LTI Grade Services |
| Feedback Tool | Personalised formative feedback per submission | Formative | Each feedback item before student receives it | Yes (when used summatively) |
| Exam Grader | Consistent marking of open-ended exam answers | Summative | Final score per answer after agent reconciliation | Yes, via LTI Grade Services |
| Oral Examination | AI-conducted structured oral assessment | Summative / integrity | Rubric-aligned evaluation before recording | Yes (early access) |

All four tools share the same principle: the AI produces a recommendation, and grades only reach students after the lecturer has explicitly approved them. This is built into the platform architecture, not added as a compliance layer.

> **EU AI Act note**
> Education grading is high-risk AI under Annex III. Eduface complies: every grade requires explicit lecturer approval, a full audit trail is maintained, and the platform runs on proprietary GPU infrastructure in the Netherlands with no third-party big-tech APIs. Eduface is approved on the Jisc/CHEST framework (UK) and HEAnet framework (Ireland).

## Frequently Asked Questions about AI assessment in Moodle

**Is there an AI grading plugin for Moodle?**
Moodle has no native AI grading capability. Eduface connects via LTI 1.3 External Tool rather than as a plugin. This is preferable: no plugin installation, no Moodle version-specific updates, and no IT maintenance inside the LMS. A learning technologist configures the connection once using the LTI 1.3 credentials Eduface provides, and the integration remains stable across all future Moodle upgrades.

**Is Eduface GDPR-compliant for Moodle users?**
Yes. Eduface runs on proprietary GPU infrastructure in the Netherlands and does not use third-party APIs such as OpenAI. Student data stays in the EU. Eduface signs a Data Processing Agreement with each institution and is an approved supplier on the Jisc/CHEST framework (UK) and HEAnet framework (Ireland), both of which require verified compliance standards.

**Does Moodle grade passback work with Eduface?**
Yes. Once a lecturer approves a grade, it passes back automatically to the Moodle Gradebook via LTI Grade Services. No manual re-entry or data export is needed. Grade passback is supported for the Paper Grader, Exam Grader, and Feedback Tool (summative use), and for Oral Examination in early access.

**How long does it take to set up Eduface in Moodle?**
Typically one afternoon. Eduface provides a Client ID, Deployment ID, and endpoint URLs. These are entered once in Moodle's Site Administration under External Tools. Eduface's onboarding team supports the configuration and runs a test submission to confirm grade passback before go-live. No server access or code changes are required.

**Does Eduface work with Moodle 4.x?**
Yes. Because Eduface connects via LTI 1.3, it has no dependency on any specific Moodle version. LTI 1.3 and Grade Services are fully supported in Moodle 4.x. When Moodle releases future updates, the Eduface integration requires no changes.
