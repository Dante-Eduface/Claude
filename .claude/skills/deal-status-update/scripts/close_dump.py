#!/usr/bin/env python3
"""Dump alle brondata van een Close lead naar één leesbaar bestand.

Haalt op: lead, contacten, opportunities (incl. huidige note), taken (open en
afgerond), notes, meetings (incl. summary.text en user_note die de MCP-tool
weglaat) en emails (met quoted tekst gestript).

Gebruik:
    python3 close_dump.py <output_dir> <naam>=<lead_id> [<naam>=<lead_id> ...]
"""
import base64
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SETTINGS = os.path.join(ROOT, ".claude", "settings.local.json")

QUOTE = re.compile(r"^\s*[>|]", re.M)
BOILER = re.compile(
    r"(Disclaimer\b|Microsoft Teams meeting|________|Join:|Meeting ID:|Passcode:"
    r"|Find a local number|Phone conference ID|Reset dial-in PIN|Org help)", re.I)


def key():
    with open(SETTINGS) as f:
        return json.load(f)["env"]["CLOSE_API_KEY"]


def get(url, k):
    req = urllib.request.Request(url)
    req.add_header("Authorization",
                   "Basic " + base64.b64encode((k + ":").encode()).decode())
    return json.load(urllib.request.urlopen(req))


def clean(text, limit=1500):
    """Strip quoted replies and calendar boilerplate."""
    if not text:
        return ""
    lines = []
    for line in text.splitlines():
        if QUOTE.match(line) or BOILER.search(line):
            continue
        lines.append(line.rstrip())
    out = "\n".join(l for l in lines if l.strip())
    return out[:limit] + ("\n[...afgekapt...]" if len(out) > limit else "")


def dump(name, lead_id, k, outdir):
    p = []
    lead = get("https://api.close.com/api/v1/lead/%s/" % lead_id, k)
    p.append("# %s (%s)\nStatus: %s\nURL: %s" % (
        lead["display_name"], lead_id, lead.get("status_label"), lead.get("url")))

    p.append("\n## Contacten")
    for c in lead.get("contacts", []):
        mails = ", ".join(e["email"] for e in c.get("emails", []))
        p.append("- %s | %s | %s" % (c.get("name"), c.get("title") or "geen titel", mails))

    p.append("\n## Opportunities")
    for o in get("https://api.close.com/api/v1/opportunity/?lead_id=%s" % lead_id, k)["data"]:
        p.append("- %s | %s (%s) | %s | conf=%s | close_date=%s" % (
            o["id"], o["status_label"], o["status_type"], o.get("value_formatted"),
            o.get("confidence"), o.get("date_won") or o.get("date_lost") or "geen"))
        if o.get("note"):
            p.append("  HUIDIGE NOTE:\n%s" % "\n".join(
                "  | " + l for l in o["note"].splitlines()))

    p.append("\n## Taken")
    tasks = get("https://api.close.com/api/v1/task/?lead_id=%s&_limit=100" % lead_id, k)["data"]
    if not tasks:
        p.append("- geen open taken")
    for t in tasks:
        p.append("- due %s | done=%s | %s | %s" % (
            t.get("date"), t.get("is_complete"), t.get("text"), t.get("assigned_to_name")))

    acts, skip = [], 0
    while True:
        page = get("https://api.close.com/api/v1/activity/?lead_id=%s&_limit=100&_skip=%d"
                   % (lead_id, skip), k)
        acts += page["data"]
        if not page.get("has_more"):
            break
        skip += 100

    p.append("\n## Notes")
    notes = [a for a in acts if a["_type"] == "Note"]
    if not notes:
        p.append("- geen notes")
    for a in sorted(notes, key=lambda x: x.get("date_created") or ""):
        p.append("\n### %s door %s\n%s" % (
            (a.get("date_created") or "")[:10], a.get("user_name"), clean(a.get("note"), 3000)))

    p.append("\n## Meetings (summary + user_note)")
    meetings = get(
        "https://api.close.com/api/v1/activity/meeting/?lead_id=%s&_limit=100"
        "&_fields=id,title,starts_at,status,summary,user_note,attendees" % lead_id, k)["data"]
    shown = 0
    for m in sorted(meetings, key=lambda x: x.get("starts_at") or ""):
        summary = (m.get("summary") or {}).get("text") or ""
        note = m.get("user_note") or ""
        if not summary and not note:
            continue
        shown += 1
        who = ", ".join(a.get("name") or a.get("email", "") for a in (m.get("attendees") or []))
        p.append("\n### %s | %s | %s\nDeelnemers: %s" % (
            (m.get("starts_at") or "")[:10], m.get("title"), m.get("status"), who))
        if summary:
            p.append("SUMMARY:\n%s" % clean(summary, 6000))
        if note:
            p.append("USER NOTE:\n%s" % clean(note, 6000))
    p.append("\n(%d van %d meetings had inhoud; de rest is alleen een agenda-item)" % (
        shown, len(meetings)))

    p.append("\n## Statuswijzigingen")
    for a in sorted(acts, key=lambda x: x.get("date_created") or ""):
        if a["_type"] == "OpportunityStatusChange":
            p.append("- %s | opp: %s -> %s" % (
                (a.get("date_created") or "")[:10], a.get("old_status_label"),
                a.get("new_status_label")))
        elif a["_type"] == "LeadStatusChange":
            p.append("- %s | lead: %s -> %s" % (
                (a.get("date_created") or "")[:10], a.get("old_status_label"),
                a.get("new_status_label")))

    p.append("\n## Emails (nieuwste eerst)")
    emails = [a for a in acts if a["_type"] == "Email"]
    seen = set()
    for a in emails:
        subj = (a.get("subject") or "").strip()
        body = clean(a.get("body_text"), 900)
        fingerprint = (subj, body[:200])
        if fingerprint in seen:
            continue
        seen.add(fingerprint)
        p.append("\n### %s | %s | van %s naar %s\nOnderwerp: %s\n%s" % (
            (a.get("date_created") or "")[:10], a.get("direction"),
            a.get("sender"), ", ".join(a.get("to") or []), subj, body))
    p.append("\n(%d emails, %d uniek na ontdubbelen)" % (len(emails), len(seen)))

    path = os.path.join(outdir, name + ".md")
    with open(path, "w") as f:
        f.write("\n".join(p))
    print("%-12s %5d regels  %s" % (name, len("\n".join(p).splitlines()), path))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    k = key()
    for pair in sys.argv[2:]:
        name, lead_id = pair.split("=", 1)
        dump(name, lead_id, k, outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
