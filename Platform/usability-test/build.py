#!/usr/bin/env python3
"""Bouwt data.json naar artifact.html (Eduface huisstijl, klaar om te publiceren als Artifact)."""
import base64, json, html, os

ROOT = os.path.dirname(os.path.abspath(__file__))

TABS = {
    "grading":  "Grading tab",
    "feedback": "Feedback tab",
    "signup":   "Signup flow",
    "rubric":   "Manage rubric",
    "algemeen": "Algemeen",
}


def esc(s):
    return html.escape(str(s or ""))


def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def shots(items):
    """Echte afbeelding als het bestand er staat, anders een placeholder met de bestandsnaam."""
    if not items:
        return ""
    out = ['<div class="shots">']
    for s in items:
        pad = s if isinstance(s, str) else s.get("pad", "")
        cap = "" if isinstance(s, str) else s.get("bijschrift", "")
        full = os.path.join(ROOT, pad)
        if pad and os.path.exists(full):
            ext = os.path.splitext(full)[1].lower().lstrip(".")
            mime = "jpeg" if ext in ("jpg", "jpeg") else ext
            out.append(f'<figure class="shot"><img src="data:image/{mime};base64,{b64(full)}" '
                       f'alt="{esc(cap)}" loading="lazy">'
                       f'<figcaption>{esc(cap)}</figcaption></figure>')
        else:
            out.append('<figure class="shot ph"><div class="phbox"><span>Afbeelding volgt</span>'
                       f'<code>{esc(os.path.basename(pad))}</code></div>'
                       f'<figcaption>{esc(cap)}</figcaption></figure>')
    out.append("</div>")
    return "".join(out)


def finding(f):
    tab = f.get("tab", "algemeen")
    bron = f'<p class="bron">Bron: {esc(f["bron"])}</p>' if f.get("bron") else ""
    return (f'<article class="find t-{tab}" data-tab="{tab}">'
            f'<span class="tag t-{tab}">{esc(TABS.get(tab, tab))}</span>'
            f'<p>{esc(f.get("tekst",""))}</p>{bron}{shots(f.get("afbeeldingen"))}</article>')


def build():
    d = json.load(open(os.path.join(ROOT, "data.json"), encoding="utf-8"))

    tel = {k: 0 for k in TABS}
    for cat in d["categorieen"]:
        for c in cat["criteria"]:
            for f in c.get("feedback", []):
                tel[f.get("tab", "algemeen")] = tel.get(f.get("tab", "algemeen"), 0) + 1
    for b in d.get("bugs", []):
        tel[b.get("tab", "algemeen")] = tel.get(b.get("tab", "algemeen"), 0) + 1
    totaal = sum(tel.values())

    P = []
    A = P.append
    A(f'<title>{esc(d["titel"])}</title>')
    A('<link rel="preconnect" href="https://fonts.googleapis.com">'
      '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=League+Spartan:wght@600;700&family=Inter:wght@400;500;600&display=swap">')
    A("<style>" + CSS + "</style>")

    A('<div class="wrap" id="wrap">')

    # header
    A('<header class="head"><p class="eyebrow">Eduface platform</p>'
      f'<h1>{esc(d["titel"])}</h1><p class="lede">{esc(d["ondertitel"])}</p>')
    A('<dl class="meta">' + "".join(
        f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in d["meta"].items()) + "</dl>")
    A("</header>")

    # filterbalk
    A('<nav class="filters" aria-label="Filter op onderdeel">'
      f'<span class="fl">Filter <b>{totaal}</b> bevindingen</span>')
    for k, naam in TABS.items():
        if tel.get(k):
            A(f'<button class="chip t-{k}" data-f="{k}" aria-pressed="true">'
              f'<i></i>{esc(naam)}<b>{tel[k]}</b></button>')
    A('<button class="chip reset" data-f="all">Alles tonen</button></nav>')

    # categorieen
    for cat in d["categorieen"]:
        n = sum(len(c.get("feedback", [])) for c in cat["criteria"])
        A(f'<section class="cat"><div class="cathead"><div class="row">'
          f'<span class="cid">{esc(cat["id"])}</span><h2>{esc(cat["titel"])}</h2>'
          f'<span class="count">{n or "geen"} {"bevinding" if n == 1 else "bevindingen"}</span>'
          f'</div><p>{esc(cat.get("intro",""))}</p></div>')
        for c in cat["criteria"]:
            A('<div class="crit">')
            A('<div class="ctop"><span class="chipid">' + esc(c["id"]) + "</span>"
              f'<h3>{esc(c["titel"])}</h3>')
            if c.get("anchors"):
                sc = c.get("score")
                A('<span class="score" title="Score 1 tot 5">'
                  + "".join(f'<i class="{f"on s{n}" if sc == n else ""}">{n}</i>' for n in range(1, 6))
                  + "</span>")
            A("</div>")
            if c.get("anchors"):
                a = c["anchors"]
                A('<div class="anchors">' + "".join(
                    f'<div><b>{n}</b>{esc(a[n])}</div>' for n in ("1", "3", "5")) + "</div>")
            fb = c.get("feedback") or []
            if fb:
                A('<div class="finds">' + "".join(finding(f) for f in fb) + "</div>")
            else:
                A('<p class="leeg">Nog geen bevindingen.</p>')
            A("</div>")
        A("</section>")

    # bugs
    bugs = d.get("bugs", [])
    if bugs:
        A('<section class="cat bugs"><div class="cathead"><div class="row">'
          '<span class="cid">!</span><h2>Bugs</h2>'
          f'<span class="count">{len(bugs)} gevonden</span></div>'
          '<p>Defecten uit deze testronde, los van de scores.</p></div>')
        for i, b in enumerate(bugs, 1):
            tab = b.get("tab", "algemeen")
            A(f'<div class="crit bug" data-tab="{tab}"><div class="ctop">'
              f'<span class="chipid bugid">{i:02d}</span><h3>{esc(b["titel"])}</h3>'
              f'<span class="tag t-{tab}">{esc(TABS.get(tab, tab))}</span></div>'
              f'<p class="waar">{esc(b.get("waar",""))}</p>'
              f'<p>{esc(b.get("tekst",""))}</p>{shots(b.get("afbeeldingen"))}</div>')
        A("</section>")

    A('<footer class="foot"><span>Eduface, usability test</span>'
      f'<span>{esc(d["meta"].get("Datum",""))}</span></footer>')
    A("</div>")
    A("<script>" + JS + "</script>")

    out = os.path.join(ROOT, "artifact.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(P))
    print("HTML:", out, f"({os.path.getsize(out)/1024:.0f} kB)")


CSS = """
:root{
  --ground:#eef4f6; --surface:#ffffff; --surface-2:#f6fafb;
  --ink:#002333; --ink-soft:#4f6b76; --ink-faint:#7d949d;
  --line:#dbe6ea; --line-soft:#e9f0f2;
  --accent:#00a352;
  --t-grading:#1462b8; --t-feedback:#6e36d0; --t-signup:#a86a05;
  --t-rubric:#0b7c7c; --t-algemeen:#5c7480; --t-bug:#c13b31;
  --shadow:0 1px 2px rgba(0,35,51,.05), 0 8px 24px -18px rgba(0,35,51,.35);
}
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
  --ground:#03161e; --surface:#072430; --surface-2:#0a2c39;
  --ink:#e6f1f4; --ink-soft:#9db6bf; --ink-faint:#7b95a0;
  --line:#123a49; --line-soft:#0e3241;
  --accent:#00e075;
  --t-grading:#63aef2; --t-feedback:#b48cf7; --t-signup:#e8ab41;
  --t-rubric:#40c6c1; --t-algemeen:#9db6bf; --t-bug:#f0837a;
  --shadow:0 1px 2px rgba(0,0,0,.3), 0 10px 28px -20px rgba(0,0,0,.9);
}}
:root[data-theme="dark"]{
  --ground:#03161e; --surface:#072430; --surface-2:#0a2c39;
  --ink:#e6f1f4; --ink-soft:#9db6bf; --ink-faint:#7b95a0;
  --line:#123a49; --line-soft:#0e3241;
  --accent:#00e075;
  --t-grading:#63aef2; --t-feedback:#b48cf7; --t-signup:#e8ab41;
  --t-rubric:#40c6c1; --t-algemeen:#9db6bf; --t-bug:#f0837a;
  --shadow:0 1px 2px rgba(0,0,0,.3), 0 10px 28px -20px rgba(0,0,0,.9);
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
h1,h2,h3,.cid,.chipid,.eyebrow{font-family:"League Spartan",Inter,sans-serif;font-weight:700;
  letter-spacing:-.015em;text-wrap:balance}
.wrap{max-width:64rem;margin:0 auto;padding:clamp(24px,5vw,56px) clamp(16px,4vw,32px) 64px;
  display:flex;flex-direction:column;gap:28px}

/* header */
.head{border-bottom:2px solid var(--ink);padding-bottom:22px;display:flex;flex-direction:column;gap:10px}
.eyebrow{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:0}
.head h1{margin:0;font-size:clamp(30px,5.6vw,46px);line-height:1.03}
.lede{margin:0;color:var(--ink-soft);max-width:44ch;font-size:17px}
.meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2px 26px;margin:12px 0 0}
.meta div{display:flex;flex-direction:column;padding:7px 0;border-top:1px solid var(--line)}
.meta dt{font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-faint)}
.meta dd{margin:0;font-size:14px;font-weight:500}

/* filters */
.filters{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:8px;align-items:center;
  background:var(--ground);padding:10px 0;border-bottom:1px solid var(--line)}
.fl{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-faint);margin-right:4px}
.fl b{color:var(--ink);font-weight:600}
.chip{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line);
  background:var(--surface);color:var(--ink);border-radius:999px;padding:6px 12px;
  font:inherit;font-size:13px;cursor:pointer;transition:opacity .15s,border-color .15s}
.chip i{width:9px;height:9px;border-radius:50%;background:var(--c,var(--ink-faint))}
.chip b{font-weight:600;font-variant-numeric:tabular-nums;color:var(--ink-faint);font-size:12px}
.chip[aria-pressed="false"]{opacity:.4}
.chip:hover{border-color:var(--c,var(--ink-soft))}
.chip:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.chip.reset{color:var(--ink-soft)}
.t-grading{--c:var(--t-grading)} .t-feedback{--c:var(--t-feedback)}
.t-signup{--c:var(--t-signup)} .t-rubric{--c:var(--t-rubric)} .t-algemeen{--c:var(--t-algemeen)}

/* categorie */
.cat{display:flex;flex-direction:column;gap:12px}
.cathead{display:flex;flex-direction:column;gap:4px}
.cathead .row{display:flex;align-items:baseline;gap:12px}
.cid{font-size:24px;color:var(--accent);line-height:1}
.cathead h2{margin:0;font-size:22px;flex:1}
.cathead p{margin:0;color:var(--ink-soft);font-size:14px;max-width:62ch}
.count{font-size:12px;color:var(--ink-faint);white-space:nowrap;
  font-variant-numeric:tabular-nums}

/* criterium */
.crit{background:var(--surface);border:1px solid var(--line);border-radius:12px;
  padding:16px 18px;display:flex;flex-direction:column;gap:12px;box-shadow:var(--shadow)}
.ctop{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.chipid{background:var(--ink);color:var(--ground);font-size:12px;padding:3px 8px;border-radius:6px;
  letter-spacing:.02em}
.ctop h3{margin:0;font-size:17px;flex:1;min-width:12ch}
.score{display:flex;gap:5px}
.score i{width:22px;height:22px;border:1px solid var(--line);border-radius:50%;font-style:normal;
  font-size:11px;display:grid;place-items:center;color:var(--ink-faint);
  font-variant-numeric:tabular-nums}
.score i.on{color:#fff;font-weight:600;background:var(--sc);border-color:var(--sc)}
.score i.on.s1,.score i.on.s2{--sc:var(--t-bug)}
.score i.on.s3{--sc:var(--t-signup)}
.score i.on.s4,.score i.on.s5{--sc:var(--accent);color:#00202e}
.anchors{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px}
.anchors div{background:var(--surface-2);border-radius:8px;padding:8px 10px;font-size:13px;
  color:var(--ink-soft);line-height:1.4}
.anchors b{display:block;font-size:11px;letter-spacing:.08em;color:var(--ink-faint);margin-bottom:2px}
.leeg{margin:0;font-size:13px;color:var(--ink-faint)}

/* bevinding */
.finds{display:flex;flex-direction:column;gap:14px}
.find{border-left:3px solid var(--c,var(--t-algemeen));padding-left:14px;
  display:flex;flex-direction:column;gap:6px}
.find p{margin:0;max-width:68ch}
.tag{align-self:flex-start;font-size:11px;letter-spacing:.05em;text-transform:uppercase;
  font-weight:600;color:var(--c,var(--t-algemeen))}
.bron{font-size:12px;color:var(--ink-faint)}
.hidden{display:none}

/* afbeeldingen */
.shots{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px;margin-top:4px}
.shot{margin:0;display:flex;flex-direction:column;gap:5px}
.shot img{width:100%;border:1px solid var(--line);border-radius:8px;display:block;cursor:zoom-in}
.shot.big{grid-column:1/-1}
.shot.big img{cursor:zoom-out}
.phbox{border:1.5px dashed var(--line);background:var(--surface-2);border-radius:8px;
  min-height:104px;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:5px;color:var(--ink-faint);font-size:13px;padding:10px;text-align:center}
.phbox code{font-size:11px;color:var(--ink-faint);word-break:break-all}
figcaption{font-size:12px;color:var(--ink-faint);line-height:1.35}

/* bugs */
.bugs .cid{color:var(--t-bug)}
.bug{border-left:3px solid var(--t-bug)}
.bugid{background:var(--t-bug);color:#fff;font-variant-numeric:tabular-nums}
.bug p{margin:0;max-width:68ch}
.waar{font-size:12px;color:var(--ink-faint);letter-spacing:.02em}

.foot{display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:12px;
  font-size:12px;color:var(--ink-faint)}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""

JS = """
(function(){
  var wrap=document.getElementById('wrap');
  var chips=wrap.querySelectorAll('.chip[data-f]');
  function apply(){
    var uit=[];
    chips.forEach(function(c){
      if(c.dataset.f!=='all'&&c.getAttribute('aria-pressed')==='false') uit.push(c.dataset.f);
    });
    wrap.querySelectorAll('[data-tab]').forEach(function(el){
      el.classList.toggle('hidden',uit.indexOf(el.dataset.tab)>-1);
    });
    wrap.querySelectorAll('.cat').forEach(function(cat){
      var zicht=cat.querySelectorAll('[data-tab]:not(.hidden)').length;
      var tot=cat.querySelectorAll('[data-tab]').length;
      var c=cat.querySelector('.count');
      if(c&&tot) c.textContent=(uit.length?zicht+' van '+tot+' zichtbaar':
        tot+(tot===1?' bevinding':' bevindingen'));
    });
  }
  wrap.addEventListener('click',function(e){
    var img=e.target.closest?e.target.closest('.shot img'):null;
    if(img) img.parentNode.classList.toggle('big');
  });
  chips.forEach(function(c){
    c.addEventListener('click',function(){
      if(c.dataset.f==='all'){
        chips.forEach(function(o){if(o.dataset.f!=='all')o.setAttribute('aria-pressed','true');});
      } else {
        c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')==='false'?'true':'false');
      }
      apply();
    });
  });
})();
"""

if __name__ == "__main__":
    build()
