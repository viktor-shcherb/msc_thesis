# 5 Evaluations [p. 37]

**Figure 7** (p. 37): **Pretraining Models Evaluation Curves.** "Comparison of downstream evaluation results across model checkpoints as training progresses. Global Evaluation uses the full suite of evaluation benchmarks. English, EU and Swiss Evaluation each includes only the tasks that involve the languages specific to that region. The aggregation between different benchmarks consists of a macro aggregation, where each different language of each dataset is considered as a separate datapoint to aggregate."

The figure contains four panels:
- **Global Evaluation Macro** (top-left): Accuracy (y-axis, ~0.25-0.55) vs Consumed Tokens (x-axis, 0.0T-15.0T). Shows Apertus-70B reaching ~0.55 at ~15T tokens, Apertus-8B reaching ~0.45. Models plotted include Apertus-70B, Apertus-8B, OLMo2-7B, OLMo2-32B, EuroLLM-1.7B, EuroLLM-9B, SmolLM3-1.7B, SmolLM3-8B, Llama3.1-8B, Llama3.1-70B.
- **English Evaluation Macro** (top-right): Accuracy (~0.45-0.75) vs Consumed Tokens (0.0T-15.0T). Apertus-70B reaches ~0.73, competitive with Llama3.1-70B.
- **EU Evaluation Macro** (bottom-left): Accuracy (~0.25-0.60) vs Consumed Tokens (0.0T-15.0T). Apertus-70B reaches ~0.58, leading other models.
- **Swiss Evaluation Macro** (bottom-right): Accuracy (~0.25-0.60) vs Consumed Tokens (0.0T-15.0T). Apertus-70B reaches ~0.58.

In all four panels, Apertus-70B and Apertus-8B show consistent improvement with more consumed tokens. The Apertus family shows consistently strong multilingual capabilities (Global, EU, Swiss Evaluation Macro) while maintaining highly competitive results in English.

---

[p. 37] The performance of Apertus is tracked from pretraining to post-training alignment. At each phase, benchmarks are tailored to the specific capabilities the model is expected to develop by that training point. These benchmarks span a wide range of tasks and domains to ensure comprehensive skill coverage. The evaluation includes both *English* and *multilingual* benchmarks, making it one of the most extensive and linguistically diverse assessments of a multilingual LLM to date. Notably, it features the most thorough evaluation yet on African and Eurasian languages, covering over **94 languages** in total. The benchmarks used at each stage are detailed in Table 22. Models are compared against a set of models that fall into two categories: *open-weight* and *fully open* models (Table 16). Open-weight models provide checkpoints but do not fully release all components, such as training data or code. Fully open models, by contrast, release not only the model weights but also training recipes, datasets, and code for complete reproducibility.
