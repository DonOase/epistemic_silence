# Epistemic Silences: A Computational Analysis of the Human Body Across Discursive Regimes

**Author:** Ștefan Eduard Pârvan  
**Affiliation:** Transilvania University of Brașov, Faculty of Sociology and Communication  
**Presented at:** Convorbiri Antropologice, June 14, 2026, Cheia, Prahova  

---

## Overview

This project applies NLP methods to identify **epistemic silences** — systematic lexical absences that reveal how two institutional discourses construct the human body differently:

- **Corpus A:** Biology/anatomy textbooks (OpenStax Anatomy & Physiology)
- **Corpus B:** Cultural anthropology texts (Connerton, Ingold)

The central argument: the difference between a biology textbook and an anthropological text about the body is not stylistic — it is **epistemic**. Each discourse produces structured absences of meaning that the other can articulate. These absences are measurable through computational linguistics.

---

## Theoretical Framework

- **Ludwik Fleck** — thought style (*Denkstil*) and thought collective (*Denkkollektiv*)
- **Karl Mannheim** — relational epistemology, social situatedness of knowledge
- **Pierre Bourdieu** — epistemic field, habitus
- **Ian Hacking, Steve Fuller** — supporting references on styles of reasoning and education as epistemic institution

---

## Key Findings

### Epistemic Silences — Anthropological words absent from biology

| Word | Biology (per 10k) | Anthropology (per 10k) | Ratio |
|------|------------------|------------------------|-------|
| social | 0.15 | 31.90 | 212.7x |
| culture | 0.15 | 21.06 | 140.4x |
| experience | 1.60 | 23.29 | 14.6x |
| ritual | 0.00 | 9.09 | ∞ |
| embodiment | 0.00 | 1.38 | ∞ |
| shame | 0.00 | 0.18 | ∞ |

### Epistemic Silences — Biological words absent from anthropology

| Word | Biology (per 10k) | Anthropology (per 10k) | Ratio |
|------|------------------|------------------------|-------|
| bone | 47.00 | 0.06 | 783.3x |
| muscle | 54.77 | 0.18 | 304.3x |
| nerve | 17.30 | 0.06 | 288.3x |
| tissue | 41.38 | 0.00 | ∞ |
| enzyme | 5.17 | 0.00 | ∞ |

### Notable observation
`pain` appears more frequently in biology than in anthropology — but exclusively as a nerve signal, not as lived experience. Same word, two entirely different thought styles. This is Fleck in data.

---

## Corpus

| File | Type | Tokens |
|------|------|--------|
| OpenStax Anatomy & Physiology | Biology textbook | 330,628 |
| Connerton — How Societies Remember | Anthropology | ~28,090 |
| Ingold — The Perception of the Environment | Anthropology | ~138,063 |
| **Total** | | **496,781** |

> PDF files are not included in this repository due to copyright. Sources are freely available via OpenStax.org and academic libraries.

---

## Methods

1. **Text extraction** — pdfplumber
2. **Preprocessing** — tokenization, stopword removal (NLTK)
3. **Word frequency analysis** — Counter, pandas
4. **Epistemic silences analysis** — target wordlist frequency comparison, normalized per 10,000 tokens
5. **Visualizations** — matplotlib, seaborn (heatmap, diverging bar chart, scatter plot, word frequency)

---

## Repository Structure
