# 7. DeepSeekMoE 145B Ongoing [p. 21–23]

[p. 21] Encouraged by the outstanding performance of DeepSeekMoE 16B, the authors further undertake a preliminary endeavor to scale up DeepSeekMoE to 145B. In this initial study, DeepSeekMoE 145B is trained on 245B tokens, but it has demonstrated consistent advantages over the GShard architecture and shown promise to match or exceed the performance of DeepSeek 67B (Dense). Furthermore, upon the completion of the final version and full training of DeepSeekMoE 145B, the authors plan to make it publicly available.

## 7.1. Experimental Setup

### Training Data and Tokenization

[p. 21] For DeepSeekMoE 145B, the same training corpus and tokenizer as DeepSeekMoE 16B are used, with the only difference being that DeepSeekMoE 145B is trained on 245B tokens for an initial study.

### Model Settings

[p. 21] For DeepSeekMoE 145B:
- Number of Transformer layers: 62
- Hidden dimension: 4096
- Multi-head attention: 32 heads, each head dimension 128
- Initialization: all learnable parameters randomly initialized with a standard deviation of 0.006
- As in DeepSeekMoE 16B, all FFNs substituted with MoE layers except for the first layer
- Each MoE layer consists of 4 shared experts and 128 routed experts, where each expert is 0.125 times the size of a standard FFN
- Each token is routed to these 4 shared experts and 12 out of 128 routed experts
- Under this configuration, DeepSeekMoE 145B has approximately 144.6B total parameters, with the number of activated parameters around 22.2B

### Training Settings

[p. 21–22] Training details for DeepSeekMoE 145B:
- Optimizer: AdamW (Loshchilov and Hutter, 2019)
- Hyper-parameters: $\beta_1 = 0.9$, $\beta_2 = 0.95$, weight_decay $= 0.1$
- Learning rate schedule: warmup-and-constant strategy
  - Linear increase from 0 to maximum value during first 2K steps
  - Then kept constant for the remainder of training
- Maximum learning rate: $3.0 \times 10^{-4}$
- Gradient clipping norm: 1.0
- Batch size: 4.5K
- Maximum sequence length: 4K
- Each training batch contains 18M tokens
- Training steps: 13,000 steps, achieving 245B training tokens
- No dropout used during training
- Pipeline parallelism used to deploy different layers of a model on different devices
- For each layer, all routed experts uniformly deployed on 4 devices (expert parallelism combined with data parallelism)
- Since expert parallelism is employed, device-level load balance must be considered to reduce computational bottleneck
- Device-level balance factor: 0.05 (to encourage balanced computation across devices)
- Expert-level balance factor: 0.003 (to prevent routing collapse)

### Evaluation Benchmarks

[p. 22] DeepSeekMoE 145B is evaluated on exactly the same internal benchmarks as used for DeepSeekMoE 16B (see Section 5.1.3).

## 7.2. Evaluations

### Baselines

[p. 22] Apart from DeepSeekMoE 145B, three additional models are considered for comparison:
- **DeepSeek 67B (Dense):** a dense model with 67.4B total parameters (refer to DeepSeek-AI (2024) for the model and training details).
- **GShard 137B:** shares the same hidden dimension and number of layers as DeepSeekMoE 145B, but follows the GShard architecture. Note that DeepSeekMoE 145B aligns the intermediate hidden dimension in each expert to a multiple of 64 for computation efficiency, so its model size is 6% larger than GShard 137B.
- **DeepSeekMoE 142B (Half Activated):** has a similar architecture to DeepSeekMoE 145B, but it contains only 2 shared experts, and only 6 out of 128 routed experts are activated.

All compared models, including DeepSeekMoE 145B, share the same training corpus. All MoE models in the comparison are trained from scratch and share the same training hyper-parameters.

### Results

[p. 22–23] From the evaluation results presented in Table 6, the following observations are made:

1. Despite having comparable total parameters and computations, DeepSeekMoE 145B significantly outperforms GShard 137B, highlighting the advantages of the DeepSeekMoE architecture again.
2. On the whole, with only 28.5% of computations, DeepSeekMoE 145B achieves comparable performance with DeepSeek 67B (Dense). Consistent with the findings from DeepSeekMoE 16B, DeepSeekMoE 145B exhibits remarkable strengths in language modeling and knowledge-intensive tasks, but with limitations in multiple-choice tasks.
3. At a larger scale, the performance of DeepSeekMoE 142B (Half Activated) does not lag behind too much from DeepSeekMoE 145B. In addition, despite having only a half of activated expert parameters, DeepSeekMoE 142B (Half Activated) still matches the performance of DeepSeek 67B (Dense), with only 18.2% of computations. It also outperforms GShard 137B, which aligns with the conclusion from Section 4.5.

**Table 6** (p. 23): Comparison among DeepSeek 67B (Dense) and MoE models at the scale of about 140B total parameters. In the lines of "# Experts" and "# Activated Experts", $a + b$ denotes $a$ shared experts and $b$ routed experts, respectively. **Bold** font indicates the best or near the best performance excluding the last column.

| Metric | # Shot | DeepSeek 67B (Dense) | GShard 137B | DeepSeekMoE 145B | DeepSeekMoE 142B (Half Activated) |
|---|---|---|---|---|---|
| # Total Params | N/A | 67.4B | 136.5B | 144.6B | 142.3B |
| # Activated Params | N/A | 67.4B | 21.6B | 22.2B | 12.2B |
| Relative Expert Size | N/A | N/A | 1 | 0.125 | 0.125 |
| # Experts | N/A | N/A | 0 + 16 | 4 + 128 | 2 + 128 |
| # Activated Experts | N/A | N/A | 0 + 2 | 4 + 12 | 2 + 6 |
| FLOPs per 4K Tokens | N/A | 2057.5T | 572.7T | 585.6T | 374.6T |
| # Training Tokens | N/A | 245B | 245B | 245B | 245B |
| Pile (Loss.) | N/A | 1.905 | 1.961 | **1.876** | 1.888 |
| HellaSwag (Acc.) | 0-shot | 74.8 | 72.0 | **75.8** | 74.9 |
| PIQA (Acc.) | 0-shot | 79.8 | 77.6 | **80.7** | 80.2 |
| ARC-easy (Acc.) | 0-shot | 69.0 | 64.0 | **69.7** | 67.9 |
| ARC-challenge (Acc.) | 0-shot | **50.4** | 45.8 | 48.8 | 49.0 |
| RACE-middle (Acc.) | 5-shot | **63.2** | 59.2 | 62.1 | 59.5 |
| RACE-high (Acc.) | 5-shot | **46.9** | 43.5 | 45.5 | 42.6 |
| DROP (EM) | 1-shot | **27.5** | 21.6 | **27.8** | 28.9 |
| GSM8K (EM) | 8-shot | **11.8** | 6.4 | **12.2** | 13.8 |
| MATH (EM) | 4-shot | 2.1 | 1.6 | **3.1** | 2.8 |
| HumanEval (Pass@1) | 0-shot | **23.8** | 17.7 | 19.5 | 23.2 |
| MBPP (Pass@1) | 3-shot | **33.6** | 27.6 | **33.2** | 32.0 |
| TriviaQA (EM) | 5-shot | 57.2 | 52.5 | **61.1** | 59.8 |
| NaturalQuestions (EM) | 5-shot | 22.6 | 19.0 | **25.0** | 23.5 |
| MMLU (Acc.) | 5-shot | **45.1** | 26.3 | 39.4 | 37.5 |
| WinoGrande (Acc.) | 0-shot | **70.7** | 67.6 | **71.9** | 70.8 |
| CLUEWSC (EM) | 5-shot | 69.1 | 65.7 | **71.9** | 72.6 |
| CEval (Acc.) | 5-shot | **40.3** | 26.2 | 37.1 | 32.8 |
| CMMLU (Acc.) | 5-shot | **40.6** | 25.4 | 35.9 | 31.9 |
| CHID (Acc.) | 0-shot | 88.5 | 86.9 | **90.3** | 88.3 |

> Table 6 caption: "Comparison among DeepSeek 67B (Dense) and MoE models at the scale of about 140B total parameters. In the lines of '# Experts' and '# Activated Experts', a + b denotes a shared experts and b routed experts, respectively. **Bold** font indicates the best or near the best performance excluding the last column. DeepSeekMoE 145B, and even DeepSeekMoE 142B (Half Activated) that has only half of activated expert parameters, outperform GShard 137B by a large margin. Moreover, with 28.5% of computations, DeepSeekMoE 145B achieves comparable performance with DeepSeek 67B." [p. 23]
