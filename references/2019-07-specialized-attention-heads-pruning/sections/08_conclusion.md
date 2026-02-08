# 8 Conclusions [p. 10]

The authors evaluate the contribution made by individual attention heads to Transformer model performance on translation. Layer-wise relevance propagation is used to show that the relative contribution of heads varies: only a small subset of heads appear to be important for the translation task. [p. 10]

Important heads have one or more interpretable functions in the model, including attending to adjacent words and tracking specific syntactic relations. To determine if the remaining less-interpretable heads are crucial to the model's performance, a new approach to pruning attention heads is introduced. [p. 10]

Key conclusions: [p. 10]

- Specialized heads are the last to be pruned, confirming their importance directly.
- The vast majority of heads, especially the encoder self-attention heads, can be removed without seriously affecting performance.

Future work: the authors would like to investigate how their pruning method compares to alternative methods of model compression in NMT. [p. 10]

## Acknowledgments [p. 10]

The authors thank anonymous reviewers, Wilker Aziz, Joost Bastings for helpful suggestions, and Yandex Machine Translation team for helpful discussions and inspiration. Ivan Titov acknowledges support of the European Research Council (ERC StG BroadSem 678254) and the Dutch National Science Foundation (NWO VIDI 639.022.518). [p. 10]
