---
title: "Why Does the Effective Context Length of LLMs Fall Short?"
authors: "An, Zhang, Zhong, Li, Gong, Luo, Xu, Kong"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["position-encoding", "context-extension", "long-context-evaluation", "position-bias"]
scope: ["effective vs claimed context length", "position frequency distribution", "training-free inference-time position manipulation"]
benchmarks_used: ["niah", "ruler", "infinitebench"]
models_introduced: []
models_evaluated: ["llama-2-7b", "llama-3-8b", "llama-3.1-8b", "llama-3.1-70b", "mistral-7b", "qwen2-72b"]
key_claims:
  - id: C1
    claim: "The left-skewed position frequency distribution in pretraining corpora is the root cause of the gap between effective and training context lengths"
    evidence: "Section 2.2, Figure 1, Eq. 2"
    status: supported
    scope: "RoPE-based models, SlimPajama-627B pretraining corpus, 2K-4K training lengths"
    magnitude: "positions i <= 1024 account for >80% of all occurrences; positions i >= 1536 constitute <5% when L=2048"
  - id: C2
    claim: "Models achieve similar effective context lengths at similar position frequencies, regardless of maximum training length"
    evidence: "Section 3, Figure 2b"
    status: supported
    scope: "1.3B TinyLlama models, 2K and 4K training lengths, SlimPajama-627B, 4-needle NIAH evaluation"
    magnitude: "both models reach 1,280-token effective length at f(1280) = 100B"
  - id: C3
    claim: "Most NIAH failure cases across 13 open-source models occur within the first L/3 of the document (peak failure depth 0-33.3%)"
    evidence: "Section 3, Table 4"
    status: supported
    scope: "13 open-source models with training lengths 2K-262K, 4-needle NIAH at training length"
    magnitude: "all 13 models have peak failure depth at 0-33.3%"
  - id: C4
    claim: "STRING improves average NIAH (4-needle) performance from 67.8% (RoPE) to 85.7% across 7 models without any training"
    evidence: "Section 4.2, Table 1"
    status: supported
    scope: "7 base models with training lengths 2K-128K, tested at training length, 500 test cases each"
    magnitude: "85.7% average vs 73.1% DCA (next best) and 67.8% RoPE baseline"
  - id: C5
    claim: "STRING improves Llama3.1 70B by 15.1 points and Qwen2 72B by 30.9 points on RULER at 128K sequence length"
    evidence: "Section 4.2, Table 2"
    status: supported
    scope: "RULER 13-task benchmark at 128K sequence length, Llama3.1 70B and Qwen2 72B"
    magnitude: "+15.1 points (66.6 to 81.7) for Llama3.1 70B; +30.9 points (53.7 to 84.6) for Qwen2 72B"
  - id: C6
    claim: "With STRING, Llama3.1 70B surpasses GPT-4-128K on both RULER (81.7 vs 81.2) and InfiniteBench (56.88 vs 55.69)"
    evidence: "Section 4.2, Tables 2 and 3"
    status: supported
    scope: "RULER at 128K and InfiniteBench at 128K, single configuration (S=L/3, W=128)"
    magnitude: "RULER: 81.7 vs 81.2 (+0.5); InfiniteBench: 56.88 vs 55.69 (+1.19)"
  - id: C7
    claim: "STRING incurs negligible overhead: within 0.3s additional latency per token and less than 5GB additional GPU memory compared to standard FlashAttention"
    evidence: "Appendix A.3, Figure 9"
    status: supported
    scope: "Llama3.1 8B on single NVIDIA 80G A100 GPU, context lengths 64K-128K, 50 test runs"
    magnitude: "<=0.3s additional latency per token; <5GB additional GPU memory at 128K"
cross_references:
  - target: 2024-01-roformer-rope
    type: extends
    detail: "STRING operates by manipulating RoPE's relative position matrix to replace undertrained tail positions with well-trained ones"
  - target: 2020-04-longformer-long-document-transformer
    type: extends
    detail: "STRING's FlashAttention implementation combines Longformer's sliding window attention with shifted self-attention"
  - target: 2024-10-ruler-context-size
    type: uses-benchmark
    detail: "Uses RULER as primary long-context evaluation benchmark; establishes new open-source SOTA at 128K"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: uses-benchmark
    detail: "Uses InfiniteBench for real-world long-context task evaluation at 128K"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "Uses 4-needle NIAH variant as primary diagnostic evaluation across 7 models"
  - target: 2024-05-yarn-context-extension
    type: evaluates
    detail: "Uses YaRN as a training-free extrapolation baseline; STRING outperforms it on all models and YaRN fails to improve Llama3.1-8B on RULER"
  - target: 2023-06-rope-ntk
    type: evaluates
    detail: "Uses NTK-Aware RoPE as a training-free extrapolation baseline; STRING outperforms it on all models"
  - target: 2023-06-pi-positional-interpolation
    type: evaluates
    detail: "References PI as a foundational context extension approach; STRING takes a fundamentally different approach of manipulating position indices rather than rescaling them"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Both identify position-dependent performance degradation; this paper attributes it to undertrained position frequencies rather than attention bias"
  - target: 2024-06-ada-leval-length-adaptable-benchmark
    type: complementary
    detail: "Both find effective context length falls short of claimed length using different methodologies"
  - target: 2026-01-longbench-pro
    type: complementary
    detail: "LongBench Pro provides large-scale 2026 evidence that claimed context windows often exceed effective long-context reasoning capability, complementing this paper's mechanistic analysis"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "Attention sinks at position 0 are consistent with position 0 having the highest frequency in the left-skewed distribution"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong provides reasoning-in-a-haystack evaluation at scales up to 10M tokens, complementing STRING's diagnostic analysis of why effective context length falls short of training length"
  - target: 2025-11-context-length-hurts-performance
    type: complementary
    detail: "Du et al. show that context length alone degrades performance even with perfect retrieval and zero distraction, extending this paper's position frequency analysis to the problem-solving dimension"
  - target: 2024-07-llama-3-herd-of-models
    type: evaluates
    detail: "Evaluates effective context length of Llama 3 models"
  - target: 2024-03-gemini-1.5-long-context
    type: complementary
    detail: "Gemini 1.5 claims 10M-token context with near-perfect NIAH recall; STRING's findings about effective vs claimed context length are directly relevant to evaluating this claim"
  - target: 2021-11-long-range-models-use-context
    type: extends
    detail: "Sun et al. empirically observe that long-range context beyond 2K tokens has negligible impact on perplexity; this paper provides a mechanistic explanation via the left-skewed position frequency distribution"
  - target: 2024-08-flenqa-input-length-reasoning
    type: complementary
    detail: "FlenQA empirically demonstrates reasoning degradation at lengths far below technical maxima; this paper provides a mechanistic explanation via undertrained position indices from left-skewed training distributions"
  - target: 2024-05-pose-positional-skip-wise-training
    type: complementary
    detail: "PoSE demonstrates efficient long-context extension, while STRING diagnoses and mitigates the remaining effective-length gap inside claimed context windows"
open_questions:
  - question: "Can the left-skewed position frequency distribution be addressed during pretraining by adjusting the data length distribution, and would this preserve reasoning ability?"
    addressed_by: null
  - question: "How does STRING interact with post-training stages (SFT, RLHF) that may further skew position frequencies?"
    addressed_by: null
  - question: "Does STRING generalize to non-RoPE positional encodings such as ALiBi or T5-bias?"
    addressed_by: null
  - question: "How do multi-stage long-context training pipelines (e.g., Llama 3.1's 6-stage approach) affect the position frequency distribution when data distributions per stage are unknown?"
    addressed_by: null
---

# Why Does the Effective Context Length of LLMs Fall Short?

**Authors:** Chenxin An, Jun Zhang, Ming Zhong, Lei Li, Shansan Gong, Yao Luo, Jingjing Xu, Lingpeng Kong (The University of Hong Kong, ByteDance Inc., University of Illinois Urbana-Champaign)
**Date:** April 2025, ICLR 2025, arXiv:2410.18745

---

## Core Research Problem

Despite advances in distributed training and efficient attention (FlashAttention, Ring Attention), the **effective context lengths** of open-source LLMs fall far short of their claimed training context lengths. On the RULER benchmark (Hsieh et al., 2024), Llama 3.1 70B has an effective context length of only 64K despite being trained with a 128K context window using scaled RoPE base frequency. More broadly, most open-source models demonstrate an effective context length less than 50% of their training length (Hsieh et al., 2024). Prior work has focused on extending context windows through data engineering (Fu et al., 2024b; Hu et al., 2024), synthetic data generation (An et al., 2024b; Zhao et al., 2024), and architectural modifications to RoPE base frequency (Peng et al., 2023; Chen et al., 2023). However, these approaches treat the symptom (short effective context) without identifying the root cause. The core challenge is: **why does the effective context length of LLMs fall short of their training context lengths, and can this gap be closed without additional training?**

---

## Problem Solutions

The paper identifies the root cause as the **left-skewed position frequency distribution** -- a pattern of severe undertraining of long-distance relative position indices during pretraining and post-training stages -- and proposes STRING (ShifTed Rotary position embeddING), a training-free inference-time fix. The solution is built on:

1. **Diagnosis -- left-skewed position frequency distribution:** In pretraining corpora such as SlimPajama-627B, the frequency of relative position indices decreases dramatically with distance. For a 2048-token context window, positions i <= 1024 account for more than 80% of all position index occurrences, while positions i >= 1536 constitute less than 5% (Figure 1a). This undertraining of distant positions directly limits the model's ability to gather information from far-away tokens.

2. **Probing evidence -- position frequency determines effective length:** Controlled pretraining experiments show that models achieve similar effective context lengths when they have been exposed to similar frequencies of position indices, regardless of their maximum training lengths (Figure 2b). The growth trend of effective length aligns with the position frequency distribution.

3. **STRING -- shifting well-trained positions to replace undertrained ones:** During inference, STRING drops infrequent position indices at the tail of the distribution and shifts well-trained (frequent) position indices from the main diagonal of the position matrix to the bottom-left corner, enabling the model to represent long-range dependencies using frequently encountered positions. A small local window preserves neighboring-token relationships.

---

## Approach Details

### Method

#### Left-Skewed Position Frequency Distribution

For relative positional encodings such as RoPE (Su et al., 2022), the relative position matrix P after computing Q^T K for a training length L is a Toeplitz matrix:

> P[m][n] = m - n

The frequency of relative position i within a single sequence is f(i) = L - i. Across a pretraining corpus C, the total frequency is:

> f(i) = sum over s in C of max(|s| - i, 0), for 0 <= i < L  (Eq. 2)

This distribution is inherently left-skewed: position 0 occurs in every token pair, while position L-1 occurs only once per maximum-length sequence. The skew is compounded by the real-world data length distribution, which is also biased toward shorter sequences. In SlimPajama-627B with a 2048-token training length:

- **Natural data distribution** (Figure 1a): Position frequency decreases following a polynomial trend due to both the biased relative position matrix and the biased data length distribution. About 20% of data consists of sequences around 256-512 tokens; approximately 20% are around 2048 tokens (from truncating long sequences).
- **Uniform data distribution** (Figure 1b): Position frequency declines quadratically.
- **Concatenated data distribution** (Figure 1c): Even when all data are concatenated to fill the context window, position frequency decreases linearly with increasing position indices.

#### Probing Experiments on Position Frequency and Effective Length

Two 1.3B-parameter TinyLlama models were pretrained from scratch on SlimPajama with context lengths of 2K and 4K tokens (1T tokens total). Effective context length was measured every 10B tokens using a 4-needle Needle-in-a-Haystack task (500 tests per length, 128-token steps). Three findings emerged:

**(1) Larger training context window consumes fewer tokens to achieve the same effective context length:** The 4K model achieved an effective length of 1.4K after 400B tokens; the 2K model required ~1T tokens for the same (Figure 2a).

**(2) Models achieve similar effective context lengths at similar position frequencies, regardless of training length:** When plotting effective context length against position frequency f(i) at that length (Figure 2b), the growth curves of both models align. For example, both reach 1,280-token effective length when f(1280) = 100B.

**(3) The growth trend of effective length aligns with the position frequency distribution:** Both models consume ~300B tokens to reach 1,024-token effective length (where their position frequencies are close), but diverge thereafter as the frequency gap widens (Figure 3). With 1T tokens, models trained at 2K vs 4K have close position frequencies when position index i <= 1024 but diverge for larger i.

Furthermore, evaluating 13 open-source models on NIAH, **all 13 models have peak failure depth at 0-33.3%** of the document (Table 4), indicating that the last L/3 positions fall into the undertrained tail of the position frequency distribution.

#### STRING: Manipulating the Position Matrix

STRING operates in three steps on the relative position matrix P, illustrated for L = 9, N = 6 (threshold for frequent positions), S = L - N = 3 (shift offset) in Figure 5:

**(1) Dropping Infrequent Positions:** Remove all position indices i >= N from the matrix.

**(2) Shifting Frequent Positions:** Shift remaining position indices from the main diagonal to fill the empty bottom-left triangle. The shift offset is S = L - N:

> P[m][n] = P[m][n] - S if m >= n - S; P[m][n] otherwise  (Eq. 3)

**(3) Restoring Locality with a Small Window:** Shifting disrupts local relationships by setting relative positions on the S-th diagonal to zero. A small local window W << S restores emphasis on the W closest neighboring tokens:

> P[m][n] = P[m][n] - S + W if m >= n - S; P[m][n] otherwise  (Eq. 4)

### Key Technical Components

- **Hyperparameters:** The authors recommend W >= 32 and L/7 <= S <= L/2. For all experiments across downstream tasks: **S = L/3** and **W = 128**.
- **Ablation on W** (Figure 7a): Performance is significantly better than RoPE when W >= 32. As long as W << S, further increasing W does not cause a performance drop.
- **Ablation on S** (Figure 7b): Within the range L/5 to L/2, performance increases with S. The trend slows when S exceeds L/3, indicating that at least the last 33-50% of positions can be overwritten.
- **Key distinction from extrapolation methods:** STRING improves performance *within* the training context length, while extrapolation methods (NTK, YaRN, ReRoPE, Self-Extend, DCA) aim to extend *beyond* it. When testing extrapolation baselines, the training length is set to 2/3 of the original and the scaling factor is 3/2.

### FlashAttention Implementation

STRING is implemented via FlashAttention (Dao et al., 2022) by splitting attention into two components (Algorithm 1):

1. **Sliding window attention** (lines 11-13): Calculates attention around the main diagonal for positions where m < n - S. Uses standard (unmodified) position indices for both queries and keys.

2. **Shifted self-attention** (lines 15-19): Computes attention in the bottom-left triangle for positions where m >= n - S. Query position indices are shifted: `pids_q_shifted = pids_query - S + W`. Keys retain original position indices. Only the last N rows of Q attend to the first N columns of K, V.

The two outputs are merged using a weighted combination based on their respective softmax normalizers (Algorithm 2). STRING incurs no additional computational cost beyond standard FlashAttention -- inference time overhead is within 0.3 seconds per token, and GPU memory increase is less than 5GB on Llama3.1 8B at 128K context (Figure 9, Appendix A.3).

### Experimental Setup

**Models:** Seven open-source base models with training lengths 2K-128K: TinyLlama-1.3B (pretrained by authors, 2K), TinyLlama-1.1B-3T (2K), Llama-2-7B (4K), Llama-3-8B (8K), LWM-7B-base (32K), Mistral-7B-base (32K), Llama-3.1-8B (128K). For RULER and InfiniteBench: additionally Llama3.1 70B and Qwen2 72B.

**Baselines:** Original RoPE, and five training-free extrapolation methods: NTK-Aware RoPE (LocalLLaMA, 2023), YaRN (Peng et al., 2023), ReRoPE (Su, 2023), Self-Extend (Jin et al., 2024), and DCA (An et al., 2024a). For extrapolation baselines, the training length is set to 2/3 of the original and the extrapolation scaling factor is 3/2.

**Evaluation benchmarks:**
- **Needle-in-a-Haystack** (4-needle, gkamradt 2023): 500 test cases per model, tested at training length
- **RULER** (Hsieh et al., 2024): 13 tasks (NIAH variants, variable tracing, aggregation, QA), 500 test cases per task, tested at 128K. Effective length = longest context where model surpasses Llama2-chat baseline (85.6 at 4K).
- **InfiniteBench** (Zhang et al., 2024d): long-context QA, summarization, retrieval, math, code, tested at 128K

### Key Results

**Needle-in-a-Haystack (4-needle) at training length (Table 1):**

| Model | L_train | ReRoPE | NTK | RoPE | Self-Extend | YaRN | DCA | STRING |
|---|---|---|---|---|---|---|---|---|
| TinyLlama-1.3B (ours) | 2K | 62.8 | 62.0 | 56.6 | 60.2 | 68.6 | 74.4 | **84.6** |
| TinyLlama-1.1B-3T | 2K | 77.2 | 79.8 | 69.8 | 83.2 | 88.0 | 80.2 | **97.2** |
| Llama-2-7B | 4K | 98.6 | 98.6 | 98.0 | 95.4 | 98.0 | 91.6 | **100.0** |
| Llama-3-8B | 8K | 99.6 | 100.0 | 99.8 | 99.8 | 100.0 | 99.9 | **99.6** |
| LWM-7B-base | 32K | 25.2 | 19.4 | 31.8 | 24.0 | 22.2 | 28.8 | **50.4** |
| Mistral-7B-base | 32K | 54.5 | 42.2 | 52.8 | 54.2 | 48.2 | 64.2 | **73.0** |
| Llama-3.1-8B | 128K | 53.6 | 71.2 | 66.0 | 65.8 | 68.8 | 72.8 | **95.2** |
| **Average** | -- | 67.3 | 67.6 | 67.8 | 69.6 | 70.5 | 73.1 | **85.7** |

- STRING outperforms all methods on every model except Llama-3-8B (where all methods saturate near 100%) (Table 1).
- The average improvement over the next best method (DCA) is 12.6 points.

**RULER at 128K sequence length (Table 2):**

| Model | Effective/Claimed | NIAH | VT | Aggregation | QA | Avg. |
|---|---|---|---|---|---|---|
| GPT-4-1106-preview | 64K / 128K | 84.8 | 99.6 | 79.7 | 59.0 | 81.2 |
| GLM4 (open-source best) | 64K / 1M | 94.4 | 97.7 | 49.7 | 63.6 | 83.1 |
| Llama3.1 (8B) | 32K / 128K | 92.6 | 70.4 | 36.2 | 58.8 | 77.0 |
| Llama3.1 (8B) + STRING | 32K / 128K | 94.0 | 88.1 | 37.6 | 62.7 | **80.0** |
| Llama3.1 (70B) | 64K / 128K | 78.9 | 59.2 | 39.8 | 47.6 | 66.6 |
| Llama3.1 (70B) + STRING | 100K / 128K | 92.7 | 95.6 | 50.0 | 63.0 | **81.7** |
| Qwen2 (72B) | 64K / 128K | 48.0 | 79.0 | 70.3 | 47.2 | 53.7 |
| Qwen2 (72B) + STRING | 100K / 128K | 91.2 | 98.4 | 83.7 | 52.2 | **84.6** |

- STRING improves Llama3.1 70B by 15.1 points and Qwen2 72B by 30.9 points (Table 2).
- Both models with STRING surpass GPT-4-128K (81.2) in average performance.
- Effective context length increases from 64K to 100K for both 70B-scale models.
- At 100K test length, Llama3.1-STRING (70B) scores 87.2 and Qwen2-STRING (72B) scores 87.8.
- All other extrapolation methods (YaRN, DCA, Self-Extend, ReRoPE) fail to improve Llama3.1-8B on RULER (Table 2).

**InfiniteBench at 128K (Table 3):**

| Tasks | GPT-4 | Claude2 | Kimi-chat | Llama3.1 8B RoPE | Llama3.1 8B STRING | Llama3.1 70B RoPE | Llama3.1 70B STRING |
|---|---|---|---|---|---|---|---|
| En.Sum | 14.73 | 14.45 | 17.93 | 26.00 | 28.22 | 26.89 | 27.64 |
| En.QA | 22.22 | 11.97 | 16.52 | 10.05 | 10.20 | 13.68 | 16.73 |
| En.MC | 67.25 | 62.88 | 72.49 | 65.50 | 70.30 | 76.41 | 81.98 |
| En.Dia | 8.50 | 46.50 | 11.50 | 20.00 | 19.50 | 18.00 | 30.50 |
| Retr.PassKey | 100.00 | 97.80 | 98.14 | 100.00 | 100.00 | 100.00 | 100.00 |
| Retr.Number | 100.00 | 98.14 | 94.42 | 99.32 | 99.89 | 100.00 | 100.00 |
| Retr.KV | 89.00 | 65.40 | 53.60 | 42.00 | 83.00 | 2.22 | 76.07 |
| Code.debug | 39.59 | 2.28 | 18.02 | 22.84 | 26.90 | 29.20 | 32.80 |
| Math.find | 60.00 | 32.29 | 12.57 | 32.18 | 34.87 | 40.92 | 46.28 |
| **Avg.** | 55.69 | 47.96 | 43.91 | 46.43 | 52.54 | 45.25 | **56.88** |

- STRING improves Llama3.1 70B by 11.63 points average, surpassing GPT-4-128K (55.69 vs 56.88) (Table 3).
- The largest single-task gain is on Retr.KV: from 2.22 to 76.07 (+73.85 points).
- STRING also improves Llama3.1 8B by 6.11 points average (Table 3).

### Pretraining Setup (for TinyLlama-1.3B probing experiments)

- Architecture: TinyLlama 1.1B (hidden size 2048, FFN size 5632, 32 attention heads, 22 layers) with Llama3 tokenizer (128,256 tokens)
- Dataset: SlimPajama-627B, 1T tokens total
- Optimizer: AdamW, cosine learning rate schedule, max LR 4e-4, min LR 4e-5, warmup 2000 steps
- Batch size: 4M tokens, gradient clipping 1.0
- Hardware: 16 NVIDIA 80G A100 GPUs (2 nodes); ~28 days for 2K, ~32 days for 4K (Appendix A.2)

---

## Limitations and Failure Modes

1. **Probing experiments limited to small-scale pretraining.** The probing experiments only investigate pretraining lengths up to 4K tokens with 1.3B-parameter models. Whether the same position-frequency-to-effective-length relationship holds at larger scales and longer training contexts is not verified (Appendix A.4).

2. **Training-side fix unexplored.** STRING addresses the left-skewed distribution only at inference time. Adjusting the position frequency distribution during training (e.g., by oversampling long sequences) is left as future work, with the caveat that such adjustments may require data similar to the original pretraining corpus to preserve reasoning ability (Appendix A.4).

3. **Opaque training data for open-source models.** The position frequency analysis relies on knowing the pretraining data distribution. For most open-source LLMs (including Llama 3.1's 6-stage training pipeline), the data distributions are unknown, making it difficult to directly measure position frequencies (Section 3, Appendix A.4).

4. **Llama-3-8B saturation.** On Llama-3-8B (8K context), all methods including RoPE achieve near-perfect NIAH scores (~99.6-100%), leaving no room for STRING to demonstrate improvement (Table 1).

5. **No evaluation beyond training length.** STRING is designed to improve performance *within* the training context length, not to extrapolate beyond it. Whether STRING can be combined with extrapolation methods for additional gains is not investigated.

6. **Aggregation task gains limited on 8B models.** On RULER at 128K, STRING's improvement on the Aggregation category for Llama3.1 8B is minimal (36.2 to 37.6), suggesting the method's effectiveness varies by task type and model scale (Table 2).

### Scope and Comparability

- **What was not tested:** STRING is evaluated only on RoPE-based models. No evaluation on ALiBi, T5-bias, or absolute positional encodings. No evaluation on instruction-tuned or chat models (all experiments use base models). No evaluation on non-English tasks. Probing experiments are limited to 1.3B-parameter models with 2K/4K training lengths; the position-frequency-to-effective-length relationship has not been verified at larger scales or longer training contexts.
- **Comparability notes:** STRING operates *within* the training context length, while the baselines (NTK, YaRN, ReRoPE, Self-Extend, DCA) are designed for extrapolation *beyond* training length. To compare them, the baselines' training length is set to 2/3 of the original and the scaling factor to 3/2, which may disadvantage the baselines since they are not operating in their intended regime. The RULER effective context length definition (surpassing Llama2-chat at 4K, score 85.6) differs from other papers that may use different thresholds. InfiniteBench commercial model results are taken from Zhang et al. (2024d), not reproduced, so differences in inference settings may exist.

---

## Conclusions

### Contributions

1. **Identified the left-skewed position frequency distribution as the root cause of the effective context length gap.** The frequency of relative position indices in pretraining corpora decreases dramatically with distance. Positions in the last L/3 of the context window are severely undertrained, directly limiting models' ability to gather distant information (Section 2, Figure 1).

2. **Established that position frequency -- not training length -- determines effective context length.** Controlled pretraining experiments demonstrate that models achieve comparable effective context lengths when exposed to similar position frequencies, regardless of their maximum training lengths (Section 3, Figure 2b). This provides a causal explanation for the <50% effective-to-training length ratio observed across open-source LLMs.

3. **Proposed STRING, a training-free method achieving substantial gains.** By shifting well-trained position indices to replace infrequent ones during inference, STRING improves NIAH (4-needle) performance by an average of 18 points across seven models, boosts Llama3.1 70B and Qwen2 72B by over 10 points on RULER and InfiniteBench, and establishes new state-of-the-art results for open-source LLMs (Section 4.2, Tables 1-3).

4. **Demonstrated that open-source models can rival commercial models on long-context tasks.** With STRING, Llama3.1 70B surpasses GPT-4-128K on both RULER (81.7 vs 81.2) and InfiniteBench (56.88 vs 55.69), demonstrating that the gap between open-source and commercial models on long-context tasks is largely attributable to undertrained position indices (Tables 2, 3).

5. **Provided an efficient FlashAttention implementation.** STRING can be implemented with negligible overhead (within 0.3s per token and <5GB additional memory) by splitting attention into sliding window and shifted self-attention components (Appendix A.3, Figure 9).

### Implications

1. **Larger models benefit more from STRING.** The performance gains on 70B-scale models are substantially larger than on 8B models (e.g., 15.1 points vs 3.0 points on RULER), suggesting that frequent positions in larger models possess a stronger latent capacity for modeling long-range dependencies that is not exploited under standard position encoding (Table 2). This is an inference from the results, not a formally established causal relationship.

2. **Position frequency may be a general bottleneck for long-context LLMs.** If the position frequency distribution is indeed the primary constraint, then pretraining strategies that explicitly balance position frequencies (e.g., by adjusting data length distributions or introducing position-aware curriculum learning) could yield further improvements. This remains speculative pending training-side experiments.

3. **The last 33-50% of position indices may be expendable.** The ablation study (Figure 7b) shows performance improves as S increases from L/5 to L/2, suggesting a significant portion of the position index range is ineffective and can be overwritten without loss.

---

## Key Claims

1. **C1: Left-skewed position frequency distribution causes the effective context length gap.** When training with L=2048 on SlimPajama, position indices i <= 1024 account for more than 80% of all occurrences, while i >= 1536 constitute less than 5% (Section 2.2, Figure 1a). Status: **supported**.

2. **C2: Position frequency determines effective context length regardless of training window size.** Both 2K and 4K TinyLlama models reach 1,280-token effective length when f(1280) = 100B, and both consume ~300B tokens to reach 1,024-token effective length where frequencies are similar (Section 3, Figure 2b). Status: **supported**.

3. **C3: NIAH failures concentrate in first L/3 of document.** All 13 tested open-source models have peak failure depth at 0-33.3%, indicating the last L/3 positions fall in the undertrained tail (Section 3, Table 4). Status: **supported**.

4. **C4: STRING achieves 85.7% average on NIAH vs 73.1% for DCA (next best) and 67.8% for RoPE.** Tested across 7 models with training lengths from 2K to 128K, 500 test cases each (Section 4.2, Table 1). Status: **supported**.

5. **C5: STRING improves RULER by 15.1 points (Llama3.1 70B) and 30.9 points (Qwen2 72B) at 128K.** Effective context length increases from 64K to 100K for both models (Section 4.2, Table 2). Status: **supported**.

6. **C6: With STRING, open-source models surpass GPT-4-128K.** Llama3.1 70B + STRING: RULER 81.7 vs GPT-4 81.2; InfiniteBench 56.88 vs GPT-4 55.69 (Section 4.2, Tables 2 and 3). Status: **supported**.

7. **C7: Negligible implementation overhead.** On Llama3.1 8B with context lengths 64K-128K, STRING adds at most 0.3s per token latency and <5GB GPU memory compared to standard FlashAttention (Appendix A.3, Figure 9). Status: **supported**.

---

## Open Questions

1. **Can the left-skewed distribution be addressed during pretraining?** The authors note that adjusting position frequency during training may require data distributions similar to the original pretraining corpus to preserve reasoning ability. Whether position-aware data sampling or curriculum learning can close the effective-to-training length gap remains open.

2. **How does post-training affect position frequency?** SFT and RLHF stages may introduce their own position frequency biases (e.g., instruction-following data tends to be short). The interaction between pretraining and post-training position distributions is unexplored.

3. **Does STRING generalize beyond RoPE?** The method is designed for RoPE's relative position matrix. Whether similar manipulation strategies apply to ALiBi, T5-bias, or absolute positional encodings is unknown.

4. **How do multi-stage training pipelines affect position frequency?** Llama 3.1 uses a 6-stage approach to gradually extend context length, but the data distribution per stage is proprietary. The position frequency analysis in this paper uses only single-stage pretraining on SlimPajama.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations
- **Su et al. (2022)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding used by all models in the paper. STRING operates by manipulating RoPE's relative position matrix.
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational transformer architecture; establishes the self-attention mechanism that inherently lacks positional information.

### Context Extension Methods (Baselines)
- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation (PI).* Referenced as a foundational context extension method; STRING's approach is fundamentally different (manipulating the position matrix rather than rescaling position indices).
- **LocalLLaMA (2023)** -- *NTK-Aware Scaled RoPE (Reddit post).* Baseline method that increases the RoPE base frequency for extrapolation. STRING outperforms it across all NIAH experiments (Table 1).
- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension.* The most established RoPE extension method; used as a primary baseline. STRING outperforms YaRN on all models in Table 1, and YaRN is the only extrapolation method that improves over RoPE on average, yet STRING exceeds it by 15.2 points.
- **Su (2023)** -- *ReRoPE (Rectified Rotary Position Embeddings).* Position matrix modification method used as a baseline. ReRoPE modifies attention computation and is less compatible with FlashAttention.
- **Jin et al. (2024)** -- *Self-Extend LLM Context Window Without Tuning.* Training-free method using repeated positions for extrapolation; baseline in Tables 1 and 2.
- **An et al. (2024a)** -- *Training-Free Long-Context Scaling of Large Language Models (DCA).* By the same first author; second-best method after STRING in NIAH experiments (73.1% vs 85.7% average). DCA also manipulates the position matrix but uses a different strategy.

### Models Used in Evaluation
- **Llama Team (2024)** -- *The Llama 3 Herd of Models.* Provides Llama3.1 8B and 70B, the primary large-scale evaluation models. STRING increases Llama3.1 70B's effective length from 64K to 100K on RULER (Table 2).
- **Bai et al. (2023)** -- *Qwen Technical Report.* Provides Qwen2 72B. STRING improves Qwen2 72B by 30.9 points on RULER, achieving 84.6 average -- the highest open-source score (Table 2).
- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* Architecture basis for TinyLlama pretraining experiments.
- **Zhang et al. (2024b)** -- *TinyLlama: An Open-Source Small Language Model.* Architecture and training framework used for the probing experiments.
- **Mistral.AI (2024)** -- *Mistral 7B.* One of the seven evaluation models in the NIAH experiments (Table 1).
- **Liu et al. (2024a)** -- *LargeWorldModel (LWM-7B-base).* Long-context model trained with Ring Attention; used in NIAH evaluation (Table 1).

### Evaluation Benchmarks
- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Primary long-context benchmark with 13 synthetic tasks. STRING establishes new open-source SOTA on RULER at 128K (Table 2).
- **Zhang et al. (2024d)** -- *InfiniteBench: Extending Long Context Evaluation Beyond 100K Tokens.* Real-world long-context tasks (QA, summarization, retrieval, code, math). STRING enables Llama3.1 70B to surpass GPT-4-128K (Table 3).
- **gkamradt (2023)** -- *Needle-in-a-Haystack.* The foundational long-context retrieval test. The paper uses the 4-needle variant following the Llama 3.1 report.

### Pretraining Data and Infrastructure
- **Cerebras (2023)** -- *SlimPajama-627B.* Pretraining corpus for TinyLlama probing experiments and for analyzing the left-skewed position frequency distribution (Figure 1).
- **Dao (2023)** -- *FlashAttention-2.* Essential for STRING's implementation; STRING splits attention into sliding window and shifted self-attention components within FlashAttention (Algorithm 1).
- **Beltagy et al. (2020)** -- *Longformer.* Introduces sliding window attention, one of the two attention patterns STRING combines in its FlashAttention implementation.

### Scaling and Analysis
- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Referenced for the methodology of analyzing how effective length grows with consumed tokens (Section 3).
