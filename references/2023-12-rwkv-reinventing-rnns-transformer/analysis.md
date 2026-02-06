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
    evidence: "Figure 1, Figure 5, Section 5.1"
    status: supported
    scope: "Zero-shot evaluation, 169M--14B scale, Pile-trained models"
    magnitude: "Comparable average accuracy across twelve NLP tasks"
  - id: C2
    claim: "RWKV achieves O(Td) time complexity and O(d) memory complexity during inference, the lowest among compared architectures"
    evidence: "Table 1, Section 3"
    status: supported
    scope: "Autoregressive inference"
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
    scope: "7B and 14B models, context extended from 1024 to 8192 tokens"
  - id: C5
    claim: "RWKV exhibits linear inference time scaling with sequence length, unlike Transformers which scale quadratically"
    evidence: "Figure 7, Section 6"
    status: supported
    scope: "Text generation benchmarks on CPU (x86) and GPU (NVIDIA A100)"
  - id: C6
    claim: "RWKV is more sensitive to prompt engineering than Transformers due to its inability to look back at previous tokens"
    evidence: "Tables 6--7, Section 9, Appendix L"
    status: supported
    scope: "Zero-shot comparison with ChatGPT and GPT-4"
    magnitude: "F1 on RTE increased from 44.2% to 74.8% with re-ordered prompts"
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
---

# RWKV: Reinventing RNNs for the Transformer Era

**Authors:** Bo Peng, Eric Alcaide, Quentin Anthony, et al. (Generative AI Commons, EleutherAI, and 27 other institutions)
**Date:** December 2023, Findings of EMNLP 2023, arXiv:2305.13048

---

## Core Research Problem

Transformers dominate NLP but suffer from **O(T^2 d) time and O(T^2 + Td) memory complexity** during inference due to the self-attention mechanism, making them inefficient for long sequences. RNNs offer linear scaling in time and constant memory during inference but are limited by the vanishing gradient problem and the inability to parallelize training across the time dimension. Previous efficient attention variants (Reformer, Performer, Linear Transformers) reduce complexity but still involve approximations or hidden quadratic factors. State space models (S4) show promise but had not been scaled beyond hundreds of millions of parameters.

**The core challenge: how to combine Transformer-level parallelizable training with RNN-level efficient inference at the scale of billions of parameters.**

---

## Problem Solutions

RWKV (Receptance Weighted Key Value) addresses this challenge through a linear attention mechanism that admits **dual formulations** — as a Transformer during training and as an RNN during inference.

1. **Linear attention via channel-wise time decay:** Replace the pairwise attention matrix with a channel-wise exponentially decaying weight vector, enabling both parallel (training) and sequential (inference) computation.
2. **Token shift mechanism:** Use linear interpolation between current and previous timestep inputs to capture temporal dependencies without explicit recurrence during the forward pass.
3. **Custom initializations and small-init embedding:** Stabilize training of deep architectures through carefully designed parameter initialization and small embedding initialization with LayerNorm.

---

## Approach Details

### Method

RWKV builds on the Attention Free Transformer (AFT) formulation by Zhai et al. (2021). In AFT, attention is computed as:

> `Attn+(W, K, V)_t = (sum_{i=1}^{t} e^{w_{t,i} + k_i} * v_i) / (sum_{i=1}^{t} e^{w_{t,i} + k_i})`

where `{w_{t,i}}` are learned pairwise position biases. RWKV simplifies this by constraining the position weights to be a **channel-wise time decay**:

> `w_{t,i} = -(t - i) * w`

where `w in (R_>=0)^d`, ensuring `e^{w_{t,i}} <= 1` and that weights decay backward in time. This constraint transforms the AFT into a recurrence.

The **WKV operator** is defined as:

> `wkv_t = (sum_{i=1}^{t-1} e^{-(t-1-i)w + k_i} * v_i + e^{u + k_t} * v_t) / (sum_{i=1}^{t-1} e^{-(t-1-i)w + k_i} + e^{u + k_t})`

where `u` is a separate learned vector that attends to the current token independently of the time decay.

Each RWKV block consists of a **time-mixing** sub-block and a **channel-mixing** sub-block with residual connections. All projection vectors are computed from linear interpolation of current and previous inputs (token shift):

> `r_t = W_r * (mu_r * x_t + (1 - mu_r) * x_{t-1})`
> `k_t = W_k * (mu_k * x_t + (1 - mu_k) * x_{t-1})`
> `v_t = W_v * (mu_v * x_t + (1 - mu_v) * x_{t-1})`

Output gating applies the sigmoid of the receptance:

> `o_t = W_o * (sigma(r_t) * wkv_t)`

The channel-mixing block uses squared ReLU activation:

> `o'_t = sigma(r'_t) * (W'_v * max(k'_t, 0)^2)`

### Key Technical Components

**Dual formulation.** During training (time-parallel mode), the WKV computation is parallelized across batch and channel dimensions with complexity O(BTd) for the scan and O(BTd^2) for the matrix multiplications (same as Transformers). During inference (time-sequential mode), the WKV operator admits a recursive formulation with state `(a_t, b_t)`:

> `a_t = e^{-w} * a_{t-1} + e^{k_t} * v_t`
> `b_t = e^{-w} * b_{t-1} + e^{k_t}`
> `wkv_t = (a_{t-1} + e^{u + k_t} * v_t) / (b_{t-1} + e^{u + k_t})`

This gives O(d) memory per layer during inference, compared to O(Td) for Transformers caching all key-value pairs.

**Internal state size.** Each layer stores five vectors of dimension D: current time-mix input, current channel-mix input, WKV numerator, WKV denominator, and an auxiliary exponent for numerical stability. Total internal state size: 5DL (or 4DL algebraically without the numerical helper).

**Custom CUDA kernel.** A custom kernel executes the WKV scan as a single compute operation on GPU, avoiding the inefficiency of sequential operations in standard frameworks.

**Small init embedding.** Embedding matrix initialized with small values (U(±1e-4)) followed by LayerNorm accelerates convergence by enabling rapid departure from the initial noisy embedding state (Figure 9).

**Parameter initialization.** Token shift mixing parameters `mu` are initialized as functions of layer depth and channel index. Time decay `w` is initialized to `−5 + 8 * (i / (d − 1))^{0.7 + 1.3l / (L − 1)}`. Most weights initialized to zero; `W_o` and `W'_v` initialized from `N(0, sqrt(d/2))`.

### Experimental Setup

**Models:** Six RWKV models from 169M to 14B parameters (Table 2):

| Name | Layers | Model Dimension | Parameters |
|---|---|---|---|
| 169M | 12 | 768 | 1.693 × 10^8 |
| 430M | 24 | 1024 | 4.304 × 10^8 |
| 1.5B | 24 | 2048 | 1.515 × 10^9 |
| 3B | 32 | 2560 | 2.985 × 10^9 |
| 7B | 32 | 4096 | 7.393 × 10^9 |
| 14B | 40 | 5120 | 1.415 × 10^10 |

**Training:** All models trained for one epoch on the Pile (330B tokens), context length 1024, bfloat16 precision, Adam optimizer without weight decay, exponential learning rate decay, PaLM auxiliary loss.

**Baselines:** Pythia (Biderman et al., 2023), OPT (Zhang et al., 2022), BLOOM (Scao et al., 2022) — all trained on comparable token budgets. Comparison is FLOP-matched to ensure fairness.

**Evaluation:** Zero-shot on 12 NLP tasks: ARC (Easy/Challenge), BoolQ, COPA, HeadQA, HellaSwag, LAMBADA, OpenBookQA, PIQA, ReCoRD, SciQ, Winogrande. Additionally: LRA benchmark, Enwik8 perplexity, extended context finetuning on Pile.

**Reproducibility:** Code released at https://github.com/BlinkDL/RWKV-LM; pretrained models at https://huggingface.co/RWKV. Training hyperparameters fully specified (Table 3, Appendix G).

### Key Results

**NLP Benchmarks (Figure 1, Figure 5):** RWKV performs comparably to Pythia, OPT, and BLOOM at equivalent compute budgets across all 12 zero-shot benchmarks. The average accuracy across tasks follows the same compute scaling trend as Transformer baselines.

**Scaling Laws (Figure 4):** RWKV follows the same log-log linear scaling form established for Transformers (Kaplan et al., 2020). Linear fit to Pareto-optimal points achieves r^2 = 0.994; extrapolation over an additional order of magnitude achieves r^2 = 0.875.

**Long Range Arena (Table 4):**

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Path-X | Avg |
|---|---|---|---|---|---|---|---|
| S4 | **59.60** | **86.82** | **90.90** | **88.65** | **94.20** | **96.35** | **86.09** |
| RWKV | 55.88 | 86.04 | 88.34 | 70.53 | 58.42 | -- | 72.07 |
| Transformer | 36.37 | 64.27 | 57.46 | 42.44 | 71.40 | -- | 53.66 |

RWKV ranks second overall, performing near S4 on text and retrieval tasks but substantially underperforming on image and pathfinder tasks.

**Enwik8 (Table 5):** RWKV achieves 1.178 bpc (12 layers, d=512, T=1024), comparable to the standard Transformer at 1.137 bpc but with O(Td) time and O(d) space complexity versus O(T^2 d) time and O(T^2 + Td) space.

**Inference Efficiency (Figures 7, 13, 14):** RWKV exhibits linear time scaling with sequence length during text generation, while Transformers scale quadratically. Memory usage remains constant regardless of sequence length.

**Extended Context (Figure 6):** Progressive finetuning from 1024 → 2048 → 4096 → 8192 tokens consistently decreases test loss on the Pile for both 7B and 14B models.

---

## Limitations and Failure Modes

1. **Limited recall over long contexts.** The linear attention mechanism funnels all past information through a fixed-size state vector, mechanistically limiting the model's ability to recall minutiae over very long contexts compared to full self-attention (Section 9).
2. **Prompt sensitivity.** RWKV is substantially more sensitive to prompt ordering than Transformers because the RNN formulation cannot "look back" at earlier tokens. Re-ordering prompts for the RTE task improved F1 from 44.2% to 74.8%, indicating that prompt engineering is significantly more important for RWKV than for standard Transformers (Appendix L, Tables 6--7).
3. **Weak mathematical reasoning.** RWKV-4-Raven-14B achieved only 5.43% accuracy on MathQA even with chain-of-thought prompting, compared to 71.4% for ChatGPT (Table 7).
4. **Underperformance on spatial tasks.** On LRA Image and Pathfinder tasks, RWKV substantially underperforms S4 (70.53 vs. 88.65 on Image; 58.42 vs. 94.20 on Pathfinder), suggesting limitations in modeling 2D spatial structure (Table 4).

### Scope and Comparability

- **Training context length.** All RWKV models were pretrained with context length 1024 tokens, shorter than many contemporary Transformer baselines. Extended context was achieved through progressive finetuning, not pretraining.
- **Comparison fairness.** Comparisons are FLOP-matched with Pythia, OPT, and BLOOM, all trained on the Pile. The paper avoids comparing with Chinchilla-optimal or overtrained models.
- **No standard long-context NLP evaluation.** The paper evaluates perplexity improvement with longer context but does not report results on long-context NLP benchmarks such as SCROLLS or LongBench.

---

## Conclusions

### Contributions

1. **Novel RNN-Transformer hybrid architecture.** RWKV combines parallelizable training (like Transformers) with efficient O(d) memory inference (like RNNs) through a linear attention mechanism based on channel-wise time decay.
2. **Scaling to 14B parameters.** RWKV is the largest dense RNN ever trained at the time of publication, demonstrating that non-Transformer architectures can scale to billions of parameters with competitive performance.
3. **Transformer-like scaling laws.** RWKV follows the same log-log linear scaling relationship as Transformers, with r^2 = 0.994 on Pareto-optimal compute-loss points.
4. **Lowest inference complexity.** RWKV achieves O(Td) time and O(d) space during inference, the lowest among all compared architectures including linear Transformers, Reformer, Performer, and AFT variants (Table 1).

### Implications

1. **Viability of linear-complexity models.** The competitive NLP performance at scale suggests that quadratic attention may not be strictly necessary for language modeling, opening a path for more efficient large-scale deployment.
2. **Prompt engineering for RNN-based models.** The increased sensitivity to prompt ordering implies that RNN-based LLMs may require fundamentally different prompting strategies than Transformers (speculative — requires systematic study).
3. **Edge deployment potential.** Constant memory inference makes RWKV suitable for consumer and edge hardware, potentially democratizing LLM access.

---

## Key Claims

1. **C1: Competitive with Transformers at matched compute.** RWKV performs on par with Pythia, OPT, and BLOOM across twelve zero-shot NLP benchmarks when compared at equivalent FLOPs (Figure 1, Figure 5). Evidence is across six model sizes (169M--14B) with consistent trends. No exact numerical table of per-task per-model results is provided in the main text; comparisons are shown as FLOP-accuracy plots.

2. **C2: Lowest inference complexity.** RWKV achieves O(Td) time and O(d) space during inference, strictly lower than all compared methods (Table 1). This is a theoretical property of the architecture, confirmed by the linear time scaling in Figure 7.

3. **C3: Transformer-like scaling laws.** The loss-compute relationship for RWKV follows the same log-log linear form as Transformers, with r^2 = 0.994 on Pareto-optimal points across 45 trained models (Figure 4, Section 4.2). The fit holds with r^2 = 0.875 when extrapolated an order of magnitude.

4. **C4: Effective use of extended context.** Progressive finetuning from 1024 to 8192 tokens yields consistently lower test loss on the Pile for both 7B and 14B models (Figure 6). Evidence is limited to perplexity on a single dataset.

5. **C5: Linear inference time scaling.** RWKV generates text with linear time scaling in sequence length, while Transformers show quadratic growth (Figure 7). Tested on CPU and GPU (A100) at float32 precision.

6. **C6: Increased prompt sensitivity.** RWKV is substantially more sensitive to prompt ordering than Transformers. On RTE, re-ordering prompts increased F1 from 44.2% to 74.8% (Tables 6--7, Appendix L). On sarcasm detection, RWKV with adapted prompts outperformed ChatGPT (50.96 vs. 49.88 F1).

---

## Open Questions

1. **Can RWKV's recall limitations over long contexts be mitigated without sacrificing linear complexity?** The authors suggest enhancing time-decay formulations and exploring initial model states (Section 7). Not yet resolved.

2. **How would RWKV perform in encoder-decoder architectures for seq2seq or multimodal settings?** The authors propose replacing cross-attention with RWKV mechanisms (Section 7). Not yet tested.

3. **Can parallel scan reduce WKV computation to O(B log(T) d)?** The authors reference Martin and Cundy (2017) for parallelizing over sequence length (Section 3.2). Not implemented in this work.

4. **Can systematic prompt engineering guidelines for RNN architectures close the gap with Transformers on reasoning tasks?** The paper shows significant gains from prompt re-ordering but does not establish general guidelines (Appendix L).

---

## Core References and Why They Are Referenced

### Attention Mechanism Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture and quadratic self-attention mechanism that RWKV aims to replace.
- **Zhai et al. (2021)** -- *An Attention Free Transformer.* Proposes AFT with pairwise position biases; RWKV directly builds on this formulation by constraining biases to channel-wise time decay.
- **Katharopoulos et al. (2020)** -- *Transformers Are RNNs.* Establishes the connection between linear attention and RNNs that RWKV exploits for dual-mode computation.

### Efficient Architecture Alternatives

- **Gu et al. (2022)** -- *Efficiently Modeling Long Sequences with Structured State Spaces.* S4 achieves strong results on LRA and serves as the primary non-Transformer baseline on the long-range benchmark.
- **Dao et al. (2022)** -- *FlashAttention.* Hardware-aware exact attention that reduces memory but retains quadratic time complexity; contrasted with RWKV's linear approach.
- **Beltagy et al. (2020)** -- *Longformer.* Local+global sparse attention for long documents; RWKV achieves better complexity guarantees.

### Transformer Baselines

- **Biderman et al. (2023)** -- *Pythia.* Primary Transformer baseline for FLOP-matched comparison across model scales.
- **Zhang et al. (2022)** -- *OPT.* Open pre-trained Transformer language models used as baselines.
- **Scao et al. (2022)** -- *BLOOM.* Open multilingual Transformer used as baseline.
- **Brown et al. (2020)** -- *GPT-3.* Demonstrates Transformer scaling; motivates the need for more efficient architectures.

### Scaling Laws

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Establishes the log-log linear scaling framework that RWKV is shown to follow.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models.* Chinchilla scaling laws; RWKV comparisons deliberately avoid Chinchilla-optimal models for fairness.

### Training Data

- **Gao et al. (2020)** -- *The Pile.* The 800GB dataset used to train all RWKV models (one epoch, 330B tokens).
