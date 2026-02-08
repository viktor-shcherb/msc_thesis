# 2 Related Work [p. 3-4]

Extensive research has been done on applying LLMs to lengthy texts, with three main areas of focus: **Length Extrapolation**, **Context Window Extension**, and **Improving LLMs' Utilization of Long Text**. While seemingly related, progress in one direction does not necessarily lead to progress in the other. Extending the context size of LLMs does not improve the model's performance beyond the context size, and neither approach ensures effective use of the long context. The StreamingLLM framework primarily lies in the first category, where LLMs are applied to text significantly exceeding the pre-training window size, potentially even of infinite length. The authors do not expand the attention window size of LLMs or enhance the model's memory and usage on long texts. The last two categories are orthogonal to their focus and could be integrated with their techniques. [p. 3]

## Length Extrapolation [p. 3]

Length extrapolation aims to enable language models trained on shorter texts to handle longer ones during testing. A predominant avenue of research targets the development of relative position encoding methods for Transformer models.

- **RoPE** (Rotary Position Embeddings; Su et al., 2021): transforms the queries and keys in every attention layer for relative position integration. Despite its promise, subsequent research (Press et al., 2022; Chen et al., 2023) indicated its underperformance on text that exceeds the training window.
- **ALiBi** (Press et al., 2022): biases the query-key attention scores based on their distance, introducing relative positional information. While this exhibited improved extrapolation, the authors' tests on MPT models highlighted a breakdown when the text length was vastly greater than the training length.

Current methodologies have yet to achieve infinite length extrapolation, causing no existing LLMs to fit for streaming applications. [p. 3]

## Context Window Extension [p. 3-4]

Context Window Extension centers on expanding the LLMs' context window, enabling the processing of more tokens in one forward pass. A primary line of work addresses the training efficiency problem. Given the quadratic complexity of attention computation during training, developing a long-context LLM is both a computational and memory challenge. [p. 3]

Solutions have ranged from:
- System-focused optimizations like FlashAttention (Dao et al., 2022; Dao, 2023), which accelerates attention computation and reduces memory footprint.
- Approximate attention methods (Zaheer et al., 2020b; Beltagy et al., 2020; Wang et al., 2020; Kitaev et al., 2020) that trade model quality for efficiency.
- Extending pre-trained LLMs with RoPE (Chen et al., 2023; kaiokendev, 2023; bloc97, 2023; Peng et al., 2023), involving position interpolation and fine-tuning.

However, all the aforementioned techniques only extend LLMs' context window to a limited extent, which falls short of the paper's primary concern of handling limitless inputs. [p. 3-4]

## Improving LLMs' Utilization of Long Text [p. 4]

This area optimizes LLMs to better capture and employ the content within the context rather than merely taking them as inputs. As highlighted by Liu et al. and Li et al., success in the previously mentioned two directions does not necessarily translate to competent utilization of lengthy contexts within LLMs. Addressing this effective usage of prolonged contexts within LLMs is still a challenge. The authors' work concentrates on stably harnessing the most recent tokens, enabling the seamless streaming application of LLMs. [p. 4]
