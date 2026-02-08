# 4 Instruction Finetuning [p. 7-8]

[p. 7] Briefly finetuning on instructions data rapidly leads to improvements on MMLU. Although the non-finetuned version of LLaMA-65B is already able to follow basic instructions, a very small amount of finetuning improves the performance on MMLU, and further improves the ability of the model to follow instructions. Since this is not the focus of this paper, only a single experiment was conducted following the same protocol as Chung et al. (2022) to train an instruct model, LLaMA-I.

**Table 10** (p. 7): **Instruction finetuning -- MMLU (5-shot).** Comparison of models of moderate size with and without instruction finetuning on MMLU.

| | Params | MMLU |
|---|---|---|
| OPT | 30B | 26.1 |
| GLM | 120B | 44.8 |
| PaLM | 62B | 55.1 |
| PaLM-cont | 62B | 62.8 |
| Chinchilla | 70B | 67.5 |
| LLaMA | 65B | 63.4 |
| | | |
| OPT-IML-Max | 30B | 43.2 |
| Flan-T5-XXL | 11B | 55.1 |
| Flan-PaLM | 62B | 59.6 |
| Flan-PaLM-cont | 62B | 66.1 |
| LLaMA-I | 65B | **68.9** |

[p. 7-8] In Table 10, the results of the instruct model LLaMA-I on MMLU are reported and compared with existing instruction finetuned models of moderate sizes, namely OPT-IML (Iyer et al., 2022) and the Flan-PaLM series (Chung et al., 2022). All the reported numbers are from the corresponding papers. Despite the simplicity of the instruction finetuning approach used here, 68.9% on MMLU is reached. LLaMA-I (65B) outperforms on MMLU existing instruction finetuned models of moderate sizes, but are still far from the state-of-the-art, that is 77.4 for GPT `code-davinci-002` on MMLU (numbers taken from Iyer et al. (2022)). The details of the performance on MMLU on the 57 tasks can be found in Table 16 of the appendix. [p. 8]
