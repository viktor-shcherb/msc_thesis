# Distribution of Scores [p. 56]

[p. 56] What is the distribution of heads' scores on the head activation evaluators?

The distribution is sharper in the small models than the full-size models. In both cases, heads with a positive prefix matching score are more likely to have a positive copying score, and this correlation is even stronger for the highest prefix matching scores. [p. 56]

(For models with more than 100 heads, a subset of heads is plotted, as seen in the opaque versus translucent datapoints immediately above.) [p. 56]

**Figure (Distribution of scores):** Two scatter plots side by side. [p. 56]

- **Left panel ("Small models"):** X-axis: Prefix matching (0.0 to 1.0). Y-axis: Copying (-1.00 to 1.00). Legend includes: 1l-mlp, 1l-attn, 2l-mlp, 2l-attn, 3l-mlp, 3l-attn, 4l-mlp, 4l-attn, 5l-mlp, 5l-attn, 6l-mlp, 6l-attn. Most heads cluster near (0, 0) or along the left edge. Heads with high prefix matching scores (>0.6) tend to also have high copying scores (>0.5). The distribution is relatively sharp with clear separation between induction heads and non-induction heads.

- **Right panel ("Full-size models"):** X-axis: Prefix matching (0.0 to 1.0). Y-axis: Copying (-1.00 to 1.00). Legend includes: full-4l, full-6l, full-10l, full-16l, full-24l, full-40l. More spread-out distribution compared to small models. Heads with high prefix matching scores still tend to have positive copying scores, but the relationship is noisier. Some heads with moderate prefix matching scores (~0.2-0.5) show a wide range of copying scores.

The figure supports the claim that prefix matching and copying scores are positively correlated, especially for the highest-scoring heads, and that this relationship is cleaner in small models than in full-scale models.
