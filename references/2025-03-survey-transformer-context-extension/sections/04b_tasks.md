# 4.2 Tasks [p. 6]

Currently, existing benchmarks propose numerous tasks to evaluate the model's ability to process long context. But there is no systematic taxonomy for these tasks [p. 6].

Therefore, we divide all tasks in existing benchmarks into seven categories from the perspective of task setting:
1. Question Answering
2. Needle-in-a-Haystack
3. Statistical Tasks
4. In-Context Learning
5. Text Generation
6. Other Tasks [p. 6]

Below is the introduction of each type of task, and the details are in the Appendix B.2 [p. 6].

## 4.2.1 Question Answering [p. 6]

**Single-hop Question Answering** requires models to locate and extract answers from a single text passage, typically involving a single fact (Rajpurkar et al., 2016; Joshi et al., 2017; Kočiský et al., 2018) [p. 6].

**Multi-hop Question Answering** requires models to integrate information from multiple sources to answer complex questions. This often involves reasoning across different pieces of evidence (Ho et al., 2020; Trivedi et al., 2022; Yang et al., 2018; Chen et al., 2024b; Zhuang et al., 2023) [p. 6].

## 4.2.2 Needle-in-a-Haystack [p. 6]

Needle-in-a-Haystack evaluate LLMs' ability to extract specific content from long contexts. These tasks can evaluate the model's retrieval capability, also measure the range of context lengths model can handle (Zhu et al., 2024; Mohtashami and Jaggi, 2023; Zhang et al., 2024; Li et al., 2024b) [p. 6].

## 4.2.3 Statistical Tasks [p. 6]

**Long Arithmetic Calculation** requires models to perform addition and subtraction operations on lengthy arithmetic expressions (Zhang et al., 2024, 2023b; Cobbe et al., 2021; Xu et al., 2024; Chen et al., 2024a) [p. 6].

**Numerical Information Extraction** requires models to identify specific mathematical elements (Zhang et al., 2024; Li et al., 2023a) [p. 6].

**Sentiment Aggregation** requires models to output the percentage of positive reviews when provided with a collection of reviews (Angelidis et al., 2021; Shaham et al., 2023) [p. 6].

**Paragraph Counting** requires models to count the number of unique paragraphs in a set of randomly repeated and shuffled passages (Bai et al., 2023) [p. 6].

## 4.2.4 Code [p. 6]

**Code Completion** requires models to complete missing code fragments based on preceding code and context (Chen et al., 2021a; Zheng et al., 2023; Bai et al., 2023; Guo et al., 2023; Zan et al., 2022; Dong et al., 2023a; Qin et al., 2024) [p. 6].

**Code Running** asks models to infer the output of lengthy programs by tracing a series of cascading function calls (Bubeck et al., 2023; An et al., 2023; Zhang et al., 2024) [p. 6-7].

**Code Debugging** requires models to identify deliberately inserted errors (Zhang et al., 2024) [p. 7].

## 4.2.5 In-Context Learning [p. 7]

The input will contain a certain amount of examples, resulting in a long input. This is caused by the example itself is very long or the number of examples is particularly large. Based on this fact, we divide In-Context Learning task into two categories: long example learning and many-shot learning [p. 7].

**Long Example Learning** requires models to process extensive inputs with long examples which have large label spaces and generate accurate predictions. This task inherently is a traditional long-context challenge (Bai et al., 2023; Li et al., 2024c; Li and Roth, 2002; NLPCC, 2014) [p. 7].

**Many-shot Learning** leverages the expanded context windows of models to process hundreds or even thousands of examples in order to complete a given task (Yu et al., 2020; Bertsch et al., 2024b) [p. 7].

## 4.2.6 Text Generation [p. 7]

**Language Modeling** serving as the pre-training task for LLMs, is also a widely used basic task to test the model's ability to generate text [p. 7].

**Document Summarization** requires models to make a summary of the input documents, which encompasses single-document and multi-document tasks. Single-document summarization extracts key information from a single document (Wang et al., 2022; Chen et al., 2021b; Huang et al., 2021; Zhong et al., 2021), while multi-document summarization synthesizes information from multiple sources into a comprehensive, non-repetitive summary containing all key points (Bai et al., 2023; An et al., 2023; Fabbri et al., 2019) [p. 7].

**Open-ended Text Generation** requires models to produce coherent and logical content given long topics (Tan et al., 2024; Bai et al., 2024; Kumar et al., 2024; Ni et al., 2024; Rafailov et al., 2024) [p. 7].

## 4.2.7 Other Tasks [p. 7]

In addition to the six types of tasks listed above, there are some tasks that are not included in this classification system but are equally important for testing the model's long context ability [p. 7].

**Reordering** asks models to reconstruct the original sequence of shuffled fragments by considering the broad context and logical relationships (Kryściński et al., 2021; Shaham et al., 2023; Li et al., 2023a; Dong et al., 2023a; Wang et al., 2024a) [p. 7].

**Context Consistency** shows models an academic paper and a hypothesis, requiring models to judge whether the hypothesis is supported or contradicted by the ideas in the paper (Dong et al., 2023a) [p. 7].

**Summary Source Paragraph Identification** challenges models to identify the original source paragraphs for given summaries (Bai et al., 2023) [p. 7].

**Character Identification** requires models to identify different speakers in long dialogues by recognizing their distinct characteristics (TVMEG, 2024; Senedd Cymru, 2024; Zhang et al., 2024; Dong et al., 2023a; Chen et al., 2021b) [p. 7].
