# Appendix D: Hardware-aware Algorithm For Selective SSMs [p. 28–29]

[p. 28]

Without input-dependent selectivity, SSMs can be efficiently implemented as a convolution (Dao, Fu, Saab, et al. 2023; Gu, Goel, and Re 2022), which leverages the fast Fourier transform (FFT) as primitive. With selectivity, SSMs are no-longer equivalent to convolution, but the authors leverage the parallel associative scan. While SSM scans are theoretically efficient ($O(BLDN)$ FLOPs, scaling linear in $L$), training foundation models with selective SSMs requires them to be efficient on modern hardware (GPUs) as well. The authors describe how they use *kernel fusion* and *recomputation* to make SSM scan fast and memory-efficient. They evaluate the speed of their scan implementation compared to convolution and attention in Section 4.5, showing that it is up to 7x times faster than attention at sequence length 32K, and is as memory-efficient as the best attention implementation (FlashAttention).

## Speed

[p. 28]

On modern hardware accelerators (GPUs) most operations (except matrix multiply) are bounded by memory-bandwidth (Dao, Fu, Ermon, et al. 2022; Ivanov et al. 2021; Williams, Waterman, and Patterson 2009). This is the case with the scan operation, and the authors use kernel fusion to reduce the amount of memory IOs, leading to significant speedup compared to a standard implementation.

The standard way to implement the scan algorithm in Section 3.2 is to prepare the scan input $\overline{A}, \overline{B}$ of size $(B, L, D, N)$ in GPU HBM (high-bandwidth memory, commonly referred to as GPU memory), call a parallel associative scan implementation to write the scan output of size $(B, L, D, N)$ to GPU HBM, then multiply that scan output with $C$ to produce an output of size $(B, L, D)$. However, this requires the number of memory reads/writes on the order of $O(BLDN)$. The authors instead fuse the discretization step, the scan, and the multiplication with $C$ into one kernel:

1. Read in $O(BLD + DN)$ bytes of memory ($\Delta$, $\boldsymbol{A}$, $\boldsymbol{B}$, $\boldsymbol{C}$) from slow HBM to fast SRAM.
2. Discretize to produce $\overline{A}, \overline{B}$ of size $(B, L, D, N)$ in SRAM.
3. Perform a parallel associative scan, yielding intermediate states of size $(B, L, D, N)$ in SRAM.
4. Multiply and sum with $C$, producing outputs of size $(B, L, D)$ and write it to HBM.

This way, IOs are reduced by a factor of $O(N)$ (the state dimension), which in practice speeds up the operation by 20-40 times (Section 4.5).

For sequence length $L$ too long where the sequence cannot fit in SRAM (which is much smaller than HBM), the sequences are split into chunks and the fused scan is performed on each chunk. As long as the intermediate scan states are available, the scan can continue with the next chunk.

## Memory

[p. 28–29]

The authors describe how they use the classical technique of *recomputation* to reduce the total amount of memory required to train selective SSM layers.

From the way the forward pass is fused, the intermediate states of size $(B, L, D, N)$ are not saved to avoid memory blowup. However, these intermediate states are necessary for the backward pass to compute gradients. The authors instead recompute those intermediate states in the backward pass. Since the inputs $\Delta$, $\boldsymbol{A}$, $\boldsymbol{B}$, $\boldsymbol{C}$ and output gradient read from HBM to SRAM are of size $O(BLN + DN)$, and the input gradients are also of size $O(BLN + DN)$, recomputation avoids the cost of reading $O(BLND)$ elements from HBM. This means that recomputation of the SSM states in the backward pass speeds up the computation compared to storing them and reading them from HBM.

Beyond optimizing for just the scan operation, the authors also use recomputation to optimize the memory requirement of the entire selective SSM block (input projection, convolution, activation, scan, output projection). In particular, they do not save intermediate activations that take a lot of memory but are fast to recompute (e.g. output of activation function or short convolution). As a result, the selective SSM layer has the same memory requirement as an optimized Transformer implementation with FlashAttention. In particular, each attention layer (FlashAttention) stores around 12 bytes of activations per token, an each MLP layer stores around 20 bytes of activations per token, for a total of 32 bytes (assuming mixed-precision training in FP16 or BF16). Each selective SSM stores around 16 bytes of activations per token. Hence two layers of selective SSMs have around the same activation memory as an attention layer and an MLP layer. [p. 29]
