"""Eén bron voor het Windesheim-deck.

Elke slide is een lijst elementen op een raster van 1920x1080 px. Twee renderers:
render_pptx  -> bewerkbare pptx (echte tekstvakken en vormen, Canva-proof)
render_html  -> HTML per slide, voor de PNG-preview via headless Chrome
Zo kunnen preview en pptx niet uit elkaar lopen.
"""
import html as H, os, subprocess

PX = 6350                     # EMU per ontwerp-pixel op 13,333 inch breed
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

NAVY, AMBER, GREEN_DEEP = '002333', 'E07B00', '007B54'
GREEN, TINT_A, TINT_G = '00E075', 'FDF0DF', 'E2FBEF'
INK50, INK100, INK200, INK500 = 'F3F7F8', 'E7EEF0', 'CDD9DE', '5B7480'
WHITE = 'FFFFFF'
HEAD, BODY = 'League Spartan', 'Inter'

# ---------------------------------------------------------------- elementen
def rect(x, y, w, h, fill, r=0):        return dict(k='rect', x=x, y=y, w=w, h=h, fill=fill, r=r)
def oval(x, y, d, fill, line, lw):      return dict(k='oval', x=x, y=y, w=d, h=d, fill=fill, line=line, lw=lw)
def pic(path, x, y, w, h):              return dict(k='pic', p=path, x=x, y=y, w=w, h=h)
def text(x, y, w, h, t, *, font=BODY, size=32, bold=False, color=NAVY,
         align='center', ls=1.15):
    return dict(k='text', x=x, y=y, w=w, h=h, t=t, font=font, size=size,
                bold=bold, color=color, align=align, ls=ls)

# ---------------------------------------------------------------- bouwstenen
COLW, GAP, M = 366, 72, 120

def cols(n):
    """x-middens voor n gelijke kolommen binnen de marges."""
    w = (1920 - 2 * M - (n - 1) * GAP) / n
    return [M + i * (w + GAP) + w / 2 for i in range(n)], w

def title(t, dark=False):
    return [text(M, 88, 1920 - 2 * M, 120, t, font=HEAD, size=96, bold=True,
                 color=WHITE if dark else NAVY, ls=1.0)]

def tile(cx, cy, icon, tone='amber', size=148):
    fill = {'amber': TINT_A, 'green': TINT_G, 'navy': INK50}[tone]
    ic = size // 2
    return [rect(cx - size / 2, cy, size, size, fill, r=size * 0.243),
            pic(f'assets/icon-{icon}-{tone}.png', cx - ic / 2, cy + (size - ic) / 2, ic, ic)]

def foot(quote=None, src=None, dark=False, page=None):
    out = [rect(M, 868, 1920 - 2 * M, 1, 'FFFFFF33' if dark else INK100)]
    if quote:
        out.append(text(M, 892, 1320, 56, quote, size=38,
                        color=WHITE if dark else NAVY, align='left', ls=1.3))
    if src:
        out.append(text(M, 950 if quote else 900, 1320, 70, src, size=23,
                        color='8FA9B4' if dark else INK500, align='left', ls=1.3))
    # Op navy krijgen de logo's een wit vlak: het Windesheim-logo heeft donkere
    # letters en verdwijnt anders in de achtergrond.
    dx = 1409 if dark else 1419
    if dark:
        out.append(rect(1400, 886, 400, 88, WHITE, r=22))
    out += [pic('logo_navy.png', dx, 907, 170, 46),
            rect(dx + 210, 904, 1, 52, INK200),
            pic('assets/windesheim.png', dx + 251, 900, 130, 60)]
    if page:
        out.append(text(1700, 1004, 100, 36, str(page),
                        size=23, color='FFFFFF59' if dark else INK200, align='right'))
    return out

# ---------------------------------------------------------------- renderers
def render_pptx(slides, path):
    from pptx import Presentation
    from pptx.util import Emu, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import PP_ALIGN

    E = lambda px: Emu(int(round(px * PX)))
    P = lambda px: Pt(px / 2)
    C = lambda hx: RGBColor.from_string(hx[:6])
    ALIGN = {'center': PP_ALIGN.CENTER, 'left': PP_ALIGN.LEFT, 'right': PP_ALIGN.RIGHT}

    prs = Presentation()
    prs.slide_width, prs.slide_height = E(1920), E(1080)

    for els in slides:
        s = prs.slides.add_slide(prs.slide_layouts[6])
        for el in els:
            k = el['k']
            if k in ('rect', 'oval'):
                shp = MSO_SHAPE.OVAL if k == 'oval' else (
                    MSO_SHAPE.ROUNDED_RECTANGLE if el.get('r') else MSO_SHAPE.RECTANGLE)
                sh = s.shapes.add_shape(shp, E(el['x']), E(el['y']), E(el['w']), E(el['h']))
                sh.fill.solid(); sh.fill.fore_color.rgb = C(el['fill'])
                sh.shadow.inherit = False
                if el.get('line'):
                    sh.line.color.rgb = C(el['line']); sh.line.width = P(el['lw'])
                else:
                    sh.line.fill.background()
                if el.get('r'):
                    sh.adjustments[0] = el['r'] / min(el['w'], el['h'])
            elif k == 'pic':
                s.shapes.add_picture(el['p'], E(el['x']), E(el['y']), E(el['w']), E(el['h']))
            elif k == 'text':
                tb = s.shapes.add_textbox(E(el['x']), E(el['y']), E(el['w']), E(el['h']))
                tf = tb.text_frame; tf.word_wrap = True
                tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
                for i, line in enumerate(el['t'].split('\n')):
                    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
                    p.alignment = ALIGN[el['align']]; p.line_spacing = el['ls']
                    r = p.add_run(); r.text = line
                    r.font.name = el['font']; r.font.size = P(el['size'])
                    r.font.bold = el['bold']; r.font.color.rgb = C(el['color'])
    prs.save(path)
    return path

def render_html(els, path, dark=False, prefix='../'):
    parts = []
    for el in els:
        k, st = el['k'], (f"left:{el['x']:.1f}px;top:{el['y']:.1f}px;"
                          f"width:{el['w']:.1f}px;height:{el['h']:.1f}px;")
        if k == 'rect':
            parts.append(f'<div style="position:absolute;{st}background:#{el["fill"]};'
                         f'border-radius:{el.get("r",0):.1f}px"></div>')
        elif k == 'oval':
            parts.append(f'<div style="position:absolute;{st}background:#{el["fill"]};'
                         f'border-radius:50%;box-shadow:0 0 0 {el["lw"]}px #{el["line"]}"></div>')
        elif k == 'pic':
            src = el['p'] if el['p'].startswith(('/', 'http')) else prefix + el['p']
            parts.append(f'<img src="{src}" style="position:absolute;{st}object-fit:contain">')
        elif k == 'text':
            parts.append(
                f'<div style="position:absolute;{st}font-family:\'{el["font"]}\',sans-serif;'
                f'font-size:{el["size"]}px;font-weight:{700 if el["bold"] else 400};'
                f'color:#{el["color"]};text-align:{el["align"]};line-height:{el["ls"]};'
                f'white-space:pre-line">{H.escape(el["t"])}</div>')
    bg = f'#{NAVY}' if dark else '#fff'
    open(path, 'w', encoding='utf-8').write(
        '<!DOCTYPE html><html lang="nl"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;600;700;800'
        '&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
        '<style>*{margin:0;padding:0;box-sizing:border-box}html,body{background:#fff}'
        f'.slide{{position:relative;width:1920px;height:1080px;overflow:hidden;background:{bg}}}'
        '</style></head><body><div class="slide">' + ''.join(parts) + '</div></body></html>')
    return path

def shoot(html_path, png_path):
    subprocess.run([CHROME, '--headless', '--disable-gpu', f'--screenshot={png_path}',
                    '--window-size=1920,1080', '--hide-scrollbars',
                    '--virtual-time-budget=4000', html_path],
                   capture_output=True)
    return png_path
