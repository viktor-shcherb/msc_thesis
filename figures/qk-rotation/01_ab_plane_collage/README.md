# QK Scatter Collage in {a, b} Rotation Plane: Llama 3.2-3B

## File
`figure.png`

## What This Figure Shows

A 2x2 collage of scatter plots showing Q and K vectors projected onto the head-specific {a, b} rotation plane for 4 randomly sampled attention heads from Llama 3.2-3B (seed=42). In each subplot:

- **Blue points**: Q vectors, colored by position (light = early, dark = late)
- **Red points**: K vectors, colored by position (light = early, dark = late)
- **Horizontal axis**: axis a (drift/position direction)
- **Vertical axis**: axis b (Q-K separation direction)

Unlike the combined QK PCA (which finds directions of maximum variance), the rotation model constructs axes with specific geometric meaning: axis a captures *all* linear position covariance (a proportional to Cov(X, t)), and axis b maximizes Q-K separation in the orthogonal complement. The Orthogonal Drift Alignment Lemma guarantees that every direction perpendicular to a has exactly zero linear covariance with position.

The scatter pattern shows: (1) Q and K form two vertically separated clusters along axis b, (2) a smooth position gradient runs horizontally along axis a within both clusters, and (3) Q and K share the same position axis but are separated on the content/identity axis.

## How It Was Produced

1. **Data source**: Q and K vectors from `viktoroo/sniffed-qk` (HuggingFace Hub, revision `llama3.2-3b-longbench-pro-128k-plus`).

2. **Rotation construction**: For each head, `construct_rotation()` computes:
   - Axis a: unit vector proportional to Cov(X_pooled, position), where X_pooled is the concatenation of Q and K vectors
   - Axis b: top eigenvector of the projected difference covariance (I - aa^T) C_delta (I - aa^T), where C_delta = E[delta delta^T] and delta = q - k

3. **Tool**: `rotate-visualize --config configs/attention-plasticity/llama3.2-3b.yaml --collage --random --seed 42`

## Key Takeaway

The {a, b} plane provides a cleaner decomposition than PCA: axis a is *defined* to capture position (not just happen to correlate with it), and axis b is *defined* to separate Q from K. This makes the geometry interpretable: position bias arises from the interaction between the Q cluster mean on axis a (mu_Q^a) and the K drift slope (alpha_K), yielding the recency bias term mu_Q^a * alpha_K * j in the attention score.
