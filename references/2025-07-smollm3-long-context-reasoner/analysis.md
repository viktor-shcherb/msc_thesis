---
title: "SmolLM3: smol, multilingual, long-context reasoner"
authors: "Bakouch, Patino, Lozhkov, Beeching, Roucher, Tazi, Reedi, Penedo, Kydlicek, Fourrier, Habib, Rasul, Gallouedec, Larcher, Morlon, Lochner, Srivastav, Nguyen, Raffel, Tunstall, Ben Allal, von Werra, Wolf"
year: 2025
venue: "Hugging Face Blog 2025"
paper_type: informal
categories: ["model-release", "context-extension", "architecture"]
scope: ["3B parameter scale", "6 European languages", "128K context via YARN extrapolation"]
benchmarks_used: ["ruler", "helmet", "hellaswag", "arc", "winogrande", "csqa", "mmlu", "mmlu-pro", "piqa", "openbookqa", "boolq", "humaneval", "mbpp", "math-hendrycks", "gsm8k", "aime-2025", "gpqa", "ifeval", "mixeval", "livecodebench", "gsm-plus", "bfcl", "global-mmlu", "belebele", "flores-200"]
models_introduced: ["smollm3-3b"]
models_evaluated: ["smollm3-3b", "qwen2.5-3b", "llama-3.2-3b", "qwen3-1.7b", "qwen3-4b"]
key_claims:
  - id: C1
    claim: "SmolLM3-3B outperforms Llama 3.2 3B and Qwen2.5 3B across most benchmarks while being competitive with 4B models"
    evidence: "Base model benchmark tables, instruct model benchmark tables, source 01 and 03"
    status: supported
    scope: "3B scale, English benchmarks, zero-shot base model evaluation"
    magnitude: "Best or second-best among 3B class on HellaSwag (76.15), ARC-CF (65.61), BoolQ (78.99), PIQA (78.89)"
  - id: C2
    claim: "Two-stage RoPE theta scaling with NoPE layers achieves competitive long-context performance up to 64K without specialized long-context data"
    evidence: "Long context extension section, source 01"
    status: supported
    scope: "3B scale, RULER benchmark, two-stage 50B+50B token training"
    magnitude: "RULER 32K: 76.35, RULER 64K: 67.85, RULER 128K: 61.03"
  - id: C3
    claim: "Extended thinking mode provides substantial improvements on reasoning benchmarks"
    evidence: "Instruct model benchmark tables, source 01 and 03"
    status: supported
    scope: "3B scale, AIME/LiveCodeBench/GPQA benchmarks, compared to same model without thinking"
    magnitude: "AIME 2025: +27.4 pp (9.3 to 36.7), LiveCodeBench v4: +14.8 pp (15.2 to 30.0), GPQA Diamond: +6.0 pp (35.7 to 41.7)"
  - id: C4
    claim: "Model merging (0.9 APO + 0.1 mid-training) recovers long-context performance lost during alignment"
    evidence: "Model Merging section, source 01"
    status: supported
    scope: "3B scale, RULER benchmark, linear merge with MergeKit"
    magnitude: "Recovered base model RULER performance on contexts up to 128K tokens"
  - id: C5
    claim: "SmolLM3 leads among 3B models on multilingual commonsense reasoning (MLMM HellaSwag) across all 5 primary non-English languages"
    evidence: "Multilingual benchmark tables, source 03 and 04"
    status: supported
    scope: "French, Spanish, German, Italian, Portuguese; MLMM HellaSwag metric"
    magnitude: "French: 63.94, Spanish: 65.85, German: 59.56, Italian: 62.49, Portuguese: 63.22 (all best in 3B class)"
  - id: C6
    claim: "Anchored Preference Optimization (APO) achieves higher downstream performance than standard DPO"
    evidence: "APO section, source 01"
    status: unvalidated
    scope: "3B scale, internal ablations only"
    magnitude: "qualitative (specific numbers not reported)"
  - id: C7
    claim: "Upsampling specialized long-context data did not boost RULER/HELMET scores beyond using NoPE + increased RoPE theta on the decay mixture"
    evidence: "Long context extension section, source 01"
    status: unvalidated
    scope: "3B scale, ablation during long-context training"
    magnitude: "qualitative (ablation result, specific numbers not reported)"
cross_references:
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "SmolLM3 uses YARN for extrapolation from 64K training length to 128K inference, following Qwen2.5's approach"
  - target: 2023-12-gqa-grouped-query-attention
    type: extends
    detail: "SmolLM3 adopts GQA with 4 groups, validated via ablations showing matching MHA performance with reduced KV cache"
  - target: 2024-10-ruler-context-size
    type: uses-benchmark
    detail: "RULER used as primary long-context evaluation benchmark at 32K, 64K, and 128K"
  - target: 2025-04-helmet-long-context-evaluation
    type: uses-benchmark
    detail: "HELMET used alongside RULER for long-context evaluation during ablations"
  - target: 2025-05-qwen3-technical-report
    type: evaluates
    detail: "Qwen3-1.7B and Qwen3-4B used as primary comparison baselines for both reasoning and non-reasoning modes"
  - target: 2026-01-ministral-3-cascade-distillation
    type: concurrent
    detail: "Both are 3B-scale open model releases targeting efficient deployment with strong capabilities"
  - target: 2025-03-gemma-3-technical-report
    type: concurrent
    detail: "Gemma 3 4B competes in the same small-model space; not directly evaluated but referenced as 4B competitor"
open_questions:
  - question: "How does SmolLM3's long-context performance degrade beyond 128K tokens, and what are the limits of YARN extrapolation at 3B scale?"
    addressed_by: null
  - question: "Would the NoPE (RoPE removal every 4th layer) strategy transfer effectively to larger model scales?"
    addressed_by: null
  - question: "What is the quantitative performance gap between APO and standard DPO that motivated the choice? Internal ablation numbers are not reported."
    addressed_by: null
  - question: "How does the reasoning mid-training and alignment pipeline interact with long-context capabilities at longer sequences (beyond the 24K token limit of APO data)?"
    addressed_by: null
  - question: "Would training on genuine long-context reasoning traces (beyond 24K tokens) recover the RULER degradation without requiring model merging?"
    addressed_by: null
---

# SmolLM3: smol, multilingual, long-context reasoner

**Authors:** Elie Bakouch, Carlos Miguel Patino, Anton Lozhkov, Edward Beeching, Aymeric Roucher, Nouamane Tazi, Aksel Joonas Reedi, Guilherme Penedo, Hynek Kydlicek, Clementine Fourrier, Nathan Habib, Kashif Rasul, Quentin Gallouedec, Hugo Larcher, Mathieu Morlon, Joshua Lochner, Vaibhav Srivastav, Xuan-Son Nguyen, Colin Raffel, Lewis Tunstall, Loubna Ben Allal, Leandro von Werra, Thomas Wolf (Hugging Face)
**Date:** July 2025
**Type:** Blog post (not a formal peer-reviewed paper)
**URL:** https://huggingface.co/blog/smollm3

SmolLM3 is the third iteration of the SmolLM family. The predecessor SmolLM2 has a formal arXiv paper (Allal et al., arXiv:2502.02737), but SmolLM3 was released solely as a blog post with accompanying model cards, training configurations, and dataset documentation on Hugging Face Hub.

---

## Core Research Problem

Small language models (1B--4B parameters) face a difficult tradeoff between model capability and deployment efficiency. At the 3B scale, prior open models like Llama 3.2 3B and Qwen2.5 3B demonstrated reasonable performance but fell short on reasoning, long-context handling, and multilingual competence simultaneously. Achieving competitive performance with larger 4B models (Qwen3-4B, Gemma 3 4B) while maintaining the computational efficiency of 3B scale remained an open challenge.

Specific gaps included: (1) limited context windows (Llama 3.2 3B supported only 128K via external extensions), (2) no native dual-mode reasoning support at the 3B scale, (3) constrained multilingual capability relative to larger models, and (4) opaque training recipes that limited reproducibility. **The core challenge is how to train a fully-open 3B model that simultaneously achieves strong reasoning, 128K context, and multilingual capability while remaining competitive with 4B alternatives.**

---

## Problem Solutions

SmolLM3 addresses these challenges through a **multi-stage training pipeline** combining architectural choices, curriculum design, and post-training strategies:

1. **Architecture optimizations**: Grouped Query Attention (GQA, 4 groups) for KV cache reduction, and NoPE (removal of RoPE from every 4th layer) for improved long-context handling without short-context degradation.
2. **Three-stage pretraining curriculum**: 11.2T tokens across web, code, and math data with progressive quality upsampling (85%/12%/3% web/code/math in Stage 1 to 63%/24%/13% in Stage 3).
3. **Two-stage long-context extension**: 100B tokens total, extending from 4K to 32K (RoPE theta 1.5M) then 32K to 64K (RoPE theta 5M), with YARN extrapolation enabling 128K inference.
4. **Reasoning mid-training**: 140B tokens (4 epochs over 35B token dataset) on reasoning traces from OpenThoughts3 and Llama-Nemotron datasets.
5. **Post-training with APO and model merging**: SFT followed by Anchored Preference Optimization, then linear merge with mid-training checkpoint (0.9 APO + 0.1 mid-training) to recover long-context performance.

---

## Approach Details

### Method

SmolLM3 uses a **decoder-only Transformer** architecture with tied embeddings, building on the Llama architecture. The model has **3 billion parameters** and is trained in bfloat16 precision.

**Grouped Query Attention (GQA)** replaces standard multi-head attention with **4 attention groups**, reducing KV cache size while matching multi-head attention performance. This was validated via ablations on a 3B model trained on 100B FineWeb-Edu tokens (source 01).

**NoPE (No Position Embeddings)** selectively removes rotary position embeddings from every 4th layer, following Yang et al. (2025). Per the blog post:

> "Improves long context performance without affecting short context"

**Intra-document masking** prevents tokens from different documents within the same training sequence from attending to each other, following the approach from "Analysing The Impact of Sequence Composition on Language Model Pre-Training" (arXiv:2402.13991) and Llama 3:

> "This helps with faster and more stable long context training while maintaining short context performance"

**Training stability**: Following OLMo 2, weight decay is removed from embedding layers, allowing embedding norms to stabilize at healthier values.

### Key Technical Components

**Pretraining curriculum (11.2T tokens, 3 stages)**:

| Stage | Tokens | Web | Code | Math | Key Changes |
|-------|--------|-----|------|------|-------------|
| Stage 1 (Stable) | 0T--8T | 85% (12% multilingual) | 12% | 3% | Foundation: FineWeb-Edu, DCLM, FineWeb2, The Stack v2 |
| Stage 2 (Stable) | 8T--10T | 75% (12% multilingual) | 15% | 10% | Higher quality: Stack-Edu, FineMath4+, MegaMath |
| Stage 3 (Decay) | 10T--11.1T | 63% (12% multilingual) | 24% | 13% | Math/code upsampling + OpenMathReasoning |

**Long-context extension (100B tokens, 2 stages)**:

| Stage | Context | Tokens | RoPE theta |
|-------|---------|--------|-----------|
| LC Stage 1 | 4K to 32K | 50B | 1.5M |
| LC Stage 2 | 32K to 64K | 50B | 5M |

A key ablation finding: upsampling specific long-context data (repositories, books, long web pages) did not boost RULER/HELMET benchmarks beyond using the existing decay mixture with longer sequences and increased RoPE theta values (source 01, limited evidence -- specific ablation numbers not reported).

**Inference extrapolation**: YARN (following Qwen2.5) is used for extrapolation beyond 64K training length to **128K inference context** (2x extension). The config specifies:

```json
{"rope_scaling": {"factor": 2.0, "original_max_position_embeddings": 65536, "type": "yarn"}}
```

**Reasoning mid-training (140B tokens)**:

- Dataset: 35B tokens total from OpenThoughts3-1.2M and a subset of Llama-Nemotron-Post-Training-Dataset-v1.1 with R1 reasoning traces
- Training: 4 epochs (~140B tokens)
- Chat template: ChatML
- Packing: Wrapped packing to avoid excessive structure

**Supervised Fine-Tuning (1.8B tokens)**:

- Non-reasoning mode: 1B tokens across 12 datasets
- Reasoning mode: 0.8B tokens across 10 datasets with reasoning traces
- Synthetic data: Generated via Qwen3-32B in reasoning mode to fill domain gaps (multi-turn, multilingual, everyday conversations)
- Training: 4 epochs (~8B tokens total), BFD packing, loss masked on user turns and tool call results

**Anchored Preference Optimization (APO)**:

APO is described as a variant of DPO with a more stable optimization objective. The DPO reward function is:

> r_theta(x,y) = beta * log(pi_theta(y|x) / pi_ref(y|x))

> L_DPO = -E[(x,y_w,y_l)] log sigma(beta * log(pi_theta(y_w|x)/pi_ref(y_w|x)) - beta * log(pi_theta(y_l|x)/pi_ref(y_l|x)))

Preference data sources:
- Non-reasoning: Tulu3 preference dataset
- Reasoning: Synthetic pairs from Qwen3-32B (chosen) vs Qwen3-0.6B (rejected)

**Model merging (post-APO recovery)**:

Alignment training degraded long-context performance (RULER), traced to reasoning mid-training data being limited to sequences below 24K tokens. Recovery via MergeKit linear merge:

- **Weights**: 0.9 (APO checkpoint soup) + 0.1 (mid-training checkpoint with strong long-context performance)
- **Result**: Recovered base model RULER performance on contexts up to 128K tokens

**Tokenizer**: Uses Llama 3.2 tokenizer (128K vocabulary) without the `bos_token`. 100K tokens from tiktoken3 + 28K additional non-English language tokens. Character compression: **3.94 characters/token** on English (vs 3.17 for Llama 2).

### Experimental Setup

**Hardware**: 384 H100 GPUs, 24 days of pretraining.

**Frameworks**: nanotron (training), datatrove (data processing), lighteval (evaluation), TRL (post-training).

**Models compared**:
- Same scale: Qwen2.5 3B, Llama 3.2 3B (base and instruct)
- Smaller: Qwen3 1.7B
- Larger: Qwen3 4B, Gemma 3 4B

**Evaluation benchmarks**:
- Base model English: HellaSwag, ARC-CF, Winogrande, CommonsenseQA, MMLU-CF, MMLU Pro CF, MMLU Pro MCF, PIQA, OpenBookQA, BoolQ, HumanEval+, MBPP+, MATH (4-shot), GSM8K (5-shot), RULER (32K/64K/128K)
- Base model multilingual: MLMM HellaSwag, Belebele, Global MMLU (CF), Flores-200 (5-shot) across 6 primary and 3 additional languages
- Instruct no-thinking: AIME 2025, GSM-Plus, LiveCodeBench v4, GPQA Diamond, IFEval, MixEval Hard, BFCL, Global MMLU
- Instruct thinking: Same benchmarks as no-thinking mode, compared against Qwen3-1.7B and Qwen3-4B

**Reproducibility**: Fully open weights (Apache 2.0), training configs released on HuggingFace, intermediate checkpoints available, training logs on W&B. Post-training data (SmolTalk2) released. Code available at github.com/huggingface/smollm. Requires transformers v4.53.0+. No variance estimates reported for any benchmark results (single-run evaluations). No seeds reported.

### Key Results

**Base model -- English benchmarks (zero-shot unless noted)**:

| Benchmark | SmolLM3-3B | Qwen2.5-3B | Llama 3.2-3B | Qwen3-1.7B-Base | Qwen3-4B-Base |
|-----------|-----------|-----------|-------------|-----------------|--------------|
| HellaSwag | **76.15** | 74.19 | 75.52 | 60.52 | 74.37 |
| ARC-CF (Avg) | **65.61** | 59.81 | 58.58 | 55.88 | 62.11 |
| Winogrande | 58.88 | **61.41** | 58.72 | 57.06 | 59.59 |
| CommonsenseQA | 55.28 | 49.14 | **60.60** | 48.98 | 52.99 |
| MMLU-CF (Avg) | 44.13 | 42.93 | 41.32 | 39.11 | **47.65** |
| MMLU Pro CF | 19.61 | 16.66 | 16.42 | 18.04 | **24.92** |
| PIQA | **78.89** | 78.35 | 78.51 | 75.35 | 77.58 |
| BoolQ | **78.99** | 73.61 | 75.33 | 74.46 | 74.28 |
| HumanEval+ | 30.48 | 34.14 | 25.00 | 43.29 | **54.87** |
| MBPP+ | 52.91 | 52.11 | 38.88 | 59.25 | **63.75** |
| MATH (4-shot) | 46.10 | 40.10 | 7.44 | 41.64 | **51.20** |
| GSM8K (5-shot) | 67.63 | 70.13 | 25.92 | 65.88 | **74.14** |
| RULER 32K | 76.35 | 75.93 | 77.58 | 70.63 | **83.98** |
| RULER 64K | 67.85 | 64.90 | **72.93** | 57.18 | 60.29 |
| RULER 128K | 61.03 | 62.23 | **71.30** | 43.03 | 47.23 |

- SmolLM3 achieves **best-in-3B-class** on HellaSwag, ARC-CF, BoolQ, PIQA (source 03, 04).
- Llama 3.2 3B leads on RULER 64K and 128K, indicating stronger long-context retention at these lengths.
- Qwen3-4B-Base (a 4B model) leads overall on knowledge and math benchmarks.
- SmolLM3's MATH 4-shot (46.10) strongly outperforms Llama 3.2 3B (7.44) and Qwen2.5 3B (40.10).

**Instruct model -- no extended thinking**:

| Benchmark | SmolLM3-3B | Qwen2.5-3B | Llama 3.1-3B | Qwen3-1.7B | Qwen3-4B |
|-----------|-----------|-----------|-------------|-----------|----------|
| AIME 2025 | 9.3 | 2.9 | 0.3 | 8.0 | **17.1** |
| GSM-Plus | 72.8 | 74.1 | 59.2 | 68.3 | **82.1** |
| LiveCodeBench v4 | 15.2 | 10.5 | 3.4 | 15.0 | **24.9** |
| GPQA Diamond | 35.7 | 32.2 | 29.4 | 31.8 | **44.4** |
| IFEval | **76.7** | 65.6 | 71.6 | 74.0 | 68.9 |
| MixEval Hard | 26.9 | 27.6 | 24.9 | 24.3 | **31.6** |
| BFCL | 92.3 | - | 92.3* | 89.5 | **95.0** |
| Global MMLU | 53.5 | 50.54 | 46.8 | 49.5 | **65.1** |

*Llama 3.1-3B uses a tool-calling finetune.

- SmolLM3 achieves **best IFEval** (76.7) across all models including the larger Qwen3-4B (68.9), indicating strong instruction-following capability (source 03).
- Competitive with Qwen3-1.7B across most metrics despite the parameter advantage.

**Instruct model -- extended thinking (reasoning mode)**:

| Benchmark | SmolLM3-3B | Qwen3-1.7B | Qwen3-4B |
|-----------|-----------|-----------|----------|
| AIME 2025 | 36.7 | 30.7 | **58.8** |
| GSM-Plus | 83.4 | 79.4 | **88.2** |
| LiveCodeBench v4 | 30.0 | 34.4 | **52.9** |
| GPQA Diamond | 41.7 | 39.9 | **55.3** |
| IFEval | 71.2 | 74.2 | **85.4** |
| MixEval Hard | 30.8 | 33.9 | **38.0** |
| BFCL | 88.8 | 88.8 | **95.5** |
| Global MMLU | 64.1 | 62.3 | **73.3** |

- Thinking mode provides large gains on AIME 2025 (+27.4 pp) and LiveCodeBench v4 (+14.8 pp).
- SmolLM3 outperforms Qwen3-1.7B on AIME (36.7 vs 30.7), GSM-Plus (83.4 vs 79.4), and GPQA Diamond (41.7 vs 39.9) in thinking mode.
- Qwen3-1.7B surpasses SmolLM3 on LiveCodeBench (34.4 vs 30.0) in thinking mode despite being smaller.
- Qwen3-4B leads substantially across all thinking-mode benchmarks.

**Multilingual base model -- MLMM HellaSwag (5 primary languages)**:

| Language | SmolLM3-3B | Qwen2.5-3B | Llama 3.2-3B | Qwen3-1.7B | Qwen3-4B |
|----------|-----------|-----------|-------------|-----------|----------|
| French | **63.94** | 57.47 | 57.66 | 51.26 | 61.00 |
| Spanish | **65.85** | 58.25 | 59.39 | 52.40 | 61.85 |
| German | **59.56** | 49.99 | 53.19 | 46.10 | 56.43 |
| Italian | **62.49** | 53.21 | 54.96 | 48.72 | 58.76 |
| Portuguese | **63.22** | 57.38 | 56.84 | 50.73 | 59.89 |

- SmolLM3 leads MLMM HellaSwag in all 5 primary non-English languages, even outperforming the larger Qwen3-4B (source 03, 04).

---

## Limitations and Failure Modes

- **Long-context performance**: SmolLM3 trails Llama 3.2 3B at RULER 64K (67.85 vs 72.93) and RULER 128K (61.03 vs 71.30), despite using YARN extrapolation (source 03, 04). The 128K gap of ~10 points is substantial.
- **Alignment-context tradeoff**: Reasoning mid-training and APO alignment degraded long-context performance (RULER), requiring a model merging recovery step. The APO preference data was limited to 24K tokens (source 01).
- **LiveCodeBench in thinking mode**: SmolLM3 (30.0) underperforms the smaller Qwen3-1.7B (34.4) in reasoning mode on competitive programming (source 03).
- **Knowledge benchmarks**: Qwen3-4B-Base substantially outperforms SmolLM3 on MMLU-CF (47.65 vs 44.13), MMLU Pro CF (24.92 vs 19.61), and code benchmarks (HumanEval+ 54.87 vs 30.48), indicating the 4B scale advantage remains meaningful (source 03, 04).
- **No variance estimates**: All benchmark results appear to be single runs without reported variance, seeds, or statistical testing (limited evidence for precise score comparisons).
- **Factual accuracy and bias**: The model card explicitly notes SmolLM3 may produce factually inaccurate content, logically inconsistent outputs, and content reflecting training data biases (source 03, 04).
- **[Inferred]** APO performance improvement over DPO is claimed based on internal ablations but no quantitative results are reported, making the claim unverifiable from public information.
- **[Inferred]** The NoPE ablation is described qualitatively ("improves long context performance without affecting short context") without specific benchmark numbers for the ablation, limiting reproducibility of the architectural decision.
- **[Inferred]** No evaluation on Asian or African languages despite the tokenizer containing 28K non-English tokens. The 3 additional languages tested (Arabic, Chinese, Russian) show weaker performance relative to competitors.

#### Scope and Comparability

- **What was not tested**: No evaluation beyond 128K context. No perplexity-based evaluation. No evaluation on summarization, multi-document QA, or other complex long-context tasks beyond RULER. No head-to-head comparison with Gemma 3 4B on the same benchmark suite. No evaluation of the model merging impact on short-context tasks beyond the benchmarks reported.
- **Comparability notes**: The blog post uses "Llama3.1-3B" and "Llama3.2-3B" interchangeably in different tables, which may reflect different base models or instruct variants (source 03 vs 04). The BFCL result for Llama 3.1 3B (92.3*) uses a tool-calling finetune, not the standard instruct model, making direct comparison on tool calling imprecise. Qwen3-4B is consistently included as a competitor despite being ~33% larger, blurring the "3B class" framing. No comparison with SmolLM2 is provided, making it impossible to assess generation-over-generation improvement from public data alone.

---

## Conclusions

#### Contributions

1. **Competitive 3B model with dual-mode reasoning**: SmolLM3 demonstrates that a 3B model with 11.2T training tokens can achieve first or second place among 3B models on commonsense, reasoning, and knowledge benchmarks while supporting both fast non-reasoning and extended thinking modes (source 01, 03).

2. **Practical long-context extension recipe**: The two-stage RoPE theta scaling (1.5M then 5M) combined with NoPE layers and 100B tokens of continued pretraining achieves RULER 64K of 67.85 without requiring specialized long-context data upsampling (source 01).

3. **Model merging as alignment recovery**: The 0.9/0.1 linear merge between APO and mid-training checkpoints provides a practical method to recover long-context capabilities degraded by alignment training limited to short sequences (source 01).

4. **Fully open training recipe**: Complete transparency with released training configs, intermediate checkpoints, W&B training logs, SmolTalk2 dataset, and Apache 2.0 licensing (source 01, 02, 03, 04, 05, 06).

5. **Strong multilingual commonsense at 3B scale**: SmolLM3 leads all 3B models and even Qwen3-4B on MLMM HellaSwag across 5 European languages with only 12% multilingual data in pretraining (source 03, 04).

#### Implications

1. **Diminishing returns of specialized long-context data**: The ablation finding that long-context data upsampling did not help beyond NoPE + RoPE theta scaling suggests that architectural choices may matter more than data composition for context extension at small scale (speculative -- ablation details are limited).

2. **Alignment-context tension**: The degradation of RULER scores after reasoning mid-training and APO highlights a broader challenge: alignment pipelines trained on short sequences may systematically harm long-context capabilities, requiring post-hoc recovery strategies like model merging.

3. **3B models approaching 4B territory**: SmolLM3's competitiveness with Qwen3-4B on several metrics suggests that data scale (11.2T tokens) and training recipe may partially compensate for parameter count at this scale, though the 4B model retains clear advantages on knowledge-intensive and code tasks.

---

## Key Claims

1. **SmolLM3 outperforms Llama 3.2 3B and Qwen2.5 3B on most English benchmarks** -- Best-in-3B-class on HellaSwag (76.15), ARC-CF (65.61), BoolQ (78.99), PIQA (78.89); MATH 4-shot 46.10 vs Llama 7.44 and Qwen2.5 40.10 (source 03, 04 benchmark tables). Scope: 3B scale, English zero-shot evaluation. Status: **supported** (comprehensive benchmark suite, but single runs without variance).

2. **Two-stage RoPE theta scaling with NoPE achieves competitive long-context performance without specialized long-context data** -- RULER 32K: 76.35, RULER 64K: 67.85, RULER 128K: 61.03 (source 01, 03, 04). Scope: 3B scale, RULER benchmark, 50B+50B token training. Status: **supported** (but trails Llama 3.2 3B at 64K and 128K by 5--10 points, and the ablation showing specialized data is unnecessary is not quantitatively reported).

3. **Extended thinking provides substantial reasoning improvements** -- AIME 2025: +27.4 pp (9.3 to 36.7), LiveCodeBench v4: +14.8 pp (15.2 to 30.0), GPQA Diamond: +6.0 pp (35.7 to 41.7) (source 01, 03). Scope: 3B scale, specific benchmarks. Status: **supported** (consistent gains across all benchmarks tested, single runs).

4. **Model merging recovers long-context performance after alignment** -- 0.9 APO + 0.1 mid-training linear merge recovers base model RULER performance up to 128K (source 01). Scope: 3B scale, RULER, linear merge. Status: **supported** (limited evidence -- specific before/after merge numbers not reported beyond qualitative statement).

5. **SmolLM3 leads among 3B models on multilingual commonsense reasoning** -- Best MLMM HellaSwag across all 5 primary non-English languages (French 63.94, Spanish 65.85, German 59.56, Italian 62.49, Portuguese 63.22), even surpassing Qwen3-4B (source 03, 04). Scope: MLMM HellaSwag metric, 5 European languages. Status: **supported** (strong evidence on this specific metric, but limited to one commonsense benchmark).

6. **APO achieves higher downstream performance than standard DPO** -- Claimed based on internal ablations (source 01). Scope: 3B scale, internal testing. Status: **unvalidated** (no quantitative comparison published).

7. **Upsampling specialized long-context data does not boost RULER/HELMET beyond NoPE + RoPE theta scaling** -- Ablation result from context extension training (source 01). Scope: 3B scale, ablation during long-context training. Status: **unvalidated** (specific numbers not reported, single model scale).

---

## Open Questions

1. **How does SmolLM3's long-context performance degrade beyond 128K tokens, and what are the limits of YARN extrapolation at 3B scale?** The model is only evaluated up to 128K context with RULER. No evaluation at longer contexts is provided. Not addressed by existing references.

2. **Would the NoPE (RoPE removal every 4th layer) strategy transfer effectively to larger model scales?** The ablation was conducted only at 3B scale. Not addressed by existing references.

3. **What is the quantitative performance gap between APO and standard DPO?** Only a qualitative claim of higher performance is made; internal ablation numbers are not published. Not addressed by existing references.

4. **How does the reasoning mid-training and alignment pipeline interact with long-context capabilities at longer sequences?** APO data was limited to 24K tokens, and RULER degradation was observed. Would longer reasoning traces during alignment avoid the need for model merging? Not addressed by existing references.

5. **Would training on genuine long-context reasoning traces (beyond 24K tokens) recover the RULER degradation without requiring model merging?** The current recovery approach (model merging) is a workaround rather than a principled solution. Not addressed by existing references.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.* SmolLM3 adopts GQA with 4 groups as its attention mechanism, validated via ablations.

- **Yang et al. (2025)** -- *NoPE: No Position Embeddings.* SmolLM3 implements the RoPE-to-NoRoPE strategy of removing rotary position embeddings from every 4th layer to improve long-context performance.

### Context Extension Methods

- **Peng et al. (2024)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* SmolLM3 uses YARN for extrapolation from 64K training context to 128K inference, following Qwen2.5's implementation.

- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* Foundational work on RoPE theta scaling that informs SmolLM3's two-stage context extension approach.

### Training Methodology

- **Groeneveld et al. (2024)** -- *OLMo 2.* SmolLM3 follows OLMo 2's approach of removing weight decay from embedding layers for training stability.

- **"Analysing The Impact of Sequence Composition on Language Model Pre-Training" (arXiv:2402.13991).** Source for intra-document attention masking strategy adopted by SmolLM3.

### Comparison Models

- **Qwen Team (2025)** -- *Qwen3 Technical Report.* Qwen3-1.7B and Qwen3-4B serve as the primary comparison baselines across all evaluation modes.

- **Meta (2024)** -- *Llama 3.2.* Llama 3.2 3B is the primary same-scale competitor. Uses the Llama 3.2 tokenizer (128K vocabulary).

### Evaluation Benchmarks

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Language Models?* Primary long-context evaluation benchmark used at 32K, 64K, and 128K context lengths.

- **Yen et al. (2024)** -- *HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly.* Used alongside RULER during ablation studies for long-context evaluation.

### Post-Training

- **Lambert et al. (2024)** -- *Tulu 3.* Tulu3 preference dataset used for non-reasoning APO training data.

- **NVIDIA (2024)** -- *Llama-Nemotron-Post-Training-Dataset.* Subset with R1 reasoning traces used for reasoning mid-training.

- **Open Thought (2024)** -- *OpenThoughts3-1.2M.* Primary reasoning trace dataset for mid-training.
