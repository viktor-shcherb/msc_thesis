# 8 Related Work [p. 9-10]

[p. 9-10] The evaluation of LLMs on long inputs has followed two distinct pathways: benchmarks of downstream tasks and next word prediction.

**Benchmarks:** In the realm of benchmarks, studies proposed datasets of long input samples that can be used to evaluate models (Shaham et al., 2023, 2022; An et al., 2023b,a; Bai et al., 2023). Those datasets are curated over inputs of different, but fixed, length. This approach, while straightforward, limits the ability to evaluate inputs of varying lengths, posing a challenge in understanding the true impact of input length on model performance.

**Next word prediction:** On the other hand, next word prediction evaluations do offer insights into how models handle inputs of different lengths (like done in Anil et al. 2023; Jiang et al. 2024). However, the correlation of this task with downstream performance was found not consistent (Liu et al., 2023a; Xia et al., 2022; Tay et al., 2022). In this paper the authors reproduce this finding with respect to extended length.

**Input intervention studies:** This study builds upon prior research that examined different aspects through input intervention, studying the semantic content (theme) of a task (Dasgupta et al., 2022), prompting strategies (Kojima et al., 2022; Yao et al., 2023; Jin et al., 2024) and various properties of the QA task (Levy et al., 2023). The current investigation focuses on input length, isolating it, to reveal its impact on performance.

> "We conclude that parametric knowledge should be accounted for when evaluating text-based reasoning capabilities." [p. 10]

The authors introduced FLenQA, which is composed of novel generated data to make sure that reasoning over the input is required.
