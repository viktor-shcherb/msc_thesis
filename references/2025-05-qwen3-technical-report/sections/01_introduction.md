# Introduction [p. 2]

## Background and Motivation

The pursuit of artificial general intelligence (AGI) or artificial super intelligence (ASI) has long been a goal for humanity. Recent advancements in large foundation models include GPT-4o (OpenAI, 2024), Claude 3.7 (Anthropic, 2025), Gemini 2.5 (DeepMind, 2025), DeepSeek-V3 (Liu et al., 2024a), Llama-4 (Meta-AI, 2025), and Qwen2.5 (Yang et al., 2024b), which have demonstrated progress toward this objective. These models are trained on vast datasets spanning trillions of tokens across diverse domains and tasks, effectively distilling human knowledge and capabilities into their parameters [p. 2].

Recent developments in reasoning models, optimized through reinforcement learning, highlight the potential for foundation models to enhance reasoning and achieve higher levels of intelligence, e.g., o3 (OpenAI, 2025), DeepSeek-R1 (Guo et al., 2025). While most state-of-the-art models remain proprietary, the rapid growth of open-source communities has substantially reduced the performance gap between open-weight and closed-source models. A number of top-tier models (Meta-AI, 2025; Liu et al., 2024a; Guo et al., 2025; Yang et al., 2024b) are now being released as open-source, fostering broader research and innovation in artificial intelligence [p. 2].

## Qwen3 Overview

In this work, the authors introduce Qwen3, the latest series in their foundation model family, Qwen. Qwen3 is a collection of open-weight large language models (LLMs) that achieve state-of-the-art performance across a wide variety of tasks. The series includes both dense models and Mixture-of-Experts (MoE) models, with the number of parameters ranging from 0.6 billion to 235 billion, to meet the needs of different downstream applications [p. 2].

Notably, the largest model, Qwen3-235B-A22B, is an MoE model with a total of 235 billion parameters and 22 billion activated ones per token. This design ensures both high performance and efficient inference [p. 2].

## Key Innovations

### Unified Thinking and Non-Thinking Modes

Qwen3 introduces several key advancements to enhance its functionality and usability. First, it integrates two distinct operating modes, thinking mode and non-thinking mode, into a single model. This allows users to toggle between fast inference and longer-form reasoning without alternating between different models, e.g., switching from Qwen2.5 to QwQ (Qwen Team, 2024). This flexibility ensures that developers and users can adapt the model's behavior to suit specific efficiency goals [p. 2].

Additionally, Qwen3 incorporates a thinking budget mechanism, providing users with fine-grained control over the level of reasoning effort applied by the model during task execution. This capability is crucial to the optimization of computational resources and performance, tailoring the model's thinking behavior to meet varying complexity in real-world applications [p. 2].

### Enhanced Multilingual Capabilities

Furthermore, Qwen3 has been pre-trained on a much broader set of 119 languages and dialects, effectively enhancing its multilingual capabilities. This broadened language support amplifies its potential for deployment in global use cases and international applications [p. 2].

These advancements together establish Qwen3 as a cutting-edge open-source large language model family, capable of effectively addressing complex tasks across various domains and languages [p. 2].

## Pre-training Data

The pre-training process for Qwen3 utilizes a large-scale dataset consisting of approximately 36 trillion tokens, curated to ensure linguistic and domain diversity. To efficiently expand the training data, they employ a multi-modal approach: Qwen2.5-VL (Bai et al., 2025) is finetuned to extract text from extensive PDF documents. They also leverage domain-specific models: Qwen2.5-Math (Yang et al., 2024c) for mathematical content and Qwen2.5-Coder (Hui et al., 2024) for code-related data [p. 2].

The pre-training process follows a three-stage strategy. In the first stage, the model is trained on about 30 trillion tokens to build a strong foundation of general knowledge. In the second stage, it is further trained on knowledge-intensive data in reasoning abilities in areas like science, technology, engineering, and mathematics (STEM) and coding. Finally, in the third stage, the model is trained on long-context data to increase its maximum context length from 4,096 to 32,768 tokens [p. 2].

## Post-Training Approach

To better align foundation models with human preferences and downstream applications, they employ a multi-stage post-training approach that empowers both thinking (reasoning) and non-thinking modes. In the first two stages, they focus on developing strong reasoning abilities through long chain-of-thought (CoT) cold-start finetuning and reinforcement learning focusing on mathematics and coding tasks. In the final two stages, they combine data with and without reasoning paths into a unified dataset for further fine-tuning, enabling the model to handle both types of input effectively, and then apply general-domain reinforcement learning to improve performance across a wide range of downstream tasks [p. 2-3].

For smaller models, they use strong-to-weak distillation, leveraging both off-policy and on-policy knowledge transfer from larger models to enhance their capabilities. Distillation from advanced teacher models significantly outperforms conventional learning in performance and training efficiency [p. 3].

## Evaluation Results

They evaluate both pre-trained and post-trained versions of their models across a comprehensive set of benchmarks spanning multiple tasks and domains. Experimental results show that their base pre-trained models achieve state-of-the-art performance. The post-trained models, whether in thinking or non-thinking mode, perform competitively against leading proprietary models and large mixture-of-experts (MoE) models such as o1, o3-mini, and DeepSeek-V3 [p. 3].

Notably, their models excel in coding, mathematics, and agent-related tasks. For example, the flagship model Qwen3-235B-A22B achieves 85.7 on AIME 24 and 81.5 on AIME'25 (AIME, 2025), 70.7 on LiveCodeBench v5 (Jain et al., 2024), 2,056 on CodeForces, and 70.8 on BFCL v3 (Yan et al., 2024) [p. 2-3].

In addition, other models in the Qwen3 series also show strong performance relative to their size. Furthermore, they observe that increasing the thinking budget for thinking tokens leads to a consistent improvement in the model's performance across various tasks [p. 3].

## Report Structure

In the following sections, they describe the design of the model architecture, provide details on its training procedures, present experimental evaluations of pre-trained and post-trained models, and finally conclude this technical report by summarizing the key findings and outlining potential directions for future research [p. 3].
