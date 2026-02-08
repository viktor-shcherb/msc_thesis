# 5 Future Work [p. 9-10]

## Extrapolating Positional Encoding

[p. 9-10] One of the obstacles in attaining infinite context length is the inability of models to attend to context lengths much larger than those they were trained on. In this work, a special indexing method is provided which can be combined with landmark tokens to bypass this issue. However, as a result, the model can only attend to tokens that are too far based on their semantic (and not their position). While this is an important improvement and facilitates extrapolation to large context lengths, it can be expected that the performance would be further improved if the exact indexing method can be used. Unfortunately, existing proposals limit (or completely disable) [p. 10] attention to far tokens which defeats the purpose. While a possible solution for models with landmark tokens is briefly discussed in Appendix E, a more thorough investigation is left as future work. Once such a method is developed, it can be directly combined with landmark tokens, yielding inference capabilities at any length.

## Hierarchical Landmarks

[p. 10] In large-scale settings, the landmark tokens can be stored in k-nearest neighbor data structures to improve retrieval performance and reduce memory usage. However, an alternative is to introduce hierarchy with higher level landmark tokens controlling the attention to lower level landmarks. In Appendix D, adding a special token which acts as a gate to all landmark tokens is investigated. This token can for example be used to decide whether a retrieval is necessary. Similarly, this token can be used at different memory cache levels where high attention to this token would constitute a cache miss, leading to lookup in lower-level (and slower) caches. Exploration of possible hierarchical landmark tokens is left as a future direction.

## Training with Cache

[p. 10] For simplicity, this work focuses on using the standard training procedure. While the standard softmax mechanism is expected to closely resemble the retrieval at inference, given the special indexing scheme, it is possible that the model would gain additional benefit from incorporating the cache during training. Investigation of such training variants is left as a future work.
