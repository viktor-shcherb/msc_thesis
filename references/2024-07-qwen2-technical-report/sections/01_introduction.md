# Introduction [p. 3]

## Context and Motivation

[p. 3] Following the emergence of ChatGPT (OpenAI, 2022), enthusiasm for large language models (LLMs) has escalated globally. The release of the Llama series (Touvron et al., 2023) further ignited interests in the open-source community, particularly regarding GPT-level local LLMs. Recently, Claude-3 Opus (Anthropic, 2024) and GPT-4o (omni) (OpenAI, 2024), the updated model for ChatGPT, have ascended to the pinnacle of the Chatbot Arena (Chiang et al., 2024). Llama-3 (AI@Meta, 2024) has emerged as the state-of-the-art open-weight model series, narrowing the performance gap with leading proprietary models and widely acknowledged as GPT-4-level. An increasing number of competitive LLMs are now pursuing advancements similar to those made by the GPT series from OpenAI, including Qwen (Bai et al., 2023a), Mistral (Jiang et al., 2023a), Gemma (Mesnard et al., 2024), etc., released in an open-weight manner.

## Qwen Series History

[p. 3] The authors have successively introduced the Qwen series (Bai et al., 2023a) and progressed to Qwen1.5 (Qwen Team, 2024a). They also unveiled the vision-language model Qwen-VL (Bai et al., 2023b) and launched the audio-language model Qwen-Audio (Chu et al., 2023). Qwen2 is the newest addition to the Qwen family of large language models and large multimodal models.

## Qwen2 Overview

[p. 3] Qwen2 is a series of LLMs grounded in the Transformer architecture (Vaswani et al., 2017), trained using next-token prediction. The model series encompasses:
- **Base language models** (foundational, pre-trained but unaligned to human preferences)
- **Instruction-tuned models** (fine-tuned with single-turn and multi-turn instruction-following datasets suitable for chat and agent purposes)

The release comprises:
- Four dense models with parameter counts of **0.5 billion, 1.5 billion, 7 billion, and 72 billion**
- A **Mixture-of-Experts (MoE) model with 57 billion parameters**, of which **14 billion are activated** for each token

The smaller models (Qwen2-0.5B and Qwen2-1.5B) are designed for easy deployment on portable devices such as smartphones, earphones, and smart glasses. The larger models cater to deployment across GPUs of varying scales.

## Pre-training Data

[p. 3] All models were pre-trained on a high-quality, large-scale dataset comprising **over 7 trillion tokens**, covering a wide range of domains and languages. Compared to previous editions of Qwen, Qwen2 includes a broader spectrum of linguistic data, enhancing the quantity and quality of code and mathematics content. This enrichment is hypothesized to improve reasoning abilities of LLMs.

## Post-training

[p. 3] All models underwent supervised fine-tuning and direct preference optimization (DPO, Rafailov et al., 2023), aligning them with human preferences through learning from human feedback.

## Key Results

[p. 3] Qwen2 outperforms competing models in evaluations of both fundamental language capabilities and instruction-tuned functionalities. Specifically:
- **Qwen2-72B-Instruct** (instruction-tuned variant):
  - 9.1 on MT-Bench (Zheng et al., 2023)
  - 48.1 on Arena-Hard (Chiang et al., 2024)
  - 35.7 on LiveCodeBench (Jain et al., 2024)
- **Qwen2-72B** (base language model):
  - 84.2 on MMLU (Hendrycks et al., 2021a)
  - 37.9 on GPQA (Rein et al., 2023)
  - 64.6 on HumanEval (Chen et al., 2021)
  - 89.5 on GSM8K (Cobbe et al., 2021)
  - 82.4 on BBH (Suzgun et al., 2023)
