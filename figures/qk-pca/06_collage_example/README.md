# QK Scatter Collage: Llama 3.2-3B (Example)

## File
`figure.png`

## What This Figure Shows

A 2x2 collage of scatter plots showing the first two principal components (PC0 vs PC1) from the combined QK PCA for 4 randomly sampled attention heads from Llama 3.2-3B (seed=42). In each subplot:

- **Blue points**: Q vectors, colored by Q-position (light blue = early positions, dark blue = late positions)
- **Red points**: K vectors, colored by K-position (light red = early positions, dark red = late positions)
- **Text box**: Per-PC explained variance ratio, r_q (Q-position correlation), and r_k (K-position correlation)

The figure directly visualizes the two key structural properties revealed by the analysis:

1. **Q/K linear separability**: In every subplot, Q (blue) and K (red) form two clearly separated clusters along PC0. A single vertical threshold on PC0 can classify vectors as Q or K with near-perfect accuracy. This is the geometric manifestation of W_Q and W_K projecting inputs into distinct regions.

2. **Position gradient within clusters**: Within each cluster, a smooth cool-to-warm color gradient runs along the PC0 direction, indicating that token position varies quasi-linearly along PC0. The sign canonicalization ensures increasing position corresponds to increasing PC0 for Q vectors.

The scatter pattern varies across heads: some show tight clusters with strong position gradients (high r_q, high r_k), while others show more diffuse clusters with weaker position encoding. This per-head variation is what drives the taxonomy classification.

## How It Was Produced

1. **Head selection**: 4 Q heads were randomly sampled from Llama 3.2-3B's available heads using `random.Random(42).sample(targets, 4)`.

2. **Data loading**: For each selected Q head, the corresponding K head was derived via GQA mapping (k_head = q_head // q_per_kv_group, where q_per_kv_group=4 for Llama 3.2-3B). Both Q and K vectors were loaded from `viktoroo/sniffed-qk` (HuggingFace Hub, revision `llama-3.2-3b-longbench-pro-128k-plus`).

3. **Combined PCA**: Q and K vectors were concatenated and PCA was fitted on the pooled set (10 components, sklearn). Q and K subsets were projected separately through the shared components. This preserves q.k exactly.

4. **Visualization**: matplotlib scatter with truncated "Blues" colormap for Q and truncated "Reds" colormap for K. Point size 4, alpha 0.6, rasterized for performance. Position normalized to [0, 1] for coloring. Shared colorbars for Q-position and K-position.

5. **Tool**: `pca-visualize --config configs/attention_plasticity/llama3.2-3b.yaml --random --collage --qk --seed 42`

## Key Takeaway

This is the most intuitive visualization of the combined QK PCA findings. The two-cloud structure (Q and K separated on PC0) with position gradients running through each cloud is immediately visible. It makes the abstract statistics (Fisher discriminant ~44, r_q ~0.80) concrete: you can *see* that PC0 simultaneously encodes Q/K identity and token position.

This figure type exists for all 11 models in the analysis. Llama 3.2-3B was selected as the example because it has the highest position-dominated head fraction (50%) and shows the clearest two-cluster structure.
