# 1 Introduction [p. 1–2]

[p. 1] Large language models (LLMs) have been improving at an incredible pace, solving problems that seemed out of reach without any task-specific training examples (Wei et al., 2022a; Ouyang et al., 2022; OpenAI, 2023). As commercial LLMs are adopted worldwide, it becomes clear that they must also operate successfully over long sequences, such as conversation histories or scientific documents. However, current LLM benchmarks that do evaluate models in a zero-shot setting, such as HELM (Liang et al., 2022) and BigBench (Srivastava et al., 2022), mostly focus on short sequences; BigBench, for example, has an average of 77 words per input.

To fill this gap, the authors introduce ZeroSCROLLS: Zero-Shot CompaRison Over Long Language Sequences, a benchmark for zero-shot long text reasoning over natural language, and conduct a thorough investigation of state-of-the-art LLMs.

ZeroSCROLLS extends SCROLLS (Shaham et al., 2022), a long text understanding benchmark that enables fine-tuning, adding four additional tasks: query-based summarization, multi-hop question answering, sentiment aggregation, and sorting book chapter summaries. The latter two tasks are specifically designed to examine a model's ability to aggregate and compare information across long sequences, while keeping evaluation simple and accurate. ZeroSCROLLS is designed to test *zero-shot* capabilities, and contains test sets with simple natural prompts and private gold references, small validation sets, and no train data. It has a live leaderboard to enable transparent and dynamic progress. Figure 1 shows the state of the leaderboard based on the experiments, and Figure 2 shows a per-task breakdown of a selected subset of models. [p. 1]

[p. 2] The authors use this new testbed to perform extensive evaluation and analysis across state-of-the-art open and closed models. Key findings:

- On question answering tasks, zero-shot LLMs bridge the gap with task-specific fine-tuned models; GPT-4 sets a new state of the art on the challenging QuALITY task (Pang et al., 2022), almost reaching human performance.
- In contrast, LLMs generally struggle to obtain such high scores for summarization tasks without a training set from which to learn the nuances and artifacts of each dataset, even though GPT-4 does approach the fine-tuned state of the art on two of three datasets.
- Two of the new tasks, sentiment aggregation and sorting book chapter summaries, prove exceptionally challenging for all LLMs, with only GPT-4 surpassing the naive baseline in each task.

The authors note that when analyzing GPT-4 responses, they often find correct answers that do not match the requested format; e.g. producing a full sentence when asked to answer in a single phrase. This problem is not unique to GPT-4. While ZeroSCROLLS is primarily aimed at facilitating research in understanding long texts, the authors encourage the community to use this benchmark to advance research in instruction understanding, prompt engineering, and evaluation of generated texts as well. [p. 2]

**Figure 1** (p. 1): "ZeroSCROLLS measures the average performance of state-of-the-art language models across 10 long text understanding tasks. The maximal amount of tokens each model can process is given in parentheses."

The figure is a horizontal bar chart showing average ZeroSCROLLS scores. Models from bottom (highest) to top (lowest):
- GPT-4 (8k): 41.7
- Claude (8k): 39.1
- ChatGPT (4k): 34.0
- DaVinci003 (4k): 33.7
- Flan-UL2 (8k): 30.6
- Flan-T5 (8k): 29.9
- Naive: 19.6
- T0pp (8k): 14.3

**Figure 2** (p. 2): "Per task scores of various LLMs and other baselines. In parentheses: the maximum number of tokens."

Three grouped bar charts showing per-task scores for Naive, Flan-UL2 (8k), Claude (8k), GPT-4 (8k), and CoLT5 (16k) - finetuned:

Left panel (Summarization tasks):
- GovReport: Naive 22.6, Flan-UL2 16.1, Claude 24.2, GPT-4 26.3, CoLT5 41.0
- SummScreenFD: Naive 6.7, Flan-UL2 11.5, Claude 16.1, GPT-4 17.3, CoLT5 20.0
- QMSum: Naive 6.7, Flan-UL2 13.6, Claude 14.6, GPT-4 18.5, CoLT5 22.5
- SQuALITY: Naive 10.5, Flan-UL2 5.7, Claude 21.0, GPT-4 22.6

Middle panel (QA tasks):
- Qasper: Naive 6.1, Flan-UL2 56.9, Claude 52.3, GPT-4 50.7, CoLT5 53.1
- NarrativeQA: Naive 2.1, Flan-UL2 25.5, Claude 32.6, GPT-4 27.6, CoLT5 31.0
- QuALITY: Naive 26.6, Flan-UL2 75.6, Claude 84.8, GPT-4 89.2, CoLT5 47.0
- MuSiQue: Naive 20.0, Flan-UL2 51.3, Claude 36.1, GPT-4 41.1

Right panel (Aggregation tasks):
- SpaceDigest: Naive 45.0, Flan-UL2 36.0, Claude 61.6, GPT-4 62.8, CoLT5 [not shown]
- BookSumSort: Naive 50.0, Flan-UL2 14.0, Claude 47.4, GPT-4 60.5, CoLT5 [not shown]

Code is available online at https://github.com/tau-nlp/zero_scrolls. Live leaderboard at https://www.zero.scrolls-benchmark.com/.
