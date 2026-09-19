# Menno - echte posts (corpus, aangeleverd 2026-06-18)

Tags: ✅ = authentieke stem (emuleren) · 👤 = persoonlijk · ⚠️ = AI-tell (substantie ja, opmaak nee)

NB: Menno's posts hebben sterke, échte technische substantie (de moat). De opmaak (bold-unicode op losse woorden, emoji achter elke bullet) is de AI-tell. Bij ghostwriten: hou de techniek + de "wat betekent dit voor onderwijs"-payoff, gooi de opmaak-tics eruit.

---

⚠️ Excited to bring state-of-the-art LLM technology, specifically designed for education and assessment, to the UK 🇬🇧

---

✅👤 Internship completed. 🎓

As part of my MSc in Artificial Intelligence: Intelligent Technology, I recently completed my internship at Van Rossum and finished it with an 8. ✅

During this internship, I had the opportunity to apply AI in a structural engineering context within a firm specializing in the design and calculation of structural systems. This turned out to be quite different from my daily work at Eduface and involved learning how to adapt AI methods to real-world industrial constraints. 🏗️

I'd like to thank Coert Doomen for the day-to-day guidance and for introducing me to the world of structural engineering.
Thanks as well to Wim Wiegerinck from Radboud University for supervising the internship and guiding the implementation of the AI predictive model.
And finally, thanks to Milco Hahury for helping set up the internship and making the connection with Van Rossum in the first place. 🙏

As the final step of my MSc in AI, I've now started writing my Master's thesis on Training 𝐓𝐫𝐚𝐧𝐬𝐟𝐨𝐫𝐦𝐞𝐫𝐬 𝐰𝐢𝐭𝐡 𝐏𝐞𝐫𝐭𝐮𝐫𝐛𝐚𝐭𝐢𝐨𝐧𝐬, supervised by Nasir Ahmad. I am very excited to contribute to this research, especially given its relevance and the significant amount of ongoing work in this rapidly evolving field. 🚀

---

✅⚠️ (sterke substantie, opmaak = AI-tell) 𝐏𝐫𝐮𝐧𝐢𝐧𝐠 𝐢𝐬 𝐚 𝐬𝐲𝐬𝐭𝐞𝐦𝐬 𝐝𝐞𝐜𝐢𝐬𝐢𝐨𝐧, 𝐧𝐨𝐭 𝐚 𝐜𝐨𝐦𝐩𝐫𝐞𝐬𝐬𝐢𝐨𝐧 𝐭𝐫𝐢𝐜𝐤

At Eduface, we don't prune models to "make them smaller." We prune them because 𝐞𝐝𝐮𝐜𝐚𝐭𝐢𝐨𝐧𝐚𝐥 𝐀𝐈 has hard system constraints. 🎓

Our model needs to be:
- fast enough for 𝐫𝐞𝐚𝐥-𝐭𝐢𝐦𝐞 feedback
- small enough to run efficiently on institution-controlled infrastructure
- predictable and stable across assignments, courses, and languages

𝐏𝐫𝐮𝐧𝐢𝐧𝐠 is one of the few model-level techniques that directly affects all three.

The naive view of pruning is simple: remove the weights that matter least.

In practice this fails, because LLMs are not collections of independent parameters. Weights co-adapt. Remove one, and the effective function of many others changes.

📊 In our pruning experiments, the key was not sparsity itself, but:
- approximating the 𝐥𝐨𝐜𝐚𝐥 𝐜𝐮𝐫𝐯𝐚𝐭𝐮𝐫𝐞 of the loss landscape
- identifying redundant directions, not redundant weights
- updating remaining parameters to compensate for removals

By pruning rows and columns (not just individual weights), you:
- reduce matrix dimensions directly
- get real gains in 𝐦𝐞𝐦𝐨𝐫𝐲 𝐚𝐧𝐝 𝐜𝐨𝐦𝐩𝐮𝐭𝐞 (no sparse kernels required)
- preserve architectural regularity, which matters in deployment

📈 For Eduface, this has very concrete impact:
- lower inference latency when generating feedback
- tighter memory bounds for 𝐥𝐨𝐜𝐚𝐥𝐥𝐲 𝐡𝐨𝐬𝐭𝐞𝐝 deployments
- higher throughput when grading many assignments simultaneously

I know this gets technical quickly, but the core idea is straightforward: pruning is not about zeroing weights, it's about removing capacity while 𝐩𝐫𝐞𝐬𝐞𝐫𝐯𝐢𝐧𝐠 function.

That is the difference between deploying an LLM and 𝐞𝐧𝐠𝐢𝐧𝐞𝐞𝐫𝐢𝐧𝐠 an educational AI system.

---

✅⚠️👤 𝐖𝐡𝐚𝐭 𝐢𝐭 𝐭𝐨𝐨𝐤 𝐭𝐨 𝐛𝐮𝐢𝐥𝐝 𝐚𝐧𝐝 𝐦𝐚𝐭𝐮𝐫𝐞 𝐨𝐮𝐫 𝐨𝐰𝐧 𝐥𝐨𝐜𝐚𝐥𝐥𝐲 𝐡𝐨𝐬𝐭𝐞𝐝 Eduface 𝐀𝐈 𝐦𝐨𝐝𝐞𝐥 𝐟𝐨𝐫 𝐟𝐞𝐞𝐝𝐛𝐚𝐜𝐤 𝐚𝐧𝐝 𝐠𝐫𝐚𝐝𝐢𝐧𝐠 (𝟐𝟎𝟐𝟓) 🎓

One of our core milestones in 2025, was training our model on both Dutch and English, specifically focused on reading comprehension.
This led to our LLM achieving the highest score on the 𝐃𝐮𝐭𝐜𝐡 𝐒𝐐𝐮𝐀𝐃 benchmark (SQuAD-NL) and ranking among the top-performing models on the 𝐄𝐧𝐠𝐥𝐢𝐬𝐡 𝐒𝐐𝐮𝐀𝐃 benchmark. 📊
Before the feedback and grading process can even begin, our model must be able to deeply understand the students' work. Accurate 𝐫𝐞𝐚𝐝𝐢𝐧𝐠 𝐜𝐨𝐦𝐩𝐫𝐞𝐡𝐞𝐧𝐬𝐢𝐨𝐧 is crucial for understanding academic context, argumentation and writing quality.

With that foundation, the next phase focused on 𝐚𝐜𝐚𝐝𝐞𝐦𝐢𝐜 𝐟𝐞𝐞𝐝𝐛𝐚𝐜𝐤 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐨𝐧. We trained the model to produce feedback that is didactic, specific, and aligned with rubric criteria.

In 2025, we also built our new 𝐠𝐫𝐚𝐝𝐢𝐧𝐠 𝐚𝐠𝐞𝐧𝐭 for open-ended exam questions together with Tilburg University. This was a core milestone in our vision to help teachers save time, and bring better and more consistent grading and feedback to education. ✍

Besides spending most of my time in coding and building training pipelines, I also stepped outside the IDE.
I met educators and learning technologists at BETT (London), ALT in Glasgow (including an unexpected Ceilidh dance), SURF Onderwijsdagen (The Hague) and OEB in Berlin (while also visiting some nice Christmas markets).🎄
Beyond the conferences, I personally had the opportunity to bring Radboud University and Tilburg University on board, something I am very proud of.

New model updates are already in progress, and several new universities in the UK, Netherlands and Ireland are onboarding. 💯

More on that in 2026. For now enjoy New Year's Eve 🥂

Marije Markus, Alex Kortekaas, Margot van Mulken, Prof Helen King, Duuk Baten, Ellena Papageorgiou, Onno van Duinen, Charles Bollen

---

✅👤 From studying AI at Radboud University to bringing AI-powered 𝗳𝗲𝗲𝗱𝗯𝗮𝗰𝗸 and 𝗴𝗿𝗮𝗱𝗶𝗻𝗴 back to Radboud University. 🎓

In September 2021, I started my bachelor's in Artificial Intelligence, just before the AI boom. In 2023, I started building Eduface, an AI platform that provides feedback and grading on assignments. In September 2024, I began my master's, and just over a year ago I received my bachelor's degree. Now, as I focus on finishing my master and scaling up Eduface, these two paths come together. 📈

I am proud to announce that Eduface will start a 𝗰𝗼𝗹𝗹𝗮𝗯𝗼𝗿𝗮𝘁𝗶𝗼𝗻 with Radboud University at the beginning of the next academic semester. 📚

Together with Margot van Mulken, we'll explore how our technology can support 𝗮𝘀𝘀𝗲𝘀𝘀𝗺𝗲𝗻𝘁 within the Faculty of Arts.

From studying AI at Radboud University, to using that knowledge to create our own 𝗹𝗼𝗰𝗮𝗹𝗹𝘆 hosted AI feedback model, helping Radboud University typically 𝘀𝗮𝘃𝗲 48,5% of their time in assessment while bringing better, 𝗱𝗶𝗱𝗮𝗰𝘁𝗶𝗰 feedback to their students. 🤖

Thanks to everyone who's been part of this journey. 🚀

Pim Haselager, Mikhail Titov, Mathijs Buddingh', Daniel Blanco Ania, Lisa van Roermund, Iglika V., Daniël Wigboldus

---

⚠️ Day 2 at #ALTC25 in Glasgow, ready to showcase Eduface to learning technologists from universities across the UK. 📚

Yesterday we had a fantastic start, talking with teams from London Business School, Imperial College London, Bath Spa University, Abertay University, and many more. 🎓

It was great to hear everyone theirs perspectives on how AI can support education, and how Eduface can help meet those needs.

In the evenening, we joined the Association for Learning Technology dinner, and learned to dance the Ceilidh, a traditional Scottish dance. 🕺

Overall it has been a great experience being in Glasgow and seeing learning technologists light up when they see the solution we provide! 🚀

---

📣 Today we are announcing that at the start of the next academic year, Eduface will start a pilot with Tilburg University. 📚

Together with Tilburg University, we will evaluate how much time our tool can save in assessing essays and exams with open-ended questions. 🎓

We want to thank Marije Markus and Wim Jelsma for their efforts in helping set up this pilot.

---

✅⚠️ Last time I made a post about the three new ways teachers can create a 𝐰𝐞𝐥𝐥-𝐝𝐞𝐟𝐢𝐧𝐞𝐝 rubric, without the need for hours of manual work. In this process, our AI analyses the rubric, strips it from non-essential content and makes the rubric complete based on the necessary 𝐝𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐯𝐞 requirements for the feedback process. 📚

Once our AI is done analyzing the rubric, it will put it into a matrix where there are 𝐟𝐨𝐮𝐫 𝐥𝐞𝐯𝐞𝐥𝐬 defined as you can see in the animation. For each rubric point, there is a description of what is needed for a student to achieve a certain level.

In this post I will follow-up on this by announcing that Eduface is in the final development and testing phase to add 𝐠𝐫𝐚𝐝𝐢𝐧𝐠 to our platform.

So we already saved time for teachers in the formative assessment process, but now we help teachers 𝐠𝐫𝐚𝐝𝐞 𝟑 𝐭𝐢𝐦𝐞𝐬 𝐟𝐚𝐬𝐭𝐞𝐫. 📈

We are aware that grading falls in the high risk category of the AI-Act. But because we have built our own AI model, hosted 𝐥𝐨𝐜𝐚𝐥𝐥𝐲 in the Netherlands, and we can be transparent on how we trained it and how it arrives at its output, we are fully compliant with all the 𝐫𝐞𝐠𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬. 🔒

Interested in making a real impact in higher education? Reach out to me, to help develop the future of learning with AI. 🚀

---

✅⚠️ What we have observed from teachers using Eduface is that their grading schemes are often short, inconsistent or filled with irrelevant context. While this might work fine when a human is using the rubric, it does not always help our AI model understand what is actually expected from the student. 📚

That's why we've introduced three new ways to create a 𝐰𝐞𝐥𝐥-𝐝𝐞𝐟𝐢𝐧𝐞𝐝 rubric, without the need for hours of manual work:

1. Upload your existing rubric: It does not matter if your rubric is very detailed and descriptive, or not at all. Our model 𝐚𝐧𝐚𝐥𝐲𝐬𝐞𝐬 your rubric to strip away non-essential content, and makes your rubric complete based on the necessary descriptive requirements. In the end you will get back your rubric, in the Eduface format, as you can see in the video below.
2. Choose from pre-built templates: Another option is choosing one of our new three rubric 𝐭𝐞𝐦𝐩𝐥𝐚𝐭𝐞𝐬 that are focused on academic writing assignments(argumentative essay, research paper, scientific paper). These templates are designed to give detailed and didactical feedback on certain academic writing assignments in higher education.
3. Build your own rubric directly in Eduface: Our last new option is for when you want to start designing your rubric from 𝐬𝐜𝐫𝐚𝐭𝐜𝐡. You can add your criteria and descriptions of the rubric, or choose from predefined rubric criteria.

With this we have created a 𝐮𝐬𝐞𝐫-𝐟𝐫𝐢𝐞𝐧𝐝𝐥𝐲 app that makes it possible to give detailed and didactic feedback, even if you don't have a rubric! 🎓

These new features are part of a larger series of 𝐢𝐦𝐩𝐫𝐨𝐯𝐞𝐦𝐞𝐧𝐭𝐬 we are working on, based on the feedback we got from our users. 📈

Do you want to try it yourself? Eduface is still free to use during our open beta. 🚀
𝐂𝐫𝐞𝐚𝐭𝐞 an account and start creating your rubric: Eduface.me

---

✅⚠️ Eduface's AI feedback model achieves the highest score in Dutch reading comprehension.🚀

A few months ago, we shared that Eduface's AI feedback model 𝐨𝐮𝐭𝐩𝐞𝐫𝐟𝐨𝐫𝐦𝐞𝐝 several leading models in the Dutch SQuAD (squad_nl) reading comprehension benchmark, including GPT-4 and Llama-3. Today we are proud to announce that our model now holds the 𝐡𝐢𝐠𝐡𝐞𝐬𝐭 F1 score on this benchmark.

Here a small explanation of the metrics used in this benchmark:
- F1 score: This metric balances precision and recall, which indicates a good measure of the model's accuracy. A high F1 score indicates that both precision and recall are good.
- Exact match (EM): This measures the percentage of predictions that match any one of the ground-truth answers exactly, which indicates the model's ability to produce precise answers.

This concludes our training phase for reading comprehension in both Dutch and English. As a result, our model now has top performance in both languages which allows us to 𝐮𝐧𝐝𝐞𝐫𝐬𝐭𝐚𝐧𝐝 student assignments even better than before.
At the same time, we have been focusing on improving the model's capabilities in giving feedback on 𝐚𝐜𝐚𝐝𝐞𝐦𝐢𝐜 𝐰𝐫𝐢𝐭𝐢𝐧𝐠. This resulted in our model being able to provide better didactic and academic feedback on writing assignments in higher education. More about this soon. 🎓

Would you like to test our model with your own assignments?
Head to Eduface.me and make a free account to 𝐭𝐫𝐲 𝐢𝐭 𝐲𝐨𝐮𝐫𝐬𝐞𝐥𝐟! 📚
