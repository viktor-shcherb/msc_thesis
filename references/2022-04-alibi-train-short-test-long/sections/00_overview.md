# Overview

**Title:** Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation

**Authors:** Ofir Press^{1,2}, Noah A. Smith^{1,3}, Mike Lewis^{2}

**Affiliations:**
1. Paul G. Allen School of Computer Science & Engineering, University of Washington
2. Facebook AI Research
3. Allen Institute for AI

**Contact:** ofirp@cs.washington.edu

**Venue:** Published as a conference paper at ICLR 2022

**Date:** 22 Apr 2022 (arXiv v2)

**Code & models:** https://github.com/ofirpress/attention_with_linear_biases

## Abstract

> "Since the introduction of the transformer model by Vaswani et al. (2017), a fundamental question has yet to be answered: how does a model achieve extrapolation at inference time for sequences that are longer than it saw during training? We first show that extrapolation can be enabled by simply changing the position representation method, though we find that current methods do not allow for *efficient* extrapolation. We therefore introduce a simpler and more efficient position method, Attention with Linear Biases (ALiBi). ALiBi does not add positional embeddings to word embeddings; instead, it biases query-key attention scores with a penalty that is proportional to their distance. We show that this method trains a 1.3 billion parameter model on input sequences of length 1024 that extrapolates to input sequences of length 2048, achieving the same perplexity as a sinusoidal position embedding model trained on inputs of length 2048 but training 11% faster and using 11% less memory. ALiBi's inductive bias towards recency also leads it to outperform multiple strong position methods on the WikiText-103 benchmark." [p. 1]

## Section Headings

1. Introduction [p. 1]
2. Current Approaches Do Not Extrapolate Efficiently [p. 2]
   - 2.1 Background and Experimental Setup [p. 2]
   - 2.2 Measuring Extrapolation [p. 3]
3. Attention with Linear Biases (ALiBi) [p. 5]
4. Results [p. 6]
   - 4.1 Results on WikiText-103 and Toronto BookCorpus [p. 6]
   - 4.2 Results on the CC100+RoBERTa Corpus [p. 7]
5. Related Work [p. 9]
6. Conclusion [p. 9]
Acknowledgments [p. 10]
References [p. 11]
A Appendix [p. 15]
  - A.1 Introduction [p. 15]
  - A.2 ALiBi Results on WikiText-103 [p. 19]
  - A.3 Results on the Toronto Book Corpus [p. 20]
  - A.4 Results on the CC100+RoBERTa Corpus [p. 21]
B Analysis [p. 22]
  - B.1 Defining Sliding Window Evaluation and the Early Token Curse [p. 23]
  - B.2 Extrapolation Reduces the Early Token Curse [p. 23]
