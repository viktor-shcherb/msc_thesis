# 1 Introduction [p. 1-2]

## Core Problem Statement

[p. 1] Long-context capability has become one of the fundamental competencies (Gao et al., 2024; Liu et al., 2024b; Li et al., 2024; Agarwal et al., 2024) of contemporary large language models (LLMs) because it takes the average human critical time and effort to digest long-form context, making a long-context-capable LLM beyond desirable.

To assess the long-context capabilities of LLMs, various evaluation benchmarks and metrics have been proposed, including:
- LongBench (Bai et al., 2023)
- L-Eval (An et al., 2023)
- NIAH (Needle in the Haystack)
- RULER (Hsieh et al., 2024)
- Ada-LEval (Wang et al., 2024)
- Loogle (Li et al., 2023a)

## Key Shortcomings of Existing Benchmarks

[p. 1] However, these benchmarks often exhibit at least one of the following three shortcomings:

### (1) Non-Reflective Synthetic Content

They rely on purely synthetic contents (like NIAH), which the authors call non-reflective synthetic and do not reflect how LLMs are used in real-life scenarios, potentially limiting the applicability of their results. Non-reflective synthetic benchmarks such as NIAH or PassKey Retrieval, where the source (e.g., a string of digits or a phrase) bears no semantic or task relevance to the padding content (e.g., unrelated posts) to evaluate models.

### (2) Fixed Input Length Per Sample

They adopt a fixed input length per data sample, making them suitable only for certain LLMs with compatible context windows. This is a major problem because context windows have grown significantly, thanks to the development of context-extension techniques and post-training recipes. With Llama 3.1 (Dubey et al., 2024) claiming a context window of 128k (in contrast to the 4k context of Llama 2), many once "long-context" datasets have already become outdated. It is therefore foreseeable that many evaluations we see today will no longer be reflective as time passes.

### (3) Conflating Performance Metrics

Moreover, having different lengths per individual data sample makes the evaluation unintuitive for many budget methods (like StreamingLLM (Xiao et al., 2023a) and InfLLM (Xiao et al., 2024)), where an arbitrarily set constant budget is applied to all inputs, ignoring the fact that this budget may exceed certain data samples. As a result, the reported "compressed performance" often mixes into a known mixture of both compressed and uncompressed practices, complicating fair assessments.

[p. 2] They do not address the conflation between base ability and long-context capability, as these benchmarks evaluate long-context capabilities only based on task scores without isolating the influence of a model's baseline abilities. Such conflation can lead to inaccurate assessments of a model's inherent capacity to handle extended contexts, ultimately hindering the accurate measurement of true long-context potential.

## Proposed Solution: 🏀-LongBench

[p. 1-2] The authors address such problems by providing a **new benchmark** involving a rich set of length-controllable real and synthetic tasks — 🏀-LongBench — and a **new evaluation metric** — LongScore — which leads to significant shifts in model rankings compared to traditional performance-based evaluations, as shown in Table 1.

**Table 1: Models' ranking on Ruler** (Hsieh et al., 2024) with different metrics [p. 1, abstract area]

| Model (size, length) | Base Ability | Old Metric | Proposed Metric |
|---------------------|--------------|------------|-----------------|
| Llama3.1 (70B, 128K) | 96.5₍₁₎ | 88.2₍₁₎ | -8.6₍₁₎ |
| Phi3-medium (14B, 128K) | 93.5₍₂₎ | 86.3₍₂₎ | -7.5₍₃₎ |
| Phi3-medium (14B, 128K) | 93.3₍₃₎ | 79.1₍₃₎ | -15.1₍₄₎ |
| LWM (7B, 1M) (Liu et al., 2024a) | 82.5₍₄₎ | 70.3₍₄₎ | -13.0₍₅₎ |

**Note:** Base Ability represents model's score within 4k context. **Old/Proposed Metric** represents the average score across various lengths using traditional metric/our proposed metric. 96.5₍₁₎ indicates a score of 96.5 with a rank of 1. More details are in Table 5. Comparing the ranking of Old Metric and Proposed Metric reveals that the rankings of the old metrics are heavily influenced by the model's inherent abilities, which do not really reflect long-context ability.

## Contributions

[p. 2] The paper:

1. **First validates the reliability** of the proposed 🏀-LongBench and the effectiveness of LongScore
2. **Then comprehensively benchmarks** various open-source models, providing **fresh insights** into long-context evaluation and offering a more accurate assessment that better reflects models' true abilities to handle extended contexts

The results of other methods are in Appendix A.1.
