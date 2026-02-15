# 2 Motivation: why do we need to refine long-context benchmarks? [p. 2-3]

[p. 2] This section introduces motivations behind this work, focusing on the existing challenges in evaluating long-context capabilities of models. Specifically, the authors identify the following issues.

## Issue 1: Performance Variance Across Task Lengths

[p. 2] **Performance variance across task lengths**, evidenced by Figure 1. The performance of LM-Infinite exhibits significant variation across tasks of different lengths within the same dataset. Many long-context datasets have uneven length distributions, introducing biases in evaluating a model's long-context capability.

To validate this hypothesis, the authors train models using five different long-context enhancement methods and evaluate their performances across varying lengths on the LongBench dataset. From Figure 1, the authors observe the following:

1. **Performance Variation:** All five models demonstrate performance differences across different text lengths within the same dataset.
2. **Alignment with Dominant Lengths:** A model's average performance aligns closely with its performance on the length range with the highest proportion of samples. For instance, on Multi-News dataset, each model's average performance is close to its performance on samples within the 0-4k length range, which represents the largest share of the dataset.

These findings highlight the need for length-aware evaluations of long-context capabilities. A more robust approach involves testing model performance on N samples across diverse lengths to obtain a comprehensive assessment of its long-context capability.

**Figure 1** (p. 2): "Illustration of LM-Infinite (Han et al., 2024), a long-context enhancement method's performances on three LongBench tasks. The colored dashed lines represent the average score of each model on the corresponding task. The size of the markers corresponds to the proportion of each text length within the entire dataset. The larger the marker, the higher the proportion. The results exhibit significant variation across tasks of different lengths within the same dataset. More results of other methods are in Appendix A.1."

Description: Three side-by-side line plots showing performance across different context lengths
- Left plot: Multi-News task (score 0-4 on y-axis, context length 0-2k to 8k+ on x-axis)
- Middle plot: Qasper task (score 0-25 on y-axis, context length 0-2k to 8k+ on x-axis)
- Right plot: Gov Report task (score 0-20 on y-axis, context length 0-2k to 8k+ on x-axis)
- Key elements: Dashed horizontal lines show average scores, marker sizes indicate sample proportions
- Notable patterns: Performance varies significantly across different length ranges; average performance tends to align with dominant length ranges
- Supports claim: Need for length-aware evaluation of long-context capabilities

More results of other methods are in Appendix A.1.

## Issue 2: Ineffectiveness of Current Metrics for Evaluating Long-Context Capability

[p. 2-3] **Ineffectiveness of current metrics for evaluating long-context capability**, evidenced by Figure 2. Existing long-context metrics primarily rely on the average performance across the benchmark. However, this approach can be misleading as it conflates the model's inherent task-specific ability with its pure long-context capability.

As illustrated in Figure 2, LLaMA 3.1-8B-Instruct performs worse than Qwen 2.5-7B-Instruct on short texts but excels on extremely long texts, such as 128k and 255k, indicating its superior long-context extension capability. In this task, the average performance suggests that Qwen 2.5-7B-Instruct is the better model. But a closer inspection reveals that LLaMA 3.1-8B-Instruct has a distinct advantage in handling extremely long texts, despite its weaker performance on shorter inputs. This discrepancy underscores the need to separate a model's base ability (on short texts) from its long-context capability.

To address this, the authors propose a novel metric that accurately captures a model's ability to handle long contexts from Base Ability.

**Figure 2** (p. 3): "Comparison between LLaMA 3.1-8B-Instruct and Qwen 2.5-7B-Instruct on the Counting Star task across varying text lengths. The dashed line represents the average score across all lengths. LLaMA 3.1-8B-Instruct performs worse than Qwen 2.5-7B-Instruct on short texts but excels on extremely long texts, indicating its superior long-context extension capability."

Description: Line plot with two models compared
- X-axis: Context lengths from 0-8k to 256k (0-8k, 8k, 16k, 32k, 64k, 128k, 256k)
- Y-axis: Score from 0 to 80
- Key elements: Two lines (blue for Llama3.1-8B-Instruct, brown for Qwen2.5-7B-Instruct), dashed horizontal lines for averages
- Notable patterns: Llama3.1-8B-Instruct starts lower (~42) but maintains performance better at extreme lengths (~25 at 256k); Qwen2.5-7B-Instruct starts higher (~60) but drops more steeply at extreme lengths (~12 at 256k)
- Supports claim: Need to separate base ability from long-context capability; average metrics can be misleading
