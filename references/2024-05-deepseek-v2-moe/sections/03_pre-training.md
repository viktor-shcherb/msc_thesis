# 3. Pre-Training [p. 11]

## 3.1 Experimental Setups

### 3.1.1 Data Construction

[p. 11] While maintaining the same data processing stages as for DeepSeek 67B (DeepSeek-AI, 2024), the amount of data is extended and data quality is elevated. In order to enlarge the pre-training corpus, the potential of the internet data is explored and cleaning processes are optimized, thus recovering a large amount of mistakenly deleted data. Moreover, more Chinese data is incorporated, aiming to better leverage the corpus available on the Chinese internet. In addition to the amount of data, data quality is also a focus. The pre-training corpus is enriched with high-quality data from various sources, and meanwhile the quality-based filtering algorithm is improved. The improved algorithm ensures that a large amount of non-beneficial data will be removed, while the valuable data will be mostly retained. In addition, contentious content is filtered out from the pre-training corpus to mitigate the data bias introduced from specific regional cultures. A detailed discussion about the influence of this filtering strategy is presented in Appendix E. [p. 11]

---
[p. 12 continued]

[p. 12] The same tokenizer as used in DeepSeek 67B is adopted, which is built based on the Byte-level Byte-Pair Encoding (BBPE) algorithm and has a vocabulary size of 100K. The tokenized pre-training corpus contains 8.1T tokens, where Chinese tokens are approximately 12% more than English ones.

### 3.1.2 Hyper-Parameters

**Model Hyper-Parameters.** [p. 12] The number of Transformer layers is set to 60 and the hidden dimension to 5120. All learnable parameters are randomly initialized with a standard deviation of 0.006. In MLA, the number of attention heads $n_h$ is set to 128 and the per-head dimension $d_h$ to 128. The KV compression dimension $d_c$ is set to 512, and the query compression dimension $d_c'$ is set to 1536. For the decoupled queries and key, the per-head dimension $d_h^R$ is set to 64. Following Dai et al. (2024), all FFNs except for the first layer are substituted with MoE layers. Each MoE layer consists of 2 shared experts and 160 routed experts, where the intermediate hidden dimension of each expert is 1536. Among the routed experts, 6 experts will be activated for each token. In addition, the low-rank compression and fine-grained expert segmentation will impact the output scale of a layer. Therefore, in practice, additional RMS Norm layers are employed after the compressed latent vectors, and additional scaling factors are multiplied at the width bottlenecks (i.e., the compressed latent vectors and the intermediate hidden states of routed experts) to ensure stable training. Under this configuration, DeepSeek-V2 comprises 236B total parameters, of which 21B are activated for each token. [p. 12]

**Training Hyper-Parameters.** [p. 12] The AdamW optimizer (Loshchilov and Hutter, 2017) is employed with hyper-parameters set to $\beta_1 = 0.9$, $\beta_2 = 0.95$, and weight_decay = 0.1. The learning rate is scheduled using a warmup-and-step-decay strategy (DeepSeek-AI, 2024). Initially, the learning rate linearly increases from 0 to the maximum value during the first 2K steps. Subsequently, the learning rate is multiplied by 0.316 after training about 60% of tokens, and again by 0.316 after training about 90% of tokens. The maximum learning rate is set to $2.4 \times 10^{-4}$, and the gradient clipping norm is set to 1.0. A batch size scheduling strategy is also used, where the batch size is gradually increased from 2304 to 9216 in the training of the first 225B tokens, and then keeps 9216 in the remaining training. The maximum sequence length is set to 4K, and DeepSeek-V2 is trained on 8.1T tokens. Pipeline parallelism is leveraged to deploy different layers of a model on different devices, and for each layer, the routed experts will be uniformly deployed on 8 devices ($D = 8$). As for the device-limited routing, each token will be sent to at most 3 devices ($M = 3$). As for balance losses, $\alpha_1$ is set to 0.003, $\alpha_2$ to 0.05, and $\alpha_3$ to 0.02. The token-dropping strategy is employed during training for acceleration, but no tokens are dropped for evaluation. [p. 12]

### 3.1.3 Infrastructures

[p. 12-13] DeepSeek-V2 is trained based on the HAI-LLM framework (High-flyer, 2023), an efficient and light-weight training framework developed internally by their engineers. It employs a 16-way zero-bubble pipeline parallelism (Qi et al., 2023), an 8-way expert parallelism (Lepikhin et al., 2021), and ZeRO-1 data parallelism (Rajbhandari et al., 2020). Given that DeepSeek-V2 has relatively few activated parameters, and a portion of the operators are recomputed to save activation memory, it can be trained without the necessity of tensor parallelism, thereby decreasing the communication overhead. Moreover, in order to further improve the training efficiency, the computation of shared experts is overlapped with the expert parallel all-to-all communication. Faster CUDA kernels are also customized for communications, routing algorithms, and fused linear computations across different experts. In addition, MLA is also optimized based on an improved version of FlashAttention-2 (Dao, 2023). [p. 13]

All experiments are conducted on a cluster equipped with NVIDIA H800 GPUs. Each node in the H800 cluster contains 8 GPUs connected using NVLink and NVSwitch within nodes. Across nodes, InfiniBand interconnects are utilized to facilitate communications. [p. 13]

### 3.1.4 Long Context Extension

[p. 13] After the initial pre-training of DeepSeek-V2, YaRN (Peng et al., 2023) is employed to extend the default context window length from 4K to 128K. YaRN was specifically applied to the decoupled shared key $\mathbf{k}_t^R$ as it is responsible for carrying RoPE (Su et al., 2024). For YaRN, the scale $s$ is set to 40, $\alpha$ to 1, $\beta$ to 32, and the target maximum context length to 160K. Under these settings, the model can be expected to respond well for a context length of 128K. Slightly diverging from original YaRN, due to the distinct attention mechanism, the length scaling factor is adjusted to modulate the attention entropy. The factor $\sqrt{t}$ is computed as $\sqrt{t} = 0.0707 \ln s + 1$, aiming at minimizing the perplexity. [p. 13]

The model is additionally trained for 1000 steps, with a sequence length of 32K and a batch size of 576 sequences. Although the training is conducted solely at the sequence length of 32K, the model still demonstrates robust performance when being evaluated at a context length of 128K. As shown in Figure 4, the results on the "Needle In A Haystack" (NIAH) tests indicate that DeepSeek-V2 performs well across all context window lengths up to 128K. [p. 13]

**Figure 4** (p. 13): "Evaluation results on the 'Needle In A Haystack' (NIAH) tests. DeepSeek-V2 performs well across all context window lengths up to 128K."
The figure shows a heatmap titled "Pressure Testing DeepSeek-V2 Base 128K Context via 'Needle In A HayStack'". The x-axis is Context Length (#Tokens) ranging from 1K to 128K. The y-axis is Document Depth Percent (%) ranging from 0 to 100. The color scale (Score) ranges from 1 to 10. The heatmap is predominantly green (high scores of ~10) across nearly all context lengths and depth percentages, with only a few small red/orange patches (around depth 45-64% at context lengths 24K and 81K), indicating near-perfect retrieval performance across all conditions.

## 3.2 Evaluations

### 3.2.1 Evaluation Benchmarks

[p. 13-14] DeepSeek-V2 is pretrained on a bilingual corpus, so it is evaluated on a series of benchmarks in English and Chinese. The evaluation is based on their internal evaluation framework integrated in the HAI-LLM framework. Included benchmarks are categorized and listed as follows, where underlined benchmarks are in Chinese:

**Multi-subject multiple-choice** datasets include MMLU (Hendrycks et al., 2020), C-Eval (Huang et al., 2023), and CMMLU (Li et al., 2023). [p. 14]

**Language understanding and reasoning** datasets include HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), ARC (Clark et al., 2018), and BigBench Hard (BBH) (Suzgun et al., 2022). [p. 14]

**Closed-book question answering** datasets include TriviaQA (Joshi et al., 2017) and NaturalQuestions (Kwiatkowski et al., 2019). [p. 14]

**Reading comprehension** datasets include RACE (Lai et al., 2017), DROP (Dua et al., 2019), C3 (Sun et al., 2019), and CMRC (Cui et al., 2019). [p. 14]

**Reference disambiguation** datasets include WinoGrande (Sakaguchi et al., 2019) and CLUEWSC (Xu et al., 2020). [p. 14]

**Language modeling** datasets include Pile (Gao et al., 2020). [p. 14]

**Chinese understanding and culture** datasets include CHID (Zheng et al., 2019) and CCPM (Li et al., 2021). [p. 14]

**Math** datasets include GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), and CMath (Wei et al., 2023). [p. 14]

**Code** datasets include HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), and CRUXEval (Gu et al., 2024). [p. 14]

**Standardized exams** include AGIEval (Zhong et al., 2023). Note that AGIEval includes both English and Chinese subsets. [p. 14]

Following their previous work (DeepSeek-AI, 2024), perplexity-based evaluation is adopted for datasets including HellaSwag, PIQA, WinoGrande, RACE-Middle, RACE-High, MMLU, ARC-Easy, ARC-Challenge, CHID, C-Eval, CMMLU, C3, and CCPM, and generation-based evaluation is adopted for TriviaQA, NaturalQuestions, DROP, MATH, GSM8K, HumanEval, MBPP, CRUXEval, BBH, AGIEval, CLUEWSC, CMRC, and CMath. In addition, language-modeling-based evaluation is performed for Pile-test and Bits-Per-Byte (BPB) is used as the metric to guarantee fair comparison among models with different tokenizers. [p. 14]

Evaluation formats for each benchmark are additionally provided in Appendix G. [p. 14]

### 3.2.2 Evaluation Results

[p. 14-16] DeepSeek-V2 is compared with several representative open-source models, including DeepSeek 67B (DeepSeek-AI, 2024) (their previous release), Qwen1.5 72B (Bai et al., 2023), LLaMA3 70B (AI@Meta, 2024), and Mixtral 8x22B (Mistral, 2024). All these models are evaluated with their internal evaluation framework, and they share the same evaluation setting. Overall, with only 21B activated parameters, DeepSeek-V2 significantly outperforms DeepSeek 67B on almost all benchmarks, and achieves top-tier performance among open-source models. [p. 14]

**Table 2** (p. 15): "Comparison among DeepSeek-V2 and other representative open-source models. All models are evaluated in our internal framework and share the same evaluation setting. **Bold** denotes the best and underline denotes the second-best. Scores with a gap smaller than 0.3 are regarded as at the same level. With only 21B activated parameters, DeepSeek-V2 achieves top-tier performance among open-source models."

| Benchmark (Metric) | # Shots | DeepSeek 67B | Qwen1.5 72B | Mixtral 8x22B | LLaMA 3 70B | DeepSeek-V2 |
|---|---|---|---|---|---|---|
| Architecture | - | Dense | Dense | MoE | Dense | MoE |
| # Activated Params | - | 67B | 72B | 39B | 70B | 21B |
| # Total Params | - | 67B | 72B | 141B | 70B | 236B |
| Pile-test (BPB) | - | 0.642 | 0.637 | 0.623 | **0.602** | 0.606 |
| BBH (EM) | 3-shot | 68.7 | 59.9 | 78.9 | **81.0** | 78.9 |
| MMLU (Acc.) | 5-shot | 71.3 | 77.2 | 77.6 | **78.9** | 78.5 |
| DROP (F1) | 3-shot | 69.7 | 71.5 | 80.4 | **82.5** | 80.1 |
| ARC-Easy (Acc.) | 25-shot | 95.3 | 97.1 | 97.3 | **97.9** | 97.6 |
| ARC-Challenge (Acc.) | 25-shot | 86.4 | 92.8 | 91.2 | **93.3** | 92.4 |
| HellaSwag (Acc.) | 10-shot | 86.3 | 85.8 | 86.6 | **87.9** | 84.2 |
| PIQA (Acc.) | 0-shot | 83.6 | 83.3 | 83.6 | **85.0** | 83.7 |
| WinoGrande (Acc.) | 5-shot | 84.9 | 82.4 | 83.7 | **85.7** | 84.9 |
| RACE-Middle (Acc.) | 5-shot | 69.9 | 63.4 | **73.3** | **73.3** | 73.1 |
| RACE-High (Acc.) | 5-shot | 50.7 | 47.0 | 56.7 | **57.9** | 52.7 |
| TriviaQA (EM) | 5-shot | 78.9 | 73.1 | **82.1** | 81.6 | 79.9 |
| NaturalQuestions (EM) | 5-shot | 36.6 | 35.6 | 39.6 | **40.2** | 38.7 |
| AGIEval (Acc.) | 0-shot | 41.3 | **64.4** | 43.4 | 49.8 | 51.2 |
| HumanEval (Pass@1) | 0-shot | 45.1 | 43.9 | **53.1** | 48.2 | 48.8 |
| MBPP (Pass@1) | 3-shot | 57.4 | 53.6 | 64.2 | **68.6** | 66.6 |
| CRUXEval-I (Acc.) | 2-shot | 42.5 | 44.3 | 52.4 | 49.4 | **52.8** |
| CRUXEval-O (Acc.) | 2-shot | 41.0 | 42.3 | 52.8 | **54.3** | 49.8 |
| GSM8K (EM) | 8-shot | 63.4 | 77.9 | 80.3 | **83.0** | 79.2 |
| MATH (EM) | 4-shot | 18.7 | 41.4 | 42.5 | 42.2 | **43.6** |
| CMath (EM) | 3-shot | 63.0 | 77.8 | 72.3 | 73.9 | **78.7** |
| CLUEWSC (EM) | 5-shot | 81.0 | 80.5 | 77.5 | 78.3 | **82.2** |
| C-Eval (Acc.) | 5-shot | 66.1 | **83.7** | 59.6 | 67.5 | 81.7 |
| CMMLU (Acc.) | 5-shot | 70.8 | **84.3** | 60.0 | 69.3 | 84.0 |
| CMRC (EM) | 1-shot | 73.4 | 66.6 | 73.1 | 73.3 | **77.5** |
| C3 (Acc.) | 0-shot | 75.3 | **78.2** | 71.4 | 74.0 | 77.4 |
| CHID (Acc.) | 0-shot | 92.1 | - | 57.0 | 83.2 | **92.7** |
| CCPM (Acc.) | 0-shot | 88.5 | 88.1 | 61.0 | 68.1 | **93.1** |

[p. 14-15] Detailed comparison of DeepSeek-V2 with its open-source counterparts one by one:

(1) Compared with Qwen1.5 72B, another model that supports both Chinese and English, DeepSeek-V2 demonstrates overwhelming advantages on the majority of English, code, and math benchmarks. As for Chinese benchmarks, Qwen1.5 72B shows better performance on multi-subject multiple-choice tasks while DeepSeek-V2 is comparable or better on others. Note that for the CHID benchmark, the tokenizer of Qwen1.5 72B will encounter errors in their evaluation framework, so the CHID score for Qwen1.5 72B is left blank. [p. 15]

(2) Compared with Mixtral 8x22B, DeepSeek-V2 achieves comparable or better English performance, except for TriviaQA, NaturalQuestions, and HellaSwag, which are closely related to English commonsense knowledge. Notably, DeepSeek-V2 outperforms Mixtral 8x22B on MMLU. On code and math benchmarks, DeepSeek-V2 demonstrates comparable performance with Mixtral 8x22B. Since Mixtral 8x22B is not specifically trained on Chinese data, its Chinese capability lags far behind DeepSeek-V2. [p. 15]

(3) Compared with LLaMA3 70B, DeepSeek-V2 is trained on fewer than a quarter of English tokens. Therefore, DeepSeek-V2 still has a slight gap in basic English capabilities with LLaMA3 70B. However, even with much fewer training tokens and activated parameters, DeepSeek-V2 still demonstrates comparable code and math capability with LLaMA3 70B. Also, as a bilingual language model, DeepSeek-V2 outperforms LLaMA3 70B overwhelmingly on Chinese benchmarks. [p. 15-16]

Finally, it is worth mentioning that certain prior studies (Hu et al., 2024) incorporate SFT data during the pre-training stage, whereas DeepSeek-V2 has never been exposed to SFT data during pre-training. [p. 16]

### 3.2.3 Training and Inference Efficiency

**Training Costs.** [p. 16] Since DeepSeek-V2 activates fewer parameters for each token and requires fewer FLOPs than DeepSeek 67B, training DeepSeek-V2 will be more economical than training DeepSeek 67B theoretically. Although training an MoE model will introduce additional communication overheads, through operator and communication optimizations, the training for DeepSeek-V2 can attain a relatively high Model FLOPs Utilization (MFU). During practical training on the H800 cluster, for training on each trillion tokens, DeepSeek 67B requires 300.6K GPU hours, while DeepSeek-V2 needs only 172.8K GPU hours, i.e., sparse DeepSeek-V2 can save 42.5% training costs compared with dense DeepSeek 67B. [p. 16]

**Inference Efficiency.** [p. 16] In order to efficiently deploy DeepSeek-V2 for service, its parameters are first converted into the precision of FP8. In addition, KV cache quantization (Hooper et al., 2024; Zhao et al., 2023) is performed for DeepSeek-V2 to further compress each element in its KV cache into 6 bits on average. Benefiting from MLA and these optimizations, actually deployed DeepSeek-V2 requires significantly less KV cache than DeepSeek 67B, and thus can serve a much larger batch size. The generation throughput of DeepSeek-V2 is evaluated based on the prompt and generation length distribution from the actually deployed DeepSeek 67B service. On a single node with 8 H800 GPUs, DeepSeek-V2 achieves a generation throughput exceeding 50K tokens per second, which is 5.76 times the maximum generation throughput of DeepSeek 67B. In addition, the prompt input throughput of DeepSeek-V2 exceeds 100K tokens per second. [p. 16]
