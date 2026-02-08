# 4.1.2 Decontamination [p. 27–28]

[p. 27] All datasets are decontaminated against the benchmarks used for development and final evaluation. Following Allal et al. (2025); Lambert et al. (2025); OLMo et al. (2025), n-gram matching is used to identify and remove training samples that are identical or similar to benchmark prompts. Given the size of the dataset and the number of benchmarks to consider, potentially contaminated samples are first filtered down using an 8-gram matching on the token level. If a match is found, the overlap between the training prompt and the benchmark prompt is calculated using the Ratcliff-Obershelp algorithm.^36 After filtering out short overlaps that are less than 5 tokens long, the sample is considered contaminated if the combined length of the overlaps is longer than half of the benchmark prompt's length. [p. 27]

This approach proved especially critical for cross-lingual contamination, where evaluation problems appear in training data as direct translations. While hash-based methods cannot detect such cases, the n-gram matching identified hundreds of translated benchmark problems that would have artificially inflated scores. Table 9 shows a typical example where a mathematical problem appears identically except for the instruction language, yielding a 0.62 match ratio despite the linguistic difference. [p. 27]

**Table 9: Cross-lingual Contamination Example.** Identical mathematical content with translated instructions. [p. 27]

| Training Sample (English) | Benchmark Sample (Urdu) |
|---|---|
| `<s>` Simplify the fraction by rationalizing the denominator: 4 / (sqrt(108) + 2*sqrt(12) + 2*sqrt(27)). | `<s>` [Urdu translation of the same instruction] 4 / (sqrt(108) + 2*sqrt(12) + 2*sqrt(27)). |
| *Match ratio: 0.62* | |

## Impact of Decontamination and License Filtering [p. 27–28]

[p. 27–28] To quantify the impact of the data filtering approaches, an ablation study is conducted using the Apertus 8B model initialized from a 10T token checkpoint and finetuned on different data configurations. Table 10 presents results across 13 benchmarks, comparing four configurations: (1) original Tulu3 without filtering, (2) Tulu3 with decontamination only, (3) Tulu3 with both decontamination and license filtering, and (4) OLMo2 data with both decontamination and license filtering. [p. 27–28]

The results reveal nuanced trade-offs. While the original Tulu3 mixture achieves an average score of 0.442, decontamination alone shows a negligible impact (0.443). However, adding license filtering reduces average performance by 5.8% (from 0.443 to 0.417), with particularly severe drops on MMLU chain-of-thought evaluation (0.513 -> 0.253, a 51% decrease). Interestingly, some capabilities improve with filtering -- TruthfulQA MC2 accuracy increases from 0.486 to 0.518 (+6.6%), and several reasoning tasks show marginal improvements. The OLMo2 filtered mixture performs comparably to Tulu3 with full filtering (0.421 vs 0.417). These results highlight the inherent tension between compliance and model capability, a trade-off accepted as necessary for responsible open-source model development. [p. 28]

**Table 10: Ablation Study for Decontamination and License Filtering.** Ablation study showing the impact of decontamination and license filtering on Apertus 8B performance across 13 benchmarks. Models were initialized from 10T token checkpoint and finetuned on different data configurations. [p. 28]

| Configuration | MMLU (CoT) | MMLU (CoT-strict) | TruthfulQA MC2 | BBH | DROP F1 | ACP-RoE | ACP-MCQ | GSM8K | HumanEval Pass@10 | MBPP Pass@1 | IFEval | ToxiGen | BBQ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OLMo2 (decon. + lic. filtered) | 0.407 | 0.325 | 0.520 | 0.467 | 0.440 | 0.543 | 0.259 | 0.498 | 0.326 | 0.328 | 0.547 | 0.577 | 0.421 |
| Tulu3 (decontaminated) | 0.558 | 0.515 | 0.486 | 0.470 | 0.461 | 0.563 | 0.247 | 0.479 | 0.353 | 0.318 | 0.547 | 0.642 | 0.443 |
| Tulu3 (decon. + lic. filtered) | 0.391 | 0.253 | 0.518 | 0.490 | 0.430 | 0.551 | 0.260 | 0.501 | 0.384 | 0.312 | 0.542 | 0.598 | 0.417 |
| Tulu3 (original) | 0.542 | 0.513 | 0.489 | 0.482 | 0.483 | 0.560 | 0.252 | 0.482 | 0.365 | 0.324 | 0.536 | 0.665 | 0.442 |

## Multilingual Performance Impact [p. 28]

[p. 28] To assess the impact of the filtering approaches on multilingual capabilities, the same model configurations are evaluated on six multilingual benchmarks spanning knowledge (Global-MMLU), mathematical reasoning (MGSM), cultural understanding (INCLUDE, CulturalBench), and Swiss-specific knowledge (Switzerland QA). As shown in Table 11, the filtering impact on multilingual tasks follows similar patterns to English benchmarks. [p. 28]

The original Tulu3 mixture achieves the strongest multilingual performance with an average of 0.510. Decontamination alone has minimal overall impact (average: 0.511), though individual metrics show minor variations -- MGSM direct evaluation drops from 0.187 to 0.176 while CulturalBench improves slightly from 0.709 to 0.717. Adding license filtering reduces average performance by 4.3% (to 0.489), with MGSM native CoT showing the largest relative drop (0.320 -> 0.273, -14.7%). Cultural knowledge benchmarks prove more robust to filtering, with CulturalBench declining only 5.4% and Switzerland QA dropping just 1.9%. The OLMo2 filtered mixture performs nearly identically to filtered Tulu3 (0.487 vs 0.489). [p. 28]

**Table 11: Impact of Decontamination and License Filtering on Multilingual Benchmark Performance.** Models were evaluated on global knowledge, mathematical reasoning, and cultural understanding tasks. [p. 28]

| Configuration | Global-MMLU | MGSM (Direct) | MGSM (Native CoT) | INCLUDE V1 | CulturalBench | Switzerland QA |
|---|---|---|---|---|---|---|
| Tulu3 (original) | 0.528 | 0.187 | 0.332 | 0.509 | 0.709 | 0.592 |
| Tulu3 (decontaminated) | 0.529 | 0.176 | 0.320 | 0.510 | 0.717 | 0.590 |
| Tulu3 (decon. + lic. filtered) | 0.500 | 0.212 | 0.273 | 0.493 | 0.678 | 0.579 |
| OLMo2 (decon. + lic. filtered) | 0.491 | 0.220 | 0.270 | 0.493 | 0.680 | 0.571 |

---

**Footnotes:**
- ^36: Implemented by the SequenceMatcher function in Python's difflib library.
