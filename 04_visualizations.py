import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import numpy as np

matplotlib.use('Agg')

OUTPUT_DIR = "output"

# --- DATE ---
words_anthropo = ["pain", "shame", "gender", "power", "experience",
                  "culture", "memory", "desire", "suffering", "identity",
                  "meaning", "ritual", "embodiment", "practice", "social"]

words_bio = ["muscle", "organ", "cell", "nerve", "bone",
             "function", "system", "tissue", "blood", "membrane",
             "pressure", "receptor", "protein", "enzyme", "skeletal"]

freq_a_anthropo = [4.29, 0.0, 0.21, 1.36, 1.6, 0.15, 3.45, 0.09, 0.33, 0.27, 2.15, 0.0, 0.0, 0.64, 0.15]
freq_b_anthropo = [0.6, 0.18, 0.42, 7.16, 23.29, 21.06, 15.83, 0.36, 0.12, 3.67, 12.34, 9.09, 1.38, 11.38, 31.9]

freq_a_bio = [54.77, 7.59, 52.99, 17.3, 47.0, 21.02, 63.91, 41.38, 100.9, 26.28, 31.55, 9.16, 13.73, 5.17, 13.73]
freq_b_bio = [0.18, 0.96, 0.42, 0.06, 0.06, 2.53, 11.8, 0.0, 1.32, 0.12, 0.84, 0.24, 0.06, 0.0, 0.12]

# =============================================================
# GRAFIC 1: DIVERGING BAR CHART
# =============================================================
all_words = words_anthropo + words_bio
all_a = freq_a_anthropo + freq_a_bio
all_b = freq_b_anthropo + freq_b_bio

# normalizare pentru vizibilitate
max_val = max(max(all_a), max(all_b))
norm_a = [-v / max_val for v in all_a]   # Biology spre stânga
norm_b = [v / max_val for v in all_b]    # Anthropology spre dreapta

fig, ax = plt.subplots(figsize=(14, 16))

y_pos = np.arange(len(all_words))

bars_a = ax.barh(y_pos, norm_a, color='steelblue', alpha=0.85, label='Biology (Corpus A)')
bars_b = ax.barh(y_pos, norm_b, color='darkorange', alpha=0.85, label='Anthropology (Corpus B)')

ax.set_yticks(y_pos)
ax.set_yticklabels(all_words, fontsize=11)
ax.axvline(0, color='black', linewidth=1.2)
ax.set_xlabel("← Biology                                    Anthropology →", fontsize=12)
ax.set_title("Epistemic Silences: Word Distribution Across Discursive Regimes\n(normalized frequency per 10,000 tokens)",
             fontsize=13, fontweight='bold', pad=15)

# linie separatoare între cele două liste
ax.axhline(len(words_anthropo) - 0.5, color='gray', linewidth=1.5, linestyle='--', alpha=0.7)
ax.text(0.01, len(words_anthropo) - 0.3, "↑ Anthropological vocabulary", fontsize=9, color='gray', transform=ax.get_yaxis_transform())
ax.text(0.01, len(words_anthropo) + 0.1, "↓ Biological vocabulary", fontsize=9, color='gray', transform=ax.get_yaxis_transform())

ax.legend(loc='lower right', fontsize=11)
ax.set_xlim(-1.1, 1.1)
ax.xaxis.set_visible(False)

plt.tight_layout()
path1 = os.path.join(OUTPUT_DIR, "diverging_bar_chart.png")
plt.savefig(path1, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Diverging bar chart salvat: {path1}")

# =============================================================
# GRAFIC 2: SCATTER PLOT EPISTEMIC
# =============================================================
all_words_scatter = words_anthropo + words_bio
all_a_scatter = freq_a_anthropo + freq_a_bio
all_b_scatter = freq_b_anthropo + freq_b_bio

# culori: portocaliu = cuvinte antropologice, albastru = cuvinte biologice
colors = ['darkorange'] * len(words_anthropo) + ['steelblue'] * len(words_bio)

fig, ax = plt.subplots(figsize=(13, 11))

scatter = ax.scatter(all_a_scatter, all_b_scatter,
                     c=colors, s=120, alpha=0.85, edgecolors='white', linewidths=0.8)

# etichete cuvinte
for i, word in enumerate(all_words_scatter):
    x, y = all_a_scatter[i], all_b_scatter[i]
    ax.annotate(word, (x, y),
                textcoords="offset points", xytext=(6, 4),
                fontsize=9, alpha=0.9)

# linie diagonală de referință
max_xy = max(max(all_a_scatter), max(all_b_scatter))
ax.plot([0, max_xy], [0, max_xy], color='gray', linewidth=1, linestyle='--', alpha=0.5, label='Equal frequency')

# zone epistemice
ax.text(max_xy * 0.6, max_xy * 0.05, "Biology\nDominance", fontsize=10,
        color='steelblue', alpha=0.6, fontweight='bold')
ax.text(max_xy * 0.02, max_xy * 0.7, "Anthropology\nDominance", fontsize=10,
        color='darkorange', alpha=0.6, fontweight='bold')

ax.set_xlabel("Frequency in Biology Textbooks (per 10,000 tokens)", fontsize=12)
ax.set_ylabel("Frequency in Anthropology Texts (per 10,000 tokens)", fontsize=12)
ax.set_title("Epistemic Scatter: Where Words Live\nWords near axes = Epistemic Silences",
             fontsize=13, fontweight='bold', pad=15)

patch_a = mpatches.Patch(color='darkorange', alpha=0.85, label='Anthropological vocabulary')
patch_b = mpatches.Patch(color='steelblue', alpha=0.85, label='Biological vocabulary')
ax.legend(handles=[patch_a, patch_b], fontsize=11, loc='upper right')

ax.set_xlim(-2, max_xy * 1.1)
ax.set_ylim(-1, max_xy * 1.1)
ax.grid(True, alpha=0.2)

plt.tight_layout()
path2 = os.path.join(OUTPUT_DIR, "epistemic_scatter.png")
plt.savefig(path2, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Scatter plot salvat: {path2}")

print("\n✓ Toate vizualele generate.")
