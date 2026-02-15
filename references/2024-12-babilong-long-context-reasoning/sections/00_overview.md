# Overview

**Title:** BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack

**Authors:** Yuri Kuratov¹'², Aydar Bulatov¹'², Petr Anokhin¹, Ivan Rodkin², Dmitry Sorokin¹, Artyom Sorokin¹, Mikhail Burtsev³

**Affiliations:**
- ¹AIRL Moscow, Russia
- ²Neural Networks and Deep Learning Lab, MIPT, Dolgoprudny, Russia
- ³London Institute for Mathematical Sciences, London, UK

**Contact:** {yurii.kuratov,bulatov.as}@phystech.edu, mb@lims.ac.uk

**Venue:** 38th Conference on Neural Information Processing Systems (NeurIPS 2024) Track on Datasets and Benchmarks

**Date:** November 2024 (arXiv:2406.10149v2, 6 Nov 2024)

## Abstract

> "In recent years, the input context sizes of large language models (LLMs) have increased dramatically. However, existing evaluation methods have not kept pace, failing to comprehensively assess the efficiency of models in handling long contexts. To bridge this gap, we introduce the BABILong benchmark, designed to test language models' ability to reason across facts distributed in extremely long documents. BABILong includes a diverse set of 20 reasoning tasks, including fact chaining, simple induction, deduction, counting, and handling lists/sets. These tasks are challenging on their own, and even more demanding when the required facts are scattered across long natural text. Our evaluations show that popular LLMs effectively utilize only 10-20% of the context and their performance declines sharply as length and task complexity increase. Among alternatives to in-context reasoning, Retrieval-Augmented Generation methods achieve a modest 60% accuracy on single-fact question answering, independent of context length. Among context extension methods, the highest performance is demonstrated by recurrent memory transformers after fine-tuning, enabling the processing of lengths up to 50 million tokens. The BABILong benchmark is extendable to any length to support the evaluation of new upcoming models with increased capabilities, and we provide splits up to 10 million token lengths." [p. 1]

## Section Headings (p. 1-21+)

- 1 Introduction
- 2 The BABILong Benchmark for Long Context Processing
- 3 Benchmarking Results
  - 3.1 Evaluation of Effective Context Size
  - 3.2 Retrieval-Augmented Generation Does Not Perform Well on BABILong
  - 3.3 Fine-Tuning Models on BABILong
  - 3.4 BABILong and Other Benchmarks
- 4 Related Work on Long Context Benchmarks and Datasets
- Conclusions
- Limitations
- Author contributions
- Acknowledgments and Disclosure of Funding
- References (p. 11-15)
- Appendices (p. 16-21+)
  - Appendix A: Code and Data Availability (p. 16)
    - A.1 Reproducibility
  - Appendix B: Related Work on Long Context Models (p. 16-17)
  - Appendix C: Details on RMT, ARMT, and Mamba fine-tuning and evaluation on BABILong (p. 17-18)
  - Appendix D: Detailed LLMs evaluation on BABILong QA1-5 tasks (p. 18-19)
  - Appendix E: Gemini Evaluation (p. 20)
  - Appendix F: BABILong Dataset Statistics (p. 20-21)
  - Appendix G: Details of the RAG Pipeline (p. 21)
  - Appendix H: Recurrent Memory Transformer Analysis (p. 22)
  - Appendix I: LLMs fine-tuning results (p. 22)
  - Appendix J: Prompts Used to Benchmark Large Language Models (p. 22-25)
  - Appendix K: Analysis of LLM Performance for Different Locations of the Supporting Facts (p. 26)
  - Appendix L: BABILong Task Examples (p. 27-30)
  - Appendix M: Author Statement (p. 31)
  - Appendix N: BABILong Datasheet (p. 31+)
