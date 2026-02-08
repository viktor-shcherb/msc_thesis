# 2 Desired Data Properties [p. 2-3]

[p. 2] The goal is to understand how input length affects LLMs reasoning capabilities over text, given that the relevant information remains the same. They use question answering tasks that require models to reason over a given text. For the investigation to be applicable to both open and closed models, they chose a behavioral approach that relies on input intervention (Holtzman et al., 2023).

The data aims to satisfy the following requirements:

## Ensuring models reason over the input

To examine the performance of models on long inputs, they require that the task can only be solved correctly by drawing conclusions from evidence in the text (Huang and Chang, 2022).

1. *Each data sample should contain several relevant text spans that are both necessary and sufficient to correctly solve the task.*

2. *All relevant spans must be consulted jointly to reach a successful solution.* Some tasks, like text summarization, can be solved using a "divide-and-conquer" approach (Gidiotis and Tsoumakas, 2020; Liu et al., 2022; Wolhandler et al., 2022), where each relevant span is individually identified, then paraphrased and added to the output. They wish to avoid such decomposable tasks, as they do not really require reasoning over long inputs.

3. *The question and supporting relevant spans should consist of novel facts not seen in training.* Ensuring that a task requires reasoning across multiple text spans is a stronger requirement than a task that requires multi hop reasoning. It was shown that models can answer existing reasoning dataset when given one some of the parts that were claimed to be required for the task (Chen and Durrett, 2019; Min et al., 2019). To avoid model reliance on parametric knowledge when they expect a reasoning process to be done (i.e to avoid data contamination (Jacovi et al., 2023; Sainz et al., 2023)), they desire that an evaluation aimed to test reasoning capabilities will require reasoning over texts that were not previously available.

## Isolating the length factor

[p. 3] To isolate the effect of length, the following requirements are imposed:

1. *The required reasoning should be independent of the length of the sample*: the relevant spans should remain the same in all length variations.

2. The added material (a.k.a "padding", text that is added to control the samples' length) *should not contradict or interfere with the reasoning over the relevant text spans*.

3. The location of each relevant span within the input should be controllable.

## Maintaining natural-looking inputs

The input should reflect something a user may naturally use in an LLM prompt. A sequence of unrelated sentences is not natural. In contrast, a sequence of unrelated paragraphs but where each paragraph is cohesive is more natural, as such an input may result from collecting relevant information from multiple sources. To best maintain the naturality of the inputs while changing an input's length, they require that the input should be cohesive at least at the level of paragraphs.
