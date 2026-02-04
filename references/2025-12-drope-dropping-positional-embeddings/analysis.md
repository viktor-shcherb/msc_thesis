---
title: "Extending the Context of Pretrained LLMs by Dropping Their Positional Embeddings"
authors: "Gelberg, Eguchi, Akiba, Cetin"
year: 2025
venue: "arXiv preprint"
paper_type: preprint
categories: ["context-extension", "position-encoding"]
scope: ["RoPE-based LLMs", "zero-shot context extension", "NoPE transformers"]
benchmarks_used: ["niah", "ruler", "longbench", "arc", "hellaswag", "piqa", "winogrande"]
models_introduced: []
models_evaluated: ["smollm-360m", "smollm-1.7b", "llama-2-7b"]
key_claims:
  - id: C1
    claim: "Positional embeddings provide a critical inductive bias that accelerates pretraining convergence; NoPE transformers develop positional bias at a bounded rate"
    evidence: "Theorem 3.4, Propositions 3.2-3.3, Figures 3-4, Section 3"
    status: supported
  - id: C2
    claim: "RoPE-scaling methods must compress low frequencies to keep phases in-distribution, inevitably shifting semantic attention heads at large distances and preventing zero-shot context extension"
    evidence: "Section 4.1, Figures 5-8, Observation 2"
    status: supported
  - id: C3
    claim: "YaRN's zero-shot behavior is equivalent to cropping the context to the pretraining length"
    evidence: "Figure 5, Section 4"
    status: supported
  - id: C4
    claim: "Dropping all positional embeddings after pretraining with short recalibration enables zero-shot context extension without long-context finetuning"
    evidence: "Tables 1-3, Table 10, Figures 1-2, Section 5"
    status: supported
  - id: C5
    claim: "DroPE outperforms PI, RoPE-NTK, YaRN, ALiBi, and RNoPE-SWA on zero-shot NIAH at 2x training context"
    evidence: "Table 1, Section 5.1"
    status: unvalidated
  - id: C6
    claim: "DroPE preserves in-context performance after recalibration, recovering >95% of original model performance after <5B tokens (0.8% of SmolLM-360M budget)"
    evidence: "Table 5, Figures 9-10, Section 5.1"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Builds on the transformer architecture; reinterprets the role of positional embeddings as a transient training scaffold"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "DroPE removes RoPE entirely after pretraining, answering why RoPE helps training (optimization, not expressivity)"
  - target: 2023-06-pi-positional-interpolation
    type: evaluates
    detail: "PI is one of three primary RoPE-scaling baselines; DroPE substantially outperforms it on all tasks"
  - target: 2023-06-rope-ntk
    type: evaluates
    detail: "RoPE-NTK is a primary baseline; DroPE outperforms it on NIAH and LongBench"
  - target: 2024-05-yarn-context-extension
    type: contradicts
    detail: "Shows YaRN's zero-shot behavior is equivalent to context cropping (Figure 5); DroPE outperforms YaRN on LongBench avg (30.52 vs 19.94, Table 2)"
  - target: 2022-04-alibi-train-short-test-long
    type: evaluates
    detail: "ALiBi is evaluated as an alternative PE architecture baseline; DroPE outperforms it on all NIAH tasks (Table 1)"
  - target: 2024-10-ruler-context-size
    type: uses-benchmark
    detail: "Uses RULER's multi-query, multi-key, and multi-value NIAH tasks as primary long-context evaluation"
  - target: 2024-08-longbench-bilingual-benchmark
    type: uses-benchmark
    detail: "Uses four LongBench tasks (MultiFieldQA, MuSiQue, GovReport, LCC) for downstream long-context evaluation"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "Uses needle-in-a-haystack evaluation framework for pressure-testing context utilization"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Cites Lost in the Middle as evidence that RoPE-scaling methods degrade when information is deep in the context (Section 4)"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Uses Llama 2 7B to demonstrate DroPE's scalability to billion-parameter pretrained models (Table 3)"
  - target: 2022-12-nope-transformers-learn-positions
    type: extends
    detail: "Builds on the NoPE finding that causal LMs learn positions without explicit PE; uses PE removal after pretraining for context extension"
  - target: 2023-12-positional-encoding-length-generalization
    type: extends
    detail: "Builds on Kazemnejad et al.'s theoretical proof that NoPE can represent both absolute and relative PEs, establishing that NoPE has the same expressivity as RoPE; DroPE shows the gap is in optimization, not expressivity"
  - target: 2025-04-attention-sink-emerges
    type: complementary
    detail: "Gu et al. show PE type does not affect attention sink emergence — even NoPE models develop sinks — providing independent evidence that PEs and attention sinks serve orthogonal roles"
open_questions:
  - question: "Does DroPE's advantage hold with long-context finetuning, or only in zero-shot settings?"
    addressed_by: null
  - question: "Can DroPE scale to models significantly larger than 7B parameters?"
    addressed_by: null
  - question: "How does DroPE interact with instruction tuning and RLHF?"
    addressed_by: null
  - question: "Can hybrid approaches (RoPE in some layers, NoPE in others) combine the benefits of both?"
    addressed_by: null
---

# Extending the Context of Pretrained LLMs by Dropping Their Positional Embeddings

**Authors:** Yoav Gelberg, Koshi Eguchi, Takuya Akiba, Edoardo Cetin (Sakana AI, University of Oxford)
**Date:** December 2025, arXiv:2512.12167

---

## Core Research Problem

Transformer-based language models suffer sharp performance degradation when inference sequence lengths exceed the pretraining context window. This is directly caused by their reliance on explicit positional embeddings (PEs), particularly Rotary Positional Embeddings (RoPE), which become out-of-distribution at unseen sequence lengths. The quadratic cost of self-attention makes pretraining at long sequence lengths computationally intractable at scale.

Existing solutions -- RoPE-scaling methods such as PI (Chen et al., 2023), RoPE-NTK (bloc97, 2023), and YaRN (Peng et al., 2023) -- introduce targeted rescaling of RoPE frequencies to avoid unseen rotations at longer sequences. However, these methods still require expensive long-context finetuning to meaningfully use tokens beyond the original sequence length and fail to generalize zero-shot to downstream tasks (Lu et al., 2024b). Alternative architectures without positional embeddings (NoPE transformers) avoid the rescaling problem but introduce "notable performance and stability trade-offs" that prevent wide adoption (Haviv et al., 2022; Kazemnejad et al., 2023).

The core challenge is: **how to enable zero-shot context extension -- using contexts beyond pretraining length without additional long-context finetuning -- while preserving in-context performance.**

---

## Problem Solutions

DroPE proposes a fundamentally different paradigm: **remove all positional embeddings from a pretrained transformer and perform a short recalibration phase at the original context length.** The method is motivated by three key observations:

1. **Observation 1 -- PEs accelerate training:** Positional embeddings provide a critical inductive bias that significantly facilitates pretraining convergence. NoPE transformers are equally expressive but develop positional bias at a bounded, slower rate due to bounded gradients of the attention positional bias functional at initialization (Theorem 3.4).

2. **Observation 2 -- PEs prevent context extension:** All RoPE-scaling methods must compress low frequencies to keep positional phases in-distribution. This compression shifts semantic attention heads at large relative distances, causing failures on downstream tasks requiring information deep in the context. This effect is inevitable for any post-hoc frequency scaling approach (Section 4.1).

3. **Observation 3 -- PEs can be safely removed post-training:** Positional embeddings are not an inherent requirement of effective language modeling and can be removed after pretraining. A short recalibration phase at the original context size recovers in-context capabilities while unlocking zero-shot generalization to unseen sequence lengths (Section 5).

---

## Approach Details

### Method

DroPE operates in two phases:

- **Phase 1 (Pretraining):** Train a standard RoPE transformer normally, leveraging the inductive bias of positional embeddings for efficient convergence.
- **Phase 2 (Recalibration):** Remove **all** positional embeddings from **every** layer and continue training for a small fraction of the original budget at the original context length.

Two deployment modes:

1. **Integrated at no extra cost:** Replace the final portion of the pretraining schedule with PE-free training (e.g., last 2B of 16.8B tokens for the from-scratch model).
2. **Adapting pretrained models:** Perform continued pretraining without PEs using 0.5--5% of the original pretraining budget.

### Key Technical Components

**Recalibration budget.** The required recalibration varies by scale:
- From-scratch (494M, 16.8B tokens): last 2.1B tokens (12.5%) at no extra cost
- SmolLM-360M (600B tokens pretrained): 30B/60B/120B tokens; >95% of in-context performance recovered after <5B tokens (0.8% of original budget)
- SmolLM-1.7B (1T tokens pretrained): 20B tokens (2%)
- Llama2-7B (reported as 4T tokens pretrained): 20B tokens (0.5%)

**QKNorm.** For extended recalibration periods (SmolLM experiments), query-key normalization (Henry et al., 2020) is added after dropping PEs to stabilize training at higher learning rates and mitigate gradient spikes. Ablation study (Table 11, Appendix D.3) shows QKNorm is not needed at lower learning rates (3x10^-4) but becomes essential at higher rates (10^-3) where training without it diverges (final loss 6.334 vs 2.496 with QKNorm).

**Softmax temperature scaling at inference.** Following Wang et al. (2024), a single scalar logit temperature is tuned on a held-out set at the target length to calibrate attention for longer sequences. The optimal scale follows a logarithmic form:

> `beta* = 1 + c * ln(s)`

where `s = C_test / C_train` is the context extension factor. For the from-scratch DroPE model, `c = 0.412`; for SmolLM-DroPE, `c = 0.103` (Appendix C.2).

### Theoretical Analysis

**Theorem 3.4 (Bounded positional bias in NoPE transformers).** Define the prefix-spread of hidden states at layer `l` as:

> `Delta_h^(l) := max_{1 <= j <= i <= T} || h_bar_i^(l) - h_j^(l) ||`

For NoPE transformers, there exists epsilon > 0 and constants C1, C2, C3 such that if initial embeddings have `Delta_h^(1) <= epsilon`, then for all layers `l <= L`:

> `Delta_h^(l) <= C1*epsilon`, `|A^c| <= C2*epsilon`, `||dA^c/dW_Q||, ||dA^c/dW_K|| <= C3*epsilon`

with high probability over initialization. Constants depend only on layers and heads, **not** on sequence length. This explains why NoPE transformers develop positional patterns slowly: at initialization, embedding uniformity propagates through the network, keeping attention maps near-uniform (alpha_ij ~ 1/i).

**Proposition 3.2 (NoPE pathology on constant sequences).** For NoPE transformers on identical input tokens: (1) all attention heads are uniform (alpha_ij = 1/i), (2) query and key gradients vanish, (3) positional bias A^c = 0 and its gradients are zero, (4) output is constant across positions.

**Proposition 3.3 (RoPE breaks uniformity).** For any non-degenerate RoPE attention head, even on constant input sequences, there exist positional weights c for which A^c > 0 and ||grad_theta A^c|| > 0. RoPE rotations break attention uniformity and provide non-zero gradients even in the worst case.

### Experimental Setup

**From-scratch experiments:** 494M parameter Qwen2-style transformer (24 layers, 14 attention heads, 2 KV heads, head dimension 64, hidden size 896) trained on 16.8B FineWeb tokens at context length 1024 using AdamW with learning rate 3x10^-4. DroPE applied at step 14K of 16K total (last 2K steps = 2.1B tokens) with learning rate 10^-3 (Table 4). Baselines: RoPE, NoPE, ALiBi, RNoPE-SWA transformers, all trained from scratch on the same data for the same number of tokens.

**Pretrained model experiments:**
- SmolLM-360M (362M params, 32 layers, 15 heads, 5 KV heads, context 2048, pretrained on 600B SmolLM corpus tokens): recalibrated with 30B/60B/120B tokens on FineWeb-Edu, QKNorm enabled, learning rate 10^-3, batch size 512
- SmolLM-1.7B: recalibrated with 20B tokens
- Llama2-7B: recalibrated with 20B tokens

**Evaluation:**
- **RULER NIAH** (multi-query, multi-key, multi-value): 500 trials per setting at 2x, 4x, 8x training context
- **LongBench** tasks: MultiFieldQA, MuSiQue, GovReport, LCC
- **Standard LM benchmarks** (in-context): ARC-E/C, HellaSwag, OpenBookQA, PIQA, WinoGrande (via LightEval harness)

### Key Results

**Zero-shot NIAH at 2x training context (from scratch, Table 1):**

| Method | MultiQuery | MultiKey | MultiValue |
|---|---|---|---|
| RoPE transformer | 0.0 | 0.0 | 0.0 |
| RoPE + PI | 0.0 | 0.0 | 0.0 |
| RoPE + RoPE-NTK | 21.1 | 19.4 | 16.5 |
| RoPE + YaRN | 17.8 | 0.5 | 14.6 |
| ALiBi transformer | 5.2 | 0.0 | 1.1 |
| NoPE transformer | 9.2 | 36.2 | 21.4 |
| RNoPE-SWA transformer | 5.2 | 25.6 | 20.6 |
| **DroPE transformer** | **28.0** | **41.6** | **23.3** |

**SmolLM-360M long-context evaluation (Table 2):**

| Method | MultiFieldQA | MuSiQue | GovReport | LCC | NIAH | Avg. |
|---|---|---|---|---|---|---|
| SmolLM | 4.03 | 0.4 | 4.48 | 5.99 | 0.0 | 2.98 |
| SmolLM + PI | 13.68 | 2.45 | 5.67 | 11.52 | 0.0 | 6.66 |
| SmolLM + RoPE-NTK | 18.87 | 4.89 | 23.71 | 8.26 | 29.84 | 17.11 |
| SmolLM + YaRN | 20.78 | 4.77 | 15.03 | 10.87 | 48.25 | 19.94 |
| **SmolLM-DroPE** | **29.33** | **7.93** | **21.87** | **18.56** | **74.92** | **30.52** |

**Larger models (Table 3):**

| Model | Method | MultiFieldQA | MuSiQue | GovReport | Avg. |
|---|---|---|---|---|---|
| SmolLM-1.7B | Base | 4.12 | 0.50 | 4.70 | 3.11 |
| SmolLM-1.7B | RoPE-NTK | 27.58 | 3.37 | 24.65 | 18.53 |
| SmolLM-1.7B | YaRN | 27.60 | 3.90 | 17.19 | 16.23 |
| SmolLM-1.7B | **DroPE** | **32.18** | **7.53** | **24.77** | **21.49** |
| Llama2-7B | Base | 17.26 | 10.43 | 32.41 | 20.03 |
| Llama2-7B | RoPE-NTK | 21.81 | 10.91 | 32.91 | 21.88 |
| Llama2-7B | YaRN | 23.13 | 7.65 | 26.65 | 19.14 |
| Llama2-7B | **DroPE** | **25.90** | **12.88** | **39.47** | **26.08** |

**NIAH at increasing extension factors (Table 10, SmolLM-360M):**

| Method | 2x | 4x | 8x |
|---|---|---|---|
| SmolLM + RoPE-NTK | 29.84 | 14.37 | 7.19 |
| SmolLM + YaRN | 48.25 | 25.62 | 12.18 |
| SmolLM + LongRoPE2 | 44.20 | 26.20 | 16.45 |
| **SmolLM-DroPE** | **74.92** | **55.00** | **52.20** |

**In-context performance preservation (Table 5):**

| Model | ARC-E | ARC-C | HellaSwag | OpenBookQA | PIQA | WinoGrande | Avg. |
|---|---|---|---|---|---|---|---|
| SmolLM-360M | 65.6 | 36.0 | 53.8 | 37.2 | 72.0 | 53.7 | 53.1 |
| SmolLM-360M-DroPE | 67.3 | 37.6 | 53.9 | 38.0 | 71.5 | 52.3 | 53.4 |
| SmolLM-1.7B | 77.50 | 44.0 | 64.10 | 42.60 | 77.30 | 56.00 | 60.25 |
| SmolLM-1.7B-DroPE | 77.70 | 42.9 | 65.90 | 43.00 | 77.10 | 57.10 | 60.62 |

- DroPE matches or slightly exceeds original model performance on all in-context benchmarks.
- Over 95% of SmolLM-360M's in-context performance is recovered after less than 5B recalibration tokens (0.8% of original pretraining budget) (Section 5.1, Figure 10).

### Recalibration Ablation

Table 6 (Appendix D.1) reports validation perplexity for a 500M-parameter model when dropping PEs at different training stages:

| Setting | DroPE @ 0K (NoPE) | DroPE @ 8K | DroPE @ 14K | DroPE @ 16K (RoPE) |
|---|---|---|---|---|
| Val. perplexity | 23.77 | 22.42 | 21.73 | 21.72 |

Later dropping yields lower perplexity, validating the importance of retaining RoPE for most of training. DroPE @ 14K (used in experiments) achieves perplexity nearly identical to the full RoPE model (21.73 vs 21.72), while unlocking zero-shot context extension.

---

## Limitations and Failure Modes

The paper does not include an explicit limitations section. The following limitations can be identified from the experimental results:

1. **Performance still degrades at higher extension factors.** While DroPE substantially outperforms baselines, NIAH accuracy drops from 74.92% at 2x to 52.20% at 8x context extension (Table 10), indicating imperfect long-range retrieval at large extension factors.

2. **Recalibration cost, while small, is non-trivial.** Adapting SmolLM-360M requires 30--120B tokens (5--20% of original budget). For the most efficient setting (Llama2-7B at 0.5%), 20B tokens of continued pretraining are still required.

3. **Scale limited to 7B parameters.** All experiments use models up to 7B parameters. Scalability to tens or hundreds of billions of parameters is not demonstrated.

4. **QKNorm required for stability at high learning rates.** Without QKNorm, recalibration at learning rate 10^-3 diverges (Table 11). This adds an architectural modification that may interact with other model components.

5. **Softmax temperature scaling requires tuning.** The logit temperature `beta*` must be fitted on held-out data at each target length, introducing a per-length calibration step.

6. **No evaluation with instruction tuning or RLHF.** All experiments use base (non-chat) models. Interaction with alignment procedures is unknown.

7. **English-only evaluation.** All benchmarks are in English; cross-lingual generalization is not tested.

8. **RoPE-NTK outperforms DroPE on GovReport for SmolLM-360M** (23.71 vs 21.87, Table 2), suggesting DroPE is not uniformly superior on all task types.

---

## Conclusions

### Contributions

1. **Theoretical analysis of why PEs help training.** Theorem 3.4 proves that NoPE transformers propagate embedding uniformity through the network, bounding positional bias and its gradients at O(epsilon) at initialization. This explains the empirical gap between NoPE and RoPE training (Figures 3--4).

2. **Identification of why RoPE-scaling fails zero-shot.** Section 4.1 demonstrates that any post-hoc RoPE frequency scaling must compress low frequencies, inevitably shifting semantic attention heads at large distances. This failure is demonstrated both theoretically and empirically (Figures 5--8).

3. **DroPE method for zero-shot context extension.** Removing all positional embeddings after pretraining with a short recalibration phase at the original context length enables zero-shot generalization to sequences far beyond training context, without any long-context finetuning. DroPE outperforms PI, RoPE-NTK, YaRN, ALiBi, and RNoPE-SWA across all tested settings (Tables 1--3, 10).

4. **In-context performance preservation.** DroPE preserves both perplexity and downstream task performance within the original training context, matching or slightly exceeding the base model (Table 5, Figures 9--10).

5. **Scalability across model and data sizes.** Results hold from 360M to 7B parameters and from 16B to (reported) 4T pretraining tokens, with recalibration costs as low as 0.5% of the pretraining budget (Section 5.1).

### Implications

1. **Positional embeddings as transient training scaffold.** The results suggest PEs are essential for efficient training convergence but are not required for effective language modeling at inference. This challenges the conventional permanent role of PEs in transformer architectures.

2. **Stage-dependent architectural choices.** Different architectural configurations may be optimal for different stages of training and inference. Recalibration between stages can reconcile trade-offs previously considered inherent. This is speculative beyond the PE case demonstrated.

3. **Potential integration into standard training pipelines.** DroPE can be incorporated at no extra cost into pretraining recipes by replacing the final training steps with PE-free training, suggesting it could become a standard pipeline component.

---

## Key Claims

1. **C1: PEs accelerate training via inductive bias (supported).** NoPE transformers develop positional bias at a bounded rate (O(epsilon)) due to embedding uniformity propagation (Theorem 3.4), while RoPE provides non-zero positional bias gradients even on constant sequences (Proposition 3.3). Empirically validated: RoPE outperforms NoPE throughout training (Figure 3), with gradient norm gap growing in deeper layers (Figure 4).

2. **C2: RoPE-scaling inevitably shifts semantic attention (supported).** Low-frequency RoPE phases never complete a full cycle within training context, so any scaling method must choose gamma_m <= 1/s, compressing semantic heads (Section 4.1). Empirically shown: YaRN shifts attention mass in semantic heads on NIAH probes (Figure 8), while positional heads are unaffected (Figure 7).

3. **C3: YaRN zero-shot equals context cropping (supported).** YaRN and a baseline that crops input to training context length show matching perplexity and NIAH behavior -- both maintain perplexity but cannot retrieve information beyond the cropped window (Figure 5).

4. **C4: DroPE enables zero-shot context extension (supported).** DroPE outperforms all baselines on zero-shot NIAH at 2x, 4x, and 8x training context (Tables 1, 10) and on LongBench tasks up to 80x the pretraining context (Table 2). No long-context finetuning is used in any experiment.

5. **C5: DroPE outperforms all baselines on zero-shot NIAH and LongBench (unvalidated).** DroPE achieves the highest scores across all NIAH variants (Table 1), LongBench averages for SmolLM-360M (30.52 vs 19.94 for YaRN, Table 2), SmolLM-1.7B (21.49 vs 18.53 for RoPE-NTK, Table 3), and Llama2-7B (26.08 vs 21.88 for RoPE-NTK, Table 3). However, RoPE-NTK outperforms DroPE on GovReport for SmolLM-360M. Marked unvalidated pending independent replication.

6. **C6: In-context performance preserved after recalibration (supported).** SmolLM-360M-DroPE matches or exceeds SmolLM-360M on all six LM benchmarks (Table 5: 53.4 vs 53.1 avg). SmolLM-1.7B-DroPE similarly matches (60.62 vs 60.25 avg). Over 95% of performance recovered after <5B tokens (Figure 10).

---

## Open Questions

1. **Does DroPE's advantage hold with fine-tuning?** All experiments evaluate zero-shot extension. Whether DroPE + long-context finetuning outperforms RoPE-scaling + long-context finetuning is untested.

2. **Can DroPE scale to models significantly larger than 7B?** The largest model tested is Llama2-7B. Behavior at 70B+ parameters, where training dynamics may differ, is unknown.

3. **How does DroPE interact with instruction tuning and RLHF?** All experiments use base models. Whether the recalibration phase can be combined with alignment procedures is an open question.

4. **Can hybrid approaches (RoPE in some layers, NoPE in others) further improve results?** The paper notes that methods like RNoPE-SWA and SWAN-GPT, which occupy a middle ground between RoPE and NoPE, are complementary to DroPE. Whether selective PE retention improves over full removal is untested.

5. **What is the optimal recalibration budget as a function of model size and pretraining tokens?** The paper tests several budgets (0.5--20% of pretraining) but does not provide a scaling law.

6. **Can the softmax temperature scaling be eliminated?** The logarithmic temperature formula requires per-length calibration. Whether the model can learn to generalize without this inference-time adjustment is open.

---

## Core References and Why They Are Referenced

### Positional Embedding Foundations

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the dominant PE scheme in modern LLMs. DroPE specifically targets removing RoPE after pretraining.
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational transformer architecture; introduced positional embeddings and the self-attention mechanism that DroPE modifies.

### NoPE (No Positional Embedding) Transformers

- **Haviv et al. (2022)** -- *Transformer Language Models Without Positional Encodings Still Learn Positional Information.* Shows NoPE transformers can learn positional information implicitly via causal masking but underperform RoPE. Motivates the question of why PEs help training.
- **Kazemnejad et al. (2023)** -- *The Impact of Positional Encoding on Length Generalization in Transformers.* Proves NoPE's first attention layer can perfectly reconstruct positions, establishing NoPE has the same expressivity as RoPE. DroPE builds on this by showing the gap is in optimization, not expressivity.

### RoPE Context Extension Methods (Baselines)

- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation (PI).* Uniform frequency scaling baseline (gamma_m = 1/s); DroPE substantially outperforms it.
- **bloc97 (2023)** -- *NTK-Aware Scaled RoPE.* Non-uniform scaling that preserves high frequencies; used as a baseline throughout DroPE's evaluations.
- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Most popular RoPE-scaling method; DroPE's primary comparison target. DroPE shows YaRN's zero-shot behavior is equivalent to context cropping (Figure 5).
- **Ding et al. (2024)** -- *LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens.* Advanced RoPE extension; DroPE outperforms LongRoPE2 on NIAH tasks at 2x/4x/8x (Table 10).

### Models Used in Evaluation

- **Allal et al. (2024)** -- *SmolLM.* Provides the 360M and 1.7B parameter models for DroPE's "LMs in the wild" experiments, demonstrating post-hoc applicability.
- **Touvron et al. (2023)** -- *Llama 2.* Provides the 7B parameter model demonstrating DroPE's scalability to large pretrained models.

### Evaluation Benchmarks

- **Hsieh et al. (2024)** -- *RULER.* Provides the multi-query/key/value NIAH tasks used for zero-shot long-context evaluation.
- **Bai et al. (2023)** -- *LongBench.* Bilingual multitask long-context benchmark; four tasks (MultiFieldQA, MuSiQue, GovReport, LCC) used for downstream evaluation.
- **Kamradt (2023)** -- *Needle in a Haystack.* Original NIAH evaluation framework for pressure-testing LLM context utilization.

### Theoretical Analysis Support

- **Barbero et al. (2024)** -- *Round and Round We Go! What Makes Rotary Positional Encodings Useful?* Demonstrates that high RoPE frequencies are used by positional heads and low frequencies by semantic heads. Directly supports DroPE's analysis of why RoPE-scaling inevitably fails (Observation 2).
- **Nesterov (2013)** -- *Introductory Lectures on Convex Optimization.* Provides convexity and smoothness results used in the proof of the softmax Lipschitz bound (Lemma B.4) underlying Theorem 3.4.
- **Vershynin (2018)** -- *High-Dimensional Probability.* Used for bounding operator norms of random weight matrices at initialization in Theorem 3.4's proof.

### Alternative Architectures (Compared Against)

- **Press et al. (2021)** -- *ALiBi: Train Short, Test Long.* Alternative PE scheme using linear attention biases for length extrapolation. DroPE outperforms ALiBi on all NIAH tasks (Table 1).
- **Yang et al. (2025b)** -- *RoPE to NoPE and Back Again (RNoPE-SWA).* Hybrid attention strategy between RoPE and NoPE. DroPE outperforms it on NIAH (Table 1). Noted as complementary.
- **Puvvada et al. (2025)** -- *SWAN-GPT.* Scalable long-context modeling approach occupying a middle ground between RoPE and NoPE. Noted as complementary.

### Training Stability

- **Henry et al. (2020)** -- *Query-Key Normalization for Transformers.* QKNorm technique adopted by DroPE during extended recalibration to stabilize training at higher learning rates.
- **Wang et al. (2024)** -- *Length Generalization of Causal Transformers Without Position Encoding.* Source of the softmax temperature scaling technique applied at inference for longer sequences.

### Data and Training

- **Penedo et al. (2024)** -- *The FineWeb Datasets.* Training data for from-scratch experiments and recalibration of SmolLM models.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Provides compute-optimal scaling reference; DroPE experiments train well beyond chinchilla-optimal rates.
