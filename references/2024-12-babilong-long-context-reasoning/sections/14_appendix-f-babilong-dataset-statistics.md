# Appendix F: BABILong Dataset Statistics [p. 20-21]

The proposed benchmark includes 20 diverse tasks, ranging from simple "needle in a haystack" scenarios with distractor facts to more complex tasks that require counting, logical reasoning, or spatial reasoning. The Figure 7 evaluates the complexity of the base short versions of these tasks. Tasks such as QA1, QA5, and QA10 are generally easier for most models, whereas QA7, QA15, and QA19 are the most challenging. The plot clearly shows that the number of facts needed for reasoning significantly impacts task complexity, as performance gradually declines from QA1 to QA2 and QA3, which differ in the number of supporting facts. The distribution of task labels is shown in Table 6. [p. 20]

**Figure 7** (p. 21): "The performance of LLMs on the bAbI (BABILong without distractor text) depends significantly on the task complexity. Each dot represents the average accuracy of the model on one thousand samples of the given task. The median accuracy across all models is denoted by black stars."

Description: Scatter plot showing accuracy (%) vs. task
- Key elements: Y-axis shows accuracy 0-100%, x-axis shows tasks qa0 through qa20; multiple colored dots for different models (gpt-4-0125-preview, Mixtral-8x22B-instruct-v-0.1, Phi-3-medium-128k-instruct, yi-34B-200k, Phi-3-mini-128k-instruct, Mixtral-8x7B-instruct-v-0.1); black stars indicate median
- Notable patterns: High accuracy (>75%) for tasks qa0-qa5, qa10; moderate accuracy (25-75%) for most middle tasks; very low accuracy (<25%) for qa7, qa15, qa17, qa19, qa20; high variance across models for most tasks; median performance shows clear task difficulty gradient
- Supports claim: Task complexity varies significantly across the 20 BABILong tasks, with some tasks being substantially more challenging than others [p. 21]

BABILong is a generative benchmark, allowing it to be scalable and increasingly demanding length of language models. The same bAbI task can be scaled to any desired length in tokens by adding a sufficient number of distractor sentences. For reproducibility, we pre-generate dataset splits for several fixed lengths: 0k (tasks with no distractor sentences), 4k, 8k, 16k, 32k, 64k, 128k, 512k, 1M and 10M tokens. The length in tokens is measured using the classic GPT-2 tokenizer, which is close in fertility to the popular GPT-4 tokenizer. As shown in Table 5, the number of tokens for tokenizers of different models may differ for samples in the same split. However considering the trade-off between the sequence length and embedding layer size, we believe the comparison remains fair. [p. 21]

**Table 5** (p. 21): "Token count for various models across selected tasks. We measure the length of BABILong samples using the conservative GPT-2 tokenizer. Actual token sizes may vary depending on the model tokenizer."

| Model | 0k | 4k | 16k | 64k | 128k |
|-------|-----|------|-------|--------|---------|
| GPT-4 | 120 | 3544 | 15071 | 61343 | 123367 |
| GPT-2 | 120 | 3700 | 15699 | 63698 | 127695 |
| Llama-2 | 135 | 3942 | 16757 | 68110 | 137222 |
| Mistral | 128 | 3863 | 16438 | 66862 | 134592 |
| Words | 98 | 2548 | 10789 | 44180 | 88592 |
| Symbols | 561 | 14507 | 61452 | 251947 | 507598 |

**Table 6** (p. 21): "The distribution of labels in first five BABILong tasks, % of all samples."

| Task | LABEL1 | LABEL2 | LABEL3 | LABEL4 | LABEL5 | LABEL6 | LABEL7 |
|------|--------|--------|--------|--------|--------|--------|--------|
| QA1 | 15.4 | 14.9 | 15.7 | 18.7 | 18.2 | 17.1 | - |
| QA2 | 15.9 | 18.7 | 16.7 | 16.5 | 17.5 | 14.6 | - |
| QA3 | 13.3 | 18.4 | 21.5 | 14.6 | 15.4 | 16.7 | - |
| QA4 | 15.6 | 17.7 | 16.6 | 17.1 | 15.3 | 17.6 | - |
| QA5 | 9.5 | 18.8 | 12.9 | 16.4 | 13.6 | 18.9 | 9.8 |
