# D Analysis on the Inter-task Correlation on LongBench [p. 18]

**Figure 5** (p. 18): "Spearman correlation between each pair of task in LongBench."

A heatmap showing Spearman correlation coefficients between all 21 task-dataset pairs (labeled 1-1 through 6-2). The color scale ranges from -0.4 (blue) to 1.0 (red). Most within-category task pairs show high positive correlation (warm red/orange), while cross-category correlations are more variable.

[p. 18] The multi-task property of LongBench is analyzed by the inter-task correlation among and across each category of tasks. Most tasks within the same task category have a high correlation, except for PassageCount (5-1), which exhibits low correlation with almost all tasks since models perform poorly (almost random) on this challenging task. The correlations between Qasper (1-2), RepoBench-P (6-2) and the other tasks are also lower, which implies that these tasks potentially require a different attention pattern than the other tasks. Notably, tasks in the same language have a higher correlation with each other, e.g., a high correlation between Chinese tasks (1-4, 2-4, 3-4, 4-4, 5-3). These observations suggest that LongBench provides a more comprehensive evaluation result by integrating various types of tasks and languages.
