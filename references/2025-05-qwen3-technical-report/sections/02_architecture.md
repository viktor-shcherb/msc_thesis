# Architecture [p. 3]

## Model Series Overview

The Qwen3 series includes 6 dense models, namely Qwen3-0.6B, Qwen3-1.7B, Qwen3-4B, Qwen3-8B, Qwen3-14B, and Qwen3-32B, and 2 MoE models, Qwen3-30B-A3B and Qwen3-235B-A22B. The flagship model, Qwen3-235B-A22B, has a total of 235B parameters with 22B activated ones [p. 3].

Below, the authors elaborate on the architecture of the Qwen3 models.

## Dense Model Architecture

The architecture of the Qwen3 dense models is similar to Qwen2.5 (Yang et al., 2024b), including using Grouped Query Attention (GQA, Ainslie et al., 2023) (Dauphin et al., 2017), Rotary Positional Embeddings (RoPE, Su et al., 2024), and RMSNorm (Jiang et al., 2023) with pre-normalization. Besides, they remove QK-bias used in Qwen2.5 (Yang et al., 2024b) and introduce QK-norm (Wortsman et al., 2023; Dehghani et al., 2023) to the attention mechanism to ensure stable training for Qwen3 [p. 3].

Key information on model architecture is provided in Table 1.

**Table 1: Model architecture of Qwen3 dense models** [p. 3]

| Models | Layers | Heads (Q / KV) | Tie Embedding | Context Length |
|---------|--------|----------------|---------------|----------------|
| Qwen3-0.6B | 28 | 16 / 8 | Yes | 32K |
| Qwen3-1.7B | 28 | 16 / 8 | Yes | 32K |
| Qwen3-4B | 36 | 32 / 8 | Yes | 128K |
| Qwen3-8B | 36 | 32 / 8 | No | 128K |
| Qwen3-14B | 40 | 40 / 8 | No | 128K |
| Qwen3-32B | 64 | 64 / 8 | No | 128K |

## MoE Model Architecture

The Qwen3 MoE models share the same fundamental architecture as the Qwen3 dense models. Key information on model architecture is provided in Table 2. They follow Qwen2.5-MoE (Yang et al., 2024b) and implement fine-grained expert-choice routing (Dai et al., 2024) [p. 3].

The Qwen3 MoE models have 128 total experts with 8 activated experts per token. Unlike Qwen2.5-MoE, the Qwen3-MoE design excludes shared experts. Furthermore, they adopt the global-batch token balancing (Qiu et al., 2025) to encourage expert specialization [p. 3].

These architectural and training innovations have yielded substantial improvements in model performance across downstream tasks.

**Table 2: Model architecture of Qwen3 MoE models** [p. 3]

| Models | Layers | Heads (Q / KV) | # Experts (Total / Activated) | Context Length |
|---------|--------|----------------|-------------------------------|----------------|
| Qwen3-30B-A3B | 48 | 32 / 4 | 128 / 8 | 128K |
| Qwen3-235B-A22B | 94 | 64 / 4 | 128 / 8 | 128K |

## Tokenizer

Qwen3 models utilize Qwen's tokenizer (Bai et al., 2023), which implements byte-level byte-pair encoding (BBPE, Brown et al., 2020; Wang et al., 2020; Sennrich et al., 2016) with a vocabulary size of 151,669 [p. 3].
