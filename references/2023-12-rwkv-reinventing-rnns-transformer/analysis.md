---
title: "RWKV: Reinventing RNNs for the Transformer Era"
authors: "Peng, Alcaide, Anthony, Albalak, Arcadinho, Biderman, Cao, Cheng, Chung, Du, Grella, GV, He, Hou, Lin, Kazienko, Kocon, Kong, Koptyra, Lau, Mantri, Mom, Saito, Song, Tang, Wang, Wind, Wozniak, Zhang, Zhang, Zhao, Zhou, Zhou, Zhu, Zhu"
year: 2023
venue: "Findings of EMNLP 2023"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "state-space-models"]
scope: ["alternative to Transformers", "linear attention mechanism", "RNN-Transformer hybrid", "efficient inference", "large-scale language modeling"]
benchmarks_used: ["arc", "boolq", "copa", "headqa", "hellaswag", "lambada", "openbookqa", "piqa", "record", "sciq", "winogrande", "lra", "enwik8", "perplexity-pile"]
models_introduced: ["rwkv-169m", "rwkv-430m", "rwkv-1.5b", "rwkv-3b", "rwkv-7b", "rwkv-14b"]
models_evaluated: ["pythia-series", "opt-125m", "opt-350m", "opt-1.3b", "bloom-series", "s4", "transformer-base"]
key_claims:
  - id: C1
    claim: "RWKV achieves competitive performance with similarly sized Transformers on standard NLP benchmarks when matched on compute (FLOPs)"
    evidence: "Figure 1, Figure 5, Section 5.1, Appendix J Figure 12"
    status: supported
    scope: "Zero-shot evaluation, 169M--14B scale, Pile-trained models, twelve NLP tasks"
    magnitude: "Comparable average accuracy across twelve NLP tasks at equivalent FLOPs; tracks within the same accuracy band as Pythia, OPT, and BLOOM at all compute levels"
  - id: C2
    claim: "RWKV achieves O(Td) time complexity and O(d) memory complexity during inference, the lowest among compared architectures"
    evidence: "Table 1, Section 3"
    status: supported
    scope: "Autoregressive inference, compared against Transformer, Reformer, Performer, Linear Transformers, AFT-full, AFT-local, and MEGA"
    magnitude: "Strictly lower than all seven compared architectures in both time and space (e.g., Linear Transformers require O(Td^2) time and O(Td + d^2) space)"
  - id: C3
    claim: "RWKV follows the same log-log linear scaling law as Transformers, with r^2 = 0.994 for Pareto-optimal points"
    evidence: "Figure 4, Section 4.2"
    status: supported
    scope: "45 models trained across varying dataset and parameter sizes"
    magnitude: "r^2 = 0.994 (interpolation), r^2 = 0.875 (extrapolation over one additional order of magnitude)"
  - id: C4
    claim: "Increasing RWKV context length via progressive finetuning yields lower test loss on the Pile"
    evidence: "Figure 6, Section 5.2"
    status: supported
    scope: "7B and 14B models, context extended from 1024 to 8192 tokens via progressive finetuning (10B + 100B + 100B tokens)"
    magnitude: "Monotonically decreasing test loss from context length 2 to 2048 for both 7B and 14B models (Figure 6); 14B consistently lower loss than 7B"
  - id: C5
    claim: "RWKV exhibits linear inference time scaling with sequence length, unlike Transformers which scale quadratically"
    evidence: "Figure 7, Figures 13--14, Section 6, Appendix K"
    status: supported
    scope: "Text generation benchmarks on CPU (x86) and GPU (NVIDIA A100), float32 precision"
    magnitude: "At 1000 tokens, RWKV-3B cumulative time ~10--15s vs ~45--65s for comparably sized Transformers (Figure 7); memory stays near-constant across model sizes up to 14B (Figure 13)"
  - id: C6
    claim: "RWKV is more sensitive to prompt engineering than Transformers due to its inability to look back at previous tokens"
    evidence: "Tables 6--7, Section 9, Appendix L"
    status: supported
    scope: "Zero-shot comparison with ChatGPT and GPT-4 on RTE, WNLI, GoEmotions, PolEmo2, Aggression, MathQA, Sarcasm, TweetSent, Unhealthy"
    magnitude: "F1 on RTE increased from 44.2% to 74.8% with re-ordered prompts; on sarcasm detection RWKV 50.96 vs ChatGPT 49.88 F1"
  - id: C7
    claim: "RWKV performs second only to S4 on the Long Range Arena benchmark, substantially outperforming standard Transformers"
    evidence: "Table 4, Appendix J.2"
    status: supported
    scope: "LRA benchmark with sequences 1K--16K tokens; five tasks tested (Path-X not evaluated for RWKV)"
    magnitude: "RWKV avg 72.07 vs S4 avg 86.09 vs Transformer avg 53.66; RWKV near S4 on Text (86.04 vs 86.82) and Retrieval (88.34 vs 90.90)"
  - id: C8
    claim: "RWKV achieves competitive bits-per-character on Enwik8 with linear time and constant space complexity"
    evidence: "Table 5, Appendix J.3"
    status: supported
    scope: "Enwik8 character-level modeling, 12 layers, d=512, T=1024, with regularization"
    magnitude: "1.178 bpc vs 1.137 bpc (Transformer, 12 layers) and 1.130 bpc (Transformer, 24 layers), while having O(Td) time and O(d) space vs O(T^2 d) time and O(T^2 + Td) space"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "RWKV replaces Transformer's quadratic dot-product attention with a linear attention mechanism while maintaining parallelizable training"
  - target: 2022-04-s4-structured-state-spaces
    type: complementary
    detail: "Both propose subquadratic alternatives to Transformers; S4 outperforms RWKV on LRA but RWKV scales to 14B parameters"
  - target: 2024-05-mamba-selective-state-spaces
    type: complementary
    detail: "Mamba introduces selective SSMs as a concurrent approach to linear-time sequence modeling; both achieve Transformer-level performance at scale"
  - target: 2022-12-flashattention
    type: complementary
    detail: "FlashAttention improves Transformer memory efficiency but retains quadratic time complexity; RWKV achieves linear time and constant memory"
  - target: 2020-12-bigbird-sparse-attention
    type: complementary
    detail: "BigBird uses sparse attention patterns; RWKV replaces attention entirely with a linear recurrence"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer combines local and global attention for long documents; RWKV uses channel-wise time decay for linear complexity"
  - target: 2024-10-rwkv-eagle-finch-matrix-states
    type: extended-by
    detail: "Eagle (RWKV-5) and Finch (RWKV-6) extend RWKV-4 with matrix-valued states and data-dependent recurrence, substantially improving expressivity and multilingual performance"
open_questions:
  - question: "Can RWKV's limited ability to recall minutiae over very long contexts be addressed without sacrificing linear complexity?"
    addressed_by: 2024-10-rwkv-eagle-finch-matrix-states
  - question: "How does RWKV perform with encoder-decoder architectures for seq2seq or multimodal tasks?"
    addressed_by: null
  - question: "Can parallel scan reduce WKV computation cost to O(B log(T) d) in practice?"
    addressed_by: null
  - question: "Can prompt engineering guidelines specific to RNN architectures systematically close the gap with Transformers on reasoning tasks?"
    addressed_by: null
  - question: "Can RWKV's mathematical reasoning weakness (5.43% on MathQA with CoT) be resolved through architectural changes or improved prompting?"
    addressed_by: null
---

# RWKV: Reinventing RNNs for the Transformer Era

**Authors:** Bo Peng*, Eric Alcaide*, Quentin Anthony*, et al. (Generative AI Commons, EleutherAI, University of Barcelona, and 27 other institutions; * equal first authorship)
**Date:** December 2023, Findings of EMNLP 2023, arXiv:2305.13048

---

## Core Research Problem

Transformers dominate NLP but suffer from **O(T^2 d) time and O(T^2 + Td) memory complexity** during inference due to the self-attention mechanism (Table 1, Section 1), making them inefficient for long sequences. RNNs offer linear scaling in time and constant memory during inference but are limited by the vanishing gradient problem (Hochreiter, 1998; Le and Zuidema, 2016) and the inability to parallelize training across the time dimension. Previous efficient attention variants such as Reformer (O(T log T d) time), Performer (O(Td^2 log d) time), and Linear Transformers (O(Td^2) time) reduce complexity but still involve approximations or hidden factors (Table 1). State space models (S4) show promise on the Long Range Arena but had not been scaled beyond hundreds of millions of parameters at the time of this work.

**The core challenge: how to combine Transformer-level parallelizable training with RNN-level efficient inference at the scale of billions of parameters.**

---

## Problem Solutions

RWKV (Receptance Weighted Key Value) addresses this challenge through a linear attention mechanism that admits **dual formulations** -- as a Transformer during training and as an RNN during inference.

1. **Linear attention via channel-wise time decay:** Replace the pairwise attention matrix with a channel-wise exponentially decaying weight vector, enabling both parallel (training) and sequential (inference) computation.
2. **Token shift mechanism:** Use linear interpolation between current and previous timestep inputs to capture temporal dependencies without explicit recurrence during the forward pass.
3. **Custom initializations and small-init embedding:** Stabilize training of deep architectures through carefully designed parameter initialization and small embedding initialization with LayerNorm.

---

## Approach Details

### Method

RWKV builds on the Attention Free Transformer (AFT) formulation by Zhai et al. (2021). In AFT, attention is computed as (eq. 9, Section 2.2):

> `Attn+(W, K, V)_t = (sum_{i=1}^{t} e^{w_{t,i} + k_i} * v_i) / (sum_{i=1}^{t} e^{w_{t,i} + k_i})`

where `{w_{t,i}} in R^{T x T}` are learned pairwise position biases. RWKV simplifies this by constraining the position weights to be a **channel-wise time decay** (eq. 10):

> `w_{t,i} = -(t - i) * w`

where `w in (R_>=0)^d`, ensuring `e^{w_{t,i}} <= 1` and that weights decay backward in time. This constraint transforms the AFT into a recurrence.

The **WKV operator** is defined as (eq. 16, Section 3.1.2):

> `wkv_t = (sum_{i=1}^{t-1} e^{-(t-1-i)w + k_i} * v_i + e^{u + k_t} * v_t) / (sum_{i=1}^{t-1} e^{-(t-1-i)w + k_i} + e^{u + k_t})`

where `u` is a separate learned vector that attends to the current token independently of the time decay.

Each RWKV block consists of a **time-mixing** sub-block and a **channel-mixing** sub-block with residual connections (Figure 2). All projection vectors are computed from linear interpolation of current and previous inputs (token shift, eqs. 11--15):

> `r_t = W_r * (mu_r . x_t + (1 - mu_r) . x_{t-1})`
> `k_t = W_k * (mu_k . x_t + (1 - mu_k) . x_{t-1})`
> `v_t = W_v * (mu_v . x_t + (1 - mu_v) . x_{t-1})`

where `.` denotes element-wise multiplication. Channel-mixing inputs `r'_t` and `k'_t` follow the same pattern (eqs. 14--15).

Output gating applies the sigmoid of the receptance (eq. 17):

> `o_t = W_o * (sigma(r_t) . wkv_t)`

The channel-mixing block uses squared ReLU activation (eq. 18, from So et al., 2021):

> `o'_t = sigma(r'_t) . (W'_v * max(k'_t, 0)^2)`

### Key Technical Components

**Dual formulation.** During training (time-parallel mode), the WKV computation is parallelized across batch and channel dimensions with complexity O(BTd) for the scan and O(BTd^2) for the matrix multiplications (same as Transformers, Section 3.2). During inference (time-sequential mode), the WKV operator admits a recursive formulation with state `(a_t, b_t)` (Appendix D, eqs. 19--22):

> `a_0, b_0 = 0`
> `wkv_t = (a_{t-1} + e^{u + k_t} . v_t) / (b_{t-1} + e^{u + k_t})`
> `a_t = e^{-w} . a_{t-1} + e^{k_t} . v_t`
> `b_t = e^{-w} . b_{t-1} + e^{k_t}`

This gives O(d) memory per layer during inference, compared to O(Td) for Transformers caching all key-value pairs.

**Numerical stability trick.** To avoid overflow in computing `e^{k_t}`, the implementation uses a shared exponent `p_t` (Appendix D, eqs. 23--28):

> `q = max(p_{t-1}, u + k_t)`
> `wkv_t = (e^{p_{t-1} - q} . a'_{t-1} + e^{u + k_t - q} . v_t) / (e^{p_{t-1} - q} . b'_{t-1} + e^{u + k_t - q})`

with corresponding updates for `a'_t`, `b'_t`, and `p_t = max(p_{t-1} - w, k_t)`.

**Internal state size.** Each layer stores five vectors of dimension D: current time-mix input, current channel-mix input, WKV numerator `a'_t`, WKV denominator `b'_t`, and auxiliary exponent `p_t` for numerical stability. Total internal state size: **5DL** (or 4DL algebraically without the numerical helper) (Appendix D).

**Custom CUDA kernel.** A custom kernel executes the WKV scan as a single compute operation on GPU, avoiding the inefficiency of sequential operations in standard frameworks (Section 3.4).

**Small init embedding.** Embedding matrix initialized with small values (U(+-1e-4)) followed by LayerNorm accelerates convergence by enabling rapid departure from the initial noisy embedding state (Figure 9, Appendix F). The small init embedding curve reaches lower loss values earlier in training compared to the standard N(0, 0.02) initialization, while both converge to approximately the same final loss.

**Parameter initialization (Appendix E).** Token shift mixing parameters `mu` are initialized as functions of layer depth `l` and channel index `i`:
- Time-mixing: `mu_{k_i} = (i/s)^{1 - l/L}`, `mu_{v_i} = (i/s)^{1 - l/L} + 0.3l/(L-1)`, `mu_{r_i} = 0.5 * (i/s)^{1 - l/L}`
- Channel-mixing: `mu_{k_i}` and `mu_{r_i}` initialized to `(i/s)^{1 - l/L}`
- Time decay `w_i` initialized to `-5 + 8 * (i/(d-1))^{0.7 + 1.3l/(L-1)}`
- Bonus `u_i` set to `0.5 * (((i+1) mod 3) - 1) + log 0.3`
- `W_o` (time-mixing) and `W'_v` (channel-mixing) initialized from `N(0, sqrt(d/s))` where `d = 4s`, yielding std dev = 2
- All other `W_r, W_k, W_v` weights initialized to 0; LayerNorm weights start from 1, biases from 0

### Theoretical Analysis

**Gradient stability (Appendix H).** The authors prove that if inputs `x_t` are bounded and model parameters are fixed, the gradients with respect to `W_k` and `W_v` are **uniformly bounded for all T** (not exploding). The key results are:

> `|d(wkv_T)_i / d(W_v)_{i,j}| = |E_i[(x_t)_j]| <= max_t |(x_t)_j|`   (eq. 32)

which is **independent of T**, and:

> `d(wkv_T)_i / d(W_k)_{i,j} = cov_i((x_t)_j, (v_t)_i)`   (eq. 33)

which is also bounded. The `wkv` softmax operation always contains at least two non-zero terms (`u` and `w`), preventing degeneration. This means the amount each `x_t` contributes to the gradient at position T is controlled in a naturally decaying fashion by the weight decay mechanism `w` -- gradients neither explode nor vanish unless the decay is designed to do so.

### Experimental Setup

**Models:** Six RWKV models from 169M to 14B parameters (Table 2):

| Name | Layers | Model Dimension | Parameters | FLOP per token |
|---|---|---|---|---|
| 169M | 12 | 768 | 1.693 x 10^8 | 2.613 x 10^8 |
| 430M | 24 | 1024 | 4.304 x 10^8 | 7.573 x 10^8 |
| 1.5B | 24 | 2048 | 1.515 x 10^9 | 2.823 x 10^9 |
| 3B | 32 | 2560 | 2.985 x 10^9 | 5.710 x 10^9 |
| 7B | 32 | 4096 | 7.393 x 10^9 | 1.437 x 10^10 |
| 14B | 40 | 5120 | 1.415 x 10^10 | 2.778 x 10^10 |

Parameter count formula: `# parameters = 2VD + 13D^2L + D(11L + 4)` where V = 50277.

**Training:** All models trained for one epoch on the Pile (330B tokens), context length 1024, bfloat16 precision, Adam optimizer (epsilon = (0.9, 0.99)) without weight decay, exponential learning rate decay from an initial constant phase, PaLM auxiliary loss (Chowdhery et al., 2022), batch size dynamically switched between 128 or 256 sequences (Section 4.1, Appendix G).

**Learning rate schedule (Table 3):**

| Model | Init LR | Warmup Mini-Epochs | End LR |
|---|---|---|---|
| 169M | 0.0006 | 361 | 0.00001 |
| 430M | 0.0004 | 411 | 0.00001 |
| 1.5B | 0.0003 | 443 | 0.00001 |
| 3B | 0.00015 | 451 | 0.00001 |
| 7B | 0.00015 | 465 | 0.00001 |
| 14B | 0.0001 | 544 | 0.000007 |

Training is organized into 8043 mini-epochs of 40320 samples each to complete one pass over the Pile.

**Baselines:** Pythia (Biderman et al., 2023), OPT (Zhang et al., 2022), BLOOM (Scao et al., 2022) -- all trained on comparable token budgets. Comparison is FLOP-matched to ensure fairness (Section 5.1). The authors avoid comparing with models trained in the Chinchilla-optimal regime or the overtrained regime.

**Evaluation:** Zero-shot on 12 NLP tasks: ARC (Easy/Challenge), BoolQ, COPA, HeadQA, HellaSwag, LAMBADA, OpenBookQA, PIQA, ReCoRD, SciQ, Winogrande. Additionally: LRA benchmark (5 tasks), Enwik8 perplexity, extended context finetuning on Pile, prompt engineering comparison with ChatGPT and GPT-4 (Appendix L).

**Reproducibility:** Code released at https://github.com/BlinkDL/RWKV-LM; pretrained models at https://huggingface.co/RWKV. Training hyperparameters fully specified (Table 3, Appendix G). Custom CUDA kernel provided. All inference experiments use float32 precision with HuggingFace Transformers.

### Key Results

**NLP Benchmarks (Figure 1, Figure 5, Appendix J Figure 12):** RWKV performs comparably to Pythia, OPT, and BLOOM at equivalent compute budgets across all 12 zero-shot benchmarks (tested at six model sizes from 169M to 14B, strong evidence across scales). The average accuracy across tasks follows the same compute scaling trend as Transformer baselines. No exact numerical per-task per-model table is provided in the paper; comparisons are shown as FLOP-accuracy plots.

**Scaling Laws (Figure 4, Section 4.2):** RWKV follows the same log-log linear scaling form established for Transformers (Kaplan et al., 2020). Linear fit to Pareto-optimal points achieves **r^2 = 0.994**; extrapolation over an additional order of magnitude achieves **r^2 = 0.875** (45 models trained, moderate-to-strong evidence).

**Long Range Arena (Table 4, Appendix J.2):**

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Path-X | Avg |
|---|---|---|---|---|---|---|---|
| S4 | **59.60** | **86.82** | **90.90** | **88.65** | **94.20** | **96.35** | **86.09** |
| RWKV | 55.88 | 86.04 | 88.34 | 70.53 | 58.42 | X | 72.07 |
| Transformer | 36.37 | 64.27 | 57.46 | 42.44 | 71.40 | X | 53.66 |
| Reformer | 37.27 | 56.10 | 53.40 | 38.07 | 68.50 | X | 50.56 |
| BigBird | 36.05 | 64.02 | 59.29 | 40.83 | 74.87 | X | 54.17 |
| Linear Trans. | 16.13 | 65.90 | 53.09 | 42.34 | 75.30 | X | 50.46 |
| Performer | 18.01 | 65.40 | 53.82 | 42.77 | 77.05 | X | 51.18 |
| FNet | 35.33 | 65.11 | 59.61 | 38.67 | 77.80 | X | 54.42 |
| Nystromformer | 37.15 | 65.52 | 79.56 | 41.58 | 70.94 | X | 57.46 |
| Luna-256 | 37.25 | 64.57 | 79.29 | 47.38 | 77.72 | X | 59.37 |
| Hrrformer | 39.98 | 65.38 | 76.15 | 50.45 | 72.17 | X | 60.83 |

RWKV ranks second overall. It performs near S4 on text (86.04 vs 86.82) and retrieval (88.34 vs 90.90) but substantially underperforms on Image (70.53 vs 88.65) and Pathfinder (58.42 vs 94.20). Path-X was not evaluated for RWKV. Other models' performances are cited from Gu et al. (2022) and Alam et al. (2023).

**Enwik8 (Table 5, Appendix J.3):**

| Method | L | d | T | Train bpc | Test bpc | Time | Space |
|---|---|---|---|---|---|---|---|
| Transformer | 12 | 512 | 1024 | 0.977 | 1.137 | O(T^2 d) | O(T^2 + Td) |
| Transformer | 24 | 256 | 1024 | 1.039 | 1.130 | O(T^2 d) | O(T^2 + Td) |
| Reformer | 12 | 512 | 1024 | 1.040 | 1.195 | O(T log T d) | O(T log T + Td) |
| Synthesizer | 12 | 512 | 1024 | 0.994 | 1.298 | O(T^2 d) | O(T^2 + Td) |
| Linear Transformer | 12 | 512 | 1024 | 0.981 | 1.207 | O(Td^2) | O(Td + d^2) |
| Performer | 12 | 512 | 1024 | 1.002 | 1.199 | O(Td^2 log d) | O(Td log d + d^2 log d) |
| AFT-simple | 12 | 512 | 1024 | 1.046 | 1.209 | O(Td) | O(Td) |
| RWKV-RNN (no reg.) | 6 | 512 | 1024 | 0.720 | -- | O(Td) | O(d) |
| RWKV-RNN (reg.) | 12 | 512 | 1024 | 1.010 | **1.178** | O(Td) | O(d) |

RWKV-RNN with regularization (12 layers, AdamW, weight decay 0.1, dropout 0.1) achieves **1.178 bpc**, competitive with the Transformer at 1.137 bpc (12 layers) and 1.130 bpc (24 layers), while having strictly lower time complexity O(Td) and constant space complexity O(d). The 6-layer variant without regularization overfits (0.720 train bpc, no test bpc reported).

**Inference Efficiency (Figure 7, Figures 13--14, Section 6, Appendix K):** RWKV exhibits **linear time scaling** with sequence length during text generation, while Transformers scale quadratically. At 1000 tokens (Figure 7), RWKV-3B takes ~10--15 seconds vs ~45--65 seconds for comparably sized Transformers (OPT-2.7B, GPT-Neo-2.7B, BLOOM-3B, Pythia-2.8B). Memory usage (Figure 13) remains near-constant regardless of sequence length: ~1 GB CPU RAM and ~2.5 GB GPU VRAM for all RWKV sizes up to 14B (excluding model parameters), while Transformer memory grows steeply. All inference experiments use float32 precision.

**Extended Context (Figure 6, Section 5.2):** Progressive finetuning -- 1024 to 2048 tokens (10B tokens), then to 4096 (100B tokens), then to 8192 (100B tokens) -- yields **monotonically decreasing test loss** on the Pile for both 7B and 14B models. Evidence is limited to perplexity on a single dataset.

**Prompt Engineering Comparison (Tables 6--7, Appendix L):**

ChatGPT, GPT-4, and RWKV-4-Raven-14B comparison (Table 6):

| Task | Measure | ChatGPT | GPT-4 | RWKV-GPT | RWKV-adapted | SOTA |
|---|---|---|---|---|---|---|
| RTE | F1 Macro | 88.1 | **91.3** | 44.2 | 74.8 | 92.1 |
| WNLI | Accuracy | 81.7 | **91.6** | 47.9 | 49.3 | 97.9 |
| GoEmotions | F1 Macro | **25.6** | 23.1 | 7.9 | 7.9 | 52.8 |
| PolEmo2 | F1 Macro | **44.1** | 41.0 | 38.2 | 40.9 | 76.4 |

ChatGPT and RWKV-4-Raven-14B comparison (Table 7):

| Task | Measure | ChatGPT | RWKV-adapted | SOTA |
|---|---|---|---|---|
| Aggression | F1 Macro | **69.10** | 56.66 | 74.45 |
| MathQA | Accuracy | **71.40** | 5.43 | 83.20 |
| Sarcasm | F1 Macro | 49.88 | **50.96** | 53.57 |
| TweetSent | F1 Macro | **63.32** | 52.50 | 72.07 |
| Unhealthy | F1 Macro | **45.21** | 43.30 | 50.96 |

The key finding is that **prompt ordering matters substantially more for RWKV** than for Transformers. The authors hypothesize that because RNN-based architectures cannot look back and readjust previous information, placing desired information *after* the main question improves results. On sarcasm detection, RWKV with adapted prompts **outperforms ChatGPT** (50.96 vs 49.88 F1). On MathQA, RWKV achieved only 5.43% with chain-of-thought and 4.13% without, suggesting fundamental limitations in sequential mathematical reasoning (single task, limited evidence for generalization).

### Model Behavior Visualization

**Time decay patterns (Figure 10, Appendix I):** Visualization of `e^{-w}` in each layer of RWKV-169M shows that initial layers have many decays close to zero (corresponding to local operations), while later layers have decays close to one (preserving information across long temporal contexts). This pattern arises partly from the initialization design and partly from learning.

**Causal trace experiment (Figure 11, Appendix I):** Following Meng et al. (2022), a causal trace analysis on RWKV-430M reveals that factual knowledge retrieval ("The Eiffel Tower is located in Paris") occurs in early layers (~4) around the subject tokens, then propagates forward through time in later layers (~20) until the prediction position.

---

## Limitations and Failure Modes

1. **Limited recall over long contexts.** The linear attention mechanism funnels all past information through a fixed-size state vector (5DL total), mechanistically limiting the model's ability to recall minutiae over very long contexts compared to full self-attention which maintains O(T^2 + Td) state (Section 9).

2. **Prompt sensitivity.** RWKV is substantially more sensitive to prompt ordering than Transformers because the RNN formulation cannot "look back" at earlier tokens. Re-ordering prompts for the RTE task improved F1 from 44.2% to 74.8% (Table 6, Appendix L). This sensitivity was confirmed across multiple tasks (Tables 6--7, nine benchmarks total).

3. **Weak mathematical reasoning.** RWKV-4-Raven-14B achieved only **5.43%** accuracy on MathQA with chain-of-thought prompting (4.13% without CoT), compared to 71.4% for ChatGPT (Table 7, Appendix L). The model struggled particularly with questions requiring intermediate results.

4. **Underperformance on spatial tasks.** On LRA Image and Pathfinder tasks, RWKV substantially underperforms S4 (70.53 vs 88.65 on Image; 58.42 vs 94.20 on Pathfinder), suggesting limitations in modeling 2D spatial structure (Table 4). Path-X was not evaluated for RWKV.

5. **[Inferred] No evaluation on non-English languages.** All benchmarks are English-only, limiting generalizability claims to multilingual settings.

6. **[Inferred] No standard long-context NLP evaluation.** The paper evaluates perplexity improvement with longer context but does not report results on long-context NLP benchmarks such as SCROLLS or LongBench.

### Scope and Comparability

- **Training context length.** All RWKV models were pretrained with context length 1024 tokens, shorter than many contemporary Transformer baselines. Extended context was achieved through progressive finetuning (up to 8192), not pretraining.
- **Comparison fairness.** Comparisons are FLOP-matched with Pythia, OPT, and BLOOM, all trained on the Pile. The paper deliberately avoids comparing with Chinchilla-optimal or overtrained models (Section 5.1).
- **LRA baseline sourcing.** LRA results for other models are cited from Gu et al. (2022) and Alam et al. (2023), not reproduced by the authors, introducing potential comparability issues across different implementations.
- **Inference precision.** All inference benchmarks use float32 precision; performance under quantization was explicitly left to future work (Section 6).
- **NLP results are figure-based.** Per-task per-model numerical tables are not provided in the main text; comparisons are presented as FLOP-accuracy plots (Figures 1, 5, 12), making precise numerical comparison difficult.

---

## Conclusions

### Contributions

1. **Novel RNN-Transformer hybrid architecture.** RWKV combines parallelizable training (like Transformers) with efficient O(d) memory inference (like RNNs) through a linear attention mechanism based on channel-wise time decay. The dual formulation is exact (no approximation involved), and the architecture achieves the **lowest inference complexity** among all compared methods (Table 1).

2. **Scaling to 14B parameters.** RWKV is the largest dense RNN ever trained at the time of publication, demonstrating that non-Transformer architectures can scale to billions of parameters with competitive performance (six model sizes, twelve NLP benchmarks).

3. **Transformer-like scaling laws.** RWKV follows the same log-log linear scaling relationship as Transformers, with r^2 = 0.994 on Pareto-optimal compute-loss points across 45 models (Figure 4).

4. **Gradient stability guarantee.** The WKV formulation provides uniformly bounded gradients with respect to `W_k` and `W_v` regardless of sequence length T (Appendix H), providing a theoretical basis for the architecture's trainability.

5. **Comprehensive open release.** Code, pretrained models (169M--14B), and full hyperparameter specifications are released, enabling reproducibility and community adoption.

### Implications

1. **Viability of linear-complexity models.** The competitive NLP performance at scale suggests that quadratic attention may not be strictly necessary for language modeling, opening a path for more efficient large-scale deployment (supported by consistent results across six model sizes).

2. **Prompt engineering for RNN-based models.** The increased sensitivity to prompt ordering implies that RNN-based LLMs may require fundamentally different prompting strategies than Transformers (speculative -- requires systematic study beyond the nine tasks examined).

3. **Edge deployment potential.** Constant memory inference makes RWKV suitable for consumer and edge hardware, potentially democratizing LLM access (noted by authors in Ethics Statement, Section 10).

---

## Key Claims

1. **C1: Competitive with Transformers at matched compute.** RWKV performs on par with Pythia, OPT, and BLOOM across twelve zero-shot NLP benchmarks when compared at equivalent FLOPs (Figure 1, Figure 5, Appendix J). Evidence spans six model sizes (169M--14B) with consistent trends (strong evidence across scales). No exact numerical table is provided; comparisons are FLOP-accuracy plots. Scope: zero-shot, Pile-trained models, English-only benchmarks. Magnitude: comparable average accuracy, tracking within the same accuracy band as Transformer baselines.

2. **C2: Lowest inference complexity.** RWKV achieves O(Td) time and O(d) space during inference, strictly lower than all seven compared methods including Linear Transformers at O(Td^2) time and Reformer at O(T log T d) time (Table 1). This is a theoretical property of the architecture, confirmed by the linear time scaling in Figure 7 and constant memory in Figure 13. Scope: autoregressive inference. Magnitude: strictly lower complexity class than all baselines.

3. **C3: Transformer-like scaling laws.** The loss-compute relationship for RWKV follows the same log-log linear form as Transformers, with r^2 = 0.994 on Pareto-optimal points across 45 trained models (Figure 4, Section 4.2). The fit holds with r^2 = 0.875 when extrapolated an order of magnitude. Scope: varying dataset and parameter sizes. Magnitude: r^2 = 0.994 interpolation, r^2 = 0.875 extrapolation (moderate evidence -- single architecture family).

4. **C4: Effective use of extended context.** Progressive finetuning from 1024 to 8192 tokens (10B + 100B + 100B tokens at each doubling) yields monotonically decreasing test loss on the Pile for both 7B and 14B models (Figure 6). Scope: Pile perplexity only, two model sizes. Magnitude: monotonically decreasing loss curves across context lengths 2--2048 (limited evidence -- single dataset, no downstream task evaluation).

5. **C5: Linear inference time scaling.** RWKV generates text with linear time scaling in sequence length, while Transformers show quadratic growth (Figure 7). At 1000 tokens, RWKV-3B takes ~10--15s vs ~45--65s for Transformer baselines. Memory remains near-constant (Figures 13--14). Scope: CPU (x86) and GPU (A100), float32 precision. Magnitude: ~3--5x faster at 1000 tokens, with the gap widening at longer sequences (tested on five model families, strong evidence).

6. **C6: Increased prompt sensitivity.** RWKV is substantially more sensitive to prompt ordering than Transformers. On RTE, re-ordering prompts increased F1 from 44.2% to 74.8% (Table 6). On sarcasm detection, RWKV with adapted prompts outperformed ChatGPT (50.96 vs 49.88 F1, Table 7). Scope: zero-shot on nine NLP tasks, RWKV-4-Raven-14B vs ChatGPT/GPT-4. Magnitude: up to 30.6 percentage point improvement from prompt re-ordering (RTE).

7. **C7: Second-best on Long Range Arena.** RWKV ranks second only to S4 across five LRA tasks with average accuracy 72.07 vs S4's 86.09 and Transformer's 53.66 (Table 4). Near-parity with S4 on text (86.04 vs 86.82) and retrieval (88.34 vs 90.90), but large gaps on Image (70.53 vs 88.65) and Pathfinder (58.42 vs 94.20). Scope: LRA benchmark, five tasks (Path-X not tested). Magnitude: avg 72.07, +18.41 over Transformer.

8. **C8: Competitive Enwik8 character-level modeling.** RWKV achieves 1.178 bpc with 12 layers, d=512, T=1024 with regularization, vs 1.137 bpc for a Transformer with the same architecture and 1.130 bpc for a deeper 24-layer Transformer (Table 5). Scope: Enwik8, single configuration. Magnitude: 0.041 bpc gap from matched Transformer, 0.048 bpc gap from deeper Transformer, while having O(Td) time and O(d) space.

---

## Open Questions

1. **Can RWKV's recall limitations over long contexts be mitigated without sacrificing linear complexity?** The authors suggest enhancing time-decay formulations and exploring initial model states (Section 7). Partially addressed by Eagle/Finch (RWKV-5/6) which introduce matrix-valued states.

2. **How would RWKV perform in encoder-decoder architectures for seq2seq or multimodal settings?** The authors propose replacing cross-attention with RWKV mechanisms (Section 7). Not yet tested.

3. **Can parallel scan reduce WKV computation to O(B log(T) d)?** The authors reference Martin and Cundy (2017) for parallelizing over sequence length (Section 3.2). Not implemented in this work.

4. **Can systematic prompt engineering guidelines for RNN architectures close the gap with Transformers on reasoning tasks?** The paper shows significant gains from prompt re-ordering but does not establish general guidelines (Appendix L, Tables 6--7).

5. **Can RWKV's mathematical reasoning weakness (5.43% on MathQA with CoT) be resolved through architectural changes or improved prompting?** Even with chain-of-thought, RWKV achieved only 5.43% vs ChatGPT's 71.4% (Appendix L). The order of information in math problems may be fundamentally challenging for sequential processing.

---

## Core References and Why They Are Referenced

### Attention Mechanism Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture and quadratic self-attention mechanism that RWKV aims to replace.
- **Zhai et al. (2021)** -- *An Attention Free Transformer.* Proposes AFT with pairwise position biases; RWKV directly builds on this formulation by constraining biases to channel-wise time decay.
- **Katharopoulos et al. (2020)** -- *Transformers Are RNNs.* Establishes the connection between linear attention and RNNs that RWKV exploits for dual-mode computation; also used as a baseline in Enwik8 experiments.

### Efficient Architecture Alternatives

- **Gu et al. (2022)** -- *Efficiently Modeling Long Sequences with Structured State Spaces.* S4 achieves strong results on LRA and serves as the primary non-Transformer baseline on the long-range benchmark; also source for LRA comparison numbers.
- **Dao et al. (2022)** -- *FlashAttention.* Hardware-aware exact attention that reduces memory but retains quadratic time complexity; contrasted with RWKV's linear approach in Appendix C.
- **Beltagy et al. (2020)** -- *Longformer.* Local+global sparse attention for long documents; RWKV achieves better complexity guarantees.

### Transformer Baselines

- **Biderman et al. (2023)** -- *Pythia.* Primary Transformer baseline for FLOP-matched comparison across model scales.
- **Zhang et al. (2022)** -- *OPT.* Open pre-trained Transformer language models used as baselines.
- **Scao et al. (2022)** -- *BLOOM.* Open multilingual Transformer used as baseline.
- **Brown et al. (2020)** -- *GPT-3.* Demonstrates Transformer scaling; motivates the need for more efficient architectures.

### Scaling Laws

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Establishes the log-log linear scaling framework that RWKV is shown to follow; also noted that LSTMs do not strictly follow the same scaling, which RWKV contradicts.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models.* Chinchilla scaling laws; RWKV comparisons deliberately avoid Chinchilla-optimal models for fairness.

### Training Data and Infrastructure

- **Gao et al. (2020)** -- *The Pile.* The 800GB dataset used to train all RWKV models (one epoch, 330B tokens).
- **Chowdhery et al. (2022)** -- *PaLM.* Source of the auxiliary loss incorporated into RWKV training.

### Interpretability

- **Meng et al. (2022)** -- *Locating and Editing Factual Associations in GPT.* Causal trace method used to analyze information retrieval and propagation patterns in RWKV (Appendix I).

### RNN and Recurrence Foundations

- **Hochreiter and Schmidhuber (1997)** -- *Long Short-Term Memory.* LSTM formulation reviewed in background; RWKV aims to overcome LSTM's training parallelization limitations.
- **Bradbury et al. (2017)** -- *Quasi-Recurrent Neural Networks.* Most similar prior work to RWKV; QRNN uses convolutional filters with fixed sizes while RWKV employs time-decaying attention.
