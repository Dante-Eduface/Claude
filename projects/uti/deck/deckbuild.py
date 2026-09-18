"""Eén bron voor het UTI-deck.

Elke slide is een lijst elementen op een raster van 1920x1080 px. Twee renderers:
render_pptx  -> bewerkbare pptx (echte tekstvakken en vormen, Canva-proof)
render_html  -> HTML per slide, voor de PNG-preview via headless Chrome
Zo kunnen preview en pptx niet uit elkaar lopen.

Tokens komen uit references/design-system/core/tokens.css + slides/tokens.css:
navy/wit/navy-getinte neutralen, groen alleen als accent (nooit als lopende
tekst), League Spartan voor koppen, Inter voor de rest. Geen amber — dat
hoort bij het oudere Windesheim-palet, niet bij het huidige core-systeem.
"""
import html as H, os, subprocess

PX = 6350                     # EMU per ontwerp-pixel op 13,333 inch breed
CHROME = os.environ.get('CHROME_PATH', '/opt/pw-browsers/chromium')

# ---------------------------------------------------------------- kleuren (core/tokens.css)
NAVY = '002333'
GREEN, GREEN_DEEP = '00E075', '007B54'
INK900, INK700, INK500, INK300, INK200, INK100, INK50 = (
    '0A2C3B', '2C4A57', '5B7480', 'A9BCC4', 'CDD9DE', 'E7EEF0', 'F3F7F8')
WHITE = 'FFFFFF'
HEAD, BODY = 'League Spartan', 'Inter'

# ---------------------------------------------------------------- type-schaal (slides/tokens.css)
HERO, TITLE, SUB, TEXT, CAPTION, STAT = 132, 76, 44, 32, 24, 180

# ---------------------------------------------------------------- canvas
W, H_, M, GAP = 1920, 1080, 120, 48

# ---------------------------------------------------------------- elementen
def rect(x, y, w, h, fill, r=0):        return dict(k='rect', x=x, y=y, w=w, h=h, fill=fill, r=r)
def oval(x, y, d, fill, line=None, lw=0): return dict(k='oval', x=x, y=y, w=d, h=d, fill=fill, line=line, lw=lw)
def pic(path, x, y, w, h):              return dict(k='pic', p=path, x=x, y=y, w=w, h=h)
def text(x, y, w, h, t, *, font=BODY, size=TEXT, bold=False, color=NAVY,
         align='center', ls=1.15):
    return dict(k='text', x=x, y=y, w=w, h=h, t=t, font=font, size=size,
                bold=bold, color=color, align=align, ls=ls)

# ---------------------------------------------------------------- bouwstenen
def cols(n, gap=GAP):
    """x-middens voor n gelijke kolommen binnen de marges."""
    w = (W - 2 * M - (n - 1) * gap) / n
    return [M + i * (w + gap) + w / 2 for i in range(n)], w

def slide_title(t, dark=False, claim_size=TITLE):
    """Slidekop: een bewering, geen label. Max twee regels."""
    return [text(M, 88, W - 2 * M, claim_size * 1.3, t, font=HEAD, size=claim_size,
                 bold=True, color=WHITE if dark else NAVY, align='left', ls=1.04)]

def foot(dark=False, page=None, source=None):
    """Vaste voettekst: scheidingslijn, logo, optionele bron, paginanummer.
    Bron staat hier — direct op de slide — niet in een aparte bronnenlijst."""
    y0 = H_ - 128
    out = [rect(M, y0, W - 2 * M, 1, 'FFFFFF33' if dark else INK100),
           pic('assets/logo_white.png' if dark else 'assets/logo_navy.png',
               M, y0 + 44, 168, 40)]
    if source:
        out += [text(M + 220, y0 + 46, W - 2 * M - 220 - 140, CAPTION * 1.6, source,
                     size=CAPTION, color='8FA9B4' if dark else INK500, align='left', ls=1.35)]
    if page:
        out += [text(W - M - 80, y0 + 50, 80, 36, str(page),
                     size=CAPTION, color='FFFFFF8C' if dark else INK500, align='right')]
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
    prs.slide_width, prs.slide_height = E(W), E(H_)

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
            line = f';box-shadow:0 0 0 {el["lw"]}px #{el["line"]}' if el.get('line') else ''
            parts.append(f'<div style="position:absolute;{st}background:#{el["fill"]};'
                         f'border-radius:50%{line}"></div>')
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
        '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;500;600;700;800'
        '&family=Inter:wght@400;450;500;600;700&display=swap" rel="stylesheet">'
        '<style>*{margin:0;padding:0;box-sizing:border-box}html,body{background:#fff}'
        f'.slide{{position:relative;width:1920px;height:1080px;overflow:hidden;background:{bg}}}'
        '</style></head><body><div class="slide">' + ''.join(parts) + '</div></body></html>')
    return path

def shoot(html_path, png_path):
    # Headless Chrome geeft een viewport die ~90px korter is dan --window-size,
    # waardoor de voettekst er stilletjes afvalt. Daarom hoger schieten en terugsnijden.
    subprocess.run([CHROME, '--headless', '--disable-gpu', f'--screenshot={png_path}',
                    f'--window-size={W},{H_ + 160}', '--hide-scrollbars', '--no-sandbox',
                    '--virtual-time-budget=4000', html_path],
                   capture_output=True)
    from PIL import Image
    im = Image.open(png_path)
    if im.size != (W, H_):
        im.crop((0, 0, W, H_)).save(png_path)
    return png_path
