# Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization

**Authors:** Cheng-Yu Hsieh, Yung-Sung Chuang, Chun-Liang Li, Zifeng Wang, Long T. Le, Abhishek Kumar, James Glass, Alexander Ratner, Chen-Yu Lee, Ranjay Krishna, Tomas Pfister (University of Washington, MIT, Google Cloud AI Research, Google DeepMind)
**Date:** August 2024, Findings of ACL 2024, DOI:10.18653/v1/2024.findings-acl.890 (arXiv:2406.16008)

---

## Core Research Problem

Large language models trained to handle long input contexts consistently struggle to locate and use relevant information placed in the middle of their input -- the "lost-in-the-middle" phenomenon first characterized by Liu et al. (2023). While this behavior has been observed across multiple decoder-only LLMs (Touvron et al., 2023; Li et al., 2023a; OpenAI, 2022), **the underlying cause remained poorly understood**. Prior mitigation strategies relied on re-ranking documents and re-ordering the most relevant ones to the beginning or end of the context (Jiang et al., 2023; Peysakhovich and Lerer, 2023). However, re-ranking requires additional supervision or dedicated fine-tuning (Karpukhin et al., 2020; Shi et al., 2023c; Sun et al., 2023), and critically, re-ranking does not fundamentally improve LLMs' ability to utilize mid-sequence context -- it merely avoids placing important content there.

**The core challenge is: identifying the mechanistic cause of the lost-in-the-middle phenomenon and developing an intervention that directly improves LLMs' ability to attend to relevant context regardless of its position in the input.**

---

## Problem Solutions

The paper establishes that the lost-in-the-middle problem is caused by an intrinsic U-shaped positional attention bias in decoder-only LLMs, and proposes a calibration mechanism to remove it. The key contributions are:

1. **Causal link to attention bias.** The authors show that LLMs assign higher attention to tokens at the beginning and end of the input, regardless of content relevance. This U-shaped attention pattern persists even after randomly shuffling document order, confirming it is positional rather than content-driven.
2. **Additive decomposition model.** Model attention on a document is decomposed into an additive combination of a relevance term and a position-dependent bias term, validated empirically with 83% and 72% concordance on two monotonicity conditions.
3. **Calibration via dummy document subtraction.** By measuring attention on a content-neutral dummy document at each position, the positional bias is estimated and subtracted, yielding calibrated attention scores that reflect true document relevance.
4. **Practical attention intervention.** The calibrated relevance scores are used to rescale token-level attention weights at inference time, improving RAG performance by up to 15 percentage points without any fine-tuning.

---

## Approach Details

### Method

The paper follows the experimental setup of Liu et al. (2023): a model answers a query x^q given K documents D = {x^gold, x^distract_1, ..., x^distract_{K-1}}, serialized as x^prompt = [x^q, x^doc_1, ..., x^doc_K, x^q] (the question is repeated before and after the documents). Experiments use Vicuna-7b-v1.5-16k (16K context) on NaturalQuestions (Kwiatkowski et al., 2019) with K = 20 documents.

**Measuring document-level attention.** Given an input prompt, the attention allocated to the k-th document is defined as the average per-token attention weight:

> Attn(x^prompt, k) = (1/N_k) * sum_{i=1}^{N_k} attn(x^doc_{k,i})

where attn(x^doc_{k,i}) is the attention weight on token i of document k when predicting the next token after the full prompt. Attention is averaged across all decoder layers and heads.

**Two key observations:**

1. **U-shaped attention bias.** Plotting Attn(x^prompt, k) across positions k = 1...20 reveals a U-shaped curve: documents at positions 1 and 20 receive the highest attention, while mid-sequence documents (positions 8--12) receive the lowest. This pattern persists after randomly shuffling document order, confirming that the bias is positional, not content-driven (Figure 4).

2. **Attention-generation correlation.** Documents receiving higher attention are disproportionately likely to be used in the model's response: 74% of incorrect predictions use content from the highest-attention half of documents, vs. 26% from the lowest-attention half (Table 1). This establishes a direct link between the positional attention bias and the lost-in-the-middle performance degradation.

### Key Technical Components

**Additive attention model.** The authors hypothesize that observed attention decomposes as:

> Attn(x^doc, k) = f(rel(x^doc), bias(k))

where rel(.) measures document relevance, bias(.) is the positional bias, and f is monotonically increasing in both arguments. Two necessary conditions are validated on 100 randomly sampled NaturalQuestions examples (K = 20):

| Condition | rel(x^doc) | bias(k) | % of valid pairs |
|---|---|---|---|
| Condition 1: fixed relevance, varying position | Fixed | Varying | 83% |
| Condition 2: varying relevance, fixed position | Varying | Fixed | 72% |

Following Occam's razor, the authors adopt a simple linear model:

> Attn(x^doc, k) = rel(x^doc) + bias(k) + epsilon

This yields a Spearman rank correlation of 0.76 between Attn(x^doc1, k) - Attn(x^doc2, k) and Attn(x^doc1, l) - Attn(x^doc2, l) across quadruplets (x^doc1, x^doc2, k, l), supporting the additive form. A log-linear alternative achieves comparable 0.75 correlation (Appendix C).

**Calibrated attention via dummy document.** With the additive model, the positional bias can be removed by subtraction. A content-neutral dummy document x^dum is placed at each position k, and its attention is measured:

> Attn(x^dum, k) = rel(x^dum) + bias(k) + epsilon

Subtracting gives the calibrated (bias-free) relevance estimate:

> rel(x^doc) = Attn(x^doc, k) - Attn(x^dum, k) + rel(x^dum)

Since rel(x^dum) is a constant across positions, the ranking of documents by Attn(x^doc, k) - Attn(x^dum, k) reflects their true relevance.

**Attention redistribution.** To operationalize calibration as an inference-time intervention, the attention values on tokens within each document are rescaled:

> attn_calibrated(x^doc_{k,i}) = (alpha_k / Attn_original(x^doc_k)) * attn_original(x^doc_{k,i}) * C

where alpha_k = Softmax(rel(x^doc_k), t), t is a temperature hyperparameter (set to 5e-5 for all experiments), and C is a normalization constant ensuring total attention is preserved. This makes the effective document-level attention proportional to relevance:

> Attn_calibrated(x^doc_k) proportional to Softmax(rel(x^doc_k), t)

**Intervention scope.** Attention calibration is applied only to the last 16 of 32 decoder layers (all attention heads in those layers). Intervening on early layers leads to unstable generation.

### Experimental Setup

**Models:**

| Model | Type | Context Window |
|---|---|---|
| Vicuna-7b-v1.5-16k | Open, decoder-only | 16K tokens |
| Tulu-2-7b | Open, decoder-only | 8K tokens |

Both models have 32 decoder layers with 32 attention heads each.

**Datasets:**

| Dataset | Type | # Queries | K | Source |
|---|---|---|---|---|
| NaturalQuestions | Open-domain QA | 2655 | 10, 20 | Wikipedia paragraphs via Contriever retrieval |
| SynthWiki | Synthetic multi-doc QA | 990 | 10, 20 | GPT-4 generated fictional Wikipedia paragraphs |

NaturalQuestions uses the 2655-query subset from Liu et al. (2023) with distractor documents from Contriever (Izacard et al., 2022a) in decreasing relevance order. SynthWiki (Peysakhovich and Lerer, 2023) uses GPT-4-generated paragraphs about fictional people to minimize knowledge contamination.

**Baselines for document ranking (Table 3):**
- Vanilla attention: rank by uncalibrated Attn(x^prompt, k).
- Query generation (Sun et al., 2023): rank by likelihood of generating the query from each document.
- Relevance generation (Sun et al., 2023): prompt the model to judge document-query relevance.

**Baselines for RAG performance (Figure 6):**
- Prompt reordering (Sun et al., 2023; Liang et al., 2023): reorder by prompted relevance scores.
- LongLLMLingua-r_k (Jiang et al., 2023): reorder by query generation likelihood.
- Attention sorting (Peysakhovich and Lerer, 2023): iteratively sort by vanilla attention.

**Hardware:** Two NVIDIA A100 GPUs. Inference: 1--3 hours per dataset. Greedy decoding throughout; no training or hyperparameter search required.

### Key Results

**Calibrated attention for document ranking (Table 3, Recall@3 on NaturalQuestions, gold document in the middle):**

| Method | K = 10 | K = 20 |
|---|---|---|
| Vanilla attention | 0.3638 | 0.2052 |
| Query generation | 0.6851 | 0.5815 |
| Relevance generation | 0.5521 | 0.4012 |
| Calibrated attention | **0.7427** | **0.6832** |

- Calibrated attention outperforms vanilla attention by 38--48 Recall@3 points.
- It also outperforms query generation (the next best method) by 6--10 points.

**RAG accuracy with attention calibration (Table 5, selected results):**

| Dataset | Model | Method | 1st | Middle | Last | Avg. |
|---|---|---|---|---|---|---|
| NQ (K=20) | Vicuna | Vanilla | 71.93 | 47.34 | 50.65 | 56.64 |
| NQ (K=20) | Vicuna | Calibrated | 66.40 | 56.19 | 51.75 | 58.11 |
| NQ (K=20) | Tulu | Vanilla | 56.94 | 35.32 | 46.59 | 46.28 |
| NQ (K=20) | Tulu | Calibrated | 57.17 | 43.08 | 61.50 | 53.91 |
| SynthWiki (K=20) | Vicuna | Vanilla | 53.73 | 43.63 | 60.20 | 52.52 |
| SynthWiki (K=20) | Vicuna | Calibrated | 57.77 | 51.21 | 68.78 | 59.25 |
| SynthWiki (K=20) | Tulu | Vanilla | 80.40 | 60.30 | 95.75 | 78.81 |
| SynthWiki (K=20) | Tulu | Calibrated | 82.22 | 75.15 | 96.14 | 84.50 |

- Mid-sequence improvements of 6--15 percentage points across all settings.
- Calibrated attention performance curves lie above vanilla baselines in 22 out of 24 position-model-dataset combinations.
- Slight performance decrease at position 1 (e.g., Vicuna on NQ drops from 71.93 to 66.40) reflects the deliberate redistribution of attention away from position-favored documents.

**Complementarity with re-ordering methods (Table 5, LongLLMLingua-r_k + Calibration):**

| Dataset | Model | LongLLMLingua-r_k | LongLLMLingua-r_k + Cal. |
|---|---|---|---|
| NQ (K=10) | Vicuna | 63.95 | 66.17 |
| NQ (K=20) | Vicuna | 59.92 | 62.22 |
| NQ (K=10) | Tulu | 56.39 | 61.31 |
| NQ (K=20) | Tulu | 43.90 | 47.34 |
| SynthWiki (K=10) | Vicuna | 70.50 | 73.43 |
| SynthWiki (K=20) | Vicuna | 62.42 | 66.96 |

- Calibration provides 2--5 percentage point improvements on top of re-ordering, achieving the highest overall performance across all settings.

### Limitations

1. **Simplified attention model.** The additive decomposition (Eq. 2) may not fully capture more intricate or adaptive attention dynamics.
2. **Computational overhead.** The method requires O(K) additional forward passes (one per position with the dummy document) to estimate the positional bias.
3. **Bias removal may be harmful.** In some tasks, positional bias may align with task structure (e.g., temporal ordering). Blanket removal may not always be beneficial.
4. **Root cause unexplained.** The paper identifies and calibrates the positional attention bias but does not determine its origin (pretraining data distribution, architecture, or optimization).

---

## Conclusions

1. **Positional attention bias causes lost-in-the-middle.** LLMs exhibit a U-shaped attention distribution over documents regardless of content, and this correlates directly with the U-shaped performance curve in RAG tasks. Documents receiving higher attention are used in 74% of model responses.

2. **Attention decomposes additively into relevance and positional bias.** An additive model Attn = rel + bias fits the data with 0.76 Spearman rank correlation and satisfies monotonicity conditions in 72--83% of tested pairs.

3. **Calibrated attention recovers true document relevance.** Subtracting the attention on a dummy document removes the positional bias, yielding relevance estimates that outperform query generation and relevance prompting by 6--10 Recall@3 points.

4. **Inference-time attention intervention improves RAG performance.** Redistributing attention according to calibrated relevance yields 6--15 percentage point improvements on mid-sequence gold documents, across two models, two datasets, and two context lengths (K = 10, 20).

5. **Complementary to re-ordering methods.** Attention calibration stacks on top of existing re-ordering pipelines (LongLLMLingua, prompt reordering, attention sorting), providing a further 2--5 percentage point boost. This suggests calibration addresses a fundamentally different aspect of the problem than re-ordering.

6. **LLMs can find relevant context in the middle.** The results challenge the view that LLMs inherently cannot use mid-sequence information. Models do attend to relevant documents even in the middle, but the overwhelming positional bias masks this signal. Removing the bias reveals latent retrieval capability.

7. **Training-free approach.** The method works as a pure inference-time intervention on off-the-shelf LLMs, requiring no fine-tuning, additional training data, or model modifications. The only hyperparameter (temperature t = 5e-5) is robust across all tested settings.

---

## Core References and Why They Are Referenced

### Lost-in-the-Middle Problem

- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Defines and characterizes the lost-in-the-middle phenomenon with the U-shaped performance curve across 10+ models. This paper directly explains the mechanistic cause (positional attention bias) of the phenomenon Liu et al. documented.
- **Peysakhovich and Lerer (2023)** -- *Attention Sorting Combats Recency Bias in Long Context Language Models.* Proposes iterative attention-based document sorting as a workaround. Provides the SynthWiki dataset used in evaluation. This paper's calibration approach is compared against attention sorting as a baseline.

### Re-ranking and RAG Methods

- **Sun et al. (2023)** -- *Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents.* Provides the query generation and relevance generation baselines for document ranking, and the prompt reordering baseline for RAG evaluation.
- **Jiang et al. (2023)** -- *LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression.* Provides the LongLLMLingua-r_k reordering baseline. This paper shows that calibration applied on top of LongLLMLingua-r_k yields the highest overall RAG performance.

### Attention Mechanisms and Interpretability

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational self-attention mechanism. The U-shaped positional bias is a surprising finding given that self-attention has no built-in position preference beyond what is encoded by positional embeddings.
- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* One of the early attention analysis works. Referenced as precedent for using attention weights to understand model behavior.
- **Dong et al. (2021)** -- *On-the-Fly Attention Modulation for Neural Generation.* Precedent for modifying attention weights at inference time to influence generation behavior.
- **Zhang et al. (2023)** -- *Tell Your Model Where to Attend: Post-Hoc Attention Steering for LLMs.* Related post-hoc attention intervention method. Finding the optimal set of attention heads to intervene on is left as future work, referencing this paper.

### Evaluation Data

- **Kwiatkowski et al. (2019)** -- *Natural Questions: A Benchmark for Question Answering Research.* Source of the 2655-query evaluation set for open-domain QA experiments.
- **Izacard et al. (2022a)** -- *Unsupervised Dense Information Retrieval with Contrastive Learning (Contriever).* Retrieval system used to obtain distractor documents for NaturalQuestions.

### Models Evaluated

- **Li et al. (2023a)** -- *How Long Can Open-Source LLMs Truly Promise on Context Length?* Provides Vicuna-7b-v1.5-16k, the primary model used throughout the paper.
- **Wang et al. (2023)** -- *How Far Can Camels Go? Exploring the State of Instruction Tuning on Open Resources.* Provides Tulu-2-7b, the second model used for evaluation.

### Context and Distraction

- **Shi et al. (2023a)** -- *Large Language Models Can Be Easily Distracted by Irrelevant Context.* Establishes that LLMs are susceptible to distraction by irrelevant content. This paper refines this finding: the model's bias toward the first document is positional rather than content-driven, persisting even after random shuffling.
- **Ravaut et al. (2023)** -- *On Position Bias in Summarization with Large Language Models.* Shows that position bias extends to content utilization in summarization, supporting the hypothesis that positional attention bias affects downstream generation.

#### Cross-References in Available Papers

- **Lost in the Middle (2024-02-lost-in-the-middle):** This paper directly builds on and explains the lost-in-the-middle phenomenon documented by Liu et al. (2023). It uses the same NaturalQuestions evaluation setup (2655 queries, K = 10 and 20, Contriever distractors) and demonstrates that the U-shaped performance curve is caused by U-shaped positional attention bias. Where Liu et al. documented the effect, this paper identifies the cause and proposes a calibration mechanism to fix it.
- **Attention Sinks (2024-05-attention-sinks-streaming):** Xiao et al. (2023) show that initial tokens act as "attention sinks" receiving disproportionate attention regardless of semantic content. This paper's finding of elevated attention at the beginning of the input is consistent with the attention sink phenomenon, extending it from a per-token observation to a document-level analysis in RAG settings.
- **Context Length Hurts Performance (2025-11-context-length-hurts-performance):** Du et al. (2025) demonstrate that context length alone degrades performance independent of retrieval. That paper places evidence at the beginning (the position this paper identifies as most favored by positional bias) and still observes degradation, suggesting that positional attention bias is one contributing factor but not the only mechanism through which long contexts hurt performance.
- **Irrelevant Context Distraction (2023-07-gsm-ic-irrelevant-context):** Shi et al. (2023) show LLMs are distracted by irrelevant context. This paper refines the finding: the bias toward early documents is positional rather than content-driven, suggesting the mechanism is attention bias rather than semantic distraction alone.
