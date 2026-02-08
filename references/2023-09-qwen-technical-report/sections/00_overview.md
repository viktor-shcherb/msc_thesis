# Qwen Technical Report — Overview

**Title:** Qwen Technical Report

**Authors:** Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, Tianhang Zhu

**Affiliation:** Qwen Team, Alibaba Group

**Venue:** arXiv preprint (arXiv:2309.16609v1)

**Date:** 28 Sep 2023

**Correspondence:** ericzhou.zc@alibaba-inc.com

> "Large language models (LLMs) have revolutionized the field of artificial intelligence, enabling natural language processing tasks that were previously thought to be exclusive to humans. In this work, we introduce QWEN, the first installment of our large language model series. QWEN is a comprehensive language model series that encompasses distinct models with varying parameter counts. It includes QWEN, the base pretrained language models, and QWEN-CHAT, the chat models finetuned with human alignment techniques. The base language models consistently demonstrate superior performance across a multitude of downstream tasks, and the chat models, particularly those trained using Reinforcement Learning from Human Feedback (RLHF), are highly competitive. The chat models possess advanced tool-use and planning capabilities for creating agent applications, showcasing impressive performance even when compared to bigger models on complex tasks like utilizing a code interpreter. Furthermore, we have developed coding-specialized models, CODE-QWEN and CODE-QWEN-CHAT, as well as mathematics-focused models, MATH-QWEN-CHAT, which are built upon base language models. These models demonstrate significantly improved performance in comparison with open-source models, and slightly fall behind the proprietary models."

## Section Headings

1. Introduction
2. Pretraining
   - 2.1 Data
   - 2.2 Tokenization
   - 2.3 Architecture
   - 2.4 Training
   - 2.5 Context Length Extension
   - 2.6 Experimental Results
3. Alignment
   - 3.1 Supervised Finetuning
     - 3.1.1 Data
     - 3.1.2 Training
   - 3.2 Reinforcement Learning from Human Feedback
     - 3.2.1 Reward Model
     - 3.2.2 Reinforcement Learning
   - 3.3 Automatic and Human Evaluation of Aligned Models
   - 3.4 Tool Use, Code Interpreter, and Agent
4. CODE-QWEN: Specialized Model for Coding
   - 4.1 Code Pretraining
   - 4.2 Code Supervised Fine-Tuning
   - 4.3 Evaluation
5. MATH-QWEN: Specialized Model for Mathematics Reasoning
   - 5.1 Training
   - 5.2 Evaluation
6. Related Work
   - 6.1 Large Language Models
   - 6.2 Alignment
   - 6.3 Tool Use and Agents
   - 6.4 LLM for Coding
   - 6.5 LLM for Mathematics
7. Conclusion
A. Appendix
   - A.1 More Training Details
     - A.1.1 Data Format for QWEN-CHAT
   - A.2 Evaluation
     - A.2.1 Automatic Evaluation
     - A.2.2 Human Evaluation
   - A.3 Analysis of Code Interpreter
