import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter

matplotlib.use('Agg')

# --- CONFIGURARE ---
OUTPUT_DIR = "output"
TOP_N = 50

def load_tokens(corpus_name):
    """Încarcă tokens dintr-un fișier txt."""
    path = os.path.join(OUTPUT_DIR, f"{corpus_name}_tokens.txt")
    with open(path, 'r', encoding='utf-8') as f:
        tokens = f.read().splitlines()
    return tokens

def get_frequency(tokens, top_n=TOP_N):
    """Returnează cele mai frecvente cuvinte."""
    counter = Counter(tokens)
    return counter.most_common(top_n)

# --- ÎNCĂRCARE ---
print("Încarc tokens...")
tokens_a = load_tokens("corpus_a")
tokens_b = load_tokens("corpus_b")

freq_a = get_frequency(tokens_a)
freq_b = get_frequency(tokens_b)

# --- SALVARE CSV ---
df_a = pd.DataFrame(freq_a, columns=["word", "frequency"])
df_b = pd.DataFrame(freq_b, columns=["word", "frequency"])

df_a["corpus"] = "Biology (Corpus A)"
df_b["corpus"] = "Anthropology (Corpus B)"

df_combined = pd.concat([df_a, df_b])
csv_path = os.path.join(OUTPUT_DIR, "word_frequency.csv")
df_combined.to_csv(csv_path, index=False)
print(f"✓ CSV salvat: {csv_path}")

# --- VIZUALIZARE ---
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# Corpus A
words_a = [w for w, _ in freq_a[:30]]
counts_a = [c for _, c in freq_a[:30]]
axes[0].barh(words_a[::-1], counts_a[::-1], color='steelblue')
axes[0].set_title("Top 30 Words — Biology Textbooks (Corpus A)", fontsize=13, fontweight='bold')
axes[0].set_xlabel("Frequency")

# Corpus B
words_b = [w for w, _ in freq_b[:30]]
counts_b = [c for _, c in freq_b[:30]]
axes[1].barh(words_b[::-1], counts_b[::-1], color='darkorange')
axes[1].set_title("Top 30 Words — Anthropology Texts (Corpus B)", fontsize=13, fontweight='bold')
axes[1].set_xlabel("Frequency")

plt.suptitle("Word Frequency Comparison: Epistemic Regimes of the Body", fontsize=15, fontweight='bold')
plt.tight_layout()

png_path = os.path.join(OUTPUT_DIR, "word_frequency.png")
plt.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"✓ Grafic salvat: {png_path}")

# --- RAPORT CONSOLĂ ---
print("\n--- TOP 20 CORPUS A (Biology) ---")
for word, count in freq_a[:20]:
    print(f"  {word}: {count}")

print("\n--- TOP 20 CORPUS B (Anthropology) ---")
for word, count in freq_b[:20]:
    print(f"  {word}: {count}")

print("\n✓ Word frequency completă.")
