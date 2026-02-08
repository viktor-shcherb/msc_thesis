# Analyses [p. 61]

## Per-token losses [p. 61]

[p. 61] The second through fourth rows of the Model Analysis Table show results derived from the per-token losses from the small models and full-scale models. The following "views" on the per-token loss data are shown: [p. 61]

- **Loss curve:** The random-token-per-example loss data -- a matrix of size (N model snapshots x 10,000 examples) for N = 200 snapshots per small model and N = 15 snapshots per full-scale model -- is averaged over the example dimension, giving an average loss per model snapshot. [p. 61]

- **2D in-context learning plot:** The context-index-average loss data -- a matrix of size (N model snapshots x 512 token index positions) -- is visualized directly as a 2D plot. This shows model performance on tokens earlier versus later in the context, as well as across training time. This technique is borrowed for highlighting "in-context learning" from Kaplan et al. [13]. A horizontal slice of this plot represents a loss curve as a function of training step, for one particular token index rather than averaged over all tokens; a vertical slice represents a particular snapshot's prediction ability as a function of token index. [p. 61]

- **2D loss derivative plot:** The partial derivative of the context-index-average loss data with respect to log(context index) is also plotted. This captures the amount that token loss is reduced by seeing e% more context. [p. 61]

- **In-context learning score:** What the authors call the "in-context learning score" is computed as the average loss of the 500th token minus the average loss of the 50th token (for a length-512 context), over training. This functions as a summary of the 2D in-context learning plot, capturing in a single summary statistic the trajectory over training time of the model's ability to make better predictions later in the context than earlier. [p. 61]

[p. 61] Additionally in a separate row at the top, PCA results from the per-token results are shown. These are displayed separately because, unlike all the other graphs, the x-axis is not elapsed training tokens. [p. 61]

- **PCA:** A plot of each model's trajectory in function space over training time, using PCA. The random-token-per-example loss data for all snapshots and all models of each type is concatenated into a large matrix, of shape (N*M model snapshots x 10,000 examples), where N = 200 snapshots per model and M = 12 models for small models, N = 15 snapshots per model and M = 6 models for full-scale models. This combined matrix is projected down to the first two principal components. Each model is then plotted separately, tracing out a trajectory in function space over the course of its training. [p. 61]

## Attention head measurements [p. 61]

[p. 61] The next two rows of Figure 1 show results derived from the attention head measurements: one row shows the score of the "prefix matching" head activation evaluator over training time, and the following row shows the prefix-matching QK-circuit eigenvalue trace over training time. [p. 61]

For the small models, all attention heads are shown. For the full-scale models, a subset of 100 heads is shown; see the Appendix for an explanation of how the 100 heads were chosen. [p. 61]

Note that in the QK-circuit plot, the change in weight decay at approximately 5 billion tokens (described in Model Details) can be seen particularly prominently as a bend or hiccup in the plotted trajectories, but occurs after the phase change and is an unrelated phenomenon. [p. 61]

## Ablation attribution to phase change [p. 61]

[p. 61] For the small models only, the final two rows of Figure 1 show results derived from the per-token loss data from the attention head ablation experiments. Only the pattern-preserving ablation results are shown here; full ablation results can be found in the appendix. Note also that ablation experiments were not conducted for the full-scale models. [p. 61]

The first "view" on the ablation data is the attribution to the "before-and-after" vector, which relates the result of each head ablation to the change in model behavior over the course of the phase change, and which is explained here. First: For a given model, a length-10,000 vector is computed by taking the delta of the random-token-per-example loss data for the "phase change end" snapshot, minus the "phase change start" snapshot. This represents how the model's behavior changed over the course of the phase change. This vector is normalized to a unit vector; this is called the before-and-after vector. It can be thought of as the "direction in token-loss space" that is affected by the phase change. Second: Note that ablating a given head also induces a change in the behavior of a model snapshot, and thus a corresponding length-10,000 vector change to the random-token-per-example loss data (calculated by subtracting the un-ablated snapshot's per-token loss vector from the ablated snapshot's per-token loss vector). The interest is in the similarity between these two changes, which is computed as the dot product between the model's before-and-after vector and the ablation change vector for this head and this snapshot. For induction heads, this dot product is negative, indicating that removing induction heads is like *undoing* the changes to model behavior that happened during the phase change. [p. 61]

The second "view" on the ablation data is the attribution to the *in-context learning score*. The model's in-context learning abilities are operationalized as how much better the model is at predicting the 500th token than the 50th token: this difference measured as Loss(ntrain, icontext=500) - Loss(ntrain, icontext=50) is the *in-context learning* score. [p. 61]
