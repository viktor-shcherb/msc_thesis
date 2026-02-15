# Appendix [p. 20–21]

## Details of pre-trained performances

[p. 20]

### Factuality and common-sense

**Table 9** | Factuality, common-sense performance and reasoning after pre-training phase [p. 20]

| Benchmark | Gemma 2 |      |      | Gemma 3 |      |      |      |
|-----------|---------|------|------|---------|------|------|------|
|           | 2B      | 9B   | 27B  | 1B      | 4B   | 12B  | 27B  |
| HellaS    | 72.9    | 81.9 | 86.4 | 62.3    | 77.2 | 84.2 | 85.6 |
| BoolQ     | 75.6    | 77.5 | 76.2 | 63.2    | 72.3 | 78.8 | 82.4 |
| PIQA      | 78.1    | 81.9 | 83.5 | 73.8    | 79.6 | 81.8 | 83.3 |
| SIQA      | 51.8    | 53.3 | 53.8 | 48.9    | 51.9 | 53.4 | 54.9 |
| TQA       | 60.2    | 76.5 | 83.8 | 39.8    | 65.8 | 78.2 | 85.5 |
| NQ        | 17.2    | 29.2 | 34.7 | 9.48    | 20.0 | 31.4 | 36.1 |
| ARC-C     | 55.8    | 69.1 | 71.4 | 38.4    | 56.2 | 68.9 | 70.6 |
| ARC-E     | 80.6    | 88.3 | 88.6 | 73.0    | 82.4 | 88.3 | 89.0 |
| WinoG     | 65.4    | 73.9 | 79.4 | 58.2    | 64.7 | 74.3 | 78.8 |
| BBH       | 42.4    | 69.4 | 74.8 | 28.4    | 50.9 | 72.6 | 77.7 |
| Drop      | 53.2    | 71.5 | 75.2 | 42.4    | 60.1 | 72.2 | 77.2 |

The performance is reported on standard benchmarks: HellaSwag (Zellers et al., 2019), BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2019), SIQA (Sap et al., 2019), TriviaQA (Joshi et al., 2017), Natural Questions (Kwiatkowski et al., 2019), ARC-C and ARC-E (Chollet, 2019), WinoGrande (Sakaguchi et al., 2019), BBH (Suzgun et al., 2022), DROP (Dua et al., 2019). Evaluation details are described in Table 19. Overall, the model performs in the same ballpark as Gemma 2, which is encouraging since these abilities are not the focus of the improvements brought by Gemma 3.

### STEM and code

**Table 10** | STEM and code performance after pre-training phase [p. 20]

| Benchmark | Gemma 2 |      |      | Gemma 3 |      |      |      |
|-----------|---------|------|------|---------|------|------|------|
|           | 2B      | 9B   | 27B  | 4B      | 12B  | 27B  |      |
| MMLU      | 52.2    | 71.2 | 75.2 | 59.6    | 74.5 | 78.6 |      |
| MMLUpro   | 22.2    | 43.7 | 49.4 | 29.2    | 45.3 | 52.2 |      |
| AGIE      | 31.6    | 53.1 | 55.1 | 42.1    | 57.4 | 66.2 |      |
| MATH      | 16.4    | 36.4 | 42.1 | 24.2    | 43.3 | 50.0 |      |
| GSM8K     | 25.0    | 70.2 | 74.6 | 38.4    | 71.0 | 82.6 |      |
| GPQA Diamond | 12.5 | 24.8 | 26.3 | 15.0    | 25.4 | 24.3 |      |
| MBPP      | 31.0    | 51.2 | 60.8 | 46.0    | 60.4 | 65.6 |      |
| HumanE    | 19.5    | 40.2 | 51.2 | 36.0    | 45.7 | 48.8 |      |

The benchmarks considered are: MMLU (Hendrycks et al., 2020), MMLU-Pro (Wang et al., 2024), AGIEval (Zhong et al., 2023), MATH (Hendrycks et al., 2021), GPQA (Rein et al., 2023), GSM8K (Cobbe et al., 2021), MBPP (Austin et al., 2021), HumanEval (Chen et al., 2021). Evaluation details are described in Table 19. Overall, the pre-trained models see consistent improvement over STEM abilities across the pre-trained models. On code, a similar improvement is seen for the 4B and 12B models but not on the 27B.

### Multimodal performance

**Table 11** | Multimodal performance after pre-training phase [p. 20]

The scores are on the val split of each dataset without P&S.

| Benchmark | 4B | 12B | 27B |
|-----------|-----|-----|-----|
| COCO caption | 102 | 111 | 116 |
| DocVQA | 72.8 | 82.3 | 85.6 |
| InfoVQA | 44.1 | 54.8 | 59.4 |
| MMMU | 39.2 | 50.3 | 56.1 |
| TextVQA | 58.9 | 66.5 | 68.6 |
| RealWorldQA | 45.5 | 52.2 | 53.9 |
| ReMI | 27.3 | 38.5 | 44.8 |
| AI2D | 63.2 | 75.2 | 79.0 |
| ChartQA | 63.6 | 74.7 | 76.3 |
| VQAv2 | 63.9 | 71.2 | 72.9 |
| BLINK | 38.0 | 35.9 | 39.6 |
| OKVQA | 51.0 | 58.7 | 60.2 |
| TallyQA | 42.5 | 51.8 | 54.3 |
| SpatialSense VQA | 50.9 | 60.0 | 59.4 |
| CountBench VQA | 26.1 | 17.8 | 68.0 |

### Image understanding

[p. 20–21]

Performance is reported across a variety of visual question answer benchmarks for the different models that were trained with a vision encoder. The benchmarks include: COCO Caption (Chen et al., 2015), DocVQA (Mathew et al., 2020), InfographicVQA (Mathew et al., 2022), MMMU (Yue et al., 2023), TextVQA (Singh et al., 2019), RealWorldQA (Rea), ReMI (Kazemi et al., 2024a), AI2D (Kembhavi et al., 2016), ChartQA (Masry et al., 2022), VQA v2 (Goyal et al., 2017), BLINK (Fu et al., 2024), OKVQA (Marino et al., 2019), TallyQA (Acharya et al., 2019), SpatialSense VQA (Yang et al., 2019), CountBench VQA (Paiss et al., 2023). Evaluation details are described in Table 20.

### Performance of pre-trained checkpoints on multi-modal benchmarks

**Table 12** | Performance of pre-trained checkpoints after fine-tuning on multi-modal benchmarks (without P&S) [p. 21]

PaliGemma 2 was transferred at 896x896 resolution for the first four benchmarks and at 448x448 resolution for the others.

| Benchmark | PaliGemma 2 |      |      | Gemma 3 |      |      |
|-----------|-------------|------|------|---------|------|------|
|           | 2B          | 9B   | 27B  | 4B      | 12B  | 27B  |
| DocVQA    | 81.6        | 86.3 | 85.1 | 86.1    | 89.0 | 89.5 |
| InfoVQA   | 41.4        | 53.1 | 50.2 | 55.6    | 61.6 | 64.6 |
| TextVQA   | 76.3        | 76.3 | 75.1 | 79.1    | 81.6 | 83.2 |
| ChartQA   | 70.7        | 79.1 | 71.3 | 79.8    | 83.5 | 83.4 |
| AI2D      | 76.0        | 84.4 | 84.6 | 80.9    | 85.6 | 86.5 |
| OKVQA     | 64.1        | 68.6 | 70.6 | 65.2    | 69.3 | 71.1 |
| CountBenchQA | 82.0     | 85.3 | 87.4 | 79.4    | 83.5 | 87.8 |
| COCO caption | 143.     | 145. | 145. | 143.    | 143. | 144. |
| VQAv2     | 84.8        | 85.8 | 85.8 | 84.1    | 84.9 | 85.1 |
| Tally QA  | 80.6        | 82.4 | 82.1 | 79.0    | 81.3 | 81.7 |

### Comparison to PaliGemma 2

[p. 21]

Multimodal Gemma 3 pre-trained checkpoints are fine-tuned following the protocol from Steiner et al. (2024) – only learning rate is swept, otherwise the same transfer settings are used. The results in Table 12 show that Gemma 3 excels at benchmarks involving document understanding, even outperforming the larger PaliGemma 2 variant. Note that due to average pooling in the vision encoder the Gemma 3 4B and 12B models are about 10x cheaper to transfer compared with the PaliGemma 2 9B and 27B models at the same 896 x 896 resolution. Gemma 3 also performs better on AI2D and OKVQA, but Gemma 2 performs slightly better on VQAv2 and COCO caption.

### Multilingual performance

**Table 13** | Multilingual performance after the pre-training phase [p. 21]

IndicGenBench is an average over benchmarks reported in Table 14.

| Benchmark | Gemma 2 |      |      | Gemma 3 |      |      |      |
|-----------|---------|------|------|---------|------|------|------|
|           | 2B      | 9B   | 27B  | 1B      | 4B   | 12B  | 27B  |
| MGSM      | 18.7    | 57.3 | 68.0 | 2.04    | 34.7 | 64.3 | 74.3 |
| GMMLU     | 43.3    | 64.0 | 69.4 | 24.9    | 57.0 | 69.4 | 75.7 |
| WMT24++   | 38.8    | 50.3 | 53.0 | 36.7    | 48.4 | 53.9 | 55.7 |
| Flores    | 30.2    | 41.3 | 44.3 | 29.5    | 39.2 | 46.0 | 48.8 |
| XQuAD     | 53.7    | 72.2 | 73.9 | 43.9    | 68.0 | 74.5 | 76.8 |
| ECLeKTic  | 8.29    | 14.0 | 17.1 | 4.69    | 11.0 | 17.2 | 24.4 |
| IndicGB   | 47.4    | 59.3 | 62.1 | 41.4    | 57.2 | 61.7 | 63.4 |

The performance is reported on multilingual tasks using in-context learning with multi-shot prompting and present results on the following benchmarks: MGSM (Shi et al., 2023), Global-MMLU-Lite (Singh et al., 2024b), WMT24++ (Deutsch et al., 2025), FLoRes (Goyal et al., 2022), XQuAD (Artetxe et al., 2020), ECLeKTic (Goldman et al., 2025), IndicGenBench (Singh et al., 2024a), XOR QA (Asai et al., 2020). Evaluation details are described in Table 19.

**Table 14** | Detailed IndicGenBench performance after the pre-training phase [p. 21]

| Benchmark | Gemma 2 |      |      | Gemma 3 |      |      |      |
|-----------|---------|------|------|---------|------|------|------|
|           | 2B      | 9B   | 27B  | 1B      | 4B   | 12B  | 27B  |
| XQuAD Indic | 54.3  | 73.1 | 74.9 | 43.1    | 68.3 | 75.2 | 77.8 |
| XORQA Indic | 66.2  | 69.9 | 72.5 | 56.3    | 68.3 | 69.8 | 70.4 |
| XORQA in-xx | 31.2  | 40.8 | 44.3 | 27.1    | 39.8 | 43.8 | 46.0 |
| Flores Indic | 38.1 | 54.0 | 56.9 | 39.0    | 52.3 | 58.0 | 59.5 |

### Long context

[p. 21]

In Table 15 (not shown on these pages - referenced only), the performance of pre-trained and fine-tuned models is reported on long context benchmarks. The benchmarks include RULER (Hsieh et al., 2024) and MRCR (Vodrahalli et al., 2024) benchmarks evaluating at 32K and 128K sequence lengths.

## 8.1. Performance of IT models

[p. 21]

Additional benchmarks on IT (instruction-tuned) models are reported in Table 18 (not shown on these pages). Note that N2C refers to Natural2Code, the Gemini 1.0 internal held-out dataset, which uses author-generated sources instead of web-based information. BBEH refers to BIG-Bench Extra Hard (Kazemi et al., 2025), a challenging LLM reasoning benchmark that aggregates several reasoning tasks (Fatemi et al., 2024).
