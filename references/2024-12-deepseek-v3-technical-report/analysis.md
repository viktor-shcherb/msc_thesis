---
title: "DeepSeek-V3 Technical Report"
authors: "DeepSeek-AI"
year: 2024
venue: "arXiv preprint 2412.19437"
paper_type: preprint
categories: ["model-release", "architecture", "attention-efficiency", "context-extension", "quantization"]
scope: ["MoE architecture", "671B total / 37B activated parameters", "128K context", "FP8 training", "multi-token prediction", "auxiliary-loss-free load balancing"]
benchmarks_used: ["mmlu", "mmlu-pro", "gsm8k", "math-hendrycks", "humaneval", "mbpp", "arc", "hellaswag", "winogrande", "bbh", "gpqa", "niah", "longbench-v2", "triviaqa", "natural-questions", "drop", "ifeval", "arena-hard", "alpaca-eval", "livecodebench", "c-eval", "cmmlu", "mgsm", "piqa", "race", "agi-eval", "rewardbench", "perplexity-pile"]
models_introduced: ["deepseek-v3"]
models_evaluated: ["gpt-4o", "claude-3.5-sonnet", "llama-3.1-405b", "qwen2.5-72b", "deepseek-v2"]
key_claims:
  - id: C1
    claim: "DeepSeek-V3 achieves 88.5% on MMLU, competitive with GPT-4o (87.2%) and Claude-3.5-Sonnet (88.3%)"
    evidence: "Table 6, Section 5.3"
    status: supported
    scope: "Chat model, simple-evals evaluation prompts, max 8K output tokens"
    magnitude: "88.5% accuracy (vs 87.2% GPT-4o, 88.3% Claude-3.5-Sonnet, 88.6% LLaMA-3.1-405B)"
  - id: C2
    claim: "Full training costs only 2.788M H800 GPU hours (~$5.576M), excluding prior research and ablation costs"
    evidence: "Table 1, Section 1"
    status: supported
    scope: "Pre-training + context extension + post-training only; excludes prior research and ablation experiments"
    magnitude: "2.788M GPU hours total ($5.576M at $2/GPU-hour)"
  - id: C3
    claim: "Auxiliary-loss-free load balancing via dynamic bias adjustment achieves better performance than auxiliary-loss-based methods"
    evidence: "Table 5, Section 4.5.2"
    status: supported
    scope: "Ablation on 15.7B (1.33T tokens) and 228.7B (578B tokens) MoE models"
    magnitude: "+3.8 points on GSM8K (74.5% vs 70.7%), +6.1 points on HumanEval (46.3% vs 40.2%) for large MoE"
  - id: C4
    claim: "Multi-token prediction improves downstream task performance, especially on code generation"
    evidence: "Table 4, Section 4.5.1"
    status: supported
    scope: "Ablation on 15.7B (1.33T tokens) and 228.7B (540B tokens) MoE models, MTP depth D=1"
    magnitude: "+9.2 points on HumanEval (53.7% vs 44.5%), +1.7 points on GSM8K (74.0% vs 72.3%) for large MoE"
  - id: C5
    claim: "Training was remarkably stable with no irrecoverable loss spikes or rollbacks throughout the entire process"
    evidence: "Section 1, Abstract"
    status: supported
    scope: "Single training run, 14.8T tokens, 671B parameter MoE"
    magnitude: "Zero rollbacks across full 14.8T token training"
  - id: C6
    claim: "DeepSeek-V3 achieves perfect Needle-in-a-Haystack retrieval up to 128K context"
    evidence: "Figure 8, Section 4.3"
    status: supported
    scope: "After two-stage YaRN context extension (4K->32K->128K), post-SFT"
    magnitude: "Score ~10/10 across all depths and context lengths up to 128K"
  - id: C7
    claim: "DeepSeek-V3 outperforms all non-o1-like models on MATH-500 and competitive math benchmarks"
    evidence: "Table 6, Figure 1"
    status: supported
    scope: "Non-long-CoT models, MATH-500 with greedy decoding, AIME/CNMO with temp=0.7 averaged over 16 runs"
    magnitude: "90.2% on MATH-500 (vs 78.3% Claude-3.5-Sonnet, 74.6% GPT-4o); 39.2% on AIME 2024 (vs 23.3% next best)"
  - id: C8
    claim: "FP8 mixed precision training achieves <0.25% relative loss error compared to BF16 baseline"
    evidence: "Section 3.3, Appendix B.1, Figure 10"
    status: supported
    scope: "Validated on ~16B and ~230B MoE models; 1.33T and ~0.9T tokens respectively"
    magnitude: "Relative loss error < 0.25%"
  - id: C9
    claim: "Distillation from DeepSeek-R1 significantly improves reasoning performance"
    evidence: "Table 9, Section 5.4.1"
    status: supported
    scope: "Ablated on DeepSeek-V2.5, LiveCodeBench and MATH-500"
    magnitude: "+6.3 points on LiveCodeBench-CoT (37.4% vs 31.1%), +8.6 points on MATH-500 (83.2% vs 74.6%)"
  - id: C10
    claim: "MTP enables 1.8x inference throughput via speculative decoding with 85-90% second-token acceptance rate"
    evidence: "Section 5.4.3"
    status: supported
    scope: "Various generation topics, speculative decoding framework"
    magnitude: "1.8x TPS improvement, 85-90% acceptance rate"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Uses Transformer architecture with significant modifications including MLA and MoE"
  - target: 2024-05-deepseek-v2-moe
    type: extends
    detail: "Direct successor; inherits MLA and DeepSeekMoE architectures, adds auxiliary-loss-free balancing and MTP"
  - target: 2024-07-llama-3-herd-of-models
    type: evaluates
    detail: "Compares against LLaMA 3.1 405B across all benchmarks, outperforming on most metrics"
  - target: 2023-03-gpt-4-technical-report
    type: evaluates
    detail: "Compares against GPT-4o, achieving competitive or superior performance on most benchmarks"
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "Uses YaRN for two-stage context extension from 4K to 32K to 128K tokens"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "Uses NIAH to validate 128K context extension with perfect retrieval across all depths"
  - target: 2024-08-deepseek-moe
    type: extends
    detail: "Builds on DeepSeekMoE architecture with finer-grained experts and shared experts"
  - target: 2025-12-deepseek-v3.2-frontier-open-llm
    type: extended-by
    detail: "DeepSeek-V3.2 introduces DeepSeek Sparse Attention (DSA) and scaled RL post-training"
  - target: 2025-04-kimi-vl-technical-report
    type: extended-by
    detail: "Kimi-VL uses Moonlight (architecture similar to DeepSeek-V3) as its MoE language backbone for a vision-language model"
open_questions:
  - question: "Would scaling to even larger MoE models (>1T parameters) maintain the training stability observed at 671B scale?"
    addressed_by: null
  - question: "Can the auxiliary-loss-free load balancing strategy be applied to other MoE architectures (e.g., Mixtral, Switch Transformer)?"
    addressed_by: null
  - question: "How does MLA compare to standard GQA in terms of long-context retrieval quality beyond NIAH?"
    addressed_by: null
  - question: "How much of the math improvement comes from architectural innovations vs DeepSeek-R1 distillation?"
    addressed_by: null
  - question: "Can the minimum deployment unit (32-320 GPUs) be reduced through further optimization or with next-generation hardware?"
    addressed_by: null
---

# DeepSeek-V3 Technical Report

**Authors:** DeepSeek-AI (~200 contributors; DeepSeek-AI, Hangzhou, China)
**Date:** December 2024, arXiv:2412.19437

---

## Core Research Problem

Training large language models at frontier scale remains prohibitively expensive, with costs for dense models like LLaMA 3.1 405B reaching hundreds of millions of dollars. Mixture-of-Experts (MoE) architectures promise efficiency by activating only a subset of parameters per token, but face several interrelated challenges: (1) **load balancing** traditionally requires auxiliary losses that degrade model performance by pushing expert utilization toward uniformity at the cost of specialization (Shazeer et al., 2017; Fedus et al., 2021; Wang et al., 2024a); (2) **cross-node expert communication** creates bottlenecks with computation-to-communication ratios approaching 1:1 (Section 3.2.1); (3) **training stability** at extreme scale often requires costly rollbacks; (4) **KV cache** for long-context inference scales linearly with model dimension in standard MHA; and (5) **low-precision training** at FP8 has not been validated at extreme scale, limiting potential efficiency gains.

The core challenge is: **how to train a cost-effective MoE model that achieves frontier performance while maintaining training stability and inference efficiency, at a fraction of the cost of comparable dense models.**

---

## Problem Solutions

DeepSeek-V3 addresses these challenges through a combination of architectural innovations, training infrastructure optimizations, and post-training techniques:

1. **Multi-head Latent Attention (MLA)** compresses keys, values, and queries via low-rank projections, reducing KV cache to a compact latent vector per token while maintaining performance comparable to standard MHA (inherited from DeepSeek-V2).

2. **Auxiliary-loss-free load balancing** uses dynamic bias adjustment to steer routing decisions without auxiliary losses, avoiding the performance degradation from traditional load balancing while enabling greater expert specialization.

3. **Multi-Token Prediction (MTP)** sequentially predicts additional future tokens, densifying training signals and enabling speculative decoding at inference time.

4. **FP8 mixed precision training** with fine-grained quantization (tile-wise for activations, block-wise for weights) and careful accumulation precision validates large-scale FP8 training for the first time.

5. **DualPipe algorithm** for bidirectional pipeline parallelism achieves near-zero all-to-all communication overhead through computation-communication overlap.

---

## Approach Details

### Method

DeepSeek-V3 is a Mixture-of-Experts Transformer with the following specifications (Section 4.2):

| Parameter | Value |
|-----------|-------|
| Total Parameters | 671B |
| Activated Parameters | 37B per token |
| Transformer Layers | 61 |
| Hidden Dimension (d) | 7,168 |
| Attention Heads (n_h) | 128 |
| Per-head Dimension (d_h) | 128 |
| KV Compression Dimension (d_c) | 512 |
| Query Compression Dimension (d'_c) | 1,536 |
| Decoupled Key/Query Per-head Dim (d^R_h) | 64 |
| Shared Experts (N_s) | 1 |
| Routed Experts (N_r) | 256 |
| Activated Routed Experts (K_r) | 8 |
| Expert Intermediate Hidden Dim | 2,048 |
| Node-Limited Routing (M) | 4 nodes |
| MTP Depth (D) | 1 |
| Vocabulary Size | 128,000 |
| Context Length | 128K (after extension) |

The first 3 layers use dense FFNs; the remaining 58 layers use MoE with 1 shared expert + 256 routed experts, 8 activated per token (Section 4.2).

### Key Technical Components

#### Multi-head Latent Attention (MLA)

MLA performs low-rank joint compression for keys and values (Section 2.1.1). The compressed latent vector c^KV_t has dimension d_c = 512, compared to d_h * n_h = 16,384 for standard MHA:

> c^KV_t = W^DKV * h_t (Eq. 1)

Keys and values are then reconstructed via up-projection:

> k^C_t = W^UK * c^KV_t (Eq. 2)
> v^C_t = W^UV * c^KV_t (Eq. 5)

A separate decoupled key k^R_t carries RoPE information:

> k^R_t = RoPE(W^KR * h_t) (Eq. 3)

The final key concatenates compressed and RoPE components: k_{t,i} = [k^C_{t,i}; k^R_t] (Eq. 4). During inference, only c^KV_t (512 dimensions) and k^R_t (64 dimensions) need caching, achieving significant KV cache reduction.

Query compression uses d'_c = 1,536 dimensions with similar structure:

> c^Q_t = W^DQ * h_t (Eq. 6)
> q^C_t = W^UQ * c^Q_t (Eq. 7)
> q^R_t = RoPE(W^QR * c^Q_t) (Eq. 8)

The attention output is computed as:

> o_{t,i} = sum_j Softmax_j(q^T_{t,i} * k_{j,i} / sqrt(d_h + d^R_h)) * v^C_{j,i} (Eq. 10)
> u_t = W^O [o_{t,1}; ...; o_{t,n_h}] (Eq. 11)

#### DeepSeekMoE with Auxiliary-Loss-Free Load Balancing

The MoE layer combines shared experts with routed experts (Section 2.1.2):

> h'_t = u_t + sum_{i=1}^{N_s} FFN^(s)_i(u_t) + sum_{i=1}^{N_r} g_{i,t} * FFN^(r)_i(u_t) (Eq. 12)

Token-to-expert affinity uses sigmoid (not softmax, differing from DeepSeek-V2):

> s_{i,t} = Sigmoid(u_t^T * e_i) (Eq. 15)

Gating values are normalized among selected experts:

> g_{i,t} = s'_{i,t} / sum_j s'_{j,t} (Eq. 13)

**Auxiliary-loss-free load balancing** adds a learned bias b_i to routing decisions without affecting gating values:

> s'_{i,t} = s_{i,t} if (s_{i,t} + b_i) in TopK, else 0 (Eq. 16)

The bias is dynamically adjusted: decreased by gamma if the expert is overloaded, increased by gamma if underloaded, where gamma = 0.001 for the first 14.3T tokens and 0.0 for the remaining 500B tokens (Section 4.2). The gating value remains derived from the original affinity score s_{i,t}, not the biased score.

**Complementary sequence-wise auxiliary loss** with extremely small alpha = 0.0001 prevents within-sequence imbalance:

> L_Bal = alpha * sum_{i=1}^{N_r} f_i * P_i (Eq. 17)

where f_i measures the fraction of tokens routed to expert i (Eq. 18) and P_i is the average token-level probability allocated to expert i (Eq. 19-20).

**Node-limited routing** ensures each token is sent to at most M = 4 nodes, selected by summing the highest K_r/M affinity scores per node. This bounds cross-node communication while allowing selection of up to 3.2 experts per node on average within NVLink bandwidth (Section 3.2.2).

**No token-dropping:** Due to effective load balancing, DeepSeek-V3 does not drop any tokens during training or inference (Section 2.1.2).

#### Multi-Token Prediction (MTP)

MTP uses D = 1 sequential module to predict one additional token (Section 2.2). The k-th MTP module combines the representation from the (k-1)-th depth with the embedding of the (i+k)-th token:

> h'^k_i = M_k * [RMSNorm(h^{k-1}_i); RMSNorm(Emb(t_{i+k}))] (Eq. 21)

This serves as input to a Transformer block:

> h^k_{1:T-k} = TRM_k(h'^k_{1:T-k}) (Eq. 22)

The shared output head computes the prediction probability:

> P^k_{i+k+1} = OutHead(h^k_i) (Eq. 23)

Both the embedding layer and output head are **shared** with the main model. The MTP training objective computes cross-entropy for each depth:

> L^k_MTP = CrossEntropy(P^k_{2+k:T+1}, t_{2+k:T+1}) (Eq. 24)

The overall MTP loss is:

> L_MTP = (lambda/D) * sum_{k=1}^{D} L^k_MTP (Eq. 25)

The MTP loss weight lambda = 0.3 for the first 10T tokens, then 0.1 for the remaining 4.8T tokens (Section 4.2). Unlike Gloeckle et al. (2024), which predicts D additional tokens in parallel with independent output heads, DeepSeek-V3 predicts them sequentially, maintaining the complete causal chain at each prediction depth.

#### DualPipe Algorithm

DualPipe is a novel bidirectional pipeline parallelism algorithm (Section 3.2.1) that divides each chunk into four components: attention, all-to-all dispatch, MLP, and all-to-all combine. For backward chunks, both attention and MLP are further split into backward-for-input and backward-for-weights. The algorithm feeds micro-batches from both ends of the pipeline simultaneously, achieving near-zero all-to-all communication overhead through computation-communication overlap.

| Method | Bubble | Parameter Memory | Activation Memory |
|--------|--------|-----------------|-------------------|
| 1F1B | (PP-1)(F+B) | 1x | PP |
| ZB1P | (PP-1)(F+B-2W) | 1x | PP |
| DualPipe | (PP/2 - 1)(F&B + B - 3W) | 2x | PP + 1 |

(Table 2, Section 3.2.1. F = forward chunk time, B = full backward chunk time, W = backward-for-weights time, F&B = overlapped forward and backward time.)

DualPipe significantly reduces pipeline bubbles compared to 1F1B and ZB1P while only increasing peak activation memory by 1/PP. The 2x parameter memory is mitigated by the large EP size used during training (Section 3.2.1).

#### FP8 Mixed Precision Training

DeepSeek-V3 validates FP8 training at extreme scale (Section 3.3):

- **Quantized in FP8:** GEMM operations (Fprop, Dgrad, Wgrad) in E4M3 format for all three passes (unlike prior work using E5M2 for backward)
- **Higher precision retained:** Embedding module, output head, MoE gating modules, normalization operators, and attention operators in BF16/FP32
- **Fine-grained quantization:** 1x128 tile-wise for activations, 128x128 block-wise for weights (Section 3.3.2)
- **Accumulation precision fix:** Promote to FP32 every N_C = 128 elements to compensate for H800's ~14-bit accumulation precision (Section 3.3.2)
- **Online quantization:** Maximum absolute value computed online for each tile/block (not delayed quantization)
- **Low-precision optimizer states:** BF16 for AdamW first/second moments; master weights and gradients in FP32 (Section 3.3.3)

Relative loss error vs BF16 baseline: < 0.25% on both ~16B and ~230B MoE models (Appendix B.1).

#### Hardware Design Suggestions

The paper provides recommendations for future AI hardware (Section 3.5):
- **Communication hardware:** Offload all-to-all communication from SMs (currently 20 out of 132 SMs dedicated) to a dedicated co-processor; unify IB and NVLink interfaces
- **Compute hardware:** Higher FP8 GEMM accumulation precision in Tensor Cores; native support for tile- and block-wise quantization; fused FP8 cast with TMA access for online quantization; support for transposed GEMM operations

### Experimental Setup

**Pre-training hardware and framework (Section 3.1, 3.2):**
- 2,048 NVIDIA H800 GPUs (8 per node, NVLink 160 GB/s within nodes, IB 50 GB/s between nodes)
- 16-way Pipeline Parallelism, 64-way Expert Parallelism (8 nodes), ZeRO-1 Data Parallelism
- No Tensor Parallelism required (memory savings from recomputation + FP8 storage)

**Pre-training hyperparameters (Section 4.2):**
- Optimizer: AdamW (beta_1 = 0.9, beta_2 = 0.95, weight_decay = 0.1)
- Peak LR: 2.2 x 10^-4
- Warmup: 2K steps linear ramp
- Schedule: Constant until 10T tokens, cosine decay to 2.2 x 10^-5 over 4.3T tokens, then constant at 2.2 x 10^-5 for 333B tokens, then 7.3 x 10^-6 for final 167B tokens
- Batch size: 3,072 -> 15,360 (ramped over first 469B tokens)
- Sequence length: 4K during pre-training
- Gradient clipping norm: 1.0

**Data (Section 4.1):** 14.8T tokens with enhanced math/code ratio vs DeepSeek-V2. Byte-level BPE tokenizer (128K vocab). Fill-in-Middle (PSM framework) at rate 0.1. Document packing without cross-sample attention masking.

**Context extension (Section 4.3):** Two-stage YaRN extension:
1. 4K -> 32K: 1,000 steps, batch size 1,920, LR 7.3 x 10^-6
2. 32K -> 128K: 1,000 steps, batch size 480, LR 7.3 x 10^-6

YaRN applied only to decoupled shared key k^R_t with scale s = 40, alpha = 1, beta = 32, scaling factor sqrt(t) = 0.1 ln(s) + 1.

**Post-training (Section 5.1, 5.2):**
- **SFT:** 1.5M instances, 2 epochs, cosine LR decay from 5 x 10^-6 to 1 x 10^-6, sample masking for packed sequences
- **RL:** Group Relative Policy Optimization (GRPO), which forgoes a critic model and estimates the baseline from group scores:

> J_GRPO(theta) = E[1/G * sum_{i=1}^{G} (min(r_theta * A_i, clip(r_theta, 1-epsilon, 1+epsilon) * A_i) - beta * D_KL(pi_theta || pi_ref))] (Eq. 26)

where A_i = (r_i - mean(r)) / std(r) (Eq. 28) and D_KL uses the reverse form (Eq. 27).

- Rule-based rewards for verifiable tasks (math, code via compiler)
- Model-based rewards for free-form answers, trained from DeepSeek-V3 SFT checkpoints with chain-of-thought reasoning

**Reasoning data distillation (Section 5.4.1):** Reasoning SFT data generated by internal DeepSeek-R1 model series. Two types of SFT samples: <problem, original response> and <system prompt, problem, R1 response>. Expert model trained via SFT+RL pipeline, then used for rejection sampling to produce final SFT data.

**Deployment (Section 3.4):**
- Prefilling: minimum 4 nodes (32 GPUs), TP4+SP with DP8, EP32, 32 redundant experts
- Decoding: minimum 40 nodes (320 GPUs), TP4+SP with DP80, EP320, each GPU hosts 1 expert

**Reproducibility:** Code and model weights are publicly available at https://github.com/deepseek-ai/DeepSeek-V3 and https://huggingface.co/deepseek-ai/DeepSeek-V3. No variance estimates reported for benchmark results. Benchmarks with <1000 samples tested multiple times with varying temperature (Section 5.3.1). Seeds not reported.

### Key Results

**Training Costs (Table 1, Section 1):**

| Phase | H800 GPU Hours | USD (at $2/hr) |
|-------|----------------|----------------|
| Pre-Training | 2,664K | $5.328M |
| Context Extension | 119K | $0.238M |
| Post-Training | 5K | $0.01M |
| **Total** | **2,788K** | **$5.576M** |

Training efficiency: 180K H800 GPU hours per trillion tokens (~3.7 days on 2,048 GPUs).

**Base Model Performance (Table 3, Section 4.4.2):**

| Benchmark (Metric) | # Shots | DeepSeek-V2 Base | Qwen2.5 72B Base | LLaMA-3.1 405B Base | DeepSeek-V3 Base |
|---|---|---|---|---|---|
| Pile-test (BPB) | - | 0.606 | 0.638 | 0.542 | 0.548 |
| BBH (EM) | 3-shot | 78.8 | 79.8 | 82.9 | **87.5** |
| MMLU (EM) | 5-shot | 78.4 | 85.0 | 84.4 | **87.1** |
| MMLU-Redux (EM) | 5-shot | 75.6 | 83.2 | 81.3 | **86.2** |
| MMLU-Pro (EM) | 5-shot | 51.4 | 58.3 | 52.8 | **64.4** |
| DROP (F1) | 3-shot | 80.4 | 80.6 | 86.0 | **89.0** |
| HellaSwag (EM) | 10-shot | 87.1 | 84.8 | **89.2** | 88.9 |
| PIQA (EM) | 0-shot | 83.9 | 82.6 | **85.9** | 84.7 |
| WinoGrande (EM) | 5-shot | **86.3** | 82.3 | 85.2 | 84.9 |
| TriviaQA (EM) | 5-shot | 80.0 | 71.9 | 82.7 | **82.9** |
| NaturalQuestions (EM) | 5-shot | 38.6 | 33.2 | **41.5** | 40.0 |
| AGIEval (EM) | 0-shot | 57.5 | 75.8 | 60.6 | **79.6** |
| HumanEval (Pass@1) | 0-shot | 43.3 | 53.0 | 54.9 | **65.2** |
| MBPP (Pass@1) | 3-shot | 65.0 | 72.6 | 68.4 | **75.4** |
| LiveCodeBench-Base (Pass@1) | 3-shot | 11.6 | 12.9 | 15.5 | **19.4** |
| GSM8K (EM) | 8-shot | 81.6 | 88.3 | 83.5 | **89.3** |
| MATH (EM) | 4-shot | 43.4 | 54.4 | 49.0 | **61.6** |
| MGSM (EM) | 8-shot | 65.6 | 76.2 | 69.9 | **79.8** |
| C-Eval (EM) | 5-shot | 81.4 | **89.2** | 72.5 | 90.1 |
| CMMLU (EM) | 5-shot | 84.0 | **89.5** | 73.7 | 88.8 |
| MMMLU-non-English (EM) | 5-shot | 64.0 | 74.8 | 73.8 | **79.4** |

DeepSeek-V3-Base outperforms all other open-source base models on most benchmarks with only 37B activated parameters, compared to 72B (Qwen2.5) and 405B (LLaMA-3.1) dense models. LLaMA-3.1-405B retains an edge on HellaSwag, PIQA, and NaturalQuestions (moderate evidence -- single evaluation framework, no variance reported).

**Chat Model Performance (Table 6, Section 5.3.2):**

| Benchmark | DeepSeek-V3 | GPT-4o-0513 | Claude-3.5-Sonnet-1022 | LLaMA-3.1-405B | Qwen2.5-72B |
|-----------|-------------|-------------|------------------------|----------------|-------------|
| MMLU (EM) | **88.5** | 87.2 | 88.3 | 88.6 | 85.3 |
| MMLU-Redux (EM) | **89.1** | 88.0 | 88.9 | 86.2 | 85.6 |
| MMLU-Pro (EM) | 75.9 | 72.6 | **78.0** | 73.3 | 71.6 |
| DROP (3-shot F1) | **91.6** | 83.7 | 88.3 | 88.7 | 76.7 |
| GPQA-Diamond (Pass@1) | 59.1 | 49.9 | **65.0** | 51.1 | 49.0 |
| SimpleQA (Correct) | 24.9 | **38.2** | 28.4 | 17.1 | 9.1 |
| IF-Eval (Prompt-Strict) | 86.1 | 84.3 | **86.5** | 86.0 | 84.1 |
| LongBench v2 (Acc.) | **48.7** | 48.1 | 41.0 | 36.1 | 39.4 |
| FRAMES (Acc.) | 73.3 | **80.5** | 72.5 | 70.0 | 69.8 |
| HumanEval-Mul (Pass@1) | **82.6** | 80.5 | 81.7 | 77.2 | 77.3 |
| LiveCodeBench-COT (Pass@1) | **40.5** | 33.4 | 36.3 | 28.4 | 31.1 |
| Codeforces (Percentile) | **51.6** | 23.6 | 20.3 | 25.3 | 24.8 |
| SWE-Bench Verified (Resolved) | 42.0 | 38.8 | **50.8** | 24.5 | 23.8 |
| Aider-Polyglot (Acc.) | **49.6** | 16.0 | 45.3 | 5.8 | 7.6 |
| AIME 2024 (Pass@1) | **39.2** | 9.3 | 16.0 | 23.3 | 23.3 |
| MATH-500 (EM) | **90.2** | 74.6 | 78.3 | 73.8 | 80.0 |
| CNMO 2024 (Pass@1) | **43.2** | 10.8 | 13.1 | 6.8 | 15.9 |
| C-SimpleQA (Correct) | **64.8** | 59.3 | 51.3 | 50.4 | 48.4 |

DeepSeek-V3 achieves the strongest performance among open-source models and is competitive with frontier closed-source models across all categories. It leads substantially on math (MATH-500, AIME, CNMO), competitive coding (Codeforces, LiveCodeBench), and Chinese knowledge (C-SimpleQA). Claude-3.5-Sonnet leads on GPQA-Diamond and SWE-Bench Verified; GPT-4o leads on SimpleQA and FRAMES (single evaluation, no variance reported).

**Open-Ended Evaluation (Table 7, Section 5.3.3):**

| Model | Arena-Hard | AlpacaEval 2.0 (LC Win Rate) |
|---|---|---|
| DeepSeek-V3 | **85.5** | **70.0** |
| Claude-3.5-Sonnet-1022 | 85.2 | 52.0 |
| GPT-4o-0513 | 80.4 | 51.1 |
| Qwen2.5-72B-Instruct | 81.2 | 49.1 |
| LLaMA-3.1 405B | 69.3 | 40.5 |

DeepSeek-V3 is the first open-source model to surpass 85% on Arena-Hard, performing on par with Claude-3.5-Sonnet-1022 (GPT-4-Turbo-1106 as judge; limited evidence -- single judge model).

**RewardBench Performance (Table 8, Section 5.3.4):**

| Model | Chat | Chat-Hard | Safety | Reasoning | Average |
|---|---|---|---|---|---|
| DeepSeek-V3 | 96.9 | 79.8 | 87.0 | 84.3 | 87.0 |
| DeepSeek-V3 (maj@6) | 96.9 | 82.6 | 89.5 | 89.2 | **89.6** |
| Claude-3.5-Sonnet-1022 | 96.4 | 79.7 | 91.1 | 87.6 | 88.7 |
| GPT-4o-0806 | 96.1 | 76.1 | 88.1 | 86.6 | 86.7 |

DeepSeek-V3 with majority voting (maj@6) achieves the highest RewardBench average, surpassing Claude-3.5-Sonnet-1022 (Section 5.3.4).

**MTP Ablation (Table 4, Section 4.5.1):**

| Benchmark | Small MoE Baseline | Small MoE w/ MTP | Large MoE Baseline | Large MoE w/ MTP |
|---|---|---|---|---|
| # Total Params | 15.7B | 15.7B | 228.7B | 228.7B |
| # Training Tokens | 1.33T | 1.33T | 540B | 540B |
| HumanEval (Pass@1) | 20.7 | 26.8 (+6.1) | 44.5 | **53.7** (+9.2) |
| MBPP (Pass@1) | 35.8 | 36.8 (+1.0) | 61.6 | 62.2 (+0.6) |
| GSM8K (EM) | 25.4 | 31.4 (+6.0) | 72.3 | 74.0 (+1.7) |
| MATH (EM) | 10.7 | 12.6 (+1.9) | 38.6 | 39.8 (+1.2) |
| BBH (EM) | 39.0 | 41.4 (+2.4) | 70.0 | 70.7 (+0.7) |
| MMLU (EM) | 50.0 | 53.3 (+3.3) | 67.5 | 66.6 (-0.9) |

MTP consistently improves code and math benchmarks across scales. The improvement is larger at small scale. MMLU shows a slight regression for the large MoE (-0.9 points), the only benchmark where MTP slightly hurts. The MTP module is discarded during inference, so inference costs are identical (controlled ablation with same training data and architecture; moderate evidence -- two scales tested but no variance estimates).

**Auxiliary-Loss-Free Ablation (Table 5, Section 4.5.2):**

| Benchmark | Small MoE Aux-Loss-Based | Small MoE Aux-Loss-Free | Large MoE Aux-Loss-Based | Large MoE Aux-Loss-Free |
|---|---|---|---|---|
| # Total Params | 15.7B | 15.7B | 228.7B | 228.7B |
| # Training Tokens | 1.33T | 1.33T | 578B | 578B |
| HumanEval (Pass@1) | 22.0 | 22.6 (+0.6) | 40.2 | **46.3** (+6.1) |
| GSM8K (EM) | 27.1 | 29.6 (+2.5) | 70.7 | **74.5** (+3.8) |
| MATH (EM) | 10.9 | 11.1 (+0.2) | 37.2 | **39.6** (+2.4) |
| Pile-test (BPB) | 0.727 | 0.724 (-0.003) | 0.656 | **0.652** (-0.004) |
| MMLU (EM) | 51.0 | 51.8 (+0.8) | 68.3 | 67.2 (-1.1) |

The auxiliary-loss-free strategy consistently improves performance on most benchmarks, with larger gains at the large scale. Similar to MTP, MMLU shows a slight regression for the large MoE (controlled ablation, same data, moderate evidence -- two scales tested).

**Batch-wise vs Sequence-wise Load Balance (Section 4.5.3):**

The key advantage of auxiliary-loss-free balancing is that it operates at batch level rather than sequence level, allowing greater expert specialization. Validation losses on 1B MoE models: sequence-wise auxiliary loss = 2.258, auxiliary-loss-free = 2.253, batch-wise auxiliary loss = 2.253. On 3B MoE models: sequence-wise = 2.085, auxiliary-loss-free = 2.080, batch-wise auxiliary loss = 2.080. Batch-wise auxiliary loss achieves the same performance as auxiliary-loss-free, confirming that the performance advantage comes from batch-level vs sequence-level balancing scope, not from the absence of loss terms per se.

**Distillation from DeepSeek-R1 (Table 9, Section 5.4.1):**

| Model | LiveCodeBench-CoT (Pass@1) | LiveCodeBench-CoT (Length) | MATH-500 (Pass@1) | MATH-500 (Length) |
|---|---|---|---|---|
| DeepSeek-V2.5 Baseline | 31.1 | 718 | 74.6 | 769 |
| DeepSeek-V2.5 +R1 Distill | **37.4** | 783 | **83.2** | 1510 |

Distillation from R1 improves LiveCodeBench by +6.3 points and MATH-500 by +8.6 points, but approximately doubles the average response length for MATH-500 (718->783 for code, 769->1510 for math). This trade-off between accuracy and response length was carefully balanced for the final DeepSeek-V3 (limited evidence -- single model, two benchmarks).

**MTP Inference (Section 5.4.3):** Second-token acceptance rate ranges 85-90% across various generation topics, enabling 1.8x TPS via speculative decoding.

---

## Limitations and Failure Modes

The paper acknowledges the following limitations (Section 6):

1. **Large deployment unit.** Prefilling requires minimum 4 nodes (32 GPUs); decoding requires minimum 40 nodes (320 GPUs). This poses a burden for small teams.

2. **Inference speed.** Despite achieving 2x improvement over DeepSeek-V2, further optimization potential remains.

The paper expects these limitations to be "naturally addressed with the development of more advanced hardware" (Section 6).

**Benchmarks where DeepSeek-V3 underperforms:**
- **SimpleQA:** 24.9% vs GPT-4o's 38.2% and Claude-3.5-Sonnet's 28.4% (Table 6). Authors attribute this to resource allocation toward Chinese knowledge.
- **SWE-Bench Verified:** 42.0% vs Claude-3.5-Sonnet's 50.8% (Table 6).
- **GPQA-Diamond:** 59.1% vs Claude-3.5-Sonnet's 65.0% (Table 6).
- **FRAMES:** 73.3% vs GPT-4o's 80.5% (Table 6).
- **RACE-High (base model):** 51.3% vs LLaMA-3.1-405B's 56.8% (Table 3).
- **HellaSwag, PIQA (base model):** Slightly behind LLaMA-3.1-405B (Table 3).

**[Inferred] Limitations not explicitly acknowledged by the authors:**
- **[Inferred]** Math performance improvements are partially confounded by distillation from DeepSeek-R1 (Section 5.4.1), making it difficult to attribute gains purely to architectural innovations vs knowledge transfer.
- **[Inferred]** No variance estimates or confidence intervals reported for any benchmark, despite using temperature=0.7 with 16 runs for AIME/CNMO (single evaluation framework).
- **[Inferred]** Block-wise quantization of activation gradients leads to model divergence (Appendix B.2), indicating FP8 training requires careful per-operation precision choices that may not generalize straightforwardly.

#### Scope and Comparability

- **What was not tested:** No evaluation on languages beyond English and Chinese (despite multilingual tokenizer). No ablation of MLA vs GQA on long-context tasks beyond NIAH. No comparison of FP8 vs BF16 at the full 671B scale (FP8 validation only at ~16B and ~230B). No exploration of MTP depth D > 1 at the full model scale.
- **Comparability notes:** DeepSeek-V3 activates 37B parameters per token vs LLaMA-3.1-405B's 405B dense parameters, making per-token FLOP comparisons asymmetric. Training cost comparisons exclude prior research and ablation costs, which the authors note explicitly (Section 1). The AIME/CNMO results use temperature=0.7 averaged over 16 runs while MATH-500 uses greedy decoding, so math benchmark results are not directly comparable to each other. Codeforces evaluation is based on percentile ranking, which depends on the competitor pool.

---

## Conclusions

### Contributions

1. **First validated FP8 training at extreme scale.** Fine-grained quantization with tile-wise (1x128) activation scaling and block-wise (128x128) weight scaling, combined with FP32 accumulation every 128 elements, achieves <0.25% relative loss error vs BF16 at ~16B and ~230B scales. E4M3 format used throughout (not hybrid E4M3/E5M2) enabled by fine-grained scaling (Section 3.3, Appendix B.1).

2. **Auxiliary-loss-free load balancing with greater expert specialization.** Dynamic bias adjustment achieves better downstream performance than auxiliary-loss methods (+3.8 points on GSM8K, +6.1 on HumanEval for large MoE) while enabling domain-specific expert specialization visible across all layers (Section 2.1.2, Table 5, Appendix C).

3. **Multi-token prediction for training and inference.** Sequential MTP improves downstream performance (+9.2 points on HumanEval for large MoE) and enables 1.8x inference throughput via speculative decoding with 85-90% acceptance rate (Section 2.2, Table 4, Section 5.4.3).

4. **Order-of-magnitude training cost reduction.** Full training in 2.788M H800 GPU hours ($5.576M at $2/hr) while achieving frontier performance, enabled by MoE architecture, FP8 training, DualPipe, and efficient communication overlap (Table 1, Section 1).

5. **Remarkable training stability.** No irrecoverable loss spikes or rollbacks throughout 14.8T token pre-training, attributed to effective load balancing and FP8 training framework (Section 1).

6. **Successful knowledge distillation from reasoning models.** Distilling reasoning capability from DeepSeek-R1 series into a standard LLM, incorporating reflection and verification patterns while maintaining concise output style (Section 5.4.1, Table 9).

### Implications

1. **MoE efficiency is practically achievable at frontier scale.** The combination of MLA, auxiliary-loss-free load balancing, node-limited routing, DualPipe, and FP8 training demonstrates that MoE communication overhead can be effectively managed to achieve frontier performance at a fraction of dense model cost.

2. **FP8 training is viable for production models.** The successful 671B parameter FP8 training suggests future models may default to lower precision, though the paper notes that H800 accumulation precision is a workaround and future hardware should provide native support (Section 3.5.2). (Speculative -- longer training runs or different architectures may reveal stability issues.)

3. **Reasoning distillation as a scalable post-training technique.** The R1 distillation approach suggests that long-CoT reasoning capabilities can be transferred to standard models without requiring them to always produce long chains of thought, potentially applicable beyond math and code domains (speculative).

4. **Batch-wise load balancing enables expert specialization.** The finding that batch-wise balancing outperforms sequence-wise balancing suggests MoE models benefit from allowing domain-specific expert selection within individual sequences (Section 4.5.3).

---

## Key Claims

1. **DeepSeek-V3 achieves 88.5% on MMLU, matching frontier closed-source models.** Competitive with GPT-4o (87.2%), Claude-3.5-Sonnet (88.3%), and LLaMA-3.1-405B (88.6%). Evidence: Table 6, Section 5.3.2. Status: **supported**. Scope: Chat model, simple-evals prompts, max 8K output. Magnitude: 88.5% vs 87.2-88.6% range. Single evaluation, no variance reported (limited evidence on stability of result).

2. **Training costs are dramatically lower than comparable models.** 2.788M H800 GPU hours total ($5.576M), compared to estimated costs for dense models at comparable performance levels. Evidence: Table 1, Section 1. Status: **supported**. Scope: Excludes prior research and ablation costs. Magnitude: $5.576M total. Single training run (limited evidence on reproducibility of cost).

3. **Auxiliary-loss-free load balancing outperforms auxiliary-loss methods.** +3.8 points on GSM8K (74.5% vs 70.7%), +6.1 points on HumanEval (46.3% vs 40.2%) for large MoE. Evidence: Table 5, Section 4.5.2. Status: **supported**. Scope: Controlled ablation at 15.7B and 228.7B scales with same training data. Magnitude: +3.8 GSM8K, +6.1 HumanEval, -1.1 MMLU. Ablation across two scales (moderate evidence).

4. **MTP improves performance on code generation and math.** +9.2 points on HumanEval (53.7% vs 44.5%), +1.7 points on GSM8K, +1.2 points on MATH for large MoE. Evidence: Table 4, Section 4.5.1. Status: **supported**. Scope: MTP depth D=1, ablation at 15.7B and 228.7B scales. Magnitude: +9.2 HumanEval, -0.9 MMLU (slight regression). Ablation across two scales (moderate evidence).

5. **Training was completely stable with no rollbacks.** Zero irrecoverable loss spikes throughout 14.8T token pre-training. Evidence: Section 1, Abstract. Status: **supported**. Scope: Single training run of one model configuration. Magnitude: Zero rollbacks. Single run (limited evidence on generalizability to other configurations).

6. **Perfect NIAH retrieval up to 128K context.** Figure 8 shows consistent score ~10/10 across all depths and context lengths after YaRN extension and SFT. Evidence: Figure 8, Section 4.3. Status: **supported**. Scope: After two-stage YaRN context extension, post-SFT. Magnitude: Score ~10/10 uniformly. Single benchmark (limited evidence on broader long-context quality).

7. **DeepSeek-V3 outperforms all non-o1-like models on MATH-500 and competitive math benchmarks.** 90.2% MATH-500 vs 78.3% Claude-3.5-Sonnet and 74.6% GPT-4o; 39.2% AIME 2024 vs 23.3% next best. Evidence: Table 6, Figure 1. Status: **supported**. Scope: Non-long-CoT models. Math improvements partially attributed to DeepSeek-R1 distillation (Section 5.4.1). Magnitude: +11.9 points over Claude-3.5-Sonnet on MATH-500. AIME/CNMO averaged over 16 runs at temp=0.7 (moderate evidence).

8. **FP8 mixed precision training achieves <0.25% relative loss error vs BF16.** Validated on ~16B and ~230B MoE models trained on 1.33T and ~0.9T tokens respectively. Evidence: Section 3.3, Appendix B.1, Figure 10. Status: **supported**. Scope: Validated at two sub-scales (not at full 671B scale for BF16 comparison). Magnitude: <0.25% relative loss error. Two model scales (moderate evidence, but not validated at full 671B scale).

9. **Distillation from DeepSeek-R1 significantly improves reasoning.** +6.3 points on LiveCodeBench-CoT (37.4% vs 31.1%), +8.6 points on MATH-500 (83.2% vs 74.6%), with response length roughly doubling for math. Evidence: Table 9, Section 5.4.1. Status: **supported**. Scope: Ablated on DeepSeek-V2.5 (not V3), two benchmarks only. Magnitude: +6.3 LiveCodeBench, +8.6 MATH-500. Single model (limited evidence).

10. **MTP enables 1.8x inference throughput via speculative decoding.** 85-90% acceptance rate for second token across various generation topics. Evidence: Section 5.4.3. Status: **supported**. Scope: Various generation topics, speculative decoding framework. Magnitude: 1.8x TPS, 85-90% acceptance rate. No detailed breakdown by task type (limited evidence on variability).

---

## Open Questions

1. **Scaling stability.** Would training stability hold at >1T total parameters, or would new instabilities emerge? The paper demonstrates zero rollbacks at 671B but provides no theoretical analysis of why stability was achieved.

2. **Generalizability of auxiliary-loss-free balancing.** Can the dynamic bias approach transfer to other MoE architectures (e.g., Mixtral, Switch Transformer) with different expert granularity and routing mechanisms?

3. **MLA vs GQA for long-context.** Does MLA's low-rank compression affect retrieval quality at extreme context lengths beyond the relatively simple NIAH test? No evaluation on more challenging long-context benchmarks (e.g., RULER, LongBench tasks beyond v2) for the base model.

4. **Attribution of math gains.** How much of the math improvement comes from architectural innovations (MTP, auxiliary-loss-free balancing) vs DeepSeek-R1 distillation? The distillation ablation (Table 9) is on DeepSeek-V2.5, not V3, leaving this question partially unresolved.

5. **Deployment efficiency.** Can the minimum deployment unit (32-320 GPUs) be reduced through model compression, expert pruning, or next-generation hardware to make DeepSeek-V3 accessible to smaller teams?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Base Transformer architecture that DeepSeek-V3 builds upon with MLA and MoE modifications.
- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Source of RoPE, used in MLA's decoupled key/query components.

### Mixture-of-Experts Foundations

- **Shazeer et al. (2017)** -- *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.* Foundational MoE architecture; DeepSeek-V3 addresses the routing collapse problem they identified.
- **Fedus et al. (2021)** -- *Switch Transformers.* Auxiliary loss approach for MoE load balancing that DeepSeek-V3's auxiliary-loss-free strategy aims to improve upon.
- **Lepikhin et al. (2021)** -- *GShard.* Traditional MoE architecture (GShard) that DeepSeekMoE improves with finer-grained and shared experts; also source of Expert Parallelism.

### Direct Predecessors

- **DeepSeek-AI (2024c)** -- *DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model.* Direct predecessor introducing MLA and DeepSeekMoE architectures that V3 inherits and refines.
- **Dai et al. (2024)** -- *DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models.* Source of the DeepSeekMoE architecture with finer-grained and shared experts.
- **Wang et al. (2024a)** -- *Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts.* Prior work on auxiliary-loss-free balancing that DeepSeek-V3's dynamic bias approach builds on.

### Context Extension

- **Peng et al. (2023a)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Context extension method used for two-stage 4K->32K->128K expansion.

### Multi-Token Prediction

- **Gloeckle et al. (2024)** -- *Better & Faster Large Language Models via Multi-token Prediction.* Concurrent work on MTP using parallel independent heads; DeepSeek-V3's sequential variant maintains causal chains.
- **Li et al. (2024b)** -- *EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty.* Source of the causal chain maintenance principle used in MTP implementation.

### Low-Precision Training

- **Dettmers et al. (2022)** -- Low-precision training techniques. Foundational work on quantized training that DeepSeek-V3's FP8 framework extends.
- **Thakkar et al. (2023)** -- Strategy of promotion to CUDA Cores for higher precision in FP8 training, adopted in DeepSeek-V3.
- **Rouhani et al. (2023b)** -- Microscaling data formats. DeepSeek-V3's fine-grained quantization is consistent with this approach.

### Pipeline Parallelism

- **Qi et al. (2023b)** -- *ZeroBubble.* Source of backward splitting into input/weights components, used in DualPipe.
- **Harlap et al. (2018)** -- *1F1B Pipeline Parallelism.* Baseline pipeline method that DualPipe improves upon.

### Post-Training

- **Shao et al. (2024)** -- *Group Relative Policy Optimization.* RL algorithm used for DeepSeek-V3 post-training, replacing the critic model with group score baselines.
- **Bai et al. (2022)** -- *Constitutional AI.* Self-rewarding approach using model's own voting evaluation for alignment in open-ended tasks.

### Competing Models

- **Dubey et al. (2024)** -- *The Llama 3 Herd of Models.* Primary dense model comparison target (LLaMA-3.1-405B).
- **OpenAI (2024)** -- *GPT-4o.* Primary closed-source comparison target.
- **Anthropic (2024)** -- *Claude 3.5 Sonnet.* Primary closed-source comparison target.
- **Qwen (2024b)** -- *Qwen2.5.* Primary open-source dense model comparison target (72B).

### Evaluation Benchmarks

- **Kamradt (2023)** -- *Needle-in-a-Haystack.* Used to validate context extension with perfect retrieval up to 128K.
- **Hendrycks et al. (2021)** -- *MATH.* Primary math reasoning benchmark; DeepSeek-V3 achieves 90.2% on MATH-500.
- **Chen et al. (2021)** -- *HumanEval.* Primary code generation benchmark; used in both final evaluation and ablation studies.
- **Lambert et al. (2024)** -- *RewardBench.* Used to evaluate DeepSeek-V3's generative reward model capability.
- **Bai et al. (2024)** -- *LongBench v2.* Long-context evaluation benchmark; DeepSeek-V3 achieves best-in-class 48.7%.
