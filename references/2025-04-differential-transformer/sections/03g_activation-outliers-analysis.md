# 3.7 Activation Outliers Analysis [p. 9]

In large language models, a subset of activations manifests with significantly larger values compared to the majority, a phenomenon commonly called activation outliers (Bondarenko et al., 2024; Sun et al., 2024) [p. 9]. The outliers result in difficulties for model quantization during training and inference [p. 9]. The authors demonstrate that DIFF Transformer can reduce the magnitude of activation outliers, potentially allowing lower bit-widths for quantization [p. 9].

## Statistics of Largest Activation Values [p. 9]

Table 5 presents the statistics of activation values collected from Transformer and DIFF Transformer models trained in Appendix B [p. 9]. They analyze two types of activations, including attention logits (i.e., pre-softmax activations), and hidden states (i.e., layer outputs) [p. 9]. The statistics are gathered from 0.4M tokens [p. 9]. As shown in Table 5, although the median values are of similar magnitude, DIFF Transformer exhibits much lower top activation values compared to Transformer [p. 9]. The results indicate that their method produces fewer activation outliers [p. 9].

| Model | Activation Type | Top-1 | Top-2 | Top-3 | Top-10 | Top-100 | Median |
|-------|-----------------|-------|-------|-------|--------|---------|--------|
| Transformer | Attention Logits | 318.0 | 308.2 | 304.9 | 284.7 | 251.5 | 5.4 |
| DIFF | Attention Logits | 38.8 | 38.8 | 37.3 | 32.0 | 27.4 | 3.3 |
| Transformer | Hidden States | 3608.6 | 3607.4 | 3603.6 | 3552.1 | 2448.2 | 0.6 |
| DIFF | Hidden States | 1688.2 | 1672.5 | 1672.1 | 1624.3 | 740.9 | 1.2 |

Table 5: Largest activation values in attention logits and hidden states [p. 9]. Top activation values are considered as activation outliers, due to their significantly higher magnitude than the median [p. 9]. DIFF Transformer mitigates outliers compared to Transformer [p. 9].

## Quantization of Attention Logits [p. 9]

As shown in Figure 8, the authors quantize the attention logits to lower bits [p. 9]. They apply dynamic post-training quantization using absmax quantization (Wan et al., 2024) [p. 9]. The 16-bit configuration represents the original results without quantization [p. 9]. The models are quantized to 8 bits, 6 bits, and 4 bits [p. 9]. Figure 8 reports the zero-shot performance on HellaSwag (Gao et al., 2023) [p. 9]. The other datasets follow a similar trend [p. 9]. DIFF Transformer retains high performance even at reduced bit-widths, ranging from 16 bits to 8 bits [p. 9]. In comparison, Transformer's accuracy significantly drops with 6-bit quantization [p. 9]. The 4-bit DIFF Transformer achieves comparable accuracy as the 6-bit Transformer, and outperforms the 4-bit Transformer by about 25% in accuracy [p. 9]. The results indicate that DIFF Transformer natively mitigates activation outliers in attention scores, providing new opportunities for low-bit FlashAttention (Dao et al., 2022) implementations [p. 9].

**Figure 8** (p. 9): "Zero-shot accuracy on the HellaSwag (Gao et al., 2023) dataset. We quantize the attention logits from 16 bits (i.e., unquantized) to 8 bits, 6 bits, and 4 bits."

Description: Line plot showing quantization performance
- X-axis: # Bits (from 16 to 4, right to left: 16, 8, 6, 4)
- Y-axis: Accuracy (%) from 40 to 70
- Two curves: Diff (Ours) (orange) and Transformer (black)
- Label at top: "HellaSwag"
- Diff (Ours) maintains ~65% accuracy from 16-bit down to 6-bit, drops to ~60% at 4-bit
- Transformer maintains ~65% from 16-bit to 8-bit, drops sharply to ~50% at 6-bit, and ~40% at 4-bit
- Both curves start at approximately same point at 16 bits
- Diff shows much more graceful degradation under quantization
- Supports claim: DIFF Transformer achieves comparable 4-bit performance to 6-bit Transformer, and outperforms 4-bit Transformer by about 25% in accuracy [p. 9]
