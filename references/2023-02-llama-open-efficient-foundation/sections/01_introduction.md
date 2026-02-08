# Introduction [p. 1]

[p. 1] Large Language Models (LLMs) trained on massive corpora of text have shown the ability to perform new tasks from textual instructions or from a few examples (Brown et al., 2020). These few-shot properties first appeared when scaling models to a sufficient size (Kaplan et al., 2020), resulting in a line of work that focuses on further scaling these models (Chowdhery et al., 2022; Rae et al., 2021). These efforts are based on the assumption that more parameters will lead to better performance.

However, recent work from Hoffmann et al. (2022) shows that, for a given compute budget, the best performances are not achieved by the largest models, but by smaller models trained on more data.

The objective of the scaling laws from Hoffmann et al. (2022) is to determine how to best scale the dataset and model sizes for a particular *training* compute budget. However, this objective disregards the *inference* budget, which becomes critical when serving a language model at scale. Given a target level of performance, the preferred model is not the fastest to train but the fastest at inference, and although it may be cheaper to train a large model to reach a certain level of performance, a smaller one trained longer will ultimately be cheaper at inference.

Key finding: although Hoffmann et al. (2022) recommends training a 10B model on 200B tokens, the authors find that a 7B model continues to improve even after 1T tokens. [p. 1]

The focus of this work is to train a series of language models that achieve the best possible performance at various inference budgets, by training on more tokens than what is typically used. The resulting models, called *LLaMA*, range from 7B to 65B parameters with competitive performance compared to the best existing LLMs. Key claims:

- **Contribution:** LLaMA-13B outperforms GPT-3 on most benchmarks, despite being 10x smaller. The authors believe this model will help democratize the access and study of LLMs, since it can be run on a single GPU. [p. 1]
- **Contribution:** The 65B-parameter model is competitive with the best large language models such as Chinchilla or PaLM-540B. [p. 1]
- **Contribution:** Unlike Chinchilla, PaLM, or GPT-3, they only use publicly available data, making the work compatible with open-sourcing, while most existing models rely on data which is either not publicly available or undocumented (e.g. "Books -- 2TB" or "Social media conversations"). [p. 1]

Open-source exceptions noted: OPT (Zhang et al., 2022), GPT-NeoX (Black et al., 2022), BLOOM (Scao et al., 2022), and GLM (Zeng et al., 2022), but none are competitive with PaLM-62B or Chinchilla. [p. 1]

Paper outline: modifications to the transformer architecture (Vaswani et al., 2017), training method, performance comparison on standard benchmarks, and exposure of biases and toxicity using responsible AI benchmarks. [p. 1]
