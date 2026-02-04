---
title: "The Impact of Positional Encoding on Length Generalization in Transformers"
authors: "Kazemnejad, Padhi, Natesan Ramamurthy, Das, Reddy"
year: 2023
venue: "NeurIPS 2023"
paper_type: conference-paper
categories: ["position-encoding", "attention-analysis", "probing-and-analysis"]
scope: ["length generalization", "decoder-only transformers", "NoPE", "scratchpad / chain-of-thought", "downstream task evaluation"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "NoPE outperforms all explicit positional encodings on length generalization across downstream tasks, achieving a mean reciprocal rank of 0.69 vs 0.55 for the next-best T5 Relative PE"
    evidence: "Figure 1, Figure 2, Section 4"
    status: supported
  - id: C2
    claim: "Commonly used positional encodings in LLMs (ALiBi, Rotary, APE) are ill-suited for length generalization on downstream tasks, with Rotary performing more similarly to APE than to other relative schemes"
    evidence: "Figure 1, Figure 2, Figure 3, Section 4"
    status: supported
  - id: C3
    claim: "NoPE can theoretically represent both absolute and relative positional encodings via the causal attention mask and feedforward layers"
    evidence: "Theorem 1, Theorem 2, Appendix C"
    status: supported
    contested_by: 2025-04-round-and-round-rope
  - id: C4
    claim: "NoPE empirically learns attention patterns most similar to T5's Relative PE, as measured by Jensen-Shannon divergence between attention distributions across layers"
    evidence: "Figure 4, Section 5.2"
    status: supported
  - id: C5
    claim: "Scratchpad/chain-of-thought is not always helpful for length generalization and its format highly impacts performance; it is beneficial only for the addition task across all PEs"
    evidence: "Figure 6, Section 6"
    status: supported
  - id: C6
    claim: "NoPE and T5 Relative PE exhibit bimodal attention distributions (both short-range and long-range), while ALiBi strongly favors short-range and Rotary/APE show uniform distributions"
    evidence: "Figure 7, Section 6.1"
    status: supported
  - id: C7
    claim: "At 1.3B scale pretraining, Rotary fails to generalize beyond training context (perplexity explodes), while NoPE and ALiBi generalize up to approximately twice the training context length"
    evidence: "Tables 3-4, Figure F.2, Appendix F"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: evaluates
    detail: "Evaluates sinusoidal APE from the original Transformer as a baseline positional encoding for length generalization"
  - target: 2022-04-alibi-train-short-test-long
    type: evaluates
    detail: "Evaluates ALiBi as a baseline; finds it underperforms T5 Relative PE and NoPE on downstream length generalization despite its promise for perplexity-based extrapolation"
  - target: 2022-12-nope-transformers-learn-positions
    type: extends
    detail: "Extends Haviv et al.'s finding that NoPE is competitive for language modeling to the length generalization setting, showing NoPE outperforms all explicit PEs on downstream tasks"
  - target: 2024-01-roformer-rope
    type: evaluates
    detail: "Evaluates Rotary (RoPE) as a baseline; finds it performs similarly to APE and poorly on length generalization, despite being classified as a relative PE"
  - target: 2022-12-chain-of-thought-prompting
    type: complementary
    detail: "Studies the interaction between positional encoding and scratchpad/chain-of-thought, finding that scratchpad is task-dependent and does not render PE choice irrelevant"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: extended-by
    detail: "DroPE builds on Kazemnejad et al.'s NoPE expressivity results to motivate dropping positional embeddings from pretrained models for context extension"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Wu et al. provide a graph-theoretic analysis of causal masking and position bias, offering a different perspective on how position information is encoded without explicit PE"
  - target: 2025-04-round-and-round-rope
    type: complementary
    detail: "Sun et al. show that NoPE cannot learn periodic positional patterns in a single attention head, refining Kazemnejad et al.'s Universal Approximation Theorem-based expressivity argument"
open_questions:
  - question: "Does NoPE's advantage on length generalization hold when scaling to large-scale pretraining (10B+ parameters) with natural language data?"
    addressed_by: null
  - question: "Can NoPE outperform explicit PEs on length generalization in pretrained models fine-tuned on downstream tasks, rather than models trained from scratch?"
    addressed_by: null
  - question: "What is the precise mechanism by which NoPE learns relative positional information via the causal mask?"
    addressed_by: 2025-07-position-bias-transformers
  - question: "Does the bimodal attention distribution (short-range + long-range) causally improve length generalization, or is it merely correlated?"
    addressed_by: null
---

# The Impact of Positional Encoding on Length Generalization in Transformers

**Authors:** Amirhossein Kazemnejad, Inkit Padhi, Karthikeyan Natesan Ramamurthy, Payel Das, Siva Reddy (Mila / McGill University, IBM Research)
**Date:** December 2023, NeurIPS 2023, arXiv:2305.19466

---

## Core Research Problem

Length generalization -- the ability to generalize from small training context sizes to larger ones -- is a critical challenge for Transformer-based language models. Positional encoding (PE) has been identified as a major factor influencing length generalization, but prior evaluations have relied primarily on language modeling perplexity, which does not always correlate with downstream task performance (Tay et al., 2022). This creates ambiguity about which PE method actually generalizes best.

Relative PEs (Shaw et al., 2018; Raffel et al., 2020) are widely believed to outperform absolute PEs for length generalization (Ontanon et al., 2022; Csordas et al., 2021), but Press et al. (2022) showed that even relative PEs like Rotary can be poor at extrapolation. Meanwhile, Haviv et al. (2022) demonstrated that decoder-only Transformers without positional encoding (NoPE) achieve competitive perplexity, but the implications for length generalization on downstream tasks were unexplored.

The core challenge is: **how different positional encoding schemes impact length generalization in decoder-only Transformers on downstream reasoning and mathematical tasks, and whether explicit positional encoding is necessary at all.**

---

## Problem Solutions

The paper provides a systematic empirical comparison of five PE schemes on length generalization across 10 downstream tasks, complemented by theoretical and empirical analysis of NoPE's mechanisms. The key findings are:

1. **NoPE outperforms all explicit PEs** on length generalization across downstream tasks, achieving a mean reciprocal rank (MRR) of 0.69, followed by T5's Relative PE (0.55), ALiBi (0.50), Rotary (0.33), and APE (0.22).
2. **NoPE can theoretically represent both absolute and relative PEs** via the causal attention mask and feedforward layers (Theorems 1 and 2).
3. **NoPE empirically resembles T5's Relative PE** in attention patterns, as measured by Jensen-Shannon divergence between attention head distributions.
4. **Scratchpad/CoT does not render PE choice irrelevant** -- it is beneficial only for addition across all PEs, and its format has non-trivial impact on performance.

---

## Approach Details

### Method

The study compares five positional encoding approaches, all applied to a conventional decoder-only Transformer trained from scratch:

- **APE (Absolute Position Embedding):** Sinusoidal variant (Vaswani et al., 2017), since the learned variant cannot produce embeddings for unseen positions.
- **T5's Relative PE:** Learned scalar bias `b = f(i - j)` added to attention dot products, with a bucket function mapping large distances to shared parameters (Raffel et al., 2020). Original T5 uses B = 32 buckets, D = 128 max distance.
- **ALiBi:** Linear bias subtracted from attention scores proportional to query-key distance, creating a recency bias (Press et al., 2022).
- **Rotary (RoPE):** Rotates query and key representations by angle proportional to absolute position before dot product, making attention depend on relative distance (Su et al., 2021).
- **NoPE:** No positional encoding of any kind. The dot product is simply `q_t^T k_i`.

All models use the "base" configuration from HuggingFace: ~107M parameters, 12 layers, 768 model dimension, 12 attention heads.

### Key Technical Components

**Length generalization setup.** Following Anil et al. (2022), each task defines a function `lambda: D -> N` returning the length/depth of an instance. Training uses instances where `lambda <= L` (default L = 20), evaluation uses `lambda in [1, 2L]` to include both seen and unseen lengths. Performance is measured as exact-match accuracy.

**Aggregate ranking.** Following Liang et al. (2022), the paper reports mean reciprocal rank (MRR) of PE methods when compared against each other across all tasks and scenarios, providing a holistic ranking.

**Attention pattern similarity.** To compare NoPE's learned mechanism to explicit PEs, the paper measures the minimum Jensen-Shannon divergence between attention head distributions across models:

> `D^(l)(A, B) = min_{(P,Q) in A_l x B_l} D_AT(P, Q)`

where `D_AT(P, Q) = (1/T) sum_{t=1}^{T} D_JSD(P_t || Q_t)` averages JSD over all positions.

**Scratchpad format analysis.** The paper decomposes each scratchpad step into five components: Step Input (I), Step Computation (C), Step Output (O), Intermediate Variable Updates (V), and Remaining Input (R). Different combinations of these components are systematically evaluated.

### Theoretical Analysis

**Theorem 1 (Absolute Encoding).** The first layer of a NoPE Transformer can recover absolute positions `[1, ..., T+1]` in the hidden state `H^(1)`. The proof constructs weights such that (a) all key vectors are identical (by reading the constant first dimension of embeddings), (b) the value vectors are non-zero only for the `<bos>` token, and (c) the uniform attention distribution produces `1/t` at position `t`, which the feedforward layer can invert to recover absolute positions (Appendix C.1).

**Theorem 2 (Relative Encoding).** Given absolute positions in `H^(1)`, subsequent layers can implement relative positional encoding. The proof constructs `W_Q` and `W_K` such that:

> `<q_t, k_i> = f_cnt(q_t, k_i) + f_rel(t - i)`

where `f_cnt` depends on content and `f_rel` depends on relative distance. The construction places position `t` in the query with a negative sign and position `i` in the key, producing an `(i - t)` term in the dot product (Appendix C.2).

### Experimental Setup

**Tasks (10 total in 3 categories):**

- *Primitive tasks:* Copy (5 variants), Reverse (3 variants)
- *Mathematical and reasoning tasks:* Addition, Polynomial Evaluation, Sorting (Single Token, Multi Digit), Summation, Parity, LEGO
- *Classical length generalization datasets:* SCAN (Lake and Baroni, 2018), PCFG (Hupkes et al., 2020)

**Training:** 100K training examples, 10K test examples per task. Length threshold L = 20 (L = 8 for scratchpad tasks). 3 seeds per dataset-PE pair. AdamW optimizer, lr = 3e-5, weight decay 0.05, batch size 64, 40K training steps, polynomial LR scheduler, 6% warmup.

**1.3B scale experiment (Appendix F):** 24 layers, d_model = 1024, d_kv = 128, d_ff = 16384, 32 attention heads. Trained on 30B tokens from a StarCoder subset (40% Python, 25% Java, 25% JavaScript, 5% GitHub issues, 5% GitHub commits). Context length 1024. Only ALiBi, Rotary, and NoPE compared.

### Key Results

**Aggregate MRR ranking (Figure 1):**

| Positional Encoding | MRR |
|---|---|
| NoPE | 0.69 |
| T5's Relative PE | 0.55 |
| ALiBi | 0.50 |
| Rotary | 0.33 |
| APE | 0.22 |

- NoPE outperforms all explicit PEs on aggregate ranking across all 10 tasks (Figure 1).
- T5's Relative PE is the best explicit PE. ALiBi is in the middle. Rotary and APE show poor length generalization (Figure 2).
- All models achieve perfect or near-perfect accuracy on I.I.D. lengths; differences emerge only at extrapolation lengths (Figure 3).

**Attention pattern similarity (Figure 4, Section 5.2):**

- NoPE's attention patterns are most similar to T5's Relative PE across all layers and length buckets (D_AT approximately 0.25 average).
- NoPE is least similar to APE and Rotary (D_AT approximately 1.0--1.5 average).
- The distance between two NoPE seeds is comparable to the NoPE--T5 distance, serving as a baseline.

**Scratchpad results (Figure 6, Section 6):**

- Scratchpad is beneficial only for the addition task across all PEs.
- For all other tasks (LEGO, Parity, Polynomial Evaluation, Sorting, Summation), scratchpad does not consistently improve length generalization.
- The scratchpad format significantly impacts performance; the optimal format differs across PEs (Figure F.8).

**Attention distance distributions (Figure 7, Section 6.1):**

| PE Method | Attention Distribution |
|---|---|
| NoPE | Bimodal (short-range + long-range) |
| T5's Relative PE | Bimodal (short-range + long-range) |
| ALiBi | Strongly short-range (recency bias) |
| Rotary | Uniform (similar to APE) |
| APE | Uniform |

- NoPE and T5 RPE, the top-performing methods, both show bimodal attention. ALiBi's recency bias restricts it to short-range attention (Figure 7).

**1.3B scale pretraining (Appendix F):**

| PE | I.I.D. PPL (1024 ctx) | OOD PPL (1800 ctx) | OOD PPL (2560 ctx) |
|---|---|---|---|
| NoPE | ~2.5 | ~30 | ~500 |
| ALiBi | ~2.5 | ~14 | ~150 |
| Rotary | ~2.5 | ~250+ (explodes) | ~800+ |

- At I.I.D. context (<=1024), all variants have similar perplexity.
- Rotary's perplexity explodes beyond the training context.
- NoPE and ALiBi generalize up to ~1800 tokens (~1.8x training context). Beyond that, ALiBi is more stable than NoPE.

---

## Limitations and Failure Modes

1. **Models trained from scratch on synthetic tasks.** All primary experiments use ~107M parameter models trained from scratch on algorithmic tasks. The authors acknowledge that no publicly available LLMs are trained with various PEs under identical conditions, preventing direct comparison of PE effects in large-scale pretraining (Limitations section).

2. **NoPE's advantage may not transfer to natural language pretraining.** The 1.3B scale experiment (Appendix F) evaluates only perplexity, not downstream length generalization. Preliminary fine-tuning yielded identical performance across PE variants because the 1.3B models' training context was much larger than the task instances (Section 7).

3. **ALiBi more stable than NoPE at larger scales.** At 1.3B scale, ALiBi maintains lower perplexity than NoPE beyond ~1800 tokens (Tables 3--4), suggesting NoPE's advantage observed on small-scale synthetic tasks may not persist at scale.

4. **Perplexity vs. downstream performance disconnect.** The paper argues that perplexity-based evaluation of length generalization can be misleading due to naturally occurring short-range dependencies in language data, which favor ALiBi's recency bias (Section 7). However, the paper's own downstream evaluation uses only synthetic tasks, not natural language downstream tasks.

5. **No evaluation of learned APE.** The paper uses sinusoidal APE rather than learned positional embeddings (used in GPT-3, OPT) because learned APE cannot produce embeddings for unseen positions. This means the APE baseline does not represent the most common variant in modern LLMs.

6. **Scratchpad tasks limited by compute.** Scratchpad experiments use L = 8 (vs L = 20 for non-scratchpad) due to the longer sequences causing out-of-memory errors (Section 6, footnote 1).

---

## Conclusions

### Contributions

1. **Systematic comparison of PE schemes on length generalization.** Provided the first comprehensive comparison of five positional encoding methods (APE, T5 Relative PE, ALiBi, Rotary, NoPE) on length generalization across 10 downstream tasks, showing clear distinctions among methods that are not visible in I.I.D. evaluation (Figures 1--3).

2. **NoPE as the best method for length generalization.** Demonstrated that decoder-only Transformers without any positional encoding outperform all explicit PE methods on downstream length generalization (MRR 0.69), while also requiring no additional computation in the attention mechanism (Figure 1, Section 4).

3. **Theoretical expressivity of NoPE.** Proved that NoPE can represent both absolute (Theorem 1) and relative (Theorem 2) positional encodings, establishing that the causal attention mask provides sufficient structural information for position recovery.

4. **Empirical characterization of NoPE's learned mechanism.** Showed through attention pattern analysis that NoPE trained with SGD learns patterns most similar to T5's Relative PE, a relative encoding scheme (Figure 4, Section 5.2).

5. **Scratchpad is not a universal solution.** Demonstrated that scratchpad/CoT is task-dependent (beneficial only for addition) and does not render PE choice irrelevant (Figure 6, Section 6).

6. **Characterization of attention distributions.** Identified that the top-performing PE methods (NoPE, T5 RPE) share a bimodal attention distribution (short-range + long-range), while poorly performing methods show either recency bias (ALiBi) or uniform attention (Rotary, APE) (Figure 7).

### Implications

1. **Explicit PEs may hinder length generalization.** The consistent underperformance of APE and Rotary -- the two most commonly used PEs in modern LLMs (GPT-3, PaLM, LLaMA) -- suggests that the inductive biases introduced by explicit PEs can actively harm generalization to unseen lengths.

2. **Rotary behaves like APE, not like a relative PE.** Despite being classified as a relative PE, Rotary shows attention patterns and length generalization behavior more similar to APE than to T5's Relative PE (Figures 4, 7). This is speculative beyond the scope of this paper but may explain Rotary's widespread adoption based on perplexity gains rather than length generalization.

3. **Perplexity is an unreliable proxy for length generalization.** ALiBi's strong perplexity-based extrapolation reported by Press et al. (2022) does not translate to downstream length generalization, underscoring the need for task-based evaluation.

---

## Key Claims

1. **C1: NoPE outperforms all explicit PEs on downstream length generalization (supported).** NoPE achieves MRR 0.69 across all tasks, followed by T5 RPE (0.55), ALiBi (0.50), Rotary (0.33), APE (0.22) (Figure 1). NoPE ranks first or second across all three task categories: primitive, mathematical/reasoning, and classical length generalization datasets (Figure 2). All models achieve near-perfect I.I.D. accuracy, confirming differences are specific to extrapolation (Figure 3).

2. **C2: Common LLM positional encodings (ALiBi, Rotary, APE) are ill-suited for length generalization (supported).** Rotary performs more similarly to APE than to relative PE schemes, both in task accuracy (Figures 1--2) and attention patterns (Figure 4). ALiBi's recency bias limits its attention to short-range dependencies (Figure 7), and it underperforms T5 RPE despite being a simplification of it (Section 4). This aligns with Taylor et al. (2022) who found no significant improvement from ALiBi.

3. **C3: NoPE can theoretically represent both absolute and relative PEs (supported, contested).** Theorem 1 proves the first layer can recover absolute positions `[1, ..., T+1]` via uniform attention over the `<bos>` token (Appendix C.1). Theorem 2 proves subsequent layers can implement relative PE (Appendix C.2). However, Sun et al. (2025) show that NoPE cannot learn periodic positional patterns in a single attention head, refining the expressivity argument.

4. **C4: NoPE empirically resembles T5's Relative PE (supported).** Attention pattern distance between NoPE and T5 RPE is approximately 0.25 (averaged across layers), comparable to the distance between different NoPE seeds. Distance to ALiBi, Rotary, and APE is 2--6x larger (~0.5--1.5) (Figure 4, right panel).

5. **C5: Scratchpad is not always helpful and format matters (supported).** Scratchpad improves all PEs only on the addition task. For the remaining 5 mathematical/reasoning tasks, no consistent benefit is observed regardless of format (Figure 6). The optimal scratchpad format varies by PE method (Figure F.8).

6. **C6: NoPE and T5 RPE show bimodal attention; ALiBi shows recency bias (supported).** Distribution of normalized attention distance shows clear bimodality for NoPE and T5 RPE (peaks near 0 and 1), strong peak near 0 for ALiBi, and approximately uniform distributions for Rotary and APE (Figure 7).

7. **C7: Rotary fails at 1.3B scale extrapolation; NoPE and ALiBi generalize to ~2x context (supported).** At 1.3B parameters pretrained on StarCoder with 1024-token context, Rotary perplexity exceeds 250 at 1200 tokens for length bucket [1500, 1750] while NoPE and ALiBi maintain ~2.1--2.3 (Table 3). NoPE and ALiBi diverge beyond ~1800 tokens, with ALiBi showing relative stability (Tables 3--4, Appendix F).

---

## Open Questions

1. **Does NoPE's advantage persist at large-scale pretraining?** The paper's primary experiments use ~107M models trained from scratch on synthetic tasks. The 1.3B experiment only evaluates perplexity, not downstream length generalization. Whether NoPE's advantage holds for 10B+ parameter models pretrained on natural language remains unknown. Not addressed in the references directory.

2. **Can NoPE outperform explicit PEs when fine-tuning pretrained models?** Preliminary fine-tuning at 1.3B yielded identical results because training contexts exceeded task lengths (Section 7). A comprehensive downstream evaluation with controlled context lengths is needed. Not addressed in the references directory.

3. **What is the precise mechanism by which NoPE learns relative positional information?** The theoretical proofs show existence but not uniqueness of the learned mechanism. Wu et al. (2025) provide a graph-theoretic analysis of how causal masking introduces directional bias. Partially addressed by `2025-07-position-bias-transformers`.

4. **Does the bimodal attention distribution causally improve length generalization?** The correlation between bimodal attention (NoPE, T5 RPE) and strong length generalization is suggestive but not causal. Whether enforcing bimodal attention would improve other PEs is untested. Not addressed in the references directory.

---

## Core References and Why They Are Referenced

### Positional Encoding Baselines

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture and sinusoidal APE, used as the APE baseline in all experiments.
- **Press et al. (2022)** -- *Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation.* Introduces ALiBi, a key baseline. The paper challenges ALiBi's promise for length generalization by showing it underperforms on downstream tasks.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces Rotary (RoPE), a baseline PE. The paper shows Rotary behaves more like APE than like relative PEs.
- **Raffel et al. (2020)** -- *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.* Introduces T5's Relative PE with the bucket function, which is the best-performing explicit PE in this study.
- **Shaw et al. (2018)** -- *Self-Attention with Relative Position Representations.* Introduces relative position representations for self-attention, foundational to the relative PE family.

### NoPE Predecessors

- **Haviv et al. (2022)** -- *Transformer Language Models without Positional Encodings Still Learn Positional Information.* Demonstrates NoPE's competitiveness on perplexity. This paper extends the finding to length generalization on downstream tasks.
- **Tsai et al. (2019)** -- *Transformer Dissection: An Unified Understanding for Transformer's Attention via the Lens of Kernel.* Explains why decoder-only Transformers are not order-agnostic due to the causal mask.

### Length Generalization

- **Anil et al. (2022)** -- *Exploring Length Generalization in Large Language Models.* Defines the length generalization evaluation framework (train on lambda <= L, test on lambda > L) adopted by this paper.
- **Ontanon et al. (2022)** -- *Making Transformers Solve Compositional Tasks.* Studies PE effects on length generalization, focusing on relative PE outperforming APE. This paper extends with more PE methods and NoPE.
- **Deletang et al. (2023)** -- *Neural Networks and the Chomsky Hierarchy.* Studies length generalization across neural architectures including Transformers, but does not compare PE methods or focus on autoregressive models.

### Scratchpad / Chain-of-Thought

- **Nye et al. (2021)** -- *Show Your Work: Scratchpads for Intermediate Computation with Language Models.* Introduces the scratchpad technique for intermediate computation, adopted as the baseline scratchpad format.
- **Wei et al. (2022)** -- *Chain of Thought Prompting Elicits Reasoning in Large Language Models.* Introduces chain-of-thought prompting, which this paper evaluates in the context of length generalization.

### Evaluation Datasets

- **Lake and Baroni (2018)** -- *Generalization without Systematicity.* Introduces SCAN, used as a classical length generalization benchmark.
- **Hupkes et al. (2020)** -- *Compositionality Decomposed: How Do Neural Networks Generalise?* Introduces PCFG, used as a classical length generalization benchmark.

### Theoretical Foundations

- **Weiss et al. (2021)** -- *Thinking Like Transformers.* Inspires the constructive proof of Theorem 1 showing NoPE can recover absolute positions.
- **Lindner et al. (2023)** -- *Tracr: Compiled Transformers as a Laboratory for Interpretability.* Inspires the constructive proof technique for Theorem 1.
