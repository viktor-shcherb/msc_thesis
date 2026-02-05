---
title: "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model"
authors: "DeepSeek-AI"
year: 2024
venue: "arXiv preprint 2405.04434"
paper_type: preprint
categories: ["model-release", "architecture", "attention-efficiency"]
scope: ["MoE language models", "KV cache compression", "efficient attention", "context extension"]
benchmarks_used: ["mmlu", "arc", "hellaswag", "winogrande", "piqa", "triviaqa", "natural-questions", "gsm8k", "math-hendrycks", "humaneval", "mbpp", "bbh", "agi-eval", "c-eval", "cmmlu", "ifeval", "mt-bench", "alpaca-eval"]
models_introduced: ["deepseek-v2", "deepseek-v2-lite"]
models_evaluated: ["llama-3-70b", "mixtral-8x7b", "qwen1.5-72b", "deepseek-67b"]
key_claims:
  - id: C1
    claim: "Multi-head Latent Attention (MLA) reduces KV cache by 93.3% compared to standard MHA while matching or exceeding MHA performance"
    evidence: "Section 2.1, Table 1 (KV cache: 2.4KB vs 36KB per token at d=5120), Table 11 ablation"
    status: supported
    scope: "DeepSeek-V2-Lite ablations, 1.8T token training"
    magnitude: "93.3% KV cache reduction"
  - id: C2
    claim: "DeepSeekMoE with fine-grained experts and shared experts achieves comparable or better performance than dense models with the same activated parameters"
    evidence: "Section 2.2, Table 12 ablation comparing 2 shared + 64 routed (K=6) vs baseline MoE configurations"
    status: supported
    scope: "DeepSeek-V2-Lite ablations"
  - id: C3
    claim: "DeepSeek-V2 achieves 42.5% of the training cost of DeepSeek 67B while achieving significantly better performance on MMLU (78.5 vs 71.3) and other benchmarks"
    evidence: "Section 4, Table 1, Table 4 cost comparison"
    status: supported
    magnitude: "57.5% training cost reduction, +7.2 MMLU points"
  - id: C4
    claim: "DeepSeek-V2 achieves 5.76x generation throughput compared to DeepSeek 67B on H800 cluster"
    evidence: "Section 4, deployment efficiency metrics"
    status: supported
    magnitude: "5.76x throughput improvement"
  - id: C5
    claim: "YaRN-extended DeepSeek-V2 supports 128K context length with continued declining perplexity up to 128K tokens"
    evidence: "Section 2.1.3, Figure 2"
    status: supported
    scope: "Extended from 4K base context via YaRN"
  - id: C6
    claim: "DeepSeek-V2 Chat outperforms all open-source chat models on AlpacaEval 2.0 (38.9%) and MT-Bench (8.97) at time of release"
    evidence: "Table 5, Section 4.3"
    status: supported
    scope: "May 2024 open-source models"
cross_references:
  - target: 2024-08-deepseek-moe
    type: extends
    detail: "DeepSeek-V2 builds upon the DeepSeekMoE architecture (fine-grained experts + shared expert isolation), extending it with Multi-head Latent Attention"
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "DeepSeek-V2 uses YaRN to extend context from 4K base to 128K, achieving continued perplexity decline at 128K"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "MLA uses decoupled RoPE where positional encoding is applied via separate key/query projections to maintain compatibility with low-rank KV compression"
  - target: 2023-10-mistral-7b
    type: extends
    detail: "DeepSeek-V2 uses Grouped-Query Attention concepts from Mistral in its MLA design; also uses sliding window attention inspiration for efficiency"
  - target: 2024-07-llama-3-herd-of-models
    type: concurrent
    detail: "Contemporary model release; Llama 3 70B achieves similar MMLU (79.5 vs 78.5) but without MoE efficiency benefits"
  - target: 2024-07-qwen2-technical-report
    type: concurrent
    detail: "Qwen2 72B released around same time; both use YaRN for context extension"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Built on Transformer architecture with novel MLA and DeepSeekMoE modifications"
open_questions:
  - question: "How does MLA perform on tasks requiring retrieval from very long contexts compared to standard attention?"
    addressed_by: null
  - question: "What is the optimal ratio of shared to routed experts for different model scales?"
    addressed_by: null
  - question: "Does the decoupled RoPE approach in MLA generalize to other attention variants?"
    addressed_by: null
---

# DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

**Authors:** DeepSeek-AI (DeepSeek)
**Date:** May 2024, arXiv:2405.04434

---

## Core Research Problem

Large language models face a fundamental tension between model capability and deployment efficiency. Larger models achieve better performance but require proportionally more compute for training and inference. Two key bottlenecks limit practical deployment:

1. **KV cache memory**: Standard Multi-Head Attention (MHA) requires storing key-value pairs for all tokens across all heads, scaling as O(n × d_h × n_h) per layer, which becomes prohibitive for long contexts.

2. **Activated parameters**: Dense models activate all parameters for every token, creating a linear relationship between model size and inference cost.

Prior work addressed these independently: Grouped-Query Attention (GQA) and Multi-Query Attention (MQA) reduce KV cache but sacrifice representational capacity; Mixture-of-Experts (MoE) reduces activated parameters but standard expert granularity limits flexibility.

**The core challenge is achieving strong model performance while simultaneously minimizing both KV cache memory and activated parameter count.**

---

## Problem Solutions

DeepSeek-V2 introduces two architectural innovations that jointly address both efficiency bottlenecks:

1. **Multi-head Latent Attention (MLA)**: Low-rank compression of KV pairs via a shared latent vector, reducing KV cache by 93.3% while maintaining MHA-level expressivity through decoupled RoPE.

2. **DeepSeekMoE**: Fine-grained expert segmentation (160 small experts vs. 16 large experts) combined with shared experts (2 per layer) that capture common knowledge, enabling better expert specialization.

3. **Device-limited routing**: Constrains expert selection to at most M devices per token, bounding communication overhead while preserving load balance.

---

## Approach Details

### Method

#### Multi-head Latent Attention (MLA)

Standard MHA computes:

> o_t = Σ_i Softmax((W_Q^i h_t)^T W_K^i H / √d_h) W_V^i H

where each head stores separate K and V vectors requiring n_h × d_h × 2 cache per token per layer.

MLA compresses KV pairs into a shared low-rank latent vector c_t^{KV}:

> c_t^{KV} = W_{DKV} h_t

where W_{DKV} ∈ R^{d_c × d} projects from hidden dimension d to compressed dimension d_c (d_c << n_h × d_h). Keys and values are reconstructed via:

> k_t^{C,i} = W_{UK}^i c_t^{KV}
> v_t^{C,i} = W_{UV}^i c_t^{KV}

**Only c_t^{KV} needs to be cached** (size d_c per token per layer), achieving 93.3% KV cache reduction (d_c = 512 vs. n_h × d_h = 128 × 128 = 16384 for standard attention with n_h=128, d_h=128).

**Decoupled RoPE**: Standard RoPE cannot be applied directly to low-rank KV because positional information would require storing position-dependent keys. MLA introduces decoupled RoPE:

> k_t^i = [k_t^{C,i}; k_t^{R,i}]

where k_t^{R,i} = RoPE(W_{KR} h_t) carries positional information via a separate low-dimensional projection (d_R dimensions). The query similarly has q_t^{R,i} = RoPE(W_{QR}^i c_t^Q). Only c_t^{KV} and k_t^R are cached.

#### DeepSeekMoE Architecture

Standard MoE replaces FFN with:

> h'_t = Σ_{i=1}^N g_i(h_t) FFN_i(h_t)

where g_i are gating weights and only top-K experts are activated.

DeepSeekMoE introduces two modifications:

1. **Fine-grained experts**: Instead of N large experts, use mN smaller experts (each with 1/m parameters) and activate mK of them. For DeepSeek-V2: m=2, so 160 routed experts (vs. 80 equivalent) with K_r=6 activated.

2. **Shared experts**: K_s experts are always activated regardless of routing:

> h'_t = Σ_{i=1}^{K_s} FFN_i^{(s)}(h_t) + Σ_{i=1}^{N_r} g_i(h_t) FFN_i^{(r)}(h_t)

DeepSeek-V2 uses K_s=2 shared experts per layer, capturing common knowledge and reducing redundancy among routed experts.

#### Device-Limited Routing

To bound communication cost in distributed inference, routing is constrained:

> g_i(h_t) = s_i(h_t) × 1_{Rank(D(i)) ≤ M}

where D(i) maps expert i to its device, and at most M=4 devices are selected per token. Within each device, only top-1 expert is activated. This ensures:
- At most M × n_D experts activated (M devices × 1 expert per device)
- Communication bounded by M all-to-all operations

### Key Technical Components

**Architecture specifications (DeepSeek-V2 236B):**
- 60 Transformer layers
- Hidden dimension d = 5120
- n_h = 128 attention heads with d_h = 128
- MLA: d_c = 512 (KV compression), d_R = 64 (RoPE), d'_c = 1536 (query compression)
- MoE: 2 shared + 160 routed experts per layer, intermediate size 1536 per expert
- K_r = 6 routed experts activated per token
- Total parameters: 236B; Activated parameters: 21B (8.9%)
- Vocabulary: 100K tokens

**DeepSeek-V2-Lite (16B/2.4B activated):**
- 27 layers, d = 2048, n_h = 16, d_h = 128
- MLA: d_c = 512, d_R = 64
- MoE: 2 shared + 64 routed experts, K_r = 6
- Total: 15.7B; Activated: 2.4B

### Theoretical Analysis

**KV cache comparison (per token per layer at d=5120, n_h=128, d_h=128):**

| Method | Cache Size | Reduction |
|--------|------------|-----------|
| MHA | 2 × n_h × d_h = 32,768 | baseline |
| GQA (8 groups) | 2 × 8 × d_h = 2,048 | 93.75% |
| MQA | 2 × d_h = 256 | 99.2% |
| MLA | d_c + d_R × n_h = 512 + 64 = 576 | 98.2% |

MLA achieves 93.3% reduction while maintaining per-head flexibility (unlike GQA/MQA which share KV across heads).

### Experimental Setup

**Pre-training:**
- Corpus: 8.1T tokens from diverse sources
- Context length: 4K tokens (base), extended to 128K via YaRN
- Hardware: Cluster of H800 GPUs
- Training cost: 42.5% of DeepSeek 67B training FLOPs
- Tokenizer: Byte-level BPE, 100K vocabulary

**Context extension:**
- YaRN applied to extend from 4K to 128K
- Two-stage training: 4K → 32K (1000 steps) → 128K (1000 steps)

**Alignment (DeepSeek-V2 Chat):**
- SFT: 1.5M examples covering math, code, writing, QA, safety
- RL: Group Relative Policy Optimization (GRPO) -- policy optimization without critic model
- GRPO samples G outputs per prompt, computes group advantage A_i = (r_i - mean(r)) / std(r), optimizes policy to maximize advantage

**Evaluation benchmarks:**
- English: MMLU, ARC, HellaSwag, WinoGrande, PIQA, TriviaQA, NQ, BBH, AGI-Eval
- Math: GSM8K, MATH
- Code: HumanEval, MBPP, CRUXEval
- Chinese: C-Eval, CMMLU
- Instruction following: IFEval, MT-Bench, AlpacaEval 2.0

### Key Results

**Base model comparison (standard benchmarks):**

| Model | Params (Active) | MMLU | GSM8K | MATH | HumanEval | BBH |
|-------|-----------------|------|-------|------|-----------|-----|
| DeepSeek-V2 | 236B (21B) | 78.5 | 79.2 | 43.6 | 81.1 | 78.9 |
| Llama 3 70B | 70B (70B) | 79.5 | 93.0 | 50.4 | 81.7 | 81.0 |
| Mixtral 8x22B | 141B (39B) | 77.8 | 78.6 | 41.8 | 46.3 | 78.4 |
| Qwen1.5 72B | 72B (72B) | 77.5 | 79.5 | 34.1 | 41.5 | 65.5 |
| DeepSeek 67B | 67B (67B) | 71.3 | 63.4 | 18.7 | 42.0 | 68.7 |

**Key observations:**
- DeepSeek-V2 matches Llama 3 70B on most benchmarks with 3.3x fewer activated parameters
- Significantly outperforms predecessor DeepSeek 67B (+7.2 MMLU, +15.8 GSM8K, +24.9 MATH)
- Achieves HumanEval 81.1% vs. Mixtral's 46.3%

**Chat model comparison:**

| Model | MT-Bench | AlpacaEval 2.0 |
|-------|----------|----------------|
| DeepSeek-V2 Chat | 8.97 | 38.9% |
| Llama 3 70B Instruct | 8.95 | 34.4% |
| Qwen1.5 72B Chat | 8.61 | 36.6% |
| Mixtral 8x22B Instruct | 8.66 | 30.9% |

**Efficiency metrics:**
- Training cost: 42.5% of DeepSeek 67B
- Generation throughput: 5.76x DeepSeek 67B (on H800 cluster)
- KV cache: 93.3% reduction vs. standard MHA

**MLA ablation (Table 11, DeepSeek-V2-Lite at 1.8T tokens):**

| Attention | KV Cache (per token) | Pile PPL | HellaSwag |
|-----------|---------------------|----------|-----------|
| MHA | 36KB | 7.13 | 72.4 |
| MLA | 2.4KB | 7.09 | 72.3 |

MLA matches MHA performance with 15x smaller KV cache.

**DeepSeekMoE ablation (Table 12):**
- Fine-grained (1/m=2 FFN size, mK activated) outperforms standard granularity
- Adding 2 shared experts improves over pure routed configuration
- Combined design achieves best accuracy-efficiency tradeoff

---

## Limitations and Failure Modes

**Acknowledged limitations:**
1. **Context extension validation**: While perplexity continues declining at 128K tokens, the paper does not evaluate on long-context benchmarks like RULER or Needle-in-a-Haystack to verify actual retrieval capability.

2. **Single architecture**: All experiments use the DeepSeek-V2 architecture; no cross-validation on other model families.

3. **Deployment constraints**: Device-limited routing with M=4 assumes specific cluster topology; efficiency gains may not transfer to different hardware configurations.

**Scope and comparability notes:**
- Comparison with Llama 3 is on release benchmarks only; Llama 3 may have advantages on other tasks
- Training data composition not disclosed, limiting reproducibility assessment
- GRPO alignment details provided but not compared to standard RLHF/DPO in controlled ablation

---

## Conclusions

### Contributions

1. **Multi-head Latent Attention (MLA)**: Novel attention mechanism achieving 93.3% KV cache reduction through low-rank compression with decoupled RoPE, matching MHA performance.

2. **DeepSeekMoE improvements**: Fine-grained expert segmentation and shared experts improve expert utilization and reduce redundancy.

3. **Efficient large-scale model**: 236B parameter model with only 21B activated parameters achieves competitive performance with dense 70B models at 42.5% training cost.

4. **GRPO alignment**: Critic-free RL alignment method achieving state-of-the-art open-source chat performance.

### Implications

1. **KV cache is compressible without quality loss**: MLA demonstrates that the full key-value representation is redundant; low-rank approximations suffice.

2. **MoE efficiency gains are real and practical**: With appropriate routing and load balancing, MoE achieves substantial efficiency improvements over dense models.

3. **Architecture innovation can substitute for scale**: DeepSeek-V2 achieves Llama 3 70B-level performance with fundamentally more efficient architecture rather than more data or compute.

---

## Key Claims

1. **C1**: MLA reduces KV cache by 93.3% (from 36KB to 2.4KB per token at d=5120) while matching MHA performance on perplexity and downstream tasks (Table 11, Section 2.1).

2. **C2**: Fine-grained experts (160 small vs. 80 large) combined with 2 shared experts per layer outperform standard MoE configurations (Table 12, Section 2.2).

3. **C3**: DeepSeek-V2 achieves 42.5% training cost of DeepSeek 67B with +7.2 MMLU points improvement (Table 4, Section 4).

4. **C4**: Generation throughput is 5.76x higher than DeepSeek 67B due to reduced activated parameters and KV cache (Section 4).

5. **C5**: YaRN extension to 128K context achieves continued perplexity decline, indicating successful context window expansion (Figure 2, Section 2.1.3).

6. **C6**: DeepSeek-V2 Chat achieves highest MT-Bench (8.97) and AlpacaEval 2.0 (38.9%) among open-source models at release (Table 5).

---

## Open Questions

1. **Long-context retrieval capability**: Does MLA's compressed representation preserve retrieval accuracy on needle-in-a-haystack and multi-hop reasoning tasks at 128K context?

2. **Optimal expert configuration**: What is the optimal ratio of shared to routed experts, and fine-grained expert count, for different model scales?

3. **Decoupled RoPE generalization**: Does the decoupled RoPE approach apply to other attention variants (linear attention, sparse attention)?

4. **MLA + context extension interaction**: How do different context extension methods (YaRN, PI, NTK) interact with MLA's low-rank compression?

---

## Core References and Why They Are Referenced

### Attention Efficiency

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundation Transformer architecture that MLA modifies.

- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head is All You Need.* Multi-Query Attention (MQA) that MLA improves upon with latent compression.

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Grouped-Query Attention baseline for KV cache reduction.

### MoE Architectures

- **Shazeer et al. (2017)** -- *Outrageously Large Neural Networks.* Original MoE layer for Transformers.

- **Fedus et al. (2022)** -- *Switch Transformers.* Simplified MoE routing that DeepSeekMoE extends.

- **Jiang et al. (2024)** -- *Mixtral of Experts.* Contemporary MoE model that DeepSeek-V2 outperforms.

### Position Encoding

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE that MLA adapts via decoupled formulation.

- **Peng et al. (2024)** -- *YaRN: Efficient Context Window Extension.* Context extension method used to scale DeepSeek-V2 to 128K.

### Alignment

- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback.* RLHF paradigm that GRPO simplifies by removing the critic model.
