# G Llama-2-70B Attention Visualization [p. 18-19]

[p. 18]

Figure 2 shows the attention visualization of Llama-2-7B; the authors further visualize the attention of Llama-2-70B in Figure 13. The observation on Llama-2-7B also holds on Llama-2-70B, where the attention scores of the initial tokens are much higher than the rest of the tokens in most layers. [p. 18-19]

**Figure 13** (p. 19): "Visualization of the *average* attention logits in Llama-2-70B over 256 sentences, each with a length of 16."

The figure shows a 20-panel grid (5 rows x 4 columns) of attention logit heatmaps from Llama-2-70B, covering layers across the model's depth with two heads each:
- (a) Layer 0 Head 0, (b) Layer 0 Head 1
- (c) Layer 8 Head 0, (d) Layer 8 Head 1
- (e) Layer 16 Head 0, (f) Layer 16 Head 1
- (g) Layer 24 Head 0, (h) Layer 24 Head 1
- (i) Layer 32 Head 0, (j) Layer 32 Head 1
- (k) Layer 40 Head 0, (l) Layer 40 Head 1
- (m) Layer 48 Head 0, (n) Layer 48 Head 1
- (o) Layer 56 Head 0, (p) Layer 56 Head 1
- (q) Layer 64 Head 0, (r) Layer 64 Head 1
- (s) Layer 72 Head 0, (t) Layer 72 Head 1

Each heatmap is a 16x16 matrix showing attention logits. The causal mask is shown as gray in the upper-right triangle. Across most layers, a strong vertical red/warm stripe is visible at the leftmost column (first token position), indicating high attention logits directed to the initial token from all subsequent positions. Layer 0 exhibits a distinctive pattern: Head 0 shows relatively uniform attention, while Head 1 shows a strong diagonal and initial-token pattern. From Layer 8 onward, the dominant blue coloring of the lower-triangular region contrasts with the red/warm first column, confirming the attention sink phenomenon scales to the 70B parameter model.
