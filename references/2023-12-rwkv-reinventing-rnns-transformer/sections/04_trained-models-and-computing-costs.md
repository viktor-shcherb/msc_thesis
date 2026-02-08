# 4 Trained Models and Computing Costs [p. 5-6]

[p. 5]

To demonstrate the scalability of RWKV, six models are trained ranging from 169 million to 14 billion parameters as shown in Table 2. All models are trained for one epoch (330 billion tokens) on the Pile (Gao et al., 2020; Biderman et al., 2022).

**Table 2** (p. 5): RWKV model architectures and FLOP counts. Further details of these hyperparameters are elaborated upon in Appendix G.

| Name | Layers | Model Dimension | Parameters | FLOP per token |
|---|---|---|---|---|
| 169 M | 12 | 768 | $1.693 \times 10^8$ | $2.613 \times 10^8$ |
| 430 M | 24 | 1024 | $4.304 \times 10^8$ | $7.573 \times 10^8$ |
| 1.5 B | 24 | 2048 | $1.515 \times 10^9$ | $2.823 \times 10^9$ |
| 3 B | 32 | 2560 | $2.985 \times 10^9$ | $5.710 \times 10^9$ |
| 7 B | 32 | 4096 | $7.393 \times 10^9$ | $1.437 \times 10^{10}$ |
| 14 B | 40 | 5120 | $1.415 \times 10^{10}$ | $2.778 \times 10^{10}$ |

The number of parameters for each model is computed using the formula:

$$\text{\# parameters} = 2VD + 13D^2L + D(11L + 4)$$

where $V = 50277$ is the vocabulary size, $D$ represents the Model Dimension and $L$ corresponds to the number of layers.

FLOPs is for a forward pass for one token. It was calculated as $2(2VD + 13D^2L)$, which is twice (add and multiply) the number of parameters in linear layers. The backwards pass FLOPs can be approximated as twice that of the forward pass, giving a total of $6(2VD + 13D^2L)$ FLOP per token. This matches the standard formula for FLOP calculations in transformers Kaplan et al. (2020): FLOP $= 6 \cdot |\text{\# tokens}| \cdot |\text{\# parameters}|$.

## 4.1 Additional Training Details

[p. 5-6]

Training uses the standard Adam optimizer without weight decay, bfloat16 precision, and a context length of 1024 tokens. Further details on hyperparameters are in Appendix G.

Diverting from standard practice for transformers, exponential decay is applied to the learning rate. The auxiliary loss introduced by PaLM (Chowdhery et al., 2022) is also incorporated, supplementing the standard cross-entropy loss function. This auxiliary loss encourages the softmax normalizer to approximate zero closely.

As for the learning rate schedule, it remains constant for the initial iterations, and subsequently decays exponentially.

## 4.2 Scaling Laws

[p. 6]

Scaling laws (Kaplan et al., 2020; Henighan et al., 2020; Hoffmann et al., 2022; Muennighoff et al., 2023) in language models refer to the mathematical relationships that describe how the performance of a language model changes with respect to various factors. These factors can include the model size ($N$), dataset size ($D$), or the optimally allocated compute budget ($C_{\min}$). Scaling laws are important for two primary reasons: they allow us to make predictions and plans regarding the costs and performance of large models before they are trained via interpolation and extrapolation (Black et al., 2022; Le Scao et al., 2022) and the contexts in which they fail provides rich feedback on important areas for future research (Wei et al., 2022a; Biderman et al., 2023a).

Previous work on scaling laws for RNNs has claimed that LSTMs do not strictly follow the same log-log linear scaling that transformers do (Kaplan et al., 2020). The authors train 45 RWKV models for a variety of pairs (dataset, parameters) and find that RWKV *does* follow the same general form of the scaling law that is well established for transformers.

**Figure 4** (p. 6): "Scaling laws curves for RWKV models"
- X-axis: Compute (exaFLOP), log scale from ~$10^{-1}$ to ~$10^2$.
- Y-axis: Loss, log scale from ~$2 \times 10^0$ to ~$4 \times 10^0$ (approximately 2.0 to 4.0).
- Three point categories plotted: Non-Optimal (black), Optimal (red), Test (blue).
- A linear Trend Line is fit to the Pareto optimal (red) points.
- The linear fit to the Pareto optimal points holds an $r^2$ value of 0.994.
- Even when extrapolating the curve an additional order of magnitude (blue test points), an extremely good fit is found with an $r^2$ of 0.875.
- The plot demonstrates that RWKV follows the same log-log linear scaling law as transformers.
