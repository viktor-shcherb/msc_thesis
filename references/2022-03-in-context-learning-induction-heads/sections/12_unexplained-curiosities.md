# Unexplained Curiosities [p. 40-41]

> "As with all scientific investigations, in the course of this work we've encountered a few unexplained phenomena. In this section, we discuss these and provide very preliminary investigations of a few that were especially surprising." [p. 40]

## Seemingly Constant In-Context Learning Score [p. 40-41]

One of the stranger observations in the paper is that in-context learning score (as defined: the loss of the 500th token in the context minus the loss of the 50th token in the context) is more or less the same for all models after the phase change. It appears to not matter whether the model is a tiny two layer model or a fairly large 13 billion parameter model, nor whether the model has just gone through the phase change or trained much longer. The only thing that matters, seemingly, is whether the model has gone through the phase change at all. [p. 40]

A natural question is whether this might be an artifact of the relatively arbitrary definition. After all, there is no reason to privilege token index 50 or 500 in the context. But it appears that varying these does not matter. The following plot shows how the large models' "in-context learning score" varies if it is defined instead as the difference between the loss at the final token in the context (8192) and other indices. While there are small differences between models -- for some definitions, small models would do slightly more "in-context learning"!^27 -- all definitions appear to show that the amount of in-context learning varies only slightly between models. [p. 40-41]

**Figure (unnumbered)** (p. 41): "In-Context Learning Score" Sensitivity to Definition
- Plot showing $\text{Loss}(i_{\text{ctx}} = -1) - \text{Loss}(i_{\text{ctx}})$ on the y-axis ($\Delta$ Loss) versus Context Index on the x-axis (log scale, from ~10^0 to ~10^3).
- Lines for six models: 4 Layer (13M), 6 Layer (42M), 10 Layer (200M), 16 Layer (810M), 24 Layer (2.7B), 40 Layer (13B).
- All lines follow nearly identical trajectories, decreasing from 0 to approximately -0.8 to -1.0 as the context index increases.
- Caption text: "Our in-context learning score requires one to pick two context indices to compare. But it appears that for a wide range of definition choices, models of different sizes still have nearly identical amounts of in-context learning. For some definitions, small models do more."
- Supports the claim that the amount of in-context learning is surprisingly constant across model sizes.

### Large models gain advantage early in context [p. 41]

Large models still predict tokens at all indices better than small models, and they are best at predicting later tokens. What is going on is that the large models gain all their advantage over small models very early in the context. In fact, the majority of the difference forms in the first ten tokens. [p. 41]

**Figure (unnumbered, left panel)** (p. 41): "Large Models Are Better at Predicting All Tokens, Including Later Ones"
- Plot showing $\text{Loss}(i_{\text{ctx}})$ on the y-axis (Loss) versus Context Index on the x-axis (log scale).
- Lines for the same six models (4L 13M through 40L 13B).
- All curves decrease with context index. Larger models have consistently lower loss at all context positions.
- The 40-layer (13B) model achieves the lowest loss at all positions, while the 4-layer (13M) model has the highest.

**Figure (unnumbered, right panel)** (p. 41): "Large Models Gain Their Loss Advantage Early in the Context"
- Plot showing $\text{Loss}(i_{\text{ctx}}) - \text{Loss}_{24L}(i_{\text{ctx}})$ on the y-axis ($\Delta$ Loss) versus Context Index on the x-axis (log scale).
- Lines for the same six models, showing loss relative to the 24-layer model.
- Most of the difference between models appears in the first ~10 tokens (left portion of the plot). After that, the lines are roughly flat, indicating no further divergence.
- The 40-layer model is slightly below zero (better than 24L), while smaller models are above zero (worse than 24L), with the gap established in the first tokens.

It seems that large models are able to pull a lot of information out of the very early context. (This might partly be, as an example, because their increased world knowledge means they do not need to gain as much information from the context.) They then further decrease their loss by a roughly fixed amount over the remainder of the context.^28 It seems likely this fixed amount is in some sense "more difficult in-context learning" for large models, since they are starting from a lower loss baseline. While it still seems mysterious to the authors why models should have the same in-context learning score, this perspective makes it "strange" rather than "shocking". [p. 41]

## Phase Change Effect on Loss Derivatives [p. 41]

Another observation the authors find quite striking is that if one looks at the derivative of the loss curves of models of different sizes, it appears that their order switches at the phase change. This is most easily seen by plotting the derivative of loss with respect to the log of elapsed tokens (since loss curves are often most easily reasoned about on a log x-axis). The key observation is that the loss decreases more slowly for small models than large models before the phase change, but the opposite is true after. [p. 41]

**Figure (unnumbered)** (p. 42): "Loss Derivative Order Appears to Invert at Phase Change"
- Plot showing $d\text{Loss} / d\log(\text{train tokens})$ on the y-axis versus Elapsed Training Tokens on the x-axis (log scale, from ~10^8 to ~10^11).
- Lines for five models: 6 Layer (42M), 10 Layer (200M), 16 Layer (810M), 24 Layer (2.7B), 40 Layer (13B).
- Y-axis ranges from approximately -0.6 to 0.0 (dashed line at 0.0).
- Orange/yellow vertical bands mark the phase change region (approximately around 10^9 tokens).
- Before the phase change: small models (6 Layer) improve faster (more negative derivative), labeled "Small models improve faster".
- After the phase change: large models (40 Layer, 24 Layer) improve faster (more negative derivative), labeled "Large models improve faster than small models".
- The inversion of ordering is clearly visible: the lines cross during the phase change interval.

While it does not seem surprising that small models learn more quickly in early training, it is striking that this inversion seems to coincide with the phase change. It is another piece of evidence that suggests the phase change is an important transition point in the training of transformers. [p. 42]

## Additional Curiosities [p. 42]

In the model analysis table: [p. 42]

- The 6-layer attention-only model has an unusual head that develops in the later half of training. This head is *not* an induction head, and yet ablating it has an effect similar to reversing the phase change (in the "before-and-after vector" attribution plot). What is this head? [p. 42]

- The 4-layer MLP model ablations are nowhere near as "peaky" as those of any other model. What is different about this model's development? [p. 42]

- The 6-layer MLP model shows a "loss spike". The authors do not yet know what causes loss spikes. [p. 42]

- The 6-layer MLP model has one lone induction head whose ablation has the opposite effect on the in-context learning score. What is this head? [p. 42]

And in the Appendix: [p. 42]

- Full-scale models above 16 layers start to show a small number of heads that score well on "prefix search", but get a *negative* score on copying, which means they are not induction heads. What can we learn about these "anti-copying prefix-search" heads? [p. 42]
