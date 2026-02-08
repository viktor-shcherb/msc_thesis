# J Additional Evaluations [p. 21-23]

[p. 21]

## J.1 Further details on NLP tasks

We evaluate on the following tasks:

- **ARC** (Clark et al., 2018): A dataset designed for multiple-choice question answering, encompassing science exam questions ranging from third grade to ninth grade. It has Easy and Challenge subsets that we report results on separately.

- **BoolQ** (Clark et al., 2019): A binary yes/no question answering benchmark.

- **COPA** (Roemmele et al., 2018): A dataset to evaluate achievement in open-domain commonsense causal reasoning.

- **HeadQA** (Vilares and Gomez-Rodriguez, 2019): A benchmark consisting of graduate-level questions encompassing various fields such as medicine, nursing, biology, chemistry, psychology, and pharmacology.

- **HellaSwag** (Zellers et al., 2019): A novel benchmark for commonsense Natural Language Inference (NLI) which is built by adversarial filtering against transformer models.

- **LAMBADA** (Paperno et al., 2016): A benchmark dataset that evaluates the model's contextual reasoning and language comprehension abilities by presenting context-target pairs, where the objective is to predict the most probable target token. We follow standard practice and use the untokenized version created by OpenAI (Brown et al., 2020).

- **OpenBookQA** (Mihaylov et al., 2018): A QA dataset to evaluate human comprehension of a subject by incorporating open book facts, scientific knowledge, and perceptual common sense, drawing inspiration from open book exams.

- **PIQA** (Bisk et al., 2020): A benchmark for the task of physical common sense reasoning, which consists of a binary choice task that can be better understood as a set of two pairs, namely (Goal, Solution).

- **ReCoRD** (Zhang et al., 2018): A benchmark for evaluating commonsense reasoning in reading comprehension by generating queries from CNN/Daily Mail news articles and requiring text span answers from corresponding summarizing passages.

- **SciQ** (Johannes Welbl Nelson F. Liu, 2017): A multiple-choice QA dataset which was created using an innovative approach to gather well-crafted multiple-choice questions that are focused on a specific domain.

- **Winogrande** (Zellers et al., 2020): A dataset designed to evaluate the acquisition of common sense reasoning by neural language models, aiming to determine whether we are accurately assessing the true capabilities of machine common sense.

**Figure 12** (p. 22): "Zero-Shot Performance of RWKV on common language modeling evaluation benchmarks."
- A 4x3 grid of 12 subplots, one for each benchmark: (a) ARC (Challenge), (b) ARC (Easy), (c) BoolQ, (d) COPA, (e) HeadQA, (f) HellaSwag, (g) LAMBADA (OpenAI), (h) OpenBookQA, (i) PIQA, (j) ReCoRD, (k) SciQ, (l) Winogrande.
- Each subplot shows Accuracy (y-axis, 0-100) vs. Compute in exaFLOP (x-axis, log scale, roughly 10^2 to 10^4).
- Four model families are plotted: BLOOM (blue x markers), Pythia (orange triangles), OPT (green plus markers), RWKV (blue squares).
- General trend: all model families improve with compute. RWKV tracks competitively with the transformer baselines across most benchmarks. On some benchmarks (e.g., PIQA, SciQ), RWKV performs on par or slightly above; on others (e.g., LAMBADA, HellaSwag), RWKV is competitive but occasionally slightly below the best transformer at the highest compute points.

---
[p. 23 continued]

## J.2 Evaluation on Long Range Arena

The Long-Range Arena (LRA) benchmark (Tay et al., 2021) is designed to assess the performance of models in handling lengthy context situations. It includes a collection of tasks with sequences ranging from 1,000 to 16,000 tokens, covering various types of data like text, natural language, synthetic images, and mathematical expressions. Other models' performances are directly cited from Gu et al. (2022); Alam et al. (2023). [p. 23]

**Table 4:** Evaluation on Long Range Arena. Other models reported in the literature (Gu et al., 2022; Alam et al., 2023). **Bolded** values are the best.

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Path-X | Avg |
|---|---|---|---|---|---|---|---|
| Transformer | 36.37 | 64.27 | 57.46 | 42.44 | 71.40 | X | 53.66 |
| Reformer | 37.27 | 56.10 | 53.40 | 38.07 | 68.50 | X | 50.56 |
| BigBird | 36.05 | 64.02 | 59.29 | 40.83 | 74.87 | X | 54.17 |
| Linear Trans. | 16.13 | 65.90 | 53.09 | 42.34 | 75.30 | X | 50.46 |
| Performer | 18.01 | 65.40 | 53.82 | 42.77 | 77.05 | X | 51.18 |
| FNet | 35.33 | 65.11 | 59.61 | 38.67 | 77.80 | X | 54.42 |
| Nystromformer | 37.15 | 65.52 | 79.56 | 41.58 | 70.94 | X | 57.46 |
| Luna-256 | 37.25 | 64.57 | 79.29 | 47.38 | 77.72 | X | 59.37 |
| Hrrformer | 39.98 | 65.38 | 76.15 | 50.45 | 72.17 | X | 60.83 |
| S4 | **59.60** | **86.82** | **90.90** | **88.65** | **94.20** | **96.35** | **86.09** |
| RWKV | 55.88 | 86.04 | 88.34 | 70.53 | 58.42 | X | 72.07 |

The results show that RWKV performs second only to the S4 model in five datasets. While RWKV substantially underperforms S4 on Image, Pathfinder, and Path-X, on the problems related to natural language and computer code processing RWKV performs on par with S4 or nearly so. [p. 23]

## J.3 Enwik8 Perplexity

We also evaluate our model in terms of perplexity on the Enwik8 dataset. Baseline comparisons are made with Reformer (Kitaev et al., 2020), Synthesizer (Tay et al., 2020) (the best performing dense version), Linear Transformer (Katharopoulos et al., 2020), Performer (Choromanski et al., 2020). $L$, $d$, and $T$ denote the number of blocks (network depth), dimension of features, and sequence length, respectively. Both Linear Transformer and Performer are implemented with customized CUDA kernels (github.com/idiap/fast-transformers), and all other models are implemented in native Pytorch. ^1 No weight decay nor dropout was used. ^2 Trained with AdamW and weight decay set to 0.1, dropout of 0.1, batch size of 16, and initial learning rate of 6e-4. [p. 23]

**Table 5:** Enwik8 results, measured in bits per character (bpc).

| Method | L | d | T | Train bpc | Test bpc | Time Complexity | Space Complexity |
|---|---|---|---|---|---|---|---|
| Transformer | 12 | 512 | 1024 | 0.977 | 1.137 | $O(T^2 d)$ | $O(T^2 + Td)$ |
| Transformer | 24 | 256 | 1024 | 1.039 | 1.130 | $O(T^2 d)$ | $O(T^2 + Td)$ |
| Reformer | 12 | 512 | 1024 | 1.040 | 1.195 | $O(T \log T \cdot d)$ | $O(T \log T + Td)$ |
| Synthesizer | 12 | 512 | 1024 | 0.994 | 1.298 | $O(T^2 d)$ | $O(T^2 + Td)$ |
| Linear Transformer | 12 | 512 | 1024 | 0.981 | 1.207 | $O(Td^2)$ | $O(Td + d^2)$ |
| Performer | 12 | 512 | 1024 | 1.002 | 1.199 | $O(Td^2 \log d)$ | $O(Td \log d + d^2 \log d)$ |
| AFT-simple | 12 | 512 | 1024 | 1.046 | 1.209 | $O(Td)$ | $O(Td)$ |
| RWKV-RNN^1 | 6 | 512 | 1024 | 0.720 | - | $O(Td)$ | $O(d)$ |
| RWKV-RNN^2 | 12 | 512 | 1024 | 1.010 | 1.178 | $O(Td)$ | $O(d)$ |

RWKV-RNN^1 (6 layers, no regularization) achieves the lowest training bpc (0.720) but no test bpc is reported (likely overfitting). RWKV-RNN^2 (12 layers, with regularization) achieves test bpc of 1.178, which is competitive with the Transformer baselines (best Transformer test bpc = 1.130 with 24 layers) while having linear time complexity $O(Td)$ and constant space complexity $O(d)$. [p. 23]
