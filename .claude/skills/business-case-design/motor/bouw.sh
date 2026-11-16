#!/usr/bin/env bash
# Van HTML-pagina's naar een bewerkbare A4-pptx, plus een controleplaat.
# Gebruik: bash bouw.sh <werkmap> <uit.pptx> [logo.png]
# De werkmap bevat de pagina's als 1-naam.html, 2-naam.html, ... (gemaakt met bouwstenen.page).
set -euo pipefail
MOTOR="$(cd "$(dirname "$0")" && pwd)"
WERK="$(cd "$1" && pwd)"; UIT="$(realpath -m "$2")"; LOGO="${3:+$(realpath "$3")}"
# Fonts uit Design/Merk, zodat de controle-PDF dezelfde letters heeft als Canva
mkdir -p ~/.fonts && cp -n "$MOTOR/../../../../Design/Merk/fonts/"*.ttf ~/.fonts/ 2>/dev/null && fc-cache -f >/dev/null || true
mkdir -p "$WERK/build" && cd "$WERK/build" && rm -f svg-*.png
PAGINAS=$(ls "$WERK"/[0-9]*-*.html | sort -t/ -k1 -V)
node "$MOTOR/extract.js" $PAGINAS
python3 "$MOTOR/build_pptx.py" layout.json "$UIT" ${LOGO:+"$LOGO"}
# Controle: pptx naar PDF, en alle pagina's op één plaat (bekijk die altijd voor je oplevert)
timeout 180 soffice --headless --convert-to pdf --outdir "$WERK/build" "$UIT" >/dev/null 2>&1 || true
PDF="$WERK/build/$(basename "${UIT%.pptx}").pdf"
rm -f p-*.png && pdftoppm -r 50 -png "$PDF" p
python3 - <<'PY'
from PIL import Image; import glob
f = sorted(glob.glob('p-*.png')); ims = [Image.open(x) for x in f]; w, h = ims[0].size; n = 3
o = Image.new('RGB', (w*n + 10*(n-1), h*((len(ims)+n-1)//n) + 10*((len(ims)-1)//n)), '#888')
for i, im in enumerate(ims): o.paste(im, ((i % n)*(w+10), (i//n)*(h+10)))
o.save('controle.png')
PY
python3 - "$UIT" <<'PY'
import sys
from pptx import Presentation
p = Presentation(sys.argv[1]); m = 76*9525
for i, sl in enumerate(p.slides, 1):
    b = [sh.text_frame.text[:30] for sh in sl.shapes if sh.has_text_frame and sh.text_frame.text.strip()
         and (sh.left < m-10 or sh.left+sh.width > p.slide_width-m+10)]
    print(f'pagina {i}: tekst buiten marge: {b or "geen"}')
PY
echo "Controleplaat: $WERK/build/controle.png"
