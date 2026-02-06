---
title: "Big Bird: Transformers for Longer Sequences"
authors: "Zaheer, Guruganesh, Dubey, Ainslie, Alberti, Ontanon, Pham, Ravula, Wang, Yang, Ahmed"
year: 2020
venue: "NeurIPS 2020"
paper_type: conference-paper
categories: ["attention-efficiency", "architecture"]
scope: ["encoder-only models", "BERT-style pretraining", "sequence length up to 4096"]
benchmarks_used: ["wikihop", "triviaqa", "hotpotqa", "natural-questions", "arxiv-summarization"]
models_introduced: ["bigbird-base", "bigbird-large", "bigbird-roberta", "bigbird-pegasus", "bigbird-etc"]
models_evaluated: ["bert-base", "roberta-base", "longformer-base"]
key_claims:
  - id: C1
    claim: "Sparse attention mechanisms satisfying certain properties can be universal approximators of sequence-to-sequence functions"
    evidence: "Theorem 1, Section 2"
    status: supported
    scope: "O(n) sparse patterns with global tokens"
  - id: C2
    claim: "Sparse encoders with global tokens are Turing complete"
    evidence: "Theorem 2, Section 2"
    status: supported
    scope: "Requires global tokens for completeness"
  - id: C3
    claim: "BigBird achieves state-of-the-art on question answering benchmarks requiring long context"
    evidence: "Table 1, Section 4.2"
    status: supported
    scope: "Natural Questions, HotpotQA, TriviaQA, WikiHop"
    magnitude: "1-5% F1 improvement over Longformer"
  - id: C4
    claim: "BigBird-Pegasus achieves state-of-the-art on long document summarization"
    evidence: "Table 2, Section 4.3"
    status: supported
    scope: "arXiv, PubMed, BigPatent datasets"
    magnitude: "1-4 ROUGE points improvement"
  - id: C5
    claim: "Random attention alone is insufficient for competitive performance"
    evidence: "Table 4, Ablation study Section 4.4"
    status: supported
    scope: "QA and MLM tasks"
  - id: C6
    claim: "Global tokens are essential for BigBird's performance"
    evidence: "Table 4, Section 4.4"
    status: supported
    scope: "Performance drops significantly without global tokens"
cross_references:
  - target: 2020-04-longformer-long-document-transformer
    type: concurrent
    detail: "Both propose sparse attention for long sequences; BigBird adds random attention and provides theoretical foundations"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "BigBird extends the Transformer architecture with sparse attention patterns"
  - target: 2024-05-mamba-selective-state-spaces
    type: complementary
    detail: "Mamba takes a fundamentally different approach to O(n) complexity: replacing attention entirely with selective state space models rather than sparse attention patterns, achieving 5× faster inference while matching Transformer quality on language modeling"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV replaces attention entirely with channel-wise linear recurrence rather than BigBird's sparse attention patterns, achieving O(d) memory and linear time at up to 14B parameters"
open_questions:
  - question: "How does BigBird scale to sequences beyond 4096 tokens?"
    addressed_by: null
  - question: "Can the theoretical universality results be extended to decoder-only models?"
    addressed_by: null
  - question: "What is the optimal ratio of random to local attention for different tasks?"
    addressed_by: null
---

# Big Bird: Transformers for Longer Sequences

**Authors:** Manzil Zaheer, Guru Guruganesh, Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, Amr Ahmed (Google Research)
**Date:** December 2020, NeurIPS 2020

---

## Core Research Problem

Transformer-based models like BERT achieve state-of-the-art results across NLP tasks but suffer from quadratic O(n²) complexity in the self-attention mechanism, where n is sequence length. This computational bottleneck limits practical context windows to 512 tokens, excluding applications requiring longer contexts such as document-level question answering, multi-document summarization, and genomics.

Prior work attempted to address this through:
1. **Sparse Transformers** (Child et al., 2019) -- Fixed sparse patterns but limited expressiveness analysis
2. **Longformer** (Beltagy et al., 2020) -- Sliding window attention with task-specific global tokens
3. **Linformer** (Wang et al., 2020) -- Low-rank approximations of attention matrices

However, these approaches lacked theoretical grounding for when sparse attention can match full attention's expressive power. **The core challenge: how to design sparse attention mechanisms that are provably expressive while maintaining linear O(n) complexity.**

---

## Problem Solutions

BigBird addresses the quadratic complexity problem through a **sparse attention mechanism** combining three components:

1. **Random attention** -- Each query attends to r random keys, capturing long-range dependencies
2. **Window attention** -- Each query attends to w/2 neighboring tokens on each side (local context)
3. **Global attention** -- g designated tokens attend to and are attended by all other tokens

The key insight is that this combination, with appropriate graph-theoretic properties, yields:
- **O(n) complexity** -- Total edges scale linearly with sequence length
- **Universal approximation** -- Can approximate any sequence-to-sequence function
- **Turing completeness** -- With global tokens, can simulate any Turing machine

---

## Approach Details

### Method

BigBird's attention pattern is defined as a directed graph where edges represent attention connections. For a sequence of length n, the attention matrix A is constructed as:

> A = A_random + A_window + A_global

Where:
- **A_random**: Each token attends to r randomly selected tokens
- **A_window**: Band matrix with bandwidth w (local sliding window)
- **A_global**: g tokens have full attention rows and columns

The total number of attention edges is O(n(r + w + g)) = O(n) when r, w, g are constants.

### Key Technical Components

**Graph-Theoretic Properties:**
The paper identifies two key properties for sparse attention graphs:
1. **Small average path length** -- Any two nodes reachable in O(log n) hops
2. **Notion of locality** -- Preserves sequential structure through window attention

**Internal Transformer Construction (ITC) vs Extended Transformer Construction (ETC):**
- **ITC**: Global tokens are existing tokens from the sequence (e.g., [CLS])
- **ETC**: Additional "extra" global tokens added to the sequence

**Attention Computation:**
Standard scaled dot-product attention is applied, but only over the sparse connections:

> Attention(Q, K, V) = softmax(QK^T / √d_k) · V

The sparsity pattern is applied via masking or block-sparse operations.

### Theoretical Analysis

**Theorem 1 (Universal Approximation):** BigBird sparse attention mechanisms are universal approximators of continuous sequence-to-sequence functions with compact support.

The proof relies on showing that sparse attention with O(n) random edges can simulate the effects of full attention through information propagation over multiple layers, using the graph's small-world properties.

**Theorem 2 (Turing Completeness):** The sparse encoder of BigBird with global tokens is Turing complete.

This extends prior work showing full attention Transformers are Turing complete (Pérez et al., 2019) to the sparse case. The global tokens are essential -- they provide a "communication bus" for information to flow between distant positions.

**Corollary:** Without global tokens (random + window only), the model loses Turing completeness, explaining the empirical importance of global attention.

### Experimental Setup

**Models:**
- **BigBird-RoBERTa**: Pretrained from RoBERTa checkpoint, then continued pretraining with 4096-length sequences
- **BigBird-PEGASUS**: Encoder-decoder model for summarization based on PEGASUS
- **BigBird-ETC**: Extended Transformer Construction variant

**Pretraining:**
- Continued pretraining from RoBERTa-base/large checkpoints
- Maximum sequence length: 4096 tokens
- Block size: 64 tokens
- Number of random blocks: 3
- Number of global tokens: 2 × block_size (ITC) or task-specific (ETC)
- Window size: 3 blocks on each side

**Evaluation Benchmarks:**
1. **Question Answering:** Natural Questions, HotpotQA, TriviaQA, WikiHop
2. **Document Summarization:** arXiv, PubMed, BigPatent
3. **Classification:** IMDB (long document classification)
4. **Genomics:** Promoter region prediction, chromatin profiling

**Reproducibility:** Code released at github.com/google-research/bigbird. Pretraining details provided but exact random seeds not reported.

### Key Results

**Question Answering (Table 1):**

| Model | Natural Questions (F1) | HotpotQA (F1) | TriviaQA (F1) | WikiHop (Acc) |
|-------|------------------------|---------------|---------------|---------------|
| BERT-base (512) | 50.3 | 58.3 | 65.3 | 66.2 |
| Longformer-base | 52.3 | 63.1 | 68.8 | 69.2 |
| BigBird-base (ITC) | 54.2 | 64.4 | 70.1 | 70.8 |
| BigBird-base (ETC) | **57.2** | **67.0** | **71.3** | **72.1** |

- BigBird-ETC outperforms Longformer by 2-5% F1 across all QA benchmarks
- The ETC variant consistently outperforms ITC, suggesting value of additional global tokens

**Document Summarization (Table 2):**

| Model | arXiv (R-1/R-2/R-L) | PubMed (R-1/R-2/R-L) | BigPatent (R-1/R-2/R-L) |
|-------|---------------------|----------------------|-------------------------|
| PEGASUS | 44.21/16.95/38.83 | 45.97/20.15/41.34 | 53.63/33.16/42.25 |
| BigBird-PEGASUS | **46.63/19.02/41.77** | **46.32/20.65/42.33** | **60.64/42.46/50.01** |

- Consistent improvements of 1-7 ROUGE points across summarization datasets
- Largest gains on BigPatent (long patents benefit most from extended context)

**Ablation Study (Table 4):**

| Attention Pattern | Natural Questions (F1) | MLM Loss |
|-------------------|------------------------|----------|
| Full attention (baseline) | 57.9 | 1.51 |
| Random only | 35.2 | 2.89 |
| Window only | 51.3 | 1.78 |
| Random + Window | 52.8 | 1.69 |
| Window + Global | 55.1 | 1.58 |
| Random + Window + Global (BigBird) | **57.2** | **1.53** |

- Random attention alone is insufficient (35.2 F1)
- Each component contributes: window provides local coherence, random enables long-range, global enables information aggregation
- Full BigBird nearly matches full attention (57.2 vs 57.9) at O(n) cost

**Genomics Results:**
- Promoter region prediction: 2-3% accuracy improvement over BERT-base
- Enables processing of 4096bp sequences vs 512bp limit of standard BERT

---

## Limitations and Failure Modes

**Acknowledged Limitations:**
1. **Fixed sparse pattern** -- The random attention pattern is fixed after sampling; dynamic patterns could potentially be more effective
2. **Block-based implementation** -- Requires sequence length divisible by block size; padding overhead for variable-length inputs
3. **Pretraining cost** -- Still requires continued pretraining to adapt from 512 to 4096 tokens

**Observed Failure Modes:**
- Without global tokens, performance degrades significantly (Table 4: 52.8 → 57.2 F1 with global)
- Random-only attention achieves only 35.2 F1 on Natural Questions, far below even window-only (51.3)

**Scope and Comparability:**
- **Encoder-only focus:** All theoretical results and most experiments are encoder-only; decoder application less explored
- **Limited scale:** Experiments primarily on base/large models (~110M-330M parameters); scaling behavior to larger models not studied
- **Context ceiling:** While extending to 4096 tokens, behavior beyond this length not evaluated
- **Comparison baseline:** Longformer comparison uses base model only; large-scale comparison limited

---

## Conclusions

### Contributions

1. **Theoretical foundations for sparse attention.** First proof that sparse attention with global tokens is Turing complete and can universally approximate sequence-to-sequence functions, providing principled justification for sparse attention designs.

2. **Three-component sparse attention pattern.** Combination of random, window, and global attention achieves O(n) complexity while maintaining expressiveness, with each component serving a distinct functional role.

3. **State-of-the-art on long-context benchmarks.** BigBird achieves best results on question answering (NQ, HotpotQA, TriviaQA, WikiHop) and summarization (arXiv, PubMed, BigPatent) tasks requiring extended context.

4. **Novel genomics applications.** Demonstrates Transformer applicability to DNA sequence modeling with 4096bp context, opening new research directions.

### Implications

1. **Global tokens are theoretically necessary.** The Turing completeness proof shows global tokens are not merely a performance enhancement but required for full computational expressiveness -- suggesting all efficient Transformers should include some form of global attention.

2. **Random attention aids generalization.** While individually weak, random connections enable information flow patterns that fixed sparse patterns cannot achieve, suggesting value in stochastic architectural components.

3. **Sparse attention as a general approach.** Success across diverse domains (NLP, genomics) suggests sparse attention is broadly applicable wherever quadratic complexity is the bottleneck.

---

## Key Claims

**C1: Sparse attention can be a universal approximator**
- *Claim:* BigBird's sparse attention mechanism can approximate any continuous sequence-to-sequence function
- *Evidence:* Theorem 1, Section 2; proof via graph-theoretic analysis of information propagation
- *Status:* Supported (mathematical proof)
- *Scope:* Requires O(n) random edges and appropriate graph properties

**C2: Sparse attention with global tokens is Turing complete**
- *Claim:* The sparse encoder satisfies Turing completeness when global tokens are included
- *Evidence:* Theorem 2, Section 2; extends Pérez et al. (2019) to sparse case
- *Status:* Supported (mathematical proof)
- *Scope:* Global tokens essential; random + window alone insufficient

**C3: BigBird outperforms Longformer on QA tasks**
- *Claim:* BigBird-ETC achieves higher F1 than Longformer on all tested QA benchmarks
- *Evidence:* Table 1, Section 4.2
- *Status:* Supported
- *Scope:* Base model comparison; Natural Questions, HotpotQA, TriviaQA, WikiHop
- *Magnitude:* 2-5% F1 improvement

**C4: BigBird-PEGASUS advances summarization state-of-the-art**
- *Claim:* Achieves best ROUGE scores on long document summarization benchmarks
- *Evidence:* Table 2, Section 4.3
- *Status:* Supported
- *Scope:* arXiv, PubMed, BigPatent datasets
- *Magnitude:* 1-7 ROUGE points improvement over PEGASUS

**C5: All three attention components are necessary**
- *Claim:* Removing any of random, window, or global attention degrades performance
- *Evidence:* Table 4, Section 4.4 ablation
- *Status:* Supported
- *Scope:* Tested on QA and MLM objectives

**C6: Near-parity with full attention at linear cost**
- *Claim:* BigBird achieves 98-99% of full attention performance with O(n) complexity
- *Evidence:* Table 4: 57.2 F1 (BigBird) vs 57.9 F1 (full attention) on NQ
- *Status:* Supported
- *Scope:* 4096 sequence length; Natural Questions benchmark

---

## Open Questions

1. **Scaling beyond 4096 tokens:** How does BigBird's performance-efficiency tradeoff evolve at 8K, 16K, or longer contexts? The theoretical results suggest scalability, but empirical validation is absent.

2. **Optimal sparsity ratios:** What is the optimal balance between random, window, and global attention for different task types? The paper uses fixed hyperparameters across tasks.

3. **Decoder-only extension:** Can the theoretical results (Turing completeness, universal approximation) be extended to autoregressive decoder-only models? The proofs focus on encoders.

4. **Dynamic sparse patterns:** Would learned or input-dependent sparse patterns outperform fixed random patterns? The paper uses static patterns sampled once.

5. **Interaction with other efficiency methods:** How does BigBird combine with quantization, pruning, or knowledge distillation for further efficiency gains?

---

## Core References and Why They Are Referenced

### Theoretical Foundations

- **Pérez et al. (2019)** -- *On the Turing Completeness of Modern Neural Network Architectures.* Proved full-attention Transformers are Turing complete; BigBird extends this to sparse attention.

- **Yun et al. (2020)** -- *Are Transformers universal approximators of sequence-to-sequence functions?* Showed full Transformers are universal approximators; BigBird proves same for sparse case.

### Sparse Attention Predecessors

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Introduced fixed sparse patterns (strided + local); BigBird adds random attention and theoretical analysis.

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Concurrent work with sliding window + global attention; BigBird adds random attention and provides theoretical foundations.

### Base Models

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers.* Base architecture BigBird extends for longer sequences.

- **Liu et al. (2019)** -- *RoBERTa: A Robustly Optimized BERT Pretraining Approach.* Checkpoint used for BigBird-RoBERTa initialization.

- **Zhang et al. (2020)** -- *PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization.* Base model for BigBird-PEGASUS summarization experiments.

### Graph Theory

- **Watts & Strogatz (1998)** -- *Collective dynamics of 'small-world' networks.* Small-world network properties that inform BigBird's sparse attention design.

### Evaluation Benchmarks

- **Kwiatkowski et al. (2019)** -- *Natural Questions: A Benchmark for Question Answering Research.* Primary QA benchmark for evaluation.

- **Yang et al. (2018)** -- *HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering.* Multi-hop reasoning benchmark.

- **Cohan et al. (2018)** -- *A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents.* arXiv and PubMed summarization datasets.
