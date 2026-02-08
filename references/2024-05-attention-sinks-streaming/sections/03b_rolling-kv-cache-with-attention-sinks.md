# 3.2 Rolling KV Cache with Attention Sinks [p. 5]

To enable LLM streaming in already trained LLMs, the authors propose a straightforward method that can recover window attention's perplexity without any model finetuning. Alongside the current sliding window tokens, they reintroduce a few starting tokens' KV in the attention computation. [p. 5]

**Figure 4** (p. 5): "The KV cache of StreamingLLM."
The figure shows three rows representing the generation of Token 7, Token 8, and Token 9. Each row shows the cache layout with colored cells: green cells (positions 0-3) represent the Attention Sinks (four initial tokens), gray cells with X marks represent Evicted Tokens, and yellow/colored cells represent the Rolling KV Cache (most recent tokens). As each new token is generated, the rolling window shifts: the oldest non-sink token is evicted and the new token enters the cache. The figure illustrates the two-part cache structure.

The KV cache in StreamingLLM can be conceptually divided into two parts, as illustrated in Figure 4:
1. **Attention sinks** (four initial tokens) stabilize the attention computation.
2. **Rolling KV Cache** retains the most recent tokens, crucial for language modeling.

StreamingLLM's design is versatile and can be seamlessly incorporated into any autoregressive language model that employs relative positional encoding, such as RoPE (Su et al., 2021) and ALiBi (Press et al., 2022). [p. 5]

## Positional Encoding Within the Cache [p. 5]

When determining the relative distance and adding positional information to tokens, StreamingLLM focuses on positions *within the cache* rather than those *in the original text*. This distinction is crucial for StreamingLLM's performance. For instance, if the current cache (Figure 4) has tokens [0, 1, 2, 3, 6, 7, 8] and is in the process of decoding the 9th token, the positions assigned are [0, 1, 2, 3, 4, 5, 6, 7], rather than the positions in the original text, which would be [0, 1, 2, 3, 6, 7, 8, 9]. [p. 5]

## Integration with RoPE and ALiBi [p. 5]

For encoding like RoPE, the Keys of tokens are cached *prior to* introducing the rotary transformation. Then, position transformation is applied to the keys in the rolling cache at each decoding phase. On the other hand, integrating with ALiBi is more direct. Here, the contiguous linear bias is applied instead of a 'jumping' bias to the attention scores. This method of assigning positional embedding within the cache is crucial to StreamingLLM's functionality, ensuring that the model operates efficiently even beyond its pre-training attention window size. [p. 5]
