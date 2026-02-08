# Overview

**Title:** Qwen2 Technical Report

**Authors:** An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan Lin, Jialong Tang, Jialin Wang, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Ma, Jianxin Yang, Jin Xu, Jingren Zhou, Jinze Bai, Jinzheng He, Junyang Lin, Kai Dang, Keming Lu, Keqin Chen, Kexin Yang, Mei Li, Mingfeng Xue, Na Ni, Pei Zhang, Peng Wang, Ru Peng, Rui Men, Ruize Gao, Runji Lin, Shijie Wang, Shuai Bai, Sinan Tan, Tianhang Zhu, Tianhao Li, Tianyu Liu, Wenbin Ge, Xiaodong Deng, Xiaohuan Zhou, Xingzhang Ren, Xinyu Zhang, Xipin Wei, Xuancheng Ren, Xuejing Liu, Yang Fan, Yang Yao, Yichang Zhang, Yu Wan, Yunfei Chu, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, Zhifang Guo, and Zhihao Fan

**Affiliations:** Qwen Team, Alibaba Group (authors ordered alphabetically by first name)

**Venue:** arXiv:2407.10671v4

**Date:** 10 Sep 2024

## Abstract

> "This report introduces the Qwen2 series, the latest addition to our large language models and large multimodal models. We release a comprehensive suite of foundational and instruction-tuned language models, encompassing a parameter range from 0.5 to 72 billion, featuring dense models and a Mixture-of-Experts model. Qwen2 surpasses most prior open-weight models, including its predecessor Qwen1.5, and exhibits competitive performance relative to proprietary models across diverse benchmarks on language understanding, generation, multilingual proficiency, coding, mathematics, and reasoning." [p. 1]

> "The flagship model, Qwen2-72B, showcases remarkable performance: 84.2 on MMLU, 37.9 on GPQA, 64.6 on HumanEval, 89.5 on GSM8K, and 82.4 on BBH as a base language model. The instruction-tuned variant, Qwen2-72B-Instruct, attains 9.1 on MT-Bench, 48.1 on Arena-Hard, and 35.7 on LiveCodeBench. Moreover, Qwen2 demonstrates robust multilingual capabilities, proficient in approximately 30 languages, spanning English, Chinese, Spanish, French, German, Arabic, Russian, Korean, Japanese, Thai, Vietnamese, and more, underscoring its versatility and global reach." [p. 1]

> "To foster community innovation and accessibility, we have made the Qwen2 model weights openly available on Hugging Face and ModelScope, and the supplementary materials including example code on GitHub. These platforms also include resources for quantization, fine-tuning, and deployment, facilitating a wide range of applications and research endeavors." [p. 1]

## Section Headings

1. Introduction (p. 3)
2. Tokenizer & Model (p. 3)
   - 2.1 Tokenizer (p. 3)
   - 2.2 Model Architecture (p. 4)
     - 2.2.1 Qwen2 Dense Model (p. 4)
     - 2.2.2 Qwen2 Mixture-of-experts Model (p. 4)
     - 2.2.3 Model Configuration (p. 5)
3. Pre-training (p. 5)
   - 3.1 Pre-training Data (p. 5)
   - 3.2 Long-context Training (p. 6)
4. Post-training (p. 6)
   - 4.1 Post-training Data (p. 6)
     - 4.1.1 Collaborative Data Annotation (p. 7)
     - 4.1.2 Automated Data Synthesis (p. 7)
   - 4.2 Supervised Fine-tuning (p. 8)
   - 4.3 Reinforcement Learning from Human Feedback (p. 8)
5. Evaluation (p. 8)
   - 5.1 Base Language Models (p. 8)
     - 5.1.1 Core Capabilities (p. 8)
   - 5.2 Instruction-tuned Model (p. 12)
     - 5.2.1 Open Benchmark Evaluation (p. 12)
     - 5.2.2 In-house Automatic Evaluation (p. 14)
     - 5.2.3 Long Context Capabilities (p. 15)
     - 5.2.4 Multilingual Evaluation (p. 18)
     - 5.2.5 Safety & Responsibility (p. 18)
     - 5.2.6 Contamination Analysis (p. 19)
6. Conclusion (p. 20)
7. References (p. 21–26)
