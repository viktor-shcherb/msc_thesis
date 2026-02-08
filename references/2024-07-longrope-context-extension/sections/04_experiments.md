# 4. Experiments [p. 6-8]

## 4.1. Setup [p. 6]

**Evaluation tasks and models.** LongRoPE is applied on LLaMA2-7B and Mistral-7B, and evaluated on three aspects: (1) perplexity of extended-context LLMs on long documents; (2) Passkey retrieval task that measures a model's ability to retrieve a simple passkey from a sea of irrelevant text; and (3) Standard LLM benchmarks within a short 4096 context window size. [p. 6]

**Fine-tuning.** For LLaMA2, a learning rate of 2e-5 with linear decay and a global batch size of 32. Fine-tuned for 400 steps on Redpajama (Computer, 2023) dataset, chunked into 128k segments bookended with the BOS and EOS tokens. Then, based on the finished checkpoint, an additional 600 steps to achieve 256k context window. The 128k context size is trained on 8 A100 GPUs with the distributed training system (Lin et al., 2023), while the 256k requires 16 A100 GPUs. In the case of Mistral, a constant learning rate of 1e-6 and a global batch size of 64 are used. For both 128k and 256k models, the authors follow the setting in YaRN (Peng et al., 2023), with 400 steps on the Together Computer's Long-Data Collections (mis, 2024) using 16k sequence length. 4 A100 GPUs are used for training. [p. 6]

**Search.** For target window size within 256k: P=64, N_1=N_2=16, p=0.3, T=40, and select top-32 for mutation/crossover in each iteration. Perplexity is calculated using 5 random PG19 validation set samples, with a minimum length requirement of the target context length. For windows over 512k, the population, mutation, and crossover sizes are halved. Perplexity is measured on 3 random samples from Pile-Books3 (Gao et al., 2020) validation set. [p. 6]

**Baselines.** To reach 2048k, fine-tuned models with 128k and 256k context windows are used. This yields LongRoPE-2048k (ft=128k) and LongRoPE-2048k (ft=256k) for LLaMA2 and Mistral, respectively. The four models are compared with state-of-the-art context window extension baselines, specifically open-sourced LLMs fine-tuned after positional interpolation using PI, NTK and YaRN. This includes Together-32k (Together, 2023), Code LLaMA (Roziere et al., 2023), LongLoRA-full-FT-100k (Chen et al., 2023b), YaRN-LLaMA and YaRN-Mistral (Peng et al., 2023). [p. 6]

## 4.2. Main Results [p. 6-8]

### Long sequence language modeling within 256k [p. 6]

Two datasets are used to demonstrate generalizability: Proof-pile (Rae et al., 2019) and PG19 (Gao et al., 2020) test splits. Perplexity is evaluated at various context lengths using sliding window of 256. For PG19, the whole test split of 100 documents is used. For Proof-pile, following YaRN (Peng et al., 2023), 10 samples are randomly selected, each with at least 128k lengths. [p. 6]

Table 5 and Table 7 compare the perplexity of LLaMA2 and Mistral extended via different interpolation methods on Proof-pile and PG19, respectively. Two key observations: **(1)** the extended models show an overall decreasing perplexity trend from 4k to 256k evaluation lengths, proving their abilities to leverage longer context. **(2)** Even with a context window 16x longer, a condition typically challenging for maintaining performance at shorter lengths, the LongRoPE-2048k models outperform state-of-the-art baselines within 256k context length. [p. 6]

**Table 5** (p. 7): Proof-pile perplexity of models with various positional interpolation methods. ft: the context window size used in fine-tuning. Even with a context window 16x longer than current long-context models, the LongRoPE models also outperform them within 256k context length.

| Base LLM | Model Name | Context Window | Extension Method | 4096 | 8192 | 32768 | 65536 | 98304 | 131072 | 262144 |
|---|---|---|---|---|---|---|---|---|---|---|
| LLaMA2-7B | LLaMA2-7B | 4k | - | 3.58 | >10^4 | >10^4 | >10^4 | >10^4 | >10^4 | >10^4 |
| LLaMA2-7B | Together | 32k | PI | 3.69 | 3.50 | 2.64 | >10^2 | >10^3 | >10^4 | >10^4 |
| LLaMA2-7B | LongLoRA | 100k | PI | 3.83 | 3.62 | 2.68 | 2.44 | 2.33 | 9.89 | >10^3 |
| LLaMA2-7B | Code LLaMA | 100k | NTK | 3.95 | 3.71 | 2.74 | 2.55 | 2.54 | 2.71 | 49.33 |
| LLaMA2-7B | YaRN (s=16) | 64k | YaRN | 3.69 | 3.51 | 2.65 | 2.42 | >10^1 | >10^1 | >10^4 |
| LLaMA2-7B | YaRN (s=32) | 128k | YaRN | 3.75 | 3.56 | 2.70 | 2.45 | 2.36 | 2.37 | 99.64 |
| LLaMA2-7B | **LongRoPE-2048k (ft=128k)** | **2048k** | **LongRoPE** | **3.71** | **3.50** | **2.60** | **2.36** | **2.27** | **2.26** | **1.88** |
| LLaMA2-7B | **LongRoPE-2048k (ft=256k)** | **2048k** | **LongRoPE** | **3.85** | **3.65** | **2.63** | **2.38** | **2.28** | **2.26** | **1.87** |
| Mistral-7B | Mistral v0.1 | 8k | - | 3.09 | 2.96 | >10^2 | >10^3 | >10^3 | >10^3 | >10^4 |
| Mistral-7B | YaRN (s=8) | 64k | YaRN | 3.18 | 3.04 | 2.37 | 2.20 | 10.39 | 57.4 | >10^4 |
| Mistral-7B | YaRN (s=16) | 128k | YaRN | 3.21 | 3.08 | 2.41 | 2.24 | 2.18 | 2.19 | 4.91 |
| Mistral-7B | **LongRoPE-2048k (ft=128k)** | **2048k** | **LongRoPE** | **3.20** | **3.04** | **2.36** | **2.18** | **2.13** | **2.13** | **1.85** |
| Mistral-7B | **LongRoPE-2048k (ft=256k)** | **2048k** | **LongRoPE** | **3.20** | **3.04** | **2.36** | **2.18** | **2.13** | **2.14** | **1.84** |

**Table 7** (p. 7): Perplexity evaluation within 256k context length on PG19.

| Base LLM | Model Name | Context Window | Extension Method | 8k | 64k | 128k |
|---|---|---|---|---|---|---|
| LLaMA2-7B | LongLoRA | 100k | PI | 7.16 | 6.81 | >10^7 |
| LLaMA2-7B | Code LLaMA | 100k | NTK | 7.58 | 8.92 | 16.80 |
| LLaMA2-7B | LongRoPE-2048k (ft=128k) | 2048k | LongRoPE | 6.98 | **6.59** | **6.35** |
| LLaMA2-7B | LongRoPE-2048k (ft=256k) | 2048k | LongRoPE | 7.37 | **6.64** | **6.31** |
| Mistral-7B | YaRN-64k | 64k | YaRN | 7.12 | 7.17 | >10^7 |
| Mistral-7B | YaRN-128k | 128k | YaRN | 7.30 | 7.53 | 7.32 |
| Mistral-7B | LongRoPE-2048k (ft=128k) | 2048k | LongRoPE | 7.13 | **7.01** | **7.02** |
| Mistral-7B | LongRoPE-2048k (ft=256k) | 2048k | LongRoPE | **7.10** | **6.98** | **7.13** |

### Long sequence language modeling beyond 2000k [p. 6-7]

To evaluate the effectiveness on extremely long documents, the Books3 (Gao et al., 2020) dataset is used. For evaluation efficiency, 20 books are randomly selected, each exceeding 2048k in length, and a sliding window of 256k is used. [p. 6]

As shown in Table 6, LongRoPE successfully extends LLaMA2-7B and Mistral-7B's context window to 2048k, while also achieving perplexity comparable or superior to baselines within shorter lengths of 8k-128k. Notable performance differences between the 2048k LLaMA2 and Mistral are observed. Mistral outperforms baselines at shorter lengths, but perplexity exceeds 7 beyond 256k. LLaMA2 performance aligns with expectations: the perplexity decreases gratefully with longer contexts, with marginal increases at 1024k and 2048k. Moreover, on LLaMA2, LongRoPE-2048k performs better at a fine-tuning length of 256k over 128k, due to the smaller secondary extension ratio (i.e., 8x vs. 16x). In contrast, Mistral performs better at fine-tuning window size of 128k. The main reason is that for Mistral's 128k and 256k fine-tuning, the authors follow YaRN's setting to use a 16k training length, which affects Mistral's ability to further extend context window after fine-tuning. [p. 6-7]

**Table 6** (p. 7): Perplexity evaluation on Books3 dataset. Without additional fine-tuning, the LongRoPE-2048k models, with a training context window size of 128k and 256k, effectively scale to an extremely long context size of 2048k. 1k=1024 tokens.

| Base LLM | Model Name | Context Window | Extension Method | 8k | 16k | 32k | 64k | 128k | 256k | 512k | 1024k | 2048k |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LLaMA2-7B | LongLoRA | 100k | PI | 6.99 | 6.80 | 6.66 | 6.59 | 20.57 | 246.45 | >10^5 | >10^4 | >10^4 |
| LLaMA2-7B | Code LLaMA | 100k | NTK | 7.68 | 7.49 | 7.38 | 7.88 | 9.80 | 98.30 | >10^3 | >10^4 | >10^4 |
| LLaMA2-7B | YaRN (s=16) | 64k | YaRN | **6.33** | **6.20** | **6.11** | **6.06** | >10^4 | >10^4 | >10^4 | >10^4 | >10^4 |
| LLaMA2-7B | YaRN (s=32) | 128k | YaRN | 6.38 | 6.25 | 6.16 | 6.11 | **6.12** | >10^4 | >10^4 | >10^4 | >10^4 |
| LLaMA2-7B | **LongRoPE-2048k (ft=128k)** | **2048k** | **LongRoPE** | 6.55 | 6.35 | 6.24 | 6.18 | 6.17 | **6.17** | **6.36** | **6.83** | **7.80** |
| LLaMA2-7B | **LongRoPE-2048k (ft=256k)** | **2048k** | **LongRoPE** | 6.81 | 6.66 | 6.31 | 6.27 | 6.21 | **6.17** | **6.17** | **6.35** | **7.08** |
| Mistral-7B | Mistral v0.1 | 8k | - | 6.32 | 66.61 | >10^2 | >10^3 | >10^5 | >10^5 | - | - | - |
| Mistral-7B | YaRN (s=16) | 64k | YaRN | **6.59** | **6.48** | **6.42** | **6.45** | 104.15 | 7221.20 | >10^3 | >10^4 | >10^4 |
| Mistral-7B | YaRN (s=32) | 128k | YaRN | 6.70 | 6.63 | 6.65 | 6.72 | 6.85 | 99.90 | >10^3 | >10^4 | >10^4 |
| Mistral-7B | **LongRoPE-2048k (ft=128k)** | **2048k** | **LongRoPE** | 6.64 | **6.48** | **6.39** | **6.45** | **6.64** | **7.08** | **7.71** | **8.93** | **12.78** |
| Mistral-7B | **LongRoPE-2048k (ft=256k)** | **2048k** | **LongRoPE** | 6.63 | **6.48** | **6.38** | **6.43** | **6.68** | **7.15** | **7.98** | **9.42** | **13.71** |

### Passkey retrieval [p. 7]

The effective context window size in generation tasks is studied using a synthetic evaluation task of passkey retrieval proposed by (Mohtashami & Jaggi, 2023). In this task, the model is asked to retrieve a random passkey (i.e., a five-digit number) hidden in a long document. The prompt template is detailed in appendix. 10 iterations of the passkey retrieval task are performed with the passkey placed at a random location uniformly distributed across the evaluation context length. [p. 7]

Fig. 4 shows the retrieval accuracy comparison with baselines. Existing models' accuracy rapidly drops to 0 beyond 128k. In contrast, despite the very challenging task of retrieving a passkey from million-level tokens, LongRoPE-LLaMA2-2048k (ft=256k) manages to maintain a high retrieval accuracy (>=90%) from 4k to 2048k. LongRoPE-Mistral-2048k (ft=128k) keeps 100% accuracy up to 1800k, dropping to 60% at 2048k, aligning with expectations from Table 6, where the perplexity slightly increases at 2048k. [p. 7]

**Figure 4** (p. 7): "Passkey retrieval accuracy of long-context LLMs. It showcases the remarkable ability of our models to accurately retrieve a passkey from a vast pool of million-level tokens."
- X-axis: evaluation context length (4k to 2048k on a log-like scale)
- Y-axis: retrieval accuracy (0% to 100%)
- Lines shown: LLaMA2-7B, Mistral-7B, LongLoRA-100k, CodeLLaMA-100k, YaRN-LLaMA-128k, YaRN-Mistral-128k, LongRoPE-LLaMA2-2048k, LongRoPE-Mistral-2048k
- Key data points: Baseline models (LongLoRA, CodeLLaMA, YaRN variants) drop to 0% accuracy beyond 128k. LongRoPE-LLaMA2-2048k maintains ~80-100% accuracy through 2048k. LongRoPE-Mistral-2048k maintains 100% up to 1800k, drops to ~60% at 2048k.

### Standard benchmarks within original context window [p. 7-8]

LongRoPE-2048k models are evaluated on the original context window using Hugging Face Open LLM Leaderboard (Face, 2024) in zero-shot and few-shot settings. The benchmarks used: 25-shot ARC-Challenge (Clark et al., 2018), 10-shot HellaSwag (Zellers et al., 2019), 5-shot MMLU (Hendrycks et al., 2020), and 0-shot TruthfulQA (Lin et al., 2021). [p. 7]

**Table 8** (p. 8): Comparison of long-context LLMs with original LLaMA2 and Mistral on the Hugging Face Open LLM benchmark.

**(a) LLaMA2-7B with extended context window**

| Model | Context Window | ARC-c | HellaSwag | MMLU | TruthfulQA |
|---|---|---|---|---|---|
| Original LLaMA2-7B | 4k | 53.1 | 78.6 | 46.6 | 39.0 |
| Together | 32k | 47.6 | 76.1 | 43.3 | 39.2 |
| Code LLaMA | 100k | 42.4 | 64.8 | 40.1 | 37.1 |
| YaRN (s=16) | 64k | 52.4 | **78.7** | 42.4 | 38.2 |
| YaRN (s=32) | 128k | 52.2 | 78.5 | 41.8 | 37.4 |
| LongRoPE-2048k (ft=128k) | 2048k | **52.9** | 76.5 | **43.4** | **38.8** |
| LongRoPE-2048k (ft=256k) | 2048k | 51.0 | 75.3 | 39.6 | 37.3 |

**(b) Mistral-7B with extended context window**

| Model | Context Window | ARC-c | HellaSwag | MMLU | TruthfulQA |
|---|---|---|---|---|---|
| Original Mistral-7B | 8k | 60.6 | 83.2 | 63.6 | 42.6 |
| MistralLite (Amazon, 2023) | 16k | 59.2 | **81.6** | 50.4 | 38.3 |
| YaRN (s=16) | 64k | **59.3** | 81.3 | 61.3 | 42.5 |
| YaRN (s=32) | 128k | 59.0 | 80.5 | 60.5 | 42.1 |
| LongRoPE-2048k (ft=128k) | 2048k | 59.0 | 81.2 | **61.3** | **43.1** |
| LongRoPE-2048k (ft=256k) | 2048k | 59.2 | 80.9 | 61.1 | 42.2 |

As Table 8 shows, the models achieve comparable results on the original benchmark designed for a smaller context window, and even outperform the original Mistral on TruthfulQA by +0.5%. LongRoPE-LLaMA2-2048k, fine-tuned at 256k, shows slightly more performance degradation, but remains within reasonable ranges for most tasks. [p. 8]

## 4.3. Ablation Results [p. 8]

### Effectiveness of the second positional interpolation [p. 8]

In the progressive extension strategy, the search algorithm conducts a second non-uniform positional interpolation on the fine-tuned extended LLMs. Effectiveness is validated by running experiments on the fine-tuned LLaMA2-256k model, extending it to 512k, 1024k, and 2048k using PI and YaRN. As Table 9 shows, the non-uniform positional interpolation sustains a consistent level of perplexity. In contrast, the perplexity under PI and YaRN quickly increases with the extension ratio. [p. 8]

**Table 9** (p. 8): Books3 perplexity comparison of extending LLaMA2-256k via different secondary positional interpolation methods.

| Model Name | Extension Method | 512k | 1024k | 2048k |
|---|---|---|---|---|
| LLaMA2-7B (ft=256k) | PI | 6.60 | 8.73 | 20.17 |
| LLaMA2-7B (ft=256k) | YaRN | 6.39 | 6.79 | 8.27 |
| LLaMA2-7B (ft=256k) | **LongRoPE** | **6.17** | **6.35** | **7.08** |

### Effectiveness of recovery at shorter context lengths [p. 8]

To mitigate performance loss at shorter context lengths, the RoPE factors for LongRoPE-2048k are readjusted via the search algorithm. Specifically, the maximum allowable scale factors for the search are decreased to encourage less interpolation at short 4k and 8k lengths. Table 10 shows the perplexity comparison of LongRoPE-LLaMA2-2048k on Proof-pile at 4k and 8k lengths, along with the average LLM benchmark accuracy. The results clearly demonstrate a significant performance improvement at short context lengths. [p. 8]

**Table 10** (p. 8): Ablation study on LongRoPE readjustment for performance recovery at shorter context lengths.

| FT Model | With Recovery | Proof-Pile Perplexity 4k | Proof-Pile Perplexity 8k | LLM Benchmark Avg. Accuracy |
|---|---|---|---|---|
| LLaMA2-7B-2048k (ft=128k) | x | 4.16 | 3.72 | 49.3 |
| LLaMA2-7B-2048k (ft=128k) | checkmark | **3.71** | **3.50** | **52.9** |
| LLaMA2-7B-2048k (ft=256k) | x | 4.51 | 3.82 | 47.9 |
| LLaMA2-7B-2048k (ft=256k) | checkmark | **3.85** | **3.65** | **50.8** |

### Analysis on the two forms of non-uniformities [p. 8]

The two non-uniformities are ablated to determine each part's contribution to the performance. Two experiments are set up: (i) extending LLaMA2-7B to short 16k and 32k using different methods -- PI, searching for RoPE dimension only, and searching for both non-uniformities; (ii) extending the fine-tuned 256k-length LLaMA2 to 2048k following the same procedure. The perplexity is evaluated without fine-tuning. [p. 8]

As Table 11 shows, non-uniformity in RoPE dimension significantly reduces perplexity compared to PI's linear interpolation. Non-uniformity in token position clearly improves performance at 16k and 32k lengths but does not show the same impact at 2048k, possibly due to the extremely long length. Preserving only the initial tokens without interpolation becomes non-useful, and the authors leave this as future work. [p. 8]

**Table 11** (p. 8): Ablation study on the two forms of non-uniformities.

| Methods | LLaMA2-7B PG19 Perplexity 16k | LLaMA2-7B PG19 Perplexity 32k | LLaMA2-7B (ft=256k) Books3 Perplexity 2048k |
|---|---|---|---|
| Linear interpolation (PI) | 14.88 | 136.30 | 20.17 |
| RoPE dim (Ours) | 7.28 | 13.00 | 7.08 |
| RoPE dim+Start tokens (Ours) | **7.22** | **11.51** | **7.08** |
