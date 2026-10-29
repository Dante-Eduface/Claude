"""Voorbeeld: het Academica-voorstel (oktober 2026). Kopieer dit bestand en vervang de inhoud.

Gebruik: python3 academica.py <werkmap>
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'motor'))
from bouwstenen import *

MAP = sys.argv[1]

page(MAP, '1-opening', f'''
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

page(MAP, '2-kosten', f'''
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

page(MAP, '3-instelling', f'''
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

page(MAP, '4-accreditatie', f'''
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

page(MAP, '5-koersplan', f'''
<h1>Koersplan</h1>
<p class="lead">Deze investering sluit naadloos aan op het kopje Efficiëntie uit het koersplan dat Academica voor de komende jaren heeft opgesteld. Binnen dat kopje versterkt het direct drie punten.</p>
<div class="stack">
  <section class="card primary"><div class="label">Koersplan Academica</div><h2 style="margin-top:2mm">Efficiëntie</h2>
    <div style="margin-top:2mm">{item("users","Een stevig kernteam")}{item("flow","Betere processen")}{item("chart","Datagedreven")}</div>
  </section>
</div>''')

page(MAP, '6-privacy', f'''
<h1>Privacy</h1>
<div class="stack">
  <section class="card primary">{ttl("shield","Academica blijft eigenaar van al het studentenwerk en alle data.")}</section>
  <section class="card tertiary">{ttl("lock","Gebruik van de data")}{lst(["Studentenwerk wordt nooit gebruikt om AI-modellen te trainen.","Verwerking alleen voor het afgesproken onderwijsdoel, in opdracht van Academica."])}</section>
  <section class="card tertiary">{ttl("globe","Waar de data staat")}{lst(["Data alleen in de EU, ook bij Microsoft, Google en Railway.","Eigen model, geen koppeling met een extern AI-model."])}</section>
  <section class="card tertiary">{ttl("scale","Wet en regie")}{lst(["AVG: verwerkersovereenkomst, een datalek binnen 48 uur gemeld.","AI Act: audit trail voor elke summatieve beoordeling.","De docent beslist, de AI assisteert."])}</section>
</div>''')
