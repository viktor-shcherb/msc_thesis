# A Ablating All Heads but One: Additional Experiment [p. 11-12]

[p. 11] Tables 5 and 6 report the difference in performance when only one head is kept for any given layer. The head is chosen to be the best head on its own on a *separate* dataset.

**Table 5** (p. 12): "Best delta BLEU by layer on `newstest2014` when only the best head (as evaluated on `newstest2013`) is kept in the WMT model. Underlined numbers indicate that the change is statistically significant with p < 0.01."

| Layer | Enc-Enc | Enc-Dec | Dec-Dec |
|-------|---------|---------|---------|
| 1     | **-1.96** | 0.02  | 0.03    |
| 2     | **-0.57** | 0.09  | -0.13   |
| 3     | **-0.45** | **-0.42** | 0.00 |
| 4     | -0.30   | **-0.60** | -0.31 |
| 5     | -0.32   | **-2.75** | **-0.66** |
| 6     | **-0.67** | **-18.89** | -0.03 |

Underlined (statistically significant) entries: Layer 1 Enc-Enc (-1.96), Layer 2 Enc-Enc (-0.57), Layer 3 Enc-Enc (-0.45), Layer 3 Enc-Dec (-0.42), Layer 4 Enc-Dec (-0.60), Layer 5 Enc-Dec (-2.75), Layer 5 Dec-Dec (-0.66), Layer 6 Enc-Enc (-0.67), Layer 6 Enc-Dec (-18.89).

**Table 6** (p. 12): "Best delta accuracy by layer on the validation set of MNLI-matched when only the best head (as evaluated on 5,000 training examples) is kept in the BERT model. None of these results are statistically significant with p < 0.01."

| Layer | Delta Acc | Layer | Delta Acc |
|-------|-----------|-------|-----------|
| 1     | -0.01%    | 7     | 0.05%     |
| 2     | -0.02%   | 8     | -0.72%    |
| 3     | -0.26%   | 9     | -0.96%    |
| 4     | -0.53%   | 10    | 0.07%     |
| 5     | -0.29%   | 11    | -0.19%    |
| 6     | -0.52%   | 12    | -0.15%    |
