---
title: "Transformers Need Glasses! Information Over-squashing in Language Tasks"
authors: "Barbero, Banino, Kapturowski, Kumaran, Araújo, Vitvitskyi, Pascanu, Veličković"
year: 2024
venue: "NeurIPS 2024"
paper_type: conference-paper
categories: ["attention-analysis", "architecture", "probing-and-analysis"]
scope: ["information propagation in decoder-only Transformers", "representational collapse", "over-squashing", "counting and copying failures", "softmax normalization limitations"]
benchmarks_used: []
models_introduced: []
models_evaluated: ["gemini-1.5-pro", "gemma-7b"]
key_claims:
  - id: C1
    claim: "Distinct input sequences to a decoder-only Transformer can yield arbitrarily close representations at the final token as sequence length increases, an effect termed representational collapse"
    evidence: "Theorem 4.2, Lemma B.2, Section 4, Figure 5"
    status: supported
  - id: C2
    claim: "Representational collapse is exacerbated by low-precision floating-point formats (bf16), causing collapse near machine precision around 50-100 tokens for fully repeated sequences"
    evidence: "Section 4.2, Figure 5(a-c)"
    status: supported
  - id: C3
    claim: "Decoder-only Transformers exhibit over-squashing: earlier tokens have exponentially more information pathways to the final token than later tokens due to the causal mask topology"
    evidence: "Theorem 5.1, Section 5"
    status: supported
  - id: C4
    claim: "Over-squashing provides a topological explanation for the U-shaped retrieval curve observed in LLMs, where information at sequence start and end is retrieved better than mid-sequence information"
    evidence: "Section 5, connection to Theorem 5.1 path-counting argument"
    status: supported
  - id: C5
    claim: "A Transformer without positional encodings and with causal attention is immediately unable to count"
    evidence: "Proposition 6.1, Section 6"
    status: supported
  - id: C6
    claim: "Counting becomes impossible in practice due to the combined effects of representational collapse and finite floating-point precision, even with positional encodings"
    evidence: "Corollary 6.2, Figures 3-4, Section 6"
    status: supported
  - id: C7
    claim: "Gemini 1.5 fails at copying the last element of sequences beyond ~300 tokens, while first-element copying remains substantially better"
    evidence: "Figure 2, Section 4"
    status: supported
  - id: C8
    claim: "Inserting delimiter tokens (e.g., commas) every few positions maintains representational separation and mitigates collapse"
    evidence: "Figure 5(d), Section 4"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Analyzes fundamental limitations of the softmax attention mechanism and causal masking introduced in the original Transformer"
  - target: 2024-02-lost-in-the-middle
    type: formalizes
    detail: "The over-squashing theorem (Theorem 5.1) provides a theoretical explanation for the U-shaped retrieval curve: early tokens have exponentially more information pathways, while end tokens benefit from recency bias"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "Both papers identify issues rooted in softmax normalization; attention sinks are related to the over-squashing phenomenon where information concentrates at initial tokens"
  - target: 2025-04-attention-sink-emerges
    type: complementary
    detail: "Gu et al. also identify softmax normalization as a root cause of attention sinks; Barbero et al. provide a complementary theoretical perspective through the over-squashing framework"
  - target: 2025-07-position-bias-transformers
    type: concurrent
    detail: "Both provide theoretical analysis of position-dependent information flow in causal Transformers; Wu et al. use graph-theoretic cumulative context probability while Barbero et al. use gradient sensitivity bounds from GNN over-squashing theory"
  - target: 2021-05-gnn-bottleneck-over-squashing
    type: extends
    detail: "Adapts the over-squashing framework introduced by Alon & Yahav for GNNs to decoder-only Transformers, using Jacobian sensitivity bounds from Di Giovanni et al. (2023) to show exponentially asymmetric information pathways in the causal mask topology"
  - target: 2020-07-quantifying-attention-flow
    type: extends
    detail: "Extends information flow analysis from encoder-only (BERT) to decoder-only Transformers, showing how the causal mask creates asymmetric information propagation"
  - target: 2024-01-roformer-rope
    type: evaluates
    detail: "Analyzes how RoPE's distance-dependent decay interacts with representational collapse, assuming positional encodings decay with distance (Theorem 4.2 assumption)"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "Both analyze information flow in Transformers; the circuits framework decomposes attention into QK/OV circuits, while Barbero et al. analyze aggregate signal propagation through the causal computation graph"
  - target: 2024-03-gemini-1.5-long-context
    type: evaluates
    detail: "Uses Gemini 1.5 as the primary model for empirical validation of counting and copying failures"
  - target: 2020-07-theoretical-limitations-self-attention
    type: extends
    detail: "Hahn proved that fixed-size self-attention cannot model PARITY or Dyck languages; Barbero et al. extend this line of theoretical analysis to decoder-only Transformers, proving representational collapse and over-squashing"
open_questions:
  - question: "Can architectural modifications (e.g., bidirectional attention layers, different normalization schemes) eliminate over-squashing while preserving autoregressive generation capability?"
    addressed_by: null
  - question: "How do different positional encoding schemes (absolute, relative, rotary) interact with the rate of representational collapse across sequence lengths?"
    addressed_by: null
  - question: "Does chain-of-thought prompting fundamentally overcome or merely delay the representational collapse and counting limitations identified?"
    addressed_by: null
---
# Transformers Need Glasses! Information Over-squashing in Language Tasks

**Authors:** Federico Barbero, Andrea Banino, Steven Kapturowski, Dharshan Kumaran, João G.M. Araújo, Alex Vitvitskyi, Razvan Pascanu, Petar Veličković (University of Oxford, Google DeepMind)
**Date:** December 2024, NeurIPS 2024 (arXiv:2406.04267)

---

## Core Research Problem

Decoder-only Transformers process sequences through causal (unidirectional) attention, where next-token prediction relies entirely on the representation of the last token at the final layer. This creates an asymmetric computation graph: earlier tokens have more layers through which their information can propagate to the final position, while later tokens have fewer. The implications of this architectural constraint for information fidelity at the final token have not been formally characterized.

Prior work established that Transformers with hard attention and infinite precision are Turing-complete (Pérez et al., 2021), but finite-precision soft-attention Transformers cannot solve simple formal languages such as PARITY and DYCK (Hahn, 2020; Delétang et al., 2023; Weiss et al., 2021). Separately, the GNN community has studied *over-squashing* --- the loss of information when many node features must be compressed into fixed-dimensional representations due to graph bottlenecks (Alon and Yahav, 2021; Topping et al., 2022; Di Giovanni et al., 2023). The connection between GNN over-squashing and Transformer information propagation under causal masking had not been drawn.

**The core challenge is: decoder-only Transformers suffer from two interrelated phenomena --- representational collapse (distinct inputs producing indistinguishable final-token representations) and over-squashing (position-dependent information loss) --- that provably limit their ability to perform counting and copying tasks.**

---

## Problem Solutions

The paper identifies two fundamental limitations of the decoder-only Transformer architecture through signal propagation analysis of the final token's representation, and proposes simple mitigations:

1. **Representational collapse** is formalized as a consequence of softmax normalization: when sequence elements converge, the softmax output converges to uniform attention, making the final-token representation insensitive to input differences.
2. **Over-squashing** is shown to arise from the causal mask topology, where the number of information pathways from token $i$ to the final token $n$ decreases for tokens closer to $n$, creating a gradient sensitivity bound that decays with the number of available paths.
3. **Practical mitigations** include inserting delimiter tokens to break representational uniformity and using higher-precision arithmetic to delay collapse.

---

## Approach Details

### Method

The analysis focuses on the Pre-LN (pre-layer-normalization) decoder-only Transformer. The architecture is formalized as:

> **Attention:** $\mathbf{z}_i^{(\ell)} = \sum_{j \le i} \alpha_{ij}^{(\ell)} \text{norm}_1^{(\ell)}(\mathbf{v}_i^{(\ell)}) + \mathbf{v}_i^{(\ell)}$
>
> **Feed-forward:** $\mathbf{v}_i^{(\ell+1)} = \psi^{(\ell)}(\text{norm}_2^{(\ell)}(\mathbf{z}_i^{(\ell)})) + \mathbf{z}_i^{(\ell)}$
>
> **Output:** $\mathbf{y}_i = \text{norm}_3(\mathbf{v}_i^{(L)})$

where $\alpha_{ij}^{(\ell)} = \exp(k(\mathbf{q}_i^{(\ell)}, \mathbf{k}_j^{(\ell)}, \mathbf{p}_{ij})) / \sum_{w \le i} \exp(k(\mathbf{q}_i^{(\ell)}, \mathbf{k}_w^{(\ell)}, \mathbf{p}_{iw}))$ are causal attention weights and $\mathbf{p}_{ij}$ are positional encodings.

### Key Technical Components

#### Representational Collapse (Section 4)

**Lemma 4.1 (Softmax Convergence).** For sequences $\mathbf{x} \in \mathbb{R}^n$ and $\mathbf{x}^* \in \mathbb{R}^{n+1}$ where the entries remain bounded and the final elements converge ($\lim_{n \to \infty} |x_n - x_n^*| = 0$), the total variation distance between their softmax distributions approaches zero:

> $\delta(\text{softmax}(\mathbf{x}), \text{softmax}(\mathbf{x}^*)) \to 0 \text{ as } n \to \infty$

**Theorem 4.2 (Representational Collapse).** Consider two sequences where the second repeats the final token of the first: $\mathbf{v}^{(0)} \in \mathbb{R}^{n \times d}$ and $\mathbf{v}^{*(0)} \in \mathbb{R}^{(n+1) \times d}$. Assuming positional encodings decay with distance (i.e., the positional bias $\mathbf{p}_{ij}$ depends on $|i - j|$ and decays as this distance grows), their final-token representations become arbitrarily close as sequence length increases:

> $\|\mathbf{y}_n - \mathbf{y}_n^*\| \to 0 \text{ as } n \to \infty$

**Quantization effects (Section 4.2).** In bf16 precision (7-bit mantissa), representational collapse reaches machine precision at approximately 50--100 tokens for fully repeated sequences. In fp32 (23-bit mantissa), collapse is delayed but not eliminated.

#### Over-squashing (Section 5)

**Theorem 5.1 (Over-squashing in Transformers).** The gradient of the final-token output $\mathbf{y}_n$ with respect to input token $\mathbf{v}_i^{(0)}$ is bounded by:

> $\left\|\frac{\partial \mathbf{y}_n}{\partial \mathbf{v}_i^{(0)}}\right\| \le C \sum_{k_1 \ge i} \cdots \sum_{k_\ell \ge k_{\ell-1}} \bar{\alpha}_{n,k_\ell}^{(L-1)} \prod_{\ell=2}^{L-1} \bar{\alpha}_{k_\ell, k_{\ell-1}}^{(\ell-1)} \bar{\alpha}_{k_1, i}^{(0)}$

where $C$ is a constant depending on layer normalization and MLP Lipschitz constants, and $\bar{\alpha}$ are upper bounds on attention weights. The key insight is that this sum counts the number of directed paths from token $i$ to token $n$ through the $L$-layer causal computation graph. Earlier tokens have combinatorially more such paths than later tokens.

**Proposition 5.2.** Under certain normalization assumptions, as layer depth $L \to \infty$, the output depends only on the first input token --- an extreme degenerate case of over-squashing.

**Connection to U-shaped retrieval.** Over-squashing explains why LLMs retrieve information better from the beginning and end of sequences than from the middle (Liu et al., 2024). The beginning has an advantage from pathway abundance (exponentially more paths); the end has an advantage from learned recency bias in autoregressive training. The middle suffers from both moderate path count and lack of recency bias.

#### Counting Impossibility (Section 6)

**Proposition 6.1.** A Transformer without positional encodings and with a causal attention mechanism is immediately unable to count. The proof relies on the fact that softmax normalization prevents unbounded accumulation of values across positions.

**Corollary 6.2.** Even with positional encodings, counting becomes impossible in practice when representational collapse occurs, because the model cannot distinguish between sequences of different lengths once their final-token representations converge.

### Experimental Setup

**Models:**
- **Gemini 1.5:** Primary model for counting and copying tasks
- **Gemma 7B:** Open-source model for internal representation analysis

**Copying tasks:**
- Binary sequences: `1...10` vs `01...1` --- copy the last element
- Sequence lengths: 50 to 500+ tokens
- Variants: first-element copying, interleaved patterns, delimiter-separated

**Counting tasks:**
- Sum arithmetic: $1 + 1 + \cdots + 1$ up to varying counts
- Sequence counting: count number of 1s in pure and mixed (70% ones) sequences
- Word frequency: count occurrences of a specific word in text

**Prompting strategies:** Direct instruction, chain-of-thought (CoT) without examples, CoT with few-shot demonstrations.

### Key Results

#### Copying Performance (Gemini 1.5)

| Task variant | Failure onset | Notes |
|---|---|---|
| Last-element copying | ~300 tokens | Accuracy degrades continuously |
| First-element copying | Substantially later | Consistent with over-squashing advantage for early positions |
| With hint ("check carefully") | Improved | Hints partially mitigate but do not eliminate failure |
| Interleaved patterns (1010...) | Improved | Pattern variation breaks collapse-inducing uniformity |

#### Counting Performance (Gemini 1.5)

Counting accuracy degrades sharply as sequence length increases. Output histograms reveal that the model clusters predictions around round numbers (50, 100), indicating coarse numerical approximation rather than systematic counting. For $1+1+\cdots+1$, the peak frequency is at the value 100, suggesting a subitizing-like approximation strategy. Chain-of-thought prompting provides minimal improvement.

#### Representational Analysis (Gemma 7B)

| Sequence type | Collapse behavior |
|---|---|
| Constant digit (all 1s) | $\infty$-norm difference reaches machine precision by ~50 tokens |
| Random digit sequences | Slower collapse but consistent downward trend |
| With comma separators | Representation separation maintained |

### Theoretical Analysis

The central theoretical insight is connecting the causal attention mask to a directed graph and applying the over-squashing framework from GNN theory. In GNNs, over-squashing is measured via commute times between nodes: the expected number of random walk steps to travel between two nodes and return. Nodes with high commute times suffer severe information loss. In the decoder-only Transformer, the causal mask creates a graph where information flows strictly left-to-right, and the final token is a convergence point for all paths --- exactly the topology prone to over-squashing.

The paper draws on Di Giovanni et al. (2023), who showed that GNN over-squashing is controlled by the Jacobian $\partial \mathbf{x}_v^{(L)} / \partial \mathbf{x}_u^{(0)}$, and adapts this analysis to the Transformer by accounting for layer normalization (absorbed into constants $\beta_i$), MLP non-linearities (bounded via Lipschitz constants), and multi-head attention (using upper bounds on per-head attention weights).

---

## Limitations and Failure Modes

- **Layer normalization simplification.** The analysis summarizes layer normalization effects via a constant $\beta_i$ rather than modeling its full input-dependent behavior. This may underestimate or overestimate the actual collapse rate.
- **Input-independent attention weights.** The theoretical bounds treat attention weights as input-independent for tractability, whereas in practice, attention patterns are highly input-dependent.
- **Tokenization effects.** Sequences like `11111` may not tokenize as five individual `1` tokens, complicating direct application of the theoretical results to real inputs.
- **Focus on final-token representation.** The analysis considers only the last token's representation at the final layer, not the full sequence of hidden states.
- **Limited architectural scope.** Results are established for pre-LN decoder-only Transformers with softmax attention and do not directly apply to encoder-decoder models, linear attention variants, or architectures using alternative normalization.
- **Empirical evaluation on proprietary model.** Primary empirical results use Gemini 1.5, whose architecture details are not publicly available, limiting reproducibility of the exact experimental setup.

---

## Conclusions

### Contributions

1. **Formalized representational collapse** (Theorem 4.2): proved that distinct input sequences produce arbitrarily close final-token representations as sequence length increases, with the effect accelerated by low-precision arithmetic (Section 4).
2. **Established over-squashing in decoder-only Transformers** (Theorem 5.1): showed that the causal mask topology creates position-dependent gradient sensitivity bounds, with earlier tokens having exponentially more information pathways than later tokens (Section 5).
3. **Proved counting impossibility** (Proposition 6.1, Corollary 6.2): demonstrated that softmax normalization and representational collapse prevent systematic counting in autoregressive Transformers (Section 6).
4. **Provided empirical validation** on Gemini 1.5 and Gemma 7B, confirming that copying fails beyond ~300 tokens and counting degrades sharply with sequence length, with representational collapse measurable in internal representations (Figures 2--5).
5. **Proposed simple mitigations**: delimiter insertion maintains representational separation; pattern variation and prompt hints partially alleviate copying failures (Figure 5(d)).

### Implications

1. The fundamental limitations identified are architectural, not a matter of scale or training --- larger models may delay but not eliminate representational collapse and over-squashing (speculative beyond paper's direct evidence).
2. The connection between GNN over-squashing and Transformer information flow opens a new theoretical lens for analyzing sequence model limitations.
3. Practical applications requiring reliable counting or copying over long sequences (e.g., code generation, mathematical reasoning) may benefit from architectural modifications that break the causal attention bottleneck.

---

## Key Claims

1. **C1 (Representational collapse).** Distinct input sequences yield arbitrarily close final-token representations as length increases (Theorem 4.2). **Status: supported.**
2. **C2 (Precision-dependent collapse).** bf16 precision causes collapse near machine precision at ~50--100 tokens for repeated sequences (Figure 5). **Status: supported.**
3. **C3 (Over-squashing in Transformers).** The causal mask creates exponentially more information pathways for earlier tokens than later tokens (Theorem 5.1). **Status: supported.**
4. **C4 (U-shape explanation).** Over-squashing provides a topological explanation for the U-shaped retrieval curve in LLMs (Section 5). **Status: supported.**
5. **C5 (Counting impossibility without PE).** Transformers without positional encodings cannot count (Proposition 6.1). **Status: supported.**
6. **C6 (Practical counting impossibility).** Counting fails in practice due to combined representational collapse and finite precision (Corollary 6.2, Figures 3--4). **Status: supported.**
7. **C7 (Copying failure).** Gemini 1.5 fails at last-element copying beyond ~300 tokens (Figure 2). **Status: supported.**
8. **C8 (Delimiter mitigation).** Inserting delimiters maintains representational separation (Figure 5(d)). **Status: supported.**

---

## Open Questions

- Can architectural modifications (e.g., bidirectional attention layers, alternative normalization) eliminate over-squashing while preserving autoregressive generation capability? *Not addressed in the reference collection.*
- How do different positional encoding schemes interact with the rate of representational collapse across sequence lengths? *Not addressed in the reference collection.*
- Does chain-of-thought prompting fundamentally overcome or merely delay representational collapse and counting limitations? *Not addressed in the reference collection.*
- Can the over-squashing framework be extended to predict performance degradation on specific downstream tasks beyond counting and copying? *Not addressed in the reference collection.*

---

## Core References and Why They Are Referenced

### Transformer Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the Transformer architecture with softmax attention and multi-head attention, the core architecture analyzed.
- **Xiong et al. (2020)** -- *On Layer Normalization in the Transformer Architecture.* Pre-LN variant used as the analysis target, with layer normalization effects absorbed into constants.

### Over-squashing Theory from Graph Neural Networks

- **Alon and Yahav (2021)** -- *On the Bottleneck of Graph Neural Networks and its Practical Implications.* Introduced over-squashing as a concept in GNNs, showing information loss when distant nodes must communicate through bottleneck structures.
- **Topping et al. (2022)** -- *Understanding Over-squashing and Bottlenecks on Graphs via Curvature.* Connected over-squashing to graph curvature, providing the geometric framework adapted here for the causal attention graph.
- **Di Giovanni et al. (2023)** -- *On Over-squashing in Message Passing Neural Networks: The Impact of Width, Depth, and Topology.* Provided the Jacobian-based sensitivity analysis that Theorem 5.1 adapts to the Transformer setting.

### Formal Language and Computational Limitations

- **Hahn (2020)** -- *Theoretical Limitations of Self-Attention in Neural Sequence Models.* Showed softmax attention cannot solve PARITY; motivation for studying fundamental limitations.
- **Delétang et al. (2023)** -- *Neural Networks and the Chomsky Hierarchy.* Demonstrated Transformers fail on formal languages outside regular/context-free classes.
- **Weiss et al. (2021)** -- *Thinking Like Transformers.* Provided RASP programming language for analyzing Transformer computations.
- **Pérez et al. (2021)** -- *Attention is Turing Complete.* Showed hard-attention infinite-precision Transformers are Turing-complete, contrasting with the finite-precision limitations studied here.

### Empirical Phenomena Explained

- **Liu et al. (2024)** -- *Lost in the Middle.* Documented the U-shaped retrieval curve that over-squashing theory explains through pathway counting.
- **Xiao et al. (2024)** -- *Efficient Streaming Language Models with Attention Sinks.* Discovered attention sinks at initial tokens, related to the over-squashing framework's prediction that initial tokens dominate information flow.

### Models Used in Evaluation

- **Google DeepMind (2024)** -- *Gemini 1.5.* Primary model for empirical validation of counting and copying failures.
- **Google DeepMind (2024)** -- *Gemma.* Open-source model used for internal representation analysis measuring representational collapse.
