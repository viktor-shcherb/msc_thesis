# Appendix B. DeepSeek-V2-Lite: A 16B Model Equipped with MLA and DeepSeekMoE [p. 29-30]

## B.1 Model Description

### Architectures

[p. 29] DeepSeek-V2-Lite has 27 layers and a hidden dimension of 2048. It also employs MLA and has 16 attention heads, where each head has a dimension of 128. Its KV compression dimension is 512, but slightly different from DeepSeek-V2, it does not compress the queries. For the decoupled queries and key, it has a per-head dimension of 64. DeepSeek-V2-Lite also employs DeepSeekMoE, and all FFNs except for the first layer are replaced with MoE layers. Each MoE layer consists of 2 shared experts and 64 routed experts, where the intermediate hidden dimension of each expert is 1408. Among the routed experts, 6 experts will be activated for each token. Under this configuration, DeepSeek-V2-Lite comprises 15.7B total parameters, of which 2.4B are activated for each token. [p. 29]

**Table 6** | Performance of DeepSeek-V2-Lite, DeepSeekMoE 16B, and DeepSeek 7B. [p. 29]

| | | DeepSeek 7B | DeepSeekMoE 16B | DeepSeek-V2-Lite |
|---|---|---|---|---|
| | Architecture | MHA+Dense | MHA+MoE | MLA+MoE |
| | Context Length | 4K | 4K | 32K |
| | # Activated Params | 6.9B | 2.8B | 2.4B |
| | # Total Params | 6.9B | 16.4B | 15.7B |
| | # Training Tokens | 2T | 2T | 5.7T |
| English | MMLU | 48.2 | 45.0 | **58.3** |
| English | BBH | 39.5 | 38.9 | **44.1** |
| English | TriviaQA | 59.7 | **64.8** | 64.2 |
| English | NaturalQuestions | 22.2 | 25.5 | **26.0** |
| English | ARC-Easy | 67.9 | 68.1 | **70.9** |
| English | ARC-Challenge | 48.1 | 49.8 | **51.2** |
| English | AGIEval | 26.4 | 17.4 | **33.2** |
| Code | HumanEval | 26.2 | 26.8 | **29.9** |
| Code | MBPP | 39.0 | 39.2 | **43.2** |
| Math | GSM8K | 17.4 | 18.8 | **41.1** |
| Math | MATH | 3.3 | 4.3 | **17.1** |
| Math | CMath | 34.5 | 40.4 | **58.4** |
| Chinese | CLUEWSC | 73.1 | 72.1 | **74.3** |
| Chinese | C-Eval | 45.0 | 40.6 | **60.3** |
| Chinese | CMMLU | 47.2 | 42.5 | **64.3** |

### Training Details

[p. 29-30] DeepSeek-V2-Lite is also trained from scratch on the same pre-training corpus of DeepSeek-V2, which is not polluted by any SFT data. It uses the AdamW optimizer with hyper-parameters set to $\beta_1 = 0.9$, $\beta_2 = 0.95$, and weight_decay = 0.1. The learning rate is scheduled using a warmup-and-step-decay strategy. Initially, the learning rate linearly increases from 0 to the maximum value during the first 2K steps. Subsequently, the learning rate is multiplied by 0.316 after training about 80% of tokens, and again by 0.316 after training about 90% of tokens. The maximum learning rate is set to $4.2 \times 10^{-4}$, and the gradient clipping norm is set to 1.0. They do not employ the batch size scheduling strategy for it, and it is trained with a constant batch size of 4608 sequences. During pre-training, the maximum sequence length is set to 4K, and DeepSeek-V2-Lite is trained on 5.7T tokens. [p. 29-30]

[p. 30] Pipeline parallelism is leveraged to deploy different layers of it on different devices, but for each layer, all experts will be deployed on the same device. Therefore, they only employ a small expert-level balance loss with $\alpha_1 = 0.001$, and do not employ device-level balance loss and communication balance loss for it. After pre-training, long context extension and SFT are also performed for DeepSeek-V2-Lite to get a chat model called DeepSeek-V2-Lite Chat. [p. 30]

**Table 7** | Performance of DeepSeek-V2-Lite Chat, DeepSeekMoE 16B Chat, and DeepSeek 7B Chat. [p. 30]

| | | DeepSeek 7B Chat | DeepSeekMoE 16B Chat | DeepSeek-V2-Lite Chat |
|---|---|---|---|---|
| | Architecture | MHA+Dense | MHA+MoE | MLA+MoE |
| | Context Length | 4K | 4K | 32K |
| | # Activated Params | 6.9B | 2.8B | 2.4B |
| | # Total Params | 6.9B | 16.4B | 15.7B |
| | # Training Tokens | 2T | 2T | 5.7T |
| English | MMLU | 49.7 | 47.2 | **55.7** |
| English | BBH | 43.1 | 42.2 | **48.1** |
| English | TriviaQA | 59.5 | 63.3 | **65.2** |
| English | NaturalQuestions | 32.7 | 35.1 | **35.5** |
| English | ARC-Easy | 70.2 | 69.9 | **74.3** |
| English | ARC-Challenge | 50.2 | 50.0 | **51.5** |
| English | AGIEval | 17.6 | 19.7 | **42.8** |
| Code | HumanEval | 45.1 | 45.7 | **57.3** |
| Code | MBPP | 39.0 | **46.2** | 45.8 |
| Math | GSM8K | 62.6 | 62.2 | **72.0** |
| Math | MATH | 14.7 | 15.2 | **27.9** |
| Math | CMath | 66.4 | 67.9 | **71.7** |
| Chinese | CLUEWSC | 66.2 | 68.2 | **80.0** |
| Chinese | C-Eval | 44.7 | 40.0 | **60.1** |
| Chinese | CMMLU | 51.2 | 49.3 | **62.5** |

## B.2 Performance Evaluation

### Base Model

[p. 30] The performance of DeepSeek-V2-Lite is evaluated and compared with previous small-size base models in Table 6. DeepSeek-V2-Lite exhibits overwhelming performance advantages, especially in reasoning, coding, and math. [p. 30]

### Chat Model

[p. 30] The performance of DeepSeek-V2-Lite Chat is evaluated and compared with previous small-size chat models in Table 7. DeepSeek-V2-Lite also outperforms the previous small-size chat models by a large margin. [p. 30]
