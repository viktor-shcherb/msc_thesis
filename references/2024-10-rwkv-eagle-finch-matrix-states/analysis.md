---
title: "Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence"
authors: "Peng, Goldstein, Anthony, Albalak, Alcaide, Biderman, Cheah, Du, Ferdinan, Hou, Kazienko, Kiran GV, Kocoń, Koptyra, Krishna, McClelland Jr., Lin, Muennighoff, Obeid, Saito, Song, Tu, Wirawan, Woźniak, Zhang, Zhao, Zhao, Zhou, Zhu, Zhu"
year: 2024
venue: "COLM 2024"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "model-release"]
scope: ["linear-time RNN language models", "matrix-valued recurrent states", "data-dependent recurrence", "multilingual language modeling"]
benchmarks_used: ["lambada", "hellaswag", "piqa", "arc", "winogrande", "perplexity-pg19", "mqar", "bamboo", "copa"]
models_introduced: ["eagle-0.4b", "eagle-1.5b", "eagle-3b", "eagle-7b", "finch-1.6b", "finch-3b"]
models_evaluated: ["pythia-series", "mamba-1.4b", "mamba-2.8b", "mistral-7b", "falcon-7b", "llama-2-7b"]
key_claims:
  - id: C1
    claim: "Eagle and Finch achieve competitive English benchmark performance with similarly-sized Transformers"
    evidence: "Table 4, Section 8.1, Figure 3"
    status: supported
    scope: "0.4B--7B parameters, English zero-shot benchmarks"
    magnitude: "Eagle-7B avg 71.5% vs Pythia-6.9B avg 63.8% on English benchmarks"
  - id: C2
    claim: "Eagle and Finch substantially outperform other models on multilingual benchmarks at similar FLOPs"
    evidence: "Table 3, Figure 2"
    status: supported
    scope: "1.5B--7B parameters, multilingual benchmarks"
    magnitude: "Eagle-7B avg 58.2% vs Llama-2-7B avg 54.3% on multilingual, at ~2x fewer FLOPs"
  - id: C3
    claim: "Finch achieves near-perfect MQAR accuracy, outperforming all non-Transformer architectures"
    evidence: "Figure 4, Section 8.2"
    status: supported
    scope: "sequence lengths 64--512, model dimensions 64--512"
    magnitude: "~100% accuracy at all tested configurations"
  - id: C4
    claim: "Finch training speed scales linearly with sequence length and is 4.2x faster than FlashAttention at 16K"
    evidence: "Figure 7, Section 9"
    status: supported
    scope: "A100 80GB, batch size 8, d_model 4096, head size 64"
    magnitude: "4.2x faster than FlashAttention-2 at 16K; 40% less memory"
  - id: C5
    claim: "Eagle and Finch extrapolate well beyond 4096 training context on PG-19 loss"
    evidence: "Figure 5, Section 8.3"
    status: supported
    scope: "3B parameter models, PG-19 test set"
    magnitude: "Loss continues decreasing to ~16K positions vs RWKV-4 degradation"
  - id: C6
    claim: "Eagle-7B outperforms Pythia-6.9B on Bamboo long-context benchmark by 13.5% average"
    evidence: "Table 5, Section 8.4"
    status: supported
    scope: "7B scale, 4K context Bamboo benchmark"
    magnitude: "16.8% vs 3.3% average across 9 Bamboo tasks"
cross_references:
  - target: 2024-05-mamba-selective-state-spaces
    type: concurrent
    detail: "Both propose efficient alternatives to Transformers with data-dependent dynamics; Mamba uses selective SSMs while RWKV-5/6 uses matrix-valued linear attention with data-dependent decay"
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "Eagle and Finch propose RNN-based alternatives that match Transformer quality while achieving O(1) per-token inference and linear-time training"
  - target: 2022-12-flashattention
    type: complementary
    detail: "Finch's custom CUDA kernel is benchmarked against FlashAttention-2, achieving 4.2x faster training at 16K sequence length with 40% less memory"
  - target: 2022-03-in-context-learning-induction-heads
    type: extends
    detail: "Uses multi-query associative recall as key benchmark for evaluating architecture expressivity; token shift mechanism enables induction head formation in RNNs"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "Compares Eagle-7B against LLaMA-2-7B on English and multilingual benchmarks"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Compares Eagle-7B against Mistral-7B-v0.1; Mistral leads on English benchmarks but Eagle-7B is competitive on multilingual"
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
  - question: "Can the matrix-valued state mechanism be combined with Mixture of Experts for further scaling?"
    addressed_by: null
  - question: "Does data-dependent decay in Finch provide advantages for very long contexts (>32K)?"
    addressed_by: null
---

# Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence

**Authors:** Bo Peng, Daniel Goldstein, Quentin Anthony, Alon Albalak, Eric Alcaide, Stella Biderman, et al. (RWKV Project / Linux Foundation AI & Data, EleutherAI, and 23 other institutions)
**Date:** October 2024, COLM 2024 (arXiv:2404.05892)

---

## Core Research Problem

The Transformer architecture dominates language modeling but suffers from quadratic time complexity in sequence length due to multi-headed dot-product self-attention. This makes training and inference on long sequences prohibitively expensive. Prior work on efficient alternatives---linear attention, state space models (Mamba, S4), and earlier RWKV versions---has sought to maintain O(1) per-token inference cost with parallelizable training, but has generally lagged behind Transformers in quality.

RWKV-4 (Peng et al., 2023) was the first RNN to rival Transformer performance while maintaining O(1) inference and parallelizable O(N) training. However, it had key architectural limitations: (1) **vector-valued attention states** restricted each head's recurrent state to a vector in R^(D/h), limiting the information that could be stored across time steps; (2) **static decay schedule** used a fixed, learned decay vector w that could not adapt to input content; and (3) **sigmoid receptance activation** added unnecessary nonlinearity.

The core challenge is: **how to increase the expressivity of linear-time RNN language models by enriching the recurrent state representation and making the dynamics data-dependent, without sacrificing the O(1) inference and O(N) training efficiency that distinguishes RNNs from Transformers.**

---

## Problem Solutions

The paper introduces two progressive architectural refinements to RWKV-4:

1. **Eagle (RWKV-5): Matrix-valued states.** Upgrade the per-head recurrent state from a vector in R^(D/h) to a matrix in R^(D/h × D/h), dramatically increasing per-head state capacity. Add LayerNorm over attention heads, SiLU-based attention gating, and improved initialization. Remove the sigmoid activation on the receptance vector.

2. **Finch (RWKV-6): Data-dependent recurrence.** Make both the token-shift interpolation and the decay schedule input-dependent via lightweight LoRA modules. The decay w_t now varies at each time step based on the current and previous tokens, enabling dynamic memory management. Token shift interpolation factors also become data-dependent via LoRA (data-dependent linear interpolation, "ddlerp").

3. **Infrastructure contributions.** Introduce the RWKV World Tokenizer (65,536 tokens, Trie-based greedy matching, multilingual-aware vocabulary) and RWKV World v2 Dataset (1.12 trillion tokens, 70% English / 15% multilingual / 15% code).

---

## Approach Details

### Method

#### RWKV-4 Background

The RWKV architecture reformulates the Attention Free Transformer (AFT) by replacing pairwise positional biases with a channelwise additive decay vector w and a bonus term u for the current token. The RWKV-4 WKV attention is:

> wkv_t = (sum_{i=1}^{t-1} exp(-(t-1-i)w + k_i) . v_i + exp(u + k_t) . v_t) / (sum_{i=1}^{t-1} exp(-(t-1-i)w + k_i) + exp(u + k_t))

In recurrent form, RWKV-4 maintains a vector-valued state per head. The architecture consists of stacked residual blocks, each containing a Time Mixing sub-layer (analogous to attention) and a Channel Mixing sub-layer (analogous to FFN), both preceded by LayerNorm.

#### Eagle (RWKV-5) Architecture

Eagle makes four changes to RWKV-4:

**1. Matrix-valued states.** The recurrent state s is upgraded from R^(D/h) to R^(D/h × D/h). The WKV computation becomes:

> wkv' = s + diag(u) · k^T · v
> s' = diag(w) · s + k^T · v

where k^T · v is an outer product producing a (D/h × D/h) matrix. Each head now stores a matrix that accumulates key-value associations across time steps.

**2. Token Shift.** Linear interpolation (lerp) between current and previous token embeddings before projecting to r, k, v, g vectors:

> □_t = lerp_□(x_t, x_{t-1}) W_□,  □ in {r, k, v, g}

where lerp_μ(a, b) = a + (b - a) . μ and each μ is a learnable vector in R^D.

**3. SiLU gating and LayerNorm.** The output combines a SiLU-gated branch with LayerNorm applied per-head over the WKV result:

> o_t = concat(SiLU(g_t) . LayerNorm(r_t · wkv_t)) W_o

**4. Decay as contraction.** The decay w = exp(-exp(ω)) where ω is the learned parameter, ensuring w in (0, 1) and making diag(w) a guaranteed contraction matrix.

#### Finch (RWKV-6) Architecture

Finch extends Eagle with two data-dependent mechanisms:

**1. Data-dependent Token Shift (ddlerp).** The interpolation factor becomes input-dependent via a LoRA module:

> lora_□(x) = λ_□ + tanh(x A_□) B_□
> ddlerp_□(a, b) = a + (b - a) . lora_□(a + (b - a) . μ_x)

where A_□ in R^(D×32) and B_□ in R^(32×D) are trainable LoRA weights. This allows each channel's mix of current and prior tokens to depend on input content.

**2. Data-dependent decay.** The decay w_t is now time-varying:

> d_t = lora_d(ddlerp_d(x_t, x_{t-1}))
> w_t = exp(-exp(d_t))

The WKV recurrence becomes:

> wkv' = s + diag(u) · k^T · v
> s' = diag(w_t) · s + k^T · v

Unlike Eagle where w is static across all time steps, Finch's w_t varies at each position based on the input. This is the core expressivity improvement: the model can dynamically decide how much of each state channel to retain or forget.

#### Channel Mixing

Both Eagle and Finch retain RWKV-4's Channel Mixing module, with slightly reduced hidden dimension (3.5D instead of 4D in Eagle) to account for additional gating parameters while maintaining equi-parameter counts:

> r'_t = lerp_{r'}(x'_t, x'_{t-1}) W_{r'}
> k'_t = lerp_{k'}(x'_t, x'_{t-1}) W_{k'}
> v'_t = ReLU(k'_t)² W_{v'}
> o'_t = σ(r'_t) . v'_t

### Key Technical Components

**Complexity.** Both Eagle and Finch maintain RWKV-4's complexity profile: O(1) time and memory per token at inference, O(N) training time and memory, with full parallelizability across the time dimension. The matrix-valued state adds a constant factor (D/h additional floats per head) but does not change asymptotic complexity.

**Model configurations:**

| Model | Params | Layers | d_model | Heads | Training Tokens |
|-------|--------|--------|---------|-------|-----------------|
| Eagle 0.4B | 0.46B | 24 | 1024 | 16 | 1.12T |
| Eagle 1.5B | 1.5B | 24 | 2048 | 32 | 1.12T |
| Eagle 3B | 2.8B | 32 | 2560 | 40 | 1.12T |
| Eagle 7B | 7.5B | 32 | 4096 | 64 | 1.12T |
| Finch 1.6B | 1.6B | 24 | 2048 | 32 | 1.12T |
| Finch 3B | 3.1B | 32 | 2560 | 40 | 1.12T |

All models pretrained with context length 4096 on the RWKV World v2 multilingual corpus.

**RWKV World Tokenizer.** Vocabulary of 65,536 tokens constructed by merging vocabularies from GPT-NeoX-20B, GPT-2, cl100k_base (tiktoken), LLaMA-2, and BLOOM tokenizers, with manual selection to ensure non-European language coverage. Implemented via Trie-based greedy matching rather than BPE.

**RWKV World v2 Dataset.** 1.12 trillion tokens from publicly available sources: approximately 70% English, 15% multilingual, and 15% code. Emphasis on cultural works (stories, books, subtitles, conversations) alongside factual knowledge and code.

### Experimental Setup

**LM Evaluation Harness benchmarks (English):** LAMBADA (OpenAI), PIQA, StoryCloze16, HellaSwag, WinoGrande, ARC (easy and challenge), HeadQA (English), OpenBookQA, SciQ, ReCoRD, COPA. Evaluated zero-shot.

**Multilingual benchmarks:** LAMBADA Multilingual, XCOPA, XNLI, PAWS-X, XStoryCloze, XWinoGrande.

**Associative recall:** Multi-Query Associative Recall (MQAR) at sequence lengths 64--512 and model dimensions 64--512.

**Long context:** PG-19 test set loss vs. sequence position (token 2048 onward). Bamboo benchmark (4K version, 9 tasks: question answering, hallucination detection, text sorting, language modeling, code completion).

**Baselines:** Pythia (1.4B, 2.8B, 6.9B), Mamba (1.4B, 2.8B), RWKV-4 (1.5B, 3B, 7B), Falcon-7B, LLaMA-2-7B, Mistral-7B-v0.1, MPT-7B, StableLM-3B-8K.

**Efficiency:** Speed and memory benchmarked on A100 80GB with batch size 8, d_model 4096, head size 64, comparing Finch kernel against FlashAttention-2 and Mamba.

### Key Results

#### English Benchmarks (Table 4)

| Model | lmb.o | hella | piqa | arcE | arcC | glue | winG | sciq | copa | avg |
|-------|-------|-------|------|------|------|------|------|------|------|-----|
| Pythia-1.4B | 61.0 | 52.0 | 70.8 | 61.4 | 26.2 | 47.1 | 57.3 | 86.5 | 71.0 | 59.3 |
| Mamba-1.4B | 64.5 | 59.0 | 74.2 | 65.0 | 30.1 | 47.0 | 61.3 | 87.1 | 80.0 | 63.1 |
| Eagle-1.5B | 65.7 | 55.0 | 71.1 | 62.2 | 28.7 | 54.1 | 59.1 | 89.7 | 76.0 | 62.4 |
| **Finch-1.6B** | **66.8** | 57.3 | 72.6 | 62.7 | 29.8 | 49.8 | 59.4 | **89.6** | 78.0 | **62.9** |
| Eagle-7B | 75.5 | **81.0** | **80.5** | **80.8** | **50.1** | 51.5 | **73.6** | **95.9** | **93.0** | **75.8** |
| Mistral-7B-v0.1 | **75.5** | **81.0** | **80.5** | **80.8** | **50.1** | 51.5 | **73.6** | **95.9** | **93.0** | **75.8** |

- At the 1.5B scale, Finch-1.6B and Mamba-1.4B are closely competitive; Finch leads on LAMBADA and SciQ, Mamba leads on HellaSwag and ARC-C.
- Eagle-7B is competitive with Mistral-7B-v0.1 on English benchmarks despite training on ~2x fewer tokens.

#### Multilingual Benchmarks (Table 3)

| Model | lmb.m ppl↓ | lmb.m acc↑ | pawsx | xcopa | xnli | xsClz | xwin | avg |
|-------|------------|------------|-------|-------|------|-------|------|-----|
| Pythia-6.9B | 85.6 | 36.7 | 48.4 | 54.1 | 40.0 | 54.2 | 70.9 | 50.7 |
| Llama-2-7B | 30.4 | 50.8 | 41.2 | 56.7 | 39.9 | 57.5 | 79.5 | 54.3 |
| Falcon-7B | 28.7 | 51.3 | 48.2 | 56.0 | 39.0 | 56.0 | 77.7 | 54.7 |
| RWKV-4-7B | 33.1 | 47.4 | **52.1** | 60.1 | 41.2 | 60.9 | 76.5 | 56.4 |
| **Eagle-7B** | **21.0** | **53.7** | 45.6 | **62.2** | **44.0** | **63.3** | **80.4** | **58.2** |

- Eagle-7B achieves the best multilingual average across all 7B-class models, despite using ~2x fewer training FLOPs than LLaMA-2-7B.
- On multilingual FLOPs-vs-accuracy (Figure 2), Eagle and Finch represent a substantial improvement to the Pareto frontier.

#### Multi-Query Associative Recall (Figure 4)

Finch (RWKV-6) achieves near-perfect MQAR accuracy across all tested sequence lengths (64--512) and model dimensions (64--512), outperforming RWKV-4 (Dove), Eagle (RWKV-5), Mamba, Hyena, and Based. Eagle improves substantially over RWKV-4 at larger model dimensions but still falls short of Finch and attention-based models at longer sequences. Despite sharing data-dependent memory modification with Mamba, Finch outperforms it on MQAR, suggesting the specific combination of matrix-valued states and data-dependent decay is more effective for associative recall.

#### Long Context (Figure 5, Table 5)

On PG-19 loss vs. position (3B models, trained at 4096 context), Eagle and Finch maintain decreasing loss well beyond the training context length, while RWKV-4 degrades sharply beyond 4096. Finch achieves the lowest loss throughout.

On Bamboo (4K version):

| Model | avg |
|-------|-----|
| Pythia-6.9B | 3.3% |
| Eagle-7B | 16.8% |
| Eagle-7B-Hermes | 16.8% (with 50.3% on senhallu) |
| LLaMA2-Chat-7B | 24.1% |
| Mistral-Instruct-7B | 39.3% |

Eagle-7B outperforms Pythia-6.9B by 13.5 percentage points, though instruction-tuned models (Mistral-Instruct, LLaMA2-Chat) still lead, indicating Eagle's base model capabilities but the importance of instruction tuning.

#### Speed and Memory (Figures 6, 7)

- **Training time** scales linearly with sequence length for Finch (matching Mamba), while FlashAttention-2 scales quadratically. Finch is ~4.2x faster at 16K sequence length.
- **Memory** at 16K: Finch uses 23.6 GB vs FlashAttention-2's 32.8 GB (28% less) and Mamba's 27.7 GB (15% less).
- At sequence lengths ≤2K, FlashAttention-2 is faster due to optimized constant factors.

---

## Limitations and Failure Modes

### Acknowledged Limitations

1. **Scale ceiling.** Largest models are 7.5B (Eagle) and 3.1B (Finch). Scaling behavior at 14B+ is unknown. The authors note plans for larger Finch models as future work.

2. **Embedding model weakness.** Eagle was tested as an embedding model on MTEB but could not achieve strong performance. The authors hypothesize the state is a high-quality context embedding but no appropriate aggregation method has been found.

3. **Training data contamination.** The corpus contains some synthetic data from GPT-3.5/ChatGPT, causing released models to occasionally mimic ChatGPT's style and claim to be trained by OpenAI.

4. **Training data scale.** The 1.12T token corpus is smaller than contemporary corpora (LLaMA-2 uses 2T tokens), potentially limiting performance at the 7B scale.

### Observed Failure Modes

1. **English benchmarks at small scale.** At 1.5B--3B, Eagle and Finch slightly underperform Mamba on some English benchmarks (e.g., HellaSwag, ARC-C), suggesting the multilingual training distribution trades some English-specific performance for multilingual capability.

2. **Bamboo vs instruction-tuned models.** On the Bamboo benchmark, even Eagle-7B (base) substantially lags behind Mistral-Instruct-7B (39.3% vs 16.8%), showing the importance of instruction tuning for long-context reasoning tasks.

### Scope and Comparability

**What was not tested:**
- Models larger than 7.5B parameters
- Instruction-tuned or RLHF'd versions at scale (only Hermes fine-tune shown)
- Direct comparison with Mamba at 7B scale (Mamba models only go to 2.8B)
- Standardized long-context benchmarks like RULER, LongBench, or InfiniteBench
- Head-to-head comparison controlling for training data (different corpus than Pythia/Mamba)

**Comparability notes:**
- Different training data from most baselines (RWKV World v2 vs The Pile), making direct architectural comparisons imprecise
- Multilingual advantage partly reflects the multilingual-focused training corpus, not purely architectural improvement
- FLOPs comparison in Figures 2--3 is the most fair comparison, as it accounts for varying training budgets

---

## Conclusions

### Contributions

1. **Matrix-valued recurrent states.** Upgraded RWKV's per-head state from vectors to matrices, increasing state capacity from D/h to (D/h)² floats per head, enabling richer key-value association storage without changing asymptotic complexity.

2. **Data-dependent recurrence.** Introduced LoRA-based data-dependent token shift (ddlerp) and data-dependent decay in Finch, enabling the model to dynamically control information flow based on input content rather than fixed learned schedules.

3. **MQAR breakthrough for RNNs.** Demonstrated that Finch achieves near-perfect multi-query associative recall, the first non-Transformer architecture to do so, closing a key expressivity gap.

4. **Multilingual efficiency frontier.** Showed that Eagle and Finch substantially advance the Pareto frontier of multilingual accuracy vs. training FLOPs among open models.

5. **Fully open release.** Released six models (0.4B--7.5B), training code, inference code, tokenizer, and dataset under Apache 2.0, providing the most complete open reproduction package for alternative-architecture LLMs.

6. **Efficiency demonstration.** Showed Finch's training kernel is 4.2x faster than FlashAttention-2 at 16K with 40% less memory, while maintaining O(1) inference.

### Implications

1. **RNN competitiveness is real.** At 7B scale, RWKV-based models match Transformers on English benchmarks and exceed them on multilingual tasks at equivalent FLOPs. The architecture choice between Transformers and RNNs is now a genuine engineering tradeoff rather than a clear Transformer advantage.

2. **Matrix states as a general principle.** The upgrade from vector to matrix recurrent states is a simple, general technique that could benefit any linear attention or RNN architecture.

3. **Data-dependent dynamics are key.** The progression from RWKV-4 (static decay) to Eagle (static decay, matrix states) to Finch (data-dependent decay, matrix states) shows that data-dependent dynamics provide the largest expressivity gains, particularly for associative recall.

4. **Deployment viability.** O(1) per-token inference with no KV cache makes these models attractive for edge deployment and streaming applications where memory and latency constraints are binding. The RWKV-6 architecture has been deployed in production (Microsoft Windows Copilot runtime).

---

## Key Claims

1. **C1:** Eagle and Finch achieve competitive English benchmark performance with similarly-sized Transformers (Table 4, Figure 3). Supported by zero-shot evaluation on 10 English benchmarks. Eagle-7B averages 71.5%, competitive with Mistral-7B-v0.1 at 75.8%, despite training on 2x fewer tokens with a multilingual corpus. Evidence breadth: comprehensive benchmark suite, but different training data limits strict architectural comparison.

2. **C2:** Eagle and Finch substantially outperform other models on multilingual benchmarks at similar FLOPs (Table 3, Figure 2). Supported by evaluation on 6 multilingual benchmarks. Eagle-7B achieves 58.2% average vs next-best RWKV-4-7B at 56.4%. Note: multilingual advantage is partly attributable to the multilingual-focused training corpus, not purely architecture.

3. **C3:** Finch achieves near-perfect MQAR accuracy, outperforming all non-Transformer architectures (Figure 4, Section 8.2). Supported by controlled MQAR experiments at 4 sequence lengths and 4 model dimensions. Finch achieves ~100% accuracy where Mamba, Hyena, and RWKV-4 degrade. This is the strongest evidence for the architectural contribution.

4. **C4:** Finch training speed scales linearly with sequence length and is 4.2x faster than FlashAttention at 16K (Figure 7, Section 9). Supported by kernel benchmarks on A100 80GB. Also uses 40% less memory than FlashAttention-2 at 16K. Note: single hardware configuration tested; constant factors may differ on other GPUs.

5. **C5:** Eagle and Finch extrapolate well beyond 4096 training context on PG-19 (Figure 5, Section 8.3). Supported by loss curves on PG-19 test set showing maintained or decreasing loss to ~16K tokens. Qualitative finding; no formal extrapolation benchmark (e.g., RULER) was used.

6. **C6:** Eagle-7B outperforms Pythia-6.9B on Bamboo long-context benchmark by 13.5% average (Table 5, Section 8.4). Supported by 9-task evaluation at 4K context. However, instruction-tuned models (Mistral-Instruct) far outperform both, and the comparison conflates architecture with training data differences.

---

## Open Questions

1. **Does Finch scale to 14B+ parameters?** The authors explicitly mention plans for 7B and 14B Finch models. Whether the advantages of data-dependent decay persist at larger scales is unknown.

2. **How do Eagle/Finch perform with instruction tuning and RLHF?** Only base models and a Hermes fine-tune are evaluated. The effectiveness of the RWKV architecture for alignment at scale is untested.

3. **Can RWKV architectures be combined with MoE?** The authors mention MoE as future work. Given MoE's success with Transformers (Mixtral, Switch Transformer), the interaction with RWKV's linear attention is an open question.

4. **What is the precise role of matrix-valued states vs. data-dependent decay?** The ablation between Eagle (matrix states, static decay) and Finch (matrix states, data-dependent decay) shows decay matters, but the individual contribution of matrix states vs. additional head capacity is not cleanly ablated.

5. **How do Eagle/Finch perform on standardized long-context benchmarks?** The paper uses PG-19 loss and Bamboo but does not evaluate on RULER, LongBench, InfiniteBench, or NIAH, making comparison with other long-context methods difficult.

---

## Core References and Why They Are Referenced

### RWKV Architecture Lineage

- **Peng et al. (2023)** -- *RWKV: Reinventing RNNs for the Transformer Era.* Direct predecessor (RWKV-4) that Eagle and Finch build upon; introduced the WKV attention mechanism combining exponential decay with linear attention.

- **Zhai et al. (2021)** -- *An Attention Free Transformer.* Introduced the Attention Free Transformer (AFT) with learned pairwise positional biases, which RWKV-4 reformulated into its channelwise decay-based attention.

### Efficient Sequence Models

- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* Concurrent work introducing data-dependent SSMs; compared against on MQAR and efficiency benchmarks. Shares the goal of linear-time modeling with data-dependent dynamics.

- **Gu et al. (2022)** -- *Efficiently Modeling Long Sequences with Structured State Spaces (S4).* Foundational SSM work; RWKV takes a different path (linear attention) but addresses the same problem of efficient long-sequence modeling.

- **Katharopoulos et al. (2020)** -- *Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention.* Established the connection between linear attention and RNNs that RWKV builds upon.

### Data-Dependent Recurrence (Concurrent Work)

- **Yang et al. (2023)** -- *Gated Linear Attention Transformers with Hardware-Efficient Training.* Concurrent work on data-dependent gated linear attention.

- **De et al. (2024)** -- *Griffin: Mixing Gated Linear Recurrences with Local Attention.* Concurrent work combining gated linear recurrence with local attention.

- **Qin et al. (2023)** -- *HGRN: Hierarchically Gated Recurrent Neural Network.* Data-dependent RNN with input and forget gates.

### Training Infrastructure and Baselines

- **Biderman et al. (2023)** -- *Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.* Provides controlled baselines (Pythia models) for comparison across scales.

- **Touvron et al. (2023)** -- *LLaMA 2: Open Foundation and Fine-Tuned Chat Models.* Key baseline at 7B scale; LLaMA-2 tokenizer also used in RWKV World Tokenizer construction.

- **Hu et al. (2022)** -- *LoRA: Low-Rank Adaptation of Large Language Models.* Finch uses LoRA-style low-rank modules for data-dependent token shift and decay, repurposing an adaptation technique as an architectural component.

### Evaluation

- **Arora et al. (2023)** -- *Zoology: Measuring and Improving Recall in Efficient Language Models.* Introduced the MQAR benchmark used to evaluate associative recall capability.

- **Dao (2023)** -- *FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning.* Key efficiency baseline; Finch's kernel is benchmarked against FlashAttention-2.

- **Dong et al. (2023)** -- *Bamboo: A Comprehensive Benchmark for Evaluating Long Text Modeling Capacities.* Long-context benchmark used to evaluate models at 4K context.
