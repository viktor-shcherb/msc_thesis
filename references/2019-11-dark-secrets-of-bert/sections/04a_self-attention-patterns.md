# 4.1 BERT's self-attention patterns [p. 3-4]

[p. 3] Manual inspection of self-attention maps for both basic pre-trained and fine-tuned BERT models suggested that there is a limited set of self-attention map types that are repeatedly encoded across different heads. Consistently with previous observations, five frequently occurring patterns were identified (shown in Figure 1):

- *Vertical*: mainly corresponds to attention to special BERT tokens *[CLS]* and *[SEP]* which serve as delimiters between individual chunks of BERT's inputs.
- *Diagonal*: formed by the attention to the previous/following tokens.
- *Vertical+Diagonal*: a mix of the previous two types.
- *Block*: intra-sentence attention for the tasks with two distinct sentences (such as RTE or MRPC).
- *Heterogeneous*: highly variable depending on the specific input and cannot be characterized by a distinct structure.

Note that because the *Heterogeneous* category contains patterns not included in the other four categories, the constructed list of classes is exhaustive. [p. 3]

[p. 3] The authors hypothesize that the last of the listed types (Heterogeneous) is more likely to capture interpretable linguistic features, necessary for language understanding. Attention to special tokens is important for cross-sentence reasoning, and attention to the previous/following token comes from language model pre-training.

## Classifier for attention pattern types

[p. 3] To estimate the proportion of attention heads that may capture linguistically interpretable information, approximately 400 sample self-attention maps were manually annotated as belonging to one of the five classes. The self-attention maps were obtained by feeding random input examples from selected tasks into the corresponding fine-tuned BERT model. This produced a somewhat unbalanced dataset, in which the "Vertical" class accounted for 30% of all samples. A convolutional neural network with 8 convolutional layers and ReLU activation functions was trained to classify input maps into one of these classes. This model achieved F1 score of 0.86 on the annotated dataset. The classifier was used to estimate the proportion of different self-attention patterns for the target GLUE tasks using up to 1000 examples (where available) from each validation set.

## Results

[p. 3-4] The self-attention map types are consistently repeated across different heads and tasks. A large portion of encoded information corresponds to attention to the previous/following token, to the special tokens, or a mixture of the two (the first three classes). The estimated upper bound on all heads in the "Heterogeneous" category (i.e. the ones that *could* be informative) varies from 32% (MRPC) to 61% (QQP) depending on the task.

> "We would like to emphasize that this only gives the upper bound on the percentage of attention heads that could potentially capture meaningful structural information beyond adjacency and separator tokens." [p. 3]

## Figure 1 (p. 4)

**Figure 1** (p. 4): "Typical self-attention classes used for training a neural network. Both axes on every image represent BERT tokens of an input example, and colors denote absolute attention weights (darker colors stand for greater weights). The first three types are most likely associated with language model pre-training, while the last two potentially encode semantic and syntactic information."

Shows five example attention map heatmaps, one for each class: Vertical, Diagonal, Vertical + Diagonal, Block, Heterogeneous. Each shows a distinct visual pattern in the L x L attention weight matrix with [CLS] and [SEP] tokens marked.

## Figure 2 (p. 4)

**Figure 2** (p. 4): "Estimated percentages of the identified self-attention classes for each of the selected GLUE tasks."

Shows stacked bar charts for MRPC, STS-B, SST-2, QQP, RTE, QNLI, and MNLI. The five classes are color-coded: Heterogeneous, Block, Vert+Diag, Diagonal, Vertical. The Heterogeneous proportion varies by task, with QQP having the largest proportion and MRPC the smallest.
