# Evaluation [p. 4-6]

[p. 4] The evaluation has two goals. First, empirically show that the GNN bottleneck exists, and find the smallest values of $r$ that raise over-squashing, using a synthetic benchmark that is theoretically solvable but where all GNNs fail to reach 100% training accuracy because of the bottleneck (Section 4.1). Second, examine whether the bottleneck exists in prior work which addressed real-world problems (Sections 4.2 to 4.4).

## 4.1 Synthetic Benchmark: NeighborsMatch

[p. 4-5] The NeighborsMatch problem (Figure 2) is a contrived problem designed to provide intuition to the extent of the effect of over-squashing, while allowing control of the problem radius $r$, and thus *control the intensity* of over-squashing. The focus is on the *training* accuracy of a model, to show that over-squashing prevents models from fitting long-range signals in the training set.

### Tree-NeighborsMatch

[p. 4-5] From the perspective of a single node $v$, the rest of the graph may look like a tree of height $K$, rooted at $v$ (Xu et al., 2018; Garg et al., 2020). To simulate this exponentially-growing receptive field, the subgraph in the middle of Figure 2 is instantiated as a binary tree of depth *depth* where the green nodes are its leaves, and the target node is the tree's root. All edges are directed toward the root, such that information is propagated from all nodes toward the target node. The goal is to predict a label for the target node, where the correct answer is the label of the green node that has the same number of blue neighbors as the target node. An illustration is shown in Figure 5 in the appendix. This allows control of the problem radius, i.e., $r = depth$. The bottleneck is observed empirically in this section; in Section 5 a lower bound for the GNN's hidden size given $r$ is provided.

### Model

[p. 5] A network with $r+1$ graph layers is implemented to allow an additional nonlinearity after the information from the leaves reaches the target node. PyTorch Geometric (Fey and Lenssen, 2019) implementation available at https://github.com/tech-srl/bottleneck/. Training configuration and hyperparameter ranges are detailed in Appendix A.

### Results

[p. 5] Figure 3 shows that some GNNs fail to fit the dataset starting from $r=4$. For example, the training accuracy of GCN (Kipf and Welling, 2017) at $r=4$ is 70%. At $r=5$, all GNNs fail to perfectly fit the data. Starting from $r=4$, the models suffered from over-squashing that resulted in *underfitting*: the bottleneck prevented the models from distinguishing between different training examples, even after they were observed tens of thousands of times. These results clearly show the existence of over-squashing, starting from $r=4$.

### Why did some GNNs perform better than others?

[p. 5] GCN and GIN managed to perfectly fit $r=3$ at most, while GGNN and GAT also reached 100% accuracy at $r=4$. The difference can be explained by their neighbor aggregation computation: consider the target node that receives messages in the $r$'th step. GCN and GIN aggregate all neighbors *before* combining them with the target node's representation; they thus must compress the information flowing from *all* leaves into a single vector, and *only afterward* interact with the target node's own representation (Equations (2) and (3)). In contrast, GAT uses attention to weight incoming messages given the target's representation: at the last layer only, the target node can ignore the irrelevant incoming edge, and absorb only the relevant incoming edge, which contains information flowing from *half* of the leaves. That is, a single vector compresses *only half* of the information. Since the number of leaves grows exponentially with $r$, it is expected that GNNs that need to compress *only half* of the information (GGNN and GAT) will succeed at an $r$ that is larger by 1. Following Levy et al. (2018), the authors hypothesize that the GRU cell in GGNNs filters incoming edges as GAT, but performs this filtering as element-wise attention.

### Overfitting short-range signals

[p. 5] If all GNNs have reached low *training* accuracy, how do GNN-based models usually *do fit* the training data in public datasets of long-range problems? The authors hypothesize that they overfit short-range signals and artifacts from the training set, rather than learning the long-range information that was squashed in the bottleneck, and thus generalize poorly at test time.

## 4.2 Quantum Chemistry: QM9

### Measuring over-squashing

[p. 5] The authors wish to measure over-squashing in existing models. Since over-squashing cannot be directly measured, they instead measure whether breaking the bottleneck improves the results of long-range problems.

### Adding a fully-adjacent layer (FA)

[p. 5-6] In Sections 4.2 to 4.4, extensively tuned models from previous work are taken, and the adjacency in the last layer is modified: given a GNN with $K$ layers, the $K$-th layer is modified to be a *fully-adjacent layer* (FA). A fully-adjacent layer is a GNN layer in which every pair of nodes is connected by an edge. In terms of Equations (1) to (3), converting an existing layer to be fully-adjacent means that $\mathcal{N}_v := \mathcal{V}$ for every node $v \in \mathcal{V}$, in that layer only. This does not change the type of layer nor add weights, but only changes adjacency of a data sample in a single layer. Thus, the $K - 1$ graph layers exploit the graph structure using their original sparse topology, and only the $K$-th layer is an FA layer that allows the topology-aware node-representations to interact directly and consider nodes beyond their original neighbors. The models are re-trained using the authors' original code, without performing *any* additional tuning, to rule out hyperparameter tuning as the source of improvement. Statistics of all datasets can be found in Appendix D.

[p. 6] The FA layer is noted as a *simple* solution, meant merely to demonstrate that over-squashing in GNNs is so prevalent and untreated that *even the simplest solution helps*. The main contribution is highlighting and explaining the over-squashing *problem*, opening the path for follow-up improvements and solutions.

### Data

[p. 6] The QM9 dataset (Ramakrishnan et al., 2014; Gilmer et al., 2017; Wu et al., 2018) contains ~130,000 graphs with ~18 nodes. Each graph is a molecule where nodes are atoms, and undirected, typed edges are different types of bonds between the atoms. The goal is to regress each graph to 13 real-valued quantum chemical properties such as *dipole moment* and *isotropic polarizability*.

### Models

[p. 6] The authors modified the implementation of Brockschmidt (2020) who performed an extensive hyperparameter tuning for multiple GNNs, by searching over 500 configurations; the same splits and best-found configurations are used. For most GNNs, Brockschmidt found that the best results are achieved using $K=8$ layers. This hints that the problem depends on long-range information and relies on both graph structure *and* distant nodes. Each modified model is re-trained for each target property using the same code, configuration, and training scheme as Brockschmidt (2020), training each model five times (using different random seeds) for each target property task. The "base" models, reported by Brockschmidt, are compared with the modified and re-trained "+FA" models.

### Results

[p. 6] Results for the top GNNs are shown in Table 1. The main results are that breaking the bottleneck by modifying a single layer to be an FA layer *significantly reduces the error rate*, by 42% on average, across six GNN types. Results for the other GNNs are shown in Appendix B due to space limitation.

### Over-squashing or under-reaching?

[p. 6] Barcelo et al. (2020) discuss the inability of a GNN node to observe nodes farther away than the number of layers $K$, termed *under-reaching*: for every fixed number of layers $K$, local information cannot travel farther than distance $K$ along edges. The authors measured the graphs' *diameter* in the QM9 dataset -- the maximum shortest path between any two nodes in a graph. The average diameter is 6.35 +/- 0.91, the maximum diameter is 10, and the 90th percentile is 8, while most models were trained with $K=8$ layers.

## Figure 3

**Figure 3** (p. 5): "Accuracy across problem radius (tree depth) in the NeighborsMatch problem. Over-squashing starts to affect GCN and GIN even at $r = 4$."

The figure shows a line plot with the x-axis being $r$ (the problem radius) ranging from 2 to 8, and the y-axis being Acc (accuracy) ranging from 0 to 1. Four lines are plotted for GGNN (train), GAT (train), GIN (train), and GCN (train). All four achieve ~1.0 accuracy at $r=2$ and $r=3$. At $r=4$, GCN drops to ~0.7 and GIN drops slightly, while GGNN and GAT remain at ~1.0. At $r=5$, all models drop significantly. By $r=7$-$8$, all models are near or below 0.2 accuracy.

## Table 1

**Table 1** (p. 6): "Average error rates (5 runs $\pm$ stdev for each property) on the QM9 dataset. The best result for every property in every GNN type is highlighted in bold. Results marked with $\dagger$ were previously reported by Brockschmidt (2020) and reproduced by us."

| Property | R-GIN base$^\dagger$ | R-GIN +FA | R-GAT base$^\dagger$ | R-GAT +FA | GGNN base$^\dagger$ | GGNN +FA |
|----------|---------------------|-----------|---------------------|-----------|---------------------|----------|
| mu | 2.64$\pm$0.11 | **2.54**$\pm$0.09 | **2.68**$\pm$0.06 | 2.73$\pm$0.07 | 3.85$\pm$0.16 | **3.53**$\pm$0.13 |
| alpha | 4.67$\pm$0.52 | **2.28**$\pm$0.04 | 4.65$\pm$0.44 | **2.32**$\pm$0.16 | 5.22$\pm$0.86 | **2.72**$\pm$0.12 |
| HOMO | 1.42$\pm$0.01 | **1.26**$\pm$0.02 | 1.48$\pm$0.03 | **1.43**$\pm$0.02 | 1.67$\pm$0.07 | **1.45**$\pm$0.04 |
| LUMO | 1.50$\pm$0.09 | **1.34**$\pm$0.04 | 1.53$\pm$0.07 | **1.41**$\pm$0.03 | 1.74$\pm$0.06 | **1.63**$\pm$0.06 |
| gap | 2.27$\pm$0.09 | **1.96**$\pm$0.04 | 2.31$\pm$0.06 | **2.08**$\pm$0.05 | 2.60$\pm$0.06 | **2.30**$\pm$0.05 |
| R2 | 15.63$\pm$1.40 | **12.61**$\pm$0.37 | 52.39$\pm$42.5 | **15.76**$\pm$1.17 | 35.94$\pm$35.7 | **14.33**$\pm$0.47 |
| ZPVE | 12.93$\pm$1.81 | **5.03**$\pm$0.36 | 14.87$\pm$2.88 | **5.98**$\pm$0.43 | 17.84$\pm$3.61 | **5.24**$\pm$0.30 |
| U0 | 5.88$\pm$1.01 | **2.21**$\pm$0.12 | 7.61$\pm$0.46 | **2.19**$\pm$0.25 | 8.65$\pm$2.46 | **3.35**$\pm$1.68 |
| U | 18.71$\pm$23.36 | **2.32**$\pm$0.18 | 6.86$\pm$0.53 | **2.11**$\pm$0.10 | 9.24$\pm$2.22 | **2.49**$\pm$0.34 |
| H | 5.62$\pm$0.81 | **2.26**$\pm$0.19 | 7.64$\pm$0.92 | **2.27**$\pm$0.29 | 9.35$\pm$0.96 | **2.31**$\pm$0.15 |
| G | 5.38$\pm$0.75 | **2.04**$\pm$0.24 | 6.54$\pm$0.36 | **2.07**$\pm$0.07 | 7.14$\pm$1.15 | **2.17**$\pm$0.29 |
| Cv | 3.53$\pm$0.37 | **1.86**$\pm$0.03 | 4.11$\pm$0.27 | **2.03**$\pm$0.14 | 8.86$\pm$9.07 | **2.25**$\pm$0.20 |
| Omega | 1.05$\pm$0.11 | **0.80**$\pm$0.04 | 1.48$\pm$0.87 | **0.73**$\pm$0.04 | 1.57$\pm$0.53 | **0.87**$\pm$0.09 |
| Relative: | | -39.54% | | -44.58% | | -47.42% |

The "+FA" column consistently outperforms the base model across nearly all properties for all three GNN types. The relative error reduction is -39.54% for R-GIN, -44.58% for R-GAT, and -47.42% for GGNN.

---
[p. 6–7 continued]

[p. 6-7] At least 90% of the examples in the dataset certainly did *not* suffer from under-reaching, because the number of layers was greater or equal to their diameter. The authors trained another set of models with 10 layers, which did not show an improvement over the base models. They conclude that the source of improvement was clearly *not* the increased reachability, but instead, the reduction in over-squashing.

### Can larger hidden sizes achieve a similar improvement?

[p. 7] The authors trained another set of models with *doubled* dimensions. These models achieved only 5.5% improvement over the base model (Appendix B.2), while adding the FA layer achieved 42% improvement using the original dimensions and without adding weights. Consistently, in Section 5 they present an analysis that shows how dimensionality increase is *ineffective* in preventing over-squashing.

### Is the entire FA layer needed?

[p. 7] The authors experimented with using only a sampled fraction of edges in the FA layer. As Appendix B.3 shows, the fraction of added edges in the last layer correlates with the decrease in error. For example, using only *half* of the possible edges in the last layer (a "semi-adjacent" layer) still reduces the error rate by 31.5% on average compared to "base".

### If all GNNs benefitted from direct interaction between all nodes, maybe graph structure is not even needed?

[p. 7] The authors trained another set of models (Appendix B.2) where *all K layers* are FA layers, thus ignoring the original graph topology; these models produced 1500% *higher* (worse) error.

