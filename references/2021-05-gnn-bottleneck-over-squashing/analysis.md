---
title: "On the Bottleneck of Graph Neural Networks and its Practical Implications"
authors: "Alon, Yahav"
year: 2021
venue: "ICLR 2021"
paper_type: conference-paper
categories: ["graph-neural-networks", "attention-analysis"]
scope: ["over-squashing in GNNs", "message-passing bottleneck", "exponential receptive field compression", "long-range interaction failure"]
benchmarks_used: ["qm9", "nci1", "enzymes", "varmisuse", "tree-neighborsmatch"]
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "GNNs suffer from over-squashing: exponentially growing information from the receptive field is compressed into fixed-size vectors, preventing propagation of long-range signals"
    evidence: "Section 3, Figure 3, Section 5 (combinatorial lower bound)"
    status: supported
  - id: C2
    claim: "GNNs that absorb incoming edges equally (GCN, GIN) are more susceptible to over-squashing than GNNs that weight or filter incoming messages (GAT, GGNN)"
    evidence: "Figure 3 (GCN/GIN fail at r=4, GAT/GGNN fail at r=5), Section 3"
    status: supported
  - id: C3
    claim: "Over-squashing is distinct from over-smoothing and under-reaching — it occurs even when the problem radius is within reach and representations remain distinguishable"
    evidence: "Section 3, Appendix E, chain experiment (Appendix A)"
    status: supported
  - id: C4
    claim: "The required hidden dimension d to represent all possible label assignments grows faster than exponentially with problem radius r"
    evidence: "Equations 4--5, Figure 4, Section 5"
    status: supported
  - id: C5
    claim: "Adding a single fully-adjacent (FA) layer at the last GNN layer reduces error by 42% on QM9 across six GNN types without any hyperparameter tuning"
    evidence: "Table 1, Table 4, Section 4.2"
    status: supported
  - id: C6
    claim: "Existing extensively-tuned GNN models on real-world benchmarks (QM9, ENZYMES, NCI1, VarMisuse) suffer from over-squashing, and breaking the bottleneck improves state-of-the-art results"
    evidence: "Tables 1--3, Table 4, Sections 4.2--4.4"
    status: supported
cross_references:
  - target: 2024-12-transformers-need-glasses-over-squashing
    type: extended-by
    detail: "Barbero et al. adapt the over-squashing framework from GNNs to decoder-only Transformers, showing that the causal mask topology creates exponentially more information pathways for earlier tokens (Theorem 5.1)"
open_questions:
  - question: "Does the over-squashing bottleneck apply to attention-based architectures beyond GNNs, such as Transformers with causal masking?"
    addressed_by: 2024-12-transformers-need-glasses-over-squashing
  - question: "Can graph rewiring or topology-aware modifications eliminate over-squashing without discarding the graph structure entirely?"
    addressed_by: null
  - question: "How does over-squashing interact with over-smoothing in deep GNNs — do they compound, or does one dominate depending on the task?"
    addressed_by: null
---

# On the Bottleneck of Graph Neural Networks and its Practical Implications

**Authors:** Uri Alon, Eran Yahav (Technion — Israel Institute of Technology)
**Date:** May 2021, ICLR 2021 (arXiv:2006.05205)

---

## Core Research Problem

Graph Neural Networks (GNNs) perform message-passing over a graph structure: each node aggregates information from its neighbors over K layers, building representations that capture increasingly distant context. The prevailing explanation for GNN failures on tasks requiring deep reasoning was **over-smoothing** — the tendency for node representations to converge to indistinguishable states as layers increase (Li et al., 2018; Oono & Suzuki, 2020). However, over-smoothing was demonstrated primarily on **short-range tasks** (e.g., paper subject classification, product category classification) where the required interaction distance (problem radius) is small.

This paper identifies a different and more fundamental limitation: **over-squashing**. A node's receptive field after K message-passing layers grows as `|N_v^K| = O(exp(K))` (Chen et al., 2018), meaning the amount of information that must be aggregated grows exponentially while node representations remain fixed-size vectors. This creates a bottleneck analogous to the fixed-size encoding vector in RNN seq2seq models (Sutskever et al., 2014; Cho et al., 2014), but **asymptotically worse** because the receptive field grows exponentially rather than linearly. As a result, GNNs fail to propagate messages from distant nodes, learning only short-range signals and generalizing poorly on tasks that depend on long-range interaction.

The paper distinguishes three failure modes that had been conflated in prior work:

1. **Under-reaching:** Distant nodes (farther than K hops) simply cannot interact. Solved by adding more layers.
2. **Over-smoothing:** Node representations become indistinguishable as layers increase. Occurs even on short-range tasks.
3. **Over-squashing:** Exponentially growing information is compressed into fixed-size vectors. Occurs even when nodes are within reach and representations remain distinguishable.

**The core challenge is: message-passing GNNs fundamentally cannot propagate long-range information because the exponentially growing receptive field must be compressed into fixed-size node representations, creating a bottleneck that worsens with problem radius.**

---

## Problem Solutions

The paper's primary contribution is **identifying and explaining the over-squashing phenomenon**, not proposing a new architecture. The solution is deliberately simple to demonstrate that over-squashing is so prevalent that even a minimal fix improves results.

1. **Over-squashing is the dominant failure mode for long-range tasks.** The paper constructs a synthetic benchmark (Tree-NeighborsMatch) that isolates over-squashing from over-smoothing and under-reaching, showing that all tested GNNs fail to fit training data beyond problem radius r=4--5.

2. **GNN aggregation mechanism determines susceptibility.** GNNs that absorb incoming edges equally (GCN, GIN) are more susceptible than those that can weight or filter messages (GAT, GGNN), because the former must compress information from all leaves into a single vector before combining with the target node.

3. **A fully-adjacent (FA) last layer breaks the bottleneck.** Modifying only the adjacency of the final GNN layer to connect all node pairs — without adding weights or changing the layer type — allows topology-aware representations from earlier layers to interact directly, reducing over-squashing.

---

## Approach Details

### Method

A standard GNN layer updates node representations via:

> h_v^(k) = f_k(h_v^(k-1), {h_u^(k-1) | u in N_v}; theta_k)

where `N_v = {u in V | (u,v) in E}`. The receptive field grows recursively:

> N_v^1 := N_v
> N_v^K := N_v^(K-1) ∪ {w | (w,u) in E and u in N_v^(K-1)}

For a GNN with K layers, the **fully-adjacent (FA) layer** modifies only the K-th layer:

> N_v := V for every node v in V, in the K-th layer only.

This does not change the layer type, add weights, or modify hyperparameters — it only changes the adjacency in a single layer. The first K-1 layers exploit the original sparse graph topology; only the last layer allows all topology-aware representations to interact directly.

### Key Technical Components

**GCN aggregation** (Kipf & Welling, 2017):

> h_v^(k) = σ(Σ_{u ∈ N_v ∪ {v}} (1/c_{u,v}) W^(k) h_u^(k-1))

where c_{u,v} is a normalization factor (typically sqrt(|N_v| · |N_u|)).

**GIN aggregation** (Xu et al., 2019):

> h_v^(k) = MLP^(k)((1 + ε^(k)) h_v^(k-1) + Σ_{u ∈ N_v} h_u^(k-1))

Both GCN and GIN aggregate **all** neighbors before combining with the target node's representation, compressing information from all leaves into a single vector. In contrast, **GAT** (Veličković et al., 2018) uses attention to weight incoming messages given the target's representation, and **GGNN** (Li et al., 2016) uses a GRU cell that filters incoming edges analogously (hypothesized as "element-wise attention" following Levy et al., 2018). At the last layer, GAT/GGNN can ignore irrelevant incoming edges and absorb only the relevant one, compressing information from only **half** the leaves. This provides at most 1 additional radius level of capacity.

**Tree-NeighborsMatch benchmark.** A synthetic problem designed to isolate over-squashing. The graph is a binary tree of controllable depth, with green label-nodes at the leaves and a target node at the root. Each green node has a unique number of blue neighbors and an alphabetical label. Each training example has a different mapping from neighbor-counts to labels. The goal is to predict the label of the green node whose neighbor count matches the target's. The problem radius r equals the tree depth. Data sizes:

| Depth (r) | Training examples | Combinatorial space |
|---|---|---|
| 2 | 96 | 96 |
| 3 | 8,000 | > 3 × 10^5 |
| 4 | 16,000 | > 3 × 10^14 |
| 5 | 32,000 | > 10^36 |
| 6 | 32,000 | > 10^90 |
| 7 | 32,000 | > 10^217 |
| 8 | 32,000 | > 10^509 |

### Theoretical Analysis

**Combinatorial lower bound for hidden dimension d** (Section 5). A binary tree (arity m=2) of depth r has 2^r leaf nodes. The number of distinct label assignments is (2^r)! / 2^(2^(r-1)). A single vector of d floats (f=32 bits each) can distinguish at most 2^(32d) cases. The requirement is:

> 2^(32d) > (2^r)! / 2^(2^(r-1))

Since factorial grows faster than any constant-base exponential, a small increase in r requires a **much larger** increase in d. Specific consequence: for d=32, the maximal achievable radius is r=7. Even d=512 can empirically fit at most r=7.

| r | Combinatorial min d | Empirical min d |
|---|---|---|
| 2 | 1 | 4 |
| 3 | 1 | 16 |
| 4 | 1 | 64 |
| 5 | 3 | 128 |
| 6 | 8 | 256 |
| 7 | 19 | 512 |
| 8 | 45 | — |
| 9 | 106 | — |
| 10 | 243 | — |
| 11 | 548 | — |

The empirical minimum always exceeds the combinatorial lower bound because gradient descent is not guaranteed to find a solution even when one exists. The analysis holds for GCN and GIN; GAT-style architectures that use the recipient node's representation to aggregate messages need to compress only half the leaves, increasing the upper bound on r by up to 1 (Footnote 1).

**Distinguishing over-squashing from long-range distance.** The authors replace the binary tree with a tree of depth 2 connected to a chain of length up to 6, preserving the same target-to-leaf distance but reducing over-squashing to the level of r=2. Result: all GNN types fit the data to near 100% across all distances, proving the failure is caused by **exponentially growing information** (over-squashing), not long-range distance per se (Appendix A).

### Experimental Setup

**Tree-NeighborsMatch.** Model dimension d=32, r+1 GNN layers, residual connections, layer normalization, Adam optimizer with learning rate 10^-3 decayed by 0.5 after 1,000 epochs without training accuracy increase, stopping after 2,000 epochs without improvement. Training typically ran for tens of thousands of epochs, sometimes reaching 100,000. Implemented in PyTorch Geometric.

**QM9** (Ramakrishnan et al., 2014). ~130,000 molecular graphs (~18 nodes each), 13 real-valued quantum chemical properties. Split: 110,462 / 10,000 / 10,000 (train/val/test). Average graph diameter 6.35 ± 0.91, maximum 10, 90th percentile 8. Used Brockschmidt (2020) implementation with 500+ hyperparameter configurations. Most GNNs best at K=8 layers. Each model trained 5 times per target property.

**NCI1** (Wale et al., 2008). 4,110 graphs (~30 nodes each), 2 classes, anti-lung-cancer activity prediction. **ENZYMES** (Borgwardt et al., 2005). 600 graphs (~33 nodes each), 6-class enzyme classification. Both evaluated using Errica et al. (2020) framework with 72 configurations per GNN type, 10-fold cross-validation, 3 seeds per fold (30 total runs).

**VarMisuse** (Allamanis et al., 2018). Program graphs for variable misuse detection: 254,360 training / 42,654 validation / 117,036 UnseenProject test / 59,974 SeenProject test. Average graphs have ~2,000--4,000 nodes, ~6,000--13,000 edges. 30 configurations per GNN type, 5 runs.

### Key Results

**Tree-NeighborsMatch training accuracy** (d=32):

| r | GGNN | GAT | GIN | GCN |
|---|---|---|---|---|
| 2 | 1.00 | 1.00 | 1.00 | 1.00 |
| 3 | 1.00 | 1.00 | 1.00 | 1.00 |
| 4 | 1.00 | 1.00 | 0.39 | 0.70 |
| 5 | 0.60 | 0.77 | 0.19 | 0.19 |
| 6 | 0.38 | 0.41 | 0.14 | 0.14 |
| 7 | 0.21 | 0.29 | 0.09 | 0.09 |
| 8 | 0.16 | — | 0.08 | 0.08 |

- GCN and GIN fail from r=4; GAT and GGNN fail from r=5.
- This is **training** accuracy — the models cannot even fit the data, ruling out overfitting as the explanation.

**QM9 error rates (×10^-3, 5 runs ± stdev, selected GNN types):**

| Property | R-GIN | R-GIN+FA | R-GAT | R-GAT+FA | GGNN | GGNN+FA |
|---|---|---|---|---|---|---|
| mu | 2.64±0.11 | **2.54±0.09** | 2.68±0.06 | 2.73±0.07 | 3.85±0.16 | **3.53±0.13** |
| alpha | 4.67±0.52 | **2.28±0.04** | 4.65±0.44 | **2.32±0.16** | 5.22±0.86 | **2.72±0.12** |
| ZPVE | 12.93±1.81 | **5.03±0.36** | 14.87±2.88 | **5.98±0.43** | 17.84±3.61 | **5.24±0.30** |
| U0 | 5.88±1.01 | **2.21±0.12** | 7.61±0.46 | **2.19±0.25** | 8.65±2.46 | **3.35±1.68** |
| Relative | — | **−39.54%** | — | **−44.58%** | — | **−47.42%** |

Average across all six tested GNN types: **42% error reduction** from adding a single FA layer, without any hyperparameter tuning.

**Biological benchmarks (30 runs ± stdev):**

| Model | NCI1 | NCI1+FA | ENZYMES | ENZYMES+FA |
|---|---|---|---|---|
| GIN | 80.0±1.4 | **81.5±1.2** | 59.6±4.5 | **67.7±5.3** |
| DiffPool | 76.9±1.9 | **77.6±1.3** | 59.5±5.6 | **65.7±4.8** |
| GraphSAGE | 76.0±1.8 | **77.7±1.8** | 58.2±6.0 | **60.8±4.5** |
| DGCNN | 76.4±1.7 | **76.8±1.5** | 38.9±5.7 | **42.8±5.3** |

Average improvement: 4.8% error reduction on NCI1, 12% on ENZYMES. GIN+FA achieves the best result on both datasets.

**VarMisuse accuracy (5 runs ± stdev):**

| Model | SeenProj | SeenProj+FA | UnseenProj | UnseenProj+FA |
|---|---|---|---|---|
| R-GCN | 88.3±0.4 | **88.4±0.7** | 82.9±0.8 | **83.8±1.0** |
| R-GAT | 86.9±0.7 | **87.9±1.0** | 81.2±0.9 | **82.0±1.9** |
| GGNN | 85.7±0.5 | **86.3±0.7** | 79.3±1.2 | 79.1±1.1 |

New state-of-the-art: **88.4%** SeenProjTest and **83.8%** UnseenProjTest (R-GCN+FA).

### Ablation Studies

**Alternative solutions** (R-GCN on QM9, Table 5):

| Variant | Relative error vs. base |
|---|---|
| +FA (last layer fully-adjacent) | −43.40% |
| Penultimate FA (FA at layer K−1) | −45.2% |
| 2× FA (two FA layers stacked) | −43.30% |
| 2× d (d=256 instead of 128) | −5.50% |
| All FA (all layers fully-adjacent) | +1,520% |

- Doubling the hidden dimension provides only 5.5% improvement — dimensionality increase is ineffective against over-squashing.
- Making **all** layers fully-adjacent (ignoring graph topology) is catastrophic (+1,520% error), confirming that the graph structure is essential in early layers.
- Penultimate FA is slightly better than last-layer FA.

**Partial-FA** (R-GCN on QM9, Table 6):

| FA edge fraction | Error vs. base |
|---|---|
| 0.25× | −8.4% |
| 0.50× | −31.5% |
| 0.75× | −37.1% |
| 1.00× (full FA) | −43.4% |

Error reduction scales monotonically with the fraction of added fully-adjacent edges.

---

## Limitations and Failure Modes

- **Over-squashing is inherent to message-passing.** The paper shows the bottleneck is a fundamental property of the message-passing paradigm where exponentially growing receptive fields must be compressed into fixed-size vectors. The FA layer is not a principled solution — it is acknowledged as "a simple solution" whose "purpose is merely to demonstrate that over-squashing in GNNs is so prevalent and untreated that even the simplest solution helps" (Section 6).

- **All-FA destroys performance.** Ignoring the graph topology entirely (all layers FA) increases error by 1,520% on QM9, demonstrating that a full solution cannot simply bypass the graph structure but must balance topology exploitation with information propagation (Table 5).

- **Gradient descent compounds the problem.** The empirical minimum hidden dimension required for each problem radius consistently exceeds the combinatorial lower bound (Figure 4), because gradient-based optimization is not guaranteed to find a solution even when one exists.

- **FA layer adds O(|V|^2) edges.** For large graphs (e.g., VarMisuse with ~2,000--4,000 nodes), the fully-adjacent layer is computationally expensive. The paper does not discuss scalability beyond the tested graph sizes.

- **Improvement on VarMisuse is smaller than on QM9.** GGNN+FA slightly underperforms base GGNN on VarMisuse UnseenProjTest (79.1% vs. 79.3%), suggesting the FA layer may not universally help on all graph types and tasks (Table 3).

- **Theoretical bound applies to GCN/GIN only.** The combinatorial analysis (Equations 4--5) is tight for GCN and GIN. For GAT-style architectures that filter messages, the bound relaxes by approximately one radius level (Footnote 1), but the exponential scaling remains.

---

## Conclusions

### Contributions

1. **Identified over-squashing as a fundamental GNN limitation distinct from over-smoothing.** The exponentially growing receptive field `|N_v^K| = O(exp(K))` must be compressed into fixed-size vectors, creating a bottleneck that prevents propagation of long-range signals. This is distinct from both under-reaching (insufficient layers) and over-smoothing (converging representations) (Section 3, Appendix E).

2. **Characterized GNN susceptibility by aggregation mechanism.** GNNs that absorb incoming edges equally (GCN, GIN) fail at problem radius r=4; those with attention or gating mechanisms (GAT, GGNN) fail at r=5. The difference arises because attention-based GNNs can filter irrelevant messages, compressing only half the information per step (Figure 3, Section 3).

3. **Established combinatorial lower bounds on hidden dimension.** The required hidden dimension d grows faster than exponentially with problem radius r (Equations 4--5). For d=32, the theoretical maximum radius is r=7; empirically, gradient descent fails earlier (Figure 4, Section 5).

4. **Demonstrated that existing real-world GNN models suffer from over-squashing.** Adding a single FA layer to extensively-tuned models reduced error by 42% on QM9 (six GNN types), 12% on ENZYMES, 4.8% on NCI1, and achieved new state-of-the-art on VarMisuse — all without hyperparameter tuning (Tables 1--3, Section 4).

5. **Provided a controlled synthetic benchmark for over-squashing.** Tree-NeighborsMatch isolates over-squashing from other failure modes, enabling precise measurement of GNN susceptibility as a function of problem radius (Section 4.1, Figure 3).

### Implications

1. Over-squashing is the **dominant** failure mode for GNN tasks requiring long-range interaction, not over-smoothing. Prior work that attributed long-range failures to over-smoothing may have been diagnosing the wrong phenomenon. [Inference: subsequent work has extended this insight to Transformers, where the causal mask creates analogous information bottlenecks (Barbero et al., 2024).]

2. The FA layer is a proof of concept, not a principled solution. It "opens the path for a variety of follow-up improvements and even better solutions for over-squashing" (Section 6). [Inference: graph rewiring, virtual nodes, and topology-aware message-passing are natural follow-up directions.]

3. The analogy between GNN over-squashing and RNN bottlenecks — where attention mechanisms provided the solution for sequences — suggests that attention-like mechanisms may be needed to fundamentally address the GNN bottleneck (Section 3).

---

## Key Claims

1. **C1: GNNs suffer from over-squashing.** The receptive field grows as O(exp(K)), compressing exponentially growing information into fixed-size vectors. On Tree-NeighborsMatch, all tested GNNs fail to fit training data beyond r=4--5 despite extensive hyperparameter tuning (Figure 3, Section 4.1). Status: **supported**.

2. **C2: GCN and GIN are more susceptible than GAT and GGNN.** GCN and GIN fail at r=4 (training accuracy 0.70 and 0.39 respectively), while GAT and GGNN maintain 100% through r=4 and fail at r=5. The difference is explained by the aggregation mechanism: GCN/GIN compress all neighbors equally; GAT/GGNN can filter irrelevant messages (Figure 3, Section 3). Status: **supported**.

3. **C3: Over-squashing is distinct from over-smoothing and under-reaching.** The chain experiment (Appendix A) shows that replacing the tree structure with a chain of equal length eliminates over-squashing while preserving distance, and all GNNs succeed — proving that the exponential information growth, not the distance, causes failure. Appendix E demonstrates a triangular graph where over-smoothing occurs without over-squashing, and Tree-NeighborsMatch where over-squashing occurs without over-smoothing. Status: **supported**.

4. **C4: The required hidden dimension d grows faster than exponentially with problem radius r.** Equations 4--5 establish the combinatorial lower bound. Empirically, d=32 suffices for r≤4 but fails for r≥5; d=512 achieves at most r=7 (Figure 4, Section 5). Status: **supported**.

5. **C5: FA layer reduces QM9 error by 42% across six GNN types.** R-GIN: −39.54%, R-GAT: −44.58%, GGNN: −47.42%, MLP: −40.33%, R-GCN: −43.40%, GNN-FiLM: −39.53%. All results averaged over 5 runs using Brockschmidt (2020) code with no additional hyperparameter tuning (Table 1, Table 4, Section 4.2). Status: **supported**.

6. **C6: Existing real-world GNN models suffer from over-squashing.** Breaking the bottleneck with a simple FA layer improves results across all tested domains without tuning: QM9 (−42%), ENZYMES (−12%), NCI1 (−4.8%), VarMisuse (new SOTA). QM9 graphs have average diameter 6.35 with 90th percentile 8, and most models used K=8 layers — so at least 90% of examples did not suffer from under-reaching. Training with K=10 showed no improvement over base, confirming the gains come from reduced over-squashing, not increased reachability (Tables 1--3, Section 4). Status: **supported**.

---

## Open Questions

1. **Does over-squashing apply to Transformers with causal masking?** The causal mask creates a directed graph topology analogous to the GNN computation graph. Whether the same exponential bottleneck applies to the Transformer's layered attention mechanism is a natural question. *Addressed by Barbero et al. (2024), who show that over-squashing does occur in decoder-only Transformers (Theorem 5.1).*

2. **Can graph rewiring or topology-aware modifications eliminate over-squashing without discarding the graph structure?** The FA layer is a blunt instrument that ignores topology entirely in the last layer. More principled approaches — such as curvature-based rewiring (Topping et al., 2022), virtual nodes, or learned graph augmentation — may preserve structure while alleviating the bottleneck. *Not addressed in the reference collection.*

3. **How do over-squashing and over-smoothing interact in deep GNNs?** The paper shows they are distinct phenomena, but does not address whether they compound in practice when both conditions are present (deep networks on tasks requiring both local and global information). *Not addressed in the reference collection.*

---

## Core References and Why They Are Referenced

### Message-Passing GNN Foundations

- **Gilmer et al. (2017)** -- *Neural Message Passing for Quantum Chemistry.* Defines the MPNN framework that formalizes GNNs as message-passing systems. Also proposed "virtual edges" to shorten long distances — an early implicit attempt to address over-squashing.

- **Kipf & Welling (2017)** -- *Semi-Supervised Classification with Graph Convolutional Networks.* Defines GCN (Equation 2), one of the two GNN types shown to be most susceptible to over-squashing due to equal-weight aggregation.

- **Xu et al. (2019)** -- *How Powerful Are Graph Neural Networks?* Defines GIN (Equation 3), the other GNN type most susceptible to over-squashing. GIN+FA achieves the best result on NCI1 and ENZYMES.

- **Veličković et al. (2018)** -- *Graph Attention Networks.* Defines GAT with attention-weighted aggregation, which the paper shows is less susceptible to over-squashing because it can filter irrelevant incoming messages.

- **Li et al. (2016)** -- *Gated Graph Sequence Neural Networks.* Defines GGNN with GRU-based gating, similarly less susceptible than GCN/GIN.

### Over-Smoothing (Contrast)

- **Li et al. (2018)** -- *Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning.* One of the first papers to identify over-smoothing. This paper argues that over-smoothing was studied only on short-range tasks and that over-squashing is a distinct, more relevant limitation for long-range problems.

- **Oono & Suzuki (2020)** -- *Graph Neural Networks Exponentially Lose Expressive Power for Node Classification.* Theoretical analysis of over-smoothing that the paper contrasts with the over-squashing phenomenon.

### RNN Bottleneck Analogy

- **Sutskever et al. (2014)** -- *Sequence to Sequence Learning with Neural Networks.* The RNN seq2seq bottleneck (encoding entire input into a fixed-size vector) is the direct analogy. The GNN bottleneck is asymptotically worse because receptive fields grow exponentially rather than linearly.

- **Cho et al. (2014)** -- *On the Properties of Neural Machine Translation: Encoder-Decoder Approaches.* Identified the RNN bottleneck for long sequences that attention mechanisms later solved.

### Implementations and Evaluation Frameworks

- **Brockschmidt (2020)** -- *GNN-FiLM: Graph Neural Networks with Feature-wise Linear Modulation.* Provides the extensively-tuned QM9 and VarMisuse implementations (500+ and 30 configurations respectively) used as baselines.

- **Errica et al. (2020)** -- *A Fair Comparison of Graph Neural Networks for Graph Classification.* Provides the NCI1 and ENZYMES evaluation framework (72 configurations per GNN type, 10-fold cross-validation) used as baselines.

### Subsequent Work on Over-Squashing

- **Topping et al. (2022)** -- *Understanding Over-squashing and Bottlenecks on Graphs via Curvature.* Connected over-squashing to graph curvature, providing a geometric framework for principled graph rewiring.

- **Di Giovanni et al. (2023)** -- *On Over-squashing in Message Passing Neural Networks: The Impact of Width, Depth, and Topology.* Provided Jacobian-based sensitivity analysis that was later adapted to the Transformer setting by Barbero et al. (2024).

- **Barbero et al. (2024)** -- *Transformers Need Glasses! Information Over-squashing in Language Tasks.* Adapts the over-squashing framework from GNNs to decoder-only Transformers, showing that the causal mask topology creates exponentially more information pathways for earlier tokens.
