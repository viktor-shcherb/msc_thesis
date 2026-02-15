# 4.2 Ablation Study: 2-Stage Pipelining Experiments [p. 9, 11]

## Experimental setup [p. 9]

[p. 9] We ablate both the 2-stage WGMMA-softmax pipelining and warp-specialization for non-causal FP16 FLASHATTENTION-3 with fixed parameters (batch, seqlen, nheads, hdim) = (4, 8448, 16, 128).

## Results [p. 11]

**Table 2** (p. 11): "Pipelining ablation measurements"

| Configuration | Time | TFLOPS/s |
|--------------|------|----------|
| FLASHATTENTION-3 | 3.538 ms | 661 |
| No GEMM-Softmax Pipelining, Warp-Specialization | 4.021 ms | 582 |
| GEMM-Softmax Pipelining, No Warp-Specialization | 4.105 ms | 570 |

[p. 9] The result in Table 2 confirms that our algorithmic improvements (asynchrony with warp-specialization and overlapping between GEMM and softmax) lead to significant speedup, from 570 to 661 TFLOPS/s.
