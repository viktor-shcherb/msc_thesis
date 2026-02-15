# Appendix C. Unsupervised Difficulty Bins [p. 21–23]

[p. 21–22] The authors compute difficulty bins without oracle ground-truth correctness information by averaging the PRM final-answer score over 2048 samples on each question, so as to obtain a value estimate corresponding to the question. They then bin the value for each question in the test-set into five quintiles (using the same procedure as the oracle difficulty bins). They refer to this as "predicted difficulty" rather than "oracle difficulty". Technically this procedure is extremely costly because it requires generating many samples. While they do not account for this cost in their analysis, in a practical production setting, this cost would be problematic. A more efficient approach would be to finetune a model to predict correctness directly, given the question. They do not explore this in their work, but leave such exploration of cheaper methods of estimating difficulty to future work.

[p. 22] In Figure 12 they plot PRM-search results using their difficulty bins, and in Figure 11 they plot the corresponding revision results. They see that in both settings these predicted bins demonstrate similar trends to the oracle bins.

**Figure 11** (p. 23): "Using our PaLM 2-S* PRM to compute difficulty bins without ground truth correctness information for revisions. On the left we plot verifier selection and on the right we plot majority selectionl We see largely similar performance trends with these bins as we do with the ground truth ones in Figures 7 and 10."

Description: Two-panel grouped bar chart
- Left panel ("Revisions Best-of-128 Weighted, Varying the Sequential to Parallel Ratio"): Grouped bar chart showing MATH Test Accuracy (%) across 5 unsupervised difficulty bins. Sequential to Parallel Ratio indicated by color gradient (10^-2 to 10^2). Bin 1 shows ~70-80% accuracy, declining to ~5-10% for bin 5.
- Right panel ("Revisions Majority@128, Varying the Sequential to Parallel Ratio"): Similar structure, showing accuracy across bins with different sequential/parallel ratios. Pattern similar to left panel with bin 1 at ~70% and bin 5 at ~5-10%.
- Notable patterns: Both selection methods show strong performance degradation from easier (bin 1) to harder (bin 5) questions, with color variation showing different ratio strategies perform differently across difficulty levels.
- Supports claim: Unsupervised difficulty bins (predicted from PRM scores) yield similar performance trends to oracle difficulty bins in Figures 7 and 10.

**Figure 12** (p. 23): "Using our PaLM 2-S* PRM to compute difficulty bins without ground truth correctness information for PRM search. We see largely similar performance trends with these bins as we do with the ground truth ones in Figure 3."

Description: Grouped bar chart
- Shows MATH Test Accuracy (%) across 5 test question bins (binned by unsupervised difficulty bins)
- Three search strategies compared: Beam Search (green), Best-of-N Weighted (orange/tan), Majority (pink)
- Bin 1: ~70-75% accuracy for all methods
- Bin 2: ~55-60% for beam search and best-of-N, ~40% for majority
- Bin 3: ~25-30% for beam/best-of-N, ~20% for majority
- Bin 4: ~10-15% for beam/best-of-N, ~5% for majority
- Bin 5: ~5-10% for all methods
- Notable patterns: Beam search and best-of-N weighted perform comparably and outperform majority voting across all difficulty bins; all methods show degradation with increasing difficulty.
- Supports claim: Unsupervised difficulty bins produce similar trends to oracle bins in Figure 3.
