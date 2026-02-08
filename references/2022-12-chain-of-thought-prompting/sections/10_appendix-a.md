# A Frequently Asked Questions [p. 16]

## A.1 Why does increasing model scale improve chain-of-thought prompting? [p. 16]

[p. 16] The finding that successful chain-of-thought reasoning predictably emerges only at certain model scales is intriguing. Scaling up language models has been shown to confer benefits such as improved performance and sample efficiency (Kaplan et al., 2020), but chain-of-thought reasoning is emergent in the sense that its success cannot be predicted only by extrapolating the performance of small scale models, as chain of thought actually hurts performance for most models smaller than 10B parameters.

The question of why model scale improves chain-of-thought prompting is certainly multi-faceted, and the authors made a preliminary attempt to shed light on it via error analysis. This small analysis involved manually reading 45 errors made by PaLM 62B and categorizing them into semantic understanding (20 errors), one step missing (18 errors), and other errors (7 errors). The "other" category included hallucinations, repetitive outputs, and symbol mapping errors. This categorization is a coarse one borrowed from the initial error analysis done on LaMDA in Appendix D.2, for which categories were conceived based on what improvements were needed to make the chain of thought correct.

As shown in Figure 9, scaling PaLM to 540B parameters fixed a substantial portion of errors in all three categories. Examples of semantic understanding and one-step missing errors that were fixed by scaling PaLM to 540B are given in Figure 10. This result appears consistent with a hypothesis that language models acquire a range of semantic understanding and logical reasoning skills as a function of model scale (though note that model scale is often conflated with other factors, such as amount of training compute).

## Figure 9 [p. 16]

**Figure 9** (p. 16): "Error analysis of 45 problems that PaLM 62B got incorrect. These errors were categorized that semantic understanding, one step missing, and other. The other category includes hallucinations, repetitive outputs, and symbol mapping errors. Scaling PaLM to 540B fixed a substantial portion of errors in all categories."

The figure is a horizontal stacked bar chart titled "Types of errors made by a 62B language model:" with three rows:

- **Semantic understanding:** 62B made 20 errors of this type, 540B fixes 6 of them. The bar shows a portion colored to indicate errors fixed by scaling from 62B to 540B.
- **One step missing:** 62B made 18 errors of this type, 540B fixes 12 of them.
- **Other:** 62B made 7 errors of this type, 540B fixes 4 of them.

The figure supports the claim that scaling fixes errors across all categories, with one-step-missing errors being most amenable to scaling (12/18 fixed).

## Observations on Small Language Model Failure [p. 16]

[p. 16] There are three notable points regarding why small language models fail:

1. Small language models fail at even relatively easy symbol mapping tasks. As demonstrated in Section 5, for even symbolic reasoning tasks that only require generalization to new examples using the same chain of thought logical structure that was given in the few-shot exemplars, small language models still failed.

2. Small language models seem to have inherently weaker arithmetic abilities, as shown by Brown et al. (2020); the ability to do simple arithmetic operations (without semantic understanding) requires sufficient model scale.

3. The authors noticed qualitatively that small language models often did not generate a final answer that could be parsed, due to either repetitions or logic that never arrived at a final answer.

In summary, the success of chain-of-thought reasoning as a result of model scale is a complicated phenomena that likely involves a variety of emergent abilities (semantic understanding, symbol mapping, staying on topic, arithmetic ability, faithfulness, etc). Future work could more thoroughly investigate what properties of pretraining data, model architecture, and optimization objective causally enable such reasoning capabilities.

## Figure 10 [p. 17]

**Figure 10** (p. 17): "Examples of semantic understanding and one-step missing errors that were fixed by scaling PaLM from 62B to 540B."

The figure shows four question-answer examples in a three-column layout (Question | 62B Model Output | 540B Model Output):

1. **Wire cutting problem** (semantic understanding error): "Tracy used a piece of wire 4 feet long to support tomato plants in the garden. The wire was cut into pieces 6 inches long. How many pieces did she obtain?" The 62B model incorrectly computed 4 * 6 = 24 pieces (failing to convert feet to inches). The 540B model correctly converted 4 feet = 48 inches, then 48 / 6 = 8 pieces.

2. **Ship travel problem** (semantic understanding error): "Tom's ship can travel at 10 miles per hour. He is sailing from 1 to 4 PM. He then travels back at a rate of 6 mph. How long does it take him to get back?" The 62B model incorrectly computed the return as 3 * 6 = 18 (confusing distance and time). The 540B model correctly computed 3 hours * 10 mph = 30 miles outbound, then 30 / 6 = 5 hours return.

3. **Grocery bill problem** (one step missing error): "Stephen placed an online order for groceries. His final bill came to $40.00. Because this was through a delivery vendor, they tacked on a 25% fee to his final total and charged him $3.00 in delivery fees. Stephen also added a $4.00 tip. After the extra fees, what was the final price of Stephen's groceries?" The 62B model computed 125% * $40.00 = $50.00 + $3.00 = $53.00 but missed the $4.00 tip. The 540B model correctly computed $40.00 + $10.00 (25%) + $3.00 + $4.00 = $57.00.

4. **Basketball tournament problem** (one step missing error): "There are four schools competing at a basketball tournament. Each school has sent a girls' basketball team and a boys' basketball team and each team has 5 players each. Each school has also sent a coach for each team. In total, how many people have all of the schools sent?" The 62B model counted 4 * 2 * 5 = 40 players and 40 + 4 = 44 coaches (wrong coach count). The 540B model correctly computed 4 schools * 2 teams * 5 players = 40 players, 4 schools * 2 coaches = 8 coaches, total = 48 people.

## A.2 What is the role of prompt engineering? [p. 17–18]

[p. 17] One of the key considerations of prompting is sensitivity to the exact prompt. There is no shortage of work showing that prompts affect language models in unexpected ways (Min et al., 2022). The general way that chain of thought annotations were created was by taking eight exemplars from the training set and decomposing the reasoning process into multiple steps leading to the final answer. Examples of chain of thought annotations are provided in Figure 3, with full prompts given in Appendix G. To analyze how sensitive chain of thought is to prompt engineering, the authors performed robustness experiments with respect to various factors:

- **Different annotators.** Robustness to three different annotators was analyzed (Section 3.4 and Figure 6). Although there is notable variance in performance, chain of thought performed better than the baseline by a large margin for all three annotators on eight datasets in arithmetic, commonsense, and symbolic reasoning (Table 6 and Table 7). Similar to the annotation process in Cobbe et al. (2021), annotators were not given specific instructions about how to write the chain of thought annotations other than to simply write the step-by-step reasoning process that led to the final answer. Thus, the annotations were written in each annotator's own linguistic "chain of thought" writing style.

- **Annotators without machine learning background.** The GSM8K dataset (Cobbe et al., 2021) conveniently provides a training set with reasoning chains written by crowd compute workers, which enables investigation of whether chain of thought still works with reasoning chains from an independent source without a background in machine learning. Three sets of eight exemplars with chains of thought from GSM8K were randomly sampled. These chain of thought annotations also outperformed the baseline by a large margin for all four arithmetic datasets (Table 6), indicating that chain of thought is not dependent on a particular set of annotators.

- **Different exemplars.** The different GSM8K exemplars experiment above (Table 6) also shows that chain-of-thought prompting works for different sets of exemplars. Notably, every set of exemplars was tested on all four arithmetic datasets (instead of picking exemplars from the training set for each dataset), which suggests that the exemplars do not necessarily have to come from the same dataset distribution as the test examples.

[p. 18] - **Different order of exemplars.** Prior work has shown that in some cases (e.g., classification) even the order of prompts matter -- varying the permutation of few-shot exemplars can cause the accuracy of GPT-3 on SST-2 to range from near chance (54.3%) to near SOTA (93.4%) (Zhao et al., 2021). The standard deviation of performance from different exemplars is shown in Table 6 and Table 7. Standard deviations with respect to prompt order are relatively minimal in almost all cases. The one exception is the coin flip task, for which exemplar orders have high standard deviation, likely for the reason cited in Zhao et al. (2021) -- for classification, many exemplars of the same category in a row biases the model outputs.

- **Different number of exemplars.** Gains from chain-of-thought prompting generally still held when there was a varying number of few-shot exemplars. This is shown for five datasets in Figure 11 (compute was not available to run this for all datasets). In preliminary experiments, further increasing the number of exemplars in standard prompting did not lead to significant gains (e.g., increasing from 8 to 16 exemplars did not improve the performance of standard prompting enough to catch up with chain-of-thought prompting).

- **Different language models.** Whether certain prompts that work better for one model work better for other large language models is another interesting question. With the same prompts, chain-of-thought prompting improves performance across all three models (LaMDA, GPT-3, and PaLM) for all datasets except CSQA and StrategyQA for GPT-3 (Table 1, Table 4, Table 5). The fact that gains from chain of thought did not transfer perfectly among models is a limitation; further work could investigate why how different pre-training datasets and model architectures affect the performance gain from chain-of-thought prompting.

**Prompt engineering still matters, though.** Although the results are relatively robust to the prompt for arithmetic reasoning, prompt engineering still does matter, and can improve performance significantly in many cases. Though most chain of thought annotations outperform standard prompting, there is large variation in many cases. For instance, for the coin flip task, the performance varied from 99.6% for Annotator A to 71.4% for Annotator C, though both were above standard prompting = 50.0% (see Table 7). There are even tasks where prompt engineering is a requirement for good performance. In preliminary experiments, the authors tried using chain of thought to enable language models to reverse the order of a list of 5 items. While two co-authors were not able to write chain of thought prompts that solved the task despite their best attempts, a third co-author was able to write a chain of thought that perfectly solved the task.

How to generate chain of thought annotations in a robust fashion could be an interesting direction for future work. For instance, an idea could be to use a large language model to automatically generate chains of thought via prompting (and potentially optimize this over a validation set).

## A.3 Will chain-of-thought prompting improve performance for my task of interest? [p. 18–19]

[p. 18–19] While chain-of-thought prompting is in principle applicable for any text-to-text task, it is more helpful for some tasks than others. Based on the experiments in this paper, the authors' intuition is that chain of thought helps the most when three conditions are met: (1) the task is challenging and requires multi-step reasoning, (2) a large language model is used, and (3) the scaling curve is relatively flat. Conversely, the benefits are smaller when one or more of these conditions are not met.

These intuitions are perhaps best supported by the arithmetic reasoning results. The performance gain from chain-of-thought prompting is largest for PaLM 540B on GSM8K (challenging multi-step problems, flat scaling curve), which meets these conditions. The performance gain is small for the subsets of MAWPS that only require one or two steps (SingleOP, SingleEq, and AddSub), for which PaLM 540B already achieves performance of 90% or higher (and it is also generally true that there is less headroom for improvement when performance is already strong).

Although the paper focused on multi-step reasoning tasks (arithmetic, commonsense, and symbolic), chain-of-thought prompting can potentially be applied to any task for which humans use a "chain of thought" to solve (at least in principle). The empirical evaluation of chain-of-thought prompting on such diverse tasks (e.g., machine translation, etc.) is left to future work.

## A.4 Why is prompting with the equation only not enough for some arithmetic reasoning datasets? [p. 19]

[p. 19] Prompting with the equation only as an intermediate step does help on many datasets, especially when the datasets only require a few reasoning steps (SVAMP, ASDiv, MAWPS). For GSM8K, however, using the equation only did not improve performance substantially. Based on qualitative analysis, the authors believe that these questions are too semantically challenging for the model to directly translate them into a math equation. Consider this example from LaMDA 137B:

> **Question:** Mike plays ping pong for 40 minutes. In the first 20 minutes, he scores 4 points. In the second 20 minutes, he scores 25% more points. How many total points did he score?

> **Equation only (wrong answer):** (4 + 20 * 0.25) = 6. The answer is 6.

> **Chain of thought (correct):** Mike played ping pong for 40 minutes. In the first 20 minutes, he scored 4 points. In the second 20 minutes, he scored 25% more points. So he scored 25% more in the second 20 minutes. 4 x 1.25 = 5. So he scored 5 points in the second 20 minutes. So he scored 9 points in total. The answer is 9.

It is hard for the model to directly translate all of the semantics into a single equation, but chain of thought allows it to better reason about each part of the question via intermediate steps in natural language.
