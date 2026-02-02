# BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack

**Authors:** Yuri Kuratov, Aydar Bulatov, Petr Anokhin, Ivan Rodkin, Dmitry Sorokin, Artyom Sorokin, Mikhail Burtsev (AIRI, MIPT, London Institute for Mathematical Sciences)
**Date:** December 2024, NeurIPS 2024 Datasets and Benchmarks Track (arXiv:2406.10149)

---

## Core Research Problem

Existing long-context benchmarks fail to keep pace with the rapidly growing context windows of LLMs. Benchmarks such as LongBench (Bai et al., 2023) and L-Eval (An et al., 2023) scale only to 40K tokens, while models claim to support hundreds of thousands to millions of tokens. The dominant synthetic evaluation -- the vanilla needle-in-a-haystack (NIAH) test -- is overly simplistic: most modern models achieve near-perfect performance on it, producing fully green heatmaps that do not differentiate between models.

More critically, the vanilla NIAH test evaluates only single-fact retrieval. It does not test whether models can reason over multiple facts scattered across a long context. Meanwhile, realistic benchmarks (ZeroSCROLLS, LongBench, InfinityBench) lack controllable sequence length and confound long-context utilization with parametric knowledge.

**The core challenge is how to build a scalable, controllable benchmark that tests genuine reasoning -- not just retrieval -- across arbitrarily long contexts.**

---

## Problem Solutions

BABILong extends the bAbI benchmark (Weston et al., 2016) -- 20 reasoning tasks designed as prerequisites for conversational AI -- by embedding task facts within long natural text from the PG19 corpus (Rae et al., 2020).

1. **Reasoning-in-a-haystack design.** Task-relevant facts (e.g., "Mary moved to the office") are interspersed between sentences drawn from PG19 books, creating a signal-in-noise problem that scales to arbitrary length.
2. **20 diverse reasoning tasks.** The tasks cover single-fact retrieval (QA1), multi-fact chaining (QA2, QA3), spatial reasoning (QA4), three-argument relations (QA5), yes/no questions, counting, lists/sets, negation, indefinite knowledge, and more.
3. **Scalable generation.** Because both the facts and the background text are generated or drawn from large corpora, BABILong can produce evaluation samples at any desired length, with predefined splits from 0K to 10M tokens.

---

## Approach Details

### Method

BABILong constructs evaluation samples by interleaving sentences from a bAbI task instance with sentences from PG19 books in their natural order. Background sentences are added until the sample reaches the target token length. The question appears at the end of the input. The model must (1) distinguish task-relevant facts from background text, (2) identify the subset of facts relevant to the question (supporting facts), and (3) perform the required reasoning to produce the answer.

The 20 tasks are labeled QA1--QA20. They differ in the number of total facts (2--320), the number of relevant facts per question (1--10), and the type of reasoning required:

| Task | Name | Facts per Task | Relevant Facts | Reasoning Type |
|---|---|---|---|---|
| QA1 | Single supporting fact | 2--10 | 1 | Retrieval |
| QA2 | Two supporting facts | 2--68 | 2 | Two-hop chaining |
| QA3 | Three supporting facts | 4--320 | 3 | Three-hop chaining |
| QA4 | Two arg relations | 2 | 1 | Spatial reasoning |
| QA5 | Three arg relations | 2--126 | 1 | Argument tracking |
| QA6 | Yes/no questions | 2--26 | 1 | Boolean reasoning |
| QA7 | Counting | 2--52 | 1--10 | Aggregation |
| QA8 | Lists/sets | 2--50 | 1--8 | Set operations |
| QA9 | Simple negation | 2--10 | 1 | Negation |
| QA10 | Indefinite knowledge | 2--10 | 1 | Uncertainty |

### Key Technical Components

**Background text selection.** PG19 was chosen because its narrative style (people, locations, actions) is distributionally similar to bAbI facts, making the filtering task non-trivial. The similarity between task facts and background text is a deliberate design choice: it prevents models from relying on superficial distributional cues.

**Evaluation metric.** Accuracy is measured by exact match of the generated answer. Performance is considered satisfactory at >85% and a complete failure at <30%.

**Few-shot prompting.** Each evaluation prompt begins with a task description and 2--3 in-context examples inside `<example>` tags, followed by the long context inside `<context>` tags, and a duplicated question after the context.

**Data contamination resistance.** Because bAbI facts are procedurally generated, BABILong is immune to data leakage from LLM training corpora.

### Experimental Setup

**Models evaluated (34+):**
- **8K context:** LLaMA-2-7B-32K, LongChat-7b-v1.5-32k, LongAlpaca-13B
- **32K--64K:** Mistral-7B-Instruct-v0.2, Mixtral-8x7B, Mixtral-8x22B
- **128K:** ChatGLM3-6b, LLama-3.1-8B/70B, Phi-3/3.5, Command-R, Qwen-2.5-7B/72B, Jamba-v1, GPT-4o-mini
- **200K:** Yi-9B/34B-200K
- **Closed-source:** GPT-4 (gpt-4-0125-preview), Gemini 1.5 Pro 002
- **Long-context adaptations:** YaRN-Mistral, Activation Beacon (LLama-2, Mistral)
- **Alternative architectures:** Mamba-2.8B, RWKV-v5/v6, RecurrentGemma-9B
- **Fine-tuned small models:** RMT (137M), ARMT (137M), Mamba (130M)
- **RAG pipelines:** GPT-4 + RAG-C/RAG-S, Llama3-ChatQA-1.5-8B + RAG-S

**Evaluation:** 1000 samples per task per length for lengths up to 32K; 100 samples per task per length for longer sequences. Predefined splits at 0K, 1K, 2K, 4K, 8K, 16K, 32K, 64K, 128K, 512K, 1M, and 10M tokens.

**Fine-tuning:** RMT and ARMT use GPT-2 (137M) backbone with 512-token segments and 16/10 memory tokens. Curriculum training from 1 to 32 segments (up to 16K tokens). Mamba-130M uses the same curriculum. AdamW optimizer, batch size 64, learning rate 3e-5 to 1e-4.

### Key Results

**Effective context utilization (QA1--QA3):**

| Model | QA1 Effective Range | QA2 (0K) | QA3 (0K) |
|---|---|---|---|
| Gemini 1.5 Pro 002 | ~64K | 89% | 79% |
| GPT-4 | ~16K | 88% | 56% |
| Qwen2.5-72B-Instruct | ~64K | 83% | 68% |
| LLama-3.1-70B-Instruct | ~16K | 82% | 43% |
| LLama-3.1-8B-Instruct | ~8K | 70% | 43% |
| Phi-3-medium-128k | ~32K | 76% | 55% |

- **LLMs effectively utilize only 10--20% of their claimed context.** On QA1, most models maintain >85% accuracy only up to 4K tokens. GPT-4 and LLama-3.1-70B extend to 16K; Qwen-2.5-72B and Gemini 1.5 Pro to 64K.
- **Multi-fact reasoning degrades sharply.** On QA2, only GPT-4 and Gemini 1.5 Pro solve the task without background text. On QA3, no LLM exceeds 80% even at 0K.
- **Context extension methods largely fail.** YaRN does not extend to longer contexts despite stable perplexity. LongChat, LongAlpaca, and LLama-2-7B-32K fail even at their trained length of 32K. Activation Beacon improves over YaRN but still achieves <40% at 32K.

**RAG results:**

| Method | QA1 4K | QA1 128K | QA2 128K | QA3 128K |
|---|---|---|---|---|
| GPT-4 + RAG-C top-5 | 70% | 16% | -- | -- |
| GPT-4 + RAG-S top-5 | 62% | 56% | 32% | 16% |
| GPT-4 + RAG-S top-20 | 58% | 51% | -- | -- |
| Llama3 + RAG-S | -- | 64% | -- | -- |

- **RAG fails on multi-fact tasks.** Sentence-level retrieval (RAG-S) outperforms chunk retrieval (RAG-C), but accuracy on QA2 and QA3 drops below random guessing. The retrieval system cannot recover all supporting facts because not all relevant facts are semantically similar to the question.

**Fine-tuned models:**

| Model | QA1 128K | QA1 1M | QA1 10M | QA1 50M |
|---|---|---|---|---|
| Mamba (130M) fine-tune | 100% | 84% | 66% | -- |
| RMT (137M) fine-tune | 94% | 55% | 66% | -- |
| ARMT (137M) fine-tune | 100% | 99% | 89% | 77% |

- **Fine-tuned small models outperform LLMs.** RMT and ARMT with GPT-2 backbone (137M parameters) significantly outperform GPT-4 despite being ~1000x smaller. ARMT processes up to 50 million tokens -- a record for single-model sequence processing.
- **Mamba excels at medium lengths but is impractical beyond 128K** due to extremely slow inference.
- **Recurrent memory models generalize far beyond training length.** Trained on up to 16K tokens (32 segments), RMT maintains performance to 128K and beyond -- over 600x the training length.

### Comparison with RULER and MMLU

BABILong's correlation with MMLU is high at short contexts (R^2 = 0.888 at 0K on QA2) and decreases as length grows. RULER maintains near-constant correlation with MMLU regardless of length (R^2 = 0.928 at <=128K). This indicates that **BABILong captures differences in long-context behavior starting from 2K tokens**, while RULER requires 128K+ tokens to differentiate models from MMLU.

### Limitations

1. **Limited background text sources.** Only PG19 and Wikipedia were tested as background text; other sources may affect difficulty.
2. **Unoptimized RAG.** The retrieval component was not optimized; better RAG pipelines might improve performance.
3. **Limited vocabulary in facts.** bAbI uses small vocabularies for names and objects, making the task easier for fine-tuned models that can learn to detect fact-specific tokens. Distractor facts partially mitigate this.
4. **No position control analysis in the main evaluation.** Unlike lost-in-the-middle style analysis, the main results do not condition on fact position within the context (though Appendix K provides a GPT-4 depth analysis).

---

## Conclusions

1. **Scalable reasoning-in-a-haystack benchmark.** BABILong provides 20 diverse reasoning tasks that can be generated at any length (predefined splits up to 10M tokens), going far beyond the single-fact retrieval of vanilla NIAH.

2. **LLMs use only 10--20% of their context.** Even for the simplest single-fact task, most models maintain satisfactory performance (>85%) only up to 4K tokens. Multi-fact reasoning degrades even at 0K for most models.

3. **RAG fails on multi-hop tasks.** Standard retrieval pipelines achieve ~60% on single-fact QA but collapse on two- and three-fact tasks because the retrieval system cannot recover all supporting facts or maintain their temporal ordering.

4. **Fine-tuned recurrent models achieve record sequence lengths.** ARMT with a 137M-parameter backbone processes up to 50 million tokens with meaningful accuracy, outperforming LLMs 1000x its size and generalizing over 600x beyond its training length.

5. **BABILong differentiates models at shorter lengths than RULER.** BABILong's correlation with MMLU drops from 2K tokens onward, indicating it captures long-context-specific behavior earlier than RULER, which requires 128K+ tokens for differentiation.

6. **Benchmark is contamination-proof.** Because facts are procedurally generated, BABILong is immune to data leakage from LLM pretraining corpora.

---

## Core References and Why They Are Referenced

### Benchmark Foundations

- **Weston et al. (2016)** -- *Towards AI-Complete Question Answering: A Set of Prerequisite Toy Tasks (bAbI).* The source of the 20 reasoning tasks that BABILong extends to long contexts. BABILong inherits bAbI's task design, fact structure, and vocabulary.
- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling (PG19).* Provides the background text corpus (books published before 1919) used as the "haystack" in BABILong.
- **Kamradt (2023)** -- *Needle In A Haystack (LLMTest).* The vanilla NIAH test that BABILong addresses as overly simplistic. BABILong replaces single-fact retrieval with multi-fact reasoning.

### Long-Context Evaluation Benchmarks

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* The closest comparable benchmark. BABILong and RULER share the NIAH extension concept, but RULER uses more synthetic haystacks (repeated noise sentences) and does not test multi-hop reasoning as deeply. BABILong shows lower correlation with MMLU at long contexts than RULER, indicating it captures different long-context behaviors.
- **Bai et al. (2023)** -- *LongBench.* A bilingual long-context benchmark limited to 40K tokens. BABILong contrasts with LongBench's lack of controllable length and reliance on parametric knowledge.
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* A zero-shot long-context benchmark that BABILong compares against as lacking controllable context length.
- **Zhang et al. (2024b)** -- *InfinityBench.* Extends long-context evaluation beyond 100K tokens. BABILong goes further with splits up to 10M tokens and evaluations to 50M.
- **Song et al. (2024b)** -- *Counting-Stars.* Another scalable NIAH-style benchmark that introduces aggregation tasks. BABILong provides more diverse reasoning categories (20 tasks vs. Counting-Stars' single task type).

### Models and Architectures

- **Reid et al. (2024)** -- *Gemini 1.5.* The top-performing commercial model on BABILong, maintaining strong performance up to 64K tokens.
- **Dubey et al. (2024)** -- *The Llama 3 Herd of Models.* LLama-3.1-70B outperforms GPT-4 on longer contexts. LLama-3.1 uses multistage pre-training from 8K to 128K with progressive length increases.
- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* Fine-tuned Mamba-130M achieves strong results on BABILong but is impractical beyond 128K due to slow inference.
- **Bulatov et al. (2022, 2024)** -- *Recurrent Memory Transformer / Beyond Attention.* RMT provides the backbone for the fine-tuned models that achieve record sequence processing (11.1M tokens for RMT, 50M for ARMT).
- **Rodkin et al. (2024)** -- *Associative Recurrent Memory Transformer (ARMT).* Achieves the record of 50M-token processing on BABILong QA1 by combining recurrent memory with trainable retrieval.

### Context Extension Methods

- **Peng et al. (2023b)** -- *YaRN: Efficient Context Window Extension.* Evaluated on BABILong; fails to extend effective context despite stable long-context perplexity.
- **Zhang et al. (2024a)** -- *Activation Beacon.* Evaluated as a context extension method; performs better than YaRN but still achieves <40% at 32K.

### Evaluation Infrastructure

- **Hendrycks et al. (2020)** -- *MMLU.* Used to compute cross-benchmark correlations showing that BABILong diverges from MMLU at shorter contexts than RULER does.

#### Cross-References in Available Papers

- **RULER (2024-10-ruler-context-size):** BABILong explicitly compares against RULER in Section 3.4 and Figure 4, showing that BABILong's correlation with MMLU drops from 2K tokens while RULER's stays constant. Both benchmarks share the NIAH extension concept but differ in task diversity and haystack naturalness.
- **Lost in the Middle (2024-02-lost-in-the-middle):** BABILong's Appendix K (Figure 10) analyzes fact position effects on GPT-4 performance, finding that mid-context facts are hardest to identify, consistent with the lost-in-the-middle phenomenon.
- **NoLiMa (2025-07-nolima-long-context-evaluation):** NoLiMa notes that some BABILong tasks (e.g., counting at 28% accuracy at 0K) confound task difficulty with context-length difficulty, and reports that models achieving effective lengths of 16K--32K on BABILong achieve only 2K on NoLiMa.
- **Context Length Hurts Performance (2025-11-context-length-hurts-performance):** Cites BABILong's gap between retrieval and reasoning performance in long contexts, which it disentangles by controlling for perfect retrieval.
- **YaRN (2024-05-yarn-context-extension):** YaRN-Mistral-7b-128k is evaluated on BABILong and fails to extend effective context despite stable perplexity, consistent with RULER's findings on the same model.
