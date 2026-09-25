# UTI demo video, voice-over script

_Draft, 2026-09-25. Voice-over for a screen recording in Blackboard Ultra. Audience: UTI and Concorde leadership, and UTI IT. Robert wants to share it with campus leaders in early October (his email of 21-09). Jeroen told him it comes with the deck this week (email 22-09)._

**How to use it**
- Plain text is what you say.
- **▶ CLICK** lines are what you do on screen. They describe the action; the exact button names go in once the demo is built.
- _source:_ lines are for you. Don't read them out.
- About 5 minutes at a relaxed pace, 4 without the optional blocks.

---

## 1. Intro (30 sec)

Hi, I'm Dante Torbed, Customer Success Manager at Eduface.

In this video you'll see one of your own labs graded twice inside Blackboard. First the way instructors grade it today, then with Eduface.

Eduface grades student work against your own answer key and writes feedback on every question. The instructor checks it, changes what they disagree with, and approves it. The AI assists, the instructor decides.

_source: product.md (Exam Grader, "The AI assists. The academic decides."). The lab is UTI's own material, sent by Robert on 28-08._

## 2. How a lab gets graded today (1 min)

**▶ CLICK** Open the course and go to [LAB NAME].

This is [LAB NAME], a lab from your HVACR program. The student fills in the lab document and uploads it here.

**▶ CLICK** Open one student's submission.

**▶ CLICK** Open the answer key next to it.

The instructor reads every answer, checks it against the key, and adds up the points.

**▶ CLICK** Enter the grade and post it.

Robert's team explained why these labs are graded by hand. Blackboard's autograding needs an exact match with the answer key, so one character off and a correct answer is marked wrong. That leaves instructors with two to four hours of grading a day, on top of eight to ten hours of teaching, mostly in the evening.

_source: Robert, meetings 26-08 and 01-09 (Close)._

So what the student gets back is mostly a score, and the feedback happens out loud, in the lab.

_source: Robert 26-08 ("minimal written feedback"), go-live plan summary._

## 3. The same lab with Eduface (1.5 min)

**▶ CLICK** Go back to the same assignment, now with Eduface on it.

Same course, same lab, same student. The instructor sets Eduface up once per assignment: the answer key, plus instructions for how the feedback should sound.

_source: product.md, "Hoe de opzet werkt"; go-live plan: without a rubric the model works from the answer key._

**▶ CLICK** Open the submission in Eduface.

Eduface has already read it. For every question you see the proposed points and a short explanation of what's right and what's missing.

**▶ CLICK** Open a question where the student used different words than the key. _(Pick one before recording. No such answer in the demo? Drop this beat.)_

Here the student gave the right answer in their own words. The autograder would have marked it wrong. Eduface gives the points and explains why.

**▶ CLICK** Open a question Eduface flagged as uncertain.

Where the model isn't sure, it flags the question. That tells the instructor where to look first.

_source: product.md, "markeert waar hij onzeker is"._

**▶ CLICK** Change the points on one question, then approve.

The instructor can change any grade or comment. Here, nothing reaches the student until the instructor approves it. For practice work, UTI can also choose to send feedback straight to the student.

_source: product.md, instellingen kiezen direct of na goedkeuring. Robert asked for instant formative feedback on 26-08._

**▶ CLICK** Open the Blackboard Gradebook.

The approved grade and the feedback land in the Gradebook, where they always go. Nobody copies grades over by hand.

_source: product.md, cijfer terug naar het gradebook; go-live plan Q&A (Jeroen)._

**▶ CLICK** Switch to the student view.

This is what the student sees: the grade, plus written feedback on every question to work from before the next lab.

### Optional: a Concorde example (30 sec)

_Only if the demo includes the Medical Assisting SOAP note. Robert asked for a healthcare example next to the HVACR one (email 22-09)._

**▶ CLICK** Open the SOAP note assignment and one submission.

It works the same way on written assignments, like this SOAP note from Medical Assisting. Eduface scores it per criterion on your assessment form and ties each comment to the passage it's about. For health programs it uses our health sciences model, trained on the conventions of that field.

_source: product.md, Paper Grader + zes vakmodellen (Health Sciences)._

## 4. What changes for leadership (40 sec)

For leadership, three things change.

Instructors get grading time back. How much time that is at UTI is what the proof of value will measure. Robert's team also told us this workload makes it harder to hire and keep instructors, because the field pays more and doesn't come with grading at night.

_source: Robert 01-09 (Close summary), go-live plan summary._

Students get written feedback on every lab, where today they mostly get a score.

And every grade comes with a written reason, so what students were told is on record.

**▶ CLICK** _(optional)_ Open the grader comparison dashboard.

The grader comparison dashboard shows at a glance where one instructor's grading drifts from the rest of the team.

_source: product.md, grader comparison dashboard; shown by Jeroen on 01-09._

## 5. The technical side, for IT (40 sec)

For IT, the technical side.

Eduface connects to Blackboard Ultra over LTI 1.3. Our engineer sets up the connection together with your Blackboard administrator. Approved grades and feedback sync back to the Gradebook automatically.

_source: go-live plan Q&A (Jeroen) and the planned step "LTI 1.3 connection: UTI IT and SR"._

We run our own model, not an API from OpenAI or any other AI provider. Student work is never sent to outside AI providers and never used to train outside models. It's encrypted in transit, access is set per role, and every graded assessment keeps an audit trail.

_source: product.md, "Hoe het model getraind is" + "Verantwoorde AI en gegevensbescherming"._

Eduface meets WCAG 2.2 AA, and your Legal and IT teams have had the VPAT since early September. Eduface also works in Canvas, if UTI moves there later.

_source: VPAT sent 02-09; go-live plan Q&A on Canvas._

## 6. Close (20 sec)

The next step we're planning with Robert is a proof of value in HVAC 101. Instructors grade real student work with Eduface in their own Blackboard course, and we measure the two things UTI asked for: the time it saves, and how close Eduface's grades come to the instructors' own.

_source: Robert 01-09, pilot in HVAC 101 with accuracy and workload as the success measures._

Thanks for watching. Questions can go to Robert, or straight to me.

**▶ ON SCREEN** dante.torbed@eduface.me

---

## Left out on purpose

- **94% accuracy.** That's the Bath Spa pilot, on written work. It's no proof for short-answer labs against an answer key (flagged as a risk in the sales-coach deal file).
- **"Significantly reduce grading time" and "improve student outcomes".** Nothing measured at UTI yet, and product.md says never to promise outcomes. The close points to the proof of value instead, because that's where the time saving gets measured.
- **"The system behind it is a bit more complex".** To IT that sounds like something is being skipped. Section 5 replaces it.
- **Cross-campus data.** Still roadmap (Jeroen, 01-09). Don't show it or promise it.
- **Length and dates of the proof of value.** The sources disagree (2, 4 and 12 weeks) and nothing is signed yet.

## To fill in once the demo is built

- [LAB NAME] and the click path per ▶ line. A screenshot of each step is enough to write in the exact buttons.
- Which beats the demo can actually show: the answer in different words, the uncertainty flag, the dashboard, the student view, the SOAP note.
- Blackboard quizzes: Bas asked about them on 21-09 and Jeroen confirmed by email that they sync. Not in product.md yet, so check with Samuel before it goes in the video.
