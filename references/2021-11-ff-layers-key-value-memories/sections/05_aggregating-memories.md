# 5 Aggregating Memories [p. 5-6]

[p. 5] The discussion so far has been about the function of a single memory cell in feed-forward layers. This section addresses how information from *multiple* cells in multiple *layers* aggregates to form a model-wide prediction. The authors show that every feed-forward layer combines multiple memories to produce a distribution that is qualitatively different from each of its component memories' value distributions (Section 5.1). These layer-wise distributions are then combined via residual connections in a refinement process, where each feed-forward layer updates the residual's distribution to finally form the model's output (Section 5.2).

## 5.1 Intra-Layer Memory Composition

[p. 6] The feed-forward layer's output can be defined as the sum of value vectors weighted by their memory coefficients, plus a bias term:

$$y^l = \sum_i \text{ReLU}(x^l \cdot k_i^l) \cdot v_i^l + b^l$$

If each value vector v_i^l contains information about the target token's distribution, the question is how this information is aggregated into a single output distribution.

**Active memories:** The behavior of 4,000 randomly-sampled prefixes from the validation set is analyzed. The validation set is used (rather than the training set used to find trigger examples) since the goal is to characterize the model's behavior at inference time, not find the examples it "memorizes" during training.

A typical example triggers hundreds of memories per layer (10%-50% of 4096 dimensions), but the majority of cells remain inactive. Interestingly, the number of active memories drops towards layer 10, which is the same layer in which semantic patterns become more prevalent than shallow patterns, according to expert annotations (see Section 3, Figure 2).

**Figure 7** (p. 6): "The fraction of active memories (i.e., with positive memory coefficient) out of 4096 memories in every layer, for a random sample of 4,000 examples."

The figure is a box plot with layers 1-16 on the x-axis and "% of active memories" (0-100) on the y-axis. Layers 1-5 show median active memory fractions around 40-50%. From layers 6-10 the fraction drops, with layer 10 showing the lowest median around 10-15%. Layers 11-16 show slightly higher medians around 15-20%, with narrower interquartile ranges than the early layers.

**Compositional outputs:** While there are cases where a single memory cell dominates the output of a layer, the majority of outputs are clearly compositional. The number of instances where the feed-forward layer's top prediction is *different* from all of the memories' top predictions is counted. Formally:

$$\text{top}(h) = \text{argmax}(h \cdot E)$$

is a generic shorthand for the top prediction from the vocabulary distribution induced by the vector h, and the number of examples where the following condition holds is computed:

$$\forall i : \text{top}(v_i^l) \neq \text{top}(y^l)$$

Figure 8 shows that, for any layer in the network, the layer's final prediction is different than *every one* of the memories' predictions in at least ~68% of the examples. Even in the upper layers, where the memories' values are more correlated with the output space (Section 4), the layer-level prediction is typically not the result of a single dominant memory cell, but a composition of multiple memories.

The authors further analyze cases where at least one memory cell agrees with the layer's prediction, and find that (a) in 60% of the examples the target token is a common stop word in the vocabulary (e.g. "the" or "of"), and (b) in 43% of the cases the input prefix has less than 5 tokens. This suggests that very common patterns in the training data might be "cached" in individual memory cells, and do not require compositionality.

---
[p. 7 continued]

**Figure 8** (p. 7): "The fraction of examples in a random sample of 4,000 examples where the layer's prediction is different from the prediction of all of its memories."

The figure is a bar chart with layers 1-16 on the x-axis and "% examples with zero agreement" (0-100) on the y-axis. All layers show high fractions, with most layers between ~68% and ~90%. The bars are highest in the middle layers (around layers 5-9, reaching approximately 85-90%), and slightly lower in the early and late layers (around 68-80%).

## 5.2 Inter-Layer Prediction Refinement

[p. 7] While a single feed-forward layer composes its memories in parallel, a multi-layer model uses the residual connection **r** to *sequentially* compose predictions to produce the model's final output:^5

$$x^\ell = \text{LayerNorm}(r^\ell)$$
$$y^\ell = \text{FF}(x^\ell)$$
$$o^\ell = y^\ell + r^\ell$$

Footnote 5 [p. 7]: The residual propagates information from previous layers, including the transformer's self-attention layers.

The authors hypothesize that the model uses the sequential composition apparatus as a means to *refine* its prediction from layer to layer, often deciding what the prediction will be at one of the lower layers.

### Residual agreement with final output

[p. 7] To test this hypothesis, the authors first measure how often the probability distribution induced by the residual vector r^\ell matches the model's final output o^L (L being the total number of layers):

$$\text{top}(r^\ell) = \text{top}(o^L)$$

**Figure 9** (p. 7): "Fraction of examples in each layer, where the residual's top prediction matches the model's output."

The figure is a bar chart with layers 1-16 on the x-axis and "% examples s.t. the residual predicts the final output" (0-100) on the y-axis. The fraction starts near 0% at layer 1, increases gradually through layers 2-9 (reaching about 20-40%), then grows rapidly from layer 10 onwards. By layer 16, the fraction reaches approximately 95%.

Figure 9 shows that roughly a third of the model's predictions are determined in the bottom few layers. This number grows rapidly from layer 10 onwards, implying that the majority of "hard" decisions occur before the final layer.

### Confidence refinement

[p. 7-8] The probability mass p that each layer's residual vector r^\ell assigns to the model's final prediction is also measured:

$$w = \text{top}(o^L)$$
$$\mathbf{p} = \text{softmax}(r^\ell \cdot E)$$
$$p = \mathbf{p}_w$$

**Figure 10** (p. 7): "Probability of the token output by the model according to the residual of each layer."

The figure is a box plot with layers 1-16 on the x-axis and "probability" (0.0-1.0) on the y-axis. In layers 1-7, the median probability is very low (near 0.0), with some outliers reaching higher values. From layer 8 onward, the median probability steadily increases. By layers 14-16, the median probability is around 0.6-0.8, with many outliers reaching close to 1.0.

Figure 10 shows a similar trend but emphasizes that it is not only the top prediction's identity that is refined as we progress through the layers, it is also the model's confidence in its decision.

### Prediction change breakdown

[p. 8] To better understand how the refinement process works at each layer, the authors measure how often the residual's top prediction changes following its interaction with the feed-forward layer (top(r^\ell) != top(o^\ell)), and whether this change results from the feed-forward layer overriding the residual (top(o^\ell) = top(y^\ell)) or from a true composition (top(r^\ell) != top(o^\ell) != top(y^\ell)).

**Figure 11** (p. 8): "Breakdown of examples by prediction cases: the layer's output prediction matches the residual's prediction (*residual*), matches the feed-forward layer's prediction (*ffn*), matches both of the predictions (*agreement*), or none of the predictions (*composition*)."

The figure is a stacked bar chart with layers 1-16 on the x-axis and "% examples" (0-100) on the y-axis. Four categories are shown:
- *residual* (blue, largest portion): dominates across all layers, occupying roughly 60-85% in most layers.
- *agreement* (orange hatched): small portion, increasing slightly in upper layers.
- *composition* (green hatched): present as a small portion across layers.
- *ffn* (red): very small portion across all layers.

By construction, there are no cases where the residual matches the feed-forward layer's prediction and does not match the output's prediction.

[p. 8] In the vast majority of examples, the residual's top prediction ends up being the model's prediction (*residual*+*agreement*). In most of these cases, the feed-forward layer predicts something different (*residual*). Perhaps surprisingly, when the residual's prediction does change (*composition*+*ffn*), it rarely changes to the feed-forward layer's prediction (*ffn*). Instead, the authors observe that composing the residual's distribution with that of the feed-forward layer produces a "compromise" prediction, which is equal to neither (*composition*). This behavior is similar to the intra-layer composition observed in Section 5.1.

> "A possible conjecture is that the feed-forward layer acts as an elimination mechanism to 'veto' the top prediction in the residual, and thus shifts probability mass towards one of the other candidate predictions in the head of the residual's distribution." [p. 8]

### Last-layer composition analysis

[p. 8] The authors manually analyze 100 random cases of last-layer composition, where the feed-forward layer modifies the residual output in the *final* layer. They find that in most cases (66 examples), the output changes to a semantically distant word (e.g., *"people"* -> *"same"*) and in the rest of the cases (34 examples), the feed-forward layer's output shifts the residual prediction to a related word (e.g., *"later"* -> *"earlier"* and *"gastric"* -> *"stomach"*). This suggests that feed-forward layers tune the residual predictions at varying granularity, even in the last layer of the model.
