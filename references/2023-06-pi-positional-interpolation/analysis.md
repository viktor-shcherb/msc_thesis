---
title: "Extending Context Window of Large Language Models via Positional Interpolation"
authors: "Chen, Wong, Chen, Tian"
year: 2023
venue: "arXiv 2023"
paper_type: preprint
categories: ["context-extension", "position-encoding"]
scope: ["RoPE-based LLMs", "context window extension", "positional encoding interpolation"]
benchmarks_used: ["perplexity-pg19", "perplexity-proofpile", "passkey-retrieval", "boolq", "piqa", "race", "winogrande"]
models_introduced: []
models_evaluated: ["llama-7b", "llama-13b", "llama-33b", "llama-65b"]
key_claims:
  - id: C1
    claim: "Position Interpolation extends LLaMA context windows up to 32768 tokens (16x) with only 1000 fine-tuning steps"
    evidence: "Tables 1-2, Section 3.1"
    status: supported
  - id: C2
    claim: "Direct extrapolation of RoPE causes catastrophic perplexity (>10^3), while PI at step 0 already achieves <20 perplexity for 4x extension"
    evidence: "Table 1 (7B/2048 row vs 7B/8192/PI), Table 3 (step 0)"
    status: supported
  - id: C3
    claim: "The interpolation bound on attention score deviation is at least ~600x smaller than the extrapolation bound"
    evidence: "Theorem 2.1, Equations 5-8, Appendix B"
    status: supported
  - id: C4
    claim: "Extended models achieve full effective context window (kmax = L') after only 200 fine-tuning steps on passkey retrieval"
    evidence: "Table 4, Section 3.3"
    status: supported
  - id: C5
    claim: "Models extended to 8192 show <2% degradation on original benchmarks within the 2048 context window"
    evidence: "Table 5, Section 3.4"
    status: supported
  - id: C6
    claim: "Perplexity consistently improves with longer context windows on PG-19, extending to 32768 without diminishing for 7B and 13B"
    evidence: "Table 1, Section 3.2"
    status: supported
  - id: C7
    claim: "Fine-tuning results are insensitive to dataset choice (Pile vs RedPajama)"
    evidence: "Table 5, Section 3.4"
    status: supported
cross_references:
  - target: 2024-01-roformer-rope
    type: extends
    detail: "PI modifies the position indices fed to RoPE to enable context extension beyond the pretrained range"
  - target: 2023-02-llama-open-efficient-foundation
    type: extends
    detail: "PI is developed specifically to extend the LLaMA model family's 2048-token context window"
  - target: 2023-06-rope-ntk
    type: concurrent
    detail: "NTK-aware scaling addresses the same RoPE extension problem with a different interpolation strategy that preserves high-frequency components"
  - target: 2024-05-yarn-context-extension
    type: extended-by
    detail: "YaRN improves on PI by combining NTK-aware interpolation with attention scaling"
  - target: 2024-07-longrope-context-extension
    type: extended-by
    detail: "LongRoPE replaces PI's uniform linear interpolation with non-uniform per-dimension rescale factors found via evolutionary search, extending context to 2048k tokens"
  - target: 2024-06-effective-long-context-scaling
    type: contradicts
    detail: "Xiong et al. show RoPE base frequency adjustment (ABF) outperforms PI on perplexity (6.323 vs 6.341 on 32K books), FIRST-SENTENCE-RETRIEVAL (ABF maintains to 32K while PI degrades at 24K+), and downstream tasks (HumanEval: 17.07 vs 15.24)"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: extended-by
    detail: "DroPE lists PI as a primary RoPE-scaling baseline and outperforms it"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi avoids the extrapolation problem by design via linear attention biases; PI addresses it post-hoc for existing RoPE-based models"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention uses random-access retrieval tokens for long context; PI provides the passkey retrieval evaluation task used in this paper"
  - target: 2020-04-compressive-transformer-pg19
    type: uses-benchmark
    detail: "Uses PG-19 (introduced by Rae et al., 2020) as the primary long-sequence perplexity benchmark for evaluating context window extension"
open_questions:
  - question: "Does position interpolation lose high-frequency information critical for local token distinctions?"
    addressed_by: 2023-06-rope-ntk
  - question: "Can regularization of max_j|h_j| during pretraining mitigate or resolve extrapolation failures entirely?"
    addressed_by: null
  - question: "Can Position Interpolation be applied to other types of position encodings such as learned position embeddings?"
    addressed_by: null
  - question: "What is the upper limit of context extension factor beyond 32x?"
    addressed_by: 2024-05-yarn-context-extension
---
# Extending Context Window of Large Language Models via Position Interpolation

**Authors:** Shouyuan Chen, Sherman Wong, Liangjian Chen, Yuandong Tian (Meta Platforms Inc.)
**Date:** June 2023, arXiv:2306.15595v2

---

## Core Research Problem

Large language models using RoPE-based positional encodings (e.g., LLaMA) are pretrained with a fixed context window (2048 tokens for LLaMA) and suffer **catastrophic performance degradation** when inference sequences exceed this length. Direct extrapolation -- simply using the model at longer position indices -- causes perplexity to exceed 10^3, comparable to an untrained model (Table 1, Section 2.2). This occurs even for nearby tokens: a question at position 3000 cannot be answered from evidence at position 2900, despite the relative distance being well within the training range.

The root cause lies in the mathematical structure of RoPE. The attention score between positions can be expressed as a basis expansion:

> a(s) = Re[sum_{j=0}^{d/2-1} h_j e^{is*theta_j}]

where s = m - n is the relative distance, theta_j = 10000^{-2j/d}, and h_j are complex coefficients derived from query and key vectors (Equation 3, Section 2.2). The trigonometric family {phi_j(s) = e^{is*theta_j}} with sufficiently large d forms a **universal approximator**: coefficients {h_j} learned during pretraining produce well-behaved attention scores within [0, L] but can generate arbitrarily large values outside this range (Figure 2, middle). The existing extrapolation bound from Su et al. (2021) decays with relative distance but depends on |h_j| and can be vacuously large.

Alternative approaches exist but are not applicable to existing pretrained models. ALiBi (Press et al., 2022) and LeX (Sun et al., 2022) enable length extrapolation by design but require training from scratch. Direct fine-tuning on longer contexts is extremely inefficient: after 10,000 training steps, the effective context window grows only from 2048 to 2560 (Table 4). The core challenge is: **how to extend the context window of existing pretrained RoPE-based LLMs efficiently, without retraining from scratch.**

---

## Problem Solutions

Position Interpolation proposes a conceptually simple solution: **linearly down-scale input position indices** so they fall within the original pretrained range, rather than extrapolating beyond it.

1. **Position index rescaling.** For a model pretrained with context window L and target context window L', replace every position index m with mL/L' before computing RoPE. This maps all indices from [0, L') back to [0, L), ensuring inputs to RoPE remain within the distribution seen during pretraining.
2. **Theoretical stability guarantee.** The interpolation bound on attention score deviation is ~600x smaller than the extrapolation bound (Theorem 2.1), because interpolation between known grid points is smooth and well-bounded thanks to the smoothness of trigonometric basis functions.
3. **Minimal fine-tuning.** After rescaling, the model needs only ~1000 fine-tuning steps on next-token prediction to fully adapt to the extended context window, starting from a good initialization.

---

## Approach Details

### Method

Position Interpolation replaces the RoPE function f(x, m) with:

> f'(x, m) = f(x, mL/L')

where L is the original context window size and L' is the target extended size (Equation 4, Section 2.3). This is the only modification: no architectural changes, no new parameters, no modifications to the attention mechanism. Position indices from [0, L') are compressed to [0, L), and the maximum relative distance between any two tokens is reduced from L' to L.

After rescaling, the model is fine-tuned using next-token prediction on the extended context window. The fine-tuning adapts the model to the denser interpolated position encodings rather than acquiring new knowledge, which explains why convergence is fast and dataset-insensitive (Section 2.3).

### Key Technical Components

**Drop-in position rescaling.** The only change is dividing position indices by L'/L before passing to RoPE. This preserves full compatibility with existing optimizations: Flash Attention (Dao et al., 2022), Fully Sharded Data Parallel (Zhao et al., 2023), and the original LLaMA architecture are all reused without modification (Section 2.3).

**Training hyperparameters.** Fine-tuning uses AdamW with beta_1 = 0.9, beta_2 = 0.95, weight decay = 0. Linear learning rate warmup over 20 steps from 10% of maximum. Maximum learning rate: 2 * 10^{-5} for 7B/13B, 10^{-5} for 33B/65B. Global batch size: 64 for extending 7B/13B/33B to 8192; 128 for all other configurations (Section 3.1).

**Dataset insensitivity.** Fine-tuning on the Pile and RedPajama produce comparable results on downstream benchmarks, suggesting the model adapts to the new position encoding distribution rather than learning new knowledge (Table 5, Section 3.4).

### Theoretical Analysis

**Theorem 2.1 (Interpolation bound).** For the attention score a(s) = Re[sum_{j=0}^{d/2-1} h_j e^{is*theta_j}] where theta_j = c^{-2j/d} with c = 10000, the interpolation value for s in [s1, s2] between known grid points satisfies:

> |a(s) - a_linear(s)| <= d * (max_j |h_j|) * (s - s1)(s2 - s) / (8 ln c)

where a_linear(s) is the linear interpolation between a(s1) and a(s2), which are well-behaved due to pretraining (Equations 5-6). For integer grid points, (s - s1)(s2 - s) <= 1/4, giving:

> |a(s) - a_linear(s)| <= d * max_j|h_j| / 294.73

The proof uses Taylor expansion to bound the second derivative |a''(s)| <= (max_j |h_j|) * d / (4 ln c), then applies the remainder formula (Appendix A).

**Comparison with extrapolation bound.** The RoPE extrapolation bound from Su et al. (2021) is:

> |a(s)| <= 2 * (max_j |h_j|) * B(s), where B(s) = sum_{k=0}^{d/2-1} |A_{k+1}(s)|

Numerically, B(s)/d >= 1 for all s and is much larger at many positions (Figure 5, Appendix B). The interpolation bound is therefore at least 2 * 294.73 ~ **600x smaller** than the extrapolation bound in the LLaMA 7B setting (d = 128), explaining why interpolation is far more stable (Section 2.3).

**Potential for regularization.** Both bounds share the common term max_j|h_j|. Regularizing this during pretraining (e.g., via ridge regression) could mitigate extrapolation failures entirely, but no existing pretraining technique leverages this (Section 2.3, noted as future work).

### Experimental Setup

**Models.** LLaMA 7B, 13B, 33B, and 65B extended to context windows of 8192, 16384, and 32768 (up to 16x the original 2048). No architectural modifications beyond position index rescaling (Section 3.1).

**Fine-tuning.** 1000 steps for PI, 10000 steps for direct fine-tuning baseline. Trained on the Pile (Gao et al., 2020). Hardware: 32 A100 GPUs for 7B/13B/33B to 8192; 128 A100 GPUs for all other configurations (Section 3.1).

**Evaluation.** (1) Perplexity on PG-19 books corpus (100 test documents) and Arxiv Math Proof-pile (128 documents, truncated to 32768 tokens), using sliding window with stride S = 256 (Section 3.2). (2) Passkey retrieval for effective context window measurement, following Mohtashami & Jaggi (2023), with 32 uniformly spaced distances and 10 trials each (Section 3.3). (3) GovReport long document summarization (972 evaluation documents, truncated to 15000 tokens), evaluated with ROUGE-1/2/L (Section 3.5). (4) Zero-shot performance on BoolQ, PIQA, Race-M, Race-H, and WinoGrande within the original 2048 context window (Section 3.4).

### Key Results

**Perplexity on PG-19 (Table 1):**

| Size | Context Window | Method | Eval 2048 | Eval 4096 | Eval 8192 | Eval 16384 | Eval 32768 |
|---|---|---|---|---|---|---|---|
| 7B | 2048 | None | 7.20 | >10^3 | >10^3 | >10^3 | >10^3 |
| 7B | 8192 | FT | 7.21 | 7.34 | 7.69 | - | - |
| 7B | 8192 | PI | 7.13 | 6.96 | 6.95 | - | - |
| 7B | 16384 | PI | 7.11 | 6.93 | 6.82 | 6.83 | - |
| 7B | 32768 | PI | 7.23 | 7.04 | 6.91 | 6.80 | 6.77 |
| 13B | 32768 | PI | 6.54 | 6.40 | 6.28 | 6.18 | 6.09 |
| 33B | 16384 | PI | 5.87 | 5.74 | 5.67 | 5.68 | - |
| 65B | 8192 | PI | 5.42 | 5.32 | 5.37 | - | - |

- On PG-19, perplexity decreases monotonically with evaluation context window size up to 32768 for 7B and 13B models, confirming genuine long-context utilization.
- Direct fine-tuning (FT) produces perplexity *regression* at longer windows (7.69 at 8192 vs 7.20 at 2048 for 7B), indicating it fails to leverage extended context.
- Perplexity reductions from extending 2048 to 16384: -0.28 (7B PG-19), -0.50 (7B Proof-pile), -0.27 (13B PG-19), -0.48 (13B Proof-pile), -0.14 (33B PG-19), -0.42 (33B Proof-pile) (Section 3.2).

**Convergence speed (Table 3, PG-19):**

| Size | Context Window | Step 0 | Step 200 | Step 400 | Step 600 | Step 800 | Step 1000 |
|---|---|---|---|---|---|---|---|
| 7B | 8192 | 16.10 | 7.12 | 7.10 | 7.02 | 6.99 | 6.95 |
| 7B | 16384 | 112.13 | 7.05 | 6.93 | 6.88 | 6.84 | 6.83 |

- Without fine-tuning (step 0), PI to 8192 already achieves perplexity ~16, vs >10^3 for direct extrapolation.
- At 200 steps, models surpass the original 2048 perplexity (7.20), indicating full context utilization.

**Effective context window via passkey retrieval (Table 4):**

| Size | Context Window | Method | 200 steps | 1000 steps | 10000 steps |
|---|---|---|---|---|---|
| 7B | 8192 | FT | 1792 | 2304 | 2560 |
| 7B | 8192 | PI | 8192 | 8192 | - |
| 7B | 16384 | PI | 16384 | 16384 | - |
| 7B | 32768 | PI | 32768 | 32768 | - |
| 33B | 8192 | PI | 8192 | 8192 | - |
| 33B | 16384 | PI | 16384 | 16384 | - |

- All PI-extended models achieve full effective context window (kmax = L') after 200 fine-tuning steps.
- Direct fine-tuning extends kmax from 2048 to only 2560 after 10,000 steps.

**Original benchmark performance (Table 5):**

| Size | Context Window | BoolQ | PIQA | Race-M | Race-H | WinoGrande |
|---|---|---|---|---|---|---|
| 7B | 2048 (original) | 76.1 | 78.9 | 55.7 | 42.2 | 69.6 |
| 7B | 8192 (PI, Pile) | 73.2 | 78.2 | 53.8 | 41.7 | 69.0 |
| 7B | 8192 (PI, RedPajama) | 75.5 | 77.4 | 54.5 | 41.5 | 68.1 |
| 33B | 2048 (original) | 81.6 | 80.2 | 61.1 | 45.9 | 76.2 |
| 33B | 8192 (PI, Pile) | 80.2 | 80.7 | 60.2 | 45.7 | 75.9 |

- Models extended to 8192 show degradation of up to 2% on original benchmarks.
- Larger extension factors show more regression: 7B extended to 32768 drops to 64.7 on BoolQ (from 76.1) and 50.1 on Race-M (from 55.7).
- Dataset choice (Pile vs RedPajama) does not significantly affect benchmark performance.

**GovReport summarization (Table 6):**

| Model | Context Window | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---|---|---|---|
| CoLT5 Base | 16K | 58.7 | 29.6 | 31.4 |
| CoLT5 XL | 16K | 61.3 | 32.2 | 33.8 |
| LLaMA-7B Extended | 16K | 60.0 | 28.0 | 29.5 |

- PI-extended LLaMA-7B achieves competitive ROUGE-1 (60.0), between CoLT5 Base and CoLT5 XL, confirming effective long-document utilization.

---

## Limitations and Failure Modes

1. **Performance regression on original context window.** Position Interpolation compresses position encodings into a narrower region, causing minor perplexity regression at the original 2048 window. On Proof-pile, degradation ranges from 0.01 to 0.05 across all model sizes (Tables 1-2, Section 3.2).

2. **Larger extension factors cause greater benchmark regression.** Extending 7B to 32768 (16x) causes substantial drops on some benchmarks: BoolQ degrades from 76.1 to 64.7 (-11.4 points), Race-M from 55.7 to 50.1 (-5.6 points) (Table 5). The paper notes BoolQ "may require models to pay close attention to word ordering in a short reference paragraph" (Section 3.4).

3. **Perplexity uptick at 32768 on Proof-pile.** For both 7B and 13B models extended to 32768, perplexity at the 32768 evaluation window increases compared to 16384 on the Proof-pile dataset (7B: 2.48 at 32768 vs 2.24 at 16384; 13B: 2.35 vs 2.15), though PG-19 shows monotonic improvement (Table 2). The paper does not discuss this discrepancy.

4. **Uniform interpolation across all frequency dimensions.** Linear position rescaling applies the same compression factor to all RoPE frequency components uniformly. High-frequency components (small theta_j), which encode fine-grained local distinctions, are compressed identically to low-frequency components. This limitation motivated the NTK-aware scaling approach (kaiokendev, 2023) and later YaRN (Peng et al., 2023).

5. **No evaluation on retrieval-oriented or multi-hop tasks.** The paper evaluates on perplexity, passkey retrieval, and summarization, but does not test whether extended models can effectively retrieve and reason over information distributed across the full extended context.

6. **Limited to RoPE-based models.** The method is specific to models using RoPE positional encoding. The paper conjectures that a similar interpolation approach could work for learnable position embeddings (e.g., OPT) but does not test this (Section 4).

---

## Conclusions

### Contributions

1. **Position Interpolation method.** Introduced a simple, parameter-free technique for extending context windows of pretrained RoPE-based LLMs by linearly rescaling position indices to the original range, requiring no architectural changes and reusing existing infrastructure (Section 2.3).

2. **Theoretical stability guarantee.** Proved that the interpolation bound on attention score deviation is ~600x smaller than the extrapolation bound (Theorem 2.1), providing a mathematical explanation for why interpolation succeeds where extrapolation fails catastrophically.

3. **Efficient adaptation.** Demonstrated that only 1000 fine-tuning steps suffice to extend LLaMA context windows up to 16x (32768 tokens), with models achieving full effective context windows after as few as 200 steps on passkey retrieval (Tables 3-4).

4. **Effective long-context utilization.** Extended models show consistent perplexity improvements with longer evaluation windows on PG-19, confirming genuine use of extended context, and achieve competitive ROUGE scores on GovReport summarization (Tables 1, 6).

5. **Preserved original capabilities.** Models extended to 8192 retain performance within 2% of the original on standard benchmarks within the 2048 context window, making them practical as general-purpose models (Table 5).

6. **Generality across model scales.** Results hold consistently from 7B to 65B parameters and extension factors from 4x to 16x (Tables 1-2, 4).

### Implications

1. **Extrapolation failure is a position encoding problem, not a fundamental limitation.** The paper reaffirms Vaswani et al. (2017)'s hypothesis that Transformers can handle sequences longer than those seen during training, provided position encodings are handled appropriately. The previously observed failure of length extrapolation is attributable to extrapolation of positional encodings specifically.

2. **Interpolation as a general principle.** Together with Dosovitskiy et al. (2021)'s interpolation of learned position embeddings in Vision Transformers, these results suggest that interpolation of positional representations is a broadly applicable strategy for extending pretrained models to longer sequences.

3. **Regularization as a potential pretraining strategy.** The shared max_j|h_j| term in both interpolation and extrapolation bounds suggests that regularizing query-key product magnitudes during pretraining could improve both interpolation and extrapolation stability -- a direction not yet explored (speculative, Section 2.3).

---

## Key Claims

**C1. PI extends LLaMA to 32768 context with 1000 fine-tuning steps.** LLaMA 7B and 13B models extended via PI to 32768 tokens achieve perplexity of 6.77 and 6.09 on PG-19 (improved from original 7.20 and 6.59 at 2048) after 1000 fine-tuning steps on the Pile (Table 1, Section 3.1). Status: **supported**.

**C2. Interpolation avoids catastrophic perplexity explosion.** At step 0 (no fine-tuning), PI to 8192 achieves perplexity ~16 on PG-19, vs >10^3 for direct extrapolation. At step 0 for PI to 16384, perplexity is 112.13 -- high but not catastrophic (Table 3). Status: **supported**.

**C3. Interpolation bound is ~600x smaller than extrapolation bound.** Theorem 2.1 bounds interpolation deviation at d * max_j|h_j| / 294.73, while the RoPE extrapolation bound is at least 2 * max_j|h_j| * d. The ratio is at least 2 * 294.73 ~ 600x (Section 2.3, Appendix B). Status: **supported**.

**C4. Full effective context window after 200 fine-tuning steps.** On passkey retrieval, all PI-extended models (7B and 33B, up to 32768 context) achieve kmax = L' after 200 steps. Direct fine-tuning achieves only kmax = 2560 after 10,000 steps (Table 4, Section 3.3). Status: **supported**.

**C5. Original benchmark degradation <2% for 8192 extension.** LLaMA 7B extended to 8192 shows at most 2.9 points degradation on BoolQ (76.1 to 73.2) and smaller differences on other benchmarks. LLaMA 33B extended to 8192 shows at most 1.4 points degradation (Table 5, Section 3.4). Status: **supported**.

**C6. Perplexity improves monotonically with context window on PG-19.** For 7B and 13B models extended to 32768, PG-19 perplexity decreases at every evaluation window size from 2048 through 32768 without diminishing returns (Table 1, Section 3.2). Status: **supported**.

**C7. Fine-tuning is dataset-insensitive.** LLaMA 7B extended to 8192 using PI, fine-tuned on the Pile vs RedPajama, achieves comparable benchmark scores (e.g., BoolQ 73.2 vs 75.5, PIQA 78.2 vs 77.4), suggesting the model adapts to new position distributions rather than learning new knowledge (Table 5, Section 3.4). Status: **supported**.

---

## Open Questions

1. **Does linear interpolation degrade high-frequency position information?** By compressing all position indices uniformly, PI reduces the resolution of high-frequency RoPE components that encode fine-grained local token distinctions. The NTK-aware scaling approach (kaiokendev, 2023) was specifically motivated by this concern. Addressed by: `2023-06-rope-ntk`.

2. **Can regularization of max_j|h_j| during pretraining resolve extrapolation failures?** Both the interpolation and extrapolation bounds share the common factor max_j|h_j|. The authors note that ridge regression with proper regularization can keep extrapolated values comparable to those within [0, L] (Section 2.3), but no existing pretraining technique exploits this. Unresolved.

3. **Is Position Interpolation applicable to other position encoding types?** The paper conjectures it could work for learned position embeddings (e.g., OPT) and notes the precedent of Dosovitskiy et al. (2021) interpolating learned embeddings in Vision Transformers (Section 4). Not tested. Unresolved.

4. **What is the upper limit of context extension factor?** The paper demonstrates up to 32x (2048 to 65536 is not tested; 32768 = 16x is the maximum). Perplexity on Proof-pile increases at 32768 for 32768-extended models, suggesting potential limits at very large extension factors. Partially addressed by YaRN, which extends further. Addressed by: `2024-05-yarn-context-extension`.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding used by LLaMA and the direct target of PI's rescaling. PI builds on RoPE's mathematical formulation (Equations 1-2) and improves upon its extrapolation bound (Section 2.2, Equation 8).
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer paper that hypothesized models can extrapolate to longer sequences. PI reaffirms this hypothesis by showing that the failure was due to positional encoding extrapolation, not a fundamental model limitation.

### Target Model

- **Touvron et al. (2023)** -- *LLaMA: Open and Efficient Foundation Language Models.* The family of models extended by PI. All experiments use LLaMA 7B through 65B with their original 2048-token context window.

### Length Extrapolation Alternatives

- **Press et al. (2022)** -- *Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation.* ALiBi enables length extrapolation by design but requires training from scratch; not applicable to existing RoPE-based models like LLaMA. Also provides the sliding window evaluation methodology used for perplexity measurement (stride S = 256).
- **Sun et al. (2022)** -- *A Length-Extrapolatable Transformer (LeX).* Another extrapolation-capable architecture, similarly not retroactively applicable to pretrained RoPE models.
- **Haviv et al. (2022)** -- *Transformer Language Models Without Positional Encodings Still Learn Positional Information.* Shows NoPE transformers learn positional information implicitly, referenced in the context of length extrapolation research.

### Concurrent Work

- **kaiokendev (2023)** -- *SuperHOT.* Concurrent blogpost that independently proposes interpolating RoPE positional encodings to extend context from 2K to 8K. PI provides theoretical justification and scales to 65B with full fine-tuning, while SuperHOT demonstrated community feasibility with LoRA.

### Related Interpolation Technique

- **Dosovitskiy et al. (2021)** -- *ViT: An Image is Worth 16x16 Words.* Proposed interpolating learned position embeddings for Vision Transformers at higher resolutions (up to 4x). PI differs by interpolating position indices (not embedding weights) for RoPE encodings and achieves up to 16x extension.

### Training Data and Infrastructure

- **Gao et al. (2020)** -- *The Pile: An 800GB Dataset of Diverse Text for Language Modeling.* Primary fine-tuning dataset for all PI experiments.
- **Together Computer (2023)** -- *RedPajama.* Alternative fine-tuning dataset used in ablation to demonstrate dataset insensitivity (Section 3.4).
- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Used for efficient training of extended models.
- **Zhao et al. (2023)** -- *PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel.* Distributed training framework used for all experiments.

### Evaluation Benchmarks

- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Introduces PG-19 book corpus, the primary long-sequence perplexity benchmark.
- **Azerbayev et al. (2022)** -- *Proof-Pile.* Arxiv math dataset providing the second perplexity evaluation benchmark.
- **Mohtashami & Jaggi (2023)** -- *Landmark Attention: Random-Access Infinite Context Length for Transformers.* Provides the passkey retrieval evaluation task used to measure effective context window size.
- **Huang et al. (2021)** -- *Efficient Attentions for Long Document Summarization.* Introduces the GovReport dataset used for long document summarization evaluation.
- **Shaham et al. (2022)** -- *SCROLLS: Standardized CompaRison Over Long Language Sequences.* Provides the leaderboard with CoLT5 baselines for GovReport summarization comparison.

### Efficient Attention and Related Models

- **Ainslie et al. (2023)** -- *CoLT5: Faster Long-Range Transformers with Conditional Computation.* Provides GovReport summarization baselines (CoLT5 Base R1=58.7, CoLT5 XL R1=61.3) against which PI-extended LLaMA is compared.
- **Hu et al. (2021)** -- *LoRA: Low-Rank Adaptation of Large Language Models.* Referenced as a parameter-efficient fine-tuning method shown by the community to work with position interpolation (concurrent work discussion).
