#!/usr/bin/env python3
"""Bouwt de Action Learning-documenten: markdown -> HTML -> PDF (headless Chrome)."""
import glob
import os
import subprocess
import sys

import markdown

BASE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 22mm 20mm 20mm 20mm; }
body { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 10.2pt;
       line-height: 1.45; color: #1a2230; }
h1 { font-size: 17pt; margin: 26px 0 10px; padding-bottom: 5px;
     border-bottom: 2px solid #0f2d4a; page-break-before: always; page-break-after: avoid; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 13pt; margin: 20px 0 7px; color: #0f2d4a; page-break-after: avoid; }
h3 { font-size: 11.2pt; margin: 15px 0 5px; color: #24425f; page-break-after: avoid; }
h4 { font-size: 10.4pt; margin: 12px 0 4px; }
p { margin: 0 0 8px; text-align: justify; }
ul, ol { margin: 0 0 10px 18px; padding: 0; }
li { margin-bottom: 3px; }
table { border-collapse: collapse; width: 100%; margin: 10px 0 14px;
        font-size: 8.6pt; page-break-inside: auto; }
th { background: #0f2d4a; color: #fff; text-align: left; padding: 5px 6px;
     border: 1px solid #0f2d4a; font-weight: 600; }
td { border: 1px solid #c3cdd8; padding: 4px 6px; vertical-align: top; }
tr:nth-child(even) td { background: #f4f7fa; }
blockquote { margin: 10px 0; padding: 9px 14px; background: #f4f7fa;
             border-left: 3px solid #1f7a5a; }
blockquote p { margin-bottom: 6px; }
code, pre { font-family: "SFMono-Regular", Menlo, monospace; font-size: 8.4pt; }
pre { background: #f4f7fa; border: 1px solid #d6dee7; padding: 9px;
      white-space: pre; overflow: hidden; page-break-inside: avoid; }
hr { border: 0; border-top: 1px solid #d6dee7; margin: 18px 0; }
strong { color: #0f2d4a; }
"""


def build(name, parts, title):
    md = "\n\n".join(open(os.path.join(BASE, "src", p), encoding="utf-8").read()
                     for p in parts)
    html_body = markdown.markdown(md, extensions=["tables", "fenced_code", "attr_list"])
    html = (f"<!DOCTYPE html><html lang='nl'><head><meta charset='utf-8'>"
            f"<title>{title}</title><style>{CSS}</style></head>"
            f"<body>{html_body}</body></html>")
    html_path = os.path.join(BASE, f"{name}.html")
    pdf_path = os.path.join(BASE, f"{name}.pdf")
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(html)
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", "--virtual-time-budget=20000",
                    f"file://{html_path}"], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import fitz
    pages = len(fitz.open(pdf_path))
    words = len(md.split())
    print(f"{name}: {pages} pagina's, {words} woorden -> {pdf_path}")
    return pages


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "opdracht"):
        parts = sorted(os.path.basename(p) for p in glob.glob(os.path.join(BASE, "src", "*.md")))
        build("Notenboom_ALP_Opdracht", parts,
              "Opdracht Action Learning Project BK4.ALP01")
    if which in ("all", "beoordeling"):
        parts = sorted(os.path.basename(p) for p in glob.glob(os.path.join(BASE, "rubric", "*.md")))
        if parts:
            src_backup = None
            md = "\n\n".join(open(os.path.join(BASE, "rubric", p), encoding="utf-8").read()
                             for p in parts)
            html_body = markdown.markdown(md, extensions=["tables", "fenced_code", "attr_list"])
            html = (f"<!DOCTYPE html><html lang='nl'><head><meta charset='utf-8'>"
                    f"<title>Beoordelingsschema BK4.ALP01</title><style>{CSS}</style></head>"
                    f"<body>{html_body}</body></html>")
            hp = os.path.join(BASE, "Notenboom_ALP_Beoordelingsschema.html")
            pp = os.path.join(BASE, "Notenboom_ALP_Beoordelingsschema.pdf")
            open(hp, "w", encoding="utf-8").write(html)
            subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                            f"--print-to-pdf={pp}", "--virtual-time-budget=20000",
                            f"file://{hp}"], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            import fitz
            print(f"beoordelingsschema: {len(fitz.open(pp))} pagina's, "
                  f"{len(md.split())} woorden -> {pp}")
