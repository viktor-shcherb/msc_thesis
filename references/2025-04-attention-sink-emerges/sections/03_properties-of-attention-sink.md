# Properties of attention sink [p. 4-6]

## 3.1 The first token acts as biases [p. 4]

### Uniqueness of the first token [p. 4]

It is noted that the calculation of hidden states for the first token has no involvement of self-attention: $h_1^l = \text{FFN}(\text{LN}(o_1^l + h_1^{l-1})) + o_1^l + h_1^{l-1}$, where $o_1^l = \text{LN}(h_1^{l-1})\mathbf{W}^{l,1}\mathbf{W}^{l,2} \cdots \mathbf{W}^{l,H}\mathbf{W}_O^l$. Therefore, $h_1^l$, and corresponding queries/keys/values $k_1^{l,h} = \text{LN}(h_1^{l-1})\mathbf{W}_K^{l,h}$, $q_1^{l,h} = \text{LN}(h_1^{l-1})\mathbf{W}_Q^{l,h}$, $v_1^{l,h} = \text{LN}(h_1^{l-1})\mathbf{W}_V^{l,h}$ could be considered as the MLP output of input position embedding. Using LLaMA3-8B Base (Dubey et al., 2024), the authors show that from certain transformer block, e.g., $l = 2$, the $\ell_2$-norm of $h_1^l$ is significantly larger than that of other tokens $h_{t \neq 1}^l \sim \mathcal{N}(p)$. This reproduces massive activations in Cancedda (2024); Sun et al. (2024). Despite the large $\ell_2$-norm of hidden states, we observe that the $\ell_2$-norm of keys and values has much smaller values than that of other tokens in the same figure, which was also observed in Devoto et al. (2024); Guo et al. (2024b) [p. 4].

### QK angles contribute to attention sink [p. 4]

In the $l$-th transformer block, we consider the keys and queries after adding PE (Rotary in LLaMA3-8B Base): $k_j^{l,h} = \text{LN}(h_j^{l-1})\mathbf{W}_K^{l,h}\mathbf{R}_{\Theta_{-1}, j} = q_j^{l,h}$ or $k_j^{l,h} = \text{LN}(h_j^{l-1})\mathbf{W}_K^{l,h}\mathbf{R}_{\Theta_{-1}, i}$, where LN is RMSNorm (Zhang & Sennrich, 2019): $\text{LN}(h) = \frac{1}{\text{RMS}(h)} \odot g$ and $\text{RMS}(h) = \sqrt{\frac{1}{d}\sum_{i=1}^d h_i^2}$. Here $g$ is a learnable gain parameter. Suppose that $h_1^{l-1}$ already has massive activations. Since $h_1^l$ has a massive magnitude in specific dimensions, the LN operation retains the magnitude in these dimensions but reduces the magnitude in other dimensions, leading to that $q_t^{l,h}, k_1^{l,h}$, and $v_1^{l,h}$ are distributed on different manifolds, especially for $k_1^{l,h}$ [p. 4].

For the $t$-th query, we know that $q_t^{l,h}k_1^{l,h\top}$ typically has much larger values than $q_t^{l,h}k_{j \neq 1}^{l,h\top}$, as visualized in Figure 2(*Bottom*). We further show that due to the different manifold of $k_1^{l,h}$, the angles between $k_1^{l,h}$ and $q_t^{l,h}$ play an important role. We have $q_t^{l,h}k_1^{l,h\top} = \|q_t^{l,h}\| \cdot \|k_1^{l,h}\| \cdot \cos(q_t^{l,h}, k_1^{l,h})$, we visualize the cosine similarity between keys and values, and the product between norm of keys and values in Figure 2(*Bottom*). Although $\|q_t^{l,h}\| \cdot \|k_1^{l,h}\|$ is comparatively small, $\cos(q_t^{l,h}, k_1^{l,h})$ is significantly large, leading to attention sink. This explains why attention sink exists despite the small $\ell_2$-norm of keys of the first token. To conclude, the first token leverages its keys to act as biases, thus minimizing the angles between $k_1^{l,h}$ and $q_t^{l,h}$ and exhibiting attention sink [p. 4].

## 3.2 Measuring attention sink [p. 4-5]

### Threshold-based metrics [p. 4]

Xiao et al. (2023b) showcased the appearance of attention sink by visualizing attention logits/scores in different heads/blocks. This leads to the intractability of measuring attention sink quantitatively due to the large number of attention heads and blocks. Therefore, we first explore the metrics to measure attention sink. Within each head, we compute the importance scores for the $k$-th token $\alpha_k^{l,h} = \frac{1}{T-k+1}\sum_{t=k}^T A_{t,k}^{l,h}$. We mainly focus on the first token $\alpha_1^{l,h}$. It is noted that $\frac{1}{T} \leq \alpha_1^{l,h} \leq 1$ since $A_{1,1}^{l,h} = 1$ and $0 \leq A_{t \neq 1,1}^{l,h} \leq 1$. Then we adopt a threshold-based metric, we consider a head has attention sink in the first token if $\alpha_1^{l,h} \geq \epsilon$. Considering that the whole model has $L$ blocks and each block has $H$ heads, we use the following metric to measure the attention sink of the whole LM: $\text{Sink}_1^\epsilon = \frac{1}{T}\sum_{l=1}^L \frac{1}{H}\sum_{h=1}^H \mathbb{I}(\alpha_1^{l,h} > \epsilon)$ [p. 4-5].

**Figure 3** (p. 4): "The metric $\text{Sink}_1^\epsilon$ (averaged on 100 sequences) tends to decrease with larger token lengths $T$. This tendency becomes more obvious with the more strict definition of attention sink (larger $\epsilon$)."

Description: Line plots showing attention sink metrics vs sequence length
- Key elements: Three panels for GPT2-XL, LLaMA2-7B Base, and LLaMA3-8B Base; x-axis shows token length $T$, y-axis shows $\text{Sink}_1^\epsilon$ (%); multiple lines for different $\epsilon$ values (0.2, 0.3, 0.4, 0.5)
- Notable patterns: All models show decreasing sink metrics with longer sequences; stricter thresholds (larger $\epsilon$) show more pronounced decreases; LLaMA3-8B shows strongest sink behavior
- Supports claim: Demonstrates that attention sink measurement depends on sequence length and threshold selection

### Selections of thresholds [p. 5]

Typically, the selections of thresholds represent the strictness of quantifying attention sink. Generally, a larger $\epsilon$ represents a strict definition for attention sink. There is no principal way to find an optimal threshold and we only use this metric to quantify the emergence of attention sink empirically. Based on Figure 3, we need to select a threshold that is both strict in quantifying attention sink and less sensitive to the token length $T$. This gives us the selection of $\epsilon = 0.3$. For fair comparisons, we need to fix $T$ when computing the metric, e.g., $T = 64$ [p. 5].

## 3.3 Attention sink under different inputs [p. 5]

### Different data domains [p. 5]

We first explore the effects of input domains on attention sinks. The pile dataset (Gao et al., 2020), a regular dataset used for LM pre-training, has 17 available data domains. As shown in Appendix C.2, input domains have negligible effects on our attention sink metric $\text{Sink}_1^\epsilon$ [p. 5].

### Beyond natural languages [p. 5]

We also consider two ideal scenarios: (i) randomly sample $T$ tokens from the tokenizer vocabulary $\mathcal{V}$ to construct a sequence, and (ii) randomly sample 1 token from the tokenizer $\mathcal{V}$ and repeat it $T$ times. As present in Table 1(*Left*), attention sink still exists when the inputs are random tokens instead of natural language data. However, with repeated tokens, attention sink in Mistral (Jiang et al., 2023) and LLaMA models disappears. In Appendix C.1, we prove that for LMs with NoPE/relative PE/ALiBi/Rotary, if the first $T$ tokens are the same, the corresponding hidden states are the same. They all have massive activations, thus dispersing the attention sink. We also provide the closed form/upper bound for attention scores in these LMs through Propositions 1-4 [p. 5].

## 3.4 Attention sink under different LMs [p. 5]

### Base vs. chat model [p. 5]

Compared with base models, chat models are typically continually trained through instruction tuning (Ouyang et al., 2022). From Table 1(*Right*), instruction tuning has an insignificant impact on attention sink, which motivates us to focus on the LM pre-training [p. 5].

### Model scale [p. 5]

We evaluate the metric $\text{Sink}_1^\epsilon$ of LLaMA2 Base (Touvron et al., 2023), LLaMA3 Base (Dubey et al., 2024), Pythia (Biderman et al., 2023), GPT2 (Radford et al., 2019), OPT (Zhang et al., 2022) families. As visualized in Figure 4(*Left*), attention sink emerges in small LMs, even in Pythia-14M. Only in Pythia family, larger-sized LMs tend to have more obvious attention sink [p. 5].

**Table 1** (p. 5): "(*Left*) Even with random sequence as input, there still exists an obvious attention sink. But with repeated tokens, the attention sink disappears for Mistral/LLaMA models. (*Right*) Chat models have comparable attention sink metrics with base models."

| LLM | $\text{Sink}_1^\epsilon$ (%) |  |  | LLM | $\text{Sink}_1^\epsilon$ (%) |  |
|-----|-----|-----|-----|-----|-----|-----|
|  | natural | random | repeat |  | Base | Chat |
| GPT2-XL | 77.00 | 70.29 | 62.28 | Mistral-7B | 97.49 | 88.34 |
| Mistral-7B | 97.49 | 75.21 | 0.00 | LLaMA2-7B | 92.47 | 92.88 |
| LLaMA2-7B Base | 92.47 | 90.13 | 0.00 | LLaMA2-13B | 91.69 | 90.94 |
| LLaMA3-8B Base | 99.02 | 91.23 | 0.00 | LLaMA3-8B | 99.02 | 98.85 |

**Figure 4** (p. 5): "(*Left*) Attention sink also emerges in small LMs. (*Middle*) Dynamics of train/valid loss and $\text{Sink}_1^\epsilon$ during LM pre-training under default setup. Attention sink becomes more obvious after certain optimization steps. (*Right*) Training loss (solid lines)/attention sink (dashed lines) dynamics of LMs using different learning rates. We observe that with smaller learning rates, attention sink tends to emerge after more optimization steps."

Description: Multi-panel plot showing model scale, training dynamics, and learning rate effects
- Key elements: Left panel shows $\text{Sink}_1^\epsilon$ (%) vs number of parameters for different model families; Middle panel shows train/valid loss and $\text{Sink}_1^\epsilon$ vs training steps; Right panel shows training loss and sink metrics vs optimization steps for different learning rates (1e-3, 4e-4, 1e-4, 1e-5)
- Notable patterns: Left - all model families show high sink metrics even at small scales (10M-10B parameters); Middle - sink emerges between 1k-2k training steps as loss decreases; Right - smaller learning rates delay sink emergence
- Supports claim: Demonstrates universal emergence of attention sink across model scales and its relationship to optimization dynamics
