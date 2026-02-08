# 4 Analysis and Discussion [p. 4–5]

## Qualitative analysis of attention visualizations

[p. 4] Figure 1 depicts raw attention, attention rollout, and attention flow for a correctly classified example across different layers. The first layer of attention rollout and attention flow are the same, and their only difference with raw attention is the addition of residual connections. As we move to the higher layers, the residual connections fade away. Moreover, in contrast to raw attention, the patterns of attention rollout and attention flow become more distinctive in the higher layers.

**Figure 1** (p. 2): "Visualisation of attention weights."
Three panels showing (a) Embedding attentions, (b) Attention rollout, (c) Attention flow, depicted as directed graphs with node-to-node connections across layers. Demonstrates that rollout and flow produce more structured, distinctive attention patterns in higher layers compared to raw attention.

**Figure 3** (p. 4): "Attention maps for the `CLS` token."
Shows heatmaps for three views (raw attention, attention rollout, attention flow) of the `CLS` embedding over input tokens (x-axis) across all 6 layers (y-axis) for three examples.

[p. 4] Three examples are analyzed:
1. The same example as in Figure 1 (correctly classified)
2. "*the article on NNP large systems <?>*" -- correctly classified; changing "article" to "articles" flips the model's decision
3. "*here the NNS differ in that the female <?>*" -- a miss-classified example; changing "NNS" (plural noun) to "NNP" (singular proper noun) flips the model's decision

For all cases, the raw attention weights are almost uniform above layer three.

Figures 2 and 3 together show that raw attention weights are almost uniform above layer three, while rollout and flow remain distinctive. (Figure 2 is documented in 02_setups-and-problem-statement.md.)

## BERT pronoun resolution examples

[p. 5] **Figure 4** (p. 4–5): "Bert attention maps."
Shows attention weights from the `mask` embedding for two potential references in coreference resolution:
- (a) "*The author talked to Sara about* `mask` *book.*" -- bars at left show relative predicted probability for "her" vs "his"; attention maps show raw attention, attention rollout, and attention flow weights over "author" and "Sara"
- (b) "*Mary convinced John of* `mask` *love.*" -- bars at left show relative predicted probability for "her" vs "his"; attention maps show weights over "Mary" and "John"

In the correctly classified example (a), both attention rollout and attention flow are consistent with each other and the prediction of the model. The final layer of raw attention does not seem consistent with the prediction, and varies a lot across different layers.

In example (b), only attention flow weights are consistent with the prediction of the model.

## Comparison of rollout and flow

[p. 4] The main difference between attention rollout and attention flow is that attention flow weights are amortized among the set of most attended tokens, as expected. Attention flow can indicate a set of input tokens that are important for the final decision, but without sharp distinctions among them. On the other hand, attention rollout weights are more focused compared to attention flow weights.

## Quantitative results on verb number prediction

[p. 4–5] As shown in Tables 1 and 2, both attention rollout and attention flow are better correlated with blank-out scores and input gradients compared to raw attention, but attention flow weights are more reliable than attention rollout.

> "The difference between these two methods is rooted in their different views of attention weights. Attention flow views them as capacities, and at every step of the algorithm, it uses as much of the capacity as possible. Hence, attention flow computes the maximum possibility of token identities to propagate to the higher layers. Whereas attention rollout views them as proportion factors and at every step, it allows token identities to be propagated to higher layers exactly based on this proportion factors. This makes attention rollout stricter than attention flow, and so we see that attention rollout provides us with more focused attention patterns." [p. 5]

However, since many simplifying assumptions are being made, the strictness of attention rollout does not lead to more accurate results, and the relaxation of attention flow seems to be a useful property.

## DistillBERT on SST-2

[p. 5] The authors also apply attention flow and attention rollout on two pretrained BERT models from https://github.com/huggingface/transformers.

**Table 3** (p. 4): SpearmanR correlation of attention based importance with input gradients for 100 samples from the test set for the DistillBERT model fine tuned on SST-2.

|         | L1             | L3             | L5             | L6             |
|---------|----------------|----------------|----------------|----------------|
| Raw     | 0.12 +/- 0.21  | 0.09 +/- 0.21  | 0.08 +/- 0.20  | 0.09 +/- 0.21  |
| Rollout | 0.11 +/- 0.19  | 0.12 +/- 0.21  | 0.13 +/- 0.21  | 0.13 +/- 0.20  |
| Flow    | 0.11 +/- 0.19  | 0.11 +/- 0.21  | 0.12 +/- 0.22  | 0.14 +/- 0.21  |

Table 3 shows the correlation of the importance score obtained from raw attention, attention rollout, and attention flow from a DistillBERT (Sanh et al., 2019) model fine-tuned to solve "SST-2" (Socher et al., 2013), the sentiment analysis task from the GLUE benchmark (Wang et al., 2018). Even though for this model all three methods have very low correlation with the input gradients, attention rollout and attention flow are slightly better than raw attention.
