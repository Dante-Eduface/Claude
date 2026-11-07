#!/usr/bin/env python3
"""Vult geldplan.html met dagdata uit ABN-exports en schrijft de publiceerbare pagina.

De repo-versie van geldplan.html bevat bewust geen transactieregels (besluit
19-09-2026). Dit script leest de exports, categoriseert ze, en zet het resultaat
in een kopie die gepubliceerd wordt. Die kopie blijft buiten de repo.

Gebruik:  python3 bouw.py <map-met-exports> [uitvoer.html]
Leest .TAB (ABN tabgescheiden) en .STA (MT940).
"""
import re, sys, json, glob, pathlib, collections

VAST = {'NS', 'Huur aan je moeder', 'Zorgpremie', 'Trainmore', 'Kapper (gepind)'}
BOOD = {'Lidl', 'Dirk', 'Medina', 'Albert Heijn', 'AH to go', 'Jumbo', 'Picnic',
        'Hoogvliet', 'Bakker', 'Vomar', 'Kruidvat', 'Etos', 'Action', 'Apotheek',
        'Primera', 'HEMA', 'Digros'}
# volgorde telt: de eerste treffer wint
NAAM = [('ns groep', 'NS'), ('ns reizigers', 'NS'), ('nl56deut0265186420', 'NS'),
        ('nl03zzz301243580000', 'NS'), ('lindeborg', 'Huur aan je moeder'),
        ('zorg en zeker', 'Zorgpremie'), ('zorgverzekeraar', 'Zorgpremie'),
        ('trainmore', 'Trainmore'), ('geldmaat', 'Kapper (gepind)'),
        ('lidl', 'Lidl'), ('dirk', 'Dirk'), ('medina', 'Medina'),
        ('albert heijn', 'Albert Heijn'), ('ah to go', 'AH to go'), ('jumbo', 'Jumbo'),
        ('picnic', 'Picnic'), ('hoogvliet', 'Hoogvliet'), ('tercih', 'Bakker'),
        ('vomar', 'Vomar'), ('kruidvat', 'Kruidvat'), ('etos', 'Etos'),
        ('action', 'Action'), ('apotheek', 'Apotheek'), ('primera', 'Primera'),
        ('hema', 'HEMA'), ('bol.co', 'bol.com'), ('tango', 'Tanken'),
        ('fair amusement', 'Kermis'), ('lib festival', 'Festival'),
        ('voetballen', 'Voetballen'), ('goede schaar', 'Kleermaker'),
        ('she ceo', 'She CEO'), ('north end', 'Café'), ('kraantj', 'Café'),
        ('copa', 'Café'), ('hasta la vista', 'Café'), ('oliebollen', 'Oliebollen'),
        ('one hundred', 'Café'), ('sinai', 'Steakhouse'), ('digros', 'Digros'),
        ('gofast', 'Fietsenwinkel'), ('tivoli', 'TivoliVredenburg')]
# eigen rekeningen: overboekingen hiertussen zijn geen uitgave
EIGEN = ['0882235753', '0884479609', '0118499882', '0142509299']
BETAAL = '882235753'

num = lambda s: float(s.replace('.', '').replace(',', '.'))
clean = lambda s: re.sub(r'\s+', ' ', s).strip()


def lees(map_):
    """Alle mutaties uit .TAB en .STA, ontdubbeld over elkaar overlappende exports."""
    recs = []
    for f in glob.glob(f'{map_}/*.TAB'):
        for regel in open(f, encoding='latin-1'):
            k = regel.rstrip('\n').split('\t')
            if len(k) >= 8:
                recs.append((k[0], k[2], num(k[6]), clean(k[7])))
    for f in glob.glob(f'{map_}/*.STA'):
        acc = cur = None
        for ln in (l.rstrip('\n') for l in open(f, encoding='latin-1')):
            if ln.startswith(':25:'):
                acc = ln[4:].strip()
            elif ln.startswith(':60F:'):
                cur = []
            elif ln.startswith(':62F:'):
                for t in cur or []:
                    recs.append((acc, '20' + t['d'], t['b'], clean(' '.join(t['i']))))
                cur = None
            elif ln.startswith(':61:') and cur is not None:
                m = re.match(r':61:(\d{6})(\d{4})?([CD])([\d.,]+)N', ln)
                if m:
                    cur.append({'d': m.group(1),
                                'b': num(m.group(4)) * (1 if m.group(3) == 'C' else -1),
                                'i': []})
            elif cur and (ln.startswith(':86:') or not ln.startswith(':')):
                cur[-1]['i'].append(ln[4:] if ln.startswith(':86:') else ln)
    uniek = {}
    for a, d, b, i in recs:
        uniek[(a, d, round(b, 2), re.sub(r'[^a-z0-9]', '', i.lower())[:46])] = (a, d, b, i)
    return uniek.values()


def naam(oms):
    laag = oms.lower()
    for sleutel, label in NAAM:
        if sleutel in laag:
            return label
    m = re.search(r'BEA,?\s*(?:Apple Pay|Betaalpas|APPLE PAY|BETAALPAS)\s+'
                  r'([A-Za-z0-9*.\' -]{3,22})', oms)
    return m.group(1).strip().title() if m else 'Overig'


def bouw(map_):
    dagen = collections.defaultdict(list)
    for acc, datum, bedrag, oms in lees(map_):
        if acc != BETAAL or bedrag >= 0:
            continue
        if any(e in oms.lower().replace(' ', '') for e in EIGEN):
            continue  # overboeking naar een eigen potje, geen uitgave
        n = naam(oms)
        groep = 'vast' if n in VAST else ('bood' if n in BOOD else 'rest')
        dagen[datum].append({'n': n, 'b': round(-bedrag, 2), 'c': groep})
    return {d: sorted(v, key=lambda x: -x['b']) for d, v in sorted(dagen.items())}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    hier = pathlib.Path(__file__).parent
    data = bouw(sys.argv[1])
    pagina = (hier / 'geldplan.html').read_text()
    gevuld = re.sub(r'const aDAG=\{\}',
                    'const aDAG=' + json.dumps(data, ensure_ascii=False,
                                               separators=(',', ':')),
                    pagina, count=1)
    uit = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else '/tmp/geldplan-gevuld.html')
    uit.write_text(gevuld)
    posten = sum(len(v) for v in data.values())
    print(f'{uit}: {len(data)} dagen, {posten} posten')
