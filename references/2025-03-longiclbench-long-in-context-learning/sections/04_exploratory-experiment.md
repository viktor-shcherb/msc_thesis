# Exploratory Experiment [p. 8-10]

Inspired by the Lost in the Middle phenomenon (Liu et al., 2023), we take analysis experiments to explore whether the position distribution of the instances will make a difference in the performance for long in-context learning with extreme-label classification tasks [p. 8].

## 4.1 Scattered Distribution [p. 8-9]

In our investigation, we conduct pilot experiments on TacRED, a medium-complexity dataset, with each label type demonstrated three times, resulting in a total of 123 distinct instances (calculated as 41 × 3) [p. 8].

Within these experiments, instances bearing the same labels are distributed randomly to form a scattered configuration. For each instance, we track its relative position within the prompt alongside its corresponding label, thereafter computing the accuracy for each label class. As illustrated in the first row of Figure 4, the visualization demonstrates the accuracy at each aligned with its position within the prompt, where diverse colors symbolize various label types. In scenarios where class instances are scattered, certain models, such as InternLM2-7B-base, demonstrate acceptable performances—approximately 60% accuracy merely on specific labels, as highlighted by a red circle in Figure 4, regardless of the instance placements. Conversely, other models, like ChatGLM3-6B-32K, exhibit robust performance across a broad spectrum of labels. Remarkably, the GPT4-turbo model consistently surpasses an 80% accuracy threshold for the majority of label types, with only a minimal count of exceptions [p. 9].

**Figure 4** (p. 9): "Visualization of accuracy for every class when instances from the same class are scattered V.S. grouped in the demonstration prompt."

Description: Six scatter plots arranged in 2 rows × 3 columns
- Top row shows "Scattered" distribution for InternLM2-7B-base, ChatGLM3-6B-32K, and GPT4-turbo
- Bottom row shows "Grouped" distribution for the same three models
- X-axis: Instance Position (0-125)
- Y-axis: Class Accuracy (%) (0-100)
- Each colored dot represents a class instance
- Notable patterns:
  - InternLM2-7B-base Scattered: Shows clustering around 60-80% for specific labels (circled in red), with many instances near 0%
  - ChatGLM3-6B-32K Scattered: Distributed more evenly across accuracy levels
  - GPT4-turbo Scattered: Majority of points above 80% accuracy threshold
  - InternLM2-7B-base Grouped: Shows clear horizontal bands (circled in red as "pertile")
  - ChatGLM3-6B-32K Grouped: Instances clustered near bottom (low accuracy)
  - GPT4-turbo Grouped: More distributed pattern, generally high accuracy
- Supports claim: Models have different sensitivity to position distribution of examples in prompts

## 4.2 Grouped Distribution [p. 9-10]

To facilitate a clear comparison between scattered and grouped distributions, we organize instances of the same class to be adjacent within the demonstration prompts. The impact of this reorganization on model performance, both pre and post-grouping, is presented in subsection A.3. It is easy to observe that there is a general decline in performance across most models after grouping instances by class. Notably, models such as Mistral and InternLM2 exhibit significant performance drops, underscoring a pronounced sensitivity to instance grouping. In an effort to delve deeper into this phenomenon, we visualize the accuracy of grouped labels in relation to their positions within the prompt, as illustrated in Figure 4. This visualization reveals that instances of the same class, denoted by dots of the same color, are positioned nearby. It became evident that some models, like InternLM2 or ChatGLM3-6B, as highlighted in subsection A.3, demonstrate high sensitivity to the distribution of instances, only handling instances with labels positioned at the end of the prompt. Conversely, other open-source models such as ChatGLM3-6B-32K, with a modest 3.3% drop in averaged performance, proved to be more resilient to changes in instance positioning. Surprisingly, even the GPT4-turbo and Gemini1.5-Pro are not immune to the challenges posed by grouped distributions, experiencing a notable decline in performance by 20.3% and 22.3%. This observed decrease in performance is consistent across models, unaffected by the specific positions of the labels within the prompt [p. 9-10].

The potential reasons why there is a substantial drop in performance after grouping the labels in demonstrations are worthy of further research to explore and offer valuable insights for future research and development in this area. One of the potential explanations is that Large Language Models can develop biases based on the position of examples within the prompt. Grouping similar examples together may accidentally reinforce such biases, leading the model to overfit to specific patterns associated with certain positions (like the end or the beginning of the demonstration context). Scattering demonstrations helps distribute examples more evenly, reducing the likelihood of position-induced biases as discussed in Lost-in-the-Middle (Liu et al., 2023) [p. 10].
