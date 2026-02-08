# 4 Values Represent Distributions [p. 4-5]

[p. 4] After establishing that keys capture patterns in training examples, the authors turn to analyze the information stored in the corresponding values. They show that each value v_i^l can be viewed as a distribution over the output vocabulary, and demonstrate that this distribution complements the patterns in the corresponding key k_i^l in the model's upper layers (see Figure 1).

## Casting values as distributions over the vocabulary

[p. 4] Each value vector v_i^l is converted into a probability distribution over the vocabulary by multiplying it by the output embedding matrix E and applying a softmax:

$$p_i^l = \text{softmax}(v_i^l \cdot E).$$

The probability distribution p_i^l is uncalibrated, since the value vector v_i^l is typically multiplied by the input-dependent memory coefficient m_i^l, changing the skewness of the output distribution. That said, the *ranking* induced by p_i^l is invariant to the coefficient, and can still be examined. This conversion assumes (naively) that all model's layers operate in the same embedding space.

Footnote 4 [p. 4]: This is a simplification; in practice, the adaptive softmax (Baevski and Auli, 2019) is used to compute probabilities.

## Value predictions follow key patterns in upper layers

[p. 4-5] For every layer l and memory dimension i, the top-ranked token according to v_i^l (argmax(p_i^l)) is compared to the next token w_i^l in the top-1 trigger example according to k_i^l (the example whose memory coefficient for k_i^l is the highest). Figure 4 shows the *agreement rate*, i.e. the fraction of memory cells (dimensions) where the value's top prediction matches the key's top trigger example (argmax(p_i^l) = w_i^l).

The agreement rate is close to zero in the lower layers (1-10), but starting from layer 11, the agreement rate quickly rises until 3.5%, showing higher agreement between keys and values on the identity of the top-ranked token. Importantly, this value is orders of magnitude higher than a random token prediction from the vocabulary, which would produce a far lower agreement rate (0.0004%), showing that upper-layer memories manifest non-trivial predictive power.

**Figure 4** (p. 4): "Agreement rate between the top-ranked token based on the value vector v_i^l, and the next token of the top-ranked trigger example associated with the key vector k_i^l."

The figure is a bar chart with layers 1-16 on the x-axis and "agreement rate (%)" (0-3.5) on the y-axis. Layers 1-10 show near-zero agreement rates (below 0.5%). Starting from layer 11, the agreement rate increases: approximately 1.0% at layer 11, 1.5% at layer 12, 2.0% at layer 13, 2.5% at layer 14, 3.0% at layer 15, and approximately 3.3% at layer 16.

[p. 5] Next, the next token of k_i^l's top-1 trigger example (w_i^l) is taken, and its rank in the value vector's distribution p_i^l is found. Figure 5 shows that the rank of the next token of a trigger example increases through the layers, meaning that w_i^l tends to get higher probability in the upper layers.

**Figure 5** (p. 5): "Distribution of the rank of the next-token in the top-1 trigger example of k_i^l (w_i^l), according to the ranking induced by the value vector v_i^l. We cut the tail of the distribution, which stretches up to the vocabulary size (~270K tokens)."

The figure is a box plot with layers 1-16 on the x-axis and "rank distribution" (0-30000) on the y-axis. In layers 1-7, the median rank is approximately 10000-15000 with wide interquartile ranges. From layer 8 onward, the median rank decreases steadily. By layers 14-16, the median rank is close to 0-2000, with much tighter interquartile ranges, indicating that the next token is ranked much higher by the value vector's distribution in upper layers.

## Detecting predictive values

[p. 5] To examine if values with high agreement rate can be automatically detected, the probability of the values' top prediction is analyzed, i.e., max(p_i^l). Figure 6 shows that although these distributions are not calibrated, distributions with higher maximum probabilities are more likely to agree with their key's top trigger example.

The 100 values with highest probability across all layers and dimensions are taken (97 out of the 100 are in the upper layers, 11-16), and for each value v_i^l, the top-50 trigger examples of k_i^l are analyzed. In almost half of the values (46 out of 100), there is at least one trigger example that agrees with the value's top prediction. Examples are provided in Table 2.

**Figure 6** (p. 5): "Agreement rate (between the top-ranked token based on the value vector v_i^l and the next token of the top-ranked trigger example associated with the key vector k_i^l) as a function of the maximal probability assigned by the value vector."

The figure is a bar chart with "top prediction probability" on the x-axis (bins: 8.9e-5, 1.3e-4, 1.8e-4, 2.2e-4, 2.7e-4, 3.1e-4, 3.6e-4, 4.e-4) and "agreement rate" (0-1.0) on the y-axis. The agreement rate increases with higher top prediction probability, starting near 0 for the lowest bins and reaching approximately 0.95 at the highest probability bin (4.e-4).

**Table 2** (p. 6): Example values, their top prediction, the fraction of their key's top-50 trigger examples that agree with their prediction, and a matching trigger example (with the target token marked in blue).

| Value | Prediction | Precision@50 | Trigger example |
|---|---|---|---|
| v_{222}^{13} | *each* | 68% | *But when bees and wasps resemble **each*** |
| v_{752}^{16} | *played* | 16% | *Her first role was in Vijay Lalwani's psychological thriller Karthik Calling Karthik, where Padukone was cast as the supportive girlfriend of a depressed man (**played**)* |
| v_{2601}^{13} | *extratropical* | 4% | *Most of the winter precipitation is the result of synoptic scale, low pressure weather systems (large scale storms such as **extratropical**)* |
| v_{881}^{15} | *part* | 92% | *Comet served only briefly with the fleet, owing in large **part*** |
| v_{2070}^{16} | *line* | 84% | *Sailing from Lorient in October 1805 with one ship of the **line*** |
| v_{3186}^{12} | *jail* | 4% | *On May 11, 2011, four days after scoring 6 touchdowns for the Slaughter, Grady was sentenced to twenty days in **jail*** |

## Discussion

[p. 5] When viewed as distributions over the output vocabulary, values in the upper layers tend to assign higher probability to the next-token of examples triggering the corresponding keys. This suggests that memory cells often store information on how to directly predict the output (the distribution of the next word) from the input (patterns in the prefix). Conversely, the lower layers do not exhibit such clear correlation between the keys' patterns and the corresponding values' distributions.

A possible explanation is that the lower layers do not operate in the same embedding space, and therefore, projecting values onto the vocabulary using the output embeddings does not produce distributions that follow the trigger examples. However, the results imply that some intermediate layers *do* operate in the same or similar space to upper layers (exhibiting some agreement), which in itself is non-trivial. The authors leave further exploration of this phenomenon to future work.
