# F Quantitative Analysis of Attention Sinks in Long Inputs [p. 18]

[p. 18]

Figures 2 and 13 illustrate the attention sink phenomenon using short sequences for clarity. Extending this analysis, Figure 12 demonstrates the distribution of attention scores (after SoftMax) towards the first token in lengthy inputs (sequence length of 4096). The authors average attention scores across 256 sequences, with each sequence comprising 4096 tokens. The plotted data represent the attention allocated by the 4096th token to the initial token in every layer.

Notably, the attention scores for the first token are significantly high, often exceeding half of the total attention, except for the two bottom layers. This observation empirically substantiates the preferential focus on the first token by the majority of layers and heads, irrespective of other tokens' distances within the sequence. Such a trend underscores the critical role of the initial tokens in a sequence, as their removal has a huge impact on language model performance due to a large portion of the denominator in the SoftMax function being removed. [p. 18]

**Figure 12** (p. 18): "Visualization of attention scores (after SoftMax) on the first token across layers in Llama-2-7B. Attention Scores are the 4096th token's attention towards the first token in each layer. The error bars are the standard deviation of the first token's attention scores across different heads in one layer. Results are averaged over 256 sentences, each having a length of 4096 tokens."

The figure is a scatter plot with error bars. X-axis: Layer ID (0 to ~31). Y-axis: Attention Score on the First Token (0.0 to 1.0). Key observations:
- Layers 0 and 1 have very low attention scores on the first token (near 0.0), shown as two isolated points at the bottom left.
- From layer 2 onward, the attention scores jump to approximately 0.6-0.9 and remain high across all subsequent layers.
- Most layers from ~4 onward show attention scores around 0.7-0.9 on the first token, with error bars indicating variability across heads.
- The pattern demonstrates that the first token consistently attracts a large share of total attention in virtually all layers except the bottom two.
