# SmolLM3-3B: r_q vs r_k Phase Portraits at Selected Checkpoints

## File
`figure.png`

## What This Figure Shows

A 2x3 grid of scatter plots showing r_q (x-axis) versus r_k (y-axis) for PC0 at six representative SmolLM3-3B training checkpoints. Each point is one attention head. Dashed lines show the taxonomy classification thresholds (r = 0.3 and r = 0.7). The six checkpoints span the full training trajectory: S1-40K (earliest pre-training), S1-1.2M (early), S1-3.4M (end of stage 1), S3-4.7M (end of pre-training), LC1-20K (end of first long-context phase), LC2-20K (final checkpoint).

The progression is striking:

- **S1-40K**: Points are diffusely spread across the plane. A substantial cluster sits at low r_q (content-focused or weakly positional). The "phase space" is poorly organized.

- **S1-1.2M**: A dense cluster has formed at high r_q (0.7-0.95) with moderate r_k (0.3-0.8). The content-focused region (bottom-left) is nearly empty. The model has rapidly learned to encode Q-position.

- **S1-3.4M**: The cluster tightens slightly. A vertical stripe at high r_q with varying r_k is visible — some heads have coupled K to position, others haven't yet.

- **S3-4.7M**: Similar to S1-3.4M but with slightly more points at high r_k. The head population is consolidating toward the position-dominated corner.

- **LC1-20K**: The cluster shifts — r_q tightens further (most points above 0.8) while r_k shows a slightly wider spread. Some heads that had moderate r_k have moved to high r_k, while others have dropped.

- **LC2-20K**: Very similar to LC1-20K. The distribution has stabilized. The majority of heads occupy the position-dominated region (top-right), with a tail of mixed heads stretching toward lower r_k.

## How It Was Produced

1. **Data source**: `results/smollm3_training_progress/qk.csv`, filtered to PC0.

2. **Checkpoint selection**: Six checkpoints were chosen to represent key transitions: the earliest available (S1-40K), early stability (S1-1.2M), end of stage 1 (S1-3.4M), end of all pre-training (S3-4.7M), end of first LC phase (LC1-20K), and final checkpoint (LC2-20K).

3. **Visualization**: matplotlib 2x3 subplot grid. Each subplot shows all heads for one checkpoint as a scatter. Dashed lines at taxonomy thresholds. All subplots share the same axis limits (r_q: [-0.05, 1.05], r_k: [-1.05, 1.05]).

4. **Script**: `scripts/generate_report_figures.py`, function `smollm_fig07_rq_rk_scatter_grid()`.

## Key Takeaway

The phase portraits provide the most intuitive view of how the head population evolves during training. The progression from a diffuse cloud to a tight cluster in the position-dominated corner mirrors the taxonomy evolution statistics, but in a continuous rather than categorical way. The key observation is that the transition is not gradual and uniform — it happens in two jumps (early stage 1 and LC onset), with relatively stable plateaus in between. The LC phase reshapes the cluster shape (tighter r_q, wider r_k spread) rather than simply shifting it, consistent with the asymmetric Q/K response to long-context adaptation.
