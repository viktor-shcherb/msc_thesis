# 12.18. More BetterChartQA Details and Results [p. 149–154]

[p. 150] Chart and plot understanding has been a particularly challenging domain for large multimodal models. While state-of-the-art models have been achieving high scores on popular chart/plot benchmarks such as ChartQA and MathVista, the authors note that the benchmarks can have templatic questions and narrow distribution of chart styles, ending up with a poor coverage of real-world cases. Besides, existing chart benchmarks usually conflate multiple challenges in one query and thus are hard to pin down where the models fail exactly.

## BetterChartQA Benchmark Construction [p. 150]

[p. 150] The authors construct an internal benchmark called BetterChartQA, composed of 374 challenging QA pairs split into 9 disjoint capability buckets (a comprehensive list is shown in Figure 32 together with by-capability performance of different Gemini models and GPT-4 Turbo). The chart images are randomly sampled from the web (news articles, government reports, academic papers, etc.) and QA pairs are written by professional human annotators. Gemini 1.0 Pro is used to judge whether a model's response is equivalent to the gold answer allowing 5% numerical error if the answer is numerical, in line with prior work in chart QA (Liu et al., 2023; Masry et al., 2022). All models are tested in a 0-shot manner.

## Prompts [p. 150–151]

[p. 150] The exact prompts for tested models and the judge are below.

Model prompt:

```
Answer the following question about the image using as few words as possible. Question: {
question} <image> Answer:
```

[p. 150–151] Template for language model evaluator (judging whether ground truth and model answer are equivalent):

```
Question: {question}
Model's answer: {prediction}
Reference answer: {ground truth}
Model's answer is exactly the same as the reference answer (for numerical answers,
tolerate 5% numerical error) [Yes/No]:
```

## BetterChartQA Results [p. 151]

[p. 151] Overall, the micro-averaged performance of the compared models in Figure 32 are 50.3% (GPT-4 Turbo), 43.0% (Gemini 1.0 Pro), 47.9% (Gemini 1.0 Ultra), 59.0% (Gemini 1.5 Flash), and 65.8% (Gemini 1.5 Pro). Gemini 1.5 Pro outperforms the previous generation of Gemini 1.0 Pro by more than 20%. In fact, the smallest class model Gemini 1.5 Flash is more than 10% better than Gemini 1.0 Ultra, with significant gains across all capability buckets.

[p. 151] Compared to Gemini 1.0 models, the improvement is especially strong in multi-figure, table, chart in context (screenshots containing charts), and scatter plot categories. Both Gemini 1.5 models (Flash and Pro) achieve overall higher scores than GPT-4 Turbo. Gemini models are especially stronger in parsing complex multi-series charts and also extracting numbers from charts (when numerical values are not explicitly written as text).

## Figure 32: By-Capability Performance on BetterChartQA [p. 154]

**Figure 32** (p. 154): "By-capability performance of Gemini different models on BetterChartQA."

The figure is a horizontal bar chart showing accuracy (%) on the x-axis (0 to 80+) for 9 capability buckets on the y-axis, with 5 models compared: GPT-4 Turbo (gray), Gemini 1.0 Pro (pink), Gemini 1.0 Ultra (red), Gemini 1.5 Flash (cyan), and Gemini 1.5 Pro (dark blue). The capability buckets and number of examples are:

- **overall (374; micro average):** Gemini 1.5 Pro leads at ~65.8%, followed by Gemini 1.5 Flash at ~59.0%, GPT-4 Turbo at ~50.3%, Gemini 1.0 Ultra at ~47.9%, and Gemini 1.0 Pro at ~43.0%.
- **multi_series (73):** Gemini 1.5 Pro leads; all models cluster between ~40–70%.
- **number_extraction (64):** Gemini 1.5 Pro leads strongly; GPT-4 Turbo trails noticeably.
- **numerical_reasoning (48):** Gemini 1.5 Pro leads; gains visible over 1.0 generation.
- **multi_figures (37):** Gemini 1.5 models show clear improvement over 1.0 models.
- **table (29):** All models score relatively high; GPT-4 Turbo is competitive here.
- **chart_in_context (47):** Strong improvement for Gemini 1.5 models over 1.0 models.
- **flowchart (22):** Gemini 1.5 Pro leads; scores cluster in ~40–65% range.
- **scatter_plot (17):** Large improvement for Gemini 1.5 models; 1.0 models score low.
- **other (37):** Moderate scores across all models.

The chart supports the claim that Gemini 1.5 Pro outperforms all other models across all capability buckets, with especially strong gains in multi-figure, table, chart_in_context, and scatter_plot categories relative to Gemini 1.0 models.

## Figure 31: BetterChartQA Examples [p. 149]

**Figure 31** (p. 149): "Examples of questions and gold answers from BetterChartQA."

The figure shows three example chart types from the BetterChartQA benchmark, each with an associated question and ground truth answer:

- **Multi-figures:** A multi-panel figure plotting recalls (y axis) against number of few-shot training examples (x axis). First row is text->image R@1, R@5, R@10 respectively; second row is image->text R@1, R@5, R@10. Question: "In which two setups do we see T2 clearly outperforming T1 all the time, regardless of number of training examples?" Ground truth: "R@1 - text to image, and R@10 - text to image."
- **Scatter plot:** A scatter plot with x-axis labeled sqrt(C_SP) (0 to 0.6) and y-axis labeled sqrt(L_EFF) (0 to ~12), showing EV diameter (nm) from ~50 to ~200. Question: "At what location is there a peak in the scatterplot? a) (0.1, 1.5) b) (0.2, 1.5) c) (0.2, 4) d) (0.1, 4)." Ground truth: "a".
- **Flowchart:** A complex bioinformatics pipeline flowchart with preprocessing step, query step, and output steps, including database construction and sequence mapping. Question: "In which step does building MySQL based relational database happen?" Ground truth: "Preprocessing Step."
