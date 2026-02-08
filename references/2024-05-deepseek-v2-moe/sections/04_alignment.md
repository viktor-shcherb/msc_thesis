# 4. Alignment [p. 16]

## 4.1 Supervised Fine-Tuning

[p. 16] Building upon their prior research (DeepSeek-AI, 2024), the instruction tuning datasets are curated to include 1.5M instances, comprising 1.2M instances for helpfulness and 0.3M instances for safety. In comparison to the initial version, data quality is improved to mitigate hallucinatory responses and enhance writing proficiency. DeepSeek-V2 is fine-tuned with 2 epochs, and the learning rate is set to $5 \times 10^{-6}$. For the evaluation of DeepSeek-V2 Chat (SFT), mainly generation-based benchmarks are included, except for several representative multiple-choice tasks (MMLU and ARC). An instruction-following evaluation (IFEval) (Zhou et al., 2023) is also conducted for DeepSeek-V2 Chat (SFT), using prompt-level loose accuracy as the metric. Moreover, LiveCodeBench (Jain et al., 2024) is employed, using questions from September 1st, 2023 to April 1st, 2024 to evaluate chat models. In addition to the standard benchmarks, the model is further evaluated on open-ended conversation benchmarks including MT-Bench (Zheng et al., 2023), AlpacaEval 2.0 (Dubois et al., 2024), and AlignBench (Liu et al., 2023). For comparison, Qwen1.5 72B Chat, LLaMA-3-70B Instruct, and Mistral-8x22B Instruct are also evaluated in their evaluation framework and settings. As for DeepSeek 67B Chat, the evaluation results reported in their previous release are directly referred to. [p. 16]

## 4.2 Reinforcement Learning

[p. 17] In order to further unlock the potential of DeepSeek-V2 and align it with human preference, Reinforcement Learning (RL) is conducted to adjust its preference.

### Reinforcement Learning Algorithm

[p. 17] To save the training costs of RL, Group Relative Policy Optimization (GRPO) (Shao et al., 2024) is adopted, which foregoes the critic model that is typically with the same size as the policy model, and estimates the baseline from group scores instead. Specifically, for each question $q$, GRPO samples a group of outputs $\{o_1, o_2, \cdots, o_G\}$ from the old policy $\pi_{\theta_{old}}$ and then optimizes the policy model $\pi_\theta$ by maximizing the following objective:

$$\mathcal{J}_{GRPO}(\theta) = \mathbb{E}[q \sim P(Q), \{o_i\}_{i=1}^{G} \sim \pi_{\theta_{old}}(O|q)]$$

$$\frac{1}{G} \sum_{i=1}^{G} \left( \min \left( \frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)} A_i, \text{clip}\left(\frac{\pi_\theta(o_i|q)}{\pi_{\theta_{old}}(o_i|q)}, 1-\varepsilon, 1+\varepsilon\right) A_i \right) - \beta \mathbb{D}_{KL}(\pi_\theta || \pi_{ref}) \right), \quad (32)$$

$$\mathbb{D}_{KL}(\pi_\theta || \pi_{ref}) = \frac{\pi_{ref}(o_i|q)}{\pi_\theta(o_i|q)} - \log \frac{\pi_{ref}(o_i|q)}{\pi_\theta(o_i|q)} - 1, \quad (33)$$

where $\varepsilon$ and $\beta$ are hyper-parameters; and $A_i$ is the advantage, computed using a group of rewards $\{r_1, r_2, \ldots, r_G\}$ corresponding to the outputs within each group:

$$A_i = \frac{r_i - \text{mean}(\{r_1, r_2, \cdots, r_G\})}{\text{std}(\{r_1, r_2, \cdots, r_G\})}. \quad (34)$$

### Training Strategy

[p. 17] In preliminary experiments, the RL training on reasoning data, such as code and math prompts, exhibits unique characteristics that are distinct from the training on general data. For example, the mathematical and coding abilities of the model can keep improving over a longer period of training steps. Therefore, a two-stage RL training strategy is employed, which first performs reasoning alignment, and then performs human preference alignment.

In the first reasoning alignment stage, a reward model $RM_{reasoning}$ is trained for code and math reasoning tasks, and the policy model is optimized with the feedback of $RM_{reasoning}$:

$$r_i = RM_{reasoning}(o_i). \quad (35)$$

[p. 17] In the second human preference alignment stage, a multi-reward framework is adopted, which acquires rewards from a helpful reward model $RM_{helpful}$, a safety reward model $RM_{safety}$, and a rule-based reward model $RM_{rule}$. The final reward of a response $o_i$ is:

$$r_i = c_1 \cdot RM_{helpful}(o_i) + c_2 \cdot RM_{safety}(o_i) + c_3 \cdot RM_{rule}(o_i), \quad (36)$$

where $c_1$, $c_2$, and $c_3$ are corresponding coefficients.

[p. 17] In order to obtain reliable reward models that play crucial roles in the RL training, preference data is carefully collected and meticulous quality filtering and proportion adjustments are conducted. Code preference data is obtained based on compiler-feedback, and mathematical preference data based on ground-truth labels. For reward model training, the reward models are initialized with DeepSeek-V2 Chat (SFT) and trained with either a point-wise or a pair-wise loss. In their experiments, they observe that the RL training can fully tap into and activate the potential of the model, enabling it to select the correct and satisfactory answer from possible responses.

### Optimizations for Training Efficiency

[p. 18] Conducting RL training on extremely large models places high demands on the training framework. It requires careful engineering optimization to manage the GPU memory and RAM pressure, and meanwhile maintain a fast training speed. The following engineering optimizations are implemented: (1) A hybrid engine that adopts different parallel strategies for training and inference respectively to achieve higher GPU utilization. (2) vLLM (Kwon et al., 2023) is leveraged with large batch sizes as the inference backend to accelerate the inference speed. (3) A scheduling strategy for offloading models to CPUs and loading models back to GPUs is carefully designed, which achieves a near-optimal balance between the training speed and memory consumption.

## 4.3 Evaluation Results

### Evaluations on Standard Benchmarks

[p. 18] DeepSeek-V2 Chat (SFT) and DeepSeek-V2 Chat (RL) are evaluated on standard benchmarks. Notably, DeepSeek-V2 Chat (SFT) demonstrates substantial improvements in GSM8K, MATH, and HumanEval evaluations compared with its base version. This progress can be attributed to the inclusion of SFT data, which comprises a considerable volume of math and code related content. DeepSeek-V2 Chat (RL) further boosts the performance on math and code benchmarks. More code and math evaluations are shown in Appendix F.

[p. 18] Comparisons with other models:
- DeepSeek-V2 Chat (SFT) surpasses Qwen1.5 72B Chat on almost all English, math, and code benchmarks. On Chinese benchmarks, DeepSeek-V2 Chat (SFT) demonstrates slightly lower scores than Qwen1.5 72B Chat on multi-subject multiple-choice tasks, consistent with the performance observed from their base versions.
- Compared with Mixtral 8x22B Instruct, DeepSeek-V2 Chat (SFT) exhibits better performance on most benchmarks, except for NaturalQuestions and IFEval.
- Compared with LLaMA3 70B Instruct, DeepSeek-V2 Chat (SFT) shows similar performance in code and math related benchmarks. LLaMA3 70B Chat exhibits better performance on MMLU and IFEval, while DeepSeek-V2 Chat (SFT) showcases stronger performance on Chinese tasks.
- DeepSeek-V2 Chat (RL) demonstrates further enhanced performance in both mathematical and coding tasks compared with DeepSeek-V2 Chat (SFT).

**Table 3** (p. 19): "Comparison among DeepSeek-V2 Chat (SFT), DeepSeek-V2 Chat (RL), and other representative open-source chat models. Regarding TriviaQA and NaturalQuestions, it is worth noting that chat models, such as LLaMA3 70B Instruct, might not strictly adhere to the format constraints typically specified in the few-shot setting. Consequently, this can lead to underestimation of certain models in our evaluation framework."

| | | DeepSeek | Qwen 1.5 | LLaMA3 | Mixtral | DeepSeek-V2 | DeepSeek-V2 |
|---|---|---|---|---|---|---|---|
| **Benchmark** | **# Shots** | **67B Chat** | **72B Chat** | **70B Inst.** | **8x22B Inst.** | **Chat (SFT)** | **Chat (RL)** |
| Context Length | - | 4K | 32K | 8K | 64K | 128K | 128K |
| Architecture | - | Dense | Dense | Dense | MoE | MoE | MoE |
| # Activated Params | - | 67B | 72B | 70B | 39B | 21B | 21B |
| # Total Params | - | 67B | 72B | 70B | 141B | 236B | 236B |
| | | | | | | | |
| TriviaQA | 5-shot | 81.5 | 79.6 | 69.1 | 80.0 | 85.4 | 86.7 |
| NaturalQuestions | 5-shot | 47.0 | 46.9 | 44.6 | **54.9** | 51.9 | 53.4 |
| MMLU | 5-shot | 71.1 | 76.2 | **80.3** | 77.8 | **78.4** | 77.8 |
| ARC-Easy | 25-shot | 96.6 | 96.8 | 96.9 | 97.1 | **97.6** | **98.1** |
| ARC-Challenge | 25-shot | 88.9 | **91.7** | **92.6** | 90.0 | **92.5** | 92.3 |
| BBH | 3-shot | 71.7 | **65.9** | **80.1** | 78.4 | **81.3** | 79.7 |
| AGIEval | 0-shot | 46.4 | **62.8** | 56.6 | 41.4 | **63.2** | 61.4 |
| IFEval | 0-shot | 55.5 | 57.3 | **79.7** | **72.1** | 64.1 | 63.8 |
| | | | | | | | |
| HumanEval | 0-shot | 73.8 | 61.4 | 68.9 | 76.2 | **76.8** | **81.1** |
| MBPP | 3-shot | 61.4 | 52.2 | 69.8 | 64.4 | **70.4** | **72.0** |
| CRUXEval-I-COT | 2-shot | 49.1 | 51.4 | **61.1** | 59.4 | 59.5 | **61.5** |
| CRUXEval-O-COT | 2-shot | 50.9 | 56.5 | **63.6** | **63.6** | 60.7 | **63.0** |
| LiveCodeBench | 0-shot | 18.3 | 18.8 | **30.5** | 25.0 | 28.7 | **32.5** |
| | | | | | | | |
| GSM8K | 8-shot | 84.1 | 81.9 | **93.2** | 87.9 | 90.8 | **92.2** |
| MATH | 4-shot | 32.6 | 40.6 | 48.5 | 49.8 | **52.7** | **53.9** |
| CMath | 0-shot | 80.3 | **82.8** | 79.2 | 75.1 | **82.0** | **81.9** |
| | | | | | | | |
| CLUEWSC | 5-shot | 78.5 | **90.1** | 85.4 | 75.8 | **88.6** | **89.9** |
| C-Eval | 5-shot | 65.2 | **82.2** | 67.9 | 60.0 | **80.9** | **78.0** |
| CMMLU | 5-shot | 67.8 | **82.9** | 70.7 | 61.0 | **82.4** | 81.6 |

**Table 4** (p. 19): "English open-ended conversation evaluations. For AlpacaEval 2.0, we use the length-controlled win rate as the metric."

| Model | MT-Bench | AlpacaEval 2.0 |
|---|---|---|
| DeepSeek 67B Chat | 8.35 | 16.6 |
| Mistral 8x22B Instruct v0.1 | 8.66 | 30.9 |
| Qwen1.5 72B Chat | 8.61 | 36.6 |
| LLaMA3 70B Instruct | **8.95** | 34.4 |
| DeepSeek-V2 Chat (SFT) | 8.62 | 30.0 |
| DeepSeek-V2 Chat (RL) | **8.97** | **38.9** |

### Evaluations on Open-Ended Generation

[p. 18-19] For English open-ended conversation generation, MT-Bench and AlpacaEval 2.0 are utilized as benchmarks. Evaluation results in Table 4 demonstrate a significant performance advantage of DeepSeek-V2 Chat (RL) over DeepSeek-V2 Chat (SFT), showcasing the effectiveness of RL training in achieving improved alignment. Compared to other open-source models, DeepSeek-V2 Chat (RL) demonstrates superior performance over Mistral 8x22B Instruct and Qwen1.5 72B Chat on both benchmarks. When compared with LLaMA3 70B Instruct, DeepSeek-V2 Chat (RL) showcases competitive performance on MT-Bench and notably outperforms it on AlpacaEval 2.0.

[p. 19] For Chinese open-ended generation capability, AlignBench is used. As presented in Table 5, DeepSeek-V2 Chat (RL) exhibits a slight advantage over DeepSeek-V2 Chat (SFT). Notably, DeepSeek-V2 Chat (SFT) surpasses all open-source Chinese models by a significant margin. It significantly outperforms the second-best open-source model, Qwen1.5 72B Chat, on both Chinese reasoning and language. Moreover, both DeepSeek-V2 Chat (SFT) and DeepSeek-V2 Chat (RL) outperform GPT-4-0613 and ERNIEBot 4.0, solidifying the position of their models in the top-tier LLMs that support Chinese. Specifically, DeepSeek-V2 Chat (RL) shows remarkable performance in Chinese language understanding, which outperforms all models including GPT-4-Turbo-1106-Preview. On the other hand, the reasoning capability of DeepSeek-V2 Chat (RL) still lags behind giant models, such as Erniebot-4.0 and GPT-4s.

**Table 5** (p. 20): "AlignBench leaderboard rated by GPT-4-0613. Models are ranked in descending order based on the overall score. Models marked with * represent that we evaluate them through their API service or open-weighted model, instead of referring to the results reported in their original papers. Suffixes of Erniebot-4.0 and Moonshot denote the timestamps when we called their API."

| Model | Overall | Reasoning Avg. | Math. | Logi. | Language Avg. | Fund. | Chi. | Open. | Writ. | Role. | Pro. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-4-1106-Preview | 8.01 | 7.73 | 7.80 | 7.66 | 8.29 | 7.99 | 7.33 | 8.61 | 8.67 | 8.47 | 8.65 |
| DeepSeek-V2 Chat (RL) | 7.91 | 7.45 | 7.77 | 7.14 | 8.36 | 8.10 | 8.28 | 8.37 | 8.53 | 8.33 | 8.53 |
| ERNIEBot-4.0-202404* | 7.89 | 7.61 | 7.81 | 7.41 | 8.17 | 7.56 | 8.53 | 8.13 | 8.45 | 8.24 | 8.09 |
| DeepSeek-V2 Chat (SFT) | 7.74 | 7.30 | 7.34 | 7.26 | 8.17 | 8.04 | 8.26 | 8.13 | 8.00 | 8.10 | 8.49 |
| GPT-4-0613 | 7.53 | 7.47 | 7.56 | 7.37 | 7.59 | 7.81 | 6.93 | 7.42 | 7.93 | 7.51 | 7.94 |
| ERNIEBot-4.0-202312* | 7.36 | 6.84 | 7.00 | 6.67 | 7.88 | 7.47 | 7.88 | 8.05 | 8.19 | 7.84 | 7.85 |
| Moonshot-v1-32k-202404* | 7.22 | 6.42 | 6.41 | 6.43 | 8.02 | 7.82 | 7.58 | 8.00 | 8.22 | 8.19 | 8.29 |
| Qwen1.5-72B-Chat* | 7.19 | 6.45 | 6.58 | 6.31 | 7.93 | 7.38 | 7.77 | 8.15 | 8.02 | 8.05 | 8.24 |
| DeepSeek-67B-Chat | 6.43 | 5.75 | 5.71 | 5.79 | 7.11 | 7.12 | 6.52 | 7.58 | 7.20 | 6.91 | 7.37 |
| ChatGLM-Turbo | 6.24 | 5.00 | 4.74 | 5.26 | 7.49 | 6.82 | 7.17 | 8.16 | 7.77 | 7.76 | 7.24 |
| ERNIEBot-3.5 | 6.14 | 5.15 | 5.03 | 5.27 | 7.13 | 6.62 | 7.60 | 7.26 | 7.56 | 6.83 | 6.90 |
| Yi-34B-Chat* | 6.12 | 4.86 | 4.97 | 4.74 | 7.38 | 6.72 | 7.28 | 7.76 | 7.44 | 7.58 | 7.53 |
| GPT-3.5-Turbo-0613 | 6.08 | 5.35 | 5.68 | 5.02 | 6.82 | 6.71 | 5.81 | 7.29 | 7.03 | 7.28 | 6.77 |
| ChatGLM-Pro | 5.83 | 4.65 | 4.54 | 4.75 | 7.01 | 6.51 | 6.76 | 7.47 | 7.07 | 7.34 | 6.89 |
| SparkDesk-V2 | 5.74 | 4.73 | 4.71 | 4.74 | 6.76 | 5.84 | 6.97 | 7.29 | 7.18 | 6.92 | 6.34 |
| Qwen-14-Chat | 5.72 | 4.81 | 4.91 | 4.71 | 6.63 | 6.90 | 6.36 | 6.74 | 6.64 | 6.59 | 6.56 |
| Baichuan2-13B-Chat | 5.25 | 3.92 | 3.76 | 4.07 | 6.59 | 6.22 | 6.05 | 7.11 | 6.97 | 6.75 | 6.43 |
| ChatGLM3-6B | 4.97 | 3.85 | 3.55 | 4.14 | 6.10 | 5.75 | 5.29 | 6.71 | 6.83 | 6.28 | 5.73 |
| Baichuan2-7B-Chat | 4.97 | 3.66 | 3.56 | 3.75 | 6.28 | 5.81 | 5.50 | 7.13 | 6.84 | 6.53 | 5.84 |
| InternLM-20B | 4.96 | 3.66 | 3.39 | 3.92 | 6.26 | 5.96 | 5.50 | 7.18 | 6.19 | 6.49 | 6.22 |
| Qwen-7B-Chat | 4.91 | 3.73 | 3.62 | 3.83 | 6.09 | 6.40 | 5.74 | 6.26 | 6.31 | 6.19 | 5.66 |
| ChatGLM2-6B | 4.48 | 3.39 | 3.16 | 3.61 | 5.58 | 4.91 | 4.52 | 6.66 | 6.25 | 6.08 | 5.08 |
| InternLM-Chat-7B | 3.65 | 2.56 | 2.45 | 2.66 | 4.75 | 4.34 | 4.09 | 5.82 | 4.89 | 5.32 | 4.06 |
| Chinese-LLaMA-2-7B-Chat | 3.57 | 2.68 | 2.29 | 3.07 | 4.46 | 4.31 | 4.26 | 4.50 | 4.63 | 4.91 | 4.13 |
| LLaMA-2-13B-Chinese-Chat | 3.35 | 2.47 | 2.21 | 2.73 | 4.23 | 4.13 | 3.31 | 4.79 | 3.93 | 4.53 | 4.71 |

## 4.4 Discussion

### Amount of SFT Data

[p. 20] The discussion surrounding the necessity of a large SFT corpus has been a topic of intense debate. Previous works (Young et al., 2024; Zhou et al., 2024) argue that fewer than 10K instances of SFT data are enough to produce satisfactory results. However, in their experiments, a significant performance decline on the IFEval benchmark is observed if fewer than 10K instances are used. A possible explanation is that a language model necessitates a certain amount of data to develop specific skills. Although the requisite data amount may diminish with the model size increasing, it cannot be entirely eliminated. Their observation underscores the critical need for sufficient data to equip an LLM with desired capabilities. Moreover, the quality of SFT data is also crucial, especially for tasks involving writing or open-ended questions.

### Alignment Tax of Reinforcement Learning

[p. 20] During human preference alignment, a significant performance enhancement on the open-ended generation benchmarks is observed, in terms of the scores rated by both AI and human evaluators. However, a phenomenon of "alignment tax" (Ouyang et al., 2022) is also noticed, i.e., the alignment process can negatively impact the performance on some standard benchmarks such as BBH. In order to alleviate the alignment tax, during the RL stage, significant efforts are made in data processing and improving training strategies, finally achieving a tolerable trade-off between the performance on standard and open-ended benchmarks. Exploring how to align a model with human preferences without compromising its general performance presents a valuable direction for future research.

### Online Reinforcement Learning

[p. 21] In preference alignment experiments, the online approach significantly outperforms the offline approach. Therefore, tremendous efforts are invested in implementing an online RL framework for aligning DeepSeek-V2. The conclusion about online or offline preference alignment can vary in different contexts, and a more thorough comparison and analysis between them is reserved for future work.
