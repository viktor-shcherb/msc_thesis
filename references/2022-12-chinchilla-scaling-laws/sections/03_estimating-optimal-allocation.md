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

---
[p. 7 continued]

**Figure 4** (p. 7): "Parametric fit. We fit a parametric modelling of the loss L_hat(N, D) and display contour (left) and isoFLOP slices (right). For each isoFLOP slice, we include a corresponding dashed line in the left plot. In the left plot, we show the efficient frontier in blue, which is a line in log-log space. Specifically, the curve goes through each iso-loss contour at the point with the fewest FLOPs. We project the optimal model size given the Gopher FLOP budget to be 40B parameters."

The figure consists of two panels:
- **Left panel ("IsoLoss contours"):** Model size (y-axis, 100M to 100B, log scale) vs Training FLOPs (x-axis, 10^18 to 10^23, log scale). Red iso-loss contours are shown across the space. The efficient frontier is plotted in blue as a straight line in log-log space, passing through each iso-loss contour at its minimum-FLOP point. Empirical data points are shown as black dots. IsoFLOP slices are shown as dashed vertical lines. A green marker indicates the *Gopher* compute budget projection.
- **Right panel ("IsoFLOPs slices"):** Loss (y-axis, ~2.0-5.0) vs Model size (x-axis, 100M to 40B, log scale). Multiple U-shaped curves are shown for different training FLOP budgets ranging from 6e+18 to 3e+21 plus *Gopher*. Each curve shows how loss varies with model size at a fixed FLOP budget.

**Efficient frontier.** The functions N_opt and D_opt can be approximated by minimizing the parametric loss L_hat under the constraint FLOPs(N, D) approximately equals 6ND (Kaplan et al., 2020). The resulting N_opt and D_opt balance the two terms in Equation (3) that depend on model size and data. By construction, they have a power-law form:

N_opt(C) = G * (C/6)^a,    D_opt(C) = G^{-1} * (C/6)^b,    where    G = (alpha * A / (beta * B))^{1/(alpha + beta)},    a = beta / (alpha + beta),    and b = alpha / (alpha + beta).    (4)

Contours of the fitted function L_hat are shown in Figure 4 (left), and the closed-form efficient computational frontier in blue. From this approach, a = 0.46 and b = 0.54 -- as summarized in Table 2.

## 3.4 Optimal model scaling [p. 7-8]

[p. 7-8] The three approaches, despite using different fitting methodologies and different trained models, yield comparable predictions for the optimal scaling in parameters and tokens with FLOPs (shown in Table 2). All three approaches suggest that as compute budget increases, model size and the amount of training data should be increased in approximately equal proportions. The first and second approaches yield very similar predictions for optimal model sizes, as shown in Figure 1 and Figure A3. The third approach predicts even smaller models being optimal at larger compute budgets. It is noted that the observed points (L, N, D) for low training FLOPs (C <= 1e21) have larger residuals ||L - L_hat(N, D)||_2^2 than points with higher computational budgets. The fitted model places increased weight on the points with more FLOPs -- automatically considering the low-computational budget points as outliers due to the Huber loss. As a consequence of the empirically observed negative curvature in the frontier C -> N_opt (see Appendix E), this results in predicting a lower N_opt than the two other approaches.

**Table 2** (p. 8): "Estimated parameter and data scaling with increased training compute. The listed values are the exponents, a and b, on the relationship N_opt proportional to C^a and D_opt proportional to C^b. Our analysis suggests a near equal scaling in parameters and data with increasing compute which is in clear contrast to previous work on the scaling of large models. The 10th and 90th percentiles are estimated via bootstrapping data (80% of the dataset is sampled 100 times) and are shown in parenthesis."

| Approach | Coeff. a where N_opt proportional to C^a | Coeff. b where D_opt proportional to C^b |
|---|---|---|
| 1. Minimum over training curves | 0.50 (0.488, 0.502) | 0.50 (0.501, 0.512) |
| 2. IsoFLOP profiles | 0.49 (0.462, 0.534) | 0.51 (0.483, 0.529) |
| 3. Parametric modelling of the loss | 0.46 (0.454, 0.455) | 0.54 (0.542, 0.543) |
| Kaplan et al. (2020) | 0.73 | 0.27 |

**Table 3** (p. 8): "Estimated optimal training FLOPs and training tokens for various model sizes. For various model sizes, we show the projections from Approach 1 of how many FLOPs and training tokens would be needed to train compute-optimal models. The estimates for Approach 2 & 3 are similar (shown in Section D.3)"

| Parameters | FLOPs | FLOPs (in *Gopher* unit) | Tokens |
|---|---|---|---|
| 400 Million | 1.92e+19 | 1/29,968 | 8.0 Billion |
| 1 Billion | 1.21e+20 | 1/4,761 | 20.2 Billion |
| 10 Billion | 1.23e+22 | 1/46 | 205.1 Billion |
| 67 Billion | 5.76e+23 | 1 | 1.5 Trillion |
| 175 Billion | 3.85e+24 | 6.7 | 3.7 Trillion |
| 280 Billion | 9.90e+24 | 17.2 | 5.9 Trillion |
| 520 Billion | 3.43e+25 | 59.5 | 11.0 Trillion |
| 1 Trillion | 1.27e+26 | 221.3 | 21.2 Trillion |
| 10 Trillion | 1.30e+28 | 22515.9 | 216.2 Trillion |

[p. 8] Current large language models are considerably over-sized, given their respective compute budgets, as shown in Figure 1. For example, a 175 billion parameter model should be trained with a compute budget of 4.41 x 10^24 FLOPs and on over 4.2 trillion tokens. A 280 billion *Gopher*-like model is the optimal model to train given a compute budget of approximately 10^25 FLOPs and should be trained on 6.8 trillion tokens. Unless one has a compute budget of 10^26 FLOPs (over 250x the compute used to train *Gopher*), a 1 trillion parameter model is unlikely to be the optimal model to train. Furthermore, the amount of training data that is projected to be needed is far beyond what is currently used to train large models, and underscores the importance of dataset collection in addition to engineering improvements that allow for model scale. While there is significant uncertainty extrapolating out many orders of magnitude, the analysis clearly suggests that given the training compute budget for many current LLMs, smaller models should have been trained on more tokens to achieve the most performant model.

In Appendix C, the IsoFLOP analysis is reproduced on two additional datasets: C4 (Raffel et al., 2020a) and GitHub code (Rae et al., 2021). In both cases the similar conclusion is reached that model size and number of training tokens should be scaled in equal proportions.
