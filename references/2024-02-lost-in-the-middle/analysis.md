---
title: "Lost in the Middle: How Language Models Use Long Contexts"
authors: "Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang"
year: 2024
venue: "TACL 2024"
paper_type: journal-paper
categories: ["position-bias", "long-context-evaluation"]
scope: ["context utilization patterns", "multi-document QA", "key-value retrieval", "positional bias in LLMs"]
benchmarks_used: ["natural-questions"]
models_introduced: []
models_evaluated: ["gpt-3.5-turbo", "gpt-4", "llama-2-7b", "llama-2-13b", "llama-2-70b"]
key_claims:
  - id: C1
    claim: "Language models exhibit a U-shaped performance curve on multi-document QA: best when relevant information is at the beginning or end of the context, worst when it is in the middle"
    evidence: "Figure 1, Figure 5, Section 2.3, Tables 5-7 (Appendix G)"
    status: contested
    contested_by: 2024-08-found-in-the-middle
  - id: C2
    claim: "Extended-context models (GPT-3.5-Turbo 16K, Claude-1.3 100K) perform nearly identically to their non-extended counterparts when input fits within the shorter context window"
    evidence: "Figure 5, Section 2.3"
    status: supported
  - id: C3
    claim: "For GPT-3.5-Turbo with 20 documents, mid-context accuracy (53.8%) drops below closed-book accuracy (56.1%), meaning added context actively hurts performance"
    evidence: "Section 2.3, Table 1, Table 6 (Appendix G)"
    status: supported
  - id: C4
    claim: "Encoder-decoder models (Flan-UL2) are robust to position changes within training-time context length (1.9% best-worst gap) but exhibit U-shaped degradation when extrapolating beyond it"
    evidence: "Figure 8, Section 4.1"
    status: supported
  - id: C5
    claim: "Query-aware contextualization enables near-perfect key-value retrieval (GPT-3.5-Turbo 16K worst-case improves from 45.6% to 100%) but minimally affects multi-document QA trends"
    evidence: "Section 4.2, Figure 9"
    status: supported
  - id: C6
    claim: "The U-shaped curve exists in base pretrained models (MPT-30B), not solely as an artifact of instruction fine-tuning"
    evidence: "Figure 10, Section 4.3"
    status: supported
  - id: C7
    claim: "Primacy bias only appears in models with 13B+ parameters; 7B Llama-2 models are solely recency-biased"
    evidence: "Figure 16, Appendix E"
    status: supported
  - id: C8
    claim: "In open-domain QA, reader performance saturates long before retriever recall: using 50 instead of 20 documents yields only ~1.5% improvement for GPT-3.5-Turbo"
    evidence: "Figure 11, Section 5"
    status: supported
cross_references:
  - target: 2024-08-found-in-the-middle
    type: extended-by
    detail: "Found in the Middle identifies positional attention bias as the mechanistic cause of the U-shaped curve and proposes calibration to mitigate it, showing models can use mid-context information when bias is removed"
  - target: 2025-07-position-bias-transformers
    type: extended-by
    detail: "Provides a theoretical framework for why positional biases emerge in Transformers"
  - target: 2025-11-pos2distill-position-bias-distillation
    type: extended-by
    detail: "Uses the lost-in-the-middle phenomenon as motivation for position-bias-aware knowledge distillation"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "Attention sinks at initial tokens may contribute to the primacy effect in the U-shaped curve"
  - target: 2024-08-longbench-bilingual-benchmark
    type: complementary
    detail: "LongBench uses random evidence placement to avoid the position biases identified here"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: complementary
    detail: "DroPE cites Lost in the Middle as evidence that RoPE-scaling methods degrade when information is deep in context"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention's position-independent retrieval mechanism could mitigate the U-shaped curve"
  - target: 2026-01-longbench-pro
    type: complementary
    detail: "Cites this paper as foundational work on the gap between advertised and effective context length"
  - target: 2019-08-bert-attention-analysis
    type: complementary
    detail: "Clark et al. identify positional attention biases in BERT (next/previous token specialization), foreshadowing the context utilization biases documented here"
  - target: 2023-07-gsm-ic-irrelevant-context
    type: complementary
    detail: "Both papers show LLMs struggle with context utilization; GSM-IC focuses on distractor content while this paper focuses on positional bias"
  - target: 2023-11-needle-in-a-haystack
    type: complementary
    detail: "NIAH tests position-dependent retrieval of a single fact; this paper provides a more controlled multi-position experimental setup with both QA and synthetic retrieval tasks"
  - target: 2025-11-context-length-hurts-performance
    type: complementary
    detail: "Extends the analysis to show that context length alone degrades performance even without positional manipulation"
  - target: 2025-04-effective-context-length-falls-short
    type: complementary
    detail: "Formalizes the gap between advertised context window size and effective utilization length, building on the observations in this paper"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: extended-by
    detail: "LongICLBench extends the lost-in-the-middle analysis to ICL settings, confirming position bias via grouped-distribution experiments with up to 46.5% accuracy drops"
  - target: 2025-07-nolima-long-context-evaluation
    type: extended-by
    detail: "NoLiMa confirms lost-in-the-middle in one-hop tasks but shows that in two-hop scenarios without literal cues, context length dominates over position"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong embeds reasoning tasks in long contexts at controlled positions, complementing the positional bias analysis here with tasks requiring multi-hop reasoning rather than single-fact retrieval"
  - target: 2024-03-gemini-1.5-long-context
    type: complementary
    detail: "Gemini 1.5's MRCR evaluation tests position-dependent retrieval with adversarially similar needles, extending the position bias analysis to millions of tokens"
open_questions:
  - question: "Is the U-shaped curve a fundamental property of Transformer attention or an artifact of training data distributions and task design?"
    addressed_by: 2024-08-found-in-the-middle
  - question: "Can architectural modifications beyond encoder-decoder (e.g., sparse attention, landmark tokens) fully mitigate positional bias in context utilization?"
    addressed_by: null
  - question: "How do the findings generalize to tasks requiring deeper reasoning over long contexts, such as summarization, multi-step reasoning, or code understanding?"
    addressed_by: null
  - question: "What training strategies (data ordering, longer sequence training, explicit position-agnostic objectives) could reduce positional bias?"
    addressed_by: null
---
# Lost in the Middle: How Language Models Use Long Contexts

**Authors:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang (Stanford University, University of California Berkeley, Samaya AI)
**Date:** February 2024, TACL Volume 12, pages 157--173, DOI:10.1162/tacl_a_00638 (arXiv:2307.03172)

---

## Core Research Problem

Recent language models have been extended to accept increasingly long input contexts (4K, 32K, up to 100K tokens), enabled by hardware improvements and algorithmic advances such as FlashAttention (Dao et al., 2022) and efficient architectures. However, it remains unclear **how well these models actually use information within long input contexts** when performing downstream tasks. This matters because many practical applications -- retrieval-augmented generation, long-document processing, multi-turn dialogue -- require models to reason over thousands of tokens of provided context.

Prior work established that small LSTM language models make increasingly coarse use of longer-term context and are biased towards recent tokens (Khandelwal et al., 2018). Sun et al. (2021) found that longer contexts improve prediction of only a few tokens, consistent with bounded mutual information theory (Sharan et al., 2018). Qin et al. (2023) found that efficient Transformers are recency-biased on long-context NLP tasks. Ivgi et al. (2023) compared encoder-decoder QA performance when the relevant paragraph is at the beginning vs. a random position, finding a preference for beginning-of-context information, but only examined two position conditions.

**The core challenge is: characterizing how the position of relevant information within long input contexts affects language model performance across architectures, and understanding the practical implications for retrieval-augmented and long-context applications.**

---

## Problem Solutions

The paper provides an **empirical characterization** rather than a new method. The key findings are:

1. **U-shaped performance curve.** Language model performance on tasks requiring information retrieval from input contexts follows a distinctive U-shape as a function of position -- performance is highest when relevant information occurs at the very beginning (primacy bias) or end (recency bias) of the context, and significantly degrades when relevant information is in the middle.
2. **Extended-context models do not help.** Models with extended context windows (e.g., GPT-3.5-Turbo 16K vs. 4K, Claude-1.3 100K vs. 8K) show nearly identical performance to their non-extended counterparts when input fits within the shorter window.
3. **Architecture matters.** Encoder-decoder models (Flan-UL2, Flan-T5-XXL) are relatively robust to position changes within their training-time sequence length, but exhibit U-shaped degradation when extrapolating beyond it.
4. **Query-aware contextualization helps retrieval but not reasoning.** Placing the query before and after the documents enables near-perfect synthetic key-value retrieval, but minimally changes multi-document QA trends.
5. **Positional bias is scale-dependent.** The full U-shaped curve (primacy + recency) appears only in models with 13B+ parameters; smaller models (7B) are solely recency-biased.
6. **More context is not always better.** In open-domain QA, reader model performance saturates long before retriever recall, indicating diminishing returns from additional retrieved documents.

---

## Approach Details

### Method

This is an empirical study with two controlled experimental tasks designed to isolate the effect of position on information utilization.

**Task 1: Multi-document question answering.** The model receives a question and k documents (Wikipedia passages of at most 100 tokens), where exactly one document contains the answer and k - 1 are retrieved distractors. Performance is measured as the position of the answer-containing document varies across all k positions.

- Data: 2655 queries from NaturalQuestions-Open (Lee et al., 2019; Kwiatkowski et al., 2019) where the annotated long answer is a paragraph.
- Answer document: the Wikipedia paragraph containing the NaturalQuestions-annotated answer.
- Distractor documents: k - 1 passages retrieved by Contriever (fine-tuned on MS-MARCO; Izacard et al., 2021) that are most relevant to the query but do not contain any annotated answers, presented in order of decreasing relevance.
- Evaluation metric: accuracy -- whether any correct answer from NaturalQuestions annotations appears in the predicted output.

**Task 2: Synthetic key-value retrieval.** The model receives a JSON object with k key-value pairs (128-bit UUIDs) and must return the value associated with a specified key. This isolates the basic ability to retrieve matching tokens from the input context, removing natural language semantics as a potential confounder.

- 500 examples each at 75, 140, and 300 key-value pairs.
- Evaluation metric: accuracy -- whether the correct UUID value appears in the predicted output.

Both tasks admit controlled manipulation of (i) input context length (changing k) and (ii) position of relevant information (changing the order of documents or position of the target key-value pair).

### Key Technical Components

- **Position modulation.** The answer-containing document is placed at different positions within the ordered list. For k = 20 documents, the answer document is tested at positions 1, 5, 10, 15, and 20 (Section 2.1, Figure 3).
- **Context length modulation.** Experiments use k = 10 (~2K tokens), 20 (~4K tokens), and 30 (~6K tokens) for multi-document QA, and 75 (~4K tokens), 140 (~8K tokens), and 300 (~16K tokens) key-value pairs for retrieval.
- **Closed-book and oracle baselines.** Closed-book provides the answer from parametric memory only (no documents); oracle provides only the single answer-containing document. These bracket the expected performance range (Table 1).
- **Query-aware contextualization.** Placing the query both before and after the documents/key-value pairs, enabling decoder-only models to attend to the query when contextualizing the data (mimicking the bidirectional encoder of encoder-decoder models; Section 4.2).
- **Greedy decoding** is used for all models (Section 2.2).
- **Ablations.** Random distractors instead of retrieved hard negatives (Appendix B); randomly ordered distractors with modified instructions (Appendix C); unambiguous question subset using AmbigQA annotations (Appendix A); base vs. instruction fine-tuned models (MPT-30B vs. MPT-30B-Instruct, Section 4.3).

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
| GPT-4 (8K) | Closed, decoder-only | 8K tokens (subset eval, Appendix D) |
| Llama-2 (7B, 13B, 70B) | Open, decoder-only | 4096 tokens (Appendix E) |

MPT-30B-Instruct was pretrained on 1T tokens with 2048-token sequences, then adapted on 50B tokens with 8192-token sequences, using ALiBi positional encoding (Press et al., 2022). LongChat-13B (16K) extends LLaMA-13B (Touvron et al., 2023a) from 2048 to 16384 tokens via condensed rotary positional embeddings (Li et al., 2023). Flan-UL2 was initially trained with 512-token sequences, then pretrained for an additional 100K steps with 1024 tokens before instruction fine-tuning on sequences with 2048 encoder tokens and 512 decoder tokens (Tay et al., 2023).

### Key Results

**Multi-document QA (20 documents, ~4K tokens, Table 6 in Appendix G):**

| Model | 1st Position | 5th Position | 10th Position | 15th Position | 20th Position | Closed-Book | Oracle |
|---|---|---|---|---|---|---|---|
| GPT-3.5-Turbo | 75.8% | 57.2% | 53.8% | 55.4% | 63.2% | 56.1% | 88.3% |
| GPT-3.5-Turbo (16K) | 75.7% | 57.3% | 54.1% | 55.4% | 63.1% | 56.0% | 88.6% |
| Claude-1.3 | 59.9% | 55.9% | 56.8% | 57.2% | 60.1% | 48.3% | 76.1% |
| Claude-1.3 (100K) | 59.8% | 55.9% | 57.0% | 57.4% | 60.0% | 48.2% | 76.4% |
| MPT-30B-Instruct | 53.7% | 51.8% | 52.2% | 52.7% | 56.3% | 31.5% | 81.9% |
| LongChat-13B (16K) | 68.6% | 57.4% | 55.3% | 52.5% | 55.0% | 35.0% | 83.4% |

- GPT-3.5-Turbo's mid-context performance (53.8%) is **lower than its closed-book performance** (56.1%), meaning the added context actively hurts when the relevant document is in the middle (Section 2.3).
- Performance drop from best to worst position exceeds **20 percentage points** for GPT-3.5-Turbo.
- Extended-context variants (GPT-3.5-Turbo 16K, Claude-1.3 100K) have **nearly identical performance** to their non-extended counterparts when input fits in the shorter window (Figure 5).

**Key-value retrieval (300 key-value pairs, ~16K tokens, Figure 7):**

| Model | Near-Best Position | Near-Worst Position |
|---|---|---|
| Claude-1.3 | ~100% | ~100% |
| Claude-1.3 (100K) | ~100% | ~100% |
| GPT-3.5-Turbo (16K) | ~80% | ~45.6% |
| MPT-30B-Instruct | ~80% | ~40% |

- Claude-1.3 achieves near-perfect performance across all positions and context lengths.
- Other models exhibit the same U-shaped degradation, even on this simple exact-match retrieval task (Figure 7).
- With query-aware contextualization, all models achieve near-perfect key-value retrieval (e.g., GPT-3.5-Turbo 16K goes from 45.6% worst-case to 100%; Section 4.2).

**Encoder-decoder models (Figure 8):**

| Setting | Flan-UL2 best-worst gap |
|---|---|
| 10 docs (~2K tokens, within 2048 training length) | 1.9% |
| 20 docs (~4K tokens, beyond training length) | ~10% (U-shaped) |
| 30 docs (~6K tokens, beyond training length) | Larger U-shaped gap |

- Encoder-decoder models are relatively robust within training-time context length, likely because bidirectional encoding allows each document to attend to all others. Robustness breaks down when extrapolating beyond training length (Section 4.1).

### Instruction Fine-Tuning Effects

Comparing MPT-30B (base) and MPT-30B-Instruct on 20-document QA (Figure 10): both exhibit the U-shaped curve. The base model shows nearly 10% best-to-worst disparity compared to ~4% for the instruction-tuned model. This indicates that the U-shaped pattern is **not solely an artifact of instruction fine-tuning** -- it exists in base pretrained models as well. The authors hypothesize that base models learn to use similarly-formatted data from Internet text seen during pretraining, e.g., StackOverflow questions and answers (Section 4.3).

### Model Scale Effects

Llama-2 models of varying sizes (7B, 13B, 70B) were evaluated on 20-document QA (Figure 16, Appendix E):

- **7B models** are solely recency-biased (no primacy effect), with or without chat fine-tuning.
- **13B and 70B models** exhibit the full U-shaped curve (both primacy and recency bias).
- Instruction fine-tuning and RLHF slightly reduce positional bias in 13B (worst-case gap narrows from ~20% to ~10%) but minimally affect 70B trends.
- The 13B base model shows a 20-point accuracy disparity between best and worst positions, which chat fine-tuning reduces to ~10 points. The 70B models show largely similar trends with and without fine-tuning.

The authors hypothesize that prior work (e.g., Khandelwal et al., 2018; Sun et al., 2021) did not observe primacy bias because the models studied were too small (<1B parameters).

### Open-Domain QA Case Study

Using a standard retriever-reader setup with Contriever on NaturalQuestions-Open (Section 5, Figure 11):

- Using 50 instead of 20 retrieved documents improves performance by only ~1.5% for GPT-3.5-Turbo and ~1% for Claude-1.3, while retriever recall increases substantially over this range.
- Reader performance saturates long before retriever recall, indicating models fail to effectively use additional retrieved documents.

The paper suggests two practical mitigations: (1) effective reranking to push relevant documents closer to the start of the input context, and (2) ranked list truncation to retrieve fewer documents when appropriate (Arampatzis et al., 2009).

---

## Limitations and Failure Modes

- **Two tasks only.** The study evaluates only multi-document QA and synthetic key-value retrieval. Generalization to other long-context tasks (summarization, multi-step reasoning, code understanding) is not tested.
- **Multi-document QA design may confound position bias.** The distractor documents are presented in order of decreasing relevance, which may introduce a prior for models to favor early documents. Although Appendix C (randomized distractor order) shows the same trends, the task structure itself has been questioned by subsequent work (see Found in the Middle, 2024-08-found-in-the-middle).
- **Greedy decoding only.** All experiments use greedy decoding. Other decoding strategies (sampling, beam search, self-consistency) are not explored and might alter the severity of positional bias.
- **Mid-2023 model vintage.** The primary models evaluated (GPT-3.5-Turbo, Claude-1.3, MPT-30B-Instruct, LongChat-13B) are from mid-2023. Subsequent model generations may exhibit different positional bias patterns.
- **No mechanistic explanation.** The paper characterizes the U-shaped phenomenon empirically but does not explain the underlying mechanism causing it. The authors offer hypotheses (training data distribution, instruction fine-tuning format) but do not test them directly.
- **Coarse position granularity.** Position is modulated at the document level (e.g., positions 1, 5, 10, 15, 20 for 20 documents), not at the token level, limiting the resolution of the analysis.
- **Limited instruction fine-tuning analysis.** Only one model pair (MPT-30B base vs. instruct) is used to study the effect of instruction fine-tuning. The interaction between fine-tuning data composition and positional bias is not systematically explored.
- **Model-specific exceptions.** Claude-1.3 achieves near-perfect key-value retrieval across all positions, and LongChat-13B (16K) sometimes generates code instead of outputting values directly (Section 3.2), indicating that the U-shaped pattern is not universal across all models and tasks.

---

## Conclusions

### Contributions

1. **U-shaped positional bias in context utilization.** Established that language models exhibit a distinctive U-shaped performance curve when relevant information is placed at different positions in the input context -- they preferentially use information at the beginning (primacy bias) and end (recency bias), with significant degradation in the middle. For GPT-3.5-Turbo with 20 documents, mid-context performance (53.8%) drops below closed-book performance (56.1%) (Figure 1, Figure 5, Table 1, Section 2.3).

2. **Extended context windows do not improve context utilization.** Demonstrated that models with extended context windows (GPT-3.5-Turbo 16K, Claude-1.3 100K) perform identically to their shorter-context counterparts on sequences fitting within the shorter window, indicating that simply expanding the context window does not improve information utilization (Figure 5, Section 2.3).

3. **Encoder-decoder robustness within training length.** Showed that encoder-decoder models (Flan-UL2, Flan-T5-XXL) are relatively robust to position changes within their training-time sequence length (1.9% best-worst gap for Flan-UL2), likely due to bidirectional encoding. This robustness breaks down when extrapolating beyond training length (Figure 8, Section 4.1).

4. **Dissociation between retrieval and reasoning via query-aware contextualization.** Demonstrated that placing the query before and after the context dramatically improves synthetic key-value retrieval (GPT-3.5-Turbo 16K from 45.6% worst-case to 100%) but minimally affects multi-document QA, separating the retrieval and reasoning components of positional bias (Section 4.2, Figure 9).

5. **Positional bias is not solely from instruction fine-tuning.** Showed that base pretrained models (MPT-30B) also exhibit the U-shaped curve, though instruction fine-tuning slightly reduces worst-case disparity (from ~10% to ~4%) (Figure 10, Section 4.3).

6. **Scale-dependent primacy bias.** Established that the full U-shaped curve (primacy + recency) emerges only in models with 13B+ parameters, while 7B models are solely recency-biased (Figure 16, Appendix E).

7. **Diminishing returns of additional context in retrieval-augmented QA.** In open-domain QA, reader performance saturates long before retriever recall, with 20 to 50 documents yielding only ~1-1.5% improvement, motivating research on reranking and list truncation (Figure 11, Section 5).

### Implications

1. **New evaluation protocol for long-context models.** Claims of robust long-context use should demonstrate minimal difference between best- and worst-case performance as a function of the position of relevant information, not just aggregate performance on long sequences (Section 1). [Inference: this protocol is proposed but not yet widely adopted.]

2. **Retrieval-augmented generation pipeline design.** The findings motivate placing relevant documents at the beginning of the context and limiting the number of retrieved documents, rather than naively increasing context length (Section 5). [Inference: practical implication, not experimentally validated as a mitigation strategy in this paper.]

3. **Training data distribution as a potential cause.** The positional bias may stem from training data distributions where important information disproportionately appears at the beginning or end of documents. If confirmed, position-aware data curation during pretraining could mitigate the bias. [Speculative: the paper does not test this hypothesis directly.]

---

## Key Claims

1. **U-shaped performance curve in multi-document QA.** Performance is highest when relevant information occurs at the very beginning or end of the input context, and degrades significantly in the middle. GPT-3.5-Turbo shows more than 20 percentage points drop from best to worst position with 20 documents (Figure 1, Figure 5, Tables 5-7 in Appendix G, Section 2.3). Status: **contested** (by 2024-08-found-in-the-middle, which attributes the curve partly to multi-document QA design artifacts).

2. **Extended-context models do not improve utilization.** GPT-3.5-Turbo and GPT-3.5-Turbo (16K) have nearly superimposed performance curves when input fits within the 4K-token window. The same holds for Claude-1.3 vs. Claude-1.3 (100K) (Figure 5, Section 2.3). Status: **supported**.

3. **Mid-context performance drops below closed-book.** For GPT-3.5-Turbo with 20 documents, accuracy at the 10th position (53.8%) is lower than closed-book accuracy (56.1%), meaning the provided documents actively hurt performance when the answer is in the middle (Section 2.3, Table 1, Table 6 in Appendix G). Status: **supported**.

4. **Encoder-decoder robustness within training-time context length.** Flan-UL2 has only 1.9% absolute difference between best- and worst-case performance in the 10-document setting (~2K tokens, within its 2048-token training length), compared to much larger gaps for decoder-only models. Beyond training length, the U-shaped degradation appears (Figure 8, Section 4.1). Status: **supported**.

5. **Query-aware contextualization helps retrieval but not QA.** Placing the query before and after the context enables near-perfect key-value retrieval for all models (e.g., GPT-3.5-Turbo 16K from 45.6% worst-case to 100% at 300 KV pairs), but only slightly changes performance trends in multi-document QA (Section 4.2, Figure 9). Status: **supported**.

6. **U-shaped curve exists in base pretrained models.** Both MPT-30B (base) and MPT-30B-Instruct show U-shaped performance, with the base model having ~10% best-worst disparity vs. ~4% for the instruction-tuned model (Figure 10, Section 4.3). Status: **supported**.

7. **Primacy bias requires sufficient model scale.** Llama-2 7B models (with or without chat fine-tuning) are solely recency-biased. The full U-shaped curve with primacy bias appears only in 13B and 70B models (Figure 16, Appendix E). Status: **supported**.

8. **Reader performance saturates before retriever recall.** In open-domain QA with Contriever, going from 20 to 50 retrieved documents improves GPT-3.5-Turbo performance by only ~1.5% and Claude-1.3 by ~1%, while retriever recall continues to increase substantially (Figure 11, Section 5). Status: **supported**.

---

## Open Questions

1. **Fundamental property vs. task artifact.** Is the U-shaped curve a fundamental property of Transformer attention, or is it an artifact of training data distributions and multi-document QA task design? Partially addressed by 2024-08-found-in-the-middle, which argues task design plays a significant role, but the synthetic key-value retrieval results (which also show U-shaped patterns for some models) suggest a deeper architectural component.

2. **Architectural mitigations.** Can architectural modifications beyond encoder-decoder models (e.g., sparse attention, landmark tokens, NoPE/DroPE) fully mitigate positional bias in context utilization? Not yet systematically addressed.

3. **Generalization to other tasks.** How do the findings generalize to tasks requiring deeper reasoning over long contexts, such as multi-document summarization, multi-step reasoning chains, or code understanding? The paper only evaluates QA and synthetic retrieval. Not yet addressed.

4. **Training-time mitigations.** What training strategies -- such as position-balanced data ordering, longer sequence pretraining, or explicit position-agnostic training objectives -- could reduce positional bias? Not yet addressed.

---

## Core References and Why They Are Referenced

### Context Utilization Analysis

- **Khandelwal et al. (2018)** -- *Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context.* Showed that small LSTM language models make increasingly coarse use of longer-term context and are biased towards recent tokens. This paper extends that analysis to Transformer LMs, finding that larger models additionally exhibit primacy bias. The absence of primacy bias in prior work is attributed to the small scale of models studied (<1B parameters).

- **Sun et al. (2021)** -- *Do Long-Range Language Models Actually Use Long-Range Context?* Found that longer contexts improve prediction of only a few tokens, consistent with bounded mutual information theory. This paper's results complement those findings by showing positional effects in instruction-formatted prompting beyond next-word prediction.

- **O'Connor and Andreas (2021)** -- *What Context Features Can Transformer Language Models Use?* Found that many information-destroying operations had marginal effects on Transformer LM predictions. Referenced as related work on how models use context.

- **Sharan et al. (2018)** -- *Prediction with a Short Memory.* Showed that sequence distributions with bounded mutual information necessarily lead to marginal average prediction benefits from increasingly long context. Provides theoretical grounding for the diminishing returns of longer context observed empirically.

### Retrieval-Augmented Generation

- **Petroni et al. (2020)** -- *How Context Affects Language Models' Factual Predictions.* Among the first to demonstrate combining retrieval context with pretrained LMs for unsupervised QA. This paper tests how effective this paradigm is when context is long and relevant information position varies.

- **Izacard et al. (2021)** -- *Contriever: Unsupervised Dense Information Retrieval with Contrastive Learning.* Provides the retrieval system used to obtain distractor documents and for the open-domain QA case study.

- **Ram et al. (2023)** -- *In-Context Retrieval-Augmented Language Models.* Representative of the RAG paradigm that this paper evaluates.

### Evaluation Data

- **Kwiatkowski et al. (2019)** -- *Natural Questions: A Benchmark for Question Answering Research.* Source of the question-answer pairs used in the multi-document QA task and open-domain QA case study (2655 queries with paragraph long answers).

- **Lee et al. (2019)** -- *Latent Retrieval for Weakly Supervised Open Domain Question Answering.* Provides the NaturalQuestions-Open split used in the evaluation.

- **Min et al. (2020)** -- *AmbigQA: Answering Ambiguous Open-Domain Questions.* Provides ambiguity annotations used to create the unambiguous question subset (Appendix A), confirming that the U-shaped findings hold on unambiguous questions.

### Models Evaluated

- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* Base model for LongChat-13B (16K), which extends LLaMA-13B's context window using condensed RoPE.

- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Used in the model scale ablation (7B, 13B, 70B, with and without chat fine-tuning) to study how primacy bias emerges with scale (Appendix E).

- **Li et al. (2023)** -- *How Long Can Open-Source LLMs Truly Promise on Context Length?* Provides LongChat-13B (16K) with condensed rotary positional embeddings.

- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* Positional encoding method used by MPT-30B-Instruct.

- **Raffel et al. (2020)** and **Chung et al. (2022)** -- *T5* and *Scaling Instruction-Finetuned Language Models.* Provide Flan-T5-XXL for the encoder-decoder comparison.

- **Tay et al. (2023)** -- *UL2: Unifying Language Learning Paradigms.* Provides Flan-UL2, the primary encoder-decoder model showing 1.9% positional robustness within training-time context.

### Architecture and Attention

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer paper. The paper notes that self-attention is technically equally capable of retrieving any token, making the observed serial-position effect surprising.

- **Dao et al. (2022)** -- *FlashAttention.* Referenced as an algorithmic improvement enabling larger context windows without changing the attention mechanism itself.

### Serial-Position Effect

- **Ebbinghaus (1913)** -- *Memory: A Contribution to Experimental Psychology.* The U-shaped performance curve parallels the serial-position effect from psychology, where humans best recall the first (primacy) and last (recency) items in a list.

- **Murdock Jr (1962)** -- *The Serial Position Effect of Free Recall.* Further establishes the serial-position effect in human memory. The connection to language models is noted as surprising given the theoretical uniformity of self-attention.

### Prior Position-Sensitivity Work

- **Ivgi et al. (2023)** -- *Efficient Long-Text Understanding with Short-Text Models.* Conducted similar needle-in-a-haystack experiments comparing beginning vs. random placement of relevant information in encoder-decoder models. This paper extends the analysis with finer-grained position modulation across more models and architectures.

- **Qin et al. (2023)** -- *The NLP Task Effectiveness of Long-Range Transformers.* Found that efficient Transformers are recency-biased on long-context NLP tasks. This paper extends these findings to standard Transformer LMs and additionally discovers primacy bias in larger models.
