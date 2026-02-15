# Effects of model architecture $p_\theta$ on attention sink [p. 7-10]

[p. 7]

In this section, we mainly explore the effects of positional embedding, pre-norm or post-norm structure, and attention design on the emergence of attention sink. In Appendix D, we also show that varying activation functions in the FFN, multi-head design do not affect the emergence of attention sink [p. 7].

## 7.1 Positional embedding [p. 7-8]

[p. 7-8]

Attention sink always appears on the first token, which motivates us to explore where such a position property is brought by positional embedding (PE). Therefore, we attempt to replace the original Rotary with other PEs, as shown in Table 3. We differentiate these PEs through the calculations of the hidden states $\boldsymbol{H}^0$ before the first transformer block and the dot product between queries and keys $\langle \boldsymbol{q}_i, \boldsymbol{k}_j \rangle$. The detailed formulations are delayed to Appendix B. From the same Table, we observe that only the model with relative PE is difficult to train while other models have comparable performance under our setup. Then we note that all these LMs, even the one without explicit PE (NoPE), have attention sink [p. 8].

**Table 3:** Positional embedding does not affect the emergence of attention sink [p. 8].

| PE | $\boldsymbol{H}^0$ | $\langle \boldsymbol{q}_i, \boldsymbol{k}_j \rangle$ | Sink₁(%) | valid loss |
|---|---|---|---|---|
| NoPE | $\boldsymbol{XW}_E$ | $\boldsymbol{q}_i \boldsymbol{k}_j^\top$ | 20.35 | 3.81 |
| Absolute PE | $\boldsymbol{XW}_E + P_{\text{abs}}$ | $\boldsymbol{q}_i \boldsymbol{k}_j^\top$ | 32.73 | 3.74 |
| Learnable PE | $\boldsymbol{XW}_E + P_{\text{learnable}}$ | $\boldsymbol{q}_i \boldsymbol{k}_j^\top$ | 33.13 | 3.79 |
| Relative PE | $\boldsymbol{XW}_E$ | $\boldsymbol{q}_i \boldsymbol{k}_j^\top + q_{\text{relative}}(i-j)$ | 35.53 | 5.45 |
| ALiBi | $\boldsymbol{XW}_E$ | $\boldsymbol{q}_i \boldsymbol{k}_j^\top + q_{\text{alibi}}(i-j)$ | 20.78 | 3.71 |
| Rotary | $\boldsymbol{XW}_E$ | $\boldsymbol{q}_i \boldsymbol{R}_{\theta,i-j} \boldsymbol{k}_j^\top$ | 18.18 | 3.73 |

**Figure 7** (p. 8): Caption: "$\ell_2$-norm ratio of $h_1^l$ and mean of $h_{l\neq 1}^l$. (*Left*) Massive activations exist not in hidden states in post-norm LMs, but in the features before LN. (*Middle*) LMs with KV biases or K biases have no massive activations, while LMs with a learnable sink token or V biases have massive activations. (*Right*) Massive activations emerge when increasing $\ell_2$-norm of $v^{s,l,h}$ for specific K biases"

Description: Three panels showing analysis of hidden state norms and attention biases
- Left: Line plot showing $\ell_2$-norm ratio across transformer blocks (0-10) for three conditions: "Pre-norm" (stays around 20), "Post-norm, before LN" (peaks around 80 at block 5-6), "Post-norm, after LN" (stays around 10). Shows massive activations exist before LN in post-norm models
- Middle: Line plot showing mean of $h_{l\neq 1}^l$ across blocks under different attention bias configurations (Default, K biases with various settings, V biases). Most configurations show similar patterns (~60-20 declining), except learnable sink token and certain V bias settings which show different behavior
- Right: Line plot showing fixed V biases with different $\ell_2$ norms ($v^{s,l,h} = 0$, $v'$, $5v'$, $20v'$). Higher norms lead to higher activation values, with $20v'$ reaching ~15 while $v^{s,l,h} = 0$ stays near 0
- Supports claim: Attention biases affect where massive activations appear in the model

## 7.2 Pre-norm and post-norm structure [p. 8]

[p. 8]

Layer normalization (LN) (Ba et al., 2016; Zhang & Sennrich, 2019) regularizes the hidden states in LMs by re-centering and re-scaling, which may alleviate the massive activations. This motivates us to explore the effects of LN location on attention sink. In the pre-norm structure, as stated in Equation 2, hidden states from the earlier layers are retained through residual connections (He et al., 2016). Therefore, if massive activations appear in a specific block, they will likely be retained in the subsequent blocks. Since they are present in post-norm LMs, the hidden states will be normalized before being fed into the following blocks, as present in Figure 1(*Left*) [p. 8].

When replacing the pre-norm structure with the post-norm structure, Sink₁ becomes 13.54%. This indicates that the attention sink still exists in post-norm LMs. After further investigations, as visualized in Figure 7(*Left*), massive activations exist in the hidden states before the post LN instead of $h_1^l$ [p. 8].

## 7.3 Attention biases [p. 8-9]

[p. 8-9]

### Learnable biases in attention [p. 8]

In Section 3.1, we have shown that the first token acts as a bias: its key $\boldsymbol{k}_1^{l,h}$ is distributed in a different manifold and its value $\boldsymbol{v}_1^{l,h}$ has small $\ell_2$ norm. Xiao et al. (2023b) considered a learnable sink token in each chunk before the input tokens during LM pre-training. As this token is fixed in the first token, this work considered it as introducing learnable biases $\boldsymbol{k}^{s,l,h}$, $\boldsymbol{v}^{s,l,h}$ in attention, as shown in the second row in Table 4. These biases are the MLP output of $x_s \cdot \boldsymbol{W}_E$. Sun et al. (2024) directly introduced learnable parameters in attention (*KV biases*). They found that this design could alleviate the massive activations. Considering the important role of $\boldsymbol{k}^{s,l,h}$ and small $\ell_2$-norm of $\boldsymbol{v}^{s,l,h}$, we consider only key biases $\boldsymbol{k}^{s,l,h}$ and fix value biases $\boldsymbol{v}^{s,l,h} = \boldsymbol{0}$ (*K biases*). As a control, we also consider only adding value biases (*V biases*). The formulations of all these attention designs are shown in Table 4 [p. 8-9].

### LMs need key biases [p. 8-9]

After evaluating the above LMs with setups in Table 4, we first observe that these LMs have comparable model performance. Moreover, as long as there are key biases $\boldsymbol{k}^{s,l,h}$, attention sink disappears on the first token but on the biases. From the setup of K biases, we reaffirm that the sink token acts as key biases, storing extra attention scores, which could be completely non-informative and not contribute to the value computation. It is worth mentioning that the introduced learnable sink token, KV biases, and V biases become part of model parameters in LMs. Removing them will lead to no attention sink in the first position, but a significant drop in model [p. 9].

**Table 4:** With comparable performance, LMs with sink token, KV biases, and K biases could shift attention sink from the first token to key biases' position. Value biases cannot affect attention sink [p. 9].

| Attention in each head | Sink₁*(%) | Sink₁(%) | valid loss |
|---|---|---|---|
| Softmax($\frac{1}{\sqrt{d_h}} \boldsymbol{Q}^{l,h} \boldsymbol{K}^{l,h\top} + \boldsymbol{M}$) $\boldsymbol{V}^{l,h}$ | - | 18.18 | 3.73 |
| Softmax($\frac{1}{\sqrt{d_h}}[\boldsymbol{Q}^{l,h}][\boldsymbol{k}^{s,l,h\top} \quad \boldsymbol{K}^{l,h\top}] + \boldsymbol{M}$) $[\boldsymbol{v}^{s,l,h}; \boldsymbol{V}^{l,h}]$ | 74.12 | 0.00 | 3.72 |
| Softmax($\frac{1}{\sqrt{d_h}} \boldsymbol{Q}^{l,h}[\boldsymbol{k}^{s,l,h\top} \quad \boldsymbol{K}^{l,h\top}] + \boldsymbol{M}$) $[\boldsymbol{v}^{s,l,h}; \boldsymbol{V}^{l,h}]$ | 72.76 | 0.04 | 3.72 |
| Softmax($\frac{1}{\sqrt{d_h}} \boldsymbol{Q}^{l,h}[\boldsymbol{k}^{s,l,h\top} \quad \boldsymbol{K}^{l,h\top}] + \boldsymbol{M}$) $[\boldsymbol{0}; \boldsymbol{V}^{l,h}]$ | 73.34 | 0.00 | 3.72 |
| Softmax($\frac{1}{\sqrt{d_h}} \boldsymbol{Q}^{l,h} \boldsymbol{K}^{l,h\top} + \boldsymbol{M}$) $\boldsymbol{V}^{l,h} + \boldsymbol{v}^{s,l,h}$ | - | 17.53 | 3.73 |

Note: Sink₁* refers to attention sink on the biases position (learnable token or bias parameters).

**Table 5:** Larger $\ell_2$-norm of fixed $\boldsymbol{v}^{s,l,h}$ results in LMs allocating more attention on $x_1$ instead of $\boldsymbol{k}^{s,l,h}$ [p. 9].

| $\boldsymbol{v}^{s,l,h}$ | $\boldsymbol{0}$ | $v'$ | $5v'$ | $20v'$ | $v''$ | $5v''$ | $20v''$ |
|---|---|---|---|---|---|---|---|
| Sink₁*(%) | 73.34 | 70.03 | 44.43 | 1.51 | 69.74 | 27.99 | 0.00 |
| Sink₁(%) | 0.00 | 0.06 | 3.71 | 25.88 | 2.15 | 5.93 | 11.21 |
| valid loss | 3.72 | 3.72 | 3.72 | 3.71 | 3.72 | 3.72 | 3.73 |

### Beyond all zeros in V biases [p. 9]

In the setup of K biases, we fix $\boldsymbol{v}^{s,l,h} = \boldsymbol{0}$. We wonder whether the fixed values of $\boldsymbol{v}^{s,l,h}$ could affect the attention sink. We consider $\boldsymbol{v}^{s,l,h} = mv'$ or $\boldsymbol{v}^{s,l,h} = mv''$, where $m$ is the controllable $\ell_2$ norm and $v' = [1, 0, 0, .., 0]$ and $v'' = [1, 1, 1, .., 1]/\sqrt{d_h}$. As shown in Table 5, with larger $\ell_2$-norm of $\boldsymbol{v}^{s,l,h}$, attention sink shifts from $\boldsymbol{k}^{s,l,h}$ to the first token. Intuitively, it is difficult for LMs to remove the effects of $\boldsymbol{v}^{s,l,h}$ with larger $\ell_2$-norm in model predictions. Then they opt to optimize the keys and values of the first token to save extra attention [p. 9].

### Design space of biases [p. 9]

In Table 12(*Right*), the LM with head-sharing KV biases tends to shift the sink from $\boldsymbol{k}^{s,l,h}$ back to the first token. While the one with head-sharing K biases is less affected. In Table 13, even with small learnable dimensions for key biases, they can still absorb large attention [p. 9].

## 7.4 Attention operation [p. 9-10]

[p. 9-10]

### General formulation of attention [p. 9]

In the last section, we realize that LMs need key biases to save extra attention. This motivates us to investigate such a property is related to the dependence among attention scores due to the softmax operation. First, the attention output for the $i$-th token can be generalized as:

$$\boldsymbol{v}_i^l = \left(\sum_{j'=1}^{i} \text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_{j'}))\right)^{-1} \sum_{j=1}^{i} \text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_j))\boldsymbol{v}_j =$$

$$\boldsymbol{Z}_i^{-1} \sum_{j=1}^{i} \text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_j))\boldsymbol{v}_j$$

where we omit the PE, $l, h$ block/head indexes for simplicity. $\boldsymbol{Z}_i$ is a normalization term and $\varphi(\cdot)$ is a kernel function. Normally, $\boldsymbol{Z}_i = \sum_{j'=1}^{i} \text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_j))$. For softmax attention, $\varphi(\cdot)$ is an identity kernel and $\text{sim}(\boldsymbol{q}_i, \boldsymbol{k}_j) = \exp(\boldsymbol{q}_i \boldsymbol{k}_j^\top / \sqrt{d_h})$ [p. 9].

### Normalization [p. 9]

In Table 14(*Left*) and Figure 29, we show that modifying normalization may result in less obvious attention sink but does not stop its emergence. So we consider removing the normalization. Since the exponential function in softmax tends to explode without normalization, we replace it with sigmoid or elu plus one. We compute the attention sink by computing the proxy attention scores by using the term $\boldsymbol{Z}_i = \sum_{j=1}^{i} \text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_j))$ for attention sink metric Sink₁*. As shown in Table 6, without normalization, LMs still have comparable validation loss but no attention sink. With normalization, attention sinks emerges in LMs with sigmoid attention [p. 9].

### Kernel functions [p. 9-10]

Motivated by linear attention (Katharopoulos et al., 2020), we consider different kernel functions $\varphi(\cdot)$, including elu plus one, identity, and MLP. It is noted that $\text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_j))$ could be minus for identity and MLP kernels. This brings intrinsic difficulty for normalization during the training and calculation of Sink₁*. For normalization in the training, we consider $\boldsymbol{Z}_i = \max(|\sum_{j'=1}^{i} \text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_{j'})) |, 1)$. When computing Sink₁*, we consider the proxy attention scores $|\text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_j))| / \sum_{j'=1}^{i} |\text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_{j'}))|$. From Table 6 (a full version in Table 15), we find that the LM with MLP kernel have no attention sink with or without normalization [p. 9-10].

**Table 6:** Normalization and selections of kernels in attention significantly affect the emergence of the attention sink. We use "*" to mark that the metric Sink₁* is computed by proxy attention scores [p. 10].

| $\text{sim}(\varphi(\boldsymbol{q}_i), \varphi(\boldsymbol{k}_j))$ | $\boldsymbol{Z}_i$ | Sink₁(%) | valid loss |
|---|---|---|---|
| $\exp(\frac{\boldsymbol{q}_i \boldsymbol{k}_j^\top}{\sqrt{d_h}})$ | $\sum_{j'=1}^{i} \exp(\frac{\boldsymbol{q}_i \boldsymbol{k}_{j'}^\top}{\sqrt{d_h}})$ | 18.18 | 3.73 |
| $\text{sigmoid}(\frac{\boldsymbol{q}_i \boldsymbol{k}_j^\top}{\sqrt{d_h}})$ | $1$ | 0.44* | 3.70 |
| $\text{sigmoid}(\frac{\boldsymbol{q}_i \boldsymbol{k}_j^\top}{\sqrt{d_h}})$ | $\sum_{j'=1}^{i} \text{sigmoid}(\frac{\boldsymbol{q}_i \boldsymbol{k}_{j'}^\top}{\sqrt{d_h}})$ | 30.24 | 3.74 |
| $\text{elu}(\frac{\boldsymbol{q}_i \boldsymbol{k}_j^\top}{\sqrt{d_h}}) + 1$ | $1$ | 0.80* | 3.69 |
| $\frac{(\text{elu}(\boldsymbol{q}_i) + 1)(\text{elu}(\boldsymbol{k}_j) + 1)^\top}{\sqrt{d_h}}$ | $\sum_{j'=1}^{i} \frac{(\text{elu}(\boldsymbol{q}_i) + 1)(\text{elu}(\boldsymbol{k}_{j'}) + 1)^\top}{\sqrt{d_h}}$ | 53.65* | 4.19 |
| $\frac{\boldsymbol{q}_i \boldsymbol{k}_j^\top}{\sqrt{d_h}}$ | $1$ | 0.00* | 3.99 |
| $\frac{\text{mlp}(\boldsymbol{q}_i, \text{mlp}(\boldsymbol{k}_j))^\top}{\sqrt{d_h}}$ | $\max\left(\left|\sum_{j'=1}^{i} \frac{\text{mlp}(\boldsymbol{q}_i, \text{mlp}(\boldsymbol{k}_{j'}))^\top}{\sqrt{d_h}}\right|, 1\right)$ | 0.19* | 3.85 |
| $\frac{\text{mlp}(\boldsymbol{q}_i, \text{mlp}(\boldsymbol{k}_j))^\top}{\sqrt{d_h}}$ | $1$ | 0.74* | 3.91 |

**Figure 8** (p. 10): Caption: "We visualize the $\ell_2$-norm ratio of $h_1^l$ and mean of $h_{l\neq 1}^l$. (*Left*) Massive activations exist in LMs with attention scores that are non-negative and added up to one. (*Middle*) Massive activations do not exist in LMs with independent attention scores. (*Right*) When scaling the model size to 1B, LLMs with sigmoid attention (no normalization) still have no massive activations"

Description: Three panels showing effects of attention mechanisms on massive activations
- Left: Line plot showing $\ell_2$-norm ratio across transformer blocks (0-10) for different attention types in "LMs with attention sink": softmax (peaks ~30 at block 4), sigmoid w/ norm (peaks ~20 at block 6), elu plus one kernel w/o norm (stays low ~10), sigmoid w/o norm (lowest, ~5). Shows massive activations appear with normalized attention
- Middle: Line plot for "LMs without attention sink" showing $\ell_2$-norm ratio (1.0-1.8) across blocks for sigmoid w/o norm, elu plus one w/o norm, identity kernel w/o norm, and MLP kernel (w/o norm, w/ norm). All stay relatively flat (1.0-1.6), showing no massive activations
- Right: "Scale up to 1B LLMs" showing $\ell_2$-norm ratio across blocks (0-20) for softmax (peaks ~22 at block 12) vs sigmoid w/o norm (stays flat ~6). Demonstrates that even at 1B scale, sigmoid without normalization prevents massive activations
- Supports claim: Normalization and kernel choice determine whether massive activations and attention sink emerge

### Inner dependence on attention scores [p. 10]

We note that the LMs with no attention sink typically relax tokens' inner dependence on attention scores. Their attention scores during pre-training could be negative or not add up to one. This indicates that attention sink (at least partially) stems from such inner dependence. Besides the attention metric computed by proxy attention scores, we also observe that the above LMs also have no massive activations, as shown in Figure 8(*Middle*) [p. 10].

### Scale up to 1B parameters [p. 10]

We compare model behaviors of 1B LMs with softmax attention and sigmoid attention (without normalization). Specifically, the latter achieves a validation loss of 3.10, slightly larger than the 3.07 achieved by softmax attention. However, the attention sink metric significantly drops from 45.11% to near zero: Sink₁* ≈ 2.46% using the proxy attention scores. Meanwhile, as present in Figure 8(*Right*), LLMs with sigmoid attention still have no massive activations. Furthermore, they have no issues of training stability during continued supervised fine-tuning in Appendix E [p. 10].

**Takeaways** (from box on p. 10):
1. Positional embedding, FFN design, LN location, and multi-head design do not affect the emergence of attention sink
2. Attention sink acts more like key biases, storing extra attention and meanwhile not contributing to the value computation
3. When relaxing tokens' inner dependence on attention scores, attention sink does not emerge in LMs
