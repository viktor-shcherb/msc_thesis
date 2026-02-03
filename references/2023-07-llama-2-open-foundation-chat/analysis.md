# Llama 2: Open Foundation and Fine-Tuned Chat Models

**Authors:** Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, ..., Thomas Scialom (Meta AI, GenAI)
**Date:** July 2023, arXiv:2307.09288

---

## Core Research Problem

Despite growing interest in open-weight language models following LLaMA (Touvron et al., 2023a), there was no open-weight model family that combined competitive base model performance with a fully documented alignment pipeline (supervised fine-tuning, RLHF) and a permissive commercial license. Existing open models were either (a) base-only without alignment (LLaMA, OPT), (b) closed-weight with alignment (GPT-4, PaLM 2), or (c) aligned but without documented methodology. Furthermore, LLaMA's 2048-token context window was a practical limitation, and its release license restricted commercial use. The core challenge was: **how to produce an open-weight model family with extended context length, documented alignment methodology, safety evaluations, and a commercial license, while matching or exceeding existing open-source models and approaching closed-source chat assistants.**

---

## Problem Solutions

Llama 2 addresses the problem through three contributions:

1. **Stronger pretrained base models.** Train 7B, 13B, and 70B parameter models on 2T tokens (40% more data than LLaMA) with an extended 4096-token context window. Adopt Grouped-Query Attention (GQA) for the 70B model to improve inference efficiency.

2. **Documented alignment pipeline (Llama 2-Chat).** Apply supervised fine-tuning (SFT) followed by iterative Reinforcement Learning from Human Feedback (RLHF) using both Rejection Sampling and Proximal Policy Optimization (PPO). Introduce Ghost Attention (GAtt) for multi-turn system prompt adherence.

3. **Open release with safety evaluation.** Release model weights under a permissive commercial license, accompanied by detailed safety evaluations, red teaming, and responsibility analysis.

---

## Approach Details

### Architecture

Llama 2 uses the same base architecture as LLaMA with two changes:

1. **Extended context length:** 4096 tokens (doubled from LLaMA's 2048). RoPE positional encoding (Su et al., 2021) with base frequency b = 10000 is retained. The extended context requires no architectural changes -- RoPE naturally supports any sequence length -- but requires training on longer sequences.

2. **Grouped-Query Attention (GQA):** The 70B model uses GQA (Ainslie et al., 2023) with 8 key-value heads shared across 64 query heads (a ratio of 8:1). This reduces the KV cache size by 8x compared to standard multi-head attention, improving inference throughput for long-sequence and large-batch generation. The 7B and 13B models retain standard multi-head attention (n_kv_heads = n_heads).

All other architectural choices from LLaMA are retained: pre-normalization with RMSNorm, SwiGLU activations, no bias terms, and the same SentencePiece BPE tokenizer with a 32,000-token vocabulary.

### Model Configurations

| Model | Parameters | d_model | n_heads | n_kv_heads | n_layers | d_ff | Context Length | Training Tokens |
|---|---|---|---|---|---|---|---|---|
| Llama 2-7B | 6.7B | 4096 | 32 | 32 | 32 | 11008 | 4096 | 2.0T |
| Llama 2-13B | 13.0B | 5120 | 40 | 40 | 40 | 13824 | 4096 | 2.0T |
| Llama 2-70B | 69.0B | 8192 | 64 | 8 | 80 | 28672 | 4096 | 2.0T |

Head dimension remains 128 (d_model / n_heads) for all models.

### Pretraining

- **Data:** 2T tokens from a new mix of publicly available data. The exact composition is not disclosed, but the paper states the data mix was adjusted to upweight more factual sources compared to LLaMA.
- **Optimizer:** AdamW (beta_1 = 0.9, beta_2 = 0.95, epsilon = 1e-5)
- **Learning rate:** Cosine schedule with 2000 warmup steps. Peak learning rates: 3.0e-4 (7B, 13B), 1.5e-4 (70B). Final learning rate is 10% of peak.
- **Weight decay:** 0.1
- **Gradient clipping:** 1.0
- **Training hardware:** Meta's Research Super Cluster (RSC) and internal production cluster, using A100-80GB GPUs.
- **Training time:** 7B required 184,320 GPU-hours; 13B required 368,640 GPU-hours; 70B required 1,720,320 GPU-hours.

### Grouped-Query Attention (GQA) Details

Standard multi-head attention (MHA) uses n_heads independent key-value heads. Multi-query attention (MQA) uses a single key-value head shared across all query heads. GQA is an intermediate: n_kv_heads key-value heads are shared across n_heads query heads, with each KV head serving n_heads / n_kv_heads query heads.

For the 70B model, 8 KV heads serve 64 query heads. This reduces the KV cache from 64 * 128 * 2 = 16,384 to 8 * 128 * 2 = 2,048 values per token per layer, an 8x reduction. The 70B model was converted from a multi-head attention checkpoint by mean-pooling the original KV heads within each group, then fine-tuning for an additional fraction of pretraining.

### Alignment: Supervised Fine-Tuning (SFT)

SFT uses publicly available instruction-tuning data plus vendor-collected annotations. The paper found that a small number of high-quality, carefully curated annotations (27,540 examples) outperformed larger but noisier datasets. Training runs for 2 epochs with a cosine learning rate schedule, peak 2e-5, batch size 64, sequence length 4096.

### Alignment: Reinforcement Learning from Human Feedback (RLHF)

RLHF proceeds through five iterative rounds (batches of human preference data collected and models updated iteratively):

1. **Reward modeling:** Two separate reward models are trained -- one for helpfulness and one for safety -- using human preference data. Binary ranking data (chosen vs. rejected) is used to train the reward models with a binary ranking loss. A margin term is added to the loss for samples with distinct annotator confidence levels.

2. **Rejection Sampling (RS):** For each prompt, K outputs are sampled from the current policy (K = 70 for Llama 2-70B-Chat). The output with the highest reward model score is selected. This new dataset is used for further SFT.

3. **Proximal Policy Optimization (PPO):** Standard PPO applied after rejection sampling. The reward function combines helpfulness and safety rewards with a parameter that upweights safety when the safety score is below a threshold.

### Ghost Attention (GAtt)

Ghost Attention is a technique for enforcing system prompt adherence across multi-turn dialogues. In training, the system prompt (instructions) is prepended to each user message in a multi-turn conversation, creating synthetic training examples where the model "sees" the system prompt at every turn. During inference, the system prompt is given only at the first turn. The model learns to attend to it across turns. GAtt is implemented by setting the loss to zero on tokens from all turns except the latest assistant response, focusing learning on following the system instruction in the current response.

### Experimental Setup

**Base model evaluation:** Standard benchmarks including MMLU (5-shot), reading comprehension, commonsense reasoning (ARC, HellaSwag, WinoGrande, BoolQ, PIQA), code (HumanEval, MBPP), and math (GSM8K, MATH).

**Chat model evaluation:** Human evaluation comparing Llama 2-Chat against ChatGPT, PaLM 2-Chat (with Bard), Falcon, Vicuna, and other open-source chat models. Evaluators choose a preferred response in pairwise comparisons on ~4000 prompts across helpfulness and safety categories.

### Key Results

**Base models (selected benchmarks):**

| Model | MMLU (5-shot) | TriviaQA (1-shot) | NQ (1-shot) | HumanEval (pass@1) | GSM8K (8-shot) |
|---|---|---|---|---|---|
| Llama 2-7B | 45.3 | 68.9 | 25.7 | 12.8 | 14.6 |
| Llama 2-13B | 54.8 | 77.2 | 32.8 | 18.9 | 28.7 |
| Llama 2-70B | 68.9 | 85.0 | 46.2 | 29.9 | 56.8 |
| LLaMA-65B | 63.4 | 84.2 | 39.9 | 23.7 | 50.9 |
| GPT-3.5 | 70.0 | -- | -- | 48.1 | 57.1 |

- Llama 2-70B outperforms LLaMA-65B on all benchmarks (68.9 vs 63.4 on MMLU; 56.8 vs 50.9 on GSM8K).
- Llama 2-70B approaches GPT-3.5 on MMLU (68.9 vs 70.0) and GSM8K (56.8 vs 57.1), but lags on code generation (29.9 vs 48.1 on HumanEval).
- On knowledge-intensive tasks (TriviaQA, NQ), Llama 2-70B matches or exceeds GPT-3.5.

**Chat models (human evaluation win rates vs. ChatGPT):**

| Model | Helpfulness Win Rate | Safety Win Rate |
|---|---|---|
| Llama 2-Chat 70B | 36.0% | 44.0% |
| Falcon-40B-Instruct | 15.0% | -- |
| Vicuna-33B | 22.0% | -- |
| ChatGPT (reference) | 50.0% | 50.0% |

- Llama 2-Chat 70B is the strongest open-source chat model at the time of release, with a 36% win rate against ChatGPT on helpfulness.
- On safety evaluations, Llama 2-Chat achieves a violation rate lower than ChatGPT on the paper's internal safety benchmarks.

### GQA Inference Speedup

The paper reports that GQA in the 70B model achieves comparable quality to MHA while enabling faster inference, particularly for long-sequence generation:

- Conversion from MHA to GQA (8 KV heads) with additional pretraining produces models with <1% accuracy degradation compared to MHA.
- Inference throughput improvement scales with batch size and sequence length due to reduced KV cache memory.

---

## Conclusions

1. **Extended context and more data improve base performance.** Llama 2's 4096-token context and 2T training tokens yield consistent improvements over LLaMA across all benchmarks (e.g., MMLU 68.9 vs 63.4 for the largest models).

2. **GQA enables efficient large-model inference.** The 70B model uses 8 KV heads (vs. 64 for full MHA), reducing KV cache by 8x with negligible quality loss. This is the first widely adopted open model to use GQA, establishing it as a standard for models >30B parameters.

3. **Iterative RLHF with rejection sampling improves progressively.** Five rounds of RLHF with increasing human preference data show consistent improvements. Rejection sampling is particularly effective at the 70B scale where more diverse samples can be drawn.

4. **Ghost Attention enables multi-turn instruction following.** GAtt allows the model to adhere to system instructions across extended multi-turn dialogues without requiring the system prompt at every turn, solving a practical deployment problem.

5. **Open-source chat models approach closed-source quality.** Llama 2-Chat 70B achieves a 36% win rate against ChatGPT on human evaluations of helpfulness, demonstrating that the gap between open and closed models was narrowing. However, a significant gap remained on coding and mathematical reasoning tasks.

6. **Established the dominant open-weight model family.** Llama 2's commercial license and documented alignment pipeline made it the foundation for the majority of subsequent open-source model development, including fine-tuned variants (Vicuna, Orca, Zephyr) and the Llama 3 successor family.

---

## Core References and Why They Are Referenced

### Architecture Foundations
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture. Llama 2 retains the decoder-only autoregressive structure with modifications.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Provides RoPE, retained in Llama 2 with the same base frequency b = 10000 but extended to 4096-token context. The extended context window of Llama 2 became the primary target for context extension research (PI, YaRN, StreamingLLM).
- **Zhang & Sennrich (2019)** -- *Root Mean Square Layer Normalization.* RMSNorm used for pre-normalization, inherited from LLaMA.
- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* SwiGLU activation, inherited from LLaMA.

### Direct Predecessor
- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* The base architecture and training methodology that Llama 2 extends. Llama 2 doubles the context length, increases training data by 40%, and adds GQA for the 70B model.

### Grouped-Query Attention
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.* Introduces GQA and the method for converting MHA checkpoints to GQA via mean-pooling of KV heads. Llama 2 70B is the first widely used open model to adopt GQA.
- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head Is All You Need.* Introduces multi-query attention (MQA), the extreme case of GQA with a single KV head. GQA is an interpolation between MQA and MHA.

### Alignment and RLHF
- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback (InstructGPT).* Establishes the SFT + RLHF pipeline that Llama 2-Chat follows.
- **Schulman et al. (2017)** -- *Proximal Policy Optimization Algorithms.* PPO algorithm used in the RLHF stage.
- **Bai et al. (2022)** -- *Constitutional AI: Harmlessness from AI Feedback.* Related alignment approach; Llama 2 uses a similar dual-reward (helpfulness + safety) framework.

### Evaluation and Safety
- **Hartvigsen et al. (2022)** -- *ToxiGen: A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection.* Used for toxicity evaluation of Llama 2-Chat.
- **Lin et al. (2022)** -- *TruthfulQA: Measuring How Models Mimic Human Falsehoods.* Used for evaluating truthfulness.

#### Cross-References in Available Papers

**How Llama 2 is referenced in papers in this directory:**

- **YaRN (2024-05-yarn-context-extension):** Llama 2 7B and 13B are the primary experimental models. YaRN extends Llama 2's 4096-token context to 64K (s=16) and 128K (s=32), achieving 2.37 perplexity at 128K on Proof-pile. YaRN requires only 400 training steps on Llama 2.
- **StreamingLLM (2024-05-attention-sinks-streaming):** Uses Llama-2-[7, 13, 70]B as primary evaluation models. Demonstrates attention sinks in the first 4 tokens of Llama 2, and achieves stable streaming at 4M+ tokens by preserving these initial tokens in the KV cache.
- **Lost in the Middle (2024-02-lost-in-the-middle):** Uses Llama 2 (7B, 13B, 70B) in the model scale ablation, demonstrating that increasing model size does not eliminate the U-shaped position bias in multi-document QA.
- **LongBench (2024-08-longbench-bilingual-benchmark):** Evaluates Llama2-7B-chat-4k as a short-context open-source baseline (31.0 average). LongChat and Vicuna variants fine-tuned from Llama 2 improve to 34.2--35.3 with extended context.
- **L-Eval (2024-08-l-eval-standardized-evaluation):** References "Touvron et al. (2023b)" as the base model for many open-source LCLMs. Evaluates Llama2-7b, Llama2-7b-chat, Llama2-13b-chat, and NTK-extended variants.
- **RULER (2024-10-ruler-context-size):** Uses Llama2-7B as the baseline for defining the "effective context size" threshold (85.6% at 4K).
- **BABILong (2024-12-babilong-long-context-reasoning):** Evaluates LLaMA-2-7B-32K (PI-extended) alongside Llama 3.1 models. LLaMA-2-7B-32K fails even at its trained length of 32K.
- **LongICLBench (2025-03-longiclbench-long-in-context-learning):** Evaluates LLaMA-2-7B-32K and LLaMA-2-7B-LongLora as context extension baselines.
- **Pos2Distill (2025-11-pos2distill-position-bias-distillation):** Uses Llama-2-7B for comparison with Attention Buckets, MoICE, and PEAR baselines on position bias mitigation.
- **DroPE (2025-12-drope-dropping-positional-embeddings):** Recalibrates Llama2-7B with DroPE using only 20B tokens, achieving LongBench Avg. 26.08 vs 21.88 for RoPE-NTK extension.
