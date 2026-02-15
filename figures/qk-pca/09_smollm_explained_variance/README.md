# SmolLM3-3B: PC0 Explained Variance During Training

## File
`figure.png`

## What This Figure Shows

A line plot tracking the mean PC0 explained variance ratio across 10 SmolLM3-3B training checkpoints. The x-axis shows chronologically ordered checkpoints; the y-axis shows mean explained variance ratio. Shaded band shows +/- 1 standard deviation. Vertical dashed lines separate training phases.

The figure shows three distinct regimes:

1. **Early growth (step 40K to 1.2M)**: PC0 explained variance jumps from ~0.19 to ~0.29. The combined QK PCA rapidly identifies a dominant direction as the model learns to separate Q from K and encode position.

2. **Plateau (steps 1.2M to 4.72M)**: PC0 variance stabilizes around 0.29 through the remainder of pre-training (stages 1-3). The leading variance structure is established early.

3. **Long-context boost (LC phases)**: PC0 explained variance jumps to ~0.34 during long-context fine-tuning and stabilizes. The increase from 0.29 to 0.34 represents a 17% relative increase in variance concentration, indicating that long-context training creates a more pronounced low-rank structure in the combined QK space.

## How It Was Produced

1. **Data source**: `results/smollm3_training_progress/qk.csv`, filtered to PC0 (`pc == 0`).

2. **Aggregation**: For each checkpoint, mean and standard deviation of the `explained_variance` column across all heads.

3. **Script**: `scripts/generate_report_figures.py`, function `smollm_fig04_explained_variance_evolution()`.

## Key Takeaway

The variance concentration increase during long-context fine-tuning suggests that adapting to longer contexts makes the positional structure *more* dominant, not less. This is counterintuitive — one might expect that longer contexts require more diverse representational strategies. Instead, the model appears to consolidate its positional encoding into a tighter low-rank structure, potentially freeing higher PCs for content. Combined with the r_k drop during LC training, this paints a picture of specialization: PC0 becomes an even stronger Q/K separator and Q-position encoder, while K vectors redistribute their positional information.
