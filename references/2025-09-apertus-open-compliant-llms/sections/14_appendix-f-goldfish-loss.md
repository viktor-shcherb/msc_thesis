# Appendix F: Implementation of Goldfish Loss [p. 85–87]

[p. 85] Verbatim regurgitation of training data is a significant concern in LLMs, as it raises both copyright (Chang et al., 2023; Karamolegkou et al., 2023) and privacy risks (Huang et al., 2022). The authors have addressed privacy risks in Section 3.1.2; with respect to copyright protection, their approach is grounded in the principle that safeguards against copyright infringement should prioritize proactive interventions during pretraining rather than reactive post-hoc measures, which have demonstrated limitations.

## Limitations of Post-hoc Memorization Mitigation

[p. 85] Nasr et al. (2025) demonstrates the fragility of post-hoc alignment using two distinct methods: a divergence attack, a form of adversarial prompting that successfully extracts verbatim training data from production models like `gpt-3.5-turbo` and `Gemini 1.5 Pro`, and a more potent finetuning attack, which reverts aligned models, including `gpt-4` and `LLaMA2-Chat`, to their pretraining objective by finetuning them on a small dataset, thereby bypassing their safety guardrails to reveal thousands of unique training examples.

Other post-hoc strategies also face inherent shortcomings. Constrained decoding, which filters or blocks known sensitive outputs, serves merely as a symptomatic treatment: it prevents explicit outputs but does not remove the underlying memorized information stored within model parameters (Park et al., 2024). Likewise, machine unlearning methods, although powerful, require prior knowledge of specific training examples to remove. They operate on a case-by-case basis, potentially causing unintended side-effects such as performance degradation (Sakarvadia et al., 2025).

## Success of Pretraining-time Mitigation

[p. 85] To proactively mitigate memorization, the authors extend the Goldfish Loss, a modification to the training objective proposed by Hans et al. (2024) to discourage the model from learning exact token-to-context mappings by selectively masking tokens during pretraining. Algorithm 1 details their implementation of goldfish loss. They modify the original Goldfish implementation by front-loading token masking during data loading rather than during pretraining for efficiency. Through calibration detailed in Xu (2025), they identify an optimal configuration of a 2% token masking rate (k = 50) and a 50-token context window for hashing (h = 50), which effectively suppresses verbatim memorization (Figure F.3) without compromising downstream performance (Table F.5).

## Table F.5: Token Masking Preserves Downstream Performance Across Model Scales

**Table F.5** (p. 85): Downstream task performance for models trained with Goldfish Loss (2% token dropout) versus standard cross-entropy loss under the same setup as in Figure F.3. The 1B and 3B Goldfish models show comparable performance to their standard counterparts. Notably, the 8B Goldfish model outperforms the standard 8B model on nearly all evaluated tasks, suggesting that the mitigation does not compromise, and may even enhance, model utility at scale.

| Model | Wiki. ppl (down) | Hella. acc (up) | Hella. norm (up) | ARC-c acc (up) | ARC-c norm (up) | ARC-e acc (up) | ARC-e norm (up) | PIQA acc (up) | Wino. acc (up) | CSQA acc (up) | MMLU acc (up) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Standard 1B | 18.71 | 40.43 | 52.31 | 33.36 | 35.15 | **68.10** | 63.13 | 71.00 | 53.91 | **21.79** | 23.65 |
| Goldfish 1B | 18.96 | **40.44** | **52.41** | 32.08 | 32.25 | 67.68 | **63.38** | **71.11** | **53.43** | 19.00 | **25.10** |
| Standard 3B | 15.42 | **46.13** | **59.93** | **38.40** | **40.44** | **73.65** | **68.01** | **73.99** | 57.06 | **21.87** | **25.69** |
| Goldfish 3B | **15.01** | 46.01 | 59.89 | 36.52 | 40.10 | 71.84 | 67.76 | 73.72 | **58.41** | 20.72 | 25.42 |
| Standard 8B | 13.15 | 49.74 | 65.74 | 42.24 | 45.99 | 75.97 | 72.18 | 75.52 | 61.88 | **20.56** | 24.53 |
| Goldfish 8B | **12.44** | **50.29** | **66.61** | **43.00** | **46.67** | **76.89** | **73.78** | **75.63** | **62.43** | 20.39 | **26.98** |

Note: Bold values indicate the better result within each model scale comparison (Standard vs. Goldfish). "down" means lower is better (perplexity); "up" means higher is better.

## Figure F.3

**Figure F.3** (p. 86): **Goldfish Loss Successfully Mitigates Memorization in LLaMA Models.** The figure compares verbatim memorization in LLaMA models (1B, 3B, and 8B) pretrained from scratch under two conditions: standard cross-entropy loss and Goldfish Loss. All models are trained on a custom 83B token dataset simulating a realistic scenario by mixing their Llama tokenizer-processed FM-Probes v1 with FineWeb-Edu data; their analysis confirms a low 13-gram contamination of 0.34% between the probe set and the web data.

The figure contains 6 heatmaps arranged in a 2x3 grid:
- **Row (a) "Standard Loss"**: Three heatmaps for Llama 1B, 3B, and 8B with standard cross-entropy loss.
- **Row (b) "Goldfish Loss"**: Three heatmaps for Llama 1B, 3B, and 8B with Goldfish Loss.

Each heatmap shows:
- X-axis: Prefix Length (ranging from 25 to 4000)
- Y-axis: Repetition Frequency (ranging from 1 to 128)
- Color scale: Rouge-L scores for 500-token suffixes, evaluated at offset 0. Higher values (darker red/orange) indicate more memorization; lower values (lighter/white) indicate less.

The results demonstrate that Goldfish Loss effectively suppresses verbatim recall across all model scales, keeping Rouge-L scores at low levels. A slight upward trend in memorization is still observable in larger models (8B) at the highest repetition counts, indicating that while significantly mitigated, the propensity to memorize is not entirely eliminated for LLaMA models.

---
[p. 87 continued]

## Algorithm 1: Training with Goldfish Loss using Precomputed Masking

**Given:** Dataset *D*, Model parameters *θ*, hash table size *M*, goldfish frequency *k*, context width *h*, goldfish token ID *g*_id

**Precompute hash table of context hashes:**
1. Initialize uniform random hash table *H* of size *M*

**function** APPLYGOLDFISHMASK(*tokens*, *maskToken*, *k*, *hashTable*, *contextSize*):
2. *maskedTokens* ← clone(*tokens*)
3. *windows* ← CreateSlidingWindows(*tokens*, *contextSize*)
4. *hashValues* ← MultiplyTokensInWindow(*windows*) mod *tableSize*
5. *lookupValues* ← *hashTable*[*hashValues*]
6. *tokensToMask* ← (*lookupValues* < 1/*k*)
7. Replace tokens at positions *contextSize* − 1 and beyond where *tokensToMask* is true with *maskToken*
8. **return** *maskedTokens*

**Dataset preparation phase:**
9. **for each** sequence *S* in dataset *D* **do**
10. *S*_masked ← ApplyGoldfishMask(*S*, *g*_id, *k*, *H*, *h*)
11. Store *S*_masked in preprocessed dataset *D*_prep
12. **end for**

**Training phase using pre-masked data:**
13. **for each** training batch *B* sampled from dataset *D*_prep **do**
14. *L* ← 0
15. **for each** sequence *S* in batch *B* **do**
16. tokens, labels ← get_preprocessed_data(*S*)  ▷ Labels already masked
17. *L* ← *L* + CrossEntropyLoss(labels, model(*tokens*))
18. **end for**
19. *θ* ← update_model_parameters(*θ*, *L*)
20. **end for**

The key modification from the original Goldfish implementation (Hans et al., 2024) is that token masking is precomputed during data loading (the "Dataset preparation phase") rather than applied during training. This front-loading approach improves training efficiency. The hash-based masking uses a sliding window of context size *h* to determine which tokens to mask, with the masking rate controlled by 1/*k* (i.e., k = 50 yields a 2% masking rate).
