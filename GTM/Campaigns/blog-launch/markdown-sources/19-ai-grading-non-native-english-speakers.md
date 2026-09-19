# Does AI Grading Disadvantage Non-Native English Speakers?

*By Eduface Team · July 2026 · 9 min read*

This is a genuinely contested research question, not a settled one, and it deserves to be treated that way rather than flattened into a confident yes or no. The honest answer is that some studies find a real, measurable disadvantage, other well designed studies find none, and the difference often comes down to exactly what's being measured and how the underlying model was built and tested. If you're evaluating an AI grading tool and this matters to your student population, which for most institutions it does, it's worth understanding the actual shape of the evidence rather than a single headline.

## Where the concern comes from

The worry has a long history that predates generative AI by decades. Early automated essay scoring research at Educational Testing Service, developing what became known as e-rater, found that human-machine agreement on scoring generally sat around 92%, but with meaningful, documented variation across essays written by speakers of different first languages (Burstein et al., 1998). That's not a new finding invented by critics of modern AI. It's a pattern the automated scoring field has been studying and trying to correct for since the technology was first deployed at scale.

## What recent research actually finds

A 2026 study using contrastive learning techniques to examine bias in a transformer-based grading model found that high-proficiency essays written by second-language English learners received scores averaging 10.3% lower than native-speaker essays that had received identical quality ratings from human raters. That's a specific, measurable, concerning gap, and it points to a real mechanism: models trained predominantly on native-speaker writing can learn to associate certain surface-level linguistic patterns, more common in second-language writing regardless of the underlying quality of the argument, with lower quality generally.

At the same time, it would be inaccurate to present this as a universal, settled finding. Other rigorous studies looking at similar questions have found no significant bias. Research comparing automated scoring against teacher and expert human raters for English language learners has, in more than one case, found that automated systems didn't introduce new bias beyond what was already present in human scoring, and in some studies found no meaningful bias at all once other factors were controlled for. A related and important nuance comes from research on GPT-based scoring specifically, which found that while the model showed high internal consistency, it also showed range compression at the upper end of the scale compared to human raters, a pattern that could disadvantage strong writers generally, native and non-native alike, in a way that's distinct from language-background bias specifically.

## Why the research disagrees with itself

The honest explanation is that "AI grading" isn't one system with one behaviour. Different models, trained on different data, evaluated with different methodologies, produce genuinely different results, and a finding from one study using one model on one dataset doesn't necessarily generalise to a different tool built differently. This is closely related to a pattern already well documented in the AI detection literature, where detectors have been shown to disproportionately flag non-native English writing as AI-generated because of similar surface-level features, formulaic phrasing, more constrained vocabulary, that a model trained mostly on native-speaker text can mistake for a quality or authenticity signal rather than recognising as a normal feature of second-language writing.

## What this means practically when evaluating a tool

Rather than asking a vendor a yes-or-no question about bias, which any vendor will comfortably answer "no" to, ask for the actual evidence: has the tool been specifically tested for score consistency across first-language groups, using human-rated benchmarks as the comparison, not just internal consistency measures. Ask whether the model's training data included substantial second-language and multilingual writing, or was built predominantly on native-speaker text with second-language performance treated as an afterthought. And ask what the tool does structurally to guard against exactly the surface-feature bias the research keeps identifying, criterion-based grading that separates argument quality from surface fluency is a meaningfully different design choice than a single holistic score, and it's worth asking which approach a given tool actually takes.

This connects directly to why mandatory human review matters here specifically, beyond the general compliance reasons covered in our companion piece on human-in-the-loop marking. If a systematic bias exists in a model's first-pass output, a genuine human review step, one where the assessor can see and evaluate the reasoning rather than just approving a number, is one of the few practical safeguards that can catch it before it affects a real grade.

## FAQ

**Is it settled that AI grading disadvantages non-native English speakers?**
No. The research is genuinely mixed. Some studies find a measurable disadvantage, others find none, and the difference often depends on the specific model, its training data, and how bias was measured.

**Why do studies disagree so much on this question?**
Because "AI grading" covers many different systems built and trained differently. A finding about one model on one dataset doesn't necessarily apply to a different tool.

**What should we actually ask a vendor about this?**
Ask for evidence of testing across first-language groups against human-rated benchmarks, what proportion of training data was second-language or multilingual writing, and whether the grading approach separates argument quality from surface fluency rather than producing one holistic score.

**Does human review help if a bias like this exists in the underlying model?**
Yes, provided the review is genuine rather than a formality. An assessor who can see the reasoning behind a grade, not just a final number, is positioned to catch a systematic pattern that a purely automated process would miss.

## Sources

- Burstein, J., Kukich, K., Wolff, S., Lu, C., & Chodorow, M. (1998). Automated Scoring Using a Hybrid Feature Identification Technique. Educational Testing Service.
