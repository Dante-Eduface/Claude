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
  {todo("De € 37.000 is uitgerekend met een model. Tot de EB-meeting hebben we wat meer tijd, dus kunnen we nauwkeuriger in kaart brengen hoeveel Eduface bespaart. Voorstel: samen met de controller bekijken wat het nakijken nu intern en extern kost. Die cijfers vervangen dan de bedragen hierboven.")}
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
  {todo("Tijdens de meeting vroegen we wat de uitdaging is. Je antwoord was: feedback voor iedereen. Dat is nog te weinig om de huidige uitdaging goed in kaart te brengen. Wat hierboven staat komt uit onze eerste meeting. Kun je het aanvullen? Dan komt het hier te staan.")}
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
def route(titel, stappen):
    """Eén manier van beoordelen: titel links, iconen met pijlen rechts."""
    cel = ARROW.join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:1mm;text-align:center">{icon(i)}<span class="small" style="color:var(--accent);font-weight:600;font-size:8pt;line-height:1.2">{t}</span></div>' for i, t in stappen)
    return f'<div class="panel" style="margin-top:2mm;padding:2.5mm 4mm;display:grid;grid-template-columns:40mm 1fr;gap:3mm;align-items:center"><div class="strong" style="font-size:10pt">{titel}</div><div style="display:flex;align-items:flex-start;gap:1mm">{cel}</div></div>'
page(MAP, '5-kwaliteit', f'''
<h1>Kwaliteit</h1>
<div class="stack tight">
  <section class="card primary" style="padding:7mm 9mm">{ttl("scale","Beoordelaars oordelen consistent: zie wie afwijkt van het team")}
    <div class="panel" style="margin-top:4mm">
      <div class="small" style="display:flex;justify-content:space-between"><span>Voorbeeld per docent</span><span>Gemiddelde 7,1</span></div>
      <div class="hbars">{hbar("Docent A",72,"7,2",avg=71)}{hbar("Docent B",70,"7,0",avg=71)}{hbar("Docent C",56,"5,6",on=True,avg=71)}</div>
    </div>
  </section>
  <section class="card secondary" style="padding:7mm 9mm">{ttl("flow","Zo loopt een opdracht")}
    <p class="desc">Per opdracht kiest de instelling een van drie routes.</p>
    {route("Direct naar de student", [("upload","Inleveren"),("spark","Eduface"),("grad","Student")])}
    {route("Tweeogenprincipe: een docent ertussen", [("upload","Inleveren"),("spark","Eduface"),("edit","Docent"),("grad","Student")])}
    {route("Vierogenprincipe: standaard bij de thesis", [("upload","Inleveren"),("spark","Eduface"),("edit","Beoordelaar 1"),("edit","Beoordelaar 2"),("grad","Student")])}
    <div class="strong" style="margin-top:4mm">Zo werkt het vierogenprincipe in Eduface</div>
    <div class="duo" style="gap:0 6mm">{lst(["Twee of drie beoordelaars kijken los van elkaar na.","Externe beoordelaars zien alleen hun opdrachten."])}{lst(["De moduleleider ziet wie wat beoordeelt en leest mee.","De moduleleider kiest of eerdere feedback zichtbaar is."])}</div>
    <p class="small" style="margin-top:1mm">Verschillende instellingen gebruiken Eduface op deze manier.</p>
  </section>
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
menu = ''.join(f'<div style="display:flex;align-items:center;gap:3mm;padding:2.2mm 3mm;border-radius:2mm;font-size:9pt;{"background:#f3f3f5;color:#b0532f;font-weight:600" if k=="Resources" else "color:#3a3d4a"}">{I(d,"4mm")}<span>{k}</span></div>' for k, d in NI.items())
rail = ''.join(f'<div style="display:grid;place-items:center;width:9mm;height:9mm;border-radius:50%;margin-top:2.6mm;{"background:#fff;color:#b0532f" if i==1 else "color:#c9cbd6"}">{I(d,"4mm")}</div>' for i, d in enumerate(RAIL + RAIL[:1]))
btn = lambda t: f'<span style="display:inline-block;padding:1.6mm 4mm;border-radius:99px;background:#f3f3f5;font-size:8pt;font-weight:600;color:#3a3d4a">{t}</span>'
act = lambda t: f'<span style="font-size:8pt;font-weight:600;color:#3a3d4a">{t}</span>'
box = '<span style="display:inline-block;width:3mm;height:3mm;border:0.3mm solid #c9cbd6;border-radius:0.6mm"></span>'
neo = f'''<div style="display:grid;grid-template-columns:15mm 1fr;border-radius:4mm;overflow:hidden;background:#f5f5f7;border:0.3mm solid var(--blue-200)">
  <div style="background:#1c1f2b;display:flex;flex-direction:column;align-items:center;padding:3mm 0">
    <img src="{LOGOS}/Academica-beeldmerk.png" style="width:11mm;height:11mm">{rail}
  </div>
  <div>
    <div style="padding:5mm 6mm 3mm;font-size:13pt;font-weight:700;color:#1c1f2b">Test met Teststudent | 1MILE2301A1</div>
    <div style="display:grid;grid-template-columns:42mm 1fr">
      <div style="background:#fff;border-radius:0 4mm 0 0;padding:4mm 3mm">{menu}</div>
      <div style="padding:2mm 6mm 6mm">
        <div style="font-size:12pt;font-weight:700;color:#1c1f2b">Resources</div>
        <div style="margin-top:3mm;font-size:8pt;line-height:1.45;color:#555a66">Use this area to share resources with your students, such as general information, videos or documents. You can reuse existing resources from our library or contribute your own.</div>
        <div style="margin-top:4mm;background:#fff;border-radius:2.5mm;padding:4mm">
          <div style="display:flex;gap:2.5mm">{btn("− Remove")}{btn("Export")}</div>
          <div style="margin-top:4mm;padding:2mm 3mm;background:#f5f5f7;border-radius:1.5mm;display:flex;align-items:center;gap:3mm;font-size:8pt;font-weight:600;color:#3a3d4a">{box}<span>Resource</span></div>
          <div style="margin-top:3mm;padding:0 3mm;display:flex;align-items:center;gap:3mm;font-size:9pt;color:#4a7fd4">{box}{I('<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L4 17l3 3 5.3-5.3a4 4 0 0 0 5.4-5.4l-2.4 2.4-2.6-.4-.4-2.6z"/>',"3.6mm")}<span>Eduface</span></div>
        </div>
        <div style="margin-top:4mm;background:#fff;border-radius:2.5mm;padding:4mm">
          <div style="font-size:11pt;font-weight:700;color:#1c1f2b">Eduface</div>
          <div style="margin-top:1.5mm;font-size:9pt;color:#4a7fd4">Eduface</div>
          <div style="margin-top:3.5mm;display:flex;gap:5mm;flex-wrap:wrap">{act("Details")}{act("Show content")}{act("Edit display properties")}{act("Edit redirect URI")}</div>
        </div>
      </div>
    </div>
  </div>
</div>'''
page(MAP, '6-integratie', f'''
<h1>Integratie</h1>
<div class="stack tight">
  <div>{neo}<p class="small" style="margin-top:2.5mm;color:rgba(255,255,255,0.8)">Eduface staat als tool in de cursus in NEO LMS.</p></div>
  <section class="card secondary" style="padding:6mm 8mm"><h2>Voordelen</h2>{lst(["Studenten leveren in zoals altijd, in NEO.","Cijfers en feedback komen automatisch terug in NEO."])}</section>
  {risk("Koppeling met NEO valt uit", ["Eduface krijgt automatisch een melding en zet de koppeling zo snel mogelijk weer live."], "Laag")}
</div>''')

# 07 Ervaring: rapport testfase lerarenopleiding (docenten) en casestudy BDK (studenten), Hogeschool Rotterdam
def docent(rol, cijfer, tijd, quote):
    return f'''<div class="panel" style="margin-top:0"><div class="small" style="font-weight:600;color:var(--accent)">{rol}</div>
<div style="display:flex;align-items:baseline;gap:2mm;margin-top:2mm"><span class="num" style="font-size:28pt">{cijfer}</span><span class="small">gebruiksvriendelijkheid</span></div>
<p class="desc" style="margin-top:2mm">{tijd}</p><p class="desc" style="color:var(--accent);font-style:italic">{quote}</p></div>'''
page(MAP, '7-ervaring', f'''
<h1>Ervaring</h1>
<div class="stack tight">
  <section class="card primary">{ttl("grad","Wat docenten ervan vinden")}
    <p class="desc">Hogeschool Rotterdam, bachelor- en masterlerarenopleiding.</p>
    <div class="duo" style="margin-top:5mm">
      {docent("Docent bachelor", "9", "Nu 20 tot 30 minuten per student. Met Eduface minder, met behoud of verbetering van de kwaliteit.", "“De workflow sluit goed aan bij hoe wij lesgeven en beoordelen.”")}
      {docent("Docent master", "8", "Nu ongeveer 45 minuten per student. Met Eduface zo'n 15 minuten, met een eindcontrole door de docent.", "“De tool vraagt de student om te concretiseren en te onderbouwen.”")}
    </div>
    <p class="small" style="margin-top:3mm">Volgens beide docenten: meer consistente feedback tussen docenten en meer inhoudelijke feedforward.</p>
  </section>
  <section class="card secondary">{ttl("chat","Wat studenten ervan vinden")}
    <p class="desc">Hogeschool Rotterdam, Bedrijfskunde. Wat studenten het meest waardeerden:</p>
    <div class="duo" style="margin-top:1mm;gap:0 6mm">{lst(["Controle op bronvermelding (APA)","Waar kernpunten onvoldoende onderbouwd zijn","Samenhang tussen de onderdelen"])}{lst(["Suggesties om modellen te verbeteren","Een denkimpuls, geen kant-en-klaar antwoord","Opmerkingen direct in de tekst"])}</div>
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
+ risk('Onjuiste of eenzijdige feedback', ['Docent is eindverantwoordelijk en past alles aan.', 'Tweede beoordeling of moderatie waar nodig.'], 'Laag')
+ risk('Gebruik voor andere doelen', ['Opdrachten worden niet gebruikt voor training.', 'Geen verzameling van inzendingen.'], 'Laag')
+ risk('Verwerking buiten de EU', ['Alle opslag en verwerking binnen Europa.'], 'Laag')
+ risk('Datalek of onvoldoende beveiliging', ['Versleuteld opgeslagen en verzonden, in de EU.', 'Beveiligingscheck door eigen IT vooraf.'], 'Laag')
+ risk('Koppeling met NEO valt uit', ['Eduface krijgt automatisch een melding en zet de koppeling zo snel mogelijk weer live.'], 'Laag')
+ risk('Nieuwe AI-wetgeving', ['AI Act: hoog risico, verplichtingen vanaf eind 2027.', 'AI-geletterdheid docenten, verplicht sinds feb. 2025.'], 'Laag tot middel', 'secondary')
+ '\n</div>')

# 11 Vervolgstappen: leeg tot het go-live-plan er is
page(MAP, '11-vervolgstappen', f'''
<h1>Vervolgstappen</h1>
{todo("Hier komen onderdelen uit het go-live-plan. Die staan in de definitieve businesscase.", "Volgt")}
''')
