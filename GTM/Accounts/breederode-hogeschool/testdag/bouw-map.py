#!/usr/bin/env python3
"""Zet een vakdossier en het standaardblad om in een genummerd mapje."""
import re, sys, json

HDR='''<div class="top">
  <div class="bdlogo"><div class="bdmark"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.7" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.2-2.9 7.4-7 9-4.1-1.6-7-4.8-7-9V6l7-3z"/><path d="M9 10h6M9 13.5h6M12 10v3.5"/></svg></div>
    <div><div class="bdname">Breederode</div><div class="bdsub">Hogeschool</div></div></div>
  <div class="edu"><img src="eduface.png"></div>
</div><div class="rule"></div>'''

MODUS = {
 'voldaan': dict(
   label='Voldaan of niet voldaan, per rubriekcriterium',
   uitleg='Het model spreekt geen cijfer uit. Per criterium zegt het voldaan of niet voldaan, net als jullie eigen formulier.',
   waarom=None),
 'descriptief': dict(
   label='Onvoldoende, voldoende, goed of uitstekend, per rubriekcriterium',
   uitleg='Het model kiest per criterium een van vier niveaus in plaats van een enkel vinkje.',
   waarom='Jullie rubriek onderscheidt zelf al kwaliteitsniveaus: waar de andere twee opleidingen alleen voldaan of niet voldaan kennen, vertaalt die van jullie punten naar onvoldoende, voldoende en goed. Een vinkje zou dat verschil weggooien. Let op het vierde niveau: Eduface kent ook uitstekend, jullie rubriek stopt bij goed.'),
}

def bouw(vak, modus, dossier, uit, extra_formulieren=2, los='De opdracht van de student'):
    d=open(dossier).read()
    head=d.split('<body>')[0]+'<body>'
    body=d.split('<body>',1)[1].replace('</body></html>','')
    dosspages=[p for p in body.split('<div class="page">') if p.strip()]
    TOTAL=1+len(dosspages)+extra_formulieren
    voet=lambda n: (f'<div class="pg"><span>Eduface testdag &middot; {vak}</span>'
                    f'<span>pagina {n} van {TOTAL}</span></div>')
    m=MODUS[modus]

    rij=lambda p,t,n,cls='': (f'<div class="tr{cls}"><div class="tp">{p}</div>'
                              f'<div><div class="tt">{t}</div><div class="tn">{n}</div></div></div>')
    laatste=1+len(dosspages)
    toc=(rij('blad 2','<b>De beoordeling naast elkaar</b>','Wat de nakijker destijds gaf en wat Eduface geeft, per rubriekcriterium, plus ruimte voor aantekeningen')
       + rij('blad 3','<b>De volledige feedback van Eduface</b>','Acht rubriekcriteria, letterlijk zoals het model ze schreef')
       + rij('blad 4','<b>Waar het uiteenloopt</b>','De plekken waar de twee beoordelingen het verst uit elkaar liggen')
       + rij('blad 5','<b>De aannames van het model</b>','Waar het model iets invult dat de rubriek openlaat, met de vraag erbij')
       + rij(f'blad {laatste+1} en {laatste+2}','<b>Beoordelingsformulier</b>, twee keer','Voor de twee andere opdrachten van vanochtend. Kruis bovenaan aan welke.')
       + rij('los',f'<b>{los}</b>','Het werk zelf, ongenummerd, zodat je het er los naast kunt leggen','  los'))

    waarom=('' if not m['waarom'] else
      f'<div class="grow"><span class="gk">Waarom deze</span><span class="gv">{m["waarom"]}</span></div>')

    voorblad='<div class="page">\n'+HDR+f'''
<h1>Eduface testdag</h1><div class="sub">{vak}</div>
<div class="sub2">woensdag 23 september 2026 &middot; Posthumalaan 120, Rotterdam</div>

<div class="ident">
  <div class="idrow"><span class="lbl">Naam</span><span class="fill"></span>
    <span class="lbl" style="margin-left:18px">Datum</span><span class="fill" style="width:110px"></span></div>
</div>

<div class="sec">
  <div class="st">De beoordelingsoptie die aanstaat</div>
  <div class="gap" style="border-left-color:var(--pale)">
    <div class="grow"><span class="gk">Gekozen</span><span class="gv"><b>{m['label']}</b></span></div>
    <div class="grow"><span class="gk">Wat dat doet</span><span class="gv">{m['uitleg']}</span></div>
    {waarom}
  </div>
</div>

<div class="sec">
  <div class="st">Wat er in dit mapje zit</div>
  <div class="sd">Alles op volgorde. De opdracht van de student zit er los bij, want die is te dik om in te binden.</div>
  <div class="toc">
{toc}
  </div>
</div>
''' + voet(1) + '\n</div>'

    uitv=[voorblad]
    for i,p in enumerate(dosspages, start=2):
        p=re.sub(r'<div class="pg">.*?</div>\s*$', voet(i), p, flags=re.S)
        uitv.append('<div class="page">'+p.rstrip()+'\n</div>')

    f=open('blad.html').read()
    fb=f.split('<body>',1)[1].replace('</body></html>','').split('<div class="foot">')[0]
    fb=re.sub(r'<div class="top">.*?<div class="rule"></div>', HDR, fb, flags=re.S)
    fb=fb.replace('<div class="sub">Breederode Hogeschool &times; Eduface &middot; woensdag 23 september 2026 &middot; Posthumalaan 120, Rotterdam</div>',
                  '<div class="sub">Voor een van de twee andere opdrachten van vanochtend</div>')
    fb=fb.replace('<h1>Beoordelingsformulier testochtend</h1>','<h1>Beoordelingsformulier</h1>')
    fb=re.sub(r'<div class="idrow"><span class="lbl">Ik werk bij</span>.*?</span></div>\s*(?=<div class="idrow"><span class="lbl">Dit blad gaat over)','',fb,flags=re.S)
    for n in range(laatste+1, TOTAL+1):
        uitv.append('<div class="page">'+fb.rstrip()+'\n'+voet(n)+'\n</div>')

    open(uit,'w').write(head+'\n'.join(uitv)+'</body></html>')
    return TOTAL

if __name__=='__main__':
    n=bouw('Master Manuele Therapie','voldaan','dossier-mt.html','map-mt.html')
    print('map-mt.html:',n,'bladen')
