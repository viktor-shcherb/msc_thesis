# 3.1 Setup [p. 5-6]

[p. 5] Position Interpolation can effectively extend context window up to 32 times of the original size, and such extension can be done with only several hundreds of training steps. The resulting models are strong LLMs with fully effective long context windows. Performance is demonstrated on a number of tasks including language modeling, passkey retrieval, and long document summarization. Benchmark results of the extended models on the original LLaMA evaluation benchmarks are also presented.

## Model Variants

[p. 6] The authors extended the pre-trained 7B, 13B, 33B and 65B LLaMA models (Touvron et al., 2023) to various context window of sizes up to 32768, using either direct fine-tuning or Position Interpolation method. Except for rescaling the position indices for models extended with Position Interpolation, they did not modify LLaMA model architectures (Touvron et al., 2023) in any ways.

## Training Procedure

[p. 6] All model variants are fine-tuned using the next token prediction objective. Training details:

- **Optimizer:** AdamW (Loshchilov & Hutter, 2019) with $\beta_1 = 0.9$ and $\beta_2 = 0.95$
- **Learning rate warmup:** 20 steps starting from 10% of the maximum learning rate
- **Learning rate:**
  - 7B and 13B models: $2 \times 10^{-5}$
  - 33B and 65B models: $10^{-5}$
- **Weight decay:** zero
- **Hardware:**
  - 7B, 13B, 33B models extended to 8192 context window: 32 A100 GPUs, 64 global batch size
  - All other cases: 128 A100 GPUs, 128 global batch size
- The main need for more GPUs is memory limitation during fine-tuning; it is possible to use fewer GPUs in certain cases
- **Framework:** PyTorch (Paszke et al., 2019) with Fully Sharded Data Parallel (Zhao et al., 2023) and Flash Attention (Dao et al., 2022)

**Fine-tuning steps:**
- Position Interpolation method: 1000 steps (unless otherwise specified)
- Direct fine-tuning method: 10000 steps

**Training data:** Primarily the Pile training dataset (Gao et al., 2020). In Section 3.4 they also compare fine-tuning performance on the RedPajama dataset (Computer, 2023). [p. 6]
