#!/usr/bin/env python3
"""Zet de status-update in het note-veld van een Close opportunity.

Close rendert GEEN markdown in het note-veld: `**vet**` blijft letterlijk staan.
Vet werkt alleen via het rich-text veld `note_html`, en dat moet beginnen met
<body> en eindigen met </body>. Close vult het platte `note`-veld daarna zelf.

Dit script leest een bestand met `**Label:** tekst`-blokken en zet dat om naar
HTML. Overschrijft de bestaande note, dat is de bedoeling: de note is een levend
statusveld, geen logboek.

Gebruik:
    python3 close_write_note.py <opportunity_id> <pad-naar-tekstbestand>
"""
import base64
import html
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SETTINGS = os.path.join(ROOT, ".claude", "settings.local.json")

BOLD = re.compile(r"\*\*(.+?)\*\*")


def to_html(text):
    """Zet blokken gescheiden door lege regels om naar <p>, met **vet** als <b>."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n", text.strip()) if b.strip()]
    out = []
    for block in blocks:
        escaped = html.escape(block).replace("\n", "<br/>")
        out.append("<p>%s</p>" % BOLD.sub(r"<b>\1</b>", escaped))
    return "<body>%s</body>" % "".join(out)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    oppo_id, path = sys.argv[1], sys.argv[2]
    with open(SETTINGS) as f:
        key = json.load(f)["env"]["CLOSE_API_KEY"]
    with open(path) as f:
        note_html = to_html(f.read())

    req = urllib.request.Request(
        "https://api.close.com/api/v1/opportunity/%s/" % oppo_id,
        data=json.dumps({"note_html": note_html}).encode(), method="PUT")
    req.add_header("Authorization",
                   "Basic " + base64.b64encode((key + ":").encode()).decode())
    req.add_header("Content-Type", "application/json")
    result = json.load(urllib.request.urlopen(req))
    print("OK %-14s %-10s %d tekens, %d blokken" % (
        result.get("lead_name", "")[:14], result.get("status_label"),
        len(result.get("note") or ""), note_html.count("<p>")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
