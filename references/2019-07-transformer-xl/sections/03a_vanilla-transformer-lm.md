# 3 Model [p. 3]

## Problem setup

Given a corpus of tokens **x** = (x_1, ..., x_T), the task of language modeling is to estimate the joint probability P(**x**), which is often auto-regressively factorized as P(**x**) = prod_t P(x_t | **x**_{<t}). The problem reduces to estimating each conditional factor. [p. 3]

A trainable neural network encodes the context **x**_{<t} into a fixed size hidden state, which is multiplied with word embeddings to obtain logits. The logits are then fed into the Softmax function, yielding a categorical probability distribution over the next token. [p. 3]

## 3.1 Vanilla Transformer Language Models [p. 3]

The central problem is how to train a Transformer to effectively encode an arbitrarily long context into a fixed size representation. Given infinite memory and computation, a simple solution would be to process the entire context sequence using an unconditional Transformer decoder. However, this is usually infeasible with limited resources. [p. 3]

One feasible but crude approximation: split the entire corpus into shorter segments of manageable sizes, and only train the model within each segment, ignoring all contextual information from previous segments. This is the *vanilla model*, visualized in Fig. 1a. Under this paradigm, information never flows across segments in either the forward or backward pass. [p. 3]

**Figure 1** (p. 3): "Illustration of the vanilla model with a segment length 4."
- (a) Train phase: shows two segments (Segment 1 and Segment 2) processed independently with no information flow between them. Each segment has its own multi-layer self-attention computation.
- (b) Evaluation phase: shows a sliding window approach with "Limited Context" where the segment is shifted right by one position at each step, recomputing from scratch. Only the last position's prediction is used.

Two critical limitations of using a fixed-length context: [p. 3]
1. The largest possible dependency length is upper bounded by the segment length, which is a few hundred on character-level language modeling (Al-Rfou et al., 2018). Although self-attention is less affected by vanishing gradients compared to RNNs, the vanilla model is not able to fully exploit this optimization advantage.
2. Though it is possible to use padding to respect sentence or semantic boundaries, in practice it has been standard to simply chunk long text into fixed-length segments due to improved efficiency (Peters et al., 2018; Devlin et al., 2018; Al-Rfou et al., 2018). Simply chunking leads to context fragmentation.

During evaluation, the vanilla model consumes a segment of the same length as in training, but only makes one prediction at the last position. Then the segment is shifted right by one position and the new segment is reprocessed from scratch (Fig. 1b). This ensures each prediction utilizes the longest possible context and relieves context fragmentation, but is extremely expensive. [p. 3]
