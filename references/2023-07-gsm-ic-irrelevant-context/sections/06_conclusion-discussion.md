# 6. Conclusion and Discussion [p. 9]

[p. 9] GSM-IC is introduced as a dataset that supports comprehensive study of the distractibility of large language models when performing arithmetic reasoning in presence of irrelevant contexts. A variety of prompting techniques are examined on GSM-IC, and all are demonstrated to be sensitive to the irrelevant information in the problems. [p. 9]

Among the studied techniques, self-consistency (Wang et al., 2022c) leads to a substantial improvement in robustness to irrelevant context across the board, and presenting example problems with irrelevant context in the prompt also consistently improves the performance. Similarly, simply adding an instruction to ignore irrelevant information brings notable performance gains on the benchmark. [p. 9]

> "Despite the improvement achieved by these methods, the fundamental issue remains: a single piece of irrelevant information can distract the models and substantially degrade their performance, even on problems whose clean versions they correctly solve." [p. 9]

The authors encourage researchers to prioritize improving on this fundamental limitation when developing new training and prompting techniques. Investigation of the distractibility on other tasks and different language models is left for future work. [p. 9]
