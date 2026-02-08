# 2 Positional attention bias overpowers mid-sequence context [p. 2-4]

[p. 2] Recent work has produced language models capable of handling increasingly long input contexts (Xiong et al., 2023; Li et al., 2023a). However, many of these models struggle to locate relevant information placed in the middle of the input sequence (Liu et al., 2023), a phenomenon known as the "lost-in-the-middle" problem. While this problem is widely recognized, the potential factors contributing to this behavior remain poorly understood. The authors seek to deepen understanding of the problem through a suite of exploratory qualitative and quantitative studies.

## Setup

The authors adhere to the original experimental setup outlined in Liu et al. (2023), utilizing an open-domain question answering task (Kwiatkowski et al., 2019) for their exploratory study. In the lost-in-the-middle setup (Liu et al., 2023), a model is tasked to answer a user query $x^{\text{q}}$ using a set of $k$ related documents retrieved from an external data source $D = \{x^{\text{gold}}, x_1^{\text{distract}}, \ldots, x_{k-1}^{\text{distract}}\}$, where only the gold document $x^{\text{gold}}$ contains the correct answer. The question and documents are typically serialized as an input sequence

$$x^{\text{prompt}} = [x^{\text{q}}, x_1^{\text{doc}}, \ldots, x_K^{\text{doc}}, x^{\text{q}}],$$

prompting a language model to generate the final answer.^1

Observations indicate that model performance significantly decreases when $x^{\text{gold}}$ is placed within the middle of the input prompt (i.e., $x_{[k/2]}^{\text{doc}}$), compared to scenarios where $x^{\text{gold}}$ is placed at the beginning or end. The authors reproduce the lost-in-the-middle phenomenon with a Vicuna-7b-v1.5-16k (Vicuna) model (Li et al., 2023a) to gain deeper insights into the characteristics of the model's errors. They focus their error analysis on the setting where they have a total of 20 documents ($K = 20$). They specifically look at the examples where the model makes incorrect predictions when the gold document is placed at the middle (10-th) position.

^1 The question is repeated before and after the documents so that the model can better attend to relevant contexts (Liu et al., 2023; Xu et al., 2023b).

## 2.1 U-shaped attention bias [p. 3-4]

[p. 3] The authors first examine responses generated when gold documents are placed in the **middle** of input prompts. Qualitatively, the model's response exhibits a strong bias towards the document at the first position, regardless of the gold document's location (Figure 2). This bias persists whether the input documents retain their original order or are randomly shuffled.

**Figure 2** (p. 3): "Left and Middle: Qualitatively, the model's response exhibits a strong bias towards the document at the first position (red). This persists whether the input documents retain their original order (left: gold document at the 10th position) or are randomly shuffled (middle: gold document at the 13th position). Model responses are shown in green, with the gold answer highlighted in yellow. Right: Our attention calibration method enables the model to find relevant context even when placed in the middle."

The figure shows three side-by-side examples of prompts and model responses for the question "what is mercy mercy me by marvin gaye about." Left panel: original prompt order with gold document at position 10 -- the model answers based on Document [1] content instead. Middle panel: shuffled order with gold document at position 13 -- the model again answers based on Document [1]. Right panel: with their calibration method, the model correctly attends to Document [10] (the gold document) and produces a correct answer referencing "sorrow regarding the environment."

[p. 3] The strong correlation between the model's output and the first document could suggest that they are highly relevant, distracting the model (Shi et al., 2023a). However, quantitatively, the model's response strongly depends on the document at the first position (Figure 3). This dependence persists even after randomly shuffling the document order, irrespective of its relevance to the query. The dependence is measured by computing the TF-IDF similarity score between the response and each document (gold document originally at position 10).

**Figure 3** (p. 3): "Quantitatively, the model's response strongly depends on the document at the first position. This dependence persists even after randomly shuffling the document order, irrespective of its relevance to the query. We measure this dependence by computing the TF-IDF similarity score between the response and each document (gold document originally at position 10)."

The figure shows two line plots (Original order and Shuffled order) with x-axis "Document at Position" (1-20) and y-axis "Relevance w.r.t. model output." Both curves show a strong spike at position 1 (~0.345 for original, ~0.340 for shuffled) and then drop to around 0.200-0.225 for positions 2-20, with only minor variation. The pattern is nearly identical between original and shuffled orders.

[p. 4] To investigate the potential origins of positional bias, the authors visualize the model's self-attention weights, as the weights has been shown to correlate with models' generations, although not necessarily causal (Dong et al., 2021; Zhang et al., 2023).

More formally, given an input prompt consisting of $K$ documents $x^{\text{prompt}} = [x_1^{\text{doc}}, \ldots, x_K^{\text{doc}}]$, where each document $x_k^{\text{doc}} = \{x_{k,i}^{\text{doc}}\}_{i=1}^{N_k}$ contains $N_k$ tokens, let $\text{Attn} : \mathcal{X} \times \mathbb{N} \to \mathbb{R}$ denote a function that computes the average attention weights assigned to document $x_k^{\text{doc}}$ as $\text{Attn}(x^{\text{prompt}}, k) = \sum_{i=1}^{N_k} \text{attn}(x_{k,i}^{\text{doc}}) / N_k$, where $\text{attn}(x_{k,i}^{\text{doc}})$ is the attention weight value allocated to token $x_{k,i}^{\text{doc}}$ when predicting the next $|x^{\text{prompt}}| + 1$ token.

The authors visualize the self-attention weights assigned to each document, averaged across all its tokens, all decoder layers, and heads. They investigate how these weights vary based on document position within the input prompt. Figure 4 (blue curve) reveals a U-shaped attention pattern. Documents near the beginning and end of the input receive higher weights, while those in the middle receive lower weights. Crucially, the U-shaped pattern persists even after randomly shuffling document order (Figure 4, orange curve), suggesting that this bias does not depend on the documents' actual content.

**Figure 4** (p. 3): "Average attention weights reveal a U-shaped positional bias in the model. Documents at the beginning and end receive greater attention, regardless of order (gold document originally at position 10). Attention is averaged across different decoder layers and attention heads."

The figure shows two curves (Original order and Shuffled order) with x-axis "Document at Position" (1-20) and y-axis "Model Attention Weight." Both curves exhibit a clear U-shape: attention is highest at position 1 (~0.00020), drops to a minimum around positions 8-12 (~0.00005), then rises again towards position 20 (~0.00018). The curves for original and shuffled order are nearly identical.

## 2.2 Does attention favor relevant context? [p. 4]

**Observation 1: Model prioritizes relevant contexts from the same position.** In Figure 4, the authors observe a significant difference in attention values at $x_{10}^{\text{doc}}$ when comparing examples with original document order (blue) and randomly shuffled order (orange). Specifically, the attention value is notably higher when $x_{10}^{\text{doc}}$ is controlled to be $x^{\text{gold}}$. This contrasts with instances where $x_{10}^{\text{doc}}$ is uncontrolled, suggesting that apart from U-shaped positional bias, the model exhibits an ability to *prioritize* relevant context.

**Observation 2: Model prioritizes highly-weighted documents for generation.** Based on these observations, the authors hypothesize that positional attention bias significantly influences the model's tendency to rely heavily on the first documents during output generation. Specifically, the models are more likely to incorporate the document receiving the highest attention (often the first) into its output. To validate this, for each of the examples of interest (where the model makes incorrect predictions), they divide the documents into first half receiving higher model attention and second half receiving lower attention. They count the number of examples in which the first or second half contains the document that is most likely used in the model's generation (i.e., having the highest TF-IDF score with model's response). In Table 1, they show that documents receiving higher attention positively correlates with them being used in the model's generation.

**Table 1** (p. 4): Number of examples where the most likely used document in the model's generation falls within the first half of documents receiving higher model attention or second half receiving lower attention. There is a strong correlation where documents receiving higher attention are more likely to be used in model's response.

|                         | Most Likely Used |     |
|-------------------------|-----------------|-----|
|                         | # of examples   | %   |
| Highest Half Attention  | 526             | 74% |
| Lowest Half Attention   | 186             | 26% |

From the above studies, the authors observe that not only does the model exhibit a U-shape positional attention bias, but this bias also correlates strongly with the model's biased tendency in using documents placed at certain positions in forming its response. They thus conjecture that lost-in-the-middle happens because of the dominating force of positional bias.
