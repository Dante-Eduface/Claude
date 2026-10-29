"""Bouwstenen voor een A4-voorstelpagina. Importeer dit in een paginascript, zie voorbeeld/academica.py."""
import os, re, shutil

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
def page(map, name, body):
    """Schrijft pagina <nr>-<naam>.html in map. Even nummers worden donker, de eerste <h1> wordt de kop met nummer."""
    os.makedirs(map, exist_ok=True)
    shutil.copy(os.path.join(os.path.dirname(__file__), 'style.css'), map)
    nr = int(name.split('-')[0])
    body = re.sub(r'<h1>(.*?)</h1>', lambda m: f'<header class="kop"><div class="label">{nr:02d}</div><h1>{m.group(1)}</h1></header>', body, count=1)
    t, ts = TINT[(nr - 1) % len(TINT) + 1]
    open(os.path.join(map, f'{name}.html'), 'w').write(f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>{name}</title>
<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@700&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css"><style>:root{{--tint:{t};--tint-soft:{ts}}}</style></head><body{' class="dark"' if nr % 2 == 0 else ''}>{body}</body></html>''')

def lens(title, sub, pos, on):
    """Paneel met een lijn en stippen, bijvoorbeeld spreiding van beoordelaars (strenger tot milder)."""
    dots_ = ''.join(f'<span style="position:absolute;top:0.9mm;left:calc({p}% - 2.1mm);width:4.2mm;height:4.2mm;border-radius:50%;box-sizing:border-box;border:0.6mm solid var(--accent);background:{"var(--accent)" if on else "#fff"}"></span>' for p in pos)
    return f'''<div class="panel" style="margin-top:0"><div class="strong">{title}</div><div class="small">{sub}</div>
<div style="position:relative;margin-top:6mm;height:6mm"><span style="position:absolute;left:0;right:0;top:2.8mm;height:0.4mm;background:var(--blue-200)"></span>{dots_}</div>
<div class="small" style="display:flex;justify-content:space-between;margin-top:2mm"><span>Strenger</span><span>Milder</span></div></div>'''

def item(k, t):
    """Rij met icoon en korte titel, voor een opsomming binnen een hoofdkaart."""
    return f'<div class="panel ttl" style="margin-top:4mm;padding:5mm">{icon(k)}<span class="strong" style="font-size:12pt">{t}</span></div>'

def lst(items):
    """Lijst met vinkjes."""
    return '<ul class="list">' + ''.join(f'<li>{CHECK}<span>{t}</span></li>' for t in items) + '</ul>'
