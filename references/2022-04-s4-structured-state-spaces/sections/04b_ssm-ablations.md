# 4.4 SSM Ablations: the Importance of HiPPO [p. 11]

[p. 11]

A critical motivation of S4 was the use of the HiPPO matrices to initialize an SSM. The authors consider several simplifications of S4 to ablate the importance of each of these components, including: (i) how important is the HiPPO initialization? (ii) how important is training the SSM on top of HiPPO? (iii) are the benefits of S4 captured by the NPLR parameterization without HiPPO?

As a simple testbed, all experiments in this section were performed on the sequential CIFAR-10 task, which the authors found transferred well to other settings. Models were constrained to at most 100K trainable parameters and trained with a simple plateau learning rate scheduler and no regularization.

## Unconstrained SSMs

[p. 11]

Generic SSMs with various initializations are investigated. The authors consider a random Gaussian initialization (with variance scaled down until it did not NaN), and the HiPPO initialization. They also consider a random diagonal Gaussian matrix as a potential structured method; parameterizing **A** as a diagonal matrix would allow substantial speedups without going through the complexity of S4's NPLR parameterization. Both freezing and training the **A** matrix are considered.

Fig. 3 shows both training and validation curves, from which several observations are made. First, training the SSM improved all methods, particularly the randomly initialized ones. For all methods, training the SSM led to improvements in both training and validation curves.

Second, a large generalization gap exists between the initializations. In particular, when **A** is trained, all initializations are able to reach perfect training accuracy. However, their validation accuracies are separated by over 15%.

## NPLR SSMs

[p. 11]

The previous experiment validates the importance of HiPPO in SSMs. This was the main motivation of the NPLR algorithm in S4, which utilizes structure of the HiPPO matrix (2) to make SSMs computationally feasible. Fig. 4a shows that random NPLR matrices still do not perform well, which validates that S4's effectiveness primarily comes from the HiPPO initialization, not the NPLR parameterization.

Finally, Fig. 4b considers the main ablations considered in this section (with trainable SSMs) and adds minor regularization. With 0.1 Dropout, the same trends still hold, and the HiPPO initialization -- in other words, the full S4 method -- achieves 84.27% test accuracy with just 100K parameters.

## Table 9: Univariate Long Sequence Time-Series Forecasting

[p. 11]

**Table 9** (p. 11): "Univariate long sequence time-series forecasting results. Full results in Appendix D.3.5."

|         | S4 MSE | S4 MAE | Informer MSE | Informer MAE | LogTrans MSE | LogTrans MAE | Reformer MSE | Reformer MAE | LSTMa MSE | LSTMa MAE | DeepAR MSE | DeepAR MAE | ARIMA MSE | ARIMA MAE | Prophet MSE | Prophet MAE |
|---------|--------|--------|--------------|--------------|--------------|--------------|--------------|--------------|-----------|-----------|------------|------------|-----------|-----------|-------------|-------------|
| ETTh1   | **0.116** | **0.271** | 0.269 | 0.435 | 0.273 | 0.463 | 2.112 | 1.436 | 0.683 | 0.768 | 0.658 | 0.707 | 0.659 | 0.766 | 2.735 | 3.253 |
| ETTh2   | **0.187** | **0.358** | 0.277 | 0.431 | 0.303 | 0.493 | 2.030 | 1.721 | 0.640 | 0.681 | 0.429 | 0.580 | 2.878 | 1.044 | 3.355 | 4.664 |
| ETTm1   | **0.292** | **0.466** | 0.512 | 0.644 | 0.598 | 0.702 | 1.793 | 1.528 | 1.064 | 0.873 | 2.437 | 1.352 | 0.639 | 0.697 | 2.747 | 1.174 |
| Weather | **0.245** | **0.375** | 0.359 | 0.466 | 0.388 | 0.499 | 2.087 | 1.534 | 0.866 | 0.809 | 0.499 | 0.596 | 1.062 | 0.943 | 3.859 | 1.144 |
| ECL     | **0.432** | **0.497** | 0.582 | 0.608 | 0.624 | 0.645 | 7.019 | 5.105 | 1.545 | 1.006 | 0.657 | 0.683 | 1.370 | 0.982 | 6.901 | 4.264 |

S4 outperforms the Informer and other baselines on 40/50 settings across 5 forecasting tasks. The tasks considered (generative modeling, image classification, time-series forecasting) are considered as LRD tasks in the literature, and serve as additional validation that S4 handles LRDs efficiently.

## Figure 3

**Figure 3** (p. 12): "CIFAR-10 classification with unconstrained, real-valued SSMs with various initializations. (*Left*) Train accuracy. (*Right*) Validation accuracy."

The figure contains two panels, both showing curves over 200 epochs on sequential CIFAR-10:
- **Left panel (Train Accuracy):** Y-axis is train accuracy (0.2 to 1.0), x-axis is epoch (0 to 200). Five methods are compared: HiPPO (red dashed), Diagonal (green dashed), Random (blue solid), Trained A (gray solid), Frozen A (dark solid). When **A** is trained, all initializations eventually reach near-perfect (~1.0) training accuracy. When **A** is frozen, training accuracy is lower, especially for Random and Frozen A.
- **Right panel (Validation Accuracy):** Y-axis is validation accuracy (0.2 to 0.7), x-axis is epoch (0 to 200). Despite similar training accuracies when **A** is trained, a large generalization gap appears: HiPPO achieves the highest validation accuracy (~0.68-0.70), Diagonal is next (~0.60-0.62), while Random, Trained A, and Frozen A cluster lower (~0.50-0.55). Validation accuracies are separated by over 15%.

Supports the claim that training the SSM improves all methods, but the HiPPO initialization provides a crucial generalization advantage.

## Figure 4

**Figure 4** (p. 12): "CIFAR-10 validation accuracy of SSMs with different initializations and parameterizations. (*Left*) NPLR parameterization with random versus HiPPO initialization. (*Right*) All methods considered in this section, including minor Dropout regularization. S4 achieves SotA accuracy on sequential CIFAR-10 with just 100K parameters."

The figure contains two panels:
- **Left panel (4a, "NPLR SSM"):** Y-axis is validation accuracy (0.45 to 0.80), x-axis is epoch (0 to 200). Compares HiPPO (red dashed) vs. Random (blue solid) under NPLR parameterization, with Trained A (gray) and Frozen A (dark) variants. HiPPO with NPLR reaches ~0.78-0.80 validation accuracy, while random NPLR matrices perform substantially worse (~0.50-0.55). This validates that S4's effectiveness comes primarily from the HiPPO initialization, not the NPLR parameterization itself.
- **Right panel (4b, "Trainable SSMs (+ Dropout)"):** Y-axis is validation accuracy (0.2 to 0.8), x-axis is epoch (0 to 200). Compares all methods with 0.1 Dropout: HiPPO (red dashed), Random NPLR (green dashed), Random Diagonal (blue solid), Random Dense (gray solid). HiPPO achieves the highest accuracy (~0.84), and the same trends hold. The full S4 method achieves 84.27% test accuracy with just 100K parameters.
