# Overview

**Title:** RWKV: Reinventing RNNs for the Transformer Era

**Authors:** Bo Peng\*, Eric Alcaide\*, Quentin Anthony\*, Alon Albalak, Samuel Arcadinho, Stella Biderman, Huanqi Cao, Xin Cheng, Michael Chung, Xingjian Du, Matteo Grella, Kranthi Kiran GV, Xuzheng He, Haowen Hou, Jiaju Lin, Przemyslaw Kazienko, Jan Kocon, Jiaming Kong, Bartlomiej Koptyra, Hayden Lau, Krishna Sri Ipsit Mantri, Ferdinand Mom, Atsushi Saito, Guangyu Song, Xiangru Tang, Bolun Wang, Johan S. Wind, Stanislaw Wozniak, Ruichong Zhang, Zhenyuan Zhang, Qihang Zhao, Peng Zhou, Qinghua Zhou, Jian Zhu, Rui-Jie Zhu (\* Equal first authorship. Others listed alphabetically.) [p. 1]

**Affiliations:** Generative AI Commons, EleutherAI, U. of Barcelona, Charm Therapeutics, Ohio State U., U. of C. Santa Barbara, Zendesk, Booz Allen Hamilton, Tsinghua University, Peking University, Storyteller.io, Crisis24, New York U., National U. of Singapore, Wroclaw U. of Science and Technology, Databaker Technology, Purdue U., Criteo AI Lab, Epita, Nextremer, Moves, Yale U., RuoxinTech, U. of Oslo, U. of Science and Technology of China, Kuaishou Technology, U. of British Columbia, U. of C. Santa Cruz, U. of Electronic Science and Technology of China [p. 1]

**Venue:** arXiv:2305.13048v2 [cs.CL]

**Date:** 11 Dec 2023

## Abstract

> "Transformers have revolutionized almost all natural language processing (NLP) tasks but suffer from memory and computational complexity that scales quadratically with sequence length. In contrast, recurrent neural networks (RNNs) exhibit linear scaling in memory and computational requirements but struggle to match the same performance as Transformers due to limitations in parallelization and scalability. We propose a novel model architecture, Receptance Weighted Key Value (RWKV), that combines the efficient parallelizable training of transformers with the efficient inference of RNNs." [p. 1]

> "Our approach leverages a linear attention mechanism and allows us to formulate the model as either a Transformer or an RNN, thus parallelizing computations during training and maintains constant computational and memory complexity during inference. We scale our models as large as 14 billion parameters, by far the largest dense RNN ever trained, and find RWKV performs on par with similarly sized Transformers, suggesting future work can leverage this architecture to create more efficient models. This work presents a significant step towards reconciling trade-offs between computational efficiency and model performance in sequence processing tasks." [p. 1]

## Section Headings

1. Introduction [p. 1-2]
2. Background [p. 2-3]
   - 2.1 Recurrent Neural Networks (RNNs) [p. 2]
   - 2.2 Transformers and AFT [p. 2-3]
3. RWKV [p. 3-5]
   - 3.1 Architecture [p. 3-5]
     - 3.1.1 Token Shift [p. 3-4]
     - 3.1.2 WKV Operator [p. 4]
     - 3.1.3 Output Gating [p. 4-5]
   - 3.2 Transformer-like Training [p. 5]
   - 3.3 RNN-like Inference [p. 5]
   - 3.4 Additional Optimizations [p. 5]
   - 3.5 Implementation [p. 5]
4. Trained Models and Computing Costs [p. 5-6]
   - 4.1 Additional Training Details [p. 5-6]
   - 4.2 Scaling Laws [p. 6]
5. Evaluations [p. 6-8]
   - 5.1 NLP Evaluations [p. 6-7]
   - 5.2 Extended Context Finetuning [p. 6-7]
   - 5.3 Long Context Benchmarks [p. 8]
6. Inference Experiments [p. 8]
7. Future Work [p. 8]
8. Conclusions [p. 8-9]
9. Limitations [p. 9]
10. Ethics Statement [p. 9-10]
Acknowledgements [p. 9]
References [p. 9-13]
A. Author Contributions (summary) [p. 14]
B. Author Contributions (detailed) [p. 15-16]
C. Additional Related Work [p. 16]
D. Time-Mixing Block as an RNN Cell [p. 17]
E. Parameter Initializations [p. 17-18]
F. Small Init Embedding [p. 18]
G. Hyperparameters [p. 19]
H. Gradient Stability in RWKV [p. 19-20]
I. Model Behavior Visualization [p. 20-21]
J. Additional Evaluations [p. 21-23]
   - J.1 Further details on NLP tasks [p. 21]
   - J.2 Evaluation on Long Range Arena [p. 23]
   - J.3 Enwik8 Perplexity [p. 23]
K. Inference Results [p. 23-25]
L. Importance of Prompt Construction and Comparison to GPT Models [p. 25-26]
M. Cases [p. 26-30]
