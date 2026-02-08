# 2 Large Context Memory Constraint [p. 2-3]

[p. 2] Given input sequences $Q, K, V \in \mathbb{R}^{s \times d}$ where $s$ is the sequence length and $d$ is the head dimension, the matrix of outputs is computed as:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d}}\right)V$$

where softmax is applied row-wise. Each self-attention sub-layer is accompanied with a feedforward network applied to each position separately and identically, consisting of two linear transformations with a ReLU activation in between:

[p. 3]

$$\text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2$$

## Blockwise Parallel Transformers

[p. 3] Prior state-of-the-arts have led to substantial reductions in memory utilization by computing attention without full materialization in a block by block manner [30, 9, 23]. These advancements lowered the memory overhead of attention to $2bsh$ bytes per layer, where $b$ is batch size, $s$ is sequence length, and $h$ is hidden size of the model. To further reduce memory usage, blockwise parallel transformer (BPT) [23] introduced a strategy where the feedforward network associated with each self-attention sub-layer is computed in a block-wise fashion. This approach limits the maximum activation size of feedforward network from $8bsh$ to $2bsh$. In summary, the state-of-the-art transformer layer's memory cost of activation is $2bsh$.

## Large Output of Each Layer

[p. 3] While BPT significantly reduces memory demand in Transformers, it still presents a major challenge for scaling up context length because it requires storing the output of each layer. This storage is crucial due to the inherent nature of self-attention, which involves interactions among all elements (n to n interactions). Without these stored outputs, the subsequent layer's self-attention becomes computationally impractical, necessitating recomputation for each sequence element. Processing 100 million tokens with batch size 1 requires over 1000GB of memory even for a modest model with hidden size 1024. Modern GPUs and TPUs typically provide less than 100GB of high-bandwidth memory (HBM), and the prospects for significant HBM expansion are hindered by physical limitations and high manufacturing costs.
