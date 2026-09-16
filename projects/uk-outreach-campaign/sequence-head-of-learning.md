# UK ABM — Head of Learning sequence (multichannel, v1)

> Scope: runs up to the **Discovery gate** (handbook Stage 1 / SQL), then hand off to Jeroen.
> Goal gate = **20-min discovery call booked = SQL**.
> Status: drafted, not yet built in Lemlist. Blockers at the bottom.

## Targeting decision (handbook-anchored)

Lead on the **Head of Learning / Head of Learning & Teaching** (the manager of the Learning Technologist), NOT the Learning Technologist.

- **Learning Technologist = Coach** (handbook Stage 2): helps + runs the tool, no authority/influence. Coaches get us a POV, not an institutional deal.
- **Head of Learning = champion-target**: has authority (manages the LT) + can influence the PVC/EB and set buying criteria.
- **PVC Education = EB** (discretionary funds): run as a parallel second thread (multi-thread), not the first touch.

Rule: the manager who owns teaching quality must be on board first. The LT joins later as a technical evaluator, not as the entry point.

## Why-now (UK HE calendar, late June)

Marking season just wrapped, exam boards done, staff drained. Summer is the window where teams decide what to change before September. Timing hook for every step: "you just came out of marking, now's the time to fix it before September."

## Variables
`{{firstName}}`, `{{universityName}}`, `{{nssAF}}` (their 2025 NSS assessment & feedback %), `{{calendarLink}}`.

---

## The sequence (multichannel, ~13 day window, then stop)

Cadence is built for the follow-up reality: most positive replies land on touch 3-4 cold. 7 touches across email + LinkedIn before we park the prospect.

### Step 1 — Day 1, LinkedIn connect (soft note)
> Hi {{firstName}}, I work with UK universities on assessment and feedback - faster feedback for students, less marking for staff. Would be good to connect.

### Step 2 — Day 1, Email
**Subject:** marking just wrapped at {{universityName}}?
> Hi {{firstName}},
>
> You've just come out of marking season, so this might land at the right time.
>
> Most heads of learning we talk to have the same problem: feedback to students is too slow or too thin, and staff are worn out from the marking that gets it there. The NSS usually shows it first - {{universityName}} sat at {{nssAF}}% on assessment and feedback in 2025.
>
> Eduface gives students fast, detailed written feedback on their assignments and takes a big chunk of the marking off staff. A few UK universities run it as a paid pilot through Jisc.
>
> Worth 20 minutes over the summer to see if it fits your plans for next year?
>
> Dante

### Step 3 — Day 3, Email (proof + value)
**Subject:** re: marking just wrapped at {{universityName}}?
> Hi {{firstName}},
>
> Quick follow-up. The part heads of learning care about most: it's not just faster, the feedback is good enough that students act on it, and your markers get their evenings back.
>
> [INSERT REAL PILOT RESULT — one sourced number, e.g. "At [pilot uni], feedback turnaround went from X days to Y, with Z% less marking time." No made-up numbers.]
>
> Summer is when most teams decide what to change before September. If feedback and marking load is on that list, I'll show you what a pilot looks like. 20 minutes, no slides. When works?
>
> Dante

### Step 4 — Day 5, LinkedIn message (if connected)
> Thanks for connecting {{firstName}}. I reached out because most heads of learning are dealing with slow feedback and marker burnout at the same time. We help with both, and a few UK unis run it as a Jisc pilot. Open to a short call over the summer?

### Step 5 — Day 8, Email (the "why you, not the tech team" angle)
**Subject:** the marking load on your team
> Hi {{firstName}},
>
> One more angle, then I'll leave it.
>
> The reason I aim this at you and not the tech team: your staff feel the marking load, but the call on whether to fix it sits with you. A learning technologist can run the tool, it only sticks if the person who owns teaching quality is behind it.
>
> If you want to take pressure off your markers before the next term, that's the conversation. Happy to keep it short.
>
> Dante

### Step 6 — Day 11, LinkedIn message / voice note (light nudge)
> {{firstName}}, last nudge from me. If taking marking load off your team before September is worth 20 minutes, here's my calendar: {{calendarLink}}. If not, no worries.

### Step 7 — Day 13, Email (break-up + clear ask)
**Subject:** should I close this off?
> Hi {{firstName}}, haven't heard back so I'll park it. If marking load or feedback scores come up before September, just reply and I'll pick it up.
>
> If it's worth a quick look now: {{calendarLink}}.
>
> Dante

---

## Multi-thread (run alongside, don't merge into the same sequence)
- **Parallel thread to the PVC Education (EB-level)**, 2 light touches max, framed as "I've reached out to [Head of Learning], wanted you on the radar too." Keeps the deal multi-threaded so it doesn't die if the champion goes quiet.
- The **Learning Technologist** is NOT cold-touched. Only brought in once the Head of Learning agrees to a call, as the technical evaluator.

## Before this goes live (blockers)
1. **Real proof point** for Step 3. One sourced pilot stat (NL pilots / Hogeschool Rotterdam?). No made-up numbers.
2. **Named Head-of-Learning contacts + emails** per target account (Lemlist enrich / `lemleads_search`). Existing Cluster A file has PVC + champion names but not all Head-of-Learning tier.
3. **Calendar link** ({{calendarLink}}).
4. **LinkedIn connected to Lemlist** for the LinkedIn steps (Steps 1, 4, 6).
