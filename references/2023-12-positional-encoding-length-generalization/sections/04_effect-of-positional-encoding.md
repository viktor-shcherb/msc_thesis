# What Is The Effect of Positional Encoding? [p. 4-5]

[p. 4] To provide a holistic view, following Liang et al. (2022), the authors report the mean ranking of various models in Figures 1 and 2 when compared against each other for all tasks and scenarios. They also showcase the accuracy of models evaluated on examples of various lengths in Figure 3. Detailed results for each task and scenario can be found in Appendix E.

First, in most tasks, models achieve a perfect or near-perfect accuracy (Figure 3) on the I.I.D. lengths, which indicates that models have no problem fitting to the training data. However, the differences among positional encoding methods become more apparent when evaluating on lengths that are larger than seen during training.

[p. 5] In most extrapolation scenarios, T5's Relative Bias outperforms other explicit positional encodings. ALiBi positions itself in the middle of the pack, while APE and Rotary show poor generalization performance.

Although Rotary is often considered a relative encoding method (Ontanon et al., 2022), the results show that it performs more similarly to APE than to other relative schemes. Moreover, ALiBi, despite its promise for length generalization, underperforms with respect to T5's Relative Bias in most cases. This result aligns with Taylor et al. (2022) who found no significant improvement from ALiBi.

Surprisingly, the NoPE model, which is just a decoder-only Transformer without any positional encoding, performs on par with or even better than the best-performing explicit PE, T5's Relative Bias. NoPE achieves the same level of generalization without *any computational overhead* since it does not compute any additional term in the attention mechanism. This property has a direct impact on the runtime and memory footprint of the model. For instance, Press et al. (2022) reported that the additional computation incurred by T5's Relative Bias can make the training and inference time of the model almost two times slower than the Transformer with APE.

**Figure 3** (p. 5): "Showcasing the generalization behavior of different positional encodings on 6 datasets. The shaded area represents evaluation examples with I.I.D. lengths (i.e. seen during training). Since all models perform perfectly, or close to it, on the I.I.D. lengths (measured on unseen examples), for improved readability, we only show a subset of them in the figure. Refer to Appendix E for more detailed plots."

The figure contains 6 subplots (Copy, Addition, SCAN on top row; Reverse, Summation, PCFG on bottom row). Each subplot shows Accuracy (y-axis, 0 to 1) vs Problem Length (x-axis). Five line series represent NoPE, T5's Relative PE, ALiBi, Rotary, and Absolute Position Embedding. Shaded regions indicate I.I.D. lengths. Key observations:
- **Copy** (x: 15-40): NoPE and T5 maintain ~1.0 accuracy well beyond training lengths; ALiBi degrades around length 25; Rotary and APE drop to ~0 at extrapolation lengths.
- **Addition** (x: 8-16): NoPE and T5 maintain moderate accuracy in extrapolation; ALiBi, Rotary, and APE drop sharply.
- **SCAN** (x: 20-40): NoPE and T5 show best extrapolation with gradual decline; others are lower.
- **Reverse** (x: 15-40): Similar pattern with NoPE and T5 leading.
- **Summation** (x: 8-16): All methods struggle in extrapolation; NoPE and T5 maintain slightly better accuracy.
- **PCFG** (x: 10-30): All methods degrade; NoPE appears slightly better than others.
