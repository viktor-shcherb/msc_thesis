# Presentation Script

**Title:** Attention Plasticity and the Geometry of Long-Context Failure
**Duration:** ~25 minutes + questions
**Audience:** MSc thesis defense committee

---

## Slide 1 — Title

"Attention Plasticity and the Geometry of Long-Context Failure."

---

## Slide 2 — The Problem (2 min)

Large language models now advertise context windows of 128K tokens or more. But there's a persistent gap between claimed and effective context length. Models that accept 128K tokens can degrade on tasks requiring retrieval or reasoning beyond 32K.

Behavioral benchmarks — LongBench-Pro, RULER, NIAH — detect this gap. They tell us *that* a model fails at long context, but not *why*. The question this thesis asks is: what is the mechanistic pathway from architecture to effective context failure?

**Key visual:** Table or bar chart showing claimed vs. effective context for several models.

---

## Slide 3 — The Hypothesis (1 min)

The attention mechanism computes a relevance score between each query and key vector. These vectors carry both content information and position information, injected by rotary positional encoding (RoPE).

Our hypothesis: when position information dominates the attention score, the model's ranking of keys becomes rigid — it ranks by position rather than by content relevance. This rigidity is the mechanistic pathway.

**Key visual:** Diagram of q^T k = content component + positional component.

---

## Slide 4 — Research Questions (1 min)

Three research questions, each addressed by a dedicated analysis:

- **RQ1:** How does position information manifest in the geometry of attention heads? → PCA + Rotation
- **RQ2:** Does positional bias functionally constrain attention? → Attention Plasticity
- **RQ3:** Do plasticity profiles correspond to behavioral performance? → Benchmark correlation

---

## Slide 5 — Method Overview (1 min)

Single forward pass captures post-RoPE Q and K vectors across all heads. Three analyses applied to the same captured data:

1. **PCA** — discovers structure, quantifies variance budget
2. **Planar Rotation** — isolates the bias mechanism parametrically
3. **Attention Plasticity** — measures functional consequence

Each analysis resolves a question the previous one leaves open. PCA finds positional dominance but can't say if it matters. Rotation quantifies the bias but can't say if content overcomes it. Plasticity measures the actual competition.

**Key visual:** Pipeline diagram: Capture → PCA → Rotation → Plasticity.

---

## Slide 6 — PCA: Positional Dominance (2 min)

We run PCA on the combined Q+K point cloud for each head. The first principal component captures ~34% of variance — more than 4× the second component. Of that, 23–32% of query variance and 9–20% of key variance is linear in token position.

Position is the single largest structural feature in these representations.

On PC0, queries appear more positional than keys: r_q ≈ 0.80 vs r_k ≈ 0.49. But this is misleading — PC0 conflates positional encoding with Q/K identity separation. We need a targeted rotation to disentangle them.

**Key visual:** Figure 6.1 — PC roles across 11 models.

---

## Slide 7 — Rotation: The Bias Mechanism (2 min)

We construct a 2D plane with semantic axes: axis *a* maximizes position covariance (the "drift axis"), axis *b* captures the Q/K centroid offset.

The PCA asymmetry reverses: on the drift axis, keys encode position *more strongly* than queries (r_k ≈ 0.87 > r_q ≈ 0.74). This correction matters — it changes which vector carries the position signal and is consistent with how RoPE encodes key positions.

Positional bias has a precise parametric form: bias_strength = μ_Q^a × α_K. The query cluster's position on the drift axis amplifies the key position gradient. Across 3,239 heads, 99% show positive bias strength — near-universal recency bias. Bias strength is tight within families: 3×10⁻⁴ for all Ministral scales, 0.8–1.0×10⁻³ for Qwen, 6–7×10⁻⁴ for Llama.

**Key visual:** Figure 6.2 — r_k > r_q on drift axis (bar chart).

---

## Slide 8 — Attention Plasticity: The Functional Test (2 min)

Bias magnitude doesn't equal bias impact. A head with large bias could still attend flexibly if content signal is strong. We need a functional measure.

Attention plasticity frames this as a reranking problem. Attention induces a ranking over keys — effective long context requires this ranking to reflect content relevance. Pairwise comparison is the atomic unit of any ranking, so we measure: given a random query and two keys, does the query's content determine which key ranks higher?

Formally: PP = 4p(1−p), where p = Φ(μ/√v). When p ≈ 0.5, content determines the outcome. When p → 0 or 1, position has locked the ordering.

We prove that plasticity decays with query position under linear positional drift — the positional term in μ grows linearly while the variance is position-independent. The rate of decay is what distinguishes models.

**Key visual:** The Gaussian closed form equation, maybe with an illustrative plasticity curve.

---

## Slide 9 — Experimental Setup (1 min)

- 13 models from 3 families: Ministral-3 (3B/8B/14B, 256K), Qwen-3 (0.6B–14B, 128K), Llama-3.2 (1B/3B/11B, 128K)
- 10 SmolLM3-3B training checkpoints (pre-training through LC extension)
- Capture: bfloat16, post-RoPE, 300 query heads per model, uniform bucket sampling
- Benchmarks: LongBench-Pro (7 matched models), RULER (2 predecessor models)

---

## Slide 10 — Result: Plasticity Profiles Separate Families (2 min)

Every model shows declining plasticity across context. The *rate* of decline separates families.

- **Ministral-3:** Gradual, near-linear decline. AP_drop ≈ 0.07–0.08. Flattest profiles.
- **Qwen-3:** Steeper decline, AP_drop ≈ 0.16–0.19. Accelerates in second half.
- **Llama-3.2:** Steepest. AP_drop ≈ 0.17–0.23. Llama-3.2-3B drops from 0.686 to 0.456.

The 2D heatmaps reveal plasticity depends on *two* distances: inter-key distance and query-to-key distance. Ministral is uniformly warm; Qwen shows a diagonal gradient; Llama shows extreme contrast.

**Key visual:** Table 6.1 (quintile profiles) + 2×2 heatmap composite (Figure 6.3).

---

## Slide 11 — Result: AP_drop Predicts LongBench-Pro (2 min)

Across 7 models with both mechanistic metrics and LBP scores, AP_drop separates families in the same order as benchmark performance:

- Ministral (~0.07) → LBP 30–40
- Qwen (~0.17) → LBP 31–37
- Llama (0.23) → LBP 16

Within Qwen, the relationship is monotonic: 14B (0.161, LBP 37.1) > 8B (0.177, 33.4) > 4B (0.187, 31.3).

The diagnostic outlier: Ministral-3-3B has the *lowest* AP_drop (0.072) and *highest* aggregate plasticity (0.622), yet scores only 30.18 on LBP. Flat plasticity profile, but limited base capability at 3B. This is the decomposition: benchmark performance = base capability × context preservation. AP_drop isolates the second factor.

**Key visual:** Figure 6.5 — AP_drop vs LBP scatter plot.

---

## Slide 12 — Result: Training Dynamics (3 min)

SmolLM3-3B across 10 checkpoints tells a three-phase story.

**Phase 1 — Pre-training.** Bias strength doubles (0.009 → 0.019). The model progressively learns to encode position in key vectors. Plasticity declines uniformly. AP_drop is mild (~0.06) within the 4K window.

**Phase 2 — LC extension onset (4K→32K).** Bias strength collapses 6× within 4K training steps, through α_K flattening. Near-position plasticity recovers to early-training levels.

**Phase 3 — LC extension continued (32K→64K).** Bias halves again (total 10× reduction). But AP_drop *triples* from 0.06 to 0.16. At 48K–64K, plasticity is 0.43 — far below the 0.57 at 3.5K–4K during pre-training at comparable bias.

**The punchline:** Bias reduction is necessary but not sufficient. After the positional term is nearly zeroed, content signal decay at distant positions becomes the binding constraint.

**Key visual:** Table 6.2 (trajectory table) + Figure 6.4 (bias decomposition).

---

## Slide 13 — The Central Finding (2 min)

Current LC extension methods — position interpolation, NTK-aware scaling, YaRN — focus on making position encodings generalize. Our results suggest this addresses only half the problem.

The Ministral-3 signal: same bias levels as SmolLM3 post-LC, but 2× flatter plasticity over 4× longer context. Whatever their recipe does, it maintains content signal strength at distance — not just bias reduction.

Two candidate mechanisms for content decay:
1. RoPE rotation accumulation decorrelating distant keys
2. Attention sink competition starving distant positions

Both are open questions for future work.

**Key visual:** Diagram showing bias component (addressed by current methods) vs. content decay component (unaddressed).

---

## Slide 14 — Limitations (1 min)

Be upfront about what this work does not do:

- **Observational, not causal.** We measure associations between geometry and performance, not interventions.
- **3 families, 1 training trajectory.** Limited generalization to MoE, SSMs, or much larger scales.
- **Pairwise ranking, not softmax weights.** Plasticity captures ranking quality but not weight allocation.
- **Base vs. instruct confound.** Mechanistic metrics on base models, benchmarks on instruct variants.
- **Linear drift and Gaussian assumptions.** Empirically supported approximations, but non-linear RoPE structure not captured.

---

## Slide 15 — Contributions Summary (1 min)

1. **Geometric framework:** Three analyses (PCA → Rotation → Plasticity) operating on the same captured Q/K vectors, each resolving what the previous leaves open.

2. **Plasticity decay theorem:** Formal proof that attention plasticity decays with query position under linear drift, with Gaussian closed form.

3. **Cross-model validation:** AP_drop separates families in benchmark order across 13 models.

4. **Bias ≠ context:** 10× bias collapse but AP_drop triples. Content signal decay is the underexplored dimension.

---

## Slide 16 — Future Work (1 min)

- **Interventional validation:** Ablate low-plasticity heads, measure retrieval accuracy.
- **Characterize content decay:** Which mechanism — RoPE accumulation, attention sinks, feature drift?
- **Broader coverage:** MoE models, SSMs, larger scales.
- **Per-length benchmarks:** Full per-length LBP/RULER correlation across all matched models.

---

## Slide 17 — Thank You / Questions

---

## Anticipated Questions

**Q: Why pairwise and not full softmax?**
A: Attention is a reranking mechanism. Any total ordering is determined by its pairwise comparisons — if pairwise orderings are corrupted by position, the global ranking is necessarily corrupted. Pairwise comparison is the natural unit for evaluating ranking quality.

**Q: How do you know the correlation with benchmarks is causal?**
A: We don't claim causality. The design is observational. The next step would be interventional — ablating heads and measuring retrieval accuracy. We make associative claims only.

**Q: What about models with sliding window attention?**
A: We analyze Mistral-v0.2 within its sliding window only. This is an implementation limitation — the sampling of key pairs requires comparable query distributions across models, so we restrict to full-attention windows.

**Q: Could instruction tuning change the geometry?**
A: Yes, this is a limitation we acknowledge. Mechanistic metrics are on base models, benchmarks on instruct variants. The fact that the correlation holds despite this confound suggests the base geometry is at least partially preserved through instruction tuning, but we cannot confirm this.

**Q: Why does Ministral-3 have such flat profiles?**
A: We don't know the specific mechanism — the training recipe is proprietary. But the metric gives a concrete target: AP_drop < 0.10 over 128K+ context. The fact that they achieve this at comparable bias levels to other families suggests their approach addresses content signal preservation, not just bias reduction.

**Q: Is the ~34% PC0 variance the same across all models?**
A: We report it as a cross-model average. Per-family variation exists: Llama models tend to have higher positional variance fractions than Ministral. The detailed per-family ranges (23–32% Q, 9–20% K) are reported in the results.

**Q: What about the Gaussian assumption?**
A: It's an approximation. Score differences are approximately Gaussian by CLT when aggregating over many key pairs, and Q-Q plots confirm reasonable normality. The decay theorem's qualitative prediction (plasticity decays with position) holds more generally — the Gaussian form just gives us a closed-form expression. Non-Gaussian content distributions would change the rate but not the direction of decay.
