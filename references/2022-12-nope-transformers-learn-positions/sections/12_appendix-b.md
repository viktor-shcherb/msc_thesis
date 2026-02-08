# B Word Order Analysis [p. 8]

[p. 8] Is positional information necessary for language modeling, or does the order of the input tokens not matter? To answer this, the authors conduct the following experiment: instead of computing the loss on the complete sequence, they pick a specific token in the sequence. The next token prediction is conditioned on the previous tokens in the sequence, and so they shuffle the order of the tokens in the prefix and compute the loss only for that specific token. They repeat the experiment with the original, un-shuffled prefix sequence as the baseline and compare the results.

The experiment was conducted on the NoPos model with an input sequence length of 512 using the WikiText-103 dataset. They randomly sample an index between 5 and 512 for the token they pick from each input sequence from the validation set.

[p. 8] Figure 5 shows the results of this experiment for 100 different inputs. These results clearly show that the transformer language model's next word predictions are not order-invariant.

**Figure 5** (p. 8): "Shuffling input tokens (for causal language modeling) leads to a massive degradation in token-level loss."

Box plot with X-axis: two conditions (Baseline, Shuffled Prefix), Y-axis: Token-Level Loss (range ~4 to ~12). The Baseline condition shows a compact box centered around ~4 with a very tight interquartile range and some minor upper outliers. The Shuffled Prefix condition shows a much higher and wider box centered around ~10–11, with the median around ~10.5 and a wider interquartile range spanning roughly 9 to 11. This demonstrates that shuffling the prefix causes a dramatic increase in token-level loss (from ~4 to ~10–11), confirming that the NoPos model relies on token order and is not order-invariant.
