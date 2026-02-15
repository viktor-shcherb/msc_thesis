# 4 How are different frequencies used? [p. 5–6]

## Frequency Range in RoPE

In this section, we explore how different frequencies of RoPE are used. RoPE relies on a set of frequencies G that take values 1, ..., θ^(-(d-2)/d), with the highest frequency varying by 1 radian per token, while the lowest being much more stable at ≈ 1/θ per token. As the angle between vectors affects the dot product, the contribution from the highest frequencies should behave similarly to random noise, i.e. a small perturbation to the token sequence order will result in a largely different activation contribution. A natural question is whether these frequencies are being used and, if so, how exactly are they helpful? [p. 5]

## Measuring Frequency Usage via Cauchy-Schwarz

To measure the usage of frequencies, we start by noting that by Cauchy-Schwarz, the effect of the k-th frequency component on the activation ai,j is upper bounded by the 2-norm of the query and key components, i.e. |qi^(k)^⊤ kj^(k)| ≤ ||qi^(k)|| ||kj^(k)||. It is therefore natural to look at the mean 2-norm for each k^th in Gemma 7B over long sequences. For Gemma 7B, we note that k = 1, ..., 128, i.e. the hidden dimension is 128 × 2 = 256 [p. 5].

## Results: Layer-Level Frequency Distribution

Figure 3 shows the results. We plot the average 2-norm at each layer of each rope 'chunk' over a number of sequences, ordering them by frequency, with the intuition that the norm will be an upper bound for how much that frequency will impact the activation dot product. We emphasize that the mean is taken over all of the 16 heads at each layer. It is clear that learning has assigned much higher norm on average to the lowest frequencies, meaning that they will likely influence the dot product the most. This seems to be true at each layer. Interestingly, there seems to be some high frequency usage present especially at the very first and last layers [p. 5].

**Figure 3** (p. 6): "2-norm plotted over 2-dimensional chunks of queries (a) and keys (b) for each layer in Gemma 7B, corresponding to different RoPE frequencies. A mean is taken over 10 different Shakespeare quotes and the 16 attention heads at each layer."

Description: Two heatmaps showing frequency usage across layers
- (a) Mean query norm distribution at each layer: Heatmap with y-axis "High Frequencies" to "Low Frequencies", x-axis showing layers 1-27, color scale 0-6 "Mean norm"
- (b) Mean key norm distribution at each layer: Similar structure to (a), color scale 0-4 "Mean norm"
- Key elements: Both show distinct banding pattern with higher values (darker colors) concentrated in low frequency regions
- Notable patterns: Low frequencies have consistently higher norms across most layers; some high frequency activity visible in first and last layers
- Supports claim: Demonstrates that Gemma 7B predominantly uses low frequencies of RoPE, with selective high frequency usage in specific layers

## Head-Level Analysis

We believe this to be remarkable evidence showcasing how Gemma adapts to RoPE by preferring to use the lowest frequencies when computing attention activations.⁶ In the Appendix (Section E.2, Figure 14), for completeness, we show that this type of distribution does not occur for the value vectors. This highlights that this behaviour is a consequence of RoPE, where learning discovers that these medium to high frequency 'chunks' are not useful and hence pushes their norm to 0 so that [p. 5] their impact on the dot product is minimal. Corresponding entries in value vectors, not being rotated, do not suffer from the same pressure to reduce their norm to 0 [p. 6].

In Figure 4, we show the frequency usage of the 16 attention heads in the first layer. The heads that stand out as using the high frequencies, especially for the keys, are Heads 5 and 8. We will show in the next section that these heads have special roles as *positional attention heads*. We also highlight the sparse nature of the frequency usage, with the presence of 'high norm' bands, especially at the lower frequencies. We highlight that this kind of pattern seems consistent with the observation that feedforward layers act as sparse dictionary lookup tables (Geva et al., 2021). In this context, we believe that these bands are used to perform some kind of sparse dictionary lookup over key semantic matching [p. 6].

**Figure 4** (p. 6): "2-norm plotted over 2-dimensional chunks of queries (a) and keys (b) for each attention head of the first layer in Gemma 7B, corresponding to different RoPE frequencies. A mean is taken over 10 different Shakespeare quotes. We explain in Section 5 the high frequency behaviour in Head 5 and Head 8."

Description: Two heatmaps showing per-head frequency usage
- (a) Mean query norms at each attention head: Y-axis shows "High Frequencies" to "Low Frequencies", x-axis shows "Attention Head" 1-16, color scale 0-16 "Mean norm"
- (b) Mean key norms at each attention head: Similar structure, color scale 0-25 "Mean norm"
- Key elements: Heads 5 and 8 show notably high values in high-frequency regions; distinct banding patterns in low frequencies
- Notable patterns: Sparse, banded structure in low frequencies; Heads 5 and 8 exhibit exceptional high-frequency usage
- Supports claim: Identifies specific attention heads (5 and 8) that use high frequencies for positional attention; demonstrates sparse "channel" structure in low frequencies

## Section Summary

**Summary of the Section:** *We empirically showed that most of the RoPE usage in Gemma 7B occurs at the low frequencies. We also identified 'high frequency' heads and high norm bands* [p. 6].

---

⁶It remains under debate whether high attention scores imply a meaningful preference (Bibal et al., 2022).
