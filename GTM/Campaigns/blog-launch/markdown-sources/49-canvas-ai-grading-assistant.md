---
title: "Canvas AI Grading Assistant: What IgniteAI Grading Assistance Does and When You Need More"
seo_title: "Canvas AI Grading Assistant: What It Does | Eduface"
meta_description: "Canvas now has AI grading. What IgniteAI Grading Assistance in SpeedGrader does, what it skips, where data goes, and when an LTI grading tool fits better."
slug: canvas-ai-grading-assistant
primary_query: "canvas ai grading assistant"
secondary_queries: ["does canvas have ai grading", "ignite ai grading assistant", "canvas ai grading tool", "canvas speedgrader ai", "ai grading canvas"]
type: integratie
category: Integrations
hub: /resources/blog/ai-essay-grader-canvas-lms-lti
related: [/resources/blog/ai-essay-grader-canvas-lms-lti, /resources/blog/how-to-write-a-rubric-ai-can-mark-against, /resources/blog/ai-grading-tools-higher-education-guide]
review_by: 2026-12-15
status: concept
outline: "H2s: What is IgniteAI Grading Assistance in Canvas? / What do you need before you can turn it on? / What does the Canvas grading assistant not do? / Where does student data go? / When is the built-in assistant enough? / When does a dedicated grading tool earn its place? / What evidence is there? / How does it compare with an LTI 1.3 tool like Eduface? / Which should your program start with? / How do you test them side by side? / FAQ. Information gain: Instructure's own limits and AI Nutrition Facts in one place, a question list for the Instructure account team, a decision table, and a side-by-side test protocol with a worked example (illustrative numbers)."
note: "Spoke van de Canvas-hub. Setup niet herhaald, alleen gelinkt. Alle Canvas-feiten uit drie Instructure-pagina's, gelezen 05-10-2026. LET OP: de FAQ van de live hub zegt nog 'Canvas does not include a built-in AI grading tool', dat klopt sinds 18-04-2026 niet meer."
---

EYEBROW: CANVAS · AI GRADING ASSISTANT

# Canvas AI Grading Assistant: What IgniteAI Grading Assistance Does and When You Need More

*Canvas now has a built-in AI grading assistant that suggests rubric ratings and comments inside SpeedGrader. Here is what it does, what Instructure says it does not do, where the data goes, and when a dedicated LTI 1.3 grading tool earns its place next to it.*

By Eduface · October 2026 · 14 min read · Written for instructors, learning technologists and directors of instructional design at private and for-profit colleges on Canvas

Your Canvas admin has switched on a new feature option, and a button called Auto-Evaluate has appeared in SpeedGrader. One click, and a rating and a comment fill in for every rubric criterion. The instructors in the pilot course like it. Then your program director asks the question you saw coming: if Canvas does AI grading now, why would we pay for another tool?

> **What is the Canvas AI grading assistant, and does Canvas have AI grading?**
> Yes, Canvas has AI grading. Instructure's built-in assistant is IgniteAI Grading Assistance for SpeedGrader, generally available since April 18, 2026. An instructor clicks Auto-Evaluate in SpeedGrader and Canvas suggests a rating and a comment for each rubric criterion on text entries and PDF or DOCX uploads. The instructor reviews, edits and submits, and students see an AI-Assisted label. It is off by default, needs a fully described rubric, and is included with Canvas Plus and Canvas Next. It does not check facts, sources or formatting.

## What is IgniteAI Grading Assistance in Canvas?

IgniteAI Grading Assistance for SpeedGrader is a Canvas feature option that suggests rubric ratings and written comments for a submission, which the instructor then reviews, edits and submits.¹ ² Instructure published the feature overview on February 18, 2026 and made it generally available on April 18, 2026, for all customer types and regions.¹ IgniteAI is Instructure's name across its AI features, so the "Canvas AI grading assistant" and the "Ignite AI grading assistant" are the same thing.

The instructor guide is explicit that this is support, not automation: "You must review and approve all AI-generated scores, feedback, and comments before submitting the assessment."² The workflow, per that guide:²

1. **Open SpeedGrader** from an assignment, quiz or graded discussion that uses a rubric.
2. **Click Auto-Evaluate.** Canvas sends the assignment information, the rubric and the submission to the model.³
3. **Review the suggestion.** A rating and a comment appear per criterion. Change, edit, or click Reset to start over (Reset cannot be undone).
4. **Click Submit Assessment.** Only then is it saved. Students see that the evaluation was AI-Assisted on their Grades page and the assignment page.

[FLOWDIAGRAM] Instructor opens SpeedGrader (assignment with a rubric) → Auto-Evaluate (assignment information, rubric and submission go to the model) → Suggested rating and comment per criterion (selected by default) → Instructor edits, accepts or resets → Submit Assessment → Student sees the result with an "AI-Assisted" label
*Figure 1: The IgniteAI Grading Assistance workflow in SpeedGrader, based on Instructure's guide. Nothing reaches the student until the instructor clicks Submit Assessment.*

One detail sits in Instructure's AI Nutrition Facts card rather than the guide: the grade suggestion "is displayed and selected by default, but the instructor must make the final decision to edit or accept the suggestions."³ The instructor starts from the AI's rating, not their own. We come back to why that matters.

## What do you need before you can turn it on?

You need the right Canvas package, two feature options, Enhanced Rubrics, and rubrics in which every criterion and rating has a title and a description.¹ ²

| Requirement | What Instructure documents | What to check |
|---|---|---|
| Canvas package | Included with Canvas Plus and Canvas Next² | Which package your contract covers |
| Feature options | "IgniteAI Grading Assistance for SpeedGrader" plus "Performance and usability upgrades for SpeedGrader"; off by default; root account, sub-account or course level¹ | Who turns it on, and where |
| Rubrics | Enhanced Rubrics on; a missing criterion or rating description gives an error and no evaluation² | How many rubrics have rating descriptions |
| Submission types | Text entry, or uploads in PDF or DOCX only² | Assignments that collect slides, images or audio |
| Assignment type | Essay-style work; not single-correct-answer assignments² | Which assessments are essays |

*Table 1: What Canvas needs before Grading Assistance runs. Source: Instructure, read October 5, 2026.*

> **For Canvas admins**
> Because the feature option works per sub-account and per course, you can pilot it in one program without switching it on institution-wide. Instructure staff confirmed in the feature overview thread that it is off by default and only available once an institution's admin team enables it.¹

The rubric requirement is the one that catches programs out. Many Canvas rubrics have criterion titles and points but empty rating descriptions, because the instructor who wrote them knows what "Proficient" means. The model does not. Instructure says results are "based only on criteria explicitly stated in the rubric",² so suggestions can only be as specific as the rubric. Our guide on [how to write a rubric AI can mark against](/resources/blog/how-to-write-a-rubric-ai-can-mark-against) covers the level descriptors that make the difference.

## What does the Canvas grading assistant not do?

Instructure is unusually direct about the limits: its own guide lists seven.² For career and professional programs, several land on exactly what graders care about.

- **It does not verify factual claims.** A technical report can cite the wrong specification and the assistant is not designed to catch it.
- **It does not evaluate sources** for legitimacy or credibility.
- **It does not check formatting.** Word count, structure and citation style stay with the instructor.
- **It does not flag harmful or sensitive content.** A submission that should prompt a welfare conversation will not be flagged.
- **It has "limited defenses against attempts to manipulate or bypass grading instructions".** A hidden instruction to the AI inside a submission is the obvious case, and one reason the instructor review is not optional.
- **It grades only what the rubric states.** What an instructor would reward without writing it down is invisible to it.
- **It is not built for single-answer questions** or quantitative work.

None of this makes the feature bad. It makes it a first pass on essay-style writing against a well-described rubric, which is what Instructure says it is. What Instructure has not published matters as much: in the documentation we read, there are no figures on how close suggestions come to instructors' grades, nothing on supported languages, and nothing on moderated or anonymous grading.

> **Questions to ask your Instructure account team**
> Is Grading Assistance in our Canvas package, and what does it cost if not? Which region does our instance use for the model? Who can see the logged model responses, and for how long? Does it work with moderated and anonymous grading? Which languages do the comments support? Do you have data on how close suggestions come to instructors' grades?

## Where does student data go when you use it?

When an instructor clicks Auto-Evaluate, the assignment information, rubric and submission go to Claude Haiku 4.5, an Anthropic model provided through Instructure's in-house AI platform, and Instructure states the model is not trained on that data.³ That comes from Instructure's AI Nutrition Facts card for Grading Assistance (revision dated July 27, 2026), the most detailed public description we found. The card also states:³

- **Retention:** "Transactional data is retained for the life of the request."
- **Logging:** "Complete response from the LLM is retained in the Canvas database for auditing purposes."
- **Regions supported:** Virginia, Oregon, Dublin, Frankfurt, Sydney.
- **Personal data:** none is sent intentionally, but incidental personal information in a submission "will be sent to the model".

For most US institutions this is a familiar profile: a general-purpose model from a large AI lab, reached through an LMS vendor you already contract with, with no training on your students' work. Two points deserve a question from your privacy team: the card lists where the model is available, not which region your instance uses, and it does not say who can view or export the logged responses.

## When is the built-in Canvas assistant enough?

For many instructors, the built-in assistant is enough, and that is where to start. It costs nothing extra if your package includes it, it lives where instructors already work, and it adds no vendor to review. It fits best when:

- **One instructor grades one section against their own rubric,** so consistency between graders is not the problem.
- **The work is essay-style and the rubric is detailed,** the case Instructure designed it for.
- **The instructor wants a first pass, not a new workflow.** Auto-Evaluate, edit, submit.
- **The stakes are low:** reflections, discussion posts and practice work.
- **There is no budget for another tool this year.** A feature instructors use beats a better tool nobody approves.

If that describes most of your grading, turn it on for one course and see whether instructors still click Auto-Evaluate in week three. You may not need anything else.

## When does a dedicated grading tool earn its place?

A dedicated tool earns its place when the problem is no longer one instructor's speed but the program's consistency, evidence and feedback loop. That is common at private and for-profit colleges: several campuses or intakes, part-time instructors grading the same capstone, accreditors asking how grades were reached. Five things separate a dedicated tool such as Eduface from the built-in assistant.

**Subject models, not one general model.** Canvas's assistant runs on one general-purpose model guided by your rubric.³ Eduface's Paper Grader runs on its own purpose-built model with six subject models (Law, Economics, Social Sciences, STEM, Humanities, Health Sciences), each trained on the conventions of its field, and uses no third-party APIs such as OpenAI's.

**Feedback on drafts.** Eduface's Paper Grader gives formative feedback on a first draft, a second draft and the final version, and tracks progress across drafts. The instructor writes the feedback instructions, picks a style (such as Reflective and Socratic, or Constructive and Direct) and decides whether feedback goes to the student directly or after approval. Instructure documents Grading Assistance as a grading step, not as draft-to-draft feedback.

**A consistency check on exams.** Eduface's Exam Grader grades open and closed answers. Three independent AI agents grade each answer without seeing each other's result; a fourth compares them. Agreement means high confidence, disagreement is flagged for the instructor. Eduface reports this is "48% more consistent than unaided human marking", with under 4 minutes from upload to suggested grade; the measurement setup is not public.

**Grader comparison across part-time instructors.** When twelve adjuncts grade the same assessment on three campuses, the question is who grades differently. Eduface's grader comparison dashboard shows when an individual grader deviates from the team or from the AI suggestion, without opening submissions one by one.

**An audit trail and a choice about anchoring.** Eduface keeps an audit trail per submission that meets EU AI Act requirements for summative assessments. In blind mode the instructor grades first and sees the AI suggestion afterward; in AI-visible mode it shows from the start; the institution can require one. Canvas pre-selects the suggestion.³ That is quicker, and it means the instructor starts from the AI's number, which is what blind mode exists to prevent.

## What evidence is there that either tool grades accurately?

Neither tool comes with a large, independent study, so your own test matters more than either vendor's claims. In the documentation we read, Instructure publishes no figures on how close Grading Assistance's suggestions come to instructors' grades.

Eduface's evidence is one pilot at one institution. At Bath Spa University in June 2026, across 435 submissions in 6 subjects and 13 markers, Eduface's suggested grade was on average about 6 points from the lecturer's grade, and about 2 points for lecturers who had tuned the model. Review took 2 to 3 minutes per submission. It is not known whether lecturers set their grade before or after seeing the suggestion, which is why the test below records the instructor's grade first.

## How does the Canvas grading assistant compare with an LTI 1.3 tool like Eduface?

Canvas's assistant is a fast first pass inside SpeedGrader; Eduface is a separate grading workflow that connects to Canvas via LTI 1.3 and returns approved grades to the Canvas Gradebook.

| | IgniteAI Grading Assistance (Canvas) | Eduface via LTI 1.3 |
|---|---|---|
| Where it runs | Inside SpeedGrader, as a feature option¹ | Separate tool in Canvas via LTI 1.3; set up once by your admin; no separate student login |
| What it grades | Text and PDF or DOCX; essay-style work² | Written coursework (Paper Grader); open and closed exam answers (Exam Grader); oral formats in beta |
| Model | Claude Haiku 4.5, general-purpose³ | Own model, six subject models; no third-party APIs such as OpenAI |
| Rubric handling | Every criterion and rating must be described² | Explainable breakdown per criterion; generates a rubric if there is none |
| Approval step | Suggestion pre-selected; instructor clicks Submit Assessment² ³ | Held until the instructor approves; blind or AI-visible mode |
| Consistency checks | None documented | Three-agent check on exams; grader comparison dashboard |
| Draft feedback | Not documented | First draft, second draft, final version |
| Data | Not used for training; response logged in Canvas; US, EU and Australian regions³ | Processed in the EU; never used to train AI models; DPA with every institution |
| Grade passback | Native, on Submit Assessment | LTI Grade Services to the Canvas Gradebook after approval |

*Table 2: Canvas's built-in grading assistant and Eduface on the same criteria. Canvas facts from Instructure, read October 5, 2026.*

[FLOWDIAGRAM] Student submits in Canvas as usual → Eduface receives it via LTI 1.3 → Subject model scores each rubric criterion and drafts comments → Instructor grades blind first or reviews the suggestion (the institution's choice) → Instructor approves → Grade returns to the Canvas Gradebook via LTI Grade Services
*Figure 2: How Eduface sits next to Canvas. The grade only reaches the Canvas Gradebook after the instructor approves it.*

We are not repeating the setup here. Our guide to the [AI essay grader for Canvas via LTI 1.3](/resources/blog/ai-essay-grader-canvas-lms-lti) covers Developer Keys, assignment configuration and grade passback step by step.

> **What Eduface doesn't do**
> Eduface does not live inside SpeedGrader. Instructors review suggestions in the Eduface interface, opened from Canvas. It is one more vendor for IT and procurement to review, with an LTI setup your admin completes once. Academic Integrity and Oral Examination are still in beta. If the Canvas assistant already covers your grading, those costs are not worth paying.

## Which should your program start with?

Start with the problem, not the tool. One instructor's time on essays points to the built-in assistant; consistency across graders, exam volume or draft feedback point elsewhere.

| If your situation is | Start with |
|---|---|
| One instructor per course, essays, detailed rubrics, Canvas Plus or Next | Canvas Grading Assistance |
| Several part-time instructors grading the same assessment across campuses | A dedicated tool with grader comparison |
| Open-answer exams at volume | Eduface Exam Grader |
| Feedback on drafts before the final submission | Eduface Paper Grader's formative feedback |
| Subject-heavy work such as law or health sciences | Test both on the same submissions |

*Table 3: A starting point by situation, not a verdict. Many programs will use both.*

## How do you test the Canvas assistant against a dedicated tool?

Run both on the same submissions, record the instructor's own grades before anyone sees a suggestion, and compare four numbers. That answers the question better than any demo, including ours.

1. **Pick one real assessment** with a fully described rubric. Twenty-five to forty submissions is enough to see a pattern.
2. **Use a test course and submissions you are allowed to use,** within your policy and each vendor's data agreement.
3. **Record the instructor's grades first.** Otherwise you measure agreement with a number they have already seen.
4. **Run Canvas Grading Assistance** and note the pre-selected rating per criterion before editing.
5. **Run the dedicated tool** on the same submissions and rubric.
6. **Compare per tool:** average points difference from the instructor, share of criteria where the rating matches, share of comments sent unedited, and minutes per submission including review.
7. **Add a second grader if you can.** If two instructors differ more than either tool does, consistency is a bigger problem than speed.

| Criterion (max points) | Instructor's grade | Suggested grade | Difference |
|---|---|---|---|
| Thesis and argument (30) | 22 | 25 | 3 |
| Use of evidence (30) | 18 | 21 | 3 |
| Application to practice (25) | 20 | 19 | 1 |
| Writing and structure (15) | 12 | 12 | 0 |
| **Total (100)** | **72** | **77** | **5 on the total, 7 across criteria** |

*Table 4: Worked example for one submission, with illustrative numbers, not a measurement of either tool.*

The totals are 5 points apart, but criterion by criterion the gap is 7, because one criterion went the other way. A tool that is close on totals but off on criteria writes comments that praise the wrong thing, and students read the comments. Track both.

If the Canvas assistant lands within a few points of your instructors and they rarely rewrite its comments, you have your answer at no extra cost. If it is close on totals but far on criteria, or your instructors disagree with each other more than with either tool, a dedicated tool deserves a proper pilot with success criteria agreed up front. Our [guide to AI grading tools](/resources/blog/ai-grading-tools-higher-education-guide) covers what else to compare.

## Frequently asked questions

**Does Canvas have AI grading?**
Yes. Since April 18, 2026, Canvas includes IgniteAI Grading Assistance for SpeedGrader, which suggests a rating and comment per rubric criterion on text-based submissions. It is off by default, so your Canvas admin has to enable it. The instructor reviews and submits every assessment; Canvas does not release AI grades on its own.

**Is the Canvas AI grading assistant free?**
It depends on your Canvas package. Instructure's guide says Grading Assistance is included with Canvas Plus and Canvas Next. In the pages we read, Instructure publishes no separate price for the feature, so check your package with your account team before planning a rollout.

**Do students see that AI helped grade their work?**
Yes. In Canvas, students see an AI-Assisted label on the Grades page and the assignment page. Eduface's interface uses a "Lecturer + AI" label to make clear that each feedback point was reviewed by the instructor before the student sees it. Either way, say in the syllabus how AI is used in grading.

**Can the Canvas grading assistant grade math or multiple-choice answers?**
No, not reliably. Instructure says it is not well-suited for objective, single-correct-answer assignments, and Canvas quizzes already score multiple-choice questions automatically. For open exam answers, Eduface's Exam Grader grades open and closed answers and flags those where its independent agents disagree.

**Can we use Canvas's grading assistant and Eduface in the same course?**
Yes, split by assignment: Grading Assistance in SpeedGrader for weekly reflections, Eduface (an LTI 1.3 external tool) for the major paper or final exam. Grading Assistance saves its assessment in SpeedGrader, and Eduface returns approved grades to the Canvas Gradebook, so both end up in Canvas.

## References

1. Instructure. (2026, February 18; updated March 18, 2026). *IgniteAI Grading Assistance for SpeedGrader: Feature Overview*. Instructure Community. https://community.instructure.com/en/discussion/664877/igniteai-grading-assistance-for-speedgrader-feature-overview (read October 5, 2026). [Key finding: generally available April 18, 2026, all customer types, globally; requires "Performance and usability upgrades for SpeedGrader"; off by default; root account, sub-account or course level; staff reply of March 3, 2026: only available when an institution's admin enables it.]
2. Instructure. (2026, updated September 25). *How do I use the IgniteAI Grading Assistance for SpeedGrader?* Instructure Community, Canvas guides. https://community.instructure.com/en/kb/articles/664423-how-do-i-use-the-igniteai-grading-assistance-for-speedgrader (read October 5, 2026). [Key finding: included with Canvas Plus and Canvas Next; Enhanced Rubrics required; text entry and PDF or DOCX only; seven limitations; instructor must review and approve; AI-Assisted label for students.]
3. Instructure. (2026, revision July 27). *AI Nutrition Facts: Grading Assistance*. IgniteAI Nutrition Facts. https://instructure.ai/nutritionfacts/?id=canvasgradingassistance (read October 5, 2026). [Key finding: Claude Haiku 4.5 via Instructure's AI platform; not trained with user data; retained for the life of the request; full response logged in the Canvas database; regions Virginia, Oregon, Dublin, Frankfurt, Sydney; suggestion selected by default.]
