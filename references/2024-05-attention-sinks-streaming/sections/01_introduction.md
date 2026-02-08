# 1 Introduction [p. 1-2]

LLMs (Radford et al., 2018; Brown et al., 2020; Zhang et al., 2022; OpenAI, 2023; Touvron et al., 2023a,b) are becoming ubiquitous, powering NLP applications such as dialog systems (Schulman et al., 2022; Taori et al., 2023; Chiang et al., 2023), document summarization (Goyal & Durrett, 2020; Zhang et al., 2023a), code completion (Chen et al., 2021; Roziere et al., 2023), and question answering (Kamalloo et al., 2023). [p. 1]

To unleash the full potential of pretrained LLMs, they should be able to efficiently and accurately perform long sequence generation. It is very challenging for LLMs to generalize to longer sequence lengths than they have been pretrained on, e.g., 4K for Llama-2 (Touvron et al., 2023b). [p. 1]

LLMs are constrained by the attention window during pre-training. Despite substantial efforts to expand the window size (Chen et al., 2023; kaiokendev, 2023; Peng et al., 2023) and improve training (Dao et al., 2022; Dao, 2023) and inference (Pope et al., 2022; Xiao et al., 2023; Anagnostidis et al., 2023; Wang et al., 2021; Zhang et al., 2023b) efficiency for lengthy inputs, the acceptable sequence length remains intrinsically *finite*, which does not allow persistent deployments. [p. 1]

The paper introduces the concept of LLM streaming applications and asks the question:

> "*Can we deploy an LLM for infinite-length inputs without sacrificing efficiency and performance?*" [p. 1]

**Figure 1** (p. 2): "Illustration of StreamingLLM vs. existing methods. The language model, pre-trained on texts of length $L$, predicts the $T$th token (where $T \gg L$)."
The figure shows four attention/caching strategies with their KV cache patterns, time complexity, and perplexity (measured using Llama-2-13B on the first book (65K tokens) in the PG-19 test set):
- (a) **Dense Attention**: $O(T^2)$ time, PPL: 5641. Has poor efficiency and performance on long text. Its performance decreases when text length exceeds the pre-training text length.
- (b) **Window Attention**: $O(TL)$ time, PPL: 5158. Efficient in inference but performance declines sharply once the starting tokens' keys and values are evicted. Breaks when initial tokens are evicted.
- (c) **Sliding Window w/ Re-computation**: $O(TL^2)$ time, PPL: 5.43. Rebuilds the KV states from the $L$ recent tokens for each new token. Performs well on long texts but its $O(TL^2)$ complexity from quadratic attention in context re-computation makes it considerably slow.
- (d) **StreamingLLM (ours)**: $O(TL)$ time, PPL: 5.40. Keeps the *attention sink* (several initial tokens) for stable attention computation, combined with the recent tokens. Efficient and offers stable performance on extended texts.

## Two Primary Challenges for Infinite Input Streams [p. 2]

1. During the decoding stage, Transformer-based LLMs cache the Key and Value states (KV) of all previous tokens, as illustrated in Figure 1(a), which can lead to excessive memory usage and increasing decoding latency (Pope et al., 2022).
2. Existing models have limited length extrapolation abilities, i.e., their performance degrades (Press et al., 2022; Chen et al., 2023) when the sequence length goes beyond the attention window size set during pre-training.

## Window Attention and Its Failure [p. 2]

Window attention (Beltagy et al., 2020) maintains only a fixed-size sliding window on the KV states of most recent tokens (Figure 1b). Although it ensures constant memory usage and decoding speed after the cache is initially filled, the model collapses once the sequence length exceeds the cache size, i.e., *even just evicting the KV of the first token*, as illustrated in Figure 3. [p. 2]

Another strategy is the sliding window with re-computation (Figure 1c), which rebuilds the KV states of recent tokens for each generated token. While it offers strong performance, this approach is significantly slower due to the computation of quadratic attention within its window, making it impractical for real-world streaming applications. [p. 2]

## Attention Sinks: The Key Phenomenon [p. 2]

The authors find an interesting phenomenon of autoregressive LLMs: a surprisingly large amount of attention score is allocated to the initial tokens, irrespective of their relevance to the language modeling task, as visualized in Figure 2. They term these tokens "attention sinks". Despite their lack of semantic significance, they collect significant attention scores. The authors attribute the reason to the Softmax operation, which requires attention scores to sum up to one for all contextual tokens. When the current query does not have a strong match in many previous tokens, the model still needs to allocate these unneeded attention values somewhere so it sums up to one. Initial tokens serve as sinks because they are visible to almost all subsequent tokens due to the autoregressive language modeling nature, making them more readily trained to serve as attention sinks. [p. 2]

## StreamingLLM Proposal [p. 2]

StreamingLLM is a simple and efficient framework that enables LLMs trained with a finite attention window to work on text of infinite length without fine-tuning. It exploits the fact that attention sinks have high attention values, and preserving them can maintain the attention score distribution close to normal. StreamingLLM simply keeps the attention sink tokens' KV (with just 4 initial tokens sufficing) together with the sliding window's KV to anchor the attention computation and stabilize the model's performance. [p. 2]

With StreamingLLM, models including Llama-2-[7, 13, 70]B, MPT-[7, 30]B, Falcon-[7, 40]B, and Pythia-[2.9, 6.9, 12]B can reliably model 4 million tokens, and potentially even more. Compared with the only viable baseline, sliding window with recomputation, StreamingLLM achieves up to 22.2x speedup. [p. 2]

**Figure 2** (p. 3): "Visualization of the *average* attention logits in Llama-2-7B over 256 sentences, each with a length of 16."
The figure shows heatmaps of attention logits across multiple layers and heads. Observations include:
1. The attention maps in the first two layers (layers 0 and 1) exhibit the "local" pattern, with recent tokens receiving more attention.
2. Beyond the bottom two layers, the model heavily attends to the initial token across all layers and heads.
Smaller inset panels show Layer 9 Head 0, Layer 10 Head 0, Layer 22 Head 0, and Layer 31 Head 0, all exhibiting strong attention to the first token position.

## Contributions [p. 3]

The authors further confirm the attention sink hypothesis and demonstrate that language models can be pre-trained to require only a single attention sink token for streaming deployment. Specifically, they suggest that an extra learnable token at the beginning of all training samples can serve as a designated attention sink. By pre-training 160-million parameter language models from scratch, they demonstrate that this single sink token preserves the model's performance in streaming cases. This is in contrast to vanilla models, which necessitate the reintroduction of multiple initial tokens as attention sinks to achieve the same performance level. [p. 3]

The authors emphasize that StreamingLLM efficiently generates coherent text from tokens within the KV cache without extending the LLMs' context length. It suits continuous operation needs with minimal memory use and past data reliance. Additionally, StreamingLLM can complement context extension methods to increase the attendable recent context. [p. 3]
