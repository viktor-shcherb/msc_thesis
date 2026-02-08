---
title: "Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models"
authors: "Levy, Jacoby, Goldberg"
year: 2024
venue: "ACL 2024"
paper_type: conference-paper
categories: ["long-context-evaluation", "benchmarking", "reasoning-evaluation", "position-bias"]
scope: ["input length effects on reasoning", "controlled evaluation of context length", "QA reasoning benchmark", "failure mode analysis", "chain-of-thought evaluation"]
benchmarks_used: ["flenqa"]
models_introduced: []
models_evaluated: ["gpt-4", "gpt-3.5-turbo", "gemini-pro", "mistral-medium", "mixtral-8x7b"]
key_claims:
  - id: C1
    claim: "LLMs degrade significantly in reasoning performance at 3000 tokens, well below their technical maximum: average accuracy drops from 0.92 to 0.68 across all tested models"
    evidence: "Section 2, Section 4, Figure 1"
    status: supported
    scope: "5 LLMs (GPT-4, GPT-3.5, Gemini Pro, Mistral Medium, Mixtral 8x7B), 3 True/False reasoning tasks, 250-3000 token range, non-adjacent key paragraphs, averaged over similar and different padding"
    magnitude: "24 percentage point accuracy drop (0.92 to 0.68 average), 600 samples per data point"
  - id: C2
    claim: "Length-induced reasoning degradation occurs even when all added tokens are duplicates of the relevant content (no irrelevant or distracting text), showing length itself is the causal factor"
    evidence: "Figure 3, Section 4.1"
    status: supported
    scope: "5 LLMs, duplicate padding only, 250-3000 tokens, 3 tasks, 300 samples per data point"
    magnitude: "All models degrade; Mixtral 8x7B drops to ~0.80 at 3000 tokens; GPT-3.5 and GPT-4 less affected but still show decline"
  - id: C3
    claim: "Position of key paragraphs affects accuracy (recency bias, lost-in-the-middle effects) but degradation with length appears at all positions"
    evidence: "Figure 4, Figure 16, Section 4.1"
    status: supported
    scope: "5 LLMs, 4 placement conditions (first/middle/last/random), similar and different padding averaged, 300 samples per data point"
    magnitude: "Last placement yields highest accuracy (recency bias); middle placement yields lowest; degradation trend present at all positions"
  - id: C4
    claim: "Different (Book Corpus) padding causes larger performance drops than similar (task-resampled) padding, contrary to the expectation that dissimilar text would be easier to ignore"
    evidence: "Figure 5, Section 4.2"
    status: supported
    scope: "5 LLMs, non-adjacent key paragraphs, 250-3000 tokens, 300 samples per data point"
    magnitude: "Books Corpus padding produces steeper accuracy decline than resampling padding in most models"
  - id: C5
    claim: "Next-word prediction accuracy correlates negatively with reasoning performance on FLenQA (Pearson rho = -0.95, p = 0.01), implying perplexity cannot substitute downstream task evaluation on long inputs"
    evidence: "Figure 6, Section 5"
    status: supported
    scope: "4 LLMs (Gemini Pro excluded due to empty replies), 250-3000 tokens, next-word exact-match accuracy vs FLenQA reasoning accuracy, 300 samples per data point"
    magnitude: "Pearson rho = -0.95, p = 0.01"
  - id: C6
    claim: "Chain-of-thought prompting improves baseline accuracy but does not mitigate length-induced degradation for most models; only GPT-4 shows an increased CoT benefit as length grows"
    evidence: "Figure 1, Section 6"
    status: supported
    scope: "5 LLMs, 3 tasks, 250-3000 tokens, zero-shot CoT using Zhou et al. (2022) elicitation string"
    magnitude: "CoT improvement roughly constant across lengths for 4/5 models; GPT-4 CoT gap increases with length; Gemini Pro CoT decreases performance at longer lengths"
  - id: C7
    claim: "Premature answering in CoT (answer before reasoning steps) correlates with incorrect responses (odds-ratio 3.643, p < 0.001) and increases with input length"
    evidence: "Figure 8, Section 7"
    status: supported
    scope: "5 LLMs, CoT prompting, 250-3000 tokens, Fisher exact test"
    magnitude: "Odds-ratio 3.643, p < 0.001; GPT-3.5 early responses reach ~300 frequency at 3000 tokens"
  - id: C8
    claim: "Reduced fact coverage in CoT reasoning steps correlates with incorrect responses (odds-ratio 3.138, p < 0.001) and coverage declines from ~0.6 to ~0.2 as input length grows"
    evidence: "Figure 9, Section 7"
    status: supported
    scope: "5 LLMs, CoT prompting, 250-3000 tokens, Fisher exact test, coverage measured by key sentence match"
    magnitude: "Odds-ratio 3.138, p < 0.001; coverage drops from ~0.6 at 250 tokens to ~0.2 at 3000 tokens for most models"
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "FlenQA cites Liu et al. (2024) for position-dependent performance degradation; both show context utilization degrades, but FlenQA isolates input length as a variable independent of task difficulty"
  - target: 2023-07-gsm-ic-irrelevant-context
    type: complementary
    detail: "Shi et al. (2023) demonstrate irrelevant context degrades math reasoning; FlenQA extends by showing degradation occurs even without irrelevant content (duplicate padding), isolating length from distraction"
  - target: 2025-11-context-length-hurts-performance
    type: extended-by
    detail: "Extends FlenQA's findings with additional controls (whitespace padding, attention masking) to further isolate length effects from content effects"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong tests reasoning across much longer contexts (up to 10M tokens); both papers show reasoning degrades with context length independently of task complexity"
  - target: 2025-04-effective-context-length-falls-short
    type: complementary
    detail: "Provides a mechanistic explanation (undertrained position indices from left-skewed training distributions) for why effective context falls short, complementing FlenQA's empirical demonstration"
  - target: 2025-07-nolima-long-context-evaluation
    type: complementary
    detail: "Both isolate true reasoning from surface matching in long-context evaluation; NoLiMa removes literal cues while FlenQA controls for input length"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Provides theoretical grounding for the position-dependent performance effects observed empirically in FlenQA"
  - target: 2024-08-found-in-the-middle
    type: complementary
    detail: "Identifies positional attention bias as the mechanistic cause of position-dependent degradation; FlenQA shows length degrades reasoning even at optimal positions (key paragraphs first)"
  - target: 2024-11-genuinely-difficult-long-context
    type: complementary
    detail: "Goldman et al. cite FlenQA as evidence that adding distractors between needles increases dispersion independently of needle count or context length; FlenQA tasks are classified across both dispersion levels in their taxonomy"
open_questions:
  - question: "What is the mechanistic cause of length-induced reasoning degradation beyond position bias effects?"
    addressed_by: 2025-11-context-length-hurts-performance
  - question: "Does length-induced reasoning degradation scale to longer contexts (>3000 tokens) and more complex multi-step tasks?"
    addressed_by: 2024-12-babilong-long-context-reasoning
  - question: "How does the distance between non-adjacent key paragraphs affect the severity of length-induced degradation?"
    addressed_by: null
  - question: "Can architectural modifications or training strategies mitigate length-induced reasoning degradation without merely improving next-word prediction?"
    addressed_by: null
---
# Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models

**Authors:** Mosh Levy, Alon Jacoby (Bar-Ilan University), Yoav Goldberg (Bar-Ilan University, Allen Institute for AI)
**Date:** August 2024, ACL 2024 (arXiv:2402.14848)

---

## Core Research Problem

Recent LLMs claim to support increasingly long input contexts (4K to 100K+ tokens), yet it remains unclear whether this support transfers across tasks. A natural assumption is that a model capable of solving a task at short input lengths should solve the same task when it is embedded within a longer prompt. Existing long-context benchmarks (Shaham et al., 2023; Li et al., 2023; Bai et al., 2023) vary both input length and task difficulty simultaneously, making it impossible to attribute performance changes to length alone. Meanwhile, next-word prediction evaluations (Anil et al., 2023; Jiang et al., 2024) show improved perplexity at longer contexts but have no established correlation with downstream task performance.

Prior work on context utilization shows that LSTMs use long-range context only coarsely (Khandelwal et al., 2018), that longer contexts improve prediction of only a few tokens (Sun et al., 2021), and that efficient Transformers are recency-biased (Qin et al., 2023). Liu et al. (2023b) established that LLMs exhibit position-dependent performance degradation in extractive QA. Shi et al. (2023) showed that irrelevant context degrades math reasoning. However, none of these studies isolate input length as a controlled variable while keeping the underlying task constant.

**The core challenge is: determining whether input length alone degrades LLM reasoning performance when the task, relevant information, and required reasoning remain identical across length variations.**

---

## Problem Solutions

The paper introduces **FLenQA** (Flexible LENgth Question Answering), a controlled QA benchmark that isolates input length as a variable. The key contributions are:

1. **Length-controlled evaluation framework.** Each sample has a fixed reasoning task (two key paragraphs, a True/False question); only the irrelevant padding changes across length variations (250--3000 tokens), keeping the reasoning requirement identical.
2. **Multiple padding strategies.** Three types of background text -- duplicate (relevant content repeated), similar (paragraphs from other instances of the same task), and different (Book Corpus text) -- and four placement conditions (first, middle, last, random) systematically explore confounds.
3. **Empirical finding: length degrades reasoning.** Average accuracy drops from 0.92 to 0.68 at 3000 tokens, well below models' technical maxima, across all five evaluated models (Section 4, Figure 1).
4. **Negative correlation with next-word prediction.** Perplexity improves with length while reasoning degrades, demonstrating these metrics are dissociated (Section 5, Figure 6).
5. **Failure mode taxonomy.** Four systematic failure patterns are identified and quantified (Section 7).

---

## Approach Details

### Method

FLenQA is a QA dataset designed to satisfy three requirements: (1) models must reason over the input (not rely on parametric knowledge), (2) input length is isolated as the only variable, and (3) inputs appear natural (Section 2). Each sample consists of a True/False question requiring joint reasoning over two key sentences, expanded to thematically coherent key paragraphs using GPT-4 (with manual verification by the authors). The dataset is completely balanced in label distribution (Section 3).

**Three reasoning tasks**, each with 100 base instances:

- **Monotone Relations (MonoRel):** Two key sentences compare entities on a monotone scale (e.g., "X is younger than Y", "Y is younger than Z"), and the question asks about a transitive relation between entities appearing in different sentences. Inspired by Sinha et al. (2018), with newly defined relation types. Names drawn randomly using the Faker Python library (Faraglia and Contributors, 2012).
- **People In Rooms (PIR):** One key sentence places a person in a named room, the other assigns a property to that room. The question asks whether the person is in a room with that property. Inspired by bAbI (Weston et al., 2016). Rooms and properties are mutually exclusive to avoid ambiguity.
- **Simplified Ruletaker:** One logical rule and two facts (each a key paragraph); the question asks whether a statement can be derived. Simplified from Clark et al. (2021) to two facts and one rule after initial experiments showed most LLMs struggle with more complex instances (Section 3.2, footnote 4).

### Key Technical Components

**Length variation.** Each base instance is expanded to approximately 250, 500, 1000, 2000, and 3000 tokens (within a tolerance of plus/minus 70 tokens as measured by the GPT-4 tokenizer; Section 3.3, footnote 5). Padding (irrelevant background text) is added in three varieties:

- **Duplicate:** Key paragraphs are repeated in alternating order until the target length is reached. No irrelevant content; the information retrieval sub-task is trivial (Section 3.3.1).
- **Similar:** Paragraphs from other base instances of the same task (excluding those with shared entities to avoid contradictions). Simulates a RAG-like setup (Mao et al., 2020; Section 3.3.1).
- **Different:** Continuous text from the Books Corpus (Zhu et al., 2015), with key paragraphs injected at sentence boundaries (Section 3.3.1).

**Placement control.** Four conditions for where key paragraphs appear within the padding (Section 3.3.2): (1) first (beginning, followed by padding), (2) middle (padding before and after, key paragraphs adjacent in the center), (3) last (padding followed by key paragraphs), (4) random (padding before, between, and after key paragraphs with random intervals).

**Key paragraph expansion.** Each key sentence is expanded to approximately 125 tokens by GPT-4, prompted to extend without adding new information. Results are manually verified by the authors (Section 3.1, Appendix A).

**Evaluation parameters.** Temperature 0, top-p 0 where available. Gemini Pro configured to ignore safety guardrails to overcome blank answers (Appendix B.2). Answers are extracted by searching for the last occurrence of "true" or "false" (case-insensitive) in the model output. Method validated on 100 manually examined responses (Appendix B.3).

### Experimental Setup

**Models evaluated:**

| Model | Context Window |
|---|---|
| GPT-4 (gpt-4-1106-preview) | 128K tokens |
| GPT-3.5 (gpt-3.5-turbo-1106) | 16K tokens |
| Gemini Pro | 32K tokens |
| Mistral Medium | 32K tokens |
| Mixtral 8x7B | 32K tokens |

**Prompting.** Two conditions: direct prompting ("Answer only True or False") and zero-shot Chain-of-Thought using the optimized elicitation string from Zhou et al. (2022): "Let's work this out in a step by step way to be sure we have the right answer." Full prompt templates for each task in both conditions appear in Appendix B.1.

**Sample sizes.** 600 samples per data point in the main experiment (Figure 1: non-adjacent key paragraphs, averaged over similar and different padding), 300 samples per data point in other experimental conditions.

**Reproducibility.** The dataset and generation code are publicly released at https://github.com/alonj/Same-Task-More-Tokens (Section 3, footnote 1). Deterministic decoding settings (temperature 0, top-p 0) support reproducibility. However, exact model versions are specific API snapshots (gpt-4-1106-preview, gpt-3.5-turbo-1106), which may become unavailable. No random seeds are reported for the data generation process beyond the programmatic construction.

### Key Results

**Baseline performance (250 tokens, Table 1):**

| Model | Prompt | MonoRel | PIR | Ruletaker |
|---|---|---|---|---|
| GPT-3.5 | Direct | 0.77 | 0.81 | 0.74 |
| GPT-3.5 | CoT | 0.86 | 0.88 | 0.88 |
| GPT-4 | Direct | 1.00 | 1.00 | 0.98 |
| GPT-4 | CoT | 1.00 | 1.00 | 0.97 |
| Gemini Pro | Direct | 0.84 | 1.00 | 0.92 |
| Gemini Pro | CoT | 0.88 | 0.96 | 0.97 |
| Mistral Medium | Direct | 0.99 | 1.00 | 0.73 |
| Mistral Medium | CoT | 1.00 | 1.00 | 0.89 |
| Mixtral 8x7B | Direct | 0.92 | 0.97 | 0.80 |
| Mixtral 8x7B | CoT | 0.86 | 0.97 | 0.93 |

- Four of five models achieve >0.89 accuracy at minimal length with direct prompting. GPT-3.5 is lowest (0.74--0.81) but still high enough for degradation to be observable (Section 3.4).

**Main result -- non-adjacent key paragraphs (Figure 1):**

- Average accuracy across all models drops from **0.92 at 250 tokens to 0.68 at 3000 tokens** -- a 24-percentage-point decline at lengths far below the models' technical maxima. Each data point reflects 600 samples (strong evidence: 5 models, 3 tasks, 2 padding types averaged).
- GPT-4 degrades least but still drops substantially without CoT (from ~1.0 to ~0.8). With CoT, GPT-4 maintains highest performance (staying above ~0.9).
- All models show monotonic degradation with length.

**Duplicate padding -- no irrelevant content (Figure 3):**

- Even when the padding consists entirely of repeated key paragraphs (no distractors, no position effects), accuracy decreases with length for all models. 300 samples per data point.
- GPT-3.5 and GPT-4 are less affected in this setting than with irrelevant padding, but degradation is still present.
- Mixtral 8x7B drops most sharply (to approximately 0.80 at 3000 tokens).

**Position effects (Figure 4, Figure 16):**

- Accuracy decreases with length regardless of key paragraph placement (first, middle, last, random). 300 samples per data point per condition; results averaged over both padding types.
- Key paragraphs placed last generally yield highest accuracy (recency bias). Middle placement often yields lowest accuracy, consistent with Liu et al. (2023b).
- Adjacency of key paragraphs produces higher accuracy than random (non-adjacent) placement.

**Padding type (Figure 5):**

- Different (Book Corpus) padding causes **larger** degradation than similar (task-resampled) padding in most models -- contrary to the expectation that dissimilar text would be easier to discard. 300 samples per data point (moderate evidence: consistent across 5 models but no formal significance test reported for the gap between padding types).

**Next-word prediction vs. reasoning (Figure 6):**

| Metric | Trend with Length |
|---|---|
| Next-word prediction accuracy | Increases |
| FLenQA reasoning accuracy | Decreases |

- Pearson correlation: **rho = -0.95, p = 0.01** (computed over 4 models; Gemini Pro excluded as it returned empty replies for next-word prediction at all lengths). 300 samples per data point (limited evidence: single correlation across 4 models; no confidence intervals reported).

**Chain-of-thought analysis (Figure 1, Section 6):**

- CoT improves accuracy across all tasks and models at short lengths.
- CoT does **not** mitigate the length-induced degradation trend for GPT-3.5, Gemini Pro, Mistral Medium, or Mixtral 8x7B: the accuracy improvement from CoT is roughly constant across lengths.
- **GPT-4 is the sole exception:** the gap between CoT and non-CoT increases as input length grows, making CoT a partial mitigation for GPT-4 only.
- For Gemini Pro, CoT actually decreases performance as input length increases, despite improving short-input performance.

### Length-Induced Failure Modes

The paper identifies four systematic failure patterns that correlate with incorrect responses and worsen with length (Section 7):

1. **Instruction non-compliance.** Models increasingly refuse to answer, responding with "There is not enough information in the text" despite the task being solvable. Refusal rate grows with input length (Figure 7). Gemini Pro shows the most pronounced increase in "Other/Refused" answers.

2. **Label bias.** Models develop a bias toward answering "False" as input length increases, despite the dataset being perfectly balanced. Gemini Pro is most affected: False answers reach approximately 400 at 3000 tokens while True answers shrink to approximately 100 (Figure 7, Figure 17).

3. **Premature answering in CoT.** Models output the final True/False answer before the reasoning steps, violating CoT instructions. Frequency increases with length (Figure 8). GPT-3.5 shows the most dramatic increase (reaching approximately 300 at 3000 tokens); GPT-4 remains relatively low. Incorrect responses are statistically dependent on premature answering (odds-ratio **3.643**, p < 0.001, Fisher exact test; Section 7, footnote 8).

4. **Reduced fact coverage in CoT.** Models fail to locate and reproduce the relevant key sentences in their reasoning steps as input length grows (Figure 9). GPT-4 starts highest (~0.6 coverage at 250 tokens) and declines to ~0.3 at 3000 tokens. GPT-3.5 starts around 0.4--0.5 and drops sharply. Mistral Medium and Mixtral 8x7B remain lower throughout, declining to near 0.1--0.2 at 3000 tokens. Incorrect responses are statistically dependent on incomplete coverage (odds-ratio **3.138**, p < 0.001, Fisher exact test; Section 7, footnote 9). Coverage measured by case-insensitive exact match of key sentences in CoT output (Appendix B.4).

---

## Limitations and Failure Modes

- **Behavioral testing only.** The observed degradation remains mechanistically unexplained due to lack of access to model internals. The authors acknowledge this direction will remain limited for closed models (Limitations section, p. 10).
- **Lowest-common-denominator task design.** Tasks are deliberately simple to ensure all models can solve them at short lengths. This may mask more severe degradation patterns in complex reasoning tasks (e.g., 5+ key paragraphs) where stronger models might degrade at even shorter lengths (Limitations section, p. 10).
- **Limited reasoning task types.** Only three types of logical reasoning tasks are tested. Other reasoning types (reading comprehension, creative synthesis, mathematical reasoning) may exhibit different degradation profiles (Limitations section, p. 10).
- **GPT-4-generated key paragraphs.** Using GPT-4 to expand key sentences to key paragraphs may introduce systematic bias in the surrounding text, potentially affecting models that share similar training data (Limitations section, p. 10).
- **Distance between key paragraphs not tested.** The study does not systematically manipulate the distance between non-adjacent key paragraphs. The authors explicitly leave this for future work (Limitations section, p. 10).
- **Short maximum length (3000 tokens).** All experiments stop at 3000 tokens, which is orders of magnitude below the claimed context windows of the evaluated models. Degradation at longer lengths is not measured.
- **[Inferred]** No variance estimates or confidence intervals are reported for any accuracy measurements, limiting assessment of statistical reliability beyond the sample sizes stated.
- **[Inferred]** All models are accessed via API at fixed snapshots (late 2023 / early 2024); results may not generalize to subsequent model versions or open-weight alternatives.

#### Scope and Comparability

- **What was not tested:** Only 5 models evaluated, all accessed via API (no open-weight models with internal access). Maximum input length is 3000 tokens -- far below model maxima. Only True/False reasoning tasks with 2 key paragraphs; no multi-hop chains, reading comprehension, summarization, or mathematical reasoning. No evaluation of fine-tuned or instruction-tuned variants beyond the default API models. Distance between non-adjacent key paragraphs not varied. No non-English evaluation.
- **Comparability notes:** FLenQA uses GPT-4's tokenizer for length measurement, which may count differently than model-native tokenizers for Gemini Pro, Mistral Medium, and Mixtral 8x7B. The "250 tokens" baseline includes only key paragraphs and the question (no padding), so it is not directly comparable to other benchmarks' "short context" conditions that may include more surrounding text. The paper's definition of "degradation" is measured against the same task at shorter length, not against a fixed performance threshold, making cross-paper comparison of absolute accuracy values less informative than the degradation trend itself. Sample sizes (300-600 per data point) are larger than many long-context evaluations but smaller than standard NLP benchmark evaluation sets.

---

## Conclusions

### Contributions

1. **FLenQA benchmark for controlled length evaluation.** Introduced a QA reasoning benchmark with three tasks (MonoRel, PIR, Simplified Ruletaker), 100 base instances each, expandable to multiple lengths with controlled padding types and placement. The dataset and generation code are publicly released (Section 3).

2. **Input length alone degrades reasoning.** Demonstrated that reasoning accuracy drops from 0.92 to 0.68 on average at 3000 tokens -- well below models' technical maxima -- even when the underlying task remains identical. The degradation trend appears across all models, tasks, padding types, and placement conditions (Section 4, Figure 1).

3. **Degradation occurs without irrelevant content.** Showed that even with duplicate padding (repeated key paragraphs, no distractors), length degrades performance. This isolates length itself as a causal factor, distinct from distraction by irrelevant content (Figure 3, Section 4.1).

4. **Negative correlation between perplexity and reasoning.** Established that next-word prediction accuracy and reasoning accuracy are negatively correlated (rho = -0.95, p = 0.01), demonstrating that perplexity-based evaluation cannot substitute for downstream task evaluation on long inputs (Figure 6, Section 5).

5. **CoT does not mitigate length-induced degradation.** Chain-of-thought prompting improves baseline accuracy but provides roughly constant improvement across lengths (no mitigation), except for GPT-4 where CoT benefit increases with length (Figure 1, Section 6).

6. **Failure mode taxonomy.** Identified and quantified four systematic failure modes that worsen with length: instruction non-compliance, label bias, premature answering in CoT (odds-ratio 3.643), and reduced fact coverage (odds-ratio 3.138), each statistically associated with incorrect responses (Section 7).

### Implications

1. **Single-length evaluation is insufficient.** Evaluating model performance at a single input length does not provide a full picture; models should be tested across multiple lengths to assess robustness. The authors argue: "for a model to be considered capable at long range, it must maintain its performance at any length it technically supports" (Section 9, p. 10).

2. **Perplexity is misleading for long-context capability.** Using perplexity or next-word prediction as a proxy for long-context capability is actively misleading, as these metrics improve with length while reasoning degrades. [Inference: this challenges the common practice of validating context extensions via perplexity alone.]

3. **Length-induced failure modes may compound.** The identified failure modes (refusals, bias, premature answering, reduced coverage) suggest multiple independent mechanisms through which length degrades performance, implying that single-fix solutions are unlikely to suffice. [Speculative: the paper does not test whether addressing individual failure modes would recover performance.]

---

## Key Claims

1. **Reasoning performance degrades at lengths far below technical maxima.** Average accuracy across five models drops from 0.92 to 0.68 at 3000 tokens, with non-adjacent key paragraphs and mixed padding types (Section 4, Figure 1). Each data point reflects 600 samples across 3 tasks and 2 padding types (strong evidence: 5 models, all show consistent degradation). **Scope:** 5 commercial LLMs, True/False reasoning, 250--3000 tokens. **Magnitude:** 24 percentage point average decline. Status: **supported**.

2. **Length alone causes degradation, not irrelevant content.** With duplicate padding (only relevant tokens added), all models still degrade with length (Figure 3, Section 4.1). This separates the length effect from the distraction effect demonstrated by Shi et al. (2023). 300 samples per data point (moderate evidence: consistent across 5 models but only one padding condition tested). **Scope:** duplicate padding, 5 LLMs, 250--3000 tokens. **Magnitude:** all models degrade; Mixtral 8x7B drops to ~0.80 at 3000 tokens. Status: **supported**.

3. **Position effects are secondary to length effects.** Degradation occurs at all four placement conditions (first, middle, last, random), though placing key paragraphs last yields slightly higher accuracy (recency bias) and middle placement yields slightly lower accuracy (Figure 4, Figure 16, Section 4.1). 300 samples per data point per condition, averaged over both padding types (moderate evidence: consistent pattern across 5 models and 4 conditions). **Scope:** similar and different padding averaged, 5 LLMs, adjacent and non-adjacent placements. **Magnitude:** recency advantage observable but degradation trend persists at all positions. Status: **supported**.

4. **Dissimilar padding is harder than similar padding.** Book Corpus padding causes larger accuracy drops than task-resampled padding in most models, contradicting the hypothesis that dissimilar text would be easier to ignore (Figure 5, Section 4.2). 300 samples per data point (moderate evidence: consistent across most models but no formal significance test for the gap between padding types). **Scope:** non-adjacent key paragraphs, 5 LLMs, 250--3000 tokens. **Magnitude:** Books Corpus produces steeper decline in most models. Status: **supported**.

5. **Next-word prediction anti-correlates with reasoning.** Pearson rho = -0.95, p = 0.01 between next-word accuracy and FLenQA reasoning accuracy across input lengths (Figure 6, Section 5). 300 samples per data point (limited evidence: 4 models, single correlation, Gemini Pro excluded, no confidence intervals). **Scope:** 4 LLMs (excluding Gemini Pro), exact-match next-word prediction, 250--3000 tokens. **Magnitude:** rho = -0.95, p = 0.01. Status: **supported**.

6. **CoT provides constant, not compensatory, benefit.** CoT prompting improves accuracy by a roughly constant margin across lengths for GPT-3.5, Gemini Pro, Mistral Medium, and Mixtral 8x7B. Only GPT-4 shows increasing CoT benefit with length (Figure 1, Section 6). For Gemini Pro, CoT decreases performance at longer lengths despite improving short-input performance (moderate evidence: 5 models, 3 tasks, but no formal test of interaction between CoT and length). **Scope:** zero-shot CoT, 5 LLMs, 250--3000 tokens. **Magnitude:** CoT uplift roughly constant for 4/5 models; GPT-4 CoT gap increases with length. Status: **supported**.

7. **Premature answering correlates with errors in CoT.** Incorrect responses are statistically dependent on producing the answer before reasoning steps, with odds-ratio 3.643 (p < 0.001, Fisher exact test). Premature answering frequency increases with input length, with GPT-3.5 showing the most dramatic increase (Figure 8, Section 7). **Scope:** CoT prompting, 5 LLMs, 250--3000 tokens. **Magnitude:** odds-ratio 3.643, p < 0.001. Status: **supported**.

8. **Reduced fact coverage correlates with errors in CoT.** Incorrect responses are statistically dependent on incomplete coverage of key sentences in CoT reasoning steps, with odds-ratio 3.138 (p < 0.001, Fisher exact test). Coverage drops from ~0.6 to ~0.2 across the 250--3000 token range for most models (Figure 9, Section 7). Coverage measured via case-insensitive key sentence matching, validated on 100 manual samples (Appendix B.4). **Scope:** CoT prompting, 5 LLMs, 250--3000 tokens. **Magnitude:** odds-ratio 3.138, p < 0.001; coverage drops from ~0.6 to ~0.2. Status: **supported**.

---

## Open Questions

1. **Mechanistic explanation for length-induced degradation.** What causes reasoning performance to drop with length even when all added tokens are relevant (duplicate padding)? The behavioral testing approach cannot answer this. Partially addressed by 2025-11-context-length-hurts-performance, which uses attention masking to further isolate the effect, and by 2025-04-effective-context-length-falls-short, which attributes degradation to undertrained position indices.

2. **Scaling to longer contexts and harder tasks.** Does the degradation pattern hold at much longer contexts (10K, 100K+ tokens) and with more complex reasoning tasks requiring more than two key paragraphs? Partially addressed by 2024-12-babilong-long-context-reasoning, which tests reasoning up to 10M tokens and confirms degradation.

3. **Distance effects between key paragraphs.** How does the distance between non-adjacent key paragraphs affect reasoning degradation? The paper explicitly leaves this for future work (Limitations section, p. 10). Not yet addressed.

4. **Mitigations beyond CoT.** Can architectural modifications (sparse attention, landmark tokens) or training strategies (position-balanced data, longer-sequence pretraining) mitigate length-induced reasoning degradation without merely improving next-word prediction? Not yet addressed.

---

## Core References and Why They Are Referenced

### Context Utilization and Length Effects

- **Khandelwal et al. (2018)** -- *Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context.* Showed small LSTM language models make increasingly coarse use of long-range context. FLenQA extends this line of work to Transformer LLMs, demonstrating that even modern models degrade with input length.

- **Sun et al. (2021)** -- *Do Long-Range Language Models Actually Use Long-Range Context?* Found that longer contexts improve prediction of only a few tokens. FLenQA complements these findings by demonstrating degradation in reasoning (not just prediction) with length.

- **Liu et al. (2023b)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Established U-shaped position bias in extractive QA. FLenQA's position experiments (Figure 4) confirm these patterns and extend the analysis by isolating length from task difficulty.

- **Shi et al. (2023)** -- *Large Language Models Can Be Easily Distracted by Irrelevant Context.* Demonstrated that appending irrelevant text to GSM-8K reduces math reasoning. FLenQA's duplicate-padding experiment (Figure 3) isolates length from distraction by showing degradation without any irrelevant content.

### Long-Context Benchmarks

- **Shaham et al. (2023)** -- *ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding.* Representative of long-context benchmarks that do not control for task difficulty across lengths -- the confound FLenQA is designed to eliminate.

- **Li et al. (2023)** -- *Loogle: Can Long-Context Language Models Understand Long Contexts?* Another long-context benchmark where length and task difficulty covary, motivating FLenQA's controlled design.

- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Long-context benchmark with fixed-length samples. FLenQA complements by enabling comparison of the same task at multiple lengths.

### Reasoning and Chain-of-Thought

- **Kojima et al. (2022)** -- *Large Language Models Are Zero-Shot Reasoners.* Introduced zero-shot CoT prompting. FLenQA tests whether CoT mitigates length-induced degradation (finding it does not for most models). Also cited in the failure modes analysis for the finding that reasoning steps after the answer do not improve performance.

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* Foundational CoT work. FLenQA's CoT analysis (Section 6) and failure mode analysis (premature answering, reduced coverage) extend understanding of CoT limitations.

- **Zhou et al. (2022)** -- *Large Language Models Are Human-Level Prompt Engineers.* Provides the optimized CoT elicitation string used in FLenQA experiments.

- **Clark et al. (2021)** -- *Transformers as Soft Reasoners over Language.* Source of the Ruletaker benchmark that FLenQA simplifies for its Simplified Ruletaker task.

- **Weston et al. (2016)** -- *Towards AI-Complete Question Answering: A Set of Prerequisite Toy Tasks.* Source of the bAbI tasks that inspire the People In Rooms (PIR) task.

- **Sinha et al. (2018)** -- *Compositional Language Understanding with Text-Based Relational Reasoning.* Source of monotonic relation types that inspire the MonoRel task.

### Evaluation Methodology

- **Holtzman et al. (2023)** -- *Generative Models as a Complex Systems Science.* Provides the methodological framework of behavioral testing through input intervention that FLenQA adopts.

- **Liu et al. (2023a)** -- *Same Pre-Training Loss, Better Downstream: Implicit Bias Matters for Language Models.* Showed that pre-training loss does not predict downstream performance. FLenQA extends this finding specifically to the relationship between next-word prediction and reasoning at varying lengths.

### Perplexity and Downstream Correlation

- **Anil et al. (2023)** -- *Gemini: A Family of Highly Capable Multimodal Models.* Uses perplexity to demonstrate long-context utilization. FLenQA shows that such perplexity improvements do not transfer to reasoning tasks.

- **Jiang et al. (2024)** -- *Mixtral of Experts.* Also uses perplexity for long-context validation. FLenQA's negative correlation result (Section 5) directly challenges this evaluation approach.
