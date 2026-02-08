# 3 Are All Attention Heads Important? [p. 3-5]

The authors perform a series of experiments in which they remove one or more attention heads from a given architecture at test time and measure the performance difference. They first remove a single attention head at each time (Section 3.2) and then remove every head in an entire layer except for one (Section 3.3).

## 3.1 Experimental Setup [p. 3]

Two trained models are considered in all following experiments:

**WMT:** The original "large" transformer architecture from Vaswani et al. (2017) with 6 layers and 16 heads per layer, trained on the WMT2014 English to French corpus. They use the pretrained model of Ott et al. (2018) and report BLEU scores on the `newstest2013` test set. In accordance with Ott et al. (2018), BLEU scores are computed on the tokenized output of the model using Moses (Koehn et al., 2007). Statistical significance is tested with paired bootstrap resampling (Koehn, 2004) using `compare-mt` (Neubig et al., 2019) with 1000 resamples. A particularity of this model is that it features 3 distinct attention mechanisms: encoder self-attention (Enc-Enc), encoder-decoder attention (Enc-Dec) and decoder self-attention (Dec-Dec), all of which use MHA.

**BERT:** BERT (Devlin et al., 2018) is a single transformer pre-trained on an unsupervised cloze-style "masked language modeling task" and then fine-tuned on specific tasks. They use the pre-trained `base-uncased` model of Devlin et al. (2018) with 12 layers and 12 attention heads which they fine-tune and evaluate on MultiNLI (Williams et al., 2018). They report accuracies on the "matched" validation set. Statistical significance is tested using the t-test. In contrast with the WMT model, BERT only features one attention mechanism (self-attention in each layer).

## 3.2 Ablating One Head [p. 3-4]

To understand the contribution of a particular attention head $h$, the model's performance is evaluated while masking that head (i.e. replacing $\text{Att}_h(x)$ with zeros). If the performance sans $h$ is significantly worse than the full model's, $h$ is obviously important; if the performance is comparable, $h$ is redundant given the rest of the model.

**Figure 1** (p. 3): "Distribution of heads by model score after masking."
- (a) WMT: Histogram showing #heads (y-axis, 0-80) vs. BLEU score (x-axis, ~35.5-36.3). Dashed red line marks baseline BLEU. The majority of heads cluster near the baseline score, with most heads having little effect when removed. Some heads result in slightly higher BLEU when removed.
- (b) BERT: Histogram showing #heads (y-axis, 0-40+) vs. Accuracy (x-axis, ~0.824-0.838). Dashed red line marks baseline accuracy. Similar pattern: most heads cluster around baseline, with removing some heads yielding slight accuracy gains.

Key observation: the majority of attention heads can be removed without deviating too much from the original score. Surprisingly, in some cases removing an attention head results in an increase in BLEU/accuracy.

**Table 1** (p. 4): "Difference in BLEU score for each head of the encoder's self attention mechanism. Underlined numbers indicate that the change is statistically significant with $p < 0.01$. The base BLEU score is 36.05."

| Layer | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|-------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| 1 | 0.03 | 0.07 | 0.05 | -0.06 | 0.03 | **-0.53** | 0.09 | **-0.33** | 0.06 | 0.03 | 0.11 | 0.04 | 0.01 | -0.04 | 0.04 | 0.00 |
| 2 | 0.01 | 0.04 | 0.10 | **0.20** | 0.06 | 0.03 | 0.00 | 0.09 | 0.10 | 0.04 | **0.15** | 0.03 | 0.05 | 0.04 | 0.14 | 0.04 |
| 3 | 0.05 | -0.01 | 0.08 | 0.09 | 0.11 | 0.02 | 0.03 | 0.03 | -0.00 | 0.13 | 0.09 | 0.09 | -0.11 | **0.24** | 0.07 | -0.04 |
| 4 | -0.02 | 0.03 | 0.13 | 0.06 | -0.05 | 0.13 | 0.14 | 0.05 | 0.02 | 0.14 | 0.05 | 0.06 | 0.03 | -0.06 | -0.10 | -0.06 |
| 5 | **-0.31** | -0.11 | -0.04 | 0.12 | 0.10 | 0.02 | 0.09 | 0.08 | 0.04 | **0.21** | -0.02 | 0.02 | -0.03 | -0.04 | 0.07 | -0.02 |
| 6 | 0.06 | 0.07 | **-0.31** | 0.15 | -0.19 | 0.15 | 0.11 | 0.05 | 0.01 | -0.08 | 0.06 | 0.01 | 0.01 | 0.02 | 0.07 | 0.05 |

Only 8 (out of 96) heads cause a statistically significant change in performance when removed from the encoder self-attention. Half of those actually result in a higher BLEU score when removed. This leads to the first observation:

> **"at test time, most heads are redundant given the rest of the model"** [p. 4]

## 3.3 Ablating All Heads but One [p. 4-5]

The question: is more than one head even needed? The authors compute the difference in performance when all heads except one are removed, within a single layer. Tables 2 and 3 report the best score for each layer in the model (i.e. the score when reducing the entire layer to the single most important head).

**Table 2** (p. 4): "Best delta BLEU by layer when only one head is kept in the WMT model. Underlined numbers indicate that the change is statistically significant with $p < 0.01$."

| Layer | Enc-Enc | Enc-Dec | Dec-Dec |
|-------|---------|---------|---------|
| 1 | **-1.31** | **0.24** | -0.03 |
| 2 | -0.16 | 0.06 | 0.12 |
| 3 | 0.12 | 0.05 | 0.18 |
| 4 | -0.15 | -0.24 | 0.17 |
| 5 | 0.02 | **-1.55** | -0.04 |
| 6 | **-0.36** | **-13.56** | 0.24 |

**Table 3** (p. 4): "Best delta accuracy by layer when only one head is kept in the BERT model. None of these results are statistically significant with $p < 0.01$."

| Layer | | Layer | |
|-------|--------|-------|--------|
| 1 | -0.01% | 7 | 0.05% |
| 2 | 0.10% | 8 | -0.72% |
| 3 | -0.14% | 9 | -0.96% |
| 4 | -0.53% | 10 | 0.07% |
| 5 | -0.29% | 11 | -0.19% |
| 6 | -0.52% | 12 | -0.12% |

Key findings:
- For most layers, one head is indeed sufficient at test time, even though the network was trained with 12 or 16 attention heads. These layers can be reduced to single-headed attention with only 1/16th (resp. 1/12th) of the number of parameters of a vanilla attention layer.
- Some layers *do* require multiple attention heads; e.g., substituting the last layer in the encoder-decoder attention of WMT with a single head degrades performance by at least **13.5 BLEU points**.
- Additionally, when selecting the best head on a validation set (`newstest2013` for WMT, 5,000-sized randomly selected subset of training set of MNLI for BERT) and evaluating on a test set (`newstest2014` for WMT, MNLI-matched validation set for BERT), similar findings hold: keeping only one head does not result in a statistically significant change in performance for 50% (resp. 100%) of layers of WMT (resp. BERT). [p. 5]

## 3.4 Are Important Heads the Same Across Datasets? [p. 5]

Caveat: the results in Sections 3.2/3.3 are only valid on specific (and rather small) test sets. To understand whether some heads are universally important, the same ablation study is performed on a second, out-of-domain test set: the MNLI "mismatched" validation set for BERT, and the MTNT English to French test set (Michel and Neubig, 2018) for WMT. Both have been assembled for the purpose of providing contrastive, out-of-domain test suites.

**Figure 2** (p. 5): "Cross-task analysis of effect of pruning on accuracy"
- (a) BLEU on `newstest2013` (x-axis, ~35.5-36.3) vs. BLEU on MTNT (y-axis, ~30.5-33.0) when individual heads are removed from WMT. Pearson $r = 0.56$. Note the ranges are not the same on X and Y axis; there is much more variation on MTNT. Original BLEU scores marked with a star.
- (b) Accuracy on MNLI-matched (x-axis, ~0.823-0.840) vs. Accuracy on MNLI-mismatched (y-axis, ~0.825-0.843) when individual heads are removed from BERT. Pearson $r = 0.68$. Scores remain in the same approximate range of values. Original accuracies marked with a star.

There is a positive, $> 0.5$ correlation ($p < 001$) between the effect of removing a head on both datasets. Moreover, heads that have the highest effect on performance on one domain tend to have the same effect on the other, suggesting that the most important heads from Section 3.2 are indeed "universally" important.
