# A. Details of Common Crawl Filtering [p. 43]

[p. 43] As mentioned in Section 2.2, two techniques were employed to improve the quality of the Common Crawl dataset: (1) filtering and (2) fuzzy deduplication.

## Filtering

[p. 43] An automatic filtering method was developed to remove low quality documents. Using the original WebText as a proxy for high-quality documents, a classifier was trained to distinguish high-quality documents from raw Common Crawl. This classifier was then used to re-sample Common Crawl by prioritizing documents predicted to be higher quality. The classifier was trained using logistic regression with features from Spark's standard tokenizer and HashingTF. For positive examples, a collection of curated datasets such as WebText, Wikipedia, and the web books corpus was used; for negative examples, unfiltered Common Crawl was used.

Each document in the dataset was kept iff:

```
np.random.pareto(alpha) > 1 - document_score
```

The value alpha = 9 was chosen in order to take mostly documents the classifier scored highly, but still include some documents that were out of distribution. alpha was chosen to match the distribution of scores from the classifier on WebText. This re-weighting increased quality as measured by loss on a range of out-of-distribution generative text samples.

## Fuzzy Deduplication

[p. 43] To further improve model quality and prevent overfitting (which becomes increasingly important as model capacity increases), documents with high overlap with other documents were fuzzily deduplicated (i.e. removed) within each dataset using Spark's MinHashLSH implementation with 10 hashes, using the same features as the classifier above. WebText was also fuzzily removed from Common Crawl. Overall this decreased dataset size by an average of 10%.

After filtering for duplicates and quality, text occurring in benchmark datasets was also partially removed, described in Appendix C.
