# 2.5 Long Context [p. 14–15]

## Long Context Extension Framework

[p. 14]

To facilitate the training of their models with extended context lengths, the authors reuse the Megatron-LM framework from pretraining. They enable inter-node context parallelism along with intra-node tensor parallelism to keep the memory consumption within device limits.

## Stages

[p. 14]

To gradually scale up the context length, the authors split training into multiple phases characterized by the context length. This incremental approach allows the model to adapt smoothly without the instability that can result from a sudden, drastic increase in context length. They also increase the RoPE Theta at each stage to smooth the adaptation to longer context lengths.

For consistency, the global batch size (GBS) from the pretraining stage was maintained throughout all long context training phases (8M tokens for the 8B model and 16M for the 70B model). The learning rate (LR) was set to the final value from the final pretraining cooldown period (1.1e-5 for the 8B model and 1.0e-6 for the 70B model), which represents 10% of the peak pretraining LR. To ensure training stability at the beginning of this new phase, they employed an LR warmup for the first 1.2 billion tokens at each stage.

The data mixture during long context extension is described in detail in Section 3.4, and the results of their long-context evaluations are presented in Section 5.2.

### Table 5

**Table 5** (p. 15): **Long-Context Extension Hyperparameters for Apertus-8B and Apertus-70B.** Parallelism is denoted as Tensor (TP), Pipeline (PP), Data (DP), and Context Parallelism (CP). Both models use a warmup of 1.2B tokens.

| Model | GBS (Tokens) | LR | Context Length (k) | RoPE Theta (M) | Parallelism (TP/PP/DP/CP) | Avg. Throughput (Tokens/GPU/s) |
|---|---|---|---|---|---|---|
| Apertus-8B | 8M | 1.1e-5 | 8 | 1 | 2/1/1024/1 | ~6150 |
| Apertus-8B | 8M | 1.1e-5 | 16 | 2 | 4/1/512/1 | ~4300 |
| Apertus-8B | 8M | 1.1e-5 | 32 | 4 | 4/1/256/2 | ~3700 |
| Apertus-8B | 8M | 1.1e-5 | 64 | 12 | 4/1/128/4 | ~1800 |
| Apertus-70B | 16M | 1e-6 | 8 | 1 | 4/8/64/1 | ~780 |
| Apertus-70B | 16M | 1e-6 | 16 | 2 | 4/8/32/2 | ~710 |
| Apertus-70B | 16M | 1e-6 | 32 | 4 | 4/8/16/4 | ~480 |
| Apertus-70B | 16M | 1e-6 | 64 | 12 | 4/8/8/8 | ~160 |
