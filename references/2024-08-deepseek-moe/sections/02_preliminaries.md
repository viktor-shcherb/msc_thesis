# 2. Preliminaries: Mixture-of-Experts for Transformers [p. 4-5]

## Standard Transformer Block

[p. 4] A standard Transformer language model is constructed by stacking $L$ layers of standard Transformer blocks, where each block can be represented as follows:

$$\mathbf{u}_{1:T}^l = \text{Self-Att}\left(\mathbf{h}_{1:T}^{l-1}\right) + \mathbf{h}_{1:T}^{l-1}, \tag{1}$$

The output of the self-attention module added to the input (residual connection).

$$\mathbf{h}_t^l = \text{FFN}\left(\mathbf{u}_t^l\right) + \mathbf{u}_t^l, \tag{2}$$

The output of the FFN added to the attention output (residual connection).

Where:
- $T$ denotes the sequence length
- $\text{Self-Att}(\cdot)$ denotes the self-attention module
- $\text{FFN}(\cdot)$ denotes the Feed-Forward Network
- $\mathbf{u}_{1:T}^l \in \mathbb{R}^{T \times d}$ are the hidden states of all tokens after the $l$-th attention module
- $\mathbf{h}_t^l \in \mathbb{R}^d$ is the output hidden state of the $t$-th token after the $l$-th Transformer block

Layer normalization is omitted for brevity.

## MoE Layer Formulation

[p. 4] A typical practice to construct an MoE language model usually substitutes FFNs in a Transformer with MoE layers at specified intervals (Du et al., 2022; Fedus et al., 2021; Lepikhin et al., 2021; Zoph, 2022). An MoE layer is composed of multiple experts, where each expert is structurally identical to a standard FFN. Each token will be assigned to one (Fedus et al., 2021) or two (Lepikhin et al., 2021) experts.

If the $l$-th FFN is substituted with an MoE layer, the computation for its output hidden state $\mathbf{h}_t^l$ is expressed as:

$$\mathbf{h}_t^l = \sum_{i=1}^{N} \left(g_{i,t} \, \text{FFN}_i\left(\mathbf{u}_t^l\right)\right) + \mathbf{u}_t^l, \tag{3}$$

Weighted sum of expert outputs plus residual connection.

$$g_{i,t} = \begin{cases} s_{i,t}, & s_{i,t} \in \text{Topk}(\{s_{j,t} | 1 \leqslant j \leqslant N\}, K), \\ 0, & \text{otherwise}, \end{cases} \tag{4}$$

Gate value: retains the affinity score if it is among the top-$K$, otherwise zero.

$$s_{i,t} = \text{Softmax}_i\left(\mathbf{u}_t^{l^T} \mathbf{e}_i^l\right), \tag{5}$$

Token-to-expert affinity score, computed as softmax over the dot product of the token hidden state and expert centroid.

Where:
- $N$ denotes the total number of experts
- $\text{FFN}_i(\cdot)$ is the $i$-th expert FFN
- $g_{i,t}$ denotes the gate value for the $i$-th expert
- $s_{i,t}$ denotes the token-to-expert affinity
- $\text{Topk}(\cdot, K)$ denotes the set comprising $K$ highest affinity scores among those calculated for the $t$-th token and all $N$ experts
- $\mathbf{e}_i^l$ is the centroid of the $i$-th expert in the $l$-th layer

[p. 4] Note that $g_{i,t}$ is sparse, indicating that only $K$ out of $N$ gate values are nonzero. This sparsity property ensures computational efficiency within an MoE layer, i.e., each token will be assigned to and computed in only $K$ experts. Layer normalization is also omitted for brevity.
