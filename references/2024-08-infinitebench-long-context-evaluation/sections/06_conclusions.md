# 6 Conclusions [p. 9–10]

[p. 9–10] The authors introduce InfiniteBench, the first benchmark tailored for long contexts exceeding 100K in average length. Empirical evidence indicates that despite claims of proficiency with such extensive contexts, current LLMs demonstrate significant performance degradation when dealing with them. This finding highlights the need for advanced methodologies to improve LLMs' efficiency in processing long context. Additionally, the analysis offers insights into LLM behavior in long-context tasks, guiding future research.

## Limitations

[p. 10] While the benchmark offers valuable insights into LLM performance, it may not be sufficiently diverse or extensive to provide a comprehensive assessment of model capabilities, a constraint common to most benchmarks. Additionally, the reliance on exact match for scoring, dependent on prompt templates and answer parsing methods, may necessitate tailored redesigns for new model evaluations.

Furthermore, supporting contexts up to 100K tokens may fall short for applications requiring analysis of extensive datasets, such as multiple books or entire databases. Exploring LLMs' capacity to handle up to a million tokens or more presents a promising research avenue. In practical applications, finetuning models to memorize context, rather than processing it during inference, could offer a more efficient alternative, albeit with significant computational demands.

## Ethics Statement

[p. 10] The human annotators are directed to exclude data that may raise sensitive ethical issues, such as offensive language or social biases. Nonetheless, the potential for encountering sensitive content persists, particularly if the sourced books or code contain such material. This concern is somewhat mitigated since the benchmark's primary focus is on evaluating the long-context capabilities of LLMs, rather than influencing their social bias.

The goal of this research is to advance the development of LLMs' proficiency in handling extensive contexts. This could aid in implementing more effective "guardrails" against misuse by incorporating detailed specifications prior to user interactions. However, this approach also potentially increases the risk of novel prompt injection attacks.
