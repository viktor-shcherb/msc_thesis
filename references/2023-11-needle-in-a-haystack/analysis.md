---
title: "Needle In A Haystack -- Pressure Testing LLMs"
authors: "Kamradt"
year: 2023
venue: "GitHub / community contribution"
paper_type: informal
categories: ["long-context-evaluation", "benchmarking"]
scope: ["long-context retrieval evaluation", "position-dependent performance"]
benchmarks_used: ["niah"]
models_introduced: []
models_evaluated: ["gpt-4", "claude-2.1"]
key_claims:
  - id: C1
    claim: "GPT-4-128K retrieval performance degrades above 73K tokens despite supporting 128K token context"
    evidence: "GPT-4-128K heatmap, November 8, 2023 X thread"
    status: supported
    scope: "GPT-4-128K (gpt-4-1106-preview), single-needle retrieval, Paul Graham essay haystack, 15x15 grid"
    magnitude: "near-perfect recall below 73K tokens, degraded recall above 73K"
  - id: C2
    claim: "GPT-4-128K fails primarily at 7--50% document depth for contexts above 73K tokens"
    evidence: "GPT-4-128K heatmap, November 8, 2023 X thread"
    status: supported
    scope: "GPT-4-128K, contexts above 73K tokens, single-needle retrieval"
    magnitude: "low recall at 7--50% depth vs. near-perfect at 0% and >50% depth"
  - id: C3
    claim: "Claude 2.1 achieves only 27% overall retrieval accuracy across its 200K context window with baseline prompting"
    evidence: "Claude 2.1 heatmap, November 21, 2023 X thread; Anthropic follow-up analysis"
    status: supported
    scope: "Claude 2.1 200K, single-needle retrieval, baseline prompt without retrieval directive, 35x35 grid"
    magnitude: "27% overall accuracy"
  - id: C4
    claim: "Adding a single prompt directive improves Claude 2.1 retrieval accuracy from 27% to 98%"
    evidence: "Anthropic follow-up analysis, November 2023; prompt template in GitHub repository"
    status: supported
    scope: "Claude 2.1 200K, single-needle retrieval, adding 'Here is the most relevant sentence in the context:' assistant prefix"
    magnitude: "27% to 98% accuracy (+71 percentage points)"
  - id: C5
    claim: "Facts placed at the very beginning (depth 0%) are recalled reliably regardless of context length for both models"
    evidence: "GPT-4 and Claude 2.1 heatmaps"
    status: supported
    scope: "GPT-4-128K and Claude 2.1 200K, single-needle retrieval, depth 0%"
    magnitude: "~100% recall at depth 0% across all tested context lengths"
  - id: C6
    claim: "Position-dependent retrieval patterns are consistent across model families: reliable at context boundaries, degraded in the middle"
    evidence: "Comparison of GPT-4 and Claude 2.1 heatmaps"
    status: supported
    scope: "GPT-4-128K and Claude 2.1 200K only, single-needle retrieval with fixed needle text"
    magnitude: "qualitative pattern consistency (boundary recall vs. middle degradation)"
cross_references:
  - target: 2024-10-ruler-context-size
    type: extended-by
    detail: "RULER extends NIAH with diverse needle types, multi-key distractors, multi-value/multi-query retrieval, and non-retrieval tasks"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Liu et al. documented U-shaped positional bias in multi-document QA at shorter contexts; NIAH extends this to full context windows"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: extended-by
    detail: "DroPE uses NIAH variants from RULER for zero-shot evaluation of positional encoding modifications"
  - target: 2024-12-babilong-long-context-reasoning
    type: extended-by
    detail: "BABILong extends the NIAH paradigm from single-fact retrieval to multi-hop reasoning tasks in long contexts"
  - target: 2025-07-nolima-long-context-evaluation
    type: extended-by
    detail: "NoLiMa identifies NIAH's high lexical overlap (ROUGE-1 = 0.905) and constructs a benchmark requiring semantic retrieval"
  - target: 2025-04-effective-context-length-falls-short
    type: extended-by
    detail: "Uses 4-needle NIAH as the primary evaluation for training-free context extension methods"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention introduced passkey retrieval, a direct predecessor to NIAH using random strings rather than natural language"
  - target: 2024-07-llama-3-herd-of-models
    type: extended-by
    detail: "Llama 3 uses NIAH and multi-needle variants to validate 128K context extension at each stage"
  - target: 2024-03-gemini-1.5-long-context
    type: extended-by
    detail: "Gemini 1.5 extends single-needle NIAH to multimodal (text, video, audio) and multi-needle variants at up to 10M tokens"
  - target: 2025-04-retrieval-head-long-context-factuality
    type: extended-by
    detail: "Wu et al. use NIAH as the core methodology to discover retrieval heads -- the sparse set of attention heads mechanistically responsible for NIAH retrieval"
  - target: 2024-07-qwen2-technical-report
    type: extended-by
    detail: "Qwen2 evaluates all model sizes (0.5B to 72B) on NIAH up to 128K tokens, demonstrating near-perfect retrieval accuracy for the 72B and 7B models with YARN+DCA"
  - target: 2024-12-deepseek-v3-technical-report
    type: extended-by
    detail: "DeepSeek-V3 uses NIAH to validate 128K context extension, achieving perfect retrieval scores across all depths and context lengths (Figure 8)"
  - target: 2025-07-lv-eval-long-context-benchmark
    type: extended-by
    detail: "LV-Eval's factrecall-en and factrecall-zh datasets extend NIAH with confusing facts insertion and keyword replacement, showing that standard NIAH is too simple"
  - target: 2024-11-genuinely-difficult-long-context
    type: complementary
    detail: "Goldman et al. classify NIAH as the primary example of low-scope low-dispersion tasks that can be solved by implicit retrieval and are least indicative of genuine long-context capabilities"
  - target: 2025-04-longgenbench-long-form-generation
    type: complementary
    detail: "LongGenBench introduces 'reversed NIAH': placing specific instructions at designated output positions in long-form generation, analogous to NIAH's needle retrieval in long inputs"
open_questions:
  - question: "Does the single-needle, high-lexical-overlap design overestimate model retrieval capabilities compared to real-world information needs?"
    addressed_by: 2025-07-nolima-long-context-evaluation
  - question: "How much of the position-dependent retrieval failure is due to attention mechanism limitations vs. training data distribution?"
    addressed_by: null
  - question: "Does prompt engineering systematically mitigate positional retrieval failures across all model families, or is Claude 2.1's sensitivity a special case?"
    addressed_by: null
  - question: "Can NIAH-style evaluation distinguish between models that truly comprehend long contexts vs. those that only perform surface-level token matching?"
    addressed_by: 2024-10-ruler-context-size
---

# Needle In A Haystack -- Pressure Testing LLMs

**Author:** Greg Kamradt (Data Independent / Leverage)
**Date:** November 2023
**Type:** X (Twitter) posts + GitHub repository (not a formal peer-reviewed paper)
**URL:** https://github.com/gkamradt/LLMTest_NeedleInAHaystack

The NIAH test became the de facto standard for evaluating long-context retrieval in LLMs. Multiple peer-reviewed papers cite it directly (RULER, BABILong, NoLiMa, DroPE) and the methodology was adopted in official model reports (e.g., Meta's Llama 3.1 technical report uses a 4-needle variant).

---

## Core Research Problem

By late 2023, LLM context windows were expanding rapidly -- GPT-4 Turbo supported 128K tokens and Claude 2.1 supported 200K tokens. Model providers marketed these as enabling long-document understanding, but **no standardized test existed for verifying whether models could actually retrieve information from arbitrary positions within these large context windows**. Prior work by Liu et al. (2023) -- *Lost in the Middle* -- had demonstrated a U-shaped performance curve in multi-document QA, but that study used shorter contexts and focused on retrieval-augmented generation settings with multiple documents. Mohtashami & Jaggi (2023) -- *Landmark Attention* -- had introduced passkey retrieval (inserting a random passkey into a long context), but this used random strings rather than natural language and did not systematically sweep over both depth and context length.

The core challenge was: **how to pressure-test whether LLMs can reliably retrieve a single piece of information placed at any depth within their full claimed context window.**

---

## Problem Solutions

Kamradt introduced a simple, controlled evaluation protocol:

1. **Single-needle insertion:** Place one out-of-context fact (the "needle") at a controlled depth within a long document (the "haystack") and ask the model to retrieve it.
2. **Systematic sweep over depth and length:** Vary both the position of the needle (0%--100% document depth) and the total context length (1K tokens up to the model's maximum) to produce a two-dimensional performance map.
3. **Heatmap visualization:** Display results as a depth-vs-length heatmap, making failure regions immediately visible.

---

## Approach Details

### Method

The test inserts a single factual sentence (the needle) into a body of unrelated but topically coherent text (the haystack), then prompts the model to answer a question whose answer is the needle. The procedure is:

1. Select a target context length (in tokens) and a target document depth (as a percentage, 0% = beginning, 100% = end).
2. Construct the haystack by concatenating Paul Graham essays (49 essays in `needlehaystack/PaulGrahamEssays/`, concatenated and repeated to reach the target length; GitHub repository).
3. Insert the needle at the token position corresponding to the specified depth percentage. The insertion algorithm encodes both needle and context to tokens, calculates `insertion_point = int(len(tokens_context) * (depth_percent / 100))`, then walks backwards to the nearest sentence boundary (period token) before inserting (GitHub repository, `insert_needle()` method).
4. Prompt the model with the combined text and a retrieval question.
5. Evaluate the model's response using an LLM evaluator via LangChain's `labeled_score_string` evaluator. The scoring rubric uses a 1--10 scale (1 = completely unrelated, 10 = perfectly accurate). Note: the X threads describe the evaluator as "GPT-4," while the GitHub code defaults to `gpt-3.5-turbo-0125` as the evaluator model (GitHub repository, `needlehaystack/evaluators/openai.py`).
6. Repeat across all combinations of depth and length intervals.

**Needle text:** `"The best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day."` (GitHub repository, `run.py`).

**Retrieval question:** `"What is the best thing to do in San Francisco?"` with the instruction `"Don't give information outside the document or repeat your findings"` (GitHub repository, `run.py`).

The needle is deliberately out-of-place relative to the Paul Graham essays (which discuss startups, great work, and related topics), ensuring that retrieval cannot be accomplished through topical association alone.

### Key Technical Components

- **Depth parameterization:** Document depth is expressed as a percentage (0%--100%). The needle is inserted at the token position corresponding to that fraction of the total context, snapped to the nearest sentence boundary. Depth intervals can be distributed linearly or via a sigmoid function (`L * sigmoid(-k * (x - x0))` with `L=100`, `x0=50`, `k=0.1`) to concentrate sampling in the middle where failures are expected (GitHub repository).
- **Context length parameterization:** The haystack is constructed to a target token count by concatenating essays and truncating. Context lengths are generated via `np.linspace(min, max, num=intervals)`. Default range: 1,000 to 16,000 tokens; the original tests extended to 128K and 200K respectively (GitHub repository).
- **Context buffer:** 200 tokens (`final_context_length_buffer`) are reserved for system messages and output, reducing the effective haystack size (GitHub repository).
- **Grid resolution:** The GPT-4-128K test used 15 depth intervals x 15 context length intervals (225 total evaluations; X thread, November 8). The Claude 2.1-200K test used 35 x 35 intervals (1,225 evaluations; X thread, November 21).
- **Prompt templates:** OpenAI uses a chat-messages format with a system prompt ("You are a helpful AI bot...") and user messages containing the context and question. Anthropic uses a completion format wrapping context in `<context>` tags, with the assistant prefix `"Here is the most relevant sentence in the context:"` -- notably, this prefix was included in the Anthropic prompt template from the start (GitHub repository, `Anthropic_prompt.txt`).
- **Multi-needle extension:** The open-source framework includes `LLMMultiNeedleHaystackTester`, which inserts multiple needles at evenly distributed depths. For n needles starting at depth d%, the spacing is `(100 - d) / n` percentage points. Default multi-needle facts use pizza ingredient statements (GitHub repository).

### Experimental Setup

**Models evaluated:**

| Model | Max Context | Date Tested | Grid Size | Cost |
|---|---|---|---|---|
| GPT-4-128K (gpt-4-1106-preview) | 128K tokens | November 8, 2023 | 15 x 15 (225 evals) | ~$200 |
| Claude 2.1 | 200K tokens | November 21, 2023 | 35 x 35 (1,225 evals) | ~$1,016 |

**Haystack material:** 49 Paul Graham essays, concatenated and repeated to fill target context lengths (GitHub repository).

**Evaluation method:** LLM-as-judge via LangChain `labeled_score_string` evaluator with a 1--10 accuracy rubric. The X threads describe "GPT-4" as the evaluator; the GitHub code defaults to `gpt-3.5-turbo-0125` (GitHub repository, `needlehaystack/evaluators/openai.py`). All evaluations used `temperature=0`.

**Reproducibility:** The `needlehaystack` Python package is installable via `pip install needlehaystack` and supports OpenAI, Anthropic, and Cohere providers. Original results are stored in `/original_results` in the repository. 2.2k GitHub stars and 233 forks as of fetch date. MIT License. No fixed random seeds are used (the test is deterministic given fixed API outputs).

### Key Results

**GPT-4-128K** (2 models tested, single needle text, single evaluator -- limited evidence):

| Condition | Performance |
|---|---|
| Context < 73K tokens | Near-perfect recall across all depths |
| Context > 73K tokens | Degradation begins |
| Depth 7%--50%, context > 73K | Low recall (failure region) |
| Depth 0% (first sentence) | ~100% recall regardless of context length |
| Depth > 50% (second half) | Generally good recall |

- Retrieval performance started to degrade above **73K tokens** (GPT-4-128K heatmap, X thread November 8).
- The primary failure region was at **7%--50% document depth** for longer contexts: the model overlooked needles placed in the early-to-middle portion of the document (GPT-4-128K heatmap).
- Facts placed at the **very beginning** (depth 0%) were recalled reliably at all context lengths, consistent with a "beginning-of-document advantage" (X thread November 8).
- Facts in the **second half** of the document were also recalled relatively well, consistent with recency bias (GPT-4-128K heatmap).

**Claude 2.1** (single model, single needle text -- limited evidence):

| Condition | Performance |
|---|---|
| Depth 0% (top of document) | ~100% accuracy |
| Depth ~100% (bottom of document) | ~100% accuracy at shorter contexts |
| Context > 90K tokens, bottom depths | Degradation begins |
| Mid-document depths, longer contexts | Unreliable recall |

- Top and bottom document positions showed approximately 100% accuracy (Claude 2.1 heatmap, X thread November 21).
- Degradation was significant starting around **90K tokens**, particularly for facts at the document's end positions (X thread November 21).
- Mid-document recall was unreliable, consistent with the "lost in the middle" phenomenon observed with GPT-4 (X thread November 21).
- Performance at low context lengths was not guaranteed to be perfect either, indicating retrieval failures are not solely a function of context length (X thread November 21).
- The GitHub repository's Anthropic prompt template includes the assistant prefix `"Here is the most relevant sentence in the context:"` which serves as a retrieval directive. Anthropic identified that Claude 2.1's training to refuse answering when evidence seems insufficient caused it to abstain rather than retrieve the out-of-place needle; including this directive substantially improved accuracy. The widely cited figures of **27% baseline accuracy** and **98% accuracy with the directive** originate from the Anthropic follow-up analysis (November 2023) and the broader discussion around these results; they are not directly reported in the captured X thread text.

### Impact and Adoption

Despite being an informal contribution, NIAH became one of the most influential long-context evaluation methods:

1. **RULER (Hsieh et al., 2024):** Directly extends NIAH along three axes -- diverse needle/haystack types, multi-key distractors, and multi-value/multi-query retrieval -- to create a comprehensive synthetic benchmark.
2. **BABILong (Kuratov et al., 2024):** Introduces "reasoning-in-a-haystack" tasks that go beyond NIAH's single-fact retrieval.
3. **NoLiMa (Vodrahalli et al., 2025):** Identifies NIAH's lexical overlap limitation and constructs a benchmark requiring semantic rather than surface-level retrieval.
4. **Llama 3.1 technical report (Meta, 2024):** Uses a 4-needle variant of NIAH for official long-context evaluation.
5. **An et al. (2025) -- *STRING:*** Uses 4-needle NIAH (following Llama 3.1) as the primary evaluation for training-free context extension methods.
6. **Gelberg et al. (2025) -- *DroPE:*** References NIAH as the foundational long-context retrieval evaluation.
7. **Community forks:** Arize AI, LangChain, and others extended the framework to support additional models, multi-needle evaluation, and integration with evaluation platforms.

---

## Limitations and Failure Modes

1. **[Inferred] Single-needle only.** The test inserts exactly one fact and asks one question. It does not evaluate multi-fact reasoning, aggregation, or multi-hop retrieval. RULER (Hsieh et al., 2024) later addressed this with multi-needle variants.

2. **[Inferred] High lexical overlap between question and needle.** The question ("What is the best thing to do in San Francisco?") shares significant lexical overlap with the needle, enabling surface-level token matching rather than deep comprehension. NoLiMa (Vodrahalli et al., 2025) later quantified this: vanilla NIAH has ROUGE-1 precision of 0.905 between question and context.

3. **[Inferred] Out-of-context needle.** The needle is topically unrelated to the haystack, which may either make it easier to find (it stands out) or harder (the model may dismiss it as irrelevant, as occurred with Claude 2.1's refusal behavior).

4. **[Inferred] LLM-as-judge evaluation.** The evaluation relies on an LLM judge (described as GPT-4 in the X threads; the GitHub code defaults to `gpt-3.5-turbo-0125`). This introduces potential scoring noise and evaluator bias compared to exact-match evaluation. No inter-annotator agreement or evaluator calibration metrics are reported.

5. **[Inferred] Two models only.** The original tests covered only GPT-4-128K and Claude 2.1. No ablation across model families, sizes, or architectures was performed. Community forks (e.g., Arize AI) later extended testing to additional models.

6. **[Inferred] No reasoning or synthesis tasks.** NIAH tests pure retrieval -- whether the model can locate and return a specific fact. It does not test whether the model can use retrieved information for downstream reasoning, summarization, or multi-step computation.

7. **[Inferred] Fixed needle text.** The same needle sentence is used across all evaluations, which could allow specific failure patterns related to that particular text rather than reflecting general retrieval capability. No sensitivity analysis over needle content is reported.

8. **[Inferred] No variance estimates.** Each (depth, length) combination is evaluated once per model. No repeated trials, confidence intervals, or statistical testing are reported. Results may be sensitive to API stochasticity despite `temperature=0`.

Note: Kamradt does not formally discuss limitations in the X threads or README. All limitations above are analyst inferences based on the experimental design.

#### Scope and Comparability

- **What was not tested:** Only two models were evaluated (GPT-4-128K and Claude 2.1). No open-source models, no models at smaller scales, and no models from other providers (e.g., Google, Mistral) were tested in the original evaluation. Only one needle text and one retrieval question were used. Only English-language content was tested.
- **Comparability notes:** The Anthropic prompt template includes the assistant prefix `"Here is the most relevant sentence in the context:"` (GitHub repository, `Anthropic_prompt.txt`), which acts as a retrieval directive. The OpenAI prompt does not include such a directive. This asymmetry in prompting means the two models were not tested under identical conditions. The evaluator model may also differ between the original X thread tests (described as GPT-4) and the default in the released code (`gpt-3.5-turbo-0125`). The scoring rubric uses a 1--10 scale, not binary pass/fail, making direct comparison with subsequent benchmarks using accuracy metrics (e.g., RULER, BABILong) non-trivial. Grid resolution also differs: 15x15 for GPT-4 vs. 35x35 for Claude 2.1, meaning the granularity of failure region identification is coarser for GPT-4.

---

## Conclusions

### Contributions

1. **Simple retrieval test exposes context window limitations.** A single-fact retrieval task across a systematic depth-length grid revealed that models fail to utilize large portions of their claimed context windows, despite marketing claims of 128K--200K token support (GPT-4 and Claude 2.1 heatmaps). Evidence from 2 models, single needle text (limited evidence).

2. **Position-dependent failure patterns documented.** Both GPT-4 and Claude 2.1 exhibited strong position-dependent performance: reliable retrieval at context boundaries (beginning and end) with degradation in the middle, consistent with the "lost in the middle" phenomenon documented by Liu et al. (2023) but observed at much longer context lengths (GPT-4 and Claude 2.1 heatmaps).

3. **Prompt sensitivity demonstrated.** Claude 2.1's accuracy changed dramatically with a prompt directive, demonstrating that NIAH results are sensitive to prompt engineering and that apparent retrieval failures may reflect model calibration (refusal to answer from insufficient evidence) rather than inability to locate the information (Anthropic follow-up analysis, November 2023). Tested on Claude 2.1 only (limited evidence for generalizability).

4. **Heatmap visualization established as diagnostic standard.** The depth-length heatmap format provided an intuitive way to identify failure regions and became the standard visualization for long-context evaluation results across subsequent work (adopted by RULER, BABILong, Llama 3.1 report, and others).

5. **Open-source framework for reproducible evaluation.** The `needlehaystack` Python package supports OpenAI, Anthropic, and Cohere providers with configurable needle text, haystack material, grid resolution, and both single-needle and multi-needle evaluation modes (GitHub repository, MIT License).

### Implications

1. **Claimed context length does not equal effective context length.** The finding that GPT-4-128K degrades above 73K tokens suggests that effective context is substantially shorter than the marketed maximum. [Inference: this observation motivated the "effective context length" concept formalized by RULER (Hsieh et al., 2024) and An et al. (2025).]

2. **Evaluation methodology shapes conclusions.** Claude 2.1's large accuracy swing with a single prompt change suggests that benchmark results are highly sensitive to evaluation protocol, and that poor benchmark performance may not reflect true capability limitations. [Inference: the Anthropic prompt template's inclusion of a retrieval directive complicates interpretation of the "baseline" vs. "improved" comparison.]

3. **Surface-level retrieval may be insufficient as a capability test.** The high lexical overlap between needle and question means NIAH primarily tests token matching rather than semantic comprehension. [Inference: this limitation, later quantified by NoLiMa, suggests that models passing NIAH may still fail at real-world long-context tasks requiring deeper understanding.]

---

## Key Claims

1. **C1: GPT-4-128K retrieval degrades above 73K tokens.** Despite supporting 128K token context, GPT-4 showed degraded retrieval performance when contexts exceeded approximately 73K tokens. Evidence: GPT-4-128K heatmap (November 8, 2023 X thread). Scope: GPT-4-128K (gpt-4-1106-preview), single-needle retrieval, Paul Graham essay haystack, 15x15 grid. Magnitude: near-perfect recall below 73K, degraded above. Status: **supported** (single model, single needle -- limited evidence).

2. **C2: GPT-4-128K fails primarily at 7--50% document depth.** For contexts above 73K tokens, the model failed to retrieve needles placed in the early-to-middle portion (7%--50% depth) while maintaining recall at the beginning and second half. Evidence: GPT-4-128K heatmap. Scope: GPT-4-128K, contexts above 73K tokens. Magnitude: low recall at 7--50% depth vs. near-perfect at 0% and >50%. Status: **supported** (single model, single needle -- limited evidence).

3. **C3: Claude 2.1 achieves 27% baseline retrieval accuracy.** Across the full 200K context window with the standard prompt, Claude 2.1 correctly retrieved the needle only 27% of the time. Evidence: Claude 2.1 heatmap (X thread November 21) and Anthropic follow-up analysis. Note: the 27% figure is from the Anthropic follow-up discussion, not directly reported in the captured X thread text. Scope: Claude 2.1 200K, baseline prompt without retrieval directive, 35x35 grid. Magnitude: 27% overall accuracy. Status: **supported** (single model, single needle -- limited evidence).

4. **C4: Prompt directive improves Claude 2.1 from 27% to 98%.** Adding the assistant prefix `"Here is the most relevant sentence in the context:"` to the prompt caused Claude 2.1's retrieval accuracy to jump from 27% to 98%. Anthropic explained this was due to the model's calibration toward refusing when evidence seems insufficient. Evidence: Anthropic follow-up analysis (November 2023); prompt template in GitHub repository. Note: the 98% figure is from the Anthropic follow-up, not directly in the captured source files. Scope: Claude 2.1 200K, specific retrieval directive. Magnitude: +71 percentage points (27% to 98%). Status: **supported** (single model, single directive -- limited evidence for generalizability).

5. **C5: Boundary positions are recalled reliably.** Facts placed at the very beginning (depth 0%) were recalled near-perfectly regardless of context length for both GPT-4 and Claude 2.1. Evidence: GPT-4 and Claude 2.1 heatmaps. Scope: both models, depth 0%. Magnitude: ~100% recall at depth 0% across all context lengths. Status: **supported** (2 models -- moderate evidence for the specific pattern).

6. **C6: Position-dependent patterns are consistent across model families.** Both GPT-4 (OpenAI) and Claude 2.1 (Anthropic) exhibited the same qualitative pattern: reliable retrieval at context boundaries with degradation in the middle, despite different providers and model families. Evidence: comparison of both heatmaps. Scope: 2 models only, single needle text with fixed question. Magnitude: qualitative pattern consistency. Status: **supported** (2 models from different providers -- moderate evidence for qualitative pattern, but limited model diversity).

---

## Open Questions

1. **Does the single-needle, high-lexical-overlap design overestimate model retrieval capabilities compared to real-world information needs?** NIAH tests one fact with high question-needle overlap. Real-world use cases involve retrieving information with indirect or paraphrased queries. Addressed by NoLiMa (Vodrahalli et al., 2025), which showed that models passing NIAH fail on low-overlap retrieval.

2. **How much of the position-dependent retrieval failure is due to attention mechanism limitations vs. training data distribution?** NIAH reveals the failure pattern but does not identify the mechanism. Is the "lost in the middle" effect caused by positional encoding decay, attention dilution, or training data biases toward beginning and end positions? Not yet addressed.

3. **Does prompt engineering systematically mitigate positional retrieval failures across all model families, or is Claude 2.1's sensitivity a special case?** The dramatic accuracy improvement with a prompt directive was demonstrated only for Claude 2.1. It is unknown whether similar techniques would help GPT-4's failure regions or other models. Not yet addressed.

4. **Can NIAH-style evaluation distinguish between models that truly comprehend long contexts vs. those that only perform surface-level token matching?** The high lexical overlap allows retrieval via token matching rather than semantic understanding. Addressed by RULER (Hsieh et al., 2024), which showed that near-perfect NIAH scores do not predict performance on harder tasks.

---

## Core References and Why They Are Referenced

### Predecessor Work

- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Documented the U-shaped positional bias in multi-document QA at shorter context lengths. NIAH extends this analysis to full context windows (128K--200K tokens) with a simpler, more controlled single-needle protocol.

- **Mohtashami & Jaggi (2023)** -- *Random-Access Infinite Context Length for Transformers (Landmark Attention).* Introduced passkey retrieval -- inserting a random passkey in a long context and asking the model to retrieve it -- which is a direct predecessor to NIAH. NIAH uses natural language rather than random strings and varies depth systematically.

### Models Evaluated

- **OpenAI (2023)** -- *GPT-4 Turbo (gpt-4-1106-preview).* The first model tested with NIAH, supporting 128K tokens. Showed degradation above 73K tokens with failures concentrated at 7%--50% depth.

- **Anthropic (2023)** -- *Claude 2.1.* The second model tested, supporting 200K tokens. The Claude 2.1 results generated significant discussion about the distinction between retrieval capability and model calibration.

### Haystack Corpus

- **Paul Graham** -- *Essays (paulgraham.com).* 49 essays used as the haystack corpus, providing topically unrelated background text (GitHub repository).

### Evaluation Infrastructure

- **LangChain** -- Evaluation chains used for automated LLM-based scoring of model responses via `labeled_score_string` evaluator, enabling assessment of paraphrased correct answers.

### Subsequent Benchmarks Building on NIAH

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Extends NIAH with multi-key, multi-value, and multi-query variants plus non-retrieval tasks (variable tracing, aggregation, QA). Showed that near-perfect NIAH scores do not predict performance on harder tasks.

- **Kuratov et al. (2024)** -- *BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack.* Extends the paradigm from retrieval to multi-hop reasoning over facts distributed across long contexts.

- **Vodrahalli et al. (2025)** -- *NoLiMa: Long-Context Evaluation Beyond Literal Matching.* Identifies that NIAH's high lexical overlap (ROUGE-1 = 0.905) between question and needle allows surface-level matching, and constructs a benchmark requiring semantic retrieval.

- **An et al. (2025)** -- *Why Does the Effective Context Length of LLMs Fall Short?* Uses 4-needle NIAH as the primary evaluation in STRING experiments, referencing it as "gkamradt 2023."
