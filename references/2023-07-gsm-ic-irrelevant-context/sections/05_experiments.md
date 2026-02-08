# 5. Experiments [p. 5–9]

[p. 5] 4,000 examples are uniformly sampled from the GSM-IC dataset (denoted by GSM-IC-4K) for evaluation and analysis purposes throughout this paper. The sampled GSM-IC-4K covers all 100 base problems. Unless otherwise specified, `code-davinci-002` is the main model used, and `text-davinci-003` (a model trained with RLHF; Ouyang et al., 2022) is also evaluated to better follow instructions. For experiments without self-consistency decoding, greedy decoding is used (i.e., temperature tau = 0); for self-consistency experiments that require multiple samples for a problem, 20 responses are sampled with temperature tau = 0.7 following Wang et al. (2022c). [p. 5]

## 5.1 Main Results on GSM-IC

[p. 5-6] The performance of different prompting techniques on GSM-IC-4K is compared (Table 3), in terms of both micro and macro accuracies, as well as their corresponding normalized accuracies. [p. 5-6]

**Table 3** (p. 6): Micro and macro accuracies (x100) on the GSM-IC-4K dataset. SC denotes self-consistency. *Norm* is the overall accuracy normalized by the fraction of solved base problems (Table 2), which is a measure for robustness w.r.t. irrelevant information. For `text-davinci-003`, the base problem accuracy with CoT is 80.0, and the base problem accuracy with LtM is 81.0. The best numbers in each column for each section (i.e., whether using `code-davinci-002` or `text-davinci-003`, whether using exemplar with irrelevant context or not, and whether using self-consistency or not) are in **boldface**.

*Prompting Exemplar w/o Irrelevant Context, `code-davinci-002`:*

| Method | Micro Accuracy ||| Macro Accuracy |||
| | 2 Steps | >2 Steps | Overall | *Norm* | 2 Steps | >2 Steps | Overall | *Norm* |
|---|---|---|---|---|---|---|---|---|
| CoT | 73.5 | 70.8 | 72.4 | 76.2 | 8.3 | 2.5 | 6.0 | *6.3* |
| CoT + INST. | 79.0 | 76.0 | 77.8 | *81.8* | 20.0 | 7.0 | 15.0 | *15.8* |
| 0-CoT | 29.0 | 29.1 | 29.0 | 65.9 | 1.7 | 0.0 | 1.0 | *2.3* |
| 0-CoT + INST. | 31.6 | 28.8 | 30.5 | 69.3 | 1.7 | 0.0 | 1.0 | *2.3* |
| LtM | 74.9 | **81.5** | 77.5 | 82.4 | 16.7 | 20.0 | 18.0 | *19.1* |
| LtM + INST. | **80.1** | 81.3 | **80.6** | **85.7** | **18.3** | **35.0** | **25.0** | ***26.6*** |
| PROGRAM | 59.1 | 47.4 | 54.4 | 65.5 | 6.7 | 2.5 | 5.0 | *6.0* |
| PROGRAM + INST. | 60.6 | 50.9 | 56.7 | 68.3 | 6.7 | 5.0 | 6.0 | *7.2* |
| CoT + SC | 87.6 | 90.1 | 88.1 | *91.8* | 29.0 | 28.3 | 30.0 | *31.3* |
| 0-CoT + SC | 61.6 | 68.4 | 64.3 | 84.6 | 0.0 | 2.5 | 1.0 | *1.3* |
| LtM + SC | **92.4** | **94.8** | **93.4** | **94.3** | **51.6** | **35.0** | **45.0** | ***45.5*** |
| PROGRAM + SC | 73.5 | 76.1 | 74.6 | 82.0 | 16.7 | 7.5 | 13.0 | *14.3* |

*Prompting Exemplar w/o Irrelevant Context, `text-davinci-003`:*

| Method | Micro Accuracy ||| Macro Accuracy |||
| | 2 Steps | >2 Steps | Overall | *Norm* | 2 Steps | >2 Steps | Overall | *Norm* |
|---|---|---|---|---|---|---|---|---|
| CoT | 69.3 | 66.9 | 68.4 | *85.4* | 10.0 | 7.5 | 9.0 | *11.3* |
| CoT + INST. | 72.0 | 70.3 | 71.3 | *89.1* | 11.7 | **12.5** | **12.0** | ***15.0*** |
| LtM | 78.0 | **73.6** | 76.3 | 94.2 | 5.0 | 0.0 | 5.0 | *6.2* |
| LtM + INST. | **80.5** | 70.9 | **76.7** | **94.7** | 5.0 | 0.0 | 5.0 | *6.2* |

*Prompting Exemplar w/ Irrelevant Context, `code-davinci-002`:*

| Method | Micro Accuracy ||| Macro Accuracy |||
| | 2 Steps | >2 Steps | Overall | *Norm* | 2 Steps | >2 Steps | Overall | *Norm* |
|---|---|---|---|---|---|---|---|---|
| CoT | 79.8 | 72.4 | 76.8 | 80.8 | 16.7 | 10.0 | 14.0 | *14.7* |
| CoT + INST. | 80.5 | 74.4 | 78.1 | 82.2 | 20.0 | 12.0 | 17.0 | *17.9* |
| LtM | 78.1 | 84.6 | 80.7 | 85.9 | **23.3** | **35.0** | **28.0** | ***29.8*** |
| LtM + INST. | **81.0** | **85.4** | **82.8** | **88.1** | **23.3** | **35.0** | **28.0** | ***29.8*** |
| PROGRAM | 67.0 | 55.0 | 62.2 | 74.9 | 11.7 | 5.0 | 9.0 | *10.8* |
| PROGRAM + INST. | 68.8 | 54.8 | 63.2 | 76.1 | 15.0 | 7.5 | 12.0 | *14.5* |

[p. 6] Overall, significant performance drop is observed for both models with all prompting techniques. The drop on macro accuracy is especially large, showing that fewer than 30% of the base problems are consistently solved after adding distractors. Comparing the two models, `text-davinci-003` achieves better normalized micro accuracy than `code-davinci-002`, though its macro accuracy is mostly worse. In Figure 3, a GSM-IC-4K example is presented where a single irrelevant sentence causes different types of errors in investigated prompting techniques. One common error type is wrongly using the number in the irrelevant sentence, as shown in the LtM prediction and other examples in Appendix B. Even if the model does not directly use the irrelevant number for numerical calculation, the presence of the irrelevant sentence in the reasoning steps alone can still cause a wrong prediction, as shown in the CoT prediction. [p. 6]

**LtM is generally the most robust technique to irrelevant context.** In terms of micro accuracy, LtM outperforms all other prompting methods across models. Using `code-davinci-002`, LtM achieves about double the macro accuracy of CoT. Interestingly, with `text-davinci-003`, despite that LtM outperforms CoT on the micro accuracy, its macro accuracy is lower. Specifically, `text-davinci-003` is highly susceptible to irrelevant context with role overlap; e.g., such irrelevant sentences decrease the macro accuracy to 0 on problems with more than 2 reasoning steps. See Table 4 for the breakdown performance on different types of irrelevant context. [p. 6]

**Selecting exemplars with distractors mitigates the distractibility.** For few-shot prompts, using exemplars with distractors (i.e., including problems with irrelevant context) consistently outperforms using the original exemplars without distractors across prompting techniques. While prior work has shown that training and fine-tuning with different types of problems improves model robustness (Li et al., 2022), these results show that prompting with exemplars that demonstrate how to ignore irrelevant context also results in significant robustness improvement. In Table 5, they further show that using exemplars with distractors does not cause a performance drop on the original GSM8K dataset. [p. 6]

---
[p. 7–9 continued]

**Figure 3** (p. 7): "Example problem and corresponding outputs by different prompting techniques (best viewed in color). The CoT answer to the original problem is highlighted in green. The added irrelevant sentence is in *italic and highlighted in red*, which causes different errors (highlighted in yellow) for all prompting techniques. More examples of model predictions can be found in Appendix B."

The figure shows a modified GSM-IC-4K problem about Maria buying French soap. The original problem asks how much Maria spends on soap for the year (correct answer: $48.00). The irrelevant sentence added is: *"Every 10 months, Maria's neighbor buys a new shampoo and moisturizer for Maria's neighbor."* The figure shows:
- **Correct CoT Output to the Original Problem:** correctly computes $8.00 x 12 / 2 = $48.00.
- **CoT on Modified Problem:** incorrectly incorporates irrelevant sentence, computing $8.00 x 12 = $96.00 (wrong answer: $96.00).
- **LtM on Modified Problem:** incorrectly uses the number from the irrelevant sentence ($8.00 * 10 = $80.00 every 10 months, then $80.00 * 12 = $960.00). Wrong answer: $960.00.
- **PROGRAM on Modified Problem:** code outputs 192.0 (wrong), computing Soap_per_year = 2 * 12 and Soap_total = Soap_price * Soap_per_year.

This figure supports the claim that different prompting techniques are susceptible to different types of errors caused by irrelevant context. [p. 7]

[p. 7] Indicating that such a prompt design can be beneficial in achieving better accuracy and robustness simultaneously. [p. 7]

**Self-consistency significantly reduces the distractibility.** Taking the majority vote from 20 samples,^6 SC improves the overall micro accuracy by more than 11 percentage points. This means that in addition to improving model performance on clean arithmetic reasoning tasks (Wang et al., 2022c), SC also substantially reduces the distractibility of large language models to irrelevant context. The gain on micro accuracy is notably large on 0-CoT (35.5 percentage points). Furthermore, the correct answer for 99.7% of the problems is in the 20 sampled answers for both CoT and LtM. Even for 0-CoT, the recall of correct solutions within 20 samples is 96.5%. Despite these improvements, the best macro accuracy among all prompting techniques is only 45%, suggesting that for more than half of the base problems, SC fails to prevent the model from being distracted by different variants of irrelevant information. These results imply that a better algorithm may be developed to further reduce the distractibility based on a few sampled solutions. [p. 7]

^6 If there is a tie, a random top-tier result is taken for evaluation, following Wang et al. (2022c) and Shi et al. (2022a). [p. 7]

**Figure 4** (p. 7): "Micro accuracies on GSM-IC-4K with respect to the number of required reasoning steps."

Bar chart showing micro accuracy (x100) on y-axis vs. number of steps (2, 3, 4, >=5) on x-axis for CoT, LtM, and PROGRAM. Readable values:
- 2 steps: CoT 73.5, LtM 74.9, PROGRAM 59.1
- 3 steps: CoT 78.8, LtM 86.5, PROGRAM 57.2 [unclear: exact values hard to read from bar chart]
- 4 steps: CoT 66.4, LtM 77.3, PROGRAM 46.3
- >=5 steps: CoT 66.3 [unclear: approximate], LtM 80.3, PROGRAM 36.7

The figure shows that CoT and PROGRAM accuracy drops significantly on problems requiring 4 or more reasoning steps, while LtM performance is fairly consistent across difficulty levels. [p. 7]

## 5.2 Break-Down Analysis

### 5.2.1 Factors of the Irrelevant Context

[p. 7–8] The performance of CoT, LtM, and PROGRAM is analyzed with respect to the considered factors (Section 3.1) of the irrelevant sentences (Table 4). For both models, (1) in-topic sentences with (2) role name overlap and (3) in-range numbers are generally more challenging, which is exemplified by Figure 3. For LtM, the latter two factors do not have a large effect on the micro accuracy. The difference is more significant for the macro accuracy and, as an anomaly, using distractors with in-range numbers turns out to be less challenging than out-of-range numbers when using irrelevant context in the exemplar. Again, with `code-davinci-002`, LtM outperforms CoT and PROGRAM on all investigated sub-categories. On the other hand, using `text-davinci-003`, LtM outperforms CoT in terms of the micro accuracy, but the macro accuracy is much lower on all sub-categories. [p. 7–8]

**Table 4** (p. 8): Breakdown accuracies (x100) w.r.t. the factors of the added irrelevant sentence. Lower accuracy indicates the model is more fragile to the corresponding type of irrelevant contexts. Note that the macro average accuracies are higher than the corresponding ones reported in Table 3 as only a subset of created problems (those corresponding to the appropriate factor) are included here to compute the metric. The best result in each column is in **boldface**.

| Method | Micro Accuracy |||||| Macro Accuracy ||||||
| | Topic || Role Overlap || Num. Range || Topic || Role Overlap || Num. Range ||
| | In | Off | Yes | No | In | Out | In | Off | Yes | No | In | Out |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *Prompting Exemplar w/o Irrelevant Context (`code-davinci-002`)* |||||||||||||
| CoT | 63.1 | 80.7 | 68.3 | 76.6 | 70.2 | 74.6 | 10.2 | 33.0 | 10.3 | 22.2 | 11.0 | 19.0 |
| LtM | **70.8** | **83.4** | **77.0** | **77.2** | **77.2** | **77.8** | **23.5** | **45.0** | **25.8** | **35.4** | **27.0** | **29.0** |
| PROGRAM | 44.1 | 63.5 | 50.7 | 58.4 | 54.3 | 54.5 | 4.1 | 24.0 | 9.3 | 16.2 | 7.0 | 11.0 |
| *Prompting Exemplar w/o Irrelevant Context (`text-davinci-003`)* |||||||||||||
| CoT | 63.3 | 72.9 | 68.7 | 68.1 | 67.2 | 69.6 | **16.3** | **36.0** | **17.5** | **20.2** | **19.0** | **22.0** |
| LtM | **75.4** | **76.9** | **75.6** | **76.8** | **75.3** | **77.2** | 6.1 | 7.0 | 6.2 | 9.1 | 6.0 | 6.0 |
| *Prompting Exemplar w/ Irrelevant Context (`code-davinci-002`)* |||||||||||||
| CoT | 70.2 | 82.7 | 73.6 | 80.2 | 76.1 | 77.7 | *18.4* | 43.0 | 21.6 | 32.3 | 22.0 | 26.0 |
| LtM | **73.0** | **87.5** | **81.4** | **80.2** | **80.0** | **81.4** | **28.6** | **58.0** | **37.1** | 42.4 | **41.0** | **35.0** |
| PROGRAM | 52.9 | 70.5 | 60.2 | 64.5 | 61.5 | 62.8 | 10.2 | 37.0 | 14.4 | 23.2 | 15.0 | 17.0 |

### 5.2.2 Break-Down Accuracies w.r.t. # Steps

[p. 7] The break-down accuracies for problems with respect to the reasoning steps are analyzed (Figure 4). While there is a significant drop for CoT and PROGRAM on problems that require four or more steps in the reasoning process, the performance of LtM is fairly consistent across difficulty. In addition to the advantage of LtM on clean problems for complicated reasoning (Zhou et al., 2022), these results show that LtM is also less sensitive to irrelevant context for complicated problems that require more steps to solve. [p. 7]

## 5.3 Instructed Prompting Improves Robustness to Irrelevant Context

[p. 7–8] Using exemplars with distractors improves robustness to irrelevant context. The performance of instructed prompting is also compared to prompts without instructions in Table 3. Adding instructions to CoT, LtM, and PROGRAM consistently improves their performance. Surprisingly, instructed prompting with original exemplars reaches comparable or even better performance than uninstructed prompting that uses exemplars with distractors for both CoT and LtM. Note that adding the instruction "Solve grade school math problems." alone does not significantly improve the performance, and it is the instruction "Feel free to ignore irrelevant information given in the questions." that makes the difference. Similar to the instruction "Let's think step by step." employed by 0-CoT, this shows that language models are -- to some extent -- able to follow natural language instructions in a way that dramatically changes their problem solving behavior, suggesting that such instructions may be useful for guiding the behavior of language models on more tasks. [p. 7–8]

[p. 8] On the original GSM8K development set (Cobbe et al., 2021; Zhou et al., 2022), no drop in accuracy is observed when using exemplars with irrelevant information, adding natural language instructions, or both (Table 5). The same holds for SVAMP (Patel et al., 2021), an arithmetic reasoning benchmark constructed by applying different types of variations to math problems from existing clean datasets, e.g., changing sentence structures, asking different questions with the same information, etc. This is impressive because the results on GSM-IC show that prompt exemplars with irrelevant information and instructed prompting both improve robustness. For the PROGRAM prompt, using exemplars with distractors even increases performance on SVAMP. [p. 8]

**Table 5** (p. 8): Accuracies (x100) on the GSM8K development set and the SVAMP test set. IRRCTX denotes irrelevant contexts, and +INST. denotes instructed prompting. The baseline results (i.e., those using the simplest exemplars without irrelevant context and without instructions) are underlined.

| Method | Exemplar w/ IRRCTX? | Accuracy ||
| | | GSM8K Dev. | SVAMP Test |
|---|---|---|---|
| CoT | checkmark | 59.3 | 79.1 |
| | X | 60.3 | 77.6 |
| CoT + INST. | checkmark | 59.3 | 79.1 |
| | X | 58.8 | 78.7 |
| LtM | checkmark | 61.9 | 76.9 |
| | X | 59.8 | 76.6 |
| LtM + INST. | checkmark | 60.9 | 76.2 |
| | X | 60.3 | 76.3 |
| PROGRAM | checkmark | 58.6 | 80.0 |
| | X | 59.8 | 77.3 |
| PROGRAM + INST. | checkmark | 59.2 | 77.9 |
| | X | 61.1 | 77.8 |

Note: Baseline results (without irrelevant context exemplars, without instructions) are the X rows for each base method (CoT, LtM, PROGRAM). The underlined baselines are: CoT X = 60.3/77.6, LtM X = 59.8/76.6, PROGRAM X = 59.8/77.3. [p. 8]

## 5.4 Complicated Prompts May Hurt the Robustness to Irrelevant Context

[p. 8–9] The 1-exemplar CoT prompt (Figure 2) is compared to a 4-exemplar prompt (Appendix D of Zhou et al., 2022), which is reported as the best-performing CoT prompt on GSM8K, on GSM-IC (Table 6). Note that the 1-exemplar CoT prompt only includes a problem with a 2-step solution, while the 4-exemplar prompt includes problems that require more reasoning steps. While the 4-exemplar prompt leads to better performance on the original GSM8K development set, the 4-exemplar prompt is surprisingly more susceptible to the distraction provided by the irrelevant context. In particular, the 4-exemplar prompt is consistently worse than the 1-exemplar prompt on problems with more than 2 intermediate steps. Even for 2-step prompts, the accuracy improvement from adding more exemplars is almost negligible when using instructions (79.0 vs 79.2). Overall, this finding indicates that adding more exemplars can make the prompt less robust as it leads to some overfitting. [p. 8–9]

**Table 6** (p. 9): Micro accuracies (x100) on the GSM8K development set and GSM-IC-4K. # Prompting Exemplars denotes the number of exemplars used in the prompt. The best number in each column is in **boldface**.

| Method | #Prompting Exemplars | GSM8K Dev. | GSM-IC-4K 2 Steps | GSM-IC-4K > 2 Steps |
|---|---|---|---|---|
| CoT | 1 | 60.3 | 73.6 | 70.8 |
| | 4 | **66.3** | **78.0** | 69.4 |
| CoT + INST. | 1 | 58.8 | **79.0** | **76.0** |
| | 4 | **66.5** | **79.2** | 70.6 |

## 5.5 Extension to DROP

[p. 9] In addition to GSM-IC, the evaluation is extended to the DROP dataset (Dua et al., 2019), where the task is to answer a question according to a long passage that naturally contains irrelevant context. An example about football games is shown in Table 8. [p. 9]

The CoT and LtM prompts in Zhou et al. (2022) are used as the baselines, and the prompt variants are evaluated with the instruction *"Solve following questions. Feel free to ignore irrelevant information given in the questions."* added before the exemplars. Note that by adding a problem reduction step in the exemplar solution, the least-to-most prompt implicitly leads the model to come up with relevant subproblems to solve the given problem. Again, the instruction consistently improves the performance of both CoT and LtM prompting (Table 7). [p. 9]

**Table 7** (p. 9): Accuracies (x100) on the football split of DROP (Dua et al., 2019) benchmark.

| Method | `code-davinci-002` | `text-davinci-003` |
|---|---|---|
| CoT | 67.4 | 68.2 |
| CoT + INST. | 68.9 | 69.9 |
| LtM | 73.4 | 70.2 |
| LtM + INST. | **74.4** | **72.8** |

**Table 8** (p. 9): A DROP example about football games.

The table shows a complete LtM solution example:
- **Paragraph:** The Seahawks played the San Francisco 49ers. In the first quarter, the Hawks RB Julius Jones got a 27-yard TD run, along with DT Craig Terrill returning a fumble 9 yards for a touchdown. In the third quarter, the 49ers almost rallied as RB H. J. Torres made a 12-yard TD pass to Lucas Nelly, along with Mare kicking a 32-yard field goal. In the final quarter, Julius Jones got another 11-yard TD.
- **Question:** How many yards do the shortest touchdown run and the longest touchdown pass combine for?
- **LtM solution:** The model decomposes into sub-questions: "How many yards was the shortest touchdown run?" and "How many yards was the longest touchdown pass?" It identifies all touchdown runs as 27-yard, 9-yard, 11-yard (shortest = 9 yards) and all touchdown passes as 12-yard (longest = 12 yards). Final answer: 9 + 12 = 21. [p. 9]
