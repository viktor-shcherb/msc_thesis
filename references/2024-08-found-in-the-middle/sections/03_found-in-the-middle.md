# 3 Found-in-the-middle: modeling and isolating positional attention bias [p. 4-6]

[p. 4-5] Ideally, a model should leverage contexts in the input prompts -- faithfully according to their relevance -- for generating the response, instead of biasing towards contexts placed at certain positions within the input. Towards this goal, the authors are interested in modeling the positional attention bias and mitigating it such that model attention can reflect the true relevance of the input context and ultimately improve models' effective utilization of the full context window.

## 3.1 Two main factors in model attention [p. 5]

[p. 5] The authors find that there are two main forces driving the model attention assigned to different documents of an input prompt: (a) where the document locates within the entire input, and (b) the relevance of the document.

**Hypothesis.** The authors consider modeling the observable attention weights allocated to the $k$-th document of an input $x^{\text{prompt}}$ as:

$$\text{Attn}(x^{\text{prompt}}, k) = f(\text{rel}(x_k^{\text{doc}}), \text{bias}(k)), \quad (1)$$

where $\text{rel}(\cdot)$ measures the relevance of an input document, $\text{bias}(\cdot)$ characterizes the positional attention bias, and $f(\cdot)$ is some unknown monotonically increasing function w.r.t. to both $\text{rel}(x_k^{\text{doc}})$ and $\text{bias}(k)$. For ease of exposition, in the remainder of the paper, they overload $\text{Attn}(x^{\text{doc}}, k)$ to denote the attention value assigned to document $x_k^{\text{doc}}$ placed at the $k$-th position within an input prompt containing $K$ documents.

### Corroborating the assumed model

The authors conduct a suite of controlled experiments using NaturalQuestion with $K = 20$ and a Vicuna-7b-v1.5-16k model to corroborate their assumed model. Specifically, for Eq. 1 to hold, it implies:

**Condition 1:** When the relevance term is fixed, model attention increases as positional bias increases. That is, given two documents $x^{\text{doc1}}$ and $x^{\text{doc2}}$: if $\text{Attn}(x^{\text{doc1}}, k) > \text{Attn}(x^{\text{doc1}}, l)$, then $\text{Attn}(x^{\text{doc2}}, k) > \text{Attn}(x^{\text{doc2}}, l)$.

**Condition 2:** Similarly, when the document position $k$ is fixed, model attention increases as the relevance of the document increases: if $\text{Attn}(x^{\text{doc1}}, k) > \text{Attn}(x^{\text{doc2}}, k)$, then $\text{Attn}(x^{\text{doc1}}, l) > \text{Attn}(x^{\text{doc2}}, l)$.

They validate Condition 1 and 2 on 100 randomly sampled examples from NaturalQuestion dataset, each with $K = 20$ documents. For validating Condition 1, given a pair of documents $(x^{\text{doc1}}, x^{\text{doc2}})$ and positions $(k, l)$, they can compute whether the relationship holds across all possible pairs. They can similarly test for Condition 2.

**Table 2** (p. 5): High correlations between model attention with document relevance and positional bias supports the hypothesized model.

| Hypothesis test | rel($x^{\text{doc}}$) | bias($k$) | % of valid pairs |
|-----------------|----------------------|-----------|-----------------|
| Condition 1     | Fixed                | Varying   | 83%             |
| Condition 2     | Varying              | Fixed     | 72%             |

In Table 2, the percentage of valid example pairs is decently high, 83% and 72% respectively, for both conditions, providing support to their hypothesis.

### Approximating f with a linear model

[p. 5] To approximate $f$, the authors consider simple linear models by following machine learning principles (a.k.a. Occam's razor), for robust estimation:

$$\text{Attn}(x^{\text{doc}}, k) = \text{rel}(x^{\text{doc}}) + \text{bias}(k) + \epsilon, \quad (2)$$

where $\epsilon$ is a noise.

To test how the model captures the underlying relationship, they compute Spearman's rank correlation between $\text{Attn}(x^{\text{doc1}}, k) - \text{Attn}(x^{\text{doc2}}, k)$ and $\text{Attn}(x^{\text{doc1}}, l) - \text{Attn}(x^{\text{doc2}}, l)$ over quadruplets of $(x^{\text{doc1}}, x^{\text{doc2}}, k, l)$ collected from NaturalQuestion. A high correlation indicates small discrepancy between $\text{Attn}(x^{\text{doc1}}, k) - \text{Attn}(x^{\text{doc2}}, k)$ and $\text{Attn}(x^{\text{doc1}}, l) - \text{Attn}(x^{\text{doc2}}, l)$. From their study, the linear model results in decently high correlation, 0.76, suggesting its effectiveness despite the simplicity. They therefore adopt Eq. 2 as their model and leave other alternatives with more degree of freedoms as future work.^2

^2 In Appendix C, the authors also explore log-linear models, which results in competitive 0.75 rank correlation.

## 3.2 Disentangling positional attention bias [p. 5-6]

[p. 5-6] Having a simple form of $f$ allows the authors to isolate the effect of positional bias from model attention. Specifically, following from Eq. 2, they can first obtain a reference model attention value with a dummy document $x^{\text{dum}}$ by:

$$\text{Attn}(x^{\text{dum}}, k) = \text{rel}(x^{\text{dum}}) + \text{bias}(k) + \epsilon. \quad (3)$$

By subtracting Eq. 2 and Eq. 3, they can offset the bias term and obtain:

$$\text{rel}(x^{\text{doc}}) \quad (4)$$
$$= \text{Attn}(x^{\text{doc}}, k) - \text{Attn}(x^{\text{dum}}, k) + \text{rel}(x^{\text{dum}})$$

Consider using a consistent dummy document $x^{\text{dum}}$ which has a constant $\text{rel}(x^{\text{dum}})$, they are then able to obtain the true relevance of different documents $x^{\text{doc}}$, free from the positional bias. They refer to $\text{Attn}(x^{\text{doc}}, k) - \text{Attn}(x^{\text{dum}}, k)$ as **calibrated attention** as it removes the baseline attention, and call the overall calibration mechanism **found-in-the-middle**.

### Calibrated attention finds relevant contexts in the middle

[p. 6] Eq. 4 allows the authors to leverage calibrated attention to estimate and rank the relevance of different documents within an input prompt. To validate the effectiveness of their model, they evaluate using calibrated attention to re-rank documents in an input prompt w.r.t. a given query. They evaluate on NaturalQuestion with the Vicuna model where they focus on the most challenging setting when the gold document is placed in the middle of the input prompt. They compare their model to:

- **Vanilla attention:** Using uncalibrated attention $\text{Attn}(x^{\text{prompt}}, k)$ to rank the documents.
- **Query generation** (Sun et al., 2023): Using likelihood of the model in generating the query based on the document.
- **Relevance generation** (Sun et al., 2023): Prompting the model to answer whether a document is relevant to a query.

**Table 3** (p. 6): Calibrated attention outperforms existing methods in ranking the relevance of retrieved contexts given a user query. Recall@3 on NaturalQuestion when gold documents are placed in the middle of input context.

|                        | Number of total documents |            |
|------------------------|--------------------------|------------|
| Method                 | $K = 10$                 | $K = 20$   |
| Vanilla attention      | 0.3638                   | 0.2052     |
| Query generation       | 0.6851                   | 0.5815     |
| Relevance generation   | 0.5521                   | 0.4012     |
| Calibrated attention   | **0.7427**               | **0.6832** |

In Table 3, the proposed calibrated attention consistently outperforms vanilla attention by a large margin, and also shows superior performance when compared to the other two re-ranking metrics. The results validate that the proposed modeling approach is effective, and that if calibrated appropriately, language models can locate relevant information even when they are hidden in the middle of the input.
