"""Meet schaal en verschuiving van een PDF-render t.o.v. het ontwerp, via overeenkomende randen op veel rijen en kolommen.
Gebruik: python3 fit_shift.py <pdf.png> <ontwerp.png> <W> <H>   (uitvoer: sx sy tx ty in ontwerp-mm, zo dat ontwerp = sx*pdf + tx)"""
import sys
from PIL import Image
import numpy as np
pdf, ref, W, H = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
def load(p):
    im = Image.open(p).convert('L')
    return np.asarray(im.resize((W, H), Image.LANCZOS) if im.size != (W, H) else im).astype(float)
a, b = load(pdf), load(ref)
def edge_pos(line, thr=30):
    g = np.diff(line); out = []
    for i in np.where(np.abs(g) > thr)[0]:
        # subpixel: zwaartepunt van de gradient rond de piek
        lo, hi = max(i - 2, 0), min(i + 3, len(g)); w = np.abs(g[lo:hi]); out.append((np.arange(lo, hi) * w).sum() / w.sum() + .5) if w.sum() else None
    res = []
    for p in out:
        if not res or p - res[-1] > 5: res.append(p)
    return np.array(res)
def match(pos_ref, pos_pdf, tol=8):
    pairs = []
    for r in pos_ref:
        d = pos_pdf - r; j = np.argmin(np.abs(d))
        if abs(d[j]) < tol: pairs.append((r, pos_pdf[j]))
    return pairs
def fit(pairs):
    x = np.array([p[1] for p in pairs]); y = np.array([p[0] for p in pairs])
    for _ in range(3):
        s, t = np.polyfit(x, y, 1); res = y - (s * x + t); keep = np.abs(res) < max(2 * res.std(), 1.0); x, y = x[keep], y[keep]
    return s, t, len(x), np.abs(y - (s * x + t)).max()
px, py = [], []
for row in np.linspace(60, H - 60, 25).astype(int): px += match(edge_pos(b[row, :]), edge_pos(a[row, :]))
for col in np.linspace(60, W - 60, 25).astype(int): py += match(edge_pos(b[:, col]), edge_pos(a[:, col]))
sx, tx, nx, ex = fit(px); sy, ty, ny, ey = fit(py)
print(f'sx={sx:.6f} tx={tx:.3f}  (n={nx}, max rest {ex:.2f} mm) | sy={sy:.6f} ty={ty:.3f}  (n={ny}, max rest {ey:.2f} mm)')
