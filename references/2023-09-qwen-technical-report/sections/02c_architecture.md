# 2.3 Architecture [p. 6–7]

[p. 6] QWEN is designed using a modified version of the Transformer architecture. The authors adopted the recent open-source approach of training large language models, LLaMA (Touvron et al., 2023a), which is widely regarded as the top open-source LLM. Modifications to the architecture include:

## Embedding and output projection

[p. 7] Based on preliminary experimental findings, the authors opted for the untied embedding approach instead of tying the weights of input embedding and output projection. This decision was made to achieve better performance at the price of memory costs.

## Positional embedding

[p. 7] RoPE (Rotary Positional Embedding) (Su et al., 2021) is chosen as the preferred option for incorporating positional information. RoPE has been widely adopted and has demonstrated success in contemporary large language models, notably PaLM (Chowdhery et al., 2022; Anil et al., 2023) and LLaMA (Touvron et al., 2023a,b). FP32 precision is used for the inverse frequency matrix, rather than BF16 or FP16, in order to prioritize model performance and achieve higher accuracy.

## Bias

[p. 7] For most layers, biases are removed following Chowdhery et al. (2022), but biases are added in the QKV layer of attention to enhance the extrapolation ability of the model (Su, 2023b).

## Pre-Norm & RMSNorm

[p. 7] Pre-normalization is used, which has been shown to improve training stability compared to post-normalization. The traditional layer normalization technique described in (Ba et al., 2016) is replaced with RMSNorm (Jiang et al., 2023). This change resulted in equivalent performance while also improving efficiency.

## Activation function

[p. 7] SwiGLU (Shazeer, 2020) is selected as the activation function, a combination of Swish (Ramachandran et al., 2017) and Gated Linear Unit (Dauphin et al., 2017). Initial experiments showed that activation functions based on GLU generally outperform other baseline options, such as GeLU (Hendrycks & Gimpel, 2016). As is common practice in previous research, the dimension of the feed-forward network (FFN) is reduced from 4 times the hidden size to 8/3 of the hidden size.

## Model configurations

[p. 7] **Table 1: Model sizes, architectures, and optimization hyper-parameters.**

| # of Params | Hidden size | Heads | Layers | Learning rate       | Batch size | Training tokens |
|-------------|-------------|-------|--------|---------------------|------------|-----------------|
| 1.8B        | 2048        | 16    | 24     | 3.0 x 10^{-4}      | 4M         | 2.2T            |
| 7B          | 4096        | 32    | 32     | 3.0 x 10^{-4}      | 4M         | 2.4T            |
| 14B         | 5120        | 40    | 40     | 3.0 x 10^{-4}      | 4M         | 3.0T            |
