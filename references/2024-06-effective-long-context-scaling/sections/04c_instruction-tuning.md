# Instruction Tuning [p. 10]

## Setup [p. 10]

[p. 10] Various strategies are explored to instruction-finetune the pre-trained long context model which do not require any supervised long data. Starting with finetuning the models with short instruction data from LLAMA 2 CHAT (referred as "RLHF V5" in (Touvron et al., 2023)) and then blending in some pretrain data to avoid forgetting of previous long context continual pretraining.

## Key Findings [p. 10]

[p. 10] As demonstrated in Table 9:
- Using only short instruction data can already produce a decent long model that significantly outperforms LLAMA 2 on various long-context tasks
- Adding pretrain data (calculating language modeling loss on the whole sequence) can further boost the performance on most datasets
- Inspired by this, adding the LM loss over the long context inputs when finetuning with self-instruct data makes learning more stable when there are unbalanced input and output lengths (footnote 5), giving significant improvements on most of the tested tasks (the last two rows of Table 9)

Footnote 5 [p. 10]: In our cases, the output lengths of most samples are a lot shorter than the those of the long-context inputs.

## Results [p. 10]

**Table 9** (p. 10): Comparison of different instruction finetuning data mixes.

| Settings | Qasper | NarrativeQA | QuALITY | SummScreenFD | QMSum |
|---|---|---|---|---|---|
| LLAMA 2 CHAT baseline | 12.2 | 9.13 | 56.7 | 10.5 | 14.4 |
| LLAMA 2 LONG finetuned with: | | | | | |
| "RLHF V5" | 22.3 | 13.2 | 71.4 | 14.8 | 16.9 |
| "RLHF V5" mix pretrain | 23.7 | 16.6 | 76.2 | **15.7** | 17.8 |
| "RLHF V5" mix self-inst w/o LM loss | 35.7 | 22.3 | 59.3 | 12.2 | 13.4 |
| "RLHF V5" mix self-inst with LM loss | **38.9** | **23.3** | **77.3** | 14.5 | **18.5** |
