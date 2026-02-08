# E Llama-2-7B Attention Visualization on Longer Sequences [p. 17]

[p. 17]

**Figure 11** (p. 17): "Visualization of the *average* attention logits in Llama-2-7B over 256 sentences, each with a length of 128."

The figure shows a 6-panel grid of attention logit heatmaps from Llama-2-7B across different layers, all using Head 0:
- (a) Layer 0 Head 0
- (b) Layer 6 Head 0
- (c) Layer 12 Head 0
- (d) Layer 18 Head 0
- (e) Layer 24 Head 0
- (f) Layer 30 Head 0

Each heatmap is a 128x128 matrix (sequence length 128). The axes represent token positions (0-120 on both axes). The heatmaps display the causal attention pattern (upper-right triangle is gray/masked). Across most layers (particularly layers 6-30), a prominent vertical red stripe is visible along the leftmost column, indicating that the initial tokens receive disproportionately high attention logits from all subsequent tokens. Layer 0 shows a more diffuse pattern. The color scales vary per panel, with attention logit values shown on the right-side color bars.

[p. 18]

Figure 2 visualizes the attention map of Llama-2-7B using short sequences (length of 16) for clarity. The authors further visualize the attention of Llama-2-7B on longer sequences (length of 128) in Figure 11. The observations on short sequences also hold on longer sequences, where the attention scores of the initial tokens are much higher than the rest of the tokens in most layers, regardless of the distance between the initial tokens and the tokens in the rest of the sequence. Because the longer the sequence, the thinner the attention sinks' scores are visualized on the heatmap. The authors further analyze the attention distribution on longer sequences (length of 4096) using a different method in Section F. [p. 18]
