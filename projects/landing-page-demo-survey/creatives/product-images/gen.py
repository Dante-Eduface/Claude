#!/usr/bin/env python3
"""Genereert zes Paper Grader-productbeelden, een per vakgebied.

Een sjabloon, zes inhouden. Het cijfer wordt uit de weging berekend, nooit met de
hand ingevuld. Tokens uit references/design-system/core/tokens.css.
Bron voor elke productclaim: references/eduface-product.md.
"""
import pathlib, html

HERE = pathlib.Path(__file__).parent

SUBJECTS = ["Law", "Economics", "Social Sciences", "STEM", "Humanities", "Health Sciences"]
ICONS = {"Law": "⚖️", "Economics": "\U0001F4C8", "Social Sciences": "\U0001F52C",
         "STEM": "⚙️", "Humanities": "\U0001F4D6", "Health Sciences": "\U0001FA7A"}

DATA = {
 "Law": dict(
   slug="law", n=86, tot=88, course="Law · Employment law case study",
   excerpt1=("The employer ended the contract without notice after a single incident. ",
             "That makes the dismissal unfair, because summary dismissal always requires gross misconduct."),
   comment_crit="Application of law",
   comment=("You state the rule and go straight to the conclusion. Work through the facts first: what did the "
            "employee actually do, and does that meet the threshold? Put the authority next to it."),
   excerpt2=("The employee had two written warnings in the previous year, ",
             "which the tribunal weighs when it looks at proportionality."),
   approved="Issue identification",
   fb_crit="Application of law",
   fb=("The rules are stated correctly but they are not applied to these facts. Take each element of the test in "
       "turn and say whether the facts meet it."),
   criteria=[("Issue identification", 25, 9), ("Application of law", 35, 7), ("Legal writing and structure", 40, 8)]),

 "Economics": dict(
   slug="economics", n=140, tot=142, course="Economics · Investment appraisal",
   excerpt1=("In September the company spent €12,000 on a feasibility study, carried out solely for this investment. ",
             "The amount therefore belongs to the project and is included in the investment total."),
   comment_crit="Determining the investment amount",
   comment=("The feasibility study was already paid for, so it is a sunk cost. Leaving it in the investment total "
            "distorts the decision. Take the €12,000 out."),
   excerpt2=("The bank loan of €180,000 is interest-only, ",
             "so the interest charge stays the same over the full term."),
   approved="Operating result and cash flow",
   fb_crit="Determining the investment amount",
   fb=("Two costs sit in the total that do not belong there: the VAT and the feasibility study. State the VAT "
       "separately and explain per item why it counts towards the investment."),
   criteria=[("Determining the investment amount", 20, 7), ("Operating result and cash flow", 40, 8),
             ("Advice and risk analysis", 40, 9)]),

 "Social Sciences": dict(
   slug="social-sciences", n=34, tot=36, course="Social Sciences · Research report, youth work",
   excerpt1=("Young people who took part in the programme reported fewer conflicts at home. ",
             "The programme therefore reduces conflict within the family."),
   comment_crit="Interpretation of results",
   comment=("You move from a difference between two groups to a cause. Nothing here rules out that the families who "
            "signed up were already more motivated. Say what the data supports, then name the limitation."),
   excerpt2=("Twenty-eight of the forty participants completed both questionnaires, ",
             "so the results describe this group and not the wider population."),
   approved="Research design",
   fb_crit="Interpretation of results",
   fb=("The findings are described accurately, but the conclusion goes further than the design allows. Rewrite it in "
       "terms of association and say what a follow-up study would need to test cause."),
   criteria=[("Research design", 30, 8), ("Interpretation of results", 30, 6), ("Reporting and sources", 40, 7)]),

 "STEM": dict(
   slug="stem", n=61, tot=64, course="STEM · Heat exchanger design report",
   excerpt1=("The required heat transfer area follows from Q = U · A · ΔT. ",
             "With U at 850 W/m²K the area comes out at 12.4 m²."),
   comment_crit="Calculation and assumptions",
   comment=("The number is right for the U you picked, but you never say where that value comes from or how much "
            "fouling you allowed for. Give the source and the margin, otherwise the area cannot be checked."),
   excerpt2=("A safety margin of 15 per cent was applied, ",
             "which brings the design to 14.3 m²."),
   approved="Reporting and units",
   fb_crit="Calculation and assumptions",
   fb=("Every step is traceable except the inputs you chose yourself. Add a short table with each assumed value, its "
       "source and its effect on the result."),
   criteria=[("Calculation and assumptions", 40, 8), ("Design choices", 30, 7), ("Reporting and units", 30, 9)]),

 "Humanities": dict(
   slug="humanities", n=112, tot=115, course="Humanities · Source analysis essay",
   excerpt1=("The pamphlet describes the strike as a threat to public order. ",
             "This shows how the population saw the strikers at the time."),
   comment_crit="Use of sources",
   comment=("A pamphlet tells you what its author wanted readers to think, not what the population thought. Say who "
            "published it and why, then use it as evidence of that position."),
   excerpt2=("Newspaper reports from the same week give a different picture, ",
             "which suggests the pamphlet stood in a wider debate."),
   approved="Structure and language",
   fb_crit="Use of sources",
   fb=("You handle the material carefully but treat one source as representative. Place each source with its author "
       "and its audience before you draw a conclusion from it."),
   criteria=[("Argument", 30, 8), ("Use of sources", 30, 7), ("Structure and language", 40, 8)]),

 "Health Sciences": dict(
   slug="health-sciences", n=47, tot=49, course="Health Sciences · Care plan, evidence-based practice",
   excerpt1=("The patient is at risk of pressure ulcers because of limited mobility. ",
             "I therefore chose to reposition every two hours."),
   comment_crit="Substantiation of the intervention",
   comment=("Two hours is the guideline default, not a choice for this patient. Link it to the risk score you "
            "recorded and say why that interval fits this case."),
   excerpt2=("The Braden score of 14 points to a moderate risk, ",
             "which is why nutrition is part of the plan as well."),
   approved="Assessment",
   fb_crit="Substantiation of the intervention",
   fb=("The plan is complete and the actions are appropriate. What is missing is the step from this patient's data "
       "to each action. Make that link explicit for every intervention."),
   criteria=[("Assessment", 30, 9), ("Substantiation of the intervention", 30, 8), ("Plan and evaluation", 40, 9)]),
}

CHECK = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
         'stroke-linejoin="round"><path d="m3 8.5 3 3 7-7"/></svg>')

CSS = """
  :root{
    --navy:#002333; --green:#00e075; --green-deep:#007b54;
    --ink-500:#5b7480; --ink-300:#a9bcc4; --ink-200:#cdd9de; --ink-100:#e7eef0; --ink-50:#f3f7f8; --white:#fff;
    --r-md:8px; --r-xl:12px; --r-2xl:20px; --r-full:9999px;
    --sh-md:0 4px 16px rgba(0,35,51,.08); --sh-lg:0 12px 40px rgba(0,35,51,.10);
    --control-h:32px; --pad:16px;
  }
  *{box-sizing:border-box;margin:0}
  html,body{background:transparent;font-family:Inter,ui-sans-serif,system-ui,sans-serif;color:var(--navy);-webkit-font-smoothing:antialiased}
  body{width:1520px;height:628px;overflow:hidden;display:grid;place-items:center}

  .t-block{font-size:17px;font-weight:600;line-height:1.3}
  .t-hero{font-size:24px;font-weight:600;line-height:1.2;font-variant-numeric:tabular-nums}
  .t{font-size:14px;font-weight:400;line-height:1.55}
  .muted{color:var(--ink-500)}


  .frame{width:1440px;height:548px;background:var(--white);border-radius:var(--r-2xl);box-shadow:var(--sh-lg);
         border:1px solid var(--ink-100);display:flex;flex-direction:column;overflow:hidden}
  .top{height:48px;border-bottom:1px solid var(--ink-100);display:flex;align-items:center;padding:0 24px;flex-shrink:0}
  .crumb{display:flex;align-items:center;gap:8px}
  .crumb .sep{color:var(--ink-300)}

  .body{flex:1;display:grid;grid-template-columns:minmax(0,52fr) minmax(0,48fr);min-height:0}
  .col{padding:24px 28px;display:flex;flex-direction:column;gap:14px;min-height:0}
  .col.left{border-right:1px solid var(--ink-100)}
  .col.right{padding:0;display:grid;grid-template-rows:minmax(0,1fr) minmax(0,1fr)}
  .col.right > div{padding:24px 28px;display:flex;flex-direction:column;gap:14px}
  .col.right > div + div{border-top:1px solid var(--ink-100)}

  .excerpt{color:var(--ink-700,#2c4a57);max-width:62ch}
  .mark{background:rgba(0,224,117,.22);box-shadow:inset 0 -2px 0 var(--green-deep);border-radius:2px;padding:1px 0}

  .card{border:1px solid var(--ink-200);border-radius:var(--r-xl);background:var(--white);box-shadow:var(--sh-md);
        padding:var(--pad);display:flex;flex-direction:column;gap:12px}
  .crit{color:var(--ink-500)}
  .done{display:inline-flex;align-items:center;gap:7px;color:var(--green-deep);font-weight:500}
  .done svg{width:15px;height:15px;flex-shrink:0}

  .acts{display:flex;align-items:center;gap:8px;margin-top:auto}
  .btn{height:var(--control-h);padding:0 14px;border-radius:var(--r-md);font-size:14px;font-weight:500;
       display:inline-flex;align-items:center;gap:6px;border:1px solid transparent;white-space:nowrap}
  .btn.pri{background:var(--navy);color:var(--white)}
  .btn.sec{background:var(--white);border-color:var(--ink-200);color:var(--navy)}
  .btn.ghost{color:var(--ink-500);padding:0 8px}
  .btn svg{width:14px;height:14px}

  .rows{display:flex;flex-direction:column}
  .row{height:42px;display:grid;grid-template-columns:minmax(0,1fr) 48px 64px;align-items:center;gap:12px;
       border-top:1px solid var(--ink-100)}
  .row:last-child{border-bottom:1px solid var(--ink-100)}
  .row .w{color:var(--ink-500);text-align:right;font-variant-numeric:tabular-nums}
  .row .s{text-align:right;font-variant-numeric:tabular-nums}
  .grade{display:flex;align-items:baseline;gap:8px}

  /* Nummers bij de drie titels, alleen in de how-it-works-variant */
  .no{width:26px;height:26px;border-radius:50%;background:var(--navy);color:var(--white);font-size:13px;
      font-weight:600;display:none;place-items:center;flex-shrink:0}
  body.callouts .no{display:grid}
  .head{display:flex;align-items:center;gap:10px}
"""

TPL = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Paper Grader · {subject}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=League+Spartan:wght@600;700&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body class="plain">

<div class="frame">
  <div class="top">
    <div class="crumb t"><span class="muted">{course}</span><span class="sep">/</span><span>Submission {n} of {tot}</span></div>
  </div>

  <div class="body">
    <div class="col left">
      <span class="head"><span class="no">1</span><span class="t-block">Comments in the text</span></span>
      <p class="t excerpt">{e1a}<span class="mark">{e1b}</span></p>
      <div class="card">
        <span class="t crit">{comment_crit}</span>
        <p class="t">{comment}</p>
        <div class="acts">
          <span class="btn pri">{check}Approve</span>
          <span class="btn sec">Edit</span>
          <span class="btn ghost">Discard</span>
        </div>
      </div>
      <p class="t excerpt" style="margin-top:2px">{e2a}<span class="mark">{e2b}</span></p>
      <div class="done t">{check}Approved by you · {approved}</div>
    </div>

    <div class="col right">
      <div>
        <span class="head"><span class="no">2</span><span class="t-block">Feedback per criterion</span></span>
        <span class="t crit">{fb_crit}</span>
        <p class="t">{fb}</p>
        <div class="acts">
          <span class="btn pri">{check}Approve</span>
          <span class="btn sec">Edit</span>
        </div>
      </div>

      <div>
        <span class="head"><span class="no">3</span><span class="t-block">Grade per criterion</span></span>
        <div class="rows">{rows}</div>
        <div class="acts" style="justify-content:space-between">
          <span class="grade"><span class="t-hero">{grade}</span><span class="t muted">/ 10 proposed</span></span>
          <span class="btn pri">{check}Approve grade</span>
        </div>
      </div>
    </div>
  </div>
</div>
</body></html>
"""

def build(subject):
    d = DATA[subject]
    assert sum(w for _, w, _ in d["criteria"]) == 100, f"{subject}: weging telt niet op tot 100"
    grade = sum(w * s for _, w, s in d["criteria"]) / 100
    rows = "".join(
        f'<div class="row t"><span>{html.escape(n)}</span><span class="w">{w}%</span>'
        f'<span class="s">{s} / 10</span></div>' for n, w, s in d["criteria"])
    out = TPL.format(css=CSS, subject=subject, course=d["course"], rows=rows,
                     n=d["n"], tot=d["tot"], check=CHECK, grade=f"{grade:.1f}",
                     e1a=d["excerpt1"][0], e1b=d["excerpt1"][1],
                     e2a=d["excerpt2"][0], e2b=d["excerpt2"][1],
                     comment_crit=d["comment_crit"], comment=d["comment"],
                     approved=d["approved"], fb_crit=d["fb_crit"], fb=d["fb"])
    path = HERE / f'paper-grader-{d["slug"]}.html'
    path.write_text(out, encoding="utf-8")
    return path.name, f"{grade:.1f}"

if __name__ == "__main__":
    for s in SUBJECTS:
        print("%-28s %s" % build(s))
