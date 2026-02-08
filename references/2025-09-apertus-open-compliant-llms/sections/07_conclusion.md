# 7 Conclusion [p. 57]

[p. 57] This report introduced Apertus, a new foundation model suite from the Swiss AI Initiative designed around three commitments: data compliance, broad multilingual coverage, and full transparency on outputs. The models are trained on 15T tokens from 1811 languages with retroactive respect for `robots.txt` and related opt outs, and with a Goldfish-style objective to curb verbatim reproduction of training text. The authors then post-train multilingual Apertus-{8B,70B}-Instruct variants to improve interaction across a large set of languages, and further align the model to reflect constitutional values when delving into controversial topics.

Experiments show strong performance across a range of knowledge, cultural, and instruction-following evaluations. Model weights are released together with data preparation recipes, evaluation suites, and training artifacts to support independent audit, replication, and extension. All outputs are released under permissive licenses and designed to comply with the data provisions of the EU AI Act, enabling use in both commercial and non-commercial settings.

The authors note that the name *Apertus* is Latin for *open*, reflecting the commitment to transparency. The culture of openness befits the public institutional basis of the Swiss AI Initiative, which supports this research program.

> "Apertus is both the largest fully open LLM released to date, and the first state-of-the-art LLM developed by a fully open, publicly funded academic consortium." [p. 57]

## Future Directions

[p. 57] Several directions are highlighted to broaden the scientific and societal impact of Apertus:

- **Scaling.** Train larger models and longer-context variants while preserving the compliance and transparency guarantees established here.
- **Distillation.** Distil the 70B model into smaller students for constrained settings without eroding multilingual and safety properties.
- **Data-to-performance mapping.** Systematically study how specific data slices and data governance choices affect capabilities, fairness, and memorization across domains.
- **Reasoning with adaptive compute.** Explore test-time variable computation that allocates more steps to harder inputs, including internal chain-of-thought tokens, routing, and variable-depth architectures (Wei et al., 2022).
- **RL with verifiers.** Develop RLVR pipelines that combine preference optimization with explicit verifiers for math, code, and other tasks with verifiable reasoning steps (OpenAI, 2024; DeepSeek-AI et al., 2025).
- **Multimodality.** Extend the stack to visual, sonic, and other data modalities while maintaining the same compliance standards for data collection and release.
- **Societal alignment.** Elicit and model diverse Swiss and multilingual preferences to inform alignment objectives and evaluation (Stammbach et al., 2024; Kirk et al., 2025).
- **Field evaluation.** Run structured studies with domain professionals and the public to assess reliability, usability, and real-world impact across languages and sectors.

[p. 57] Apertus aims to set a new baseline for trustworthy and globally relevant open models by pairing capable multilingual systems with verifiable data practices and complete reproducibility. The authors invite the community to inspect, stress test, and build on these models and artifacts so that future iterations are both more powerful and more accountable.
