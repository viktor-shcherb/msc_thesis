# 4.5. Analysis on Expert Specialization [p. 13–14]

[p. 13] An empirical analysis on the expert specialization of DeepSeekMoE 2B is conducted. DeepSeekMoE 2B in this section refers to the model reported in Table 1, i.e., comprising 2.0B total parameters, with 1 shared expert and 7 out of 63 routed experts being activated.

## DeepSeekMoE Exhibits Lower Redundancy Among Routed Experts

[p. 13] To assess the redundancy among routed experts, varying ratios of top routed experts are disabled and the Pile loss is evaluated. Specifically, for each token, a certain ratio of experts with the highest routing probability is masked, and then top-K experts are selected from the remaining routed experts. For fairness, DeepSeekMoE is compared with GShard x1.5 since they have the same Pile loss when no experts are disabled.

[p. 13] As shown in Figure 4, compared with GShard x1.5, DeepSeekMoE is more sensitive to the disabling of top routed experts. This sensitivity suggests a lower level of parameter redundancy in DeepSeekMoE, since each routed expert is more irreplaceable. In contrast, GShard x1.5 exhibits greater redundancy among its expert parameters, so it can buffer the performance drop when top routed experts are disabled.

**Figure 4** (p. 13): "Pile loss with regard to different ratios of disabled top routed experts. Notably, DeepSeekMoE exhibits greater sensitivity to the ratio of disabled top routed experts, indicating lower redundancy among routed experts in DeepSeekMoE."

- X-axis: Ratio of Disabled Top Routed Experts (0, 1/16, 2/16, 3/16, 4/16)
- Y-axis: Pile Loss (range ~2 to 9)
- Two lines:
  - DeepSeekMoE (orange/yellow, circle markers): starts at ~1.8 (ratio 0), rises steeply to ~5 (ratio 1/16), ~7.5 (ratio 2/16), ~8.5 (ratio 3/16), ~9 (ratio 4/16)
  - GShard x1.5 (blue, x markers): starts at ~1.8 (ratio 0), rises more gradually to ~3 (ratio 1/16), ~5.5 (ratio 2/16), ~7 (ratio 3/16), ~7.5 (ratio 4/16)
- DeepSeekMoE's steeper curve demonstrates higher sensitivity to expert removal, confirming lower redundancy.

## Shared Experts Are Irreplaceable by Routed Experts

[p. 13] To investigate the role of the shared expert in DeepSeekMoE, it is disabled and one more routed expert is activated instead. The evaluation on Pile shows a significant increase in the Pile loss, rising from 1.808 to 2.414, even though the same computational cost is maintained. This result highlights the crucial function of the shared expert and indicates that the shared expert captures fundamental and essential knowledge not shared with routed experts, making it irreplaceable by routed ones.

## DeepSeekMoE Acquires Knowledge More Accurately

[p. 13–14] To validate the claim that higher flexibility in combining activated experts contributes to more accurate and targeted knowledge acquisition, the authors investigate whether DeepSeekMoE can acquire requisite knowledge with fewer activated experts. Specifically, the number of activated routed experts is varied from 3 to 7 and the resulting Pile loss is evaluated. As demonstrated in Figure 5, even with only 4 routed experts activated, DeepSeekMoE achieves a Pile loss comparable with GShard (which uses full top-2 activation).

**Figure 5** (p. 14): "Pile loss with regard to different numbers of activated routed experts in DeepSeekMoE. With only 4 routed experts activated, DeepSeekMoE achieves a Pile loss comparable with GShard."

- X-axis: Activated Routed Experts (3, 4, 5, 6, 7)
- Y-axis: Pile Loss (range ~1.82 to 1.96)
- DeepSeekMoE (orange/yellow curve, circle markers): decreasing Pile loss as more experts are activated, from ~1.96 (3 experts) to ~1.808 (7 experts)
- GShard (full top-2 activated) shown as a blue x marker and horizontal blue dashed line at approximately 1.867 Pile loss
- An annotation "same activated expert parameters" marks where DeepSeekMoE with ~6 activated routed experts matches GShard's activated expert parameter count
- With 4 routed experts, DeepSeekMoE already achieves a Pile loss below GShard's level (~1.867)

[p. 14] This observation supports the proposition that DeepSeekMoE can acquire requisite knowledge more accurately and efficiently.

[p. 14] Encouraged by these findings, to validate the expert specialization and accurate knowledge acquisition of DeepSeekMoE more rigorously, a new model is trained from scratch. This model comprises 1 shared expert and 63 routed experts, where only 3 routed experts are activated. The evaluation results shown in Figure 6 demonstrate that, even with the same total expert parameters and only half of the activated expert parameters, DeepSeekMoE still outperforms GShard. This highlights the ability of DeepSeekMoE to leverage expert parameters more efficiently, i.e., the proportion of effective parameters in the activated experts is much higher than that of GShard.

**Figure 6** (p. 14): "Comparison between GShard and DeepSeekMoE with half the activated experts (trained from scratch). With the same total expert parameters and only half of the activated expert parameters, DeepSeekMoE still outperforms GShard."

- X-axis: Metrics (HellaSwag, PIQA, ARC-easy, ARC-challenge, TriviaQA, NaturalQuestions)
- Y-axis: Performance (range 0 to 80)
- Two configurations compared (bar chart):
  1. 0 shared expert + 2 out of 16 routed experts (GShard) — blue bars
  2. 1 shared expert + 3 out of 63 routed experts (DeepSeekMoE with half the activated experts) — orange bars
- Approximate values from the chart:
  - HellaSwag: GShard ~50, DeepSeekMoE ~52
  - PIQA: GShard ~70, DeepSeekMoE ~70
  - ARC-easy: GShard ~44, DeepSeekMoE ~47
  - ARC-challenge: GShard ~32, DeepSeekMoE ~34
  - TriviaQA: GShard ~10, DeepSeekMoE ~15
  - NaturalQuestions: GShard ~3, DeepSeekMoE ~4
- DeepSeekMoE outperforms GShard on all six benchmarks despite using only half the activated expert parameters.
