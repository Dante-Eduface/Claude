"""Bouwt de UTI business case (low, expected en high case in een document) als PDF.

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
# Samenvatting: B = Low (alleen overloop), C = Expected (alle tijdwinst, r = 50%), D = High (bullish, r = 70%)
LOW = dict(cash_h=M["B14"].value, sav=M["B15"].value, ratio=M["B18"].value)
EXP = dict(cash_h=M["C14"].value, sav=M["C15"].value, ratio=M["C18"].value)
HIGH = dict(cash_h=M["D14"].value, sav=M["D15"].value, ratio=M["D18"].value)
RED_H = M["D6"].value      # reductie in de high case
SAVED_H_HIGH = TOTAL_H * RED_H
SAVED_MULTI_HIGH = SAVED_MULTI * RED_H / RED

DD, TD = SEC2 / 2, SEC3 / 3
INSTR_DAYS = (DD + TD) * D
OVER2 = max(0.0, 2 * G - WIN)
OVER3 = max(0.0, 3 * G - WIN)
CEIL_H = (DD * OVER2 + TD * OVER3) * D
NEED_H = COST / RATE
NEED_MIN = NEED_H / INSTR_DAYS * 60
for c in (LOW, EXP, HIGH):
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
        ("High case: hours freed and valued", HIGH["cash_h"], "key", True),
        ("Expected case: hours freed and valued", EXP["cash_h"], "key", True),
        ("Low case: hours outside scheduled time", LOW["cash_h"], "key", True),
        (f"Needed to cover the licence ({usd100(COST)})", NEED_H, "gate", False),
    ]
    out = []
    for lab, hrs, kind, is_key in rows:
        w = hrs / TOTAL_H * 100
        out.append(
            f'<div class="row{" is-key" if is_key else ""}"><div class="lab">{e(lab)}</div>'
            f'<div class="track"><div class="bar {kind}" style="width:{w:.2f}%"></div></div>'
            f'<div class="val">{h10(hrs)} h</div></div>'
        )
    cap = f"Hours per year, all HVAC sections, at ${RATE:.0f} an hour. Dark bars: hours freed that UTI values at the cost of an instructor hour (the tool saves {h10(SAVED_H)} hours at {pct(RED)} and {h10(SAVED_H_HIGH)} at {pct(RED_H)}). Outlined bar: hours needed to cover the licence cost."
    return f'<figure class="bars">{"".join(out)}<figcaption>{e(cap)}</figcaption></figure>'


def build():
    p1 = ("UTI's HVAC program grew from about 29 to about 98 sections per course start in twelve months. The share of instructors teaching two or "
          "three sections went from 14% to 42%, and they grade more than their shift schedule leaves room for.")
    p2 = ("Expected and high value every hour freed in these shifts at what an instructor hour costs, because UTI would otherwise pay for it, in overtime "
          "or extra hires. Low counts only grading outside scheduled hours. All cases are estimates until the pilot measures them.")

    CASES = (LOW, EXP, HIGH)
    n3 = lambda *xs: "".join(f"<td class='n'>{x}</td>" for x in xs)
    glance = (
        "<tr><td>Hours valued</td><td>Grading outside scheduled hours</td><td>All hours freed in these shifts</td><td>All hours freed in these shifts</td></tr>"
        "<tr><td>Time the tool takes off</td>" + n3(*(pct(x) for x in (RED, RED, RED_H))) + "</tr>"
        "<tr><td>Value a year</td>" + n3(*(usd100(c["sav"]) for c in CASES)) + "</tr>"
        "<tr><td>Licence cost a year</td>" + n3(*(usd100(COST) for c in CASES)) + "</tr>"
        "<tr class='total'><td>Net result a year</td>" + n3(*(net_text(c["sav"], COST) for c in CASES)) + "</tr>"
        "<tr><td>Back for every $1 spent</td>" + n3(*(f"${c['ratio']:.2f}" for c in CASES)) + "</tr>"
    )

    today_rows = [
        ("HVAC sections per day", "About 100 (about 29 per course start in Oct 2025, about 98 in Oct 2026)", "UTI Operations 10 Nov; HVAC data export"),
        ("Instructors teaching HVAC", "66 (22 per course start in Oct 2025, 67 in Oct 2026), at 14 campuses", "UTI Operations 10 Nov; HVAC data export"),
        ("Instructors with two or three sections", "42% of instructors and 60% of sections in Oct 2026 (14% and 24% in Oct 2025)", "HVAC data export"),
        ("Students per section, days", f"{STUDENTS:.0f} students per section (one 5-hour class), {D:.0f} days a year (51 weeks, 5 days)", "UTI Operations, 13 Nov"),
        ("Cost per instructor hour", f"${RATE:.0f} (UTI estimate)", "UTI Operations, 10 Nov"),
        ("Grading time per section per day", "30 to 60 minutes (UTI estimate, not tracked)", "UTI Operations, 10 and 13 Nov"),
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

    def mins(x):
        return int(x + 0.5)
    two_low = 2 * G * (1 - RED) * 60
    two_high = 2 * G * (1 - RED_H) * 60
    ba = (
        "<tr><td>Marking and review</td><td>The instructor marks each lab by hand, in the time scheduled after class.</td>"
        "<td>Eduface proposes a score with feedback per criterion against UTI's answer key and rubric. The instructor checks, edits and approves it before the student sees anything.</td></tr>"
        f"<tr><td>Two-section shift</td><td>{need2:.0f} minutes of grading against {WIN * 60:.0f} scheduled, about {OVER2 * 60:.0f} minutes over.</td>"
        f"<td>{mins(two_low)} minutes at {pct(RED)} saved, {mins(two_high)} at {pct(RED_H)}. Both fit inside the {WIN * 60:.0f} scheduled minutes.</td></tr>"
    )

    step4 = "<strong>Low:</strong> only grading outside scheduled hours. <strong>Expected and high:</strong> all hours freed in these shifts."
    calc = (
        f"<tr><td>1</td><td>Grading today</td><td>{S:.0f} sections × {G:g} h × {D:.0f} days</td><td class='n' colspan='3'>{h10(TOTAL_H)} h, all cases</td><td>UTI Operations, 10 Nov (30 to 60 min, midpoint)</td></tr>"
        f"<tr><td>2</td><td>Tool saves</td><td>{pct(RED)} of step 1 (high case: {pct(RED_H)})</td>{n3(h10(SAVED_H) + ' h', h10(SAVED_H) + ' h', h10(SAVED_H_HIGH) + ' h')}<td>Eduface assumption, tested in the pilot</td></tr>"
        f"<tr><td>3</td><td>Multi-section shifts</td><td>{pct(SHARE)} of sections (Oct 2026)</td>{n3(h10(SAVED_MULTI) + ' h', h10(SAVED_MULTI) + ' h', h10(SAVED_MULTI_HIGH) + ' h')}<td>HVAC data export. Single-section shifts are paid 8 hours either way.</td></tr>"
        f"<tr><td>4</td><td>Hours valued</td><td>{step4}</td>{n3(h10(LOW['cash_h']) + ' h', h10(EXP['cash_h']) + ' h', h10(HIGH['cash_h']) + ' h')}<td>UTI shift schedules, 13 Nov</td></tr>"
        f"<tr><td>5</td><td>Value</td><td>Hours × ${RATE:.0f}</td>{n3(usd100(LOW['sav']), usd100(EXP['sav']), usd100(HIGH['sav']))}<td>UTI Operations, 10 Nov</td></tr>"
        f"<tr><td>6</td><td>Licence cost</td><td>{IN_CLASS:,.0f} students × ${PRICE:.2f} × 12 months</td><td class='n' colspan='3'>{usd100(COST)}, all cases</td><td>Eduface price per student per month</td></tr>"
        f"<tr class='total'><td></td><td>Net per year</td><td>Step 5 minus step 6</td>{n3(*(net_text(c['sav'], COST) for c in CASES))}<td></td></tr>"
        f"<tr><td></td><td>Back per $1</td><td>Step 5 divided by step 6</td>{n3(*('$%.2f' % c['ratio'] for c in CASES))}<td></td></tr>"
    )

    def three(g=G, r=RED, rh=RED_H, m=1.0):
        return (lens1(g, r, m), lens2(g, r, m), lens2(g, rh, m))
    base = (LOW["sav"], EXP["sav"], HIGH["sav"])
    sens = [
        ("Base case", base, COST),
        ("Grading 30 minutes per section (base 45)", three(g=0.5), COST),
        ("Grading 60 minutes per section (base 45)", three(g=1.0), COST),
        (f"Tool removes 30% (base {pct(RED)}, high {pct(RED_H)})", three(r=0.3, rh=0.3), COST),
        ("Only half of step 4 hours realised", (None, EXP["sav"] / 2, HIGH["sav"] / 2), COST),
        (f"Time and a half (${RATE * 1.5:.0f} an hour)", three(m=1.5), COST),
    ]
    def cell(v, cost):
        return "<td class='n'>n/a</td><td class='n'>n/a</td>" if v is None else f"<td class='n'>{usd100(v)}</td><td class='n'>{net_text(v, cost)}</td>"
    sens_rows = "".join(
        f"<tr{' class=total' if i == 0 else ''}><td>{e(lab)}</td>" + "".join(cell(v, cost) for v in vals) + "</tr>"
        for i, (lab, vals, cost) in enumerate(sens)
    )

    fte = SAVED_SINGLE / 2080
    leavers = 66 * 0.20

    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Eduface in HVAC: business case for Universal Technical Institute</title>
<link rel="stylesheet" href="file://{HERE}/style.css"></head><body>
<img class="brand" src="file://{LOGO}" alt="Eduface">
<h1>Eduface in HVAC: business case for Universal Technical Institute</h1>
<p class="case">Low case, expected case and high case</p>
<p class="status">Draft for validation by UTI, 24 Nov 2026. Based on figures from UTI Operations. Hours are rounded to 10, dollars to $100. Contact: Dante Torbed, dante.torbed@eduface.me.</p>

<p class="lead">{e(p1)}</p>
{chart()}

<table class="keep"><caption>The three cases at a glance</caption>{cg((28, 24, 24, 24))}
<thead><tr><th></th><th class="n">Low case</th><th class="n">Expected case</th><th class="n">High case</th></tr></thead><tbody>{glance}</tbody></table>

<h2>Customer context</h2>
<table class="keep"><caption>HVAC at UTI today</caption>{cg((29, 45, 26))}
<thead><tr><th>Measure</th><th>Value</th><th>Source</th></tr></thead><tbody>{today}</tbody></table>

<table class="keep"><caption>Scheduled time against grading needed, at {need1:.0f} minutes per section</caption>{cg((17, 14, 33, 16, 20))}
<thead><tr><th>Shift</th><th class="n">Share of sections</th><th>Scheduled for grading, prep and training aids</th><th class="n">Grading needed</th><th>Gap per day</th></tr></thead><tbody>{gap}</tbody></table>
<p class="src">UTI example shift schedules and HVAC data export, 13 Nov 2026; UTI Operations, 10 Nov 2026. Over a year the gap adds up to about {h10(CEIL_H)} hours, or {usd100(CEIL_H * RATE)} at ${RATE:.0f} an hour if it is paid time. UTI Operations has not yet confirmed how these hours are paid.</p>

<table class="keep"><caption>Current and future state: how a lab submission is handled</caption>{cg((18, 41, 41))}
<thead><tr><th>Step</th><th>Today</th><th>With Eduface</th></tr></thead><tbody>{ba}</tbody></table>

<h2>Cost justification</h2>
<p>{e(p2)}</p>
<table class="keep"><caption>How the value is calculated</caption>{cg((5, 14, 27, 11, 11, 11, 21))}
<thead><tr><th>Step</th><th>What</th><th>Calculation</th><th class="n">Low</th><th class="n">Expected</th><th class="n">High</th><th>Basis</th></tr></thead><tbody>{calc}</tbody></table>

<h3>Not counted in the numbers</h3>
<ul>
<li><strong>Single-section shifts.</strong> About {h10(SAVED_SINGLE)} hours a year ({fte:.1f} full-time equivalents) go to preparation and tutoring. They are paid 8 hours either way, so not counted.</li>
<li><strong>Turnover.</strong> 37% of HVAC instructors left last year (25 of 66); UTI Operations suggests 20% for planning, about {leavers:.0f} leavers at $10,000 to $15,000 each. No evidence yet that grading load is the cause, so none is counted.</li>
</ul>

<table class="keep"><caption>What moves the result</caption>{cg((29, 11.8, 11.8, 11.8, 11.8, 11.8, 12))}
<thead><tr><th>If this changes</th><th class="n">Low: value</th><th class="n">Low: net</th><th class="n">Expected: value</th><th class="n">Expected: net</th><th class="n">High: value</th><th class="n">High: net</th></tr></thead><tbody>{sens_rows}</tbody></table>
<p class="src">Value and net are per year, net after the licence cost. The half-realised row does not apply to the low case.</p>

<h2>Validation</h2>
<table class="keep"><caption>What the pilot measures</caption>{cg((30, 44, 26))}
<thead><tr><th>Measure</th><th>How</th><th>Tests</th></tr></thead><tbody>
<tr><td>Grading time per section</td><td>A control group logs grading time for 1 to 2 weeks before and during the pilot.</td><td>The 45 minutes and the {pct(RED)} (high: {pct(RED_H)})</td></tr>
<tr><td>Grading outside scheduled hours</td><td>The same group, by one, two and three sections.</td><td>The gap of about {OVER2 * 60:.0f} minutes</td></tr>
<tr><td>Pay rules, two and three sections</td><td>UTI Operations confirms how the hours are paid.</td><td>Paid time or not, and the rate</td></tr>
</tbody></table>
<p>The licence pays for itself if the pilot shows about {NEED_MIN:.0f} minutes a day less paid or overtime grading per instructor with two or three sections, about {h10(NEED_H)} hours a year at ${RATE:.0f}. The low case assumes {LOW['min']:.0f} minutes, the expected case {EXP['min']:.0f} and the high case {HIGH['min']:.0f}, which also needs the tool to remove {pct(RED_H)} of the grading time.</p>
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
