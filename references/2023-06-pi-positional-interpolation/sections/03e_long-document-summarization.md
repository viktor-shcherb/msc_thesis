# 3.5 Long Document Summarization [p. 9–10]

[p. 9] The authors evaluate their models' performance on the long document summarization task. They consider the GovReport (Huang et al., 2021) dataset, which contains 17457 documents for training and 972 documents for evaluation. Each document comes with a human generated summary. All input documents are truncated to their first 15000 tokens.

## Setup

[p. 9–10] The LLaMA models are extended with Position Interpolation with a context window of 16384. The rescaling of position indices is still required during this fine-tuning step. They first format the raw document using the prompt template in Figure 4, and then concatenate the prompt with the ground-truth summary (truncated to 1000 tokens) associated with each document. The model is fine-tuned using the next token prediction task with the above setup for 10 epochs. The losses from the input prompt proportion of training examples are excluded during fine-tuning.

**Inference parameters:**
- Generation temperature: 0.5
- $\text{top}_p = 0.95$
- Final output truncated at 1000 tokens

**Evaluation metric:** ROUGE-1/ROUGE-2/ROUGE-L scores (Lin, 2004) comparing the models' outputs vs the ground-truth summaries. [p. 10]

## Table 6: ROUGE Score on GovReport Dataset [p. 10]

Includes results from two baselines in existing SCROLLS Leaderboard (Shaham et al., 2022; Ainslie et al., 2023).

| Model | Context Window | ROUGE-1 | ROUGE-2 | ROUGE-L |
|-------|---------------|---------|---------|---------|
| CoLT5 Base (Ainslie et al., 2023) | 16K | 58.7 | 29.6 | 31.4 |
| CoLT5 XL (Ainslie et al., 2023) | 16K | 61.3 | 32.2 | 33.8 |
| LLaMA-7B Extended | 16K | 60.0 | 28.0 | 29.5 |

[p. 10] The extended LLaMA-7B model has obtained competitive R1 score among other models with minimal tuning of hyper-parameters. This result suggests their models with 16384 context window can effectively handle the long document summarization task.

## Figure 4: Input format for long document summarization [p. 10]

**Figure 4** (p. 10): "Input format for long doc summarization."

The prompt format is:
```
Read the following article and then summarize it.
# .... Document goes here
Now summarize the above article.
Summary:
```
