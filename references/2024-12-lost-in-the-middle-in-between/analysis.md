---
title: "Lost in the Middle, and In-Between: Enhancing Language Models' Ability to Reason Over Long Contexts in Multi-Hop QA"
authors: "Baker, Raut, Shaier, Hunter, von der Wense"
year: 2024
venue: "arXiv 2024"
paper_type: preprint
categories: ["position-bias", "long-context-evaluation", "reasoning-evaluation"]
scope: ["multi-hop QA positional bias", "inter-document distance effects", "chain-of-thought prompting for position bias", "context reduction for position bias"]
benchmarks_used: ["hotpotqa", "2wikimultihopqa", "musique"]
models_introduced: []
models_evaluated: ["gpt-3.5-turbo", "mpt-7b", "llama-2-7b"]
key_claims:
  - id: C1
    claim: "In multi-hop QA, performance degrades not only with respect to the absolute position of evidence documents but also with respect to the relative distance between them: adjacent evidence documents yield higher accuracy than separated ones across datasets and models"
    evidence: "Figure 4, Section 6, Tables 3-5"
    status: supported
  - id: C2
    claim: "Chain-of-thought prompting improves multi-hop QA performance for instruction-tuned models (MPT-7b-instruct, GPT-3.5-Turbo) but causes sharp performance decline for non-instruction-tuned models (Llama-2-7b-longlora)"
    evidence: "Figures 2-3, Section 6, Tables 3-5"
    status: supported
  - id: C3
    claim: "Context reduction via summarization or knowledge graph triple extraction flattens positional bias curves but reduces overall accuracy, particularly for instruction-tuned models"
    evidence: "Figure 2, Section 6, Table 2, Tables 3-5"
    status: supported
  - id: C4
    claim: "Llama-2-7b-longlora exhibits strong primacy bias with little to no recency bias, and CoT prompting exacerbates this by causing over-reliance on few-shot exemplars"
    evidence: "Figure 3, Section 6, Table 5"
    status: supported
  - id: C5
    claim: "Existing out-of-the-box context reduction methods are insufficient to fully mitigate the lost-in-the-middle problem in multi-hop settings, as they often produce reasoning chains too fragile for effective multi-hop QA"
    evidence: "Section 8, Tables 3-5"
    status: supported
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: extends
    detail: "Directly extends Liu et al.'s lost-in-the-middle analysis from single-hop to multi-hop QA, adopting the same 20-document setup and best-subspan accuracy metric, and adding the inter-document distance dimension"
  - target: 2024-08-found-in-the-middle
    type: complementary
    detail: "Found in the Middle identifies positional attention bias as the mechanism behind the U-shaped curve; this paper shows the problem persists and compounds in multi-hop settings where multiple evidence documents must be integrated"
  - target: 2022-04-alibi-train-short-test-long
    type: evaluates
    detail: "Evaluates MPT-7b-8k-instruct, which uses ALiBi positional encoding, finding it exhibits the same positional biases in multi-hop QA"
  - target: 2022-12-chain-of-thought-prompting
    type: complementary
    detail: "Tests chain-of-thought prompting as a mitigation strategy for positional bias, finding it helps instruction-tuned models but harms non-instruction-tuned ones"
  - target: 2023-07-gsm-ic-irrelevant-context
    type: complementary
    detail: "Both papers study how LLMs handle context with irrelevant information; GSM-IC focuses on distractor content in reasoning, while this paper focuses on positional effects of relevant documents in multi-hop QA"
  - target: 2025-07-nolima-long-context-evaluation
    type: complementary
    detail: "NoLiMa confirms that in two-hop scenarios without literal cues, context length dominates over position; this paper provides complementary evidence that inter-document distance is an additional factor in multi-hop degradation"
open_questions:
  - question: "How do newer, larger models (GPT-4, Llama 3, Gemini) perform on the same multi-hop positional bias experiments?"
    addressed_by: null
  - question: "Can tailored preprocessing methods that preserve multi-hop reasoning paths mitigate positional bias without the accuracy loss of generic summarization or KG extraction?"
    addressed_by: null
  - question: "What is the interaction between the number of reasoning hops and the severity of positional bias — does the effect scale linearly or combinatorially with hop count?"
    addressed_by: null
  - question: "Can dynamic chain-of-thought or advanced prompting techniques help non-instruction-tuned models overcome their primacy bias in multi-hop QA?"
    addressed_by: null
---
# Lost in the Middle, and In-Between: Enhancing Language Models' Ability to Reason Over Long Contexts in Multi-Hop QA

**Authors:** George Arthur Baker, Ankush Raut, Sagi Shaier, Lawrence E Hunter, Katharina von der Wense (University of Colorado Boulder, University of Chicago Department of Pediatrics, Johannes Gutenberg University Mainz)
**Date:** December 2024, arXiv:2412.10079

---

## Core Research Problem

The "lost in the middle" phenomenon, first identified by Liu et al. (2024), shows that language models exhibit a U-shaped performance curve when relevant information is placed at different positions in the input context — performance is highest at the beginning and end, and degrades in the middle. However, prior work has only studied this problem in **single-hop** settings, where a single piece of critical information (one gold document) must be located among distractors.

In multi-hop question answering (MHQA), models must reason over **multiple** evidence documents spread across the input context to arrive at an answer. This setting introduces an additional dimension to positional bias: not only the absolute positions of evidence documents matter, but also their **relative distance** from each other. Existing mitigation strategies — document re-ranking (Peysakhovich and Lerer, 2023; Tang et al., 2023), summarization (Kim et al., 2024), and extended-context training (An et al., 2024) — face fundamental scalability limitations in multi-hop settings because the number of possible document orderings grows combinatorially with the number of reasoning steps.

**The core challenge is: characterizing how both the absolute position and the relative distance between multiple evidence documents affect multi-hop QA performance, and whether existing mitigation strategies (CoT prompting, context reduction) can address the compounded positional bias.**

---

## Problem Solutions

The paper provides an **empirical characterization** of the lost-in-the-middle problem in multi-hop QA and evaluates potential mitigations. The key findings are:

1. **Inter-document distance matters.** Performance degrades not only when evidence is in the middle of the context, but also when evidence documents are separated by distractors rather than placed adjacently.
2. **CoT helps instruction-tuned models only.** Chain-of-thought prompting improves performance for instruction-tuned models (MPT-7b-instruct, GPT-3.5-Turbo) but causes sharp declines for non-instruction-tuned models (Llama-2-7b-longlora) due to primacy bias and over-reliance on exemplars.
3. **Context reduction is a double-edged sword.** Summarization and KG triple extraction flatten positional bias curves but reduce overall accuracy, as information loss during reduction breaks fragile multi-hop reasoning chains.

---

## Approach Details

### Method

This is an empirical study using controlled manipulation of evidence document positions within 20-document contexts across three multi-hop QA datasets. For each question, evidence documents are placed at specific ordinal positions among distractor documents, and model accuracy is measured as a function of position configuration.

### Key Technical Components

**Datasets:**

| Dataset | Hops | Questions |
|---|---|---|
| HotpotQA | 2 | 3,703 |
| 2WikiMultihopQA | 2, 4 | 6,288 |
| MuSiQue-Ans | 2, 3, 4 | 1,209 |

The second half of each validation set is used as the test set (official test sets are private). For 2WikiMultihopQA, which contains only 10 documents per question, an additional 10 distractor documents are retrieved using a Contriever setup following Liu et al. (2024) (Table 1, footnote 1).

**Position configurations tested (all within 20 total documents):**

- **2-hop adjacent:** (1,2), (5,6), (10,11), (15,16), (19,20)
- **2-hop separated:** (1,5), (5,10), (10,15), (15,20)
- **3-hop adjacent:** (1,2,3), (5,6,7), (10,11,12), (15,16,17), (18,19,20)
- **3-hop separated:** (1,5,10), (5,10,15), (10,15,20)
- **4-hop adjacent:** (1,2,3,4), (5,6,7,8), (10,11,12,13), (15,16,17,18), (17,18,19,20)
- **4-hop separated:** (1,3,5,7), (5,7,9,11), (10,12,14,16), (14,16,18,20)

The total possible position combinations are C(20,2) = 190 for 2-hop, C(20,3) = 1,140 for 3-hop, and C(20,4) = 4,845 for 4-hop, making exhaustive evaluation computationally prohibitive (Section 4).

**Context reduction methods:**

1. **Knowledge graph triple extraction:** LLaMA 2 7B (Touvron et al., 2023) prompted to extract factual triples from each document independently.
2. **Summarization:** BART-large-CNN (Lewis et al., 2019), fine-tuned on CNN/Daily Mail, with maximum generation length of 50 tokens per document.

Average document word counts (Table 2):

| Dataset | Full | Summarized | KG |
|---|---|---|---|
| HotpotQA | 69 | 29 | 33 |
| 2WikiMultihopQA | 45 | 21 | 29 |
| MuSiQue-Ans | 85 | 32 | 35 |

**Evaluation metric:** Best-subspan accuracy — score of 1 if the model's output contains any annotated answer (or alternative answers for MuSiQue), 0 otherwise (Section 3.1.2).

**Generation parameters:** Temperature 0, maximum 256 tokens (Section 4).

### Experimental Setup

**Models evaluated:**

| Model | Type | Context | Notes |
|---|---|---|---|
| MPT-7b-8k-instruct | Open, instruction-tuned | 8K tokens | ALiBi positional encoding |
| Llama-2-7b-longlora-8k-ft | Open, non-instruction-tuned | 8K tokens | LongLoRA fine-tuning (Chen et al., 2023) |
| GPT-3.5-turbo-1106 | Closed | 16K tokens | Reproducible outputs |

Closed-book baselines (no documents provided):

| Dataset | GPT-3.5 | MPT-7b | Llama-2-longlora |
|---|---|---|---|
| HotpotQA | 40.64% | 14.88% | 12.21% |
| MuSiQue-Ans | 14.39% | 3.64% | 0.74% |
| 2WikiMultihopQA | 44.99% | 20.13% | 31.65% |

### Key Results

**GPT-3.5-turbo-1106 — HotpotQA 2-hop (Table 3):**

| Condition | (1,2) | (10,11) | (19,20) | (1,5) | (10,15) |
|---|---|---|---|---|---|
| Standard | 76.72% | 71.40% | 73.89% | 73.75% | 70.16% |
| Standard + CoT | 79.26% | 75.10% | 76.64% | 77.48% | 71.78% |
| KG | 56.09% | 53.61% | 57.52% | 56.12% | 52.01% |
| KG + CoT | 34.94% | 29.57% | 31.14% | 31.60% | 28.54% |
| Summaries | 60.11% | 58.30% | 60.73% | 59.90% | 56.36% |
| Summaries + CoT | 60.63% | 58.84% | 61.92% | 61.27% | 57.41% |

- Standard prompting shows a ~5 percentage point drop from edge positions to middle (76.72% at (1,2) vs. 71.40% at (10,11)).
- CoT improves performance across all positions by 2-4 percentage points.
- KG extraction drastically reduces accuracy (76.72% -> 56.09%) while flattening the positional curve.
- KG + CoT produces the worst overall results (34.94% at best), suggesting CoT reasoning on impoverished KG context is counterproductive.

**GPT-3.5-turbo-1106 — MuSiQue-Ans 2-hop (Table 3):**

| Condition | (1,2) | (10,11) | (19,20) | (5,10) | (10,15) |
|---|---|---|---|---|---|
| Standard | 56.23% | 41.21% | 52.72% | 40.89% | 38.18% |
| Standard + CoT | 58.47% | 44.25% | 53.83% | 48.08% | 44.25% |

- The U-shaped curve is more pronounced: 15 percentage point drop from (1,2) to (10,11).
- Separated positions show even lower accuracy: (10,15) at 38.18% vs. (10,11) at 41.21%.

**GPT-3.5-turbo-1106 — 2WikiMultihopQA 4-hop (Table 3):**

| Condition | (1,2,3,4) | (10,11,12,13) | (17,18,19,20) | (10,12,14,16) |
|---|---|---|---|---|
| Standard | 91.29% | 90.12% | 89.60% | 89.24% |
| Standard + CoT | 93.27% | 93.70% | 93.12% | 92.31% |
| Summaries + CoT | 94.80% | 93.41% | 92.83% | 93.41% |

- Performance is high across all configurations, with smaller positional effects (~2 percentage points).
- CoT provides consistent improvement of ~2-3 percentage points.

**Llama-2-7b-longlora — catastrophic failures (Table 5):**

| Dataset | Condition | Best | Worst |
|---|---|---|---|
| HotpotQA | Standard | 3.11% (1,2) | 0.70% (10,15) |
| HotpotQA | KG | 25.76% (1,2) | 7.56% (15,20) |
| HotpotQA | CoT | 0.59% (1,2) | 0.46% (all mid) |
| MuSiQue 3-hop | Standard | 0.00% (all) | 0.00% (all) |
| MuSiQue 4-hop | All conditions | 0.00% (all) | 0.00% (all) |
| 2Wiki 4-hop | Standard | 30.75% (1,2,3,4) | 3.73% (14,16,18,20) |

- **Pronounced primacy bias:** Performance drops sharply from position (1,2) to all other positions.
- **CoT is destructive:** On HotpotQA, standard prompting yields 3.11% at (1,2), while CoT drops to 0.59%. On 2Wiki 4-hop standard, 30.75% at (1,2,3,4) drops to 0.51% with CoT.
- **KG extraction helps more than full documents:** On HotpotQA, KG yields 25.76% at (1,2) vs. 3.11% for standard — context reduction benefits this less capable model.
- **MuSiQue 3-hop and 4-hop:** Near-zero accuracy across all conditions, relegated to Appendix A due to "exceedingly poor performance" (Section 5).

### Adjacent vs. Separated Evidence

Figure 4 compares average accuracy when evidence documents are adjacent vs. separated for full-document prompts. For GPT-3.5-Turbo:

| Dataset | Adjacent Avg. | Separated Avg. |
|---|---|---|
| HotpotQA (2-hop) | ~73% | ~71% |
| MuSiQue (2-hop) | ~47% | ~45% |
| MuSiQue (3-hop) | ~49% | ~45% |
| MuSiQue (4-hop) | ~52% | ~48% |
| 2Wiki (2-hop) | ~61% | ~59% |
| 2Wiki (4-hop) | ~90% | ~89% |

For MPT-7b-instruct, the same pattern holds with larger gaps on some datasets.

---

## Limitations and Failure Modes

- **Subset of position combinations evaluated.** Computational constraints limited the analysis to 9 configurations per hop count out of 190, 1,140, or 4,845 possible orderings. The selected subset may not capture the full extent of positional effects (Limitations section).
- **Mid-2023 model vintage.** All models evaluated (GPT-3.5-Turbo-1106, MPT-7b-instruct, Llama-2-7b-longlora) were state-of-the-art at the time of the study. Newer models with greater reasoning capabilities may exhibit improved robustness (Limitations section).
- **Out-of-the-box context reduction only.** Summarization (BART-large-CNN) and KG extraction (LLaMA 2 7B) are generic methods not tailored for multi-hop reasoning. Model-specific fine-tuning or optimized preprocessing was not explored (Limitations section).
- **No mechanistic analysis.** The paper characterizes the positional effects empirically but does not investigate the underlying attention mechanisms or architectural causes.
- **Llama-2-7b-longlora near-zero performance.** The non-instruction-tuned model achieves near-zero accuracy on MuSiQue 3-hop and 4-hop across all conditions, limiting the conclusions that can be drawn about positional effects for weaker models (Table 5, Section 5).
- **Closed-book baselines vary widely.** Llama-2-7b-longlora achieves only 0.74% closed-book on MuSiQue, questioning whether the model has sufficient capability for the task independent of positional effects.
- **CoT + KG interaction.** Combining KG extraction with CoT often produces catastrophic results (e.g., HotpotQA GPT-3.5: 76.72% standard -> 34.94% KG + CoT), suggesting these mitigations can interact negatively.

---

## Conclusions

### Contributions

1. **Inter-document distance as a new dimension of positional bias.** Demonstrated that in multi-hop QA, performance depends not only on where evidence documents are located relative to the context edges but also on how far apart they are from each other — adjacent evidence consistently outperforms separated evidence across datasets and models (Figure 4, Section 6).

2. **Multi-hop extension of lost-in-the-middle.** Extended the analysis of Liu et al. (2024) from single-hop to multi-hop QA with 2, 3, and 4 reasoning hops across three standard datasets, confirming that the positional bias persists and compounds with reasoning complexity (Figures 2-3, Tables 3-5).

3. **CoT effectiveness depends on instruction tuning.** Showed that chain-of-thought prompting is a viable partial mitigation for instruction-tuned models but is harmful for non-instruction-tuned models, where it exacerbates primacy bias through over-reliance on few-shot exemplars (Figures 2-3, Section 6).

4. **Context reduction trade-off.** Established that generic context reduction (summarization, KG extraction) flattens positional bias curves but at the cost of overall accuracy, particularly for instruction-tuned models. Non-instruction-tuned models benefit more from context reduction (Figure 2, Section 6).

### Implications

1. **Re-ranking strategies may be insufficient for multi-hop QA.** Because positional bias affects both absolute positions and inter-document distances, simply moving documents to the edges does not solve the problem when multiple evidence documents must be reasoned over. [Inference: the combinatorial growth of arrangements makes re-ranking impractical.]

2. **Multi-hop QA requires dedicated mitigation strategies.** The failure of generic context reduction and the mixed results of CoT suggest that multi-hop positional bias may require task-specific solutions rather than general-purpose mitigations. [Inference: this is the authors' conclusion but no specific solution is proposed.]

---

## Key Claims

1. **Adjacent evidence yields higher accuracy than separated evidence.** Across all datasets and instruction-tuned models, placing evidence documents adjacently yields higher average accuracy than separating them with distractors. For GPT-3.5-Turbo on MuSiQue 4-hop, adjacent documents average ~52% vs. ~48% separated (Figure 4, Section 6). Status: **supported**.

2. **CoT helps instruction-tuned models but harms non-instruction-tuned ones.** For MPT and GPT-3.5, CoT improves performance by 2-6 percentage points in most configurations. For Llama-2-7b-longlora, CoT causes HotpotQA accuracy to drop from 3.11% to 0.59% at (1,2) and from 30.75% to 0.51% on 2Wiki 4-hop at (1,2,3,4) (Figures 2-3, Tables 3, 5, Section 6). Status: **supported**.

3. **Context reduction flattens positional bias but reduces accuracy.** On HotpotQA with GPT-3.5, summarization reduces the best-worst gap from ~6 percentage points (standard) to ~4 percentage points, but drops peak accuracy from 76.72% to 60.73%. KG extraction drops peak accuracy further to 57.52% (Table 3, Section 6). Status: **supported**.

4. **Llama-2-7b-longlora exhibits strong primacy bias.** The model shows dramatic accuracy drops from position (1,2) to non-initial positions across all datasets: on 2Wiki 2-hop standard, 27.29% at (1,2) vs. 2.54% at (19,20) (Table 5, Section 6). Status: **supported**.

5. **Generic context reduction is insufficient for multi-hop QA.** Context reduction methods "often produce reasoning chains that are too fragile for effective application in multi-hop QA" — combining KG + CoT on HotpotQA with GPT-3.5 drops accuracy to 34.94% at (1,2) vs. 76.72% standard, and to 1.16% with Llama-2-longlora (Tables 3, 5, Section 8). Status: **supported**.

---

## Open Questions

1. **Newer model robustness.** Do newer and larger models (GPT-4, Llama 3, Gemini 1.5) exhibit the same positional bias patterns in multi-hop QA, or has scaling and improved training mitigated the problem? Not yet addressed.

2. **Tailored context reduction.** Can preprocessing methods that specifically preserve multi-hop reasoning paths (rather than generic summarization) mitigate positional bias without sacrificing accuracy? Not yet addressed.

3. **Dynamic CoT for non-instruction-tuned models.** Can advanced prompting techniques such as dynamic chain-of-thought or least-to-most prompting help non-instruction-tuned models overcome their primacy bias? Not yet addressed.

4. **Exhaustive position evaluation.** Would evaluating all C(20,k) position combinations reveal non-linear interactions between evidence positions that the subset analysis misses? Not yet addressed.

5. **External memory mechanisms.** Could augmenting model architectures with dynamic evidence retrieval or external memory reduce sensitivity to document positioning in multi-hop settings? Not yet addressed.

---

## Core References and Why They Are Referenced

### Direct Predecessors

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* The foundational paper establishing the U-shaped positional bias in single-hop QA and key-value retrieval. This paper directly extends the experimental setup (20 documents, best-subspan accuracy, Contriever distractors) to multi-hop settings.

### Mitigation Strategies

- **Peysakhovich and Lerer (2023)** -- *Attention Sorting Combats Recency Bias in Long Context Language Models.* Proposed sorting documents by attention scores to mitigate positional bias. Referenced as a re-ranking approach that scales poorly to multi-hop settings due to combinatorial growth in document orderings.

- **Tang et al. (2023)** -- *Found in the Middle: Permutation Self-Consistency Improves Listwise Ranking in Large Language Models.* Introduced permutation self-consistency for re-ranking. Referenced as another re-ranking strategy limited by combinatorial scaling in multi-hop QA.

- **Kim et al. (2024)** -- *SURE: Improving Open-Domain Question Answering of LLMs via Summarized Retrieval.* Document length reduction via summarization. Referenced as a context reduction approach that this paper evaluates.

- **Zhou et al. (2023)** -- *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models.* Chain-of-thought prompting foundation. Referenced as the basis for the CoT prompting strategy evaluated.

### Multi-Hop QA Foundations

- **Yang et al. (2018)** -- *HotpotQA: A Dataset for Diverse, Explainable Multi-Hop Question Answering.* Provides the HotpotQA dataset used in evaluation.

- **Saxena et al. (2020)** -- *Improving Multi-Hop Question Answering over Knowledge Graphs Using Knowledge Base Embeddings.* Multi-hop QA over knowledge graphs. Referenced as related work on the multi-hop reasoning challenge.

### Concurrent Work

- **Levy et al. (2024)** -- *Same Task, More Tokens: The Impact of Input Length on the Reasoning Performance of Large Language Models.* Concurrent work examining how input length degrades reasoning. Differs from this paper in focusing on overall input size rather than document position, using a custom true/false dataset (FLenQA) rather than standard multi-hop QA benchmarks, and limiting analysis to two-step questions.

### Models Evaluated

- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* Provides the ALiBi positional encoding used by MPT-7b-8k-instruct.

- **Chen et al. (2023)** -- *LongLoRA: Efficient Fine-Tuning of Long-Context Large Language Models.* Provides the LongLoRA fine-tuning method used for Llama-2-7b-longlora-8k-ft.

- **Touvron et al. (2023)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Base model for the Llama-2-7b-longlora variant and the LLaMA 2 7B model used for KG triple extraction.

### Context Reduction Tools

- **Lewis et al. (2019)** -- *BART: Denoising Sequence-to-Sequence Pre-Training for Natural Language Generation, Translation, and Comprehension.* Provides BART-large-CNN used for document summarization, with maximum 50-token generation per document.

### Evaluation Methodology

- **Kwiatkowski et al. (2019)** -- *Natural Questions: A Benchmark for Question Answering Research.* Referenced for the evaluation methodology adopted from Liu et al. (2024).

- **Kandpal et al. (2023)** -- *Large Language Models Struggle to Learn Long-Tail Knowledge.* Referenced for the best-subspan accuracy metric used.
