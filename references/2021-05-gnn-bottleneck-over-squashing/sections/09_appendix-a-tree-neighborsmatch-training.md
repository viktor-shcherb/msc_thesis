# A Tree-NeighborsMatch -- Training Details [p. 12-13]

## Figure 5

**Figure 5** (p. 12): "An example of a TREE-NEIGHBORSMATCH, that is an instance of the general NEIGHBORSMATCH problem that we examine in Section 4. The target node (?) is the root of a tree of $depth$=3 (from the target node to the green nodes). The green nodes (A, B, C, ...) have blue neighbors and an alphabetical label. The node B has a single blue neighbor; the node C has *two* blue neighbors; and the node D has no blue neighbors; each other green node has another unique number of blue neighbors. The goal it to predict a label for the target node (?) according to its number of blue neighbors. The correct answer is C in this example, because the target node has two blue neighbors, like the green node that is marked with C in the same graph. To make a correct prediction, the network must propagate information from *all* leaves toward the target node, and make the decision given a single fixed-sized vector that compresses all this information."

The figure shows a binary tree of depth 3 rooted at the target node (marked with ?). The tree has 8 leaf nodes labeled A through H. Each leaf node has a varying number of blue circle neighbors below it: A has a few, B has one, C has two, D has none, E through H have varying numbers. The target node at the root also has blue neighbors. Edges are directed upward toward the root.

## Data

[p. 12] A separate dataset is created for every tree depth (which is equal to $r$, the problem radius), and sampled up to 32,000 examples per dataset. The label of each leaf ("A", "B", "C" in Figure 2) is represented as a one-hot vector. To tease the effect of the bottleneck from the ability of a GNN to count neighbors, they concatenated each leaf node's initial representation with a 1-hot vector representing the number of blue neighbors, instead of creating the blue nodes. The target node is initialized with a learned vector as its (missing) label, concatenated with a 1-hot vector representing its number of blue neighbors. Intermediate nodes are initialized with another learned vector.

## Model

[p. 12] The network has an initial linear layer, followed by $r + 1$ GNN layers. Afterward, the final target node representation goes through a linear layer and a softmax to predict its label. They experimented with GCN (Kipf and Welling, 2017), GGNN (Li et al., 2016), GIN (Xu et al., 2019) and GAT (Velickovic et al., 2018) as the graph layers.

[p. 13] In Section 4.1, model dimensions of $d=32$ were used. Larger values led to the exact same trend. Residual connections were added, summing every node with its own representation in the previous layer to increase expressivity, and layer normalization was used which eased convergence. The Adam optimizer was used with a learning rate of $10^{-3}$, decayed by 0.5 after every 1000 epochs without an increase in training accuracy, and stopped training after 2000 epochs of no training accuracy improvement. This usually led to tens of thousands of training epochs, sometimes reaching 100,000 epochs.

## Hyperparameter tuning

[p. 13] To rule out hyperparameter tuning as the source of degraded performance, they experimented with changing activations (ReLu, tanh, MLP, none), using layer normalization and batch normalization, residual connections, various batch sizes, and whether or not the same GNN weights should be "unrolled" over time steps. The presented results were obtained using the configurations that achieved the best results.

## Over-squashing or just long-range?

[p. 13] To rule out the possibility that the long-range itself is preventing the GNNs from fitting the data, they repeated the experiment of Figure 3 for depths 4 to 8, where the distance between the leaves and the target node remained the same, but the amount of over-squashing was as in $r=2$. That is, the graph looks like a tree of $depth=2$, where the root is connected to a "chain" of length of up to 6, and the target node is at the other side of the chain. This setting maintains the long-range as in the original problem, but reduces the amount of information that needs to be squashed. This setting *disentangles* the effect of the long-range itself from the effect of the growing amount of information (i.e., from over-squashing). In this setting, *all GNN types managed to easily fit the data to close to 100%* across all distances, showing that the problem is the amount of over-squashing, rather than the long-range itself.
