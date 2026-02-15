# 3.2 Intra-warpgroup overlapping GEMMs and softmax (continued) [p. 7]

## Algorithm 2: FlashAttention-3 consumer warpgroup forward pass [p. 7]

**Require:** Matrices **Q**_i ∈ ℝ^(Br×d) and **K**, **V** ∈ ℝ^(N×d) in HBM, key block size B_c with T_c = ⌈N/B_c⌉

1: Reallocate predetermined number of registers as function of number of consumer warps.
2: On-chip, initialize **O**_i = (0) ∈ ℝ^(Br×d) and ℓ_i, m_i = (0), (-∞) ∈ ℝ^(B_r).
3: Wait for **Q**_i and **K**_0 to be loaded in shared memory.
4: Compute **S**_cur = **Q**_i**K**_0^T using WGMMA. Commit and wait.
5: Release the 0th stage of the buffer for **K**.
6: Compute m_i, **P**_cur and ℓ_i based on **S**_cur, and rescale **O**_i.
7: **for** 1 ≤ j < T_c - 1 **do**
8:    Wait for **K**_j to be loaded in shared memory.
9:    Compute **S**_next = **Q**_i**K**_j^T using WGMMA. Commit but do not wait.
10:   Wait for **V**_j-1 to be loaded in shared memory.
11:   Compute **O**_i = **O**_i + **P**_cur**V**_j-1 using WGMMA. Commit but do not wait.
12:   Wait for the WGMMA **Q**_i**K**_j^T.
13:   Compute m_i, **P**_next and ℓ_i based on **S**_next.
14:   Wait for the WGMMA **P**_cur**V**_j-1 and then rescale **O**_i.
15:   Release the (j % s)th, resp. (j - 1 % s)th stage of the buffer for **K**, resp. **V**.
16:   Copy **S**_next to **S**_cur.
17: **end for**
18: Wait for **V**_T_c-1 to be loaded in shared memory.
19: Compute **O**_i = **O**_i + **P**_last**V**_T_c-1 using WGMMA. Commit and wait.
20: Epilogue: Rescale **O**_i based on m_i. Compute **L**_i based on m_i and ℓ_i. Write **O**_i and **L**_i to HBM as the i-th block of **O** and **L**.

## Analysis of Algorithm 2 [p. 7]

[p. 7] Algorithm 2 functions as a replacement for the consumer path of Algorithm 1 to comprise the complete FLASHATTENTION-3 algorithm for FP16 precision. At a high-level, we use WGMMA as a metonym for asynchronous GEMM. Within the mainloop (lines 8 to 16), the second WGMMA operation of iteration j (line 11) is overlapped with softmax operations from iteration j+1 (line 13).

[p. 7] While the pipelined structure illustrated above offers theoretical performance gains, there are several practical aspects to consider:

### Compiler reordering

[p. 7] The pseudocode represents an idealized execution order but the compiler (NVCC) often rearranges instructions for optimization. This can disrupt the carefully crafted WGMMA and non-WGMMA operation pipelining sequence, potentially leading to unexpected behavior or diminished performance gains. An analysis of the SASS code shows that the compiler generates overlapped code as expected (Section B.2).

### Register pressure

[p. 7] To maintain optimal performance, register spilling should be minimized. However, the 2-stage pipeline requires additional registers to store context between stages. Specifically, an extra **S**_next must be kept in registers, leading to extra register usage of size B_r × B_c × sizeof(float) per threadblock. This increased register demand may conflict with using larger block sizes (another common optimization), which is also register-hungry. In practice, tradeoffs based on register profiling results.

### 3-stage pipelining

[p. 7] Extending the 2-stage algorithm described above, we propose a 3-stage variant that would further overlap the second WGMMA with softmax. While this approach offers the potential for even higher Tensor Core utilization, it requires even more registers due to an additional stage in the pipeline, making the trade-off between tile size and pipeline depth more difficult to balance. A detailed description of the 3-stage algorithm and its evaluation results can be found in Appendix B.3.
