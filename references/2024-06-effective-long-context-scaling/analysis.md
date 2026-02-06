---
title: "Effective Long-Context Scaling of Foundation Models"
authors: "Xiong, Liu, Molybog, Zhang, Bhargava, Hou, Martin, Rungta, Sankararaman, Oguz, Khabsa, Fang, Mehdad, Narang, Malik, Fan, Bhosale, Edunov, Lewis, Wang, Ma"
year: 2024
venue: "NAACL 2024"
paper_type: conference-paper
categories: ["context-extension", "position-encoding", "model-release"]
scope: ["RoPE-based LLMs", "continual pretraining", "long-context scaling", "Llama 2 family"]
benchmarks_used: ["humaneval", "mbpp", "gsm8k", "math-hendrycks", "mmlu", "natural-questions", "triviaqa", "hellaswag", "winogrande", "arc", "piqa", "csqa", "zeroscrolls", "l-eval", "truthfulqa", "toxigen", "bold"]
models_introduced: ["llama-2-long-7b", "llama-2-long-13b", "llama-2-long-34b", "llama-2-long-70b"]
models_evaluated: ["llama-2-7b", "llama-2-13b", "llama-2-70b", "gpt-3.5-turbo", "gpt-4", "mistral-7b", "mpt-7b", "claude-2.1"]
key_claims:
  - id: C1
    claim: "RoPE base frequency adjustment (ABF) outperforms Position Interpolation (PI) for long-context extension"
    evidence: "Table 5, Table 6, Figure 5, Section 4.1"
    status: supported
    scope: "Llama 2 7B, 32k context"
  - id: C2
    claim: "Validation loss follows power-law scaling with context length: L(c) = (alpha/c)^beta + gamma"
    evidence: "Figure 1, Section 3.1"
    status: supported
    scope: "Llama 2 Long 7B-70B, up to 32k context"
  - id: C3
    claim: "Long-context continual pretraining saves ~40% FLOPs compared to pretraining from scratch with no performance loss"
    evidence: "Table 10, Table 11, Section 4.4"
    status: supported
    scope: "7B model, 32k context"
  - id: C4
    claim: "Data quality matters more than length distribution for long-context continual pretraining"
    evidence: "Table 7, Table 8, Section 4.2"
    status: supported
    scope: "7B model ablations"
  - id: C5
    claim: "Llama 2 Long 70B Chat outperforms gpt-3.5-turbo-16k on 7/10 ZeroSCROLLS tasks without human-annotated long data"
    evidence: "Table 4, Section 3.2"
    status: supported
  - id: C6
    claim: "Llama 2 Long improves over Llama 2 on short-context benchmarks, especially coding, math, and MMLU"
    evidence: "Table 1, Table 2, Section 3.1"
    status: supported
cross_references:
  - target: 2023-07-llama-2-open-foundation-chat
    type: extends
    detail: "Llama 2 Long is built through continual pretraining from Llama 2 checkpoints with 400B additional tokens"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Modifies RoPE's base frequency from 10,000 to 500,000 to reduce attention decay for distant tokens"
  - target: 2023-06-pi-positional-interpolation
    type: contradicts
    detail: "Shows that RoPE ABF outperforms Position Interpolation on both perplexity and downstream tasks (Table 5, Table 6)"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "YaRN evaluated as baseline; Llama 2 Long 7B outperforms Yarn-7B-128k and Yarn-13B-128k on long-context tasks (Table 3)"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: uses-benchmark
    detail: "Uses ZeroSCROLLS for instruction-tuned model evaluation, outperforming gpt-3.5-turbo-16k on 7/10 tasks"
  - target: 2024-08-l-eval-standardized-evaluation
    type: uses-benchmark
    detail: "Evaluates on L-Eval tasks including Coursera, TPO, TopicRetrieval, FinQA, ContractQA, NaturalQuestions (Table 17)"
  - target: 2022-12-flashattention
    type: complementary
    detail: "Uses FlashAttention for efficient training with negligible GPU memory overhead when increasing sequence length"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "Compares to ALiBi's approach; both address long-context via positional encoding modifications but RoPE ABF operates on RoPE-based models"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention cited as concurrent long-context work; Llama 2 Long uses continual pretraining rather than architectural modifications"
  - target: 2024-07-llama-3-herd-of-models
    type: extended-by
    detail: "Llama 3 adopts similar RoPE base frequency scaling approach for long-context extension"
  - target: 2025-07-lv-eval-long-context-benchmark
    type: complementary
    detail: "LV-Eval provides a controlled long-context evaluation framework with knowledge-leakage mitigation, complementing the training methods proposed in this paper"
open_questions:
  - question: "Why does the power-law exponent beta increase with model size (0.45 for 7B to 0.51 for 70B)?"
    addressed_by: null
  - question: "Can the training curriculum findings (40% FLOP savings) scale to longer contexts (64k+) and larger models?"
    addressed_by: null
  - question: "What is the optimal base frequency for different target context lengths beyond 32k?"
    addressed_by: 2024-07-longrope-context-extension
---
# Effective Long-Context Scaling of Foundation Models

**Authors:** Wenhan Xiong, Jingyu Liu, Igor Molybog, et al. (GenAI, Meta)
**Date:** June 2024, NAACL 2024; arXiv:2309.16039

---

## Core Research Problem

Large language models with robust long-context capabilities are primarily available through proprietary APIs (Anthropic, OpenAI). Existing open-source long-context models fall short in three ways: (1) they primarily measure long-context capabilities via language modeling loss and synthetic tasks, which do not demonstrate real-world effectiveness (Section 1); (2) they often overlook maintaining strong performance on standard short-context tasks, either bypassing evaluations or reporting degraded performance (Chen et al., 2023; Peng et al., 2023); and (3) there is no open recipe for building long-context models that match proprietary model performance.

A key technical limitation is that Llama 2's RoPE positional encoding imposes a heavy decay on attention scores for distant tokens, preventing the attention module from aggregating information beyond 4,000-6,000 tokens even after extensive continual pretraining (Section 4.1). The core challenge is: **how to extend Llama 2's context window to 32k tokens while improving (not degrading) performance on both long-context and short-context tasks.**

---

## Problem Solutions

The paper presents Llama 2 Long, a series of long-context LLMs supporting effective context windows of 32,768 tokens, built through:

1. **RoPE base frequency adjustment (ABF):** Increase the RoPE base frequency from b = 10,000 to b = 500,000, which reduces the rotation angle per dimension and attenuates the attention score decay for distant tokens (Section 2.1, Section 4.1).

2. **Continual pretraining:** Train from Llama 2 checkpoints with 400B additional tokens formed as long sequences (32k for 7B/13B, 16k for 34B/70B), rather than pretraining from scratch (Section 2.1).

3. **Quality-focused data mix:** Up-sample long texts but prioritize data quality over length distribution; the quality of the data plays a more critical role than the length of texts (Section 4.2).

4. **Cost-effective instruction tuning:** Use Llama 2 Chat's RLHF data augmented with synthetic self-instruct long QA data generated by Llama 2 Chat itself, without any human-annotated long instruction data (Section 2.2).

---

## Approach Details

### Method

**RoPE Base Frequency Adjustment (ABF):**

RoPE maps position m to rotation angles via:

> f^{RoPE}(x, m)_j = (x_{2j} + ix_{2j+1}) e^{i b^{-2j/d} m}

where b = 10,000 is the base frequency and d is the model dimension. The attention score decays as relative position |m - n| increases (Figure 4). Increasing b to 500,000 reduces the rotation angles, which reduces the decaying effect for distant tokens.

The paper provides theoretical analysis (Appendix B) showing that ABF distributes embedded vectors with increased granularity compared to Position Interpolation (PI). The distance between consecutive embedding images scales as:

> For ABF: C_d ~ (log b + log beta)^{-1}
> For PI: C_d ~ alpha * (log b)^{-1}

With b = 10,000, alpha = 1/4 (PI), and beta = 50 (ABF), the granularity is 0.076 for ABF vs 0.027 for PI, making it easier for the model to distinguish between positions with ABF.

**Continual Pretraining:**

- 400B tokens over 100,000 steps
- 7B/13B: 32,768-token sequences; 34B/70B: 16,384-token sequences
- Same number of tokens per batch as Llama 2 (4M tokens per gradient update)
- Learning rate: 2e-5 for 7B/13B, 1e-5 for 34B/70B (smaller LR critical for larger models)
- Cosine schedule with 2000 warm-up steps
- FlashAttention for memory efficiency; ~17% speed loss when increasing from 4k to 16k for 70B

**Power-Law Scaling:**

Validation loss follows a power-law relationship with context length (Figure 1):

> L(c) = (alpha/c)^beta + gamma

Fitted parameters for each model size:

| Model | alpha | beta | gamma |
|---|---|---|---|
| Llama 2 Long 7B | 25.4 | 0.45 | 1.56 |
| Llama 2 Long 13B | 19.5 | 0.48 | 1.45 |
| Llama 2 Long 34B | 17.7 | 0.50 | 1.41 |
| Llama 2 Long 70B | 17.9 | 0.51 | 1.35 |

Larger models have larger beta, indicating they leverage contexts more effectively.

### Key Technical Components

**Position Interpolation (PI) Comparison:**

PI linearly scales input positions by alpha = L/L' so that positions in long sequences map to the original position range. Both PI and ABF reduce attention decay, but ABF provides higher granularity between consecutive position embeddings (Theorem 1, Appendix B).

| PE Variant | 32k Perplexity (Books) | FIRST-SENTENCE-RETRIEVAL | HumanEval | MMLU |
|---|---|---|---|---|
| RoPE (baseline) | 6.548 | Fails beyond 4-6k | 14.63 | 45.69 |
| RoPE PI | 6.341 | Degrades at 24k+ | 15.24 | 45.84 |
| RoPE ABF | **6.323** | Maintains to 32k | **17.07** | **46.24** |
| xPos ABF | 6.331 | Similar to ABF | 16.46 | 45.72 |

(Table 5, Table 6, Figure 5)

**xPos Comparison:**

xPos smooths high-frequency oscillation in RoPE that could be undesirable for language modeling. However, with base frequency modification, xPos does not outperform RoPE ABF on perplexity, downstream tasks, or extrapolation (Table 5, Table 6, Appendix C).

**Instruction Tuning Without Human Annotation:**

1. Take Llama 2 Chat's RLHF dataset (short prompts)
2. Generate synthetic long QA data via self-instruct:
   - Select random chunk from long document
   - Prompt Llama 2 Chat to write QA pairs
   - Apply self-critique step for verification
   - Use original long document as context
3. Concatenate short instruction data as 16k sequences
4. For long data: add padding, process individually without truncation
5. **Key finding:** Calculate LM loss on long input prompts (not just output tokens) gives consistent improvements (Table 9)

### Experimental Setup

**Models:** Llama 2 Long 7B, 13B, 34B, 70B; all continually pretrained from Llama 2 checkpoints.

**Short-context benchmarks:**
- Coding: HumanEval (0-shot), MBPP (3-shot)
- Math: GSM8K (8-shot), MATH (4-shot)
- Knowledge: MMLU (5-shot), NaturalQuestions (5-shot), TriviaQA (5-shot)
- Commonsense: PIQA, SIQA, HellaSwag, WinoGrande, ARC, OpenBookQA, CommonsenseQA

**Long-context benchmarks:**
- NarrativeQA (0-shot), QuALITY (2-shot), Qasper (2-shot), QMSum (1-shot)
- ZeroSCROLLS (10 tasks)
- L-Eval (6 tasks)

**Baselines:** Focused Transformer 3B, YaRN 7B/13B-128k, Together-7B-32k, Xgen-7B-8k, MPT-7B-8k/30B-8k, GPT-3.5-turbo, GPT-3.5-turbo-16k, GPT-4, Claude

**Reproducibility:** No code release mentioned. Training details provided (Section 2.1). Hyperparameters specified (learning rates, batch sizes, schedules). Evaluation prompts described (footnote 2, Appendix D).

### Key Results

**Short-context benchmarks (Table 1, Table 2):**

| Model | Size | Coding | Math | MMLU | Commonsense | OpenQA |
|---|---|---|---|---|---|---|
| Llama 2 | 70B | 37.4 | 35.2 | 68.9 | 71.9 | 63.6 |
| Llama 2 Long | 70B | **39.9** | **41.3** | **71.7** | **72.7** | **64.0** |

- Llama 2 Long **improves** over Llama 2 on all aggregated metrics
- 70B: +2.5 Coding, +6.1 Math, +2.8 MMLU
- Outperforms GPT-3.5 on MMLU (71.7 vs 70.0) and GSM8K (65.4 vs 57.1)

**Long-context benchmarks (Table 3):**

| Model | NarrativeQA F1 | Qasper F1 | QuALITY EM | QMSum ROUGE |
|---|---|---|---|---|
| YaRN-7B-128k | 20.9 | 26.2 | 32.3 | 11.4 |
| YaRN-13B-128k | 23.4 | 27.1 | 46.4 | 11.9 |
| Llama 2 Long 7B | 21.9 | 27.8 | 43.2 | **14.9** |
| Llama 2 Long 13B | 25.6 | **31.2** | **57.6** | **15.7** |
| Llama 2 Long 70B | **30.9** | **35.7** | **79.7** | **16.5** |

- Llama 2 Long 13B outperforms YaRN-13B-128k on all tasks
- Performance improves monotonically as max context length increases (Figure 2)

**ZeroSCROLLS instruction-tuned results (Table 4):**

| Model | GR | SS | QM | SQAL | Qspr | Nrtv | QALT | MuSQ | SpDg | BkSS | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-3.5-turbo-16k | 24.3 | 16.2 | 17.4 | 21.4 | 50.0 | 29.5 | 72.0 | 27.0 | 54.1 | 54.6 | 36.7 |
| Llama 2 Long Chat 70B | **26.0** | 15.0 | **20.0** | 20.9 | **52.0** | **31.7** | **82.6** | 27.3 | **55.5** | 46.2 | **37.7** |

- Outperforms GPT-3.5-turbo-16k on **7/10 tasks** (underscored)
- Achieved without any human-annotated long-context data

**Training curriculum ablation (Table 10, Table 11):**

| Curriculum | FLOPs | NarrativeQA | Qasper | Quality | QMSum |
|---|---|---|---|---|---|
| 32k from scratch | 3.783 × 10^22 | 18.5 | 28.6 | 37.9 | 11.46 |
| 4k→32k @ 20% | 3.405 × 10^22 | 20.0 | 28.1 | 38.8 | 12.09 |
| 4k→32k @ 40% | 3.026 × 10^22 | 20.1 | 27.0 | 37.4 | 12.44 |
| 4k→32k @ 80% | 2.270 × 10^22 | 18.5 | 25.0 | 38.3 | 11.00 |

- Switching at 40% saves ~40% FLOPs with no performance loss on perplexity
- Models quickly adapt to increased sequence length within a few thousand steps (Figure 6)

**Data mix ablation (Table 7, Table 8):**

| Data Mix | NarrativeQA Δ | Qasper Δ | Quality Δ | MMLU |
|---|---|---|---|---|
| Llama 2 Long data mix | **23.70%** | **43.64%** | **75.5%** | **48.62** |
| Llama 2 data mix | 18.23% | 38.12% | 60.3% | 46.30 |
| - remove long text data | 19.48% | 39.14% | 67.1% | 46.25 |
| - upsample existing long | 22.15% | 36.82% | 65.0% | 46.25 |

- Removing long texts still achieves most gains; upsampling long texts provides no consistent advantage
- **Data quality matters more than length distribution**

---

## Limitations and Failure Modes

1. **Limited functionality for long-form outputs.** The model has not been finetuned for applications requiring long-form generation such as creative writing (Section 6).

2. **Tokenizer efficiency.** The Llama tokenizer (32k vocabulary) produces ~10% more tokens than GPT-3.5's tokenizer and cannot efficiently handle whitespace, making it inefficient for long code data (Section 6).

3. **Hallucination.** Like other LLMs, hallucination is observed, potentially more pronounced for long-context models due to dense information consumption and insufficient alignment (Section 6).

4. **34B/70B trained on shorter sequences.** The larger models were trained with 16k sequences rather than 32k due to computational constraints, though they still support 32k inference.

5. **Evaluation limitations.** Automatic metrics for summarization (single ground-truth, n-gram matching) do not align with human preference. Input truncation may remove necessary information. Proprietary models may have data leakage concerns (Section 3.2).

6. **No passkey retrieval evaluation.** The paper uses FIRST-SENTENCE-RETRIEVAL but notes "passkey task is overly simple for context probing" (footnote 4), not providing systematic needle-in-haystack evaluation.

### Scope and Comparability

- **What was not tested:** Context lengths beyond 32k; models beyond Llama 2 family; complex reasoning tasks over long contexts.
- **Comparability notes:** Together-7B-32k is not purely pretrained (finetuned with supervised data), making comparison imperfect. Maximum prompt length set to 16,384 tokens for long-task comparison (some models support longer).

---

## Conclusions

### Contributions

1. **RoPE base frequency adjustment (ABF) for long-context.** Introduced a minimal modification to RoPE (b: 10,000 → 500,000) that outperforms Position Interpolation on perplexity, synthetic retrieval tasks, and downstream benchmarks. Provided theoretical analysis showing ABF provides higher positional granularity (Section 4.1, Appendix B).

2. **Power-law context scaling.** Demonstrated that validation loss follows L(c) = (alpha/c)^beta + gamma, establishing context length as another important axis of LLM scaling. Larger models have larger beta exponents, indicating more effective context utilization (Figure 1).

3. **Efficient continual pretraining recipe.** Showed that switching from 4k to 32k sequences at 40% of training saves ~40% FLOPs with equivalent performance, validating continual pretraining from short-context models (Section 4.4).

4. **Data quality over length distribution.** Ablations show that long-context capabilities can be trained with limited long data; improvements come from data quality, not length distribution (Section 4.2).

5. **Cost-effective long-context instruction tuning.** Achieved GPT-3.5-turbo-16k-competitive performance on ZeroSCROLLS using only synthetic self-instruct data without human annotation. Key insight: calculating LM loss on long input prompts improves performance (Section 2.2, Section 4.3).

6. **Short-context improvements.** Unlike prior work reporting degradation, Llama 2 Long improves over Llama 2 on short-context benchmarks, attributed to additional compute and knowledge from new data (Section 3.1).

### Implications

1. **Continual pretraining is sufficient for long-context.** The successful training curriculum ablation suggests that long-context capabilities can be efficiently added post-hoc without architectural changes beyond positional encoding modifications.

2. **Sparse attention may not be necessary at 32k.** For Llama 2 70B (h = 8192), attention only becomes a bottleneck beyond 49,152 tokens (6h), suggesting full attention remains viable for moderate context extensions (Section 2.1).

3. **Human annotation may be unnecessary for long-context alignment.** The success of self-instruct long data suggests scalable approaches to long-context instruction tuning without expensive human annotation (speculative beyond QA tasks).

---

## Key Claims

**C1. RoPE ABF outperforms Position Interpolation for long-context extension.** ABF achieves lower perplexity (6.323 vs 6.341 on 32k Books), maintains FIRST-SENTENCE-RETRIEVAL to 32k (PI degrades at 24k+), and improves downstream tasks (HumanEval: 17.07 vs 15.24, MMLU: 46.24 vs 45.84) (Table 5, Table 6, Figure 5). Theoretical analysis shows ABF provides 2.8x higher positional granularity (Appendix B). Status: **supported**.

**C2. Validation loss follows power-law scaling with context length.** L(c) = (alpha/c)^beta + gamma fits all model sizes with R² implied by Figure 1. The 70B model's beta = 0.51 indicates ~30% loss reduction when doubling context (2^{-0.51} ≈ 0.70). Status: **supported**.

**C3. Continual pretraining saves ~40% FLOPs compared to pretraining from scratch.** Switching from 4k to 32k at 40% of training uses 3.026 × 10^22 FLOPs vs 3.783 × 10^22 for 32k from scratch (-20%), with equivalent perplexity (Table 11) and comparable long-context task performance (Table 10). Status: **supported**. Note: The "40%" savings is computed from curriculum switching, actual savings depend on switch point.

**C4. Data quality matters more than length distribution for long-context training.** Removing long texts from Llama 2 data still achieves most performance gains (NarrativeQA: 19.48% vs 23.70% with new data). Upsampling existing long texts (22.15%) does not consistently outperform removing long texts (19.48%) (Table 7). Status: **supported**.

**C5. Llama 2 Long 70B Chat outperforms gpt-3.5-turbo-16k on 7/10 ZeroSCROLLS tasks.** Specifically: GR (26.0 vs 24.3), QM (20.0 vs 17.4), Qspr (52.0 vs 50.0), Nrtv (31.7 vs 29.5), QALT (82.6 vs 72.0), SpDg (55.5 vs 54.1), overall average (37.7 vs 36.7) (Table 4). Status: **supported**.

**C6. Llama 2 Long improves over Llama 2 on short-context benchmarks.** 70B improvements: Coding +2.5 (39.9 vs 37.4), Math +6.1 (41.3 vs 35.2), MMLU +2.8 (71.7 vs 68.9), Commonsense +0.8 (72.7 vs 71.9), OpenQA +0.4 (64.0 vs 63.6) (Table 1). Attributed to additional FLOPs and knowledge from new data. Status: **supported**.

---

## Open Questions

1. **Why does the power-law exponent beta increase with model size?** The paper observes beta increasing from 0.45 (7B) to 0.51 (70B) but does not explain the mechanism. Is this related to attention head count, hidden dimension, or emergent capabilities? Unresolved.

2. **Can the training curriculum findings scale to longer contexts and larger models?** The 40% FLOP savings are demonstrated at 7B scale with 32k context. Whether this generalizes to 64k+, 128k, or million-token contexts remains untested. Partially addressed by: `2024-07-longrope-context-extension` (LongRoPE uses progressive extension to 2048k).

3. **What is the optimal base frequency for different target context lengths?** The paper uses b = 500,000 for 32k context. The relationship between optimal b and target context length is not characterized. Addressed by: `2024-07-longrope-context-extension` (LongRoPE uses search-based methods to find optimal rescale factors).

4. **Does the LM loss on input prompts generalize beyond QA tasks?** The instruction tuning finding that LM loss on inputs helps is specific to long QA tasks with unbalanced input/output lengths. Generalization to other task types is unknown. Unresolved.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations

- **Su et al. (2022)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding modified in this work. The base frequency b = 10,000 is the parameter adjusted to b = 500,000.
- **Sun et al. (2022)** -- *A Length-Extrapolatable Transformer (xPos).* Alternative rotary encoding that smooths high-frequency oscillation. Evaluated as XPOS ABF but found not to outperform RoPE ABF.

### Direct Predecessors (Context Extension Methods)

- **Chen et al. (2023)** -- *Extending Context Window via Positional Interpolation.* Concurrent approach that linearly scales positions. ABF is shown to outperform PI on perplexity and downstream tasks (Table 5, Table 6).
- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension.* Evaluated as baseline. Llama 2 Long outperforms YaRN-7B-128k and YaRN-13B-128k on all long-context tasks (Table 3).
- **Mohtashami & Jaggi (2023)** -- *Landmark Attention.* Concurrent long-context work; their passkey task is noted as "overly simple for context probing" (footnote 4).

### Base Models

- **Touvron et al. (2023)** -- *Llama 2: Open Foundation and Fine-tuned Chat Models.* The base model that Llama 2 Long extends through continual pretraining. RLHF dataset used for instruction tuning.

### Concurrent Long-Context Models (Baselines)

- **Tworkowski et al. (2023)** -- *Focused Transformer.* Baseline model using contrastive training for context scaling (Table 3).
- **MosaicML (2023)** -- *MPT-7B/30B.* Baseline long-context models evaluated in Table 3.
- **Nijkamp et al. (2023)** -- *Xgen-7B.* Baseline with 8k context (Table 3).
- **Together (2023)** -- *Llama-2-7B-32K.* PI-based 32k model; noted as finetuned with supervised data, not purely pretrained.
- **Rozière et al. (2023)** -- *Code Llama.* Concurrently suggests the base frequency modification idea.

### Scaling Laws

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Foundational scaling laws work; power-law context scaling (Figure 1) extends this paradigm to context length.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Scaling laws reference for the power-law formulation.

### Evaluation Benchmarks

- **Shaham et al. (2023)** -- *ZeroSCROLLS.* Primary long-context evaluation benchmark for instruction-tuned model (Table 4).
- **An et al. (2023)** -- *L-Eval.* Additional long-context evaluation benchmark (Table 17).
- **Kočiský et al. (2018)** -- *NarrativeQA.* Long-context QA benchmark.
- **Pang et al. (2022)** -- *QuALITY.* Long-context multiple-choice QA benchmark.
- **Dasigi et al. (2021)** -- *Qasper.* Scientific paper QA benchmark.
- **Zhong et al. (2021)** -- *QMSum.* Query-based meeting summarization benchmark.

### Training Infrastructure

- **Dao et al. (2022)** -- *FlashAttention.* Enables efficient long-sequence training with negligible GPU memory overhead.

### Safety Evaluation

- **Lin et al. (2021)** -- *TruthfulQA.* Factuality benchmark for safety evaluation (Table 12).
- **Hartvigsen et al. (2022)** -- *ToxiGen.* Toxicity benchmark (Table 12).
- **Dhamala et al. (2021)** -- *BOLD.* Bias in open-ended language generation benchmark (Table 12).
