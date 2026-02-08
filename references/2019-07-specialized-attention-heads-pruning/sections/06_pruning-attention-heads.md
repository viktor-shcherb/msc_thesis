# 6 Pruning Attention Heads [p. 6]

The authors introduce a method for pruning attention heads to determine whether remaining (non-specialized) heads are redundant to translation quality or play equally vital but less easily defined roles. The method is based on Louizos et al. (2018). Whereas Louizos et al. pruned individual neural network weights, this work prunes entire model components (i.e. heads). [p. 6]

## 6.1 Method [p. 6]

The original Transformer architecture is modified by multiplying the representation computed by each head_i by a scalar gate $g_i$. Equation (3) turns into:

$$\text{MultiHead}(Q, K, V) = \text{Concat}_i(g_i \cdot \text{head}_i) W^O$$

Unlike usual gates, $g_i$ are parameters specific to heads and are independent of the input (i.e. the sentence). The goal is to disable less important heads completely rather than simply down-weighting them. Ideally, $L_0$ regularization would be applied to the scalars $g_i$. The $L_0$ norm equals the number of non-zero components and would push the model to switch off less important heads: [p. 6]

$$L_0(g_1, \ldots, g_h) = \sum_{i=1}^{h} (1 - [[g_i = 0]]),$$

where $h$ is the number of heads, and $[[\cdot]]$ denotes the indicator function. [p. 6]

Unfortunately, the $L_0$ norm is non-differentiable and so cannot be directly incorporated as a regularization term in the objective function. Instead, a stochastic relaxation is used: each gate $g_i$ is now a random variable drawn independently from a head-specific distribution. In training, gate values $g_i$ are resampled for each batch (footnote 5). [p. 6]

The Hard Concrete distributions (Louizos et al., 2018) are used, a parameterized family of mixed discrete-continuous distributions over the closed interval $[0, 1]$, see Figure 6a. The distributions have non-zero probability mass at 0 and 1, $P(g_i = 0|\phi_i)$ and $P(g_i = 1|\phi_i)$, where $\phi_i$ are the distribution parameters. [p. 6]

Intuitively, the Hard Concrete distribution is obtained by stretching the binary version of the Concrete (aka Gumbel softmax) distribution (Maddison et al., 2017; Jang et al., 2017) from the original support of $(0, 1)$ to $(-\epsilon, 1 + \epsilon)$ and then collapsing the probability mass assigned to $(-\epsilon, 1]$ and $[1, 1 + \epsilon)$ to single points, 0 and 1, respectively. These stretching and rectification operations yield a mixed discrete-continuous distribution over $[0, 1]$. [p. 6]

The sum of the probabilities of heads being non-zero can be used as a relaxation of the $L_0$ norm:

$$L_C(\phi) = \sum_{i=1}^{h} (1 - P(g_i = 0|\phi_i)).$$

The new training objective is:

$$L(\theta, \phi) = L_{xent}(\theta, \phi) + \lambda L_C(\phi),$$

where $\theta$ are the parameters of the original Transformer, $L_{xent}(\theta, \phi)$ is cross-entropy loss for the translation model, and $L_C(\phi)$ is the regularizer described above. [p. 6]

The objective is easy to optimize: the reparameterization trick (Kingma and Welling, 2014; Rezende et al., 2014) can be used to backpropagate through the sampling process for each $g_i$, whereas the regularizer and its gradients are available in closed form. [p. 6]

The model converges to solutions where gates are either almost completely closed (i.e. the head is pruned, $P(g_i = 0|\phi_i) \approx 1$) or completely open ($P(g_i = 1|\phi_i) \approx 1$), the latter not being explicitly encouraged (footnote 6). This means that at test time the model can be treated as a standard Transformer and use only a subset of heads. At test time, gate values are either 0 or 1 depending on which of the values $P(g_i = 0|\phi_i)$, $P(g_i = 1|\phi_i)$ is larger (footnote 7). [p. 6]

The combination of noise and rectification has been previously used to achieve discretization (e.g., Kaiser and Bengio (2018)). [p. 6]

**Figure 6** (p. 6): Concrete distribution: (a) Concrete and its stretched and rectified version (Hard Concrete); (b) Hard Concrete distributions with different parameters. Two line plots showing:
- (a) Comparison of Concrete distribution (blue curve) vs hard concrete (orange curve) with p(0)=0.23, p(1)=0.23. The hard concrete has probability mass at 0 and 1.
- (b) Three Hard Concrete distributions with different parameters: p(0)=0.23, p(1)=0.23 (blue); p(0)=0.04, p(1)=0.69 (orange); p(0)=0.86, p(1)=0.01 (green).

## Application procedure

When applying the regularizer, the authors start from the converged model trained without the $L_C$ penalty (i.e. parameters $\theta$ are initialized with the parameters of the converged model) and then add the gates and continue training the full objective. By varying the coefficient $\lambda$ in the optimized objective, models with different numbers of heads retained are obtained. [p. 6]

## 6.2 Pruning Encoder Heads [p. 6]

To determine which head functions are most important in the encoder and how many heads the model needs, a series of experiments with gates applied only to encoder self-attention is conducted. A model is pruned by fine-tuning a trained model with the regularized objective. During pruning, the parameters of the decoder are fixed and only the encoder parameters and head gates are fine-tuned. By not fine-tuning the decoder, the authors ensure that the functions of the pruned encoder heads do not migrate to the decoder. [p. 6]

In preliminary experiments, fine-tuning a trained model gives slightly better results (0.2-0.6 BLEU) than applying the regularized objective, or training a model with the same number of self-attention heads, from scratch (footnote 8). [p. 6]

### 6.2.1 Quantitative Results: BLEU Score [p. 6]

BLEU scores are provided in Figure 7. [p. 6]

> "Surprisingly, for OpenSubtitles, we lose only 0.25 BLEU when we prune all but 4 heads out of 48." [p. 6]

For the more complex WMT task, 10 heads in the encoder are sufficient to stay within 0.15 BLEU of the full model. [p. 6]

If all heads in a layer are pruned, the only remaining connection to the previous layer is the residual connection (footnote 9). [p. 6]

**Figure 7** (p. 7): BLEU score as a function of number of retained encoder heads (EN-RU). Regularization applied by fine-tuning trained model. Two line plots:
- WMT (left): Y-axis BLEU 28.25–29.75. With 48 heads: ~29.6 BLEU. Remains near plateau down to ~19 heads. At 10 heads: ~29.5. At 5 heads: ~29.0. At 2 heads: ~28.25.
- OpenSubtitles (right): Y-axis BLEU 31.6–32.4. With 48 heads: ~32.4. Remains near plateau down to ~17 heads. At 9 heads: ~32.15. At 4 heads: ~32.15. At 1 head: ~31.7.

---
[p. 7–9 continued]

### 6.2.2 Functions of Retained Heads [p. 7]

Results in Figure 7 suggest that the encoder remains effective even with only a few heads. The authors investigate the function of those heads that remain in the encoder during pruning. Figure 8 shows all heads color-coded for their function in a pruned model. Each column corresponds to a model with a particular number of heads retained after pruning. Heads from all layers are ordered by their function. Some heads can perform several functions (e.g., $s \to v$ and $v \to o$); in this case the number of functions is shown. [p. 7]

First, the model with 17 heads retains heads with all the functions identified in Section 5, even though 2/3 of the heads have been pruned. [p. 7]

This indicates that these functions are indeed the most important. Furthermore, when there are fewer heads in the model, some functions "drift" to other heads: for example, positional heads starting to track syntactic dependencies; hence some heads are assigned more than one color at certain stages in Figure 8. [p. 7]

**Figure 8** (p. 7): Functions of encoder heads retained after pruning. Each column represents all remaining heads after varying amount of pruning (EN-RU; Subtitles). Columns labeled 48, 30, 17, 14, 11, 9, 7, 6, 5, 4, 3, 2, 1. Heads are color-coded:
- Purple: positional
- Green: syntactic
- Orange: rare tokens
- Grey: unknown
At 48 heads (full model): 34 heads with various functions. At 17 heads: all function types still present. As pruning increases, heads take on multiple functions. At 1 head: a single head remains.

## 6.3 Pruning All Types of Attention Heads [p. 7–8]

The pruning technique is found to be efficient at reducing the number of heads in the encoder without a major drop in translation quality. Now the effect of pruning all types of attention heads in the model (not just in the encoder) is investigated. This allows evaluation of the importance of different types of attention in the model for the task of translation. In these experiments, gates are added to all multi-head attention heads in the Transformer, i.e. encoder and decoder self-attention and attention from the decoder to the encoder. [p. 7]

### 6.3.1 Quantitative Results: BLEU Score [p. 7–8]

Results of experiments pruning heads in all attention layers are provided in Table 2. For models trained on WMT data, it is possible to prune almost 3/4 of encoder heads and more than 1/3 of heads in decoder self-attention and decoder-encoder attention without any noticeable loss in translation quality (sparse heads, row 1). It is also possible to prune more than half of all heads in the model and lose no more than 0.25 BLEU. [p. 7–8]

While these results show clearly that the majority of attention heads can be removed from the fully trained model without significant loss in translation quality, it is not clear whether a model can be trained from scratch with such a small number of heads. In the rightmost column in Table 2, BLEU scores are provided for models trained with exactly the same number and configuration of heads in each layer as the corresponding pruned models but starting from a random initialization of parameters. The degradation in translation quality is more significant than for pruned models with the same number of heads. This agrees with observations made in works on model compression: sparse architectures learned through pruning cannot be trained from scratch to the same test set performance as a model trained with joint sparsification and optimization (Zhu and Gupta, 2017; Gale et al., 2019). In this case, attention heads are less likely to learn important roles when a model is retrained from scratch with a small number of heads. [p. 8–9]

**Table 2** (p. 7): BLEU scores for gates in all attentions, EN-RU. Number of attention heads is provided in the following order: encoder self-attention, decoder self-attention, decoder-encoder attention.

| | attention heads (e/d/d-e) | BLEU from trained | BLEU from scratch |
|---|---|---|---|
| **WMT, 2.5m** | | | |
| baseline | 48/48/48 | | 29.6 |
| sparse heads | 14/31/30 | 29.62 | 29.47 |
| | 12/21/25 | 29.36 | 28.95 |
| | 8/13/15 | 29.06 | 28.56 |
| | 5/9/12 | 28.90 | 28.41 |
| **OpenSubtitles, 6m** | | | |
| baseline | 48/48/48 | | 32.4 |
| sparse heads | 27/31/46 | 32.24 | 32.23 |
| | 13/17/31 | 32.23 | 31.98 |
| | 6/9/13 | 32.27 | 31.84 |

### 6.3.2 Heads Importance [p. 8–9]

Figure 9 shows the number of retained heads for each attention type at different pruning rates. The model prefers to prune encoder self-attention heads first, while decoder-encoder attention heads appear to be the most important for both datasets. Obviously, without decoder-encoder attention no translation can happen. [p. 8]

The importance of decoder self-attention heads, which function primarily as a target side language model, varies across domains. These heads appear to be almost as important as decoder-encoder attention heads for WMT data with its long sentences (24 tokens on average), and slightly more important than encoder self-attention heads for OpenSubtitles dataset where sentences are shorter (8 tokens on average). [p. 9]

Figure 10 shows the number of active self-attention and decoder-encoder attention heads at different layers in the decoder for models with different sparsity rate (to reduce noise, the sum of heads remaining in pairs of adjacent layers is plotted). Self-attention heads are retained more readily in the lower layers, while decoder-encoder attention heads are retained in the higher layers. This suggests that lower layers of the Transformer's decoder are mostly responsible for language modeling, while higher layers are mostly responsible for conditioning on the source sentence. These observations are similar for both datasets used. [p. 9]

**Figure 9** (p. 8): Number of active heads of different attention type for models with different sparsity rate. Two line plots:
- WMT (left): Y-axis 0–48 active heads. X-axis: 0–108 pruned heads. Three lines for enc self (blue circles), dec self (red squares), dec-enc (orange triangles). Encoder self-attention drops fastest; decoder-encoder drops slowest.
- OpenSubtitles (right): Y-axis 8–48. X-axis: 0–102 pruned heads. Same pattern: encoder self-attention pruned first, decoder-encoder last.

**Figure 10** (p. 8): Number of active heads in different layers of the decoder for models with different sparsity rate (EN-RU, WMT). Two line plots:
- Decoder self-attention (left): Y-axis 0–16 active heads. X-axis: 0–35 pruned heads. Three lines for layers 1+2 (blue), 3+4 (red), 5+6 (orange). Lower layers (1+2) retain more heads.
- Dec-enc attention (right): Y-axis 4–16. X-axis: 0–33 pruned heads. Higher layers (5+6) retain more heads.
