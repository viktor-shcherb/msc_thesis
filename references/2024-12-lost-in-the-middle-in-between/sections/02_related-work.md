# 2 Related Work [p. 2-3]

## 2.1 The "Lost in the Middle" Problem [p. 2]

The "Lost in the Middle" problem, first identified by Liu et al. (2024), highlights a significant limitation in long-context LMs. Specifically, when relevant information is distributed throughout a long context, model performance varies depending on the information's position. Their findings reveal that performance follows a characteristic curve: accuracy is poorest when critical information appears in the middle of the context and improves when the information is near the beginning or end.

In their experiments with the NaturalQuestions-Open dataset (Kwiatkowski et al., 2019), Liu et al. (2024) tested question-answering accuracy by repositioning the document containing the answer among distractor documents. They observed consistent variations in accuracy based on the document's position. Additionally, the authors studied a long-context key-value retrieval task, where models were tasked with retrieving a specific value associated with a key in an extended JSON file. Across both tasks, their results demonstrated that no examined model could process relevant information equally well across all positions.

## 2.2 Mitigation Strategies for "Lost in the Middle" [p. 2]

To mitigate the "Lost in the Middle" problem, Liu et al. (2024) proposed Query-Aware Contextualization, which involves placing a query both before and after the request. While this approach effectively resolves the issue in the key-value retrieval setting, it has little impact on multi-document question answering, leaving the problem unresolved in that domain.

Other efforts have focused on re-ranking passages before including them in the input prompt. Peysakhovich and Lerer (2023) observed that LLMs assign preferential attention to relevant documents compared to irrelevant ones, even when located at the same position. They proposed sorting documents based on average attention scores while accounting for the typical attention distribution associated with positional biases.

Similarly, Tang et al. (2023) introduced "permutation self-consistency," a method that shuffles document orders and asks the model to rank their relevance, using a cumulative vote to determine the final ordering. However, these approaches are likely to scale poorly in the multi-hop QA setting. In multi-hop reasoning, later documents in the chain depend on earlier ones, making the number of permutations required for a robust ranking grow combinatorially with the number of reasoning steps.

## 2.3 Multi-Hop Question Answering [p. 3]

Multi-Hop Question Answering (MHopQA) tasks involve reasoning across multiple documents (Yang et al., 2018; Saxena et al., 2020; Mavi et al., 2024), where relevant information is often scattered across the context in disconnected pieces. This often require models to combine parametric knowledge (Guo et al., 2022; Feng et al., 2023; Shaier et al., 2024a, 2023a; Trivedi et al., 2020; Su et al., 2024; Lee et al., 2021) with complex external context to derive answers. Unlike single-hop QA tasks where all relevant information is co-located, the distributed nature of multihop reasoning poses significant challenges, often resulting in degraded performance.

The complexity of traversing reasoning chains across multiple sources not only reduces accuracy (Guo et al., 2022; Pezeshkpour, 2023; Wang et al., 2023; Shaier et al., 2023b; Wang et al., 2024; Su et al., 2024) but also hinders the model's ability to consistently utilize all relevant information (Yang et al., 2018; Su et al., 2024; Shaier et al., 2024b,c; Trivedi et al., 2020). As input size and reasoning steps grow, maintaining factual accuracy becomes increasingly difficult, further compounding these challenges.

## 2.4 Impact of Input Length on Reasoning [p. 3]

Simultaneously to our work, Levy et al. (2024) examined how LLM performance degrades with increasing input length. They found that reasoning performance deteriorates as the number of input tokens grows.

Our study differs from theirs in several key aspects:

1. We focus on performance with respect to document position within a fixed-size context, whereas Levy et al. (2024) investigate performance relative to overall input size.

2. We evaluate on three popular multi-hop QA datasets, while Levy et al. (2024) use their custom dataset, FLenQA, which consists exclusively of true/false questions.

3. We study questions requiring up to four reasoning steps, whereas Levy et al. (2024) limit their analysis to two-step comparison questions.

These distinctions emphasize our focus on understanding how positional biases within fixed contexts impact reasoning, particularly in multi-hop QA tasks.
