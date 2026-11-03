"""Businesscase Academica, versie na feedback Marjolein (03-11-2026). Elf pagina's.

Gebruik: python3 academica.py <werkmap>
"""
import sys
sys.path.insert(0, '/home/user/Claude/.claude/skills/business-case-design/motor')
from bouwstenen import *

MAP = sys.argv[1]
LOGOS = "/home/user/Claude/Design/Merk/logo-van-scholen/Logo's/NL scholen"
EDUFACE = "/home/user/Claude/Design/Merk/logos/logo_navy.png"

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
  {todo("De € 37.000 vragen we na bij de controller: wat kost het nakijken nu, intern en extern?")}
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
  <p class="note" style="margin-top:10mm">De huidige doorlooptijd is 1 week voor formatieve feedback op conceptstukken en 4 weken voor een summatieve beoordeling. Met Eduface kan die mogelijk aanzienlijk korter worden.</p>
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
    <div class="panel">
      <div class="small" style="display:flex;justify-content:space-between"><span>Voorbeeld per docent</span><span>Gemiddelde 7,1</span></div>
      <div class="hbars">{hbar("Docent A",72,"7,2",avg=71)}{hbar("Docent B",70,"7,0",avg=71)}{hbar("Docent C",56,"5,6",on=True,avg=71)}</div>
    </div>
  </section>
  <section class="card secondary">{ttl("eye","Thesis: ervaring met het vierogenprincipe")}
    {flow([(None,"Eduface doet een voorstel"),(None,"Beoordelaar 1"),(None,"Beoordelaar 2")], compact=True)}
    {todo("Hier komt onze ervaring met het vierogenprincipe bij andere instellingen. Volgt van Eduface.", "Volgt")}
  </section>
  <section class="card tertiary">{ttl("doc","Elk cijfer is navolgbaar")}
    <p class="desc">Onderbouwing per rubriccriterium.</p>
  </section>
  <p class="note" style="margin-top:6mm">Consistent beoordelen is een speerpunt van dit project. Daarmee helpt het om de eisen van de accreditatiepartij steviger te borgen, en dat kan een positieve impact hebben op de pabo, die nu in de accreditatie zit.</p>
</div>''')

# 06 Integratie
I = lambda d, size='3.2mm': f'<svg viewBox="0 0 24 24" style="width:{size};height:{size}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
NI = {  # menu-iconen in NEO
 'Lessons':'<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6"/>',
 'News':'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 9h6M7 13h10"/>',
 'Calendar':'<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
 'Assignments':'<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/>',
 'Gradebook':'<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 4v16"/>',
 'Mastery':'<path d="M4 20h16M7 16v-4M12 16V8M17 16v-7"/>',
 'Resources':'<path d="M4 4h4v16H4zM10 4h4v16h-4z"/><path d="m16 5 4 1-3 14-4-1"/>',
 'Students':'<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 'Teachers':'<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
}
RAIL = ['<path d="M3 11 12 4l9 7v9H3z"/>','<path d="M4 9h16v11H4zM8 9V5h8v4"/>','<path d="M5 4h4v16H5zM11 4h4v16h-4z"/>','<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>','<rect x="4" y="4" width="7" height="7"/><rect x="13" y="4" width="7" height="7"/><rect x="4" y="13" width="7" height="7"/><rect x="13" y="13" width="7" height="7"/>','<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20a6 6 0 0 1 12 0M14 20a5 5 0 0 1 8 0"/>','<path d="M12 3v6M6 15v-3h12v3M4 15h4v5H4zM10 15h4v5h-4zM16 15h4v5h-4z"/>','<path d="M4 20 10 12l4 4 6-10"/>']
menu = ''.join(f'<div style="display:flex;align-items:center;gap:2mm;padding:0.5mm 2.5mm;border-radius:1.5mm;font-size:7.5pt;{"background:#f1f1f3;color:#b0532f;font-weight:600" if k=="Resources" else "color:#3a3d4a"}">{I(d)}<span>{k}</span></div>' for k, d in NI.items())
rail = ''.join(f'<div style="display:grid;place-items:center;width:7mm;height:7mm;border-radius:50%;margin-top:1mm;{"background:#fff;color:#b0532f" if i==1 else "color:#c9cbd6"}">{I(d,"3mm")}</div>' for i, d in enumerate(RAIL[:6]))
btn = lambda t: f'<span style="display:inline-block;padding:1.2mm 3mm;border-radius:99px;background:#f1f1f3;font-size:7pt;font-weight:600;color:#3a3d4a">{t}</span>'
act = lambda t: f'<span style="font-size:7pt;font-weight:600;color:#3a3d4a">{t}</span>'
neo = f'''<div style="margin-top:4mm;display:grid;grid-template-columns:11mm 36mm 1fr;border-radius:3mm;overflow:hidden;background:#f5f5f7;border:0.3mm solid var(--blue-200)">
  <div style="background:#1c1f2b;display:flex;flex-direction:column;align-items:center;padding-top:2mm">
    <img src="{LOGOS}/Academica-beeldmerk.png" style="width:8mm;height:8mm">{rail}
  </div>
  <div style="background:#fff;padding:3mm 2mm">
    <div style="font-size:9pt;font-weight:600;color:#1c1f2b;margin:0 0 2mm 1mm">Test met Teststudent</div>{menu}
  </div>
  <div style="padding:4mm 5mm">
    <div style="font-size:10pt;font-weight:600;color:#1c1f2b">Resources</div>
    <div style="margin-top:2mm;font-size:7pt;line-height:1.4;color:#555a66">Use this area to share resources with your students, such as general information, videos or documents.</div>
    <div style="margin-top:3mm;background:#fff;border-radius:2mm;padding:3mm">
      <div style="display:flex;gap:2mm">{btn("− Remove")}{btn("Export")}</div>
      <div style="margin-top:3mm;padding:1.5mm 2mm;background:#f5f5f7;border-radius:1mm;font-size:7pt;font-weight:600;color:#3a3d4a">Resource</div>
      <div style="margin-top:2mm;padding:0 2mm;display:flex;align-items:center;gap:1.5mm;font-size:7.5pt;color:#4a7fd4">{I('<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L4 17l3 3 5.3-5.3a4 4 0 0 0 5.4-5.4l-2.4 2.4-2.6-.4-.4-2.6z"/>')}<span>Eduface</span></div>
    </div>
    <div style="margin-top:3mm;background:#fff;border-radius:2mm;padding:3mm">
      <div style="font-size:9pt;font-weight:600;color:#1c1f2b">Eduface</div>
      <div style="margin-top:1mm;font-size:7.5pt;color:#4a7fd4">Eduface</div>
      <div style="margin-top:2.5mm;display:flex;gap:4mm">{act("Details")}{act("Show content")}{act("Edit display properties")}</div>
    </div>
  </div>
</div>'''
lockup = f'''<div style="display:flex;align-items:center;gap:4mm">
  <img src="{LOGOS}/Academica-beeldmerk.png" style="width:9mm;height:9mm">
  <span class="strong" style="font-size:12pt;color:var(--muted)">×</span>
  <img src="{EDUFACE}" style="width:30mm;height:8.1mm">
  <span class="small" style="margin-left:auto">Eduface staat als tool in de cursus in NEO LMS</span>
</div>'''
page(MAP, '6-integratie', f'''
<h1>Integratie</h1>
<div class="stack tight">
  <section class="card tertiary" style="background:#fff;padding:5mm 6mm">{lockup}{neo}</section>
  <section class="card primary"><h2>Zo loopt een opdracht</h2>
    {flow([(None,"Student levert in via NEO"),(None,"Eduface maakt feedback en een cijfervoorstel"),(None,"Docent bekijkt en past aan"),(None,"Cijfer en feedback terug in NEO")], compact=True)}
    <p class="small" style="margin-top:3mm">Tussenopdrachten volgen het tweeogenprincipe. Directe feedback naar de student kan ook, de instelling kiest.</p>
  </section>
  <div class="duo">
    <section class="card secondary" style="padding:7mm"><h2>Voordelen</h2>{lst(["Studenten leveren in zoals altijd.","Cijfers en feedback komen automatisch terug in NEO."])}</section>
    <section class="card tertiary" style="padding:7mm"><h2>Als de koppeling uitvalt</h2>{lst(["Eduface krijgt automatisch een melding.","Opgelost volgens de SLA, streven binnen 48 uur."])}</section>
  </div>
</div>''')

# 07 Ervaring: casestudy Hogeschool Rotterdam, Bedrijfskunde (concept, aangeleverd door Dante 03-11-2026)
page(MAP, '7-ervaring', f'''
<h1>Ervaring</h1>
<div class="stack">
  <section class="card primary">{ttl("grad","Hogeschool Rotterdam, Bedrijfskunde")}
    <p class="desc">Pilot met formatieve feedback op teamrapporten van meer dan 20 pagina's, op basis van de bestaande cursusrubric.</p>
    <div class="duo" style="margin-top:5mm">
      <div class="panel" style="margin-top:0"><div class="num">79%</div><p class="desc">van de studenten positief (57%) of neutraal (22%)</p></div>
      <div class="panel" style="margin-top:0"><div class="strong">Tweede ronde beter dan de eerste</div><p class="desc">Een scherpere rubricconfiguratie werkte direct door in de feedback.</p></div>
    </div>
  </section>
  <section class="card secondary">{ttl("chat","Wat studenten het meest waardeerden")}
    <div class="duo" style="margin-top:2mm;gap:0 6mm">{lst(["Controle op bronvermelding (APA)","Waar kernpunten onvoldoende onderbouwd zijn","Samenhang tussen de onderdelen"])}{lst(["Suggesties om modellen te verbeteren","Een denkimpuls, geen kant-en-klaar antwoord","Opmerkingen direct in de tekst"])}</div>
  </section>
  <p class="statement" style="font-size:14pt">"We moeten als opleiding blijven werken met AI in ons onderwijs. Niets doen is geen optie."</p>
  <p class="small" style="margin-top:2mm">Conclusie uit de eindevaluatie van de pilot</p>
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
+ risk('Onjuiste of eenzijdige feedback', ['Docent is eindverantwoordelijk en past alles aan.', 'Tweede beoordeling of moderatie waar nodig.'], 'Laag')
+ risk('Gebruik voor andere doelen', ['Opdrachten worden niet gebruikt voor training.', 'Geen verzameling van inzendingen.'], 'Laag')
+ risk('Verwerking buiten de EU', ['Alle opslag en verwerking binnen Europa.'], 'Laag')
+ risk('Datalek of onvoldoende beveiliging', ['Versleuteld opgeslagen en verzonden, in de EU.', 'Beveiligingscheck door eigen IT vooraf.'], 'Laag')
+ risk('Koppeling met NEO valt uit', ['Eduface krijgt automatisch een melding.', 'Opgelost volgens de SLA, streven binnen 48 uur.'], 'Laag')
+ risk('Nieuwe AI-wetgeving', ['AI Act: hoog risico, verplichtingen vanaf eind 2027.', 'AI-geletterdheid docenten, verplicht sinds feb. 2025.'], 'Laag tot middel', 'secondary')
+ '\n</div>')

# 11 Vervolgstappen: voorstel, wordt aangevuld met het go-live-plan
def fase(k, titel, punten, soort='tertiary'):
    return f'<section class="card {soort}" style="padding:5mm 9mm">{ttl(k, titel)}{lst(punten)}</section>'
page(MAP, '11-vervolgstappen', f'''
<h1>Vervolgstappen</h1>
{todo("Dit is een voorstel, het go-live-plan vult het verder in. Welke docenten en modules zijn geschikt om mee te testen, en wat is voor jullie een geslaagde test?", "Graag jullie input")}
<div class="stack" style="margin-top:6mm">
  {fase("grad","Inrichten en trainen",["Startsessie per docent: opdracht en rubric inrichten, feedback lezen en aanpassen.","Docenten openen Eduface vanuit NEO, een vast aanspreekpunt bij Eduface."],"primary")}
  {fase("flag","Testen",["Een kleine groep docenten, een of twee modules, met echte tussenopdrachten."])}
  {fase("chart","Meten of het werkt",["Vooraf vastleggen wat goed is: tijd per beoordeling, spreiding tussen beoordelaars, oordeel van docenten.","Evaluatie na de testperiode, samen met de opleidingscoördinator."])}
  {fase("eye","Grip voor de opleidingscoördinator",["Per opleiding zien wat er beoordeeld is en welke beoordelaar afwijkt.","Een vast evaluatiemoment met Eduface."],"secondary")}
</div>''')
