# Argument 3: When we directly "knock out" induction heads in small models at test-time, the amount of in-context learning greatly decreases [p. 18-19]

## Strength of argument for sub-claims [p. 18]

|                      | Small Attention-Only | Small with MLPs  | Large Models |
|----------------------|----------------------|------------------|--------------|
| Contributes Some     | Strong, Causal       | Strong, Causal   |              |
| Contributes Majority | Strong, Causal       | Medium, Causal   |              |

Note: The Large Models column is left blank (grayed out in the original), indicating that ablation evidence is not available for large models. [p. 18]

## Overview of ablation approach [p. 18]

For the cases ablations cover, they are by far the strongest evidence. The basic argument is that knocking out induction heads decreases the amount of in-context learning observed in the models. By "knocking out" the authors mean that they remove a given attention head from the model at test time, doing a forward pass on the transformer without it. (See the methods section for exact details of how the ablation is done.) [p. 18]

The ablations presented show how attention heads contribute to in-context learning, but ablations can also be used to study how attention heads contribute to the overall behavior change that occurs during the phase change (see the Model Analysis Table). [p. 18]

## Ablation results [p. 18-19]

**Figure 11** (p. 18): "Ablation of attention heads and their contribution to in-context learning." A 2x3 grid of plots. Top row: "In-Context Learning Score" for one-layer, two-layer, and three-layer attention-only models. Bottom row: "Ablation to In-Context Learning Score" for the same three model sizes. X-axis for all: Elapsed Training Tokens (0 to 1e10). Key observations:

**Top row (In-Context Learning Score):**
- Y-axis ranges from 0.0 to -0.5.
- **One-layer model:** no phase change; in-context learning score stays flat around -0.1.
- **Two-layer model:** shows the characteristic phase change with in-context learning improving from approximately -0.15 nats to approximately -0.4 nats.
- **Three-layer model:** same phase change pattern.
- Annotation: "During the phase change in-context learning improves by ~250%, from ~-0.15 nats to ~-0.4 nats." [p. 18]

**Bottom row (Ablation to In-Context Learning Score):**
- Y-axis ranges from -0.15 to 0.15, with a dagger symbol indicating "contributes to in-context learning" for positive values.
- Each line represents a single attention head, colored by type: **pink** = previous token; **dark purple** = induction; **yellow-green** = other.
- **One-layer model:** labeled "one-layer model no change" -- ablation contributions stay near 0.0 for all heads throughout training.
- **Two-layer and three-layer models:** labeled "models with more than one layer have a phase change" -- induction heads (dark purple lines) show large positive ablation contributions that increase during the phase change, meaning their removal decreases in-context learning. Other heads show near-zero or slightly negative contributions.
- Annotation: "The attention heads which increase in-context learning are almost entirely **induction heads**. They form as in-context learning increases and drive its increase." [p. 18]

These plots are a small excerpt of the Model Analysis Table. See the methods section for exact details of how the ablation is done. [p. 18]

---
[p. 19 continued]

## Interpreting the ablation results [p. 19]

In fact, *almost all* the in-context learning in small attention-only models appears to come from these induction heads. This begins at the start of the phase change, and remains true through the end of training.^17 [p. 19]

Unfortunately, there are no ablations for the full-scale models.^18 For the models where ablations are available, the evidence is clearly dispositive that induction heads increase in-context learning (at least as the authors have chosen to evaluate it). But the question of whether they are the *primary* mechanism requires further consideration. [p. 19]

### Considerations on whether induction heads are the primary mechanism [p. 19]

- In attention-only models, in-context learning must essentially be a sum of contributions from different attention heads.^19 But in models with MLPs, in-context learning could also come from interactions between MLP and attention layers. While ablating attention heads would affect such mechanisms, the relationship between the effect of the ablation on in-context learning and its true importance becomes more complicated.^20 As a result, the authors state they cannot be fully confident that head ablations in MLP models give the full picture. [p. 19]

- The ablations measure the *marginal* effects of removing attention heads from the model. To the extent two heads do something similar and the layer norm before the logits rescales things, the importance of individual heads may be masked. [p. 19]

## Conclusion for Argument 3 [p. 19]

> All things considered, the authors "feel comfortable concluding from this that induction heads are the primary mechanism for in-context learning in small attention-only models, but see this evidence as only suggestive for the MLP case." [p. 19]
