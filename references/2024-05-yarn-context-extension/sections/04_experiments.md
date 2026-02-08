# 4 Experiments [p. 7-10]

The authors show that YaRN successfully achieves context window extension of language models using RoPE as its position embedding. This result is achieved with only 400 training steps, representing approximately 0.1% of the model's original pre-training corpus, a 10x reduction from Roziere et al. [31] and 2.5x reduction in training steps from Chen et al. [9], making it highly compute-efficient for training with no additional inference costs. They calculate the perplexity of long documents and score on established benchmarks to evaluate the resulting models, finding that they surpass all other context window extension methods. [p. 7-8]

They broadly followed the training and evaluation procedures as outlined in [9]. [p. 8]

## 4.1 Training [p. 8]

For training, the authors extended the Llama 2 [39] 7B and 13B parameter models. No changes were made to the LLaMA model architecture other than the calculation of the embedding frequencies as described in Section 3.4 with $s = 16$ and $s = 32$. [p. 8]

Training hyperparameters: [p. 8]
- Learning rate: $2 \times 10^{-5}$
- Weight decay: none
- Linear warmup: 20 steps
- Optimizer: AdamW [24] with $\beta_1 = 0.9$ and $\beta_2 = 0.95$
- Batch size: global batch size 64
- For $s = 16$: fine-tuned for 400 steps
- For $s = 32$: followed the same procedure, but started from the finished $s = 16$ checkpoint and trained for an additional 200 steps

Framework: PyTorch [26] with Fully Sharded Data Parallelism [42] and Flash Attention 2 [13]. [p. 8]

Dataset: PG19 dataset [29] chunked into 64k segments bookended with the BOS and EOS token. [p. 8]

## 4.2 Extrapolation and Transfer Learning [p. 8]

In Code Llama [31], a dataset with 16k context was used with a scale factor set to $s \approx 88.6$, which corresponds to a context size of 355k. They show that the network extrapolates up to 100k context without ever seeing those context sizes during training. Similar to Section 3.1 and Roziere et al. [31], YaRN also supports training with a higher scale factor $s$ than the length of the dataset. Due to compute constraints, they test only $s = 32$ by further fine-tuning the $s = 16$ model for 200 steps using the same dataset with 64k context. [p. 8]

The authors show in Section 4.3.1 that the $s = 32$ model successfully extrapolates up to 128k context using only 64k context during training. Unlike previous "blind" interpolation methods, YaRN is much more efficient at transfer learning when increasing the scale $s$. This demonstrates successful transfer learning from $s = 16$ to $s = 32$ without the network needing to relearn the interpolated embeddings, as the $s = 32$ model is equivalent to the $s = 16$ model across the entire context size, despite only being trained on $s = 32$ for 200 steps. [p. 8]

## 4.3 Evaluation [p. 8]

The evaluations focus on three aspects: [p. 8]
1. the perplexity scores of fine-tuned models with extended context window,
2. the passkey retrieval task on fine-tuned models,
3. the common LLM benchmark results of fine-tuned models.

## 4.3.1 Long Sequence Language Modeling [p. 8-9]

To evaluate the long sequence language modeling performances, the authors use the GovReport [18] and Proof-pile [4] datasets both of which contain many long sequence samples. For all evaluations, the test splits of both datasets were used exclusively. All perplexity evaluations were calculated using the sliding window method from Press et al. [27] with $S = 256$. [p. 8]

Firstly, they evaluated how the model performed as the context window increased. They selected 10 random samples from Proof-pile with at least 128k tokens each and evaluated the perplexity of each of these samples when truncated at 2k steps from a sequence length of 2k tokens through 128k tokens. [p. 8]

**Table 1** (p. 9): "Sliding window perplexity (S = 256) of ten 128k Proof-pile documents over Llama-2 extended via PI, NTK and YaRN"

| Extension Method | Trained Tokens | Context Window | 2048 | 4096 | 6144 | 8192 | 10240 |
|---|---|---|---|---|---|---|---|
| PI ($s = 2$) | 1B | 8k | 3.92 | 3.51 | **3.51** | **3.34** | 8.07 |
| NTK ($\theta = 20$k) | 1B | 8k | 4.20 | 3.75 | 3.74 | 3.59 | 6.24 |
| YaRN ($s = 2$) | 400M | 8k | **3.91** | **3.50** | **3.51** | 3.35 | **6.04** |

Table 1 shows a side-by-side comparison of Llama-2 model extended from 4096 to 8192 context length via PI (LLongMA-2 7b$^5$), "NTK-aware" and YaRN. Note that PI and "NTK-aware" models were trained using the methodology in Chen et al. [9], while YaRN used the same methodology but 2.5x less training steps and data, as described in Section 4.1. [p. 9]

Footnote 5: LLongMA-2 7b [28] is fine-tuned from Llama-2 7b, trained at 8k context length with PI using the RedPajama dataset [12]. [p. 9]

The authors further evaluated YaRN at the scale factor $s = 16, 32$ and compared them against a few open-source models fine-tuned from Llama-2 and extended to more than 32k context window such as Together.ai [37] and "NTK-aware" Code Llama [31]. The results are summarized in Table 2 (with a more detailed plot in Figure 1). [p. 9]

**Table 2** (p. 9): "Sliding window perplexity (S = 256) of ten 128k Proof-pile documents truncated to evaluation context window size"

| Model Size | Model Name | Context Window | Extension Method | 8192 | 32768 | 65536 | 98304 | 131072 |
|---|---|---|---|---|---|---|---|---|
| 7B | Together | 32k | PI | **3.50** | **2.64** | $> 10^2$ | $> 10^3$ | $> 10^4$ |
| 7B | Code Llama | 100k | NTK | 3.71 | 2.74 | 2.55 | 2.54 | 2.71 |
| 7B | YaRN ($s = 16$) | 64k | YaRN | 3.51 | 2.65 | **2.42** | $> 10^1$ | $> 10^1$ |
| 7B | YaRN ($s = 32$) | 128k | YaRN | 3.56 | 2.70 | 2.45 | **2.36** | **2.37** |
| 13B | Code Llama | 100k | NTK | 3.54 | 2.63 | 2.41 | 2.37 | 2.54 |
| 13B | YaRN ($s = 16$) | 64k | YaRN | **3.25** | **2.50** | **2.29** | $> 10^1$ | $> 10^1$ |
| 13B | YaRN ($s = 32$) | 128k | YaRN | 3.29 | 2.53 | 2.31 | **2.23** | **2.24** |

The authors observe the model exhibits strong performance across the entire targeted context size, with YaRN interpolation being the first method to successfully extend the effective context size of Llama 2 to 128k. Of particular note are the YaRN ($s = 32$) models, which show continued declining perplexity through 128k, despite the fine-tuning data being limited to 64k tokens in length, demonstrating that the model is able to generalize to unseen context lengths. [p. 9]

Furthermore, in Appendix B.1, the authors show the results of the average perplexity on 50 untruncated GovReport documents with at least 16k tokens per sample evaluated on the setting of 32k maximal context window without Dynamic Scaling in Table 4. Similar to the Proof-pile results, the GovReport results show that fine-tuning with YaRN achieves good performance on long sequences. [p. 9]

## 4.3.2 Passkey Retrieval [p. 9]

The passkey retrieval task as defined in [25] measures a model's ability to retrieve a simple passkey (i.e., a five-digit number) from amongst a large amount of otherwise meaningless text. For their evaluation of the models, the authors performed 10 iterations of the passkey retrieval task with the passkey placed at a random location uniformly distributed across the evaluation context window on different context window sizes ranging from 8k to 128k. Both 7b and 13b models fine-tuned using YaRN at 128k context size passes the passkey retrieval task with very high accuracy ($> 99\%$) within the entire context window size. Detailed results are shown in Appendix B.2. [p. 9]

## 4.3.3 Standardized Benchmarks [p. 9-10]

The Hugging Face Open LLM Leaderboard [19] compares a multitude of LLMs across a standardized set of four public benchmarks. Specifically, the authors use 25-shot ARC-Challenge [11], 10-shot HellaSwag [41], 5-shot MMLU [17], and 0-shot TruthfulQA [23]. [p. 9]

To test the degradation of model performance under context extension, they evaluated their models using this suite and compared it to established scores for the Llama 2 baselines as well as publicly available PI and "NTK-aware" models. The results are summarized in Table 3. [p. 9-10]

**Table 3** (p. 10): "Performance of context window extensions methods on the Hugging Face Open LLM benchmark suite compared with original Llama 2 baselines"

| Model Size | Model Name | Context Window | Extension Method | ARC-c | Hellaswag | MMLU | TruthfulQA |
|---|---|---|---|---|---|---|---|
| 7B | Llama 2 | 4k | None | **53.1** | 77.8 | **43.8** | 39.0 |
| 7B | Together | 32k | PI | 47.6 | 76.1 | 43.3 | **39.2** |
| 7B | Code Llama | 100k | NTK | 39.9 | 60.8 | 31.1 | 37.8 |
| 7B | YaRN ($s = 16$) | 64k | YaRN | 52.3 | **78.8** | 42.5 | 38.2 |
| 7B | YaRN ($s = 32$) | 128k | YaRN | 52.1 | 78.4 | 41.7 | 37.3 |
| 13B | Llama 2 | 4k | None | **59.4** | 82.1 | **55.8** | 37.4 |
| 13B | Code Llama | 100k | NTK | 40.9 | 63.4 | 32.8 | **43.8** |
| 13B | YaRN ($s = 16$) | 64k | YaRN | 58.1 | **82.3** | 52.8 | 37.8 |
| 13B | YaRN ($s = 32$) | 128k | YaRN | 58.0 | 82.2 | 51.9 | 37.3 |

The authors observe that there is minimal performance degradation between the YaRN models and their respective Llama 2 baselines. They also observe that there was on average a 0.49% drop in scores between the YaRN $s = 16$ and $s = 32$ models. From this they conclude that the iterative extension from 64k to 128k results in negligible performance loss. [p. 10]
