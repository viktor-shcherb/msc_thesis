# Chapter 6: Results

Draft — 2026-02-15

## Purpose

The largest chapter. Present findings organized by research question, not by analysis method. Each section builds on the previous: discover the bias geometry → measure its functional consequence → trace its development → validate against benchmarks.

---

## 6.1 — Position Bias Geometry (RQ1)

**~6–7 pages**

### Research question

*What is the geometric structure of position bias in attention heads?*

### Narrative arc

PCA reveals that position is the dominant source of Q/K variance and that models cluster by family. But PCA's axes conflate position encoding with Q/K identity, producing a misleading asymmetry (r_q > r_k). Rotation corrects this by constructing semantically targeted axes, revealing that keys encode position more strongly than queries — and that position bias has a precise parametric form.

### Section structure

#### 6.1.1 — PCA reveals positional dominance

**Key claims:**
- PC0 captures ~34% of combined Q+K variance, far exceeding subsequent components. Roughly 25% of total Q+K variance is linear in token position.
- On PC0, queries show stronger position correlation than keys (r_q ≈ 0.80 vs r_k ≈ 0.49) — but this is misleading (foreshadow).
- Head taxonomy: 26.6% position-dominated, 14.2% Q-positional, 3.8% content-focused, 55.4% mixed. Most heads carry some positional structure.
- Families cluster distinctly in (r_q, r_k) space: Llama top-right, small Qwen Q-positional, Ministral moderate-mixed.

**Figures:**
- `qk-pca/01_pc_roles` — **Figure 6.1.** Grouped bar chart: position correlation across PCs for 11 models. Visual: PC0 tower dwarfs everything else. Caption emphasizes the ~25% variance finding.
- `qk-pca/02_rq_vs_rk_scatter` — **Figure 6.2.** Scatter of r_q vs r_k on PC0, colored by family. Visual: three distinct clusters. Caption notes the apparent r_q > r_k asymmetry that will be corrected.

**Transition:** "PCA's dominant principal component conflates two sources of structure: position encoding and Q/K identity separation. The high r_q on PC0 partly reflects the Q cluster mean aligning with the position gradient direction, not a genuine asymmetry in position encoding strength. To disentangle these, we construct a rotation with axes targeted at specific geometric quantities."

#### 6.1.2 — Rotation isolates the bias mechanism

**Key claims:**
- On the drift axis a (maximum position covariance), the asymmetry reverses: r_k ≈ 0.87 > r_q ≈ 0.74. Keys encode position more strongly than queries. This is a substantive correction — it changes which vector carries the position signal.
- The {a, b} plane captures ~30–43% of variance (comparable to PCA's top 2 PCs) but with guaranteed semantic meaning.
- Bias has a precise parametric form: bias_strength = μ_Q^a × α_K. One interpretable scalar per head.
- 99.0% of heads show positive bias_strength (recency bias). Only 31/3,239 heads show primacy bias.
- Simpson's paradox: overall correlation between bias and separation is +0.48, but within-family Llama reverses to −0.65. Families have genuinely different bias-separation trade-offs.

**Figures:**
- `qk-rotation/01_ab_plane_collage` — **Figure 6.3.** The {a, b} plane scatter for one model (Llama 3.2-3B). Q and K clusters with position gradients. Caption: "unlike PCA, both axes have guaranteed geometric meaning."
- `qk-rotation/02_rq_rk_drift_bars` — **Figure 6.4.** Bar chart of |r_q| and |r_k| on axis a across 11 models. Visual: K bars consistently taller than Q bars — the reversal. Place near or reference PCA's Figure 6.1 for contrast.
- `qk-rotation/04_bias_strength` — **Figure 6.5.** Histogram of bias_strength across families. Visual: 99% positive, tight distributions. Caption emphasizes universality of recency bias.
- `qk-rotation/07_bias_vs_separation` — **Figure 6.6.** Scatter showing Simpson's paradox. Caption highlights the within-Llama reversal.

**Transition:** "Rotation quantifies the bias mechanism — how much positional preference enters each head's attention score. But a large bias does not necessarily constrain attention: if content signal is strong, the query can still attend to semantically relevant keys regardless of position. The next question is functional: does position bias actually dominate content signal?"

#### Summary of appendix figures for 6.1

- `qk-pca/05_explained_variance` → Appendix (PC0 = 34% stated in text)
- `qk-pca/03_layer_heatmap_rq` → Appendix (r_q uniformity stated in text)
- `qk-pca/04_layer_heatmap_rk` → Appendix (r_k heterogeneity stated in text)
- `qk-pca/06_collage_example` → Appendix (the PCA-frame scatter; rotation collage preferred in main text)
- `qk-rotation/03_variance_decomposition` → Appendix (~38% stated in text)
- `qk-rotation/05_slope_ratio` → Appendix (K drifts 1.8× faster; detail)
- `qk-rotation/06_layer_heatmaps` → Appendix (layer-depth bias; supporting)
- `qk-rotation/08_complement_collage` → Appendix (RoPE donut rings; beautiful but tangential)

---

## 6.2 — Plasticity Profiles (RQ2)

**~5–6 pages**

### Research question

*Does position bias constrain what the model can attend to at long distances?*

### Narrative arc

Plasticity declines with context position for all models, but the *rate* of decline is what distinguishes families. The key insight is that plasticity is a positional profile, not a scalar — aggregate plasticity is misleading. The 2D heatmaps reveal hidden structure: plasticity depends on both inter-key distance and query-to-key-midpoint distance. Head-level heterogeneity further distinguishes architectural strategies.

### Section structure

#### 6.2.1 — Plasticity declines with position; the rate separates families

**Key claims:**
- All 11 models show monotonic plasticity decline across context.
- ap_drop ordering: Ministral (~0.07) < Qwen (~0.17) < Llama (0.23). This ordering is consistent within families and across families.
- Aggregate plasticity does NOT predict performance: Ministral-3B has the highest aggregate (0.622) but scores only 30.18 on LBP. The aggregate confounds attention mechanics with base capability.
- The informative metrics are positional: ap_drop and ap_last_20%.

**Tables:**
- **Table 6.1:** Decile plasticity profile (from notes Table 4). All 11 models, 10 position bins. The quantitative backbone.
- **Table 6.2:** Per-length-bin plasticity (from notes Table 2). 7 LBP-matched models, 5 length bins.

**No figure in this subsection** — the tables carry the argument. The figures come in the next two subsections where visual evidence is stronger than numbers.

#### 6.2.2 — 2D geometry: plasticity depends on two distances

**Key claims:**
- The 2D bucket heatmaps reveal that the 1D position profiles collapse essential structure. Plasticity is a function of BOTH inter-key distance and query-to-key-midpoint distance.
- Keys close together, far from query → content always wins (high plasticity regardless of absolute distance).
- Keys far apart, one near query → position strongly favors the nearer key (low plasticity).
- The transition between these regimes is where families diverge:
  - Ministral: warm (>0.55) nearly everywhere. Dark corner confined to >90K inter-key distance.
  - Qwen: clear diagonal gradient. Dark region starts at ~50K. Architecture-determined shape nearly identical across 0.6B–14B.
  - Llama-3B: most extreme contrast. Dark zone starts at ~40K, reaches <0.2 in extreme corner.
  - Llama-11B: non-smooth. Dark patches at specific distances + recovery zone around 57K–65K. NoPE layer interference.

**Figures:**
- `attention-plasticity/01-04 bucket heatmaps` — **Figure 6.7.** Combined 2×2 figure: Ministral-14B, Qwen-14B, Llama-3B, Llama-11B. This is arguably the most visually striking result in the thesis. Caption highlights the family contrast and the Llama-11B anomaly.

#### 6.2.3 — Head heterogeneity reveals architectural strategies

**Key claims:**
- Ministral: tight bundle. Low inter-head variance. All heads decline gently. Homogeneous architecture — every head contributes similarly to content-based retrieval.
- Qwen: bimodal. Content-specialized heads (0.8–1.0) coexist with position-locked heads (0.2–0.3). Heterogeneous specialization — some heads do retrieval, others encode structure.
- Llama-3B: wide spread that converges at distance. Past 100K, ALL heads cluster at ~0.45. Position eventually dominates every head, even initially plastic ones.
- Llama-11B: non-monotone profile with mid-context recovery. Distinctive among all models.

**Figures:**
- `attention-plasticity/05-07 profiles` — **Figure 6.8.** Combined 1×3 figure: Ministral-3B (tight bundle), Qwen-4B (bimodal), Llama-3B (convergent). Gray per-head traces with red mean. Caption: three qualitatively different internal organizations.

**Transition:** "The cross-model results provide a static picture of how different training recipes and architectures shape attention geometry. To understand how this geometry develops — and whether the position bias mechanisms we observe are intrinsic to the architecture or emerge during training — we next trace a single model across its training trajectory."

#### Summary of appendix figures for 6.2

- `attention-plasticity/04_bucket_heatmap_llama3.2_11b` → could stay in main (part of 2×2) OR be pulled out as a separate appendix figure with extended discussion of NoPE interference. Decision: keep in the 2×2 composite for contrast, but add appendix discussion.
- `attention-plasticity/08_component_weights_qwen3_14b` → Appendix. The bimodal RoPE dimension structure is interesting but tangential. Mention in text: "the positional information concentrates in two clusters of embedding dimensions (see Appendix X), reflecting RoPE's rotation structure."

---

## 6.3 — Training Dynamics (RQ3)

**~5–6 pages**

### Research question

*How do position bias and its consequences evolve during training?*

### Narrative arc

Three temporal phases with distinct mechanistic signatures. Pre-training: position structure emerges rapidly, bias grows, plasticity declines uniformly. LC extension: bias collapses dramatically, but plasticity doesn't fully recover — near-position flexibility returns while distant-position flexibility remains poor. The punchline: bias reduction is necessary but not sufficient.

This section integrates all three analyses on SmolLM3, following the temporal axis rather than the analysis-method axis.

### Section structure

#### 6.3.1 — Position structure emerges early

**Key claims:**
- PCA: r_q jumps from 0.67 to 0.82 within the first 1.2M steps. r_k increases more gradually.
- Head taxonomy evolves rapidly: position-dominated heads grow from 34% to 55% within stage 1. Content-focused heads virtually disappear.
- By step 1.2M, the structural fingerprint (which heads are positional, which are mixed) is largely set. Subsequent pre-training refines but doesn't restructure.

**Figures:**
- `qk-pca/08_smollm_taxonomy_evolution` — **Figure 6.9.** Stacked bar chart of head category fractions across training. Visual: rapid specialization in early training, consolidation during LC.
- `qk-pca/12_smollm_rq_rk_scatter_grid` — **Figure 6.10.** 2×3 scatter grid (r_q vs r_k) at six checkpoints. Visual: diffuse cloud → tight position-dominated cluster, with two discrete jumps.

#### 6.3.2 — Bias grows during pre-training, collapses during LC extension

**Key claims:**
- Pre-training: bias_strength doubles (0.009 → 0.019), driven by α_K growth. The model learns to encode position in key vectors.
- LC extension onset (4K→32K): bias_strength collapses 6× in the first 4K steps. Further halving during 32K→64K extension. Total: 10× reduction.
- The collapse mechanism: α_K (key drift slope) drops 93%, while r_k (key position correlation) holds at 0.90+. Keys still encode position with high fidelity, but the slope of the encoding flattens — position information becomes more uniform across keys.
- Simultaneously, μ_Q^a increases 43% and separation_strength increases 14%. Q/K become MORE geometrically distinct during LC extension, not less.

**Figures:**
- `qk-rotation/09_smollm_trajectory` — **Figure 6.11.** Four-panel bar chart tracking rotation metrics across training. Visual: stable r_k, jumping separation, collapsing bias_strength.
- `qk-rotation/10_smollm_bias_decomposition` — **Figure 6.12.** Three-panel decomposition: μ_Q^a (up), α_K (down), product (down). Visual: α_K collapse dominates.

**Table:**
- **Table 6.3:** Joint rotation + plasticity trajectory (from notes Table 5). All 10 checkpoints with rotation and plasticity metrics.

#### 6.3.3 — Bias collapse is necessary but not sufficient

**Key claims:**
- Near-position plasticity (first_20%) recovers from 0.552 to 0.588 during LC extension — back to early stage 1 levels. Bias reduction works locally.
- Distant-position plasticity (last_20%) plummets to 0.427 — far below the 0.57 the model achieved at 3.5K–4K during pre-training at comparable bias levels.
- ap_drop triples from 0.06 to 0.16 despite 10× bias collapse. The plasticity gradient STEEPENS as the context window grows.
- The excess ap_drop (0.16 − 0.06 ≈ 0.10) reflects content signal decay at distance — after bias is nearly zeroed, content variance in the complement subspace loses strength at distant positions, so even minimal positional bias dominates.
- Decomposition: ap_drop ≈ bias_component + content_decay_component.

**Figures:**
- `attention-plasticity/09_smollm_plasticity_trajectory` (NEW — to be generated) — **Figure 6.13.** Line plot with three traces: ap_first_20%, ap_last_20%, ap_drop across 10 checkpoints. Visual: near-position recovers, distant-position stagnates, gap widens. This is the "necessary but not sufficient" figure.

**Table:**
- **Table 6.4:** Per-position plasticity during LC extension (from notes Table 7). Shows the position-by-position divergence.

**Transition:** "The training dynamics show that position bias is only one factor governing attention flexibility. Do these mechanistic metrics — measured on internal Q/K geometry — predict how models actually perform on long-context tasks?"

#### Summary of appendix figures for 6.3

- `qk-pca/07_smollm_position_signal` → Appendix (r_q/r_k trajectories; summarized by 12's scatter grid)
- `qk-pca/09_smollm_explained_variance` → Appendix (PC0 variance jump is one number)
- `qk-pca/10_smollm_layer_heatmap_rq` → Appendix (r_q uniformity can be stated)
- `qk-pca/11_smollm_layer_heatmap_rk` → Appendix (r_k layer dynamics; supporting)

---

## 6.4 — Benchmark Validation (RQ4)

**~3–4 pages**

### Research question

*Do mechanistic metrics predict behavioral long-context performance?*

### Narrative arc

ap_drop separates model families in the same ordering as LongBench-Pro scores. Aggregate plasticity fails as a predictor because it conflates attention mechanics with base model capability. This motivates a decomposition: benchmark performance ≈ base capability × context preservation. Plasticity measures the second factor.

### Section structure

#### 6.4.1 — ap_drop predicts LongBench-Pro ordering

**Key claims:**
- Across families: ap_drop separates Ministral (~0.07, LBP 30–40) < Qwen (~0.17, LBP 31–37) < Llama (0.23, LBP 16). The ordering matches.
- Within Qwen: monotonic — 14B (ap_drop 0.161, LBP 37.1) > 8B (0.178, 33.4) > 4B (0.186, 31.3). Larger models degrade less and score higher.
- Within Ministral: nearly flat ap_drop across scales (0.068–0.082). LBP varies with scale (30–40), suggesting capability not context drives the within-family ranking.
- ap_last_20% also tracks: Llama-3B at 0.456 (last) maps to LBP 15.71 (last). Ministral at 0.57–0.59 maps to 37–40.

**Tables:**
- **Table 6.5:** The full 7-model comparison (from notes Table 1). LBP Overall, bias_strength, plasticity, ap_first_20%, ap_last_20%, ap_drop, family.

**Figures:**
- `attention-plasticity/10_apdrop_vs_lbp_scatter` (NEW — to be generated) — **Figure 6.14.** Scatter plot: ap_drop (x) vs LBP Overall (y), 7 points colored by family. Simple, definitive. The visual evidence for the ordering claim. Ministral-3B sits off the regression line (low ap_drop, low LBP), motivating the next subsection.

#### 6.4.2 — Base capability vs. context preservation

**Key claims:**
- Ministral-3B is the diagnostic case: ap_drop 0.072 (comparable to 14B) but LBP only 30.18. Flat plasticity profile means good context preservation, but low LBP means limited base capability at 3B scale.
- Aggregate plasticity (0.622, highest of all) fails to predict LBP because it doesn't separate these two factors.
- This motivates the decomposition: LBP ≈ f(base_capability) × g(context_preservation). Plasticity metrics capture g, not f.
- Within a family (controlled base architecture), ap_drop correlates with LBP. Across families, the base capability confound must be controlled for.

#### 6.4.3 — Per-length correspondence

**Key claims:**
- For Ministral-14B (the only model with per-length LBP from Figure 7): plasticity at each length bin correlates with LBP at that length.
  - 8K: plasticity 0.684, LBP 51.88
  - 128K: plasticity 0.596, LBP 42.36
- Plasticity decline (~13%) is shallower than LBP decline (~18%). The gap reflects length-independent task difficulty — some tasks are harder regardless of context length.
- SmolLM3 post-LC (ap_drop 0.16) matches Qwen-3 models (0.16–0.19) at comparable scale and similar LC training recipes. Ministral-3 achieves 0.07 at comparable bias levels — whatever its training recipe does, it goes beyond standard bias reduction.

**Tables:**
- **Table 6.6:** Ministral-14B per-length LBP vs plasticity (from notes Table 3).

---

## Figure inventory for Chapter 6

### Main text (14–15 figures + tables)

| Figure | Source | Section | Type |
|--------|--------|---------|------|
| 6.1 | qk-pca/01_pc_roles | 6.1.1 | Single |
| 6.2 | qk-pca/02_rq_vs_rk_scatter | 6.1.1 | Single |
| 6.3 | qk-rotation/01_ab_plane_collage | 6.1.2 | Single |
| 6.4 | qk-rotation/02_rq_rk_drift_bars | 6.1.2 | Single |
| 6.5 | qk-rotation/04_bias_strength | 6.1.2 | Single |
| 6.6 | qk-rotation/07_bias_vs_separation | 6.1.2 | Single |
| 6.7 | attention-plasticity/01-04 heatmaps | 6.2.2 | Composite 2×2 |
| 6.8 | attention-plasticity/05-07 profiles | 6.2.3 | Composite 1×3 |
| 6.9 | qk-pca/08_smollm_taxonomy_evolution | 6.3.1 | Single |
| 6.10 | qk-pca/12_smollm_rq_rk_scatter_grid | 6.3.1 | Single |
| 6.11 | qk-rotation/09_smollm_trajectory | 6.3.2 | Single |
| 6.12 | qk-rotation/10_smollm_bias_decomposition | 6.3.2 | Single |
| 6.13 | attention-plasticity/09_smollm_trajectory (NEW) | 6.3.3 | Single |
| 6.14 | attention-plasticity/10_apdrop_vs_lbp (NEW) | 6.4.1 | Single |

### Appendix

| Figure | Source | Notes |
|--------|--------|-------|
| A.1 | qk-pca/05_explained_variance | PC0 = 34% |
| A.2 | qk-pca/06_collage_example | PCA-frame scatter |
| A.3 | qk-pca/03_layer_heatmap_rq | r_q layer uniformity |
| A.4 | qk-pca/04_layer_heatmap_rk | r_k layer heterogeneity |
| A.5 | qk-rotation/03_variance_decomposition | {a,b} plane = ~38% |
| A.6 | qk-rotation/05_slope_ratio | K drifts 1.8× faster |
| A.7 | qk-rotation/06_layer_heatmaps | Layer-depth bias |
| A.8 | qk-rotation/08_complement_collage | RoPE donut rings |
| A.9 | attention-plasticity/08_component_weights | RoPE dimension structure |
| A.10 | qk-pca/07_smollm_position_signal | r_q/r_k training trajectories |
| A.11 | qk-pca/09_smollm_explained_variance | PC0 variance during training |
| A.12 | qk-pca/10_smollm_layer_heatmap_rq | SmolLM3 r_q layers |
| A.13 | qk-pca/11_smollm_layer_heatmap_rk | SmolLM3 r_k layers |

### Tables in main text

| Table | Section | Content |
|-------|---------|---------|
| 6.1 | 6.2.1 | Decile plasticity profile (11 models × 10 bins) |
| 6.2 | 6.2.1 | Per-length-bin plasticity (7 models × 5 bins) |
| 6.3 | 6.3.2 | Joint rotation + plasticity trajectory (10 checkpoints) |
| 6.4 | 6.3.3 | Per-position plasticity during LC extension |
| 6.5 | 6.4.1 | 7-model LBP + mechanistic metrics comparison |
| 6.6 | 6.4.3 | Ministral-14B per-length LBP vs plasticity |
