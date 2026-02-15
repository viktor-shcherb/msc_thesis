---
title: "LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens"
authors: "Ding, Zhang, Zhang, Xu, Shang, Xu, Yang, Yang"
year: 2024
venue: "ICML 2024"
paper_type: conference-paper
categories: ["context-extension", "position-encoding"]
scope: ["RoPE-based LLMs", "context window extension", "positional encoding interpolation", "non-uniform rescaling"]
benchmarks_used: ["perplexity-pg19", "perplexity-proofpile", "perplexity-books", "passkey-retrieval", "arc", "hellaswag", "mmlu", "truthfulqa"]
models_introduced: []
models_evaluated: ["llama-2-7b", "mistral-7b"]
key_claims:
  - id: C1
    claim: "LongRoPE extends context windows to 2048k tokens with only 1k fine-tuning steps at within 256k training lengths, achieving an 8x extension beyond fine-tuning length without additional training"
    evidence: "Section 3.3, Section 4.1-4.2, Table 6"
    status: supported
    scope: "LLaMA2-7B and Mistral-7B, RoPE-based models, 256k fine-tuning length"
    magnitude: "512x total extension (4k to 2048k); 8x beyond fine-tuning length; ~1000 fine-tuning steps"
  - id: C2
    claim: "Non-uniform positional interpolation with evolutionary search discovers rescale factors that outperform PI, NTK, and YaRN baselines in perplexity for non-fine-tuned extensions"
    evidence: "Section 2.2, Table 1, Section 3.2, Figure 3"
    status: supported
    scope: "LLaMA2-7B, 8k-32k non-fine-tuned extensions, PG19 and Proof-pile evaluation"
    magnitude: "PG19 8k: 9.37 vs 10.21 (Dy-NTK) and 10.65 (PI); PG19 16k: 11.34 vs 20.49 (PI)"
  - id: C3
    claim: "Progressive extension strategy (pretrained -> 256k -> 2048k via secondary search) is more effective than direct extension to very long contexts"
    evidence: "Section 3.3, Section 4.3, Table 9"
    status: supported
    scope: "LLaMA2-7B fine-tuned to 256k, secondary extension to 512k-2048k on Books3"
    magnitude: "Books3 2048k perplexity: LongRoPE 7.08 vs YaRN 8.27 vs PI 20.17"
  - id: C4
    claim: "LongRoPE-LLaMA2-7B maintains high passkey retrieval accuracy from 4k to 2048k tokens"
    evidence: "Section 4.2, Figure 4"
    status: supported
    scope: "LLaMA2-7B fine-tuned at 256k, synthetic passkey retrieval task, 10 iterations per length"
    magnitude: ">=90% accuracy from 4k to 2048k for LLaMA2; Mistral 100% to 1800k, drops to 60% at 2048k"
  - id: C5
    claim: "Short-context recovery via additional RoPE factor search restores original context window performance while maintaining extended context capabilities"
    evidence: "Section 3.3, Section 4.3, Table 10"
    status: supported
    scope: "LLaMA2-7B-2048k models, Proof-pile 4k/8k evaluation, Open LLM Leaderboard benchmarks"
    magnitude: "ft=128k recovery: Proof-pile 4k from 4.16 to 3.71, benchmark avg from 49.3 to 52.9"
  - id: C6
    claim: "LongRoPE-extended models maintain comparable performance on standard benchmarks at 4096 context despite 512x extension ratio"
    evidence: "Section 4.3, Table 8"
    status: supported
    scope: "LLaMA2-7B and Mistral-7B at 4096 context, ARC-c/HellaSwag/MMLU/TruthfulQA benchmarks"
    magnitude: "LLaMA2 ft=128k: ARC-c 52.9 (vs 53.1 orig), MMLU 43.4 (vs 46.6); Mistral ft=128k: all metrics within 2.3 points"
  - id: C7
    claim: "RoPE dimension non-uniformity is the primary contributor to performance gains, while token position non-uniformity provides additional but diminishing benefit at extreme lengths"
    evidence: "Section 4.3, Table 11"
    status: supported
    scope: "LLaMA2-7B non-fine-tuned 16k/32k and fine-tuned 256k extended to 2048k, PG19 and Books3"
    magnitude: "16k PG19: RoPE dim reduces PI 14.88 to 7.28; adding start tokens further to 7.22; at 2048k both give 7.08"
cross_references:
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "LongRoPE builds on YaRN's frequency-aware interpolation by discovering non-uniform rescale factors via evolutionary search rather than using fixed NTK-by-parts formulas with predetermined alpha/beta parameters"
  - target: 2023-06-pi-positional-interpolation
    type: extends
    detail: "LongRoPE improves on PI's uniform linear interpolation by discovering non-uniform dimension-wise and position-wise rescaling factors, and achieves 8x non-fine-tuning extension vs PI's ~2x"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "LongRoPE modifies RoPE's per-dimension frequencies via learned non-uniform rescale factors rather than the original fixed theta_d = 10000^(-2d/|D|) values"
  - target: 2025-03-survey-transformer-context-extension
    type: complementary
    detail: "Survey taxonomizes LongRoPE under base frequency adjustment subcategory of positional encoding approaches for context extension"
  - target: 2024-05-pose-positional-skip-wise-training
    type: extends
    detail: "LongRoPE continues PoSE's train-short context-extension direction and pushes the practical range from 128k toward multi-million-token contexts"
open_questions:
  - question: "Can the evolutionary search be replaced with a principled analytical formula for optimal rescale factors?"
    addressed_by: null
  - question: "Does the progressive extension strategy and 8x non-fine-tuning ratio generalize to other architectures beyond LLaMA2 and Mistral?"
    addressed_by: null
  - question: "What is the optimal trade-off between search cost and extension quality at extreme context lengths?"
    addressed_by: null
  - question: "Why does Mistral degrade more than LLaMA2 at very long contexts (>256k) despite similar architecture?"
    addressed_by: null
  - question: "Can token position non-uniformity be made effective at extreme lengths (>2048k), given that it shows no benefit at 2048k?"
    addressed_by: null
---
# LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens

**Authors:** Yiran Ding (Hangzhou Dianzi University, intern at Microsoft Research), Li Lyna Zhang, Chengruidong Zhang, Yuanyuan Xu (University of Science and Technology of China), Ning Shang, Jiahang Xu, Fan Yang, Mao Yang (Microsoft Research)
**Date:** February 2024, arXiv:2402.13753; published at ICML 2024
**Code:** https://github.com/microsoft/LongRoPE

---

## Core Research Problem

Large context windows enable applications such as long document understanding, multi-turn conversations, and in-context learning with many examples. However, extending context windows of pretrained LLMs faces three core obstacles (Section 1): (1) **untrained new position indices** introduce catastrophic out-of-distribution values -- extending from 4k to >1000k introduces more than 90% new positions, making fine-tuning difficult to converge; (2) **fine-tuning requires corresponding-length texts**, and long texts exceeding 1000k tokens are scarce, while training on such lengths is prohibitively expensive in GPU resources; (3) **attention becomes dispersed** across extremely many positions, degrading performance on the original short context.

Prior methods address the first obstacle through positional interpolation. Position Interpolation (Chen et al., 2023a) -- *Extending Context Window via Positional Interpolation* -- linearly downscales all RoPE rotation angles by the extension ratio s, but this makes position information "crowded," hindering distinction between closely positioned tokens, and limits effective extension to ~128k (Section 2.1). NTK-aware scaling (LocalLLaMA, 2023) distributes interpolation pressure across RoPE dimensions -- less interpolation for lower dimensions (higher frequencies), more for higher dimensions -- but achieves at most 4x extension without fine-tuning. YaRN (Peng et al., 2023) -- *Efficient Context Window Extension* -- categorizes RoPE dimensions into three frequency-based groups with different interpolation strategies, but relies on human-designed grouping rules with predetermined alpha/beta parameters that may be sub-optimal for new models.

The core challenge is: **how to extend context windows to millions of tokens while minimizing fine-tuning costs, maintaining short-context performance, and achieving effective utilization of the extended context.**

---

## Problem Solutions

LongRoPE introduces three key innovations that together enable 2048k token context windows:

1. **Non-uniform positional interpolation via evolutionary search.** Rather than using uniform or fixed frequency-dependent interpolation, LongRoPE discovers two forms of non-uniformity: (a) varying RoPE dimensions require different rescale factors, and (b) initial token positions benefit from no interpolation. An evolutionary search algorithm efficiently finds per-dimension rescale factors and a starting-token threshold that minimize perplexity at the target length.

2. **Progressive extension strategy.** Instead of directly fine-tuning to 2048k tokens, LongRoPE first searches and fine-tunes to 256k, then performs a second search on the fine-tuned model to reach 2048k without additional training. This exploits the observation that searched rescale factors enable approximately 8x extension beyond the fine-tuning length.

3. **Short-context recovery.** Extended models suffer performance degradation at original context lengths due to positional crowding. LongRoPE performs an additional evolutionary search to find RoPE factors optimized for short contexts (4k-8k), then dynamically selects appropriate factors during inference based on input length.

---

## Approach Details

### Method

LongRoPE formulates context extension as a search problem over RoPE rescale factors (Section 3.1). For a model pretrained with context length L and target extension to L' = s * L, the method searches for per-dimension rescale factors lambda_i and a starting token threshold n_hat. The modified RoPE embedding is defined by the indicator function:

> RoPE_i(n) = [..., cos(I(lambda_i, n_hat) * n / beta^i), sin(I(lambda_i, n_hat) * n / beta^i), ...]
>
> where I(lambda_i, n_hat) = 1 if n < n_hat; 1/lambda_i if n >= n_hat
>
> (Equation 3)

Here beta = theta^(2/d) with theta = 10000, i = 0, ..., d/2 - 1, and n is the token position index. For positions below the threshold n_hat, original RoPE values are preserved (no interpolation). For positions at or above n_hat, the rescale factor lambda_i is applied per-dimension. The optimization objective is to minimize perplexity on input samples of length L'.

### Key Technical Components

**Non-uniform dimension rescaling (Finding 1, Section 2.2).** The evolutionary search reveals that RoPE dimensions exhibit substantial non-uniformities not captured by existing methods. Table 1 (Section 2.2) demonstrates this on LLaMA2-7B without fine-tuning:

| Extension Method | PG19 8192 | PG19 16384 | Proof-pile 8192 | Proof-pile 16384 |
|---|---|---|---|---|
| PI | 10.65 | 20.49 | 3.65 | 4.93 |
| Dy-NTK | 10.21 | 23.29 | 3.50 | 3.87 |
| YaRN | 32.64 | 87.89 | 3.49 | 3.25 |
| **Search (Dim-wise lambda)** | **9.37** | **11.34** | **3.45** | **3.13** |

The searched solution significantly outperforms all baselines. Notably, YaRN underperforms PI on PG19 at these lengths because it does not reach the target context window length for non-fine-tuned LLMs (Section 2.2).

**Non-uniform position rescaling (Finding 2, Section 2.2).** Retaining the first n_hat tokens without positional interpolation improves performance. Table 2 (Section 2.2) shows this on LLaMA2-7B for PI at 8k context: perplexity drops from 10.65 (n_hat=0) to **10.49** (n_hat=64). For Dy-NTK at 8k: from 10.21 to **10.13** (n_hat=128). The optimal n_hat depends on the target extension length -- this is consistent with Streaming LLM (Xiao et al., 2023) and LM-Infinite (Han et al., 2023), which observe that initial tokens receive large attention scores.

**Combined non-uniform interpolation (Finding 3, Section 2.2).** Table 3 (Section 2.2) shows Proof-pile perplexity for LLaMA2-7B extended to 64k:

| Method | Non-fine-tuned | Fine-tuned |
|---|---|---|
| PI | 72.54 | 2.44 |
| YaRN | 4.15 | 2.42 |
| **Search (Dim-wise lambda and n_hat)** | **3.22** | **2.36** |

The searched method outperforms both PI and YaRN in both settings, providing better initialization for fine-tuning.

**Evolutionary search algorithm (Section 3.2).** The search space (Table 4) for lambda_i ranges from 1.0 to s * 1.25 with step size 0.01, and n_hat from {0, 1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 64, 128, 256}. The algorithm (Algorithm 1) uses:
- Population size P = 64
- Mutation size N_1 = 16, crossover size N_2 = 16
- Mutation probability p = 0.3
- Max iterations T = 40
- Top-32 individuals selected for mutation/crossover each iteration
- Fitness function: perplexity on 5 random PG19 validation samples (for targets <= 256k) or 3 random Pile-Books3 samples (for targets > 512k)
- Population and mutation/crossover sizes halved for windows over 512k

The initial population is seeded with PI, NTK, and YaRN solutions; remaining P-3 individuals are random mutations of these three (Section 3.2). A **monotonically non-decreasing constraint** (lambda_i <= lambda_{i+1}) is enforced, based on NTK theory that lower dimensions (higher frequency) require less interpolation (Section 3.2).

**Progressive extension (Section 3.3).** Three steps:
1. **Search for 128k and 256k** rescale factors on the pretrained LLM (32x and 64x extension ratios)
2. **Fine-tune to 256k:** First 400 steps at 128k, then swap to 256k factors and 600 additional steps
3. **Search for 2048k** on the fine-tuned 256k model (8x secondary extension) -- no additional fine-tuning needed

This progressive approach is more effective than direct fine-tuning to 256k from scratch (Section A.2, Table 12, Figure 5c).

**Short-context recovery (Section 3.3).** An extra evolution search is performed on the extended LLM with reduced maximum lambda values to find factors optimized for 4k and 8k contexts. During inference, the LLM dynamically switches RoPE factors based on input sequence length (if length < 8k, use short-context factors; otherwise, use long-context factors).

### Experimental Setup

**Models.** LLaMA2-7B (Touvron et al., 2023) and Mistral-7B v0.1 (Jiang et al., 2023), both using RoPE positional encoding with base theta = 10000.

**Fine-tuning (LLaMA2, Section 4.1 and A.2):**
- 128k extension: 400 steps on 8 A100 GPUs, learning rate 2e-5 with linear decay, global batch size 32
- 256k extension: 600 additional steps on 16 A100 GPUs, starting from 128k checkpoint
- Dataset: RedPajama (Computer, 2023), segments chunked into 128k bookended with BOS/EOS tokens
- Total fine-tuning cost: 8 A100s for 1 week (128k) + 16 A100s for 2 weeks (256k)

**Fine-tuning (Mistral, Section 4.1 and A.2):**
- Both 128k and 256k: 400 steps on 4 A100 GPUs, constant learning rate 1e-6, global batch size 64
- Training sequence length: 16k (following YaRN methodology)
- Dataset: Together Computer's Long-Data Collections
- Total fine-tuning cost: 4 A100s for 2 days

**Search costs (Section A.3):**
- Up to 256k: approximately 3 days on a single A100
- 512k: 2 A100 GPUs
- 1024k-2048k: 4-8 A100 GPUs, within a 5-day limit
- Per-evaluation at 2048k: approximately 50 minutes

**Infrastructure:** All experiments on 16 A100 GPUs with Flash Attention-2 (Dao, 2023) for acceleration. CUBE distributed training system (Lin et al., 2023) used for contexts beyond 512k (Section A.1).

**Evaluation:**
1. **Perplexity** on Proof-pile (Rae et al., 2019) at 4k-262k, PG19 at 8k-128k, and Books3 (Gao et al., 2020) at 8k-2048k with sliding windows (256 tokens for most, 256k for Books3)
2. **Passkey retrieval** (Mohtashami & Jaggi, 2023) at 4k-2048k, 10 iterations per length, passkey at random location
3. **Standard benchmarks** at 4096 context: ARC-Challenge (25-shot), HellaSwag (10-shot), MMLU (5-shot), TruthfulQA (0-shot) via Hugging Face Open LLM Leaderboard

**Baselines:** Together-32k (PI), Code LLaMA-100k (NTK), LongLoRA-full-FT-100k (PI), YaRN-LLaMA s=16 (64k), YaRN-LLaMA s=32 (128k), YaRN-Mistral s=8 (64k), YaRN-Mistral s=16 (128k), MistralLite (Amazon, 2023).

**Reproducibility:** Code released at https://github.com/microsoft/LongRoPE. Search uses random PG19/Books3 samples (no fixed seeds reported). Fine-tuning hyperparameters fully specified. Hardware requirements are substantial (8-16 A100 GPUs).

### Key Results

**Proof-pile perplexity within 256k (Table 5, Section 4.2):**

| Base LLM | Model | Context Window | 4096 | 8192 | 32768 | 65536 | 98304 | 131072 | 262144 |
|---|---|---|---|---|---|---|---|---|---|
| LLaMA2-7B | Together | 32k | 3.69 | 3.50 | 2.64 | >10^2 | >10^3 | >10^4 | >10^4 |
| LLaMA2-7B | LongLoRA | 100k | 3.83 | 3.62 | 2.68 | 2.44 | 2.33 | 9.89 | >10^3 |
| LLaMA2-7B | Code LLaMA | 100k | 3.95 | 3.71 | 2.74 | 2.55 | 2.54 | 2.71 | 49.33 |
| LLaMA2-7B | YaRN (s=32) | 128k | 3.75 | 3.56 | 2.70 | 2.45 | 2.36 | 2.37 | 99.64 |
| LLaMA2-7B | **LongRoPE-2048k (ft=128k)** | 2048k | 3.71 | 3.50 | 2.60 | 2.36 | 2.27 | 2.26 | 1.88 |
| LLaMA2-7B | **LongRoPE-2048k (ft=256k)** | 2048k | 3.85 | 3.65 | 2.63 | 2.38 | 2.28 | 2.26 | 1.87 |
| Mistral-7B | YaRN (s=16) | 128k | 3.21 | 3.08 | 2.41 | 2.24 | 2.18 | 2.19 | 4.91 |
| Mistral-7B | **LongRoPE-2048k (ft=128k)** | 2048k | 3.20 | 3.04 | 2.36 | 2.18 | 2.13 | 2.13 | 1.85 |
| Mistral-7B | **LongRoPE-2048k (ft=256k)** | 2048k | 3.20 | 3.04 | 2.36 | 2.18 | 2.13 | 2.14 | 1.84 |

- Even with a context window 16x longer than baselines, LongRoPE models outperform or match baselines within 256k (tested across 2 models and 2 evaluation sets -- moderate evidence)
- Perplexity continues to decrease with longer contexts up to 262k, demonstrating genuine long-context utilization

**Books3 perplexity at extreme lengths (Table 6, Section 4.2):**

| Base LLM | Model | Context Window | 8k | 16k | 32k | 64k | 128k | 256k | 512k | 1024k | 2048k |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LLaMA2-7B | LongLoRA | 100k | 6.99 | 6.80 | 6.66 | 6.59 | 20.57 | 246.45 | >10^5 | >10^4 | >10^4 |
| LLaMA2-7B | YaRN (s=16) | 64k | **6.33** | **6.20** | **6.11** | **6.06** | >10^4 | >10^4 | >10^4 | >10^4 | >10^4 |
| LLaMA2-7B | YaRN (s=32) | 128k | 6.38 | 6.25 | 6.16 | 6.11 | 6.12 | >10^4 | >10^4 | >10^4 | >10^4 |
| LLaMA2-7B | **LongRoPE-2048k (ft=128k)** | 2048k | 6.55 | 6.35 | 6.24 | 6.18 | 6.17 | 6.17 | 6.36 | 6.83 | 7.80 |
| LLaMA2-7B | **LongRoPE-2048k (ft=256k)** | 2048k | 6.81 | 6.66 | 6.31 | 6.27 | 6.21 | 6.17 | 6.17 | 6.35 | 7.08 |
| Mistral-7B | YaRN (s=16) | 64k | **6.59** | **6.48** | **6.42** | **6.45** | 104.15 | 7221.20 | >10^3 | >10^4 | >10^4 |
| Mistral-7B | YaRN (s=32) | 128k | 6.70 | 6.63 | 6.65 | 6.72 | 6.85 | 99.90 | >10^3 | >10^4 | >10^4 |
| Mistral-7B | **LongRoPE-2048k (ft=128k)** | 2048k | 6.64 | 6.48 | 6.39 | 6.45 | 6.64 | 7.08 | 7.71 | 8.93 | 12.78 |
| Mistral-7B | **LongRoPE-2048k (ft=256k)** | 2048k | 6.63 | 6.48 | 6.38 | 6.43 | 6.68 | 7.15 | 7.98 | 9.42 | 13.71 |

- LongRoPE-LLaMA2 (ft=256k) maintains 7.08 perplexity at 2048k -- reasonable given the 512x extension (tested on 20 books exceeding 2048k, 256k sliding window)
- LongRoPE-LLaMA2 (ft=128k) achieves 7.80 at 2048k (16x secondary extension vs 8x for ft=256k)
- Mistral degrades more severely: perplexity exceeds 7 beyond 256k, reaching 12.78-13.71 at 2048k. The paper attributes this partly to Mistral's 16k training length (following YaRN methodology), which limits further extension capability
- YaRN baselines catastrophically spike beyond their fine-tuning length (>10^4 perplexity)

**Passkey retrieval (Figure 4, Section 4.2):**

- **LongRoPE-LLaMA2-2048k (ft=256k):** maintains >=90% retrieval accuracy from 4k to 2048k (10 iterations per length, passkey at random location)
- **LongRoPE-Mistral-2048k (ft=128k):** 100% accuracy up to 1800k, drops to ~60% at 2048k
- All baselines (LongLoRA, Code LLaMA, YaRN variants) drop to 0% accuracy beyond 128k
- Evidence is moderate: synthetic task only, 10 iterations per evaluation length, single passkey

**Short-context benchmark performance (Table 8, Section 4.3, 4096 context):**

**(a) LLaMA2-7B:**

| Model | Context Window | ARC-c | HellaSwag | MMLU | TruthfulQA |
|---|---|---|---|---|---|
| Original LLaMA2-7B | 4k | 53.1 | 78.6 | 46.6 | 39.0 |
| Together | 32k | 47.6 | 76.1 | 43.3 | 39.2 |
| Code LLaMA | 100k | 42.4 | 64.8 | 40.1 | 37.1 |
| YaRN (s=16) | 64k | 52.4 | **78.7** | 42.4 | 38.2 |
| YaRN (s=32) | 128k | 52.2 | 78.5 | 41.8 | 37.4 |
| **LongRoPE-2048k (ft=128k)** | 2048k | **52.9** | 76.5 | **43.4** | **38.8** |
| LongRoPE-2048k (ft=256k) | 2048k | 51.0 | 75.3 | 39.6 | 37.3 |

**(b) Mistral-7B:**

| Model | Context Window | ARC-c | HellaSwag | MMLU | TruthfulQA |
|---|---|---|---|---|---|
| Original Mistral-7B | 8k | 60.6 | 83.2 | 63.6 | 42.6 |
| MistralLite | 16k | 59.2 | **81.6** | 50.4 | 38.3 |
| YaRN (s=16) | 64k | **59.3** | 81.3 | 61.3 | 42.5 |
| YaRN (s=32) | 128k | 59.0 | 80.5 | 60.5 | 42.1 |
| **LongRoPE-2048k (ft=128k)** | 2048k | 59.0 | 81.2 | **61.3** | **43.1** |
| LongRoPE-2048k (ft=256k) | 2048k | 59.2 | 80.9 | 61.1 | 42.2 |

- LongRoPE-LLaMA2 (ft=128k) with short-context recovery: ARC-c drops only 0.2 points, HellaSwag drops 2.1, MMLU drops 3.2, TruthfulQA drops 0.2 vs original
- LongRoPE-Mistral (ft=128k) maintains or slightly improves most metrics; TruthfulQA +0.5% over original
- The ft=256k variants show slightly more degradation (tested on 4 benchmarks at single context length -- limited evidence for short-context claim generalization)

### Ablation Studies

**Effectiveness of secondary positional interpolation (Table 9, Section 4.3):**

| Model (ft=256k) | Extension Method | 512k | 1024k | 2048k |
|---|---|---|---|---|
| LLaMA2-7B | PI | 6.60 | 8.73 | 20.17 |
| LLaMA2-7B | YaRN | 6.39 | 6.79 | 8.27 |
| LLaMA2-7B | **LongRoPE** | **6.17** | **6.35** | **7.08** |

LongRoPE's non-uniform interpolation sustains consistent perplexity across 512k-2048k, while PI and YaRN degrade rapidly with extension ratio (single model -- limited evidence).

**Short-context recovery effectiveness (Table 10, Section 4.3):**

| FT Model | With Recovery | Proof-Pile PPL 4k | Proof-Pile PPL 8k | LLM Benchmark Avg. |
|---|---|---|---|---|
| LLaMA2-7B-2048k (ft=128k) | No | 4.16 | 3.72 | 49.3 |
| LLaMA2-7B-2048k (ft=128k) | **Yes** | **3.71** | **3.50** | **52.9** |
| LLaMA2-7B-2048k (ft=256k) | No | 4.51 | 3.82 | 47.9 |
| LLaMA2-7B-2048k (ft=256k) | **Yes** | **3.85** | **3.65** | **50.8** |

Recovery search brings substantial improvements: 3.6 point average benchmark improvement for ft=128k, 2.9 for ft=256k (LLaMA2 only -- limited evidence for generalization to other models).

**Ablation on two forms of non-uniformities (Table 11, Section 4.3):**

| Methods | LLaMA2 PG19 16k | LLaMA2 PG19 32k | LLaMA2 (ft=256k) Books3 2048k |
|---|---|---|---|
| Linear interpolation (PI) | 14.88 | 136.30 | 20.17 |
| RoPE dim (Ours) | 7.28 | 13.00 | 7.08 |
| RoPE dim + Start tokens (Ours) | **7.22** | **11.51** | **7.08** |

- RoPE dimension non-uniformity is the dominant contributor: reduces PI 14.88 to 7.28 at 16k
- Token position non-uniformity provides additional benefit at shorter lengths (7.28 to 7.22 at 16k, 13.00 to 11.51 at 32k) but **no additional benefit at 2048k** (both 7.08), possibly because preserving only initial tokens is insufficient at extreme lengths
- The authors leave the diminishing token-position effect at extreme lengths as future work

### Search Convergence

Figure 6 (Section A.3) shows that the search efficiently finds high-quality factors. For 256k search (64x extension), after just 1 iteration, solutions significantly better than PI and YaRN are found, with validation perplexity reducing from 273.27 to 118.47 over iterations. Notably, **YaRN performs worse than PI (linear interpolation) at 64x extension** in non-fine-tuned settings, indicating that human-heuristic-based non-uniform interpolation is challenging at high ratios. For 2048k search, search iterations are constrained by the ~50 minute per-evaluation cost; better results are likely achievable with more search time (Section A.3).

---

## Limitations and Failure Modes

1. **Perplexity degradation at extreme lengths.** LLaMA2-LongRoPE (ft=256k) perplexity increases from 6.17 at 256k to 7.08 at 2048k on Books3 (Table 6). Mistral degrades more severely: from 7.08 at 256k to 12.78 at 2048k for ft=128k, and from 7.15 to 13.71 for ft=256k. The paper does not analyze the root cause of this degradation beyond noting the large extension ratio.

2. **Model-dependent effectiveness.** Mistral shows substantially worse long-context performance than LLaMA2 at >256k despite similar architecture. The paper attributes this partly to Mistral's 16k training length (following YaRN methodology), but does not conduct a controlled comparison isolating this factor (Section 4.2).

3. **Computationally expensive search.** Finding optimal rescale factors for 2048k requires up to 5 days on 8 A100 GPUs, with each fitness evaluation taking approximately 50 minutes (Section A.3). Search iterations are constrained by this cost, meaning results may be suboptimal.

4. **Token position non-uniformity ineffective at extreme lengths.** The ablation (Table 11) shows that the n_hat starting token mechanism provides no additional benefit at 2048k (both variants yield 7.08). The authors acknowledge this and leave it as future work.

5. **[Inferred]** **No downstream task evaluation at extended lengths.** Evaluation at 2048k is limited to perplexity and passkey retrieval (a synthetic task). Complex reasoning, information synthesis, or multi-document QA at extreme lengths are not evaluated.

6. **[Inferred]** **Limited model coverage.** Only evaluated on LLaMA2-7B and Mistral-7B; scaling behavior to larger models (13B, 70B) or different architectures is unknown.

7. **[Inferred]** **No variance estimates.** Perplexity and passkey results are reported without confidence intervals or standard deviations across runs, despite the stochastic nature of the search algorithm and random evaluation sample selection.

#### Scope and Comparability

- **What was not tested:** Models larger than 7B; non-RoPE architectures; downstream tasks requiring reasoning over long contexts (e.g., multi-hop QA, summarization); non-English text; the effect of different base theta values.
- **Comparability notes:** The Mistral fine-tuning uses 16k training length (following YaRN), while LLaMA2 uses the full target context length. This makes direct comparison between the two models' extension quality difficult. Different baselines use different fine-tuning budgets and datasets, complicating cross-method comparison. The Books3 evaluation uses a 256k sliding window while Proof-pile uses 256-token windows -- perplexity values are not directly comparable across these two evaluations. YaRN baselines in the paper are the open-sourced versions, which may differ from reproductions with different hyperparameters.

---

## Conclusions

### Contributions

1. **Discovery of two non-uniformities in positional interpolation.** Empirically demonstrated that RoPE dimensions and initial token positions require non-uniform treatment, and that evolutionary search can efficiently discover per-dimension rescale factors that outperform fixed formulas including PI, NTK, and YaRN (Section 2.2, Tables 1-3, Figure 3).

2. **Progressive extension strategy.** Introduced a two-stage approach (256k fine-tune then 2048k search) that exploits the 8x non-fine-tuning extension capability, enabling 2048k context with only ~1000 fine-tuning steps at within 256k training length (Section 3.3, Tables 6, 9).

3. **Short-context recovery mechanism.** Developed a method to maintain original context window performance through separate RoPE factor search and dynamic factor selection at inference time, recovering up to 3.6 points of average benchmark accuracy (Section 3.3, Table 10).

4. **First 2048k context extension.** Achieved the first published extension of LLM context windows to 2048k tokens while maintaining reasonable perplexity (7.08 on LLaMA2) and >=90% passkey retrieval accuracy (Section 4.2, Table 6, Figure 4).

5. **Compute-efficient extension.** Extended context by 512x (4k to 2048k) with only ~1000 fine-tuning steps at 256k training length, compared to prior methods that required fine-tuning at or near the target length (Section 3.3, 4.1).

### Implications

1. **Learned rescale factors outperform fixed formulas.** The success of evolutionary search over human-designed rules (YaRN performing worse than PI at 64x extension, Section A.3) suggests that optimal context extension parameters are model-specific and length-dependent, favoring learned over hand-designed approaches.

2. **Progressive extension enables extreme lengths.** The 8x non-fine-tuning extension capability suggests that context extension methods need not be trained at the final target length, significantly reducing compute requirements (speculative: the 8x ratio may not hold for all models or extension regimes).

3. **Short-context performance is recoverable.** The recovery mechanism demonstrates that extended models can dynamically adapt their positional encoding behavior based on input length, potentially enabling a single model checkpoint to handle diverse context requirements (speculative: not tested beyond LLaMA2).

---

## Key Claims

**C1. LongRoPE extends context windows to 2048k tokens with only ~1000 fine-tuning steps at within 256k training lengths.** The progressive extension strategy fine-tunes LLaMA2 in 400+600 steps and Mistral in 400 steps, then searches for 2048k factors without additional fine-tuning, achieving 8x extension beyond fine-tuning length. Books3 perplexity at 2048k: 7.08 for LLaMA2 ft=256k, 7.80 for ft=128k (Table 6, Section 4.2). Scope: LLaMA2-7B and Mistral-7B only. Magnitude: 512x total extension, ~1000 steps. Status: **supported** (tested on 2 models -- limited model diversity).

**C2. Non-uniform positional interpolation discovers rescale factors that outperform PI, NTK, and YaRN baselines.** On LLaMA2-7B without fine-tuning, searched dim-wise lambda achieves PG19 8192 perplexity of 9.37 vs 10.65 (PI), 10.21 (Dy-NTK), 32.64 (YaRN); PG19 16384: 11.34 vs 20.49 (PI) (Table 1, Section 2.2). With fine-tuning at 64k: Proof-pile 2.36 vs 2.44 (PI), 2.42 (YaRN) (Table 3). Scope: LLaMA2-7B, 8k-64k extensions, PG19 and Proof-pile. Magnitude: up to 2.0x improvement over PI at 16k. Status: **supported** (single model, two datasets -- moderate evidence).

**C3. Progressive extension is more effective than direct extension.** On the fine-tuned LLaMA2-256k model extended to 2048k via secondary search: LongRoPE achieves 7.08 Books3 perplexity vs YaRN's 8.27 and PI's 20.17 (Table 9, Section 4.3). Additionally, fine-tuning from 128k checkpoint to 256k is more effective than direct 256k fine-tuning: Proof-pile 262k perplexity 1.87 vs 1.95 (Table 12, Section A.2). Scope: LLaMA2-7B ft=256k, Books3 evaluation. Magnitude: LongRoPE 7.08 vs PI 20.17 at 2048k. Status: **supported** (single model -- limited evidence).

**C4. LongRoPE-LLaMA2-7B maintains high passkey retrieval accuracy from 4k to 2048k tokens.** LongRoPE-LLaMA2-2048k (ft=256k) achieves >=90% accuracy from 4k to 2048k; Mistral maintains 100% to 1800k, drops to ~60% at 2048k (Figure 4, Section 4.2). All baselines drop to 0% beyond 128k. Scope: Synthetic passkey retrieval task, 10 iterations per length, two 7B models. Magnitude: >=90% accuracy maintained across 512x extension range for LLaMA2. Status: **supported** for LLaMA2; partially supported for Mistral (60% at 2048k).

**C5. Short-context recovery restores original context window performance.** Additional search for short-context RoPE factors recovers Proof-pile 4k perplexity from 4.16 to 3.71 and average benchmark accuracy from 49.3% to 52.9% for ft=128k (Table 10, Section 4.3). Scope: LLaMA2-7B-2048k, Proof-pile and 4 benchmarks at 4k context. Magnitude: 3.6 percentage point benchmark improvement, 0.45 perplexity improvement at 4k. Status: **supported** (LLaMA2 only, no Mistral ablation -- limited evidence for generalization).

**C6. LongRoPE-extended models maintain comparable performance on standard benchmarks at 4096 context.** At 4096 context, LLaMA2-LongRoPE ft=128k achieves ARC-c 52.9 (vs 53.1 original), HellaSwag 76.5 (vs 78.6), MMLU 43.4 (vs 46.6), TruthfulQA 38.8 (vs 39.0). Mistral-LongRoPE ft=128k: ARC-c 59.0 (vs 60.6), HellaSwag 81.2 (vs 83.2), MMLU 61.3 (vs 63.6), TruthfulQA 43.1 (vs 42.6) (Table 8, Section 4.3). Scope: 4096 context only, 4 benchmarks. Magnitude: LLaMA2 drops 0.2-3.2 points; Mistral within 2.0 points on all tasks. Status: **supported** (4 benchmarks, single evaluation context length -- moderate evidence).

**C7. RoPE dimension non-uniformity is the primary contributor; token position non-uniformity provides diminishing benefit at extreme lengths.** Ablation (Table 11): at 16k, RoPE dim reduces PI 14.88 to 7.28; adding start tokens further to 7.22. At 32k, dim gives 13.00, adding tokens gives 11.51. At 2048k, both yield 7.08 -- token position non-uniformity provides no additional benefit (Section 4.3). Scope: LLaMA2-7B non-fine-tuned 16k/32k and ft=256k extended to 2048k. Magnitude: 0.06-1.49 perplexity improvement from token non-uniformity at shorter lengths, 0.0 at 2048k. Status: **supported** (single model, limited lengths -- moderate evidence).

---

## Open Questions

1. **Can evolutionary search be replaced with analytical formulas?** The paper uses computationally expensive search to find rescale factors. Whether these factors follow predictable patterns that could be captured by closed-form expressions remains unknown. The monotonicity constraint hints at structure, but no closed-form relationship is derived. Unresolved.

2. **Does progressive extension generalize beyond LLaMA2/Mistral?** The 8x non-fine-tuning extension capability is demonstrated only on these two 7B models. Whether this ratio holds for other architectures, different model sizes, or different base theta values is untested. Unresolved.

3. **What is the optimal trade-off between search cost and extension quality?** The paper uses fixed search budgets and acknowledges that more search time could yield better results (Section A.3); a systematic study of diminishing returns is not provided. Unresolved.

4. **Why does Mistral degrade more than LLaMA2 at very long contexts?** Despite similar architecture and RoPE configuration, Mistral shows substantially worse perplexity and passkey accuracy beyond 256k. The paper suggests the 16k training length is a factor but does not isolate this variable. Unresolved.

5. **Can token position non-uniformity be made effective at extreme lengths?** The ablation shows n_hat provides no benefit at 2048k (Table 11). Whether a different formulation of position-dependent rescaling could help at extreme lengths is an open question the authors explicitly leave for future work. Unresolved.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces Rotary Position Embeddings (RoPE), the positional encoding that LongRoPE modifies. The entire method is built on RoPE's per-dimension frequency structure theta_i = theta^(-2i/d) with default theta = 10000.

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer architecture; provides context for positional encoding requirements in self-attention.

### Direct Predecessors (Positional Interpolation Methods)

- **Chen et al. (2023a)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* The uniform linear interpolation baseline (PI) that LongRoPE improves upon. PI's limitation of treating all dimensions identically with lambda = s motivates the non-uniform search. Also identifies the short-context degradation problem.

- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* The frequency-aware NTK-by-parts interpolation method. LongRoPE builds on YaRN's insight that dimensions should be treated differently, but replaces fixed grouping formulas with searched factors. LongRoPE also follows YaRN's fine-tuning settings for Mistral.

- **LocalLLaMA (2023b)** -- *NTK-Aware Scaled RoPE.* Proposes spreading interpolation pressure via base frequency change, distributing across RoPE dimensions. LongRoPE's evolutionary search is initialized with NTK solutions, and the monotonicity constraint is based on NTK theory.

- **LocalLLaMA (2023a)** -- *Dynamically Scaled RoPE.* Improved dynamic NTK that adjusts extension ratio based on current sequence length. Comparison baseline in non-fine-tuning experiments.

### Context Extension Methods

- **Roziere et al. (2023)** -- *Code Llama: Open Foundation Models for Code.* Uses NTK-aware scaling for 100k context; serves as a fine-tuning-based comparison baseline, showing limitations of fixed rescaling.

- **Chen et al. (2023b)** -- *LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models.* Full fine-tuning with PI for 100k context; comparison baseline. Also represents efficient fine-tuning approaches that are orthogonal to LongRoPE.

### Attention Pattern Observations

- **Xiao et al. (2023)** -- *Efficient Streaming Language Models with Attention Sinks.* Provides evidence that initial tokens receive disproportionately large attention scores ("attention sinks"), motivating LongRoPE's n_hat starting token threshold.

- **Han et al. (2023)** -- *LM-Infinite: Simple On-the-Fly Length Generalization.* Further evidence for the importance of initial token positions in attention computation.

### Models Evaluated

- **Touvron et al. (2023)** -- *LLaMA 2: Open Foundation and Fine-Tuned Chat Models.* Primary evaluation model; LongRoPE extends LLaMA2-7B from 4k to 2048k tokens.

- **Jiang et al. (2023)** -- *Mistral 7B.* Secondary evaluation model demonstrating generalization beyond the LLaMA family.

### Evaluation Datasets and Benchmarks

- **Rae et al. (2019)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Source of the PG19 dataset used for perplexity evaluation and search fitness evaluation.

- **Gao et al. (2020)** -- *The Pile: An 800GB Dataset of Diverse Text for Language Modeling.* Source of the Books3/Pile-Books3 subset used for perplexity evaluation at extreme lengths (>512k) and search fitness.

- **Mohtashami & Jaggi (2023)** -- *Landmark Attention: Random-Access Infinite Context Length for Transformers.* Provides the passkey retrieval evaluation task used to measure effective context utilization.

- **Clark et al. (2018)** -- *ARC: AI2 Reasoning Challenge.* 25-shot ARC-Challenge benchmark for short-context evaluation.

- **Zellers et al. (2019)** -- *HellaSwag.* 10-shot commonsense NLI benchmark for short-context evaluation.

- **Hendrycks et al. (2020)** -- *MMLU: Measuring Massive Multitask Language Understanding.* 5-shot multitask benchmark for short-context evaluation.

- **Lin et al. (2021)** -- *TruthfulQA.* 0-shot benchmark for truthfulness evaluation.

### Search Methodology

- **Guo et al. (2020)** -- *Single Path One-Shot Neural Architecture Search with Uniform Sampling.* Provides the evolutionary search framework adapted for RoPE rescale factor optimization.
