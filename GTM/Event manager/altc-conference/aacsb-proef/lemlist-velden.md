# Lemlist-velden per persoon: "The business outcomes of AI marking and feedback"

_2026-10-06. Dit is de bron voor de import. Vervangt de stappenvolgorde uit `flow-uitgeschreven.md` (die volgde mijn eigen aanname, niet de echte flow)._

## De flow in Lemlist (gelezen 06-10-2026)

Campagne `cam_kM7vngvjiuG7Wda8i`, status draft, afzender dante.torbed@eduface.me.

```
1. LinkedIn-connectieverzoek          {{linkedInConnectionRequest}}   (als Premium-notitie, max 300 tekens)
   │
   └─ na 4 dagen: verzoek geaccepteerd?
        ├─ JA  (warm)  → LinkedIn-bericht  {{linkedInMessage}}
        │               → belttaak, hoge prioriteit, "Bel om webinar aanmelder te krijgen (warm)"  {{Call_script}}
        └─ NEE (koud)  → e-mail  {{firstEmailSubject}} / {{firstEmail}}
                        → belttaak, gemiddelde prioriteit, "Bel om webinar aanmelder te krijgen (koud)"  {{Call_script}}
```

**Wat dat betekent voor de copy:**
- **Het LinkedIn-bericht gaat alleen naar wie accepteerde, de mail alleen naar wie niet accepteerde.** Niemand krijgt beide. De mail is dus voor de koude groep het eerste wat ze echt lezen, en moet op zichzelf staan.
- **Bellen komt in beide takken direct erna** (delay 0). Er is één `Call_script` per persoon, dus het script mag niet aannemen of iemand een LinkedIn-bericht of een mail kreeg. Neutraal: "I reached out earlier about...".
- **Antwoord op een ja (2a) zit niet in Lemlist.** Dat stuur je zelf, versie B hieronder.
- **Het connectieverzoek staat in het Premium-veld** (`altMessage`). Het gewone notitieveld is leeg. Zonder Premium gaat het verzoek dus zonder notitie de deur uit.
- **Mails in Lemlist hebben `<br>`-tags nodig**, anders valt de opmaak weg (zie `lemlist-import`). Bij de export zet ik de witregels om.
- **Zonder e-mailadres** (O'Mahony, Barac, McMahon-Beattie) kan de mail in de koude tak niet uit. Zonder telefoon (O'Mahony, Kleijnen, Øverby) kom je bij de belttaak uit op de centrale.

**Custom fields voor de export:** `linkedInConnectionRequest`, `linkedInMessage`, `firstEmailSubject`, `firstEmail`, `Call_script`. Daarnaast de standaardvelden: firstName, lastName, email, linkedinUrl, companyName, phone.

[link] = https://events.teams.microsoft.com/event/4239b958-f045-4d0c-8367-96a44223b992@b817b3d1-ef29-4188-b513-db36a036f9b1?source=copyLinkOneEventsShareDialog

---

## 1. Barry O'Mahony, Abu Dhabi University
LinkedIn: https://www.linkedin.com/in/professor-barry-o-mahony-2b62501b/ · e-mail: geen · telefoon: geen

**linkedInConnectionRequest**
Hi Barry, I'm Dante from Eduface. I read your interview in the ADU freshman guide where you mention using AI for grading and feedback. Not many provosts say that out loud yet. We're hosting an online session on the business outcomes of AI marking and feedback. Would you like a personal invite?

**linkedInMessage**
Thanks for connecting, Barry. Another line from that interview stayed with me, the moderating system you put in place for exams. I'd be curious whether AI plays a part in that too.

The session is on Thursday 15 October, 11:00 to 12:00 UK time (14:00 in Abu Dhabi). Would you be able to make it? The link is here either way.
[link]

**firstEmailSubject / firstEmail:** geen adres.

**Call_script** (geen direct nummer, via de centrale van ADU)
Opening: "Hi Barry, it's Dante from Eduface. I reached out earlier about our online session on the business outcomes of AI marking and feedback. In your freshman guide interview you mentioned ADU using AI for grading and feedback. Can I ask, how has that landed with faculty?"
Uitnodiging: "That's exactly the kind of experience we'd love in the room. It's on Thursday 15 October at 14:00 your time. Would you like to join?"
Bij ja: "Great, what's the best email to send the link to?"
Voicemail: "Hi Barry, Dante from Eduface. Quick one about our online session on the business outcomes of AI marking and feedback, Thursday 15 October at 14:00 Abu Dhabi time. I'll send you the link on LinkedIn, it'd be great to have you there."

**2a. Bij ja (zelf sturen)**
Brilliant, glad you're joining. Here's the link for Thursday 15 October, 11:00 to 12:00 UK time (14:00 in Abu Dhabi).
[link]
I'd genuinely love to hear your take on how AI grading has gone at ADU afterwards.

---

## 2. Dominic Finn, Strathclyde Business School
LinkedIn: kandidaat uk.linkedin.com/in/dominic-finn-a273b312 (zelf checken) · dominic.finn@strath.ac.uk · 0141 548 3621

**linkedInConnectionRequest**
Hi Dominic, I'm Dante from Eduface. I came across your OR Society session on the AI skills graduates need versus the ones they actually get, and that gap stuck with me. We're hosting an online session on the business outcomes of AI marking and feedback. Would you like a personal invite?

**linkedInMessage**
Thanks for connecting, Dominic. I also saw you presented early research at OR68 on redesigning MSc capstone reflection. I'd be curious where that's heading.

Our session is on Thursday 15 October, 11:00 to 12:00 UK time, on Teams. Would you be able to make it? The link is here either way.
[link]

**firstEmailSubject**
You don't know what you don't know

**firstEmail**
Hi Dominic,

I sent you a LinkedIn request a few days ago, so here it is by email as well.

On your staff page you wrote that moving from banking into higher education showed you that "sometimes you don't know what you don't know". That's a fair description of where a lot of institutions are with AI marking right now, and it's pretty much why we set up this session, The Business Outcomes of AI Marking and Feedback. It's on Thursday 15 October, 11:00 to 12:00 UK time, on Teams.

Registration is by invitation, and the link is below.

[link]

Would that time work for you?

Best,
Dante Torbed
Eduface

**Call_script**
Opening: "Hi Dominic, it's Dante from Eduface. I reached out earlier about our online session on the business outcomes of AI marking and feedback. I came across your OR Society session on the AI skills graduates need versus what they get. Can I ask, what did your alumni say was missing?"
Uitnodiging: "That's really interesting, and it's partly why I'm calling. The session is on Thursday 15 October at 11. Would you like to join?"
Bij ja: "Great, I'll send the link to your Strathclyde address right after this call."
Voicemail: "Hi Dominic, Dante from Eduface. Quick one about our online session on the business outcomes of AI marking and feedback, Thursday 15 October at 11 UK time. I've sent you the link, it'd be great to have you there."

**2a. Bij ja (zelf sturen)**
Brilliant, glad you're joining. Here's the link for Thursday 15 October, 11:00 to 12:00 UK time.
[link]
I'd genuinely love to hear your take on that need-versus-get gap afterwards.

---

## 3. Simon Mercado, ESCP Business School
LinkedIn: https://linkedin.com/in/simon-anthony-mercado-35ab6118 · smercado@escp.eu · +44 7795 602920 (mobiel, eigen cv)

**linkedInConnectionRequest**
Hi Simon, I'm Dante from Eduface. I read your July paper and the point that business schools can't harness frontier tech the way specialist digital providers can. That's close to what our online session is about, the business outcomes of AI marking and feedback. Would you like a personal invite?

**linkedInMessage**
Thanks for connecting, Simon. The other line from your paper I keep coming back to is the "wipe-out" of graduate entry-level roles. If that's where things are going, how schools assess what graduates can actually do matters even more.

Our session is on Thursday 15 October, 11:00 to 12:00 UK time, on Teams. Would you be able to make it? The link is here either way.
[link]

**firstEmailSubject**
Ten years as an external examiner

**firstEmail**
Hi Simon,

I sent you a LinkedIn request a few days ago, so here it is by email as well.

You spent ten years as an external examiner at Newcastle and Hertfordshire, so you've seen marking across institutions from the outside. Our session, The Business Outcomes of AI Marking and Feedback, looks at the same work from the institution's side. It's on Thursday 15 October, 11:00 to 12:00 UK time, on Teams.

Registration is by invitation, and the link is below.

[link]

Would that time work for you?

Best,
Dante Torbed
Eduface

**Call_script**
Opening: "Hi Simon, it's Dante from Eduface. I reached out earlier about our online session on the business outcomes of AI marking and feedback. I read your July paper on business schools and frontier tech. Can I ask, how has ChatGPT Edu landed with faculty at ESCP?"
Uitnodiging: "That's useful to hear, and it's partly why I'm calling. The session is on Thursday 15 October at 11. Would you like to join?"
Bij ja: "Great, I'll send the link to your ESCP address straight after this."
Voicemail: "Hi Simon, Dante from Eduface. Quick one about our online session on the business outcomes of AI marking and feedback, Thursday 15 October at 11 UK time. I've sent you the link, it'd be great to have you there."

**2a. Bij ja (zelf sturen)**
Brilliant, glad you're joining. Here's the link for Thursday 15 October, 11:00 to 12:00 UK time.
[link]
I'd genuinely love to hear your take on the capacity point from your paper afterwards.

---

## 4. Karin Barac, University of Pretoria
LinkedIn: https://www.linkedin.com/in/karin-barac-87042170/ · e-mail: geen · +27 12 420 5439 (uit een snippet)

**linkedInConnectionRequest**
Hi Karin, I'm Dante from Eduface. I read your TUTBuddy paper, peer review in auditing classes of up to 670 students without marking every piece. A smart way around the numbers. We're hosting an online session on the business outcomes of AI marking and feedback. Would you like a personal invite?

**linkedInMessage**
Thanks for connecting, Karin. I also saw your new paper on the 13 African audit offices, where procedural and symbolic compliance wins out over substantive quality management. It made me wonder how often the same happens with assessment quality in universities.

Our session is on Thursday 15 October, 11:00 to 12:00 UK time (12:00 in Pretoria), on Teams. Would you be able to make it? The link is here either way.
[link]

**firstEmailSubject / firstEmail:** geen adres.

**Call_script**
Opening: "Hi Karin, it's Dante from Eduface. I reached out earlier about our online session on the business outcomes of AI marking and feedback. I read that digital acumen came out on top in your CA2025 research. Can I ask, how do you actually assess that in your students?"
Uitnodiging: "That's a hard one, and it's partly why I'm calling. The session is on Thursday 15 October at 12 your time. Would you like to join?"
Bij ja: "Great, what's the best email to send the link to?"
Voicemail: "Hi Karin, Dante from Eduface. Quick one about our online session on the business outcomes of AI marking and feedback, Thursday 15 October at 12 Pretoria time. I'll send you the link on LinkedIn, it'd be great to have you there."

**2a. Bij ja (zelf sturen)**
Brilliant, glad you're joining. Here's the link for Thursday 15 October, 11:00 to 12:00 UK time (12:00 in Pretoria).
[link]
I'd genuinely love to hear your take on whether something like TUTBuddy changes with AI afterwards.

---

## 5. Una McMahon-Beattie, Ulster University Business School
LinkedIn: niet gevonden (zelf zoeken) · e-mail: geen geverifieerd · +44 28 9536 5793

**linkedInConnectionRequest**
Hi Una, I'm Dante from Eduface. I read your piece with Ian Yeoman on technology boosting workers' productivity rather than replacing them. Universities are asking the same about AI marking, which is what our online session on its business outcomes is about. Would you like a personal invite?

**linkedInMessage**
Thanks for connecting, Una. I have to say, teaching critical thinking through horror metaphors, and zombies before that, is the most memorable thing I've read about hospitality education in a while.

Our session is on Thursday 15 October, 11:00 to 12:00 UK time, on Teams. Would you be able to make it? The link is here either way.
[link]

**firstEmailSubject / firstEmail:** geen geverifieerd adres.

**Call_script**
Opening: "Hi Una, it's Dante from Eduface. I reached out earlier about our online session on the business outcomes of AI marking and feedback. I read in your PRME report that Ulster is working towards AACSB, and that you're leading it. Can I ask, where are you on that journey now?"
Uitnodiging: "It's partly why I'm calling. The session is on Thursday 15 October at 11, with several universities joining. Would you like to join?"
Bij ja: "Brilliant, what's the best email address to send the link to?"
Voicemail: "Hi Una, Dante from Eduface. I'm calling about our online session on the business outcomes of AI marking and feedback, Thursday 15 October at 11. I'd love to send you an invite, you can reach me on [jouw nummer]."

**2a. Bij ja (zelf sturen)**
Brilliant, glad you're joining. Here's the link for Thursday 15 October, 11:00 to 12:00 UK time.
[link]
I'd genuinely love to hear your take on technology boosting people rather than replacing them afterwards.

---

## 6. Mirella Kleijnen, VU Amsterdam (Nederlands)
LinkedIn: niet gevonden (zelf zoeken) · mirella.kleijnen@vu.nl · telefoon: geen
**Eerst het VU-spoor in Close checken.**

**linkedInConnectionRequest**
Hi Mirella, ik ben Dante van Eduface. Ik kwam je paper van juni tegen over hoe deans incentives kunnen verschuiven naar interactiekwaliteit en wederzijds leren. Onze online sessie over de business outcomes van AI-nakijken en feedback raakt daar precies aan. Zal ik je persoonlijk uitnodigen?

**linkedInMessage**
Dank voor het connecten, Mirella. Uit je eerdere werk bleef me het onderscheid bij tussen afwijzen, uitstellen en verzet bij innovaties. Ik ben benieuwd welke van de drie je bij AI-nakijken het vaakst ziet.

De sessie is op donderdag 15 oktober, van 12:00 tot 13:00, in het Engels via Teams. Lukt dat? De link staat hieronder.
[link]

**firstEmailSubject**
Toetsing herontwerpen onder druk

**firstEmail**
Hi Mirella,

Een paar dagen geleden stuurde ik je een connectieverzoek op LinkedIn, dus bij deze ook per mail.

Op je VU-profiel las ik dat je in de coronatijd het onderwijs en de toetsing in korte tijd opnieuw hebt ingericht. AI-nakijken vraagt een vergelijkbare herbezinning, alleen zonder deadline van buitenaf. Daar gaat onze sessie over, The Business Outcomes of AI Marking and Feedback. Hij is op donderdag 15 oktober, van 12:00 tot 13:00, in het Engels via Teams.

Deelname gaat op uitnodiging, de link staat hieronder.

[link]

Past dat tijdstip?

Best,
Dante Torbed
Eduface

**Call_script** (geen nummer, via de centrale van de VU)
Opening: "Hoi Mirella, met Dante van Eduface. Ik had je eerder benaderd over onze online sessie over de business outcomes van AI-nakijken en feedback. Mag ik je iets vragen, hoe kijken jullie bij SBE nu naar AI bij het nakijken?"
Uitnodiging: "Daar gaat de sessie precies over. Hij is donderdag 15 oktober om 12 uur, in het Engels. Zou je erbij willen zijn?"
Bij ja: "Mooi, dan stuur ik je de link direct na dit gesprek."
Voicemail: "Hoi Mirella, met Dante van Eduface. Even kort over onze online sessie over de business outcomes van AI-nakijken en feedback, donderdag 15 oktober om 12 uur. De link heb ik je gestuurd, het zou mooi zijn als je erbij bent."

**2a. Bij ja (zelf sturen)**
Mooi, fijn dat je erbij bent. Hier is de link voor donderdag 15 oktober, van 12:00 tot 13:00 (de sessie is in het Engels).
[link]
Ik hoor achteraf heel graag hoe jij ernaar kijkt vanuit je werk over weerstand tegen innovatie.

---

## 7. Elvira Bolat, Bournemouth University (eerst haar LinkedIn checken)
LinkedIn: https://www.linkedin.com/in/elvirabolat/ · ebolat@bournemouth.ac.uk (onder voorbehoud) · 01202 968755 (onder voorbehoud)

**linkedInConnectionRequest**
Hi Elvira, I'm Dante from Eduface. I read your essay on the platform university and the AI-driven deskilling of academic labour. We're hosting an online session on the business outcomes of AI marking and feedback, and your sceptical view is exactly what it needs. Would you like a personal invite?

**linkedInMessage**
Thanks for connecting, Elvira. Funnily enough, I also found your 2014 paper on marking 300 students' work on tablets, with live updates across the marking team. So you've seen technology in marking from both sides, which is why I'd really value your view in the room.

The session is on Thursday 15 October, 11:00 to 12:00 UK time, on Teams. Would you be able to make it? The link is here either way.
[link]

**firstEmailSubject**
A sceptical voice in the room

**firstEmail**
Hi Elvira,

I sent you a LinkedIn request a few days ago, so here it is by email as well.

Most sessions on AI marking end up as one long nod. With your Assurance of Learning and external examiner work, plus what you wrote about the AI-driven deskilling of academic labour, you'd bring the question most people skip, what it does to academic work itself. Our session is called The Business Outcomes of AI Marking and Feedback, on Thursday 15 October, 11:00 to 12:00 UK time, on Teams.

Registration is by invitation, and the link is below.

[link]

Would that time work for you?

Best,
Dante Torbed
Eduface

**Call_script**
Opening: "Hi Elvira, it's Dante from Eduface. I reached out earlier about our online session on the business outcomes of AI marking and feedback. I read your essay on the platform university, the bit about losing the space for critical inquiry and slowness. Can I ask, where do you see AI making that worse, and is there anywhere it could help?"
Uitnodiging: "That's exactly the kind of view I'd love in the room. The session is on Thursday 15 October at 11. Would you join?"
Bij ja: "Brilliant, I'll send the link over straight after this call."
Voicemail: "Hi Elvira, Dante from Eduface. Quick one about our online session on the business outcomes of AI marking and feedback, Thursday 15 October at 11. I'd really like a sceptical voice in the room, I've sent you the link."

**2a. Bij ja (zelf sturen)**
Brilliant, glad you're joining. Here's the link for Thursday 15 October, 11:00 to 12:00 UK time.
[link]
I'd genuinely love to hear your take on what we got right and wrong afterwards.

---

## 8. Kirsteen Daly, Adam Smith Business School (zonder haakje)
LinkedIn: https://www.linkedin.com/in/kirsteen-daly-cmgr-mcmi-0863388a/ · Kirsteen.Daly@glasgow.ac.uk · 0141 330 4666 (uit een snippet)

**linkedInConnectionRequest**
Hi Kirsteen, I'm Dante from Eduface. We're hosting an online session on the business outcomes of AI marking and feedback, with several universities joining. As you look after accreditations at the Adam Smith Business School, I thought it might be up your street. Would you like a personal invite?

**linkedInMessage**
Thanks for connecting, Kirsteen. I saw you helped run EFMD's Smart Data Management programme, which has since turned into a data and AI workshop. Our session sits right next to that, looking at what AI marking means for an institution rather than for one marker.

It's on Thursday 15 October, 11:00 to 12:00 UK time, on Teams. Would you be able to make it? The link is here either way.
[link]

**firstEmailSubject**
The business outcomes of AI marking

**firstEmail**
Hi Kirsteen,

I sent you a LinkedIn request a few days ago, so here it is by email as well. On Thursday 15 October we're hosting an online session, The Business Outcomes of AI Marking and Feedback, with several universities joining. It runs from 11:00 to 12:00 UK time, on Teams.

If a colleague in learning and teaching at the Adam Smith Business School would get more out of it than you, I'd be glad to invite them too. The link is below either way.

[link]

Would that time work for you?

Best,
Dante Torbed
Eduface

**Call_script**
Opening: "Hi Kirsteen, it's Dante from Eduface. I reached out earlier about our online session on the business outcomes of AI marking and feedback. You look after accreditations at the school, so can I ask, are AACSB or EQUIS asking you anything about AI yet?"
Uitnodiging: "It's partly why I'm calling. The session is on Thursday 15 October at 11. Would you like to join?"
Niet haar ding: "Fair enough. Is there someone in learning and teaching you'd point me to instead?"
Voicemail: "Hi Kirsteen, Dante from Eduface. Quick one about our online session on the business outcomes of AI marking and feedback, Thursday 15 October at 11 UK time. I've sent you the link, it'd be great to have you or a colleague there."

**2a. Bij ja (zelf sturen)**
Brilliant, glad you're joining. Here's the link for Thursday 15 October, 11:00 to 12:00 UK time.
[link]
I'd genuinely love to hear your take on where accreditation bodies are heading with AI afterwards.

---

## 9. Harald Øverby, BI Norwegian Business School
LinkedIn: kandidaat https://www.linkedin.com/in/harald-%C3%B8verby-997a2b23b/ (niet bevestigd) · harald.overby@bi.no · telefoon: geen

**linkedInConnectionRequest**
Hi Harald, I'm Dante from Eduface. Going from Provost to Special Advisor on AI and technology at BI, you'll have seen AI in education from just about every angle. We're hosting an online session on the business outcomes of AI marking and feedback. Would you like a personal invite?

**linkedInMessage**
Thanks for connecting, Harald. Unrelated to the session, but a law master's on the Android Auto case alongside a professorship in data science is quite the side project.

The session is on Thursday 15 October, 12:00 to 13:00 Oslo time, on Teams. Would you be able to make it? The link is here either way.
[link]

**firstEmailSubject**
AI and assessment methods at BI

**firstEmail**
Hi Harald,

I sent you a LinkedIn request a few days ago, so here it is by email as well.

Your rector put it plainly in BI's latest announcement, AI is changing how BI develops effective assessment methods. Having advised BI on AI and technology, you'll know better than most what that means in practice. Our session, The Business Outcomes of AI Marking and Feedback, is on Thursday 15 October, 12:00 to 13:00 Oslo time, on Teams.

Registration is by invitation, and the link is below.

[link]

Would that time work for you?

Best,
Dante Torbed
Eduface

**Call_script** (geen nummer, via de centrale van BI)
Opening: "Hi Harald, it's Dante from Eduface. I reached out earlier about our online session on the business outcomes of AI marking and feedback. You advised BI on AI and technology after your time as provost. Can I ask, what surprised you most in that role?"
Uitnodiging: "That's exactly the kind of experience we'd love in the room. The session is on Thursday 15 October at 12 Oslo time. Would you like to join?"
Bij ja: "Great, I'll send the link to your BI address straight after this."
Voicemail: "Hi Harald, Dante from Eduface. Quick one about our online session on the business outcomes of AI marking and feedback, Thursday 15 October at 12 Oslo time. I've sent you the link, it'd be great to have you there."

**2a. Bij ja (zelf sturen)**
Brilliant, glad you're joining. Here's the link for Thursday 15 October, 12:00 to 13:00 Oslo time.
[link]
I'd genuinely love to hear your take on what you saw from the advisory seat afterwards.

---

## 10. Bendik Samuelsen, BI Norwegian Business School
LinkedIn: https://www.linkedin.com/in/bendik-meling-samuelsen-7b3bb/ (uit een snippet) · bendik.samuelsen@bi.no · +47 464 10 561

**linkedInConnectionRequest**
Hi Bendik, I'm Dante from Eduface. I read in Khrono that BI is working on shared guidelines for using AI when grading student work. I'd love to know how you're approaching it. We're hosting an online session on the business outcomes of AI marking and feedback. Would you like a personal invite?

**linkedInMessage**
Thanks for connecting, Bendik. I also came across BI's input to the national AI committee, the line that oral exams are resource-heavy and that BI should look at new ways to assess students orally at a larger scale. That's one of the harder problems in assessment right now, so it stood out.

Our session is on Thursday 15 October, 12:00 to 13:00 Oslo time, on Teams. Would you be able to make it? The link is here either way.
[link]

**firstEmailSubject**
Learning at scale

**firstEmail**
Hi Bendik,

I sent you a LinkedIn request a few days ago, so here it is by email as well.

When BI gave its teaching award last year, you praised a course for getting students to learn "at scale, in a class with more than 90 students", and that course already gave students feedback on their writing through an AI tool. Scale is exactly where marking and feedback get hard, and it's the angle of our session, The Business Outcomes of AI Marking and Feedback. It's on Thursday 15 October, 12:00 to 13:00 Oslo time, on Teams.

Registration is by invitation, and the link is below.

[link]

Would that time work for you?

Best,
Dante Torbed
Eduface

**Call_script**
Opening: "Hi Bendik, it's Dante from Eduface. I reached out earlier about our online session on the business outcomes of AI marking and feedback. I read in Khrono that BI is working on shared guidelines for AI in grading. Can I ask, how far along are you with those?"
Uitnodiging: "That's helpful, and it's partly why I'm calling. The session is on Thursday 15 October at 12 your time. Would you like to join?"
Bij ja: "Great, I'll send the link to your BI address straight after this."
Voicemail: "Hi Bendik, Dante from Eduface. Quick one about our online session on the business outcomes of AI marking and feedback, Thursday 15 October at 12 Oslo time. I've sent you the link, it'd be great to have you there."

**2a. Bij ja (zelf sturen)**
Brilliant, glad you're joining. Here's the link for Thursday 15 October, 12:00 to 13:00 Oslo time.
[link]
I'd genuinely love to hear your take on where BI's guidelines end up afterwards.
