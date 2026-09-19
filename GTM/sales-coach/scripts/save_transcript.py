#!/usr/bin/env python3
"""Bewaart een Close meeting-transcript in data/transcripts/ en print de kerncijfers.

De Close REST API geeft geen transcripts. Alleen de MCP-tool
`fetch_meeting_transcript` doet dat, en die output is te groot voor de chat,
dus wordt hij door de harness naar een bestand geschreven. Dit script pakt dat
bestand op, zet het op de juiste plek en geeft je meteen de praatratio.

    python3 scripts/save_transcript.py <pad-naar-tool-result.txt>
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)
OUT = os.path.join(PROJECT, "data", "transcripts")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    with open(sys.argv[1]) as f:
        d = json.load(f)

    mid = d.get("meeting_id")
    if not mid:
        print("Geen meeting_id in dit bestand. Is dit wel een transcript-output?")
        return 1

    os.makedirs(OUT, exist_ok=True)
    dest = os.path.join(OUT, mid + ".json")
    with open(dest, "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)

    print(f"opgeslagen: data/transcripts/{mid}.json")
    for t in d.get("transcripts", []):
        dur = float(t.get("duration_seconds") or 0)
        print(f"  taal {t.get('language')}, {round(dur/60)} minuten, {len(t.get('text',''))} tekens")
        for sp in t.get("speakers", []):
            pct = round((sp.get("talk_percentage") or 0) * 100)
            kant = "jij" if sp.get("side") == "close-user" else "prospect"
            print(f"  {pct:3d}%  {sp.get('label')}  ({kant})")
    print("\nLees de tekst met:")
    print(f"  python3 -c \"import json;print(json.load(open('data/transcripts/{mid}.json'))['transcripts'][0]['text'])\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
