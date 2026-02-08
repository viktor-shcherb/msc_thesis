# 2. Non-uniformity in Positional Interpolation [p. 2-4]

## 2.1. Preliminary [p. 2]

Transformer models require explicit positional information, often in the form of position embedding, to represent the order of input tokens. The work focuses on the RoPE (Su et al., 2021) position embedding, which is widely used in recent LLMs. For a token at position index $n$, its corresponding RoPE encoding can be simplified as follows:

$$[cos(n\theta_0), sin(n\theta_0), cos(n\theta_1), \cdots, cos(n\theta_{d/2-1}), sin(n\theta_{d/2-1})]$$
(1)

where $d$ is the embedding dimension, $n\theta_i$ is the rotary angle of token at position $n$, $\theta_i = \theta^{-2i/d}$ represents the rotation frequencies. In RoPE, the default base value of $\theta$ is 10000.

**Context window extension ratio $s$ and positional interpolation.** The context window extension ratio $s$ is defined as the ratio of extended context length $L'$ to the original length $L$: $s = \frac{L'}{L}$.

To extend the context window from $L$ to $L'$, current positional interpolation methods suggest downscaling rotation frequencies $\theta_i$ based on extension ratio $s$. Let $\beta = \theta^{2/d}$, and $\lambda$ denote the actual rescale factor related to $s$. The unified positional interpolation methods are as follows:

$$\left[cos\left(\frac{n}{\lambda(\beta)^0}\right), sin\left(\frac{n}{\lambda(\beta)^0}\right), cos\left(\frac{n}{\lambda(\beta)^1}\right), \cdots, sin\left(\frac{n}{\lambda(\beta)^{d/2-1}}\right)\right]$$
(2)

**Linear positional interpolation (PI).** PI (Chen et al., 2023a) suggests linear interpolation of position indices within the pre-trained length limit. For a target extension ratio $s$, the rotation angles of all positions are linearly reduced by $\lambda = s$ across all RoPE dimensions. However, this makes the position information very "crowded", hindering the model's ability to distinguish closely positioned tokens. Therefore, PI tends to underperform at high extension ratios.

**NTK-based interpolation and extrapolation.** (LocalLLaMA, 2023b;a) look at RoPE from an information encoding perspective and apply the Neural Tangent Kernel (NTK) theory (Jacot et al., 2018; Tancik et al., 2020). To mitigate the crowded-positions issue in PI, they suggest distributing interpolation pressure across RoPE dimensions. It scales lower (high frequency) dimensions less and higher (low frequency) dimensions more, resulting in both positional interpolation and extrapolation, where $\lambda = s^i$. The improved dynamic NTK (LocalLLaMA, 2023a) adjusts the extension ratio at each position based on the current sequence length. Unlike PI, which necessitates fine-tuning, NTK-aware methods can extend context windows in non-fine-tuning scenarios, but usually with a maximum extension ratio of 4x.

[p. 3] **YaRN** (Peng et al., 2023) introduces a significant improvement to positional interpolation performance. It divides RoPE dimensions into three frequency-based groups, each with a different interpolation strategy. High frequency dimensions undergo extrapolation ($\lambda$=1), while low frequency dimensions use linear interpolation (PI). The RoPE dimensions that fall in-between employ the NTK. The key of YaRN lies in its grouping of RoPE dimensions, which currently depends on human-led empirical experiments. This may result in sub-optimal performance for new LLMs.

## 2.2. Study on Non-uniform Positional Interpolation [p. 3-4]

Inspired by NTK and YaRN, the authors notice their gains from nonlinearity, specifically in considering different frequencies across RoPE dimensions for specialized interpolation and extrapolation. However, current non-linearities heavily rely on human-designed rules. This naturally raises two questions: (1) Is the current positional interpolation optimal? (2) Are there unexplored non-linearities?

To answer these questions, the authors use evolution search (see Sec. 3) to discover better non-uniform positional interpolations for LLaMA2-7B. The search is guided by perplexity, using 5 random samples from PG19 (Rae et al., 2019) validation set.

> **Finding 1:** *RoPE dimensions exhibit substantial non-uniformities, which are not effectively handled by current positional interpolation methods.* [p. 3]

The authors search the optimal $\lambda$ for each RoPE dimension in Eq. 2. Table 1 compares the perplexity of LLaMA2-7B under different methods on PG19 and Proof-pile (Azerbayev et al., 2022) test sets, without fine-tuning. The searched solution shows significant improvements, suggesting that current linear (PI) and non-uniform (Dynamic-NTK and YaRN) interpolations are sub-optimal. Notably, YaRN underperforms than PI and NTK on PG19, as it doesn't reach the target context window length for non-fine-tuned LLM. For example, YaRN's perplexity spikes after 7k in an 8k context size.

Through the search, the rescaled factors $\lambda$ in Eq. 2 become non-uniform, differing from the fixed scale $s$ in PI, NTK's formula calculation, and YaRN's group-wise calculation. These non-uniform factors significantly improve LLaMA2's language modeling performance (i.e., perplexity) for 8k and 16k context windows without fine-tuning. This is because the resulting positional embedding effectively preserves the original RoPE, especially key dimensions, thus reducing LLM's difficulty in distinguishing close token positions.

**Table 1.** Perplexity of LLaMA2-7B extended via different methods. By a simple search for the rescale factors of each RoPE dimension, we can greatly reduce the perplexity. [p. 3]

| (LLaMA2-7B) | PG19 (5 samples) | | Proof-pile (10 samples) | |
|---|---|---|---|---|
| Extension method | 8192 | 16384 | 8192 | 16384 |
| PI | 10.65 | 20.49 | 3.65 | 4.93 |
| Dy-NTK | 10.21 | 23.29 | 3.50 | 3.87 |
| YaRN | 32.64 | 87.89 | 3.49 | 3.25 |
| **Search for RoPE Dim-wise $\lambda$** | **9.37** | **11.34** | **3.45** | **3.13** |

> **Finding 2:** *RoPE for the initial tokens in the input sequence should be extrapolated with less interpolation.* [p. 4]

For the initial $\hat{n}$ tokens in input sequences, the authors hypothesize that their RoPE should do less interpolation. This is because they receive large attention scores, making them crucial to attention layers, as observed in Streaming LLM (Xiao et al., 2023) and LM-Infinite (Han et al., 2023). To verify this, they extend the context window to 8k and 16k using PI and NTK, keeping the first $\hat{n}$ (0, 2, 4, ..., 256) tokens without interpolation. When $\hat{n}$=0, it reverts to the original PI and NTK.

**Table 2.** Perplexity of LLaMA2-7B extended on PG19 (5 samples). When retaining the first $\hat{n}$ tokens without positional interpolation, the performance of both PI and Dynamic-NTK are improved. [p. 3]

| (LLaMA2-7B) | L' | No interpolation for first $\hat{n}$ tokens | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| Extension method | | 0 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 |
| PI | 8k | 10.65 | 10.65 | 10.65 | 10.65 | 10.66 | 10.59 | **10.49** | 10.54 | 11.74 |
| | 16k | 20.49 | 20.39 | 20.36 | 20.02 | 19.64 | 19.96 | 20.64 | 22.27 | 34.65 |
| Dy-NTK | 8k | 10.21 | 10.21 | 10.21 | 10.21 | 10.22 | 10.20 | 10.15 | **10.13** | 10.62 |
| | 16k | 23.29 | 23.29 | 23.27 | 23.08 | **22.68** | 22.94 | 23.58 | 27.94 | 90.99 |

Table 2 highlights two key observations: **(1)** retaining the starting tokens without position interpolation indeed improves the performance. **(2)** The optimal number of starting tokens, $\hat{n}$, depends on the target extension length.

> **Finding 3:** *Non-uniform positional interpolation effectively extends LLM context window in both fine-tuning and non-fine-tuning settings.* [p. 4]

While the searched non-uniform position interpolation significantly improves the extension performance at 8k and 16k without fine-tuning, longer extensions require fine-tuning. The authors fine-tune LLaMA2-7B with the searched RoPE for a 64k context window size (see Appendix for settings).

**Table 3.** Proof-pile perplexity of the extended LLaMA2-7B with a 64k context window in non-fine-tuned and fine-tuned settings. [p. 3]

| Method | non-fine-tuned | fine-tuned |
|---|---|---|
| PI | 72.54 | 2.44 |
| YaRN | 4.15 | 2.42 |
| **Search (Dim-wise $\lambda$ and $\hat{n}$)** | **3.22** | **2.36** |

The searched method significantly outperforms PI and YaRN, both before and after fine-tuning LLaMA2-7B. This is due to effective use of non-uniform positional interpolation, minimizing information loss and providing a better initialization for fine-tuning.

**Summary.** The study uncovers two non-uniformities: varying RoPE dimensions and token positions. Utilizing these non-uniformities effectively in positional interpolation greatly improves LLM context extension performance.

**Figure 2** (p. 3): "An illustrative example to show RoPE embedding under different interpolation methods. *Upper*: RoPE under direct extrapolation. *Middle*: Rescaled RoPE under linear positional interpolation. *Down*: LongRoPE fully exploits the identified two non-uniformities, leading to varied interpolation and extrapolation across RoPE dimensions at different token positions."

The figure shows three rows of waveform plots. The upper row shows standard RoPE with normal oscillations in the pre-trained range (0-4096) and direct extrapolation into the unseen range (4096-8192). The middle row shows PI rescaled RoPE with compressed oscillations across the full 0-8192 range. The bottom row shows the LongRoPE approach with three colored lines (Dim=0/64, Dim=40/64, Dim=60/64), illustrating that different RoPE dimensions get different levels of interpolation/extrapolation, and the initial $\hat{n}$ positions are retained without interpolation.
