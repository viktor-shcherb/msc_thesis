# 5. Scaling up to DeepSeekMoE 16B [p. 15–16]

[p. 15] With the DeepSeekMoE architecture, the MoE model is scaled up to a larger scale with 16B total parameters and trained on 2T tokens. The results demonstrate that compared with LLaMA2 7B, DeepSeekMoE 16B achieves superior performance with only about 40% of computations.

## 5.1. Experimental Setup

### 5.1.1. Training Data and Tokenization

[p. 15] The training data is sampled from the same corpus as described in Section 4.1.1. Different from the validation experiments, a larger amount of data with 2T tokens is sampled, aligning with the number of training tokens of LLaMA2 7B. The HuggingFace Tokenizer tools are also used to train a BPE tokenizer, but the vocabulary size is set to 100K for DeepSeekMoE 16B.

### 5.1.2. Hyper-Parameters

**Model Settings.** [p. 15] For DeepSeekMoE 16B:
- Number of Transformer layers: 28
- Hidden dimension: 2048
- Multi-head attention: 16 heads, each head dimension 128
- Initialization: all learnable parameters randomly initialized with a standard deviation of 0.006
- All FFNs substituted with MoE layers except for the first layer, since the load balance status converges especially slower for the first layer
- Each MoE layer consists of 2 shared experts and 64 routed experts, where each expert is 0.25 times the size of a standard FFN
- Each token is routed to these 2 shared experts and 6 out of 64 routed experts
- An even finer expert segmentation granularity is not employed due to the potential reduction in computational efficiency associated with excessively small expert sizes; at a larger scale over 16B, a finer granularity can still be employed
- Under this configuration, DeepSeekMoE 16B has approximately 16.4B total parameters, with the number of activated parameters around 2.8B

**Training Settings.** [p. 15]
- Optimizer: AdamW (Loshchilov and Hutter, 2019)
- Hyper-parameters: $\beta_1 = 0.9$, $\beta_2 = 0.95$, weight_decay $= 0.1$
- Learning rate schedule: warmup-and-step-decay strategy
  - Linear increase from 0 to maximum value during first 2K steps
  - Multiplied by 0.316 at 80% of training steps
  - Multiplied by 0.316 again at 90% of training steps
- Maximum learning rate for DeepSeekMoE 16B: $4.2 \times 10^{-4}$
- Gradient clipping norm: 1.0
- Batch size: 4.5K
- Maximum sequence length: 4K
- Each training batch contains 18M tokens
- Total number of training steps: 106,449 (to achieve 2T training tokens)
- No dropout used during training
- Pipeline parallelism leveraged to deploy different layers on different devices; for each layer, all experts deployed on the same device
- No tokens dropped during training; device-level balance loss not employed
- Expert-level balance factor set to $\alpha_1 = 0.001$ (smaller than validation experiments)
  - Under their parallelization strategy, a higher expert-level balance factor cannot increase computation efficiency but instead will compromise model performance

### 5.1.3. Evaluation Benchmarks

[p. 16] In addition to the benchmarks used in the validation experiments, additional benchmarks are incorporated for a more comprehensive evaluation. The distinctions from the benchmarks used in validation experiments are as follows:

**Language Modeling.** Models also evaluated on the test set of Pile (Gao et al., 2020). Since the tokenizer used in DeepSeekMoE 16B is different from that used in LLaMA2 7B, bits per byte (BPB) is used as the evaluation metric for a fair comparison.

**Reading Comprehension.** DROP (Dua et al., 2019) is additionally considered. Evaluation metric: Exactly Matching (EM) rate.

**Math Reasoning.** GSM8K (Cobbe et al., 2021) and MATH (Hendrycks et al., 2021) are additionally incorporated, using EM as the evaluation metric.

**Multi-Subject Multiple-Choice.** MMLU (Hendrycks et al., 2020) is additionally evaluated. Evaluation metric: accuracy.

**Disambiguation.** WinoGrande (Sakaguchi et al., 2019) is additionally considered. Evaluation metric: accuracy.

**Chinese Benchmarks.** Since DeepSeekMoE 16B is pretrained on a bilingual corpus, four Chinese benchmarks are evaluated:
- CLUEWSC (Xu et al., 2020): a Chinese disambiguation benchmark
- CEval (Huang et al., 2023): a Chinese multi-subject multiple-choice benchmark
- CMMLU (Li et al., 2023): a Chinese multi-subject multiple-choice benchmark with a similar form to MMLU
- CHID (Zheng et al., 2019): a Chinese idiom completion benchmark, aiming to evaluate the understanding of Chinese culture
- Evaluation metrics for Chinese benchmarks: accuracy or EM

**Open LLM Leaderboard.** [p. 16] DeepSeekMoE 16B is additionally evaluated on the Open LLM Leaderboard, a public leaderboard supported by HuggingFace. It consists of six tasks: ARC (Clark et al., 2018), HellaSwag (Zellers et al., 2019), MMLU (Hendrycks et al., 2020), TruthfulQA (Lin et al., 2022), Winogrande (Sakaguchi et al., 2019), and GSM8K (Cobbe et al., 2021). All benchmarks are evaluated using their internal evaluation framework. The Open LLM Leaderboard comparison enables fair and convenient comparison with open source models.

## 5.2. Evaluations

### 5.2.1. Internal Comparison with DeepSeek 7B

[p. 16] An internal comparison between DeepSeekMoE 16B and DeepSeek 7B (DeepSeek-AI, 2024), a dense language model with 6.9B parameters, is first conducted. Ensuring fairness, both models are trained on the same corpus with 2T tokens. This enables an accurate assessment of the effectiveness of the MoE architecture, independent of the influence of the training data.

---
[p. 17 continued]

**Table 3** (p. 17): Comparison between DeepSeek 7B and DeepSeekMoE 16B. **Bold** font indicates the best or near the best. With only 40.5% of computations, DeepSeekMoE 16B achieves comparable performance with DeepSeek 7B.

| Metric | # Shot | DeepSeek 7B (Dense) | DeepSeekMoE 16B |
|---|---|---|---|
| # Total Params | N/A | 6.9B | 16.4B |
| # Activated Params | N/A | 6.9B | 2.8B |
| FLOPs per 4K Tokens | N/A | 183.5T | 74.4T |
| # Training Tokens | N/A | 2T | 2T |
| Pile (BPB) | N/A | 0.75 | **0.74** |
| HellaSwag (Acc.) | 0-shot | 75.4 | **77.1** |
| PIQA (Acc.) | 0-shot | 79.2 | **80.2** |
| ARC-easy (Acc.) | 0-shot | **67.9** | 68.1 |
| ARC-challenge (Acc.) | 0-shot | 48.1 | **49.8** |
| RACE-middle (Acc.) | 5-shot | **63.2** | 61.9 |
| RACE-high (Acc.) | 5-shot | **46.5** | 46.4 |
| DROP (EM) | 1-shot | **34.9** | 32.9 |
| GSM8K (EM) | 8-shot | 17.4 | **18.8** |
| MATH (EM) | 4-shot | 3.3 | **4.3** |
| HumanEval (Pass@1) | 0-shot | 26.2 | **26.8** |
| MBPP (Pass@1) | 3-shot | **39.0** | 39.2 |
| TriviaQA (EM) | 5-shot | 59.7 | **64.8** |
| NaturalQuestions (EM) | 5-shot | 22.2 | **25.5** |
| MMLU (Acc.) | 5-shot | **48.2** | 45.0 |
| WinoGrande (Acc.) | 0-shot | **70.5** | 70.2 |
| CLUEWSC (EM) | 5-shot | **73.1** | 72.1 |
| CEval (Acc.) | 5-shot | **45.0** | 40.6 |
| CMMLU (Acc.) | 5-shot | **47.2** | 42.5 |
| CHID (Acc.) | 0-shot | 89.3 | **89.4** |

[p. 17] Key observations from Table 3:

1. On the whole, with about only 40% of the computations, DeepSeekMoE 16B achieves comparable performance with DeepSeek 7B.
2. DeepSeekMoE 16B exhibits notable strengths in language modeling and knowledge-intensive tasks such as Pile, HellaSwag, TriviaQA, and NaturalQuestions. Given that in an MoE model, FFN parameters are much heavier than attention parameters, these outcomes align with the proposition that FFNs in Transformers exhibit the capability for knowledge memorization (Dai et al., 2022a).
3. Compared with the excellent performance on other tasks, DeepSeekMoE exhibits limitations in addressing multiple-choice tasks. This inadequacy stems from the limited attention parameters in DeepSeekMoE 16B (DeepSeekMoE 16B has only about 0.5B attention parameters, while DeepSeek 7B has 2.5B attention parameters). The authors' earlier investigation on DeepSeek 7B reveals a positive correlation between the attention capacity and performance on multiple-choice tasks. For example, DeepSeek 7B MQA, which is equipped with the multi-query attention mechanism (Shazeer, 2019), also struggled in MMLU-like tasks.

[p. 17–18] In addition, for a more comprehensive understanding of the training process of DeepSeekMoE 16B, the authors also provide the benchmark curves of DeepSeekMoE 16B and DeepSeek 7B (Dense) during training in Appendix C for reference.

[p. 18] Critically, due to the modest number of parameters in DeepSeekMoE 16B, it enables single-device deployment on a GPU with 40GB of memory. With appropriate operator optimizations, it can achieve nearly 2.5 times the inference speed of a 7B dense model.

### 5.2.2. Comparison with Open Source Models

**Internal Comparison with LLaMA2 7B.** [p. 18] DeepSeekMoE 16B is mainly compared with LLaMA2 7B (Touvron et al., 2023b), a well-known and strong open source language model with 6.7B parameters. Both DeepSeekMoE 16B and LLaMA2 7B are pretrained on 2T tokens. Compared with LLaMA2 7B, DeepSeekMoE has 245% of total parameters but only needs 39.6% of computations.

**Table 4** (p. 18): Comparison between LLaMA2 7B and DeepSeekMoE 16B. With only 39.6% of computations, DeepSeekMoE 16B outperforms LLaMA2 7B on the majority of benchmarks.

| Metric | # Shot | LLaMA2 7B | DeepSeekMoE 16B |
|---|---|---|---|
| # Total Params | N/A | 6.7B | 16.4B |
| # Activated Params | N/A | 6.7B | 2.8B |
| FLOPs per 4K Tokens | N/A | 187.9T | 74.4T |
| # Training Tokens | N/A | 2T | 2T |
| Pile (BPB) | N/A | 0.76 | **0.74** |
| HellaSwag (Acc.) | 0-shot | 75.6 | **77.1** |
| PIQA (Acc.) | 0-shot | 78.0 | **80.2** |
| ARC-easy (Acc.) | 0-shot | **69.1** | 68.1 |
| ARC-challenge (Acc.) | 0-shot | 49.0 | **49.8** |
| RACE-middle (Acc.) | 5-shot | 60.7 | **61.9** |
| RACE-high (Acc.) | 5-shot | 45.8 | **46.4** |
| DROP (EM) | 1-shot | **34.0** | 32.9 |
| GSM8K (EM) | 8-shot | 15.5 | **18.8** |
| MATH (EM) | 4-shot | 2.6 | **4.3** |
| HumanEval (Pass@1) | 0-shot | 14.6 | **26.8** |
| MBPP (Pass@1) | 3-shot | 21.8 | **39.2** |
| TriviaQA (EM) | 5-shot | 63.8 | **64.8** |
| NaturalQuestions (EM) | 5-shot | **25.5** | 25.5 |
| MMLU (Acc.) | 5-shot | **45.8** | 45.0 |
| WinoGrande (Acc.) | 0-shot | 69.6 | **70.2** |
| CLUEWSC (EM) | 5-shot | 64.0 | **72.1** |
| CEval (Acc.) | 5-shot | 33.9 | **40.6** |
| CMMLU (Acc.) | 5-shot | 32.6 | **42.5** |
| CHID (Acc.) | 0-shot | 37.9 | **89.4** |

[p. 18–19] Key observations from Table 4:

1. Among the evaluated benchmarks, with only about 40% of computations, DeepSeekMoE 16B outperforms LLaMA2 7B on the majority of benchmarks.
2. The math reasoning and code generation capabilities of DeepSeekMoE 16B are stronger than LLaMA2 7B, attributed to the enriched presence of mathematical and code-related text in the pretraining corpus.
3. Given the presence of Chinese texts in the pretraining corpus, DeepSeekMoE 16B exhibits a substantial performance advantage over LLaMA2 7B on Chinese benchmarks.
4. Despite being trained on fewer English texts, DeepSeekMoE 16B achieves comparable or better performance compared with LLaMA2 7B on English understanding or knowledge-intensive benchmarks, which demonstrates the exceptional capabilities of DeepSeekMoE 16B.

**Evaluation on Open LLM Leaderboard.** [p. 19] Beyond internal evaluations, DeepSeekMoE 16B is also evaluated on the Open LLM Leaderboard to compare with other open source models. In addition to LLaMA2 7B, a broader set of open source models is considered, including LLaMA 7B (Touvron et al., 2023a), Falcon 7B (Almazrouei et al., 2023), GPT-J 6B (Wang and Komatsuzaki, 2021), RedPajama-INCITE 7B and 3B (Together-AI, 2023), Open LLaMA 7B and 3B (Geng and Liu, 2023), OPT 2.7B (Zhang et al., 2022), Pythia 2.8B (Biderman et al., 2023), GPT-neo 2.7B (Black et al., 2021), and BLOOM 3B (Scao et al., 2022). The evaluation results, as presented in Figure 1, show that DeepSeekMoE 16B consistently outperforms models with similar activated parameters by a large margin. Moreover, it achieves comparable performance with LLaMA2 7B, which has approximately 2.5 times the activated parameters.
