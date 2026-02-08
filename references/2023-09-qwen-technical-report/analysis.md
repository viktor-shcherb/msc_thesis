---
title: "Qwen Technical Report"
authors: "Bai, Bai, Chu, Cui, Dang, Deng, Fan, Ge, Han, Huang, Hui, Ji, Li, Lin, Lin, Liu, Liu, Lu, Lu, Ma, Men, Ren, Ren, Tan, Tan, Tu, Wang, Wang, Wang, Wu, Xu, Xu, Yang, Yang, Yang, Yang, Yao, Yu, Yuan, Yuan, Zhang, Zhang, Zhang, Zhang, Zhou, Zhou, Zhou, Zhu"
year: 2023
venue: "arXiv preprint"
paper_type: preprint
categories: ["model-release", "architecture", "position-encoding", "context-extension"]
scope: ["bilingual LLM (English/Chinese)", "open-source foundation models", "1.8B-14B parameter range"]
benchmarks_used: ["mmlu", "c-eval", "gsm8k", "math-hendrycks", "humaneval", "mbpp", "bbh", "hellaswag", "piqa", "arc", "cmmlu", "agi-eval", "gaokao-bench", "boolq", "csqa", "natural-questions", "lambada", "siqa"]
models_introduced: ["qwen-1.8b", "qwen-7b", "qwen-14b", "code-qwen-7b", "code-qwen-14b"]
models_evaluated: ["llama-7b", "llama-13b", "llama-2-7b", "llama-2-13b", "llama-2-70b", "gpt-3.5-turbo", "gpt-4", "mpt-7b", "falcon-7b"]
key_claims:
  - id: C1
    claim: "Qwen-14B outperforms all previous 13B-class open-source base models on all 7 evaluated benchmarks (MMLU, C-Eval, GSM8K, MATH, HumanEval, MBPP, BBH)"
    evidence: "Table 2, Section 2.6"
    status: supported
    scope: "base models only, 7 benchmarks, 5-shot/8-shot/4-shot/0-shot/3-shot settings"
    magnitude: "66.3 MMLU, 72.1 C-Eval, 61.3 GSM8K, 24.8 MATH, 32.3 HumanEval, 40.8 MBPP, 53.4 BBH"
  - id: C2
    claim: "Combining dynamic NTK-aware interpolation, LogN-Scaling, and layer-wise window attention maintains low perplexity at extended context lengths without fine-tuning"
    evidence: "Table 3, Section 2.5"
    status: supported
    scope: "Qwen-7B and Qwen-14B, arXiv test data, context lengths up to 16384 tokens"
    magnitude: "Qwen-7B perplexity 4.32 at 16K (vs. 2645.09 without techniques); Qwen-14B perplexity 3.42 at 16K"
  - id: C3
    claim: "RLHF significantly outperforms SFT models in human evaluation, approaching but not matching GPT-4"
    evidence: "Figure 4, Section 3.3"
    status: supported
    scope: "300 Chinese instructions, 5 categories (knowledge, language understanding, creative writing, math, coding)"
    magnitude: "RLHF win rate ~34.4% vs GPT-3.5 (vs ~32.3% for SFT-14B); GPT-4 win rate ~54.0% vs GPT-3.5"
  - id: C4
    claim: "Qwen-Chat achieves 98% tool selection accuracy on ReAct prompting benchmark, surpassing GPT-4 (95%) and GPT-3.5 (85%)"
    evidence: "Table 6, Section 3.4"
    status: supported
    scope: "Chinese language ReAct benchmark, up to 5 candidate plugins, 7B and 14B model sizes"
    magnitude: "98% accuracy (7B and 14B), 93 Rouge-L (14B), 2.4% false positive rate (14B) vs GPT-4 95%/90/15.0%"
  - id: C5
    claim: "Adding bias to QKV attention layers enhances length extrapolation ability"
    evidence: "Section 2.3, citing Su (2023b)"
    status: unvalidated
    scope: "RoPE-based Transformers"
    magnitude: "qualitative"
  - id: C6
    claim: "Code-Qwen-14B-Chat achieves 66.4% pass@1 on HumanEval and 51.9% average on HumanEvalPack, leading open-source models in its parameter class"
    evidence: "Tables 10-11, Section 4.3"
    status: supported
    scope: "HumanEval Python code generation and HumanEvalPack 6-language synthesize, pass@1"
    magnitude: "66.4% HumanEval (vs Code-Llama-Python-34B 53.7%), 51.9% HumanEvalPack avg (vs WizardCoder-15B 40.5%)"
  - id: C7
    claim: "Math-Qwen-14B-Chat outperforms all open-source math-specialized models of similar size and exceeds Minerva-62B on MATH"
    evidence: "Table 12, Section 5.2"
    status: supported
    scope: "GSM8K, MATH, Math401, Math23K benchmarks, greedy decoding"
    magnitude: "69.8% GSM8K, 24.2% MATH, 85.0% Math401, 78.4% Math23K (vs WizardMath-13B 63.9%/14.0%, Minerva-62B 52.4%/27.6%)"
cross_references:
  - target: 2023-02-llama-open-efficient-foundation
    type: extends
    detail: "Qwen architecture builds on LLaMA with modifications including untied embeddings, QKV bias, and SwiGLU activation"
  - target: 2023-07-llama-2-open-foundation-chat
    type: concurrent
    detail: "Released concurrently; Qwen compares against Llama 2 throughout as primary baseline"
  - target: 2024-07-qwen2-technical-report
    type: extended-by
    detail: "Qwen2 succeeds Qwen with expanded model sizes and improved performance"
open_questions:
  - question: "What is the optimal balance between pretrained gradient coefficient and PPO data for mitigating alignment tax?"
    addressed_by: null
  - question: "How do layer-wise window sizes affect context modeling at different depths, and what is the optimal assignment strategy?"
    addressed_by: null
  - question: "How do continued pretraining data requirements for code/math specialization scale with base model size?"
    addressed_by: null
---

# Qwen Technical Report

**Authors:** Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, Tianhang Zhu (Qwen Team, Alibaba Group)
**Date:** September 2023, arXiv:2309.16609

---

## Core Research Problem

Despite advances in large language models, the community faces persistent challenges with **reproducibility, steerability, and accessibility** of strong models (Section 1). Proprietary models like GPT-4 demonstrate impressive capabilities across language understanding, code generation, and mathematical reasoning, but open-source alternatives have limitations:

1. **Weak multilingual support** -- prior open-source efforts (LLaMA, Llama 2) lacked native optimization for Chinese, limiting bilingual applications.
2. **Fixed context windows** -- base models trained on short context lengths (typically 2048 tokens) cannot handle longer inputs without quality degradation.
3. **No specialized domain variants** -- open-source model families typically lack coding- and math-specific variants that can compete with proprietary models.

The core challenge: **how to build a comprehensive, competitive open-source LLM family with strong bilingual (English/Chinese) capabilities, effective context extension, specialized domain variants for coding and mathematics, and alignment with human preferences**.

---

## Problem Solutions

The paper introduces **Qwen** (Qianwen, meaning "thousands of prompts" in Chinese), a family of large language models addressing these gaps through:

1. **Modified Transformer architecture** building on LLaMA with targeted improvements: untied embeddings, QKV bias for extrapolation, FP32 RoPE inverse frequencies, SwiGLU activation (Section 2.3).
2. **Large bilingual tokenizer** with ~152K vocabulary built on tiktoken cl100k_base, augmented for Chinese and other languages (Section 2.2).
3. **Training-free context extension** combining dynamic NTK-aware interpolation, LogN-Scaling, and layer-wise window attention for inference-time length extension (Section 2.5).
4. **Comprehensive alignment pipeline** using SFT with ChatML format followed by RLHF with PPO, including preference model pretraining (Section 3).
5. **Specialized domain models**: Code-Qwen (continued code pretraining + multi-stage SFT) and Math-Qwen-Chat (math SFT) variants (Sections 4--5).

---

## Approach Details

### Method

#### Architecture

Qwen adopts a modified Transformer architecture based on LLaMA (Touvron et al., 2023a) with the following design choices (Section 2.3):

| Component | Design Choice | Rationale |
|-----------|--------------|-----------|
| Embedding | Untied input/output projection | Better performance at cost of memory |
| Position encoding | RoPE with FP32 inverse frequency | Higher accuracy than BF16/FP16 |
| Bias | QKV attention layers only (Su, 2023b) | Enhances length extrapolation ability |
| Normalization | Pre-Norm with RMSNorm (Jiang et al., 2023) | Training stability + efficiency |
| Activation | SwiGLU (Shazeer, 2020) | Outperforms GeLU in experiments |
| FFN dimension | 8/3 x hidden size | Standard practice with GLU variants |

**Model configurations (Table 1):**

| Parameters | Hidden Size | Heads | Layers | Learning Rate | Batch Size | Training Tokens |
|------------|-------------|-------|--------|---------------|------------|-----------------|
| 1.8B | 2048 | 16 | 24 | 3.0 x 10^-4 | 4M | 2.2T |
| 7B | 4096 | 32 | 32 | 3.0 x 10^-4 | 4M | 2.4T |
| 14B | 5120 | 40 | 40 | 3.0 x 10^-4 | 4M | 3.0T |

#### Tokenization

Qwen uses BPE tokenization based on tiktoken cl100k_base (Jain, 2022), augmented with commonly used Chinese characters and words, other language tokens, and single-digit number splitting (following LLaMA). Final vocabulary size: **~152K tokens** (Section 2.2).

The tokenizer achieves higher compression efficiency than LLaMA, Baichuan, ChatGLM2, and InternLM across most languages (Figure 3), implying lower inference serving costs per equivalent information content.

#### Pretraining Data

Up to **3 trillion tokens** from diverse sources (Section 2.1):
- Public web documents with HTML text extraction and language identification
- Encyclopedia, books, code (multilingual with English and Chinese emphasis)
- High-quality instruction data mixed into pretraining

**Data quality pipeline:**
1. Exact-match deduplication after normalization + fuzzy deduplication via MinHash/LSH
2. Rule-based and ML-based quality filtering (language models, text-quality scorers, offensive content detectors)
3. Selective up-sampling of high-quality sources
4. 13-gram overlap filtering against benchmark test sets for decontamination (following Brown et al., 2020)

#### Context Length Extension

Qwen implements **training-free** techniques applied solely during inference (Section 2.5):

1. **NTK-aware interpolation** (bloc97, 2023): Adjusts RoPE base frequency to preserve high-frequency information without fine-tuning, unlike position interpolation (Chen et al., 2023a) which scales all dimensions equally.

2. **Dynamic NTK-aware interpolation**: Changes scale dynamically by chunks to avoid severe performance degradation (later formalized in Peng et al., 2023a / YaRN).

3. **LogN-Scaling** (Chiang & Cholak, 2022; Su, 2023a): Rescales the dot product of query and value by a factor dependent on the ratio of context length to training length, stabilizing attention entropy as context grows.

4. **Layer-wise window attention** (building on Beltagy et al., 2020): Assigns shorter windows to lower layers and longer windows to higher layers, based on the observation that **lower layers are more sensitive to context length extension** compared to higher layers.

### Key Technical Components

**Training configuration** (Section 2.4):
- Context length: 2048 tokens
- Documents shuffled, merged, and truncated to context length
- Flash Attention (Dao et al., 2022) for efficiency
- Optimizer: AdamW (beta_1=0.9, beta_2=0.95, epsilon=10^-8)
- Learning rate: cosine schedule, peak per Table 1, decayed to 10% of peak
- BFloat16 mixed precision

**SFT configuration** (Section 3.1.2):
- ChatML format with `<|im_start|>` and `<|im_end|>` special tokens
- Loss masks on system and user inputs
- Sequence length: 2048, batch size: 128, total steps: 4000
- Peak learning rate: 2 x 10^-6 (warmup over 1430 steps)
- Weight decay: 0.1, dropout: 0.1, gradient clipping: 1.0

**RLHF configuration** (Section 3.2):
- Reward model: same-sized pretrained Qwen + pooling layer, trained with preference model pretraining (PMP) on large comparison dataset then fine-tuned on diverse prompts (~6600 tags for sampling)
- Reward model training: learning rate 3 x 10^-6, batch size 64, 1 epoch
- PPO: 50-step value model warmup before policy updates; 2 responses sampled per query
- KL divergence coefficient: 0.04, policy LR: 1 x 10^-6, value LR: 5 x 10^-6
- Value loss clipping: 0.15, top-p: 0.9
- Pretrained gradient to mitigate alignment tax (significantly larger volume of pretrained data vs PPO data)

**Code-Qwen** (Section 4):
- Continued pretraining on ~90B code tokens, context length extended to 8192
- Learning rate: 6.0 x 10^-5 (14B) / 3.0 x 10^-5 (7B), 3% warmup, no decay
- Multi-stage SFT for chat variants; Code-Qwen-Chat SFT LR: 2.0 x 10^-6 (14B) / 1.0 x 10^-5 (7B)

**Math-Qwen-Chat** (Section 5):
- Math SFT on augmented instruction dataset, sequence length 1024
- Loss masks on system/user inputs
- Peak LR: 2 x 10^-5, 50K training steps

### Experimental Setup

**Base model evaluation** (Section 2.6): Compared against LLaMA (7B-65B), Llama 2 (7B-70B), MPT (7B/30B), Falcon (7B/40B), ChatGLM2-6B, InternLM (7B/20B), Baichuan2 (7B/13B), XVERSE-13B, StableBeluga2-70B on 7 benchmarks:
- MMLU (5-shot), C-Eval (5-shot), GSM8K (8-shot), MATH (4-shot), HumanEval (0-shot), MBPP (3-shot), BBH (3-shot)
- Baseline scores collected from official results and OpenCompass (OpenCompass Team, 2023)

**Chat model evaluation** (Section 3.3): Compared Qwen-Chat (1.8B/7B/14B) against GPT-3.5, GPT-4, ChatGLM2-6B, InternLM-Chat-7B, Baichuan2-Chat (7B/13B), Llama 2-Chat (7B/13B/70B) on MMLU, C-Eval, GSM8K, HumanEval, BBH in both zero-shot and few-shot settings.

**Human evaluation** (Section 3.3): 300 Chinese instructions across knowledge, language understanding, creative writing, coding, and mathematics. Three annotators ranked model responses. Models: Qwen-7B-Chat (SFT), Qwen-14B-Chat (SFT), Qwen-14B-Chat (RLHF), GPT-3.5, GPT-4.

**Tool use evaluation** (Section 3.4): In-house Chinese ReAct benchmark with up to 5 candidate plugins; code interpreter benchmark covering math problem-solving, data visualization, and general tasks; Hugging Face Agent benchmark.

**Code evaluation** (Section 4.3): HumanEval, MBPP (pass@1), HumanEvalPack (synthesize, 6 languages).

**Math evaluation** (Section 5.2): GSM8K, MATH (Lightman et al., 2023 test set), Math401, Math23K. Greedy decoding.

**Reproducibility:** Code and model weights released on GitHub and Hugging Face for 7B and 14B models. No seeds reported. Pretraining data composition not fully specified. Single-run results throughout; no variance estimates reported (limited evidence for reproducibility).

### Key Results

**Base model evaluation (Table 2):**

| Model | Params | MMLU 5-shot | C-Eval 5-shot | GSM8K 8-shot | MATH 4-shot | HumanEval 0-shot | MBPP 3-shot | BBH 3-shot |
|---|---|---|---|---|---|---|---|---|
| MPT | 7B | 30.8 | 23.5 | 9.1 | 3.0 | 18.3 | 22.8 | 35.6 |
| MPT | 30B | 47.9 | - | 15.2 | 3.1 | 25.0 | 32.8 | 38.0 |
| Falcon | 7B | 27.8 | - | 6.8 | 2.3 | - | 11.2 | 28.0 |
| Falcon | 40B | 57.0 | - | 19.6 | 5.5 | - | 29.8 | 37.1 |
| ChatGLM2 | 6B | 47.9 | 51.7 | 32.4 | 6.5 | - | - | 33.7 |
| InternLM | 7B | 51.0 | 53.4 | 31.2 | 6.3 | 10.4 | 14.0 | 37.0 |
| InternLM | 20B | 62.1 | 58.8 | 52.6 | 7.9 | 25.6 | 35.6 | 52.5 |
| Baichuan2 | 7B | 54.7 | 56.3 | 24.6 | 5.6 | 18.3 | 24.2 | 41.6 |
| Baichuan2 | 13B | 59.5 | 59.0 | 52.8 | 10.1 | 17.1 | 30.2 | 49.0 |
| LLaMA | 7B | 35.6 | 27.3 | 11.0 | 2.9 | 12.8 | 17.7 | 33.5 |
| LLaMA | 13B | 47.7 | 31.8 | 20.3 | 4.2 | 15.8 | 22.0 | 37.9 |
| LLaMA | 33B | 58.7 | 37.5 | 42.3 | 7.1 | 21.7 | 30.2 | 50.0 |
| LLaMA | 65B | 63.7 | 40.4 | 54.4 | 10.6 | 23.7 | 37.7 | 58.4 |
| Llama 2 | 7B | 46.8 | 32.5 | 16.7 | 3.3 | 12.8 | 20.8 | 38.2 |
| Llama 2 | 13B | 55.0 | 41.4 | 29.6 | 5.0 | 18.9 | 30.3 | 45.6 |
| Llama 2 | 34B | 62.6 | - | 42.2 | 6.2 | 22.6 | 33.0 | 44.1 |
| Llama 2 | 70B | 69.8 | 50.1 | 63.3 | 13.5 | 29.9 | 45.0 | 64.9 |
| StableBeluga2 | 70B | 68.6 | 51.4 | 69.6 | 14.6 | 28.0 | 11.4 | 69.3 |
| **Qwen** | **1.8B** | 44.6 | 54.7 | 21.2 | 5.6 | 17.1 | 14.8 | 28.2 |
| **Qwen** | **7B** | 58.2 | 63.5 | 51.7 | 11.6 | 29.9 | 31.6 | 45.0 |
| **Qwen** | **14B** | **66.3** | **72.1** | **61.3** | **24.8** | **32.3** | **40.8** | **53.4** |

- Qwen-14B outperforms all previous 13B-class open-source models on all 7 benchmarks (tested against 12 open-source model variants -- strong evidence for the claim within this comparison set).
- Qwen-14B outperforms Llama 2-70B on 3 of 7 benchmarks (C-Eval: 72.1 vs 50.1, MATH: 24.8 vs 13.5, HumanEval: 32.3 vs 29.9) despite being 5x smaller.
- Qwen-7B outperforms Llama 2-13B on all 7 benchmarks and is competitive with Baichuan2-13B.

**Context extension (Table 3, arXiv test data):**

| Model | 1024 | 2048 | 4096 | 8192 | 16384 |
|---|---|---|---|---|---|
| Qwen-7B (base) | 4.23 | 3.78 | 39.35 | 469.81 | 2645.09 |
| + dynamic_ntk | 4.23 | 3.78 | 3.59 | 3.66 | 5.71 |
| + dynamic_ntk + logn | 4.23 | 3.78 | 3.58 | 3.56 | 4.62 |
| + dynamic_ntk + logn + window_attn | 4.23 | 3.78 | 3.58 | 3.49 | 4.32 |
| Qwen-14B (base) | - | 3.46 | 22.79 | 334.65 | 3168.35 |
| + dynamic_ntk + logn + window_attn | - | 3.46 | 3.29 | 3.18 | 3.42 |

Each technique contributes incrementally: dynamic NTK reduces 16K perplexity from 2645 to 5.71; adding LogN further reduces to 4.62; adding window attention reaches 4.32 (ablation across 3 techniques on a single model -- moderate evidence).

**Aligned model evaluation (Table 5):**

| Model | Params | MMLU 0/5-shot | C-Eval 0/5-shot | GSM8K 0/8-shot | HumanEval 0-shot | BBH 0/3-shot |
|---|---|---|---|---|---|---|
| GPT-4 | - | -/83.0 | -/69.9 | -/91.4 | 86.6 | -/86.7 |
| GPT-3.5 | - | -/69.1 | -/52.5 | -/78.2 | 73.2 | -/70.1 |
| Llama 2-Chat | 70B | -/63.8 | -/44.3 | -/59.3 | 32.3 | -/60.8 |
| Qwen-Chat | 14B | 64.6/66.5 | 69.8/71.7 | 60.1/59.3 | 43.9 | 46.9/58.7 |
| Qwen-Chat | 7B | 55.8/57.0 | 59.7/59.3 | 50.3/54.1 | 37.2 | 39.6/46.7 |

Qwen-14B-Chat outperforms all open-source models except Llama 2-Chat-70B (which it still beats on C-Eval and HumanEval) (Table 5).

**Reward model accuracy (Table 4):**

| Dataset | Qwen Helpful-base | Qwen Helpful-online | Anthropic Helpful-base | Anthropic Helpful-online | OpenAI Summ. | Stanford SHP | OpenAI PRM800K |
|---|---|---|---|---|---|---|---|
| PMP | 62.68 | 61.62 | 76.52 | 65.43 | 69.60 | 60.05 | 70.59 |
| RM | 74.78 | 69.71 | 73.98 | 64.57 | 69.99 | 60.10 | 70.52 |

The PMP model generalizes well on out-of-distribution data; the reward model shows significant improvement on Qwen-specific datasets after fine-tuning (Section 3.2.1).

**Tool use via ReAct prompting (Table 6):**

| Model | Params | Tool Selection (Acc.) | Tool Input (Rouge-L) | False Positive (%) |
|---|---|---|---|---|
| GPT-4 | - | 95 | 90 | 15.0 |
| GPT-3.5 | - | 85 | 88 | 75.0 |
| Qwen-Chat | 1.8B | 92 | 89 | 19.3 |
| Qwen-Chat | 7B | 98 | 91 | 7.3 |
| Qwen-Chat | 14B | **98** | **93** | **2.4** |

GPT-3.5's poor performance is attributed to the Chinese-language focus of the benchmark (Section 3.4). The authors note the benchmark may be "relatively easy" and require enhancement.

**Code interpreter executability (Table 7):**

| Model | Params | Math (%) | Visualization (%) | General (%) | All (%) |
|---|---|---|---|---|---|
| GPT-4 | - | 91.9 | 85.9 | 82.8 | 86.8 |
| GPT-3.5 | - | 89.2 | 65.0 | 74.1 | 72.9 |
| Code Llama-Instruct | 13B | 93.2 | 55.8 | 74.1 | 68.8 |
| Qwen-Chat | 7B | 82.4 | 64.4 | 67.2 | 70.2 |
| Qwen-Chat | 14B | 89.2 | 84.1 | 65.5 | 81.7 |

**Code interpreter correctness (Table 8):**

| Model | Params | Math (%) | Vis.-Hard (%) | Vis.-Easy (%) | Vis.-All (%) |
|---|---|---|---|---|---|
| GPT-4 | - | 82.8 | 66.7 | 60.8 | 63.8 |
| GPT-3.5 | - | 47.3 | 33.3 | 55.7 | 44.2 |
| Code Llama-Instruct | 13B | 28.2 | 27.4 | 62.0 | 44.2 |
| Qwen-Chat | 7B | 41.9 | 40.5 | 54.4 | 47.2 |
| Qwen-Chat | 14B | 58.4 | 53.6 | 59.5 | 56.4 |

Qwen-14B-Chat surpasses all open-source alternatives on code interpreter tasks despite being a generalist model. Code Llama excels on easy visualization but fails on hard tasks requiring multi-step planning (Figure 5, Section A.3).

**Hugging Face Agent benchmark (Table 9):**

| Task | Model | Params | Tool Selection | Tool Used | Code Correctness |
|---|---|---|---|---|---|
| Run Mode | GPT-4 | - | 100 | 100 | 97.4 |
| Run Mode | GPT-3.5 | - | 95.4 | 96.3 | 87.0 |
| Run Mode | Qwen-Chat | 14B | 93.5 | 94.4 | 87.0 |
| Chat Mode | GPT-4 | - | 97.9 | 97.9 | 98.5 |
| Chat Mode | GPT-3.5 | - | 97.3 | 96.8 | 89.6 |
| Chat Mode | Qwen-Chat | 14B | 97.9 | 97.9 | 95.5 |

Qwen-14B-Chat matches GPT-3.5 on Run Mode code correctness and approaches GPT-4 on Chat Mode.

**Code generation -- HumanEval and MBPP (Table 10, selected rows):**

| Model | Params | HumanEval | MBPP |
|---|---|---|---|
| GPT-4 | - | 86.6 | - |
| GPT-3.5 | - | 73.2 | - |
| WizardCoder-Python | 34B | 73.2 | 61.2 |
| Unnatural Code Llama | 34B | 62.2 | 61.2 |
| Code Llama-Python | 34B | 53.7 | 56.2 |
| Code-Qwen-Chat | 14B | **66.4** | 52.4 |
| Code-Qwen | 14B | 45.1 | 51.4 |

**Code generation -- HumanEvalPack multilingual (Table 11, selected rows):**

| Model | Params | Python | JavaScript | Java | Go | C++ | Rust | Avg. |
|---|---|---|---|---|---|---|---|---|
| GPT-4 | - | 86.6 | 82.9 | 81.7 | 72.6 | 78.7 | 67.1 | 78.3 |
| WizardCoder | 15B | 59.8 | 49.5 | 36.1 | 36.4 | 40.9 | 20.2 | 40.5 |
| Code-Qwen-Chat | 14B | **66.4** | **58.5** | **56.1** | **47.6** | **54.2** | **28.7** | **51.9** |
| Code-Qwen | 14B | 45.1 | 51.8 | 57.3 | 39.6 | 18.2 | 20.7 | 38.8 |

Code-Qwen-Chat-14B achieves the highest average among open-source models on HumanEvalPack (51.9% vs WizardCoder-15B 40.5%), substantially outperforming across all 6 languages (tested on 6 programming languages -- moderate evidence for multilingual code capability).

**Math reasoning (Table 12):**

| Model | Params | GSM8K | MATH | Math401 | Math23K |
|---|---|---|---|---|---|
| GPT-4 | - | 92.0 | 42.5 | 83.5 | 74.0 |
| GPT-3.5 | - | 80.8 | 34.1 | 75.1 | 60.0 |
| Minerva | 62B | 52.4 | 27.6 | - | - |
| GAIRMath-Abel | 70B | 83.6 | 28.3 | - | - |
| WizardMath | 70B | 81.6 | 22.7 | - | - |
| Qwen-Chat | 14B | 60.1 | 18.4 | 70.1 | 67.0 |
| Math-Qwen-Chat | 14B | 69.8 | 24.2 | **85.0** | **78.4** |
| Math-Qwen-Chat | 7B | 62.5 | 17.2 | 80.8 | 75.4 |

Math-Qwen-14B-Chat outperforms all open-source models of similar size. It exceeds Minerva-62B on MATH (24.2 vs 27.6 at 62B) and dominates on arithmetic (Math401: 85.0) and Chinese math (Math23K: 78.4). However, it significantly trails 70B-class open-source models on GSM8K (69.8 vs 83.6 GAIRMath-Abel-70B) (tested across 4 math benchmarks with greedy decoding -- moderate evidence).

---

## Limitations and Failure Modes

1. **Gap with proprietary models:** Qwen-Chat "still falls behind GPT-4" in human evaluation across all categories (Section 3.3, Figure 4). The RLHF model achieves ~34.4% win rate against GPT-3.5 while GPT-4 achieves ~54.0%.

2. **Limited base context length:** Base models trained on only 2048 tokens. Context extension techniques are inference-time only, and perplexity at 16K (4.32 for 7B) is notably higher than at the training length of 2048 (3.78), indicating quality degradation at extended lengths (Table 3).

3. **Benchmark evaluation limitations:** The authors explicitly state that "traditional benchmark evaluation" may not "accurately measure the performance and potential of chat models" and call for "new evaluation methods specifically tailored to aligned models" (Section 3.3).

4. **Code interpreter limitations:** Qwen-Chat can fail on visualization tasks requiring multi-step planning. Code Llama outperforms on easy visualization tasks, and GPT-4 substantially outperforms all models on code interpreter correctness (82.8% math vs 58.4% for Qwen-14B, Table 8).

5. **[Inferred]** No explicit safety benchmarks reported. While safety data was included in SFT annotations (Section 3.1.1), no quantitative safety evaluation is presented.

6. **[Inferred]** All results are single-run with no variance estimates or confidence intervals reported across any benchmark, limiting the statistical rigor of the comparisons.

7. **Tool use benchmark limitations:** The authors note their ReAct benchmark "may be relatively easy and may require further enhancement" (Section 3.4), and GPT-3.5's poor performance may reflect the Chinese-language focus rather than genuine tool-use weakness.

#### Scope and Comparability

- **What was not tested:** Models larger than 14B were not released or evaluated for Qwen. No evaluation on long-context benchmarks beyond perplexity (e.g., no QA, summarization, or retrieval tasks at extended lengths). No safety or toxicity benchmarks. No evaluation of the 1.8B chat model in human evaluation. No non-English, non-Chinese language evaluation beyond tokenizer compression efficiency.
- **Comparability notes:** The tool use benchmark (Table 6) is Chinese-language only, which disadvantages English-centric models like GPT-3.5. The code interpreter benchmarks (Tables 7-8) are in-house and not used by other papers, limiting cross-paper comparison. Math evaluation uses the Lightman et al. (2023) test set for MATH rather than the original test set, which may yield different scores. Human evaluation uses 300 Chinese-only instructions, limiting generalizability to English interaction quality. Baseline scores are collected from official reports and OpenCompass rather than re-evaluated under identical conditions.

---

## Conclusions

### Contributions

1. **Open-source bilingual LLM family:** Released Qwen models at 1.8B, 7B, and 14B parameters with strong English/Chinese capabilities. Qwen-14B outperforms all prior 13B-class open-source models on 7 benchmarks and matches Llama 2-70B on several tasks despite being 5x smaller (Table 2).

2. **Efficient multilingual tokenizer:** Developed ~152K vocabulary tokenizer achieving higher compression rates than LLaMA, Baichuan, ChatGLM2, and InternLM across most languages tested (Figure 3).

3. **Training-free context extension:** Demonstrated that combining NTK-aware interpolation, LogN-Scaling, and layer-wise window attention enables effective 8K-16K context handling at inference time without fine-tuning, reducing 16K perplexity from 2645.09 to 4.32 for Qwen-7B (Table 3).

4. **Comprehensive alignment pipeline:** Documented full SFT and RLHF procedures with detailed hyperparameters. RLHF significantly outperforms SFT in human evaluation (Figure 4).

5. **Domain-specialized variants:** Code-Qwen-14B-Chat achieves 66.4% on HumanEval and 51.9% average on HumanEvalPack, leading open-source models. Math-Qwen-14B-Chat achieves 69.8% on GSM8K and 24.2% on MATH with greedy decoding (Tables 10-12).

6. **Strong tool use and agent capabilities:** Qwen-14B-Chat achieves 98% tool selection accuracy on ReAct benchmark (surpassing GPT-4's 95%), and approaches GPT-4 on Hugging Face Agent benchmark (Tables 6, 9).

### Implications

1. **Architecture design choices matter for length extrapolation:** QKV bias and layer-wise window attention suggest that careful Transformer modifications remain consequential for long-context capability, though the QKV bias claim rests on a single citation without ablation (unvalidated).

2. **Smaller models with more tokens can be competitive:** Qwen-14B trained on 3T tokens competes with Llama 2-70B on several benchmarks, consistent with Chinchilla-style scaling insights favoring more data at smaller model sizes.

3. **Generalist models can outperform specialists on agent tasks:** Qwen-Chat outperforms Code Llama on code interpreter tasks despite being a generalist model, suggesting that broad capability is important for tasks requiring planning, language understanding, and coding simultaneously (Table 8).

---

## Key Claims

1. **C1:** Qwen-14B outperforms all previous 13B-class open-source base models on all 7 evaluated benchmarks: MMLU 66.3 (5-shot), C-Eval 72.1 (5-shot), GSM8K 61.3 (8-shot), MATH 24.8 (4-shot), HumanEval 32.3 (0-shot), MBPP 40.8 (3-shot), BBH 53.4 (3-shot) (Table 2, Section 2.6). *Status: supported.* Tested against 12 open-source model variants across 7 benchmarks (strong evidence within this comparison set). Scope: base models without alignment, specific shot settings. No variance estimates reported (limited evidence for statistical significance).

2. **C2:** Combining dynamic NTK-aware interpolation, LogN-Scaling, and layer-wise window attention maintains low perplexity at extended context lengths without fine-tuning. Qwen-7B achieves 4.32 perplexity at 16K (vs 2645.09 baseline), and Qwen-14B achieves 3.42 at 16K (Table 3, Section 2.5). *Status: supported.* Scope: arXiv test data, up to 16384 tokens, perplexity metric only. Tested on 2 model sizes with incremental ablation of 3 techniques (moderate evidence). No downstream task evaluation at extended lengths.

3. **C3:** RLHF significantly outperforms SFT models in human evaluation across knowledge, language understanding, creative writing, math, and coding (Figure 4, Section 3.3). Qwen-14B-Chat (RLHF) achieves ~34.4% average win rate vs GPT-3.5, compared to ~32.3% for Qwen-14B-Chat (SFT). *Status: supported.* Scope: 300 Chinese instructions, 3 annotators. Approximate percentages read from figure (limited precision). Single evaluation dataset (limited evidence for generalization beyond Chinese).

4. **C4:** Qwen-Chat achieves 98% tool selection accuracy on Chinese ReAct benchmark, surpassing GPT-4 (95%) and GPT-3.5 (85%), with only 2.4% false positive rate vs GPT-4's 15.0% (Table 6, Section 3.4). *Status: supported.* Scope: in-house Chinese-language benchmark with up to 5 candidate plugins. Authors acknowledge benchmark "may be relatively easy." Single benchmark, Chinese only (limited evidence for generalization).

5. **C5:** Adding bias to QKV attention layers enhances length extrapolation ability (Section 2.3). *Status: unvalidated* -- referenced to Su (2023b) without experimental ablation or quantitative evidence in this paper. Scope: RoPE-based Transformers. Magnitude: qualitative claim.

6. **C6:** Code-Qwen-14B-Chat achieves 66.4% pass@1 on HumanEval and 51.9% average on HumanEvalPack across 6 languages, leading open-source models in its parameter class (Tables 10-11, Section 4.3). *Status: supported.* Scope: pass@1 metric, synthesize mode for HumanEvalPack. WizardCoder-Python-34B (73.2%) and GPT-3.5 (73.2%) score higher on HumanEval but are larger or proprietary. Tested on 2 benchmarks across 6 languages (moderate evidence).

7. **C7:** Math-Qwen-14B-Chat outperforms all open-source math-specialized models of similar size and exceeds Minerva-62B on MATH: 69.8% GSM8K, 24.2% MATH, 85.0% Math401, 78.4% Math23K (Table 12, Section 5.2). *Status: supported.* Scope: greedy decoding, Lightman et al. (2023) MATH test set. Still significantly trails 70B-class open-source models (GAIRMath-Abel-70B: 83.6% GSM8K, 28.3% MATH) and GPT-3.5/GPT-4. Tested on 4 benchmarks (moderate evidence).

---

## Open Questions

1. **Optimal alignment tax mitigation:** The paper notes using "significantly larger volume of pretrained data in comparison to PPO data" but provides no optimal ratios or systematic study of the pretrained gradient coefficient trade-off (Section 3.2.2). Not addressed by subsequent work in this repository.

2. **Layer-wise window assignment strategy:** The observation that "lower layers are more sensitive to context length extension" (Section 2.5) is stated as motivation for the layer-wise window scheme but not systematically studied. What are the optimal window size assignments, and how do they interact with model depth and size? Not addressed by subsequent work in this repository.

3. **Scaling laws for domain specialization:** How do continued pretraining data requirements for code (~90B tokens used) and math SFT data scale with base model size? Is the 90B code token budget optimal for 14B-scale models? Not addressed by subsequent work in this repository.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* Primary architectural foundation. Qwen extends LLaMA with untied embeddings, QKV bias, and other modifications.

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Source of RoPE positional encoding used in Qwen with FP32 inverse frequency precision.

- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* Basis for SwiGLU activation function selection over GeLU.

- **Su (2023b)** -- *The Magical Effect of the Bias Term: RoPE + Bias = Better Length Extrapolation.* Cited for the decision to add bias to QKV attention layers for length extrapolation.

### Context Extension Techniques

- **bloc97 (2023)** -- *NTK-aware Scaled RoPE.* Reddit post introducing NTK-aware interpolation for training-free context extension, core technique in Qwen's context extension pipeline.

- **Chen et al. (2023a)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* Position interpolation (PI) method that NTK-aware interpolation improves upon.

- **Chiang & Cholak (2022)** -- *Overcoming a Theoretical Limitation of Self-Attention.* Source of LogN-Scaling technique for stabilizing attention entropy.

- **Su (2023a)** -- *Improving Transformer: Length Extrapolation Ability and Position Robustness.* Co-source of LogN-Scaling.

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Source of window attention mechanism adapted for layer-wise assignment.

- **Peng et al. (2023a)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Formally discusses the dynamic NTK-aware interpolation technique used in Qwen.

### Alignment and Training

- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback.* InstructGPT paper establishing the SFT + RLHF paradigm that Qwen follows.

- **Bai et al. (2022b)** -- *Training a Helpful and Harmless Assistant with RLHF.* Source of preference model pretraining (PMP) concept used in Qwen's reward model training.

- **Schulman et al. (2017)** -- *Proximal Policy Optimization Algorithms.* PPO algorithm used for Qwen's RLHF policy training.

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Flash Attention used in pretraining and code pretraining for efficiency.

### Primary Baselines

- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Primary baseline model compared across all evaluations.

- **Roziere et al. (2023)** -- *Code Llama: Open Foundation Models for Code.* Key code baseline; also motivates the continued pretraining approach for Code-Qwen.

### Evaluation Benchmarks

- **Hendrycks et al. (2020)** -- *Measuring Massive Multitask Language Understanding.* MMLU benchmark.

- **Huang et al. (2023)** -- *C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite.* Primary Chinese evaluation benchmark.

- **Chen et al. (2021)** -- *Evaluating Large Language Models Trained on Code.* HumanEval code generation benchmark; also Codex model.

- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems.* GSM8K grade school math benchmark.

- **Hendrycks et al. (2021)** -- *Measuring Mathematical Problem Solving with the MATH Dataset.* MATH competition mathematics benchmark.

- **Yao et al. (2022)** -- *ReAct: Synergizing Reasoning and Acting in Language Models.* ReAct prompting format used for Qwen's tool use evaluation.
