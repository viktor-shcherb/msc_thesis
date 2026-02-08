# Appendix D: Contamination on Academic Benchmarks [p. 29, 32]

[p. 29] Cross-contamination between academic benchmarks and the pre-training data is measured similarly to the methodology presented in Appendix C. Results are presented in Table 11.

## Table 11

**Table 11.** Contamination between GPT-4 pre-training data and academic benchmarks. The approximate contamination between the GPT-4 pre-training data and the academic benchmarks evaluated on is reported. For datasets other than HumanEval, contamination was estimated based on 1000 randomly chosen examples against the training data. For HellaSwag, results are computed on a privately held secret holdout, so it was not checked for contamination against the pre-training dataset; however GPT-4's holdout results are close to the results on the validation set (95.6%) which was explicitly masked out during training. For DROP, GPT-4's score on the entire subsample was 82.5. The base GPT-4 model (without RLHF) was used for these evals. [p. 32]

| Benchmark | GPT-4 | GPT-3.5 | Contamination | GPT-4 (non-contaminated) | Degradation |
|---|---|---|---|---|---|
| MMLU | 86.4% | 70.0% | ~0.6% | - | - |
| GSM-8K | 92.0% | 57.1% | ~1% | - | - |
| HellaSwag | 95.3% | 85.5% | -* | - | - |
| AI2 | 96.3% | 85.2% | ~3.4% | - | - |
| WinoGrande | 87.5% | 81.6% | ~0.9% | - | - |
| HumanEval | 67.0% | 48.1% | 25% | 65.58% | -2.12% |
| DROP (F1) | 80.9 | 64.1 | ~21% | 82.8* (subsample) | 0 |

\* HellaSwag contamination was not checked because results are computed on a privately held secret holdout.

\* DROP GPT-4 (non-contaminated) value of 82.8 is marked with an asterisk in the original table, referring to a subsample.
