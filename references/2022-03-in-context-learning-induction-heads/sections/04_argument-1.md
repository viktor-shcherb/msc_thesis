# Argument 1: Transformer language models undergo a "phase change" during training, during which induction heads form and simultaneously in-context learning improves dramatically [p. 9-11]

[p. 9] The first line of evidence comes from correlating measures of in-context learning and measures of induction head presence over the course of training. Specifically, a tight co-variation is observed between them across dozens of models, of different sizes, trained on different datasets (see Model Analysis Table for more on the models in which this co-occurrence is observed). [p. 9]

## Strength of argument for sub-claims [p. 10]

|                      | Small Attention-Only    | Small with MLPs         | Large Models            |
|----------------------|-------------------------|-------------------------|-------------------------|
| Contributes Some     | Medium, Correlational   | Medium, Correlational   | Medium, Correlational   |
| Contributes Majority | Medium, Correlational   | Medium, Correlational   | Medium, Correlational   |

The table summarizes the quality of the evidence for Argument 1: it applies to both large and small models, and is the expected outcome if induction heads were responsible for the majority of in-context learning, but it is only correlational and so could be confounded. [p. 10]

## Abrupt onset of in-context learning [p. 10]

The first observation is that if in-context learning is measured for transformer language models over the course of training (defined as the 50th token loss minus the 500th token loss as described in Key Concepts), it develops abruptly in a narrow window early in training (roughly 2.5 to 5 billion tokens) and then is constant for the rest of training. Before this window there is less than 0.15 nats of in-context learning; after it there is roughly 0.4 nats, an amount that remains constant for the rest of training and is also constant across many different model sizes (except for the one-layer model where not much in-context learning ever forms). [p. 10]

This seems surprising -- naively, one might expect in-context learning to improve gradually over training, and improve with larger model sizes, as most things in machine learning do. [p. 10]

**Figure 3** (p. 10): "Models with more than one layer have an abrupt improvement in in-context learning." Three panels show in-context learning score (y-axis, ranging from approximately -0.5 to 0.0) vs. elapsed training tokens (x-axis, ranging from 0 to 1e10) for one-layer, two-layer, and three-layer attention-only models. The "phase change" period is highlighted in yellow/orange in the two-layer and three-layer panels (roughly between 2.5e9 and 5e9 tokens), selected based on the derivative of in-context learning. Key observations:
- **One-layer model:** has no sudden improvement; in-context learning score stays relatively flat around -0.1.
- **Two-layer model:** shows a sudden drop (improvement) in in-context learning score during the highlighted phase change region, from approximately -0.1 to approximately -0.4.
- **Three-layer model:** shows a similar sudden improvement during the same phase change window.
The pattern holds true very generally: many examples are shown in the Model Analysis Table later in the paper, including models of varying model architecture and size. [p. 10]

## Derivative of loss with respect to log token index [p. 10-11]

One might wonder if the sudden increase is somehow an artifact of the choice to define in-context learning in terms of the difference between the 500th and 50th tokens. This is discussed in more depth later. But an easy way to see that this is a robust phenomenon is to look at the derivative of loss with respect to the logarithm of token index in context. This can be thought of as measuring something like "in-context learning per e% increase in context length." This can be visualized on a 2D plot, where one axis is the amount of training that has elapsed, the other is the token index being predicted. Before the phase change, loss largely stops improving around token 50, but after the phase change, loss continues to improve past that point. [p. 10-11]

**Figure 4** (p. 11): "Derivative of loss with respect to log token index." Three heatmap panels for one-layer, two-layer, and three-layer attention-only models. X-axis: elapsed training tokens (0 to 1e10). Y-axis: token index in context (0 to 500+). Color scale represents derivative of loss with respect to log(token index), ranging from 0.1 (light) to -0.3 (dark blue). Negative values mean more in-context learning. The subtitle notes: "The rate at which loss decreases with increasing token index can be thought of as something like 'in-context learning per token'. This appears to be most naturally measured with respect to the log number of tokens." The highlighted "phase change" portion of training is the same area highlighted in previous plots, selected based on the derivative of the in-context score. Key observations:
- **One-layer model:** losses flatten after token 50 throughout training.
- **Two-layer and three-layer models:** after the phase change, they continue to reduce their loss with longer contexts (dark blue regions extend to higher token indices post phase change). [p. 11]

## Co-occurrence with induction head formation [p. 11]

A sudden improvement in in-context learning is not the only thing that changes in the phase change window. If the attention heads of a model are scored for whether they are induction heads (using a *prefix matching score* which measures their ability to perform the task used to define induction heads in Key Concepts), induction heads are found to form abruptly during exactly the same window where in-context learning develops. Again only a few models are shown, but a full set is shown in the Model Analysis Table. The exception is the one-layer model, where induction heads never form -- just as in-context learning never substantially develops for the one-layer model. [p. 11]

**Figure 5** (p. 11): "Induction heads form in phase change." Each line is an attention head, scored by the "prefix matching" evaluation. Three panels for one-layer, two-layer, and three-layer attention-only models. X-axis: elapsed training tokens (0 to 1e10). Y-axis: prefix matching score (0.0 to 1.0). The highlighted "phase change" portion of training is the same area highlighted in previous plots. Key observations:
- **One-layer model:** has no induction heads; all lines remain near 0.0 throughout training.
- **Two-layer model:** several attention heads abruptly increase their prefix matching score during the phase change, with some reaching approximately 0.8-0.9.
- **Three-layer model:** similarly, several heads abruptly develop high prefix matching scores during the phase change. [p. 11]

## Connection to overall training dynamics [p. 11]

This already strongly suggests some connection between induction heads and in-context learning, but beyond just that, the phase change window appears to be a pivotal point for the training process in general: whatever is occurring is visible as a bump on the training loss curve. It is in fact the only place in training where the loss is not convex (monotonically decreasing in slope). [p. 11]

That might not sound significant, but the loss curve is averaging over many thousands of tokens. Many behaviors people find interesting in language models, such as the emergence of arithmetic, would be microscopic on the loss curve. For something to be visible at that scale suggests it is a widespread, major change in model behavior. This shift also appears to be the first point where, at least for small models, the loss curve diverges from a one-layer model -- which does not display the bump, just as it does not display the other abrupt changes. [p. 11]

---
[p. 12 continued]

## Loss curves diverge during phase change [p. 12]

**Figure 6** (p. 12): "Loss curves diverge during phase change." Three panels for one-layer, two-layer, and three-layer attention-only models. X-axis: elapsed training tokens (0 to 1e10). Y-axis: loss in nats/token (ranging from approximately 2.0 to 8.0). The highlighted "phase change" portion of training is the same area highlighted in previous plots, selected based on the derivative of the in-context score. Key observations:
- **One-layer model:** loss curve decreases smoothly with no bump.
- **Two-layer model:** the one-layer model's loss curve is overlaid for comparison; the two-layer loss initially tracks the one-layer loss, then diverges at the phase change with a visible "bump" where loss temporarily plateaus or increases slightly before resuming decline.
- **Three-layer model:** same pattern -- loss diverges from the one-layer model at the phase change, with a visible bump. The three-layer model eventually achieves lower loss than the two-layer model.
- One-layer model has no bump in loss curve; models with more than one layer have a "bump" where loss diverges from the one-layer model. [p. 12]

## Per-token loss principal component analysis [p. 12]

PCA can also be applied to the per-token losses, as described in the per-token-loss analysis method (see Key Concepts). This allows summarizing the main dimensions of variation in how several models' predictions vary over the course of training. [p. 12]

The first two principal components of these models' predictions are shown, with the golden outline highlighting the same interval shown above (when in-context learning abruptly improved). The training trajectories pivot during exactly the same window where the other changes happen. In some sense, whatever is occurring when in-context learning improves is the primary deviation from the basic trajectory the transformers follow during the course of their training. Once again the only exception is the one-layer model -- where induction heads cannot form and in-context learning does not improve. [p. 12]

**Figure 7** (p. 12): "Per-token loss principal component analysis." Three panels for one-layer, two-layer, and three-layer attention-only models. X-axis: first principal component. Y-axis: second principal component. Each panel shows the training trajectory as a curve through PCA space, with an arrow labeled "training" indicating direction. The "phase change" portion of training is highlighted in orange, the same interval as in previous plots. Key observations:
- **One-layer model:** trajectory stays roughly the same direction throughout training; no abrupt pivot.
- **Two-layer model:** trajectory abruptly pivots orthogonally at the phase change point.
- **Three-layer model:** trajectory similarly pivots orthogonally at the phase change point.
- The trajectory of models with more than one layer pivots orthogonally at the same point. [p. 12]

---
[p. 13 continued]

## Summary of co-occurring changes [p. 13]

In summary, the following things all co-occur during the same abrupt window:

- Capacity for in-context learning sharply improves (as measured via the in-context learning score).
- Induction heads form.
- Loss undergoes a small "bump" (that is, the loss curve undergoes a period of visibly steeper improvement than the parts of the curve before and after).
- The model's trajectory abruptly changes (in the space of per-token losses, as visualized with PCA). [p. 13]

Collectively these results suggest that some important transition is happening during the 2.5e9 to 5e9 token window early in training (for large models this is maybe 1-2% of the way through training). The authors call this transition "the phase change", in that it is an abrupt change that alters the model's behavior and has both macroscopic (loss and in-context learning curves) and microscopic (induction heads) manifestations, perhaps analogous to e.g. ice melting.^10 [p. 13]

## Looking at the Phase Change More Closely [p. 13]

A natural explanation would be that for all these models, the induction heads *implement* in-context learning: their formation is what drives all the other changes observed. To strengthen this hypothesis, a few things are checked. [p. 13]

First, the window where the phase change happens does not appear to correspond to a scheduled change in learning rate, warmup, or weight decay; there is not some known exogenous factor precipitating everything. [p. 13]

Second, some of the small models were trained on a different dataset, and the phase change developed in the same way (see Model Analysis Table for more details).^11 [p. 13]

Third, to strengthen the connection a little more, the authors look qualitatively and anecdotally at what is going on with the model's behavior during the phase change. One way to do this is to look at specific tokens the model gets better and worse at predicting. The model's loss is an average of billions of log-likelihood losses for individual tokens. By pulling them apart, one can get a sense for what has changed. [p. 13]

Concretely, the first paragraph of Harry Potter is used as an example. The differences in log-likelihoods are compared between the start and the end of the phase change.^12 The majority of the changes occur when tokens are repeated multiple times in the text. If a sequence of tokens occurs multiple times, the model is better at predicting the sequence the second time it shows up. On the other hand, if a token is followed by a different token than it previously was, the post-phase-change model is worse at predicting it. [p. 13]

---
[p. 14 continued]

**Figure 8** (p. 14): "PCA plot of per-token losses" (left) and "Per-token losses on Harry Potter" (right). Left panel: shows the PCA training trajectory with two points marked A and B, indicating before and after the phase change. An arrow shows the pivot direction. Right panel: the first paragraph of Harry Potter text with tokens highlighted. Tokens in green/teal highlight are tokens the model predicts *better* after the phase change (repeated sequences such as "Dursley", "Dursleys", "Potters", "small son"); tokens in red/orange highlight are tokens the model predicts *worse* after the phase change (cases where the same token is followed by a different token than previously, such as "Mrs Potter" where previous instances of "Mrs" were followed by "Dursley"). Below the text, examples are listed:
- When text is repeated, the post-phase-change model better predicts tokens: "Mrs Dursley" -> "Mrs Dursley", "the Potters" -> "the Potters", "a small son" -> "a small son"
- Cases where the same token is followed by a different token are given lower probability: "very large" vs "very useful", "didn't hold" vs "didn't think", "Mrs Dursley" vs "Mrs Potter" [p. 14]

The same analysis can be done over the course of model training. The loss curve is the average of millions of per-token loss curves, and it can be broken apart to look at the loss curves for individual tokens. [p. 14]

In particular, per-token loss trajectories are shown for two tokens in the first paragraph of Harry Potter. In red, a token whose prediction gets dramatically *better* during the phase change: the last of four tokens in "The Dursleys", a sequence that appears several times in the text. In blue, a token that gets meaningfully *worse* during the phase change: the first-ever appearance of "Mrs Potter", after both previous instances of "Mrs" were followed by "Dursley" instead. [p. 14]

**Figure 9** (p. 14): "Per-token losses over training." X-axis: elapsed training tokens (0 to 1e10). Y-axis: loss in nats/token (0.0 to 14.0). Two specific token loss trajectories are plotted, along with the mean loss curve (dashed gray line). The "phase change" interval is highlighted at the bottom.
- **"Mrs Potter" (blue line):** This token's loss *increases* during the phase change, because the model incorrectly predicts that the next token should be "D" from "Dursley". The loss rises from approximately 10 nats to approximately 12 nats during the phase change.
- **"The Dursleys" (red line, specifically the token "leys"):** This token's loss *decreases* during the phase change, because the model correctly predicts "leys" based on a previous example of "Dursleys". The loss drops dramatically from approximately 10 nats to approximately 2 nats during the phase change.
- The mean loss curve continues to decline smoothly. [p. 14]

All of this shows that during the phase change, exactly the behaviors one would expect to see if induction heads were indeed contributing the majority of in-context learning are observed. [p. 14]

---
[p. 15 continued]

## Assessing the Evidence [p. 15]

Despite all of the co-occurrence evidence above (and more in the Model Analysis Table), the fact remains that it has not been shown that induction heads *are* the primary mechanism for in-context learning. It has merely been shown that induction heads form at the same time as in-context learning, and that in-context learning does not improve thereafter. There are a number of potential confounds in this story. [p. 15]

### Arguments in favor of causal connection [p. 15]

- The formation of induction heads is correlated with a great increase in models' capacity for in-context learning, for a wide variety of models large and small.
- It is highly improbable these two sharp transitions would co-occur across so many models by pure chance, without any causal connection.
- There is almost surely some connection, and the simplest possibility is that induction heads are the primary mechanism driving the observed increase in in-context learning. (However, as discussed below, it could also be a confounding variable.)
- Since over 75% of final in-context learning forms in this window, one might naively believe this to be the amount of in-context learning that induction heads are responsible for. [p. 15]

### Confounds and reasons for caution [p. 15]

- In large models, there is low time resolution on the analysis over training. Co-occurrence when one only has 15 points in time is less surprising and weaker evidence.
- Perhaps other mechanisms form in the models at this point, that contribute to not only induction heads, but also other sources of in-context learning. (For example, perhaps the phase change is really the point at which the model learns how to compose layers through the residual stream, enabling both induction heads and potentially many other mechanisms that also require composition of multiple heads.) Put another way, perhaps the co-occurrence is primarily caused by a shared latent variable, rather than direct causality from induction heads to the full observed change in in-context learning.
- The fact that in-context learning score is roughly constant (at 0.4 nats) after the phase change does not necessarily mean that the underlying mechanisms of in-context learning are constant after that point. In particular, the metric used measures a *relative* loss between the token index 500 and 50, and the model's performance at token 50 improves over training time. Reducing the loss a fixed amount from a lower baseline is likely harder, and so may be driven by additional mechanisms as training time goes on.^13 ^14 [p. 15]

One point worth noting is that the argument that induction heads account for most in-context learning *at the transition point* of the phase change is more solid than the argument that they account for most in-context learning *at the end of training* -- a lot could be changing during training even as the in-context learning score remains constant. [p. 15]
