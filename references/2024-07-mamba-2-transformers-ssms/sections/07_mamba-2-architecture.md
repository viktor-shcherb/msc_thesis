# 7 The Mamba-2 Architecture [p. 22-25]

[p. 22] By connecting SSMs and attention, the SSD framework allows the development of a shared vocabulary and library of techniques for both. This section discusses several examples of understanding and modifying SSD layers using ideas originally developed for Transformers, resulting in the Mamba-2 architecture. These axes of variation are ablated in Section 9.4.

## 7.1 Block Design

[p. 23] This subsection discusses modifications to the neural network block that are independent of the inner sequence mixing layer (i.e. outside the core SSD layer).

**Parallel Parameter Projections.** Mamba-1 was motivated by an SSM-centric point of view where the selective SSM layer is viewed as a map from $X \mapsto Y$. The SSM parameters $A, B, C$ are viewed as subsidiary and are functions of the SSM input $X$. Thus the linear projections defining ($A, B, C$) occur after the initial linear projection to create $X$.

In Mamba-2, the SSD layer is viewed as a map from $A, X, B, C \mapsto Y$. It therefore makes sense to produce $A, X, B, C$ in parallel with a single projection at the beginning of the block. Note the analogy to standard attention architectures, where $X, B, C$ correspond to the $Q, K, V$ projections that are created in parallel.

Note that adopting parallel projections for the $A, B, C, X$ inputs to the SSM slightly reduces parameters and more importantly is more amenable to tensor parallelism for larger models, by using standard Megatron sharding patterns (Shoeybi et al. 2019).

**Extra Normalization.** In preliminary experiments, instabilities were prone to arising in larger models. This was alleviated by adding an extra normalization layer (e.g. LayerNorm, GroupNorm, or RMSNorm) to the block right before the final output projection. This usage of normalization is most directly related to the NormFormer architecture (Shleifer, Weston, and Ott 2021), which also added normalization layers at the end of the MLP and MHA blocks.

This change is similar to other recent models related to Mamba-2 that were derived from a linear attention viewpoint. The original linear attention formulation normalizes by a denominator term that emulates the normalization of the softmax function in standard attention. TransNormerLLM (Qin, Dong Li, et al. 2023) and RetNet (Y. Sun et al. 2023) find that this normalization is unstable and add an extra LayerNorm or GroupNorm after the linear attention layer. The extra normalization layer in Mamba-2 differs slightly from these, occurring after the multiplicative gate branch instead of before. [p. 23]

**Figure 6** (p. 23): "(**Mamba-2 Architecture.**) The Mamba-2 block simplifies the Mamba block by removing sequential linear projections; the SSM parameters $A, B, C$ are produced at the beginning of the block instead of as a function of the SSM input $X$. An additional normalization layer is added as in NormFormer (Shleifer, Weston, and Ott 2021), improving stability. The $B$ and $C$ projections only have a single head shared across the $X$ heads, analogous to multi-value attention (MVA)."

The figure shows two block diagrams side by side:
- **Sequential Mamba Block** (left): Input flows up through Conv, then a nonlinearity gate $\sigma$. The SSM block receives $X$ as input and produces $A, X, B, C$ sequentially (with $A, B, C$ derived from $X$). Output $Y$ is produced from the SSM. A separate gate branch $\sigma$ merges with the output.
- **Parallel Mamba Block** (right): Input flows up through Conv, then the SSM block receives $A, X, B, C$ in parallel (all projected at the beginning). An additional normalization node $N$ is placed after the gating and before the output projection. A separate gate branch $\sigma$ merges with the output.

Legend:
- Rectangular boxes = Linear projection
- Rounded boxes = Sequence transformation
- Circles = Nonlinearity (activation, normalization, multiplication)

## 7.2 Multihead Patterns for Sequence Transformations

[p. 24] Recall that SSMs are defined as a sequence transformation (Definition 2.1) where:
- $A, B, C$ parameters have a state dimension N.
- They define a sequence transformation $\mathbb{R}^\mathsf{T} \to \mathbb{R}^\mathsf{T}$, which for example can be represented as a matrix $M \in \mathbb{R}^{(\mathsf{T},\mathsf{T})}$.
- This transformation operates over an input sequence $X \in \mathbb{R}^{(\mathsf{T},\mathsf{P})}$, independently over the P axis.

One can view this as defining one *head* of the sequence transformation.

**Definition 7.1** (Multihead patterns). *A multihead sequence transformation consists of* H *independent heads, for a total model dimension of* D = d_model. *The parameters may be tied across heads, leading to a **head pattern**.* [p. 24]

The state size N and head dimension P are analogous to the $QK$ head dimension and $V$ head dimension of attention, respectively. Just as in modern Transformer architectures (Chowdhery et al. 2023; Touvron, Lavril, et al. 2023), in Mamba-2 these are generally chosen to be constants around 64 or 128; when the model dimension D increases, the number of heads is increased while keeping the head dimensions N and P fixed. In order to describe how to do this, ideas from multihead attention are transferred and generalized to define similar patterns for SSMs, or any general sequence transformation.

### Multi-head SSM (MHS) / Multi-head Attention (MHA) Pattern

| Parameter | Shape       | Equation |
|-----------|-------------|----------|
| $X$       | (T, H, P)  | (17)     |
| $A$       | (T, H)     |          |
| $B$       | (T, H, N)  |          |
| $C$       | (T, H, N)  |          |

[p. 24] The classic MHA pattern assumes that the head dimension P divides the model dimension D. The number of heads is defined as $\mathsf{H} = \mathsf{D}/\mathsf{P}$. Then, H copies of the core sequence transformation are created by creating H independent copies of each parameter. Note that while the MHA pattern was first described for the attention sequence transformation, it can be applied to anything compatible with Definition 2.1. For example, a multi-head SSD layer would accept inputs with shapes according to equation (17) where the SSD algorithm is broadcasted over the $\mathsf{H}$ = n_heads dimension.

### Multi-contract SSM (MCS) / Multi-query Attention (MQA) Pattern

| Parameter | Shape       | Equation |
|-----------|-------------|----------|
| $X$       | (T, 1, P)  | (18)     |
| $A$       | (T, H)     |          |
| $B$       | (T, 1, N)  |          |
| $C$       | (T, H, N)  |          |

[p. 24] Multi-query attention (Shazeer 2019) is a clever optimization for attention that can dramatically improve the speed of autoregressive inference, which relies on caching the $K$ and $V$ tensors. This technique simply avoids giving $K$ and $V$ the extra head dimension, or in other words broadcasts a single head of ($K, V$) across all the heads of $Q$.

Using the state space duality, an equivalent SSM version of MQA is defined as equation (18). Here, $X$ and $B$ (the SSM analogs of attention's $V$ and $K$) are shared across the H heads. This is called the *multi-contract SSM (MCS)* head pattern, because the $C$ parameter which controls the SSM state contraction has independent copies per head.

A multi-key attention (MKA) or *multi-expand SSM (MES)* head pattern is similarly defined, where $B$ (which controls the SSM expansion) is independent per head while $C$ and $X$ are shared across heads.

### Multi-expand SSM (MES) / Multi-key Attention (MKA) Pattern

| Parameter | Shape       | Equation |
|-----------|-------------|----------|
| $X$       | (T, 1, P)  | (19)     |
| $A$       | (T, H)     |          |
| $B$       | (T, H, N)  |          |
| $C$       | (T, 1, N)  |          |

### Multi-input SSM (MIS) / Multi-value Attention (MVA) Pattern

| Parameter | Shape       | Equation |
|-----------|-------------|----------|
| $X$       | (T, H, P)  | (20)     |
| $A$       | (T, H)     |          |
| $B$       | (T, 1, N)  |          |
| $C$       | (T, 1, N)  |          |

[p. 24] While MQA makes sense for attention because of its KV cache, it is not the natural choice for SSMs. In Mamba, instead, $X$ is viewed as the main input to the SSM, and therefore $B$ and $C$ are parameters that are shared across the input channels. A new multi-value attention (MVA) or *multi-input SSM (MIS)* pattern is defined in equation (20), which can again be applied to any sequence transformation such as SSD.

**Proposition 7.2.** *The selective SSM (S6) layer of the Mamba architecture (Gu and Dao 2023) can be viewed as having*

- *Head dimension $\mathsf{P} = 1$: every channel has independent SSM dynamics $A$.*
- *Multi-input SSM (MIS) or multi-value attention (MVA) head structure: the $B, C$ matrices (corresponding to $K, Q$ in the attention duality) are shared across all channels of the input $X$ (corresponding to $V$ in attention).* [p. 24-25]

[p. 25] These head pattern variants can be ablated when applied to SSD (Section 9.4.3). Interestingly, despite being controlled in parameter counts and total state dimension, there is a noticeable difference in downstream performance. The authors empirically find that the MVA pattern as originally used in Mamba performs best.

### Grouped Head Patterns

[p. 25] The ideas of multi-query attention can be extended to *grouped-query attention* (Ainslie et al. 2023): instead of 1 K and V head, one can create G independent K and V heads, where $1 < \mathsf{G}$ and G divides H. This is motivated both by bridging the performance difference between multi-query and multi-head attention, and enabling more efficient tensor parallelism by setting G to be a multiple of the number of shards (Section 8).

Similarly, the multi-input SSM head pattern used in Mamba-2 can be easily extended to **grouped-input SSM (GIS)**, or synonymously **grouped-value attention (GVA)**. The generalization is straightforward and the details are omitted for simplicity.

## 7.3 Other SSD Extensions from Linear Attention

[p. 25] This subsection describes an example of architectural modifications to SSD motivated by linear attention. These are ablated in Section 9.4.3 as a form of negative result, finding that they do not significantly improve performance enough to adopt them as default settings. Nonetheless, these illustrate how the vast literature on attention can be incorporated to define variants of SSD. The choice of kernel feature map is treated as a hyperparameter in the Mamba-2 architecture, and other simple modifications inspired by attention are expected to be possible as well.

**Kernel Attention Approximations to Softmax Attention.** Many variants of linear attention or kernel attention are motivated by viewing the attention scores $\text{softmax}(QK^\top)$ as composed of

1. An exponential kernel $Z = \exp(QK^\top)$, which can be approximated by $Z = \psi(Q)\psi(K)^\top$ for some kernel feature map.
2. Normalizing the kernel so that rows sum to 1 via $M = G / G\mathbf{1}\mathbf{1}^\top$, where the division happens elementwise and $\mathbf{1}$ is the all 1's vector.

**Exponential Kernel Feature Maps.** In Mamba-2, a flexible kernel feature map is incorporated and applied to the $B$ and $C$ branches (corresponding to the $K$ and $V$ branches in attention). The feature map can also be optionally applied to the $X$ ($V$) branch, for simplicity and symmetry. This is represented in Figure 6 by an arbitrary nonlinearity. By default, $\psi$ is chosen to be an elementwise Swish / SiLU function (Hendrycks and Gimpel 2016; Ramachandran, Zoph, and Le 2017). Other options are explored in the ablations in Section 9.4.3, including feature maps used by Linear Attention, Performer, Random Feature Attention, and cosFormer (Section 4.1.3). [p. 25]

**Incorporating a Normalization (Denominator) Term.** To find the denominator term, one simply has to compute $M\mathbf{1}$. But recall that the final output of the model is just $Y = MX$ (equation (16)). So the normalization terms can be found simply by augmenting $X$ with an extra column $\mathbf{1}$, resulting in a tensor of shape $(\mathsf{T}, \mathsf{P} + 1)$.

Note that in this case, the kernel feature map $\psi$ must be positive so that the sum is positive. [p. 25]
