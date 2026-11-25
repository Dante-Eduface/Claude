"""Bouwt de twee drukbestanden voor Full Vision (OEB 2026, stand C11) op 25% schaal.
Stappen: Chromium -> PDF, bijsnijden op de exacte maat in mm, Ghostscript -dNoOutputFonts (tekst naar outlines), PNG-reserve."""
import subprocess, os, sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
from pypdf import Transformation
HERE = os.path.dirname(os.path.abspath(__file__)); PT = 72 / 25.4; S = 0.25
# Chromium schaalt de achterwand 0,15% te klein; gemeten met fit_shift.py en hier teruggezet (fascia: 0,003%, geen correctie nodig)
FIX = {'Eduface_OEB2026_C11_Achterwand_25pct': (1.001929, 1.001797), 'Eduface_OEB2026_C11_Fascia_25pct': (1.0, 1.0)}
JOBS = [  # naam, html, breedte mm (100%), hoogte mm (100%)
    ('Eduface_OEB2026_C11_Achterwand_25pct', '../backwall-print.html', 2954, 2520),
    ('Eduface_OEB2026_C11_Fascia_25pct',     '../facade-print.html',   3020, 350)]
os.makedirs(f'{HERE}/raw', exist_ok=True); os.makedirs(f'{HERE}/levering', exist_ok=True)
for name, html, W, H in JOBS:
    raw, cut, out = f'{HERE}/raw/{name}.pdf', f'{HERE}/raw/{name}_cut.pdf', f'{HERE}/levering/{name}.pdf'
    subprocess.run(['node', f'{HERE}/export_pdf.js', f'{HERE}/{html}', str(W), str(H), raw], check=True)
    r = PdfReader(raw); pg = r.pages[0]; ph = float(pg.mediabox.height)
    sx, sy = FIX[name]
    if (sx, sy) != (1.0, 1.0): pg.add_transformation(Transformation().scale(sx, sy).translate(0, ph * (1 - sy)))   # vast aan linksboven
    ew, eh = W * S * PT, H * S * PT                       # exacte maat in punten
    box = RectangleObject([0, ph - eh, ew, ph])           # vast aan linksboven: de overmaat valt rechts en onder weg
    pg.mediabox = box; pg.cropbox = box
    w = PdfWriter(); w.add_page(pg); w.write(cut)
    subprocess.run(['gs', '-q', '-dBATCH', '-dNOPAUSE', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.6', '-dNoOutputFonts',
        '-dAutoFilterColorImages=false', '-dColorImageFilter=/FlateEncode', '-dDownsampleColorImages=false',
        '-dAutoFilterGrayImages=false', '-dGrayImageFilter=/FlateEncode', '-dDownsampleGrayImages=false', '-dDownsampleMonoImages=false',
        '-dUseCropBox', f'-sOutputFile={out}', cut], check=True)
    print('klaar', out)
