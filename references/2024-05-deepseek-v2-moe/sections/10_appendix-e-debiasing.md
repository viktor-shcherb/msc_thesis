# Appendix E. Discussion About Pre-Training Data Debiasing [p. 32-33]

[p. 32] During pre-training data preparation, contentious content is identified and filtered out, such as values influenced by regional cultures, to avoid the model exhibiting unnecessary subjective biases on these controversial topics. Consequently, DeepSeek-V2 performs slightly worse on the test sets that are closely associated with specific regional cultures. For example, when evaluated on MMLU, although DeepSeek-V2 achieves comparable or superior performance on the majority of testsets compared with its competitors like Mixtral 8x22B, it still lags behind on the Humanity-Moral subset, which is mainly associated with American values. [p. 32]

[p. 32] Further, a manual analysis is conducted on this subset. Three well-educated human annotators conduct independent annotations on 420 moral scenarios from the MMLU Humanity-Moral subset. Then, the agreement among their annotations and the ground-truth label is computed. As shown in Table 10, three human annotators and the ground-truth label exhibit a low agreement with each other. Therefore, the abnormal performance of DeepSeek-V2 on these value-sensitive test sets is attributed to their efforts in debiasing the pre-training corpus. [p. 32]

**Table 10** (p. 33): "Three well-educated human annotators conduct independent annotations on 420 moral scenarios from the MMLU Humanity-Moral subset, on which DeepSeek-V2 and its competitive models demonstrate performance inconsistency. Three annotators and the ground-truth label exhibit a low agreement with each other. This indicates that the answers to the Humanity-Moral subset can be contentious according to specific regional cultures."

| Agreement | Ground-Truth Label | Annotator 1 | Annotator 2 | Annotator 3 |
|---|---|---|---|---|
| Ground-Truth Label | 100.0% | 66.7% | 59.8% | 42.1% |
| Annotator 1 | 66.7% | 100.0% | 57.9% | 69.0% |
| Annotator 2 | 59.8% | 57.9% | 100.0% | 65.5% |
| Annotator 3 | 42.1% | 69.0% | 65.5% | 100.0% |
