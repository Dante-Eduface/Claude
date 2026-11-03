"""Businesscase Academica, versie na feedback Marjolein (03-11-2026). Elf pagina's.

Gebruik: python3 academica.py <werkmap>
"""
import sys
sys.path.insert(0, '/home/user/Claude/.claude/skills/business-case-design/motor')
from bouwstenen import *

MAP = sys.argv[1]

# 01 Voorstel (ongewijzigd)
page(MAP, '1-voorstel', f'''
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

# 02 Uitdaging (nieuw): het nakijkprobleem, met theorie en praktijk als blikvanger
venn = '''<div style="position:relative;height:48mm;margin-top:6mm">
  <span style="position:absolute;left:calc(50% - 52mm);top:0;width:48mm;height:48mm;border-radius:50%;border:0.6mm solid var(--accent);background:#fff"></span>
  <span style="position:absolute;left:calc(50% - 22mm);top:0;width:48mm;height:48mm;border-radius:50%;border:0.6mm solid var(--accent);background:transparent"></span>
  <span class="strong" style="position:absolute;left:calc(50% - 50mm);top:21mm;width:26mm;text-align:center">Theorie</span>
  <span class="strong" style="position:absolute;left:calc(50% + 0mm);top:21mm;width:26mm;text-align:center">Praktijk</span>
  <span class="strong" style="position:absolute;left:calc(50% - 22mm);top:18.5mm;width:18mm;text-align:center;font-size:9pt">De</span>
  <span class="strong" style="position:absolute;left:calc(50% - 22mm);top:23mm;width:18mm;text-align:center;font-size:9pt">nakijker</span>
</div>'''
page(MAP, '2-uitdaging', f'''
<h1>Uitdaging</h1>
<div class="stack">
  <section class="card primary">{ttl("grad","Praktijkgerichte papers vragen gespecialiseerde nakijkers")}
    <p class="desc">Applied science beoordelen vraagt kennis van de theorie én van de praktijk. Die combinatie is schaars.</p>
    {venn}
  </section>
  <section class="card secondary">{ttl("clock","Inwerken kost tijd en geld")}
    <p class="desc">Nieuwe nakijkers trainen duurt lang, en de uren lopen op.</p>
  </section>
  <p class="note" style="margin-top:10mm">Met Eduface kan de doorlooptijd van feedback en beoordeling mogelijk aanzienlijk korter worden.</p>
</div>''')

# 03 Kosten (ongewijzigd)
page(MAP, '3-kosten', f'''
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

# 04 Opbrengst (NEO heeft nu een eigen pagina)
page(MAP, '4-opbrengst', f'''
<h1>Opbrengst</h1>
<div class="stack">
  <section class="card primary">{ttl("scale","Uniforme beoordeling")}
    <p class="desc">Elke opdracht wordt langs dezelfde criteria beoordeeld, door elke beoordelaar.</p>
    <div class="duo" style="margin-top:6mm">{lens("Zonder","Elke beoordelaar met een eigen blik",[14,42,63,88],False)}{lens("Met Eduface","Iedereen langs dezelfde criteria",[44,50,56,62],True)}</div>
  </section>
  <section class="card secondary">{ttl("chat","Formatieve feedback voor elke student")}
    <p class="desc">Nu krijgt de helft van de studenten formatieve feedback. Met Eduface is dat iedereen.</p>
  </section>
  <section class="card tertiary">{ttl("link","Werkt binnen NEO LMS")}
    <p class="desc">Opdrachten en cijfers lopen via NEO. Docenten en studenten werken in de omgeving die ze kennen.</p>
  </section>
</div>''')

# 05 Kwaliteit (was Accreditatie): dashboard als productbeeld, vier en twee ogen
page(MAP, '5-kwaliteit', f'''
<h1>Kwaliteit</h1>
<div class="stack">
  <section class="card primary">{ttl("scale","Beoordelaars oordelen consistent")}
    <p class="desc">Zie in één overzicht wie afwijkt van het team.</p>
    {placeholder(["Productbeeld volgt", "Dashboard: beoordelaars vergelijken"], 30)}
  </section>
  <section class="card secondary">{ttl("eye","Vier ogen en twee ogen")}
    <div class="small" style="margin-top:4mm;font-weight:600;color:var(--accent)">Thesis, vier ogen</div>
    {flow([(None,"Eduface doet een voorstel"),(None,"Beoordelaar 1"),(None,"Beoordelaar 2")], compact=True)}
    <div class="small" style="margin-top:3mm;font-weight:600;color:var(--accent)">Tussenopdracht, twee ogen</div>
    {flow([(None,"Eduface doet een voorstel"),(None,"Docent"),(None,"Tweede beoordelaar alleen als het nodig is")], compact=True)}
  </section>
  <section class="card tertiary">{ttl("doc","Elk cijfer is navolgbaar")}
    <p class="desc">Onderbouwing per rubriccriterium.</p>
  </section>
  <p class="note" style="margin-top:6mm">Consistent beoordelen is een speerpunt van dit project. Daarmee helpt het om de eisen van de accreditatiepartij steviger te borgen, en dat kan een positieve impact hebben op de pabo, die nu in de accreditatie zit.</p>
</div>''')

# 06 Integratie (nieuw)
page(MAP, '6-integratie', f'''
<h1>Integratie</h1>
<p class="lead">Eduface werkt binnen NEO LMS. Studenten en docenten blijven in de omgeving die ze kennen.</p>
<div class="stack">
  <section class="card primary">{ttl("link","Zo loopt een opdracht")}
    {flow([("upload","Student levert in via NEO"),("spark","Eduface maakt feedback en een cijfervoorstel"),("edit","Docent bekijkt en past aan"),("return","Cijfer en feedback terug in NEO")])}
    <p class="small" style="margin-top:4mm">Feedback kan ook direct naar de student, zonder tussenstap van de docent. Die keuze maakt de instelling zelf.</p>
  </section>
  <div class="duo">
    <section class="card secondary"><h2>Voordelen</h2>{lst(["Studenten leveren in zoals altijd.","Docenten hebben geen extra omgeving nodig.","Cijfers en feedback komen automatisch terug in NEO."])}</section>
    <section class="card tertiary"><h2>Als de koppeling uitvalt</h2>{lst(["Eduface krijgt automatisch een melding.","Opgelost volgens de SLA, met als streven binnen 48 uur."])}</section>
  </div>
  <p class="small" style="margin-top:4mm">De koppeling is gebouwd op LTI, de standaard voor koppelingen met een LMS, en is live. Een koppeling via de API is in ontwikkeling.</p>
</div>''')

# 07 Ervaring (placeholder tot de casestudy er is)
page(MAP, '7-ervaring', f'''
<h1>Ervaring</h1>
<div class="stack">
  <section class="card primary">{ttl("grad","Hogeschool Rotterdam, lerarenopleiding")}
    <p class="desc">Hoe de lerarenopleiding met Eduface werkt en wat docenten ervan vinden.</p>
    {placeholder("Casestudy volgt", 60)}
  </section>
  <section class="card secondary">{ttl("users","Wat andere instellingen waarderen")}
    <p class="desc">De inhoudelijke ervaring van Universiteit Leiden en de Radboud Universiteit.</p>
    {placeholder("Volgt", 30)}
  </section>
</div>''')

# 08 Koersplan (ongewijzigd)
page(MAP, '8-koersplan', f'''
<h1>Koersplan</h1>
<p class="lead">Deze investering sluit naadloos aan op het kopje Efficiëntie uit het koersplan dat Academica voor de komende jaren heeft opgesteld. Binnen dat kopje versterkt het direct drie punten.</p>
<div class="stack">
  <section class="card primary"><div class="label">Koersplan Academica</div><h2 style="margin-top:2mm">Efficiëntie</h2>
    <div style="margin-top:2mm">{item("users","Een stevig kernteam")}{item("flow","Betere processen")}{item("chart","Datagedreven")}</div>
  </section>
</div>''')

# 09 Privacy (ongewijzigd)
page(MAP, '9-privacy', f'''
<h1>Privacy</h1>
<div class="stack">
  <section class="card primary">{ttl("shield","Academica blijft eigenaar van al het studentenwerk en alle data.")}</section>
  <section class="card tertiary">{ttl("lock","Gebruik van de data")}{lst(["Studentenwerk wordt nooit gebruikt om AI-modellen te trainen.","Verwerking alleen voor het afgesproken onderwijsdoel, in opdracht van Academica."])}</section>
  <section class="card tertiary">{ttl("globe","Waar de data staat")}{lst(["Data alleen in de EU, ook bij Microsoft, Google en Railway.","Eigen model, geen koppeling met een extern AI-model."])}</section>
  <section class="card tertiary">{ttl("scale","Wet en regie")}{lst(["AVG: verwerkersovereenkomst, een datalek binnen 48 uur gemeld.","AI Act: audit trail voor elke summatieve beoordeling.","De docent beslist, de AI assisteert."])}</section>
</div>''')

# 10 Risicoanalyse (plus de koppeling met NEO)
page(MAP, '10-risicoanalyse', f'''
<h1>Risicoanalyse</h1>
<div class="stack" style="margin-top:5mm">
''' + risk('Persoonsgegevens in opdrachten', ['Verwerkersovereenkomst over persoonsgegevens.'], 'Laag')
+ risk('Onjuiste of eenzijdige feedback', ['Docent is eindverantwoordelijk en past alles aan.', 'Training voor docenten in het werken met Eduface.', 'Tweede beoordeling of moderatie waar nodig.'], 'Laag')
+ risk('Gebruik voor andere doelen', ['Opdrachten worden niet gebruikt voor training.', 'Geen verzameling van inzendingen.'], 'Laag')
+ risk('Verwerking buiten de EU', ['Alle opslag en verwerking binnen de EER.', 'Geen doorgifte naar landen buiten de EER.'], 'Laag')
+ risk('Datalek of onvoldoende beveiliging', ['Versleuteld opgeslagen en verzonden, in de EU.', 'Beveiligingscheck door eigen IT vooraf.'], 'Laag')
+ risk('Koppeling met NEO valt uit', ['Eduface krijgt automatisch een melding.', 'Opgelost volgens de SLA, streven binnen 48 uur.'], 'Laag')
+ risk('Nieuwe AI-wetgeving', ['AI Act: hoog risico, verplichtingen vanaf eind 2027.', 'AI-geletterdheid docenten, verplicht sinds feb. 2025.'], 'Laag tot middel', 'secondary')
+ '\n</div>')

# 11 Vervolgstappen: voorstel, wordt aangevuld met het go-live-plan
def fase(k, titel, punten, soort='tertiary'):
    return f'<section class="card {soort}" style="padding:6mm 9mm">{ttl(k, titel)}{lst(punten)}</section>'
page(MAP, '11-vervolgstappen', f'''
<h1>Vervolgstappen</h1>
<p class="lead">Een voorstel voor de start. Het go-live-plan vult dit verder in.</p>
<div class="stack" style="margin-top:6mm">
  {fase("grad","Inrichten en trainen",["Startsessie per docent: opdracht en rubric inrichten, feedback lezen en aanpassen.","Docenten openen Eduface vanuit NEO, een vast aanspreekpunt bij Eduface."],"primary")}
  {fase("flag","Testen",["Een kleine groep docenten, een of twee modules, met echte tussenopdrachten."])}
  {fase("chart","Meten of het werkt",["Vooraf vastleggen wat goed is: tijd per beoordeling, spreiding tussen beoordelaars, oordeel van docenten.","Evaluatie na de testperiode, samen met de opleidingscoördinator."])}
  {fase("eye","Grip voor de opleidingscoördinator",["Per opleiding zien wat er beoordeeld is en welke beoordelaar afwijkt.","Een vast evaluatiemoment met Eduface."],"secondary")}
</div>''')
