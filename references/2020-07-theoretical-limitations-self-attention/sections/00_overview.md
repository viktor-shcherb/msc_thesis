# Overview

**Title:** Theoretical Limitations of Self-Attention in Neural Sequence Models

**Authors:** Michael Hahn (Stanford University, mhahn2@stanford.edu)

**Venue:** Transactions of the Association for Computational Linguistics, vol. 8, pp. 156--171, 2020. https://doi.org/10.1162/tacl_a_00306

**Action Editor:** Yoav Goldberg. Submission batch: 7/2019; Revision batch: 11/2019; Published 2020.

**Abstract:**

> "Transformers are emerging as the new workhorse of NLP, showing great success across tasks. Unlike LSTMs, transformers process input sequences entirely through self-attention. Previous work has suggested that the computational capabilities of self-attention to process hierarchical structures are limited. In this work, we mathematically investigate the computational power of self-attention to model formal languages. Across both soft and hard attention, we show strong theoretical limitations of the computational abilities of self-attention, finding that it cannot model periodic finite-state languages, nor hierarchical structure, unless the number of layers or heads increases with input length. These limitations seem surprising given the practical success of self-attention and the prominent role assigned to hierarchical structure in linguistics, suggesting that natural language can be approximated well with models that are too weak for the formal languages typically assumed in theoretical linguistics." [p. 1]

## Section headings (observed so far)

1. Introduction
2. Related Work
3. Self-Attention
4. Regular and Context-Free Languages
5. Results for Hard Attention
6. Results for Soft Attention
7. Discussion
8. Conclusion
Acknowledgments
References
