---
title: "Turnitin AI Detection Accuracy: What the Score Means and What to Do With It"
seo_title: "Turnitin AI Detection Accuracy: What Scores Mean | Eduface"
meta_description: "How accurate is Turnitin AI detection? What the score means, the false positive math, who gets flagged, and a score-to-action protocol for instructors."
slug: turnitin-ai-detection-accuracy
primary_query: "turnitin ai detection accuracy"
secondary_queries: ["is turnitin ai detection accurate", "turnitin ai score meaning", "turnitin ai detection false positive", "what to do with a turnitin ai score", "turnitin ai detection non native english", "turnitin ai detection percentage"]
type: regelgeving
category: Research
hub: /resources/blog/ai-plagiarism-detection-failing-higher-education
related: [/resources/blog/turnitin-vs-eduface, /resources/blog/ai-assessment-scale-aias]
review_by: 2027-04-19
status: concept
note: "Outline (gate skipped on Dante's word, 'write all 6'; readability brief 19-10-2026). Type: explainer with a working-method core. H2s: Turnitin's own claims / what the score means / independent evidence / the 1% math / who is at risk / score-to-action protocol / conversation script / evidence checklist / what detection is useful for / verification in the assignment and where Eduface fits / what to do next / FAQ. Information gain: score-to-action table per band, copy-ready conversation script, evidence checklist that does not use the score, false-positive math with labelled EXAMPLE numbers (plus the share-of-flags calculation), and the at-risk table built only from what the sources say. Sources opened 19-10-2026: Turnitin AI writing detection FAQ page (turnitin.co.uk), Turnitin CPO update (May 2023), Turnitin false positives blog (2023), Vanderbilt (16-08-2023), Liang et al. 2023 (arXiv v3 of the Patterns paper), Weber-Wulff et al. 2023 (arXiv preprint of the IJEI paper). guides.turnitin.com returned HTTP 403, so the current guide wording was not read."
components: "8 figures, 6 tables, 5 card grids, 7 callouts (1 copy-ready script). Card grids use the [CARDS: n] ... [/CARDS] notation, one item per line as '- **Title** | text'."
---

EYEBROW: TURNITIN · AI DETECTION ACCURACY

# Turnitin AI Detection Accuracy: What the Score Means and What to Do With It

*What Turnitin itself says about its AI writing score, what independent tests found, how many honest students a 1% false positive rate flags at your college, and a step-by-step protocol for what to do at every score.*

By Eduface · October 2026 · 28 min read · Written for instructors, academic integrity leads and program directors at private and for-profit colleges

You open a Similarity Report and the AI writing indicator says 38%. The paper is from a student who has been quiet all term, writes in English as a second language and turned in everything on time. Your syllabus says unauthorized AI use is a violation. Your dean wants integrity cases handled consistently, and you have no idea whether 38% means "probably cheated" or "probably fine."

> **Turnitin AI detection accuracy**
> Turnitin states that its AI writing detection has a document-level false positive rate below 1% for documents where it finds more than 20% AI writing, and a sentence-level false positive rate of about 4%. Below 20%, Turnitin shows an asterisk because the score is less reliable. Independent tests found Turnitin among the more accurate detectors but concluded that no detector tested was reliable enough to serve as evidence. Turnitin itself says the score should not be the sole basis for action. Use it to open a review, never to close one.

> **Key takeaways**
> - Turnitin claims under 1% false positives per document, only for documents scored above 20%, and about 4% per highlighted sentence.
> - A score is the share of qualifying prose that the model predicts is AI-written, not the share of the whole paper, and not a probability of misconduct.
> - At 1%, a college that checks 10,000 human-written papers a term flags about 100 of them. The fewer students who actually use AI, the larger the share of flags that are wrong.
> - Students writing in a second language, students who machine-translate their own work and short or formulaic submissions carry the most risk of a false flag.
> - Decide on evidence that does not depend on the score: drafts, version history, a short oral check and the citation trail.

[CARDS: 3]
- **What the number says** | Turnitin's own accuracy claims, how the score is calculated, what the asterisk and the gray indicator mean, and what independent studies found when they tested detectors.
- **What it means at your college** | The false positive math with worked numbers, and which students are most likely to be flagged for writing they did themselves.
- **What to do with it** | A score-to-action protocol, a copy-ready conversation script, an evidence checklist that ignores the score, and how to build verification into the assignment.
[/CARDS]

## How accurate is Turnitin's AI detection, according to Turnitin?

Turnitin reports a false positive rate below 1% at the document level, but only for documents where it detects more than 20% AI writing. That condition matters more than the headline. The figure describes how often a fully human-written document crosses the 20% line, not how often any score is wrong.

Turnitin explains the claim in its own words: "we might flag a human-written document as AI-written for one out of every 100 fully-human written documents."¹ To check it, Turnitin says it ran 800,000 academic papers written before ChatGPT's release through the detector in April 2023.¹ ²

The sentence-level figure is different, and it is the one you see when you open the report. Turnitin's Chief Product Officer wrote in May 2023 that the sentence-level false positive rate is about 4%: for every 100 highlighted sentences, about four may be human-written.² Turnitin added that 54% of those false positive sentences sat right next to actual AI writing, which is why it advises reading the highlights in context rather than one by one.²

There is also a trade-off in the other direction. To keep false positives low, Turnitin says it may miss about 15% of the AI-written text in a document: "if we identify that 50% of a document is likely written by an AI tool, it could contain as much as 65% AI writing."¹ The detector is tuned to under-flag rather than over-flag. That is the right choice for students, and it also means a low score is not a clean bill of health.

| Turnitin's claim | Level | What it means for you |
|---|---|---|
| False positive rate below 1%, for documents with more than 20% AI writing¹ | Document | About 1 in 100 fully human papers can cross the 20% line |
| False positive rate of about 4%² | Highlighted sentence | Some highlighted sentences in any report are human-written |
| Higher incidence of false positives below 20%, shown with an asterisk¹ ² | Document | A score under 20% is not a finding; Turnitin calls it less reliable |
| May miss about 15% of AI-written text in a document¹ | Document | A 50% score could mean up to 65%; a low score does not prove human authorship |
| Tested on 800,000 pre-ChatGPT papers, April 2023¹ ² | Validation | Turnitin's own test, not an independent one |

*Table 1: Turnitin's published accuracy claims, at the level each one applies to. The 1% claim does not apply below the 20% threshold.*

[FIGUUR: Two side-by-side panels titled "Two false positive rates, two different questions". Left panel, navy header "Document level": a stack of 100 small paper icons drawn as simple rectangles, 99 white and 1 amber. Label: "Fully human-written documents: about 1 in 100 may be scored above 20%". Footnote: "Applies only to documents with more than 20% AI writing detected". Right panel, navy header "Sentence level": a column of 100 short horizontal bars representing highlighted sentences, 96 grey and 4 amber. Label: "Highlighted sentences: about 4 in 100 may be human-written". Footnote: "Most sit next to actual AI writing (Turnitin, May 2023)". A thin strip under both panels: "Source: Turnitin's own published figures. Not independently verified."]
*Figure 1: Turnitin publishes two false positive rates; the 1% applies to whole documents above 20%, the 4% to individual highlighted sentences.*

> **What Turnitin itself says about the score**
> "The percentage on the AI writing indicator should not be used as the sole basis for action or a definitive grading measure by instructors." Turnitin also states that it "does not make a determination of misconduct" and that "the final decision on whether any misconduct has occurred rests with the reviewer/instructor."¹

## What does the Turnitin AI score actually mean?

The Turnitin AI score is the percentage of qualifying prose in a submission that the model predicts was generated by AI. It is not the percentage of the whole paper, and it is not the probability that the student cheated. Those are the two most common misreadings, and both push instructors toward a conclusion the number does not support.

"Qualifying" does real work in that sentence. Turnitin only analyzes long-form prose: sentences in paragraphs. Lists, bullet points, poetry, scripts, code and annotated bibliographies are left out, so the percentage and the highlighted text do not always line up.¹

### How Turnitin calculates the number

Turnitin breaks each submission into overlapping segments of a few hundred words, about five to ten sentences each. Every sentence gets a score between 0 (human) and 1 (AI). The model averages those scores into one prediction for the document.¹

[FLOWDIAGRAM] 1 Submission (at least 300 words of prose; .docx, .pdf, .txt or .rtf) → 2 Filter (only long-form prose sentences count; lists, code, bibliographies are left out) → 3 Segments (overlapping blocks of a few hundred words, five to ten sentences) → 4 Sentence scores (each sentence scored from 0 = human to 1 = AI) → 5 Document percentage (average across segments = share of qualifying prose predicted to be AI)
*Figure 2: The score is an average of sentence predictions over qualifying prose, which is why it can differ from the share of text that is highlighted.*

Short papers behave differently. Turnitin notes that in a document of only a few hundred words, the prediction is "mostly 'all or nothing'" because there is only one segment and no overlap, so a paper mixing original and AI text "could be flagged as entirely AI-generated."¹

### What the indicator shows

The indicator in the Similarity Report has four states, and only one of them is a usable number.¹

[FIGUUR: Four indicator chips in a row, each with a short label underneath, drawn as rounded pills. Chip 1, blue, "38%": "Processed. Share of qualifying prose predicted to be AI." Chip 2, blue with an asterisk (*): "Below 20%. Turnitin marks the score with an asterisk: less reliable, higher incidence of false positives." Chip 3, grey, "- -": "Not processed. Under 300 words of prose, wrong file type, or submitted before detection was available." Chip 4, grey with "!": "Error. Processing failed; try again." Under chips 2 to 4 a bracket labelled "Not a finding". Under chip 1 a bracket labelled "A reason to look, not a conclusion".]
*Figure 3: Of the four indicator states, three tell you nothing about authorship, and the fourth only tells you where to look.*

A few other facts change how you should handle a report. Students cannot see the AI indicator, though instructors can download the AI report as a PDF and share it.¹ Turnitin's FAQ says AI-paraphrased text, such as text run through a paraphrasing tool, is presented as likely AI-generated, without a separate label in the report.¹ Turnitin's FAQ also says the detector processes long-form English, and that non-English papers get no report; Turnitin has extended language support over time, so check the current guide for your account.¹ Finally, administrators can switch the feature off for the whole institution.¹

[CARDS: 2]
- **What the score is** | A model's prediction of how much qualifying prose looks AI-generated, averaged over overlapping segments, with known error rates that Turnitin publishes and asks you to account for.
- **What the score is not** | A measure of the whole paper, a probability of misconduct, a judgment about whether AI use was allowed on this assignment, or evidence a student can see and answer without your help.
[/CARDS]

## Is Turnitin AI detection accurate in independent tests?

Independent testing places Turnitin among the more accurate AI detectors, while concluding that none of the tools tested is reliable enough to be used as evidence of misconduct. Both halves of that sentence come from the same study, and you need both.

In 2023, a team of eight researchers led by Debora Weber-Wulff tested 14 detection tools, including Turnitin, on 54 test cases they wrote themselves.³ Turnitin scored highest on every accuracy measure they used. Yet the authors found that even the highest accuracy values were below 80%, and concluded that the tools are "neither accurate nor reliable."³

Two findings from that study matter for any college with international or multilingual students. Human-written text was classified correctly 96% of the time on average, but when the researchers took human writing in another language and machine-translated it into English, accuracy dropped by 20%.³ The authors warn that this leaves second-language students "at risk of being falsely accused" when they translate their own work.³ Lightly editing AI text by hand also cut detection sharply, from 74% for unedited AI text to 42% for edited text.³

A second study looked at bias directly. Researchers at Stanford, led by Weixin Liang, ran 91 TOEFL essays written by non-native English speakers and 88 essays by US eighth-graders through seven widely used detectors.⁴ The detectors were near-perfect on the US essays. On the TOEFL essays, the average false positive rate was 61.22%; all seven detectors flagged 19.78% of them as AI-written, and 97.80% were flagged by at least one.⁴

Turnitin was not one of the seven detectors in the Liang study, so the 61% figure is not a Turnitin number. The mechanism still applies to any detector that leans on how predictable the wording is. The flagged essays had significantly lower "perplexity," a measure of how predictable each next word is, and when the researchers had ChatGPT enrich the vocabulary of the same essays, the false positive rate fell from 61.22% to 11.77%.⁴ Turnitin describes its own model in similar terms: it is trained to detect differences in "word probability," because AI tends to pick "highly probable" next words.¹ Turnitin also says it included second-language learners in its training data to reduce bias.¹

[FIGUUR: Horizontal bar chart titled "Seven detectors, two groups of human writers (Liang et al., 2023)". Bar 1, navy, "US eighth-grade essays (n = 88)": near zero, labelled "near-perfect accuracy". Bar 2, amber, "TOEFL essays by non-native writers (n = 91)": 61.22%, labelled "average false positive rate". Side panel with three stat tiles: "97.80% flagged by at least one detector", "19.78% flagged by all seven", "11.77% after ChatGPT enriched the vocabulary". Footer in small type: "Turnitin was not among the seven detectors tested. The study shows a mechanism, not a Turnitin error rate."]
*Figure 4: Human essays written in simpler, more predictable English were flagged far more often, and enriching the vocabulary alone cut the false positive rate by about 49 points.*

| Source | What was tested | Key finding | What it means for you |
|---|---|---|---|
| Turnitin (2023)¹ ² | Turnitin, on 800,000 pre-ChatGPT papers | Below 1% document false positives above 20%; about 4% per sentence | The vendor's own figure, with conditions attached |
| Weber-Wulff et al. (2023)³ | 14 detectors, including Turnitin, 54 test cases | Turnitin most accurate; no tool above 80%; machine translation cut accuracy on human text by 20% | Best of the field is still not evidence on its own |
| Liang et al. (2023)⁴ | 7 detectors, not Turnitin; TOEFL vs US eighth-grade essays | 61.22% average false positives on non-native writers; near zero on native writers | Predictable wording drives false flags; check who is being flagged |
| Vanderbilt University (2023)⁵ | Institutional decision after months of use | Disabled Turnitin's AI detector for the foreseeable future | Some colleges judged the risk not worth it |

*Table 2: Turnitin's own figures next to the independent evidence. The studies differ in tools and dates; read each finding with its context.*

Vanderbilt's reasons are worth reading because they are the reasons an integrity lead will hear in a committee. In August 2023, Vanderbilt said the feature had been switched on with less than 24 hours' notice, could not be disabled at launch, and came with no detailed explanation of how it decides that writing is AI-generated.⁵ It also cited research that detectors are more likely to flag non-native English writers, and raised privacy concerns about sending student work to separate detection services.⁵ Turnitin's FAQ now states that institutions can disable the feature, so the first two reasons describe the 2023 launch more than today's settings.¹

## What does a 1% false positive rate mean at your college?

A 1% false positive rate means about one human-written paper in every hundred gets flagged, and at college scale that is a lot of students. The percentage sounds small because it describes one paper. Your integrity office handles all of them.

Vanderbilt did this math for itself. It submitted 75,000 papers to Turnitin in 2022, and calculated that at a 1% false positive rate, "around 750 student papers could have been incorrectly labeled as having some of it written by AI."⁵

The same arithmetic works for a private college. All numbers below are an EXAMPLE, and they assume Turnitin's 1% rate holds for your students' writing, which is exactly what the independent studies question.

[FIGUUR: A grid of 100 small squares in 10 rows of 10, titled "EXAMPLE: one term at a multi-campus college". Header stat: "10,000 human-written papers checked". Each square represents 100 papers. 99 squares in light grey labelled collectively "9,900 papers, no flag above 20%". 1 square in amber labelled "about 100 human-written papers flagged above 20%". To the right, three stacked stat tiles: "Per term: about 100 flagged papers", "Per year (three intakes): about 300", "Per instructor grading 400 papers a year: about 4". Footer: "All numbers EXAMPLE, at Turnitin's stated 1% document-level rate. Real rates for your students may be higher."]
*Figure 5: At Turnitin's own 1% rate, a college checking 10,000 human-written papers a term would see about 100 innocent flags, roughly four a year for an instructor who grades 400 papers.*

The harder question is what share of all flags are wrong, and that depends on how many students actually use AI where they should not. When few students do, false positives make up a larger share of the flags you see. The two scenarios below use EXAMPLE assumptions, including an EXAMPLE detection rate for AI-written papers, which is not a Turnitin figure.

| EXAMPLE assumption | Scenario A: AI misuse common | Scenario B: AI misuse rare |
|---|---|---|
| Papers checked, papers with substantial AI misuse | 10,000, of which 1,000 | 10,000, of which 200 |
| Flagged human papers (1% of human papers) | 90 | 98 |
| Flagged AI papers (EXAMPLE: 85% caught) | 850 | 170 |
| Share of all flags that are human-written | about 1 in 10 | about 1 in 3 (37%) |

*Table 3: The same 1% false positive rate produces very different odds per flag. In a course with little misuse, a flag is much more likely to be wrong.*

[FIGUUR: Two stacked horizontal bars, titled "EXAMPLE: of every flag you see, how many are wrong?". Bar A "AI misuse common (10% of papers)": 940 flags total, 850 navy segment "AI-written", 90 amber segment "human-written", label "about 1 in 10 flags is wrong". Bar B "AI misuse rare (2% of papers)": 268 flags total, 170 navy, 98 amber, label "about 1 in 3 flags is wrong". Footer: "Same detector, same 1% rate. Only the share of students misusing AI changed. All numbers EXAMPLE; the 85% catch rate is an assumption."]
*Figure 6: When misuse is rare, a flag is far more likely to land on an honest student, because the false positives stay while the true positives shrink.*

This is why a program that has redesigned its assessments, and expects little misuse, should trust individual flags less, not more. It is also why the 1% figure on its own cannot tell an instructor how likely it is that this particular student cheated.

## Who is most at risk of a false Turnitin AI flag?

Students whose writing is predictable, short, formulaic or translated are most at risk of being flagged for work they wrote themselves. Several of those risks come from Turnitin's own documentation, and the rest from the independent studies above.

That list maps closely onto many private and for-profit colleges. If your students include adult learners writing in a second language, career changers returning to academic writing after years away, or online students who draft in another language first, assume your false positive rate is higher than the vendor average until you have checked.

| Who | Why the risk is higher | Source |
|---|---|---|
| Students writing in English as a second language | Simpler, more predictable wording looks like AI to perplexity-based detectors | Liang et al.⁴; Vanderbilt⁵ |
| Students who machine-translate their own writing | Translation leaves traces that detectors read as AI; accuracy on human text fell by 20% | Weber-Wulff et al.³ |
| Short submissions of a few hundred words | One segment, no overlap: the prediction is "mostly all or nothing" | Turnitin¹ |
| Formulaic writing: lists without variation, repetition, paraphrase without new ideas | Turnitin names these as sources of false positives | Turnitin¹ |
| Introductions and conclusions | Turnitin found more false positives in the first and last sentences and changed its method | Turnitin¹ ² |
| Any score below 20% | Turnitin found a higher incidence of false positives and marks these with an asterisk | Turnitin¹ ² |

*Table 4: Who is most at risk of a false flag, using only what Turnitin and the studies report.*

[CARDS: 3]
- **Check the student, not only the paper** | Before you act on a flag, ask whether the student writes in a second language, drafts in another language, or has a documented accommodation. That is context for your review, not an excuse.
- **Check the assignment type** | Short reflections, lab write-ups with set phrasing and templated business reports produce predictable prose by design. A high score on a template says little.
- **Check your own pattern** | If flags in a course cluster among international or ESL students, treat that as a signal about the detector before you treat it as a signal about the students.
[/CARDS]

Grammar tools are a common worry. Turnitin says that in its initial tests, corrections made by grammar checkers to human-written text were in most cases not flagged as AI-written, while text produced by generative writing features inside those tools likely would be.¹ That is the vendor's statement, not an independent result, so ask students what tools they used rather than assuming either way.

## What should an instructor do at each Turnitin AI score?

At every score, the same rule applies: the number decides whether you look closer, and evidence you can show the student decides the outcome. The protocol below turns that rule into steps per score band. The bands are ours, built on Turnitin's 20% threshold; they are not Turnitin categories.

Before any band, check one thing: was AI use allowed on this assignment, and at what level? A paper that uses AI for planning on an assignment set at a planning level is not a violation, whatever the score. If your college uses the AI Assessment Scale, our guide to [making each level of the AI Assessment Scale hold](/resources/blog/ai-assessment-scale-aias) shows what evidence each level needs.

[FLOWDIAGRAM] 1 Check the assignment rules (was AI allowed, at what level?) → 2 Read the indicator state (number, asterisk, gray, error) → 3 Read the paper, not the percentage (compare with the student's earlier work) → 4 Gather evidence that does not use the score (drafts, version history, citation trail) → 5 Talk to the student (open questions about their own paper) → 6 Decide and record (on the evidence; the score is a footnote at most)
*Figure 7: The score enters at step 2 and leaves at step 3; every later step runs on evidence you can show the student.*

| Score band | What it tells you | What you do | What you do not do |
|---|---|---|---|
| Gray (- -) or error (!) | Nothing: the paper was not processed | Grade as normal; resubmit only if your policy requires a report | Treat a missing score as suspicious |
| Asterisk, below 20% | Turnitin calls this less reliable | Grade as normal; no follow-up on the score alone | Mention the score to the student or in a report |
| 20% to 39% (EXAMPLE band) | Some prose resembles AI; within reach of a false positive | Read the highlighted passages in context; compare with earlier work; follow up only if the paper itself raises questions | Open a case, lower the grade or ask for a confession |
| 40% to 79% (EXAMPLE band) | A substantial share of prose resembles AI | Check drafts and version history; check the citation trail; invite the student to talk about the paper | Decide before you have spoken to the student |
| 80% to 100% (EXAMPLE band) | Most qualifying prose resembles AI | Same as above, plus a short oral check on the paper; refer to the integrity process only with evidence beyond the score | Refer the score alone, or share it as proof |

*Table 5: A score-to-action protocol. Bands above 20% are EXAMPLE bands; agree your own with your integrity office and apply them the same way across sections.*

> **The rule that holds at every band**
> The score opens a review; it never closes one. If you could not explain your decision to the student without mentioning the percentage, you do not yet have enough to act on.

The value of a shared protocol is consistency. When three adjunct instructors teach the same course across two campuses, one should not refer a 35% paper while another ignores an 85% paper. A program director can fix that with one table and a short briefing.

## How should you talk to a student about a flagged paper?

Talk to the student about their paper, not about the score, and start from the assumption that they wrote it. Turnitin's own advice for these conversations is to "assume positive intent" and to acknowledge upfront that false positives happen, because ignoring that "will lead to a far more defensive and confrontational interaction."⁶

The script below is built for a 15-minute meeting or video call. It asks questions that a student who wrote the paper can answer easily and that are hard to bluff, and it never asks the student to explain a number they cannot see.

> **Copy-ready: conversation script for a flagged paper**
> **Opening.** "Thanks for meeting. I read your paper on [topic] closely and I'd like to understand how you put it together. This isn't an accusation. Some tools flag writing for review, and they get it wrong sometimes, so I want to hear from you before I decide anything."
>
> **Process.** "Walk me through how you wrote it. Where did you start, and how long did it take?" / "Do you have notes, an outline or earlier drafts? Did you write it in Google Docs or Word?" / "Did you use any tools along the way: grammar checkers, translation, AI? Our policy for this assignment allows [what was allowed]."
>
> **Content.** "In your second section you argue that [claim]. Can you explain that in your own words?" / "Why did you choose [source] here? What did you take from it?" / "If you had another week, what would you change?"
>
> **Close.** "Thanks, that helps. Here's what happens next: [I'll review your drafts / I'm satisfied and grading as normal / I need to refer this under our policy, and here's what that process looks like]. You'll hear from me by [date]."
>
> **Do not say:** "Turnitin says 62% of this is AI." / "Just tell me if you used ChatGPT." / "If you admit it now, it'll go easier."

Write down what the student says, the questions you asked and what they showed you. If the conversation settles it, the record protects both of you. If it does not, the record is what the integrity process needs, and the score is not.

[CARDS: 2]
- **Signs the student wrote it** | They explain the argument in their own words, recall why they chose sources, show notes or drafts, and can describe what was hard. Hesitation and nerves are normal and are not evidence.
- **Signs you need more evidence** | They cannot explain key claims, do not recognize sources they cited, have no drafts and no version history for a long paper, or describe a process that does not match the paper.
[/CARDS]

## What evidence counts if the Turnitin AI score does not?

Evidence that counts is evidence about the student's process and understanding, which you can show to the student and to a panel. The checklist below avoids the score entirely, which is also what Turnitin's guidance and the independent researchers point toward: Weber-Wulff and colleagues note that detectors "do not provide any evidence" and that their reports "cannot be used as the only basis" for reporting students.³

| Evidence | What it shows | How to collect it | Its limits |
|---|---|---|---|
| Draft history | The paper developed over time | Require an outline and a draft before the final | Drafts can be produced after the fact |
| Version history | Writing happened in steps, with revisions | Ask for Google Docs or Word version history | Not every student drafts in a cloud editor |
| Oral check | The student understands and can defend their own paper | Five to ten minutes of questions drawn from the paper | Nerves and language skills affect fluency; judge content |
| Citation trail | Sources exist and say what the paper claims | Check two or three citations against the originals | Honest students also make citation errors |
| Comparison with earlier work | The paper fits the student's level and voice | Compare with in-class writing or earlier submissions | Students improve; a jump is a question, not a finding |
| Notes and research materials | The thinking behind the paper | Ask for notes, annotated readings, search history | Absence of notes is weak evidence on its own |

*Table 6: An evidence checklist that does not rely on the AI score. No single item settles a case; several items pointing the same way can.*

[FIGUUR: A vertical evidence ladder titled "From weakest to strongest evidence", five rungs from bottom to top. Bottom rung, grey: "AI score alone (Turnitin: not a sole basis)". Rung 2, light grey: "Style differs from earlier work". Rung 3, light navy: "No drafts or version history for a long paper". Rung 4, navy: "Citations that do not exist or do not say what the paper claims". Top rung, dark navy: "Cannot explain or defend the paper's own argument in an oral check". A bracket on the right spanning rungs 3 to 5: "Combine two or more before you refer a case". A small note under the ladder: "Every rung is still a judgment. None is proof on its own."]
*Figure 8: The score is the weakest rung; an inability to explain one's own paper, combined with a missing process, is the strongest evidence an instructor can collect.*

A missing citation trail deserves special attention. Vanderbilt's guidance noted that AI tools can "generate whole sources out of nothing," and advised instructors to look for inaccuracies in sources, arguments and facts, and to compare the writing with the student's other work.⁵ A fabricated reference is something a student can see and respond to. A percentage is not.

> **For academic integrity leads**
> Write down your minimum evidence standard: for example, no referral on the AI score alone, and at least two pieces of process or understanding evidence for any case. Tell students in the syllabus what you may ask for (drafts, version history, a short conversation) so the request is routine, not a signal of suspicion. Then check twice a year whether flags and referrals cluster among second-language students. None of this is legal advice; your policy and your accreditor's expectations decide the final wording.

## What is AI detection actually useful for?

AI detection is useful for deciding where to look and for seeing patterns across a program; it is not useful for deciding what happened in a single case. That is a narrower job than most people buy it for, and an honest one.

Used for triage, a score can point an instructor with 200 papers toward the five worth reading closely. In the independent test above, Turnitin was the most accurate tool, and its design deliberately leans toward missing AI text rather than flagging human text.³ ¹ Turnitin also gives administrators aggregated AI scores for the institution, available since February 2024, which can show whether a redesigned assessment changed anything.¹

[CARDS: 2]
- **Where detection helps** | Triage in large batches. Spotting a course where scores jump after an assignment change. Starting a conversation that you would have had anyway. Program-level patterns over a term, read alongside other data.
- **Where it does not** | Deciding a single case. Short or formulaic assignments. Papers by students writing in a second language without other evidence. Any situation where the student cannot see and answer what you are relying on.
[/CARDS]

Verification beats detection because it produces evidence about the student rather than a prediction about the text. A detector estimates whether prose looks machine-written; it cannot tell you whether the student understood the assignment, which is what the grade is supposed to certify. A short conversation about the paper answers that question directly, and the answer holds up whichever tool, or which future model, the student used. For the longer argument, see [why AI plagiarism detection is failing higher education](/resources/blog/ai-plagiarism-detection-failing-higher-education).

## How do you build verification into the assignment instead?

You build verification in by making the writing process visible and adding a short oral moment, so you are not reconstructing evidence after a flag. Both steps cost less time when they are designed into the assignment than when you add them to one suspicious paper.

Three changes cover most of it. Require at least one draft before the final, with feedback on it, so there is a process to look at. Ask students to write in an editor with version history, and say in the syllabus that you may ask to see it. Add a five-minute oral check for a sample of students on every major paper, not only the flagged ones, so being asked is routine.

This is where Eduface fits, and it is worth being plain about what Eduface is. Eduface is not an AI detector. It does not score text for the likelihood that AI wrote it. It offers two routes to the kind of evidence described above.

[CARDS: 2]
- **Draft-by-draft feedback (Paper Grader)** | The Paper Grader's formative feedback runs over a first draft, a second draft and the final version, with comments tied to your rubric. Student progress is tracked across successive drafts, so the writing process is on record before anyone asks. You choose whether feedback goes to the student directly or after you approve it.
- **Oral questions on the student's own paper (Academic Integrity, beta)** | Academic Integrity asks the student critical questions about their own paper, which they answer orally, as in a thesis defense. A student who wrote the paper can usually explain it. It is in beta, so pilot it on one course first.
[/CARDS]

If your college already licenses Turnitin, the two do not compete for the same job. Turnitin answers where a text may have come from; Eduface helps with feedback, grading and verification. Our comparison of [Turnitin vs Eduface](/resources/blog/turnitin-vs-eduface) covers the overlap and how colleges use both.

> **What Eduface doesn't do**
> Eduface does not detect AI writing and does not prove who wrote a paper; no tool does. Academic Integrity is in beta. A student who has rehearsed answers about a paper they did not write may still get through a short oral check, so the outcome is evidence for the instructor to weigh, not a verdict. The instructor decides.

## What to do next

Pick the actions that fit your role. Each one takes less than a week.

1. **Instructors: check the assignment rules before the score.** For your next batch, confirm what AI use was allowed, then use the score only to decide which papers you read more closely.
2. **Instructors: keep the conversation script ready.** Save the script above, fill in your policy wording, and use it for every flagged paper so every student gets the same conversation.
3. **Program directors: agree the score bands once.** Adopt the score-to-action table, or your own version, across all sections and campuses, and brief adjunct instructors on it at the start of each intake.
4. **Integrity leads: set a minimum evidence standard.** Put "no referral on the score alone" in writing, list the evidence you accept, and review twice a year whether flags cluster among second-language students.
5. **Course leads: design the evidence in.** Add one required draft, version history and a short oral check for a sample of students on your next major assignment.

## Frequently asked questions

**Is Turnitin AI detection accurate?**
It is among the more accurate detectors, and still not accurate enough to prove misconduct. Turnitin reports a document-level false positive rate below 1% for documents with more than 20% AI writing, and an independent 2023 test ranked it first of 14 tools while finding no tool above 80% accuracy. Use the score to decide where to look, not what happened.

**What does the asterisk on a Turnitin AI score mean?**
It means the score is below 20% and Turnitin considers it less reliable. Turnitin found a higher incidence of false positives in that range and added the asterisk to call attention to it. Treat an asterisked score as no finding.

**Can Turnitin AI detection be wrong?**
Yes. Turnitin itself says its false positive rate is not zero: about 1 in 100 fully human documents at the document level, and about 4 in 100 highlighted sentences. Independent research has found higher false positive rates for writing by non-native English speakers and for machine-translated human text.

**Can students see their Turnitin AI score?**
No, not by default. Turnitin states that the AI writing indicator and report are visible only to instructors and administrators, though instructors can download the AI report as a PDF and share it. If you discuss a flag with a student, talk about the paper rather than a number they have not seen.

**What percentage of AI on Turnitin is acceptable?**
There is no acceptable percentage, because the score does not measure whether AI use was allowed. An assignment that permits AI for planning can produce a high score without any violation, and a low score does not prove the work is the student's own. Your assignment rules decide what is acceptable; the score only shows where to look.

**Does Turnitin flag non-native English speakers more?**
Turnitin says it trained its model with second-language writers included to reduce bias. Independent research shows the risk is real for detectors of this kind: in a 2023 Stanford study of seven other detectors, essays by non-native writers were wrongly flagged 61% of the time on average. Check whether flags in your courses cluster among these students.

**Can a college turn off Turnitin's AI detection?**
Yes. Turnitin states that administrators can enable or disable AI writing detection in their admin settings, which removes the indicator and report for instructors. Vanderbilt University disabled it in August 2023 and published its reasons.

## References

<!-- OPEN POINT for Dante: guides.turnitin.com and help.turnitin.com returned HTTP 403 to automated fetches on 19-10-2026. Facts above come from Turnitin's public AI writing detection FAQ on turnitin.co.uk and two Turnitin blog posts, all read in full that day. The FAQ still describes English-only detection and an asterisk "for percentages less than 20"; Turnitin's current guides may describe more languages and a different low-score display (search snippets mention "*%" for 1 to 19% since July 2024). Open the current guide in a browser before publishing and update the "What the indicator shows" paragraph if it differs. -->

1. Turnitin. *AI writing detection: frequently asked questions* (product feature page). turnitin.co.uk/products/features/ai-writing-detection. Accessed October 19, 2026. [Key finding: the percentage is the share of qualifying long-form prose the model predicts was AI-generated; overlapping segments of a few hundred words, sentences scored 0 to 1; document false positive rate under 1% for documents with over 20% AI writing; may miss about 15% of AI text (50% could be up to 65%); asterisk for percentages below 20 because less reliable; at least 300 words of prose and .docx, .pdf, .txt or .rtf; short documents "mostly all or nothing"; lists, repetition and paraphrase without new ideas can cause false positives; AI-paraphrased text shown as likely AI-generated; English long-form; not visible to students, PDF download available; admins can disable; aggregated institution scores since February 13, 2024; score "should not be used as the sole basis for action"; final decision rests with the instructor.]
2. Chechitelli, A. (2023, May). *AI writing detection update from Turnitin's Chief Product Officer.* Turnitin blog. turnitin.co.uk/blog/ai-writing-detection-update-from-turnitins-chief-product-officer. Accessed October 19, 2026. [Key finding: 800,000 pre-ChatGPT papers tested; higher incidence of false positives below 20%, so an asterisk was added; minimum raised from 150 to 300 words; more false positives in first and last sentences; document false positive rate under 1% above 20%; sentence-level rate about 4%, with 54% of false positive sentences right next to actual AI writing.]
3. Weber-Wulff, D., Anohina-Naumeca, A., Bjelobaba, S., Foltýnek, T., Guerrero-Dib, J., Popoola, O., Šigut, P., & Waddington, L. (2023). Testing of detection tools for AI-generated text. *International Journal for Educational Integrity, 19*, 26. doi.org/10.1007/s40979-023-00146-z. Read via the arXiv preprint (arXiv:2306.15666), October 19, 2026. [Key finding: 14 tools including Turnitin, 54 test cases; Turnitin scored highest on all accuracy measures, but no tool reached 80% accuracy; tools "neither accurate nor reliable"; 96% accuracy on human text fell by 20% for machine-translated human text; manual editing cut detection from 74% to 42%; detectors provide no evidence and their reports cannot be the only basis for reporting students.]
4. Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. *Patterns, 4*(7), 100779. Read via arXiv:2304.02819v3, October 19, 2026. [Key finding: seven detectors, not including Turnitin; 91 TOEFL essays and 88 US eighth-grade essays; near-perfect accuracy on US essays; average false positive rate of 61.22% on TOEFL essays; 19.78% flagged by all seven and 97.80% by at least one; enriching vocabulary with ChatGPT cut the rate to 11.77%; flagged essays had lower perplexity.]
5. Vanderbilt University, Brightspace and Instructional Technology Support. (2023, August 16). *Guidance on AI detection and why we're disabling Turnitin's AI detector.* vanderbilt.edu/brightspace/2023/08/16/guidance-on-ai-detection-and-why-were-disabling-turnitins-ai-detector. Accessed October 19, 2026. [Key finding: disabled for the foreseeable future; enabled with less than 24 hours' notice, no option to disable at launch, no insight into how it works; 75,000 papers in 2022 would mean around 750 incorrectly labeled at 1%; detectors more likely to flag non-native English writers; privacy concerns; advice to compare with the student's other work, check sources for fabrication, and talk to the student.]
6. Turnitin. (2023). *Understanding false positives within our AI writing detection capabilities.* Turnitin blog. turnitin.co.uk/blog/understanding-false-positives-within-our-ai-writing-detection-capabilities. Accessed October 19, 2026. [Key finding: Turnitin does not make a determination of misconduct; tips to plan for false positives in advance, "assume positive intent," and acknowledge false positives upfront to avoid a "defensive and confrontational interaction."]
