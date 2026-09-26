#!/usr/bin/env python3
"""Zoekt in de lokale Close-dump naar studentenaantallen, voor alle leads tegelijk.

Leest de .md-bestanden die GTM/ICP/pijn-oplossing/close_alles.py maakt (notes, calls,
inkomende mails, meeting-samenvattingen) en geeft per treffer een regel terug: lead,
datum, type, activity-id, getal en een stukje tekst eromheen. Oordelen doet het niet,
dat doet de skill: een pilotgroep van 125 komt hier ook langs.

Gebruik:
  python3 scan_dump.py [dump_map] [--lead "naam of lead_id"] [--min 100]
"""
import argparse, glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DEFAULT_DUMP = os.path.join(ROOT, "GTM", "ICP", "pijn-oplossing", "close-dump")

WOORD = (r"(?:students?|learners?|pupils?|trainees?|enrol(?:l)?(?:ment|ed)s?|"
         r"studenten|cursisten|cursist|deelnemers|lerenden|leerlingen)")
GETAL = r"(\d{1,3}(?:[.,]\d{3})+|\d{2,6})(\s*\+|\s*k\b|\s+(?:thousand|duizend))?"
VOOR = re.compile(GETAL + r"(?:\s+[^\s]+){0,3}?\s+" + WOORD, re.I)
NA = re.compile(WOORD + r"(?:\s+[^\s]+){0,5}?\s+(?:[~±≈]|ca\.?\s*|circa\s+)?" + GETAL, re.I)
VALUTA = re.compile(r"[€£$]\s*$|\b(?:eur|gbp|usd)\s*$", re.I)
KOP = re.compile(r"^### (\S+) \| ([^|]+?) \|.*?id=(\S+)", re.M)


def naar_int(tekst, staart):
    n = int(re.sub(r"[.,]", "", tekst))
    s = (staart or "").strip().lower()
    if s in ("k", "thousand", "duizend"):
        n *= 1000
    return n


def treffers(tekst, minimum):
    for rx, groep in ((VOOR, 1), (NA, 1)):
        for m in rx.finditer(tekst):
            ruw = m.group(groep)
            staart = m.group(groep + 1)
            start = m.start(groep)
            if VALUTA.search(tekst[max(0, start - 5):start]):
                continue
            if ruw.startswith("0"):
                continue  # telefoonnummer of code, geen aantal
            n = naar_int(ruw, staart)
            if n < minimum:
                continue
            if 1990 <= n <= 2035 and not re.search(r"[.,]", ruw) and not (staart or "").strip():
                continue  # jaartal, geen aantal
            a, b = max(0, m.start() - 110), min(len(tekst), m.end() + 110)
            yield n, " ".join(tekst[a:b].split())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("dump", nargs="?", default=DEFAULT_DUMP)
    p.add_argument("--lead", help="alleen leads waarvan naam of lead_id dit bevat")
    p.add_argument("--min", type=int, default=100)
    args = p.parse_args()

    bestanden = sorted(f for f in glob.glob(os.path.join(args.dump, "*.md")))
    leads_met = set()
    rijen = []
    for f in bestanden:
        tekst = open(f, encoding="utf-8").read()
        naam = tekst.splitlines()[0].lstrip("# ").strip()
        m = re.search(r"^lead_id: (\S+)", tekst, re.M)
        lead_id = m.group(1) if m else "?"
        if args.lead and args.lead.lower() not in (naam + " " + lead_id).lower():
            continue
        koppen = list(KOP.finditer(tekst))
        for i, k in enumerate(koppen):
            blok = tekst[k.end(): koppen[i + 1].start() if i + 1 < len(koppen) else len(tekst)]
            gezien = set()
            for n, fragment in treffers(blok, args.min):
                if (n, fragment) in gezien:
                    continue
                gezien.add((n, fragment))
                leads_met.add(lead_id)
                rijen.append((naam, lead_id, k.group(1), k.group(2).strip(), k.group(3), n, fragment))

    print("lead\tlead_id\tdatum\ttype\tactivity_id\tgetal\tfragment")
    for r in rijen:
        print("\t".join(str(x) for x in r))
    print(f"# {len(bestanden)} bestanden, {len(leads_met)} leads met een kandidaat, {len(rijen)} treffers",
          file=sys.stderr)


if __name__ == "__main__":
    main()
