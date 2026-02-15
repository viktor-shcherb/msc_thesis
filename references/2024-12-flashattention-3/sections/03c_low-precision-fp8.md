# 3.3 Low-precision with FP8 [p. 7-9]

## Efficiency: layout transformations [p. 7-8]

[p. 7] Computing the forward pass of FLASHATTENTION-3 in FP8 precision poses additional challenges not encountered for FP16 in terms of layout conformance.

[p. 8] First, we note that the input tensors **Q**, **K**, and **V** are typically given as contiguous in the head dimension, while to satisfy the k-major constraint on FP8 WGMMA for the second GEMM we need **V**, or rather the tiles of **V** loaded into SMEM, to be contiguous along the sequence length dimension. Since the TMA load itself cannot change the contiguous dimension, we then need to either (1) transpose **V** in GMEM as a pre-processing step, or (2) do an in-kernel transpose of tiles of **V** after loading them into SMEM. To implement option (1), we can either (1a) fuse the transpose to the epilogue of a preceding layer, or (1b) call a standalone pre-processing transpose kernel⁷ to exchange the strides of the sequence length and head dimensions. However, (1a) is difficult to integrate into a standard library, and (1b) would be wasteful in a memory-bound situation such as inference.

[p. 8] Instead, for FP8 FLASHATTENTION-3 we opt for option (2). For the in-kernel transpose, we take advantage of the LDSM (ldmatrix) and STSM (stmatrix) instructions, which involve a warp of threads collectively loading SMEM to RMEM and storing RMEM to SMEM as a granularity of 128 bytes.⁸ The LDSM/STSM instructions are both register efficient, allowing us to execute them in the producer warpgroup, and capable of transposing layouts when doing memory copy. Moreover, after the first iteration when the next V tile will arrive, the transpose of the next V tile to be executed in the shadow of the two WGMMAs that involve the preceding V and current K tile.

[p. 8] Second, we observe that unlike with FP16, the memory layout of the FP32 accumulator of an FP8 WGMMA is different from that assumed for its operands. We depict fragments of these two layouts in Fig. 3 and Fig. 4, where the entries are held in registers per thread in the listed order. By using byte permute instructions, we can then transform the WGMMA's accumulator into a column-major format suitable for the second WGMMA, and compatibly with the layout of the V tile produced by the in-kernel transpose. Specifically, with reference to Fig. 4, we can change the order in columns to

{d0 d1 d4 d5 d2 d3 d6 d7},

and this register permutation is then replicated over every 8 bytes. In terms of the logical shape of the **P** tile, this maneuver permutes its columns (e.g., columns 0189 now become the first four columns). For WGMMA to then compute the correct output tile, we can correspondingly arrange for the in-kernel transpose to write out a matching row permutation of the **V** tile.⁹

**Figure 3** (p. 8): "FP32 accumulator register WGMMA layout – rows 0 and 8, threads 0-3, entries 0-7."

Description: Register layout table showing data arrangement
- Key elements: Two rows of colored cells containing coordinate pairs in format "T{thread} ({register},{entry})" such as "T0 (d0, d1)", "T1 (d0, d1)", etc. Rows represent threads 0-3, entries 0-7 for rows 0 and 8.
- Notable patterns: Shows how FP32 accumulator data is distributed across threads and registers in WGMMA for rows 0 and 8
- Supports claim: Illustrates the memory layout of FP32 accumulator which differs from FP8 operand layout and requires transformation [p. 8]

**Figure 4** (p. 8): "FP8 operand A register WGMMA layout – rows 0 and 8, threads 0-3, entries 0-7."

Description: Register layout table showing data arrangement
- Key elements: Two rows of colored cells containing coordinate pairs in format "T{thread} ({register},{entry})" for threads 0-3, entries 0-7 for rows 0 and 8. Pattern shows "T0 (a0, a1)", "T0 (a2, a3)", etc.
- Notable patterns: Shows how FP8 operand data is organized differently from the FP32 accumulator layout
- Supports claim: Illustrates the operand layout that must be reconciled with the accumulator layout through byte permute instructions to enable correct WGMMA computation [p. 8]

## Accuracy: block quantization and incoherent processing [p. 8-9]

[p. 8-9] With FP8 (e4m3) format, one only uses 3 bits to store the mantissa, and 4 bits for the exponent. This results in higher numerical error than FP16/BF16. Moreover, large models typically have outlier values [20, 54] that are much larger in magnitude than most other values, making quantization difficult. One typically use per-tensor scaling [37] by keeping one scalar per tensor (e.g., one for **Q**, **K**, and for **V**). To reduce the quantization error in FP8, we employ two techniques:

1. **Block quantization**: we keep one scalar per block, so that for each of **Q**, **K**, **V** we split the tensor into blocks of size B_r × d or B_c × d and quantize them separately. This quantization can be fused with an operation right before attention (e.g., rotary embedding [57] is typically applied to **Q** and **K** before attention) to slow down (since rotary embedding is memory-bandwidth bound). As the FLASHATTENTION-3 algorithm naturally operates on blocks, we can scale each block of **S** to account for this block quantization at no computation cost.

2. **Incoherent processing**: to even out outliers, we multiply **Q** and **K** with a random orthogonal matrix **M** before quantizing to FP8. Since **M** is orthogonal, **MM**^T = **I** and so (**QM**)(**KM**)^T = **QK**^T, i.e., multiplying both **Q** and **K** with **M** does not change the attention output. This serves to "spread out" the outliers: since each row of **QM** or **KM** is a random sum of entries of **Q** or **K**, thus reducing quantization error. In practice, we follow Chee et al. [9] and Tseng et al. [58] and choose **M** to be the product of random diagonal matrices of ±1 and a Hadamard matrix, which can be multiplied in O(d log d) instead of O(d²), and can also be fused with the rotary embedding at no extra computation cost.

[p. 9] We validate that these two techniques reduces numerical error by up to 2.6× in §4.3.

---

⁷ An optimized transpose kernel will achieve speed near the bandwidth of the device [46].

⁸ In the PTX documentation, LDSM/STSM are described as copying 8×8 matrices with 16-bit entries [40, §9.7.13.4.15-16], but we can pack 8-bit entries two at a time to use the LDSM/STSM in the context of FP8 precision. However, the transposed versions of LDSM/STSM cannot split packed 8-bit entries, which necessitates certain register movements in between LDSM and STSM to actually perform a tile-wise transpose; we omit the details.

⁹ This additional freedom afforded by doing the in-kernel transpose eliminates having to use shuffle instructions to change register ownership across threads, which we previously described in [7].
