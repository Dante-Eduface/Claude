"""Zet een blog-markdown (blog-writer formaat) om naar een blog-builder spec-JSON.
Gebruik: python3 md2spec.py <bron.md> <figuren-prefix> <uit.json> [figurl.json]
figurl.json: {"<figuurbestand.png>": "<framerusercontent-url>"}; zonder dat bestand blijft src het lokale pad."""
import re, json, sys, os
from PIL import Image
src, figprefix, out = sys.argv[1:4]
urls = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else {}
FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
txt = open(src).read()
txt = re.sub(r'<!--.*?-->', '', txt, flags=re.S)
fm, body = re.match(r'---\n(.*?)\n---\n(.*)', txt, re.S).groups()
meta = {}
for line in fm.splitlines():
    m = re.match(r'(\w+):\s*(.*)', line)
    if m: meta[m.group(1)] = m.group(2).strip().strip('"')
def runs(s):
    out = []; pos = 0
    for m in re.finditer(r'\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)', s):
        if m.start() > pos: out.append([s[pos:m.start()], False])
        if m.group(1): out.append([m.group(1), True])
        else: out.append([m.group(2), True, m.group(3)])
        pos = m.end()
    if pos < len(s): out.append([s[pos:], False])
    return out
def para(s):
    s = s.strip()
    if '**' in s or '](' in s: return {"t": "p", "runs": runs(s)}
    return {"t": "p", "x": s}
def clean(s): return re.sub(r'\*\*(.+?)\*\*', r'\1', re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)).strip()
figs = sorted([f for f in os.listdir(FIGDIR) if f.startswith(figprefix) and f.endswith('.png')],
              key=lambda f: int(re.search(r'-f(\d+)-', f).group(1)))
figi = 0
lines = body.split('\n'); i = 0; blocks = []; hero = {}
while i < len(lines):
    l = lines[i]
    if not l.strip(): i += 1; continue
    if l.startswith('EYEBROW:'): hero['eyebrow'] = l.split(':', 1)[1].strip(); i += 1; continue
    if l.startswith('# '): hero['h1'] = l[2:].strip(); i += 1; continue
    if not hero.get('subtitle') and re.match(r'^\*[^*].*\*$', l.strip()) and 'h1' in hero and not blocks:
        hero['subtitle'] = l.strip().strip('*'); i += 1; continue
    if l.startswith('By Eduface'):
        parts = [p.strip() for p in l.split('·')]
        hero['meta'] = ' · '.join(parts[:3]); meta['_read'] = parts[2]; i += 1; continue
    if l.startswith('## '):
        h = l[3:].strip(); blocks.append({"t": "h2", "x": "Sources" if h == 'References' else h}); i += 1; continue
    if l.startswith('[CARDS'):
        n = int(re.search(r'\d+', l).group()); items = []; i += 1
        while not lines[i].startswith('[/CARDS]'):
            m = re.match(r'- \*\*(.+?)\*\* \| (.*)', lines[i])
            if m: items.append({"title": m.group(1), "x": m.group(2)})
            i += 1
        blocks.append({"t": "cards", "cols": n if n <= 3 else 2, "items": items}); i += 1; continue
    if l.startswith('[FIGUUR') or l.startswith('[FLOWDIAGRAM'):
        f = figs[figi]; figi += 1
        w, h = Image.open(os.path.join(FIGDIR, f)).size
        alt = open(os.path.join(FIGDIR, f.replace('.png', '.alt'))).read().strip() if os.path.exists(os.path.join(FIGDIR, f.replace('.png', '.alt'))) else f
        blocks.append({"t": "img", "src": urls.get(f, 'local:' + f), "aspect": round(w / h, 4), "alt": alt}); i += 1; continue
    if l.startswith('>'):
        ql = []
        while i < len(lines) and lines[i].startswith('>'):
            ql.append(lines[i][1:].lstrip() if lines[i] != '>' else ''); i += 1
        title = clean(ql[0]) if ql[0].startswith('**') else ''
        rest = ql[1:] if title else ql
        x = '\n'.join(rest).strip()
        b = {"t": "callout", "title": title}
        if ('**' in x or '](' in x) and '\n' not in x: b["runs"] = runs(x)
        else: b["x"] = clean(x)
        blocks.append(b); continue
    if l.startswith('|'):
        rows = []
        while i < len(lines) and lines[i].startswith('|'):
            cells = [clean(c) for c in lines[i].strip().strip('|').split('|')]
            if not all(re.match(r'^-+$', c.replace(':', '')) for c in cells): rows.append(cells)
            i += 1
        head, rows = rows[0], rows[1:]
        blocks.append({"t": "table", "weights": [1.3] + [1] * (len(head) - 1), "head": head, "rows": rows}); continue
    if re.match(r'^\*\*[^*].*\?\*\*$', l.strip()) or re.match(r'^\*\*[^*]+:\*\*$', l.strip()):
        blocks.append({"t": "pb", "x": clean(l)}); i += 1; continue
    if re.match(r'^\*[^*].*\*$', l.strip()):
        blocks.append({"t": "p", "x": l.strip().strip('*')}); i += 1; continue
    blocks.append(para(l)); i += 1
slug = meta['slug']
spec = {"slug": slug, "path": "/resources/blog/" + slug, "category": meta['category'], "readTime": meta['_read'],
        "cardTitle": meta['title'], "seoTitle": meta['seo_title'], "seoDesc": meta['meta_description'],
        "excerpt": hero.get('subtitle', meta['meta_description']), "publishedDate": "2026-10-15T00:00:00.000Z",
        "hero": hero, "blocks": blocks,
        "cta": {"title": "Talk to Eduface about AI-assisted grading", "desc": "See how instructors grade against their own rubric, approve every grade and send it back to the LMS gradebook."}}
json.dump(spec, open(out, 'w'), indent=1, ensure_ascii=False)
from collections import Counter
print(slug, Counter(b['t'] for b in blocks), 'figs used', figi, 'of', len(figs))
