# 4.1 Benchmarking Attention [p. 9-10]

## Experimental setup [p. 9]

[p. 9] We measure the runtime of different attention methods on an H100 80GB SXM5 GPU for different settings (without / with causal mask, head dimension 64 or 128 or 256). We report the results in Fig. 5 and Fig. 6, showing that FLASHATTENTION-3 is around 1.5-2.0× faster than FLASHATTENTION-2 in the forward pass and 1.5-1.75× faster in the backward pass. Compared to a standard attention implementation, FLASHATTENTION-3 can be up to 3-16× faster. For medium and long sequences (1k+), our reference implementation of FLASHATTENTION-3 even surpasses the speed of a vendor's library (cuDNN – closed source) that has been optimized for H100 GPUs.

### Benchmark settings [p. 9]

[p. 9] We vary the sequence length as 512, 1k, ..., 16k, and set batch size so that the total number of tokens is 16k. We set the hidden dimension to 2048, and head dimension to be either 64, 128, or 256 (i.e., 32 heads, 16 heads, or 8 heads). To calculate the FLOPs of the forward pass, we use:

4 · seqlen² · head dimension · number of heads.

[p. 9] With causal masking, we divide this number by 2 to account for the fact that approximately only half of the entries are calculated. To get the FLOPs of the backward pass, we multiply the forward pass FLOPs by 2.5 (since there are 2 matmuls in the forward pass and 5 matmuls in the backward pass, due to recomputation).

[p. 9] We then measure the runtime for FP8 for the forward pass under similar settings. We report the results for headdim 256 in Fig. 7 and give the full results in Appendix C.2.

## Results: Forward pass [p. 10]

**Figure 5** (p. 10): "Attention forward speed (FP16/BF16) on H100 GPU"

Description: Six bar charts arranged in 2×3 grid comparing attention implementations
- Key elements:
  - (a) Forward, without causal mask, head dim 64
  - (b) Forward, with causal mask, head dim 64
  - (c) Forward, without causal mask, head dim 128
  - (d) Forward, with causal mask, head dim 128
  - (e) Forward, without causal mask, head dim 256
  - (f) Forward, with causal mask, head dim 256
  - X-axis: Sequence length (512, 1k, 2k, 4k, 8k, 16k)
  - Y-axis: Speed (TFLOPS/s)
  - Five bars per sequence length: Standard attention (blue), FlashAttention-2 (orange), Triton (green), cuDNN (red/purple), FlashAttention-3 (dark purple)
- Notable patterns:
  - FlashAttention-3 consistently achieves highest speeds across all settings
  - For head dim 64 without causal mask (a): FA-3 reaches ~497 TFLOPS/s at 16k seqlen
  - For head dim 64 with causal mask (b): FA-3 reaches ~475 TFLOPS/s at 16k seqlen
  - For head dim 128 without causal mask (c): FA-3 reaches ~649 TFLOPS/s at 16k seqlen
  - For head dim 128 with causal mask (d): FA-3 reaches ~616 TFLOPS/s at 16k seqlen
  - For head dim 256 without causal mask (e): FA-3 reaches ~756 TFLOPS/s at 16k seqlen
  - For head dim 256 with causal mask (f): FA-3 reaches ~642 TFLOPS/s at 16k seqlen
  - Standard attention (blue) performs significantly worse, typically <200 TFLOPS/s
  - Performance improvements are most pronounced at longer sequence lengths (8k, 16k)
- Supports claim: Demonstrates that FLASHATTENTION-3 is 1.5-2.0× faster than FLASHATTENTION-2 and can reach up to 740 TFLOPS/s (75% utilization) on H100 GPUs [p. 9]
