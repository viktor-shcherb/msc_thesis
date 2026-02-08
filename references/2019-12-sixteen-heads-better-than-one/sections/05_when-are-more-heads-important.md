# 5 When Are More Heads Important? The Case of Machine Translation [p. 7-8]

[p. 7] As shown in Table 2, not all MHA layers can be reduced to a single attention head without significantly impacting performance. To get a better idea of how much each part of the transformer-based translation model relies on multi-headedness, the authors repeat the heuristic pruning experiment from Section 4 for each type of attention separately (Enc-Enc, Enc-Dec, and Dec-Dec).

**Figure 4** (p. 7): "BLEU when incrementally pruning heads from each attention type in the WMT model."
- X-axis: Percentage pruned (0%-100%). Y-axis: BLEU (0-35).
- Three lines: Enc-Enc (red circles), Enc-Dec (blue triangles), Dec-Dec (green squares).
- Performance drops much more rapidly when heads are pruned from the Enc-Dec attention layers.
- Pruning more than 60% of the Enc-Dec attention heads results in catastrophic performance degradation (BLEU drops to near 0).
- The encoder and decoder self-attention layers can still produce reasonable translations (BLEU scores around 30) with only 20% of the original attention heads.

Key finding: encoder-decoder attention is much more dependent on multi-headedness than self-attention.
