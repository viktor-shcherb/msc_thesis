# 3.3 Extension: Block-Sparse FlashAttention [p. 6]

[p. 6]

FlashAttention is extended to approximate attention: block-sparse FlashAttention, whose IO complexity is smaller than FlashAttention by a factor proportional to the sparsity.

Given inputs $\mathbf{Q}, \mathbf{K}, \mathbf{V} \in \mathbb{R}^{N \times d}$ and a mask matrix $\tilde{\mathbf{M}} \in \{0, 1\}^{N \times N}$, the goal is to compute:

$$\mathbf{S} = \mathbf{Q}\mathbf{K}^\top \in \mathbb{R}^{N \times N}, \quad \mathbf{P} = \text{softmax}(\mathbf{S} \odot \mathbb{1}_{\tilde{\mathbf{M}}}) \in \mathbb{R}^{N \times N}, \quad \mathbf{O} = \mathbf{P}\mathbf{V} \in \mathbb{R}^{N \times d},$$

where $(\mathbf{S} \odot \mathbb{1}_{\tilde{\mathbf{M}}})_{kl} = \mathbf{S}_{kl}$ if $\tilde{\mathbf{M}}_{kl} = 1$ and $-\infty$ if $\mathbf{M}_{kl} = 0$. The mask $\tilde{\mathbf{M}}$ is required to have block form: for some block sizes $B_r, B_c$, for all $k, l$, $\tilde{\mathbf{M}}_{k,l} = \mathbf{M}_{ij}$ with $i = \lfloor k / B_r \rfloor$, $j = \lfloor l / B_c \rfloor$ for some $\mathbf{M} \in \{0, 1\}^{N/B_r \times N/B_c}$.

---
[p. 7 continued]

Given a predefined block sparsity mask $\mathbf{M} \in \{0, 1\}^{N/B_r \times N/B_c}$, Algorithm 1 can easily be adapted to only compute the nonzero blocks of the attention matrix. The algorithm is identical to Algorithm 1, except zero blocks are skipped. The algorithm description is reproduced in Algorithm 5 in Appendix B.

## Proposition 4 (IO Complexity of Block-Sparse FlashAttention)

> Let $N$ be the sequence length, $d$ be the head dimension, and $M$ be the size of SRAM with $d \leq M \leq Nd$. Block-sparse FlashAttention (Algorithm 5) requires $\Theta(Nd + N^2 d^2 M^{-1} s)$ HBM accesses where $s$ is the fraction of nonzero blocks in the block-sparsity mask. [p. 7]

Applying block-sparsity yields a direct improvement by the sparsity to the larger term in the IO complexity. For large sequence lengths $N$, $s$ is often set to $N^{-1/2}$ [11] or $N^{-1} \log N$ [3, 17, 92], resulting in $\Theta(N\sqrt{N})$ or $\Theta(N \log N)$ IO complexity. For downstream experiments, the fixed butterfly sparsity pattern [17] is used, which has been shown to be able to approximate arbitrary sparsity [16].

## Empirical Validation

In Fig. 2 (right), as the sparsity increases, the runtime of block-sparse FlashAttention improves proportionally. On the LRA benchmark, block-sparse FlashAttention achieves 2.8x speedup, while performing on par with standard attention (Section 4).
