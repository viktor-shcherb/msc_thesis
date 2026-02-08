---
title: "Democratizing Open and Compliant LLMs for Global Language Environments: Apertus v1 Technical Report"
authors: "Project Apertus, Hernandez-Cano, Hagele, Huang, Romanou, Solergibert, Pasztor, Messmer, Garbaya, Durech, Hakimi, Garcia Giraldo, Ismayilzada, Foroutan, Moalla, Chen, Sabolcec, Xu, Bosselut, Jaggi, Schlag"
year: 2025
venue: "arXiv 2025"
paper_type: preprint
categories: ["architecture", "model-release", "benchmarking"]
scope: ["8B and 70B dense decoder-only Transformers", "15T tokens pretraining on 1811 languages", "data compliance via retroactive robots.txt filtering and Goldfish loss", "multilingual LLM evaluation across 94 languages"]
benchmarks_used: ["mmlu", "hellaswag", "winogrande", "arc", "piqa", "gsm8k", "humaneval", "mbpp", "bbh", "truthfulqa", "ifeval", "gpqa", "toxigen", "ruler", "mgsm"]
models_introduced: ["apertus-8b", "apertus-70b"]
models_evaluated: ["llama-3.1-8b", "llama-3.1-70b", "qwen2.5-7b", "qwen2.5-72b", "qwen3-8b", "qwen3-32b"]
key_claims:
  - id: C1
    claim: "The Apertus architecture and training recipe (xIELU, AdEMAMix, QK-Norm, WSD, Goldfish loss) matches baseline training loss with 30-40% fewer tokens at 3B scale"
    evidence: "Table 3, Figure 2, Section 2.4"
    status: supported
    scope: "1.5B and 3B ablation models, 100B token runs on internal datamix"
    magnitude: "30-40% fewer tokens to reach same loss; Apertus 3B loss 1.843 vs baseline 3B loss 1.906"
  - id: C2
    claim: "Goldfish loss effectively suppresses verbatim memorization at scale while preserving downstream task performance"
    evidence: "Figure 8, Table 25, Table F.5, Section 5.4"
    status: supported
    scope: "8B and 70B models, exposure frequencies up to 128, prefix lengths up to 5000 tokens, greedy and nucleus decoding"
    magnitude: "Rouge-L remains at baseline ~0.18 regardless of exposure frequency; Goldfish 8B outperforms standard 8B on most benchmarks (Table F.5)"
  - id: C3
    claim: "Apertus-70B is the strongest pretrained fully open model on multilingual benchmarks at equivalent scale"
    evidence: "Tables 14 and 15, Figure 7, Section 5.1"
    status: supported
    scope: "Fully open models compared at 8B and 70B scale; evaluated on ARC, HellaSwag, WinoGrande, XNLI, XCOPA, PIQA, MMLU, Global-MMLU, INCLUDE, CulturalBench, BLEnD, SwitzerlandQA"
    magnitude: "Apertus-70B avg 67.5% on language understanding (vs OLMo2-32B 67.7%), avg 58.9% on factual knowledge (vs OLMo2-32B 62.0%); leads all fully open models on INCLUDE V1/V2 and XCOPA"
  - id: C4
    claim: "License filtering for data compliance reduces post-training performance by approximately 5.8% on English benchmarks"
    evidence: "Table 10, Section 4.1.2"
    status: supported
    scope: "Apertus 8B initialized from 10T checkpoint, SFT on Tulu3 mixture, 13 English benchmarks"
    magnitude: "Average performance drops from 0.443 to 0.417 (-5.8%); MMLU CoT-strict drops from 0.515 to 0.253 (-51%)"
  - id: C5
    claim: "Retroactive robots.txt filtering removes approximately 8% of English data and 4% of multilingual data from the pretraining corpus"
    evidence: "Section 3.1.1"
    status: supported
    scope: "Top 1M English domains and top 1M non-English domains from FineWeb/FineWeb-2, robots.txt as of January 2025"
    magnitude: "~8% English token loss, ~4% multilingual token loss"
  - id: C6
    claim: "Apertus-70B-Instruct substantially outperforms Llama-3.3-70B-Instruct on low-resource Romansh translation"
    evidence: "Table 24, Section 5.3"
    status: supported
    scope: "German-Romansh translation across 6 Romansh varieties, 3-shot prompting, greedy decoding, WMT24++ preliminary benchmark"
    magnitude: "Rumantsch Grischun DE->RM: 27.8 vs 21.6 BLEU (+6.2); RM->DE: 44.7 vs 35.6 BLEU (+9.1)"
  - id: C7
    claim: "Apertus achieves 80% strong scaling parallel efficiency at 4096 GPUs for the 70B model"
    evidence: "Figure 13, Section 6.3.6"
    status: supported
    scope: "70B model on Alps GH200 infrastructure, Megatron-LM framework, GBS 16.8M tokens"
    magnitude: "80% strong scaling parallel efficiency at 4096 GPUs, 723 tokens/sec/GPU throughput"
  - id: C8
    claim: "Apertus math and coding performance is comparatively weak, attributed to lack of RL-based training (RLVR)"
    evidence: "Table 18, Section 5.2"
    status: supported
    scope: "8B and 70B Instruct models on HumanEval, MBPP, GSM8K, MGSM, Hendrycks Math, MathQA"
    magnitude: "Apertus-70B-Instruct avg 54.4% vs Qwen3-32B 76.3% and Llama-3.3-70B 74.3% on math/code benchmarks"
  - id: C9
    claim: "FP8 training yields ~26% throughput increase but causes loss divergence after ~300B tokens"
    evidence: "Appendix D, Figure D.1, Section 2.6"
    status: supported
    scope: "Apertus 8B, FP8 current scaling recipe applied at ~8T consumed tokens"
    magnitude: "26.3% throughput increase (6.96k to 8.79k tokens/sec/GPU); substantial loss increase after 300B tokens of FP8 training"
  - id: C10
    claim: "The Swiss AI Charter receives 97.3% average agreement from a survey of 163 Swiss residents"
    evidence: "Table 13, Section 4.3.2"
    status: supported
    scope: "163 Swiss residents via Prolific and ETH Decision Sciences Lab, ~88% passed attention check, 11 articles evaluated"
    magnitude: "97.3% average agreement (agree / agree+disagree); 71.8% strong agreement (always/definitely yes)"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Apertus is a dense decoder-only Transformer building on the original architecture with GQA, RoPE, RMSNorm, and xIELU modifications"
  - target: 2017-05-moe-sparsely-gated-mixture-experts
    type: complementary
    detail: "MoE investigated for Apertus but not derisked in time for pretraining; mentioned as future direction"
  - target: 2024-10-ruler-context-size
    type: uses-benchmark
    detail: "RULER benchmark used to evaluate Apertus long-context capabilities at 4k-64k lengths"
open_questions:
  - question: "Why did Apertus-70B not show significant improvement from the learning rate cooldown, unlike typical behavior at smaller scales?"
    addressed_by: null
  - question: "Can Goldfish loss be made robust to near-duplicate texts with formatting or tokenization divergence?"
    addressed_by: null
  - question: "How much would RLVR training (RL with verifiers) close the math and coding gap with models like Qwen3 and Llama 3.3?"
    addressed_by: null
  - question: "What is the optimal learning rate for AdEMAMix at 70B scale, given the hypothesis that the peak LR was set too low?"
    addressed_by: null
  - question: "Can FP8 training be stabilized through architectural modifications (e.g., FOG reordered layer norms) to maintain the 26% throughput gain?"
    addressed_by: null
---

# Democratizing Open and Compliant LLMs for Global Language Environments: Apertus v1 Technical Report

**Authors:** Project Apertus -- Alejandro Hernandez-Cano, Alexander Hagele, Allen Hao Huang, Angelika Romanou, Antoni-Joan Solergibert, Barna Pasztor, Bettina Messmer, Dhia Garbaya, Eduard Frank Durech, Ido Hakimi, Juan Garcia Giraldo, Mete Ismayilzada, Negar Foroutan, Skander Moalla, Tiancheng Chen, Vinko Sabolcec, Yixuan Xu (Core Team); Antoine Bosselut, Martin Jaggi, Imanol Schlag (Leads) (EPFL, ETH Zurich, CSCS, HES-SO Valais-Wallis, HSLU, IST Austria, ZHAW, University of Zurich, University of Bern, Vischer)
**Date:** September 2025, arXiv:2509.14233

---

## Core Research Problem

Most open-source LLMs fall short in two critical dimensions: **data compliance** and **multilingual representation**. The vast majority of today's open models are actually only open-weight -- they do not release pretraining data, training code, or reproducibility scripts, and many allegedly include large amounts of data collected without regard for content-owner rights (Section 1). Even models that release some data do not retroactively respect `robots.txt` changes, meaning opt-out preferences expressed after crawl time are ignored. This creates legal risk under regulations like the EU AI Act.

Simultaneously, most LLMs focus on English or a small subset of high-resource languages, with models like Llama, Gemma, and Qwen covering at most tens of languages (Section 1). This leaves billions of speakers of mid- and low-resource languages without adequate LLM support. The few exceptions -- BLOOM, Aya, and Qwen3 -- still cover roughly 10x fewer languages than Apertus.

A further problem is that LLMs memorize and can verbatim reproduce training data, raising both copyright and privacy risks. Post-hoc approaches to mitigation (constrained decoding, unlearning, alignment) have proven fragile to adversarial attacks (Appendix F).

**The core challenge is how to build a fully open, data-compliant, massively multilingual LLM that suppresses verbatim memorization while maintaining competitive performance.**

---

## Problem Solutions

The Apertus suite addresses these limitations through a combination of data governance, architectural innovation, and training methodology:

1. **Retroactive data compliance** -- All pretraining data is filtered to respect `robots.txt` opt-outs as of January 2025, retroactively applied to crawls from 2013-2024. PII is removed and the top 5% most toxic documents per language are filtered.
2. **Goldfish loss for memorization prevention** -- A modified cross-entropy loss that masks ~2% of tokens during pretraining using deterministic hashing, preventing the model from learning exact token-to-context mappings.
3. **Massive multilingual coverage** -- Training on 15T tokens from 1811 languages using FineWeb-2, with ~40% of pretraining data allocated to non-English content and 149 languages in post-training.
4. **Architectural efficiency improvements** -- xIELU activation function, AdEMAMix optimizer, QK-Norm, and WSD learning rate schedule that together achieve 30-40% token efficiency gains.
5. **Full transparency** -- All code, data pipelines, intermediate checkpoints, evaluation suites, and training scripts released under permissive licenses.

---

## Approach Details

### Method

Apertus is a **dense decoder-only Transformer** at two scales: 8B (32 layers, 32 attention heads, dim 4096, MLP dim 21504) and 70B (80 layers, 64 attention heads, dim 8192, MLP dim 43008). Both support up to 65,536 token contexts after long-context extension (Table 1, Section 2.1).

The architecture incorporates several modifications to the standard Transformer:

- **Grouped-Query Attention (GQA):** 8 KV heads for both model sizes, reducing KV cache memory.
- **RoPE embeddings** with base Theta = 500,000 during pretraining, extended via NTK-aware scaling during long-context phases.
- **RMSNorm** with Pre-Norm placement for training stability.
- **QK-Norm** to prevent excessively large attention logits.
- **No biases** in any linear layers.
- **Untied embeddings** -- input and output embedding weights are separate.
- **Cross-document attention masking** -- tokens cannot attend across document boundaries within a context window.
- **BoD/EoD tokens** -- every document is bracketed with `<s>` and `</s>` tokens; loss on EoD tokens is masked.

The key novel activation function is **xIELU** (Huang & Schlag, 2025):

> xIELU(x) = alpha_p * x^2 + 0.5x if x > 0; alpha_n * (e^x - 1) - alpha_n * x + 0.5x if x <= 0

where alpha_p and alpha_n are trainable scalars per layer. xIELU extends Squared ReLU to handle negative inputs.

Training uses the **Goldfish loss** to mitigate memorization:

> L(theta) = -(1/|G|) * sum_{i=1}^{L} G_i(x_i) * log P_theta(x_i | x_{<i})

where G is a binary mask sampled via deterministic hashing with a 2% masking rate (k=50) and a 50-token context window for hashing (h=50). Token masking is precomputed during data loading for efficiency (Algorithm 1, Appendix F).

### Key Technical Components

**AdEMAMix optimizer.** A first for an LLM at this scale, AdEMAMix (Pagliardini et al., 2025) adds a long-term EMA momentum vector to Adam, better leveraging old gradients for faster convergence. Optimizer benchmarking shows AdEMAMix consistently scales more favorably with model size, training duration, and batch size than alternatives (Semenov et al., 2025). Gradient clipping is set aggressively at 0.1 (Section 2.6).

**Warmup-Stable-Decay (WSD) learning rate schedule.** Enables continual training without specifying total length in advance (Hu et al., 2024; Hagele et al., 2024). The cooldown uses a negative square root (1-sqrt) shape. For the 8B model: peak LR 1.1e-4; for the 70B: peak LR 1.0e-5. Warmup is linear for 16.8B tokens. Final LR is 10% of peak (Section 2.3).

**Batch size doubling.** The global batch size is doubled mid-training (8B: at 8T tokens from 4.2M to 8.4M tokens; 70B: at 4.4T tokens from 8.4M to 16.8M tokens), which has been shown to benefit later stages of training while increasing hardware efficiency (Section 2.3).

**Long-context extension.** Context length is extended from 4,096 to 65,536 tokens in four stages (8k, 16k, 32k, 64k), with progressive RoPE Theta increases from 1M to 12M. Each stage uses 1.2B token warmup. The data mixture is ~70% Stage 5 data, ~20% FineWeb-Long (documents >4k tokens), and ~10% Institutional Books (Table 5, Table 8, Section 2.5).

**QRPO alignment.** Quantile Reward Policy Optimization (Matrenok et al., 2025) is used for preference alignment, operating on absolute reward signals rather than relative preferences. The loss is:

> L_QRPO = E_{x,y}[(R_q(x,y) - beta_KL * log Z_q(x) - beta_KL * log(pi_theta(y|x) / pi_ref(y|x)))^2]

A length-normalized variant divides beta_KL by completion length |y|. Length normalization consistently improves downstream performance for both QRPO and DPO; QRPO outperforms DPO at 70B scale (Section 4.3).

**Constitutional alignment via Swiss AI Charter.** Controversial topics are aligned using an LLM-as-judge (Qwen3-32B) scoring completions against an 11-article charter informed by Swiss constitutional values. Completions are scored on a 1-9 scale using probability-weighted pointwise scoring, with pairwise ranking for the top 5 (Section 4.3.2).

### Experimental Setup

**Pretraining infrastructure:** Alps supercomputer at CSCS -- 10,752 NVIDIA Grace-Hopper (GH200) GPUs, up to 4,096 GPUs used concurrently. Built on Megatron-LM (Section 6.1).

**Pretraining data:** 15T tokens across 5 stages:
- Stage 1 (0-5T): FineWeb-Edu Score-2, FineWeb-2-HQ, StarCoder, FineMath
- Stage 2 (5-9T, 70B only): FineWeb-HQ, FineWeb-Edu Score-3, multilingual data
- Stage 3 (9-12T): Adds MegaMath, InfiMM-WebMath
- Stage 4 (12-13.5T): DCLM-Edu replaces FineWeb-Edu, higher quality filtering
- Stage 5 (13.5-15T, cooldown): Adds Wikipedia, parallel data, task data, code with quality filtering

**Post-training:** ~4.18M SFT examples across 6 categories (Foundation 9.56%, Math/Reasoning 11.60%, Code 9.02%, Multilingual 34.22%, Regional 22.54%, Domain-Specific 13.02%). Alignment uses 380,537 non-controversial and 72,698 controversial prompts with QRPO (Section 4.1.3, 4.2, 4.3).

**Evaluation:** 94 languages covered across pretraining (probabilistic scoring) and post-training (generation-based) benchmarks. Uses lm-evaluation-harness. Baselines include fully open models (OLMo2, EuroLLM, SmolLM) and open-weight models (Llama 3.1, Qwen 2.5, Qwen3, Gemma 3).

**Reproducibility:** All code (pretraining, post-training, evaluation), data pipelines, intermediate checkpoints, and model weights released under permissive licenses. Training ran for ~6 million GPU hours; the 70B model required 6.74 x 10^24 FLOPs and ~5 GWh of hydropower.

### Key Results

**Pretraining -- General Language Understanding (Table 14):**

| Model | Avg | ARC | HellaSwag | WinoGrande | XNLI | XCOPA | PIQA |
|---|---|---|---|---|---|---|---|
| Apertus-8B | 65.8 | 72.7 | 59.8 | 70.6 | 45.2 | 66.5 | 79.8 |
| Apertus-70B | 67.5 | 70.6 | 64.0 | 73.3 | 45.3 | 69.8 | 81.9 |
| OLMo2-7B | 64.0 | 72.9 | 60.4 | 74.5 | 40.4 | 55.2 | 80.9 |
| OLMo2-32B | 67.7 | 76.2 | 66.7 | 78.6 | 42.9 | 60.1 | 82.1 |
| Llama3.1-8B | 65.4 | 71.6 | 60.0 | 73.4 | 45.3 | 61.8 | 80.1 |
| Llama3.1-70B | 67.3 | 74.4 | 56.5 | 79.4 | 44.3 | 66.7 | 82.3 |

- Apertus-70B achieves the **highest XCOPA score** (69.8) among all evaluated models, demonstrating strong multilingual causal reasoning (tested across 13 fully open and open-weight models, strong evidence).
- Apertus-8B surpasses all fully open models on average (65.8 vs OLMo2-7B 64.0) and is competitive with Llama3.1-8B (65.4) despite using only compliant data.

**Pretraining -- Factual Knowledge (Table 15):**

| Model | Avg | MMLU | Global-MMLU | INCLUDE V1 | INCLUDE V2 | CulturalBench | BLEnD | SwitzerlandQA |
|---|---|---|---|---|---|---|---|---|
| Apertus-8B | 56.9 | 61.6 | 55.3 | 54.8 | 37.3 | 55.2 | 72.2 | 62.1 |
| Apertus-70B | 58.9 | 65.2 | 58.2 | 57.0 | 38.5 | 58.1 | 75.0 | 60.2 |
| OLMo2-7B | 51.6 | 60.5 | 41.1 | 33.8 | 30.6 | 69.5 | 73.2 | 52.5 |
| OLMo2-32B | 62.0 | 71.9 | 57.4 | 50.6 | 37.5 | 74.8 | 79.4 | 62.4 |

- Apertus leads all fully open models on **INCLUDE V1** (54.8 vs OLMo2-7B 33.8, covering 44 languages) and **INCLUDE V2** (37.3 vs OLMo2-7B 30.6, covering 45 languages), though OLMo2-32B is competitive on V2.
- On English-centric benchmarks (MMLU, CulturalBench), OLMo2-32B leads, reflecting Apertus's trade-off from allocating ~40% of training data to non-English content.

**Post-training -- Math and Coding (Table 18):**

| Model | Avg | HumanEval P@10 | MBPP P@1 | GSM8K | MGSM | Hendrycks Math | MathQA |
|---|---|---|---|---|---|---|---|
| Apertus-70B-Instruct | 54.4 | 73.0 | 47.0 | 77.6 | 64.3 | 30.8 | 33.9 |
| Apertus-8B-Instruct | 44.2 | 67.0 | 36.2 | 62.9 | 48.5 | 18.2 | 32.1 |
| OLMo2-32B-Instruct | 56.7 | 69.0 | 41.8 | 88.2 | 67.3 | 44.3 | 29.6 |
| Qwen3-32B | 76.3 | 97.0 | 73.6 | 93.6 | 74.0 | 69.2 | 50.5 |

- Math and coding are Apertus's **weakest areas**. The paper attributes this to lack of RLVR training, which is known to enhance these capabilities (moderate evidence -- acknowledged but not ablated).

**Long-Context -- RULER (Table 23):**

| Model | 4k | 8k | 16k | 32k | 64k |
|---|---|---|---|---|---|
| Apertus-8B-Instruct | 91.2 | 87.2 | 79.1 | 65.9 | 61.4 |
| Apertus-70B-Instruct | 94.8 | 89.9 | 85.7 | 81.9 | 67.3 |
| Llama-3.1-8B-Instruct | 95.0 | 94.0 | 91.8 | 86.2 | 84.8 |
| Qwen2.5-72B-Instruct | 96.1 | 95.0 | 94.5 | 93.3 | 89.3 |

- Apertus shows **significant degradation** beyond 16k context, with Apertus-8B-Instruct dropping from 91.2 at 4k to 61.4 at 64k, and Apertus-70B-Instruct from 94.8 to 67.3 (though the 70B 64k evaluation exceeded the maximum allowed runtime). This is substantially worse than Llama-3.1-8B-Instruct (84.8 at 64k) and Qwen2.5-72B (89.3 at 64k).

### Ablation Results

**Architecture ablations at 1.5B scale (Table 3):**

| Modification | Loss |
|---|---|
| Baseline 1.5B | 2.037 |
| + Cross-document attention | 2.037 |
| + Cosine -> WSD, lower LR | 2.033 |
| + AdamW -> AdEMAMix | 2.002 |
| + SwiGLU -> xIELU (with wider MLP) | 1.997 |
| Apertus 3B (all changes merged) | **1.843** |
| Baseline 3B | 1.906 |

- **AdEMAMix** and **xIELU** provide the largest individual gains (each ~0.035-0.040 loss reduction). Combined at 3B scale, the full recipe achieves loss 1.843 vs baseline 1.906 (ablated at 1.5B and 3B scale on 100B tokens, moderate evidence).

**OLMo2 comparison (Table 4):** At 1B scale, Apertus matches OLMo2's loss with **46% fewer tokens**; at 7B, with **30% fewer tokens** (20,000 iterations, replayed on identical OLMo2 data, single configuration per scale, limited evidence for generalizability).

**Cooldown data ablations (Table 7):** DCLM-edu gives the largest performance gain (Full Macro 0.45383 vs Regular 0.44738, tested on 1.5B models with 100B token cooldowns, moderate evidence).

---

## Limitations and Failure Modes

**Author-acknowledged limitations:**

- **Math and coding performance is weak** relative to models that use RLVR training. Apertus-70B-Instruct averages 54.4% on math/code benchmarks vs 76.3% for Qwen3-32B (Table 18, Section 5.2). The authors explicitly note RLVR has not been applied.

- **Goldfish loss is fragile to near-duplicates.** The deterministic hashing mechanism breaks when training data contains slightly varied versions of the same text. All 22 sequences with Rouge-L >= 0.7 among 10,672 Gutenberg probes were canonical works (Keats, Shakespeare, US Constitution, Bible) appearing both in Gutenberg probes and repeatedly in the 15T pretraining corpus. Formatting divergence (~21.5 tokens/line vs. web line-breaking) and tokenizer inconsistency create mismatched masks (Section 5.4.2).

- **Long-context performance degrades significantly.** On RULER, Apertus-8B-Instruct drops from 91.2 at 4k to 61.4 at 64k tokens, and Apertus-70B-Instruct drops from 94.8 to 67.3 (though the 70B 64k evaluation exceeded the maximum allowed runtime on the node). Both are well below Llama-3.1-8B-Instruct (84.8 at 64k) and Qwen2.5-72B (89.3 at 64k) (Table 23).

- **70B cooldown did not produce expected benchmark gains.** Unlike the 8B model and prior work at smaller scales, Apertus-70B showed no significant change in loss slope at the cooldown phase (13.5T tokens). The authors hypothesize the peak LR was set too low (Section 2.6).

- **FP8 training failed after ~300B tokens** -- a 26% throughput gain was obtained but loss diverged, requiring rollback to BF16 (Section 2.6, Appendix D).

- **HarmBench safety scores are worse than most fully open models** (31.9 for 70B, 35.2 for 8B vs. e.g. EuroLLM-22B 8.0, ALLaM-7B 7.0), though comparable to open-weight models. The authors explicitly choose not to pursue jailbreak resistance, citing the ease of removing post-training guardrails from open-weight models (Table 26, Section 5.5).

- **License filtering incurs a performance cost.** Adding license filtering to Tulu3 data reduces average English benchmark performance by 5.8% and multilingual performance by 4.3%, with particularly severe drops on MMLU CoT-strict (-51%) and MGSM native CoT (-14.7%) (Tables 10-11, Section 4.1.2).

- **[Inferred]** The performance gap between Apertus-70B and smaller 8B is smaller than typically observed in other model families (acknowledged in Section 5.2), suggesting potential underperformance of the 70B model that may relate to the suboptimal peak learning rate.

- **[Inferred]** Safety testing across all 1811 pretraining languages is infeasible -- the authors test on 12 languages for LinguaSafe and note this falls short of the full pretraining/post-training language coverage (Section 5.5.1).

#### Scope and Comparability

- **What was not tested:** Models were not evaluated with RLVR training; no multimodal capabilities; no evaluation of agentic or tool-use performance despite the chat template supporting tool calls; long-context evaluation at 64k for 70B exceeded runtime limits; safety benchmarks cover only 12 of 1811+ languages.
- **Comparability notes:** Many baseline models (Qwen3, Llama 3.3) have undergone additional RL training that Apertus has not, making math/code comparisons unequal. The RULER evaluation shows that Apertus's long-context extension (4-stage progressive with 225B total tokens) produces substantially weaker results than Llama 3.1's approach, despite similar target context lengths (65k vs. 128k). The 70B model uses a notably low peak LR (1.0e-5) compared to typical values at this scale, which may explain the subdued cooldown effect.

---

## Conclusions

### Contributions

1. **First fully open 70B-scale LLM.** Apertus-70B is the largest fully open model to date (70B parameters, 15T tokens), with complete release of code, data pipelines, checkpoints, and training artifacts under permissive licenses (Section 1).

2. **Retroactive data compliance standard.** The paper establishes a new compliance protocol that retroactively applies January 2025 `robots.txt` opt-outs to web crawls spanning 2013-2024, designed to comply with EU AI Act data provisions (Section 3.1.1).

3. **Goldfish loss at scale.** The first large-scale validation of the Goldfish objective (Hans et al., 2024), demonstrating effective suppression of verbatim memorization at 8B and 70B scale even after 128 exposures, with no degradation in downstream performance (Section 5.4, Appendix F).

4. **Massively multilingual pretraining.** Training on 1811 languages -- roughly 10x more than prior multilingual models like BLOOM, Aya, or Qwen3 -- with ~40% non-English allocation and 149 languages in post-training (Section 1).

5. **Architectural efficiency recipe.** The combination of xIELU, AdEMAMix, QK-Norm, WSD schedule, and cross-document attention masking achieves 30-40% token efficiency gains at 3B scale and outperforms OLMo2's recipe at 1B and 7B scale (Section 2.4).

6. **Constitutional alignment through the Swiss AI Charter.** A novel alignment approach using a charter informed by Swiss constitutional values, with 97.3% average agreement from Swiss residents, deployed via LLM-as-judge scoring (Section 4.3.2).

### Implications

1. **Data compliance imposes measurable costs.** The ~5.8% English performance drop from license filtering (Table 10) and ~8% English token loss from `robots.txt` filtering quantify the real trade-off between compliance and capability. This challenges the notion that compliance can be achieved without sacrificing performance.

2. **Goldfish loss may shift the copyright discussion.** By demonstrating effective memorization prevention at scale, Apertus provides a concrete technical mechanism for addressing copyright concerns in LLM training, potentially influencing regulatory approaches (speculative -- effectiveness against adversarial extraction attacks not yet tested).

3. **Multilingual allocation trades off English performance.** Apertus-70B's factual knowledge average (58.9%) lags OLMo2-32B (62.0%) despite having 2x the parameters, suggesting the ~40% non-English data allocation necessarily reduces English benchmarks (speculative -- not directly ablated).

---

## Key Claims

1. **Apertus recipe achieves 30-40% token efficiency over a Llama-style baseline at 3B scale** (Table 3, Figure 2). The combined modifications (xIELU, AdEMAMix, QK-Norm, WSD, Goldfish loss) reach the same training loss with 30-40% fewer tokens. xIELU and AdEMAMix individually contribute the largest gains (loss 1.997 and 2.002 vs baseline 2.037). Status: **supported** (ablated at 1.5B and 3B scale on 100B tokens, moderate evidence; also validated against OLMo2 at 1B and 7B scale).

2. **Goldfish loss suppresses verbatim memorization without degrading performance** (Figure 8, Table 25, Table F.5). Rouge-L remains at baseline ~0.18 across all exposure frequencies (1-128) and prefix lengths (50-5000 tokens), for both 8B and 70B models, under both greedy and nucleus decoding. At 8B scale, Goldfish loss actually outperforms standard cross-entropy on most downstream benchmarks. Status: **supported** (tested across 2 model sizes, 2 decoding strategies, and 9 exposure frequencies; strong evidence within tested conditions).

3. **Apertus is the strongest fully open model on multilingual benchmarks** (Tables 14-15, Figure 7). Apertus-70B leads all fully open models on INCLUDE V1/V2 (54.8/37.3 at 8B, 57.0/38.5 at 70B) and XCOPA (69.8). At 8B scale it leads on average language understanding (65.8 vs OLMo2-7B 64.0). Status: **supported** (evaluated across 13+ baselines on a comprehensive suite, strong evidence; however, overall average across language understanding and factual knowledge is nuanced -- OLMo2-32B leads on factual knowledge with 62.0 avg vs 58.9).

4. **License filtering costs ~5.8% English and ~4.3% multilingual performance** (Tables 10-11). The most severe impact is on MMLU CoT-strict (-51%), while some capabilities (TruthfulQA) improve. Status: **supported** (single model size 8B, single checkpoint at 10T tokens, limited evidence for generalizability to other scales).

5. **Retroactive robots.txt filtering removes ~8% English and ~4% multilingual tokens** (Section 3.1.1). Status: **supported** (single measurement point, limited evidence -- filtering applied to top 1M English and 1M non-English domains only).

6. **Apertus substantially outperforms Llama-3.3-70B on Romansh translation** (Table 24). Apertus-70B-Instruct achieves +6.2 BLEU on DE->RM and +9.1 BLEU on RM->DE for Rumantsch Grischun. Status: **supported** (6 Romansh varieties tested, single baseline Llama-3.3-70B, preliminary benchmark version, limited evidence).

7. **80% strong scaling parallel efficiency at 4096 GPUs** (Figure 13, Section 6.3.6). The 70B model achieves 723 tokens/sec/GPU at full scale with GBS of 16.8M tokens. Status: **supported** (measured on Alps GH200 infrastructure, single configuration, limited evidence for generalizability).

8. **Math and coding are weak due to lack of RLVR** (Table 18). Apertus-70B-Instruct averages 54.4% vs Qwen3-32B 76.3% on math/code benchmarks. Status: **supported** (the performance gap is clear; the attribution to lack of RLVR is plausible but not directly ablated -- no Apertus+RLVR variant exists, so this remains a hypothesis).

9. **FP8 training yields 26% throughput increase but destabilizes training after ~300B tokens** (Section 2.6, Appendix D, Figure D.1). Status: **supported** (single experiment on 8B model, limited evidence).

10. **Swiss AI Charter receives 97.3% agreement from Swiss residents** (Table 13, Section 4.3.2). Status: **supported** (163 participants, ~88% passed attention check, moderate evidence -- sample size is modest and limited to Prolific/ETH lab demographics).

---

## Open Questions

1. **Why did Apertus-70B not benefit from the learning rate cooldown?** Unlike the 8B model and established results at smaller scales, the 70B showed no significant loss slope change or benchmark jump at the cooldown phase (13.5T tokens). The authors hypothesize the peak LR was too low, but this remains unvalidated (Section 2.6). Not addressed by subsequent work.

2. **Can Goldfish loss be made robust to near-duplicate texts?** The deterministic hashing is fragile to formatting and tokenization divergences between versions of the same text. All high-memorization cases (Rouge-L >= 0.7) were canonical works appearing in both Gutenberg probes and web data (Section 5.4.2). Not addressed by subsequent work.

3. **How much would RLVR training close the math and coding gap?** The paper explicitly identifies RLVR as a future direction and attributes the math/code weakness to its absence, but provides no estimate of the expected improvement (Section 7). Not addressed by subsequent work.

4. **What is the optimal peak learning rate for AdEMAMix at 70B scale?** The 70B model used a notably low peak LR of 1.0e-5, and the authors were unable to establish proper scaling rules due to time constraints (Section 2.6). Not addressed by subsequent work.

5. **Can FP8 training be stabilized through architectural modifications?** The authors' separate work (Hernandez-Cano et al., 2025) achieves stable FP8 training on FOG architectures with reordered layer normalizations, but this was not validated on Apertus at scale (Appendix D). Not addressed by subsequent work.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that Apertus builds upon as a dense decoder-only model.
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.* Provides the grouped-query attention mechanism used in Apertus for inference efficiency.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE embeddings are the positional encoding used in Apertus with base Theta 500,000.
- **Huang & Schlag (2025)** -- *xIELU activation function.* The novel activation function used in Apertus MLP layers, extending Squared ReLU to handle negative inputs.

### Optimization and Training

- **Pagliardini et al. (2025)** -- *AdEMAMix optimizer.* The optimizer used for all Apertus training, adding long-term EMA momentum to Adam.
- **Hu et al. (2024); Hagele et al. (2024)** -- *WSD learning rate schedule.* The Warmup-Stable-Decay schedule used for continual training without specifying total length in advance.
- **Hans et al. (2024)** -- *Goldfish Loss.* The original memorization prevention objective that Apertus extends and validates at 8B-70B scale.

### Data and Compliance

- **Penedo et al. (2025)** -- *FineWeb-2.* The base multilingual web-crawl dataset providing 1811 languages for Apertus pretraining.
- **Penedo et al. (2024a)** -- *FineWeb.* The English web-crawl dataset used as the basis for English pretraining data.
- **Fan et al. (2025)** -- *Data compliance gap when respecting training data opt-out.* Provides the framework for retroactive robots.txt filtering.

### Post-Training

- **Matrenok et al. (2025)** -- *QRPO.* The Quantile Reward Policy Optimization algorithm used for Apertus alignment.
- **Lambert et al. (2025)** -- *Tulu 3.* Provides post-training data foundations and length normalization approach for alignment.
- **OLMo et al. (2025)** -- *OLMo2.* Key fully open model baseline and source of post-training data pipelines.

### Evaluation Benchmarks

- **Hsieh et al. (2024)** -- *RULER.* Multi-task synthetic long-context benchmark used for Apertus long-context evaluation at 4k-64k.
- **Romanou et al. (2025)** -- *INCLUDE.* Multilingual cultural knowledge benchmark covering 44 languages, where Apertus leads among fully open models.
- **Singh et al. (2025)** -- *Global-MMLU.* Multilingual extension of MMLU used for cross-lingual factual knowledge evaluation.

### Models Used in Evaluation

- **Grattafiori et al. (2024)** -- *Llama 3.* Open-weight model family used as primary comparison baseline at 8B and 70B scales.
- **Yang et al. (2024b; 2025b)** -- *Qwen 2.5 and Qwen 3.* Open-weight model families that serve as strongest baselines on math, coding, and reasoning.
- **Martins et al. (2025)** -- *EuroLLM.* Fully open multilingual model family used as a key baseline for multilingual comparisons.
