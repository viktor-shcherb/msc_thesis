# 3.1 Producer-Consumer asynchrony (continued) [p. 6]

[p. 6] in Fig. 1. Though in practice the pingpong scheduling is not as clean as depicted in the figure, we generally find this to improve performance (e.g., from 570 TFLOPS to 620-640 TFLOPS for FP16 forward with head dimension 128 and sequence length 8192).

**Figure 1** (p. 6): "Pingpong scheduling for 2 warpgroups to overlap softmax and GEMMs: the softmax of one warpgroup should be scheduled when the GEMMs of another warpgroup are running. The same color denotes the same iteration."

Description: Timeline diagram showing two warpgroups executing operations
- Key elements: Two horizontal timelines labeled "Warpgroup 1" and "Warpgroup 2", with boxes representing GEMM0, Softmax, GEMM1, GEMM0 (second iteration), Softmax operations arranged along a time axis
- Notable patterns: Operations are staggered between the two warpgroups such that when one warpgroup performs softmax, the other performs GEMMs. The same color coding indicates operations belonging to the same iteration across both warpgroups.
- Supports claim: Illustrates the pingpong scheduling strategy where softmax computation of one warpgroup overlaps with GEMM computation of another warpgroup to hide the low-throughput softmax operations [p. 5]

### Attention variants

[p. 6] For multi-query attention [51] and grouped query attention [3], we follow the approach in FLASHATTENTION-2 and adjust the tensor indexing to avoid duplicating **K** and **V** in HBM.

# 3.2 Intra-warpgroup overlapping GEMMs and softmax [p. 6]

[p. 6] Even within one warpgroup, we can overlap some instructions in the softmax with some instructions in the GEMMs. We describe one technique to do so.

[p. 6] In the attention algorithm, operations within the inner loop (main loop) have sequential dependencies that impede parallelization within a single iteration. For example, (local) softmax (lines 18 to 19) relies on the output **S**_i^(j) of the first GEMM, while the second GEMM uses **P̃**_i^(j) as an operand. Indeed, the exit statements in lines 17 and 21 of Algorithm 1 serialize the execution of softmax and GEMMs. However, we can break these dependencies by pipelining across iterations through additional buffers in registers. Pursuing this idea, we propose the following two-stage⁶ GEMM-softmax pipelining algorithm:

**Figure 2** (p. 6): "2-stage WGMMA-softmax pipelining"

Description: Timeline diagram showing pipelined execution of WGMMA and softmax operations
- Key elements: Three horizontal timelines labeled "WGMMA0", "Softmax", and "WGMMA1", with numbered boxes (0, 1, 2, ..., N-2, N-1) representing iterations arranged along a time axis
- Notable patterns: The operations are staggered such that:
  - WGMMA0 executes iterations 0, 1, 2, ..., N-1
  - Softmax executes iterations 0, 1, 2, ..., N-1 with a one-stage delay
  - WGMMA1 executes iterations 0, 1, ..., N-2, N-1 with a two-stage delay
  The staggering shows how softmax for iteration i overlaps with WGMMA operations for iterations i+1 and i+2.
- Supports claim: Illustrates the 2-stage pipelining technique that breaks sequential dependencies between GEMMs and softmax by using additional register buffers, allowing operations from different iterations to overlap [p. 6]

---

⁶ Note that the number of stages of the overlapping scheme is bounded by, but need not equal, the number x of stages in the circular SMEM buffer.
