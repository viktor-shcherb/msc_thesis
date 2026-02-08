# Overview

**Title:** LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding

**Authors:** Yushi Bai^{1,2}, Xin Lv^2, Jiajie Zhang^{1,2}, Hongchang Lyu^3, Jiankai Tang^1, Zhidian Huang^1, Zhengxiao Du^{1,2}, Xiao Liu^{1,2}, Aohan Zeng^{1,2}, Lei Hou^1, Yuxiao Dong^{1,dagger}, Jie Tang^1, Juanzi Li^{1,dagger}

**Affiliations:**
1. Tsinghua University
2. Zhipu.AI
3. Institute of Automation, Chinese Academy of Sciences

(dagger = corresponding authors)

**Venue:** arXiv:2308.14508v2

**Date:** 19 Jun 2024 (v2)

**Abstract:**
> "Although large language models (LLMs) demonstrate impressive performance for many language tasks, most of them can only handle texts a few thousand tokens long, limiting their applications on longer sequence inputs, such as books, reports, and codebases. Recent works have proposed methods to improve LLMs' long context capabilities by extending context windows and more sophisticated memory mechanisms. However, comprehensive benchmarks tailored for evaluating long context understanding are lacking. In this paper, we introduce LongBench, the first bilingual, multi-task benchmark for long context understanding, enabling a more rigorous evaluation of long context understanding. LongBench comprises 21 datasets across 6 task categories in both English and Chinese, with an average length of 6,711 words (English) and 13,386 characters (Chinese). These tasks cover key long-text application areas including single-doc QA, multi-doc QA, summarization, few-shot learning, synthetic tasks, and code completion. All datasets in LongBench are standardized into a unified format, allowing for effortless automatic evaluation of LLMs. Upon comprehensive evaluation of 8 LLMs on LongBench, we find that: (1) Commercial model (GPT-3.5-Turbo-16k) outperforms other open-sourced models, but still struggles on longer contexts. (2) Scaled position embedding and fine-tuning on longer sequences lead to substantial improvement on long context understanding. (3) Context compression technique such as retrieval brings improvement for model with weak ability on long contexts, but the performance still lags behind models that have strong long context understanding capability." [p. 1]

## Section Headings

1. Introduction [p. 1-2]
2. Related Work [p. 2-3]
3. LongBench: Task and Construction [p. 3-5]
   - 3.1 Problem Definition [p. 3]
   - 3.2 Dataset Construction [p. 3-5]
     - 3.2.1 Data Collection and Annotation [p. 3-5]
     - 3.2.2 Data Extraction [p. 5-6]
4. Experiments [p. 6-9]
   - 4.1 Benchmarking Results on LongBench and LongBench-E [p. 6-8]
   - 4.2 Impact of Context Compression Techniques [p. 8-9]
   - 4.3 Context Understanding or Memorization? [p. 9]
5. Conclusion [p. 9]
6. Limitations [p. 9-10]
Acknowledgement [p. 10]
References [p. 10-12]
A. Dataset Details [p. 13-14]
B. Evaluation Setups [p. 14-17]
C. Radar Plot and Analysis [p. 17-18]
D. Analysis on the Inter-task Correlation on LongBench [p. 18]
E. Full results on LongBench-E [p. 19]
