---
title: "DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models"
authors: "Dai, Deng, Zhao, Xu, Gao, Chen, Li, Zeng, Yu, Wu, Xie, Li, Huang, Luo, Ruan, Sui, Liang"
year: 2024
venue: "ACL 2024"
paper_type: conference-paper
categories: ["architecture", "model-release"]
scope: ["mixture-of-experts", "expert specialization", "parameter efficiency"]
benchmarks_used: ["hellaswag", "piqa", "arc", "race", "humaneval", "mbpp", "triviaqa", "natural-questions", "mmlu", "winogrande", "gsm8k", "math-hendrycks", "c-eval", "cmmlu"]
models_introduced: ["deepseek-moe-2b", "deepseek-moe-16b", "deepseek-moe-145b"]
models_evaluated: ["llama-2-7b", "llama-7b", "deepseek-moe-16b"]
key_claims:
  - id: C1
    claim: "DeepSeekMoE 2B achieves comparable performance with GShard 2.9B, which has 1.5x expert parameters and computation"
    evidence: "Table 2, Section 4.3"
    status: supported
    scope: "2B parameter scale, 100B training tokens"
    magnitude: "Matches GShard with 1.5x resources"
  - id: C2
    claim: "DeepSeekMoE 2B nearly approaches the performance of Dense×16, which sets the upper bound of MoE models"
    evidence: "Table 2, Section 4.3"
    status: supported
    scope: "2B parameter scale, 100B training tokens"
  - id: C3
    claim: "DeepSeekMoE 16B achieves comparable performance with LLaMA2 7B using only ~40% of computations"
    evidence: "Table 4, Figure 1, Section 5.2"
    status: supported
    scope: "16B total params, 2T training tokens"
    magnitude: "39.6% of LLaMA2 7B FLOPs (74.4T vs 187.9T per 4K tokens)"
  - id: C4
    claim: "DeepSeekMoE 145B achieves comparable performance with DeepSeek 67B using only 28.5% of computations"
    evidence: "Table 6, Section 7.2"
    status: supported
    scope: "145B total params, 245B training tokens (preliminary)"
    magnitude: "28.5% of DeepSeek 67B FLOPs"
  - id: C5
    claim: "Fine-grained expert segmentation increases combinatorial flexibility from 120 to 4.4 billion combinations"
    evidence: "Section 3.1"
    status: supported
    scope: "N=16 experts, top-2 vs 64 experts top-8"
    magnitude: "C(16,2)=120 vs C(64,8)=4,426,165,368"
cross_references:
  - target: 2024-05-deepseek-v2-moe
    type: extended-by
    detail: "DeepSeek-V2 builds upon the DeepSeekMoE architecture with Multi-head Latent Attention"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "DeepSeekMoE extends the Transformer FFN layers with MoE"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "LLaMA2 7B serves as primary dense baseline for comparison"
open_questions:
  - question: "How does DeepSeekMoE scale beyond 145B parameters?"
    addressed_by: 2024-05-deepseek-v2-moe
  - question: "What is the optimal ratio between shared and routed experts at different scales?"
    addressed_by: null
  - question: "Can the architecture benefit from even finer expert granularity at larger scales?"
    addressed_by: null
---

# DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

**Authors:** Damai Dai, Chengqi Deng, Chenggang Zhao, R.X. Xu, Huazuo Gao, Deli Chen, Jiashi Li, Wangding Zeng, Xingkai Yu, Y. Wu, Zhenda Xie, Y.K. Li, Panpan Huang, Fuli Luo, Chong Ruan, Zhifang Sui, Wenfeng Liang (DeepSeek-AI, Peking University, Tsinghua University, Nanjing University)
**Date:** August 2024, ACL 2024 (arXiv:2401.06066)

---

## Core Research Problem

Mixture-of-Experts (MoE) architectures enable parameter scaling while keeping computational costs modest by activating only a subset of experts per token. However, conventional MoE architectures like GShard face two fundamental limitations that prevent expert specialization:

1. **Knowledge Hybridity:** With limited experts (e.g., 8 or 16), tokens assigned to a specific expert cover diverse knowledge types. The expert must assemble vastly different types of knowledge in its parameters, which are difficult to utilize simultaneously.

2. **Knowledge Redundancy:** Tokens assigned to different experts may require common knowledge. Multiple experts converge in acquiring shared knowledge, leading to parameter redundancy.

These issues collectively prevent MoE models from reaching their theoretical upper-bound performance. Prior work (GShard, Switch Transformer) employed top-1 or top-2 routing with limited experts, leaving substantial room for improving expert specialization.

**Core challenge: how to design an MoE architecture that maximizes expert specialization while maintaining computational efficiency.**

---

## Problem Solutions

DeepSeekMoE introduces two principal strategies to achieve ultimate expert specialization:

1. **Fine-Grained Expert Segmentation:** Segment each expert FFN into m smaller experts (reducing FFN intermediate dimension by 1/m) while activating mK experts instead of K. This maintains constant total parameters and computation while dramatically increasing combinatorial flexibility.

2. **Shared Expert Isolation:** Isolate K_s experts as always-activated shared experts that capture common knowledge across contexts, reducing redundancy among routed experts and allowing each routed expert to specialize on distinctive aspects.

---

## Approach Details

### Method

The standard MoE layer computation is:

> h_t^l = Σ_{i=1}^{N} (g_{i,t} FFN_i(u_t^l)) + u_t^l

where g_{i,t} is the gate value (sparse, only K nonzero) and s_{i,t} = Softmax_i(u_t^{lT} e_i^l) is the token-to-expert affinity.

**Fine-Grained Expert Segmentation** modifies this to:

> h_t^l = Σ_{i=1}^{mN} (g_{i,t} FFN_i(u_t^l)) + u_t^l

where mN is the total number of fine-grained experts and mK experts are activated (g_{i,t} has mK nonzero values).

**Shared Expert Isolation** further modifies the architecture:

> h_t^l = Σ_{i=1}^{K_s} FFN_i(u_t^l) + Σ_{i=K_s+1}^{mN} (g_{i,t} FFN_i(u_t^l)) + u_t^l

where the first K_s experts are always activated (shared), and mK - K_s routed experts are selected from the remaining mN - K_s experts.

### Key Technical Components

**Combinatorial Flexibility:** For N=16 experts with top-2 routing, conventional MoE yields C(16,2) = 120 combinations. With 4× segmentation (64 experts, top-8), DeepSeekMoE yields C(64,8) = 4,426,165,368 combinations—a 36-million-fold increase.

**Load Balance Losses:**

Expert-level balance loss (prevents routing collapse):
> L_ExpBal = α_1 Σ_{i=1}^{N'} f_i P_i

where f_i is the fraction of tokens routed to expert i and P_i is the average routing probability.

Device-level balance loss (for distributed training):
> L_DevBal = α_2 Σ_{i=1}^{D} f'_i P'_i

where experts are partitioned into D groups across devices.

**Shared-to-Routed Expert Ratio:** Experiments show 1:3 ratio (1 shared, 3 activated routed) yields marginally better performance than other ratios.

### Experimental Setup

**DeepSeekMoE 2B (Validation):**
- 9 Transformer layers, hidden dimension 1280
- 10 attention heads (128 dim each)
- 1 shared expert + 63 routed experts (7 activated)
- Expert size: 0.25× standard FFN
- Training: 100B tokens, batch size 2K sequences, max LR 1.08×10^-3
- Expert-level balance factor: 0.01

**DeepSeekMoE 16B:**
- 28 layers, hidden dimension 2048, 16 attention heads
- 2 shared experts + 64 routed experts (6 activated)
- Expert size: 0.25× standard FFN
- 16.4B total parameters, 2.8B activated parameters
- Training: 2T tokens (same as LLaMA2 7B), max LR 4.2×10^-4
- Expert-level balance factor: 0.001

**DeepSeekMoE 145B:**
- 62 layers, hidden dimension 4096, 32 attention heads
- 4 shared experts + 128 routed experts (12 activated)
- Expert size: 0.125× standard FFN
- 144.6B total parameters, 22.2B activated parameters
- Training: 245B tokens (preliminary), max LR 3.0×10^-4
- Device-level balance factor: 0.05, expert-level balance factor: 0.003

**Reproducibility:** Code and DeepSeekMoE 16B checkpoint publicly released. Model deployable on single 40GB GPU without quantization.

### Key Results

**Validation Experiments (2B scale, 100B tokens):**

| Model | Total Params | Activated Params | Pile Loss | HellaSwag | TriviaQA |
|-------|--------------|------------------|-----------|-----------|----------|
| Dense | 0.2B | 0.2B | 2.060 | 38.8 | 4.9 |
| GShard | 2.0B | 0.3B | 1.867 | 50.5 | 10.2 |
| DeepSeekMoE | 2.0B | 0.3B | **1.808** | **54.8** | **16.6** |
| GShard×1.5 | 2.9B | 0.35B | 1.808 | 54.4 | 15.7 |
| Dense×16 | 2.0B | 1.89B | 1.806 | 55.1 | 16.5 |

- DeepSeekMoE 2B matches GShard with 1.5× expert parameters and computation
- DeepSeekMoE 2B nearly approaches Dense×16 (theoretical upper bound for MoE)

**DeepSeekMoE 16B vs Dense Models:**

| Metric | LLaMA2 7B | DeepSeek 7B | DeepSeekMoE 16B |
|--------|-----------|-------------|-----------------|
| FLOPs/4K tokens | 187.9T | 183.5T | 74.4T (39.6%) |
| Pile BPB | 0.76 | 0.75 | **0.74** |
| HellaSwag | 75.6 | 75.4 | **77.1** |
| TriviaQA | 63.8 | 59.7 | **64.8** |
| HumanEval | 14.6 | 26.2 | **26.8** |
| MMLU | **45.8** | **48.2** | 45.0 |

**DeepSeekMoE 145B (Preliminary, 245B tokens):**

| Metric | DeepSeek 67B | GShard 137B | DeepSeekMoE 145B |
|--------|--------------|-------------|------------------|
| FLOPs/4K tokens | 2057.5T | 572.7T | 585.6T (28.5%) |
| Pile Loss | 1.905 | 1.961 | **1.876** |
| HellaSwag | 74.8 | 72.0 | **75.8** |
| TriviaQA | 57.2 | 52.5 | **61.1** |

### Expert Specialization Analysis

**Lower Redundancy:** When disabling top routed experts, DeepSeekMoE shows greater sensitivity than GShard×1.5 (same baseline Pile loss), indicating lower parameter redundancy—each expert is more irreplaceable.

**Shared Expert Irreplaceability:** Disabling the shared expert and activating one more routed expert increases Pile loss from 1.808 to 2.414, demonstrating the shared expert captures fundamental knowledge not replaceable by routed experts.

**Efficient Knowledge Acquisition:** DeepSeekMoE with only 4 activated routed experts achieves comparable Pile loss to GShard with full top-2 activation, demonstrating more accurate knowledge acquisition with fewer experts.

---

## Limitations and Failure Modes

**Acknowledged by Authors:**

1. **Multiple-choice task limitations:** DeepSeekMoE 16B underperforms on MMLU-like tasks compared to DeepSeek 7B. Authors attribute this to limited attention parameters (0.5B vs 2.5B in DeepSeek 7B), noting a positive correlation between attention capacity and multiple-choice performance.

2. **Preliminary 145B results:** The 145B model is trained on only 245B tokens—a preliminary study. Full training results pending.

3. **First layer exception:** The first layer uses dense FFN instead of MoE because load balance converges especially slowly for it.

**Scope and Comparability:**

- All internal comparisons use the same training corpus, enabling fair architecture comparisons but not reflecting differences in data quality across open-source models.
- Chinese benchmark advantages for DeepSeekMoE reflect bilingual training corpus, not purely architectural benefits.
- Expert-level balance factor varies by model size (0.01 for 2B, 0.001 for 16B, 0.003 for 145B), making cross-scale comparisons imperfect.

---

## Conclusions

### Contributions

1. **Fine-grained expert segmentation architecture.** Segment experts into smaller units while activating proportionally more experts, dramatically increasing combinatorial flexibility (36 million-fold increase in possible combinations) while maintaining constant compute.

2. **Shared expert isolation.** Dedicate always-activated experts to capture common knowledge, reducing redundancy among routed experts and enabling higher specialization.

3. **Empirical validation of near-upper-bound performance.** At 2B scale, DeepSeekMoE nearly matches Dense×16 (theoretical MoE upper bound), demonstrating the architecture approaches optimal parameter utilization.

4. **Scalable efficiency gains.** Consistent ~60% compute reduction vs comparable dense models across scales: 2B matches 2.9B GShard, 16B matches 7B dense, 145B matches 67B dense.

5. **Public release.** DeepSeekMoE 16B released, deployable on single 40GB GPU without quantization.

### Implications

1. **Expert specialization as key MoE objective.** The paper reframes MoE design around maximizing expert specialization rather than simply scaling parameters, suggesting architectural innovations targeting specialization may yield greater returns than naive scaling.

2. **Trade-off between attention and FFN parameters.** The MMLU limitation highlights that MoE architectures, which primarily scale FFN parameters, may benefit from complementary attention scaling for certain task types.

3. **Foundation for larger DeepSeek models.** The architecture provides the basis for DeepSeek-V2 and subsequent models in the DeepSeek series.

---

## Key Claims

1. **C1: DeepSeekMoE 2B matches GShard 2.9B.** With same total parameters (2B) and activated parameters (0.3B), DeepSeekMoE achieves performance comparable to GShard with 1.5× expert parameters and computation. Evidence: Table 2 shows identical Pile loss (1.808) and comparable benchmark scores. Scope: 100B training tokens, validation experiments.

2. **C2: DeepSeekMoE approaches theoretical MoE upper bound.** DeepSeekMoE 2B nearly matches Dense×16 (1.808 vs 1.806 Pile loss), which represents the maximum achievable performance by activating all experts. Evidence: Table 2. Scope: 2B scale, 100B tokens.

3. **C3: 60% compute reduction at 16B scale.** DeepSeekMoE 16B achieves comparable performance to LLaMA2 7B and DeepSeek 7B using only 40% of computations. Evidence: Tables 3-4, Figure 1. Magnitude: 74.4T vs 183.5-187.9T FLOPs per 4K tokens.

4. **C4: Consistent advantages at 145B scale.** DeepSeekMoE 145B matches DeepSeek 67B with 28.5% of compute. Evidence: Table 6. Scope: Preliminary results with 245B tokens.

5. **C5: Expert specialization empirically demonstrated.** DeepSeekMoE shows (a) greater sensitivity to expert disabling, (b) irreplaceable shared experts, and (c) comparable performance with fewer activated experts. Evidence: Section 4.5, Figures 4-6.

---

## Open Questions

1. **Optimal expert granularity vs. computational efficiency.** Authors note finer granularity than 0.25× is not used at 16B scale "due to potential reduction in computational efficiency." What are the precise trade-offs, and can they be mitigated with better kernels?

2. **Shared expert ratio across scales.** The 1:3 ratio was selected based on 2B experiments with minimal difference between ratios. Does this ratio remain optimal at larger scales?

3. **Attention scaling for MoE models.** Given MMLU limitations attributed to limited attention parameters, how should attention capacity be scaled alongside MoE-based FFN scaling?

4. **Load balance at first layer.** Why does load balance converge slowly at the first layer, and are there architectural modifications that could enable MoE at all layers?

---

## Core References and Why They Are Referenced

### MoE Foundations

- **Jacobs et al. (1991)** -- *Adaptive Mixtures of Local Experts.* Original MoE concept for handling different samples with independent expert modules.

- **Shazeer et al. (2017)** -- *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.* Introduced MoE to language model training with gated routing, establishing the sparsity paradigm DeepSeekMoE builds upon.

### MoE Architectures

- **Lepikhin et al. (2021)** -- *GShard.* Primary baseline architecture using top-2 learnable routing. DeepSeekMoE explicitly demonstrates advantages over GShard at multiple scales.

- **Fedus et al. (2021)** -- *Switch Transformers.* Top-1 routing baseline, demonstrating MoE scaling to trillion parameters with simple routing.

- **Rajbhandari et al. (2022)** -- *DeepSpeed-MoE.* Credited as prototype for shared expert isolation from an engineering perspective, while DeepSeekMoE approaches it algorithmically.

### Dense Baselines

- **Touvron et al. (2023b)** -- *LLaMA 2.* Primary dense baseline for DeepSeekMoE 16B comparison, trained on same 2T tokens.

- **DeepSeek-AI (2024)** -- *DeepSeek LLM.* DeepSeek 7B and 67B provide dense baselines trained on identical corpora for fair architectural comparison.

### Transformer Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer architecture that DeepSeekMoE extends by replacing FFN layers with MoE layers.
