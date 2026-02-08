---
title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
authors: "Devlin, Chang, Lee, Toutanova"
year: 2019
venue: "NAACL 2019"
paper_type: conference-paper
categories: ["architecture", "model-release"]
scope: ["bidirectional pre-training", "language understanding", "fine-tuning", "English"]
benchmarks_used: ["glue", "squad", "swag"]
models_introduced: ["bert-base", "bert-large"]
models_evaluated: []
key_claims:
  - id: C1
    claim: "BERT_LARGE achieves a GLUE score of 80.5%, a 7.7 point absolute improvement over prior state of the art"
    evidence: "Table 1, Section 4.1"
    status: supported
    scope: "8 GLUE tasks (WNLI excluded), English, single-model single-task"
    magnitude: "+7.7 points over prior SOTA (72.8), +7.0 average accuracy over OpenAI GPT"
  - id: C2
    claim: "Bidirectional pre-training via MLM is critical: replacing MLM with left-to-right LM drops MNLI-m from 84.4 to 82.1 and SQuAD F1 from 88.5 to 77.8"
    evidence: "Table 5, Section 5.1"
    status: supported
    scope: "BERT_BASE architecture, same pre-training data and fine-tuning scheme"
    magnitude: "-2.3 MNLI-m, -9.2 MRPC, -10.7 SQuAD F1"
  - id: C3
    claim: "Next sentence prediction pre-training benefits QNLI (+3.5 points), MNLI (+0.5), and SQuAD F1 (+0.6)"
    evidence: "Table 5, Section 5.1"
    status: supported
    scope: "BERT_BASE architecture, MLM kept in both conditions"
    magnitude: "+3.5 QNLI, +0.5 MNLI-m, +0.6 SQuAD F1"
  - id: C4
    claim: "BERT_LARGE ensemble achieves SQuAD v1.1 Test F1 of 93.2, surpassing the top leaderboard system by +1.5 F1"
    evidence: "Table 2, Section 4.2"
    status: supported
    scope: "7-system ensemble with TriviaQA data augmentation"
    magnitude: "+1.5 F1 over top leaderboard system (91.7)"
  - id: C5
    claim: "BERT_LARGE achieves SQuAD v2.0 Test F1 of 83.1, a +5.1 F1 improvement over the previous best system"
    evidence: "Table 3, Section 4.3"
    status: supported
    scope: "Single model, no TriviaQA augmentation"
    magnitude: "+5.1 F1 over MIR-MRC (78.0)"
  - id: C6
    claim: "Larger pre-trained models lead to strict accuracy improvements across all tasks, even MRPC with only 3,600 training examples"
    evidence: "Table 6, Section 5.2"
    status: supported
    scope: "3 to 24 layers, 768 to 1024 hidden, MNLI/MRPC/SST-2, 5 random restarts"
    magnitude: "+8.7 MNLI-m (77.9 to 86.6), +8.0 MRPC (79.8 to 87.8), +5.3 SST-2 (88.4 to 93.7)"
  - id: C7
    claim: "Feature-based BERT (concat last 4 hidden layers) achieves 96.1 Dev F1 on CoNLL-2003 NER, only 0.3 F1 behind fine-tuning"
    evidence: "Table 7, Section 5.3"
    status: supported
    scope: "CoNLL-2003 NER, BERT_BASE, two-layer 768-dim BiLSTM classifier, 5 random restarts"
    magnitude: "96.1 vs. 96.4 Dev F1 (0.3 gap)"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "BERT uses the Transformer encoder architecture with bidirectional self-attention for pre-training"
  - target: 2019-08-bert-attention-analysis
    type: extended-by
    detail: "Clark et al. analyze what linguistic knowledge is captured in BERT's attention heads, finding syntactic specialization"
  - target: 2019-11-dark-secrets-of-bert
    type: extended-by
    detail: "Kovaleva et al. characterize five recurring self-attention patterns in BERT across GLUE tasks"
  - target: 2019-12-sixteen-heads-better-than-one
    type: extended-by
    detail: "Michel et al. demonstrate that many of BERT's attention heads can be pruned with minimal performance loss"
  - target: 2020-04-longformer-long-document-transformer
    type: extended-by
    detail: "Longformer extends BERT-style pre-training to long documents (4,096 tokens) using sparse local+global attention"
  - target: 2020-07-quantifying-attention-flow
    type: extended-by
    detail: "Abnar and Zuidema propose attention rollout and flow to trace information propagation through BERT's layers"
open_questions:
  - question: "Can bidirectional pre-training be effectively extended to autoregressive generation tasks?"
    addressed_by: null
  - question: "Is next sentence prediction truly necessary, or can MLM alone suffice for strong downstream performance?"
    addressed_by: null
  - question: "How to handle sequences longer than BERT's 512-token limit while preserving pre-trained representations?"
    addressed_by: 2020-04-longformer-long-document-transformer
  - question: "Does the pre-train/fine-tune mismatch from [MASK] tokens meaningfully limit downstream performance?"
    addressed_by: null
---

# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

**Authors:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova (Google AI Language)
**Date:** June 2019, NAACL 2019; arXiv:1810.04805

---

## Core Research Problem

Language model pre-training had been shown effective for improving NLP tasks (Dai and Le, 2015; Peters et al., 2018; Howard and Ruder, 2018; Radford et al., 2018), but existing approaches were constrained by **unidirectional architectures**. Two paradigms existed: *feature-based* approaches like ELMo (Peters et al., 2018a), which extract context-sensitive features from a shallow concatenation of independently trained left-to-right and right-to-left LSTMs, and *fine-tuning* approaches like OpenAI GPT (Radford et al., 2018), which use a left-to-right Transformer where every token can only attend to previous tokens in the self-attention layers.

The fundamental limitation is that standard conditional language models can only be trained left-to-right *or* right-to-left, since bidirectional conditioning would allow each word to indirectly "see itself" in a multi-layered context (Section 3.1). This unidirectionality "limits the choice of architectures that can be used during pre-training" and is "sub-optimal for sentence-level tasks, and could be very harmful when applying fine-tuning based approaches to token-level tasks such as question answering, where it is crucial to incorporate context from both directions" (Section 1). ELMo's concatenation of independently trained left-to-right and right-to-left representations is a workaround but is (a) twice as expensive, (b) non-intuitive for tasks like QA where the right-to-left model cannot condition answers on questions, and (c) strictly less powerful than a deeply bidirectional model that uses both left and right context at every layer (Section 5.1).

The core challenge is: **how to pre-train deep bidirectional representations from unlabeled text that can be fine-tuned with minimal task-specific modifications for a broad range of NLP tasks.**

---

## Problem Solutions

BERT (Bidirectional Encoder Representations from Transformers) proposes two innovations to enable deep bidirectional pre-training:

1. **Masked language model (MLM) pre-training:** Instead of predicting the next token left-to-right, BERT randomly masks 15% of input tokens and trains the model to predict the original vocabulary ID of masked tokens from their bidirectional context. This is inspired by the Cloze task (Taylor, 1953) and avoids the "see itself" problem because masked tokens are replaced before being fed to the model.

2. **Next sentence prediction (NSP) pre-training:** A binary classification task where the model predicts whether two text spans are consecutive in the original corpus (50% IsNext, 50% NotNext), training the model to understand inter-sentence relationships.

3. **Unified fine-tuning architecture:** The same pre-trained model is fine-tuned for diverse downstream tasks (classification, question answering, sequence tagging) by adding a single output layer and fine-tuning all parameters end-to-end. This contrasts with feature-based approaches that require task-specific architectures.

---

## Approach Details

### Method

BERT's model architecture is a multi-layer bidirectional Transformer encoder based on Vaswani et al. (2017). The paper reports results on two model sizes:

- **BERT_BASE:** L=12, H=768, A=12, feed-forward size=3072, Total Parameters=110M
- **BERT_LARGE:** L=24, H=1024, A=16, feed-forward size=4096, Total Parameters=340M

where L is the number of layers (Transformer blocks), H is the hidden size, and A is the number of self-attention heads. The feed-forward size is always 4H (Section 3, footnote 3). BERT_BASE was chosen to have the same model size as OpenAI GPT for comparison (Section 3).

**Input representation:** For a given token, its input representation is the sum of three embeddings (Figure 2):

> E_input = E_token + E_segment + E_position

- **Token embeddings:** WordPiece embeddings (Wu et al., 2016) with a 30,000 token vocabulary.
- **Segment embeddings:** A learned embedding indicating whether a token belongs to sentence A or sentence B.
- **Position embeddings:** Learned positional embeddings (up to 512 positions).

Every input sequence begins with a special [CLS] token whose final hidden state C serves as the aggregate sequence representation for classification. Sentence pairs are separated by a [SEP] token. A "sentence" in BERT can be any contiguous span of text, not necessarily a linguistic sentence (Section 3).

### Key Technical Components

#### Masked Language Model (Section 3.1)

15% of all WordPiece tokens in each input sequence are selected for prediction. To mitigate the mismatch between pre-training (which uses [MASK] tokens) and fine-tuning (which does not), the selected tokens are not always replaced with [MASK]:

- **80% of the time:** Replace with [MASK] token.
- **10% of the time:** Replace with a random token from the vocabulary.
- **10% of the time:** Keep the original token unchanged.

The final hidden vector T_i corresponding to the selected token is fed into an output softmax over the vocabulary to predict the original token with cross-entropy loss. Because only 15% of tokens are predicted per batch (vs. 100% in standard LM training), MLM converges marginally slower than left-to-right pre-training, but "the empirical improvements of the MLM model far outweigh the increased training cost" (Appendix C.1, Figure 5).

#### Next Sentence Prediction (Section 3.1)

For each pre-training example, two spans A and B are sampled from the corpus. 50% of the time B is the actual next sentence following A (IsNext), and 50% of the time B is a random sentence (NotNext). The [CLS] representation C is used to classify IsNext vs. NotNext. The final model achieves 97-98% accuracy on NSP (Section 3.1, footnote 5).

#### Fine-tuning Procedure (Section 3.2)

BERT's self-attention mechanism unifies sentence-pair encoding and cross-attention into a single model: encoding a concatenated text pair with bidirectional self-attention effectively includes bidirectional cross-attention between the two sentences. For each downstream task:

- **Classification tasks** (MNLI, SST-2, etc.): The [CLS] representation C is fed into a classification layer W, computing log(softmax(CW^T)).
- **Question answering** (SQuAD): A start vector S and end vector E are learned. The probability of word i being the start of the answer span is:

> P_i = exp(S * T_i) / sum_j exp(S * T_j)

  The candidate span score from position i to j is:

> score(i, j) = S * T_i + E * T_j

- **Sequence tagging** (NER): Token representations T_i are fed into a token-level classifier.

### Experimental Setup

**Pre-training data:** BooksCorpus (800M words; Zhu et al., 2015) + English Wikipedia text passages (2,500M words), totaling approximately 3.3 billion words. Document-level corpus (not shuffled sentences) to enable extraction of long contiguous sequences (Section 3.1).

**Pre-training procedure (Appendix A.2):**
- Batch size: 256 sequences x 512 tokens = 128,000 tokens/batch.
- Steps: 1,000,000 (~40 epochs over the corpus).
- Optimizer: Adam with lr=1e-4, beta_1=0.9, beta_2=0.999, L2 weight decay=0.01.
- Learning rate schedule: linear warmup over first 10,000 steps, then linear decay.
- Dropout: 0.1 on all layers.
- Activation: GELU (Hendrycks and Gimpel, 2016) instead of ReLU.
- Loss: sum of mean masked LM likelihood and mean NSP likelihood.
- Hardware: BERT_BASE on 4 Cloud TPUs (16 TPU chips), BERT_LARGE on 16 Cloud TPUs (64 TPU chips). Each pre-training took 4 days.
- Sequence length: 128 for 90% of steps, then 512 for remaining 10% to learn positional embeddings (Appendix A.2).

**Fine-tuning procedure (Appendix A.3):**
- Batch size: 16 or 32.
- Learning rate: selected from {5e-5, 4e-5, 3e-5, 2e-5}.
- Epochs: 2, 3, or 4.
- Dropout: 0.1.
- All results reproducible in at most 1 hour on a single Cloud TPU (Section 3.2, footnote 7).
- For BERT_LARGE on small datasets, multiple random restarts with the same pre-trained checkpoint but different fine-tuning data shuffling and classifier layer initialization (Section 4.1).

### Key Results

#### GLUE (Table 1, Section 4.1)

GLUE test results scored by the evaluation server. BERT and OpenAI GPT are single-model, single-task. F1 for QQP and MRPC, Spearman for STS-B, accuracy for other tasks.

| System | MNLI-m/mm | QQP | QNLI | SST-2 | CoLA | STS-B | MRPC | RTE | Average |
|---|---|---|---|---|---|---|---|---|---|
| Pre-OpenAI SOTA | 80.6/80.1 | 66.1 | 82.3 | 93.2 | 35.0 | 81.0 | 86.0 | 61.7 | 74.0 |
| BiLSTM+ELMo+Attn | 76.4/76.1 | 64.8 | 79.8 | 90.4 | 36.0 | 73.3 | 84.9 | 56.8 | 71.0 |
| OpenAI GPT | 82.1/81.4 | 70.3 | 87.4 | 91.3 | 45.4 | 80.0 | 82.3 | 56.0 | 75.1 |
| BERT_BASE | 84.6/83.4 | 71.2 | 90.5 | 93.5 | 52.1 | 85.8 | 88.9 | 66.4 | 79.6 |
| **BERT_LARGE** | **86.7/85.9** | **72.1** | **92.7** | **94.9** | **60.5** | **86.5** | **89.3** | **70.1** | **82.1** |

- BERT_BASE and BERT_LARGE outperform all prior systems on all 8 tasks (Section 4.1).
- BERT_BASE obtains 4.5% and BERT_LARGE obtains 7.0% average accuracy improvement over OpenAI GPT (Section 4.1).
- On the official GLUE leaderboard, BERT_LARGE obtains 80.5, compared to OpenAI GPT at 72.8 (Section 4.1). The "Average" column in the table (82.1) differs from the official GLUE score because it excludes WNLI.
- BERT_LARGE significantly outperforms BERT_BASE across all tasks, especially those with very little training data (Section 4.1).

#### SQuAD v1.1 (Table 2, Section 4.2)

| System | Dev EM | Dev F1 | Test EM | Test F1 |
|---|---|---|---|---|
| Human | -- | -- | 82.3 | 91.2 |
| #1 Ensemble - nlnet | -- | -- | 86.0 | 91.7 |
| BiDAF+ELMo (Single) | -- | 85.6 | -- | 85.8 |
| R.M. Reader (Ensemble) | 81.2 | 87.9 | 82.3 | 88.5 |
| BERT_BASE (Single) | 80.8 | 88.5 | -- | -- |
| BERT_LARGE (Single) | 84.1 | 90.9 | -- | -- |
| BERT_LARGE (Sgl.+TriviaQA) | 84.2 | 91.1 | 85.1 | 91.8 |
| **BERT_LARGE (Ens.+TriviaQA)** | **86.2** | **92.2** | **87.4** | **93.2** |

- The single BERT_LARGE model (90.9 Dev F1) outperforms the top leaderboard ensemble system (91.7 Test F1) in terms of F1 (Section 4.2).
- With TriviaQA data augmentation, the BERT_LARGE ensemble achieves 93.2 Test F1, surpassing the top leaderboard system by +1.5 F1 (Section 4.2).
- Without TriviaQA fine-tuning data, BERT_LARGE still achieves 90.9 Dev F1, only 0.1-0.4 F1 below the TriviaQA-augmented version (Section 4.2).

#### SQuAD v2.0 (Table 3, Section 4.3)

| System | Dev EM | Dev F1 | Test EM | Test F1 |
|---|---|---|---|---|
| Human | 86.3 | 89.0 | 86.9 | 89.5 |
| #1 Single - MIR-MRC | -- | -- | 74.8 | 78.0 |
| unet (Ensemble) | -- | -- | 71.4 | 74.9 |
| **BERT_LARGE (Single)** | **78.7** | **81.9** | **80.0** | **83.1** |

- BERT_LARGE achieves +5.1 F1 improvement over the previous best system (78.0 F1) (Section 4.3).
- The approach is simple: questions without answers are treated as having an answer span at the [CLS] token. A no-answer score is compared to the best non-null span score:

> s_null = S * C + E * C
>
> s_hat_{i,j} = max_{j >= i} S * T_i + E * T_j

  A non-null answer is predicted when s_hat_{i,j} > s_null + tau, where threshold tau is selected on the dev set to maximize F1. Fine-tuned for 2 epochs with lr=5e-5 and batch size 48 (Section 4.3).

#### SWAG (Table 4, Section 4.4)

| System | Dev | Test |
|---|---|---|
| ESIM+GloVe | 51.9 | 52.7 |
| ESIM+ELMo | 59.1 | 59.2 |
| OpenAI GPT | -- | 78.0 |
| BERT_BASE | 81.6 | -- |
| **BERT_LARGE** | **86.6** | **86.3** |
| Human (expert) | -- | 85.0 |
| Human (5 annotations) | -- | 88.0 |

- BERT_LARGE outperforms OpenAI GPT by +8.3% and ESIM+ELMo by +27.1% (Section 4.4).
- BERT_LARGE (86.3) surpasses expert human performance (85.0) but falls short of 5-annotation human performance (88.0) (Table 4).
- Fine-tuned for 3 epochs with lr=2e-5 and batch size 16. Each of the four choices is encoded as a separate sequence with the given sentence, scored by a dot product with the [CLS] representation and normalized via softmax (Section 4.4).

#### Ablation: Effect of Pre-training Tasks (Table 5, Section 5.1)

Dev set results using the BERT_BASE architecture with different pre-training configurations:

| Configuration | MNLI-m (Acc) | QNLI (Acc) | MRPC (Acc) | SST-2 (Acc) | SQuAD (F1) |
|---|---|---|---|---|---|
| **BERT_BASE** | **84.4** | **88.4** | **86.7** | **92.7** | **88.5** |
| No NSP | 83.9 | 84.9 | 86.5 | 92.6 | 87.9 |
| LTR & No NSP | 82.1 | 84.3 | 77.5 | 92.1 | 77.8 |
| + BiLSTM | 82.1 | 84.1 | 75.7 | 91.6 | 84.9 |

- Removing NSP hurts QNLI by 3.5 points, MNLI by 0.5, and SQuAD by 0.6 (Table 5).
- Replacing MLM with left-to-right LM (LTR & No NSP, comparable to OpenAI GPT) causes large drops: MRPC falls by 9.2 points (86.7 to 77.5) and SQuAD F1 by 10.7 points (88.5 to 77.8) (Table 5).
- Adding a randomly initialized BiLSTM on top of the LTR model improves SQuAD F1 from 77.8 to 84.9 but still falls far short of bidirectional MLM pre-training (88.5). The BiLSTM hurts GLUE task performance (Table 5).

#### Ablation: Effect of Model Size (Table 6, Section 5.2)

Dev set accuracy averaged over 5 random restarts of fine-tuning:

| #L | #H | #A | LM (ppl) | MNLI-m | MRPC | SST-2 |
|---|---|---|---|---|---|---|
| 3 | 768 | 12 | 5.84 | 77.9 | 79.8 | 88.4 |
| 6 | 768 | 3 | 5.24 | 80.6 | 82.2 | 90.7 |
| 6 | 768 | 12 | 4.68 | 81.9 | 84.8 | 91.3 |
| 12 | 768 | 12 | 3.99 | 84.4 | 86.7 | 92.9 |
| 12 | 1024 | 16 | 3.54 | 85.7 | 86.9 | 93.3 |
| 24 | 1024 | 16 | 3.23 | 86.6 | 87.8 | 93.7 |

- Larger models yield strict accuracy improvements on all four datasets, including MRPC with only 3,600 labeled training examples (Section 5.2).
- Prior work (Peters et al., 2018b; Melamud et al., 2016) showed mixed results from scaling feature-based pre-trained models. The paper hypothesizes that fine-tuning allows task-specific models to benefit from larger representations even with very small downstream data (Section 5.2).

#### Feature-based Approach (Table 7, Section 5.3)

CoNLL-2003 Named Entity Recognition results, averaged over 5 random restarts:

| System | Dev F1 | Test F1 |
|---|---|---|
| ELMo (Peters et al., 2018a) | 95.7 | 92.2 |
| CVT (Clark et al., 2018) | -- | 92.6 |
| CSE (Akbik et al., 2018) | -- | **93.1** |
| BERT_LARGE (fine-tuning) | **96.6** | 92.8 |
| BERT_BASE (fine-tuning) | 96.4 | 92.4 |
| Concat Last Four Hidden (feature-based) | 96.1 | -- |
| Weighted Sum Last Four Hidden | 95.9 | -- |
| Second-to-Last Hidden | 95.6 | -- |
| Weighted Sum All 12 Layers | 95.5 | -- |
| Last Hidden | 94.9 | -- |
| Embeddings only | 91.0 | -- |

- The best feature-based method (concatenating the top 4 hidden layers) achieves 96.1 Dev F1, only 0.3 F1 behind fine-tuning the entire model (96.4 for BERT_BASE) (Table 7, Section 5.3).
- Feature-based BERT uses a randomly initialized two-layer 768-dimensional BiLSTM over fixed contextual embeddings (Section 5.3).

#### Masking Strategy Ablation (Table 8, Appendix C.2)

| MASK | SAME | RND | MNLI (Fine-tune) | NER (Fine-tune) | NER (Feature-based) |
|---|---|---|---|---|---|
| 80% | 10% | 10% | 84.2 | 95.4 | 94.9 |
| 100% | 0% | 0% | 84.3 | 94.9 | 94.0 |
| 80% | 0% | 20% | 84.1 | 95.2 | 94.6 |
| 80% | 20% | 0% | 84.4 | 95.2 | 94.7 |
| 0% | 20% | 80% | 83.7 | 94.8 | 94.6 |
| 0% | 0% | 100% | 83.6 | 94.9 | 94.6 |

- Fine-tuning is surprisingly robust to different masking strategies (Appendix C.2).
- Using only [MASK] (100%/0%/0%) is problematic for the feature-based approach on NER (94.0 vs. 94.9 with the default strategy), because the model never learns to represent non-masked tokens during pre-training (Appendix C.2).

---

## Limitations and Failure Modes

1. **Pre-train/fine-tune mismatch from [MASK] tokens.** The [MASK] token appears during pre-training but never during fine-tuning. The 80/10/10 masking strategy mitigates this, but the mismatch remains a fundamental design tension (Section 3.1). The ablation in Table 8 shows the feature-based approach is more sensitive to this mismatch than fine-tuning.

2. **MLM predicts only 15% of tokens per batch.** Compared to standard left-to-right language model training (which predicts 100% of tokens), MLM converges marginally slower, "which suggests that more pre-training steps may be required for the model to converge" (Appendix A.1, C.1). The paper shows BERT_BASE gains ~1.0% additional MNLI accuracy when trained for 1M steps vs. 500K steps (Figure 5).

3. **Maximum sequence length of 512 tokens.** BERT's learned positional embeddings support at most 512 positions. To speed up pre-training, 90% of steps use sequence length 128 (Appendix A.2). This hard limit excludes long-document tasks.

4. **BERT_LARGE unstable on small datasets.** Fine-tuning BERT_LARGE was "sometimes unstable on small datasets", requiring multiple random restarts with different data shuffling and classifier initialization to select the best model (Section 4.1).

5. **Encoder-only architecture.** BERT uses a bidirectional Transformer encoder and cannot perform autoregressive generation. This limits applicability to classification, span extraction, and tagging tasks unless paired with a separate decoder.

6. **WNLI excluded from evaluation.** The paper excludes WNLI from the GLUE evaluation because "every trained system that's been submitted to GLUE has performed worse than the 65.1 baseline accuracy of predicting the majority class" due to dataset construction issues (Appendix B.1). For the GLUE submission, BERT always predicts the majority class on WNLI.

7. **English-only evaluation.** All pre-training data and evaluation benchmarks are in English. The paper does not evaluate cross-lingual or multilingual capabilities.

#### Scope and Comparability

- **What was not tested:** No models beyond BERT_BASE (110M) and BERT_LARGE (340M) were evaluated on downstream tasks. The model size ablation (Table 6) tests intermediate sizes on only 3 GLUE tasks (MNLI, MRPC, SST-2), not on SQuAD or SWAG. No decoder or encoder-decoder architectures were compared. No languages other than English were tested.
- **Comparability notes:** The comparison with OpenAI GPT is carefully controlled (same model size for BERT_BASE, same number of training steps) but uses different training data (BERT adds Wikipedia to BooksCorpus), different batch sizes (128K vs. 32K words/batch), and different fine-tuning learning rate selection strategies (task-specific vs. fixed 5e-5). The LTR & No NSP ablation (Table 5) isolates bidirectionality more cleanly but still uses BERT's larger training data. The SQuAD v1.1 ensemble results use TriviaQA data augmentation, making them not directly comparable to systems without such augmentation.

---

## Conclusions

### Contributions

1. **Demonstrated the importance of bidirectional pre-training.** The MLM objective enables deep bidirectional representations that substantially outperform left-to-right pre-training (LTR & No NSP drops MRPC by 9.2 points and SQuAD F1 by 10.7 points relative to full BERT) and shallow bidirectional concatenation (ELMo) (Table 5, Section 5.1).

2. **Showed that pre-trained representations reduce the need for task-specific architectures.** BERT is the first fine-tuning-based model to achieve state-of-the-art on both sentence-level tasks (GLUE) and token-level tasks (SQuAD, NER), outperforming many task-specific architectures with a single unified model plus one output layer (Section 1, Tables 1-4).

3. **Advanced state of the art on eleven NLP tasks.** BERT_LARGE achieves: GLUE score 80.5% (+7.7 over prior SOTA), MNLI accuracy 86.7% (+4.6), SQuAD v1.1 Test F1 93.2 (+1.5), SQuAD v2.0 Test F1 83.1 (+5.1), SWAG Test accuracy 86.3% (+8.3 over GPT) (Abstract, Tables 1-4).

4. **Demonstrated that larger pre-trained models benefit even small-scale tasks.** Scaling from 3 layers to 24 layers yields strict improvements on all tasks including MRPC (3,600 training examples), contradicting prior findings that scaling feature-based pre-trained models shows diminishing returns (Table 6, Section 5.2).

5. **Showed BERT is effective for both fine-tuning and feature-based approaches.** Feature-based BERT (concatenating the top 4 hidden layers) achieves 96.1 Dev F1 on CoNLL-2003 NER, only 0.3 F1 behind fine-tuning, demonstrating that BERT's pre-trained representations are rich enough to support both paradigms (Table 7, Section 5.3).

### Implications

1. **Pre-training + fine-tuning as the dominant NLP paradigm.** BERT established that a single pre-trained model, fine-tuned with minimal task-specific parameters, can surpass heavily-engineered task-specific systems across a wide range of NLP tasks. This paradigm shift reduced reliance on task-specific architecture design. [Inference: the generality of this finding was confirmed by subsequent models (RoBERTa, XLNet, etc.) but was not demonstrated in this paper beyond the tested tasks.]

2. **Bidirectional context is essential for language understanding.** The ablation showing that left-to-right pre-training severely degrades token-level tasks like SQuAD (F1 drops from 88.5 to 77.8) suggests that many NLU tasks fundamentally require reasoning over both left and right context (Table 5). [Inference: this may explain why decoder-only models later required much larger scale to achieve competitive NLU performance.]

3. **Scale benefits transfer across task sizes.** The finding that BERT_LARGE improves even on tasks with <4K training examples challenges the conventional wisdom that large models overfit small datasets, provided they are sufficiently pre-trained (Section 5.2).

---

## Key Claims

1. **C1: BERT_LARGE achieves GLUE score of 80.5%.** On the official GLUE leaderboard, BERT_LARGE obtains 80.5, a 7.7 point absolute improvement over the prior state of the art (74.0 for Pre-OpenAI SOTA) and 7.7 points above OpenAI GPT (72.8) (Table 1, Section 4.1). Excluding WNLI, the average across 8 tasks is 82.1 (Table 1). Status: **supported**.

2. **C2: Bidirectional pre-training via MLM is critical.** Replacing the MLM objective with left-to-right LM (directly comparable to OpenAI GPT using BERT's training data and setup) drops MNLI-m accuracy from 84.4 to 82.1 (-2.3), MRPC from 86.7 to 77.5 (-9.2), and SQuAD F1 from 88.5 to 77.8 (-10.7) (Table 5, Section 5.1). Status: **supported**.

3. **C3: Next sentence prediction benefits QNLI, MNLI, and SQuAD.** Removing NSP while keeping MLM drops QNLI by 3.5 points (88.4 to 84.9), MNLI by 0.5 (84.4 to 83.9), and SQuAD F1 by 0.6 (88.5 to 87.9) (Table 5, Section 5.1). Status: **supported**.

4. **C4: BERT_LARGE ensemble achieves 93.2 Test F1 on SQuAD v1.1.** The 7-system ensemble with TriviaQA augmentation achieves 87.4 EM / 93.2 F1 on the test set, surpassing the top leaderboard system (nlnet ensemble: 86.0 EM / 91.7 F1) by +1.5 F1. The single BERT model outperforms the top ensemble in F1 score (Table 2, Section 4.2). Status: **supported**.

5. **C5: BERT_LARGE achieves 83.1 Test F1 on SQuAD v2.0.** A single BERT_LARGE model achieves 80.0 EM / 83.1 F1, surpassing the previous best system (MIR-MRC: 74.8 EM / 78.0 F1) by +5.1 F1 (Table 3, Section 4.3). Status: **supported**.

6. **C6: Larger models improve on all tasks including low-resource ones.** Scaling from (L=3, H=768) to (L=24, H=1024) yields strict improvements on MNLI-m (77.9 to 86.6), MRPC (79.8 to 87.8), and SST-2 (88.4 to 93.7), including MRPC with only 3,600 labeled examples (Table 6, Section 5.2). Status: **supported**.

7. **C7: Feature-based BERT is competitive with fine-tuning.** Concatenating the top 4 hidden layers of BERT_BASE as fixed features achieves 96.1 Dev F1 on CoNLL-2003 NER, vs. 96.4 for BERT_BASE fine-tuning and 96.6 for BERT_LARGE fine-tuning (Table 7, Section 5.3). Status: **supported**.

---

## Open Questions

1. **Can bidirectional pre-training be extended to autoregressive generation?** BERT's encoder-only architecture cannot perform text generation. The paper lists making "generation less sequential" as future work but does not address the bidirectional-generative gap. Not addressed within the references directory.

2. **Is next sentence prediction truly necessary?** The NSP ablation shows benefits on QNLI, MNLI, and SQuAD (Table 5), but the effect on other tasks is minimal (SST-2: -0.1, MRPC: -0.2). Subsequent work (RoBERTa, Liu et al., 2019) showed that removing NSP and training with longer sequences can match or exceed BERT's performance, but this is not represented in the references directory. Not addressed.

3. **How to handle sequences longer than 512 tokens?** BERT's learned positional embeddings limit input to 512 tokens, excluding long-document tasks. Addressed by `2020-04-longformer-long-document-transformer`, which extends BERT-style pre-training to 4,096 tokens using local windowed attention and global attention tokens.

4. **Does the [MASK] mismatch limit performance?** The discrepancy between pre-training (with [MASK] tokens) and fine-tuning (without them) is a design concern (Section 3.1). Table 8 shows the feature-based approach is more sensitive to this than fine-tuning, but the overall impact on downstream performance remains unclear. Not addressed.

---

## Core References and Why They Are Referenced

### Architecture Foundation

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Provides the Transformer architecture that BERT is built upon. BERT uses the Transformer encoder with bidirectional self-attention; the paper explicitly states its implementation is "almost identical to the original" (Section 3).

### Direct Predecessors and Baselines

- **Peters et al. (2018a)** -- *Deep Contextualized Word Representations (ELMo).* Primary feature-based baseline. ELMo uses a shallow concatenation of independently trained left-to-right and right-to-left LSTMs. BERT contrasts itself against ELMo's shallow bidirectionality and demonstrates superior results on GLUE (71.0 vs. 82.1 average) and SQuAD (Table 1, Section 1).

- **Radford et al. (2018)** -- *Improving Language Understanding with Unsupervised Learning (OpenAI GPT).* Primary fine-tuning baseline. GPT uses a left-to-right Transformer LM, while BERT uses a bidirectional MLM. BERT_BASE was designed to match GPT's model size for direct comparison. BERT outperforms GPT on all GLUE tasks (75.1 vs. 82.1 average) (Table 1, Section 1, Appendix A.4).

- **Howard and Ruder (2018)** -- *Universal Language Model Fine-tuning for Text Classification (ULMFiT).* Demonstrates effective transfer learning via fine-tuning LMs. Referenced as a key predecessor in the fine-tuning paradigm (Section 2.2).

### Pre-training Objectives

- **Taylor (1953)** -- *Cloze Procedure: A New Tool for Measuring Readability.* The Cloze task, which asks subjects to predict deleted words from context, directly inspires BERT's masked language model objective (Section 3.1).

- **Vincent et al. (2008)** -- *Extracting and Composing Robust Features with Denoising Autoencoders.* Denoising autoencoders reconstruct entire inputs from corrupted versions. BERT's MLM differs by predicting only the masked tokens rather than reconstructing the full input (Section 3.1).

### Evaluation Benchmarks

- **Wang et al. (2018a)** -- *GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding.* The primary evaluation benchmark. BERT advances the GLUE score from 74.0 to 80.5 (Section 4.1).

- **Rajpurkar et al. (2016)** -- *SQuAD: 100,000+ Questions for Machine Comprehension of Text.* Provides the SQuAD v1.1 question answering benchmark. BERT achieves 93.2 Test F1 on this dataset (Section 4.2, Table 2).

- **Zellers et al. (2018)** -- *SWAG: A Large-Scale Adversarial Dataset for Grounded Commonsense Inference.* Provides the SWAG commonsense inference benchmark. BERT_LARGE achieves 86.3% test accuracy, surpassing human expert performance (85.0%) (Section 4.4, Table 4).

- **Tjong Kim Sang and De Meulder (2003)** -- *Introduction to the CoNLL-2003 Shared Task.* Provides the NER evaluation used to compare fine-tuning and feature-based approaches (Section 5.3, Table 7).

### Tokenization and Training

- **Wu et al. (2016)** -- *Google's Neural Machine Translation System.* Provides the WordPiece tokenization used by BERT with a 30,000 token vocabulary (Section 3).

- **Hendrycks and Gimpel (2016)** -- *Gaussian Error Linear Units (GELUs).* BERT uses GELU activation instead of the standard ReLU (Appendix A.2).

- **Zhu et al. (2015)** -- *Aligning Books and Movies.* Source of the BooksCorpus (800M words) used for BERT pre-training (Section 3.1).

### Transfer Learning Context

- **Dai and Le (2015)** -- *Semi-Supervised Sequence Learning.* Early work on pre-training sequence models from unlabeled text and fine-tuning for downstream tasks, establishing the paradigm BERT follows (Sections 1, 2.2).

- **Conneau et al. (2017)** -- *Supervised Learning of Universal Sentence Representations from Natural Language Inference Data.* Demonstrates transfer from supervised NLI. Referenced as an example of transfer learning from supervised data (Section 2.3).

### Representation Analysis

- **Peters et al. (2018b)** -- *Dissecting Contextual Word Embeddings: Architecture and Representation.* Shows mixed results from scaling feature-based pre-trained models from 2 to 4 layers. BERT's finding that fine-tuning benefits from scale even on small tasks contrasts with these feature-based results (Section 5.2).
