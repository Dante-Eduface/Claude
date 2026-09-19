#!/usr/bin/env python3
"""Bakt data/deals/*.json in tot een dubbelklikbare sales-coach.html.

    python3 GTM/sales-coach/scripts/build.py
"""
import glob
import json
import os
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)
OUT = os.path.join(PROJECT, "sales-coach.html")
TPL = os.path.join(PROJECT, "app", "template.html")


def main():
    deals = []
    for p in sorted(glob.glob(os.path.join(PROJECT, "data", "deals", "*.json"))):
        with open(p) as f:
            d = json.load(f)
        if "close" not in d:
            continue
        d.setdefault("coach", {})
        d["coach"].setdefault("calls", [])
        deals.append(d)

    calls = [c for d in deals for c in d["coach"]["calls"]]
    ratios = [c["praatratio"] for c in calls if c.get("praatratio") is not None]
    drills = sum(len(c.get("drills") or []) for c in calls)
    ongescoord = [c for c in calls if not c.get("zelfscore")]

    focus_path = os.path.join(PROJECT, "data", "focus.json")
    focus = {}
    if os.path.exists(focus_path):
        with open(focus_path) as f:
            focus = json.load(f)

    payload = {
        "gebouwd": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "deals": deals,
        "focus": focus,
        "stats": {
            "calls_gereviewd": len(calls),
            "praatratio": round(sum(ratios[-5:]) / len(ratios[-5:])) if ratios else None,
            "drills": drills,
            "zonder_zelfscore": len(ongescoord),
        },
    }

    with open(TPL) as f:
        html = f.read()
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html = html.replace("__DATA__", blob)
    with open(OUT, "w") as f:
        f.write(html)
    kb = os.path.getsize(OUT) // 1024
    print(f"{OUT}\n{len(deals)} deals, {len(calls)} gecoachte gesprekken, {drills} drills, {kb} kB")


if __name__ == "__main__":
    main()
