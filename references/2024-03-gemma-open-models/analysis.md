---
title: "Gemma: Open Models Based on Gemini Research and Technology"
authors: "Gemma Team, Google DeepMind"
year: 2024
venue: "arXiv preprint 2403.08295"
paper_type: preprint
categories: ["model-release", "architecture"]
scope: ["open-weight language models", "efficient 2B and 7B models", "instruction tuning", "RLHF", "safety evaluation"]
benchmarks_used: ["mmlu", "hellaswag", "piqa", "winogrande", "arc", "boolq", "triviaqa", "natural-questions", "humaneval", "mbpp", "gsm8k", "math-hendrycks", "bbh", "agi-eval", "csqa", "truthfulqa"]
models_introduced: ["gemma-2b", "gemma-7b"]
models_evaluated: ["llama-2-7b", "llama-2-13b", "mistral-7b"]
key_claims:
  - id: C1
    claim: "Gemma 7B outperforms Llama 2 13B on MMLU (64.3% vs 54.8%) despite having roughly half the parameters"
    evidence: "Table 6, Section Evaluation"
    status: supported
    scope: "5-shot evaluation"
    magnitude: "+9.5 percentage points over Llama 2 13B"
  - id: C2
    claim: "Gemma 7B achieves 46.4% on GSM8K, outperforming Mistral 7B (35.4%) by 11 points"
    evidence: "Table 6, Section Evaluation"
    status: supported
    scope: "maj@1 evaluation"
    magnitude: "+11 percentage points"
  - id: C3
    claim: "Gemma 7B achieves 24.3% on MATH, nearly double Mistral 7B's 12.7%"
    evidence: "Table 6, Section Evaluation"
    status: supported
    scope: "4-shot evaluation"
    magnitude: "+11.6 percentage points"
  - id: C4
    claim: "Gemma 7B outperforms similarly sized open models on 11 out of 18 text-based tasks"
    evidence: "Abstract, Table 6"
    status: supported
  - id: C5
    claim: "Gemma 7B IT achieves 61.2% win rate over Mistral v0.2 7B Instruct on instruction following"
    evidence: "Table 5, Section Human Preference Evaluations"
    status: supported
    scope: "human evaluation on ~1000 prompts"
  - id: C6
    claim: "Gemma 7B IT achieves 63.5% win rate over Mistral v0.2 7B Instruct on safety prompts"
    evidence: "Table 5, Section Human Preference Evaluations"
    status: supported
    scope: "human evaluation on ~400 safety prompts"
  - id: C7
    claim: "Gemma models memorize training data at comparable rates to PaLM models of similar size"
    evidence: "Figure 2, Section Memorization Evaluations"
    status: supported
    scope: "exact memorization using 50-token continuations"
  - id: C8
    claim: "No sensitive personal data was memorized by Gemma models"
    evidence: "Figure 3, Section Memorization Evaluations"
    status: unvalidated
    scope: "based on Google Cloud Sensitive Data Protection tool, which has known false positive issues"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Based on the Transformer decoder architecture with RoPE, GeGLU, and RMSNorm modifications"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Primary comparison target; Gemma 7B outperforms Llama 2 13B on most benchmarks"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "Compares against LLaMA 1 models"
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
---

# Gemma: Open Models Based on Gemini Research and Technology

**Authors:** Gemma Team, Google DeepMind (Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya Pathak, Laurent Sifre, et al.)
**Date:** February 2024, arXiv:2403.08295

---

## Core Research Problem

At the time of Gemma's release, open-weight language models such as Llama 2 (Touvron et al., 2023b) and Mistral 7B (Jiang et al., 2023) had established strong baselines for community research and commercial applications. However, these models were trained independently of the frontier closed models (e.g., Gemini, GPT-4), limiting the transfer of architectural insights, training recipes, and safety practices from the most capable systems. Google DeepMind's Gemini models (Gemini Team, 2023) demonstrated state-of-the-art performance but remained closed. The core challenge was: **how to release lightweight, openly available models that leverage Gemini's research and technology while maintaining strong safety properties and enabling broad community access.**

---

## Problem Solutions

Gemma addresses the gap between frontier closed models and open-weight alternatives through:

1. **Technology transfer from Gemini.** Apply the architectures, data pipelines, training recipes, and safety practices developed for Gemini to smaller, openly releasable models.

2. **Two model sizes for different deployment scenarios.** Provide a 7B model for GPU/TPU deployment and a 2B model for CPU and on-device applications.

3. **Both pretrained and instruction-tuned checkpoints.** Release base models for research and fine-tuning, plus instruction-tuned variants with SFT and RLHF for immediate application use.

4. **Comprehensive safety evaluation and filtering.** Apply data filtering, safety benchmarking, red teaming, and memorization analysis to reduce risks from open model release.

---

## Approach Details

### Architecture

Gemma uses a decoder-only Transformer architecture (Vaswani et al., 2017) with several post-Transformer improvements:

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

Parameter counts (Table 2):
- **Gemma 2B:** 524M embedding + 1.98B non-embedding = ~2.5B total
- **Gemma 7B:** 787M embedding + 7.75B non-embedding = ~8.5B total

The large vocabulary (256K tokens) inherited from Gemini accounts for the relatively high embedding parameter count.

### Key Technical Components

**Multi-Query Attention (MQA) for 2B.** The 2B model uses MQA (num_kv_heads = 1) based on ablations showing MQA works well at smaller scales (Shazeer, 2019). The 7B model uses standard multi-head attention.

**RoPE Embeddings.** Rotary positional embeddings (Su et al., 2021) are applied in each layer rather than absolute positional embeddings. Input and output embeddings are tied to reduce model size.

**GeGLU Activations.** The standard ReLU is replaced with the approximated GeGLU activation function (Shazeer, 2020).

**RMSNorm.** The input of each transformer sub-layer (attention and feedforward) is normalized with RMSNorm (Zhang and Sennrich, 2019) rather than LayerNorm.

### Training Data

- **Gemma 2B:** Trained on 3T tokens
- **Gemma 7B:** Trained on 6T tokens

Data sources include primarily-English web documents, mathematics, and code. Unlike Gemini, Gemma is not multimodal and is not optimized for multilingual tasks. The tokenizer is a subset of Gemini's SentencePiece tokenizer with 256K vocabulary, using byte-level encodings for unknown tokens.

**Data filtering:** Heuristics and model-based classifiers remove harmful or low-quality content. All evaluation sets are filtered from pretraining data with targeted contamination analysis. Personal information and sensitive data are filtered using automated techniques.

**Data mixture staging:** Following Gemini's approach, the corpus mixture is altered throughout training to increase the weight of relevant, high-quality data towards the end of training.

### Training Infrastructure

- **Hardware:** TPUv5e (256 chips per pod, configured as 16x16 2D torus)
- **7B model:** 16 pods = 4096 TPUv5e chips, 16-way model sharding + 16-way data replication
- **2B model:** 2 pods = 512 TPUv5e chips, 256-way data replication
- **Optimizer state:** Sharded using ZeRO-3-like techniques
- **Framework:** JAX with Pathways single-controller programming paradigm, GSPMD partitioner, MegaScale XLA compiler

**Carbon footprint:** Estimated ~131 tCO2eq for pretraining, offset by Google's carbon neutrality program.

### Instruction Tuning

**Supervised Fine-Tuning (SFT):** Fine-tuned on a mix of text-only, English-only synthetic and human-generated prompt-response pairs. Data mixtures selected using LM-based side-by-side evaluations (Zheng et al., 2023): a high-capability model judges preferences between test and baseline model responses. Different prompt sets test instruction following, factuality, creativity, and safety. LM judges use chain-of-thought prompting (Wei et al., 2022) and constitutional AI techniques (Bai et al., 2022).

**Synthetic data filtering:** Multiple filtering stages remove personal information, unsafe/toxic outputs, mistaken self-identification data, and duplicates. Subsets encouraging attribution, hedging, and refusals are included to minimize hallucinations.

**Formatting:** Special control tokens (`<start_of_turn>`, `<end_of_turn>`, `user`, `model`) delineate conversation turns.

**RLHF:** The SFT model is further fine-tuned using RLHF (Christiano et al., 2017; Ouyang et al., 2022). A reward function is trained on human-labeled English preference data using the Bradley-Terry model. The policy is trained using a "novel reinforcement learning algorithm" (not specified). High-capacity LM raters compute side-by-side comparisons to tune hyperparameters and mitigate reward hacking.

### Experimental Setup

**Evaluation methodology:** Most benchmarks use the same methodology as Gemini. For benchmarks compared with Mistral (ARC, CommonsenseQA, BBH, AGI Eval English-only), the Mistral technical report methodology is replicated. Due to restrictive licensing, LLaMA-2 numbers are cited from the original paper rather than re-evaluated.

**Baselines:** Llama 2 7B, Llama 2 13B, Mistral 7B.

**Human preference evaluation:** ~1000 prompts for instruction following (creative writing, coding, following instructions) and ~400 prompts for safety, evaluated against Mistral v0.2 7B Instruct.

### Key Results

**Academic benchmarks (Table 6):**

| Benchmark | Metric | LLaMA-2 7B | LLaMA-2 13B | Mistral 7B | Gemma 2B | Gemma 7B |
|---|---|---|---|---|---|---|
| MMLU | 5-shot, top-1 | 45.3 | 54.8 | 62.5 | 42.3 | **64.3** |
| HellaSwag | 0-shot | 77.2 | 80.7 | 81.0 | 71.4 | **81.2** |
| PIQA | 0-shot | 78.8 | 80.5 | **82.2** | 77.3 | 81.2 |
| BoolQ | 0-shot | 77.4 | 81.7 | **83.2** | 69.4 | **83.2** |
| WinoGrande | partial | 69.2 | 72.8 | **74.2** | 65.4 | 72.3 |
| ARC-c | - | 45.9 | 49.4 | 54.9 | 42.1 | **53.2** |
| TriviaQA | 5-shot | 72.1 | **79.6** | 62.5 | 53.2 | 63.4 |
| NQ | 5-shot | 25.7 | **31.2** | 23.2 | 12.5 | 23.0 |
| HumanEval | pass@1 | 12.8 | 18.3 | 26.2 | 22.0 | **32.3** |
| MBPP | 3-shot | 20.8 | 30.6 | 40.2 | 29.2 | **44.4** |
| GSM8K | maj@1 | 14.6 | 28.7 | 35.4 | 17.7 | **46.4** |
| MATH | 4-shot | 2.5 | 3.9 | 12.7 | 11.8 | **24.3** |
| AGIEval | - | 29.3 | 39.1 | 41.2 | 24.2 | **41.7** |
| BBH | - | 32.6 | 39.4 | 56.1 | 35.2 | 55.1 |
| **Average** | - | 46.9 | 52.4 | 54.5 | 45.0 | **56.9** |

Key observations:
- Gemma 7B outperforms Llama 2 13B on MMLU by +9.5 points (64.3 vs 54.8) despite having roughly half the parameters.
- Strong performance on math: GSM8K +11 points over Mistral 7B (46.4 vs 35.4), MATH +11.6 points (24.3 vs 12.7).
- Strong performance on code: HumanEval +6.1 points over Mistral 7B (32.3 vs 26.2), MBPP +4.2 points (44.4 vs 40.2). Gemma 7B exceeds CodeLLaMA-7B on MBPP (41.4%).
- Weaker on knowledge benchmarks: TriviaQA 63.4 vs Llama 2 13B's 79.6, NQ 23.0 vs 31.2.

**HuggingFace H6 benchmark (Table 7):**

| Benchmark | Mistral 7B | Gemma 7B |
|---|---|---|
| ARC-c | 60.0 | **61.9** |
| HellaSwag | **83.3** | 82.2 |
| MMLU | 64.2 | **64.6** |
| TruthfulQA | 42.2 | **44.8** |
| WinoGrande | 78.4 | **79.0** |
| GSM8K | 37.8 | **50.9** |
| **Average** | 61.0 | **63.8** |

**Human preference evaluation (Table 5, Gemma 1.1 IT):**

| Model | Safety Win Rate | Instruction Following Win Rate |
|---|---|---|
| Gemma 7B IT vs Mistral v0.2 7B | 63.5% [60.7%, 66.1%] | 61.2% [59.3%, 63%] |
| Gemma 2B IT vs Mistral v0.2 7B | 60.1% [57.3%, 62.8%] | 45% [43.1%, 46.9%] |

### Memorization Analysis

**Methodology:** Sample 10,000 documents from each corpus, use first 50 tokens as prompt, classify as memorized if subsequent 50 tokens exactly match ground truth. Also measure approximate memorization with 10% edit distance threshold.

**Results (Figure 2):** Gemma memorizes training data at comparable rates to PaLM models of similar size (~0.1-1% exact memorization depending on data source).

**Personal data (Figure 3):** No sensitive data was memorized. Some potentially "personal" data (as classified by Google Cloud Sensitive Data Protection) was memorized at lower rates than non-personal data, though the tool has known false positive issues.

**Approximate memorization (Figure 4):** Roughly 50% more data is approximately memorized than exactly memorized, consistent across data subcategories.

---

## Limitations and Failure Modes

1. **Knowledge benchmark weakness.** Gemma 7B significantly underperforms Llama 2 13B on knowledge-intensive benchmarks: TriviaQA (63.4 vs 79.6), NaturalQuestions (23.0 vs 31.2). This suggests the smaller parameter count limits factual knowledge storage.

2. **Limited context length.** Models are trained on 8192-token context. No long-context evaluation is provided, and no context extension method is applied.

3. **English-only optimization.** Unlike Gemini, Gemma is not trained for multilingual performance. The 256K vocabulary is inherited from Gemini but primarily serves English.

4. **No pretraining details disclosed.** Data composition, training hyperparameters, optimizer settings, and learning rate schedules are not provided, limiting reproducibility.

5. **RLHF algorithm not specified.** The paper states a "novel reinforcement learning algorithm" is used but provides no details.

6. **Safety evaluation limitations.** Human safety evaluation uses only ~400 prompts. Standard toxicity benchmarks (ToxiGen) show mixed results: Gemma 7B IT achieves 38.75 vs Mistral's 61.77 (lower is better on this benchmark).

7. **Open model risks acknowledged.** The paper acknowledges inability to prevent malicious fine-tuning and the challenge of protecting against toxic generation, hallucinations, and PII leakage without API-level filtering.

### Scope and Comparability

- **What was not tested:** Long-context performance, multilingual tasks, multimodal capabilities.
- **Comparability notes:** LLaMA-2 numbers are cited from the original paper (different evaluation setup) due to licensing restrictions. Some Mistral benchmarks were re-evaluated by the authors.

---

## Conclusions

### Contributions

1. **State-of-the-art open 7B model.** Gemma 7B outperforms Llama 2 13B on MMLU (64.3 vs 54.8) and achieves the highest average score (56.9%) among compared open models on 18 benchmarks.

2. **Strong math and coding performance.** Gemma 7B achieves 46.4% on GSM8K (+11 over Mistral 7B), 24.3% on MATH (+11.6 over Mistral 7B), and 44.4% on MBPP (exceeding CodeLLaMA-7B's 41.4%).

3. **Two deployment-optimized sizes.** The 7B model targets GPU/TPU deployment; the 2B model with MQA targets CPU and on-device applications.

4. **Technology transfer from frontier models.** Demonstrates that architectural innovations, training recipes, and safety practices from closed frontier models (Gemini) can be transferred to smaller open models.

5. **Comprehensive safety evaluation.** Includes memorization analysis, safety benchmarks, human evaluation on safety prompts, and discussion of open model risks.

### Implications

1. **Open models can approach frontier quality at smaller scales.** The gap between open and closed models continues to narrow, with Gemma achieving Gemini-informed performance in a 7B model.

2. **Training data quality and mixture may matter more than scale.** Gemma 7B outperforms Llama 2 13B despite fewer parameters, suggesting training methodology and data quality contribute significantly to capability.

3. **Open release enables safety research.** By releasing pretrained checkpoints, Google DeepMind enables community research on interpretability, transparency, and safety that is not possible with API-only access.

---

## Key Claims

1. **Gemma 7B outperforms Llama 2 13B on MMLU.** 64.3% vs 54.8% (+9.5 points). Evidence: Table 6. Status: **supported**.

2. **Gemma 7B achieves 46.4% on GSM8K, outperforming Mistral 7B by 11 points.** Evidence: Table 6. Status: **supported**.

3. **Gemma 7B achieves 24.3% on MATH, nearly double Mistral 7B's 12.7%.** Evidence: Table 6. Status: **supported**.

4. **Gemma outperforms similarly sized open models on 11 out of 18 text-based tasks.** Evidence: Abstract, Table 6. Status: **supported**.

5. **Gemma 7B IT achieves 61.2% win rate over Mistral v0.2 7B Instruct on instruction following.** Based on human evaluation of ~1000 prompts. Evidence: Table 5. Status: **supported**.

6. **Gemma 7B IT achieves 63.5% win rate on safety prompts.** Based on human evaluation of ~400 prompts. Evidence: Table 5. Status: **supported**.

7. **Gemma memorizes training data at comparable rates to PaLM.** Evidence: Figure 2. Status: **supported**.

8. **No sensitive personal data was memorized.** Based on Google Cloud Sensitive Data Protection tool. Evidence: Figure 3. Status: **unvalidated** (tool has known false positive issues, dataset classification not independently verified).

---

## Open Questions

1. **Long-context performance.** How does Gemma perform on tasks requiring context beyond its 8K training length? Can context extension methods (e.g., RoPE scaling) be applied effectively?

2. **Pretraining data composition.** What is the detailed breakdown of web, code, and math data? What filtering criteria were applied?

3. **Instruction tuning transferability.** How does Gemma's SFT/RLHF recipe perform when applied to other base models?

4. **Optimal model size for deployment.** What tasks benefit most from the 7B vs 2B tradeoff?

5. **RLHF algorithm details.** What is the "novel reinforcement learning algorithm" used for policy optimization?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that Gemma is based on.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Provides RoPE positional embeddings used in each Gemma layer.
- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head Is All You Need.* Provides multi-query attention used in the 2B model.
- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* Provides GeGLU activation function.
- **Zhang and Sennrich (2019)** -- *Root Mean Square Layer Normalization.* Provides RMSNorm used instead of LayerNorm.

### Training and Alignment

- **Christiano et al. (2017)** -- *Deep Reinforcement Learning from Human Preferences.* Foundation for RLHF used in instruction tuning.
- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback.* InstructGPT RLHF methodology.
- **Bai et al. (2022)** -- *Constitutional AI: Harmlessness from AI Feedback.* Constitutional AI techniques used in LM-based judges.
- **Wei et al. (2022)** -- *Chain of Thought Prompting Elicits Reasoning in Large Language Models.* Chain-of-thought prompting used in LM judges.

### Primary Comparisons

- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Primary comparison target; Gemma 7B outperforms Llama 2 13B.
- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* LLaMA 1 comparison.
- **Jiang et al. (2023)** -- *Mistral 7B.* Direct 7B-scale comparison target; Gemma 7B outperforms on math and coding.
- **Almazrouei et al. (2023)** -- *The Falcon Series of Open Language Models.* Open model comparison.

### Parent Model

- **Gemini Team (2023)** -- *Gemini: A Family of Highly Capable Multimodal Models.* Gemma's architectures, data pipelines, and training recipes are derived from Gemini.

### Safety and Evaluation

- **Zheng et al. (2023)** -- *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* LM-based side-by-side evaluation methodology for SFT data selection.
- **Weidinger et al. (2021)** -- *Ethical and Social Risks of Harm from Language Models.* Framework for understanding LLM risks informing responsible deployment.
