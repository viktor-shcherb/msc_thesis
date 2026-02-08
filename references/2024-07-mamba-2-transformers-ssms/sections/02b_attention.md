# 2.2 Attention [p. 5]

[p. 5] Attention broadly refers to a type of computation that assigns scores to every pair of positions in a sequence, allowing each element to "attend" to the rest. By far the most common and important variant of attention is softmax self-attention, which can be defined as:

$$Y = \text{softmax}(QK^\top) \cdot V$$

for $Q, K, V \in \mathbb{R}^{(T,P)}$. The mechanism of pairwise comparisons (induced by materializing $QK^\top$) leads to the characteristic quadratic training cost of attention.

Many variants of attention have been proposed, but all share the underlying core of these attention scores, with various approximations (Tay et al. 2022). The most important variant for this work is **linear attention** (Katharopoulos et al. 2020). Roughly speaking, this family of methods drops the softmax by folding it into a kernel feature map, and uses associativity of matrix multiplication to rewrite $(QK^\top) \cdot V = Q \cdot (K^\top V)$. Moreover, in the important case of causal (autoregressive) attention, they show that when the causal mask is incorporated into the left-hand side as $(L \circ QK^\top) \cdot V$, where $L$ is the lower-triangular 1's matrix, then the right-hand side can be expanded as a recurrence.

Several recent and concurrent works such as RetNet (Y. Sun et al. 2023) and GateLoop (Katsch 2023) strengthen this to more general forms of $L$ (Section 10). The formulation of structured masked attention in this work will strongly generalize these ideas.
