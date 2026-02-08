# Overview

**Title:** Transformer Feed-Forward Layers Are Key-Value Memories

**Authors:** Mor Geva^{1,2}, Roei Schuster^{1,3}, Jonathan Berant^{1,2}, Omer Levy^{1}

**Affiliations:**
1. Blavatnik School of Computer Science, Tel-Aviv University
2. Allen Institute for Artificial Intelligence
3. Cornell Tech

**Contact:** {morgeva@mail, joberant@cs, levyomer@cs}.tau.ac.il, rs864@cornell.edu

**Venue:** arXiv:2012.14913v2 [cs.CL]

**Date:** 5 Sep 2021

**Code:** https://github.com/mega002/ff-layers/

## Abstract

> "Feed-forward layers constitute two-thirds of a transformer model's parameters, yet their role in the network remains under-explored. We show that feed-forward layers in transformer-based language models operate as key-value memories, where each key correlates with textual patterns in the training examples, and each value induces a distribution over the output vocabulary. Our experiments show that the learned patterns are human-interpretable, and that lower layers tend to capture shallow patterns, while upper layers learn more semantic ones. The values complement the keys' input patterns by inducing output distributions that concentrate probability mass on tokens likely to appear immediately after each pattern, particularly in the upper layers. Finally, we demonstrate that the output of a feed-forward layer is a composition of its memories, which is subsequently refined throughout the model's layers via residual connections to produce the final output distribution." [p. 1]

## Section Headings

1. Introduction [p. 1-2]
2. Feed-Forward Layers as Unnormalized Key-Value Memories [p. 2-3]
3. Keys Capture Input Patterns [p. 3-4]
   - 3.1 Experiment [p. 3]
   - 3.2 Results [p. 3-4]
4. Values Represent Distributions [p. 4-5]
5. Aggregating Memories [p. 5-8]
   - 5.1 Intra-Layer Memory Composition [p. 6-7]
   - 5.2 Inter-Layer Prediction Refinement [p. 7-8]
6. Related Work [p. 8-9]
7. Discussion and Conclusion [p. 9-10]
Acknowledgements [p. 10]
References [p. 10-12]
A. Pattern Analysis [p. 11-12]
B. Implementation Details [p. 11]
