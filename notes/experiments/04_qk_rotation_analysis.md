# Planar Rotation Analysis: Disentangling Position from Content in R^d

## Purpose

This experiment constructs a 2D rotation model for Q/K vectors directly in the original R^d embedding space (no PCA). Instead of finding directions of maximum variance, it finds directions with specific geometric meaning: one that captures all linear position covariance, and one that maximally separates Q from K. This yields a precise parametric model for the attention score contribution of the 2D plane, with interpretable parameters that quantify recency bias, position encoding strength, and Q/K separation.

## Source Code
- Repository: https://github.com/viktor-shcherb/qk-rotation
- CLI: `rotate-analyze` (analysis) and `rotate-visualize` (scatter collages, complement collages)
- Report: `qk-rotation/report.html`
- Report generation: `qk-rotation/scripts/generate_report.py`

## Figures

All figures are stored in `figures/qk-rotation/` with per-figure README descriptions.

### Cross-Model Analysis (11 models)
| # | Figure | Key insight |
|---|--------|-------------|
| 01 | {a,b} plane collage | Q/K separated on b, position gradient on a |
| 02 | r_q vs r_k on drift axis | K encodes position more strongly than Q (reverses PCA finding) |
| 03 | Variance decomposition | 2D plane captures ~38% of total variance |
| 04 | Bias strength distribution | 99% of heads have positive (recency) bias |
| 05 | K-to-Q drift slope ratio | Keys drift 1.8x faster than queries |
| 06 | Layer-depth heatmaps | Early layers encode position more strongly |
| 07 | Bias vs separation (Simpson's) | Within-family correlations reverse the overall trend |
| 08 | Complement collage | RoPE rotation planes visible as donuts in d-2 complement |

### SmolLM3-3B Training Dynamics (10 checkpoints)
| # | Figure | Key insight |
|---|--------|-------------|
| 09 | Training trajectory | Bias collapses 91% during LC; separation strengthens |
| 10 | Bias decomposition | alpha_K collapse drives bias reduction; mu_Q^a grows |

## Data

- **Input**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk` (HuggingFace Hub), captured via `qk-sniffer`
- **Cross-model output**: `qk-rotation/results/rotation/rotated.csv` (3,239 rows — 11 models x ~300 heads)
- **SmolLM output**: `qk-rotation/results/smollm3_training_progress/rotated.csv` (3,000 rows — 10 checkpoints x 300 heads)

## Method

### The 2D Rotation Model

For each attention head, construct two orthonormal axes in R^d:

1. **Axis a (drift/position)**: a proportional to Cov(X, t), where X is the pooled Q+K matrix and t is token position. By the **Orthogonal Drift Alignment Lemma**, this direction captures *all* linear position covariance — every direction perpendicular to a has exactly zero covariance with position.

2. **Axis b (separation)**: b = argmax E[(b^T delta)^2] subject to b perpendicular to a, where delta = q - k. This is the top eigenvector of the projected difference covariance (I - aa^T) C_delta (I - aa^T).

### Orthogonal Drift Alignment Lemma

If a proportional to Cov(X, t) = (1/N) X_centered^T t_centered, then for any unit vector v perpendicular to a: Cov(v^T X, t) = 0 exactly.

Proof: Cov(v^T X, t) = v^T Cov(X, t) = v^T (||c|| * a) = ||c|| * (v^T a) = 0.

This is verified empirically: max residual_pos_r = 7.3e-15 across all 3,239 heads.

### Parametric Attention Score Model

Projecting Q and K onto {a, b} gives:

```
q_a(i) = mu_Q^a + alpha_Q * i + epsilon_Q^a(i)
k_a(j) = mu_K^a + alpha_K * j + epsilon_K^a(j)
q_b(i) = mu_Q^b + epsilon_Q^b(i)     [zero position covariance]
k_b(j) = mu_K^b + epsilon_K^b(j)     [zero position covariance]
```

The attention score contribution from the 2D plane:

```
s_2D(i,j) = [mu_Q^a * mu_K^a + mu_Q^b * mu_K^b]   (constant)
           + mu_Q^a * alpha_K * j                     (KEY-POSITION BIAS)
           + alpha_Q * mu_K^a * i                     (query-position term)
           + alpha_Q * alpha_K * i*j                   (interaction)
           + content terms
```

The **dominant position bias term** is mu_Q^a * alpha_K * j. We call this product **bias_strength**.

### Metrics Computed Per Head

| Metric | Description |
|--------|-------------|
| position_r | \|corr(a^T x_pooled, position)\| |
| omega, omega_r_squared | Rotation frequency and R^2 of sinusoidal fit |
| r_q_a, r_k_a | Separate Q/K position correlations on axis a |
| alpha_q, alpha_k | Regression slopes: a^T x = alpha * pos + const |
| separation_strength | E[(b^T delta)^2] / E[\|\|delta\|\|^2] |
| var_frac_a, var_frac_b | Variance fractions along a and b |
| plane_var_fraction | Total variance in {a,b} / total variance |
| residual_pos_r | Max \|corr\| of position with any complement direction |
| mu_q_a, mu_k_a, mu_q_b, mu_k_b | Cluster means on axes |
| bias_strength | mu_Q^a * alpha_K (sign-invariant recency bias) |
| content_var_b | Mean within-class variance on b (semantic capacity) |

## Models

Same 11 models and 10 SmolLM3-3B checkpoints as the PCA analysis (see `03_qk_pca_analysis.md`).

---

## Key Findings

### Finding 1: K Encodes Position More Strongly Than Q (Reversal of PCA)

On the drift axis a: mean |r_k| = 0.87, mean |r_q| = 0.74. This **reverses** the PCA finding (where r_q > r_k on PC0). The reversal occurs because PCA's PC0 aligns with maximum total variance (dominated by Q/K cluster separation), while the drift axis aligns with position covariance specifically. K vectors project more linearly onto the position-covariance direction.

Additionally, keys drift faster: median |alpha_K| / |alpha_Q| = 1.83. The K drift slope is the primary driver of recency bias through the mu_Q^a * alpha_K term.

### Finding 2: Universal Recency Bias

99.0% of all 3,239 heads have positive bias_strength (mu_Q^a * alpha_K > 0), meaning later key positions receive systematically higher attention scores. Only 31 heads show negative (primacy) bias.

The mechanism: axis a is oriented so that projection increases with position. Since Q vectors project positively on a (mu_Q^a > 0 in 98.7% of heads) and K projections also increase with position (alpha_K > 0), the product mu_Q^a * alpha_K * j grows with key position j.

### Finding 3: 2 Dimensions Capture ~38% of Variance

The {a, b} plane captures 38% of total Q+K variance on average (range: 29-46%). Axis b (separation) consistently accounts for more variance than axis a (drift) in 88% of heads. The remaining ~62% is spread across d-2 complement dimensions.

### Finding 4: The Complement Contains RoPE Rotation Planes

The complement of {a, b} has **exactly zero linear position covariance** (lemma verified). But it contains strong *non-linear* position structure: donut/ring patterns in SVD pairs where angle theta = atan2(SVD_{2i+1}, SVD_{2i}) correlates with position at |angle_r| up to 1.0.

These are **RoPE rotation planes** — pairs of dimensions where RoPE applies the same 2D rotation to both Q and K. Since the rotation is shared, Q and K are indistinguishable on these rings (~50% classification accuracy). Across models, 18-29 of 30 SVD pairs per head are active rotation planes, capturing 44-89% of complement variance.

**Interpretation**: The {a, b} plane captures the *asymmetric drift* — the component of RoPE's effect that differs between Q and K (via W_Q and W_K). The complement captures the *symmetric rotation* — the component shared identically between Q and K. Shared rotations cancel in q^T k up to the relative rotation cos(theta_i - theta_j), contributing relative-position encoding. The {a, b} plane contributes absolute-position bias.

### Finding 5: Simpson's Paradox in Bias vs Separation

Overall correlation between bias_strength and separation_strength is +0.48, but within Llama 3.2 it reverses to -0.65. High-bias Llama heads have low separation; high-bias Qwen heads have high separation. Ministral3 shows no correlation. Any pooled cross-family analysis would reach the wrong conclusion.

### Finding 6: Bias Collapse During Long-Context Training

SmolLM3-3B training dynamics reveal three phases:

1. **Rapid initialization (<1M steps)**: The 2D geometry bootstraps rapidly. |r_k| = 0.86 at step 40k. mu_Q^a doubles, bias_strength grows +75%.

2. **Pre-training plateau (1M-4.7M steps)**: Metrics stabilize. The model has found its equilibrium geometry for short-context language modeling.

3. **Long-context fine-tuning**: Dramatic restructuring:
   - **bias_strength drops 91%** (19.4 -> 1.8 x10^3)
   - Driven by **alpha_K collapsing 93%** (4.08 -> 0.27 x10^3)
   - mu_Q^a *increases* +43% (4.65 -> 6.64) — would push bias up, but alpha_K collapse overwhelms
   - |r_k| stays near-perfect (0.918 -> 0.905) — drift *direction* preserved, *slope* flattened
   - separation_strength increases +10%, plane_var_fraction increases +14%

The model flattens the drift slopes while preserving the drift direction and strengthening Q/K separation. It learns to maintain position awareness for relative-position attention (via RoPE's symmetric component) while eliminating the absolute-position recency bias.

---

## Relationship to PCA Analysis

The rotation model and PCA analysis are complementary:

| Aspect | Combined QK PCA | Planar Rotation Model |
|--------|-----------------|----------------------|
| Axes chosen by | Maximum variance | Position covariance + Q/K separation |
| PC0 / axis a captures | Q/K identity + position (confounded) | Position only (by construction) |
| Q vs K position asymmetry | r_q > r_k (Q dominant on PC0) | r_k > r_q (K dominant on drift axis) |
| Attention score model | Identified mu_Q amplification | Full parametric decomposition with bias_strength |
| Complement characterization | Not analyzed | RoPE rotation planes (donuts, angle_r ~ 1.0) |
| Training dynamics | r_k drops during LC | alpha_K collapses 93% while r_k preserved |

The PCA finding that "r_q > r_k" and the rotation finding that "r_k > r_q" are both correct — they measure position correlation on different axes. PCA's PC0 is the maximum-variance direction (dominated by Q/K cluster separation), which happens to align more with Q's position encoding. The drift axis a is the maximum-*position-covariance* direction, which aligns more with K's position encoding.

---

## Connection to Thesis: Effective Context Length

### Mechanistic precision of position bias

The parametric attention score model (s_2D = ... + mu_Q^a * alpha_K * j + ...) provides a more precise mechanistic account than the PCA-based mu_Q amplification mechanism. bias_strength = mu_Q^a * alpha_K is a single scalar per head that quantifies recency bias, is sign-invariant, and decomposes cleanly into a Q cluster property (mu_Q^a) and a K drift property (alpha_K).

### Long-context training mechanism

The bias collapse finding (Finding 6) reveals the precise mechanism by which long-context training improves ECL: the model does NOT change the position-encoding direction (r_k preserved), but flattens the drift slopes (alpha_K drops 10x). This means:
- Relative-position encoding (via RoPE's symmetric rotations in the complement) is preserved
- Absolute-position bias (via the asymmetric drift in {a, b}) is suppressed
- Q/K separation strengthens, giving the model more capacity for content-based attention

This predicts that effective context extension methods should target alpha_K reduction specifically, rather than modifying the position encoding as a whole. Methods like RoPE theta scaling implicitly do this by changing the relationship between position and rotation angle, but the rotation model offers a more targeted diagnostic.

### Asymmetric vs symmetric RoPE decomposition

The decomposition into asymmetric drift ({a, b} plane) and symmetric rotation (complement) provides a new theoretical framework for understanding RoPE:
- The asymmetric component creates absolute-position bias (harmful for long context)
- The symmetric component creates relative-position encoding (useful for local attention patterns)
- Long-context training selectively suppresses the asymmetric component while preserving the symmetric one
- This decomposition could inform more targeted position encoding interventions
