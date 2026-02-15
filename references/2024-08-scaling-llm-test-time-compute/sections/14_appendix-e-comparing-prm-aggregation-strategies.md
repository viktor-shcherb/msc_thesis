# Appendix E. Comparing PRM Aggregation Strategies [p. 24]

[p. 24] The authors compare different methods of aggregating per-step PRM scores to produce a final score for the full solution. Specifically they compare: 1) taking the minimum score across all steps as done in Lightman et al. [22] (e.g. "min"); 2) taking the product of all step correctness probabilities (e.g. "prod"); and 3) taking just the last step prediction (e.g. "last"). They see in Figure 13 that taking the last step outperforms the other two approaches. Prior works [22, 45] found min to be the best aggregator. They believe that the discrepancy is due to the fact that their verifier was trained with soft MC return labels, which surface very differently from binary correctness labels, and therefore other aggregation strategies may not have the same effect.

**Figure 13** (p. 24): "We compare different methods of aggregating per-step PRM scores to produce a final score for the full solution: 'min' refers to taking the minimum score across all steps, 'prod' takes the product of all step correctness probabilities, and 'last' just uses the last step score. We see that last performs the best across all aggregation strategies."

Description: Line plot comparing aggregation strategies
- X-axis: Number of Samples (log scale from 2^0 to 2^8)
- Y-axis: MATH Test Accuracy (%) ranging from ~10% to ~40%
- Five lines plotted: PRM min (blue), PRM prod (orange), PRM last (red), Base LM Majority (light blue), ORM (green)
- Notable patterns: All PRM variants and ORM show smooth scaling with number of samples; "PRM last" (blue) is the clear top performer (~37% at 2^8 samples); "Base LM Majority" (light blue) is below (~33%); "PRM min" (blue) and "ORM" (green) perform next best (~30%); "PRM prod" (orange) performs worst among PRM variants (~28%); all methods show logarithmic improvement with sample count.
- Supports claim: Last step aggregation outperforms min and prod aggregation strategies for the authors' soft-label trained PRM.

[p. 24] Interestingly, when using the last step aggregation, they are effectively using the PRM like an ORM. However, they see that the PRM still outperforms the ORM, suggesting that in their case the per-step PRM training may be largely useful as a form of representation learning, rather than purely as a tool at inference time. Future work should further explore this line of reasoning.
