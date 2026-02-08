# 6. Alignment for DeepSeekMoE 16B [p. 19–21]

[p. 19] Previous research indicates that MoE models typically do not emerge significant gains from fine-tuning (Artetxe et al., 2022; Fedus et al., 2021). However, Shen et al. (2023) present findings suggesting that MoE models can indeed benefit from instruction tuning. In order to assess whether DeepSeekMoE 16B can benefit from fine-tuning, the authors conduct supervised fine-tuning to construct a chat model based on DeepSeekMoE 16B. The experimental results reveal that DeepSeekMoE Chat 16B also achieves comparable performance with LLaMA2 SFT 7B and DeepSeek Chat 7B.

## 6.1. Experimental Setup

### Training Data

[p. 19] For training the chat model, supervised fine-tuning (SFT) is conducted on in-house curated data, comprising 1.4M training examples. This dataset spans a broad range of categories including math, code, writing, question answering, reasoning, summarization, and more. The majority of the SFT training data is in English and Chinese, rendering the chat model versatile and applicable in bilingual scenarios.

### Hyper-Parameters

[p. 19] During supervised fine-tuning:
- Batch size: 1024 examples
- Epochs: 8
- Optimizer: AdamW (Loshchilov and Hutter, 2019)
- Maximum sequence length: 4K
- Training examples packed as densely as possible until reaching the sequence length limit
- No dropout used for supervised fine-tuning
- Constant learning rate of $10^{-5}$ without incorporating any learning rate scheduling strategy

### Evaluation Benchmarks

[p. 19–20] For evaluation of the chat models, benchmarks similar to those in Section 5.1.3 are used, with the following adjustments:
1. Pile (Gao et al., 2020) is excluded since chat models are seldom employed for pure language modeling.
2. CHID (Zheng et al., 2019) is excluded due to the observed instability of results, hindering the derivation of solid conclusions.
3. BBH (Suzgun et al., 2022) is additionally included to provide a more comprehensive assessment of the reasoning ability of the chat models.

## 6.2. Evaluations

### Baselines

[p. 20] To validate the potential of DeepSeekMoE 16B after alignment, supervised fine-tuning is conducted for LLaMA2 7B, DeepSeek 7B, and DeepSeekMoE 16B, where the same fine-tuning data is used to ensure fairness. Correspondingly, three chat models are constructed: LLaMA2 SFT 7B^3, DeepSeek Chat 7B, and DeepSeekMoE Chat 16B. DeepSeekMoE Chat 16B is compared with the other two dense chat models (with about 2.5 times the FLOPs) across a wide range of downstream tasks.

> ^3 "We use LLaMA2 SFT to distinguish from the official LLaMA2 Chat (Touvron et al., 2023b) model." [p. 20]

### Results

**Table 5** (p. 20): Comparison among LLaMA2 SFT 7B, DeepSeek Chat 7B and DeepSeekMoE Chat 16B, with all three models fine-tuned on the same SFT data. Compared with both 7B dense models, DeepSeekMoE Chat 16B still achieves comparable or better performance on the majority of benchmarks with only 40% of computations.

| Metric | # Shot | LLaMA2 SFT 7B | DeepSeek Chat 7B | DeepSeekMoE Chat 16B |
|---|---|---|---|---|
| # Total Params | N/A | 6.7B | 6.9B | 16.4B |
| # Activated Params | N/A | 6.7B | 6.9B | 2.8B |
| FLOPs per 4K Tokens | N/A | 187.9T | 183.5T | 74.4T |
| HellaSwag (Acc.) | 0-shot | 67.9 | 71.0 | **72.2** |
| PIQA (Acc.) | 0-shot | 76.9 | 78.4 | **79.7** |
| ARC-easy (Acc.) | 0-shot | 69.7 | **70.2** | 69.9 |
| ARC-challenge (Acc.) | 0-shot | **50.8** | 50.2 | 50.0 |
| BBH (EM) | 3-shot | 39.3 | **43.1** | 42.2 |
| RACE-middle (Acc.) | 5-shot | 63.9 | **66.1** | 64.8 |
| RACE-high (Acc.) | 5-shot | 49.6 | **50.8** | 50.6 |
| DROP (EM) | 1-shot | 40.0 | **41.7** | 33.8 |
| GSM8K (EM) | 0-shot | **63.4** | 62.6 | 62.2 |
| MATH (EM) | 4-shot | 13.5 | 14.7 | **15.2** |
| HumanEval (Pass@1) | 0-shot | 35.4 | 45.1 | **45.7** |
| MBPP (Pass@1) | 3-shot | 27.8 | 39.0 | **46.2** |
| TriviaQA (EM) | 5-shot | 60.1 | 59.5 | **63.3** |
| NaturalQuestions (EM) | 0-shot | **35.2** | 32.7 | 35.1 |
| MMLU (Acc.) | 0-shot | **50.0** | 49.7 | 47.2 |
| WinoGrande (Acc.) | 0-shot | 65.1 | 68.4 | **69.0** |
| CLUEWSC (EM) | 5-shot | 48.4 | 66.2 | **68.2** |
| CEval (Acc.) | 0-shot | 35.1 | **44.7** | 40.0 |
| CMMLU (Acc.) | 0-shot | 36.9 | **51.2** | 49.3 |

[p. 21] Key observations from Table 5:

1. DeepSeekMoE Chat 16B, while consuming nearly 40% of computations, achieves comparable performance with 7B dense models across language understanding and reasoning (PIQA, ARC, BBH), machine reading comprehension (RACE), mathematical (GSM8K, MATH), and knowledge-intensive tasks (TriviaQA, NaturalQuestions).
2. On code generation tasks, DeepSeekMoE Chat 16B significantly outperforms LLaMA2 SFT 7B, demonstrating notable improvements on HumanEval and MBPP. In addition, it also surpasses DeepSeek Chat 7B.
3. On multiple-choice question answering benchmarks including MMLU, CEval, and CMMLU, DeepSeekMoE Chat 16B still falls behind DeepSeek Chat 7B, consistent with the observations for the base model (Section 5.2.1). However, it is worth noting that, after supervised fine-tuning, the performance gap between DeepSeekMoE 16B and DeepSeek 7B is narrowed.
4. Benefiting from the pretraining on a bilingual corpus, DeepSeekMoE Chat 16B notably outperforms LLaMA2 SFT 7B on all Chinese benchmarks. These results demonstrate the balanced capabilities of DeepSeekMoE 16B in both Chinese and English, enhancing its versatility and applicability in diverse scenarios.

In conclusion, the evaluation for the chat models highlights the potential of DeepSeekMoE 16B in benefiting from alignment, and validates its consistent advantages in achieving comparable performance with dense models while using only about 40% of computations.