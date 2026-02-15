# 1 Introduction [p. 2]

**Figure 1** (p. 1): "Kimi k1.5 long-CoT results."

Description: Bar chart showing performance comparison across multiple benchmarks (Math, Code, Vision)
- Key elements: 6 benchmark groups (AIME 2024, MATH 500, Codeforces, LiveCodeBench v5, MathVista, MMMU) with bars comparing Kimi k1.5 long-CoT (blue) against baselines including OpenAI o1 (light blue), OpenAI o1-mini (light gray), QVQ-72B-Preview (medium gray), and QwQ-32B-Preview (darker gray)
- Notable patterns:
  - AIME 2024 (Pass@1): Kimi k1.5 77.5, o1 74.4, o1-mini 63.6, QwQ 50
  - MATH 500 (EM): Kimi k1.5 96.2, o1 94.8, o1-mini 90, QwQ 90.6
  - Codeforces (Percentile): Kimi k1.5 94, o1 94, o1-mini 88, QwQ 62
  - LiveCodeBench v5 24.12-25.2 (Pass@1): Kimi k1.5 62.5, o1 67.2, o1-mini 53.1, QwQ 40.6
  - MathVista (Pass@1): Kimi k1.5 74.9, o1 71, o1-mini 71.4, QVQ 70
  - MMMU (Pass@1): o1 77.3, QVQ 70.3, Kimi k1.5 70.0
- Supports claim: Kimi k1.5 achieves state-of-the-art reasoning performance matching OpenAI's o1 across multiple benchmarks

**Figure 2** (p. 2): "Kimi k1.5 short-CoT results."

Description: Bar chart comparing short-CoT performance across Math, Code, Vision, and General domains
- Key elements: 8 benchmark groups with bars comparing Kimi k1.5 short-CoT (blue) against OpenAI 4o (light blue), Claude 3.5 Sonnet (light gray), Qwen2-VL (medium gray), LLaMA-3.1-405B-Inst. (gray), DeepSeek V3 (medium gray), and Qwen2.5-72B-Inst. (darker gray)
- Notable patterns:
  - Math section: AIME 2024 (Pass@1): Kimi k1.5 60.8, DeepSeek V3 39.2, Qwen2.5 72B 23.3, LLaMA-3.1 405B 23.3, Claude 3.5 Sonnet 16.0, GPT-4o 9.3; MATH-500 (EM): Kimi k1.5 94.6, DeepSeek V3 90.2, Qwen2.5 72B 80.0, Claude 3.5 Sonnet 78.3, GPT-4o 74.6, LLaMA-3.1 405B 73.8
  - Code section: LiveCodeBench v4 24.08-24.11 (Pass@1-CoT): Kimi k1.5 47.3, DeepSeek V3 40.5, Claude 3.5 Sonnet 36.3, GPT-4o 33.4, Qwen2.5 72B 31.1, LLaMA-3.1 405B 28.4
  - Vision section: MathVista_test (Pass@1): Kimi k1.5 70.1, Qwen2-VL 69.7, Claude 3.5 Sonnet 65.3, GPT-4o 63.8; MMMU_val (Pass@1): GPT-4o 69.1, Kimi k1.5 68.0, Claude 3.5 Sonnet 66.4, Qwen2-VL 64.5
  - General section: MMLU (EM): DeepSeek V3 88.5, LLaMA-3.1 405B 88.6, Claude 3.5 Sonnet 88.3, Kimi k1.5 87.4, GPT-4o 87.2, Qwen2.5 72B 85.3; IF-Eval (Prompt Strict): Kimi k1.5 87.2, Claude 3.5 Sonnet 86.5, DeepSeek V3 86.1, LLaMA-3.1 405B 86.0, Qwen2.5 72B 84.1, GPT-4o 84.3; CLUEWSC (EM): Kimi k1.5 91.7, Qwen2.5 72B 91.4, DeepSeek V3 90.9, GPT-4o 87.9, Claude 3.5 Sonnet 85.4, LLaMA-3.1 405B 84.7; C-Eval (EM): Kimi k1.5 88.3, DeepSeek V3 86.5, Qwen2.5 72B 86.1, Claude 3.5 Sonnet 76.7, GPT-4o 76.0, LLaMA-3.1 405B 61.5
- Supports claim: Kimi k1.5 short-CoT outperforms existing short-CoT models such as GPT-4o and Claude Sonnet 3.5 by a large margin (up to +550%)

## Main Content [p. 2]

Language model pretraining with next token prediction has been studied under the context of the scaling law, where proportionally scaling model parameters and data sizes leads to the continued improvement of intelligence (Kaplan et al. 2020; Hoffmann et al. 2022). However, this approach is limited to the amount of available high-quality training data (Villalobos et al. 2024; Muennighoff et al. 2023). In this report, we present the training recipe of Kimi k1.5, our latest multi-modal LLM trained with reinforcement learning (RL). The goal is to explore a possible new axis for continued scaling. Using RL with LLMs, the models learns to explore with rewards and thus is not limited to a pre-existing static dataset.

There are a few key ingredients about the design and training of k1.5.

- **Long context scaling**. We scale the context window of RL to 128k and observe continued improvement of performance with an increased context length. A key idea behind our approach is to use partial rollouts to improve training efficiency—i.e., sampling new trajectories by reusing a large chunk of previous trajectories, avoiding the cost to re-generate the new trajectories from scratch. Our observation identifies the context length as a key dimension of the continued scaling of RL with LLMs.

- **Improved policy optimization**. We derive a formulation of RL with long-CoT and employ a variant of online mirror descent for robust policy optimization. This algorithm is further improved by our effective sampling strategy, length penalty, and optimization of the data recipe.

- **Simplistic Framework**. Long context scaling, combined with the improved policy optimization methods, establishes a simplistic RL framework for learning with LLMs. Since we are able to scale the context length, the learned CoTs exhibit the properties of planning, reflection, and correction. An increased context length has an effect of increasing the number of search steps. As a result, we show that strong performance can be achieved without relying on more complex techniques such as Monte Carlo tree search, value functions, and process reward models.

- **Multimodalities**. Our model is jointly trained on text and vision data, which has the capabilities of jointly reasoning over the two modalities.

Moreover, we present effective long2short methods that use long-CoT techniques to improve short-CoT models. Specifically, our approaches include applying length penalty with long-CoT activations and model merging.

Our long-CoT version achieves state-of-the-art reasoning performance across multiple benchmarks and modalities—e.g., 77.5 on AIME, 96.2 on MATH 500, 94-th percentile on Codeforces, 74.9 on MathVista—matching OpenAI's o1. Our model also achieves state-of-the-art short-CoT reasoning results—e.g., 60.8 on AIME, 94.6 on MATH500, 47.3 on LiveCodeBench—outperforming existing short-CoT models such as GPT-4o and Claude Sonnet 3.5 by a large margin (up to +550%). Results are shown in Figures 1 and 2.
