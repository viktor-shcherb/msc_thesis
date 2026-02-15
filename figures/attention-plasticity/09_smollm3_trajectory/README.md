# SmolLM3-3B Plasticity Trajectory Across Training

## File
`figure.png` / `figure.pdf`

## What This Figure Shows

Two-panel plot tracking attention plasticity and positional bias across 10 SmolLM3-3B training checkpoints, spanning pre-training (4K context, 6 checkpoints) and long-context extension (4K→32K→64K, 4 checkpoints).

**Top panel**: AP_first_20% (blue) and AP_last_20% (red) with the gap between them shaded (AP_drop, purple). During pre-training, both lines decline together — the gap stays narrow (~0.04–0.06). At the LC extension boundary, the lines diverge: AP_first_20% recovers to early-training levels (~0.59), while AP_last_20% plummets to ~0.43. The shaded gap triples from ~0.06 to ~0.16.

**Bottom panel**: bias_strength (from rotation analysis) as bars. Bias grows steadily during pre-training (0.009→0.019), then collapses 10× at LC extension onset (0.019→0.002).

## Key Takeaway

Bias collapse at LC extension onset recovers near-position plasticity (first 20% of context) but fails to recover distant-position plasticity (last 20%). The widening gap despite near-zero bias is the visual signature of the "necessary but not sufficient" finding: bias reduction alone does not ensure flexible attention at distance. The residual AP_drop after bias collapse reflects content signal decay — a mechanism independent of positional bias.

## How It Was Produced

1. **Data source**: `smollm3_model_report.csv` (plasticity) and `smollm3_training_progress/rotated.csv` (rotation bias_strength).
2. **Script**: `generate.py` in this directory.
