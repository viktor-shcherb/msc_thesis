# 2 Pretraining [p. 5-6]

[p. 5] To create the Llama 2 family, the authors began with the pretraining approach described in Touvron et al. (2023), using an optimized auto-regressive transformer, but made several changes to improve performance. Specifically: more robust data cleaning, updated data mixes, trained on 40% more total tokens, doubled the context length, and used grouped-query attention (GQA) to improve inference scalability for larger models.

**Figure 4** (p. 5): "Training of Llama 2-Chat."

Flow diagram showing the training pipeline: Pretraining data feeds into self-supervised learning to produce Llama 2. Then supervised fine-tuning produces an initial Llama-2-chat. Subsequently, the model is iteratively refined using RLHF, specifically through rejection sampling and Proximal Policy Optimization (PPO). Human preference data feeds into a Safety Reward Model and a Helpful Reward Model. Throughout the RLHF stage, the accumulation of iterative reward modeling data in parallel with model enhancements is crucial to ensure the reward models remain within distribution.

## 2.1 Pretraining Data

[p. 5] The training corpus includes a new mix of data from publicly available sources, which does not include data from Meta's products or services. An effort was made to remove data from sites known to contain a high volume of personal information about private individuals. They trained on 2 trillion tokens of data, up-sampling the most factual sources in an effort to increase knowledge and dampen hallucinations, as this provides a good performance-cost trade-off.

[p. 5] A variety of pretraining data investigations were performed so that users can better understand the potential capabilities and limitations of the models; results can be found in Section 4.1.

## 2.2 Training Details

[p. 5] The authors adopt most of the pretraining setting and model architecture from Llama 1. Architecture details:
- Standard transformer architecture (Vaswani et al., 2017)
- Pre-normalization using RMSNorm (Zhang and Sennrich, 2019)
- SwiGLU activation function (Shazeer, 2020)
- Rotary positional embeddings (RoPE, Su et al. 2022)

Primary architectural differences from Llama 1: increased context length and grouped-query attention (GQA). Ablation experiments detailed in Appendix Section A.2.1.

**Table 1** (p. 6): "Llama 2 family of models." Token counts refer to pretraining data only. All models are trained with a global batch-size of 4M tokens. Bigger models -- 34B and 70B -- use Grouped-Query Attention (GQA) for improved inference scalability.

| Model | Training Data | Params | Context Length | GQA | Tokens | LR |
|---|---|---|---|---|---|---|
| Llama 1 | *See Touvron et al. (2023)* | 7B | 2k | ✗ | 1.0T | 3.0 x 10^-4 |
| Llama 1 | | 13B | 2k | ✗ | 1.0T | 3.0 x 10^-4 |
| Llama 1 | | 33B | 2k | ✗ | 1.4T | 1.5 x 10^-4 |
| Llama 1 | | 65B | 2k | ✗ | 1.4T | 1.5 x 10^-4 |
| Llama 2 | *A new mix of publicly available online data* | 7B | 4k | ✗ | 2.0T | 3.0 x 10^-4 |
| Llama 2 | | 13B | 4k | ✗ | 2.0T | 3.0 x 10^-4 |
| Llama 2 | | 34B | 4k | ✓ | 2.0T | 1.5 x 10^-4 |
| Llama 2 | | 70B | 4k | ✓ | 2.0T | 1.5 x 10^-4 |

### Hyperparameters

[p. 5] Training used the AdamW optimizer (Loshchilov and Hutter, 2017), with beta_1 = 0.9, beta_2 = 0.95, eps = 10^-5. Cosine learning rate schedule with warmup of 2000 steps, decaying the final learning rate down to 10% of the peak learning rate. Weight decay of 0.1 and gradient clipping of 1.0. Figure 5 (a) shows the training loss for Llama 2 with these hyperparameters.

**Figure 5** (p. 6): "Training Loss for Llama 2 models. We compare the training loss of the Llama 2 family of models. We observe that after pretraining on 2T Tokens, the models still did not show any sign of saturation."

Line chart showing Train PPL (y-axis, range ~1.4-2.2) vs. Processed Tokens in Billions (x-axis, 0-2000). Four lines for Llama-2 7B (red), 13B (blue), 34B (green), 70B (purple/pink). All models show smooth decreasing loss curves with no sign of saturation at 2T tokens. The text on p. 5 references this as "Figure 5 (a)", indicating the full Figure 5 may have additional panels on later pages.

### Tokenizer

[p. 6] Same tokenizer as Llama 1: bytepair encoding (BPE) algorithm (Sennrich et al., 2016) using the SentencePiece implementation (Kudo and Richardson, 2018). As with Llama 1, all numbers are split into individual digits, and bytes are used to decompose unknown UTF-8 characters. Total vocabulary size is 32k tokens.

## 2.2.1 Training Hardware & Carbon Footprint

[p. 6] Models pretrained on Meta's Research Super Cluster (RSC) (Lee and Sengupta, 2022) as well as internal production clusters. Both clusters use NVIDIA A100s. Two key differences between clusters:

1. **Interconnect type:** RSC uses NVIDIA Quantum InfiniBand; production cluster uses RoCE (RDMA over converged Ethernet) solution based on commodity ethernet switches. Both solutions interconnect at 200 Gbps end-points.
2. **Per-GPU power consumption cap:** RSC uses 400W; production cluster uses 350W.

With this two-cluster setup, the authors were able to compare the suitability of these different types of interconnect for large-scale training. RoCE (a more affordable, commercial interconnect network) can scale almost as well as expensive InfiniBand up to 2000 GPUs, which makes pretraining even more democratizable.

---
[p. 7 continued]

**Carbon Footprint of Pretraining.** Following preceding research (Bender et al., 2021a; Patterson et al., 2021; Wu et al., 2022; Dodge et al., 2022), the authors use power consumption estimates of GPU devices and carbon efficiency to calculate carbon emissions from pretraining the Llama 2 models. Actual GPU power usage depends on utilization and is likely to vary from Thermal Design Power (TDP), which is used as an estimation for GPU power. The calculations do not account for further power demands such as interconnect or non-GPU server power consumption, nor datacenter cooling systems. Additionally, the carbon output related to the production of AI hardware, like GPUs, could add to the overall carbon footprint as suggested by Gupta et al. (2022b,a).

**Table 2** (p. 7): "CO_2 emissions during pretraining." Time: total GPU time required for training each model. Power Consumption: peak power capacity per GPU device for the GPUs used adjusted for power usage efficiency. 100% of the emissions are directly offset by Meta's sustainability program, and because they are openly releasing these models, the pretraining costs do not need to be incurred by others.

| Model | Size | Time (GPU hours) | Power Consumption (W) | Carbon Emitted (tCO_2eq) |
|---|---|---|---|---|
| Llama 2 | 7B | 184320 | 400 | 31.22 |
| Llama 2 | 13B | 368640 | 400 | 62.44 |
| Llama 2 | 34B | 1038336 | 350 | 153.90 |
| Llama 2 | 70B | 1720320 | 400 | 291.42 |
| Total | | 3311616 | | 539.00 |

A cumulative of 3.3M GPU hours of computation was performed on hardware of type A100-80GB (TDP of 400W or 350W). Total emissions estimated at **539 tCO_2eq**, of which 100% were directly offset by Meta's sustainability program. The open release strategy means pretraining costs will not need to be incurred by other companies, saving more global resources.

## 2.3 Llama 2 Pretrained Model Evaluation [p. 7-8]

[p. 7] Results reported for Llama 1 and Llama 2 base models, MosaicML Pretrained Transformer (MPT), and Falcon (Almazrouei et al., 2023) models on standard academic benchmarks. All evaluations use Meta's internal evaluations library. Results for MPT and Falcon models are reproduced internally. For these models, the best score between their own evaluation framework and any publicly reported results is always picked.

Table 3 summarizes overall performance across a suite of popular benchmarks. Safety benchmarks are shared in Section 4.1. The benchmarks are grouped into the following categories (results for all individual benchmarks available in Section A.2.2):

- **Code.** Average pass@1 scores on HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021).
- **Commonsense Reasoning.** Average of PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), HellaSwag (Zellers et al., 2019a), WinoGrande (Sakaguchi et al., 2021), ARC easy and challenge (Clark et al., 2018), OpenBookQA (Mihaylov et al., 2018), and CommonsenseQA (Talmor et al., 2018). 7-shot results for CommonsenseQA and 0-shot results for all other benchmarks.
- **World Knowledge.** 5-shot performance on NaturalQuestions (Kwiatkowski et al., 2019) and TriviaQA (Joshi et al., 2017); report the average.
- **Reading Comprehension.** 0-shot average on SQuAD (Rajpurkar et al., 2018), QuAC (Choi et al., 2018), and BoolQ (Clark et al., 2019).
- **MATH.** Average of GSM8K (8 shot) (Cobbe et al., 2021) and MATH (4 shot) (Hendrycks et al., 2021) benchmarks at *top 1*.
- **Popular Aggregated Benchmarks.** Overall results for MMLU (5 shot) (Hendrycks et al., 2020), Big Bench Hard (BBH) (3 shot) (Suzgun et al., 2022), and AGI Eval (3-5 shot) (Zhong et al., 2023). For AGI Eval, only English tasks evaluated; report the average.

**Table 3** (p. 8): "Overall performance on grouped academic benchmarks compared to open-source base models."

| Model | Size | Code | Commonsense Reasoning | World Knowledge | Reading Comprehension | Math | MMLU | BBH | AGI Eval |
|---|---|---|---|---|---|---|---|---|---|
| MPT | 7B | 20.5 | 57.4 | 41.0 | 57.5 | 4.9 | 26.8 | 31.0 | 23.5 |
| MPT | 30B | 28.9 | 64.9 | 50.0 | 64.7 | 9.1 | 46.9 | 38.0 | 33.8 |
| Falcon | 7B | 5.6 | 56.1 | 42.8 | 36.0 | 4.6 | 26.2 | 28.0 | 21.2 |
| Falcon | 40B | 15.2 | 69.2 | 56.7 | 65.7 | 12.6 | 55.4 | 37.1 | 37.0 |
| Llama 1 | 7B | 14.1 | 60.8 | 46.2 | 58.5 | 6.95 | 35.1 | 30.3 | 23.9 |
| Llama 1 | 13B | 18.9 | 66.1 | 52.6 | 62.3 | 10.9 | 46.9 | 37.0 | 33.9 |
| Llama 1 | 33B | 26.0 | 70.0 | 58.4 | 67.6 | 21.4 | 57.8 | 39.8 | 41.7 |
| Llama 1 | 65B | 30.7 | 70.7 | 60.5 | 68.6 | 30.8 | 63.4 | 43.5 | 47.6 |
| Llama 2 | 7B | 16.8 | 63.9 | 48.9 | 61.3 | 14.6 | 45.3 | 32.6 | 29.3 |
| Llama 2 | 13B | 24.5 | 66.9 | 55.4 | 65.8 | 28.7 | 54.8 | 39.4 | 39.1 |
| Llama 2 | 34B | 27.8 | 69.9 | 58.7 | 68.0 | 24.2 | 62.6 | 44.1 | 43.4 |
| Llama 2 | 70B | **37.5** | **71.9** | **63.6** | **69.4** | **35.2** | **68.9** | **51.2** | **54.2** |

[p. 8] Llama 2 models outperform Llama 1 models. In particular, Llama 2 70B improves the results on MMLU and BBH by approximately 5 and approximately 8 points, respectively, compared to Llama 1 65B. Llama 2 7B and 30B models outperform MPT models of the corresponding size on all categories besides code benchmarks. For the Falcon models, Llama 2 7B and 34B outperform Falcon 7B and 40B models on all categories of benchmarks. Additionally, Llama 2 70B model outperforms all open-source models.

[p. 8] Comparison to closed-source models: as shown in Table 4, Llama 2 70B is close to GPT-3.5 (OpenAI, 2023) on MMLU and GSM8K, but there is a significant gap on coding benchmarks. Llama 2 70B results are on par or better than PaLM (540B) (Chowdhery et al., 2022) on almost all benchmarks. There is still a large gap in performance between Llama 2 70B and GPT-4 and PaLM-2-L.

**Table 4** (p. 8): "Comparison to closed-source models on academic benchmarks." Results for GPT-3.5 and GPT-4 are from OpenAI (2023). Results for PaLM are from Chowdhery et al. (2022). Results for PaLM-2-L are from Anil et al. (2023).

| Benchmark (shots) | GPT-3.5 | GPT-4 | PaLM | PaLM-2-L | Llama 2 |
|---|---|---|---|---|---|
| MMLU (5-shot) | 70.0 | **86.4** | 69.3 | 78.3 | 68.9 |
| TriviaQA (1-shot) | -- | -- | 81.4 | **86.1** | 85.0 |
| Natural Questions (1-shot) | -- | -- | 29.3 | **37.5** | 33.0 |
| GSM8K (8-shot) | 57.1 | **92.0** | 56.5 | 80.7 | 56.8 |
| HumanEval (0-shot) | 48.1 | **67.0** | 26.2 | -- | 29.9 |
| BIG-Bench Hard (3-shot) | -- | -- | 52.3 | **65.7** | 51.2 |

[p. 8] The authors also analyzed potential data contamination and share details in Section A.6.
