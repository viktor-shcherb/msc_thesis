# DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

**Authors:** DeepSeek-AI
**Affiliations:** DeepSeek-AI (research@deepseek.com)
**Venue:** arXiv:2405.04434v5 [cs.CL]
**Date:** 19 Jun 2024

## Abstract

> "We present DeepSeek-V2, a strong Mixture-of-Experts (MoE) language model characterized by economical training and efficient inference. It comprises 236B total parameters, of which 21B are activated for each token, and supports a context length of 128K tokens. DeepSeek-V2 adopts innovative architectures including Multi-head Latent Attention (MLA) and DeepSeekMoE. MLA guarantees efficient inference through significantly compressing the Key-Value (KV) cache into a latent vector, while DeepSeekMoE enables training strong models at an economical cost through sparse computation. Compared with DeepSeek 67B, DeepSeek-V2 achieves significantly stronger performance, and meanwhile saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times. We pretrain DeepSeek-V2 on a high-quality and multi-source corpus consisting of 8.1T tokens, and further perform Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) to fully unlock its potential. Evaluation results show that, even with only 21B activated parameters, DeepSeek-V2 and its chat versions still achieve top-tier performance among open-source models. The model checkpoints are available at https://github.com/deepseek-ai/DeepSeek-V2." [p. 1]

## Section Headings

1. Introduction (p. 4)
2. Architecture (p. 6)
   - 2.1 Multi-Head Latent Attention: Boosting Inference Efficiency (p. 6)
     - 2.1.1 Preliminaries: Standard Multi-Head Attention (p. 6)
     - 2.1.2 Low-Rank Key-Value Joint Compression (p. 7)
     - 2.1.3 Decoupled Rotary Position Embedding (p. 8)
     - 2.1.4 Comparison of Key-Value Cache (p. 8)
   - 2.2 DeepSeekMoE: Training Strong Models at Economical Costs (p. 9)
     - 2.2.1 Basic Architecture (p. 9)
     - 2.2.2 Device-Limited Routing (p. 9)
     - 2.2.3 Auxiliary Loss for Load Balance (p. 10)
     - 2.2.4 Token-Dropping Strategy (p. 11)
3. Pre-Training (p. 11)
   - 3.1 Experimental Setups (p. 11)
     - 3.1.1 Data Construction (p. 11)
     - 3.1.2 Hyper-Parameters (p. 12)
     - 3.1.3 Infrastructures (p. 12)
     - 3.1.4 Long Context Extension (p. 13)
   - 3.2 Evaluations (p. 13)
     - 3.2.1 Evaluation Benchmarks (p. 13)
     - 3.2.2 Evaluation Results (p. 14)
     - 3.2.3 Training and Inference Efficiency (p. 16)
4. Alignment (p. 16)
   - 4.1 Supervised Fine-Tuning (p. 16)
   - 4.2 Reinforcement Learning (p. 17)
   - 4.3 Evaluation Results (p. 18)
   - 4.4 Discussion (p. 20)
5. Conclusion, Limitation, and Future Work (p. 21)
A. Contributions and Acknowledgments (p. 27)
B. DeepSeek-V2-Lite: A 16B Model Equipped with MLA and DeepSeekMoE (p. 29)
   - B.1 Model Description (p. 29)
   - B.2 Performance Evaluation (p. 30)
C. Full Formulas of MLA (p. 31)
D. Ablation of Attention Mechanisms (p. 31)
   - D.1 Ablation of MHA, GQA, and MQA (p. 31)
   - D.2 Comparison Between MLA and MHA (p. 31)
E. Discussion About Pre-Training Data Debiasing (p. 32)
F. Additional Evaluations on Math and Code (p. 32)
G. Evaluation Formats (p. 33)
