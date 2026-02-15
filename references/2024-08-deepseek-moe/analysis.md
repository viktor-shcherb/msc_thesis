---
title: "DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models"
authors: "Dai, Deng, Zhao, Xu, Gao, Chen, Li, Zeng, Yu, Wu, Xie, Li, Huang, Luo, Ruan, Sui, Liang"
year: 2024
venue: "ACL 2024"
paper_type: conference-paper
categories: ["architecture", "model-release"]
scope: ["mixture-of-experts", "expert specialization", "parameter efficiency"]
benchmarks_used: ["perplexity-pile", "hellaswag", "piqa", "arc", "race", "humaneval", "mbpp", "triviaqa", "natural-questions", "mmlu", "winogrande", "gsm8k", "math-hendrycks", "drop", "bbh", "truthfulqa", "c-eval", "cmmlu", "open-llm-leaderboard"]
models_introduced: ["deepseek-moe-2b", "deepseek-moe-16b", "deepseek-moe-145b"]
models_evaluated: ["deepseek-moe-2b", "deepseek-moe-16b", "deepseek-moe-145b", "deepseek-7b", "deepseek-67b", "llama-2-7b", "llama-7b"]
key_claims:
  - id: C1
    claim: "DeepSeekMoE 2B achieves comparable performance with GShard 2.9B, which has 1.5x expert parameters and computation"
    evidence: "Table 2, Section 4.3"
    status: supported
    scope: "2B parameter scale, 100B training tokens, 12 benchmarks"
    magnitude: "Matches GShard x1.5 Pile loss (both 1.808) with 0.24B vs 0.35B activated expert params"
  - id: C2
    claim: "DeepSeekMoE 2B nearly approaches the performance of Dense x16, which sets the upper bound of MoE models"
    evidence: "Table 2, Section 4.3"
    status: supported
    scope: "2B parameter scale, 100B training tokens"
    magnitude: "1.808 vs 1.806 Pile loss; HellaSwag 54.8 vs 55.1; TriviaQA 16.6 vs 16.5"
  - id: C3
    claim: "DeepSeekMoE 16B achieves comparable performance with LLaMA2 7B using only about 40% of computations"
    evidence: "Table 4, Figure 1, Section 5.2"
    status: supported
    scope: "16B total params, 2.8B activated params, 2T training tokens, English and Chinese benchmarks"
    magnitude: "39.6% of LLaMA2 7B FLOPs (74.4T vs 187.9T per 4K tokens); outperforms on majority of benchmarks"
  - id: C4
    claim: "DeepSeekMoE 145B achieves comparable performance with DeepSeek 67B using only 28.5% of computations"
    evidence: "Table 6, Section 7.2"
    status: supported
    scope: "145B total params, 245B training tokens (preliminary), 22 benchmarks"
    magnitude: "28.5% of DeepSeek 67B FLOPs (585.6T vs 2057.5T per 4K tokens)"
  - id: C5
    claim: "Fine-grained expert segmentation increases combinatorial flexibility from 120 to 4.4 billion combinations"
    evidence: "Section 3.1"
    status: supported
    scope: "N=16 experts, top-2 vs m=4 segmentation (64 experts, top-8)"
    magnitude: "C(16,2)=120 vs C(64,8)=4,426,165,368 (36-million-fold increase)"
  - id: C6
    claim: "DeepSeekMoE exhibits lower redundancy among routed experts compared with GShard"
    evidence: "Figure 4, Section 4.5"
    status: supported
    scope: "2B parameter scale, compared against GShard x1.5 at same baseline Pile loss"
    magnitude: "Steeper Pile loss degradation when disabling top routed experts (qualitative comparison via curves)"
  - id: C7
    claim: "Shared experts capture fundamental knowledge irreplaceable by routed experts"
    evidence: "Section 4.5"
    status: supported
    scope: "DeepSeekMoE 2B, single shared expert"
    magnitude: "Pile loss increases from 1.808 to 2.414 when shared expert is disabled and one more routed expert activated"
  - id: C8
    claim: "DeepSeekMoE Chat 16B achieves comparable performance with LLaMA2 SFT 7B and DeepSeek Chat 7B after alignment"
    evidence: "Table 5, Section 6.2"
    status: supported
    scope: "16B total params, 1.4M SFT examples, 19 benchmarks"
    magnitude: "Comparable or better on majority of benchmarks with ~40% of computations"
cross_references:
  - target: 2024-05-deepseek-v2-moe
    type: extended-by
    detail: "DeepSeek-V2 builds upon the DeepSeekMoE architecture with Multi-head Latent Attention"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "DeepSeekMoE extends the Transformer FFN layers with MoE"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "LLaMA2 7B serves as primary dense baseline for comparison at 16B scale"
  - target: 2024-12-deepseek-v3-technical-report
    type: extended-by
    detail: "DeepSeek-V3 scales DeepSeekMoE to 671B total parameters (256 routed + 1 shared expert, 8 activated per token) with auxiliary-loss-free load balancing replacing the multi-level auxiliary losses"
open_questions:
  - question: "How does DeepSeekMoE scale beyond 145B parameters with full training?"
    addressed_by: [2024-05-deepseek-v2-moe, 2024-12-deepseek-v3-technical-report]
  - question: "What is the optimal ratio between shared and routed experts at different scales?"
    addressed_by: null
  - question: "Can the architecture benefit from even finer expert granularity at larger scales with better kernels?"
    addressed_by: null
  - question: "Why does load balance converge especially slowly at the first layer, and can MoE be enabled there?"
    addressed_by: null
  - question: "Does FFN-heavy MoE have fundamental limitations for reasoning tasks, or can attention-FFN co-scaling resolve the MMLU gap?"
    addressed_by: null
---

# DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

**Authors:** Damai Dai, Chengqi Deng, Chenggang Zhao, R.X. Xu, Huazuo Gao, Deli Chen, Jiashi Li, Wangding Zeng, Xingkai Yu, Y. Wu, Zhenda Xie, Y.K. Li, Panpan Huang, Fuli Luo, Chong Ruan, Zhifang Sui, Wenfeng Liang (DeepSeek-AI; Peking University; Tsinghua University; Nanjing University)
**Date:** August 2024, ACL 2024 (arXiv:2401.06066)

---

## Core Research Problem

Mixture-of-Experts (MoE) architectures enable parameter scaling while keeping computational costs modest by activating only a subset of experts per token. However, conventional MoE architectures like GShard (Lepikhin et al., 2021) -- *GShard* and Switch Transformer (Fedus et al., 2021) -- *Switch Transformers* face two fundamental limitations that prevent expert specialization:

1. **Knowledge Hybridity:** With limited experts (e.g., 8 or 16), tokens assigned to a specific expert cover diverse knowledge types. The designated expert must assemble vastly different types of knowledge in its parameters, which are difficult to utilize simultaneously (Section 1).

2. **Knowledge Redundancy:** Tokens assigned to different experts may require common knowledge. Multiple experts converge in acquiring shared knowledge in their parameters, leading to parameter redundancy (Section 1).

These issues collectively prevent MoE models from reaching their theoretical upper-bound performance. Prior work employed top-1 or top-2 routing with a limited number of experts, leaving substantial room for improving expert specialization (Section 8).

**Core challenge: how to design an MoE architecture that maximizes expert specialization while maintaining computational efficiency.**

---

## Problem Solutions

DeepSeekMoE introduces two principal strategies to achieve ultimate expert specialization:

1. **Fine-Grained Expert Segmentation:** Segment each expert FFN into m smaller experts (reducing FFN intermediate dimension by 1/m) while activating mK experts instead of K. This maintains constant total parameters and computation while dramatically increasing combinatorial flexibility.

2. **Shared Expert Isolation:** Isolate K_s experts as always-activated shared experts that capture common knowledge across contexts, reducing redundancy among routed experts and allowing each routed expert to specialize on distinctive aspects.

These two strategies are complementary: fine-grained segmentation decomposes diverse knowledge into more specialized units, while shared expert isolation eliminates the need for routed experts to redundantly learn common knowledge.

---

## Approach Details

### Method

The standard MoE layer replaces the FFN in a Transformer block. The computation for the output hidden state is (Eq. 3, Section 2):

> h_t^l = sum_{i=1}^{N} (g_{i,t} FFN_i(u_t^l)) + u_t^l

where g_{i,t} is the gate value (sparse, only K nonzero) determined by:

> g_{i,t} = s_{i,t} if s_{i,t} in Topk({s_{j,t} | 1 <= j <= N}, K), else 0

and s_{i,t} = Softmax_i(u_t^{lT} e_i^l) is the token-to-expert affinity score computed via dot product of the token hidden state and expert centroid (Eqs. 4-5, Section 2).

**Fine-Grained Expert Segmentation** modifies this to (Eq. 6, Section 3.1):

> h_t^l = sum_{i=1}^{mN} (g_{i,t} FFN_i(u_t^l)) + u_t^l

where mN is the total number of fine-grained experts and mK experts are activated (g_{i,t} has mK nonzero values). Each fine-grained expert has an FFN intermediate dimension of 1/m the original size (Eqs. 6-8).

**Shared Expert Isolation** further modifies the architecture (Eq. 9, Section 3.2):

> h_t^l = sum_{i=1}^{K_s} FFN_i(u_t^l) + sum_{i=K_s+1}^{mN} (g_{i,t} FFN_i(u_t^l)) + u_t^l

where the first K_s experts are always activated (shared), and (mK - K_s) routed experts are selected from the remaining (mN - K_s) experts via top-(mK - K_s) gating (Eqs. 9-11).

### Key Technical Components

**Combinatorial Flexibility:** For N=16 experts with top-2 routing, conventional MoE yields C(16,2) = 120 combinations. With 4x segmentation (64 experts, top-8), DeepSeekMoE yields C(64,8) = 4,426,165,368 combinations -- a **36-million-fold increase** (Section 3.1).

**Expert-Level Balance Loss** (prevents routing collapse, Eq. 12, Section 3.3):

> L_ExpBal = alpha_1 * sum_{i=1}^{N'} f_i * P_i

where f_i = (N' / (K'T)) * sum_t 1(Token t selects Expert i) is the fraction of tokens routed to expert i (normalized so uniform gives f_i = 1), and P_i = (1/T) * sum_t s_{i,t} is the average routing probability (Eqs. 12-14). N' = mN - K_s and K' = mK - K_s.

**Device-Level Balance Loss** (for distributed training, Eq. 15, Section 3.3):

> L_DevBal = alpha_2 * sum_{i=1}^{D} f'_i * P'_i

where experts are partitioned into D groups across devices, f'_i is the average expert frequency within group, and P'_i is the sum of routing probabilities in the group (Eqs. 15-17). In practice, a small expert-level factor prevents routing collapse while a larger device-level factor promotes balanced computation.

**Shared-to-Routed Expert Ratio:** Experiments at 2B scale show 1:3 ratio (1 shared, 3 activated routed) yields marginally better Pile loss (1.806) than 1:7 ratio (1.808) or 4:4 ratio (1.811). The 1:3 ratio is adopted for scaling (Section 4.4).

**First Layer Exception:** The first Transformer layer uses a dense FFN instead of MoE because load balance converges especially slowly for it (Section 5.1.2).

### Experimental Setup

**DeepSeekMoE 2B (Validation):**
- 9 Transformer layers, hidden dimension 1280, 10 attention heads (128 dim each)
- 1 shared expert + 63 routed experts (7 activated), expert size 0.25x standard FFN
- ~2.0B total params, ~0.3B activated params
- Training: 100B tokens from multilingual corpus (English/Chinese focus), batch size 2K sequences, max sequence length 2K, max LR 1.08x10^-3
- AdamW optimizer (beta_1=0.9, beta_2=0.95, weight_decay=0.1), warmup-and-step-decay schedule
- Expert-level balance factor alpha_1 = 0.01; all experts on single GPU; no token dropping
- Tokenizer: BPE with 8K vocabulary

**DeepSeekMoE 16B:**
- 28 layers, hidden dimension 2048, 16 attention heads (128 dim each)
- 2 shared experts + 64 routed experts (6 activated), expert size 0.25x standard FFN
- 16.4B total params, 2.8B activated params (~0.5B attention params)
- Training: 2T tokens (same as LLaMA2 7B), batch size 4.5K sequences, max sequence length 4K, max LR 4.2x10^-4
- Expert-level balance factor alpha_1 = 0.001; pipeline parallelism; no token dropping
- Tokenizer: BPE with 100K vocabulary
- FLOPs per 4K tokens: 74.4T

**DeepSeekMoE 145B:**
- 62 layers, hidden dimension 4096, 32 attention heads (128 dim each)
- 4 shared experts + 128 routed experts (12 activated), expert size 0.125x standard FFN
- 144.6B total params, 22.2B activated params
- Training: 245B tokens (preliminary), batch size 4.5K, max sequence length 4K, max LR 3.0x10^-4
- Device-level balance factor alpha_2 = 0.05, expert-level balance factor alpha_1 = 0.003
- Expert parallelism: routed experts on 4 devices
- FLOPs per 4K tokens: 585.6T

**Alignment (SFT) for DeepSeekMoE 16B:**
- 1.4M training examples spanning math, code, writing, QA, reasoning, summarization
- Batch size 1024, 8 epochs, constant LR 10^-5, max sequence length 4K
- Same SFT data applied to LLaMA2 7B and DeepSeek 7B for fair comparison

**Reproducibility:** Code released at github.com/deepseek-ai/DeepSeek-MoE. DeepSeekMoE 16B checkpoint publicly released, deployable on single 40GB GPU without quantization. No mention of random seeds. Training infrastructure: NVIDIA A100 and H800 clusters with HAI-LLM framework.

### Key Results

**Validation Experiments (2B scale, 100B tokens, Table 1):**

| Model | Total Params | Activated Params | Pile Loss | HellaSwag | PIQA | ARC-e | ARC-c | TriviaQA | NQ |
|---|---|---|---|---|---|---|---|---|---|
| Dense | 0.2B | 0.2B | 2.060 | 38.8 | 66.8 | 41.0 | 26.0 | 4.9 | 1.4 |
| Hash Layer | 2.0B | 0.2B | 1.932 | 46.2 | 68.4 | 45.3 | 28.2 | 6.5 | 1.4 |
| Switch | 2.0B | 0.2B | 1.881 | 49.1 | 70.5 | 45.9 | 30.2 | 8.9 | 2.5 |
| GShard | 2.0B | 0.3B | 1.867 | 50.5 | 70.6 | 43.9 | 31.6 | 10.2 | 3.2 |
| **DeepSeekMoE** | **2.0B** | **0.3B** | **1.808** | **54.8** | **72.3** | **49.4** | **34.3** | **16.6** | **5.7** |

DeepSeekMoE demonstrates **overwhelming advantages** over GShard with the same total and activated parameters across all benchmarks (Table 1, Section 4.2).

**Comparison with Larger Baselines (Table 2):**

| Model | Activated Expert Params | FLOPs/2K tokens | Pile Loss | HellaSwag | TriviaQA | NQ |
|---|---|---|---|---|---|---|
| GShard x1.5 | 0.35B | 5.8T | 1.808 | 54.4 | 15.7 | 4.7 |
| Dense x16 (upper bound) | 1.89B | 24.6T | 1.806 | 55.1 | 16.5 | 6.3 |
| DeepSeekMoE | 0.24B | 4.3T | 1.808 | 54.8 | 16.6 | 5.7 |

DeepSeekMoE matches GShard x1.5 (which has 1.5x expert parameters and computation) and nearly approaches Dense x16, the theoretical MoE upper bound (Table 2, Section 4.3). At the larger 13B scale, DeepSeekMoE **outperforms** GShard x1.5 distinctly (Table 10, Appendix B).

**DeepSeekMoE 16B vs Dense Models (Table 3 and Table 4, Section 5.2):**

| Metric | # Shot | LLaMA2 7B | DeepSeek 7B | DeepSeekMoE 16B |
|---|---|---|---|---|
| FLOPs/4K tokens | N/A | 187.9T | 183.5T | 74.4T (39.6%) |
| Pile BPB | N/A | 0.76 | 0.75 | **0.74** |
| HellaSwag | 0-shot | 75.6 | 75.4 | **77.1** |
| PIQA | 0-shot | 78.0 | 79.2 | **80.2** |
| TriviaQA | 5-shot | 63.8 | 59.7 | **64.8** |
| NaturalQuestions | 5-shot | **25.5** | 22.2 | 25.5 |
| HumanEval | 0-shot | 14.6 | 26.2 | **26.8** |
| MBPP | 3-shot | 21.8 | **39.0** | 39.2 |
| GSM8K | 8-shot | 15.5 | 17.4 | **18.8** |
| MATH | 4-shot | 2.6 | 3.3 | **4.3** |
| MMLU | 5-shot | **45.8** | **48.2** | 45.0 |
| DROP | 1-shot | **34.0** | **34.9** | 32.9 |
| WinoGrande | 0-shot | 69.6 | **70.5** | 70.2 |

With only ~40% of computations, DeepSeekMoE 16B outperforms LLaMA2 7B on the majority of benchmarks (Table 4). Strengths are in language modeling and knowledge-intensive tasks (HellaSwag, TriviaQA). Weakness is on multiple-choice tasks (MMLU) due to limited attention parameters: 0.5B vs 2.5B in DeepSeek 7B (Section 5.2.1). DeepSeekMoE 16B also dramatically outperforms models with similar activated parameters on the Open LLM Leaderboard (Figure 1, tested across 12+ models with 2-7B activated parameters -- strong evidence for compute-efficiency claim).

**Alignment Results (Table 5, Section 6.2):**

| Metric | # Shot | LLaMA2 SFT 7B | DeepSeek Chat 7B | DeepSeekMoE Chat 16B |
|---|---|---|---|---|
| FLOPs/4K tokens | N/A | 187.9T | 183.5T | 74.4T |
| HellaSwag | 0-shot | 67.9 | 71.0 | **72.2** |
| HumanEval | 0-shot | 35.4 | 45.1 | **45.7** |
| MBPP | 3-shot | 27.8 | 39.0 | **46.2** |
| MATH | 4-shot | 13.5 | 14.7 | **15.2** |
| TriviaQA | 5-shot | 60.1 | 59.5 | **63.3** |
| MMLU | 0-shot | **50.0** | 49.7 | 47.2 |
| BBH | 3-shot | 39.3 | **43.1** | 42.2 |
| DROP | 1-shot | 40.0 | **41.7** | 33.8 |
| GSM8K | 0-shot | **63.4** | 62.6 | 62.2 |

DeepSeekMoE Chat 16B achieves comparable performance with both 7B dense chat models on most benchmarks, with notable strengths on code generation (HumanEval, MBPP) and knowledge tasks (TriviaQA), while the MMLU gap narrows after SFT (Table 5, Section 6.2). All three models use the same SFT data for fair comparison.

**DeepSeekMoE 145B (Preliminary, 245B tokens, Table 6):**

| Metric | # Shot | DeepSeek 67B | GShard 137B | DeepSeekMoE 145B | DeepSeekMoE 142B (Half) |
|---|---|---|---|---|---|
| Total Params | N/A | 67.4B | 136.5B | 144.6B | 142.3B |
| Activated Params | N/A | 67.4B | 21.6B | 22.2B | 12.2B |
| FLOPs/4K tokens | N/A | 2057.5T | 572.7T | 585.6T | 374.6T |
| Pile Loss | N/A | 1.905 | 1.961 | **1.876** | 1.888 |
| HellaSwag | 0-shot | 74.8 | 72.0 | **75.8** | 74.9 |
| TriviaQA | 5-shot | 57.2 | 52.5 | **61.1** | 59.8 |
| MMLU | 5-shot | **45.1** | 26.3 | 39.4 | 37.5 |
| HumanEval | 0-shot | **23.8** | 17.7 | 19.5 | 23.2 |

DeepSeekMoE 145B matches or exceeds DeepSeek 67B on most tasks with only 28.5% of computations. GShard 137B is significantly outperformed. Even DeepSeekMoE 142B (Half Activated), with only 18.2% of DeepSeek 67B's compute, still matches DeepSeek 67B overall and outperforms GShard 137B (Table 6, Section 7.2). Results are preliminary (245B tokens only -- limited evidence for final performance).

### Expert Specialization Analysis

**Lower Redundancy (Figure 4, Section 4.5):** When disabling top routed experts progressively (ratios 1/16 to 4/16), DeepSeekMoE shows greater sensitivity than GShard x1.5 (both starting at same 1.808 Pile loss). DeepSeekMoE's loss rises more steeply (~5 at 1/16 disabled vs ~3 for GShard x1.5), indicating each expert is more irreplaceable -- lower parameter redundancy.

**Shared Expert Irreplaceability (Section 4.5):** Disabling the shared expert and activating one more routed expert increases Pile loss from **1.808 to 2.414** (a 33% increase), demonstrating the shared expert captures fundamental knowledge not replaceable by routed experts (single experiment, no variance reported -- limited evidence but large effect size).

**Efficient Knowledge Acquisition (Figure 5, Section 4.5):** DeepSeekMoE with only 4 activated routed experts achieves Pile loss comparable to GShard with full top-2 activation (~1.867). Training a separate model from scratch with 1 shared + 3 activated routed experts (half the activated expert parameters of GShard) still outperforms GShard on all six evaluated benchmarks (Figure 6).

### Ablation Studies

Ablation studies (Figure 3, Section 4.4) with controlled total and activated parameters show consistent improvement from:
1. GShard (0 shared + 2 out of 16 routed) -- baseline
2. + Shared expert isolation (1 shared + 1 out of 15 routed) -- improvement on most benchmarks
3. + Fine-grained segmentation to 32 experts (1 shared + 3 out of 31 routed) -- further improvement
4. + Finer segmentation to 64 experts (1 shared + 7 out of 63 routed) -- best performance (full DeepSeekMoE)

Each strategy contributes incrementally, with fine-grained segmentation providing the largest gains (tested across 6 benchmarks -- moderate evidence).

---

## Limitations and Failure Modes

**Acknowledged by Authors:**

1. **Multiple-choice task limitations:** DeepSeekMoE 16B underperforms on MMLU (45.0 vs 48.2 for DeepSeek 7B) and Chinese multiple-choice tasks (CEval, CMMLU). Authors attribute this to limited attention parameters: DeepSeekMoE 16B has only ~0.5B attention parameters vs 2.5B in DeepSeek 7B. A positive correlation between attention capacity and multiple-choice performance is observed, consistent with DeepSeek 7B MQA also struggling on MMLU (Section 5.2.1).

2. **Preliminary 145B results:** The 145B model is trained on only 245B tokens -- a preliminary study, not a fully trained model. Full training results were pending at publication (Section 7).

3. **First layer exception:** The first layer uses dense FFN instead of MoE because load balance converges especially slowly for it, with no further analysis of why (Section 5.1.2).

4. **Finer granularity limited by efficiency:** At 16B scale, finer than 0.25x expert size is not used "due to potential reduction in computational efficiency associated with excessively small expert sizes" (Section 5.1.2).

5. **DROP performance gap:** DeepSeekMoE Chat 16B scores 33.8 on DROP vs 41.7 for DeepSeek Chat 7B -- a notable regression on this reading comprehension benchmark (Table 5).

- **[Inferred]** No variance estimates or confidence intervals reported for any experimental results. All comparisons are based on single training runs (no seeds mentioned), limiting statistical conclusions.

- **[Inferred]** The ablation studies for shared-to-routed expert ratio show minimal differences (Pile loss 1.808, 1.806, 1.811 for 1, 2, 4 shared experts), yet the 1:3 ratio is adopted without testing at larger scales.

#### Scope and Comparability

- **What was not tested:** No evaluation on non-English languages beyond Chinese. No comparison with other MoE architectures beyond GShard, Switch Transformer, and Hash Layer (e.g., no comparison with expert-choice routing of Zhou et al., 2022, or ST-MoE). No evaluation of inference latency beyond the 2.5x speedup claim for 16B. The 145B model is only a preliminary study.
- **[Inferred]** All internal comparisons use the same training corpus, enabling fair architecture comparisons but not reflecting data quality differences with open-source models (LLaMA2 uses different data).
- **[Inferred]** Chinese benchmark advantages for DeepSeekMoE over LLaMA2 7B (e.g., CHID 89.4 vs 37.9) reflect the bilingual training corpus, not purely architectural benefits.
- **[Inferred]** Expert-level balance factor varies by model size (0.01 for 2B, 0.001 for 16B, 0.003 for 145B), making cross-scale comparisons of routing behavior imperfect.
- **Comparability note:** The 145B comparison trains all models (including DeepSeek 67B dense) on only 245B tokens, enabling fair comparison but not reflecting fully-trained model behavior.

---

## Conclusions

### Contributions

1. **Fine-grained expert segmentation architecture.** Segment experts into smaller units while activating proportionally more, dramatically increasing combinatorial flexibility (36-million-fold increase) while maintaining constant compute (Section 3.1, validated at 2B, 16B, and 145B scales).

2. **Shared expert isolation.** Dedicate always-activated experts to capture common knowledge, reducing redundancy among routed experts. Empirically validated: disabling the shared expert causes a 33% Pile loss increase even when compensated with an additional routed expert (Section 4.5).

3. **Empirical validation of near-upper-bound performance.** At 2B scale, DeepSeekMoE nearly matches Dense x16 (1.808 vs 1.806 Pile loss), demonstrating the architecture approaches optimal parameter utilization (Table 2, Section 4.3).

4. **Consistent compute efficiency across three scales.** ~60% compute reduction vs comparable dense models: 2B matches 2.9B GShard, 16B matches 7B dense, 145B matches 67B dense (Tables 2, 4, 6).

5. **Successful MoE alignment.** DeepSeekMoE Chat 16B demonstrates that the architecture benefits from supervised fine-tuning, achieving comparable chat performance with 7B dense models (Table 5, Section 6).

6. **Public release.** DeepSeekMoE 16B released, deployable on single 40GB GPU without quantization.

### Implications

1. **Expert specialization as key MoE objective.** The paper reframes MoE design around maximizing expert specialization rather than simply scaling parameters, suggesting architectural innovations targeting specialization may yield greater returns than naive scaling (speculative beyond demonstrated scales).

2. **Trade-off between attention and FFN parameters.** The MMLU limitation highlights that MoE architectures, which primarily scale FFN parameters, may benefit from complementary attention scaling for certain task types -- a design consideration for future MoE models.

3. **Foundation for larger DeepSeek models.** The architecture provides the basis for DeepSeek-V2 and subsequent models in the DeepSeek series.

---

## Key Claims

1. **C1: DeepSeekMoE 2B matches GShard 2.9B.** With same total parameters (2B) and fewer activated expert parameters (0.24B vs 0.35B), DeepSeekMoE achieves performance comparable to GShard with 1.5x expert parameters and computation. Both achieve 1.808 Pile loss; DeepSeekMoE outperforms on most benchmarks (HellaSwag 54.8 vs 54.4, TriviaQA 16.6 vs 15.7). Evidence: Table 2, Section 4.3. Scope: 100B training tokens, 2B scale. Evidence breadth: tested across 12 benchmarks (moderate evidence), single training run, no variance reported.

2. **C2: DeepSeekMoE approaches theoretical MoE upper bound.** DeepSeekMoE 2B nearly matches Dense x16 (1.808 vs 1.806 Pile loss; HellaSwag 54.8 vs 55.1; TriviaQA 16.6 vs 16.5), which represents the maximum achievable performance by activating all experts. Evidence: Table 2, Section 4.3. Scope: 2B scale, 100B tokens. Evidence breadth: single scale only (limited evidence for generalizability).

3. **C3: ~60% compute reduction at 16B scale.** DeepSeekMoE 16B achieves comparable performance to LLaMA2 7B and DeepSeek 7B using only ~40% of computations (74.4T vs 183.5-187.9T FLOPs per 4K tokens). Outperforms on majority of benchmarks, underperforms on MMLU. Evidence: Tables 3-4, Figure 1, Section 5.2. Scope: 2T training tokens, bilingual corpus. Evidence breadth: tested across 22 benchmarks and against 12+ open-source models on Open LLM Leaderboard (strong evidence); single training run.

4. **C4: Consistent advantages at 145B scale.** DeepSeekMoE 145B matches DeepSeek 67B with 28.5% of compute (585.6T vs 2057.5T FLOPs). Even the Half Activated variant (142B) matches DeepSeek 67B with 18.2% of compute (374.6T). Evidence: Table 6, Section 7.2. Scope: Preliminary results with 245B tokens only. Evidence breadth: preliminary training only, not full convergence (limited evidence).

5. **C5: Combinatorial flexibility drives specialization.** Fine-grained segmentation increases expert combinations from C(16,2)=120 to C(64,8)=4,426,165,368, a 36-million-fold increase, enabling more precise knowledge decomposition. Evidence: Section 3.1 (mathematical argument), ablation studies in Figure 3 (empirical validation). Scope: demonstrated at 2B scale with m=4 segmentation. Evidence breadth: ablation across 4 configurations and 6 benchmarks (moderate evidence).

6. **C6: Lower redundancy among routed experts.** DeepSeekMoE shows greater sensitivity to expert disabling than GShard x1.5 (both starting from same 1.808 Pile loss), indicating each expert is more irreplaceable with lower parameter redundancy. Evidence: Figure 4, Section 4.5. Scope: 2B scale, compared against GShard x1.5. Evidence breadth: single scale, qualitative comparison via loss curves (limited evidence).

7. **C7: Shared experts are irreplaceable.** Disabling the shared expert and activating one more routed expert increases Pile loss from 1.808 to 2.414 (33% degradation). Evidence: Section 4.5. Scope: DeepSeekMoE 2B, single shared expert. Evidence breadth: single experiment, single scale (limited evidence but large effect size).

8. **C8: MoE benefits from alignment.** DeepSeekMoE Chat 16B achieves comparable performance with LLaMA2 SFT 7B and DeepSeek Chat 7B, contradicting prior findings that MoE models do not benefit from fine-tuning. Evidence: Table 5, Section 6.2. Scope: 1.4M SFT examples, 19 benchmarks. Evidence breadth: single SFT recipe, same data for all models (moderate evidence for fair comparison).

---

## Open Questions

1. **Optimal expert granularity vs. computational efficiency.** Authors note finer granularity than 0.25x is not used at 16B scale "due to potential reduction in computational efficiency." The 145B model uses 0.125x. What are the precise trade-offs, and can they be mitigated with better GPU kernels? Not addressed in the paper.

2. **Shared expert ratio across scales.** The 1:3 ratio was selected based on 2B experiments with minimal difference between ratios (Pile loss 1.808, 1.806, 1.811). Does this ratio remain optimal at larger scales? Not addressed.

3. **Attention scaling for MoE models.** Given MMLU limitations attributed to limited attention parameters (0.5B in DeepSeekMoE 16B vs 2.5B in DeepSeek 7B), how should attention capacity be scaled alongside MoE-based FFN scaling? Partially addressed by DeepSeek-V2's Multi-head Latent Attention.

4. **Load balance at first layer.** Why does load balance converge slowly at the first layer, and are there architectural modifications that could enable MoE at all layers? Not addressed.

5. **Attention-FFN interaction in MoE.** The paper observes that FFN-heavy MoE excels at knowledge-intensive tasks but underperforms on multiple-choice reasoning. Does FFN-heavy MoE have fundamental limitations for reasoning tasks, or can attention-FFN co-scaling resolve the MMLU gap? Not addressed.

---

## Core References and Why They Are Referenced

### MoE Foundations

- **Jacobs et al. (1991)** -- *Adaptive Mixtures of Local Experts.* Original MoE concept for handling different samples with independent expert modules.

- **Shazeer et al. (2017)** -- *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.* Introduced MoE to language model training with gated routing, establishing the sparsity paradigm DeepSeekMoE builds upon. Also identified routing collapse risk that motivates the balance losses.

### MoE Architectures (Direct Baselines)

- **Lepikhin et al. (2021)** -- *GShard.* Primary baseline architecture using top-2 learnable routing. DeepSeekMoE explicitly demonstrates advantages over GShard at 2B, 16B (implicit), and 145B scales.

- **Fedus et al. (2021)** -- *Switch Transformers.* Top-1 routing baseline in validation experiments, demonstrating MoE scaling to trillion parameters with simple routing.

- **Roller et al. (2021)** -- *Hash Layers for Large Sparse Models.* Top-1 hash-based routing baseline in validation experiments.

- **Rajbhandari et al. (2022)** -- *DeepSpeed-MoE.* Credited as prototype for shared expert isolation from an engineering perspective, while DeepSeekMoE approaches it algorithmically.

### Dense Baselines

- **Touvron et al. (2023b)** -- *LLaMA 2.* Primary dense baseline for DeepSeekMoE 16B comparison, trained on same 2T tokens.

- **DeepSeek-AI (2024)** -- *DeepSeek LLM.* DeepSeek 7B and 67B provide dense baselines trained on identical corpora for fair architectural comparison.

### Transformer Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer architecture whose FFN layers DeepSeekMoE replaces with MoE layers.

### Knowledge and Routing Analysis

- **Dai et al. (2022a)** -- *Knowledge Neurons in Pretrained Transformers.* Supports the proposition that FFNs in Transformers exhibit knowledge memorization capability, explaining why MoE (which scales FFN parameters) excels at knowledge-intensive tasks.

- **Zhou et al. (2022)** -- *Mixture-of-Experts with Expert Choice Routing.* Alternative routing strategy (expert-choice) referenced in related work; not directly compared.

- **Shen et al. (2023)** -- *Flan-MoE.* Finding that MoE models can benefit from instruction tuning, motivating the alignment experiments in Section 6.
