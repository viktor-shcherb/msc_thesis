# A.2 ALiBi Results on WikiText-103 [p. 19-20]

## Figure 8

**Figure 8** (p. 19): "The training speed and validation perplexity (with $L_{valid}$ = 3072) for ALiBi models and the sinusoidal model trained with $L$ = 3072. All our models trained on 512 or more tokens achieve better perplexity than the sinusoidal model even though all of them (except the $L$ = 3072) require less time and memory to train."

The figure is a scatter plot titled "Training Speed vs. Valid Perplexity with $L_{valid}$ = 3072":
- x-axis: Training Words Per Second (right arrow), range approximately 15000 to 30000
- y-axis: Perplexity (down arrow, lower is better), range approximately 17.5 to 19.0
- Sinusoidal baseline: single orange square at approximately (15000, 18.7) labeled "$L$ = 3072"
- ALiBi models: blue x markers at various points:
  - $L$ = 3072 at approximately (15500, 17.6)
  - $L$ = 2048 at approximately (20000, 17.65)
  - $L$ = 1536 at approximately (23000, 17.7)
  - $L$ = 1024 at approximately (26000, 18.0)
  - $L$ = 512 at approximately (28000, 18.35)
- Key observation: All ALiBi models with $512 \leq L < 3072$ are faster to train than the sinusoidal model with $L$ = 3072, but they all achieve better perplexity scores on the validation set.

[p. 19]

Figure 8 depicts a cross section of Figure 4, showing ALiBi models with different train lengths and the sinusoidal baseline, all evaluated on $L_{valid}$ = 3072 tokens. All ALiBi models with $512 \leq L < 3072$ are faster to train than the sinusoidal model with $L$ = 3072, but they all achieve greater perplexity scores on the validation set. The ALiBi model with $L$ = 3072 trains just as fast as the sinusoidal one but bests its score by more than one perplexity point; the standard deviation for the sinusoidal model with $L$ = 3072 is 0.24. [p. 19]

## Table 5

**Table 5** (p. 19): "Perplexity when ALiBi extrapolates on the WikiText-103 development set. *For results we present for the sinusoidal, rotary and T5 bias models, $L = L_{valid}$ (so we do not test the extrapolation abilities of those baselines here)."

Table 5 shows the perplexity values obtained when 8 different ALiBi models, trained on $L$ values between 64 and 3072, extrapolating to $L_{valid}$ values longer than the ones they were trained on. In addition, results are presented for the sinusoidal, rotary and T5 bias models, with $L_{valid} = L$. [p. 19]

|  | Evaluation Length |||||||
| ALiBi Train Length | 64 | 128 | 256 | 512 | 1024 | 1536 | 2048 | 3072 |
|---|---|---|---|---|---|---|---|---|
| 64 | 28.46 | 24.70 | 22.88 | 22.09 | 21.73 | 21.63 | 21.59 | 21.53 |
| 128 | - | 23.98 | 21.70 | 20.67 | 20.36 | 20.29 | 20.31 | 20.28 |
| 256 | - | - | **21.29** | 19.89 | 19.29 | 19.13 | 19.10 | 19.03 |
| 512 | - | - | - | 19.73 | 18.81 | 18.50 | 18.48 | 18.40 |
| 1024 | - | - | - | - | **18.66** | 18.20 | 18.05 | 17.96 |
| 1536 | - | - | - | - | - | **18.12** | 17.90 | 17.72 |
| 2048 | - | - | - | - | - | - | **17.91** | 17.64 |
| 3072 | - | - | - | - | - | - | - | **17.60** |
| Sinusoidal* | **28.03** | **23.81** | 21.45 | 20.05 | 19.34 | 19.05 | 18.87 | 18.67 |
| Rotary* | - | - | - | 20.07 | 19.33 | - | - | 18.57 |
| T5 Bias* | - | - | - | **19.65** | 18.80 | - | - | 18.01 |

Note: Bold values indicate best score for each evaluation length column. Dashes indicate configurations not tested (model not trained at that length or longer).

## Table 6

**Table 6** (p. 20): "Test perplexity and runtime on WikiText-103 for two of our ALiBi models and models that use the sinusoidal, rotary and T5 bias methods."

| Model | Param. | Train Speed | Inference Speed | Valid | Test |
|---|---|---|---|---|---|
| Sinusoidal, $L$ = 3072 | **247M** | 15.3k | **13.6k** | 18.67 | 19.38 |
| Rotary, $L$ = 3072 | **247M** | **11.5k** | 12.2k | 18.57 | 19.28 |
| T5 Bias, $L$ = 3072 | **247M** | 4.3k | 7.3k | 18.01 | 18.73 |
| ALiBi, $L$ = 512, $L_{valid}$ = 3072 | **247M** | 28.3k | **13.6k** | 18.40 | 19.08 |
| ALiBi, $L$ = 3072, $L_{valid}$ = 3072 | **247M** | 15.5k | **13.6k** | **17.60** | **18.30** |

Note: Train Speed and Inference Speed are measured in words per second (up arrow = higher is better). Valid and Test are perplexity (down arrow = lower is better). [p. 20]

Table 6 compares ALiBi to the sinusoidal, rotary and T5 bias baselines on the test set of WikiText-103, and Table 7 compares ALiBi to the current state of the art models on that test set. [p. 19]

## Table 7

**Table 7** (p. 20): "Valid and test perplexity scores on WikiText-103 for two of our ALiBi models and models that use the sinusoidal, rotary and T5 bias methods with sliding window evaluation (section B and S=512 following Baevski & Auli (2018), Khandelwal et al. (2020), Press et al. (2021)). The sinusoidal model presents our results from training and inference with the model of Baevski & Auli."

| Model | Param. | Valid | Test |
|---|---|---|---|
| Adaptive Inputs (Baevski & Auli, 2018) | **247M** | 17.97 | 18.70 |
| Transformer-XL (Dai et al., 2019) | 257M | - | 18.3 |
| Shortformer (Press et al., 2021) | **247M** | 17.47 | 18.15 |
| Sandwich Transformer (Press et al., 2020) | **247M** | - | 17.96 |
| Staged Training (Press et al., 2021) | **247M** | - | 17.56 |
| Compressive Transformer (Rae et al., 2020) | 329M | - | 17.1 |
| Routing Transformer (Roy et al., 2020) | - | - | 15.8 |
| kNN-LM (Khandelwal et al., 2020) | **247M** | 15.81 | **15.79** |
| Sinusoidal, $L$ = 3072 | **247M** | 17.95 | 18.67 |
| Rotary, $L$ = 3072 | **247M** | 17.98 | 18.72 |
| T5 Bias, $L$ = 3072 | **247M** | 17.37 | 18.12 |
| ALiBi, $L$ = 512, $L_{valid}$ = 3072 | **247M** | 18.30 | 19.01 |
| ALiBi, $L$ = 3072, $L_{valid}$ = 3072 | **247M** | **16.97** | 17.66 |

Note: Valid and Test are perplexity (down arrow = lower is better). [p. 20]
