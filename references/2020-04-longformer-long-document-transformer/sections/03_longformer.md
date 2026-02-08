# Longformer [p. 3-4]

[p. 3] The original Transformer model has a self-attention component with O(n^2) time and memory complexity where n is the input sequence length. To address this challenge, Longformer sparsifies the full self-attention matrix according to an "attention pattern" specifying pairs of input locations attending to one another. Unlike the full self-attention, the proposed attention pattern scales linearly with the input sequence, making it efficient for longer sequences. This section discusses the design and implementation of this attention pattern.

## 3.1 Attention Pattern

### Sliding Window

[p. 3-4] Given the importance of local context (Kovaleva et al., 2019), the attention pattern employs a fixed-size window attention surrounding each token. Using multiple stacked layers of such windowed attention results in a large receptive field, where top layers have access to all input locations and have the capacity to build representations that incorporate information across the entire input, similar to CNNs (Wu et al., 2019).

Given a fixed window size w, each token attends to 1/2 * w tokens on each side (Fig. 2b). The computation complexity of this pattern is O(n x w), which scales linearly with input sequence length n. In a transformer with l layers, the receptive field size at the top layer is l x w (assuming w is fixed for all layers). Depending on the application, it might be helpful to use different values of w for each layer to balance between efficiency and model representation capacity (section 4.1).

### Dilated Sliding Window

[p. 4] To further increase the receptive field without increasing computation, the sliding window can be "dilated". This is analogous to dilated CNNs (van den Oord et al., 2016) where the window has gaps of size dilation d (Fig. 2c). Assuming a fixed d and w for all layers, the receptive field is l x d x w, which can reach tens of thousands of tokens even for small values of d.

In multi-headed attention, each attention head computes a different attention score. The authors found settings with different dilation configurations per head improves performance by allowing some heads without dilation to focus on local context, while others with dilation focus on longer context.

### Global Attention

[p. 4] In state-of-the-art BERT-style models for NLP tasks, the optimal input representation differs from language modeling and varies by task:
- For masked language modeling (MLM), the model uses local context to predict the masked word.
- For classification, the model aggregates the representation of the whole sequence into a special token (`[CLS]` in case of BERT).
- For QA, the question and document are concatenated, allowing the model to compare the question with the document through self-attention.

The windowed and dilated attention are not flexible enough to learn task-specific representations. Accordingly, the authors add "global attention" on few pre-selected input locations. Importantly, this attention operation is symmetric: a token with a global attention attends to all tokens across the sequence, and all tokens in the sequence attend to it. Fig. 2d shows an example of a sliding window attention with global attention at a few tokens at custom locations.

Examples of global attention usage:
- For classification, global attention is used for the `[CLS]` token.
- For QA, global attention is provided on all question tokens.

Since the number of such tokens is small relative to and independent of n, the complexity of the combined local and global attention is still O(n). While specifying global attention is task specific, it is an easy way to add inductive bias to the model's attention, and it is much simpler than existing task specific approaches that use complex architecture to combine information across smaller input chunks.

### Linear Projections for Global Attention

[p. 4] Two sets of projections are used: Q_s, K_s, V_s to compute attention scores of sliding window attention, and Q_g, K_g, V_g to compute attention scores for the global attention. The additional projections provide flexibility to model the different types of attention, which is shown to be critical for best performance on downstream tasks. Q_g, K_g, V_g are all initialized with values that match Q_s, K_s, V_s.

### Equation 1: Scaled Dot-Product Attention [p. 4]

Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V

Standard attention score computation used in regular transformers. The expensive operation is the matrix multiplication QK^T because both Q and K have n (sequence length) projections.

## 3.2 Implementation

[p. 4] For Longformer, the dilated sliding window attention computes only a fixed number of the diagonals of QK^T. As shown in Fig. 1, this results in a linear increase in memory usage compared to quadratic increase for full self-attention. However, implementing it requires a form of banded matrix multiplication that is not supported in existing deep learning libraries like PyTorch/Tensorflow.

Fig. 1 compares the performance of three different ways of implementing it:
- **`loop`**: a memory efficient PyTorch implementation that supports dilation but is unusably slow and only used for testing.
- **`chunks`**: only supports the non-dilated case and is used for the pretraining/finetuning setting.
- **`cuda`**: a fully functioning highly optimized custom CUDA kernel implemented using TVM (Chen et al., 2018) and used for the language modeling experiments (see Appendix A for more details).

## Figure 1 (p. 1)

**Caption:** "Runtime and memory of full self-attention and different implementations of Longformer's self-attention; Longformer-loop is non-vectorized, Longformer-chunk is vectorized, and Longformer-cuda is a custom cuda kernel implementations."

- **Left plot (Time):** x-axis: seq len (up to ~16,000), y-axis: ms/batch (up to ~2,500). Full self-attention grows quadratically; Longformer-loop grows linearly but steeply; Longformer-chunks and Longformer-cuda grow linearly and are much faster, with Longformer-chunks being the fastest.
- **Right plot (Memory):** x-axis: seq len (up to ~16,000), y-axis: MB (up to ~15,000). Full self-attention grows quadratically and runs out of memory for long sequences on current GPUs. Longformer's memory usage scales linearly with the sequence length across all implementations.

## Figure 2 (p. 3)

**Caption:** "Comparing the full self-attention pattern and the configuration of attention patterns in our Longformer."

Four sub-figures showing attention matrices:
- **(a) Full n^2 attention:** dense attention matrix, all positions attend to all positions.
- **(b) Sliding window attention:** banded diagonal pattern, each token attends to a local window of neighbors.
- **(c) Dilated sliding window:** banded diagonal with gaps (dilation), allowing larger receptive field without more computation.
- **(d) Global+sliding window:** combination of the sliding window band pattern plus a few rows/columns that are fully dense (the global attention tokens).
