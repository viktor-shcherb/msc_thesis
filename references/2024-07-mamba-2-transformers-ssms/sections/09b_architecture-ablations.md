# 9.4 Architecture Ablations [p. 32–33]

## 9.4.1 Block Design

[p. 32] Section 7.1 introduces the Mamba-2 block, which has small modifications to the Mamba-1 block that are partly motivated by the connection to attention and also to improve the scalability of Mamba-2. Table 4 ablates these architecture changes to the block, which occur outside of the core SSM layer.

The ablations validate that parallel projections to create $(A, B, C, X)$ saves parameters and performs slightly better than Mamba's sequential projections. More importantly, this modification is amenable to tensor parallelism at larger model sizes (Section 8). Additionally, the extra normalization layer also slightly improves performance. More importantly, preliminary experiments at larger scales observed that it also helps with training stability.

**Table 4** (p. 32): "(**Ablations: Mamba-2 block.**) We ablate the major differences between the Mamba-2 and Mamba-1 neural network blocks (Figure 6, Section 7.1). Note that these components are independent of the inner sequence mixing layer; in these ablations, we use SSD for the inner SSM layer (differing from the S6 layer of Mamba-1)."

| Block | *ABCX* Projections | Extra Normalization | Parameters | Perplexity |
|---|---|---|---|---|
| Mamba-1 | Sequential | X | 129.3M | 11.76 |
|  | Sequential | checkmark | 129.3M | 11.54 |
|  | Parallel | X | 126.5M | 11.66 |
| Mamba-2 | Parallel | checkmark | 126.5M | 11.49 |

Mamba-2 block (parallel projections + extra normalization) achieves the lowest perplexity (11.49) with fewer parameters (126.5M vs 129.3M).

## 9.4.2 Head Structure

[p. 32] Section 7.2 describes how the dimensions of the $B, C, X$ projections can be viewed as a hyperparameter analogous to notions of multi-head attention and multi-query attention. The authors also showed how the original Mamba architecture is analogous to multi-value attention (Proposition 7.2), which was a choice that naturally developed from the state-space model point of view and was not previously ablated.

Table 5 ablates choices of the multi-head structure for the Mamba-2 architecture. Strikingly, the authors find a large difference between multi-value and multi-query or multi-key head patterns, despite seeming very similar. This is not explained by the total state size, which is the same for all of them (equal to HPN or the product of the number of heads, head dimension, and state dimension).

The authors also compare to multi-head patterns where the number of $C, B, X$ (analogous to $Q, K, V$) heads is equal. They compare against the standard multi-head pattern, as well as one with aggressive sharing where they all have only 1 head. In the latter case, the model still has H different sequence mixers $M$, because each head still has a different $A$. When parameter matched, these multi-head patterns perform similarly to each other, in between the MVA and MQA/MKA patterns.

**Table 5** (p. 33): "(**Ablations: Multi-head structure.**) All models have state expansion factor $N = 64$ and head size $P = 64$ and are trained to Chinchilla scaling law token counts. The number of $A$ heads is always equal to the total heads H, i.e. each head has a separate input-dependent $A$ decay factor. (*Top*) 125M models, 2.5B tokens (*Bottom*) 360M models, 7B tokens"

| SSM Head Pattern | Attn. Analog | A heads | B heads | C heads | X heads | Layers | Params | Ppl. |
|---|---|---|---|---|---|---|---|---|
| Multi-input (MIS) | Multi-value (MVA) | 24 | 1 | 1 | 24 | 24 | 126.5M | **11.66** |
| Multi-contract (MCS) | Multi-query (MQA) | 24 | 1 | 24 | 1 | 24 | 126.5M | 12.62 |
| Multi-expand (MES) | Multi-key (MKA) | 24 | 24 | 1 | 1 | 24 | 126.5M | 12.59 |
| Multi-head (MHS) | Multi-head (MHA) | 24 | 24 | 24 | 24 | 15 | 127.6M | 12.06 |
| Multi-state (MSS) | - | 24 | 1 | 1 | 1 | 36 | 129.6M | 12.00 |
| Multi-input (MIS) | Multi-value (MVA) | 32 | 1 | 1 | 32 | 48 | 361.8M | **8.73** |
| Multi-contract (MCS) | Multi-query (MQA) | 32 | 1 | 32 | 1 | 48 | 361.8M | 9.33 |
| Multi-expand (MES) | Multi-key (MKA) | 32 | 32 | 1 | 1 | 48 | 361.8M | 9.36 |
| Multi-head (MHS) | Multi-head (MHA) | 32 | 1 | 1 | 1 | 70 | 361.3M | 9.01 |
| Multi-state (MSS) | - | 32 | 32 | 32 | 32 | 29 | 357.3M | 9.04 |

Multi-input/multi-value (MIS/MVA) achieves the best perplexity at both model sizes (11.66 at 125M, 8.73 at 360M), matching the original Mamba design choice.

## 9.4.3 Attention Kernel Approximations

[p. 32–33] Section 7.3 noted how SSD can be combined with ideas from the linear attention literature, such as various forms of kernel approximations. The authors ablate several variants of these suggested by previous works in Table 6. These include the cosFormer (Qin, Weixuan Sun, et al. 2022), Random Feature Attention H. Peng et al. 2021, and Positive Random Features (Performer) (Choromanski et al. 2021).

The authors also ablate adding a normalization term, akin to the denominator of the softmax function in standard attention. They found that this introduced instabilities to most variants, but slightly improved performance for the ReLU activation function $\psi$.

**Table 6** (p. 33): "(**Ablations: Kernel approximations.**) We test various proposals for the kernel activation function $\psi$, including linear attention variants aiming to approximate the exp kernel from standard softmax attention."

| Kernel activation $\varphi$ | Perplexity |
|---|---|
| none | 11.58 |
| Swish | 11.66 |
| Exp | 11.62 |
| ReLU | 11.73 |
| ReLU + normalization | 11.64 |
| cosFormer | 11.97 |
| Random Feature Attention | 11.57 |
| Positive Random Features (Performer) | 12.21 |

Table 7 also tests more recent proposals to improve linear attention that involve expanding the feature dimension (Based (Arora, Eyuboglu, Zhang, et al. 2024) and ReBased (Aksenov et al. 2024)). These linear attention extensions aim to appropriate the exp kernel with a quadratic approximation. ReBased also proposes to replace the QK activation function with a layer normalization; from an SSM-centric view, the authors apply a normalization on top of $(B, C)$ before applying the SSM function.

**Table 7** (p. 33): "(**Ablations: Kernel approximations.**) We test the (Re)Based methods for linear attention approximations, which involve expanded feature maps. (*Top*) 130M models. (*Bottom*) 380M models with $N = 256$."

| Kernel activation $\varphi$ | Perplexity |
|---|---|
| Swish | 11.67 |
| Swish + Taylor (Based) | 12.19 |
| LayerNorm | 11.50 |
| LayerNorm + Square (ReBased) | 11.84 |
| Swish | 8.58 |
| Swish + Taylor (Based) | 8.71 |
| LayerNorm | 8.61 |
| LayerNorm + Square (ReBased) | 8.63 |

The authors note that this technique has been independently proposed as the "QK-Norm" for softmax attention (Team 2024) and an "internal normalization" for Mamba (Lieber et al. 2024).

Overall, Table 6 and Table 7 found that the kernel approximation methods did not seem to improve over simple pointwise non-linear activation functions for $\psi$. The default settings for Mamba-2 use $\psi(x) = \text{Swish}(x)$ to follow Mamba-1, but the authors suggest that removing this activation entirely may be a simpler choice that they did not extensively test.

The authors emphasize that SSD and vanilla linear attention differ in the inclusion of the 1-semiseparable mask $L$, while the various linear attention methods in the literature were derived to approximate softmax attention without this term; thus, the negative results may be not unexpected.
