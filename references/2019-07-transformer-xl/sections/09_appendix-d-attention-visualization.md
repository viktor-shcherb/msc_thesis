# Appendix D: Attention Visualization [p. 14–16]

Visualization of the attention learned by the SoTA model on the WikiText-103 validation set. This model has 16 10-head transformer layers and relies on a memory of length 640. [p. 14]

## Average attention distribution (Figure 5)

**Figure 5** (p. 14): "Average attention over the previous 640 tokens, where each row corresponds to a attention head and each column corresponds to a relative location. There are totally 160 attention heads, and every 10 heads come from a single layer. Darker colors indicate higher values."
- Shows a heatmap with 160 rows (heads, grouped by layer) and 640 columns (relative positions in memory). The overall trend is to focus more on the nearby tokens than the faraway ones. However, some attention heads have a wider attention distribution over the entire memory span, notably: [p. 14]
  - Head 8 from layer 1
  - Head 78 from layer 8
  - Head 158 from layer 16

## Individual head visualizations (Figure 6)

The three notable heads with wider attention spans are visualized for a randomly chosen position. [p. 14–15]

**Figure 6** (p. 15): "Visualization of the three heads with a wide attention range. Each row corresponds to a target location/token and each column corresponds to a context location/token. Tokens in the memory that have top 20% attention values are highlighted in red."
- (a) Head 8 from layer 1
- (b) Head 78 from layer 8
- (c) Head 158 from layer 16

Three different patterns of wider attention are observed: [p. 14–15]

- **Head 8 in the 1st layer:** an almost uniform attention over the entire memory span. This is intuitive, as lower-level layers need to screen the entire memory span to decide where to focus for higher-level layers. [p. 14]

- **Head 78 in the 8th layer (a middle-level layer):** a very sparse attention pattern scattered in all ranges of the memory. This fits the intuition that as information accumulates, the network may focus on some particular position with special interests. [p. 15]

- **Head 158 in the 16th layer (the last layer):** each target location (corresponding to each row) has its own distinct sparse focus, differing from head 78 where target locations largely share the same attentive location in memory. The pattern is also different from head 8, where a few locations are clearly attended more than others. [p. 15]

## Attention score decomposition (Figure 7)

As discussed in section 3.3, the attention score can be decomposed into four intuitive terms. Here, the contribution of these four terms to the overall attention trend in Fig. 5 is investigated. Since term (c) represents the global content bias (the prior importance of each word regardless of context), it is left out, focusing on terms (a), (b), and (d). For each term, the Softmax w.r.t. the memory span is taken and the resulting distribution is averaged over all tokens in the validation set. [p. 15]

**Figure 7** (p. 16): "Visualization of the three terms in computing the attention score. Each row corresponds to a attention head and each column corresponds to a relative location."
- (a) Term (a): content-based addressing
- (b) Term (b): content-dependent positional bias
- (c) Term (d): global positional bias

Observations: [p. 15–16]

- **Term (a)** is fully content-based addressing. When averaging over all target words, the result is essentially uniform over the entire context, except for a few very close words, which are likely to be semantically similar to the target word. [p. 15]

- **Term (b)** overall trend highly resembles that of the entire attention distribution in Fig. 5. This suggests that the global trend of focusing on the nearby context is largely contributed by this content-dependent positional bias. [p. 15]

- **Term (d)** also focuses more on nearby words. However, compared to the trend of term (b), it is clearly flatter and biases towards a longer context. [p. 15]
