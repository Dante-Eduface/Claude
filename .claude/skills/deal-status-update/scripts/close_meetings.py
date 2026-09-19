#!/usr/bin/env python3
"""Print meeting summaries + user notes for one or more Close leads.

De Close MCP-tool geeft bij een meeting alleen het `note`-veld terug, en dat is
de agenda uit de agenda-uitnodiging. De echte inhoud zit in `summary.text`
(AI notetaker) en `user_note` (wat Jeroen/Dante zelf typte). Dit script haalt
die op via de REST API.

Gebruik:
    python3 close_meetings.py <lead_id> [<lead_id> ...]
"""
import base64
import json
import os
import sys
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SETTINGS = os.path.join(ROOT, ".claude", "settings.local.json")


def api_key():
    with open(SETTINGS) as f:
        return json.load(f)["env"]["CLOSE_API_KEY"]


def get(url, key):
    req = urllib.request.Request(url)
    token = base64.b64encode((key + ":").encode()).decode()
    req.add_header("Authorization", "Basic " + token)
    return json.load(urllib.request.urlopen(req))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    key = api_key()
    fields = "id,title,starts_at,status,summary,user_note,attendees,duration"
    for lead_id in sys.argv[1:]:
        url = (
            "https://api.close.com/api/v1/activity/meeting/"
            "?lead_id=%s&_limit=100&_fields=%s" % (lead_id, fields)
        )
        data = get(url, key)
        meetings = sorted(data["data"], key=lambda m: m.get("starts_at") or "")
        print("=" * 70)
        print("LEAD %s  (%d meetings)" % (lead_id, len(meetings)))
        print("=" * 70)
        for m in meetings:
            summary = (m.get("summary") or {}).get("text") or ""
            note = m.get("user_note") or ""
            if not summary and not note:
                continue
            people = ", ".join(
                a.get("name") or a.get("email", "") for a in (m.get("attendees") or [])
            )
            print("\n## %s | %s | status=%s" % (
                (m.get("starts_at") or "")[:10], m.get("title"), m.get("status")))
            print("Deelnemers: %s" % people)
            if summary:
                print("\nSUMMARY:\n%s" % summary)
            if note:
                print("\nUSER NOTE:\n%s" % note)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
