# A.4 Results on the CC100+RoBERTa Corpus [p. 21-22]

[p. 21]

Table 11 compares the 1.3 billion parameter ALiBi models when extrapolating to two times the number of tokens that they were trained on. The sinusoidal model is used as the baseline, trained for the same amount of time as the ALiBi model that it is compared to (and so since ALiBi models run faster in this setting, the sinusoidal models complete less updates).

[p. 22]

## Table 11

**Table 11** (p. 22): "Perplexity, memory, and train time on the CC100+RoBERTa corpus for our ALiBi models and the sinusoidal baseline. We run our $L$ = 512 (1024) model and the sinusoidal model with $L$ = 1024 (2048) for the same amount of time. We show that our models achieve strong results even though they use 6–11% less memory."

| | Training ||| Valid PPL ||
| | Memory | Updates | Hours | $L_{valid}$ = 1024 | $L_{valid}$ = 2048 |
|---|---|---|---|---|---|
| Sinusoidal, $L_{train}$ = 1024 | 26.2 GB | 46.7k | 5.5k | **9.24** | - |
| ALiBi, $L_{train}$ = 512 | **24.6 GB** | 50.0k | 5.5k | 9.30 | - |
| Sinusoidal, $L_{train}$ = 2048 | 29.3 GB | 44.2k | 5.9k | - | 9.01 |
| ALiBi, $L_{train}$ = 1024 | **26.2 GB** | 50.0k | 5.9k | - | **8.92** |

Note: Memory (down arrow = lower is better), Hours (down arrow = lower is better), Valid PPL (down arrow = lower is better). Bold highlights best value in each comparison pair. [p. 22]

Table 12 compares the 1.3 billion parameter ALiBi models to the sinusoidal baselines, with and without extrapolation, with all models completing 50,000 updates. [p. 22]

## Table 12

**Table 12** (p. 22): "Perplexity, train time and memory use of the sinusoidal and ALiBi models on the CC100+RoBERTa corpus when all models are trained with 50k updates."

| | Training ||| Valid PPL |||
| | Memory | Updates | Hours | $L_{valid}$ = 512 | $L_{valid}$ = 1024 | $L_{valid}$ = 2048 |
|---|---|---|---|---|---|---|
| Sinusoidal, $L_{train}$ = 512 | 24.6 GB | 50.0k | 5.5k | 9.71 | 37.05 | 105.42 |
| ALiBi, $L_{train}$ = 512 | 24.6 GB | 50.0k | 5.5k | 9.79 | 9.30 | 9.54 |
| Sinusoidal, $L_{train}$ = 1024 | 26.2 GB | 50.0k | 5.9k | - | 9.15 | 48.85 |
| ALiBi, $L_{train}$ = 1024 | 26.2 GB | 50.0k | 5.9k | - | 9.16 | **8.92** |
| Sinusoidal, $L_{train}$ = 2048 | 29.3 GB | 50.0k | 6.7k | - | - | 8.83 |
| ALiBi, $L_{train}$ = 2048 | 29.4 GB | 50.0k | 6.7k | - | - | 8.84 |

Note: Memory (down arrow = lower is better), Hours (down arrow = lower is better), Valid PPL (down arrow = lower is better). When the sinusoidal model extrapolates (evaluates on longer sequences than it was trained on), perplexity explodes (e.g., 37.05, 105.42, 48.85), whereas ALiBi maintains strong perplexity under extrapolation. [p. 22]
