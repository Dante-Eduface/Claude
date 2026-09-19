#!/usr/bin/env python3
"""
sync-opnames.py - haalt Dictafoon-opnames (Voice Memos) op met hun echte titel.

Waarom dit script bestaat:
De Dictafoon-app slaat elk bestand op als tijdstempel (20260910 125647.m4a). De
titel die je in de app typt staat NIET in de bestandsnaam, maar in een SQLite-
database (CloudRecordings.db, kolom ZENCRYPTEDTITLE). Dit script koppelt die
twee en zet de opname als "2026-09-10 Action Learning.m4a" in Drive.

TWEE STANDEN:

  sync    Kopieert nieuwe opnames uit de Dictafoon-map naar de doelmap, met de
          juiste naam. Vereist Volledige schijftoegang (zie onderaan).

  rename  Hernoemt bestanden die AL in de doelmap staan en nog een tijdstempel
          als naam hebben. Gebruikt de meegekopieerde CloudRecordings.db in de
          doelmap. Werkt zonder Volledige schijftoegang.

Draaien:
    python3 .claude/scripts/sync-opnames.py rename
    python3 .claude/scripts/sync-opnames.py sync
    python3 .claude/scripts/sync-opnames.py sync --droogloop

Bestanden die er al staan worden nooit overschreven en nooit verwijderd.
Het origineel in de Dictafoon-app blijft altijd staan, sync kopieert alleen.

VOLLEDIGE SCHIJFTOEGANG (eenmalig, nodig voor 'sync'):
Systeeminstellingen > Privacy en beveiliging > Volledige schijftoegang, en zet
daar het programma aan dat dit script draait (Terminal, of Claude).
"""

import argparse
import os
import re
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRON = Path.home() / "Library/Group Containers/group.com.apple.VoiceMemos.shared/Recordings"
DOEL = Path(
    "/Users/User/Library/CloudStorage/GoogleDrive-dante.torbed@eduface.me/"
    "My Drive/Eduface/Archive/Opnamens"
)
DB_NAAM = "CloudRecordings.db"

# Apple rekent tijd vanaf 2001-01-01, unix vanaf 1970-01-01.
APPLE_EPOCH = 978307200

TIJDSTEMPEL = re.compile(r"^\d{8} \d{6}(-[0-9A-F]{8})?$")


def schoon(titel: str) -> str:
    """Maak een titel geschikt als bestandsnaam."""
    for teken in "/:|\\":
        titel = titel.replace(teken, "-")
    titel = re.sub(r"[-\s]*-[-\s]*", " - ", titel) if "-" in titel else titel
    titel = re.sub(r"\s+", " ", titel).strip(" .-")
    return titel


def lees_db(db_pad: Path):
    """Geef {bestandsnaam: (datum, titel)} uit een CloudRecordings.db.

    De database gebruikt write-ahead logging, dus -wal en -shm moeten mee,
    anders mis je alles wat sinds de laatste checkpoint is opgenomen.
    """
    if not db_pad.exists():
        return {}
    tmp = Path(tempfile.mkdtemp())
    try:
        for achtervoegsel in ("", "-wal", "-shm"):
            bron = Path(str(db_pad) + achtervoegsel)
            if bron.exists():
                shutil.copy2(bron, tmp / (DB_NAAM + achtervoegsel))
        con = sqlite3.connect(tmp / DB_NAAM)
        rijen = con.execute(
            "SELECT ZPATH, ZENCRYPTEDTITLE, ZCUSTOMLABEL, ZDATE "
            "FROM ZCLOUDRECORDING WHERE ZPATH IS NOT NULL"
        ).fetchall()
        con.close()
    except sqlite3.Error as fout:
        print(f"[fout] database niet te lezen: {fout}", file=sys.stderr)
        return {}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    uit = {}
    for pad, titel, label, datum in rijen:
        naam = Path(pad).name
        titel = schoon(titel or label or "")
        if not titel or not datum:
            continue
        dag = datetime.fromtimestamp(datum + APPLE_EPOCH).strftime("%Y-%m-%d")
        uit[naam] = (dag, titel)
    return uit


def vrije_naam(doelmap: Path, basis: str, ext: str) -> Path:
    """Geef een pad dat nog niet bestaat, met (2), (3) erachter als het moet."""
    kandidaat = doelmap / f"{basis}{ext}"
    teller = 2
    while kandidaat.exists():
        kandidaat = doelmap / f"{basis} ({teller}){ext}"
        teller += 1
    return kandidaat


def doe_rename(doelmap: Path, droogloop: bool) -> int:
    """Hernoem bestanden in de doelmap die nog een tijdstempel als naam hebben."""
    titels = lees_db(doelmap / DB_NAAM)
    if not titels:
        print(f"[fout] geen {DB_NAAM} in {doelmap}. Sleep die mee vanuit de "
              f"Dictafoon-map, of gebruik de stand 'sync'.", file=sys.stderr)
        return 1

    gedaan = 0
    for bestand in sorted(doelmap.glob("*.m4a")):
        if not TIJDSTEMPEL.match(bestand.stem):
            continue
        gegevens = titels.get(bestand.name)
        if not gegevens:
            print(f"[over]  {bestand.name} staat niet in de database")
            continue
        dag, titel = gegevens
        doel = vrije_naam(doelmap, f"{dag} {titel}", ".m4a")
        print(f"[naam]  {bestand.name} -> {doel.name}")
        if not droogloop:
            bestand.rename(doel)
        gedaan += 1
    return gedaan


def doe_sync(bronmap: Path, doelmap: Path, droogloop: bool) -> int:
    """Kopieer nieuwe opnames uit de Dictafoon-map naar de doelmap."""
    if not bronmap.exists():
        print(f"[fout] {bronmap} bestaat niet", file=sys.stderr)
        return -1
    try:
        os.listdir(bronmap)
    except PermissionError:
        print(f"[fout] geen toegang tot de Dictafoon-map.\n"
              f"       macOS schermt die af. Zet Volledige schijftoegang aan voor het\n"
              f"       programma dat dit script draait: Systeeminstellingen > Privacy en\n"
              f"       beveiliging > Volledige schijftoegang.\n"
              f"       Daarna werkt 'sync'. Zonder die toegang kun je de opnames zelf\n"
              f"       naar de doelmap slepen en daarna 'rename' draaien.",
              file=sys.stderr)
        return -1
    bestanden = sorted(bronmap.glob("*.m4a"))

    titels = lees_db(bronmap / DB_NAAM)
    doelmap.mkdir(parents=True, exist_ok=True)
    bestaand = {p.name for p in doelmap.iterdir()} if doelmap.exists() else set()

    gedaan = 0
    for bestand in bestanden:
        gegevens = titels.get(bestand.name)
        if gegevens:
            dag, titel = gegevens
            basis = f"{dag} {titel}"
        else:
            dag = datetime.fromtimestamp(bestand.stat().st_mtime).strftime("%Y-%m-%d")
            basis = f"{dag} {bestand.stem}"
            print(f"[let op] {bestand.name} heeft geen titel in de database")

        # Al aanwezig onder deze naam, of onder de oude tijdstempelnaam.
        if f"{basis}.m4a" in bestaand or bestand.name in bestaand:
            continue

        doel = vrije_naam(doelmap, basis, ".m4a")
        print(f"[nieuw] {bestand.name} -> {doel.name}")
        if not droogloop:
            shutil.copy2(bestand, doel)
        gedaan += 1

    # Database meekopieren, zodat 'rename' later ook zonder toegang werkt.
    if not droogloop:
        for achtervoegsel in ("", "-wal", "-shm"):
            bron = Path(str(bronmap / DB_NAAM) + achtervoegsel)
            if bron.exists():
                try:
                    shutil.copy2(bron, Path(str(doelmap / DB_NAAM) + achtervoegsel))
                except OSError:
                    pass
    return gedaan


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("stand", choices=["sync", "rename"],
                   help="sync = nieuwe opnames ophalen, rename = bestaande hernoemen")
    p.add_argument("--doel", default=str(DOEL), help="doelmap (standaard Archive/Opnamens)")
    p.add_argument("--bron", default=str(BRON), help="Dictafoon-map")
    p.add_argument("--droogloop", action="store_true",
                   help="laat zien wat er zou gebeuren, verander niets")
    a = p.parse_args()

    doelmap = Path(a.doel)
    if a.stand == "rename":
        n = doe_rename(doelmap, a.droogloop)
    else:
        n = doe_sync(Path(a.bron), doelmap, a.droogloop)

    if n < 0:
        return 1
    woord = "zou " if a.droogloop else ""
    print(f"\n{n} bestand(en) {woord}verwerkt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
