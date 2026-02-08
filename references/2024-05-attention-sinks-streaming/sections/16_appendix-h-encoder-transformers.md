# H Attention Sinks in Encoder Transformers [p. 20-21]

[p. 20]

The paper mainly explores the attention sink phenomenon observed in autoregressive, decoder-only language models like GPT and Llama. Building upon the insights from Section 3.1, the authors propose that this phenomenon likely extends to other Transformer architectures, including encoder models such as BERT (Devlin et al., 2019) and ViT (Dosovitskiy et al., 2021). This assumption stems from the fact that these models share a similar Transformer structure and utilize SoftMax attention mechanisms. [p. 20]

To substantiate this hypothesis, the authors analyze the attention patterns of BERT-base-uncased, as depicted in Figure 14. Their findings reveal that BERT-base-uncased exhibits the attention sink phenomenon, characterized by disproportionately high attention scores assigned to the `[SEP]` token in most layers. This indicates that the model consistently relies on the omnipresent `[SEP]` token as a focal point for attention. [p. 20-21]

Furthermore, concurrent research by Darcet et al. identifies similar attention spikes in Vision Transformers, attributed to random background patch tokens acting as "registers" for global image information. The authors contend that these "registers" are analogous to the attention sink phenomenon they observed, suggesting that this is a universal characteristic across all Transformer models. [p. 21]

**Figure 14** (p. 20): "Visualization of attention maps for sentence 'StreamingLLM can work on infinite-length texts without compromising efficiency and performance.' in BERT-base-uncased."

The figure shows a 12-panel grid (4 rows x 3 columns) of attention heatmaps for BERT-base-uncased layers 0 through 11, all using Head 0. Each heatmap has tokens on both axes: `[CLS]`, streaming, ##, ##m, can, work, on, infinite, length, texts, without, com, ##promising, efficiency, and, performance, `[SEP]`. Key observations:
- In many layers (particularly layers 6-11), the columns corresponding to `[CLS]` and especially `[SEP]` show notably higher attention scores (warm/red colors), indicating that most tokens attend heavily to these special tokens.
- Layer 0 shows a more diffuse attention pattern with some diagonal emphasis.
- The attention sink behavior intensifies in deeper layers, with `[SEP]` consistently drawing high attention from nearly all tokens.
- This is the encoder equivalent of the "attention sink" phenomenon: in autoregressive models initial tokens serve as sinks, while in bidirectional encoder models the omnipresent special tokens (`[CLS]`, `[SEP]`) serve the same role.
