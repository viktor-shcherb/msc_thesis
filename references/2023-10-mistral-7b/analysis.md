---
title: "Mistral 7B"
authors: "Jiang, Sablayrolles, Mensch, Bamford, Chaplot, de las Casas, Bressand, Lengyel, Lample, Saulnier, Renard Lavaud, Lachaux, Stock, Le Scao, Lavril, Wang, Lacroix, El Sayed"
year: 2023
venue: "arXiv preprint 2310.06825"
paper_type: preprint
categories: ["model-release", "architecture", "attention-efficiency"]
scope: ["efficient 7B language model", "sliding window attention", "grouped-query attention", "rolling buffer cache", "model efficiency vs scale"]
benchmarks_used: ["mmlu", "hellaswag", "winogrande", "piqa", "arc", "siqa", "openbookqa", "natural-questions", "triviaqa", "boolq", "humaneval", "mbpp", "math-hendrycks", "gsm8k", "bbh", "agi-eval", "csqa", "mt-bench"]
models_introduced: ["mistral-7b"]
models_evaluated: ["llama-2-7b", "llama-2-13b", "llama-33b", "code-llama-7b"]
key_claims:
  - id: C1
    claim: "Mistral 7B outperforms Llama 2 13B across all evaluated benchmarks despite being nearly half the size"
    evidence: "Table 2, Figure 4, Section 3"
    status: supported
    scope: "12 benchmarks covering reasoning, knowledge, comprehension, math, code; re-evaluated with authors' own pipeline"
    magnitude: "margins from -0.2 (NQ: 28.8 vs 29.0) to +17.9 (GSM8K: 52.2 vs 34.3)"
  - id: C2
    claim: "Mistral 7B outperforms LLaMA 1 34B on reasoning, mathematics, and code generation benchmarks"
    evidence: "Figure 4, Section 3"
    status: supported
    scope: "math, code, and reasoning categories only; knowledge and comprehension not claimed"
    magnitude: "bar chart comparison only; exact deltas not tabulated"
  - id: C3
    claim: "Sliding window attention with W=4096 across 32 layers provides a theoretical attention span of approximately 131K tokens"
    evidence: "Section 2, Figure 1"
    status: supported
    scope: "theoretical receptive field via information propagation across layers; assumes no information loss per layer"
    magnitude: "W x k = 4096 x 32 = 131,072 tokens theoretical span"
  - id: C4
    claim: "Rolling buffer cache reduces cache memory by 8x on 32K-token sequences without impacting model quality"
    evidence: "Section 2, Figure 2"
    status: unvalidated
    scope: "32K-token sequence length, rolling buffer of size W=4096"
    magnitude: "8x cache memory reduction (32K/4K)"
  - id: C5
    claim: "Mistral 7B Instruct outperforms all 7B models on MT-Bench (6.84) and is comparable to 13B chat models"
    evidence: "Table 3, Section 4"
    status: supported
    scope: "MT-Bench and Chatbot Arena ELO; fine-tuned on public HuggingFace instruction datasets only"
    magnitude: "6.84 vs 6.27 (Llama 2 7B Chat), 6.84 vs 6.65 (Llama 2 13B Chat)"
  - id: C6
    claim: "Mistral 7B achieves equivalent performance to Llama 2 models 1.9-5.4x its size depending on benchmark category"
    evidence: "Figure 5, Section 3"
    status: supported
    scope: "estimated from Llama 2 7B/13B/70B scaling curves on MMLU, reasoning, knowledge, comprehension"
    magnitude: "equivalent to ~23B (MMLU, 3.3x), ~38B (reasoning, 5.4x), ~13B (knowledge, 1.9x), ~21B (comprehension, 3.0x)"
  - id: C7
    claim: "With the recommended system prompt, the model declines 100% of 175 unsafe prompts while maintaining higher MT-Bench than Llama 2's system prompt"
    evidence: "Table 4, Section 5.1"
    status: unvalidated
    scope: "175 curated unsafe prompts; Mistral system prompt only"
    magnitude: "100% refusal rate; MT-Bench 6.58 vs 6.38 with Llama 2 system prompt"
  - id: C8
    claim: "Self-reflection content moderation achieves 99.4% precision and 95.6% recall on a curated adversarial/standard prompt dataset"
    evidence: "Section 5.2"
    status: unvalidated
    scope: "manually curated balanced dataset of adversarial and standard prompts; Mistral 7B Instruct as classifier"
    magnitude: "99.4% precision, 95.6% recall (acceptable prompts as positives)"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Based on the Transformer decoder-only architecture with SWA and GQA modifications"
  - target: 2023-12-gqa-grouped-query-attention
    type: extends
    detail: "Uses GQA with 8 KV heads to reduce KV cache memory and improve inference throughput"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Primary comparison target; Mistral 7B outperforms Llama 2 13B on all benchmarks despite being nearly half the size"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "Outperforms LLaMA 1 34B on reasoning, mathematics, and code generation despite being 5x smaller"
  - target: 2025-04-attention-sink-emerges
    type: extended-by
    detail: "Empirical analysis of when and how attention sinks emerge in Mistral 7B"
  - target: 2025-04-retrieval-head-long-context-factuality
    type: extended-by
    detail: "Uses Mistral 7B to study retrieval heads for long-context factuality"
  - target: 2024-10-ruler-context-size
    type: extended-by
    detail: "RULER evaluates Mistral 7B's real context utilization capabilities"
  - target: 2024-05-yarn-context-extension
    type: extended-by
    detail: "YaRN extends Mistral 7B's context window using modified RoPE scaling"
  - target: 2024-07-llama-3-herd-of-models
    type: extended-by
    detail: "Llama 3 compares against Mistral 7B as a baseline open-weight model"
  - target: 2026-01-ministral-3-cascade-distillation
    type: extended-by
    detail: "Ministral 3 builds on Mistral architecture with GQA (32 query / 8 KV heads), derived via Cascade Distillation from Mistral Small 3.1"
  - target: 2024-03-gemma-open-models
    type: extended-by
    detail: "Gemma 7B outperforms Mistral 7B on math benchmarks (GSM8K +11 points, MATH +11.6 points) and coding (HumanEval +6.1 points)"
  - target: 2025-04-longgenbench-long-form-generation
    type: extended-by
    detail: "LongGenBench evaluates Mistral 7B v0.2 on long-form generation; achieves 81.8% CR but only 20.4% STIC-2 at 16K tokens"
open_questions:
  - question: "What is the training data mixture and total token count for Mistral 7B? The paper discloses no pretraining details."
    addressed_by: null
  - question: "How does SWA perform on tasks requiring global attention over the full context, compared to full attention?"
    addressed_by: 2024-10-ruler-context-size
  - question: "Does the theoretical 131K attention span of SWA translate to effective long-context performance in practice?"
    addressed_by: 2024-10-ruler-context-size
  - question: "What is the optimal scaling of sliding window size relative to model depth for different task types?"
    addressed_by: null
---

# Mistral 7B

**Authors:** Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lelio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothee Lacroix, William El Sayed (Mistral AI)
**Date:** October 2023, arXiv:2310.06825

---

## Core Research Problem

Scaling language models to achieve high performance typically requires increasing parameter count, which raises computational costs and inference latency, creating barriers to practical deployment. At the time of this paper, the dominant open-weight models -- Llama 2 (Touvron et al., 2023b) and LLaMA (Touvron et al., 2023a) -- demonstrated a clear correlation between model size and benchmark performance. However, the efficiency axis was underexplored: whether a smaller, carefully designed model could match or exceed larger models while maintaining lower inference cost. Additionally, standard full attention scales quadratically with sequence length, limiting practical context windows and increasing memory requirements during decoding. The core challenge was: **how to build a 7B-parameter model that outperforms the best 13B open model across all benchmarks while incorporating architectural innovations for efficient long-sequence handling.**

---

## Problem Solutions

Mistral 7B addresses the efficiency-performance tradeoff through two main contributions:

1. **Architectural efficiency.** Combine grouped-query attention (GQA, Ainslie et al., 2023) for reduced KV cache and faster decoding with sliding window attention (SWA, Child et al., 2019; Beltagy et al., 2020) for subquadratic attention over long sequences, plus a rolling buffer cache for fixed memory usage during generation.

2. **Superior performance at smaller scale.** Through undisclosed training data and methodology improvements, achieve a 7B model that outperforms Llama 2 13B on all evaluated benchmarks and LLaMA 1 34B on reasoning, mathematics, and code generation, demonstrating that model capabilities compress more efficiently than previously assumed.

---

## Approach Details

### Method

Mistral 7B is a decoder-only Transformer (Vaswani et al., 2017) with the following configuration (Table 1, Section 2):

| Parameter | Value |
|---|---|
| dim | 4096 |
| n_layers | 32 |
| head_dim | 128 |
| hidden_dim | 14336 |
| n_heads | 32 |
| n_kv_heads | 8 |
| window_size | 4096 |
| context_len | 8192 |
| vocab_size | 32000 |

The architecture retains standard components from the LLaMA family (RMSNorm, SwiGLU activations, RoPE positional encoding, BPE tokenizer with 32K vocabulary) and introduces three inference-focused innovations described below.

### Key Technical Components

#### Sliding Window Attention (SWA)

Each attention layer restricts each token to attend only to the W = 4096 preceding tokens in the previous layer, rather than all preceding tokens. However, because Transformers stack layers, information propagates across layers: the hidden state at position i in layer k, h_i, attends to all hidden states from the previous layer with positions between i - W and i. Recursively, h_i can access tokens from the input layer at a distance of up to W x k tokens (Section 2, Figure 1).

> Theoretical attention span: W x k = 4096 x 32 = ~131K tokens

In practice, for a sequence length of 16K with W = 4096, custom modifications to FlashAttention (Dao et al., 2022) and xFormers (Lefaudeux et al., 2022) yield a **2x speed improvement** over a vanilla attention baseline (Section 2).

#### Rolling Buffer Cache

The fixed window size enables a **rolling buffer cache** of fixed size W. Keys and values for timestep i are stored at position i mod W. When i > W, older entries are overwritten, capping cache size at W regardless of sequence length. On a 32K-token sequence, this **reduces cache memory by 8x** compared to storing the full KV cache, without impacting model quality (Section 2, Figure 2). Note: the "without impacting model quality" claim is stated without experimental evidence (no ablation comparing rolling buffer vs full cache).

#### Pre-fill and Chunking

For long prompts, the KV cache is pre-filled in chunks of size W. Each chunk attends to the rolling buffer cache (sliding window over previous chunks) and to itself via a causal mask. Tokens outside the sliding window from earlier chunks are not attended to (Section 2, Figure 3). This limits peak memory usage during prompt processing.

### Experimental Setup

**Evaluation benchmarks** (all re-evaluated with the authors' own evaluation pipeline for fair comparison):

- **Commonsense Reasoning (0-shot):** HellaSwag, WinoGrande, PIQA, SIQA, OpenbookQA, ARC-Easy, ARC-Challenge, CommonsenseQA
- **World Knowledge (5-shot):** NaturalQuestions, TriviaQA
- **Reading Comprehension (0-shot):** BoolQ, QuAC
- **Math:** GSM8K (8-shot, maj@8), MATH (4-shot, maj@4)
- **Code:** HumanEval (0-shot), MBPP (3-shot, hand-verified subset)
- **Aggregated:** MMLU (5-shot), BBH (3-shot), AGI Eval (3-5-shot, English MCQ only)

**Evaluation differences from Llama 2 paper:** (1) MBPP uses the hand-verified subset; (2) TriviaQA does not provide Wikipedia contexts (Section 3).

**Baselines:** Llama 2 7B, Llama 2 13B, Code-Llama 7B, and LLaMA 1 34B (since Llama 2 34B was not open-sourced).

**Training details:** The paper does not disclose pretraining data composition, total token count, training compute, hardware, or optimization hyperparameters. This is a significant gap for reproducibility.

**Reproducibility:** Code released at https://github.com/mistralai/mistral-src. Model weights released under Apache 2.0 on HuggingFace. No training seeds, data composition, or optimizer details reported. Deployment facilitated via vLLM (Kwon et al., 2023).

### Key Results

**Base model comparison (Table 2, Section 3):**

| Benchmark | Mistral 7B | Llama 2 7B | Llama 2 13B | Code-Llama 7B |
|---|---|---|---|---|
| MMLU | 60.1% | 44.4% | 55.6% | 36.9% |
| HellaSwag | 81.3% | 77.1% | 80.7% | 62.9% |
| WinoGrande | 75.3% | 69.5% | 72.9% | 62.3% |
| PIQA | 83.0% | 77.9% | 80.8% | 72.8% |
| ARC-Easy | 80.0% | 68.7% | 75.2% | 59.4% |
| ARC-Challenge | 55.5% | 43.2% | 48.8% | 34.5% |
| NaturalQuestions | 28.8% | 24.7% | 29.0% | 11.0% |
| TriviaQA | 69.9% | 63.8% | 69.6% | 34.9% |
| HumanEval | 30.5% | 11.6% | 18.9% | 31.1% |
| MBPP | 47.5% | 26.1% | 35.4% | 52.5% |
| MATH | 13.1% | 3.9% | 6.0% | 5.2% |
| GSM8K | 52.2% | 16.0% | 34.3% | 20.8% |

- Mistral 7B outperforms Llama 2 13B on **every benchmark** despite having roughly half the parameters (single eval pipeline, all models re-evaluated by the authors for comparability).
- On MMLU: +4.5 points over Llama 2 13B (60.1 vs 55.6), +15.7 over Llama 2 7B.
- On GSM8K: +17.9 points over Llama 2 13B (52.2 vs 34.3), +36.2 over Llama 2 7B.
- On HumanEval: +11.6 points over Llama 2 13B (30.5 vs 18.9), approaches Code-Llama 7B (31.1) without sacrificing non-code benchmarks.
- Weakest relative gains on world knowledge (NaturalQuestions: 28.8 vs 29.0 for Llama 2 13B), consistent with fewer parameters limiting stored knowledge.
- No variance estimates or confidence intervals reported for base model results (limited evidence on statistical significance).

**Equivalent model size analysis (Figure 5, Section 3):**

| Category | Equivalent Llama 2 Size | Compression Factor |
|---|---|---|
| MMLU (STEM reasoning) | ~23B | 3.3x |
| Reasoning | ~38B | 5.4x |
| Knowledge | ~13B | 1.9x |
| Comprehension | ~21B | 3.0x |

Mistral 7B achieves performance equivalent to Llama 2 models 1.9-5.4x its size depending on the category. The lower compression on knowledge benchmarks (1.9x) is attributed to the limited parameter count restricting stored factual knowledge (estimated from Llama 2 7B/13B/70B scaling curves; moderate evidence -- interpolation from 3 model sizes).

### Instruction Finetuning

Mistral 7B -- Instruct was fine-tuned on publicly available instruction datasets from Hugging Face. No proprietary data or special training tricks were used (Section 4).

**Chat model comparison (Table 3, Section 4):**

| Model | Chatbot Arena ELO | MT-Bench |
|---|---|---|
| WizardLM 13B v1.2 | 1047 | 7.2 |
| Mistral 7B Instruct | 1031 | 6.84 +/- 0.07 |
| Llama 2 13B Chat | 1012 | 6.65 |
| Vicuna 13B | 1041 | 6.57 |
| Llama 2 7B Chat | 985 | 6.27 |
| Vicuna 7B | 997 | 6.17 |
| Alpaca 13B | 914 | 4.53 |

- Mistral 7B Instruct achieves the highest MT-Bench score among all 7B models (6.84 vs 6.27 for Llama 2 7B Chat; reported as mean over 10 iterations with standard deviation).
- Comparable to 13B chat models: exceeds Llama 2 13B Chat (6.65) and Vicuna 13B (6.57) on MT-Bench.
- Independent human evaluation on llmboxing.com: Mistral 7B outputs preferred 5020 times vs 4143 for Llama 2 13B (as of October 6, 2023; Section 4, Figure 6).

### Guardrails and Content Moderation

**System prompt effect on MT-Bench (Table 4, Section 5.1):**

| Configuration | MT-Bench |
|---|---|
| No system prompt | 6.84 +/- 0.07 |
| Llama 2 system prompt | 6.38 +/- 0.07 |
| Mistral system prompt | 6.58 +/- 0.05 |

The Mistral system prompt ("Always assist with care, respect, and truth...") reduces MT-Bench less than the Llama 2 system prompt (-0.26 vs -0.46), while achieving 100% refusal rate on 175 unsafe prompts (Section 5.1). Notably, Mistral correctly answers "How to kill a linux process" with the system prompt, while Llama 2 13B Chat refuses (Table 5, Section 5.1).

**Self-reflection content moderation (Section 5.2):** Mistral 7B -- Instruct can classify prompts and responses into categories (illegal activities, hateful/violent content, unqualified advice). On a manually curated and balanced dataset of adversarial and standard prompts, self-reflection achieves **99.4% precision and 95.6% recall** (considering acceptable prompts as positives). Dataset size and composition are not disclosed, and no baseline comparisons are provided (limited evidence).

---

## Limitations and Failure Modes

The paper itself does not include an explicit limitations section. The only author-acknowledged limitation is the lower compression ratio on knowledge benchmarks (1.9x vs 3-5x on reasoning), which they attribute to the limited parameter count restricting stored knowledge (Section 3, Figure 5).

The following are inferred limitations:

1. **[Inferred]** No training details disclosed. The paper provides no information about pretraining data composition, total token count, training compute, hardware, optimizer settings, or learning rate schedule. This limits reproducibility and makes it impossible to assess whether performance gains come from architecture, data, or training methodology.

2. **[Inferred]** Limited long-context evaluation. Despite SWA providing a theoretical 131K attention span, the paper does not evaluate on any long-context benchmarks. The actual context length is 8192 tokens (Table 1), and no experiments test performance at or beyond this limit.

3. **[Inferred]** Safety evaluation is minimal. Safety is tested on only 175 prompts (Section 5.1), far fewer than the thousands used in Llama 2's evaluation. No standard toxicity benchmarks (ToxiGen, TruthfulQA) are reported for the base or instruct model.

4. **[Inferred]** Content moderation evaluation details missing. The self-reflection precision/recall numbers are reported on a "manually curated and balanced dataset" without disclosing the dataset size, composition, or baseline comparisons (Section 5.2).

5. **[Inferred]** No ablation studies. The paper does not ablate the contribution of individual components (SWA vs full attention, GQA vs MHA, rolling buffer vs full cache) to overall performance. It is unclear how much of the improvement comes from architecture vs data vs training.

6. **[Inferred]** No variance or confidence intervals on base model benchmarks. Only the MT-Bench scores report standard deviations (over 10 iterations). The Table 2 benchmark results appear to be single evaluations with no reported variance.

#### Scope and Comparability

- **What was not tested:** No long-context benchmarks (e.g., passkey retrieval, needle-in-a-haystack, SCROLLS). No multilingual evaluation. No toxicity or bias benchmarks. No evaluation at context lengths beyond 8K tokens. LLaMA 1 34B comparison is shown only in bar charts (Figure 4), not in the detailed Table 2.
- **Comparability notes:** All baselines were re-evaluated using the authors' own pipeline, which differs from the Llama 2 paper's protocol on at least two benchmarks (MBPP hand-verified subset, TriviaQA without Wikipedia context). This means Table 2 numbers may not be directly comparable to numbers reported in the original Llama 2 paper. The use of maj@8 for GSM8K and maj@4 for MATH (majority voting over multiple samples) should be noted when comparing to papers that report pass@1.

---

## Conclusions

### Contributions

1. **A 7B model that outperforms all open 13B models.** Mistral 7B surpasses Llama 2 13B on every evaluated benchmark, with particularly large margins on math (+17.9 on GSM8K), code (+11.6 on HumanEval), and MMLU (+4.5) (Table 2, Section 3).

2. **Sliding window attention with rolling buffer cache for efficient inference.** The combination of SWA (W=4096) with a fixed-size rolling buffer cache provides O(W) memory during generation regardless of sequence length, with a theoretical attention span of W x k = 131K tokens across 32 layers (Section 2).

3. **Demonstrated high compression of model capabilities.** On reasoning benchmarks, Mistral 7B matches a Llama 2 model estimated at ~38B parameters (5.4x compression), suggesting the capability-parameter relationship is more favorable than previously assumed (Figure 5, Section 3).

4. **Effective instruction-tuned variant with minimal effort.** Mistral 7B -- Instruct, fine-tuned only on public data without proprietary tricks, exceeds all 7B chat models and matches 13B chat models on MT-Bench (Table 3, Section 4).

5. **System prompting with reduced helpfulness penalty.** The Mistral system prompt achieves 100% refusal on 175 unsafe prompts while reducing MT-Bench by only 0.26 points (vs 0.46 for the Llama 2 system prompt), and avoids over-cautious refusals on benign queries like "How to kill a linux process" (Tables 4-5, Section 5.1).

### Implications

1. **The scaling laws problem is three-dimensional.** The paper argues that the field has focused on the two-dimensional relationship between model capabilities and training cost (Hoffmann et al., 2022), whereas the problem is three-dimensional: capabilities, training cost, and inference cost. Much remains unexplored in optimizing for inference efficiency (Section 6). This is a directional claim not rigorously validated.

2. **Smaller models may be more practical than scaling.** For many deployment scenarios, a well-trained 7B model may provide better cost-performance tradeoffs than a 13B or 34B model, particularly given the quadratic or rolling-buffer-bounded memory costs of attention. This implication is speculative beyond the specific benchmarks evaluated.

3. **SWA as a practical alternative to full attention.** The absence of reported quality degradation from SWA suggests that for decoder-only language modeling, local attention with information propagation across layers may be sufficient for most tasks. However, this remains unvalidated on long-context tasks requiring global reasoning.

---

## Key Claims

1. **Mistral 7B outperforms Llama 2 13B across all evaluated benchmarks.** Margins range from -0.2 points on NaturalQuestions (28.8 vs 29.0) to +17.9 on GSM8K (52.2 vs 34.3). Evidence: Table 2, Figure 4, Section 3. Status: **supported**. Scope: 12 benchmarks re-evaluated with authors' pipeline, covering reasoning, knowledge, comprehension, math, and code. Magnitude: +4.5 MMLU, +17.9 GSM8K, +11.6 HumanEval, +6.7 ARC-c. Evidence breadth: all models re-evaluated with a single common pipeline for fair comparison, but no variance estimates reported (moderate evidence -- consistent across 12 benchmarks but single-run evaluations).

2. **Mistral 7B outperforms LLaMA 1 34B on reasoning, mathematics, and code generation.** Evidence: Figure 4, Section 3. Status: **supported**. Scope: reasoning, math, and code categories only; knowledge and comprehension not claimed. Magnitude: shown in bar charts only, exact numbers not tabulated. Evidence breadth: bar chart comparison without exact values or error bars (limited evidence -- visual comparison only).

3. **SWA with W=4096 and 32 layers provides theoretical attention span of ~131K tokens.** Each layer propagates information W tokens forward; after k layers, the receptive field is W x k = 4096 x 32 = 131,072. Evidence: Section 2, Figure 1. Status: **supported** (theoretical; practical effectiveness not evaluated). Scope: theoretical receptive field assuming no information loss per layer. Magnitude: 131K tokens. Evidence breadth: mathematical derivation, no empirical validation of whether the theoretical span translates to usable context (theoretical argument only).

4. **Rolling buffer cache reduces cache memory by 8x on 32K sequences without quality impact.** Cache size is fixed at W=4096 regardless of sequence length. Evidence: Section 2, Figure 2. Status: **unvalidated**. Scope: 32K-token sequences, rolling buffer of size W=4096. Magnitude: 8x cache memory reduction. Evidence breadth: architectural description with no experimental evidence of quality preservation (no evidence -- claim is stated without supporting experiment).

5. **Mistral 7B Instruct outperforms all 7B models on MT-Bench and is comparable to 13B chat models.** MT-Bench 6.84 +/- 0.07 vs Llama 2 7B Chat 6.27 and Llama 2 13B Chat 6.65. Evidence: Table 3, Section 4. Status: **supported**. Scope: MT-Bench and Chatbot Arena ELO; fine-tuned on public HuggingFace datasets. Magnitude: +0.57 over Llama 2 7B Chat, +0.19 over Llama 2 13B Chat. Evidence breadth: MT-Bench averaged over 10 iterations with standard deviation reported; independent human eval on llmboxing.com corroborates (moderate evidence).

6. **Mistral 7B achieves equivalent performance to Llama 2 models 1.9-5.4x its size depending on benchmark category.** Equivalent sizes: 23B (MMLU, 3.3x), 38B (reasoning, 5.4x), 13B (knowledge, 1.9x), 21B (comprehension, 3.0x). Evidence: Figure 5, Section 3. Status: **supported**. Scope: estimated from Llama 2 7B/13B/70B scaling curves. Magnitude: 1.9x-5.4x compression depending on category. Evidence breadth: interpolation from 3 Llama 2 model sizes; lower bound on knowledge compression explicitly noted (moderate evidence).

7. **With the recommended system prompt, the model declines 100% of 175 unsafe prompts.** MT-Bench drops from 6.84 to 6.58 with the Mistral system prompt. Evidence: Table 4, Section 5.1. Status: **unvalidated**. Scope: 175 curated unsafe prompts; Mistral system prompt. Magnitude: 100% refusal rate; -0.26 MT-Bench penalty. Evidence breadth: small eval set (175 prompts), no standard safety benchmarks, no comparison to other safety methods (limited evidence).

8. **Self-reflection content moderation achieves 99.4% precision and 95.6% recall.** Evidence: Section 5.2. Status: **unvalidated**. Scope: manually curated balanced dataset of adversarial and standard prompts, Mistral 7B Instruct as classifier. Magnitude: 99.4% precision, 95.6% recall. Evidence breadth: dataset size and composition undisclosed, no baselines, no cross-validation details (limited evidence).

---

## Open Questions

1. **Pretraining details.** What data mixture, token count, compute budget, and optimization settings were used? Without these, it is impossible to determine whether Mistral 7B's gains come from architecture, data quality, data scale, or training methodology. Not addressed.

2. **SWA vs full attention quality.** Does SWA degrade performance on tasks requiring global context (e.g., document-level reasoning, long-range retrieval)? The paper provides no comparison between SWA and full attention on matched models. Partially addressed by RULER (2024-10-ruler-context-size), which evaluates Mistral 7B on long-context tasks and finds performance degrades significantly beyond the training context length.

3. **Long-context effectiveness.** The theoretical 131K span does not guarantee effective utilization. How does Mistral 7B perform on needle-in-a-haystack and other long-context tasks beyond its 8K context length? Partially addressed by RULER (2024-10-ruler-context-size) and retrieval head analysis (2025-04-retrieval-head-long-context-factuality).

4. **Optimal window size.** How sensitive is performance to the sliding window size W? Is W=4096 optimal, or would smaller/larger windows trade off efficiency and quality differently? Not addressed.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that Mistral 7B is based on.
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.* Provides grouped-query attention (8 KV heads for 32 query heads), reducing KV cache by 4x and accelerating inference.

### Sliding Window Attention Predecessors

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Introduces sparse attention patterns including local sliding windows. One of the two cited origins of SWA.
- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Combines local sliding window attention with global attention tokens. The other cited origin of SWA.

### Primary Comparisons

- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* The main comparison target. Mistral 7B outperforms Llama 2 13B on all benchmarks. Mistral 7B -- Instruct outperforms Llama 2 13B -- Chat.
- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* LLaMA 1 34B is the secondary comparison. Mistral 7B outperforms it on reasoning, math, and code.
- **Roziere et al. (2023)** -- *Code Llama: Open Foundation Models for Code.* Code-Llama 7B compared on code benchmarks; Mistral 7B approaches its coding performance without sacrificing general benchmarks.

### Scaling Laws

- **Hoffmann et al. (2022)** -- *An Empirical Analysis of Compute-Optimal Large Language Model Training (Chinchilla).* The paper's conclusion directly challenges Chinchilla's two-dimensional framing (capability vs training cost), arguing for a three-dimensional view including inference cost (Section 6).

### Efficient Inference

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Modified to support SWA, yielding 2x speedup over vanilla attention at 16K sequence length.
- **Kwon et al. (2023)** -- *Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM).* Reference implementation uses vLLM for deployment.

### Evaluation Benchmarks

- **Hendrycks et al. (2020)** -- *Measuring Massive Multitask Language Understanding (MMLU).* Primary aggregated benchmark; Mistral 7B achieves 60.1% (Table 2).
- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems (GSM8K).* Math reasoning benchmark where Mistral 7B shows its largest margin over Llama 2 13B (+17.9 points).
- **Chen et al. (2021)** -- *Evaluating Large Language Models Trained on Code (HumanEval).* Code generation benchmark where Mistral 7B nearly matches the specialized Code-Llama 7B.
