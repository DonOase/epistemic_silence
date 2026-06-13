import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter

matplotlib.use('Agg')

# --- CONFIGURARE ---
OUTPUT_DIR = "output"

# Cuvinte așteptate în antropologie, absente/rare în biologie
LIST_1_ANTHROPOLOGY = [
    "pain", "shame", "gender", "power", "experience",
    "culture", "memory", "desire", "suffering", "identity",
    "meaning", "ritual", "embodiment", "practice", "social"
]

# Cuvinte așteptate în biologie, absente/rare în antropologie
LIST_2_BIOLOGY = [
    "muscle", "organ", "cell", "nerve", "bone",
    "function", "system", "tissue", "blood", "membrane",
    "pressure", "receptor", "protein", "enzyme", "skeletal"
]

def load_tokens(corpus_name):
    path = os.path.join(OUTPUT_DIR, f"{corpus_name}_tokens.txt")
    with open(path, 'r', encoding='utf-8') as f:
        tokens = f.read().splitlines()
    return tokens

def get_word_frequencies(tokens, wordlist):
    counter = Counter(tokens)
    total = len(tokens)
    results = {}
    for word in wordlist:
        count = counter.get(word, 0)
        # frequenta relativa per 10,000 tokens
        results[word] = round((count / total) * 10000, 2)
    return results

# --- ÎNCĂRCARE ---
print("Încarc tokens...")
tokens_a = load_tokens("corpus_a")
tokens_b = load_tokens("corpus_b")
print(f"  Corpus A: {len(tokens_a)} tokens")
print(f"  Corpus B: {len(tokens_b)} tokens")

# --- ANALIZĂ ---
print("\nCalculez frecvențe...")

freq_list1_a = get_word_frequencies(tokens_a, LIST_1_ANTHROPOLOGY)
freq_list1_b = get_word_frequencies(tokens_b, LIST_1_ANTHROPOLOGY)

freq_list2_a = get_word_frequencies(tokens_a, LIST_2_BIOLOGY)
freq_list2_b = get_word_frequencies(tokens_b, LIST_2_BIOLOGY)

# --- DATAFRAMES ---
df_list1 = pd.DataFrame({
    "word": LIST_1_ANTHROPOLOGY,
    "Biology (A)": [freq_list1_a[w] for w in LIST_1_ANTHROPOLOGY],
    "Anthropology (B)": [freq_list1_b[w] for w in LIST_1_ANTHROPOLOGY]
})

df_list2 = pd.DataFrame({
    "word": LIST_2_BIOLOGY,
    "Biology (A)": [freq_list2_a[w] for w in LIST_2_BIOLOGY],
    "Anthropology (B)": [freq_list2_b[w] for w in LIST_2_BIOLOGY]
})

# --- SALVARE CSV ---
df_list1.to_csv(os.path.join(OUTPUT_DIR, "silences_anthropology_words.csv"), index=False)
df_list2.to_csv(os.path.join(OUTPUT_DIR, "silences_biology_words.csv"), index=False)
print("✓ CSV-uri salvate")

# --- VIZUALIZARE HEATMAP ---
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Heatmap Lista 1 - cuvinte antropologice
data1 = df_list1.set_index("word")[["Biology (A)", "Anthropology (B)"]]
im1 = axes[0].imshow(data1.values, aspect='auto', cmap='RdYlGn')
axes[0].set_xticks([0, 1])
axes[0].set_xticklabels(["Biology (A)", "Anthropology (B)"], fontsize=11)
axes[0].set_yticks(range(len(LIST_1_ANTHROPOLOGY)))
axes[0].set_yticklabels(LIST_1_ANTHROPOLOGY, fontsize=10)
axes[0].set_title("Anthropological Words\n(freq. per 10,000 tokens)", fontsize=12, fontweight='bold')
for i in range(len(LIST_1_ANTHROPOLOGY)):
    for j in range(2):
        axes[0].text(j, i, str(data1.values[i, j]), ha='center', va='center', fontsize=9, fontweight='bold')
plt.colorbar(im1, ax=axes[0])

# Heatmap Lista 2 - cuvinte biologice
data2 = df_list2.set_index("word")[["Biology (A)", "Anthropology (B)"]]
im2 = axes[1].imshow(data2.values, aspect='auto', cmap='RdYlGn')
axes[1].set_xticks([0, 1])
axes[1].set_xticklabels(["Biology (A)", "Anthropology (B)"], fontsize=11)
axes[1].set_yticks(range(len(LIST_2_BIOLOGY)))
axes[1].set_yticklabels(LIST_2_BIOLOGY, fontsize=10)
axes[1].set_title("Biological Words\n(freq. per 10,000 tokens)", fontsize=12, fontweight='bold')
for i in range(len(LIST_2_BIOLOGY)):
    for j in range(2):
        axes[1].text(j, i, str(data2.values[i, j]), ha='center', va='center', fontsize=9, fontweight='bold')
plt.colorbar(im2, ax=axes[1])

plt.suptitle("Epistemic Silences: Systematic Lexical Absences Across Discursive Regimes",
             fontsize=14, fontweight='bold')
plt.tight_layout()

png_path = os.path.join(OUTPUT_DIR, "epistemic_silences_heatmap.png")
plt.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"✓ Heatmap salvat: {png_path}")

# --- RAPORT CONSOLĂ ---
print("\n--- EPISTEMIC SILENCES: CUVINTE ANTROPOLOGICE ---")
print(f"{'Cuvânt':<15} {'Biology (A)':>12} {'Anthropology (B)':>18} {'Ratio B/A':>10}")
print("-" * 60)
for word in LIST_1_ANTHROPOLOGY:
    a = freq_list1_a[word]
    b = freq_list1_b[word]
    ratio = round(b / a, 1) if a > 0 else "∞"
    print(f"  {word:<13} {a:>12} {b:>18} {str(ratio):>10}")

print("\n--- EPISTEMIC SILENCES: CUVINTE BIOLOGICE ---")
print(f"{'Cuvânt':<15} {'Biology (A)':>12} {'Anthropology (B)':>18} {'Ratio A/B':>10}")
print("-" * 60)
for word in LIST_2_BIOLOGY:
    a = freq_list2_a[word]
    b = freq_list2_b[word]
    ratio = round(a / b, 1) if b > 0 else "∞"
    print(f"  {word:<13} {a:>12} {b:>18} {str(ratio):>10}")

print("\n✓ Analiză epistemic silences completă.")
