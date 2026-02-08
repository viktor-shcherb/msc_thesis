# Appendix B. Comparing DeepSeekMoE with Larger Models [p. 31-32]

[p. 31] Comparisons among DeepSeekMoE, GShard x1.2, and GShard x1.5 are shown in Table 8. Comparisons among DeepSeekMoE, Dense x4, and Dense x16 are shown in Table 9.

## Table 8: Comparison with Larger GShard Models (2B Scale)

**Table 8** (p. 31): Comparison between DeepSeekMoE and larger GShard models.

| Metric | # Shot | GShard x1.2 | GShard x1.5 | DeepSeekMoE |
|---|---|---|---|---|
| Relative Expert Size | N/A | 1.2 | 1.5 | 0.25 |
| # Experts | N/A | 0 + 16 | 0 + 16 | 1 + 63 |
| # Activated Experts | N/A | 0 + 2 | 0 + 2 | 1 + 7 |
| # Total Expert Params | N/A | 2.3B | 2.8B | 1.9B |
| # Activated Expert Params | N/A | 0.28B | 0.35B | 0.24B |
| # Training Tokens | N/A | 100B | 100B | 100B |
| Pile (Loss) | N/A | 1.824 | **1.808** | **1.808** |
| HellaSwag (Acc.) | 0-shot | 53.7 | 54.4 | **54.8** |
| PIQA (Acc.) | 0-shot | 71.8 | 71.1 | **72.3** |
| ARC-easy (Acc.) | 0-shot | 46.8 | 47.3 | **49.4** |
| ARC-challenge (Acc.) | 0-shot | 31.7 | **34.1** | **34.3** |
| RACE-middle (Acc.) | 5-shot | 43.7 | **46.4** | 44.0 |
| RACE-high (Acc.) | 5-shot | 31.9 | **32.4** | 31.7 |
| HumanEval (Pass@1) | 0-shot | 3.7 | 3.0 | **4.9** |
| MBPP (Pass@1) | 3-shot | 2.4 | **2.6** | 2.2 |
| TriviaQA (EM) | 5-shot | 15.2 | 15.7 | **16.6** |
| NaturalQuestions (EM) | 5-shot | 4.5 | 4.7 | **5.7** |

## Table 9: Comparison with Larger Dense Baselines (2B Scale)

[p. 32] Comparison between DeepSeekMoE and larger dense baselines.

**Table 9** (p. 32): Comparison between DeepSeekMoE and larger dense baselines.

| Metric | # Shot | Dense x4 | Dense x16 | DeepSeekMoE |
|---|---|---|---|---|
| Relative Expert Size | N/A | 1 | 1 | 0.25 |
| # Experts | N/A | 4 + 0 | 16 + 0 | 1 + 63 |
| # Activated Experts | N/A | 4 + 0 | 16 + 0 | 1 + 7 |
| # Total Expert Params | N/A | 0.47B | 1.89B | 1.89B |
| # Activated Expert Params | N/A | 0.47B | 1.89B | 0.24B |
| # Training Tokens | N/A | 100B | 100B | 100B |
| Pile (Loss) | N/A | 1.908 | **1.806** | 1.808 |
| HellaSwag (Acc.) | 0-shot | 47.6 | **55.1** | 54.8 |
| PIQA (Acc.) | 0-shot | 70.0 | 71.9 | **72.3** |
| ARC-easy (Acc.) | 0-shot | 43.9 | **51.9** | 49.4 |
| ARC-challenge (Acc.) | 0-shot | 30.5 | 33.8 | **34.3** |
| RACE-middle (Acc.) | 5-shot | 42.4 | **46.3** | 44.0 |
| RACE-high (Acc.) | 5-shot | 30.7 | **33.0** | 31.7 |
| HumanEval (Pass@1) | 0-shot | 1.8 | 4.3 | **4.9** |
| MBPP (Pass@1) | 3-shot | 0.2 | **2.2** | **2.2** |
| TriviaQA (EM) | 5-shot | 9.9 | **16.5** | 16.6 |
| NaturalQuestions (EM) | 5-shot | 3.0 | **6.3** | 5.7 |

## Table 10: Comparison at Larger Scale (13B Total Parameters)

[p. 32] At a larger scale of 13B total parameters, DeepSeekMoE is compared with GShard x1.2 and GShard x1.5, and the results are shown in Table 10. At a larger scale, DeepSeekMoE even outperforms GShard x1.5 distinctly.

**Table 10** (p. 32): Comparison between DeepSeekMoE and larger GShard models at a larger scale.

| Metric | # Shot | GShard x1.2 | GShard x1.5 | DeepSeekMoE |
|---|---|---|---|---|
| Relative Expert Size | N/A | 1.2 | 1.5 | 0.25 |
| # Experts | N/A | 0 + 16 | 0 + 16 | 1 + 63 |
| # Activated Experts | N/A | 0 + 2 | 0 + 2 | 1 + 7 |
| # Total Expert Params | N/A | 15.9B | 19.8B | 13.3B |
| # Activated Expert Params | N/A | 2.37B | 2.82B | 2.05B |
| # Training Tokens | N/A | 100B | 100B | 100B |
| HellaSwag (Acc.) | 0-shot | 66.6 | 67.7 | **69.1** |
| PIQA (Acc.) | 0-shot | 75.6 | **76.0** | **75.7** |
| ARC-easy (Acc.) | 0-shot | 56.8 | 56.8 | **58.8** |
| ARC-challenge (Acc.) | 0-shot | **39.9** | 37.6 | **38.5** |
| RACE-middle (Acc.) | 5-shot | 51.6 | 50.6 | **52.4** |
| RACE-high (Acc.) | 5-shot | 37.4 | 36.3 | **38.5** |
| HumanEval (Pass@1) | 0-shot | 6.1 | 6.1 | **9.8** |
| MBPP (Pass@1) | 3-shot | 7.0 | **11.6** | 10.6 |
| TriviaQA (EM) | 5-shot | 36.5 | 36.7 | **38.2** |
| NaturalQuestions (EM) | 5-shot | 12.6 | 12.1 | **13.7** |
