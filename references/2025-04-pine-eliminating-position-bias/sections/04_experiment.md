# 4 EXPERIMENT [p. 7]

The experiments aim to show PINE can improve model performance across diverse tasks and have superior performance than other approaches [p. 7].

## 4.1 Settings [p. 7]

### Task Selection

Four tasks are selected that pose position bias [p. 7]:
- **LM-as-a-judge** (Zheng et al., 2024b) that prompts LMs to select a better response out of two options [p. 7]
- **Retrieval-augmented question-answering** (Liu et al., 2024) that asks LMs to answer questions based on retrieved documents [p. 7]
- **Molecule generation** based on provided properties (Ramakrishnan et al., 2014) [p. 7]
- **Math reasoning** where conditions can be swapped in several given conditions (Chen et al., 2024b) [p. 7]

Temperature 0 is followed to avoid variance [p. 7]. The authors follow previous work (Liu et al., 2024, Lambert et al., 2024a) and use temperature 0 in to avoid variance [p. 7].

### LM-as-a-judge

The method is benchmarked on 23 datasets in the RewardBench³ (Lambert et al., 2024b) that can be categorized into four types: Chat, Chat-Hard, Safety, and Reasoning [p. 7]. The official data split, prompts, and evaluation code are used to avoid variance for reproducibility [p. 7]. LLaMa-3-Instruct models (AI, 2024) and Qwen-1.5-Chat models (Bai et al., 2023) are used for experiments [p. 7]. To show how positions affect results, four scenarios are presented with the ground-truth response positioned at first, second, or shuffled, and PINE results (which yield the same results for all three scenarios above) [p. 7].

### Retrieval-augmented QA

The settings and prompts, data, and evaluation scripts of (Liu et al., 2024)⁴ are followed [p. 7]. Only one of the retrieved documents (10 or 20 in total) contains the ground-truth answer for the given question [p. 7]. All prompts are listed in Appendix E [p. 7]. LLaMa-3-70B-Instruct model (AI, 2024) is used for experiment [p. 7]. To show how positions affect results, four scenarios are presented: the ground-truth document is positioned at the beginning, middle, last, or shuffled, and PINE results (which yield the same results for all scenarios above) [p. 7].

### Molecule Generation and Math reasoning

Two bonus experiments are conducted [p. 7]:
- **Molecule generation** based on given properties (property positions can be swapped) [p. 7]
- **Math reasoning** where conditions can be swapped [p. 7]

More details of the four tasks can be found in Appendix E [p. 7]. Qualitative examples of the four tasks can be found in Appendix F [p. 7].

### Baselines

The goal of PINE is to eliminate position bias during inference mechanically [p. 7]. Therefore, methods that have the same goal are chosen as baselines [p. 7]:
1. **Vanilla inference** [p. 7]
2. **Vanilla inference with no inter-document attention** (NIA for short, i.e., the middle figure in Figure 3) [p. 7]. The latter documents will have no knowledge about the former ones [p. 7].
3. **Parallel Context Window (PCW, the rightmost in Figure 3)** (Ratner et al., 2023). PCW extends the baseline (2) by manipulating positions of documents to allow all documents share the same positions [p. 7]. PCW allows all documents to share the same positions [p. 7].
4. **Structured Prompting (SP, a variant version of PCW)** (Hao et al., 2022). SP extends (3) by lowering attentions between decoded tokens and input documents to 1/N to solve the perplexity exploding problem in PCW [p. 7]. Similar to the proof in Section 3.3, we can know that (1) and (2) are not inter-document position-invariant, whereas (3) and (4) are [p. 7].

Beyond these methods, two other debiasing baselines are introduced: permutation (Zheng et al., 2024a) and calibration (Zhao et al., 2021) [p. 7].

## 4.2 Results on LM-as-a-Judge [p. 7-8]

### Position bias exists across different models and sizes

Position bias is first analyzed with different models (Appendix C) [p. 7]. Position bias is quite common in RewardBench, and can be up to 48.0% [p. 7]. Larger models have less position bias, however, the position bias could still on average affect up to 10% data [p. 7-8].

**Table 1** (p. 8): "Main results of RewardBench. Vanilla denotes the normal inference. (GT at A) means the ground truth chosen response is presented at the first, and (GT at B) indicates the second. For the 72B model, we additionally benchmark and compare with the Qwen 2.5 model. PINE consistently improves LM's performance across different models and sizes and is particularly useful when assessing reasoning pairs."

| Method | Llama-3-Instruct 8B | Llama-3-Instruct 70B | 1.8B | 4B | 7B | Qwen-1.5-Chat 32B | Qwen-1.5-Chat 72B / 72B (Qwen 2.5) | 110B |
|--------|---------|---------|------|----|----|-------|------------|------|
| **RewardBench (Full set)** | | | | | | | | |
| Vanilla (GT at A) | 67.5 | 78.0 | 36.3 | 29.5 | 61.4 | 74.2 | 79.6 / 87.2 | 87.2 |
| Vanilla (GT at B) | 66.3 | 76.5 | 66.2 | 76.6 | 59.6 | 74.8 | 69.5 / 80.5 | 75.7 |
| Vanilla (Shuffle) | 64.8 | 76.0 | 50.3 | 53.1 | 60.9 | 72.8 | 72.8 / 83.4 | 81.1 |
| **PINE** | **66.7**₊₁.₉ | **77.4**₊₁.₄ | **52.9**₊₂.₆ | **58.2**₊₅.₁ | **61.5**₊₀.₆ | **74.8**₊₂.₀ | **71.8**₋₁.₁ / **84.5**₊₁.₁ | **82.9**₊₁.₇ |
| **RewardBench (Reasoning set)** | | | | | | | | |
| Vanilla (GT at A) | 80.3 | 87.8 | 43.3 | 42.8 | 62.1 | 78.3 | 83.0 / 93.7 | 90.0 |
| Vanilla (GT at B) | 66.0 | 80.3 | 57.2 | 62.3 | 54.3 | 73.6 | 68.7 / 76.0 | 73.0 |
| Vanilla (Shuffle) | 65.3 | 78.9 | 48.4 | 54.1 | 59.3 | 66.8 | 68.2 / 85.5 | 78.0 |
| **PINE** | **73.4**₊₈.₁ | **87.6**₊₈.₇ | **60.1**₊₁₁.₇ | **61.0**₊₆.₉ | **63.0**₊₃.₇ | **76.7**₊₉.₉ | **69.0**₊₀.₈ / **91.3**₊₅.₈ | **86.2**₊₈.₂ |

**Table 2** (p. 8): "Baseline performance on RewardBench. PINE achieves superior performance to baseline models, performing 4.8% and 4.7% better than the best performed baseline on two models."

| Method | LLaMa-3-8B-Instruct<br/>Reasoning | LLaMa-3-8B-Instruct<br/>Full Set | Qwen1.5-7B-Chat<br/>Reasoning | Qwen1.5-7B-Chat<br/>Full Set |
|--------|-----------|----------|-----------|----------|
| NIA (GT at A) | 43.7 | 56.3 | 60.7 | 61.3 |
| NIA (GT at B) | 66.7 | 65.8 | 44.1 | 52.2 |
| NIA | 55.9 | 61.9 | 51.4 | 56.8 |
| PCW | 56.5 | 61.7 | 53.4 | 55.2 |
| SP | 55.4 | 60.8 | 52.4 | 55.4 |
| **PINE** | **73.4**₊₁₆.₉ | **66.7**₊₄.₈ | **63.0**₊₉.₆ | **61.5**₊₄.₇ |

### PINE consistently improve model performance across models and sizes

Table 1 shows the main results on RewardBench [p. 8]. Experiments are conducted with Llama-3 and Qwen-1.5 across different model sizes [p. 8]. The position of the ground truth chosen response is randomly shuffled [p. 8]. Therefore, the accuracy of the random guess method is expected to be 50% [p. 8]. First, the first two rows reveal that larger models tend to have a primacy bias, whereas smaller models tend to have a recency bias [p. 8]. By comparing the last two rows of each model size, it is concluded that across different sizes perform better with the help of PINE by eliminating position bias [p. 8]. The only exception is the Qwen-1.5-72B-Chat model [p. 8]. The authors suspect this model is not well-trained since Qwen-1.5-32B-Chat performs the same as the 72B model in vanilla inference, despite half of the model size. Qwen 2 report (Yang et al., 2024) also shows that the Qwen 1.5 72B model performs even worse than 32B in reasoning [p. 8]. Moreover, Table 1 shows that Qwen 2.5 72B can obtain consistent performance gains [p. 8]. Overall, PINE improves performance from a statistical perspective and makes models more reliable when as evaluators [p. 8]. Full results are shown in Appendix D [p. 8].

### PINE is extremely useful when assessing reasoning problems in RewardBench

PINE consistently improves model performance on the "reasoning" subset by a large margin: from 8 to 10 percentage points in most cases [p. 8]. Specifically, LlaMa-3 Instruct 70B was originally ranked 22nd generative model in the reasoning subset of RewardBench. With PINE, it achieves the 7th rank (87.6%), **outperforming GPT-4-0125-preview (the previous 8th rank, 86.9%), GPT-4o-2024-08-06 (the previous 9th rank, 86.6%)**, and **Llama-3.1-405B-Instruct-Turbo (the previous 7th rank, 87.1%)**⁶ [p. 8].

### PINE performs better than baseline models that adopt different attention masks

PINE is then compared with baseline models mentioned in Section 4.1 on Llama-3-8B-Instruct and Qwen1.5-7B-Chat model [p. 8-9]. They adopt a different attention mask: masking inter-document attention instead of making them bi-directional [p. 9]. Since NIA is not inter-document position-invariant, two extreme cases are also applied to NIA with two extreme cases: the ground truth chosen response is always in the first or second [p. 9].

⁶Results are provided by the official leaderboard (as of Sep 17, 2024): https://huggingface.co/spaces/allenai/reward-bench

---
[p. 9 continued]

place [p. 9]. Results on Table 2 show that PINE achieves the best performance and largely outperforms the best baselines by ∼ 5%, and outperforms NIA even if NIA is placed in the extreme case [p. 9]. On the reasoning subset, this performance gap becomes even greater [p. 9]. The results reveal that masking inter-document attention mask is much less effective than bidirectional inter-document attention mask applied in PINE [p. 9].

### PINE performs better than permutation and calibration methods

Another two widely used debiasing methods are permutation (Zheng et al., 2024a) and calibration (Zhao et al., 2021) [p. 9]. They are usually used in the logit-based evaluation or single-token generation [p. 9]. Their effectiveness in the open-ended generation is less explored [p. 9]. In the experiments, calibration methods are found to generate rubbish responses, which the authors believe is due to the strong assumption in (Zhao et al., 2021): uniform distribution of all tokens in the generation task [p. 9]. For the permutation methods, LLama-3-8B-Instruct has 69.0% and 65.9% accuracy, Qwen1.5-7B-Chat has 58.2% and 61.3% accuracy on the reasoning set and full set respectively, all underperforming PINE (numbers reported in Table 2) [p. 9].

## 4.3 Results on Retrieval-Augmented Question-Answering [p. 9]

### PINE performs better than baselines, on-par with vanilla inference on average while not being affected by the worst case

Models tend to produce better when the gold-standard document is at the beginning and the end of all documents in retrieval-augmented question-answers [p. 9]. Figure 4(a) shows the results on LLaMa-3-70B-Instruct when 10 or 20 documents were presented [p. 9]. First, it is easy to conclude that all baselines are much worse than PINE (the pink line), which is consistent to the previous experiment [p. 9]. Second, PINE achieves on-par performance on average compared with vanilla inference while being inter-document position invariant [p. 9]. Specifically, PINE is slightly better/worse than vanilla inference with the gap +1.2/-2.0 when there are 10 and 20 documents in total [p. 9]. The authors hypothesize that the slight performance drop of PINE for the 20 document setting is due to the performance drop of document importance score computation in PINE when presented with many documents [p. 9]. However, PINE is position-invariant, therefore PINE is not be affected by the worst case (the bottom of blue solid curves) [p. 9]. Third, the height generally becomes smaller between blue and brown solid lines in Figure 4(a), and between the blue one and pink line in Figure 4(b) when the gold-standard document position increases, reflecting the causal attention generally prefers distant content, which is consistent to the hypothesis in Section 1 [p. 9]. The brown line in Figure 4(a) and red line in Figure 4(b) generally reflect recency bias instead of primacy bias with RoPE, which is consistent to previous works (Su et al., 2024, Peysakhovich & Lerer, 2023) [p. 9].

**Figure 4** (p. 9): "The results of retrieval-augmented QA on Llama-3-70B-Instruct. Dashed lines indicate that the method is either inter-document position-invariant or the result is obtained on the order-shuffled data (denoted in the legend). (a) shows results of PINE against baselines. (b) shows results of different designs of PINE."

Description: Two-panel line chart
- Key elements: (a) shows 6 different methods plotted against position of document with the answer (x-axis) and accuracy (y-axis). Two separate plots for total document counts of 10 and 20. (b) shows PINE with/without re-assignment and PINE (reverse/normal) methods for total document count of 10.
- Notable patterns: In (a), PINE maintains consistent performance around 74-75% regardless of answer position (shown as horizontal dashed pink line). Vanilla and NIA show declining performance as answer position moves further from the beginning. In (b), PINE with re-assignment outperforms PINE without re-assignment, and normal ordering outperforms reverse ordering.
- Supports claim: Demonstrates PINE's position-invariance and superior performance compared to baselines in retrieval-augmented QA tasks.

### PINE performs better than other position assignment methods

Retrieval-augmented QA experiments are extended with the two mentioned alternative position assignment methods, and the results are presented in Figure 4(b) [p. 9-10]. The figure tells that PINE is slightly better than PINE without position re-assignment on average [p. 10]. The gap becomes larger when 20 documents are presented: +1.5 [p. 10]. Position re-assignment reversely has relatively worse results, showing that PINE is a better design choice, which is consistent to the intuitive explanation in Section 3.4 [p. 10]. Although position re-assignment seems only to bring less gains than bidirectional attention mask, it is required to complete the proof that PINE can **eliminate** the position bias [p. 10]. Therefore, PINE without position re-assignment may suffice if one does not aim to eliminate the position bias and cares more about efficiency (no extra O(nk log k) sorting cost) [p. 10].

## 4.4 Results on Molecule Generation and Math Reasoning [p. 10]

### PINE improves model performance on 5 out of 6 criteria in molecule generation

Table 3 shows the results of molecule generation [p. 10]. The consistent gain in 5 out 6 criteria shows the effectiveness of PINE [p. 10].

**Table 3** (p. 10): "The result of molecule generation on QM9 dataset. PINE improves model performance in 5 out of 6 criteria."

| Model | α | ϵ<sub>HOMO</sub> | ϵ<sub>LUMO</sub> | Δϵ | μ | C<sub>v</sub> |
|-------|---|------|------|----|----|-------|
| LLama | 6.3997 | 103.93 | 53.4 | 99.13 | 3.4112 | 4.3785 |
| Llama + PINE | **6.3702** | **102.15** | **53.09** | **98.27** | 3.4917 | **4.2886** |

### PINE improves math reasoning capabilities

Figure 5 shows the results of Qwen1.5 models on R-GSM dataset [p. 10]. It can be shown that PINE outperforms vanilla inference for both small 7B models and large 110B models [p. 10].

**Figure 5** (p. 10): "Math reasoning results of Qwen1.5 series on R-GSM subset. PINE improves the reasoning accuracy by 12.6% and 5.3% with 7B and 110B models respectively compared with vanilla inference."

Description: Bar chart comparing Vanilla vs PINE performance
- Key elements: Two groups of bars (7B and 110B models), blue bars for Vanilla, teal bars for PINE. Y-axis shows Accuracy from 0-80.
- Notable patterns: For 7B model, Vanilla achieves ~50% while PINE achieves ~62%. For 110B model, Vanilla achieves ~75% while PINE achieves ~80%.
- Supports claim: PINE improves math reasoning accuracy by 12.6% for 7B models and 5.3% for 110B models.

## 4.5 Computational Overhead [p. 10]

Section 3.4 briefly discusses the computational overhead, with a conclusion that PINE's efficiency is acceptable [p. 10]. In the experiments, the wall time of PINE is found to be ∼2x and ∼8x of the vanilla inference on the LM-as-a-judge task and retrieval-augmented QA task with 20 documents which is acceptable at least during experiments [p. 10]. However, the code has not been specially optimized to accelerate PINE, and the implementation still contains a "for" loop. Therefore, the authors believe there is room to accelerate PINE [p. 10]. Compared with the time overhead, the memory overhead is small and PINE can be run with 70B models on 3x A100 80G on the retrieval-augmented QA task, which requires the same number of GPUs as the vanilla inference [p. 10]. Since efficiency is not the main focus of this paper, this is left as future work [p. 10].