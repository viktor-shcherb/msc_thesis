# 4 Setting [p. 6]

[p. 6] The authors evaluate the impact of Ring Attention on improving Transformer models by benchmarking maximum sequence length and model flops utilization.

## Model Configuration

The study is built upon the LLaMA architecture, considering 3B, 7B, 13B, and 30B model sizes.

## Baselines

Ring Attention is compared with:
- Vanilla transformers [37] — computes self-attention by materializing the attention matrix and computes the feedforward network normally
- Transformers with memory efficient attention [30] and its efficient CUDA implementation [9]
- Transformers with both memory efficient attention and feedforward [23]

## Training Configuration

- Full gradient checkpointing [5] applied to both attention and feedforward, following prior works [30, 23]
- Experiments on both GPUs and TPUs
- GPUs: single DGX A100 server with 8 GPUs and distributed 32 A100 GPUs
- TPUs: from older generations TPUv3 to newer TPUv4 and TPUv5e
- All results obtained using full precision instead of mixed precision
