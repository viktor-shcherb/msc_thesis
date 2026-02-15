# 3.1 Producer-Consumer asynchrony through warp-specialization and pingpong scheduling [p. 4-6]

## Warp-specialization

[p. 4] As with FLASHATTENTION-2, the forward pass of FLASHATTENTION-3 is embarrassingly parallel in the batch size, number of heads, and query sequence length. Thus, it will suffice to give a CTA-level view of the algorithm, which operates on a tile **Q**_i of the query matrix to compute the corresponding tile **O**_i of the output. To simplify the description, we first give the warp-specialization scheme with a circular SMEM buffer that does *not* have in addition the GEMM-softmax overlapping. Let d be the head dimension, N the sequence length, and fix a query block size B_c to divide **Q** into T_c = ⌈N/B_c⌉ blocks **Q**_1,..., **Q**_T_c.

### Algorithm 1: FLASHATTENTION-3 forward pass without intra-consumer overlapping—CTA view

**Require:** Matrices **Q**_i ∈ ℝ^(B_c×d) and **K**, **V** ∈ ℝ^(N×d) in HBM, key block size B_r with T_r = ⌈N/B_r⌉

1: Initialize pipeline object to manage barrier synchronization with x-stage circular SMEM buffer.
2: **if** in producer warpgroup **then**
3:     Deallocate predetermined number of registers.
4:     Issue load **Q**_i from HBM to shared memory.
5:     Upon completion, commit to notify consumer of the load of **Q**_i.
6:     **for** 0 ≤ j < T_r **do**
7:         Wait for the (j % x)th stage of the buffer to be consumed.
8:         Issue loads of **K**_j, **V**_j from HBM to shared memory at the (j % x)th stage of the buffer.
9:         Upon completion, commit to notify consumers of the loads of **K**_j, **V**_j.
10:    **end for**
11: **else**
12:    Reallocate predetermined number of registers as function of number of consumer warps.
13:    On-chip, initialize **O**_i = (0) ∈ ℝ^(B_c×d) and ℓ_i, m_i = (0), (−∞) ∈ ℝ^(B_c).
14:    Wait for **Q**_i to be loaded in shared memory.
15:    **for** 0 ≤ j < T_r **do**
16:        Wait for **K**_j to be loaded in shared memory.
17:        Compute **S**_i^(j) = **Q**_i**K**_j^T (SS-GEMM). Commit and wait.
18:        Store m_i^old = m_i and compute m_i = max(m_i^old, rowmax(**S**_i^(j))).
19:        Compute **P̃**_i^(j) = exp(**S**_i^(j) − m_i) and ℓ_i = exp(m_i^old − m_i)ℓ_i + rowsum(**P̃**_i^(j)).
20:        Wait for **V**_j to be loaded in shared memory.
21:        Compute **O**_i = diag(exp(m_i^old − m_i))^(−1)**O**_i + **P̃**_i^(j)**V**_j (RS-GEMM). Commit and wait.
22:        Release the (j % x)th stage of the buffer for the producer.
23:    **end for**
24:    Compute **O**_i = diag(ℓ_i)^(−1)**O**_i and L_i = m_i + log(ℓ_i).
25:    Write **O**_i and L_i to HBM as the ith block of **O** and L.
26: **end if**

[p. 5] For our implementation of Algorithm 1 on Hopper, we use setmaxnreg for (de)allocations, TMA for loads of **Q**_i and {**K**_j, **V**_j}_0≤j<T_r, and WGMMA to execute the GEMMs for the consumer mainloop, with the SS or RS prefix indicating whether the first operand is sourced from shared memory or register file. For interpreting the execution flow of Algorithm 1, note that issuing TMA loads does not stall on the completion of other loads due to asynchrony. Moreover, in the producer mainloop, no waits and issued = x iterations as the buffer gets filled.

## Pingpong scheduling

[p. 5] The asynchronous nature of WGMMA and TMA, along with warp-specialization, opens up the opportunity to overlap the softmax computation of one warpgroup with the GEMM of another warpgroup. To motivate this, notice that non-matmul operations have much lower throughput than matmul operations on modern hardware accelerators. As an example, H100 GPU can do 989 TFLOPS of FP16 matmul but only 3.9 TFLOPS of special functions such as exponential⁵ (necessary for softmax). For the attention forward pass in FP16 with head dimension 128, there are 512× floatmul FLOPS compared to exponential operations, but the exponential has 256× lower throughput, so exponential can take 50% of the cycle compared to matmul. The situation is even worse with FP8, where the matmul throughput doubles but the exponential throughput stays the same.

[p. 5] Since the exponential is performed by a separate hardware unit (the multi-function unit), ideally we'd want the exponential calculation to be scheduled when the Tensor Cores are performing the matmul. To do so, we use synchronization barriers (bar.sync instructions) to force the GEMMs (GEMM1 = PV of one iteration, and GEMM0 = QK^⊤ of the next iteration) of warpgroup 1 to be scheduled before the GEMMs of warpgroup 2. As a result, the softmax of warpgroup 1 will be scheduled while warpgroup 2 is performing its GEMMs. Then the roles swap, with warpgroup 2 doing softmax while warpgroup 1 doing GEMMs (hence, "pingpong" scheduling). This is illustrated

---

⁵ The CUDA programming guide specifies that 16 operations of special functions can be performed per streaming multiprocessor (SM) per clock cycle. We multiply 16 by 132 SMs and 1830 MHz clock speed to get 3.9 TFLOPS of special functions.
