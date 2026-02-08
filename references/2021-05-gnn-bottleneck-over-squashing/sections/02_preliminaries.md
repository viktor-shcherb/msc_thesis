# Preliminaries [p. 2-3]

## Graph definition

[p. 2] A directed graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ contains nodes $\mathcal{V}$ and edges $\mathcal{E}$, where $(u, v) \in \mathcal{E}$ denotes an edge from node $u$ to node $v$. For brevity, all edges are treated as having the same *type*; in general, every edge can have a type and features (Schlichtkrull et al., 2018).

## Graph neural networks

[p. 2-3] GNNs operate by propagating neural messages between neighboring nodes. At every propagation step (a graph layer): the network computes each node's sent message; every node aggregates its received messages; and each node updates its representation by combining the aggregated incoming messages with its own previous representation.

Each node is associated with an initial representation $\mathbf{h}_v^{(0)} \in \mathcal{R}^{d_0}$, usually derived from the node's label or its given features. A GNN layer updates each node's representation given its neighbors, yielding $\mathbf{h}_v^{(1)} \in \mathcal{R}^d$. In general, the $k$-th layer of a GNN is a parametric function $f_k$ applied to each node by considering its neighbors:

$$\mathbf{h}_v^{(k)} = f_k\left(\mathbf{h}_v^{(k-1)}, \{\mathbf{h}_u^{(k-1)} \mid u \in \mathcal{N}_v\}; \theta_k\right) \tag{1}$$

where $\mathcal{N}_v$ is the set of nodes that have edges to $v$: $\mathcal{N}_v = \{u \in \mathcal{V} \mid (u, v) \in \mathcal{E}\}$. The total number of layers $K$ is usually determined empirically as a hyperparameter.

## GCN update rule

[p. 3] The design of the function $f$ is what mostly distinguishes one type of GNN from the other. Graph convolutional networks (GCN) define $f$ as:

$$\mathbf{h}_v^{(k)} = \sigma\left(\sum_{u \in \mathcal{N}_v \cup \{v\}} \frac{1}{c_{u,v}} W^{(k)} \mathbf{h}_u^{(k-1)}\right) \tag{2}$$

where $\sigma$ is a nonlinearity such as $ReLU$, and $c_{u,v}$ is a normalization factor often set to $\sqrt{|\mathcal{N}_v| \cdot |\mathcal{N}_u|}$ or $|\mathcal{N}_v|$ (Hamilton et al., 2017).

## GIN update rule

[p. 3] Graph isomorphism networks (GIN) (Xu et al., 2019) update a node's representation using:

$$\mathbf{h}_v^{(k)} = MLP^{(k)}\left(\left(1 + \epsilon^{(k)}\right) \mathbf{h}_v^{(k-1)} + \sum_{u \in \mathcal{N}_v} \mathbf{h}_u^{(k-1)}\right) \tag{3}$$

## Prediction

[p. 3] Usually, the last ($K$-th) layer's output is used for prediction: in node-prediction, $\mathbf{h}_v^{(K)}$ is used to predict a label for $v$; in graph-prediction, a permutation-invariant "readout" function aggregates the nodes of the final layer using summation, averaging, or a weighted sum (Li et al., 2016).
