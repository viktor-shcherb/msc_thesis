# 3.6 Reading Comprehension [p. 18]

[p. 18] GPT-3 is evaluated on the task of reading comprehension using a suite of 5 datasets including abstractive, multiple choice, and span based answer formats in both dialog and single question settings. A wide spread in GPT-3's performance across these datasets is observed, suggestive of varying capability with different answer formats. In general GPT-3 is on par with initial baselines and early results trained using contextual representations on each respective dataset.

## CoQA

[p. 18] GPT-3 performs best (within 3 points of the human baseline) on CoQA [RCM19], a free-form conversational dataset.

## QuAC

[p. 18] GPT-3 performs worst (13 F1 below an ELMo baseline) on QuAC [CHI+18], a dataset which requires modeling structured dialog acts and answer span selections of teacher-student interactions.

## DROP

[p. 18] On DROP [DWD+19], a dataset testing discrete reasoning and numeracy in the context of reading comprehension, GPT-3 in a few-shot setting outperforms the fine-tuned BERT baseline from the original paper but is still well below both human performance and state-of-the-art approaches which augment neural networks with symbolic systems [RLL+19].

## SQuAD 2.0

[p. 18] On SQuAD 2.0 [RJL18], GPT-3 demonstrates its few-shot learning capabilities, improving by almost 10 F1 (to 69.8) compared to a zero-shot setting. This allows it to slightly outperform the best fine-tuned result in the original paper.

## RACE

[p. 18] On RACE [LXL+17], a multiple choice dataset of middle school and high school english examinations, GPT-3 performs relatively weakly and is only competitive with the earliest work utilizing contextual representations and is still 45% behind SOTA.

### Table 3.7: Results on reading comprehension tasks. All scores are F1 except results for RACE which report accuracy. [p. 18]

| Setting | CoQA | DROP | QuAC | SQuADv2 | RACE-h | RACE-m |
|---|---|---|---|---|---|---|
| Fine-tuned SOTA | **90.7**^a | **89.1**^b | **74.4**^c | **93.0**^d | **90.0**^e | **93.1**^e |
| GPT-3 Zero-Shot | 81.5 | 23.6 | 41.5 | 59.5 | 45.5 | 58.4 |
| GPT-3 One-Shot | 84.0 | 34.3 | 43.3 | 65.4 | 45.9 | 57.4 |
| GPT-3 Few-Shot | 85.0 | 36.5 | 44.3 | 69.8 | 46.8 | 58.1 |

^a [JZC+19] ^b [JN20] ^c [AI19] ^d [QIA20] ^e [SPP+19]

## Figures

**Figure 3.7** (p. 19): "GPT-3 results on CoQA reading comprehension task. GPT-3 175B achieves 85 F1 in the few-shot setting, only a few points behind measured human performance and state-of-the-art fine-tuned models. Zero-shot and one-shot performance is a few points behind, with the gains to few-shot being largest for bigger models."
- X-axis: Parameters in LM (Billions), from 0.1B to 175B. Y-axis: Accuracy (F1), from ~30 to ~90.
- Three lines: Zero-Shot (blue), One-Shot (green), Few-Shot K=5 (orange).
- Horizontal dashed lines: "Fine-tuned SOTA" at ~90.7, "Human" at ~90.
- All three lines rise from ~35-40 at 0.1B. At 175B: Zero-Shot ~81.5, One-Shot ~84.0, Few-Shot ~85.0.
- The gap between few-shot and zero-shot widens at larger model sizes.
- Few-shot GPT-3 175B is only a few points behind both human performance and fine-tuned SOTA.
