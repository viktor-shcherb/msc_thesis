# Analysis [p. 7-9]

## 5.1 Memory and Time Efficiency

[p. 7] Compare Full-length vs PoSE for scaling LLaMA-7B from 2k to 4k/8k/16k using 1,000 steps, batch size 16, 8xV100.

**Figure 3** (p. 8): "Full-length fine-tuning v.s. PoSE in terms of memory, time, and perplexity-vs-steps."

Description:
- (a) Memory (GB): Full-length increases steeply with target length (16k reported OOM on setup), PoSE remains near-constant.
- (b) Time (hours for 1,000 steps): Full-length increases with target length, PoSE near-constant and lower.
- (c) Perplexity-vs-step (GovReport, 16k target): PoSE closely tracks Full-length during training trajectory.

Claim in text [p. 7]: PoSE provides large memory/time savings while maintaining similar language-modeling quality to Full-length.

## 5.2 Compatibility Across RoPE LLMs and PI Strategies

[p. 7] Models tested: LLaMA-7B, LLaMA2-7B, GPT-J-6B, Baichuan2-7B.

[p. 7] Interpolation tested: Linear, NTK, YaRN (plus Original for comparison).

**Figure 4** (p. 8): "Perplexity of LLaMA-7B, LLaMA2-7B, GPT-J-6B, Baichuan2-7B extended to 16k via PoSE with Linear / NTK / YaRN interpolation."

Description:
- Four panels (one per model), x-axis context from 1k to 16k, y-axis perplexity.
- Curves show PoSE+PI variants with low perplexity compared with originals.
- Reported pattern: NTK often has an upturn before target length; YaRN/Linear are more stable near target length.

## 5.3 Potential for Extremely-Long Context

[p. 8] Extreme-length evaluation uses Books3 and Gutenberg (PG-19), with 20 books per dataset, each >128k tokens.

[p. 8] Extended models tested at 96k and 128k with Linear/NTK/YaRN interpolation; sliding-window step increased to 16k for evaluation efficiency.

**Table 2** (p. 9): "Perplexity of models extended to extreme context size via PoSE on PG-19 and Books3."

| Model | PG19 32k | PG19 64k | PG19 96k | PG19 128k | Books3 32k | Books3 64k | Books3 96k | Books3 128k |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PoSE-Linear-96k | 10.18 | 11.11 | 13.57 | - | 9.98 | 10.90 | 13.42 | - |
| PoSE-NTK-96k | 7.98 | 20.39 | 38.73 | - | 8.29 | 20.82 | 40.39 | - |
| PoSE-YaRN-96k | 8.31 | 8.65 | 9.36 | - | 8.90 | 9.40 | 10.38 | - |
| PoSE-Linear-128k | 16.90 | 22.47 | 26.77 | 31.18 | 26.20 | 43.62 | 57.08 | 70.87 |
| PoSE-NTK-128k | 8.04 | 14.84 | 29.48 | 34.80 | 8.34 | 16.04 | 31.42 | 37.00 |
| PoSE-YaRN-128k | 9.32 | 10.36 | 10.77 | 11.33 | 10.56 | 12.30 | 13.07 | 13.81 |

Text conclusion [p. 8-9]: strongest extreme-length behavior is reported for PoSE + YaRN up to 128k.

## 5.4 Capability on Original Context Benchmarks

[p. 8-9] Standard benchmark evaluation includes zero-shot (BoolQ, PIQA, WinoGrande, TruthfulQA) and few-shot (25-shot ARC-C, 10-shot HellaSwag).

**Table 3** (p. 9): "Performance of PoSE-extended LLaMA model on standard benchmarks ..."

| Model | BoolQ | PIQA | WinoGrande | TruthfulQA | ARC-C | HellaSwag |
|---|---:|---:|---:|---:|---:|---:|
| Original LLaMA | 75.11 | 78.67 | 69.85 | 34.08 | 51.19 | 77.75 |
| Full-Linear-16k | 70.95 | 77.64 | 69.06 | 31.89 | 48.55 | 74.19 |
| Full-NTK-16k | 75.80 | 78.08 | 68.98 | 33.83 | 48.81 | 76.57 |
| Full-YaRN-16k | 73.88 | 77.64 | 68.15 | 34.12 | 50.60 | 77.18 |
| PoSE-Linear-16k | 74.50 | 78.13 | 68.59 | 32.05 | 48.29 | 75.56 |
| PoSE-NTK-16k | 74.28 | 78.24 | 68.90 | 33.89 | 49.83 | 76.82 |
| PoSE-YaRN-16k | 74.28 | 78.02 | 69.06 | 34.00 | 49.23 | 77.04 |
| PoSE-Linear-128k | 67.71 | 76.22 | 67.56 | 36.16 | 39.93 | 66.04 |
| PoSE-NTK-128k | 75.35 | 78.18 | 68.98 | 32.71 | 49.66 | 76.19 |
| PoSE-YaRN-128k | 73.61 | 77.80 | 70.01 | 34.47 | 48.46 | 75.54 |

[p. 9] Text interpretation: PoSE models mostly show marginal degradation relative to original/full-length baselines, except larger degradation for 128k Linear interpolation.
