# 2 Architectural details [p. 2-3]

[p. 2] Mistral 7B is based on a transformer architecture [27].

## Model Architecture Parameters

**Table 1: Model architecture.** [p. 2]

| Parameter    | Value |
|-------------|-------|
| dim         | 4096  |
| n_layers    | 32    |
| head_dim    | 128   |
| hidden_dim  | 14336 |
| n_heads     | 32    |
| n_kv_heads  | 8     |
| window_size | 4096  |
| context_len | 8192  |
| vocab_size  | 32000 |

## Sliding Window Attention

SWA exploits the stacked layers of a transformer to attend to information beyond the window size W. The hidden state in position i of the layer k, h_i, attends to all hidden states from the previous layer with positions between i - W and i. Recursively, h_i can access tokens from the input layer at a distance of up to W x k tokens, as illustrated in Figure 1. [p. 2]

At the last layer, using a window size of W = 4096, there is a theoretical attention span of approximately 131K tokens. In practice, for a sequence length of 16K and W = 4096, changes made to FlashAttention [11] and xFormers [18] yield a 2x speed improvement over a vanilla attention baseline. [p. 2]

**Figure 1** (p. 2): "Sliding Window Attention. The number of operations in vanilla attention is quadratic in the sequence length, and the memory increases linearly with the number of tokens. At inference time, this incurs higher latency and smaller throughput due to reduced cache availability. To alleviate this issue, we use sliding window attention: each token can attend to at most W tokens from the previous layer (here, W = 3). Note that tokens outside the sliding window still influence next word prediction. At each attention layer, information can move forward by W tokens. Hence, after k attention layers, information can move forward by up to k x W tokens."

The figure shows three panels: (1) Vanilla Attention -- a lower-triangular matrix of 1s (full causal attention over tokens "The cat sat on the"); (2) Sliding Window Attention -- a banded lower-triangular matrix where each token attends to at most W = 3 previous tokens; (3) Effective Context Length -- a diagram showing layers stacked vertically and tokens horizontally, with colored bars indicating how information propagates across layers, showing that effective context grows with depth.

## Rolling Buffer Cache

[p. 2-3] A fixed attention span means the cache size can be limited using a rolling buffer cache. The cache has a fixed size of W, and the keys and values for the timestep i are stored in position i mod W of the cache. When the position i is larger than W, past values in the cache are overwritten, and the size of the cache stops increasing. On a sequence length of 32k tokens, this reduces the cache memory usage by 8x, without impacting the model quality. [p. 2]

**Figure 2** (p. 3): "Rolling buffer cache. The cache has a fixed size of W = 4. Keys and values for position i are stored in position i mod W of the cache. When the position i is larger than W, past values in the cache are overwritten. The hidden state corresponding to the latest generated tokens are colored in orange."

The figure shows three timesteps (i, i+1, i+2) with three example sequences. At each timestep, the cache of size W = 4 is filled and overwritten in a circular fashion, with the most recent token's hidden state highlighted in orange.

## Pre-fill and Chunking

[p. 3] When generating a sequence, tokens are predicted one-by-one, as each token is conditioned on the previous ones. However, the prompt is known in advance, and the (k, v) cache can be pre-filled with the prompt. If the prompt is very large, it can be chunked into smaller pieces, and the cache can be pre-filled with each chunk. The window size can be selected as the chunk size. For each chunk, the attention is computed over both the cache and the chunk. [p. 3]

**Figure 3** (p. 3): "Pre-fill and chunking. During pre-fill of the cache, long sequences are chunked to limit memory usage. We process a sequence in three chunks, 'The cat sat on', 'the mat and saw', 'the dog go to'. The figure shows what happens for the third chunk ('the dog go to'): it attends itself using a causal mask (rightmost block), attends the cache using a sliding window (center block), and does not attend to past tokens as they are outside of the sliding window (left block)."

The figure shows an attention matrix for the third chunk with tokens "the", "dog", "go", "to" as queries. Columns represent "The cat sat on" (Past), "the mat and saw" (Cache), and "the dog go to" (Current). The Past block is all zeros. The Cache block shows sliding window attention (partial 1s). The Current block shows causal attention (lower-triangular 1s).
