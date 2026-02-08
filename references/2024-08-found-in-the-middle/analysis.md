---
title: "Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization"
authors: "Hsieh, Chuang, Li, Wang, Le, Kumar, Glass, Ratner, Lee, Krishna, Pfister"
year: 2024
venue: "Findings of ACL 2024"
paper_type: conference-paper
categories: ["position-bias", "attention-analysis"]
scope: ["positional attention bias in decoder-only LLMs", "RAG performance", "multi-document QA"]
benchmarks_used: ["natural-questions", "synthwiki"]
models_introduced: []
models_evaluated: ["vicuna-7b-v1.5-16k", "tulu-2-7b"]
key_claims:
  - id: C1
    claim: "LLMs exhibit a U-shaped positional attention bias where tokens at the beginning and end receive higher attention regardless of content relevance, persisting after random document shuffling"
    evidence: "Figure 4, Section 2.1"
    status: supported
    scope: "Vicuna-7b-v1.5-16k, K=20 documents, NaturalQuestions, greedy decoding"
    magnitude: "~4x attention ratio between positions 1/20 and mid-sequence positions 8-12 (0.00020 vs 0.00005)"
  - id: C2
    claim: "Documents receiving higher model attention are disproportionately used in generation: 74% of incorrect predictions use content from the highest-attention half of documents"
    evidence: "Table 1, Section 2.2"
    status: supported
    scope: "Vicuna-7b-v1.5-16k, K=20, NaturalQuestions, gold doc at position 10, incorrect predictions only"
    magnitude: "526 out of 712 incorrect examples (74%) vs 186 (26%)"
  - id: C3
    claim: "Model attention decomposes additively into document relevance and positional bias terms, with monotonicity conditions holding in 83% and 72% of tested pairs and 0.76 Spearman rank correlation"
    evidence: "Table 2, Section 3.1"
    status: supported
    scope: "Vicuna-7b-v1.5-16k, K=20, 100 randomly sampled NaturalQuestions examples"
    magnitude: "83% valid pairs (Condition 1), 72% valid pairs (Condition 2), 0.76 Spearman rank correlation (linear), 0.75 (log-linear)"
  - id: C4
    claim: "Calibrated attention outperforms existing document ranking methods, achieving 0.7427 and 0.6832 Recall@3 at K=10 and K=20, surpassing the next best method (query generation) by 6-10 points"
    evidence: "Table 3, Section 3.2"
    status: supported
    scope: "Vicuna-7b-v1.5-16k, NaturalQuestions, gold document placed in the middle, greedy decoding"
    magnitude: "0.7427 vs 0.6851 (K=10), 0.6832 vs 0.5815 (K=20), improvement of 5.8-10.2 Recall@3 points"
  - id: C5
    claim: "Inference-time attention calibration improves mid-sequence RAG accuracy by 6-15 percentage points across two models and two datasets without any fine-tuning"
    evidence: "Figure 5, Table 5, Section 4.2"
    status: supported
    scope: "Vicuna-7b-v1.5-16k and Tulu-2-7b, NaturalQuestions and SynthWiki, K=10 and K=20, greedy decoding, last 16 of 32 layers"
    magnitude: "6-15 pp mid-sequence improvement; calibrated curve above vanilla in 22/24 position-model-dataset combinations"
  - id: C6
    claim: "Attention calibration is complementary to re-ordering methods, providing 2-5 percentage point additional improvements on top of LongLLMLingua-r_k"
    evidence: "Figure 6, Table 5, Section 4.3"
    status: supported
    scope: "Vicuna-7b-v1.5-16k and Tulu-2-7b, NaturalQuestions and SynthWiki, K=10 and K=20"
    magnitude: "2-5 pp average accuracy improvement on top of LongLLMLingua-r_k across all tested settings"
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: extends
    detail: "Directly uses Liu et al.'s experimental setup and explains the mechanistic cause (positional attention bias) of the U-shaped performance curve; challenges the interpretation that models fundamentally cannot use mid-context information"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Both address position bias: this paper provides empirical analysis and practical mitigation through attention calibration, while Position Bias provides theoretical analysis of why position biases emerge"
  - target: 2023-07-gsm-ic-irrelevant-context
    type: complementary
    detail: "GSM-IC establishes that LLMs are distracted by irrelevant context; this paper refines the finding to show the bias is positional rather than purely content-driven, persisting even after random document shuffling"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "Attention sinks at initial tokens may contribute to the primacy component of the U-shaped attention bias documented here"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Builds on the foundational self-attention mechanism; the U-shaped positional bias is a surprising emergent property given that self-attention has no built-in position preference beyond positional embeddings"
  - target: 2019-08-bert-attention-analysis
    type: complementary
    detail: "Early attention analysis work showing positional patterns in BERT; this paper extends attention analysis to document-level positional bias in decoder-only LLMs"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: complementary
    detail: "LongICLBench documents recency bias in ICL through grouped-distribution analysis, complementing the positional attention bias findings and RAG-focused calibration in this paper"
  - target: 2025-11-pos2distill-position-bias-distillation
    type: complementary
    detail: "Pos2Distill proposes a training-based alternative to attention calibration for mitigating position bias, using self-distillation from advantageous positions rather than inference-time attention reweighting"
  - target: 2024-12-lost-in-the-middle-in-between
    type: complementary
    detail: "Baker et al. show the positional bias persists and compounds in multi-hop QA, where inter-document distance adds a second dimension to the bias beyond absolute position; attention calibration could potentially address both dimensions"
  - target: 2025-07-position-bias-single-dimension-scaling
    type: complementary
    detail: "Both mitigate position bias at inference time without training: this paper calibrates document-level attention via dummy-document subtraction, while Yu et al. scale a single positional hidden states channel; both evaluate on NaturalQuestions with 20 documents"
  - target: 2025-04-pine-eliminating-position-bias
    type: complementary
    detail: "PINE proposes bidirectional inter-document attention and importance-based position re-assignment as an alternative to attention calibration for eliminating position bias, with formal invariance guarantees"
  - target: 2024-08-flenqa-input-length-reasoning
    type: complementary
    detail: "FlenQA shows length degrades reasoning even at optimal positions (key paragraphs first), indicating the positional attention bias identified here is one mechanism but length-induced degradation is broader"
open_questions:
  - question: "What is the root cause of positional attention bias -- pretraining data distribution, transformer architecture, or optimization process?"
    addressed_by: null
  - question: "What is the optimal set of attention heads to intervene on for attention calibration, rather than applying to all heads in the last 16 layers?"
    addressed_by: null
  - question: "Are there tasks where positional attention bias is beneficial and blanket removal would be harmful?"
    addressed_by: null
  - question: "Can more efficient calibration methods be developed that reduce the O(K) forward pass overhead?"
    addressed_by: null
---

# Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization

**Authors:** Cheng-Yu Hsieh (University of Washington; Google Cloud AI Research), Yung-Sung Chuang (MIT), Chun-Liang Li (Google Cloud AI Research), Zifeng Wang (Google Cloud AI Research), Long T. Le (Google Cloud AI Research), Abhishek Kumar (Google DeepMind), James Glass (MIT), Alexander Ratner (University of Washington), Chen-Yu Lee (Google Cloud AI Research), Ranjay Krishna (University of Washington), Tomas Pfister (Google Cloud AI Research)
**Date:** August 2024, Findings of ACL 2024, DOI:10.18653/v1/2024.findings-acl.890 (arXiv:2406.16008)

---

## Core Research Problem

Large language models trained to handle long input contexts consistently struggle to locate and use relevant information placed in the middle of their input -- the "lost-in-the-middle" phenomenon first characterized by Liu et al. (2023). This U-shaped performance degradation has been observed across multiple decoder-only LLMs (Touvron et al., 2023; Li et al., 2023a; OpenAI, 2022), yet the underlying cause remained poorly understood. Prior mitigation strategies relied on re-ranking documents and re-ordering the most relevant ones to the beginning or end of the context (Jiang et al., 2023; Peysakhovich and Lerer, 2023). However, re-ranking requires additional supervision or dedicated fine-tuning (Karpukhin et al., 2020; Shi et al., 2023c; Sun et al., 2023), and critically, re-ordering does not fundamentally improve LLMs' ability to utilize mid-sequence context -- it merely avoids placing important content there.

**The core challenge is: identifying what causes the lost-in-the-middle phenomenon and developing an intervention that directly improves LLMs' ability to attend to relevant context regardless of its position in the input.**

---

## Problem Solutions

The paper establishes that the lost-in-the-middle problem is caused by an intrinsic U-shaped positional attention bias in decoder-only LLMs, and proposes a calibration mechanism ("found-in-the-middle") to remove it. The key contributions are:

1. **Causal link to attention bias.** LLMs assign higher attention to tokens at the beginning and end of the input, regardless of content relevance. This U-shaped attention pattern persists after randomly shuffling document order, confirming it is positional rather than content-driven.
2. **Attention-generation correlation.** Documents receiving higher attention are disproportionately used in generation: 74% of incorrect predictions incorporate content from the highest-attention half of documents.
3. **Additive decomposition model.** Model attention on a document decomposes additively into a relevance term and a position-dependent bias term, validated empirically with monotonicity conditions holding in 83% and 72% of tested pairs.
4. **Calibration via dummy document subtraction.** By measuring attention on a content-neutral dummy document at each position, the positional bias is estimated and subtracted, yielding calibrated attention scores that reflect true document relevance.
5. **Inference-time attention intervention.** The calibrated relevance scores are used to rescale token-level attention weights at inference time, improving RAG performance by up to 15 percentage points without any fine-tuning.

---

## Approach Details

### Method

The paper follows the experimental setup of Liu et al. (2023): a model answers a query x^q given K documents D = {x^gold, x^distract_1, ..., x^distract_{K-1}}, serialized as x^prompt = [x^q, x^doc_1, ..., x^doc_K, x^q] (the question is repeated before and after the documents). Initial experiments use Vicuna-7b-v1.5-16k on NaturalQuestions (Kwiatkowski et al., 2019) with K = 20 documents, focusing on error analysis when the gold document is placed at the middle (10th) position.

**Measuring document-level attention.** Given an input prompt, the attention allocated to the k-th document is defined as the average per-token attention weight:

> Attn(x^prompt, k) = (1/N_k) * sum_{i=1}^{N_k} attn(x^doc_{k,i})

where attn(x^doc_{k,i}) is the attention weight on token i of document k when predicting the next |x^prompt| + 1 token. Attention is averaged across all decoder layers and attention heads.

**Two key observations:**

1. **U-shaped attention bias.** Plotting Attn(x^prompt, k) across positions k = 1...20 reveals a U-shaped curve: documents at positions 1 and 20 receive the highest attention (~0.00020), while mid-sequence documents (positions 8-12) receive the lowest (~0.00005). This pattern persists after randomly shuffling document order, confirming that the bias is positional, not content-driven (Figure 4).

2. **Attention-generation correlation.** Documents receiving higher attention are disproportionately likely to be used in the model's response. This is confirmed both qualitatively -- the model's output exhibits a strong bias toward the first-position document regardless of shuffling (Figure 2), measured via TF-IDF similarity between response and each document (Figure 3) -- and quantitatively (Table 1):

| Document attention group | # of examples | % |
|---|---|---|
| Highest half attention | 526 | 74% |
| Lowest half attention | 186 | 26% |

### Key Technical Components

**Additive attention model.** The authors hypothesize that observed attention decomposes as:

> Attn(x^prompt, k) = f(rel(x^doc_k), bias(k))

where rel(.) measures document relevance, bias(.) is the positional bias, and f is monotonically increasing in both arguments. Two necessary conditions are validated on 100 randomly sampled NaturalQuestions examples (K = 20):

| Condition | rel(x^doc) | bias(k) | % of valid pairs |
|---|---|---|---|
| Condition 1: fixed relevance, varying position | Fixed | Varying | 83% |
| Condition 2: varying relevance, fixed position | Varying | Fixed | 72% |

Following Occam's razor, the authors adopt a simple linear model:

> Attn(x^doc, k) = rel(x^doc) + bias(k) + epsilon

This yields a Spearman rank correlation of 0.76 between Attn(x^doc1, k) - Attn(x^doc2, k) and Attn(x^doc1, l) - Attn(x^doc2, l) across quadruplets (x^doc1, x^doc2, k, l), supporting the additive form. A log-linear alternative achieves comparable 0.75 correlation (Appendix C, Table 4):

| Model form of f | Rank correlation |
|---|---|
| Linear | 0.76 |
| Log-linear | 0.75 |

**Calibrated attention via dummy document.** With the additive model, the positional bias can be removed by subtraction. A content-neutral dummy document x^dum is placed at each position k, and its attention is measured:

> Attn(x^dum, k) = rel(x^dum) + bias(k) + epsilon

Subtracting gives the calibrated (bias-free) relevance estimate:

> rel(x^doc) = Attn(x^doc, k) - Attn(x^dum, k) + rel(x^dum)

Since rel(x^dum) is a constant across positions, ranking documents by Attn(x^doc, k) - Attn(x^dum, k) reflects their true relevance. The authors call this **calibrated attention** and the overall mechanism **found-in-the-middle**.

**Attention redistribution for RAG.** To operationalize calibration as an inference-time intervention, the attention values on tokens within each document are rescaled:

> attn_calibrated(x^doc_{k,i}) = (alpha_k / Attn_original(x^doc_k)) * attn_original(x^doc_{k,i}) * C

where alpha_k = Softmax(rel(x^doc_k), t), t is the temperature hyperparameter (set to 5e-5 for all experiments), and C is a normalization constant ensuring total attention is preserved. This makes the effective document-level attention proportional to relevance:

> Attn_calibrated(x^doc_k) proportional to Softmax(rel(x^doc_k), t)

**Intervention scope.** Attention calibration is applied only to the last 16 of 32 decoder layers (all attention heads in those layers). Intervening on early layers leads to unstable generation (Appendix B). The temperature t = 5e-5 is robust across all tested settings (Appendix B).

### Experimental Setup

**Models:**

| Model | Type | Context Window |
|---|---|---|
| Vicuna-7b-v1.5-16k | Open, decoder-only, 7B params | 16K tokens |
| Tulu-2-7b | Open, decoder-only, 7B params | 8K tokens |

Both models have 32 decoder layers with 32 attention heads each.

**Datasets:**

| Dataset | Type | # Entries | K | Source |
|---|---|---|---|---|
| NaturalQuestions | Open-domain QA | 2655 queries | 10, 20 | Wikipedia paragraphs via Contriever retrieval |
| SynthWiki | Synthetic multi-doc QA | 990 entries | 10, 20 | GPT-4 generated fictional Wikipedia paragraphs |

NaturalQuestions uses the 2655-query subset from Liu et al. (2023) with distractor documents from Contriever (Izacard et al., 2022a) in decreasing relevance order. SynthWiki (Peysakhovich and Lerer, 2023) uses GPT-4-generated paragraphs about fictional people to minimize knowledge contamination. Distractor documents in SynthWiki are randomly sampled and randomly ordered.

**Baselines for document ranking (Table 3):**
- Vanilla attention: rank by uncalibrated Attn(x^prompt, k).
- Query generation (Sun et al., 2023): rank by likelihood of generating the query from each document.
- Relevance generation (Sun et al., 2023): prompt the model to judge document-query relevance.

**Baselines for RAG performance (Table 5):**
- Attention sorting (Peysakhovich and Lerer, 2023): iteratively sort documents by vanilla attention.
- Prompt reordering (Sun et al., 2023; Liang et al., 2023): reorder by prompted relevance scores.
- LongLLMLingua-r_k (Jiang et al., 2023): reorder by query generation likelihood.
- LongLLMLingua-r_k + Calibration: LongLLMLingua-r_k with attention calibration applied on top.

**Hardware:** Two NVIDIA A100 GPUs. Inference: 1-3 hours per dataset. Greedy decoding throughout; no training or hyperparameter search required. All results are single-run (no variance reported) since greedy decoding is deterministic.

**Reproducibility:** The paper uses publicly available models (Vicuna-7b-v1.5-16k, Tulu-2-7b) and datasets (NaturalQuestions under Apache-2.0, SynthWiki). The method is purely inference-based with a single hyperparameter (t = 5e-5). No code availability is mentioned in the paper.

### Key Results

**Calibrated attention for document ranking (Table 3, Recall@3 on NaturalQuestions, gold document placed in the middle):**

| Method | K = 10 | K = 20 |
|---|---|---|
| Vanilla attention | 0.3638 | 0.2052 |
| Query generation | 0.6851 | 0.5815 |
| Relevance generation | 0.5521 | 0.4012 |
| **Calibrated attention** | **0.7427** | **0.6832** |

- Calibrated attention outperforms vanilla attention by 38-48 Recall@3 points.
- It also outperforms query generation (the next best method) by 5.8-10.2 points.
- Tested on a single model (Vicuna) and single dataset (NaturalQuestions) for document ranking (limited evidence for ranking claim specifically).

**RAG accuracy with attention calibration (Table 5, selected results):**

| Dataset | Model | Method | K=10 1st | K=10 5th | K=10 10th | K=10 Avg. | K=20 1st | K=20 10th | K=20 20th | K=20 Avg. |
|---|---|---|---|---|---|---|---|---|---|---|
| NQ | Vicuna | Vanilla | 74.35 | 54.83 | 52.01 | 60.39 | 71.93 | 47.34 | 50.65 | 56.64 |
| NQ | Vicuna | Calibrated | 70.84 | 62.61 | 55.78 | 63.07 | 66.40 | 56.19 | 51.75 | 58.11 |
| NQ | Tulu | Vanilla | 70.50 | 48.81 | 49.26 | 56.19 | 56.94 | 35.32 | 46.59 | 46.28 |
| NQ | Tulu | Calibrated | 71.52 | 57.13 | 63.54 | 64.06 | 57.17 | 43.08 | 61.50 | 53.91 |
| SynthWiki | Vicuna | Vanilla | 65.15 | 48.68 | 68.58 | 60.80 | 53.73 | 43.63 | 60.20 | 52.52 |
| SynthWiki | Vicuna | Calibrated | 68.58 | 53.83 | 74.14 | 65.52 | 57.77 | 51.21 | 68.78 | 59.25 |
| SynthWiki | Tulu | Vanilla | 92.22 | 81.51 | 94.34 | 89.35 | 80.40 | 60.30 | 95.75 | 78.81 |
| SynthWiki | Tulu | Calibrated | 92.92 | 87.77 | 95.25 | 91.98 | 82.22 | 75.15 | 96.14 | 84.50 |

- Mid-sequence improvements of 6-15 percentage points across all settings (tested across 2 models, 2 datasets, 2 context lengths -- moderate evidence).
- Calibrated attention performance curves lie above vanilla baselines in 22 out of 24 position-model-dataset combinations (Figure 5).
- Slight performance decrease at position 1 for some settings (e.g., Vicuna on NQ drops from 71.93 to 66.40 at K = 20) reflects the deliberate redistribution of attention away from position-favored documents.
- Average accuracy improvements range from 1.47 pp (NQ/Vicuna/K=20) to 7.87 pp (NQ/Tulu/K=10).

**Complementarity with re-ordering methods (Table 5, LongLLMLingua-r_k + Calibration, average accuracy):**

| Dataset | K | Model | LongLLMLingua-r_k | LongLLMLingua-r_k + Cal. | Improvement |
|---|---|---|---|---|---|
| NQ | 10 | Vicuna | 63.95 | 66.17 | +2.22 |
| NQ | 20 | Vicuna | 59.92 | 62.22 | +2.30 |
| NQ | 10 | Tulu | 56.39 | 61.31 | +4.92 |
| NQ | 20 | Tulu | 43.90 | 47.34 | +3.44 |
| SynthWiki | 10 | Vicuna | 70.50 | 73.43 | +2.93 |
| SynthWiki | 20 | Vicuna | 62.42 | 66.96 | +4.54 |
| SynthWiki | 10 | Tulu | 94.04 | 94.44 | +0.40 |
| SynthWiki | 20 | Tulu | 95.45 | 95.75 | +0.30 |

- Calibration provides 0.3-4.9 percentage point improvements on top of re-ordering across all 8 dataset-K-model combinations, achieving the highest overall performance.
- The improvement is smallest on SynthWiki/Tulu where both methods already achieve >94% accuracy (ceiling effect).

---

## Limitations and Failure Modes

The paper explicitly discusses four limitations (Section 6, Limitations):

1. **Simplified attention model.** The additive decomposition (Eq. 2) may not fully capture more intricate or adaptive attention dynamics. The intrinsic mechanisms driving positional bias could be more complex than the model accounts for, and some aspects of attention bias may be learnable or adaptive, responding to subtle aspects of the data or training process.

2. **Computational overhead.** The method requires O(K) additional forward passes (one per position with the dummy document) to estimate the positional bias. The authors frame the study as primarily a scientific investigation and expect future work to develop more efficient calibration methods.

3. **Positional bias may be beneficial.** In some tasks or scenarios, the natural tendency of models to focus on the beginning and end of inputs could align with the structure of the task or the nature of the data. Blanket removal of positional bias may not always be beneficial. Task-specific assessment is recommended before applying calibration.

4. **Root cause unexplained.** The paper identifies and calibrates the positional attention bias but does not determine its origin -- whether it stems from pretraining data distribution, transformer architecture, or optimization process.

5. **Performance decrease at favored positions.** Calibrated attention can slightly reduce performance when the gold document is at position 1 (e.g., Vicuna on NQ drops from 71.93 to 66.40 at K = 20), a direct consequence of redistributing attention away from position-favored documents (Table 5). In 2 out of 24 position-model-dataset combinations, calibrated attention slightly underperforms vanilla (Figure 5).

6. **[Inferred] Limited model scale.** Both models evaluated are 7B parameter models. The paper does not test whether the findings generalize to larger models (13B, 70B) or different architectures (e.g., encoder-decoder, non-RoPE position encodings).

#### Scope and Comparability

- **What was not tested:** Models larger than 7B parameters, non-decoder-only architectures, non-RoPE positional encodings, non-English datasets, tasks beyond multi-document QA (e.g., summarization, multi-hop reasoning, code generation), context lengths beyond 16K tokens, settings with more than 20 documents.
- **Comparability notes:** The experimental setup follows Liu et al. (2023) exactly (same 2655-query NaturalQuestions subset, same serialization format with question repeated before and after documents), making results directly comparable to the lost-in-the-middle paper. However, comparisons with other position-bias mitigation methods (e.g., PINE, Pos2Distill, single-dimension scaling) are not possible because those papers post-date this work or use different evaluation protocols. The SynthWiki dataset uses randomly ordered distractors (unlike NaturalQuestions which uses relevance-decreasing order), which means the two datasets test somewhat different scenarios. All results use greedy decoding; different decoding strategies may yield different relative improvements.

---

## Conclusions

### Contributions

1. **Positional attention bias causes lost-in-the-middle.** The paper establishes a direct connection between LLMs' U-shaped attention distribution over documents and the U-shaped performance curve in RAG tasks. Documents receiving higher attention are used in 74% of model responses (Table 1, Section 2.2).

2. **Additive attention decomposition.** Model attention decomposes as rel(x^doc) + bias(k) + epsilon, with 0.76 Spearman rank correlation and monotonicity conditions satisfied in 72-83% of tested pairs (Table 2, Section 3.1).

3. **Calibrated attention mechanism.** Subtracting the attention on a dummy document removes the positional bias, yielding relevance estimates that outperform query generation and relevance prompting by 5.8-10.2 Recall@3 points (Table 3, Section 3.2).

4. **Inference-time attention intervention.** Redistributing attention according to calibrated relevance yields 6-15 percentage point improvements on mid-sequence gold documents across two models, two datasets, and two context lengths (Figure 5, Table 5, Section 4.2).

5. **Complementarity with re-ordering.** Attention calibration stacks on top of existing re-ordering pipelines (LongLLMLingua-r_k, prompt reordering, attention sorting), providing a further 0.3-4.9 percentage point boost, suggesting calibration addresses a fundamentally different aspect of the problem than re-ordering (Figure 6, Table 5, Section 4.3).

6. **Training-free approach.** The method works as a pure inference-time intervention requiring no fine-tuning, additional training data, or model modifications. The only hyperparameter (temperature t = 5e-5) is robust across all tested settings (Appendix B).

### Implications

1. **Models can find relevant context in the middle.** The results challenge the view that LLMs inherently cannot use mid-sequence information. Models do attend to relevant documents even in the middle, but the positional bias masks this signal. Removing the bias reveals latent retrieval capability. [Speculative: may not hold for all model families or scales.]

2. **Attention bias as a general problem.** The U-shaped attention bias may affect tasks beyond multi-document QA, including summarization (Ravaut et al., 2023) and other long-context applications. Calibration-style interventions may be broadly applicable. [Speculative: not validated outside RAG in this paper.]

3. **Root cause investigation needed.** Understanding whether positional bias originates from pretraining data, architecture, or optimization could lead to architectural improvements that eliminate the bias at training time rather than requiring inference-time correction.

---

## Key Claims

1. **C1: U-shaped positional attention bias exists in decoder-only LLMs.** Documents at the beginning and end of the input receive higher attention weights (~0.00020) regardless of content, while mid-sequence documents receive lower weights (~0.00005). This persists after random shuffling of document order (Figure 4, Section 2.1). Scope: Vicuna-7b-v1.5-16k, K=20, NaturalQuestions. Evidence: single model, one dataset, but confirmed across both original and shuffled orderings (moderate evidence). Status: **supported**.

2. **C2: Attention-generation correlation.** 74% of incorrect predictions (526/712) incorporate content from the highest-attention half of documents, establishing a direct link between positional attention bias and the lost-in-the-middle performance degradation (Table 1, Section 2.2). Scope: Vicuna-7b-v1.5-16k, K=20, NaturalQuestions, gold doc at position 10, incorrect predictions only. Evidence: single model, single dataset, single position (limited evidence for generality). Status: **supported**.

3. **C3: Additive attention decomposition.** Model attention decomposes as relevance + positional bias + noise, validated by monotonicity conditions (83% and 72%) and 0.76 Spearman rank correlation across document-position quadruplets (Table 2, Section 3.1). Log-linear alternative achieves competitive 0.75 correlation (Table 4, Appendix C). Scope: Vicuna-7b-v1.5-16k, K=20, 100 randomly sampled NaturalQuestions examples. Evidence: single model, 100 examples (limited evidence for generality of decomposition). Status: **supported**.

4. **C4: Calibrated attention outperforms existing ranking methods.** Achieves 0.7427 and 0.6832 Recall@3 at K = 10 and K = 20, surpassing query generation (0.6851 and 0.5815) and vanilla attention (0.3638 and 0.2052) (Table 3, Section 3.2). Scope: Vicuna-7b-v1.5-16k, NaturalQuestions, gold in middle, greedy decoding. Evidence: single model, single dataset for ranking evaluation (limited evidence). Status: **supported**.

5. **C5: Attention calibration improves mid-sequence RAG accuracy by 6-15 percentage points.** Performance curves lie above vanilla baselines in 22 out of 24 position-model-dataset combinations (Figure 5, Table 5, Section 4.2). Scope: 2 models (both 7B), 2 datasets, K=10 and K=20, greedy decoding, last 16/32 layers. Evidence: tested across 2 models, 2 datasets, 2 context lengths (moderate evidence, though both models are 7B scale). Status: **supported**.

6. **C6: Calibration is complementary to re-ordering.** Applying calibration on top of LongLLMLingua-r_k yields 0.3-4.9 percentage point additional improvements across all 8 tested settings (Figure 6, Table 5, Section 4.3). Scope: same as C5. Evidence: consistent across all 8 dataset-K-model combinations (moderate evidence). Status: **supported**.

---

## Open Questions

1. **What is the root cause of positional attention bias?** The paper identifies and calibrates the bias but does not determine whether it originates from pretraining data distribution, transformer architecture, or optimization process (Section 6, Limitations). Not yet addressed.

2. **What is the optimal set of attention heads for intervention?** The paper applies calibration to all heads in the last 16 of 32 layers. Finding the best subset is left as future work, referencing Zhang et al. (2023) (Appendix B). Not yet addressed.

3. **Are there tasks where positional bias is beneficial?** Blanket removal may not always be desirable if positional bias aligns with task structure, e.g., temporal ordering (Section 6, Limitations). Not yet addressed.

4. **Can more efficient calibration methods reduce the O(K) overhead?** The current method requires one additional forward pass per document position (Section 6, Limitations). Not yet addressed.

---

## Core References and Why They Are Referenced

### Lost-in-the-Middle Problem

- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Defines and characterizes the lost-in-the-middle phenomenon with the U-shaped performance curve. This paper directly uses their experimental setup (NaturalQuestions subset, 2655 queries, same prompt serialization format) and explains the mechanistic cause of the phenomenon they documented.
- **Peysakhovich and Lerer (2023)** -- *Attention Sorting Combats Recency Bias in Long Context Language Models.* Proposes iterative attention-based document sorting as a workaround for lost-in-the-middle. Provides the SynthWiki dataset used in evaluation. Attention sorting serves as a baseline in this paper.

### Re-ranking and RAG Methods

- **Sun et al. (2023)** -- *Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents.* Provides the query generation and relevance generation baselines for document ranking (Table 3), and the prompt reordering baseline for RAG evaluation (Table 5).
- **Jiang et al. (2023)** -- *LongLLMLingua: Accelerating and Enhancing LLMs in Long Context Scenarios via Prompt Compression.* Provides the LongLLMLingua-r_k reordering baseline. This paper shows that calibration on top of LongLLMLingua-r_k yields the highest overall RAG performance.

### Attention Mechanisms and Interpretability

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational self-attention mechanism. The U-shaped positional bias is a surprising emergent property given that self-attention has no built-in position preference beyond positional embeddings.
- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Early attention analysis work. Referenced as precedent for using attention weights to understand model behavior.
- **Dong et al. (2021)** -- *On-the-Fly Attention Modulation for Neural Generation.* Precedent for modifying attention weights at inference time to influence generation behavior.
- **Zhang et al. (2023)** -- *Tell Your Model Where to Attend: Post-Hoc Attention Steering for LLMs.* Related post-hoc attention intervention method. Finding the optimal attention heads for intervention is left as future work referencing this paper.

### Evaluation Data

- **Kwiatkowski et al. (2019)** -- *Natural Questions: A Benchmark for Question Answering Research.* Source of the 2655-query evaluation set for open-domain QA experiments.
- **Izacard et al. (2022a)** -- *Unsupervised Dense Information Retrieval with Contrastive Learning (Contriever).* Retrieval system used to obtain distractor documents for NaturalQuestions.

### Models Evaluated

- **Li et al. (2023a)** -- *How Long Can Open-Source LLMs Truly Promise on Context Length?* Provides Vicuna-7b-v1.5-16k, the primary model used throughout the paper.
- **Wang et al. (2023)** -- *How Far Can Camels Go? Exploring the State of Instruction Tuning on Open Resources.* Provides Tulu-2-7b, the second model used for evaluation.

### Context and Distraction

- **Shi et al. (2023a)** -- *Large Language Models Can Be Easily Distracted by Irrelevant Context.* Establishes that LLMs are susceptible to distraction by irrelevant content. This paper refines the finding: the model's bias is positional rather than purely content-driven, persisting even after random document shuffling.
- **Ravaut et al. (2023)** -- *On Position Bias in Summarization with Large Language Models.* Shows that position bias extends to content utilization in summarization, supporting the hypothesis that positional attention bias affects downstream generation beyond QA.
