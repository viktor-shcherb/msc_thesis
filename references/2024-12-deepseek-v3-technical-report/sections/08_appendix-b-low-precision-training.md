# Appendix B. Ablation Studies for Low-Precision Training [p. 47–48]

**Figure 10** (p. 47): "Loss curves comparison between BF16 and FP8 training. Results are smoothed by Exponential Moving Average (EMA) with a coefficient of 0.9."

Description: Two side-by-side line graphs showing training loss over training steps
- Left panel: "BF16 v.s. FP8 on 16B DeepSeek-v2" - Shows loss curves from 0 to ~1200 steps
- Right panel: "BF16 v.s. FP8 on 230B DeepSeek-v2" - Shows loss curves over similar range
- Both panels include inset zoomed views showing oscillatory patterns in the loss curves
- Red line represents one approach, blue line represents the other
- Loss values range from approximately 1.5 to 3.5 on the y-axis
- The curves show typical decreasing loss patterns with initial steep decline followed by gradual improvement
- Supports claim: FP8 mixed precision framework maintains training stability comparable to BF16

## B.1. FP8 vs. BF16 Training [p. 47]

The authors validate their FP8 mixed precision framework by comparing it to BF16 training on two baseline models across different scales [p. 47]:

**Small scale experiment:**
- Model: Baseline MoE model with approximately 16B total parameters
- Training data: 1.33T tokens
- Result: Relative error remains below 0.25% with high-precision accumulation and fine-grained quantization strategies [p. 47]

**Large scale experiment:**
- Model: Baseline MoE model with approximately 230B total parameters
- Training data: Around 0.9T tokens
- Result: Training curves shown in Figure 10 demonstrate comparable stability between FP8 and BF16 [p. 47]

The experiments show that the FP8 mixed precision framework maintains training quality while providing computational benefits [p. 47].

## B.2. Discussion About Block-Wise Quantization [p. 47–48]

The authors investigate the necessity of tile-wise fine-grained quantization versus block-wise quantization for different tensor operations [p. 47].

**Quantization groupings:**
- Tile-wise fine-grained quantization uses different groupings for activation quantization:
  - Forward pass: 1x128 grouping
  - Backward pass: 128x1 grouping
- Similar process required for activation gradients [p. 47]
- A straightforward strategy is to apply block-wise quantization per 128x128 elements, similar to how model weights are quantized [p. 47]
- This approach would require only transposition for backward, not regrouping [p. 47]

**Experimental findings:**
The authors conduct an experiment where all tensors associated with Dgrad (the operation computing activation gradients and back-propagating to shallow layers in a chain-like manner) are quantized on a block-wise basis [p. 47].

**Results on 16B MoE model:**
- Model: Approximately 16B total parameters
- Training: Around 300B tokens
- Observation: Block-wise quantization of activation gradients leads to model divergence [p. 48]
- Hypothesis: This sensitivity arises because activation gradients are highly imbalanced among tokens, resulting in token-correlated outliers (Xi et al., 2023) [p. 48]
- Conclusion: These outliers cannot be effectively managed by a block-wise quantization approach [p. 48]

**Citation:**
The paper cites Xi et al., 2023 in reference to token-correlated outliers in activation gradients [p. 48].
