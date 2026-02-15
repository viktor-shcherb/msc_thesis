# Appendix E. Truncation Length Setting [p. 26]

[p. 26] The appendix explains two practical issues in thinking-mode inference:
1. Some models generate outputs far longer than default 8k budget (example: MiniMax-M2 has 538/4500 inferences far beyond 8k).
2. Claimed context length may be unstable near upper bounds, requiring conservative truncation for reliable scoring.

[p. 26] For DeepSeek-V3.2, GLM-4.6, and MiniMax-M2, truncation is set to **120k** with **32k** thinking output budget to preserve reasoning space and reduce evaluation failures.

## Table 4: GLM-4.6 non-thinking scores under different truncation lengths [p. 26]

| Truncation Length | 8k | 16k | 32k | 64k | 128k | 256k |
|---|---:|---:|---:|---:|---:|---:|
| 190k | 53.74 | 50.76 | 51.93 | 45.60 | 37.73 | 2.55 |
| 120k | 53.98 | 49.88 | 52.26 | 46.18 | 38.68 | 34.14 |

[p. 26] Interpretation in text: with 190k truncation, GLM-4.6 becomes unstable on 256k-length samples, producing a collapse in score. This is cited as direct evidence of divergence between effective and claimed context length.
