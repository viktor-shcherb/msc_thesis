# 6 Analysis [p. 6]

## Proximity of relevant documents significantly affects performance [p. 6]

Figure 4 highlights a clear trend: models perform better when relevant documents are adjacent compared to when they are separated by distractor documents. This suggests that the spatial proximity of evidence is crucial for models to effectively retrieve and integrate information. When documents are adjacent, connections between them are more easily captured, potentially due to the model's attention mechanisms. In contrast, when distractors separate the relevant documents, the models struggle to retrieve and synthesize the necessary evidence, resulting in a drop in performance.

**Figure 3** (p. 6): "Experimental results for Llama-2-7b-longlora-8k-ft. Results for MuSiQue 3- and 4-hop splits are relegated to Appendix A due to exceedingly poor performance."

Description: Multi-panel line graph showing QA accuracy results for non-instruction-tuned model
- Key elements: Four panels showing results for HotpotQA (2-hop), MuSiQue (2-hop), 2WikiMultiHopQA (2-hop), and 2WikiMultiHopQA (4-hop)
- X-axis: Evidence Positions (showing various position combinations)
- Y-axis: Accuracy (percentage)
- Lines: Six different conditions shown:
  - Red solid: Full Doc.
  - Red dashed: Full Doc. + CoT
  - Green solid: Summary
  - Green dashed: Summary + CoT
  - Blue solid: KG
  - Blue dashed: KG + CoT
- Notable patterns:
  - Generally lower performance compared to instruction-tuned models
  - Extreme degradation with CoT prompting (sharp drops in dashed red lines)
  - More stable performance without CoT
  - Similar U-shaped curves showing position sensitivity
- Supports claim: Non-instruction-tuned models struggle with CoT-style reasoning and show different response patterns to prompting strategies

## Chain-of-Thought prompting yields mixed results [p. 6]

For instruction-tuned models such as MPT and GPT-3.5, CoT prompting with few-shot exemplars markedly improves performance compared to zero-shot settings in most scenarios. This improvement likely stems from the explicit reasoning steps provided by CoT, which help these models better structure their responses and navigate complex multi-hop reasoning tasks. However, for the non-instruction-tuned Llama 2 longlora model, CoT prompting leads to a sharp decline in performance. This discrepancy may stem from the model's inherent biases: it demonstrates a pronounced primacy bias, with little to no recency bias, leading to an over-reliance on the few-shot exemplars and improper integration of the actual task-specific context. This suggests that non-instruction-tuned models may require careful tuning or additional training to fully leverage CoT-style reasoning.

## Context reduction mitigates position biases but sacrifices accuracy [p. 6-7]

Figure 2 reveals that reducing context—whether through summarization or knowledge graph triple extraction—dampens the impact of the "lost in the middle" problem. Specifically, evidence located in the middle of the input achieves performance levels closer to those of edge-positioned evidence when using reduced context. This flattening of the performance curve suggests that context reduction alleviates the models' positional biases. However, this improvement comes at a cost: overall accuracy declines, particularly in instruction-tuned models like MPT and GPT-3.5. This drop is likely due to information loss during the context reduction process. Interestingly, the non-instruction-tuned Llama 2 longlora model benefits substantially from context reduction, suggesting that these methods can serve as a useful preprocessing step for less robust models.

**Figure 4** (p. 7): "Average question-answering accuracy for full document prompts by distance setting for GPT and MPT models. Performance with adjacent evidence documents is generally higher than when evidence documents are separated by distractor documents."

Description: Two bar charts comparing QA performance by distance setting
- Key elements:
  - (a) GPT 3.5 Turbo results (top chart)
  - (b) MPT 7b 8k Instruct results (bottom chart)
  - X-axis: Six datasets (HotpotQA 2-hop, MuSiQue 2-hop, MuSiQue 3-hop, MuSiQue 4-hop, 2Wiki 2-hop, 2Wiki 4-hop)
  - Y-axis: Avg. Accuracy (percentage, scale 0-100)
  - Two bar colors per dataset:
    - Red bars: "Adjacent Documents" (evidence documents placed next to each other)
    - Blue bars: "Separated Documents" (evidence documents separated by distractors)
- Notable patterns:
  - For GPT 3.5 Turbo: Adjacent documents consistently achieve ~2-5% higher accuracy across all datasets except 2Wiki 4-hop where performance is nearly identical (~90%)
  - For MPT 7b 8k Instruct: Adjacent documents show larger gains (~3-10% higher) on most datasets, with most pronounced difference on HotpotQA 2-hop (~50% vs ~42%)
  - Both models show smallest distance effect on 2Wiki 4-hop dataset
  - Overall accuracy varies significantly by dataset complexity (HotpotQA and MuSiQue harder than 2Wiki)
- Supports claim: Spatial proximity between relevant documents significantly affects multi-hop reasoning performance across different model architectures

---
[p. 7-8 continued]

## Summary of key findings [p. 8]

The paper's analysis underscores the complexity of the "Lost in the Middle" problem in multi-hop settings, extending beyond the single-hop scenarios that current mitigation strategies typically address. The findings reveal that model performance is not only influenced by the absolute positions of evidence documents but also by their relative positioning, highlighting a previously underexplored dimension of this problem.

Context-reduction techniques such as summarization and knowledge graph triple extraction show promise as potential solutions. However, the results indicate that these out-of-the-box approaches are insufficient to fully mitigate the issue, as they often lead to a trade-off between reducing positional bias and retaining critical information.

The disparity in performance improvements between instruction-tuned and non-instruction-tuned models suggests an opportunity to better align model architectures with task-specific reasoning demands. Investigating the potential of advanced prompting techniques, such as dynamic CoT, could enhance model performance, particularly for non-instruction-tuned models like Llama 2 longlora.

Finally, incorporating external memory mechanisms or augmenting model architectures to dynamically prioritize and retrieve relevant evidence could offer a path forward. Such modifications may allow models to better handle long-context reasoning challenges, reducing sensitivity to document positioning and improving overall robustness in multi-hop settings.

By addressing these directions, future research can move closer to resolving the challenges posed by dispersed evidence in multi-hop question answering and enhancing the capabilities of long-context language models in reasoning-intensive tasks.
