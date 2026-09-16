#!/usr/bin/env python3
"""
dossiers-genereren.py - eenmalige, herhaalbare migratie van CSV-cellen naar dossiers.

Het master-document bewaart de stand, het dossier bewaart de inhoud. Dit script
verplaatst wat er al in de vier inhoudsvelden stond naar een dossier per persoon,
en splitst het oude dossiers.md naar een bestand per organisatie.

HARDE EIS: dit script overschrijft nooit een bestaand dossier. migrate-master.py
mag opnieuw gedraaid worden en de dossiers moeten dat overleven, net als
DANTE_KIEST daar.

Drie stappen, los te draaien zodat je ertussen kunt kijken:

  dossiers-genereren.py personen [--echt]   dossiers uit people.csv
  dossiers-genereren.py orgs     [--echt]   dossiers.md splitsen per organisatie
  dossiers-genereren.py teasers  [--echt]   de vier velden inkorten tot 200 tekens

Zonder --echt doet hij niets, hij vertelt alleen wat hij zou doen.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pipeline as P  # noqa: E402

OUD_DOSSIERS_MD = os.path.join(P.REPO, "projects", "targetlijst-nl", "dossiers.md")
STEMPEL = "<!-- gemigreerd uit het master-document op 2026-08-14, niet herschreven -->"
DRAGER_WAARSCHUWING = (
    "LET OP: dit is overgezet uit de oude CSV-velden. De dragers zijn nog niet "
    "toegekend, dus lees hier geen last van de beoordelaar in die er niet staat. "
    "Zie references/onderwijs-vaktermen.md."
)


def blok(titel, waarde):
    waarde = (waarde or "").strip()
    if not waarde:
        return ""
    return "**%s**\n%s\n" % (titel, waarde) if titel else waarde + "\n"


def persoon_dossier(p, org_naam):
    """Kolom naar kop. Niets herschrijven, alleen verplaatsen."""
    kop = "# %s%s" % (p.get("naam") or p["person_id"], (" — " + org_naam) if org_naam else "")
    uit = [kop, "", "<!-- id: %s -->" % p["person_id"], STEMPEL, ""]

    def sectie(naam, stukken):
        inhoud = "\n".join(s for s in stukken if s).strip()
        uit.append("## %s" % naam)
        if inhoud:
            uit.append(inhoud)
        uit.append("")

    sectie("Waarom deze persoon", [
        blok("", p.get("waarom_deze_persoon")),
        blok("Functiebron", p.get("functie_bron")),
        blok("In functie sinds", p.get("in_functie_sinds")),
        blok("Alternatief hoger in de boom", p.get("alternatief_hoger_in_boom")),
    ])
    sectie("Bronnen", [
        blok("Bron van het haakje", p.get("haakje_bron_url")),
        blok("Type bron", p.get("haakje_bron_type")),
        blok("Datum van de bron", p.get("haakje_gevonden_op")),
    ])
    cit = [blok("", p.get("opvallend")), blok("Haakje zoals agent 3 het opschreef", p.get("haakje"))]
    if any(c for c in cit):
        cit.insert(0, DRAGER_WAARSCHUWING + "\n")
    sectie("Citaten", cit)
    sectie("Toetsprogramma", [
        blok("", p.get("toetsprogramma")),
        blok("Schrijfwerk", p.get("schrijfwerk")),
    ])
    sectie("Getallen", [])
    sectie("Rare details", [])
    sectie("Persoon", [
        blok("Functie", p.get("functie")),
        blok("LinkedIn", p.get("linkedin_url")),
        blok("Type instelling", p.get("type_instelling")),
    ])
    sectie("Onzekerheden", [blok("", p.get("twijfels"))])
    sectie("Berichten", [
        blok("Connectieverzoek", p.get("connectieverzoek")),
        blok("Opvolgmail, onderwerp", p.get("opvolgmail_onderwerp")),
        blok("Opvolgmail", p.get("opvolgmail")),
        blok("Waarom dit bericht", p.get("waarom_dit_bericht")),
        blok("Afgevallen openers", p.get("afgevallen_openers")),
        blok("Status", p.get("bericht_status")),
    ])
    return "\n".join(uit).rstrip() + "\n"


VELDEN_DIE_TELLEN = [
    "opvallend", "haakje", "toetsprogramma", "schrijfwerk", "twijfels",
    "waarom_dit_bericht", "connectieverzoek", "opvolgmail", "waarom_deze_persoon",
    "alternatief_hoger_in_boom",
]


def cmd_personen(a):
    orgs = {o["org_id"]: o for o in P.load(P.ORGS, P.ORG_COLS)}
    people = P.load(P.PEOPLE, P.PERSON_COLS)
    gemaakt = overgeslagen = leeg = 0
    klachten = []
    for p in people:
        pid = p["person_id"]
        if not any((p.get(v) or "").strip() for v in VELDEN_DIE_TELLEN):
            leeg += 1
            continue
        pad = P.dossier_pad(pid)
        if os.path.exists(pad):
            overgeslagen += 1
            continue
        tekst = persoon_dossier(p, orgs.get(p.get("org_id"), {}).get("naam", ""))
        problemen = P.dossier_klachten(pid, tekst)
        if problemen:
            klachten.append((pid, problemen))
            continue
        if a.echt:
            os.makedirs(os.path.dirname(pad), exist_ok=True)
            with open(pad, "w", encoding="utf-8") as f:
                f.write(tekst)
            P.journal([(pid, "dossier", "", "%d regels (migratie)" % len(tekst.splitlines()),
                        "migratie")])
        gemaakt += 1
    print("dossiers aangemaakt: %d" % gemaakt)
    print("al aanwezig, met rust gelaten: %d" % overgeslagen)
    print("geen inhoud om te verplaatsen: %d" % leeg)
    if klachten:
        print("niet weggeschreven, %d stuks:" % len(klachten))
        for pid, pr in klachten[:20]:
            print("  %s: %s" % (pid, "; ".join(pr)))
    if not a.echt:
        print("\n(dit was een proefdraai, voeg --echt toe om het echt te doen)")


def cmd_orgs(a):
    """dossiers.md splitsen: ## per organisatie, matchen op naam en aliassen."""
    if not os.path.exists(OUD_DOSSIERS_MD):
        print("niets te splitsen, %s bestaat niet" % OUD_DOSSIERS_MD)
        return
    orgs = P.load(P.ORGS, P.ORG_COLS)
    zoek = {}
    for o in orgs:
        for n in [o["naam"]] + [x for x in (o.get("naam_aliassen") or "").split("|") if x]:
            if n.strip():
                zoek.setdefault(P.norm(n), o["org_id"])

    tekst = open(OUD_DOSSIERS_MD, encoding="utf-8").read()
    ronde, kop, buf, stukken = "", None, [], []
    for regel in tekst.splitlines():
        m1 = re.match(r"^#\s+(.+?)\s*$", regel)
        m2 = re.match(r"^##\s+(.+?)\s*$", regel)
        if m2:
            if kop:
                stukken.append((kop, ronde, "\n".join(buf).strip()))
            kop, buf = m2.group(1), []
        elif m1:
            if kop:
                stukken.append((kop, ronde, "\n".join(buf).strip()))
            kop, buf = None, []
            ronde = m1.group(1)
        elif kop is not None:
            buf.append(regel)
    if kop:
        stukken.append((kop, ronde, "\n".join(buf).strip()))

    gemaakt = overgeslagen = ongematcht = 0
    onbekend = []
    for naam, ronde_naam, inhoud in stukken:
        # koppen zijn vaak "Naam — oordeel" of "Naam (toelichting)". Probeer van
        # lang naar kort, zodat "Docendo — NEE" alsnog bij Docendo landt.
        kandidaten = [naam]
        for sep in ("—", " - ", "(", ",", ":"):
            kandidaten.append(naam.split(sep)[0])
        oid = next((zoek[P.norm(k)] for k in kandidaten if P.norm(k) in zoek), None)
        if not oid:
            ongematcht += 1
            onbekend.append(naam)
            continue
        pad = P.dossier_pad(oid)
        if os.path.exists(pad):
            overgeslagen += 1
            continue
        uit = ["# %s" % naam, "", "<!-- id: %s -->" % oid, STEMPEL,
               "<!-- herkomst: dossiers.md, %s -->" % (ronde_naam or "onbekende ronde"), "",
               "## Status", inhoud, ""]
        doc = "\n".join(uit).rstrip() + "\n"
        if a.echt:
            os.makedirs(os.path.dirname(pad), exist_ok=True)
            with open(pad, "w", encoding="utf-8") as f:
                f.write(doc)
            P.journal([(oid, "dossier", "", "%d regels (migratie)" % len(doc.splitlines()),
                        "migratie")])
        gemaakt += 1
    print("secties in dossiers.md: %d" % len(stukken))
    print("organisatiedossiers aangemaakt: %d" % gemaakt)
    print("al aanwezig, met rust gelaten: %d" % overgeslagen)
    print("geen organisatie voor gevonden: %d" % ongematcht)
    for n in onbekend[:25]:
        print("  ? %s" % n)
    if not a.echt:
        print("\n(proefdraai, voeg --echt toe)")


def teaser(v):
    """Eerste zinsdeel, hooguit TEASER_MAX tekens. De lading staat in het dossier."""
    v = re.sub(r"\s+", " ", (v or "").strip())
    if len(v) <= P.TEASER_MAX:
        return v
    knip = v[:P.TEASER_MAX - 1]
    for sep in (" | ", "; ", ". "):
        i = knip.rfind(sep)
        if i > 60:
            return knip[:i].strip(" .;|")
    i = knip.rfind(" ")
    return (knip[:i] if i > 60 else knip).rstrip() + "…"


def cmd_teasers(a):
    people = P.load(P.PEOPLE, P.PERSON_COLS)
    wijzigingen, zonder_dossier = [], []
    for p in people:
        pid = p["person_id"]
        te_lang = {v: p[v] for v in P.TEASER_VELDEN if len(p.get(v) or "") > P.TEASER_MAX}
        if not te_lang:
            continue
        if not os.path.exists(P.dossier_pad(pid)):
            zonder_dossier.append(pid)
            continue
        for v, oud in te_lang.items():
            wijzigingen.append((pid, v, oud, teaser(oud)))
    print("in te korten velden: %d" % len(wijzigingen))
    if zonder_dossier:
        print("OVERGESLAGEN, geen dossier dus niets om naar te verwijzen: %d"
              % len(zonder_dossier))
        for pid in zonder_dossier[:10]:
            print("  %s" % pid)
    for pid, v, oud, nieuw in wijzigingen[:5]:
        print("  %s.%s: %d -> %d tekens" % (pid, v, len(oud), len(nieuw)))
    if not a.echt:
        print("\n(proefdraai, voeg --echt toe)")
        return
    with P.Lock():
        rows = P.load(P.PEOPLE, P.PERSON_COLS)
        idx = {r["person_id"]: r for r in rows}
        for pid, v, oud, nieuw in wijzigingen:
            idx[pid][v] = nieuw
            idx[pid]["laatst_bijgewerkt"] = P.now_iso()
            idx[pid]["bijgewerkt_door"] = "migratie"
        P.save(P.PEOPLE, P.PERSON_COLS, rows)
    P.journal([(pid, v, oud, nieuw, "migratie") for pid, v, oud, nieuw in wijzigingen])
    print("ingekort: %d velden. De volledige tekst staat in het dossier." % len(wijzigingen))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for naam, fn in (("personen", cmd_personen), ("orgs", cmd_orgs), ("teasers", cmd_teasers)):
        p = sub.add_parser(naam)
        p.add_argument("--echt", action="store_true", help="echt schrijven")
        p.set_defaults(fn=fn)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
