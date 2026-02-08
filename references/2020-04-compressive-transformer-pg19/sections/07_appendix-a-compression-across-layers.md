# Appendix A: Compression Across Layers [p. 15]

[p. 15] The authors inspect the compression loss broken down by the layer index, to investigate whether there is a trend in network depth with how compressible the representations are. The compression loss here refers to the attention-reconstruction attention loss. This is plotted for a 24-layer trained model on Enwik8, and an 18-layer model trained on WikiText-103.

Key findings:
- The compression loss for character-based language modelling is about one order of magnitude lower than that of word-level language modelling.
- The first layer's representations are highly compressible.
- From then on there is no fixed trend.
- Some non-contiguous layers have a very similar compression loss (e.g. layers 4 & 6, 5 & 7), which suggests information is being routed from these layer pairs via the skip connection.

**Figure 6** (p. 15): "Model analysis. Compression loss broken down by layer."

The figure contains two box plots side by side:
- **Left panel (Enwik8):** x-axis shows layers 1-24, y-axis shows compression loss (0 to ~1.6e-3). Layer 1 has very low compression loss. Subsequent layers show higher and more variable compression loss, generally in the range of 4e-4 to 1.6e-3, with no clear monotonic trend.
- **Right panel (WikiText-103):** x-axis shows layers 1-18, y-axis shows compression loss (0 to ~1.6e-2). Layer 1 again has very low compression loss. Higher layers have compression losses roughly in the range of 4e-3 to 1.6e-2, about one order of magnitude higher than Enwik8. No clear monotonic trend with depth.
