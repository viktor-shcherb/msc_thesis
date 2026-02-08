# D Compute Cost [p. 21–22]

[p. 21–22] The authors compare the runtime of their proposed methods in Table 11. The clipped softmax is only marginally more expensive compared to using vanilla softmax attention. The gated attention using the linear **G** adds the compute overhead between 3% and 8%, depending on the model. Adding weight decay on LayerNorm $\gamma$ for OPT and adding the LayerNorm after the patch embeddings for ViT had a negligible effect on the runtime.

The estimated compute cost of producing the main results in the paper is about 320 GPU days (on A100) and the total cost of the project (including preliminary experiments and ablation studies) is about 1400 GPU days.

**Table 11** (p. 22): "An overview of the runtime of the proposed methods, compared to the vanilla pre-training, measured in hours on Nvidia-A100 GPUs."

| Model | Vanilla | Clipped softmax | Gated attention (Linear / MLP) |
|-------|---------|-----------------|-------------------------------|
| BERT  | 92.8^{+/-1.2} | 93.6^{+/-0.8} | 97.7 / 119.1 |
| OPT   | 53.6^{+/-0.4} | 54.4^{+/-0.4} | 55.7 / 64.7 |
| ViT   | 101.8^{+/-0.3} | 104.0^{+/-0.7} | 110.8 / 122.9 |
