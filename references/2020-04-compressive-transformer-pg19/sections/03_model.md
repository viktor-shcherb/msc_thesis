# 3 Model [p. 2-4]

[p. 2-3] The Compressive Transformer is a long-range sequence model which compacts past activations into a compressed memory. It is a variant of the Transformer (Vaswani et al., 2017), a deep residual network which only uses attention to propagate information over time (namely *multi-head attention*). It builds on the ideas of the TransformerXL (Dai et al., 2019) which maintains a memory of past activations at each layer to preserve a longer history of context. The TransformerXL discards past activations when they become sufficiently old (controlled by the size of the memory). The key principle of the Compressive Transformer is to compress these old memories, instead of discarding them, and store them in an additional *compressed memory*.

**Figure 1** (p. 3): "The Compressive Transformer keeps a fine-grained memory of past activations, which are then compressed into coarser *compressed* memories. The above model has three layers, a sequence length n_s = 3, memory size n_m = 6, compressed memory size n_cm = 6. The highlighted memories are compacted, with a compression function f_c per layer, to a single compressed memory -- instead of being discarded at the next sequence. In this example, the rate of compression c = 3."

The figure shows three layers stacked vertically with time on the horizontal axis. Each layer has three regions separated by vertical bars: compressed memory (left, green circles), memory (middle, orange/red circles), and sequence (right, orange circles). Compression functions f_c^(1), f_c^(2), f_c^(3) are shown mapping from the oldest memories to compressed memory for each layer.

## 3.1 Description [p. 3]

Define n_m and n_cm to be the number of respective memory and compressive memory slots in the model per layer. The overall input sequence S = x_1, x_2, ..., x_{|s|} represents input observations (e.g. tokens from a book). These are split into fixed-size windows of size n_s for the model to process in parallel. The model observes **x** = x_t, ..., x_{t+n_s} at time t, which is referred to as the *sequence* (e.g. in Figure 1). As the model moves to the next sequence, its n_s hidden activations are pushed into a fixed-sized FIFO memory (like the TransformerXL). The oldest n_s activations in memory are evicted, but unlike the TransformerXL they are not discarded. Instead a *compression operation* is applied:

f_c : R^{n_s x d} -> R^{floor(n_s / c) x d}

mapping the n_s oldest memories to floor(n_s / c) compressed memories which are then stored in a secondary FIFO *compressed memory*. d denotes the hidden size of activations and c refers to the compression rate; a higher value indicates more coarse-grained compressed memories. The full architecture is described in Algorithm 1.

### Algorithm 1: Compressive Transformer [p. 3]

**At time zero:**
1. m_0 <- 0 // Initialize memory to zeros (l x n_m x d)
2. cm_0 <- 0 // Initialize compressed memory to zeros (l x n_cm x d)

**At time t:**
3. h^(1) <- xW_emb // Embed input sequence (n_s x d)
4. **for** layer i = 1, 2, ..., l **do**
5.   mem^(i) <- concat(cm_t^(i), m_t^(i)) // ((n_cm + n_m) x d)
6.   a_tilde^(i) <- multihead_attention^(i)(h^(i), mem_t^(i)) // MHA over both mem types (n_s x d)
7.   a^(i) <- layer_norm(a_tilde^(i) + h^(i)) // Regular skip + layernorm (n_s x d)
8.   old_mem^(i) <- m_t^(i)[:n_s] // Oldest memories to be forgotten (n_s x d)
9.   new_cm^(i) <- f_c^(i)(old_mem^(i)) // Compress oldest memories by factor c (floor(n_s/c) x d)
10.  m_{t+1}^(i) <- concat(m_t^(i), h^(i))[-n_m :] // Update memory (n_m x d)
11.  cm_t^(i) <- concat(cm_t^(i), new_cm^(i))[-n_cm :] // Update compressed memory (n_cm x d)
12.  h^(i+1) <- layer_norm(mlp^(i)(a^(i)) + a^(i)) // Mixing MLP (n_s x d)

## 3.2 Compression Functions and Losses [p. 4]

For choices of compression functions f_c the authors consider:
1. **max/mean pooling**, where the kernel and stride is set to the compression rate c
2. **1D convolution** also with kernel & stride set to c
3. **dilated convolutions**
4. **most-used** where the memories are sorted by their average attention (usage) and the most-used are preserved. The pooling is used as a fast and simple baseline. The *most-used* compression scheme is inspired by the garbage collection mechanism in the Differentiable Neural Computer (Graves et al., 2016) where low-usage memories are erased. The convolutional compression functions contain parameters which require training.

### Compression losses

One can train the compression network using gradients from the loss; however for very old memories this requires backpropagating-through-time (**BPTT**) over long unrolls. The authors also consider some local auxiliary compression losses:

**Auto-encoding loss:** reconstruct the original memories from the compressed memories:

L^{ae} = ||old_mem^(i) - g(new_cm^(i))||_2

where g : R^{n_s/c x d} -> R^{n_s x d} is learned. This is a lossless compression objective -- it attempts to retain all information in memory.

**Attention-reconstruction loss** (Algorithm 2): reconstructs the content-based attention over memory, with content-based attention over the compressed memories. This is a lossy objective, as information that is no longer attended to can be discarded, and the authors found this worked best. Compression loss gradients are stopped from passing into the main network as this prevents learning. Instead the Transformer optimizes the task objective and the compression network optimizes the compression objective conditioned on task-relevant representations; there is no need to mix the losses with a tuning constant.

### Algorithm 2: Attention-Reconstruction Loss [p. 4]

1. L^{attn} <- 0
2. **for** layer i = 1, 2, ..., l **do**
3.   h^(i) <- stop_gradient(h^(i)) // Stop compression grads from passing...
4.   old_mem^(i) <- stop_gradient(old_mem^(i)) // ...into transformer network.
5.   Q, K, V <- stop_gradient(attention params at layer i) // Re-use attention weight matrices.
6.   def attn(h, m) <- sigma((hQ)(mK))(mV) // Use content-based attention (no relative).
7.   new_cm^(i) <- f_c^(i)(old_mem^(i)) // Compression network (to be optimized).
8.   L^{attn} <- L^{attn} + ||attn(h^(i), old_mem^(i)) - attn(h^(i), new_cm^(i))||_2

## 3.3 Temporal Range [p. 4]

The TransformerXL with a memory of size n has a maximum temporal range of l x n with an attention cost of O(n_s^2 + n_s * n) (see Dai et al. (2019) for a detailed discussion).

The Compressive Transformer has a maximum temporal range of l x (n_m + c * n_cm) with an attention cost of O(n_s^2 + n_s(n_m + n_cm)).

For example, setting n_cm = n_m = n/2 and c = 3, the maximum temporal range is two times greater than the TransformerXL with an identical attention cost. Thus if we can learn in the c > 1 compressed setting, the temporal range of the model can be significantly increased.
