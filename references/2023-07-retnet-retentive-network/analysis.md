---
title: "Retentive Network: A Successor to Transformer for Large Language Models"
authors: "Sun, Dong, Huang, Ma, Xia, Xue, Wang, Wei"
year: 2023
venue: "arXiv 2023"
paper_type: preprint
categories: ["architecture", "attention-efficiency"]
scope: ["sequence modeling", "training-inference efficiency trade-off", "linear recurrence", "alternative to attention"]
benchmarks_used: ["perplexity-pile", "perplexity-pg22", "perplexity-govreport", "perplexity-qmsum", "perplexity-summscreen", "hellaswag", "boolq", "copa", "piqa", "winograd-schema", "winogrande", "storycloze"]
models_introduced: ["retnet-1.3b", "retnet-2.7b", "retnet-6.7b"]
models_evaluated: ["retnet-1.3b", "retnet-2.7b", "retnet-6.7b", "h3", "hyena", "linear-transformer"]
key_claims:
  - id: C1
    claim: "RetNet simultaneously achieves training parallelism, O(1) inference cost, linear long-sequence memory complexity, and competitive performance -- breaking the 'impossible triangle'"
    evidence: "Table 1, Figure 2, Sections 2-3"
    status: unvalidated
    scope: "1.3B-6.7B scale, 100B training tokens"
    magnitude: "qualitative"
  - id: C2
    claim: "RetNet achieves comparable perplexity to Transformer at 1.3B and outperforms Transformer at 2.7B and 6.7B scale"
    evidence: "Figure 5, Section 3.2"
    status: supported
    scope: "1.3B-6.7B, 100B tokens, Pile/C4/Stack training data, 2048 max length"
    magnitude: "~0.2 PPL improvement at 6.7B (estimated from Figure 5)"
  - id: C3
    claim: "RetNet 6.7B decodes 8.4x faster, saves 70% GPU memory, and achieves 15.6x lower latency than Transformer at 8K sequence length"
    evidence: "Figure 1, Figure 6, Section 3.4"
    status: supported
    scope: "6.7B model, A100-80GB GPU, 8K input length"
    magnitude: "8.4x throughput, 70% memory, 15.6x latency"
  - id: C4
    claim: "RetNet achieves higher training throughput and lower memory than both standard Transformer and Transformer+FlashAttention across 1.3B-13B scales"
    evidence: "Table 4, Section 3.3"
    status: supported
    scope: "8192 training length, 8x A100-80GB, vanilla PyTorch (no kernel fusion)"
    magnitude: "25-50% memory saving, 7x acceleration vs standard Transformer"
  - id: C5
    claim: "At 200M scale, RetNet outperforms RWKV, H3, Hyena, and Linear Transformer on both in-domain and out-of-domain perplexity"
    evidence: "Table 5, Section 3.5"
    status: supported
    scope: "200M parameters, 16 layers, 1024 hidden dim"
    magnitude: "3.9 PPL improvement over next-best H3 on in-domain (26.05 vs 29.97)"
  - id: C6
    claim: "The swish gate and GroupNorm are essential components of retention -- removing either degrades in-domain perplexity by 1.5-1.8 points"
    evidence: "Table 6, Section 3.6"
    status: supported
    scope: "200M model ablation"
    magnitude: "1.79 PPL for swish gate, 1.49 PPL for GroupNorm"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "RetNet proposes an alternative to multi-head attention with a retention mechanism that removes softmax and supports recurrent formulation"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Retention's parallel formulation derives from xPos, a decay-augmented variant of RoPE, connecting rotary position encodings to linear recurrence"
  - target: 2022-04-s4-structured-state-spaces
    type: complementary
    detail: "RetNet compares with S4/H3 as alternative sequence models; both achieve subquadratic complexity but via different mechanisms (retention vs structured state spaces)"
  - target: 2024-05-mamba-selective-state-spaces
    type: concurrent
    detail: "Mamba and RetNet are concurrent proposals for Transformer alternatives; both achieve O(1) inference through recurrent formulations but Mamba uses selective state spaces"
  - target: 2022-12-flashattention
    type: complementary
    detail: "RetNet compares training efficiency against FlashAttention-optimized Transformers, claiming competitive throughput without custom CUDA kernels"
open_questions:
  - question: "Can RetNet scale beyond 6.7B parameters and maintain its advantages over Transformers at 70B+ scale with trillions of training tokens?"
    addressed_by: null
  - question: "Does RetNet's fixed exponential decay inherently limit its ability to model truly long-range dependencies compared to softmax attention's dynamic weighting?"
    addressed_by: null
  - question: "Would making gamma learnable or input-dependent improve performance at the cost of complicating the recurrent formulation?"
    addressed_by: null
  - question: "How does RetNet perform with instruction tuning, RLHF, chain-of-thought prompting, and other techniques essential for practical LLM deployment?"
    addressed_by: null
  - question: "Can custom kernels (analogous to FlashAttention for Transformers) significantly improve RetNet's wall-clock performance beyond vanilla PyTorch?"
    addressed_by: null
---

# Retentive Network: A Successor to Transformer for Large Language Models

**Authors:** Yutao Sun, Li Dong, Shaohan Huang, Shuming Ma, Yuqing Xia, Jilong Xue, Jianyong Wang, Furu Wei (Microsoft Research, Tsinghua University)
**Date:** July 2023, arXiv:2307.08621v4

---

## Core Research Problem

Transformers have become the dominant architecture for large language models, but their O(N) per-step inference cost and memory-bound key-value cache make deployment expensive and latency-sensitive, especially as sequence lengths grow. Training parallelism of Transformers is a key advantage over recurrent models, but this comes at the cost of O(N^2) attention computation and growing KV cache memory during generation.

Prior attempts to resolve this tension have each sacrificed at least one desirable property. **Linear attention** (Katharopoulos et al., 2020) replaces softmax with kernel approximations to enable recurrent inference, but modeling capability and performance are worse than Transformers. **Recurrent neural networks** achieve O(1) inference but sacrifice training parallelism. **RWKV** (Peng et al., 2023) uses element-wise operators for acceleration but harms representation capacity. **S4/H3** (Gu et al., 2021; Dao et al., 2022) and **Hyena** (Poli et al., 2023) replace attention with state space models or long convolutions, but achieve O(N log N) rather than O(N) memory complexity and do not clearly outperform Transformers.

The authors frame this as the **"impossible triangle"** (Figure 2): **how to simultaneously achieve training parallelism, low-cost O(1) inference, and strong language modeling performance.**

---

## Problem Solutions

RetNet proposes a **retention mechanism** that theoretically unifies recurrence and attention through matrix diagonalization, yielding three mathematically equivalent computation paradigms:

1. **Parallel representation** -- similar to attention but with exponential decay instead of softmax, enabling GPU-efficient training.
2. **Recurrent representation** -- O(1) per-step inference via a fixed-size state, eliminating the KV cache entirely.
3. **Chunkwise recurrent representation** -- a hybrid that processes chunks in parallel while passing cross-chunk information recurrently, enabling linear-complexity long-sequence training.

The architecture replaces multi-head attention with **multi-scale retention (MSR)**, where each head uses a different exponential decay rate γ, combined with a swish gate and GroupNorm for stability.

---

## Approach Details

### Method

The retention mechanism begins from a recurrent formulation. Given input X ∈ R^{|x| × d_model}, project to a one-dimensional function v(n) = X_n · w_V, and define a recurrent state update:

> s_n = A s_{n-1} + K_n^T v_n,  A ∈ R^{d×d}, K_n ∈ R^{1×d}
>
> o_n = Q_n s_n = Σ_{m=1}^{n} Q_n A^{n-m} K_m^T v_m,  Q_n ∈ R^{1×d}

where Q_n, K_n are content-aware projections: Q = XW_Q, K = XW_K.

The key insight is **diagonalizing** the matrix A = Λ(γe^{iθ})Λ^{-1}, where γ, θ ∈ R^d. By absorbing Λ into W_Q and W_K, the recurrence yields:

> o_n = Σ_{m=1}^{n} γ^{n-m} (Q_n e^{inθ})(K_m e^{imθ})^† v_m

where Q_n(γe^{iθ})^n and K_m(γe^{iθ})^{-m} correspond to **xPos** (Sun et al., 2022), a relative position embedding for Transformers. The scalar decay γ simplifies this to:

> o_n = Σ_{m=1}^{n} γ^{n-m} (Q_n e^{inθ})(K_m e^{imθ})^† v_m    (Equation 4)

This formulation is parallelizable within training instances.

#### Parallel Representation

The parallel form (for training) defines the retention layer as:

> Q = (XW_Q) ⊙ Θ,  K = (XW_K) ⊙ Θ̄,  V = XW_V
>
> Θ_n = e^{inθ},  D_{nm} = γ^{n-m} if n ≥ m, else 0
>
> Retention(X) = (QK^T ⊙ D)V    (Equation 5)

where D ∈ R^{|x|×|x|} combines causal masking and exponential decay into a single matrix.

#### Recurrent Representation

For O(1) inference:

> S_n = γ S_{n-1} + K_n^T V_n
>
> Retention(X_n) = Q_n S_n    (Equation 6)

The state S_n has fixed size d_k × d_v, independent of sequence length.

#### Chunkwise Recurrent Representation

For long-sequence training with chunk size B:

> Retention(X_{[i]}) = (Q_{[i]} K_{[i]}^T ⊙ D) V_{[i]} + (Q_{[i]} R_{i-1}) ⊙ ξ    (Equation 7)
>
> R_i = K_{[i]}^T (V_{[i]} ⊙ ζ) + γ^B R_{i-1}

where the first term is the inner-chunk parallel computation and the second term is the cross-chunk recurrent information.

### Key Technical Components

**Multi-Scale Retention (MSR).** Each layer uses h = d_model / d retention heads with different per-head decay rates:

> γ = 1 - 2^{-5-arange(0,h)} ∈ R^h    (Equation 8)

Different γ values create **multi-scale** modeling: heads with γ close to 1 attend to long-range context, while heads with smaller γ focus on local patterns. The MSR layer is:

> head_i = Retention(X, γ_i)
>
> Y = GroupNorm_h(Concat(head_1, ..., head_h))
>
> MSR(X) = (swish(XW_G) ⊙ Y) W_O

where W_G, W_O ∈ R^{d_model × d_model}. The **swish gate** (Ramachandran et al., 2017) enhances non-linearity. **GroupNorm** (Wu & He, 2018) normalizes each head separately (rather than LayerNorm across all heads), because different γ scales produce different variance statistics.

**Retention Score Normalization.** Three normalization factors stabilize numerics without affecting final results (due to GroupNorm's scale invariance): (1) normalize QK^T as QK^T/√d; (2) replace D with D̃_{nm} = D_{nm}/√(Σ_{i=1}^{n} D_{ni}); (3) normalize retention scores R̃_{nm} = R_{nm} / max(|Σ_{i=1}^{n} R_{ni}|, 1).

**Overall Architecture.** L identical blocks with pre-LayerNorm and residual connections:

> Y^l = MSR(LN(X^l)) + X^l
>
> X^{l+1} = FFN(LN(Y^l)) + Y^l    (Equation 9)

where FFN(X) = gelu(XW_1)W_2. Parameters are initialized following DeepNet (Wang et al., 2022) for training stability.

**Parameter Allocation.** To match Transformer parameter counts: retention has 8d^2 parameters (W_Q, W_K ∈ R^{d×d}, W_V, W_G, W_O ∈ R^{d×2d} with head dimension of V being twice Q/K), and FFN intermediate dimension is 2d. Head dimension is set to 256 for Q/K and 512 for V. In experiments, γ = 1 - e^{linspace(log 1/32, log 1/512, h)} instead of the default formula.

### Experimental Setup

**Model Sizes:**

| Size | Hidden Dim. | #Layers | Batch Size | # Tokens | Learning Rate |
|---|---|---|---|---|---|
| 1.3B | 2048 | 24 | 4M | 100B | 6 × 10^{-4} |
| 2.7B | 2560 | 32 | 4M | 100B | 3 × 10^{-4} |
| 6.7B | 4096 | 32 | 4M | 100B | 3 × 10^{-4} |

**Training Data:** The Pile (Gao et al., 2020), C4 (Dodge et al., 2021), and The Stack (Kocetkov et al., 2022).

**Training Details:** 2048 max sequence length, 25K training steps, AdamW optimizer (β₁=0.9, β₂=0.98), weight decay 0.05 (Section 3.1 text; Table 7 in Appendix A reports 0.01), 375 warmup steps. LR scheduler described as "linear learning rate decay" in Section 3.1 but "Polynomial decay" in Table 7 (Appendix A). Gradient clipping at 2.0, dropout 0.1. DeepNet initialization. Implementation based on TorchScale (Ma et al., 2022). Trained on **512 AMD MI200 GPUs**.

**200M Comparison Setup:** 16 layers, 1024 hidden dimension, head dimension 8 (for H3) or matching, batch size 0.5M tokens, 10K steps. Compared architectures: Linear Transformer, RWKV, H3, Hyena, RetNet.

**Evaluation:** Language modeling perplexity on validation set (in-domain) and out-of-domain corpora (PG22, QMSum, GovReport, SummScreen). Zero-shot and 4-shot downstream tasks (HellaSwag, BoolQ, COPA, PIQA, Winograd, Winogrande, StoryCloze) with 6.7B models. Training cost (memory, throughput) with 8× A100-80GB GPUs. Inference cost (memory, throughput, latency) with A100-80GB.

**Reproducibility:** Code released via Microsoft/unilm (TorchScale). Training data is publicly available. Hyperparameters are fully specified in Table 2 and Appendix A. No variance estimates or multiple seeds reported.

### Key Results

#### Language Modeling (Scaling)

RetNet achieves comparable perplexity to Transformer, with RetNet outperforming at ≥2B (Figure 5):

| Model Size | RetNet PPL | Transformer PPL |
|---|---|---|
| 1.3B | ~14.8 | ~14.5 |
| 2.7B | ~13.2 | ~13.4 |
| 6.7B | ~12.8 | ~13.0 |

(Values estimated from Figure 5; exact numbers not provided in text. The paper states RetNet "tends to outperform Transformer when the model size is larger than 2B.")

#### Context Length Perplexity (Appendix B, Table 8)

| Model | 512 | 1024 | 2048 |
|---|---|---|---|
| Transformer | 13.55 | 12.56 | 12.35 |
| RetNet | 13.09 | 12.14 | 11.98 |

RetNet consistently outperforms Transformer across context lengths, with increasing advantage at longer contexts.

#### Zero-Shot and Few-Shot (6.7B, Table 3)

| Setting | HS | BoolQ | COPA | PIQA | Winograd | Winogrande | SC | Avg |
|---|---|---|---|---|---|---|---|---|
| *Zero-Shot* | | | | | | | | |
| Transformer | 55.9 | 62.0 | 69.0 | 74.6 | 69.5 | 56.5 | 75.0 | 66.07 |
| RetNet | **60.7** | **62.2** | **77.0** | **75.4** | **77.2** | **58.1** | **76.0** | **69.51** |
| *4-Shot* | | | | | | | | |
| Transformer | 55.8 | 58.7 | 71.0 | 75.0 | 71.9 | 57.3 | 75.4 | 66.44 |
| RetNet | **60.5** | **60.1** | **78.0** | **76.0** | **77.9** | **59.9** | **75.9** | **69.76** |

RetNet outperforms Transformer on 6/7 zero-shot tasks and 6/7 4-shot tasks, with a **3.4 point average improvement** in both settings.

#### Training Cost (8192 Sequence Length, Table 4)

| Model Size | Memory: Trm (GB) | Memory: Trm+FlashAttn (GB) | Memory: RetNet (GB) | Throughput: Trm (wps) | Throughput: Trm+FlashAttn (wps) | Throughput: RetNet (wps) |
|---|---|---|---|---|---|---|
| 1.3B | 74.8 | 38.8 | 34.5 | 10832.4 | 63965.2 | 73344.8 |
| 2.7B | 69.6 | 42.1 | 42.0 | 5186.0 | 34990.2 | 38921.2 |
| 6.7B | 69.0 | 51.4 | 48.0 | 2754.4 | 16230.1 | 17458.6 |
| 13B | 61.4 | 46.3 | 45.9 | 1208.9 | 7945.1 | 8642.2 |

RetNet achieves lower memory and higher throughput than both vanilla Transformer and Transformer+FlashAttention at all scales. RetNet uses vanilla PyTorch without kernel fusion, suggesting further optimization potential.

#### Inference Cost (6.7B, Figure 6)

At 8K sequence length:
- **Memory:** RetNet ~15 GB (constant), Transformer ~43 GB (grows linearly with length). RetNet saves **~70%** memory.
- **Throughput:** RetNet ~300 wps (length-invariant), Transformer ~35 wps at 8K. RetNet is **8.4x faster**.
- **Latency:** RetNet ~20 ms (batch-size-invariant), Transformer ~310 ms at batch size 8. RetNet is **15.6x lower latency**.

RetNet's inference cost is constant with respect to both sequence length and batch size, because the recurrent state has fixed size.

#### Comparison with Efficient Architectures (200M, Table 5)

| Method | In-Domain | PG22 | QMSum | GovReport | SummScreen |
|---|---|---|---|---|---|
| RWKV | 30.92 | 51.41 | 28.17 | 19.80 | 25.78 |
| H3 | 29.97 | 49.17 | 24.29 | 19.19 | 25.11 |
| Hyena | 32.08 | 52.75 | 28.18 | 20.55 | 26.51 |
| Linear Transformer | 40.24 | 63.86 | 28.45 | 25.33 | 32.02 |
| **RetNet** | **26.05** | **45.27** | **21.33** | **16.52** | **22.48** |

RetNet outperforms all compared architectures on every corpus, with 3.9 points better in-domain perplexity than the next best (H3: 29.97).

#### Ablation Study (200M, Table 6)

| Method | In-Domain | PG22 | QMSum | GovReport | SummScreen |
|---|---|---|---|---|---|
| RetNet | **26.05** | **45.27** | **21.33** | **16.52** | **22.48** |
| − swish gate | 27.84 | 49.44 | 22.52 | 17.45 | 23.72 |
| − GroupNorm | 27.54 | 46.95 | 22.61 | 17.59 | 23.73 |
| − γ decay | 27.86 | 47.85 | 21.99 | 17.49 | 23.70 |
| − multi-scale decay | 27.02 | 47.18 | 22.08 | 17.17 | 23.38 |
| Reduce head dimension | 27.68 | 47.72 | 23.09 | 17.46 | 23.41 |

- **Swish gate** is the most impactful component (+1.79 in-domain PPL when removed).
- **γ decay** is essential (+1.81 in-domain PPL when removed, equivalent to γ=1 which removes recurrence).
- **GroupNorm** improves over LayerNorm (+1.49) due to different variance statistics across multi-scale heads.
- **Multi-scale decay** (different γ per head) helps versus single γ for all heads (+0.97).
- **Larger head dimension** (256 vs 64) improves performance (+1.63) by increasing recurrent state memory capacity.

---

## Limitations and Failure Modes

1. **Limited scale.** All experiments use models up to 6.7B parameters trained on only 100B tokens. Modern LLMs train on trillions of tokens at scales of 70B+. It is unknown whether RetNet's advantages persist at larger scales.

2. **Short training context.** Maximum training length is 2048 tokens. The paper evaluates inference up to 8K but does not train or evaluate on sequences longer than 2048, leaving long-context modeling capability unvalidated.

3. **[Inferred] No long-context task evaluation.** The paper evaluates only perplexity and short-context downstream tasks. No evaluation on retrieval, multi-hop QA, summarization of long documents, or other tasks that specifically require long-range reasoning.

4. **[Inferred] No variance estimates.** Single runs only; no error bars, confidence intervals, or multi-seed experiments.

5. **Vanilla PyTorch implementation.** RetNet's training cost comparison uses vanilla PyTorch while FlashAttention uses highly optimized CUDA kernels. The comparison favors RetNet in "ease of implementation" but does not reflect the best achievable performance for either architecture. The authors acknowledge this, noting kernel fusion is "left for future work" (Section 3.3).

6. **[Inferred] Fixed exponential decay.** The decay rates γ are fixed hyperparameters, not learned or input-dependent. This may limit the model's ability to adapt its effective context window to different tasks or inputs, in contrast to attention which can dynamically attend to arbitrary positions.

7. **[Inferred] Rejected at major venues.** The paper was rejected at both ICLR 2024 and NeurIPS 2024, suggesting the research community had significant concerns about the claims or methodology.

### Scope and Comparability

- **What was not tested:** Models larger than 6.7B; training beyond 100B tokens; long-context evaluation benchmarks (RULER, LongBench, Needle-in-a-Haystack, etc.); comparison with Mamba or other SSMs published around the same time; instruction tuning or RLHF performance.
- **Comparability notes:** The 200M comparison (Table 5) uses only 10K training steps with 0.5M token batches, a much smaller scale than the main experiments. Training cost comparisons (Table 4) use 8× A100-80GB, different from the 512× AMD MI200 setup used for main experiments. RetNet uses GELU activation in FFN while some baselines may differ.

---

## Conclusions

### Contributions

1. **Retention mechanism with three equivalent representations.** Derived the theoretical connection between recurrence and attention through matrix diagonalization, yielding parallel (training), recurrent (O(1) inference), and chunkwise recurrent (long-sequence training) formulations that are mathematically equivalent.

2. **Multi-scale retention architecture.** Introduced per-head exponential decay rates, swish gating, and GroupNorm as key design choices that enable competitive language modeling performance. Ablations confirm each component's contribution.

3. **Favorable inference cost profile.** Demonstrated that RetNet's recurrent inference achieves constant memory, throughput, and latency regardless of sequence length and batch size, in stark contrast to Transformer's growing KV cache costs.

4. **Competitive scaling results.** Showed that RetNet matches or exceeds Transformer perplexity at 1.3B-6.7B scale and outperforms alternative efficient architectures (RWKV, H3, Hyena, Linear Transformer) at 200M scale.

### Implications

1. **The "impossible triangle" may not be impossible.** RetNet's design suggests that training parallelism, efficient inference, and strong performance can coexist, though validation at larger scales is needed. *Speculative: whether this holds at 70B+ scale with trillions of tokens remains an open question.*

2. **xPos/RoPE as a bridge to linear recurrence.** The theoretical derivation connecting xPos (a RoPE variant) to the retention recurrence suggests that position encoding research and efficient architecture research are more closely linked than previously recognized.

3. **Fixed decay as a viable alternative to attention.** The success of fixed exponential decay rates (rather than learned or data-dependent weighting as in softmax attention) suggests that the dynamic, input-dependent weighting of attention may not be strictly necessary for competitive language modeling. *Speculative: this remains contested, as attention's dynamic weighting is often considered essential for tasks requiring precise retrieval.*

---

## Key Claims

1. **C1: "Impossible triangle" broken** (Table 1, Figure 2). RetNet achieves training parallelism, O(1) inference cost, O(N) memory complexity, and competitive performance simultaneously. **Status: unvalidated** -- the claim rests on experiments at limited scale (≤6.7B, 100B tokens). The "performance" criterion is demonstrated only via perplexity and simple downstream tasks, not on the breadth of capabilities expected of modern LLMs.

2. **C2: Favorable scaling** (Figure 5, Section 3.2). RetNet matches Transformer perplexity at 1.3B and outperforms at 2.7B and 6.7B scale (improvement of ~0.2 PPL at 6.7B, estimated from Figure 5). **Status: supported** within the tested regime. Note: only three data points on the scaling curve; no variance estimates; extrapolation to larger scales is uncertain.

3. **C3: Massive inference efficiency gains** (Figure 1, Figure 6, Section 3.4). At 6.7B/8K: 8.4x throughput, 70% memory savings, 15.6x latency reduction vs Transformer. **Status: supported** -- these follow directly from the O(1) recurrent formulation. The advantage grows with sequence length as Transformer costs scale linearly.

4. **C4: Competitive training efficiency** (Table 4, Section 3.3). RetNet uses less memory and achieves higher throughput than Transformer+FlashAttention at 1.3B-13B scale. **Status: supported** -- though RetNet uses vanilla PyTorch while FlashAttention uses optimized CUDA kernels, making the comparison somewhat asymmetric. FlashAttention-2 (released concurrently) may narrow or reverse this gap.

5. **C5: Superior to efficient alternatives** (Table 5, Section 3.5). At 200M scale, RetNet outperforms RWKV, H3, Hyena, and Linear Transformer on all evaluated corpora. **Status: supported** at the tested scale. Note: single scale (200M), limited training (10K steps), and evolving baselines (RWKV and Mamba have since improved significantly).

6. **C6: Architectural components are essential** (Table 6, Section 3.6). Swish gate (+1.79 PPL), GroupNorm (+1.49 PPL), γ decay (+1.81 PPL), multi-scale decay (+0.97 PPL), and larger head dimension (+1.63 PPL) all contribute meaningfully. **Status: supported** -- clean ablation at 200M scale.

---

## Open Questions

1. **Scaling beyond 6.7B.** Does RetNet maintain competitive performance and efficiency advantages at 70B+ scale with trillions of training tokens? The scaling curve (Figure 5) has only three points, making extrapolation uncertain. *Not yet addressed.*

2. **Long-range dependency modeling.** Does the fixed exponential decay inherently limit RetNet's ability to model truly long-range dependencies (e.g., retrieval over 100K+ tokens), compared to attention's ability to assign arbitrary weights? *Not yet addressed.*

3. **Learned vs fixed decay.** Would making γ learnable or input-dependent improve performance at the cost of complicating the recurrent formulation? *Not yet addressed.*

4. **Interaction with modern techniques.** How does RetNet perform with instruction tuning, RLHF, chain-of-thought prompting, and other techniques that have proven essential for practical LLM deployment? *Not yet addressed.*

5. **Hardware-specific optimization.** The paper uses vanilla PyTorch. Can custom kernels (analogous to FlashAttention for Transformers) significantly improve RetNet's wall-clock performance? *Not yet addressed.*

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The Transformer architecture that RetNet aims to succeed, providing the baseline for all comparisons.
- **Ba et al. (2016)** -- *Layer Normalization.* Used in RetNet's overall architecture (pre-LayerNorm residual blocks).
- **Wu & He (2018)** -- *Group Normalization.* RetNet uses GroupNorm instead of LayerNorm within retention heads to handle different variance scales from multi-scale decay.
- **Ramachandran et al. (2017)** -- *Swish activation.* Used in RetNet's gating mechanism for non-linearity.

### Position Encoding and Retention Derivation

- **Sun et al. (2022)** -- *A Length-Extrapolatable Transformer (xPos).* RetNet's retention formulation derives from xPos, connecting rotary position embeddings to the parallel form of retention.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE is the basis for xPos, from which retention's position encoding is derived.

### Alternative Efficient Architectures (Compared)

- **Katharopoulos et al. (2020)** -- *Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention.* Linear attention as a baseline; achieves O(1) inference but with degraded performance.
- **Peng et al. (2023)** -- *RWKV: Reinventing RNNs for the Transformer Era.* Recurrent alternative compared at 200M scale; uses element-wise operators.
- **Gu et al. (2021)** -- *Efficiently Modeling Long Sequences with Structured State Spaces (S4).* State space model baseline.
- **Dao et al. (2022)** -- *Hungry Hungry Hippos (H3): Towards Language Modeling with State Space Models.* H3 compared at 200M scale.
- **Poli et al. (2023)** -- *Hyena Hierarchy: Towards Larger Convolutional Language Models.* Long convolution model compared at 200M scale.

### Training Infrastructure

- **Wang et al. (2022)** -- *DeepNet: Scaling Transformers to 1,000 Layers.* Initialization strategy used for training stability.
- **Ma et al. (2022)** -- *TorchScale: Transformers at Scale.* Implementation framework.
- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Training cost comparison baseline.
- **Shoeybi et al. (2019)** -- *Megatron-LM.* SubLN normalization approach referenced for retention's per-head normalization.

### Training Data

- **Gao et al. (2020)** -- *The Pile.* Primary training corpus.
- **Dodge et al. (2021)** -- *C4 corpus.* Training data component.
- **Kocetkov et al. (2022)** -- *The Stack.* Code training data component.

### Evaluation Benchmarks

- **Zellers et al. (2019)** -- *HellaSwag.* Zero-shot and few-shot evaluation benchmark.
- **Clark et al. (2019)** -- *BoolQ.* Yes/no QA evaluation.
- **Bisk et al. (2020)** -- *PIQA.* Physical intuition QA.
- **Wang et al. (2019)** -- *SuperGLUE (COPA).* Causal reasoning evaluation.
- **Mostafazadeh et al. (2017)** -- *StoryCloze.* Narrative understanding evaluation.
