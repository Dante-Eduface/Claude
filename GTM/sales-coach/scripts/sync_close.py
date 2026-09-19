#!/usr/bin/env python3
"""Sync Close CRM -> GTM/sales-coach/data/deals/*.json

Elk dealbestand heeft twee zones:
  "close"  wordt bij elke sync overschreven (feiten uit het CRM)
  "coach"  blijft altijd staan (prep, MEDDPICC, call-reviews, stakeholderrollen)

Gebruik:
    python3 GTM/sales-coach/scripts/sync_close.py            # alle leads met een gesprek
    python3 GTM/sales-coach/scripts/sync_close.py --lead lead_xxx
"""
import base64
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(PROJECT, "..", ".."))
DEALS = os.path.join(PROJECT, "data", "deals")
SETTINGS = os.path.join(ROOT, ".claude", "settings.local.json")

BASE = "https://api.close.com/api/v1/"


def key():
    with open(SETTINGS) as f:
        return json.load(f)["env"]["CLOSE_API_KEY"]


_K = None


def get(path):
    global _K
    if _K is None:
        _K = key()
    req = urllib.request.Request(BASE + path)
    req.add_header("Authorization", "Basic " + base64.b64encode((_K + ":").encode()).decode())
    return json.load(urllib.request.urlopen(req))


def get_all(path, limit=100):
    out, skip = [], 0
    sep = "&" if "?" in path else "?"
    while True:
        r = get(f"{path}{sep}_limit={limit}&_skip={skip}")
        out += r.get("data", [])
        if not r.get("has_more"):
            return out
        skip += limit


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")
    return s or "onbekend"


def txt(html):
    if not html:
        return ""
    s = re.sub(r"<br\s*/?>", "\n", html)
    s = re.sub(r"</p>", "\n\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return s.strip()


EMPTY_COACH = {
    "next_action": {"wat": "", "wanneer": "", "wie": "", "waarom": ""},
    "prep": {"doel": "", "openers": [], "vragen": [], "risicos": [], "bezwaren": []},
    "meddpicc": {},
    "gate": {"fase": "", "open": None, "ontbreekt": []},
    "stakeholders": [],
    "calls": [],
    "diagnose": "",
    "laatst_gecoacht": "",
}


def main():
    only = None
    if "--lead" in sys.argv:
        only = sys.argv[sys.argv.index("--lead") + 1]

    print("Close ophalen...")
    opps = get_all("opportunity/")
    meetings = get_all("activity/meeting/")
    calls = get_all("activity/call/")
    tasks = get_all("task/?_type=lead")

    lead_ids = set()
    for m in meetings:
        if m.get("lead_id"):
            lead_ids.add(m["lead_id"])
    for c in calls:
        if c.get("lead_id") and c.get("status") == "completed" and (c.get("note") or c.get("duration")):
            lead_ids.add(c["lead_id"])
    for o in opps:
        lead_ids.add(o["lead_id"])
    if only:
        lead_ids = {only}

    print(f"{len(lead_ids)} accounts met een gesprek of opportunity")

    by_lead_m, by_lead_c, by_lead_t, by_lead_o = {}, {}, {}, {}
    for m in meetings:
        by_lead_m.setdefault(m.get("lead_id"), []).append(m)
    for c in calls:
        by_lead_c.setdefault(c.get("lead_id"), []).append(c)
    for t in tasks:
        by_lead_t.setdefault(t.get("lead_id"), []).append(t)
    for o in opps:
        by_lead_o.setdefault(o["lead_id"], []).append(o)

    os.makedirs(DEALS, exist_ok=True)
    index = []
    for lid in sorted(lead_ids):
        try:
            lead = get(f"lead/{lid}/")
        except Exception as e:
            print(f"  overslaan {lid}: {e}")
            continue

        slug = slugify(lead.get("display_name") or lead.get("name"))
        path = os.path.join(DEALS, slug + ".json")

        doc = {"slug": slug, "coach": json.loads(json.dumps(EMPTY_COACH))}
        if os.path.exists(path):
            with open(path) as f:
                doc = json.load(f)
            coach = doc.get("coach") or {}
            for k, v in EMPTY_COACH.items():
                coach.setdefault(k, json.loads(json.dumps(v)))
            doc["coach"] = coach
            doc["slug"] = slug

        o_list = sorted(by_lead_o.get(lid, []), key=lambda o: o.get("date_updated") or "", reverse=True)
        opp = o_list[0] if o_list else None

        m_list = sorted(
            [m for m in by_lead_m.get(lid, []) if m.get("status") != "canceled"],
            key=lambda m: m.get("starts_at") or "",
        )
        c_list = sorted(
            [c for c in by_lead_c.get(lid, []) if c.get("note") or (c.get("duration") or 0) > 30],
            key=lambda c: c.get("activity_at") or "",
        )

        gesprekken = []
        for m in m_list:
            gesprekken.append({
                "id": m["id"],
                "soort": "meeting",
                "datum": (m.get("starts_at") or "")[:10],
                "titel": m.get("title") or "Meeting",
                "duur_min": round((m.get("duration") or 0) / 60),
                "status": m.get("status"),
                "deelnemers": [a.get("email") for a in (m.get("attendees") or [])],
                "samenvatting": (m.get("summary") or {}).get("text") if isinstance(m.get("summary"), dict) else None,
                "eigen_notitie": txt(m.get("user_note_html")) or m.get("user_note") or "",
                "transcript_beschikbaar": bool(m.get("notetaker_id")),
            })
        for c in c_list:
            gesprekken.append({
                "id": c["id"],
                "soort": "call",
                "datum": (c.get("activity_at") or "")[:10],
                "titel": "Telefoon " + (c.get("direction") or ""),
                "duur_min": round((c.get("duration") or 0) / 60),
                "status": c.get("disposition"),
                "deelnemers": [],
                "samenvatting": None,
                "eigen_notitie": txt(c.get("note_html")) or c.get("note") or "",
                "transcript_beschikbaar": bool(c.get("has_recording")),
            })
        gesprekken.sort(key=lambda g: g["datum"])
        vandaag = datetime.now().strftime("%Y-%m-%d")
        for g in gesprekken:
            g["komend"] = g["datum"] > vandaag
        gehad = [g for g in gesprekken if not g["komend"]]
        komend = [g for g in gesprekken if g["komend"]]

        open_taken = [
            {"tekst": t.get("text"), "datum": (t.get("date") or "")[:10]}
            for t in by_lead_t.get(lid, [])
            if not t.get("is_complete")
        ]

        doc["close"] = {
            "lead_id": lid,
            "naam": lead.get("display_name") or lead.get("name"),
            "url": f"https://app.close.com/lead/{lid}/",
            "lead_status": (lead.get("status_label") or ""),
            "opportunity_id": opp["id"] if opp else None,
            "fase": opp.get("status_label") if opp else None,
            "fase_type": opp.get("status_type") if opp else None,
            "waarde": round((opp.get("value") or 0) / 100) if opp else None,
            "valuta": opp.get("value_currency") if opp else "EUR",
            "confidence": opp.get("confidence") if opp else None,
            "close_date": opp.get("date_won") if opp else None,
            "eigenaar": opp.get("user_name") if opp else lead.get("created_by_name"),
            "crm_note": (opp.get("note") or "") if opp else "",
            "contacten": [
                {
                    "naam": c.get("name"),
                    "titel": c.get("title"),
                    "email": (c.get("emails") or [{}])[0].get("email"),
                    "id": c.get("id"),
                }
                for c in (lead.get("contacts") or [])
            ],
            "gesprekken": gesprekken,
            "open_taken": open_taken,
            "laatste_gesprek": gehad[-1]["datum"] if gehad else None,
            "volgende_afspraak": komend[0]["datum"] if komend else None,
            "aantal_gehad": len(gehad),
            "gesynct": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        }

        with open(path, "w") as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)
        index.append(slug)
        print(f"  {slug:35s} {len(gesprekken)} gesprekken")

    print(f"\n{len(index)} deals weggeschreven naar data/deals/")
    print("Bouw nu de app: python3 GTM/sales-coach/scripts/build.py")


if __name__ == "__main__":
    sys.exit(main() or 0)
