# Experimental Narrative

Draft — 2026-02-15

## Three Mechanistic Analyses, One Dataset

The thesis experiments are three mechanistic analyses applied to the same captured Q/K vectors. All three are orthogonal transformations or probabilistic models over attention head internals. They differ in what quantity they compute and what question they answer.

| Analysis | Computes | Question |
|----------|----------|----------|
| Combined QK PCA | Variance decomposition, correlation with position | How is Q/K variance distributed? How much is positional? |
| Planar Rotation | Targeted axis projections, drift slopes, bias magnitude | What is the parametric form of position bias? |
| Attention Plasticity | P(query changes which key wins) | Does position bias dominate content signal in key selection? |

## PCA as Exploratory Precursor to Rotation

PCA and Rotation are both orthogonal rotations that preserve q·k exactly. The difference is what the axes are constructed to capture.

PCA maximizes variance. PC0 captures ~34% of pooled Q+K variance and is position-correlated, but it **confounds Q/K identity separation with position encoding**. The Q/K cluster offset dominates PC0, inflating r_q relative to r_k. PCA reports r_q ≈ 0.80 > r_k ≈ 0.49.

Rotation constructs axes with explicit semantic targets:
- **Axis a** (drift): direction of maximum linear covariance with position. All orthogonal directions have exactly zero position covariance (verified at 7.3e-15 residual).
- **Axis b** (separation): direction of maximum Q-K separation, constrained to b ⊥ a.

On axis a, the result reverses: **r_k ≈ 0.87 > r_q ≈ 0.74**. Keys encode position more strongly. This is a substantive correction — it changes the interpretation of how position bias enters attention scores.

Rotation provides what PCA cannot:
- A precise bias term: **bias_strength = μ_Q^a · α_K** (one scalar per head)
- Clean separation of asymmetric drift ({a,b} plane) from symmetric RoPE rotation (complement)
- Training dynamics with mechanistic specificity: α_K collapses 93% during LC fine-tuning while r_k stays at 0.90+

PCA's role in the thesis is methodological scaffolding — the exploratory discovery that motivated Rotation's targeted axis construction. Key findings (head taxonomy, training dynamics, μ_Q amplification) are restated more cleanly in Rotation's framework. PCA should be presented as the step that revealed positional dominance and Q/K separability, then superseded.

## Rotation and Plasticity: Complementary Questions

Rotation quantifies the bias. Plasticity measures whether the bias dominates.

A head can have large bias_strength and still attend flexibly if the content signal overwhelms the positional term. Conversely, modest bias_strength can dominate if content variance is small. bias_strength alone cannot determine whether attention is position-locked.

Plasticity resolves this by measuring the **competition** between position and content within the attention score difference D = q^T(k₁ - k₂). The positional and content contributions enter as competing terms. The metric 4p(t)(1-p(t)) captures who wins:

- p(t) = Φ(m(t)/√v), where m(t) contains the positional contribution and v contains content variance
- When |m/√v| >> 0: position dominates → plasticity → 0
- When |m/√v| ≈ 0: content dominates → plasticity → 1

Rotation and Plasticity are not levels. They are the same level of analysis — mechanistic — asking different questions:

- **Rotation**: what is the mechanism? (parametric, interpretable, decomposable)
- **Plasticity**: does the mechanism dominate? (scalar, integrates over all contributions, directly relevant to ECL)

When plasticity is low, Rotation tells you *why* (large bias_strength). When bias_strength is large, Plasticity tells you *whether it matters* (whether content can compensate).

## Gaps Plasticity Closes

| Gap between Rotation and ECL | How Plasticity fills it |
|------------------------------|------------------------|
| Bias magnitude ≠ bias impact | Puts bias and content on the same scale via p(t) = Φ(m/√v) |
| Per-head scalar ≠ position profile | Per-bucket plasticity reveals *where in the context* the head loses flexibility |
| Bias drops during LC training — does attention improve? | SmolLM3 checkpoints show: bias collapse recovers near-position plasticity but distant-position plasticity remains poor (ap_drop triples from 0.06 to 0.16 despite 10× bias reduction). Bias reduction is necessary but not sufficient. |
| Geometric head taxonomy (correlation thresholds) | Functional classification: does the head do query-dependent retrieval or not? |
| Single distance variable | 2D heatmaps reveal plasticity depends on both inter-key distance and query-to-key-midpoint distance — a structure invisible in 1D position profiles or per-head scalars |
| No connection to benchmarks | ap_drop separates model families in the same ordering as LongBench Pro scores; ap_last_20% tracks benchmark performance better than aggregate plasticity |

## What Plasticity Reveals: Cross-Model Results

### Plasticity is not a single number — it is a positional profile

Across 11 models from 3 families (Ministral3, Qwen3, Llama 3.2), plasticity declines monotonically with context position. But the *rate* of decline is what distinguishes families:

- **Ministral3** (3B/8B/14B): ap_drop ≈ 0.07. Near-linear, gentle decline. Flattest of all families.
- **Qwen3** (0.6B–14B): ap_drop ≈ 0.16–0.19. Steeper, accelerating in the second half. Scale helps: 14B is flatter than 0.6B.
- **Llama 3.2** (1B/3B): ap_drop ≈ 0.22–0.23. Steepest decline. All heads converge to ~0.45 past 100K.

This ordering — Ministral < Qwen < Llama — matches the LongBench Pro ranking among the 7 matched models.

### Aggregate plasticity does NOT predict benchmark performance

Ministral3-3B has the highest aggregate plasticity (0.622) but scores only 30.18 on LBP, below Qwen3-14B (0.590, scores 37.11). Cross-family comparison is confounded by base capability. Plasticity measures attention mechanics, not model quality.

The informative metrics are positional:
- **ap_drop** (first_20% − last_20%): separates families in benchmark order
- **ap_last_20%**: Llama-3.2-3B at 0.456 maps cleanly to its last-place LBP (15.71); Ministral3 at 0.57–0.59 maps to 37–40

This motivates a decomposition: benchmark performance = base capability × context preservation. Plasticity measures the second factor. Ministral3-3B is the diagnostic case — flat plasticity (good context preservation) but low LBP (limited base capability).

### Plasticity is 2D, not 1D

The 2D bucket heatmaps reveal that plasticity depends on **both** inter-key distance (separation between competing keys) and query-to-key-midpoint distance (how far the query is from the midpoint of the two keys). The 1D position profiles collapse this structure.

The geometry of the competition:
- Keys close together, far from query → content always wins (high plasticity regardless of absolute distance)
- Keys far apart, one near query → position strongly favors the nearer key (low plasticity)
- The transition between these regimes is where families diverge

Ministral3's warm heatmap (>0.55 nearly everywhere) means content wins even at 80K+ inter-key separation. Qwen3 and Llama show progressively earlier onset of the position-dominated dark zone (50K and 40K respectively).

### Head heterogeneity differs by family

Per-head plasticity profiles reveal distinct internal organization:
- **Ministral3**: tight bundle — homogeneous heads, all decline gently
- **Qwen3**: bimodal — content heads (0.8–1.0) coexist with position-locked heads (0.2–0.3)
- **Llama 3.2-3B**: wide spread that **converges at distance** — past 100K, even content-specialized heads collapse to ~0.45
- **Llama 3.2-11B / Llama 3.1-8B**: non-monotone profile with mid-context recovery zone around 60K–100K. A NoPE layer study (see `notes/experiments/06_nope_layer_study.md`) rules out cross-attention layers as the cause — Llama-3.1-8B (no NoPE layers) shows the same pattern. The recovery is a Llama-family trait at 32+ layers, distributed across nearly all self-attention layers, absent in Llama-3.2-{1B,3B} and all Ministral/Qwen models regardless of depth

### Component weights expose RoPE dimension structure

All models show the same bimodal pattern: two clusters of position-encoding dimensions (~33–70 and ~100–128) with dead zones (0–33, 73–100) carrying zero positional information. The dead-zone dimensions are pure content channels. Ministral3 concentrates positional information into narrower peaks; Qwen3 distributes it more broadly.

## What Plasticity Reveals: SmolLM3 Training Dynamics

Joint rotation + plasticity analysis across 10 SmolLM3-3B checkpoints (pre-training → LC extension to 64K) reveals:

### Bias collapse is necessary but not sufficient

**Pre-training** (4K context): bias_strength doubles (0.009 → 0.019). Plasticity drops uniformly (0.585 → 0.516). ap_drop is mild (~0.06) within the short window.

**LC extension** (4K → 32K → 64K): bias_strength collapses 10× (0.019 → 0.002). But plasticity does not recover uniformly:
- Near-position plasticity **recovers** (first_20%: 0.552 → 0.588, back to early-training levels)
- Distant-position plasticity **remains poor** (last_20%: 0.427)
- ap_drop **triples** (0.06 → 0.16)

The bias term is near zero, yet distant keys still lose the competition to nearby keys. The residual plasticity gradient, after bias is removed, reflects **content signal decay at distance** — the content component of q^T(k₁ − k₂) loses variance at distant positions, independent of positional bias.

### ap_drop decomposes into bias and content-decay components

During pre-training: ap_drop ≈ 0.06, driven by bias_strength growth.
After LC training: ap_drop ≈ 0.16, despite 10× lower bias. The excess (0.16 − 0.06 ≈ 0.10) is content-decay at distance.

This decomposition explains the cross-model ordering: SmolLM3 post-LC (ap_drop 0.16) matches Qwen3 (0.16–0.19) — both are standard LC-trained models of similar scale. Ministral3 achieves ap_drop 0.07 at comparable bias levels over 4× longer context. Whatever Ministral3's training recipe does, it maintains content signal strength at distance — not just bias reduction.

## Connecting to Benchmarks

### LongBench Pro (7 matched models)

ap_drop separates Ministral3 (~0.07) < Qwen3 (~0.17) < Llama 3.2 (0.23), matching the LBP ordering. Within Qwen3, larger models have smaller ap_drop (14B: 0.161, 4B: 0.186) and higher LBP (37.1 vs 31.3).

For Ministral3-14B (the only model with per-length LBP data from Figure 7), plasticity at each length bin correlates with LBP at that length: 0.684 → 51.88 at 8K, declining to 0.596 → 42.36 at 128K. The plasticity decline (~13%) is shallower than the LBP decline (~18%), suggesting length-independent difficulty accounts for part of the benchmark degradation.

### RULER (2 models: Llama-3.1-8B + Mistral-v0.2-7B)

RULER provides per-length scores at 6 bins (4K–128K). Two models sniffed and analyzed:

**Llama-3.1-8B** (128K full attention, RULER: 95.5→77.0): ap_drop = 0.158, matching Qwen3-range. Plasticity declines monotonically at bin level (0.729→0.506), tracking RULER decline. The decile profile shows the same non-monotone bump as Llama-3.2-11B — dip at 40–50%, recovery at 70–80% — confirming this as a Llama-family trait. Compared to Llama-3.2-3B (ap_drop 0.230), the 3.1 generation retains more plasticity at distance.

**Mistral-v0.2-7B** (32K sliding window, RULER: 93.6→13.8): ap_drop = 0.063 — the lowest of all 13 models — yet catastrophically fails on RULER at 64K (49.0) and 128K (13.8). The paradox resolves immediately: plasticity is only measured within the 32K sliding window, where attention IS flexible. The RULER failure is architectural — tokens beyond the window are unreachable.

This reveals a **fundamental limitation of plasticity**: it measures context degradation (gradual loss of attention flexibility) but not context truncation (hard architectural cutoff). Two distinct ECL failure modes:
- **Degradation**: plasticity-detectable. Llama-3.2-3B, Qwen3 models.
- **Truncation**: invisible to plasticity. Mistral-v0.2-7B.

## Open Gaps

| Gap | Description |
|-----|-------------|
| **Per-length benchmark data** | Per-length LBP scores needed for 6 of 7 matched models. |
| **Head composition** | Per-head plasticity does not capture cross-layer interaction. A low-plasticity early head feeding a high-plasticity later head may not limit model-level ECL. |
| **Causal direction** | All analyses are observational. Claiming "low plasticity causes ECL failure" requires interventions — ablating low-plasticity heads and measuring retrieval accuracy. |
| **Softmax globality** | Plasticity uses key pairs. Softmax normalizes over all keys — a head with high pairwise plasticity could still concentrate attention if many biased keys compete simultaneously. |
| **Dataset dependence** | Computed over LongBench-Pro 128K+. Stability of plasticity profiles across document types is untested. |
| **Content decay mechanism** | The residual ap_drop after bias collapse is attributed to content signal decay, but the precise mechanism (RoPE rotation accumulation? attention sink competition? feature drift?) is uncharacterized. |
| **Plasticity blind spot** | Plasticity cannot detect architectural range limits (sliding window, finite context). Mistral-v0.2-7B demonstrates this: excellent within-window plasticity, catastrophic beyond-window failure. |
