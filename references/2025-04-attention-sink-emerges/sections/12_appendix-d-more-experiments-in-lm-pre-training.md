# Appendix D: More experiments in LM pre-training [p. 26]

## D.1 Optimization [p. 26]

### Learning rate [p. 26]

In Section 4, we find that attention sink appears less obvious in LMs trained with small learning rates. This conclusion holds even if we compensate for more training steps. In our base setup, we adopt a learning rate of 4e-4. When we scale the learning rate to half, i.e., 2e-4, we scale the training steps to 2 times, i.e., 40k. As shown in Table 9, when we keep the multiply between learning rate and training steps constant (highlighted using cyan color), LMs trained with smaller learning rates tend to exhibit less obvious attention sink. Therefore, we conclude that small learning rates not only slow down the increase of attention sink but also mitigate attention sink even with longer training durations.

**Table 9:** Attention sink appears less obvious in LMs trained with small learning rates even compensating for more training steps.

| learning rate | training steps (k) | Sink₁↑(%) | valid loss |
|---|---|---|---|
| 8e-4 | 10 | 23.44 | 3.79 |
| 8e-4 | 20 | 32.23 | 3.70 |
| 4e-4 | 20 | 18.18 | 3.73 |
| 2e-4 | 20 | 11.21 | 3.78 |
| 2e-4 | 40 | 16.81 | 3.68 |
| 1e-4 | 20 | 2.90 | 3.92 |
| 1e-4 | 80 | 6.29 | 3.67 |

### Batch size [p. 26]

During the pre-training, we consider different batch sizes with other hyper-parameters fixed. As shown in Table 10(Left), batch size does not affect the emergence of attention sink.

## D.2 Data distribution [p. 26]

### Training data amount [p. 26]

In Section 5, we find that with less training data, attention sink also disappears. Meanwhile, LMs are also susceptible to overfitting. To disentangle the effects of training data amount and overfitting on attention sink, we monitor the dynamics of train/valid loss and attention sink metric during the LM pre-training. As shown in Figure 28. With only 50M and 100M training data, LMs overfit at very early stages, between 1k and 2k steps. Meanwhile, Sink₁↑ maintains a very small value (less than 1%). While for the setup with 5B training data, Sink₁↑ keeps increasing after a certain step. This indicates that the amount of training data, instead of overfitting, plays an important role in the emergence of attention sink.

**Figure 28** (p. 26): Dynamics of train/valid loss and Sink₁↑ during LM pre-training under different amounts of training data: (Left) 50M; (Middle) 100M; (Right) 5B.

Description: Three dual-axis line plots showing training dynamics over steps (x-axis: 0-5k steps).
- Left panel (50M data): Shows train loss (orange) and valid loss (cyan) both around 4-8 on left y-axis, and sink (purple diamonds) near 0% on right y-axis (0-10%). Valid loss increases sharply after 1k steps indicating overfitting.
- Middle panel (100M data): Similar pattern with losses around 4-8, sink remains below 2%, overfitting visible after 2k steps.
- Right panel (5B data): Train loss (orange) and valid loss (cyan) both decrease smoothly from ~6 to ~4. Sink (purple diamonds) increases from near 0% to ~7% after 3k steps.
- Key elements: Dual y-axes with Loss (0-8) on left and Sink₁↑(%) (0-10) on right, steps (k) on x-axis
- Notable patterns: With small datasets (50M, 100M), overfitting occurs early and sink remains minimal. With large dataset (5B), no overfitting and sink emerges after sufficient training.
- Supports claim: Amount of training data, rather than overfitting, determines attention sink emergence

### Fixing token in a specific position [p. 26]

During the pre-training, we consider fixing the token $x_{\text{fix}}$ in the first/second/third position. Consequently, when evaluating the attention sink metric, in Table 10(Right), we find that attention sink appears in the fixed token instead of the first token.

---
[p. 27 continued]

**Table 10:** (Left) Batch size has no effect on the emergence of attention sink. (Right) Attention sink appears in the fixed token instead of the first token.

| Batch size | 0.25M | 0.5M | 1M | 2M | Fixed position | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|---|
| Sink₁↑(%) | 16.45 | 17.19 | 18.18 | 16.19 | Sink₁↑(%) | 74.11 | 0.00 | 0.00 |
| valid loss | 3.92 | 3.78 | 3.73 | 3.68 | Sink₂↑(%) | 0.00 | 69.03 | 0.00 |
| | | | | | Sink₃↑(%) | 0.00 | 0.00 | 69.64 |
| | | | | | Sink₄↑(%) | 0.01 | 0.01 | 0.00 |

## D.3 FFN design [p. 27]

### Activation functions [p. 27]

Since FFN in the earlier transformer block blasts off the $\ell_2$-norm of the first token, we are wondering whether activation functions in FFN will affect the attention sink. Besides the SwiGLU activations used in our default setup, we also consider other activation functions, as present in Table 11. We observe that different FFN designs do not affect the emergence of attention sink.

**Table 11:** Modifying the activation functions in FFN does not affect the emergence of attention sink.

| Activation functions | $F$ | Sink₁↑(%) | valid loss |
|---|---|---|---|
| ReLU | ReLU$(hW_1)W_2$ | 16.90 | 3.82 |
| GeLU (Hendrycks & Gimpel, 2016) | GeLU$(hW_1)W_2$ | 14.76 | 3.79 |
| Swish (Ramachandran et al., 2017) | Swish$(hW_1)W_2$ | 17.89 | 3.80 |
| ReGLU (Shazeer, 2020) | (ReLU$(hW_1) \odot hW_2)W_3$ | 13.88 | 3.75 |
| GeGLU (Shazeer, 2020) | (GeLU$(hW_1) \odot hW_2)W_3$ | 17.86 | 3.73 |
| SwiGLU (Shazeer, 2020) | (Swish$(hW_1) \odot hW_2)W_3$ | 18.18 | 3.73 |

## D.4 Attention design [p. 27]

### Multi-head design in attention [p. 27]

We consider two perspectives in multi-head design in attention. Firstly, we explore whether the number of heads will impact on attention sink, especially for $H = 1$, which refers to single-head self-attention. Second, attention output from each head is concatenated: $O^l = \text{Concat}_{h=1}^H (A^{l,h}V^{l,h})W_O^l$. We consider an alternative concatenation operation for the attention operation: $O^l = \sum_{h=1}^H (A^{l,h}V^{l,h})W_O^l$. As shown in Table 12(Left), multi-head design does not affect the emergence of attention sink.

**Table 12:** (Left) Modifying multi-head design does not affect the emergence of attention sink. (Right) Sharing KV biases across heads in each block results in attention sink shifting back to the first token from K biases.

| Multi-head | Sink₁↑(%) | valid loss | Head-sharing Biases type | ✓ KV | ✓ KV | × K | × K |
|---|---|---|---|---|---|---|---|
| $H = 8$ | 18.18 | 3.73 | | | | | |
| $H = 4$ | 10.68 | 3.74 | Sink₁↑(%) | 72.76 | 56.61 | 73.34 | 68.31 |
| $H = 2$ | 12.95 | 3.76 | Sink₁ₖ↑(%) | 0.04 | 12.44 | 0.00 | 0.23 |
| $H = 1$ | 19.50 | 3.78 | valid loss | 3.72 | 3.72 | 3.72 | 3.72 |
| addition | 21.76 | 3.74 | | | | | |

### Head-sharing K/KV biases in attention [p. 27]

In the main paper, we consider both KV biases and V biases in attention. These biases are not shared by different heads in each block. We further explore whether head-sharing patterns will affect their functionality. As present in Table 12(Right), LMs with KV biases are more likely affected by the head-sharing pattern: attention sink shifts from the K biases to the first token. While LMs with only K biases are less affected.

### Learnable dimensions of K biases [p. 27-28]

In the setup of K biases, we set all dimensions of $\mathbf{k}^{i,l,h}$ as learnable weights. In Section 3.1, we have shown that K biases are distributed in a different manifold, with low rank. Therefore, we consider only $d_a$ dimensions of $\mathbf{k}^{i,l,h}$ are adjustable/learnable while the other $d_h - d_a$ dimensions are zeros. As present in Table 13, with very few learnable dimensions, even for $d_a = 1$, $\mathbf{k}^{i,l,h}$ are still allocated significant attention. With more learnable dimensions, the attention sink appears more obvious.

**Table 13:** Even with very few learnable dimensions for $\mathbf{k}^{i,l,h}$, large attention appears in $\mathbf{k}^{i,l,h}$.

| $d_a$ | 1 | 2 | 4 | 8 | 16 | 32 | 64 |
|---|---|---|---|---|---|---|---|
| Sink₁↑(%) | 32.18 | 30.88 | 30.94 | 31.39 | 23.30 | 51.23 | 69.19 |
| Sink₁ₖ↑(%) | 4.74 | 4.96 | 4.39 | 4.54 | 2.19 | 1.94 | 0.04 |
| valid loss | 3.73 | 3.72 | 3.72 | 3.73 | 3.73 | 3.73 | 3.72 |

### Scaling the normalization in softmax attention [p. 28]

Before our experiments about replacing softmax attention, we first explore the effects of normalization scales in softmax attention. In the main paper, the attention output for the $i$-th token with output is

$$v_i^l = \sum_{j=1}^i \frac{\sin(\varphi(q_i), \varphi(k_j))}{\sum_{j'=1}^i \sin(\varphi(q_i), \varphi(k_{j'}))} v_j = \sum_{j=1}^i \frac{\sin(\varphi(q_i), \varphi(k_j))}{Z_i} v_j.$$ (29)

We consider a scale factor $\alpha$, the normalization term is $Z_i = \frac{1}{\alpha}\sum_{j'=1}^i \sin(\varphi(q_i), \varphi(k_j))$, and then the attention score are sum up to $\alpha$. For default setup, $\alpha = 1$. As shown in Table 14(Left), with a smaller normalization scale, attention sink tends to appear in fewer heads. From another perspective,

$$v_i^l = \sum_{j=1}^i \frac{\alpha \sin(\varphi(q_i), \varphi(k_j))}{\sum_{j'=1}^i \sin(\varphi(q_i), \varphi(k_{j'}))} v_j = \sum_{j=1}^i \frac{\sin(\varphi(q_i), \varphi(k_j))}{\sum_{j'=1}^i \sin(\varphi(q_i), \varphi(k_{j'}))} h_j/(\alpha W_V),$$ (30)

$$o_i^l = \text{Concat}_{h=1}^H (v_i^{l,h})W_O.$$ (31)

Therefore, this normalization scale can be regarded as the scale for $W_V$ or $W_O$. We show that this normalization scaling could be implemented by scaling learning rates and initialization. We use $s$ to represent the optimization step, and $s = 0$ refers to the initialization. When scaling the normalization, we have the following SGD update rule (take $W_O$ for example):

$$W_O^{s+1} = W_O^s - \eta \nabla_{W_O} \mathcal{L}(\alpha W_O^s)$$ (32)

$$= W_O^s - \alpha \eta \nabla_W \mathcal{L}(W)|_{W = \alpha W_O^s},$$ (33)

where $\eta$ is the original learning rate. Suppose we only modify the learning rate and initialization, to ensure each optimization step $W_O^s = \alpha W_O^s$, we need first to ensure $W_O^0 = \alpha W_O^0$. Suppose that we have $W_O^s = W_O^s$, then the update rule is

$$W_O^{s+1} = W_O^s - \eta' \nabla_{W_O^s} \mathcal{L}(W_O^s)$$ (34)

$$= \alpha W_O^s - \eta' \nabla_W \mathcal{L}(W)|_{W = \alpha W_O^s},$$ (35)

To ensure $W_O^{s+1} = \alpha W_O^{s+1}$, we need the new learning rate $\eta'$ meets $\eta' = \alpha^2 \eta$. For advanced optimization algorithms, e.g., Adam (Kingma & Ba, 2014) and AdamW (Loshchilov & Hutter, 2017). We have the following update rule (take AdamW for example, $\gamma$ refers to the weight decay ratio):

$$g_{s+1} = \nabla_{W_O} \mathcal{L}(\alpha W_O^s) = \alpha \nabla_W \mathcal{L}(W)|_{W = \alpha W_O^s}$$ (36)

$$m_{s+1} = \beta_1 m_s + (1 - \beta_1) g_{s+1}$$ (37)

$$v_{s+1} = \beta_2 v_s + (1 - \beta_2) g_{s+1}^2$$ (38)

$$W_O^{s+1} = (1 - \eta \gamma) W_O^s - \eta \frac{m_{s+1}/(1 - \beta_1^t)}{\sqrt{v_{s+1}/(1 - \beta_2^t)} + \epsilon}$$ (39)

We denote $\hat{g}_{s+1}$, $\hat{m}_{s+1}$, $\hat{v}_{s+1}$ represents the intermediate counterparts for update of scenario where we only modify learning rate and initialization. First, we also need to ensure the initialization $W_O^0 = \alpha W_O^0$. Then we assume that we have already matched $W_O^s = \alpha W_O^s$. The gradient for each step is

$$\hat{g}_{s+1} = \nabla_{W_O^s} \mathcal{L}(W_O^s) = \nabla_W \mathcal{L}(W)|_{W = \alpha W_O^s} = g_{s+1}/\alpha$$ (40)

---
[p. 29 continued]

Then the first and second moment will be $\hat{m}_{s+1} = m_{s+1}/\alpha$ and $\hat{v}_{s+1} = v_{s+1}/\alpha^2$. The updated weights will be

$$W_O^{s+1} = (1 - \eta' \gamma') W_O^s - \eta' \frac{\hat{m}_{s+1}/(1 - \beta_1^t)}{\sqrt{\hat{v}_{s+1}/(1 - \beta_2^t)} + \epsilon'}$$ (41)

$$= (1 - \eta' \gamma') \alpha W_O^s - \eta' \frac{m_{s+1}/\alpha(1 - \beta_1^t)}{\sqrt{v_{s+1}/\alpha^2(1 - \beta_2^t)} + \epsilon'}.$$ (42)

Therefore, to ensure $W_O^{s+1} = \alpha W_O^{s+1}$, one solution is $\eta' = \alpha \eta$ and $\epsilon' = \epsilon/\alpha$ and $\gamma' = \gamma/\alpha$.

**Table 14:** (Left) Scaling the normalization in Softmax attention to less than one can mitigate attention sink but not prevent its emergence. (Right) Sigmoid attention (without sigmoid attention) trained by different learning rates and weight decay ratios have no attention sink.

| Scale $\alpha$ | Sink₁↑(%) | valid loss | Learning rate | Weight decay | Sink₁↑(%) | valid loss |
|---|---|---|---|---|---|---|
| 2.0 | 29.10 | 3.72 | 4e-4 | 0.0 | 0.64 | 3.77 |
| 1.0 | 18.18 | 3.73 | 4e-4 | 0.1 | 0.44 | 3.70 |
| 0.2 | 9.41 | 3.72 | 4e-4 | 0.5 | 0.18 | 3.76 |
| 0.1 | 3.59 | 3.76 | 4e-4 | 1.0 | 0.30 | 4.06 |
| 0.05 | 4.53 | 3.78 | 1e-3 | 0.1 | 0.81 | 3.68 |
| | | | 1e-4 | 0.1 | 0.36 | 4.08 |

### Normalizer [p. 29]

Besides the normalizer $Z_i = \sum_{j'=1}^i \sin(\varphi(q_i), \varphi(k_{j'}))$ considered in the main paper, we consider alternative normalizer: $Z_i = \left(\sum_{j'=1}^i \sin(\varphi(q_i), \varphi(k_{j'}))^p\right)^{\frac{1}{p}}$, which gives us following attention operation:

$$v_i^l = \frac{\sum_{j=1}^i \sin(\varphi(q_i), \varphi(k_j))v_j}{Z_i} = \frac{\sum_{j=1}^i \sin(\varphi(q_i), \varphi(k_j))v_j}{\left(\sum_{j'=1}^i \sin(\varphi(q_i), \varphi(k_{j'}))^p\right)^{\frac{1}{p}}}.$$ (43)

For softmax attention, we have $\sin(\varphi(q_i), \varphi(k_j)) = \exp(\frac{q_i k_j^T}{\sqrt{d_h}})$, then we can derive that

$$v_i^l = \frac{\sum_{j=1}^i \exp(\frac{q_i k_j^T}{\sqrt{d_h}})v_j}{\left(\sum_{j'=1}^i \exp(\frac{q_i k_{j'}^T}{\sqrt{d_h}})^p\right)^{\frac{1}{p}}} = \sum_{j=1}^i \frac{\exp(\frac{q_i k_j^T}{\sqrt{d_h}/p})}{\left(\sum_{j'=1}^i \exp(\frac{q_i k_{j'}^T}{\sqrt{d_h}/p})\right)^{\frac{1}{p}}} v_j.$$ (44)

This is equivalent to adding a temperature $1/p$ into the softmax attention logits, and then taking the $p$-root of attention scores after softmax. We call this $p$-normalized softmax attention. $p = 1$ in regular softmax attention. Similarly, we construct $p$-normalized sigmoid attention.

We find that when $p = 2$ or $p = 3$ or $p = 4$, pre-training of $p$-normalized softmax attention diverges and the loss goes infinity. When $p = 1/2$ or $p = 1/3$ or $p = 1/4$, LM pre-training converges. As the attention scores are not added up to one, we investigate to massive activations instead, as visualized in Figure 29(Left). With smaller $p$, massive activations are mitigated to some extent, but not as effective as sigmoid attention normalization. Intuitively, smaller $p$ induces a larger temperature in softmax operation, which leads to flattened attention logits.

Afterward, we conduct experiments on $p$-normalized sigmoid attention. There is no training problem with $p$ larger than 1. As visualized in Figure 29(Right), LMs with $p$-normalized sigmoid attention still demonstrate strong massive activations. To conclude, different normalizers may affect the amplitude of attention sink, but not stop its emergence.

---
[p. 30 continued]

**Figure 29** (p. 30): $\ell_2$-norm ratio of $h_i^l$ and mean of $h_{l\neq0}^l$. (Left) $p$-normalized softmax attention and also sigmoid attention without normalization (as reference). (Right) $p$-normalized sigmoid attention and also sigmoid attention without normalization (as reference).

Description: Two line plots showing $\ell_2$-norm ratios across transformer blocks (x-axis: Block 0-10, y-axis: $\ell_2$-Norm Ratio 0-40 for left, 0-20 for right).
- Left panel (Softmax): Shows multiple curves for different $p$ values ($p = 1$, $p = 1/2$, $p = 1/3$, $p = 1/4$) and sigmoid without normalization. All $p$-normalized softmax curves peak around block 5-6 (reaching ~16-20), with $p = 1$ showing the highest peak. Sigmoid without normalization remains flat near 0.
- Right panel (Sigmoid): Shows curves for $p = 1$, $p = 2$, $p = 3$, $p = 4$ and no normalization. The $p$-normalized sigmoid curves show high peaks (reaching ~32-38) around blocks 5-6, especially for $p = 1$ and $p = 2$. No normalization case remains flat near 0.
- Key elements: Line plots with block number on x-axis, $\ell_2$-norm ratio on y-axis
- Notable patterns: Normalized attention (both softmax and sigmoid with $p$-norm) shows massive activations peaking in middle blocks, while sigmoid without normalization prevents this phenomenon
- Supports claim: Different normalizers affect the amplitude of attention sink but don't stop its emergence for normalized attention

### Attention operations [p. 29-30]

Firstly, we present all attempted attention operations in Table 15. It is noted that several setups lead to training failure. For LMs with sigmoid attention without normalization, we vary the learning rates or weight decay ratios $\gamma$. Consequently, as shown in Table 14(Right), the trained LMs still have no attention sink, which further confirms our conclusion in the main paper.

**Table 15:** Normalization and selections of kernels in attention significantly affect the emergence of the attention sink. We use "*" to mark that the metric Sink₁↑ is computed by proxy attention scores. We use "-" to represent the training failure under the setup.

| $\sin(\varphi(q_i), \varphi(k_j))$ | $Z_i$ | Sink₁↑(%) | valid loss |
|---|---|---|---|
| $\exp(\frac{q_i k_j^T}{\sqrt{d_h}})$ | $\sum_{j'=1}^i \exp(\frac{q_i k_{j'}^T}{\sqrt{d_h}})$ | 18.18 | 3.73 |
| sigmoid$(\frac{q_i k_j^T}{\sqrt{d_h}})$ | 1 | 0.44* | 3.70 |
| sigmoid$(\frac{q_i k_j^T}{\sqrt{d_h}})$ | $\sum_{j'=1}^i$ sigmoid$(\frac{q_i k_{j'}^T}{\sqrt{d_h}})$ | 30.24 | 3.74 |
| elu$(\frac{q_i k_j^T}{\sqrt{d_h}}) + 1$ | 1 | 0.80* | 3.69 |
| elu$(\frac{q_i k_j^T}{\sqrt{d_h}}) + 1$ | $\sum_{j'=1}^i$ elu$(\frac{q_i k_{j'}^T}{\sqrt{d_h}}) + 1$ | - | - |
| $\frac{(\text{elu}(q_i)+1)(\text{elu}(k_j)+1)^T}{\sqrt{d_h}}$ | $\sum_{j'=1}^i \frac{(\text{elu}(q_i)+1)(\text{elu}(k_j)+1)^T}{\sqrt{d_h}}$ | 53.65* | 4.19 |
| $\frac{(\text{elu}(q_i)+1)(\text{elu}(k_j)+1)^T}{\sqrt{d_h}}$ | 1 | - | - |
| $\frac{q_i k_j^T}{\sqrt{d_h}}$ | max$\left(\left|\sum_{j'=1}^i \frac{q_i k_{j'}^T}{\sqrt{d_h}}\right|, 1\right)$ | - | - |
| $\frac{q_i k_j^T}{\sqrt{d_h}}$ | 1 | 0.00* | 3.99 |
| $\frac{\text{mlp}(q_i \text{mlp}(k_j)^T}{\sqrt{d_h}}$ | max$\left(\left|\sum_{j'=1}^i \frac{\text{mlp}(q_i \text{mlp}(k_j)^T}{\sqrt{d_h}}\right|, 1\right)$ | 0.19* | 3.85 |
| $\frac{\text{mlp}(q_i \text{mlp}(k_j)^T}{\sqrt{d_h}}$ | 1 | 0.74* | 3.91 |
