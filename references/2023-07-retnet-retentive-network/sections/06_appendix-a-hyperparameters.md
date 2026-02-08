# A Hyperparameters [p. 14]

**Table 7** (p. 14): "Hyperparameters used for the models in Section 3."

| Hyperparameters | 1.3B | 2.7B | 6.7B |
|---|---|---|---|
| Layers | 24 | 32 | 32 |
| Hidden size | 2048 | 2560 | 4096 |
| FFN size | 4096 | 5120 | 8192 |
| Heads | 8 | 10 | 16 |
| Learning rate | 6 x 10^-4 | 3 x 10^-4 | 3 x 10^-4 |
| LR scheduler | Polynomial decay | Polynomial decay | Polynomial decay |
| Warm-up steps | 375 | 375 | 375 |
| Tokens per batch | 4M | 4M | 4M |
| Adam beta | (0.9, 0.98) | (0.9, 0.98) | (0.9, 0.98) |
| Training steps | 25,000 | 25,000 | 25,000 |
| Gradient clipping | 2.0 | 2.0 | 2.0 |
| Dropout | 0.1 | 0.1 | 0.1 |
| Weight decay | 0.01 | 0.01 | 0.01 |
