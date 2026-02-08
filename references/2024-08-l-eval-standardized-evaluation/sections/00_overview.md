# Overview

**Title:** L-Eval: Instituting Standardized Evaluation for Long Context Language Models

**Authors:** Chenxin An, Shansan Gong, Ming Zhong, Xingjian Zhao, Mukai Li, Jun Zhang, Lingpeng Kong, Xipeng Qiu

**Affiliations:**
- Fudan University
- The University of Hong Kong
- University of Illinois Urbana-Champaign
- Shanghai AI Lab

**Venue:** Preprint (arXiv:2307.11088v3)

**Date:** 4 Oct 2023

**Code/Data:** https://github.com/OpenLMLab/LEval

## Abstract

> "Recently, there has been growing interest in extending the context length of large language models (LLMs), aiming to effectively process long inputs of one turn or conversations with more extensive histories. While proprietary models such as GPT-4 and Claude can largely preserve the reasoning ability in an extended context, open-source models are still progressing through the early stages of development. To bridge this gap, we propose L-Eval to institute a more standardized evaluation for long context language models (LCLMs) addressing two key aspects: dataset construction and evaluation metrics. On the one hand, we build a new evaluation suite containing 20 sub-tasks, 508 long documents, and over 2,000 human-labeled query-response pairs encompassing diverse question styles, domains, and input length (3k~200k tokens). On the other hand, we investigate the effectiveness in evalution metrics for LCLMs. Results show that popular n-gram matching metrics generally can not correlate well with human judgment, and thus we strongly advocate for length-instruction-enhanced (LIE) evaluation and employing LLM judges. We conducted a comprehensive study of 4 popular commercial LLMs and 12 open-source counterparts using the L-Eval benchmark. Our empirical findings offer useful insights into the study of LCLMs and lay the groundwork for the development of more principled evaluation of these models." [p. 1]

## Section Headings

1. Introduction
2. Related Work
   - 2.1 Long Context Language Models
   - 2.2 Long Sequences Benchmarks
3. Towards High-Quality and Diverse Long Context Datasets
   - 3.1 Data Annotation from Scratch
   - 3.2 Data Re-annotation from Public Datasets
   - 3.3 Data Filtering and Correction
   - 3.4 Statistics
4. Towards Standardized Long Context Evaluation Metrics
   - 4.1 Length Instruction Enhanced Long Context Evaluation
5. Benchmarking LLMs with L-Eval
   - 5.1 Baselines
   - 5.2 Main Results
6. Conclusion
A. Appendix
   - A.1 Baseline Models in L-Eval
   - A.2 Human Evaluation
   - A.3 Analysis
B. Data Collection and Annotation for L-Eval
   - B.1 TOFEL (English Tests)
   - B.2 GSM (16-shot) (Grade School Math)
   - B.3 QuALITY (Gutenberg)
   - B.4 Coursera (Advanced Lectures)
   - B.5 SFiction (Scientific Fictions)
   - B.6 CodeU (Python)
   - B.7 TopicRet (Lengthy Conversation)
   - B.8 LongFQA (Finance)
   - B.9 CUAD (Law)
   - B.10 MultiDoc2Dial (Dialogues over Multi-Documents)
   - B.11 Natural Questions (Wikipedia)
   - B.12 NarrativeQA (Narratives)
   - B.13 Qasper (Papers)
   - B.14 OpenReview (Papers)
   - B.15 GovReport (Government Reports)
   - B.16 QMSum (Meetings)
   - B.17 SPACE (Reviews)
   - B.18 Multi-News (News)
   - B.19 BigPatent (Patents)
   - B.20 SummScreen (TV Show)
