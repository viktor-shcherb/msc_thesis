# SmolLM3-3B: Head Taxonomy Evolution During Training

## File
`figure.png`

## What This Figure Shows

A stacked bar chart showing the fraction of heads in each taxonomy category (position-dominated, Q-positional, K-positional, content-focused, mixed) across 10 SmolLM3-3B training checkpoints. The x-axis shows chronologically ordered checkpoints; the y-axis shows fraction of heads (0 to 1). Vertical dashed lines separate training phases.

The figure reveals two major transitions in head specialization:

**Early specialization (stage 1, steps 40K to 1.2M):**
- Position-dominated heads jump from 34% to 55%
- Content-focused heads collapse from 11% to under 1%
- Mixed heads shrink from 54% to 38%

This rapid shift indicates that the model quickly learns to encode position in the leading PC. Content-focused heads — those where neither Q nor K position correlates strongly with PC0 — nearly vanish within the first third of pre-training.

**Long-context consolidation (LC phases):**
- Position-dominated heads jump again from ~58% to ~71%
- Q-positional heads drop from ~11% to ~3%
- Mixed heads continue declining to ~26%

The conversion of Q-positional heads to position-dominated during long-context training is particularly notable: it means heads that previously encoded position only in Q are now encoding it in K as well, despite the overall r_k drop seen in the position signal figure. This apparent contradiction resolves when considering that Q-positional→position-dominated conversion affects a minority of heads, while the r_k drop reflects a broader, subtler trend across all heads.

## How It Was Produced

1. **Data source**: `results/smollm3_training_progress/qk.csv`, filtered to PC0 (`pc == 0`).

2. **Classification**: Each head is classified based on its PC0 r_q and |r_k| using thresholds of 0.7 (high) and 0.3 (low):
   - Position-dominated: r_q > 0.7 AND |r_k| > 0.7
   - Q-positional: r_q > 0.7 AND |r_k| < 0.3
   - K-positional: r_q < 0.3 AND |r_k| > 0.7
   - Content-focused: r_q < 0.3 AND |r_k| < 0.3
   - Mixed: everything else

3. **Aggregation**: For each checkpoint, count heads in each category and normalize to fractions.

4. **Visualization**: matplotlib stacked bar chart with category-specific colors (blue for position-dominated, indigo for Q-positional, pink for K-positional, green for content-focused, gray for mixed).

5. **Script**: `scripts/generate_report_figures.py`, function `smollm_fig03_taxonomy_evolution()`.

## Key Takeaway

The taxonomy evolution shows that positional specialization is a progressive, multi-stage process. The model first establishes Q-position encoding (killing content-focused heads), then gradually strengthens K-position coupling (converting Q-positional and mixed heads to position-dominated). Long-context fine-tuning accelerates this second transition. By the final checkpoint, 71% of heads are position-dominated on PC0, meaning the majority of attention heads have both strong Q-position and strong K-position signals — suggesting most heads implement a position-dependent attention bias through the alpha*beta interaction term.
