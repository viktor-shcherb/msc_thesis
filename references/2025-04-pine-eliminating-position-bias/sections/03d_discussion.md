# 3.4 Discussion [p. 6]

## Different Position Re-Assignment Methods

PINE puts documents with higher importance scores to a closer position to queries [p. 6]. Another option is to put documents with higher importance scores in a more distant position to the queries [p. 6]. Considering the recency bias brought by the most popular rotary position embedding (RoPE) (Su et al., 2024), this alternative approach makes RoPE "disrespect" the attention of models [p. 6]. Therefore, the authors believe this alternative choice is not optimal, which is justified by experiments in Section 4.3 [p. 6].

## Different Attention Masks

Previous work PCW (Ratner et al., 2023) adopts a different way: it masks the inter-document attention instead of making it bidirectional (Figure 3 middle and right) [p. 6]. Accordingly, it adopts a simplified position re-assignment method of ours: putting all documents in the same positions [p. 6]. However, masking all inter-document attention loses contextual information (the white part surrounded by colored blocks is enlarged). Moreover, some different tokens now share the same positions (Figure 3, right), which could confuse models [p. 6]. As a result, PCW performs poorly in language generation tasks (Section 4) [p. 6].

**Figure 3** (p. 6): "Previous work PCW (Ratner et al., 2023) eliminates position bias by first masking all inter-document attention and then re-assigning all documents the same positions."

Description: Three-panel diagram comparing attention mechanisms
- Key elements: Shows three stages with grid-based attention matrices. Same color scheme as Figure 2 (orange for SYS, blue shades for D₁/D₂/D₃, green for decoded tokens). Left panel shows "Attention Masking", middle panel shows "Equal Position", right panel shows the final result with position assignments.
- Notable patterns: The notions are kept the same as Figure 2. The experiment in Section 4 shows that PCW brings severe performance drop for tasks requiring language generation.
- Supports claim: Demonstrates why the previous PCW approach is suboptimal compared to PINE's bidirectional attention approach.

## Inference Cost

PINE incurs additional computation overhead due to extra operations [p. 6]. Practically, the extra big O computation complexity to obtain hidden states is O(nk log k), where n and k denote text length and the number of input documents, respectively [p. 6]. The bidirectional attention does not bring extra cost, the position re-assignment brings O(k log k) for each token since the sorting [p. 6].

---
[p. 6-7 continued]

The algorithms are involved [p. 7]. The real computation cost is acceptable since k is usually small (e.g., k = 2 in the LLM-as-a-judge task and k = 20 in the retrieval-augmented QA) [p. 7]. Section 4.5 shows results of real-world wall time and memory cost [p. 7].
