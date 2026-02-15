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
    scope: "2-4 hop QA, 20-document contexts, GPT-3.5-Turbo and MPT-7b-instruct, HotpotQA/2WikiMultihopQA/MuSiQue"
    magnitude: "~2-10 percentage point advantage for adjacent vs. separated evidence depending on dataset and model (Figure 4)"
  - id: C2
    claim: "Chain-of-thought prompting improves multi-hop QA performance for instruction-tuned models (MPT-7b-instruct, GPT-3.5-Turbo) but causes sharp performance decline for non-instruction-tuned models (Llama-2-7b-longlora)"
    evidence: "Figures 2-3, Section 6, Tables 3-5"
    status: supported
    scope: "3 models tested (2 instruction-tuned, 1 non-instruction-tuned), 3 multi-hop QA datasets, few-shot CoT"
    magnitude: "CoT improves instruction-tuned models by 2-6 pp; for Llama-2-longlora, CoT drops HotpotQA (1,2) from 3.11% to 0.59% and 2Wiki 4-hop (1,2,3,4) from 30.51% to 0.51%"
  - id: C3
    claim: "Context reduction via summarization or knowledge graph triple extraction flattens positional bias curves but reduces overall accuracy, particularly for instruction-tuned models"
    evidence: "Figure 2, Section 6, Table 2, Tables 3-5"
    status: supported
    scope: "BART-large-CNN summarization (50 token max) and LLaMA 2 7B KG extraction, 3 datasets, 3 models"
    magnitude: "On HotpotQA GPT-3.5, standard peak 76.72% drops to 60.73% (summaries) and 57.52% (KG); positional gap narrows from ~6 pp to ~4 pp"
  - id: C4
    claim: "Llama-2-7b-longlora exhibits strong primacy bias with little to no recency bias, and CoT prompting exacerbates this by causing over-reliance on few-shot exemplars"
    evidence: "Figure 3, Section 6, Table 5"
    status: supported
    scope: "Llama-2-7b-longlora-8k-ft only, non-instruction-tuned, 3 datasets"
    magnitude: "On 2Wiki 2-hop standard, 27.29% at (1,2) vs. 2.54% at (19,20); CoT drops performance further to 0.26% at (1,2)"
  - id: C5
    claim: "Existing out-of-the-box context reduction methods are insufficient to fully mitigate the lost-in-the-middle problem in multi-hop settings, as they often produce reasoning chains too fragile for effective multi-hop QA"
    evidence: "Section 8, Tables 3-5"
    status: supported
    scope: "Generic BART-large-CNN summarization and LLaMA 2 7B KG extraction, no task-specific fine-tuning"
    magnitude: "KG+CoT on HotpotQA GPT-3.5 drops to 34.94% at (1,2) vs. 76.72% standard; Llama-2-longlora KG+CoT drops to 1.16% at (1,2) on HotpotQA"
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
  - question: "What is the interaction between the number of reasoning hops and the severity of positional bias -- does the effect scale linearly or combinatorially with hop count?"
    addressed_by: null
  - question: "Can dynamic chain-of-thought or advanced prompting techniques help non-instruction-tuned models overcome their primacy bias in multi-hop QA?"
    addressed_by: null
  - question: "Would exhaustive evaluation of all C(20,k) position combinations reveal non-linear interactions between evidence positions that the subset analysis misses?"
    addressed_by: null
  - question: "Could augmenting model architectures with external memory mechanisms or dynamic evidence retrieval reduce sensitivity to document positioning in multi-hop settings?"
    addressed_by: null
---
# Lost in the Middle, and In-Between: Enhancing Language Models' Ability to Reason Over Long Contexts in Multi-Hop QA

**Authors:** George Arthur Baker, Ankush Raut, Sagi Shaier, Lawrence E Hunter, Katharina von der Wense (University of Colorado Boulder; University of Chicago, Department of Pediatrics; Johannes Gutenberg University Mainz)
**Date:** December 2024, arXiv:2412.10079

---

## Core Research Problem

The "lost in the middle" phenomenon, first identified by Liu et al. (2024) -- *Lost in the Middle: How Language Models Use Long Contexts* -- shows that language models exhibit a U-shaped performance curve when relevant information is placed at different positions in the input context: accuracy is highest when critical information is near the beginning or end, and lowest when it is in the middle. However, prior work has only studied this in **single-hop** settings, where a single piece of critical information must be located among distractors.

In multi-hop question answering (MHQA), models must reason over **multiple** evidence documents scattered across the input context to arrive at an answer. This introduces an additional dimension to positional bias beyond absolute position: the **relative distance between evidence documents**. Existing mitigation strategies face fundamental scalability limitations in this setting:

- **Document re-ranking** (Peysakhovich and Lerer, 2023; Tang et al., 2023): The number of possible document orderings grows combinatorially with reasoning steps, making robust re-ranking impractical.
- **Summarization** (Kim et al., 2024): The likelihood of omitting essential information during summarization grows with the number of reasoning steps, risking broken reasoning chains.
- **Extended-context training** (An et al., 2024): Would need to account for overwhelming positional combinations rather than single-document placement.

**The core challenge is: how both the absolute position and the relative distance between multiple evidence documents affect multi-hop QA performance, and whether existing mitigation strategies (CoT prompting, context reduction) can address the compounded positional bias in multi-hop settings.**

---

## Problem Solutions

The paper provides an **empirical characterization** of the lost-in-the-middle problem in multi-hop QA settings and evaluates potential mitigations. The key observations are:

1. **Inter-document distance matters.** Performance degrades not only when evidence is in the middle of the context, but also when evidence documents are separated by distractors rather than placed adjacently (Figure 4, Section 6).
2. **CoT helps instruction-tuned models only.** Chain-of-thought prompting improves performance for instruction-tuned models (MPT-7b-instruct, GPT-3.5-Turbo) but causes sharp performance declines for non-instruction-tuned models (Llama-2-7b-longlora) due to primacy bias and over-reliance on exemplars (Figures 2-3, Section 6).
3. **Context reduction is a double-edged sword.** Summarization and KG triple extraction flatten positional bias curves but reduce overall accuracy, as information loss during reduction breaks fragile multi-hop reasoning chains (Figure 2, Section 6).

---

## Approach Details

### Method

This is an empirical study using controlled manipulation of evidence document positions within 20-document contexts across three multi-hop QA datasets. For each question, evidence documents are placed at specific ordinal positions among distractor documents, and model accuracy is measured as a function of position configuration. The methodology follows Liu et al. (2024), extended to handle multiple evidence documents simultaneously.

### Key Technical Components

**Datasets (Table 1, Section 3.1):**

| Dataset | Hops | Questions |
|---|---|---|
| HotpotQA | 2 | 3,703 |
| 2WikiMultihopQA | 2, 4 | 6,288 |
| MuSiQue-Ans | 2, 3, 4 | 1,209 |

The second half of each validation set is used as the test set (official test sets are private). For 2WikiMultihopQA, which contains only 10 documents per question, an additional 10 distractor documents are retrieved using a Contriever setup following Liu et al. (2024) (Table 1, footnote 1, Section 3.1).

**Position configurations tested (all within 20 total documents, Section 4):**

- **2-hop adjacent:** (1,2), (5,6), (10,11), (15,16), (19,20)
- **2-hop separated:** (1,5), (5,10), (10,15), (15,20)
- **3-hop adjacent:** (1,2,3), (5,6,7), (10,11,12), (15,16,17), (18,19,20)
- **3-hop separated:** (1,5,10), (5,10,15), (10,15,20)
- **4-hop adjacent:** (1,2,3,4), (5,6,7,8), (10,11,12,13), (15,16,17,18), (17,18,19,20)
- **4-hop separated:** (1,3,5,7), (5,7,9,11), (10,12,14,16), (14,16,18,20)

The total possible position combinations are C(20,2) = 190 for 2-hop, C(20,3) = 1,140 for 3-hop, and C(20,4) = 4,845 for 4-hop, making exhaustive evaluation computationally prohibitive. The study evaluates 5 adjacent and 4 separated configurations for 2-hop and 4-hop, and 5 adjacent and 3 separated for 3-hop (Section 4).

**Context reduction methods (Section 3.1.3):**

1. **Knowledge graph triple extraction:** LLaMA 2 7B (Touvron et al., 2023) instruction-prompted to extract factual triples from each document independently.
2. **Summarization:** BART-large-CNN (Lewis et al., 2019), fine-tuned on CNN/DailyMail, with maximum generation length capped at 50 tokens per document.

Average document word counts after reduction (Table 2, Section 3.1.3):

| Dataset | Full | Summarized | KG |
|---|---|---|---|
| HotpotQA | 69 | 29 | 33 |
| 2WikiMultihopQA | 45 | 21 | 29 |
| MuSiQue-Ans | 85 | 32 | 35 |

**Evaluation metric:** Best-subspan accuracy -- score of 1 if the model's output contains the annotated answer (or any alternative answer for MuSiQue), 0 otherwise. Following Liu et al. (2024), Kandpal et al. (2023), and Mallen et al. (2022) (Section 3.1.2).

**Generation parameters:** Temperature 0, maximum 256 tokens (Section 4).

### Experimental Setup

**Models evaluated (Section 3.1.1):**

| Model | Type | Context Window | Notes |
|---|---|---|---|
| MPT-7b-8k-instruct | Open, instruction-tuned | 8K tokens | Uses ALiBi positional encoding (Press et al., 2022) |
| Llama-2-7b-longlora-8k-ft | Open, non-instruction-tuned | 8K tokens | LongLoRA fine-tuning of Llama 2 (Chen et al., 2023) |
| GPT-3.5-turbo-1106 | Closed-source | 16K tokens | Reproducible outputs |

**Closed-book baselines** (no documents provided; percentages next to dataset names in Tables 3-5):

| Dataset | GPT-3.5-Turbo | MPT-7b-instruct | Llama-2-longlora |
|---|---|---|---|
| HotpotQA | 40.64% | 14.88% | 12.21% |
| MuSiQue-Ans | 14.39% | 3.64% | 0.74% |
| 2WikiMultihopQA | 44.99% | 20.13% | 31.65% |

**Prompting conditions (6 per experiment):** standard, standard + CoT, KG, KG + CoT, summaries, summaries + CoT. CoT uses few-shot exemplars (Section 4).

**Reproducibility:** Code and data are available at https://github.com/Spongeorge/long-context-multihop. Temperature is set to 0 for reproducibility. No variance estimates or multiple runs are reported (single run per configuration, limited evidence).

### Key Results

**GPT-3.5-turbo-1106 -- HotpotQA 2-hop (Table 3):**

| Condition | (1,2) | (5,6) | (10,11) | (15,16) | (19,20) | (1,5) | (5,10) | (10,15) | (15,20) |
|---|---|---|---|---|---|---|---|---|---|
| Standard | 76.72% | 71.13% | 71.40% | 72.81% | 73.89% | 73.75% | 69.97% | 70.16% | 71.13% |
| Standard + CoT | 79.26% | 73.91% | 75.10% | 75.61% | 76.64% | 77.48% | 72.89% | 71.78% | 74.13% |
| KG | 56.09% | 53.82% | 53.61% | 54.28% | 57.52% | 56.12% | 51.96% | 52.01% | 54.65% |
| KG + CoT | 34.94% | 28.03% | 29.57% | 59.92% | 31.14% | 31.60% | 25.25% | 28.54% | 29.84% |
| Summaries | 60.11% | 59.52% | 58.30% | 59.79% | 60.73% | 59.90% | 57.01% | 56.36% | 58.71% |
| Summaries + CoT | 60.63% | 61.09% | 58.84% | 59.79% | 61.92% | 61.27% | 57.84% | 57.41% | 57.90% |

- Standard prompting shows a ~5 percentage point drop from the best edge position (76.72% at (1,2)) to the middle (71.13% at (5,6) and 71.40% at (10,11)).
- CoT improves performance across all positions by approximately 2-4 percentage points.
- KG extraction drastically reduces peak accuracy (76.72% to 56.09%) while narrowing the positional spread.
- KG + CoT produces the worst results overall (34.94% at best), suggesting CoT reasoning on impoverished KG context is counterproductive. The anomalous 59.92% at (15,16) is present in the source data.

**GPT-3.5-turbo-1106 -- MuSiQue-Ans 2-hop (Table 3):**

| Condition | (1,2) | (5,6) | (10,11) | (15,16) | (19,20) | (1,5) | (5,10) | (10,15) | (15,20) |
|---|---|---|---|---|---|---|---|---|---|
| Standard | 56.23% | 43.45% | 41.21% | 43.93% | 52.72% | 53.83% | 40.89% | 38.18% | 45.21% |
| Standard + CoT | 58.47% | 48.24% | 44.25% | 46.96% | 53.83% | 55.43% | 48.08% | 44.25% | 47.28% |

- The U-shaped curve is more pronounced than HotpotQA: 15 percentage point drop from (1,2) at 56.23% to (10,11) at 41.21% (Section 6).
- Separated positions show even lower accuracy than middle adjacent positions: (10,15) at 38.18% vs. (10,11) at 41.21%.

**GPT-3.5-turbo-1106 -- 2WikiMultihopQA 4-hop (Table 3):**

| Condition | (1,2,3,4) | (5,6,7,8) | (10,11,12,13) | (15,16,17,18) | (17,18,19,20) | (1,3,5,7) | (5,7,9,11) | (10,12,14,16) | (14,16,18,20) |
|---|---|---|---|---|---|---|---|---|---|
| Standard | 91.29% | 90.04% | 90.12% | 89.82% | 89.60% | 89.82% | 88.65% | 89.24% | 89.60% |
| Standard + CoT | 93.27% | 92.24% | 93.70% | 92.24% | 93.12% | 93.05% | 92.24% | 92.31% | 92.46% |
| Summaries + CoT | 94.80% | 92.31% | 93.41% | 93.92% | 92.83% | 94.22% | 92.97% | 93.41% | 93.48% |

- Performance is high across all configurations (89-95%), with smaller positional effects (~2 percentage points).
- CoT provides consistent improvement of ~2-3 percentage points.
- This dataset at 4-hop appears substantially easier than the others, potentially because many questions can be partially answered from parametric knowledge (44.99% closed-book baseline).

**MPT-7b-8k-instruct -- HotpotQA 2-hop (Table 4):**

| Condition | (1,2) | (5,6) | (10,11) | (15,16) | (19,20) | (1,5) | (5,10) | (10,15) | (15,20) |
|---|---|---|---|---|---|---|---|---|---|
| Standard | 51.90% | 45.13% | 46.46% | 49.56% | 53.25% | 41.61% | 38.54% | 41.48% | 47.18% |
| Standard + CoT | 57.17% | 48.88% | 49.96% | 54.04% | 59.09% | 48.96% | 46.26% | 50.36% | 55.60% |

- U-shaped curve with recency bias: highest at (19,20) = 53.25% for standard, 59.09% for CoT.
- CoT provides larger gains for MPT than GPT-3.5 (5-6 percentage points).
- Separated positions systematically underperform adjacent positions (e.g., (1,5) at 41.61% vs. (1,2) at 51.90%).

**Llama-2-7b-longlora-8k-ft -- catastrophic performance patterns (Table 5):**

| Dataset/Condition | Best Position/Score | Worst Position/Score |
|---|---|---|
| HotpotQA, Standard | (1,2): 3.11% | (10,15): 0.70% |
| HotpotQA, KG | (1,2): 25.76% | (15,20): 7.56% |
| HotpotQA, Standard + CoT | (1,2): 0.59% | (5,6)-(19,20): ~0.46% |
| MuSiQue 2-hop, Standard | (1,2): 1.92% | most positions: 0.00% |
| MuSiQue 3-hop, All conditions | 0.00%-0.26% across all positions | 0.00% |
| MuSiQue 4-hop, All conditions | 0.00% across all positions | 0.00% |
| 2Wiki 2-hop, Standard | (1,2): 27.29% | (19,20): 2.54% |
| 2Wiki 4-hop, Standard | (1,2,3,4): 30.51% | (14,16,18,20): 3.73% |
| 2Wiki 4-hop, Standard + CoT | (1,2,3,4): 0.51% | across all: ~0.51-1.10% |

- **Pronounced primacy bias:** Performance drops sharply from position (1,2) to all other positions. On 2Wiki 2-hop standard, accuracy falls from 27.29% at (1,2) to 2.54% at (19,20) -- a 24.75 percentage point drop (Table 5).
- **CoT is destructive:** On HotpotQA, standard prompting yields 3.11% at (1,2), while CoT drops to 0.59%. On 2Wiki 4-hop, standard yields 30.51% at (1,2,3,4) while CoT drops to 0.51% (Table 5, Section 6).
- **KG extraction helps more than full documents for this model:** On HotpotQA, KG yields 25.76% at (1,2) vs. 3.11% for standard, and on 2Wiki 4-hop, KG yields 43.56% at (1,2,3,4) vs. 30.51% standard. Context reduction benefits this less capable model (Table 5, Section 6).
- **MuSiQue 3-hop and 4-hop:** Near-zero accuracy across all conditions (0.00% for all 4-hop configurations), relegated to Appendix A due to "exceedingly poor performance" (Figure 3 caption).

### Adjacent vs. Separated Evidence

Figure 4 compares average accuracy when evidence documents are adjacent vs. separated for full-document standard prompts. Based on the Figure 4 description (visual estimates from bar charts, Section 6):

For **GPT-3.5-Turbo:** Adjacent documents consistently achieve ~2-5% higher accuracy across all datasets except 2Wiki 4-hop where performance is nearly identical (~90%). The effect is present but modest given the overall high performance on some datasets.

For **MPT-7b-8k-instruct:** Adjacent documents show larger gains (~3-10% higher) on most datasets, with the most pronounced difference on HotpotQA 2-hop (~50% vs ~42%).

Both models show the smallest distance effect on 2Wiki 4-hop, where overall accuracy is highest (tested across 2 instruction-tuned models, 6 dataset-hop combinations; moderate evidence).

---

## Limitations and Failure Modes

- **Subset of position combinations evaluated.** Computational constraints limited the analysis to 9 configurations per hop count out of 190 (2-hop), 1,140 (3-hop), or 4,845 (4-hop) possible orderings. The selected subset may not capture the full extent of positional effects or non-linear interactions between positions (Limitations section).
- **Mid-2023 model vintage.** All models evaluated (GPT-3.5-Turbo-1106, MPT-7b-instruct, Llama-2-7b-longlora) were state-of-the-art at the time of the study but have since been superseded. Newer models with greater reasoning capabilities may exhibit improved robustness (Limitations section).
- **Out-of-the-box context reduction only.** Summarization (BART-large-CNN, 50-token max) and KG extraction (LLaMA 2 7B) are generic methods not tailored for multi-hop reasoning. Model-specific fine-tuning or optimized preprocessing was not explored (Limitations section).
- **Llama-2-7b-longlora near-zero performance.** The non-instruction-tuned model achieves 0.00% accuracy on MuSiQue 3-hop and 4-hop across all conditions, and near-zero on most other configurations, limiting the conclusions that can be drawn about positional effects for weaker models. Its 0.74% closed-book baseline on MuSiQue questions whether the model has sufficient task capability independent of positional effects (Table 5, Section 5).
- **CoT + KG interaction.** Combining KG extraction with CoT often produces catastrophic results (e.g., HotpotQA GPT-3.5: 76.72% standard vs. 34.94% KG + CoT), suggesting these mitigations can interact negatively rather than additively (Table 3).
- **[Inferred]** No mechanistic analysis of attention patterns or architectural causes. The paper characterizes positional effects empirically but does not investigate the underlying attention mechanisms producing the U-shaped curve or primacy bias.
- **[Inferred]** No variance estimates or multiple runs reported. All results appear to be single runs, limiting statistical confidence in the reported differences, particularly for smaller effects (~2 percentage points).
- **[Inferred]** English-only evaluation. All three datasets are English, limiting generalizability claims to other languages.

#### Scope and Comparability

- **What was not tested:** Models larger than 7B parameters in the open-source category; no models with context windows exceeding 16K tokens; no models from the GPT-4, Llama 3, Gemini, or Claude families; no instruction-tuned variants of Llama 2; no evaluation of re-ranking mitigations in multi-hop settings (only discussed theoretically).
- **Comparability notes:** The 20-document fixed context follows Liu et al. (2024), enabling direct comparison with single-hop results from that paper. However, the multi-hop datasets (HotpotQA, 2WikiMultihopQA, MuSiQue) differ from the NaturalQuestions-Open dataset used by Liu et al. The use of best-subspan accuracy is consistent with Liu et al. but differs from exact-match metrics used in some multi-hop QA leaderboards. The closed-book baselines (e.g., 44.99% for GPT-3.5 on 2WikiMultihopQA) suggest substantial parametric knowledge contamination, which may confound the positional bias measurements on that dataset. Levy et al. (2024) is concurrent work studying input length effects on reasoning, but uses a custom true/false dataset (FLenQA) with only 2-step questions, making direct comparison difficult (Section 2.4).

---

## Conclusions

### Contributions

1. **Inter-document distance as a new dimension of positional bias.** Demonstrated that in multi-hop QA, performance depends not only on where evidence documents are located relative to the context edges but also on how far apart they are from each other -- adjacent evidence consistently outperforms separated evidence by ~2-10 percentage points across datasets and models (Figure 4, Section 6).

2. **Multi-hop extension of lost-in-the-middle.** Extended the analysis of Liu et al. (2024) from single-hop to multi-hop QA with 2, 3, and 4 reasoning hops across three standard datasets (HotpotQA, 2WikiMultihopQA, MuSiQue), confirming that the U-shaped positional bias persists in multi-hop settings (Figures 2-3, Tables 3-5).

3. **CoT effectiveness depends on instruction tuning.** Showed that chain-of-thought prompting improves instruction-tuned model performance by 2-6 percentage points but is harmful for non-instruction-tuned models, where it exacerbates primacy bias through over-reliance on few-shot exemplars -- Llama-2-longlora drops from 3.11% to 0.59% on HotpotQA (1,2) with CoT (Figures 2-3, Section 6, Tables 3, 5).

4. **Context reduction trade-off quantified.** Established that generic context reduction (summarization, KG extraction) flattens positional bias curves but at the cost of overall accuracy: on HotpotQA GPT-3.5, summarization drops peak accuracy from 76.72% to 60.73% while narrowing the positional gap. Non-instruction-tuned models (Llama-2-longlora) benefit more from context reduction, with KG extraction yielding 25.76% vs. 3.11% standard on HotpotQA (Figure 2, Section 6, Tables 3, 5).

### Implications

1. **Re-ranking strategies may be insufficient for multi-hop QA.** Because positional bias affects both absolute positions and inter-document distances, simply moving documents to the edges does not solve the problem when multiple evidence documents must be reasoned over. The combinatorial growth of arrangements (C(20,k) configurations) makes re-ranking impractical in multi-hop settings. [Inference: the authors discuss this theoretically but do not evaluate re-ranking experimentally.]

2. **Multi-hop QA requires dedicated mitigation strategies.** The failure of generic context reduction and the mixed results of CoT suggest that multi-hop positional bias may require task-specific solutions -- such as tailored preprocessing that preserves reasoning paths, or architectural modifications for dynamic evidence retrieval -- rather than general-purpose mitigations (Sections 7-8). [Inference: the authors suggest this direction but propose no concrete solution.]

---

## Key Claims

1. **Adjacent evidence yields higher accuracy than separated evidence in multi-hop QA.** Across all datasets and instruction-tuned models, placing evidence documents adjacently yields higher average accuracy than separating them with distractors. For GPT-3.5-Turbo, adjacent documents achieve ~2-5 percentage points higher accuracy across most dataset-hop combinations; for MPT-7b-instruct, the gap is larger at ~3-10 percentage points (Figure 4, Section 6). Scope: 2-4 hop, 20-document contexts, 3 datasets, 2 instruction-tuned models. Evidence from Figure 4 bar charts (visual estimates, moderate evidence -- no exact numbers provided for this aggregation). Status: **supported**.

2. **CoT helps instruction-tuned models but harms non-instruction-tuned ones.** For MPT-7b-instruct and GPT-3.5-Turbo, CoT improves performance by 2-6 percentage points in most configurations. For Llama-2-7b-longlora, CoT causes HotpotQA accuracy to drop from 3.11% to 0.59% at (1,2), and 2Wiki 4-hop standard accuracy to drop from 30.51% to 0.51% at (1,2,3,4) (Figures 2-3, Tables 3, 4, 5, Section 6). Scope: 3 models (2 instruction-tuned, 1 non-instruction-tuned), few-shot CoT prompting, 3 datasets. Status: **supported** (tested across 3 models but only 1 non-instruction-tuned model, limited evidence for the negative direction).

3. **Context reduction flattens positional bias but reduces accuracy.** On HotpotQA with GPT-3.5, summarization reduces peak accuracy from 76.72% to 60.73% while narrowing the best-worst gap from ~6 percentage points (standard: 76.72% at (1,2) vs. 69.97% at (5,10)) to ~4 percentage points (summaries: 60.73% at (19,20) vs. 56.36% at (10,15)). KG extraction drops peak accuracy further to 57.52% (Table 3, Section 6). Scope: BART-large-CNN summarization with 50-token max and LLaMA 2 7B KG extraction, 3 datasets, 3 models. Status: **supported** (consistent trend across models and datasets, moderate evidence).

4. **Llama-2-7b-longlora exhibits strong primacy bias.** The model shows dramatic accuracy drops from first positions to all others: on 2Wiki 2-hop standard, 27.29% at (1,2) vs. 2.54% at (19,20) -- a 24.75 percentage point drop. On 2Wiki 4-hop standard, 30.51% at (1,2,3,4) vs. 3.73% at (14,16,18,20). The paper attributes this to the model's inherent biases and lack of instruction tuning (Table 5, Section 6). Scope: single non-instruction-tuned model, 3 datasets. Status: **supported** (strong effect size but tested on only 1 model, limited evidence for generalizability).

5. **Generic context reduction is insufficient for multi-hop QA.** The authors conclude that out-of-the-box context reduction methods "often produce reasoning chains that are too fragile for effective application in multi-hop QA." Combining KG extraction with CoT on HotpotQA with GPT-3.5 drops accuracy to 34.94% at (1,2) vs. 76.72% standard. With Llama-2-longlora, KG + CoT drops to 1.16% at (1,2) on HotpotQA (Tables 3, 5, Section 8). Scope: generic BART-large-CNN summarization and LLaMA 2 7B KG extraction only, no task-specific fine-tuning tested. Status: **supported** (for these specific generic methods; the claim does not address tailored methods).

---

## Open Questions

1. **Newer model robustness.** Do newer and larger models (GPT-4, Llama 3, Gemini 1.5) exhibit the same positional bias patterns in multi-hop QA, or has scaling and improved training mitigated the problem? The Limitations section acknowledges this explicitly. Not yet addressed.

2. **Tailored context reduction.** Can preprocessing methods that specifically preserve multi-hop reasoning paths (rather than generic summarization or KG extraction) mitigate positional bias without sacrificing accuracy? Raised in Sections 7 and 8. Not yet addressed.

3. **Hop count and positional bias interaction.** What is the interaction between the number of reasoning hops and the severity of positional bias -- does the effect scale linearly or combinatorially with hop count? The paper evaluates 2, 3, and 4 hops but does not systematically analyze the scaling relationship (Section 7). Not yet addressed.

4. **Dynamic CoT for non-instruction-tuned models.** Can advanced prompting techniques such as dynamic chain-of-thought or least-to-most prompting help non-instruction-tuned models overcome their primacy bias in multi-hop QA? Raised in Section 7. Not yet addressed.

5. **Exhaustive position evaluation.** Would evaluating all C(20,k) position combinations reveal non-linear interactions between evidence positions that the subset analysis (9 configurations) misses? Raised in Section 7 and Limitations. Not yet addressed.

6. **External memory mechanisms.** Could augmenting model architectures with external memory or dynamic evidence retrieval reduce sensitivity to document positioning in multi-hop settings? Raised in Section 7. Not yet addressed.

---

## Core References and Why They Are Referenced

### Direct Predecessors

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* The foundational paper establishing the U-shaped positional bias in single-hop QA and key-value retrieval. This paper directly extends the experimental setup (20 documents, best-subspan accuracy, Contriever distractors) to multi-hop settings. Referenced extensively throughout Sections 1-4.

### Mitigation Strategies

- **Peysakhovich and Lerer (2023)** -- *Attention Sorting Combats Recency Bias in Long Context Language Models.* Proposed sorting documents by attention scores to mitigate positional bias. Referenced as a re-ranking approach that scales poorly to multi-hop settings due to combinatorial growth in document orderings (Sections 1, 2.2).

- **Tang et al. (2023)** -- *Found in the Middle: Permutation Self-Consistency Improves Listwise Ranking in Large Language Models.* Introduced permutation self-consistency for document re-ranking. Referenced as another re-ranking strategy limited by combinatorial scaling in multi-hop QA (Sections 1, 2.2).

- **Kim et al. (2024)** -- *SURE: Improving Open-Domain Question Answering of LLMs via Summarized Retrieval.* Document length reduction via summarization for QA. Referenced as the summarization mitigation approach that this paper extends to multi-hop settings (Section 1).

- **Zhou et al. (2023)** -- *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models.* Chain-of-thought prompting technique. Referenced as the basis for the CoT prompting strategy evaluated in this paper (Section 1).

### Multi-Hop QA Foundations

- **Yang et al. (2018)** -- *HotpotQA: A Dataset for Diverse, Explainable Multi-Hop Question Answering.* Provides the HotpotQA dataset used for evaluation and is foundational work on multi-hop QA (Sections 2.3, 3.1).

- **Saxena et al. (2020)** -- *Improving Multi-Hop Question Answering over Knowledge Graphs Using Knowledge Base Embeddings.* Multi-hop QA over knowledge graphs, referenced as related work on the multi-hop reasoning challenge (Section 2.3).

- **Mavi et al. (2024)** -- *Multi-Hop Question Answering.* Survey of multi-hop QA tasks, referenced for background on MHQA challenges (Section 2.3).

### Concurrent Work

- **Levy et al. (2024)** -- *Same Task, More Tokens: The Impact of Input Length on the Reasoning Performance of Large Language Models.* Concurrent work examining how input length degrades reasoning. Differs in focusing on overall input size rather than document position, using a custom true/false dataset (FLenQA) rather than standard multi-hop QA benchmarks, and limiting analysis to two-step comparison questions (Section 2.4).

### Models and Architectures Evaluated

- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* Provides the ALiBi positional encoding mechanism used by MPT-7b-8k-instruct (Sections 1, 3.1.1).

- **Chen et al. (2023)** -- *LongLoRA: Efficient Fine-Tuning of Long-Context Large Language Models.* Provides the LongLoRA fine-tuning method used for Llama-2-7b-longlora-8k-ft (Section 3.1.1).

- **Touvron et al. (2023)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Base model for Llama-2-7b-longlora and the LLaMA 2 7B model used for KG triple extraction (Sections 3.1.1, 3.1.3).

### Context Reduction Tools

- **Lewis et al. (2019)** -- *BART: Denoising Sequence-to-Sequence Pre-Training for Natural Language Generation, Translation, and Comprehension.* Provides BART-large-CNN used for document summarization with 50-token maximum generation (Section 3.1.3).

### Evaluation Methodology

- **Kwiatkowski et al. (2019)** -- *Natural Questions: A Benchmark for Question Answering Research.* Referenced for the NaturalQuestions-Open dataset used by Liu et al. (2024) in the original lost-in-the-middle experiments (Section 2.1).

- **Kandpal et al. (2023)** -- *Large Language Models Struggle to Learn Long-Tail Knowledge.* Referenced for the best-subspan accuracy evaluation metric adopted (Section 3.1.2).

- **Mallen et al. (2022)** -- *When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories.* Co-referenced with Kandpal et al. for the evaluation metric (Section 3.1.2).
