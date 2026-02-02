# LongICLBench: Long-context LLMs Struggle with Long In-context Learning

**Authors:** Tianle Li, Ge Zhang, Quy Duc Do, Xiang Yue, Wenhu Chen (University of Waterloo, Carnegie Mellon University, Vector Institute)
**Date:** March 2025, TMLR (arXiv:2404.02060)

---

## Core Research Problem

Long-context LLMs now support windows from 32K to 2M tokens, yet their evaluation has relied on three inadequate metrics: (1) language model perplexity over long documents, (2) synthetic retrieval tasks like passkey retrieval or needle-in-a-haystack (NIAH), on which many models achieve 99%+ accuracy, and (3) long-document question answering or summarization over datasets like Qasper (Dasigi et al., 2021). Perplexity and NIAH provide only a minimum bar. Long-document QA allows models to take shortcuts by reading a short snippet rather than the entire input. Summarization suffers from strong position bias, where LLMs can utilize leading sentences (Nallapati et al., 2017) to achieve high performance.

These metrics are therefore insufficient to measure whether LLMs can genuinely comprehend and reason over the entire input sequence. Existing benchmarks like LongBench (Bai et al., 2023) and L-Eval (An et al., 2023) are limited to moderate lengths and do not require full-input comprehension. **The core challenge is how to evaluate whether long-context LLMs can truly process and reason over long, context-rich sequences rather than relying on local retrieval shortcuts.**

---

## Problem Solutions

The paper proposes using **in-context learning (ICL) on extreme-label classification tasks** as a natural testbed for long-context evaluation. Unlike retrieval-based tasks, extreme-label ICL forces models to scan the entire demonstration to understand the full label space before making predictions.

1. **Extreme-label classification as evaluation.** With 28 to 174 classes, the demonstration sequences naturally grow long (2K--50K tokens), and models cannot predict correctly without comprehending the full label space across the entire input.
2. **Six datasets of graded difficulty.** Tasks span emotion classification (28 classes, short) to discourse marker classification (174 classes, long), creating a difficulty gradient in both label-space complexity and context length.
3. **Position distribution analysis.** Exploratory experiments compare scattered vs. grouped label distributions to reveal position biases in long-context processing.

---

## Approach Details

### Method

LongICLBench consists of six classification datasets where the prompt contains in-context demonstrations covering all class labels. Each **round** provides one example per class, so 1 round of the 174-class Discovery dataset already requires ~10K tokens. Evaluation uses 1 to 5 rounds (1-shot to 5-shot per class), with demonstrations sampled to ensure even label distribution. The model must output the correct label for a held-out test instance.

For each dataset, 500 test examples are sampled from the original test set with balanced label distribution. All open-source models use base (non-instruction-tuned) weights; API-based models use their default configurations.

### Key Technical Components

**Benchmark datasets:**

| Dataset | Task Type | # Classes | Tokens/Shot | Total Tokens |
|---|---|---|---|---|
| GoEmotion | Emotion Classification | 28 | 28 | [1K, 4K] |
| BANKING77 | Intent Classification | 77 | 28 | [2K, 11K] |
| TacRED | Relation Extraction | 41 | 80 | [4K, 18K] |
| Few-NERD | Entity Recognition | 66 | 61 | [5K, 23K] |
| DialogRE | Relation Extraction | 36 | 226 | [8K, 32K] |
| Discovery | Discourse Marker Classification | 174 | 61 | [10K, 50K] |

**Evaluation metrics.** Accuracy for GoEmotion, BANKING77, and Discovery. F1 score for TacRED, Few-NERD, and DialogRE.

**Prompt design.** Each dataset has a task-specific template (Table 9 in paper). Demonstrations are formatted with explicit input-output pairs. The test query follows the demonstrations with the same format.

### Experimental Setup

**Models evaluated (15 total):**

| Model | Size | Strategy | Support |
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

**BANKING77 (77 intents, 2K--14K tokens):**

| Model | 1R (2K) | 2R (4K) | 3R (7K) | 4R (9K) | 5R (14K) |
|---|---|---|---|---|---|
| GPT4-turbo | 73.5 | 80.5 | 82.0 | 83.5 | **84.4** |
| GPT4o | **80.8** | 79.8 | 81.2 | 71.2 | 71.4 |
| Gemini-1.5-Pro | 28.8 | 79.4 | **82.2** | 81.8 | 70.4 |
| LLaMA-2-7B-32K | 30.2 | **70.4** | 72.0 | 75.6 | 77.2 |
| Qwen-1.5-7B | 21.6 | 52.8 | 61.4 | 66.0 | 67.8 |
| Mistral-7B-v0.2 | 29.8 | 43.6 | 66.4 | **67.8** | 64.0 |
| SoTA (RoBERTa + ICDA) | | | | | 94.4 |

- Most open-source models benefit from more demonstrations up to 3 rounds, then plateau or decline.
- GPT4-turbo is the only model that consistently improves across all 5 rounds.

**TacRED (41 relations, 4K--18K tokens):**

| Model | 1R (4K) | 3R (10K) | 5R (18K) |
|---|---|---|---|
| GPT4-turbo | 74.4 | 79.5 | **84.2** |
| Gemini-1.5-Pro | 72.6 | 79.6 | 82.3 |
| Mistral-7B-v0.2 | **53.3** | 51.6 | 42.3 |
| Qwen-1.5-7B | 38.7 | 45.2 | 40.6 |
| SoTA (DeepStruct) | | | 76.8 |

- Open-source models peak at intermediate lengths (7K--14K tokens) and then decline, consistent with the lost-in-the-middle phenomenon.

**Discovery (174 discourse markers, 10K--50K tokens):**

| Model | 1R (10K) | 2R (20K) | 3R (30K) | 5R (50K) |
|---|---|---|---|---|
| Gemini-1.5-Pro | **14.0** | 6.0 | 3.2 | 2.8 |
| GPT4-turbo | 1.5 | 0.5 | 0.5 | 0.5 |
| GPT4o | 2.8 | 0.8 | 0.8 | 0.4 |
| Claude3-Opus | 1.2 | 0.6 | 0.6 | 0.2 |
| All open-source | 0 | 0 | 0 | 0 |
| SoTA (MTL, fine-tuned) | | | | 87.4 |

- On the hardest task, **all LLMs achieve close-to-zero performance** except Gemini-1.5-Pro at 14% (1 round only). A fine-tuned BERT-based model achieves 87.4%, highlighting the massive gap between ICL and fine-tuning on this task.
- Several models (LLaMA-2-7B-32K, ChatGLM3-6B-32K) fail to produce valid output at higher rounds, marked with X in the paper.

**DialogRE (36 relations, 8K--32K tokens):**

| Model | 1R (8K) | 3R (19K) | 5R (32K) |
|---|---|---|---|
| GPT4-turbo | 42.9 | 52.0 | **57.7** |
| GPT4o | 40.6 | 41.0 | 45.3 |
| Gemini-1.5-Pro | 29.6 | 31.2 | 34.3 |
| Mistral-7B-v0.2 | **24.0** | 23.2 | 21.1 |
| Claude3-Opus | 16.8 | 15.3 | 0 |
| SoTA (HiDialog) | | | 77.1 |

- Only GPT4-turbo consistently benefits from more demonstrations. Claude3-Opus collapses completely at 5 rounds (32K tokens).

### Position Distribution Analysis

Inspired by the lost-in-the-middle phenomenon (Liu et al., 2023), the authors analyze how the position distribution of demonstration instances affects performance. Experiments use TacRED with 3 rounds (41 x 3 = 123 instances at ~10K tokens).

**Scattered distribution (random).** Instances of the same label are distributed randomly across the prompt. Some models (InternLM2-7B) achieve ~60% accuracy on only specific label types regardless of position. GPT4-turbo exceeds 80% accuracy on most label types.

**Grouped distribution (same-label instances adjacent).**

| Model | Scattered | Grouped | Delta |
|---|---|---|---|
| Mistral-7B-v0.2 | 51.6 | 5.1 | **-46.5** |
| GPT4-turbo | 79.5 | 59.2 | **-20.3** |
| Gemini-1.5-Pro | 79.6 | 57.3 | **-22.3** |
| Qwen-1.5-7B | 45.2 | 33.0 | -12.2 |
| InternLM2-7B | 15.5 | 4.8 | -9.7 |
| ChatGLM3-6B-32K | 38.9 | 35.6 | -3.3 |

- **Grouping causes universal performance degradation.** Even GPT4-turbo and Gemini-1.5-Pro drop by 20.3% and 22.3%.
- Models like Mistral and InternLM2 show extreme sensitivity, only correctly predicting labels positioned at the end of the prompt in the grouped setting.
- ChatGLM3-6B-32K is most resilient with only a 3.3% drop.

### Architectural Findings

- **Transformer-based models consistently outperform RNN-based alternatives.** RWKV-5-World and Mamba-2.8B achieve near-zero performance on most tasks, despite their theoretical ability to handle unlimited context.
- Among open-source Transformer models, **performance is roughly linear w.r.t. demonstration length** for some models (Qwen, Mistral), suggesting a predictable mathematical relationship between performance and task complexity.

### Limitations

LongICLBench encompasses only one type of evaluation application: extreme-label classification with long in-context learning. Other tasks requiring full-input comprehension (e.g., multi-document reasoning, long-horizon planning) are not covered.

---

## Conclusions

1. **Extreme-label ICL as a long-context evaluation paradigm.** In-context learning on classification tasks with 28--174 classes creates a natural testbed requiring full-input comprehension, complementing existing benchmarks focused on retrieval, QA, or summarization.

2. **Performance degrades with task complexity.** All models show dramatic performance drops as the number of classes and context length increase. On Discovery (174 classes), all models except Gemini-1.5-Pro achieve near-zero accuracy, while fine-tuned BERT reaches 87.4%.

3. **Most LLMs cannot effectively use context beyond 20K tokens.** Open-source models peak at intermediate context lengths (7K--14K tokens). Only GPT4-turbo consistently benefits from additional demonstrations across all context lengths.

4. **Strong position bias in long-context processing.** Grouping same-label demonstrations together causes large performance drops (up to 46.5% for Mistral), with some models only predicting labels from the end of the prompt, consistent with the lost-in-the-middle phenomenon.

5. **Non-Transformer architectures fail on this task.** RWKV and Mamba, despite their theoretical advantage of unlimited context with linear complexity, perform far behind Transformer-based models across all evaluated datasets.

---

## Core References and Why They Are Referenced

### Long-Context Evaluation Benchmarks

- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Cited as a prior long-context benchmark with 21 bilingual datasets averaging ~6K words, which LongICLBench complements by testing full-input comprehension rather than retrieval-based tasks.
- **An et al. (2023)** -- *L-Eval: Instituting Standardized Evaluation for Long Context Language Models.* Cited as supporting 20 sub-tasks with input lengths of 3K--200K tokens, but focused on QA and summarization rather than ICL.
- **Zhang et al. (2024)** -- *InfinityBench: Extending Long Context Evaluation Beyond 100K Tokens.* Referenced as encompassing 12 tasks with an average length of 200K tokens, representing the upper range of existing benchmarks.
- **Tay et al. (2021)** -- *Long Range Arena: A Benchmark for Efficient Transformers.* Cited as an early long-context benchmark with sequences of 1K--16K tokens.

### Position Bias and Context Utilization

- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Directly inspired the exploratory experiments on scattered vs. grouped demonstration distributions. The paper's finding that models favor information at the beginning and end of context is confirmed in the grouped-distribution analysis.

### In-Context Learning Foundations

- **Dong et al. (2023)** -- *A Survey on In-Context Learning.* Provides the theoretical and empirical background on ICL as an inference paradigm.
- **Milios et al. (2023)** -- *In-Context Learning for Text Classification with Many Labels.* Direct predecessor exploring ICL on many-label tasks; LongICLBench extends this to the long-context regime with systematic length and complexity scaling.
- **Anil et al. (2022)** -- *Exploring Length Generalization in Large Language Models.* Referenced for length generalization challenges that motivate the benchmark design.

### Positional Embedding and Context Extension Methods

- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* The position interpolation method used by LLaMA-2-7B-32K, one of the strongest open-source models evaluated.
- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Context extension method; evaluated indirectly through models that use NTK-aware interpolation.
- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* Mamba-2.8B is evaluated as a representative non-Transformer architecture and demonstrates that linear-complexity models fail on tasks requiring full-input comprehension.
- **Peng et al. (2023)** -- *RWKV: Reinventing RNNs for the Transformer Era.* RWKV-5-World is evaluated as the other non-Transformer alternative; similarly fails on most tasks.

### Evaluation Datasets

- **Casanueva et al. (2020)** -- *Efficient Intent Detection with Dual Sentence Encoders (BANKING77).* Source of the 77-intent banking dataset used as a medium-difficulty task.
- **Zhang et al. (2017)** -- *Position-Aware Attention and Supervised Data Improve Slot Filling (TacRED).* Source of the 41-relation extraction dataset used for position distribution analysis.
- **Sileo et al. (2019)** -- *Mining Discourse Markers for Unsupervised Sentence Representation Learning (Discovery).* Source of the 174-class dataset that forms the hardest evaluation task.
- **Demszky et al. (2020)** -- *GoEmotions: A Dataset of Fine-Grained Emotions.* Source of the 28-emotion classification dataset (easiest task).
- **Ding et al. (2021)** -- *Few-NERD: A Few-Shot Named Entity Recognition Dataset.* Source of the 66-entity-type dataset.
- **Yu et al. (2020)** -- *Dialogue-Based Relation Extraction (DialogRE).* Source of the 36-relation dialogue dataset.

#### Cross-References in Available Papers

- **Lost in the Middle (2024-02-lost-in-the-middle):** LongICLBench's position distribution analysis (Section 4) is directly inspired by the lost-in-the-middle phenomenon. The grouped-distribution experiment confirms that models favor labels at the end of the prompt, consistent with Liu et al.'s finding that models struggle with information in the middle of long contexts.
- **LongBench (2024-08-longbench-bilingual-benchmark):** LongICLBench cites LongBench as a prior long-context benchmark, noting that its QA and summarization tasks allow shortcut strategies that do not require full-input comprehension. LongICLBench's extreme-label ICL design addresses this gap.
- **L-Eval (2024-08-l-eval-standardized-evaluation):** Cited alongside LongBench as a benchmark with input lengths up to 200K tokens, but focused on QA and summarization rather than ICL.
- **YaRN (2024-05-yarn-context-extension):** YaRN's NTK-aware interpolation is referenced as a context extension strategy. Qwen-1.5-7B uses NTK-aware interpolation and achieves moderate performance on BANKING77 (67.8% at 5R) but fails on Discovery.
- **PI (2023-06-pi-positional-interpolation):** Position interpolation is the strategy used by LLaMA-2-7B-32K, which is one of the stronger open-source models on BANKING77 (77.2% at 5R) but fails completely on TacRED and Discovery.
- **BABILong (2024-12-babilong-long-context-reasoning):** Both benchmarks address the inadequacy of synthetic evaluations like NIAH. BABILong tests reasoning-in-a-haystack with procedurally generated facts; LongICLBench tests full-input comprehension through extreme-label ICL. They are complementary: BABILong focuses on multi-hop reasoning at scale, while LongICLBench focuses on label-space comprehension.
- **RULER (2024-10-ruler-context-size):** Both extend beyond simple NIAH evaluation. RULER uses synthetic tasks with controlled complexity; LongICLBench uses real classification tasks. LongICLBench's observation that performance degrades beyond 20K tokens aligns with RULER's effective context length findings.
