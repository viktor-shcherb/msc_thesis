---
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
authors: "Wei, Wang, Schuurmans, Bosma, Ichter, Xia, Chi, Le, Zhou"
year: 2022
venue: "NeurIPS 2022"
paper_type: conference-paper
categories: ["in-context-learning", "reasoning-evaluation"]
scope: ["chain-of-thought prompting", "emergent reasoning abilities", "few-shot prompting for reasoning"]
benchmarks_used: ["gsm8k", "svamp", "asdiv", "mawps", "csqa", "strategyqa"]
models_introduced: []
models_evaluated: ["palm-540b", "lamda-137b", "gpt-3-175b"]
key_claims:
  - id: C1
    claim: "Chain-of-thought prompting is an emergent ability of model scale, only yielding performance gains with models of ~100B parameters"
    evidence: "Figure 4, Table 2, Section 3.2"
    status: supported
    scope: "LaMDA, GPT-3, PaLM model families; arithmetic, commonsense, and symbolic reasoning tasks"
    magnitude: "Flat or negative gains below ~100B; GSM8K +39.0 points for PaLM 540B, +31.3 for GPT-3 175B"
  - id: C2
    claim: "PaLM 540B with chain-of-thought prompting achieves 56.9% on GSM8K, surpassing finetuned GPT-3 with a verifier (55%)"
    evidence: "Figure 2, Table 1, Section 3.2"
    status: supported
    scope: "GSM8K benchmark, greedy decoding, 8 manually written exemplars"
    magnitude: "56.9% vs 55% prior best (finetuned GPT-3 + verifier), vs 17.9% standard prompting"
  - id: C3
    claim: "Chain-of-thought prompting has larger performance gains for more complicated problems and minimal gains on easy one-step problems"
    evidence: "Figure 4, Table 3, Section 3.2"
    status: supported
    scope: "MAWPS subtasks (SingleOp, SingleEq, AddSub, MultiArith) and GSM8K; PaLM 540B"
    magnitude: "GSM8K +39.0 vs SingleOp +0.0 for PaLM 540B; MultiArith +52.5 vs AddSub -2.0"
  - id: C4
    claim: "The benefit of chain-of-thought prompting comes from natural language reasoning steps, not just variable computation or equation extraction"
    evidence: "Figure 5, Table 6, Section 3.3"
    status: supported
    scope: "GSM8K, LaMDA 137B and PaLM 540B; three ablation variants"
    magnitude: "LaMDA 137B GSM8K: CoT 14.3% vs equation-only 5.4%, variable-compute 6.4%, reasoning-after-answer 6.1%, standard 6.5%"
  - id: C5
    claim: "Chain-of-thought prompting facilitates length generalization to longer sequences on symbolic reasoning tasks"
    evidence: "Figure 8, Table 5, Section 5"
    status: supported
    scope: "PaLM 540B; last-letter concatenation and coin-flip tasks; 2-step exemplars tested on 3- and 4-step inputs"
    magnitude: "Last letter concat OOD (4): 63.0% CoT vs 0.0% standard; Coin flip OOD (4): 90.2% CoT vs 54.8% standard"
  - id: C6
    claim: "Chain-of-thought prompting is robust to different annotators, exemplar orders, and language models"
    evidence: "Figure 6, Table 6, Table 7, Section 3.4"
    status: supported
    scope: "LaMDA 137B on GSM8K, MAWPS, commonsense, and symbolic tasks; 3 annotators, multiple exemplar sets"
    magnitude: "All annotators outperform standard prompting by large margin; variance: coin flip 99.6% (A) vs 71.4% (C)"
cross_references:
  - target: 2019-02-gpt-2-language-models-unsupervised
    type: extends
    detail: "Chain-of-thought prompting extends GPT-2's zero-shot paradigm by eliciting reasoning through intermediate natural language steps"
  - target: 2023-07-gsm-ic-irrelevant-context
    type: extended-by
    detail: "GSM-IC tests whether chain-of-thought reasoning is robust to irrelevant context added to math problems"
  - target: 2025-04-retrieval-head-long-context-factuality
    type: complementary
    detail: "Wu et al. show that CoT reasoning heavily depends on retrieval heads because the model must refer back to input information during multi-step reasoning; masking retrieval heads drops GSM8K CoT accuracy from 45.1% to 2.0%"
  - target: 2025-01-kimi-k1.5-scaling-rl
    type: extended-by
    detail: "Kimi k1.5 extends chain-of-thought from prompting to RL training, scaling CoT context to 128k tokens and achieving 96.2% on MATH-500 and 77.5% on AIME 2024"
  - target: 2020-12-gpt-3-few-shot-learners
    type: extends
    detail: "Extends GPT-3's few-shot prompting paradigm by adding intermediate reasoning steps, unlocking reasoning capabilities that standard few-shot prompting could not achieve"
  - target: 2024-08-scaling-llm-test-time-compute
    type: extended-by
    detail: "Builds on chain-of-thought as a mechanism for using test-time compute, studying how to optimally scale test-time computation for math reasoning"
  - target: 2024-12-lost-in-the-middle-in-between
    type: complementary
    detail: "Tests CoT prompting as a mitigation for positional bias in multi-hop QA, finding it helps instruction-tuned models (2-6 pp gain) but harms non-instruction-tuned models"
  - target: 2026-01-longbench-pro
    type: complementary
    detail: "LongBench Pro operationalizes non-thinking vs thinking prompt templates at long context scale and finds large gains mainly for models with native reasoning training"
open_questions:
  - question: "Does chain of thought emulate actual reasoning, or is it a surface-level pattern that mimics reasoning?"
    addressed_by: null
  - question: "How can chain-of-thought reasoning be induced in smaller models (<100B parameters)?"
    addressed_by: null
  - question: "How can the factual correctness of generated reasoning chains be improved?"
    addressed_by: null
  - question: "Can chain-of-thought prompting be combined with self-consistency (majority voting) to further improve performance?"
    addressed_by: null
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**Authors:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou (Google Research, Brain Team)
**Date:** NeurIPS 2022, arXiv:2201.11903

---

## Core Research Problem

Scaling up language model size improves performance on many NLP tasks, but has not proved sufficient for challenging reasoning tasks such as arithmetic, commonsense, and symbolic reasoning (Rae et al., 2021). Two prior approaches each have key limitations. First, **rationale-augmented training** (Ling et al., 2017; Cobbe et al., 2021) generates natural language intermediate steps but requires expensive annotation of large training datasets with high-quality rationales. Second, **standard few-shot prompting** (Brown et al., 2020) avoids finetuning but works poorly on tasks requiring multi-step reasoning, with performance often not improving substantially with model scale.

The core challenge is: **how to unlock the reasoning abilities of large language models without task-specific finetuning or large annotated datasets, using only a few demonstrations at inference time.**

---

## Problem Solutions

The paper proposes **chain-of-thought prompting**, a method that augments few-shot exemplars with intermediate natural language reasoning steps. The key idea is simple: instead of prompting with (input, output) pairs, prompt with (input, chain of thought, output) triples.

1. **Chain of thought as intermediate steps.** Each exemplar includes a series of natural language reasoning steps that decompose the problem before arriving at the final answer (Figure 1).

2. **Few-shot prompting only.** The method requires no finetuning, no gradient updates, and no large training datasets -- only a handful of manually written exemplars (typically 8) with chain-of-thought annotations.

3. **Emergent ability at scale.** Chain-of-thought reasoning emerges naturally in sufficiently large language models (~100B+ parameters) when demonstrations are provided.

---

## Approach Details

### Method

Chain-of-thought prompting modifies standard few-shot prompting by augmenting each exemplar's answer with intermediate reasoning steps. For a math word problem like "The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?", instead of answering "The answer is 27" (incorrect), the chain of thought reads: "The cafeteria had 23 apples originally. They used 20 to make lunch. So they had 23 - 20 = 3. They bought 6 more apples, so they have 3 + 6 = 9. The answer is 9" (Figure 1).

The approach has four properties (Section 2):
1. It allows models to **decompose multi-step problems** into intermediate steps, allocating additional computation to harder problems.
2. It provides an **interpretable window** into the model's reasoning, enabling debugging of incorrect reasoning paths.
3. It is applicable to **any task solvable via language-based reasoning** (math, commonsense, symbolic manipulation).
4. It can be **elicited from off-the-shelf models** simply by including chain-of-thought demonstrations in few-shot exemplars.

### Key Technical Components

**Prompt construction.** For arithmetic reasoning, 8 few-shot exemplars with manually written chains of thought are used across all benchmarks (except AQuA, which uses 4 exemplars from the training set). The same set of 8 exemplars is reused across GSM8K, SVAMP, ASDiv, and MAWPS. No prompt engineering or optimization is performed (Section 3.1, Appendix Table 20).

**Greedy decoding.** All results use greedy decoding from the language model. Follow-up work (Wang et al., 2022a) shows that taking the majority final answer over many sampled generations (self-consistency) further improves chain-of-thought prompting (Section 3.1).

**External calculator.** An optional post-hoc enhancement applies a Python calculator to equations in the generated chain of thought. This improves GSM8K performance from 56.9% to 58.6% for PaLM 540B (Table 1, Appendix B).

### Experimental Setup

**Arithmetic reasoning benchmarks (Section 3.1):**
- GSM8K (Cobbe et al., 2021): 1,319 grade school math word problems
- SVAMP (Patel et al., 2021): 1,000 math word problems with varying structures
- ASDiv (Miao et al., 2020): 2,096 diverse math word problems
- AQuA (Ling et al., 2017): 254 algebraic word problems (multiple choice)
- MAWPS (Koncel-Kedziorski et al., 2016): aggregated benchmark with SingleOp, SingleEq, AddSub, and MultiArith subsets

**Commonsense reasoning benchmarks (Section 4):**
- CSQA (Talmor et al., 2019): commonsense questions requiring prior knowledge
- StrategyQA (Geva et al., 2021): multi-hop strategy questions
- Date Understanding, Sports Understanding (BIG-bench): specialized evaluation sets
- SayCan (Ahn et al., 2022): mapping natural language instructions to robot action sequences

**Symbolic reasoning tasks (Section 5):**
- Last letter concatenation: concatenate last letters of words in a name
- Coin flip: track coin state after a sequence of flips/non-flips

**Language models evaluated:**
- GPT-3: text-ada-001 (350M), text-babbage-001 (1.3B), text-curie-001 (6.7B), text-davinci-002 (175B)
- LaMDA: 422M, 2B, 8B, 68B, 137B parameters
- PaLM: 8B, 62B, 540B parameters
- UL2 20B
- Codex (code-davinci-002)

### Key Results

**Arithmetic reasoning (accuracy %, Table 1):**

| Model | Prompting | GSM8K | SVAMP | ASDiv | AQuA | MAWPS |
|---|---|---|---|---|---|---|
| Prior best (finetuning) | N/A | 55.0 | 57.4 | 75.3 | 37.9 | 88.4 |
| PaLM 540B | Standard | 17.9 | 69.4 | 72.1 | 25.2 | 79.2 |
| PaLM 540B | Chain of thought | **56.9** (+39.0) | **79.0** (+9.6) | 73.9 (+1.8) | 35.8 (+10.6) | **93.3** (+14.2) |
| GPT-3 175B | Standard | 15.6 | 65.7 | 70.3 | 24.8 | 72.7 |
| GPT-3 175B | Chain of thought | 46.9 (+31.3) | 68.9 (+3.2) | 71.3 (+1.0) | 35.8 (+11.0) | 87.1 (+14.4) |
| LaMDA 137B | Standard | 6.5 | 29.5 | 40.1 | 25.5 | 43.2 |
| LaMDA 137B | Chain of thought | 14.3 (+7.8) | 37.5 (+8.0) | 46.6 (+6.5) | 20.6 (-4.9) | 57.9 (+14.7) |

- PaLM 540B with chain-of-thought prompting achieves **new state of the art on GSM8K** (56.9%), surpassing finetuned GPT-3 with a verifier (55%) using only 8 exemplars and no finetuning (Figure 2).
- Chain-of-thought prompting achieves **new state of the art on SVAMP and MAWPS** with PaLM 540B.
- Performance gains are largest for harder multi-step problems (GSM8K: +39.0 for PaLM 540B) and smallest for easy single-step problems (SingleOp: +0.0 for PaLM 540B, Table 3).

**Commonsense reasoning (accuracy %, PaLM, Table 4):**

| Benchmark | PaLM 540B Standard | PaLM 540B CoT | Prior Best |
|---|---|---|---|
| CSQA | 78.1 | 79.9 | 91.2 |
| StrategyQA | 68.6 | **77.8** | 69.4 |
| Date Understanding | 49.0 | 65.3 | -- |
| Sports Understanding | 80.5 | **95.4** | 84.0 (human) |
| SayCan | 80.8 | 91.7 | -- |

- Chain-of-thought prompting outperforms prior state of the art on StrategyQA (77.8% vs. 69.4%) and surpasses an unaided sports enthusiast on Sports Understanding (95.4% vs. 84%) (Section 4).
- Gain on CSQA is minimal (+1.8), suggesting chain of thought is less helpful when a task does not require multi-step reasoning.

**Symbolic reasoning (accuracy %, PaLM 540B, Table 5):**

| Task | Standard (in-domain) | CoT (in-domain) | Standard (OOD) | CoT (OOD) |
|---|---|---|---|---|
| Last Letter Concat (2 → 4) | 7.6 | 99.4 | 0.0 | 63.0 |
| Coin Flip (2 → 4) | 98.1 | 100.0 | 54.8 | 90.2 |

- Chain-of-thought prompting achieves near-perfect in-domain performance and **facilitates length generalization** to OOD inputs with more steps than shown in exemplars (Figure 8).

### Ablation Study

Three ablations on GSM8K (Figure 5, Table 6, LaMDA 137B and PaLM 540B) isolate what makes chain-of-thought prompting effective:

1. **Equation only.** Prompting the model to output only a mathematical equation before the answer. This does not help on GSM8K (5.4% vs. 6.5% standard for LaMDA 137B), implying the natural language reasoning steps are necessary for semantically complex problems. It does help on simpler one-step or two-step problems (Section 3.3).

2. **Variable compute only.** Prompting the model to output a sequence of dots equal to the equation length, providing the same number of intermediate tokens without reasoning content. This performs about the same as baseline (6.4% for LaMDA 137B), ruling out variable computation alone as the explanation (Section 3.3).

3. **Chain of thought after answer.** Providing the chain of thought only after the final answer, testing whether the benefit is merely from activating relevant knowledge. This also performs about the same as baseline (6.1% for LaMDA 137B), confirming that the sequential reasoning before the answer is essential (Section 3.3).

### Error Analysis

Manual analysis of 50 correct and 50 incorrect model outputs from LaMDA 137B on GSM8K (Appendix D):

**Correct outputs (50 examples):** 49 of 50 had logically and mathematically correct chains of thought. Only 1 arrived at the correct answer by coincidence through incorrect reasoning.

**Incorrect outputs (50 examples):**
- 8% had only calculator errors (correct reasoning, wrong arithmetic)
- 16% had symbol mapping errors (correct logic but wrong numbers plugged in)
- 22% were missing one reasoning step
- 54% had major errors in semantic understanding or coherence

Scaling from PaLM 62B to 540B fixed a substantial portion of errors in all categories: 6 of 20 semantic understanding errors, 12 of 18 one-step-missing errors, and 4 of 7 other errors (Figure 9, Appendix A.1).

---

## Limitations and Failure Modes

- **Not actual reasoning.** Whether the model is actually "reasoning" or performing sophisticated pattern matching remains an open question. The authors explicitly note that chain of thought "emulates the thought processes of human reasoners" but do not claim the model is reasoning (Section 6).

- **No guarantee of correct reasoning paths.** Generated chains of thought are not always factually correct. Incorrect chains can lead to both wrong answers and accidentally correct answers, especially on multiple-choice and binary classification tasks (Appendix D.1, D.2).

- **Only works at large scale.** Chain-of-thought prompting is an emergent ability requiring models of ~100B+ parameters. For smaller models, it actually hurts performance -- small models produce "fluent but illogical chains of thought" (Section 3.2, Figure 4, Table 2).

- **Minimal gain on simple tasks.** On easy one-step problems (e.g., MAWPS SingleOp), chain-of-thought prompting provides negligible or no improvement (Table 3).

- **Minimal gain on some commonsense tasks.** On CSQA, gain is only +1.8 points for PaLM 540B, suggesting chain of thought is less helpful when the task does not inherently require multi-step reasoning (Table 4, Section 4).

- **Sensitivity to prompt construction.** While robust across annotators and exemplar orders for arithmetic, there is notable variance on some tasks (e.g., coin flip: 99.6% for Annotator A vs. 71.4% for Annotator C, Table 7). Some tasks require careful prompt engineering (Section 3.4, Appendix A.2).

- **Annotation cost for finetuning.** While the cost of writing 8 chain-of-thought exemplars is minimal, scaling to finetuning-sized datasets of rationales would be prohibitively expensive (Section 6).

- **[Inferred]** No evaluation on non-English languages, limiting the generalizability of chain-of-thought prompting claims to multilingual settings.

- **[Inferred]** All experiments use greedy decoding; the interaction between chain-of-thought prompting and sampling strategies (temperature, top-k, nucleus sampling) is not systematically explored beyond the self-consistency follow-up mention (Section 3.1).

### Scope and Comparability

- **What was not tested:** Models smaller than 350M and larger than 540B; non-English languages; tasks beyond arithmetic, commonsense, and symbolic reasoning (e.g., machine translation, summarization, code generation); open-ended generation tasks; sampling strategies other than greedy decoding; prompt optimization or automatic chain-of-thought generation; models trained on code-heavy data beyond Codex.
- **Comparability notes:** The prior best results on arithmetic benchmarks (GSM8K, SVAMP, MAWPS) are from finetuned models with task-specific training data, making direct comparison with a prompting-only approach imprecise -- the methods differ in compute allocation (training-time vs. inference-time), data requirements, and generalizability. The StrategyQA prior best is from a single-model leaderboard entry as of May 2022. BIG-bench tasks (Date Understanding, Sports Understanding) lack established prior baselines for comparison.

---

## Conclusions

### Contributions

1. **Chain-of-thought prompting as a general method.** Demonstrates that augmenting few-shot exemplars with intermediate reasoning steps significantly improves performance on arithmetic, commonsense, and symbolic reasoning tasks without any finetuning (Sections 3--5).

2. **Emergent reasoning through scale.** Establishes that chain-of-thought reasoning is an emergent ability of model scale: it does not improve performance for small models but yields large gains at ~100B+ parameters, turning flat scaling curves into steeply increasing ones (Figure 4, Section 3.2).

3. **State-of-the-art on GSM8K without finetuning.** PaLM 540B with 8 chain-of-thought exemplars achieves 56.9% on GSM8K, surpassing finetuned GPT-3 with a verifier (55%), demonstrating that prompting alone can compete with task-specific finetuning (Figure 2, Table 1).

4. **Ablation evidence for natural language reasoning.** Ablations show that the benefit is not from variable computation or knowledge activation alone, but specifically from the sequential natural language reasoning steps (Figure 5, Section 3.3).

5. **Length generalization on symbolic tasks.** Chain-of-thought prompting enables language models to generalize to input sequences longer than those seen in the few-shot exemplars for symbolic reasoning tasks (Figure 8, Section 5).

### Implications

1. **Standard prompting underestimates LLM capabilities.** The results suggest that standard few-shot prompting provides only a lower bound on what large language models can do. Chain-of-thought prompting expands the set of tasks these models can solve successfully (Section 6). [Inference: this implies that evaluation of LLMs should consider prompting strategies, not just model size.]

2. **Prompting as an alternative to finetuning for reasoning.** Achieving state-of-the-art on GSM8K without finetuning suggests that for some reasoning tasks, prompting strategies may substitute for expensive task-specific training, provided models are sufficiently large (Section 1).

3. **Natural language as a reasoning medium.** The success of chain-of-thought reasoning in natural language (vs. equations or formal representations) suggests that language models can leverage the structure of natural language to perform multi-step reasoning, making the approach broadly applicable to any task humans can solve via language (Section 2).

---

## Key Claims

1. **C1: Emergent ability of model scale.** Chain-of-thought prompting does not improve performance for small models and only yields gains with models of ~100B parameters. For smaller models, it can actually hurt performance by producing fluent but illogical chains of thought (Figure 4, Table 2, Section 3.2). Tested across 3 model families (LaMDA, GPT-3, PaLM) at 4--5 scales each, on 5 arithmetic benchmarks (strong evidence). Status: **supported**.

2. **C2: State-of-the-art on GSM8K.** PaLM 540B with chain-of-thought prompting achieves 56.9% accuracy on GSM8K, surpassing finetuned GPT-3 with a verifier (55%) and standard prompting (17.9%) (Figure 2, Table 1). Single model, greedy decoding, 8 exemplars (limited evidence for robustness of the exact number; LaMDA results averaged over 5 seeds). Status: **supported**.

3. **C3: Larger gains on harder problems.** Chain-of-thought prompting has larger performance gains for more complicated multi-step problems (GSM8K: +39.0) and minimal gains on easy single-step problems (MAWPS SingleOp: +0.0 for PaLM 540B) (Figure 4, Table 3, Section 3.2). Demonstrated across 4 MAWPS subtasks stratified by difficulty plus GSM8K, for all 3 model families (strong evidence). Status: **supported**.

4. **C4: Natural language reasoning is the key ingredient.** Ablations show that equation-only prompting, variable-compute-only prompting, and reasoning-after-answer prompting all perform near the standard prompting baseline on GSM8K, while chain-of-thought prompting substantially outperforms all of them (Figure 5, Table 6, Section 3.3). Ablation on LaMDA 137B and PaLM 540B across 4 arithmetic and 4 commonsense/symbolic datasets (moderate evidence -- 2 model sizes, multiple datasets, but single run per configuration with standard deviations from exemplar ordering only). Status: **supported**.

5. **C5: Length generalization on symbolic tasks.** Chain-of-thought prompting enables PaLM 540B to generalize from 2-step exemplars to 4-step test inputs on last-letter concatenation (63.0% OOD vs. 0.0% standard) and coin flip (90.2% OOD vs. 54.8% standard) (Figure 8, Table 5, Section 5). Tested on 2 synthetic tasks for PaLM and LaMDA at multiple scales (moderate evidence -- only 2 toy tasks). Status: **supported**.

6. **C6: Robustness across annotators and models.** Chain-of-thought prompting outperforms standard prompting across all tested annotators (A, B, C), exemplar sets (including exemplars from GSM8K training set), and language models (LaMDA, GPT-3, PaLM), though with notable variance on some tasks (Figure 6, Tables 6--7, Section 3.4). LaMDA 137B tested with 3 annotators + 3 GSM8K training set exemplar sets across 8 datasets; standard deviations from 5 random exemplar orderings (strong evidence for arithmetic; moderate for commonsense/symbolic due to single model size in robustness analysis). Status: **supported**.

---

## Open Questions

1. **Does chain of thought reflect actual reasoning?** The paper explicitly leaves open whether the neural network is "actually reasoning" or performing sophisticated pattern matching (Section 6). Not addressed.

2. **How can chain-of-thought reasoning be induced in smaller models?** The emergence of chain-of-thought reasoning only at ~100B+ parameters makes it costly for real-world deployment. The paper suggests this as future work (Section 6). Not directly addressed, though subsequent work on knowledge distillation and instruction tuning has made smaller models capable of chain-of-thought reasoning.

3. **How can the factual correctness of generated chains of thought be improved?** Generated reasoning paths are not guaranteed to be correct. The paper notes this as an open direction (Section 6, Appendix D). Not addressed.

4. **Can chain-of-thought prompting be combined with self-consistency?** The paper mentions follow-up work by Wang et al. (2022a) showing that majority voting over sampled chains of thought further improves performance (Section 3.1). This has been validated in subsequent work.

---

## Core References and Why They Are Referenced

### Foundations

- **Brown et al. (2020)** -- *Language Models Are Few-Shot Learners.* Establishes the few-shot prompting paradigm that chain-of-thought prompting extends. The paper's baseline "standard prompting" follows this approach of providing input-output exemplars.

- **Ling et al. (2017)** -- *Program Induction by Rationale Generation.* Pioneers the idea of using natural language rationales to solve math word problems through intermediate steps, via training from scratch. Chain-of-thought prompting achieves the same effect through prompting alone.

- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems.* Creates the GSM8K benchmark and demonstrates finetuning with rationale-augmented data. Chain-of-thought prompting with PaLM 540B surpasses their finetuned GPT-3 with verifier (56.9% vs. 55%).

### Models Evaluated

- **Thoppilan et al. (2022)** -- *LaMDA: Language Models for Dialog Applications.* Provides the LaMDA model family (422M--137B parameters) used as one of three primary model families in evaluation.

- **Chowdhery et al. (2022)** -- *PaLM: Scaling Language Modeling with Pathways.* Provides PaLM (8B, 62B, 540B), the model that achieves the strongest chain-of-thought results including state-of-the-art on GSM8K.

- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback.* Provides the InstructGPT models (GPT-3 text-davinci-002) used in evaluation.

### Emergent Abilities and Scaling

- **Wei et al. (2022b)** -- *Emergent Abilities of Large Language Models.* Provides the conceptual framework of emergent abilities that chain-of-thought reasoning exemplifies: capabilities that appear unpredictably at certain model scales.

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Establishes scaling laws showing improved performance with model size, which chain-of-thought prompting extends to reasoning tasks where standard scaling was insufficient.

### Intermediate Reasoning Steps

- **Nye et al. (2021)** -- *Show Your Work: Scratchpads for Intermediate Computation with Language Models.* Most closely related prior work on using intermediate steps, showing that language models can predict program outputs via line-by-line intermediate predictions. Chain-of-thought generalizes this from domain-specific primitives to natural language.

### Evaluation Benchmarks

- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems.* Provides the GSM8K benchmark.

- **Patel et al. (2021)** -- *Are NLP Models Really Able to Solve Simple Math Word Problems?* Provides the SVAMP benchmark.

- **Talmor et al. (2019)** -- *CommonsenseQA.* Provides the CSQA commonsense reasoning benchmark.

- **Geva et al. (2021)** -- *Did Aristotle Use a Laptop?* Provides the StrategyQA multi-hop reasoning benchmark, where chain-of-thought prompting with PaLM 540B achieves new state of the art (77.8% vs. 69.4%).

### Follow-up Work

- **Wang et al. (2022a)** -- *Self-Consistency Improves Chain of Thought Reasoning in Language Models.* Shows that sampling multiple chains of thought and taking the majority final answer further improves chain-of-thought prompting performance, mentioned as concurrent/follow-up work.
