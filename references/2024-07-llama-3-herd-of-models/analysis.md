---
title: "The Llama 3 Herd of Models"
authors: "Dubey, Jauhri, Pandey, Kadian, Al-Dahle, Letman, Mathur, Schelten, Yang, Fan, et al."
year: 2024
venue: "arXiv preprint 2407.21783"
paper_type: preprint
categories: ["model-release", "architecture", "context-extension", "long-context-evaluation", "scaling-laws"]
scope: ["open foundation models", "dense transformer scaling", "128K context extension", "grouped-query attention", "RoPE scaling", "multimodal integration", "tool use"]
benchmarks_used: ["mmlu", "mmlu-pro", "gsm8k", "humaneval", "mbpp", "arc", "hellaswag", "winogrande", "piqa", "natural-questions", "triviaqa", "squad", "bbh", "agi-eval", "race", "boolq", "niah", "zeroscrolls", "infinitebench", "gpqa", "ifeval", "mgsm", "drop"]
models_introduced: ["llama-3-8b", "llama-3-70b", "llama-3.1-8b", "llama-3.1-70b", "llama-3.1-405b"]
models_evaluated: ["llama-2-7b", "llama-2-70b", "mistral-7b", "mixtral-8x7b", "gpt-4", "gpt-4o", "claude-3.5-sonnet", "gemini-1.5-pro"]
key_claims:
  - id: C1
    claim: "Llama 3.1 405B performs competitively with GPT-4 across benchmarks, scoring 88.6% on MMLU (0-shot CoT) vs GPT-4's 85.4% and GPT-4o's 88.7%"
    evidence: "Table 2, Section 5.2"
    status: supported
    scope: "English benchmarks, post-trained instruct models, 0-shot and few-shot evaluation"
    magnitude: "88.6% MMLU (vs GPT-4 85.4%, GPT-4o 88.7%); 96.8% GSM8K (vs GPT-4 94.2%); 96.9% ARC-C (vs GPT-4 96.4%)"
  - id: C2
    claim: "Pre-training on 15.6T tokens with 3.8x10^25 FLOPs yields a 405B dense model that outperforms earlier larger models such as PaLM 540B"
    evidence: "Section 3, Section 9.1, Table 13"
    status: supported
    scope: "dense Transformer architecture, English-dominant pre-training corpus with multilingual data"
    magnitude: "405B parameters trained on 15.6T tokens vs PaLM 540B; MMLU pre-trained: 85.2% (Llama 3 405B) vs 86.4% (GPT-4)"
  - id: C3
    claim: "Context length extension from 8K to 128K tokens via incremental training on ~800B tokens achieves 100% needle-in-a-haystack retrieval at all depths and context lengths"
    evidence: "Section 3.4.2, Figure 7"
    status: supported
    scope: "single-needle retrieval, 128K context, 6-stage incremental extension for 405B"
    magnitude: "100% single-needle retrieval; >97.5% multi-needle recall across all model sizes (Table 21)"
  - id: C4
    claim: "Llama 3 405B achieves 95.2% on ZeroSCROLLS/QuALITY, matching GPT-4 (0125) and outperforming GPT-4o (90.5%)"
    evidence: "Table 2, Table 21"
    status: supported
    scope: "ZeroSCROLLS validation set, exact match metric, 128K context post-trained models"
    magnitude: "95.2% EM (matching GPT-4 0125 at 95.2%; GPT-4o at 90.5%; Claude 3.5 Sonnet at 90.5%)"
  - id: C5
    claim: "Training the 405B model on 16K H100 GPUs achieves >90% effective training time despite 466 job interruptions in a 54-day period"
    evidence: "Section 3.3.4, Table 5"
    status: supported
    scope: "54-day snapshot period, Meta production cluster with RoCE fabric, 16K H100 GPUs"
    magnitude: ">90% effective training time; 466 total interruptions (419 unexpected, 58.7% GPU-related)"
  - id: C6
    claim: "Scaling law extrapolation with (alpha, A) = (0.53, 0.29) correctly predicts training a 402B model on 16.55T tokens as compute-optimal for 3.8x10^25 FLOPs"
    evidence: "Section 3.2.1, Figure 2, Figure 3"
    status: supported
    scope: "power-law fit from 6x10^18 to 10^22 FLOPs extrapolated to 3.8x10^25 FLOPs"
    magnitude: "Predicted 402B parameters on 16.55T tokens; actual 405B trained on 15.6T tokens"
  - id: C7
    claim: "Mixing 0.1% synthetic long-context SFT data with short-context data optimizes both long- and short-context performance; DPO on short-context data alone does not degrade long-context capabilities"
    evidence: "Section 4.3.4"
    status: supported
    scope: "post-training stage only, synthetic QA/summarization/code reasoning data, Llama 3 models"
    magnitude: "0.1% mixing ratio; DPO on short-context only preserves long-context performance (qualitative)"
  - id: C8
    claim: "Llama 3 405B trails GPT-4o and Claude 3.5 Sonnet on human evaluations, particularly on reasoning and coding"
    evidence: "Figure 17, Section 5.3"
    status: supported
    scope: "~7,000 prompts, 6 single-turn + 3 multi-turn capabilities, 7-point scale, excluding ties"
    magnitude: "vs GPT-4o: 16.8% win / 30.1% loss on reasoning, 22.0% win / 28.0% loss on coding; vs Claude 3.5 Sonnet: 22.4% win / 28.5% loss on coding"
cross_references:
  - target: 2023-07-llama-2-open-foundation-chat
    type: extends
    detail: "Direct successor to Llama 2 with 8x more training data (15.6T vs 2T tokens), 128K context (vs 4K), 405B flagship model, and improved tokenizer (128K vocabulary)"
  - target: 2023-02-llama-open-efficient-foundation
    type: extends
    detail: "Third generation of LLaMA family, retaining decoder-only dense Transformer with RoPE, RMSNorm, SwiGLU but scaling to 405B parameters and 15.6T tokens"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Uses standard dense Transformer architecture with minor modifications (GQA, RMSNorm, SwiGLU, RoPE)"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Uses RoPE with increased base frequency theta=500,000 (vs 10,000 in Llama 2) to support 128K context"
  - target: 2024-05-attention-sinks-streaming
    type: extended-by
    detail: "Attention sink analysis applicable to Llama 3 models"
  - target: 2025-07-position-bias-transformers
    type: extended-by
    detail: "Position bias analysis conducted on Llama 3 models"
  - target: 2025-04-effective-context-length-falls-short
    type: extended-by
    detail: "Evaluates effective context length of Llama 3 models, finding context utilization falls short of nominal window"
  - target: 2024-02-lost-in-the-middle
    type: extended-by
    detail: "Positional bias analysis methodology applicable to Llama 3's 128K context"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "Uses needle-in-a-haystack and multi-needle variants to validate 128K context extension at each incremental stage"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: uses-benchmark
    detail: "Uses ZeroSCROLLS QuALITY for long-context evaluation"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: uses-benchmark
    detail: "Uses InfiniteBench En.QA and En.MC for 100K+ token evaluation"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Mistral 7B included as an open-weight baseline for comparison with Llama 3 8B"
  - target: 2023-03-gpt-4-technical-report
    type: evaluates
    detail: "Evaluates Llama 3.1 405B against GPT-4 and GPT-4o across multiple benchmarks, showing competitive performance"
open_questions:
  - question: "Would training beyond 15.6T tokens continue to improve the 405B model, or has a data quality ceiling been reached?"
    addressed_by: null
  - question: "Can the multimodal compositional approach (cross-attention adapters) match jointly pre-trained multimodal models at scale?"
    addressed_by: null
  - question: "Does the 128K context extension maintain quality on tasks requiring reasoning over the full context, beyond simple retrieval?"
    addressed_by: 2025-04-effective-context-length-falls-short
  - question: "How does the 8K-to-128K incremental context extension compare to methods like YaRN or PI in terms of quality per compute?"
    addressed_by: null
  - question: "Would a mixture-of-experts architecture achieve better quality per inference FLOP than the dense 405B model at this scale?"
    addressed_by: null
---

# The Llama 3 Herd of Models

**Authors:** Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, et al. (Llama Team, AI @ Meta)
**Date:** July 2024, arXiv:2407.21783

---

## Core Research Problem

Despite the proliferation of large language models, the open-weight ecosystem lacked a model competitive with proprietary frontier systems (GPT-4, Claude 3.5 Sonnet, Gemini 1.5 Pro) across the full range of capabilities: general knowledge, coding, mathematics, reasoning, multilingual understanding, long-context processing, and tool use. Llama 2's largest model (70B parameters) trailed GPT-4 on most benchmarks and was limited to a 4,096-token context window. Scaling to hundreds of billions of parameters with dense architectures posed infrastructure challenges (training reliability, parallelism at 16K GPU scale), and integrating multimodal capabilities (vision, speech) typically required complex joint pre-training that could degrade text performance. The Llama 2 post-training pipeline used PPO-based RLHF, which was complex and difficult to scale. Furthermore, no openly released dense Transformer exceeded ~70B parameters at frontier quality levels. The core challenge was: **how to train and release an open-weight dense Transformer model family at 405B scale that matches proprietary frontier models while supporting 128K context, multilingual capabilities, and tool use, using a simple and scalable training recipe.**

---

## Problem Solutions

Llama 3 addresses this through three interconnected strategies:

1. **Massive data and compute scaling.** Train 8B, 70B, and 405B parameter dense Transformers on approximately 15.6T tokens (8x more than Llama 2) using 3.8 x 10^25 FLOPs. Use scaling laws with fitted parameters (alpha, A) = (0.53, 0.29) to determine that 402B parameters on 16.55T tokens is compute-optimal, then train smaller models well beyond compute-optimal to trade training compute for inference efficiency.

2. **Incremental context extension.** Extend context from 8K to 128K tokens during the final pre-training stage through six progressive increases in sequence length over ~800B tokens, using RoPE with base frequency theta = 500,000. Validate at each stage that short-context performance recovers and needle-in-a-haystack retrieval is perfect.

3. **Simple post-training with iterative refinement.** Apply six rounds of supervised fine-tuning (SFT), rejection sampling, and Direct Preference Optimization (DPO) -- replacing the PPO-based RLHF of Llama 2 -- combined with extensive synthetic data generation for coding, math, tool use, and long-context tasks.

---

## Approach Details

### Method

Llama 3 uses a **standard dense Transformer** (decoder-only, autoregressive) with minor modifications from the original Transformer architecture (Vaswani et al., 2017):

- **Grouped-Query Attention (GQA):** 8 key-value heads across all model sizes (vs. full MHA or size-dependent GQA in Llama 2). This reduces KV cache size by 4x (8B), 8x (70B), and 16x (405B) compared to standard MHA.
- **Positional encoding:** RoPE with base frequency theta = 500,000 (increased from 10,000 in Llama 2). Xiong et al. (2023) showed this value effective for context lengths up to 32,768 (Section 3.2).
- **Normalization:** RMSNorm (pre-normalization).
- **Activation:** SwiGLU.
- **Tokenizer:** 128,000-token vocabulary using tiktoken (100K base tokens + 28K additional tokens for non-English languages). Compression rate improved from 3.17 to 3.94 characters per token on English data vs. Llama 2's 32K SentencePiece tokenizer (Section 3.2).
- **Attention mask:** Document-level mask preventing cross-document attention within packed sequences, found important for long-context pre-training but with limited impact during standard pre-training (Section 3.2).

| Hyperparameter | 8B | 70B | 405B |
|---|---|---|---|
| Layers | 32 | 80 | 126 |
| Model Dimension | 4,096 | 8,192 | 16,384 |
| FFN Dimension | 14,336 | 28,672 | 53,248 |
| Attention Heads | 32 | 64 | 128 |
| Key/Value Heads | 8 | 8 | 8 |
| Peak Learning Rate | 3 x 10^-4 | 1.5 x 10^-4 | 8 x 10^-5 |
| Activation Function | SwiGLU | SwiGLU | SwiGLU |
| Vocabulary Size | 128,000 | 128,000 | 128,000 |
| Positional Embeddings | RoPE (theta=500,000) | RoPE (theta=500,000) | RoPE (theta=500,000) |

(Table 3, Section 3.2)

### Key Technical Components

#### Pre-Training Data

- **Total:** ~15T multilingual tokens from publicly available sources (knowledge cutoff end of 2023) (Section 3.1).
- **Composition:** ~50% general knowledge, ~25% mathematical/reasoning, ~17% code, ~8% multilingual (Section 3.1.2).
- **Curation pipeline:** PII/safety filtering, custom HTML parser for text extraction (optimized for precision in boilerplate removal; markdown removed as it was found harmful to performance), three-level deduplication (URL-level, document-level MinHash, line-level with threshold of 6 occurrences per 30M document bucket), heuristic filtering (n-gram coverage, "dirty word" counting, KL divergence), model-based quality filtering (fasttext + RoBERTa classifiers trained on Llama 2 predictions, DistilRoBERTa for efficiency) (Section 3.1.1).
- No Meta user data used.

#### Scaling Laws

The paper fits a power-law relation for compute-optimal training tokens (Section 3.2.1):

> N*(C) = A * C^alpha

with fitted parameters **(alpha, A) = (0.53, 0.29)** from models trained between 6 x 10^18 and 10^22 FLOPs (40M to 16B parameters). Extrapolation to 3.8 x 10^25 FLOPs predicts training a **402B parameter model on 16.55T tokens** as compute-optimal. A two-stage prediction methodology correlates (1) compute-optimal negative log-likelihood with training FLOPs, then (2) negative log-likelihood with task accuracy using both scaling law models and Llama 2 models. This predicts ARC Challenge performance within a slight underestimate across four orders of magnitude extrapolation (Figure 4). An important observation is that IsoFLOPs curves become **flatter** around the minimum as compute budget increases, meaning the 405B model is robust to small deviations from compute-optimal (Section 3.2.1).

#### Training Infrastructure (405B)

- **Hardware:** Up to 16K H100 GPUs (80GB HBM3, 700W TDP) from a cluster of 24K GPUs on Meta's Grand Teton platform (Section 3.3.1).
- **Network:** RoCE fabric with 400 Gbps interconnects, three-layer Clos topology. 3,072 GPUs per pod with full bisection bandwidth; 1:7 oversubscription between pods at aggregation layer (Section 3.3.1).
- **Storage:** Tectonic distributed file system, 240 PB, 2 TB/s sustained throughput (Section 3.3.1).
- **Parallelism (4D):** Tensor Parallelism (TP=8) within nodes, Context Parallelism (CP=up to 16), Pipeline Parallelism (PP=16), Data Parallelism (FSDP, DP=8-128). Order [TP, CP, PP, DP] optimized for network topology (Section 3.3.2).
- **Numerical precision:** BF16 with FP32 gradient accumulation and FP32 reduce-scatter (Section 3.3.2).
- **MFU:** 38-43% BF16 model FLOPs utilization depending on configuration (Table 4, Section 3.3.2).
- **Reliability:** >90% effective training time. In a 54-day snapshot, 466 job interruptions occurred (47 planned, 419 unexpected). GPU issues accounted for 58.7% of unexpected interruptions. Only 3 required manual intervention (Section 3.3.4, Table 5).

| GPUs | TP | CP | PP | DP | Seq. Len. | Tokens/Batch | TFLOPs/GPU | BF16 MFU |
|---|---|---|---|---|---|---|---|---|
| 8,192 | 8 | 1 | 16 | 64 | 8,192 | 16M | 430 | 43% |
| 16,384 | 8 | 1 | 16 | 128 | 8,192 | 16M | 400 | 41% |
| 16,384 | 8 | 16 | 16 | 8 | 131,072 | 16M | 380 | 38% |

(Table 4, Section 3.3.2)

#### Training Schedule (405B)

- **Optimizer:** AdamW (beta_1=0.9, beta_2=0.95, eps=1e-5) (Section 3.4.1).
- **LR schedule:** Cosine decay from 8 x 10^-5 to 8 x 10^-7 over 1,200,000 steps, with 8,000-step linear warmup (Section 3.4.1).
- **Batch size ramp:** 4M tokens (seq len 4,096) -> 8M tokens (seq len 8,192) after 252M tokens -> 16M tokens after 2.87T tokens (Section 3.4.1).
- **Total tokens:** 15.6T text tokens for the flagship model.
- **Training stability:** Very stable; few loss spikes observed and no interventions required for training divergence (Section 3.4.1).

#### Annealing

During the final 40M tokens, learning rate is linearly annealed to 0, context length set to 128K, and data mix adjusted to upsample high-quality sources. **Polyak averaging** of checkpoints during annealing produces the final pre-trained model. Annealing on GSM8K/MATH training sets improved the 8B model by **24.0%/6.4%** respectively; improvements on 405B were **negligible**, suggesting the flagship has strong in-context learning capabilities (Section 3.4.3, Section 3.1.3).

#### Context Length Extension

Context length is extended from 8K to 128K tokens during the final pre-training stage (Section 3.4.2):

1. Context length is increased **incrementally** in six stages (for 405B), starting from 8K and ending at 128K.
2. At each stage, two criteria must be met before proceeding: (a) short-context evaluation performance has **recovered completely**, (b) the model **perfectly solves needle-in-a-haystack** up to that length.
3. Approximately **800B training tokens** are used for the long-context stage.
4. **Context Parallelism (CP)** enables training on 128K sequences: the input is partitioned into 2 x CP chunks, with the i-th CP rank receiving the i-th and (2 x CP - 1 - i)-th chunks for load balancing. An all-gather based method collects K and V tensors for computing attention on local Q chunks. This is preferred over ring-based CP because (1) it supports different attention masks (e.g., document mask) more flexibly, and (2) the all-gather overhead is negligible since K/V tensors are much smaller than Q due to GQA (O(S) vs O(S^2)) (Section 3.3.2).
5. **Document attention mask** prevents cross-document attention within packed sequences, found important for long-context training (Section 3.2).

### Post-Training

Post-training uses six rounds of SFT followed by DPO -- replacing the PPO-based RLHF from Llama 2 (Section 4.1):

- **Reward modeling:** Trained on pre-trained checkpoint using human preference data. Margin term from Llama 2 RM loss removed. Training concatenates prompt + multiple shuffled responses in a single row for efficiency (Section 4.1.2).
- **SFT:** Learning rate 10^-5 over 8.5K-9K steps (Section 4.1.3).
- **DPO:** Learning rate 10^-5, beta=0.1. PPO was explored but DPO required less compute for large-scale models and performed better on IFEval. Two modifications: (1) masking formatting tokens from loss to prevent conflicting gradients, (2) NLL regularization with coefficient 0.2 on chosen sequences (Section 4.1.4).
- **Rejection sampling:** K=10-30 samples per prompt, selected by reward model. PagedAttention used for 2x throughput improvement during rejection sampling. Data from the 405B model used to train smaller models (distillation) (Section 4.2.2).
- **Model averaging** applied at each RM, SFT, and DPO stage (Section 4.1.5).
- **Synthetic data generation** used extensively: ~1M synthetic coding dialogs with execution feedback, ~1.2M backtranslation dialogs for code explanation/documentation, step-wise reasoning traces with MCTS and stepwise reward models for math, tool use data, and long-context synthetic QA/summarization/code reasoning (Sections 4.3.1, 4.3.3, 4.3.4, 4.3.5).

#### Long-Context Post-Training

- Synthetic SFT data generated for QA (documents split into 8K chunks, full document used as context), summarization (hierarchical approach), and long-context code reasoning (removing key dependency files from repos) (Section 4.3.4).
- Synthetic samples categorized by length: 16K, 32K, 64K, 128K tokens.
- **0.1% synthetic long-context data** mixed with short-context data optimizes both (Section 4.3.4).
- DPO on short-context data alone does **not** degrade long-context performance, suspected due to fewer optimizer steps in DPO than SFT (Section 4.3.4).

### Experimental Setup

**Pre-training evaluation:** Standard benchmarks across 8 categories (Table 8): reading comprehension (SQuAD V2, QuAC, RACE), code (HumanEval, MBPP), commonsense (CSQA, PiQA, SiQA, OpenBookQA, WinoGrande), math/reasoning (GSM8K, MATH, ARC-C, DROP, WorldSense), adversarial (Adv SQuAD, Dynabench SQuAD, GSM-Plus, PAWS), long context (QuALITY, many-shot GSM8K), aggregate (MMLU, MMLU-Pro, AGIEval, BBH) (Section 5.1).

**Post-training evaluation:** MMLU, MMLU-Pro, IFEval, GSM8K, MATH, GPQA, ARC-C, HumanEval, MBPP, MGSM, Nexus, BFCL, ZeroSCROLLS, NIAH, InfiniteBench. Decontamination applied via exact match with benchmark prompts (Section 5.2, Table 16).

**Human evaluation:** ~7,000 prompts spanning 6 single-turn and 3 multi-turn capabilities, ~10% easy / ~30% medium / ~60% hard. 7-point scale pairwise comparisons. Modeling teams did not have access to evaluation prompts (Section 5.3).

**Significance:** 95% confidence intervals reported assuming Gaussian distribution: CI(S) = 1.96 * sqrt(S*(1-S)/N) (Section 5.1.1).

**Reproducibility:** Code released at github.com/meta-llama/llama3. Model weights released under Llama 3 Community License. Evaluation data released on HuggingFace. Seeds and exact hyperparameters are partially documented; not all details (e.g., data mix proportions at each training stage) are fully specified.

### Key Results

**Post-trained models on key benchmarks (Table 2):**

| Benchmark | Llama 3 8B | Llama 3 70B | Llama 3 405B | GPT-4 (0125) | GPT-4o | Claude 3.5 Sonnet |
|---|---|---|---|---|---|---|
| MMLU (0-shot, CoT) | 73.0 | 86.0 | 88.6 | 85.4 | 88.7 | 88.3 |
| MMLU-Pro (5-shot, CoT) | 48.3 | 66.4 | 73.3 | 64.8 | 74.0 | 77.0 |
| IFEval | 80.4 | 87.5 | 88.6 | 84.3 | 85.6 | 88.0 |
| HumanEval (0-shot) | 72.6 | 80.5 | 89.0 | 86.6 | 90.2 | 92.0 |
| GSM8K (8-shot, CoT) | 84.5 | 95.1 | 96.8 | 94.2 | 96.1 | 96.4 |
| MATH (0-shot, CoT) | 51.9 | 68.0 | 73.8 | 64.5 | 76.6 | 71.1 |
| ARC-C (0-shot) | 83.4 | 94.8 | 96.9 | 96.4 | 96.7 | 96.7 |
| GPQA (0-shot, CoT) | 32.8 | 46.7 | 51.1 | 41.4 | 53.6 | 59.4 |
| MGSM (0-shot, CoT) | 68.9 | 86.9 | 91.6 | 85.9 | 90.5 | 91.6 |

(Table 2, Section 5.2. Llama 3 405B outperforms GPT-4 (0125) on MMLU, GSM8K, ARC-C, IFEval; trails GPT-4o on MATH and GPQA; trails Claude 3.5 Sonnet on MMLU-Pro, HumanEval, GPQA. Strong evidence: evaluation across 14+ benchmarks spanning 7 capability categories.)

**Long-context benchmarks (Table 21):**

| Benchmark | Llama 3 8B | Llama 3 70B | Llama 3 405B | GPT-4 (0125) | GPT-4o |
|---|---|---|---|---|---|
| ZeroSCROLLS/QuALITY (EM) | 81.0 | 90.5 | 95.2 | 95.2 | 90.5 |
| InfiniteBench En.MC (Acc) | 65.1 | 78.2 | 83.4 | 72.0 | 82.5 |
| Multi-needle (Recall) | 98.8 | 97.5 | 98.1 | 100.0 | 100.0 |
| InfiniteBench En.QA (F1) | 27.1 | 36.7 | 30.5 | 15.7 | 19.1 |

(Table 21, Section 5.2.6. Llama 3 405B matches GPT-4 on QuALITY at 95.2% and outperforms it on InfiniteBench En.MC (83.4% vs 72.0%) and En.QA (30.5% vs 15.7%). All Llama 3 models achieve near-perfect needle-in-a-haystack retrieval (>97.5%). Note: Claude 3.5 Sonnet scored 90.8% on multi-needle, substantially below Llama 3 models. Moderate evidence: 3 benchmark suites tested, but only accuracy/F1 metrics.)

**Pre-trained models on aggregate benchmarks (Table 13):**

| Model | MMLU | MMLU-Pro | AGIEval | BBH |
|---|---|---|---|---|
| Llama 3 8B | 66.7 | 37.1 | 47.8 | 64.2 |
| Llama 3 70B | 79.3 | 53.8 | 64.6 | 81.6 |
| Llama 3 405B | 85.2 | 61.6 | 71.6 | 85.9 |
| GPT-4 | 86.4 | -- | -- | -- |
| Gemini Ultra | 83.7 | -- | -- | 83.6 |

(Table 13, Section 5.1.1)

**Human evaluation (Figure 17, 405B vs competitors, excluding ties):**

| Competitor | Category | Win | Loss |
|---|---|---|---|
| GPT-4 | English | 24.1% | 23.6% |
| GPT-4 | Coding | 28.0% | 24.2% |
| GPT-4 | Multilingual | 19.7% | 31.1% |
| GPT-4o | English | 22.1% | 24.8% |
| GPT-4o | Reasoning | 16.8% | 30.1% |
| GPT-4o | Coding | 22.0% | 28.0% |
| GPT-4o | Multilingual | 17.4% | 34.7% |
| Claude 3.5 Sonnet | English | 29.0% | 20.5% |
| Claude 3.5 Sonnet | Reasoning | 18.9% | 26.4% |
| Claude 3.5 Sonnet | Coding | 22.4% | 28.5% |

(Figure 17, Section 5.3. Llama 3 405B is roughly at parity with GPT-4 on English and coding; trails GPT-4o on reasoning, coding, and multilingual; outperforms Claude 3.5 Sonnet on English but trails on reasoning and coding. Limited evidence on strength of human evaluation conclusions: ~7,000 prompts but subjective 7-point scale, annotator bias acknowledged.)

### Contamination Analysis

Novel contamination detection using 8-gram overlap applied to pre-training data (Table 15, Section 5.1.4). Key findings:

| Benchmark | Contamination % | Perf. gain 405B |
|---|---|---|
| AGIEval | 98 | 16.3 |
| BBH | 95 | 41.0 |
| HellaSwag | 85 | 14.3 |
| GSM8K | 41 | 1.3 |
| MATH | 1 | -0.2 |
| SQuAD | 0 | 0.0 |

High contamination in AGIEval (98%) and BBH (95%) with substantial performance gains warrants caution interpreting those results. GSM8K shows 41% contamination but minimal impact (1.3 point gain for 405B). MATH and SQuAD show negligible contamination effects. For MMLU, MMLU-Pro, HumanEval, and MBPP, 8-gram overlap gives such high contamination scores at all thresholds that performance gain estimation is not possible (Section 5.1.4).

### FP8 Inference Quantization

Applied to feedforward network layers (~50% of inference compute). Self-attention layers are not quantized. Three mitigations: (1) no quantization in first/last Transformer layers, (2) dynamic scaling factors upper-bounded to 1200 to prevent underflows from high-perplexity tokens, (3) row-wise quantization (per-row scaling factors for both parameters and activations) (Section 6.2).

FP8 achieves up to **50% throughput improvement** during pre-fill and fits the 405B model on a **single node** of 8 H100 GPUs (vs. 2 nodes for BF16), providing roughly a 2x throughput advantage. Quality impact is negligible as measured by reward score distribution over 100K responses (Figure 26, Section 6.2).

### Multimodal Integration

**Vision:** Compositional approach using cross-attention adapters between a pre-trained ViT-H/14 image encoder (850M parameters with multi-layer features and gated self-attention) and the language model. Cross-attention layers added after every 4th self-attention layer; ~100B additional parameters for Llama 3 405B. Video adapter adds temporal aggregator (perceiver resampler) and video cross-attention layers, supporting up to 64 frames (Section 7.2).

| Benchmark | Llama 3-V 405B | GPT-4V | GPT-4o | Claude 3.5 Sonnet |
|---|---|---|---|---|
| MMMU (val, CoT) | 64.5 | 56.4 | 69.1 | 68.3 |
| VQAv2 (test-dev) | 80.2 | 77.2 | -- | -- |
| ChartQA (test, CoT) | 85.8 | 78.4 | 85.7 | 90.8 |
| DocVQA (test) | 92.6 | 88.4 | 92.8 | 95.2 |

(Table 29, Section 7.6. Llama 3-V 405B outperforms GPT-4V on all benchmarks but trails GPT-4o on MMMU and Claude 3.5 Sonnet on ChartQA and DocVQA. Moderate evidence: 6 benchmarks tested but vision models not released.)

**Speech:** Encoder-adapter approach with conformer-based speech encoder (~100M adapter parameters). Supports 34 languages for understanding. Text-to-speech via streaming synthesis without language model fine-tuning. Language model parameters are not updated during speech adapter training (Sections 8, 8.2).

---

## Limitations and Failure Modes

1. **Trailing proprietary models on reasoning and coding.** Human evaluations show Llama 3 405B loses to GPT-4o on reasoning (16.8% win vs 30.1% loss) and coding (22.0% win vs 28.0% loss). GPQA scores trail Claude 3.5 Sonnet by 8.3 points (51.1% vs 59.4%) (Figure 17, Table 2).

2. **Multilingual gap.** Despite improved multilingual support (8 languages), Llama 3 405B trails GPT-4o on multilingual MMLU (83.2% vs 85.5%) and loses on multilingual human evaluations against GPT-4o (17.4% win vs 34.7% loss) (Table 20, Figure 17).

3. **High contamination on some benchmarks.** AGIEval (98%), BBH (95%), and HellaSwag (85%) show high contamination rates with substantial performance gains on contaminated samples, complicating interpretation of those results (Table 15, Section 5.1.4).

4. **Multimodal models not released.** Vision and speech capabilities are described as "still under active development and not yet ready for release" (Section 1). Image pre-training learning rate settings from small-scale experiments did not generalize to long training schedules. Numerical instabilities arose with BF16 gradient accumulation after adding the image encoder, requiring FP32 gradient accumulation (Section 7.3).

5. **Verbatim memorization scales with model size.** Average 50-gram verbatim memorization rates increase from 0.26% (8B) to 0.60% (70B) to 1.13% (405B) for English (Table 24, Section 5.4.2).

6. **File upload capability gap.** Human evaluation of code execution shows Llama 3 405B loses significantly to GPT-4o on file upload tasks (22.9% win vs 64.2% loss; Figure 16, Section 5.2.7).

7. **[Inferred]** The paper notes that dense architectures have "numerous trade offs in terms of training and inference efficiency" compared to MoE (Section 9.1), but does not quantify the inference cost disadvantage of the 405B dense model vs. comparable-quality MoE models.

8. **[Inferred]** No evaluation on tasks requiring reasoning across the full 128K context (as opposed to retrieval). The long-context benchmarks test retrieval (NIAH), QA (InfiniteBench), and reading comprehension (ZeroSCROLLS), but none require multi-step reasoning distributed across the full context window.

#### Scope and Comparability

- **What was not tested:** No evaluation on perplexity-based benchmarks (e.g., WikiText-2, PG-19), limiting comparability with papers that primarily report perplexity. No evaluation of effective context utilization beyond retrieval. No evaluation on LongBench, RULER, or BABILong. No evaluation of MoE baselines at equivalent compute budgets.
- **Comparability notes:** The paper uses both reproduced and reported numbers for competitor models, selecting the best score. For some 405B-class competitors, only reported numbers are available (pre-trained models not released). MMLU is evaluated in both 5-shot (standard) and 0-shot CoT configurations; the paper's Table 2 flagship comparison uses 0-shot CoT, which differs from the common 5-shot standard used in most leaderboards. Human evaluations exclude ties, making win/loss rates not directly comparable to studies that include ties. Contamination analysis uses 8-gram overlap, which may not be optimal for all benchmarks (e.g., for MMLU, HumanEval, MBPP, the method gives uninformative results).

---

## Conclusions

### Contributions

1. **Largest open-weight dense Transformer.** The 405B model with 128K context is the largest publicly available dense Transformer, trained on 15.6T tokens using 3.8 x 10^25 FLOPs. It performs competitively with GPT-4 across standard benchmarks (MMLU 88.6% vs 85.4%, GSM8K 96.8% vs 94.2%; Table 2).

2. **Validated compute-optimal scaling for dense models.** Scaling law extrapolation with (alpha, A) = (0.53, 0.29) correctly predicts the 402B/16.55T configuration from experiments spanning 6 x 10^18 to 10^22 FLOPs. IsoFLOPs curves flatten at high compute, making the model robust to small deviations (Section 3.2.1, Figure 2).

3. **Incremental context extension to 128K tokens.** Six-stage progressive extension from 8K to 128K over ~800B tokens achieves near-perfect needle-in-a-haystack retrieval and 95.2% on ZeroSCROLLS/QuALITY, matching GPT-4 (Section 3.4.2, Table 21).

4. **Simple post-training outperforms complex pipelines.** SFT + rejection sampling + DPO (without PPO) across six rounds, combined with extensive synthetic data generation, produces competitive results with less complexity. DPO was found to require less compute than PPO and perform better on instruction following benchmarks (Section 4.1.4).

5. **Compositional multimodal integration.** Cross-attention adapters for vision (~100B additional parameters for 405B) and speech (~100M adapter parameters) enable modality integration without degrading text performance and without joint pre-training. Vision model outperforms GPT-4V on all benchmarks tested (Table 29). Models not yet released (Sections 7, 8).

6. **Comprehensive training infrastructure documentation.** Detailed reporting of 4D parallelism strategies, flexible pipeline scheduling (tunable N), failure analysis (58.7% GPU-related), reliability engineering (>90% effective training time), and environmental effects (1-2% diurnal throughput variation from temperature) for 16K H100 GPU training (Section 3.3).

### Implications

1. **Dense architectures remain competitive at 405B scale.** Despite the trend toward MoE, Llama 3's dense architecture matches or exceeds MoE models (Mixtral 8x22B) on quality, though at higher inference cost. The paper states "dense architectures are not the limiting factor" (Section 9.1) -- this is speculative as no controlled MoE comparison at equivalent compute is provided.

2. **Data quality and quantity are the primary scaling lever.** The 8x increase in training data (15.6T vs 2T) and improved curation drove larger gains than architectural changes, consistent with "straightforward methods at ever increasing scales" (Section 9.1).

3. **Open-weight models can match proprietary frontier models.** Llama 3 405B achieves approximate parity with GPT-4 and narrows the gap to GPT-4o and Claude 3.5 Sonnet, though deficits remain on reasoning and multilingual tasks. Speculative: proprietary model comparisons depend heavily on evaluation methodology and benchmark selection.

4. **Context extension through continued pre-training is effective but costly.** The ~800B token investment for 8K-to-128K extension is substantial but achieves robust retrieval performance without architectural changes to the attention mechanism. Whether this quality holds for reasoning-intensive long-context tasks is unresolved.

---

## Key Claims

1. **Llama 3 405B matches GPT-4 on MMLU and outperforms it on several benchmarks.** MMLU 0-shot CoT: 88.6% vs 85.4%; GSM8K: 96.8% vs 94.2%; ARC-C: 96.9% vs 96.4%; IFEval: 88.6% vs 84.3%. Evidence: Table 2, Section 5.2. Status: **supported**. Scope: English benchmarks, post-trained instruct models. Magnitude: 88.6% vs 85.4% MMLU. Strong evidence: tested across 14+ benchmarks and 7 capability categories, though contamination concerns exist for AGIEval and BBH.

2. **Pre-training on 15.6T tokens with compute-optimal scaling produces a 405B model outperforming larger prior models.** Despite having fewer parameters than PaLM 540B, Llama 3 405B outperforms it through better scaling laws. Evidence: Section 3, Section 9.1. Status: **supported**. Scope: dense Transformer, English-dominant training. Magnitude: 405B < 540B parameters but higher benchmark scores. Moderate evidence: comparison with PaLM is indirect (different benchmarks, tokenizers, training data).

3. **Incremental context extension from 8K to 128K achieves 100% NIAH retrieval.** Six-stage progressive extension over ~800B tokens, with validation at each stage. Evidence: Section 3.4.2, Figure 7. Status: **supported**. Scope: single-needle retrieval task, up to 128K context. Magnitude: 100% single-needle, >97.5% multi-needle recall. Moderate evidence: retrieval is tested but reasoning over full context is not evaluated.

4. **Llama 3 405B achieves 95.2% on ZeroSCROLLS/QuALITY (128K context).** Matches GPT-4 (0125) at 95.2% and outperforms GPT-4o (90.5%) and Claude 3.5 Sonnet (90.5%). Evidence: Table 2, Table 21. Status: **supported**. Scope: ZeroSCROLLS validation set, exact match metric. Magnitude: 95.2% EM. Moderate evidence: single benchmark, validation set only (test set ground truth not publicly available).

5. **>90% effective training time achieved at 16K GPU scale.** Despite 419 unexpected interruptions in 54 days (78% hardware-related, 58.7% GPU-specific), only 3 required manual intervention. Evidence: Section 3.3.4, Table 5. Status: **supported**. Scope: Meta production cluster, 54-day snapshot, RoCE fabric. Magnitude: >90% effective training time, 466 total interruptions. Single observation period (limited evidence on generalizability to other clusters).

6. **Scaling law extrapolation with (alpha, A) = (0.53, 0.29) predicts the compute-optimal 402B/16.55T configuration.** Fitted from models at 6 x 10^18 to 10^22 FLOPs, extrapolated to 3.8 x 10^25 FLOPs. ARC Challenge prediction across four orders of magnitude slightly underestimates actual performance. Evidence: Section 3.2.1, Figures 2-4. Status: **supported**. Scope: power-law fit, 40M-16B model sizes extrapolated to 405B. Magnitude: predicted 402B/16.55T, actual 405B/15.6T. Moderate evidence: single extrapolation validated on one benchmark (ARC Challenge).

7. **0.1% synthetic long-context data suffices for post-training.** Mixing this proportion with short-context data optimizes both long- and short-context performance. DPO on short-context data alone does not degrade long-context capabilities. Evidence: Section 4.3.4. Status: **supported**. Scope: Llama 3 post-training, synthetic QA/summarization/code data. Magnitude: 0.1% mixing ratio. Limited evidence: ablation details not fully reported; no variance estimates.

8. **Llama 3 405B trails GPT-4o and Claude 3.5 Sonnet on human evaluations.** Loses on reasoning (16.8% vs 30.1% against GPT-4o), coding (22.0% vs 28.0% against GPT-4o), and multilingual (17.4% vs 34.7% against GPT-4o). Evidence: Figure 17, Section 5.3. Status: **supported**. Scope: ~7,000 prompts, 7-point scale, excluding ties. Magnitude: 13.3 pp gap on reasoning vs GPT-4o. Moderate evidence: large prompt set but subjective evaluation; annotator bias acknowledged as limitation.

---

## Open Questions

1. **Data scaling ceiling.** Would continued training beyond 15.6T tokens improve 405B performance, or has data quality become the bottleneck? The paper does not report training loss saturation behavior. The annealing results (negligible improvement for 405B on GSM8K/MATH) hint at diminishing returns for the flagship model.

2. **Dense vs. MoE at 405B+ scale.** The paper argues dense architectures are competitive but acknowledges inference efficiency trade-offs (Section 9.1). Whether MoE would achieve better quality per inference FLOP at this scale is unresolved. No controlled comparison at equivalent compute budget is provided.

3. **Effective context utilization at 128K.** While NIAH retrieval is near-perfect, whether the model can effectively reason over information distributed throughout a 128K context (not just retrieve it) remains unclear. Partially addressed by effective context length evaluations (2025-04-effective-context-length-falls-short).

4. **Context extension compute trade-off.** The ~800B token investment for 8K-to-128K extension is substantial. How this compares to post-hoc methods (YaRN, PI) in quality per compute is not analyzed.

5. **Multimodal integration scalability.** The compositional approach with cross-attention adapters adds ~100B parameters for vision at 405B scale. Whether this scales efficiently to higher resolutions, more modalities, and whether it can match jointly pre-trained multimodal models is unclear. The models remain unreleased.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The base Transformer architecture that Llama 3 retains as a dense decoder-only model with minor modifications.
- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Provides RoPE, used with increased base frequency theta=500,000 for 128K context support.
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.* Grouped-query attention used across all Llama 3 model sizes with 8 KV heads.

### Direct Predecessors

- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* First-generation open-weight LLaMA establishing the architecture (RMSNorm, SwiGLU, RoPE).
- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Direct predecessor with 2T tokens and 4K context. Llama 3 extends to 15.6T tokens, 128K context, and 405B parameters, and replaces PPO with DPO.

### Scaling Laws

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Foundational scaling law framework.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Compute-optimal training framework that Llama 3's scaling law extrapolation builds on, with fitted (alpha, A) = (0.53, 0.29).

### Context Extension

- **Xiong et al. (2023)** -- *Effective Long-Context Scaling of Foundation Models.* Showed RoPE theta=500,000 effective for context lengths up to 32,768, informing Llama 3's choice.

### Long-Context Evaluation

- **Kamradt (2023)** -- *Needle-in-a-Haystack test.* Used to validate context extension at each incremental stage and as a post-training benchmark.
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* Long-text understanding benchmark; QuALITY subset used for evaluation.
- **Zhang et al. (2024)** -- *InfiniteBench.* 100K+ token evaluation benchmark (En.QA and En.MC tasks).

### Post-Training

- **Rafailov et al. (2023)** -- *Direct Preference Optimization.* DPO replaces PPO from Llama 2's RLHF pipeline as the primary alignment method. Found to require less compute and perform better on instruction following.

### Competing Models

- **OpenAI (2023)** -- *GPT-4 Technical Report.* Primary comparison target for flagship model.
- **Jiang et al. (2024)** -- *Mixtral of Experts.* MoE model compared against Llama 3's dense approach; Llama 3 outperforms it.
- **Chowdhery et al. (2023)** -- *PaLM: Scaling Language Modeling with Pathways.* Larger (540B) but less performant model, demonstrating Llama 3's scaling efficiency.

### Multimodal Foundations

- **Alayrac et al. (2022)** -- *Flamingo: a Visual Language Model for Few-Shot Learning.* Cross-attention adapter architecture for composing vision encoders with language models, adopted in Llama 3's vision integration.
- **Xu et al. (2023)** -- *DINOv2.* Pre-trained ViT-H/14 image encoder used as the base vision encoder.
