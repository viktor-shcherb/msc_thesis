# E Discussion: Over-Smoothing vs. Over-Squashing [p. 16]

[p. 16] Although *over-smoothing* and *over-squashing* are related, they are disparate phenomena that occur in different types of problems.

**Over-smoothing without over-squashing:** Consider a triangular graph containing only three nodes, where every node has a scalar value, an edge to each of the other nodes, and needs to compute a function of its own value and the other nodes' values. The problem radius in this case is $r=1$. As the number of layers is increased, the representations of the nodes might become indistinguishable, and thus suffer from *over-smoothing*. However, there will be *no over-squashing* in this case, because there is no growing amount of information that is squashed into fixed-sized vectors while passing long-range messages.

**Over-squashing without over-smoothing:** Contrarily, in the TREE-NEIGHBORSMATCH problem, there is no reason for over-smoothing to occur, because there are no two nodes that can converge to the same representation. A node in a "higher" level in the tree contains twice the information than a node in a "lower" level. Thus, this is a case where *over-squashing can occur without over-smoothing*.
