# Pretraining Data Mix [p. 8–9]

## Setup [p. 8–9]

[p. 8–9] The data used to continually pretrain the model combines existing datasets used by LLAMA 2 and new long text data. The data source mix ratio is adjusted to up-weight long data samples. Early experiments with 7B models confirm significant improvements using this data mix for long-context tasks, as shown in the first two rows of Table 7.

## Ablation Design [p. 9]

[p. 9] Two additional ablations are performed using LLAMA 2's pretrain datasets to rigorously investigate the source of improvements and differentiate the effects of the data length distribution and the quality of the corpus itself:
1. Remove the long text data from the LLAMA 2 dataset and continually pretrain the model with mostly short documents
2. Increase the sample weights of existing long text data to be similar to the long text ratio used by the proposed new model

## Results on Long-Context Tasks [p. 9]

**Table 7** (p. 9): Comparison of different pretraining data mix on long-context tasks. Instead of showing the absolute performance, relative improvements over the 7B LLAMA 2 which has a 4,096-token context window are reported. All models are evaluated with prompts truncated at 16,384 tokens.

| Continual Pretrain Data | NarrativeQA Delta F1 | Qasper Delta F1 | Quality Delta EM | QMSum Delta ROUGE-geo |
|---|---|---|---|---|
| LLAMA 2 LONG data mix | **23.70%** | **43.64%** | **75.5%** | **45.70%** |
| LLAMA 2 data mix | 18.23% | 38.12% | 60.3% | 44.87% |
| - remove long text data | 19.48% | 39.14% | 67.1% | 36.60% |
| - upsample existing long text data | 22.15% | 36.82% | 65.0% | 42.83% |

## Key Findings [p. 9]

[p. 9] Interestingly, even with most of the long texts removed, the model can still obtain most of the performance gain over LLAMA 2. There is no clear and consistent advantage as the long data ratio is greatly increased (the third row vs. the fourth row in Table 7 and Table 8). Similar results observed on the FIRST-SENTENCE-RETRIEVAL task as shown by Figure 7 in the Appendix.

[p. 9] Based on the above ablations, adjusting the length distribution of the pretrain data does not provide major benefits. However, as the authors evaluate these model variants' performance on standard short-context tasks, they find that the new data mix also leads to large improvements in many cases, especially knowledge-intensive tasks like MMLU, as shown in Table 8. These results suggest that:

> *long-context LLMs can be effectively trained even with very limited long data* [p. 9]

and the improvements of the pretrain data over the one used by LLAMA 2 mostly come from the quality of the data itself, instead of the length distribution difference.

## Results on Short-Context Tasks [p. 9]

**Table 8** (p. 9): Standard short task performance of long-context models with different pretrain data mix.

| Continual Pretrain Data | HumanEval | Math | MMLU | HellaSwag | TQA |
|---|---|---|---|---|---|
| LLAMA 2 LONG data mix | **17.08** | **4.09** | **48.62** | 76.74 | 66.24 |
| LLAMA 2 data mix | 15.24 | 3.61 | 46.30 | 76.63 | **66.71** |
| - remove long text data | 17.07 | 3.57 | 46.25 | **76.76** | 65.90 |
| - upsample existing long text data | 17.07 | 3.53 | 46.25 | 76.74 | 66.04 |
