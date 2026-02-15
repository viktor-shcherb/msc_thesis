# Overview

**Title:** KIMI K1.5: SCALING REINFORCEMENT LEARNING WITH LLMS

**Subtitle:** Technical Report of Kimi k1.5

**Authors:** Kimi Team

**Affiliations:** Not specified on title page

**Venue:** arXiv:2501.12599v4 [cs.AI]

**Date:** 3 Jun 2025

## Abstract

> Language model pretraining with next token prediction has proved effective for scaling compute but is limited to the amount of available training data. Scaling reinforcement learning (RL) unlocks a new axis for the continued improvement of artificial intelligence, with the promise that large language models (LLMs) can scale their training data by learning to explore with rewards. However, prior published work has not produced competitive results. In light of this, we report on the training practice of Kimi k1.5, our latest multi-modal LLM trained with RL, including its RL training techniques, multi-modal data recipes, and infrastructure optimization. Long context scaling and improved policy optimization methods are key ingredients of our approach, which establishes a simplistic, effective RL framework without relying on more complex techniques such as Monte Carlo tree search, value functions, and process reward models. Notably, our system achieves state-of-the-art reasoning performance across multiple benchmarks and modalities—e.g., 77.5 on AIME, 96.2 on MATH 500, 94-th percentile on Codeforces, 74.9 on MathVista—matching OpenAI's o1. Moreover, we present effective long2short methods that use long-CoT techniques to improve short-CoT models, yielding state-of-the-art short-CoT reasoning results—e.g., 60.8 on AIME, 94.6 on MATH500, 47.3 on LiveCodeBench—outperforming existing short-CoT models such as GPT-4o and Claude Sonnet 3.5 by a large margin (up to +550%).

## Section Headings

- Abstract (p. 1)
- 1 Introduction (p. 2)
- 2 Approach: Reinforcement Learning with LLMs (p. 3)
  - 2.1 RL Prompt Set Curation (p. 3)
  - 2.2 Long-CoT Supervised Fine-Tuning (p. 3)
  - 2.3 Reinforcement Learning (p. 4)
    - 2.3.1 Problem Setting (p. 4)
    - 2.3.2 Policy Optimization (p. 5)
    - 2.3.3 Length Penalty (p. 5)
    - 2.3.4 Sampling Strategies (p. 6)
    - 2.3.5 More Details on Training Recipe (p. 6)
  - 2.4 Long2short: Context Compression for Short-CoT Models (p. 7)
  - 2.5 Other Training Details (p. 8)
    - 2.5.1 Pretraining (p. 8)
    - 2.5.2 Vanilla Supervised Finetuning (p. 8)
  - 2.6 RL Infrastructure (p. 8)
    - 2.6.1 Large Scale Reinforcement Learning Training System for LLM (p. 9)
    - 2.6.2 Partial Rollouts for Long CoT RL (p. 9)
    - 2.6.3 Hybrid Deployment of Training and Inference (p. 9)
    - 2.6.4 Code Sandbox (p. 11)
- 3 Experiments (p. 11)
  - 3.1 Evaluation (p. 11)
  - 3.2 Main Results (p. 12)
  - 3.3 Long Context Scaling (p. 12)
  - 3.4 Long2short (p. 13)
  - 3.5 Ablation Studies (p. 14)
- 4 Conclusions (p. 15)
- References (p. 16)
- Appendix (p. 20)
  - A Contributions (p. 20)
  - B Pretraining (p. 21)
    - B.1 Language Data (p. 21)
    - B.2 Multimodal Data (p. 22)
    - B.3 Model Architecture (p. 23)
    - B.4 Training Stages (p. 23)
  - C Evaluation Details (p. 24)
    - C.1 Text Benchmark (p. 24)
    - C.2 Reasoning Benchmark (p. 25)
    - C.3 Image Benchmark (p. 25)
