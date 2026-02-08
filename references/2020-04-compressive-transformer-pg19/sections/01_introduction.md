# 1 Introduction [p. 1-2]

## Memory in neural networks

[p. 1] Humans remember information over long time horizons via lossy compression -- aggressively selecting, filtering, or integrating input stimuli based on factors of surprise, perceived danger, or repetition (Richards and Frankland, 2017).

RNNs (Rumelhart et al., 1986) learn to represent observation history in a compressed state vector. The LSTM (Hochreiter and Schmidhuber, 1997) uses learned gates on its state vector to determine what information is stored or forgotten from memory.

## The Transformer and its memory cost

[p. 1] The key advance since LSTMs has been in *not* bottlenecking all historical information in the state, but instead keeping past activations in an external memory and *attending* to them. The Transformer (Vaswani et al., 2017) stores the hidden activation of every time-step and integrates this information using an attention operator (Bahdanau et al., 2014). The Transformer represents the past with a tensor (depth x memory size x dimension) of past observations that is, in practice, an order of magnitude larger than an LSTM's hidden state.

The Transformer has brought state-of-the-art performance in machine translation (Vaswani et al., 2017), language modelling (Dai et al., 2019; Shoeybi et al., 2019), video captioning (Zhou et al., 2018), and language understanding benchmarks (Devlin et al., 2018; Yang et al., 2019).

[p. 1-2] One drawback is the computational cost of attending to every time-step and the storage cost of preserving this large memory. Several works have focused on reducing the computational cost of attention with sparse access mechanisms (Rae et al., 2016; Child et al., 2019; Sukhbaatar et al., 2019; Lample et al., 2019). However sparse attention does not solve the storage problem and often requires custom sparse kernels for efficient implementation.

## The Compressive Transformer proposal

[p. 2] The authors propose the Compressive Transformer, a simple extension to the Transformer which maps past hidden activations (memories) to a smaller set of compressed representations (compressed memories). It uses the same attention mechanism over both its set of memories and compressed memories, learning to query both its short-term granular memory and longer-term coarse memory.

Key results claimed:
- State-of-the-art in character-based language modelling: 0.97 bpc on Enwik8 from the Hutter Prize (Hutter, 2012)
- State-of-the-art in word-level language modelling: 17.1 perplexity on WikiText-103 (Merity et al., 2016)

[p. 2] The Compressive Transformer also works for high-frequency speech modelling with a trend of lower likelihood than TransformerXL and Wavenet (Oord et al., 2016) when trained over 400,000 steps. It can be used as a memory component within an RL agent, IMPALA (Espeholt et al., 2018), and can successfully compress and make use of past observations.

## PG-19 benchmark

[p. 2] The authors present a new book-level language-modelling benchmark PG-19, extracted from texts in Project Gutenberg (https://www.gutenberg.org/), to further promote the direction of long-context sequence modelling. This is over double the size of existing LM benchmarks and contains text with much longer contexts.
