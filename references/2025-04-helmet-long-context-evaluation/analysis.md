---
title: "HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly"
authors: "Yen, Gao, Hou, Ding, Fleischer, Izsak, Wasserblat, Chen"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["long-context language model evaluation", "benchmark design", "correlation analysis between synthetic and downstream tasks"]
benchmarks_used: ["niah", "ruler", "infinitebench", "natural-questions", "triviaqa", "hotpotqa", "helmet"]
models_introduced: []
models_evaluated: ["gpt-4", "gpt-4o", "gpt-4o-mini", "claude-3.5-sonnet", "gemini-1.5-pro", "gemini-1.5-flash", "llama-3-8b", "llama-3-70b", "llama-3.1-8b", "llama-3.1-70b", "llama-3.2-1b", "llama-3.2-3b", "mistral-7b", "phi-3-mini", "phi-3-medium", "qwen2-7b", "qwen2.5-7b", "qwen2.5-14b", "qwen2.5-72b", "yi-6b", "yi-34b"]
key_claims:
  - id: C1
    claim: "Synthetic tasks like NIAH do not reliably predict downstream long-context performance"
    evidence: "Figure 3, Figure 4, Section 3.1"
    status: supported
    scope: "35 instruction-tuned models at 128K input length, Spearman rank correlation"
    magnitude: "NIAH average correlation with downstream tasks rho=0.68; no synthetic task exceeds rho=0.8 average"
  - id: C2
    claim: "Different HELMET task categories exhibit distinct trends and low correlations with each other"
    evidence: "Figure 5, Section 3.2"
    status: supported
    scope: "35 instruction-tuned models at 128K, Spearman rank correlation across 7 categories"
    magnitude: "ICL-Cite rho=0.34, ICL-Summ rho=0.38, ICL-Re-rank rho=0.36; RAG-LongQA rho=0.92"
  - id: C3
    claim: "Open-source models significantly lag behind closed-source models on complex tasks requiring full-context reasoning or instruction following, and the gap widens with increasing context length"
    evidence: "Figure 6, Figure 7, Section 3.3"
    status: supported
    scope: "Instruction-tuned models with 128K+ claimed context windows, evaluated at 8K-128K"
    magnitude: "30-40 absolute points gap on citation generation and re-ranking at 128K"
  - id: C4
    claim: "RAG tasks are a better proxy for downstream performance than synthetic tasks and are recommended for fast model development"
    evidence: "Figure 3, Figure 4, Section 3.1"
    status: supported
    scope: "35 instruction-tuned models at 128K, correlation analysis"
    magnitude: "RAG average correlation rho=0.78 vs NIAH rho=0.68; HotpotQA-LongQA rho=0.92"
  - id: C5
    claim: "Model-based evaluation using GPT-4o is more reliable than n-gram overlap metrics like ROUGE for long-context QA and summarization"
    evidence: "Figure 2, Table 14, Section 2.2"
    status: supported
    scope: "NarrativeQA, InfiniteBench Sum, Multi-LexSum tasks"
    magnitude: "Cohen's kappa=0.91 for summary precision, kappa=0.76 for recall on x-BENCH Sum"
  - id: C6
    claim: "Two-shot demonstrations substantially improve evaluation robustness and enable evaluation of base models"
    evidence: "Table 8, Section 2.3"
    status: supported
    scope: "Base and instruction-tuned models at 128K, averaged across three random seeds"
    magnitude: "Base Llama-3.1-8B improves from 0.1 to 7.5 on MSMARCO, from 77.3 to 95.0 on JSON KV"
  - id: C7
    claim: "Positional embedding extrapolation remains a challenge; models using position extrapolation degrade sharply beyond training lengths"
    evidence: "Figure 7, Section E.3"
    status: supported
    scope: "Qwen2 with YaRN and Llama-3 with RoPE theta adjustment, 8B-70B scale"
    magnitude: "Sharp performance drops past L=32768 for extrapolating models"
  - id: C8
    claim: "HELMET provides more consistent and reliable model rankings than existing benchmarks like RULER and InfiniteBench"
    evidence: "Figure 1, Table 5, Table 9, Appendix A"
    status: supported
    scope: "6 frontier LCLMs at 128K tokens"
    magnitude: "RULER shows Flash outperforming Pro; InfiniteBench ranks Llama-3.2-3B-Inst at 2.8 vs HELMET at 36.9"
cross_references:
  - target: 2024-10-ruler-context-size
    type: extends
    detail: "HELMET uses selected RULER tasks as its synthetic recall subset and demonstrates that RULER's full average score does not reliably predict downstream performance"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: extends
    detail: "HELMET directly compares against InfiniteBench, showing that improved prompting and model-based evaluation yield more reliable rankings than InfiniteBench's ROUGE-based metrics"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: extends
    detail: "HELMET addresses ZeroSCROLLS limitations including inadequate context lengths (mostly <128K) and lack of base model support"
  - target: 2024-08-longbench-bilingual-benchmark
    type: extends
    detail: "HELMET extends beyond LongBench's limited context lengths and adds controllable length evaluation with more diverse task categories"
  - target: 2024-08-l-eval-standardized-evaluation
    type: extends
    detail: "HELMET adopts L-Eval's length-instruction-enhanced evaluation approach for summarization while replacing its reference-free pairwise win-rates with reference-based model evaluation"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "HELMET uses NIAH as a baseline synthetic task and demonstrates its saturation across most frontier models"
  - target: 2024-02-lost-in-the-middle
    type: extends
    detail: "HELMET extends the lost-in-the-middle analysis to 128K tokens across multiple models and finds that middle-position performance is not always worse than start-of-context"
  - target: 2024-11-genuinely-difficult-long-context
    type: complementary
    detail: "Both papers argue that simple synthetic tasks are insufficient for evaluating long-context capabilities; Goldman et al. focus on task difficulty while HELMET focuses on holistic benchmark design"
  - target: 2024-05-yarn-context-extension
    type: evaluates
    detail: "HELMET evaluates YaRN-based models (including Qwen2 with YaRN scaling) and finds positional extrapolation still degrades beyond training lengths"
open_questions:
  - question: "What is the optimal selection method for synthetic tasks that best correlate with downstream performance?"
    addressed_by: null
  - question: "How do HELMET rankings generalize to non-English languages?"
    addressed_by: null
  - question: "How should long-context evaluation adapt as models scale beyond 128K to 1M+ tokens?"
    addressed_by: null
  - question: "Can the gap between open-source and closed-source models on complex long-context tasks (citation, re-ranking) be closed with better training recipes rather than scale?"
    addressed_by: null
  - question: "What evaluation methodology should be used for long-context tasks that do not fit existing HELMET categories, such as code understanding or multimodal contexts?"
    addressed_by: null
---

# HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly

**Authors:** Howard Yen, Tianyu Gao, Minmin Hou, Ke Ding, Daniel Fleischer, Peter Izsak, Moshe Wasserblat, Danqi Chen (Princeton Language and Intelligence, Princeton University; Intel)
**Date:** April 2025, ICLR 2025; arXiv:2410.02694

---

## Core Research Problem

Evaluating long-context language models (LCLMs) reliably remains an unsolved challenge. Despite the proliferation of benchmarks for long-context abilities, model developers overwhelmingly rely on synthetic tasks like needle-in-a-haystack (NIAH) or arbitrary subsets of existing datasets (Table 1, Section 1). The authors identify four concrete design flaws in existing benchmarks that explain this state of affairs:

1. **Insufficient coverage of downstream tasks.** Existing benchmarks either focus on synthetic tasks or include only a narrow slice of applications such as a single QA dataset (Section 1).
2. **Inadequate context lengths.** Most natural language datasets in benchmarks like ZeroSCROLLS, LongBench, and L-Eval have median lengths well below 128K tokens, making them unable to test frontier model capabilities (Table 4, Section 1).
3. **Unreliable metrics.** Commonly used metrics like ROUGE correlate poorly with human judgment for open-ended tasks like summarization and long-form QA (Section 1).
4. **Incompatibility with base models.** Many benchmarks require instruction-tuned models, forcing base model developers to fall back on perplexity and synthetic tasks (Section 1).

These flaws cause existing benchmarks to either be inapplicable or provide noisy signals. As shown in Figure 1, at 128K tokens, NIAH is saturated (near 100% for all frontier models), RULER produces unexpected rankings (Gemini Flash outperforming Pro), and InfiniteBench yields questionable results (70B Llama underperforming 8B). **The core challenge is how to design a comprehensive, reliable, and practically useful benchmark for evaluating long-context language models across diverse downstream applications.**

---

## Problem Solutions

HELMET (How to Evaluate Long-context Models Effectively and Thoroughly) addresses all four design flaws through:

1. **Seven diverse application-centric task categories** spanning synthetic recall, RAG, generation with citations, passage re-ranking, many-shot in-context learning, long-document QA, and summarization -- ensuring broad coverage of LCLM capabilities.
2. **Controllable context lengths up to 128K tokens** for all datasets, achieved by adjusting the number of retrieved passages, demonstration shots, or document truncation.
3. **Reference-based model evaluation** using GPT-4o as a judge for QA and summarization tasks, replacing unreliable n-gram overlap metrics.
4. **Two-shot prompting** for all tasks, reducing evaluation noise from output formatting inconsistencies and enabling robust evaluation of base models.

---

## Approach Details

### Method

HELMET curates 20 datasets across 7 categories, each designed to test distinct long-context capabilities. The benchmark design follows three principles: diverse coverage, controllable lengths, and reliable metrics.

**Task categories and datasets** (Table 3, Section 2.1):

| Category | Datasets | Metric |
|---|---|---|
| Retrieval-augmented generation (RAG) | Natural Questions, TriviaQA, PopQA, HotpotQA | SubEM |
| Generation with citations (Cite) | ALCE ASQA, ALCE QAMPARI | Recall + Cite avg |
| Passage re-ranking (Re-rank) | MS MARCO | NDCG@10 |
| Many-shot in-context learning (ICL) | TREC Coarse, TREC Fine, NLU, BANKING77, CLINC150 | Accuracy |
| Long-document QA (LongQA) | NarrativeQA, x-BENCH QA, x-BENCH MC | Model-based / ROUGE F1 / Accuracy |
| Summarization (Summ) | x-BENCH Sum, Multi-LexSum | Model-based |
| Synthetic recall | JSON KV, RULER MK Needle, RULER MK UUID, RULER MV | SubEM |

### Key Technical Components

**Length control.** For RAG, citation, and re-ranking tasks, the number of passages k is determined from the target input length L. For ICL, the number of shots is adjusted. For long-document QA and summarization, documents are truncated from the end to fit L (Section 2.1).

**Hard negative distractor selection for RAG.** Unlike prior work that randomly samples passages, HELMET retrieves the top k-1 distractors using Alibaba-NLP/gte-large-en-v1.5 from a Wikipedia 2019 corpus, making the task more realistic and challenging (Section 2.1, footnote 3).

**Gold passage positioning for RAG.** For NQ, TriviaQA, and PopQA, the gold passage is placed at six evenly distributed positions following Liu et al. (2023). For HotpotQA (multi-hop), two gold passages are combined with k-2 distractors and randomly shuffled into three permutations (Section 2.1).

**Numbered label mapping for ICL.** Natural language labels are mapped to integer labels (0, 1, ..., n-1) to test genuine task learning rather than reliance on pre-trained priors (Section 2.1).

**Model-based evaluation for QA.** For NarrativeQA, GPT-4o-2024-05-13 is prompted with the question, ground truth, and model output. It scores fluency (0 or 1) and correctness (0-3). The final score is fluency x correctness, normalized to [0, 100] (Section 2.2, Table 10).

**Model-based evaluation for summarization.** The gold summary is decomposed into atomic claims by GPT-4o. Recall is the percentage of claims supported by the generation; precision is the percentage of generated sentences supported by the reference. The final score is fluency x F1(recall, precision) (Section 2.2).

**Two-shot demonstrations.** Two in-context examples are added to prompts for all tasks (except ICL, which varies shots, and RULER, which uses original formatting). This reduces output formatting noise and enables base model evaluation (Section 2.3, Table 8).

### Experimental Setup

**Models:** 59 LCLMs evaluated, spanning closed-source (GPT-4 series, Claude-3.5-Sonnet, Gemini-1.5 Flash/Pro), and open-source families (Llama 2/3/3.1/3.2, Mistral, Phi-3, Yi, Qwen 2/2.5, Jamba, ProLong). Models include full dense transformers, sliding-window attention, and hybrid SSM architectures (Table 15, Section 3).

**Input lengths:** L in {8192, 16384, 32768, 65536, 131072} Llama-2 tokens. All models use greedy decoding (Section 3).

**Hardware:** Open-source models evaluated on H100 GPUs (80GB). Proprietary models accessed via provider APIs (Section D).

**Sample sizes:** 600 examples for JSON KV, NQ, PopQA, TQA; 300 for MSMARCO and HotpotQA; 500 for ICL datasets; 100 for remaining datasets (Section D).

**Reproducibility:** Code released at https://github.com/princeton-nlp/HELMET. Data at https://huggingface.co/datasets/princeton-nlp/HELMET. Model outputs planned for release (Section 6).

### Key Results

**Benchmark comparison at 128K tokens** (Table 5, Section A.1):

| Model | Claimed Length | NIAH | RULER | InfiniteBench | HELMET |
|---|---|---|---|---|---|
| GPT-4o-mini | 128000 | 100.0 | 80.8 | 51.9 | 54.1 |
| GPT-4o-08 | 128000 | 100.0 | 93.3 | 57.1 | 63.8 |
| Gemini-1.5-Flash | 1048576 | 100.0 | 86.6 | 50.8 | 50.7 |
| Gemini-1.5-Pro | 2097152 | 45.3 | 65.3 | 60.8 | 62.7 |
| Llama-3.1-8B-Inst | 131072 | 100.0 | 81.3 | 44.1 | 47.0 |
| Llama-3.1-70B-Inst | 131072 | 100.0 | 75.8 | 39.7 | 49.3 |

- **NIAH is saturated**: Most frontier models score 100.0, providing no differentiation (Figure 1, Table 5).
- **RULER produces anomalous rankings**: Gemini Flash (86.6) outperforms Gemini Pro (65.3), and Llama-3.1-8B-Inst (81.3) outperforms the 70B variant (75.8) (Table 5).
- **InfiniteBench underestimates Llama-3.2 models**: Llama-3.2-3B-Inst scores 2.8 on InfiniteBench but 36.9 on HELMET, because HELMET's improved prompting reveals their actual capabilities (Table 9).
- **HELMET differentiates consistently**: Rankings align with expected capability orderings (GPT-4o > Gemini-1.5-Pro > Llama-3.1-70B > Llama-3.1-8B) (Figure 1).

**Correlation between synthetic and downstream tasks** (Figure 3, Section 3.1; tested across 35 instruction-tuned models at 128K):

| Synthetic Task | ICL | Cite | Re-rank | LongQA | Summ | Avg |
|---|---|---|---|---|---|---|
| NIAH | 0.44 | 0.71 | 0.75 | 0.76 | 0.72 | 0.68 |
| RULER MK | 0.48 | 0.73 | 0.84 | 0.79 | 0.87 | 0.74 |
| RULER MV | 0.61 | 0.71 | 0.77 | 0.83 | 0.79 | 0.74 |
| RULER All | 0.51 | 0.77 | 0.85 | 0.79 | 0.83 | 0.75 |
| Recall (HELMET) | 0.61 | 0.74 | 0.85 | 0.82 | 0.85 | 0.77 |
| RAG | 0.50 | 0.72 | 0.85 | 0.92 | 0.89 | 0.78 |

- **No synthetic task achieves an average correlation above 0.80** with downstream tasks (Figure 3).
- **RAG tasks consistently achieve the highest average correlation** (0.78), with HotpotQA reaching 0.92 with LongQA (Figure 4; strong evidence from 35 models, p=2.9e-12 for Spearman rho).
- **Tasks with noisier, more distracting contexts better differentiate models**: NIAH clusters models at 0% or 100%, while RULER MK and HotpotQA distribute performance more evenly (Figure 4).

**Inter-category correlations at 128K** (Figure 5, Section 3.2):

| | RAG | Cite | Re-rank | LongQA | Summ | ICL |
|---|---|---|---|---|---|---|
| Recall | 0.88 | 0.74 | 0.85 | 0.82 | 0.85 | 0.61 |
| RAG | -- | 0.72 | 0.85 | 0.92 | 0.89 | 0.50 |
| Cite | -- | -- | 0.84 | 0.72 | 0.82 | 0.34 |
| Re-rank | -- | -- | -- | 0.87 | 0.89 | 0.36 |
| LongQA | -- | -- | -- | -- | 0.85 | 0.51 |
| Summ | -- | -- | -- | -- | -- | 0.38 |

- **ICL correlates poorly with all other categories** (0.34-0.61), indicating it measures a distinct capability (Figure 5).
- **Citation generation also shows lower cross-category correlations**, suggesting that instruction following and fact recall in long contexts are distinct capabilities (Section 3.2).

**Performance degradation with context length** (Figure 7, Section 3.3):

| Model | NIAH 128K | RAG 128K | Re-rank 128K | Cite 128K |
|---|---|---|---|---|
| GPT-4o-08 | 100.0 | [not in notes] | 85.8-89.2 | 45.4-48.8 |
| Gemini-1.5-Pro | 98.5-100.0 | 73.8-77.4 | 77.6-81.7 | 47.3-48.2 |
| Llama-3.1-8B-Inst | [not in notes] | [not in notes] | [not in notes] | [not in notes] |
| Qwen2.5-57B-Inst | 96.6 at 128K | [not in notes] | [not in notes] | [not in notes] |

- **Performance degradation is category-dependent**: most models retain performance on recall and RAG at longer inputs but degrade substantially on re-ranking and citation generation (Figure 7, Section 3.3).
- **Open-source models collapse on citation generation at 128K**, while GPT-4o remains relatively stable (Section 3.3).
- **No single model wins across all categories**: GPT-4o leads on recall and citations; Gemini excels on re-ranking and LongQA; many open-source models outperform closed-source on ICL (Section 3.3).

### Additional Results

**ROUGE vs. model-based evaluation** (Table 14, Section 2.2): Model-based evaluation reveals quality differences that ROUGE misses. Claude-3.5-Sonnet scores 16.2 F1 but 43.5 GPT-based score on NarrativeQA, because Claude generates verbose assistant-style text penalized by n-gram overlap but correctly answers the question. Llama-3.1-8B-Inst achieves 45.1 F1 (similar to GPT-4o-05's 46.5) but only 47.7 GPT-based score vs GPT-4o-05's 55.4, revealing the true quality gap (Table 14; moderate evidence -- compared across 15 models on 3 tasks).

**Two-shot vs. zero-shot evaluation** (Table 8, Section 2.3): Two-shot demonstrations substantially improve base model evaluation. Llama-3.1-8B base improves from 0.1 to 7.5 on MSMARCO re-ranking, from 77.3 to 95.0 on JSON KV. Standard deviations across 3 seeds are generally low (1-3 points), confirming stability (Table 8; moderate evidence -- 3 seeds reported).

**Lost-in-the-middle analysis** (Section E.4, Figures 11-14): The authors extend Liu et al.'s (2023) analysis to 128K tokens across multiple models. They find that while models generally prefer retrieving from the beginning of input, **middle-position performance is often better than start-of-context performance for long inputs**, partially contradicting the simple "U-shaped" pattern from prior work. The pattern varies substantially by model family.

**Positional embedding extrapolation** (Section E.3): Both Llama-3 with modified RoPE theta (b=16M) and Qwen2 with YaRN scaling show **sharp performance drops past L=32768**. Altering positional embeddings can also degrade shorter-length performance (e.g., Llama-3-8B-Inst on ODQA and ICL).

**Claude performance analysis** (Section E.6, Tables 16-19): Claude-3.5-Sonnet underperforms on several HELMET categories not because of weak long-context capabilities but because it frequently fails to follow task-specific instructions -- not outputting citation markers, not following re-ranking format, refusing answers due to copyright concerns, and output truncation from generation token limits.

---

## Limitations and Failure Modes

- The authors note that their synthetic task selection (4 tasks for the HELMET recall subset) may not be optimal: "There may be more optimal methods for selecting synthetic datasets, and they leave this as future work" (Section E.1).
- Compute constraints limited evaluation: 8 H100 GPUs prevented running some larger models (Command-R, Jamba-1.5-Large) at 128K tokens (Section D).
- The model-based evaluation relies on GPT-4o as judge, introducing potential bias. However, human agreement is reported: Cohen's kappa=0.76 for recall and kappa=0.91 for precision on InfiniteBench Sum, and kappa=0.72/0.83 for Multi-LexSum (Section B.6).
- The benchmark evaluates coding tasks as out-of-scope for "general-purpose" LCLMs, potentially missing an important capability dimension (Section A.2).
- **[Inferred]** All evaluation uses greedy decoding, which may not reflect real-world usage patterns where sampling-based decoding is common.
- **[Inferred]** The benchmark is English-only, limiting generalizability claims to multilingual settings.
- **[Inferred]** The number of evaluation samples varies by task (100-600), which may introduce different levels of statistical power across categories.

#### Scope and Comparability

**What was not tested:** Models beyond 128K tokens (despite some models claiming 1M+ context); non-English evaluation; code-related tasks; multimodal inputs; sampling-based decoding; very large open-source models (>70B parameters) at full context length due to compute constraints.

**Comparability notes:** HELMET measures input length in Llama-2 tokens, which differ from native tokenizer counts for other models. This standardization enables cross-model comparison but means the effective input length in each model's native tokenizer may vary. The benchmark's reliance on GPT-4o-2024-05-13 as judge means evaluation quality depends on that specific model version. HELMET's RAG tasks use hard-negative retrieval (via gte-large-en-v1.5), making them more difficult than benchmarks using random distractor passages (e.g., Lee et al., 2024), and cross-benchmark RAG performance comparisons must account for this difference.

---

## Conclusions

#### Contributions

1. **Comprehensive benchmark design.** HELMET provides 7 application-centric categories with 20 datasets, all supporting controllable lengths up to 128K tokens, addressing coverage gaps in prior benchmarks (Table 2, Table 3).
2. **Reliable model-based evaluation.** Reference-based GPT-4o evaluation for QA and summarization achieves high human agreement (kappa=0.72-0.91) and better differentiates model quality than ROUGE (Figure 2, Table 14).
3. **Empirical evidence that synthetic tasks poorly predict downstream performance.** Systematic correlation analysis across 35 models shows no synthetic task exceeds rho=0.80 average correlation with downstream categories (Figure 3).
4. **Demonstration that long-context capabilities are multidimensional.** Different task categories exhibit low cross-correlation (especially ICL with rho=0.34-0.61), establishing that no single task can represent overall LCLM quality (Figure 5).
5. **Largest controlled comparison of LCLMs.** Evaluation of 59 models across architectures, scales, and training approaches provides the most comprehensive LCLM comparison available at the time of publication (Table 15, Section 3).
6. **Practical recommendation for model development.** RAG tasks are identified as the best fast proxy for downstream performance, combining ease of use, strong correlation with other tasks, and base model compatibility (Section 3.1).

#### Implications

1. **Benchmark saturation necessitates harder tasks.** The near-perfect NIAH scores across frontier models suggest the field must move toward more challenging and realistic evaluation, as simple retrieval tasks no longer differentiate capabilities.
2. **Open-source models need targeted improvement on complex instruction following.** The 30-40 point gap on citation and re-ranking suggests that training approaches for open-source models may need to emphasize instruction adherence in long-context settings, not just context extension.
3. **Position extrapolation is not yet solved.** Even with techniques like YaRN and RoPE theta modification, models degrade sharply beyond training lengths, implying that length generalization remains a fundamental challenge for the field (speculative: longer training lengths may be necessary rather than inference-time scaling of positional embeddings).

---

## Key Claims

1. **Synthetic tasks like NIAH are poor predictors of downstream performance.** At 128K tokens across 35 instruction-tuned models, NIAH achieves an average Spearman correlation of only 0.68 with downstream categories, and no synthetic task exceeds 0.80 (Figure 3, Section 3.1). NIAH clusters most models at 0% or 100%, providing poor separability (Figure 4, rho=0.63 with x-BENCH QA, p=5.1e-05). Evidence breadth: 35 models, 6 downstream categories, at a single context length of 128K (strong evidence for the tested setting; correlation at shorter lengths not systematically reported for the main claim).

2. **Different HELMET categories exhibit distinct trends and low correlations.** ICL correlates at only 0.34-0.61 with other categories; citation generation also shows lower cross-category correlation (Figure 5, Section 3.2). This indicates these categories test distinct capabilities. Evidence breadth: 35 models, 7 categories, at 128K (strong evidence).

3. **Open-source models lag behind closed-source on complex long-context tasks, with the gap widening at longer contexts.** On citation generation and re-ranking, closed-source models (GPT-4o, Gemini-1.5-Pro) outperform the best open-source models by 30-40 absolute points at 128K (Figure 6, Figure 7, Section 3.3). Open-source models collapse on citation generation at 128K while GPT-4o remains stable. Evidence breadth: approximately 20 instruction-tuned models with 128K+ context, across 5 lengths (strong evidence across multiple categories).

4. **RAG tasks are the best proxy for real-world downstream performance.** RAG achieves the highest average Spearman correlation with downstream categories at 0.78, with HotpotQA correlating at 0.92 with LongQA (Figure 3, Figure 4, Section 3.1). RAG's advantage over synthetic tasks is attributed to its use of realistically distracting retrieved passages that prevent saturation. Evidence breadth: 35 models, single context length (strong evidence for 128K; not verified at other lengths in the main analysis).

5. **Model-based evaluation is more reliable than ROUGE.** GPT-4o-based evaluation reveals quality differences masked by ROUGE: Llama-3.1-8B-Inst scores similar ROUGE to GPT-4o but substantially lower on model-based evaluation; Mistral repetitive outputs receive ROUGE 12.3 but model-based 0.0 (Figure 2, Table 14, Section 2.2). Human agreement validation: kappa=0.76-0.91 for different components (Section B.6). Evidence breadth: 15 models on 3 datasets, with targeted human validation (moderate evidence).

6. **Two-shot demonstrations improve robustness and enable base model evaluation.** Adding 2 demonstrations to prompts substantially improves both base and instruction-tuned models (Table 8, Section 2.3). Llama-3.1-8B base improves from near-zero to meaningful performance on structured tasks. Three seeds show low variance. Evidence breadth: 11 models, 4 tasks, 3 seeds (moderate evidence).

7. **Positional embedding extrapolation degrades beyond training length.** Both Llama-3 with RoPE theta=16M and Qwen2 with YaRN scaling show sharp performance drops past L=32768, with degradation consistent across 8B-70B model sizes (Figure 7, Section E.3). Evidence breadth: 2 model families, multiple sizes, evaluated at 5 lengths (moderate evidence -- limited to RoPE-based extrapolation).

8. **HELMET provides more consistent model rankings than existing benchmarks.** At 128K tokens, HELMET rankings align with expected capability orderings while RULER and InfiniteBench produce anomalous rankings (Figure 1, Table 5, Table 9, Section A). The expected orderings are based on model family capability hierarchies (e.g., larger models outperforming smaller, Pro outperforming Flash). Evidence breadth: 6 frontier models for main comparison, 11 models for InfiniteBench comparison (moderate evidence -- relies on assumed capability orderings rather than human evaluation ground truth).

---

## Open Questions

1. **What is the optimal selection method for synthetic tasks that best correlate with downstream performance?** The authors acknowledge their selection of 4 RULER tasks for the recall subset "may not be optimal" and leave systematic selection as future work (Section E.1). Not addressed by existing references.

2. **How do HELMET rankings generalize to non-English languages?** All HELMET evaluation is English-only. Whether the observed correlations and category-specific trends hold for other languages is unknown. Not addressed by existing references.

3. **How should long-context evaluation adapt as models scale beyond 128K to 1M+ tokens?** HELMET evaluates up to 128K tokens, but several models claim 1M+ context windows. Whether HELMET's design principles (controllable length, hard negatives, model-based evaluation) scale to these lengths is untested. Not addressed by existing references.

4. **Can the gap between open-source and closed-source models on complex long-context tasks (citation, re-ranking) be closed with better training recipes rather than scale?** The 30-40 point gap at 128K may reflect training differences (e.g., instruction tuning quality, RLHF) rather than fundamental architectural limitations. Not addressed by existing references.

5. **What evaluation methodology should be used for long-context tasks not covered by HELMET, such as code understanding or multimodal contexts?** The authors explicitly exclude coding tasks as "out of scope for general long-context language modeling" (Section A.2), but code and multimodal settings are important LCLM applications. Not addressed by existing references.

---

## Core References and Why They Are Referenced

### Evaluation Benchmark Predecessors

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* RULER provides the synthetic recall tasks that HELMET selectively incorporates and serves as a primary comparison benchmark demonstrating that full RULER averages do not predict downstream performance.

- **Zhang et al. (2024b)** -- *InfiniteBench: Extending Long Context Evaluation Beyond 100K Tokens.* InfiniteBench is the primary prior benchmark at 128K+ tokens; HELMET directly compares against it and shows that improved prompting recovers capabilities InfiniteBench misses (e.g., Llama-3.2 models).

- **Shaham et al. (2023)** -- *ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding.* ZeroSCROLLS represents the zero-shot evaluation paradigm that HELMET extends with few-shot prompting and longer context support.

- **Bai et al. (2024)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* LongBench exemplifies benchmarks with diverse tasks but inadequate context lengths that HELMET aims to supersede.

- **An et al. (2024)** -- *L-Eval: Instituting Standardized Evaluation for Long Context Language Models.* L-Eval contributes the length-instruction-enhanced evaluation technique adopted by HELMET for summarization tasks.

### Foundational Tasks and Datasets

- **Kamradt (2024)** -- *Needle in a Haystack - Pressure Testing LLMs.* The original NIAH test that HELMET demonstrates is saturated across frontier models and poorly predictive of downstream performance.

- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Provides the gold passage positioning methodology adopted by HELMET and the lost-in-the-middle phenomenon that HELMET extends to 128K tokens.

- **Gao et al. (2023)** -- *Enabling Large Language Models to Generate Text with Citations.* Contributes the ALCE benchmark used for HELMET's citation generation category.

### Models Evaluated

- **Dubey et al. (2024)** -- *The Llama 3 Herd of Models.* Provides the Llama 3/3.1 model family that is central to HELMET's evaluation, demonstrating both the capabilities and limitations of open-source long-context models.

- **Team et al. (2024)** -- *Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens of Context.* Gemini 1.5 Pro/Flash serve as key proprietary baselines and their performance on HELMET establishes the capability frontier.

### Position Encoding and Context Extension

- **Peng et al. (2024)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* YaRN-based models (Qwen2) are evaluated to demonstrate that position extrapolation remains a challenge.

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE is the predominant positional encoding in evaluated models; its extrapolation properties are a key analysis dimension.
