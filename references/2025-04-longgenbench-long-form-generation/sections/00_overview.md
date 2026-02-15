# Overview

**Title:** LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs

**Authors:** Yuhao Wu¹, Ming Shan Hee¹, Zhiqing Hu¹, Roy Ka-Wei Lee¹

**Affiliations:**
- ¹Singapore University of Technology and Design

**Contact:** {wu_yuhao, mingshan_hee, zhiqing_hu}@mymail.sutd.edu.sg, roy_lee@sutd.edu.sg

**Venue:** Published as a conference paper at ICLR 2025

**Date:** 2024-09 (arXiv: 2409.02076)

**Repository:** https://github.com/mozhu621/LongGenBench

## Abstract

> "Current benchmarks like 'Needle-in-a-Haystack' (NIAH), Ruler, and Needlebench focus on models' ability to understand long-context input sequences but fail to capture a critical dimension: the generation of high-quality long-form text. Applications such as design proposals, technical documentation, and creative writing rely on coherent, instruction-following outputs over extended sequences—a challenge that existing benchmarks do not adequately address. To fill this gap, we introduce LongGenBench, a novel benchmark designed to rigorously evaluate large language models' (LLMs) ability to generate long text while adhering to complex instructions. Through tasks requiring specific events or constraints within generated text, LongGenBench evaluates model performance across four distinct scenarios, three instruction types, and two generation-lengths (16K and 32K tokens). Our evaluation of ten state-of-the-art LLMs reveals that, despite strong results on Ruler, all models struggled with long text generation on LongGenBench, particularly as text length increased. This suggests that current LLMs are not yet equipped to meet the demands of real-world, long-form text generation. We open-source LongGenBench to promote comprehensive evaluation and improvement in this critical area, with code and data available at https://github.com/mozhu621/LongGenBench."

## Section Headings

1. Introduction
2. LongGenBench Benchmark
   - 2.1 Task Definition
   - 2.2 Four Distinct Scenario Setups
   - 2.3 Specific Task Instruction
   - 2.4 Evaluation Metric
   - 2.5 Evaluations Pipeline
3. Experiments
   - 3.1 Experimental Setup
   - 3.2 Main Result
   - 3.3 Accuracy Trend with Varying Sequence Length
   - 3.4 Three Specific Task Instructions
   - 3.5 Comparison with Long-Context Input
4. Analysis and Limitations
   - Richness of Content
   - Rationality of Content
   - Instruction Data
   - Generalizability
5. Related Work
   - Instruction Following
   - Long-context Benchmarks and Tasks
   - Long-form Text Generation
6. Conclusion
7. Acknowledgment
8. References
