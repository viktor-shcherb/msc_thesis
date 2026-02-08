# D. Switch Transformers in Lower Compute Regimes [p. 29-31]

[p. 29-30]

Switch Transformer is also an effective architecture at small scales as well as in regimes with thousands of cores and trillions of parameters. Many of the prior experiments were at the scale of 10B+ parameter models, but as shown in Figure 12 as few as 2 experts produce compelling gains over a FLOP-matched counterpart. Even if a super computer is not readily available, training Switch Transformers with 2, 4, or 8 experts (as the authors typically recommend one expert per core) results in solid improvements over T5 dense baselines.

[p. 31]

**Figure 12** (p. 31): "Switch Transformer with few experts. Switch Transformer improves over the baseline even with very few experts. Here we show scaling properties at very small scales, where we improve over the T5-Base model using 2, 4, and 8 experts."

The figure shows a line plot with Training Step (x-axis, 0 to 1e5) vs. Neg Log Perplexity (y-axis, -2.0 to -1.5). Four curves are plotted:
- Switch-Base: 8e (green) -- best performing, reaches approximately -1.68 at 1e5 steps
- Switch-Base: 4e (orange) -- second best, reaches approximately -1.72 at 1e5 steps
- Switch-Base: 2e (blue) -- third, reaches approximately -1.75 at 1e5 steps
- T5-Base (red) -- worst performing dense baseline, reaches approximately -1.77 at 1e5 steps

All Switch Transformer variants outperform the T5-Base dense model throughout training, with the gap increasing with the number of experts.
