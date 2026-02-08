# 6 Conjecture [p. 5-6]

[p. 5] How do transformers without explicit positional encoding learn absolute positions? The authors conjecture that the *causal attention* in autoregressive transformer language models allows them to predict the number of attendable tokens at each position, i.e., the number of tokens in the sequence that precede the current one. Such a mechanism could effectively encode the *absolute* position of each token into its vector representation. Indeed, the analysis (Section 5) reveals that some notion of absolute positions exists in the hidden layers of language models even when they are trained without explicit positional encoding, and that this information is acquired throughout the first few layers.

[p. 5-6] On the other hand, bidirectional transformer encoders (which are used in masked language modeling, e.g. Devlin et al. 2019) do not contain causal attention masks or any other limitation on the attention mechanism; thus, they should be unable to learn absolute positions without explicit positional encoding. The authors tested this corollary by training a masked language model based on RoBERTa large (Liu et al., 2019) on the Pile (see App. C for hyperparameters).

**Table 4** (p. 5): Validation set perplexity of *masked* language models (Devlin et al., 2019) trained with various positional encoding methods on an excerpt of the Pile (Gao et al., 2020). The model architecture is based on RoBERTa large (Liu et al., 2019), and processes 128 tokens per sequence. While position-aware models converge to very low perplexities, training without positional encodings (*NoPos*) fails.

|            | MLM Perplexity |
|------------|---------------|
| NoPos      | 147.18        |
| Learned    | 4.06          |
| Sinusoidal | 4.07          |
| ALiBi      | 4.00          |

[p. 5] Table 4 shows that, indeed, the NoPos model has significantly worse perplexities than the position-informed baselines. This result echoes the findings of Sinha et al. (2021), who also observed that MLMs without positional embeddings suffer significant performance degradation.
