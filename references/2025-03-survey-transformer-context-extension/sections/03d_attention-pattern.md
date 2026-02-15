# 3.4 Attention Pattern [p. 5]

There is a class of methods modifying the attention pattern, i.e. the range of tokens attended to. They can better adapt models to expand processing sequence length [p. 5].

Some of them do not require additional training and can be employed as plug-and-play solutions in existing models [p. 5].

These methods are divided into three main categories:
1. Sliding window
2. Parallel context
3. Sparse attention [p. 5]

## 3.4.1 Sliding Window [p. 5]

This type of method divides the sequence into segments and performs attention calculation segment by segment without significantly increasing computational complexity. The attention results from earlier segments are stored, which later segments can use during their attention calculation (Dai et al., 2019; Han et al., 2024; Xiao et al., 2023) [p. 5].

## 3.4.2 Parallel Context [p. 5]

The Parallel Context method folds the context part of the input (i.e., in-context examples) into multiple segments. These segments first calculate attention independently, and share the same set of position indexes. And then prompt tokens in the input attend to all the context tokens, so that fully utilize contextual information (Ratner et al., 2022; Hao et al., 2022) [p. 5].

These methods require no training and can be plug-and-played into existing models [p. 5].

## 3.4.3 Sparse Attention [p. 5]

Some work reduce the number of tokens involved in the attention computation, decreasing computational load. They randomly join the original attention method which attends to local continuous tokens, while expand the attentive field, and attend to discrete tokens with further context (Ding et al., 2023; Yu et al., 2023; Chen et al., 2023c) [p. 5].
