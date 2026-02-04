---
title: "Large Language Models Can Be Easily Distracted by Irrelevant Context"
authors: "Shi, Chen, Misra, Scales, Dohan, Chi, Schärli, Zhou"
year: 2023
venue: "ICML 2023"
paper_type: conference-paper
categories: ["reasoning-evaluation", "in-context-learning"]
scope: ["math reasoning", "distractor robustness", "prompting techniques"]
benchmarks_used: ["gsm-ic", "gsm8k", "svamp"]
models_introduced: []
models_evaluated: ["gpt-3-175b"]
key_claims:
  - id: C1
    claim: "All prompting techniques are sensitive to irrelevant context: macro accuracy falls below 30% across CoT, LtM, Program, and 0-CoT with greedy decoding on code-davinci-002"
    evidence: "Table 3, Section 5.1"
    status: supported
  - id: C2
    claim: "Least-to-Most prompting is the most robust technique to irrelevant context, achieving approximately double the macro accuracy of CoT (18% vs. 6%) with code-davinci-002"
    evidence: "Table 3, Section 5.1"
    status: supported
  - id: C3
    claim: "Self-consistency with 20 samples improves micro accuracy by more than 11 percentage points and achieves 99.7% recall of correct answers for both CoT and LtM"
    evidence: "Table 3, Section 5.1"
    status: supported
  - id: C4
    claim: "Adding irrelevant context to few-shot exemplars consistently improves robustness without degrading performance on clean GSM8K or SVAMP problems"
    evidence: "Tables 3 and 5, Sections 5.1 and 5.3"
    status: supported
  - id: C5
    claim: "In-topic sentences, overlapping role names, and in-range numbers are the most distracting distractor properties"
    evidence: "Table 4, Section 5.2.1"
    status: supported
  - id: C6
    claim: "Using more exemplars (4 vs. 1) in the CoT prompt can increase susceptibility to irrelevant context, despite improving clean-problem accuracy"
    evidence: "Table 6, Section 5.4"
    status: supported
cross_references:
  - target: 2022-12-chain-of-thought-prompting
    type: extends
    detail: "Tests whether chain-of-thought reasoning is robust to irrelevant context added to math problems"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Both show LLMs struggle with context utilization; GSM-IC focuses on distractor content while Lost in the Middle focuses on positional bias"
  - target: 2024-08-found-in-the-middle
    type: complementary
    detail: "Found in the Middle refines the distraction finding to show the model's bias is positional rather than purely content-driven"
  - target: 2025-11-context-length-hurts-performance
    type: complementary
    detail: "Extends the analysis to show that even without irrelevant content, context length alone degrades performance"
  - target: 2024-08-flenqa-input-length-reasoning
    type: complementary
    detail: "FlenQA extends the irrelevant-context analysis by showing that degradation occurs even with duplicate (relevant-only) padding, isolating length from distraction"
open_questions:
  - question: "How does distractibility manifest in model families beyond the GPT-3 family (e.g., open-weight models, instruction-tuned models trained with different methods)?"
    addressed_by: null
  - question: "How does performance degrade when multiple irrelevant sentences are added, as in real-world inputs?"
    addressed_by: null
  - question: "Can fine-tuning on problems with irrelevant context provide more robust improvements than prompting-based mitigations alone?"
    addressed_by: null
---
# Large Language Models Can Be Easily Distracted by Irrelevant Context

**Authors:** Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Schärli, Denny Zhou (Google DeepMind; TTIC; Purdue University)
**Date:** July 2023, ICML 2023, PMLR 202:31210--31227 (arXiv:2302.00093)

---

## Core Research Problem

Large language models have achieved strong performance on arithmetic reasoning benchmarks such as GSM8K (Cobbe et al., 2021), but existing evaluations provide inputs where **all information is relevant** to the solution. Real-world problems typically include extraneous, contextually related information that must be filtered out. Studies in psychology show that irrelevant information significantly degrades problem-solving accuracy in children and adults (Hoyer et al., 1979; Pasolunghi et al., 1999; Marzocchi et al., 2002).

Prior work on input perturbations either substitutes sentences in base problems with paraphrases (Patel et al., 2021; Kumar et al., 2021) or evaluates adversarial distractors in reading comprehension (Jia & Liang, 2017). These approaches alter the problem structure rather than simply adding extraneous information. Meanwhile, work on prompting with noisy ground truth (Min et al., 2022; Madaan & Yazdanbakhsh, 2022) studies incorrect exemplar answers, not irrelevant content in the problem descriptions themselves.

**The core challenge is: how robust are large language model prompting techniques to irrelevant information in the input, and what strategies can mitigate the resulting performance degradation?**

---

## Problem Solutions

The paper introduces a controlled benchmark and systematic analysis of LLM distractibility. The key contributions are:

1. **GSM-IC benchmark.** Grade-School Math with Irrelevant Context -- an arithmetic reasoning dataset built from GSM8K that adds one irrelevant sentence to each problem description, systematically varying three distractor factors: topic relevance, role name overlap, and number range similarity.
2. **Distractibility characterization.** Evaluation of multiple prompting techniques on GSM-IC showing that macro accuracy drops below 30% when irrelevant context is introduced -- meaning fewer than 30% of base problems are consistently solved across all distractor variants.
3. **Factor analysis.** Identification of which properties of irrelevant information are most distracting: in-topic sentences, overlapping role names, and in-range numbers cause the largest performance drops.
4. **Mitigation strategies.** Self-consistency decoding, exemplars containing irrelevant context, and explicit instructions to ignore irrelevant information each improve robustness.

---

## Approach Details

### Method

**GSM-IC construction.** The benchmark starts from 100 base problems selected from the GSM8K training set. Each base problem requires 2--7 reasoning steps (60 require exactly 2 steps; see Figure 5, Appendix A). Problems are selected such that at least one of the investigated prompting techniques solves them correctly, making this an "easy" subset of GSM8K (Table 2).

For each base problem, one irrelevant sentence is inserted immediately before the question. The sentence is constructed by combining three binary factors (Figure 1, Section 3.1):

1. **Topic:** *In-topic* (same domain as the problem, e.g., a shopping problem gets an irrelevant shopping sentence) vs. *off-topic* (unrelated domain, drawn from general templates such as "The shoe size of [ROLE] is [NUMBER]").
2. **Role name overlap:** *Overlap* (the irrelevant sentence uses a character name derived from the original problem, e.g., "X's father", "X's sister") vs. *no overlap* (uses a name from {Ada, David, Emma, Jack, John, Mary, Max, Tom}).
3. **Number range:** *In-range* (the number a satisfies 1/10 <= a/b <= 10 for some number b in the original problem) vs. *out-of-range* (falls outside this ratio).

Four in-topic and four off-topic sentence templates are written per problem, with five overlapping and five non-overlapping role names, and four in-range and four out-of-range numbers. The full GSM-IC benchmark contains **58,052 examples**. A uniformly sampled evaluation subset **GSM-IC-4K** of 4,000 examples (covering all 100 base problems) is used throughout.

All generated sentences are manually verified for grammaticality and for not affecting the standard solution. When adding an irrelevant sentence introduces referential ambiguity (e.g., a pronoun "she" becoming ambiguous), the question is modified to use an explicit name (Table 10, Appendix A).

### Key Technical Components

**Evaluation metrics.** Three metrics capture different aspects of robustness (Section 3.2):

> **Micro accuracy:** Acc_micro(M; P) = sum_{p in P} 1[M(p) = s(p)] / |P|

Standard average accuracy across all GSM-IC examples.

> **Macro accuracy:** Acc_macro(M; B) = sum_{b in B} 1[for all p in P(b): M(p) = s(p)] / |B|

Fraction of base problems where the model answers correctly across *all* distractor variants. This is the strictest measure -- a base problem counts as correct only if every irrelevant-context variant is solved correctly.

> **Normalized accuracy:** norm(a_M; M) = a_M / n_M

Micro or macro accuracy divided by the model's accuracy on the original clean base problems (Table 2), measuring the relative degradation caused by irrelevant context.

**Prompting techniques evaluated (Section 4):**

| Technique | Description |
|---|---|
| Chain-of-Thought (CoT) | Step-by-step reasoning chains in exemplars (Wei et al., 2022) |
| Zero-shot CoT (0-CoT) | Appending "Let's think step by step:" without exemplars (Kojima et al., 2022) |
| Least-to-Most (LtM) | Decomposing problems into subproblems, solving sequentially (Zhou et al., 2022) |
| Program prompting | Generating Python code to solve the problem (Chowdhery et al., 2022; Chen et al., 2022) |
| Self-consistency (SC) | Sampling 20 outputs and taking majority vote (Wang et al., 2022c) |

**Mitigation strategies (Sections 4.2--4.3):**

1. **Exemplars with irrelevant context (IrrCtx):** Include irrelevant sentences in the few-shot exemplars themselves, teaching the model by example to ignore extraneous information.
2. **Instructed prompting (INST):** Prepend "Solve grade school math problems. Feel free to ignore irrelevant information given in the questions." before the exemplars.
3. **Self-consistency (SC):** Sample 20 responses with temperature 0.7 and take majority vote.

These mitigations are combinable (e.g., LtM + INST w/ IrrCtx).

### Experimental Setup

**Models:** code-davinci-002 (Codex, code-specialized GPT-3 variant) and text-davinci-003 (instruction-tuned GPT-3 variant with RLHF). Both are in the GPT-3 model family via the OpenAI API.

**Evaluation:** GSM-IC-4K (4,000 examples uniformly sampled across distractor conditions) for all main experiments. Greedy decoding (temperature 0) for base experiments; temperature 0.7 with 20 samples for self-consistency. Prompts use a single exemplar following Zhou et al. (2022) to avoid overfitting to specific prompt formats.

**Additional evaluation:** GSM8K development set (1,000 problems), SVAMP test set (Patel et al., 2021), and the football split of DROP (Dua et al., 2019) for generalization.

### Key Results

**Base performance on clean GSM8K problems (no irrelevant context, code-davinci-002, Table 2):**

| Method | CoT | LtM | Program | 0-CoT |
|---|---|---|---|---|
| Greedy | 95.0 | 94.0 | 83.0 | 44.0 |
| + SC | 96.0 | 99.0 | 91.0 | 76.0 |

**Main results on GSM-IC-4K (code-davinci-002, exemplar w/o irrelevant context, Table 3):**

| Method | Micro Acc. (Overall) | Micro Norm. | Macro Acc. (Overall) | Macro Norm. |
|---|---|---|---|---|
| CoT | 72.4 | 76.2 | 6.0 | 6.3 |
| CoT + INST | 77.8 | 81.8 | 15.0 | 15.8 |
| 0-CoT | 29.0 | 65.9 | 1.0 | 2.3 |
| LtM | 77.5 | 82.4 | 18.0 | 19.1 |
| LtM + INST | 80.6 | 85.7 | 25.0 | 26.6 |
| Program | 54.4 | 65.5 | 5.0 | 6.0 |
| CoT + SC | 88.1 | 91.8 | 30.0 | 31.3 |
| LtM + SC | 93.4 | 94.3 | 45.0 | 45.5 |

**With exemplar w/ irrelevant context (code-davinci-002, Table 3):**

| Method | Micro Acc. (Overall) | Macro Acc. (Overall) |
|---|---|---|
| CoT | 76.8 | 14.0 |
| LtM | 80.7 | 28.0 |
| LtM + INST | 82.8 | 28.0 |

**Key takeaways:**

- **All prompting techniques are highly distractible.** Adding a single irrelevant sentence causes macro accuracy to fall below 30% across all techniques with greedy decoding, meaning fewer than 30% of base problems are consistently solved across all distractor variants (Table 3, Section 5.1).
- **LtM is the most robust technique.** LtM achieves approximately double the macro accuracy of CoT (18% vs. 6%) with code-davinci-002. Problem decomposition helps the model focus on relevant subproblems. LtM performance is also more consistent across varying numbers of reasoning steps (Figure 4, Section 5.2.2).
- **Self-consistency is the most effective single mitigation.** SC improves micro accuracy by more than 11 percentage points. The correct answer appears in the 20 sampled responses for 99.7% of problems with both CoT and LtM, and 96.5% with 0-CoT (Section 5.1). However, the best macro accuracy with SC is only 45% (LtM + SC), meaning more than half of base problems still have at least one distractor variant that causes failure.
- **Exemplars with irrelevant context improve robustness.** Using exemplars that contain irrelevant information consistently outperforms clean exemplars across prompting techniques, and does not degrade performance on clean GSM8K or SVAMP problems (Tables 3 and 5, Sections 5.1 and 5.3).
- **Instructed prompting helps.** Adding "Feel free to ignore irrelevant information given in the questions." consistently improves performance for CoT, LtM, and Program. The improvement comes specifically from the instruction to ignore irrelevant information, not from the general task description "Solve grade school math problems." alone (Section 5.3). Instructed prompting with clean exemplars reaches comparable or better performance than uninstructed prompting with distractor exemplars for both CoT and LtM.

**Factor analysis (Table 4, Section 5.2.1):**

| Factor | More Distracting Condition | Less Distracting Condition |
|---|---|---|
| Topic | In-topic (e.g., CoT micro: 63.1) | Off-topic (e.g., CoT micro: 80.7) |
| Role name | Overlapping name (e.g., CoT micro: 68.3) | Non-overlapping name (e.g., CoT micro: 76.6) |
| Number range | In-range number (e.g., CoT micro: 70.2) | Out-of-range number (e.g., CoT micro: 74.6) |

All three factors affect distractibility, with **topic relevance** having the largest effect. For LtM, role overlap and number range have smaller effects on micro accuracy but larger effects on macro accuracy (Table 4).

**More exemplars can hurt robustness (Table 6, Section 5.4).** A 4-exemplar CoT prompt (the best-performing prompt on clean GSM8K) is more susceptible to distraction than the 1-exemplar prompt on problems with more than 2 reasoning steps (69.4% vs. 70.8% micro accuracy). With instructions, the gap on 2-step problems nearly disappears (79.2 vs. 79.0).

**Extension to DROP (Table 7, Section 5.5).** On the football split of DROP, where passages naturally contain irrelevant context, LtM + INST achieves the best accuracy (74.4% with code-davinci-002, 72.8% with text-davinci-003), confirming that instructed prompting and problem decomposition improve robustness beyond synthetic benchmarks.

**text-davinci-003 comparison (Table 3).** text-davinci-003 achieves better normalized micro accuracy than code-davinci-002 (e.g., CoT normalized micro: 85.4 vs. 76.2) but worse macro accuracy in most settings. text-davinci-003 is particularly susceptible to irrelevant context with role overlap: macro accuracy drops to 0% on problems with more than 2 reasoning steps for LtM (Table 4, Section 5.1).

---

## Limitations and Failure Modes

- **Single irrelevant sentence.** The benchmark adds only one irrelevant sentence per problem. Real-world inputs may contain multiple, interleaved distractors of varying types (Section 6).
- **Short reasoning chains.** Base problems require 2--7 steps, with 60% requiring only 2 steps. Longer reasoning tasks may exhibit different distractibility patterns.
- **GPT-3 family only.** Only code-davinci-002 and text-davinci-003 are evaluated. Generalization to other model families (open-weight models, newer instruction-tuned models) is not tested (Section 6).
- **Template-based distractors.** The irrelevant sentences are generated from templates (Table 9, Appendix A), which may not capture the full diversity of irrelevant information in practice.
- **No fine-tuning evaluation.** The paper focuses exclusively on prompting-based approaches. Li et al. (2022) showed that knowledge-aware fine-tuning can improve robustness, but this is not compared.
- **Macro accuracy remains low.** Even the best combination (LtM + SC) achieves only 45% macro accuracy, meaning more than half of base problems still have at least one distractor variant that causes failure (Table 3).
- **Prompt engineering sensitivity.** Only one exemplar is used in main experiments to avoid overfitting. The finding that 4 exemplars can hurt robustness (Table 6) raises concerns about prompt-design fragility.

---

## Conclusions

### Contributions

1. **GSM-IC benchmark for distractor robustness.** Introduced a 58,052-example arithmetic reasoning dataset with controlled irrelevant context, enabling systematic measurement of LLM distractibility across three orthogonal factors (topic, role overlap, number range) and three metrics (micro, macro, normalized accuracy) (Section 3).

2. **Characterization of prompting technique vulnerability.** Demonstrated that all investigated prompting techniques (CoT, 0-CoT, LtM, Program) are sensitive to irrelevant context, with macro accuracy below 30% for all methods with greedy decoding (Table 3, Section 5.1).

3. **Identification of effective mitigations.** Showed that self-consistency (+11 pp micro accuracy), exemplars with irrelevant context, and instructed prompting each substantially improve robustness, and that these mitigations are combinable without degrading clean-problem accuracy (Tables 3 and 5, Sections 5.1--5.3).

4. **Factor analysis of distractibility.** Identified that in-topic sentences, overlapping role names, and in-range numbers are the most distracting, providing a taxonomy of distractor difficulty (Table 4, Section 5.2.1).

5. **Problem decomposition aids robustness.** Established that Least-to-Most prompting is the most robust technique, with consistent performance across varying numbers of reasoning steps, suggesting that problem decomposition helps models focus on relevant information (Figure 4, Section 5.2.2).

### Implications

1. **More context can actively hurt performance.** Providing additional information to LLMs, even a single extraneous sentence, can substantially degrade reasoning accuracy. This motivates careful context curation in retrieval-augmented generation (RAG) pipelines and long-context applications. [Inference]

2. **Instruction-following enables behavioral modulation.** The effectiveness of a simple instruction to "ignore irrelevant information" suggests that language models can, to some extent, adjust their context-processing behavior through natural language directives (Section 5.3). [Inference]

3. **Prompt complexity may reduce robustness.** The finding that 4-exemplar prompts are more susceptible to distraction than 1-exemplar prompts (Table 6) suggests that additional prompt complexity can introduce overfitting that trades accuracy for robustness (Section 5.4). [Inference]

---

## Key Claims

1. **All prompting techniques are distractible.** No more than 18% of base problems (macro accuracy) are consistently solved across all distractor variants for any prompting technique with greedy decoding on code-davinci-002. The best macro accuracy without self-consistency is 25% (LtM + INST) and the best with SC is 45% (LtM + SC) (Table 3, Section 5.1). Status: **supported**.

2. **LtM is the most robust technique.** LtM achieves 18% macro accuracy vs. 6% for CoT and 5% for Program with code-davinci-002 (greedy). LtM micro accuracy is consistent across 2--7 reasoning steps, while CoT and Program degrade significantly on problems requiring 4+ steps (Table 3, Figure 4). Status: **supported**.

3. **Self-consistency achieves 99.7% recall.** With 20 samples, the correct answer appears among the sampled responses for 99.7% of GSM-IC problems with both CoT and LtM, and 96.5% with 0-CoT. SC improves overall micro accuracy by more than 11 percentage points (Table 3, Section 5.1). Status: **supported**.

4. **Exemplars with distractors improve robustness without hurting clean accuracy.** Using exemplars containing irrelevant context consistently outperforms clean exemplars on GSM-IC while maintaining or improving accuracy on GSM8K and SVAMP (Tables 3 and 5, Sections 5.1 and 5.3). Status: **supported**.

5. **Topic, role overlap, and number range all affect distractibility.** In-topic sentences are more distracting than off-topic (CoT micro: 63.1 vs. 80.7), overlapping roles more than non-overlapping (68.3 vs. 76.6), and in-range numbers more than out-of-range (70.2 vs. 74.6) (Table 4, Section 5.2.1). Status: **supported**.

6. **More exemplars can hurt robustness.** A 4-exemplar CoT prompt (66.3% on clean GSM8K dev) is consistently worse than a 1-exemplar prompt (60.3% on GSM8K dev) on GSM-IC problems with >2 steps (69.4% vs. 70.8%), despite achieving higher clean-problem accuracy (Table 6, Section 5.4). Status: **supported**.

---

## Open Questions

1. **Generalization to other model families.** The paper evaluates only GPT-3 family models (code-davinci-002 and text-davinci-003). How distractible are open-weight models, newer instruction-tuned models, and models trained with different alignment methods? Not yet addressed in this reference set.

2. **Multiple distractors.** How does performance degrade when multiple irrelevant sentences are added? Real-world inputs often contain many pieces of extraneous information. Not yet addressed.

3. **Fine-tuning vs. prompting for robustness.** Li et al. (2022) proposed knowledge-aware fine-tuning for robustness to irrelevant context. How do fine-tuning approaches compare to the prompting-based mitigations on GSM-IC? Not yet addressed.

4. **Interaction with context length.** How does distractibility interact with long-context settings where the volume of irrelevant information is much larger? Partially addressed by the 2025-11-context-length-hurts-performance reference, which shows that context length itself degrades performance even without irrelevant content.

---

## Core References and Why They Are Referenced

### Arithmetic Reasoning Benchmarks

- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems (GSM8K).* Provides the base dataset from which GSM-IC is constructed. The 100 base problems are sampled from the GSM8K training set.
- **Patel et al. (2021)** -- *Are NLP Models Really Able to Solve Simple Math Word Problems? (SVAMP).* Earlier work showing NLP models struggle with math problem variations. GSM-IC differs by adding irrelevant context rather than modifying problem structure. SVAMP is also used as a validation benchmark.
- **Dua et al. (2019)** -- *DROP: A Reading Comprehension Benchmark Requiring Discrete Reasoning.* Used to evaluate generalization of instructed prompting to a naturalistic setting where passages inherently contain irrelevant context.

### Prompting Techniques

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* Provides the CoT baseline. GSM-IC shows that CoT is vulnerable to irrelevant context despite its reasoning benefits.
- **Kojima et al. (2022)** -- *Large Language Models Are Zero-Shot Reasoners.* Provides the 0-CoT baseline ("Let's think step by step"), which achieves the lowest absolute accuracy on GSM-IC (29.0% micro).
- **Zhou et al. (2022)** -- *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models.* Provides LtM, the most robust prompting technique on GSM-IC. The paper follows Zhou et al.'s exemplar design and prompt structure.
- **Wang et al. (2022c)** -- *Self-Consistency Improves Chain of Thought Reasoning in Language Models.* Provides the self-consistency decoding strategy, the most effective single mitigation for distractibility. The 99.7% recall finding shows that correct reasoning paths exist but are not reliably selected by greedy decoding.
- **Chen et al. (2022)** -- *Program of Thoughts Prompting.* Provides the program-based prompting baseline that generates Python code to solve problems.

### Input Perturbation and Adversarial Evaluation

- **Jia & Liang (2017)** -- *Adversarial Examples for Evaluating Reading Comprehension Systems.* Shows that neural QA systems are affected by adversarial distracting sentences. GSM-IC extends this to arithmetic reasoning with LLMs.
- **Li et al. (2022)** -- *Large Language Models with Controllable Working Memory.* Proposes knowledge-aware fine-tuning on problems with counterfactual and irrelevant context. GSM-IC shows that prompting-based approaches (exemplars with distractors) can also mitigate distractibility without training.
- **Min et al. (2022)** -- *Rethinking the Role of Demonstrations in In-Context Learning.* Shows that label correctness in exemplars matters less than format, raising questions about how models use context.
- **Madaan & Yazdanbakhsh (2022)** -- *Text and Patterns: For Effective Chain of Thought, It Takes Two to Tango.* Shows that entity correctness in CoT prompts matters more than numerical correctness, complementing GSM-IC's finding that role name overlap is a key factor in distractibility.

### Models

- **Brown et al. (2020)** -- *Language Models Are Few-Shot Learners (GPT-3).* Foundation for the models evaluated (code-davinci-002 and text-davinci-003 are GPT-3 family variants).
- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback.* text-davinci-003 is trained with RLHF following this approach, and achieves better normalized micro accuracy but worse macro accuracy than code-davinci-002.
