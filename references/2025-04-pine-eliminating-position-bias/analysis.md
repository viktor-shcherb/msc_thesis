---
title: "Eliminating Position Bias of Language Models: A Mechanistic Approach"
authors: "Wang, Zhang, Li, Huang, Han, Ji, Kakade, Peng, Ji"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["position-bias", "attention-analysis", "mechanistic-interpretability"]
scope: ["position bias", "causal attention", "positional encoding", "inference-time intervention", "LM-as-a-judge"]
benchmarks_used: ["rewardbench", "natural-questions", "gsm8k"]
models_introduced: []
models_evaluated: ["llama-3-8b", "llama-3-70b", "qwen1.5-7b"]
key_claims:
  - id: C1
    claim: "Position bias arises from two components: causal attention (favoring distant content) and positional encodings like RoPE (favoring nearby content)"
    evidence: "Section 3.2, Equation 1, Figure 1 lower left"
    status: supported
  - id: C2
    claim: "PINE provably eliminates inter-document position bias by replacing causal with bidirectional inter-document attention and re-assigning positions by importance scores"
    evidence: "Section 3.3, Lemma 1, Theorem 1"
    status: supported
  - id: C3
    claim: "PINE consistently provides 8-10 percentage point gains on RewardBench reasoning subset, making Llama-3-70B-Instruct (87.6%) outperform GPT-4-0125-preview (86.9%)"
    evidence: "Table 1, Section 4.2"
    status: supported
  - id: C4
    claim: "Position bias affects up to 48% of data points for smaller models and persists above 10% even for 110B-parameter models"
    evidence: "Table 4, Appendix C"
    status: supported
  - id: C5
    claim: "Masking inter-document attention (PCW, NIA, SP) is substantially worse than bidirectional inter-document attention (PINE) because it loses contextual information"
    evidence: "Table 2, Section 4.2"
    status: supported
  - id: C6
    claim: "Placing more important documents closer to the query (aligning with RoPE's recency bias) outperforms reverse placement"
    evidence: "Figure 4b, Section 4.3"
    status: supported
  - id: C7
    claim: "PINE's computational overhead is approximately 2x for k=2 documents and 8x for k=20 documents"
    evidence: "Section 3.4"
    status: supported
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: extends
    detail: "Uses Liu et al.'s experimental setup and directly addresses the U-shaped position bias phenomenon they documented"
  - target: 2024-08-found-in-the-middle
    type: complementary
    detail: "Both address position bias at inference time; Hsieh et al. use attention calibration while PINE uses bidirectional attention and importance-based position re-assignment"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "PINE's mechanistic analysis identifies RoPE's recency bias as one of two causes of position bias and designs position re-assignment to align with it"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Wu et al. provide theoretical characterization of how position bias emerges from causal masking and PE; PINE provides a practical inference-time solution based on similar mechanistic insights"
  - target: 2025-11-pos2distill-position-bias-distillation
    type: complementary
    detail: "Both address position bias mitigation; Pos2Distill uses training-based self-distillation while PINE uses training-free inference-time attention modification"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Modifies the Transformer's causal attention mechanism to enable bidirectional inter-document attention"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi introduces a linear distance penalty creating recency bias; PINE's analysis identifies such PE-induced bias as one cause of position bias"
open_questions:
  - question: "Can PINE's computational overhead (2-8x) be reduced through optimized implementations that eliminate the for-loop over documents?"
    addressed_by: null
  - question: "Does PINE's bidirectional inter-document attention cause instruction-following degradation in tasks beyond LM-as-a-judge?"
    addressed_by: null
  - question: "Can PINE be extended to eliminate position bias in vision-language models, where spatial position bias has been demonstrated?"
    addressed_by: null
  - question: "How does PINE perform with more than 20 documents, given the slight accuracy degradation observed at k=20?"
    addressed_by: null
---
# Eliminating Position Bias of Language Models: A Mechanistic Approach

**Authors:** Ziqi Wang, Hanlin Zhang, Xiner Li, Kuan-Hao Huang, Chi Han, Shuiwang Ji, Sham M. Kakade, Hao Peng, Heng Ji (University of Illinois Urbana-Champaign, Harvard University, Texas A&M University)
**Date:** April 2025, ICLR 2025 (arXiv:2407.01100)

---

## Core Research Problem

Position bias is a prevalent issue in modern language models where models prioritize content based on its position within the context rather than its relevance or quality. This bias manifests across diverse tasks: LM-as-a-judge systems exhibit primacy bias, favoring the response presented first (Zheng et al., 2024b); retrieval-augmented QA shows a U-shaped performance curve where accuracy is best when the gold document is at the beginning or end and worst in the middle (Liu et al., 2024); multiple-choice QA models favor options at certain positions (Zheng et al., 2024a); and vision-language models perform better when target content is at certain spatial positions (Figure 1, Appendix A).

Prior approaches to position bias fall into two categories. **Mitigation** methods reduce but do not eliminate the bias: data augmentation with training (Junqing et al., 2023; Zhu et al., 2023), content sorting by attention value (Peysakhovich & Lerer, 2023), calibration (Hsieh et al., 2024), and removing positional encoding (Kazemnejad et al., 2024). **Elimination** methods aim to fully remove the bias but face severe limitations: permutation-then-average has O(k!) computational overhead (Zheng et al., 2024a;b); Parallel Context Windows (PCW) masks all inter-document attention, losing contextual information and confusing models with identical positions for different tokens (Ratner et al., 2023); and calibration-based approaches assume uniform token distributions, producing incoherent outputs in generation tasks (Zhao et al., 2021).

**The core challenge is: how to provably eliminate inter-document position bias in language models at inference time, without training, without combinatorial search, and without sacrificing contextual information between documents.**

---

## Problem Solutions

The paper introduces **Position-INvariant inferencE (PINE)**, a training-free zero-shot method that provably eliminates inter-document position bias.

1. **Mechanistic root-cause analysis.** The authors attribute position bias to exactly two components in the attention computation: the causal attention mask (which favors distant/earlier content) and positional encodings like RoPE (which favor nearby/recent content). These two biases act in opposing directions (Section 3.2, Figure 1 lower left).
2. **Bidirectional inter-document attention.** PINE replaces the causal attention mask with bidirectional attention between documents while preserving causal attention within each document, maintaining information flow between all documents without losing contextual information.
3. **Importance-based position re-assignment.** PINE computes position-free importance scores between documents and assigns key positions so that more important documents are placed closer to the query, aligning with RoPE's inherent recency bias.

---

## Approach Details

### Method

The standard Transformer attention computation (Section 3.2, Equation 1) is:

> Q_PE = PE(Q, pos_Q), K_PE = PE(K, pos_K)
>
> H = Softmax(Q_PE * K_PE^T / sqrt(d)) * 1_causal * V

where PE denotes the positional encoding function, pos_Q and pos_K are position indices, 1_causal is the causal mask, and d is the hidden dimension. The authors identify two sources of position bias from this equation:

1. **Positional encoding (PE):** Changes document positions produce different Q_PE and K_PE representations, altering attention scores. RoPE specifically exhibits recency bias -- attention weight decays with increasing relative distance (Su et al., 2024).
2. **Causal attention mask (1_causal):** Enforces unidirectional information flow. Later tokens can attend to all earlier tokens, but earlier tokens cannot attend to later ones. This asymmetry generally favors content that appears earlier in the sequence (distant from the generation point).

PINE modifies both components to produce a position-invariant hidden state H_PINE.

### Key Technical Components

**Bidirectional inter-document attention (Component 1).** The causal mask is relaxed so that tokens in different documents can attend to each other bidirectionally. Intra-document attention remains causal to preserve token order within each document. Making intra-document attention bidirectional would degenerate models into bag-of-words models (Section 3.3, Figure 2 middle).

**Importance-based position re-assignment (Component 2).** Positions are re-assigned in three steps:

*Step 1 -- Token-level importance without PE:*

> Importance_token(i, j) = Softmax(q_i * k_j^T / sqrt(d))

where Q, K have **not** been applied to positional encoding.

*Step 2 -- Document-level importance by averaging:*

> Importance(D_i, D_j) = sum_{m in D_i, n in D_j} Importance_token(m, n) / |D_j|

The length normalization (dividing by |D_j|) prevents assigning higher importance to longer documents. Summation without normalization converts position bias to length bias; using maximum instead of averaging yields worse performance due to noise from unimportant tokens (footnote 3).

*Step 3 -- Position assignment:* Documents are sorted by importance -- more important documents are placed at closer positions to the query when serving as keys.

**Query position assignment.** Since LMs are trained causally, each document is treated as the **last** document when serving as queries. This means a query token's position is always larger than the key tokens', consistent with training (Section 3.3, Figure 2 right).

**Key position varies by query.** Unlike vanilla inference where each token has a fixed position as a key regardless of the query, in PINE the key position of a document depends on which document is the query (based on importance ranking). This is visible in Figure 2 where column values differ across rows.

### Theoretical Analysis

**Lemma 1:** If the input Q, K, V are inter-document position-invariant representations, then H_PINE are also inter-document position-invariant representations.

The proof proceeds by showing that (1) SYS tokens are unaffected by PINE; (2) for each document D_i, the importance score Importance(D_i, D_j) uses Q, K without positional encoding, so it is not a function of input document positions; (3) after sorting by importance, positional encoding is applied deterministically based on the importance ranking, not the original positions (Section 3.3).

**Theorem 1:** Given an input, if H_PINE is applied to every layer, attention head, and token, then the model outputs are inter-document position-invariant representations.

Proved by mathematical induction: the embedding layer is not position-dependent; by Lemma 1, attention hidden states at each layer are position-invariant; FFN, QKV projection, and layer normalization are element-wise operations that preserve position invariance (Appendix B).

Both bidirectional attention **and** position re-assignment are required for the proof. PINE must be applied to every layer, every attention head, and every token. The method is not limited to RoPE -- it works with any positional encoding (Section 3.3).

**Inference cost.** Extra big-O complexity is O(nk log k), where n is the text length and k is the number of documents. Bidirectional attention adds no extra cost; position re-assignment adds O(k log k) per token for sorting. In practice, wall time is approximately 2x for LM-as-a-judge (k=2) and approximately 8x for retrieval-augmented QA with 20 documents (k=20). Memory overhead is small -- 70B models run on 3x A100 80G, same as vanilla inference (Section 3.4).

### Comparison with Parallel Context Windows (PCW)

PCW (Ratner et al., 2023) differs from PINE in two ways (Figure 3): (1) PCW **masks all** inter-document attention instead of making it bidirectional, losing contextual information; (2) PCW assigns all documents the **same** positions, confusing models. PCW performs poorly in language generation tasks as a result (Table 2).

### Experimental Setup

**LM-as-a-judge (Section 4.2).** Benchmark: RewardBench (Lambert et al., 2024b), 23 datasets across four subsets (Chat, Chat-Hard, Safety, Reasoning). Models: Llama-3-Instruct (8B, 70B), Qwen-1.5-Chat (1.8B, 4B, 7B, 32B, 72B, 110B), Qwen-2.5-Instruct (72B). Temperature: 0. Position conditions: ground-truth at position A, at position B, shuffled, and PINE.

**Retrieval-augmented QA (Section 4.3).** Follows Liu et al. (2024) setup, prompts, data, and evaluation scripts. NaturalQuestions data with 10 or 20 retrieved documents, one containing the correct answer. Model: Llama-3-70B-Instruct.

**Molecule generation (Section 4.4).** Dataset: QM9 (Ramakrishnan et al., 2014), 130k+ molecules with six quantum properties (alpha, epsilon_HOMO, epsilon_LUMO, Delta_epsilon, mu, Cv). Custom 8-layer Llama model (8 heads, 768 hidden dimensions). Evaluation: 10,000 sampled 6-property conditions with randomized property order; MAE between target and predicted property values.

**Math reasoning (Section 4.4).** Dataset: R-GSM (Chen et al., 2024a), a subset of GSM8K with interchangeable premises, further cleaned to 95 problems. Models: Qwen-1.5-Chat (7B, 110B). Prompts from OpenAI/simple-evals.

**Baselines.** NIA (no inter-document attention, keeps RoPE), PCW (Ratner et al., 2023), SP (Structured Prompting, Hao et al., 2022), Permutation (Zheng et al., 2024a), Calibration (Zhao et al., 2021).

### Key Results

**RewardBench -- Reasoning subset (Table 1):**

| Model | Vanilla (Shuffle) | PINE | Gain |
|---|---|---|---|
| Llama-3-8B-Instruct | 65.3 | **73.4** | +8.1 |
| Llama-3-70B-Instruct | 78.9 | **87.6** | +8.7 |
| Qwen-1.5-1.8B-Chat | 48.4 | **60.1** | +11.7 |
| Qwen-1.5-4B-Chat | 54.1 | **61.0** | +6.9 |
| Qwen-1.5-7B-Chat | 59.3 | **63.0** | +3.7 |
| Qwen-1.5-32B-Chat | 66.8 | **76.7** | +9.9 |
| Qwen-1.5-110B-Chat | 78.0 | **86.2** | +8.2 |
| Qwen-2.5-72B-Instruct | 85.5 | **91.3** | +5.8 |

- PINE moves Llama-3-70B-Instruct from 22nd to 7th rank among generative models on RewardBench, outperforming GPT-4-0125-preview (86.9%), GPT-4o-2024-08-06 (86.6%), and Llama-3.1-405B-Instruct-Turbo (87.1%) on the reasoning subset.
- The one exception is Qwen-1.5-72B-Chat, which shows a slight decrease (-1.1 on the full set); the authors attribute this to the model being poorly trained, noting Qwen 2 reports 72B performing worse than 32B in reasoning.

**RewardBench -- Full set (Table 1):**

| Model | Vanilla (Shuffle) | PINE | Gain |
|---|---|---|---|
| Llama-3-8B-Instruct | 64.8 | **66.7** | +1.9 |
| Llama-3-70B-Instruct | 76.0 | **77.4** | +1.4 |
| Qwen-1.5-7B-Chat | 60.9 | **61.5** | +0.6 |
| Qwen-1.5-110B-Chat | 81.1 | **82.9** | +1.7 |

- Full-set gains are more modest because the Chat and Safety subsets have less position bias and PINE can cause instruction-following degradation on these subsets.

**Baseline comparison (Table 2, Llama-3-8B-Instruct):**

| Method | Reasoning | Full |
|---|---|---|
| NIA | 55.9 | 61.9 |
| PCW | 56.5 | 61.7 |
| SP | 55.4 | 60.8 |
| Permutation | 69.0 | 65.9 |
| **PINE** | **73.4** | **66.7** |

- PINE outperforms the best baseline (Permutation) by 4.4 percentage points on reasoning and 0.8 on the full set.
- Calibration (Zhao et al., 2021) generates incoherent outputs in open-ended generation and is not applicable.

**Retrieval-augmented QA (Figure 4a, Llama-3-70B-Instruct):**

- With 10 documents: PINE is slightly better than vanilla on average (+1.2 accuracy).
- With 20 documents: PINE is slightly worse than vanilla on average (-2.0 accuracy).
- PINE is position-invariant, avoiding worst-case performance dips seen in vanilla inference. All baselines (NIA, PCW, SP) are substantially worse than PINE.

**Molecule generation on QM9 (Table 3, MAE, lower is better):**

| Metric | Vanilla | PINE |
|---|---|---|
| alpha | 6.3997 | **6.3702** |
| epsilon_HOMO | 103.93 | **102.15** |
| epsilon_LUMO | 53.40 | **53.09** |
| Delta_epsilon | 99.13 | **98.27** |
| mu | **3.4112** | 3.4917 |
| Cv | 4.3785 | **4.2886** |

- PINE improves 5 out of 6 quantum property predictions. The only metric where vanilla is better is dipole moment (mu).

**Math reasoning on R-GSM (Figure 5):**

- Qwen-1.5-7B-Chat: PINE improves accuracy by +12.6% over vanilla.
- Qwen-1.5-110B-Chat: PINE improves accuracy by +5.3% over vanilla.

### Position Re-Assignment Ablation

Three variants compared on retrieval-augmented QA with 10 documents (Figure 4b):

1. **PINE (default, closer = more important):** Best average performance.
2. **PINE without position re-assignment:** Slightly worse (-0.3 with 10 docs, -1.5 with 20 docs). Still eliminates attention mask bias but not PE bias.
3. **PINE with reverse re-assignment (farther = more important):** Worst of the three. Conflicts with RoPE's recency bias.

### Position Bias Prevalence

Position bias can affect up to **48.0%** of data points (Qwen-1.5-4B-Chat on Chat). The Reasoning subset consistently shows high bias: 27.6% for Llama-3-8B, 15.2% for Llama-3-70B, 23.5-26.5% for Qwen-1.5-7B through 110B (Table 4, Appendix C). Larger models generally have less position bias but it persists above 10% on average even at 110B scale.

### Per-Dataset Highlights

PINE substantially improves code evaluation benchmarks on RewardBench: Llama-3-8B HumanEval pass rates increase from 73.5-79.0 to 81.4-86.6 across languages (cpp, go, java, js, python, rust). Math-prm jumps from 66.4 to 80.5 for Llama-3-70B and from 74.5 to 84.8 for Qwen-2.5-72B (Tables 7-15, Appendix D).

---

## Limitations and Failure Modes

1. **Computational overhead.** PINE requires approximately 2x wall time for k=2 documents (LM-as-a-judge) and approximately 8x for k=20 documents (retrieval-augmented QA). The current implementation contains a for-loop over documents and has not been optimized (Section 3.4, Section 5).
2. **Instruction-following degradation.** PINE sometimes causes LLMs to solve the user's question directly instead of comparing two responses, or to fail to output answers in the requested format (e.g., "[[A]]" or "[[B]]"), causing parsing failures (Appendix D).
3. **Safety over-helpfulness.** Under PINE, LMs sometimes overly focus on helpfulness in safety-critical prompts, leading to performance drops on the RewardBench Safety subset (Appendix D).
4. **Degradation with many documents.** With 20 documents in retrieval-augmented QA, PINE is slightly worse than vanilla on average (-2.0 accuracy), suggesting importance score computation accuracy degrades with more documents (Section 4.3).
5. **Adversarial subset sensitivity.** On specific RewardBench adversarial subsets (llmbar-adver-manual, llmbar-adver-neighbor), PINE sometimes underperforms vanilla -- e.g., Llama-3-70B manual: 53.3 to 47.8 (Appendix D).
6. **Model-specific exceptions.** Qwen-1.5-72B-Chat shows a slight overall decrease (-1.1) with PINE; the authors attribute this to the model being poorly trained (Section 4.2).

---

## Conclusions

### Contributions

1. **Mechanistic root-cause identification.** Attributes position bias to exactly two architectural components: causal attention (favoring distant content) and positional encodings like RoPE (favoring nearby content), with the two biases acting in opposing directions (Section 3.2).

2. **Provably position-invariant inference.** Introduces PINE, a training-free zero-shot method that provably eliminates inter-document position bias via bidirectional inter-document attention and importance-based position re-assignment, with formal guarantees (Lemma 1, Theorem 1).

3. **Large gains on reasoning evaluation.** PINE consistently provides 8-10 percentage point improvements on the RewardBench reasoning subset, making Llama-3-70B-Instruct outperform GPT-4-0125-preview and GPT-4o on this benchmark (Table 1).

4. **Broad applicability.** Demonstrates position bias elimination across four distinct tasks: LM-as-a-judge, retrieval-augmented QA, molecule generation, and math reasoning, establishing position bias as a general phenomenon addressable by a single method (Sections 4.2-4.4).

5. **Bidirectional attention superiority.** Establishes that bidirectional inter-document attention is substantially superior to masking inter-document attention (PCW, NIA, SP) for position bias elimination, resolving the design choice in favor of preserving inter-document context (Table 2).

### Implications

1. **Position bias as a universal architectural limitation.** The mechanistic analysis implies that position bias is an inherent property of any causal Transformer with relative positional encodings, not a training data artifact. This suggests all such models would benefit from position-invariant inference when documents are order-agnostic (speculative for models not tested).

2. **Importance-based ordering as a general principle.** The finding that aligning position assignment with importance scores (closer = more important) respects RoPE's recency bias suggests a general design principle for inference-time interventions on RoPE-based models (Section 4.3).

3. **VLM position bias.** The demonstration that vision-language models exhibit spatial position bias (Figure 1, Appendix A) suggests PINE-like methods may be needed for multimodal models, though this is not experimentally validated.

---

## Key Claims

**C1. Position bias has two opposing mechanistic causes.** Causal attention favors distant (earlier) content because later tokens can attend to all earlier tokens but not vice versa. RoPE favors nearby (recent) content through attention decay with increasing relative distance. These opposing biases combine to produce the observed position-dependent performance (Section 3.2, Equation 1, Figure 1 lower left). Status: **supported**.

**C2. PINE provably eliminates inter-document position bias.** By replacing causal inter-document attention with bidirectional attention and re-assigning positions based on importance scores, PINE produces outputs that are mathematically invariant to document ordering. Both components are necessary for the proof (Section 3.3, Lemma 1, Theorem 1, Appendix B). Status: **supported**.

**C3. 8-10 percentage point gains on reasoning evaluation.** PINE consistently provides 8-10 percentage point improvements on the RewardBench reasoning subset across most models tested. Llama-3-70B-Instruct achieves 87.6% with PINE, outperforming GPT-4-0125-preview (86.9%) and GPT-4o-2024-08-06 (86.6%) (Table 1, Section 4.2). Status: **supported**.

**C4. Position bias prevalence at scale.** Position bias affects up to 48.0% of data points for smaller models (Qwen-1.5-4B-Chat on Chat) and persists above 10% on average for 110B-parameter models. The Reasoning subset is consistently the most affected, with 23.5-27.6% of data points showing bias (Table 4, Appendix C). Status: **supported**.

**C5. Bidirectional attention outperforms masked attention.** On Llama-3-8B-Instruct RewardBench reasoning, PINE (73.4%) outperforms PCW (56.5%), SP (55.4%), and NIA (55.9%) by 16.9+ percentage points. Masking inter-document attention loses contextual information critical for generation tasks (Table 2, Section 4.2). Status: **supported**.

**C6. Importance-aligned position re-assignment is optimal.** Placing more important documents closer to the query (+0.3 over no re-assignment with 10 docs, +1.5 with 20 docs) outperforms both no re-assignment and reverse re-assignment. This aligns with RoPE's inherent recency bias (Figure 4b, Section 4.3). Status: **supported**.

**C7. Computational overhead scales with document count.** PINE's extra cost is O(nk log k) in theory, translating to approximately 2x wall time for k=2 and approximately 8x for k=20 in practice. Memory overhead is small (Section 3.4). Status: **supported**.

---

## Open Questions

1. **Can PINE's computational overhead be reduced?** The current implementation uses a for-loop over documents. Parallelized or batched implementations could potentially reduce the 2-8x overhead, but this is not explored.

2. **Does bidirectional inter-document attention degrade instruction following in general?** PINE causes instruction-following failures on some RewardBench subsets (models solving the question instead of comparing responses). Whether this extends to other instruction-following tasks is unknown.

3. **Can PINE handle vision-language position bias?** The paper demonstrates spatial position bias in VLMs (Figure 1, Appendix A) but does not test PINE on multimodal models. Extending PINE to visual tokens would require defining "documents" in the image domain.

4. **How does PINE scale beyond 20 documents?** PINE shows a slight accuracy drop with 20 documents (-2.0 vs. vanilla on average) compared to gains with 10 documents (+1.2). Whether this degradation continues at 50 or 100 documents is untested.

---

## Core References and Why They Are Referenced

### Position Bias Identification

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Documents the U-shaped position bias in retrieval-augmented QA. PINE uses their experimental setup, prompts, data, and evaluation scripts for the retrieval-augmented QA experiments.
- **Zheng et al. (2024b)** -- *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* Documents primacy bias in LM-as-a-judge evaluations. Motivates the LM-as-a-judge experiments and provides the permutation baseline.
- **Zheng et al. (2024a)** -- *Large Language Models Are Not Robust Multiple Choice Selectors.* Documents position bias in multiple-choice QA and proposes the permutation-then-average elimination method with O(k!) cost.
- **Hsieh et al. (2024)** -- *Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization.* Proposes inference-time attention calibration as an alternative approach to position bias mitigation.
- **Chen et al. (2024b)** -- *Premise Order Matters in Reasoning with Large Language Models.* Documents position bias in math reasoning; introduces the R-GSM dataset used for evaluation.

### Position Encoding and Attention Mechanism

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, whose recency bias is identified as one of two causes of position bias.
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture with causal attention, identified as the other cause of position bias.
- **Peysakhovich & Lerer (2023)** -- *Attention Sorting Combats Recency Bias in Long Context Language Models.* Proposes attention-based document sorting to mitigate recency bias. PINE builds on the idea of using attention values for document ordering but provides formal guarantees.

### Mechanical Approaches to Position Bias (Baselines)

- **Ratner et al. (2023)** -- *Parallel Context Windows for Large Language Models.* Introduces PCW, which masks inter-document attention and assigns identical positions. Used as the primary mechanical baseline; PINE's bidirectional attention is shown to be substantially superior.
- **Hao et al. (2022)** -- *Structured Prompting: Scaling In-Context Learning to 1,000 Examples.* Variant of PCW that lowers attention between decoded tokens and input documents. Used as the SP baseline.
- **Zhao et al. (2021)** -- *Calibrate Before Use: Improving Few-Shot Performance of Language Models.* Proposes calibration-based debiasing. Shown to fail in open-ended generation tasks.

### Evaluation Benchmarks

- **Lambert et al. (2024a;b)** -- *RewardBench.* Primary evaluation benchmark for LM-as-a-judge experiments, comprising 23 datasets across Chat, Chat-Hard, Safety, and Reasoning subsets.
- **Ramakrishnan et al. (2014)** -- *QM9 Dataset.* Quantum chemistry dataset for molecule generation experiments, containing 130k+ molecules with DFT-calculated properties.

### Models Used in Evaluation

- **Meta AI (2024)** -- *Llama 3.* Primary experimental models (8B, 70B Instruct variants) used across LM-as-a-judge and retrieval-augmented QA.
- **Bai et al. (2023)** -- *Qwen Technical Report.* Qwen-1.5 model family (1.8B through 110B) used for LM-as-a-judge breadth evaluation and math reasoning.
