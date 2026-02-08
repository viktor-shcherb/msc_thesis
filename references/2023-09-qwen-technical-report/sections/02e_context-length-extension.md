# 2.5 Context Length Extension [p. 7–8]

[p. 7–8] Transformer models have a significant limitation in terms of context length for their attention mechanism. As the context length increases, the quadratic-complexity computation leads to a drastic increase in both computation and memory costs. The authors implemented simple training-free techniques that are solely applied during inference to extend the context length of the model.

## NTK-aware interpolation

[p. 8] One of the key techniques used is NTK-aware interpolation (bloc97, 2023). Unlike position interpolation (PI) (Chen et al., 2023a) which scales each dimension of RoPE equally, NTK-aware interpolation adjusts the base of RoPE to prevent the loss of high-frequency information in a training-free manner.

## Dynamic NTK-aware interpolation

[p. 8] A trivial extension called dynamic NTK-aware interpolation is also implemented, which is later formally discussed in (Peng et al., 2023a). It dynamically changes the scale by chunks, avoiding severe performance degradation. These techniques effectively extend the context length of Transformer models without compromising computational efficiency or accuracy.

## LogN-Scaling

[p. 8] QWEN additionally incorporates LogN-Scaling (Chiang & Cholak, 2022; Su, 2023a). LogN-Scaling rescales the dot product of the query and value by a factor that depends on the ratio of the context length to the training length, ensuring that the entropy of the attention value remains stable as the context length grows.

## Window attention

[p. 8] Window attention (Beltagy et al., 2020) restricts the attention to a limited context window, preventing the model from attending to tokens that are too far away.

## Layer-wise window assignment

[p. 8] The authors observed that the long-context modeling ability of the model varies across layers, with lower layers being more sensitive in context length extension compared to the higher layers. To leverage this observation, different window sizes are assigned to each layer, using shorter windows for lower layers and longer windows for higher layers.

## Perplexity evaluation

[p. 9] **Table 3: Results of QWEN on long-context inference using various techniques.** The experimental findings reveal that the application of crucial techniques enables the model to consistently achieve low perplexity as the context length increases.

| Model                                    | 1024 | 2048 | 4096   | 8192   | 16384   |
|------------------------------------------|------|------|--------|--------|---------|
| QWEN-7B                                  | 4.23 | 3.78 | 39.35  | 469.81 | 2645.09 |
| + dynamic_ntk                            | 4.23 | 3.78 | 3.59   | 3.66   | 5.71    |
| + dynamic_ntk + logn                     | 4.23 | 3.78 | 3.58   | 3.56   | 4.62    |
| + dynamic_ntk + logn + window_attn       | 4.23 | 3.78 | 3.58   | 3.49   | 4.32    |
| QWEN-14B                                 | -    | 3.46 | 22.79  | 334.65 | 3168.35 |
| + dynamic_ntk + logn + window_attn       | -    | 3.46 | 3.29   | 3.18   | 3.42    |

The test data consists of academic papers from https://arxiv.org (footnote 3, p. 9). The results demonstrate that by combining NTK-aware interpolation, LogN-Scaling, and layer-wise window assignment, the models can effectively maintain performance in the context of over 8192 tokens.
