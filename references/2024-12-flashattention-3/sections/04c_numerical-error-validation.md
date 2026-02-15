# 4.3 Numerical Error Validation [p. 10-11]

## Experimental setup [p. 10-11]

[p. 10] As there has been interest in the numerical error [21] of FLASHATTENTION, we compare FLASHATTENTION-2, FLASHATTENTION-3, and a standard implementation of attention against a reference implementation in FP64. To simulate outlier features and activations in LLMs [20, 54], we generate the entries of **Q**, **K**, **V** with the following distribution:

N(0, 1) + N(0, 100) · Bernoulli(0.001).

[p. 11] That is, each entry is normally distributed with zero mean and standard deviation 1, but for 0.1% of entries we add an independent term that's much larger (with mean zero and standard deviation 10). We then measure the root mean squared error (RMSE) in Table 3.

## Results: FP16 accuracy [p. 11]

[p. 11] In FP16, both FLASHATTENTION-2 and FLASHATTENTION-3 achieves 1.7× lower RMSE compared to the standard implementation since intermediate results (softmax) are kept in FP32. The baseline attention in FP8 uses per-tensor scaling, with matmul accumulator in FP32 and intermediate softmax results kept in FP16.

## Results: FP8 accuracy [p. 11]

[p. 11] Thanks to block quantization and incoherent processing, FLASHATTENTION-3 in FP8 is 2.6× more accurate than this baseline.

**Table 3** (p. 12): "Numerical error comparisons in FP16 and FP8 (e4m3)"

| Method | Baseline FP16 | FLASHATTENTION-2 FP16 | FLASHATTENTION-3 FP16 |
|--------|---------------|----------------------|----------------------|
| RMSE   | 3.2e-4        | 1.9e-4               | 1.9e-4               |

| Method | Baseline FP8 | FLASHATTENTION-3 FP8 | No block quant | No incoherent processing |
|--------|--------------|---------------------|----------------|-------------------------|
| RMSE   | 2.4e-2       | 9.1e-3              | 9.3e-3         | 2.4e-2                  |

## Results: Backward pass [p. 11]

**Figure 6** (p. 11): "Attention backward speed (FP16/BF16) on H100 GPU"

Description: Two bar charts comparing attention implementations in backward pass
- Key elements:
  - (a) Backward, without causal mask, head dim 64
  - (b) Backward, without causal mask, head dim 128
  - X-axis: Sequence length (512, 1k, 2k, 4k, 8k, 16k)
  - Y-axis: Speed (TFLOPS/s)
  - Four bars per sequence length: Standard attention (blue), FlashAttention-2 (orange), cuDNN (red/purple), FlashAttention-3 (dark purple)
- Notable patterns:
  - For head dim 64 (a): FA-3 reaches ~476 TFLOPS/s at 16k seqlen
  - For head dim 128 (b): FA-3 reaches ~581 TFLOPS/s at 16k seqlen
  - FlashAttention-3 consistently outperforms other implementations
  - Performance gap increases with sequence length
- Supports claim: Demonstrates that FLASHATTENTION-3 is 1.5-1.75× faster than FLASHATTENTION-2 in the backward pass [p. 9]

## Results: FP8 forward pass [p. 11]

**Figure 7** (p. 11): "Attention forward speed (FP8) on H100 GPU"

Description: Two bar charts comparing FP8 attention implementations
- Key elements:
  - (a) Forward, without causal mask, head dim 256
  - (b) Forward, with causal mask, head dim 256
  - X-axis: Sequence length (512, 1k, 2k, 4k, 8k, 16k)
  - Y-axis: Speed (TFLOPS/s)
  - Three bars per sequence length: Triton (green), cuDNN (red/purple), FlashAttention-3 (dark purple)
- Notable patterns:
  - For without causal mask (a): FA-3 reaches ~1,171 TFLOPS/s at 16k seqlen
  - For with causal mask (b): FA-3 reaches ~1,056 TFLOPS/s at 16k seqlen
  - FlashAttention-3 achieves close to 1.2 PFLOPS/s as stated in abstract
  - Consistently outperforms both Triton and cuDNN implementations
  - Performance advantage is maintained across all sequence lengths
- Supports claim: Validates that FP8 FLASHATTENTION-3 reaches close to 1.2 PFLOPS/s [p. 1, abstract]
