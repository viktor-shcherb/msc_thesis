---
title: "Kimi Linear: An Expressive, Efficient Attention Architecture"
authors: "Kimi Team"
year: 2025
venue: "arXiv 2025"
paper_type: preprint
categories: ["architecture", "attention-efficiency", "long-context-evaluation"]
scope: ["hybrid linear attention", "efficient inference", "linear attention with delta rule", "MoE models"]
benchmarks_used: ["ruler", "mmlu-pro", "mmlu", "mrcr", "longbench-v2", "hellaswag", "arc", "winogrande", "bbh", "triviaqa", "gsm8k", "math-hendrycks", "humaneval", "evalplus", "c-eval", "cmmlu"]
models_introduced: ["kimi-linear-48b-a3b"]
models_evaluated: []
key_claims:
  - id: C1
    claim: "Kimi Linear outperforms full MLA attention across short-context, long-context, and RL scaling regimes with identical training recipe"
    evidence: "Tables 3-5, Figure 6"
    status: supported
    scope: "1.4T training tokens, 48B/3B MoE architecture"
    magnitude: "MMLU-Pro: 51.0 vs 47.2 MLA; RULER@128k: 84.3 vs 81.3 MLA"
  - id: C2
    claim: "Kimi Linear achieves up to 6× decoding throughput at 1M context while reducing KV cache by 75%"
    evidence: "Figure 1b, Figure 7b, Section 5.6"
    status: supported
    scope: "1M token context, batch size 1"
    magnitude: "6.3× TPOT speedup (1.84ms vs 11.48ms)"
  - id: C3
    claim: "Fine-grained (channel-wise) gating in KDA outperforms head-wise gating (GDN) on synthetic retrieval tasks"
    evidence: "Figure 4, Section 5.1"
    status: supported
    scope: "2-layer, 2-head model on Palindrome, MQAR, Stack tasks"
  - id: C4
    claim: "3:1 KDA-to-MLA hybrid ratio provides optimal quality-efficiency tradeoff"
    evidence: "Table 1, Section 5.2"
    status: supported
    scope: "16-head, 16-layer scaling law model"
  - id: C5
    claim: "NoPE for MLA layers combined with KDA provides better long-context performance than RoPE"
    evidence: "Table 5, Section 5.2"
    status: supported
    scope: "128k context benchmarks"
    magnitude: "RULER: 84.3 (NoPE) vs 78.8 (RoPE)"
  - id: C6
    claim: "Kimi Linear demonstrates ~1.16× computational efficiency over MLA in scaling law experiments"
    evidence: "Figure 5, Section 5.3"
    status: supported
    scope: "653M-1.7B activated parameter models"
  - id: C7
    claim: "KDA kernel achieves ~2× speedup over general DPLR formulation"
    evidence: "Figure 2, Section 3.2"
    status: supported
    scope: "2K-64K input lengths, batch size 1, 16 heads"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Kimi Linear extends standard Transformer attention with hybrid linear attention architecture to achieve subquadratic complexity"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Both address quadratic attention bottleneck; Longformer uses sparse local+global patterns, Kimi Linear uses linear attention with delta rule hybridized with full attention"
  - target: 2024-10-ruler-context-size
    type: uses-benchmark
    detail: "RULER is primary long-context benchmark; Kimi Linear achieves 84.3 at 128k (vs 81.3 MLA) and 94.8 at 1M context"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "YaRN extends context via RoPE interpolation; Kimi Linear delegates position encoding to KDA layers and uses NoPE for MLA, avoiding RoPE extrapolation issues"
  - target: 2024-01-roformer-rope
    type: complementary
    detail: "Paper interprets linear attention with gated delta rule as learnable multiplicative position encoding that relaxes RoPE's orthogonality constraint"
  - target: 2025-04-attention-sink-emerges
    type: complementary
    detail: "Cites gated attention mechanism as alleviating attention sink phenomenon (Section 4, citing Qiu et al. 2025)"
open_questions:
  - question: "How does Kimi Linear's performance scale beyond 48B total parameters?"
    addressed_by: null
  - question: "Can KDA replace full attention entirely with sufficient state expansion?"
    addressed_by: null
  - question: "Does NoPE + KDA generalize to other hybrid architectures beyond MLA?"
    addressed_by: null
---
# Kimi Linear: An Expressive, Efficient Attention Architecture

**Authors:** Kimi Team (Moonshot AI, with collaborators from Soochow University, HKUST Guangzhou, MIT, Hangzhou Institute of Medicine)
**Date:** October 2025, arXiv:2510.26692v2

---

## Core Research Problem

Standard softmax attention in Transformers has **quadratic time complexity** O(T²) and **linearly growing KV cache**, creating fundamental bottlenecks for long-context inference. These inefficiencies are especially problematic for agentic LLMs that must process extended trajectories, tool-use interactions, and reinforcement learning (RL) test-time scaling scenarios (Section 1).

**Linear attention** offers O(T) complexity by reformulating attention as kernelized feature interactions, but historically underperforms softmax attention due to limited expressivity. Recent advances using gating/decay mechanisms and the delta rule have narrowed this gap, but purely linear structures remain constrained by **finite-state RNN capacity**, making long-sequence modeling and in-context retrieval theoretically challenging.

**Hybrid architectures** combining softmax and linear attention offer a practical compromise, but previous hybrid models operated at limited scale or lacked comprehensive evaluation. The core challenge is: **how to develop an attention architecture that matches or surpasses full attention in quality while achieving substantial efficiency gains in both speed and memory—enabling the next generation of decoding-heavy, agentic LLMs.**

---

## Problem Solutions

Kimi Linear addresses this through three integrated innovations:

1. **Kimi Delta Attention (KDA)**: A linear attention module extending Gated DeltaNet with **fine-grained channel-wise gating** instead of coarse head-wise gating. Each feature dimension maintains an independent forgetting rate, enabling more precise regulation of finite-state RNN memory.

2. **Hardware-efficient chunkwise algorithm**: KDA uses a specialized variant of Diagonal-Plus-Low-Rank (DPLR) transition matrices that substantially reduces computation compared to general DPLR while remaining consistent with the classical delta rule.

3. **Hybrid architecture with NoPE**: Kimi Linear interleaves KDA with full MLA (Multi-Head Latent Attention) layers in a uniform **3:1 ratio**, delegating positional encoding entirely to KDA layers while using No Position Encoding (NoPE) for MLA layers.

---

## Approach Details

### Method

**Kimi Delta Attention (KDA)** extends the gated delta rule with fine-grained decay:

> **S**_t = (**I** - β_t **k**_t **k**_t^⊤) Diag(**α**_t) **S**_{t-1} + β_t **k**_t **v**_t^⊤ ∈ ℝ^{d_k × d_v}
>
> **o**_t = **S**_t^⊤ **q**_t ∈ ℝ^{d_v}

Where:
- **S**_t is the matrix-valued recurrent state (associative memory)
- **α**_t ∈ [0,1]^{d_k} is the **fine-grained channel-wise decay** (vs scalar α_t in GDN)
- β_t ∈ [0,1] is the learning rate for the delta rule update
- The term (**I** - β_t **k**_t **k**_t^⊤) implements Householder-style correction toward mapping **k**_t → **v**_t

This can be rewritten as DPLR: **S**_t = (Diag(**α**_t) - β_t **k**_t (**k**_t ⊙ **α**_t)^⊤) **S**_{t-1} + β_t **k**_t **v**_t^⊤

### Key Technical Components

**Neural Parameterization.** For each head h:

- **q**_t^h, **k**_t^h = L2Norm(Swish(ShortConv(**W**_{q/k}^h **x**_t))) ∈ ℝ^{d_k}
- **v**_t^h = Swish(ShortConv(**W**_v^h **x**_t)) ∈ ℝ^{d_v}
- **α**_t^h = f(**W**_↑^α **W**_↓^α **x**_t) ∈ [0,1]^{d_k} (low-rank projection)
- β_t^h = Sigmoid(**W**_β^h **x**_t) ∈ [0,1]

Key components: ShortConv for local token dependencies, L2Norm on q/k for eigenvalue stability, Sigmoid output gating (vs Swish), head-wise RMSNorm before output projection.

**Chunkwise Parallelization.** The recurrence is expanded into chunk-wise form using WY representation to pack rank-1 updates into compact matrices. Key efficiency gain: by binding both variables **a** and **b** to **k** in the DPLR formulation, KDA reduces secondary chunk computations from 4 to 2 and eliminates 3 matrix multiplications, achieving ~2× speedup over general DPLR (Figure 2).

**Hybrid Architecture.** Kimi Linear stacks blocks of 3 KDA layers followed by 1 MLA layer (3:1 ratio). MLA layers use **No Position Encoding (NoPE)**, delegating positional information entirely to KDA. This design:
- Enables conversion to efficient pure Multi-Query Attention during inference
- Simplifies long-context training (no RoPE frequency tuning needed)
- Provides balanced positional bias across layers for better long-range extrapolation

**KDA as Learnable Position Encoding.** The paper shows linear attention with gated delta rule can be expressed analogously to RoPE:

> o_t = Σ_{i=1}^t (**q**_t^⊤ (∏_{j=i+1}^t **A**_j (**I** - β_j **k**_j **k**_j^⊤)) **k**_j) **v**_j

This formulation interprets KDA as multiplicative positional encoding with **data-dependent, learnable** transition matrix, relaxing RoPE's orthogonality constraint and avoiding fixed-frequency extrapolation issues.

### Experimental Setup

**Model Configuration.** 48B total parameters, 3B activated parameters via MoE (8/256 experts activated + 1 shared expert). Architecture follows Moonlight with increased MoE sparsity (32).

**Training.**
- 4096-token context window during pretraining
- MuonClip optimizer, WSD learning rate schedule
- 1.4T tokens for fair comparison experiments, 5.7T tokens for final release
- Same annealing schedule and long-context activation as Kimi K2

**Post-training.**
- Multi-stage SFT: general instruction-following followed by reasoning-intensive data
- RLVR on mathematics/code/STEM with PTX loss to prevent capability degeneration
- Truncated importance sampling for stable RL with precision mismatch

**Evaluation Benchmarks.**
- General: HellaSwag, ARC-Challenge, Winogrande, MMLU, TriviaQA, MMLU-Redux, MMLU-Pro, GPQA-Diamond, BBH
- Code: LiveCodeBench v6, EvalPlus
- Math: AIME 2025, MATH 500, HMMT 2025, PolyMath-en
- Long-context: MRCR, RULER, Frames, HELMET-ICL, RepoQA, Long Code Arena, LongBench v2
- Chinese: C-Eval, CMMLU

### Key Results

**Pretraining (1.4T tokens, Table 3):**

| Category | Benchmark | MLA | GDN-H | Kimi Linear |
|----------|-----------|-----|-------|-------------|
| General | MMLU-Pro | 47.2 | 47.9 | **51.0** |
| General | BBH | 71.6 | 70.6 | **72.9** |
| General | TriviaQA | 68.9 | 70.1 | **71.7** |
| Math | GSM8K | 83.7 | 81.7 | **83.9** |
| Code | CRUXEval-O-cot | 61.5 | 58.1 | **62.0** |
| Chinese | CMMLU | 79.5 | 80.7 | **80.8** |

**Long-Context (128k, Table 5):**

| Benchmark | MLA | GDN-H | Kimi Linear (RoPE) | Kimi Linear |
|-----------|-----|-------|-------------------|-------------|
| RULER | 81.3 | 80.5 | 78.8 | **84.3** |
| MRCR | 22.6 | 23.9 | 22.0 | **29.6** |
| HELMET-ICL | 88.0 | 85.5 | 88.0 | **90.0** |
| RepoQA | 63.0 | 63.0 | 66.5 | **68.5** |
| Average | 52.2 | 51.2 | 51.8 | **54.5** |

**RL Scaling (Figure 6).** During math RL training, Kimi Linear shows faster accuracy growth and wider performance gap vs MLA on both training set and test sets (MATH500, AIME 2025).

**Efficiency (Figure 7):**

| Context Length | MLA TPOT | Kimi Linear TPOT | Speedup |
|----------------|----------|------------------|---------|
| 128K | 5.2ms | 3.1ms | 1.7× |
| 512K | 10.5ms | 4.6ms | 2.3× |
| 1M | 11.5ms | 1.8ms | 6.3× |

**Extended Training (5.7T tokens, Tables 8-9).** Kimi Linear@5.7T achieves:
- RULER@128k: 95.4, RULER@1M: 94.8
- AIME 2025 (Avg@64): 58.6
- LiveCodeBench v6 (Pass@1): 45.7

### Synthetic Task Results

On controlled synthetic tasks (2-layer, 2-head models), KDA consistently outperforms GDN and Mamba2:

| Task | KDA@2048 | GDN@2048 | Mamba2@2048 |
|------|----------|----------|-------------|
| Palindrome | ~100% | ~75% | ~0% |
| MQAR | ~100% | ~75% | ~0% |
| Stack | ~100% | ~100% | ~0% |

KDA converges significantly faster than GDN on Palindrome and MQAR tasks (Figure 4), confirming benefits of fine-grained decay for selective forgetting.

### Ablation Studies

**Hybrid Ratio (Table 1):**

| Ratio | Training PPL | Validation PPL |
|-------|--------------|----------------|
| 3:1 | **9.23** | **5.65** |
| 0:1 (pure MLA) | 9.45 | 5.77 |
| 1:1 | 9.29 | 5.66 |
| 7:1 | 9.23 | 5.70 |
| 15:1 | 9.34 | 5.82 |

**Output Gate:** Sigmoid output gate outperforms no gating (+0.02 val PPL) and Swish gating (+0.16 val PPL).

**Convolution Layer:** Removing ShortConv degrades validation PPL by 0.05.

---

## Limitations and Failure Modes

1. **Long-context retrieval bottleneck.** Pure linear attention still struggles with precise memory retrieval and exact copying, necessitating the hybrid approach with full attention layers.

2. **Limited model sizes evaluated.** All experiments use 48B/3B MoE architecture. Scaling behavior beyond this size is not demonstrated.

3. **RoPE variant underperforms on long context.** Kimi Linear (RoPE) achieves lower RULER scores (78.8) than the NoPE variant (84.3), suggesting the NoPE design is essential for the architecture's long-context performance.

4. **GDN-H performance decline in long context.** While GDN-H outperforms MLA in short-context pretraining, it falls behind MLA in long-context evaluations (Table 5: 51.2 vs 52.2 average), indicating fine-grained gating is critical for long-context tasks.

5. **Hardware-specific efficiency.** Efficiency gains depend on kernel implementations and may vary with different hardware configurations.

### Scope and Comparability

- **What was not tested:** Dense (non-MoE) architectures, model scales beyond 48B, comparison with sparse attention methods (NSA, MoBA)
- **Comparability notes:** All comparisons use identical training recipe (1.4T tokens, same data, same hyperparameters) ensuring fair comparison across attention variants

---

## Conclusions

### Contributions

1. **Kimi Delta Attention (KDA).** Introduced channel-wise gating for the gated delta rule, enabling more precise regulation of finite-state RNN memory compared to head-wise gating in GDN. Demonstrated ~2× kernel speedup over general DPLR through constrained formulation.

2. **Hybrid architecture with NoPE.** Established that interleaving KDA with NoPE full attention at 3:1 ratio provides optimal quality-efficiency tradeoff, achieving 75% KV cache reduction while surpassing full attention quality.

3. **Comprehensive empirical validation.** Demonstrated through 1.4T token training that Kimi Linear outperforms full MLA across short-context (MMLU-Pro: +3.8), long-context (RULER@128k: +3.0), and RL scaling regimes.

4. **Scaling law efficiency.** Showed ~1.16× computational efficiency over MLA in compute-optimal training conditions.

5. **Open-source release.** Released KDA kernels with vLLM integration and pre-trained checkpoints, enabling drop-in replacement for full attention architectures.

### Implications

1. **Linear attention with delta rule can serve as learnable position encoding.** The interpretation of KDA as data-dependent multiplicative position encoding that relaxes RoPE's orthogonality constraint suggests new directions for position-aware architectures (speculative).

2. **Hybrid architectures may be optimal for agentic LLMs.** The consistent advantages across short-context, long-context, and RL scenarios suggest hybrid linear-full attention is particularly suited for agentic inference workloads requiring long-horizon generation.

3. **Fine-grained gating is essential for linear attention quality.** The performance gap between KDA and GDN-H, especially on long-context tasks, indicates that per-channel decay control is a key factor in linear attention expressivity.

---

## Key Claims

**C1. Kimi Linear outperforms full MLA attention across all evaluated scenarios with identical training recipe.** Demonstrated on 1.4T token training: MMLU-Pro 51.0 vs 47.2 (+3.8), BBH 72.9 vs 71.6 (+1.3), RULER@128k 84.3 vs 81.3 (+3.0). Performance hierarchy: Kimi Linear > GDN-H > MLA on short-context; Kimi Linear > MLA > GDN-H on long-context. Status: **supported**.

**C2. Kimi Linear achieves up to 6× decoding throughput at 1M context.** TPOT at 1M tokens: 1.84ms (Kimi Linear) vs 11.48ms (MLA), enabling 6.3× speedup. KV cache reduction of 75% due to 3:1 linear-to-full ratio. Speedup increases with context length (1.7× at 128K, 2.3× at 512K). Status: **supported**.

**C3. Fine-grained (channel-wise) gating outperforms head-wise gating on synthetic retrieval tasks.** On Palindrome, MQAR, and Stack tasks, KDA achieves ~100% accuracy at 2048 tokens while GDN achieves ~75% (Palindrome, MQAR) and Mamba2 fails entirely. KDA converges significantly faster during training. Status: **supported**.

**C4. 3:1 KDA-to-MLA ratio is optimal among tested configurations.** Ablation over 0:1, 1:1, 3:1, 7:1, 15:1 ratios shows 3:1 achieves lowest training (9.23) and validation (5.65) perplexity. Higher ratios (7:1, 15:1) degrade validation performance; lower ratios increase inference overhead. Status: **supported**.

**C5. NoPE for MLA layers provides better long-context performance than RoPE.** RULER@128k: 84.3 (NoPE) vs 78.8 (RoPE). The paper hypothesizes NoPE avoids positional mismatch between linear attention's implicit bias and full attention's explicit RoPE bias. Status: **supported**.

**C6. Kimi Linear achieves ~1.16× computational efficiency in scaling law experiments.** Fitted curves: MLA: 2.3092 × C^{-0.0536}; Kimi Linear: 2.2879 × C^{-0.0527}. At equivalent loss, Kimi Linear requires ~1.16× less compute. Status: **supported**.

**C7. KDA kernel achieves ~2× speedup over general DPLR.** Execution time comparison at 64K tokens shows KDA at ~32ms vs DPLR at ~64ms. Improvement comes from reducing secondary chunk computations (4→2) and eliminating 3 matrix multiplications. Status: **supported**.

---

## Open Questions

1. **How does Kimi Linear scale beyond 48B total parameters?** All experiments use a single model size. Whether the performance advantages persist or amplify at larger scales remains untested. Unresolved.

2. **Can KDA replace full attention entirely with sufficient state expansion?** The paper notes state expansion techniques can mitigate linear attention's retrieval limitations but does not test this. Unresolved.

3. **Does NoPE + KDA generalize to other hybrid architectures?** Only tested with MLA as the full attention component. Applicability to other attention variants unknown. Unresolved.

4. **What explains GDN-H's long-context performance degradation relative to MLA?** Despite outperforming MLA on short-context pretraining, GDN-H underperforms on long-context benchmarks. The paper does not fully explain this reversal. Unresolved.

---

## Core References and Why They Are Referenced

### Linear Attention Foundations

- **Katharopoulos et al. (2020)** -- *Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention.* Foundation for linear attention formulation. Reformulates attention as kernelized features enabling O(T) complexity via associative matrix products.

- **Schlag et al. (2021)** -- *Linear Transformers Are Secretly Fast Weight Programmers.* Provides fast-weight perspective on linear attention. The state S is interpreted as associative memory storing transient key-value mappings. DeltaNet reinterprets recurrence as online gradient descent on reconstruction loss.

### Gated Linear Attention Methods

- **Yang et al. (2025) [111]** -- *Gated Delta Networks.* Direct predecessor. GDN introduces scalar forget gate α_t to delta rule, implementing weight decay on fast weights. KDA extends this with fine-grained channel-wise gating.

- **Yang et al. (2024) [114]** -- *Gated Linear Attention Transformers.* GLA introduces channel-wise gates with chunkwise parallelism. KDA adopts similar fine-grained decay philosophy while combining with delta rule.

- **Dao & Gu (2024) [16]** -- *Transformers are SSMs (Mamba2).* Establishes connection between Transformers and SSMs. Uses head-wise scalar decay. KDA's synthetic experiments show Mamba2 fails on copying/retrieval tasks where KDA and GDN succeed.

### State Space Models and DPLR

- **Gu et al. (2022) [30]** -- *Efficiently Modeling Long Sequences with Structured State Spaces (S4).* Introduces Diagonal-Plus-Low-Rank (DPLR) structure for state transitions. KDA uses constrained DPLR variant for efficiency.

- **Peng et al. (2025) [71]** -- *RWKV-7 "Goose".* DPLR-based architecture with expressive dynamic state evolution. Compared in Table 6 as related attention mechanism.

### Hybrid Architectures

- **Lieber et al. (2024) [57]** -- *Jamba.* Hybrid Transformer-Mamba architecture. Establishes inter-layer hybrid paradigm that Kimi Linear follows.

- **MiniMax et al. (2025) [66]** -- *MiniMax-01.* Scaling foundation models with Lightning Attention. Another hybrid approach combining linear and full attention.

### Positional Encoding

- **Su et al. (2024) [88]** -- *RoFormer: RoPE.* Standard positional encoding in modern LLMs. Paper interprets KDA as learnable alternative to RoPE that relaxes orthogonality constraint.

- **Kazemnejad et al. (2023) [49]** -- *The Impact of Positional Encoding on Length Generalization.* Shows no existing PE method generalizes well to longer sequences. Motivates KDA's learnable position encoding approach.

### Attention Efficiency

- **DeepSeek-AI (2025) [19]** -- *DeepSeek-V3 Technical Report.* Introduces MLA (Multi-Head Latent Attention). Kimi Linear hybridizes KDA with MLA for the full attention component.

- **Yuan et al. (2025) [119]** -- *Native Sparse Attention (NSA).* Hardware-aligned sparse attention. Discussed as alternative approach to attention efficiency that maintains full KV cache.

### Evaluation Benchmarks

- **Hsieh et al. (2024) [38]** -- *RULER.* Primary long-context benchmark used to demonstrate Kimi Linear's advantages (84.3 at 128k, 94.8 at 1M).

- **Bai et al. (2024) [6]** -- *LongBench v2.* Long-context benchmark testing deep understanding beyond retrieval.

### Training Infrastructure

- **Liu et al. (2025) [62]** -- *Moonlight: Muon is Scalable for LLM Training.* Backbone architecture and optimizer (MuonClip) adopted by Kimi Linear.

- **Team Kimi (2025) [50]** -- *Kimi K2.* Training corpus and post-training recipe source. Kimi Linear follows K2's annealing schedule and long-context activation.
