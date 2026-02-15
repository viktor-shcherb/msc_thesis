# Effects of data distribution $p_{\text{Data}}$ on attention sink [p. 6]

[p. 6]

## Training data amount [p. 6]

In the default setup, we consider 5B tokens. We wonder whether the attention sink emerges if we further constrain the data within a fixed compute budget. Therefore, we constrain the training data to 5B, 2.5B, 500M, 200M, 100M, and 50M. Meanwhile, we fix the batch size and optimization steps. As visualized in Figure 5(*Right*), with less training data, attention sink disappears. Further evidence in Figure 28 shows that this is not related to overfitting [p. 6].

## Randomness in data distribution [p. 6]

After packing documents into chunks, we re-sample the first token within the chunk $x_1 \sim \text{Uniform}(\mathcal{V})$. The trained LM has the metric $\text{Sink}_1^\epsilon = 27.03\%$, even larger than the default setup. This further verifies the semantic information of the sink token. We also consider $x_1, x_2 \sim \text{Uniform}(\mathcal{V})$, and we find attention sink shifts to the second token with $\text{Sink}_2 = 14.08\%$ while the attention sink on the first token is much less obvious $\text{Sink}_1 = 1.98\%$. But when only sample $x_2 \sim \text{Uniform}(\mathcal{V})$, the attention sink still always appears on the first token ($\text{Sink}_1 = 20.99\%$). Additionally, we find with more random tokens during pre-training, attention sink tends to disappear [p. 6].

## Fixing token in a specific position [p. 6]

Xiao et al. (2023b) considered a learnable token in the first token position within each chunk, which can be considered as $x_1 \sim \mathbb{I}(x = x_{\text{fix}})$. We also consider fixing the token $x_{\text{fix}}$ in the second/third token position during pre-training. Consequently, the attention sink always appears in the fixed token instead of the first token, as shown in Table 10(*Right*) [p. 6].

**Takeaways** (from box on p. 7, top):
1. Attention sink emerges after LMs are trained on sufficient training data
2. Attention sink could be shifted to other positions rather than the first token if modifying $p_{\text{data}}$
