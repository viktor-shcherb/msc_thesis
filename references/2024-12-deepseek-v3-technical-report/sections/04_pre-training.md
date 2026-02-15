# 4. Pre-Training [p. 21]

## 4.1. Data Construction [p. 21]

Compared with DeepSeek-V2, the pre-training corpus is optimized by enhancing the ratio of mathematical and programming samples, while expanding multilingual coverage beyond English and Chinese. The data processing pipeline is refined to minimize redundancy while maintaining corpus diversity. Inspired by Ding et al. (2024), the document packing method is implemented for data integrity but does not incorporate cross-sample attention masking during training. The training corpus for DeepSeek-V3 consists of 14.8T high-quality and diverse tokens in the tokenizer. [p. 21]

In the training process of DeepSeekCoder-V2 (DeepSeek-AI, 2024a), it is observed that the Fill-in-Middle (FIM) strategy does not compromise the next-token prediction capability while enabling the model to accurately predict middle text based on contextual cues. In alignment with DeepSeekCoder-V2, the FIM strategy is also incorporated in the pre-training of DeepSeek-V3. To be specific, the Prefix-Suffix-Middle (PSM) framework is employed to structure data as follows: [p. 22]

```
<|fim_begin|>_fpre<|fim_hole|>_fsuf<|fim_end|>_fmiddle<|eos_token|>
```

This structure is applied at the document level as a part of the pre-packing process. The FIM strategy is applied at a rate of 0.1, consistent with the PSM framework. [p. 22]

The tokenizer for DeepSeek-V3 employs Byte-level BPE (Shibata et al., 1999) with an extended vocabulary of 128K tokens. The tokenization and training data for the tokenizer are modified to optimize multilingual compression efficiency. In addition, compared with DeepSeek-V2, the new pretokenizer introduces tokens that combine punctuations and line breaks. However, this trick may introduce the token boundary bias (Lundberg, 2023) when the model processes multi-line prompts without terminal line breaks, particularly for few-shot evaluation prompts. To address this issue, a certain proportion of such combined tokens is randomly split during training, which exposes the model to a wider array of special cases and mitigates this bias. [p. 22]

## 4.2. Hyper-Parameters [p. 22]

### Model Hyper-Parameters [p. 22]

The number of Transformer layers is set to 61 and the hidden dimension to 7168. All learnable parameters are randomly initialized with a standard deviation of 0.006. In MLA, the number of attention heads n_h is set to 128 and the per-head dimension d_h to 128. The KV compression dimension d_c is set to 512, and the query compression dimension d_c' is set to 1536. For the decoupled queries and key, the per-head dimension d_h^R is set to 64. All FFNs except for the first three layers are substituted with MoE layers. Each MoE layer consists of 1 shared expert and 256 routed experts, where the intermediate hidden dimension of each expert is 2048. Among the routed experts, 8 experts will be activated for each token, and each token will be ensured to be sent to at most 4 nodes. The multi-token prediction depth D is set to 1, i.e., besides the exact next token, each token will predict one additional token. As DeepSeek-V2, DeepSeek-V3 also employs additional RMSNorm layers after the compressed latent vectors, and multiplies additional scaling factors at the width bottlenecks. Under this configuration, DeepSeek-V3 comprises 671B total parameters, of which 37B are activated for each token. [p. 22]

### Training Hyper-Parameters [p. 22]

The AdamW optimizer (Loshchilov and Hutter, 2017) is employed with hyper-parameters set to β₁ = 0.9, β₂ = 0.95, and weight_decay = 0.1. The maximum sequence length is set to 4K during pre-training. DeepSeek-V3 is trained on 14.8T tokens. As for the learning rate scheduling, the learning rate is first linearly increased from 0 to 2.2 × 10⁻⁴ during the first 2K steps. Then, a constant learning rate of 2.2 × 10⁻⁴ is kept until the model consumes 10T training tokens. Subsequently, the learning rate is gradually decayed to 2.2 × 10⁻⁵ in 4.3T tokens, following a cosine decay curve. During the training of the final 500B tokens, a constant learning rate of 2.2 × 10⁻⁵ is kept in the first 333B tokens, and then the learning rate is switched to another constant learning rate of 7.3 × 10⁻⁶ in the remaining 167B tokens. The gradient clipping norm is set to 1.0. A batch size scheduling strategy is employed, where the batch size is gradually increased from 3072 to 15360 in the training of the first 469B tokens, and then keeps 15360 in the remaining training. Pipeline parallelism is leveraged to deploy a model on different GPUs, and for each layer, the routed experts will be uniformly deployed on 64 GPUs belonging to 8 nodes. As for the node-limited routing, each token will be sent to at most 4 nodes (i.e., M = 4). For auxiliary-loss-free load balancing, the bias update speed γ is set to 0.001 for the first 14.3T tokens, and to 0.0 for the remaining 500B tokens. For the balance loss, α is set to 0.0001, just to avoid extreme imbalance within any single sequence. The MTP loss weight λ is set to 0.3 for the first 10T tokens, and to 0.1 for the remaining 4.8T tokens. [p. 22-23]

## 4.3. Long Context Extension [p. 23]

A similar approach to DeepSeek-V2 (DeepSeek-AI, 2024c) is adopted to enable long context capabilities in DeepSeek-V3. After the pre-training stage, YaRN (Peng et al., 2023a) is applied for context extension and two additional training phases are performed, each comprising 1000 steps, to progressively expand the context window from 4K to 32K and then to 128K. The YaRN configuration is consistent with that used in DeepSeek-V2, being applied exclusively to the decoupled shared key $\mathbf{k}_t^R$. The hyper-parameters remain identical across both phases, with the scale s = 40, α = 1, β = 32, and the scaling factor $\sqrt{t} = 0.1 \ln s + 1$. In the first phase, the sequence length is set to 32K, and the batch size is 1920. During the second phase, the sequence length is increased to 128K, and the batch size is reduced to 480. The learning rate for both phases is set to 7.3 × 10⁻⁶, matching the final learning rate from the pre-training stage. [p. 23]

Through this two-phase extension training, DeepSeek-V3 is capable of handling inputs up to 128K in length while maintaining strong performance. Figure 8 illustrates that DeepSeek-V3, following supervised fine-tuning, achieves notable performance on the "Needle In A Haystack" (NIAH) test, demonstrating consistent robustness across context window lengths up to 128K. [p. 23]

**Figure 8** (p. 23): "Pressure Testing DeepSeek-V3 128K Context via 'Needle In A Haystack'"

Description: Heatmap visualization
- Key elements: X-axis shows Context Length (Tokens) from 2K to 128K, Y-axis shows Document Depth Percent (%) from 0 to 100, color scale shows Score from 1 (red) to 10 (cyan/green)
- Notable patterns: The heatmap is uniformly colored in bright cyan/green (score ~10), indicating perfect or near-perfect performance across all context lengths and document depths
- Supports claim: DeepSeek-V3 performs well across all context window lengths up to 128K on the NIAH test [p. 23]

## 4.4. Evaluations [p. 24]

### 4.4.1. Evaluation Benchmarks [p. 24]

The base model of DeepSeek-V3 is pretrained on a multilingual corpus with English and Chinese constituting the majority, so its performance is evaluated on a series of benchmarks primarily in English and Chinese, as well as on a multilingual benchmark. The evaluation is based on the internal evaluation framework integrated in the HAI-LLM framework. Considered benchmarks are categorized and listed as follows, where underlined benchmarks are in Chinese and double-underlined benchmarks are multilingual ones: [p. 24]

**Multi-subject multiple-choice** datasets include MMLU (Hendrycks et al., 2020), MMLU-Redux (Gema et al., 2024), MMLU-Pro (Wang et al., 2024b), MMMLU (OpenAI, 2024b), C-Eval (Huang et al., 2023), and CMMLU (Li et al., 2023). [p. 24]

**Language understanding and reasoning** datasets include HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), ARC (Clark et al., 2018), and BigBench Hard (BBH) (Suzgun et al., 2022). [p. 24]

**Closed-book question answering** datasets include TriviaQA (Joshi et al., 2017) and NaturalQuestions (Kwiatkowski et al., 2019). [p. 24]

**Reading comprehension** datasets include RACE (Lai et al., 2017), DROP (Dua et al., 2019), C3 (Sun et al., 2019a), and CMRC (Cui et al., 2019). [p. 24]

**Reference disambiguation** datasets include CLUEWSC (Xu et al., 2020) and WinoGrande (Sakaguchi et al., 2019). [p. 24]

**Language modeling** datasets include Pile (Gao et al., 2020). [p. 24]

**Chinese understanding and culture** datasets include CCPM (Li et al., 2021). [p. 24]

**Math** datasets include GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021), MGSM (Shi et al., 2023), and CMath (Wei et al., 2023). [p. 24]

**Code** datasets include HumanEval (Chen et al., 2021), LiveCodeBench-Base (0801-1101) (Jain et al., 2024), MBPP (Austin et al., 2021), and CRUXEval (Gu et al., 2024). [p. 24]

**Standardized exams** include AGIEval (Zhong et al., 2023). Note that AGIEval includes both English and Chinese subsets. [p. 24]

Following previous work (DeepSeek-AI, 2024b;c), perplexity-based evaluation is adopted for datasets including HellaSwag, PIQA, WinoGrande, RACE-Middle, RACE-High, MMLU, MMLU-Redux, MMLU-Pro, MMMLU, ARC-Easy, ARC-Challenge, C-Eval, CMMLU, C3, and CCPM, and generation-based evaluation is adopted for TriviaQA, NaturalQuestions, DROP, MATH, GSM8K, MGSM, HumanEval, MBPP, LiveCodeBench-Base, CRUXEval, BBH, AGIEval, CLUEWSC, CMRC, and CMath. In addition, language-modeling-based evaluation is performed for Pile-test and Bits-Per-Byte (BPB) is used as the metric to guarantee fair comparison among models using different tokenizers. [p. 24]

### 4.4.2. Evaluation Results [p. 24]

In Table 3, the base model of DeepSeek-V3 is compared with the state-of-the-art open-source base models, including DeepSeek-V2-Base (DeepSeek-AI, 2024c) (the previous release), Qwen2.5 72B Base (Qwen, 2024b), and LLaMA-3.1 405B Base (AI@Meta, 2024b). All these models are evaluated with the internal evaluation framework, and it is ensured that they share the same evaluation setting. Note that due to the changes in the evaluation framework over the past months, the performance of DeepSeek-V2-Base exhibits a slight difference from the previously reported results. Overall, DeepSeek-V3-Base comprehensively outperforms DeepSeek-V2-Base and Qwen2.5 72B Base, and surpasses LLaMA-3.1 405B Base in the majority of benchmarks, essentially becoming the strongest open-source model. [p. 24-25]

From a more detailed perspective, DeepSeek-V3-Base is compared with the other open-source base models individually. (1) Compared with DeepSeek-V2-Base, due to the improvements in the model architecture, the scale-up of the model size and training tokens, and the enhancement of data quality, DeepSeek-V3-Base achieves significantly better performance as expected. (2) Compared with Qwen2.5 72B Base, the state-of-the-art Chinese open-source model, with only half of the activated parameters, DeepSeek-V3-Base also demonstrates remarkable advantages, especially on English, multilingual, code, and math benchmarks. As for Chinese benchmarks, except for CMMLU, a Chinese multi-subject multiple-choice task, DeepSeek-V3-Base also shows better performance than Qwen2.5 72B. (3) Compared with LLaMA-3.1 405B Base, the largest open-source model with 11 times the activated parameters, DeepSeek-V3-Base also exhibits much better performance on multilingual, code, and math benchmarks. As for English and Chinese language benchmarks, DeepSeek-V3-Base shows competitive or better performance, and is especially good on BBH, MMLU-series, DROP, C-Eval, CMMLU, and CCPM. [p. 25-26]

Due to the efficient architectures and comprehensive engineering optimizations, DeepSeek-V3 achieves extremely high training efficiency. Under the training framework and infrastructures, training DeepSeek-V3 on each trillion tokens requires only 180K H800 GPU hours, which is much cheaper than training 72B or 405B dense models. [p. 26]

**Table 3** (p. 25): "Comparison among DeepSeek-V3-Base and other representative open-source base models. All models are evaluated with our internal evaluation framework and share the same evaluation setting. Scores with a gap not exceeding 0.3 are considered to be at the same level. DeepSeek-V3-Base achieves the best performance on most benchmarks, especially on math and code tasks."

| Benchmark (Metric) | # Shots | DeepSeek-V2 Base | Qwen2.5 72B Base | LLaMA-3.1 405B Base | DeepSeek-V3 Base |
|---|---|---|---|---|---|
| Architecture | - | MoE | Dense | Dense | MoE |
| # Activated Params | - | 21B | 72B | 405B | 37B |
| # Total Params | - | 236B | 72B | 405B | 671B |
| Pile-test (BPB) | - | 0.606 | 0.638 | 0.542 | 0.548 |
| BBH (EM) | 3-shot | 78.8 | 79.8 | 82.9 | 87.5 |
| MMLU (EM) | 5-shot | 78.4 | 85.0 | 84.4 | 87.1 |
| MMLU-Redux (EM) | 5-shot | 75.6 | 83.2 | 81.3 | 86.2 |
| MMLU-Pro (EM) | 5-shot | 51.4 | 58.3 | 52.8 | 64.4 |
| DROP (F1) | 3-shot | 80.4 | 80.6 | 86.0 | 89.0 |
| ARC-Easy (EM) | 25-shot | 97.6 | 98.4 | 98.4 | 98.9 |
| ARC-Challenge (EM) | 25-shot | 92.2 | 94.5 | 95.3 | 95.3 |
| **English** HellaSwag (EM) | 10-shot | 87.1 | 84.8 | 89.2 | 88.9 |
| PIQA (EM) | 0-shot | 83.9 | 82.6 | 85.9 | 84.7 |
| WinoGrande (EM) | 5-shot | 86.3 | 82.3 | 85.2 | 84.9 |
| RACE-Middle (EM) | 5-shot | 73.1 | 68.1 | 74.2 | 67.1 |
| RACE-High (EM) | 5-shot | 52.6 | 50.3 | 56.8 | 51.3 |
| TriviaQA (EM) | 5-shot | 80.0 | 71.9 | 82.7 | 82.9 |
| NaturalQuestions (EM) | 5-shot | 38.6 | 33.2 | 41.5 | 40.0 |
| AGIEval (EM) | 0-shot | 57.5 | 75.8 | 60.6 | 79.6 |
| HumanEval (Pass@1) | 0-shot | 43.3 | 53.0 | 54.9 | 65.2 |
| **Code** MBPP (Pass@1) | 3-shot | 65.0 | 72.6 | 68.4 | 75.4 |
| LiveCodeBench-Base (Pass@1) | 3-shot | 11.6 | 12.9 | 15.5 | 19.4 |
| CRUXEval-I (EM) | 2-shot | 52.5 | 59.1 | 58.5 | 67.3 |
| CRUXEval-O (EM) | 2-shot | 49.8 | 59.9 | 59.9 | 69.8 |
| GSM8K (EM) | 8-shot | 81.6 | 88.3 | 83.5 | 89.3 |
| **Math** MATH (EM) | 4-shot | 43.4 | 54.4 | 49.0 | 61.6 |
| MGSM (EM) | 8-shot | 65.6 | 76.2 | 69.9 | 79.8 |
| CMath (EM) | 3-shot | 78.7 | 84.5 | 77.3 | 90.7 |
| CLUEWSC (EM) | 5-shot | 82.0 | 82.5 | 83.0 | 82.7 |
| C-Eval (EM) | 5-shot | 81.4 | 89.2 | 72.5 | 90.1 |
| **Chinese** CMMLU (EM) | 5-shot | 84.0 | 89.5 | 73.7 | 88.8 |
| CMRC (EM) | 1-shot | 77.4 | 75.8 | 76.0 | 76.3 |
| C3 (EM) | 0-shot | 77.4 | 76.7 | 79.7 | 78.6 |
| CCPM (EM) | 0-shot | 93.0 | 88.5 | 78.6 | 92.0 |
| **Multilingual** MMMLU-non-English (EM) | 5-shot | 64.0 | 74.8 | 73.8 | 79.4 |

## 4.5. Discussion [p. 26]

### 4.5.1. Ablation Studies for Multi-Token Prediction [p. 26]

In Table 4, the ablation results for the MTP strategy are shown. To be specific, the MTP strategy is validated on top of two baseline models across different scales. At the small scale, a baseline MoE model comprising 15.7B total parameters on 1.33T tokens is trained. At the large scale, a baseline MoE model comprising 228.7B total parameters on 540B tokens is trained. On top of them, keeping the training data and the other architectures the same, a 1-depth MTP module is appended onto them and models with the MTP strategy are trained for comparison. Note that during inference, the MTP module is directly discarded, so the inference costs of the compared models are exactly the same. From the table, it can be observed that the MTP strategy consistently enhances the model performance on most of the evaluation benchmarks. [p. 26]

**Table 4** (p. 26): "Ablation results for the MTP strategy. The MTP strategy consistently enhances the model performance on most of the evaluation benchmarks."

| Benchmark (Metric) | # Shots | Small MoE Baseline | Small MoE w/ MTP | Large MoE Baseline | Large MoE w/ MTP |
|---|---|---|---|---|---|
| # Activated Params (Reference) | - | 2.4B | 2.4B | 20.9B | 20.9B |
| # Total Params (Reference) | - | 15.7B | 15.7B | 228.7B | 228.7B |
| # Training Tokens | - | 1.33T | 1.33T | 540B | 540B |
| Pile-test (BPB) | - | 0.729 | 0.729 | 0.658 | 0.657 |
| BBH (EM) | 3-shot | 39.0 | 41.4 | 70.0 | 70.7 |
| MMLU (EM) | 5-shot | 50.0 | 53.3 | 67.5 | 66.6 |
| DROP (F1) | 1-shot | 39.2 | 41.3 | 68.5 | 70.6 |
| TriviaQA (EM) | 5-shot | 56.9 | 57.7 | 67.0 | 67.3 |
| NaturalQuestions (EM) | 5-shot | 22.7 | 22.3 | 27.2 | 28.5 |
| HumanEval (Pass@1) | 0-shot | 20.7 | 26.8 | 44.5 | 53.7 |
| MBPP (Pass@1) | 3-shot | 35.8 | 36.8 | 61.6 | 62.2 |
| GSM8K (EM) | 8-shot | 25.4 | 31.4 | 72.3 | 74.0 |
| MATH (EM) | 4-shot | 10.7 | 12.6 | 38.6 | 39.8 |

### 4.5.2. Ablation Studies for the Auxiliary-Loss-Free Balancing Strategy [p. 26]

In Table 5, the ablation results for the auxiliary-loss-free balancing strategy are shown. This strategy is validated on top of two baseline models across different scales. At the small scale, a baseline MoE model comprising 15.7B total parameters on 1.33T tokens is trained. At the large scale, a baseline MoE model comprising 228.7B total parameters on 578B tokens is trained. [p. 26]

---
[p. 26–27 continued]

On top of them, keeping the training data and the other architectures the same, the auxiliary losses are removed and the auxiliary-loss-free balancing strategy is introduced for comparison. From the table, it can be observed that the auxiliary-loss-free strategy consistently achieves better model performance on most of the evaluation benchmarks. [p. 27]

**Table 5** (p. 27): "Ablation results for the auxiliary-loss-free balancing strategy. Compared with the purely auxiliary-loss-based method, the auxiliary-loss-free strategy consistently achieves better model performance on most of the evaluation benchmarks."

| Benchmark (Metric) | # Shots | Small MoE Aux-Loss-Based | Small MoE Aux-Loss-Free | Large MoE Aux-Loss-Based | Large MoE Aux-Loss-Free |
|---|---|---|---|---|---|
| # Activated Params | - | 2.4B | 2.4B | 20.9B | 20.9B |
| # Total Params | - | 15.7B | 15.7B | 228.7B | 228.7B |
| # Training Tokens | - | 1.33T | 1.33T | 578B | 578B |
| Pile-test (BPB) | - | 0.727 | 0.724 | 0.656 | 0.652 |
| BBH (EM) | 3-shot | 37.2 | 39.3 | 66.7 | 67.9 |
| MMLU (EM) | 5-shot | 51.0 | 51.8 | 68.3 | 67.2 |
| DROP (F1) | 1-shot | 38.1 | 39.0 | 67.1 | 67.1 |
| TriviaQA (EM) | 5-shot | 58.3 | 58.5 | 66.7 | 67.7 |
| NaturalQuestions (EM) | 5-shot | 23.2 | 23.4 | 27.1 | 28.1 |
| HumanEval (Pass@1) | 0-shot | 22.0 | 22.6 | 40.2 | 46.3 |
| MBPP (Pass@1) | 3-shot | 36.6 | 35.8 | 59.2 | 61.2 |
| GSM8K (EM) | 8-shot | 27.1 | 29.6 | 70.7 | 74.5 |
| MATH (EM) | 4-shot | 10.9 | 11.1 | 37.2 | 39.6 |

Both of the baseline models purely use auxiliary losses to encourage load balance, and use the sigmoid gating function on top. Their hyper-parameters to control the strength of auxiliary losses are the same as DeepSeek-V2-Lite and DeepSeek-V2, respectively. On top of these two baseline models, keeping the training data and the other architectures the same, the auxiliary losses are removed and the auxiliary-loss-free balancing strategy is introduced for comparison. From the table, it can be observed that the auxiliary-loss-free strategy consistently achieves better model performance on most of the evaluation benchmarks. [p. 27]

### 4.5.3. Batch-Wise Load Balance VS. Sequence-Wise Load Balance [p. 27]

The key distinction between auxiliary-loss-free balancing and sequence-wise auxiliary loss lies in their balancing scope: batch-wise versus sequence-wise. Compared with the sequence-wise auxiliary loss, batch-wise balancing imposes a more flexible constraint, as it does not enforce in-domain balance on each sequence. This flexibility allows experts to better specialize in different domains. To validate this, the expert load of a 16B auxiliary-loss-based baseline and a 16B auxiliary-loss-free model on different domains in the Pile test set is recorded and analyzed. As illustrated in Figure 9, it can be observed that the auxiliary-loss-free model demonstrates greater expert specialization patterns as expected. [p. 27]

To further investigate the correlation between this flexibility and the advantage in model performance, a batch-wise auxiliary loss that encourages load balance on each training batch instead of each sequence is additionally designed and validated. The experimental results show that, when achieving a similar level of batch-wise load balance, the batch-wise auxiliary loss can also achieve similar model performance to the auxiliary-loss-free method. To be specific, in the experiments with 1B MoE models, the validation losses are: 2.258 (using a sequence-wise auxiliary loss), 2.253 (using the auxiliary-loss-free method), and 2.253 (using a batch-wise auxiliary loss). Also observe similar results on 3B MoE models: the model using a sequence-wise auxiliary loss achieves a validation loss of 2.085, and the models using the auxiliary-loss-free method or a batch-wise auxiliary loss achieve the same validation loss of 2.080. [p. 27]

In addition, although the batch-wise load balancing methods show consistent performance advantages, they also face two potential challenges in efficiency: (1) load imbalance within certain sequences or small batches, and (2) domain-shift-induced load imbalance during inference. The first challenge is naturally addressed by the training framework that uses large-scale expert parallelism and data parallelism, which guarantees a large size of each micro-batch. For the second challenge, an efficient inference framework with redundant expert deployment is also designed and implemented, as described in Section 3.4, to overcome it. [p. 27-28]

**Figure 9** (p. 28): "Expert load of auxiliary-loss-free and auxiliary-loss-based models on three domains in the Pile test set. The auxiliary-loss-free model shows greater expert specialization patterns than the auxiliary-loss-based one. The relative expert load denotes the ratio between the actual expert load and the theoretically balanced expert load. Due to space constraints, we only present the results of two layers as an example, with the results of all layers provided in Appendix C."

Description: Heatmap visualization
- Key elements: Four horizontal heatmaps showing expert load patterns for "Aux-Loss-Based Layer 9", "Aux-Loss-Free Layer 9", "Aux-Loss-Based Layer 18", and "Aux-Loss-Free Layer 18". Each heatmap has three rows labeled "Wikipedia (en) -", "Github -", "DM Mathematics -". The x-axis shows expert numbers (numbered 1-64 with detailed labels). The color scale shows "Relative Expert Load" from 0 to 10, where yellow represents balanced load (~1-2), orange represents moderate load (~4-6), and red represents high load (~8-10).
- Notable patterns: The Aux-Loss-Free models show strong red concentrations (high specialization) in specific experts for each domain, particularly visible in Layer 9 and Layer 18. For example, in Aux-Loss-Free Layer 9, DM Mathematics shows concentrated red spikes around specific expert indices. In contrast, Aux-Loss-Based models show more uniform yellow coloring with less pronounced specialization patterns.
- Supports claim: The auxiliary-loss-free model demonstrates greater expert specialization patterns compared to the auxiliary-loss-based model, as experts more strongly specialize in specific domains [p. 27]
