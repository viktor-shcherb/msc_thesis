# Appendix F: Robustness of In-Context Learning [p. 19]

As described in Section 3.5, they evaluate the robustness of in-context learning of Transformer and DIFF Transformer with permutations of the same in-context examples [p. 19]. They evaluate the 3B-size language models that are extended to 64K input length (Section 3.3) [p. 19].

Figure 11 provides comparisons on four datasets, with in-context examples randomly arranged [p. 19]. The evaluation protocol is the same as in Section 3.5 [p. 19]. The variance in accuracy of DIFF Transformer is consistently lower than that of Transformer, indicating greater robustness of DIFF Transformer for in-context learning [p. 19].

**Figure 11** (p. 19): "Robustness evaluation of in-context learning on four datasets. Accuracy is evaluated with order permutations of demonstration examples by sweeping random seeds. The dash lines represent the margin between the best and worst results. Demonstration examples are randomly arranged in the prompt."

Description: Four line charts arranged in a 2×2 grid, each showing accuracy (%) vs Random Seed (0-9)
- (a) TREC with 6 classes: Orange line (Diff Ours) fluctuates around 94.0% with variance of 4.0; black line (Transformer) fluctuates more widely between approximately 70-85% with variance of 19.0
- (b) TREC-fine with 50 classes: Orange line (Diff Ours) fluctuates around 80-90% with variance of 9.0; black line (Transformer) fluctuates between approximately 60-80% with variance of 24.0
- (c) Banking-77 with 77 classes: Orange line (Diff Ours) fluctuates around 75-80% with variance of 9.0; black line (Transformer) fluctuates between approximately 60-72% with variance of 13.0
- (d) Clinic-150 with 150 classes: Orange line (Diff Ours) fluctuates around 78-82% with variance of 6.0; black line (Transformer) fluctuates between approximately 72-80% with variance of 12.0
- Key elements: Two lines per chart - orange for "Diff (Ours)" and black for "Transformer"; dashed horizontal lines show margin between best and worst results
- Notable patterns: In all four datasets, DIFF Transformer (orange) shows consistently smaller variance (lower fluctuation) compared to Transformer (black), demonstrating superior robustness to order permutations
- Supports claim: DIFF Transformer has greater robustness for in-context learning across different random seeds and order permutations [p. 19]
