# Appendix H: Recurrent Memory Transformer Analysis [p. 22]

To understand how recurrent models consistently retain their performance over extremely long sequences, we analyze RMT memory and attention patterns on the QA1 task. We evaluate RMT trained on 32 segments or approximately 16k tokens on a single sample with two facts, see Figure 8 (a) and (b). For both sequence lengths 16k and 128k the memory states exhibit a consistent pattern. In the absence of fact in input, the memory remains similar to its initial states, but the introduction of fact leads to visible change in the memory state. This indicates the model learned to distinguish important facts from distractor text and storing facts in memory. Memory attention maps (c) and (d) when RMT writes the fact to memory (c) and then reads it from memory (d). The intensity of red color corresponds to the amount of attention between the query on the left and key on the top. [p. 22]

**Figure 8** (p. 22): "RMT learns to detect and store relevant facts using memory. Heatmaps (a) and (b) represent pairwise distances between memory states on QA1 with context size 16k (a) and 128k (b). Distant states are marked with blue color and similar states with red. Change in memory mainly occurs when the model meets a new fact, which indicates model adaptation to distinguishing and storing facts in memory. Memory attention maps (c) and (d) when RMT writes the fact to memory (c) and then reads it from memory (d). The intensity of red color corresponds to the amount of attention between the query on the left and key on the top."

Description: Four heatmaps showing RMT memory analysis
- Key elements:
  - (a) Heatmap for 16k context showing pairwise distances between memory states, with segments 0-32 on both axes
  - (b) Heatmap for 128k context showing similar pattern with more segments (0-128)
  - (c) Memory attention map when writing facts to memory
  - (d) Memory attention map when reading facts from memory
  - Color scale: blue for distant states (0), red for similar states (150 for 16k, 175 for 128k)
- Notable patterns: Diagonal red pattern in (a) and (b) showing similar adjacent memory states. Distinct blue-red boundaries occur when new facts are encountered. Attention maps (c) and (d) show concentrated red regions indicating focused attention during fact writing and reading operations.
- Supports claim: RMT learns to distinguish important facts from distractor text and store them in memory, as evidenced by the visible changes in memory state when facts are encountered and the distinctive attention patterns during read/write operations.
