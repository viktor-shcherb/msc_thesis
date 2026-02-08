# 3 Model Architecture [p. 3]

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. The encoder maps an input sequence of symbol representations (x_1, ..., x_n) to a sequence of continuous representations **z** = (z_1, ..., z_n). Given **z**, the decoder generates an output sequence (y_1, ..., y_m) one element at a time. At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next. [p. 2-3]

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder. [p. 3]

## Figures

**Figure 1** (p. 3): `"The Transformer - model architecture."`
Shows the full encoder-decoder architecture. Left half: encoder stack with N x layers, each containing Multi-Head Attention followed by Feed Forward, both with Add & Norm residual connections. Input Embedding + Positional Encoding feeds into the encoder. Right half: decoder stack with N x layers, each containing Masked Multi-Head Attention, Multi-Head Attention (attending to encoder output), and Feed Forward, all with Add & Norm. Output Embedding (shifted right) + Positional Encoding feeds into the decoder. Final output passes through a Linear layer and Softmax to produce Output Probabilities. [p. 3]

## 3.1 Encoder and Decoder Stacks [p. 3]

**Encoder:** Composed of a stack of N = 6 identical layers. Each layer has two sub-layers:
1. Multi-head self-attention mechanism
2. Simple, position-wise fully connected feed-forward network

A residual connection [11] is employed around each of the two sub-layers, followed by layer normalization [1]. The output of each sub-layer is LayerNorm(x + Sublayer(x)), where Sublayer(x) is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension d_model = 512. [p. 3]

**Decoder:** Also composed of a stack of N = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Residual connections around each sub-layer, followed by layer normalization (same as encoder). The self-attention sub-layer in the decoder stack is modified to prevent positions from attending to subsequent positions. This masking, combined with the fact that the output embeddings are offset by one position, ensures that the predictions for position i can depend only on the known outputs at positions less than i. [p. 3]
