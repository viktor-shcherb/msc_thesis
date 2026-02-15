# Appendix B. Additional Revision Results [p. 21–22]

[p. 21] The authors plot additional results for majority selection using their PaLM 2-S* revision model in Figure 10. With majority selection, they see largely similar trends to those found in Figure 7 for verifier selection.

**Figure 10** (p. 22): "Varying the ratio of generation budget allocated to sequential verses parallel samples, using majority to select the answer, rather than the verifier. Left: Each line represents a fixed generation budget as the ratio is changed. We see that similar to the verifier case, in the majority case, there exists an ideal ratio of sequential to parallel test-time compute at a given budget. Right: Analyzing performance across difficulty bins, we see that the easier questions are mostly invariant the ratio of sequential to parallel, whereas on the harder questions there is an ideal ratio of sequential to parallel test-time compute."

Description: Two-panel figure with line plots and bar charts
- Left panel: Line plot showing MATH Test Accuracy (%) vs Sequential/Parallel Ratio, with multiple colored lines representing different generation budgets (ranging from 10^0 to 10^2 samples). Each line peaks around 2^-1 to 2^0 ratio.
- Right panel: Grouped bar chart showing MATH Test Accuracy (%) across 5 difficulty bins (binned by increasing difficulty level). Purple bars represent sequential samples, pink/orange bars represent parallel samples at different ratios (indicated by color gradient from 10^-2 to 10^2 Sequential to Parallel Ratio).
- Notable patterns: Performance peaks at intermediate sequential/parallel ratios; easier questions (bins 1-2) show ~60-80% accuracy relatively invariant to ratio; harder questions (bins 3-5) show lower accuracy (~0-30%) with more sensitivity to the sequential/parallel ratio.
- Supports claim: Similar trends to verifier selection (Figure 7) when using majority voting instead of verifier-based selection.
