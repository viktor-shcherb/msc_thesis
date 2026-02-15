# Appendix D: Hyperparameters for Section 3.1 [p. 18]

Table 9 presents the detailed hyperparameters for the DIFF Transformer-3B models in Section 3.1 [p. 18]. For Transformer-3B, the only difference is that there are 24 heads [p. 18]. Notice that both Transformer-3B and DIFF Transformer-3B have similar FLOPs [p. 18].

| Params | Values |
|---|---|
| Layers | 28 |
| Hidden size | 3072 |
| FFN size | 8192 |
| Vocab size | 100,288 |
| Heads | 12 |
| Adam β | (0.9, 0.95) |
| LR | 3.2 × 10⁻⁴ |
| Batch size | 4M |
| Warmup steps | 1000 |
| Weight decay | 0.1 |
| Dropout | 0.0 |

Table 9: Hyperparameters used for the DIFF Transformer-3B model in Section 3.1 [p. 18].
