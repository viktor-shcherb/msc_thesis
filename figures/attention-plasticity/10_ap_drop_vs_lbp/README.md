# AP_drop vs LongBench Pro Score

## File
`figure.png` / `figure.pdf`

## What This Figure Shows

Scatter plot of AP_drop (first 20% − last 20% plasticity) against LongBench Pro Overall score for the 7 models with both mechanistic and benchmark data. Points are colored by model family: Ministral (blue), Qwen (red), Llama (green). A linear trend line and Pearson correlation (r = −0.67) are shown.

The three model families form distinct clusters along the AP_drop axis: Ministral (~0.07), Qwen (~0.16–0.19), Llama (0.23). This ordering matches the LongBench Pro ranking. Within Qwen, larger models have smaller AP_drop and higher LBP scores.

## Key Takeaway

AP_drop — the rate at which attention plasticity degrades with context position — separates model families in the same ordering as benchmark performance. The correlation is moderate (r = −0.67) rather than strong because Ministral3-3B is a diagnostic outlier: flat plasticity (AP_drop = 0.072) but low benchmark score (30.18). This model has good attention mechanics but limited base capability, illustrating the decomposition: benchmark performance = base capability × context preservation. Plasticity measures the second factor.

## How It Was Produced

1. **Data source**: `model_report.csv` (AP_drop) and LongBench Pro Table 3 non-thinking scores.
2. **Script**: `generate.py` in this directory.
