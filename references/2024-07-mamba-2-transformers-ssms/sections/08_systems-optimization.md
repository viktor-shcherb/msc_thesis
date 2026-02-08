# 8 Systems Optimization for SSMs [p. 25-26]

[p. 25] This section describes several systems optimizations for SSMs, in particular the Mamba-2 architecture, for large-scale efficient training and inference. The focus is on tensor parallel and sequence parallel for large-scale training, as well as variable-length sequences for efficient finetuning and inference.

## 8.1 Tensor Parallel

[p. 26] Tensor parallelism (TP) (Shoeybi et al. 2019) is a model parallelism technique that splits each layer (e.g., attention, MLP) to run on multiple accelerators such as GPUs. This technique is widely used to train most large models (Brown et al. 2020; Chowdhery et al. 2023; Touvron, Lavril, et al. 2023; Touvron, L. Martin, et al. 2023) on GPU clusters where each node typically has 4-8 GPUs with fast networking such as NVLink. TP was originally designed for the Transformer architecture, and it is not straightforward to adapt it to other architectures. The authors first show the challenge of using TP with the Mamba architecture, then show how the Mamba-2 architecture is designed to make TP efficient.

### Mamba-1 TP Challenge

[p. 26] Recall the Mamba architecture, with a single input $u \in \mathbb{R}^{L \times d}$ (no batching for simplicity), input projection matrices $W^{(x)}, W^{(z)} \in \mathbb{R}^{d \times ed}$ where $e$ is the expansion factor (typically 2), and output projection matrix $W^{(o)} \in \mathbb{R}^{ed \times d}$:

$$x = u W^{(x)\top} \in \mathbb{R}^{L \times ed}$$
$$z = u W^{(z)\top} \in \mathbb{R}^{L \times ed}$$
$$x_c = \text{conv1d}(x) \in \mathbb{R}^{L \times ed} \quad \text{(depthwise, independent along } d\text{)}$$
$$\Delta, B, C = \text{low-rank projection}(x_c)$$
$$y = SSM_{A,B,C,\Delta}(x_c) \in \mathbb{R}^{L \times ed} \quad \text{(independent along } d\text{)}$$
$$y_g = y \cdot \phi(z) \quad \text{(gating, e.g., with } \phi \text{ being SiLU)}$$
$$\text{out} = y_g W^{(o)\top} \in \mathbb{R}^{L \times d}.$$

[p. 26] With TP, suppose the computation is split along 2 GPUs. It is easy to split the input projection matrices $W^{(x)}$ and $W^{(z)}$ into two partitions of size $d \times \frac{ed}{2}$. Then each GPU would hold half of $x_c$ of size $L \times \frac{ed}{2}$. However, since $\Delta, B, C$ are functions of $x_c$, an extra all-reduce between the GPUs would be needed to get the whole of $x_c$ before computing $\Delta, B, C$. After that the two GPUs can compute the SSM in parallel since they are independent along $d$. At the end, the output projection matrices $W^{(o)}$ can be split into two partitions each of size $\frac{ed}{2} \times d$, and an all-reduce is performed at the end.

Compared to Transformers, this would incur two all-reduces instead of one, doubling the time spent in communication. For large-scale Transformers training, communication might already take a significant fraction of time (e.g. 10-20%), and doubling communication would make Mamba not as efficient for large-scale training.

### Mamba-2 TP Solution

[p. 26] With Mamba-2, the goal is to have only one all-reduce per block, similar to attention or MLP blocks in Transformers. The key change is that the projection to get $\Delta, B, C$ is made directly from $u$ instead of from $x_c$, allowing the projection matrices to be split across different GPUs. This is equivalent to having several "groups" of $\Delta, B, C$ on different GPUs, which is like having several "groups" of $\Delta, B, C$ on a larger "logical GPU". Moreover, GroupNorm is used within each block, with number of groups divisible by the TP degree, so that the GPUs in a TP group do not have to communicate within the block:

$$x = u W^{(x)\top} \in \mathbb{R}^{L \times ed}$$
$$z = u W^{(z)\top} \in \mathbb{R}^{L \times ed}$$
$$\Delta, B, C = \text{projection}(u) \quad \text{(one or more groups of } \Delta, B, C \text{ per GPU)}$$
$$x_c = \text{conv1d}(x) \in \mathbb{R}^{L \times ed} \quad \text{(depthwise, independent along } d\text{)}$$
$$y = SSM_{A,B,C,\Delta}(x_c) \in \mathbb{R}^{L \times ed} \quad \text{(independent along } d\text{)}$$
$$y_g = y \cdot \phi(z) \quad \text{(gating, e.g., with } \phi \text{ being SiLU)}$$
$$y_n = \text{groupnorm}(y_g) \quad \text{(number of groups divisible by degree of tensor parallel)}$$
$$\text{out} = y_g W^{(o)\top} \in \mathbb{R}^{L \times d}.$$

[unclear: The paper writes the final output as $y_g W^{(o)\top}$ rather than $y_n W^{(o)\top}$, despite computing $y_n = \text{groupnorm}(y_g)$ on the preceding line. This appears to be a typo in the paper; the output should logically use $y_n$.]

[p. 26] Only the input projection matrices and the output projection matrices need to be split, and only one all-reduce is needed at the end of the block. This is similar to the design of TP for attention and MLP layers. In particular, if TP degree is 2, $W^{(x)} = [W_1^{(x)}, W_2^{(x)}]$ with $W_i^{(x)} \in \mathbb{R}^{d \times ed/2}$, $W^{(z)} = [W_1^{(z)}, W_2^{(z)}]$ with $W_i^{(z)} \in \mathbb{R}^{d \times ed/2}$,

[p. 27] and $W^{(o)} = \begin{bmatrix} W_1^{(o)} \\ W_2^{(o)} \end{bmatrix}$ with $W_i^{(o)} \in \mathbb{R}^{ed/2 \times d}$. For $i = 1, 2$, the TP Mamba-2 layer can be written as:

$$x^{(i)} = u W_i^{(x)\top} \in \mathbb{R}^{L \times ed/2}$$
$$z^{(i)} = u W_i^{(z)\top} \in \mathbb{R}^{L \times ed/2}$$
$$\Delta^{(i)}, B^{(i)}, C^{(i)} = \text{projection}(u) \quad \text{(one or more groups of } \Delta, B, C \text{ per GPU)}$$
$$x_c^{(i)} = \text{conv1d}(x^{(i)}) \in \mathbb{R}^{L \times ed/2}$$
$$y^{(i)} = SSM_{A,B,C,\Delta}(x_c^{(i)}) \in \mathbb{R}^{L \times ed/2}$$
$$y_g^{(i)} = y^{(i)} \cdot \phi(z^{(i)})$$
$$y_n^{(i)} = \text{groupnorm}(y_g^{(i)}) \quad \text{(number of groups divisible by degree of tensor parallel)}$$
$$\text{out}^{(i)} = y_g^{(i)} W_i^{(o)\top} \in \mathbb{R}^{L \times d/2}$$
$$\text{out} = \sum_i \text{out}^{(i)}. \quad \text{(summing outputs from all GPUs with an all-reduce)}$$

**Figure 7** (p. 27): "(**Parallelism with the Mamba-2 Block.**) (*Left*: **Tensor Parallelism**) We split the input projection matrices $W^{(x)}, W^{(z)}$ and the output projection matrix $W^{(o)}$. Each SSM head $(A, B, C, X) \mapsto Y$ lives on a single device. Choosing GroupNorm for the final normalization layer avoids extra communication. We need one all-reduce per layer, just like the MLP or attention blocks in a Transformer. (*Right*: **Sequence/Context Parallelism**) Analogous to the SSD algorithm, with multiple devices, we can split along the sequence dimension. Each device computes the state of its sequence, then pass that state to the next GPU."

The figure shows two diagrams side by side:
- **Left (Tensor Parallelism):** Two GPUs each hold a partition of the input projection weights ($W_1^{(x)}, W_1^{(z)}$ and $W_2^{(x)}, W_2^{(z)}$) and output projection weights ($W_1^{(o)}, W_2^{(o)}$). The layer input is broadcast to both GPUs. Each GPU computes its partition of the SSM (with its own $A, B, C$ groups) and applies GroupNorm. The outputs are summed via an all-reduce at the top.
- **Right (Sequence/Context Parallelism):** Three GPUs (GPU1, GPU2, GPU3) each hold a chunk of the input sequence $X$. Each GPU computes its local states $H$ and outputs $Y$. States are passed sequentially from one GPU to the next (GPU1 $\to$ GPU2 $\to$ GPU3), analogous to the block decomposition in the SSD algorithm (Figure 5).

## 8.2 Sequence Parallelism

[p. 27] For very long sequences, it may be necessary to split the input and activation to different GPUs along the sequence length dimension. There are two main techniques:

1. **Sequence parallelism (SP) for residual and normalization operations:** first proposed by Korthikanti et al. (2023), this technique decomposes the all-reduce in TP as reduce-scatter and all-gather. Noticing that the residual and normalization operations are repeated on the same input for all GPUs in the same TP group, SP splits the activations along the sequence length dimension by performing: reduce-scatter, residual and normalization, then all-gather.

   Since the Mamba-2 architecture uses the same residual and normalization structure, SP applies without modification.

2. **Sequence parallelism for the token-mixing operations (attention or SSM),** also known as "context parallelism" (CP). Several techniques have been developed for attention layer (e.g., Ring attention (Liu, Yan, et al. 2024; Liu, Zaharia,

---
[p. 28 continued]

   and Abbeel 2023)), with sophisticated load-balancing technique (Brandon et al. 2023). The difficulty with sequence parallelism in attention is that queries and keys can be split into blocks, but each query block needs to interact with key blocks, leading to communication bandwidth quadratic in the number of workers.

   With SSMs, the sequence can be split in a simple manner: each worker takes an initial state, computes the SSM with respect to its inputs, returns the final state, and passes that final state to the next worker. The communication bandwidth is linear in the number of workers. This decomposition is exactly the same as the block-decomposition in the SSD algorithm (Figure 5) to split into blocks / chunks. Context parallelism with Mamba-2 is illustrated in Figure 7 (*Right*).

## 8.3 Variable Length

[p. 28] While pretraining often uses the same sequence lengths for the batch, during finetuning or inference, the model might need to process different input sequences of different lengths. One naive way to handle this case is to right-pad all sequences in the batch to the maximum length, but this can be inefficient if sequences are wildly different lengths. For transformers, sophisticated techniques have been developed to avoid padding and do load-balancing between GPUs (Zeng et al. 2022; Y. Zhai et al. 2023), or packing multiple sequences in the same batch and adjusting the attention mask (Ding et al. 2024; Pouransari et al. 2024). With SSMs and Mamba in particular, variable sequence lengths can be handled by simply treating the whole batch as one long sequence, and avoiding passing the states between individual sequences. This is equivalent to simply setting $A_t = 0$ for tokens $t$ at the end of one sequence to prevent it from passing information to the token $t + 1$, which belongs to a different sequence.
