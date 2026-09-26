#!/usr/bin/env python3
"""Deal value voor Close uit een studentenaantal.

De formule komt uit .claude/scripts/pipeline.py (bereken_jaarwaarde: studenten x 3 x 12),
zodat een prijswijziging op één plek landt. Close rekent in euro, dus het bedrag is euro
voor elke markt. Alleen het eindbedrag wordt afgerond, op twee significante cijfers, half
naar boven. Het studentenaantal zelf blijft exact: dat is het bewijs.

Gebruik: python3 dealwaarde.py 14000 800 34314
"""
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, ".claude", "scripts"))
from pipeline import bereken_jaarwaarde  # noqa: E402


def afronden(bedrag, cijfers=2):
    """Rond af op `cijfers` significante cijfers, half naar boven: 531612 wordt 530000."""
    if not bedrag or bedrag <= 0:
        return None
    stap = 10 ** max(len(str(int(bedrag))) - cijfers, 0)
    return int((Decimal(int(bedrag)) / stap).quantize(Decimal(1), rounding=ROUND_HALF_UP)) * stap


def deal_value(studenten):
    """Geeft (exact, afgerond) in euro, of (None, None) als er geen bruikbaar getal is."""
    exact = bereken_jaarwaarde(studenten)
    return exact, afronden(exact)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        exact, rond = deal_value(arg)
        print(f"{arg} studenten: exact {exact}, Deal value {rond}")
