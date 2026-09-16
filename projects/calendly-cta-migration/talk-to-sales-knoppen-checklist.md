# Werkbestand: "Talk to sales" knoppen → Calendly

**Doel:** elke knop die nu naar de talk-to-sales pagina (`/resources/talk-to-sales`) gaat, ompunten naar de Calendly-link. **Tekst laten staan.** Talk-to-sales pagina zelf blijft bestaan (Dante wil eerst conversie meten).

**Nieuwe link (overal plakken):**
```
https://calendly.com/eduface/30min?back=1
```

**Niet aanraken:** "Create free account" (→ app.eduface.me/signup), "Log in", menu-links, "Pricing".

---

## A. Blog: AI Essay Grader for Brightspace D2L
Pagina: `/resources/blog/ai-essay-grader-brightspace-d2l` — dit zijn alle knoppen die IK op deze pagina heb gebouwd (nav + footer komen uit de layout, zie sectie C):

- [x] **"Book a demo"** (CTA-blok onderaan) → AL omgezet naar Calendly ✅
- [ ] "Create free account" → laten staan (signup), NIET wijzigen

> Op deze pagina zelf staat verder geen enkele talk-to-sales knop. Klaar.

---

## B. Gedeelde componenten (1x aanpassen = overal goed)
Deze staan op ELKE pagina. Open het component in Framer (dubbelklik), dan kan ik de link erin omzetten — of doe het zelf. Dit zijn de belangrijkste:

- [ ] **Footer** — heeft een "Talk to sales" tekstlink (kolom "Connect"). → Calendly
- [ ] **Nav** (bovenbalk) — "Book a demo" / sales-knop rechtsboven. → Calendly (check of 'ie naar talk-to-sales wijst)
- [ ] **CTA** component (het herhaalde blok onderaan pagina's) — sales-knop. → Calendly

> Let op: als de link als *prop per instance* is ingesteld (niet vast in het component), dan moet 'ie per pagina apart. Dat zie ik zodra het component open is.

---

## C. Pagina's om na te lopen (hero / losse CTA-knoppen)
Marketing-pagina's hebben vaak een eigen "Talk to sales" / "Book a demo" knop in de hero of tussen de secties. Loop deze na (open in Framer → check elke knop → Calendly waar 'ie naar talk-to-sales gaat):

- [ ] `/` (Home)
- [ ] `/pricing`
- [ ] `/product/paper-grader`
- [ ] `/product/exam-grader`
- [ ] `/product/feedback`
- [ ] `/product/oral-examination`
- [ ] `/resources/lms-integrations`
- [ ] `/resources/case-study`
- [ ] `/resources/about-us`
- [ ] `/resources/environmental`
- [ ] `/resources/safety`
- [ ] `/resources/blog` (blog index)
- [ ] Overige blogposts (elk een CTA-blok onderaan): how-ai-delivers-formative-feedback-at-scale, why-ai-feedback-nurtures-creativity, ai-plagiarism-detection-failing-higher-education, nss-assessment-feedback-scores, lecturer-marking-time-higher-education, ai-powered-assessment-higher-education, can-ai-mark-papers-fairly, business-case-ai-assessment-higher-education, eu-ai-act-higher-education-assessment, nss-assessment-strategy-paradox, formative-assessment-higher-education, automated-feedback-vs-manual-feedback, cograder-review-2026-higher-education, gradescope-review-2026-higher-education, human-in-the-loop-ai-assessment

> De meeste blogposts gebruiken waarschijnlijk hetzelfde CTA-component (sectie B). Als dat zo is, zijn ze in één klap goed en hoef je ze hier niet los te doen.

---

## Snelste route
1. Eerst **sectie B** (Footer, Nav, CTA-component). Grote kans dat dit 80%+ van alle knoppen in één keer fixt.
2. Daarna **sectie C** alleen voor pagina's met een eigen losse knop die NIET uit een gedeeld component komt.

Open een component/pagina in Framer en zeg het, dan zet ik de link er meteen in.
