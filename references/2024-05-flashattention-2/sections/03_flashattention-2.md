# 3 FlashAttention-2: Algorithm, Parallelism, and Work Partitioning [p. 5-6]

[p. 5] The FlashAttention-2 algorithm includes several tweaks to FlashAttention to reduce the number of non-matmul FLOPs, describes how to parallelize the computation on different thread blocks to make full use of the GPU resources, and describes partitioning the work between different warps within one thread block to reduce the amount of shared memory access. These improvements lead to 2-3x speedup as validated in Section 4.

## 3.1 Algorithm [p. 5]

The algorithm from FlashAttention is tweaked to reduce the number of non-matmul FLOPs. This is because modern GPUs have specialized compute units (e.g., Tensor Cores on Nvidia GPUs) that makes matmul much faster. As an example, the A100 GPU has a max theoretical throughput of 312 TFLOPs/s of FP16/BF16 matmul, but only 19.5 TFLOPs/s of non-matmul FP32. Another way to think about this is that each non-matmul FLOP is 16x more expensive than a matmul FLOP. To maintain high throughput (e.g., more than 50% of the maximum theoretical TFLOPs/s), the goal is to spend as much time on matmul FLOPs as possible.

### 3.1.1 Forward pass [p. 5-6]

The online softmax trick as shown in Section 2.3 is revisited and two minor tweaks are made to reduce non-matmul FLOPs:

**Tweak 1.** [p. 5] The two terms of the output update do not need to be rescaled by $\text{diag}(\ell^{(2)})^{-1}$:

$$\mathbf{O}^{(2)} = \text{diag}(\ell^{(1)} / \ell^{(2)})^{-1} \mathbf{O}^{(1)} + \text{diag}(\ell^{(2)})^{-1} e^{\mathbf{S}^{(2)} - m^{(2)}} \mathbf{V}^{(2)}.$$

Instead, an "un-scaled" version of $\mathbf{O}^{(2)}$ is maintained and the statistics $\ell^{(2)}$ are kept around:

$$\tilde{\mathbf{O}}^{(2)} = \text{diag}(\ell^{(1)})^{-1} \mathbf{O}^{(1)} + e^{\mathbf{S}^{(2)} - m^{(2)}} \mathbf{V}^{(2)}.$$

Only at the very end of the loop is the final $\tilde{\mathbf{O}}^{(\text{last})}$ scaled by $\text{diag}(\ell^{(\text{last})})^{-1}$ to get the right output.

**Tweak 2.** [p. 5] Both the max $m^{(j)}$ and the sum of exponentials $\ell^{(j)}$ do not need to be saved for the backward pass. Only the logsumexp needs to be stored: $L^{(j)} = m^{(j)} + \log(\ell^{(j)})$.

[p. 6] In the simple case of 2 blocks in Section 2.3, the online softmax trick now becomes:

$$m^{(1)} = \text{rowmax}(\mathbf{S}^{(1)}) \in \mathbb{R}^{B_r}$$

$$\ell^{(1)} = \text{rowsum}(e^{\mathbf{S}^{(1)} - m^{(1)}}) \in \mathbb{R}^{B_r}$$

$$\tilde{\mathbf{O}}^{(1)} = e^{\mathbf{S}^{(1)} - m^{(1)}} \mathbf{V}^{(1)} \in \mathbb{R}^{B_r \times d}$$

$$m^{(2)} = \max(m^{(1)}, \text{rowmax}(\mathbf{S}^{(2)})) = m$$

$$\ell^{(2)} = e^{m^{(1)} - m^{(2)}} \ell^{(1)} + \text{rowsum}(e^{\mathbf{S}^{(2)} - m^{(2)}}) = \text{rowsum}(e^{\mathbf{S}^{(1)} - m}) + \text{rowsum}(e^{\mathbf{S}^{(2)} - m}) = \ell$$

$$\tilde{\mathbf{P}}^{(2)} = \text{diag}(\ell^{(2)})^{-1} e^{\mathbf{S}^{(2)} - m^{(2)}}$$

$$\tilde{\mathbf{O}}^{(2)} = \text{diag}(e^{m^{(1)} - m^{(2)}}) \tilde{\mathbf{O}}^{(1)} + e^{\mathbf{S}^{(2)} - m^{(2)}} \mathbf{V}^{(2)} = e^{s^{(1)} - m} \mathbf{V}^{(1)} + e^{s^{(2)} - m} \mathbf{V}^{(2)}$$

$$\mathbf{O}^{(2)} = \text{diag}(\ell^{(2)})^{-1} \tilde{\mathbf{O}}^{(2)} = \mathbf{O}.$$

**Algorithm 1: FlashAttention-2 forward pass** [p. 6]

**Require:** Matrices $\mathbf{Q}, \mathbf{K}, \mathbf{V} \in \mathbb{R}^{N \times d}$ in HBM, block sizes $B_c$, $B_r$.

1. Divide $\mathbf{Q}$ into $T_r = \lceil \frac{N}{B_r} \rceil$ blocks $\mathbf{Q}_1, \ldots, \mathbf{Q}_{T_r}$ of size $B_r \times d$ each, and divide $\mathbf{K}, \mathbf{V}$ in to $T_c = \lceil \frac{N}{B_c} \rceil$ blocks $\mathbf{K}_1, \ldots, \mathbf{K}_{T_c}$ and $\mathbf{V}_1, \ldots, \mathbf{V}_{T_c}$ of size $B_c \times d$.
2. Divide the output $\mathbf{O} \in \mathbb{R}^{N \times d}$ into $T_r$ blocks $\mathbf{O}_i, \ldots, \mathbf{O}_{T_r}$ of size $B_r \times d$ each, and divide the logsumexp $L$ into $T_r$ blocks $L_i, \ldots, L_{T_r}$ of size $B_r$ each.
3. **for** $1 \leq i \leq T_r$ **do**
4. $\quad$ Load $\mathbf{Q}_i$ from HBM to on-chip SRAM.
5. $\quad$ On chip, initialize $\mathbf{O}_i^{(0)} = (0)_{B_r \times d} \in \mathbb{R}^{B_r \times d}$, $\ell_i^{(0)} = (0)_{B_r} \in \mathbb{R}^{B_r}$, $m_i^{(0)} = (-\infty)_{B_r} \in \mathbb{R}^{B_r}$.
6. $\quad$ **for** $1 \leq j \leq T_c$ **do**
7. $\quad\quad$ Load $\mathbf{K}_j, \mathbf{V}_j$ from HBM to on-chip SRAM.
8. $\quad\quad$ On chip, compute $\mathbf{S}_i^{(j)} = \mathbf{Q}_i \mathbf{K}_j^T \in \mathbb{R}^{B_r \times B_c}$.
9. $\quad\quad$ On chip, compute $m_i^{(j)} = \max(m_i^{(j-1)}, \text{rowmax}(\mathbf{S}_i^{(j)})) \in \mathbb{R}^{B_r}$, $\tilde{\mathbf{P}}_i^{(j)} = \exp(\mathbf{S}_i^{(j)} - m_i^{(j)}) \in \mathbb{R}^{B_r \times B_c}$ (pointwise), $\ell_i^{(j)} = e^{m_i^{(j-1)} - m_i^{(j)}} \ell_i^{(j-1)} + \text{rowsum}(\tilde{\mathbf{P}}_i^{(j)}) \in \mathbb{R}^{B_r}$.
10. $\quad\quad$ On chip, compute $\mathbf{O}_i^{(j)} = \text{diag}(e^{m_i^{(j-1)} - m_i^{(j)}}) \mathbf{O}_i^{(j-1)} + \tilde{\mathbf{P}}_i^{(j)} \mathbf{V}_j$.
11. $\quad$ **end for**
12. $\quad$ On chip, compute $\mathbf{O}_i = \text{diag}(\ell_i^{(T_c)})^{-1} \mathbf{O}_i^{(T_c)}$.
13. $\quad$ On chip, compute $L_i = m_i^{(T_c)} + \log(\ell_i^{(T_c)})$.
14. $\quad$ Write $\mathbf{O}_i$ to HBM as the $i$-th block of $\mathbf{O}$.
15. $\quad$ Write $L_i$ to HBM as the $i$-th block of $L$.
16. **end for**
17. Return the output $\mathbf{O}$ and the logsumexp $L$.

**Causal masking.** [p. 6] One common use case of attention is in auto-regressive language modeling, where a causal mask must be applied to the attention matrix $\mathbf{S}$ (i.e., any entry $\mathbf{S}_{ij}$ with $j > i$ is set to $-\infty$).

1. As FlashAttention and FlashAttention-2 already operate by blocks, for any blocks where all the column indices are more than the row indices (approximately half of the blocks for large sequence length), the computation of that block can be skipped. This leads to around 1.7-1.8x speedup compared to attention without the causal mask.

2. The causal mask does not need to be applied for blocks whose row indices are guaranteed to be strictly less than the column indices. This means that for each row, the causal mask only needs to be applied to 1 block (assuming square block).

**Correctness, runtime, and memory requirement.** [p. 7] As with FlashAttention, Algorithm 1 returns the correct output $\mathbf{O} = \text{softmax}(\mathbf{Q}\mathbf{K}^\top)\mathbf{V}$ (with no approximation), using $O(N^2 d)$ FLOPs and requires $O(N)$ additional memory beyond inputs and output (to store the logsumexp $L$). The proof is almost the same as the proof of Dao et al. [5, Theorem 1], so it is omitted.

### 3.1.2 Backward pass [p. 7]

The backward pass of FlashAttention-2 is almost the same as that of FlashAttention. A minor tweak is made to only use the row-wise logsumexp $L$ instead of both the row-wise max and row-wise sum of exponentials in the softmax.

**Algorithm 2: FlashAttention-2 Backward Pass** [p. 7]

**Require:** Matrices $\mathbf{Q}, \mathbf{K}, \mathbf{V}, \mathbf{O}, \mathbf{dO} \in \mathbb{R}^{N \times d}$ in HBM, vector $L \in \mathbb{R}^N$ in HBM, block sizes $B_c$, $B_r$.

1. Divide $\mathbf{Q}$ into $T_r = \lceil \frac{N}{B_r} \rceil$ blocks $\mathbf{Q}_1, \ldots, \mathbf{Q}_{T_r}$ of size $B_r \times d$ each, and divide $\mathbf{K}, \mathbf{V}$ in to $T_c = \lceil \frac{N}{B_c} \rceil$ blocks $\mathbf{K}_1, \ldots, \mathbf{K}_{T_c}$ and $\mathbf{V}_1, \ldots, \mathbf{V}_{T_c}$, of size $B_c \times d$ each.
2. Divide the output $\mathbf{O} \in \mathbb{R}^{N \times d}$ into $T_r$ blocks $\mathbf{O}_1, \ldots, \mathbf{O}_{T_r}$ of size $B_r \times d$ each, divide $\mathbf{dO}$ into $T_r$ blocks $\mathbf{dO}_1, \ldots, \mathbf{dO}_{T_r}$ of size $B_r \times d$ each, and divide $L$ into $T_r$ blocks $L_1, \ldots, L_{T_r}$ of size $B_r$ each.
3. Initialize $\mathbf{dQ} = (0)_{N \times d}$ in HBM and divide it into $T_r$ blocks $\mathbf{dQ}_1, \ldots, \mathbf{dQ}_{T_r}$ of size $B_r \times d$ each. Divide $\mathbf{dK}$ in to $T_c$ blocks $\mathbf{dK}_1, \ldots, \mathbf{dK}_{T_c}$ and $\mathbf{dV}_1, \ldots, \mathbf{dV}_{T_c}$, of size $B_c \times d$ each.
4. Compute $D = \text{rowsum}(\mathbf{dO} \circ \mathbf{O}) \in \mathbb{R}^d$ (pointwise multiply), write $D$ to HBM and divide it into $T_r$ blocks $D_1, \ldots, D_{T_r}$ of size $B_r$ each.
5. **for** $1 \leq j \leq T_c$ **do**
6. $\quad$ Load $\mathbf{K}_j, \mathbf{V}_j$ from HBM to on-chip SRAM.
7. $\quad$ Initialize $\mathbf{dK}_j = (0)_{B_c \times d}, \mathbf{dV}_j = (0)_{B_c \times d}$ on chip.
8. $\quad$ **for** $1 \leq i \leq T_r$ **do**
9. $\quad\quad$ Load $\mathbf{Q}_i, \mathbf{O}_i, \mathbf{dO}_i, \mathbf{dQ}_i, L_i, D_i$ from HBM to on-chip SRAM.
10. $\quad\quad$ On chip, compute $\mathbf{S}_i^{(j)} = \mathbf{Q}_i \mathbf{K}_j^T \in \mathbb{R}^{B_r \times B_c}$.
11. $\quad\quad$ On chip, compute $\mathbf{P}_i^{(j)} = \exp(\mathbf{S}_{ij} - L_i) \in \mathbb{R}^{B_r \times B_c}$.
12. $\quad\quad$ On chip, compute $\mathbf{dV}_j \leftarrow \mathbf{dV}_j + (\mathbf{P}_i^{(j)})^\top \mathbf{dO}_i \in \mathbb{R}^{B_c \times d}$.
13. $\quad\quad$ On chip, compute $\mathbf{dP}_i^{(j)} = \mathbf{dO}_i \mathbf{V}_j^\top \in \mathbb{R}^{B_r \times B_c}$.
14. $\quad\quad$ On chip, compute $\mathbf{dS}_i^{(j)} = \mathbf{P}_i^{(j)} \circ (\mathbf{dP}_i^{(j)} - D_i) \in \mathbb{R}^{B_r \times B_c}$.
15. $\quad\quad$ Load $\mathbf{dQ}_i$ from HBM to SRAM, then on chip, update $\mathbf{dQ}_i \leftarrow \mathbf{dQ}_i + \mathbf{dS}_i^{(j)} \mathbf{K}_j \in \mathbb{R}^{B_r \times d}$, and write back to HBM.
16. $\quad\quad$ On chip, compute $\mathbf{dK}_j \leftarrow \mathbf{dK}_j + \mathbf{dS}_i^{(j)\top} \mathbf{Q}_i \in \mathbb{R}^{B_c \times d}$.
17. $\quad$ **end for**
18. $\quad$ Write $\mathbf{dK}_j, \mathbf{dV}_j$ to HBM.
19. **end for**
20. Return $\mathbf{dQ}, \mathbf{dK}, \mathbf{dV}$.

**Multi-query attention and grouped-query attention.** [p. 7] Multi-query attention (MQA) [15] and grouped-query attention (GQA) [1] are variants of attention where multiple heads of query attend to the same head of key and value, in order to reduce the size of the KV cache during inference. Instead of having to duplicate the key and value heads for the computation, the indices into the head are implicitly manipulated to perform the same computation. In the backward pass, the gradients $\mathbf{dK}$ and $\mathbf{dV}$ need to be summed across different heads that were implicitly duplicated.

## 3.2 Parallelism [p. 7-8]

[p. 7] The first version of FlashAttention parallelizes over batch size and number of heads. One thread block is used to process one attention head, and there are overall batch size $\cdot$ number of heads thread blocks. Each thread block is scheduled to run on a streaming multiprocessor (SM), and there are 108 of these SMs on an A100 GPU for example. This scheduling is efficient when this number is large (say $\geq 80$), since it can effectively use almost all of the compute resources on the GPU.

[p. 8] In the case of long sequences (which usually means small batch sizes or small number of heads), to make better use of the multiprocessors on the GPU, FlashAttention-2 now additionally parallelizes over the sequence length dimension. This results in significant speedup for this regime.

**Forward pass.** [p. 8] The outer loop (over sequence length) is embarrassingly parallel, and the thread blocks scheduled on different SMs do not need to communicate with each other. FlashAttention-2 also parallelizes over the batch dimension and number of heads dimension, as done in FlashAttention. The increased parallelism over sequence length helps improve occupancy (fraction of GPU resources being used) when the batch size and number of heads are small, leading to speedup in this case.

The ideas of swapping the order of the loop (outer loop over row blocks and inner loop over column blocks, instead of the other way round in the original FlashAttention paper), as well as parallelizing over the sequence length dimension, were first suggested and implemented by Phil Tillet in the Triton [17] implementation.^3

**Backward pass.** [p. 8] The only shared computation between different column blocks is the update of $\mathbf{dQ}$ in Algorithm 2, where $\mathbf{dQ}_i$ must be loaded from HBM to SRAM, then on chip updated as $\mathbf{dQ}_i \leftarrow \mathbf{dQ}_i + \mathbf{dS}_i^{(j)} \mathbf{K}_j$, and written back to HBM. FlashAttention-2 thus parallelizes over the sequence length dimension as well for the backward pass, and schedules 1 thread block for each column block. Atomic adds are used to communicate between different thread blocks to update $\mathbf{dQ}$.

The parallelization scheme is described in Fig. 2.

**Figure 2** (p. 8): "In the forward pass (left), we parallelize the workers (thread blocks) where each worker takes care of a block of rows of the attention matrix. In the backward pass (right), each worker takes care of a block of columns of the attention matrix."

The figure shows a grid visualization of the attention matrix. In the forward pass (left), 5 workers each take a row of blocks, colored distinctly per worker. In the backward pass (right), 5 workers each take a column of blocks, colored distinctly per worker. Diagonal blocks are highlighted in a darker shade to indicate the causal mask boundary.

^3 https://github.com/openai/triton/blob/main/python/tutorials/06-fused-attention.py

## 3.3 Work Partitioning Between Warps [p. 9]

[p. 9] As Section 3.2 describes how to schedule thread blocks, even within each thread block, the work must also be partitioned between different warps. Typically 4 or 8 warps per thread block are used, and the partitioning is described in Fig. 3.

**Forward pass.** [p. 9] For each block, FlashAttention splits $\mathbf{K}$ and $\mathbf{V}$ across 4 warps while keeping $\mathbf{Q}$ accessible by all warps. Each warp multiplies to get a slice of $\mathbf{Q}\mathbf{K}^\top$, then they need to multiply with a slice of $\mathbf{V}$ and communicate to add up the result. This is referred to as the "split-K" scheme. However, this is inefficient since all warps need to write their intermediate results out to shared memory, synchronize, then add up the intermediate results. These shared memory reads/writes slow down the forward pass in FlashAttention.

In FlashAttention-2, $\mathbf{Q}$ is instead split across 4 warps while keeping $\mathbf{K}$ and $\mathbf{V}$ accessible by all warps. After each warp performs matrix multiply to get a slice of $\mathbf{Q}\mathbf{K}^\top$, they just need to multiply with their shared slice of $\mathbf{V}$ to get their corresponding slice of the output. There is no need for communication between warps. The reduction in shared memory reads/writes yields speedup (Section 4).

**Figure 3** (p. 9): "Work partitioning between different warps in the forward pass"

The figure shows two diagrams side-by-side:
- (a) FlashAttention: $\mathbf{Q}$ is accessed by all warps (Warp 1-4), $\mathbf{K}^\top$ is split across Warp 1, 2, 3, 4. $\mathbf{V}$ is also split across Warp 1, 2, 3, 4. Blue shading indicates "Accessed by all warps" and striped shading indicates "Split across different warps."
- (b) FlashAttention-2: $\mathbf{K}^\top$ is accessed by all warps (Warp 1-4). $\mathbf{Q}$ is split across Warp 1, 2, 3, 4. $\mathbf{V}$ is accessed by all warps (Warp 1-4). This avoids the "split-K" communication overhead.

**Backward pass.** [p. 9] Similarly for the backward pass, the warps are partitioned to avoid the "split-K" scheme. However, it still requires some synchronization due to the more complicated dependency between all the different inputs and gradients $\mathbf{Q}, \mathbf{K}, \mathbf{V}, \mathbf{O}, \mathbf{dO}, \mathbf{dQ}, \mathbf{dK}, \mathbf{dV}$. Nevertheless, avoiding "split-K" reduces shared memory reads/writes and again yields speedup (Section 4).

**Tuning block sizes.** [p. 9] Increasing block sizes generally reduces shared memory loads/stores, but increases the number of registers required and the total amount of shared memory. Past a certain block size, register spilling causes significant slowdown, or the amount of shared memory required is larger than what the GPU has available, and the kernel cannot run at all. Typically blocks of size $\{64, 128\} \times \{64, 128\}$ are chosen, depending on the head dimension $d$ and the device shared memory size.

The authors manually tune for each head dimension since there are essentially only 4 choices for block sizes, but note this could benefit from auto-tuning to avoid manual labor. This is left to future work.
