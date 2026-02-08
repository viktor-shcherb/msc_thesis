# A. Switch for Attention [p. 27-28]

[p. 27]

Shazeer et al. (2018); Lepikhin et al. (2020) designed MoE Transformers (Shazeer et al., 2017) by adding MoE layers into the dense feedforward network (FFN) computations of the Transformer. Similarly, this work also replaced the FFN layer in the Transformer, but here the authors briefly explore an alternate design. They add Switch layers into the Transformer *Self-Attention* layers. To do so, they replace the trainable weight matrices that produce the queries, keys and values with Switch layers as seen in Figure 10.

Table 10 records the quality after a fixed number of steps as well as training time for several variants. Though the authors find improvements, they also found these layers to be more unstable when using bfloat16 precision and thus did not include them in the final variant.

[p. 28]

However, when these layers do train stably, the authors believe the preliminary positive results suggests a future promising direction.

**Figure 10** (p. 28): "Switch layers in attention. We diagram how to incorporate the Switch layer into the Self-Attention transformer block. For each token (here we show two tokens, x_1 = 'More' and x_2 = 'Parameters'), one set of weights produces the query and the other set of unique weights produces the shared keys and values. We experimented with each expert being a linear operation, as well as a FFN, as was the case throughout this work. While we found quality improvements using this, we found this to be more unstable when used with low precision number formats, and thus leave it for future work."

The figure shows two diagrams side by side. On the left, a standard Transformer block with a "Switching Self-Attention" layer is shown (input x goes through Switching Self-Attention, Add + Normalize, Feed Forward Layer, Add + Normalize, producing y). On the right, the detailed architecture is shown: for each token (x_1, x_2), positional embeddings are added, then a Router assigns each token to one of several FFN experts (FFN 1 through FFN 4) with different routing probabilities (p = 0.5 for x_1, p = 0.7 for x_2). The expert outputs produce separate Self-Attention Q, K, V matrices, which feed into the standard Self-Attention mechanism, then Add + Normalize, Feed-Forward Layer, Add + Normalize, producing outputs y_1 and y_2.

**Table 10: Switch attention layer results** (p. 28)

All models have 32 experts and train with 524k tokens per batch. "Experts FF" is when experts replace the FFN in the Transformer, which is the standard setup throughout the paper. "Experts FF + Attention" is when experts are used to replace both the FFN and the Self-Attention layers. When training with bfloat16 precision the models that have experts attention diverge.

| Model | Precision | Quality @100k Steps (up) | Quality @16H (up) | Speed (ex/sec) (up) |
|---|---|---|---|---|
| Experts FF | float32 | -1.548 | -1.614 | 1480 |
| Expert Attention | float32 | -1.524 | **-1.606** | 1330 |
| Expert Attention | bfloat16 | [diverges] | [diverges] | -- |
| Experts FF + Attention | float32 | **-1.513** | -1.607 | 1240 |
| Expert FF + Attention | bfloat16 | [diverges] | [diverges] | -- |
