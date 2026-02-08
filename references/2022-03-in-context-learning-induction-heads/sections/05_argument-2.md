# Argument 2: When we change the transformer architecture in a way that shifts when induction heads form or whether they can form, the dramatic improvement in in-context learning shifts in a precisely matching way [p. 16]

## Strength of argument for sub-claims [p. 16]

|                      | Small Attention-Only       | Small with MLPs            | Large Models               |
|----------------------|----------------------------|----------------------------|----------------------------|
| Contributes Some     | Medium, Interventional     | Medium, Interventional     | Weak, Interventional       |
| Contributes Majority | Medium, Interventional     | Medium, Interventional     | Weak, Interventional       |

## Motivation for an interventional experiment [p. 16]

One thing that falls short about Argument 1 is that the analysis is just observing induction heads and in-context learning co-vary; like any observational study, it is not as convincing as if one actively changed one thing and measured what happened to the other. In this section, a more "interventional" experiment is done, in which the model architecture is changed in a way that makes induction heads easier to form, and the effect on in-context learning is observed. The change makes a bigger difference for smaller models so is more convincing there, but also carries some amount of weight for larger models (see table above). [p. 16]

## Design of the experiment [p. 16]

The experiment starts with the observation (noted in the previous section) that the phase change and the corresponding improvement in in-context learning only occurs in transformers with more than one layer. This is what one would predict if induction heads were the mechanism for the majority of in-context learning: induction heads require a composition of attention heads, which is only possible with two or more layers.^15 [p. 16]

Of course, the observation about one-layer models is pretty weak evidence by itself. (One could imagine one-layer models being different from models with more layers in all sorts of ways.) But it suggests a more general line of attack. If induction heads are the mechanism behind the large improvement in in-context learning, that makes predictions about the minimum architectural requirements in order to achieve the observed improvement. For a standard transformer, the important thing is to have two attention layers. But that is only because the key vectors need to be a function of the attended token and the token before it. [p. 16]

## Smeared key architecture [p. 16]

A "smeared key" architecture is defined with a very simple modification that should make it easy for transformers of any depth to express induction heads. In the modified models, for each head *h*, a trainable real parameter $\alpha^h$ is introduced, which is used as $\sigma(\alpha^h) \in [0, 1]$ to interpolate between the key for the current token and previous token^16:

$$k_j^h = \sigma(\alpha^h) k_j^h + (1 - \sigma(\alpha^h)) k_{j-1}^h$$

Where $\sigma$ is the sigmoid function, $k_j^h$ is the key vector for token $j$ at head $h$, and $k_{j-1}^h$ is the key vector for the previous token. This allows each head to optionally smear its keys with the previous token's key, making it possible for a single attention layer to implement the induction head pattern (since the key now contains information about both the current and previous tokens). [p. 16]

## Predictions [p. 16]

The hypothesis that induction heads are the primary mechanism of in-context learning predicts that the phase change will happen in one-layer models with this change, and perhaps might happen earlier in models with more layers. If they are one of several major contributing factors, one might expect some of the in-context learning improvement to happen early, and the rest at the same time as the original phase change. [p. 16]

---
[p. 17 continued]

## Results [p. 17]

The results are in line with the predictions: when the smeared-key architecture is used, in-context learning does indeed form for one-layer models (when it did not before), and it forms earlier for two-layer and larger models. More such results can be seen in the Model Analysis Table. [p. 17]

**Figure 10** (p. 17): "Smeared key architecture results." A 2x2 grid of plots comparing Vanilla Models (top row) vs. Smeared Keys Models (bottom row), for One Layer (left column) and Two Layers (right column). X-axis: Elapsed Training Tokens (0 to 1e10). Y-axis: In-Context Learning Score (0.0 to -0.5). An annotation arrow indicates: "Switching from the standard transformer architecture to the 'smeared key' architecture causes the phase change **to happen in one-layer models** and **to happen earlier**." Key observations:
- **Vanilla, One Layer (top-left):** labeled "no phase change" -- the in-context learning score stays relatively flat, never dropping substantially below approximately -0.1.
- **Vanilla, Two Layers (top-right):** labeled "phase change" -- shows the typical abrupt drop in in-context learning score (from approximately -0.1 to approximately -0.4) during the phase change window.
- **Smeared Keys, One Layer (bottom-left):** labeled "phase change despite being one-layer" -- shows a phase change occurring, with in-context learning score dropping to approximately -0.4, which did not happen in the vanilla one-layer model.
- **Smeared Keys, Two Layers (bottom-right):** labeled "phase change occurs earlier than in baseline" -- shows the phase change occurring earlier than in the vanilla two-layer model.

These plots are an excerpt of the Model Analysis Table. [p. 17]

## Caveats for large models [p. 17]

However, the authors note one probably should not make too strong an inference about large models on this evidence. This experiment suggests that induction heads are the *minimal mechanism* for greatly increased in-context learning in transformers. But one could easily imagine that in larger models, this mechanism is not the whole story, and also this experiment does not refute the idea of the mechanism of in-context learning changing over the course of training. [p. 17]
