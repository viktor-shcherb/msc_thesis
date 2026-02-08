# A.3 Results on the Toronto Book Corpus [p. 20-21]

[p. 20]

To ensure that results are not specific to the WikiText-103 corpus, the authors apply the model and the baselines to a different domain while using a similar model architecture and the same ALiBi slopes as those used in the previous subsection.

The authors emphasize that the set of slopes was chosen by running experiments on the WikiText-103 corpus, and here they apply that set of slopes to a model trained on a very different text domain. Throughout the entire process of developing this method, they ran only one set of experiments on this domain using the previously selected set of slopes.

Specifically, they use the Toronto BooksCorpus (Zhu et al., 2015), which has been used to train BERT (Devlin et al., 2019) (in conjunction with the English Wikipedia). The corpus is about 700M tokens (2.9 GB).

They use the same train/validation/test split as Khandelwal et al. (2020) and their tokenization, which uses BERT's vocabulary of 29K byte-pair encodings. Since the vocabulary is much smaller than WikiText-103's, they replace the adaptive word embedding and softmax of Baevski & Auli (2018) with a tied word embedding and softmax matrix (Press & Wolf, 2017; Inan et al., 2017).

[p. 21]

Results in Figure 9 (and Table 8) replicate the success on the WikiText-103 dataset. The ALiBi model surpasses the sinusoidal baseline when trained on the same amount of input tokens ($L$) and, in addition, the model is able to extrapolate to longer sequences at inference. This occurs even though the set of slopes was *not* tuned on this dataset. This result establishes the generality of ALiBi and the particular set of slopes they found and suggests that they may be used on different text domains without further hyperparameter tuning. [p. 21]

Tables 9 and 10 present the perplexities for the ALiBi models, the baselines, and the current state of the art on the Toronto BookCorpus validation and test sets. The results here mirror the results on WikiText-103: they improve over the sinusoidal baseline even when ALiBi is trained on fewer tokens. [p. 21]

## Figure 9

**Figure 9** (p. 21): "ALiBi-enabled models evaluated on different input lengths on the Toronto BookCorpus. Our models extrapolate to longer sequence lengths and outperform the sinusoidal baseline even when trained on much shorter sequences."

The figure is a line plot titled "ALiBi Extrapolating on Toronto BookCorpus":
- x-axis: Validation Input Length ($L_{valid}$), values: 512, 1024, 3072
- y-axis: Perplexity (down arrow, lower is better), range approximately 13.0 to 15.0
- ALiBi lines (dashed with markers):
  - $L$ = 512: starts at approximately 14.3 at 512, decreases to approximately 13.6 at 1024, then approximately 13.55 at 3072
  - $L$ = 1024: starts at approximately 13.85 at 1024, decreases to approximately 13.5 at 3072
  - $L$ = 3072: single point at approximately 13.15 at 3072
- Sinusoidal baselines (square markers):
  - Sinusoidal, $L$ = 512: approximately 14.8 at 512
  - Sinusoidal, $L$ = 1024: approximately 14.7 at 1024
  - Sinusoidal, $L$ = 3072: approximately 14.45 at 3072
- Key observation: All ALiBi models achieve lower perplexity than the corresponding sinusoidal models, and ALiBi models extrapolate well to longer sequences.

## Table 8

**Table 8** (p. 21): "ALiBi models extrapolating on the Toronto BookCorpus development set. *For the results of the sinusoidal models, $L = L_{valid}$ (so we do not test the extrapolation abilities of those models here)."

|  | Evaluation Length ||
| Train Length | 512 | 1024 | 3072 |
|---|---|---|---|
| 512 | 14.29 | 13.64 | 13.55 |
| 1024 | - | 13.86 | 13.52 |
| 3072 | - | - | 13.15 |
| Sinusoidal* | 14.80 | 14.73 | 14.46 |

## Table 9

**Table 9** (p. 21): "Validation and test perplexities on the Toronto Book Corpus dataset."

| Model | Param. | Valid | Test |
|---|---|---|---|
| Sinusoidal, L = 3072 | **247M** | 14.46 | 11.67 |
| ALiBi, $L_{train}$ = 512, $L_{valid}$ = 3072 | **247M** | 13.55 | 10.98 |
| ALiBi, $L_{train}$ = 3072, $L_{valid}$ = 3072 | **247M** | **13.15** | **10.73** |

Note: Valid and Test are perplexity (down arrow = lower is better). [p. 21]

---
[p. 22 continued]

## Table 10

**Table 10** (p. 22): "Validation and test perplexities on the Toronto Book Corpus dataset with a sliding window (§B). Following (Baevski & Auli, 2018; Khandelwal et al., 2020; Press et al., 2020; 2021), we set the sliding window stride S=512."

| Model | Param. | Valid | Test |
|---|---|---|---|
| kNN-LM (Khandelwal et al., 2020) | **247M** | 14.20 | 10.89 |
| Shortformer (Press et al., 2021) | **247M** | 13.40 | 10.88 |
| Sandwich (Press et al., 2020) | **247M** | - | 10.83 |
| Staged Training (Press et al., 2021) | **247M** | 12.80 | 10.48 |
| Sinusoidal, L = 3072 | **247M** | 14.06 | 11.40 |
| ALiBi, $L$ = 512, $L_{valid}$ = 3072 | **247M** | 13.76 | 11.11 |
| ALiBi, $L$ = 3072, $L_{valid}$ = 3072 | **247M** | **12.70** | **10.40** |

Note: Valid and Test are perplexity (down arrow = lower is better). [p. 22]
