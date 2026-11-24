"""Bouwt de UTI business case (verwacht en hoog) als PDF.

Alle cijfers komen uit GTM/Accounts/uti/business-case-berekening.xlsx (gecachte waarden),
zodat het document nooit afwijkt van het model.

Gebruik:  python3 -I GTM/Accounts/uti/business-case/build.py
Vereist:  openpyxl, node + playwright (render.js).
"""
import html
import subprocess
import sys
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent
UTI = HERE.parent
MODEL = UTI / "business-case-berekening.xlsx"
LOGO = Path("/home/user/Claude/Design/Merk/logos/logo_navy.png")
OUT_DIR = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else UTI

# ---------------------------------------------------------------- cijfers uit het model
wb = openpyxl.load_workbook(MODEL, data_only=True)
A, B, M, R = wb["Aannames"], wb["Berekening"], wb["Samenvatting"], wb["Rooster"]

S = A["B5"].value          # secties per dag
D = A["B6"].value          # lesdagen
RATE = A["B7"].value       # $ per uur
STUDENTS = A["B9"].value   # studenten per sectie
PRICE = A["B10"].value     # $ per student per maand
G = A["B22"].value         # nakijktijd per sectie, uur
RED = A["B23"].value       # reductie
SHARE = B["B5"].value      # aandeel secties bij 2 of 3 secties
SEC1, SEC2, SEC3 = B["B12"].value, B["B13"].value, B["B14"].value   # secties per dag per type
TOTAL_H = B["B16"].value
SAVED_H = B["B21"].value
SAVED_SINGLE = B["B22"].value
SAVED_MULTI = B["B23"].value
COST = B["B31"].value
LICENSED = B["B30"].value      # Licensed Students (betaald aantal)
IN_CLASS = B["B29"].value      # studenten in de klas
TAIL = IN_CLASS * A["B11"].value  # studenten die de laatste 3 maanden klaar zijn
WIN = R["H35"].value       # venster nakijken, prep, TTEV voor een double (uur)
WIN_AM, WIN_EVE = R["H33"].value, R["H34"].value
SINGLE_WIN = [R.cell(r, 8).value for r in (30, 31, 32)]
CASES = {
    "expected": dict(col="C", label="Expected case"),
    "high": dict(col="D", label="High case, an upper bound"),
}
for c in CASES.values():
    c["cash_h"] = M[f"{c['col']}14"].value
    c["sav"] = M[f"{c['col']}15"].value
    c["net"] = M[f"{c['col']}17"].value
    c["ratio"] = M[f"{c['col']}18"].value

DD, TD = SEC2 / 2, SEC3 / 3                     # instructeurs met 2 resp. 3 secties per dag
INSTR_DAYS = (DD + TD) * D                       # instructeur-dagen per jaar bij 2 of 3 secties
OVER2 = max(0.0, 2 * G - WIN)                    # uren overloop per dag, double
OVER3 = max(0.0, 3 * G - WIN)                    # idem triple
CEIL_H = (DD * OVER2 + TD * OVER3) * D           # uren per jaar buiten het rooster
NEED_H = COST / RATE                             # uren om de licentie terug te verdienen
NEED_MIN = NEED_H / INSTR_DAYS * 60              # minuten per dag per 2-3-secties-instructeur
for k, c in CASES.items():
    c["min"] = c["cash_h"] / INSTR_DAYS * 60


def lens1(g, r, m=1.0):
    return (DD * min(r * 2 * g, max(0, 2 * g - WIN)) + TD * min(r * 3 * g, max(0, 3 * g - WIN))) * D * RATE * m


def lens2(g, r, m=1.0):
    return S * g * D * r * SHARE * RATE * m


# ---------------------------------------------------------------- opmaak van getallen
def h10(x):
    return f"{int(x / 10 + 0.5) * 10:,}"


def usd100(x):
    return f"${int(x / 100 + 0.5) * 100:,}"


def usd(x):
    return f"${int(round(x)):,}"


def signed(x):
    v = int(abs(x) / 100 + 0.5) * 100
    return f"+${v:,}" if x >= 0 else f"-${v:,}"


def pct(x):
    return f"{round(x * 100):.0f}%"


def e(t):
    return html.escape(t, quote=False)


# ---------------------------------------------------------------- inhoud
def chart(case, c):
    max_h = TOTAL_H
    rows = [
        ("Grading time today", TOTAL_H, "ctx", False),
        (f"Time the tool takes off ({pct(RED)} of grading time)", SAVED_H, "ctx", False),
    ]
    if case == "expected":
        rows += [
            ("Of that, in two- and three-section shifts", SAVED_MULTI, "ctx", False),
            ("Of that, grading outside scheduled hours: payroll savings", c["cash_h"], "key", True),
        ]
    else:
        rows += [
            ("Of that, in two- and three-section shifts: payroll savings (all of it, in this case)", SAVED_MULTI, "key", True),
        ]
    rows.append((f"Hours needed to cover the licence ({usd(COST)} at ${RATE:.0f} an hour)", NEED_H, "gate", False))
    out = []
    for lab, hrs, kind, is_key in rows:
        w = hrs / max_h * 100
        out.append(
            f'<div class="row{" is-key" if is_key else ""}"><div class="lab">{e(lab)}</div>'
            f'<div class="track"><div class="bar {kind}" style="width:{w:.2f}%"></div></div>'
            f'<div class="val">{h10(hrs)} h</div></div>'
        )
    cap = (f"Hours per year, all HVAC sections ({S:.0f} per day, {D:.0f} teaching days). "
           "Dark bar: hours that become payroll savings. Outlined bar: hours of payroll savings needed to cover the licence cost.")
    return f'<figure class="bars">{"".join(out)}<figcaption>{e(cap)}</figcaption></figure>'


def build(case):
    c = CASES[case]
    sav, net, ratio, cash_h = c["sav"], c["net"], c["ratio"], c["cash_h"]
    expected = case == "expected"

    # --- summary
    p1 = (f"UTI's HVAC program grew from about 29 to about 98 sections per course start in twelve months. The share of instructors "
          f"who teach two or three sections went from 14% to 42%, and those instructors grade more than their shift schedule leaves room for.")
    if expected:
        p2 = (f"Eduface proposes a score and written feedback for each lab submission, and the instructor reviews and approves it. "
              f"We expect this to take about {pct(RED)} off the grading time. On the assumptions in this document, about {h10(cash_h)} hours a year "
              f"of grading that today falls outside scheduled hours goes away. At ${RATE:.0f} an hour that is about {usd100(sav)}. "
              f"The licence for all HVAC students costs about {usd(COST)} a year, so the expected net result is about {usd100(net)} a year, "
              f"or ${ratio:.2f} back for every $1 spent.")
        p3 = (f"This is an estimate until the pilot measures it. The licence pays for itself if the tool removes about {NEED_MIN:.0f} minutes a day "
              f"from each instructor who teaches two or three sections. This case assumes about {c['min']:.0f}. A high case is a separate document.")
    else:
        p2 = (f"Eduface proposes a score and written feedback for each lab submission, and the instructor reviews and approves it. "
              f"We expect this to take about {pct(RED)} off the grading time. This case assumes that every hour saved in two- and three-section "
              f"shifts becomes a payroll saving. That is about {h10(cash_h)} hours a year, worth about {usd100(sav)} at ${RATE:.0f} an hour. "
              f"The licence for all HVAC students costs about {usd(COST)} a year, so the net result is about {usd100(net)} a year, "
              f"or ${ratio:.2f} back for every $1 spent.")
        p3 = (f"This is an upper bound, not a forecast. The expected case, a separate document, counts only grading outside scheduled hours. "
              f"The licence pays for itself if the tool removes about {NEED_MIN:.0f} minutes a day from each instructor who "
              f"teaches two or three sections. This case assumes about {c['min']:.0f}.")

    # --- HVAC today table
    today_rows = [
        ("HVAC sections per day", "About 100 (about 29 per course start in Oct 2025, about 98 in Oct 2026)", "UTI Operations, 10 Nov 2026; HVAC data export, 13 Nov 2026"),
        ("Instructors teaching HVAC", "66 (22 per course start in Oct 2025, 67 in Oct 2026)", "UTI Operations, 10 Nov 2026; HVAC data export"),
        ("Campuses with HVAC", "14", "HVAC data export"),
        ("Instructors with two or three sections", "42% of instructors and 60% of sections in Oct 2026 (14% and 24% in Oct 2025)", "HVAC data export"),
        ("Students per section, teaching days a year", f"{STUDENTS:.0f} students, {D:.0f} days (51 weeks, 5 days)", "UTI Operations, 13 Nov 2026"),
        ("Cost per instructor hour", f"${RATE:.0f} (UTI estimate)", "UTI Operations, 10 Nov 2026"),
        ("Grading time per section per day", "30 to 60 minutes (UTI estimate, not tracked)", "UTI Operations, 10 and 13 Nov 2026"),
    ]
    today = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(s)}</td></tr>" for a, b, s in today_rows)

    # --- gap table
    sw1, sw2 = f"{min(SINGLE_WIN):.1f} to {max(SINGLE_WIN):.1f} h", f"{WIN_AM:.1f} to {WIN_EVE:.1f} h ({WIN * 60:.0f} min on average)"
    need1, need2, need3 = G * 60, 2 * G * 60, 3 * G * 60
    gap = (
        f"<tr><td>One section</td><td class='n'>{pct(SEC1 / S)}</td><td>{sw1}</td><td class='n'>{need1:.0f} min</td><td>None</td></tr>"
        f"<tr><td>Two sections</td><td class='n'>{pct(SEC2 / S)}</td><td>{sw2}</td><td class='n'>{need2:.0f} min</td><td>About {OVER2 * 60:.0f} min</td></tr>"
        f"<tr><td>Three sections</td><td class='n'>{pct(SEC3 / S)}</td><td>No fixed limit</td><td class='n'>{need3:.0f} min</td><td>All of it</td></tr>"
    )

    # --- calculation table
    step4_text = ("Only the grading that falls outside scheduled hours: about {o2:.0f} of the {s2:.0f} minutes saved per day for a two-section "
                  "instructor, all saved time for a three-section instructor").format(o2=OVER2 * 60, s2=RED * 2 * G * 60) if expected else \
                 "All saved time in these shifts is counted as a payroll saving"
    calc = (
        f"<tr><td>1</td><td>Grading time today</td><td>{S:.0f} sections × {G:g} h × {D:.0f} days</td><td class='n'>{h10(TOTAL_H)} h</td><td>UTI Operations: 30 to 60 minutes, midpoint. Not measured.</td></tr>"
        f"<tr><td>2</td><td>Time the tool takes off</td><td>{pct(RED)} of step 1</td><td class='n'>{h10(SAVED_H)} h</td><td>Eduface assumption. Measured in the pilot.</td></tr>"
        f"<tr><td>3</td><td>In two- and three-section shifts</td><td>{pct(SHARE)} of sections (Oct 2026)</td><td class='n'>{h10(SAVED_MULTI)} h</td><td>HVAC data export. The other {h10(SAVED_SINGLE)} h fall in single-section shifts, paid 8 hours either way.</td></tr>"
        f"<tr><td>4</td><td>Becomes payroll savings</td><td>{step4_text}</td><td class='n'>{h10(cash_h)} h</td><td>UTI example shift schedules, 13 Nov 2026</td></tr>"
        f"<tr><td>5</td><td>Value</td><td>{h10(cash_h)} h × ${RATE:.0f}</td><td class='n'>{usd100(sav)}</td><td>UTI Operations, 10 Nov 2026</td></tr>"
        f"<tr><td>6</td><td>Licence cost</td><td>{LICENSED:,.0f} Licensed Students × ${PRICE:.2f} × 12 months</td><td class='n'>{usd(COST)}</td><td>Draft licence agreement, sent 16 Nov 2026, Articles 1.1, 5.1 and 5.4</td></tr>"
        f"<tr class='total'><td></td><td>Net result per year</td><td>Step 5 minus step 6</td><td class='n'>{usd100(net)}</td><td>${ratio:.2f} back for every $1 spent</td></tr>"
    )

    # --- sensitivity
    if expected:
        base = c["sav"]
        sens = [
            ("Base case", base),
            ("Grading takes 30 minutes per section instead of 45", lens1(0.5, RED)),
            ("Grading takes 60 minutes per section instead of 45", lens1(1.0, RED)),
            ("The tool removes 30% of grading time instead of 50%", lens1(G, 0.3)),
            ("Hours outside scheduled hours are paid at time and a half ($57 an hour)", lens1(G, RED, 1.5)),
        ]
        sens_note = ("The result depends most on how long grading really takes. At 30 minutes per section it fits inside the scheduled time and "
                     "leaves little to save in payroll. Once the tool removes more than about 30% of grading time, the result no longer depends on "
                     "that percentage, because the grading outside scheduled hours is already gone.")
    else:
        base = c["sav"]
        sens = [
            ("Base case", base),
            ("Grading takes 30 minutes per section instead of 45", lens2(0.5, RED)),
            ("Grading takes 60 minutes per section instead of 45", lens2(1.0, RED)),
            ("The tool removes 30% of grading time instead of 50%", lens2(G, 0.3)),
            ("Hours in these shifts are paid at time and a half ($57 an hour)", lens2(G, RED, 1.5)),
        ]
        sens_note = ("This case moves in proportion to grading time, to the share the tool removes, and to the hourly rate. It is the ceiling, "
                     "because it counts every saved hour as money.")
    sens = [(lab, v, COST) for lab, v in sens]
    sens.append((f"3,000 Licensed Students are billed instead of {LICENSED:,.0f} (more students drop out)", base, 3000 * PRICE * 12))
    sens_rows = "".join(
        f"<tr{' class=total' if i == 0 else ''}><td>{e(lab)}</td><td class='n'>{usd100(v)}</td><td class='n'>{signed(v - cost)}</td></tr>"
        for i, (lab, v, cost) in enumerate(sens)
    )

    # --- aanvullende waarde
    fte = SAVED_SINGLE / 2080
    leavers = 66 * 0.20

    html_doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Eduface in HVAC: business case for Universal Technical Institute ({c['label']})</title>
<link rel="stylesheet" href="file://{HERE}/style.css"></head><body>
<img class="brand" src="file://{LOGO}" alt="Eduface">
<h1>Eduface in HVAC: business case for Universal Technical Institute</h1>
<p class="case">{e(c['label'])}</p>
<p class="status">Draft for validation by UTI, 24 Nov 2026. Prepared by Eduface from figures supplied by UTI Operations (10 to 18 Nov 2026). Every input names its source.</p>

<p class="lead">{e(p1)}</p>
<p>{e(p2)}</p>
{chart(case, c)}
<p style="margin-top:var(--s3)">{e(p3)}</p>

<h2>Customer context</h2>
<h3>What UTI is working toward</h3>
<ul>
<li>UTI's North Star strategy is mainly campus growth, diversification and optimization (UTI, 18 Sep 2026).</li>
<li>UTI adds two new campuses a year and brings existing programs to as many campuses as possible (UTI, 18 Sep 2026). HVAC already runs at 14 campuses.</li>
<li>Instructor supply is the constraint. Some campuses struggle to hire and keep instructors, and UTI moves instructors across the country to teach courses (UTI, 18 Sep 2026).</li>
<li>Instructor pay is one of the largest variable costs that education directors manage. Hourly instructors who grade have no time left to tutor (UTI, 18 Sep 2026).</li>
</ul>

<table><caption>HVAC at UTI today</caption><colgroup><col style="width:30%"><col style="width:44%"><col style="width:26%"></colgroup>
<thead><tr><th>Measure</th><th>Value</th><th>Source</th></tr></thead><tbody>{today}</tbody></table>
<p class="src">A section is one 5-hour class of about {STUDENTS:.0f} students. UTI Operations does not track grading time or turnover causes separately, so grading time and the cost of an instructor hour are estimates.</p>

<h3>Where the grading pressure sits</h3>
<p>Instructors who teach one section are paid for 8 hours and have about 2.5 to 2.8 hours scheduled after class for grading, preparation and training aid work. Grading fits. Instructors who teach two sections work a 12-hour shift with only {WIN * 60:.0f} minutes on average scheduled for the same tasks, so two sections at {need1:.0f} minutes each leave a gap of about {OVER2 * 60:.0f} minutes a day outside scheduled hours. Instructors with three sections get as much time as they need.</p>
<table class="keep"><caption>Scheduled time against grading needed, at {need1:.0f} minutes per section</caption><colgroup><col style="width:17%"><col style="width:14%"><col style="width:33%"><col style="width:16%"><col style="width:20%"></colgroup>
<thead><tr><th>Shift</th><th class="n">Share of sections</th><th>Scheduled for grading, prep and training aids</th><th class="n">Grading needed</th><th>Gap per day</th></tr></thead><tbody>{gap}</tbody></table>
<p class="src">UTI example shift schedules and HVAC data export, 13 Nov 2026; UTI Operations estimate of 30 to 60 minutes per section, 10 Nov 2026 (midpoint used). Gap calculated by Eduface.</p>
<p>Over a year, grading outside scheduled hours adds up to about {h10(CEIL_H)} hours, or about {usd100(CEIL_H * RATE)} at ${RATE:.0f} an hour if it is paid time. UTI Operations has not yet confirmed how these hours are paid, and the payroll data it checked was not representative, so the pilot baseline will settle it. Earlier conversations (26 Aug 2026) cited 2 to 4 hours of grading a day. This case uses the lower figure from UTI Operations.</p>

<h2>Current and future state</h2>
<table><caption>How a lab submission is handled</caption><colgroup><col style="width:18%"><col style="width:41%"><col style="width:41%"></colgroup>
<thead><tr><th>Step</th><th>Today</th><th>With Eduface</th></tr></thead><tbody>
<tr><td>Submission</td><td>Students upload lab documents in Blackboard Ultra.</td><td>Unchanged for students.</td></tr>
<tr><td>Marking</td><td>The instructor marks each lab by hand. Blackboard auto-grading only accepts exact matches, so an answer one character off counts as wrong.</td><td>Eduface reads each submission against UTI's own answer key and rubric and proposes a score with feedback per criterion. It marks where it is unsure.</td></tr>
<tr><td>Review</td><td>The instructor is the marker.</td><td>The instructor checks, edits and approves each proposal. Nothing reaches the student or the gradebook before that.</td></tr>
<tr><td>Feedback to students</td><td>Mostly verbal and occasional, and not measured.</td><td>Written feedback per criterion, inside Blackboard.</td></tr>
<tr><td>Gradebook</td><td>The instructor enters the grade.</td><td>The approved grade and feedback sync to the Blackboard gradebook.</td></tr>
<tr><td>Instructor time</td><td>Grading in the hours after class, often in the evening.</td><td>Less grading time per submission. The freed time can go to preparation, training aids and tutoring.</td></tr>
</tbody></table>
<p class="src">Eduface product description; demonstration on UTI's own labs, 1 Sep 2026; UTI statements, 26 Aug and 18 Sep 2026.</p>

<table><caption>Decision criteria UTI has raised or agreed, and where each stands</caption><colgroup><col style="width:24%"><col style="width:18%"><col style="width:30%"><col style="width:28%"></colgroup>
<thead><tr><th>Criterion</th><th>Raised or agreed by</th><th>How it is addressed</th><th>Status</th></tr></thead><tbody>
<tr><td>Works inside Blackboard Ultra, grades sync to the gradebook</td><td>UTI, 26 Aug 2026</td><td>LTI 1.3 connection. Approved grades and feedback sync back.</td><td>First call 19 Nov 2026. First course set up by 7 Dec 2026 (target).</td></tr>
<tr><td>Instructor stays in control</td><td>UTI and Concorde, 25 Sep 2026</td><td>The instructor approves every proposal before the student sees it.</td><td>By design. In the draft licence agreement, Article 10.2.</td></tr>
<tr><td>Accuracy above 90% after calibration</td><td>UTI, 18 Sep 2026</td><td>Tuned per course on UTI's answer keys and rubrics.</td><td>To validate in the pilot.</td></tr>
<tr><td>Student data is not used to train AI</td><td>UTI IT, 25 Sep 2026</td><td>Contractual commitment.</td><td>In the draft licence agreement, Article 10.3.</td></tr>
<tr><td>Accessibility documentation</td><td>UTI, 1 Sep 2026</td><td>VPAT, WCAG 2.2 AA, report of July 2026.</td><td>Shared 2 Sep 2026.</td></tr>
<tr><td>Security and legal review</td><td>UTI</td><td>Questionnaire returned 27 Oct 2026.</td><td>Security review completed 6 Nov 2026. Legal review in progress.</td></tr>
<tr><td>Little setup work per course</td><td>UTI, 18 Sep 2026</td><td>Course setup with the program lead in four calls over two weeks.</td><td>To validate in the first course.</td></tr>
</tbody></table>
<h2>Cost justification</h2>
<table class="keep"><caption>How the savings are calculated ({e(c['label'].lower())})</caption><colgroup><col style="width:6%"><col style="width:19%"><col style="width:31%"><col style="width:12%"><col style="width:32%"></colgroup>
<thead><tr><th>Step</th><th>What</th><th>Calculation</th><th class="n">Result</th><th>Basis</th></tr></thead><tbody>{calc}</tbody></table>
<p class="src">A Licensed Student is a student with a submission processed in the month or in the three months before (Article 1.1). At this size the count is rounded up to the next 250 (Article 5.4). We estimate {LICENSED:,.0f}: about {IN_CLASS:,.0f} students in class plus about {h10(TAIL)} who finished in the last three months. Students who drop out are not included, so the count may be higher. Every 250 students adds {usd(250 * PRICE * 12)} a year. Onboarding, one LMS integration, training for up to 50 users and standard support are included (Article 8.2). No fee accrues in months without students (Article 5.3).</p>

<table class="keep"><caption>What moves the result</caption><colgroup><col style="width:62%"><col style="width:19%"><col style="width:19%"></colgroup>
<thead><tr><th>If this changes</th><th class="n">Payroll savings a year</th><th class="n">Net of licence cost</th></tr></thead><tbody>{sens_rows}</tbody></table>
<p class="src">{e(sens_note)} Other inputs as in the base case.</p>

<h3>Not counted in the numbers</h3>
<ul>
<li><strong>Time returned in single-section shifts.</strong> About {h10(SAVED_SINGLE)} hours a year, roughly {fte:.1f} full-time equivalents (2,080 hours each). Single-section instructors are paid 8 hours either way, so it is not a payroll saving. It is time for preparation, training aids and tutoring.</li>
<li><strong>Turnover.</strong> Last year 37% of HVAC instructors left (25 of 66); UTI Operations suggests 20% as a planning figure (18 Nov 2026). At 20%, about {leavers:.0f} leave a year, and replacing an instructor costs $10,000 to $15,000 (10 Nov 2026), so $132,000 to $198,000. If better workload kept one in ten of them, that is $13,000 to $20,000 a year. UTI Operations links turnover to HVAC growth, and there is no evidence yet that grading load causes departures, so none is counted.</li>
<li><strong>Quality and completion.</strong> Consistent written feedback on every submission, and the effect of freed instructor time on course completion, which UTI tracks and Eduface has not seen.</li>
</ul>

<h2>Validation and plan</h2>
<table class="keep"><caption>What the pilot measures</caption><colgroup><col style="width:24%"><col style="width:50%"><col style="width:26%"></colgroup>
<thead><tr><th>Measure</th><th>How</th><th>Tests</th></tr></thead><tbody>
<tr><td>Grading time per section per day</td><td>A control group of instructors logs grading time for 1 to 2 weeks before the pilot, then during it (agreed in principle by UTI Operations, 13 Nov 2026).</td><td>The 45 minutes and the {pct(RED)}</td></tr>
<tr><td>Grading outside scheduled hours</td><td>The same group, per course start, for instructors with one, two and three sections.</td><td>The gap of about {OVER2 * 60:.0f} minutes</td></tr>
<tr><td>Pay rules for two- and three-section shifts</td><td>UTI Operations confirms how the hours are paid and at what rate.</td><td>Whether the gap is paid time, and the hourly rate</td></tr>
<tr><td>Accuracy</td><td>Difference between the score Eduface proposes and the instructor's final score on pilot submissions.</td><td>The 90% criterion</td></tr>
</tbody></table>

<p class="src">Sector evidence for the accuracy criterion, not UTI evidence: a UK university pilot in June 2026 (435 assignments, 13 instructors) averaged about 6 points from the instructor's grade, and about 2 points where instructors had tuned the model. That was written work, not lab short answers.</p>
<h3>Decision rule</h3>
<p>The licence pays for itself if the pilot shows about {NEED_MIN:.0f} minutes a day less paid or overtime grading per instructor with two or three sections. Across HVAC that is about {h10(NEED_H)} hours a year at ${RATE:.0f}. This case assumes {c['min']:.0f} minutes. After the pilot we replace the assumptions with the measured values and update this document.</p>

<table><caption>Plan</caption><colgroup><col style="width:46%"><col style="width:32%"><col style="width:22%"></colgroup>
<thead><tr><th>Step</th><th>Who</th><th>When</th></tr></thead><tbody>
<tr><td>Licence agreement and DPA sent to UTI</td><td>Jeroen van Gessel</td><td>16 Nov 2026</td></tr>
<tr><td>Licence agreement reviewed by UTI Legal and procurement</td><td>UTI Legal</td><td>To confirm</td></tr>
<tr><td>LTI 1.3 connection in Blackboard Ultra, first call</td><td>Jeroen van Gessel, Dante Torbed and Charlie Rosenbam</td><td>19 Nov 2026</td></tr>
<tr><td>First HVAC course fully set up (four calls over two weeks)</td><td>Dante Torbed and Dan Lawson</td><td>7 Dec 2026 (target)</td></tr>
<tr><td>Baseline grading-time measurement</td><td>Bas Schotsman and a control group of instructors</td><td>To confirm</td></tr>
<tr><td>Days on campus, Bloomfield</td><td>Dante Torbed, Jeroen van Gessel, Menno Hahury and Dan Lawson</td><td>18 to 20 Jan 2027 (tentative)</td></tr>
<tr><td>Pilot go-live, HVAC 101, about 125 students</td><td>Robert Jordan</td><td>Jan 2027, date to be set</td></tr>
<tr><td>Pilot results and updated business case</td><td>Eduface and UTI Operations</td><td>To confirm</td></tr>
<tr><td>Decision on HVAC-wide rollout</td><td>UTI leadership</td><td>To confirm, subject to UTI budget</td></tr>
</tbody></table>

<p class="src">If UTI moves from Blackboard to Canvas later, Eduface also integrates with Canvas, so a migration does not need a new contract (UTI Q&amp;A, go-live plan, 12 Nov 2026).</p>
<h3>Assumptions to validate</h3>
<ol>
<li>Grading takes 45 minutes per section per day. UTI Operations estimates 30 to 60 and does not track it.</li>
<li>The tool removes about {pct(RED)} of that time. Eduface has not yet measured this on UTI's labs.</li>
<li>{"Grading outside scheduled hours is paid time, at $38 an hour." if expected else "Every saved hour in two- and three-section shifts reduces paid hours, at $38 an hour."} How these hours are paid is not yet confirmed.</li>
<li>HVAC runs at about 100 sections and about {IN_CLASS:,.0f} students in class across the year ({LICENSED:,.0f} Licensed Students), with the mix of Oct 2026. Growth raises both the licence cost and the gap.</li>
<li>The licence terms in the draft agreement of 16 Nov 2026 stay as sent.</li>
</ol>
<p class="src">Contact: Dante Torbed, Customer Success Manager, Eduface, dante.torbed@eduface.me. Figures are rounded: hours to the nearest 10, dollars to the nearest $100. The model behind this document is available on request.</p>
</body></html>"""
    return html_doc


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for case in CASES:
        name = f"UTI_Business_Case_{case.capitalize()}"
        BUILD = HERE / "_build"
        BUILD.mkdir(exist_ok=True)
        src = BUILD / f"{name}.html"
        src.write_text(build(case), encoding="utf-8")
        pdf = OUT_DIR / f"{name}.pdf"
        subprocess.run(["node", str(HERE / "render.js"), str(src), str(pdf)], check=True, cwd=str(HERE))
        print("wrote", pdf)


if __name__ == "__main__":
    main()
