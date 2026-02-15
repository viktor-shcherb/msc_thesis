# 5. Ablations [p. 5–6]

In this section, the authors focus on the impact of their architecture changes, as well as some of the vision abilities new to this model.

## 5.1. Pre-training ability probing [p. 5–6]

The authors use several standard benchmarks as probes during pre-training to ensure their models capture general abilities, and in Figure 2, the authors compare the quality of pre-trained models from Gemma 2 and 3 across these general abilities, namely, science, code, factuality, multilinguality, reasoning, and vision. The details of the performance across the different public benchmarks used in these probes are summarized in the appendix. Overall, the authors see that the new versions improve in most categories, despite the addition of vision. The authors particularly focus on multilinguality in this version, and this directly impacts the quality of their models. However, despite the use of decontamination techniques, there is always a risk of contamination of these probes (Mirzadeh et al., 2024), making more definitive conclusions harder to assess.

**Figure 2** (p. 6): "Summary of the performance of different pre-trained models from Gemma 2 and 3 across general abilities. These plots are meant to give a simplified summary and details are in the appendix."

Description: Three radar charts comparing pre-trained model performance
- Key elements: Three separate radar charts showing six dimensions (Code, Vision, Factuality, Reasoning, Science, Multilingual). Each chart compares different models with colored lines (red for Gemma 2 models, blue for Gemma 3 models)
  - Left chart: Gemma 2 (2B, 9B) vs Gemma 3 (1B, 4B)
  - Middle chart: Gemma 2 (9B) vs Gemma 3 (12B)
  - Right chart: Gemma 2 (27B) vs Gemma 3 (27B)
- Notable patterns: Gemma 3 models (blue lines) generally show improvements across most dimensions compared to Gemma 2 models (red lines), with particularly strong performance in Vision (a new capability). The charts show progressive improvement with model size.
- Supports claim: Demonstrates that Gemma 3 improves in most categories despite the addition of vision, with particular focus on multilinguality improvements

## 5.2. Local:Global attention layers [p. 6]

The authors measure the impact of changes to local and global self-attention layers on performance and memory consumption during inference.

### Local:Global ratio [p. 6]

In Fig. 3, the authors compare different ratios of local to global attention layers. 1:1 is used in Gemma 2 models, and 5:1 is used in Gemma 3. The authors observe minimal impact on perplexity when changing this ratio.

**Figure 3** (p. 6): "Impact of Local:Global ratio on the perplexity on a validation set. The impact is minimal, even with 7-to-1 local to global. This ablation is run with text-only models."

Description: Line plot showing perplexity vs local:global ratio
- Key elements: Two lines (labeled "2B" in orange and "9B" in yellow) showing delta perplexity on y-axis (ranging from -0.1 to 0.1) versus Local:Global ratio on x-axis (1:1, 3:1, 5:1, 7:1)
- Notable patterns: Both lines remain relatively flat and close to zero across all ratios, indicating minimal impact on perplexity
- Supports claim: Demonstrates that increasing the ratio of local to global attention layers (up to 7:1) has minimal impact on model perplexity, validating the architectural choice of 5:1 for Gemma 3

### Sliding window size [p. 6–7]

In Fig. 4, the authors compare different sliding window sizes for the local attention layers in different global:local ratio configurations. The sliding window can be reduced significantly without impacting perplexity.
