# 2.4 Training [p. 7]

[p. 7] To train QWEN, the standard approach of autoregressive language modeling is followed, as described in Radford et al. (2018). This involves training the model to predict the next token based on the context provided by the previous tokens.

## Training details

- Context length: 2048
- Batching: documents are shuffled, merged, and truncated to the specified context length
- Flash Attention is employed in the attention modules (Dao et al., 2022) to improve computational efficiency and reduce memory usage
- Optimizer: AdamW (Kingma & Ba, 2014; Loshchilov & Hutter, 2017)
- Hyperparameters: beta_1 = 0.9, beta_2 = 0.95, epsilon = 10^{-8}
- Learning rate schedule: cosine schedule with a specified peak learning rate for each model size (see Table 1)
- The learning rate is decayed to a minimum of 10% of the peak learning rate
- All models are trained with BFloat16 mixed precision for training stability
