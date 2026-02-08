# Experiments and Evaluation [p. 8–11]

[p. 8] The proposed RoFormer is evaluated on various NLP tasks. The performance of the proposed solution is validated on machine translation (Section 4.1). Then, the RoPE implementation is compared with BERT Devlin et al. [2019] during the pre-training stage (Section 4.2). Based on the pre-trained model, evaluations across different downstream tasks from GLUE benchmark Singh et al. [2018] are carried out (Section 4.3). Experiments using the proposed RoPE with the linear attention of PerFormer Choromanski et al. [2020] are conducted (Section 4.4). Additional tests on Chinese data are included (Section 4.5). All experiments were run on two cloud servers with 4 x V100 GPUs.

## Machine Translation

### Experimental Settings

[p. 9] The standard WMT 2014 English-German dataset Bojar et al. [2014] is chosen, which consists of approximately 4.5 million sentence pairs. The transformer-based baseline alternative Vaswani et al. [2017] is used for comparison.

### Implementation details

[p. 9] Modifications on the self-attention layer of the baseline model Vaswani et al. [2017] are made to enable RoPE in its learning process. The setup for English-to-German translation uses a vocabulary of 37k based on a joint source and target byte pair encoding (BPE) Sennrich et al. [2015]. During the evaluation, a single model is obtained by averaging the last 5 checkpoints. The result uses beam search with a beam size of 4 and length penalty 0.6. The experiment is implemented in PyTorch in the fairseq toolkit (MIT License) Ott et al. [2019]. The model is optimized with the Adam optimizer using $\beta_1 = 0.9$, $\beta_2 = 0.98$, learning rate is increased linearly from $1e{-}7$ to $5e{-}4$ and then decayed proportionally to the inverse square root of the step number. Label smoothing with 0.1 is also adopted. The BLEU Papineni et al. [2002] score on the test set is reported as the final metric.

### Results

[p. 9] The baseline model and RoFormer are trained under the same settings and results are reported in Table 1. RoFormer gives better BLEU scores compared to the baseline Transformer.

**Table 1** (p. 9): "The proposed RoFormer gives better BLEU scores compared to its baseline alternative Vaswani et al. [2017] on the WMT 2014 English-to-German translation task Bojar et al. [2014]."

| Model | BLEU |
|---|---|
| Transformer-base Vaswani et al. [2017] | 27.3 |
| RoFormer | **27.5** |

## Pre-training Language Modeling

[p. 9] The second experiment validates the performance of the proposal in terms of learning contextual representations. The original sinusoidal position encoding of BERT is replaced with RoPE during the pre-training step.

### Experimental Settings

[p. 9] The BookCorpus Zhu et al. [2015] and the Wikipedia Corpus Foundation [2021] from Huggingface Datasets library (Apache License 2.0) are used for pre-training. The corpus is further split into train and validation sets at 8:2 ratio. The masked language-modeling (MLM) loss values of the training process are used as an evaluation metric. The well-known BERT Devlin et al. [2019] is adopted as the baseline model. Note that bert-base-uncased is used in the experiments.

### Implementation details

[p. 9] The sinusoidal position encoding in the self-attention block of the baseline model is replaced with the proposed RoPE and self-attention is realized according to Equation (16). Both BERT and RoFormer are trained with batch size 64 and maximum sequence length of 512 for 100k steps. AdamW Loshchilov and Hutter [2017] is used as the optimizer with learning rate 1e-5.

### Results

[p. 9] The MLM loss during pre-training is shown on the left plot of Figure 3. Compared to the vanilla BERT, RoFormer experiences faster convergence.

**Figure 3** (p. 10): "Evaluation of RoPE in language modeling pre-training. **Left**: training loss for BERT and RoFormer. **Right**: training loss for PerFormer with and without RoPE."
The figure contains two side-by-side line plots. The left plot shows MLM Loss (y-axis, range approximately 2-10) vs Train Steps (K) (x-axis, range 0-250). Two curves are shown: RoFormer (blue/green) and BERT (orange/red). Both start around 10 and decrease, but RoFormer converges faster, reaching lower loss values earlier. Both converge to approximately 2 by 250K steps. The right plot shows LM Loss (y-axis, range approximately 1.3-3.2) vs Train Steps (K) (x-axis, range 0-100). Two curves are shown: PerFormer w/. RoPE and PerFormer w/o. RoPE. The PerFormer with RoPE achieves lower loss and converges faster than the PerFormer without RoPE.

## Fine-tuning on GLUE tasks

[p. 10] Consistent with the previous experiments, the weights of the pre-trained RoFormer are fine-tuned across various GLUE tasks in order to evaluate its generalization ability on downstream NLP tasks.

### Experimental Settings

[p. 10] Several datasets from GLUE are used: MRPC Dolan and Brockett [2005], SST-2 Socher et al. [2013], QNLI Rajpurkar et al. [2016], STS-B Al-Natsheh et al. [2017], QQP Chen et al. [2018b] and MNLI Williams et al. [2018]. F1-score is used for MRPC and QQP dataset, spearman correlation for STS-B, and accuracy for the remaining as the evaluation metrics.

### Implementation details

[p. 10] Huggingface Transformers library (Apache License 2.0) Wolf et al. [2020] is used to fine-tune each of the aforementioned downstream tasks for 3 epochs, with a maximum sequence length of 512, batch size of 32 and learning rates 2,3,4,5e-5. Following Devlin et al. [2019], the best-averaged results on the validation set are reported.

### Results

[p. 10] The evaluation results of the fine-tuning tasks are reported in Table 2. RoFormer can significantly outperform BERT in three out of six datasets, and the improvements are considerable.

**Table 2** (p. 10): "Comparing RoFormer and BERT by fine tuning on downstream GLEU tasks."

| Model | MRPC | SST-2 | QNLI | STS-B | QQP | MNLI(m/mm) |
|---|---|---|---|---|---|---|
| BERT Devlin et al. [2019] | 88.9 | 93.5 | 90.5 | 85.8 | 71.2 | 84.6/83.4 |
| RoFormer | **89.5** | 90.7 | 88.0 | **87.0** | **86.4** | 80.2/79.8 |

## Performer with RoPE

[p. 10] Performer Choromanski et al. [2020] introduces an alternative attention mechanism, linear attention, which is designed to avoid quadratic computation cost that scales with input sequence length. As discussed in Section 3.3, the proposed RoPE can be easily implemented in the PerFormer model to realize the relative position encoding while keeping its linearly scaled complexity in self-attention. Its performance is demonstrated with the pre-training task of language modeling.

### Implementation details

[p. 11] Tests are carried out on the Enwik8 dataset Mahoney [2006], which is from English Wikipedia that includes markup, special characters and text in other languages in addition to English text. RoPE is incorporated into the 12 layer char-based PerFormer with 768 dimensions and 12 heads. To better illustrate the efficacy of RoPE, the loss curves of the pre-training process with and without RoPE are reported under the same settings, i.e., learning rate 1e-4, batch size 128 and a fixed maximum sequence length of 1024, etc. Code adopted from https://github.com/lucidrains/performer-pytorch (MIT License).

### Results

[p. 11] As shown on the right plot of Figure 3, substituting RoPE into Performer leads to rapid convergence and lower loss under the same amount of training steps. These improvements, in addition to the linear complexity, make Performer more attractive.

## Evaluation on Chinese Data

[p. 11] In addition to experiments on English data, additional results on Chinese data are shown. To validate the performance of RoFormer on long texts, experiments on long documents whose length exceeds 512 characters are conducted.

### Implementation

[p. 11] Modifications on WoBERT Su [2020] are carried out by replacing the absolute position embedding with the proposed RoPE. As a cross-comparison with other pre-trained Transformer-based models in Chinese, i.e. BERT Devlin et al. [2019], WoBERT Su [2020], and NEZHA Wei et al. [2019], their tokenization level and position embedding information is tabulated in Table 3.

**Table 3** (p. 11): "Cross-comparison between our RoFormer and other pre-trained models on Chinese data. 'abs' and 'rel' annotates absolute position embedding and relative position embedding, respectively."

| Model | BERT Devlin et al. [2019] | WoBERT Su [2020] | NEZHA Wei et al. [2019] | RoFormer |
|---|---|---|---|---|
| Tokenization level | char | word | char | word |
| Position embedding | abs. | abs. | rel. | RoPE |

### Pre-training

[p. 11] RoFormer is pre-trained on approximately 34GB of data collected from Chinese Wikipedia, news and forums. The pre-training is carried out in multiple stages with changing batch size and maximum input sequence length in order to adapt the model to various scenarios. As shown in Table 4, the accuracy of RoFormer elevates with an increasing upper bound of sequence length, which demonstrates the ability of RoFormer in dealing with long texts. The authors claim that this is the attribute to the excellent generalizability of the proposed RoPE.

**Table 4** (p. 11): "Pre-training strategy of RoFormer on Chinese dataset. The training procedure is divided into various consecutive stages. In each stage, we train the model with a specific combination of maximum sequence length and batch size."

| Stage | Max seq length | Batch size | Training steps | Loss | Accuracy |
|---|---|---|---|---|---|
| 1 | 512 | 256 | 200k | 1.73 | 65.0% |
| 2 | 1536 | 256 | 12.5k | 1.61 | 66.8% |
| 3 | 256 | 256 | 120k | 1.75 | 64.6% |
| 4 | 128 | 512 | 80k | 1.83 | 63.4% |
| 5 | 1536 | 256 | 10k | 1.58 | 67.4% |
| 6 | 512 | 512 | 30k | 1.66 | 66.2% |

### Downstream Tasks & Dataset

[p. 11–12] The Chinese AI and Law 2019 Similar Case Matching (CAIL2019-SCM) Xiao et al. [2019] dataset is chosen to illustrate the ability of RoFormer in dealing with long texts, i.e., semantic text matching. CAIL2019-SCM contains 8964 triplets of cases published by the Supreme People's Court of China. The input triplet, denoted as (A, B and C), are fact descriptions of three cases. The task is to predict whether the pair (A, B) is closer than (A, C) under a predefined similarity measure. Existing methods mostly cannot perform significantly on CAIL2019-SCM dataset due to the length of documents (i.e., mostly more than 512 characters). The data is split into train, validation and test sets based on the well-known ratio 6:2:2.

### Results

[p. 12] The pre-trained RoFormer model is applied to CAIL2019-SCM with different input lengths. The model is compared with the pre-trained BERT and WoBERT model on the same pre-training data, as shown in Table 5. With short text cut-offs, i.e., 512, the result from RoFormer is comparable to WoBERT and is slightly better than the BERT implementation. However, when increasing the maximum input text length to 1024, RoFormer outperforms WoBERT by an absolute improvement of 1.5%.

**Table 5** (p. 12): "Experiment results on CAIL2019-SCM task. Numbers in the first column denote the maximum cut-off sequence length. The results are presented in terms of percent accuracy."

| Model | Validation | Test |
|---|---|---|
| BERT-512 | 64.13% | 67.77% |
| WoBERT-512 | 64.07% | 68.10% |
| **RoFormer-512** | **64.13%** | **68.29%** |
| **RoFormer-1024** | **66.07%** | **69.79%** |

### Limitations of the work

[p. 12] Although the authors provide theoretical groundings as well as promising experimental justifications, the method is limited by the following facts:

- Despite the fact that they mathematically format the relative position relations as rotations under 2D sub-spaces, there lacks thorough explanations on why it converges faster than baseline models that incorporate other position encoding strategies.
- Although they have proved that the model has favourable property of long-term decay for inter-token products, Section (3.3), which is similar to the existing position encoding mechanisms, the model shows superior performance on long texts than peer models, but they have not come up with a faithful explanation.

The proposed RoFormer is built upon the Transformer-based infrastructure, which requires hardware resources for pre-training purpose.
