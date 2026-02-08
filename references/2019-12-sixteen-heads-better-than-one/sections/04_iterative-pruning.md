# 4 Iterative Pruning of Attention Heads [p. 5-6]

In the ablation experiments (Sections 3.2 and 3.3), the authors observed the effect of removing one or more heads within a single layer, without considering what would happen if they altered two or more different layers at the same time. To test the compounding effect of pruning multiple heads from across the entire model, they sort all the attention heads in the model according to a proxy importance score (described below), and then remove the heads one by one. This iterative, heuristic approach avoids combinatorial search.

## 4.1 Head Importance Score for Pruning [p. 6]

As a proxy score for head importance, the authors look at the expected sensitivity of the model to the mask variables $\xi_h$ defined in Section 2.3:

$$I_h = \mathbb{E}_{x \sim X} \left| \frac{\partial \mathcal{L}(x)}{\partial \xi_h} \right| \tag{2}$$

where $X$ is the data distribution and $\mathcal{L}(x)$ the loss on sample $x$. Intuitively, if $I_h$ has a high value then changing $\xi_h$ is liable to have a large effect on the model. The absolute value is used to avoid datapoints with highly negative or positive contributions from nullifying each other in the sum.

Plugging Equation 1 into Equation 2 and applying the chain rule yields the final expression for $I_h$:

$$I_h = \mathbb{E}_{x \sim X} \left| \text{Att}_h(x)^T \frac{\partial \mathcal{L}(x)}{\partial \text{Att}_h(x)} \right|$$

This formulation is reminiscent of the literature on pruning neural networks (LeCun et al., 1990; Hassibi and Stork, 1993; Molchanov et al., 2017, inter alia). In particular, it is equivalent to the Taylor expansion method from Molchanov et al. (2017).

Estimating $I_h$ only requires performing a forward and backward pass, and therefore is not slower than training. In practice, the expectation is computed over the training data or a subset thereof (footnote 5: for the WMT model they use all `newstest20[09-12]` sets to estimate $I$). As recommended by Molchanov et al. (2017), they normalize the importance scores by layer (using the $\ell_2$ norm).

## 4.2 Effect of Pruning on BLEU/Accuracy [p. 6]

**Figure 3** (p. 6): "Evolution of accuracy by number of heads pruned according to $I_h$ (solid blue) and individual oracle performance difference (dashed green)."

Figures 3a (WMT) and 3b (BERT) describe the effect of attention-head pruning on model performance while incrementally removing 10% of the total number of heads in order of increasing $I_h$ at each step.

- (a) "Evolution of BLEU score on `newstest2013` when heads are pruned from WMT." X-axis: Percentage pruned (0%-100%). Y-axis: BLEU (0-35). BLEU stays relatively flat around 35 until ~20% pruned, then begins declining, with a sharp drop after ~60% pruned, reaching near 0 at 100%.
- (b) "Evolution of accuracy on the MultiNLI-matched validation set when heads are pruned from BERT." X-axis: Percentage pruned (0%-100%). Y-axis: Accuracy (0.0-0.8). Accuracy stays relatively flat around 0.8 until ~40% pruned, then begins declining, with a sharp drop after ~60% pruned, reaching near 0.0 at 100%.

Both figures also show results when the pruning order is determined by the score difference from Section 3.2 (dashed lines), but using $I_h$ is faster and yields better results. See Appendix B for experiments on four additional datasets.

Key finding: this approach allows pruning up to **20%** of heads from WMT and **40%** of heads from BERT without incurring any noticeable negative impact. Performance drops sharply when pruning further, meaning that neither model can be reduced to a purely single-head attention model without retraining or incurring substantial losses to performance.

---
[p. 7 continued]

## 4.3 Effect of Pruning on Efficiency [p. 7]

Beyond downstream task performance, there are intrinsic advantages to pruning heads. Each head represents a non-negligible proportion of the total parameters in each attention layer (6.25% for WMT, ~8.34% for BERT), and roughly speaking, in both models, approximately one third of the total number of parameters is devoted to MHA across all layers (footnote 6: slightly more in WMT because of the Enc-Dec attention).

Actually pruning the heads (not just masking) results in an appreciable increase in inference speed.

**Table 4** (p. 7): "Average inference speed of BERT on the MNLI-matched validation set in examples per second ($\pm$ standard deviation). The speedup relative to the original model is indicated in parentheses."

| Batch size | 1 | 4 | 16 | 64 |
|---|---|---|---|---|
| Original | $17.0 \pm 0.3$ | $67.3 \pm 1.3$ | $114.0 \pm 3.6$ | $124.7 \pm 2.9$ |
| Pruned (50%) | $17.3 \pm 0.6$ | $69.1 \pm 1.3$ | $134.0 \pm 3.6$ | $146.6 \pm 3.4$ |
| | (+1.9%) | (+2.7%) | (+17.5%) | (+17.5%) |

Experiments were conducted on two different machines, both equipped with GeForce GTX 1080Ti GPUs. Each experiment is repeated 3 times on each machine (for a total of 6 datapoints for each setting). Pruning half of the model's heads speeds up inference by up to ~17.5% for higher batch sizes (this difference vanishes for smaller batch sizes).
