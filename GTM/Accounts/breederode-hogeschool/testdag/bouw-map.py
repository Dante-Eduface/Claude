#!/usr/bin/env python3
"""Zet vakdossiers en beoordelingsformulieren om in een genummerd mapje.

Geen voorblad: blad 1 is de beoordeling naast elkaar. De beoordelingsoptie
staat op blad 1, onder de naamregel.
"""
import re

HDR = ('<div class="top">\n  <img src="breederode.png" class="bdlogo">\n'
       '  <div class="edu"><img src="eduface.png"></div>\n</div><div class="rule"></div>')

MODUS = {
 'voldaan': dict(
   label='Voldaan of niet voldaan, per rubriekcriterium',
   waarom=None),
 'descriptief': dict(
   label='Onvoldoende, voldoende, goed of uitstekend, per rubriekcriterium',
   waarom='Jullie rubriek onderscheidt zelf al niveaus, een vinkje zou dat weggooien. '
          'Let op: Eduface kent ook uitstekend, jullie rubriek stopt bij goed.'),
}

def _optie(modus):
    m = MODUS[modus]
    r = f'<div class="grow"><span class="gk">Beoordelingsoptie</span><span class="gv"><b>{m["label"]}</b></span></div>'
    if m['waarom']:
        r += f'\n    <div class="grow"><span class="gk">Waarom deze</span><span class="gv">{m["waarom"]}</span></div>'
    return f'<div class="gap" style="border-left-color:var(--pale);margin-top:10px">\n    {r}\n  </div>'

def _formulier(criteria):
    """criteria: lijst met namen (voorgedrukt) of een getal (schrijfregels)."""
    f = open('blad.html').read()
    fb = f.split('<body>', 1)[1].replace('</body></html>', '').split('<div class="foot">')[0]
    fb = re.sub(r'<div class="top">.*?<div class="rule"></div>', HDR, fb, flags=re.S)
    fb = fb.replace('<div class="sub">Breederode Hogeschool &times; Eduface &middot; woensdag 23 september 2026 &middot; Posthumalaan 120, Rotterdam</div>',
                    '<div class="sub">Voor een van de andere opdrachten</div>')
    fb = fb.replace('<h1>Beoordelingsformulier testochtend</h1>', '<h1>Beoordelingsformulier</h1>')
    fb = re.sub(r'<div class="idrow"><span class="lbl">Ik werk bij</span>.*?</span></div>\s*(?=<div class="idrow"><span class="lbl">Dit blad gaat over)', '', fb, flags=re.S)

    # het aantal criteria verschilt per vak, dus de rijen komen uit de rubriek
    vakjes = ('<td class="c"><span class="box"></span></td>' * 3
              + '<td class="c" style="width:52px"><span class="box"></span></td>' * 2)
    if isinstance(criteria, int):
        rijen = ''.join(f'<tr><td class="q"><span class="qn">{i}</span><span class="cw"></span></td>{vakjes}</tr>\n    '
                        for i in range(1, criteria + 1))
    else:
        rijen = ''.join(f'<tr><td class="q"><span class="qn">{i}</span> {n}</td>{vakjes}</tr>\n    '
                        for i, n in enumerate(criteria, 1))
    fb = re.sub(r'(<th style="width:52px">oordeel<br>klopt niet</th></tr>\s*).*?(\s*</table>)',
                lambda m: m.group(1) + rijen.rstrip() + m.group(2), fb, flags=re.S)
    return fb

def bouw(vak, modus, dossiers, uit, formulieren=2, criteria=8):
    blokken, head = [], None
    for d in dossiers:
        t = open(d).read()
        head = head or t.split('<body>')[0] + '<body>'
        body = t.split('<body>', 1)[1].replace('</body></html>', '')
        blokken += [p for p in body.split('<div class="page">') if p.strip()]

    TOTAAL = len(blokken) + formulieren
    voet = lambda n: (f'<div class="pg"><span>Eduface testdag &middot; {vak}</span>'
                      f'<span>pagina {n} van {TOTAAL}</span></div>')

    uitv = []
    for i, p in enumerate(blokken, start=1):
        p = re.sub(r'<div class="pg">.*?</div>\s*$', voet(i), p, flags=re.S)
        if i == 1:   # de beoordelingsoptie hoort op het eerste blad
            p = p.replace('</div>\n\n<div class="sec">', '</div>\n' + _optie(modus) + '\n\n<div class="sec">', 1)
        uitv.append('<div class="page">' + p.rstrip() + '\n</div>')

    fb = _formulier(criteria)
    for n in range(len(blokken) + 1, TOTAAL + 1):
        uitv.append('<div class="page">' + fb.rstrip() + '\n' + voet(n) + '\n</div>')

    open(uit, 'w').write(head + '\n'.join(uitv) + '</body></html>')
    return TOTAAL

if __name__ == '__main__':
    n = bouw('Master Manuele Therapie', 'voldaan', ['dossier-mt.html'], 'map-mt.html')
    print('map-mt.html:', n, 'bladen')
