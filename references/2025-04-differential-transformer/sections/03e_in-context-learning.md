# 3.5 In-Context Learning [p. 7]

The authors evaluate in-context learning from two perspectives, including many-shot classification and robustness of in-context learning [p. 7]. In-context learning is a fundamental capability of language models, which indicates how well a model can utilize the context [p. 7].

## Many-Shot In-Context Learning [p. 7]

As presented in Figure 6, the authors compare the accuracy of many-shot classification between Transformer and their architecture [p. 7]. They evaluate the 3B-size language models that support 64K input length (Section 3.3) [p. 7]. They follow the evaluation protocol of Bertsch et al. (2024) and use constrained decoding (Ratner et al., 2023) [p. 7]. They incrementally increase the number of demonstration samples from 1-shot to the maximal length [p. 7]. Specifically, the TREC (Hovy et al., 2001) dataset has 6 classes, TREC-fine (Hovy et al., 2001) has 50 classes, Banking-77 (Casanueva et al., 2020) has 77 classes, and Clinic-150 (Larson et al., 2019) has 150 classes [p. 7]. The results show that DIFF Transformer consistently outperforms Transformer across datasets and varying numbers of demonstration samples [p. 7]. Moreover, the improvement in average accuracy is substantial, ranging from 5.2% to 21.6% [p. 7].

**Figure 6** (p. 7): "Many-shot in-context learning accuracy on four datasets. Demonstration examples increase from 1-shot until the total length reaches 64K tokens. The dashed lines represent the average accuracy after the performance becomes stable."

Description: Four line plots comparing Transformer and Diff Transformer performance
- **(a) TREC with 6 classes:**
  - X-axis: # Samples from 0 to 3000
  - Y-axis: Accuracy (%) from 50 to 90
  - Two curves: Diff (Ours) (orange, dotted line) and Transformer (black, solid line)
  - Annotation: "+18.0" showing improvement
  - Diff shows consistently higher accuracy (~85-90%) while Transformer fluctuates (60-75%)
- **(b) TREC-fine with 50 classes:**
  - X-axis: # Samples from 0 to 3000
  - Y-axis: Accuracy (%) from 40 to 80
  - Annotation: "+21.6" showing improvement
  - Similar pattern with Diff maintaining ~80% while Transformer at ~60%
- **(c) Banking-77 with 77 classes:**
  - X-axis: # Samples from 0 to 2500
  - Y-axis: Accuracy (%) from 50 to 80
  - Annotation: "+10.4"
  - Diff reaches ~75-80% accuracy while Transformer stays around 60-70%
- **(d) Clinic-150 with 150 classes:**
  - X-axis: # Samples from 0 to 3000
  - Y-axis: Accuracy (%) from 55 to 80
  - Annotation: "+5.2"
  - Diff achieves ~75-80% while Transformer fluctuates around 70-75%
- Supports claim: DIFF Transformer consistently outperforms Transformer with improvements ranging from 5.2% to 21.6% [p. 7]

## Robustness of In-Context Learning [p. 8]

Figure 7 compares the robustness of in-context learning between Transformer and DIFF Transformer [p. 8]. Given the same demonstration examples, the authors analyze the performance variance with order permutations [p. 8]. Lower variance indicates greater robustness and less risk of catastrophic performance degradation [p. 8]. The evaluation protocol is the same as above [p. 8]. Figure 7 presents the analysis on the TREC dataset [p. 8]. More results are also provided in Appendix F [p. 8]. They evaluate two prompt formats, i.e., examples are randomly arranged (Figure 7a), and alternately arranged by class (Figure 7b) [p. 8]. In both settings, DIFF Transformer shows much smaller performance variance compared to Transformer [p. 8]. The results indicate that their approach is more robust for in-context learning [p. 8]. In contrast, Transformer tends to be distracted by order permutations (Lu et al., 2022), resulting in a huge margin between the best and worst results [p. 8].

**Figure 7** (p. 8): "Robustness evaluation of in-context learning on the TREC dataset. Accuracy is evaluated with order permutations of demonstration examples by sweeping random seeds. The dash lines represent the margin between the best and worst results. Smaller margin indicates superior robustness. Two prompt formats are examined."

Description: Two line plots showing robustness analysis
- **(a) Examples are randomly arranged:**
  - X-axis: Random Seed from 0 to 9
  - Y-axis: Accuracy (%) from 65 to 90
  - Two curves: Diff (Ours) (orange) and Transformer (black)
  - Diff shows stable performance around 90% with small variance
  - Transformer fluctuates significantly between ~65% and ~82%
  - Annotation: "19.0" showing margin for Transformer
  - Annotation: "4.0" showing margin for Diff
  - Dashed horizontal lines show best/worst bounds for each model
- **(b) Examples are arranged alternately by class:**
  - X-axis: Random Seed from 0 to 30
  - Y-axis: Accuracy (%) from 30 to 100
  - Diff maintains stable ~90-95% accuracy
  - Transformer shows extreme variance, dropping as low as ~30%
  - Annotation: "56.7" showing large margin for Transformer
  - Annotation: "13.4" showing margin for Diff
- Supports claim: DIFF Transformer demonstrates superior robustness with much smaller performance variance compared to Transformer across different orderings [p. 8]
