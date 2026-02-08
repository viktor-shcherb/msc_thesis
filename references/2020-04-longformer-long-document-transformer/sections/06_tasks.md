# Tasks [p. 7-9]

[p. 7] Longformer is applied to multiple long document tasks, including QA, coreference resolution and classification. Tab. 6 shows the evaluation datasets have contexts significantly longer than 512 wordpieces. The primary goal is to evaluate whether the attention mechanism can act as a replacement for the standard self-attention mechanism in BERT style models, and to perform controlled trials against a strong baseline. The authors are also interested in evaluating whether complicated task specific models necessitated by BERT's limited context can be replaced with simpler models that just concatenate all available context into a single sequence.

The baseline is a RoBERTa based model that breaks the context into the longest possible segment, passes each individually through RoBERTa, and concatenates the activations for further processing. For QA tasks, the question is also concatenated to each segment so that RoBERTa can condition its contextual representations of the context on the question. The Longformer variant replaces the RoBERTa self-attention mechanism with the windowed attention used during pretraining, plus a task motivated global attention. The global attention uses additional linear projections (section 3.1).

### Table 6: Average and 95th percentile of context length of datasets in wordpieces [p. 7]

WH: WikiHop, TQA: TriviaQA, HQA: HotpotQA, ON: OntoNotes, HY: Hyperpartisan news

| Wordpieces | WH | TQA | HQA | ON | IMDB | HY |
|---|---|---|---|---|---|---|
| avg. | 1,535 | 6,589 | 1,316 | 506 | 300 | 705 |
| 95th pctl. | 3,627 | 17,126 | 1,889 | 1,147 | 705 | 1,975 |

## 6.1 Question Answering

[p. 7] Three datasets are used: WikiHop (Welbl et al., 2018), TriviaQA (Joshi et al., 2017, Wikipedia setting), and HotpotQA (Yang et al., 2018, distractor setting).^7

^7 The full version of TriviaQA and HotpotQA are used, not the simplified versions in MRQA (Fisch et al., 2019). [p. 7, footnote 7]

**WikiHop and TriviaQA:** Follow the simple QA model of BERT (Devlin et al., 2019), and concatenate question and documents into one long sequence, run it through Longformer, then have a dataset-specific prediction layer. WikiHop uses a classification layer for the candidate while TriviaQA uses the loss function of Clark and Gardner (2017) to predict answer span. Global attention is included on question tokens and answer candidates for WikiHop and on question tokens for TriviaQA.

**HotpotQA:** A multihop QA dataset that involves extracting answer spans and evidence sentences from 10 Wikipedia paragraphs, 2 of which are relevant and the rest are distractors. A two-stage model is used that first selects the most relevant paragraphs then passes them to a second stage for answer extraction. Both stages concatenate question and context into one sequence, run it through Longformer, then use task-specific prediction layers. The models are trained in a multi-task way to predict relevant paragraphs, evidence sentences, answer spans and question types (yes/no/span) jointly. This model is simpler than recent SOTA models that include complex task-specific architectures (e.g., Tu et al., 2019; Chen et al., 2019; Tu et al., 2020; Groeneveld et al., 2020). See Appendix D for further details about the models and hyperparameters.

## 6.2 Coreference Resolution

[p. 7-8] OntoNotes (Pradhan et al., 2012) is used, and the model from Joshi et al. (2019), a modification of the system from Lee et al. (2018) to replace ELMo with BERT. The Longformer system is a straightforward adaption of the baseline model by replacing RoBERTa with Longformer and extending the sequence length. Global attention is not used for this task.

## 6.3 Document Classification

[p. 8] Evaluation on IMDB (Maas et al., 2011) and Hyperpartisan news detection (Kiesel et al., 2019) datasets.^8

^8 For Hyperpartisan the training data is split into 80/10/10 train/dev/test sets, and mean F1 across five seeds is reported. [p. 8, footnote 8]

IMDB is a standard sentiment classification dataset consisting of movie reviews. While most documents are short, about 13.6% of them are larger than 512 wordpieces (Tab. 6). Documents in Hyperpartisan are relatively long, and it is small with only 645 documents making it a good test for Longformer's ability to adapt to limited data. Global attention is used on the `[CLS]` token.

## 6.4 Results

### Table 7: Summary of finetuning results on QA, coreference resolution, and document classification [p. 8]

Results are on the development sets comparing Longformer-base with RoBERTa-base. TriviaQA, Hyperpartisan metrics are F1, WikiHop and IMDB use accuracy, HotpotQA is joint F1, OntoNotes is average F1.

| Model | WikiHop | TriviaQA | HotpotQA | OntoNotes | IMDB | Hyperpartisan |
|---|---|---|---|---|---|---|
| RoBERTa-base | 72.4 | 74.3 | 63.5 | 78.4 | 95.3 | 87.4 |
| Longformer-base | **75.0** | **75.2** | **64.4** | **78.6** | **95.7** | **94.8** |

[p. 8] **Main Result:** Longformer consistently outperforms the RoBERTa baseline. Its performance gain is especially obvious for tasks that require long context such as WikiHop and Hyperpartisan. For TriviaQA, the improvement is more modest as the local context is often sufficient to answer the question. In the case of HotpotQA, the supporting fact auxiliary supervision allows models to easily find relevant contexts and then focus on local context, leading to smaller gains. This is contrasted with WikiHop that only includes distant supervision of intermediate reasoning chains, where the approach excels by reasoning over the entire context. On the IMDB and OntoNotes datasets the performance gains are smaller. For IMDB, the majority of the dataset consists of short documents and thus it is expected to see smaller improvements. For OntoNotes, the distance between any two mentions is typically quite small so that a baseline that processes smaller chunks separately is able to stitch together mentions into coreference chains without considering cross chunk interactions.

### Longformer-large for QA

[p. 8] The performance of Longformer-large on long context QA tasks is also evaluated. Tab. 8 shows that Longformer-large achieves new state-of-the-art results^9 on WikiHop and TriviaQA by large margins (3.6 and 4 points respectively), and for HotpotQA, it underperforms the current state-of-the-art (Fang et al., 2020) by a point.

^9 At submission time, May 2020. Later, BigBird (Zaheer et al., 2020) improved leaderboard results on these datasets. There are confounding factors such as using 16X more compute in BigBird's pretraining compared with Longformer, potentially affecting the performance. [p. 9, footnote 9]

### Table 8: Leaderboard results of Longformer-large at time of submission (May 2020) [p. 8]

All numbers are F1 scores.

| Model | WikiHop | TriviaQA | HotpotQA |
|---|---|---|---|
| Current^a SOTA | 78.3 | 73.3 | **74.2** |
| Longformer-large | **81.9** | **77.3** | 73.2 |

### Table 9: HotpotQA results in distractor setting test set [p. 9]

Quark's test results are not available. All numbers are F1 scores. ^dagger shows contemporaneous leaderboard submissions.

| Model | ans. | supp. | joint |
|---|---|---|---|
| TAP 2 (ensemble) (Glass et al., 2019) | 79.8 | 86.7 | 70.7 |
| SAE (Tu et al., 2019) | 79.6 | 86.7 | 71.4 |
| Quark (dev) (Groeneveld et al., 2020) | 81.2 | 87.0 | 72.3 |
| C2F Reader (Shao et al., 2020) | 81.2 | 87.6 | 72.8 |
| Longformer-large | 81.3 | 88.3 | 73.2 |
| ETC-large^dagger (Ainslie et al., 2020) | 81.2 | 89.1 | 73.6 |
| GSAN-large^dagger | 81.6 | 88.7 | 73.9 |
| HGN-large (Fang et al., 2020) | 82.2 | 88.5 | 74.2 |

[p. 8-9] Tab. 9 shows the detailed results of HotpotQA compared with published and unpublished concurrent models. Longformer places second on the published leaderboard, outperforming all other published results except for HGN (Fang et al., 2020). All published top performing models in this task (Tu et al., 2019; Fang et al., 2020; Shao et al., 2020) use GNNs (Kipf and Welling, 2017) or graph network of entities, which seem to encode an important inductive bias for the task and can potentially improve results further. Nevertheless, Longformer strongly outperforms all other methods including the recent non-GNN methods (Glass et al., 2019; Shao et al., 2020; Groeneveld et al., 2020).

## 6.5 Ablations on WikiHop

### Table 10: WikiHop development set ablations [p. 9]

| Model | Accuracy / Delta |
|---|---|
| Longformer (seqlen: 4,096) | 73.8 |
| RoBERTa-base (seqlen: 512) | 72.4 / -1.4 |
| Longformer (seqlen: 4,096, 15 epochs) | 75.0 / +1.2 |
| Longformer (seqlen: 512, attention: n^2) | 71.7 / -2.1 |
| Longformer (seqlen: 2,048) | 73.1 / -0.7 |
| Longformer (no MLM pretraining) | 73.2 / -0.6 |
| Longformer (no linear proj.) | 72.2 / -1.6 |
| Longformer (no linear proj. no global atten.) | 65.5 / -8.3 |
| Longformer (pretrain extra position embed. only) | 73.5 / -0.3 |

[p. 9] Tab. 10 presents an ablation study for WikiHop on the development set. All results use Longformer-base, fine-tuned for five epochs with identical hyperparameters except where noted. Key findings:

- Longformer benefits from longer sequences, global attention, separate projection matrices for global attention, MLM pretraining, and longer training.
- When configured as in RoBERTa-base (seqlen: 512, and n^2 attention) Longformer performs slightly worse than RoBERTa-base, confirming that performance gains are not due to additional pretraining.
- Performance drops slightly when using the RoBERTa model pretrained when only unfreezing the additional position embeddings, showing that Longformer can learn to use long range context in task specific fine-tuning with large training datasets such as WikiHop.
