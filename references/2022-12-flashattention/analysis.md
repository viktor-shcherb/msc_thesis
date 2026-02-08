---
title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
authors: "Dao, Fu, Ermon, Rudra, Re"
year: 2022
venue: "NeurIPS 2022"
paper_type: conference-paper
categories: ["attention-efficiency", "architecture"]
scope: ["exact attention", "GPU memory optimization", "training efficiency"]
benchmarks_used: ["lra"]
models_introduced: []
models_evaluated: ["bert-large", "gpt-2"]
key_claims:
  - id: C1
    claim: "Standard attention is memory-bound: HBM accesses, not FLOPs, determine wall-clock runtime"
    evidence: "Figure 2 left panel table, Section 3.2"
    status: supported
    scope: "A100 GPU, GPT-2 medium, seq length 1024, head dim 64, 16 heads, batch size 64"
    magnitude: "41.7 ms runtime with 40.3 GB HBM R/W vs. 7.3 ms with 4.4 GB HBM R/W despite higher FLOPs (75.2 vs 66.6 GFLOPs)"
  - id: C2
    claim: "FlashAttention requires O(N^2 d^2 M^{-1}) HBM accesses compared to Theta(Nd + N^2) for standard attention"
    evidence: "Theorem 2, Section 3.2, proof in Appendix C"
    status: supported
    scope: "Exact attention computation, SRAM size M with d <= M <= Nd"
    magnitude: "Up to 9x fewer HBM accesses for typical d=64-128, M~100KB"
  - id: C3
    claim: "No exact attention algorithm can asymptotically improve on O(N^2 d^2 M^{-1}) HBM accesses for all SRAM sizes"
    evidence: "Proposition 3, proof in Appendix C"
    status: supported
    scope: "All M in [d, Nd], exact (not approximate) attention"
    magnitude: "qualitative (lower bound proof)"
  - id: C4
    claim: "FlashAttention trains BERT-large 15% faster than the MLPerf 1.1 speed record"
    evidence: "Table 1, Section 4.1"
    status: supported
    scope: "BERT-large (340M params), seq length 512, 8xA100-80GB GPUs, LAMB optimizer, target 72.0% masked LM accuracy"
    magnitude: "17.4 +/- 1.4 min vs 20.0 +/- 1.5 min (averaged over 10 runs)"
  - id: C5
    claim: "FlashAttention achieves up to 3.5x speedup on GPT-2 training over HuggingFace baseline"
    evidence: "Table 2, Section 4.1"
    status: supported
    scope: "GPT-2 small/medium, seq length 1K, OpenWebText, 8xA100-40GB GPUs, 400K steps"
    magnitude: "GPT-2 small: 2.7 days vs 9.5 days (3.5x); GPT-2 medium: 6.9 days vs 21.0 days (3.0x); 1.7-2.0x over Megatron-LM"
  - id: C6
    claim: "FlashAttention memory scales linearly with sequence length, up to 20x more efficient than standard attention"
    evidence: "Figure 3 right, Table 21, Section 4.3"
    status: supported
    scope: "A100-40GB GPU, batch size 16, 8 heads, head dim 64, no dropout/masking"
    magnitude: "209 MB at N=1024 vs 1184 MB standard; 836 MB at N=4096 vs 17024 MB standard; linear vs quadratic scaling"
  - id: C7
    claim: "FlashAttention enables the first Transformer to achieve better-than-chance on Path-X (16K) and Path-256 (64K)"
    evidence: "Table 6, Section 4.2"
    status: supported
    scope: "Path-X (128x128 images, 16K tokens) and Path-256 (256x256 images, 64K tokens), pretrained on Path-64 with positional embedding interpolation"
    magnitude: "61.4% on Path-X (FlashAttention), 56.0%/63.1% on Path-X/Path-256 (block-sparse); chance is 50%"
  - id: C8
    claim: "Longer context enabled by FlashAttention improves model quality on language modeling and document classification"
    evidence: "Table 4, Table 5, Section 4.2"
    status: supported
    scope: "GPT-2 small on OpenWebText (context 1K-4K), RoBERTa on MIMIC-III and ECtHR (seq 512-16K)"
    magnitude: "0.7 perplexity improvement (17.5 vs 18.2) with 4K context; +4.3 F1 on MIMIC-III (57.1 vs 52.8) and +8.5 F1 on ECtHR (80.7 vs 72.2)"
  - id: C9
    claim: "FlashAttention is up to 3x faster than PyTorch attention for sequences up to 2K; block-sparse FlashAttention is faster than all known approximate attention methods"
    evidence: "Figure 3, Tables 9-20, Section 4.3"
    status: supported
    scope: "A100-40GB GPU, batch size 16, 8 heads, head dim 64, with/without dropout and masking"
    magnitude: "Up to 3x speedup over PyTorch; block-sparse is fastest across all sequence lengths tested (128-64K)"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Provides an IO-aware implementation of the standard Transformer attention mechanism"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses sparse attention patterns; FlashAttention provides an efficient exact attention primitive that can be combined with sparsity"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi addresses length extrapolation through position encoding; FlashAttention addresses computational efficiency of attention"
  - target: 2024-05-flashattention-2
    type: extended-by
    detail: "FlashAttention-2 improves GPU utilization from 25-40% to 50-73% through better parallelism and work partitioning"
  - target: 2024-05-ring-attention-near-infinite-context
    type: extended-by
    detail: "Ring Attention builds on memory-efficient attention techniques, using blockwise computation locally on each host and overlapping inter-host KV communication to enable context lengths scaling with device count"
  - target: 2024-12-flashattention-3
    type: extended-by
    detail: "FlashAttention-3 achieves 75% H100 utilization through warp-specialized asynchrony, GEMM-softmax pipelining, and FP8 low-precision support"
  - target: 2024-05-mamba-selective-state-spaces
    type: complementary
    detail: "Mamba (co-authored by Tri Dao) proposes an alternative to attention entirely using selective SSMs; both address Transformer efficiency but FlashAttention optimizes exact attention IO while Mamba eliminates quadratic attention altogether"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV achieves linear time and constant memory by replacing attention with channel-wise time decay; FlashAttention retains quadratic time but makes exact attention IO-efficient"
  - target: 2023-07-retnet-retentive-network
    type: complementary
    detail: "RetNet compares training efficiency against FlashAttention-optimized Transformers, claiming competitive throughput with vanilla PyTorch; both address Transformer efficiency from opposite directions"
  - target: 2025-04-differential-transformer
    type: complementary
    detail: "DIFF Transformer provides a FlashAttention-compatible implementation of its differential attention mechanism, leveraging FlashAttention's IO-aware tiling for efficient training and inference"
open_questions:
  - question: "How can FlashAttention be extended to multi-GPU settings with efficient inter-GPU communication?"
    addressed_by: 2024-05-ring-attention-near-infinite-context
  - question: "Can the IO-aware approach be compiled from high-level code rather than requiring custom CUDA kernels?"
    addressed_by: null
  - question: "How do the benefits scale to even larger models (10B+ parameters)?"
    addressed_by: null
  - question: "Can GPU utilization be improved beyond 25-40% of theoretical maximum?"
    addressed_by: 2024-05-flashattention-2
  - question: "Can the block-sparse extension support content-dependent or learned sparsity patterns rather than fixed patterns?"
    addressed_by: null
  - question: "Can the IO-aware approach extend beyond attention to other memory-intensive deep learning operations?"
    addressed_by: null
---

# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

**Authors:** Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Re (Stanford University; University at Buffalo, SUNY)
**Date:** December 2022, NeurIPS 2022 (arXiv:2205.14135)

---

## Core Research Problem

Transformers have become the dominant architecture in NLP and vision, but their self-attention mechanism has time and memory complexity quadratic in sequence length N, making long sequences prohibitively expensive. Many approximate attention methods -- sparse (Kitaev et al., 2020), low-rank (Choromanski et al., 2020; Wang et al., 2020), and combinations (Beltagy et al., 2020; Zaheer et al., 2020) -- have been proposed to reduce compute complexity to linear or near-linear. However, these methods often **fail to achieve wall-clock speedup** against standard attention and have not gained wide adoption (Section 1).

The authors identify the root cause: existing methods focus on reducing FLOPs, but on modern GPUs, **compute speed has outpaced memory speed**, making most Transformer operations memory-bound rather than compute-bound (Ivanov et al., 2021). The bottleneck is reading and writing data between levels of the GPU memory hierarchy:

- **GPU SRAM (on-chip):** ~19 TB/s bandwidth, 192 KB per streaming multiprocessor (A100 has 108 SMs)
- **GPU HBM (high bandwidth memory):** 1.5-2.0 TB/s bandwidth, 40-80 GB capacity (A100)

Standard attention implementations materialize the N x N attention matrices S and P to HBM, requiring O(N^2) memory accesses. For typical models where N >> d (e.g., GPT-2 with N=1024, d=64), these memory accesses dominate runtime (Section 2.2).

**The core challenge is: computing exact attention with sub-quadratic HBM accesses while maintaining numerical correctness and supporting the backward pass for training.**

---

## Problem Solutions

The paper introduces **FlashAttention**, an IO-aware exact attention algorithm built on two well-established techniques:

1. **Tiling.** Split the inputs Q, K, V into blocks that fit in SRAM. Compute attention output incrementally by maintaining running statistics (max and sum) for the softmax normalization. This avoids materializing the full N x N attention matrix to HBM.

2. **Recomputation.** Instead of storing the O(N^2) attention matrix for the backward pass, store only the output O and softmax normalization statistics (m, l). Recompute the attention matrix on-the-fly during the backward pass from blocks of Q, K, V in SRAM. Despite increased FLOPs, this is faster due to massively reduced HBM access.

3. **Kernel fusion.** All operations (matrix multiply, softmax, masking, dropout, matrix multiply) are fused into a single CUDA kernel, avoiding repeated HBM reads/writes that typically occur between unfused operations.

---

## Approach Details

### Method

Standard attention computes:

> S = QK^T in R^{N x N}, P = softmax(S) in R^{N x N}, O = PV in R^{N x d}

where softmax is applied row-wise. Standard implementations write S and P to HBM (Algorithm 0, Section 2.2).

FlashAttention restructures this computation to avoid materializing S and P. The key insight is that softmax can be decomposed across blocks using the following identity. For a vector x in R^B:

> m(x) = max_i x_i, f(x) = [e^{x_1 - m(x)} ... e^{x_B - m(x)}], l(x) = sum_i f(x)_i, softmax(x) = f(x)/l(x)

For concatenated vectors x = [x^{(1)} x^{(2)}]:

> m(x) = max(m(x^{(1)}), m(x^{(2)}))
> l(x) = e^{m(x^{(1)}) - m(x)} l(x^{(1)}) + e^{m(x^{(2)}) - m(x)} l(x^{(2)})

By tracking statistics (m, l), softmax can be computed one block at a time without materializing the full attention matrix (Section 3.1). This is termed *algebraic aggregation* (Gray et al., 1997).

### Key Technical Components

**Block sizes (Algorithm 1, line 1).** Given SRAM size M:

> B_c = ceil(M / (4d)), B_r = min(ceil(M / (4d)), d)

These ensure blocks of K, V (size B_c x d), Q, O (size B_r x d), and S (size B_r x B_c) fit in SRAM simultaneously.

**Algorithm structure (forward pass, Algorithm 1).** The outer loop iterates over K, V blocks (index j = 1..T_c where T_c = ceil(N/B_c)). The inner loop iterates over Q blocks (index i = 1..T_r where T_r = ceil(N/B_r)). For each (i, j) pair:

1. Load K_j, V_j from HBM to SRAM (line 6)
2. Load Q_i, O_i, l_i, m_i from HBM to SRAM (line 8)
3. Compute S_{ij} = Q_i K_j^T on chip (line 9)
4. Compute local softmax statistics: m_tilde_{ij} = rowmax(S_{ij}), P_tilde_{ij} = exp(S_{ij} - m_tilde_{ij}), l_tilde_{ij} = rowsum(P_tilde_{ij}) (line 10)
5. Update global statistics: m_i^new = max(m_i, m_tilde_{ij}), l_i^new = e^{m_i - m_i^new} l_i + e^{m_tilde_{ij} - m_i^new} l_tilde_{ij} (line 11)
6. Update output: O_i <- diag(l_i^new)^{-1} (diag(l_i) e^{m_i - m_i^new} O_i + e^{m_tilde_{ij} - m_i^new} P_tilde_{ij} V_j) (line 12)
7. Write O_i, l_i, m_i back to HBM (lines 12-13)

The full forward pass (Algorithm 2, Appendix B.3) also includes softmax scaling tau (typically 1/sqrt(d)), masking (MASK function for padding), dropout (with PRNG state saved for backward pass recomputation), and numerical stability via max-shifting.

**Backward pass (Algorithm 4, Appendix B.4).** Store only O, l, m (and PRNG state for dropout). Recompute S_{ij} and P_{ij} from blocks of Q_i, K_j during backward. The key identity D_i = P_{i:}^T dP_{i:} = do_i^T o_i (Eq. 4) allows computing the softmax gradient without reducing over vectors of size N, since do_i and o_i have size d (Section B.2). The backward pass loop structure mirrors the forward pass, accumulating gradients dQ, dK, dV in a blockwise manner (Algorithm 4, lines 6-25).

**Comparison with Rabe and Staats (2021).** Three major differences are described in Appendix B.5: (1) FlashAttention focuses on reducing memory *accesses* (achieving 2-4x speedup) while Rabe & Staats focuses on reducing total memory *footprint* (roughly same speed as standard attention); (2) FlashAttention incrementally updates one copy of O rather than maintaining K copies for K blocks; (3) FlashAttention derives the backward pass analytically and only recomputes the attention matrix, not temporary block outputs.

### Theoretical Analysis

**Theorem 1 (Correctness and complexity).** Algorithm 1 returns O = softmax(QK^T)V with O(N^2 d) FLOPs and requires O(N) additional memory beyond inputs and output (Section 3.1, proof in Appendix C by induction on j).

**Theorem 2 (IO complexity).** Let N be sequence length, d be head dimension, and M be SRAM size with d <= M <= Nd:

> Standard attention: Theta(Nd + N^2) HBM accesses
> FlashAttention: Theta(N^2 d^2 M^{-1}) HBM accesses

For typical values (d=64-128, M ~ 100KB), d^2 is many times smaller than M, so FlashAttention requires **many times fewer HBM accesses** (Section 3.2, proof in Appendix C). The proof proceeds by noting that K, V blocks of size Theta(M) are loaded, requiring Theta(Nd/M) passes over Q and O, each loading Theta(Nd) elements, yielding Theta(N^2 d^2 / M) total.

**Proposition 3 (Lower bound / Optimality).** No exact attention algorithm can achieve o(N^2 d^2 M^{-1}) HBM accesses for all M in [d, Nd]. The proof uses a contradiction: at M = Theta(Nd), any algorithm must perform at least Omega(Nd) accesses (to read inputs and write outputs), which matches Theta(N^2 d^2 / (Nd)) = Theta(Nd) (Section 3.2, Appendix C).

**Theorem 5 (Backward IO complexity).** The FlashAttention backward pass (Algorithm 4) requires Theta(N^2 d^2 M^{-1}) HBM accesses, matching the forward pass, while the standard backward requires Theta(Nd + N^2) (Appendix B.4, proof in Appendix C).

### Extension: Block-Sparse FlashAttention

Given a block sparsity mask M in {0,1}^{(N/B_r) x (N/B_c)}, the algorithm skips zero blocks (Algorithm 5, Appendix D.1). The IO complexity becomes:

> Theta(Nd + N^2 d^2 M^{-1} s)

where s is the fraction of nonzero blocks (Proposition 4). For large N, typical sparsity patterns use s = N^{-1/2} (Child et al., 2019) or s = N^{-1} log N (Beltagy et al., 2020; Zaheer et al., 2020), yielding O(N sqrt(N)) or O(N log N) IO complexity. The fixed butterfly sparsity pattern from Dao et al. (2022) is used in experiments, as it can approximate arbitrary sparsity patterns (Dao et al., 2020) (Section 3.3).

### Experimental Setup

**BERT-large training (Section 4.1, Appendix E.1).** 16 layers, 1024 hidden, 16 heads, 340M parameters. Wikipedia dataset. LAMB optimizer, lr=3.75e-3, batch size 448, max 7100 steps, FP16 with Apex AMP (O2). Stopped at 72.0% validation accuracy on masked LM. 8xA100-80GB GPUs. Averaged over 10 runs. Compared against Nvidia's MLPerf 1.1 submission.

**GPT-2 training (Section 4.1, Appendix E.2).** Small (117M) and medium (345M) models. OpenWebText dataset with GPT-2 BPE tokenizer. AdamW optimizer, lr=6e-4 (small) / 1.5e-4 (medium), weight decay 0.1, effective batch size 512 (gradient accumulation), 400K steps. Mixed-precision (PyTorch AMP). 8xA100-40GB GPUs. 0.5% random validation split (fixed across all models). Compared against HuggingFace and Megatron-LM.

**Long-Range Arena (Section 4.1, Appendix E.3).** Five tasks with sequence lengths 1K-4K: ListOps, Text, Retrieval, Image, Pathfinder. Hyperparameters from Tay et al. (2020) and Xiong et al. (2021). Mixed-precision for all except Performer (unstable) and Local Attention (no FP16 support). Speedup computed as geometric mean of per-task speedups.

**Long document classification (Section 4.2, Appendix E.2).** MIMIC-III (medical discharge summaries, avg 2,395 tokens, max 14,562 tokens) and ECtHR (legal cases, avg 2,197 tokens, max 49,392 tokens). Fine-tune pretrained RoBERTa with repeated positional embeddings (following Beltagy et al., 2020), varying sequence length from 512 to 16K.

**Path-X and Path-256 (Section 4.2, Appendix E.3).** Classify whether two points in 128x128 (Path-X, 16K tokens) or 256x256 (Path-256, 64K tokens) images are connected. Pretrain on Path-64 for 200 epochs, then transfer with spatially interpolated positional embeddings and fine-tune for 200 epochs (cosine decay with 1 epoch warmup). For Path-X, an additional 200-epoch fine-tuning stage adds roughly 4 points of accuracy.

**Attention benchmarking (Section 4.3, Appendix E.6).** One A100-40GB GPU, 8 heads, head dim 64, batch size 16. Random Q, K, V. Dropout 0.1, padding mask with random lengths. Average of 100 measurements. Baselines: PyTorch, Megatron (exact); Reformer, Local Attention, Linformer, Smyrf, LSFormer (approximate); Block Sparse (OpenAI), Longformer, BigBird (sparse).

**Reproducibility:** Code is open-sourced at https://github.com/HazyResearch/flash-attention (later https://github.com/Dao-AILab/flash-attention). Training seeds and exact hyperparameters are provided. Validation curves (Figure 4) confirm FlashAttention produces identical training/validation perplexity curves as baseline implementations.

### Key Results

**Training speed (Tables 1-2):**

| Model | Implementation | Time | Speedup |
|---|---|---|---|
| BERT-large | Nvidia MLPerf 1.1 | 20.0 +/- 1.5 min | 1.0x |
| BERT-large | FlashAttention | 17.4 +/- 1.4 min | 1.15x |
| GPT-2 small | HuggingFace | 9.5 days | 1.0x |
| GPT-2 small | Megatron-LM | 4.7 days | 2.0x |
| GPT-2 small | FlashAttention | 2.7 days | 3.5x |
| GPT-2 medium | HuggingFace | 21.0 days | 1.0x |
| GPT-2 medium | Megatron-LM | 11.5 days | 1.8x |
| GPT-2 medium | FlashAttention | 6.9 days | 3.0x |

GPT-2 perplexity is identical across implementations: 18.2 (small) and 14.2-14.3 (medium), confirming numerical equivalence (Table 2, Figure 4).

**Long-Range Arena accuracy (Table 3):**

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Avg | Speedup |
|---|---|---|---|---|---|---|---|
| Transformer | 36.0 | 63.6 | 81.6 | 42.3 | 72.7 | 59.3 | - |
| FlashAttention | 37.6 | 63.9 | 81.4 | 43.5 | 72.7 | 59.8 | 2.4x |
| Block-sparse FlashAttention | 37.0 | 63.0 | 81.3 | 43.6 | 73.3 | 59.6 | 2.8x |
| Linformer | 35.6 | 55.9 | 77.7 | 37.8 | 67.6 | 54.9 | 2.5x |
| Linear Attention | 38.8 | 63.2 | 80.7 | 42.6 | 72.5 | 59.6 | 2.3x |
| Performer | 36.8 | 63.6 | 82.2 | 42.1 | 69.9 | 58.9 | 1.8x |
| Local Attention | 36.1 | 60.2 | 76.7 | 40.6 | 66.6 | 56.0 | 1.7x |
| Reformer | 36.5 | 63.8 | 78.5 | 39.6 | 69.4 | 57.6 | 1.3x |
| Smyrf | 36.1 | 64.1 | 79.0 | 39.6 | 70.5 | 57.9 | 1.7x |

FlashAttention matches or exceeds standard attention accuracy while being 2.4x faster. Block-sparse FlashAttention is the fastest method at 2.8x. Note: LRA accuracy is highly dependent on tuning (Xiong et al., 2021); reproduced baselines perform better than originally reported.

**Longer context quality -- GPT-2 small on OpenWebText (Table 4):**

| Implementation | Context length | Perplexity | Training time (speedup vs Megatron 1K) |
|---|---|---|---|
| GPT-2 small - Megatron-LM | 1K | 18.2 | 4.7 days (1.0x) |
| GPT-2 small - FlashAttention | 1K | 18.2 | 2.7 days (1.7x) |
| GPT-2 small - FlashAttention | 2K | 17.6 | 3.0 days (1.6x) |
| GPT-2 small - FlashAttention | 4K | 17.5 | 3.6 days (1.3x) |

GPT-2 with FlashAttention and 4K context is **30% faster** than Megatron with 1K context while achieving **0.7 better perplexity** (limited evidence: single model size, single dataset).

**Long document classification -- micro-F1 (Table 5):**

| Dataset | 512 | 1024 | 2048 | 4096 | 8192 | 16384 |
|---|---|---|---|---|---|---|
| MIMIC-III | 52.8 | 50.7 | 51.7 | 54.6 | 56.4 | 57.1 |
| ECtHR | 72.2 | 74.3 | 77.1 | 78.6 | 80.7 | 79.2 |

Longer sequences yield **+4.3 points** on MIMIC-III (512 to 16K) and **+8.5 points** on ECtHR (512 to 8K). ECtHR peaks at 8K with slight degradation at 16K; MIMIC-III shows non-monotonic improvement at 1024, possibly due to distribution shift in specialized medical text (limited evidence: 2 datasets, single pretrained model RoBERTa).

**Path-X and Path-256 -- first Transformer solutions (Table 6):**

| Model | Path-X (16K) | Path-256 (64K) |
|---|---|---|
| Transformer (standard) | X | X |
| Linformer | X | X |
| Linear Attention | X | X |
| Performer | X | X |
| Local Attention | X | X |
| Reformer | X | X |
| Smyrf | X | X |
| FlashAttention | 61.4 | X |
| Block-sparse FlashAttention | 56.0 | 63.1 |

(X = OOM or random performance; chance is 50%. Path-256 has relatively shorter paths than Path-X despite longer sequences, making it easier to obtain higher accuracy.)

**Runtime and memory benchmarks (A100, batch 16, 8 heads, d=64, Tables 9-21):**

FlashAttention is up to 3x faster than PyTorch attention for sequences up to 2K. Approximate/sparse methods begin to cross over with FlashAttention between sequences of 512 and 1024, but **block-sparse FlashAttention is faster than all known implementations** across all sequence lengths tested (128-64K).

Memory footprint scales linearly with sequence length for FlashAttention:

| Attention Method | N=1024 | N=4096 | N=65536 |
|---|---|---|---|
| PyTorch Attention | 1184 MB | 17024 MB | OOM |
| Linformer | 287 MB | 1652 MB | 26252 MB |
| FlashAttention | 209 MB | 836 MB | 13376 MB |

FlashAttention is up to **20x more memory-efficient** than exact attention and 2x more efficient than Linformer at 64K (Table 21, measured on combined forward+backward without dropout/masking).

### Comparison with Apex FMHA

Table 7 (Appendix E.4) compares FlashAttention against Nvidia's Apex FMHA (the fastest known implementation at the time, limited to head dim 64, A100, seq <= 512). At BERT-large configuration (batch 64, 16 heads, d=64):

| Method | 128 (fwd+bwd) | 256 (fwd+bwd) | 512 (fwd+bwd) |
|---|---|---|---|
| Apex FMHA | 0.27 ms | 0.81 ms | 2.95 ms |
| FlashAttention | 0.28 ms | 0.75 ms | 2.81 ms |

FlashAttention is 4% slower at length 128, 8% faster at 256, and 5% faster at 512. FlashAttention's forward pass is generally faster but backward pass is slightly slower due to recomputation overhead. Unlike FMHA, FlashAttention supports longer sequences, more head dimensions (16, 32, 64, 128), and broader GPU types (all Turing and Ampere GPUs).

### Speedup Across GPU Types

Speedup varies by GPU due to different HBM bandwidth and SRAM sizes (Appendix E.5):
- **A100 (d=64):** 2-4x speedup, more with dropout+masking due to kernel fusion (Figure 5)
- **A100 (d=128):** Less speedup overall, but up to 3x with causal masking (Figure 6)
- **RTX 3090:** 2.5-4.5x speedup, slightly higher than A100 due to lower memory bandwidth (~900 GB/s vs ~1.5 TB/s) (Figure 7)
- **T4:** 1.5-3.5x combined speedup, 2.5-4.5x forward-only; smaller SRAM requires smaller block sizes, matching IO analysis prediction (Figure 8)

---

## Limitations and Failure Modes

1. **Requires custom CUDA kernels.** Each attention variant requires reimplementation in CUDA, a considerably lower-level language than PyTorch, requiring significant engineering effort. Implementations may not be transferable across GPU architectures (Section 5, "Compiling to CUDA").

2. **Head dimension constraints.** Current implementation supports head dimensions 16, 32, 64, 128. Other dimensions require additional kernel implementations (Section 5, Appendix E.4).

3. **Single-GPU optimization.** The IO analysis is optimal for a single GPU. Multi-GPU settings introduce inter-GPU communication as an additional memory hierarchy level not addressed in this work (Section 5, "Multi-GPU IO-Aware Methods").

4. **Not always faster at short sequences.** At sequence length 128, FlashAttention is 4% slower than Apex FMHA in forward+backward (Table 7, Appendix E.4). This is because recomputation overhead is proportionally larger when the sequence is short.

5. **[Inferred]** Approximate methods eventually cross over. For sequences beyond 512-1024, some approximate methods (e.g., Linformer) become faster in raw runtime than FlashAttention, though they sacrifice exactness (Figure 3 left, Section 4.3). Block-sparse FlashAttention remains faster than all approximate methods.

6. **[Inferred]** Block-sparse patterns are fixed. The sparsity pattern must be determined before training; dynamic or content-dependent sparsity is not supported (Section 3.3, Algorithm 5). The fixed butterfly pattern is used throughout.

7. **[Inferred]** No evaluation on non-English languages, and quality evaluation is limited to two downstream tasks (MIMIC-III and ECtHR) plus language modeling perplexity. The generalizability of the quality improvements from longer context is not extensively validated.

#### Scope and Comparability

- **What was not tested:** Models larger than GPT-2 medium (345M parameters) were not evaluated for training speed or quality. The paper does not test FlashAttention with models at 1B+ scale. No evaluation on generation quality metrics (only perplexity and classification). No multi-GPU training experiments.
- **Hardware scope:** All training experiments on A100 GPUs (80GB for BERT, 40GB for GPT-2). Benchmarking covers A100, RTX 3090, and T4, but training experiments are A100-only.
- **Comparability notes:** The LRA accuracy results are highly dependent on tuning procedures (footnote 3, p. 8); the authors' reproduced baselines already outperform those in the original LRA paper (Tay et al., 2020). The BERT training comparison is against Nvidia's MLPerf 1.1 submission on the same initialization and evaluation split, making it a controlled comparison. The Apex FMHA comparison is limited to sequence lengths <= 512 and head dim 64 only, since FMHA does not support longer sequences.

---

## Conclusions

### Contributions

1. **IO-aware attention as a principle.** First to argue that memory access, not FLOPs, is the bottleneck for attention on modern GPUs, and to design an algorithm explicitly optimized for IO complexity rather than computational complexity (Section 1, Section 3.2).

2. **Asymptotically optimal algorithm.** FlashAttention achieves Theta(N^2 d^2 M^{-1}) HBM accesses for both forward and backward passes, and proves this is optimal for exact attention via a matching lower bound (Theorem 2, Proposition 3, Theorem 5).

3. **Practical training speedups.** Demonstrates 2-4x wall-clock speedup on real training tasks (BERT-large 15% faster than MLPerf record, GPT-2 up to 3.5x over HuggingFace, LRA 2.4x) while computing exact attention with identical numerical outputs (Tables 1-3, Figure 4).

4. **Linear memory footprint.** Reduces attention memory from O(N^2) to O(N), enabling sequences up to 64K tokens on a single GPU (Theorem 1, Table 21).

5. **Quality improvements via longer context.** Longer sequences enabled by FlashAttention yield 0.7 better perplexity on GPT-2, 4.3-8.5 points on document classification, and the first Transformer solutions to Path-X (61.4%) and Path-256 (63.1%) (Tables 4-6).

6. **Block-sparse FlashAttention.** Extension to approximate attention that is faster than all known exact, approximate, and sparse attention methods across all tested sequence lengths (Section 3.3, Section 4.3).

### Implications

1. **IO-awareness as a design principle.** The success of FlashAttention suggests that future algorithm design for deep learning should consider memory hierarchy, not just FLOP counts. The "hardware lottery" (Hooker, 2020) -- where theoretically efficient algorithms fail to translate to wall-clock gains -- can be partially overcome by IO-aware design.

2. **Exact vs. approximate attention.** FlashAttention demonstrates that exact attention can be made efficient enough to be competitive with or faster than approximate methods for sequences up to ~1K, and block-sparse FlashAttention dominates all approximate methods even at 64K. This questions the need for attention approximations at moderate sequence lengths (speculative for longer contexts).

3. **Foundation for longer-context training.** By solving the memory bottleneck, FlashAttention opens the path for training with much longer contexts, which subsequent work (FlashAttention-2, Ring Attention, FlashAttention-3) has built upon to reach millions of tokens.

---

## Key Claims

**C1. Attention is memory-bound.** Standard attention runtime is determined by HBM accesses (40.3 GB), not compute (66.6 GFLOPs). FlashAttention reduces HBM accesses to 4.4 GB, achieving 7.3 ms runtime vs 41.7 ms for standard attention despite performing more FLOPs (75.2 vs 66.6 GFLOPs) (Figure 2 left panel table, Section 3.2). **Scope:** A100 GPU, GPT-2 medium configuration (seq 1024, head dim 64, 16 heads, batch 64). **Magnitude:** 5.7x speedup with 9.2x fewer HBM accesses. Status: **supported** (single configuration but strongly validated by runtime correlating with HBM accesses across block sizes in Figure 2 middle panel).

**C2. IO complexity reduction.** Standard attention: Theta(Nd + N^2) HBM accesses. FlashAttention: Theta(N^2 d^2 M^{-1}) HBM accesses (Theorem 2, Section 3.2). **Scope:** Exact attention, SRAM size M with d <= M <= Nd. **Magnitude:** Up to 9x fewer HBM accesses for d=64-128, M ~ 100KB. Status: **supported** (formal proof in Appendix C; validated empirically in Figure 2).

**C3. Optimality.** No exact attention algorithm can achieve o(N^2 d^2 M^{-1}) HBM accesses for all M in [d, Nd] (Proposition 3, Appendix C). **Scope:** Exact (not approximate) attention, all SRAM sizes in the specified range. **Magnitude:** qualitative (matching lower bound). Status: **supported** (formal proof; note the lower bound is over the full range of M -- proving tighter bounds for specific M values is left as future work).

**C4. BERT training speedup.** FlashAttention trains BERT-large to 72% validation accuracy in 17.4 +/- 1.4 minutes vs Nvidia's MLPerf 1.1 record of 20.0 +/- 1.5 minutes (Table 1, Section 4.1). **Scope:** BERT-large (340M params), seq 512, 8xA100-80GB, LAMB optimizer. **Magnitude:** 15% wall-clock speedup (2.6 minutes). Status: **supported** (10 runs with variance reported, controlled comparison against MLPerf submission using same initialization and evaluation split; limited to single model size and single hardware configuration).

**C5. GPT-2 training speedup.** Up to 3.5x speedup over HuggingFace (GPT-2 small: 2.7 vs 9.5 days) and 1.7-2.0x over Megatron-LM (Table 2, Section 4.1). **Scope:** GPT-2 small (117M) and medium (345M), seq 1024, OpenWebText, 8xA100-40GB, 400K steps. **Magnitude:** 3.5x (small) and 3.0x (medium) over HuggingFace; 1.7x (small) and 1.7x (medium) over Megatron-LM. Status: **supported** (2 model sizes, identical perplexity across implementations confirmed by validation curves; limited to 8xA100-40GB configuration).

**C6. Linear memory scaling.** Memory footprint grows linearly with sequence length: 209 MB at N=1024, 836 MB at N=4096, 13376 MB at N=65536, compared to standard attention's 1184 MB, 17024 MB, and OOM respectively (Table 21, Section 4.3). **Scope:** A100-40GB, batch 16, 8 heads, d=64, no dropout/masking (forward+backward). **Magnitude:** Up to 20x more memory-efficient at N=4096; enables sequences up to 64K that standard attention cannot fit. Status: **supported** (comprehensive benchmarking across sequence lengths 128-64K; single hardware/batch configuration).

**C7. First Path-X and Path-256 solutions.** FlashAttention achieves 61.4% on Path-X (16K tokens), block-sparse FlashAttention achieves 56.0% on Path-X and 63.1% on Path-256 (64K tokens), where all prior Transformers and approximate methods achieved random performance or OOM (Table 6, Section 4.2). **Scope:** Path-X (128x128 images), Path-256 (256x256 images), pretrained on Path-64 with positional embedding interpolation, fine-tuned with cosine decay. **Magnitude:** 61.4% vs 50% chance on Path-X; 63.1% vs 50% chance on Path-256. Status: **supported** (single model architecture; comparison against 7 baselines all failing; Path-256 has shorter paths than Path-X despite longer sequences).

**C8. Longer context improves quality.** GPT-2 small with 4K context achieves 0.7 better perplexity than 1K context while training 30% faster than Megatron at 1K (Table 4). Long document classification gains 4.3 F1 on MIMIC-III and 8.5 F1 on ECtHR (Table 5). **Scope:** GPT-2 small only for perplexity; RoBERTa on 2 classification datasets (English medical/legal text). **Magnitude:** 17.5 vs 18.2 perplexity; 57.1 vs 52.8 micro-F1 (MIMIC-III); 80.7 vs 72.2 micro-F1 (ECtHR). Status: **supported** (limited evidence: single model size for perplexity, 2 English-only datasets for classification, non-monotonic improvement at some lengths).

**C9. Benchmarking dominance.** FlashAttention is up to 3x faster than PyTorch attention for sequences up to 2K, and block-sparse FlashAttention is faster than all tested exact, approximate, and sparse attention methods across all sequence lengths 128-64K (Figure 3, Tables 9-20, Section 4.3). **Scope:** A100-40GB, batch 16, 8 heads, d=64, tested with various dropout/masking configurations. **Magnitude:** Up to 3x over PyTorch; block-sparse is 2x-100x+ faster than approximate methods at long sequences. Status: **supported** (comprehensive benchmarking: 4 configurations x 10 sequence lengths x 12 baselines; single GPU type for full benchmark, additional GPU types in Appendix E.5).

---

## Open Questions

1. **Multi-GPU IO-aware methods.** How can the IO-aware approach extend to multi-GPU training with efficient inter-GPU communication, accounting for the additional memory hierarchy level? The current analysis is optimal for single-GPU only (Section 5). Partially addressed by Ring Attention (2024-05-ring-attention-near-infinite-context), which overlaps inter-host communication with blockwise computation.

2. **Compilation from high-level code.** Can attention algorithms be written in PyTorch and automatically compiled to IO-aware CUDA implementations, similar to Halide for image processing (Ragan-Kelley et al., 2013)? This would remove the significant engineering burden of custom CUDA kernels (Section 5).

3. **Scaling to larger models.** How do the benefits of FlashAttention scale to 10B+ parameter models with different attention dynamics and multi-head configurations? The paper evaluates up to 345M parameters only.

4. **GPU utilization improvement.** Can GPU utilization be improved beyond the 25-40% of theoretical maximum FLOPs/s achieved by FlashAttention? Addressed by FlashAttention-2 (2024-05-flashattention-2), which achieves 50-73% utilization through better parallelism and work partitioning.

5. **Dynamic sparsity.** Can the block-sparse extension support content-dependent or learned sparsity patterns rather than requiring fixed patterns determined before training (Section 3.3)?

6. **IO-aware deep learning beyond attention.** Can the IO-aware approach extend to other memory-intensive deep learning operations beyond attention, such as sparse MLP layers and kernel methods (Appendix D.2)?

---

## Core References and Why They Are Referenced

### Hardware and IO Complexity Foundations

- **Aggarwal & Vitter (1988)** -- *The Input/Output Complexity of Sorting.* Foundational work on IO complexity analysis that FlashAttention's theoretical framework builds upon directly.
- **Williams et al. (2009)** -- *Roofline: An Insightful Visual Performance Model.* Introduces arithmetic intensity as the key metric for distinguishing compute-bound from memory-bound operations, central to FlashAttention's argument.
- **Ivanov et al. (2021)** -- *Data Movement Is All You Need.* Shows that most Transformer operations are bottlenecked by memory accesses, directly motivating FlashAttention.
- **Milakov & Gimelshein (2018)** -- *Online Normalizer Calculation for Softmax.* Technique for computing softmax incrementally that FlashAttention's tiling approach builds upon.

### Transformer and Attention

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture and standard attention mechanism that FlashAttention optimizes.
- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers.* BERT-large is a key benchmark: FlashAttention beats the MLPerf training speed record.
- **Radford et al. (2019)** -- *Language Models Are Unsupervised Multitask Learners (GPT-2).* GPT-2 small/medium are key benchmarks for training speedup and quality evaluation.

### Efficient Attention Methods (Baselines)

- **Kitaev et al. (2020)** -- *Reformer: The Efficient Transformer.* Sparse attention via locality-sensitive hashing; used as baseline in LRA and Path-X experiments.
- **Choromanski et al. (2020)** -- *Rethinking Attention with Performers.* Low-rank attention approximation; used as baseline in LRA and Path-X experiments.
- **Wang et al. (2020)** -- *Linformer: Self-Attention with Linear Complexity.* Low-rank projection of keys and values; key baseline in LRA, Path-X, and runtime benchmarks.
- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Sparse attention with local+global patterns; baseline in benchmarking and source of positional embedding repetition technique.
- **Zaheer et al. (2020)** -- *Big Bird: Transformers for Longer Sequences.* Combines sparse attention patterns; baseline in benchmarking.
- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Block-sparse attention; inspiration for block-sparse FlashAttention and source of sparsity ratio s = N^{-1/2}.

### Memory-Efficient Attention

- **Rabe & Staats (2021)** -- *Self-Attention Does Not Need O(n^2) Memory.* Shows attention can be computed with O(n) memory using tiling/recomputation. FlashAttention builds on this but focuses on reducing IO (achieving 2-4x speedup) rather than just memory reduction (roughly same speed as standard attention). Three key differences described in Appendix B.5.

### Benchmarks and Training Infrastructure

- **Tay et al. (2020)** -- *Long Range Arena: A Benchmark for Efficient Transformers.* Provides the LRA benchmark including Path-X; used for accuracy and speed comparison.
- **Mattson et al. (2020)** -- *MLPerf Training Benchmark.* BERT training benchmark whose speed record FlashAttention beats by 15%.
- **Liu et al. (2019)** -- *RoBERTa: A Robustly Optimized BERT Pretraining Approach.* Pretrained model used as backbone for long document classification experiments.
- **Shoeybi et al. (2019)** -- *Megatron-LM.* Training infrastructure baseline for GPT-2 experiments; also provides fused softmax+masking optimization.

### Structured Matrices and Sparsity

- **Dao et al. (2022)** -- *Pixelated Butterfly.* Provides the fixed butterfly sparsity pattern used in block-sparse FlashAttention experiments.
- **Dao et al. (2020)** -- *Kaleidoscope.* Proves butterfly matrices can approximate arbitrary structured matrices, justifying the choice of butterfly sparsity.
