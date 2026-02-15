---
title: "Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence"
authors: "Peng, Goldstein, Anthony, Albalak, Alcaide, Biderman, Cheah, Du, Ferdinan, Hou, Kazienko, Kiran GV, Kocon, Koptyra, Krishna, McClelland Jr., Lin, Muennighoff, Obeid, Saito, Song, Tu, Wirawan, Wozniak, Zhang, Zhao, Zhao, Zhou, Zhu, Zhu"
year: 2024
venue: "COLM 2024"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "model-release"]
scope: ["linear-time RNN language models", "matrix-valued recurrent states", "data-dependent recurrence", "multilingual language modeling"]
benchmarks_used: ["lambada", "hellaswag", "piqa", "arc", "winogrande", "perplexity-pg19", "mqar", "bamboo", "copa", "storycloze", "headqa", "openbookqa", "record", "glue"]
models_introduced: ["eagle-0.4b", "eagle-1.5b", "eagle-3b", "eagle-7b", "finch-1.6b", "finch-3b"]
models_evaluated: ["pythia-series", "mamba-1.4b", "mamba-2.8b", "mistral-7b", "falcon-7b", "llama-2-7b", "mpt-7b"]
key_claims:
  - id: C1
    claim: "Eagle and Finch achieve competitive English benchmark performance with similarly-sized Transformers"
    evidence: "Table 4, Figure 3"
    status: supported
    scope: "0.4B--7B parameters, English zero-shot benchmarks, RWKV World v2 training corpus"
    magnitude: "Eagle-7B avg 71.5% vs Mistral-7B-v0.1 avg 75.8% (4.3pp gap despite ~2x fewer tokens and multilingual corpus)"
  - id: C2
    claim: "Eagle and Finch substantially outperform other models on multilingual benchmarks at similar FLOPs"
    evidence: "Table 3, Figure 2"
    status: supported
    scope: "1.5B--7B parameters, 6 multilingual benchmarks"
    magnitude: "Eagle-7B avg 58.2% vs next-best RWKV-4-7B avg 56.4% and Falcon-7b avg 55.7%"
  - id: C3
    claim: "Finch achieves near-perfect MQAR accuracy, outperforming all non-Transformer architectures"
    evidence: "Figure 4, Section 8.2"
    status: supported
    scope: "sequence lengths 64--512, model dimensions 64--512, controlled MQAR task"
    magnitude: "~100% accuracy at all tested configurations where Mamba, Hyena, RWKV-4 degrade"
  - id: C4
    claim: "Finch training speed scales linearly with sequence length and is ~4.2x faster than FlashAttention-2 at 16K"
    evidence: "Figure 7, Section 9"
    status: supported
    scope: "A100 80GB, batch size 8, d_model 4096, head size 64, single hardware configuration"
    magnitude: "~4.2x faster than FlashAttention-2 at 16K; Finch 23.6 GB vs FA2 32.8 GB vs Mamba 27.7 GB at 16K"
  - id: C5
    claim: "Eagle and Finch extrapolate well beyond 4096 training context on PG-19 loss"
    evidence: "Figure 5, Section 8.3"
    status: supported
    scope: "3B parameter models, PG-19 test set, loss metric only"
    magnitude: "Loss continues decreasing beyond 10K positions vs RWKV-4 sharp degradation beyond 4096"
  - id: C6
    claim: "Eagle-7B-Hermes outperforms Pythia-6.9B on Bamboo long-context benchmark by 13.5pp average"
    evidence: "Table 5, Section 8.4"
    status: supported
    scope: "7B scale, 4K context Bamboo benchmark, Hermes fine-tuned model"
    magnitude: "Eagle-7B-Hermes 16.8% vs Pythia-6.9B 3.3% avg across 9 Bamboo tasks"
  - id: C7
    claim: "Finch (RWKV-6) architecture alone matches Mamba performance when controlling for training data"
    evidence: "Table 18, Appendix J"
    status: supported
    scope: "170M parameters, Pile dataset, GPT-NeoX-20B tokenizer"
    magnitude: "RWKV-6-Pile avg 50.7% vs Mamba avg 50.1% on 12 English benchmarks"
cross_references:
  - target: 2024-05-mamba-selective-state-spaces
    type: concurrent
    detail: "Both propose efficient alternatives to Transformers with data-dependent dynamics; Mamba uses selective SSMs while RWKV-5/6 uses matrix-valued linear attention with data-dependent decay"
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "Eagle and Finch propose RNN-based alternatives that match Transformer quality while achieving O(1) per-token inference and linear-time training"
  - target: 2022-12-flashattention
    type: complementary
    detail: "Finch's custom CUDA kernel is benchmarked against FlashAttention-2, achieving ~4.2x faster training at 16K sequence length"
  - target: 2022-03-in-context-learning-induction-heads
    type: extends
    detail: "Token shift mechanism enables induction head formation in RNNs within a single layer; MQAR benchmark used to evaluate this capability"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "Compares Eagle-7B against LLaMA-2-7B on English and multilingual benchmarks"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Compares Eagle-7B against Mistral-7B-v0.1; Mistral leads on English benchmarks (75.8% vs 71.5%) but Eagle-7B is competitive on multilingual"
  - target: 2022-04-s4-structured-state-spaces
    type: complementary
    detail: "S4 pioneered structured state spaces; RWKV takes a different path via linear attention reformulation but shares the goal of efficient sequence modeling"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: extends
    detail: "Direct successor to RWKV-4; Eagle adds matrix-valued states and SiLU gating, Finch adds data-dependent token shift and decay via LoRA modules"
open_questions:
  - question: "Can RWKV-5/6 scale effectively to 14B+ parameters and beyond?"
    addressed_by: null
  - question: "How do Eagle/Finch perform on instruction-following and RLHF tasks at scale?"
    addressed_by: null
  - question: "Can the RWKV architecture be combined with Mixture of Experts for further scaling?"
    addressed_by: null
  - question: "Does data-dependent decay in Finch provide advantages for very long contexts (>32K)?"
    addressed_by: null
  - question: "What is the precise individual contribution of matrix-valued states vs. data-dependent decay?"
    addressed_by: null
  - question: "How do Eagle/Finch perform on standardized long-context benchmarks (RULER, LongBench, NIAH)?"
    addressed_by: null
---

# Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence

**Authors:** Bo Peng, Daniel Goldstein, Quentin Anthony, Alon Albalak, Eric Alcaide, Stella Biderman, Eugene Cheah, Xingjian Du, Teddy Ferdinan, Haowen Hou, Przemyslaw Kazienko, Kranthi Kiran GV, Jan Kocon, Bartlomiej Koptyra, Satyapriya Krishna, Ronald McClelland Jr., Jiaju Lin, Niklas Muennighoff, Fares Obeid, Atsushi Saito, Guangyu Song, Haoqin Tu, Cahya Wirawan, Stanislaw Wozniak, Ruichong Zhang, Bingchen Zhao, Qihang Zhao, Peng Zhou, Jian Zhu, Rui-Jie Zhu (RWKV Project / Linux Foundation AI & Data, EleutherAI, Recursal AI, Ohio State University, University of California Santa Barbara, Wroclaw Tech, and 20+ other institutions)
**Date:** October 2024, COLM 2024 (arXiv:2404.05892)

---

## Core Research Problem

The Transformer architecture dominates language modeling but suffers from **quadratic time complexity** in sequence length due to multi-headed dot-product self-attention. This makes training and inference on long sequences prohibitively expensive. Prior work on efficient alternatives -- linear attention, state space models (Mamba, S4), and earlier RWKV versions -- has sought to maintain O(1) per-token inference cost with parallelizable training, but has generally lagged behind Transformers in quality.

RWKV-4 (Peng et al., 2023) was the first RNN to rival Transformer performance while maintaining O(1) inference and parallelizable O(N) training (Table 1, Section 1). However, it had key architectural limitations: (1) **vector-valued attention states** restricted each head's recurrent state to a vector in R^(D/h), limiting information storage capacity across time steps; (2) **static decay schedule** used a fixed, learned decay vector w that could not adapt to input content; and (3) **sigmoid receptance activation** added unnecessary nonlinearity and prevented the receptance from functioning as a pure query term.

The core challenge is: **how to increase the expressivity of linear-time RNN language models by enriching the recurrent state representation and making the dynamics data-dependent, without sacrificing the O(1) inference and O(N) training efficiency that distinguishes RNNs from Transformers.**

---

## Problem Solutions

The paper introduces two progressive architectural refinements to RWKV-4:

1. **Eagle (RWKV-5): Matrix-valued states.** Upgrade the per-head recurrent state from a vector in R^(D/h) to a matrix in R^(D/h x D/h), dramatically increasing per-head state capacity. Add LayerNorm over attention heads, SiLU-based attention gating, and improved initialization. Remove the sigmoid activation on the receptance vector.

2. **Finch (RWKV-6): Data-dependent recurrence.** Make both the token-shift interpolation and the decay schedule input-dependent via lightweight LoRA modules. The decay w_t now varies at each time step based on current and previous tokens, enabling dynamic memory management. Token shift interpolation factors also become data-dependent via LoRA (data-dependent linear interpolation, "ddlerp").

3. **Infrastructure contributions.** Introduce the RWKV World Tokenizer (65,536 tokens, Trie-based greedy matching, multilingual-aware vocabulary) and RWKV World v2 Dataset (1.12 trillion tokens, ~70% English / ~15% multilingual / ~15% code).

---

## Approach Details

### Method

#### RWKV-4 Background

The RWKV architecture reformulates the Attention Free Transformer (AFT) by replacing pairwise positional biases with a channelwise additive decay vector w and a bonus term u for the current token. The RWKV-4 WKV attention is (Equation 2, Section 2):

> wkv_i = (sum_{j=1}^{i-1} exp(-(i-1-j)w + k_j) . v_j + exp(u + k_i) . v_i) / (sum_{j=1}^{i-1} exp(-(i-1-j)w + k_j) + exp(u + k_i))

In recurrent form, RWKV-4 maintains a vector-valued state per head. The architecture consists of stacked residual blocks, each containing a Time Mixing sub-layer (analogous to attention) and a Channel Mixing sub-layer (analogous to FFN), both preceded by LayerNorm (Section 3, Figure 1).

#### Eagle (RWKV-5) Architecture

Eagle makes four changes to RWKV-4 (Section 4.1):

**1. Matrix-valued states.** The recurrent state s is upgraded from R^(D/h) to R^(D/h x D/h). The WKV computation becomes (Equations 6-9, Section 4.1.2):

> wkv_t = diag(u) . k_t^T . v_t + sum_{i=1}^{t-1} diag(w)^{t-1-i} . k_i^T . v_i

In recurrent form:

> wkv' = s + diag(u) . k^T . v
> s' = diag(w) . s + k^T . v

where k^T . v is an outer product producing a (D/h x D/h) matrix. Each head now stores a matrix that accumulates key-value associations across time steps. The internal state size increases from 5DL (RWKV-4) to 66DL (Eagle/Finch) -- more than an order of magnitude larger (Appendix E, Equation 30).

**2. Token Shift.** Linear interpolation (lerp) between current and previous token embeddings before projecting to r, k, v, g vectors (Equations 3-4, Section 4.1.1):

> lerp_sq(a, b) = a + (b - a) . mu_sq
> sq_i = lerp_sq(x_i, x_{i-1}) W_sq,  sq in {r, k, v, g}

where each mu_sq in R^D is a learnable vector. This enables induction head formation within a single layer (Section 4.1.1).

**3. SiLU gating and LayerNorm.** The output combines a SiLU-gated branch with LayerNorm applied per-head over the WKV result (Equation 7):

> o_i = concat(SiLU(g_i) . LayerNorm(r_i . wkv_i)) W_o

**4. Decay as contraction.** The decay w = exp(-exp(omega)) where omega in R^(D/h) is the learned parameter, ensuring w in (0, 1) and making diag(w) a guaranteed contraction matrix (Equation 5).

#### Finch (RWKV-6) Architecture

Finch extends Eagle with two data-dependent mechanisms (Section 4.2):

**1. Data-dependent Token Shift (ddlerp).** The interpolation factor becomes input-dependent via a LoRA module (Equations 14-15, Section 4.2.1):

> lora_sq(x) = lambda_sq + tanh(x A_sq) B_sq
> ddlerp_sq(a, b) = a + (b - a) . lora_sq(a + (b - a) . mu_x)

where A_sq in R^(D x 32) and B_sq in R^(32 x D) are trainable LoRA weights (doubled to D x 64, 64 x D for the decay LoRA). This allows each channel's mix of current and prior tokens to depend on input content.

**2. Data-dependent decay.** The decay w_t is now time-varying (Equations 17-18, Section 4.2.2):

> d_t = lora_d(ddlerp_d(x_t, x_{t-1}))
> w_t = exp(-exp(d_t))

The WKV recurrence becomes (Equations 19, 21-22):

> wkv' = s + diag(u) . k^T . v
> s' = diag(w_t) . s + k^T . v

Unlike Eagle where w is static across all time steps, Finch's w_t varies at each position based on the input. This is the core expressivity improvement: the model can dynamically decide how much of each state channel to retain or forget. The paper describes this as a "second-order variant of Token-Shifting" (Section 4.2.2).

#### Channel Mixing

Both Eagle and Finch retain RWKV-4's Channel Mixing module, with slightly reduced hidden dimension (3.5D instead of 4D in Eagle) to account for additional gating parameters while maintaining equi-parameter counts. Finch does not reduce the hidden dimension despite adding LoRA parameters (Section 4.1.3, Equations 10-13):

> r'_i = lerp_{r'}(x'_i, x'_{i-1}) W_{r'}
> k'_i = lerp_{k'}(x'_i, x'_{i-1}) W_{k'}
> v'_i = ReLU(k'_i)^2 W_{v'}
> o'_i = sigma(r'_i) . v'_i

### Key Technical Components

**Complexity.** Both Eagle and Finch maintain RWKV-4's complexity profile: O(1) time and memory per token at inference, O(N) training time and memory, with full parallelizability across the time dimension. The matrix-valued state adds a constant factor (D/h additional floats per head) but does not change asymptotic complexity (Table 1, Section 1).

**Model configurations (Table 11, Appendix E):**

| Model | Params | Layers | d_model | Heads | Training Tokens |
|-------|--------|--------|---------|-------|-----------------|
| Eagle 0.4B | 0.46B | 24 | 1024 | 16 | 1.12T |
| Eagle 1.5B | 1.58B | 24 | 2048 | 32 | 1.12T |
| Eagle 3B | 3.06B | 32 | 2560 | 40 | 1.12T |
| Eagle 7B | 7.52B | 32 | 4096 | 64 | 1.12T |
| Finch 1.6B | 1.60B | 24 | 2048 | 32 | 1.12T |
| Finch 3B | 3.10B | 32 | 2560 | 40 | 1.12T |

All models pretrained with context length 4096 on the RWKV World v2 multilingual corpus. Training used bfloat16 with float32 for WKV computation for numerical stability. Adam optimizer with beta_1=0.9, beta_2=0.99, weight decay 0.001. Learning rate followed linear 10-step warmup then cosine decay (Table 17, Appendix H).

**Training hardware:** Eagle 0.4B on 24 A100s, 1.5B and 3B on 48 A100s, 7B on 64 H800s (Table 17).

**RWKV World Tokenizer (Section 5).** Vocabulary of 65,536 tokens constructed by merging vocabularies from GPT-NeoX-20B, GPT-2, cl100k_base (tiktoken), LLaMA-2, and BLOOM tokenizers, with manual selection to ensure non-European language coverage. Implemented via Trie-based greedy matching rather than BPE. The Rust implementation achieves 90.32 MB/s tokenization speed, 9.6x faster than Tiktoken (Table 13, Appendix F).

**RWKV World v2 Dataset (Section 6).** 1.12 trillion tokens from publicly available sources: approximately 70% English, 15% multilingual, and 15% code. Emphasis on cultural works (stories, books, subtitles, conversations) alongside factual knowledge and code (Table 9, Appendix D).

### Experimental Setup

**LM Evaluation Harness benchmarks (English, Table 4):** LAMBADA (OpenAI), HellaSwag, PIQA, ARC (easy and challenge), GLUE, WinoGrande, SciQ, COPA. Evaluated zero-shot.

**Multilingual benchmarks (Table 3):** LAMBADA Multilingual, XCOPA, XNLI, PAWS-X, XStoryCloze, XWinoGrande.

**Associative recall (Section 8.2):** Multi-Query Associative Recall (MQAR) at sequence lengths 64--512 and model dimensions 64--512.

**Long context (Section 8.3--8.4):** PG-19 test set loss vs. sequence position (token 2048 onward). Bamboo benchmark (4K version, 9 tasks: question answering, hallucination detection, text sorting, language modeling).

**Multimodal (Sections 10--11):** VisualRWKV (CLIP-L + Eagle 1.5B/3B on GQA, ScienceQA-IMG, Text-VQA, POPE); RWKV Music Modeling (Irishman ABC dataset); AudioRWKV (AudioSet, 8.7M--28.4M parameter models).

**Baselines:** Pythia (1.4B, 2.8B, 6.9B), Mamba (1.4B, 2.8B), RWKV-4 (1.5B, 3B, 7B), Falcon-7B, LLaMA-2-7B, Mistral-7B-v0.1, MPT-7B.

**Efficiency (Section 9):** Speed and memory benchmarked on A100 80GB with batch size 8, d_model 4096, head size 64, comparing Finch kernel against FlashAttention-2 and Mamba.

**Controlled ablation (Appendix J):** 170M parameter RWKV-6 trained from scratch on the Pile dataset with GPT-NeoX-20B tokenizer (330B tokens) to isolate architectural contributions from data/tokenizer effects.

**Reproducibility:** All models released under Apache 2.0 with training code, inference code, time-parallel training code, and dataset. Hardware and hyperparameters documented in Appendices E and H. No variance estimates or multiple seeds reported.

### Key Results

#### English Benchmarks (Table 4, Section 8.1)

| Model | lmb.o | hella | piqa | arcE | arcC | glue | winG | sciq | copa | avg |
|-------|-------|-------|------|------|------|------|------|------|------|-----|
| Pythia-1.4B | 61.0 | 52.0 | 70.8 | 54.4 | 26.2 | 47.1 | 57.3 | 86.5 | 74.0 | 59.9 |
| RWKV-4-1.5B | 60.1 | 51.6 | 71.5 | 58.4 | 27.1 | 46.1 | 55.2 | 84.7 | 78.0 | 59.2 |
| Eagle-1.5B | 65.7 | 55.0 | 71.1 | 62.2 | 28.7 | 54.1 | 59.1 | 89.7 | 76.0 | 62.4 |
| Finch-1.6B | 66.8 | 57.3 | 72.6 | 62.7 | 29.8 | 49.8 | 59.4 | 89.6 | 78.0 | 62.9 |
| Mamba-1.4B | 64.5 | 59.0 | 74.2 | 65.0 | 30.1 | 47.0 | 61.3 | 87.1 | 80.0 | 63.1 |
| Pythia-2.8B | 63.8 | 59.1 | 73.9 | 63.8 | 29.0 | 47.3 | 58.2 | 88.6 | 79.0 | 62.5 |
| Eagle-3B | 68.7 | 62.6 | 74.3 | 68.6 | 33.8 | 46.3 | 62.0 | 92.6 | 85.0 | 66.0 |
| Mamba-2.8B | 68.1 | 65.9 | 75.2 | 69.7 | 33.8 | 46.3 | 63.0 | 90.2 | 84.0 | 66.2 |
| Finch-3B | 70.8 | 64.8 | 74.2 | 66.5 | 34.6 | 58.2 | 63.6 | 92.5 | 82.0 | 67.5 |
| Pythia-6.9B | 60.9 | 63.2 | 74.8 | 66.5 | 32.0 | 47.7 | 61.5 | 88.9 | 79.0 | 63.8 |
| RWKV-4-7B | 69.8 | 65.3 | 75.0 | 67.4 | 34.0 | 56.4 | 62.4 | 90.8 | 85.0 | 67.3 |
| Eagle-7B | 74.2 | 70.9 | 77.0 | 73.8 | 39.5 | 57.5 | 67.4 | 95.5 | 88.0 | 71.5 |
| MPT-7B | 66.6 | 76.4 | 79.1 | 76.5 | 42.4 | 59.3 | 68.1 | 93.0 | 86.0 | 71.9 |
| LLaMA-2-7B | 73.5 | 76.0 | 78.1 | 76.4 | 43.1 | 42.9 | 69.1 | 93.9 | 87.0 | 71.1 |
| Falcon-7B | 74.6 | 76.4 | 79.5 | 74.8 | 40.3 | 45.8 | 67.1 | 94.4 | 88.0 | 71.2 |
| Mistral-7B-v0.1 | 75.5 | 81.0 | 80.5 | 80.8 | 60.1 | 51.5 | 73.6 | 95.9 | 93.0 | 75.8 |

- At the 1.5B scale, Finch-1.6B (62.9%) and Mamba-1.4B (63.1%) are closely competitive; Finch leads on LAMBADA and SciQ, Mamba leads on HellaSwag, PIQA, and ARC.
- At the 3B scale, Finch-3B (67.5%) leads Eagle-3B (66.0%) and Mamba-2.8B (66.2%).
- **Eagle-7B (71.5%) is competitive with MPT-7B (71.9%), LLaMA-2-7B (71.1%), and Falcon-7B (71.2%)**, but trails Mistral-7B-v0.1 (75.8%) substantially. Mistral's advantage is largest on HellaSwag (+10.1pp) and ARC-C (+20.6pp). Note: different training data limits strict architectural comparison.

#### Multilingual Benchmarks (Table 3, Section 8.1)

| Model | lmb.m ppl | lmb.m acc | pawsx | xcopa | xnli | xsClz | xwin | avg |
|-------|-----------|-----------|-------|-------|------|-------|------|-----|
| Pythia-6.9B | 85.6 | 36.7 | 48.4 | 54.1 | 40.0 | 54.2 | 70.9 | 50.7 |
| MPT-7B | 49.8 | 44.4 | 43.5 | 53.6 | 39.8 | 56.3 | 76.9 | 52.4 |
| LLaMA-2-7B | 30.4 | 50.8 | 41.2 | 56.7 | 39.9 | 57.5 | 79.5 | 54.3 |
| Mistral-7B-v0.1 | 27.1 | 51.9 | 41.5 | 55.9 | 43.1 | 59.2 | 81.2 | 54.5 |
| Falcon-7B | 28.7 | 51.3 | 48.2 | 58.0 | 39.0 | 59.0 | 77.7 | 55.7 |
| RWKV-4-7B | 33.1 | 47.4 | 52.1 | 60.1 | 41.2 | 60.9 | 76.5 | 56.4 |
| **Eagle-7B** | **21.0** | **53.7** | 45.6 | **62.2** | **44.0** | **63.3** | **80.4** | **58.2** |

- **Eagle-7B achieves the best multilingual average (58.2%) across all 7B-class models**, improving +1.8pp over RWKV-4-7B and +2.5pp over Falcon-7B.
- On multilingual FLOPs-vs-accuracy (Figure 2), Eagle and Finch represent a substantial improvement to the Pareto frontier. Note: multilingual advantage is partly attributable to the multilingual-focused training corpus, not purely architecture.

#### Multi-Query Associative Recall (Figure 4, Section 8.2)

Finch (RWKV-6) achieves **near-perfect MQAR accuracy across all tested sequence lengths (64--512) and model dimensions (64--512)**, outperforming RWKV-4 (Dove), Eagle (RWKV-5), Mamba, Hyena, and Based. Eagle improves substantially over RWKV-4 at larger model dimensions but still falls short of Finch and attention-based models at longer sequences. Despite sharing data-dependent memory modification with Mamba, Finch outperforms it on MQAR, suggesting the specific combination of matrix-valued states and data-dependent decay is more effective for associative recall (tested across 4 sequence lengths and 4 model dimensions; moderate evidence).

#### Long Context (Figure 5, Table 5, Sections 8.3--8.4)

On PG-19 loss vs. position (3B models, trained at 4096 context), Eagle and Finch maintain decreasing loss well beyond the training context length, while RWKV-4 degrades sharply beyond ~10^4 tokens. Finch achieves the lowest loss throughout (Figure 5; qualitative finding, no formal extrapolation benchmark used).

On Bamboo (4K version, Table 5):

| Model | meetingqa | paperqa | meetingpred | showspred | reportsumsort | showssort | senhallu | abshallu | altqa | avg |
|-------|-----------|---------|-------------|-----------|---------------|-----------|----------|----------|-------|-----|
| Pythia-1.4B | 15.0% | 4.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.1% |
| Mamba-1.4B | 15.0% | 2.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 2.0% | 0.0% | 2.1% |
| Eagle-1.5B | 21.0% | 19.0% | 1.0% | 0.0% | 0.0% | 0.0% | 13.2% | 23.5% | 5.5% | 9.2% |
| Finch-1.6B | 19.0% | 22.0% | 1.0% | 8.0% | 0.0% | 0.0% | 10.7% | 17.3% | 2.5% | 8.9% |
| Mamba-2.8B-Hermes | 27.0% | 25.0% | 0.0% | 9.0% | 0.0% | 0.0% | 19.7% | 26.4% | 0.0% | 11.9% |
| Finch-3B | 20.0% | 26.0% | 4.0% | 7.0% | 0.0% | 0.0% | 14.4% | 23.6% | 6.5% | 11.3% |
| Pythia-6.9B | 19.0% | 7.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 3.3% |
| Eagle-7B-Hermes | 31.0% | 23.0% | 0.0% | 0.0% | 0.0% | 0.0% | 50.3% | 46.9% | 0.0% | 16.8% |
| LLaMA2-Chat-7B | 6.0% | 17.0% | 4.0% | 12.0% | 0.0% | 0.0% | 64.7% | 63.4% | 46.0% | 24.1% |
| Mistral-Instruct-7B | 65.0% | 73.0% | 17.0% | 32.0% | 0.0% | 0.0% | 80.5% | 72.8% | 13.5% | 39.3% |

- Eagle-7B-Hermes outperforms Pythia-6.9B by 13.5pp average (16.8% vs 3.3%). Note: Eagle-7B base model is not reported separately; the Hermes fine-tune is used for this comparison.
- Instruction-tuned Transformer models (Mistral-Instruct 39.3%, LLaMA2-Chat 24.1%) substantially outperform all base and Hermes-tuned RWKV models.
- All models score 0% on reportsumsort and showssort tasks.

#### Speed and Memory (Figures 6, 7, Section 9)

| Sequence Length | Finch (GB) | Mamba (GB) | FlashAttention-2 (GB) |
|----------------|------------|------------|----------------------|
| 512 | 0.5 | 0.8 | 1.0 |
| 1024 | 1.5 | 1.7 | 2.1 |
| 2048 | 2.9 | 3.5 | 4.1 |
| 4096 | 5.9 | 6.9 | 8.2 |
| 8192 | 11.8 | 13.9 | 16.4 |
| 16384 | 23.6 | 27.7 | 32.8 |

- **Training time** scales linearly with sequence length for Finch (matching Mamba), while FlashAttention-2 scales quadratically. Finch is **~4.2x faster at 16K** sequence length and ~180ms vs FA2's ~800ms (Figure 7).
- **Memory** at 16K: Finch uses 23.6 GB vs FlashAttention-2's 32.8 GB and Mamba's 27.7 GB (Figure 6). The paper states "40% and 17% less memory usage than Flash Attention and Mamba respectively" (Section 9).
- At sequence lengths <=2K, FlashAttention-2 is faster due to optimized constant factors (single hardware configuration tested; limited evidence for generalization to other GPUs).

### Ablation Studies

#### Architectural Ablation (Table 18, Appendix J)

To isolate architecture from data/tokenizer effects, a 170M parameter RWKV-6 was trained on the Pile with GPT-NeoX-20B tokenizer (330B tokens), matching Pythia and Mamba training conditions exactly:

| Model | lmb.o ppl | lmb.o acc | hella | piqa | avg (12 benchmarks) |
|-------|-----------|-----------|-------|------|---------------------|
| RWKV-4-Pile | 29.2 | 33.1 | 32.2 | 64.9 | 47.7 |
| Pythia | 24.4 | 38.8 | 31.7 | 62.6 | 47.9 |
| Mamba | 16.0 | 44.2 | 35.3 | 64.4 | 50.1 |
| RWKV-6-Pile | 16.1 | 44.5 | 34.9 | 64.4 | 50.7 |

RWKV-6 slightly outperforms Mamba (50.7% vs 50.1%) on the 12-benchmark average when training data and tokenizer are controlled, confirming that the architectural improvements provide genuine gains beyond data effects.

#### DDLerp Ablation (Table 19, Appendix K)

A small 6-layer, d_model=768 Finch model trained on 1.6B token minipile dataset at context length 512:

| Configuration | Final Validation Loss |
|---------------|----------------------|
| Finch (full DDLerp) | 2.91 |
| Finch with DDLerp only on decay | 2.923 |
| Finch with no DDLerp at all | 2.926 |

DDLerp on all components (r, k, v, g, decay) provides the best loss, with most benefit coming from applying DDLerp beyond just decay. However, the absolute differences are small (0.016 loss units; small-scale experiment with limited evidence for whether this gap persists at larger scales).

### Multimodal Extensions

#### Music Modeling (Section 10.1, Figure 8)

An RWKV-5-Music model (24 layers, D=512, byte-level tokenizer with V=128) trained on the Irishman ABC music sheet dataset achieves approximately **2% lower loss** than the RWKV-4-Music model with identical hyperparameters, primarily in the musical score portion of ABC files.

#### VisualRWKV (Section 10.2, Table 6)

VisualRWKV pairs a CLIP-L (0.4B) vision encoder with Eagle language models using a two-stage instruction-tuning process (feature alignment then end-to-end fine-tuning):

| Method | Vision Encoder | LLM | GQA | ScienceQA-IMG | Text-VQA | POPE |
|--------|---------------|-----|-----|---------------|----------|------|
| InstructBLIP | EVA01-CLIP-G | Vicuna-7B | 49.2 | 60.5 | 50.1 | -- |
| InstructBLIP | EVA01-CLIP-G | Vicuna-13B | 49.5 | 63.1 | 50.7 | 78.9 |
| VisualRWKV | CLIP-L | Eagle-1.5B | 48.5 | 46.2 | 37.8 | 81.8 |
| VisualRWKV | CLIP-L | Eagle-3B | 49.7 | 58.3 | 46.4 | 81.4 |

VisualRWKV with Eagle-3B achieves GQA (49.7) comparable to InstructBLIP with Vicuna-13B (49.5) using a much smaller vision encoder and language model, demonstrating the architecture's viability for vision-language tasks.

#### AudioRWKV (Section 11, Table 7)

AudioRWKV introduces quad-directional shift (Q-Shift) for processing 2D audio spectrograms:

| Model | Parameters | mAP |
|-------|-----------|-----|
| PANNs | 81M | 0.434 |
| HTS-AT | 28.8M | 0.437 |
| AudioRWKV-T | 8.7M | 0.435 |
| AudioRWKV-S | 28.4M | 0.452 |

AudioRWKV-Tiny (8.7M) achieves comparable mAP (0.435) to HTS-AT (0.437) with 3.3x fewer parameters. AudioRWKV-S (28.4M) sets a new best at 0.452.

---

## Limitations and Failure Modes

### Acknowledged Limitations

1. **Scale ceiling.** Largest models are 7.52B (Eagle) and 3.10B (Finch). Scaling behavior at 14B+ is unknown. The authors explicitly note plans for larger Finch models as future work (Section 12, Future Work).

2. **Embedding model weakness.** Eagle was tested as an embedding model on MTEB but could not achieve strong performance. The authors hypothesize the state is a high-quality context embedding but no appropriate aggregation method has been found (Limitations, p. 17).

3. **Training data contamination.** The corpus contains some synthetic data from GPT-3.5 and ChatGPT, causing released models to occasionally mimic ChatGPT's style and claim to be trained by OpenAI (Limitations, p. 17).

4. **Training data scale.** The 1.12T token corpus is smaller than contemporary corpora (LLaMA-2 uses 2T tokens), potentially limiting performance at the 7B scale (Future Work, p. 17).

### Observed Failure Modes

1. **English benchmarks at small scale.** At 1.5B, Finch-1.6B (62.9%) slightly underperforms Mamba-1.4B (63.1%) on the English average, with particularly large gaps on HellaSwag (-1.7pp), PIQA (-1.6pp), and ARC-E (-2.3pp) (Table 4), suggesting the multilingual training distribution trades some English-specific performance.

2. **Bamboo vs. instruction-tuned models.** On the Bamboo benchmark, even Eagle-7B-Hermes (16.8%) substantially lags behind Mistral-Instruct-7B (39.3%) and LLaMA2-Chat-7B (24.1%), indicating the importance of instruction tuning for long-context reasoning tasks (Table 5).

3. **Universal zero scores on sorting tasks.** All tested models score 0% on reportsumsort and showssort Bamboo tasks, and code completion was dropped because all models failed (Table 5, Section 8.4).

4. **[Inferred]** Prompt template sensitivity. The paper notes the model remains "very sensitive to the selected prompt template" (Appendix G.4), which may limit practical zero-shot applicability.

### Scope and Comparability

**What was not tested:**
- Models larger than 7.52B parameters
- Instruction-tuned or RLHF'd Finch versions (only Eagle-7B-Hermes shown)
- Direct comparison with Mamba at 7B scale (Mamba models only go to 2.8B in the comparison)
- Standardized long-context benchmarks like RULER, LongBench, InfiniteBench, or NIAH
- Head-to-head comparison controlling for training data at the 7B scale (only 170M ablation controls for data)
- Multiple seeds or variance estimates for any benchmark

**Comparability notes:**
- Different training data from most baselines (RWKV World v2 vs The Pile for Pythia/Mamba, unknown data for Mistral/Falcon), making direct architectural comparisons imprecise at 7B scale
- Multilingual advantage partly reflects the multilingual-focused training corpus, not purely architectural improvement
- The 170M-scale ablation on the Pile (Table 18) provides the cleanest architectural comparison, showing RWKV-6 matching Mamba when data is controlled
- FLOPs comparison in Figures 2--3 is the most fair cross-scale comparison, as it accounts for varying training budgets

---

## Conclusions

### Contributions

1. **Matrix-valued recurrent states.** Upgraded RWKV's per-head state from vectors in R^(D/h) to matrices in R^(D/h x D/h), increasing state capacity from 5DL to 66DL (more than 10x), enabling richer key-value association storage without changing asymptotic complexity (Section 4.1.2, Appendix E).

2. **Data-dependent recurrence.** Introduced LoRA-based data-dependent token shift (ddlerp) and data-dependent decay in Finch, enabling the model to dynamically control information flow based on input content rather than fixed learned schedules (Section 4.2).

3. **MQAR breakthrough for RNNs.** Demonstrated that Finch achieves near-perfect multi-query associative recall, the first non-Transformer architecture to do so, closing a key expressivity gap (Figure 4, Section 8.2).

4. **Multilingual efficiency frontier.** Showed that Eagle and Finch substantially advance the Pareto frontier of multilingual accuracy vs. training FLOPs among open models (Table 3, Figure 2).

5. **Controlled architectural validation.** The 170M-parameter Pile ablation (Table 18) provides evidence that RWKV-6's architecture alone matches Mamba when training data and tokenizer are controlled.

6. **Fully open release.** Released six models (0.46B--7.52B), training code, inference code, tokenizer, and dataset under Apache 2.0, providing the most complete open reproduction package for alternative-architecture LLMs (Table 2).

7. **Efficiency demonstration.** Showed Finch's training kernel is ~4.2x faster than FlashAttention-2 at 16K with lower memory usage, while maintaining O(1) inference (Figures 6--7, Section 9).

8. **Multimodal extensibility.** Demonstrated RWKV architecture viability for vision-language (VisualRWKV), music modeling, and audio classification tasks with competitive results (Sections 10--11).

### Implications

1. **RNN competitiveness is real.** At 7B scale, RWKV-based models match Transformers (MPT, LLaMA-2, Falcon) on English benchmarks and exceed them on multilingual tasks at equivalent FLOPs. The architecture choice is now a genuine engineering tradeoff. However, Mistral-7B still leads by 4.3pp on English, suggesting Transformers retain an advantage with sufficient training (speculative -- the gap may be partly attributable to data differences).

2. **Matrix states as a general principle.** The upgrade from vector to matrix recurrent states is a simple, general technique that could benefit any linear attention or RNN architecture. The 10x+ state size increase enables fundamentally richer information storage.

3. **Data-dependent dynamics are key.** The progression from RWKV-4 (static decay) to Eagle (static decay, matrix states) to Finch (data-dependent decay, matrix states) shows that data-dependent dynamics provide the largest expressivity gains, particularly for associative recall (Figure 4).

4. **Deployment viability.** O(1) per-token inference with no KV cache makes these models attractive for edge deployment and streaming applications where memory and latency constraints are binding.

---

## Key Claims

1. **C1:** Eagle and Finch achieve competitive English benchmark performance with similarly-sized Transformers (Table 4, Figure 3). Supported by zero-shot evaluation on 9 English benchmarks. Eagle-7B averages 71.5%, close to MPT-7B (71.9%), LLaMA-2-7B (71.1%), and Falcon-7B (71.2%), but 4.3pp below Mistral-7B-v0.1 (75.8%). Scope: 0.4B--7B parameters, English zero-shot. Evidence breadth: comprehensive benchmark suite across 4 scales, but different training data limits strict architectural comparison.

2. **C2:** Eagle and Finch substantially outperform other models on multilingual benchmarks at similar FLOPs (Table 3, Figure 2). Supported by evaluation on 6 multilingual benchmarks. Eagle-7B achieves 58.2% average vs next-best RWKV-4-7B at 56.4% (+1.8pp) and Falcon-7B at 55.7% (+2.5pp). Scope: 1.5B--7B parameters, 6 multilingual benchmarks. Note: multilingual advantage is partly attributable to the multilingual-focused training corpus, not purely architecture.

3. **C3:** Finch achieves near-perfect MQAR accuracy, outperforming all non-Transformer architectures (Figure 4, Section 8.2). Supported by controlled MQAR experiments at 4 sequence lengths and 4 model dimensions. Finch achieves ~100% accuracy where Mamba, Hyena, and RWKV-4 degrade. Scope: sequence lengths 64--512, model dimensions 64--512. This is the strongest evidence for the architectural contribution (moderate evidence from controlled synthetic task).

4. **C4:** Finch training speed scales linearly with sequence length and is ~4.2x faster than FlashAttention-2 at 16K (Figure 7, Section 9). Supported by kernel benchmarks on A100 80GB. Finch uses 23.6 GB vs FA2's 32.8 GB at 16K. Scope: A100 80GB, batch size 8, d_model 4096, head size 64. Single hardware configuration tested (limited evidence for generalization to other GPUs).

5. **C5:** Eagle and Finch extrapolate well beyond 4096 training context on PG-19 (Figure 5, Section 8.3). Supported by loss curves on PG-19 test set showing maintained or decreasing loss beyond training context. Scope: 3B models, PG-19 test set, loss metric only. Qualitative finding; no formal extrapolation benchmark was used (limited evidence).

6. **C6:** Eagle-7B-Hermes outperforms Pythia-6.9B on Bamboo long-context benchmark by 13.5pp average (Table 5, Section 8.4). Supported by 9-task evaluation at 4K context. Eagle-7B-Hermes achieves 16.8% vs Pythia-6.9B's 3.3%. Scope: 7B scale, 4K context, Hermes-fine-tuned model. However, instruction-tuned Transformers far outperform both (Mistral-Instruct 39.3%), and the comparison conflates architecture with training data and fine-tuning differences.

7. **C7:** Finch (RWKV-6) architecture alone matches Mamba when controlling for training data (Table 18, Appendix J). Supported by 170M-parameter controlled ablation on the Pile. RWKV-6-Pile avg 50.7% vs Mamba avg 50.1% across 12 benchmarks. Scope: 170M parameters, Pile dataset, GPT-NeoX-20B tokenizer. Limited evidence: single scale, no variance reported, but strongest evidence for purely architectural contribution.

---

## Open Questions

1. **Does Finch scale to 14B+ parameters?** The authors explicitly mention plans for 7B and 14B Finch models (Future Work, p. 17). Whether the advantages of data-dependent decay persist at larger scales is unknown.

2. **How do Eagle/Finch perform with instruction tuning and RLHF?** Only base models and a Hermes fine-tune are evaluated. The effectiveness of the RWKV architecture for alignment at scale is untested.

3. **Can RWKV architectures be combined with MoE?** The authors mention MoE as future work (Future Work, p. 17). Given MoE's success with Transformers (Mixtral, Switch Transformer), the interaction with RWKV's linear attention is an open question.

4. **Does data-dependent decay in Finch provide advantages for very long contexts (>32K)?** The paper only tests up to ~16K on PG-19 loss curves and uses 4K Bamboo. Whether Finch's dynamic decay enables genuine long-context reasoning at 32K+ is untested.

5. **What is the precise individual contribution of matrix-valued states vs. data-dependent decay?** The ablation between Eagle (matrix states, static decay) and Finch (matrix states, data-dependent decay) shows decay matters, but there is no ablation of RWKV-4 + data-dependent decay without matrix states. The DDLerp ablation (Table 19) shows only 0.016 loss improvement from full DDLerp vs no DDLerp at small scale.

6. **How do Eagle/Finch perform on standardized long-context benchmarks?** The paper uses PG-19 loss and Bamboo but does not evaluate on RULER, LongBench, InfiniteBench, or NIAH, making comparison with other long-context methods difficult.

---

## Core References and Why They Are Referenced

### RWKV Architecture Lineage

- **Peng et al. (2023)** -- *RWKV: Reinventing RNNs for the Transformer Era.* Direct predecessor (RWKV-4) that Eagle and Finch build upon; introduced the WKV attention mechanism combining exponential decay with linear attention.

- **Zhai et al. (2021)** -- *An Attention Free Transformer.* Introduced the Attention Free Transformer (AFT) with learned pairwise positional biases, which RWKV-4 reformulated into its channelwise decay-based attention (Equation 1, Section 2).

### Efficient Sequence Models

- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* Concurrent work introducing data-dependent SSMs; compared against on MQAR and efficiency benchmarks. Shares the goal of linear-time modeling with data-dependent dynamics but takes a different architectural path (selective SSM vs. linear attention with matrix states).

- **Gu et al. (2022)** -- *Efficiently Modeling Long Sequences with Structured State Spaces (S4).* Foundational SSM work; RWKV takes a different path (linear attention) but addresses the same problem of efficient long-sequence modeling.

- **Katharopoulos et al. (2020)** -- *Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention.* Established the connection between linear attention and RNNs that RWKV builds upon.

- **Sun et al. (2023)** -- *Retentive Network: A Successor to Transformer as Large Language Models.* RetNet introduces fixed per-head decay rates and xPos to linear attention; Eagle's per-channel learned decay is a refinement of this approach (Appendix C).

### Data-Dependent Recurrence (Concurrent Work)

- **Yang et al. (2023)** -- *Gated Linear Attention Transformers with Hardware-Efficient Training.* Concurrent work on data-dependent gated linear attention; data-dependent states similar to Finch's approach (Appendix C).

- **De et al. (2024)** -- *Griffin: Mixing Gated Linear Recurrences with Local Attention.* Concurrent work combining gated linear recurrence with local attention (Section 2, Appendix C).

- **Qin et al. (2023)** -- *HGRN: Hierarchically Gated Recurrent Neural Network.* Data-dependent RNN with input and forget gates (Section 2).

### Training Infrastructure and Baselines

- **Biderman et al. (2023)** -- *Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.* Provides controlled baselines (Pythia models) for comparison across scales.

- **Touvron et al. (2023)** -- *LLaMA 2: Open Foundation and Fine-Tuned Chat Models.* Key baseline at 7B scale; LLaMA-2 tokenizer also used in RWKV World Tokenizer construction.

- **Hu et al. (2022)** -- *LoRA: Low-Rank Adaptation of Large Language Models.* Finch uses LoRA-style low-rank modules for data-dependent token shift and decay, repurposing an adaptation technique as an architectural component.

### Evaluation

- **Arora et al. (2023)** -- *Zoology: Measuring and Improving Recall in Efficient Language Models.* Introduced the MQAR benchmark used to evaluate associative recall capability.

- **Dao (2023)** -- *FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning.* Key efficiency baseline; Finch's kernel is benchmarked against FlashAttention-2.

- **Dong et al. (2023)** -- *Bamboo: A Comprehensive Benchmark for Evaluating Long Text Modeling Capacities.* Long-context benchmark used to evaluate models at 4K context.

- **Elhage et al. (2021)** -- *A Mathematical Framework for Transformer Circuits.* Induction heads concept that motivates token shift design; AR capability linked to in-context learning effectiveness (Section 4.1.1, Section 8.2).
