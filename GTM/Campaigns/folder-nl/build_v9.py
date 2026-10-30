"""Bouwt folder-v9.html uit folder-v8.html.

Linker binnenpagina (eigen model) blijft gelijk. Nieuw:
- voorkant: probleem en belofte + Paper Grader-productbeeld
- achterkant: Exam Grader-productbeeld + oproep en contact
- binnen rechts: controleerbaar en veilig
"""
import re

s = open('folder-v8.html', encoding='utf-8').read()
s = s.replace('<title>Eduface folder v8</title>', '<title>Eduface folder v9</title>')

def ic(path, cls='ic sm'):
    return f'<span class="{cls}"><svg viewBox="0 0 24 24">{path}</svg></span>'

CHECK = '<svg class="tick" viewBox="0 0 24 24"><path d="m5 12 5 5 9-10"/></svg>'
WARN = '<svg class="warn-ic" viewBox="0 0 24 24"><path d="M12 4 2.5 20h19Z"/><path d="M12 10v4M12 17.2v.3"/></svg>'
CHEV_L = '<svg viewBox="0 0 24 24"><path d="m15 6-6 6 6 6"/></svg>'
CHEV_R = '<svg viewBox="0 0 24 24"><path d="m9 6 6 6-6 6"/></svg>'

def sk(*w):  # skeleton-regels
    return ''.join(f'<i style="width:{x}%"></i>' for x in w)

# ------------------------------------------------------------------ Paper Grader
paper = f'''
<div class="app">
  <div class="app-bar"><span class="crumb">Toetsbeleid · Essay 2 <em>/</em> <b>Inzending 140 van 142</b></span>
    <span class="bar-r">Wacht 6 dagen <span class="nav">{CHEV_L}</span><span class="nav">{CHEV_R}</span></span></div>
  <div class="app-body">
    <div class="col-doc">
      <div class="doc-top"><span class="skel title"></span><span class="muted">2.140 woorden</span></div>
      <div class="skel-lines">{sk(96, 100, 88, 64)}</div>
      <span class="skel sub"></span>
      <p class="doc-p">In de praktijk <mark>controleren examencommissies vooral achteraf. Dit laat zien dat een steekproef nooit genoeg zicht geeft op de spreiding tussen beoordelaars.</mark></p>
      <div class="sugg">
        <div class="sugg-h"><i class="dot"></i>Voorgestelde opmerking <em>·</em> <b>Onderbouwing</b></div>
        <p>Je trekt een algemene conclusie uit één observatie. Noem het onderzoek waaruit blijkt dat commissies vooral achteraf controleren, en leg uit waarom een steekproef de spreiding mist.</p>
        <div class="btns"><span class="btn-p">{CHECK}Goedkeuren</span><span class="btn-o">Bewerken</span><span class="btn-t">Verwerpen</span></div>
      </div>
      <div class="skel-lines">{sk(92, 100, 70, 96, 84)}</div>
    </div>
    <div class="col-score">
      <div class="sc-h"><b>Score per criterium</b><span class="muted">Weging · Score</span></div>
      <div class="sc-row"><span class="skel" style="width:58%"></span><span class="w">25%</span><span class="v">8 / 10</span></div>
      <div class="sc-row"><span class="skel" style="width:72%"></span><span class="w">20%</span><span class="v">7 / 10</span></div>
      <div class="sc-row"><span class="skel" style="width:46%"></span><span class="w">20%</span><span class="v need">{WARN}jouw oordeel</span></div>
      <div class="sc-row"><span class="skel" style="width:64%"></span><span class="w">20%</span><span class="v">6 / 10</span></div>
      <div class="sc-row"><span class="skel" style="width:52%"></span><span class="w">15%</span><span class="v">8 / 10</span></div>
      <div class="gen">
        <div class="sugg-h"><i class="dot"></i>Algemene feedback <em>·</em> <b>concept</b></div>
        <p>Heldere probleemstelling. Het zwakke punt is de onderbouwing: twee keer trek je een conclusie zonder bron.</p>
        <div class="btns"><span class="btn-o">{CHECK}Goedkeuren</span><span class="btn-t">Bewerken</span></div>
      </div>
      <div class="total"><span><b>7,2</b> / 10 voorgesteld</span><span class="muted">1 criterium open</span></div>
      <div class="app-foot"><span class="muted">Gaat naar het cijferregister.</span><span class="btn-p">{CHECK}Cijfer goedkeuren</span></div>
    </div>
  </div>
</div>'''

# ------------------------------------------------------------------ Exam Grader
exam = f'''
<div class="app">
  <div class="app-bar"><span class="crumb">Bedrijfseconomie · Tentamen blok 2 <em>/</em> <b>Inzending 61 van 64</b></span>
    <span class="bar-r"><span class="nav">{CHEV_L}</span><span class="nav">{CHEV_R}</span></span></div>
  <div class="app-body">
    <div class="col-doc">
      <span class="cap">Vraag 2 · 6 punten</span>
      <p class="q">Een bakkerij betaalt € 2.000 huur per maand en € 0,40 aan grondstoffen per brood. Welke kosten zijn vast en welke variabel, en wat gebeurt er met de kostprijs per brood als de productie stijgt?</p>
      <div class="key">
        <span class="cap">Correctiemodel</span>
        <ul><li>Huur is vast, grondstoffen zijn variabel</li><li>Vaste kosten per brood dalen bij meer productie</li><li>Variabele kosten per brood blijven gelijk</li></ul>
      </div>
      <span class="cap">Antwoord student</span>
      <p class="ans">Huur is vast en de grondstoffen zijn variabel. <mark>Als je meer broden bakt, wordt elk brood goedkoper.</mark></p>
    </div>
    <div class="col-score">
      <div class="fb">
        <div class="fb-h"><svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4Z"/></svg>Feedback op vraag 2</div>
        <p>Je deelt de kosten goed in. Bij de kostprijs mis je een stap: alleen de vaste kosten per brood dalen, de € 0,40 aan grondstoffen blijft gelijk. Zeg welk deel daalt en waarom.</p>
        <div class="fb-next"><span>Vraag 3 · Break-even</span><span class="ok-s">{CHECK}Feedback klaar</span></div>
      </div>
      <div class="sc-h"><b>Score per criterium</b><span class="muted">Punten</span></div>
      <div class="sc-row two"><span>Indeling van de kosten</span><span class="v">2 / 2</span></div>
      <div class="sc-row two"><span>Verloop van de kostprijs</span><span class="v need">{WARN}twijfel · 1 / 2</span></div>
      <div class="sc-row two"><span>Uitleg en begrippen</span><span class="v">1 / 2</span></div>
      <div class="total"><span><b>4</b> / 6 voorgesteld</span><span class="btn-p">{CHECK}Cijfer goedkeuren</span></div>
    </div>
  </div>
</div>'''

# ------------------------------------------------------------------ Sheet 1
LOCK = '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'
MAIL = '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>'
PHONE = '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>'
WEB = '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>'

sheet1 = f'''<section class="sheet">

  <div class="panel dark back9">
    <span class="kick">EXAM GRADER</span>
    <h2 class="h9">Open vragen, nagekeken tegen jullie correctiemodel.</h2>
    <div class="shotwrap dark-shot">{exam}</div>
    <div class="used9">
      <span class="lbl">Gebruikt door</span>
      <div class="logos9"><div class="ph">Hogeschool Rotterdam<small>logo</small></div><div class="ph">Tilburg University<small>logo</small></div><div class="ph">Radboud Universiteit<small>logo</small></div></div>
    </div>
    <div class="cta9">
      <h3>Laat één van jullie eigen opdrachten nakijken en leg het cijfer naast dat van jullie docent.</h3>
      <div class="contact9">
        <div>{ic(MAIL, 'ic sm inv')}dante.torbed@eduface.me</div>
        <div>{ic(PHONE, 'ic sm inv')}+31 6394 090 99</div>
        <div>{ic(WEB, 'ic sm inv')}eduface.me</div>
      </div>
      <div class="qr">QR<br>[link]</div>
    </div>
  </div>

  <div class="panel front9">
    <img class="logo" src="../../../Design/Merk/logos/logo_navy.png" alt="Eduface">
    <h1>Twee docenten.<br>Eén paper.<br>Twee verschillende cijfers.</h1>
    <div class="promise">
      <span class="kick">PAPER GRADER</span>
      <p>Elk paper nagekeken op jullie rubric, met per criterium de onderbouwing. <b>De docent keurt het cijfer goed.</b></p>
    </div>
    <div class="shotwrap">{paper}</div>
    <div class="lms">
      <div class="lms-h"><b>Werkt in jullie LMS</b><span>Cijfers en feedback gaan automatisch terug.</span></div>
      <div class="lms-row"><div class="ph">Moodle</div><div class="ph">Blackboard</div><div class="ph">Brightspace</div><div class="ph">Canvas</div><div class="ph">itslearning</div><div class="ph">NEO LMS</div></div>
    </div>
  </div>
</section>'''

a = s.index('<section class="sheet">')
b = s.index('</section>', a) + len('</section>')
s = s[:a] + sheet1 + s[b:]

# ------------------------------------------------------------------ Binnen rechts
SHIELD = '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6Z"/><path d="m9 12 2 2 4-4"/>'
EU = '<circle cx="12" cy="12" r="9"/><path d="M12 7v.01M15.5 8.5v.01M17 12v.01M15.5 15.5v.01M12 17v.01M8.5 15.5v.01M7 12v.01M8.5 8.5v.01"/>'
NOTRAIN = '<circle cx="12" cy="12" r="9"/><path d="m5.6 5.6 12.8 12.8"/>'
SCALE = '<path d="M12 3v18M7 21h10M5 7h14"/><path d="m5 7-3 6a3 3 0 0 0 6 0Z"/><path d="m19 7-3 6a3 3 0 0 0 6 0Z"/>'
USERCHK = '<circle cx="9" cy="8" r="4"/><path d="M2 21c.7-4 3.5-6 7-6 1.8 0 3.3.5 4.5 1.4"/><path d="m16 17 2 2 4-4"/>'
LINES = '<path d="M4 6h16M4 12h10M4 18h13"/>'
HIST = '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l3 2"/>'

right = f'''  <div class="panel safe">
    <h2>Controleerbaar en veilig</h2>
    <p class="body lead9">Elk cijfer is te herleiden, elke stap ligt vast, en jullie data blijft van jullie.</p>

    <span class="grp">Controleerbaar</span>
    <div class="two9">
      <div class="card9">
        <div class="c9-h">{ic(LINES, 'ic')}<div><h3>Explainability</h3><p class="body">Elke score per criterium, gekoppeld aan de passage in de tekst.</p></div></div>
        <div class="viz">
          <div class="vz-row"><span>Analyse</span><b>7 / 10</b></div>
          <div class="vz-link">↳ alinea 2 · <mark>controleren vooral achteraf</mark></div>
        </div>
      </div>
      <div class="card9">
        <div class="c9-h">{ic(HIST, 'ic')}<div><h3>Auditability</h3><p class="body">Bij summatieve toetsen wordt elke stap bewaard, in een audit trail die voldoet aan de AI Act.</p></div></div>
        <div class="viz log">
          <div><span>09:12</span>AI-voorstel per criterium</div>
          <div><span>09:14</span>Docent past opmerking aan</div>
          <div class="done"><span>09:15</span>Cijfer goedgekeurd</div>
        </div>
      </div>
    </div>

    <span class="grp">Veilig</span>
    <div class="safe-card">
      <div class="sf">{ic(EU, 'ic mi')}<div><b>Data blijft in de EU</b><span>Opslag en verwerking binnen Europa.</span></div></div>
      <div class="sf">{ic(NOTRAIN, 'ic mi')}<div><b>Niet getraind op jullie data</b><span>Studentwerk wordt nooit gebruikt om het model te trainen.</span></div></div>
      <div class="sf">{ic(SHIELD, 'ic mi')}<div><b>Beleid sluit aan op de AVG</b><span>Verwerking volgens de Europese privacywet.</span></div></div>
      <div class="sf">{ic(USERCHK, 'ic mi')}<div><b>Voldoet aan de AI Act</b><span>De docent beslist over elk cijfer, en alles is vastgelegd.</span></div></div>
    </div>
  </div>
'''
a = s.index('  <div class="panel how">')
b = s.index('</section>', a)
s = s[:a] + right + s[b:]

css = '''
  /* ===================== v9 ===================== */
  /* productbeeld, in de stijl van de echte app */
  .shotwrap { position: relative; margin-top: 16px; min-width: 0; }
  .sheet { grid-template-columns: minmax(0,1fr) minmax(0,1fr); }
  .panel { min-width: 0; }
  .app { width: 690px; zoom: .697; background: var(--white); border: 1px solid var(--ink-100); border-radius: 14px; box-shadow: 0 18px 50px rgba(0,35,51,.12); overflow: hidden; font-size: 13px; color: var(--navy); }
  .dark-shot .app { box-shadow: 0 22px 60px rgba(0,0,0,.35); }
  .app-bar { display: flex; justify-content: space-between; align-items: center; padding: 11px 18px; border-bottom: 1px solid var(--ink-100); }
  .crumb { color: var(--ink-500); } .crumb em { font-style: normal; margin: 0 4px; color: var(--ink-300); } .crumb b { color: var(--navy); font-weight: 500; }
  .bar-r { display: flex; align-items: center; gap: 8px; color: var(--ink-500); }
  .nav { width: 26px; height: 26px; border: 1px solid var(--ink-200); border-radius: 7px; display: grid; place-items: center; }
  .nav svg { width: 14px; height: 14px; fill: none; stroke: var(--navy); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
  .app-body { display: grid; grid-template-columns: 1fr 270px; }
  .col-doc { padding: 16px 18px; border-right: 1px solid var(--ink-100); display: flex; flex-direction: column; gap: 10px; }
  .col-score { padding: 16px 18px; display: flex; flex-direction: column; }
  .muted { color: var(--ink-500); font-size: 12px; }
  .doc-top { display: flex; justify-content: space-between; align-items: center; }
  .skel { display: block; height: 8px; border-radius: 4px; background: var(--ink-200); }
  .skel.title { width: 55%; height: 10px; } .skel.sub { width: 34%; height: 9px; margin-top: 4px; }
  .skel-lines { display: flex; flex-direction: column; gap: 7px; } .skel-lines i { display: block; height: 6px; border-radius: 3px; background: var(--ink-100); }
  .doc-p { font-size: 13px; line-height: 1.55; color: var(--ink-700); }
  .doc-p mark, .ans mark { background: var(--mint); border-bottom: 2px solid var(--green); padding: 0 1px; }
  .sugg { border: 1px solid var(--ink-200); border-radius: 12px; padding: 12px 14px; box-shadow: 0 4px 14px rgba(0,35,51,.06); display: flex; flex-direction: column; gap: 8px; }
  .sugg-h { font-size: 12px; color: var(--ink-500); display: flex; align-items: center; gap: 6px; } .sugg-h em { font-style: normal; } .sugg-h b { color: var(--navy); font-weight: 500; }
  .dot { width: 7px; height: 7px; border-radius: 99px; background: var(--ink-300); display: inline-block; }
  .sugg p, .gen p { font-size: 12.5px; line-height: 1.5; color: var(--navy); }
  .btns { display: flex; align-items: center; gap: 8px; }
  .btn-p, .btn-o, .btn-t { display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 600; border-radius: 8px; padding: 6px 11px; white-space: nowrap; }
  .btn-p { background: var(--navy); color: var(--white); } .btn-o { border: 1px solid var(--ink-200); color: var(--navy); } .btn-t { color: var(--ink-500); font-weight: 500; }
  .tick { width: 13px; height: 13px; fill: none; stroke: currentColor; stroke-width: 2.4; stroke-linecap: round; stroke-linejoin: round; }
  .sc-h { display: flex; justify-content: space-between; align-items: baseline; padding-bottom: 8px; border-bottom: 1px solid var(--ink-100); }
  .sc-h b { font-size: 14px; }
  .sc-row { display: grid; grid-template-columns: 1fr 40px 92px; align-items: center; gap: 8px; padding: 10px 0; border-bottom: 1px solid var(--ink-100); font-size: 12.5px; }
  .sc-row.two { grid-template-columns: 1fr auto; }
  .sc-row .skel { height: 7px; background: var(--ink-100); }
  .sc-row .w { color: var(--ink-500); text-align: right; } .sc-row .v { text-align: right; font-variant-numeric: tabular-nums; }
  .v.need { color: #b3261e; font-weight: 600; display: inline-flex; align-items: center; justify-content: flex-end; gap: 4px; }
  .warn-ic { width: 13px; height: 13px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
  .gen { margin-top: 12px; display: flex; flex-direction: column; gap: 8px; }
  .total { display: flex; justify-content: space-between; align-items: center; margin-top: 12px; padding-top: 10px; border-top: 1px solid var(--ink-100); font-size: 12.5px; color: var(--ink-500); }
  .total b { font-family: var(--display); font-size: 26px; color: var(--navy); margin-right: 2px; }
  .app-foot { display: flex; justify-content: space-between; align-items: center; gap: 10px; margin-top: 10px; padding-top: 10px; border-top: 1px solid var(--ink-100); }
  .app-foot .muted { font-size: 11px; }
  .cap { font-size: 10.5px; font-weight: 600; letter-spacing: .06em; color: var(--ink-500); text-transform: uppercase; }
  .q { font-size: 13.5px; font-weight: 600; line-height: 1.5; color: var(--navy); }
  .key { border: 1.5px solid var(--navy); border-radius: 10px; background: var(--ink-50); padding: 10px 12px; display: flex; flex-direction: column; gap: 6px; }
  .key ul { margin: 0; padding-left: 16px; font-size: 12.5px; line-height: 1.5; color: var(--ink-700); }
  .ans { font-size: 13px; line-height: 1.55; color: var(--ink-700); }
  .fb { border: 1px solid var(--mint-line); border-left: 4px solid var(--green); background: var(--mint); border-radius: 10px; padding: 12px 13px; display: flex; flex-direction: column; gap: 7px; margin-bottom: 14px; }
  .fb-h { display: flex; align-items: center; gap: 7px; font-size: 13.5px; font-weight: 600; }
  .fb-h svg { width: 15px; height: 15px; fill: none; stroke: var(--green-deep); stroke-width: 2; stroke-linejoin: round; }
  .fb p { font-size: 12.5px; line-height: 1.5; }
  .fb-next { display: flex; justify-content: space-between; font-size: 11.5px; color: var(--ink-500); border-top: 1px solid var(--mint-line); padding-top: 7px; }
  .ok-s { color: var(--green-deep); font-weight: 600; display: inline-flex; align-items: center; gap: 4px; }

  /* voorkant */
  .front9 .logo { height: 24px; align-self: flex-start; }
  .front9 .app-body { grid-template-columns: 1fr 300px; }
  .front9 .sc-row { grid-template-columns: 1fr 36px 104px; }
  .front9 .sc-row .skel { width: auto !important; }
  .front9 h1 { margin-top: 22px; font-size: 39px; }
  .promise { margin-top: 18px; border-left: 3px solid var(--green); padding-left: 14px; }
  .promise p { font-size: 14.5px; line-height: 1.45; color: var(--ink-700); margin-top: 4px; max-width: 44ch; } .promise b { color: var(--navy); }
  .front9 .lms { margin-top: auto; padding-top: 10px; }
  .front9 .shotwrap { margin-top: 18px; }

  /* achterkant */
  .h9 { font-size: 24px; color: var(--white); margin-top: 6px; max-width: 22ch; }
  .back9 .shotwrap { margin-top: 14px; }
  .back9 .used9 { margin-top: 14px; }
  .used9 { margin-top: 4px; }
  .logos9 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 8px; } .logos9 .ph { height: 44px; font-size: 11px; }
  .cta9 { margin-top: auto; padding-top: 16px; border-top: 1px solid var(--line-inv); display: grid; grid-template-columns: 1fr 92px; gap: 6px 18px; }
  .cta9 h3 { grid-column: 1 / -1; font-size: 19px; line-height: 1.15; color: var(--white); margin-bottom: 6px; }
  .contact9 { display: flex; flex-direction: column; gap: 7px; justify-content: center; } .contact9 div { display: flex; align-items: center; gap: 10px; font-size: 12.5px; }
  .back9 .qr { width: 92px; height: 92px; }

  /* binnen rechts */
  .safe h2 { margin-top: 0; }
  .lead9 { font-size: 13.5px; margin-top: 6px; max-width: 46ch; }
  .grp { display: block; font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-500); margin: 18px 0 8px; }
  .two9 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .card9 { border: 1px solid var(--ink-100); background: var(--ink-50); border-radius: 12px; padding: 14px; display: flex; flex-direction: column; gap: 12px; }
  .c9-h { display: flex; flex-direction: column; gap: 8px; } .c9-h h3 { font-size: 16px; } .c9-h .body { font-size: 12px; margin-top: 2px; }
  .viz { margin-top: auto; background: var(--white); border: 1px solid var(--ink-100); border-radius: 9px; padding: 9px 10px; font-size: 11px; display: flex; flex-direction: column; gap: 5px; }
  .vz-row { display: flex; justify-content: space-between; font-weight: 600; } .vz-link { color: var(--ink-500); }
  .viz.log div { display: flex; gap: 8px; color: var(--ink-700); } .viz.log span { color: var(--ink-500); font-variant-numeric: tabular-nums; }
  .viz.log .done { color: var(--green-deep); font-weight: 600; }
  .safe-card { flex: 1; border: 1px solid var(--mint-line); background: var(--mint); border-radius: 14px; padding: 6px 16px; display: flex; flex-direction: column; justify-content: space-around; }
  .sf { display: grid; grid-template-columns: 36px 1fr; gap: 12px; align-items: center; padding: 9px 0; }
  .sf + .sf { border-top: 1px solid var(--mint-line); }
  .sf .ic { width: 36px; height: 36px; background: var(--white); }
  .sf b { display: block; font-size: 14px; } .sf span:not(.ic) { font-size: 12px; color: var(--ink-700); }
</style>'''
s = s.replace('</style>', css, 1)
open('folder-v9.html', 'w', encoding='utf-8').write(s)
print('ok')
