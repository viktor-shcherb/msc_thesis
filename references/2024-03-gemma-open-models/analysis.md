---
title: "Gemma: Open Models Based on Gemini Research and Technology"
authors: "Gemma Team, Google DeepMind"
year: 2024
venue: "arXiv preprint 2403.08295"
paper_type: preprint
categories: ["model-release", "architecture"]
scope: ["open-weight language models", "efficient 2B and 7B models", "instruction tuning", "RLHF", "safety evaluation"]
benchmarks_used: ["mmlu", "hellaswag", "piqa", "siqa", "winogrande", "arc", "boolq", "triviaqa", "natural-questions", "humaneval", "mbpp", "gsm8k", "math-hendrycks", "bbh", "agi-eval", "csqa", "openbookqa", "truthfulqa", "toxigen", "bold"]
models_introduced: ["gemma-2b", "gemma-7b"]
models_evaluated: ["llama-2-7b", "llama-2-13b", "mistral-7b"]
key_claims:
  - id: C1
    claim: "Gemma 7B outperforms Llama 2 13B on MMLU (64.3% vs 54.8%) despite having roughly half the parameters"
    evidence: "Table 6, Section 6"
    status: supported
    scope: "5-shot evaluation, English-only, Gemini evaluation methodology; LLaMA-2 numbers from original paper (different eval setup)"
    magnitude: "+9.5 percentage points over Llama 2 13B (64.3 vs 54.8)"
  - id: C2
    claim: "Gemma 7B achieves 46.4% on GSM8K, outperforming Mistral 7B (35.4%) by 11 points"
    evidence: "Table 6, Section 6"
    status: supported
    scope: "maj@1 evaluation; Mistral number re-evaluated by authors"
    magnitude: "+11.0 percentage points (46.4 vs 35.4)"
  - id: C3
    claim: "Gemma 7B achieves 24.3% on MATH, nearly double Mistral 7B's 12.7%"
    evidence: "Table 6, Section 6"
    status: supported
    scope: "4-shot evaluation"
    magnitude: "+11.6 percentage points (24.3 vs 12.7)"
  - id: C4
    claim: "Gemma outperforms similarly sized open models on 11 out of 18 text-based tasks"
    evidence: "Abstract, Table 6"
    status: supported
    scope: "18 benchmarks, comparison against Llama 2 7B/13B and Mistral 7B; LLaMA-2 numbers from original paper"
    magnitude: "11/18 tasks with best score; average 56.9% vs next-best Mistral 7B 54.5%"
  - id: C5
    claim: "Gemma 7B IT achieves 61.2% win rate over Mistral v0.2 7B Instruct on instruction following"
    evidence: "Table 5, Section 6"
    status: supported
    scope: "human evaluation on ~1000 prompts covering creative writing, coding, and instruction following; Gemma 1.1 IT version"
    magnitude: "61.2% win rate [95% CI: 59.3%, 63%]"
  - id: C6
    claim: "Gemma 7B IT achieves 63.5% win rate on safety prompts vs Mistral v0.2 7B Instruct"
    evidence: "Table 5, Section 6"
    status: supported
    scope: "human evaluation on ~400 safety prompts; Gemma 1.1 IT version"
    magnitude: "63.5% win rate [95% CI: 60.7%, 66.1%]"
  - id: C7
    claim: "Gemma models memorize training data at comparable rates to PaLM models of similar size"
    evidence: "Figure 2, Section 6"
    status: supported
    scope: "exact memorization using 50-token continuations on 10,000 sampled documents per corpus"
    magnitude: "~0.1-1% exact memorization rate depending on data source"
  - id: C8
    claim: "No sensitive personal data was memorized by Gemma models"
    evidence: "Figure 3, Section 6"
    status: unvalidated
    scope: "based on Google Cloud Sensitive Data Protection tool classification; tool has known false positive issues"
    magnitude: "0% sensitive data memorized; some 'personal' data memorized at lower rates than non-personal data"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Based on the Transformer decoder architecture with RoPE, GeGLU, and RMSNorm modifications"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Primary comparison target; Gemma 7B outperforms Llama 2 13B on most benchmarks"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "Compares against LLaMA 1 models as a comparable open model"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Direct comparison target at 7B scale; Gemma 7B outperforms on math and coding benchmarks"
  - target: 2022-12-chain-of-thought-prompting
    type: extends
    detail: "Uses chain-of-thought prompting for LM-based judges during SFT data selection"
  - target: 2025-03-gemma-3-technical-report
    type: extended-by
    detail: "Gemma 3 adds multimodality, 128K context, and 5:1 local-global attention interleaving"
open_questions:
  - question: "How does Gemma perform on long-context tasks beyond its 8K context window?"
    addressed_by: 2025-03-gemma-3-technical-report
  - question: "What is the detailed composition of the pretraining data mixture?"
    addressed_by: null
  - question: "How does Gemma's instruction tuning recipe transfer to other base models?"
    addressed_by: null
  - question: "What tasks benefit most from the 7B vs 2B tradeoff for deployment?"
    addressed_by: null
  - question: "What is the 'novel reinforcement learning algorithm' used for RLHF policy optimization?"
    addressed_by: null
---

# Gemma: Open Models Based on Gemini Research and Technology

**Authors:** Gemma Team, Google DeepMind (Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya Pathak, Laurent Sifre, Morgane Riviere, Mihir Sanjay Kale, Juliette Love, Pouya Tafti, Leonard Hussenot, Pier Giuseppe Sessa, et al.)
**Date:** March 2024, arXiv:2403.08295

---

## Core Research Problem

At the time of Gemma's release, open-weight language models such as Llama 2 (Touvron et al., 2023b) and Mistral 7B (Jiang et al., 2023) had established strong baselines for community research and commercial applications. However, these models were trained independently of frontier closed models (e.g., Gemini, GPT-4), limiting the transfer of architectural insights, training recipes, and safety practices from the most capable systems. Google DeepMind's Gemini models (Gemini Team, 2023) demonstrated state-of-the-art performance but remained closed-weight, preventing the community from studying, fine-tuning, or building upon them directly.

Prior open model releases from Google (Word2Vec, BERT, T5) had enabled broad community innovation (Mikolov et al., 2013; Devlin et al., 2018; Raffel et al., 2019), but no openly available model had yet inherited the training infrastructure and recipes from Google's frontier Gemini program.

The core challenge was: **how to release lightweight, openly available models that leverage Gemini's research and technology while maintaining strong safety properties and enabling broad community access.**

---

## Problem Solutions

Gemma addresses the gap between frontier closed models and open-weight alternatives through:

1. **Technology transfer from Gemini.** Apply the architectures, data pipelines, training recipes, and safety practices developed for Gemini to smaller, openly releasable models (Section 1).

2. **Two model sizes for different deployment scenarios.** Provide a 7B model for GPU/TPU deployment and a 2B model for CPU and on-device applications (Section 1).

3. **Both pretrained and instruction-tuned checkpoints.** Release base models for research and fine-tuning, plus instruction-tuned variants with SFT and RLHF for immediate application use (Section 1).

4. **Comprehensive safety evaluation and filtering.** Apply data filtering, safety benchmarking, red teaming, and memorization analysis to reduce risks from open model release (Sections 4, 6, 7).

---

## Approach Details

### Method

Gemma uses a **decoder-only Transformer architecture** (Vaswani et al., 2017) with several post-Transformer improvements. The core parameters are (Table 1, Section 2):

| Parameter | Gemma 2B | Gemma 7B |
|---|---|---|
| d_model | 2048 | 3072 |
| Layers | 18 | 28 |
| Feedforward hidden dims | 32768 | 49152 |
| Num heads | 8 | 16 |
| Num KV heads | 1 (MQA) | 16 (MHA) |
| Head size | 256 | 256 |
| Vocab size | 256128 | 256128 |
| Context length | 8192 | 8192 |

Parameter counts (Table 2, Section 2):
- **Gemma 2B:** 524M embedding + 1,982M non-embedding = ~2.5B total
- **Gemma 7B:** 787M embedding + 7,751M non-embedding = ~8.5B total

The large vocabulary (256K tokens) is inherited from Gemini and designed for multilingual use, accounting for the relatively high embedding parameter count compared to English-only models.

### Key Technical Components

**Multi-Query Attention (MQA) for 2B.** The 2B model uses MQA (num_kv_heads = 1) based on ablations showing MQA works well at smaller scales (Shazeer, 2019). The 7B model uses standard multi-head attention (num_kv_heads = 16) (Section 2).

**RoPE Embeddings.** Rotary positional embeddings (Su et al., 2021) are applied in each layer rather than absolute positional embeddings. Input and output embeddings are tied (shared) to reduce model size (Section 2).

**GeGLU Activations.** The standard ReLU non-linearity is replaced with the approximated version of the GeGLU activation function (Shazeer, 2020) (Section 2).

**RMSNorm.** The input of each transformer sub-layer (both attention and feedforward) is normalized with RMSNorm (Zhang and Sennrich, 2019) rather than LayerNorm (Section 2).

**Tokenizer.** A subset of Gemini's SentencePiece tokenizer (Kudo and Richardson, 2018) with 256K vocabulary. It splits digits, does not remove extra whitespace, and uses byte-level encodings for unknown tokens (Section 4).

### Training Data

- **Gemma 2B:** Trained on **3T tokens**
- **Gemma 7B:** Trained on **6T tokens**

Data sources include primarily-English web documents, mathematics, and code. Unlike Gemini, Gemma is not multimodal and is not trained for multilingual performance (Section 4).

**Data filtering:** Heuristics and model-based classifiers remove harmful or low-quality content. All evaluation sets are filtered from pretraining data with targeted contamination analysis. Personal information and sensitive data are filtered using automated techniques (Section 4).

**Data mixture staging:** Following Gemini's approach, the corpus mixture is altered throughout training to increase the weight of relevant, high-quality data towards the end of training. The final data mixture was determined through ablation experiments on both model sizes (Section 4).

### Training Infrastructure

- **Hardware:** TPUv5e (256 chips per pod, configured as 16x16 2D torus) (Section 3)
- **7B model:** 16 pods = 4096 TPUv5e chips; 16-way model sharding + 16-way data replication within each pod
- **2B model:** 2 pods = 512 TPUv5e chips; 256-way data replication within each pod
- **Optimizer state:** Sharded using ZeRO-3-like techniques; data-replica reduce over data-center network via Pathways
- **Framework:** JAX with Pathways single-controller programming paradigm (Barham et al., 2022), GSPMD partitioner (Xu et al., 2021), MegaScale XLA compiler

**Carbon footprint:** Estimated ~131 tCO2eq for pretraining, offset by Google's carbon neutrality program (Section 3).

### Instruction Tuning

**Supervised Fine-Tuning (SFT):** Fine-tuned on a mix of text-only, English-only synthetic and human-generated prompt-response pairs. Data mixtures selected using LM-based side-by-side evaluations (Zheng et al., 2023): a high-capability model judges preferences between test and baseline model responses. Different prompt sets test instruction following, factuality, creativity, and safety. LM judges use chain-of-thought prompting (Wei et al., 2022) and constitutional AI techniques (Bai et al., 2022) to align with human preferences (Section 5).

**Synthetic data filtering:** Multiple filtering stages remove personal information, unsafe/toxic outputs, mistaken self-identification data, and duplicates. Subsets encouraging attribution, hedging, and refusals are included to minimize hallucinations (Section 5).

**Formatting:** Special control tokens (`<start_of_turn>`, `<end_of_turn>`, `user`, `model`) delineate conversation turns. Using the formatter is important; out-of-distribution generation without it produces worse results (Table 3, Section 5).

**RLHF:** The SFT model is further fine-tuned using RLHF (Christiano et al., 2017; Ouyang et al., 2022). A reward function is trained on human-labeled English preference data using the Bradley-Terry model (Bradley and Terry, 1952). The policy is trained using a "novel reinforcement learning algorithm" (not further specified). High-capacity LM raters compute side-by-side comparisons to tune hyperparameters and mitigate reward hacking (Amodei et al., 2016; Skalse et al., 2022) (Section 5).

### Experimental Setup

**Evaluation methodology:** Most benchmarks use the same evaluation methodology as Gemini. For benchmarks compared with Mistral (ARC, CommonsenseQA, BBH, AGI Eval English-only), the Mistral technical report methodology is replicated. Due to restrictive licensing, LLaMA-2 numbers are cited from the original paper rather than re-evaluated (different evaluation setup) (Section 6).

**Baselines:** Llama 2 7B, Llama 2 13B, Mistral 7B (Section 6).

**Human preference evaluation:** ~1000 prompts for instruction following (creative writing, coding, following instructions) and ~400 prompts for safety, evaluated against Mistral v0.2 7B Instruct. Results reported for Gemma 1.1 IT (main body) and Gemma 1.0 IT (Appendix) (Section 6).

**Reproducibility:** No training hyperparameters (optimizer, learning rate, schedule) are disclosed. Pretraining data composition is not detailed. RLHF algorithm is not specified. Code for inference and serving is open-sourced, but training code is not.

### Key Results

**Academic benchmarks (Table 6, Section 6):**

| Benchmark | Metric | LLaMA-2 7B | LLaMA-2 13B | Mistral 7B | Gemma 2B | Gemma 7B |
|---|---|---|---|---|---|---|
| MMLU | 5-shot, top-1 | 45.3 | 54.8 | 62.5 | 42.3 | **64.3** |
| HellaSwag | 0-shot | 77.2 | 80.7 | 81.0 | 71.4 | **81.2** |
| PIQA | 0-shot | 78.8 | 80.5 | **82.2** | 77.3 | 81.2 |
| SIQA | 0-shot | 48.3 | 50.3 | 47.0* | 49.7 | **51.8** |
| BoolQ | 0-shot | 77.4 | 81.7 | 83.2* | 69.4 | **83.2** |
| WinoGrande | partial | 69.2 | 72.8 | **74.2** | 65.4 | 72.3 |
| CQA | 7-shot | 57.8 | 67.3 | 66.3* | 65.3 | **71.3** |
| OBQA | - | **58.6** | 57.0 | 52.2 | 47.8 | 52.8 |
| ARC-e | - | 75.2 | 77.3 | 80.5 | 73.2 | **81.5** |
| ARC-c | - | 45.9 | 49.4 | **54.9** | 42.1 | 53.2 |
| TriviaQA | 5-shot | 72.1 | **79.6** | 62.5 | 53.2 | 63.4 |
| NQ | 5-shot | 25.7 | **31.2** | 23.2 | 12.5 | 23.0 |
| HumanEval | pass@1 | 12.8 | 18.3 | 26.2 | 22.0 | **32.3** |
| MBPP | 3-shot | 20.8 | 30.6 | 40.2* | 29.2 | **44.4** |
| GSM8K | maj@1 | 14.6 | 28.7 | 35.4* | 17.7 | **46.4** |
| MATH | 4-shot | 2.5 | 3.9 | 12.7 | 11.8 | **24.3** |
| AGIEval | - | 29.3 | 39.1 | 41.2* | 24.2 | **41.7** |
| BBH | - | 32.6 | 39.4 | **56.1*** | 35.2 | 55.1 |
| **Average** | - | 46.9 | 52.4 | 54.5 | 45.0 | **56.9** |

*Asterisks (*) denote evaluations run by the Gemma authors using Mistral methodology. Mistral reports 50.2 on a different MBPP split; on that split Gemma 7B achieves 54.5. LLaMA-2 numbers are from the original paper due to licensing restrictions (different evaluation setup, limiting direct comparability).*

Key observations:
- **Gemma 7B outperforms Llama 2 13B on MMLU** by +9.5 points (64.3 vs 54.8) despite having roughly half the parameters (Table 6).
- **Strong math performance:** GSM8K +11 points over Mistral 7B (46.4 vs 35.4), MATH +11.6 points (24.3 vs 12.7) (Table 6).
- **Strong code performance:** HumanEval +6.1 points over Mistral 7B (32.3 vs 26.2), MBPP +4.2 points (44.4 vs 40.2). Gemma 7B exceeds CodeLLaMA-7B on MBPP (44.4 vs 41.4) (Table 6, Section 6).
- **Weaker on knowledge benchmarks:** TriviaQA 63.4 vs Llama 2 13B's 79.6, NQ 23.0 vs 31.2 (Table 6). This is a notable gap suggesting parameter count limits factual knowledge storage.
- **Gemma 7B best on 11 of 18 benchmarks** with highest average (56.9%) vs next-best Mistral 7B (54.5%) (single evaluation per configuration, no variance reported -- limited evidence for per-benchmark claims).

**HuggingFace H6 benchmark (Table 7, Section 6):**

| Benchmark | Mistral 7B | Gemma 7B |
|---|---|---|
| ARC-c | 60.0 | **61.9** |
| HellaSwag | **83.3** | 82.2 |
| MMLU | 64.2 | **64.6** |
| TruthfulQA | 42.2 | **44.8** |
| WinoGrande | 78.4 | **79.0** |
| GSM8K | 37.8 | **50.9** |
| **Average** | 61.0 | **63.8** |

*All evaluations run by HuggingFace (independent of authors). Gemma 7B outperforms Mistral 7B on 5/6 benchmarks (moderate evidence -- independent evaluation replication).*

**Human preference evaluation (Table 5, Section 6, Gemma 1.1 IT):**

| Model | Safety Win Rate | Instruction Following Win Rate |
|---|---|---|
| Gemma 7B IT vs Mistral v0.2 7B | 63.5% [60.7%, 66.1%] | 61.2% [59.3%, 63%] |
| Gemma 2B IT vs Mistral v0.2 7B | 60.1% [57.3%, 62.8%] | 45% [43.1%, 46.9%] |

*Win/Tie/Loss for Gemma 7B IT: Safety 51.5%/23.9%/24.6%, Instruction Following 52.2%/18.1%/29.8%. Ties broken evenly for final win rate. ~1000 instruction prompts and ~400 safety prompts (moderate evidence -- single comparison against one baseline).*

**Gemma 1.0 IT results (Appendix Table 9):** The earlier Gemma 1.0 IT models showed lower win rates: 7B IT achieved 58% safety / 51.7% instruction following; 2B IT achieved 56.5% safety / 41.6% instruction following. The 1.1 IT version improved substantially on both axes.

**Safety benchmarks (Table 8, Section 6, Gemma 1.1 IT):**

| Benchmark | Mistral v0.2 7B | Gemma 1.1 IT 2B | Gemma 1.1 IT 7B |
|---|---|---|---|
| RealToxicity (avg) | 8.44 | **7.03** | 8.04 |
| BOLD | 46.0 | **47.76** | 45.2 |
| CrowS-Pairs (top-1) | 32.76 | 45.89 | **49.67** |
| BBQ Ambig (1-shot, top-1) | **97.53** | 58.97 | 86.06 |
| BBQ Disambig (top-1) | 84.45 | 53.9 | **85.08** |
| Winogender (top-1) | **64.3** | 50.14 | 57.64 |
| TruthfulQA | **48.54** | 44.24 | 45.34 |
| Winobias 1_2 | **65.72** | 55.93 | 59.22 |
| Winobias 2_2 | 84.53 | **89.46** | 89.2 |
| Toxigen | 61.77 | **29.64** | 38.75 |

*Mixed results: Gemma 7B IT outperforms Mistral on CrowS-Pairs, BBQ Disambig, Winobias 2_2, and Toxigen (lower = better), but underperforms on BBQ Ambig, Winogender, TruthfulQA, and Winobias 1_2. LLaMA-2 numbers not comparable due to different TruthfulQA evaluation setups (MC2 vs GPT-Judge) (limited evidence -- single evaluation, no variance reported).*

### Memorization Analysis

**Methodology:** Sample 10,000 documents from each corpus, use first 50 tokens as prompt, classify as memorized if subsequent 50 tokens exactly match ground truth. Also measure approximate memorization with 10% edit distance threshold (Ippolito et al., 2022) (Section 6).

**Results (Figure 2):** Gemma memorizes training data at comparable rates to PaLM models of similar size (~0.1-1% exact memorization depending on data source). When evaluating on a shared subset of training corpora, much lower memorization rates are observed due to less overlap between Gemma and PaLM pretraining data. "Total memorization" across the entire pretraining dataset gives a more reliable estimate (Section 6).

**Personal data (Figure 3):** No sensitive data was memorized (as classified by Google Cloud Sensitive Data Protection). Some potentially "personal" data was memorized at lower rates than non-personal data. The detection tool has known false positive issues -- it matches patterns without considering context, likely overestimating personal data identification (Section 6).

**Approximate memorization (Figure 4):** Roughly 50% more data is approximately memorized than exactly memorized, consistent across data subcategories (Section 6).

---

## Limitations and Failure Modes

1. **Knowledge benchmark weakness.** Gemma 7B significantly underperforms Llama 2 13B on knowledge-intensive benchmarks: TriviaQA (63.4 vs 79.6), NaturalQuestions (23.0 vs 31.2) (Table 6). This suggests the smaller parameter count limits factual knowledge storage.

2. **Limited context length.** Models are trained on 8192-token context (Table 1). No long-context evaluation is provided, and no context extension method is applied.

3. **English-only optimization.** Unlike Gemini, Gemma is not trained for multilingual performance. The 256K vocabulary is inherited from Gemini but primarily serves English (Section 4).

4. **No pretraining details disclosed.** Data composition, training hyperparameters, optimizer settings, and learning rate schedules are not provided, limiting reproducibility significantly (Sections 3, 4).

5. **RLHF algorithm not specified.** The paper states a "novel reinforcement learning algorithm" is used for policy optimization but provides no details (Section 5).

6. **Safety evaluation limitations.** Human safety evaluation uses only ~400 prompts. Standard safety benchmarks show mixed results: Gemma 7B IT underperforms Mistral on BBQ Ambig (86.06 vs 97.53), Winogender (57.64 vs 64.3), TruthfulQA (45.34 vs 48.54), and Winobias 1_2 (59.22 vs 65.72) (Table 8).

7. **Open model risks acknowledged.** The paper acknowledges inability to prevent malicious fine-tuning and the challenge of protecting against toxic generation, hallucinations, and PII leakage without API-level filtering (Section 7).

8. **[Inferred]** No ablation studies isolating the contribution of individual architectural choices (MQA, GeGLU, RMSNorm) or data mixture decisions. It is unclear which factors drive the performance gains over baselines.

9. **[Inferred]** The comparison with LLaMA-2 is based on numbers from the original paper with a different evaluation setup, limiting direct comparability on individual benchmarks.

### Scope and Comparability

- **What was not tested:** Long-context performance, multilingual tasks, multimodal capabilities. No evaluation on tasks requiring context beyond 8K tokens. No evaluation on non-English benchmarks despite the multilingual vocabulary.
- **Comparability notes:** LLaMA-2 numbers are cited from the original paper due to licensing restrictions, not re-evaluated under the same setup. Some Mistral benchmarks (ARC, CQA, BBH, AGIEval, GSM8K, MBPP) were re-evaluated by the Gemma authors using Mistral's methodology. For MBPP specifically, Mistral reports 50.2 on a different split; on that split Gemma 7B achieves 54.5. HuggingFace H6 results provide independent evaluation replication for a subset of benchmarks.

---

## Conclusions

### Contributions

1. **State-of-the-art open 7B model.** Gemma 7B outperforms Llama 2 13B on MMLU (64.3 vs 54.8) and achieves the highest average score (56.9%) among compared open models on 18 benchmarks (Table 6).

2. **Strong math and coding performance.** Gemma 7B achieves 46.4% on GSM8K (+11 over Mistral 7B), 24.3% on MATH (+11.6 over Mistral 7B), and 44.4% on MBPP (exceeding CodeLLaMA-7B's 41.4%) (Table 6, Section 6).

3. **Two deployment-optimized sizes.** The 7B model targets GPU/TPU deployment; the 2B model with MQA targets CPU and on-device applications (Section 1).

4. **Technology transfer from frontier models.** Demonstrates that architectural innovations, training recipes, and safety practices from closed frontier models (Gemini) can be transferred to smaller open models (Sections 1, 8).

5. **Comprehensive safety evaluation.** Includes memorization analysis, 10 safety benchmarks (Table 8), human evaluation on safety prompts (Table 5), and discussion of open model risks (Sections 6, 7).

### Implications

1. **Open models can approach frontier quality at smaller scales.** The gap between open and closed models continues to narrow, with Gemma achieving Gemini-informed performance in a 7B model. However, this is speculative regarding "frontier quality" as no direct comparison with Gemini is provided.

2. **Training data quality and mixture may matter more than scale.** Gemma 7B outperforms Llama 2 13B despite fewer parameters, suggesting training methodology and data quality contribute significantly to capability. This interpretation is speculative since the pretraining details are undisclosed.

3. **Open release enables safety research.** By releasing pretrained checkpoints, Google DeepMind enables community research on interpretability, transparency, and safety that is not possible with API-only access (Section 7).

---

## Key Claims

1. **Gemma 7B outperforms Llama 2 13B on MMLU.** 64.3% vs 54.8% (+9.5 points). Scope: 5-shot evaluation, English-only. Evidence: Table 6. Status: **supported** (single evaluation configuration, LLaMA-2 numbers from different evaluation setup -- limited comparability).

2. **Gemma 7B achieves 46.4% on GSM8K, outperforming Mistral 7B by 11 points.** Scope: maj@1 evaluation, Mistral number re-evaluated by authors. Evidence: Table 6. Status: **supported** (single evaluation configuration, no variance reported -- limited evidence).

3. **Gemma 7B achieves 24.3% on MATH, nearly double Mistral 7B's 12.7%.** Scope: 4-shot evaluation. Evidence: Table 6. Status: **supported** (single evaluation configuration -- limited evidence).

4. **Gemma outperforms similarly sized open models on 11 out of 18 text-based tasks.** Scope: 18 benchmarks across Llama 2 7B/13B and Mistral 7B; LLaMA-2 numbers from original paper. Magnitude: 11/18 tasks with best score; average 56.9% vs next-best Mistral 7B 54.5%. Evidence: Abstract, Table 6. Status: **supported** (18 benchmarks across 4 baselines -- moderate evidence; but LLaMA-2 numbers not re-evaluated under same setup).

5. **Gemma 7B IT achieves 61.2% win rate over Mistral v0.2 7B Instruct on instruction following.** Scope: human evaluation on ~1000 prompts (creative writing, coding, instructions), Gemma 1.1 IT version. Magnitude: 61.2% [95% CI: 59.3%, 63%]. Evidence: Table 5. Status: **supported** (single comparison against one baseline -- moderate evidence; confidence intervals provided).

6. **Gemma 7B IT achieves 63.5% win rate on safety prompts.** Scope: human evaluation on ~400 safety prompts, Gemma 1.1 IT version. Magnitude: 63.5% [95% CI: 60.7%, 66.1%]. Evidence: Table 5. Status: **supported** (only ~400 prompts, single comparison -- limited evidence; confidence intervals provided).

7. **Gemma memorizes training data at comparable rates to PaLM models of similar size.** Scope: exact memorization using 50-token continuations, 10,000 sampled documents per corpus. Magnitude: ~0.1-1% exact memorization rate. Evidence: Figure 2. Status: **supported** (comparison against PaLM and PaLM 2 at comparable sizes -- moderate evidence).

8. **No sensitive personal data was memorized by Gemma models.** Scope: based on Google Cloud Sensitive Data Protection tool classification, which has known false positive issues. Magnitude: 0% sensitive data memorized. Evidence: Figure 3. Status: **unvalidated** (detection tool has known false positives, dataset classification not independently verified -- limited evidence).

---

## Open Questions

1. **Long-context performance.** How does Gemma perform on tasks requiring context beyond its 8K training length? Can context extension methods (e.g., RoPE scaling) be applied effectively? *Addressed by Gemma 3 (2025-03-gemma-3-technical-report), which extends context to 128K.*

2. **Pretraining data composition.** What is the detailed breakdown of web, code, and math data? What filtering criteria were applied? The paper states "primarily-English data from web documents, mathematics, and code" without quantitative detail. *Unresolved.*

3. **Instruction tuning transferability.** How does Gemma's SFT/RLHF recipe perform when applied to other base models? *Unresolved.*

4. **Optimal model size for deployment.** What tasks benefit most from the 7B vs 2B tradeoff? The 2B model underperforms on instruction following (45% win rate vs Mistral 7B) but performs well on safety (60.1% win rate). *Unresolved.*

5. **RLHF algorithm details.** What is the "novel reinforcement learning algorithm" used for policy optimization? No details are provided in the paper. *Unresolved.*

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that Gemma is based on.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Provides RoPE positional embeddings used in each Gemma layer.
- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head Is All You Need.* Provides multi-query attention used in the 2B model.
- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* Provides GeGLU activation function used in both models.
- **Zhang and Sennrich (2019)** -- *Root Mean Square Layer Normalization.* Provides RMSNorm used instead of LayerNorm.

### Training Infrastructure and Data

- **Barham et al. (2022)** -- *Pathways: Asynchronous Distributed Dataflow for ML.* Pathways distributed training approach used for orchestrating training across TPU pods.
- **Xu et al. (2021)** -- *GSPMD: General and Scalable Parallelization for ML Computation Graphs.* GSPMD partitioner used for training step computation.
- **Kudo and Richardson (2018)** -- *SentencePiece.* SentencePiece tokenizer (subset of Gemini's) used for tokenization.

### Training and Alignment

- **Christiano et al. (2017)** -- *Deep Reinforcement Learning from Human Preferences.* Foundation for RLHF used in instruction tuning.
- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback.* InstructGPT RLHF methodology informing Gemma's approach.
- **Bai et al. (2022)** -- *Constitutional AI: Harmlessness from AI Feedback.* Constitutional AI techniques used in LM-based judges for SFT data selection.
- **Wei et al. (2022)** -- *Chain of Thought Prompting Elicits Reasoning in Large Language Models.* Chain-of-thought prompting used in LM judges during SFT.
- **Zheng et al. (2023)** -- *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* LM-based side-by-side evaluation methodology for SFT data selection.

### Primary Comparisons

- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Primary comparison target; Gemma 7B outperforms Llama 2 13B on most benchmarks.
- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* LLaMA 1 comparison.
- **Jiang et al. (2023)** -- *Mistral 7B.* Direct 7B-scale comparison target; Gemma 7B outperforms on math and coding.
- **Almazrouei et al. (2023)** -- *The Falcon Series of Open Language Models.* Open model comparison referenced in introduction.

### Parent Model

- **Gemini Team (2023)** -- *Gemini: A Family of Highly Capable Multimodal Models.* Gemma's architectures, data pipelines, training recipes, and safety practices are derived from Gemini.

### Safety and Evaluation

- **Weidinger et al. (2021)** -- *Ethical and Social Risks of Harm from Language Models.* Framework for understanding LLM risks informing responsible deployment strategy.
- **Nasr et al. (2023)** -- *Scalable Extraction of Training Data from (Production) Language Models.* Adversarial attacks on aligned models; definition of discoverable memorization used in evaluation.
- **Carlini et al. (2022)** -- *Quantifying Memorization Across Neural Language Models.* Prior work on discoverable memorization referenced in memorization evaluation methodology.
- **Ippolito et al. (2022)** -- *Preventing Verbatim Memorization in Language Models Gives a False Sense of Privacy.* Approximate memorization methodology with 10% edit distance threshold.
