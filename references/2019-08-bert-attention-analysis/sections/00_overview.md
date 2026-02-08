# Overview

**Title:** What Does BERT Look At? An Analysis of BERT's Attention

**Authors:** Kevin Clark, Urvashi Khandelwal, Omer Levy, Christopher D. Manning

**Affiliations:**
- Computer Science Department, Stanford University (Clark, Khandelwal, Manning)
- Facebook AI Research (Levy)

**Emails:** {kevclark,urvashik,manning}@cs.stanford.edu, omerlevy@fb.com

**Venue:** arXiv:1906.04341v1 [cs.CL]

**Date:** 11 Jun 2019

**Code:** https://github.com/clarkkev/attention-analysis

## Abstract

> "Large pre-trained neural networks such as BERT have had great recent success in NLP, motivating a growing body of research investigating what aspects of language they are able to learn from unlabeled data. Most recent analysis has focused on model outputs (e.g., language model surprisal) or internal vector representations (e.g., probing classifiers). Complementary to these works, we propose methods for analyzing the attention mechanisms of pre-trained models and apply them to BERT. BERT's attention heads exhibit patterns such as attending to delimiter tokens, specific positional offsets, or broadly attending over the whole sentence, with heads in the same layer often exhibiting similar behaviors. We further show that certain attention heads correspond well to linguistic notions of syntax and coreference. For example, we find heads that attend to the direct objects of verbs, determiners of nouns, objects of prepositions, and coreferent mentions with remarkably high accuracy. Lastly, we propose an attention-based probing classifier and use it to further demonstrate that substantial syntactic information is captured in BERT's attention." [p. 1]

## Section headings

1. Introduction
2. Background: Transformers and BERT
3. Surface-Level Patterns in Attention
   - 3.1 Relative Position
   - 3.2 Attending to Separator Tokens
   - 3.3 Focused vs Broad Attention
4. Probing Individual Attention Heads
   - 4.1 Method
   - 4.2 Dependency Syntax
   - 4.3 Coreference Resolution
5. Probing Attention Head Combinations
6. Clustering Attention Heads
7. Related Work
8. Conclusion
