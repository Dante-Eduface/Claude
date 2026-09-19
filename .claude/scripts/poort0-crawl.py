#!/usr/bin/env python3
"""Crawl a provider site shallowly and pull sentences that answer: who marks the work?
Usage: scan.py <slug> <starturl>  -> writes out/<slug>.txt
"""
import sys, re, os, html, urllib.parse, io
import urllib.request

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'}

OWN = re.compile(r'marked by|marking|marker|assessed by|internal moderation|internally verified|internal verification|standardisation|board of examiners|assessment board|examination board|exam board|assessment criteria|assessment brief|dissertation|coursework|written assignment|reflective (essay|journal|report)|portfolio is assessed|feedback on (your|assessed)|working days|tutors? (will |)(mark|assess|provide feedback)', re.I)
EXTERN = re.compile(r'awarded by (Pearson|BTEC|NCFE|City ?& ?Guilds|OCR|AQA|Highfield|CMI|ILM)|Pearson VUE|Ofqual|awarding (organisation|body)|externally (assessed|marked|set|examined)|external examination|prepares? you for the (ACCA|CIMA|ICAEW|CII|CIPD|CFA|CIM|NEBOSH|IOSH)|end-?point assessment|EPAO', re.I)
DUUR = re.compile(r'\b\d{1,2}\s*(years?|months?)\b|\b(one|two|three|four)[- ]year|\b\d{3}\s*credits?\b|full-?time', re.I)
PRIJS = re.compile(r'(£|GBP\s?)[\d,]{4,}', re.I)
SIZE = re.compile(r'(over |more than |around |approximately |some )?[\d,]{3,7}\+? (students|learners|apprentices)', re.I)

LINKPAT = re.compile(r'assess|regulation|polic|quality|handbook|how-you|marking|academic|about|student|course|fees|tuition', re.I)


def fetch(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            ct = r.headers.get('Content-Type', '')
            raw = r.read(3_000_000)
            if 'pdf' in ct or url.lower().endswith('.pdf'):
                try:
                    import fitz
                    doc = fitz.open(stream=raw, filetype='pdf')
                    return '\n'.join(p.get_text() for p in doc), 'pdf'
                except Exception:
                    return '', 'pdf'
            return raw.decode('utf-8', 'ignore'), 'html'
    except Exception as e:
        return '', 'err:' + str(e)[:60]


def text_of(h):
    h = re.sub(r'(?is)<(script|style|nav|footer)[^>]*>.*?</\1>', ' ', h)
    t = re.sub(r'<[^>]+>', ' ', h)
    return re.sub(r'\s+', ' ', html.unescape(t))


def sentences(t):
    return re.split(r'(?<=[.!?])\s+', t)


def main():
    slug, start = sys.argv[1], sys.argv[2]
    base = urllib.parse.urlparse(start)
    root = base.scheme + '://' + base.netloc
    seen = set()
    todo = [start]
    out = []
    pages = 0
    while todo and pages < 10:
        u = todo.pop(0)
        if u in seen:
            continue
        seen.add(u)
        body, kind = fetch(u)
        if not body:
            continue
        pages += 1
        t = text_of(body) if kind == 'html' else re.sub(r'\s+', ' ', body)
        for s in sentences(t):
            s = s.strip()
            if len(s) < 30 or len(s) > 400:
                continue
            tags = []
            if OWN.search(s):
                tags.append('OWN')
            if EXTERN.search(s):
                tags.append('EXT')
            if SIZE.search(s):
                tags.append('SIZE')
            if PRIJS.search(s) and re.search(r'fee|tuition|cost|price', s, re.I):
                tags.append('FEE')
            if DUUR.search(s) and re.search(r'course|programme|degree|study|duration|ba |bsc |ma |msc |hnd|hnc', s, re.I):
                tags.append('DUR')
            if tags:
                out.append('[' + ','.join(tags) + '] ' + s + ' <<' + u)
        if pages < 10 and kind == 'html':
            for href in re.findall(r'href="([^"#]+)"', body):
                if href.startswith('mailto') or href.startswith('tel'):
                    continue
                full = urllib.parse.urljoin(u, href)
                if not full.startswith(root):
                    continue
                if full in seen or full in todo:
                    continue
                if LINKPAT.search(full):
                    todo.append(full)
            todo.sort(key=lambda x: 0 if re.search(r'assess|regulat|polic|handbook|marking', x, re.I) else 1)
    os.makedirs('out', exist_ok=True)
    # dedupe
    ded = []
    s2 = set()
    for l in out:
        k = l.split(' <<')[0]
        if k in s2:
            continue
        s2.add(k)
        ded.append(l)
    with open('out/' + slug + '.txt', 'w') as f:
        f.write('PAGES: %d\n' % pages + '\n'.join(ded[:120]))


main()
