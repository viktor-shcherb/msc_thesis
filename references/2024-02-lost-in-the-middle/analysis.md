# Lost in the Middle: How Language Models Use Long Contexts

**Authors:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang (Stanford University, University of California Berkeley, Samaya AI)
**Date:** February 2024, TACL Volume 12, pages 157--173, DOI:10.1162/tacl_a_00638 (arXiv:2307.03172)

---

## Core Research Problem

Recent language models have been extended to accept increasingly long input contexts (4K, 32K, up to 100K tokens), enabled by hardware improvements and algorithmic advances such as FlashAttention (Dao et al., 2022) and efficient architectures. However, it remains unclear **how well these models actually use information within long input contexts** when performing downstream tasks. This matters because many practical applications -- retrieval-augmented generation, processing long documents, multi-turn dialogue -- require models to reason over thousands of tokens of provided context. Prior work by Khandelwal et al. (2018) showed that small LSTM language models make increasingly coarse use of longer-term context, and Qin et al. (2023) found that efficient Transformers are recency-biased on long-context NLP tasks. Ivgi et al. (2023) compared encoder-decoder QA performance when the relevant paragraph is at the beginning vs. a random position, finding a preference for beginning-of-context information, but only examined two position conditions. The core challenge is: **characterizing how the position of relevant information within long input contexts affects language model performance, and understanding the practical implications for retrieval-augmented and long-context applications.**

---

## Problem Solutions

The paper provides an empirical characterization rather than a new method. The key findings are:

1. **U-shaped performance curve:** Language model performance on tasks requiring information retrieval from input contexts follows a distinctive U-shape as a function of the position of relevant information -- performance is highest when relevant information occurs at the very beginning (primacy bias) or end (recency bias) of the context, and significantly degrades when relevant information is in the middle.
2. **Extended-context models do not help:** Models with extended context windows (e.g., GPT-3.5-Turbo 16K vs. 4K, Claude-1.3 100K vs. 8K) show nearly identical performance to their non-extended counterparts when input fits within the shorter context window, indicating that extending the context window does not improve information utilization.
3. **Architecture matters:** Encoder-decoder models (Flan-UL2, Flan-T5-XXL) are relatively robust to position changes within their training-time sequence length, but exhibit U-shaped degradation when extrapolating beyond it.
4. **More context is not always better:** In open-domain QA, reader model performance saturates long before retriever recall, suggesting diminishing returns from providing more retrieved documents.

---

## Approach Details

### Method

This is an empirical study with two controlled experimental tasks:

**Task 1: Multi-document question answering.** The model receives a question and k documents (Wikipedia passages of at most 100 tokens), where exactly one document contains the answer and k - 1 are retrieved distractors. Performance is measured as the position of the answer-containing document varies across all k positions.

- Data: 2655 queries from NaturalQuestions-Open (Lee et al., 2019; Kwiatkowski et al., 2019) where the annotated long answer is a paragraph.
- Answer document: the Wikipedia paragraph containing the NaturalQuestions-annotated answer.
- Distractor documents: k - 1 passages retrieved by Contriever (fine-tuned on MS-MARCO; Izacard et al., 2021) that are most relevant to the query but do not contain any annotated answers, presented in order of decreasing relevance.
- Evaluation metric: accuracy -- whether any of the correct answers from NaturalQuestions annotations appear in the predicted output.

**Task 2: Synthetic key-value retrieval.** The model receives a JSON object with k key-value pairs (128-bit UUIDs) and must return the value associated with a specified key. This isolates the basic ability to retrieve matching tokens from the input context, removing natural language semantics as a potential confounder.

- 500 examples each at 75, 140, and 300 key-value pairs.
- Evaluation metric: accuracy -- whether the correct UUID value appears in the predicted output.

Both tasks admit controlled manipulation of (i) input context length (changing k) and (ii) position of relevant information (changing the order of documents or position of the target key-value pair).

### Key Technical Components

- **Position modulation:** The answer-containing document is placed at different positions within the ordered list of documents. For multi-document QA with k = 20 documents, the answer document is tested at positions 1, 5, 10, 15, and 20.
- **Context length modulation:** Experiments use k = 10 (~2K tokens), 20 (~4K tokens), and 30 (~6K tokens) for multi-document QA, and 75 (~4K tokens), 140 (~8K tokens), and 300 (~16K tokens) key-value pairs for retrieval.
- **Closed-book and oracle baselines:** Closed-book provides the answer from parametric memory only (no documents); oracle provides only the single answer-containing document. These bracket the expected performance range.
- **Query-aware contextualization:** Placing the query both before and after the documents/key-value pairs, enabling decoder-only models to attend to the query when contextualizing the data (mimicking the bidirectional encoder of encoder-decoder models).
- **Greedy decoding** is used for all models.

### Experimental Setup

**Models evaluated:**

| Model | Type | Max Context |
|---|---|---|
| GPT-3.5-Turbo (0613) | Closed, decoder-only | 4K tokens |
| GPT-3.5-Turbo (16K, 0613) | Closed, decoder-only | 16K tokens |
| Claude-1.3 | Closed, decoder-only | 8K tokens |
| Claude-1.3 (100K) | Closed, decoder-only | 100K tokens |
| MPT-30B-Instruct | Open, decoder-only (ALiBi) | 8192 tokens |
| LongChat-13B (16K) | Open, decoder-only (condensed RoPE) | 16384 tokens |
| Flan-T5-XXL | Open, encoder-decoder | 512 tokens (training) |
| Flan-UL2 | Open, encoder-decoder | 2048 tokens (training) |
| GPT-4 (8K) | Closed, decoder-only | 8K tokens (subset eval) |
| Llama-2 (7B, 13B, 70B) | Open, decoder-only | 4096 tokens |

**Additional ablations:**
- Random distractors instead of retrieved hard negatives (Appendix B).
- Randomly ordered distractors with modified instructions (Appendix C).
- Unambiguous question subset using AmbigQA annotations (Appendix A).
- Base vs. instruction fine-tuned models (MPT-30B vs. MPT-30B-Instruct).
- Open-domain QA with Contriever retriever, varying k from 5 to 50 retrieved documents.

### Key Results

**Multi-document QA (20 documents, ~4K tokens):**

| Model | Best Position (1st) | Middle (10th) | Last (20th) | Closed-Book | Oracle |
|---|---|---|---|---|---|
| GPT-3.5-Turbo | 75.8% | 53.8% | 63.2% | 56.1% | 88.3% |
| GPT-3.5-Turbo (16K) | 75.7% | 54.1% | 63.1% | 56.0% | 88.6% |
| Claude-1.3 | 59.9% | 56.8% | 60.1% | 48.3% | 76.1% |
| Claude-1.3 (100K) | 59.8% | 57.0% | 60.0% | 48.2% | 76.4% |
| MPT-30B-Instruct | 53.7% | 52.2% | 56.3% | 31.5% | 81.9% |
| LongChat-13B (16K) | 68.6% | 55.3% | 55.0% | 35.0% | 83.4% |

- GPT-3.5-Turbo's mid-context performance (53.8%) is **lower than its closed-book performance** (56.1%), meaning the added context actively hurts when the relevant document is in the middle.
- Performance drop from best to worst position exceeds **20 percentage points** for GPT-3.5-Turbo.
- Extended-context variants (GPT-3.5-Turbo 16K, Claude-1.3 100K) have nearly identical performance to their non-extended counterparts when input fits in the shorter window.

**Key-value retrieval (300 key-value pairs, ~16K tokens):**

| Model | Best Position | Worst Position |
|---|---|---|
| Claude-1.3 | ~100% | ~100% |
| Claude-1.3 (100K) | ~100% | ~100% |
| GPT-3.5-Turbo (16K) | ~80% | ~45.6% |
| MPT-30B-Instruct | ~80% | ~40% |

- Claude-1.3 and Claude-1.3 (100K) achieve near-perfect performance across all positions and context lengths.
- Other models exhibit the same U-shaped degradation, even on this simple exact-match retrieval task.
- With query-aware contextualization, all models achieve near-perfect key-value retrieval (e.g., GPT-3.5-Turbo 16K goes from 45.6% worst-case to 100%).

**Encoder-decoder models:**

| Setting | Flan-UL2 (within 2048 training length) | Flan-UL2 (beyond training length) |
|---|---|---|
| Best-worst accuracy gap (10 docs, ~2K tokens) | 1.9% | N/A |
| Best-worst accuracy gap (20 docs, ~4K tokens) | N/A | ~10% (U-shaped) |

**Open-domain QA (retriever-reader):**

- Using 50 instead of 20 retrieved documents improves performance by only ~1.5% for GPT-3.5-Turbo and ~1% for Claude-1.3, while retriever recall increases substantially over this range.
- Reader performance saturates long before retriever recall, indicating models fail to effectively use additional retrieved documents.

**Model scale (Llama-2):**

- 7B models are solely recency-biased (no primacy effect).
- 13B and 70B models exhibit the full U-shaped curve (both primacy and recency bias).
- Instruction fine-tuning and RLHF slightly reduce positional bias in 13B (worst-case gap narrows from ~20% to ~10%) but minimally affect 70B trends.

### Instruction Fine-Tuning Effects

Comparing MPT-30B (base) and MPT-30B-Instruct on 20-document QA: both exhibit the U-shaped curve, with the base model showing nearly 10% best-to-worst disparity compared to ~4% for the instruction-tuned model. This indicates that the U-shaped pattern is **not solely an artifact of instruction fine-tuning** -- it exists in base pretrained models as well.

### Practical Implications

The paper suggests two mitigation strategies for retrieval-augmented generation:
1. **Effective reranking:** Push relevant documents closer to the start of the input context, where models are best at using them.
2. **Ranked list truncation:** Retrieve fewer documents when appropriate, since adding more documents offers diminishing returns and may hurt performance by burying relevant information in the middle.

---

## Conclusions

1. **U-shaped positional bias in context utilization:** Language models exhibit a distinctive U-shaped performance curve when relevant information is placed at different positions in the input context -- they preferentially use information at the beginning (primacy bias) and end (recency bias), with significant degradation in the middle. For GPT-3.5-Turbo, mid-context performance drops below closed-book (no documents) performance.

2. **Extended context windows do not improve context utilization:** Models with extended context windows (GPT-3.5-Turbo 16K, Claude-1.3 100K) perform identically to their shorter-context counterparts on sequences that fit within the shorter window. Simply expanding the context window does not teach models to better use the context they already have.

3. **Encoder-decoder architecture provides partial robustness:** Encoder-decoder models (Flan-UL2, Flan-T5-XXL) are relatively robust to position changes within their training-time sequence length (1.9% best-worst gap), likely because their bidirectional encoder allows each document to attend to all others. This robustness breaks down when extrapolating beyond training length.

4. **Query-aware contextualization helps retrieval but not reasoning:** Placing the query before and after the context dramatically improves synthetic key-value retrieval (GPT-3.5-Turbo 16K from 45.6% worst-case to 100%) but minimally affects multi-document QA, suggesting that the QA task requires deeper reasoning beyond simple token matching.

5. **Positional bias is an emergent property of scale:** The U-shaped curve (with primacy bias) appears only in sufficiently large models (13B+ parameters). Smaller models (7B) are solely recency-biased, suggesting that primacy bias emerges with model scale.

6. **Diminishing returns of additional context in retrieval-augmented QA:** In open-domain QA, reader performance saturates long before retriever recall, with going from 20 to 50 documents yielding only ~1-1.5% improvement. This establishes that more context is not always better, and motivates research on reranking and list truncation.

7. **New evaluation protocol for long-context models:** The paper proposes that claims of robust long-context use must demonstrate minimal difference between best- and worst-case performance as a function of the position of relevant information, not just aggregate performance on long sequences.

---

## Core References and Why They Are Referenced

### Context Utilization Analysis
- **Khandelwal et al. (2018)** -- *Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context.* Showed that small LSTM language models make increasingly coarse use of longer-term context and are biased towards recent tokens. This paper extends that analysis to Transformer LMs, finding that larger models additionally exhibit primacy bias.
- **Sun et al. (2021)** -- *Do Long-Range Language Models Actually Use Long-Range Context?* Found that longer contexts improve prediction of only a few tokens, consistent with the theory of bounded mutual information. This paper's results complement these findings by showing positional effects in instruction-formatted prompting.
- **O'Connor and Andreas (2021)** -- *What Context Features Can Transformer Language Models Use?* Found that many information-destroying operations had marginal effects on Transformer LM predictions. Referenced as related work on how models use context.

### Retrieval-Augmented Generation
- **Petroni et al. (2020)** -- *How Context Affects Language Models' Factual Predictions.* Among the first to demonstrate combining retrieval context with pretrained LMs for unsupervised QA. This paper tests the effectiveness of this paradigm when context is long.
- **Izacard et al. (2021)** -- *Contriever: Unsupervised Dense Information Retrieval with Contrastive Learning.* Provides the retrieval system used in this paper to obtain distractor documents and for the open-domain QA case study.
- **Ram et al. (2023)** -- *In-Context Retrieval-Augmented Language Models.* Representative of the RAG paradigm that this paper evaluates.

### Evaluation Data
- **Kwiatkowski et al. (2019)** -- *Natural Questions: A Benchmark for Question Answering Research.* Source of the question-answer pairs used in the multi-document QA task and open-domain QA case study.
- **Lee et al. (2019)** -- *Latent Retrieval for Weakly Supervised Open Domain Question Answering.* Provides the NaturalQuestions-Open split used in the evaluation.
- **Min et al. (2020)** -- *AmbigQA: Answering Ambiguous Open-Domain Questions.* Provides ambiguity annotations used to create the unambiguous question subset (Appendix A).

### Models Evaluated
- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* Base model for LongChat-13B (16K).
- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Used in the model scale ablation (7B, 13B, 70B, with and without chat fine-tuning).
- **Li et al. (2023)** -- *How Long Can Open-Source LLMs Truly Promise on Context Length?* Provides LongChat-13B (16K) with condensed RoPE.
- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* Positional encoding method used by MPT-30B-Instruct.
- **Raffel et al. (2020)** and **Chung et al. (2022)** -- *T5* and *Scaling Instruction-Finetuned Language Models.* Provide Flan-T5-XXL.
- **Tay et al. (2023)** -- *UL2: Unifying Language Learning Paradigms.* Provides Flan-UL2.

### Efficient Attention and Architecture
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer paper. The paper notes that self-attention is technically equally capable of retrieving any token, making the observed serial-position effect surprising.
- **Dao et al. (2022)** -- *FlashAttention.* Referenced as an algorithmic improvement enabling larger context windows.
- **Beltagy et al. (2020)** -- *Longformer.* Efficient attention variant referenced in the long-context models related work.
- **Zaheer et al. (2020)** -- *Big Bird: Transformers for Longer Sequences.* Efficient attention variant referenced in related work.

### Serial-Position Effect
- **Ebbinghaus (1913)** -- *Memory: A Contribution to Experimental Psychology.* The U-shaped performance curve parallels the serial-position effect from psychology, where humans best recall the first (primacy) and last (recency) items in a list.
- **Murdock Jr (1962)** -- *The Serial Position Effect of Free Recall.* Further establishes the serial-position effect in human memory. The connection to language models is noted as surprising given the theoretical uniformity of self-attention.

### Concurrent / Related Retrieval Work
- **Ivgi et al. (2023)** -- *Efficient Long-Text Understanding with Short-Text Models.* Conducted similar needle-in-a-haystack experiments comparing beginning vs. random placement of relevant information in encoder-decoder models. This paper extends with finer-grained position analysis across more models and architectures.
- **Papailiopoulos et al. (2023)** -- *A Little Retrieval Test for Large Language Models.* Similar goal to the key-value retrieval task. This paper differs by using random UUIDs to remove natural language confounders.

#### Cross-References in Available Papers

- **PI (2023-06-pi-positional-interpolation):** Not directly connected. PI addresses context window extension via position interpolation; this paper tests whether models can effectively *use* extended contexts, finding that they often cannot. The two papers address complementary aspects of the long-context problem: PI solves how to enable long contexts mechanically, while this paper shows that enabling long contexts does not guarantee effective utilization.
- **NTK-Aware Scaled RoPE (2023-06-rope-ntk):** Similarly addresses context extension from the position encoding side. This paper's finding that extended-context models do not outperform their shorter counterparts provides empirical motivation for why position encoding methods alone are insufficient.
- **YaRN (2024-05-yarn-context-extension):** YaRN extends context windows via improved RoPE interpolation. This paper's results motivate evaluating such methods not just on perplexity but on position-controlled information retrieval tasks.
- **RULER (2024-10-ruler-context-size):** RULER provides a benchmark for evaluating long-context capabilities with controlled complexity, directly building on the insight from this paper that position-controlled evaluation is essential.
