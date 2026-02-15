# 3 Experiments [p. 5–6]

## 3.1 Experimental Setup [p. 5–6]

### Models [p. 5]

We selected ten long-context large language models (LLMs), comprising eight open-source and two closed-source models. These models range in size from 7B to 72B parameters, with one featuring a Mixture of Experts (MoE) architecture. The claimed context lengths of these models vary from 32K to 128K tokens⁸. These models were selected to represent a diverse array of architectures,

---

[p. 6 continued]

covering both Mixture of Experts and standard transformer designs, as well as a range of parameter sizes. This diversity ensures a comprehensive evaluation of their ability to handle long-context tasks [p. 6].

**Algorithm 1** Evaluations Pipeline [p. 6]

```
Initialization:
1: Task instructions → T
2: Tested long context LM → model
3: Set of Special Task Instruction for evaluation matching → Check_Set

Main Process:
4: Use Tested model to get Answer for T → A
5: A → {A₁, A₂, ..., Aₙ}, split into subtasks
6: empty set for storing evaluations → E
7: for each Tᵢ in Check_Set do
8:     if there is Aᵢ matching Tᵢ then
9:         eval(Aᵢ, Tᵢ) → Eᵢ
10:        E → Add Eᵢ to E
11:    end if
12: end for
13: ∑ E → Score, compute the final completion score
14: return Score
```

### Inference Setup [p. 6]

We utilized the vLLM (Kwon et al., 2023) system, which optimizes key-value (KV) cache memory for efficient large-scale inference. This system is crucial for handling long-form generation efficiently, reducing memory overhead, and maximizing inference throughput. Inferences were performed using BFloat16 precision on 8× NVIDIA A800 GPUs, employing greedy decoding to generate the outputs. This setup ensured consistency and efficiency in the inference process [p. 6].

### Task Configurations [p. 6]

For each scenario, we generated 800 examples at two specified lengths: 16K tokens and 32K tokens. The generation used designated templates for each model, ensuring task-specific relevance. The tasks were selected to reflect both creative and technical long-form generation challenges, such as diary writing, menu planning, and skyscraper design. To ensure the relevance of the generated content and prevent off-topic responses or refusals to answer, we prefixed each task input with a carefully curated answer prompt designed to guide LLMS toward output. The tasks were specifically selected to test the models' ability to generate instruction-following long-form content in both creative and technical contexts. For example: In the Urban Planning task, models were tasked with generating detailed designs for a new urban district, including descriptions of key facilities such as parks, schools, and transportation systems [p. 6].

### Evaluation Metric [p. 6]

We evaluated model performance using the three metrics defined in Section 2.4: Main Task Completion, Specific Task Instruction Completion-1 (STIC-1), and Specific Task Instruction Completion-2 (STIC-2). These metrics provided a comprehensive assessment of the models' ability to adhere to instructions and generate coherent long-form text [p. 6].

## 3.2 Main Result [p. 6]

The results of the long-form text generation tasks for both Short-version (16K) and Long-version (32K) tokens are summarized in Table 3 [p. 6].

**Main Task Completion.** Significant disparities in performance across models primarily stem from differences in architecture and training datasets. Notably, models with varying parameter sizes, such as LLama3.1-8B-instruction (Dubey et al., 2024) (over 8 billion parameters), Qwen-72B (Yang et al., 2024) (over 20 billion parameters), and GPT-4o-mini (OpenAI, 2024a) (a closed-source model), have demonstrated superior efficacy, successfully completing most primary tasks in full. In contrast, some models struggle with these tasks, exhibiting limitations such as: 1) models responding solely to specified subtasks, neglecting others, and 2) models halting after only completing the initial task segment, despite prompts requiring full sequential subtask completion. This issue may originate from the current instructional tuning data, which could cause partial responses in complex, lengthy tasks [p. 6].

---

[p. 7 continued]

**Table 3** (p. 7): Long-form generation Performance of selected models evaluated at length from 16k and 32k. The weighted average score (wAvg) is used to represent the model's final performance at the given task length. Note that the GPT-4-32K is currently closed for use, and the longest versions that can be used are the GPT-4o and GPT-4o-mini 16K output limitation.

| Models | Claimed Length | Short-version (16K) |  |  |  |  | Long-version (32K) |  |  |  |
|--------|----------------|---------------------|--|--|--|--|--------------------|--|--|--|
|  |  | CR | STIC-1 | STIC-2 | Len. | wAvg | CR | STIC-1 | STIC-2 | Len. | wAvg |
| **Models with 7-10B Parameters** |  |  |  |  |  |  |  |  |  |  |  |
| Mamba-2.8B | 2K | 11.3% | 23.8% | 2.1% | 902 | 0.2% | 5.6% | 29.8% | 1.6% | 864 | 0.1% |
| FILM-7B | 32K | 36.0% | 22.4% | 9.0% | 6280 | 3.2% | 37.4% | 30.9% | 10.9% | 13775 | 4.1% |
| Mistral-v0.2-7B | 32K | 81.8% | 25.7% | 20.4% | 7296 | 16.7% | 48.2% | 35.4% | 15.7% | 16146 | 7.6% |
| Phi-3-mini-3.8B | 128K | 22.9% | 27.6% | 5.4% | 4165 | 1.2% | 7.4% | 46.9% | 2.4% | 2613 | 0.2% |
| LLama3.1-8B | 128K | 93.5% | 23.4% | 22.0% | 8804 | 21.6% | 77.6% | 28.9% | 20.6% | 17354 | 16.0% |
| Qwen2-7B | 128K | 60.0% | 23.3% | 13.5% | 5138 | 8.1% | 40.0% | 31.7% | 12.6% | 9617 | 5.0% |
| LongWriter-llama3.1-8B | 128K | 46.0% | 32.6% | 14.2% | 11036 | 6.5% | 34.5% | 36.3% | 10.8% | 19925 | 3.7% |
| **Models Larger Than 20B Parameters** |  |  |  |  |  |  |  |  |  |  |  |
| Mistral-8x7B | 32K | 83.0% | 34.4% | 28.1% | 8113 | 22.6% | 60.5% | 36.3% | 20.3% | 15839 | 12.3% |
| Phi-3.5-8x7B | 128K | 26.9% | 46.4% | 11.3% | 5430 | 3.0% | 7.4% | 62.9% | 6.0% | 6633 | 0.4% |
| LLama3.1-70B | 128K | 79.3% | 34.4% | 29.2% | 8055 | 23.1% | 63.1% | 43.3% | 26.3% | 15197 | 16.6% |
| Qwen2-72B | 128K | 94.4% | 29.7% | 27.1% | 8013 | 25.5% | 66.2% | 34.4% | 21.7% | 19845 | 14.4% |
| **Closed-source Model** |  |  |  |  |  |  |  |  |  |  |  |
| GPT-4o-mini | 128K | 97.0% | 34.8% | 33.4% | 8940 | 32.4% | – | – | – | – | – |
| GPT-4o | 128K | 67.2% | 42.9% | 24.4% | 9055 | 15.3% | – | – | – | – | – |

Especially in GPT-4o (OpenAI, 2023), it recognizes that this task will generate a long output and only provides a few examples [p. 7].

**STIC-1 and STIC-2.** The STIC-1 metric revealed strong performance in adhering to task instructions for models like LLama3.1-70B and GPT-4o-mini, particularly in shorter sequences [p. 7]. However, a significant drop in STIC-2 scores for several models indicates that maintaining instruction adherence over longer text sequences remains a challenge. This performance degradation emphasizes the need for better tuning and architectural modifications to improve long-term coherence [p. 7].

A common failure mode observed across multiple models was the tendency to forget or misinterpret instructions as the sequence length increased. For example, in the Skyscraper Design task, some models correctly described the initial few floors but deviated from the original plan as the task progressed, particularly in the 32K token setting. This highlights the memory retention issue in long-context models, which often leads to a loss of coherence and adherence to task instructions. Examples of failures where models struggled to follow instructions are provided in Appendix F [p. 7].

**Length (Number of words).** We calculated the average output word count for models that consistently completed all subtasks, achieving an 80% completion rate in sub-scenarios, excluding data from unsuccessful attempts. Most models substantially exceeded previous benchmarks for long-form generation tasks in terms of output length. Notably, the LongWriter (Bai et al., 2024) model excelled, efficiently meeting word count requirements for each subtask. Given the results and the weighted average score (wAvg) of 16k, the open-source Qwen2-72B and the closed-source GPT-4o models demonstrated optimal performance. At a sequence length of 32K, the LLama3.1-8B model, outperformed models with larger parameters, highlighting its efficiency in managing extended lengths [p. 7].

## 3.3 Accuracy Trend with Varying Sequence Length [p. 7–8]

As illustrated in Figure 2, there is a clear decline in model performance as output length increases. Models exhibited strong adherence to initial instructions at shorter sequence lengths, but performance gradually degraded as the text generation extended beyond the 4,000-token threshold. This degradation aligns with trends identified in the NIAH dataset and underscores the challenge of maintaining instruction adherence and coherence over long outputs [p. 7–8].

**Figure 2** (p. 8): "The right side of the figure illustrates the model's performance on specific instruction tasks at 16K as sequence length increases, whereas the left side depicts performance at 32K. All curves have been smoothed with a Moving Average."

Description: Two line plots showing accuracy trends.
- Key elements: Left plot shows performance curves for multiple models (GPT_4o_mini, LongWriter, Llama-3.1-8B, Llama-3.1-70B, Mistral-7B, Mistral-8x7B, Qwen2-7B, Qwen2-72B) at 16K token setting with x-axis showing sequence length and y-axis showing Acc. Right plot shows the same models (excluding GPT_4o_mini) at 32K token setting.
- Notable patterns: All models show declining performance as sequence length increases beyond 4,000 tokens. Performance drops are more pronounced in the 32K setting. Most curves show initial high performance (around 0.4-0.5) degrading to lower levels (around 0.2) as sequence length extends.
- Supports claim: Demonstrates the performance degradation challenge in long-form generation tasks.

This deviation becomes particularly pronounced when outputs exceed 4,000 tokens, where adherence to instructions significantly diminishes, and further deterioration is observed as outputs approach 16,000 tokens. In contrast, tasks involving shorter outputs, such as those in the NIAH dataset or simpler multi-needle tasks, showed near-perfect performance, highlighting the disparity in model behavior across different sequence lengths [p. 8].

Potential reasons for this decline include limitations in the self-attention mechanism used in transformers, which may struggle to maintain meaningful context over long sequences. Additionally, models trained with limited long-form data may overfit to shorter patterns, leading to a loss of coherence in extended generations. These findings suggest that architectural changes or improved training strategies may be necessary to overcome these challenges in future iterations of LLMs [p. 8].

## 3.4 Three Specific Task Instructions [p. 8]

Figure 3a presents the model's performance metrics across various task types: single, range, and periodic. The model demonstrated comparable proficiency in both single and range tasks, reflecting its capability to follow direct and straightforward instructions effectively. However, the slight reduction in performance for range tasks suggests that additional complexity, such as processing multiple data points within a defined range, introduces a marginal increase in cognitive load for the model [p. 8].

The most significant decline in performance was observed in periodic tasks, where the model struggled to interpret instructions that required recurring events, such as "every four weeks starting from week 10." These tasks demand a higher degree of reasoning and temporal awareness, which may challenge the model's capacity to maintain consistency over extended sequences. As a result, outcomes for periodic tasks were considerably poorer compared to single and range tasks, which have clearer and more well-defined parameters. The model's performance hierarchy can generally be summarized as single > range > periodic, highlighting the increased difficulty associated with periodic tasks. This trend underscores the need for future improvements in long-context models, particularly in handling more complex, time-based instructions [p. 8].

## 3.5 Comparison with Long-Context Input [p. 8–9]

We examine the relationship between a model's ability to handle long inputs and its performance on long outputs. Specifically, we investigate whether a model's capacity to manage long-range inputs corresponds to improved performance on long-range outputs. For this analysis, we use the RULER dataset, a synthetic benchmark designed to evaluate long-context length and task complexity, making it ideal for comprehensive evaluations of long-context LLMs. We compare the models' performance on sequences of the same length, as shown in Figure 3b, which indicates a significant performance gap between input handling and output performance. At 16K tokens, the Pearson correlation coefficient is 0.51, while at 32K tokens, it increases to 0.66, suggesting that there is some overlap in the skills required for managing long inputs and generating long outputs, but these tasks are not entirely equivalent [p. 8–9].

**Figure 3a** (p. 9): (a) Performance Comparison on three tasks settings

Description: Bar chart showing performance comparison across three task types.
- Key elements: Three groups of bars (Single(SI), Range(RI), Periodic(PI)) with different colored bars representing different models (GPT_4o_mini, Llama-3.1-8B, Llama-3.1-70B, Mistral-7B, Mistral-8x7B, Qwen2-7B, Qwen2-72B). Y-axis shows Acc from 0.00 to 0.40. Red dashed horizontal line represents average for each category.
- Notable patterns: Performance decreases from Single to Range to Periodic tasks. Single tasks show scores around 0.30-0.35, Range tasks around 0.20-0.25, and Periodic tasks around 0.10-0.20.
- Supports claim: Demonstrates the performance hierarchy single > range > periodic.

**Figure 3b** (p. 9): (b) Performance Comparison on Ruler and LongGenBench Tasks

Description: Line plot showing correlation between Ruler and LongGenBench performance.
- Key elements: Two pairs of lines comparing performance at different sequence lengths (Llama3.1-8B, Llama3.1-70B, Mistral-8x7B, Qwen2-7B, Qwen2-72B). X-axis shows different tasks/models, Y-axis shows scores from 0 to 100. Red lines represent Ruler (16K) and Ruler (32K), blue lines represent LongGenBench (16K) and LongGenBench (32K).
- Notable patterns: Ruler performance is consistently higher (60-90 range) than LongGenBench performance (20-40 range), showing a significant performance gap.
- Supports claim: Demonstrates significant performance gap between input handling (Ruler) and output generation (LongGenBench).

Handling long inputs primarily requires the model to retain and process existing information, while generating long outputs demands more complex reasoning, memory retention, and coherence management over extended sequences. Thus, models that excel in long-input retrieval may still struggle with long-form generation, particularly in tasks requiring strict instruction adherence over time. This distinction highlights the need for models to be optimized for both input handling and output generation to achieve consistent performance in long-context tasks [p. 9].

---

⁸Detailed specifications of these models are provided in Appendix D.
