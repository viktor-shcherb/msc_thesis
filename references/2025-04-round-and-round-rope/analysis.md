---
title: "Round and Round We Go! What Makes Rotary Positional Encodings Useful?"
authors: "Barbero, Vitvitskyi, Perivolaropoulos, Pascanu, Veličković"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["position-encoding", "attention-analysis", "mechanistic-interpretability"]
scope: ["rotary positional encoding", "RoPE frequency analysis", "positional attention heads", "semantic attention channels"]
benchmarks_used: ["perplexity-wiki", "perplexity-flanv2"]
models_introduced: []
models_evaluated: ["gemma-7b", "gemma-2b", "llama-3.1-8b"]
key_claims:
  - id: C1
    claim: "RoPE does not necessarily decay attention activations with relative distance; given any query and any relative distance r, a key can be found such that the softmax value is largest at distance r"
    evidence: "Proposition 3.1, Section 3, Figure 2"
    status: supported
  - id: C2
    claim: "For queries and keys sampled from a standard multivariate Gaussian, the expected activation is 0 regardless of relative distance, implying no decay"
    evidence: "Proposition 3.2, Section 3, Figure 2(b)"
    status: supported
  - id: C3
    claim: "Gemma 7B largely prefers to use the lowest frequencies of RoPE for computing attention activations, with the first and last layers showing the most high-frequency usage"
    evidence: "Section 4, Figure 3, Figure 4"
    status: supported
  - id: C4
    claim: "High frequencies in RoPE are used by Gemma 7B to construct robust positional attention heads (diagonal and previous-token patterns)"
    evidence: "Section 5, Figure 5, Figure 6, Theorem 5.3, Tables 3-5"
    status: supported
  - id: C5
    claim: "NoPE cannot learn diagonal or off-diagonal attention patterns in a single attention head"
    evidence: "Proposition 5.2, Section 5"
    status: supported
  - id: C6
    claim: "Low-frequency semantic channels in RoPE cannot be robust over arbitrarily long context due to the density of irrational rotations"
    evidence: "Theorem 6.1, Section 6"
    status: supported
  - id: C7
    claim: "0.75-RoPE (removing 25% lowest frequencies) achieves the best validation perplexity on Gemma 2B, outperforming standard RoPE (θ=10k), RoPE (θ=500k), and NoPE on both Wiki and FlanV2"
    evidence: "Table 2, Section 6.1"
    status: supported
cross_references:
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Provides mechanistic analysis of how RoPE is used in practice; challenges the long-term decay justification from Su et al. and shows Gemma 7B exploits high frequencies for positional heads and low frequencies for semantic channels"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Discusses similarity between RoPE and sinusoidal APE (both encode position through frequency ranges of sines/cosines), noting the additive vs multiplicative difference"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "Contrasts RoPE with ALiBi; argues that prior to this work the common belief was that ALiBi and RoPE behave analogously by decaying attention with distance, but this paper shows RoPE does not necessarily decay"
  - target: 2024-07-llama-3-herd-of-models
    type: complementary
    detail: "Llama 3 uses RoPE with θ=500,000; this paper explains why increasing θ helps -- it provides more 'slow enough' frequencies for semantic channels, preventing misalignment over long context"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "LLaMA adopted RoPE; this paper analyzes the internal mechanics of how RoPE-based models use different frequencies"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "Both perform mechanistic interpretability; this paper focuses specifically on how RoPE enables specific attention head types rather than general circuit analysis"
  - target: 2022-03-in-context-learning-induction-heads
    type: complementary
    detail: "Olsson et al. identify induction heads; this paper identifies positional heads (diagonal and previous-token) enabled specifically by RoPE's high frequencies"
  - target: 2021-11-ff-layers-key-value-memories
    type: complementary
    detail: "Geva et al. show FF layers act as sparse dictionary lookup; this paper observes similar sparse 'band' patterns in RoPE query/key frequency usage"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: complementary
    detail: "DroPE drops high-frequency RoPE dimensions after pretraining; this paper provides the mechanistic justification, showing high frequencies encode positional patterns while low frequencies carry semantics"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Both analyze RoPE's decay properties theoretically; Barbero et al. argue decay is not the core benefit, while Chi et al. characterize the decay as Gaussian-like"
  - target: 2025-04-attention-sink-emerges
    type: complementary
    detail: "Gu et al. study attention sinks across PE types; Barbero et al. identify BOS-attending semantic heads in Gemma 7B that use low-frequency RoPE bands"
open_questions:
  - question: "Does p-RoPE improve long-context generalization beyond 8k context length?"
    addressed_by: null
  - question: "Can the mechanistic findings about RoPE frequency usage guide better positional encoding designs for extremely long contexts?"
    addressed_by: null
  - question: "Why does Gemma 7B learn diagonal attention heads (which behave like residual connections) -- is this a training artifact?"
    addressed_by: null
  - question: "Do the frequency usage patterns transfer to models with different architectures (e.g., mixture-of-experts)?"
    addressed_by: null
---
# Round and Round We Go! What Makes Rotary Positional Encodings Useful?

**Authors:** Federico Barbero, Alex Vitvitskyi, Christos Perivolaropoulos, Razvan Pascanu, Petar Veličković (University of Oxford, Google DeepMind)
**Date:** October 2024, arXiv:2410.06205; published at ICLR 2025

---

## Core Research Problem

Rotary Positional Encodings (RoPE) have become the dominant positional encoding in modern LLMs (LLaMA, Gemma, Llama 3), yet the specific reasons why RoPE is useful remain poorly understood. The common justification, originally provided by Su et al. (2024), is that RoPE helps **decay attention coefficients as relative distance increases**. However, this claim relies on queries and keys being constant vectors -- an unrealistic assumption. Follow-up works have used this decay claim to justify modifications such as increasing the base wavelength θ from 10,000 to 500,000 (Xiong et al., 2023; Dubey et al., 2024).

RoPE operates by splitting query and key vectors into 2-dimensional chunks and rotating each chunk at a different frequency. The fastest frequency rotates at 1 radian per token, while the slowest rotates at approximately 1/θ radians per token. As dot product attention depends on the angle between queries and keys, the highest frequencies should behave like random noise under small token rearrangements, making their role unclear.

**The core challenge is to understand how RoPE is mechanically used by trained LLMs -- specifically, what roles the different rotation frequencies play and whether the commonly assumed decay property is actually the reason RoPE is effective.**

---

## Problem Solutions

The paper provides a mechanistic analysis of RoPE usage in Gemma 7B, challenging conventional wisdom and proposing a new understanding based on frequency-specific roles:

1. **Decay is not the core mechanism.** The paper proves that RoPE does not necessarily decay activations with distance and that Gemma 7B exploits this to create specific attention patterns (Propositions 3.1, 3.2).
2. **Frequency specialization.** Gemma 7B allocates most query/key norm to the lowest RoPE frequencies, using them as semantic channels. The highest frequencies are reserved for positional attention heads (Section 4).
3. **High frequencies enable positional heads.** RoPE's highest frequencies are used to construct robust diagonal and previous-token attention patterns -- a capability NoPE provably lacks (Section 5, Theorem 5.3).
4. **Low frequencies carry semantics but are fragile.** Low-frequency bands act as semantic channels but cannot be robust over arbitrarily long context due to the density of irrational rotations (Section 6, Theorem 6.1).
5. **p-RoPE: truncating lowest frequencies.** Removing the lowest 25% of RoPE frequencies creates robust semantic channels and improves validation perplexity on Gemma 2B models (Section 6.1).

---

## Approach Details

### Method

**Notation.** Token embedding x_i in R^d, with query q_i = W_Q x_i and key k_i = W_K x_i. Queries and keys are decomposed into 2-dimensional chunks: q_i = ⊕_{k=1...d/2} q_i^{(k)}, with q_i^{(k)} in R^2. RoPE defines a sequence of angles:

> G = (g_k = θ^{-2(k-1)/d} : k = 1, ..., d/2)

where g_1 = 1 (fastest, 1 radian/token) and g_{d/2} = θ^{-(d-2)/d} ≈ θ^{-1} (slowest). The rotation matrix for frequency g_k is:

> ρ(g_k) = [[cos(g_k), -sin(g_k)], [sin(g_k), cos(g_k)]]

The block-diagonal matrix R^i = ⊕_{k=1...d/2} ρ(g_k)^i = ⊕_{k=1...d/2} ρ(ig_k) applies position-dependent rotations. The RoPE kernel is:

> k_RoPE(q_i, k_j) = (R^i q_i)^T (R^j k_j) = q_i^T R^{j-i} k_j = Σ_{k=1...d/2} (q_i^{(k)})^T ρ(g_k)^{j-i} k_j^{(k)}

**Frequency usage measurement.** The paper measures how much each frequency contributes to the attention activation by computing the mean 2-norm of each query/key chunk ∥q_i^{(k)}∥, justified by the Cauchy-Schwarz bound |⟨q_i^{(k)}, k_j^{(k)}⟩| ≤ ∥q_i^{(k)}∥ ∥k_j^{(k)}∥. These norms are averaged over 10 Shakespeare quotes and all 16 attention heads per layer (Section 4).

### Key Technical Components

**Positional attention construction (Section 5, Theorem 5.3).** For the diagonal case: set all queries and keys equal (q_i = k_j = ψ). Then:

> a_{i,j} = ∥ψ∥^2 cos((j - i)g)

By Lemma A.1 (irrational rotations: ng ≡ 0 (mod 2π) only when n = 0), the activation is maximal at j = i and strictly smaller otherwise. As ∥ψ∥^2 → ∞, α_{i,i} → 1 - ε for any ε > 0.

For the off-diagonal (previous-token) case: set q_i = ψ and k_i = ρ(g)ψ, so that ρ(g)^{i-1} k_i = ρ(g)^i ψ aligns with ρ(g)^i q_i.

The highest frequencies create the sharpest positional patterns because they misalign queries and keys most rapidly: g_1 = 1 misaligns by a radian after 1 token, while g_{d/2} ≈ 1/10,000 requires ≈ 10,000 tokens.

**p-RoPE (Section 6.1).** Removes the lowest (1-p) fraction of RoPE frequencies, replacing them with identity (no rotation). With 0 ≤ p ≤ 1: p = 0 coincides with NoPE, p = 1 with standard RoPE. The removed low-frequency dimensions act as **robust semantic channels** that are independent of relative distance. Implementation pads the timescale array with infinity for the removed frequencies, making sin(position/∞) = 0 and cos(position/∞) = 1.

### Theoretical Analysis

**Proposition 3.1 (RoPE can be maximal at arbitrary distance).** Given any non-zero query q and any relative distance r, there exists a key k = R^r q such that q^T R^{j-i} k = Σ_k ∥ψ^{(k)}∥^2 cos((j - i + r)g_k), which is maximal only when j - i = -r (Section A.1).

**Proposition 3.2 (Gaussian queries and keys do not decay).** For q, k ~ N(0, I), E[q^T R^r k] = 0 for any relative distance r. The proof uses the fact that the standard multivariate Gaussian is isotropic: rotating k^{(k)} by ρ(g_k) preserves the distribution (Section A.1).

**Proposition 5.2 (NoPE cannot learn positional patterns).** Proof by counterexample: for sequence [x_bos, x_1, x_1] with repeated tokens, a_{3,3} = ⟨q_3, k_3⟩ = ⟨q_3, k_2⟩ = a_{3,2}, implying α_{3,3} < 1/2, which contradicts the diagonal pattern requirement α_{i,i} > 1 - ε (Section A.2).

**Theorem 6.1 (Semantic channels not robust over long context).** For d = 2 (single RoPE frequency g_1), given a long enough sequence, the attention head cannot attend to a target token with α_{i,n} > 1 - ε. The proof uses Lemma A.2 (irrational rotations are dense in [0, 2π]): for any desired rotation angle, there exists a position in a long enough sequence where a non-target token's activation exceeds the target's (Section A.3).

### Experimental Setup

**Mechanistic analysis (Sections 3--6):** Gemma 7B (Gemma Team et al., 2024), 28 layers, 16 heads per layer, hidden dimension 256 (128 RoPE frequency pairs), θ = 10,000, 8k context. Analysis performed on 10 Shakespeare quotes. Llama 3.1 8B validation in Appendix C (32 layers, GQA, θ = 500,000, 128k context).

**p-RoPE training (Section 6.1):** Gemma 2B models trained from scratch. Datasets: English Wikipedia (6,672,479 documents, 19.88 GiB, 10% validation holdout) and FlanV2 (Longpre et al., 2023; 15,000,000 samples). Training: 10,000 steps, batch size 512, sequence length 8,192, θ = 10,000. Standard Gemma 2B architecture.

### Key Results

**Validation perplexity on Gemma 2B (Table 2):**

| Encoding | Wiki | FlanV2 |
|---|---|---|
| NoPE | 4.8594 | 6.6429 |
| RoPE (θ = 10k) | 4.4627 | 6.4429 |
| RoPE (θ = 500k) | 4.4485 | 6.4593 |
| 0.75-RoPE_reversed | 4.4592 | 6.4683 |
| 0.75-RoPE_partial | 4.4537 | 6.4562 |
| 0.25-RoPE | 4.5302 | 6.5111 |
| **0.75-RoPE** | **4.4414** | **6.4422** |

- **0.75-RoPE achieves the best perplexity** on both Wiki (4.4414) and FlanV2 (6.4422), outperforming standard RoPE (θ=10k) and the increased wavelength variant (θ=500k) (Table 2, Section 6.1).
- **Removing the lowest frequencies is better than removing the highest:** 0.75-RoPE outperforms 0.75-RoPE_reversed (which removes the highest 25%), confirming that low frequencies are the ones that should be freed from rotation (Table 2).
- **Aggressive truncation harms performance:** 0.25-RoPE (keeping only 25% of frequencies) degrades perplexity to 4.5302/6.5111, still significantly better than NoPE (4.8594/6.6429) (Table 2).
- **NoPE vs RoPE vs p-RoPE properties (Table 1):** NoPE supports semantic but not positional patterns; RoPE supports positional but not robust semantic patterns; p-RoPE supports both.

**Mechanistic findings (Gemma 7B):**

- **Frequency usage (Figure 3):** At every layer, query and key norms are concentrated at the lowest frequencies. Value vectors show no such pattern, confirming this is a consequence of RoPE (Figure 13, Section E.2).
- **Positional heads use high frequencies (Figures 5, 6):** Heads 5 and 8 in Layer 1 are positional heads (diagonal and previous-token respectively). Their query/key norms are concentrated at the highest frequencies.
- **Diagonal head activations match Cauchy-Schwarz bound (Tables 3, 4):** For Layer 1 Head 5, diagonal activations (e.g., 383.00 at token 3) are close to the Cauchy-Schwarz upper bound (483.97), while previous-token activations (82.13) are much lower, confirming queries and keys are approximately equal.
- **Apostrophe semantic head (Figure 7):** Layer 1 Head 10 makes tokens after an apostrophe attend to it, using high frequencies for previous-token detection and a low-frequency band (g_119 ≈ 0.0002) as a semantic channel for BOS attention. The channel contributes ≈ -85.5 for non-BOS and ≈ +24.9 for BOS tokens (Section E.1).
- **Llama 3.1 8B replication (Figure 10):** Similar frequency usage patterns occur in Llama 3.1 8B with θ = 500,000. The high-norm band onset at ≈ 500,000^{-40/64} ≈ 0.0001 matches where bands appear in Gemma 7B at 10,000^{-0.8} ≈ 0.0006 (Section C).

---

## Limitations and Failure Modes

1. **Limited p-RoPE evaluation scale.** The p-RoPE experiments use only Gemma 2B models with 8k context, which the authors acknowledge is "not very large." Improvements from wavelength increase were typically observed at 32k context (Xiong et al., 2023). Larger-scale validation is left to future work (Section B.5).

2. **Perplexity as sole metric.** The authors note that "lower perplexity does not necessarily mean better downstream performance" (Kuribayashi et al., 2021). No downstream task evaluation is provided for p-RoPE (Section B.5).

3. **Mechanistic coverage is incomplete.** The middle-frequency RoPE dimensions have considerably smaller but non-zero norms and "could still play a role" that is not captured by the analysis (Section B.5).

4. **Single-head analysis for NoPE impossibility.** Proposition 5.2 proves NoPE cannot learn positional patterns for a *single head in isolation*. A sequence of attention heads could potentially learn such patterns via the Universal Approximation Theorem (Cybenko, 1989; Kazemnejad et al., 2024) (Section A.2).

5. **Theorem 6.1 restricted to d = 2.** The proof of semantic channel instability is given only for the case of a single RoPE frequency. The authors argue this is still informative since observed semantic bands are "often very distinct and focused on a single frequency" (Section 6).

---

## Conclusions

### Contributions

1. **Challenged the decay narrative for RoPE.** Proved that RoPE does not necessarily decay activations with distance (Proposition 3.1, 3.2), contradicting the primary justification given by Su et al. (2024) and used by subsequent works to motivate modifications like increasing θ (Section 3).

2. **Identified frequency specialization in trained models.** Demonstrated empirically that Gemma 7B allocates most query/key norm to the lowest RoPE frequencies, with high-frequency usage concentrated in specific positional attention heads (Section 4, Figures 3, 4).

3. **Proved RoPE enables positional attention patterns that NoPE cannot.** Showed by construction that RoPE can learn arbitrarily sharp diagonal and previous-token attention patterns (Theorem 5.3) and that NoPE provably cannot (Proposition 5.2). Gemma 7B learns constructions strikingly similar to the theoretical ones (Section 5, Tables 3--5).

4. **Explained the role of low frequencies as semantic channels.** Identified low-frequency "bands" in query/key vectors used for semantic matching (e.g., apostrophe detection), proved these channels are not robust over long context (Theorem 6.1), and connected this to why increasing θ helps with long-context performance (Section 6).

5. **Proposed p-RoPE as a principled modification.** Introduced p-RoPE, which removes the lowest RoPE frequencies to create robust semantic channels. 0.75-RoPE achieves the best validation perplexity on Gemma 2B, outperforming standard RoPE, increased-wavelength RoPE, and partial-RoPE (Table 2, Section 6.1).

### Implications

1. **Increasing θ provides more usable semantic frequencies.** (Inference) The paper's analysis explains why Llama 3's θ = 500,000 helps: it provides more frequencies whose rotation over 128k tokens is small enough to serve as stable semantic channels. With θ = 10,000 and 128k context, the lowest frequency completes ≈ 2.04 full rotations, potentially destroying semantic information.

2. **RoPE and NoPE are complementary, not competing.** (Inference) RoPE enables positional patterns; NoPE enables robust semantic patterns. p-RoPE combines both strengths, suggesting that future positional encodings should explicitly allocate dimensions for both roles.

3. **Context length scaling requires coordinated θ and frequency allocation.** (Inference) The paper predicts that as contexts grow, θ must increase proportionally -- or equivalently, some frequencies should be freed from rotation entirely via p-RoPE-style truncation.

---

## Key Claims

1. **C1: RoPE can be maximal at arbitrary distance.** Given any non-zero query q and any relative distance r, there exists a key k such that the softmax value is largest at distance r. The construction sets k^{(k)} = ρ(g_k)^r q^{(k)} and relies on the uniqueness of irrational rotations (Lemma A.1). Evidence: Proposition 3.1, Section 3. Status: **supported**.

2. **C2: Gaussian queries and keys do not decay.** For q, k ~ N(0, I), E[q^T R^r k] = 0 for any r, because the isotropic Gaussian is invariant under rotation. The decay visible with constant all-ones vectors (Figure 2a) disappears with Gaussian vectors (Figure 2b). Evidence: Proposition 3.2, Section 3, Figure 2. Status: **supported**.

3. **C3: Gemma 7B prefers low RoPE frequencies.** The mean 2-norm of query and key chunks is concentrated at the lowest frequencies across all 28 layers. High-frequency usage appears mainly in the first and last layers. Value vectors show no such pattern (Figure 13), confirming this is RoPE-specific. Evidence: Section 4, Figures 3, 4, 13. Status: **supported**.

4. **C4: High frequencies construct positional attention heads.** Diagonal heads (Layer 1 Head 5, Layer 27 Head 8) and previous-token heads (Layer 1 Head 8) concentrate their norm at the highest frequencies. The learned construction matches the theoretical one: queries and keys are approximately equal (Tables 3--5). Evidence: Section 5, Figures 5, 6, 14--16, Tables 3--5. Status: **supported**.

5. **C5: NoPE cannot learn diagonal or off-diagonal patterns.** A single attention head with NoPE and repeated tokens [x_bos, x_1, x_1] yields α_{3,3} = α_{3,2} < 1/2, violating the definition of a diagonal pattern. Evidence: Proposition 5.2, Section A.2. Status: **supported**.

6. **C6: Semantic channels are not robust over long context.** For d = 2 and a single RoPE frequency, the density of irrational rotations (Lemma A.2) guarantees that for large enough N, a token swap exists making the target activation no longer the largest. Evidence: Theorem 6.1, Section A.3. Status: **supported**.

7. **C7: 0.75-RoPE improves over standard RoPE on Gemma 2B.** 0.75-RoPE achieves Wiki perplexity 4.4414 vs 4.4627 for RoPE (θ=10k) and 4.4485 for RoPE (θ=500k). On FlanV2: 6.4422 vs 6.4429 and 6.4593 respectively. Evidence: Table 2, Section 6.1. Status: **supported**.

---

## Open Questions

1. **Does p-RoPE improve long-context generalization?** The paper trains only with 8k context. The authors "expect that truncating some small percentage of the lowest frequency tokens [would] help with long-context generalisation" but lack resources to validate this (Section B.5). **Unresolved.**

2. **Can mechanistic RoPE understanding guide better PE design for extreme contexts?** The paper establishes that frequencies serve distinct roles (positional vs semantic) but does not propose a complete alternative to the geometric frequency schedule θ^{-2(k-1)/d}. **Unresolved.**

3. **Why does Gemma 7B learn diagonal attention heads?** Diagonal heads behave like residual connections. The paper notes this "constitutes interesting learnt behaviour which requires further analysis -- perhaps a training 'bug'" (Section 5). **Unresolved.**

4. **Do findings generalize across architectures?** The paper verifies consistency between Gemma 7B and Llama 3.1 8B (Appendix C) and across input domains (Italian, Chinese, code, arithmetic; Figure 19), but both models use standard dense Transformer architectures. MoE or other architectures remain untested. **Unresolved.**

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE and the decay justification that this paper challenges. The frequency schedule θ_i = 10,000^{-2(i-1)/d} and block-diagonal rotation structure are the objects of study.

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer and sinusoidal absolute positional encodings. The paper notes strong similarity between RoPE and APE (both use frequency ranges of sines/cosines) but with the key difference of multiplicative vs additive application.

- **Press et al. (2021)** -- *Train Short, Test Long: ALiBi.* An alternative PE that truly decays attention with distance. The paper contrasts ALiBi's guaranteed decay with RoPE's lack thereof.

### Context Extension and Wavelength Modification

- **Xiong et al. (2023)** -- *Effective Long-Context Scaling.* Proposes increasing θ to 500,000. This paper provides a mechanistic explanation: larger θ provides more stable low-frequency semantic channels.

- **Roziere et al. (2023)** -- *Code Llama.* First proposes increasing the RoPE wavelength, a practice later adopted by Llama 3.

- **Dubey et al. (2024)** -- *The Llama 3 Herd of Models.* Uses θ = 500,000 for 128k context. Llama 3.1 8B is used as a secondary validation model in Appendix C.

- **Xu et al. (2024)** -- *Base of RoPE Bounds Context Length.* Studies the relationship between θ and maximum context length, supporting this paper's claim that θ must scale with context.

### NoPE and Positional Encoding Analysis

- **Haviv et al. (2022)** -- *Transformer Language Models Without Positional Encodings.* Shows Transformers can perform well without PE. This paper argues NoPE and RoPE are complementary, not competing.

- **Kazemnejad et al. (2024)** -- *The Impact of Positional Encoding on Length Generalization.* Proves Transformers can recover positional information through the causal mask (via Universal Approximation Theorem). This paper shows NoPE cannot learn positional patterns in a single head.

- **Ruoss et al. (2023)** -- *Randomized Positional Encodings.* Proposes randomizing RoPE positions for OOD generalization. This paper provides an alternative explanation: randomization pushes models to use the lowest frequencies (Section B.3).

### Mechanistic Interpretability

- **Elhage et al. (2021)** -- *A Mathematical Framework for Transformer Circuits.* Foundational mechanistic interpretability framework. This paper applies similar "reverse engineering" specifically to RoPE's role.

- **Olsson et al. (2022)** -- *In-Context Learning and Induction Heads.* Identifies induction heads. This paper identifies positional heads (diagonal and previous-token) as a distinct category enabled by RoPE.

- **Geva et al. (2021)** -- *Transformer Feed-Forward Layers Are Key-Value Memories.* Observes sparse dictionary lookup in FF layers. This paper finds analogous sparse "band" patterns in RoPE query/key frequency usage.

### Models Used in Analysis

- **Gemma Team et al. (2024)** -- *Gemma: Open Models Based on Gemini Research and Technology.* Provides the primary model (Gemma 7B, 28 layers, 16 heads, d=256) and the training architecture (Gemma 2B) used for p-RoPE experiments.

### Training Data

- **Longpre et al. (2023)** -- *The Flan Collection.* Provides the FlanV2 dataset (15M samples) used for p-RoPE training experiments.
