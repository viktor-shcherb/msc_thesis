# Performance Evaluation [p. 21–25]

[p. 21]

## Multimodal Performance (continued from previous section)

### Comparison to PaliGemma 2

The authors fine-tune multimodal Gemma 3 pre-trained checkpoints following the protocol from Steiner et al. (2024), with only the learning rate swept while other transfer settings remain the same [p. 21]. Table 12 shows that Gemma 3 excels at benchmarks involving document understanding, outperforming the larger PaliGemma 2 model in some cases [p. 21]. Due to average pooling in the vision encoder, the Gemma 3 4B and 12B models are about 10x cheaper to transfer compared with the PaliGemma 2 9B and 27B models at the same 896 x 896 resolution [p. 21]. Gemma 3 also performs better on AI2D and OKVQA, but slightly better on VQAv2 and COCO caption [p. 21].

**Table 12** (p. 21): Performance of pre-trained checkpoints after fine-tuning on multi-modal benchmarks (without P&S). PaliGemma 2 was transferred at 896x896 resolution for the first four benchmarks and at 448x448 resolution for the others.

| Benchmark | PaliGemma 2 2B | PaliGemma 2 9B | PaliGemma 2 27B | Gemma 3 4B | Gemma 3 12B | Gemma 3 27B |
|-----------|----------------|----------------|-----------------|------------|-------------|-------------|
| DocVQA | 81.6 | 86.3 | 85.1 | 86.1 | 89.0 | **89.5** |
| InfoVQA | 41.4 | 53.1 | 50.2 | 55.6 | 61.6 | **64.6** |
| TextVQA | 76.3 | 76.3 | 75.1 | 79.1 | 81.6 | **83.2** |
| ChartQA | 70.7 | 79.1 | 71.3 | 79.8 | 83.5 | **83.4** |
| AI2D | 76.0 | 84.4 | 84.6 | 80.9 | 85.6 | **86.5** |
| OKVQA | 64.1 | 68.6 | 70.6 | 65.2 | 69.3 | **71.1** |
| CountBenchQA | 82.0 | 85.3 | 87.4 | 79.4 | 83.5 | **87.8** |
| COCO caption | 143. | 145. | **145.** | 143. | 143. | 144. |
| VQAv2 | 84.8 | 85.8 | 85.8 | 84.1 | 84.9 | **85.1** |
| Tally QA | 80.6 | 82.4 | 82.1 | 79.0 | 81.3 | **81.7** |

### Multimodal Multilingual Performance

Table 13 reports the performance of pre-trained models on multilingual tasks [p. 21]. The authors apply in-context learning with multi-shot prompting and present results on the following benchmarks: MGSM (Shi et al., 2023), Global-MMLU-Lite (Singh et al., 2024b), WMT24++ (Deutsch et al., 2025), FLoRes (Goyal et al., 2022), XQuAD (Artetxe et al., 2020), ECLeKTic (Goldman et al., 2025), IndicGenBench (Singh et al., 2024a), XOR QA (Asai et al., 2020) [p. 21]. Evaluation details are described in Table 19 [p. 21].

**Table 13** (p. 21): Multilingual performance after the pre-training phase. IndicGenBench is an average over benchmarks reported in Table 14.

| Benchmark | Gemma 2 2B | Gemma 2 9B | Gemma 2 27B | Gemma 3 1B | Gemma 3 4B | Gemma 3 12B | Gemma 3 27B |
|-----------|------------|------------|-------------|------------|------------|-------------|-------------|
| MGSM | 18.7 | 57.3 | 68.0 | 2.04 | 34.7 | 64.3 | **74.3** |
| GMMLU | 43.3 | 64.0 | 69.4 | 24.9 | 57.0 | 69.4 | **75.7** |
| WMT24++ | 38.8 | 50.3 | 53.0 | 36.7 | 48.4 | 53.9 | **55.7** |
| Flores | 30.2 | 41.3 | 44.3 | 29.5 | 39.2 | 46.0 | **48.8** |
| XQuAD | 53.7 | 72.2 | 73.9 | 43.9 | 68.0 | 74.5 | **76.8** |
| ECLeKTic | 8.29 | 14.0 | 17.1 | 4.69 | 11.0 | 17.2 | **24.4** |
| IndicGB | 47.4 | 59.3 | 62.1 | 41.4 | 57.2 | 61.7 | **63.4** |

**Table 14** (p. 21): Detailed IndicGenBench performance after the pre-training phase.

| Benchmark | Gemma 2 2B | Gemma 2 9B | Gemma 2 27B | Gemma 3 1B | Gemma 3 4B | Gemma 3 12B | Gemma 3 27B |
|-----------|------------|------------|-------------|------------|-------------|-------------|-------------|
| XQuAD Indic | 54.3 | 73.1 | 74.9 | 43.1 | 68.3 | 75.2 | **77.8** |
| XORQA | 66.2 | 69.9 | 72.5 | 56.3 | 68.3 | 69.8 | **70.4** |
| XORQA in-xx | 31.2 | 40.8 | 44.3 | 27.1 | 39.8 | 43.8 | **46.0** |
| Flores Indic | 38.1 | 54.0 | 56.9 | 39.0 | 52.3 | 58.0 | **59.5** |

### Long Context Performance

In Table 15, the authors report the performance of pre-trained and fine-tuned models on long context benchmarks [p. 21]. They include RULER (Hsieh et al., 2024) and MRCR (Vodrahalli et al., 2024) benchmarks evaluating at 32K and 128K sequence lengths [p. 21].

**Table 15** (p. 21-22): Performance of pre-trained (PT) and instruction fine-tuned (IT) models on long context benchmarks at different context lengths.

|  | Gemma 3 PT |  |  | Gemma 3 IT |  |  |
|---|---|---|---|---|---|---|
| Context | 4B | 12B | 27B | 4B | 12B | 27B |
| RULER 32K | 67.1 | **90.6** | 85.9 | 61.4 | 80.3 | **91.1** |
| RULER 128K | 51.7 | **80.7** | 72.9 | 46.8 | 57.1 | **66.0** |
| MRCR 32K | 44.7 | 59.8 | **63.2** | 49.8 | 53.7 | **63.2** |
| MRCR 128K | 40.6 | 56.9 | **60.0** | 44.6 | 49.8 | **59.3** |

[p. 22]

## 8.1. Performance of IT models

In Table 18, the authors report additional benchmarks on their IT models [p. 21]. N2C refers to Natural2Code, the Gemini 1.0 internal held-out dataset which uses author-generated sources instead of web-based information [p. 21]. BBEH refers to BIG-Bench Extra Hard (Kazemi et al., 2025), a challenging LLM reasoning benchmark that aggregates several reasoning tasks (Fatemi et al., 2024; Hessel et al., 2022; Kazemi et al., 2023, 2024b; Kıcıman et al., 2023; Nie et al., 2024; Sánchez et al., 2024; Shah et al., 2024; Tyen et al., 2023; White et al., 2024; Yamada et al., 2023; Zhang et al., 2024) [p. 21]. ECLeKTic refers to Goldman et al. (2025) [p. 21]. The authors report the micro average score [p. 21-22]. More evaluation details are described in Table 21 [p. 22].

**Table 16** (p. 22): Performance of instruction fine-tuned (IT) models on multimodal benchmarks. If not mentioned, these results are on the final test set of each dataset with P&S applied.

| Benchmark | 4B | 12B | 27B |
|-----------|-----|------|------|
| MMMU (val) | 48.8 | 59.6 | **64.9** |
| DocVQA | 75.8 | **87.1** | 86.6 |
| InfoVQA | 50.0 | 64.9 | **70.6** |
| TextVQA | 57.8 | **67.7** | 65.1 |
| AI2D | 74.8 | 84.2 | **84.5** |
| ChartQA | 68.8 | 75.7 | **78.0** |
| VQAv2 (val) | 62.4 | **71.6** | 71.0 |
| MathVista (testmini) | 50.0 | 62.9 | **67.6** |

**Table 17** (p. 22): Performance of instruction fine-tuned (IT) models on vision understanding benchmarks using 0 shot with 16 frames linspace. Perception Test consists of real-world videos designed to show perceptually interesting situations and they report results on the multiple choice video QA benchmark in terms of top-1 accuracy. ActivityNet-QA reports standard gpt-evaluation.

| Benchmark | 4B | 12B | 27B |
|-----------|-----|------|------|
| Perception Test MCVQA | 50.6 | 54.9 | **58.1** |
| ActivityNet-QA | 46.3 | 50.4 | **52.8** |

## 8.2. Performance of IT models on video understanding

**Additional multimodal evaluations.** Gemma 3 IT models were evaluated on common vision benchmarks following the evaluation protocol of Gemini 1.5 (Gemini Team, 2024) [p. 22]. The results are given in Table 16 when P&S is activated [p. 22].

**Table 18** (p. 23): Performance of instruction fine-tuned (IT) models of different sizes on more internal and external benchmarks.

| Benchmark | Gemma 2 2B | Gemma 2 9B | Gemma 2 27B | Gemma 3 1B | Gemma 3 4B | Gemma 3 12B | Gemma 3 27B |
|-----------|------------|------------|-------------|------------|------------|-------------|-------------|
| MMLU | 56.1 | 71.3 | 76.2 | 38.8 | 58.1 | 71.9 | **76.9** |
| MBPP | 36.6 | 59.2 | 67.4 | 35.2 | 63.2 | 73.0 | **74.4** |
| HumanEval | 20.1 | 40.2 | 51.8 | 41.5 | 71.3 | 85.4 | **87.8** |
| N2C | 46.8 | 68.3 | 77.3 | 56.0 | 70.3 | 80.7 | **84.5** |
| LiveCodeBench | 7.0 | 20.0 | 29.0 | 5.0 | 23.0 | 32.0 | **39.0** |
| GSM8K | 62.6 | 88.1 | 91.1 | 62.8 | 89.2 | 94.4 | **95.9** |
| MATH | 27.2 | 49.4 | 55.6 | 48.0 | 75.6 | 83.8 | **89.0** |
| HiddenMath | 2.0 | 8.0 | 12.0 | 15.0 | 42.0 | 51.0 | **56.0** |
| BBH | 41.4 | 69.0 | 74.9 | 39.1 | 72.2 | 85.7 | **87.6** |
| BBEH | 5.9 | 9.8 | 14.8 | 7.2 | 11.0 | 16.3 | **19.3** |
| IFEval | 80.4 | 88.4 | **91.1** | 80.2 | 90.2 | 88.9 | 90.4 |
| GMMLU-Lite | 41.9 | 64.8 | 68.6 | 34.2 | 54.5 | 69.5 | **75.1** |
| ECLeKTic | 5.3 | 11.8 | 17.6 | 1.4 | 4.6 | 10.3 | **16.7** |
| WMT24++ | 37.4 | 48.7 | 51.7 | 35.9 | 46.8 | 51.6 | **53.4** |

[p. 24]

## Benchmark Methodology Details

**Table 19** (p. 24): Details on text benchmarks. Char-Len stands for Character Length Normalization and COT stands for Chain-Of-Thought prompting.

| Evaluation | Metric | Type | n-shot | COT | Norm |
|------------|--------|------|--------|-----|------|
| MBPP | pass@1 | sampling | 3-shot | | |
| HumanEval | pass@1 | sampling | 0-shot | | |
| HellaSwag | Accuracy | scoring | 10-shot | | Char-Len |
| BoolQ | Accuracy | scoring | 0-shot | | Char-Len |
| PIQA | Accuracy | scoring | 0-shot | | Char-Len |
| SIQA | Accuracy | scoring | 0-shot | | Char-Len |
| TriviaQA | Accuracy | sampling | 5-shot | | |
| Natural Questions | Accuracy | sampling | 5-shot | | |
| ARC-C | Accuracy | scoring | 25-shot | | Char-Len |
| ARC-E | Accuracy | scoring | 0-shot | | Char-Len |
| WinoGrande | Accuracy | scoring | 5-shot | | Char-Len |
| BBH | Accuracy | sampling | few-shot | Yes | |
| DROP | Token F1 score | sampling | 1-shot | | |
| AGIEval | Accuracy | sampling | 3-5-shot | | |
| MMLU | Accuracy | scoring | 5-shot | | Char-Len |
| MATH | Accuracy | sampling | 4-shot | Yes | |
| GSM8K | Accuracy | sampling | 8-shot | Yes | |
| GPQA Diamond | Accuracy | sampling | 5-shot | Yes | |
| MMLU-Pro | Accuracy | sampling | 5-shot | Yes | |
| MGSM | Accuracy | sampling | 8-shot | | |
| FLoRes | CHaRacter-level F-score | sampling | 1-shot | | |
| Global-MMLU-Lite | Accuracy | scoring | 5-shot | | Char-Len |
| XQuAD | CHaRacter-level F-score | sampling | 5-shot | | |
| WMT24++ | CHaRacter-level F-score | sampling | 5-shot | | |
| ECLeKTic | ECLeKTic score | sampling | 2-shot | | First-line/strip |
| XQuAD Indic | CHaRacter-level F-score | sampling | 5-shot | | |
| XOR QA IN-EN | CHaRacter-level F-score | sampling | 5-shot | | |
| XOR QA IN-XX | CHaRacter-level F-score | sampling | 5-shot | | |
| FLoRes Indic | CHaRacter-level F-score | sampling | 5-shot | | |
| RULER | Accuracy | scoring | 0-shot | | |
| MRCR | MRCR score | sampling | few-shot | | |

[p. 25]

**Table 20** (p. 25): Details on vision benchmarks. No Chain-Of-Thought prompting nor normalization.

| Evaluation | Metric | Type | n-shot |
|------------|--------|------|--------|
| COCO Caption | Cider score | sampling | 4-shot |
| DocVQA | ANLS score | sampling | 4-shot |
| InfographicVQA | ANLS score | sampling | 4-shot |
| MMMU | Accuracy | sampling | 3-shot text only |
| TextVQA | Accuracy | sampling | 4-shot |
| RealWorldQA | Accuracy | sampling | 4-shot text only |
| ReMI | Accuracy | sampling | 4-shot |
| AI2D | Accuracy | sampling | 4-shot |
| ChartQA | Accuracy | sampling | 4-shot |
| VQA v2 | Accuracy | sampling | 4-shot |
| BLINK | Accuracy | sampling | 0-shot |
| OK-VQA | Accuracy | sampling | 4-shot |
| TallyQA | Accuracy | sampling | 4-shot |
| SpatialSense VQA | Accuracy | sampling | 4-shot |
| CountBench VQA | Accuracy | sampling | 0-shot |

**Table 21** (p. 25): Details on instruction fine-tuned (IT) benchmarks. No normalization.

| Evaluation | Metric | Type | n-shot | COT |
|------------|--------|------|--------|-----|
| MMLU | Accuracy | sampling | 0-shot | |
| MBPP | pass@1 | sampling | 3-shot | |
| HumanEval | pass@1 | sampling | 0-shot | |
| N2C | pass@1 | sampling | 0-shot | |
| LiveCodeBench | Average over 8 samples | sampling | 0-shot | Yes |
| GSM8K | Accuracy | sampling | 0-shot | Yes |
| GPQA Diamond | Accuracy | sampling | 0-shot | Yes |
| MATH | Accuracy | sampling | 0-shot | |
| HiddenMath | Accuracy | sampling | 0-shot | |
| BBH | Accuracy | sampling | 0-shot | |
| BBEH | Accuracy | sampling | 0-shot | |
| IFEval | Accuracy | sampling | 0-shot | |
| Global-MMLU-lite | Accuracy | sampling | 0-shot | Yes |
| ECLeKTic | ECLeKTic score | sampling | 0-shot | |
| WMT24++ | CHaRacter-level F-score | sampling | 0-shot | |

## Citations in this section

The following citations appear in pages 21-25:

- Kembhavi et al., 2016 (AI2D)
- Masry et al., 2022 (ChartQA)
- Goyal et al., 2017 (VQA v2)
- Fu et al., 2024 (BLINK)
- Marino et al., 2019 (OK-VQA)
- Acharya et al., 2019 (TallyQA)
- Yang et al., 2019 (SpatialSense VQA)
- Paiss et al., 2023 (CountBench VQA)
- Steiner et al., 2024 (PaliGemma 2 transfer protocol)
- Shi et al., 2023 (MGSM)
- Singh et al., 2024b (Global-MMLU-Lite)
- Deutsch et al., 2025 (WMT24++)
- Goyal et al., 2022 (FLoRes)
- Artetxe et al., 2020 (XQuAD)
- Goldman et al., 2025 (ECLeKTic)
- Singh et al., 2024a (IndicGenBench)
- Asai et al., 2020 (XOR QA)
- Hsieh et al., 2024 (RULER)
- Vodrahalli et al., 2024 (MRCR)
- Kazemi et al., 2025 (BIG-Bench Extra Hard / BBEH)
- Fatemi et al., 2024 (reasoning task in BBEH)
- Hessel et al., 2022 (reasoning task in BBEH)
- Kazemi et al., 2023, 2024b (reasoning tasks in BBEH)
- Kıcıman et al., 2023 (reasoning task in BBEH)
- Nie et al., 2024 (reasoning task in BBEH)
- Sánchez et al., 2024 (reasoning task in BBEH)
- Shah et al., 2024 (reasoning task in BBEH)
- Tyen et al., 2023 (reasoning task in BBEH)
- White et al., 2024 (reasoning task in BBEH)
- Yamada et al., 2023 (reasoning task in BBEH)
- Zhang et al., 2024 (reasoning task in BBEH)
- Gemini Team, 2024 (Gemini 1.5 evaluation protocol)
