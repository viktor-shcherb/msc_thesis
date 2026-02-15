# Appendix D: Detailed LLMs evaluation on BABILong QA1-5 tasks [p. 18-19]

Here we present the complete results of LLMs evaluation. Table 4 showcases the performance of 38 models across the first five tasks. Comparing the tasks in the table makes evident the difference in task complexity for language models. QA1 is the easiest, with most models achieving over 70% accuracy for the 0k split. QA4 is significantly more challenging, and only 5 models can reach this level of performance. QA2 and QA3 pose even greater challenges for most models. [p. 18]

The number of parameters positively impacts accuracy on the shortest 0k split. Among non-finetuned models, GPT-4, Phi-3-medium, Qwen, Jamba, Command-R, Yi-34B and Mixtral 8x22B consistently outperform smaller models. Notably, RWKV and Mamba-2.8B also demonstrate strong performance on QA2 and QA3. However, as the context length increases, some of the largest models lose their advantage over smaller ones. [p. 18]

**Table 4** (p. 19): "Results of LLM evaluation on the first five tasks of BABILong. Rows correspond to sequence lengths, columns denote models, and each section represents a separate task from QA1 to QA5. Each number indicates the average accuracy of the model at a given sequence length, calculated over 1000 samples for lengths up to 32k tokens, and over 100 samples for longer lengths."

The table contains results for 38 models across context lengths from 0k to 10M tokens. Selected results for representative models:

**QA1 (Single Supporting Fact) - Sample of models:**

| Length | GPT-4 | GPT-3.5-turbo | Claude-3-opus | Llama-3-8b-instruct | Mistral-7b-instruct | RWKV-v5-7b | Mamba-2.8b |
|--------|-------|---------------|---------------|---------------------|---------------------|------------|------------|
| 0k | 93 | 91 | 82 | 85 | 67 | 95 | 93 |
| 1k | 82 | 64 | 83 | 62 | 54 | 100 | 100 |
| 2k | 68 | 53 | 62 | 53 | 50 | 100 | 100 |
| 4k | 58 | 50 | 55 | 52 | 50 | 100 | 100 |
| 8k | 56 | 37 | 56 | 51 | 49 | 100 | 100 |
| 128k | [unclear: value not clearly visible] | [unclear: value not clearly visible] | [unclear: value not clearly visible] | [unclear: value not clearly visible] | [unclear: value not clearly visible] | 98 | 100 |

**QA2 (Two Supporting Facts) - Sample of models:**

| Length | GPT-4 | Llama-3-8b-instruct | RWKV-v5-7b | Mamba-2.8b |
|--------|-------|---------------------|------------|------------|
| 0k | 58 | 44 | 43 | 88 |
| 1k | 47 | 26 | 27 | 73 |
| 2k | 37 | 26 | 28 | 65 |
| 4k | 27 | 20 | 25 | 62 |

**QA3 (Three Supporting Facts) - Sample of models:**

| Length | GPT-4 | RWKV-v5-7b | Mamba-2.8b |
|--------|-------|------------|------------|
| 0k | 44 | 28 | 56 |
| 1k | 28 | 28 | 49 |
| 2k | 26 | 23 | 43 |

**QA4 (Two Arg Relations) - Sample of models:**

| Length | GPT-4 | Phi-3-medium-128k | Yi-34b |
|--------|-------|-------------------|--------|
| 0k | 72 | 65 | 62 |
| 1k | 67 | 63 | 61 |
| 2k | 67 | 63 | 60 |

**QA5 (Three Arg Relations) - Sample of models:**

| Length | GPT-4 | Command-R-Plus |
|--------|-------|----------------|
| 0k | 53 | 44 |
| 1k | 42 | 38 |
| 2k | 39 | 35 |

[Note: Table 4 in the PDF is extremely dense with color-coded cells showing all 38 models across all 5 tasks and 13-14 length configurations each. The complete table contains several hundred individual accuracy values. The samples above capture representative performance patterns. The full table shows that performance generally degrades with increasing context length, with notable exceptions like RWKV and Mamba maintaining high accuracy on QA1 even at extreme lengths.]
