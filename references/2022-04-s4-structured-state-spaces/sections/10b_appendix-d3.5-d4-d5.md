# D.3.5 Time Series Forecasting compared to Informer [p. 30]

## Figure 5

**Figure 5** (p. 30): "Comparison of S4 and specialized time-series models for forecasting tasks. (Top Left) The forecasting task involves predicting future values of a time-series given past context. (Bottom Left) We perform simple forecasting using a sequence model such as S4 as a black box. (Right) Informer uses an encoder-decoder architecture designed specifically for forecasting problems involving a customized attention module (figure taken from Zhou et al. [50])."

The figure shows two architectural approaches side by side:
- **Left panels:** S4 approach. Top left shows the forecasting task (Context window followed by Forecast window over a time-series). Bottom left shows S4 as a simple black box: Context is fed in, and the model outputs the Forecast directly.
- **Right panel:** Informer architecture with an encoder-decoder structure. The encoder has multiple layers of Multi-head ProbSparse Self-attention with a "Dependency pyramid." The decoder has Multi-head Attention, Masked Multi-head ProbSparse Self-attention, and a Fully Connected Layer producing Outputs. Inputs to the encoder are $X_{\text{feed\_en}}$ and inputs to the decoder are $X_{\text{feed\_de}} = \{X_{\text{token}}, X_0\}$.

## Forecasting Approach

[p. 30]

A simple figure (Fig. 5) contrasting the architecture of S4 against that of the Informer [50] is included.

In Fig. 5, the goal is to forecast a contiguous range of future predictions (Green, length $F$) given a range of past context (Blue, length $C$). The entire context is simply concatenated with a sequence of masks set to the length of the forecast window. This input is a single sequence of length $C + F$ that is run through the same simple deep S4 model used throughout this work, which maps to an output of length $C + F$. The last $F$ outputs are then used as the forecasted predictions.

Tables 13 and 14 contain full results on all 50 settings considered by Zhou et al. [50]. S4 sets the best results on 40 out of 50 of these settings.

## Table 13: Univariate Long Sequence Time-Series Forecasting

**Table 13** (p. 31): "Univariate long sequence time-series forecasting results on four datasets (five cases)."

Methods compared: S4, Informer, Informer$^\dagger$, LogTrans, Reformer, LSTMa, DeepAR, ARIMA, Prophet. Metrics: MSE and MAE. Bold indicates best result.

### ETTh1

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | DeepAR MSE | DeepAR MAE | ARIMA MSE | ARIMA MAE | Prophet MSE | Prophet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|-----------|-----------|-------------|-------------|
| 24  | **0.061** | **0.191** | 0.098 | 0.247 | 0.092 | 0.246 | 0.103 | 0.259 | 0.222 | 0.389 | 0.114 | 0.272 | 0.107 | 0.280 | 0.108 | 0.284 | 0.115 | 0.275 |
| 48  | **0.079** | **0.220** | 0.158 | 0.319 | 0.161 | 0.322 | 0.167 | 0.328 | 0.284 | 0.445 | 0.193 | 0.358 | 0.162 | 0.327 | 0.175 | 0.424 | 0.168 | 0.330 |
| 168 | **0.104** | **0.258** | 0.183 | 0.346 | 0.187 | 0.355 | 0.207 | 0.375 | 1.522 | 1.191 | 0.236 | 0.392 | 0.239 | 0.422 | 0.396 | 0.504 | 1.224 | 0.763 |
| 336 | **0.080** | **0.229** | 0.222 | 0.387 | 0.215 | 0.369 | 0.230 | 0.398 | 1.860 | 1.124 | 0.580 | 0.698 | 0.445 | 0.552 | 0.468 | 0.593 | 1.549 | 1.820 |
| 720 | **0.116** | **0.271** | 0.269 | 0.435 | 0.257 | 0.421 | 0.273 | 0.463 | 2.112 | 1.436 | 0.683 | 0.768 | 0.658 | 0.707 | 0.659 | 0.766 | 2.735 | 3.253 |

### ETTh2

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | DeepAR MSE | DeepAR MAE | ARIMA MSE | ARIMA MAE | Prophet MSE | Prophet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|-----------|-----------|-------------|-------------|
| 24  | 0.095 | 0.234 | **0.093** | **0.240** | 0.099 | 0.241 | 0.102 | 0.255 | 0.263 | 0.437 | 0.155 | 0.307 | 0.098 | 0.263 | 3.554 | 0.445 | 0.199 | 0.381 |
| 48  | 0.191 | 0.346 | **0.155** | **0.314** | 0.159 | 0.317 | 0.169 | 0.348 | 0.458 | 0.545 | 0.190 | 0.348 | 0.163 | 0.341 | 3.190 | 0.474 | 0.304 | 0.462 |
| 168 | **0.167** | **0.333** | 0.232 | 0.389 | 0.235 | 0.390 | 0.246 | 0.422 | 1.029 | 0.879 | 0.385 | 0.514 | 0.255 | 0.414 | 2.800 | 0.595 | 2.145 | 1.068 |
| 336 | **0.189** | **0.361** | 0.263 | 0.417 | 0.258 | 0.423 | 0.267 | 0.437 | 1.668 | 1.228 | 0.558 | 0.606 | 0.604 | 0.607 | 2.753 | 0.738 | 2.096 | 2.543 |
| 720 | **0.187** | **0.358** | 0.277 | 0.431 | 0.285 | 0.442 | 0.303 | 0.493 | 2.030 | 1.721 | 0.640 | 0.681 | 0.429 | 0.580 | 2.878 | 1.044 | 3.355 | 4.664 |

### ETTm1

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | DeepAR MSE | DeepAR MAE | ARIMA MSE | ARIMA MAE | Prophet MSE | Prophet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|-----------|-----------|-------------|-------------|
| 24  | **0.024** | **0.117** | 0.030 | 0.137 | 0.034 | 0.160 | 0.065 | 0.202 | 0.095 | 0.228 | 0.121 | 0.233 | 0.091 | 0.243 | 0.090 | 0.206 | 0.120 | 0.290 |
| 48  | **0.051** | **0.174** | 0.069 | 0.203 | 0.066 | 0.194 | 0.078 | 0.220 | 0.249 | 0.390 | 0.305 | 0.411 | 0.219 | 0.362 | 0.179 | 0.306 | 0.133 | 0.305 |
| 96  | **0.086** | **0.229** | 0.194 | 0.372 | 0.187 | 0.384 | 0.199 | 0.386 | 0.920 | 0.767 | 0.287 | 0.420 | 0.364 | 0.496 | 0.272 | 0.399 | 0.194 | 0.396 |
| 288 | **0.160** | **0.327** | 0.401 | 0.554 | 0.409 | 0.548 | 0.411 | 0.572 | 1.108 | 1.245 | 0.524 | 0.584 | 0.948 | 0.795 | 0.462 | 0.558 | 0.452 | 0.571 |
| 672 | **0.292** | **0.466** | 0.512 | 0.644 | 0.519 | 0.665 | 0.598 | 0.702 | 1.793 | 1.528 | 1.064 | 0.873 | 2.437 | 1.352 | 0.639 | 0.697 | 2.747 | 1.174 |

### Weather

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | DeepAR MSE | DeepAR MAE | ARIMA MSE | ARIMA MAE | Prophet MSE | Prophet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|-----------|-----------|-------------|-------------|
| 24  | 0.125 | 0.254 | **0.117** | **0.251** | 0.238 | 0.368 | 0.136 | 0.279 | 0.231 | 0.401 | 0.131 | 0.254 | 0.128 | 0.274 | 0.219 | 0.355 | 0.302 | 0.433 |
| 48  | **0.151** | **0.305** | 0.178 | 0.318 | 0.185 | 0.316 | 0.206 | 0.356 | 0.328 | 0.423 | 0.190 | 0.334 | 0.203 | 0.353 | 0.273 | 0.409 | 0.445 | 0.536 |
| 168 | **0.198** | **0.333** | 0.266 | 0.398 | 0.260 | 0.404 | 0.309 | 0.439 | 0.654 | 0.634 | 0.341 | 0.448 | 0.293 | 0.551 | 0.503 | 0.599 | 2.441 | 1.142 |
| 336 | 0.300 | 0.417 | **0.297** | **0.416** | 0.310 | 0.422 | 0.359 | 0.484 | 1.792 | 1.093 | 0.456 | 0.554 | 0.585 | 0.644 | 0.728 | 0.730 | 1.987 | 2.468 |
| 720 | **0.245** | **0.375** | 0.359 | 0.466 | 0.361 | 0.471 | 0.388 | 0.499 | 2.087 | 1.534 | 0.866 | 0.809 | 0.499 | 0.596 | 1.062 | 0.943 | 3.859 | 1.144 |

### ECL

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | DeepAR MSE | DeepAR MAE | ARIMA MSE | ARIMA MAE | Prophet MSE | Prophet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|-----------|-----------|-------------|-------------|
| 48  | **0.222** | **0.350** | 0.239 | 0.359 | 0.238 | 0.368 | 0.280 | 0.429 | 0.971 | 0.884 | 0.493 | 0.539 | 0.204 | 0.357 | 0.879 | 0.764 | 0.524 | 0.595 |
| 168 | **0.331** | **0.421** | 0.447 | 0.503 | 0.442 | 0.514 | 0.454 | 0.529 | 1.671 | 1.587 | 0.723 | 0.653 | **0.315** | 0.436 | 1.032 | 0.833 | 2.725 | 1.273 |
| 336 | **0.328** | **0.422** | 0.489 | 0.528 | 0.501 | 0.552 | 0.514 | 0.563 | 3.528 | 2.196 | 1.212 | 0.898 | 0.414 | 0.519 | 1.136 | 0.876 | 2.246 | 3.077 |
| 720 | **0.428** | **0.494** | 0.540 | 0.571 | 0.543 | 0.578 | 0.558 | 0.609 | 4.891 | 4.047 | 1.511 | 0.966 | 0.563 | 0.595 | 1.251 | 0.933 | 4.243 | 1.415 |
| 960 | **0.432** | **0.497** | 0.582 | 0.608 | 0.594 | 0.638 | 0.624 | 0.645 | 7.019 | 5.105 | 1.545 | 1.006 | 0.657 | 0.683 | 1.370 | 0.982 | 6.901 | 4.264 |

**Count** (number of settings where each method is best): S4: 22, Informer: 5, Informer$^\dagger$: 0, LogTrans: 0, Reformer: 0, LSTMa: 0, DeepAR: 2, ARIMA: 0, Prophet: 0.

## Table 14: Multivariate Long Sequence Time-Series Forecasting

**Table 14** (p. 32): "Multivariate long sequence time-series forecasting results on four datasets (five cases)."

Methods compared: S4, Informer, Informer$^\dagger$, LogTrans, Reformer, LSTMa, LSTnet. Metrics: MSE and MAE. Bold indicates best result.

### ETTh1

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | LSTnet MSE | LSTnet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|
| 24  | **0.525** | **0.542** | 0.577 | 0.549 | 0.620 | 0.577 | 0.686 | 0.604 | 0.991 | 0.754 | 0.650 | 0.624 | 1.293 | 0.901 |
| 48  | **0.641** | **0.615** | 0.685 | 0.625 | 0.692 | 0.671 | 0.766 | 0.757 | 1.313 | 0.906 | 0.702 | 0.675 | 1.456 | 0.960 |
| 168 | 0.980 | 0.779 | **0.931** | **0.752** | 0.947 | 0.797 | 1.002 | 0.846 | 1.824 | 1.138 | 1.212 | 0.867 | 1.997 | 1.214 |
| 336 | 1.407 | 0.910 | 1.128 | 0.873 | **1.094** | **0.813** | 1.362 | 0.952 | 2.117 | 1.280 | 1.424 | 0.994 | 2.655 | 1.369 |
| 720 | **1.162** | **0.842** | 1.215 | 0.896 | 1.241 | 0.917 | 1.397 | 1.291 | 2.415 | 1.520 | 1.960 | 1.322 | 2.143 | 1.380 |

### ETTh2

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | LSTnet MSE | LSTnet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|
| 24  | 0.871 | 0.736 | **0.720** | **0.665** | 0.753 | 0.727 | 0.828 | 0.730 | 1.531 | 1.613 | 1.143 | 0.813 | 2.742 | 1.457 |
| 48  | **1.240** | **0.867** | 1.457 | 1.001 | 1.461 | 1.077 | 1.806 | 1.034 | 1.871 | 1.735 | 1.671 | 1.221 | 3.567 | 1.687 |
| 168 | **2.580** | **1.255** | 3.489 | 1.515 | 3.485 | 1.612 | 4.070 | 1.681 | 4.660 | 1.846 | 4.117 | 1.674 | 3.242 | 2.513 |
| 336 | **1.980** | **1.128** | 2.723 | 1.340 | 2.626 | 1.285 | 3.875 | 1.763 | 4.028 | 1.688 | 3.434 | 1.549 | 2.544 | 2.591 |
| 720 | **2.650** | **1.340** | 3.467 | 1.473 | 3.548 | 1.495 | 3.913 | 1.552 | 5.381 | 2.015 | 3.963 | 1.788 | 4.625 | 3.709 |

### ETTm1

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | LSTnet MSE | LSTnet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|
| 24  | 0.426 | 0.487 | 0.323 | **0.369** | **0.306** | 0.371 | 0.419 | 0.412 | 0.724 | 0.607 | 0.621 | 0.629 | 1.968 | 1.170 |
| 48  | 0.580 | 0.565 | 0.494 | 0.503 | **0.465** | **0.470** | 0.507 | 0.583 | 1.098 | 0.777 | 1.392 | 0.939 | 1.999 | 1.215 |
| 96  | 0.699 | 0.649 | **0.678** | 0.614 | 0.681 | **0.612** | 0.768 | 0.792 | 1.433 | 0.945 | 1.339 | 0.913 | 2.762 | 1.542 |
| 288 | **0.824** | **0.674** | 1.056 | 0.786 | 1.162 | 0.879 | 1.462 | 1.320 | 1.820 | 1.094 | 1.740 | 1.124 | 1.257 | 2.076 |
| 672 | **0.846** | **0.709** | 1.192 | 0.926 | 1.231 | 1.103 | 1.669 | 1.461 | 2.187 | 1.232 | 2.736 | 1.555 | 1.917 | 2.941 |

### Weather

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | LSTnet MSE | LSTnet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|
| 24  | **0.334** | **0.381** | 0.335 | 0.381 | 0.349 | 0.397 | 0.435 | 0.477 | 0.655 | 0.583 | 0.546 | 0.570 | 0.615 | 0.545 |
| 48  | 0.406 | 0.433 | 0.395 | 0.459 | **0.386** | **0.433** | 0.426 | 0.666 | 0.729 | 0.666 | 0.829 | 0.677 | 0.660 | 0.589 |
| 168 | **0.525** | **0.527** | 0.608 | 0.567 | 0.613 | 0.582 | 0.727 | 0.671 | 1.318 | 0.855 | 1.038 | 0.835 | 0.748 | 0.647 |
| 336 | **0.531** | **0.539** | 0.702 | 0.620 | 0.634 | 0.634 | 0.754 | 0.670 | 1.930 | 1.167 | 1.657 | 1.059 | 0.782 | 0.683 |
| 720 | **0.578** | **0.578** | 0.831 | 0.731 | 0.834 | 0.741 | 0.885 | 0.773 | 2.726 | 1.575 | 1.536 | 1.109 | 0.851 | 0.757 |

### ECL

| Horizon | S4 MSE | S4 MAE | Informer MSE | Informer MAE | Informer$^\dagger$ MSE | Informer$^\dagger$ MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | LSTnet MSE | LSTnet MAE |
|---------|--------|--------|--------------|--------------|------------------------|------------------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|
| 48  | **0.255** | **0.352** | 0.344 | 0.393 | 0.334 | 0.399 | 0.355 | 0.418 | 1.404 | 0.999 | 0.486 | 0.572 | 0.369 | 0.445 |
| 168 | **0.283** | **0.373** | 0.368 | 0.424 | 0.353 | 0.420 | 0.368 | 0.432 | 1.515 | 1.069 | 0.574 | 0.602 | 0.394 | 0.476 |
| 336 | **0.292** | **0.382** | 0.381 | 0.431 | 0.381 | 0.439 | 0.373 | 0.439 | 1.601 | 1.104 | 0.886 | 0.795 | 0.419 | 0.477 |
| 720 | **0.289** | **0.377** | 0.406 | 0.443 | 0.391 | 0.438 | 0.409 | 0.454 | 2.009 | 1.170 | 1.676 | 1.095 | 0.556 | 0.565 |
| 960 | **0.299** | **0.387** | 0.460 | 0.548 | 0.492 | 0.550 | 0.477 | 0.589 | 2.141 | 1.387 | 1.591 | 1.128 | 0.605 | 0.599 |

**Count** (number of settings where each method is best): S4: 18, Informer: 5, Informer$^\dagger$: 6, LogTrans: 0, Reformer: 0, LSTMa: 0, LSTnet: 0.

---

# D.4 Visualizations [p. 30]

[p. 30]

The convolutional filter $\bar{K}$ learned by S4 for the Pathfinder and CIFAR-10 tasks is visualized in Appendix D.4.

## Figure 6

**Figure 6** (p. 32): "(Convolutional filters on Pathfinder) A random selection of filters learned by S4 in the first layer (top 2 rows) and last layer (bottom 2 rows) of the best model."

The figure shows a 4x8 grid of grayscale filter visualizations. The top 2 rows (first layer filters) show varied patterns including smooth gradients, oscillatory patterns, and some with high-frequency striped structures. The bottom 2 rows (last layer filters) show more structured, often diagonal striped patterns with clear directional orientations, suggesting the model learns increasingly structured spatial features at deeper layers.

---

# D.5 Reproduction [p. 30–31]

[p. 30]

Since the first version of this paper, several experiments have been updated. The corresponding paragraph below should be read before citing LRA or SC results.

## Long Range Arena

Follow-ups to this paper expanded the theoretical understanding of S4 while improving some results. The results reported in Table 4 have been updated to results from the papers [19, 20]. More specifically, the method S4-LegS in those works refers to the *same model* presented in this paper, with the "-LegS" suffix referring to the initialization defined in equation (2). As such, results from the original Table 4 have been directly updated.

[p. 31]

The updated results have only minor hyperparameter changes compared to the original results. The original results and hyperparameters are shown in Table 10 (Appendix D.2). Appendix B of [19] describes the changes in hyperparameters, which are also documented from the experiment configuration files in the publically available code at https://github.com/HazyResearch/state-spaces.

## Speech Commands

The Speech Commands (SC) dataset [47] is originally a 35-class dataset of spoken English words. However, this paper was part of a line of work starting with Kidger et al. [23] that has used a smaller 10-class subset of SC [18, 23, 35, 36]. In an effort to avoid dataset fragmentation in the literature, the authors have since moved to the original dataset. They are now calling this 10-class subset **SC10** to distinguish it from the full 35-class **SC** dataset. To cite S4 as a baseline for Speech Commands, please use Table 11 from [19] instead of Table 5 from this paper. In addition to using the full SC dataset, it also provides a number of much stronger baselines than the ones used in this work.

## WikiText-103

The original version of this paper used an S4 model with batch size 8, context size 1024 which achieved a validation perplexity of 20.88 and test perplexity of 21.28. It was later retrained with a batch size of 1 and context size 8192 which achieved a validation perplexity of 19.69 and test perplexity of 20.95, and a model checkpoint is available in the public repository. The rest of the model is essentially identical, so the results from the original table have been updated.
