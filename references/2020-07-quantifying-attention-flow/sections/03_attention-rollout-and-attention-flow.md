# 3 Attention Rollout and Attention Flow [p. 3–4]

[p. 3] Attention rollout and attention flow recursively compute the token attentions in each layer of a given model given the embedding attentions as input. They differ in the assumptions they make about how attention weights in lower layers affect the flow of information to the higher layers and whether to compute the token attentions relative to each other or independently.

## Residual connections

[p. 3] To compute how information propagates from the input layer to the embeddings in higher layers, it is crucial to take the residual connections in the model into account as well as the attention weights. In a Transformer block, both self-attention and feed-forward networks are wrapped by residual connections, i.e., the input to these modules is added to their output.

When we only use attention weights to approximate the flow of information in Transformers, we ignore the residual connections. But these connections play a significant role in tying corresponding positions in different layers.

To compute attention rollout and attention flow, the attention graph is augmented with extra weights to represent residual connections. Given the attention module with residual connection, values in layer $l+1$ are computed as:

$$V_{l+1} = V_l + W_{att} V_l$$

where $W_{att}$ is the attention matrix. Thus:

$$V_{l+1} = (W_{att} + I) V_l$$

[p. 3] To account for residual connections, an identity matrix is added to the attention matrix and the weights are re-normalized. This results in:

$$A = 0.5 W_{att} + 0.5 I$$

where $A$ is the raw attention updated by residual connections.

## Multi-head attention

[p. 3] Analyzing individual heads requires accounting for mixing of information between heads through a position-wise feed-forward network in Transformer block. Using attention rollout and attention flow, it is also possible to analyze each head separately (more details in Appendix A.1). However, in the paper's analysis, for simplicity, the attention at each layer is averaged over all heads.

## Attention rollout

[p. 3] Attention rollout is an intuitive way of tracking down the information propagated from the input layer to the embeddings in the higher layers. Given a Transformer with $L$ layers, the goal is to compute the attention from all positions in layer $l_i$ to all positions in layer $l_j$, where $j < i$.

In the attention graph, a path from node $v$ at position $k$ in $l_i$, to node $u$ at position $m$ in $l_j$, is a series of edges that connect these two nodes. The weight of each edge represents the proportion of information transferred between two nodes. To compute how much of the information at $v$ is propagated to $u$ through a particular path, we multiply the weights of all edges in that path. Since there may be more than one path between two nodes, to compute the total amount of information propagated from $v$ to $u$, we sum over all possible paths between these two nodes.

At the implementation level, the attention weights matrices in all the layers are recursively multiplied:

$$\tilde{A}(l_i) = \begin{cases} A(l_i) \tilde{A}(l_{i-1}) & \text{if } i > j \\ A(l_i) & \text{if } i = j \end{cases} \quad (1)$$

In this equation, $\tilde{A}$ is attention rollout, $A$ is raw attention, and the multiplication operation is a matrix multiplication. To compute input attention, we set $j = 0$. [p. 3]

## Attention flow

[p. 3–4] **Definition (flow network):** In graph theory, a flow network is a directed graph with a "capacity" associated with each edge. Formally, given $G = (V, E)$ is a graph, where $V$ is the set of nodes, and $E$ is the set of edges in $G$; $C = \{c_{uv} \in \mathbb{R} \mid \forall u, v \text{ where } e_{u,v} \in E \wedge u \neq v\}$ denotes the capacities of the edges and $s, t \in V$ are the source and target (sink) nodes respectively.

**Flow** is a mapping of edges to real numbers, $f : E \to \mathbb{R}$, that satisfies two conditions:
- (a) **capacity constraint**: for each edge the flow value should not exceed its capacity, $|f_{uv} \leq c_{uv}|$
- (b) **flow conservation**: for all nodes except $s$ and $t$ the input flow should be equal to output flow -- sum of the flow of outgoing edges should be equal to sum of the flow of incoming edges

Given a flow network, a maximum flow algorithm finds a flow which has the maximum possible value between $s$ and $t$ (Cormen et al., 2009).

[p. 4] Treating the attention graph as a flow network, where the capacities of the edges are attention weights, using any maximum flow algorithm, we can compute the maximum attention flow from any node in any of the layers to any of the input nodes.

> "In attention flow, the weight of a single path is the minimum value of the weights of the edges in the path, instead of the product of the weights." [p. 4]

The attention for node $s$ to node $t$ cannot be computed by simply adding up the weights of all paths between them, since there might be overlap between the paths and this might result in overflow in the overlapping edges.

## Computational complexity

[p. 4] Both proposed methods can be computed in polynomial time:
- **Attention rollout:** $O(d * n^2)$
- **Attention flow:** $O(d^2 * n^4)$

where $d$ is the depth of the model and $n$ is the number of tokens.

## Table 2

[p. 3]

**Table 2:** SpearmanR correlation of attention based importance with input gradients for 2000 samples from the test set for the verb number prediction model.

|         | L1             | L2             | L3             | L4             | L5             | L6             |
|---------|----------------|----------------|----------------|----------------|----------------|----------------|
| Raw     | 0.53+/-0.33    | 0.16+/-0.38    | -0.06+/-0.42   | 0.00+/-0.47    | 0.24+/-0.40    | 0.46+/-0.35    |
| Rollout | 0.22+/-0.31    | 0.27+/-0.32    | 0.39+/-0.32    | 0.47+/-0.32    | 0.53+/-0.32    | 0.54+/-0.31    |
| Flow    | 0.22+/-0.31    | 0.31+/-0.34    | 0.54+/-0.32    | 0.61+/-0.28    | 0.60+/-0.28    | 0.61+/-0.28    |

This is also the case when computing correlations with input gradients (Table 2): raw attention correlations are low except for the first layer.
