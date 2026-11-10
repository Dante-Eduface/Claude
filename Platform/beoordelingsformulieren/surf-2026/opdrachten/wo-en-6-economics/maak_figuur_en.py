"""Maakt figuur 1 voor de fictieve paper over Veltra Connect.

LET OP, bewuste fout: het ARR-doel voor 2027 staat hier op 24,0 in plaats van 22,0
(de tabel in de paper zegt 22,0). Dat is de fout die de student maakt, om te testen
of Eduface hem oppikt via het grafiek-criterium. Niet "repareren".

Draaien: python3 maak_figuur.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HIER = Path(__file__).parent
plt.rcParams["font.family"] = "Carlito"

gerealiseerd = [(2023, 7.3), (2024, 9.9), (2025, 12.6), (2025.5, 14.9)]
doel = [(2026, 17.0), (2027, 24.0), (2028, 28.0)]  # 2027 hoort 22,0 te zijn
drempel = [(2026, 13.6), (2027, 17.6), (2028, 22.4)]

fig, ax = plt.subplots(figsize=(8, 4.6), dpi=200)


def lijn(punten, **opmaak):
    x, y = zip(*punten)
    ax.plot(x, y, **opmaak)
    for xi, yi in punten:
        ax.annotate(f"{yi:.1f}".replace(",", ","), (xi, yi), textcoords="offset points",
                    xytext=(0, 7), ha="center", fontsize=9)


lijn(gerealiseerd, color="#1f4e79", marker="o", linewidth=2, label="Actual ARR")
lijn(doel, color="#2e7d32", marker="s", linewidth=2, label="Earn-out target (100%)")
lijn(drempel, color="#c62828", marker="^", linewidth=1.5, linestyle="--",
     label="Threshold (80% of target)")

ax.set_title("Figure 1. Veltra Connect ARR versus earn-out targets, 2023–2028",
             fontsize=11, loc="left")
ax.set_ylabel("ARR (€ m)")
ax.set_xlabel("Year (as at 31 December; 2025.5 = June 2026)")
ax.set_xticks([2023, 2024, 2025, 2026, 2027, 2028])
ax.set_ylim(0, 32)
ax.grid(axis="y", alpha=0.3)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="upper left", frameon=False, fontsize=9)
fig.text(0.01, 0.01, "Source: Veltra Connect case data, own analysis.", fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(HIER / "figure-1-arr-en.png")
print("figure-1-arr-en.png")
