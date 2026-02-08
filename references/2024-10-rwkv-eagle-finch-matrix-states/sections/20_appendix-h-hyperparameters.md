# Appendix H: Hyperparameters [p. 38]

[p. 38] All Eagle and Finch models were trained under bfloat16 format for most parameters, except that float32 was used to compute WKV for numerical stability. The Adam optimizer was configured with β₁ = 0.9, β₂ = 0.99 and 0.001 weight decay applied only to linear layers and embedding weights. The context length for pretraining was 4096 tokens. Learning rate for all models followed a linear 10 step warmup schedule from 20% to 100% of the maximum learning rate, followed by cosine decay to the minimum learning rate.

[p. 38] The time_decay w parameters are placed into a special 2x learning rate multiplier grouping.

### Table 17: Learning Rate Hyperparameters [p. 40]

| Parameters | 0.4B | 1.5B/1.6B | 3B | 7B |
|------------|------|-----------|----|----|
| Max LR | 4 × 10⁻⁴ | 3 × 10⁻⁴ | 2 × 10⁻⁴ | 1.5 × 10⁻⁴ |
| Min LR | 2 × 10⁻⁵ | 2 × 10⁻⁵ | 1.5 × 10⁻⁵ | 1 × 10⁻⁵ |
| Micro Batch Size | 8 | 8 | 4 | 9 |
| GPU Count | 24 | 48 | 48 | 64 |
| GPU Type | A100 | A100 | A100 | H800 |
| Batch Size | 786432 | 1572864 | 786432 | 2359296 |

Caption: Learning Rate Hyperparameters for pretrained Eagle and Finch models
