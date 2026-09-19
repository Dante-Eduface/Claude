#!/usr/bin/env python3
"""Dump alle Close-leads met gespreksinhoud (meetings, calls met notitie, notes, mails).
Bouwt voort op deal-status-update/scripts/close_dump.py, plus calls en een lead-lijst.
Gebruik: python3 close_alles.py <output_dir>
"""
import base64, json, os, re, sys, urllib.request, urllib.parse, time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SETTINGS = os.path.join(ROOT, ".claude", "settings.local.json")
QUOTE = re.compile(r"^\s*[>|]", re.M)
BOILER = re.compile(r"(Disclaimer\b|Microsoft Teams meeting|________|Join:|Meeting ID:|Passcode:"
                    r"|Find a local number|Phone conference ID|Reset dial-in PIN|Org help)", re.I)

def key():
    with open(SETTINGS) as f:
        return json.load(f)["env"]["CLOSE_API_KEY"]

def get(url, k):
    for i in range(4):
        try:
            req = urllib.request.Request(url)
            req.add_header("Authorization", "Basic " + base64.b64encode((k + ":").encode()).decode())
            return json.load(urllib.request.urlopen(req))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2 + i * 2); continue
            raise
        except (urllib.error.URLError, ConnectionError, OSError):
            time.sleep(3 + i * 3); continue
    raise RuntimeError("rate limit")

def clean(text, limit=1500):
    if not text: return ""
    lines = [l.rstrip() for l in text.splitlines() if not (QUOTE.match(l) or BOILER.search(l))]
    out = "\n".join(l for l in lines if l.strip())
    return out[:limit] + ("\n[...afgekapt...]" if len(out) > limit else "")

def paged(url, k):
    skip, out = 0, []
    while True:
        page = get(url + ("&" if "?" in url else "?") + "_limit=100&_skip=%d" % skip, k)
        out += page["data"]
        if not page.get("has_more"): return out
        skip += 100

def dump(lead_id, k, outdir):
    lead = get("https://api.close.com/api/v1/lead/%s/" % lead_id, k)
    name = lead["display_name"]
    p = ["# %s\nlead_id: %s\nStatus: %s\nClose: https://app.close.com/lead/%s/\nWebsite: %s" % (
        name, lead_id, lead.get("status_label"), lead_id, lead.get("url"))]
    p.append("\n## Contacten")
    for c in lead.get("contacts", []):
        p.append("- %s | %s" % (c.get("name"), c.get("title") or "geen titel"))
    p.append("\n## Opportunities")
    for o in get("https://api.close.com/api/v1/opportunity/?lead_id=%s" % lead_id, k)["data"]:
        p.append("- %s (%s) | %s | conf=%s" % (o["status_label"], o["status_type"], o.get("value_formatted"), o.get("confidence")))
        if o.get("note"): p.append("  HUIDIGE NOTE:\n" + "\n".join("  | " + l for l in o["note"].splitlines()))
    acts = paged("https://api.close.com/api/v1/activity/?lead_id=%s" % lead_id, k)
    p.append("\n## Notes")
    for a in sorted([a for a in acts if a["_type"] == "Note"], key=lambda x: x.get("date_created") or ""):
        p.append("\n### %s | note | door %s | id=%s\n%s" % ((a.get("date_created") or "")[:10], a.get("user_name"), a["id"], clean(a.get("note"), 4000)))
    p.append("\n## Calls (met notitie)")
    for a in sorted([a for a in acts if a["_type"] == "Call" and (a.get("note") or "").strip()], key=lambda x: x.get("date_created") or ""):
        c = next((c for c in lead.get("contacts", []) if c["id"] == a.get("contact_id")), {})
        p.append("\n### %s | call | met %s | %ss | id=%s\n%s" % ((a.get("date_created") or "")[:10], c.get("name") or "onbekend", a.get("duration"), a["id"], clean(a.get("note"), 4000)))
    p.append("\n## Meetings (summary + user_note)")
    meetings = get("https://api.close.com/api/v1/activity/meeting/?lead_id=%s&_limit=100&_fields=id,title,starts_at,status,summary,user_note,attendees" % lead_id, k)["data"]
    for m in sorted(meetings, key=lambda x: x.get("starts_at") or ""):
        summary = (m.get("summary") or {}).get("text") or ""; note = m.get("user_note") or ""
        if not summary and not note: continue
        who = ", ".join(a.get("name") or a.get("email", "") for a in (m.get("attendees") or []))
        p.append("\n### %s | meeting | %s | id=%s\nDeelnemers: %s" % ((m.get("starts_at") or "")[:10], m.get("title"), m["id"], who))
        if summary: p.append("SUMMARY:\n" + clean(summary, 8000))
        if note: p.append("USER NOTE:\n" + clean(note, 8000))
    p.append("\n## Emails (inbound alleen, nieuwste eerst)")
    seen = set()
    for a in [a for a in acts if a["_type"] == "Email" and a.get("direction") == "incoming"]:
        subj = (a.get("subject") or "").strip(); body = clean(a.get("body_text"), 1200)
        fp = (subj, body[:200])
        if fp in seen or not body: continue
        seen.add(fp)
        p.append("\n### %s | email in | van %s | id=%s\nOnderwerp: %s\n%s" % ((a.get("date_created") or "")[:10], a.get("sender"), a["id"], subj, body))
    safe = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-")[:60]
    path = os.path.join(outdir, safe + ".md")
    with open(path, "w") as f: f.write("\n".join(p))
    return name, len("\n".join(p).splitlines()), path

def main():
    outdir = sys.argv[1]; os.makedirs(outdir, exist_ok=True); k = key()
    ids = {}
    for m in paged("https://api.close.com/api/v1/activity/meeting/?_fields=id,lead_id,summary,user_note", k):
        if (m.get("summary") or {}).get("text") or m.get("user_note"): ids[m["lead_id"]] = ids.get(m["lead_id"], 0) + 3
    for c in paged("https://api.close.com/api/v1/activity/call/?_fields=id,lead_id,note", k):
        if len((c.get("note") or "").strip()) > 25: ids[c["lead_id"]] = ids.get(c["lead_id"], 0) + 1
    for n in paged("https://api.close.com/api/v1/activity/note/?_fields=id,lead_id,note", k):
        if len((n.get("note") or "").strip()) > 40: ids[n["lead_id"]] = ids.get(n["lead_id"], 0) + 1
    print("%d leads met inhoud" % len(ids))
    index = []
    done = set()
    idx = os.path.join(outdir, "_index.tsv")
    if os.path.exists(idx):
        for line in open(idx).read().splitlines()[1:]:
            parts = line.split("\t"); done.add(parts[1]); index.append(tuple(parts))
    for lid, score in sorted(ids.items(), key=lambda x: -x[1]):
        if lid in done: continue
        name, n, path = dump(lid, k, outdir)
        index.append((name, lid, score, n, os.path.basename(path)))
        print("%-45s score=%2d %5d regels" % (name[:45], score, n), flush=True)
        with open(idx, "w") as f:
            f.write("naam\tlead_id\tscore\tregels\tbestand\n")
            for r in index: f.write("\t".join(str(x) for x in r) + "\n")
    with open(os.path.join(outdir, "_index.tsv"), "w") as f:
        f.write("naam\tlead_id\tscore\tregels\tbestand\n")
        for r in index: f.write("\t".join(str(x) for x in r) + "\n")

if __name__ == "__main__": main()
