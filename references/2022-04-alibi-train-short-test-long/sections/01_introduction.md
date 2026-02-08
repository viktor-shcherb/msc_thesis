# 1 Introduction [p. 1-2]

[p. 1]

When constructing a transformer-based language model, a major design decision is the length of training sequences, denoted $L$, which has to date been equivalent to the length of inference sequences. More context (larger $L$) improves predictions at inference time, but longer sequences are more expensive to train on.

Before transformers, RNN language models were trained on shorter-$L$ sequences and assumed to generalize to longer contexts at inference time (Mikolov et al., 2010; Mikolov & Zweig, 2012; Zaremba et al., 2014). Vaswani et al. (2017), introducing the transformer, speculated that it "may [...] extrapolate to sequence lengths longer than the ones encountered during training." The authors define **extrapolation** as a model's ability to continue performing well as the number of input tokens during validation increases beyond the number of tokens on which the model was trained. They find that transformer language models (LMs) that use sinusoidal position embeddings have very weak extrapolation abilities (see Figure 1). [p. 1]

The failure to extrapolate is caused by the position embedding method. As shown in Figure 1, recent alternatives to the original sinusoidal position method (Su et al., 2021; Raffel et al., 2020) have improved extrapolation. However, the better of these, the T5 bias, is considerably slower than the sinusoidal approach and uses extra memory and parameters (Figure 2). [p. 1]

The authors introduce Attention with Linear Biases (ALiBi) to facilitate efficient extrapolation. ALiBi negatively biases attention scores with a linearly decreasing penalty proportional to the distance between the relevant key and query. This approach eliminates position embeddings entirely. [p. 1]

[p. 2]

Compared to a sinusoidal model trained on the same input length, ALiBi requires no additional runtime or parameters and incurs a negligible (0-0.7%) memory increase. ALiBi can be implemented by changing only a few lines of existing transformer code. [p. 2]

Using ALiBi, a transformer LM can be trained on short-$L$ sequences and therefore at much lower cost, and it can still be reliably applied to long sequences at runtime. For example, a 1.3 billion parameter LM trained on $L = 1024$ tokens with ALiBi achieves the same perplexity as a sinusoidal model trained on $L = 2048$ when both are tested on sequences of 2048 tokens, even though *our model is 11% faster and uses 11% less memory*. [p. 2]

Though performance peaks at around two times the number of tokens the model was trained on, ALiBi maintains strong performance even on sequences of length 10,000. In recently explored settings where NLP training examples are given as context to an LM (Brown et al., 2020), this approach will allow exposure to more examples and enables generation of longer outputs. [p. 2]

## Figure 1

**Figure 1** (p. 2): "Extrapolation: as the (validation-set's) input sequence gets longer ($x$-axis), current position methods (sinusoidal, rotary, and T5) show degraded perplexity ($y$-axis, lower is better), but our method ($\S$3) does not. Models were trained on WikiText-103 with sequences of $L = 512$ (left) or $L = 1{,}024$ (right) tokens. T5 ran out of memory on our 32GB GPU. For more detail on exact perplexities and runtimes, see Tables 2 and 3 in the appendix."

Two side-by-side plots:
- **Left panel:** "Extrapolation for Models Trained on 512 Tokens." x-axis: Inference Input Tokens (512 to 16000); y-axis: Perplexity (15 to 55). Four lines: Sinusoidal (rises sharply after ~600), Rotary (rises after ~700), T5 Bias (rises after ~1100), ALiBi (stays flat/low across the full range).
- **Right panel:** "Extrapolation for Models Trained on 1024 Tokens." x-axis: Inference Input Tokens (1024 to 16000); y-axis: Perplexity (15 to 55). Same four methods with similar pattern: Sinusoidal and Rotary degrade quickly, T5 Bias degrades more slowly, ALiBi remains low and stable.

Key observation: ALiBi is the only method whose perplexity does not degrade as input length increases well beyond the training length. Sinusoidal degrades almost immediately; Rotary degrades slightly later; T5 Bias degrades more gradually but still substantially.
