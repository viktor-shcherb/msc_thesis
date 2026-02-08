# Appendix D. Ablation of Attention Mechanisms [p. 31-32]

## D.1 Ablation of MHA, GQA, and MQA

[p. 31] The evaluation results for 7B dense models with MHA, GQA, and MQA on four hard benchmarks are shown in Table 8. All of these three models are trained on 1.33T tokens, and share the same architecture except for the attention mechanisms. In addition, for a fair comparison, the number of parameters of them is aligned to around 7B by adjusting the number of layers. From the table, MHA demonstrates significant advantages over GQA and MQA on these benchmarks. [p. 31]

**Table 8** (p. 32): "Comparison among 7B dense models with MHA, GQA, and MQA, respectively. MHA demonstrates significant advantages over GQA and MQA on hard benchmarks."

| Benchmark (Metric) | # Shots | Dense 7B w/ MQA | Dense 7B w/ GQA (8 Groups) | Dense 7B w/ MHA |
|---|---|---|---|---|
| # Params | - | 7.1B | 6.9B | 6.9B |
| BBH (EM) | 3-shot | 33.2 | 35.6 | **37.0** |
| MMLU (Acc.) | 5-shot | 37.9 | 41.2 | **45.2** |
| C-Eval (Acc.) | 5-shot | 30.0 | 37.7 | **42.9** |
| CMMLU (Acc.) | 5-shot | 34.6 | 38.4 | **43.5** |

## D.2 Comparison Between MLA and MHA

[p. 31-32] In Table 9, the evaluation results for MoE models equipped with MLA and MHA, respectively, on four hard benchmarks are shown. For a solid conclusion, models are trained and evaluated across two scales. Two small MoE models comprise about 16B total parameters, and are trained on 1.33T tokens. Two large MoE models comprise about 250B total parameters, and are trained on 420B tokens. Also, two small MoE models and two large MoE models respectively share the same architecture except for the attention mechanisms. From the table, MLA shows better performance than MHA. More importantly, MLA requires a significantly smaller amount of KV cache (14% for small MoE models and 4% for large MoE models) than MHA. [p. 31]

**Table 9** (p. 32): "Comparison between MLA and MHA on hard benchmarks. DeepSeek-V2 shows better performance than MHA, but requires a significantly smaller amount of KV cache."

| Benchmark (Metric) | # Shots | Small MoE w/ MHA | Small MoE w/ MLA | Large MoE w/ MHA | Large MoE w/ MLA |
|---|---|---|---|---|---|
| # Activated Params | - | 2.5B | 2.4B | 25.0B | 21.5B |
| # Total Params | - | 15.8B | 15.7B | 250.8B | 247.4B |
| KV Cache per Token (# Element) | - | 110.6K | 15.6K | 860.2K | 34.6K |
| BBH (EM) | 3-shot | 37.9 | **39.0** | 46.6 | **50.7** |
| MMLU (Acc.) | 5-shot | 48.7 | **50.0** | 57.5 | **59.0** |
| C-Eval (Acc.) | 5-shot | **51.6** | 50.9 | 57.9 | **59.2** |
| CMMLU (Acc.) | 5-shot | 52.3 | **53.4** | 60.7 | **62.5** |
