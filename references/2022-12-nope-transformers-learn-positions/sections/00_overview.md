# Overview

**Title:** Transformer Language Models without Positional Encodings Still Learn Positional Information

**Authors:**
- Adi Haviv (Tel Aviv University)
- Ori Ram (Tel Aviv University)
- Ofir Press (University of Washington)
- Peter Izsak (Intel Labs)
- Omer Levy (Tel Aviv University; Meta AI)

**Contact:** {adi.haviv, ori.ram, levyomer}@cs.tau.ac.il, ofirp@cs.washington.edu, peter.izsak@intel.com

**Venue:** arXiv:2203.16634v2 [cs.CL]

**Date:** 5 Dec 2022

## Abstract

> "Causal transformer language models (LMs), such as GPT-3, typically require some form of positional encoding, such as positional embeddings. However, we show that LMs without any explicit positional encoding are still competitive with standard models, and that this phenomenon is robust across different datasets, model sizes, and sequence lengths. Probing experiments reveal that such models acquire an implicit notion of absolute positions throughout the network, effectively compensating for the missing information. We conjecture that causal attention enables the model to infer the number of predecessors that each token can attend to, thereby approximating its absolute position. Our findings indicate that causal LMs might derive positional awareness not only from the explicit positioning mechanism, but also from the effects of the causal mask." [p. 1]

## Section Headings

1. Introduction
2. Positional Encodings
3. Experiment Setup
4. Results
5. Analysis
6. Conjecture
7. Related Work
8. Conclusion
9. Limitations
- Acknowledgements
- References
- Appendix A: NoPos Performance Across Different Segments of the Input
- Appendix B: Word Order Analysis
- Appendix C: Hyperparameters
