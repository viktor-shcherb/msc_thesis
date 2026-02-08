---
title: "Language Models are Few-Shot Learners"
authors: "Brown, Mann, Ryder, Subbiah, Kaplan, et al."
year: 2020
venue: "NeurIPS 2020"
paper_type: conference-paper
categories: ["architecture", "in-context-learning", "scaling-laws", "model-release"]
scope: ["autoregressive language models", "few-shot evaluation", "meta-learning", "task-agnostic NLP"]
benchmarks_used: ["penn-treebank", "lambada", "storycloze", "hellaswag", "triviaqa", "natural-questions", "webqa", "wmt-translation", "winograd-schema", "winogrande", "piqa", "arc", "openbookqa", "squad", "race", "superglue", "boolq", "copa"]
models_introduced: ["gpt-3-175b"]
models_evaluated: ["bert-large", "gpt-2", "roberta-large"]
key_claims:
  - id: C1
    claim: "In-context learning ability improves with model scale; larger models make more efficient use of in-context examples"
    evidence: "Figure 1.2, Figure 1.3, aggregate results across 42 benchmarks"
    status: supported
    scope: "125M to 175B parameters, 42 accuracy-denominated benchmarks"
    magnitude: "Few-shot performance increases more rapidly than zero-shot with scale; gap widens at larger sizes"
  - id: C2
    claim: "GPT-3 175B achieves state-of-the-art on LAMBADA (86.4%) and TriviaQA (71.2%) in few-shot settings without gradient updates"
    evidence: "Table 3.2 (LAMBADA), Table 3.3 (TriviaQA)"
    status: supported
    scope: "175B model, few-shot setting (K=15 for LAMBADA, K=64 for TriviaQA), closed-book for TriviaQA"
    magnitude: "18.4 pp improvement over prior SOTA on LAMBADA; 3.2 pp over RAG on TriviaQA"
  - id: C3
    claim: "GPT-3-generated news articles are indistinguishable from human-written articles 52% of the time (near chance)"
    evidence: "Table 3.11, Table 3.12, Figure 3.13"
    status: supported
    scope: "200-500 word news articles, ~80 US-based participants per condition"
    magnitude: "52% detection accuracy vs 86% for control model; power-law decrease with model size"
  - id: C4
    claim: "Data contamination has minimal effect on benchmark performance for most datasets"
    evidence: "Section 4, Figure 4.2"
    status: supported
    scope: "13-gram overlap analysis across all evaluated benchmarks"
    magnitude: "~0% performance change on 75%+ clean benchmarks; PIQA 3 pp decrease, Winograd 2.6 pp decrease on clean subsets"
  - id: C5
    claim: "GPT-3 struggles with tasks requiring comparison of two text snippets"
    evidence: "WiC (49.4%), ANLI results (34-40%), Section 3.7, 3.8, 5"
    status: supported
    scope: "175B model, few-shot and one-shot settings, comparison-format tasks"
    magnitude: "WiC at 49.4% (random chance); ANLI R3 few-shot at ~40% vs SOTA ~48%"
  - id: C6
    claim: "GPT-3 few-shot outperforms prior unsupervised NMT by ~5 BLEU when translating into English"
    evidence: "Table 3.4"
    status: supported
    scope: "175B model, few-shot setting, translation into English (Fr, De, Ro), WMT'14/WMT'16"
    magnitude: "Fr->En 39.2 vs MASS 34.9; De->En 40.6 vs MASS 35.2; Ro->En 39.5 vs MASS 33.1"
  - id: C7
    claim: "GPT-3 175B achieves reasonable arithmetic proficiency, including 100% on 2-digit addition in few-shot"
    evidence: "Table 3.9, Figure 3.10"
    status: supported
    scope: "175B model, few-shot setting, synthetic arithmetic tasks"
    magnitude: "100% on 2D+, 98.9% on 2D-, 80.4% on 3D+, 29.2% on 2Dx; dramatic jump from 13B to 175B"
cross_references:
  - target: 2019-02-gpt-2-language-models-unsupervised
    type: extends
    detail: "GPT-3 scales GPT-2's architecture from 1.5B to 175B parameters, using same architecture with modified initialization, pre-normalization, reversible tokenization, and added sparse attention"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "GPT-3 uses Transformer decoder architecture with alternating dense and locally banded sparse attention"
  - target: 2022-12-chinchilla-scaling-laws
    type: extended-by
    detail: "Chinchilla revises GPT-3's scaling approach, showing that models should be trained on more tokens relative to parameters"
  - target: 2023-02-llama-open-efficient-foundation
    type: extended-by
    detail: "LLaMA-13B outperforms GPT-3 175B on most benchmarks by training on more tokens with architectural improvements"
  - target: 2023-07-llama-2-open-foundation-chat
    type: extended-by
    detail: "Llama 2 continues scaling open models with longer context and RLHF"
  - target: 2022-12-chain-of-thought-prompting
    type: extended-by
    detail: "Chain-of-thought prompting enhances GPT-3's reasoning by eliciting intermediate steps"
  - target: 2023-03-gpt-4-technical-report
    type: extended-by
    detail: "GPT-4 extends GPT-3's capabilities with multimodality and improved reasoning"
  - target: 2022-03-in-context-learning-induction-heads
    type: extended-by
    detail: "Olsson et al. provide mechanistic explanation for GPT-3's in-context learning via induction heads"
open_questions:
  - question: "Does in-context learning represent genuine task acquisition at inference time or pattern recognition from training?"
    addressed_by: 2022-03-in-context-learning-induction-heads
  - question: "Will continued scaling hit fundamental limits of the pretraining objective?"
    addressed_by: null
  - question: "Can bidirectional architectures achieve GPT-3's scale while maintaining few-shot learning abilities?"
    addressed_by: null
  - question: "How can pre-training sample efficiency be improved to approach human levels?"
    addressed_by: null
  - question: "How can language models be grounded in physical world experience or other modalities?"
    addressed_by: null
---

# Language Models are Few-Shot Learners

**Authors:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei (OpenAI; Jared Kaplan also Johns Hopkins University)
**Date:** December 2020, NeurIPS 2020 (arXiv:2005.14165)

---

## Core Research Problem

The dominant paradigm in NLP prior to GPT-3 involved pre-training on large text corpora followed by task-specific fine-tuning. While architecturally task-agnostic, this approach has critical limitations:

1. **Data requirements**: Strong performance "typically requires fine-tuning on a dataset of thousands to hundreds of thousands of examples specific to that task" (Section 1).

2. **Poor generalization**: "The potential to exploit spurious correlations in training data fundamentally grows with the expressiveness of the model and the narrowness of the training distribution." Fine-tuned models may "exaggerate actual performance on the underlying task" relative to human-level benchmarks (Section 1).

3. **Disconnect from human learning**: "Humans do not require large supervised datasets to learn most language tasks -- a brief directive in natural language... or at most a tiny number of demonstrations... is often sufficient to enable a human to perform a new task" (Section 1).

The paper introduces **in-context learning** as an alternative paradigm where the model adapts to tasks at inference time without gradient updates. This is framed as a form of meta-learning: "the model develops a broad set of skills and pattern recognition abilities at training time, and then uses those abilities at inference time to rapidly adapt to or recognize the desired task" (Section 1).

The key hypothesis is that in-context learning abilities scale with model size: "Since in-context learning involves absorbing many skills and tasks within the parameters of the model, it is plausible that in-context learning abilities might show similarly strong gains with scale" (Section 1).

**Core challenge: how to build task-agnostic language models that perform diverse NLP tasks competitively by conditioning on natural language descriptions and demonstrations at inference time, without any gradient updates.**

---

## Problem Solutions

GPT-3 addresses the problem by scaling autoregressive language models dramatically (to 175 billion parameters) and evaluating task performance using in-context learning rather than fine-tuning:

1. **Massive scale**: Train GPT-3 with 175B parameters -- "10x more than any previous non-sparse language model" (Section 1).

2. **Three evaluation settings without gradient updates**:
   - **Zero-shot**: Only a natural language task description
   - **One-shot**: One demonstration plus task description
   - **Few-shot**: K demonstrations (typically 10-100) that fit in the context window

3. **Systematic scaling analysis**: Train 8 model sizes from 125M to 175B parameters to study how in-context learning improves with scale.

---

## Approach Details

### Method

GPT-3 uses the same model architecture as GPT-2 (Radford et al., 2019):

> "We use the same model and architecture as GPT-2, including the modified initialization, pre-normalization, and reversible tokenization described therein, with the exception that we use alternating dense and locally banded sparse attention patterns in the layers of the transformer, similar to the Sparse Transformer." (Section 2.1)

The key methodological contribution is the in-context learning evaluation framework:

- **Zero-shot**: Task description followed by prompt (e.g., "Translate English to French: cheese =>")
- **One-shot**: Task description, one example, then prompt
- **Few-shot**: Task description, K examples (randomly drawn from training set), then prompt

Examples are delimited by 1-2 newlines. For multiple choice tasks, the model compares LM likelihood of each completion option, normalized by number of tokens. On a small number of datasets (ARC, OpenBookQA, RACE) likelihood is additionally normalized by the unconditional probability P(completion|"Answer:") (Section 2.4).

For free-form completion tasks, beam search is used with beam width 4 and length penalty alpha = 0.6 (Section 2.4).

### Key Technical Components

#### Model Configurations

| Model | Parameters | Layers | d_model | Heads | d_head | Batch Size | Learning Rate |
|---|---|---|---|---|---|---|---|
| GPT-3 Small | 125M | 12 | 768 | 12 | 64 | 0.5M | 6.0 x 10^-4 |
| GPT-3 Medium | 350M | 24 | 1024 | 16 | 64 | 0.5M | 3.0 x 10^-4 |
| GPT-3 Large | 760M | 24 | 1536 | 16 | 96 | 0.5M | 2.5 x 10^-4 |
| GPT-3 XL | 1.3B | 24 | 2048 | 24 | 128 | 1M | 2.0 x 10^-4 |
| GPT-3 2.7B | 2.7B | 32 | 2560 | 32 | 80 | 1M | 1.6 x 10^-4 |
| GPT-3 6.7B | 6.7B | 32 | 4096 | 32 | 128 | 2M | 1.2 x 10^-4 |
| GPT-3 13B | 13.0B | 40 | 5140 | 40 | 128 | 2M | 1.0 x 10^-4 |
| GPT-3 175B | 175.0B | 96 | 12288 | 96 | 128 | 3.2M | 0.6 x 10^-4 |

Context window: n_ctx = 2048 tokens for all models. Feed-forward dimension: d_ff = 4 * d_model. All models trained for 300 billion tokens (Table 2.1, Section 2.1).

#### Training Data

| Dataset | Tokens | Weight | Epochs (300B) |
|---|---|---|---|
| Common Crawl (filtered) | 410B | 60% | 0.44 |
| WebText2 | 19B | 22% | 2.9 |
| Books1 | 12B | 8% | 1.9 |
| Books2 | 55B | 8% | 0.43 |
| Wikipedia | 3B | 3% | 3.4 |

Training data is **93% English** by word count, 7% other languages. Common Crawl was downloaded from 41 monthly shards (2016-2019), constituting 45TB compressed before filtering and 570GB after filtering (~400B BPE tokens). Filtering used a classifier trained to distinguish high-quality text from raw web crawl. Fuzzy deduplication was performed at document level within and across datasets (Section 2.2, Appendix A). Higher-quality datasets are sampled more frequently: CommonCrawl and Books2 are seen less than once, while other datasets are seen 2-3 times (Table 2.2).

#### Training Procedure

- **Optimizer**: Adam with beta_1 = 0.9, beta_2 = 0.95, epsilon = 10^-8
- **Gradient clipping**: Global norm clipped at 1.0
- **Weight decay**: 0.1
- **Learning rate schedule**: Cosine decay to 10% of initial value over 260B tokens
- **LR warmup**: Linear warmup over first 375M tokens
- **Batch size ramp**: Gradually increased from 32K tokens to full value over first 4-12B tokens
- **Total training**: 300B tokens for all models
- **Sequence packing**: Multiple documents packed into 2048-token sequences, delimited by end-of-text token, no special masking (Appendix B)

### Experimental Setup

Models evaluated on **over 20 benchmarks** spanning:
- **Language modeling**: Penn Tree Bank, LAMBADA, HellaSwag, StoryCloze
- **Closed-book QA**: TriviaQA, Natural Questions, WebQuestions
- **Translation**: WMT'14 Fr-En, WMT'16 De-En, WMT'16 Ro-En (both directions)
- **Winograd-style**: Winograd (273 schemas), Winogrande
- **Common sense reasoning**: PIQA, ARC (Easy + Challenge), OpenBookQA
- **Reading comprehension**: CoQA, QuAC, DROP, SQuAD 2.0, RACE-h, RACE-m
- **SuperGLUE**: BoolQ, CB, COPA, RTE, WiC, WSC, MultiRC, ReCoRD
- **NLI**: ANLI (R1, R2, R3)
- **Synthetic**: 10 arithmetic tasks, 5 word scrambling tasks, SAT analogies
- **Qualitative**: News article generation, novel word usage, grammar correction

**Baselines**: Fine-tuned BERT-Large, RoBERTa, T5-11B, RAG, task-specific SOTA models.

**Compute**: V100 GPUs with model parallelism (within matrix multiply and across layers). GPT-3 175B consumed ~3,640 petaflop/s-days. By comparison, RoBERTa-Large used ~50 petaflop/s-days, similar to GPT-3 2.7B (Figure 2.2, Appendix D).

**Reproducibility**: Architecture hyperparameters, optimizer settings, and dataset composition are fully reported. Code repository exists at github.com/openai/gpt-3 but model weights were not publicly released. Random seeds not reported. Exact hardware configuration (number of GPUs, training duration) not fully specified.

### Key Results

#### Language Modeling and Completion

| Task | SOTA | GPT-3 Zero-Shot | GPT-3 One-Shot | GPT-3 Few-Shot |
|---|---|---|---|---|
| Penn Tree Bank (ppl) | 35.8 | **20.5** | -- | -- |
| LAMBADA (acc) | 68.0% | 76.2% | 72.5% | **86.4%** |
| LAMBADA (ppl) | 8.63 | 3.00 | 3.35 | **1.92** |
| StoryCloze (acc) | 91.8% | 83.2% | 84.7% | 87.7% |
| HellaSwag (acc) | 85.6% | 78.9% | 78.1% | 79.3% |

GPT-3 sets new SOTA on PTB perplexity (20.5 vs 35.8, zero-shot only since PTB lacks example structure) and LAMBADA accuracy (86.4%, improvement of over 18 pp from SOTA, Table 3.2). On LAMBADA, few-shot uses a fill-in-the-blank format that frames the task as cloze completion, which is not effective one-shot but dramatically improves few-shot performance (Section 3.1.2). HellaSwag and StoryCloze remain below fine-tuned SOTA (moderate evidence -- single model, no variance reported).

#### Closed-Book Question Answering

| Task | RAG (Fine-tuned) | T5-11B+SSM | T5-11B | GPT-3 Zero-Shot | GPT-3 One-Shot | GPT-3 Few-Shot |
|---|---|---|---|---|---|---|
| TriviaQA | 68.0% | 60.5% | 50.1% | 64.3% | 68.0% | **71.2%** |
| WebQuestions | 45.5% | 44.7% | 37.4% | 14.4% | 25.3% | 41.5% |
| Natural Questions | 44.5% | 36.6% | 34.5% | 14.6% | 23.0% | 29.9% |

GPT-3 few-shot achieves new SOTA on TriviaQA in the closed-book setting (71.2% vs RAG's 68.0%, Table 3.3). On WebQuestions and Natural Questions, the large gap between zero-shot and few-shot "may suggest a distribution shift" (Section 3.2). Performance scales smoothly with model size on all three datasets (strong evidence -- consistent trend across 8 model sizes, Figure 3.3).

#### Translation (BLEU)

| Direction | Supervised SOTA | Best Unsupervised (MASS) | GPT-3 Zero-Shot | GPT-3 One-Shot | GPT-3 Few-Shot |
|---|---|---|---|---|---|
| Fr->En | 35.0 | 34.9 | 21.2 | 33.7 | **39.2** |
| De->En | 40.2 | 35.2 | 27.2 | 30.4 | **40.6** |
| Ro->En | 39.9 | 33.1 | 19.9 | 38.6 | **39.5** |
| En->Fr | 45.6 | 37.5 | 25.2 | 28.3 | 32.6 |
| En->De | 41.2 | 29.8 (mBART) | 24.6 | 26.2 | 29.7 |
| En->Ro | 38.5 | 35.2 (MASS) | 14.1 | 20.6 | 21.0 |

Strong **asymmetry**: translation into English significantly outperforms translation from English. GPT-3 few-shot outperforms prior unsupervised NMT by ~5 BLEU when translating into English (Table 3.4). En->Ro is "a noticeable outlier at over 10 BLEU worse than prior unsupervised NMT work," possibly due to reusing GPT-2's English-optimized BPE tokenizer (Section 3.3). BLEU scores measured with multi-bleu.perl using XLM's tokenization for comparability with prior unsupervised work. All directions show smooth improvement with model capacity (moderate evidence -- single model per size, no variance reported).

#### Winograd-Style Tasks

| Task | Fine-tuned SOTA | GPT-3 Zero-Shot | GPT-3 One-Shot | GPT-3 Few-Shot |
|---|---|---|---|---|
| Winograd (273) | 90.1% | 88.3%* | 89.7%* | 88.6%* |
| Winogrande | 84.6% | 70.2% | 73.2% | 77.7% |

Winograd results marked with asterisk due to contamination concerns (45% flagged, 2.6% decrease on clean subset, Section 4). On Winogrande, few-shot GPT-3 175B (77.7%) is competitive with fine-tuned RoBERTa (79%) but well below SOTA T5 (84.6%) and human performance (94.0%) (Table 3.5). The gap between zero-shot and few-shot widens at larger model sizes (Figure 3.5).

#### Common Sense Reasoning

| Task | Fine-tuned SOTA | GPT-3 Zero-Shot | GPT-3 One-Shot | GPT-3 Few-Shot |
|---|---|---|---|---|
| PIQA | 79.4% | 81.0%* | 80.5%* | 82.8%* |
| ARC (Easy) | 92.0% | 68.8% | 71.2% | 70.1% |
| ARC (Challenge) | 78.5% | 51.4% | 53.2% | 51.5% |
| OpenBookQA | 87.2% | 57.6% | 58.8% | 65.4% |

GPT-3 sets SOTA on PIQA (82.8%) in few-shot (marked with asterisk due to 29% contamination flagging and 3 pp decrease on clean subset, Section 4). ARC and OpenBookQA remain far below SOTA -- UnifiedQA exceeds GPT-3 by 27% on ARC Challenge and 22% on OpenBookQA (Table 3.6, Section 3.5). In-context learning gains are "mixed" with "small and inconsistent gains" on PIQA and ARC (limited evidence per task -- single model configuration).

#### Reading Comprehension

| Task | Fine-tuned SOTA | GPT-3 Zero-Shot | GPT-3 One-Shot | GPT-3 Few-Shot |
|---|---|---|---|---|
| CoQA (F1) | 90.7 | 81.5 | 84.0 | 85.0 |
| DROP (F1) | 89.1 | 23.6 | 34.3 | 36.5 |
| QuAC (F1) | 74.4 | 41.5 | 43.3 | 44.3 |
| SQuAD 2.0 (F1) | 93.0 | 59.5 | 65.4 | 69.8 |
| RACE-h (acc) | 90.0% | 45.5% | 45.9% | 46.8% |
| RACE-m (acc) | 93.1% | 58.4% | 57.4% | 58.1% |

GPT-3 performs best on CoQA (85.0 F1 few-shot, within 3 points of human baseline) and worst on QuAC (44.3 F1, 13 points below an ELMo baseline). On SQuAD 2.0, few-shot improves by ~10 F1 over zero-shot, slightly outperforming the original paper's fine-tuned BERT baseline. RACE performance is "relatively weak" -- "only competitive with the earliest work utilizing contextual representations and is still 45% behind SOTA" (Table 3.7, Section 3.6). Wide spread in performance suggests varying capability across answer formats (limited evidence for format-sensitivity claim -- observational, no controlled ablation).

#### SuperGLUE

| Task | Fine-tuned SOTA | BERT-Large | GPT-3 Few-Shot |
|---|---|---|---|
| Average | 89.0 | 69.0 | 71.8 |
| BoolQ (acc) | 91.0 | 77.4 | 76.4 |
| CB (acc) | 96.9 | 83.6 | 75.6 |
| CB (F1) | 93.9 | 75.7 | 52.0 |
| COPA (acc) | 94.8 | 70.6 | **92.0** |
| RTE (acc) | 92.5 | 71.7 | 69.0 |
| WiC (acc) | 76.1 | 69.6 | 49.4 |
| WSC (acc) | 93.8 | 64.6 | 80.1 |
| MultiRC (acc) | 62.3 | 24.1 | 30.5 |
| MultiRC (F1a) | 88.2 | 70.0 | 75.4 |
| ReCoRD (acc) | 92.5 | 71.3 | **90.2** |
| ReCoRD (F1) | 93.3 | 72.0 | 91.1 |

GPT-3 few-shot (K=32) achieves near-SOTA on COPA (92.0%) and ReCoRD (90.2% acc, 91.1 F1), but **WiC at 49.4% is random chance level** (Table 3.8). GPT-3 outperforms BERT-Large on 4 of 8 tasks. The SuperGLUE score increases with both model size and K, with GPT-3 surpassing BERT-Large at approximately K=8 (Figure 3.8). WiC failure "hints at" a broader pattern where "GPT-3 appears to be weak in the few-shot or one-shot setting at some tasks that involve comparing two sentences or snippets" (Section 3.7) (strong evidence for scaling trend -- tested across 8 model sizes and multiple K values; limited evidence for comparison-task weakness -- observational pattern across a few tasks).

#### NLI

ANLI R3 few-shot GPT-3 175B achieves ~40% accuracy (vs SOTA ~48% and random chance 33%). All smaller models "hover around random chance" on all ANLI rounds, and only the 175B few-shot model "closes almost half the gap from random chance to SOTA" (Figure 3.9). RTE few-shot achieves 69.0% (Section 3.8). These results suggest "NLI is still a very difficult task for language models and they are only just beginning to show signs of progress" (limited evidence -- dev-set evaluation with only 1500 examples, estimated 1.2% standard deviation).

#### Arithmetic

| Task | Zero-Shot | One-Shot | Few-Shot |
|---|---|---|---|
| 2-digit Addition | 76.9% | 99.6% | **100.0%** |
| 2-digit Subtraction | 58.0% | 86.4% | **98.9%** |
| 3-digit Addition | 34.2% | 65.5% | 80.4% |
| 3-digit Subtraction | 48.3% | 78.7% | 94.2% |
| 4-digit Addition | 4.0% | 14.0% | 25.5% |
| 4-digit Subtraction | 7.5% | 14.0% | 26.8% |
| 5-digit Addition | 0.7% | 3.5% | 9.3% |
| 5-digit Subtraction | 0.8% | 3.8% | 9.9% |
| 2-digit Multiplication | 19.8% | 27.4% | 29.2% |
| 1-digit Composite | 9.8% | 14.3% | 21.3% |

**Significant capability jump from 13B to 175B** -- the 13B model solves 2-digit arithmetic only ~50% of the time (Table 3.9, Figure 3.10). Memorization spot-check found only 17/2000 (0.8%) addition problems and 2/2000 (0.1%) subtraction problems in training data. Incorrect answers show patterns (e.g., not carrying a "1") suggesting actual computation rather than table memorization (Section 3.9.1) (moderate evidence -- 2000-instance test sets, memorization analysis performed, but single model per size).

#### Word Scrambling

| Task | Zero-Shot | One-Shot | Few-Shot |
|---|---|---|---|
| Cycle Letters (CL) | 3.7% | 21.7% | 37.9% |
| Anagrams-1 (A1) | 2.3% | 8.6% | 15.1% |
| Anagrams-2 (A2) | 8.9% | 25.9% | 39.7% |
| Random Insertion (RI) | 8.3% | 45.4% | 67.2% |
| Reversed Words (RW) | 0.1% | 0.5% | 0.4% |

**Reversed words: near-zero performance** across all model sizes and settings. The dramatic difference between zero-shot and few-shot performance (especially for Random Insertion: 8.3% to 67.2%) "suggests that the model really does appear to learn these tasks at test time" (Table 3.10, Section 3.9.2). These tasks require character-level manipulation despite BPE encoding operating on sub-word units (~0.7 words per token on average).

#### SAT Analogies

GPT-3 achieves **65.2% few-shot, 59.1% one-shot, 53.7% zero-shot** on 374 SAT analogy problems. The average college applicant scored 57%. The 175B model improves by over 10% compared to the 13B model. Random chance is 20% (Section 3.9.3, Figure 3.12).

#### News Article Generation

| Model | Mean Human Detection Accuracy | 95% CI |
|---|---|---|
| Control (bad model) | 86% | 83%-90% |
| GPT-3 Small (125M) | 76% | 72%-80% |
| GPT-3 Medium (350M) | 61% | 58%-65% |
| GPT-3 Large (760M) | 68% | 64%-72% |
| GPT-3 XL (1.3B) | 62% | 59%-65% |
| GPT-3 2.7B | 62% | 58%-65% |
| GPT-3 6.7B | 60% | 56%-63% |
| GPT-3 13B | 55% | 52%-58% |
| GPT-3 175B | 52% | 49%-54% |

Longer articles (~500 words): control 88%, GPT-3 175B 52% (Table 3.11, Table 3.12). Human detection accuracy follows a **power-law decrease** with model size (Figure 3.13). Approximately 80 US-based participants per condition. Statistical significance confirmed via two-sample T-tests: 175B vs control t=16.9, p=1e-34 (strong evidence -- multiple model sizes, ~80 participants per condition, separate control, statistical testing).

---

## Limitations and Failure Modes

### Explicitly Acknowledged Limitations

1. **Text synthesis weaknesses**: GPT-3 samples "sometimes repeat themselves semantically at the document level, start to lose coherence over sufficiently long passages, contradict themselves, and occasionally contain non-sequitur sentences or paragraphs" (Section 5).

2. **Comparison task failures**: Near-chance performance on tasks requiring comparing two sentences or snippets, including WiC (49.4%), ANLI (34-40%), and certain reading comprehension tasks. "This could also explain the comparatively low scores for RTE and CB, which also follow this format" (Section 5).

3. **Autoregressive architecture limitations**: The focus on autoregressive language models (without bidirectional architectures) "comes at the cost of potentially worse performance on tasks which empirically benefit from bidirectionality" -- fill-in-the-blank tasks, tasks requiring looking back and comparing content (Section 5).

4. **Limits of the pretraining objective**: "Scaling pure self-supervised prediction is likely to hit limits, and augmentation with a different approach is likely to be necessary." The objective weights every token equally, lacks a notion of what is most important, and the model is not grounded in other modalities (Section 5).

5. **Poor sample efficiency**: GPT-3 sees "much more text during pre-training than a human sees in their lifetime" (Section 5).

6. **Inference cost**: "Models at the scale of GPT-3... are both expensive and inconvenient to perform inference on" (Section 5).

7. **Ambiguity of few-shot learning**: Unclear whether few-shot learning "actually learns new tasks 'from scratch' at inference time, or if it simply recognizes and identifies tasks that it has learned during training" (Section 5).

8. **Inherited biases**: Gender bias (83% of occupations more likely followed by male identifiers), racial bias (consistently low sentiment for "Black" across model sizes), and religious associations (Islam associated with violence/terrorism-related words in top 40 co-occurrences) (Section 6.2).

### Tasks Where GPT-3 Struggles

- **Natural language inference**: ANLI R3 ~40% (vs SOTA ~48%), RTE 69.0% (Section 3.8)
- **Reading comprehension**: RACE-h 46.8%, RACE-m 58.1%, QuAC 44.3 F1, DROP 36.5 F1 (Table 3.7)
- **Word-in-context**: WiC 49.4% (random chance level) (Table 3.8)
- **Reversed words**: Near-zero performance across all model sizes (Table 3.10)
- **Common sense physics**: Difficulty with questions like "If I put cheese into the fridge, will it melt?" despite doing well on PIQA (Section 5)

### Data Contamination

A bug in contamination filtering caused some overlaps to remain in training data. Conservative 13-gram overlap analysis found 75%+ of benchmarks were clean with ~0% performance change on clean subsets. PIQA (29% flagged) showed 3 pp decrease; Winograd (45% flagged) showed 2.6 pp decrease. Wikipedia-based language modeling benchmarks were excluded entirely due to contamination. Manual inspection found reading comprehension overlaps contained source text but not question-answer pairs. LAMBADA had "substantial genuine contamination" but impact was within 0.5% (Section 4, Figure 4.2).

#### Scope and Comparability

- **What was not tested:** No evaluation on non-English NLU benchmarks (only English and translation tasks); no evaluation of fine-tuned GPT-3 (deliberately omitted to focus on in-context learning); no evaluation with bidirectional or encoder-decoder objectives; no evaluation at context lengths beyond 2048 tokens; no evaluation on generation quality metrics beyond human discrimination of news articles.
- **[Inferred]** No evaluation on code generation, summarization, or dialogue tasks beyond CoQA/QuAC.
- **Comparability notes:** Translation BLEU scores use multi-bleu.perl with XLM tokenization (not SacreBLEU) for comparability with prior unsupervised NMT work; SacreBLEU scores reported separately in Appendix H. SuperGLUE results submitted to test server for few-shot only, other settings use development set. The "closed-book" QA setting is stricter than standard closed-book (no fine-tuning on QA datasets either). PIQA few-shot result is from test server; other PIQA results from development set. Winograd evaluation uses the "partial evaluation" method from GPT-2, which differs from the WSC binary classification format in SuperGLUE.

---

## Conclusions

### Contributions

1. **Largest dense language model**: Trained GPT-3 with 175B parameters, 10x larger than previous non-sparse models, demonstrating continued scaling benefits with a smooth power-law trend extending two orders of magnitude beyond prior work (Section 2, Figure 3.1).

2. **In-context learning paradigm**: Established systematic framework for zero-shot, one-shot, and few-shot evaluation without gradient updates, showing competitive performance across diverse NLP tasks (Section 1, 3).

3. **Scaling behavior of in-context learning**: Demonstrated that "few-shot performance increases more rapidly" with scale than zero-shot, with "larger models make increasingly efficient use of in-context information" across 42 benchmarks (Figures 1.2, 1.3).

4. **State-of-the-art results without fine-tuning**: Achieved SOTA on LAMBADA (86.4%), TriviaQA (71.2%), PTB perplexity (20.5), PIQA (82.8%), and near-SOTA on COPA (92.0%) and ReCoRD (90.2%) (Section 3).

5. **Translation capabilities from English-dominant training**: GPT-3 few-shot outperforms prior unsupervised NMT by ~5 BLEU when translating into English despite being trained on only 7% non-English text (Section 3.3, Table 3.4).

6. **Systematic contamination analysis**: Conducted thorough analysis of data contamination effects using 13-gram overlap, finding minimal impact on most benchmarks and flagging specific problematic datasets (Section 4).

7. **Bias documentation**: Provided preliminary analysis of gender, racial, and religious biases in the model's outputs with systematic co-occurrence methodology (Section 6.2).

### Implications

1. **Task-agnostic NLP systems**: "Very large language models may be an important ingredient in the development of adaptable, general language systems" that can perform diverse tasks without task-specific training data (Section 8).

2. **Meta-learning interpretation**: The gap between zero/one/few-shot performance growing with model size "perhaps suggests that larger models are more proficient meta-learners" (Section 1).

3. **Limits of pure self-supervision**: Augmentation with different approaches -- "learning the objective function from humans, fine-tuning with reinforcement learning, or adding additional modalities such as images" -- will likely be necessary (Section 5). [Speculative at time of publication, later confirmed by InstructGPT and multimodal model development.]

4. **Practical deployment concerns**: Model scale creates inference cost challenges; distillation "has not been tried at the scale of hundreds of billions of parameters" and "new challenges and opportunities may be associated with applying it to models of this size" (Section 5).

---

## Key Claims

1. **C1: In-context learning improves with scale.** Figure 1.2 shows that "larger models make increasingly efficient use of in-context information" on a word-unscrambling task. Figure 1.3 shows that across 42 accuracy-denominated benchmarks, "few-shot performance increases more rapidly" than zero-shot with model size. The gap between zero-shot and few-shot widens with model capacity. **Scope:** 125M to 175B parameters, 42 benchmarks. **Magnitude:** Aggregate few-shot at 175B is approximately 60-65 vs zero-shot at approximately 45-50. Status: **supported** (strong evidence -- tested across 8 model sizes and 42 benchmarks).

2. **C2: GPT-3 achieves SOTA on LAMBADA and TriviaQA in few-shot settings.** LAMBADA: 86.4% accuracy vs. prior SOTA of 68.0% (Table 3.2), using fill-in-the-blank format with K=15. TriviaQA: 71.2% vs. RAG's 68.0% in closed-book setting (Table 3.3), with K=64. Both without gradient updates. **Scope:** 175B model, specific K values, closed-book for TriviaQA. **Magnitude:** +18.4 pp on LAMBADA; +3.2 pp on TriviaQA. Status: **supported** (moderate evidence -- single model, test-server evaluation for TriviaQA wiki split).

3. **C3: Human-generated text detection approaches chance for GPT-3 175B.** Humans achieved only 52% accuracy on ~200-word articles (Table 3.11) and 52% on ~500-word articles (Table 3.12), compared to 86-88% for control models. The decrease follows a power-law with model size (Figure 3.13). **Scope:** ~80 US participants per condition, 200-500 word news articles. **Magnitude:** 52% detection vs 86% control (t=16.9, p=1e-34). Status: **supported** (strong evidence -- multiple model sizes, ~80 participants per condition, control experiments, statistical testing).

4. **C4: Data contamination minimally affects most benchmarks.** Conservative 13-gram overlap analysis found 75%+ of benchmarks were clean with ~0% performance change on clean subsets (Figure 4.2). Exceptions: PIQA (3 pp decrease) and Winograd (2.6 pp decrease). **Scope:** All evaluated benchmarks using 13-gram overlap. **Magnitude:** ~0% change for most; 2-4 pp for flagged datasets. Status: **supported** (moderate evidence -- conservative methodology may overcount contamination; clean subsets may not be identically distributed).

5. **C5: GPT-3 struggles with comparison tasks.** WiC achieves 49.4% (random chance, Table 3.8), ANLI R3 achieves ~40% few-shot vs SOTA ~48% (Figure 3.9). Pattern extends to RTE (69%) and CB (75.6% acc, 52.0% F1). The paper attributes this to autoregressive architecture lacking bidirectionality (Section 5). **Scope:** 175B model, comparison-format tasks in few-shot and one-shot settings. **Magnitude:** WiC at random chance; ANLI closes only half the gap from chance to SOTA. Status: **supported** (moderate evidence -- consistent pattern across multiple comparison tasks, but causal attribution to architecture is conjectural).

6. **C6: GPT-3 few-shot outperforms prior unsupervised NMT by ~5 BLEU into English.** Fr->En 39.2 vs MASS 34.9 (+4.3); De->En 40.6 vs MASS 35.2 (+5.4); Ro->En 39.5 vs MASS 33.1 (+6.4) (Table 3.4). Translation from English significantly underperforms. **Scope:** 175B model, few-shot, translation into English only, WMT'14/16, multi-bleu.perl scoring. **Magnitude:** +4.3 to +6.4 BLEU into English; -3 to -14 BLEU from English vs unsupervised SOTA. Status: **supported** (moderate evidence -- single model, one scoring method; SacreBLEU scores in appendix).

7. **C7: GPT-3 175B achieves reasonable arithmetic proficiency.** 100% on 2-digit addition, 98.9% on 2-digit subtraction, 80.4% on 3-digit addition in few-shot setting (Table 3.9). Dramatic capability jump from 13B to 175B -- 13B solves 2-digit arithmetic ~50% of the time (Figure 3.10). **Scope:** 175B model, few-shot, synthetic arithmetic tasks with 2000 test instances each. **Magnitude:** Near-perfect on 2-digit, ~80-94% on 3-digit, 25-27% on 4-digit, 29.2% on 2-digit multiplication. Status: **supported** (moderate evidence -- 2000-instance test sets, memorization check performed, but no variance estimates).

---

## Open Questions

1. **Nature of in-context learning**: Does few-shot learning represent genuine task acquisition at inference time, or pattern recognition from training? The paper notes this is "ambiguous" and "may also vary from task to task" -- synthetic tasks like word scrambling "seem especially likely to be learned de novo, whereas translation clearly must be learned during pretraining" (Section 5). Partially addressed by Olsson et al. (2022) -- *In-context Learning and Induction Heads* -- which identifies induction heads as a mechanistic explanation.

2. **Limits of scaling**: Will continued scaling hit fundamental limits of the pretraining objective? The paper notes the objective "weights every token equally and lacks a notion of what is most important to predict" and that "scaling pure self-supervised prediction is likely to hit limits" (Section 5). When will augmentation with other approaches become necessary? Not directly addressed.

3. **Bidirectional models at scale**: Can bidirectional architectures achieve GPT-3's scale while maintaining few-shot learning abilities? The paper conjectures that "a large bidirectional model would be stronger at fine-tuning than GPT-3" and that "making a bidirectional model at the scale of GPT-3, and/or trying to make bidirectional models work with few- or zero-shot learning, is a promising direction" (Section 5). Not directly addressed.

4. **Sample efficiency**: How can pre-training sample efficiency be improved to approach human levels? "Might come from grounding in the physical world to provide additional information, or from algorithmic improvements" (Section 5). Not directly addressed.

5. **Grounding**: How can language models be grounded in "other domains of experience, such as video or real-world physical interaction"? The paper notes models "lack a large amount of context about the world" and suggests "adding additional modalities such as images" as a promising direction (Section 5). Not directly addressed.

---

## Core References and Why They Are Referenced

### Architecture and Scaling

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that GPT-3 builds upon, using the decoder-only autoregressive variant.

- **Radford et al. (2019)** -- *Language Models are Unsupervised Multitask Learners (GPT-2).* Direct predecessor. GPT-3 uses identical architecture with modified initialization, pre-normalization, and reversible tokenization. Scaled from 1.5B to 175B parameters. GPT-2 was the first to explore in-context learning, achieving 4% on Natural Questions and 55 F1 on CoQA (Section 1).

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Predicted smooth power-law improvement with compute. Guided GPT-3's model/data scaling decisions and batch size/learning rate choices. GPT-3 extends these trends by two orders of magnitude (Section 2.1, 2.3, Figure 3.1).

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* GPT-3 uses "alternating dense and locally banded sparse attention patterns" from this work (Section 2.1).

### Pre-training and Fine-tuning Baselines

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers.* Established bidirectional pre-training paradigm. GPT-3 deliberately omits bidirectionality to focus on autoregressive in-context learning. BERT-Large serves as fine-tuning baseline on SuperGLUE (69.0 average, Table 3.8).

- **Liu et al. (2019)** -- *RoBERTa: A Robustly Optimized BERT Pretraining Approach.* Improved BERT pretraining. Serves as fine-tuning comparison baseline on Winogrande (79%) and ANLI, representing ~50 petaflop/s-days of compute (Figure 2.2).

- **Raffel et al. (2019)** -- *Exploring the Limits of Transfer Learning with T5.* 11B parameter encoder-decoder model representing fine-tuned SOTA on many benchmarks. T5-11B+SSM's closed-book QA results (36.6% NQ, 60.5% TriviaQA) are surpassed by GPT-3 few-shot (Table 3.3).

- **Lewis et al. (2020)** -- *RAG: Retrieval-Augmented Generation.* Represents open-domain fine-tuning SOTA on QA with a 15.3B parameter dense vector index of 21M documents. GPT-3 one-shot matches RAG on TriviaQA (68.0%) and few-shot surpasses it (71.2%) (Table 3.3).

### Meta-Learning

- **Vinyals et al. (2016)** -- *Matching Networks for One Shot Learning.* GPT-3's in-context learning relates to this meta-learning approach, where a broad distribution of tasks is used during training (Section 7).

- **Duan et al. (2016)** -- *RL2: Fast Reinforcement Learning via Slow Reinforcement Learning.* GPT-3's approach of "stuffing the model's context with previous examples is most structurally similar to RL2" (Section 7).

### Evaluation Benchmarks

- **Wang et al. (2019)** -- *SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding.* Primary benchmark suite for evaluating GPT-3's language understanding capabilities (Section 3.7).

- **Paperno et al. (2016)** -- *The LAMBADA Dataset.* Long-range dependency benchmark where GPT-3 achieves SOTA (86.4% vs prior 68.0%, Table 3.2).

- **Nie et al. (2019)** -- *Adversarial NLI (ANLI).* Adversarially-mined NLI benchmark exposing GPT-3's weakness on comparison tasks (Section 3.8).

### Contamination and Training Data

- **Trinh and Le (2018)** -- *A Simple Method for Commonsense Reasoning.* First paper to train an LM on Common Crawl data and detect/remove training overlap with evaluation data, establishing precedent for GPT-3's contamination analysis (Section 4).
