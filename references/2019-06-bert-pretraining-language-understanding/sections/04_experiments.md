# Experiments [p. 5-6]

BERT fine-tuning results on 11 NLP tasks.

## 4.1 GLUE

[p. 5-6] The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks. Detailed descriptions of GLUE datasets are included in Appendix B.1.

### Fine-tuning setup for GLUE

- Input sequence represented as described in Section 3 (single sentence or sentence pairs)
- Final hidden vector C in R^H corresponding to `[CLS]` used as the aggregate representation
- Only new parameters introduced during fine-tuning: classification layer weights W in R^{K x H}, where K is the number of labels
- Classification loss: log(softmax(CW^T))
- Batch size: 32
- Fine-tune for 3 epochs over the data for all GLUE tasks
- Best fine-tuning learning rate selected from {5e-5, 4e-5, 3e-5, 2e-5} on the Dev set
- For BERT_LARGE: fine-tuning was sometimes unstable on small datasets, so several random restarts were run and the best model on the Dev set was selected (same pre-trained checkpoint, different fine-tuning data shuffling and classifier layer initialization)

### Table 1: GLUE Test results

Scored by the evaluation server (https://gluebenchmark.com/leaderboard). The number below each task denotes the number of training examples. The "Average" column is slightly different than the official GLUE score since the problematic WNLI set is excluded. BERT and OpenAI GPT are single-model, single task. F1 scores reported for QQP and MRPC, Spearman correlations for STS-B, accuracy scores for the other tasks. Entries that use BERT as one of their components are excluded.

| System | MNLI-(m/mm) 392k | QQP 363k | QNLI 108k | SST-2 67k | CoLA 8.5k | STS-B 5.7k | MRPC 3.5k | RTE 2.5k | Average |
|---|---|---|---|---|---|---|---|---|---|
| Pre-OpenAI SOTA | 80.6/80.1 | 66.1 | 82.3 | 93.2 | 35.0 | 81.0 | 86.0 | 61.7 | 74.0 |
| BiLSTM+ELMo+Attn | 76.4/76.1 | 64.8 | 79.8 | 90.4 | 36.0 | 73.3 | 84.9 | 56.8 | 71.0 |
| OpenAI GPT | 82.1/81.4 | 70.3 | 87.4 | 91.3 | 45.4 | 80.0 | 82.3 | 56.0 | 75.1 |
| BERT_BASE | 84.6/83.4 | 71.2 | 90.5 | 93.5 | 52.1 | 85.8 | 88.9 | 66.4 | 79.6 |
| BERT_LARGE | **86.7/85.9** | **72.1** | **92.7** | **94.9** | **60.5** | **86.5** | **89.3** | **70.1** | **82.1** |

### Key results for GLUE

[p. 6] Both BERT_BASE and BERT_LARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the prior state of the art. BERT_BASE and OpenAI GPT are nearly identical in terms of model architecture apart from the attention masking. For the largest and most widely reported GLUE task, MNLI, BERT obtains a 4.6% absolute accuracy improvement. On the official GLUE leaderboard, BERT_LARGE obtains a score of 80.5, compared to OpenAI GPT which obtains 72.8 as of the date of writing.

BERT_LARGE significantly outperforms BERT_BASE across all tasks, especially those with very little training data. The effect of model size is explored more thoroughly in Section 5.2.

The GLUE data set distribution does not include the Test labels, and only a single GLUE evaluation server submission was made for each of BERT_BASE and BERT_LARGE. [p. 6, footnote 9]

## 4.2 SQuAD v1.1

[p. 6] The Stanford Question Answering Dataset (SQuAD v1.1) is a collection of 100k crowd-sourced question/answer pairs (Rajpurkar et al., 2016). Given a question and a passage from Wikipedia containing the answer, the task is to predict the answer text span in the passage.

### SQuAD v1.1 fine-tuning details

- Input: question and passage represented as a single packed sequence, with the question using the A embedding and the passage using the B embedding
- A start vector S in R^H and an end vector E in R^H are introduced during fine-tuning
- Probability of word i being the start of the answer span:

  P_i = e^{S . T_i} / sum_j e^{S . T_j}

  (softmax of dot product between T_i and S over all words in the paragraph)

- Analogous formula used for the end of the answer span
- Score of a candidate span from position i to position j: S . T_i + E . T_j
- Maximum scoring span where j >= i is used as the prediction
- Training objective: sum of the log-likelihoods of the correct start and end positions
- Fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32

### SQuAD v1.1 results

[p. 6] Table 2 shows top leaderboard entries as well as results from top published systems (Seo et al., 2017; Clark and Gardner, 2018; Peters et al., 2018a; Hu et al., 2018). Top results from the SQuAD leaderboard do not have up-to-date public system descriptions available, and are allowed to use any public data when training their systems. The authors therefore use modest data augmentation by first fine-tuning on TriviaQA (Joshi et al., 2017) before fine-tuning on SQuAD.

The best performing system outperforms the top leaderboard system by +1.5 F1 in ensembling and +1.3 F1 as a single system. In fact, the single BERT model outperforms the top ensemble system in terms of F1 score. Without TriviaQA fine-tuning data, only 0.1-0.4 F1 is lost, still outperforming all existing systems by a wide margin.

---
[p. 7 continued]

### Table 2: SQuAD 1.1 results

The BERT ensemble is 7x systems which use different pre-training checkpoints and fine-tuning seeds.

| System | Dev EM | Dev F1 | Test EM | Test F1 |
|---|---|---|---|---|
| **Top Leaderboard Systems (Dec 10th, 2018)** | | | | |
| Human | - | - | 82.3 | 91.2 |
| #1 Ensemble - nlnet | - | - | 86.0 | 91.7 |
| #2 Ensemble - QANet | - | - | 84.5 | 90.5 |
| **Published** | | | | |
| BiDAF+ELMo (Single) | - | 85.6 | - | 85.8 |
| R.M. Reader (Ensemble) | 81.2 | 87.9 | 82.3 | 88.5 |
| **Ours** | | | | |
| BERT_BASE (Single) | 80.8 | 88.5 | - | - |
| BERT_LARGE (Single) | 84.1 | 90.9 | - | - |
| BERT_LARGE (Ensemble) | 85.8 | 91.8 | - | - |
| BERT_LARGE (Sgl.+TriviaQA) | 84.2 | 91.1 | 85.1 | 91.8 |
| BERT_LARGE (Ens.+TriviaQA) | 86.2 | 92.2 | 87.4 | 93.2 |

The TriviaQA data used consists of paragraphs from TriviaQA-Wiki formed of the first 400 tokens in documents, that contain at least one of the provided possible answers. [p. 7, footnote 12]

## 4.3 SQuAD v2.0

[p. 7] The SQuAD 2.0 task extends the SQuAD 1.1 problem definition by allowing for the possibility that no short answer exists in the provided paragraph, making the problem more realistic.

A simple approach is used to extend the SQuAD v1.1 BERT model for this task. Questions that do not have an answer are treated as having an answer span with start and end at the `[CLS]` token. The probability space for the start and end answer span positions is extended to include the position of the `[CLS]` token. For prediction, the score of the no-answer span is compared:

s_null = S . C + E . C

to the score of the best non-null span:

s_hat_{i,j} = max_{j >= i} S . T_i + E . T_j

A non-null answer is predicted when s_hat_{i,j} > s_null + tau, where the threshold tau is selected on the dev set to maximize F1. TriviaQA data is not used for this model. Fine-tuned for 2 epochs with a learning rate of 5e-5 and a batch size of 48.

### Table 3: SQuAD 2.0 results

Results compared to prior leaderboard entries and top published work (Sun et al., 2018; Wang et al., 2018b), excluding systems that use BERT as one of their components.

| System | Dev EM | Dev F1 | Test EM | Test F1 |
|---|---|---|---|---|
| **Top Leaderboard Systems (Dec 10th, 2018)** | | | | |
| Human | 86.3 | 89.0 | 86.9 | 89.5 |
| #1 Single - MIR-MRC (F-Net) | - | - | 74.8 | 78.0 |
| #2 Single - nlnet | - | - | 74.2 | 77.1 |
| **Published** | | | | |
| unet (Ensemble) | - | - | 71.4 | 74.9 |
| SLQA+ (Single) | - | - | 71.4 | 74.4 |
| **Ours** | | | | |
| BERT_LARGE (Single) | 78.7 | 81.9 | 80.0 | 83.1 |

[p. 7] A +5.1 F1 improvement over the previous best system is observed.

## 4.4 SWAG

[p. 7] The Situations With Adversarial Generations (SWAG) dataset contains 113k sentence-pair completion examples that evaluate grounded commonsense inference (Zellers et al., 2018). Given a sentence, the task is to choose the most plausible continuation among four choices.

### SWAG fine-tuning details

- Construct four input sequences, each containing the concatenation of the given sentence (sentence A) and a possible continuation (sentence B)
- Only task-specific parameters introduced: a vector whose dot product with the `[CLS]` token representation C denotes a score for each choice, normalized with a softmax layer
- Fine-tune for 3 epochs with a learning rate of 2e-5 and a batch size of 16

### Table 4: SWAG Dev and Test accuracies

Human performance measured with 100 samples, as reported in the SWAG paper.

| System | Dev | Test |
|---|---|---|
| ESIM+GloVe | 51.9 | 52.7 |
| ESIM+ELMo | 59.1 | 59.2 |
| OpenAI GPT | - | 78.0 |
| BERT_BASE | 81.6 | - |
| BERT_LARGE | **86.6** | **86.3** |
| Human (expert)^dagger | - | 85.0 |
| Human (5 annotations)^dagger | - | 88.0 |

[p. 7] BERT_LARGE outperforms the authors' baseline ESIM+ELMo system by +27.1% and OpenAI GPT by 8.3%.
