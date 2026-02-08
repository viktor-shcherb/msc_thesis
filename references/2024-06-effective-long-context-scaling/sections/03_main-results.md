# Main Results [p. 4-6]

## Pretrained Model Evaluation [p. 4-5]

### Short Tasks [p. 4]

[p. 4] To make long-context LLMs universally useful, an important desideratum is to ensure robust performance on standard short-context tasks. Performance is verified on a series of common benchmarks following Touvron et al. (2023). Results are shown in Table 1. Overall, the authors observe results that are *on-par and, in most cases, stronger results* than LLAMA 2. Notably, significantly improved results on coding, math, and knowledge intensive tasks such as MMLU. As shown in Table 2, the model outperforms GPT-3.5 on MMLU and GSM8k. This is in contrast to a previous work (Chen et al., 2023) which observes degradation on short tasks. The improvements are attributed to additional computation FLOPs and the knowledge learned from newly introduced long data.

**Table 1** (p. 4): Performance on standard short-context benchmarks. Coding score is the average of pass@1 of HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021); Math score is the average of top-1 accuracy of 8-shot GSM8K (Cobbe et al., 2021) and 4-shot MATH (Hendrycks et al., 2021); OpenQA score is the average of 5-shot performance on NaturalQuestions (Kwiatkowski et al., 2019) and TriviaQA (Joshi et al., 2017); Commonsense score is the average of PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), ARC easy and challenge (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018) and CommonsenseQA (Talmor et al., 2018).

| Model | Size | Coding | Math | MMLU | Commonsense | OpenQA |
|---|---|---|---|---|---|---|
| LLAMA 2 | 7B | 16.8 | 8.55 | 45.3 | 63.9 | 48.9 |
| LLAMA 2 | 13B | 24.5 | 16.3 | 54.8 | 66.9 | 55.4 |
| LLAMA 2 | 34B | 27.8 | 24.2 | 62.6 | 69.9 | 58.7 |
| LLAMA 2 | 70B | 37.4 | 35.2 | 68.9 | 71.9 | 63.6 |
| LLAMA 2 LONG | 7B | 20.6 | 10.5 | 47.8 | 64.9 | 51.0 |
| LLAMA 2 LONG | 13B | 25.7 | 21.5 | 60.1 | 67.8 | 56.8 |
| LLAMA 2 LONG | 34B | 29.9 | 29.0 | 65.0 | 70.9 | 60.3 |
| LLAMA 2 LONG | 70B | **39.9** | **41.3** | **71.7** | **72.7** | **64.0** |

**Table 2** (p. 4): Comparison with closed models on standard short tasks.

| Task | GPT-3.5 | GPT-4 | PaLM | PaLM-2-L | LLAMA 2 | LLAMA 2 LONG |
|---|---|---|---|---|---|---|
| MMLU (5-shot) | 70.0 | **86.4** | 69.3 | 78.3 | 68.9 | 71.7 |
| Natural Questions (1-shot) | - | - | 29.3 | **37.5** | 33.0 | 35.7 |
| GSM8K (8-shot) | 57.1 | **92.0** | 56.5 | 80.7 | 56.8 | 65.4 |
| HumanEval (0-shot) | 48.1 | **67.0** | 26.2 | - | 29.9 | 32.9 |

### Long Tasks [p. 4-5]

[p. 4] Different from previous works (Chen et al., 2023; Mohtashami and Jaggi, 2023) that mostly rely on perplexity and synthetic tasks to gauge long-context performance, the authors perform long-context evaluation using real-world language tasks:

- **NarrativeQA** (Kocisky et al., 2018): 0-shot
- **QuALITY** (Pang et al., 2022): 2-shot
- **Qasper** (Dasigi et al., 2021): 2-shot
- **QMSum** (Zhong et al., 2021): 1-shot

Number of shots decided based on average sample length (samples in Qasper and QuALITY are often much shorter than NarrativeQA). QA-style tasks chosen for ease of prompt engineering and less biased automatic evaluations. Input prompts truncated from left side if they exceed the maximum input length of the model or 16,384 tokens.

[p. 4] Comparison with open-source long-context models available in Huggingface Transformers: Focused Transformer (Tworkowski et al., 2023a), YaRN (Peng et al., 2023), Xgen (Nijkamp et al., 2023), MPT (MosaicML, 2023b,a) and Together's LLAMA 2 fork (Together, 2023).

Footnote 2 [p. 4]: Simple prompt format used: "{CONTEXT} Q: {QUESTION}, A:" to evaluate all pretrained models.

**Table 3** (p. 5): Comparison with open-source long-context models on research benchmarks. ^{+}: "together-7B-32k" is not a purely self-supervised model and has been finetuned using supervised datasets which can improve its few-shot results. *: ROUGE-geo is the geometric mean of ROUGE-1, 2 and L. All numbers are validation results and the maximum allowed prompt length is set to 16,384 tokens.

| Model | NarrativeQA F1 (0-shot) | Qasper F1 (2-shot) | QuALITY EM (2-shot) | QMSum ROUGE-geo* (1-shot) |
|---|---|---|---|---|
| Focused Transformer (3B) | 16.3 | 15.4 | 20.5 | 10.6 |
| Yarn-7B-128k | 20.9 | 26.2 | 32.3 | 11.4 |
| Together-7B-32k^{+} | 23.3 | 27.3 | 41.2 | 12.6 |
| Xgen-7B-8k-base | 17.4 | 20.5 | 21.0 | 6.79 |
| MPT-7B-8k | 18.8 | 24.7 | 23.7 | 8.78 |
| Yarn-13B-128k | 23.4 | 27.1 | 46.4 | 11.9 |
| MPT-30B-8k | 22.9 | 29.0 | 41.5 | 10.3 |
| LLAMA 2 70B | 25.7 | 27.5 | 53.0 | 11.9 |
| LLAMA 2 LONG 7B | 21.9 | 27.8 | 43.2 | 14.9 |
| LLAMA 2 LONG 13B | 25.6 | 31.2 | 57.6 | 15.7 |
| LLAMA 2 LONG 34B | 29.4 | 33.7 | 65.7 | 15.9 |
| LLAMA 2 LONG 70B | **30.9** | **35.7** | **79.7** | **16.5** |

[p. 5] At the 7B scale, only "Together-7B-32k" can match the model's performance, but that model is not purely self-supervised and has been finetuned using a large supervised dataset. The 7/13B variants have been trained with 32k-token sequences; comparisons using 32,768 maximum prompt lengths are consistent, as shown in Table 13 (Appendix).

### Effective Context Utilization [p. 5]

[p. 5] The authors validate that their models can effectively use increased context window by showing (Figure 2) that results on each long task improve monotonically as context lengths increase. Inspired by Kaplan et al. (2020) and Hoffmann et al. (2022), they found that the language modeling loss follows a power-law plus constant scaling relationship with the context length (Figure 1), suggesting:

- The model continues to show gain in performance (on language modeling loss) up to 32,768 tokens of text, despite having diminishing returns. For the 70B model, doubling the context length reduces the loss by a factor of 2^{-beta} ~ 0.7 plus a model specific constant (1 - 2^{-beta}) * gamma.
- Larger models can leverage the contexts more effectively, indicated by the larger beta value of the curves.

**Figure 1** (p. 1): "We show that our model's validation loss can be fit as a function of the context length: L(c) = (alpha/c)^{beta} + gamma with a different set of alpha, beta, gamma for each model size. This power-law relationship also suggests that context length is another important axis of scaling LLMs and our model can continually improve its performance as we increase the context length up to 32,768 tokens."

The figure shows validation loss (y-axis) vs. context length (x-axis, log scale from 10^0 to 10^4) for four model sizes. All curves decrease monotonically. Fitted parameters:
- LLAMA 2 LONG 7B: alpha = 25.4, beta = 0.45, gamma = 1.56
- LLAMA 2 LONG 13B: alpha = 19.5, beta = 0.48, gamma = 1.45
- LLAMA 2 LONG 34B: alpha = 17.7, beta = 0.50, gamma = 1.41
- LLAMA 2 LONG 70B: alpha = 17.9, beta = 0.51, gamma = 1.35

**Figure 2** (p. 5): "Performance on long-context tasks as the maximum context lengths of prompts increase."

The figure contains four subplots, each showing performance (y-axis) vs. maximum input length (x-axis: 4,096 / 8,192 / 12,288 / 16,384) for the LLAMA 2 LONG 70B model:
- NarrativeQA (F1): 27.5 -> 28.7 -> 30.2 -> 30.9
- Qasper (F1): 28.9 -> 32.7 -> 35.1 -> 35.7
- QuALITY (EM): 63.9 -> 80.3 -> 79.6 -> 79.7
- QMSum (ROUGE-geo): 10.9 -> 11.9 -> 14.4 -> 16.5

All four tasks show generally increasing performance with context length. QuALITY shows a slight dip from 80.3 to 79.6 between 8,192 and 12,288 before recovering to 79.7 at 16,384.

## Instruction Tuning Results [p. 6]

### ZeroSCROLLS Benchmark [p. 6]

[p. 6] The instruction-tuned model is tested on ZeroSCROLLS (Shaham et al., 2023), which bundles 10 long-context datasets spanning summarization, question answering, to multi-document aggregation tasks. The same configuration (prompts, truncation strategy, and maximum generation lengths, etc) is used as specified by the benchmark. Without using any human annotated long context data, the 70B chat model outperforms gpt-3.5-turbo-16k on 7 out of the 10 tasks. Evaluations on six new long tasks in L-Eval (An et al., 2023) again show strong results, as shown in Table 17 in the Appendix. The finetuned model is particularly good at QA tasks which is the main theme of the self-instruct data.

[p. 6] Evaluating long-context LLMs is a nontrivial task. Caveats noted:
- Summarization tasks come with a single ground-truth summary and n-gram matching metrics do not necessarily align with human preference
- For QA and aggregation tasks, truncating the input context might also remove information necessary to answer the question
- Most proprietary models do not share training data details, making it hard to account for potential leakage during public benchmark evaluation

**Table 4** (p. 6): ZeroSCROLLS long-context leaderboard results. ^{+}Evaluated as of 8/7/2023. The GPT-4 and Claude results are directly copied from the leaderboard. Underscored are the 7/10 tasks where the model outperforms gpt-3.5-turbo-16k.

| Model | GR | SS | QM | SQAL | Qspr | Nrtv | QALT | MuSQ | SpDg | BkSS | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-3.5-turbo (4k) | 21.3 | 16.1 | 15.6 | 20.4 | 49.3 | 25.1 | 66.6 | 27.1 | 49.1 | 49.8 | 34.0 |
| GPT-3.5-turbo-16k^{+} | 24.3 | 16.2 | 17.4 | 21.4 | 50.0 | 29.5 | 72.0 | 27.0 | 54.1 | 54.6 | 36.7 |
| Claude (8k) | 24.2 | 16.1 | 14.6 | 21.0 | 52.3 | 32.6 | 84.8 | 36.1 | 61.6 | 47.4 | 39.1 |
| GPT4 (8k) | 26.3 | 17.3 | 18.5 | 22.6 | 50.7 | 27.6 | 89.2 | 41.1 | 62.8 | 60.5 | 41.7 |
| LLAMA 2 LONG CHAT 70B | 26.0 | 15.0 | 20.0 | 20.9 | 52.0 | 31.7 | 82.6 | 27.3 | 55.5 | 46.2 | 37.7 |

Column headers: Summarization (GR = GovReport, SS = SummScreenFD, QM = QMSum), SQAL = SQuALITY, Question answering (Qspr = Qasper, Nrtv = NarrativeQA, QALT = QuALITY), MuSQ = MuSiQue, Aggregation (SpDg = SpaceDigest, BkSS = BookSumSort).

## Human Evaluation [p. 6]

[p. 6] Complementary to automatic evaluation, human evaluations are conducted by asking annotators whether they prefer the generation from the instruction finetuned model or from other models.

**Figure 3** (p. 6): "Human preference on model responses with multi-turn conversation and multi-document search query answering data."

Horizontal stacked bar chart showing Win / Tie / Loss rates (% Win Rate) for LLAMA 2 LONG vs. other models:
- LLAMA 2 LONG vs. MPT-30b-chat: Win 53.3 (+/- 2.3), Tie 28.7 (+/- 2.0), Loss 18.1 (+/- 1.8)
- LLAMA 2 LONG vs. GPT-4: Win 25.0 (+/- 1.9), Tie 30.0 (+/- 1.7), Loss 45.0 (+/- 2.3)
- LLAMA 2 LONG vs. GPT-3.5-turbo-16k: Win 35.8 (+/- 1.6), Tie 31.5 (+/- 2.2), Loss 32.8 (+/- 2.1)
- LLAMA 2 LONG vs. Claude-2-100k: Win 38.9 (+/- 1.9), Tie 29.4 (+/- 2.0), Loss 31.7 (+/- 1.8)

---
[p. 6–7 continued]

[p. 6–7] Comparison against proprietary models including MPT-30B-chat, GPT-4, GPT-3.5-turbo-16k, and Claude-2 in terms of helpfulness, honesty, and harmlessness. Unlike automatic metrics, humans are better at evaluating the quality of model responses for long context models because of the large space of acceptable answers. Two major application scenarios are used with a total of 2,352 examples:
- **Multi-turn conversation data:** each prompt is a chat history based on which the model needs to generate a coherent response
- **Multi-document search query answering:** the model is provided with a few most relevant documents retrieved from a search session and the corresponding search query; the model must leverage the retrieved documents to answer the given query

Each comparison example was evaluated by 3 different human annotators. The standard win rate is calculated by averaging the result of each comparison example and the final score along with the 95% confidence interval is shown in Figure 3.

[p. 7] With very little instruction data, the model can achieve competitive performance against MPT-30B-chat, GPT-3.5-turbo-16k, and Claude-2. Human evaluation on longer context tasks is challenging and generally requires well trained and skilled annotators. The authors hope this study can give a sense of the potential of their instruction finetuned model on some long context downstream applications and also motivate future efforts in developing more robust long context automatic evaluations.
