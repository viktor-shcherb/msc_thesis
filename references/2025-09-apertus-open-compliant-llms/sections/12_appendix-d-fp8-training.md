# Appendix D: FP8 Training [p. 83]

[p. 83] During the later stages of Apertus 8B pretraining, the authors experimented with enabling FP8 data formats through NVIDIA's Transformer Engine library. At ~8T consumed tokens, they adopted the Current Scaling FP8 recipe, which allowed FP8 GEMM computation for all linear projections in both the forward and backward passes, including the FFN linear layers and the QKV projections. This resulted in ~26.3% throughput increase (6.96k -> 8.79k tokens/sec/GPU), and a minor instantaneous loss increase of around 0.01. However, after a stable training for 300B tokens, this caused a more substantial loss increase as shown in Figure D.1, which led them to roll back and not use FP8 training during the main pretraining run.

In their separate work Hernandez-Cano et al. (2025), conducted after the launch of Apertus pretraining, they achieved more stable FP8 training on FOG architectures by modifying the ordering of layer normalizations. This adjustment enabled stable FP8 attention computation and substantially reduced the presence of large activation outliers across the network (He et al., 2024). As a result, it lowered the risk of numerical instability from FP8 quantization and computation, specifically underflows and overflows.

## Figure D.1

**Figure D.1** (p. 83): **FP8 Training Dynamics.** After enabling FP8 training for roughly 300B tokens, a substantial loss increase is observed, and larger gradient norm instabilities. Loss plots are smoothed with a running average window of 25 steps; gradient norm with 300 steps.

The figure consists of two panels:
- **Left panel ("8B Loss Curve"):** X-axis: Consumed Tokens (8.0T to 8.6T); Y-axis: Loss (approximately 1.85 to 1.91). Shows BF16 (blue) and FP8 (orange) loss curves. After switching to FP8 at ~8T tokens, the FP8 loss (orange) begins diverging upward from the BF16 baseline (blue) after roughly 300B tokens of FP8 training. By ~8.5T tokens the FP8 loss is noticeably higher.
- **Right panel ("8B Gradient Norms"):** X-axis: Consumed Tokens (8.0T to 8.6T); Y-axis: Gradient Norms (approximately 0.2 to 1.0). The FP8 gradient norms (orange) show larger spikes and instabilities compared to BF16 (blue), particularly visible around 8.1T-8.3T tokens, with several sharp peaks reaching ~0.8-1.0.
