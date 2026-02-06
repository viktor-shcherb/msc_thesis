---
title: "Language Models are Unsupervised Multitask Learners"
authors: "Radford, Wu, Child, Luan, Amodei, Sutskever"
year: 2019
venue: "OpenAI Technical Report"
paper_type: informal
categories: ["architecture", "in-context-learning", "model-release"]
scope: ["zero-shot learning", "unsupervised multitask learning", "language model scaling"]
benchmarks_used: ["penn-treebank", "perplexity-wikitext2", "perplexity-wikitext103", "squad", "triviaqa", "swag", "winogrande"]
models_introduced: ["gpt-2"]
models_evaluated: []
key_claims:
  - id: C1
    claim: "Language models can perform zero-shot task transfer without any parameter or architecture modification"
    evidence: "Tables 1-4, Sections 3.1-3.8"
    status: supported
    scope: "Reading comprehension, summarization, translation, question answering"
    magnitude: "Competitive with supervised baselines on several tasks"
  - id: C2
    claim: "Model capacity is essential for zero-shot task transfer; larger models show consistent improvements"
    evidence: "Tables 1-4, Figure 4"
    status: supported
    scope: "117M to 1.5B parameters"
    magnitude: "Log-linear improvement with model size across most benchmarks"
  - id: C3
    claim: "A sufficiently large language model trained on diverse text can learn to perform tasks demonstrated in natural language sequences"
    evidence: "Section 2, Tables 1-4"
    status: supported
  - id: C4
    claim: "WebText-trained models achieve state-of-the-art zero-shot language modeling on multiple benchmarks"
    evidence: "Table 3: Penn Treebank 35.76 perplexity, WikiText-103 17.48 perplexity"
    status: supported
    scope: "Zero-shot evaluation only; no fine-tuning"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "GPT-2 uses decoder-only Transformer architecture with modified layer normalization placement"
  - target: 2019-07-transformer-xl
    type: concurrent
    detail: "Both address context length limitations in Transformers; Transformer-XL uses segment-level recurrence while GPT-2 uses larger fixed context"
  - target: 2023-02-llama-open-efficient-foundation
    type: extended-by
    detail: "LLaMA continues GPT-2's scaling approach with architectural improvements (RoPE, SwiGLU, RMSNorm)"
  - target: 2022-12-chinchilla-scaling-laws
    type: extended-by
    detail: "Chinchilla formalizes optimal compute allocation between parameters and tokens, revising implicit assumptions in GPT-2 scaling"
  - target: 2022-12-chain-of-thought-prompting
    type: extended-by
    detail: "Chain-of-thought prompting extends GPT-2's zero-shot paradigm by eliciting reasoning through prompting"
  - target: 2020-12-gpt-3-few-shot-learners
    type: extended-by
    detail: "GPT-3 scales GPT-2's architecture from 1.5B to 175B parameters, demonstrating that in-context learning improves dramatically with scale"
open_questions:
  - question: "What is the optimal ratio of parameters to training tokens for zero-shot transfer?"
    addressed_by: 2022-12-chinchilla-scaling-laws
  - question: "Can zero-shot performance approach supervised fine-tuning with sufficient scale?"
    addressed_by: null
  - question: "How does the training data distribution affect zero-shot generalization to specific domains?"
    addressed_by: null
---

# Language Models are Unsupervised Multitask Learners

**Authors:** Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever (OpenAI)
**Date:** February 2019
**Type:** Technical report (not peer-reviewed)
**URL:** https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

---

## Core Research Problem

Machine learning systems at the time of writing excelled at narrow tasks given large labeled datasets, but were brittle and sensitive to distribution shift. Multitask learning offered a path toward more general systems, but progress was limited by the need for explicit task-specific supervision and multi-task objectives. Prior work on language model pretraining (GPT-1, BERT, ELMo) showed that unsupervised learning on text followed by supervised fine-tuning could improve task performance, but still required task-specific datasets, architectures, or fine-tuning procedures.

The core question was: **can language modeling alone, without any task-specific training, produce systems capable of performing diverse tasks in a zero-shot manner?**

The paper hypothesizes that a language model trained on a sufficiently large and diverse corpus will begin to learn to perform tasks in order to better predict the next token, because many tasks can be expressed as sequences of natural language. If this hypothesis holds, language models should exhibit emergent zero-shot task transfer as a function of model capacity.

---

## Problem Solutions

GPT-2 addresses the problem by training a large Transformer language model on a diverse corpus of internet text (WebText) and evaluating zero-shot task transfer across a wide range of NLP benchmarks:

1. **Task conditioning through natural language.** Tasks are specified through natural language descriptions and examples embedded in the input context, rather than through separate task tokens, output heads, or fine-tuning. The model reads the task specification and input, then generates the output as a continuation.

2. **Diverse training data at scale.** WebText, a new dataset of 40GB of text from outbound links on Reddit with at least 3 karma, provides diverse task demonstrations implicitly embedded in naturally occurring text (news articles, fiction, code, conversations, Wikipedia, etc.).

3. **Increased model capacity.** Four model sizes (117M, 345M, 762M, 1.5B parameters) demonstrate that zero-shot task performance improves log-linearly with model size, suggesting that capacity is a key bottleneck for zero-shot transfer.

---

## Approach Details

### Method

GPT-2 is an autoregressive Transformer language model that models the probability of a sequence as the product of conditional next-token probabilities:

> p(x) = ∏ p(s_n | s_1, ..., s_{n-1})

The key methodological insight is that supervised tasks can be reframed as language modeling. A supervised task with inputs x and outputs y can be modeled as p(output | input, task), which can be expressed as a sequence: `(task description) (input) (output)`. For example:

- **Translation:** "(translate to french, english text, french text)"
- **Reading comprehension:** "(document, question, answer)"
- **Summarization:** "(article, TL;DR:, summary)"

The model learns to perform tasks implicitly by predicting what comes next in naturally occurring text that contains task demonstrations.

### Key Technical Components

#### Architecture

GPT-2 uses a decoder-only Transformer with the following modifications from GPT-1:

- **Layer normalization placement:** Moved to the input of each sub-block (attention, FFN), similar to a pre-activation residual network. An additional layer normalization is added after the final self-attention block.
- **Modified initialization:** Residual layer weights are scaled by 1/√N at initialization, where N is the number of residual layers. This improves training stability.
- **Context length:** Increased from 512 to 1024 tokens.
- **Vocabulary size:** Byte-level BPE with 50,257 tokens (GPT-1 used word-level BPE with 40,000 merges).
- **Batch size:** 512 sequences.

#### Model Configurations

| Model | Layers | d_model | Heads | Parameters |
|---|---|---|---|---|
| GPT-2 Small | 12 | 768 | 12 | 117M |
| GPT-2 Medium | 24 | 1024 | 16 | 345M |
| GPT-2 Large | 36 | 1280 | 20 | 762M |
| GPT-2 XL | 48 | 1600 | 25 | 1.5B |

Head dimension is d_model / n_heads = 64 for all models.

#### Training Data: WebText

WebText is constructed by scraping all outbound links from Reddit that received at least 3 karma (a heuristic for quality filtering based on community curation). The resulting dataset:

- 45 million links after filtering
- 40 GB of text after deduplication and cleaning
- ~8 million documents
- Wikipedia is excluded to prevent contamination of test sets

This approach differs from prior work (CommonCrawl, etc.) by using human curation signals rather than classifier-based filtering.

#### Byte-Level BPE

Rather than word-level or Unicode code point BPE, GPT-2 uses byte-level BPE:

- Input text is encoded as UTF-8 bytes
- BPE operates on byte sequences rather than characters
- This allows the model to assign a probability to any Unicode string
- Vocabulary of 50,257 tokens after 50,000 merges + 256 byte tokens + end-of-text token

To prevent BPE from merging across character categories (which creates fragmented tokens), merging is prevented across character class boundaries (letters, digits, punctuation).

### Experimental Setup

Zero-shot evaluation is performed by conditioning the model on a natural language prompt and measuring performance on the task without any gradient updates.

**Reading comprehension (CoQA):** The model is given a document, conversation history, and a final question, then generates an answer. Greedy decoding is used.

**Summarization (CNN/Daily Mail):** The article is followed by "TL;DR:" and the model generates a summary.

**Translation (WMT'14 En-Fr):** The model is prompted with example translation pairs followed by the test sentence and "=" to elicit translation.

**Question answering (Natural Questions):** The model is given an example Q&A pair followed by the test question.

**Language modeling:** Standard perplexity evaluation on Penn Treebank, WikiText-2, WikiText-103, enwik8, text8, LAMBADA, and Children's Book Test.

### Key Results

#### Language Modeling (Zero-Shot)

| Dataset | GPT-2 1.5B | Previous SOTA | SOTA Method |
|---|---|---|---|
| Penn Treebank | 35.76 | 46.54 | LSTM + Neural Cache |
| WikiText-2 | 18.34 | 39.14 | LSTM + Neural Cache |
| WikiText-103 | 17.48 | 18.3 | Transformer-XL |
| enwik8 (bpc) | 0.93 | 0.99 | Transformer-XL |
| text8 (bpc) | 0.98 | 1.08 | Transformer-XL |
| LAMBADA (acc.) | 63.24% | 59.23% | LSTM + Gated Attention |
| LAMBADA (ppl.) | 8.63 | 99.8 | LSTM + Gated Attention |

GPT-2 achieves state-of-the-art zero-shot perplexity on 7 of 8 language modeling benchmarks (Table 3). On LAMBADA, zero-shot GPT-2 improves accuracy from 59.23% to 63.24% and reduces perplexity from 99.8 to 8.63.

#### Children's Book Test (Zero-Shot Accuracy)

| Model | Common Nouns | Named Entities |
|---|---|---|
| Human | 81.6 | 81.6 |
| LSTM + Attention | 69.2 | 72.0 |
| GPT-2 1.5B | 89.05 | 89.05 |

GPT-2 achieves new SOTA and exceeds human performance on CBT (Table 4).

#### Reading Comprehension (CoQA, Zero-Shot F1)

| Model | F1 |
|---|---|
| GPT-2 1.5B | 55 |
| BERT Large (supervised) | 89 |
| Human | 90 |

Zero-shot GPT-2 achieves 55 F1 without any fine-tuning, demonstrating emergent reading comprehension capability (Section 3.6).

#### Summarization (CNN/Daily Mail, Zero-Shot ROUGE)

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---|---|---|
| GPT-2 1.5B (TL;DR:) | 29.34 | 8.27 | 26.58 |
| GPT-2 1.5B (No hint) | 21.58 | 4.03 | 19.47 |
| Supervised Neural | 39.53 | 17.28 | 36.38 |

Zero-shot summarization is possible but lags significantly behind supervised methods. The "TL;DR:" prompt is critical; without it, performance drops substantially (Table 5).

#### Translation (WMT'14 En-Fr, Zero-Shot BLEU)

| Model | En→Fr | Fr→En |
|---|---|---|
| GPT-2 1.5B | 5.0 | 11.5 |
| Supervised SOTA | 45.6 | -- |

Zero-shot translation is weak (5.0 BLEU En→Fr) but not random. Performance is asymmetric: Fr→En (11.5 BLEU) is better than En→Fr (5.0 BLEU), likely reflecting the English-heavy training data (Section 3.5).

#### Winograd Schema Challenge (Zero-Shot Accuracy)

| Model | Partial | Full |
|---|---|---|
| GPT-2 1.5B | 70.70 | 63.0 |
| Previous SOTA | 63.0 | -- |

GPT-2 increases accuracy on the partial scoring version from 63% to 70.7% (Section 3.7).

#### Scaling Behavior

Performance on all benchmarks improves log-linearly with model size. On language modeling, even the largest model has not saturated, suggesting that further scaling would continue to improve zero-shot performance (Figure 4). The authors explicitly note: "GPT-2 is still quite far from human performance on many tasks."

---

## Limitations and Failure Modes

- **Summarization quality.** Zero-shot summaries "often focus on recent content from the article or confuse specific details such as how many cars were involved in a crash" (Section 3.3). The model struggles to identify key information.

- **Translation.** Zero-shot translation achieves only 5.0 BLEU on En→Fr, far below supervised systems (45.6 BLEU). The model is not a practical translation system without fine-tuning (Section 3.5).

- **Reading comprehension.** 55 F1 on CoQA is well below supervised models (89 F1) and human performance (90 F1) (Section 3.6).

- **Question answering.** On Natural Questions, GPT-2 correctly answers only 4.1% of questions, far below the 30-50% range of systems using retrieval (Section 3.4).

- **Repetition and incoherence.** Text generation exhibits repetition, especially for longer outputs. The model sometimes loses coherence or switches topics unexpectedly.

- **Training data bias.** WebText is biased toward content from Reddit's population and interests. This may affect the distribution of implicit task demonstrations.

- **Fixed context length.** The 1024-token context limits the model's ability to handle long documents or multi-turn conversations.

- **No mechanism for factual grounding.** The model generates plausible-sounding but potentially incorrect facts. "We have observed various failure modes such as repetitive text, world modeling failures... text which switches topics suddenly, and unnatural topic transitions" (Section 6).

---

## Conclusions

### Contributions

1. **Zero-shot task transfer paradigm.** Demonstrated that language models can perform tasks without task-specific training by conditioning on natural language descriptions. This established the zero-shot evaluation paradigm that became standard practice (Tables 1-5).

2. **Scaling improves zero-shot performance.** Showed that larger models exhibit better zero-shot transfer across all evaluated tasks, with log-linear improvements from 117M to 1.5B parameters. This motivated subsequent scaling efforts (GPT-3, Chinchilla, LLaMA) (Figure 4).

3. **WebText dataset.** Introduced a methodology for curating training data using social curation signals (Reddit karma) rather than classifier-based filtering. This approach influenced subsequent dataset construction efforts (Section 2.1).

4. **Byte-level BPE.** Demonstrated that byte-level tokenization works well for language modeling, enabling open-vocabulary modeling without unknown tokens. This became widely adopted (Section 2.2).

5. **State-of-the-art zero-shot language modeling.** Achieved SOTA perplexity on 7 of 8 language modeling benchmarks without any domain adaptation, demonstrating the generalization capability of large-scale pretraining (Table 3).

### Implications

1. **Language modeling as a proxy for general intelligence.** The paper argues that "language models are unsupervised multitask learners" -- that predicting the next token implicitly requires learning to perform many tasks. This framing influenced the field's subsequent focus on scaling language models as a path to general AI capabilities. [Central thesis of the paper.]

2. **Compute scaling as a research direction.** The consistent improvement from 117M to 1.5B parameters, with no saturation observed, suggested that continued scaling would yield further capability gains. This motivated the scaling agenda that produced GPT-3, Chinchilla, and LLaMA. [Speculative implication validated by subsequent work.]

3. **Prompt engineering as an alternative to fine-tuning.** By demonstrating that task performance can be elicited through natural language prompts, the paper opened the research direction of prompt engineering, which became essential for leveraging large language models without fine-tuning. [Implication subsequently validated.]

---

## Key Claims

1. **C1: Zero-shot task transfer without parameter modification.** GPT-2 performs translation, summarization, reading comprehension, and question answering by conditioning on natural language prompts, with no fine-tuning, task-specific heads, or architecture changes. Evidence: Tables 1-5, Sections 3.1-3.8. Status: **supported**. Scope: Performance varies widely by task; translation and QA remain weak.

2. **C2: Capacity is essential for zero-shot transfer.** Performance improves log-linearly with model size across all evaluated benchmarks. Even at 1.5B parameters, performance has not saturated on most tasks. Evidence: Figure 4, Tables 1-4. Status: **supported**. Magnitude: Consistent improvement across 10x parameter increase.

3. **C3: Language modeling implicitly learns diverse tasks.** A language model trained only to predict the next token can learn to perform tasks that are demonstrated in natural language sequences, without explicit task supervision. Evidence: Section 2, empirical results in Tables 1-5. Status: **supported**. This is the central hypothesis of the paper.

4. **C4: WebText models achieve SOTA zero-shot language modeling.** GPT-2 achieves the best perplexity on 7 of 8 language modeling benchmarks in zero-shot evaluation. Evidence: Table 3. Status: **supported**. Scope: Zero-shot only; fine-tuned models or those with adaptive mechanisms (e.g., Transformer-XL with memory) may perform better.

---

## Open Questions

1. **What is the optimal ratio of parameters to training tokens?** GPT-2 trains on ~40GB of text for models up to 1.5B parameters. Whether this ratio is optimal, or whether smaller models trained on more data could achieve similar performance, was not explored. Subsequently addressed by Chinchilla (Hoffmann et al., 2022).

2. **Can zero-shot performance approach supervised fine-tuning with sufficient scale?** GPT-2 shows a large gap between zero-shot and supervised performance on most tasks (e.g., 55 vs 89 F1 on CoQA). Whether scaling alone can close this gap remains an open question. Partially addressed by GPT-3, which showed few-shot can approach fine-tuning on some tasks.

3. **How does training data composition affect zero-shot generalization?** WebText is dominated by certain domains (news, discussion, Wikipedia-linked content). How this affects zero-shot performance on specialized domains (legal, medical, scientific) is not explored.

4. **What are the limits of zero-shot reasoning?** GPT-2 shows emergent zero-shot capabilities but struggles with multi-step reasoning, factual consistency, and tasks requiring world knowledge. What architectural or training modifications could address these limitations?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that GPT-2 builds upon. GPT-2 uses a decoder-only variant with modified layer normalization placement.

- **Radford et al. (2018)** -- *Improving Language Understanding by Generative Pre-Training (GPT-1).* The direct predecessor to GPT-2. GPT-2 scales up the GPT-1 architecture (12→48 layers, 117M→1.5B parameters) and shifts from fine-tuning to zero-shot evaluation.

### Language Model Scaling

- **Jozefowicz et al. (2016)** -- *Exploring the Limits of Language Modeling.* Large-scale LSTM language modeling that GPT-2 surpasses. Demonstrated that scale improves language modeling performance.

- **Merity et al. (2018)** -- *An Analysis of Neural Language Modeling at Multiple Scales.* LSTM language modeling baselines that GPT-2 compares against on Penn Treebank and WikiText.

### Tokenization

- **Sennrich et al. (2016)** -- *Neural Machine Translation of Rare Words with Subword Units.* Introduced BPE for NMT. GPT-2 extends this to byte-level BPE for open-vocabulary modeling.

### Transfer Learning

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers.* Contemporary work on pretraining. BERT uses bidirectional attention and supervised fine-tuning; GPT-2 uses unidirectional attention and zero-shot evaluation.

- **Howard & Ruder (2018)** -- *Universal Language Model Fine-tuning (ULMFiT).* Prior work on language model pretraining for transfer learning that GPT-2 extends.

### Evaluation Benchmarks

- **Paperno et al. (2016)** -- *The LAMBADA Dataset.* The LAMBADA benchmark where GPT-2 achieves substantial zero-shot improvements (99.8→8.63 perplexity).

- **Hill et al. (2016)** -- *The Goldilocks Principle: Reading Children's Books with Explicit Memory Representations.* The Children's Book Test benchmark where GPT-2 exceeds human performance.

- **Levesque et al. (2012)** -- *The Winograd Schema Challenge.* Commonsense reasoning benchmark where GPT-2 improves from 63% to 70.7%.
