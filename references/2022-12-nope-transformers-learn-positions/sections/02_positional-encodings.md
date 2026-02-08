# 2 Positional Encodings [p. 2]

Transformer models consist of interleaved self-attention and feed-forward layers, which are both order-invariant. Therefore, to convey the order of the input tokens, some form of positional information is explicitly introduced into the model.

*Absolute positions* are commonly encoded as vectors (one for each position), which are then added to the input tokens' embeddings and fed to the first layer of the transformer. *Relative positions* are typically encoded as biases (added to attention scores) within the self-attention layers.

The paper considers three popular methods as baselines:

**Learned.** Embeddings trained to represent absolute positions (Sukhbaatar et al., 2015; Gehring et al., 2017). Learned positional embeddings are commonly used in MLMs (Devlin et al., 2019; Liu et al., 2019) as well as in large autoregressive language models, such as GPT-3 (Brown et al., 2020). [p. 2]

**Sinusoidal.** Constant vectors computed by a non-parametric function of the input token's absolute position. Sine and cosine functions of different frequencies are used, such that each dimension of the positional encoding corresponds to a sinusoid. Sinusoidal embeddings were introduced in Vaswani et al. (2017) for machine translation, and are also used in language modeling (Baevski and Auli, 2019). [p. 2]

**ALiBi.** Attention with LInear BIases (Press et al., 2022) injects information about the relative distances between tokens by adding negative biases to attention scores, which grow linearly with the distance between each pair of tokens. [p. 2]
