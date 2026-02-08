# 1 Introduction [p. 1-2]

Language modeling requires modeling long-term dependency, with successful applications including unsupervised pretraining (Dai and Le, 2015; Peters et al., 2018; Radford et al., 2018; Devlin et al., 2018). [p. 1]

## RNN limitations

Recurrent neural networks (RNNs), in particular LSTMs (Hochreiter and Schmidhuber, 1997), have been a standard solution for language modeling. However, RNNs are difficult to optimize due to gradient vanishing and explosion (Hochreiter et al., 2001), and gating in LSTMs plus gradient clipping (Graves, 2013) might not fully address this. Previous work found that LSTM language models use 200 context words on average (Khandelwal et al., 2018), indicating room for improvement. [p. 1]

## Transformer limitations

Direct connections between long-distance word pairs in attention mechanisms might ease optimization and enable learning of long-term dependency (Bahdanau et al., 2014; Vaswani et al., 2017). Al-Rfou et al. (2018) designed auxiliary losses to train deep Transformer networks for character-level language modeling, outperforming LSTMs by a large margin. However, the LM training in Al-Rfou et al. (2018) is performed on separated fixed-length segments of a few hundred characters, without any information flow across segments. [p. 1]

Two consequences of the fixed context length:
1. The model cannot capture any longer-term dependency beyond the predefined context length.
2. Fixed-length segments are created by selecting consecutive chunks without respecting sentence or semantic boundaries. The model lacks necessary contextual information to predict the first few symbols, leading to inefficient optimization and inferior performance. [p. 1]

The authors refer to this problem as *context fragmentation*. [p. 1]

## Proposed solution

To address these limitations, the authors propose Transformer-XL (meaning extra long). Key ideas: [p. 1-2]
- Instead of computing hidden states from scratch for each new segment, reuse hidden states obtained in previous segments.
- The reused hidden states serve as memory for the current segment, building a recurrent connection between segments.
- Information can be propagated through the recurrent connections, enabling very long-term dependency.
- Passing information from the previous segment also resolves context fragmentation.
- The authors show the necessity of using relative positional encodings rather than absolute ones, to enable state reuse without temporal confusion.
- A new relative positional encoding formulation is introduced that generalizes to attention lengths longer than those observed during training. [p. 2]

## Results summary

- Strong results on five datasets, from word-level to character-level language modeling. [p. 2]
- Able to generate relatively coherent long text articles with *thousands of* tokens (see Appendix E), trained on only 100M tokens. [p. 2]

## Contributions

> "Our main technical contributions include introducing the notion of recurrence in a purely self-attentive model and deriving a novel positional encoding scheme. These two techniques form a complete set of solutions, as any one of them alone does not address the issue of fixed-length contexts." [p. 2]

Transformer-XL is the first self-attention model that achieves substantially better results than RNNs on both character-level and word-level language modeling. [p. 2]
