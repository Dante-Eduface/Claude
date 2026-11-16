#!/usr/bin/env python3
"""Bouw een Eduface go-live plan (.docx) uit een JSON-bestand, op het vaste sjabloon.

Gebruik:
  python3 build.py <plan.json> <uit.docx> [--png <map>] [--template <sjabloon.docx>]

Het sjabloon is het UTI go-live plan (opmaak, kleuren, tabellen). Het script vervangt
alle inhoud; de opmaak komt uit prototyperijen in het sjabloon. Zie ../reference.md
voor het JSON-schema.
"""
import json, os, re, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_TEMPLATE = HERE.parent / "template" / "go-live-plan-template.docx"
ZEBRA = "ebf5ff"
SH = f'<w:shd w:fill="{ZEBRA}" w:val="clear"/>'
STATUS = {
    "Done": "6aa84f", "In progress": "f59e0b", "Proposed": "f1c232",
    "To confirm": "f1c232", "To share": "f1c232", "Shared": "93c47d",
    "To plan together": "bf9000",
}
PLAIN_FILLS = ("auto", ZEBRA, "ffffff")


def status_color(t):
    if t in STATUS:
        return STATUS[t]
    if t.startswith("Waiting"):
        return "f59e0b"
    return None


def esc(x):
    return (x or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def rows(tb):
    return re.findall(r"<w:tr[ >].*?</w:tr>", tb, re.S)


def cells(r):
    return re.findall(r"<w:tc>.*?</w:tc>", r, re.S)


def fill_of(c):
    f = re.findall(r'<w:shd w:fill="(\w+)"', c.split("</w:tcPr>")[0])
    return f[0].lower() if f else "auto"


def settexts(r, texts):
    cs = cells(r)
    assert len(cs) == len(texts), (len(cs), texts)
    out = r
    for c, t in zip(cs, texts):
        if t is None:
            continue
        runs = re.findall(r"<w:r>(?:(?!</w:r>).)*?<w:t[^>]*>[^<]*</w:t></w:r>", c, re.S)
        nc = c
        for k, ru in enumerate(runs):
            new = re.sub(r"(<w:t[^>]*>)[^<]*(</w:t>)", lambda m: m.group(1) + esc(t) + m.group(2), ru) if k == 0 else ""
            nc = nc.replace(ru, new, 1)
        nc = nc.replace("<w:t>", '<w:t xml:space="preserve">')
        out = out.replace(c, nc, 1)
    return out


def cellfix(c, zebra):
    f = fill_of(c)
    if f not in PLAIN_FILLS:  # statuscel: kleur volgt de tekst
        t = "".join(re.findall(r"<w:t[^>]*>([^<]*)", c)).strip()
        col = status_color(t)
        if col:
            c = re.sub(r'w:fill="\w+"', f'w:fill="{col}"', c, count=1)
        return c
    c = re.sub(r"<w:shd [^>]*/>(?=(?:(?!<w:tcPr>).)*?</w:tcPr>)", "", c, flags=re.S)
    if zebra:
        c = re.sub(r"(<w:tcPr>.*?)(<w:noWrap|<w:tcMar>|<w:textDirection|<w:tcFitText|<w:vAlign|<w:hideMark|</w:tcPr>)",
                   lambda m: m.group(1) + SH + m.group(2), c, count=1, flags=re.S)
    return c


def shade(r, zebra):
    return re.sub(r"<w:tc>.*?</w:tc>", lambda m: cellfix(m.group(0), zebra), r, flags=re.S)


def keep_whole(r):
    return r.replace('<w:cantSplit w:val="0"/>', '<w:cantSplit w:val="1"/>')


def keep_next(r):
    def fix(m):
        ppr = m.group(0)
        if "<w:keepNext" in ppr:
            return ppr
        st = re.match(r"<w:pPr>(<w:pStyle [^>]*/>)?", ppr)
        return ppr[:st.end()] + "<w:keepNext/>" + ppr[st.end():]
    return re.sub(r"<w:pPr>.*?</w:pPr>", fix, r, flags=re.S)


def body(tb, keep, new):
    rs = rows(tb)
    a = tb.find(rs[0]); b = tb.rfind(rs[-1]) + len(rs[-1])
    return tb[:a] + "".join(rs[:keep]) + "".join(new) + tb[b:]


def build(plan, template, out_docx):
    work = Path(tempfile.mkdtemp(prefix="glp_"))
    with zipfile.ZipFile(template) as z:
        z.extractall(work)
    doc = work / "word" / "document.xml"
    s = doc.read_text()
    s = re.sub(r'<w:commentRange(Start|End) w:id="\d+"/>', "", s)
    s = re.sub(r'<w:r><w:commentReference w:id="\d+"/></w:r>', "", s)
    s = re.sub(r' w14:paraId="[0-9A-F]+"', "", s)
    T = list(re.finditer(r"<w:tbl>.*?</w:tbl>", s, re.S))
    assert len(T) == 9, f"sjabloon heeft {len(T)} tabellen, verwacht 9"
    new = {}

    # 1 titel + laatst bijgewerkt
    t = T[1].group(0); rs = rows(t)
    new[1] = body(t, 0, [settexts(rs[0], [f"{plan['client']} Go Live Plan"]),
                         settexts(rs[1], [f"Last updated {plan['last_updated']} by {plan.get('author', 'Dante Torbed')}"])])

    # 2 information
    t = T[2].group(0); rs = rows(t)
    new[2] = body(t, 1, [settexts(rs[1], [k, v]) for k, v in plan["info"]])

    # 3 brief summary: alinea's in een cel, gescheiden door een witregel
    t = T[3].group(0); rs = rows(t); r = rs[1]
    p = re.search(r"<w:p[ >].*?</w:p>", r, re.S).group(0)
    rpr = re.search(r"<w:r>(<w:rPr>.*?</w:rPr>)", p, re.S)
    rpr = rpr.group(1) if rpr else ""
    runs = []
    for i, para in enumerate(plan["summary"]):
        if i:
            runs.append(f"<w:r>{rpr}<w:br/><w:br/></w:r>")
        runs.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(para)}</w:t></w:r>')
    ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
    np_ = p[:p.index(">") + 1] + (ppr.group(0) if ppr else "") + "".join(runs) + "</w:p>"
    new[3] = t.replace(r, r.replace(p, np_), 1)

    # 4 who is involved: groepsrij Eduface, mensen, groepsrij klant, mensen
    t = T[4].group(0); rs = rows(t)
    groups = [i for i, r in enumerate(rs) if i > 0 and '<w:tblHeader w:val="1"/>' in r]
    g_proto = rs[groups[0]]
    person = next(r for i, r in enumerate(rs) if i > groups[0] and i not in groups)
    def people(lst):
        return [keep_whole(shade(settexts(person, [esc(x) for x in it]), i % 2 == 1)) for i, it in enumerate(lst)]
    who = [settexts(g_proto, ["Eduface"] + [" "] * (len(cells(g_proto)) - 1))] + people(plan["eduface_team"])
    who += [settexts(g_proto, [plan["client"]] + [" "] * (len(cells(g_proto)) - 1))] + people(plan["client_team"])
    new[4] = body(t, 1, [settexts(r, [None] * len(cells(r))) for r in who])

    # 5 planned steps
    t = T[5].group(0); rs = rows(t); proto = rs[2]
    steps = [keep_whole(shade(settexts(proto, [str(i + 1)] + list(st)), i % 2 == 1)) for i, st in enumerate(plan["steps"])]
    new[5] = body(t, 2, steps)

    # 6 days on campus (optioneel)
    t = T[6].group(0)
    if plan.get("campus"):
        rs = rows(t)
        title = settexts(rs[0], [plan["campus"]["title"]])
        days = [keep_whole(shade(settexts(rs[2], list(d)), i % 2 == 1)) for i, d in enumerate(plan["campus"]["days"])]
        new[6] = body(t, 0, [keep_next(title), keep_next(rs[1])] + days)
    else:
        new[6] = ""

    # 7 where everything lives
    t = T[7].group(0); rs = rows(t)
    link = next(r for r in rs[2:] if "<w:hyperlink" in r)
    colored = next(r for r in rs[2:] if "<w:hyperlink" not in r and fill_of(cells(r)[1]) not in PLAIN_FILLS)
    plain = next(r for r in rs[2:] if "<w:hyperlink" not in r and fill_of(cells(r)[1]) in PLAIN_FILLS)
    res = []
    for i, it in enumerate(plan["resources"]):
        name, status, detail = it[0], it[1], it[2]
        url = it[3] if len(it) > 3 else None
        if url:
            rels = work / "word" / "_rels" / "document.xml.rels"
            rid = re.search(r'r:id="(\w+)"', link).group(1)
            rx = rels.read_text()
            rx = re.sub(rf'(Id="{rid}"[^>]*Target=")[^"]*"', lambda m: m.group(1) + esc(url) + '"', rx)
            rx = re.sub(rf'(Target=")[^"]*("[^>]*Id="{rid}")', lambda m: m.group(1) + esc(url) + m.group(2), rx)
            rels.write_text(rx)
            proto = link
        else:
            proto = colored if status_color(status) else plain
        res.append(keep_whole(shade(settexts(proto, [name, status, detail]), i % 2 == 1)))
    new[7] = body(t, 0, [keep_next(rs[0]), keep_next(rs[1])] + res)

    # 8 questions and answers
    t = T[8].group(0); rs = rows(t)
    qa = [keep_whole(shade(settexts(rs[2], list(q)), i % 2 == 1)) for i, q in enumerate(plan["qa"])]
    new[8] = body(t, 0, [keep_next(rs[0]), keep_next(rs[1])] + qa)

    out = s
    for k in sorted(new, reverse=True):
        m = T[k]
        out = out[:m.start()] + new[k] + out[m.end():]
    doc.write_text(out)

    # klantlogo
    if plan.get("client_logo"):
        set_logo(work, Path(plan["client_logo"]))

    # opmerkingen leeg
    cm = work / "word" / "comments.xml"
    if cm.exists():
        cm.write_text(re.sub(r"<w:comment .*?</w:comment>", "", cm.read_text(), flags=re.S))

    out_docx = Path(out_docx)
    if out_docx.exists():
        out_docx.unlink()
    with zipfile.ZipFile(out_docx, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(work.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(work).as_posix())
    shutil.rmtree(work)
    return out_docx


def set_logo(work, logo):
    from PIL import Image
    rels = (work / "word" / "_rels" / "document.xml.rels").read_text()
    doc = work / "word" / "document.xml"
    s = doc.read_text()
    rids = re.findall(r'r:embed="(\w+)"', s)
    rid = rids[1]  # tweede afbeelding = klantlogo
    target = re.search(rf'Id="{rid}"[^>]*Target="([^"]+)"|Target="([^"]+)"[^>]*Id="{rid}"', rels)
    target = target.group(1) or target.group(2)
    dst = work / "word" / target
    im = Image.open(logo).convert("RGBA")
    im.save(dst.with_suffix(".png"))
    if dst.suffix != ".png":
        dst.unlink()
    m = re.search(rf'<wp:extent cx="(\d+)" cy="(\d+)"/>(?:(?!<wp:extent).)*?r:embed="{rid}"', s, re.S)
    cx_old, cy_old = int(m.group(1)), int(m.group(2))
    cy_new = int(cx_old * im.height / im.width)
    block = m.group(0).replace(f'cy="{cy_old}"', f'cy="{cy_new}"')
    tail = s[m.end():]
    tail = tail.replace(f'<a:ext cx="{cx_old}" cy="{cy_old}"/>', f'<a:ext cx="{cx_old}" cy="{cy_new}"/>', 1)
    doc.write_text(s[:m.start()] + block + tail)


def render(docx, outdir):
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    prof = tempfile.mkdtemp(prefix="lo_")
    env = dict(os.environ, SAL_USE_VCLPLUGIN="svp")
    subprocess.run(["soffice", f"-env:UserInstallation=file://{prof}", "--headless", "--convert-to", "pdf",
                    "--outdir", str(outdir), str(docx)], check=True, capture_output=True, env=env)
    pdf = outdir / (Path(docx).stem + ".pdf")
    subprocess.run(["pdftoppm", "-png", "-r", "150", str(pdf), str(outdir / Path(docx).stem)], check=True)
    return sorted(outdir.glob(Path(docx).stem + "-*.png"))


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) < 2:
        sys.exit(__doc__)
    tpl = DEFAULT_TEMPLATE
    png = None
    if "--template" in a:
        tpl = Path(a[a.index("--template") + 1])
    if "--png" in a:
        png = a[a.index("--png") + 1]
    plan = json.loads(Path(a[0]).read_text())
    if plan.get("client_logo") and not os.path.isabs(plan["client_logo"]):
        plan["client_logo"] = str((Path(a[0]).parent / plan["client_logo"]).resolve())
    out = build(plan, tpl, a[1])
    print(out)
    if png:
        for p in render(out, png):
            print(p)
