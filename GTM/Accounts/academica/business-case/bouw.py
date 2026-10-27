"""Business case Academica, uniform opgebouwd.

Eén elementenlijst per pagina (A4, 1240x1754 ontwerp-px). Daaruit komen een
HTML-preview (PNG via Playwright) en een bewerkbare pptx voor Canva.
De inhoud is letterlijk overgenomen uit de Canva-versie van 27-10-2026.
"""
import html as H, json, subprocess, sys

W, HGT, M = 1240, 1754, 96
CW = W - 2 * M
EMU = 7560000 / W                     # A4-breedte in EMU per ontwerp-px
PT = 595.276 / W                      # punt per ontwerp-px

NAVY, INK700, INK500, INK200, INK100, INK50, WHITE = (
    '002333', '2C4A57', '5B7480', 'CDD9DE', 'E7EEF0', 'F3F7F8', 'FFFFFF')
SOFT = '9EABB1'                       # wit op 62% over navy
HEAD, BODY = 'League Spartan', 'Inter'
R = 20                                # één radius voor alle kaarten

# ---------------------------------------------------------------- elementen
def rect(x, y, w, h, fill, r=0):  return dict(k='rect', x=x, y=y, w=w, h=h, fill=fill, r=r)
def oval(x, y, d, fill):          return dict(k='oval', x=x, y=y, w=d, h=d, fill=fill)
def pic(p, x, y, w, h):           return dict(k='pic', p=p, x=x, y=y, w=w, h=h)
def text(x, y, w, h, t, *, font=BODY, size=21, bold=False, color=INK700,
         align='left', ls=1.45, spc=0, mid=False):
    return dict(k='text', x=x, y=y, w=w, h=h, t=t, font=font, size=size, bold=bold,
                color=color, align=align, ls=ls, spc=spc, mid=mid)

# ---------------------------------------------------------------- stijlen
def eyebrow(x, y, t, color=INK500, w=CW):
    return text(x, y, w, 22, t.upper(), size=16, bold=True, color=color, ls=1.2, spc=0.08)

def h2(y, t, h=60):
    return text(M, y, CW, h, t, font=HEAD, size=46, bold=True, color=NAVY, ls=1.1)

def icoon(x, y, naam, d=60, fill=WHITE):
    ic = d * 0.45
    return [oval(x, y, d, fill), pic(f'assets/icon-{naam}.png', x + (d - ic) / 2, y + (d - ic) / 2, ic, ic)]

def rij(y, h, naam, titel, sub=None, subw=920, regels=1):
    """Lichte kaart met icoon, titel en optionele toelichting. Zelfde opbouw op elke pagina."""
    out = [rect(M, y, CW, h, INK50, R)] + icoon(M + 28, y + (h - 60) / 2, naam)
    ty = y + (h - (30 + (38 + 27 * regels - 6 if sub else 0))) / 2
    out.append(text(M + 116, ty, 860, 30, titel, size=25, bold=True, color=NAVY, ls=1.2))
    if sub:
        out.append(text(M + 116, ty + 38, subw, 60, sub, size=19, color=INK700, ls=1.4))
    return out

def voet(n):
    return [rect(M, 1660, CW, 2, INK100),
            text(M, 1684, 900, 24, 'Business case Eduface · Academica University of Applied Sciences · concept',
                 size=16, color=INK500, ls=1.2),
            text(W - M - 100, 1684, 100, 24, str(n), size=16, bold=True, color=INK500, align='right', ls=1.2)]

def stat(y, h, label, getal, sub, donker):
    fg, lab, sb = (WHITE, SOFT, WHITE) if donker else (NAVY, INK500, INK700)
    return [rect(M, y, CW, h, NAVY if donker else INK50, R),
            eyebrow(M + 56, y + 44, label, color=lab, w=600),
            text(M + 56, y + 80, 900, 120, getal, font=HEAD, size=120, bold=True, color=fg, ls=1.0),
            text(M + 56, y + 200, 900, 30, sub, size=21, color=sb, ls=1.3)]

# ---------------------------------------------------------------- pagina 1
p1 = [pic('assets/academica.png', M, 96, 330, 64),
      eyebrow(M, 248, 'Managementsamenvatting'),
      pic('assets/eduface.png', M, 290, 236, 64),
      text(M, 392, 980, 220,
           'Eduface is een onderwijskundig AI-model, ontwikkeld met hulp van de Universiteit Leiden '
           'en de Radboud Universiteit, dat formatieve en summatieve feedback geeft op '
           'studentopdrachten. Docenten besteden daardoor minder tijd aan het formuleren van '
           'feedback, elke student krijgt formatieve feedback, en een groeiend aantal studenten vraagt '
           'niet om evenredig meer nakijkers. Dat is een concrete invulling van het koerspunt '
           'efficiëntie.', size=22, ls=1.55)]
p1 += stat(668, 262, 'Nu', '€ 37.000', 'Wat nakijken de opleiding nu kost', False)
p1 += [pic('assets/icon-down.png', W / 2 - 24, 942, 48, 48)]
p1 += stat(1002, 262, 'Met Eduface', '106%', 'Rendement op de investering', True)
p1 += [rect(M, 1346, CW, 2, INK100), rect(M, 1490, CW, 2, INK100)]
for pth, x, w, h in [('hr', 196, 236, 61), ('tilburg', 504, 228, 58), ('radboud', 804, 262, 60)]:
    p1.append(pic(f'assets/{pth}.png', x, 1419 - h / 2, w, h))
p1 += voet(1)

# ---------------------------------------------------------------- pagina 2
p2 = [eyebrow(M, 96, 'Kosten'), h2(124, 'Dit kost Eduface'),
      rect(M, 216, CW, 320, NAVY, R),
      text(M + 56, 266, 900, 150, '€ 1.500', font=HEAD, size=150, bold=True, color=WHITE, ls=1.0),
      text(M + 56, 424, 900, 40, 'per maand, vooraf betaald', size=30, color=WHITE, ls=1.2),
      text(M + 56, 466, 900, 30, '€ 18.000 per jaar, exclusief btw', size=21, color=SOFT, ls=1.3)]
half = (CW - 24) / 2
for i, (t, s) in enumerate([('Eerste 400 studenten', '€ 3,75 per student per maand, samen € 1.500'),
                            ('Elke student daarboven', '€ 3 per student per maand')]):
    x = M + i * (half + 24)
    p2 += [rect(x, 560, half, 124, INK50, R),
           text(x + 36, 588, half - 72, 30, t, size=25, bold=True, color=NAVY, ls=1.2),
           text(x + 36, 626, half - 72, 30, s, size=19, color=INK700, ls=1.4)]
p2.append(eyebrow(M, 732, 'Wat de instelling ervoor krijgt'))
p2 += rij(768, 124, 'scale', 'Uniforme beoordeling',
          'Elke opdracht wordt langs dezelfde criteria beoordeeld, door elke beoordelaar.')
p2 += rij(908, 124, 'link', 'Integratie in NEO LMS',
          'Opdrachten en cijfers lopen via NEO. Docenten en studenten werken in de omgeving die ze kennen.')
p2 += rij(1048, 124, 'feedback', 'Formatieve feedback voor elke student',
          'Nu krijgt de helft van de studenten formatieve feedback. Met Eduface is dat iedereen.', subw=560, regels=2)
p2.append(text(W - M - 360, 1084, 328, 56, '50% → 100%', font=HEAD, size=48, bold=True,
               color=NAVY, align='right', ls=1.0))
p2 += voet(2)

# ---------------------------------------------------------------- pagina 3
p3 = [eyebrow(M, 96, 'Koersplan'), h2(124, 'Efficiency en organisatie als voorwaarde'),
      text(M, 192, CW, 30, 'Op deze onderdelen van ons koersplan heeft Eduface impact.', size=21, color=INK500, ls=1.3)]
for i, (n, t) in enumerate([('monitor', 'Inzet op IT'), ('workflow', 'Betere processen'),
                            ('chart', 'Datagedreven'), ('users', 'Een stevig kernteam')]):
    p3 += rij(250 + i * 104, 92, n, t)
p3 += [eyebrow(M, 700, 'Accreditatie'),
       h2(728, 'Elke beoordeling blijft navolgbaar, de docent blijft eindverantwoordelijk', h=110)]
kw = (CW - 48) / 3
kaarten = [('file', 'Beoordeling is navolgbaar',
            'Elk cijfer heeft een onderbouwing per rubriccriterium.\nEen audit trail die voldoet aan de AI Act legt elke summatieve beoordeling vast.',
            'Blijft: de docent stelt het cijfer vast'),
           ('scale', 'Beoordelaars oordelen consistent',
            'Een overzicht toont welke beoordelaar afwijkt van het team.',
            'Blijft: kalibratie twee keer per jaar'),
           ('shield', 'De examencommissie borgt de kwaliteit',
            'Per beoordeling is de onderbouwing direct in te zien.', 'Blijft: de steekproef')]
for i, (n, t, b, pil) in enumerate(kaarten):
    x, y, pad = M + i * (kw + 24), 868, 28
    iw = kw - 2 * pad
    p3 += [rect(x, y, kw, 530, INK50, R)] + icoon(x + pad, y + pad, n)
    p3 += [eyebrow(x + pad, y + 112, 'Eis', w=iw),
           text(x + pad, y + 138, iw, 64, t, size=23, bold=True, color=NAVY, ls=1.25),
           rect(x + pad, y + 218, iw, 2, INK200),
           eyebrow(x + pad, y + 238, 'Met Eduface', w=iw),
           text(x + pad, y + 266, iw, 170, b, size=18, color=INK700, ls=1.4),
           rect(x + pad, y + 458, iw, 46, WHITE, 23),
           text(x + pad, y + 458, iw, 46, pil, size=15, bold=True, color=NAVY, align='center', ls=1.2, mid=True)]
p3 += [rect(M, 1422, CW, 104, INK50, R), rect(M, 1422, 8, 104, NAVY),
       eyebrow(M + 36, 1444, 'Waarom nu'),
       text(M + 36, 1472, CW - 72, 30,
            'Bij nieuwe accreditaties is consistent beoordelen een aandachtspunt. De Pabo zit nu in accreditatie.',
            size=19, bold=True, color=NAVY, ls=1.3)]
p3 += voet(3)

# ---------------------------------------------------------------- pagina 4
p4 = [eyebrow(M, 96, 'Privacy')]
items = ['Academica blijft eigenaar van al het studentenwerk en alle data.',
         'Studentenwerk wordt niet gebruikt om AI-modellen te trainen.',
         'Studentdata gaat niet naar externe AI-aanbieders.',
         'Verwerking alleen voor het afgesproken onderwijsdoel.',
         'Verwerkersovereenkomst afgesloten (bijlage: "Verwerkersovereenkomst Eduface", versie voor onbekostigde instellingen).']
y = 136
for i, t in enumerate(items):
    h = 96 if i == 4 else 64
    p4 += [pic('assets/icon-check.png', M, y + 18, 28, 28),
           text(M + 52, y + 16, CW - 52, h - 20, t, size=21, color=NAVY, ls=1.45)]
    y += h
    if i < 4:
        p4.append(rect(M, y, CW, 2, INK100))
p4 += [text(M, y + 12, CW, 26, 'De verwerkersovereenkomst ligt ter beoordeling bij onze AVG-functionaris.',
            size=17, color=INK500, ls=1.3),
       h2(y + 120, 'Riso anylaze comming soon')]
p4 += voet(4)

PAGES = [p1, p2, p3, p4]

# ---------------------------------------------------------------- renderers
def render_html(els, path):
    parts = []
    for e in els:
        st = f"left:{e['x']:.1f}px;top:{e['y']:.1f}px;width:{e['w']:.1f}px;height:{e['h']:.1f}px;"
        if e['k'] == 'rect':
            parts.append(f'<div style="position:absolute;{st}background:#{e["fill"]};border-radius:{e["r"]}px"></div>')
        elif e['k'] == 'oval':
            parts.append(f'<div style="position:absolute;{st}background:#{e["fill"]};border-radius:50%"></div>')
        elif e['k'] == 'pic':
            parts.append(f'<img src="../{e["p"]}" style="position:absolute;{st}object-fit:contain">')
        else:
            flex = 'display:flex;align-items:center;justify-content:center;' if e['mid'] else ''
            parts.append(f'<div style="position:absolute;{st}{flex}font-family:\'{e["font"]}\';font-size:{e["size"]}px;'
                         f'font-weight:{700 if e["bold"] else 400};color:#{e["color"]};text-align:{e["align"]};'
                         f'line-height:{e["ls"]};letter-spacing:{e["spc"]}em;white-space:pre-line">{H.escape(e["t"])}</div>')
    open(path, 'w').write(
        '<!doctype html><html><head><meta charset="utf-8"><style>'
        "@font-face{font-family:'League Spartan';font-weight:700;src:url('../../../../../Design/Merk/fonts/LeagueSpartan-Bold.ttf')}"
        f'*{{margin:0;padding:0;box-sizing:border-box}}body{{width:{W}px;height:{HGT}px;position:relative;background:#fff;overflow:hidden}}'
        '</style></head><body>' + ''.join(parts) + '</body></html>')

def render_pptx(pages, path):
    from pptx import Presentation
    from pptx.util import Emu, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
    from pptx.oxml.ns import qn
    E = lambda v: Emu(int(round(v * EMU)))
    C = RGBColor.from_string
    AL = {'left': PP_ALIGN.LEFT, 'center': PP_ALIGN.CENTER, 'right': PP_ALIGN.RIGHT}
    prs = Presentation()
    prs.slide_width, prs.slide_height = E(W), E(HGT)
    for els in pages:
        s = prs.slides.add_slide(prs.slide_layouts[6])
        for e in els:
            if e['k'] in ('rect', 'oval'):
                shp = MSO_SHAPE.OVAL if e['k'] == 'oval' else (MSO_SHAPE.ROUNDED_RECTANGLE if e['r'] else MSO_SHAPE.RECTANGLE)
                sh = s.shapes.add_shape(shp, E(e['x']), E(e['y']), E(e['w']), E(e['h']))
                sh.fill.solid(); sh.fill.fore_color.rgb = C(e['fill'])
                sh.line.fill.background(); sh.shadow.inherit = False
                st = sh._element.find(qn('p:style'))      # themastijl geeft anders een schaduw
                if st is not None: sh._element.remove(st)
                if e['k'] == 'rect' and e['r']:
                    sh.adjustments[0] = min(0.5, e['r'] / min(e['w'], e['h']))
            elif e['k'] == 'pic':
                s.shapes.add_picture(e['p'], E(e['x']), E(e['y']), E(e['w']), E(e['h']))
            else:
                tb = s.shapes.add_textbox(E(e['x']), E(e['y']), E(e['w']), E(e['h']))
                tf = tb.text_frame; tf.word_wrap = True
                tf.vertical_anchor = MSO_ANCHOR.MIDDLE if e['mid'] else MSO_ANCHOR.TOP
                tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
                for i, line in enumerate(e['t'].split('\n')):
                    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
                    p.alignment = AL[e['align']]
                    # League Spartan heeft een hoge ascent: grote cijfers zakken anders weg in de pptx
                    p.line_spacing = 0.8 if e['font'] == HEAD and e['size'] >= 100 else e['ls']
                    r = p.add_run(); r.text = line
                    r.font.name = e['font']; r.font.size = Pt(e['size'] * PT); r.font.bold = e['bold']
                    r.font.color.rgb = C(e['color'])
                    if e['spc']:
                        r._r.get_or_add_rPr().set('spc', str(int(e['spc'] * e['size'] * PT * 100)))
    prs.save(path)

if __name__ == '__main__':
    for i, els in enumerate(PAGES, 1):
        render_html(els, f'preview/pagina-{i}.html')
    render_pptx(PAGES, 'business-case-academica-bewerkbaar.pptx')
