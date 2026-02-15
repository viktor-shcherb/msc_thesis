---
title: "Gemma 3 Technical Report"
authors: "Gemma Team"
year: 2025
venue: "arXiv preprint 2503.19786"
paper_type: preprint
categories: ["model-release", "architecture", "context-extension", "long-context-evaluation", "attention-efficiency"]
scope: ["open multimodal models", "128K context", "local-global attention interleaving", "knowledge distillation", "KV cache efficiency", "vision-language"]
benchmarks_used: ["mmlu", "mmlu-pro", "gsm8k", "math-hendrycks", "humaneval", "mbpp", "gpqa", "hellaswag", "piqa", "winogrande", "arc", "bbh", "triviaqa", "natural-questions", "ruler", "mrcr", "mmmu", "livecodebench", "ifeval", "mgsm", "drop", "boolq", "siqa"]
models_introduced: ["gemma-3-1b", "gemma-3-4b", "gemma-3-12b", "gemma-3-27b"]
models_evaluated: ["gemma-2-2b", "gemma-2-9b", "gemma-2-27b", "gemini-1.5-pro", "gemini-1.5-flash", "deepseek-v3"]
key_claims:
  - id: C1
    claim: "5:1 local-to-global attention layer interleaving reduces KV cache memory overhead from ~60% to less than 15% at 32K context with minimal perplexity impact"
    evidence: "Figure 3, Figure 5, Section 5.2"
    status: supported
    scope: "text-only 2B model ablations, 32K context"
    magnitude: "~45 percentage point reduction in KV cache overhead at 32K; perplexity change within +/-0.1 even at 7:1 ratio"
  - id: C2
    claim: "Gemma 3 27B IT achieves Elo 1338 on Chatbot Arena, ranking 9th overall and above much larger open models"
    evidence: "Table 5, Section 4.1"
    status: supported
    scope: "preliminary results as of March 8, 2025; does not account for visual abilities"
    magnitude: "Elo 1338; 20 points above DeepSeek-V3 (1318, 671B/37B MoE), 69 points above LLaMA 3.1 405B (1269), 81 points above Qwen2.5-72B (1257), 118 points above Gemma 2 27B (1220)"
  - id: C3
    claim: "Gemma 3 models memorize long-form text at significantly lower rates than prior Gemma and Gemini models, with no personal information detected"
    evidence: "Figure 9, Section 6"
    status: supported
    scope: "exact and approximate memorization with 50-token prefix/suffix; personal information detected using Google Cloud SDP with high-recall settings"
    magnitude: "memorization rates around 0.001-0.01% (log scale) vs up to ~1% for prior models; ~24x relative increase in approximate vs exact memorization"
  - id: C4
    claim: "Gemma 3 4B IT is competitive with Gemma 2 27B IT, and Gemma 3 27B IT is comparable to Gemini 1.5 Pro across zero-shot IT benchmarks"
    evidence: "Table 6, Abstract"
    status: supported
    scope: "zero-shot IT benchmarks with Google-internal evaluation settings"
    magnitude: "Gemma 3 27B IT: 67.5 vs 56.9 (Gemma 2 27B) on MMLU-Pro; 89.0 vs 86.5 (Gemini 1.5 Pro) on MATH; 60.3 vs 52.0 (Gemini 1.5 Pro) on HiddenMath"
  - id: C5
    claim: "Sliding window size can be reduced to 1024 tokens (from 4096) without significant perplexity impact when using local-to-global interleaving"
    evidence: "Figure 4, Section 5.2"
    status: supported
    scope: "2B text-only model ablations with 1:1 and 3:1 local:global ratios"
    magnitude: "perplexity change within +/-0.01 across window sizes 512-4096"
  - id: C6
    claim: "Pan & Scan improves document understanding tasks by enabling native aspect ratio and resolution handling at inference time"
    evidence: "Table 8, Section 5.5"
    status: supported
    scope: "4B and 27B models on validation sets; 4-shot evaluation"
    magnitude: "+4.8 to +8.2 points on DocVQA, +12.9 to +17.0 points on InfoVQA, +1.6 to +1.9 on TextVQA"
  - id: C7
    claim: "RoPE rescaling with factor 8 enables 128K context after 32K pre-training, with perplexity generalizing to 128K but degrading beyond"
    evidence: "Figure 7, Section 5.3"
    status: supported
    scope: "4B, 12B, 27B models; perplexity evaluation"
    magnitude: "perplexity stable through 128K then rapid degradation; RULER 27B IT: 91.1% at 32K vs 66.0% at 128K"
  - id: C8
    claim: "For distillation, larger teachers become better than smaller teachers for longer training horizons"
    evidence: "Figure 8, Section 5.4"
    status: supported
    scope: "2B student model with two teacher sizes; single comparison"
    magnitude: "crossover at approximately 30-40B training tokens; delta perplexity shifts from +0.002 to -0.006"
cross_references:
  - target: 2024-03-gemma-open-models
    type: extends
    detail: "Third generation of Gemma family, adding multimodality, 128K context, and 5:1 local-global attention interleaving"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Decoder-only Transformer with GQA, RoPE, RMSNorm, and novel local-global attention interleaving"
  - target: 2024-10-ruler-context-size
    type: uses-benchmark
    detail: "Uses RULER for long-context evaluation at 32K and 128K lengths"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "Different approach to context extension; Gemma 3 uses RoPE rescaling with increased base frequency (10K to 1M for global layers)"
  - target: 2025-04-kimi-vl-technical-report
    type: concurrent
    detail: "Both are 2025 multimodal models with 128K context; Kimi-VL uses MoE with 2.8B activated parameters while Gemma 3 uses dense local-global interleaving"
  - target: 2025-07-smollm3-long-context-reasoner
    type: concurrent
    detail: "SmolLM3 3B competes in the same small-model space as Gemma 3 4B; both target 128K context with fully open weights"
open_questions:
  - question: "How does the 5:1 local-global interleaving affect tasks requiring multi-hop reasoning across the full 128K context?"
    addressed_by: null
  - question: "Would the local-global attention pattern transfer to MoE architectures?"
    addressed_by: null
  - question: "Can the significantly reduced memorization rates be attributed to specific architectural or training choices?"
    addressed_by: null
  - question: "Would unfreezing the vision encoder during training improve vision-language integration, and at what cost to text performance?"
    addressed_by: null
  - question: "What modifications would be needed to extend beyond 128K context without the rapid perplexity degradation observed in Figure 7?"
    addressed_by: null
---

# Gemma 3 Technical Report

**Authors:** Gemma Team (Google DeepMind)
**Date:** March 2025, arXiv:2503.19786

---

## Core Research Problem

Open language models face a fundamental tension between capability and efficiency at deployment scale. Previous Gemma models (Gemma Team, 2024a,b) supported only 8K context and lacked vision capabilities, limiting their applicability. Extending context to 128K tokens with standard global attention causes the **KV cache to grow linearly with sequence length**, creating memory bottlenecks -- at 32K context, the KV cache consumes approximately 60% of total memory in a standard global-only attention configuration (Figure 5, Section 5.2). This prevents deployment on consumer hardware such as PCs, laptops, and high-end GPUs. Additionally, multimodal capability requires integrating vision encoders without degrading text performance, and prior open models lacked competitive multilingual coverage. The core challenge was: **how to add multimodality and 128K context to lightweight open models while maintaining KV cache efficiency for consumer hardware deployment.**

---

## Problem Solutions

Gemma 3 addresses these challenges through three architectural and training innovations:

1. **5:1 local-to-global attention interleaving.** Alternate 5 local sliding window attention layers (1024-token span) with 1 global attention layer to reduce KV cache memory from ~60% overhead to <15% at 32K context, with perplexity changes within +/-0.1 (Figures 3, 5).

2. **RoPE frequency scaling for long context.** Increase global attention RoPE base frequency from 10K to 1M while keeping local layers at 10K, and apply RoPE rescaling with factor 8 to extend from 32K pre-training context to 128K at deployment (Figure 7, Section 5.3).

3. **Frozen vision encoder with Pan & Scan.** Use a shared 400M SigLIP encoder (frozen during training) with adaptive windowing at inference to handle varying aspect ratios and resolutions, providing +4.8 to +17.0 point improvements on document understanding tasks (Table 8).

---

## Approach Details

### Method

Gemma 3 uses a **decoder-only Transformer** architecture with the following key modifications from previous Gemma versions:

- **Grouped-Query Attention (GQA):** Same as Gemma 2 (Ainslie et al., 2023).
- **Normalization:** RMSNorm (Zhang and Sennrich, 2019) with both post-norm and pre-norm.
- **QK-norm:** Replaces the soft-capping mechanism from Gemma 2, inspired by Dehghani et al. (2023), Wortsman et al. (2023), and Chameleon Team (2024).
- **5:1 local-global interleaving:** 5 local sliding window layers (1024-token span) followed by 1 global attention layer, starting with a local layer as the first layer.
- **RoPE base frequency:** 1M for global attention layers (up from 10K in Gemma 2), 10K for local attention layers.

**Table 1 -- Parameter Counts:**

| Model | Vision Encoder | Embedding Params | Non-embedding Params |
|-------|----------------|------------------|----------------------|
| 1B | 0 | 302M | 698M |
| 4B | 417M | 675M | 3,209M |
| 12B | 417M | 1,012M | 10,759M |
| 27B | 417M | 1,416M | 25,600M |

The vocabulary has 262K entries using the Gemini 2.0 SentencePiece tokenizer (Kudo and Richardson, 2018), which is more balanced for non-English languages than the previous Gemma tokenizer.

#### Vision Modality

- **Vision encoder:** 400M SigLIP variant (Zhai et al., 2023), a Vision Transformer (Dosovitskiy, 2020) trained with a CLIP-like loss (Radford et al., 2021). **Frozen** during training to preserve text capabilities; shared across 4B, 12B, 27B models.
- **Input resolution:** 896 x 896 pixels.
- **Output compression:** 256 image tokens per image via 4x4 average pooling. This makes 4B and 12B models approximately **10x cheaper to transfer** compared with PaliGemma 2 at the same resolution (Section 5.5).
- **Pan & Scan (P&S):** Inference-time adaptive windowing inspired by LLaVA (Liu et al., 2024). Segments images into non-overlapping crops, resizes each to 896x896, and passes to encoder. Applied only when necessary, with control over maximum number of crops. Can be disabled for faster inference.

### Key Technical Components

#### Local-Global Attention Interleaving

The 5:1 local-to-global ratio was validated through ablations on 2B and 9B text-only models (Figures 3-6):

**Perplexity impact of local:global ratio (Figure 3):** Both 2B and 9B models show delta perplexity within +/-0.1 across ratios from 1:1 to 7:1, confirming minimal quality loss from increased local layer proportion (limited evidence: text-only models only, no downstream task evaluation).

**Sliding window size impact (Figure 4):** Delta perplexity remains within +/-0.01 for window sizes from 512 to 4096 tokens at both 1:1 and 3:1 ratios on a 2B model (limited evidence: single model size).

**KV cache memory impact (Figure 5, 2B model at 32K context):**

| Configuration | KV Cache Overhead at 32K |
|---------------|--------------------------|
| Global only (Gemma 1, LLaMA style) | ~60% |
| 1:1, sw=4096 (Gemma 2) | ~35% |
| 1:3, sw=1024 (Gemma 3 style) | <15% |

KV cache memory grows much more slowly with context length under the 5:1 architecture: Figure 6 shows the global-only 2B model KV cache growing steeply from 1K to 128K context, while the L:G=5:1, sw=1024 architecture shows dramatically reduced growth.

#### Long Context Extension

Instead of training with 128K sequences from scratch (Section 5.3):

1. Pre-train with **32K sequences**.
2. Apply **RoPE rescaling with factor 8** at end of pre-training (following Chen et al., 2023).
3. Increase global attention **RoPE base frequency from 10K to 1M**.

> RoPE rescaling factor = 8, applied to extend from 32K pre-training context to 128K inference context.

Models generalize to 128K context (perplexity stable) but **rapidly degrade beyond 128K** (Figure 7). This pattern is consistent across 4B, 12B, and 27B models (moderate evidence: three model sizes, perplexity metric only).

#### Distillation

All Gemma 3 models are trained with knowledge distillation (Hinton et al., 2015):

- Sample **256 logits per token**, weighted by teacher probabilities.
- Student learns the teacher's distribution within these samples via **cross-entropy loss**.
- Teacher's target distribution is set to zero probability for non-sampled logits, then renormalized.

**Teacher size ablation (Figure 8, Section 5.4):** For short training horizons, a smaller teacher is better (regularization effect); the trend reverses for longer training, with the crossover at approximately 30-40B tokens. This contradicts common findings that smaller teachers are always preferable for small students (limited evidence: single student size, two teacher sizes).

### Experimental Setup

#### Pre-Training

- **Training tokens:** 14T (27B), 12T (12B), 4T (4B), 2T (1B).
- **Data:** Mix of text and images; increased multilingual data with language balancing strategy inspired by Chung et al. (2023).
- **Filtering:** Quality reweighting (Sachdeva et al., 2024), evaluation set decontamination, PII filtering, reduction of recitation risk.
- **Vision embeddings:** Pre-computed for each image, adding no cost to language model training.

**Training Infrastructure (Table 2):**

| Model | TPU Type | #Chips | Data Shards | Seq Shards | Replicas |
|-------|----------|--------|-------------|------------|----------|
| 1B | TPUv5e | 512 | 16 | 16 | 2 |
| 4B | TPUv5e | 2048 | 16 | 16 | 8 |
| 12B | TPUv4 | 6144 | 16 | 16 | 24 |
| 27B | TPUv5p | 6144 | 24 | 8 | 32 |

Optimizer state sharded using ZeRO-3 (Ren et al., 2021). Multi-pod training via Pathways (Barham et al., 2022). Single-controller programming with JAX (Roberts et al., 2023) and GSPMD partitioner (Xu et al., 2021).

#### Post-Training

Post-training combines:
1. **Knowledge distillation** from a large IT teacher (Agarwal et al., 2024; Anil et al., 2018; Hinton et al., 2015).
2. **RL finetuning** using improved BOND (Sessa et al., 2024), WARM (Rame et al., 2024b), and WARP (Rame et al., 2024a).

**Reward functions:** Weight-averaged reward models trained on human feedback, code execution feedback (Gehring et al., 2024), and ground-truth rewards for solving math problems (DeepSeek-AI, 2025; Lambert et al., 2024).

**Data filtering for post-training:** Filtering of personal information, unsafe/toxic outputs, mistaken self-identification, and duplicated examples. Includes subsets encouraging better in-context attribution, hedging, and refusals.

#### Quantization Aware Training (QAT)

Quantized checkpoints provided by fine-tuning for approximately 5,000 steps using QAT (Jacob et al., 2018), with probabilities from the non-quantized checkpoint as targets.

**Table 3 -- Memory Footprints (weights only, GB):**

| Model | bf16 | Int4 | Int4 (blocks=32) | SFP8 |
|-------|------|------|-------------------|------|
| 1B | 2.0 | 0.5 | 0.7 | 1.0 |
| 4B | 8.0 | 2.6 | 2.9 | 4.4 |
| 12B | 24.0 | 6.6 | 7.1 | 12.4 |
| 27B | 54.0 | 14.1 | 15.3 | 27.4 |

**With KV cache at 32K context (8-bit quantized KV):**

| Model | bf16 + KV | Int4 + KV | Int4 (blocks=32) + KV | SFP8 + KV |
|-------|-----------|-----------|------------------------|-----------|
| 1B | 2.9 | 1.4 | 1.6 | 1.9 |
| 4B | 12.7 | 7.3 | 7.6 | 9.1 |
| 12B | 38.9 | 21.5 | 22.0 | 27.3 |
| 27B | 72.7 | 32.8 | 34.0 | 46.1 |

**Reproducibility:** Model weights available on HuggingFace and Kaggle. Code at github.com/google-deepmind/gemma. Training details (learning rate schedules, exact data mixtures) not published. No variance estimates reported for benchmark results.

### Key Results

#### Chatbot Arena (Table 5)

Gemma 3 27B IT achieves **Elo 1338** (rank 9, preliminary results as of March 8, 2025), above all other open dense models and several much larger models:

| Rank | Model | Elo | Open | Type | Params |
|------|-------|-----|------|------|--------|
| 9 | **Gemma-3-27B-IT** | **1338** | yes | Dense | 27B |
| 13 | DeepSeek-V3 | 1318 | yes | MoE | 671B/37B |
| 28 | Meta-Llama-3.1-405B-Instruct | 1269 | yes | Dense | 405B |
| 39 | Qwen2.5-72B-Instruct | 1257 | yes | Dense | 72B |
| 59 | Gemma-2-27B-it | 1220 | yes | Dense | 27B |

Note: Elo scores do not take into account visual abilities, which none of the listed competing open models have (limited evidence: single leaderboard snapshot, preliminary results).

#### IT Model Benchmarks (Table 6)

| Benchmark | Gemma 2 27B | Gemma 3 27B | Gemini 1.5 Pro | Gemini 2.0 Pro |
|-----------|-------------|-------------|----------------|----------------|
| MMLU-Pro | 56.9 | 67.5 | 75.8 | 79.1 |
| LiveCodeBench | 20.4 | 29.7 | 34.2 | 36.0 |
| Bird-SQL (dev) | 46.7 | 54.4 | 54.4 | 59.3 |
| GPQA Diamond | 34.3 | 42.4 | 59.1 | 64.7 |
| FACTS Grounding | 62.4 | 74.9 | 80.0 | 82.8 |
| Global MMLU-Lite | 68.6 | 75.1 | 80.8 | 86.5 |
| MATH | 55.6 | 89.0 | 86.5 | 91.8 |
| HiddenMath | 14.8 | 60.3 | 52.0 | 65.2 |
| MMMU (val) | - | 64.9 | 65.9 | 72.7 |

Key observations from Table 6:
- Gemma 3 27B IT **surpasses Gemini 1.5 Pro on MATH** (89.0 vs 86.5) and HiddenMath (60.3 vs 52.0).
- Gemma 3 27B IT remains **below Gemini 1.5 Pro** on GPQA Diamond (42.4 vs 59.1) and Global MMLU-Lite (75.1 vs 80.8).
- Authors do not compare directly with external models, encouraging third-party leaderboards for fairer comparison.

#### Additional IT Benchmarks (Table 18)

| Benchmark | Gemma 2 27B | Gemma 3 27B |
|-----------|-------------|-------------|
| MMLU | 76.2 | 76.9 |
| MBPP | 67.4 | 74.4 |
| HumanEval | 51.8 | 87.8 |
| GSM8K | 91.1 | 95.9 |
| BBH | 74.9 | 87.6 |
| IFEval | 91.1 | 90.4 |

Gemma 3 27B IT improves substantially on code (HumanEval: 87.8 vs 51.8) and reasoning (BBH: 87.6 vs 74.9) but shows marginal change on MMLU (76.9 vs 76.2) and slight regression on IFEval (90.4 vs 91.1) (strong evidence for code/reasoning gains: consistent across model sizes in Table 18).

#### Long Context (Table 15)

| Benchmark | Context | 4B PT | 12B PT | 27B PT | 4B IT | 12B IT | 27B IT |
|-----------|---------|-------|--------|--------|-------|--------|--------|
| RULER | 32K | 67.1 | 90.6 | 85.9 | 61.4 | 80.3 | 91.1 |
| RULER | 128K | 51.7 | 80.7 | 72.9 | 46.8 | 57.1 | 66.0 |
| MRCR | 32K | 44.7 | 59.8 | 63.2 | 49.8 | 53.7 | 63.2 |
| MRCR | 128K | 40.6 | 56.9 | 60.0 | 44.6 | 49.8 | 59.3 |

Notable: **IT models often score lower than PT models on long-context benchmarks** (e.g., RULER 128K: 12B PT 80.7 vs 12B IT 57.1), suggesting post-training may degrade long-context retrieval capabilities (moderate evidence: consistent across model sizes but only two benchmarks).

#### Vision -- Impact of Pan & Scan (Table 8, validation set, 4-shot)

| | DocVQA | InfoVQA | TextVQA |
|---|--------|---------|---------|
| 4B | 72.8 | 44.1 | 58.9 |
| 4B w/ P&S | 81.0 | 57.0 | 60.8 |
| Delta | +8.2 | +12.9 | +1.9 |
| 27B | 85.6 | 59.4 | 68.6 |
| 27B w/ P&S | 90.4 | 76.4 | 70.2 |
| Delta | +4.8 | +17.0 | +1.6 |

P&S improvements are largest on tasks requiring text reading from images (DocVQA, InfoVQA) and smaller on TextVQA, consistent with the mechanism enabling native aspect ratio processing (moderate evidence: two model sizes, three benchmarks, validation sets only).

#### Vision -- Comparison with PaliGemma 2 (Table 12, fine-tuned, without P&S)

| Benchmark | PaliGemma 2 27B | Gemma 3 27B |
|-----------|-----------------|-------------|
| DocVQA | 85.1 | 89.5 |
| InfoVQA | 50.2 | 64.6 |
| TextVQA | 75.1 | 83.2 |
| ChartQA | 71.3 | 83.4 |
| AI2D | 84.6 | 86.5 |
| VQAv2 | 85.8 | 85.1 |
| COCO caption | 145. | 144. |

Gemma 3 excels on document understanding benchmarks while PaliGemma 2 retains slight advantages on VQAv2 and COCO caption (moderate evidence: after fine-tuning protocol matching, three model sizes).

#### Vision Encoder Resolution (Table 7, 2B short-schedule model)

| Resolution | DocVQA | InfoVQA | TextVQA |
|------------|--------|---------|---------|
| 256 | 31.9 | 23.1 | 44.1 |
| 448 | 45.4 | 31.6 | 53.5 |
| 896 | 59.8 | 33.7 | 58.0 |

Higher resolution consistently improves performance, justifying the 896x896 choice (limited evidence: single 2B model, three benchmarks, short schedule).

#### Multilingual Performance (Table 13, pre-trained models)

| Benchmark | Gemma 2 27B | Gemma 3 27B |
|-----------|-------------|-------------|
| MGSM | 68.0 | 74.3 |
| Global MMLU | 69.4 | 75.7 |
| WMT24++ | 53.0 | 55.7 |
| FLoRes | 44.3 | 48.8 |
| XQuAD | 73.9 | 76.8 |
| ECLeKTic | 17.1 | 24.4 |
| IndicGenBench | 62.1 | 63.4 |

Consistent multilingual improvements across all benchmarks, with the largest gain on ECLeKTic (+7.3 points) reflecting the expanded multilingual data and new tokenizer (moderate evidence: pre-trained model comparison across 7 multilingual benchmarks).

#### Pre-trained Model Quality (Tables 9-10, selected highlights)

| Benchmark | Gemma 2 27B | Gemma 3 27B |
|-----------|-------------|-------------|
| HellaSwag | 86.4 | 85.6 |
| TriviaQA | 83.8 | 85.5 |
| BBH | 74.8 | 77.7 |
| MMLU | 75.2 | 78.6 |
| GSM8K | 74.6 | 82.6 |
| MATH | 42.1 | 50.0 |

Pre-trained model quality is maintained or improved despite the addition of vision, with notable STEM improvements (MATH: +7.9, GSM8K: +8.0) and slight regressions on some commonsense benchmarks (HellaSwag: -0.8) (strong evidence: consistent pattern across all model sizes in Tables 9-10).

---

## Limitations and Failure Modes

1. **Long context degradation beyond 128K.** Models generalize to 128K but rapidly degrade at longer contexts (Figure 7, Section 5.3). No evaluation is provided beyond 128K.

2. **1B model lacks vision and 128K context.** The smallest model has no vision encoder and only 32K context, limiting its applicability in multimodal or long-context settings.

3. **RULER/MRCR significant drop at 128K.** RULER 128K performance drops substantially from 32K (e.g., 27B IT: 91.1% at 32K vs 66.0% at 128K; 12B IT: 80.3% at 32K vs 57.1% at 128K; Table 15). MRCR shows a similar pattern.

4. **IT models degrade on long-context benchmarks relative to PT models.** RULER 128K: 12B PT achieves 80.7 vs 12B IT 57.1; 27B PT achieves 72.9 vs 27B IT 66.0 (Table 15). Post-training may impair long-context retrieval.

5. **Contamination risk acknowledged.** "There is always a risk of contamination of these probes, making more definitive conclusions harder to assess" (Section 5.1, citing Mirzadeh et al., 2024).

6. **Chatbot Arena numbers preliminary.** Elo scores are "preliminary results received on March 8, 2025" (Table 5 caption).

7. **No direct comparison with external models.** The authors do not run external models in their evaluation settings, noting that "running them in their setting does not guarantee a fair comparison" (Section 4.2). This limits cross-paper comparability.

8. **[Inferred]** KV cache ablations conducted only on 2B text-only models. It is unclear whether the perplexity-quality trade-offs of 5:1 interleaving hold at 12B and 27B scale or with multimodal inputs.

9. **[Inferred]** No variance estimates or confidence intervals reported for any benchmark results (except Chatbot Arena Elo 95% CI).

10. **[Inferred]** Freezing the vision encoder limits vision-language integration depth; the encoder cannot adapt to the specific language model's representation space during training.

### Scope and Comparability

- **What was not tested:** Models larger than 27B; dense models with full global attention as a baseline at 128K context; MoE architectures; downstream task evaluation of the local-global interleaving trade-off (only perplexity was measured in ablations); unfrozen vision encoder variants.
- **Comparability notes:** The authors explicitly discourage direct comparison with external models due to differing evaluation settings and encourage using third-party leaderboards instead. KV cache overhead percentages (Figure 5) are specific to the 2B model at 32K context and should not be extrapolated to other sizes without verification. Pre-trained benchmarks (Tables 9-10) use n-shot settings described in Table 19, while IT benchmarks (Table 6, 18) use 0-shot settings described in Table 21 -- these settings differ and results should not be mixed.

---

## Conclusions

### Contributions

1. **KV cache efficient long context via local-global interleaving.** The 5:1 local-to-global ratio with 1024-token sliding window reduces KV cache overhead from ~60% to <15% at 32K context with perplexity change within +/-0.1 (Figure 5, Section 5.2). This is the key architectural innovation enabling practical long-context deployment on consumer hardware.

2. **128K context open models via RoPE rescaling.** Gemma 3 4B, 12B, 27B support 128K context through RoPE rescaling (factor 8) and increased base frequency (1M for global layers), achieving 91.1% on RULER 32K and 66.0% on RULER 128K for the 27B IT model (Table 15).

3. **Multimodal capability with efficient integration.** Shared frozen 400M SigLIP encoder with 256-token compression per image, providing approximately 10x transfer cost savings compared to PaliGemma 2 (Section 5.5). Pan & Scan provides +4.8 to +17.0 point improvements on document understanding tasks (Table 8).

4. **Significantly reduced memorization.** Gemma 3 models memorize long-form text at rates around 0.001-0.01% (log scale), substantially lower than prior Gemma and Gemini models (~1%), with no personal information detected in memorized outputs (Figure 9, Section 6).

5. **Strong performance at smaller scale.** Gemma 3 27B IT achieves Elo 1338 on Chatbot Arena, outperforming much larger models including DeepSeek-V3 (671B/37B MoE, Elo 1318), LLaMA 3.1 405B (Elo 1269), and Qwen2.5-72B (Elo 1257) (Table 5).

6. **Improved multilingual capabilities.** Consistent gains across 7 multilingual benchmarks relative to Gemma 2, supported by the new Gemini 2.0 tokenizer (262K vocabulary, more balanced for non-English) and expanded multilingual training data (Tables 13-14).

### Implications

1. **Local-global interleaving may enable practical long-context deployment.** The dramatic KV cache reduction suggests dense models can support long context on consumer hardware without sparse attention approximations. However, quality ablations are demonstrated only on 2B text-only models at 32K context.

2. **Distillation from larger teachers is effective for longer training.** Ablations show the crossover at ~30-40B tokens where larger teachers become preferable (Figure 8), contrary to some prior findings. This has implications for compute-optimal distillation strategies.

3. **Frozen vision encoders are a viable strategy.** Freezing the vision encoder preserves text capabilities while adding multimodal understanding, though this approach may limit vision-language integration depth (speculative -- no unfrozen comparison is provided).

4. **Post-training may trade off long-context capability.** The consistent IT degradation relative to PT on RULER and MRCR (Table 15) suggests that instruction tuning may need specialized long-context preservation strategies.

---

## Key Claims

1. **5:1 local-global interleaving reduces KV cache overhead with minimal quality loss.** From ~60% to <15% at 32K context (Figure 5). Perplexity change is within +/-0.1 even with 7:1 ratio (Figure 3). Sliding window can be reduced from 4096 to 512 within +/-0.01 perplexity (Figure 4). Evidence: Figures 3-6, Section 5.2. Status: **supported**. Scope: 2B text-only model ablations at 32K context. Magnitude: ~45 percentage point reduction in KV cache overhead.

2. **Gemma 3 27B IT ranks 9th on Chatbot Arena with Elo 1338.** Above DeepSeek-V3 (1318, +20), LLaMA 3.1 405B (1269, +69), Qwen2.5-72B (1257, +81), and 118 Elo points above Gemma 2 27B (1220). Evidence: Table 5. Status: **supported**. Scope: preliminary results as of March 8, 2025; does not reflect vision capabilities. Magnitude: Elo 1338 (single leaderboard snapshot).

3. **Gemma 3 models memorize at significantly lower rates than prior models.** Memorization rates around 0.001-0.01% (log scale) vs up to ~1% for prior models. No personal information detected using Google Cloud SDP. Evidence: Figure 9, Section 6. Status: **supported**. Scope: exact and approximate memorization with 50-token prefix/suffix. Magnitude: approximately two orders of magnitude reduction; ~24x relative increase in approximate vs exact memorization.

4. **Gemma 3 4B IT is competitive with Gemma 2 27B IT, and Gemma 3 27B IT is comparable to Gemini 1.5 Pro.** Gemma 3 27B IT surpasses Gemini 1.5 Pro on MATH (89.0 vs 86.5) and HiddenMath (60.3 vs 52.0) but falls short on GPQA Diamond (42.4 vs 59.1) and MMLU-Pro (67.5 vs 75.8). Evidence: Table 6, Abstract. Status: **supported**. Scope: zero-shot IT benchmarks with Google-internal evaluation settings. Magnitude: +10.6 MMLU-Pro improvement over Gemma 2 27B (67.5 vs 56.9); mixed results vs Gemini 1.5 Pro.

5. **Sliding window size can be reduced to 1024 tokens without significant perplexity impact.** Perplexity change within +/-0.01 across window sizes 512-4096 at both 1:1 and 3:1 local:global ratios. Evidence: Figure 4, Section 5.2. Status: **supported**. Scope: 2B text-only model ablations. Magnitude: +/-0.01 perplexity across 8x window size range.

6. **Pan & Scan improves document understanding tasks substantially.** +4.8 to +8.2 on DocVQA, +12.9 to +17.0 on InfoVQA, +1.6 to +1.9 on TextVQA. Evidence: Table 8, Section 5.5. Status: **supported**. Scope: 4B and 27B models on validation sets, 4-shot evaluation. Magnitude: up to +17.0 points on InfoVQA.

7. **RoPE rescaling enables 128K context after 32K pre-training.** Models generalize to 128K (perplexity stable) but rapidly degrade beyond. Evidence: Figure 7, Section 5.3. Status: **supported**. Scope: 4B, 12B, 27B models, perplexity evaluation. Magnitude: RULER 27B IT drops from 91.1% (32K) to 66.0% (128K); perplexity remains stable through 128K then increases sharply.

8. **Larger teachers become preferable for longer training horizons in distillation.** Delta perplexity shifts from ~+0.002 (smaller teacher better) to ~-0.006 (larger teacher better) as training tokens increase. Crossover at approximately 30-40B tokens. Evidence: Figure 8, Section 5.4. Status: **supported**. Scope: single 2B student with two teacher sizes (limited evidence: one student size). Magnitude: ~0.008 perplexity spread between extremes.

---

## Open Questions

1. **Multi-hop reasoning at 128K.** How well can models reason over information distributed throughout the full 128K context, not just retrieve it? The RULER and MRCR drops from 32K to 128K (Table 15) suggest degradation but the nature of failure modes is not analyzed.

2. **Local-global pattern for MoE.** Would the 5:1 interleaving pattern transfer to MoE architectures, which already have sparse computation?

3. **Root cause of reduced memorization.** Is the significantly lower memorization rate attributable to architectural changes (local-global interleaving), training data curation, distillation, or some combination? The paper does not isolate the contributing factor.

4. **Vision encoder fine-tuning.** Would unfreezing the vision encoder during training improve vision-language integration, and at what cost to text performance? The current approach of freezing the encoder is pragmatic but may limit multimodal capability.

5. **Beyond 128K context.** What modifications would be needed to extend beyond 128K without the rapid perplexity degradation observed in Figure 7? The current RoPE rescaling factor of 8 appears to have a hard ceiling.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Base Transformer architecture that Gemma 3 builds upon as a decoder-only variant.
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Grouped-Query Attention mechanism used across all Gemma 3 models.
- **Zhang and Sennrich (2019)** -- *Root Mean Square Layer Normalization.* RMSNorm used for training stability with both pre-norm and post-norm.
- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Sliding window self-attention pattern adapted for the local attention layers in Gemma 3's 5:1 interleaving.

### Direct Predecessors

- **Gemma Team (2024a)** -- *Gemma: Open Models Based on Gemini Research and Technology.* First-generation Gemma establishing architecture foundations and 8K context.
- **Gemma Team (2024b)** -- *Gemma 2: Improving Open Language Models at a Practical Size.* Direct predecessor with 1:1 local-global ratio, soft-capping, and 8K context; provides the memorization measurement methodology.

### Context Extension

- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* RoPE rescaling approach adapted for extending global attention span from 32K to 128K in Gemma 3.

### Vision Integration

- **Zhai et al. (2023)** -- *SigLIP: Sigmoid Loss for Language Image Pre-Training.* Vision encoder architecture (400M variant) used across all multimodal Gemma 3 models.
- **Liu et al. (2024)** -- *LLaVA: Visual Instruction Tuning.* Pan & Scan approach inspired by LLaVA's handling of varying resolutions and aspect ratios.
- **Steiner et al. (2024)** -- *PaliGemma 2: A Family of Versatile VLMs for Transfer.* Fine-tuning protocol used for multimodal benchmark comparison (Table 12).

### Pre-Training and Distillation

- **Hinton et al. (2015)** -- *Distilling the Knowledge in a Neural Network.* Foundation for both pre-training and post-training distillation approach.
- **Sachdeva et al. (2024)** -- *How to Train Data-Efficient LLMs.* Quality reweighting step used in data filtering during pre-training.

### Post-Training

- **Sessa et al. (2024)** -- *BOND: Aligning LLMs with Best-of-N Distillation.* RL finetuning method used in post-training.
- **Rame et al. (2024a,b)** -- *WARP and WARM.* Weight averaging methods for reward models (WARM) and policies (WARP) used in RL finetuning.
- **Gehring et al. (2024)** -- *RLEF: Grounding Code LLMs in Execution Feedback.* Code execution feedback used as reward signal in RL finetuning.

### Long-Context Evaluation

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Multi-task synthetic long-context benchmark used for 32K and 128K evaluation.
- **Vodrahalli et al. (2024)** -- *MRCR (Michelangelo).* Long-context evaluation beyond needle-in-haystack, used alongside RULER at 32K and 128K.

### Training Stability

- **Dehghani et al. (2023)** -- *Scaling Vision Transformers to 22 Billion Parameters.* Inspiration for QK-norm, which replaces soft-capping from Gemma 2.
- **Wortsman et al. (2023)** -- *Small-Scale Proxies for Large-Scale Transformer Training Instabilities.* Additional inspiration for QK-norm adoption.
