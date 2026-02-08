# Overview

**Title:** Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**Authors:** Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, Denny Zhou

**Affiliations:** Google Research, Brain Team

**Venue:** 36th Conference on Neural Information Processing Systems (NeurIPS 2022)

**Date:** 2022 (arXiv v6: 10 Jan 2023)

## Abstract

> "We explore how generating a chain of thought---a series of intermediate reasoning steps---significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-of-thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting. Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking. For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier." [p. 1]

## Section Headings

1. Introduction
2. Chain-of-Thought Prompting
3. Arithmetic Reasoning
   - 3.1 Experimental Setup
   - 3.2 Results
   - 3.3 Ablation Study
   - 3.4 Robustness of Chain of Thought
4. Commonsense Reasoning
5. Symbolic Reasoning
6. Discussion
7. Related Work
8. Conclusions
- Acknowledgements
- Checklist
- A Frequently Asked Questions
  - A.1 Why does increasing model scale improve chain-of-thought prompting?
  - A.2 What is the role of prompt engineering?
  - A.3 Will chain-of-thought prompting improve performance for my task of interest?
  - A.4 Why is prompting with the equation only not enough for some arithmetic reasoning datasets?
- B All Experimental Results
- C Extended Related Work
  - C.1 Prompting
  - C.2 Natural language explanations
  - C.3 Program synthesis and execution
  - C.4 Numeric and logical reasoning
  - C.5 Intermediate language steps
- D Additional Analysis
  - D.1 Correct Chain of Thought Analysis
  - D.2 Incorrect Chain of Thought Analysis
  - D.3 Additional Robustness Analysis
- E Additional Details
  - E.1 Reproducibility Statement
  - E.2 Computational Resources
  - E.3 Dataset Details and Licenses
- F Appendix: Input/Output Examples
- G Appendix: Full Prompts
- H Appendix: Alternate Annotators for MWP
