# Model Architecture [p. 2-3]

Ministral 3 uses a decoder-only Transformer backbone [Vaswani et al., 2017] with size-scaled depth/width and consistent attention/head structure.

## Table 1 [p. 2]

**Table 1:** "Architectural specifications and hyperparameters for the Ministral 3 family. All models use a vocabulary size of 131K tokens."

| Model | Layers | Latent dim. | Q/KV heads | FFN dim. | Tied embeddings | Context length |
|---|---:|---:|---:|---:|:---:|---:|
| Ministral 3 14B | 40 | 5120 | 32 / 8 | 16384 | No | 256k |
| Ministral 3 8B | 34 | 4096 | 32 / 8 | 14336 | No | 256k |
| Ministral 3 3B | 26 | 3072 | 32 / 8 | 9216 | Yes | 256k |

## Shared architectural choices [p. 2-3]

- Grouped-Query Attention (GQA): 32 query heads / 8 KV heads [Ainslie et al., 2023]
- RoPE positional embeddings [Su et al., 2021]
- SwiGLU activations [Shazeer, 2020]
- RMSNorm [Zhang and Sennrich, 2019]
- YaRN + position-based softmax temperature scaling for long context [Peng et al., 2023; Nakanishi, 2025; MetaAI, 2025]

The paper notes that tied input-output embeddings are used only for the 3B model to limit embedding-parameter dominance [p. 3].

## Vision encoder [p. 3]

All Ministral 3 variants share a frozen **410M-parameter ViT** copied from Mistral Small 3.1 Base, using the Pixtral-style vision architecture [Agrawal et al., 2024].

- Frozen vision encoder across sizes.
- Projection from vision latent space to LM space is retrained separately for each target model size.
