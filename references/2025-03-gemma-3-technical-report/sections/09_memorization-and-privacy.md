# 6. Memorization and Privacy [p. 8–9]

Large language models may produce near-copies of entire text used in training (Biderman et al., 2023; Carlini et al., 2021, 2022; Ippolito et al., 2022; Nasr et al., 2023). Several prior reports have released audits that quantify this risk by measuring the memorization rate (Anil et al., 2023; Chowdhery et al., 2022; Gemini Team, 2023, 2024; Gemma Team, 2024a,b; LLaMa Team, 2024). This "memorization rate"¹ is defined as the ratio of generations from the model that match its training data compared to all model generations using the following setup. We follow the methodology described in Gemma Team (2024b) to measure it.

Specifically, we subsample a large portion of training data distributed uniformly across different corpora and test for discoverable extraction (Nasr et al., 2023) of this content using a prefix of length 50 and a suffix of length 50. We denote text as either "exactly memorized" if all tokens in the completion match the source suffix or "approximately memorized" if they match up to an edit distance of 10%.

**Figure 9** (p. 9): "Total memorization rates for both exact and approximate memorization. Gemma 3 models memorize significantly less than all prior models. *No results for approximate memorization on these models."

Description: Bar chart
- X-axis: Different models (ordered in reverse chronological order, with newest Gemma 3 models on left)
- Y-axis: % Memorized (ranging from 0.001 to 10, log scale)
- Two bar types: "Exact" (teal) and "Approximate" (darker teal/green)
- Models shown include: [unclear: individual model names not fully readable but includes Gemma 3 1B, 4B, 12B, 27B and prior Gemini models]
- Notable patterns:
  - Gemma 3 models show memorization rates around 0.001-0.01%
  - Prior models show higher rates, ranging up to approximately 1%
  - Clear decreasing trend from older to newer models
- Supports claim: Gemma 3 models memorize significantly less than prior models

Figure 9 compares the memorization rates across Gemma and Gemini models; the models are ordered in reverse chronological order, with the newest Gemma 3 models on the left. We find that Gemma 3 models memorize significantly less text at a much lower rate than prior models (note the log y-axis). We observe only a marginal difference in the memorization rates between the 4B, 12B, and 27B models, with 1B memorizing less than these larger models. Further, we find that a larger proportion of text is characterized as approximately memorized, with a relative increase in approximate memorization compared to exact memorization of roughly 24x on average.

We also study the rate at which the generations may contain personal information. To identify potentially personal information, we use the Google Cloud Sensitive Data Protection (SDP) service.² SDP uses broad detection rules to identify text that may contain personal information. SDP is designed to have high recall and does not consider the context in which the information may appear, which leads to many false positives. Thus, we are likely overestimating the true amount of potentially personal information contained in the outputs classified as memorized. SDP also provides broad severity levels: low, medium, and high. We classify text as personal if SDP classifies it as personal information at any severity level. We observed no personal information in the outputs characterized as memorization for all Gemma 3 models. This indicates a low rate of personal data, below our detection thresholds, in outputs classified as memorization.

---

¹We do not state or imply [here] that a model "contains" its training data in the sense that there is a copy of that data in the model. Rather, a model memorizes attributes of its training data such that in certain cases it is statistically able to generate such training data when following rules and using information about features of its training data that it does contain."

²https://cloud.google.com/sensitive-data-protection
