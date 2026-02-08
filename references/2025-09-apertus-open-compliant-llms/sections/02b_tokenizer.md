# 2.2 Tokenizer [p. 10-11]

[p. 10]

The tokenizer is a byte-level BPE model that segments documents into subword units (Sennrich et al., 2016). The authors adapt the established v3 tekken tokenizer from `Mistral-Nemo-Base-2407`, which is designed to accommodate a large proportion of multilingual documents and code.^6 The vocabulary size is 2^17 = 131,072 subwords, as part of which they modified 47 custom special tokens to better support code and math data.^7

The choice was based on a comparison of the tokenizers of several large language models (e.g., Llama-3.1, Mistral-Nemo, Qwen-2.5, and Gemma-2) using four intrinsic evaluation metrics: **fertility rate**, **compression ratio**, **vocabulary utilization**, and **Gini coefficient** (Foroutan et al., 2025a). Fertility rate and compression ratio provide insight into the computational efficiency of a tokenizer. Vocabulary utilization measures how effectively a tokenizer's pre-defined vocabulary represents input text. The Gini coefficient summarizes multilingual fairness by capturing the inequality of tokenization costs across languages. Details of the metrics are provided in Appendix I.

The evaluations are conducted using the FLORES+ development set covering 55 languages (nll, 2024). Figure 1 presents the comparison results. Mistral-Nemo achieves the lowest Gini coefficient, indicating more equitable tokenization costs across languages. More broadly, Mistral-Nemo matches or outperforms the other tokenizers in vocabulary utilization, fertility rate, and compression ratio, highlighting its strong global efficiency. Although Mistral-Nemo and Gemma-2 show similar performance on fertility rate and compression ratio, Mistral-Nemo is selected as the preferred tokenizer because it is fairer across languages and uses a smaller vocabulary (128k vs. 256k), making it more efficient for pretraining without sacrificing performance.

### Figure 1

**Figure 1** (p. 11): **Intrinsic Evaluation of Four Multilingual Tokenizers.** The Mistral-Nemo tokenizer consistently matches or outperforms other tokenizers in fertility rate, compression ratio, and vocabulary utilization, highlighting its strong overall efficiency. In addition, it achieves a lower Gini coefficient, indicating greater fairness by distributing tokenization costs more evenly across languages.

The figure contains four bar chart panels, each comparing Llama-3.1, Mistral-Nemo, Qwen-2.5, and Gemma-2:

1. **Fertility Rate (lower is better):** Y-axis: # Tokens / # Bytes. Approximate values: Llama-3.1 ~0.35, Mistral-Nemo ~0.32, Qwen-2.5 ~0.33, Gemma-2 ~0.32.
2. **Compression Ratio (higher is better):** Y-axis: # Lines / # Tokens. Approximate values: Llama-3.1 ~0.015, Mistral-Nemo ~0.025, Qwen-2.5 ~0.02, Gemma-2 ~0.025.
3. **Gini Coefficient (lower is better):** Y-axis scale 0-0.4. Approximate values: Llama-3.1 ~0.32, Mistral-Nemo ~0.20, Qwen-2.5 ~0.25, Gemma-2 ~0.22.
4. **Vocabulary Utilization (higher is better):** Y-axis: Vocabulary Utilization [%], scale 0-0.6. Approximate values: Llama-3.1 ~0.42, Mistral-Nemo ~0.52, Qwen-2.5 ~0.38, Gemma-2 ~0.35.

Mistral-Nemo shows the best or near-best performance across all four metrics.

**Footnotes:**
- ^6: https://huggingface.co/mistralai/Mistral-Nemo-Base-2407
- ^7: https://huggingface.co/swiss-ai/Apertus-70B-2509
