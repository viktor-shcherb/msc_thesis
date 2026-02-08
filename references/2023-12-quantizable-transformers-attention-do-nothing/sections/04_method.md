# 4 Method [p. 5-6]

[p. 5] The authors introduce proposed modifications for the softmax attention mechanism. Based on insights from Section 3, the core idea of these modifications is to grant the model the ability to produce very small magnitude (or even exact zeros) output of the attention function, without producing outliers.

The self-attention [60] is defined as follows:

$$\text{Attention}(\mathbf{x}) := \text{softmax}\left( \frac{\mathbf{Q}(\mathbf{x})\mathbf{K}(\mathbf{x})^T}{\sqrt{d_{\text{head}}}} \right) V(\mathbf{x}) \quad (3)$$

where $\mathbf{Q}$, $\mathbf{K}$ and $\mathbf{V}$ are learnable linear projections of the input $\mathbf{x}$. Most modern transformer models employ a multi-headed variant of self-attention, where $d_{\text{model}}$ features are partitioned into $n_{\text{heads}}$ groups of $d_{\text{head}}$ features, and the final output is the concatenation of the outputs of (3) applied to each group.

## 4.1 Clipped Softmax

[p. 5] The authors propose to replace the softmax function in (3) with the following clipped softmax:

$$\text{clipped\_softmax}(\mathbf{x};\, \zeta, \gamma) :=$$
$$\text{clip}\left((\zeta - \gamma) \cdot \text{softmax}(\mathbf{x}) + \gamma,\, 0,\, 1\right). \quad (4)$$

Here $\mathbf{x}$ is the input and $\zeta \geq 1$, $\gamma \leq 0$ are the stretch factors which are hyper-parameters of the method. Similar formulation was used before for sigmoid function [40, 45]. Equation (4) can be viewed as stretching the output of the softmax from $(0, 1)$ to $(\gamma, \zeta)$ and then clipping back to $(0, 1)$ so that exact zeros can be represented if $\gamma < 0$ and exact ones if $\zeta > 1$. Specifically, the values of the softmax larger than $\frac{1 - \gamma}{\zeta - \gamma}$ are rounded to one whereas values smaller than $\frac{-\gamma}{\zeta - \gamma}$ are rounded to zero.

With this drop-in replacement, exact zeros (and ones) can be achieved with a finite range for the softmax input. In addition, whenever values are clipped they will not give a gradient, preventing the outliers to grow further.

## 4.2 Gated Attention

[p. 6] An alternative way of architecting the model to have a small attention output without outliers is to equip it with an explicit conditional gating mechanism, as shown in Figure 5. The idea is that the model can use the gating to either keep or nullify the update to the representation of certain tokens and not rely on the attention probabilities and values to achieve the same outcome.

The following modification to the attention function is proposed:

$$\text{Gated\_attention}(\mathbf{x}) := \text{sigmoid}(\mathbf{G}(\mathbf{x})) \odot \text{softmax}\left( \frac{\mathbf{Q}(\mathbf{x})\mathbf{K}(\mathbf{x})^T}{\sqrt{d_{\text{head}}}} \right) V(\mathbf{x}). \quad (5)$$

Here $\mathbf{G}$ is the gating function, $\odot$ is an element-wise multiplication across the token axis and everything else remains the same as in (3). The gating function $\mathbf{G}$ is parameterized by a small neural network that is learned jointly with the rest of the model. The attention formulation is replaced with the proposed variant in every layer on the transformer network.

### Gating Module Design

[p. 6] The input to the attention layer $\mathbf{x}$ has shape $(T, d_{\text{model}})$ that is reshaped into $(n_{\text{heads}}, T, d_{\text{head}})$ for the multi-headed self-attention, where $T$ is the sequence length. The gating function is defined on a per-head basis. For each head $i \in \{1, \ldots, n_{\text{heads}}\}$, $\mathbf{G}_i : \mathbb{R}^{d_{\text{head}}} \to \mathbb{R}$ and the output of the gating module is $\boldsymbol{\pi}_i \in \mathbb{R}^T$ that is computed as follows:

$$\hat{\boldsymbol{\pi}}_{i,t} = \mathbf{G}_i(\mathbf{x}_{i,t,:}) \quad \forall t \in \{1, \ldots, T\} \quad (6)$$

$$\boldsymbol{\pi}_{i,:} = \text{sigmoid}(\hat{\boldsymbol{\pi}}_{i,:}), \quad (7)$$

Note that gating modules are shared between different token positions but not shared across attention heads.

The gating module is designed to be as lightweight as possible. $\mathbf{G}_i$'s are parameterized by a single linear layer. This gives a gating module that is computationally inexpensive and has a memory overhead of just $n_{\text{heads}} \cdot (d_{\text{head}} + 1) \sim d_{\text{model}}$ extra parameters (which is equivalent to 1 extra token) per attention layer (footnote 6: For instance, in case of BERT-base, this amounts to less than 0.009% of the total model size.). The effect of using several other gating functions is also investigated in Appendix B.1.

**Figure 5** (p. 6): "A schematic illustration of our proposed gated attention."
- Shows a block diagram of the gated attention mechanism: input $\mathbf{x}$ feeds into four projections G, Q, K, V. Q, K, V go into the Attention block producing $A$, while G produces the gating signal. The gate output and attention output $A$ are combined via element-wise multiplication ($\odot$), then passed through a Linear layer and added to the residual via $\oplus$.
