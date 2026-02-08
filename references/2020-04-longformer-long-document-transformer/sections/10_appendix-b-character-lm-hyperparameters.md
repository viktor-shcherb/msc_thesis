# B Character LM Hyperparameters [p. 13-15]

[p. 13] Evaluation on `text8` and `enwik8`, both containing 100M characters from Wikipedia split into 90M, 5M, 5M for train, dev, test. The model only specifies how the self-attention component works, and is agnostic to the other design choices for the transformer model.

## Model Architecture

[p. 13] The implementation is based on the Transformer-XL (Dai et al., 2019) code^11 with the memory mechanism disabled. Relative position embeddings with sinusoidal weights are used as in Dai et al. (2019). Two different model sizes:
- **Small model:** 12 layers, 512 hidden size, as in Dai et al. (2019)
- **Large model:** 30 layers, 512 hidden size, as in Child et al. (2019)

^11 https://github.com/kimiyoung/transformer-xl [p. 13, footnote 11]

## Training Details

[p. 13] Mixed precision training (floating points 16 and 32) using apex^12 to reduce memory consumption and speed-up training. However, the attention computation is kept in fp32 to avoid numerical instability issues.^13 Gradient checkpointing (Chen et al., 2016) is used to reduce memory usage. All experiments are run on 48GB RTX8000 GPUs.

^12 https://github.com/NVIDIA/apex [p. 13, footnote 12]

^13 Using fp16 in the attention operation results in floating point overflow and NaNs in later stages of training. [p. 13, footnote 13]

## Hardware and Runtime

[p. 14] Small model experiments run on 4 RTX8000 GPUs for 16 days. Large model experiments run on 8 RTX8000 GPUs for 13 days.

## Hyperparameter Search

[p. 14] Most of the hyperparameter search is similar to the ablation in Tab. 4 where the configuration is run for 150K steps on `text8`. Experimented with:
- Absolute position embeddings and learned position embeddings (relative and sinusoidal selected)
- Dropout values of [0.1, 0.2] (small model) and [0.1, 0.4] (large model)
- Pre-layernorm and post-layernorm (Xiong et al., 2020)
- Learning rate (LR) of phase1 of values [2.5e-5, 5e-4, 1e-4] constant and cosine LR schedules
- Different configurations for dilation (on all heads, on 2 heads, no dilation)

Number of gradient updates/phase reported in Tab. 12 is determined by running each phase until the validation BPC stops getting better.

## Table 12: Hyperparameters for the best performing model for character-level language modeling [p. 15]

| Param | Value |
|---|---|
| Position Embeddings | Relative and Sinusoidal as in Dai et al. (2019) |
| Small model config | 12 layers, 8 heads, 512 hidden size as in Dai et al. (2019) |
| Large model config | 30 layers, 8 heads, 512 hidden size as in Child et al. (2019) |
| Optimizer | AdamW |
| Dropout | 0.2 (small model), 0.4 (large model) |
| Gradient clipping | 0.25 |
| Weight Decay | 0.01 |
| Layernorm Location | pre-layernorm (Xiong et al., 2020) |
| Activation | GeLU |
| Number of phases | 5 |
| Phase 1 window sizes | 32 (bottom layer) - 8,192 (top layer) |
| Phase 5 window sizes | 512 (bottom layer) - (top layer) |
| Phase 1 sequence length | 2,048 |
| Phase 5 sequence length | 23,040 (gpu memory limit) |
| Phase 1 LR | 0.00025 |
| Phase 5 LR | 0.000015625 |
| Batch size per phase | 32, 32, 16, 16, 16 |
| #Steps per phase (small) | 430K, 50k, 50k, 35k, 5k |
| #Steps per phase (large) | 350K, 25k, 10k, 5k, 5k |
| Warmup | 10% of the phase steps with maximum 10K steps |
| LR scheduler | constant throughout each phase |
| Dilation (small model) | 0 (layers 0-5), 1 (layers 6-7), 2 (layers 8-9), 3 (layers 10-11) |
| Dilation (large model) | 0 (layers 0-14), 1 (layers 15-19), 2 (layers 20-24), 3 (layers 25-29) |
| Dilation heads | 2 heads only |
