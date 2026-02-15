# Overview

## Paper Metadata

**Title:** HELMET: How to Evaluate Long-Context Language Models Effectively and Thoroughly

**Authors:** Howard Yen, Tianyu Gao, Minmin Hou, Ke Ding, Daniel Fleischer, Peter Izsak, Moshe Wasserblat, Danqi Chen

**Affiliations:**
- Princeton Language and Intelligence, Princeton University
- Intel

**Contact:** {hyen, tianyug, danqic}@cs.princeton.edu

**URL:** https://princeton-nlp.github.io/HELMET

**Venue:** Published as a conference paper at ICLR 2025

**ArXiv:** arXiv:2410.02694v3 [cs.CL] 6 Mar 2025

## Abstract

> Many benchmarks exist for evaluating long-context language models (LCLMs), yet developers often rely on synthetic tasks such as needle-in-a-haystack (NIAH) or an arbitrary subset of tasks. However, it remains unclear whether these benchmarks reflect the diverse downstream applications of LCLMs, and such inconsistencies further complicate model comparison. We investigate the underlying reasons behind these practices and find that existing benchmarks often provide noisy signals due to limited coverage of applications, insufficient context lengths, unreliable metrics, and incompatibility with base models. In this work, we introduce HELMET (How to Evaluate Long-context Models Effectively and Thoroughly), a comprehensive benchmark encompassing seven diverse, application-centric categories. We also address several issues in previous benchmarks by adding controllable lengths up to 128K tokens, model-based evaluation for reliable metrics, and few-shot prompting for robustly evaluating base models. Consequently, we demonstrate that HELMET offers more reliable and consistent rankings of frontier LCLMs. Through a comprehensive study of 59 LCLMs, we find that (1) synthetic tasks like NIAH do not reliably predict downstream performance; (2) the diverse categories in HELMET exhibit distinct trends and low correlations with each other; and (3) while most LCLMs achieve perfect NIAH scores, open-source models significantly lag behind closed ones when tasks require full-context reasoning or following complex instructions—the gap widens as length increases. Finally, we recommend using our RAG tasks for fast model development, as they are easy to run and better predict other downstream performance; ultimately, we advocate for a holistic evaluation across diverse tasks.

## Section Headings

1. Introduction [p. 1-2]
2. Our Benchmark: HELMET [p. 3-6]
   - 2.1 Realistic and diverse long-context applications [p. 3-5]
   - 2.2 Reliable evaluation metrics [p. 5-6]
   - 2.3 Robust prompting and controlled evaluation settings [p. 6]
3. Analysis [p. 7-9]
   - 3.1 Simple synthetic tasks are poor predictors of real-world performance [p. 7]
   - 3.2 Diverse LCLM applications call for diverse evaluation [p. 8]
   - 3.3 Model performance across tasks and lengths [p. 8-9]
4. Related Works [p. 10]
5. Conclusion [p. 10]
6. Reproducibility Statement [p. 11]
7. Acknowledgments [p. 11]
8. References [p. 11-28]
A. Appendix A: Comparison with Other Benchmarks [p. 29-30]
   - A.1 Results [p. 29-30]
   - A.2 Discussions [p. 29-30]
B. Appendix B: Datasets [p. 31-34]
   - B.1 Retrieval-Augmented Generation [p. 31-32]
   - B.2 Generation with Citations [p. 32]
   - B.3 Passage Re-ranking [p. 32]
   - B.4 In-context Learning [p. 32]
   - B.5 Synthetic Tasks [p. 32-33]
   - B.6 Model-based Evaluation [p. 33-34]
C. Appendix C: Models [p. 34]
D. Appendix D: Experimental Setup [p. 34]
E. Appendix E: Additional Results [p. 35-51]
   - E.1 Correlation between Synthetic and Downstream Tasks [p. 35]
   - E.2 Correlation between Datasets [p. 36]
   - E.3 Positional Embedding Extrapolation Remains a Challenge [p. 37-38]
   - E.4 Presence of Lost in the Middle [p. 38-39, 46-48]
   - E.5 Comparison between Base and Instruction-tuned Models [p. 39]
   - E.6 Performance of Claude [p. 39, 49-51]
   - E.7 Full Results [p. 39]
