# Appendix C: Pretraining Hyperparameters [p. 82]

[p. 82] The authors conduct their runs using the WSD scheduler, following the guideline from Hagele et al. (2024), which recommends setting the maximal learning rate (LR) to half of what would typically be used with a cosine scheduler. They also apply LR cooldown with a (1-sqrt) decay shape. They employ the AdEMAMix optimizer, which has recently shown promising results for pretraining.

Compared to AdamW, AdEMAMix introduces two additional hyperparameters beyond the standard ones (e.g., beta_1, beta_2, weight decay): the first-moment parameter beta_3 and alpha, which controls the influence of the slow exponential moving average on the weight update. Stable training requires warmup for both alpha and beta_3. As shown in Pagliardini et al. (2025), these parameters can be scheduled independently of the LR, and it is not necessary to continue scheduling them throughout the entire training. Following this observation, they set the warmup for alpha and beta_3 to 100,000 steps, i.e., before the first checkpoint of WSD. For the rest of the training, alpha and beta_3 remain unchanged.

Another important consideration is the choice of beta parameters. Many prior settings for large-scale training use the basic values of (beta_1 = 0.9, beta_2 = 0.95). However, Semenov et al. (2025) shows that higher values, especially for beta_2, are beneficial when training spans millions of iterations. In line with this, they increase beta_2 to 0.999 and beta_3 to 0.9999 during pretraining, which reduces variance in gradient estimates and improves stability at scale. Interestingly, they also find this strategy effective for post-training: when training runs for fewer iterations, lowering (beta_2, beta_3) yields better results.

## Table C.4: Model Architecture and Hyperparameters for Pretraining

**Table C.4** (p. 82): Apertus Model Architecture and Hyperparameters for Pretraining.

| Hyperparameters | Value |
|---|---|
| Position Embedding Type | RoPE |
| RoPE theta during main pretraining | 500'000 |
| Max Position Embeddings during main pretraining | 4096 |
| RoPE theta after 64k context expansion | 12'000'000 |
| Rope Scaling Factor (NTK) | 8 |
| Weight Decay | 0.1 |
| Gradient Clipping | 0.1 |
| Adam beta | (0.9, 0.999) |
| AdEMAMix alpha | 8 |
| AdEMAMix beta_3 | 0.9999 |
| AdEMAMix alpha, beta_3 Warmup | 100'000 |
| LR Decay Style | WSD |
| LR WSD Decay Style | 1-sqrt |
| LR Warmup Duration | 16.78BT |
| Goldfish k | 50 |
| Goldfish h | 50 |
| Initialization std | 0.008944 |
