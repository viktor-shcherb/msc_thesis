# B Addition Details on Algorithms [p. 18-20]

## B.1 Asynchrony Through Warp Specialization for the Backward Pass [p. 18]

Similar to the forward pass (Section 3.1) we use warp specialization to handle asynchrony. Instead of just a simple producer-consumer pattern in the forward pass, we do something more sophisticated: we all have a dQ writer, since we need to accumulate the value of dQ produced by each thread block to the global value of dQ. This dQ accumulation introduces memory contention (many thread blocks writing to the same-location so having a separate warp to handle this (along with asynchrony) will avoid blocking the rest of the warps in the thread block to perform the next computation (matmul).

We include the backward pass with warp specialization in Algorithm 3.

### Algorithm 3: FlashAttention-3 backward pass with warp specialization

**Require:** Matrices Q, K, V, O, dO ∈ ℝ^(N×d) in HBM, logsum-exp vector L ∈ ℝ^N in HBM, block sizes B_c, B_r.

1. Divide N by B_c. Set T_c = ⌈N/B_c⌉. Divide B_c = rowsum(dO ∘ O) in HBM (pointwise multiply), write D to HBM and divide it into T_c blocks D_1,...,D_{T_c} of size B_c each.

2. Divide Q into T_r = ⌈N/B_r⌉ blocks Q_1,...,Q_{T_r} of size B_r ×d each, and divide K, V into T_c = ⌈N/B_c⌉ blocks K_1,...,K_{T_c} and V_1,...,V_{T_c} of size B_c ×d each.

3. Divide dO into T_r blocks dO_1,...,dO_{T_r} of size B_r ×d each, and divide L into T_r blocks L_1,...,L_{T_r} of size B_r each.

4. Initialize pipeline object to manage barrier synchronization with s-stage circular SMEM buffer.

5. **if** in producer warpgroup **then**

6. Deallocate predetermined number of registers.

7. Issue load K_j and V_j from HBM to shared memory.

8. Upon completion, commit to notify consumer of the load of K_j and V_j.

9. **for** 1 ≤ i ≤ T_r **do**

10. Wait for the (i%s)-th stage of the buffer to be consumed.

11. Issue loads of Q_i, dO_i from HBM to shared memory at the (i%s)-th stage of the buffer.

12. Upon completion, commit to notify consumers of the loads of Q_i, dO_i.

13. **end for**

14. **else if** in consumer warpgroups **then**

15. Reallocate predetermined number of registers as function of number of consumer warps.

16. On-chip, Initialize dK_j = (0)_{B_c ×d}, dV_j = (0)_{B_c ×d}.

17. Wait for K_j and V_j to be loaded in shared memory.

18. **for** 1 ≤ i ≤ T_r **do**

19. Wait for Q_i to be loaded in shared memory.

20. Load L_i, D_i from HBM to on-chip SRAM.

21. On chip, compute S_i^(j) = Q_iK_j^T ∈ ℝ^(B_r×B_c) (SS-GEMM). Commit.

22. Wait for dO_i to be loaded in shared memory.

23. On chip, compute dP_i^(j) = dO_iV_j^T ∈ ℝ^(B_r×B_c) (SS-GEMM). Commit.

24. On chip, wait for S_i^(j), then compute P_i^(j) = exp(S_{ij} - L_i) ∈ ℝ^(B_r×B_c).

25. On chip, wait for dP_i^(j), then compute dS_i^(j) = P_i^(j) ∘ (dP_i^(j) - D_i) ∈ ℝ^(B_r×B_c).

26. On chip, compute dV_j ← dV_j + (P_i^(j))^T dO_i ∈ ℝ^(B_c×d) (RS-GEMM). Commit.

27. On chip, compute dK_j ← dK_j + dS_i^(j))^T Q_i ∈ ℝ^(B_c×d) (RS-GEMM). Commit and wait for both dV_j and dK_j.

28. On chip, compute dQ_i^(local) = dS_i^(j)K_j ∈ ℝ^(B_r×d) (SS-GEMM), and write dQ_i^(local) to smem. Notify the dQ-writer.

29. **end for**

30. **else if** in dQ-writer warp **then**

31. **for** 1 ≤ i ≤ T_r **do**

32. Wait for dQ_i^(local) to be ready in smem.

33. Using a semaphore, atomically add dQ_i^(local) to dQ_i in global memory.

34. **end for**

35. **end if**

## B.2 2-Stage Pipelining SASS Analysis [p. 19]

We give simplified SASS code for the inside of the consumer warpgroup mainloop.

```
// Compute row_max
FMNMX.FTZ R0, R24, R6, !PT ;
SHFL.BFLY PT, R185, R2, 0x2, 0x1f ;
... FMNMX and SHFL.BFLY ...

// Apply exp2 and row_sum. Rescale O.
FMUL.FTZ R2, R4, UR9 ;
MUFU.EX2 R185, R184 ;
FFMA.FTZ R24, R24, UR9, -R6.reuse ;
FADD.FTZ R24, R211, R24 ;
... FMUL, FFMA, FMUL, MUFU.EX2, FADD ...

// FP32 -> FP16 conversion are interleaved with exp2, row_sum and O rescaling.
F2FP.F16.F32.PACK_AB R231, R26, R231 ;
... F2FP, FMUL, MUFU, FFMA, FADD ...

// Start the first WGMMA. Broken down into 8 HGMMAs.
// The first 7 HGMMAs are packed together.
WARPGROUP.ARRIVE ;
HGMMA.64x192x16.F32 R24, gdesc[UR44], R2, !UPT ;
... HGMMA x 6 ...

// FP32->FP16, exp2, row_sum, O rescaling are interleaved with HGMMA.
F2FP.F16.F32.PACK_AB R214, R214, R187 ;
MUFU.EX2 R234, R5 ;
FADD.FTZ R237, R187, R2 ;
... F2FP, MUFU, FADD ...

// The last HGMMA is issued here. No need to wait.
HGMMA.64x192x16.F32 R24, gdesc[UR44], R24, gsb0 ;

// Start the second WGMMA. Broken down into 12 HGMMAs.
// All 12 HGMMAs are packed together. Not interleaved with other instructions.
WARPGROUP.ARRIVE ;
HGMMA.64x128x16.F32 R120, R228, gdesc[UR8].tnspB, R120 ;
... HGMMA x 10 ...
HGMMA.64x128x16.F32 R120, R184, gdesc[UR8].tnspB, R120, gsb0 ;

// wgmma.wait_group at the end.
WARPGROUP.DEPBAR.LE gsb0, 0x0 ;
```

We make the following observations:

1. Softmax is reordered to the very beginning, even before the first WGMMA.

2. The first WGMMA is interleaved with softmax and FP32 → FP16 datatype conversion of S. This indicates that WGMMA and non-WGMMAs are executed in parallel.

3. exp2, row\_sum, O rescaling and FP32 → FP16 conversions are interleaved together.

4. The second WGMMA is not overlapped with other instructions, as expected.

Overall, SASS shows that the 2-stage pipelining idea works as expected.

## B.3 3-Stage Pipelining Algorithm [p. 20]

We experiment with a 3-stage pipelining algorithm to parallelize the first WGMMA from iteration i + 2, softmax from iteration j + 1, and the second WGMMA from iteration j. We describe this algorithm in Algorithm 4. This algorithm behaves worse than the 2-stage pipelining algorithm due to the reasons below:

[Figure 8: 3-Stage Pipelining - A timeline diagram showing the execution of WGMMA0 (iterations 0-N-1), Softmax (iterations 0-N-1), and WGMMA1 (iterations 0-N-1) with overlapping stages]

**Figure 8** (p. 20): "3-Stage Pipelining"

Description: Timeline diagram showing three rows (WGMMA0, Softmax, WGMMA1) with numbered boxes representing iterations. The boxes are offset to show pipelining, with iterations overlapping across the three stages. The diagram illustrates how the algorithm attempts to parallelize computation from different iterations.

### Algorithm 4: FlashAttention 3-stage pipelining consumer warpgroup forward pass

**Require:** Matrices Q, K, V ∈ ℝ^(N×d) in HBM, block sizes B_c, B_r. Each warpgroup reads 1 block Qi of size B_r ×d, T_c = ⌈N/B_c⌉. Each warpgroup reads K_r from HBM. Each warpgroup writes 1 output block O_i of size B_r ×d, and 1 logsum-exp block L_i of size B_r.

1. Initialization. Load Q_i from HBM to on-chip SRAM. Initialize O_i, ℓ_i, m_i, scale_o.

2. Wait for the producer warpgroup loading K_0 from HBM to on-chip SRAM.

3. Compute S = Q_iK_0^T using WGMMA. Commit and wait.

4. Compute m_i, P_i, ℓ_i, scale_o based on S.

5. Wait for the producer warpgroup loading K_1 from HBM to on-chip SRAM.

6. Compute S = Q_iK_1^T using WGMMA. Commit and wait.

7. **for** 2 ≤ j < T_c - 2 **do**

8. Wait for the producer warpgroup loading K_j from HBM to on-chip SRAM.

9. Compute S_next = Q_iK_j^T using WGMMA. Commit but do not wait.

10. Wait for the producer warpgroup loading V_{j-2} from HBM to on-chip SRAM.

11. Rescale O_i based on scale_o.

12. Compute O_i = O_i + P_iV_{j-2} using WGMMA. Commit but do not wait.

13. Compute m_i, P_i, ℓ_i, scale_o based on S.

14. Wait for all previous WGMMAs.

15. Copy S_next to S.

16. Copy P_i_next to P_i.

17. **end for**

18. Wait for the producer warpgroup loading V_{T_c-2} from HBM to on-chip SRAM.

19. Rescale O_i based on scale_o.

20. Compute O_i = O_i + P_iV_{T_c-2} using WGMMA. Commit and wait.

21. Compute m_i, P_i, ℓ_i, scale_o based on S.

22. Wait for the producer warpgroup loading V_{T_c-1} from HBM to on-chip SRAM.

23. Rescale O_i based on scale_o.

24. Compute O_i = O_i + P_iV_{T_c-1} using WGMMA. Commit and wait.

25. Epilogue. Rescale O_i based on ℓ_i. Compute L_i based on ℓ_i and m_i. Write O_i and L_i to HBM as the i-th block of O and L.

**Overlapping:** We expected that softmax can be overlapped with (the first WGMMA + the second WGMMA). However, the compiler doesn't cooperate in this way. SASS code shows that only the first WGMMA is overlapped with softmax, while the second WGMMA is not. It's not clear why the compiler chooses to reorder instructions in this way.

**Register pressure:** This algorithm requires more registers compared to the 2-stage pipelining algorithm. In theory, it needs to store an extra P_i and scale_o, which is of size B_r × B_c ×sizeof(input_data_type) + B_r ×sizeof(float). As a result, a smaller block size needs to be chosen.
