<!--
Referentieblog, door Dante geplakt op 25-09-2026. Letterlijk overgenomen, alleen de opmaak is naar markdown gezet.
Gebruik voor STIJL en OPBOUW. Niet als bron voor feiten of claims:
- de deadline "August 2026" is achterhaald (Digital Omnibus: 2 december 2027)
- Jisc/CHEST, HEAnet, "95% alignment", GPU in NL, blind/AI-visible mode staan niet in Platform/product.md (W7)
- de uitleg van art. 13 als plicht richting studenten is juridisch te toetsen, zie ../stijl.md
-->

EYEBROW: (niet meegegeven)

# The EU AI Act and Higher Education: What Institutions Need to Know About Assessment Tools

*The EU AI Act classifies AI used in academic assessment as high-risk. Compliance obligations land from August 2026. Here is what every institution deploying AI assessment tools needs to understand before the deadline.*

Eduface · 7 min read · Written for HE compliance leads & DVCs

A new AI tool arrives on your institution's radar. A department wants to pilot it for essay marking. Your legal or compliance team asks whether it falls under the EU AI Act. You ask your Learning Technologist, who checks with IT, and nobody quite knows the answer.

This scenario is playing out at institutions across the UK and Europe right now, and the clock is moving.

> **What does the EU AI Act mean for higher education assessment tools?**
> The EU AI Act (Regulation 2024/1689) classifies AI systems used to evaluate academic performance as high-risk under Annex III, point 3(b). High-risk classification does not prohibit use: it requires institutions and tool providers to meet obligations around human oversight, transparency, and accountability. Any AI assessment tool deployed after August 2026 must comply. Tools already in use by February 2025 had a transitional window but should now be actively reviewed.

## What exactly does the EU AI Act cover in higher education?

The EU AI Act (Regulation (EU) 2024/1689) entered into force in August 2024.¹ It takes a tiered approach to AI risk. At the top are prohibited uses, such as social scoring. Below that sit high-risk applications, which are permitted but regulated. The regulation then applies progressively across a transition timetable, with high-risk AI systems in education facing full compliance obligations from August 2026.

Annex III of the Act lists eight categories of high-risk AI. Category 3 covers education and vocational training. Point 3(b) is the one directly relevant to assessment tools: it covers AI systems intended to evaluate the learning outcomes of natural persons, including those used to automate exam scoring, student placement, and the evaluation of individual academic performance.

The key phrase is "evaluate the learning outcomes." Any AI system that generates, influences, or informs a grade or assessment decision falls into scope. Automated essay scoring, AI-generated feedback tied to a mark, and tools that rank or group students based on assessed outputs are all high-risk systems under the Act.

[FIGUUR: EU AI Act: Risk Tiers for Higher Education]
- PROHIBITED: Social scoring, real-time biometric surveillance
- HIGH-RISK (Annex III): AI assessment tools, student placement systems, automated exam scoring (Annex III, point 3(b))
- LIMITED RISK: Chatbots, AI tutors (transparency obligations only)
- MINIMAL RISK: Spam filters, AI-based scheduling tools (no specific obligations)
- Onderschrift in figuur: High-risk AI in education: full compliance required from August 2026

*Figure 1: The EU AI Act's four-tier risk framework. AI systems used in academic assessment fall into the high-risk category under Annex III, point 3(b).*

## What obligations does high-risk classification create for institutions?

High-risk classification under the EU AI Act creates obligations for both the AI provider and the institution deploying the system. The most substantive requirements for day-to-day academic use are found in Articles 13 and 14.

### Article 13: Transparency

High-risk AI systems must be sufficiently transparent so that deployers can interpret and use the outputs correctly. In practice, this means institutions must be able to explain to students how AI is involved in their assessment, what data is used, and how the system arrives at its outputs. A tool that produces a grade without any explanation of how it was generated does not meet this standard.

### Article 14: Human oversight

Article 14 is the most consequential requirement for assessment tools. It mandates that high-risk AI systems be designed so that a qualified human can effectively oversee, interpret, and where necessary override their outputs. Institutions must not only make human review technically possible but ensure it is operationally embedded in the workflow.

This rules out any scenario where AI-generated grades are released to students without a qualified member of staff having reviewed and approved them. It also means institutions need to document their oversight procedures, not simply assert that human review happens.

> **Compliance risk:** Deploying an AI assessment tool where grades are automatically released without lecturer sign-off is non-compliant under Article 14 of the EU AI Act, regardless of the tool's accuracy. The human oversight requirement is structural, not optional.

## Where are most institutions right now on AI policy?

The gap between regulatory requirement and institutional readiness is significant. The 2024 EDUCAUSE AI Landscape Study, which surveyed more than 900 higher education technology professionals, found that only 23% of institutions had any AI-related acceptable use policies in place, and that nearly half of respondents disagreed that their institution had appropriate policies and guidelines to enable ethical and effective decision-making about AI use.²

These figures reflect a sector that has moved quickly to experiment with AI tools but has not yet built the governance frameworks to deploy them responsibly at scale. For institutions in the EU and UK, where the AI Act applies or is being tracked for potential equivalent adoption, this gap creates legal and reputational exposure.

[FIGUUR: Institutional AI Policy Readiness (2024). Source: EDUCAUSE AI Landscape Study 2024 (n=900+ institutions)]
- 23% Have AI acceptable use policies in place
- 77% Do not yet have AI acceptable use policies
- Nearly half (48%) disagree their institution has adequate AI governance policies

*Figure 2: Only 23% of higher education institutions surveyed by EDUCAUSE in 2024 had AI acceptable use policies in place.*

## What should an institution do to prepare for AI Act compliance in assessment?

The following steps address the most immediate compliance requirements for institutions deploying or considering AI assessment tools.

- **Audit current AI tools against Annex III.** Any tool that affects student grades or academic progression decisions needs to be reviewed. This includes tools embedded in your LMS that you may not have scrutinised as AI systems.
- **Confirm the provider's compliance status.** Ask suppliers whether their system is designed to meet Article 13 (transparency) and Article 14 (human oversight) requirements. Request documentation, not just assurances.
- **Embed human review into the workflow, not just on paper.** Article 14 requires that human oversight is operationally meaningful. A policy that says lecturers may review grades is not the same as a workflow that requires them to do so before release.
- **Inform students of AI involvement.** Transparency obligations under Article 13 extend to the students being assessed. Course handbooks and assessment briefs should disclose where AI tools are used in the marking process.
- **Document oversight procedures.** High-risk AI systems require record-keeping. Institutions should maintain logs of AI-generated outputs and the human decisions made in response to them.

## How does Eduface meet the EU AI Act requirements?

Eduface was designed around the human-in-the-loop principle that the EU AI Act now makes mandatory for assessment AI. Human oversight is not a setting that can be switched off: every mark generated by Eduface requires lecturer review and sign-off before it is released to any student.

Two workflow modes are available. In blind mode, the lecturer completes their own marking first, without seeing Eduface's AI grades. Only after finishing their own marking does the system reveal the AI grades for comparison. This protects against anchoring bias and gives the lecturer confidence that their judgement is independent. In AI-visible mode, the AI marks are shown upfront and the lecturer edits or overrides them as needed before release. Institutions can set which mode is mandatory for their staff, providing governance control at the institutional level.

On transparency, Eduface generates detailed, criterion-referenced feedback that explains the reasoning behind each score. Students and lecturers can see not just the mark but the specific feedback against each rubric element. All processing runs on Eduface's own GPU infrastructure in the Netherlands: no student data passes through third-party AI APIs such as OpenAI.

| EU AI Act obligation | Requirement | Eduface approach |
|---|---|---|
| Article 13: Transparency | System outputs must be interpretable; institutions must be able to explain AI involvement to affected individuals | Criterion-referenced feedback explains every score; students see the reasoning, not just a number |
| Article 14: Human oversight | Qualified humans must be able to review, interpret, and override AI outputs; release without human sign-off is non-compliant | Lecturer sign-off is mandatory before any grade is released; two workflow modes (blind and AI-visible) give institutions governance control |
| Article 9: Risk management | Providers must implement risk management systems covering the AI system's lifecycle | Ongoing accuracy monitoring against lecturer marks; 95% alignment validated in UK pilots |
| Data protection: GDPR alignment | Student data must be processed lawfully and with appropriate safeguards | Processing on Eduface's own EU-based infrastructure; no data passed to third-party APIs |

## Frequently asked questions

**Does the EU AI Act apply to UK institutions after Brexit?**
The EU AI Act applies to providers and deployers operating within the EU. UK institutions are not directly bound by EU law post-Brexit, but any tool provided by an EU-based company or processing data within the EU falls within scope. The UK government is monitoring the Act and has indicated intent to develop equivalent frameworks. Institutions operating across the UK and EU, or procuring tools from EU providers, should treat compliance as a practical requirement now.

**What is the timeline for EU AI Act compliance for assessment tools?**
The Act entered into force in August 2024. Prohibitions on unacceptable-risk AI applied from February 2025. Full obligations for high-risk AI systems, including those in educational assessment, apply from August 2026. Institutions deploying AI assessment tools should be reviewing compliance now rather than waiting for the deadline.

**What counts as "human oversight" under Article 14?**
Article 14 requires that a qualified human can effectively oversee the AI system's operation, interpret its outputs, and intervene or override when necessary. For assessment tools, this means a lecturer or responsible academic must review and approve marks before release. A policy document stating that review is possible does not satisfy the requirement: the workflow itself must make human approval a mandatory step.

**Is Eduface approved as a compliant AI assessment tool?**
Eduface is designed to meet the requirements of the EU AI Act for high-risk educational AI systems, including mandatory human oversight (Article 14), transparent criterion-referenced output (Article 13), and EU-based data processing without third-party API dependency. Eduface is also an approved supplier on the Jisc/CHEST framework in the UK and the HEAnet framework in Ireland.

**Do students need to be told their work was assessed using AI?**
Under Article 13 of the EU AI Act, institutions must ensure affected individuals can understand the AI system's role in decisions that affect them. For assessment, this means students should be informed in advance that AI tools are used in the marking process, what role they play, and that a qualified human reviews and is responsible for the final grade. Most institutions will need to update assessment briefs and course handbooks accordingly.

## Compliance is not optional, but it is achievable

The EU AI Act does not prohibit AI in assessment. It creates a framework that, if followed, should make AI assessment tools more trustworthy for students, staff, and institutions alike. The institutions that act now, rather than waiting for August 2026, will be in a stronger position both regulatorily and in terms of student and staff confidence in the tools they deploy.

[CTA-BLOK]
**Talk to Eduface about compliant AI assessment**
Eduface is built around the human-in-the-loop principle and approved on the Jisc/CHEST framework. Request a demo to see how the compliance workflow operates in practice.
[Request a demo]

## References

1. European Parliament and Council of the EU. (2024). Regulation (EU) 2024/1689 (Artificial Intelligence Act). Official Journal of the European Union. [Annex III, point 3(b): educational assessment AI classified as high-risk. Article 14: human oversight mandatory. Article 13: transparency requirements.]
2. EDUCAUSE. (2024). 2024 EDUCAUSE AI Landscape Study. EDUCAUSE. [Key finding: only 23% of institutions surveyed had AI acceptable use policies in place; 48% disagreed that adequate governance frameworks existed.]
3. Hattie, J., & Timperley, H. (2007). The power of feedback. Review of Educational Research, 77(1), 81–112.
4. University and College Union. (2016). Workload is an education issue: UCU workload survey report 2016. UCU. [Key finding: 75% of HE staff describe their job as stressful; 46% report unrealistic time pressures from marking and administrative workload.]
