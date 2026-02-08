# The GNN Bottleneck [p. 3-4]

## Problem radius and receptive field

[p. 3] Given a graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ and a given node $v$, the problem's required range of interaction, the *problem radius*, is denoted by $r$. $r$ is generally unknown in advance, and usually approximated empirically by tuning the number of layers $K$. The set of nodes in the receptive field of $v$ is denoted $\mathcal{N}_v^K$, defined recursively as $\mathcal{N}_v^1 := \mathcal{N}_v$ and $\mathcal{N}_v^K := \mathcal{N}_v^{K-1} \cup \{w \mid (w, u) \in \mathcal{E} \wedge u \in \mathcal{N}_v^{K-1}\}$.

## Over-squashing mechanism

[p. 3] When a prediction problem relies on long-range interaction, the GNN must have as many layers $K$ as the estimated range of these interactions (i.e., $K \geq r$), or otherwise distant nodes would not be able to interact. However, the number of nodes in each node's receptive field grows *exponentially* with the number of layers: $|\mathcal{N}_v^K| = \mathcal{O}(\exp(K))$ (Chen et al., 2018). As a result, an exponentially-growing amount of information is squashed into a fixed-length vector (the vector resulting from the $\sum$ in Equations (2) and (3)), and crucial messages fail to reach their distant destinations. The model learns only short-range signals from the training data and consequently might generalize poorly at test time.

## NeighborsMatch problem

[p. 3-4] **Example:** Consider the NeighborsMatch problem of Figure 2. Green nodes (A, B, C) have a varying number of blue neighbors and an alphabetical label. Each example in the dataset is a different graph that has a different mapping from numbers of neighbors to labels. The rest of the graph represents a general, unknown, graph structure. The goal is to predict a label for the target node (marked with a question mark), according to its number of blue neighbors. The correct answer is C in this case, because the target node has *two* blue neighbors, like the node marked with C in the same graph. Every example in the dataset has a different mapping from numbers of neighbors to labels, and thus message propagation and matching between the target node and all the green nodes must be performed *for every graph in the dataset*.

[p. 4] Since the model must propagate information from *all* green nodes before predicting the label, a bottleneck at the target node is inevitable. This bottleneck causes *over-squashing*, which can prevent the model from fitting the training data perfectly. The bottleneck is demonstrated empirically in Section 4; in Section 5, theoretical lower bounds for the GNN's hidden size are provided. Adding direct edges between the target node and the green nodes, or making edges bidirectional, could ease information flow for this specific problem. However, in real-life domains (e.g., molecules), the optimal message propagation structure is not known a priori, and the given relations (such as bonds between atoms) must be used as the graph's edges.

## Analogy to programming

[p. 4] Although contrived, the NeighborsMatch problem resembles real-world problems modeled as graphs. For example, a computer program in Python may declare multiple variables (the green nodes in Figure 2) along with their types and values (their numbers of blue neighbors); predicting which variable should be used in a specific location (predict the alphabetical label) must use one of the variables that are available in scope based on the required type and value. The authors experiment with this VARMISUSE problem in Section 4.4.

## Short- vs. long-range problems

[p. 4] Much of prior GNN work focused on problems that were local in nature, with small problem radii, where the underlying inductive bias was that a node's most relevant context is its local neighborhood. With the growing popularity of GNNs, their adoption expanded to domains requiring longer-range information propagation, without addressing the inherent bottleneck.

The paper focuses on problems that *require* long-range information -- that is, a correct prediction requires considering the local environment of a node *and* interactions beyond the close neighborhood. For example, a chemical property of a molecule (Ramakrishnan et al., 2014; Gilmer et al., 2017) can depend on the combination of atoms that reside on the molecule's *opposite sides*. Such problems require many GNN layers, and since the receptive field of each node grows exponentially with the number of layers, more layers means over-squashing is more harmful.

In problems that are local in nature (small $r$), the bottleneck is less troublesome, because a GNN can perform well with few layers (e.g., $K=2$ layers in Kipf and Welling (2017)). Domains such as citation networks (Sen et al., 2008), social networks (Leskovec and Mcauley, 2012), and product recommendations (Shchur et al., 2018) usually raise short-range problems and are thus *not* the focus of this paper.

## Figure 2

**Figure 2** (p. 3): "The NeighborsMatch: green nodes (A, B, C) have blue neighbors and an alphabetical label. The goal is to predict the label (A, B, or C) of the green node that has the same number of blue neighbors as the target node (?) in the same graph. In this example, the correct label is C, because the target node has *two* blue neighbors, like the node marked with C in the same graph."

The figure shows a graph with a target node (marked with ?) at the top, three green nodes labeled A, B, and C at the sides, each connected to varying numbers of blue neighbor nodes. The central subgraph (marked with a gear symbol) represents a general unknown graph structure connecting the target to the green nodes.
