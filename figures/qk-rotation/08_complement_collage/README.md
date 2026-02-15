# Complement Subspace Collage: Llama 3.2-3B

## File
`figure.png`

## What This Figure Shows

A 5x6 grid of scatter plots showing 30 consecutive SVD-pair slices of the complement subspace (d-2 dimensions after removing axes a and b) for one randomly selected head from Llama 3.2-3B. Blue = Q vectors, red = K vectors, colored by token position.

The top SVD pairs reveal clear donut/ring patterns — these are RoPE rotation planes where position is encoded as the *angle* around the ring (theta = atan2(SVD_{2i+1}, SVD_{2i})). Computing the angle-position correlation yields |angle_r| up to 1.0 for many pairs. The patterns fade from crisp donuts in the top pairs to unstructured Gaussian blobs in the later pairs as RoPE frequencies exceed the Nyquist limit.

Crucially, Q and K are completely mixed on these rings: the same RoPE rotation is applied to both, so they overlap with ~50% classification accuracy.

## How It Was Produced

1. **Complement projection**: X_perp = X - (X @ a)a^T - (X @ b)b^T, then SVD on the centered pooled complement.
2. **Tool**: `rotate-visualize --config configs/attention-plasticity/llama3.2-3b.yaml --complement --random --seed 42`

## Key Takeaway

The complement of {a, b} is not structureless. It contains the *symmetric* component of RoPE — the rotation that is shared identically between Q and K. Since shared rotations cancel in the dot product q^T k, they contribute relative-position encoding (cos(theta_i - theta_j)) rather than absolute-position bias. Across all models, 18-29 of 30 SVD pairs per head are active rotation planes, capturing 44-89% of complement variance.
