# Large Language Models Can Be Easily Distracted by Irrelevant Context

**Authors:** Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael Schärli, Denny Zhou (Google Research)
**Date:** July 2023, ICML 2023, PMLR 202:31210--31227 (arXiv:2302.00093)

---

## Core Research Problem

Large language models have achieved strong performance on various NLP tasks, but existing benchmarks predominantly evaluate models on inputs where **all information in the context is relevant** to the task. In real-world settings, inputs frequently contain irrelevant or extraneous information -- documents with tangential details, user queries with unnecessary context, or problem descriptions with distracting numbers and names. Prior work on arithmetic reasoning benchmarks such as GSM8K (Cobbe et al., 2021) tests problem-solving ability but does not assess how models handle the presence of information that should be ignored. This gap is critical because practical deployments of LLMs (e.g., for document QA, tool-assisted reasoning, or agentic tasks) inevitably expose models to noisy, partially relevant inputs. **The core challenge is: how robust are large language models to irrelevant context in their input, and what prompting strategies can mitigate the resulting performance degradation?**

---

## Problem Solutions

The paper introduces a controlled benchmark and systematic analysis of LLM distractibility. The key contributions are:

1. **GSM-IC benchmark.** Grade-School Math with Irrelevant Context -- an arithmetic reasoning dataset built on GSM8K that adds irrelevant sentences to problem descriptions, systematically varying three distractor factors: topic relevance, role name overlap, and number range similarity.
2. **Distractibility characterization.** Evaluation of multiple prompting techniques (Chain-of-Thought, Least-to-Most, Zero-shot CoT, Program-based) on GSM-IC, showing that macro accuracy drops below 30% when irrelevant context is introduced.
3. **Factor analysis.** Identification of which properties of irrelevant information are most distracting: in-topic sentences, overlapping role names, and in-range numbers cause the largest performance drops.
4. **Mitigation strategies.** Self-consistency decoding, exemplars containing irrelevant context, and explicit instructions to ignore irrelevant information each substantially improve robustness.

---

## Approach Details

### Method

**GSM-IC construction.** The benchmark starts from 100 base problems selected from the GSM8K training set and generates distractor variants by inserting one irrelevant sentence into each problem description. Each irrelevant sentence is constructed by combining three binary factors:

1. **Topic:** *In-topic* (same domain as the problem, e.g., a shopping problem gets an irrelevant shopping sentence) vs. *off-topic* (unrelated domain).
2. **Role:** *Overlap* (the irrelevant sentence uses a character name that appears in the original problem) vs. *no overlap* (introduces a new name).
3. **Number range:** *In-range* (the irrelevant number has a similar magnitude to numbers in the problem) vs. *out-of-range* (a clearly different magnitude).

This yields 2 x 2 x 2 = 8 distractor conditions per base problem. With additional sentence templates, the full dataset contains **58,052 total examples**, with a uniformly sampled evaluation subset **GSM-IC-4K** of 4,000 examples.

**Metrics.** Three accuracy measures capture different aspects of robustness:

- **Micro accuracy:** Average accuracy across all GSM-IC examples (standard metric).
- **Macro accuracy:** Fraction of base problems for which the model answers correctly across *all* distractor variants. This is the strictest measure -- a base problem counts as correct only if every irrelevant-context variant is solved correctly.
- **Normalized accuracy:** Micro accuracy on GSM-IC divided by accuracy on the original (clean) base problems, measuring the relative degradation caused by irrelevant context.

### Key Technical Components

**Prompting techniques evaluated:**

| Technique | Description |
|---|---|
| Standard prompting | Direct question-answer exemplars |
| Chain-of-Thought (CoT) | Step-by-step reasoning chains in exemplars (Wei et al., 2022) |
| Zero-shot CoT | Appending "Let's think step by step" without exemplars (Kojima et al., 2022) |
| Least-to-Most (LtM) | Decomposing problems into subproblems, solving sequentially (Zhou et al., 2023) |
| Program prompting | Generating Python code to solve the problem (Chen et al., 2022) |

**Mitigation strategies:**

1. **Self-consistency (SC):** Sample multiple outputs (up to 20) and take the majority vote (Wang et al., 2023). This is the most effective single mitigation.
2. **Exemplars with irrelevant context (IrrCtx):** Include irrelevant sentences in the few-shot exemplars themselves, teaching the model by example to ignore extraneous information.
3. **Explicit instruction (INST):** Prepend "Feel free to ignore irrelevant information given in the questions" to the prompt.

These mitigations are combinable (e.g., LTM + SC, LTM + INST w/ IrrCtx).

### Experimental Setup

**Models:**

| Model | Type | Provider |
|---|---|---|
| code-davinci-002 (Codex) | Code-specialized GPT-3 variant | OpenAI |
| text-davinci-003 | Instruction-tuned GPT-3 variant | OpenAI |
| ChatGPT (gpt-3.5-turbo) | Chat-optimized model | OpenAI |

**Evaluation:** GSM-IC-4K (4,000 examples uniformly sampled across distractor conditions) for the main experiments. Full GSM-IC (58,052 examples) for factor analysis. Greedy decoding for base experiments; temperature sampling for self-consistency.

### Key Results

**Base performance on clean GSM8K problems (no irrelevant context):**

| Model | CoT | LtM |
|---|---|---|
| text-davinci-003 | 80.0% | 81.0% |
| code-davinci-002 | ~80% | ~80% |

**Performance with irrelevant context (GSM-IC):**

The introduction of a single irrelevant sentence causes dramatic drops. Across prompting techniques, **macro accuracy falls below 30%** -- meaning fewer than 30% of base problems are consistently solved correctly across all distractor variants.

**Leaderboard -- micro accuracy on GSM-IC (code-davinci-002):**

| Method | Micro Accuracy |
|---|---|
| LTM + Self-Consistency (20 samples) | 93.4% |
| LTM + INST w/ IrrCtx | 82.8% |
| LTM w/ IrrCtx | 80.7% |
| LTM + INST | 80.6% |
| LTM (baseline) | 77.5% |

- **Least-to-Most prompting** achieves the highest baseline robustness among non-ensemble methods, approximately double the macro accuracy of Chain-of-Thought. Problem decomposition helps the model focus on relevant subproblems.
- **Self-consistency** is the most effective single mitigation, boosting micro accuracy by over 11 percentage points and achieving **99.7% recall** of correct answers within 20 samples.
- **Exemplars with irrelevant context** improve performance without degrading clean-problem accuracy, demonstrating that models can learn to disregard extraneous information through in-context examples.

**Factor analysis -- which distractor properties are most distracting:**

| Factor | More Distracting Condition | Less Distracting Condition |
|---|---|---|
| Topic | In-topic | Off-topic |
| Role | Overlapping name | Non-overlapping name |
| Number range | In-range number | Out-of-range number |

- **Role name overlap** and **in-range numbers** have the strongest effect on model sensitivity. When the irrelevant sentence uses a character name from the problem and a number of similar magnitude, models are most likely to incorporate the irrelevant information into their reasoning.
- **Topic relevance** also plays a role but is secondary to role and number overlap.

### Limitations

- The benchmark uses a **single irrelevant sentence** per problem. Real-world inputs may contain multiple, interleaved distractors of varying types.
- Experiments are limited to **short reasoning chains** (GSM8K problems requiring 2--8 steps). Longer reasoning tasks may exhibit different distractibility patterns.
- Only **GPT-3 family models** (code-davinci-002, text-davinci-003, ChatGPT) are evaluated. Generalization to other model families is not tested.
- No **supervised fine-tuning** or **out-of-distribution evaluations** are included -- the paper focuses exclusively on prompting-based approaches.
- The distractor design is **template-based**, which may not capture the full diversity of irrelevant information encountered in practice.

---

## Conclusions

1. **LLMs are highly distractible by irrelevant context.** Adding a single irrelevant sentence to arithmetic reasoning problems drops macro accuracy below 30% across all prompting techniques tested, demonstrating a fundamental vulnerability in how models process input context.

2. **Problem decomposition improves robustness.** Least-to-Most prompting, which decomposes problems into subproblems, achieves approximately double the macro accuracy of Chain-of-Thought. Structured reasoning helps models focus on relevant information.

3. **Self-consistency is the most effective mitigation.** Sampling multiple outputs and taking a majority vote boosts micro accuracy by over 11 percentage points and achieves 99.7% recall of correct answers within 20 samples. This suggests that correct reasoning paths exist but are not reliably selected by greedy decoding.

4. **In-context examples of irrelevant information transfer robustness.** Including irrelevant sentences in few-shot exemplars teaches models to ignore extraneous context, without degrading performance on clean problems.

5. **Distractor similarity drives distractibility.** Irrelevant information that is topically related, uses overlapping character names, or contains numbers of similar magnitude to the problem causes the largest performance drops. Models struggle most when irrelevant information is superficially similar to relevant information.

6. **Explicit instructions help but do not solve the problem.** Adding "ignore irrelevant information" to the prompt yields gains, but models remain substantially degraded compared to clean-input performance, indicating that instruction-following alone is insufficient.

7. **Implications for long-context and retrieval-augmented settings.** The findings demonstrate that providing more context to LLMs can actively hurt performance when that context includes irrelevant information, motivating careful context curation in RAG pipelines and long-context applications.

---

## Core References and Why They Are Referenced

### Arithmetic Reasoning Benchmarks

- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems (GSM8K).* Provides the base dataset from which GSM-IC is constructed. GSM8K's 100 training problems serve as the foundation for generating irrelevant-context variants.
- **Patel et al. (2021)** -- *Are NLP Models Really Able to Solve Simple Math Word Problems?* Earlier work showing that NLP models struggle with math problems containing superficially similar but irrelevant numerical information. GSM-IC extends this to LLMs with a more systematic distractor design.

### Prompting Techniques

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* Provides the Chain-of-Thought prompting baseline. GSM-IC shows that CoT is vulnerable to irrelevant context despite its reasoning benefits.
- **Kojima et al. (2022)** -- *Large Language Models Are Zero-Shot Reasoners.* Provides the Zero-shot CoT ("Let's think step by step") baseline.
- **Zhou et al. (2023)** -- *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models.* Provides the Least-to-Most prompting technique, which achieves the highest baseline robustness on GSM-IC by decomposing problems into subproblems.
- **Wang et al. (2023)** -- *Self-Consistency Improves Chain of Thought Reasoning in Language Models.* Provides the self-consistency decoding strategy, which is the most effective single mitigation for irrelevant-context distractibility.
- **Chen et al. (2022)** -- *Program of Thoughts Prompting.* Provides the program-based prompting baseline that generates Python code to solve problems.

### Models

- **Brown et al. (2020)** -- *Language Models Are Few-Shot Learners (GPT-3).* Foundation for the models evaluated (code-davinci-002, text-davinci-003).
- **Chen et al. (2021)** -- *Evaluating Large Language Models Trained on Code (Codex).* Provides code-davinci-002, which achieves the strongest results on GSM-IC with appropriate prompting.

### Related Work on Context Utilization

- **Min et al. (2022)** -- *Rethinking the Role of Demonstrations in In-Context Learning.* Shows that label correctness in exemplars matters less than format, raising questions about how models use context that GSM-IC addresses from a different angle.

#### Cross-References in Available Papers

- **Context Length Hurts Performance (2025-11-context-length-hurts-performance):** Du et al. (2025) cite this paper in Section 6 (Core References, "Positional Bias and Context Length Effects"): "Shi et al. (2023) -- *Large Language Models Can Be Easily Distracted by Irrelevant Context.* Shows that irrelevant tokens distract models." Du et al.'s key contribution is demonstrating that even *without* irrelevant content (via attention masking), context length alone degrades performance -- extending beyond the distraction mechanism identified here. The two papers are complementary: this paper shows irrelevant tokens are distracting, while Du et al. show that even when distraction is eliminated, the sheer positional distance introduced by longer contexts independently hurts performance.
- **Lost in the Middle (2024-02-lost-in-the-middle):** Liu et al. (2024) study how the *position* of relevant information affects performance, finding a U-shaped curve. This paper studies a different dimension: how the *presence* of irrelevant information affects performance, regardless of position. Together, the two papers characterize complementary failure modes in long-context settings -- positional bias and content-based distraction.
