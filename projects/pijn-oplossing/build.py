#!/usr/bin/env python3
"""Voegt extractie/*.json samen tot items.json en bouwt pijn-oplossing.html (data inline).
Gebruik: python3 build.py [--alleen-thema <slug>]  (proefmodus: toont één thema)
"""
import json, glob, os, sys, html, collections, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
themas = json.load(open(os.path.join(HERE, "themas.json")))
themas.pop("_uitleg", None)
mapping = themas.pop("_mapping", {})

items = []
for f in sorted(glob.glob(os.path.join(HERE, "extractie", "*.json"))):
    try:
        data = json.load(open(f))
    except Exception as e:
        print("KAPOT:", f, e); continue
    for it in data:
        it.setdefault("persoon", None); it.setdefault("functie", None)
        it["thema"] = mapping.get(it["thema"], it["thema"])
        items.append(it)

# onbekende thema's melden en toch tonen
onbekend = collections.Counter(i["thema"] for i in items if i["thema"] not in themas)
for slug, n in onbekend.items():
    themas[slug] = {"naam": slug.replace("-", " ").capitalize(), "wat": "Nieuw thema uit de extractie, nog geen definitie.",
                    "oplossing": "Nog geen oplossingstekst. Toets eerst of dit thema blijft.", "bron": "", "geen_claim": "alles", "nieuw": True}
if onbekend: print("Nieuwe thema's:", dict(onbekend))

# dedup op (org, citaat[:80])
seen, uniq = set(), []
for it in items:
    k = (it["org"], (it.get("citaat") or "")[:80].lower())
    if k in seen: continue
    seen.add(k); uniq.append(it)
items = uniq

TYPE_VOLG = {"pijn": 0, "uitkomst": 1, "bezwaar": 2, "huidig": 3, "oplossing_verwoord": 4}
items.sort(key=lambda i: (i["thema"], TYPE_VOLG.get(i["type"], 9), i.get("datum") or ""))
json.dump(items, open(os.path.join(HERE, "items.json"), "w"), ensure_ascii=False, indent=1)

# thema-volgorde: op aantal items
per_thema = collections.Counter(i["thema"] for i in items)
volgorde = sorted(themas, key=lambda s: -per_thema.get(s, 0))
alleen = None
if "--alleen-thema" in sys.argv:
    alleen = sys.argv[sys.argv.index("--alleen-thema") + 1]
    volgorde = [alleen]; items = [i for i in items if i["thema"] == alleen]

segs = collections.Counter(i["segment"] for i in items)
orgs = len(set(i["org"] for i in items))
stamp = datetime.date.today().isoformat()

data_js = json.dumps({"items": items, "themas": {s: themas[s] for s in volgorde}, "volgorde": volgorde}, ensure_ascii=False)
tpl = open(os.path.join(HERE, "template.html")).read()
out = (tpl.replace("/*DATA*/", "window.DATA=" + data_js + ";")
          .replace("{{STAMP}}", stamp).replace("{{N_ITEMS}}", str(len(items)))
          .replace("{{N_ORGS}}", str(orgs)).replace("{{N_THEMAS}}", str(len(volgorde))))
name = "proef.html" if alleen else "pijn-oplossing.html"
open(os.path.join(HERE, name), "w").write(out)
print("%s: %d items, %d orgs, %d thema's | segmenten %s" % (name, len(items), orgs, len(volgorde), dict(segs)))

# ---- markdown-bron voor het volgende venster ----
SEGN = {"nl-ho": "NL ho", "uk-he": "UK/IE", "particulier": "particulier", "intl": "intl"}
TYPN = {"pijn": "Pijn", "uitkomst": "Gewenste uitkomst", "bezwaar": "Bezwaar", "huidig": "Huidige aanpak", "oplossing_verwoord": "Onze verwoording"}
md = ["# Pijn en oplossing uit Close", "", "Stand %s. %d uitspraken, %d organisaties, %d thema's. Bron: Close (meetings, calls, notes, inbound mails), gedumpt met close_alles.py, geextraheerd per dossier in extractie/, samengevoegd in items.json. Besluiten van Dante (klopt/weg) staan in besluiten.json zodra hij ze heeft gekopieerd uit de pagina." % (stamp, len(items), orgs, len(volgorde)), "",
      "Leesregels: `zekerheid=parafrase` komt uit een AI-samenvatting van een meeting, `letterlijk` uit een mail, notitie of geciteerde uitspraak. Elke regel eindigt met de Close-link van de lead; het activity-id staat in items.json.", ""]
for slug in volgorde:
    t = themas[slug]; lijst = [i for i in items if i["thema"] == slug]
    md += ["## %s (%d)" % (t["naam"], len(lijst)), "", "_%s_" % t["wat"], "", "**Onze oplossing:** %s" % t["oplossing"]]
    if t.get("bron"): md.append("Bron: %s" % t["bron"])
    if t.get("geen_claim"): md.append("Geen claim in de bron over: %s" % t["geen_claim"])
    md.append("")
    for typ in TYPE_VOLG:
        sub = [i for i in lijst if i["type"] == typ]
        if not sub: continue
        md.append("### %s" % TYPN[typ])
        for i in sub:
            wie = ", ".join(x for x in [i.get("persoon"), i.get("functie")] if x)
            md.append("- `%s` [%s] \"%s\" (%s%s, %s, %s, %s) %s" % (
                i["id"], SEGN.get(i["segment"], i["segment"]), i["citaat"], i["org"], (", " + wie) if wie else "",
                i.get("datum") or "", i["bron_type"], i["zekerheid"], i["close_url"]))
            md.append("  - %s" % i["samenvatting"])
        md.append("")
if not alleen:
    open(os.path.join(HERE, "pijn-bibliotheek.md"), "w").write("\n".join(md))
    print("pijn-bibliotheek.md geschreven")
