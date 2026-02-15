# Overview

**Title:** DeepSeek-V3 Technical Report

**Authors:** DeepSeek-AI

**Affiliation:** DeepSeek-AI (research@deepseek.com)

**Venue/Publication:** arXiv:2412.19437v2 [cs.CL]

**Date:** 18 Feb 2025

**Model Checkpoints:** https://github.com/deepseek-ai/DeepSeek-V3

## Abstract

> "We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities. Comprehensive evaluations reveal that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Despite its excellent performance, DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training. In addition, its training process is remarkably stable. Throughout the entire training process, we did not experience any irrecoverable loss spikes or perform any rollbacks. The model checkpoints are available at https://github.com/deepseek-ai/DeepSeek-V3." [p. 1]

## Section Headings

Based on the table of contents (pages 2-3):

1. Introduction (p. 4)
2. Architecture (p. 6)
   - 2.1 Basic Architecture (p. 6)
     - 2.1.1 Multi-Head Latent Attention (p. 7)
     - 2.1.2 DeepSeekMoE with Auxiliary-Loss-Free Load Balancing (p. 8)
   - 2.2 Multi-Token Prediction (p. 10)
3. Infrastructures (p. 11)
   - 3.1 Compute Clusters (p. 11)
   - 3.2 Training Framework (p. 12)
     - 3.2.1 DualPipe and Computation-Communication Overlap (p. 12)
     - 3.2.2 Efficient Implementation of Cross-Node All-to-All Communication (p. 13)
     - 3.2.3 Extremely Memory Saving with Minimal Overhead (p. 14)
   - 3.3 FP8 Training (p. 14)
     - 3.3.1 Mixed Precision Framework (p. 15)
     - 3.3.2 Improved Precision from Quantization and Multiplication (p. 16)
     - 3.3.3 Low-Precision Storage and Communication (p. 18)
   - 3.4 Inference and Deployment (p. 18)
     - 3.4.1 Prefilling (p. 19)
     - 3.4.2 Decoding (p. 19)
   - 3.5 Suggestions on Hardware Design (p. 20)
     - 3.5.1 Communication Hardware (p. 20)
     - 3.5.2 Compute Hardware (p. 20)
4. Pre-Training (p. 21)
   - 4.1 Data Construction (p. 21)
   - 4.2 Hyper-Parameters (p. 22)
   - 4.3 Long Context Extension (p. 23)
   - 4.4 Evaluations (p. 24)
     - 4.4.1 Evaluation Benchmarks (p. 24)
     - 4.4.2 Evaluation Results (p. 24)
   - 4.5 Discussion (p. 26)
     - 4.5.1 Ablation Studies for Multi-Token Prediction (p. 26)
     - 4.5.2 Ablation Studies for the Auxiliary-Loss-Free Balancing Strategy (p. 26)
     - 4.5.3 Batch-Wise Load Balance VS. Sequence-Wise Load Balance (p. 27)
5. Post-Training (p. 28)
   - 5.1 Supervised Fine-Tuning (p. 28)
   - 5.2 Reinforcement Learning (p. 29)
     - 5.2.1 Reward Model (p. 29)
     - 5.2.2 Group Relative Policy Optimization (p. 30)
   - 5.3 Evaluations (p. 30)
     - 5.3.1 Evaluation Settings (p. 30)
     - 5.3.2 Standard Evaluation (p. 31)
     - 5.3.3 Open-Ended Evaluation (p. 33)
     - 5.3.4 DeepSeek-V3 as a Generative Reward Model (p. 33)
   - 5.4 Discussion (p. 34)
     - 5.4.1 Distillation from DeepSeek-R1 (p. 34)
     - 5.4.2 Self-Rewarding (p. 34)
     - 5.4.3 Multi-Token Prediction Evaluation (p. 35)
6. Conclusion, Limitations, and Future Directions (p. 35)
A. Contributions and Acknowledgments (p. 45–46) ✓ extracted
B. Ablation Studies for Low-Precision Training (p. 47–48) ✓ extracted
   - B.1 FP8 vs. BF16 Training (p. 47)
   - B.2 Discussion About Block-Wise Quantization (p. 47)
C. Expert Specialization Patterns of the 16B Aux-Loss-Based and Aux-Loss-Free Models (p. 48–51) ✓ extracted
