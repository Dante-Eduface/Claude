"""Maakt figuur 1 voor de simpele fictieve paper over Veltra Connect.

LET OP, bewuste fout: het omzetdoel voor 2027 staat hier op 12,0 in plaats van 10,0
(de tabel in de paper zegt 10,0). Dat is de fout die de student maakt, om te testen
of Eduface hem oppikt via het grafiek-criterium. Niet "repareren".

Draaien: python3 maak_figuur_simpel.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HIER = Path(__file__).parent
plt.rcParams["font.family"] = "Carlito"

jaren = ["2023", "2024", "2025", "2026", "2027"]
waarden = [3.5, 4.6, 6.0, 8.0, 12.0]  # 2027 hoort 10,0 te zijn
is_doel = [False, False, False, True, True]

fig, ax = plt.subplots(figsize=(7, 4), dpi=200)
kleuren = ["#7fb27f" if d else "#1f4e79" for d in is_doel]
staven = ax.bar(jaren, waarden, color=kleuren, width=0.6,
                hatch=["//" if d else "" for d in is_doel], edgecolor="white")
for staaf, waarde in zip(staven, waarden):
    ax.annotate(f"€{waarde:.1f}".replace(".", ","), (staaf.get_x() + staaf.get_width() / 2, waarde),
                textcoords="offset points", xytext=(0, 4), ha="center", fontsize=10)

ax.set_title("Figuur 1. Omzet Veltra Connect en de earn-out-doelen, 2023–2027",
             fontsize=11, loc="left")
ax.set_ylabel("Omzet (€ mln)")
ax.set_xlabel("Jaar")
ax.set_ylim(0, 14)
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(handles=[Patch(color="#1f4e79", label="Gerealiseerde omzet"),
                   Patch(facecolor="#7fb27f", hatch="//", edgecolor="white", label="Earn-out-doel")],
          loc="upper left", frameon=False, fontsize=9)
fig.text(0.01, 0.01, "Bron: casusgegevens Veltra Connect, eigen bewerking.", fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(HIER / "figuur-1-omzet-simpel.png")
print("figuur-1-omzet-simpel.png")
