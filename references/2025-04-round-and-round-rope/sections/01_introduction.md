# Introduction [p. 1–2]

## Positional Encodings in Transformers

Positional information is commonly provided to the attention mechanism in Transformers through absolute positional encodings (Vaswani et al., 2017), relative positional encodings (Su et al., 2024), or by introducing a bias directly into the activation (Press et al., 2021). One of the currently most widely adopted encodings, especially in Large Language Models (LLMs), are Rotary Positional Encodings (RoPE) (Su et al., 2024), being used in popular models such as Llama 3 (Dubey et al., 2024) and Gemma (Gemma Team et al., 2024) [p. 1].

RoPE acts on the queries and keys by splitting them in 2-dimensional chunks and rotating each chunk at a different frequency. The method can be implemented efficiently and provides an expressive approach to positional encodings [p. 1].

## Understanding RoPE: Challenging Common Assumptions

Despite the significant adoption of RoPE, the specific reasons why this method is useful to Transformer models remains poorly understood. One of the main arguments in favor of RoPE, made by Su et al. (2024), is that the method helps to decay attention coefficients as the relative distance grows. Most such claims, however, rely on the queries and keys being *constant* vectors – which is uncommon in practice. In fact, in this work we find situations in which this decay does *not* occur and that this is exploited at times by attention heads in Gemma 7B (Gemma Team et al., 2024) [p. 1].

Further, there are open intriguing questions as to why exactly the different frequencies in RoPE are useful. In the standard parameterisation of RoPE, the fastest frequencies rotate at 1 radian per token, whilst the slowest are several orders of magnitude slower at ≈ 1/10,000 radians per token. As dot product attention directly depends on the angle between the queries and keys, the highest frequencies are extremely sensitive to small token rearrangements, making them poor carriers of [p. 1] information. Consequently, we find it interesting and important to understand how exactly the different rotation frequencies are useful to LLMs [p. 2].

## Contributions

In this work we study in-depth empirically and theoretically how Transformers and in particular auto-regressive LLMs benefit from RoPE. We rely on the pretrained and open-source Gemma 7B (Gemma Team et al., 2024) model for our empirical analysis and show consistent results with Llama3.1 8B (Dubey et al., 2024) in the Appendix. We summarise our findings [p. 2]:

**Section 3 findings:**
- We argue against the common claim that RoPE is useful because it encourages the decay of attention coefficients with distance. We provide theoretical and empirical evidence to support our claim [p. 2].

**Section 4 findings:**
- We propose a new way to understand the usage of different frequencies in the queries and keys. We find that Gemma 7B largely prefers to use the low frequencies of RoPE. The first and last layers instead make most use of the high frequencies [p. 2].

**Section 5 findings:**
- We show that the highest frequencies in RoPE are cleverly used by Gemma 7B to construct special 'positional' attention heads (see Figure 1). We mathematically prove the 'robustness' of the construction [p. 2].

**Section 6 findings:**
- We study how the low frequencies are used. We observe distinct 'bands' in the low frequencies of the queries and keys. We conjecture that Gemma 7B is using them as 'information channels'. We prove that these channels cannot be robust over long context [p. 2].

**Section 6.1 findings:**
- We propose a new technique called p-RoPE that removes the lowest frequencies of RoPE to create robust semantic channels. We show not only that removing a percentage of the frequencies maintains the performance, but also *improves* it on 2 billion parameter models. We believe that eliminating these channels, and increasing the maximum RoPE wavelength helps with long-context, e.g. as shown in Llama 3 (Dubey et al., 2024) [p. 2].

**Figure 1** (p. 2): "Depiction of our construction which allows Transformers to obtain positional attention heads using RoPE – zooming in on a single RoPE frequency for clarity. On the **left** we depict key and query vectors for each position i, where keys are identical, and queries are just a rotated version of the keys, in a way that matches one of RoPE's highest frequencies. The **center** depicts how keys get rotated by RoPE, making the key at i − 1 perfectly align with the query. Due to the high frequency of the rotation, all other keys will lead to a smaller activation weights. On the **right** we show the resulting attention weights, resulting in this case in an off-diagonal positional attention. See Section 5 for more details."

Description: Diagram with three panels showing RoPE construction mechanism
- Key elements: Left panel shows key/query vectors at different positions (qi = ρ(g)ψi, qi-1 = ρ(g)ψi, etc.), center panel shows circular rotation visualization with ρ(g)ki-1 and ρ(g)ki marked, right panel shows resulting attention weight matrix α with diagonal pattern
- Notable patterns: The construction demonstrates how high-frequency rotations create off-diagonal positional attention patterns
- Supports claim: Illustrates the mechanism by which Gemma 7B uses highest frequencies to construct positional attention heads
