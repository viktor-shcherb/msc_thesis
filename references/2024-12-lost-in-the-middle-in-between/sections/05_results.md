# 5 Results [p. 4-5]

The results for instruction-tuned models are presented in Figure 2, while those for non-instruction-tuned models are shown in Figure 3. For a comprehensive view of all results, including instances where models performed suboptimally, please refer to Appendix A. We focus here on the most notable findings.

Specifically, Figures 2 and 3 illustrate the performance variations across the three models, with respect to each dataset, as we manipulate the placement of the relevant documents (e.g., positions 1 and 2, 5 and 6, etc.). Additionally, the figures compare model performance when using the full document, a summarized version, or knowledge graph triples extracted from the document. For each condition, we experiment with and without CoT prompting to assess its impact on model performance.

**Figure 2** (p. 5): "The performance impacts of varying the positions of relevant documents within instruction-tuned models' inputs, with context reduction techniques and Chain-of-Thought prompting. All positions are out of 20 total documents. KG + CoT results for gpt-3.5-turbo are omitted to Appendix A to highlight other results."

Description: Multi-panel line graph showing QA accuracy results
- Key elements: Six panels arranged in a 2x3 grid showing results for mpt-7b-8k-instruct (top row) and gpt-3.5-turbo-1106 (bottom row) across three datasets: HotpotQA (2-hop), 2WikiMultiHopQA (2-hop and 4-hop), and MuSiQue (2-hop, 3-hop, and 4-hop)
- X-axis: Evidence Positions (showing various position combinations like 0-1, 0-6, 0-10, etc.)
- Y-axis: Accuracy (percentage)
- Lines: Six different conditions shown with different colors and line styles:
  - Red solid: Full Doc.
  - Red dashed: Full Doc. + CoT
  - Green solid: Summary
  - Green dashed: Summary + CoT
  - Blue solid: KG
  - Blue dashed: KG + CoT
- Notable patterns:
  - Performance generally shows U-shaped curves with lowest accuracy when evidence is in middle positions
  - Full documents typically achieve highest accuracy
  - CoT prompting (dashed lines) shows variable effects depending on model and dataset
  - Context reduction (Summary, KG) generally reduces accuracy but can mitigate position effects
- Supports claim: Demonstrates the "lost in the middle" problem persists in multi-hop QA settings and varies by distance between evidence documents

Lastly, Figure 4 provides a detailed analysis of how the distance between relevant documents impacts model performance across different datasets.
