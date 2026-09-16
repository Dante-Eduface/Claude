#!/usr/bin/env python3
"""Rendert het weekmenu naar weekmenu.html.

    python3 build.py                 # nieuwste menu in menu/
    python3 build.py 2026-W36        # specifieke week
"""
import json, pathlib, sys, html

ROOT = pathlib.Path(__file__).parent
MENU = ROOT / "menu"


def latest():
    files = sorted(MENU.glob("*.json"))
    if not files:
        sys.exit("Geen menu gevonden in menu/")
    return files[-1]


def esc(x):
    return html.escape(str(x))


def render(d):
    rows = ""
    for day in d["days"]:
        pre = f'<div class="pre">17:00, voor de gym &middot; {esc(day["pre"])}</div>' if day.get("pre") else ""
        rest = "rest" if day["training"].lower().startswith("rust") else ""
        rows += f"""
      <tr>
        <th scope="row">
          <div class="dag">{esc(day['dag'])}</div>
          <div class="tr {rest}">{esc(day['training'])}</div>
        </th>
        <td>{esc(day['ontbijt'])}</td>
        <td>{esc(day['lunch'])}</td>
        <td>{pre}<div>{esc(day["diner"])}</div></td>
        <td class="snack">{esc(day['snack'])}</td>
      </tr>"""

    changes = "".join(f"<li>{esc(c)}</li>" for c in d["changes"])
    prep = "".join(
        f'<div class="fase"><h3>{esc(f["fase"])}</h3><ol>'
        + "".join(f"<li>{esc(s)}</li>" for s in f["stappen"])
        + "</ol></div>"
        for f in d["prep"]
    )
    shop = "".join(
        f'<div class="groep"><h3>{esc(g["groep"])}</h3><p>{esc(g["items"])}</p></div>'
        for g in d["boodschappen"]
    )
    t = d["targets"]

    return TEMPLATE.format(
        week=d["week"], range=esc(d["range"]), prep_date=esc(d["prep_date"]),
        kcal=t["kcal"], eiwit=esc(t["eiwit"]), stop=esc(t["stop_eating"]),
        changes=changes, rows=rows, prep=prep, shop=shop,
        rot_eiwit=esc(d["rotatie"]["eiwit"]), rot_saus=esc(d["rotatie"]["saus"]),
        rot_let=esc(d["rotatie"]["let_op"]),
    )


TEMPLATE = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Weekmenu week {week}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=League+Spartan:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{{
  --navy:#002333; --ink-700:#2c4a57; --ink-500:#5b7480; --ink-300:#a9bcc4;
  --ink-200:#cdd9de; --ink-100:#e7eef0; --ink-50:#f3f7f8;
  --green-deep:#007b54;
  --font-sans:"Inter",ui-sans-serif,system-ui,sans-serif;
  --font-display:"League Spartan",var(--font-sans);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:var(--font-sans);font-size:15px;line-height:1.6;color:var(--navy);
     background:var(--ink-50);-webkit-font-smoothing:antialiased;padding:40px 24px 80px}}
.wrap{{max-width:1080px;margin:0 auto}}
h1,h2,h3{{font-family:var(--font-display);letter-spacing:-.01em;font-weight:600}}
h1{{font-size:30px;line-height:1.15}}
h2{{font-size:19px;margin-bottom:16px}}
h3{{font-size:14px;margin-bottom:8px}}

.head{{margin-bottom:24px}}
.head .range{{color:var(--ink-500);font-size:15px;margin-top:2px}}
.targets{{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}}
.chip{{background:#fff;border:1px solid var(--ink-100);border-radius:999px;
       padding:6px 14px;font-size:13px}}
.chip b{{font-weight:600}}

section{{margin-bottom:40px}}

.changes{{background:#fff;border:1px solid var(--ink-100);border-radius:12px;padding:20px 24px}}
.changes ul{{margin:0;padding-left:20px}}
.changes li{{font-size:14px;margin-bottom:6px;color:var(--ink-700)}}
.changes li:last-child{{margin-bottom:0}}

.tablewrap{{overflow-x:auto;background:#fff;border:1px solid var(--ink-100);border-radius:12px}}
table{{width:100%;border-collapse:collapse;min-width:840px}}
thead th{{text-align:left;font-size:10px;text-transform:uppercase;letter-spacing:.08em;
         font-weight:600;color:var(--ink-500);padding:12px 18px;
         border-bottom:1px solid var(--ink-100);background:var(--ink-50);white-space:nowrap}}
tbody th{{text-align:left;padding:16px 18px;border-bottom:1px solid var(--ink-100);
         vertical-align:top;width:150px;font-weight:400}}
tbody td{{padding:16px 18px;border-bottom:1px solid var(--ink-100);
         vertical-align:top;font-size:14px;line-height:1.5}}
tbody tr:last-child th,tbody tr:last-child td{{border-bottom:none}}
.dag{{font-family:var(--font-display);font-weight:600;font-size:15px}}
.tr{{font-size:12px;color:var(--green-deep);font-weight:500;margin-top:2px}}
.tr.rest{{color:var(--ink-300);font-weight:400}}
.pre{{margin-bottom:10px;padding-bottom:10px;border-bottom:1px dashed var(--ink-200);
      font-size:13px;color:var(--ink-700)}}
.snack{{color:var(--ink-700)}}

.cols{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}}
.fase,.groep{{background:#fff;border:1px solid var(--ink-100);border-radius:12px;padding:20px 24px}}
.fase ol{{margin:0;padding-left:18px}}
.fase li{{font-size:14px;color:var(--ink-700);margin-bottom:6px;line-height:1.5}}
.fase li:last-child{{margin-bottom:0}}
.groep p{{font-size:14px;color:var(--ink-700);line-height:1.7}}

.rot{{background:#fff;border:1px solid var(--ink-100);border-radius:12px;padding:20px 24px;font-size:14px}}
.rot dt{{font-size:11px;text-transform:uppercase;letter-spacing:.08em;font-weight:600;
        color:var(--ink-500);margin-bottom:2px}}
.rot dd{{margin:0 0 12px;color:var(--ink-700)}}
.rot .let{{border-top:1px solid var(--ink-100);padding-top:12px;margin-top:4px;color:var(--navy)}}

@media (max-width:640px){{
  body{{padding:24px 12px 56px}}
  h1{{font-size:24px}}
}}
@media print{{
  body{{background:#fff;padding:0}}
  .tablewrap,.fase,.groep,.rot,.changes{{border-color:#ccc}}
  table{{min-width:0}}
}}
</style>
</head>
<body>
<div class="wrap">

  <div class="head">
    <h1>Weekmenu week {week}</h1>
    <div class="range">{range} &middot; prep op {prep_date}</div>
    <div class="targets">
      <span class="chip"><b>{kcal}</b> kcal</span>
      <span class="chip">eiwit <b>{eiwit}</b></span>
      <span class="chip">klaar met eten <b>{stop}</b></span>
    </div>
  </div>

  <section>
    <h2>Wat er deze week anders is</h2>
    <div class="changes"><ul>{changes}</ul></div>
  </section>

  <section>
    <h2>De week</h2>
    <div class="tablewrap">
      <table>
        <thead>
          <tr><th>Dag</th><th>Ontbijt</th><th>Lunch (mee)</th><th>Diner</th><th>Snack</th></tr>
        </thead>
        <tbody>{rows}
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Zondag prep</h2>
    <div class="cols">{prep}</div>
  </section>

  <section>
    <h2>Boodschappen</h2>
    <div class="cols">{shop}</div>
  </section>

  <section>
    <h2>Rotatiecheck</h2>
    <div class="rot">
      <dl>
        <dt>Eiwitbronnen</dt><dd>{rot_eiwit}</dd>
        <dt>Sausbasis</dt><dd>{rot_saus}</dd>
      </dl>
      <div class="let">{rot_let}</div>
    </div>
  </section>

</div>
</body>
</html>
"""

if __name__ == "__main__":
    src = MENU / f"{sys.argv[1]}.json" if len(sys.argv) > 1 else latest()
    data = json.loads(src.read_text())
    out = ROOT / "weekmenu.html"
    out.write_text(render(data))
    print(f"{out.name} gebouwd uit {src.name} (week {data['week']}, {data['range']}).")
