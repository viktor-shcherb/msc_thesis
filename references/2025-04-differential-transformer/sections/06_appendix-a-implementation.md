# Appendix A: Implementation of Differential Attention [p. 15]

The authors present the pseudocode for DiffAttn(·) and conventional softmax attention [p. 15].

## Pseudocode Comparison

**Conventional Attention:**
```python
def Attention(X, W_q, W_k, W_v):
    Q = X @ W_q
    K = X @ W_k
    V = X @ W_v
    # Q, K, V: [b, n, d]
    s = 1 / sqrt(d)
    A = Q @ K.transpose(-1, -2) * s

    return softmax(A) @ V
```

**Differential Attention:**
```python
def DiffAttn(X, W_q, W_k, W_v, λ):
    Q1, Q2 = split(X @ W_q)
    K1, K2 = split(X @ W_k)
    V = X @ W_v
    # Q1, K1: [b, n, d]; V: [b, n, 2d]
    s = 1 / sqrt(d)
    A1 = Q1 @ K1.transpose(-1, -2) * s
    A2 = Q2 @ K2.transpose(-1, -2) * s
    return
        (softmax(A1) - λ softmax(A2)) @ V
```

[p. 15]

## Implementation with FlashAttention

Additionally, the authors provide implementations with FlashAttention (Dao et al., 2022) [p. 15]. They categorize the implementations into two types by whether it supports using different dimensions between Q, K and V [p. 15]. FlashDiffAttn_1(·) denotes the package that supports different dimensions (e.g., xformers¹), and FlashDiffAttn_2(·) the package that does not (e.g., flash-attention²) [p. 15]. They also provide the unified-flash-attention³ package, which is modified based on the official FlashAttention2 (Dao, 2023), in order to support different dimensions between Q, K and V [p. 15].

The code implementation is available at https://aka.ms/Diff-Transformer [p. 15].

**FlashDiffAttn_1 Implementation:**
```python
def FlashDiffAttn_1(X, W_q, W_k, W_v, λ):
    Q1, Q2 = split(X @ W_q)
    K1, K2 = split(X @ W_k)
    V = X @ W_v

    A1 = flash_attn(Q1, K1, V)

    A2 = flash_attn(Q2, K2, V)

    return A1 - λ A2
```

**FlashDiffAttn_2 Implementation:**
```python
def FlashDiffAttn_2(X, W_q, W_k, W_v, λ):
    Q1, Q2 = split(X @ W_q)
    K1, K2 = split(X @ W_k)
    V1, V2 = split(X @ W_v)

    A11 = flash_attn(Q1, K1, V1)
    A12 = flash_attn(Q1, K1, V2)
    A1 = Concat(A11, A12)
    A21 = flash_attn(Q2, K2, V1)
    A22 = flash_attn(Q2, K2, V2)
    A2 = Concat(A21, A22)
    return A1 - λ A2
```

[p. 15]

¹https://github.com/facebookresearch/xformers
²https://github.com/Dao-AILab/flash-attention
³https://aka.ms/flash-diff

## Efficiency

Table 7 compares the throughput between DIFF Transformer and Transformer [p. 15]. For fair comparison, they use the customized-flash-attention implementation mentioned above for both methods [p. 15]. The experiments are conducted with NVIDIA H100-80GB GPU cards [p. 15].

| Model | Model Size | Length | **Throughput** | |
|---|---|---|---|---|
| | | | **Forward + Backward** | **Forward** |
| Transformer | 3B | 2K | 7247 | 51228 |
| DIFF | 3B | 2K | 6635 (−9%) | 46811 (−9%) |
| Transformer | 3B | 4K | 7491 | 48762 |
| DIFF | 3B | 4K | 6718 (−12%) | 44521 (−10%) |
| Transformer | 13B | 2K | 998 | 14346 |
| DIFF | 13B | 2K | 942 (−6%) | 13653 (−5%) |

Table 7: Throughput is measured with number of tokens per second [p. 15].

As shown in Table 7, they evaluate the settings with different model size (3B, 13B) and context length (2K, 4K) [p. 15]. For 3B models, there are 12 heads for DIFF Transformer and 24 heads for Transformer [p. 15]. For 13B model there are 20 heads for DIFF Transformer and 40 heads for Transformer [p. 15]. All models have the same head dimension d = 128 [p. 15]. Training efficiency consists of forward and backward [p. 15]. Prefill efficiency only includes forward [p. 15]. Table 7 shows throughput results are comparable within an acceptable range [p. 15]. Notice that the customized-flash-attention implementation is built on FlashAttention2 (Dao, 2023) [p. 15]. With the recent release of FlashAttention3 (Shah et al., 2024), the gap of throughput can be further reduced [p. 15]. More advanced kernel implementation, which is specifically designed for differential attention, can also improve throughput [p. 15].
