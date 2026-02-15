# 4 Evaluating Subgraph Recovery Algorithms [p. 6-8]

[p. 6] The evaluation is framed with two questions:
- **Q1:** Does the method recover subgraphs corresponding to underlying task algorithms?
- **Q2:** Does the method avoid irrelevant components?

## 4.1 Grounded evaluation with prior circuits [p. 6-7]

[p. 6-7] Using canonical circuits from prior literature, the paper casts edge recovery as binary classification and reports ROC/AUC over threshold sweeps.

**Figure 3** (p. 7): edge-level ROC across IOI, Greater-Than, Docstring, tracr-xproportion, tracr-reverse.

Key qualitative findings (p. 7):
- Performance is sensitive to corruption distribution and metric choice.
- ACDC is competitive with gradient-based methods and best on several settings.
- Robustness is limited; some tasks/settings remain difficult.

## 4.2 Stand-alone properties on induction [p. 8]

[p. 8] Independent of "ground-truth" circuits, methods are compared on:
- KL divergence to original model output (lower better).
- Number of edges in recovered subgraph (lower preferred for sparsity).

**Figure 4** (p. 8): KL vs edge count for induction under corrupted and zero activations.
- ACDC tends to dominate the Pareto frontier for moderate+ edge budgets.

## Quantitative appendix tables (AUC)

[p. 21] **Table 2 (Random/Corrupted Ablation):**
- KL metric ACDC edge AUC: Docstring 0.982, Greater-Than 0.853, IOI 0.869.
- ACDC beats HISP/SP on these three edge-level KL tasks.

[p. 21] **Table 3 (Zero Ablation):**
- ACDC underperforms for some language tasks (e.g., IOI KL edge AUC 0.539),
- but achieves perfect tracr edge AUC under Loss (1.000 for both tracr tasks).

## Main caveats stated by authors

[p. 7-8] The paper highlights two major limitations:
1. Methods that optimize one scalar metric can miss "negative" components (harmful heads).
2. Human-labeled "ground-truth" circuits are themselves incomplete/noisy, limiting interpretability of ROC-based conclusions.
