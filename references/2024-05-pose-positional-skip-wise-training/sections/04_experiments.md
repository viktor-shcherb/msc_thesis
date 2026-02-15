# Experiments [p. 5-7]

## 4.1 Setups

[p. 5] Main training setup (LLaMA-7B):
- Objective: next-token prediction
- Steps: 1,000
- Global batch size: 64
- Hardware: 8 x V100 (DeepSpeed ZeRO stage 3)
- Learning rate: `2e-5` with linear scheduler, 10 warmup steps
- Optimizer: AdamW (default hyperparameters)
- Fine-tuning data: The Pile, minimum sample length 2,048 tokens
- Default interpolation: Linear
- Evaluation hardware: single A100 GPU
- Inference optimization: FlashAttention v2

[p. 5] Evaluation tasks:
- Long text language modeling: GovReport and Proof-pile
- Passkey retrieval: synthetic prompt protocol from Mohtashami and Jaggi (2023)

[p. 5] Baselines:
- Full-length fine-tuning (with PI)
- RandPos (with PI)
- PI-only in passkey plots (PI without fine-tuning)

## 4.2 Language Modeling

[p. 6] Dataset details:
- GovReport: 19,402 reports, average length 7,866 tokens; evaluate on 50 samples longer than 32,768 tokens.
- Proof-pile: select 50 samples longer than 32,768 tokens.

[p. 6] Sliding-window perplexity uses stride 1,024.

**Table 1** (p. 6): "Perplexity of models trained with different methods ... GovReport and Proof-pile ... 2k to 32k."

| Method | Train/Target | Gov 2k | Gov 4k | Gov 8k | Gov 16k | Gov 32k | Proof 2k | Proof 4k | Proof 8k | Proof 16k | Proof 32k |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Original | -/- | 4.74 | >10^3 | >10^3 | >10^3 | >10^3 | 2.83 | >10^3 | >10^3 | >10^3 | >10^3 |
| Full-length | 16k/16k | 4.87 | 4.70 | 4.61 | 4.59 | - | 2.93 | 2.71 | 2.58 | 2.53 | - |
| RandPos | 2k/16k | 11.63 | 11.17 | 11.54 | 15.16 | - | 7.26 | 6.83 | 6.76 | 7.73 | - |
| RandPos | 2k/32k | 93.43 | 95.85 | 91.79 | 93.22 | 97.57 | 60.74 | 63.54 | 60.56 | 63.15 | 66.47 |
| PoSE (Ours) | 2k/16k | 4.84 | 4.68 | 4.60 | 4.60 | - | 2.95 | 2.74 | 2.61 | 2.60 | - |
| PoSE (Ours) | 2k/32k | 4.91 | 4.76 | 4.68 | 4.64 | 4.66 | 3.01 | 2.78 | 2.66 | 2.60 | 2.59 |

Takeaways stated in text [p. 6]:
- PoSE perplexity generally decreases as evaluation context increases for extended models.
- PoSE is comparable to full-length fine-tuning despite using shorter train context.
- PoSE strongly outperforms RandPos.

## 4.3 Passkey Retrieval for Effective Context Window

[p. 6-7] Protocol:
- Compare Original LLaMA, PoSE-16k, PoSE-32k, plus Full-length, RandPos, PI-only.
- Prompt length varied from 2k to 32k.
- 50 trials per length.
- Random 5-digit passkey at random location.

**Figure 2** (p. 7):

"(a) Prompt template used for passkey retrieval; (b) Retrieval accuracy for the PoSE-extended 16k / 32k models, compared with other baselines."

Description:
- Panel (a): synthetic prompt with distractor text, embedded passkey statement, and retrieval question.
- Panel (b): accuracy-vs-context-length curves for Original, PoSE-16k, PoSE-32k, PI-only-16k, RandPos-16k, Full-length-16k.
- Key pattern: Original/PI-only/RandPos collapse near 0 beyond 2k; PoSE-16k/32k retain high accuracy (reported >= 90%) within target windows.
