# 3 Outlier Analysis [p. 3-5]

## Outliers in BERT Models

[p. 3] Outliers are present only in a few designated embedding dimensions but they appear regularly and consistently across multiple layers and data sequences. The strongest magnitude outliers in BERT typically appear at the output of FFN in the last encoder layers.

The authors start by taking the pre-trained *BERT-base-uncased* checkpoint from HuggingFace [65] and fine-tune it on MNLI dataset from the well-known GLUE benchmark [61] (see experimental details in C.1). To identify the outlier dimensions, they pass the MNLI-m validation set through the network and record all outliers (footnote 1: outliers defined as values that exceed 6 standard deviations from the mean of the corresponding activation tensor, following Bondarenko et al. [4]) at the FFN output in layers #10 and #11 (footnote 2: 1-based indexing for encoder layers and attention heads throughout the paper). As shown in Figure 1, there are indeed only a few hidden dimensions where outliers ever occur. The majority of outliers (> 97%) correlate with the position of delimiter tokens -- [SEP], ".", and ",".

To better understand the role of those outliers, the authors analyze the attention patterns of the corresponding attention heads. BERT-base uses multi-head attention with $n_{\text{heads}} = 12$ and each head operating on a consecutive subset of $d_{\text{head}} = 64$ features. Therefore, the hidden dimension #180, which happens to have the highest outlier count in both layers #10 and #11, corresponds to attention head #3. In Figure 2 (and more examples in Appendix A.1) they show examples of the attention matrices, values and their product for that head.

[p. 3-4] A common pattern found is that the attention head assigns almost all of its probability mass to [SEP] tokens, and other less informative tokens like dots/commas, while these tokens also have small values in **V** associated with those tokens. This results in a small magnitude product between the two (see Figure 2a). This effectively corresponds to a (soft) *no-update* of the hidden representation, where only small noise is added after the residual. In other cases (Figure 2b and 2c), a significant portion of attention probability is still spent on delimiter tokens. However, by allocating some of the probability mass on other tokens (together with the small values for the delimiter tokens), this results in a (soft) *selective* update of the hidden representation.

These patterns in self-attention seem to be a learned "workaround" for the limitations of having the softmax and the residual connections in cases where the attention head does not want to update the representation of some or all of the tokens. These observations are in line with Clark et al. [8], Kovaleva et al. [30] that also argued that attending exclusively or almost exclusively to delimiter tokens such as [SEP], periods/commas acts as a "no-op" when the attention head's function is not applicable.

**Figure 1** (p. 3): "Histograms of outlier counts vs. token positions (blue) and hidden dimensions (green), recorded from the MNLI-m validation set on BERT-base. We use zero-based indexing for dimensions."
- Two subfigures: (a) FFN output in layer #10, (b) FFN output in layer #11
- Blue bars show outlier counts by token position: [SEP] has by far the highest count (~60000+ in layer #10, ~50000+ in layer #11), with ".", "the", "it", "to", "and", "," also showing counts but much smaller
- Green bars show outlier counts by hidden dimension: only a few specific dimensions (#180, #720, #123, #181, #25, #526, #308) have outliers, with #180 having the highest count in both layers

**Figure 2** (p. 4): "Visualization of the patterns in the self-attention, specifically the attention probabilities, values, and their product (left, middle and right columns, respectively), in attention head #3 for BERT-base, computed on several data sequences from MNLI-m validation set."
- Three rows showing different cases:
  - (a) Attention layer #11, data sequence #1 -- attention concentrates on delimiter tokens, small values, small product (no-update)
  - (b) Attention layer #11, data sequence #5 -- significant attention on delimiters but some on other tokens (selective update)
  - (c) Attention layer #10, data sequence #5 -- similar selective update pattern
- Left column: attention probability matrices (heatmaps), middle column: value matrices, right column: their product

## Outliers in ViT

[p. 4] A similar analysis is conducted for Vision transformer [15] trained on ImageNet [52]. For this study, a pre-trained checkpoint is used following the experimental setup from Section 5. The ViT/S-16 configuration with only 22M parameters is used (footnote 3).

Findings are highlighted in Figure 3 and more examples are provided in Appendix A.2. The analysis shows many similarities to the BERT case. Instead of delimiter tokens, the majority of outliers seem to correlate with some random uninformative patches (e.g., in the background). The corresponding attention head in the next layer allocates the majority of attention probabilities to the same patches. Those outlier patches on average have a distinctly smaller magnitude of values compared to non-outlier ones, leading to similar no-update behavior. The fact that those values are not as close to zero as in the BERT case might be related to the smaller model capacity, or a relatively shorter training procedure.

**Figure 3** (p. 4): "A summary of our outlier analysis for ViT demonstrated on a random image from ImageNet validation set. (a) An input image. (b) Outliers in the output of layer #11. (c) Cumulative attention weight spent on every patch (matrix of attention probabilities summed over rows) in the attention head #1, layer #12. (d) A corresponding matrix of attention probabilities. (e) An average magnitude of values for outlier and non-outlier patches."
- (a) Shows an input image (a bird/parrot)
- (b) Shows outlier locations in layer #11 output -- concentrated in specific spatial locations
- (c) Shows cumulative attention weights as a heatmap -- attention concentrated on specific patches (including background patches)
- (d) Shows the full attention probability matrix (~196x196 patches), with visible concentration patterns
- (e) Bar chart comparing average magnitude of values: non-outlier patches have magnitude ~2.0-2.5, outlier patches have magnitude ~0.5, confirming much smaller values for outlier patches

## Hypothesis

[p. 4-5] Based on these observations, the authors pose the following hypothesis on how the behavior of attention heads is related to outliers:

1. In order for an attention block to not update a representation of a token on the residual, some attention heads want to allocate most of their attention probability mass to some fixed and common set of tokens that have a low information content (e.g., delimiter tokens or background patches) that can be learned to have a small value function output.

2. [p. 5] From the definition of the softmax function (footnote 4: $\text{softmax}(\mathbf{x})_i = \exp(\mathbf{x}_i) / \sum_{j=1}^{d} \exp(\mathbf{x}_j)$), it is easy to see that this would require an input of the softmax to have a relatively big dynamic range (Figure 4, marker 1). In fact, in the limit case where softmax is exactly zero, this would require an infinite dynamic range:

$$\text{softmax}(\mathbf{x})_i = 0 \quad \Leftrightarrow \quad \exists j \neq i,\, \mathbf{x}_j - \mathbf{x}_i = +\infty \quad (2)$$

3. Since Layer Normalization ([1], marker 2) normalizes the outliers, the magnitude of the FFN output *in the previous layer* (marker 3) has to be very high to still produce a sufficiently big dynamic range after the LayerNorm. This is also applicable for the transformer models with LayerNorm applied prior to the self-attention or linear transformations instead, a variant adopted by GPT, OPT, and many vision transformers [15, 38, 57, 58].

4. Finally, as softmax will never output exact zeros, it will always back-propagate a gradient signal to grow bigger outliers (footnote 5: Let $\mathbf{y} = \text{softmax}(\mathbf{x})$. Then $\frac{\partial y_i}{\partial x_j} \neq 0 \; \forall i, j$.). The outliers will thus tend to become stronger in magnitude, the longer the network is trained.

**Figure 4** (p. 5): "A schematic illustration of the attention layer in BERT. Hidden activation tensor is denoted by x. $\oplus$ is an element-wise addition. A problematic output of the FFN that generates largest in magnitude outliers is highlighted in red. Notice how those outliers in the *previous* layer influence the behavior in the attention mechanism in the *next* layer."
- Shows a block diagram of the attention layer: previous layer's FFN (Linear, GELU, Linear) outputs feed through a residual connection (with marker 3 showing "biggest outliers" at the FFN output), then through Layer Norm (marker 2), then into the attention mechanism with Q, K, V projections, Attention computation (marker 1), followed by a Linear layer and another residual addition leading to the next layer.
