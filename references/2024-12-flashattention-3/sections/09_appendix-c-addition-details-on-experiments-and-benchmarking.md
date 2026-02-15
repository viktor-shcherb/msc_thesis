# C Addition Details on Experiments and Benchmarking [p. 21]

## C.1 System and libraries [p. 21]

We benchmark the speed on an H100 80GB SXM5 (700W). We generally use the latest versions of the libraries, at the time of writing (May 2024). Specifically, we use:

- CUDA 12.3
- cuDNN 9.1.1.17
- CUTLASS 3.5
- FlashAttention 2.5.8
- Triton nightly 3.0.0.post20240424212437
- PyTorch 2.3.0

To reduce variability, we fix the GPU clock speed to 1830MHz (clock speed used to calculate the 989 TFLOPS FP16 theoretical max throughput). We repeat the benchmarks 100 times and take the average timing.

## C.2 FP8 Attention Full Results [p. 21-22]

We use following sequence lengths: 512, 1024, 2048, 4224, 8448, 16896. When sequence length ≥ 4k, we make it also divisible by 132 (number of SMs in H100 SXM5) to avoid wave quantization.

### Figure 9: Attention forward speed (FP8) on H100 GPU [p. 22]

The figure shows attention forward pass speed comparisons across Triton, cuDNN, and FlashAttention-3 implementations using FP8 precision on H100 80GB SXM5. Results are organized in 6 subplots:

**Without causal mask:**
- (a) Head dimension 64, without causal mask
- (c) Head dimension 128, without causal mask
- (e) Head dimension 256, without causal mask

**With causal mask:**
- (b) Head dimension 64, with causal mask
- (d) Head dimension 128, with causal mask
- (f) Head dimension 256, with causal mask

**Key observations from the benchmarks:**

For head dimension 64:
- Without causal mask: FlashAttention-3 achieves speeds ranging from ~350 TFLOPS at sequence length 512 to ~615 TFLOPS at sequence length 16k
- With causal mask: FlashAttention-3 achieves speeds ranging from ~250 TFLOPS at sequence length 512 to ~575 TFLOPS at sequence length 16k

For head dimension 128:
- Without causal mask: FlashAttention-3 reaches up to ~1000 TFLOPS at longer sequence lengths (8k-16k)
- With causal mask: FlashAttention-3 reaches up to ~850 TFLOPS at longer sequence lengths

For head dimension 256:
- Without causal mask: FlashAttention-3 achieves speeds up to ~1150 TFLOPS at sequence length 16k
- With causal mask: FlashAttention-3 reaches up to ~1000 TFLOPS at sequence length 16k

FlashAttention-3 consistently outperforms both Triton and cuDNN implementations across all configurations, with the performance advantage becoming more pronounced at longer sequence lengths and larger head dimensions.
