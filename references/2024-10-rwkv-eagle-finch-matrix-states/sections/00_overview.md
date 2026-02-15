# Overview [p. 1–2]

## Paper Information

**Title:** Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence

**Authors:** Bo Peng^{1,2,*}, Daniel Goldstein^{2,3,*}, Quentin Anthony^{2,4,23,*}, Alon Albalak^{2,5,9}, Eric Alcaide^{2,7,6,8}, Stella Biderman^{2,6}, Eugene Cheah^{1,2,3}, Xingjian Du^1, Teddy Ferdinan^9, Haowen Hou^{10}, Przemysław Kazienko^9, Kranthi Kiran GV^{2,11}, Jan Kocoń^9, Bartłomiej Koptyra^9, Satyapriya Krishna^7, Ronald McClelland Jr.^{2,12}, Jiaju Lin^{24}, Niklas Muennighoff^{11}, Fares Obeid^2, Atsushi Saito^{2,13}, Guangyu Song^{2,23}, Haoqin Tu^{16,17}, Cahya Wirawan^{2,16}, Stanisław Woźniak^9, Ruichong Zhang^{19}, Bingchen Zhao^{20}, Qihang Zhao^{21}, Peng Zhou^{21}, Jian Zhu^{22}, Rui-Jie Zhu^{17}

^* Equal first authorship. Others listed alphabetically.

**Affiliations:**
1. RWKV Project (under Linux Foundation AI & Data)
2. EleutherAI
3. Recursal AI
4. Ohio State University
5. University of California, Santa Barbara
6. SynthLabs
7. Charm Therapeutics
8. Dalle Molle Institute for Artificial Intelligence Research
9. Wrocław Tech
10. Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ)
11. New York University
12. Harvard University
13. Ronsor Labs
14. Nextremer Co. Ltd.
15. University of Chinese Academy of Sciences
16. University of California, Santa Cruz
17. AI-Research.id
18. Tsinghua University
19. University of Edinburgh
20. LuxiTech Co. Ltd.
21. University of British Columbia
22. Zyphra
23. Pennsylvania State University
24. Tano Labs

**Venue/Date:** Conference on Language Modeling (COLM), October 7–9, 2024, Philadelphia; arXiv:2404.05892v4 [cs.CL], 26 Sep 2024

**Code/Models:**
- Models: https://huggingface.co/RWKV
- Training code: https://github.com/RWKV/RWKV-LM
- Inference code: https://github.com/RWKV/ChatRWKV
- Time-parallel training code: https://github.com/RWKV/RWKV-infctx-trainer

**License:** Apache 2.0

## Abstract

> "We present Eagle (RWKV-5) and Finch (RWKV-6), sequence models improving upon the RWKV (RWKV-4) (Peng et al., 2023) architecture. Our architectural design advancements include multi-headed matrix-valued states and a dynamic recurrence mechanism that improve expressivity while maintaining the inference efficiency characteristics of RNNs. We introduce a new multilingual corpus with 1.12 trillion tokens and a fast tokenizer based on greedy matching for enhanced multilinguality. We trained four Eagle models, ranging from 0.46 to 7.5 billion parameters, and two Finch models with 1.6 and 3.1 billion parameters and find that they achieve competitive performance across a wide variety of benchmarks. We release all our models on HuggingFace under the Apache 2.0 license." [p. 1]

## Section Headings

1. Introduction (p. 3)
2. Background (p. 4)
3. Eagle/Finch Architecture (p. 5)
4. Method (p. 6)
   - 4.1 Eagle (p. 6)
     - 4.1.1 Eagle Token Shift (p. 6)
     - 4.1.2 Eagle Time Mixing (p. 7)
     - 4.1.3 Channel Mixing (p. 7)
   - 4.2 Finch (p. 7)
     - 4.2.1 Finch Token Shift (p. 7)
     - 4.2.2 Finch Time Mixing (p. 8)
5. RWKV World Tokenizer (p. 8)
6. RWKV World v2 Dataset (p. 9)
7. Pre-Trained Models (p. 9)
8. Language Modeling Experiments (p. 9)
   - 8.1 LM Evaluation Harness Benchmarks (p. 9)
   - 8.2 Associative Recall (p. 11)
   - 8.3 Long Context Experiments (p. 12)
   - 8.4 Bamboo Benchmark (p. 12)
9. Speed and Memory Benchmarks (p. 14)
10. Multimodal Experiments (p. 15)
    - 10.1 RWKV Music Modelling (p. 15)
    - 10.2 VisualRWKV (p. 15)
11. RWKV on Audio (p. 16)
12. Conclusions (p. 17)

**Appendices:**
- A. Author Contributions (p. 28)
- B. Additional Architecture Details (p. 29)
- C. Additional Related Work (p. 32)
- D. Training Dataset Details (p. 33)
- E. Computing Costs (p. 33)
- F. New Tokenizer Details (p. 35)
- G. Additional Evaluations (p. 36)
- H. Hyperparameters (p. 38)
- I. Parameter Initializations (p. 38)
- J. Architectural Ablations (p. 40)
- K. DDLerp Ablations (p. 41)
- L. Non-English Chat Examples (p. 41)
- M. Chat Examples - Comparison with RWKV-4 (p. 43)
