# Where Induction Heads Form [p. 54-56]

[p. 54] This section examines where induction heads are located in models: whether they generally form in the second layer, the last layer, or somewhere else.

## Small Attention-Only Models [p. 55]

In the attention-only models, induction heads form in the last layer. [p. 55]

(In these plots, each point represents a head, colored by layer and arranged along the x-axis by depth in the model. The height of the point is the prefix matching score of that head.) [p. 55]

**Figures (small attention-only models):** Six scatter plots arranged in a 2x3 grid, labeled 1l-attn through 6l-attn. [p. 55]

- **1l-attn:** All heads near zero prefix matching score. X-axis: Head depth 0-10.
- **2l-attn:** A few heads in the later layers reach prefix matching scores of ~0.6-0.8. X-axis: Head depth 0-20.
- **3l-attn:** Several heads in the last layer reach prefix matching scores of ~0.6-0.8. X-axis: Head depth 0-30.
- **4l-attn:** One head in the last layer reaches ~0.75 prefix matching score. Most other heads near zero. X-axis: Head depth 0-40.
- **5l-attn:** Several heads in later layers reach ~0.5-0.7 prefix matching score. X-axis: Head depth 0-50.
- **6l-attn:** Several heads in the last layer reach ~0.6-0.8 prefix matching score. X-axis: Head depth 0-60.

All plots: Y-axis is prefix matching score (0.0 to 1.0). X-axis is "Head depth in model (total # heads)". In all cases, the high-scoring induction heads appear in the final layer of the model.

## Small Models with MLPs [p. 55]

In small models with MLPs, by the 5L and 6L size, the induction heads form more in the second-to-last layer. [p. 55]

**Figures (small models with MLPs):** Six scatter plots arranged in a 2x3 grid, labeled 1l-mlp through 6l-mlp. [p. 55]

- **1l-mlp:** All heads near zero prefix matching score. X-axis: Head depth 0-10.
- **2l-mlp:** A few heads reach prefix matching scores of ~0.7-0.8. X-axis: Head depth 0-15.
- **3l-mlp:** One head reaches ~0.7 prefix matching score. X-axis: Head depth 0-30.
- **4l-mlp:** A few heads reach ~0.6-0.8 prefix matching score, appearing in later layers. X-axis: Head depth 0-40.
- **5l-mlp:** Several heads in the later layers reach ~0.6-0.8 prefix matching score, with some appearing in the second-to-last layer. X-axis: Head depth 0-50.
- **6l-mlp:** Several heads reach ~0.6-0.9 prefix matching score, concentrated in the second-to-last layer. X-axis: Head depth 0-60.

All plots: Y-axis is prefix matching score (0.0 to 1.0). X-axis is "Head depth in model (total # heads)". The trend shows that as model depth increases, induction heads shift from the last layer to the second-to-last layer.

## Full-Scale Models [p. 55-56]

[p. 55-56] In the models in the full-scale sweep, induction heads form earlier. In fact, in 24L and 40L models the majority of induction heads form before the halfway point in model depth. [p. 55-56]

Note that in these plots, only a randomized sample of 100 heads (with selection biased towards those scoring highly on prefix matching) are shown as opaque dots; most of the datapoints are left translucent for ease of reading. [p. 56]

**Figures (full-scale models):** Six scatter plots arranged in a 2x3 grid, labeled full-4l through full-40l. [p. 56]

- **full-4l:** Several heads with prefix matching scores up to ~0.9, with one green-colored head (later layer) scoring highest. X-axis: Head depth 0-30.
- **full-6l:** A couple of heads reach prefix matching scores up to ~1.0. X-axis: Head depth 0-60.
- **full-10l:** Many heads with high prefix matching scores (up to ~1.0), distributed across model depth with a concentration in the first half. X-axis: Head depth 0-200.
- **full-16l:** Many heads reach prefix matching scores of 0.4-1.0, distributed broadly across the first half of model depth. X-axis: Head depth 0-500.
- **full-24l:** Many heads with high prefix matching scores, with the majority appearing before the halfway point (~500 of ~1000 total head depth). X-axis: Head depth 0-1000.
- **full-40l:** Many heads with high prefix matching scores, with the majority appearing before the halfway point (~750 of ~1500 total head depth). X-axis: Head depth 0-1500.

All plots: Y-axis is prefix matching score (0.0 to 1.0). X-axis is "Head depth in model (total # heads)". The key finding is that in larger models, induction heads form in earlier layers (before the midpoint), unlike in small models where they concentrate in the last or second-to-last layer.
