# Background: Positional Encoding in Transformers [p. 3]

[p. 3] Transformers, in contrast to sequential models such as RNNs, are parallel architectures that employ positional encoding to help encode word order. The most common choices for positional encoding are either *absolute*, where each absolute position (e.g. 1, 2, 3, ...) is directly represented, or *relative*, where the distance between tokens is used as positional information. This section briefly reviews the popular encoding methods used in Transformers (formal details in Appendix B).

## Absolute Position Embedding (APE)

APE embeds each absolute position $i$ into a position vector $\mathbf{p}_i$ and adds word embeddings to their corresponding $\mathbf{p}_i$ before feeding them to the model. The non-parametric variant of APE uses periodic functions such as sine and cosine to generate embeddings for any position $i$ (Vaswani et al., 2017). A learned version of APE, used in GPT3 (Brown et al., 2020) and OPT (Zhang et al., 2022), trains the position embeddings along with the model parameters, and it cannot generate a position embedding for unseen positions, so the context window is set to a fixed length.

## T5's Relative Bias

T5's Relative bias first maps the relative distance $(i - j)$ between tokens at positions $i$ and $j$ to a scalar bias value $b = f(i - j)$, where $f$ is a lookup table. The relative bias $b$ (learned during training) then is added to the dot product of the query and key in the self-attention mechanism. The lookup table maps distances larger than a threshold to the same parameter to enable generalization to unseen distances.

## Rotary

Rotary, used in PaLM (Chowdhery et al., 2022) and LLaMA (Touvron et al., 2023), rotates the query and key representations with an angle proportional to their absolute positions before applying the dot product attention. As a result of this rotation, the attention dot product will only depend on the relative distance between tokens, effectively making it a relative positional encoding (Su et al., 2021).

## ALiBi

ALiBi, used in BLOOM (Scao et al., 2022a), is similar to T5's Relative Bias but instead subtracts a scalar bias from the attention score. This bias grows linearly with the distance between the query and key tokens. This, in effect, creates a preference toward recent tokens (recency bias).

## Decoder-only Transformers without PE

Encoder-only Transformers, such as BERT, become bag-of-words models in the absence of positional encoding. However, decoder-only Transformers with causal attention mask are not permutation invariant and can model sequences even without explicit position information (Tsai et al., 2019). But it is unclear if these models encode position information implicitly or generalize to unseen lengths. This is demystified in Section 5.
