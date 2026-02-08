# Overview

**Title:** ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding

**Authors:** Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Berant, Omer Levy

**Affiliations:**
- Uri Shaham: The Blavatnik School of Computer Science, Tel Aviv University
- Maor Ivgi: The Blavatnik School of Computer Science, Tel Aviv University
- Avia Efrat: The Blavatnik School of Computer Science, Tel Aviv University
- Jonathan Berant: The Blavatnik School of Computer Science, Tel Aviv University
- Omer Levy: The Blavatnik School of Computer Science, Tel Aviv University; Meta AI

**Venue:** arXiv:2305.14196v3 [cs.CL]

**Date:** 17 December 2023

## Abstract

> "We introduce ZeroSCROLLS, a zero-shot benchmark for natural language understanding over long texts, which contains only test and small validation sets, without training data. We adapt six tasks from the SCROLLS benchmark, and add four new datasets, including two novel information fusing tasks, such as aggregating the percentage of positive reviews. Using ZeroSCROLLS, we conduct a comprehensive evaluation of both open-source and closed large language models, finding that Claude outperforms ChatGPT, and that GPT-4 achieves the highest average score. However, there is still room for improvement on multiple open challenges in ZeroSCROLLS, such as aggregation tasks, where models struggle to pass the naive baseline. As the state of the art is a moving target, we invite researchers to evaluate their ideas on the live ZeroSCROLLS leaderboard." [p. 1]

## Section Headings

1. Introduction
2. Background: SCROLLS
3. The ZeroSCROLLS Benchmark
   - 3.1 Tasks
     - 3.1.1 Summarization
     - 3.1.2 Question Answering
     - 3.1.3 Aggregation
   - 3.2 Prompting
   - 3.3 Automatic Evaluation
4. Evaluating State-of-the-Art LLMs
   - 4.1 Models
   - 4.2 Main Results
   - 4.3 Impact of Model Size and Input Length
5. Analysis
   - Discrepancies in Question Answering
   - Format Discrepancy
6. Conclusion
7. Limitations
Acknowledgements
A. Prompts
