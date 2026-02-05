---
title: "DeepSeek-V3 Technical Report"
authors: "DeepSeek-AI"
year: 2024
venue: "arXiv preprint 2412.19437"
paper_type: preprint
categories: ["model-release", "architecture", "attention-efficiency", "context-extension", "quantization"]
scope: ["MoE architecture", "671B total / 37B activated parameters", "128K context", "FP8 training", "multi-token prediction", "auxiliary-loss-free load balancing"]
benchmarks_used: ["mmlu", "mmlu-pro", "gsm8k", "math-hendrycks", "humaneval", "mbpp", "arc", "hellaswag", "winogrande", "bbh", "gpqa", "niah", "longbench-v2", "triviaqa", "natural-questions", "drop", "ifeval", "arena-hard", "alpaca-eval", "livecodebench", "c-eval"]
models_introduced: ["deepseek-v3"]
models_evaluated: ["gpt-4o", "claude-3.5-sonnet", "llama-3.1-405b", "qwen2.5-72b"]
key_claims:
  - id: C1
    claim: "DeepSeek-V3 achieves 88.5% on MMLU, competitive with GPT-4o (87.2%) and Claude-3.5-Sonnet (88.3%)"
    evidence: "Table 6, Section 5.3"
    status: supported
    scope: "0-shot evaluation"
    magnitude: "88.5% accuracy"
  - id: C2
    claim: "Full training costs only 2.788M H800 GPU hours (~$5.6M), an order of magnitude less than comparable models"
    evidence: "Table 1, Section 1"
    status: supported
    scope: "Pre-training + context extension + post-training"
    magnitude: "2.788M GPU hours total"
  - id: C3
    claim: "Auxiliary-loss-free load balancing via dynamic bias adjustment achieves better performance than auxiliary-loss-based methods"
    evidence: "Table 5, Section 4.5.2"
    status: supported
    scope: "Small and large MoE ablations"
    magnitude: "3.8 points on GSM8K for large MoE"
  - id: C4
    claim: "Multi-token prediction improves downstream task performance, especially on code generation"
    evidence: "Table 4, Section 4.5.1"
    status: supported
    scope: "MTP depth D=1"
    magnitude: "+9.2 points on HumanEval for large MoE"
  - id: C5
    claim: "Training was remarkably stable with no irrecoverable loss spikes or rollbacks throughout the entire process"
    evidence: "Section 1, Abstract"
    status: supported
    scope: "14.8T token pre-training"
  - id: C6
    claim: "DeepSeek-V3 achieves perfect Needle-in-a-Haystack retrieval up to 128K context"
    evidence: "Figure 8, Section 4.3"
    status: supported
    scope: "After YaRN-based context extension"
  - id: C7
    claim: "DeepSeek-V3 outperforms all open-source models and matches closed-source frontier models on math benchmarks"
    evidence: "Table 6, Figure 1"
    status: supported
    scope: "MATH-500, AIME 2024, CNMO 2024"
    magnitude: "90.2% on MATH-500 vs 78.3% Claude-3.5-Sonnet"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Uses Transformer architecture with significant modifications including MLA and MoE"
  - target: 2024-07-llama-3-herd-of-models
    type: evaluates
    detail: "Compares against LLaMA 3.1 405B across all benchmarks, outperforming on most metrics"
  - target: 2023-03-gpt-4-technical-report
    type: evaluates
    detail: "Compares against GPT-4o, achieving competitive or superior performance on most benchmarks"
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "Uses YaRN for context extension from 4K to 128K tokens"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "Uses NIAH to validate 128K context extension with perfect retrieval"
  - target: 2025-12-deepseek-v3.2-frontier-open-llm
    type: extended-by
    detail: "DeepSeek-V3.2 introduces DeepSeek Sparse Attention (DSA) and scaled RL post-training, achieving frontier reasoning performance"
open_questions:
  - question: "Would scaling to even larger MoE models (>1T parameters) maintain the training stability observed at 671B scale?"
    addressed_by: null
  - question: "Can the auxiliary-loss-free load balancing strategy be applied to other MoE architectures?"
    addressed_by: null
  - question: "How does MLA compare to standard GQA in terms of long-context retrieval quality?"
    addressed_by: null
---

# DeepSeek-V3 Technical Report

**Authors:** DeepSeek-AI (~200 contributors)
**Date:** December 2024, arXiv:2412.19437

---

## Core Research Problem

Training large language models at frontier scale remains prohibitively expensive, with costs reaching hundreds of millions of dollars for dense models like LLaMA 3.1 405B. Mixture-of-Experts (MoE) architectures promise efficiency gains by activating only a subset of parameters per token, but face several challenges: (1) **load balancing** traditionally requires auxiliary losses that degrade model performance, (2) **cross-node communication** for expert parallelism creates bottlenecks with computation-to-communication ratios approaching 1:1, (3) **training stability** at extreme scale often requires costly rollbacks, and (4) **KV cache** for long-context inference scales linearly with model dimension.

The core challenge is: **how to train a cost-effective MoE model that achieves frontier performance while maintaining training stability and inference efficiency.**

---

## Problem Solutions

DeepSeek-V3 addresses these challenges through four innovations:

1. **Multi-head Latent Attention (MLA).** Low-rank joint compression of keys, values, and queries reduces KV cache to a small latent vector per token while maintaining multi-head attention quality.

2. **Auxiliary-loss-free load balancing.** Dynamic bias adjustment steers routing decisions without auxiliary losses, avoiding the performance degradation from traditional load balancing.

3. **Multi-token prediction (MTP).** Sequential prediction of additional tokens densifies training signals and enables speculative decoding at inference time.

4. **FP8 mixed precision training.** Fine-grained quantization with careful accumulation precision validates large-scale FP8 training for the first time.

---

## Approach Details

### Architecture

DeepSeek-V3 is a Mixture-of-Experts Transformer with the following specifications (Section 4.2):

| Parameter | Value |
|-----------|-------|
| Total Parameters | 671B |
| Activated Parameters | 37B per token |
| Layers | 61 |
| Hidden Dimension | 7,168 |
| Attention Heads | 128 |
| Per-head Dimension | 128 |
| Vocabulary Size | 128,000 |
| Context Length | 128K (after extension) |

The first 3 layers use dense FFNs; remaining layers use MoE with 1 shared expert + 256 routed experts, 8 activated per token.

### Key Technical Components

#### Multi-head Latent Attention (MLA)

MLA performs low-rank joint compression for keys and values (Section 2.1.1). The compressed latent vector c^KV_t has dimension d_c = 512, compared to d_h * n_h = 16,384 for standard MHA:

> c^KV_t = W^DKV * h_t

Keys and values are then reconstructed via up-projection:

> k^C_t = W^UK * c^KV_t
> v^C_t = W^UV * c^KV_t

A separate decoupled key k^R_t carries RoPE information:

> k^R_t = RoPE(W^KR * h_t)

The final key concatenates compressed and RoPE components: k_t,i = [k^C_t,i; k^R_t]. During inference, only c^KV_t (512 dimensions) and k^R_t (64 dimensions) need caching, achieving significant KV cache reduction.

Query compression uses d'_c = 1,536 dimensions with similar structure.

#### DeepSeekMoE with Auxiliary-Loss-Free Load Balancing

The MoE layer combines one shared expert with K_r = 8 routed experts selected from N_r = 256 (Section 2.1.2):

> h'_t = u_t + FFN^(s)(u_t) + sum_{i=1}^{N_r} g_i,t * FFN^(r)_i(u_t)

Token-to-expert affinity uses sigmoid (not softmax):

> s_i,t = Sigmoid(u_t^T * e_i)

**Load balancing** adds a learned bias b_i to routing decisions without affecting gating values:

> g'_i,t = s_i,t if (s_i,t + b_i) in TopK, else 0

The bias is dynamically adjusted: decreased by gamma = 0.001 for overloaded experts, increased for underloaded experts. A complementary sequence-level auxiliary loss with extremely small alpha = 0.0001 prevents within-sequence imbalance.

**Ablation results (Table 5):** Auxiliary-loss-free achieves 74.5% on GSM8K vs 70.7% for auxiliary-loss-based (large MoE), +3.8 points.

#### Node-Limited Routing

Each token is sent to at most M = 4 nodes, selected by summing the highest K_r/M affinity scores per node. This bounds cross-node communication while allowing 3.2 experts per node on average within the NVLink bandwidth.

#### Multi-Token Prediction (MTP)

MTP sequentially predicts D = 1 additional token using a separate module that combines the main model's representation with the embedding of the predicted token (Section 2.2):

> h'^k_i = M_k * [RMSNorm(h^{k-1}_i); RMSNorm(Emb(t_{i+k}))]

The MTP loss is weighted by lambda = 0.3 for the first 10T tokens, 0.1 thereafter:

> L_MTP = (lambda/D) * sum_{k=1}^{D} CrossEntropy(P^k, t)

**Ablation results (Table 4):** MTP improves HumanEval from 44.5% to 53.7% (+9.2 points) for large MoE.

At inference, the MTP module achieves 85-90% acceptance rate for the second token, enabling 1.8x throughput via speculative decoding (Section 5.4.3).

### Training Infrastructure

**Hardware (Section 3.1):**
- 2,048 NVIDIA H800 GPUs (8 per node, NVLink 160 GB/s, IB 50 GB/s between nodes)

**Parallelism (Section 3.2):**
- 16-way Pipeline Parallelism
- 64-way Expert Parallelism (8 nodes)
- ZeRO-1 Data Parallelism
- No Tensor Parallelism

**DualPipe Algorithm:** Novel bidirectional pipeline scheduling feeds micro-batches from both ends simultaneously, achieving near-zero all-to-all communication overhead through computation-communication overlap.

### FP8 Mixed Precision Training

DeepSeek-V3 validates FP8 training at extreme scale (Section 3.3):

- **Quantized:** GEMM operations (Fprop, Dgrad, Wgrad) in E4M3 format
- **Higher precision:** Embeddings, output head, gating, normalization, attention operators in BF16/FP32
- **Fine-grained quantization:** 1x128 tile-wise for activations, 128x128 block-wise for weights
- **Accumulation fix:** Promote to FP32 every N_C = 128 elements to compensate for H800's ~14-bit accumulation precision

Relative loss error vs BF16 baseline: < 0.25% (Appendix B.1).

### Training Schedule

**Hyperparameters (Section 4.2):**
- Optimizer: AdamW (beta_1=0.9, beta_2=0.95, weight_decay=0.1)
- Peak LR: 2.2 x 10^-4
- Warmup: 2K steps linear
- Schedule: Constant until 10T tokens, cosine decay to 2.2 x 10^-5 over 4.3T tokens
- Batch size: 3,072 -> 15,360 (ramped over first 469B tokens)
- Sequence length: 4K during pre-training

**Data:** 14.8T tokens with enhanced math/code ratio, byte-level BPE tokenizer (128K vocab), Fill-in-Middle at 0.1 rate.

### Context Extension

Two-stage YaRN extension (Section 4.3):
1. 4K -> 32K: 1,000 steps, batch size 1,920, LR 7.3 x 10^-6
2. 32K -> 128K: 1,000 steps, batch size 480, LR 7.3 x 10^-6

YaRN applied only to decoupled key k^R_t with scale s = 40, alpha = 1, beta = 32.

**Total context extension cost:** 119K H800 GPU hours.

### Post-Training

**SFT (Section 5.1):** 1.5M instances, 2 epochs, cosine LR decay from 5 x 10^-6 to 1 x 10^-6. Reasoning data generated by internal DeepSeek-R1 model with reflection/verification patterns.

**RL (Section 5.2):** Group Relative Policy Optimization (GRPO) with rule-based rewards for verifiable tasks (math, code) and model-based rewards for free-form answers.

### Key Results

**Chat Model Performance (Table 6):**

| Benchmark | DeepSeek-V3 | GPT-4o | Claude-3.5-Sonnet | LLaMA-3.1-405B |
|-----------|-------------|--------|-------------------|----------------|
| MMLU | **88.5** | 87.2 | 88.3 | 88.6 |
| MMLU-Pro | 75.9 | 72.6 | **78.0** | 73.3 |
| GPQA-Diamond | 59.1 | 49.9 | **65.0** | 51.1 |
| MATH-500 | **90.2** | 74.6 | 78.3 | 73.8 |
| AIME 2024 | **39.2** | 9.3 | 16.0 | 23.3 |
| HumanEval-Mul | **82.6** | 80.5 | 81.7 | 77.2 |
| LiveCodeBench-COT | **40.5** | 33.4 | 36.3 | 28.4 |
| Codeforces Percentile | **51.6** | 23.6 | 20.3 | 25.3 |
| LongBench v2 | **48.7** | 48.1 | 41.0 | 36.1 |

**Base Model Performance (Table 3):**

| Benchmark | DeepSeek-V3-Base | LLaMA-3.1-405B | Qwen2.5-72B |
|-----------|------------------|----------------|-------------|
| MMLU | **87.1** | 84.4 | 85.0 |
| BBH | **87.5** | 82.9 | 79.8 |
| HumanEval | **65.2** | 54.9 | 53.0 |
| GSM8K | **89.3** | 83.5 | 88.3 |
| MATH | **61.6** | 49.0 | 54.4 |

**Training Costs (Table 1):**

| Phase | H800 GPU Hours | USD (at $2/hr) |
|-------|----------------|----------------|
| Pre-Training | 2,664K | $5.328M |
| Context Extension | 119K | $0.238M |
| Post-Training | 5K | $0.01M |
| **Total** | **2,788K** | **$5.576M** |

**Training efficiency:** 180K H800 GPU hours per trillion tokens (~3.7 days on 2,048 GPUs).

---

## Limitations and Failure Modes

The paper acknowledges the following limitations (Section 6):

1. **Large deployment unit.** Prefilling requires minimum 4 nodes (32 GPUs); decoding requires minimum 40 nodes (320 GPUs). This poses a burden for small teams.

2. **Inference speed.** Despite 2x improvement over DeepSeek-V2, further optimization potential remains.

3. **English factual knowledge.** SimpleQA: 24.9% vs GPT-4o's 38.2%, attributed to resource allocation toward Chinese knowledge.

4. **Software engineering tasks.** SWE-Bench Verified: 42.0% vs Claude-3.5-Sonnet's 50.8%.

### Scope and Comparability

- **Single model tested:** Results are for DeepSeek-V3 only; ablations used smaller proxies.
- **No variance estimates reported** for benchmark results.
- **Distillation from DeepSeek-R1:** Math improvements partially attributed to distillation, complicating attribution of gains to architectural innovations.

---

## Conclusions

### Contributions

1. **First validated FP8 training at extreme scale.** Fine-grained quantization with accumulation precision fixes achieves <0.25% relative loss error vs BF16, enabling practical FP8 training for 671B parameter models (Section 3.3, Appendix B.1).

2. **Auxiliary-loss-free load balancing.** Dynamic bias adjustment achieves better downstream performance than auxiliary-loss methods (+3.8 points on GSM8K for large MoE) while maintaining balanced expert utilization (Section 2.1.2, Table 5).

3. **Multi-token prediction for training and inference.** MTP improves downstream performance (+9.2 points on HumanEval) and enables 1.8x inference throughput via speculative decoding with 85-90% acceptance rate (Section 2.2, Section 5.4.3).

4. **Order-of-magnitude training cost reduction.** Full training in 2.788M H800 GPU hours (~$5.6M) while achieving frontier performance, compared to estimated hundreds of millions for comparable dense models (Table 1).

5. **Remarkable training stability.** No irrecoverable loss spikes or rollbacks throughout 14.8T token pre-training, attributed to effective load balancing and FP8 training framework (Section 1).

### Implications

1. **MoE efficiency is practically achievable.** The combination of MLA, auxiliary-loss-free load balancing, and node-limited routing demonstrates that MoE communication overhead can be effectively managed, making frontier MoE models practical.

2. **FP8 training is viable at scale.** The successful 671B parameter FP8 training suggests future models may default to lower precision, reducing hardware requirements. This is speculative as longer training runs may reveal stability issues.

3. **Architectural innovations compound.** MLA, DeepSeekMoE, MTP, and FP8 training each provide independent benefits; their combination enables cost-effective frontier training.

---

## Key Claims

1. **DeepSeek-V3 achieves 88.5% on MMLU, matching frontier closed-source models.** Competitive with GPT-4o (87.2%), Claude-3.5-Sonnet (88.3%), LLaMA-3.1-405B (88.6%). Evidence: Table 6. Status: **supported**.

2. **Training costs are dramatically lower than comparable models.** 2.788M H800 GPU hours total (~$5.6M), orders of magnitude less than estimated costs for LLaMA 3.1 405B or GPT-4. Evidence: Table 1. Status: **supported**. Scope: Excludes prior research and ablation costs.

3. **Auxiliary-loss-free load balancing outperforms auxiliary-loss methods.** +3.8 points on GSM8K (74.5% vs 70.7%), +6.1 points on HumanEval (46.3% vs 40.2%) for large MoE. Evidence: Table 5. Status: **supported**. Scope: Controlled ablation with same training budget.

4. **MTP improves performance on code generation and math.** +9.2 points on HumanEval (53.7% vs 44.5%), +1.2 points on MATH (39.8% vs 38.6%) for large MoE. Evidence: Table 4. Status: **supported**. Scope: MTP depth D=1.

5. **Training was completely stable with no rollbacks.** Zero irrecoverable loss spikes throughout 14.8T token pre-training. Evidence: Section 1, Abstract. Status: **supported**. Scope: Single training run.

6. **Perfect NIAH retrieval up to 128K context.** Figure 8 shows consistent score ~10/10 across all depths and context lengths. Evidence: Figure 8. Status: **supported**. Scope: After YaRN context extension.

7. **DeepSeek-V3 outperforms all models on MATH-500 and competitive math benchmarks.** 90.2% vs Claude-3.5-Sonnet 78.3%, GPT-4o 74.6%. Evidence: Table 6, Figure 1. Status: **supported**. Scope: Partially attributed to DeepSeek-R1 distillation.

---

## Open Questions

1. **Scaling stability.** Would training stability hold at >1T parameters, or would new instabilities emerge?

2. **Generalizability of auxiliary-loss-free balancing.** Can the dynamic bias approach transfer to other MoE architectures (e.g., Mixtral, Switch Transformer)?

3. **MLA vs GQA for long-context.** Does MLA's compression affect retrieval quality at extreme context lengths beyond NIAH?

4. **Attribution of math gains.** How much of the math improvement comes from architectural innovations vs DeepSeek-R1 distillation?

5. **Deployment efficiency.** Can the minimum deployment unit (32-320 GPUs) be reduced through optimization?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Base Transformer architecture that DeepSeek-V3 builds upon.
- **Shazeer et al. (2017)** -- *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.* Foundational MoE architecture enabling sparse expert activation.

### Direct Predecessors

- **DeepSeek-AI (2024)** -- *DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model.* Direct predecessor introducing MLA and DeepSeekMoE architectures that V3 inherits and refines.

### Context Extension

- **Peng et al. (2024)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Context extension method used for 4K->128K expansion.

### Multi-Token Prediction

- **Gloeckle et al. (2024)** -- *Better & Faster Large Language Models via Multi-token Prediction.* Concurrent work on MTP that DeepSeek-V3's sequential variant improves upon.

### Load Balancing

- **Wang et al. (2024)** -- *Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts.* Prior work on auxiliary-loss-free balancing that DeepSeek-V3's dynamic bias approach extends.

### Competing Models

- **Dubey et al. (2024)** -- *The Llama 3 Herd of Models.* Primary dense model comparison target.
- **OpenAI (2024)** -- *GPT-4o.* Primary closed-source comparison target.
- **Anthropic (2024)** -- *Claude 3.5 Sonnet.* Primary closed-source comparison target.

### Evaluation Benchmarks

- **Kamradt (2023)** -- *Needle-in-a-Haystack.* Used to validate context extension quality.
- **Hendrycks et al. (2021)** -- *MATH.* Primary math reasoning benchmark.
- **Chen et al. (2021)** -- *HumanEval.* Primary code generation benchmark.
