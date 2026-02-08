# 8. Flash-8B: Pushing the Frontier for More Efficient Models [p. 45–46]

[p. 45] Flash-8B is a transformer decoder model derived from the architectural innovations and optimizations employed in the development of Flash. By inheriting the same core architecture, optimizations, and data mixture refinements as its larger counterpart, Flash-8B demonstrates multimodal capabilities with support for context window exceeding 1 million tokens. This unique combination of speed, quality, and capabilities represents a step function leap in the domain of single-digit billion parameter models.

[p. 45] While Flash-8B's smaller form factor necessarily leads to a reduction in quality compared to Flash and 1.5 Pro, it unlocks substantial benefits, particularly in terms of high throughput and extremely low latency. This translates to affordable and timely large-scale multimodal deployments, facilitating novel use cases previously deemed infeasible due to resource constraints. Examples of such use cases include:

- **Large-Scale Data Labeling:** Flash-8B's efficiency enables the automated labeling of massive datasets, accelerating the training process for other downstream models.
- **High-Throughput Agent Serving:** Flash-8B can power intelligent agents deployed at scale, facilitating real-time interactions with a large user base.
- **Model Integration in Complex Workflows:** Flash-8B's speed facilitates its integration into intricate workflows involving multiple models working in tandem, unlocking sophisticated capabilities.

[p. 45] At the time of writing, Flash-8B remains under active development, with ongoing efforts focused on maximizing its performance within the given inference budget. However, the authors present preliminary results to underscore the model's competitive standing. This achievement paves the way for delivering high-quality intelligence to billions of users, democratizing access to advanced AI technologies.

## Multimodality

[p. 45] Initial evaluations demonstrate strong multimodal performance from Flash-8B across a range of visual tasks. The findings indicate that Flash-8B achieves approximately 80-90% of the performance exhibited by Flash on established benchmarks, demonstrating a minimal trade-off between efficiency and capability as demonstrated in Table 22.

## Long Context

[p. 45] To evaluate long context performance of Gemini 1.5 Flash-8B, it is evaluated on the same long documents and code data sources used to evaluate Gemini 1.5 Pro and Gemini 1.5 Flash. Figure 7 shows the cumulative NLL up to a specific token index. A power law of the form *L*(*x*) = *alpha* * *x*^*beta* + *gamma* is also fit to these data points (dashed line). In the same way as the other Gemini 1.5 models, Gemini 1.5 Flash-8B NLL decreases monotonically with sequence length and thus prediction accuracy improves up to the tested sequence lengths (1M for long documents, and 2M for code). This indicates that even at its small size, Gemini 1.5 Flash-8B also can make use of the whole input even at very long-context lengths, leveraging information that might have occurred millions of tokens earlier in the document. A power law can hold between log-loss and context length up to extremely long context lengths for Gemini 1.5 Flash-8B as well.

**Figure 20** (p. 47): "Cumulative average negative log-likelihood (NLL) as a function of token position in long documents and code data. A lower value demonstrates better prediction. Although with some expected degradation compared to Gemini 1.5 Flash, Gemini 1.5 Flash-8B shows the same impressive long context scaling trends as Gemini 1.5 Pro and Gemini 1.5 Flash for both long documents and code data up to 2 million tokens."

- **Left panel:** Cumulative Average NLL for Long Documents. R^2 = 0.991. X-axis: sequence position (128 to 1M). Y-axis: negative log-likelihood. Shows power law fit (dashed line), Gemini 1.5 Flash (red), and Gemini 1.5 Flash-8B (yellow). Both curves decrease monotonically; Flash-8B runs consistently higher (worse NLL) than Flash but follows the same downward trend.
- **Right panel:** Cumulative Average NLL for Code. R^2 = 0.998. X-axis: sequence position (128 to 2M). Y-axis: negative log-likelihood. Same comparison. Flash-8B again tracks the same power law scaling pattern as Flash, with a consistent quality gap.

## Table 22

**Table 22** (p. 46): A sampling of evaluation results comparing Gemini 1.5 Flash-8B and Gemini 1.5 Flash models on a few standard evaluations spanning capabilities and modalities. Unless otherwise stated we report accuracy. All numbers are obtained after instruction-tuning, as described in Section 4.

| Capability | Benchmark | Gemini 1.5 Flash-8B | Gemini 1.5 Flash |
|---|---|---|---|
| Math and Science | **GPQA:** Graduate-Level Google-Proof Q&A. (Rein et al., 2023) | 30.8%, 0-shot | 39.5%, 0-shot |
| Math and Science | **MATH:** Math problems ranging across 5 levels of difficulty and 7 sub-disciplines. (Hendrycks et al., 2021b) | 35.9%, 4-shot, Minerva prompt | 54.9%, 4-shot, Minerva prompt |
| General Reasoning | **BigBench - Hard:** A subset of harder tasks from Big Bench formatted as CoT problems. (Srivastava et al., 2022; Suzgun et al., 2022) | 69.5%, 3-shot | 85.5%, 3-shot |
| General Reasoning | **MMLU (test):** Multiple-choice questions in 57 subjects (professional & academic). (Hendrycks et al., 2021a) | 68.1%, 5-shot | 78.9%, 5-shot |
| Coding | **Natural2Code** chat preamble* (Metric: pass rate). | 67.6%, 0-shot | 77.2%, 0-shot |
| Multilinguality | **MGSM:** Multilingual math reasoning. (Shi et al., 2023a) | 70.5%, 8-shot | 82.4%, 8-shot |
| Multilinguality | **CoVoST 2:** Automatic speech translation (20 languages). Metric: BLEU (up). (Wang et al., 2020) | 24.9, 0-shot | 36.1, 0-shot |
| Multimodal | **MMMU (val):** Image-based, multi-discipline, college-level problems. (Yue et al., 2023) | 50.3%, 4-shot | 56.1%, 0-shot |
| Multimodal | **DocVQA:** Visual QA on documents with text and non-textual elements. (Mathew et al., 2021) | 73.6%, 0-shot | 88.8%, 0-shot |
| Multimodal | **TextVQA:** Visual QA on text within images. (Singh et al., 2019) | 66.7%, 0-shot | 78.7%, 0-shot |
| Video understanding | **VATEX (test):** English video captioning. Metric: CIDER (Vedantam et al., 2015). (Wang et al., 2019a) | 53.2, 4-shot | 57.1, 4-shot |
