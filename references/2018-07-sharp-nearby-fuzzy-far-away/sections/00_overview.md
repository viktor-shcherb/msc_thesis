# Overview

**Title:** Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context

**Authors:** Urvashi Khandelwal, He He, Peng Qi, Dan Jurafsky

**Affiliations:** Computer Science Department, Stanford University

**Venue:** arXiv:1805.04623v1 [cs.CL]

**Date:** 12 May 2018

## Abstract

> "We know very little about how neural language models (LM) use prior linguistic context. In this paper, we investigate the role of context in an LSTM LM, through ablation studies. Specifically, we analyze the increase in perplexity when prior context words are shuffled, replaced, or dropped. On two standard datasets, Penn Treebank and WikiText-2, we find that the model is capable of using about 200 tokens of context on average, but sharply distinguishes nearby context (recent 50 tokens) from the distant history. The model is highly sensitive to the order of words within the most recent sentence, but ignores word order in the long-range context (beyond 50 tokens), suggesting the distant past is modeled only as a rough semantic field or topic. We further find that the neural caching model (Grave et al., 2017b) especially helps the LSTM to copy words from within this distant context. Overall, our analysis not only provides a better understanding of how neural LMs use their context, but also sheds light on recent success from cache-based models."

## Section headings (observed so far)

1. Introduction
2. Language Modeling
3. Approach
4. How much context is used?
   - 4.1 Do different types of words need different amounts of context?
5. Nearby vs. long-range context
   - 5.1 Does word order matter?
   - 5.2 Types of words and the region of context
6. To cache or not to cache?
   - 6.1 Can LSTMs copy words without caches?
   - 6.2 How does the cache help?
7. Discussion
8. Conclusion
A. Hyperparameter settings
B. Additional Figures
