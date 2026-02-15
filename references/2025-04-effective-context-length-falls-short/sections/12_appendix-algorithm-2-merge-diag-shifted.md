# Algorithm 2: Pseudocode of merge_diag_shifted [p. 19]

[p. 19]

**Algorithm 2** Pseudocode of merge_diag_shifted

```
1  def merge_diag_shifted(O_diag, O_shifted, attn_map_diag, attn_map_shifted):
2      """
3      Merge the attention outputs from the diagonal and left-bottom triangle.
4
5      Parameters:
6      O_diag (Tensor: [L, d] ): Output tensor from diagonal attention.
7      O_shifted (Tensor: [N, d]): Output tensor from left-bottom triangle attention.
8      attn_map_diag (Tensor: [L, L]): Attention map from diagonal attention.
9      attn_map_shifted (Tensor: [N, N]): Attention map from left-bottom triangle attention.
10
11     Returns:
12         output (Tensor: [L, d] ): Merged output tensor.
13     """
14
15     # the softmax normalizer of the sliding window attention
16     S=L-N # S is the sliding window size, and N is the triangle height
17     diag_norm = attn_map_diag.sum(-1) # shape: [L,]
18     # the softmax normalizer of the self-attention
19     shifted_norm = attn_map_shifted.sum(-1) # shape: [N,]
20     O_diag_head = O_diag[:S] # shape: [S, d], no need for changing the first S tokens
21     O_diag_tail = O_diag[S:] # [N, d]
22     diag_norm_tail = diag_lise[S:] # [N,]
23     diag_rate = diag_norm_tail / (diag_norm_tail + shifted_norm) # [N,]
24     shifted_rate = shifted_norm / (diag_norm_tail + shifted_norm) # [N,]
25     O_merged_tail = diag_rate * O_diag_tail + shifted_rate * O_shifted  # [N,d]
26     output = torch.cat([O_diag_head, O_merged_tail]) # [L, d]
27     return output
```

Note: Line 22 in the PDF appears to read `diag_lise[S:]` which is likely a typo for `diag_norm[S:]` based on the variable naming convention used elsewhere in the algorithm.

Description: This algorithm merges attention outputs from two components:
1. The diagonal attention component (sliding window attention)
2. The left-bottom triangle attention component (shifted positions)

The merge is performed by computing normalized weights for each component based on their attention map sums, then combining them proportionally. The first S tokens use only diagonal attention output, while the remaining N tokens use a weighted combination of both attention outputs.
