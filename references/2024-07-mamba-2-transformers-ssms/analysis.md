---
title: "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality"
authors: "Dao, Gu"
year: 2024
venue: "ICML 2024"
paper_type: conference-paper
categories: ["state-space-models", "architecture", "attention-efficiency", "scaling-laws"]
scope: ["SSM-attention duality theory", "hardware-efficient SSM algorithms", "language modeling up to 2.7B parameters"]
benchmarks_used: ["mqar", "perplexity-pile", "lambada", "hellaswag", "piqa", "arc", "winogrande", "openbookqa"]
models_introduced: ["mamba-2-130m", "mamba-2-370m", "mamba-2-780m", "mamba-2-1.3b", "mamba-2-2.7b"]
models_evaluated: ["mamba-130m", "mamba-370m", "mamba-790m", "mamba-1.4b", "mamba-2.8b", "pythia-series", "mamba-2-130m", "mamba-2-370m", "mamba-2-780m", "mamba-2-1.3b", "mamba-2-2.7b"]
key_claims:
  - id: C1
    claim: "State space models are equivalent to semiseparable matrices: the SSM transformation y = SSM(A,B,C)(x) is identical to multiplication by an N-semiseparable matrix in SSS representation."
    evidence: "Theorem 3.5, Section 3"
    status: supported
    scope: "all structured SSMs with state size N"
    magnitude: "qualitative -- exact equivalence, not an approximation"
  - id: C2
    claim: "Any SSM of state size N on sequence length T can be computed in O(TN) time, matching the lower bound given by the size of B and C."
    evidence: "Theorem 3.7, Section 3.4"
    status: supported
    scope: "general SSMs including unstructured A matrices, with preprocessing"
    magnitude: "O(TN) time complexity, tight with representation size"
  - id: C3
    claim: "Efficient autoregressive attention with bounded-order recurrence must use a semiseparable mask matrix, meaning it must be an SSM."
    evidence: "Theorem 5.2, Appendix C.2 (Theorem C.3)"
    status: supported
    scope: "autoregressive transformations with bounded order k"
    magnitude: "qualitative -- a structural necessity result"
  - id: C4
    claim: "The SSD algorithm is 2-8x faster than Mamba's optimized selective scan implementation while allowing much larger state sizes."
    evidence: "Figure 10, Section 9.3"
    status: supported
    scope: "state expansion N=64, sequence lengths 512-512K, A100 80GB GPU"
    magnitude: "2-8x speedup; SSD time nearly independent of state dimension vs. linear scaling for Mamba scan"
  - id: C5
    claim: "Mamba-2 Pareto-dominates Mamba and Transformer++ in both perplexity and wall-clock time on Chinchilla scaling laws."
    evidence: "Figure 9, Section 9.2.1"
    status: supported
    scope: "125M-1.3B parameters, trained on the Pile with Chinchilla token counts"
    magnitude: "consistent perplexity improvement over Mamba and Transformer++ at matched FLOPs"
  - id: C6
    claim: "Mamba-2-2.7B trained on 300B tokens matches or outperforms Mamba-2.8B and Pythia-2.8B, and outperforms Pythia-6.9B on average zero-shot accuracy."
    evidence: "Table 1 (Table 10), Section 9.2.2"
    status: supported
    scope: "2.7B scale, 300B tokens on the Pile, GPT-NeoX tokenizer, 7 zero-shot tasks"
    magnitude: "60.2 avg accuracy vs. 59.9 (Mamba-2.8B), 55.7 (Pythia-2.8B), 58.3 (Pythia-6.9B)"
  - id: C7
    claim: "Mamba-2 significantly outperforms Mamba-1 on multi-query associative recall (MQAR), and increasing state size N from 16 to 256 consistently improves performance."
    evidence: "Figure 8, Section 9.1"
    status: supported
    scope: "MQAR with sequence lengths 256-1024, model dimensions 32-256, 2 layers"
    magnitude: "Mamba-2 N=256 matches or exceeds attention accuracy in all settings; Mamba-1 N=16 often below 0.50"
  - id: C8
    claim: "A hybrid of 58 SSD layers + 6 attention layers (roughly 10% attention) outperforms both pure Mamba-2 and pure Transformer++ at the 2.7B scale."
    evidence: "Table 3, Section 9.2.3"
    status: supported
    scope: "2.7B parameters, 64 layers, 300B tokens on the Pile"
    magnitude: "5.95 Pile ppl and 61.0 avg accuracy vs. 6.09/60.2 (Mamba-2) and 6.13/60.2 (Transformer++)"
  - id: C9
    claim: "The multi-value attention (MVA) / multi-input SSM (MIS) head pattern, as used in Mamba-1, outperforms multi-query, multi-key, and multi-head patterns when controlling for total state size."
    evidence: "Table 5, Section 9.4.2"
    status: supported
    scope: "125M and 360M models, state expansion N=64, head size P=64, Chinchilla token counts"
    magnitude: "11.66 ppl (MVA) vs. 12.62 (MQA), 12.59 (MKA), 12.06 (MHA) at 125M; 8.73 vs. 9.33, 9.36, 9.01 at 360M"
  - id: C10
    claim: "Kernel approximation methods from linear attention literature do not improve over simple pointwise nonlinear activations when combined with SSD's 1-semiseparable mask."
    evidence: "Tables 6-7, Section 9.4.3"
    status: supported
    scope: "125M-380M models, various kernel feature maps including cosFormer, RFA, Performer, Based, ReBased"
    magnitude: "best perplexity from RFA (11.57) or LayerNorm (11.50) vs. Swish default (11.66/11.67); Performer worst at 12.21"
cross_references:
  - target: 2024-05-mamba-selective-state-spaces
    type: extends
    detail: "Mamba-2 refines Mamba's selective SSM by restricting A to scalar-identity structure, enabling 2-8x faster training via the SSD algorithm while maintaining competitive language modeling."
  - target: 2022-04-s4-structured-state-spaces
    type: extends
    detail: "SSD generalizes the S4 framework by providing the semiseparable matrix equivalence for all SSMs and enabling selective (time-varying) models with hardware-efficient algorithms."
  - target: 2022-12-flashattention
    type: complementary
    detail: "FlashAttention-2 is the main attention speed baseline; SSD crosses over in efficiency at sequence length 2K and is 6x faster at 16K."
  - target: 2024-05-flashattention-2
    type: complementary
    detail: "SSD benchmarked against FlashAttention-2 for speed comparison; SSD is faster for sequence lengths above 2K."
  - target: 2023-07-retnet-retentive-network
    type: extends
    detail: "RetNet's decay mask is a special case of SSD's structured masked attention framework where A_t is time-invariant."
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV-4 is an RNN baseline in downstream evaluations; RWKV-5/6 later adopted selectivity and state expansion ideas shared with Mamba-2."
  - target: 2022-12-chinchilla-scaling-laws
    type: uses-benchmark
    detail: "Chinchilla scaling protocol used to set token-to-model-size ratios for scaling law experiments."
  - target: 2023-12-gqa-grouped-query-attention
    type: complementary
    detail: "GQA's grouped head patterns inspire the grouped-input SSM (GIS) / grouped-value attention (GVA) head structure in Mamba-2."
  - target: 2020-12-gpt-3-few-shot-learners
    type: uses-benchmark
    detail: "GPT-3 model specifications and training recipe used as the baseline configuration for scaling experiments."
open_questions:
  - question: "Can the SSD structured matrix algorithms be refined to handle general diagonal A (not just scalar-identity) with the same hardware efficiency?"
    addressed_by: null
  - question: "Which specific aspect of the Mamba-2 architecture is responsible for its dramatic improvement over Mamba-1 on MQAR, even at the same state size N=16?"
    addressed_by: null
  - question: "Do attention sinks (Darcet et al. 2024, Xiao et al. 2024) exist in Mamba models, and can interpretability techniques developed for Transformers be transferred to SSMs?"
    addressed_by: null
  - question: "Can the SSD framework be used to design principled non-causal variants of Mamba for bidirectional tasks?"
    addressed_by: null
  - question: "What are the theoretical limits of SSM-based models on copying and in-context learning tasks compared to full softmax attention?"
    addressed_by: null
  - question: "Can other forms of structured masks (e.g., Toeplitz, Fourier) in the SMA framework yield models with different useful properties beyond SSD?"
    addressed_by: null
---

# Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality

**Authors:** Tri Dao (Princeton University), Albert Gu (Carnegie Mellon University)
**Date:** May 2024, arXiv:2405.21060; published at ICML 2024

---

## Core Research Problem

While Transformers dominate language modeling, their core attention mechanism scales **quadratically** in sequence length during training and requires a **KV cache linear in sequence length** during inference. Structured state space models (SSMs) like Mamba offer linear-time training and constant-size state during generation, matching or beating Transformers at small to medium scale. However, the development of SSMs has appeared **disjoint from the Transformer ecosystem**: SSMs are harder to understand, experiment with, and train efficiently. In particular, Mamba's selective scan does not leverage **matrix multiplication units** on modern accelerators (GPUs/TPUs), leaving substantial hardware efficiency on the table (Section 1, p. 1).

Prior work on linear attention (Katharopoulos et al. (2020) -- *Transformers are RNNs*) established a connection between attention and linear RNNs, but this connection was limited to LTI (non-selective) models and a simple causal mask. The challenge is **how to develop a rich theoretical framework connecting selective SSMs and attention variants, and use it to design SSM architectures that are as hardware-efficient as Transformers while maintaining linear-time scaling** (Section 1, p. 1-2).

---

## Problem Solutions

The paper proposes **structured state space duality (SSD)**, a framework showing that SSMs and variants of attention are closely related through the abstraction of **structured matrices** -- specifically semiseparable matrices. The key components:

1. **SSMs are semiseparable matrices** (Section 3): The matrix transformation form of any SSM is an N-semiseparable matrix in sequentially semiseparable (SSS) representation. Different SSM computation methods correspond to different structured matrix multiplication algorithms.

2. **Structured masked attention (SMA)** generalizes linear attention (Section 4): By viewing masked attention as a 4-way tensor contraction, the quadratic and linear modes are simply two contraction orderings. Any structured matrix can serve as the mask, not just the causal 1s matrix.

3. **State space duality** (Section 5): Scalar-identity SSMs and 1-semiseparable SMA are duals of each other -- they share the same linear and quadratic forms. Furthermore, any attention variant with efficient bounded-order autoregression must be an SSM (Theorem 5.2).

4. **Hardware-efficient SSD algorithm** (Section 6): A block decomposition of the semiseparable matrix combines the linear recurrence for inter-chunk computation with the quadratic dual form for intra-chunk computation, achieving O(TN^2) FLOPs dominated by matrix multiplications.

5. **Mamba-2 architecture** (Section 7): Parallel projections, extra normalization, multi-value attention (MVA) head structure, and tensor-parallelism-friendly design yield a practical architecture 2-8x faster than Mamba.

---

## Approach Details

### Method

The SSD framework proceeds through three theoretical stages that converge on a unified model.

**Stage 1: SSMs as Semiseparable Matrices.** Starting from the selective SSM recurrence:

> h_t = A_t h_{t-1} + B_t x_t
> y_t = C_t^T h_t

The matrix transformation form is derived by unrolling the recurrence (Section 3.1):

> y = Mx, where M_ji = C_j^T A_{j:i}^x B_i (Equation 3)

This is exactly the SSS (sequentially semiseparable) representation of an N-semiseparable matrix (Theorem 3.5). The equivalence means that **any method of computing an SSM is a structured matrix multiplication algorithm on semiseparable matrices** (Section 3.4.3).

**Stage 2: Structured Masked Attention.** Masked kernel attention is rewritten as a single 4-way tensor contraction (Equation 12):

> Y = contract(TN, SN, SP, TS -> TP)(Q, K, V, L)

The **quadratic mode** (standard attention) contracts Q and K first to form the Gram matrix (Equation 13). The **linear mode** contracts V and K first, with the bottleneck being multiplication by the mask L (Equation 15). Standard linear attention is the special case where L is the cumsum matrix; SMA generalizes this to **any structured matrix L** (Definition 4.2).

**Stage 3: The Duality.** When A = aI (scalar times identity), the SSM matrix M factors as:

> M = L . (CB^T), where L = 1SS(a)

The quadratic computation of this SSM is identical to masked kernel attention with a 1-semiseparable mask (Equation 16). The notation duality is: C <-> Q, B <-> K, X <-> V, A_{j:i} <-> L_{ji}, N (state expansion) <-> N (kernel feature dimension) (Figure 4).

**The SSD Algorithm** (Section 6) computes the model via block decomposition of M:

1. **Diagonal blocks (intra-chunk):** Compute each chunk's output using the quadratic SMA form -- this is a batched matrix multiplication BMM(T/Q, Q, Q, N) for the kernel matrix and BMM(T/Q, Q, P, Q) for the output.

2. **Right factors (B-block-factors):** Compute per-chunk final states assuming zero initial state -- BMM(T/Q, N, P, Q).

3. **Center factors (A-block-factors):** Propagate states across chunks via a scalar SSM scan of length T/Q on N*P channels -- negligible cost O(TNP/Q).

4. **Left factors (C-block-factors):** Convert corrected states to output contributions -- BMM(T/Q, Q, P, N).

When N = P = Q, all matmul terms become BMM(T/N, N, N, N), yielding:

> Total FLOPs: O(TN^2), Memory: O(TN), dominated by matrix multiplications (Theorem 6.1)

A complete PyTorch implementation is provided in Listing 1 (p. 21, ~40 lines of code).

### Key Technical Components

**Scalar-identity structure on A.** Compared to Mamba's diagonal A, SSD restricts A_t = a_t * I for scalar a_t. This slightly reduces expressivity but enables the dual quadratic form to look exactly like masked attention, allowing matrix multiplication units to be leveraged (Section 2.4, p. 5-6).

**Head dimension P.** Mamba used P = 1 (each channel has independent SSM dynamics). Mamba-2 uses P = {64, 128}, matching Transformer conventions. This is critical for hardware efficiency: the matmul units operate on (N, N) blocks rather than scalar operations (Section 2.4, Section 7.2).

**Parallel projections.** All SSM parameters (A, B, C, X) are projected in parallel from the input u at the beginning of the block, rather than deriving B, C from X sequentially as in Mamba-1. This saves parameters (126.5M vs. 129.3M at 125M scale) and enables tensor parallelism via standard Megatron sharding (Section 7.1, Table 4).

**Extra normalization.** A GroupNorm/RMSNorm layer is added after the gating operation and before the output projection, improving training stability at larger scales. This is analogous to NormFormer (Shleifer, Weston, and Ott (2021)) and similar to normalization used in TransNormerLLM and RetNet (Section 7.1, p. 23).

**Multi-value attention (MVA) / Multi-input SSM (MIS) head pattern.** B and C are shared across all H heads; only X (values) and A have per-head copies. This matches Mamba-1's original design and is shown to outperform MQA, MKA, and MHA patterns at matched total state size (Section 7.2, Table 5).

**Grouped-value attention (GVA) / Grouped-input SSM (GIS).** Extends MVA with G independent (B, C) groups (1 < G, G | H), analogous to grouped-query attention (Ainslie et al. (2023)). This enables more flexible tensor parallelism by setting G to a multiple of the TP degree (Section 7.2, p. 25).

**Variable-length sequence handling.** The entire batch is treated as one long sequence; setting A_t = 0 at sequence boundaries prevents information leakage between sequences. No padding tokens are needed (Section 8.3, p. 28).

### Theoretical Analysis

**Theorem 3.5** (SSM-semiseparable equivalence): The SSM operator SSM(A, B, C) and the SSS matrix constructor SSS(A, B, C) are identical -- structured state space models and sequentially semiseparable matrices share the same acronyms and the same mathematical object (Section 3.3, p. 9).

**Theorem 3.7** (Optimal SSM computation): Any SSM with state size N on sequence length T can be computed in O(TN) time (not accounting for preprocessing). This is tight with the lower bound given by the representation size of B and C (Section 3.4.1, p. 10).

**Theorem 5.2** (Autoregressive attention must be semiseparable): For any SMA instance that is an autoregressive process with bounded order, the mask L must be a semiseparable matrix -- i.e., efficient autoregressive attention is semiseparable SMA. Proved via the inverse closure property of semiseparable matrices (Appendix C.2, p. 49-50).

**Theorem 6.1** (SSD algorithm efficiency): With state expansion N and head dimension P = N, the SSD algorithm achieves O(TN^2) training FLOPs, O(TN) inference FLOPs, O(N^2) inference memory, with work dominated by matrix multiplications. All bounds are tight (Section 6, p. 17-18).

**Closure properties** (Proposition C.1): Semiseparable matrices are closed under addition (order adds), multiplication (order adds), and inverse (order increases by at most 1). These imply that parallel SSMs, sequential SSM composition, and inverses of SSMs remain SSMs (Appendix C.1, p. 48).

### Experimental Setup

**MQAR (Section 9.1):** Multi-query associative recall with T/4 key-value pairs, sequence lengths T in {256, 512, 1024}, model dimensions D in {32, 64, 128, 256}, 2 layers, vocab size 8192. Curriculum training with 4 difficulty levels. Baselines: softmax attention, Based architecture, Mamba-1 (N=16), Mamba-2 (N=16, 64, 256).

**Scaling laws (Section 9.2.1):** Models from 125M to 1.3B parameters trained on the Pile with GPT-2 tokenizer. Chinchilla-optimal token counts (2.5B to 26B tokens). AdamW optimizer, gradient clip 1.0, weight decay 0.1, cosine LR schedule with 5x GPT-3 peak LR. Baselines: Transformer++, Mamba (Table 9, Appendix D.2).

**Downstream evaluations (Section 9.2.2):** Models at 130M, 370M, 780M, 1.3B, 2.7B trained on 300B tokens on the Pile with GPT-NeoX tokenizer. Zero-shot evaluation on LAMBADA, HellaSwag, PIQA, ARC-E, ARC-C, WinoGrande, OpenBookQA using the EleutherAI LM evaluation harness. Baselines: Pythia, Mamba, Hybrid H3, RWKV-4, OPT, GPT-Neo (Tables 1, 10).

**Hybrid models (Section 9.2.3):** 350M (48 layers, 7B tokens) and 2.7B (64 layers, 300B tokens) models combining SSD layers with attention and/or MLP layers. Configurations tested: pure Mamba-2, Mamba-2 + attention (6 of 64 layers), Mamba-2 + MLP, Mamba-2 + MLP + attention, Transformer++ (Tables 2-3).

**Speed benchmarks (Section 9.3):** SSD vs. Mamba scan vs. FlashAttention-2 on A100 80GB PCIe GPU. Sequence lengths 512 to 512K, state dimensions 4 to 256.

**Ablations (Section 9.4):** Block design (Table 4), head structure (Table 5), kernel approximations (Tables 6-7). All ablations at 125M-380M scale with Chinchilla token counts.

**Reproducibility:** Code and pretrained checkpoints at https://github.com/state-spaces/mamba. Training seeds not reported; single run per configuration (no variance estimates reported) (limited evidence for individual data points, but broad coverage across model sizes).

### Key Results

**SSD Speed (Figure 10, Section 9.3):**

| Setting (A100 80GB, N=64) | SSD | Mamba Scan | FlashAttention-2 |
|---|---|---|---|
| Seq len 2K | ~crossover | ~2-3x slower | ~crossover |
| Seq len 16K | ~6x faster than FA-2 | ~4-8x slower than SSD | baseline |
| State dim scaling (seq 4K) | nearly flat (~1ms) | linear increase (~6ms at N=256) | constant (~1ms, independent of N) |

SSD's time is nearly independent of state dimension, while Mamba's scan scales linearly with N (Figure 10, right panel). This enables much larger state sizes without speed penalty.

**Scaling Laws (Figure 9, Section 9.2.1):**

Mamba-2 matches or slightly beats Mamba at every FLOP budget from 125M to 1.3B, and both Pareto-dominate Transformer++ in perplexity vs. FLOPs (tested across 4 model sizes -- moderate evidence).

**Downstream Zero-Shot (Table 1, Section 9.2.2):**

| Model | Pile ppl | LAMBADA ppl | Avg acc (7 tasks) |
|---|---|---|---|
| Pythia-2.8B | 6.73 | 5.04 | 55.7 |
| RWKV4-3B | 7.00 | 5.24 | 56.4 |
| Mamba-2.8B | 6.22 | 4.23 | 59.9 |
| **Mamba-2-2.7B** | **6.09** | **4.10** | **60.2** |
| Pythia-6.9B | 6.51 | 4.45 | 58.3 |

Mamba-2-2.7B achieves 60.2% average accuracy, exceeding Mamba-2.8B (59.9%), Pythia-2.8B (55.7%), and even Pythia-6.9B (58.3%). Similar patterns hold at 780M and 1.3B (Table 10, strong evidence across 5 model sizes).

**Hybrid Models (Table 3, Section 9.2.3):**

| Model (2.7B, 64 layers) | Pile ppl | Avg acc |
|---|---|---|
| Transformer++ | 6.13 | 60.2 |
| Mamba-2 (64 SSD) | 6.09 | 60.2 |
| Mamba-2-Attention (58 SSD + 6 attn) | **5.95** | **61.0** |
| Mamba-2-MLP-Attention (28 SSD + 4 attn + 32 MLP) | 6.00 | 60.7 |
| Mamba-2-MLP (32 SSD + 32 MLP) | 6.13 | 59.6 |

Adding ~10% attention layers (6/64) to Mamba-2 yields the best configuration, outperforming both pure architectures (tested at one model size -- limited evidence for the exact ratio, but supported by the 350M ablation in Table 2).

**MQAR (Figure 8, Section 9.1):**

Mamba-2 with N=256 matches or exceeds softmax attention in all three sequence length settings (256, 512, 1024). Even at the same state size N=16, Mamba-2 substantially outperforms Mamba-1 (which often falls below 50% accuracy). Increasing N from 16 to 64 to 256 consistently improves performance, validating the importance of state size for associative recall (tested across 4 model dimensions and 3 sequence lengths -- moderate evidence).

**Head Structure Ablation (Table 5, Section 9.4.2):**

| Head Pattern | Attn Analog | Ppl (125M) | Ppl (360M) |
|---|---|---|---|
| Multi-input (MIS) | Multi-value (MVA) | **11.66** | **8.73** |
| Multi-contract (MCS) | Multi-query (MQA) | 12.62 | 9.33 |
| Multi-expand (MES) | Multi-key (MKA) | 12.59 | 9.36 |
| Multi-head (MHS) | Multi-head (MHA) | 12.06 | 9.01 |
| Multi-state (MSS) | - | 12.00 | 9.04 |

MVA/MIS is substantially better despite all patterns having the same total state size HPN (tested at two model sizes -- moderate evidence).

---

## Limitations and Failure Modes

**Author-acknowledged limitations:**

- SSD **does not generalize standard softmax attention** or any attention kernel transformation without a finite feature map (Section 10.3, p. 35). The gap between SSD and full softmax attention remains theoretically and empirically uncharacterized for many tasks.

- The scalar-identity restriction on A (compared to Mamba's diagonal A) is a **deliberate expressivity-efficiency tradeoff**. The authors hypothesize that refining the algorithms to support general diagonal A with similar hardware efficiency may be possible, but have not achieved this (Section 10.1, p. 34).

- The authors state they are "not sure which aspect of the architecture is the predominant factor" for Mamba-2's improvement over Mamba-1 on MQAR, even at controlled state sizes (Section 9.1, p. 30).

- Kernel approximation methods from the linear attention literature (cosFormer, Performer, RFA, Based, ReBased) do **not improve** over simple pointwise activations when combined with SSD's 1-semiseparable mask, suggesting the 1-SS mask already captures most of what these methods aim to provide (Section 9.4.3, Tables 6-7; negative result).

- Adding MLP layers in place of SSD layers **reduces model quality** despite improving hardware efficiency, meaning the pure SSD architecture is more parameter-efficient than a hybrid SSD+MLP design (Table 3, Section 9.2.3).

**[Inferred] limitations:**

- **[Inferred]** No evaluation on non-English languages. All training and evaluation uses English-only data (the Pile), limiting generalizability claims.

- **[Inferred]** No variance estimates or multiple seeds reported for any experiment. Single run per configuration makes it difficult to assess robustness of small differences between architectures.

- **[Inferred]** The hybrid model experiments (Table 2 at 350M, Table 3 at 2.7B) test only 1-2 model sizes each; the optimal ratio of attention layers (~10%) may not generalize across scales.

- **[Inferred]** The MQAR task, while informative, is synthetic. The paper does not test on naturalistic information retrieval or in-context learning tasks beyond zero-shot classification.

- **[Inferred]** SSD's advantage over FlashAttention-2 only manifests at sequence length >= 2K. For short-context applications, Transformer architectures with interleaved MLP layers may still be more efficient due to MLP hardware friendliness (acknowledged briefly in Section 9.3).

#### Scope and Comparability

- **What was not tested:** Models beyond 2.7B parameters; non-English languages; fine-tuning performance; instruction following; long-context tasks beyond MQAR (e.g., no evaluation on LongBench, RULER, or document QA); multi-turn dialogue; vision or multimodal tasks.

- **Comparability notes:** Scaling law experiments use the GPT-2 tokenizer while downstream experiments use GPT-NeoX tokenizer. The Transformer++ baseline uses an "improved recipe" (RoPE, SwiGLU MLP, RMSNorm, higher LR) that is stronger than standard GPT-3 but not identical to any single published model's recipe. Direct comparison with Pythia is fair (same tokenizer, dataset, token count), but comparisons with models using different tokenizers (H3, OPT, GPT-Neo) are less directly comparable. The MQAR experiments use a harder variant than most prior work (longer sequences, smaller models, random filler tokens), so results are not directly comparable to prior MQAR numbers.

---

## Conclusions

#### Contributions

1. **SSM-semiseparable equivalence (Theorem 3.5).** Established that state space models are exactly semiseparable matrices, unifying two previously disjoint fields and enabling the transfer of structured matrix algorithms to sequence models.

2. **Structured masked attention (SMA) framework.** Generalized linear attention to arbitrary structured masks via tensor contraction analysis, showing that the quadratic/linear duality is simply a contraction reordering (Section 4, Definition 4.2).

3. **State space duality (SSD) theorem.** Proved that scalar-identity SSMs and 1-semiseparable SMA are dual, and that any efficient autoregressive attention must be an SSM (Theorem 5.2, Section 5).

4. **Hardware-efficient SSD algorithm.** Designed a block decomposition algorithm achieving O(TN^2) training FLOPs dominated by matrix multiplications, with a simple ~40-line PyTorch implementation (Section 6, Listing 1, Theorem 6.1).

5. **Mamba-2 architecture.** Combined parallel projections, extra normalization, MVA head structure, and the SSD algorithm into a practical architecture that is 2-8x faster than Mamba while matching or exceeding its quality (Sections 7-9).

6. **Systems optimizations for SSMs.** Demonstrated tensor parallelism with a single all-reduce per block (matching Transformers), sequence parallelism via state passing, and variable-length handling without padding (Section 8).

7. **Comprehensive ablation study.** Systematically compared head structures (MVA, MQA, MKA, MHA), block designs (parallel vs. sequential projections, extra normalization), and kernel approximations, establishing design principles for SSM architectures (Section 9.4).

#### Implications

1. **SSMs and Transformers share a common mathematical foundation.** The SSD framework suggests that future architectural innovations can be developed from either the SSM or attention perspective and transferred across both paradigms. This is speculative in the sense that the transfer has only been demonstrated for a few techniques so far.

2. **Hybrid SSM-attention architectures may be optimal.** The finding that ~10% attention layers improve pure Mamba-2 suggests that SSMs and attention capture complementary capabilities -- SSMs for general sequence processing, attention for precise retrieval. This aligns with concurrent work (Jamba, Griffin) but the optimal ratio likely depends on task and scale.

3. **State expansion is critical for information-dense tasks.** SSD's ability to scale state size N without proportional slowdown may prove crucial as models are applied to tasks requiring larger working memory (e.g., multi-step reasoning, code generation).

---

## Key Claims

1. **SSMs are semiseparable matrices (C1).** The SSM transformation y = SSM(A,B,C)(x) with state size N is identical to multiplication by an N-semiseparable matrix in SSS form (Theorem 3.5, Section 3). This is an exact equivalence, not an approximation. Applies to all structured SSMs regardless of A structure (strong evidence -- formal proof).

2. **Optimal SSM computation complexity (C2).** Any SSM with state size N on sequence length T can be computed in O(TN) time, matching the lower bound (Theorem 3.7, Section 3.4). This holds even for unstructured A with preprocessing. (Strong evidence -- formal proof, with practical caveats about preprocessing cost.)

3. **Efficient autoregressive attention requires semiseparable masks (C3).** Any SMA instance with bounded-order autoregressive recurrence must use a semiseparable mask, and is therefore an SSM (Theorem 5.2, proved in Appendix C.2). Scope: autoregressive transformations with bounded order k. (Strong evidence -- formal proof.)

4. **SSD is 2-8x faster than Mamba's scan (C4).** The SSD algorithm achieves 2-8x speedup over Mamba's optimized selective scan at N=64 on an A100 GPU, and SSD's runtime is nearly independent of state dimension while Mamba's scales linearly (Figure 10, Section 9.3). Scope: A100 80GB PCIe, sequence lengths 512-512K, N=64. (Moderate evidence -- single GPU type benchmarked, no variance reported.)

5. **Mamba-2 Pareto-dominates on scaling laws (C5).** Mamba-2 achieves equal or lower perplexity than both Mamba and Transformer++ at every FLOP budget from 125M to 1.3B parameters under Chinchilla scaling on the Pile (Figure 9, Section 9.2.1). (Moderate evidence -- 4 model sizes, single runs, one dataset.)

6. **Mamba-2-2.7B outperforms larger Pythia models (C6).** Mamba-2-2.7B achieves 60.2% average zero-shot accuracy across 7 tasks, exceeding Mamba-2.8B (59.9%), Pythia-2.8B (55.7%), and Pythia-6.9B (58.3%) (Table 1/10, Section 9.2.2). Scope: 300B tokens on the Pile, GPT-NeoX tokenizer, 7 downstream tasks. (Moderate evidence -- 5 model sizes but single runs, English only.)

7. **Mamba-2 dramatically improves over Mamba-1 on MQAR (C7).** On the multi-query associative recall task, Mamba-2 with N=256 matches or exceeds softmax attention, while Mamba-1 with N=16 often falls below 50% accuracy. Even at matched N=16, Mamba-2 substantially outperforms Mamba-1 (Figure 8, Section 9.1). (Moderate evidence -- synthetic task, 4 model dims x 3 sequence lengths.)

8. **Hybrid SSD+attention outperforms pure architectures (C8).** At 2.7B scale, 58 SSD + 6 attention layers achieves 5.95 Pile ppl and 61.0% avg accuracy, exceeding pure Mamba-2 (6.09/60.2) and Transformer++ (6.13/60.2) (Table 3, Section 9.2.3). (Limited evidence -- one model size at full scale, supported by 350M ablation in Table 2.)

9. **MVA/MIS head pattern is best for SSMs (C9).** The multi-value attention pattern (B, C shared across heads, X per-head) outperforms MQA, MKA, and MHA patterns at matched total state size, with 11.66 vs. 12.06-12.62 ppl at 125M and 8.73 vs. 9.01-9.36 at 360M (Table 5, Section 9.4.2). (Moderate evidence -- 2 model sizes, consistent pattern.)

10. **Kernel approximations do not help SSD (C10).** Various linear attention kernel feature maps (cosFormer, Performer, RFA, Based, ReBased) do not improve over simple Swish/SiLU when combined with SSD's 1-semiseparable mask. The authors attribute this to the mask already providing what these methods aim to approximate (Tables 6-7, Section 9.4.3). (Moderate evidence -- tested at 125M-380M, single runs.)

---

## Open Questions

1. **Can SSD algorithms be extended to general diagonal A?** The authors hypothesize this is possible but have not achieved it. General diagonal A would restore full Mamba-level expressivity with SSD-level hardware efficiency (Section 10.1, p. 34). Not yet addressed.

2. **What drives Mamba-2's MQAR improvement over Mamba-1 at matched state size?** Even with N=16, Mamba-2 substantially outperforms Mamba-1 on MQAR, but the authors cannot identify which architectural change is responsible (Section 9.1, p. 30). Not yet addressed.

3. **Do attention sinks exist in Mamba models?** The attention sink phenomenon has been observed in Transformers; whether analogous artifacts exist in SSMs and whether interpretability techniques transfer remains open (Section 10.3, p. 35). Partially addressed by 2025-04-attention-sink-emerges (for Transformers) but not specifically for SSMs.

4. **Can SSD enable principled non-causal Mamba variants?** The matrix mixer viewpoint could enable bidirectional SSM variants, but this remains unexplored (Section 10.2, p. 35). Not yet addressed.

5. **What are the theoretical limits of SSMs on copying and ICL tasks?** Concurrent work has started studying SSM vs. attention tradeoffs on copying and in-context learning, but a complete picture is missing (Section 10.3, p. 35). Not yet addressed.

6. **Can other structured masks in SMA yield useful new models?** The framework accommodates Toeplitz, Fourier, and other structured masks, but only the semiseparable case has been explored empirically (Section 4.3, Figure 3). Not yet addressed.

---

## Core References and Why They Are Referenced

### Direct Predecessors

- **Gu and Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* The immediate predecessor: introduces the selective SSM (S6) that Mamba-2 refines. Provides the baseline architecture, training recipe, and experimental setup that this paper extends.

- **Katharopoulos et al. (2020)** -- *Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention.* The paper's title is an homage to this work, which first connected attention to linear RNNs. SSD significantly generalizes this connection from LTI cumsum masks to arbitrary structured masks.

- **Gu, Goel, and Re (2022)** -- *Efficiently Modeling Long Sequences with Structured State Spaces (S4).* Introduced the diagonal-plus-low-rank structure for SSMs and the DPLR parameterization. SSD extends this lineage by establishing the semiseparable matrix equivalence.

### Structured Matrix Theory

- **Vandebril et al. (2005)** -- *A Bibliography on Semiseparable Matrices.* Survey of the semiseparable matrix literature that provides the mathematical foundation for the SSM-semiseparable connection.

- **Pernet, Signargout, and Villard (2023)** -- *Exact Computations with Quasiseparable Matrices.* Provides tight bounds on semiseparable matrix representation and multiplication, directly used in Proposition 3.6 and Theorem 3.7.

### Concurrent and Related Models

- **Sun et al. (2023)** -- *Retentive Network: A Successor to Transformer.* RetNet uses decay masks as a special case of SSD's structured masked attention; architecturally differs in using MHA rather than MVA head patterns.

- **Katsch (2023)** -- *GateLoop: Fully Data-Controlled Linear Recurrence.* Concurrently proposed input-dependent decay factors and the same dual quadratic "surrogate attention" form as SSD.

- **Yang et al. (2024)** -- *Gated Linear Attention Transformers.* Proposed gated linear attention with chunkwise algorithms, a related approach to SSD's block decomposition.

- **De et al. (2024)** -- *Griffin: Mixing Gated Linear Recurrences with Local Attention.* Showed that RNN + local attention hybrids compete with strong Transformers, supporting the hybrid results in Section 9.2.3.

- **Lieber et al. (2024)** -- *Jamba: A Hybrid Transformer-Mamba Language Model.* Concurrent hybrid Mamba-attention work validating the complementarity finding.

### Hardware and Systems

- **Dao (2024)** -- *FlashAttention-2: Faster Attention with Better Parallelism.* The main attention speed baseline; SSD is benchmarked against it to demonstrate competitive or superior training throughput.

- **Shoeybi et al. (2019)** -- *Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism.* Provides the tensor parallelism framework that Mamba-2 is specifically designed to support.

### Evaluation Baselines

- **Biderman et al. (2023)** -- *Pythia: A Suite for Analyzing Large Language Models.* Provides the primary Transformer baseline trained under identical conditions (same tokenizer, dataset, token count) for fair comparison.

- **Hoffmann et al. (2022)** -- *Chinchilla: An Empirical Analysis of Compute-Optimal Training.* Provides the scaling law protocol (token-to-parameter ratio) used for all scaling experiments.

- **Brown et al. (2020)** -- *GPT-3: Language Models are Few-Shot Learners.* Provides model size specifications and training recipe baselines used throughout the experiments.

### Attention Variants

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Motivates the grouped head patterns (GVA/GIS) that extend the MVA pattern in Mamba-2 for tensor parallelism.

- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head is All You Need.* Introduces multi-query attention, which SSD's head pattern framework subsumes and generalizes.
