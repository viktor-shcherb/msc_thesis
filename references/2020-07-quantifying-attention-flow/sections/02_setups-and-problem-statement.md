# 2 Setups and Problem Statement [p. 2–3]

## Task and dataset

[p. 2] The analysis focuses on the **verb number prediction task**: predicting singularity or plurality of a verb of a sentence, when the input is the sentence up to the verb position. The authors use the **subject-verb agreement dataset** (Linzen et al., 2016).

This task and dataset are convenient because they offer a clear hypothesis about what part of the input is essential for the correct solution. For instance, given "*the key to the cabinets*" as input, attending to "key" helps the model predict singular as output, while attending to "cabinets" (an *agreement attractor*, with the opposite number) is unhelpful.

## Model

[p. 2] The authors train a Transformer encoder with GPT-2 Transformer blocks as described in Radford et al. (2019); Wolf et al. (2019) (without masking). Model specifications:
- **Layers:** 6
- **Heads:** 8
- **Hidden/embedding size:** 128
- A `CLS` token is added (similar to BERT, Devlin et al., 2019) and its embedding in the final layer is used as the input to the classifier
- **Accuracy** on subject-verb agreement task: **0.96**

Code publicly available at: https://github.com/samiraabnar/attention_flow

## Observations on raw attention

[p. 2] Visualizing raw attention in Figure 1a (like Vig, 2019): for a correctly classified example, only in the first couple of layers are there some distinctions in the attention patterns for different positions, while in higher layers the attention weights are rather uniform.

**Figure 2** (p. 2): "Raw Attention maps for the `CLS` token at different layers."
Shows heatmaps of raw attention from the `CLS` token at different layers. The figure demonstrates that raw attention scores of the `CLS` token over input tokens (x-axis) at different layers (y-axis) similarly lack an interpretable pattern.

These observations reflect the fact that as we go deeper into the model, the embeddings are more contextualized and may all carry similar information. This underscores the need to track down attention weights all the way back to the input layer, and is in line with findings of Serrano and Smith (2019), who show that attention weights do not necessarily correspond to the relative importance of input tokens.

## Evaluation methodology

[p. 2] To quantify the usefulness of raw attention weights and the two proposed alternatives, besides input gradients, the authors employ an input ablation method, **blank-out**, to estimate an importance score for each input token. Blank-out replaces each token in the input, one by one, with `UNK` and measures how much it affects the predicted probability of the correct class.

The authors compute the **Spearman's rank correlation coefficient** between the attention weights of the `CLS` embedding in the final layer and the importance scores from blank-out.

## Table 1

[p. 2]

**Table 1:** SpearmanR correlation of attention based importance with blank-out scores for 2000 samples from the test set for the verb number prediction model.

|         | L1             | L2             | L3              | L4              | L5             | L6             |
|---------|----------------|----------------|-----------------|-----------------|----------------|----------------|
| Raw     | 0.69+/-0.27    | 0.10+/-0.43    | -0.11+/-0.49    | -0.09+/-0.52    | 0.20+/-0.45    | 0.29+/-0.39    |
| Rollout | 0.32+/-0.26    | 0.38+/-0.27    | 0.51+/-0.26     | 0.62+/-0.26     | 0.70+/-0.25    | 0.71+/-0.24    |
| Flow    | 0.32+/-0.26    | 0.44+/-0.29    | 0.70+/-0.25     | 0.70+/-0.22     | 0.71+/-0.22    | 0.70+/-0.22    |

[p. 2] The correlation between raw attention weights of the `CLS` token and blank-out scores is rather low, except for the first layer.
