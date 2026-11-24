"""Bouwt de UTI business case (expected case en high case in een document) als PDF.

Alle cijfers komen uit GTM/Accounts/uti/business-case-berekening.xlsx (gecachte waarden),
zodat het document nooit afwijkt van het model.

Gebruik:  python3 -I GTM/Accounts/uti/business-case/build.py [uitvoermap]
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
SEC1, SEC2, SEC3 = B["B12"].value, B["B13"].value, B["B14"].value
TOTAL_H = B["B16"].value
SAVED_H = B["B21"].value
SAVED_SINGLE = B["B22"].value
SAVED_MULTI = B["B23"].value
IN_CLASS = B["B29"].value
LICENSED = B["B30"].value  # betaalde studenten (= studenten in de klas, geen staartje)
COST = B["B31"].value
WIN = R["H35"].value
WIN_AM, WIN_EVE = R["H33"].value, R["H34"].value
SINGLE_WIN = [R.cell(r, 8).value for r in (30, 31, 32)]
EXP = dict(cash_h=M["C14"].value, sav=M["C15"].value, ratio=M["C18"].value)
HIGH = dict(cash_h=M["D14"].value, sav=M["D15"].value, ratio=M["D18"].value)

DD, TD = SEC2 / 2, SEC3 / 3
INSTR_DAYS = (DD + TD) * D
OVER2 = max(0.0, 2 * G - WIN)
OVER3 = max(0.0, 3 * G - WIN)
CEIL_H = (DD * OVER2 + TD * OVER3) * D
NEED_H = COST / RATE
NEED_MIN = NEED_H / INSTR_DAYS * 60
for c in (EXP, HIGH):
    c["min"] = c["cash_h"] / INSTR_DAYS * 60


def lens1(g, r, m=1.0):
    return (DD * min(r * 2 * g, max(0, 2 * g - WIN)) + TD * min(r * 3 * g, max(0, 3 * g - WIN))) * D * RATE * m


def lens2(g, r, m=1.0):
    return S * g * D * r * SHARE * RATE * m


# ---------------------------------------------------------------- opmaak van getallen
def r100(x):
    return int(abs(x) / 100 + 0.5) * 100


def h10(x):
    return f"{int(x / 10 + 0.5) * 10:,}"


def usd100(x):
    return f"${r100(x):,}"


def usd(x):
    return f"${int(round(x)):,}"


def net_text(sav, cost):
    v = r100(sav) - r100(cost)
    return f"+${v:,}" if v >= 0 else f"-${abs(v):,}"


def pct(x):
    return f"{round(x * 100):.0f}%"


def e(t):
    return html.escape(t, quote=False)


def cg(widths):
    return "<colgroup>" + "".join(f'<col style="width:{w}%">' for w in widths) + "</colgroup>"


# ---------------------------------------------------------------- inhoud
def chart():
    rows = [
        ("Grading time today", TOTAL_H, "ctx", False),
        (f"Time the tool takes off ({pct(RED)} of grading time)", SAVED_H, "ctx", False),
        ("High case: all hours saved in two- and three-section shifts", HIGH["cash_h"], "key", True),
        ("Expected case: only grading outside scheduled hours", EXP["cash_h"], "key", True),
        (f"Hours needed to cover the licence ({usd100(COST)} at ${RATE:.0f} an hour)", NEED_H, "gate", False),
    ]
    out = []
    for lab, hrs, kind, is_key in rows:
        w = hrs / TOTAL_H * 100
        out.append(
            f'<div class="row{" is-key" if is_key else ""}"><div class="lab">{e(lab)}</div>'
            f'<div class="track"><div class="bar {kind}" style="width:{w:.2f}%"></div></div>'
            f'<div class="val">{h10(hrs)} h</div></div>'
        )
    cap = "Hours per year, all HVAC sections. Dark bars: hours that become payroll savings. Outlined bar: hours needed to cover the licence cost."
    return f'<figure class="bars">{"".join(out)}<figcaption>{e(cap)}</figcaption></figure>'


def build():
    # --- first page
    p1 = ("UTI's HVAC program grew from about 29 to about 98 sections per course start in twelve months. The share of instructors teaching two or "
          "three sections went from 14% to 42%, and they grade more than their shift schedule leaves room for.")
    p2 = (f"Eduface proposes a score and written feedback for each lab submission, and the instructor reviews and approves it. We expect this to "
          f"take about {pct(RED)} off the grading time. This document shows an expected case and a high case. The high case is an upper bound, not a "
          f"forecast. Both are estimates until the pilot measures them.")

    glance = (
        f"<tr><td>Payroll savings a year</td><td class='n'>{usd100(EXP['sav'])}</td><td class='n'>{usd100(HIGH['sav'])}</td></tr>"
        f"<tr><td>Licence cost a year</td><td class='n'>{usd100(COST)}</td><td class='n'>{usd100(COST)}</td></tr>"
        f"<tr class='total'><td>Net result a year</td><td class='n'>{net_text(EXP['sav'], COST)}</td><td class='n'>{net_text(HIGH['sav'], COST)}</td></tr>"
        f"<tr><td>Back for every $1 spent</td><td class='n'>${EXP['ratio']:.2f}</td><td class='n'>${HIGH['ratio']:.2f}</td></tr>"
    )

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

    sw1 = f"{min(SINGLE_WIN):.1f} to {max(SINGLE_WIN):.1f} h"
    sw2 = f"{WIN_AM:.1f} to {WIN_EVE:.1f} h ({WIN * 60:.0f} min on average)"
    need1, need2, need3 = G * 60, 2 * G * 60, 3 * G * 60
    gap = (
        f"<tr><td>One section</td><td class='n'>{pct(SEC1 / S)}</td><td>{sw1}</td><td class='n'>{need1:.0f} min</td><td>None</td></tr>"
        f"<tr><td>Two sections</td><td class='n'>{pct(SEC2 / S)}</td><td>{sw2}</td><td class='n'>{need2:.0f} min</td><td>About {OVER2 * 60:.0f} min</td></tr>"
        f"<tr><td>Three sections</td><td class='n'>{pct(SEC3 / S)}</td><td>No fixed limit</td><td class='n'>{need3:.0f} min</td><td>All of it</td></tr>"
    )

    # --- calculation table: both cases side by side
    step4_exp = (f"<strong>Expected:</strong> only grading that falls outside scheduled hours, about {OVER2 * 60:.0f} of the {RED * 2 * G * 60:.0f} minutes saved "
                 f"per day for a two-section instructor, all saved time for three sections. <strong>High:</strong> all saved time in these shifts.")
    calc = (
        f"<tr><td>1</td><td>Grading time today</td><td>{S:.0f} sections × {G:g} h × {D:.0f} days</td><td class='n' colspan='2'>{h10(TOTAL_H)} h, both cases</td><td>UTI Operations: 30 to 60 minutes, midpoint. Not measured.</td></tr>"
        f"<tr><td>2</td><td>Time the tool takes off</td><td>{pct(RED)} of step 1</td><td class='n' colspan='2'>{h10(SAVED_H)} h, both cases</td><td>Eduface assumption. Measured in the pilot.</td></tr>"
        f"<tr><td>3</td><td>In two- and three-section shifts</td><td>{pct(SHARE)} of sections (Oct 2026)</td><td class='n' colspan='2'>{h10(SAVED_MULTI)} h, both cases</td><td>HVAC data export. The other {h10(SAVED_SINGLE)} h fall in single-section shifts, paid 8 hours either way.</td></tr>"
        f"<tr><td>4</td><td>Becomes payroll savings</td><td>{step4_exp}</td><td class='n'>{h10(EXP['cash_h'])} h</td><td class='n'>{h10(HIGH['cash_h'])} h</td><td>UTI example shift schedules, 13 Nov 2026</td></tr>"
        f"<tr><td>5</td><td>Value</td><td>Hours × ${RATE:.0f}</td><td class='n'>{usd100(EXP['sav'])}</td><td class='n'>{usd100(HIGH['sav'])}</td><td>UTI Operations, 10 Nov 2026</td></tr>"
        f"<tr><td>6</td><td>Licence cost</td><td>{IN_CLASS:,.0f} students × ${PRICE:.2f} × 12 months</td><td class='n' colspan='2'>{usd100(COST)}, both cases</td><td>Draft licence agreement, sent 16 Nov 2026, Article 5.1</td></tr>"
        f"<tr class='total'><td></td><td>Net result per year</td><td>Step 5 minus step 6</td><td class='n'>{net_text(EXP['sav'], COST)}</td><td class='n'>{net_text(HIGH['sav'], COST)}</td><td></td></tr>"
        f"<tr><td></td><td>Back for every $1 spent</td><td>Step 5 divided by step 6</td><td class='n'>${EXP['ratio']:.2f}</td><td class='n'>${HIGH['ratio']:.2f}</td><td></td></tr>"
    )

    # --- sensitivity, both cases
    base_e, base_h = EXP["sav"], HIGH["sav"]
    sens = [
        ("Base case", base_e, base_h, COST),
        ("Grading takes 30 minutes per section instead of 45", lens1(0.5, RED), lens2(0.5, RED), COST),
        ("Grading takes 60 minutes per section instead of 45", lens1(1.0, RED), lens2(1.0, RED), COST),
        ("The tool removes 30% of grading time instead of 50%", lens1(G, 0.3), lens2(G, 0.3), COST),
        (f"Hours are paid at time and a half (${RATE * 1.5:.0f} an hour)", lens1(G, RED, 1.5), lens2(G, RED, 1.5), COST),
        (f"2,500 students instead of {LICENSED:,.0f} (sections keep growing)", base_e, base_h, 2500 * PRICE * 12),
    ]
    sens_rows = "".join(
        f"<tr{' class=total' if i == 0 else ''}><td>{e(lab)}</td><td class='n'>{usd100(a)}</td><td class='n'>{net_text(a, cost)}</td>"
        f"<td class='n'>{usd100(b)}</td><td class='n'>{net_text(b, cost)}</td></tr>"
        for i, (lab, a, b, cost) in enumerate(sens)
    )
    sens_note = ("In the expected case the result depends most on how long grading really takes. At 30 minutes per section it fits inside the scheduled time "
                 "and leaves little to save in payroll. Once the tool removes more than about 30% of grading time, the expected case no longer depends on "
                 "that percentage, because the grading outside scheduled hours is already gone. The high case moves in proportion to grading time, the share "
                 "the tool removes and the hourly rate, because it counts every saved hour as money.")

    fte = SAVED_SINGLE / 2080
    leavers = 66 * 0.20

    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Eduface in HVAC: business case for Universal Technical Institute</title>
<link rel="stylesheet" href="file://{HERE}/style.css"></head><body>
<img class="brand" src="file://{LOGO}" alt="Eduface">
<h1>Eduface in HVAC: business case for Universal Technical Institute</h1>
<p class="case">Expected case and high case</p>
<p class="status">Draft for validation by UTI, 24 Nov 2026. Prepared by Eduface from figures supplied by UTI Operations. Every input names its source.</p>

<p class="lead">{e(p1)}</p>
<p>{e(p2)}</p>
{chart()}

<table class="keep"><caption>The two cases at a glance</caption>{cg((46, 27, 27))}
<thead><tr><th></th><th>Expected case</th><th>High case</th></tr></thead><tbody>{glance}</tbody></table>

<h2>Customer context</h2>
<h3>What UTI is working toward</h3>
<ul>
<li>UTI's North Star strategy is mainly campus growth, diversification and optimization (UTI, 18 Sep 2026).</li>
<li>UTI adds two new campuses a year and brings existing programs to as many campuses as possible (UTI, 18 Sep 2026). HVAC already runs at 14 campuses.</li>
<li>Instructor supply is the constraint. Some campuses struggle to hire and keep instructors, and UTI moves instructors across the country to teach courses (UTI, 18 Sep 2026).</li>
<li>Instructor pay is one of the largest variable costs that education directors manage. Hourly instructors who grade have no time left to tutor (UTI, 18 Sep 2026).</li>
</ul>

<table class="keep"><caption>HVAC at UTI today</caption>{cg((30, 44, 26))}
<thead><tr><th>Measure</th><th>Value</th><th>Source</th></tr></thead><tbody>{today}</tbody></table>
<p class="src">A section is one 5-hour class of about {STUDENTS:.0f} students. UTI Operations does not track grading time or turnover causes separately, so grading time and the cost of an instructor hour are estimates.</p>

<h3>Where the grading pressure sits</h3>
<p>Instructors who teach one section are paid for 8 hours and have about 2.5 to 2.8 hours scheduled after class for grading, preparation and training aid work. Grading fits. Instructors who teach two sections work a 12-hour shift with only {WIN * 60:.0f} minutes on average scheduled for the same tasks, so two sections at {need1:.0f} minutes each leave a gap of about {OVER2 * 60:.0f} minutes a day outside scheduled hours. Instructors with three sections get as much time as they need.</p>
<table class="keep"><caption>Scheduled time against grading needed, at {need1:.0f} minutes per section</caption>{cg((17, 14, 33, 16, 20))}
<thead><tr><th>Shift</th><th class="n">Share of sections</th><th>Scheduled for grading, prep and training aids</th><th class="n">Grading needed</th><th>Gap per day</th></tr></thead><tbody>{gap}</tbody></table>
<p class="src">UTI example shift schedules and HVAC data export, 13 Nov 2026; UTI Operations estimate of 30 to 60 minutes per section, 10 Nov 2026 (midpoint used). Gap calculated by Eduface.</p>
<p>Over a year, grading outside scheduled hours adds up to about {h10(CEIL_H)} hours, or about {usd100(CEIL_H * RATE)} at ${RATE:.0f} an hour if it is paid time. UTI Operations has not yet confirmed how these hours are paid, and the payroll data it checked was not representative, so the pilot baseline will settle it. Earlier conversations (26 Aug 2026) cited 2 to 4 hours of grading a day. This document uses the lower figure from UTI Operations.</p>

<h2>Current and future state</h2>
<table><caption>How a lab submission is handled</caption>{cg((18, 41, 41))}
<thead><tr><th>Step</th><th>Today</th><th>With Eduface</th></tr></thead><tbody>
<tr><td>Submission</td><td>Students upload lab documents in Blackboard Ultra.</td><td>Unchanged for students.</td></tr>
<tr><td>Marking</td><td>The instructor marks each lab by hand. Blackboard auto-grading only accepts exact matches, so an answer one character off counts as wrong.</td><td>Eduface reads each submission against UTI's own answer key and rubric and proposes a score with feedback per criterion. It marks where it is unsure.</td></tr>
<tr><td>Review</td><td>The instructor is the marker.</td><td>The instructor checks, edits and approves each proposal. Nothing reaches the student or the gradebook before that.</td></tr>
<tr><td>Feedback to students</td><td>Mostly verbal and occasional, and not measured.</td><td>Written feedback per criterion, inside Blackboard.</td></tr>
<tr><td>Gradebook</td><td>The instructor enters the grade.</td><td>The approved grade and feedback sync to the Blackboard gradebook.</td></tr>
<tr><td>Instructor time</td><td>Grading in the hours after class, often in the evening.</td><td>Less grading time per submission. The freed time can go to preparation, training aids and tutoring.</td></tr>
</tbody></table>
<p class="src">Eduface product description; demonstration on UTI's own labs, 1 Sep 2026; UTI statements, 26 Aug and 18 Sep 2026.</p>

<table><caption>Decision criteria UTI has raised or agreed, and where each stands</caption>{cg((24, 18, 30, 28))}
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
<table><caption>How the savings are calculated, expected case and high case</caption>{cg((5, 15, 27, 11, 11, 31))}
<thead><tr><th>Step</th><th>What</th><th>Calculation</th><th class="n">Expected case</th><th class="n">High case</th><th>Basis</th></tr></thead><tbody>{calc}</tbody></table>
<p class="src">The licence cost is the number of students times ${PRICE:.2f} per student per month (Article 5.1). Every 100 students adds {usd(100 * PRICE * 12)} a year. Onboarding, one LMS integration, training for up to 50 users and standard support are included (Article 8.2). No fee accrues in months without students (Article 5.3).</p>

<table class="keep"><caption>What moves the result</caption>{cg((44, 14, 14, 14, 14))}
<thead><tr><th>If this changes</th><th class="n">Expected: savings</th><th class="n">Expected: net</th><th class="n">High: savings</th><th class="n">High: net</th></tr></thead><tbody>{sens_rows}</tbody></table>
<p class="src">Savings are payroll savings a year; net is after the licence cost. {e(sens_note)} Other inputs as in the base case.</p>

<h3>Not counted in the numbers</h3>
<ul>
<li><strong>Time returned in single-section shifts.</strong> About {h10(SAVED_SINGLE)} hours a year, roughly {fte:.1f} full-time equivalents (2,080 hours each). Single-section instructors are paid 8 hours either way, so it is not a payroll saving. It is time for preparation, training aids and tutoring.</li>
<li><strong>Turnover.</strong> Last year 37% of HVAC instructors left (25 of 66); UTI Operations suggests 20% as a planning figure (18 Nov 2026). At 20%, about {leavers:.0f} leave a year, and replacing an instructor costs $10,000 to $15,000 (10 Nov 2026), so $132,000 to $198,000. If better workload kept one in ten of them, that is $13,000 to $20,000 a year. UTI Operations links turnover to HVAC growth, and there is no evidence yet that grading load causes departures, so none is counted.</li>
<li><strong>Quality and completion.</strong> Consistent written feedback on every submission, and the effect of freed instructor time on course completion, which UTI tracks and Eduface has not seen.</li>
</ul>

<h2>Validation and plan</h2>
<table class="keep"><caption>What the pilot measures</caption>{cg((24, 50, 26))}
<thead><tr><th>Measure</th><th>How</th><th>Tests</th></tr></thead><tbody>
<tr><td>Grading time per section per day</td><td>A control group of instructors logs grading time for 1 to 2 weeks before the pilot, then during it (agreed in principle by UTI Operations, 13 Nov 2026).</td><td>The 45 minutes and the {pct(RED)}</td></tr>
<tr><td>Grading outside scheduled hours</td><td>The same group, per course start, for instructors with one, two and three sections.</td><td>The gap of about {OVER2 * 60:.0f} minutes</td></tr>
<tr><td>Pay rules for two- and three-section shifts</td><td>UTI Operations confirms how the hours are paid and at what rate.</td><td>Whether the gap is paid time, and the hourly rate</td></tr>
<tr><td>Accuracy</td><td>Difference between the score Eduface proposes and the instructor's final score on pilot submissions.</td><td>The 90% criterion</td></tr>
</tbody></table>
<p class="src">Sector evidence for the accuracy criterion, not UTI evidence: a UK university pilot in June 2026 (435 assignments, 13 instructors) averaged about 6 points from the instructor's grade, and about 2 points where instructors had tuned the model. That was written work, not lab short answers.</p>

<h3>Decision rule</h3>
<p>The licence pays for itself if the pilot shows about {NEED_MIN:.0f} minutes a day less paid or overtime grading per instructor with two or three sections. Across HVAC that is about {h10(NEED_H)} hours a year at ${RATE:.0f}. The expected case assumes {EXP['min']:.0f} minutes, the high case {HIGH['min']:.0f}. After the pilot we replace the assumptions with the measured values and update this document.</p>

<table><caption>Plan</caption>{cg((46, 32, 22))}
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
<li>Expected case: grading outside scheduled hours is paid time, at $38 an hour. High case: every saved hour in two- and three-section shifts reduces paid hours, at $38 an hour. How these hours are paid is not yet confirmed.</li>
<li>HVAC runs at about 100 sections and about {IN_CLASS:,.0f} students across the year, with the mix of Oct 2026. Growth raises both the licence cost and the gap.</li>
<li>The licence terms in the draft agreement of 16 Nov 2026 stay as sent.</li>
</ol>
<p class="src">Contact: Dante Torbed, Customer Success Manager, Eduface, dante.torbed@eduface.me. Figures are rounded: hours to the nearest 10, dollars to the nearest $100. The model behind this document is available on request.</p>
</body></html>"""


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    BUILD = HERE / "_build"
    BUILD.mkdir(exist_ok=True)
    src = BUILD / "UTI_Business_Case.html"
    src.write_text(build(), encoding="utf-8")
    pdf = OUT_DIR / "UTI_Business_Case.pdf"
    subprocess.run(["node", str(HERE / "render.js"), str(src), str(pdf)], check=True, cwd=str(HERE))
    print("wrote", pdf)


if __name__ == "__main__":
    main()
