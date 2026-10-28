import re
"""Genereert de zes pagina's op één stylesheet."""
IC = {
 'scale':'<path d="M12 3v18M7 21h10M5 7h14M5 7l-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z"/>',
 'doc':'<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
 'shield':'<path d="M12 3 5 6v6c0 4 3 7 7 9 4-2 7-5 7-9V6z"/><path d="m9 12 2 2 4-4"/>',
 'chat':'<path d="M4 5h16v11H9l-5 4z"/><path d="m9 11 2 2 4-4"/>',
 'link':'<path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/>',
 'users':'<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/>',
 'flow':'<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/><path d="M6.5 10v4a3 3 0 0 0 3 3H14"/>',
 'chart':'<path d="M4 20h16M7 16v-4M12 16V8M17 16v-7"/>',
 'lock':'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
}
def icon(k): return f'<span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{IC[k]}</svg></span>'
def ttl(k, t): return f'<div class="ttl">{icon(k)}<h2>{t}</h2></div>'
CHECK = '<span class="check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>'
# Een mensje per 5% van de studenten: gevuld krijgt feedback, met alleen een rand niet
PERSON = '<circle cx="12" cy="7.5" r="4"/><path d="M4 21.5c0-4.7 3.6-8 8-8s8 3.3 8 8z"/>'
def dots(k):
    # Twee rijen van tien. Een rij zonder feedback krijgt een kader, zodat de lege plekken opvallen.
    rows = []
    for r in range(2):
        figs = ''.join(f'<svg class="{"on" if r * 10 + i < k else ""}" viewBox="0 0 24 24">{PERSON}</svg>' for i in range(10))
        empty = r * 10 >= k
        rows.append(f'<div class="dots{" empty" if empty else ""}">{figs}</div>' + ('<div class="small" style="margin-top:1.5mm">Krijgt nu geen feedback</div>' if empty else ''))
    return '<div style="margin-top:6mm">' + ''.join(rows) + '</div>'
def hbar(lbl, pct, val, on=False, avg=None):
    a = f'<span style="position:absolute;top:-1.5mm;bottom:-1.5mm;left:{avg}%;width:0.5mm;background:var(--muted)"></span>' if avg else ''
    return f'<div class="hbar{" on" if on else ""}"><span>{lbl}</span><div class="track"><div class="fill" style="width:{pct}%"></div>{a}</div><b>{val}</b></div>'
# Per onderdeel een eigen tint (hoofdkaart, tweede kaart), om en om een lichte en een donkere pagina
TINT = {1: ('#e3e6f4', '#f1f2f9'), 2: ('#e4e0f5', '#f1eff9'), 3: ('#dfe8f3', '#eef3f9'),
        4: ('#e0eaf0', '#eff5f8'), 5: ('#dde4f7', '#edf1fb'), 6: ('#e6e8ee', '#f3f4f7')}
def page(name, body, first=False):
    nr = int(name.split('-')[0])
    body = re.sub(r'<h1>(.*?)</h1>', lambda m: f'<header class="kop"><div class="label">{nr:02d}</div><h1>{m.group(1)}</h1></header>', body, count=1)
    t, ts = TINT[nr]
    open(f'{name}.html', 'w').write(f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>{name}</title>
<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css"><style>:root{{--tint:{t};--tint-soft:{ts}}}</style></head><body{' class="dark"' if nr % 2 == 0 else ''}>{body}</body></html>''')

page('1-opening', f'''
<h1>Voorstel</h1>
<p class="lead">Eduface is een onderwijskundig AI-model, ontwikkeld met hulp van de Universiteit Leiden en de Radboud Universiteit, dat formatieve en summatieve feedback geeft op studentopdrachten. Docenten besteden daardoor minder tijd aan het formuleren van feedback, elke student krijgt formatieve feedback, en een groeiend aantal studenten vraagt niet om evenredig meer nakijkers.</p>
<p class="statement">Dat is een concrete invulling van het koerspunt efficiëntie.</p>
<div class="stack">
  <div class="duo">
    <section class="card tertiary"><div class="label">Nu</div><div class="num" style="margin-top:3mm">€ 37.000</div><p class="desc">Feedback voor de helft</p>{dots(10)}</section>
    <section class="card primary"><div class="label">Met Eduface</div><div class="num" style="margin-top:3mm">€ 18.000</div><p class="desc">Feedback voor elke student</p>{dots(20)}</section>
  </div>
  <p class="small" style="margin-top:3mm">Elk poppetje staat voor 5% van de studenten.</p>
  <section class="card secondary"><div class="num">76% goedkoper</div><p class="desc">per student die feedback krijgt</p></section>
</div>''')

page('2-kosten', f'''
<h1>Kosten</h1>
<div class="stack">
  <section class="card primary">
    <div class="num">€ 3,75</div>
    <p class="desc">per student per maand* · exclusief btw</p>
    <div class="panel">
      <div class="strong">Hoe meer studenten, hoe lager de prijs per student</div>
      <div class="small">Prijs per student per maand</div>
      <div class="hbars">{hbar("Tot en met 400", 100, "€ 3,75", on=True)}{hbar("Meer dan 400", 80, "€ 3,00")}</div>
    </div>
    <p class="small" style="margin-top:4mm">* Minimaal € 1.500 per maand, dat dekt de eerste 400 studenten.</p>
  </section>
</div>''')

lens = lambda title, sub, pos, on: f'''<div class="panel" style="margin-top:0"><div class="strong">{title}</div><div class="small">{sub}</div>
<div style="position:relative;margin-top:6mm;height:6mm"><span style="position:absolute;left:0;right:0;top:2.8mm;height:0.4mm;background:var(--blue-200)"></span>{''.join(f'<span style="position:absolute;top:0.9mm;left:calc({p}% - 2.1mm);width:4.2mm;height:4.2mm;border-radius:50%;box-sizing:border-box;border:0.6mm solid var(--accent);background:{"var(--accent)" if on else "#fff"}"></span>' for p in pos)}</div>
<div class="small" style="display:flex;justify-content:space-between;margin-top:2mm"><span>Strenger</span><span>Milder</span></div></div>'''
page('3-instelling', f'''
<h1>Opbrengst</h1>
<div class="stack">
  <section class="card primary">{ttl("scale","Uniforme beoordeling")}
    <p class="desc">Elke opdracht wordt langs dezelfde criteria beoordeeld, door elke beoordelaar.</p>
    <div class="duo" style="margin-top:6mm">{lens("Zonder","Elke beoordelaar met een eigen blik",[14,42,63,88],False)}{lens("Met Eduface","Iedereen langs dezelfde criteria",[44,50,56,62],True)}</div>
  </section>
  <section class="card secondary">{ttl("chat","Formatieve feedback voor elke student")}
    <p class="desc">Nu krijgt de helft van de studenten formatieve feedback. Met Eduface is dat iedereen.</p>
  </section>
  <section class="card tertiary">{ttl("link","Integratie in NEO LMS")}
    <p class="desc">Opdrachten en cijfers lopen via NEO. Docenten en studenten werken in de omgeving die ze kennen.</p>
  </section>
</div>''')

page('4-accreditatie', f'''
<h1>Accreditatie</h1>
<div class="stack">
  <section class="card primary">{ttl("scale","Beoordelaars oordelen consistent")}
    <p class="desc">Zie in één overzicht wie afwijkt van het team.</p>
    <div class="panel">
      <div class="small" style="display:flex;justify-content:space-between"><span>Voorbeeld per docent</span><span>Gemiddelde 7,1</span></div>
      <div class="hbars">{hbar("Docent A",72,"7,2",avg=71)}{hbar("Docent B",70,"7,0",avg=71)}{hbar("Docent C",56,"5,6",on=True,avg=71)}</div>
    </div>
  </section>
  <section class="card secondary">{ttl("doc","Elk cijfer is navolgbaar")}
    <p class="desc">Onderbouwing per rubriccriterium.</p><span class="tag" style="background:#fff">AI Act audit trail</span>
  </section>
  <section class="card tertiary">{ttl("shield","De examencommissie borgt de kwaliteit")}
    <p class="desc">Elke onderbouwing direct in te zien.</p>
  </section>
  <p class="note" style="margin-top:10mm">Consistent beoordelen is een speerpunt van dit project. Daarmee helpt het om de eisen van de accreditatiepartij hierboven steviger te borgen, en dat kan een positieve impact hebben op de pabo, die nu in de accreditatie zit.</p>
</div>''')

item = lambda k, t: f'<div class="panel ttl" style="margin-top:4mm;padding:5mm">{icon(k)}<span class="strong" style="font-size:12pt">{t}</span></div>'
page('5-koersplan', f'''
<h1>Koersplan</h1>
<p class="lead">Deze investering sluit naadloos aan op het kopje Efficiëntie uit het koersplan dat Academica voor de komende jaren heeft opgesteld. Binnen dat kopje versterkt het direct drie punten.</p>
<div class="stack">
  <section class="card primary"><div class="label">Koersplan Academica</div><h2 style="margin-top:2mm">Efficiëntie</h2>
    <div style="margin-top:2mm">{item("users","Een stevig kernteam")}{item("flow","Betere processen")}{item("chart","Datagedreven")}</div>
  </section>
</div>''')

lst = lambda items: '<ul class="list">' + ''.join(f'<li>{CHECK}<span>{t}</span></li>' for t in items) + '</ul>'
page('6-privacy', f'''
<h1>Privacy</h1>
<div class="stack">
  <section class="card primary">{ttl("shield","Academica blijft eigenaar van al het studentenwerk en alle data.")}</section>
  <section class="card tertiary">{ttl("lock","Gebruik van de data")}{lst(["Studentenwerk wordt nooit gebruikt om AI-modellen te trainen.","Verwerking alleen voor het afgesproken onderwijsdoel, in opdracht van Academica."])}</section>
  <section class="card tertiary">{ttl("globe","Waar de data staat")}{lst(["Data alleen in de EU, ook bij Microsoft, Google en Railway.","Eigen model, geen koppeling met een extern AI-model."])}</section>
  <section class="card tertiary">{ttl("scale","Wet en regie")}{lst(["AVG: verwerkersovereenkomst, een datalek binnen 48 uur gemeld.","AI Act: audit trail voor elke summatieve beoordeling.","De docent beslist, de AI assisteert."])}</section>
</div>''')
