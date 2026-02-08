# 3.8 NLI [p. 20-21]

[p. 20] Natural Language Inference (NLI) [Fyo00] concerns the ability to understand the relationship between two sentences. In practice, this task is usually structured as a two or three class classification problem where the model classifies whether the second sentence logically follows from the first, contradicts the first sentence, or is possibly true (neutral).

## RTE

[p. 21] SuperGLUE includes an NLI dataset, RTE, which evaluates the binary version of the task. On RTE, only the largest version of GPT-3 performs convincingly better than random (56%) in any evaluation setting, but in a few-shot setting GPT-3 performs similarly to a single-task fine-tuned BERT Large.

## ANLI

[p. 21] GPT-3 is also evaluated on the recently introduced Adversarial Natural Language Inference (ANLI) dataset [NWD+19]. ANLI is a difficult dataset employing a series of adversarially mined natural language inference questions in three rounds (R1, R2, and R3). Similar to RTE, all of the models smaller than GPT-3 perform at almost exactly random chance on ANLI, even in the few-shot setting (~33%), whereas GPT-3 itself shows signs of life on Round 3. Results for ANLI R3 are highlighted in Figure 3.9 and full results for all rounds can be found in Appendix H.

## Overall assessment

[p. 21] These results on both RTE and ANLI suggest that NLI is still a very difficult task for language models and they are only just beginning to show signs of progress.

## Figures

**Figure 3.9** (p. 21): "Performance of GPT-3 on ANLI Round 3."
- Caption: "Results are on the dev-set, which has only 1500 examples and therefore has high variance (we estimate a standard deviation of 1.2%). We find that smaller models hover around random chance, while few-shot GPT-3 175B closes almost half the gap from random chance to SOTA. Results for ANLI rounds 1 and 2 are shown in the appendix."
- X-axis: Parameters in LM (Billions), from 0.1B to 175B. Y-axis: Accuracy, from 32 to 48.
- Three lines: Zero-Shot (blue), One-Shot (green), Few-Shot K=50 (orange).
- Horizontal dashed lines: "Fine-tuned SOTA" at ~48, "Fine-tuned RoBERTa-Large" at ~44, "Fine-tuned BERT-Large" at ~43, "Random Guessing" at ~33.
- All three lines are noisy and hover around 33-36 for models from 0.1B to 13B, with substantial variance (one-shot spikes to ~36 at 1.3B then drops back).
- At 175B: Zero-Shot ~34, One-Shot ~35, Few-Shot ~40.
- Only the few-shot 175B model shows a meaningful departure from random chance, closing almost half the gap to fine-tuned SOTA.
