# Combined QK PCA Analysis: Positional Structure in Attention Vectors

## Purpose

This experiment applies PCA to Q and K attention vectors to quantify how much of the Q/K representational space encodes token position versus semantic content. The "combined QK PCA" uses a shared rotation matrix for Q and K, preserving q.k exactly, which makes the PCA basis the natural coordinate system for reasoning about attention scores.

## Source Code
- Repository: https://github.com/viktor-shcherb/qk-pca-analysis
- CLI: `pca-analyze` (analysis) and `pca-visualize` (scatter collages)
- Report: `qk-pca-analysis/report.html`
- Report generation: `qk-pca-analysis/scripts/generate_report_figures.py`

## Figures

All figures are stored in `figures/qk-pca/` with per-figure README descriptions. See each subdirectory for production details and interpretation.

### Cross-Model Analysis (11 models)
| # | Figure | Key insight |
|---|--------|-------------|
| 01 | PC roles bar chart | PC0 dominates: r_q~0.80, r_k~0.48 |
| 02 | r_q vs r_k scatter | Model families occupy distinct (r_q, r_k) regions |
| 03 | Layer heatmap r_q | Q-position universally high across all layers and models |
| 04 | Layer heatmap r_k | K-position varies by family: low in small Qwen3, moderate elsewhere |
| 05 | Explained variance | PC0 captures ~34% of combined QK variance |
| 06 | Collage example | Visual confirmation: two clusters (Q/K) with position gradients |

### SmolLM3-3B Training Dynamics (10 checkpoints)
| # | Figure | Key insight |
|---|--------|-------------|
| 07 | Position signal over training | r_q rises monotonically; r_k peaks then drops in LC |
| 08 | Taxonomy evolution | Position-dominated: 34% → 71% across training |
| 09 | Explained variance over training | PC0 EV jumps from 0.19 → 0.29 → 0.34 |
| 10 | Layer heatmap r_q | Q-position uniform across layers by step 1.2M |
| 11 | Layer heatmap r_k | K-position stronger in early layers, drops in LC |
| 12 | Phase portraits | Diffuse → tight cluster in position-dominated corner |

## Data

- **Input**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk` (HuggingFace Hub), captured via `qk-sniffer` (see `notes/experiments/01_qk_capture.md`)
- **Cross-model output**: `qk-pca-analysis/results/attention_plasticity/qk.csv` (32,391 rows — 11 models × ~300 heads × 10 PCs)
- **SmolLM output**: `qk-pca-analysis/results/smollm3_training_progress/qk.csv` (30,001 rows — 10 checkpoints × 300 heads × 10 PCs)

## Method

### Combined QK PCA
1. For each attention head: load Q vectors and the corresponding K vectors (derived via GQA mapping)
2. Pool Q and K into a single matrix (both ∈ R^d, where d is the head dimension)
3. Fit PCA on the pooled matrix (10 components, sklearn)
4. Project Q and K subsets separately through the shared PCA components
5. Compute Pearson r between each PC's projection and token position, independently for Q (r_q) and K (r_k)
6. The shared rotation preserves q.k exactly: (Uq)·(Uk) = q·k

### Sign Canonicalization
For each PC, orient the eigenvector so that r_q >= 0. When |r_q| < 0.05, fall back to r_k as the anchor. After canonicalization:
- r_q >= 0 always — its magnitude is Q-position signal strength
- The **sign** of r_k becomes meaningful: positive = concordant (Q and K position gradients aligned), negative = discordant

### Head Taxonomy
Based on PC0 sign-canonicalized r_q and |r_k|, with thresholds at 0.7 (high) and 0.3 (low):
- **Position-dominated**: r_q > 0.7, |r_k| > 0.7
- **Q-positional**: r_q > 0.7, |r_k| < 0.3
- **K-positional**: r_q < 0.3, |r_k| > 0.7
- **Content-focused**: r_q < 0.3, |r_k| < 0.3
- **Mixed**: everything else

## Models

### Cross-Model Analysis
| Model | Family | Layers | Q Heads | GQA Ratio |
|-------|--------|--------|---------|-----------|
| qwen3-0.6b | Qwen3 | 28 | 300 | 2 |
| qwen3-1.7b | Qwen3 | 28 | 300 | 2 |
| qwen3-4b | Qwen3 | 36 | 300 | 4 |
| qwen3-8b | Qwen3 | 36 | 300 | 4 |
| qwen3-14b | Qwen3 | 40 | 300 | 4 |
| llama3.2-1b | Llama 3.2 | 16 | 300 | 4 |
| llama3.2-3b | Llama 3.2 | 28 | 300 | 4 |
| llama3.2-11b | Llama 3.2 | 32 | 239 | 4 |
| ministral3-3b | Ministral3 | 26 | 300 | 4 |
| ministral3-8b | Ministral3 | 34 | 300 | 4 |
| ministral3-14b | Ministral3 | 40 | 300 | 4 |

### SmolLM3-3B Training Checkpoints
See `notes/experiments/02_smollm3_checkpoints.md` for full details. 10 checkpoints spanning stage 1 pre-training through 32K→64K long-context fine-tuning.

---

## Key Findings

### Finding 1: ~25% of Q+K Variance Is Linear in Position

The single most striking result. Across all 11 models:
- **27% of total Q-vector variance** is explained by a linear function of token position (sum of EV_i × r²_q,i across PCs 0-9)
- **14% of total K-vector variance** is linear in position
- **PC0 alone accounts for ~90% of this positional variance** in Q and ~74% in K

This means roughly a quarter of the entire Q+K representational space — hundreds of dimensions of floating-point vectors — collapses to a single number: token position. The rest (~75%) encodes content (semantic information).

Per-model variation:
| Model | Q position variance | K position variance |
|-------|-------------------|-------------------|
| Small Qwen3 (0.6b, 1.7b) | ~32% | ~9% |
| Large Qwen3 (4b, 8b, 14b) | ~24% | ~14% |
| Llama 3.2 | ~31% | ~20% |
| Ministral3 | ~23% | ~11% |

### Finding 2: Q and K Are Linearly Separable on PC0

In the combined PCA space, Q and K vectors form two cleanly separable clusters:
- Fisher discriminant on PC0: ~44
- Linear classification accuracy (PC0+PC1): 98.5-100%
- Mean Q/K cluster separation on PC0: ~47 units

PC0 simultaneously encodes (a) Q/K identity and (b) token position. This dual role is why PC0 captures such high variance (~34%).

### Finding 3: The μ_Q Amplification Mechanism

Because the combined PCA preserves q.k exactly, the attention score decomposes as q.k = Σ_i q'_i × k'_i. On PC0:

- q'_0(i) ≈ μ_Q + α·i + ε_i  (Q cluster mean + position slope + content)
- k'_0(j) ≈ μ_K + β·j + η_j  (K cluster mean + position slope + content)

The product q'_0 × k'_0 contains a term **μ_Q · β·j** — the Q cluster mean amplifies the K-position gradient. Even moderate r_k (~0.48) produces a large attention-score bias when multiplied by |μ_Q| ~ 20-30 units.

**This is the mechanistic origin of position bias.** The model doesn't need explicit position-biased attention; it emerges from the geometry of the Q/K embedding space.

### Finding 4: Head Taxonomy

Grand totals across 11 models (3,239 heads):
| Category | Fraction | Description |
|----------|----------|-------------|
| Mixed | 55.4% | Moderate position in Q and/or K |
| Position-dominated | 26.6% | Strong position in both Q and K |
| Q-positional | 14.2% | Strong Q-position, weak K-position |
| Content-focused | 3.8% | Weak position in both |
| K-positional | <0.1% | Strong K-position, weak Q-position |

Model-family differences:
- **Llama 3.2**: Highest position-dominated (38-50%), lowest mixed (46-52%)
- **Qwen3 large**: Similar to Llama (37-39% position-dominated)
- **Qwen3 small**: Few position-dominated (5-7%), high Q-positional (39%)
- **Ministral3**: Overwhelmingly mixed (77-84%), moderate position-dominated (8-19%)

### Finding 5: Positional Structure Emerges Rapidly During Training

SmolLM3-3B training dynamics:
- r_q jumps from 0.67 to 0.81 within first 1.2M steps (first third of stage 1)
- Content-focused heads collapse from 11% to <1% in the same period
- Position-dominated heads grow from 34% to 55%
- The positional structure is essentially established within the first third of pre-training

### Finding 6: Long-Context Fine-Tuning Reshapes Q/K Asymmetry

During LC training (4K→32K→64K):
- r_q continues climbing: 0.81 → 0.87
- r_k **drops**: 0.54 → 0.46
- PC0 explained variance increases: 0.29 → 0.34
- Position-dominated heads jump: 58% → 71%

The asymmetry suggests the model strengthens Q-position encoding while partially decoupling K from position. This may increase attention plasticity: if K vectors carry less position and more content, the attention pattern becomes more query-dependent (the definition of high plasticity).

---

## Connection to Thesis: Effective Context Length

### Position bias as the dominant ECL failure mode

The μ_Q amplification mechanism (Finding 3) provides a precise mechanistic explanation for why position bias is so strong in transformer attention. The bias is not an incidental artifact — it's a first-order term in the attention score decomposition, amplified by the large Q/K cluster separation. This connects to the related work's evidence on attention sinks, cumulative context probability convergence, and position-bias interventions (STRING, PINE).

### Plasticity prediction from PCA

The head taxonomy (Finding 4) directly predicts attention plasticity:
- **Position-dominated heads** → low plasticity (position determines attention regardless of query content)
- **Content-focused heads** → high plasticity (attention depends on query-key semantic similarity)
- **Q-positional heads** → intermediate (position affects which queries attend where, but keys don't have position bias)

The taxonomy can thus serve as a PCA-based proxy for plasticity, computable from the same sniffed Q/K vectors without needing the full plasticity calculation.

### Why long-context training improves ECL

Finding 6 suggests a specific mechanism: long-context fine-tuning increases PC0 explained variance (stronger low-rank structure) while decoupling K from position (r_k drops). This combination:
1. Makes the Q/K separation cleaner (higher Fisher discriminant)
2. Frees K vectors to encode more content
3. Potentially increases plasticity by making attention less position-determined

This predicts that models with more long-context fine-tuning should show higher plasticity and better ECL — a testable hypothesis.

### Positional overhead as an ECL metric

The "~25% positional variance" finding (Finding 1) suggests a clean scalar metric: **positional overhead** = fraction of Q+K variance attributable to linear position. Models or heads with higher positional overhead have less capacity for content-based attention, potentially limiting their effective context utilization. Tracking this metric across checkpoints or interventions could complement behavioral ECL benchmarks with a mechanistic quantity.

### Training dynamics and context extension

The rapid emergence of positional structure (Finding 5) — content-focused heads nearly vanish within the first third of training — suggests that the model quickly converges to a positional encoding strategy that may be difficult to modify later. Context extension methods (PI, YaRN, RoPE theta scaling) modify the positional signal but cannot easily reallocate the ~25% of variance already committed to position. This may explain why context extension gains don't reliably transfer to hard reasoning tasks: the underlying positional overhead persists.
