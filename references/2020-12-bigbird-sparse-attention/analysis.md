---
title: "Big Bird: Transformers for Longer Sequences"
authors: "Zaheer, Guruganesh, Dubey, Ainslie, Alberti, Ontanon, Pham, Ravula, Wang, Yang, Ahmed"
year: 2020
venue: "NeurIPS 2020"
paper_type: conference-paper
categories: ["attention-efficiency", "architecture"]
scope: ["encoder-only and encoder-decoder models", "BERT/RoBERTa/PEGASUS-based pretraining", "sequence length up to 4096 tokens"]
benchmarks_used: ["natural-questions", "hotpotqa", "triviaqa", "wikihop", "arxiv-summarization", "imdb-sentiment", "hyperpartisan", "glue", "squad"]
models_introduced: ["bigbird-base", "bigbird-large", "bigbird-roberta", "bigbird-pegasus", "bigbird-etc"]
models_evaluated: ["bert-base", "roberta-base", "longformer-base"]
key_claims:
  - id: C1
    claim: "Sparse attention mechanisms satisfying certain graph properties (containing a star graph) are universal approximators of continuous sequence-to-sequence functions"
    evidence: "Theorem 1, Section 3.2, Appendix A"
    status: supported
    scope: "Requires O(n) sparse attention pattern containing a star graph (global token connected to all others)"
    magnitude: "qualitative -- existence proof, d_p(f, g) <= epsilon for any epsilon > 0"
  - id: C2
    claim: "Sparse encoder-decoder transformers with global tokens are Turing complete"
    evidence: "Theorem 3, Section 3.3, Appendix B"
    status: supported
    scope: "Requires global tokens and arbitrary precision (same assumption as Perez et al. 2019)"
    magnitude: "qualitative -- constructive proof via simulation of arbitrary Turing machine"
  - id: C3
    claim: "Sparse attention mechanisms necessarily incur a cost: some tasks solvable in O(1) layers by full attention require Omega(n) layers for any sparse mechanism"
    evidence: "Proposition 1/2, Section 3.4, Appendix C"
    status: supported
    scope: "Tasks reducible to minimum inner product search on unit vectors, under OVC assumption, d = Theta(log^2 n)"
    magnitude: "Omega_tilde(n^{1-o(1)}) layers required vs O(1) for full attention"
  - id: C4
    claim: "BigBird-ETC achieves state-of-the-art on Natural Questions LA, TriviaQA, and WikiHop, and is competitive on HotpotQA"
    evidence: "Table 3, Section 4"
    status: supported
    scope: "Large ETC model, 4096 tokens, test set leaderboard results"
    magnitude: "NQ LA 77.8 F1, TriviaQA Full 84.5/Verified 92.4 F1, WikiHop 82.3 Acc; HotpotQA Joint 73.6 (3rd on leaderboard)"
  - id: C5
    claim: "BigBird-Pegasus achieves state-of-the-art on long document summarization"
    evidence: "Table 4, Section 4.1"
    status: supported
    scope: "Large model warm-started from Pegasus, arXiv/PubMed/BigPatent datasets"
    magnitude: "arXiv R-1/R-2/R-L 46.63/19.02/41.77; PubMed 46.32/20.65/42.33; BigPatent 60.64/42.46/50.01 (2-8 ROUGE points over Pegasus)"
  - id: C6
    claim: "Random and window attention alone are insufficient; global tokens are critical for competitive performance"
    evidence: "Table 1, Section 2 (p. 4)"
    status: supported
    scope: "Base model, 512-token evaluation on MLM/SQuAD/MNLI"
    magnitude: "R+W achieves 62.7/85.1/80.5 vs BERT-base 64.2/88.5/83.4 on MLM/SQuAD/MNLI"
  - id: C7
    claim: "BigBird achieves near-perfect accuracy on promoter region prediction"
    evidence: "Table 6, Section 5"
    status: supported
    scope: "Base model with MLM+NSP pretraining on human reference genome, EPDnew dataset"
    magnitude: "99.9 F1 vs previous best DeePromoter 95.6 F1 (~4.3 point improvement)"
  - id: C8
    claim: "BigBird improves document classification when documents are long and training data is limited"
    evidence: "Table 15, Appendix E.4"
    status: supported
    scope: "Base and large models, 4096 tokens, classification on IMDb/Yelp-5/Arxiv/Patents/Hyperpartisan"
    magnitude: "Arxiv +5 points over SoTA (92.31 vs 87.96); Hyperpartisan 92.2 vs SoTA 90.6; smaller gains on shorter/larger datasets"
cross_references:
  - target: 2020-04-longformer-long-document-transformer
    type: concurrent
    detail: "Both propose sparse attention for long sequences; BigBird adds random attention and provides theoretical foundations (universal approximation, Turing completeness). Key differences: BigBird-ETC uses learned global tokens with CPC loss and relative position encodings."
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "BigBird extends the Transformer architecture by replacing full quadratic self-attention with a sparse O(n) attention pattern combining random, window, and global components."
  - target: 2024-05-mamba-selective-state-spaces
    type: complementary
    detail: "Mamba takes a fundamentally different approach to O(n) complexity: replacing attention entirely with selective state space models rather than sparsifying the attention pattern."
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV replaces attention entirely with channel-wise linear recurrence rather than BigBird's sparse attention patterns, achieving O(d) memory and linear time."
open_questions:
  - question: "How does BigBird scale to sequences significantly beyond 4096 tokens?"
    addressed_by: null
  - question: "Can the theoretical universality and Turing completeness results be extended to decoder-only autoregressive models?"
    addressed_by: null
  - question: "What is the optimal ratio of random to local to global attention for different task types?"
    addressed_by: null
  - question: "Would learned or input-dependent sparse patterns outperform fixed random patterns?"
    addressed_by: null
  - question: "How does BigBird combine with quantization, pruning, or knowledge distillation for further efficiency gains?"
    addressed_by: null
---

# Big Bird: Transformers for Longer Sequences

**Authors:** Manzil Zaheer, Guru Guruganesh, Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, Amr Ahmed (Google Research)
**Date:** December 2020, NeurIPS 2020 (Vancouver, Canada), pp. 17283--17297; arXiv:2007.14062

---

## Core Research Problem

Transformer-based models such as BERT achieve state-of-the-art results across NLP tasks, but their full self-attention mechanism has computational and memory requirements that are **quadratic in sequence length**. On commonly available hardware and model sizes, this translates to a practical input limit of roughly 512 tokens (Section 1, p. 1-2), excluding tasks requiring longer context such as document-level question answering, multi-document summarization, and genomics sequence modeling.

Prior work attempted to address this bottleneck through two directions:

1. **Context selection:** SpanBERT, ORQA, REALM, RAG -- select relevant subsets of context to feed into a standard Transformer. These require significant engineering (e.g., backprop through nearest neighbor search) and are hard to train (Section 1.1, p. 2).
2. **Reducing attention complexity:** Child et al. (2019) proposed sparse patterns at O(n sqrt(n)); Kitaev et al. (2019) used LSH for O(n log n); Longformer introduced sliding window + global tokens; ETC used global tokens extensively (Section 1.1, p. 2-3). However, most of these methods are heuristic-based and "do not come with theoretical guarantees" (p. 3).

Two fundamental questions remained open: (1) can sparse attention achieve the empirical benefits of full attention using fewer inner products? (2) do sparse attention mechanisms preserve the expressivity (universal approximation, Turing completeness) of the original network? **The core challenge: how to design a sparse attention mechanism that is provably expressive while maintaining O(n) complexity.**

---

## Problem Solutions

BigBird addresses both the theoretical and practical challenges through a **sparse attention mechanism** combining three components inspired by graph theory:

1. **Random attention** -- Each query attends to r randomly selected keys, producing a random graph with Theta(n) edges where any two nodes are reachable in O(log n) hops, enabling rapid information flow (Section 2, p. 3).
2. **Window (local) attention** -- Each query attends to w/2 neighboring tokens on each side, preserving locality of reference (high clustering coefficient), inspired by the Watts-Strogatz small-world model (Section 2, p. 4).
3. **Global attention** -- g designated tokens attend to and are attended by all other tokens, providing a "communication bus" that is theoretically necessary for Turing completeness (Section 2, p. 4).

The key insight is that this combination yields **O(n) complexity** (total edges = O(n(r + w + g)) where r, w, g are constants) while provably preserving **universal approximation** and **Turing completeness** of full attention. The paper also proves a complementary negative result: some tasks solvable in O(1) layers by full attention necessarily require Omega(n) layers under any sparse mechanism.

---

## Approach Details

### Method

BigBird's attention is defined via a **generalized attention mechanism** parameterized by a directed graph D on vertices {1, ..., n}. For query token i, only its out-neighbors N(i) in D participate in attention:

> ATTN_D(X)_i = x_i + sum_{h=1}^{H} sigma( Q_h(x_i) K_h(X_{N(i)})^T ) . V_h(X_{N(i)})

where Q_h, K_h : R^d -> R^m are query and key functions, V_h : R^d -> R^d is the value function, sigma is a scoring function (softmax or hardmax), and H is the number of heads (Equation AT, Section 2, p. 3). The adjacency matrix A in {0,1}^{n x n} encodes which query-key pairs are computed. When A is the complete graph, this recovers the full quadratic attention of Vaswani et al. (2017).

The BigBird attention matrix is the union of three components:

> A = A_random + A_window + A_global

- **A_random**: Each token attends to r randomly chosen keys
- **A_window**: Band matrix where query i attends to keys i - w/2 through i + w/2
- **A_global**: g tokens have full attention rows and columns

Two constructions for global tokens:

- **BigBird-ITC (Internal Transformer Construction):** Existing tokens (e.g., [CLS]) are made global -- A(i, :) = 1 and A(:, i) = 1 for i in G (Section 2, p. 4).
- **BigBird-ETC (Extended Transformer Construction):** Additional global tokens are appended to the sequence, creating a new matrix B in {0,1}^{(n+g) x (n+g)}. This adds extra storage for context and generally improves performance (Section 2, p. 4).

### Key Technical Components

**Block-Sparse Implementation (Appendix D):**
To achieve efficiency on GPU/TPU hardware (which require coalesced memory operations), BigBird "blockifies" the attention pattern rather than computing sporadic lookups. The query and key matrices Q, K in R^{n x d} are blocked along the sequence length to obtain ceil(n/b) x b x d tensors. Window attention is computed by making w copies of the blocked key tensor and rolling each copy along the block axis (Figure 5, p. 32). The result is a compact dense tensor K'' of size ceil(n/b) x (g + w + r)b x d, enabling efficient dense tensor multiplication at cost O(n(g + w + r)bd) (Equation 13, p. 32).

**Hyperparameters (Table 8, Appendix E.1):**

| Parameter | BIGBIRD-ITC (base) | BIGBIRD-ETC (base) |
|---|---|---|
| Block length, b | 64 | 84 |
| # global tokens, g | 2 x b = 128 | 256 |
| Window length, w | 3 x b = 192 | 3 x b = 252 |
| # random tokens, r | 3 x b = 192 | 0 |
| Max sequence length | 4096 | 4096 |
| Hidden size / heads / layers | 768 / 12 / 12 | 768 / 12 / 12 |
| Compute resources | 8 x 8 TPUv3 | 8 x 8 TPUv3 |

Note: ETC uses 0 random tokens, relying instead on its richer global token structure with relative position encodings and CPC loss regularization (Appendix E.3, p. 35).

### Theoretical Analysis

**Theorem 1 (Universal Approximation, Section 3.2):** For 1 < p < infinity and epsilon > 0, for any continuous function f in F_{CD}, there exists a sparse-attention Transformer g in T_D^{H,m,q} such that d_p(f, g) <= epsilon, where D is any graph containing the star graph S.

The star graph S is defined on {0, ..., n} with N(i) = {0, i} for i in {1, ..., n} and N(0) = {1, ..., n} -- i.e., a single global token connected to all others (Definition 1, p. 5). The proof proceeds in three steps: (1) approximate f by a piece-wise constant function on a grid of granularity delta; (2) compute a **contextual mapping** -- a unique encoding of each (X, x_i) pair -- using only sparse attention plus the global token, via a novel "selective shift operator" (Lemma 2, Appendix A); (3) approximate the modified transformer by one with ReLU and softmax (Lemma 5, Appendix A). The key technical novelty is Step 2: the global token acts as a relay, aggregating information from all columns in n interleaved phases of "low shift" and "high shift" operations (Lemma 3, Appendix A, p. 19-20).

**Theorem 3 (Turing Completeness, Section 3.3, Appendix B):** There exists a sparse attention mechanism using O(n) inner products such that the resulting class of Transformer Networks is Turing complete.

The proof extends Perez et al. (2019) to sparse attention. The main challenge is that Perez et al.'s addressing scheme (Lemma B.4) uses full attention to retrieve tape symbols in one step. BigBird decomposes this via the **associativity of max**: instead of computing the minimum over all past steps at once, it distributes the computation across O(sqrt(j)) intermediate decoder steps for Turing machine step j, using the specific sparse graph where step j(j+1)/2 + k attends to step k(k+1)/2 (Figure 2, p. 23). The construction requires a 4-layer decoder with an additional layer (Layer 3) not present in Perez et al.'s proof, which distinguishes "compute steps" from "intermediate steps" using a flipping bit h(i) (Appendix B.2.3, p. 25-26).

**Proposition 2 (No Free Lunch, Section 3.4, Appendix C):** For the task of finding the furthest vector for each vector in a sequence (Task 1), a single-layer full attention network suffices, but any sparse attention with O_tilde(n) edges requires Omega_tilde(n^{1-o(1)}) layers, under the Orthogonal Vector Conjecture (OVC). The proof constructs an explicit full-attention solution using Q([a;b]) = -a, K([a;b]) = a, V([a;b]) = [0;a] (Equations 9-11, Appendix C, p. 28), and shows that a fast sparse solution would violate OVC.

### Experimental Setup

**Pretraining:**
- Warm-started from public RoBERTa checkpoint (base: 12 layers, 768 hidden, 12 heads; large: 24 layers, 1024 hidden, 16 heads)
- Pretrained on four datasets: Books (1.0B tokens), CC-News (7.4B), Stories (7.7B), Wikipedia (3.1B) (Table 9, p. 33)
- MLM objective with 15% token masking, sequence length 4096
- Learning rate 10^{-4} with warmup over first 10K steps and linear decay
- Batch size 256 (base), 2048 (large)

**Evaluation Tasks:**
1. **Question Answering (4 tasks):** Natural Questions, HotpotQA-distractor, TriviaQA-wiki, WikiHop -- all using 4096-token input with task-specific output heads (Table 11 for dataset statistics, Tables 12-13 for hyperparameters, Appendix E.2)
2. **Document Summarization (3 long + 2 short):** arXiv, PubMed, BigPatent (long); BBC XSum, CNN/DailyMail (short) -- sparse encoder with full attention decoder, warm-started from Pegasus for large models (Table 17-18, Appendix E.5)
3. **Classification (5 tasks):** IMDb, Yelp-5, Arxiv topics, Patents, Hyperpartisan -- single layer + cross-entropy on [CLS] token (Table 14, Appendix E.4)
4. **GLUE (8 tasks):** MNLI, QQP, QNLI, SST-2, CoLA, STS-B, MRPC, RTE -- competitive with full attention (Table 16, Appendix E.4)
5. **Genomics (2 tasks):** Promoter region prediction (EPDnew dataset), chromatin-profile prediction (919 profiles from DeepSea/ENCODE) -- pretrained on human reference genome GRCh37 with BPE tokenization averaging 8.78 bp per token (Tables 5-7, Section 5; Table 21, Appendix F)

**Reproducibility:** Code released at github.com/google-research/bigbird. Pretraining hyperparameters fully specified. Exact random seeds not reported. Classification on smaller datasets (IMDb, Hyperpartisan) repeated 5 times with standard deviations reported (Table 15).

### Key Results

**Building Block Comparison at 512 tokens (Table 1, p. 4):**

This initial sanity check demonstrates that random + window attention is insufficient without global tokens:

| Model | MLM | SQuAD | MNLI |
|---|---|---|---|
| BERT-base | 64.2 | 88.5 | 83.4 |
| Random (R) | 60.1 | 83.0 | 80.2 |
| Window (W) | 58.3 | 76.4 | 73.1 |
| R + W | 62.7 | 85.1 | 80.5 |

- R + W still falls short of BERT-base on all three metrics, motivating the addition of global tokens (p. 4).

**Question Answering -- Dev Results, Base Models (Table 2, p. 7):**

| Model | HotpotQA Ans | HotpotQA Sup | HotpotQA Joint | NaturalQ LA | NaturalQ SA | TriviaQA Full | WikiHop MCQ |
|---|---|---|---|---|---|---|---|
| RoBERTa | 73.5 | 83.4 | 63.5 | - | - | 74.3 | 72.4 |
| Longformer | 74.3 | 84.4 | 64.4 | - | - | 75.2 | 75.0 |
| BIGBIRD-ITC | **75.7** | 86.8 | 67.7 | 70.8 | 53.3 | **79.5** | **75.9** |
| BIGBIRD-ETC | 75.5 | **87.1** | **67.8** | **73.9** | **54.9** | 78.7 | **75.9** |

- BIGBIRD-ETC consistently outperforms Longformer across all QA tasks at the base model level (4 tasks, single configuration per task -- moderate evidence).
- ETC variant slightly outperforms ITC on most metrics, supporting the value of structured global tokens.

**Question Answering -- Test Results, Large Models (Table 3, p. 7):**

| Model | HotpotQA Ans | HotpotQA Sup | HotpotQA Joint | NaturalQ LA | NaturalQ SA | TriviaQA Full | TriviaQA Verified | WikiHop MCQ |
|---|---|---|---|---|---|---|---|---|
| HGN | **82.2** | 88.5 | **74.2** | - | - | - | - | - |
| ReflectionNet | - | - | - | 77.1 | **64.1** | - | - | - |
| Fusion-in-Decoder | - | - | - | - | - | 84.4 | 90.3 | - |
| MRC-GCN | - | - | - | - | - | - | - | 78.3 |
| Longformer | 81.2 | 88.3 | 73.2 | - | - | 77.3 | 85.3 | 81.9 |
| BIGBIRD-ETC | 81.2 | **89.1** | 73.6 | **77.8** | 57.9 | **84.5** | **92.4** | **82.3** |

As stated by the authors: "For **Natural Questions Long Answer (LA), TriviaQA, and WikiHop, BIGBIRD-ETC is the new state-of-the-art**. On HotpotQA we are third in the leaderboard by F1 and second by Exact Match" (p. 7). Test results from respective leaderboards -- strong evidence for multi-task SoTA claims, though each task evaluated on a single large model configuration.

**Long Document Summarization (Table 4, p. 8):**

| | Model | arXiv R-1 | arXiv R-2 | arXiv R-L | PubMed R-1 | PubMed R-2 | PubMed R-L | BigPatent R-1 | BigPatent R-2 | BigPatent R-L |
|---|---|---|---|---|---|---|---|---|---|---|
| Base | Transformer | 28.52 | 6.70 | 25.58 | 31.71 | 8.32 | 29.42 | 39.66 | 20.94 | 31.20 |
| Base | + RoBERTa | 31.98 | 8.13 | 29.53 | 35.77 | 13.85 | 33.32 | 41.11 | 22.10 | 32.58 |
| Base | + Pegasus | 34.81 | 10.16 | 30.14 | 39.98 | 15.15 | 35.89 | 43.55 | 20.43 | 31.80 |
| Base | BIGBIRD-RoBERTa | 41.22 | 16.43 | **36.96** | 43.70 | 19.32 | **39.99** | **55.69** | **37.27** | **45.56** |
| Large | Pegasus (Reported) | 44.21 | 16.95 | 38.83 | 45.97 | 20.15 | 41.34 | 52.29 | 33.08 | 41.75 |
| Large | Pegasus (Re-eval) | 43.85 | 16.83 | 39.17 | 44.53 | 19.30 | 40.70 | 52.25 | 33.04 | 41.80 |
| Large | BIGBIRD-Pegasus | **46.63** | **19.02** | **41.77** | **46.32** | **20.65** | **42.33** | **60.64** | **42.46** | **50.01** |

- BIGBIRD-Pegasus improves over Pegasus (Reported) by 2.42/2.07/2.94 on arXiv, 0.35/0.50/0.99 on PubMed, and 8.35/9.38/8.26 on BigPatent.
- Largest gains on BigPatent, where salient content is evenly distributed throughout long documents (3 datasets, base + large models -- moderate evidence).

**Shorter Summarization (Table 20, p. 38):**

| Model | BBC XSum R-1 | BBC XSum R-2 | BBC XSum R-L | CNN/DM R-1 | CNN/DM R-2 | CNN/DM R-L |
|---|---|---|---|---|---|---|
| Pegasus (Re-eval, Large) | **47.37** | **24.31** | **39.23** | **44.15** | **21.56** | **41.05** |
| BIGBIRD-Pegasus (Large) | 47.12 | 24.05 | 38.80 | 43.84 | 21.11 | 40.74 |

- On shorter documents where full attention is feasible, BigBird's sparse attention performs comparably but does not exceed Pegasus, confirming sparse attention does not degrade performance on shorter contexts.

**Document Classification (Table 15, p. 36):**

| Model | IMDb | Yelp-5 | Arxiv | Patents | Hyperpartisan |
|---|---|---|---|---|---|
| SoTA (prior) | 97.4 | 73.28 | 87.96 | 69.01 | 90.6 |
| RoBERTa (512) | 95.0 +/- 0.2 | 71.75 | 87.42 | 67.07 | 87.8 +/- 0.8 |
| BIGBIRD (4096) | 95.2 +/- 0.2 | 72.16 | **92.31** | 69.30 | **92.2 +/- 1.7** |

- Gains are most significant where documents are long and training data is limited: Arxiv (100% excess fraction over 512 tokens, 30K examples) improves by ~5 points over SoTA; Hyperpartisan (53% excess, 645 examples) improves by 1.6 points (5 datasets with varying document lengths -- moderate evidence for the length-benefit hypothesis).
- On short-document IMDb (14% excess fraction), gains are minimal (single run on base model per dataset except IMDb/Hyperpartisan with 5 repeats).

**GLUE Results (Table 16, p. 36):**

| System | MNLI-(m/mm) | QQP | QNLI | SST-2 | CoLA | STS-B | MRPC | RTE |
|---|---|---|---|---|---|---|---|---|
| RoBERTa | 87.6/- | 91.9 | 92.8 | 94.8 | 63.6 | 91.2 | 90.2 | 78.7 |
| BIGBIRD | 87.5/87.3 | 88.6 | 92.2 | 94.6 | 58.5 | 87.8 | 91.5 | 75.0 |

- Competitive with RoBERTa on GLUE (which has short contexts), though slightly lower on some tasks (CoLA, STS-B, RTE). This shows sparse attention does not severely degrade short-context performance, but does not match full attention exactly (8 tasks, base model, dev set only -- moderate evidence).

**MLM Pretraining (Table 10, p. 33):**

| Model | Base BPC | Large BPC |
|---|---|---|
| RoBERTa (sqln: 512) | 1.846 | 1.496 |
| Longformer (sqln: 4096) | 1.705 | 1.358 |
| BIGBIRD-ITC (sqln: 4096) | 1.678 | 1.456 |
| BIGBIRD-ETC (sqln: 4096) | **1.611** | **1.274** |

- Longer context improves MLM prediction: both BigBird variants outperform RoBERTa at 512, and BIGBIRD-ETC outperforms Longformer at 4096. The ETC variant is the best at both scales.

**Genomics -- MLM Pretraining (Table 5, p. 9):**

| Model | BPC |
|---|---|
| SRILM | 1.57 |
| BERT (sqln. 512) | 1.23 |
| BIGBIRD (sqln. 4096) | **1.12** |

**Genomics -- Promoter Region Prediction (Table 6, p. 9):**

| Model | F1 |
|---|---|
| CNNProm | 69.7 |
| DeePromoter | 95.6 |
| BIGBIRD | **99.9** |

- Nearly perfect F1 (~4.3 points over previous best DeePromoter). Authors note this high performance is not surprising due to overlap between negative example generation and MLM pretraining (Appendix F.2, p. 41; single dataset, single model -- limited evidence for generalizability).

**Genomics -- Chromatin-Profile Prediction (Table 7, p. 10):**

| Model | TF | HM | DHS |
|---|---|---|---|
| gkm-SVM | 89.6 | - | - |
| DeepSea | 95.8 | 85.6 | **92.3** |
| BIGBIRD | **96.1** | **88.7** | 92.1 |

- Strongest improvement on histone-mark (HM) prediction (+3.1 AUC), which is "known to have longer-range correlations" (Gates et al., 2017). Slightly lower on DHS (-0.2), suggesting longer context specifically helps tasks with long-range dependencies (ensemble of 2 models, held-out chromosomes -- moderate evidence).

---

## Limitations and Failure Modes

**Acknowledged Limitations:**

1. **No free lunch** -- The paper proves (Proposition 2, Section 3.4) that certain tasks requiring all-pair inner products are provably harder for any sparse attention mechanism, requiring Omega(n) layers versus O(1) for full attention. This is a fundamental theoretical limitation.
2. **Fixed sparse pattern** -- The random attention is sampled once and fixed; the paper does not explore dynamic or learned sparsity patterns.
3. **Block-based implementation constraints** -- Efficient GPU/TPU computation requires blockifying the attention pattern (Appendix D), which introduces padding overhead for variable-length inputs and requires sequence length divisible by block size.

**Observed Failure Modes:**

- Without global tokens, random + window achieves only 62.7/85.1/80.5 on MLM/SQuAD/MNLI versus BERT-base's 64.2/88.5/83.4 (Table 1, p. 4), confirming global tokens are critical.
- On GLUE tasks (short context), BIGBIRD trails RoBERTa on several benchmarks: CoLA 58.5 vs 63.6 (-5.1), STS-B 87.8 vs 91.2 (-3.4), RTE 75.0 vs 78.7 (-3.7), QQP 88.6 vs 91.9 (-3.3) (Table 16, p. 36).
- On shorter summarization (BBC XSum, CNN/DailyMail), BIGBIRD-Pegasus slightly underperforms Pegasus (Table 20, p. 38), suggesting sparse attention may have marginal overhead on short inputs.
- IMDb classification: BIGBIRD 95.2 vs SoTA 97.4, significantly below the best non-BERT method (Table 15, p. 36).

**[Inferred]** The paper evaluates only base and large models (~110M-330M parameters); scaling behavior to billion-parameter models is unknown.

**[Inferred]** All NLP experiments are English-only, limiting generalizability claims to other languages.

**[Inferred]** The BIGBIRD-ITC large model shows higher BPC (1.456) than Longformer large (1.358) on MLM pretraining (Table 10), despite ITC outperforming Longformer at base scale. This anomaly is not discussed.

#### Scope and Comparability

- **What was not tested:** Models beyond ~330M parameters; sequences beyond 4096 tokens; non-English languages; decoder-only autoregressive models; dynamic or learned sparsity; combination with other efficiency techniques (quantization, distillation, pruning).
- **Comparability notes:** QA test results (Table 3) compare against leaderboard entries that may use different model sizes, training data, or task-specific engineering. The Longformer comparison uses the same base/large setup but there are differences in global token design and regularization (ETC uses CPC loss and relative position encodings, Longformer does not; Appendix E.3, p. 35). Classification SoTA baselines (Table 15) include non-BERT methods. Genomics baselines (DeepSea, DeePromoter) are not Transformer-based.

---

## Conclusions

### Contributions

1. **First theoretical foundations for sparse attention.** Proved that sparse attention with global tokens is both a universal approximator of continuous sequence-to-sequence functions (Theorem 1) and Turing complete (Theorem 3), providing principled justification for sparse attention designs beyond heuristic arguments.

2. **Complementary negative result.** Established that sparsity incurs a provable cost: the furthest-vector task requires Omega(n) layers for any sparse mechanism versus O(1) for full attention (Proposition 2), grounding the expressivity/efficiency tradeoff.

3. **Three-component sparse attention pattern.** Designed an O(n) attention mechanism combining random, window, and global components, with a block-sparse GPU/TPU-efficient implementation enabling 8x longer sequences on the same hardware.

4. **State-of-the-art on long-context benchmarks.** Achieved best results on Natural Questions LA, TriviaQA, WikiHop (QA) and arXiv, PubMed, BigPatent (summarization), with consistent improvements from extending context to 4096 tokens.

5. **Novel genomics applications.** Demonstrated attention-based contextual language models for DNA sequences, achieving 99.9 F1 on promoter prediction and improving chromatin-profile prediction, particularly on histone marks with long-range dependencies.

### Implications

1. **Global tokens are theoretically necessary.** The Turing completeness proof requires global tokens -- random + window alone is insufficient (a corollary of Theorem 3). This suggests all efficient Transformer architectures should include some form of global attention for full expressiveness. (Speculative: this may explain why CLS tokens work well empirically in BERT-style models.)

2. **Graph-theoretic perspective on attention.** Framing attention as a graph sparsification problem opens connections to random graph theory, small-world networks, and spectral graph theory, potentially informing future sparse attention designs.

3. **Sparse attention is broadly applicable.** Success across diverse domains (NLP QA, summarization, classification, GLUE, genomics) suggests sparse attention is not task-specific but a general approach wherever quadratic complexity is the bottleneck.

---

## Key Claims

**C1: Sparse attention is a universal approximator**
- *Claim:* Any sparse attention graph containing a star graph (a single global token connected to all others) can approximate any continuous sequence-to-sequence function to arbitrary precision.
- *Evidence:* Theorem 1, Section 3.2; constructive proof via contextual mappings using selective shift operators (Appendix A, Lemmas 2-5).
- *Status:* Supported (mathematical proof).
- *Scope:* Requires the sparse graph to contain the star graph S; functions must be continuous with compact domain [0,1]^{n x d}.
- *Magnitude:* For any epsilon > 0, d_p(f, g) <= epsilon.

**C2: Sparse attention with global tokens is Turing complete**
- *Claim:* There exists a sparse attention mechanism with O(n) inner products such that the resulting Transformer is Turing complete.
- *Evidence:* Theorem 3, Section 3.3; constructive proof extending Perez et al. (2019) via associativity of max over O(sqrt(j)) intermediate steps (Appendix B).
- *Status:* Supported (mathematical proof).
- *Scope:* Requires global tokens; uses arbitrary precision assumption (same as Perez et al. 2019); encoder-decoder architecture.
- *Magnitude:* Constructive simulation of arbitrary Turing machine with O(n) inner products per step.

**C3: Sparse attention incurs a provable cost**
- *Claim:* For Task 1 (finding furthest vectors), full attention solves it in O(1) layers, but any sparse attention with O_tilde(n) edges requires Omega_tilde(n^{1-o(1)}) layers.
- *Evidence:* Proposition 2, Section 3.4; reduction from the Orthogonal Vector Conjecture (Appendix C).
- *Status:* Supported (conditional on OVC, a standard assumption in fine-grained complexity).
- *Scope:* Applies to all sparse graphs with O_tilde(n) edges, not just BigBird; dimension d = Theta(log^2 n).
- *Magnitude:* Layer count gap from O(1) to Omega(n^{1-o(1)}) -- essentially linear vs constant.

**C4: BigBird-ETC achieves SoTA on QA with long context**
- *Claim:* BIGBIRD-ETC achieves new state-of-the-art on Natural Questions LA, TriviaQA (Full and Verified), and WikiHop on test leaderboards.
- *Evidence:* Table 3, Section 4 (p. 7); leaderboard test results.
- *Status:* Supported.
- *Scope:* Large ETC model, 4096 tokens, English QA tasks; leaderboard results as of 2020.
- *Magnitude:* NQ LA 77.8 F1 (vs ReflectionNet 77.1); TriviaQA Verified 92.4 F1 (vs Fusion-in-Decoder 90.3); WikiHop 82.3 Acc (vs Longformer 81.9). Tested across 4 tasks (strong breadth), single model per task.

**C5: BigBird-Pegasus advances long document summarization**
- *Claim:* BIGBIRD-Pegasus achieves best ROUGE scores on arXiv, PubMed, and BigPatent long document summarization.
- *Evidence:* Table 4, Section 4.1 (p. 8-9).
- *Status:* Supported.
- *Scope:* Large model warm-started from Pegasus; 3072 max encoder sequence length; beam size 5.
- *Magnitude:* Over Pegasus (Reported): arXiv +2.42/+2.07/+2.94, PubMed +0.35/+0.50/+0.99, BigPatent +8.35/+9.38/+8.26 (R-1/R-2/R-L). Tested on 3 long-document datasets (moderate evidence).

**C6: Random + window attention is insufficient without global tokens**
- *Claim:* At 512 tokens, random + window attention achieves only 62.7/85.1/80.5 on MLM/SQuAD/MNLI, falling short of BERT-base's 64.2/88.5/83.4.
- *Evidence:* Table 1, Section 2 (p. 4).
- *Status:* Supported.
- *Scope:* Base model, 512-token sequences, 3 benchmarks (MLM, SQuAD, MNLI).
- *Magnitude:* Gaps of 1.5/3.4/2.9 points on MLM/SQuAD/MNLI. Limited to 3 tasks at 512 tokens (moderate evidence; no ablation at 4096 reported with these specific combinations).

**C7: BigBird enables near-perfect promoter prediction**
- *Claim:* BigBird achieves 99.9 F1 on promoter region prediction, a ~4.3 point jump from previous best.
- *Evidence:* Table 6, Section 5 (p. 9).
- *Status:* Supported.
- *Scope:* EPDnew dataset, 8000bp sequences, base model pretrained with MLM+NSP on human reference genome.
- *Magnitude:* 99.9 F1 vs DeePromoter 95.6 F1 (+4.3 points). Single dataset, single model (limited evidence for generalizability).

**C8: Long-context classification benefits scale with document length**
- *Claim:* BigBird's classification gains are most significant when documents are long and training data is limited.
- *Evidence:* Table 15, Appendix E.4 (p. 35-36).
- *Status:* Supported.
- *Scope:* 5 classification datasets varying in length and training set size.
- *Magnitude:* Arxiv (100% >512 tokens): +4.35 over SoTA; Hyperpartisan (53% >512): +1.6 over SoTA; IMDb (14% >512): -2.2 below SoTA. Pattern holds across 5 datasets (moderate evidence for the length/data-size interaction hypothesis).

---

## Open Questions

1. **Scaling beyond 4096 tokens:** How does BigBird's performance-efficiency tradeoff evolve at 8K, 16K, or longer contexts? The theoretical results suggest scalability, but empirical validation is absent. The block-sparse implementation may face additional challenges at very long sequences.

2. **Decoder-only extension:** Can the theoretical results (Turing completeness, universal approximation) be extended to autoregressive decoder-only models? The proofs focus on encoder (Theorem 1) and encoder-decoder (Theorem 3) architectures.

3. **Optimal sparsity ratios:** What is the optimal balance between random, window, and global attention for different task types? The paper uses fixed hyperparameters across tasks (e.g., r = 3b for ITC, r = 0 for ETC).

4. **Dynamic sparse patterns:** Would learned or input-dependent sparse patterns outperform fixed random patterns? The paper samples random attention once and fixes it; adaptive sparsity could potentially improve performance.

5. **Interaction with other efficiency methods:** How does BigBird combine with quantization, pruning, or knowledge distillation for further efficiency gains? No such combinations are explored.

---

## Core References and Why They Are Referenced

### Theoretical Foundations

- **Perez et al. (2019)** -- *On the Turing Completeness of Modern Neural Network Architectures.* Proved full-attention Transformers are Turing complete under arbitrary precision; BigBird extends this to sparse attention by decomposing the tape-history lookup across intermediate decoder steps.

- **Yun et al. (2019)** -- *Are Transformers universal approximators of sequence-to-sequence functions?* Showed full Transformers approximate all continuous sequence-to-sequence functions on compact domains; BigBird adapts the contextual mapping technique to sparse attention using a global token relay.

- **Yun et al. (2020)** -- *O(n) connections are expressive enough.* Contemporary work also proving universal approximation for sparse transformers, but did not show Turing completeness.

### Graph Theory

- **Watts & Strogatz (1998)** -- *Collective dynamics of 'small-world' networks.* The small-world model (ring lattice + random rewiring) directly inspires BigBird's window + random attention design, balancing locality (high clustering) with short paths.

### Sparse Attention Predecessors

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Introduced fixed sparse patterns (strided + local) at O(n sqrt(n)) complexity; BigBird adds random attention and provides theoretical justification.

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Concurrent work with sliding window + global attention. BigBird adds random attention and theoretical foundations. Key implementation differences: BigBird-ETC uses CPC loss for global tokens and relative position encodings (Appendix E.3).

### Base Models

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers.* Base architecture and MLM pretraining objective that BigBird extends to longer sequences.

- **Liu et al. (2019)** -- *RoBERTa: A Robustly Optimized BERT Pretraining Approach.* Checkpoint used for BigBird-RoBERTa initialization; pretraining recipe followed.

- **Zhang et al. (2020)** -- *PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization.* Summarization-specialized pretraining; checkpoint used for BigBird-Pegasus large model.

- **Ainslie et al. (2020)** -- *ETC: Encoding Long and Structured Data in Transformers.* Closely related work that extensively used global tokens; the BIGBIRD-ETC variant builds on this construction.

### Evaluation Benchmarks

- **Kwiatkowski et al. (2019)** -- *Natural Questions: A Benchmark for Question Answering Research.* Primary QA benchmark where BigBird-ETC achieves SoTA on long answers.

- **Yang et al. (2018)** -- *HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering.* Multi-hop reasoning benchmark requiring evidence aggregation across documents.

- **Cohan et al. (2018)** -- *A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents.* Source of arXiv and PubMed long document summarization datasets.

- **Zhou & Troyanskaya (2015)** -- *Predicting Effects of Noncoding Variants with Deep Learning-Based Sequence Model.* DeepSea model and 919 chromatin-profile prediction dataset used for genomics evaluation.

### Fine-Grained Complexity

- **Abboud et al. (2014, 2015); Williams (2005); Backurs & Indyk (2015)** -- Orthogonal Vector Conjecture (OVC) hardness results underlying the "no free lunch" Proposition 2 proving inherent limitations of sparse attention.
