# 5 Discussion, Limitations, Conclusion [p. 12]

## Summary of contributions [p. 12]

[p. 12] With FLASHATTENTION-3, we have demonstrated that new programming techniques and hardware features such as asynchrony and low-precision can improve the efficiency and accuracy of attention. We are able to speed up attention by 1.5-2.0× times compared to FLASHATTENTION-2, and reduce FP8 numerical error by 2.6× compared to standard per-tensor quantization.

## Future work and limitations [p. 12]

[p. 12] Some limitations of our work that we hope to address in the future include: optimizing for LLM inference, integrating a persistent kernel design into the FP8 kernel[^10], and understanding the effects of low-precision attention in large-scale training.

[p. 12] Though we have focused on Hopper GPUs in this work, we expect that the techniques here will apply to other hardware accelerators. We hope that a faster and more accurate primitive such as attention will unlock new applications in long-context tasks.

[^10]: For our benchmarks, FP16 FLASHATTENTION-3 has a persistent kernel and load balancing strategy, while FP8 FLASHATTENTION-3 does not. This partly explains why FP8 FLASHATTENTION-3 does not perform as well for small sequence length and causal masking compared to the FP8 cuDNN kernels.
