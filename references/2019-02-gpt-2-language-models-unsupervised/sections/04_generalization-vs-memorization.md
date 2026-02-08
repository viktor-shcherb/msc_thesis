# 4. Generalization vs Memorization [p. 8-9]

[p. 8] Recent work in computer vision has shown that common image datasets contain a non-trivial amount of near-duplicate images. For instance CIFAR-10 has 3.3% overlap between train and test images (Barz & Denzler, 2019). This results in an over-reporting of the generalization performance of machine learning systems. As the size of datasets increases this issue becomes increasingly likely which suggests a similar phenomena could be happening with WebText. Therefore it is important to analyze how much test data also shows up in the training data.

## Overlap detection method

[p. 8] To study this the authors created Bloom filters containing 8-grams of WebText training set tokens. To improve recall, strings were normalized to contain only lower-cased alphanumeric words with a single space as a delimiter. The Bloom filters were constructed such that the false positive rate is upper bounded by 1/10^8. They further verified the low false positive rate by generating 1M strings, of which zero were found by the filter. [p. 8]

These Bloom filters let the authors calculate, given a dataset, the percentage of 8-grams from that dataset that are also found in the WebText training set.

**Table 6** (p. 8): "Percentage of test set 8 grams overlapping with training sets."

|               | PTB      | WikiText-2 | enwik8   | text8    | Wikitext-103 | 1BW      |
|---------------|----------|------------|----------|----------|-------------|----------|
| Dataset train | **2.67%** | 0.66%      | **7.50%** | 2.34%    | **9.09%**   | **13.19%** |
| WebText train | 0.88%    | **1.63%**  | 6.31%    | **3.94%** | 2.42%       | 3.75%    |

[p. 8] Common LM datasets' test sets have between 1-6% overlap with WebText train, with an average of overlap of 3.2%. Somewhat surprisingly, many datasets have larger overlaps with their own training splits, with an average of 5.9% overlap.

## Manual inspection and specific dataset overlaps

[p. 8] The approach optimizes for recall, and while manual inspection shows many common phrases, there are many longer matches that are due to duplicated data. This is not unique to WebText. For instance, the test set of WikiText-103 has an article which is also in the training dataset. Since there are only 60 articles in the test set there is at least an overlap of 1.6%. Potentially more worryingly, 1BW has an overlap of nearly 13.2% with its own training set according to this procedure. [p. 8]

For the Winograd Schema Challenge, only 10 schemata had any 8-gram overlaps with the WebText training set. Of these, 2 were spurious matches. Of the remaining 8, only 1 schema appeared in any contexts that gave away the answer. [p. 8-9]

For CoQA, about 15% of documents in the news domain are already in WebText and the model performs about 3 F1 better on these. CoQA's development set metric reports the average performance over 5 different domains and the authors measure a gain of about 0.5-1.0 F1 due to overlap across the various domains. However, no actual training questions or answers are in WebText since CoQA was released after the cutoff date for links in WebText. [p. 9]

On LAMBADA, the average overlap is 1.2%. GPT-2 performs about 2 perplexity better on examples with greater than 15% overlap. Recalculating metrics when excluding all examples with any overlap shifts results from 8.6 to 8.7 perplexity and reduces accuracy from 63.2% to 62.9%. This very small change in overall results is likely due to only 1 in 200 examples having significant overlap. [p. 9]

## Summary of overlap analysis

[p. 9] Overall, the analysis suggests that data overlap between WebText training data and specific evaluation datasets provides a small but consistent benefit to reported results. However, for most datasets the authors do not notice significantly larger overlaps than those already existing between standard training and test sets, as Table 6 highlights.

Understanding and quantifying how highly similar text impacts performance is an important research question. Better de-duplication techniques such as scalable fuzzy matching could also help better answer these questions. For now, the authors recommend the use of n-gram overlap based de-duplication as an important verification step and sanity check during the creation of training and test splits for new NLP datasets. [p. 9]

## Memorization analysis via held-out performance

[p. 9] Another potential way of determining whether the performance of WebText LMs is attributable to memorization is inspecting their performance on their own held-out set. As shown in Figure 4, performance on both the training and test sets of WebText are similar and improve together as model size is increased. This suggests even GPT-2 is still underfitting on WebText in many ways. [p. 9]

**Figure 4** (p. 9): "The performance of LMs trained on WebText as a function of model size."

X-axis: # of parameters in LM (117M, 345M, 762M, 1542M). Y-axis: Perplexity. Two lines: WebText train (blue) and WebText test (orange). Both lines decrease together as model size grows: from approximately 16/17 at 117M down to approximately 10/11 at 1542M. The train and test curves are close together throughout, with the test set only slightly higher, indicating the model is not memorizing. [p. 9]

GPT-2 is also able to write news articles about the discovery of talking unicorns. An example is provided in Table 13. [p. 9]
