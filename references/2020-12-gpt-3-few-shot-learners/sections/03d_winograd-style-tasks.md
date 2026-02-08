# 3.4 Winograd-Style Tasks [p. 16-17]

[p. 16] The Winograd Schemas Challenge [LDM12] is a classical task in NLP that involves determining which word a pronoun refers to, when the pronoun is grammatically ambiguous but semantically unambiguous to a human. Recently fine-tuned language models have achieved near-human performance on the original Winograd dataset, but more difficult versions such as the adversarially-mined Winogrande dataset [SBBC19] still significantly lag human performance. GPT-3's performance is tested on both Winograd and Winogrande, as usual in the zero-, one-, and few-shot setting.

## Winograd results

[p. 17] On Winograd, GPT-3 is tested on the original set of 273 Winograd schemas, using the same "partial evaluation" method described in [RWC+19]. Note that this setting differs slightly from the WSC task in the SuperGLUE benchmark, which is presented as binary classification and requires entity extraction to convert to the form described in this section. On Winograd GPT-3 achieves 88.3%, 89.7%, and 88.6% in the zero-shot, one-shot, and few-shot settings, showing no clear in-context learning but in all cases achieving strong results just a few points below state-of-the-art and estimated human performance. Contamination analysis found some Winograd schemas in the training data but this appears to have only a small effect on results (see Section 4).

## Winogrande results

[p. 17] On the more difficult Winogrande dataset, gains to in-context learning are found: GPT-3 achieves 70.2% in the zero-shot setting, 73.2% in the one-shot setting, and 77.7% in the few-shot setting. For comparison a fine-tuned RoBERTa model achieves 79%, state-of-the-art is 84.6% achieved with a fine-tuned high capacity model (T5), and human performance on the task as reported by [SBBC19] is 94.0%.

### Table 3.5: Results on the WSC273 version of Winograd schemas and the adversarial Winogrande dataset. See Section 4 for details on potential contamination of the Winograd test set. [p. 16]

| Setting | Winograd | Winogrande (XL) |
|---|---|---|
| Fine-tuned SOTA | **90.1**^a | **84.6**^b |
| GPT-3 Zero-Shot | 88.3* | 70.2 |
| GPT-3 One-Shot | 89.7* | 73.2 |
| GPT-3 Few-Shot | 88.6* | 77.7 |

^a [SBBC19] ^b [LYN+20]

Note: Asterisks (*) on Winograd results indicate potential test set contamination concerns (see Section 4).

## Figures

**Figure 3.5** (p. 16): "Zero-, one-, and few-shot performance on the adversarial Winogrande dataset as model capacity scales. Scaling is relatively smooth with the gains to few-shot learning increasing with model size, and few-shot GPT-3 175B is competitive with a fine-tuned RoBERTa-large."
- X-axis: Parameters in LM (Billions), from 0.1B to 175B. Y-axis: Accuracy, from 50 to 90.
- Three lines: Zero-Shot (blue), One-Shot (green), Few-Shot K=50 (orange).
- Horizontal dashed lines: "Human" at ~94, "Fine-tuned SOTA" at ~85, "Fine-tuned RoBERTa-Large" at ~79, "Fine-tuned BERT-Large" at ~67, "Random Guessing" at 50.
- All three lines rise from ~50-53 at 0.1B. At 175B: Zero-Shot ~70, One-Shot ~73, Few-Shot ~77.7.
- Few-shot scaling is steeper than zero-shot, with the gap widening at larger model sizes.
- Few-shot GPT-3 175B is competitive with fine-tuned RoBERTa-Large.
