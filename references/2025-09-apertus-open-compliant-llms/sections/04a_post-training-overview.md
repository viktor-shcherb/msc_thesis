# 4 Post-Training [p. 26]

[p. 26] Post-training transforms the pretrained Apertus models into capable instruction-following systems through a two-stage optimization process, following established practices in modern LLM development (Yang et al., 2024b; Riviere et al., 2024; Grattafiori et al., 2024; Lambert et al., 2025; OLMo et al., 2025).

First, *supervised finetuning* adapts the model's outputs to structured conversational formats using curated prompt-completion pairs (SFT, Section 4.2). This stage serves multiple objectives beyond basic instruction following: it teaches the model to recognize and respond appropriately to diverse task types (from creative writing to technical analysis) and in various languages, maintain contextual coherence across multi-turn interactions, and adapt style and level of formality (register) to match user intent. The SFT stage essentially bridges the gap between next-token prediction learned during pretraining and the structured, purposeful generation expected from conversational AI systems. [p. 26]

Second, an *alignment* stage refines the model's behavior according to human preferences and values (Section 4.3). Using preference data together with the QRPO algorithm (Matrenok et al., 2025), the SFT model is optimized for responses that balance multiple qualitative criteria, including helpfulness, harmlessness, and honesty. For Apertus, this alignment process incorporates both standard quality metrics through existing pretrained reward models and constitutional values as encoded in a charter. [p. 26]

The section begins by outlining the data for both the SFT and alignment steps, then turns to the training details for each. Additionally, the post-training pipeline^33 is released with all the reproducibility scripts. Huggingface TRL library^34 and DeepSpeed framework^35 are used for both stages of post-training. The codebase is based on the Python Machine Learning Research Template (Moalla, 2025). [p. 26]

## 4.1 Data Overview [p. 26]

[p. 26] The collection and preparation of post-training data follow the same core principles as the pretraining corpus: transparency, permissive licensing, multilingual inclusivity, and legal compliance. The process begins by collecting openly available datasets, which are subject to legal and quality filtering (4.1.1). Selected datasets are then decontaminated against evaluation benchmarks to ensure the integrity and reliability of downstream assessments (4.1.2).

### 4.1.1 Data Collection & Legal Compliance [p. 26]

**License filtering.** The collection process is initiated by gathering a broad set of candidate datasets and classifying them according to their licensing terms. The selection process is then guided by two criteria: (i) content must be explicitly released under licenses permitting redistribution and commercial use (*e.g.*, CC-BY, Apache 2.0), and (ii) the collection procedure must be fully documented and reproducible. Hence, any dataset picked must be versioned or re-publishable. [p. 26]

At this stage, it is helpful to distinguish between *source datasets* and *compound datasets* (or *mixtures*), which incorporate multiple source datasets or other mixtures. Source dataset selection is straightforward and performed manually. Datasets released under non-permissive or restrictive licenses (*e.g.*, NC or SA), or those with ambiguous or unspecified licenses are excluded. [p. 26]

For compound datasets, a careful verification is undertaken to ensure that the overarching license of a mixture aligns with the licenses of all constituent source datasets and mixtures. In the rare cases where invalid re-licensing is detected, the material is excluded. Likewise, source datasets originating from providers that have opted out of AI training through `robots.txt`, possess share-alike licences (*e.g.*, Reddit, StackExchange), or otherwise fail to meet compliance standards are excluded. This is achieved with a Python-based filtering framework that excludes samples or subsets with incompatible licenses using dataset-specific rules. The approach employs chunked processing for scalability and maintains detailed metadata logs to ensure transparency and reproducibility. The impact of license filtering is evaluated along with decontamination (see Section 4.1.2 and Table 10). [p. 26–27]

**Quality filtering.** Quality filtering is performed through a combination of metadata analysis and manual inspection. Criteria include the provider, the scientific impact of the release, and most importantly whether the data is of human or synthetic origin as initial proxies of quality. Meticulous inspection of dataset samples remains the primary criterion for decision-making. Potential red flags include hallucinations in synthetic data, overly long or incoherent responses, and the presence of repetitive patterns in model outputs. For math- and code-related tasks, datasets with verified solutions are prioritised. [p. 27]

Lastly, keyword-based filtering on prompts and completions is employed to remove organizational branding and identity markers (*e.g.*, "AI2", "Allen Institute", "Open Assistant", "Anthropic", "OpenAI") that could bias Apertus toward the response style of other LLMs, or would create internal confusion about Apertus's actual provenance and capabilities. [p. 27]

---

**Footnotes:**
- ^33: github.com/swiss-ai/posttraining
- ^34: huggingface.co/docs/trl/en/index
- ^35: github.com/deepspeedai/DeepSpeed
