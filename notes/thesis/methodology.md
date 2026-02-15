# Chapter 4: Methodology

Draft — 2026-02-15

## Purpose

Define the three-analysis measurement framework applied to Q/K vectors. No results here — only the tools, their formal definitions, and why they answer complementary questions. The reader should finish this chapter knowing exactly what each analysis computes and what question it answers, and understand the logical progression: PCA (exploratory) → Rotation (mechanistic precision) → Plasticity (functional consequence).

---

## 4.1 — Q/K Capture Protocol

**~1.5 pages**

### Argument

Post-RoPE Q/K vectors are the right object of study because they contain the position-encoded representation the model uses at scoring time. Pre-RoPE vectors would miss position encoding; attention weights would lose the Q/K decomposition.

### Content

1. **What we capture.** For each attention head, we collect Q and K vectors at every token position. These are post-RoPE, post-projection vectors — the exact inputs to the dot-product attention score q^T k.

2. **Why post-RoPE.** RoPE applies a position-dependent rotation to Q and K before scoring. The post-RoPE vectors carry both content and position information as the model sees them. Analyzing pre-RoPE vectors would characterize the learned representations but miss the position encoding that determines attention patterns.

3. **Dataset.** 500 examples from LongBench-Pro (128K+ tokens). Realistic, long, diverse tasks. The choice of realistic text (not synthetic needles or random tokens) means the captured vectors reflect the model's behavior on the kind of input it was trained for.

4. **Sampling strategy.** Uniform position bucketing with min_bucket_size=8192 tokens. 300 query heads sampled per model. This ensures coverage across the full context window without overrepresenting early positions (which would happen with uniform token sampling, since most documents are front-loaded).

5. **Scope.** All query heads are captured. In GQA models, the shared key is simply broadcast to each query head in the group, so each (query head, key) pair is analyzed independently — no special handling is needed.

### Transition to 4.2

> The captured vectors form a high-dimensional point cloud for each head. The first question is structural: how is variance distributed, and how much is explained by position?

---

## 4.2 — PCA Decomposition

**~2 pages**

### Argument

PCA is the natural starting point: it finds the directions of maximum variance without assumptions about what those directions represent. We apply it to the combined Q+K point cloud and ask which components correlate with position.

### Content

1. **Combined Q+K pooling.** We concatenate Q and K vectors from the same head into one point cloud (labeled by type and position). This lets PCA find directions that separate Q from K as well as directions that encode position — both contribute to variance.

2. **Correlation with position.** For each principal component, compute Pearson correlation between the projection and token position, separately for Q vectors (r_q) and K vectors (r_k). Sign-canonicalize so the dominant correlation is positive.

3. **Head taxonomy.** Based on (r_q, r_k) on PC0, classify heads into four categories:
   - Position-dominated: both |r_q| and |r_k| > threshold
   - Q-positional: |r_q| > threshold, |r_k| below
   - Content-focused: both below threshold
   - Mixed: intermediate

   The taxonomy is descriptive — it summarizes what PCA reveals about variance structure. It is NOT a causal classification (a head classified as "position-dominated" may still perform content-dependent retrieval if the positional variance is large but the content signal still wins in the dot product).

4. **What PCA can and cannot do.**
   - CAN: discover that position is the dominant source of variance; reveal that Q/K separability and position encoding are confounded on PC0; provide a model-agnostic structural fingerprint.
   - CANNOT: isolate position from Q/K identity; provide a parametric bias term; tell you whether position dominates content in the attention score.

   The confound: PC0 maximizes total variance, which includes the large Q/K cluster offset. This inflates r_q relative to r_k because the Q cluster mean happens to align with the position gradient direction. Rotation resolves this by constructing axes with explicit semantic targets.

### Transition to 4.3

> PCA reveals that position structure exists and is pervasive, but its axes conflate position encoding with Q/K identity separation. To isolate the bias mechanism, we construct a rotation with axes targeted at specific geometric quantities.

---

## 4.3 — Planar Rotation Model

**~3–4 pages.** This is the methodological core.

### Argument

We construct a 2D plane in the head's embedding space with axes that have guaranteed semantic meaning: one captures all linear position covariance, the other captures maximum Q-K separation. This gives a parametric bias term and a clean decomposition of the embedding space.

### Content

1. **Axis a: drift direction.** The direction that maximizes linear covariance between projection and token position, computed over the combined Q+K pool (both Q and K vectors pooled with their respective positions). By construction, all directions orthogonal to a have exactly zero linear position covariance. This is the unique direction where position "lives" linearly in the combined representation.

   *Math (inline, short):* axis a = argmax_u Cov(u^T x, t) subject to ||u|| = 1, where x ranges over pooled Q and K vectors. Solution: a = Cov(x, t) / ||Cov(x, t)||. Verification: residual correlation on orthogonal complement < 1e-14.

   Because Q and K may encode position differently, using the combined pool captures the shared positional direction — the one that enters the dot product q^T k. Separate Q-only or K-only drift directions would miss this shared structure.

2. **Axis b: separation direction.** The direction orthogonal to a that maximizes Q-K centroid separation: b = argmax_u (μ_Q - μ_K)^T u subject to ||u|| = 1, u ⊥ a. Solution: project (μ_Q - μ_K) onto the complement of a, normalize.

3. **The {a, b} plane.** Together, a and b span a 2D plane. In this plane:
   - The horizontal axis (a) shows position gradients — tokens at different positions spread along a.
   - The vertical axis (b) shows Q/K identity — Q and K clusters separate vertically.
   - The position gradient of K vectors along a is measured by the drift slope α_K (linear regression coefficient).
   - The Q cluster centroid on axis a is μ_Q^a.

4. **Bias strength formula.** The contribution of the drift mechanism to the attention score is:

   bias_strength = μ_Q^a × α_K

   This is one scalar per head. It measures how much the Q cluster's position on the drift axis amplifies the K position gradient. When bias_strength > 0, nearer keys are favored (recency bias).

   *Math (inline):* The dot product q^T k projected onto axis a decomposes as q_a · k_a. The mean positional contribution is μ_Q^a × (α_K · t_k + intercept), which increases linearly with key position at rate μ_Q^a × α_K.

5. **Complement: the (d-2)-dimensional remainder.** Everything orthogonal to the {a, b} plane. This subspace contains:
   - RoPE rotation planes: pairs of dimensions where position encodes as rotation angle. Q and K overlap perfectly on these rings — shared RoPE cancels in the dot product, contributing only relative-position structure.
   - Content dimensions: carrying semantic signal with zero position encoding.

   The complement is where content signal lives. The {a, b} plane is where asymmetric position bias lives. This separation is exact by construction.

6. **Relationship to PCA.** Both PCA and Rotation are orthogonal transformations that preserve q · k exactly. PCA maximizes variance; Rotation targets position covariance and Q/K separation. The key difference: on axis a, r_k > r_q (keys encode position more strongly), reversing PCA's PC0 finding. The reversal occurs because PC0 conflates the Q/K centroid offset with position encoding; axis a isolates position.

### Transition to 4.4

> Rotation quantifies the bias mechanism: how much does position enter the attention score, and through what geometric pathway? But bias magnitude alone does not determine whether position dominates content. A head with large bias_strength may still attend flexibly if content signal is strong enough to overcome the positional preference. To measure the functional consequence — does position actually constrain which key wins? — we need a different quantity.

---

## 4.4 — Attention Plasticity

**~3–4 pages.** This section presents the formal framework from the paper (ICML 2025).

### Argument

Plasticity measures whether position bias dominates content signal in determining which key a query attends to. It answers the question PCA and Rotation cannot: does the bias matter functionally? The key insight is that keys are fixed by the prefix, while queries are random (drawn from the workload distribution of future continuations). Plasticity measures how often key orderings flip under this query randomness.

### Content

1. **Setup: keys are fixed, queries are random.** Fix an attention head and a prefix x_{1:n}. The keys k_i for i ≤ n are deterministic functions of the prefix — they are fixed. Now consider a query at position t > n. The query q_t depends on future tokens beyond the prefix, which are drawn from the workload distribution D. From the perspective of the prefix, q_t is a random variable.

   This is the fundamental asymmetry: keys carry the context we want to retrieve from; queries carry the question being asked. Plasticity measures whether the model's answer to "which key is most relevant?" depends on the question (content-driven) or is predetermined by position.

2. **Pairwise preference.** For a fixed prefix x_{1:n} and a pair of admissible key indices (I, J) with I < J, the pairwise preference probability is:

   p_{n,t}(x_{1:n}, I, J) = Pr_{q_t}[f(q_t, k_I) > f(q_t, k_J)]

   The probability is taken only over the random query q_t (drawn from future continuations of the prefix). The keys and their indices are held fixed.

3. **Pairwise plasticity.** For a fixed prefix and key pair:

   PP_{n,t}(x_{1:n}, I, J) = 4 · p · (1 - p)

   This is the scaled Bernoulli variance of the indicator "does q_t prefer k_I over k_J?" PP = 1 when p = 0.5 (content determines the winner — the ordering flips often). PP → 0 when p → 0 or 1 (position determines the winner — the ordering is rigid regardless of the query).

4. **Attention Plasticity at position t (Definition).** Aggregate PP over random prefixes and random key pairs:

   AP_t = E[PP_{N,t}(X_{1:N}, I, J)]

   where the expectation is over: (i) a random prefix length N uniform in {1,...,t-1}, (ii) a random prefix X_{1:N} from D, (iii) a random key pair (I,J) uniform over admissible pairs. AP_t ∈ [0,1] is a scalar that depends only on the query position t (for a fixed head and workload).

5. **Positional-semantic decomposition.** To compute AP_t in closed form, we decompose queries using an orthogonal alignment:

   - Estimate the drift direction from query-position regression: β = Cov(q_t, t) (over the workload).
   - Construct a Householder rotation R mapping β/||β|| to e_1. Apply R to both Q and K vectors.
   - In the rotated basis, coordinate 1 captures all linear position covariance; coordinates 2...d are position-decorrelated ("semantic").

   **Note:** This is distinct from the 2D rotation in Section 4.3. The Rotation analysis constructs a {a, b} plane from the combined Q+K pool for geometric characterization. The plasticity framework uses a query-only Householder rotation for the theoretical decomposition. Both are orthogonal transformations preserving q·k; they serve different purposes.

6. **Gaussian closed-form.** Under sub-Gaussian assumptions on the query distribution (Assumption 2.1 in the paper), the score difference D = q_t^T(k_I - k_J) is approximately Gaussian. In the rotated basis, with key difference δ = k_I^rot - k_J^rot:

   μ = δ_1 · (α_pos + β_pos · τ_q) + δ_{2:d}^T · m_sem

   v = δ_1² · σ²_pos + δ_{2:d}^T · diag(σ²_sem) · δ_{2:d}

   p = Φ(μ / √v)

   where:
   - δ_1 = positional coordinate difference between the two keys
   - α_pos + β_pos · τ_q = mean query positional coordinate at query bucket position τ_q
   - m_sem, σ²_sem = mean and variance of query semantic coordinates at query bucket
   - σ²_pos = residual variance of query positional coordinate after linear detrending

   The ratio μ/√v is the signal-to-noise ratio. When keys differ in position (δ_1 ≠ 0) and the query position τ_q grows, the positional term in μ grows linearly (via β_pos · τ_q) while v stays bounded. This drives p away from 0.5 → plasticity → 0.

7. **Main theoretical result (Theorem 2.3).** Under the positional-semantic model with non-zero positional drift:

   AP_t ≤ AP_∞ + C · exp(−c · t²)

   If all key pairs have distinct positional coordinates, AP_t → 0 as t → ∞. In words: attention plasticity inevitably decays with query position whenever the query distribution exhibits linear positional drift — which all examined models do.

8. **Primary bucketing: per-query-position.** The native computation is per-query-bucket: for each query position bucket q, pool all eligible keys from earlier buckets, sample key pairs, compute the Gaussian closed-form, and average. This produces AP as a function of query position — the plasticity profile.

9. **Secondary bucketing: 2D heatmaps.** Each sampled key pair also produces a 2D coordinate:
   - **Inter-key distance:** |p_{k_1} - p_{k_2}|
   - **Query-to-key-midpoint distance:** τ_q - ½(p_{k_1} + p_{k_2})

   Binning plasticity by these two distances reveals structure invisible in the 1D position profile. Keys close together but far from query → content wins (high plasticity). Keys far apart with one near query → position dominates (low plasticity).

10. **Aggregate metrics.**
    - ap_overall: bucket-size-weighted mean across query position buckets.
    - ap_first_20%, ap_last_20%: mean plasticity for query positions in the first/last 20% of context.
    - ap_drop = ap_first_20% − ap_last_20%: the plasticity degradation across context. This is the key diagnostic metric.

### Transition to 4.5

> The three analyses form a logical progression: PCA discovers that position structure exists, Rotation parameterizes the bias mechanism, and Plasticity measures whether the bias dominates content signal. All three are orthogonal transformations or probabilistic models over the same captured Q/K vectors.

---

## 4.5 — Connecting the Three Analyses

**~1 page**

### Argument

The three analyses are not three levels of abstraction — they are three orthogonal questions about the same Q/K geometry, at the same level of mechanistic detail.

### Content

Summary table:

| Analysis | Computes | Question | Key metric |
|----------|----------|----------|------------|
| PCA | Variance decomposition, position correlation | How is Q/K variance distributed? | r_q, r_k on PC0; head taxonomy |
| Rotation | Targeted axis projections, drift slopes | What is the parametric form of position bias? | bias_strength = μ_Q^a × α_K |
| Plasticity | Pr(random query flips key ordering) | Does position bias dominate content? | ap_drop (plasticity degradation) |

**Two related orthogonal transformations.** Rotation (4.3) and Plasticity (4.4) both use orthogonal transformations that preserve q·k, but they differ in construction and purpose:
- **Rotation** constructs axes from the combined Q+K pool — axis a captures the shared positional drift, axis b captures Q-K identity separation. Purpose: geometric characterization of the bias mechanism.
- **Plasticity** constructs a Householder rotation from query-only drift — coordinate 1 captures query positional drift, the rest are semantically decorrelated. Purpose: formal framework for the decay theorem and the Gaussian closed-form.

On the drift axis, both rotations isolate position covariance, and the resulting projections are closely related. The Rotation analysis additionally constructs axis b (Q-K separation), which the Plasticity framework does not need.

**Logical dependencies:**
- PCA → Rotation: PCA discovers positional dominance; Rotation isolates and parameterizes it.
- Rotation → Plasticity: Rotation gives bias_strength; Plasticity tests whether it functionally constrains attention.
- Plasticity fills specific gaps that Rotation leaves open (bias magnitude ≠ impact; per-head scalar ≠ position profile; no connection to benchmarks).

When plasticity is low, Rotation tells you *why* (large bias_strength). When bias_strength is large, Plasticity tells you *whether it matters* (whether content can compensate).

---

## Appendix A candidates from Chapter 4

- Full derivation of orthogonal drift alignment (Householder construction) if the inline version in 4.3 feels too heavy.
- Implementation details of sign canonicalization in PCA.
- Proof that all directions orthogonal to axis a have zero linear position covariance.
- Full proofs from the paper: Lemma 2.1 (sub-Gaussian score noise), Lemma 2.2 (single-pair decay), Theorem 2.3 (AP decay bound). The main text should state the theorem and give intuition; the appendix carries the formal proofs.
- Sub-Gaussian parameter estimation from finite samples (safety margins, normality diagnostics).
- Invariance of dot-product attention under orthogonal transformation (short proof: R^T R = I preserves inner products).
