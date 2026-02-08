# A.6 Dataset Contamination [p. 75–76]

[p. 75] With the increasing scale of publicly available training data, it has become inevitable that some portion of evaluation data is seen during training, and may provide an undue boost in evaluation performance.

## Prior Work on Measuring Contamination [p. 75]

[p. 75] Earlier work (Brown et al. (2020), Wei et al. (2022a), Du et al. (2022)) in measuring dataset contamination considered an example from an evaluation set to be "contaminated" if there existed a collision between a high-order *n*-gram (generally, *n* = 13) from the sample and the training data. This was a deliberately conservative approach in order to produce a "clean" subset of the data with high precision, and is used in open-sourced evaluation libraries (e.g. Gao et al. (2021)).

This approach, however, was unable to detect precisely what proportion of a given sample is contaminated. Furthermore, as noted in Chowdhery et al. (2022), some datasets (such as BoolQ) contain contexts extracted verbatim from the web, but not the question and answer continuation. As such, highly contaminated samples from these datasets are unlikely to gain an unfair advantage. The methodology in Chowdhery et al. (2022) further improves on the earlier *n*-gram collision detection by considering a sample to be contaminated if 70% of all 8-grams can be found at least once in the training data.

## Token-Level Contamination Approach [p. 75]

[p. 75] The previous methodologies noted above all consider contamination in text space, and do not appear to consider the formatting of prompts used for actual evaluation. In contrast, the authors instead match on tokenized input, being careful to pass fully verbalized evaluation samples to the tokenizer. They also diverge from previous methodologies by considering contamination from a bottom-up perspective. A token is considered to be contaminated if it appears in any token *n*-gram longer than 10 tokens in both the evaluation sample and the training set. The contamination percentage of a sample is defined as the percentage of tokens contaminated. This allows viewing benchmark performance of the models on a range of contamination scales, while retaining the ability to test a high-precision clean subset (samples with < 20% contamination) and a high-precision contaminated subset (samples with > 80% contamination). [p. 75]

To account for the vagaries of the precise format of verbalized samples, a small "skipgram budget" of four tokens is allowed, so that matched spans between an evaluation sample and the training data can differ in at most four positions (trailing mismatches, or mismatches in the first 10 tokens are not allowed).

Such 10(+)-skipgrams were identified with suffix arrays implemented using a variation of the library from Lee et al. (2022), modified to work on a PySpark cluster (effectively without random access to disk). Given the embarrassingly parallel nature of the task, all such 10-grams (and their full lengths) in the entire dataset were found in around seven hours (including time to tokenize), utilizing an estimated 1,500 cores. [p. 75]

## Contamination Subset Definitions [p. 75]

[p. 75] As there are many confounding factors at play when determining whether dataset contamination has contributed to evaluation performance (mostly stemming from the fact that "clean" and "dirty" subsets do not necessarily well-estimate the population distribution), the following assumption is made: In the event of dataset contamination contributing to evaluation performance, the "cleanest" examples are expected to have an overall *worse* average score than their complement, and the "dirtiest" samples are expected to have an overall *better* average score than their complement. It is insufficient evidence for contamination if only one of these were true. To this end, four (non-disjoint) subset types are defined as follows:

- *"Clean"* samples, with less than 20% token contamination,
- *"Not clean"* samples, with greater than (or equal to) 20% token contamination,
- *"Not dirty"* samples, with less than 80% token contamination,
- *"Dirty"* samples, with greater than (or equal to) 80% token contamination.

## Addressing Fragmented Matches [p. 75–76]

[p. 75–76] There is an additional confounding factor that is addressed directly. With the given definition of contamination, there is a possibility that a sample may appear contaminated, by virtue of many tokens appearing in matched sequences found in the training data. However, the matched sequences might be highly fragmented across the training data, in which case it is very unlikely the model saw the correctly-assembled contaminated sequences during training. To reduce the chance of this phenomenon, the analysis is repeated with minimum match length *L* in {10, 20, 30, 40, 50}. Since in the limit of *L* -> infinity every sample falls into both the "clean" and "not dirty" (there is no contamination), the largest *L* for each dataset that appeared to benefit from contamination is reported to strike a balance between fragmentation and overall contamination. [p. 76]

## Statistical Test [p. 76]

[p. 76] For each dataset and each of the above sample subset types, both the mean X-bar of the performance metric *X* and the statistic *Z_n* = (X-bar - mu_n) / sigma_n are computed, where *n* is the size of the sample subset type, and mu_n and sigma_n^2 are the mean and variance of the sampling distribution of the performance metric for samples of size *n*, respectively. By the Central Limit Theorem, *Z_n* tends towards a standard normal distribution and so there is sufficient evidence to suggest contamination has affected evaluation performance on a dataset if all four sample subsets have |*Z_n*| > 2.

## Results [p. 76]

[p. 76] Results for this analysis can be seen in Table 51. Only HellaSwag and MMLU-Humanities appear to have been boosted due to contamination in the training data, with the 70B model appearing to have gained a greater benefit than the 7B model, as one might expect. Furthermore, the impact of this effect on MMLU-Humanities appears to cause a benefit for MMLU-Overall for the 70B model, albeit with only a small delta (-0.9) between the "clean" subset performance and the sampling mean. No other dataset (for any choice of *L*) appears to have benefitted from dataset contamination, and the results are omitted from these datasets for conciseness.

**Table 51: Contamination analysis results for affected datasets.** [p. 76] No other evaluation datasets had sufficient evidence to be considered affected by contamination. Avg. Contam. % denotes the average per-sample contamination percentage for the given subset type. Models sizes refer to pretrained-only models.

| Dataset | Model | Subset Type | Avg. Contam. % | *n* | X-bar | mu_n | Z_n |
|---|---|---|---|---|---|---|---|
| HellaSwag (*L* = 40) | 70B | Clean | 0 | 7391 | 80.0 | 82.5 | -5.73 |
| | | Not Clean | 67.5 | 2651 | 89.5 | 82.4 | 9.56 |
| | | Not Dirty | 11.5 | 9194 | 81.6 | 82.5 | -2.27 |
| | | Dirty | 86.1 | 848 | 92.2 | 82.5 | 7.42 |
| | 7B | Clean | 0 | 7391 | 70.5 | 73.3 | -5.46 |
| | | Not Clean | 67.5 | 2651 | 81.3 | 73.4 | 9.17 |
| | | Not Dirty | 11.5 | 9194 | 72.4 | 73.4 | -2.06 |
| | | Dirty | 86.1 | 848 | 83.7 | 73.3 | 6.84 |
| MMLU-Humanities (*L* = 50) | 70B | Clean | 0.05 | 3996 | 62.2 | 65.3 | -4.08 |
| | | Not Clean | 85.12 | 709 | 82.7 | 65.3 | 9.71 |
| | | Not Dirty | 2.73 | 4185 | 62.7 | 65.3 | -3.50 |
| | | Dirty | 94.5 | 520 | 85.8 | 65.3 | 9.80 |
| | 7B | Clean | 0.05 | 3996 | 40.8 | 42.9 | -2.75 |
| | | Not Clean | 85.2 | 709 | 54.9 | 42.8 | 6.50 |
| | | Not Dirty | 2.73 | 4185 | 41.1 | 42.9 | -2.25 |
| | | Dirty | 94.5 | 520 | 56.9 | 42.8 | 6.49 |
| MMLU-Overall (*L* = 50) | 70B | Clean | 0.02 | 11862 | 68.0 | 68.9 | -2.00 |
| | | Not Clean | 84.7 | 2180 | 73.5 | 68.9 | 4.64 |
| | | Not Dirty | 3.18 | 12506 | 67.7 | 68.9 | -2.75 |
| | | Dirty | 94.4 | 1536 | 78.2 | 68.9 | 7.87 |
