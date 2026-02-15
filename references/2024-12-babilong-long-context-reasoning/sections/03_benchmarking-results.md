# Benchmarking Results [p. 4-6]

## Models evaluated [p. 4]

To maximize value for the research community, we have included models with the highest number of monthly downloads³ from the Hugging Face platform in our evaluation such as LLama-3 (AI@Meta, 2024); 32k-64k – Mistral (Jiang et al., 2023), Mixtral (Jiang et al., 2024); 128k – ChatGLM3 (Du et al., 2022), LLama-3.1 (Dubey et al., 2024), Phi-3 and Phi-3.5 (Abdin et al., 2024), Command-R (Cohere, 2024), Qwen-2.5 (Team, 2024); 200k – Yi (Young et al., 2024); including long-context fine-tuning: LongChat (Li et al., 2023a), LLama-2-7b-32k (Xiong et al., 2023), LongAlpaca (Chen et al., 2023); long-context adaptation methods: Yarnv2 Mistral (Peng et al., 2023b), Mistral and LLama-2 with Activation Beacons (Zhang et al., 2024a). As a reference, we included GPT-4 (gpt-4-0125-preview) and Gemini 1.5 Pro 002, currently the most powerful model available. Retrieval-augmented generation was also tested, as it represents a common solution for long document QA. As alternatives to traditional transformer architectures, we considered the Mamba (Gu & Dao, 2023), Jamba (Lieber et al., 2024), Recurrent Memory Transformer (RMT) (Bulatov et al., 2022), and Associative RMT (ARMT) (Rodkin et al., 2024). Summary of evaluation results is presented in the Table 2. The table reports average accuracy of models on the first 5 tasks (QA1-QA5) of BABILong for different context sizes. For evaluation details for each task see Table 4 and Appendix C. [p. 4]

³As of May 2024. Since then we have added new models such as Mistral v0.3, Llama-3.1, Qwen-2.5, Phi-3.5, and GPT-4o-mini.

**Table 2** (p. 4): "BABILong is a challenging benchmark for current long-context models. Even models that claim to support 128K tokens experience degradation beyond their input capacity. RAG methods do not help, while fine-tuning of small scale models (ARMT and RMT, 137M and Mamba, 130M) shows that the tasks are solvable. Values represent average accuracy over QA1-QA5 tasks from BABILong. Models are grouped by the length of the context they claim to support."

[Large detailed table showing performance across different context lengths (0K to 10M tokens) and models. Key observations from the table:]

Models grouped by context length support:
- 0K (baseline, no background text): Most models score 70-100%
- 4K: Scores range 48-100%, with GPT-4 at 76%, various models 60-88%
- 8K: Performance generally declines, 44-94% range
- 16K: Further decline, 37-77% range
- 32K: 28-71% range, significant degradation
- 64K: 19-68% range
- 128K: 13-60% range, major performance drop
- 512K: 8-56% range
- 1M: Very few models tested, 42-78% for those that were
- 10M: Only RMT shows 34% and GPT shows 74%

Notable entries:
- GPT-4: 76% (0K), 52% (4K), 44% (8K), declining to lower scores at longer contexts
- Gemini 1.5 Pro 002: Data shown at various lengths
- Small models (ARMT, RMT): Show competitive performance when fine-tuned
- Most models show steep decline beyond their claimed context window

## Vulnerability to data leakage [p. 4]

are vulnerable to data leakage to training sets of modern large language models (Sainz et al., 2023). Generated benchmarks, such as bAbI and BABILong, are immune to this type of contamination. [p. 4]

## Task design rationale [p. 4]

In this work we deliberately employ simple algorithmic tasks to underscore the fundamental limitations of current models in collecting evidence over long contexts even for basic reasoning. The brevity and similarity of the task sentences also enable the model distinguish them from seemingly close background text with the assistance of specific examples. This difference in distributions enables the scalability of BABILong to large amounts of diverse noise. Nevertheless, the BABILong approach can be applied to incorporate more complex tasks, using the same strategy of mixing task sentences with background text. [p. 4]
