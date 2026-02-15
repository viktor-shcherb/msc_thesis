# 4 Shifted Rotary Position Embedding [p. 5–6]

[p. 5]

In Figure 1c, we demonstrate that even when all data are concatenated to fill the training context window, positions at the tail remain infrequent. In this section, we introduce ShifTed Rotary position embeddING (STRING). STRING shifts position indices from the diagonal of P towards its bottom-left corner, allowing the model to gather distant information with frequent position indices.

**Figure 4** (p. 6): "NIAH results for our pretrained model TinyLlama-1.3B (2K) and Llama3.1 (128K) where the X-axis means input context length and the Y-axis represents the document depth. In this figure, we clearly observe that for TinyLlama 2K and Llama3.1 128K, most poor-performing cases are concentrated in the lower-left triangle, indicating that the models are unable to gather distant needles."

Description: Two heatmaps showing NIAH results
- Key elements: Two heatmaps side by side, one for TinyLlama-1.3B-2K and one for Llama3.1 (128K). X-axis shows context length, Y-axis shows document depth from 0 to 100%. Color scale indicates performance (darker/red = worse, lighter/green = better).
- Notable patterns: Both models show a distinct pattern where poor performance (darker red/orange regions) concentrates in the lower-left triangle of the heatmap. This indicates failure to retrieve needles when they are far from the query position. For TinyLlama 2K, poor performance appears at smaller context lengths. For Llama3.1 128K, the poor-performing region extends to much longer context lengths but maintains the same triangular pattern.
- Supports claim: Models struggle to gather distant information, with failures concentrated when needles are positioned far from the end of the document where the query is located.

**Figure 5** (p. 6): "A illustrative example of STRING for a sequence length of L = 9. (a) Position indices 6, 7, and 8 are removed from the matrix. (b) Indices 0, 1, 2, 3, 4, and 5 are shifted from the main diagonal to the lower-left triangle with an offset of 3. (c) Recovering locality where m ≥ n − 3, thereby restoring emphasis on the neighboring W tokens. The position matrix of Llama3.1-128K using STRING is shown in Figure 8 Appendix."

Description: Three matrix diagrams showing STRING transformation
- Key elements: (a) shows initial position matrix with dropping infrequent positions. Positions 6, 7, 8 removed leaving empty slots. (b) shows shifting frequent positions. Indices shifted leftward with stride of 3 to fill empty slots. Numbers shown: [5, 4, 3, 2, 1, 0] becoming shifted positions. (c) shows final matrix after recovering locality with small constant W added to diagonals where m ≥ n − 3.
- Notable patterns: The transformation moves well-trained position indices from the diagonal (where they represent short distances) to the lower-left region (where they now represent long distances). A small window W maintains local context.
- Supports claim: STRING enables models to use frequently trained position indices to represent long-range dependencies that were previously assigned to undertrained position indices.

## 4.1 Manipulating the Position Matrix [p. 6]

STRING is implemented by manipulating the position matrix P. The three main procedure of STRING is shown in Figure 5:

**(1) Dropping Infrequent Positions:** We begin by assuming that position indices greater than a threshold N falls into the infrequent area. Consequently, STRING initially drops all position indices i ≥ N. As depicted in Figure 5a, we set N = 6 and L = 9, resulting in the removal of position indices 6, 7, and 8 from the matrix and leaving an empty area.

**(2) Shifting Frequent Positions:** Next, we shift the remaining position indices from the main diagonal (the high-frequency area) to fill the empty triangle in the bottom-left corner of P. The shift offset is defined as S = L − N. In our example, S = 9 − 6 = 3, as shown in Figure 5b. For instance, let's consider the last row of the matrix P. The position indices after dropping are [−, −, −, 5, 4, 3, 2, 1, 0]. To fill the 3 empty slots, we shift the positions leftwards with a stride of 3, and they become [5, 4, 3, 2, 1, 0, 2, 1, 0]. Formally, the updated position matrix is defined as:

```
P[m][n] = {
    P[m][n] − S    if m ≥ n − S,
    P[m][n]        otherwise.
}
```
(3)

Here, m, n is the row/column index, m = n − S indicates that the element is located on a diagonal of S away from the main diagonal, and m ≥ n − S signifies that the element is in the lower-left region relative to this diagonal. The resulting position matrix after this operation is shown in Figure 5b.

**(3) Restoring Locality with a Small Window:** Applying Eq. 3 disrupts the model's ability to capture local relationships because it alters the relative positions between neighboring tokens (Su, 2023; Jin et al., 2024; An et al., 2024a). Specifically, the relative positions on the S-th diagonal are set to zero. Since neighboring tokens are crucial for generating fluent content, we introduce a small local window value W ≪ S for elements where m ≥ n − S, as illustrated in Figure 5c. This adjustment maintains emphasis on the closest W neighboring tokens. The final position matrix is defined as:

```
P[m][n] = {
    P[m][n] − S + W    if m ≥ n − S,
    P[m][n]            otherwise.
}
```
(4)

In Eq. 4, S is the shift offset, and W is used to ensure the neighboring W tokens remain the closest in terms of positional encoding. Notably, W does not rely on L, whereas S heavily depends on L. We suggest setting the local window W ≥ 32 to ensure the necessary fluency of content, and the offset L/7 ≤ S ≤ L/2. We set S = L/3 and W = 128 for all models across downstream tasks. An ablation study is shown in Figure 7.

---
[p. 7 continued]

## FlashAttention Implementation [p. 7]

We implement STRING using FlashAttention (Dao et al., 2022), which is essential for verifying the method on modern large language models (LLMs) that typically have long context windows (e.g., 128K tokens). STRING can be efficiently implemented by modifying the position indices used in RoPE and combining two attention patterns. The pseudocode for STRING is provided in Algorithm 1. Our implementation splits the standard self-attention mechanism into two components:

1. **Sliding Window Attention (lines 11-13):** This approach calculates the attention outputs around the main diagonal by considering positions where m < n − S (line 13). When computing the sliding window attention, there is no need to modify the position indices for either queries (line 6) or keys (line 7).

2. **Shifted Self-Attention (lines 15-19):** This method computes the attention outputs in the bottom-left triangle, specifically for positions where m ≥ n − S, utilizing shifted self-attention (line 19). In this process, the position indices for queries are replaced with shifted position indices (line 16). STRING controls the relative distance by only modifying the position indices for queries and there is no influence on other key and value values.

Finally, we merge the attention outputs from the sliding window around the main diagonal and the left-bottom triangle to produce the final output. An example of applying STRING on Llama3.1 is shown in Section 8A.1 and the efficiency test of STRING is shown in Figure 9.

**Algorithm 1** Pseudocode of STRING with FlashAttention

```
1  # Q, K, V: tensors with shape [L, d]
2  # W:  the local window value (scalar)
3  # S:  the sliding window size (scalar)
4  # N:  the left-bottom triangle height (scalar)
5
6  pids_query = [0,1,2,...L-1]  # standard position ids for keys
7  pids_key = [0,1,2,...L-1]  # standard position ids for queries
8  # Apply rotary position embeddings to K
9  K = apply_rotary_pos_emb(K, pids_key)
10
11  # ---- Calculating self-attention around the diagonal ---->
12  Q_diag = apply_rotary_pos_emb(Q, pids_query)
13  O_diag, attn_map_diag = flash_attn(Q_diag, K, V, sliding_window=S)
14
15  # ---- Calculating self-attention at the left-bottom triangle ---->
16  pids_q_shifted = pids_query - S + W  # new position ids for queries
17  Q_shifted = apply_rotary_pos_emb(Q, pids_q_shifted)
18  # locate only in the bottom-left triangle & calculate flash-attn
19  O_shifted, attn_map_shifted = flash_attn(Q_shifted[-N:], K[:N], V[:N])
20
21  # Merge the attention outputs from the diagonal and left-bottom triangle
22  output = merge_diag_shifted(O_diag, O_shifted, attn_map_diag, attn_map_shifted)
```

**Figure 6** (p. 7): "Detailed pseudocode of STRING incorporating FlashAttention Dao et al. (2022). The implementation of merge_diag_shifted can be found in Algorithm 2 in the Appendix."

Description: Algorithm pseudocode box
- Key elements: Detailed code listing showing the FlashAttention implementation of STRING. Shows variable definitions, RoPE application, two attention computation paths (sliding window and shifted), and merging step.
- Notable patterns: The code demonstrates the two-component approach: standard attention for the diagonal band and shifted attention for the lower-left triangle, then merging results.
- Supports claim: STRING can be efficiently implemented by modifying position indices in RoPE and combining two attention patterns in FlashAttention.
