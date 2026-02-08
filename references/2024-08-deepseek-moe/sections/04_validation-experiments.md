# 4. Validation Experiments [p. 7–11]

## 4.1. Experimental Setup

### 4.1.1. Training Data and Tokenization

[p. 7–8] Training data is sampled from a large-scale multilingual corpus created by DeepSeek-AI. The corpus primarily focuses on English and Chinese but also encompasses other languages. It is derived from diverse sources, including web text, mathematical material, coding scripts, published literature, and various other textual materials. For the purpose of validation experiments, a subset containing 100B tokens is sampled from the corpus.

[p. 8] For tokenization, the HuggingFace Tokenizer^2 tools are used to train byte pair encoding (BPE) (Sennrich et al., 2016) tokenizers on a smaller subset of the training corpus. In the validation experiments, a tokenizer with a vocabulary size of 8K is prepared, and the vocabulary size will be scaled up when training larger models.

^2 https://github.com/huggingface/tokenizers

### 4.1.2. Infrastructures

[p. 8] Experiments are conducted based on HAI-LLM (High-Flyer, 2023), an efficient and light-weight training framework which integrates multiple parallelism strategies, including tensor parallelism (Korthikanti et al., 2023; Narayanan et al., 2021; Shoeybi et al., 2019), ZeRO data parallelism (Rajbhandari et al., 2020), PipeDream pipeline parallelism (Harlap et al., 2018), and more specifically, expert parallelism (Lepikhin et al., 2021) by combining data and tensor parallelism. To optimize performance, GPU kernels are developed with CUDA and Triton (Tillet et al., 2019) for gating algorithms and fusing computations across linear layers in different experts.

[p. 8] All experiments are carried out on clusters equipped with NVIDIA A100 or H800 GPUs. Each node in the A100 cluster contains 8 GPUs connected pairwise via the NVLink bridge. The H800 cluster also features 8 GPUs per node, interconnected using NVLink and NVSwitch within nodes. For both A100 and H800 clusters, InfiniBand interconnects are utilized to facilitate communication across nodes.

### 4.1.3. Hyper-Parameters

**Model Settings.** [p. 8] In the validation experiments:
- Number of Transformer layers: 9
- Hidden dimension: 1280
- Multi-head attention: 10 heads, each head dimension 128
- Initialization: all learnable parameters randomly initialized with a standard deviation of 0.006
- All FFNs are substituted with MoE layers
- Total number of expert parameters equals 16 times that of a standard FFN
- Activated expert parameters (including shared expert parameters and activated routed expert parameters): 2 times that of a standard FFN
- Under this configuration, each MoE model has approximately 2B total parameters, with the number of activated parameters around 0.3B

**Training Settings.** [p. 8]
- Optimizer: AdamW (Loshchilov and Hutter, 2019)
- Hyper-parameters: $\beta_1 = 0.9$, $\beta_2 = 0.95$, weight_decay $= 0.1$
- Learning rate schedule: warmup-and-step-decay strategy
  - Linear increase from 0 to maximum value during first 2K steps
  - Multiplied by 0.316 at 80% of training steps
  - Multiplied by 0.316 again at 90% of training steps
- Maximum learning rate for validation experiments: $1.08 \times 10^{-3}$
- Gradient clipping norm: 1.0
- Batch size: 2K
- Maximum sequence length: 2K
- Each training batch contains 4M tokens
- Total number of training steps: 25,000 (to achieve 100B training tokens)
- No dropout used during training
- All parameters (including expert parameters) deployed on a single GPU device to avoid unbalanced computation
- No tokens dropped during training; device-level balance loss not employed

[p. 9] Expert-level balance factor set to $\alpha_1 = 0.01$ to prevent routing collapse.

[p. 9] An overview table of hyper-parameters for DeepSeekMoE across different sizes is provided in Appendix A.

### 4.1.4. Evaluation Benchmarks

[p. 9] Evaluations are conducted on a wide range of benchmarks covering various types of tasks:

**Language Modeling.** Models evaluated on the test set of Pile (Gao et al., 2020), with the evaluation metric being cross-entropy loss.

**Language Understanding and Reasoning.** HellaSwag (Zellers et al., 2019), PIQA (Bisk et al., 2020), ARC-challenge and ARC-easy (Clark et al., 2018). Evaluation metric: accuracy.

**Reading Comprehension.** RACE-high and RACE-middle (Lai et al., 2017). Evaluation metric: accuracy.

**Code Generation.** HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021). Evaluation metric: Pass@1 (pass rate for only one generation attempt).

**Closed-Book Question Answering.** TriviaQA (Joshi et al., 2017) and NaturalQuestions (Kwiatkowski et al., 2019). Evaluation metric: Exactly Matching (EM) rate.

## 4.2. Evaluations

### Baselines

[p. 9] Five models are compared for validation experiments:

- **Dense**: standard dense Transformer language model with 0.2B total parameters.
- **Hash Layer** (Roller et al., 2021): MoE architecture based on top-1 hash routing, with 2.0B total parameters and 0.2B activated parameters, aligned with the dense baseline.
- **Switch Transformer** (Fedus et al., 2021): well-known MoE architecture based on top-1 learnable routing, with total parameters and activated parameters the same as Hash Layer.
- **GShard** (Lepikhin et al., 2021): employs a top-2 learnable routing strategy, with 2.0B total parameters and 0.3B activated parameters (one more expert is activated compared to top-1 routing methods).
- **DeepSeekMoE**: has 1 shared expert and 63 routed experts, where each expert is 0.25 times the size of a standard FFN. Including DeepSeekMoE, all compared models share the same training corpus and training hyper-parameters. All compared MoE models have the same number of total parameters, and GShard has the same number of activated parameters as DeepSeekMoE.

### Results

[p. 9–10] Evaluation results are presented in Table 1. All demonstrated models are evaluated after training on 100B tokens.

**Table 1** (p. 10): Evaluation results for validation experiments. **Bold** font indicates the best. Compared with other MoE architectures, DeepSeekMoE exhibits a substantial performance advantage.

| Metric | # Shot | Dense | Hash Layer | Switch | GShard | DeepSeekMoE |
|---|---|---|---|---|---|---|
| # Total Params | N/A | 0.2B | 2.0B | 2.0B | 2.0B | 2.0B |
| # Activated Params | N/A | 0.2B | 0.2B | 0.2B | 0.3B | 0.3B |
| FLOPs per 2K Tokens | N/A | 2.9T | 2.9T | 2.9T | 4.3T | 4.3T |
| # Training Tokens | N/A | 100B | 100B | 100B | 100B | 100B |
| Pile (Loss) | N/A | 2.060 | 1.932 | 1.881 | 1.867 | **1.808** |
| HellaSwag (Acc.) | 0-shot | 38.8 | 46.2 | 49.1 | 50.5 | **54.8** |
| PIQA (Acc.) | 0-shot | 66.8 | 68.4 | 70.5 | 70.6 | **72.3** |
| ARC-easy (Acc.) | 0-shot | 41.0 | 45.3 | 45.9 | 43.9 | **49.4** |
| ARC-challenge (Acc.) | 0-shot | 26.0 | 28.2 | 30.2 | 31.6 | **34.3** |
| RACE-middle (Acc.) | 5-shot | 38.8 | 38.8 | 43.6 | 42.1 | **44.0** |
| RACE-high (Acc.) | 5-shot | 29.0 | 30.0 | 30.9 | 30.4 | **31.7** |
| HumanEval (Pass@1) | 0-shot | 0.0 | 1.2 | 2.4 | 3.7 | **4.9** |
| MBPP (Pass@1) | 3-shot | 0.2 | 0.6 | 0.4 | 0.2 | **2.2** |
| TriviaQA (EM) | 5-shot | 4.9 | 6.5 | 8.9 | 10.2 | **16.6** |
| NaturalQuestions (EM) | 5-shot | 1.4 | 1.4 | 2.5 | 3.2 | **5.7** |

Key observations from Table 1 [p. 10]:
1. With sparse architectures and more total parameters, Hash Layer and Switch Transformer achieve significantly stronger performance than the dense baseline with the same number of activated parameters.
2. Compared with Hash Layer and Switch Transformer, GShard has more activated parameters and achieves slightly better performance than Switch Transformer.
3. With the same number of total parameters and activated parameters, DeepSeekMoE demonstrates overwhelming advantages over GShard. These results showcase the superiority of the DeepSeekMoE architecture within the existing landscape of MoE architectures.

## 4.3. DeepSeekMoE Aligns Closely with the Upper Bound of MoE Models

[p. 10] Having demonstrated that DeepSeekMoE outperforms the dense baseline and other MoE architectures, comparisons with larger baselines (more total parameters or activated parameters) are provided to give a more precise understanding of the performance of DeepSeekMoE. These comparisons enable estimation of the required model size of GShard or dense baselines to achieve equivalent performance to DeepSeekMoE.

### Comparison with GShard x1.5

[p. 10] Table 2 shows the comparison between DeepSeekMoE and a larger GShard model with 1.5 times the expert size, which results in 1.5 times both expert parameters and expert computation. Overall, DeepSeekMoE achieves comparable performance with GShard x1.5, underscoring the significant advantage inherent in the DeepSeekMoE architecture. In addition to the comparison with GShard x1.5, the comparison with GShard x1.2 is also shown in Appendix B.

[p. 10] Furthermore, when the number of total parameters of DeepSeekMoE is increased to 13.3B and compared with GShard x1.2 and GShard x1.5 with 15.9B and 19.8B total parameters, respectively, DeepSeekMoE can even outperform GShard x1.5 distinctly. These results are also provided in Appendix B.

### Comparison with Dense x16

[p. 11] Table 2 also shows the comparison between DeepSeekMoE and larger dense models. For a fair comparison, the widely used ratio (1:2) between the attention and FFN parameters is not used. Instead, 16 shared experts are configured where each expert has the same number of parameters as a standard FFN. This architecture mimics a dense model with 16 times standard FFN parameters. From the table, DeepSeekMoE nearly approaches the performance of Dense x16, which sets the strict upper bound of MoE models in terms of the model capacity.

> "at least at the scale of about 2B parameters and 100B training tokens, the performance of DeepSeekMoE aligns closely with the theoretical upper bound of MoE models" [p. 11]

Also, additional comparisons with Dense x4 are provided in Appendix B.

**Table 2** (p. 11): Comparisons among DeepSeekMoE, larger GShard models, and larger dense models. In the line of "# Experts", $a + b$ denotes $a$ shared and $b$ routed experts. In the line of "# Activated Experts", $a + b$ denotes $a$ activated shared experts and $b$ activated routed experts.

| Metric | # Shot | GShard x1.5 | Dense x16 | DeepSeekMoE |
|---|---|---|---|---|
| Relative Expert Size | N/A | 1.5 | 1 | 0.25 |
| # Experts | N/A | 0 + 16 | 16 + 0 | 1 + 63 |
| # Activated Experts | N/A | 0 + 2 | 16 + 0 | 1 + 7 |
| # Total Expert Params | N/A | 2.83B | 1.89B | 1.89B |
| # Activated Expert Params | N/A | 0.35B | 1.89B | 0.24B |
| FLOPs per 2K Tokens | N/A | 5.8T | 24.6T | 4.3T |
| # Training Tokens | N/A | 100B | 100B | 100B |
| Pile (Loss) | N/A | 1.808 | 1.806 | 1.808 |
| HellaSwag (Acc.) | 0-shot | 54.4 | 55.1 | 54.8 |
| PIQA (Acc.) | 0-shot | 71.1 | 71.9 | 72.3 |
| ARC-easy (Acc.) | 0-shot | 47.3 | 51.9 | 49.4 |
| ARC-challenge (Acc.) | 0-shot | 34.1 | 33.8 | 34.3 |
| RACE-middle (Acc.) | 5-shot | 46.4 | 46.3 | 44.0 |
| RACE-high (Acc.) | 5-shot | 32.4 | 33.0 | 31.7 |
| HumanEval (Pass@1) | 0-shot | 3.0 | 4.3 | 4.9 |
| MBPP (Pass@1) | 3-shot | 2.6 | 2.2 | 2.2 |
| TriviaQA (EM) | 5-shot | 15.7 | 16.5 | 16.6 |
| NaturalQuestions (EM) | 5-shot | 4.7 | 6.3 | 5.7 |

DeepSeekMoE achieves comparable performance with a GShard model containing 1.5 times expert parameters and computation. In addition, DeepSeekMoE nearly approaches the performance of a dense model with 16 times FFN parameters, which sets the upper bound for MoE models in terms of the model capacity.

## 4.4. Ablation Studies

[p. 11–12] In order to substantiate the effectiveness of the fine-grained expert segmentation and shared expert isolation strategies, ablation studies for DeepSeekMoE are conducted and the results are presented in Figure 3. For a fair comparison, all models included in the comparison have the same number of total parameters and activated parameters.

**Figure 3** (p. 12): "Ablation studies for DeepSeekMoE. The performance is normalized by the best performance for clarity in presentation. All compared models have the same number of parameters and activated parameters. We can find that fine-grained expert segmentation and shared expert isolation both contribute to stronger overall performance."

- X-axis: Metrics (HellaSwag, PIQA, ARC-easy, ARC-challenge, TriviaQA, NaturalQuestions)
- Y-axis: Normalized Performance (range ~0.5 to 1.2)
- Four configurations compared (bar chart):
  1. 0 shared expert + 2 out of 16 routed experts (GShard) — lowest performance across most benchmarks
  2. 1 shared expert + 1 out of 15 routed experts (+ shared expert isolation) — improvement over GShard on most benchmarks
  3. 1 shared expert + 3 out of 31 routed experts (+ fine-grained expert segmentation) — further improvement
  4. 1 shared expert + 7 out of 63 routed experts (+ finer expert segmentation) — best performance (the full DeepSeekMoE configuration)
- The figure shows a consistent trend: each incremental strategy (shared expert isolation, then progressively finer segmentation) improves performance.

### Shared Expert Isolation

[p. 12] To evaluate the influence of the shared expert isolation strategy, one expert is isolated as the shared one based on GShard. From Figure 3, compared with GShard, the intentional isolation of a shared expert yields improved performance across a majority of benchmarks. These results support the proposition that the shared expert isolation strategy contributes to a stronger model performance.

### Fine-Grained Expert Segmentation

[p. 12] To assess the effectiveness of the fine-grained expert segmentation strategy, a more detailed comparison is conducted by further segmenting the experts into a finer grain. Specifically, each expert is segmented into 2 or 4 smaller experts, resulting in a total of 32 (1 shared + 31 routed) or 64 (1 shared + 63 routed) experts. Figure 3 reveals a consistent trend that the continuous refinement of expert segmentation granularity corresponds to a continuous enhancement in overall model performance. These findings provide empirical substantiation for the effectiveness of the fine-grained expert segmentation strategy.

### Ratios Between Shared and Routed Experts

[p. 12] The best ratio of shared experts and routed experts is investigated. Based on the finest granularity with 64 total experts and keeping the number of total experts and activated experts constant, the authors attempt to isolate 1, 2, and 4 experts as shared ones. Different ratios of the shared experts and routed experts do not significantly impact the performance, and 1, 2, and 4 shared experts achieve a Pile loss of 1.808, 1.806, and 1.811, respectively. Considering that the ratio of 1:3 yields a marginally better Pile loss, when scaling up DeepSeekMoE, the ratio between shared experts and activated routed experts is kept as 1:3.
