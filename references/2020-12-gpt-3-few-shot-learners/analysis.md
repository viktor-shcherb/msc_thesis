---
title: "Language Models are Few-Shot Learners"
authors: "Brown, Mann, Ryder, Subbiah, Kaplan, et al."
year: 2020
venue: "NeurIPS 2020"
paper_type: conference-paper
categories: ["architecture", "in-context-learning", "scaling-laws", "model-release"]
scope: ["autoregressive language models", "few-shot evaluation", "meta-learning", "task-agnostic NLP"]
benchmarks_used: ["perplexity-wikitext103", "triviaqa", "natural-questions", "webqa", "squad", "race", "hellaswag", "piqa", "winogrande", "arc", "boolq", "gsm8k", "mmlu"]
models_introduced: ["gpt-3-175b"]
models_evaluated: ["bert-large", "gpt-2", "roberta-large"]
key_claims:
  - id: C1
    claim: "In-context learning ability improves with model scale; larger models make more efficient use of in-context examples"
    evidence: "Figure 1.2, Figure 1.3, aggregate results across 42 benchmarks"
    status: supported
    scope: "125M to 175B parameters"
    magnitude: "Few-shot performance increases more rapidly than zero-shot with scale"
  - id: C2
    claim: "GPT-3 175B achieves state-of-the-art on LAMBADA (86.4%) and TriviaQA (71.2%) in few-shot settings without gradient updates"
    evidence: "Table 3.1 (LAMBADA), Table 3.3 (TriviaQA)"
    status: supported
    magnitude: "18.4% improvement over prior SOTA on LAMBADA; 3.2% over RAG on TriviaQA"
  - id: C3
    claim: "GPT-3-generated news articles are indistinguishable from human-written articles 52% of the time (near chance)"
    evidence: "Table 3.11, Table 3.12, Figure 3.13"
    status: supported
    scope: "200-500 word articles"
  - id: C4
    claim: "Data contamination has minimal effect on benchmark performance for most datasets"
    evidence: "Section 4, Figure 4.2, Table C.1"
    status: supported
    scope: "75%+ clean datasets showed ~0% performance change"
  - id: C5
    claim: "GPT-3 struggles with tasks requiring comparison of two text snippets"
    evidence: "WiC (49.4%), ANLI results, Section 5"
    status: supported
    magnitude: "WiC at random chance level"
cross_references:
  - target: 2019-02-gpt-2-language-models-unsupervised
    type: extends
    detail: "GPT-3 scales GPT-2's architecture from 1.5B to 175B parameters, using same architecture with modified initialization and sparse attention"
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
---

# Language Models are Few-Shot Learners

**Authors:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei (OpenAI)
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

Examples are delimited by 1-2 newlines. For multiple choice tasks, the model compares LM likelihood of each completion option, normalized by number of tokens.

### Key Technical Components

#### Model Configurations

| Model | Parameters | Layers | d_model | Heads | d_head | Batch Size | Learning Rate |
|---|---|---|---|---|---|---|---|
| GPT-3 Small | 125M | 12 | 768 | 12 | 64 | 0.5M | 6.0 × 10⁻⁴ |
| GPT-3 Medium | 350M | 24 | 1024 | 16 | 64 | 0.5M | 3.0 × 10⁻⁴ |
| GPT-3 Large | 760M | 24 | 1536 | 16 | 96 | 0.5M | 2.5 × 10⁻⁴ |
| GPT-3 XL | 1.3B | 24 | 2048 | 24 | 128 | 1M | 2.0 × 10⁻⁴ |
| GPT-3 2.7B | 2.7B | 32 | 2560 | 32 | 80 | 1M | 1.6 × 10⁻⁴ |
| GPT-3 6.7B | 6.7B | 32 | 4096 | 32 | 128 | 2M | 1.2 × 10⁻⁴ |
| GPT-3 13B | 13.0B | 40 | 5140 | 40 | 128 | 2M | 1.0 × 10⁻⁴ |
| GPT-3 175B | 175.0B | 96 | 12288 | 96 | 128 | 3.2M | 0.6 × 10⁻⁴ |

Context window: n_ctx = 2048 tokens for all models. Feed-forward dimension: d_ff = 4 × d_model.

#### Training Data

| Dataset | Tokens | Weight | Epochs (300B) |
|---|---|---|---|
| Common Crawl (filtered) | 410B | 60% | 0.44 |
| WebText2 | 19B | 22% | 2.9 |
| Books1 | 12B | 8% | 1.9 |
| Books2 | 55B | 8% | 0.43 |
| Wikipedia | 3B | 3% | 3.4 |

Training data is 93% English by word count, 7% other languages. Common Crawl was filtered using a classifier trained to distinguish high-quality text from raw web crawl, then fuzzy deduplicated at document level.

#### Training Procedure

- **Optimizer**: Adam with β₁ = 0.9, β₂ = 0.95, ε = 10⁻⁸
- **Gradient clipping**: Global norm clipped at 1.0
- **Weight decay**: 0.1
- **Learning rate schedule**: Cosine decay to 10% of initial value over 260B tokens
- **LR warmup**: Linear warmup over first 375M tokens
- **Total training**: 300B tokens for all models

### Experimental Setup

Models evaluated on 20+ benchmarks spanning:
- **Language modeling**: Penn Tree Bank, LAMBADA
- **Closed-book QA**: TriviaQA, Natural Questions, WebQuestions
- **Translation**: WMT'14 (Fr-En), WMT'16 (De-En, Ro-En)
- **Reading comprehension**: CoQA, QuAC, DROP, SQuAD 2.0, RACE
- **SuperGLUE**: BoolQ, CB, COPA, RTE, WiC, WSC, MultiRC, ReCoRD
- **Common sense**: PIQA, ARC, OpenBookQA, Winograd, Winogrande
- **NLI**: ANLI (R1, R2, R3)
- **Synthetic**: Arithmetic, word scrambling, SAT analogies

**Baselines**: Fine-tuned BERT-Large, RoBERTa, T5-11B, and task-specific SOTA models. Compute: V100 GPUs, ~3,640 petaflop/s-days for 175B model.

### Key Results

#### Language Modeling and Completion

| Task | SOTA | GPT-3 Zero-Shot | GPT-3 Few-Shot |
|---|---|---|---|
| Penn Tree Bank (ppl) | 35.8 | **20.5** | -- |
| LAMBADA (acc) | 68.0% | 76.2% | **86.4%** |
| LAMBADA (ppl) | 8.63 | 3.00 | **1.92** |
| StoryCloze (acc) | 91.8% | 83.2% | 87.7% |

GPT-3 few-shot achieves 86.4% on LAMBADA, an improvement of over 18 percentage points from previous SOTA.

#### Closed-Book Question Answering

| Task | Fine-tuned SOTA | GPT-3 Zero-Shot | GPT-3 Few-Shot |
|---|---|---|---|
| TriviaQA | 68.0% (RAG) | 64.3% | **71.2%** |
| WebQuestions | 45.5% (RAG) | 14.4% | 41.5% |
| Natural Questions | 44.5% (RAG) | 14.6% | 29.9% |

GPT-3 few-shot achieves new SOTA on TriviaQA in the closed-book setting (71.2%), outperforming RAG despite no retrieval.

#### Translation (BLEU)

| Direction | Supervised SOTA | GPT-3 Zero-Shot | GPT-3 Few-Shot |
|---|---|---|---|
| Fr→En | 35.0 | 21.2 | **39.2** |
| De→En | 40.2 | 27.2 | **40.6** |
| Ro→En | 39.9 | 19.9 | **39.5** |
| En→Fr | 45.6 | 25.2 | 32.6 |
| En→De | 41.2 | 24.6 | 29.7 |

Strong asymmetry: translation into English significantly better than from English. GPT-3 outperforms previous unsupervised NMT by ~5 BLEU when translating into English.

#### SuperGLUE

| Task | Fine-tuned SOTA | BERT-Large | GPT-3 Few-Shot |
|---|---|---|---|
| Average | 89.0 | 69.0 | 71.8 |
| COPA | 94.8 | 70.6 | **92.0** |
| ReCoRD (acc) | 92.5 | 71.3 | **90.2** |
| WSC | 93.8 | 64.6 | 80.1 |
| WiC | 76.1 | 69.6 | 49.4 |

GPT-3 achieves near-SOTA on COPA (92.0%) and ReCoRD (90.2%), but WiC (49.4%) is at random chance level.

#### Arithmetic

| Task | Zero-Shot | One-Shot | Few-Shot |
|---|---|---|---|
| 2-digit Addition | 76.9% | 99.6% | **100.0%** |
| 2-digit Subtraction | 58.0% | 86.4% | **98.9%** |
| 3-digit Addition | 34.2% | 65.5% | 80.4% |
| 4-digit Addition | 4.0% | 14.0% | 25.5% |
| 2-digit Multiplication | 19.8% | 27.4% | 29.2% |

Significant capability jump from 13B to 175B model. Smaller models (even 13B) solve 2-digit arithmetic only ~50% of the time.

#### News Article Generation

| Model | Human Detection Accuracy |
|---|---|
| GPT-3 175B (~200 words) | **52%** (near chance) |
| GPT-3 175B (~500 words) | **52%** |
| Control (bad model) | 86% |

Human detection accuracy approaches chance level as model size increases, following a power-law trend.

---

## Limitations and Failure Modes

### Explicitly Acknowledged Limitations

1. **Text synthesis weaknesses**: GPT-3 samples sometimes repeat themselves semantically at the document level, lose coherence over sufficiently long passages, contradict themselves, and occasionally contain non-sequitur sentences or paragraphs (Section 5).

2. **Comparison task failures**: Near-chance performance on tasks requiring comparing two sentences or snippets, including WiC (49.4%), ANLI, and certain reading comprehension tasks (Section 5).

3. **Autoregressive architecture limitations**: The focus on autoregressive language models (without bidirectional architectures) may hurt performance on fill-in-the-blank tasks and tasks requiring looking back and comparing content (Section 5).

4. **Poor sample efficiency**: GPT-3 sees far more text during pre-training than a human sees in their lifetime (Section 5).

5. **Inference cost**: Models at GPT-3's scale are expensive and inconvenient for practical inference (Section 5).

6. **Inherited biases**: The model retains biases present in training data, including gender bias (83% of occupations more likely followed by male identifiers), racial bias (consistently low sentiment for "Black"), and religious associations (Islam associated with violence-related words) (Section 6.2).

### Tasks Where GPT-3 Struggles

- **Natural language inference**: ANLI (34-40%), RTE (69%)
- **Reading comprehension**: RACE (46-58%), QuAC (44 F1)
- **Word-in-context**: WiC (49.4%, random chance)
- **Reversed words**: Near-zero performance

### Data Contamination

Analysis showed 75%+ of benchmarks were clean (no overlap with training data) and showed ~0% performance change on clean subsets. PIQA (29% flagged) and Winograd (45% flagged) showed 2-4% performance decreases on clean subsets. Wikipedia-based language modeling benchmarks were excluded due to contamination (Section 4).

---

## Conclusions

### Contributions

1. **Largest dense language model**: Trained GPT-3 with 175B parameters, 10x larger than previous non-sparse models, demonstrating continued scaling benefits (Section 2).

2. **In-context learning paradigm**: Established systematic framework for zero-shot, one-shot, and few-shot evaluation without gradient updates, showing competitive performance across diverse NLP tasks (Section 1, 3).

3. **Scaling behavior of in-context learning**: Demonstrated that few-shot performance increases more rapidly with scale than zero-shot, with larger models making more efficient use of contextual examples (Figures 1.2, 1.3).

4. **State-of-the-art results without fine-tuning**: Achieved SOTA on LAMBADA (86.4%), TriviaQA (71.2%), Penn Tree Bank perplexity (20.5), and near-SOTA on several SuperGLUE tasks (Section 3).

5. **Translation capabilities from English-dominant training**: GPT-3 outperforms unsupervised NMT by ~5 BLEU when translating into English despite being trained on only 7% non-English text (Section 3.3).

6. **Systematic contamination analysis**: Conducted and documented thorough analysis of data contamination effects, finding minimal impact on most benchmarks (Section 4).

7. **Bias documentation**: Provided preliminary analysis of gender, racial, and religious biases in the model's outputs (Section 6.2).

### Implications

1. **Task-agnostic NLP systems**: Very large language models may be an important ingredient in developing adaptable, general language systems that can perform diverse tasks without task-specific training data (Section 1).

2. **Meta-learning interpretation**: The gap between zero/one/few-shot performance growing with model size suggests larger models are more proficient meta-learners, not just memorizers (Section 3).

3. **Limits of pure self-supervision**: Pure self-supervised prediction will likely hit limits; augmentation with different approaches (RLHF, multimodal grounding) may be necessary for continued progress (Section 5). [Speculative implication, later confirmed by InstructGPT/ChatGPT development.]

4. **Practical deployment concerns**: Model scale creates inference cost challenges that may require distillation or other efficiency techniques for practical deployment (Section 5, 6.3).

---

## Key Claims

1. **C1: In-context learning improves with scale.** Figure 1.2 shows that "larger models make increasingly efficient use of in-context information." The gap between zero-shot and few-shot widens with model capacity across 42 benchmarks (Figure 1.3). Status: **supported**.

2. **C2: GPT-3 achieves SOTA on LAMBADA and TriviaQA in few-shot settings.** LAMBADA: 86.4% accuracy vs. prior SOTA of 68.0% (Table 3.1). TriviaQA: 71.2% vs. RAG's 68.0% (Table 3.3). Both without gradient updates. Status: **supported**.

3. **C3: Human-generated text detection approaches chance for GPT-3 175B.** Humans achieved only 52% accuracy distinguishing GPT-3-generated news articles from real ones, compared to 86% for a control model (Tables 3.11-3.12). Status: **supported**.

4. **C4: Data contamination minimally affects most benchmarks.** Analysis using 13-gram overlap found 75%+ of benchmarks were clean, with ~0% performance change on clean subsets. Exceptions: PIQA and Winograd showed 2-4% decreases (Section 4, Figure 4.2). Status: **supported**.

5. **C5: GPT-3 struggles with comparison tasks.** WiC achieves 49.4% (random chance level), ANLI achieves 34-40% (vs. SOTA 48-74%), demonstrating systematic difficulty with tasks requiring comparing text snippets (Section 3, 5). Status: **supported**.

---

## Open Questions

1. **Nature of in-context learning**: Does few-shot learning represent genuine task acquisition at inference time, or pattern recognition from training? The paper notes this is "ambiguous" and may vary task-by-task (Section 5). Partially addressed by Olsson et al. (2022) -- *In-context Learning and Induction Heads* -- which identifies induction heads as a mechanistic explanation.

2. **Limits of scaling**: Will continued scaling hit fundamental limits of the pretraining objective? When will augmentation with other approaches become necessary? Not directly addressed.

3. **Bidirectional models at scale**: Can bidirectional architectures achieve GPT-3's scale while maintaining few-shot learning abilities? Not directly addressed, though T5 represents a partial answer with encoder-decoder at 11B scale.

4. **Sample efficiency**: How can pre-training sample efficiency be improved to approach human levels? Not directly addressed.

5. **Grounding**: How can language models be grounded in physical world experience or other modalities? Partially addressed by multimodal models (GPT-4V, Gemini).

---

## Core References and Why They Are Referenced

### Architecture and Scaling

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that GPT-3 builds upon, using the decoder-only autoregressive variant.

- **Radford et al. (2019)** -- *Language Models are Unsupervised Multitask Learners (GPT-2).* Direct predecessor. GPT-3 uses identical architecture with modified initialization, pre-normalization, and reversible tokenization. Scaled from 1.5B to 175B parameters.

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Predicted smooth power-law improvement with compute. Guided GPT-3's model and data scaling decisions. GPT-3 extends these trends by two orders of magnitude.

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* GPT-3 uses alternating dense and locally banded sparse attention patterns from this work.

### Pre-training and Fine-tuning Baselines

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers.* Established bidirectional pre-training paradigm. GPT-3 deliberately omits bidirectionality to focus on autoregressive in-context learning. BERT-Large serves as fine-tuning baseline on SuperGLUE (69.0 average).

- **Liu et al. (2019)** -- *RoBERTa: A Robustly Optimized BERT Pretraining Approach.* Improved BERT pretraining. Serves as fine-tuning comparison baseline, representing ~50 petaflop/s-days of compute.

- **Raffel et al. (2019)** -- *Exploring the Limits of Transfer Learning with T5.* 11B parameter encoder-decoder model representing fine-tuned SOTA on many benchmarks. T5's closed-book QA results (36.6% NaturalQs, 50.1% TriviaQA) are beaten by GPT-3 few-shot.

### Meta-Learning

- **Vinyals et al. (2016)** -- *Matching Networks for One Shot Learning.* GPT-3's in-context learning relates to this meta-learning approach.

- **Duan et al. (2016)** -- *RL²: Fast Reinforcement Learning via Slow Reinforcement Learning.* GPT-3's approach of "stuffing context with examples" most resembles this meta-RL method.

### Evaluation Benchmarks

- **Wang et al. (2019)** -- *SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding.* Primary benchmark suite for evaluating GPT-3's language understanding capabilities.

- **Paperno et al. (2016)** -- *The LAMBADA Dataset.* Long-range dependency benchmark where GPT-3 achieves SOTA (86.4% vs. prior 68.0%).
