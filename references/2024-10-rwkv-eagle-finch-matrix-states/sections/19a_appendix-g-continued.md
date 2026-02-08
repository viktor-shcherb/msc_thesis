# Appendix G: Additional Evaluations (continued) [p. 39]

### Table 15: Self-Learning Capability Evaluation [p. 39]

| METHOD | MODEL | FINETUNED? | SLC |
|--------|-------|------------|-----|
| Open Generation | neural-chat-7b-v3-3 | Yes - DPO | 0.57 |
|  | Mistral-7B-Instruct-v0.2 | Yes - Instruct | 0.35 |
|  | Mistral-7B-v0.1 | No | 0.31 |
|  | TinyLlama-1.1B-Chat-v1.0 | Yes - Vanilla and DPO | 0.08 |
|  | rwkv-4-world-7b | Partially instruct trained | 0.40 |
|  | v5-Eagle-7B-HF | Partially instruct trained | 0.37 |
| Oracle-Selected | neural-chat-7b-v3-3 | Yes - DPO | 0.75 |
|  | Mistral-7B-Instruct-v0.2 | Yes - Instruct | 0.65 |
|  | Mistral-7B-v0.1 | No | 0.43 |
|  | TinyLlama-1.1B-Chat-v1.0 | Yes - Vanilla and DPO | 0.36 |
|  | rwkv-4-world-7b | Partially instruct trained | 0.73 |
|  | v5-Eagle-7B-HF | Partially instruct trained | 0.70 |
| Induced Generation | neural-chat-7b-v3-3 | Yes - DPO | 0.59 |
|  | Mistral-7B-Instruct-v0.2 | Yes - Instruct | 0.25 |
|  | Mistral-7B-v0.1 | No | 0.33 |
|  | TinyLlama-1.1B-Chat-v1.0 | Yes - Vanilla and DPO | 0.17 |
|  | rwkv-4-world-7b | Partially instruct trained | 0.44 |
|  | v5-Eagle-7B-HF | Partially instruct trained | 0.57 |
| External Prompt | neural-chat-7b-v3-3 | Yes - DPO | 0.74 |
|  | Mistral-7B-Instruct-v0.2 | Yes - Instruct | 0.84 |
|  | Mistral-7B-v0.1 | No | 0.37 |
|  | TinyLlama-1.1B-Chat-v1.0 | Yes - Vanilla and DPO | 0.22 |
|  | rwkv-4-world-7b | Partially instruct trained | 0.78 |
|  | v5-Eagle-7B-HF | Partially instruct trained | 0.65 |

Caption: Self-Learning Capability Evaluation.

### Table 16: Eagle 7B and Raven 7B Dataset Comparison [p. 39]

| Dataset | Eagle-7B | Raven-7b |
|---------|----------|----------|
| Aggression | 0.6587 | 0.4063 |
| MathQA | 0.4760 | 0.4028 |
| Sarcasm | 0.4679 | 0.4782 |
| TweetSent | 0.5355 | 0.5541 |
| Unhealthy | 0.2986 | 0.2834 |
| TweetStance | 0.3933 | 0.3070 |
| Spam | 0.7290 | 0.4902 |
| ColBER | 0.4088 | 0.2889 |
| CoLa | 0.5285 | 0.4677 |
| TextEntail | 0.7765 | 0.6137 |
| GoEmo | 0.0956 | 0.0814 |
| PolEmo | 0.5037 | 0.2639 |
| WNLI | 0.5257 | 0.4638 |

Caption: Eagle 7B and Raven 7B reasoning performance comparison based on subsets of selected datasets. The used metric is F1-macro (except for MathQA where accuracy is used instead).

## G.4 Zero-shot evaluation on additional NLP tasks

[p. 38] Zero-shot evaluation is a difficult setup (Sanh et al., 2021; Albalak et al., 2022). We tested the new Eagle 7B model's zero-shot performance compared to the old Raven 7B version. The experiments presented are done on the subsets of datasets used to test ChatGPT performance in (Kocoń et al., 2023). As shown in Table 16, the new model consistently outperforms the old one on various tasks. It is to be noted that the new model remains very sensitive to the selected prompt template, just as the old one, as was shown in (Peng et al., 2023).
