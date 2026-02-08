# 2.6 Final Run Retrospective [p. 15–16]

### Figure 3

**Figure 3** (p. 15): **Pretraining Loss Curves and Gradient Norms.** The entirety of pretraining was stable, without major loss spikes or rollbacks. This held true even with the doubling of the global batch size (GBS), as well as changes in data mixtures, which result in discontinuous loss jumps through the difference in average cross entropy. The different stages of data are described in Section 3; Phase 5 coincides with the learning rate cooldown. For the gradient norms, curves are smoothed with a running window of 500 steps (70B) and 1000 steps (8B). The gradient norms of the 70B are noticeably smaller. No smoothing is applied to the loss curves.

- Top-left ("70B Loss Curve"): x-axis is Consumed Tokens (0.0T to 15.0T), y-axis is Loss (roughly 1.2 to 2.2). The loss curve shows steady decrease with vertical dashed lines marking data phase transitions (Sentence-GBS, Data Phase 1, Data Phase 2, Data Phase 3, Data Phase 4). Discontinuous jumps visible at data mixture transitions. Loss reaches roughly 1.2-1.3 by 15T.
- Top-right ("8B Loss Curve"): Similar layout. Loss decreases from ~2.2 to roughly 1.2-1.3, with the same phase transitions marked. Data Phase 4 transitions visible near 12.5T-15.0T.
- Bottom-left ("70B Gradient Norms"): x-axis is Consumed Tokens (0.0T to 15.0T), y-axis is Gradient Norms (0.0 to 1.0). Gradient norms remain relatively stable and low (~0.2-0.4 range), with smoothing applied (running window of 500 steps).
- Bottom-right ("8B Gradient Norms"): Similar layout. Gradient norms are visibly larger and noisier than 70B, with spikes reaching up to ~0.8-1.0, smoothed with running window of 1000 steps.

The Weights & Biases report of the main pretraining runs is publicly available. The authors plot the loss curves and gradient norms over the course of training both the 8B and 70B model in Figure 3. For transparency, reproducibility, and further research, they provide a retrospective analysis.

## Training Stability

[p. 15–16]

To much of the authors' satisfaction, the training runs were extremely stable and they never saw any major loss spikes or non-recoverable failures. Such extended stability was unexpected due to the scale and extensive length of training. Notably, the gradient norms remained within a considerable range for Apertus-70B, even across changes to the data mixture and batch size. While the norms grew visibly larger in the Apertus-8B run, this did not affect the loss and performance. Overall, there was only a single instance where the 70B model showed a NaN loss value. They believe this was due to a hardware failure, and they recovered through a rollback and replay.

## Gradient Clipping

[p. 16]

From the authors' experience and ablations, the AdEMAMix optimizer is more sensitive to the value of gradient norm clipping since the added momentum keeps a much longer history of gradient values. Their experiments led to setting a clipping value of 0.1. This means that when considering the gradient norms of Figure 3, in practice, clipping is applied at almost every step. While they did not notice any downstream influence of such aggressive clipping, it remains an interesting question to understand its necessity and the effects on training.

## Cooldown

[p. 16]

Perhaps surprisingly, Apertus-70B did not show a significant difference in slope with the onset of the cooldown phase (13.5T tokens, Figure 3), nor a large jump in benchmarks (see Figure 7). This is contrary to established results on a smaller scale and the run of Apertus-8B. It remains unclear why this was the case; the authors' main hypothesis is that the peak learning rate was set too low and that the model had not yet converged on the phase 4 data mixture. Due to the tight schedule of the project, they were unable to establish proper scaling rules for learning rate or experiment with more values at scale.

## Architecture

[p. 16]

Beyond the ablations described in Section 2.4, the authors put much research into improving the existing transformer architecture and its efficiency. In particular, they investigated reducing and preventing outlier activations through reordered or removed layer norms, similar to He et al. (2024), Blake et al. (2025) and Hernandez-Cano et al. (2025), with the motivation of enabling FP8 training. Further examples include the use of sparsely gated Mixture-of-Experts (Shazeer et al., 2017). None of these modifications were derisked enough at the time of pretraining, but remain on the horizon for future versions of Apertus.

## FP8 Training

[p. 16]

To accelerate training throughput, the authors experimented with FP8 data formats during the later stages. While this change resulted in a roughly 26% higher throughput, after roughly 300B tokens consumed of FP8 training, the loss suffered a major increase. They therefore decided to roll back and continue with the BF16 training normally. More information is provided in Appendix D.
