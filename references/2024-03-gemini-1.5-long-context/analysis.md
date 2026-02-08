---
title: "Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens of Context"
authors: "Reid, Savinov, Teplyashin, Lepikhin, Lillicrap, et al."
year: 2024
venue: "arXiv preprint 2024"
paper_type: preprint
categories: ["long-context-evaluation", "model-release", "architecture", "in-context-learning", "benchmarking"]
scope: ["multimodal long-context", "mixture-of-experts", "million-token context windows", "long-context retrieval"]
benchmarks_used: ["niah", "mrcr", "mtob", "mmlu", "humaneval", "gsm8k", "hellaswag", "bbh", "wmt-translation", "math-hendrycks", "gpqa", "egoschema", "drop", "mmmu", "mgsm"]
models_introduced: ["gemini-1.5-pro", "gemini-1.5-flash"]
models_evaluated: ["gemini-1.5-pro", "gemini-1.5-flash", "gpt-4", "claude-2.1", "gpt-3.5-turbo", "gemini-pro"]
key_claims:
  - id: C1
    claim: "Gemini 1.5 Pro achieves >99% recall on needle-in-a-haystack retrieval up to at least 10M tokens across text, video, and audio modalities"
    evidence: "Figure 1, Section 5 (100% text recall up to 530K, >99.7% at 1M, 99.2% at 10M; 100% audio recall; >99.8% video recall up to 2M tokens)"
    status: supported
    scope: "synthetic single-needle retrieval task, greedy decoding, Paul Graham essays haystack (text), AlphaGo documentary (video), VoxPopuli (audio)"
    magnitude: "100% text recall up to 530K, >99.7% at 1M, 99.2% at 10M; 100% audio at 107h; 100% video at 10.5h"
  - id: C2
    claim: "Next-token prediction loss follows a power law L(x) = alpha * x^beta + gamma with context length, holding up to at least 1M tokens for documents and 10M tokens for code"
    evidence: "Figure 7, Section 5.1 (R^2 = 0.997 for documents, R^2 = 0.995 for code)"
    status: supported
    scope: "held-out long documents up to 1M tokens, code repositories up to 10M tokens, instruction-tuned checkpoint"
    magnitude: "R^2 = 0.997 (documents), R^2 = 0.995 (code); power-law fit deviates near 10M for code"
  - id: C3
    claim: "Gemini 1.5 Pro matches or surpasses Gemini 1.0 Ultra on 78% of core capability benchmarks while using significantly less training compute"
    evidence: "Table 1 (35/45 wins across text, vision, audio)"
    status: supported
    scope: "45 core capability benchmarks spanning text (19), vision (21), audio (5); greedy decoding"
    magnitude: "35/45 wins (77.8%); main gains in math/science (+18.1%), charts & documents (+39.6%); main losses in audio ASR (-3.8%), AST (-3.9%)"
  - id: C4
    claim: "Given a Kalamang grammar book (~250K tokens) in context, Gemini 1.5 Pro learns to translate at a level approaching a human learner"
    evidence: "Tables 4-5 (kgv-to-eng: 4.00 vs 5.52 human; eng-to-kgv: 5.46 vs 5.60 human on 0-6 scale)"
    status: supported
    scope: "single language (Kalamang), ~250K tokens of grammar + dictionary + parallel sentences, single human evaluator"
    magnitude: "kgv-to-eng: 4.00 vs 5.52 human (gap 1.52); eng-to-kgv: 5.46 vs 5.60 human (gap 0.14) on 0-6 scale"
  - id: C5
    claim: "Gemini 1.5 Pro performance improves monotonically with more in-context examples on planning tasks, while GPT-4 Turbo plateaus or degrades"
    evidence: "Figure 16 (Logistics, Mini-Grid, Trip Planning, Calendar Scheduling)"
    status: supported
    scope: "4 planning tasks (Logistics, Mini-Grid, Trip Planning, Calendar Scheduling), up to 400-600 shots, greedy decoding"
    magnitude: "Mini-Grid 1-shot 28% to 400-shot 77%; Calendar Scheduling 1-shot 33% to 100-shot 52%; GPT-4 Turbo degrades after ~80 shots on Logistics"
  - id: C6
    claim: "Full-context (710K tokens) Gemini 1.5 Pro dramatically outperforms RAG-augmented baselines on long-document QA"
    evidence: "Figure 14 (Bradley-Terry strength 6.24 vs 1.77 for RAG Gemini 1.5 Pro, 1.64 for RAG GPT-4 Turbo)"
    status: supported
    scope: "single book (Les Miserables, 710K tokens), 100 auto-generated questions, TF-IDF retrieval with 4K-token chunks, auto-rater evaluation"
    magnitude: "Bradley-Terry strength 6.24 vs 1.77 (RAG 1.5 Pro) vs 1.64 (RAG GPT-4 Turbo); wins 78% vs own RAG, 83% vs RAG GPT-4 Turbo"
  - id: C7
    claim: "Gemini 1.5 Flash, online-distilled from 1.5 Pro, outperforms Gemini 1.0 Pro on 82% of core benchmarks while being substantially faster"
    evidence: "Table 2 (41/50 wins); Table 3 (>650 chars/sec English, >30% faster than Claude 3 Haiku)"
    status: supported
    scope: "50 core benchmarks spanning text, vision, audio; latency measured on Vertex AI streaming API with 10K-char inputs"
    magnitude: "41/50 wins (82%); 1.5 ms/char English (vs 2.2 for Claude 3 Haiku); >650 chars/sec English"
  - id: C8
    claim: "On 1H-VideoQA, Gemini 1.5 Pro at full 1fps achieves 72.2% accuracy vs 52.3% for GPT-4V at 150 frames, showing performance continues scaling with more frames"
    evidence: "Table 9, Figure 15"
    status: supported
    scope: "125 five-way MCQ over 40-105 minute public videos, zero-shot, 1fps frame extraction"
    magnitude: "72.2% at full 1fps vs 52.3% GPT-4V at 150 frames; 45.2% vs 36.5% at 16 frames; EgoSchema saturates at 16 frames"
cross_references:
  - target: 2023-11-needle-in-a-haystack
    type: extends
    detail: "Gemini 1.5 extends single-needle NIAH to multimodal (text, video, audio) and multi-needle variants at up to 10M tokens, far beyond the original text-only evaluation"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "RULER evaluates Gemini 1.5 Pro and finds it achieves the highest average score (95.8%) with effective length exceeding 128K tokens across 13 tasks"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong evaluates Gemini 1.5 Pro on reasoning-in-a-haystack tasks; achieves ~64K effective context on QA1, among the top-performing models"
  - target: 2025-07-nolima-long-context-evaluation
    type: complementary
    detail: "NOLIMA evaluates Gemini 1.5 Pro on latent associative reasoning without literal matches; effective length drops to 2K, suggesting literal matching inflates reported capabilities"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: complementary
    detail: "LongICLBench evaluates Gemini 1.5 Pro on extreme-label ICL; one of the only models achieving non-zero performance on the hardest 174-class Discovery task"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Lost in the Middle documents position-dependent performance degradation; Gemini 1.5's MRCR evaluation tests a related phenomenon with adversarially similar needles"
  - target: 2025-04-effective-context-length-falls-short
    type: complementary
    detail: "STRING identifies that effective context length falls short of claimed length due to training distribution bias; relevant to whether Gemini 1.5's 10M token claim translates to effective capability"
  - target: 2025-11-context-length-hurts-performance
    type: complementary
    detail: "Evaluates Gemini 2.0 (successor) and finds it shows better robustness than open-source models but still exhibits context-length-induced degradation"
open_questions:
  - question: "What specific architectural changes enable 10M-token context without performance degradation? The paper describes only 'a series of significant architecture changes' without enumeration."
    addressed_by: null
  - question: "Does Gemini 1.5's near-perfect NIAH recall at 10M tokens transfer to complex reasoning tasks requiring information integration across the full context?"
    addressed_by: 2025-07-nolima-long-context-evaluation
  - question: "Why does the power-law relationship between NLL and context length hold so precisely (R^2 > 0.995), and does this reflect a fundamental property of Transformer architectures or training data structure?"
    addressed_by: null
  - question: "Can the full-context advantage over RAG (Figure 14) be maintained as retrieval systems improve, or will RAG close the gap at lower compute cost?"
    addressed_by: null
  - question: "Can the in-context translation capability generalize beyond Kalamang to other complex skill acquisition tasks requiring structured reasoning from novel material?"
    addressed_by: null
---
# Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens of Context

**Authors:** Gemini Team, Google DeepMind (1000+ contributors; led by Machel Reid, Nikolay Savinov, Denis Teplyashin, Dmitry Lepikhin, Timothy Lillicrap, et al.)
**Date:** March 2024, arXiv:2403.05530 (v1--v5, December 2024)

---

## Core Research Problem

At the time of publication, state-of-the-art LLMs were limited to relatively short context windows -- Claude 3.0 at 200K tokens and GPT-4 Turbo at 128K tokens. Even models with extended context windows often suffered from degraded retrieval and reasoning performance as context length grew. Prior long-context work focused primarily on text, with no system capable of natively handling millions of tokens across text, video, and audio simultaneously with high fidelity.

Existing evaluation suites were also insufficient. Benchmarks typically focused on individual modalities and were restricted to tasks with shorter context lengths, failing to stress-test the new capabilities of frontier multimodal models.

The core challenge was: **how to build a multimodal model that can recall and reason over fine-grained information from millions of tokens of context -- spanning long documents, hours of video, and hours of audio -- without degrading core capabilities or requiring retrieval-augmented pipelines.**

---

## Problem Solutions

Gemini 1.5 addresses this through a family of two models built on a sparse mixture-of-experts (MoE) Transformer architecture, with improvements across the entire model stack:

1. **Sparse MoE architecture** (Gemini 1.5 Pro) that uses learned routing to activate a subset of parameters per input, enabling large total parameter count with constant per-input compute.
2. **Undisclosed architectural changes** enabling long-context understanding up to 10M tokens without performance degradation.
3. **Online distillation** (Gemini 1.5 Flash) from the larger Pro model for efficiency with minimal quality regression.
4. **Multimodal natively** -- text, image, video, audio, and code are interleaved in a single input sequence rather than handled by separate modality-specific systems.

---

## Approach Details

### Method

**Gemini 1.5 Pro** is a sparse mixture-of-experts Transformer-based model building on Gemini 1.0's multimodal capabilities and a long history of MoE research at Google (Shazeer et al., 2017; Lepikhin et al., 2020; Fedus et al., 2021; Du et al., 2022; Zoph et al., 2022). MoE models use a learned routing function to direct inputs to a subset of parameters for processing, allowing total parameter count to grow while keeping activated parameters constant per input.

**Gemini 1.5 Flash** is a dense Transformer decoder model online-distilled from Gemini 1.5 Pro (Hinton et al., 2015; Agarwal et al., 2024b). It uses parallel computation of attention and feedforward components (following the PaLM pattern from Chowdhery et al., 2023b) and is trained with higher-order preconditioned methods for improved quality.

The paper does not disclose total parameter counts, active parameter counts, number of experts, expert capacity, routing mechanism details, or the positional encoding scheme. The specific architectural changes enabling 10M-token context are described only as "a series of significant architecture changes" without enumeration.

### Key Technical Components

**Training infrastructure.** Both models are trained on multiple 4096-chip pods of Google's TPUv4 accelerators using JAX with XLA and the GSPMD partitioner for automatic parallelism. Training uses the "single controller" programming model. Models are initialized from random initialization (not from Gemini 1.0).

**Pre-training data.** Multimodal and multilingual data across web documents, code, image, audio, and video content. Volume not disclosed.

**Instruction tuning.** Fine-tuned on a collection of multimodal paired instructions and responses, with further tuning from human preference data. All evaluations use the same instruction-tuned checkpoint at temperature 0 (greedy decoding).

**Context window.** Gemini 1.5 Pro supports up to 10M tokens; Flash supports 2M+ tokens. Inputs can include text strings, video (up to 2 hours), images, and audio files (up to 22 hours).

### Experimental Setup

Evaluation is organized into three categories:

**Diagnostic long-context evaluations:**
- Perplexity over long sequences (up to 1M tokens for documents, 10M for code)
- Text needle-in-a-haystack (1K to 10M tokens; haystack built from Paul Graham essays)
- Video needle-in-a-haystack (10.5-hour video, 37,994 frames at 1fps, 9.9M tokens)
- Audio needle-in-a-haystack (up to 107 hours of speech, 9.7M tokens, VoxPopuli dataset)
- Multiple needles (50 and 100 unique needles up to 1M tokens)
- MRCR (Multi-Round Co-reference Resolution): adversarially similar needles requiring disambiguation, 2000 instances

**Realistic long-context evaluations:**
- MTOB (Machine Translation from One Book): Kalamang language translation from grammar manual
- Low-resource MT scaling: 6 languages (Acholi, Abkhaz, Navajo, Bemba, Ewe, Kurdish)
- Long-document QA: 100 questions about Les Miserables (710K tokens)
- Long-context ASR: 15-minute YouTube video transcription
- 1H-VideoQA: 125 five-way MCQ over 40-105 minute public videos
- In-context planning: BlocksWorld, Logistics, Mini-Grid, Trip Planning, Calendar Scheduling

**Core capability benchmarks:** MMLU, MATH, GPQA, GSM8K, BigBench-Hard, HumanEval, Natural2Code, WMT23, MGSM, MMMU, MathVista, ChartQA, DocVQA, EgoSchema, ActivityNet-QA, FLEURS, CoVoST 2, and many others.

**Baselines:** GPT-4 Turbo, GPT-4V, Claude 3 (Haiku/Sonnet/Opus), Claude 2.1, Gemini 1.0 Pro, Gemini 1.0 Ultra, USM, Whisper.

### Key Results

#### Diagnostic Long-Context Results

**Perplexity follows a power law with context length (Figure 7):**

> L(x) = alpha * x^beta + gamma

| Fit | R^2 | Range |
|---|---|---|
| Long documents | 0.997 | Up to ~1M tokens |
| Code repositories | 0.995 | Up to ~10M tokens |

NLL decreases monotonically with sequence length for both Pro and Flash models. Gemini 1.0 Pro plateaus at its 32K training context.

**Needle-in-a-haystack recall (Section 5):**

| Modality | Model | Max Context | Recall |
|---|---|---|---|
| Text | 1.5 Pro | 530K | 100% |
| Text | 1.5 Pro | 1M | >99.7% |
| Text | 1.5 Pro | 10M | 99.2% |
| Text | 1.5 Flash | 2M | 100% |
| Audio | 1.5 Pro | 107 hours / 9.7M tokens | 100% |
| Audio | 1.5 Flash | 107 hours / 9.7M tokens | 98.7% |
| Video | 1.5 Pro | 10.5 hours / 9.9M tokens | 100% |
| Video | 1.5 Flash | 2M tokens | >99.8% |
| Text (GPT-4 Turbo) | GPT-4 Turbo | 128K | Multiple failures visible |

**Multiple needle retrieval (Figure 11, Appendix Figure 27):** With 100 needles, Gemini 1.5 Pro maintains ~70% recall at 128K and >60% at 1M tokens, while GPT-4 Turbo oscillates around ~50% at 128K.

**MRCR (Figure 12):** Gemini 1.5 Pro overtakes GPT-4 Turbo and Claude 3 Opus after ~32K tokens, achieving ~75% string similarity at 1M tokens.

#### Realistic Long-Context Results

**MTOB Kalamang translation (Tables 4-5, human evaluation on 0-6 scale):**

| Setting | Gemini 1.5 Pro | Best Competitor (half book) | Human Learner |
|---|---|---|---|
| kgv-to-eng (full book) | 4.00 | Claude 3 Opus: 3.74 | 5.52 |
| eng-to-kgv (full book) | 5.46 | Claude 3 Opus: 5.18 | 5.60 |

In the 0-shot setting, no model shows any ability to translate Kalamang. With the full grammar book in context, Gemini 1.5 Pro approaches human learner performance, particularly on eng-to-kgv where the gap is only 0.14 points.

**Long-document QA -- Les Miserables (Figure 14, Bradley-Terry model strength):**

| System | Strength (e^beta) |
|---|---|
| Full 710K context Gemini 1.5 Pro | **6.24** |
| RAG 4K context Gemini 1.5 Pro | 1.77 |
| RAG 4K context GPT-4 Turbo | 1.64 |
| 0K context GPT-4 Turbo | 1.30 |
| 0K context Gemini 1.5 Pro | 1.37 |

Full-context Gemini 1.5 Pro beats RAG-augmented Gemini 1.5 Pro in 78% of cases and RAG-augmented GPT-4 Turbo in 83% of cases.

**Long-context ASR (Table 8, WER on 15-minute videos):**

| Model | WER |
|---|---|
| Gemini 1.5 Pro | **5.5%** |
| Whisper (30s segments) | 7.3% |
| Gemini 1.0 Pro (30s segments) | 7.8% |
| USM | 8.8% |
| Gemini 1.5 Flash | 8.8% |

**1H-VideoQA (Table 9):**

| Model | 16 frames | 150 frames | Full video (1fps) |
|---|---|---|---|
| GPT-4V | 36.5% | 52.3% | Not supported |
| Gemini 1.5 Pro | **45.2%** | **56.3%** | **72.2%** |
| Gemini 1.5 Flash | 39.7% | 50.8% | 65.9% |

Performance continues scaling with more frames for 1H-VideoQA, unlike EgoSchema which saturates at 16 frames (Figure 15).

#### Core Capability Results

**Core text benchmarks (Table 11, selected):**

| Benchmark | 1.0 Pro | 1.0 Ultra | 1.5 Flash | 1.5 Pro |
|---|---|---|---|---|
| MMLU (5-shot) | 71.8% | 83.7% | 78.9% | **85.9%** |
| MATH (4-shot, Minerva) | 32.6% | 53.2% | 54.9% | **67.7%** |
| GPQA (0-shot) | 27.9% | 35.7% | 39.5% | **46.2%** |
| BigBench-Hard (3-shot) | 75.0% | 83.6% | 85.5% | **89.2%** |
| GSM8K (11-shot) | 77.9% | 88.9% | 86.2% | **90.8%** |
| HumanEval (0-shot) | 67.7% | 74.4% | 74.3% | **84.1%** |
| Hellaswag (10-shot) | 84.7% | 87.8% | 86.5% | **93.3%** |

DROP is a notable exception: 1.0 Ultra (82.4 F1) beats 1.5 Pro (74.9 F1).

**Math-specialized model (Table 21):**

| Benchmark | 1.5 Pro | Math-Specialized 1.5 Pro | Claude 3 Opus | GPT-4 Turbo |
|---|---|---|---|---|
| MATH | 67.7 | **80.6** (91.1 rm@256) | 60.1 | 73.4 |
| AIME 2024 | 2/30 | **7/30** | 2/30 | 1/30 |
| HiddenMath | 20.1 | **35.2** | 17.3 | 24.6 |

The rm@256 result (91.1%) uses reward-model-based selection over 256 samples, which the paper notes is "on par with human-expert performance."

**Long-context math prompting (Table 48):** Providing ~730K tokens of SymPy/SciPy documentation as in-context examples improved Intermediate Algebra (Levels 4&5) from 12.5% (GPT-4) to **25.8%** (Gemini 1.5 Pro), without any filtering or human intervention on the examples.

**Image understanding (Table 18, selected):**

| Benchmark | 1.0 Ultra | 1.5 Flash | 1.5 Pro |
|---|---|---|---|
| MMMU (val, 0-shot) | 59.4% | 56.1% | **62.2%** |
| MathVista (testmini, 0-shot) | 53.0% | 58.4% | **63.9%** |
| ChartQA (test, 0-shot) | 80.8% | 85.4% | **87.2%** |
| DocVQA (test, 0-shot) | 92.4% | 89.9% | **93.1%** |

**Video understanding (Table 19, selected):**

| Benchmark | 1.0 Ultra | 1.5 Flash | 1.5 Pro |
|---|---|---|---|
| EgoSchema (test, 0-shot) | 61.5% | 65.7% | **72.2%** |
| ActivityNet-QA (test, 0-shot) | 52.2% | 55.3% | **57.5%** |

**Gemini 1.5 Flash efficiency (Table 3, ms per output character):**

| Language | 1.5 Flash | 1.5 Pro | GPT-4 Turbo | Claude 3 Haiku |
|---|---|---|---|---|
| English | **1.5** | 4.3 | 6.8 | 2.2 |
| Japanese | **4.3** | 10.9 | 35.4 | 10.7 |

Flash generates over 650 characters per second for English, more than 30% faster than Claude 3 Haiku.

**Safety (Table 23, violation rate reduction relative to Gemini 1.0 Ultra):**

| Model | T2T English | T2T Multilingual | I2T |
|---|---|---|---|
| 1.5 Flash | -53% | -36% | -43% |
| 1.5 Pro | -58% | -44% | -62% |

### Long-Context Safety

Adversarial needle-in-the-haystack safety evaluation embeds harmful prompts in Paul Graham essays at varying depths and context lengths (Table 28). Safety violation rates are **28.6% lower on average** in long context compared to short context. The authors attribute this to the model failing to locate the adversarial needle rather than inherent long-context safety, warning that as retrieval improves, safety risks may increase.

**Prompt injection vulnerability (Table 32):** Handcrafted prompt injection templates achieve 73-100% success rates across sensitive data types, with higher success on 1.5 models than 1.0 Ultra for several categories. The authors hypothesize this is caused by improved instruction-following capabilities making the model more susceptible to following injected instructions.

---

## Limitations and Failure Modes

1. **Undisclosed architecture.** The paper does not disclose parameter counts, number of experts, positional encoding scheme, or the specific architectural changes enabling long context. The authors acknowledge this by describing only "a series of significant architecture changes" (Section 3.1). This limits reproducibility and scientific analysis of the long-context capability.

2. **Prompt injection susceptibility.** Handcrafted prompt injection attacks achieve 73-100% success rates (Table 32). The authors acknowledge that better instruction following is a double-edged sword: the model more readily follows both legitimate and injected instructions. Email address exfiltration shows +75.2% increase over 1.0 Ultra.

3. **Tone regression.** Gemini 1.5 Pro shows an 11% regression in tone quality compared to Gemini 1.0 Ultra (Table 29b). The authors note this is "an area being prioritized for future work" (Section 9.4.2).

4. **Audio parity gaps.** Gemini 1.5 Pro shows a 5.7% WER gap between genders in ASR, much worse than USM's 0.4% (Table 35). AAVE recognition recall is low (0.21 for Flash, 0.44 for Pro). The authors acknowledge this and note "more research is needed" (Section 9.4.4).

5. **Income-based accuracy gap.** While overall accuracy improves on the Dollar Street dataset, the gap between best- and worst-performing income groups increases for 1.5 Pro (20.4 vs 16.6 for Ultra, Table 34). The authors acknowledge that "special attention may be needed" for equitable improvement across groups.

6. **Grounded over-refusal.** Both 1.5 models show increased refusal rates on grounded queries (where context clues support an answer), not just ungrounded ones (Figure 22). Flash shows a 140% increase in grounded refusals over Ultra. The authors acknowledge this tradeoff between safety and helpfulness (Section 9.4.2).

7. **Audio regression in 1.5 series.** Slight regressions on multilingual ASR/AST benchmarks relative to 1.0 Ultra, attributed by the authors to post-training data containing only 5 head languages (Table 10, Section 6).

8. **Long-context divergence vulnerability.** Longer prompts make divergence attacks easier (61.5% success with 999K-token prompts vs 35.6% with 1K-token prompts), which can lead to training data emission (Section 9.4.3). The authors acknowledge this increased attack surface from longer context.

9. **DROP regression.** 1.5 Pro (74.9 F1) underperforms 1.0 Ultra (82.4 F1) on the DROP benchmark (Table 11). The paper reports this without explanation.

10. **Benchmark saturation concerns.** BBQ bias accuracy approaches 100% for 1.5 models (Figure 26b), suggesting the benchmark may lose diagnostic value for measuring biases in future models. The authors note existing benchmarks "may not be helpful for measuring biases in future, more capable models" (Section 9.4.4).

11. **[Inferred] Single-task evidence for full-context vs RAG.** The dramatic full-context advantage over RAG (C6) is demonstrated on only one book (Les Miserables) with auto-generated questions and an auto-rater, limiting generalizability of the claim that full-context processing obviates retrieval.

12. **[Inferred] No variance reporting.** Planning task results (Figure 16) use 70% confidence intervals, but most other evaluations report single-run results without variance estimates or statistical significance tests, making it difficult to assess reliability.

13. **[Inferred] Kalamang evaluation relies on a single non-native human evaluator.** The MTOB human evaluation scores come from one language learner who can identify their own translations, introducing potential bias. The authors acknowledge this constraint (footnote 13) but it limits the strength of the human-parity claim.

#### Scope and Comparability

- **What was not tested:** No evaluation on context lengths between 1M and 10M for realistic tasks (only diagnostic NIAH tested at 10M). No evaluation of reasoning tasks requiring multi-hop integration across the full 10M-token context. No comparison with open-source long-context models (e.g., Llama 2 Long, YaRN-extended models). Flash-8B results are preliminary and incomplete. No evaluation of generation quality at very long output lengths.
- **Comparability notes:** GPT-4 Turbo comparisons are capped at 128K tokens; Claude 3 comparisons are capped at 200K tokens. The RAG baseline uses TF-IDF retrieval with 4K-token chunks -- more sophisticated retrieval (dense retrieval, ColBERT, multi-step) would be a stronger baseline. MTOB human evaluation uses a single non-native evaluator rather than multiple independent raters. Latency measurements (Table 3) use minimum-of-32 queries rather than median or percentile, potentially understating typical latency. The paper's "win rate" metric counts any improvement as a win regardless of magnitude, which obscures the size of gains and losses. Evaluation uses greedy decoding throughout, so results may differ under sampling.

---

## Conclusions

### Contributions

1. **First commercially available model with millions-of-tokens context.** Gemini 1.5 Pro extends context from 32K to 10M tokens -- a generational leap over Claude 3 (200K) and GPT-4 Turbo (128K) -- with near-perfect retrieval (>99%) across text, video, and audio modalities (Figure 1, Section 5).

2. **Power-law scaling of NLL with context length.** Demonstrated that next-token prediction loss follows L(x) = alpha * x^beta + gamma with R^2 > 0.995 up to millions of tokens, showing the model genuinely uses long-range context for prediction (Figure 7).

3. **Full-context superiority over RAG.** On long-document QA (Les Miserables, 710K tokens), full-context Gemini 1.5 Pro achieves 3.5x the Bradley-Terry strength of the best RAG-augmented system, winning in 78-83% of head-to-head comparisons (Figure 14).

4. **In-context language learning.** Given a grammar manual for Kalamang (fewer than 200 speakers worldwide), Gemini 1.5 Pro learns to translate at a level approaching a human learner, demonstrating genuine in-context learning from previously unseen material (Tables 4-5).

5. **Efficient distilled model.** Gemini 1.5 Flash, online-distilled from Pro, outperforms Gemini 1.0 Pro on 82% of benchmarks while generating >650 English characters per second and achieving 100% text NIAH recall up to 2M tokens (Tables 2-3).

6. **Multimodal long-context benchmarks.** Introduced new evaluation tasks -- video NIAH (10.5 hours), audio NIAH (107 hours), MRCR, 1H-VideoQA, and ASROB -- that test multimodal long-context capabilities beyond existing text-only benchmarks.

7. **MoE efficiency.** Gemini 1.5 Pro matches or surpasses 1.0 Ultra across most benchmarks (78% win rate) while using significantly less training compute, demonstrating the efficiency of sparse MoE architectures for frontier model development (Table 1).

### Implications

1. **Context may substitute for retrieval.** The dramatic advantage of full-context processing over RAG on long-document QA (6.24 vs 1.77 Bradley-Terry strength) suggests that as context windows grow, retrieval-augmented approaches may become unnecessary for document-scale inputs (speculative, tested on only one task).

2. **Monotonic in-context learning scaling.** The consistent improvement with more in-context examples on planning tasks (Figure 16), where competitors degrade, suggests that MoE architectures may be better suited to in-context learning at scale (speculative, mechanism unknown).

3. **Evaluation methodology gap.** The saturation of existing benchmarks (EgoSchema at 16 frames, BBQ at 100% accuracy) highlights the need for harder evaluation tasks that scale with model capability, particularly for long-context understanding.

---

## Key Claims

**C1. Near-perfect retrieval up to 10M tokens across modalities.** Gemini 1.5 Pro achieves 100% text recall up to 530K tokens, >99.7% at 1M, and 99.2% at 10M. Audio recall is 100% over 107 hours (9.7M tokens). Video recall exceeds 99.8% up to 2M tokens (Figure 1, Section 5). Status: **supported**.

**C2. Power-law NLL scaling with context.** The fit L(x) = alpha * x^beta + gamma achieves R^2 = 0.997 for documents (up to ~1M tokens) and R^2 = 0.995 for code (up to ~10M tokens). NLL decreases monotonically throughout (Figure 7, Section 5.1). Status: **supported**.

**C3. Gemini 1.5 Pro matches or surpasses 1.0 Ultra on 78% of benchmarks.** Across 45 core capability evaluations: 35 wins, 10 losses. Wins include math/science (+18.1%), charts & documents (+39.6%), multimodal reasoning (+14.8%). Main losses are in audio (-3.8% ASR, -3.9% AST) (Table 1, Table 10). Status: **supported**.

**C4. In-context Kalamang translation approaches human level.** With full grammar book: kgv-to-eng human eval 4.00 (vs 5.52 human), eng-to-kgv 5.46 (vs 5.60 human) on a 0-6 scale. In the 0-shot setting, all models score near 0, confirming no prior Kalamang knowledge (Tables 4-5, Section 6.1). Status: **supported**.

**C5. Monotonic improvement with in-context examples.** On Logistics (1-shot 43% to 400-shot improvement), Mini-Grid (1-shot 28% to 400-shot 77%), Trip Planning (1-shot to 100-shot 42%), and Calendar Scheduling (1-shot 33% to 100-shot 52%), Gemini 1.5 Pro improves consistently. GPT-4 Turbo plateaus or degrades on all four tasks (Figure 16). Status: **supported**.

**C6. Full-context dramatically outperforms RAG.** On Les Miserables QA (710K tokens), full-context Gemini 1.5 Pro achieves Bradley-Terry strength 6.24 vs 1.77 for RAG 1.5 Pro and 1.64 for RAG GPT-4 Turbo. It wins 78% of head-to-head comparisons against its own RAG variant (Figure 14, Section 6.2). Status: **supported**.

**C7. Flash matches Pro's context capabilities at lower cost.** Gemini 1.5 Flash achieves 100% text NIAH recall up to 2M tokens, NLL follows the same power-law trend (R^2 = 0.991 documents, 0.998 code), and outperforms 1.0 Pro on 82% of benchmarks while being >30% faster than Claude 3 Haiku (Tables 2-3, Figure 20). Status: **supported**.

**C8. 1H-VideoQA shows continued scaling with frames.** At 16 frames: 45.2% vs GPT-4V 36.5%. At 150 frames: 56.3% vs 52.3%. At full 1fps: 72.2% (GPT-4V cannot process). EgoSchema saturates at 16 frames, making 1H-VideoQA a better discriminator of long-context video capability (Table 9, Figure 15). Status: **supported**.

---

## Open Questions

1. **What are the specific architectural changes enabling 10M-token context?** The paper states only "a series of significant architecture changes" without enumeration. The positional encoding scheme, routing mechanism modifications, and any memory or caching strategies are not disclosed. Unresolved.

2. **Does near-perfect NIAH recall transfer to complex reasoning at extreme lengths?** Retrieval is necessary but not sufficient for long-context understanding. NOLIMA (2025) finds Gemini 1.5 Pro's effective length drops to 2K tokens when literal matching cues are removed. Addressed by: `2025-07-nolima-long-context-evaluation`.

3. **Why does NLL follow a power law with context so precisely?** The R^2 > 0.995 fit is striking. Whether this reflects a fundamental property of Transformer architectures, a characteristic of natural language structure, or an artifact of the training data distribution is unknown. Unresolved.

4. **Will the full-context advantage over RAG persist?** The 3.5x Bradley-Terry strength advantage is measured against TF-IDF retrieval with 4K-token chunks. More sophisticated retrieval systems (dense retrieval, multi-step reasoning chains) might narrow this gap at lower compute cost. Unresolved.

5. **Can the in-context translation capability generalize to other complex skill acquisition?** The Kalamang result demonstrates remarkable in-context learning, but the paper tests only one language with a well-structured grammar manual. Whether similar capabilities extend to other domains requiring structured reasoning from novel material is unclear. Unresolved.

---

## Core References and Why They Are Referenced

### Mixture-of-Experts Foundations

- **Shazeer et al. (2017)** -- *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.* Foundational work on sparsely-gated MoE that Gemini 1.5 Pro's architecture builds upon.
- **Lepikhin et al. (2020)** -- *GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding.* Scaling MoE to large models across TPU pods; directly relevant to Gemini's training infrastructure.
- **Fedus et al. (2021)** -- *Switch Transformers.* Simplified MoE routing with one expert per token; part of the MoE lineage leading to Gemini 1.5.
- **Zoph et al. (2022)** -- *Designing Effective Sparse Expert Models.* Design principles for sparse MoE models referenced as foundational to Gemini 1.5's architecture.

### Long-Context and Efficient Transformers

- **Kamradt (2023)** -- *Needle in a Haystack.* The evaluation methodology that Gemini 1.5 extends to multimodal settings and multi-needle variants at up to 10M tokens.
- **Press et al. (2021)** -- *ALiBi: Train Short, Test Long.* Alternative positional encoding for length extrapolation; referenced among context extension approaches but the paper does not state which approach Gemini uses.
- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* Referenced as a novel architecture for long sequences; positioned as an alternative approach to the Transformer-based method Gemini uses.

### Predecessor Models

- **Gemini Team (2023)** -- *Gemini 1.0.* Direct predecessor providing the multimodal foundation. Gemini 1.5 builds on 1.0's research advances and architectural choices.
- **Chowdhery et al. (2023b)** -- *PaLM.* Provides the parallel attention-feedforward pattern used in Gemini 1.5 Flash's architecture.
- **OpenAI (2023a)** -- *GPT-4 Technical Report.* Primary competitor; GPT-4 Turbo (128K context) is the main baseline for long-context comparisons.

### Distillation

- **Hinton et al. (2015)** -- *Distilling the Knowledge in a Neural Network.* Foundational knowledge distillation work underlying the online distillation of Flash from Pro.
- **Agarwal et al. (2024b)** -- Cited for online distillation techniques used to train Gemini 1.5 Flash from Pro.

### Evaluation Benchmarks

- **Hendrycks et al. (2021a)** -- *MMLU.* Multitask language understanding benchmark used as a core text evaluation.
- **Hendrycks et al. (2021b)** -- *MATH.* Competition mathematics benchmark; base 1.5 Pro achieves 67.7%, math-specialized achieves 91.1% with rm@256.
- **Rein et al. (2023)** -- *GPQA.* Graduate-level science QA used to measure advanced reasoning.
- **Tanzer et al. (2023)** -- *Machine Translation from One Book.* The MTOB benchmark evaluating in-context learning from a grammar manual; Gemini 1.5 paper extends this with full-book context and additional baselines.
- **Mangalam et al. (2023)** -- *EgoSchema.* Long-form egocentric video QA benchmark; used to demonstrate that existing video benchmarks saturate at short context (16 frames).

### Scaling Laws

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* The power-law relationship between NLL and context length (Figure 7) echoes the scaling law framework, applied here to context length rather than model/data size.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Referenced for compute-optimal training principles; Gemini 1.5 Pro is described as "significantly more efficient" than 1.0 Ultra.
