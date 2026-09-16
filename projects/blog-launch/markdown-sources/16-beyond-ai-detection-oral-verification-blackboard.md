# Beyond AI Detection: Verifying Student Work With Oral Follow-Up Questions in Blackboard

*By Eduface Team · July 2026 · 8 min read*

Institutions have spent several years now in a detection arms race that nobody is winning: a new checker gets deployed, students adapt, and the cycle repeats without ever settling the underlying question of whether a submission genuinely reflects what a student understands. Some have responded by retreating to supervised, pen-and-paper exams, a defensible short-term fix that quietly narrows what's actually being assessed back down to recall and handwriting speed. Our companion piece on Moodle covers why detection tools specifically are the wrong lens for this problem in the first place, and makes the case for verification, asking a student to account for their own work, instead. This piece stays closer to the mechanism itself: why asking someone unplanned follow-up questions about a piece of writing actually works as a test of authorship, and what that means for setting it up in Blackboard specifically.

## The cognitive reason this actually works

There's a genuinely old, well replicated finding in cognitive psychology that explains why this approach is so hard to fake. Norman Slamecka and Peter Graf's 1978 research demonstrated what's now called the generation effect: people remember information they generated themselves substantially better than information they simply read or were given (Slamecka & Graf, 1978). The gap isn't small. A meta-analysis of subsequent studies found generated information remembered roughly half a standard deviation better than material that was merely read, a genuinely large and consistent effect across dozens of replications.

Apply that to a submitted assignment. A student who worked through a specific argument themselves, who chose which source to cite and why, who made a specific methodological decision partway through, has a rich, generated memory trace of those choices. A student who copied, or had AI produce, the same content has, at best, a read memory trace of it, thinner, less connected to the specific reasoning, and far more vulnerable to collapsing under an unexpected, specific follow-up question that a plagiarism checker or an AI detector would never think to ask.

## Why this beats detection on its own terms

AI detection tools try to answer a fundamentally different, and considerably harder, question: was this text produced by a machine. That question turns out to be genuinely difficult to answer reliably. A 2025 evidence synthesis in the journal Information reviewed peer-reviewed literature on commercial AI detectors and found frequent false positives and a consistent lack of transparency about how scores are calculated, with the problem worse still for multilingual and non-native English writers, whose more formulaic sentence structure gets mistaken for machine output more often than it should (MDPI Information, 2025). Published false positive rates across different tools and studies have ranged from single digits up into the 30% region, which is a serious problem when a false accusation can end up in a formal misconduct process that follows a student for years. Integrity Check mode sidesteps that question entirely. It doesn't try to detect anything about the text itself. It reads the student's specific submission and generates follow-up questions that only someone with a genuine, generated memory trace of writing it, in Slamecka and Graf's sense, could answer fluently: what case did you cite to support this specific claim, and why did you choose it over the alternative.

That reframes the whole exercise from a probabilistic guess about text origin into a direct, low-stakes conversation a student who did the work can simply have.

## What this looks like set up in Blackboard

Integrity Check mode works across both Blackboard Learn and Blackboard Ultra, which matters for institutions currently mid-migration between the two interfaces, since the LTI 1.3 integration doesn't require picking one or the other. A lecturer configures the session by linking it to a specific student submission, and Eduface reads that submission and generates questions unique to it, specific arguments, specific cited sources, specific methodological choices, rather than generic questions that could apply to any essay on the topic. Every question pulled is traceable to a specific part of the student's own document.

The student completes a short spoken session, usually fifteen to twenty minutes, and the full transcript is returned to the lecturer alongside the outcome, so the decision about what happens next always sits with a human, not with an automated flag. As with Eduface's other Blackboard integrations, setup runs through LTI 1.3 with no separate plugin, and a first session is typically live within 48 hours.

## Where this fits alongside an existing academic integrity policy

Integrity Check isn't a replacement for your misconduct process, it's an earlier, more accurate input into it. Most institutions' existing policies were built around detection evidence, a similarity score, an AI detection percentage, which is exactly the evidence type most vulnerable to false positives and hardest for a student to meaningfully contest. A transcript showing a student unable to account for specific choices in their own submission is a fundamentally different, and considerably more defensible, kind of evidence to bring into a formal conversation, precisely because it's about what the student can demonstrate now, not a probabilistic guess about how the text was originally produced.

## FAQ

**Why don't AI detectors work reliably for catching AI-generated submissions?**
Because the statistical gap between AI-generated and human-written text keeps narrowing as models improve, and detectors have to trade off false positives against false negatives with no reliable way to eliminate both. Published false positive rates vary widely by tool and study, but the consistent finding is that no detector is accurate enough to be used as the sole basis for an accusation.

**Does Integrity Check mode work the same way in Blackboard Learn and Blackboard Ultra?**
Yes. The LTI 1.3 integration runs across both interfaces, which is useful for institutions currently migrating between them.

**Is this the same as running an AI detector on a submission?**
No, and that's the whole point. It doesn't estimate whether text was AI-generated. It generates specific follow-up questions from the submission itself and checks whether the student can account for their own reasoning.

**What happens to the outcome of an Integrity Check session?**
The full transcript is returned to the lecturer. There's no automated flag or score that triggers a process on its own, the decision about what to do next stays with a human.

**Why does this work better than a plagiarism or AI detection score?**
Because it's based on a well established memory effect: people recall and can elaborate on information they generated themselves far better than information they merely read or copied, which makes genuine authorship easy to demonstrate and difficult to fake.

## Sources

- Slamecka, N. J., & Graf, P. (1978). The Generation Effect: Delineation of a Phenomenon. *Journal of Experimental Psychology: Human Learning and Memory*, 4(6), 592-604.
- MDPI *Information* (2025). Evaluating AI Detection Tools in Higher Education: A Qualitative Evidence Synthesis, Vol. 16.
