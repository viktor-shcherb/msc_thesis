# 4 Experiments: Natural Language Processing [p. 6-9]

[p. 6] The goal is to showcase benefits of modeling longer input sequences for NLP tasks, for which three representative tasks are selected. They begin with basic masked language modeling (MLM; Devlin et al. [22]) to check if better contextual representations can be learnt by utilizing longer contiguous sequences. Next, they consider QA with supporting evidence, for which the capability to handle longer sequences would allow retrieving more evidence using crude systems like TF-IDF/BM25. Finally, they tackle long document classification where discriminating information may not be located in the first 512 tokens. [p. 7]

Below, results for BIGBIRD using sequence length 4096 are summarized, while all other setup details including computational resources, batch size, step size are deferred to App. E.

## Pretraining and MLM

[p. 7] The authors follow [22, 63] to create base and large versions of BIGBIRD and pretrain using the MLM objective. This task involves predicting a random subset of tokens which have been masked out. They use four standard data-sets for pretraining (listed in App. E.1, Tab. 9), warm-starting from the public RoBERTa checkpoint. They compare performance in predicting the masked out tokens in terms of bits per character (BPC), following [8]. As seen in App. E.1, Tab. 10, both BIGBIRD and Longformer perform better than limited length RoBERTa, with BIGBIRD-ETC performing the best. They note that they trained their models on a reasonable 16GB memory/chip with batch size of 32-64. Memory efficiency is due to efficient blocking and sparsity structure of the sparse attention mechanism described in Sec. 2. [p. 7]

## Question Answering (QA)

[p. 7] Four challenging datasets are considered:

1. **Natural Questions [52]:** For the given question, find a short span of answer (SA) from the given evidences as well as highlight the paragraph from the given evidences containing information about the correct answer (LA).
2. **HotpotQA-distractor [100]:** Similar to natural questions, it requires finding the answer (Ans) as well as the supporting facts (Sup) over different documents needed for multi-hop reasoning from the given evidences.
3. **TriviaQA-wiki [41]:** Provide an answer for the given question using provided Wikipedia evidence; however, the answer might not be present in the given evidence. On a smaller *verified* subset of the question, the given evidence is guaranteed to contain the answer. They model the answer as span selection in this case as well.
4. **WikiHop [95]:** Choose correct option from multiple-choice questions (MCQ), by aggregating information spread across multiple documents given in the evidences.

[p. 8] As these tasks are very competitive, multiple highly engineered systems have been designed specific to each dataset confirming to respective output formats. For a fair comparison, the authors had to use some additional regularization for training BIGBIRD, details of which are provided in App. E.2 along with exact architecture description. They experiment using the base sized model and select the best configuration on the development set (as reported in Tab. 2). They observe that BIGBIRD-ETC, with expanded global tokens, consistently outperforms all other models. Thus, they chose this configuration to train a large sized model to be used for evaluation on the hidden test set.

### Table 2 (p. 7)

**Table 2:** QA Dev results using Base size models. We report accuracy for WikiHop and F1 for HotpotQA, Natural Questions, and TriviaQA.

| Model | HotpotQA Ans | HotpotQA Sup | HotpotQA Joint | NaturalQ LA | NaturalQ SA | TriviaQA Full | WikiHop MCQ |
|---|---|---|---|---|---|---|---|
| RoBERTa | 73.5 | 83.4 | 63.5 | - | - | 74.3 | 72.4 |
| Longformer | 74.3 | 84.4 | 64.4 | - | - | 75.2 | 75.0 |
| BIGBIRD-ITC | **75.7** | 86.8 | 67.7 | 70.8 | 53.3 | **79.5** | **75.9** |
| BIGBIRD-ETC | 75.5 | **87.1** | **67.8** | **73.9** | **54.9** | 78.7 | **75.9** |

### Table 3 (p. 7)

**Table 3:** Fine-tuning results on **Test** set for QA tasks. The Test results (F1 for HotpotQA, Natural Questions, TriviaQA, and Accuracy for WikiHop) have been picked from their respective leaderboard. For each task the top-3 leaders were picked not including BIGBIRD-etc.

> "For **Natural Questions Long Answer (LA), TriviaQA, and WikiHop, BIGBIRD-ETC is the new state-of-the-art**. On HotpotQA we are third in the leaderboard by F1 and second by Exact Match (EM)." [p. 7]

| Model | HotpotQA Ans | HotpotQA Sup | HotpotQA Joint | NaturalQ LA | NaturalQ SA | TriviaQA Full | TriviaQA Verified | WikiHop MCQ |
|---|---|---|---|---|---|---|---|---|
| HGN [26] | **82.2** | 88.5 | **74.2** | - | - | - | - | - |
| GSAN | 81.6 | 88.7 | 73.9 | - | - | - | - | - |
| ReflectionNet [32] | - | - | - | 77.1 | **64.1** | - | - | - |
| RikiNet-v2 [61] | - | - | - | 76.1 | 61.3 | - | - | - |
| Fusion-in-Decoder [39] | - | - | - | - | - | 84.4 | 90.3 | - |
| SpanBERT [42] | - | - | - | - | - | 79.1 | 86.6 | - |
| MRC-GCN [87] | - | - | - | - | - | - | - | 78.3 |
| MultiHop [14] | - | - | - | - | - | - | - | 76.5 |
| Longformer [8] | 81.2 | 88.3 | 73.2 | - | - | 77.3 | 85.3 | 81.9 |
| BIGBIRD-ETC | 81.2 | **89.1** | 73.6 | **77.8** | 57.9 | **84.5** | **92.4** | **82.3** |

## Classification

[p. 8] They tackle long document classification where discriminating information may not be located in the first 512 tokens. Following BERT, they use one layer with cross entropy loss on top of the first [CLS] token. They observe that gains of using BIGBIRD are more significant when there are longer documents and fewer training examples. For instance, using base sized model, BIGBIRD improves state-of-the-art for Arxiv dataset by about **5% points**. On Patents dataset, there is improvement over using simple BERT/RoBERTa, but given the large size of training data the improvement over SoTA (which is not BERT based) is not significant. This performance gain is not seen for the much smaller IMDb dataset. Detailed results with experimental setup detail are presented in App. E.4 which show competitive performance. [p. 8]

## 4.1 Encoder-Decoder Tasks [p. 8-9]

[p. 8] For an encoder-decoder setup, both encoder and decoder suffer from quadratic complexity due to full self-attention. The authors focus on introducing the sparse attention mechanism of BIGBIRD only at the encoder side. This is because, in practical generative applications, the length of the output sequence is typically small as compared to the input. For example, for text summarization (c.f. App. E.5, Tab. 18) the median output sequence length is ~200 where as the input sequence's median length is > 3000. For such applications, it is more efficient to use sparse attention mechanism for the encoder and full self-attention for the decoder. [p. 8-9]

### Summarization

[p. 9] Document summarization is a task of creating a short and accurate summary of a text document. They used three long document datasets for testing their model, details of which are mentioned in Tab. 18. They focus on abstractive summarization of long documents where using a longer contextual encoder should improve performance. The reasons are two-fold: First, the salient content can be evenly distributed in the long document, not just in the first 512 tokens, and this is by design in the BigPatents dataset [78]. Second, longer documents exhibit a richer discourse structure and summaries are considerably more abstractive, thereby observing more context helps.

As has been pointed out recently [76, 107], pretraining helps in generative tasks; they warm start from their general purpose MLM pretraining on base-sized models as well as utilizing state-of-the-art summarization specific pretraining from Pegasus [107] on large-sized models. The results of training BIGBIRD sparse encoder along with full decoder on these long document datasets are presented in Tab. 4. Modeling longer context brings significant improvement. Along with hyperparameters, they also present results on shorter but more widespread datasets in App. E.5 which show that using sparse attention does not hamper performance either. [p. 9]

### Table 4 (p. 8)

**Table 4:** Summarization ROUGE score for long documents.

| | | Arxiv | | | PubMed | | | BigPatent | | |
|---|---|---|---|---|---|---|---|---|---|---|
| | Model | R-1 | R-2 | R-L | R-1 | R-2 | R-L | R-1 | R-2 | R-L |
| Prior Art | SumBasic [68] | 29.47 | 6.95 | 26.30 | 37.15 | 11.36 | 33.43 | 27.44 | 7.08 | 23.66 |
| | LexRank [25] | 33.85 | 10.73 | 28.99 | 39.19 | 13.89 | 34.59 | 35.57 | 10.47 | 29.03 |
| | LSA [97] | 29.91 | 7.42 | 25.67 | 33.89 | 9.93 | 29.70 | - | - | - |
| | Attn-Seq2Seq [85] | 29.30 | 6.00 | 25.56 | 31.55 | 8.52 | 27.38 | 28.74 | 7.87 | 24.66 |
| | Pntr-Gen-Seq2Seq [77] | 32.06 | 9.04 | 25.16 | 35.86 | 10.22 | 29.69 | 33.14 | 11.63 | 28.55 |
| | Long-Doc-Seq2Seq [20] | 35.80 | 11.05 | 31.80 | 38.93 | 15.37 | 35.21 | - | - | - |
| | Sent-CLF [81] | 34.01 | 8.71 | 30.41 | 45.01 | 19.91 | 41.16 | 36.20 | 10.99 | 31.83 |
| | Sent-PTR [81] | 42.32 | 15.63 | 38.06 | 43.30 | 17.92 | 39.47 | 34.21 | 10.78 | 30.07 |
| | Extr-Abst-TLM [81] | 41.62 | 14.69 | 38.03 | 42.13 | 16.27 | 39.21 | 38.65 | 12.31 | 34.09 |
| | Dancer [31] | 42.70 | 16.54 | 38.44 | 44.09 | 17.69 | 40.27 | - | - | - |
| Base | Transformer | 28.52 | 6.70 | 25.58 | 31.71 | 8.32 | 29.42 | 39.66 | 20.94 | 31.20 |
| | + RoBERTa [76] | 31.98 | 8.13 | 29.53 | 35.77 | 13.85 | 33.32 | 41.11 | 22.10 | 32.58 |
| | + Pegasus [107] | 34.81 | 10.16 | 30.14 | 39.98 | 15.15 | 35.89 | 43.55 | 20.43 | 31.80 |
| | BIGBIRD-RoBERTa | 41.22 | 16.43 | **36.96** | 43.70 | 19.32 | **39.99** | **55.69** | **37.27** | **45.56** |
| Large | Pegasus (Reported) [107] | 44.21 | 16.95 | 38.83 | 45.97 | 20.15 | 41.34 | 52.29 | 33.08 | 41.75 |
| | Pegasus (Re-eval) | 43.85 | 16.83 | 39.17 | 44.53 | 19.30 | 40.70 | 52.25 | 33.04 | 41.80 |
| | BIGBIRD-Pegasus | **46.63** | **19.02** | **41.77** | **46.32** | **20.65** | **42.33** | **60.64** | **42.46** | **50.01** |
