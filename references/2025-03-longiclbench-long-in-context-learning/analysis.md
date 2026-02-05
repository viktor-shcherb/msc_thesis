---
title: "LongICLBench: Long-context LLMs Struggle with Long In-context Learning"
authors: "Li, Zhang, Do, Yue, Chen"
year: 2025
venue: "TMLR 2025"
paper_type: journal-paper
categories: ["benchmarking", "in-context-learning", "long-context-evaluation", "position-bias"]
scope: ["in-context learning with many demonstrations", "extreme-label classification up to 174 classes", "context lengths 1K to 50K tokens"]
benchmarks_used: ["longicl-bench"]
models_introduced: []
models_evaluated: ["gpt-4", "gemini-1.5-pro", "mistral-7b", "llama-2-7b", "qwen-series"]
key_claims:
  - id: C1
    claim: "All LLMs achieve near-zero performance on Discovery (174 classes, 10K-50K tokens) except Gemini-1.5-Pro at 14% accuracy, while a fine-tuned BERT model achieves 87.4%"
    evidence: "Table 6, Section 3.3"
    status: supported
  - id: C2
    claim: "Most open-source models benefit from more demonstrations up to intermediate context lengths (7K-14K tokens), then performance plateaus or declines"
    evidence: "Tables 3-6, Figure 1, Section 3.3"
    status: supported
  - id: C3
    claim: "Grouping same-label demonstrations together causes universal performance degradation, with drops up to 46.5% for Mistral-7B and 20.3% for GPT4-turbo on TacRED at 10K tokens"
    evidence: "Table 10, Section 4.2, Figure 4"
    status: supported
  - id: C4
    claim: "Transformer-based models consistently outperform non-Transformer alternatives (RWKV-5-World, Mamba-2.8B), which achieve near-zero performance on most tasks despite theoretical unlimited context support"
    evidence: "Tables 3-6, Section 3.3"
    status: supported
  - id: C5
    claim: "Only GPT4-turbo consistently improves with additional demonstrations across all context lengths and datasets evaluated"
    evidence: "Tables 3-5, Figure 1, Section 3.3"
    status: supported
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: extends
    detail: "Position distribution analysis (Section 4) directly inspired by Liu et al.'s lost-in-the-middle finding; confirms position bias extends to ICL with grouped demonstrations causing up to 46.5% accuracy drops"
  - target: 2024-08-longbench-bilingual-benchmark
    type: complementary
    detail: "LongBench evaluates long-context via QA, summarization, and retrieval averaging ~6K words; LongICLBench complements it by requiring full-input comprehension via extreme-label ICL at 2K-50K tokens"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: complementary
    detail: "InfiniteBench tests 100K+ token contexts across 12 tasks; LongICLBench provides a complementary evaluation paradigm requiring full label-space comprehension rather than information retrieval"
  - target: 2024-08-l-eval-standardized-evaluation
    type: complementary
    detail: "L-Eval evaluates long-context via QA and summarization at 3K-200K tokens; LongICLBench differs by requiring models to scan all demonstrations to learn the complete label space"
  - target: 2021-05-long-range-arena
    type: complementary
    detail: "LRA benchmarks efficient Transformers at 1K-16K tokens with synthetic tasks; LongICLBench tests real-world classification at 2K-50K tokens requiring natural language understanding"
  - target: 2022-03-in-context-learning-induction-heads
    type: complementary
    detail: "Olsson et al. identify the mechanistic basis of ICL via induction heads; LongICLBench measures the practical limits of ICL scaling when demonstrations grow to tens of thousands of tokens"
  - target: 2024-08-found-in-the-middle
    type: complementary
    detail: "Both papers identify position bias in long-context processing; Found in the Middle proposes attention calibration for RAG while LongICLBench documents recency bias in ICL through grouped-distribution analysis"
  - target: 2024-03-gemini-1.5-long-context
    type: evaluates
    detail: "LongICLBench evaluates Gemini 1.5 Pro on extreme-label ICL tasks; one of the only models with non-zero performance on the hardest 174-class Discovery task"
  - target: 2024-03-yi-open-foundation-models
    type: evaluates
    detail: "Yi-6B-200K evaluated on extreme-label in-context learning tasks at 2K-50K token context lengths"
open_questions:
  - question: "What causes the performance ceiling in extreme-label ICL — context window limitations, attention degradation, or label-space complexity?"
    addressed_by: null
  - question: "Why do non-Transformer architectures (RWKV, Mamba) fail on long ICL despite unlimited theoretical context, and can architectural modifications close the gap?"
    addressed_by: null
  - question: "Does the recency bias observed in grouped ICL share the same root cause as the lost-in-the-middle phenomenon in retrieval-augmented generation?"
    addressed_by: null
---
# LongICLBench: Long-context LLMs Struggle with Long In-context Learning

**Authors:** Tianle Li, Ge Zhang, Quy Duc Do, Xiang Yue, Wenhu Chen (University of Waterloo, Carnegie Mellon University, Vector Institute)
**Date:** March 2025, TMLR (arXiv:2404.02060)

---

## Core Research Problem

Long-context LLMs now support windows from 32K to 2M tokens, yet their evaluation has relied on three inadequate paradigms: (1) language model perplexity over long documents, used by most papers; (2) synthetic retrieval tasks like passkey retrieval (Mohtashami & Jaggi, 2023) or needle-in-a-haystack (Team et al., 2023; Fu et al., 2024), on which several LLMs achieve 99%+ accuracy; and (3) long-document question answering or summarization over datasets like Qasper (Dasigi et al., 2021). Perplexity and passkey retrieval provide only a minimum bar. Long-document QA allows models to take shortcuts by reading a short snippet rather than the entire input. Summarization suffers from strong position bias, where LLMs can utilize leading sentences (Nallapati et al., 2017) to achieve high performance.

These metrics are therefore insufficient to measure whether LLMs can genuinely comprehend and reason over the entire input sequence. Existing benchmarks like LongBench (Bai et al., 2023b) with an average of ~6K words, L-Eval (An et al., 2023) with 3K--200K token inputs, and InfiniteBench (Zhang et al., 2024) with an average of 200K tokens focus on retrieval, QA, and summarization, none of which strictly require processing the full input. **The core challenge is how to evaluate whether long-context LLMs can truly comprehend and reason over long, context-rich sequences rather than relying on local retrieval shortcuts.**

---

## Problem Solutions

The paper proposes using **in-context learning (ICL) on extreme-label classification tasks** as a natural testbed for long-context evaluation. Unlike retrieval-based tasks, extreme-label ICL forces models to scan the entire demonstration to understand the full label space before making predictions.

1. **Extreme-label classification as evaluation.** With 28 to 174 classes, the demonstration sequences naturally grow long (1K--50K tokens), and models cannot predict correctly without comprehending the full label space across the entire input.
2. **Six datasets of graded difficulty.** Tasks span emotion classification (28 classes, short) to discourse marker classification (174 classes, long), creating a difficulty gradient in both label-space complexity and context length.
3. **Position distribution analysis.** Exploratory experiments compare scattered vs. grouped label distributions to reveal position biases in long-context ICL processing.

---

## Approach Details

### Method

LongICLBench consists of six classification datasets where the prompt contains in-context demonstrations covering all class labels. Each **round** provides one example per class, so 1 round of the 174-class Discovery dataset already requires ~10K tokens. Evaluation uses 1 to 5 rounds (1-shot to 5-shot per class), with demonstrations sampled to ensure even label distribution. The model must output the correct label for a held-out test instance.

For each dataset, 500 test examples are sampled from the original test set with balanced label distribution. All open-source models use base (non-instruction-tuned) weights; API-based models use their default configurations.

### Key Technical Components

**Benchmark datasets (Table 1):**

| Dataset | Task Type | # Classes | Tokens/Shot | Total Tokens |
|---|---|---|---|---|
| GoEmotion | Emotion Classification | 28 | 28 | [1K, 4K] |
| BANKING77 | Intent Classification | 77 | 28 | [2K, 11K] |
| TacRED | Relation Extraction | 41 | 80 | [4K, 18K] |
| Few-NERD | Entity Recognition | 66 | 61 | [5K, 23K] |
| DialogRE | Relation Extraction | 36 | 226 | [8K, 32K] |
| Discovery | Discourse Marker Classification | 174 | 61 | [10K, 50K] |

**Evaluation metrics.** Accuracy for GoEmotion, BANKING77, and Discovery. F1 score for TacRED, Few-NERD, and DialogRE.

**Prompt design.** Each dataset has a task-specific template (Table 9 in paper). Demonstrations are formatted with explicit input-output pairs. The test query follows the demonstrations in the same format.

### Experimental Setup

**Models evaluated (15 total, Table 2):**

| Model | Size | Strategy | Context Support |
|---|---|---|---|
| Gemma-7B-base | 7B | RoPE + LF | 8K |
| LLaMA-2-7B-32K | 7B | Position Interpolation | 32K |
| ChatGLM3-6B-32K | 6B | Position Encoding Scheme | 32K |
| Qwen-1.5-7B-base | 7B | NTK-Aware Interpolation | 32K |
| Mistral-7B-v0.2-base | 7B | Long-context fine-tuning | 32K |
| LLaMA-2-7B-LongLora | 7B | Shifted Short Attention | 100K |
| Yi-6B-200K | 6B | Position Interpolation + LF | 200K |
| InternLM2-7B-base | 7B | Dynamic NTK | 200K |
| Long-LLaMA-code-7B | 7B | Focused Transformer | 256K |
| RWKV-5-World | 3B | Attention-free (RNN-like) | Unlimited |
| Mamba-2.8B | 2.8B | State Space Model | Unlimited |
| GPT4-turbo | -- | -- | 128K |
| GPT4o | -- | -- | 128K |
| Claude3-Opus | -- | -- | 200K |
| Gemini-1.5-Pro | -- | -- | 10M |

**Hardware.** Open-source models inferred on eight NVIDIA RTX A6000 GPUs.

### Key Results

**BANKING77 (Table 3, 77 intents, Accuracy):**

| Model | 1R (2K) | 2R (4K) | 3R (7K) | 4R (9K) | 5R (14K) |
|---|---|---|---|---|---|
| GPT4-turbo | 73.5 | 80.5 | 82.0 | 83.5 | **84.4** |
| GPT4o | **80.8** | 79.8 | 81.2 | 71.2 | 71.4 |
| Gemini-1.5-Pro | 28.8 | 79.4 | **82.2** | 81.8 | 70.4 |
| Claude3-Opus | 60.0 | 62.6 | 62.2 | 43.8 | 26.0 |
| LLaMA-2-7B-32K | 30.2 | **70.4** | 72.0 | 75.6 | 77.2 |
| Qwen-1.5-7B | 21.6 | 52.8 | 61.4 | 66.0 | 67.8 |
| Mistral-7B-v0.2 | 29.8 | 43.6 | 66.4 | **67.8** | 64.0 |
| Long-LLaMA-code-7B | 3.0 | 19.4 | 28.0 | 31.6 | 32.6 |
| SoTA (RoBERTa + ICDA) | | | | | 94.4 |

- Most open-source models benefit from more demonstrations up to 3 rounds, then plateau or decline.
- GPT4-turbo is the only model that consistently improves across all 5 rounds.
- Claude3-Opus degrades sharply after 3 rounds (62.2 at 3R to 26.0 at 5R).
- From 1R to 2R (2K to 4K tokens), most open-source models show large jumps (e.g., LLaMA-2-7B-32K: 30.2 → 70.4).

**TacRED (Table 4, 41 relations, F1):**

| Model | 1R (4K) | 2R (7K) | 3R (10K) | 4R (14K) | 5R (18K) |
|---|---|---|---|---|---|
| GPT4-turbo | 74.4 | 76.5 | 79.5 | 80.4 | **84.2** |
| Gemini-1.5-Pro | 72.6 | **81.4** | 79.6 | 81.4 | 82.3 |
| Claude3-Opus | 68.7 | 74.1 | 35.4 | 43.4 | 44.3 |
| Mistral-7B-v0.2 | **53.3** | 53.1 | 51.6 | 48.0 | 42.3 |
| Qwen-1.5-7B | 38.7 | 47.3 | 45.2 | 43.6 | 40.6 |
| ChatGLM3-6B-32K | 29.7 | 36.1 | 38.9 | 40.1 | 25.2 |
| SoTA (DeepStruct) | | | | | 76.8 |

- Open-source models peak at early rounds and decline, consistent with practical context-length limits.
- GPT4-turbo and Gemini-1.5-Pro surpass the fine-tuned SoTA (DeepStruct: 76.8 F1) using ICL alone.
- Claude3-Opus collapses at 3R (10K tokens), dropping from 74.1 to 35.4 F1.

**Few-NERD (Table 8, 66 entity types, F1):**

| Model | 1R (5K) | 2R (9K) | 3R (14K) | 4R (19K) | 5R (24K) |
|---|---|---|---|---|---|
| GPT4-turbo | 53.4 | **55.3** | **56.2** | 55.6 | **56.8** |
| Gemini-1.5-Pro | **55.4** | 47.8 | 49.5 | 41.4 | 42.4 |
| Claude3-Opus | 53.5 | 51.3 | 51.2 | 52.4 | 52.5 |
| Mistral-7B-v0.2 | 42.2 | 47.4 | 48.9 | **50.0** | 50.0 |
| InternLM2-7B | 43.6 | 46.2 | 46.5 | 47.8 | 48.3 |
| Qwen-1.5-7B | 40.0 | 46.4 | 47.6 | 47.3 | 47.8 |
| SoTA (PL-Marker) | | | | | 70.9 |

- Open-source models show steady improvement with more rounds (Mistral: 42.2 → 50.0).
- Gemini-1.5-Pro starts strongest at 1R (55.4) but declines with more context.

**DialogRE (Table 5, 36 relations, F1):**

| Model | 1R (8K) | 2R (13K) | 3R (19K) | 4R (25K) | 5R (32K) |
|---|---|---|---|---|---|
| GPT4-turbo | 42.9 | 47.8 | 52.0 | 55.9 | **57.7** |
| GPT4o | 40.6 | 41.5 | 41.0 | 47.3 | 45.3 |
| Gemini-1.5-Pro | 29.6 | 37.8 | 31.2 | 32.4 | 34.3 |
| Mistral-7B-v0.2 | **24.0** | 23.0 | 23.2 | 22.0 | 21.1 |
| Claude3-Opus | 16.8 | 30.3 | 15.3 | 0.8 | 0 |
| SoTA (HiDialog) | | | | | 77.1 |

- Only GPT4-turbo consistently benefits from more demonstrations.
- Claude3-Opus collapses completely at 4R and 5R (0.8 and 0 F1 at 25K and 32K tokens).
- All models remain far below the fine-tuned SoTA (77.1 F1).

**Discovery (Table 6, 174 discourse markers, Accuracy):**

| Model | 1R (10K) | 2R (20K) | 3R (30K) | 4R (40K) | 5R (50K) |
|---|---|---|---|---|---|
| Gemini-1.5-Pro | **14.0** | 6.0 | 3.2 | 1.8 | 2.8 |
| GPT4o | 2.8 | 0.8 | 0.8 | 0.6 | 0.4 |
| GPT4-turbo | 1.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| Claude3-Opus | 1.2 | 0.6 | 0.6 | 0.6 | 0.2 |
| All open-source | 0 | 0 | 0 | 0 | 0 |
| SoTA (MTL, fine-tuned) | | | | | 87.4 |

- On the hardest task, **all LLMs achieve near-zero performance** except Gemini-1.5-Pro at 14% (1R only), which itself declines to 2.8% by 5R.
- A fine-tuned BERT-based model achieves 87.4%, highlighting the massive gap between ICL and fine-tuning on tasks with very large label spaces.
- Several models (LLaMA-2-7B-32K, ChatGLM3-6B-32K) fail to produce valid output at higher rounds, marked with X in the paper (Table 6).

**GoEmotion (Table 7, 28 emotions, Accuracy):**

| Model | 1R (0.8K) | 3R (2.4K) | 5R (4K) |
|---|---|---|---|
| GPT4-turbo | **36.5** | 35.0 | 32.0 |
| Claude3-Opus | 25.8 | 17.0 | 19.6 |
| GPT4o | 23.0 | 21.2 | 22.2 |
| ChatGLM3-6B-32K | 22.0 | 15.0 | 10.6 |
| Qwen-1.5-7B | 14.8 | **18.6** | **14.2** |
| SoTA (BERT) | | | 58.9 |

- Even on the easiest task (28 classes, up to 4K tokens), the best ICL performance (GPT4-turbo: 36.5%) falls well below the fine-tuned SoTA (58.9%).
- Performance generally declines or fluctuates with more rounds for most models.

### Position Distribution Analysis

Inspired by the lost-in-the-middle phenomenon (Liu et al., 2023), the authors analyze how the position distribution of demonstration instances affects ICL performance. Experiments use TacRED with 3 rounds (41 x 3 = 123 instances at ~10K tokens).

**Scattered distribution (random).** Instances of the same label are distributed randomly across the prompt. Some models (InternLM2-7B) achieve ~60% accuracy only on specific label types (per:religion, per:age, per:date_of_birth) regardless of instance placement, while GPT4-turbo exceeds 80% accuracy on the majority of label types (Figure 4, Section 4.1).

**Grouped distribution (same-label instances adjacent, Table 10):**

| Model | Scattered | Grouped | Delta |
|---|---|---|---|
| Mistral-7B-v0.2 | 51.6 | 5.1 | **-46.5** |
| GPT4-turbo | 79.5 | 59.2 | **-20.3** |
| Gemini-1.5-Pro | 79.6 | 57.3 | **-22.3** |
| Qwen-1.5-7B | 45.2 | 33.0 | -12.2 |
| InternLM2-7B | 15.5 | 4.8 | -9.7 |
| Yi-6B-200K | 8.0 | 0 | -8.0 |
| ChatGLM3-6B-32K | 38.9 | 35.6 | -3.3 |

- **Grouping causes universal performance degradation.** Even GPT4-turbo and Gemini-1.5-Pro drop by 20.3 and 22.3 percentage points respectively.
- Models like Mistral and InternLM2 show extreme sensitivity, correctly predicting only labels positioned at the end of the prompt in the grouped setting, indicating strong **recency bias** (Figure 4, Section 4.2).
- ChatGLM3-6B-32K is the most resilient open-source model with only a 3.3 percentage point drop.

### Architectural Findings

- **Transformer-based models consistently outperform RNN-based alternatives.** RWKV-5-World (3B) and Mamba-2.8B achieve near-zero performance on most tasks across all context lengths, despite their theoretical ability to handle unlimited context with linear time/memory complexity (Tables 3--6, Section 3.3).
- Among open-source Transformer models, **performance of some models (Qwen, Mistral) is roughly linear w.r.t. demonstration length** on easier tasks, suggesting a predictable relationship between performance and task complexity for ICL (Figure 3, Section 3.3).

---

## Limitations and Failure Modes

1. **Single evaluation paradigm.** LongICLBench encompasses only one type of evaluation: extreme-label classification with long in-context learning. Other tasks requiring full-input comprehension (e.g., multi-document reasoning, long-horizon planning) are not covered (Appendix A.6).

2. **Base models only for open-source.** All open-source models are evaluated using base (pre-instruction-tuning) weights (Section 3.2). Instruction-tuned versions may perform differently on classification tasks.

3. **Limited model sizes.** Open-source models are restricted to ~7B parameters (Section 3.2). Larger open-source models may exhibit different scaling behavior.

4. **No analysis of failure modes.** The paper documents near-zero performance on Discovery but does not analyze why models fail (e.g., whether they output invalid labels, random labels, or systematically biased predictions).

5. **Confounded difficulty dimensions.** Task difficulty increases simultaneously along label-space size, context length, and label granularity, making it impossible to isolate which factor drives performance degradation. [Inference: not stated explicitly.]

---

## Conclusions

### Contributions

1. **Extreme-label ICL as a long-context evaluation paradigm.** In-context learning on classification tasks with 28--174 classes creates a natural testbed requiring full-input comprehension, complementing existing benchmarks focused on retrieval, QA, or summarization (Section 1, Tables 1--6).

2. **Systematic difficulty gradient.** Six datasets spanning 1K to 50K tokens and 28 to 174 classes reveal where each model's comprehension breaks down, from relatively easy (BANKING77, most models >60%) to extremely hard (Discovery, all models near zero) (Figure 3, Section 3.3).

3. **Practical ICL context limits.** Open-source models typically peak at intermediate context lengths (7K--14K tokens) and then plateau or decline. Only GPT4-turbo consistently benefits from additional demonstrations across all datasets and context lengths (Tables 3--5, Section 3.3).

4. **Position bias in long ICL.** Grouping same-label demonstrations together causes large performance drops across all models (up to 46.5% for Mistral), with some models only predicting labels from the end of the prompt, consistent with the lost-in-the-middle phenomenon (Table 10, Figure 4, Section 4.2).

5. **Non-Transformer architectures fail on long ICL.** RWKV and Mamba, despite their theoretical advantage of unlimited context with linear complexity, perform far behind Transformer-based models across all evaluated datasets (Tables 3--6, Section 3.3).

### Implications

1. **ICL is not a substitute for fine-tuning on complex tasks.** The gap between ICL and fine-tuned SoTA widens dramatically with task complexity (87.4% vs. near-zero on Discovery), suggesting that current ICL mechanisms are insufficient for tasks with very large label spaces. [Speculative: this gap may narrow with future models.]

2. **Claimed context lengths may overstate practical capability.** Models supporting 100K--200K tokens in theory (Yi-6B-200K, InternLM2-7B, Long-LLaMA-code-7B) show no advantage over 32K-context models on these tasks, indicating that raw context window size does not determine comprehension ability.

3. **Attention architecture matters for comprehension.** The failure of linear-complexity alternatives (RWKV, Mamba) suggests that full quadratic attention may be necessary for tasks requiring global context comprehension, not just local pattern matching.

---

## Key Claims

1. **C1: Near-zero performance on the hardest task.** All LLMs achieve near-zero accuracy on Discovery (174 classes) except Gemini-1.5-Pro at 14% (1R), while a fine-tuned BERT model achieves 87.4% (Table 6, Section 3.3). Status: **supported**.

2. **C2: Intermediate context length optimum.** Most open-source models benefit from more demonstrations up to intermediate lengths (7K--14K tokens), then plateau or decline. After 3 rounds on BANKING77, limited performance gain is achieved by adding more examples (Tables 3--6, Figure 1, Section 3.3). Status: **supported**.

3. **C3: Grouping degrades performance universally.** Placing same-label demonstrations adjacent causes drops of 46.5% (Mistral), 22.3% (Gemini-1.5-Pro), and 20.3% (GPT4-turbo) on TacRED 3R (~10K tokens). Some models only predict labels from the end of the prompt in the grouped setting (Table 10, Figure 4, Section 4.2). Status: **supported**.

4. **C4: Transformer superiority over non-Transformer architectures.** RWKV-5-World and Mamba-2.8B achieve near-zero performance on most tasks, despite unlimited theoretical context support. Transformer-based models consistently outperform them across all datasets (Tables 3--6, Section 3.3). Status: **supported**.

5. **C5: GPT4-turbo uniquely robust.** GPT4-turbo is the only model that consistently improves with additional demonstrations across all context lengths on BANKING77, TacRED, and DialogRE. Other API-based models (GPT4o, Claude3-Opus, Gemini-1.5-Pro) show declining or fluctuating performance at longer lengths (Tables 3--5, Section 3.3). Status: **supported**.

---

## Open Questions

1. **What causes the performance ceiling in extreme-label ICL?** Is it context window limitations, attention degradation over long sequences, or the inherent difficulty of large label spaces? The paper documents the phenomenon but does not isolate the cause (Section 5). Not yet addressed.

2. **Why do non-Transformer architectures fail on long ICL?** RWKV and Mamba have linear-time complexity and unlimited theoretical context but achieve near-zero on most tasks. Whether this reflects architectural limitations in global reasoning or insufficient training data/methodology is unclear (Tables 3--6). Not yet addressed.

3. **Does the recency bias in grouped ICL share the same root cause as lost-in-the-middle?** The grouped-distribution experiments show models favor end-of-prompt labels, paralleling the U-shaped attention bias found by Liu et al. (2023), but the causal mechanism may differ between ICL and retrieval settings (Section 4.2). Not yet addressed.

---

## Core References and Why They Are Referenced

### Long-Context Evaluation Benchmarks

- **Bai et al. (2023b)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Cited as a prior long-context benchmark comprising 21 bilingual datasets averaging ~6K words, which LongICLBench complements by testing full-input comprehension rather than retrieval-based tasks.
- **An et al. (2023)** -- *L-Eval: Instituting Standardized Evaluation for Long Context Language Models.* Cited as supporting 20 sub-tasks with input lengths of 3K--200K tokens, but focused on QA and summarization rather than ICL.
- **Zhang et al. (2024)** -- *InfiniteBench: Extending Long Context Evaluation Beyond 100K Tokens.* Referenced as encompassing 12 tasks with an average length of 200K tokens, representing the upper range of existing benchmarks.
- **Tay et al. (2021)** -- *Long Range Arena: A Benchmark for Efficient Transformers.* Cited as an early long-context benchmark with sequences of 1K--16K tokens for evaluating efficient Transformer variants.

### Position Bias and Context Utilization

- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Directly inspired the exploratory experiments on scattered vs. grouped demonstration distributions (Section 4). The paper's finding that models favor information at the beginning and end of context is confirmed in the grouped-distribution analysis.

### In-Context Learning Foundations

- **Dong et al. (2023)** -- *A Survey on In-Context Learning.* Provides the theoretical and empirical background on ICL as an inference paradigm.
- **Milios et al. (2023)** -- *In-Context Learning for Text Classification with Many Labels.* Direct predecessor exploring ICL on many-label tasks; LongICLBench extends this to the long-context regime with systematic length and complexity scaling.
- **Anil et al. (2022)** -- *Exploring Length Generalization in Large Language Models.* Referenced for length generalization challenges that motivate the benchmark design.
- **Liu et al. (2022)** -- *What Makes Good In-Context Examples for GPT-3?* Establishes that increasing the number of ICL demonstrations can enhance performance, which LongICLBench tests at extreme scale.

### Positional Embedding and Context Extension Methods

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE is the positional encoding foundation for most Transformer-based models evaluated in the benchmark.
- **Press et al. (2022)** -- *Train Short, Test Long: ALiBi.* ALiBi is referenced as one of the approaches for extending context windows via relative position encodings.
- **Chen et al. (2023a)** -- *Extending Context Window via Positional Interpolation.* The position interpolation method used by LLaMA-2-7B-32K, one of the strongest open-source models evaluated.
- **Peng et al. (2023b)** -- *YaRN: Efficient Context Window Extension.* NTK-aware interpolation from this lineage is used by Qwen-1.5-7B-base.

### Non-Transformer Architectures

- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* Mamba-2.8B is evaluated as a representative state space model and achieves near-zero performance across all tasks, demonstrating that linear-complexity architectures fail on tasks requiring global context comprehension.
- **Peng et al. (2023a)** -- *RWKV: Reinventing RNNs for the Transformer Era.* RWKV-5-World is evaluated as the RNN-based alternative; similarly fails on most tasks despite unlimited theoretical context.

### Evaluation Datasets

- **Casanueva et al. (2020)** -- *Efficient Intent Detection with Dual Sentence Encoders (BANKING77).* Source of the 77-intent banking dataset used as a medium-difficulty task.
- **Zhang et al. (2017)** -- *Position-Aware Attention and Supervised Data Improve Slot Filling (TacRED).* Source of the 41-relation extraction dataset used for position distribution analysis.
- **Sileo et al. (2019)** -- *Mining Discourse Markers for Unsupervised Sentence Representation Learning (Discovery).* Source of the 174-class dataset that forms the hardest evaluation task.
- **Demszky et al. (2020)** -- *GoEmotions: A Dataset of Fine-Grained Emotions.* Source of the 28-emotion classification dataset (easiest task).
- **Ding et al. (2021)** -- *Few-NERD: A Few-Shot Named Entity Recognition Dataset.* Source of the 66-entity-type dataset.
- **Yu et al. (2020)** -- *Dialogue-Based Relation Extraction (DialogRE).* Source of the 36-relation dialogue dataset.
