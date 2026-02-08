# 3 RWKV [p. 3-5]

[p. 3]

The RWKV model architecture is defined by four fundamental elements that are intrinsic to the time-mixing and channel-mixing blocks:

- $R$: The **Receptance** vector acts as the receiver of past information.
- $W$: The **Weight** signifies the positional weight decay vector, a trainable parameter within the model.
- $K$: The **Key** vector performs a role analogous to $K$ in traditional attention mechanisms.
- $V$: The **Value** vector functions similarly to $V$ in conventional attention processes.

These core elements interact multiplicatively at each timestep, as depicted in Figure 2.

## 3.1 Architecture

The RWKV model is composed of stacked residual blocks. Each block consists of a time-mixing and a channel-mixing sub-block, embodying recurrent structures to leverage past information.

The model uses a unique attention-like score update process, which includes a time-dependent softmax operation improving numerical stability and mitigating vanishing gradients (for rigorous proof, see Appendix H). It ensures that the gradient is propagated along the most relevant path. Additionally, layer normalization (Ba et al., 2016) incorporated within the architecture aids in stabilizing the gradients, effectively addressing both vanishing and exploding gradient issues. These design elements not only enhance the training dynamics of deep neural networks but also facilitate the stacking of multiple layers, leading to superior performance over conventional RNN models by capturing complex patterns across different levels of abstraction (see also Appendix I).

**Figure 2** (p. 3): "Elements within an RWKV block (left) and the complete RWKV residual block, equipped with a final head for language modeling (right)."
- Left panel shows the internal structure of a single RWKV block with two sub-blocks: Time Mixing (bottom) containing $R$, $K$, $V$ inputs flowing into a WKV operator, then through $\sigma$ gating to produce output; Channel Mixing (top) containing $R'$, $K'$ inputs flowing through $\sigma$ gating.
- Right panel shows the complete RWKV residual block stack: Input Embedding at the bottom, followed by LayerNorm, Time Mixing with token shift (with residual connections via $\oplus$), LayerNorm, Channel Mixing with token shift (with residual connections via $\oplus$), repeated for multiple layers, ending with LayerNorm, Out projection, and Softmax for Output Probabilities.

### 3.1.1 Token Shift

[p. 3-4]

In this architecture, all linear projection vectors ($R$, $K$, $V$ in time-mixing, and $R'$, $K'$ in channel-mixing) involved in computations are produced by linear interpolation between current and previous timestep inputs, facilitating a token shift.

The vectors for time-mixing computation are linear projections of linear combinations of the current and previous inputs of the block:

$$r_t = W_r \cdot (\mu_r \odot x_t + (1 - \mu_r) \odot x_{t-1}), \quad (11)$$

$$k_t = W_k \cdot (\mu_k \odot x_t + (1 - \mu_k) \odot x_{t-1}), \quad (12)$$

$$v_t = W_v \cdot (\mu_v \odot x_t + (1 - \mu_v) \odot x_{t-1}), \quad (13)$$

[p. 4]

as are the channel-mixing inputs:

$$r'_t = W'_r \cdot (\mu'_r \odot x_t + (1 - \mu'_r) \odot x_{t-1}), \quad (14)$$

$$k'_t = W'_k \cdot (\mu'_k \odot x_t + (1 - \mu'_k) \odot x_{t-1}). \quad (15)$$

The token shift is implemented as a simple offset in the temporal dimension at each block using the PyTorch (Paszke et al., 2019) library as `nn.ZeroPad2d((0,0,1,-1))`.

**Figure 3** (p. 4): "RWKV architecture for language modeling."
- Shows three sequential timesteps processing tokens "My", "name", "is" through the full RWKV architecture.
- Each timestep has: Layer Norm at bottom, Time Mix block with Token shift and residual connections (States passed between timesteps), Layer Norm, Channel Mix block with Token shift and residual connections, more layers denoted by "...", LM Head at top.
- Token shift arrows show information flowing from the previous timestep's Layer Norm output to the current timestep's Time Mix and Channel Mix blocks.
- Output predictions shown at top: "name", "is", "Bob".

### 3.1.2 WKV Operator

[p. 4]

The computation of the $WKV$ operator in the model parallels the method used in Attention Free Transformer (AFT) (Zhai et al., 2021). However, unlike AFT where $W$ is a pairwise matrix, the model treats $W$ as a channel-wise vector that is modified by relative position. This recurrent behavior is defined by the time-dependent update of the $WKV$ vectors, formalized in the following equation:

$$wkv_t = \frac{\sum_{i=1}^{t-1} e^{-(t-1-i)w+k_i} \odot v_i + e^{u+k_t} \odot v_t}{\sum_{i=1}^{t-1} e^{-(t-1-i)w+k_i} + e^{u+k_t}}. \quad (16)$$

To circumvent any potential degradation of $W$, a vector $U$ is introduced that separately attends to the current token. More information about this can be found in Appendix I.

### 3.1.3 Output Gating

[p. 4-5]

Output gating is implemented in both time-mixing and channel-mixing blocks using the sigmoid of the receptance, $\sigma(r)$. The output vector $o_t$ post the $WKV$ operator is given by:

$$o_t = W_o \cdot (\sigma(r_t) \odot wkv_t). \quad (17)$$

In the channel-mixing block, a similar operation is performed:

$$o'_t = \sigma(r'_t) \odot (W'_v \cdot \max(k'_t, 0)^2), \quad (18)$$

where the squared ReLU activation function is adopted (So et al., 2021).

## 3.2 Transformer-like Training

[p. 5]

RWKV can be efficiently parallelized using a technique called *time-parallel mode*, reminiscent of Transformers. The time complexity of processing a batch of sequences in a single layer is $O(BTd^2)$, primarily consisting of matrix multiplications $W_\lambda$, where $\lambda \in \{r, k, v, o\}$ (assuming $B$ sequences, $T$ maximum tokens, and $d$ channels). In contrast, updating attention scores $wkv_t$ involves a serial scan (see Appendix D for more detail) and has complexity $O(BTd)$.

The matrix multiplications can be parallelized similarly to $W_\lambda$, where $\lambda \in \{Q, K, V, O\}$ in conventional Transformers. The element-wise $WKV$ computation is time-dependent but can be readily parallelized along the other two dimensions (Lei et al., 2018).

## 3.3 RNN-like Inference

[p. 5]

Recurrent networks commonly utilize the output at state $t$ as input at state $t + 1$. This usage is also observed in the autoregressive decoding inference of language models, where each token must be computed before being passed to the next step. RWKV takes advantage of this RNN-like structure, known as *time-sequential mode*. In this context, RWKV can be conveniently formulated recursively for decoding during inference, as demonstrated in Appendix D.

## 3.4 Additional Optimizations

[p. 5]

**Custom Kernels** To address inefficiencies in the $WKV$ computation arising from the sequential nature of the task when using standard deep learning frameworks, a custom CUDA kernel has been developed. This kernel enables the execution of a single compute kernel on training accelerators, while all other parts of the model, such as matrix multiplications and point-wise operations, are already inherently parallelizable and efficient.

**Small Init Embedding** During the initial stage of training a transformer model (Vaswani et al., 2017), the authors observe that the embedding matrix undergoes slow changes, presenting a challenge for the model to move away from its initial noisy embedding state. To address this issue, they propose an approach that involves initializing the embedding matrix with small values and subsequently applying an additional LayerNorm operation. This accelerates and stabilizes the training process, allowing for the training of deep architectures with post-LN components. The effectiveness of this approach is demonstrated in Figure 9, illustrating improved convergence by enabling the model to quickly transition away from the initially small embedding state. This is achieved through small changes occurring in a single step, which subsequently lead to substantial alterations in directions and further notable changes after the LayerNorm operation.

**Custom Initialization** Building on principles from previous works (He et al., 2016; Jumper et al., 2021), an initialization strategy is adopted where parameters are set to values resembling an identity mapping while breaking symmetry to establish a clear information flow. The majority of weights are initialized to zero, and linear layers do not employ biases. Detailed formulas are given in Appendix E. The choice of initialization plays a crucial role in both the speed and quality of convergence (refer to Appendix F for further details).

## 3.5 Implementation

[p. 5]

RWKV is implemented using the PyTorch Deep Learning Library (Paszke et al., 2019). Additional optimization strategies inspired by DeepSpeed (Rasley et al., 2020) are integrated into the system, improving its efficiency and scalability.

The model begins with an embedding layer, as detailed in Section 3.4. Following this are several identical residual blocks arranged sequentially. These are depicted in Figures 2 and 3 and adhere to the principles outlined in Section 3.1.1. After the last block, a simple output projection head, consisting of a LayerNorm (Ba et al., 2016) and a linear projection, is employed for logits generation for next-token prediction and computation of the cross-entropy loss during training.
