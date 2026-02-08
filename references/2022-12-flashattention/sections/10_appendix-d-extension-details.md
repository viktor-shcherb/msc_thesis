# D Extension Details [p. 25–26]

## D.1 Block-Sparse FlashAttention

[p. 25]

The full block-sparse FlashAttention algorithm is described in Algorithm 5. The algorithm is identical to Algorithm 2, except that zero blocks are skipped.

### Algorithm 5: Block-Sparse FlashAttention Forward Pass

**Require:** Matrices $\mathbf{Q}, \mathbf{K}, \mathbf{V} \in \mathbb{R}^{N \times d}$ in HBM, on-chip SRAM of size $M$, softmax scaling constant $\tau \in \mathbb{R}$, masking function MASK, dropout probability $p_{\text{drop}}$, block sizes $B_c = \lceil \frac{M}{4d} \rceil$, $B_r = \min(\lceil \frac{M}{4d} \rceil, d)$, block sparsity mask $\mathbf{M} \in \{0, 1\}^{N/B_r \times N/B_c}$.

1. Initialize the pseudo-random number generator state $\mathcal{R}$ and save to HBM.
2. Initialize $\mathbf{O} = (0)_{N \times d} \in \mathbb{R}^{N \times d}$, $\ell = (0)_N \in \mathbb{R}^N$, $m = (-\infty)_N \in \mathbb{R}^N$ in HBM.
3. Divide **Q** into $T_r = \lceil \frac{N}{B_r} \rceil$ blocks $\mathbf{Q}_1, \ldots, \mathbf{Q}_{T_r}$ of size $B_r \times d$ each, and divide **K**, **V** into $T_c = \lceil \frac{N}{B_c} \rceil$ blocks $\mathbf{K}_1, \ldots, \mathbf{K}_{T_c}$ and $\mathbf{V}_1, \ldots, \mathbf{V}_{T_c}$, of size $B_c \times d$ each.
4. Divide **O** into $T_r$ blocks $\mathbf{O}_1, \ldots, \mathbf{O}_{T_r}$ of size $B_r \times d$ each, divide $\ell$ into $T_r$ blocks $\ell_1, \ldots, \ell_{T_r}$ of size $B_r$ each, divide $m$ into $T_r$ blocks $m_1, \ldots, m_{T_r}$ of size $B_r$ each.
5. **for** $1 \leq j \leq T_c$ **do**
6. &emsp; Load $\mathbf{K}_j, \mathbf{V}_j$ from HBM to on-chip SRAM.
7. &emsp; **for** $1 \leq i \leq T_r$ **do**
8. &emsp;&emsp; **if** $M_{ij} \neq 0$ **then**
9. &emsp;&emsp;&emsp; Load $\mathbf{Q}_i, \mathbf{O}_i, \ell_i, m_i$ from HBM to on-chip SRAM.
10. &emsp;&emsp;&emsp; On chip, compute $\mathbf{S}_{ij} = \tau \mathbf{Q}_i \mathbf{K}_j^\top \in \mathbb{R}^{B_r \times B_c}$.
11. &emsp;&emsp;&emsp; On chip, compute $\mathbf{S}_{ij}^{\text{masked}} = \text{MASK}(\mathbf{S}_{ij})$.
12. &emsp;&emsp;&emsp; On chip, compute $\tilde{m}_{ij} = \text{rowmax}(\mathbf{S}_{ij}^{\text{masked}}) \in \mathbb{R}^{B_r}$, $\tilde{\mathbf{P}}_{ij} = \exp(\mathbf{S}_{ij}^{\text{masked}} - \tilde{m}_{ij}) \in \mathbb{R}^{B_r \times B_c}$ (pointwise), $\tilde{\ell}_{ij} = \text{rowsum}(\tilde{\mathbf{P}}_{ij}) \in \mathbb{R}^{B_r}$.
13. &emsp;&emsp;&emsp; On chip, compute $m_i^{\text{new}} = \max(m_i, \tilde{m}_{ij}) \in \mathbb{R}^{B_r}$, $\ell_i^{\text{new}} = e^{m_i - m_i^{\text{new}}} \ell_i + e^{\tilde{m}_{ij} - m_i^{\text{new}}} \tilde{\ell}_{ij} \in \mathbb{R}^{B_r}$.
14. &emsp;&emsp;&emsp; On chip, compute $\tilde{\mathbf{P}}_{ij}^{\text{dropped}} = \text{dropout}(\tilde{\mathbf{P}}_{ij}, p_{\text{drop}})$.
15. &emsp;&emsp;&emsp; Write $\mathbf{O}_i \leftarrow \text{diag}(\ell_i^{\text{new}})^{-1} (\text{diag}(\ell_i) e^{m_i - m_i^{\text{new}}} \mathbf{O}_i + e^{\tilde{m}_{ij} - m_i^{\text{new}}} \tilde{\mathbf{P}}_{ij}^{\text{dropped}} \mathbf{V}_j)$ to HBM.
16. &emsp;&emsp;&emsp; Write $\ell_i \leftarrow \ell_i^{\text{new}}$, $m_i \leftarrow m_i^{\text{new}}$ to HBM.
17. &emsp;&emsp; **end if**
18. &emsp; **end for**
19. **end for**
20. Return $\mathbf{O}, \ell, m, \mathcal{R}$.

### Proof of Proposition 4

[p. 25]

The proof is very similar to the proof of Theorem 2. For the block-sparse case, only blocks corresponding to nonzero blocks need to be loaded. As a result, the number of memory accesses are scaled by $s$, the fraction of nonzero blocks in the block-sparsity mask. However, for small values of $s$, the result $\mathbf{O} \in \mathbb{R}^{N \times d}$ would still need to be written. Therefore the number of HBM accesses is

$$\Theta\left(Nd + \frac{N^2 d^2}{M} s\right).$$

$\square$

## D.2 Potential Extensions

[p. 25–26]

A few potential extensions of the IO-aware approach to speed up deep learning training are discussed.

**Multi-GPU Attention.** Large language models are trained on hundreds or thousands of GPUs, and one typically splits the attention computation between 4-8 GPUs on the same node [77]. This introduces another level of memory hierarchy: beside GPU SRAM and GPU HBM, we also have the HBM of other GPUs. For very long sequences, the different GPUs on the same node can cooperate to compute attention by taking into account the asymmetry of different levels of memory hierarchy. [p. 26]

**Sparse MLP layers.** Typical dense MLP layers are compute-bound and not memory-bound. To improve their efficiency, MLP layers with sparse weight matrices can be used [17]. However, many sparse MLP layers are instead memory-bound, and their speedup is often not proportional to the sparsity. The authors believe that an IO-aware implementation can alleviate this issue and realize the benefits of sparsity. They are excited about future work in this direction, to reduce the computational requirement of large models and improve their wall-block runtime. [p. 26]

**Kernel machine learning.** The approach in FlashAttention relies on the fact that the $N \times N$ attention matrix is a function of a low-rank matrix $\mathbf{Q}\mathbf{K}^\top$ (of rank $d \ll N$). As a result, the inputs $\mathbf{Q}, \mathbf{K}$ can be repeatedly loaded and the block of the attention matrix recomputed, significantly reducing HBM access. A similar scenario happens in kernel machine learning: each element $K_{ij}$ of the $N \times N$ kernel matrix $\mathbf{K}$ is a function of two vectors of size $d \ll N$, as it measures the similarity between two datapoints $x_i$ and $x_j$. The KeOps library [8, 26] is a successful example of how reducing memory reads/writes can speed up kernel operations. The authors hope that this will motivate kernel methods that focus more on reducing IOs instead of just FLOPs. [p. 26]
