# 3.7 SuperGLUE [p. 18-20]

[p. 18] In order to better aggregate results on NLP tasks and compare to popular models such as BERT and RoBERTa in a more systematic way, GPT-3 is evaluated on a standardized collection of datasets, the SuperGLUE benchmark [WPN+19] [WPN+19] [CLC+19] [DMST19] [RBG11] [KCR+18] [ZLL+18] [DGM06] [BHDD+06] [GMDD07] [BDD+09] [PCC18] [PHR+18]. GPT-3's test-set performance on the SuperGLUE dataset is shown in Table 3.8. In the few-shot setting, 32 examples are used for all tasks, sampled randomly from the training set. For all tasks except WSC and MultiRC, a new sample of examples is used in the context for each problem. For WSC and MultiRC, the same set of randomly drawn examples from the training set is used as context for all of the problems evaluated.

## Task-by-task analysis

[p. 20] A wide range in GPT-3's performance across tasks is observed.

**COPA and ReCoRD:** On COPA and ReCoRD GPT-3 achieves near-SOTA performance in the one-shot and few-shot settings, with COPA falling only a couple points short and achieving second place on the leaderboard, where first place is held by a fine-tuned 11 billion parameter model (T5).

**WSC:** On WSC, performance is still relatively strong, achieving 80.1% in the few-shot setting (note that GPT-3 achieves 88.6% on the original Winograd dataset as described in Section 3.4).

**BoolQ, MultiRC, and RTE:** On BoolQ, MultiRC, and RTE, performance is reasonable, roughly matching that of a fine-tuned BERT-Large.

**CB:** On CB, signs of life are seen at 75.6% in the few-shot setting.

**WiC:** WiC is a notable weak spot with few-shot performance at 49.4% (at random chance). A number of different phrasings and formulations for WiC (which involves determining if a word is being used with the same meaning in two sentences) were tried, none of which was able to achieve strong performance. This hints at a phenomenon that will become clearer in the next section (which discusses the ANLI benchmark) -- GPT-3 appears to be weak in the few-shot or one-shot setting at some tasks that involve comparing two sentences or snippets, for example whether a word is used the same way in two sentences (WiC), whether one sentence is a paraphrase of another, or whether one sentence implies another. This could also explain the comparatively low scores for RTE and CB, which also follow this format.

## Overall assessment

[p. 20] Despite these weaknesses, GPT-3 still outperforms a fine-tuned BERT-large on four of eight tasks and on two tasks GPT-3 is close to the state-of-the-art held by a fine-tuned 11 billion parameter model.

[p. 20] The few-shot SuperGLUE score steadily improves with both model size and with number of examples in the context showing increasing benefits from in-context learning (Figure 3.8). K is scaled up to 32 examples per task, after which point additional examples will not reliably fit into the context. When sweeping over values of K, GPT-3 requires less than eight total examples per task to outperform a fine-tuned BERT-Large on overall SuperGLUE score.

### Table 3.8: Performance of GPT-3 on SuperGLUE compared to fine-tuned baselines and SOTA. All results are reported on the test set. GPT-3 few-shot is given a total of 32 examples within the context of each task and performs no gradient updates. [p. 19]

| Setting | SuperGLUE Average | BoolQ Accuracy | CB Accuracy | CB F1 | COPA Accuracy | RTE Accuracy |
|---|---|---|---|---|---|---|
| Fine-tuned SOTA | **89.0** | **91.0** | **96.9** | **93.9** | **94.8** | **92.5** |
| Fine-tuned BERT-Large | 69.0 | 77.4 | 83.6 | 75.7 | 70.6 | 71.7 |
| GPT-3 Few-Shot | 71.8 | 76.4 | 75.6 | 52.0 | 92.0 | 69.0 |

| Setting | WiC Accuracy | WSC Accuracy | MultiRC Accuracy | MultiRC F1a | ReCoRD Accuracy | ReCoRD F1 |
|---|---|---|---|---|---|---|
| Fine-tuned SOTA | **76.1** | **93.8** | **62.3** | **88.2** | **92.5** | **93.3** |
| Fine-tuned BERT-Large | 69.6 | 64.6 | 24.1 | 70.0 | 71.3 | 72.0 |
| GPT-3 Few-Shot | 49.4 | 80.1 | 30.5 | 75.4 | 90.2 | 91.1 |

## Figures

**Figure 3.8** (p. 20): "Performance on SuperGLUE increases with model size and number of examples in context."
- Caption: "A value of K = 32 means that our model was shown 32 examples per task, for 256 examples total divided across the 8 tasks in SuperGLUE. We report GPT-3 values on the dev set, so our numbers are not directly comparable to the dotted reference lines (our test set results are in Table 3.8). The BERT-Large reference model was fine-tuned on the SuperGLUE training set (125K examples), whereas BERT++ was first fine-tuned on MultiNLI (392K examples) and SWAG (113K examples) before further fine-tuning on the SuperGLUE training set (for a total of 630K fine-tuning examples). We find the difference in performance between the BERT-Large and BERT++ to be roughly equivalent to the difference between GPT-3 with one example per context versus eight examples per context."
- **Left panel (SuperGLUE Performance):** X-axis: Billions of Parameters in LM, from 0.1 to 175. Y-axis: SuperGLUE Score, from 40 to 90+. Three lines: Zero-shot (blue), One-shot (green), Few-shot K=32 (orange). Horizontal dashed lines: "Human" at ~90, "Fine-tuned SOTA" at ~89, "Fine-tuned BERT++" at ~70, "Fine-tuned BERT Large" at ~69, "Random Guessing" at ~45. Zero-shot rises from ~48 at 0.1B to ~55 at 175B. One-shot rises from ~50 at 0.1B to ~65 at 175B. Few-shot rises from ~50 at 0.1B to ~72 at 175B. Few-shot GPT-3 175B surpasses both BERT-Large and BERT++ baselines.
- **Right panel (In-Context Learning on SuperGLUE):** X-axis: Number of Examples in Context (K), from 0 to 32. Y-axis: SuperGLUE Score, from 40 to 90+. One line: Few-shot GPT-3 175B (orange). Same horizontal reference lines as left panel. The score increases from ~55 at K=0 to ~72 at K=32, with steepest gains between K=0 and K=8. GPT-3 surpasses the Fine-tuned BERT Large line at approximately K=8.
