# 5.3 Low-resource Translation [p. 42–45]

[p. 42] As the model is pretrained on low-resource languages, Apertus's translation abilities to and from Romansh, a low-resource language that is one of Switzerland's four official languages, are specifically tested. A preliminary version of the Romansh WMT24++ benchmark for machine translation is used (Vamvas et al., 2025). This benchmark evaluates translation quality between German and either of six written varieties of the Romansh language -- Rumantsch Grischun as well as the regional varieties Sursilvan, Sutsilvan, Surmiran, Puter, and Vallader. The benchmark is an extension of WMT24++ (Deutsch et al., 2025) and follows the protocol of the WMT24 General Machine Translation Shared Task (Kocmi et al., 2024), *i.e.*, few-shot prompting with 3 example sentence pairs and greedy decoding. Table 24 reports the BLEU score (Papineni et al., 2002) of the generated translations. Across the board, the results demonstrate greater low-resource translation abilities compared to the baseline Llama-3.3-70B-Instruct.

---

**Table 23: Results on RULER Benchmark Across Various Context Lengths** [p. 45]

Evaluation of Apertus-70B-Instruct on 64k context length exceeded the maximum allowed runtime on the node.

| Model | 4k | 8k | 16k | 32k | 64k |
|---|---|---|---|---|---|
| Apertus-8B | 89.5 | 82.1 | 75.8 | 70.3 | 55.9 |
| Apertus-70B | 88.3 | 80.2 | 77.7 | 71.1 | 56.9 |
| Apertus-8B-Instruct | 91.2 | 87.2 | 79.1 | 65.9 | 61.4 |
| Apertus-70B-Instruct | 94.8 | 89.9 | 85.7 | 81.9 | 67.3 |
| Qwen3-8B | 94.2 | 93.1 | 91.6 | 89.7 | 75.7 |
| Qwen3-32B | 94.4 | 94.1 | 93.5 | 92.6 | 87.1 |
| Qwen2.5-72B-Instruct | 96.1 | 95.0 | 94.5 | 93.3 | 89.3 |
| Llama-3.1-8B | 93.1 | 91.5 | 90.4 | 85.7 | 81.3 |
| Llama-3.1-8B-Instruct | 95.0 | 94.0 | 91.8 | 86.2 | 84.8 |
| Llama-3.3-70B-Instruct | 95.2 | 94.7 | 94.8 | 93.7 | 85.0 |
| Gemma-3-12b-it | 89.6 | 84.6 | 77.5 | 72.1 | 61.0 |
| Gemma-3-27b-it | 92.7 | 85.4 | 79.8 | 68.7 | 58.0 |
| SmolLM3-3B | 88.4 | 83.9 | 81.8 | 76.6 | 65.9 |

---

**Table 24: Post-training Evaluation** [p. 45]

BLEU scores for machine translation between German and six varieties of Romansh, based on a preliminary version of the Romansh WMT24++ benchmark. Higher scores are better. The arrows (up/down) show the desired direction for the metric.

| Model | Rumantsch Grischun DE to RM (up) | Rumantsch Grischun RM to DE (up) | Sursilvan DE to RM (up) | Sursilvan RM to DE (up) | Sutsilvan DE to RM (up) | Sutsilvan RM to DE (up) |
|---|---|---|---|---|---|---|
| Apertus-8B-Instruct | 23.0 | 41.3 | 12.8 | 31.0 | 7.3 | 20.3 |
| Apertus-70B-Instruct | 27.8 | 44.7 | 15.2 | 37.3 | 8.2 | 27.9 |
| Llama-3.3-70B-Instruct | 21.6 | 35.6 | 11.9 | 28.0 | 6.6 | 16.0 |

| Model | Surmiran DE to RM (up) | Surmiran RM to DE (up) | Puter DE to RM (up) | Puter RM to DE (up) | Vallader DE to RM (up) | Vallader RM to DE (up) |
|---|---|---|---|---|---|---|
| Apertus-8B-Instruct | 9.3 | 26.7 | 8.9 | 27.2 | 11.0 | 31.1 |
| Apertus-70B-Instruct | 10.5 | 34.3 | 9.9 | 33.7 | 12.2 | 38.6 |
| Llama-3.3-70B-Instruct | 7.9 | 22.1 | 8.7 | 27.5 | 11.0 | 31.6 |
