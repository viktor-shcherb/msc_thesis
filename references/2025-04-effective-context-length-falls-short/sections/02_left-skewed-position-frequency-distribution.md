# 2 Left-Skewed Position Frequency Distribution [p. 2–3]

## 2.1 Position Embeddings in LLMs [p. 2–3]

Self-attention mechanisms (Vaswani et al., 2017; Radford et al., 2018; Dai et al., 2019) inherently lack positional information (Liu et al., 2021; Su et al., 2022; Sun et al., 2022). To introduce positional information, a common approach is to design a function p. For an input at position i, we inject positional information using the following method: h_i = p(h, i) where h is the hidden representation of the input token. Another approach involves relative positional encodings (Bao et al., 2020), such as T5-bias (Raffel et al., 2023) and ALiBi (Press et al., 2022), which injects relative positional information by incorporating the relative distance (i − j) when computing the attention score between the j-th token and the i-th token.

To achieve better training stability and lower perplexity, mainstream large models like Qwen (Hui et al., 2024) and Llama (Llama Team, 2024) employ Rotary Position Embedding (RoPE) (Su et al., 2022) as their positional encoding method. RoPE directly injects positional information into the query and key vectors, enabling the inner product to encode the relative position information between the query and key. We adopt the notation from the original paper. Considering the i-th query and the j-th key, we have: q_i = p(q, i) and k_j = p(k, j). When computing attention, the inner product q_i^⊤k_j contains only the relative positional information (i − j), which means for any pair (m, n) such that m − n = i − j, it holds that q_m^⊤k_n = q_i^⊤k_j.

## 2.2 Relative Position Matrix and Position Frequency [p. 3]

Using relative positional encodings implies that, given training length L, the resulting relative position matrix P after computing Q^⊤K is defined by:

```
P = [
    0
    1       0
    ⋱       ⋱       ⋱
    L − 2   ⋯       1     0
    L − 1   L − 2   ⋯     1   0
]
```
(1)

where the Toeplitz matrix P captures the relative positional relationships between tokens, with each element P[m][n] = m − n encoding the relative distance between the m-th and n-th tokens in a sequence. Based on Eq. 1, we define the frequency of relative position i by f(i) = L − i, which is the number of occurrences of a relative position i. Throughout the remainder of this paper, the term "position" refers to **relative position**. The structure of matrix P is linearly skewed toward smaller positions, which inherently favors performance on shorter sequences. For example, when using a training context window of L = 2048 tokens, the relative position 2047 occurs only once in P.

The frequency of relative positions in P also depends on the data length distribution of the pretraining corpus C. We can obtain the frequency of relative position i by the following equation:

f(i) = ∑_{s∈C} max(|s| − i, 0),    0 ≤ i < L     (2)

We observe that the position frequency distribution is usually highly *left-skewed*, indicating that the model is frequently exposed to small positions, while larger positions account for only a small proportion. To illustrate this phenomenon, we examine the position distribution when using SlimPajama-627B (Cerebras, 2023) as the training corpus. The blue bars in Figure 1 illustrate the position

**Figure 1** (p. 3): "Position frequency distribution exhibits a pronounced left-skewed pattern across training data of varying lengths. Figure 1a illustrates the natural data length distribution of SlimPajama-627B where oversized data is truncated into multiple 2K sequences. Figure 1b presents the case with a uniform length distribution and Document frequencies decline quadratically. Figure 1c demonstrates that when all data are concatenated into a 2K sequence, the position frequency decreases linearly with increasing position indices. The X-axis presents each length (shown in orange) and position indices (shown in blue). The left Y-axis indicates the frequency of each position, while the right Y-axis represents the number of data for each length."

Description: Three bar charts showing position frequency distributions
- Key elements: (a) Natural data distribution shows steep left-skewed pattern with blue bars (position frequency) and orange bars (data length distribution). (b) Uniform data distribution also shows left-skewed pattern. (c) Concatenated data distribution shows nearly linear decrease.
- Notable patterns: In all three scenarios, position frequency decreases as position index increases. The natural distribution (a) shows the most pronounced skew. Even uniform distribution (b) produces skewed position frequencies. Concatenated data (c) shows position frequencies decreasing linearly with increasing position indices up to 2K.
- Supports claim: This demonstrates that the left-skewed position frequency distribution is inherent to LLM training, regardless of the data length distribution strategy used.

## Position Frequency Statistics [p. 4]

[p. 4]

When the training length is 2048, the position indices i ≤ 1024 account for more than 80% of all indices, whereas those with i ≥ 1536 constitute less than **5%**. In addition to the biased relative position matrix P, the real-world data length distribution is also biased. Given a training context length of 2048 tokens, the data length distribution is shown in Figure 1a (orange bars): about 20% of the data consists of sequences around 256-512 tokens, and approximately 20% of the samples are around 2048 tokens. This latter percentage arises because long sequences are segmented into multiple sequences of length 2048, following popular open-source pretraining projects (Geng & Liu, 2023; Zhang et al., 2024b). Due to the combined effect of the data distribution and the relative position matrix, the frequency of positions decreases following a polynomial trend as the position indices increase.

Despite capturing local dependencies is often effective for LLMs, the imbalance in position frequency distribution when modeling both local and long-range dependencies is more pronounced than expected. This may result in a substantial underrepresentation of long-range dependencies.
