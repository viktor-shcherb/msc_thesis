---
title: "Transformer Language Models without Positional Encodings Still Learn Positional Information"
authors: "Haviv, Ram, Press, Izsak, Levy"
year: 2022
venue: "Findings of EMNLP 2022"
paper_type: conference-paper
categories: ["position-encoding", "probing-and-analysis"]
scope: ["causal language models", "implicit positional encoding", "NoPos transformers"]
benchmarks_used: ["perplexity-wikitext103", "perplexity-pile"]
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "Causal transformer LMs without explicit positional encoding (NoPos) achieve competitive perplexity with position-aware models, with gaps as small as 0.05 perplexity at 1.3B parameters on the Pile"
    evidence: "Table 1, Section 4"
    status: supported
    scope: "causal LMs, 247M (WikiText-103) and 125M-1.3B (Pile), word-level and BPE tokenization, English only"
    magnitude: "0.05 perplexity gap vs Learned at 1.3B on Pile; 0.55 gap at 247M on WikiText-103"
  - id: C2
    claim: "The competitiveness of NoPos models is robust across model sizes (125M-1.3B), datasets (WikiText-103, the Pile), and sequence lengths (256-2048)"
    evidence: "Tables 1-3, Section 4"
    status: supported
    scope: "125M-1.3B parameters, WikiText-103 and Pile datasets, 256-2048 token sequences, English only"
    magnitude: "NoPos-vs-Learned gap ranges from 0.04 to 0.55 perplexity across all tested settings"
  - id: C3
    claim: "NoPos models learn implicit absolute positional information, achieving similar probing accuracy to models with learned positional embeddings by the middle layers of the network"
    evidence: "Figure 2, Section 5"
    status: supported
    scope: "1.3B parameter model on the Pile, 1024-token sequences, probed with 2-layer feed-forward classifier"
    magnitude: "MAD drops from ~340 (random baseline) to comparable to Learned model (~15-20) by layer 12"
  - id: C4
    claim: "NoPos models fail for masked (bidirectional) language models, with perplexity of 147.18 vs 4.06 for learned embeddings"
    evidence: "Table 4, Section 6"
    status: supported
    scope: "RoBERTa-large architecture, 128-token sequences on the Pile, single model configuration"
    magnitude: "147.18 vs 4.06 perplexity (36x degradation)"
  - id: C5
    claim: "The causal attention mask is responsible for implicit positional encoding by allowing the model to infer the number of attendable predecessors at each position"
    evidence: "Section 6, Table 4 (MLM failure as supporting evidence)"
    status: unvalidated
    scope: "general conjecture for causal transformer LMs"
    magnitude: "qualitative"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Demonstrates that the transformer architecture can learn positions without explicit positional encodings when using causal attention"
  - target: 2022-04-alibi-train-short-test-long
    type: evaluates
    detail: "ALiBi is used as a baseline positional encoding method; outperforms NoPos consistently but the gap narrows at larger model sizes"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: extended-by
    detail: "DroPE builds on the NoPE finding by removing positional embeddings after pretraining with a short recalibration phase for zero-shot context extension"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Wu et al. provide a formal graph-theoretic analysis of the causal mask's effect on position bias, refining Haviv et al.'s conjecture about how causal attention encodes position"
  - target: 2023-12-positional-encoding-length-generalization
    type: extended-by
    detail: "Kazemnejad et al. extend the NoPE finding from perplexity competitiveness to length generalization on downstream tasks, showing NoPE outperforms all explicit PEs and theoretically proving NoPE can represent both absolute and relative PEs"
open_questions:
  - question: "Does the competitiveness of NoPos models hold at scales much larger than 1.3B parameters?"
    addressed_by: null
  - question: "What is the precise mechanism by which causal attention encodes positional information?"
    addressed_by: 2025-07-position-bias-transformers
  - question: "Can NoPos models extrapolate to sequence lengths beyond training?"
    addressed_by: 2025-12-drope-dropping-positional-embeddings
  - question: "Do NoPos models maintain competitive performance on downstream tasks beyond language modeling perplexity?"
    addressed_by: 2023-12-positional-encoding-length-generalization
---

# Transformer Language Models without Positional Encodings Still Learn Positional Information

**Authors:** Adi Haviv, Ori Ram, Ofir Press, Peter Izsak, Omer Levy (Tel Aviv University, University of Washington, Intel Labs, Meta AI)
**Date:** December 2022, Findings of EMNLP 2022, DOI:10.18653/v1/2022.findings-emnlp.99

---

## Core Research Problem

The transformer's self-attention mechanism is order-invariant: it is agnostic to the position of tokens in the input sequence. To convey token order, transformer models inject positional information explicitly, either through absolute positional embeddings (Vaswani et al., 2017; Gehring et al., 2017) or relative bias factors (Shaw et al., 2018; Raffel et al., 2020; Press et al., 2022). Removing these positional signals is widely assumed to render the model unable to distinguish token positions and thus unable to model language effectively.

However, there is limited prior work investigating whether models can infer positions implicitly. Irie et al. (2019) found that transformer LMs without positional encoding outperformed those with sinusoidal embeddings in speech recognition, and Biderman informally showed competitive results on a small 350M-parameter character-level model (enwik8). Neither work demonstrated robustness across scales and datasets, nor investigated how implicit positional information is acquired (Section 7).

The core challenge is: **whether causal transformer language models can learn useful positional information without any explicit positional encoding, and if so, through what mechanism.**

---

## Problem Solutions

The paper demonstrates empirically that causal transformer LMs trained without any positional encoding ("NoPos" models) are competitive with standard position-aware models. The key findings are:

1. **NoPos models achieve near-parity perplexity** with models using learned, sinusoidal, or ALiBi positional encodings, with the gap narrowing as model size increases.
2. **NoPos models acquire implicit absolute positional information** throughout the network, as demonstrated by probing classifiers that can predict token positions from internal representations.
3. **The causal attention mask is conjectured to be the mechanism** enabling implicit positional encoding: by restricting each token to attend only to its predecessors, the mask allows the model to infer the number of attendable tokens and thus approximate its absolute position.
4. **This phenomenon is unique to causal (autoregressive) models.** Masked language models (bidirectional) without positional encoding fail to converge, supporting the conjecture that causal masking is essential.

---

## Approach Details

### Method

The study compares four positional encoding strategies, all trained from scratch under identical conditions:

- **NoPos:** No explicit positional information of any kind.
- **Learned:** Trainable absolute positional embeddings (Sukhbaatar et al., 2015; Gehring et al., 2017), as used in BERT and GPT-3.
- **Sinusoidal:** Non-parametric position vectors computed from sine and cosine functions of different frequencies (Vaswani et al., 2017).
- **ALiBi:** Attention with Linear Biases (Press et al., 2022), which adds negative biases to attention scores proportional to the distance between tokens.

### Key Technical Components

**Position probing.** To determine whether NoPos models learn positional information, the authors freeze the trained LMs and train a separate 2-layer feed-forward ReLU network to predict the absolute position (0--1023) of each token from its hidden representation after each transformer layer. The probe is trained as a 1024-class classification problem. Performance is measured as mean absolute distance (MAD) between predicted and actual positions. Each layer's probe is trained separately (Section 5).

**Word order analysis.** To verify that positional information is necessary for the NoPos model's predictions, the authors shuffle the prefix tokens preceding a randomly selected target token and measure the change in loss. If the model were order-invariant, shuffling should not affect predictions. The experiment is conducted on the WikiText-103 NoPos model with 512-token sequences (Appendix B).

**MLM control experiment.** To test whether the causal mask is the source of implicit positional information, the authors train masked language models (using RoBERTa-large architecture) with and without positional encoding. Unlike causal LMs, MLMs use bidirectional attention and thus cannot infer position from the attention mask structure (Section 6).

**Segment-level analysis.** To determine whether NoPos models perform differently at different parts of the sequence, the authors split each 1024-token input sequence into eight consecutive segments and compute perplexity for each segment separately, comparing NoPos to the Learned baseline (Appendix A).

### Experimental Setup

**Canonical setting (WikiText-103).** The WikiText-103 corpus (Merity et al., 2017) contains over 100 million words from Wikipedia, tokenized at the word level (267K vocabulary). Model: adaptive embedding transformer (Baevski and Auli, 2019) with 16 layers, 1024 model dimensions, 4096 feed-forward dimensions, 8 attention heads, 247M total parameters. Sequence length: 512 tokens (shortened from 3072 as in Press et al., 2022). Optimizer: Nesterov accelerated gradient, peak learning rate 1, 16K warmup steps, 286K total steps, 72K tokens/batch, dropout 0.3 (Table 5, Appendix C).

**Large-scale setting (The Pile).** 2 of 30 shards from the Pile (Gao et al., 2020), filtered to remove GitHub and DM Mathematics sources and the shortest/longest 1% of examples. Tokenizer: GPT-2 (50K vocabulary). Validation set: 2000 documents (2.6M tokens). Training set: 15M documents (21B tokens). Model: GPT-3 XL architecture (Brown et al., 2020) with 24 layers, 2048 model dimensions, 8192 feed-forward dimensions, 32 attention heads, 1.3B parameters. Sequence length: 1024 tokens. Optimizer: Adam, learning rate 2e-3, 500 warmup steps, 10K total steps, 256K tokens/batch, no dropout, weight decay 0.01 (Table 5, Appendix C).

**Scaling experiments.** Model size scaling: 125M, 350M, 760M, 1.3B parameters on the Pile (1024-token sequences). Architecture details per size: 125M (12 layers, 768 dims, 3072 ff, 12 heads), 350M (24 layers, 1024 dims, 4096 ff, 16 heads), 760M (24 layers, 1536 dims, 6144 ff, 16 heads), 1.3B (24 layers, 2048 dims, 8192 ff, 32 heads) (Table 6, Appendix C). Sequence length scaling: 256, 512, 1024, 2048 tokens with the 1.3B model.

**Probing setup.** 2-layer feed-forward ReLU probe, trained separately per layer, sequence length 1024, Adam optimizer, learning rate 2e-3, 500 warmup steps, 10K steps, 64K tokens/batch (Table 5, Appendix C).

**MLM setup.** RoBERTa-large architecture (Liu et al., 2019), 128-token sequences on the Pile, Adam optimizer, learning rate 1e-3, 500 warmup steps, 10K steps, 1.024M tokens/batch, dropout 0.1 (Table 5, Appendix C).

**Reproducibility.** Code and trained models are publicly released at https://github.com/adihaviv/NoPos. No mention of random seeds or variance across runs for the Pile experiments. The authors note that training at 1.3B scale is resource-intensive (Section 9). For WikiText-103, Press et al. (2020) report that training with 5 different seeds can result in gaps of up to 0.9 perplexity (0.34 standard deviation), providing context for the WikiText-103 gap sizes (footnote 2, Section 4).

### Key Results

**Main perplexity comparison (Table 1):**

| Method | WikiText-103 | The Pile |
|---|---|---|
| NoPos | 20.97 | 13.10 |
| Learned | 20.42 | 13.05 |
| Sinusoidal | 20.16 | 12.93 |
| ALiBi | 19.71 | 12.51 |

- NoPos trails Learned by only 0.55 perplexity on WikiText-103 and 0.05 on the Pile (Table 1, Section 4).
- ALiBi consistently outperforms all methods, with a larger margin than the gap between the other three.
- The WikiText-103 gap of 0.55 is within the range of seed variance (up to 0.9) reported by Press et al. (2020) for that setting (footnote 2, Section 4).

**Model size scaling (Table 2, the Pile, 1024-token sequences):**

| Method | 125M | 350M | 760M | 1.3B |
|---|---|---|---|---|
| NoPos | 22.15 | 16.87 | 14.29 | 13.10 |
| Learned | 22.04 | 16.84 | 14.21 | 13.05 |
| Sinusoidal | 21.49 | 16.58 | 14.04 | 12.93 |
| ALiBi | 19.94 | 15.66 | 13.53 | 12.51 |

- The gap between NoPos and Learned narrows as model size increases: 0.11 at 125M, 0.03 at 350M, 0.08 at 760M, 0.05 at 1.3B (Table 2, Section 4). Tested across 4 model sizes on a single dataset (moderate evidence for the scaling trend).
- Smaller models benefit more from fixed, non-parametric positional encodings (Sinusoidal and ALiBi), but these performance gaps diminish at larger scales.

**Sequence length scaling (Table 3, the Pile, 1.3B model):**

| Method | 256 | 512 | 1024 | 2048 |
|---|---|---|---|---|
| NoPos | 14.98 | 13.82 | 13.10 | 12.87 |
| Learned | 14.94 | 13.77 | 13.05 | 12.72 |
| Sinusoidal | 14.84 | 13.66 | 12.93 | 12.62 |
| ALiBi | 14.65 | 13.37 | 12.51 | 12.06 |

- NoPos-vs-Learned gap remains consistently small across sequence lengths: 0.04 at 256, 0.05 at 512, 0.05 at 1024, 0.15 at 2048 (Table 3, Section 4). Tested at a single model size (limited evidence for length generalization).
- ALiBi's advantage over other methods increases with longer sequences (0.33 at 256, 0.81 at 2048 vs NoPos).

**Position probing (Figure 2, Section 5):**

- NoPos model starts with no positional information in the first layer (MAD on par with random baseline at ~340).
- Becomes position-aware within 4 layers (MAD drops below 100).
- By the middle layers (~layer 12), NoPos achieves MAD comparable to the Learned model (~15--20).
- NoPos contains more positional information than ALiBi in middle layers.
- All models shed positional information in the final layers (MAD rises), consistent with Voita et al. (2019).
- Evidence based on a single 1.3B model on a single dataset with a single probe architecture (limited evidence for the probing claim's generality).

**Probe prediction quality (Figure 3, Section 5):**

- Position predictions are more accurate at the beginning of the sequence.
- Accuracy degrades and confidence intervals widen for later positions (beyond position ~256).
- Single-example predictions closely track the diagonal (ground truth) for early positions.

**Segment-level analysis (Figure 4, Appendix A):**

- Splitting 1024-token sequences into 8 consecutive segments, the NoPos model shows similar or slightly worse loss compared to the baseline on all segments.
- Both models perform better on later segments (lower loss), and the gap between NoPos and the baseline is small and approximately constant across all segments.
- Note: the figure caption refers to "Learned" baseline but the legend labels the comparison line as "Sinusoidal" (Appendix A).

**Word order matters (Figure 5, Appendix B):**

- Shuffling the prefix tokens increases the average token-level loss from ~4 to ~10--11 (Figure 5).
- This demonstrates that the NoPos model actively uses positional information it acquires, not merely tolerating the absence of explicit encoding.
- Experiment conducted on the WikiText-103 NoPos model with 512-token sequences, 100 different inputs (limited evidence -- single model, single dataset).

**MLM failure (Table 4, Section 6):**

| MLM Method | Perplexity |
|---|---|
| NoPos | 147.18 |
| Learned | 4.06 |
| Sinusoidal | 4.07 |
| ALiBi | 4.00 |

- Removing positional encoding from masked LMs causes catastrophic failure (Table 4, Section 6).
- Position-aware MLMs converge to perplexity ~4; NoPos MLM reaches 147.18.
- This supports the conjecture that causal attention is the mechanism enabling implicit positional encoding.
- Tested on a single architecture (RoBERTa-large) with 128-token sequences (limited evidence -- single model, single sequence length).

### Concurrent Work

Scao et al. (2022) independently observed that NoPos models are competitive and further evaluated 27 downstream tasks: NoPos reached 41.23% average accuracy, compared to 41.72% for Learned and 43.70% for ALiBi (Section 4).

---

## Limitations and Failure Modes

The paper includes an explicit limitations section (Section 9):

1. **Scale limited to 1.3B parameters.** Although the gap narrows as model size increases, models tested are more than 100x smaller than the largest LLMs. The authors acknowledge that results at much larger scales "can be unexpected" (Section 9).

2. **NoPos is always slightly worse.** Despite small margins, NoPos consistently underperforms all position-aware methods on every setting tested (Tables 1--3). The authors note this "suggests that the inductive bias of positional encoding is indeed important" (Section 9).

3. **Reproducibility concerns at scale.** Training at 1.3B scale is resource-intensive. The authors release trained models to mitigate this (Section 9).

4. **The mechanism remains a conjecture.** The claim that the causal attention mask enables implicit positional encoding is stated as a hypothesis (Section 6). The MLM experiment provides supporting evidence (Table 4) but does not constitute a proof.

5. **[Inferred]** Probing accuracy degrades for later positions. The position probe becomes "fuzzier" for tokens beyond position ~256 (Figure 3, Section 5), suggesting that implicit positional encoding is less precise for later sequence positions. The authors do not discuss this as a limitation.

6. **[Inferred]** No evaluation beyond language modeling perplexity. The paper does not evaluate NoPos models on downstream tasks. Scao et al. (2022)'s concurrent results suggest competitive downstream performance but with a gap of ~2.5% average accuracy between NoPos and ALiBi (41.23% vs 43.70%, Section 4).

7. **[Inferred]** No variance estimates reported for the Pile experiments. All perplexity comparisons on the Pile are from single training runs, preventing assessment of whether small gaps (e.g., 0.05 at 1.3B) are statistically meaningful. The WikiText-103 seed variance context (up to 0.9 perplexity per Press et al., 2020) is noted but not replicated for the Pile setting.

#### Scope and Comparability

- **What was not tested:** Models larger than 1.3B parameters; non-English languages; downstream tasks (only perplexity evaluated); decoder-only architectures other than the GPT-3 family; sequence lengths beyond 2048; RoPE or other rotary positional encodings (not included as baselines).
- **Comparability notes:** The WikiText-103 setting uses a different model architecture (adaptive embedding transformer, 247M params, word-level tokenization) than the Pile setting (GPT-3 XL, 1.3B params, BPE tokenization), making direct cross-setting comparison of absolute perplexity values inappropriate. The MLM experiment uses a different architecture (RoBERTa-large), different sequence length (128 vs 1024), and different training hyperparameters than the causal LM experiments, limiting the strength of the causal-mask conjecture. ALiBi's sequence length advantage is well-documented by its authors, so its superior performance at longer sequences may not reflect on NoPos specifically.

---

## Conclusions

### Contributions

1. **Demonstrated robustness of NoPos language models.** Causal transformer LMs without any positional encoding achieve competitive perplexity across two datasets (WikiText-103, the Pile), four model sizes (125M--1.3B), and four sequence lengths (256--2048), with the gap to learned positional embeddings as small as 0.05 perplexity at 1.3B scale (Tables 1--3).

2. **Probing evidence of implicit absolute positions.** Probing classifiers reveal that NoPos models acquire absolute positional information within the first few layers, matching the probing accuracy of models with learned positional embeddings by the network's middle layers (Figure 2, Section 5).

3. **Identified causal masking as the key mechanism.** Masked language models without positional encoding fail to converge (perplexity 147.18 vs ~4 for position-aware MLMs), while causal LMs succeed, supporting the conjecture that the causal attention mask implicitly provides positional information (Table 4, Section 6).

4. **Public release of trained models.** All 1.3B parameter models (NoPos, Learned, Sinusoidal, ALiBi) are publicly released for future research at https://github.com/adihaviv/NoPos.

### Implications

1. **Positional encoding may be less critical than assumed for causal LMs.** The results challenge the common assumption that explicit positional encoding is essential for transformer language models, suggesting that the causal mask alone provides a sufficient positional signal. This has implications for architecture design and training pipelines.

2. **The gap between causal and bidirectional models may be partly architectural.** The asymmetry between causal LMs (where NoPos works) and MLMs (where it fails) highlights that the causal mask provides more than just an autoregressive constraint -- it also encodes structural information about token position.

3. **Potential for post-hoc PE removal.** The finding that PEs are not strictly necessary for causal LMs motivates exploring whether positional embeddings can be removed from pretrained models to improve context extension. This is speculative beyond the scope of this paper.

---

## Key Claims

1. **C1: NoPos causal LMs are competitive with position-aware models (supported).** On the Pile at 1.3B scale, NoPos achieves 13.10 perplexity vs 13.05 for Learned, a gap of 0.05 (Table 1). On WikiText-103 at 247M scale, the gap is 0.55 (20.97 vs 20.42). Performance differences between NoPos, Learned, and Sinusoidal are "small both in absolute terms and with respect to their difference with ALiBi" (Section 4). **Scope:** causal LMs, 247M and 1.3B scale, English only, word-level and BPE tokenization. **Magnitude:** 0.05--0.55 perplexity gap depending on setting. Tested on 2 datasets and 4 model sizes (strong evidence for the perplexity claim, though no variance estimates reported for Pile experiments).

2. **C2: Robustness across model sizes, datasets, and sequence lengths (supported).** The gap between NoPos and Learned narrows from 0.11 at 125M to 0.05 at 1.3B (Table 2). The gap remains consistently small (0.04--0.15) across sequence lengths 256--2048 (Table 3). Results hold on both WikiText-103 and the Pile (Table 1). **Scope:** 125M--1.3B parameters, 256--2048 token sequences, English only. **Magnitude:** NoPos-vs-Learned gap ranges 0.03--0.55 perplexity across all settings. Tested across 4 model sizes and 4 sequence lengths on 2 datasets (strong evidence for robustness within tested range; single run per configuration, no variance reported).

3. **C3: NoPos models learn implicit absolute positions (supported).** Position probes trained on frozen 1.3B models show that NoPos starts with no positional information in layer 0 (MAD ~340, on par with random baseline) but reaches MAD comparable to the Learned model by layer 12 (Figure 2). Shuffling the prefix increases token-level loss from ~4 to ~10--11, confirming the model uses this positional information (Figure 5, Appendix B). **Scope:** 1.3B model on the Pile, 1024-token sequences, 2-layer feed-forward probe. **Magnitude:** MAD drops from ~340 (random) to ~15--20 (comparable to Learned) by middle layers. Single model probed with a single probe architecture (limited evidence for generality of the mechanism).

4. **C4: NoPos fails for masked (bidirectional) language models (supported).** RoBERTa-large trained without positional encoding on the Pile achieves perplexity 147.18, compared to 4.06 for Learned, 4.07 for Sinusoidal, and 4.00 for ALiBi (Table 4). This establishes that the phenomenon is unique to causal LMs. Consistent with Sinha et al. (2021), who also observed MLM performance degradation without positional embeddings. **Scope:** RoBERTa-large architecture, 128-token sequences, single configuration. **Magnitude:** 147.18 vs 4.06 perplexity (36x degradation). Single architecture tested (limited evidence -- only RoBERTa-large, only 128-token sequences).

5. **C5: Causal attention mask encodes position via predecessor counting (unvalidated).** The conjecture is stated but not formally proven. The MLM failure (C4) provides circumstantial supporting evidence, but the specific mechanism (counting attendable predecessors) remains a hypothesis (Section 6). **Scope:** general conjecture for causal transformer LMs. **Magnitude:** qualitative. Marked unvalidated pending formal theoretical confirmation.

---

## Open Questions

1. **Does the competitiveness of NoPos models extend to scales much larger than 1.3B?** The narrowing gap between NoPos and Learned with increasing model size (Table 2) suggests yes, but the largest current models are 100x+ larger than 1.3B. The authors explicitly note this as a limitation (Section 9). Not directly addressed in the references directory.

2. **What is the precise mechanism by which causal attention encodes positional information?** The conjecture that models count attendable predecessors is intuitive but unproven. Wu et al. (2025) provide a graph-theoretic analysis showing that causal masking introduces directional bias toward earlier positions via iterative attention, offering a partial formal treatment. Addressed by `2025-07-position-bias-transformers`.

3. **Can NoPos models extrapolate to sequence lengths beyond training?** The paper does not test length generalization. Gelberg et al. (2025) show that removing positional embeddings from pretrained models enables zero-shot context extension to sequences far beyond training context. Addressed by `2025-12-drope-dropping-positional-embeddings`.

4. **Do NoPos models maintain competitive performance on downstream tasks?** Scao et al. (2022) show competitive but slightly lower accuracy (41.23% vs 41.72% for Learned on 27 tasks, Section 4), but this is from a concurrent work with a different model. Kazemnejad et al. (2023) systematically evaluate NoPE on downstream tasks and show it outperforms all explicit PEs on length generalization. Addressed by `2023-12-positional-encoding-length-generalization`.

---

## Core References and Why They Are Referenced

### Foundational Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the transformer architecture with sinusoidal positional encodings. NoPos directly removes the positional component while retaining the rest of the architecture.

### Positional Encoding Baselines

- **Gehring et al. (2017)** -- *Convolutional Sequence to Sequence Learning.* Introduces learned positional embeddings, used as a baseline and in GPT-3.
- **Press et al. (2022)** -- *Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation.* Introduces ALiBi, the strongest baseline in the paper. Also defines the WikiText-103 evaluation setting with 512-token sequences used in the canonical experiment.
- **Shaw et al. (2018)** -- *Self-Attention with Relative Position Representations.* Relative position representations for self-attention, part of the background on positional encoding methods.
- **Sukhbaatar et al. (2015)** -- *End-to-End Memory Networks.* Early use of learned positional embeddings, cited as a precursor to the Learned baseline.

### Training Data and Architectures

- **Merity et al. (2017)** -- *Pointer Sentinel Mixture Models.* Introduces the WikiText-103 corpus used in the canonical setting.
- **Gao et al. (2020)** -- *The Pile: An 800GB Dataset of Diverse Text for Language Modeling.* Provides the large-scale training corpus used for the 1.3B parameter experiments.
- **Brown et al. (2020)** -- *Language Models Are Few-Shot Learners.* Provides the GPT-3 model architecture specifications (125M--1.3B variants) used in the Pile experiments.
- **Baevski and Auli (2019)** -- *Adaptive Input Representations for Neural Language Modeling.* Provides the adaptive embedding transformer architecture used in the WikiText-103 setting.

### Masked Language Modeling Control

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* The MLM objective and bidirectional attention used to test whether NoPos works without causal masking. NoPos fails on MLM (Table 4).
- **Liu et al. (2019)** -- *RoBERTa: A Robustly Optimized BERT Pretraining Approach.* Provides the RoBERTa-large architecture used for the MLM control experiment.

### Prior Work on Implicit Positions

- **Irie et al. (2019)** -- *Language Modeling with Deep Transformers.* Prior observation that transformers without positional encoding can outperform sinusoidal models in speech recognition. Limited to a single domain.
- **Sinha et al. (2021)** -- *Masked Language Modeling and the Distributional Hypothesis.* Observed that MLMs without positional embeddings suffer significant performance degradation, consistent with Haviv et al.'s MLM failure result.

### Internal Representation Analysis

- **Voita et al. (2019)** -- *The Bottom-Up Evolution of Representations in the Transformer.* Finding that models shed positional information in final layers, consistent with the probing results in Figure 2.

### Concurrent Work

- **Scao et al. (2022)** -- *What Language Model to Train If You Have One Million GPU Hours?* Independently observes that NoPos models are competitive and shows competitive downstream task performance (41.23% vs 41.72% for Learned across 27 tasks).
