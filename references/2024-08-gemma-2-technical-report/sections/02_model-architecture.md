# 2. Model Architecture [p. 2]

The Gemma 2 models are based on a decoder-only transformer architecture (Vaswani et al., 2017), similar to previous Gemma models (Gemma Team, 2024). The main parameters and architecture choices are summarized in Table 1. [p. 2]

## Table 1 | Overview of the main model parameters and design choices [p. 2]

| Parameters | 2B | 9B | 27B |
|---|---|---|---|
| d_model | 2304 | 3584 | 4608 |
| Layers | 26 | 42 | 46 |
| Pre-norm | yes | yes | yes |
| Post-norm | yes | yes | yes |
| Non-linearity | GeGLU | GeGLU | GeGLU |
| Feedforward dim | 18432 | 28672 | 73728 |
| Head type | GQA | GQA | GQA |
| Num heads | 8 | 16 | 32 |
| Num KV heads | 4 | 8 | 16 |
| Head size | 256 | 256 | 128 |
| Global att. span | 8192 | 8192 | 8192 |
| Sliding window | 4096 | 4096 | 4096 |
| Vocab size | 256128 | 256128 | 256128 |
| Tied embedding | yes | yes | yes |

## Table 2 | Parameter counts for the Gemma models [p. 2]

| Model | Embedding Parameters | Non-embedding Parameters |
|---|---|---|
| 2B | 590,118,912 | 2,024,517,888 |
| 9B | 917,962,752 | 8,324,201,984 |
| 27B | 1,180,237,824 | 26,047,480,320 |

The larger embedding parameter counts compared to models limited to one or a few languages are inherited from the large Gemini vocabulary (256k entries), which is designed to work on a large number of languages. [p. 2]

## Shared Elements with Gemma 1

Several architectural elements are similar to the first version of Gemma models: a context length of 8192 tokens, the use of Rotary Position Embeddings (RoPE) (Su et al., 2021), and the approximated GeGLU non-linearity (Shazeer, 2020). [p. 2]

## Key Differences from Gemma 1

A few elements differ between Gemma 1 and Gemma 2, including using deeper networks. [p. 2]

## Local Sliding Window and Global Attention

The authors alternate between a local sliding window attention (Beltagy et al., 2020a,b) and global attention (Luong et al., 2015) in every other layer. The sliding window size of local attention layers is set to 4096 tokens, while the span of the global attention layers is set to 8192 tokens. [p. 2]

## Logit Soft-Capping

Logits are capped (Bello et al., 2016) in each attention layer and the final layer such that the value of the logits stays between -soft_cap and +soft_cap. The capping function is:

logits <- soft_cap * tanh(logits / soft_cap)

The soft_cap parameter is set to 50.0 for the self-attention layers and to 30.0 for the final layer. [p. 2]

## Post-norm and Pre-norm with RMSNorm

To stabilize training, RMSNorm (Zhang and Sennrich, 2019) is used to normalize the input and output of each transformer sub-layer, the attention layer, and the feedforward layer. [p. 2]

## Grouped-Query Attention (GQA)

GQA (Ainslie et al., 2023) is used with num_groups = 2, based on ablations showing increased speed at inference time while maintaining downstream performance. [p. 2]
