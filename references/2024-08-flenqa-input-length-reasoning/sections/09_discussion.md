# 9 Discussion [p. 10]

[p. 10] The authors study the effect of input length on reasoning performance of current Large Language Models (LLMs). Their findings reveal a significant drop in performance with longer inputs, occurring well before reaching the models' maximum input-length capacity. Their experiments relied on FLenQA, a dataset they constructed that allows to isolate the length factor, by adjusting the parts in the input that are irrelevant to the task. They show that regardless of how the samples are adjusted, there is still a strong effect of length on reasoning performance.

They identified specific failure modes, including difficulties in following extended instructions and biases towards less relevant information. Their analysis reveals specific failings, providing possible directions for future studies to address and rectify the weaknesses found in LLMs.

> "In conclusion, our work indicates that evaluating a model's performance based on a single input length does not provide a full picture, and more nuanced evaluation is required. We argue that for a model to be considered capable at long range, it must maintain its performance at any length it technically supports." [p. 10]

## Limitations [p. 10]

1. Because of the nature of behavioral testing, the observed drop in performance with varying input lengths remains unexplained; because of lack of access to many of the models, the authors suspect this direction will continue to be limited.

2. The approach aimed to create a universally applicable test across different LLMs, leading to the selection of tasks that cater to the lowest common denominator. This approach potentially overlooks the nuanced performance differences in more complex reasoning tasks (e.g. 5 key paragraphs), where, for instance, stronger models might exhibit performance degradation at shorter input lengths compared to what their findings suggest.

3. They focused on a subset of reasoning task types which may differ behaviourally from other types.

4. In order to extend the key sentences to key paragraphs, they employed GPT4 which may have introduced some level bias to the text that surrounded the text required to the reasoning task (that was generated without GPT4).

5. The study did not test the distance between key paragraphs, leaving an aspect of LLM performance unexplored that they leave for future research.

## Acknowledgements [p. 10]

This project has received funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme, grant agreement No. 802774 (iEXTRACT).

The authors thank Uri Katz, Royi Rassin and Natalie Shapira for illuminating discussions and comments.
