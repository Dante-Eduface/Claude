"""Rendert iconen en logo's uit de HTML-versie naar transparante PNG's voor de pptx."""
import re, subprocess, pathlib
from PIL import Image

HIER = pathlib.Path(__file__).parent
A = HIER / 'assets'
ROOT = HIER.parents[3]
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
html = (HIER.parent / 'business-case-academica.html').read_text()
symbols = {m[0]: (m[1], m[2]) for m in
           re.findall(r'<symbol id="i-([a-z]+)" (viewBox="0 0 24 24"[^>]*)>(.*?)</symbol>', html, re.S)}

def shoot(body, out, w, h):
    tmp = A / '_tmp.html'
    tmp.write_text(f'<html><body style="margin:0;background:transparent">{body}</body></html>')
    subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                    '--default-background-color=00000000', f'--window-size={w + 40},{h + 200}',
                    f'--screenshot={out}', f'file://{tmp}'], capture_output=True)
    tmp.unlink()
    im = Image.open(out).convert('RGBA')
    bbox = im.split()[3].getbbox()
    if bbox: im.crop(bbox).save(out)

for naam, (attrs, inner) in symbols.items():
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="192" height="192" {attrs} style="color:#000326">{inner}</svg>'
    shoot(svg, A / f'icoon-{naam}.png', 192, 192)

merk = ROOT / 'Design/Merk/logo-van-scholen'
grijs = 'filter:grayscale(1) opacity(.7)'
shoot(f'<img src="file://{HIER.parent}/academica-logo.svg" style="width:826px;height:160px">', A / 'logo-academica.png', 826, 160)
shoot(f'<img src="file://{merk}/Logo\'s/NL scholen/Hogeschool Rotterdam.svg" style="height:160px;{grijs}">', A / 'logo-hr.png', 1200, 160)
shoot(f'<img src="file://{merk}/Logo\'s/NL scholen/Radboud universiteit- Cropped.svg" style="height:160px;{grijs}">', A / 'logo-radboud.png', 1200, 160)
shoot(f'<img src="file://{merk}/overdehaagse-mediakit-hhsnlgroenhexpng.png" style="height:160px;{grijs}">', A / 'logo-hhs.png', 1200, 160)
shoot(f'<img src="file://{merk}/Logo\'s/SVG niet cropped/Tilburg universiteit.svg" style="width:1032px;height:712px;{grijs}">', A / 'logo-tilburg.png', 1032, 712)
print(sorted(p.name for p in A.iterdir()))
