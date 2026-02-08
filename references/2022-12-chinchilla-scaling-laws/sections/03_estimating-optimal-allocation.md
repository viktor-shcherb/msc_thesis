# 3. Estimating the optimal parameter/training tokens allocation [p. 4-6]

[p. 4] Three different approaches are presented to answer the question driving the research: *Given a fixed FLOPs budget, how should one trade-off model size and the number of training tokens?* In all three cases, the authors start by training a range of models varying both model size and the number of training tokens and use the resulting training curves to fit an empirical estimator of how they should scale. A power-law relationship between compute and model size is assumed as done in Clark et al. (2022); Kaplan et al. (2020), though future work may want to include potential curvature in this relationship for large model sizes. The resulting predictions are similar for all three methods and suggest that parameter count and number of training tokens should be increased equally with more compute -- with proportions reported in Table 2. This is in clear contrast to previous work on this topic and warrants further investigation.

Footnote 3: "We compute FLOPs as described in Appendix F." [p. 4]

## 3.1 Approach 1: Fix model sizes and vary number of training tokens [p. 5]

[p. 5] In the first approach the number of training steps is varied for a fixed family of models (ranging from 70M to over 10B parameters), training each model for 4 different number of training sequences. From these runs, an estimate of the minimum loss achieved for a given number of training FLOPs is directly extracted. Training details for this approach can be found in Appendix D.

For each parameter count N, 4 different models are trained, decaying the learning rate by a factor of 10x over a horizon (measured in number of training tokens) that ranges by a factor of 16x. Then, for each run, the training loss curve is smoothed and then interpolated. From this, a continuous mapping from FLOP count to training loss for each run is obtained. Then, for each FLOP count, it is determined which run achieves the lowest loss. Using these interpolants, a mapping from any FLOP count C, to the most efficient choice of model size N and number of training tokens D such that FLOPs(N, D) = C is obtained. At 1500 logarithmically spaced FLOP values, the model size that achieves the lowest loss of all models along with the required number of training tokens is found. Finally, power laws are fitted to estimate the optimal model size and number of training tokens for any given amount of compute (see the center and right panels of Figure 2), obtaining a relationship N_opt proportional to C^a and D_opt proportional to C^b. The authors find that a = 0.50 and b = 0.50 -- as summarized in Table 2. In Section D.4, a head-to-head comparison at 10^21 FLOPs is shown, using the model size recommended by their analysis and by the analysis of Kaplan et al. (2020) -- using the model size they predict has a clear advantage.

Footnote 4: "Note that all selected points are within the last 15% of training. This suggests that when training a model over D tokens, we should pick a cosine cycle length that decays 10x over approximately D tokens -- see further details in Appendix B." [p. 5]

**Figure 2** (p. 5): "Training curve envelope. On the left we show all of our different runs. We launched a range of model sizes going from 70M to 10B, each for four different cosine cycle lengths. From these curves, we extracted the envelope of minimal loss per FLOP, and we used these points to estimate the optimal model size (center) for a given compute budget and the optimal number of training tokens (right). In green, we show projections of optimal model size and training token count based on the number of FLOPs used to train Gopher (5.76 x 10^23)."

The figure consists of three panels:
- **Left panel:** Training loss (y-axis, range ~2.0-6.0) vs FLOPs (x-axis, 10^17 to 10^22). Multiple curves shown for model sizes from 75M to 10B, each with different cosine cycle lengths. Curves are colored by model size. The envelope of minimum loss per FLOP is visible.
- **Center panel:** Parameters (y-axis, 100M to 1T, log scale) vs FLOPs (x-axis, 10^17 to 10^25, log scale). Points from the envelope are plotted, with a power-law fit line. A green marker shows the projection for the Gopher compute budget.
- **Right panel:** Tokens (y-axis, 10^9 to 10^12, log scale) vs FLOPs (x-axis, 10^17 to 10^25, log scale). Points from the envelope are plotted with a power-law fit line. A green marker shows the projection for the Gopher compute budget (labeled 1.4T).

## 3.2 Approach 2: IsoFLOP profiles [p. 5-6]

[p. 5] In the second approach the model size is varied for a fixed set of 9 different training FLOP counts (ranging from 6 x 10^18 to 3 x 10^21 FLOPs), and the final training loss for each point is considered. In contrast with Approach 1 that considered points (N, D, L) along the entire training runs, this allows directly answering the question: For a given FLOP budget, what is the optimal parameter count?

Footnote 5: "In approach 2, model size varies up to 16B as opposed to approach 1 where we only used models up to 10B." [p. 5]
Footnote 6: "The number of training tokens is determined by the model size and training FLOPs." [p. 5]
Footnote 7: "We set the cosine schedule length to match the number of tokens, which is optimal according to the analysis presented in Appendix B." [p. 5]

[p. 6] For each FLOP budget, the final loss (after smoothing) is plotted against the parameter count in Figure 3 (left). In all cases, a diverse enough set of model sizes has been trained to see a clear minimum in the loss. A parabola is fitted to each IsoFLOPs curve to directly estimate at what model size the minimum loss is achieved (Figure 3 (left)). As with the previous approach, a power law between FLOPs and loss-optimal model size and number of training tokens is then fitted, shown in Figure 3 (center, right). Again, exponents of the form N_opt proportional to C^a and D_opt proportional to C^b are fitted and it is found that a = 0.49 and b = 0.51 -- as summarized in Table 2.

**Figure 3** (p. 6): "IsoFLOP curves. For various model sizes, we choose the number of training tokens such that the final FLOPs is a constant. The cosine cycle length is set to match the target FLOP count. We find a clear valley in loss, meaning that for a given FLOP budget there is an optimal model to train (left). Using the location of these valleys, we project optimal model size and number of tokens for larger models (center and right). In green, we show the estimated number of parameters and tokens for an optimal model trained with the compute budget of Gopher."

The figure consists of three panels:
- **Left panel:** Training Loss (y-axis, ~2.0-3.2) vs Parameters (x-axis, 100M to 30B, log scale). Nine IsoFLOP curves are shown for budgets from 6e18 to 3e21 FLOPs. Each curve shows a clear U-shaped valley (minimum) at an intermediate model size. Colored dots and lines mark each FLOP budget level.
- **Center panel:** Parameters (y-axis, 100M to 1T, log scale) vs FLOPs (x-axis, 10^17 to 10^23, log scale). The optimal model sizes from the IsoFLOP minima are plotted. A power-law fit line is shown. A green marker indicates the projection for the Gopher compute budget (G3).
- **Right panel:** Tokens (y-axis, 100M to 10T, log scale) vs FLOPs (x-axis, 10^17 to 10^25, log scale). The optimal token counts from the IsoFLOP minima are plotted. A power-law fit line is shown. A green marker indicates the projection for the Gopher compute budget (1.4T).

## 3.3 Approach 3: Fitting a parametric loss function [p. 6]

[p. 6] Lastly, all final losses from experiments in Approach 1 & 2 are modelled as a parametric function of model parameter count and the number of seen tokens. Following a classical risk decomposition (see Section D.2), the following functional form is proposed:

L_hat(N, D) = E + A / N^alpha + B / D^beta.  (2)

- The first term E captures the loss for an ideal generative process on the data distribution, and should correspond to the entropy of natural text.
- The second term captures the fact that a perfectly trained transformer with N parameters underperforms the ideal generative process.
- The final term captures the fact that the transformer is not trained to convergence, as we only make a finite number of optimisation steps, on a sample of the dataset distribution.

**Model fitting.** To estimate (A, B, E, alpha, beta), the Huber loss (Huber, 1964) between the predicted and observed log loss is minimized using the L-BFGS algorithm (Nocedal, 1980):

min_{A, B, E, alpha, beta} sum_{Runs i} Huber_delta(log L_hat(N_i, D_i) - log L_i)  (3)

Possible local minima are accounted for by selecting the best fit from a grid of initialisations. The Huber loss (delta = 10^-3) is robust to outliers, which is found important for good predictive performance over held-out data points. Section D.2 details the fitting procedure and the loss decomposition.
