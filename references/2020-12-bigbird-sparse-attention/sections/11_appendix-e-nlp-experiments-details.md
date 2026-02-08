# E NLP experiments details [p. 33-36]

## E.1 MLM Pretraining [p. 33]

[p. 33] Four publicly available datasets are used: Books [110], CC-News [34], Stories [89], and Wikipedia to pretrain BIGBIRD. The sentencepiece vocabulary is borrowed from RoBERTa (which is in turn borrowed from GPT2). Any document longer than 4096 is split into multiple documents and shorter documents are joined so that the resulting documents are close to but not much smaller than 4096. Following the original BERT training, 15% of tokens are masked and the model is trained to predict the mask. The authors warm start from RoBERTa's checkpoint. Two different models are trained: BIGBIRD-ITC-base and BIGBIRD-ETC-base. The hyperparameters for these two models are given in Tab. 8. In all experiments, a learning rate warmup over the first 10,000 steps and linear decay of the learning rate are used.

[p. 33] Similarly to the norm, a large version of the model is also trained, which has 24 layers with 16 heads and hidden dimension of 1024. Following the observation from RoBERTa, pretraining uses a larger batch size of 2048 for this size. For BIGBIRD-ITC the block length was kept same as base size, but for BIGBIRD-ETC the block length was almost doubled to 169. All the remaining parameters were the same.

### Table 8 (p. 33)

**Table 8:** Hyperparameters for the two BIGBIRD base models for MLM.

| Parameter | BIGBIRD-ITC | BIGBIRD-ETC |
|---|---|---|
| Block length, b | 64 | 84 |
| # of global token, g | 2 x b | 256 |
| Window length, w | 3 x b | 3 x b |
| # of random token, r | 3 x b | 0 |
| Max. sequence length | 4096 | 4096 |
| # of heads | 12 | 12 |
| # of hidden layers | 12 | 12 |
| Hidden layer size | 768 | 768 |
| Batch size | 256 | 256 |
| Loss | MLM | MLM |
| Activation layer | gelu | gelu |
| Dropout prob | 0.1 | 0.1 |
| Attention dropout prob | 0.1 | 0.1 |
| Optimizer | Adam | Adam |
| Learning rate | 10^{-4} | 10^{-4} |
| Compute resources | 8 x 8 TPUv3 | 8 x 8 TPUv3 |

### Table 9 (p. 33)

**Table 9:** Dataset used for pre training.

| Dataset | # tokens | Avg. doc len. |
|---|---|---|
| Books [110] | 1.0B | 37K |
| CC-News [34] | 7.4B | 561 |
| Stories [89] | 7.7B | 8.2K |
| Wikipedia | 3.1B | 592 |

### Table 10 (p. 33)

**Table 10:** MLM performance on held-out set.

| Model | Base BPC | Large BPC |
|---|---|---|
| RoBERTa (sqln: 512) | 1.846 | 1.496 |
| Longformer (sqln: 4096) | 1.705 | 1.358 |
| BIGBIRD-ITC (sqln: 4096) | 1.678 | 1.456 |
| BIGBIRD-ETC (sqln: 4096) | **1.611** | **1.274** |

Note: The two numeric columns correspond to Base and Large model sizes.

## E.2 Question Answering [p. 33-35]

[p. 33] The detailed statistics of the four datasets used are given in Tab. 11. All the hyperparameters for BIGBIRD, used for creating Tab. 2, are shown in Tab. 12, and those submitted to get Tab. 3 are shown in Tab. 13. Two types of regularization are used in training:

- A variant of contrastive predictive coding [70] is used as a dual encoder model.
- Position embedding is used for ITC and relative position encoding [79] for ETC.

### Table 11 (p. 34)

**Table 11:** Question Answering Datasets

| Dataset | Instances Training | Instances Dev | Instance Length Median | Instance Length Max |
|---|---|---|---|---|
| HotpotQA-distractor [100] | 90447 | 7405 | 1227 | 3560 |
| Natural Questions [52] | 307373 | 7830 | 3258 | 77962 |
| TriviaQA [41] | 61888 | 7993 | 4900 | 32755 |
| WikiHop [95] | 43738 | 5129 | 1541 | 20337 |

### Table 12 (p. 34)

**Table 12:** Hyperparameters of base BIGBIRD model used for Question Answering i.e. the numbers reported in Tab. 2.

| Parameter | HotpotQA ITC | HotpotQA ETC | NaturalQ ITC | NaturalQ ETC | TriviaQA ITC | TriviaQA ETC | WikiHop ITC | WikiHop ETC |
|---|---|---|---|---|---|---|---|---|
| Global token location | | | | | | | | |
| # of global token, g | 128 | 256 | 128 | 230 | 128 | 320 | 128 | 430 |
| Window length, w | 192 | 252 | 192 | 252 | 192 | 252 | 192 | 252 |
| # of random token, r | 192 | 0 | 192 | 0 | 192 | 0 | 192 | 0 |
| Max. sequence length | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 | 4096 |
| # of heads | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| # of hidden layers | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Hidden layer size | 768 | 768 | 768 | 768 | 768 | 768 | 768 | 768 |
| Batch size | 32 | 32 | 128 | 128 | 32 | 32 | 64 | 64 |
| Loss | cross-entropy golden spans | cross-entropy golden spans | cross-entropy golden spans | cross-entropy golden spans | cross-entropy noisy spans [18] | cross-entropy noisy spans [18] | cross-entropy ans choices | cross-entropy ans choices |
| Compute resources | 4 x 2 TPUv3 | 4 x 2 TPUv3 | 4 x 8 TPUv3 | 4 x 8 TPUv3 | 4 x 2 TPUv3 | 4 x 2 TPUv3 | 4 x 4 TPUv3 | 4 x 4 TPUv3 |

### Table 13 (p. 35)

**Table 13:** Hyperparameters of large BIGBIRD model for Question Answering submitted for test i.e. the numbers reported in Tab. 3.

| Parameter | HotpotQA | NaturalQ | TriviaQA | WikiHop |
|---|---|---|---|---|
| Global token location | ETC | ETC | ETC | ETC |
| # of global token, g | 256 | 230 | 320 | 430 |
| Window length, w | 507 | 507 | 507 | 507 |
| # of random token, r | 0 | 0 | 0 | 0 |
| Max. sequence length | 4096 | 4096 | 4096 | 4096 |
| # of heads | 16 | 16 | 16 | 16 |
| # of hidden layers | 24 | 24 | 24 | 24 |
| Hidden layer size | 1024 | 1024 | 1024 | 1024 |
| Batch size | 32 | 64 | 32 | 64 |
| Loss | cross-entropy | cross-entropy | cross-entropy | cross-entropy |
| Num epochs | {5, 9} | {3, 5} | {3, 5} | {5, 10} |
| Optimizer | Adam | Adam | Adam | LAMB |
| Learning rate | 3 x 10^{-5} | {5, 10} x 10^{-5} | {3, 5} x 10^{-5} | {2, 5} x 10^{-5} |
| Compute resources | 4 x 4 TPUv3 | 4 x 8 TPUv3 | 4 x 4 TPUv3 | 4 x 8 TPUv3 |

### HotpotQA [p. 34]

[p. 34] The data consists of each question with multiple evidence paragraphs. 16 QA are filtered where the answer was not in the given evidences. For BIGBIRD-ITC, the first 128 global tokens are used. For BIGBIRD-ETC, there is one global token for each question token, one for each evidence paragraph, and one for each sentence within the paragraph, for a maximum of 256 global tokens. A dense layer on the output corresponding to global token of the evidence paragraph is used to predict whether it is a supporting fact with a threshold over the output logits. The answer type (yes/no/span) is predicted with a single dense layer from the global CLS token. For span-based answers, the spans are predicted with dense layers on the sequence with the distance between start and end positions to be no more than 30 words. The spans are ranked by sum of start and end logits.

### Natural Questions [p. 34]

[p. 34] The data consists of question with supporting evidence, but in form of a single, potentially long, document and not multiple paragraphs. The setup of [5] is largely followed. For documents that are longer than 4096, a sliding window approach is used with stride of 2048. CLS token is used at the beginning, followed by the question followed by a separator token followed by the document as input. For BIGBIRD-ITC, the first 128 tokens are made global. For BIGBIRD-ETC, a global token is made for CLS, question, and one token for each of the paragraphs. Four predictors at the final layer are trained to predict long answer start, long answer end, short answer start, and short answer end respectively. Instead of independently predicting the start and end of answers, the start is first predicted and then the best end location beyond the start is predicted. For short answer, the distance between start and end positions is limited to be no more than 38 words. The answer type (null, yes, no, short, long) is predicted from CLS token output embedding. When the logit for a yes/no answer is higher than the logits for short, long or null answer, the short answer is replaced with a corresponding yes/no text.

### TriviaQA [p. 34-35]

[p. 34-35] The data consists of question-answer pairs with Wikipedia articles as the "noisy" supporting evidence. They are called noisy because the given Wikipedia articles may or may not contain the answer. Moreover, the answer entities are not annotated to appropriate span in the article; rather all occurrences found using fuzzy string matching are listed. CLS token is used at the beginning, followed by the question followed by a separator token followed by the document as input. For BIGBIRD-ITC, the first 128 tokens are made global. For BIGBIRD-ETC, a global token is made for CLS, question, and one token for each sentence up to a maximum of 320 global tokens. Given the noisy nature of answer span, Clark and Gardner [18] are followed for training. A dense layer on the sequence is used to predict the answer span for each article independently, with the distance between start and end positions to be no more than 16 words. For each article the span with maximum start logit + end logit is chosen. Then normalization is applied over all the documents associated with that question.

### WikiHop [p. 35]

[p. 35] For each question in WikiHop, up to 79 candidates are given, and 63 supporting paragraphs. In the BIGBIRD-ITC model, following Beltagy et al. [8], the answer and the question are concatenated with special tokens: [q] Question [/q] [ans] Ans1 [/ans] ... [ans] AnsN [/ans] along with the context. As the start of the text always contains questions followed by answers, the first 128 tokens attend globally. In BIGBIRD-ETC model, there is no need to insert special [ans], [/ans] etc. as global tokens are designed appropriately. Along with global tokens for question, there is one per candidate answer up to a maximum of 430. Further, answer tokens are linked to their mentions using relative position label. Lastly, a dense layer takes in the output vector corresponding to a candidate answer, and predicts a score for the current candidate to be the correct answer. This dense layer is applied to each candidate independently and the candidate with the best score is picked as the final answer.

[p. 35] It is worthwhile to note that explicitly designed attention connection in ETC works slightly better, the random connection based ITC is pretty competitive.

## E.3 Relationship to Contemporary Work [p. 35]

[p. 35] **Longformer** Child et al. [16] introduced localized sliding window to reduce computation. A more recent version, which includes localized sliding windows and global tokens, was introduced independently by Longformer [8]. Although BIGBIRD contains additional random tokens, there are also differences in the way global and local tokens are realized. In particular even when there is no random token, as used to get SoTA in question answering, there are two key differences between Longformer and BIGBIRD-etc (see [4]):

1. Global-local attention with relative position encodings is used, which enables it to better handle structured inputs.
2. Unlike Longformer, the global tokens are trained using CPC loss and their use is learned during finetuning.

## E.4 Classification [p. 35-36]

[p. 35-36] Two types of classification task are tried.

### Document classification [p. 35-36]

[p. 35-36] Experiments are conducted on datasets of different lengths and contents, as listed in Tab. 15. In particular, sentiment analysis (IMDb [64] and Yelp-5 [108]) task and topic assignment (Arxiv [35], Patents [53], and Hyperpartisan [47]) task are considered. Following BERT, one layer with cross entropy loss on top of the first [CLS] token from the BIGBIRD encoder consuming 4096 tokens is used. The results of document classification experiments are reported in Tab. 15. Comparison is made against state-of-the-art (SoTA) methods for each dataset and plain RoBERTa model with 512 tokens truncation. In all experiments, a learning rate warmup over the first 10% steps and linear decay of the learning rate are used. For better quantitative evaluation, the fraction of the dataset that exceeds 512 tokens (i.e. the length at which the document is often truncated) is computed. The gains of using BIGBIRD are more significant when there are longer documents and fewer training examples. For instance, using base sized model, BIGBIRD improves state-of-the-art for Arxiv dataset by about 5% points. On Patents dataset, there is improvement over using simple BERT/RoBERTa, but given the large size of training data the improvement over SoTA (which is not BERT based) is not significant.

### Table 14 (p. 36)

**Table 14:** Hyperparameters for document classification.

| Parameter | IMDb | Arxiv | Patents | Hyperpartisan | Yelp-5 |
|---|---|---|---|---|---|
| Batch size | 64 | 64 | 64 | 32 | 32 |
| Learning rate | 1 x 10^{-5} | 3 x 10^{-5} | 5 x 10^{-5} | 5 x 10^{-6} | 2 x 10^{-5} |
| Num epochs | 40 | 10 | 3 | 15 | 2 |
| TPUv3 slice | 4 x 4 | 4 x 4 | 4 x 4 | 4 x 2 | 4 x 8 |
| # of heads | | 12 | | | 16 |
| # of hidden layers | | 12 | | | 24 |
| Hidden layer size | | 768 | | | 1024 |
| Block length, b | | | 64 | | |
| Global token location | | | ITC | | |
| # of global token, g | | | 2 x b | | |
| Window length, w | | | 3 x b | | |
| # of random token, r | | | 3 x b | | |
| Max. sequence length | | | 4096 | | |
| Vocab size | | | 50358 | | |
| Activation layer | | | gelu | | |
| Dropout prob | | | 0.1 | | |
| Attention dropout prob | | | 0.1 | | |
| Loss | | | cross-entropy | | |
| Optimizer | | | Adam | | |

Note: In Table 14, the parameters # of heads through Optimizer share values across the first three datasets (IMDb, Arxiv, Patents) using the base model (12 heads, 12 layers, 768 hidden), while Yelp-5 uses the large model (16 heads, 24 layers, 1024 hidden). Hyperpartisan uses 4 x 2 TPUv3 with batch size 32.

### Table 15 (p. 36)

**Table 15:** Classification results. We report the F1 micro-averaged score for all datasets. Experiments on smaller IMDb and Hyperpartisan datasets are repeated 5 times and the average performance is presented along with standard deviation.

| Model | IMDb [64] | Yelp-5 [108] | Arxiv [35] | Patents [53] | Hyperpartisan [47] |
|---|---|---|---|---|---|
| # Examples | 25000 | 650000 | 30043 | 1890093 | 645 |
| # Classes | 2 | 5 | 11 | 663 | 2 |
| Excess fraction | 0.14 | 0.04 | 1.00 | 0.90 | 0.53 |
| SoTA | [88] 97.4 | [3] 73.28 | [69] 87.96 | [69] 69.01 | [40] 90.6 |
| RoBERTa | 95.0 +/- 0.2 | 71.75 | 87.42 | 67.07 | 87.8 +/- 0.8 |
| BIGBIRD | 95.2 +/- 0.2 | 72.16 | **92.31** | 69.30 | **92.2 +/- 1.7** |

### GLUE [p. 36-37]

[p. 36-37] The General Language Understanding Evaluation (GLUE) benchmark [92] tests language models on 8 different natural language understanding tasks. The same training parameters as mentioned in `https://github.com/pytorch/fairseq/blob/master/examples/roberta/README.glue.md` are used. Model parameters are b = 64, g = 2 x b, w = 3 x b, r = 3 x b (using the BIGBIRD-ITC base model pretrained on MLM task). The performance of BIGBIRD is compared to BERT, XLNet [101], and RoBERTa in Tab. 16. Even on tasks that have a much smaller context, their performance is competitive to full attention models.

### Table 16 (p. 36)

**Table 16:** GLUE Dev results on base sized models. Number of training examples is reported below each task. MCC score is reported for CoLA, F1 score is reported for MRPC, Spearman correlation is reported for STS-B, and accuracy scores are reported for the other tasks.

| System | MNLI-(m/mm) 392k | QQP 363k | QNLI 108k | SST-2 67k | CoLA 8.5k | STS-B 5.7k | MRPC 3.5k | RTE 2.5k |
|---|---|---|---|---|---|---|---|---|
| BERT | 84.6/83.4 | 71.2 | 90.5 | 93.5 | 52.1 | 85.8 | 88.9 | 66.4 |
| XLNet | 86.8/- | 91.4 | 91.7 | 94.7 | 60.2 | 89.5 | 88.2 | 74.0 |
| RoBERTa | 87.6/- | 91.9 | 92.8 | 94.8 | 63.6 | 91.2 | 90.2 | 78.7 |
| BIGBIRD | 87.5/87.3 | 88.6 | 92.2 | 94.6 | 58.5 | 87.8 | 91.5 | 75.0 |

## E.5 Summarization [p. 37-38]

[p. 37] As discussed in Sec. 4.1, given the small length of output sequence, sparse BIGBIRD attention is used only for the encoder, while keeping the full attention for the decoder. The number of hidden layers, number of heads, and hidden dimension is the same for encoder and decoder. The hyperparameters are detailed in Tab. 17. Results are summarized in Tab. 20. In all experiments, a learning rate warmup over the first 10,000 steps and square root decay of the learning rate are used.

### Table 17 (p. 37)

**Table 17:** Encoder hyperparameters for Summarization. We use full attention in decoder.

| Parameter | Base: BIGBIRD-RoBERTa | Large: BIGBIRD-Pegasus |
|---|---|---|
| Block length, b | 64 | 64 |
| Global token location | ITC | ITC |
| # of global token, g | 2 x b | 2 x b |
| Window length, w | 3 x b | 3 x b |
| # of random token, r | 3 x b | 3 x b |
| Max. encoder sequence length (BBC-XSUM) | 1024 | 1024 |
| Max. encoder sequence length (CNN/DM) | 2048 | 2048 |
| Max. encoder sequence length (Others) | 3072 | 3072 |
| Max. decoder sequence length (BBC-XSUM) | 64 | 64 |
| Max. decoder sequence length (CNN/DM) | 128 | 128 |
| Max. decoder sequence length (Others) | 256 | 256 |
| Beam size | 5 | 5 |
| Length penalty (BBC-XSUM) | 0.7 | 0.7 |
| Length penalty (Others) | 0.8 | 0.8 |
| # of heads | 12 | 16 |
| # of hidden layers | 12 | 16 |
| Hidden layer size | 768 | 1024 |
| Batch size | 128 | 128 |
| Loss | teacher forced cross-entropy | teacher forced cross-entropy |
| Activation layer | gelu | gelu |
| Dropout prob | 0.1 | 0.1 |
| Attention dropout prob | 0.1 | 0.1 |
| Optimizer | Adam | Adafactor |
| Learning rate | 1 x 10^{-5} | 1 x 10^{-4} |
| Compute resources | 4 x 4 TPUv3 | 4 x 8 TPUv3 |

### Table 18 (p. 37)

**Table 18:** Statistics of datasets used for summarization.

| Dataset | Training | Dev | Test | Input Length Median | Input Length 90%-ile | Output Length Median | Output Length 90%-ile |
|---|---|---|---|---|---|---|---|
| Arxiv [20] | 203037 | 6436 | 6440 | 6151 | 14405 | 171 | 352 |
| PubMed [20] | 119924 | 6633 | 6658 | 2715 | 6101 | 212 | 318 |
| BigPatent [78] | 1207222 | 67068 | 67072 | 3082 | 7693 | 123 | 197 |

### Table 19 (p. 38)

**Table 19:** Shorter summarization dataset statistics.

| Dataset | Training | Dev | Test | Input Length Median | Input Length 90%-ile | Output Length Median | Output Length 90%-ile |
|---|---|---|---|---|---|---|---|
| BBC XSum [67] | 204044 | 11332 | 11334 | 359 | 920 | 25 | 32 |
| CNN/DailyMail [36] | 287113 | 13368 | 11490 | 777 | 1439 | 59 | 93 |

### Table 20 (p. 38)

**Table 20:** Summarization ROUGE score for shorter documents.

| | Model | BBC XSum R-1 | BBC XSum R-2 | BBC XSum R-L | CNN/DailyMail R1 | CNN/DailyMail R2 | CNN/DailyMail R-L |
|---|---|---|---|---|---|---|---|
| Prior Art | Lead | 16.30 | 1.61 | 11.95 | 39.60 | 17.70 | 36.20 |
| | PtGen [77] | 29.70 | 9.21 | 23.24 | 39.53 | 17.28 | 36.38 |
| | ConvS2S [28] | 31.89 | 11.54 | 25.75 | -- | -- | -- |
| | MMN [48] | 32.00 | 12.10 | 26.00 | -- | -- | -- |
| | Bottom-Up [29] | -- | -- | -- | 41.22 | 18.68 | 38.34 |
| | TransLM [45] | -- | -- | -- | 39.65 | 17.74 | 36.85 |
| | UniLM [23] | -- | -- | -- | 43.47 | 20.30 | 40.63 |
| | Extr-Abst-BERT [62] | 38.81 | 16.50 | 31.27 | 42.13 | 19.60 | 39.18 |
| | BART [56] | 45.14 | 22.27 | 37.25 | 44.16 | 21.28 | 40.90 |
| Base | Transformer [91] | 29.61 | 9.47 | 23.17 | 34.89 | 13.13 | 32.12 |
| | + RoBERTa [76] | 39.92 | **17.33** | **32.63** | 39.44 | 18.69 | 36.80 |
| | + Pegasus [107] | 39.79 | 16.58 | 31.70 | **41.79** | **18.81** | **38.93** |
| | BIGBIRD-RoBERTa | 39.52 | 17.22 | 32.30 | 39.25 | 18.46 | 36.61 |
| Large | Pegasus (Reported) [107] | 47.60 | 24.83 | 39.64 | 44.16 | 21.56 | 41.30 |
| | Pegasus (Re-eval) | **47.37** | **24.31** | **39.23** | **44.15** | **21.56** | **41.05** |
| | BIGBIRD-Pegasus | 47.12 | 24.05 | 38.80 | 43.84 | 21.11 | 40.74 |

[p. 38] Following the success of several recent works [76, 63], the encoder-decoder BIGBIRD transformer model is warm started with pretrained weights and the weights between encoder and decoder are shared. In particular, the query/key/value matrix of self-attention and all the feedforward layers are shared between encoder and decoder. The only variable that is initialized randomly is the encoder-decoder attention. For the base sized model, the MLM pretrained model on 4096 sequence length from App. E.1 is used, which is in turn initialized using the public RoBERTa checkpoint. For the large size model, weights are lifted from the state-of-the-art Pegasus model [107], which is pretrained using an objective designed for summarization task.

[p. 38] To check if sparse attention causes significant degradation as compared to full attention, a further experiment is conducted on two shorter but popular datasets, where full attention can be used without significantly truncating the document. The statistics of these two datasets are in Tab. 19. The performance is competitive, which shows that sparse attention can achieve similar performance to a full attention model.
