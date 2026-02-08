# 3.1 An Efficient Attention Algorithm With Tiling and Recomputation [p. 4-5]

[p. 4]

Given the inputs $\mathbf{Q}, \mathbf{K}, \mathbf{V} \in \mathbb{R}^{N \times d}$ in HBM, the aim is to compute the attention output $\mathbf{O} \in \mathbb{R}^{N \times d}$ and write it to HBM. The goal is to reduce the amount of HBM accesses (to sub-quadratic in $N$).

Two established techniques (tiling, recomputation) are applied to overcome the technical challenge of computing exact attention in sub-quadratic HBM accesses. This is described in Algorithm 1. The main idea is that the inputs **Q**, **K**, **V** are split into blocks, loaded from slow HBM to fast SRAM, then the attention output is computed with respect to those blocks. By scaling the output of each block by the right normalization factor before adding them up, the correct result is obtained at the end.

## Tiling

Attention is computed by blocks. Softmax couples columns of **K**, so the large softmax is decomposed with scaling [51, 60, 66]. For numerical stability, the softmax of vector $x \in \mathbb{R}^B$ is computed as:

$$m(x) := \max_i x_i, \quad f(x) := \left[e^{x_1 - m(x)} \quad \cdots \quad e^{x_B - m(x)}\right], \quad \ell(x) := \sum_i f(x)_i, \quad \text{softmax}(x) := \frac{f(x)}{\ell(x)}.$$

[p. 5]

For vectors $x^{(1)}, x^{(2)} \in \mathbb{R}^B$, the softmax of the concatenated $x = \begin{bmatrix} x^{(1)} & x^{(2)} \end{bmatrix} \in \mathbb{R}^{2B}$ can be decomposed as:

$$m(x) = m\left(\begin{bmatrix} x^{(1)} & x^{(2)} \end{bmatrix}\right) = \max(m(x^{(1)}), m(x^{(2)})),$$

$$f(x) = \begin{bmatrix} e^{m(x^{(1)}) - m(x)} f(x^{(1)}) \quad e^{m(x^{(2)}) - m(x)} f(x^{(2)}) \end{bmatrix},$$

$$\ell(x) = \ell\left(\begin{bmatrix} x^{(1)} & x^{(2)} \end{bmatrix}\right) = e^{m(x^{(1)}) - m(x)} \ell(x^{(1)}) + e^{m(x^{(2)}) - m(x)} \ell(x^{(2)}),$$

$$\text{softmax}(x) = \frac{f(x)}{\ell(x)}.$$

Therefore if extra statistics $(m(x), \ell(x))$ are tracked, softmax can be computed one block at a time. The inputs **Q**, **K**, **V** are split into blocks (Algorithm 1 line 3), the softmax values are computed along with extra statistics (Algorithm 1 line 10), and the results are combined (Algorithm 1 line 12). This style of aggregation is called *algebraic aggregation* [33] (footnote 2).

## Recomputation

One of the goals is to not store $O(N^2)$ intermediate values for the backward pass. The backward pass typically requires the matrices $\mathbf{S}, \mathbf{P} \in \mathbb{R}^{N \times N}$ to compute the gradients with respect to **Q**, **K**, **V**. However, by storing the output **O** and the softmax normalization statistics $(m, \ell)$, the attention matrix **S** and **P** can be easily recomputed in the backward pass from blocks of **Q**, **K**, **V** in SRAM. This can be seen as a form of selective gradient checkpointing [10, 34]. While gradient checkpointing has been suggested to reduce the maximum amount of memory required [66], all implementations (that they know of) have to trade speed for memory. In contrast, even with more FLOPs, the recomputation speeds up the backward pass due to reduced HBM accesses (Fig. 2). The full backward pass description is in Appendix B.

## Implementation Details: Kernel Fusion

Tiling enables implementation of the algorithm in one CUDA kernel, loading input from HBM, performing all the computation steps (matrix multiply, softmax, optionally masking and dropout, matrix multiply), then writing the result back to HBM (masking and dropout in Appendix B). This avoids repeatedly reading and writing of inputs and outputs from and to HBM.

## Algorithm 1: FlashAttention

**Require:** Matrices $\mathbf{Q}, \mathbf{K}, \mathbf{V} \in \mathbb{R}^{N \times d}$ in HBM, on-chip SRAM of size $M$.

1. Set block sizes $B_c = \lceil M / (4d) \rceil$, $B_r = \min\left(\lceil M / (4d) \rceil, d\right)$.
2. Initialize $\mathbf{O} = (0)_{N \times d} \in \mathbb{R}^{N \times d}$, $\ell = (0)_N \in \mathbb{R}^N$, $m = (-\infty)_N \in \mathbb{R}^N$ in HBM.
3. Divide **Q** into $T_r = \lceil N / B_r \rceil$ blocks $\mathbf{Q}_1, \ldots, \mathbf{Q}_{T_r}$ of size $B_r \times d$ each, and divide **K**, **V** in to $T_c = \lceil N / B_c \rceil$ blocks $\mathbf{K}_1, \ldots, \mathbf{K}_{T_c}$ and $\mathbf{V}_1, \ldots, \mathbf{V}_{T_c}$, of size $B_c \times d$ each.
4. Divide **O** into $T_r$ blocks $\mathbf{O}_1, \ldots, \mathbf{O}_{T_r}$ of size $B_r \times d$ each, divide $\ell$ into $T_r$ blocks $\ell_1, \ldots, \ell_{T_r}$, divide $m$ into $T_r$ blocks $m_1, \ldots, m_{T_r}$ of size $B_r$ each.
5. **for** $1 \leq j \leq T_c$ **do**
6. &emsp; Load $\mathbf{K}_j, \mathbf{V}_j$ from HBM to on-chip SRAM.
7. &emsp; **for** $1 \leq i \leq T_r$ **do**
8. &emsp;&emsp; Load $\mathbf{Q}_i, \mathbf{O}_i, \ell_i, m_i$ from HBM to on-chip SRAM.
9. &emsp;&emsp; On chip, compute $\mathbf{S}_{ij} = \mathbf{Q}_i \mathbf{K}_j^\top \in \mathbb{R}^{B_r \times B_c}$.
10. &emsp;&emsp; On chip, compute $\tilde{m}_{ij} = \text{rowmax}(\mathbf{S}_{ij}) \in \mathbb{R}^{B_r}$, $\tilde{\mathbf{P}}_{ij} = \exp(\mathbf{S}_{ij} - \tilde{m}_{ij}) \in \mathbb{R}^{B_r \times B_c}$ (pointwise), $\tilde{\ell}_{ij} = \text{rowsum}(\tilde{\mathbf{P}}_{ij}) \in \mathbb{R}^{B_r}$.
11. &emsp;&emsp; On chip, compute $m_i^{\text{new}} = \max(m_i, \tilde{m}_{ij}) \in \mathbb{R}^{B_r}$, $\ell_i^{\text{new}} = e^{m_i - m_i^{\text{new}}} \ell_i + e^{\tilde{m}_{ij} - m_i^{\text{new}}} \tilde{\ell}_{ij} \in \mathbb{R}^{B_r}$.
12. &emsp;&emsp; Write $\mathbf{O}_i \leftarrow \text{diag}(\ell_i^{\text{new}})^{-1} (\text{diag}(\ell_i) e^{m_i - m_i^{\text{new}}} \mathbf{O}_i + e^{\tilde{m}_{ij} - m_i^{\text{new}}} \tilde{\mathbf{P}}_{ij} \mathbf{V}_j)$ to HBM.
13. &emsp;&emsp; Write $\ell_i \leftarrow \ell_i^{\text{new}}$, $m_i \leftarrow m_i^{\text{new}}$ to HBM.
14. &emsp; **end for**
15. **end for**
16. Return **O**.

## Theorem 1

> Algorithm 1 returns $\mathbf{O} = \text{softmax}(\mathbf{Q}\mathbf{K}^\top)\mathbf{V}$ with $O(N^2 d)$ FLOPs and requires $O(N)$ additional memory beyond inputs and output. [p. 5]

Proof is in Appendix C.
