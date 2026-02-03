# Needle In A Haystack -- Pressure Testing LLMs

**Author:** Greg Kamradt
**Date:** November 2023
**Type:** X (Twitter) posts + GitHub repository (not a formal peer-reviewed paper)
**URL:** https://github.com/gkamradt/LLMTest_NeedleInAHaystack

The NIAH test became the de facto standard for evaluating long-context retrieval in LLMs. Multiple peer-reviewed papers cite it directly (RULER, BABILong, NoLiMa, DroPE) and the methodology was adopted in official model reports (e.g., Meta's Llama 3.1 technical report uses a 4-needle variant).

---

## Core Research Problem

By late 2023, LLM context windows were expanding rapidly -- GPT-4 Turbo supported 128K tokens and Claude 2.1 supported 200K tokens. Model providers marketed these as enabling long-document understanding, but **no standardized test existed for verifying whether models could actually retrieve information from arbitrary positions within these large context windows**. Prior work by Liu et al. (2023) -- *Lost in the Middle* -- had demonstrated a U-shaped performance curve in multi-document QA, but that study used at most ~6K tokens of context and focused on retrieval-augmented generation settings with multiple documents. The core challenge was: **how to pressure-test whether LLMs can reliably retrieve a single piece of information placed at any depth within their full claimed context window.**

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
2. Construct the haystack by concatenating Paul Graham essays (218 essays total, providing sufficient text to reach 200K tokens when repeated).
3. Insert the needle at the specified depth within the haystack.
4. Prompt the model with the combined text and a retrieval question.
5. Evaluate the model's response using GPT-4 as a judge (via LangChain evals).
6. Repeat across all combinations of depth and length intervals.

**Needle text:** "The best thing to do in San Francisco is eat a sandwich and sit in Dolores Park on a sunny day."

**Retrieval question:** "What is the best thing to do in San Francisco?" (using only the provided context).

The needle is deliberately out-of-place relative to the Paul Graham essays (which discuss startups, great work, and related topics), ensuring that retrieval cannot be accomplished through topical association alone.

### Key Technical Components

- **Depth parameterization:** Document depth is expressed as a percentage (0%--100%). The needle is inserted at the character position corresponding to that percentage of the total haystack length.
- **Context length parameterization:** The haystack is constructed to a target token count by concatenating essays and truncating. Tested from 1K tokens up to each model's maximum.
- **Grid resolution:** The GPT-4-128K test used 15 depth intervals x 15 context length intervals (225 total evaluations). The Claude 2.1-200K test used 35 x 35 intervals (1,225 evaluations).
- **Automated evaluation:** Model responses are scored by GPT-4 using LangChain evaluation chains, rather than exact string matching, allowing for paraphrased correct answers.
- **Heatmap output:** Results are displayed as a 2D heatmap with context length on the x-axis and document depth on the y-axis, with color indicating retrieval accuracy.

### Experimental Setup

**Models evaluated:**

| Model | Max Context | Date Tested | Grid Size |
|---|---|---|---|
| GPT-4-128K (gpt-4-1106-preview) | 128K tokens | November 8, 2023 | 15 x 15 |
| Claude 2.1 | 200K tokens | November 21, 2023 | 35 x 35 |

**Haystack material:** Paul Graham essays (218 essays).

**Cost:** Approximately $1,016 in API calls for the Claude 2.1 test ($8 per million tokens).

### Key Results

**GPT-4-128K:**

| Condition | Performance |
|---|---|
| Context < 73K tokens | Near-perfect recall across all depths |
| Context > 73K tokens | Degradation begins |
| Depth 7%--50%, context > 73K | Low recall (failure region) |
| Depth 0% (first sentence) | ~100% recall regardless of context length |
| Depth > 50% (second half) | Generally good recall |

- Recall performance started to degrade above **73K tokens**.
- The primary failure region was at **7%--50% document depth** for longer contexts: the model overlooked needles placed in the early-to-middle portion of the document.
- Facts placed at the **very beginning** (depth 0%) were recalled reliably at all context lengths.
- Facts in the **second half** of the document were also recalled relatively well, consistent with recency bias.

**Claude 2.1:**

| Condition | Performance |
|---|---|
| Overall retrieval accuracy (baseline prompt) | 27% |
| Depth 0% (first sentence) | ~100% accuracy |
| Depth ~100% (bottom of document) | ~100% accuracy at short contexts |
| Context > 90K, bottom depths | Degradation begins |
| With prompt directive ("Here is the most relevant sentence in the context:") | 98% accuracy |

- Initial testing yielded only **27% overall retrieval accuracy**.
- Near-perfect accuracy at document extremes (top and bottom), with severe degradation in the middle and at longer contexts.
- Starting at ~90K tokens, performance at the bottom of the document also degraded.
- Anthropic identified that Claude 2.1's training to refuse answering when evidence seems insufficient caused it to abstain rather than retrieve the out-of-place needle. Adding a single prompt directive ("Here is the most relevant sentence in the context:") improved accuracy from **27% to 98%**.

### Practical Implications

The original posts drew three takeaways:

1. **No guarantees on retrieval.** Facts placed in long contexts are not guaranteed to be retrieved, even well within the model's claimed context window.
2. **Less context = more accuracy.** Shorter contexts generally yield more reliable retrieval.
3. **Position matters.** Facts at the very beginning and in the second half of the document are recalled more reliably than facts in the early-to-middle region.

### Limitations

1. **Single-needle only.** The test inserts exactly one fact and asks one question. It does not evaluate multi-fact reasoning, aggregation, or multi-hop retrieval.
2. **Lexical overlap between question and needle.** The question ("What is the best thing to do in San Francisco?") shares significant lexical overlap with the needle, enabling surface-level token matching rather than deep comprehension. NoLiMa (Vodrahalli et al., 2025) later quantified this: vanilla NIAH has ROUGE-1 precision of 0.905 between question and context.
3. **Out-of-context needle.** The needle is topically unrelated to the haystack, which may either make it easier to find (it stands out) or harder (the model may dismiss it as irrelevant, as occurred with Claude 2.1).
4. **LLM-as-judge evaluation.** Using GPT-4 as an evaluator introduces potential scoring noise compared to exact-match evaluation.
5. **Two models only.** The original tests covered only GPT-4 and Claude 2.1. Community forks (e.g., Arize AI) later extended testing to additional models.

### Impact and Adoption

Despite being an informal contribution, NIAH became one of the most influential long-context evaluation methods:

1. **RULER (Hsieh et al., 2024):** Directly extends NIAH along three axes -- diverse needle/haystack types, multi-key distractors, and multi-value/multi-query retrieval -- to create a comprehensive synthetic benchmark.
2. **BABILong (Kuratov et al., 2024):** Introduces "reasoning-in-a-haystack" tasks that go beyond NIAH's single-fact retrieval.
3. **NoLiMa (Vodrahalli et al., 2025):** Identifies NIAH's lexical overlap limitation and constructs a benchmark requiring semantic rather than surface-level retrieval.
4. **Llama 3.1 technical report (Meta, 2024):** Uses a 4-needle variant of NIAH for official long-context evaluation.
5. **An et al. (2025) -- STRING:** Uses 4-needle NIAH (following Llama 3.1) as the primary evaluation for training-free context extension methods.
6. **Gelberg et al. (2025) -- DroPE:** References NIAH as the foundational long-context retrieval evaluation.
7. **Community forks:** Arize AI, LangChain, and others extended the framework to support additional models, multi-needle evaluation, and integration with evaluation platforms.

---

## Conclusions

1. **Simple retrieval test exposes context window limitations.** A single-fact retrieval task across a systematic depth-length grid revealed that models fail to utilize large portions of their claimed context windows, despite marketing claims of 128K--200K token support.

2. **Position-dependent failure patterns.** Both GPT-4 and Claude 2.1 exhibited strong position-dependent performance: reliable retrieval at context boundaries (beginning and end) with degradation in the middle, consistent with the "lost in the middle" phenomenon documented by Liu et al. (2023).

3. **Prompt sensitivity.** Claude 2.1's accuracy jumped from 27% to 98% with a single prompt directive, demonstrating that NIAH results are sensitive to prompt engineering and that apparent retrieval failures may reflect model calibration (refusal to answer from insufficient evidence) rather than inability to locate the information.

4. **Heatmap visualization as a diagnostic tool.** The depth-length heatmap format provided an intuitive way to identify failure regions and became the standard visualization for long-context evaluation results.

5. **Foundation for subsequent benchmarks.** NIAH established the "needle-in-a-haystack" paradigm that RULER, BABILong, NoLiMa, and other benchmarks directly build upon, each addressing specific limitations (multi-hop reasoning, lexical overlap, task diversity) while retaining the core depth-length sweep methodology.

---

## Core References and Why They Are Referenced

### Predecessor Work
- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Documented the U-shaped positional bias in multi-document QA at shorter context lengths (~2K--6K tokens). NIAH extends this analysis to full context windows (128K--200K tokens) with a simpler, more controlled single-needle protocol.
- **Mohtashami & Jaggi (2023)** -- *Random-Access Infinite Context Length for Transformers (Landmark Attention).* Introduced passkey retrieval -- inserting a random passkey in a long context and asking the model to retrieve it -- which is a direct predecessor to NIAH. NIAH uses natural language rather than random strings and varies depth systematically.

### Models Evaluated
- **OpenAI (2023)** -- *GPT-4 Turbo (gpt-4-1106-preview).* The first model tested with NIAH, supporting 128K tokens.
- **Anthropic (2023)** -- *Claude 2.1.* The second model tested, supporting 200K tokens. The Claude 2.1 results (27% baseline, 98% with prompt optimization) generated significant discussion about the distinction between retrieval capability and model calibration.

### Evaluation Infrastructure
- **LangChain** -- Evaluation chains used for automated GPT-4-based scoring of model responses.

### Subsequent Benchmarks Building on NIAH
- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Extends NIAH with multi-key, multi-value, and multi-query variants plus non-retrieval tasks (variable tracing, aggregation, QA).
- **Kuratov et al. (2024)** -- *BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack.* Extends the paradigm from retrieval to multi-hop reasoning over facts distributed across long contexts.
- **Vodrahalli et al. (2025)** -- *NoLiMa: Long-Context Evaluation Beyond Literal Matching.* Identifies that NIAH's high lexical overlap (ROUGE-1 = 0.905) between question and needle allows surface-level matching, and constructs a benchmark requiring semantic retrieval.
- **An et al. (2025)** -- *Why Does the Effective Context Length of LLMs Fall Short?* Uses 4-needle NIAH as the primary evaluation in STRING experiments, referencing it as "gkamradt 2023."

#### Cross-References in Available Papers

- **Lost in the Middle (2024-02-lost-in-the-middle):** NIAH and Lost in the Middle are complementary: Lost in the Middle uses multi-document QA at shorter contexts (~2K--6K tokens) with multiple distractors, showing the U-shaped curve. NIAH uses single-needle retrieval at full context scale (128K--200K tokens) with a simpler protocol. Lost in the Middle does not cite NIAH (it precedes NIAH in the arXiv timeline, July 2023 vs. November 2023), but both establish the same core finding -- models struggle with information in the middle of their context.
- **RULER (2024-10-ruler-context-size):** RULER directly cites Kamradt (2023) as the "vanilla NIAH test" that it extends (Section 2). RULER's S-NIAH task replicates the basic needle retrieval setup, and RULER adds MK-NIAH (multi-key), MV-NIAH (multi-value), and MQ-NIAH (multi-query) variants. RULER demonstrates that near-perfect vanilla NIAH performance does not predict performance on harder tasks.
- **BABILong (2024-12-babilong-long-context-reasoning):** BABILong cites Kamradt (2023) as the vanilla NIAH test that it addresses as "overly simplistic," replacing single-fact retrieval with multi-fact reasoning tasks from the bAbI suite.
- **NoLiMa (2025-07-nolima-long-context-evaluation):** NoLiMa directly cites Kamradt (2023) and quantifies NIAH's limitation: ROUGE-1 precision of 0.905 between question and context, vs. NoLiMa's 0.069. NoLiMa's "Direct" ablation condition replicates vanilla NIAH to demonstrate how literal matches simplify the task.
- **Effective Context Length Falls Short (2025-04-effective-context-length-falls-short):** References "gkamradt 2023" as the foundational NIAH test. Uses a 4-needle variant (following the Llama 3.1 report) as one of two primary evaluation benchmarks. STRING improves NIAH (4-needle) performance by an average of 18 points across seven models.
- **DroPE (2025-12-drope-dropping-positional-embeddings):** References Kamradt (2023) as the "original NIAH evaluation framework for pressure-testing LLM context utilization." Uses RULER's NIAH variants (which build on Kamradt's design) for zero-shot long-context evaluation.
- **Context Length Hurts Performance (2025-11-context-length-hurts-performance):** Uses Paul Graham Essays from Kamradt (2023) as "essay distraction tokens" in their distraction experiments, directly building on the NIAH haystack material.
