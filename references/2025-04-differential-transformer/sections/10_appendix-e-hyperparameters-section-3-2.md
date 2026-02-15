# Appendix E: Hyperparameters for Section 3.2 [p. 18]

Table 10 reports the hidden dimension, number of layers, and number of heads of DIFF Transformer for different model sizes [p. 18]. For all model sizes of Transformer, they double the number of heads compared with DIFF Transformer to align parameters [p. 18]. The FFN size is 8/3 × d_model, where d_model is the hidden dimension [p. 18]. The training length is set to 2048 [p. 18]. The batch size is set to 0.25M tokens [p. 18]. They use AdamW (Loshchilov & Hutter, 2019) with β₁ = 0.9, β₂ = 0.98 [p. 18]. The learning rate is 1.5 × 10⁻³ for 830M to 2.8B sizes, and 7.5 × 10⁻⁴ for 6.8B to 13.1B sizes [p. 18]. The warmup steps are 375 with linear rate decay [p. 18]. The weight decay is set to 0.05 [p. 18]. They train the models with 40k steps, i.e., 10B tokens [p. 18].

| Size | Hidden Dim. | #Layers | #Heads |
|---|---|---|---|
| 830M | 1536 | 24 | 8 |
| 1.4B | 2048 | 24 | 8 |
| 2.8B | 2560 | 32 | 10 |
| 6.8B | 4096 | 32 | 16 |
| 13.1B | 5120 | 40 | 20 |

Table 10: Model size and hyperparameters used for DIFF Transformer in Section 3.2 [p. 18].
