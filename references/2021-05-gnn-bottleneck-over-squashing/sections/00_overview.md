# Overview

**Title:** On the Bottleneck of Graph Neural Networks and its Practical Implications

**Authors:** Uri Alon & Eran Yahav

**Affiliations:** Technion, Israel ({urialon, yahave}@cs.technion.ac.il)

**Venue:** Published as a conference paper at ICLR 2021

**Date:** 9 Mar 2021 (arXiv:2006.05205v4)

**Code:** https://github.com/tech-srl/bottleneck/

## Abstract

> "Since the proposal of the graph neural network (GNN) by Gori et al. (2005) and Scarselli et al. (2008), one of the major problems in training GNNs was their struggle to propagate information between distant nodes in the graph. We propose a new explanation for this problem: GNNs are susceptible to a *bottleneck* when aggregating messages across a long path. This bottleneck causes the *over-squashing* of exponentially growing information into fixed-size vectors. As a result, GNNs fail to propagate messages originating from distant nodes and perform poorly when the prediction task depends on long-range interaction. In this paper, we highlight the inherent problem of over-squashing in GNNs: we demonstrate that the bottleneck hinders popular GNNs from fitting long-range signals in the training data; we further show that GNNs that absorb incoming edges equally, such as GCN and GIN, are *more susceptible* to over-squashing than GAT and GGNN; finally, we show that prior work, which extensively tuned GNN models of long-range problems, suffer from over-squashing, and that breaking the bottleneck improves their state-of-the-art results without any tuning or additional weights." [p. 1]

## Section headings

1. Introduction
2. Preliminaries
3. The GNN Bottleneck
4. Evaluation
   - 4.1 Synthetic Benchmark: NeighborsMatch
   - 4.2 Quantum Chemistry: QM9
   - 4.3 Biological Benchmarks
   - 4.4 Programs: VarMisuse
5. How Long is Long-Range?
6. Related Work
7. Conclusion
8. Acknowledgments
A. Tree-NeighborsMatch -- Training Details
B. QM9 -- Additional Results
   - B.1 Additional GNN Types
   - B.2 Alternative Solutions
   - B.3 Partial-FA Layers
C. Biological Benchmarks -- Training Details
D. Data Statistics
   - D.1 Synthetic Dataset: Tree-NeighborsMatch
   - D.2 Quantum Chemistry: QM9
   - D.3 Biological Benchmarks
   - D.4 VarMisuse
E. Discussion: Over-Smoothing vs. Over-Squashing
