# A Appendix [p. 14–16]

## A.1 Baseline Models in L-Eval [p. 14–15]

### Commercial Models

[p. 14]

- **Claude-100k** is developed by Anthropic and targets understanding extremely long documents and answering related questions. It has the longest context length among all the LLMs.
- **GPT-4-32k** is developed by OpenAI. It is the long context version of GPT-4 maintaining very strong reasoning ability over 32k context length but also the most expensive model.
- **Turbo-4k-0613** is the snapshot of GPT-3.5 from June 13th 2023 which can handle up to 4k input tokens. Turbo-16k-0613 is the released long context version of Turbo-4k-0613.

### Open-source Models

[p. 14]

- **Llama1** (Touvron et al., 2023a) is a widely used open-source model developed by Meta AI with a 2k pre-training context length. The first version of Llama did not release a chatbot-based model.
- **Vicuna1.3** (Chiang et al., 2023) is a chatbot fine-tuned from Llama1 on shareGPT.
- **Longchat-16k** (Li et al., 2023a) is the long context version of Vicuna. It uses positional interpolation to adapt 16k context. Concretely, they further fine-tune Llama1 on lengthy dialogues (16k tokens) from shareGPT.
- **Llama2** (Touvron et al., 2023b) is the second version of Llama recently released by Meta AI. The updated version has 4k pretraining context with more powerful long context understanding capabilities.
- **Llama2-chat** (Touvron et al., 2023b) is a chatbot based on Llama2 released together with Llama2. If the pre-defined input format is not followed (i.e., ignore the special tokens), there will be a significant degradation in performance.
- **Llama2-NTK-chat** (LocalLLaMA, 2023b) is the long context version of Llama2-chat. It uses NTK-aware positional embedding. If the model context window is to be extended to *t* (called *t* as a scale-up factor) times its original pertaining size, the original base=10,000 of RoPE (theta_n = 10000^{-2n/d}) is increased to 10,000 x t^{d/(d-2)} where *d* is the head dimension in Transformer. In the authors' experiments, this theory does not hold in practical tasks: the model still tends to generate random tokens when setting t = 4 on 16k context length. They set t = 8 in experiments.
- **Llama2-NTK-chat (Dyn)** (LocalLLaMA, 2023a) is the dynamic version of Llama2-NTK-chat. The only difference is that the scale-up factor *t* in dynamic NTK depends on the current input length *L* and the pertaining length *l*, i.e., t = L/l.
- **Vicuna1.5-16k** uses Llama2 as the base model and performs further finetuning on concatenated 16k tokens lengthy dialogues from shareGPT. This model is based on positional interpolation which helps the training process converge fast.
- **LongChat1.5-32k** is the 32k version of Vicuna1.5-16k.
- **Chatglm2-8k** (Du et al., 2022) is the second version of the open-source bilingual chat model Chatglm. The context length of the base model is further pretrained with 32k context window and finetuned on dialogue data with 8k context window.
- **Chatglm2-32k** is the long context version of Chatglm2 using positional interpolation.

[p. 15]

- **XGen-8k-inst** developed by Salesforce follows a multi-stage pertaining procedure. They first train the model with 2k context length and progressively increase the pertaining length to 4k, finally reaching 8k.
- **MPT-7B-StoryWriter-65k** is designed to handle super-long context lengths. It was tuned on MPT-7B with a context length of 65k tokens on a subset of Books3 dataset.

## A.2 Human Evaluation [p. 15–16]

[p. 15] Evaluating long-sequence, open-ended tasks remains a challenge. As previously discussed, almost all metrics, including the highly accurate automatic metric, the GPT-4 evaluator, exhibit bias. Consequently, human evaluation may be the most equitable metric to assess these models. The authors detail the human evaluation procedure conducted on seven baseline models using an 85-question subset. The goal is to examine the correlation between human judgement and automatic metrics. Additionally, the aim is to evaluate the performance of the length-instruction-enhanced evaluation method proposed in the paper.

**Experimental setup:** Seven models are evaluated, comprising three commercial and four open-source models: (1) Claude-100k, (2) turbo-16k-0613, (3) Turbo-4k-0613, (4) Vicuna1.5-7b-16k (Llama2), (5) Longchat-7b-16k (Llama1), (6) Llama2-7b-chat, and (7) Llama2-13b-chat. These models are tested on an 85-question subset of L-Eval open-ended tasks. Each sample is scored by three annotators, all of whom are Ph.D. students researching long context language models. The average score is calculated to obtain the final human evaluation results. To determine if the ranking produced by automatic metrics correlates with the ranking provided by the annotators, the Kendall-Tau correlation coefficient is used. Each model generates outputs twice: first in the original mode without any length instruction, and then with the given length instructions. Greedy search is used as the decoding algorithm to minimize variance. The model outputs are ranked on a five-level scale: [p. 15]

- Level-1 (worst): The response is totally unhelpful to answer the question.
- Level-2: The output generally deviates from the original question, but some information is useful to solve the problem.
- Level-3: The response is partially correct, but the generated answer may contain some errors or omit key information.
- Level-4: Most of the response is correct, but there may be minor issues such as being overly long (which cannot be considered a flaw if it is a reasonable explanation), or it might omit some information, but this does not affect the overall meaning.
- Level-5 (best): The output is close-to-human or even better.

[p. 16]

**Human evaluation results:** The results are presented in Table 5. Despite being fine-tuned on longer contexts, open-source long context models still struggle with very long input sequences during inference. When fed with numerous input tokens, the number of Level-1 outputs from open-source LCLMs significantly increases, while the LLMs with only a 4k context length can maintain their generation quality at a partially correct level, albeit without achieving high scores. The N-gram metrics F-1 and ROUGE generally do not correlate with the human evaluation results. Given the impracticality of testing a large number of samples using LLMs due to high costs and inefficiency, the authors urge for more advanced metrics. They will release their human assessment to aid research on these metrics.

**Table 5** (p. 15): "Human evaluation results and results from other automatic metrics where **#Level-N** denotes the number of outputs (the sum from all annotators) in Level-N on the 85-question subset. Texts colored with red mean very unsatisfactory results."

*Length-instruction-enhanced evaluation results:*

| Model | #Level-1 | #Level-2 | #Level-3 | #Level-4 | #Level-5 | Human-Avg | GPT-4 | GPT-3.5 | F-1 | R-L |
|---|---|---|---|---|---|---|---|---|---|---|
| llama2-7b-chat | 53 | 38 | 74 | 46 | 44 | 2.96 | 38.52 | 42.37 | 24.26 | 28.48 |
| llama2-13b-chat | 41 | 37 | 68 | 59 | 50 | 3.15 | 40.00 | 48.07 | 26.10 | 30.90 |
| Turbo-4k-0613 | 43 | 29 | 51 | 72 | 60 | 3.30 | 42.05 | 43.75 | 26.05 | 30.75 |
| Claude-100k | 14 | 15 | 37 | 69 | 120 | 4.04 | **60.88** | **63.75** | 26.39 | 31.57 |
| turbo-16k-0613 | 37 | 12 | 43 | **90** | 73 | 3.58 | 50.00 | 50.00 | **27.99** | **32.93** |
| Vicuna-7b-16k | **125** | 26 | 45 | 43 | 16 | 2.21 | 23.23 | 35.09 | 16.25 | 19.40 |
| longchat-7b-16k | **113** | 29 | 61 | 32 | 20 | 2.28 | 23.82 | 37.57 | 17.12 | 20.81 |

*Original evaluation results:*

| Model | #Level-1 | #Level-2 | #Level-3 | #Level-4 | #Level-5 | Human-Avg | GPT-4 | GPT-3.5 | F-1 | R-L |
|---|---|---|---|---|---|---|---|---|---|---|
| llama2-7b-chat | **136** | 49 | 47 | 15 | 8 | 1.86 | 32.35 | 42.40 | 14.29 | 17.72 |
| llama2-13b-chat | 92 | 50 | 64 | 38 | 11 | 2.31 | 35.00 | 55.76 | 13.62 | 18.10 |
| Turbo-4k-0613 | 66 | 38 | 60 | 40 | 51 | 2.89 | 50.00 | 44.06 | 20.06 | 24.88 |
| Claude-100k | 27 | 52 | 81 | 66 | 29 | 3.08 | **53.23** | **76.68** | 15.31 | 19.59 |
| turbo-16k-0613 | 42 | 40 | 78 | 64 | 31 | 3.00 | 50.00 | 50.00 | 20.60 | **25.96** |
| Vicuna-7b-16k | **138** | 49 | 46 | 14 | 8 | 1.84 | 23.23 | 38.27 | 14.69 | 17.90 |
| longchat-7b-16k | **156** | 40 | 36 | 18 | 5 | 1.72 | 22.05 | 35.76 | 13.25 | 15.73 |

## A.3 Analysis [p. 16]

[p. 16]

**Table 6** (p. 16): "Performance of various models on open-ended QA datasets in terms of F1 score. For results tested with N-gram metrics, please note that the results may not be accurate when the performance of the models is very similar or there is a large difference in the granularity of the output."

| Model | Ret. | Tokens | Fin. | Contract | Multidoc | Nrtv | NQ | SCI | Avg. |
|---|---|---|---|---|---|---|---|---|---|
| Turbo-16k-0613 | ✗ | 16k | **45.36** | 24.87 | 31.45 | 18.20 | 45.90 | 28.25 | 32.33 |
| AdaEmb-Turbo-0613 | ✓ | 4k | 39.69 | 24.09 | **35.62** | **18.59** | 49.66 | **33.36** | **33.50** |
| BM25-Turbo-0613 | ✓ | 4k | 40.79 | **26.10** | 35.17 | 16.32 | **53.73** | 25.83 | 32.99 |
| *Truncating input tokens to the pretraining context length* | | | | | | | | | |
| Llama2-7b-chat | ✗ | 4k | **40.06** | 23.00 | **27.28** | 13.48 | 28.11 | 25.95 | 26.31 |
| Llama2-13b-chat | ✗ | 4k | 38.07 | **23.14** | 26.14 | **16.76** | **35.43** | **27.46** | **27.83** |
| Vicuna1.3-7b | ✗ | 2k | 30.49 | 17.69 | 17.70 | 14.57 | 15.49 | 7.69 | 17.27 |
| Longchat-7b-16k | ✗ | 2k | 27.27 | 19.78 | 13.99 | 13.21 | 18.11 | 7.61 | 16.66 |
| Chatglm2-6b-8k | ✗ | 2k | 29.60 | 19.06 | 16.22 | 13.21 | 17.52 | 12.26 | 17.97 |
| XGen-7b-8k (2k-4k-8k) | ✗ | 2k | 34.43 | 21.28 | 21.59 | 14.97 | 29.58 | 14.12 | 22.66 |
| *Truncating input tokens to the further finetuning context length* | | | | | | | | | |
| Chatglm2-7b-32k | ✗ | 32k | 30.27 | **26.95** | **24.97** | 14.00 | **37.94** | **26.44** | **26.76** |
| Longchat1.5-7b-32k | ✗ | 32k | **36.06** | 18.16 | 14.96 | 11.79 | 24.92 | 12.09 | 19.66 |
| Longchat-7b-16k | ✗ | 16k | 38.37 | 26.78 | 8.31 | **15.17** | 20.21 | 9.74 | 19.76 |
| Vicuna1.5-7b-16k | ✗ | 16k | 39.31 | 18.04 | 18.44 | 8.19 | 19.39 | 21.80 | 20.86 |
| Longchat-13b-16k | ✗ | 16k | 37.85 | 21.11 | 12.18 | 14.76 | 22.75 | 14.95 | 20.60 |
| Vicuna1.5-13b-16k | ✗ | 16k | **45.57** | 18.16 | 15.88 | 15.03 | 37.13 | 23.40 | 25.86 |
| Llama2-13b-NTK* | ✗ | 16k | 30.99 | 15.88 | 13.61 | 6.89 | 11.13 | 15.58 | 15.67 |
| Llama2-13b-NTK(Dyn)* | ✗ | 16k | 39.99 | 18.59 | 25.49 | 13.09 | 14.51 | **26.90** | 23.09 |
| Longchat-13b-16k | ✗ | 8k | 36.94 | 16.70 | 10.77 | 7.55 | 14.14 | 9.91 | 16.00 |
| Chatglm2-6b-8k | ✗ | 8k | 33.17 | 15.76 | 13.76 | 7.02 | 3.50 | 6.36 | 13.26 |
| XGen-7b-8k | ✗ | 8k | 36.40 | 22.01 | 17.08 | 9.41 | 13.88 | 20.23 | 19.83 |
| MPT-7b-65k | ✗ | 8k | 10.01 | 6.24 | 3.95 | 1.77 | 0.77 | 1.68 | 4.06 |

**Results from n-gram metrics:** [p. 16–17] Testing all cases in open-ended tasks in L-Eval with GPT-4 is not affordable. To give an overview of all models on open-ended tasks, all models are tested with n-gram metrics. As can be seen from the win rate from LLM judges (Table 4) and human evaluation (Table 5), there is still a significant margin between commercial LLMs and open-source LLMs. However, the margin is not clear enough based on n-gram metrics. Based on n-gram metrics, the open-source LCLMs also fail to beat their origin short-context model on truncated context. Overall, current open-source LCLMs generally excel more in conventional summarization tasks that involve instructions like "Summarize this document" compared with query-based summarization and QA tasks. For query-based tasks that pose questions from a specific perspective, performance can be significantly degraded if the instruction is not fully understood. The increased input length can also lower the model's ability to comprehend lengthy instructions, thereby inhibiting its capability to generate answers that closely match the length of the ground truth. This phenomenon is less likely to be observed with more sophisticated LLMs (i.e. Turbo-16k). A naive solution is adding the instruction at both the beginning and end of the long input but there is still room to improve the ability of instruction understanding for LCLMs. [p. 17]

**Table 7** (p. 17): "Performance of various models on **query-based** summarization and generation tasks in terms of ROUGE."

| Model | Tokens | paper_assistant R-1 | paper_assistant R-2 | paper_assistant R-L | review_summ R-1 | review_summ R-2 | review_summ R-L | meeting_summ R-1 | meeting_summ R-2 | meeting_summ R-L | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Turbo-16k-0613 | 16k | 39.55 | 10.92 | 18.61 | **30.18** | **7.14** | 18.67 | 30.20 | 7.22 | 19.31 | 20.20 |
| AdaEmb-Turbo-0613 | 4k | 38.07 | 9.61 | 17.33 | 29.81 | 6.47 | **18.91** | **31.92** | **8.24** | **20.84** | 20.13 |
| BM25-Turbo-0613 | 4k | **41.59** | **13.39** | **21.24** | 29.89 | 5.99 | 18.19 | 31.37 | **8.50** | 20.65 | **21.20** |
| *Truncating input tokens to the pretraining context length* | | | | | | | | | | | |
| Llama2-7b-chat | 4k | 37.15 | 9.47 | 18.05 | 29.75 | 6.61 | 18.96 | 28.75 | 6.24 | 19.37 | 19.37 |
| Llama2-13b-chat | 4k | 37.27 | 9.79 | 18.49 | **30.49** | **6.69** | **19.23** | **29.63** | **6.54** | **19.65** | **19.75** |
| Vicuna1.3-7b | 2k | 34.63 | 8.73 | 16.87 | 29.01 | 6.28 | 18.18 | 24.18 | 4.93 | 15.93 | 17.63 |
| Longchat-7b-16k | 2k | 37.01 | 9.61 | 18.21 | 26.45 | 5.05 | 16.88 | 23.92 | 4.65 | 15.75 | 17.50 |
| Chatglm2-6b-8k | 2k | 36.91 | 9.45 | 17.96 | 27.74 | 5.77 | 17.62 | 25.92 | 5.61 | 17.57 | 18.28 |
| XGen-7b (2k-4k-8k) | 2k | **37.72** | **9.97** | **18.77** | 28.21 | 5.94 | 18.69 | 26.94 | 5.92 | 18.24 | 18.93 |
| *Truncating input tokens to the further finetuning context length* | | | | | | | | | | | |
| Chatglm-6b-32k | 32k | 32.65 | 8.09 | 16.51 | 22.05 | 6.10 | 16.61 | **28.94** | **8.86** | **20.83** | 17.84 |
| Longchat1.5-7b-32k | 32k | 32.49 | 7.79 | 15.97 | 27.53 | 5.80 | 17.94 | 25.29 | 5.22 | 16.49 | 17.16 |
| Longchat-7b-16k | 16k | 35.05 | 8.57 | 16.70 | 26.07 | 5.97 | 17.06 | 20.13 | 4.74 | 13.21 | 16.38 |
| Vicuna1.5-7b-16k | 16k | 36.84 | 9.78 | 17.66 | 28.91 | 6.47 | 18.25 | 26.90 | 5.53 | 17.33 | 18.63 |
| Longchat-13b-16k | 16k | 34.41 | 8.07 | 16.45 | 27.24 | 5.63 | 17.00 | 24.58 | 5.85 | 16.32 | 17.28 |
| Vicuna1.5-13b-16k | 16k | 36.30 | 8.69 | 18.20 | 28.59 | 6.15 | 18.49 | 27.82 | 6.39 | 18.83 | 18.82 |
| Llama2-13b-NTK* | 16k | 35.22 | 8.53 | 17.04 | 23.97 | 4.72 | 14.89 | 18.92 | 4.13 | 13.16 | 15.61 |
| Llama2-13b-NTK(Dyn)* | 16k | 28.89 | 7.21 | 14.83 | 26.86 | 5.33 | 17.55 | 22.29 | 4.88 | 15.29 | 15.90 |
| Longchat-13b-16k | 8k | 34.29 | 8.21 | 16.06 | 26.76 | 5.61 | 16.77 | 20.86 | 4.01 | 13.81 | 16.26 |
| Chatglm2-6b-8k | 8k | **38.07** | **9.61** | 17.33 | **29.81** | **6.47** | **18.91** | 24.74 | 4.45 | 4.44 | 18.36 |
| XGen-7b-8k | 8k | 35.94 | 8.49 | **17.92** | 28.92 | 6.28 | **19.11** | 28.06 | 6.12 | 19.17 | **18.89** |
| MPT-7b-65k | 8k | 15.91 | 2.91 | 11.18 | 7.66 | 1.00 | 7.00 | 5.24 | 0.71 | 5.10 | 6.30 |

---
[p. 17–18 continued]

**Retrieve-based models vs long context models:** [p. 17–18] The authors compare a representative LCLM baseline Turbo-16k-0613 with its short version Turbo-4k-0613 enhanced with retrieval in Table 3 (closed-ended tasks) and Table 4 (open-ended tasks). They use a sparse retrieval retriever bm25 and a strong dense retriever text-embedding-ada-002. Retrieve-based approaches generally yield better outcomes for tasks that have readily retrievable answers. For example, for long lectures understanding where the long document always contains some definitions and explanations for some academic terms, retrieval-based approaches obtain better results. However, retrieval is not a general solution as its performance is strongly related to instruction and document style. For example, they would never answer questions like *how many sentences are there in a document*. Results show that **CodeU** and **GSM(16-shot)** in L-Eval can not be solved by retrieval. Retrieval-based methods also face difficulties in automatically **identifying the query** from user inputs. Retrieval methods demonstrate comparatively less satisfactory performance in tasks where the answer cannot be retrieved, such as topic retrieval or tasks that demand models with long-range reasoning abilities like financial QA. Retrieve-based models produce similar or even superior results for summarization tasks, possibly because some paragraphs resembling summaries can be retrieved. The main reason why regular Turbo-0613 outperforms Turbo-16k is its superior ability to accurately follow instructions. However, even for these tasks, there are instances where the predicted answer might be "I don't know" or "not mentioned" due to the limitation of the retrieval process. When evaluating retrievers, bm25 often matches the performance of the dense retriever, ada-embedding, in closed-ended tasks. However, in the open-ended tasks, the dense retriever ada-embedding outperforms BM25 by more than two points. This superior performance can be attributed to the dense retriever's ability to leverage not only term matching but also semantic matching. [p. 18]

**Table 8** (p. 18): "Performance of various models on long document summarization tasks in terms of ROUGE."

| Model | Tokens | gov_report R-1 | gov_report R-2 | gov_report R-L | news R-1 | news R-2 | news R-L | patent R-1 | patent R-2 | patent R-L | tv_show R-1 | tv_show R-2 | tv_show R-L | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Turbo-16k-0613 | 16k | **45.9** | **15.6** | **23.6** | 35.3 | 8.1 | 16.1 | **46.0** | **20.3** | **29.3** | 32.0 | 5.4 | 16.9 | 24.5 |
| AdaEmb-Turbo-0613 | 4k | 45.0 | 14.3 | 20.8 | 35.7 | 7.7 | 15.4 | 45.6 | 15.9 | 27.6 | 30.0 | 3.3 | 15.2 | 23.0 |
| bm25-Turbo-0613 | 4k | 44.6 | 14.2 | 21.5 | **38.4** | **9.1** | **16.8** | 43.3 | 15.5 | 27.1 | 31.0 | 4.6 | 15.4 | 23.4 |
| *Truncating input tokens to the pretraining context length* | | | | | | | | | | | | | | |
| llama2-7b-chat | 4k | 43.7 | 15.3 | 22.2 | 33.2 | 6.4 | 15.5 | 49.2 | 22.9 | 31.6 | 29.4 | 4.8 | 15.6 | 24.1 |
| llama2-13b-chat | 4k | **46.3** | **16.1** | **24.0** | **34.9** | **8.1** | **16.3** | 48.4 | 20.9 | 30.3 | **32.6** | **6.6** | **17.2** | **25.1** |
| vicuna1.3-7b | 2k | 44.6 | 16.4 | 23.2 | 32.9 | 6.9 | 14.8 | 44.7 | 20.4 | 28.8 | 28.7 | 3.6 | 14.8 | 23.3 |
| longchat-7b-16k | 2k | 43.6 | 16.2 | 23.7 | 28.1 | 4.8 | 13.0 | 47.0 | 22.2 | 30.9 | 27.2 | 3.0 | 14.4 | 22.8 |
| chatglm2-6b-8k | 2k | 45.2 | **18.3** | **24.6** | 32.1 | 6.9 | 15.0 | 44.6 | 22.1 | 30.0 | 26.4 | 2.6 | 13.8 | 23.4 |
| xgen-7b-8k | 2k | 45.1 | 17.2 | 22.9 | 35.0 | 7.5 | 15.5 | **49.6** | **25.2** | **34.6** | 28.8 | 3.6 | 15.4 | 23.9 |
| *Truncating input tokens to the further finetuning context length* | | | | | | | | | | | | | | |
| chatglm2-6b-32k | 32k | 38.1 | 16.1 | 21.0 | 24.2 | 5.8 | 12.8 | 46.5 | 24.1 | **32.5** | 23.4 | 4.2 | 13.8 | 21.8 |
| Longchat1.5-7b-32k | 32k | 45.7 | 17.7 | 24.0 | **36.8** | **8.7** | 15.7 | 42.0 | 18.2 | 27.2 | 21.5 | 2.7 | 13.0 | 22.7 |
| longchat-7b-16k | 16k | 47.2 | 18.9 | 23.9 | 27.7 | 5.4 | 13.4 | 46.2 | 20.9 | 30.1 | 26.2 | 3.3 | 14.7 | 23.1 |
| vicuna1.5-7b-16k | 16k | 47.2 | 18.9 | 25.0 | 32.3 | 6.8 | 15.5 | **48.1** | **25.1** | 32.4 | 26.0 | 3.6 | 14.8 | **24.6** |
| longchat-13b-16k | 16k | 46.2 | 18.2 | 24.1 | 35.2 | 7.6 | 15.8 | 45.3 | 22.6 | 29.8 | **31.9** | **6.0** | **17.3** | 24.0 |
| vicuna1.5-13b-16k | 16k | 45.2 | 17.9 | 24.2 | 31.6 | 6.8 | 15.2 | 46.1 | 21.8 | 30.0 | 28.3 | 3.7 | 16.3 | 23.9 |
| llama2-13b-NTK | 16k | 33.0 | 11.0 | 17.7 | 26.0 | 6.4 | 13.5 | 37.9 | 13.5 | 22.9 | 25.6 | 5.3 | 14.0 | 18.9 |
| llama2-13b-NTK(Dyn) | 16k | 42.0 | 14.9 | 22.4 | 34.0 | 7.8 | **15.9** | 45.3 | 19.1 | 28.5 | 25.5 | 3.9 | 13.9 | 22.7 |
| longchat-13b-16k | 8k | **49.3** | **19.5** | **25.1** | 34.9 | 7.4 | 15.5 | 43.5 | 20.1 | 28.0 | 31.0 | 4.5 | 15.7 | 24.5 |
| chatglm2-6b | 8k | 40.6 | 14.3 | 21.5 | 32.9 | 7.2 | 15.1 | 46.3 | 22.3 | 31.4 | 27.5 | 2.6 | 14.5 | 23.0 |
| xgen-7b-8k | 8k | 40.2 | 13.8 | 21.1 | 31.9 | 6.0 | 15.3 | 45.9 | 21.4 | 29.2 | 28.2 | 3.3 | 15.2 | 22.6 |
| mpt-7b-65k | 8k | 33.3 | 10.7 | 19.3 | 13.6 | 1.5 | 9.2 | 25.5 | 12.2 | 20.2 | 11.0 | 1.3 | 6.4 | 13.6 |

**Dynamic NTK scaling rules do not hold in practical tasks:** [p. 18] Dynamic NTK-aware positional embedding (LocalLLaMA, 2023a) is becoming increasingly popular for extrapolation without further training. Based on dynamic NTK, given an input sequence with length *L* and the model pretraining length *l*, the original base 10,000 in RoPE is set to 10,000 x (L/l)^{d/(d-2)} where *d* is the head dimension. The authors find that the scaling rule does not hold in practical tasks when the number of input tokens changes. The improvements can be further improved using some variants of NTK. Two simple modifications on the original dynamic NTK are studied: [p. 18]

1. **NTK-bias** — base = 10,000 x (L/l + 1)^{d/(d-2)}, where 1 is the bias
2. **NTK-weighted** — base = 10,000 x (L/l + 2)^{d/(d-2)}

Results are shown in Figure 6 where Llama2-PI-sharegpt is a fine-tuned baseline using position interpolation. The test results are on Coursera, truncating the input length. Employing which variants of NTK are strongly affected by the maximum tokens of the dataset. When the input length is between 4k and 8k, NTK+bias gets the best results and NTK-weighted baseline is more robust on 16k input tokens. [p. 18]

**Figure 6** (p. 18): "Performance of different NTK-based methods when tackling input length at multiple scales."
Bar chart with x-axis "Truncated length" (0k, 4k, 8k, 16k) and y-axis "Accuracy(%)" (0 to 48). Five series shown in legend: llama2-PI-sharegpt, llama2-NTK-dyn, llama2-NTK, llama2-NTK-weighted, llama2-NTK+bias. At 4k, llama2-PI-sharegpt leads at ~45%. At 8k, NTK+bias appears highest. At 16k, NTK-weighted performs most robustly. The figure demonstrates that NTK scaling rules are sensitive to input length and no single variant dominates across all lengths.

**Figure 7** (p. 19): "Overall results on open-ended tasks and closed-ended tasks. We find that GPT-4-32k is more capable of closed-ended tasks demonstrating powerful reasoning ability over long context since most closed-ended task in L-Eval has less than 32k input tokens, but the 100k context length help Claude surpass both GPT-4-32k and Turbo-16k on open-ended tasks which generally has more input tokens."
Horizontal bar chart comparing models on both closed-ended (blue bars) and open-ended (yellow/gold bars) tasks. Y-axis lists models from top to bottom: GPT-4-32k, Claude1.3-100k, Turbo-16k-0613, AdaEmb-Turbo-4k, BM25-Turbo-4k, Llama2-13b-chat, Vicuna1.5-13b-16k, Llama2-7b-chat, Llama2-13b-chat [unclear: partially overlapping labels], Chatglm-6b-32k, Longchat-13b-16k, Longchat-7b-16k, Longchat1.5-7b-32k, Chatglm2-6b-8k, Vicuna1.5-7b-16k, XGen-4k. X-axis ranges 0–80. GPT-4-32k achieves the highest closed-ended score (~73). Claude1.3-100k has the highest open-ended score (~66) with a high closed-ended score as well (~66). Open-source models cluster between ~17 and ~45.

**Figure 8** (p. 19): "Overall results on the topic retrieval tasks. Testing short context models on this task with truncated input texts is unfair, so we only include long context LLMs."
Horizontal bar chart with models on y-axis and accuracy (0–100) on x-axis. Only long context LLMs are included. From top: Gpt-4-32k (~91), Claude-100k (~87), Turbo-16k-0613 (~80), llama2-13b-ntk-16k (~76), BM25-turbo-4k (~69), llama2-7b-ntk-16k (~69), Longchat-13b-16k (~67), Chatglm-32k (~67), Vicuna-1.5-13b-16k (~62), Longchat-7b-16k (~61), Longchat1.5-7b-32k (~54), Vicuna-1.5-7b-16k [unclear: exact value, appears ~34–40].
