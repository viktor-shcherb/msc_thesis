# Appendix K: Analysis of LLM Performance for Different Locations of the Supporting Facts [p. 26]

Fig. 10 shows the evaluation result of the GPT-4-Turbo model when all the facts in task are located in the same quarter of the input query. It is seen that the performance of the model is not the same for different locations of the supporting facts. The most difficult location to identify the facts is in the middle of context which corresponds to the depth = 50 in the Fig. 10. [p. 26]

**Figure 10** (p. 26): "Evaluation results for GPT-4-Turbo with different locations of the facts in the QA1 task."

Description: Heatmap showing performance by fact location and context length
- Key elements:
  - Y-axis: Task showing "qa1 (depth = X)" where X is 75, 50, 25, 0 (representing quarters of the context)
  - X-axis: Context length in tokens (4k, 8k, 16k, 32k, 64k)
  - Color scale: Green (100) to red (0), representing accuracy percentage
- Notable patterns:
  - qa1 (depth = 75): 96, 88, 68, 40, 32 - steady decline with context length
  - qa1 (depth = 50): 100, 92, 44, 24, 36 - sharp drop at longer contexts
  - qa1 (depth = 25): 100, 92, 72, 44, 32 - similar pattern to depth=75
  - qa1 (depth = 0): 92, 100, 80, 64, 20 - most variable performance
  - Middle position (depth = 50) shows worst performance at 16k+ tokens
  - All positions show degradation as context length increases
- Supports claim: Performance varies significantly by fact location, with middle positions (depth = 50) being most difficult to process, especially at longer context lengths.
