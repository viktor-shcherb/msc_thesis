# Overview

**Title:** Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer

**Authors:** Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean (*equally major contributors)

**Affiliations:**
- Google Brain ({noam, azalia, andydavis, qvl, geoffhinton, jeff}@google.com)
- Jagiellonian University, Cracow (krzysztof.maziarz@student.uj.edu.pl)

**Venue:** Under review as a conference paper at ICLR 2017 (arXiv:1701.06538v1, 23 Jan 2017)

**Note:** Work done as a member of the Google Brain Residency program (g.co/brainresidency)

## Abstract

> "The capacity of a neural network to absorb information is limited by its number of parameters. Conditional computation, where parts of the network are active on a per-example basis, has been proposed in theory as a way of dramatically increasing model capacity without a proportional increase in computation. In practice, however, there are significant algorithmic and performance challenges. In this work, we address these challenges and finally realize the promise of conditional computation, achieving greater than 1000x improvements in model capacity with only minor losses in computational efficiency on modern GPU clusters. We introduce a Sparsely-Gated Mixture-of-Experts layer (MoE), consisting of up to thousands of feed-forward sub-networks. A trainable gating network determines a sparse combination of these experts to use for each example. We apply the MoE to the tasks of language modeling and machine translation, where model capacity is critical for absorbing the vast quantities of knowledge available in the training corpora. We present model architectures in which a MoE with up to 137 billion parameters is applied convolutionally between stacked LSTM layers. On large language modeling and machine translation benchmarks, these models achieve significantly better results than state-of-the-art at lower computational cost." [p. 1]

## Sections

1. Introduction and Related Work
   1.1 Conditional Computation
   1.2 Our Approach: The Sparsely-Gated Mixture-of-Experts Layer
   1.3 Related Work on Mixtures of Experts
2. The Structure of the Mixture-of-Experts Layer
   2.1 Gating Network
3. Addressing Performance Challenges
   3.1 The Shrinking Batch Problem
   3.2 Network Bandwidth
4. Balancing Expert Utilization
5. Experiments
   5.1 1 Billion Word Language Modeling Benchmark
   5.2 100 Billion Word Google News Corpus
   5.3 Machine Translation (Single Language Pair)
   5.4 Multilingual Machine Translation
6. Conclusion
Appendices:
   A. Load-Balancing Loss
   B. Hierarchical Mixture of Experts
   C. 1 Billion Word Language Modeling Benchmark - Experimental Details
      C.1 8-Million-Operations-per-Timestep Models
      C.2 More Expensive Models
   D. 100 Billion Word Google News Corpus - Experimental Details
   E. Machine Translation - Experimental Details
   F. Strictly Balanced Gating
   G. Attention Function
