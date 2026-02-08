# Appendix A. Overview of Hyper-Parameters [p. 31]

[p. 31] An overview of hyper-parameters for DeepSeekMoE across various sizes is presented. The relative expert size is in comparison to a standard FFN.

**Table 7** (p. 31): Overview of hyper-parameters for DeepSeekMoE across various sizes. The relative expert size is in comparison to a standard FFN.

| # Params | # Layers | Hidden Size | # Attn Heads | # Shared Experts | # Routed Experts | Relative Expert Size | Sequence Length | Batch Size (Sequence) | Learning Rate |
|---|---|---|---|---|---|---|---|---|---|
| 2.0B | 9 | 1280 | 10 | 1 | 63 (7 activated) | 0.25 | 2048 | 2048 | 1.08e-3 |
| 16.4B | 28 | 2048 | 16 | 2 | 64 (6 activated) | 0.25 | 4096 | 4608 | 4.2e-4 |
| 144.6B | 62 | 4096 | 32 | 4 | 128 (12 activated) | 0.125 | 4096 | 4608 | 3.0e-4 |
