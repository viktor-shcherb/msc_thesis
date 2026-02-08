# 7 Discussion and Conclusion [p. 9-10]

[p. 9] Understanding how and why transformers work is crucial to many aspects of modern NLP, including model interpretability, data security, and development of better models. Feed-forward layers account for most of a transformer's parameters, yet little is known about their function in the network.

The authors propose that feed-forward layers emulate key-value memories, and provide a set of experiments showing that: (a) keys are correlated with human-interpretable input patterns; (b) values, mostly in the model's upper layers, induce distributions over the output vocabulary that correlate with the next-token distribution of patterns in the corresponding key; and (c) the model's output is formed via an aggregation of these distributions, whereby they are first composed to form individual layer outputs, which are then refined throughout the model's layers using residual connections.

## Future research directions

[p. 9-10] The findings open important research directions:

- **Layer embedding space.** A correlation between value distributions over the output vocabulary and key patterns is observed, that increases from lower to upper layers (Section 4). Is this because the layer's output space transforms across layers? If so, how? The authors note that this possible transformation cannot be explained solely by the function of feed-forward layers: if the model only did a series of key-value look-ups and value-distribution aggregation via weighted addition, then a single, unifying embedding space would appear more natural. Thus, the transformation might have to do with the interplay between feed-forward layers and self-attention layers.

- **Beyond language modeling.** The formulation of feed-forward networks as key-value memories generalizes to any transformer model, e.g. BERT encoders and neural translation models. The authors thus expect their qualitative empirical observations to hold across diverse settings, and leave verification of this for future work.

- **Practical implications.** A better understanding of feed-forward layers has many implications in NLP. For example, future studies may offer interpretability methods by automating the pattern-identification process; memory cells might affect training-data privacy as they could facilitate white-box membership inference (Nasr et al., 2019); and studying cases where a correct pattern is identified but then suppressed during aggregation may guide architectural novelties.

[p. 10]
> "Thus, by illuminating the role of feed-forward layers, we move towards a better understanding of the inner workings of transformers, and open new research threads on modern NLP models." [p. 10]
