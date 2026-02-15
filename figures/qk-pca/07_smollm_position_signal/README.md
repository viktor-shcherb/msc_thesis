# SmolLM3-3B: Position Correlation on PC0 During Training

## File
`figure.png`

## What This Figure Shows

A line plot tracking mean r_q (blue, circles) and mean r_k (red, squares) on PC0 across 10 SmolLM3-3B training checkpoints. The x-axis shows checkpoints in chronological order (left to right: stage 1 pre-training, stage 2, stage 3, long-context 4K->32K, long-context 32K->64K). Shaded bands show +/- 1 standard deviation. Vertical dashed lines separate training phases.

The figure reveals two distinct dynamics:

**r_q (Q-position correlation)** increases monotonically throughout training:
- Starts at 0.67 at step 40K (already moderate — RoPE structure is partially present even early)
- Jumps sharply to 0.81 by step 1.2M (within the first third of stage 1)
- Continues climbing gradually through stages 2-3 (~0.84)
- Reaches ~0.87 during long-context fine-tuning and stabilizes

**r_k (K-position correlation)** follows a non-monotonic trajectory:
- Starts at 0.46 at step 40K
- Rises to ~0.53 during stage 1 and peaks at ~0.54 in stage 2
- **Drops** to ~0.46 during long-context fine-tuning phases

This Q/K asymmetry during long-context training is a key finding: the model strengthens Q-position encoding while partially decoupling K from position, potentially freeing K vectors to carry more content information for long-range retrieval.

## How It Was Produced

1. **Data source**: `results/smollm3_training_progress/qk.csv`, filtered to PC0 (`pc == 0`). Contains results from 10 SmolLM3-3B checkpoints, each analyzed with the same combined QK PCA pipeline as the cross-model analysis.

2. **Model**: SmolLM3-3B (`HuggingFaceTB/SmolLM3-3B-checkpoints`), 36 layers, 16 Q heads, 4 KV heads (GQA ratio 4). 300 Q heads sampled per checkpoint with seed 0.

3. **Checkpoints** (chronological order):
   - Stage 1: steps 40K, 1.2M, 2.4M, 3.44M (max_position_embeddings=4096, rope_theta=50000)
   - Stage 2: step 4.2M (same RoPE config)
   - Stage 3: step 4.72M (same RoPE config)
   - LC 4K->32K: steps 4K, 20K (max_position_embeddings=32768, rope_theta=2000000)
   - LC 32K->64K: steps 4K, 20K (max_position_embeddings=65536, rope_theta=5000000)

4. **Aggregation**: For each checkpoint, mean and standard deviation of r_q and r_k across all heads.

5. **Script**: `scripts/generate_report_figures.py`, function `smollm_fig01_position_signal_over_training()`.

## Key Takeaway

Positional structure in Q vectors emerges rapidly during early pre-training and continues strengthening throughout training. K-position encoding follows a different trajectory — it strengthens during pre-training but partially retreats during long-context fine-tuning. This asymmetry suggests that long-context training specifically reshapes the Q/K balance: the model learns to maintain strong Q-position encoding (for the positional bias mechanism) while allowing keys to become more content-oriented (potentially supporting better long-range retrieval). This connects directly to the attention plasticity framework: decoupling K from position increases the head's capacity for query-dependent key selection.
