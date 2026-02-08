# Introduction [p. 1-2]

## GNNs and message passing

[p. 1] Graph neural networks (GNNs) (Gori et al., 2005; Scarselli et al., 2008; Micheli, 2009) have seen sharply growing popularity (Duvenaud et al., 2015; Hamilton et al., 2017; Xu et al., 2019). GNNs model complex structural data containing elements (nodes) with relationships (edges) between them, applicable to social networks, computer programs, chemical and biological systems.

A GNN layer can be viewed as a message-passing step (Gilmer et al., 2017), where each node updates its state by aggregating messages from direct neighbors. GNN variants (Li et al., 2016; Velickovic et al., 2018; Kipf and Welling, 2017) mostly differ in how each node aggregates neighbor representations with its own. Problems requiring interaction between non-directly-connected nodes achieve this by stacking multiple GNN layers. The required range of interaction between nodes is called the *problem radius*.

## Over-smoothing vs. over-squashing

[p. 1] In practice, GNNs were observed *not* to benefit from more than few layers. The accepted explanation is *over-smoothing*: node representations become indistinguishable when the number of layers increases (Wu et al., 2020). Over-smoothing was mostly demonstrated in *short-range* tasks (Li et al., 2018; Klicpera et al., 2018; Chen et al., 2020a; Oono and Suzuki, 2020; Zhao and Akoglu, 2020; Rong et al., 2020; Chen et al., 2020b) -- tasks with small *problem radii*, where a node's correct prediction mostly depends on its local neighborhood. Such tasks include paper subject classification (Sen et al., 2008) and product category classification (Shchur et al., 2018).

The authors hypothesize that in tasks depending on *long-range* information (larger problem radii), the explanation for limited performance is *over-squashing*, not over-smoothing. The differences between over-squashing and over-smoothing are further discussed in Section 6.

## The GNN bottleneck analogy

[p. 2] To allow a node to receive information from other nodes at a radius of $K$, the GNN needs at least $K$ layers, or otherwise it suffers from *under-reaching* -- distant nodes will not be aware of each other. However, as the number of layers increases, the number of nodes in each node's receptive field grows *exponentially*. This causes *over-squashing*: information from the exponentially-growing receptive field is compressed into fixed-length node vectors. The graph fails to propagate messages from distant nodes and learns only short-range signals.

The GNN bottleneck is analogous to the bottleneck of sequential RNN models. Traditional seq2seq models (Sutskever et al., 2014; Cho et al., 2014a,b) suffered from a bottleneck at every decoder state -- the model had to encapsulate the entire input sequence into a fixed-size vector. In RNNs, the receptive field grows *linearly* with the number of recursive applications. In GNNs, the bottleneck is asymptotically more harmful, because the receptive field grows *exponentially*. This difference is illustrated in Figure 1.

## Contributions

[p. 2] The paper's main contribution is introducing the *over-squashing* phenomenon -- a novel explanation for the major issue of training GNNs for long-range problems. The authors:
- Use a controlled problem to demonstrate how over-squashing prevents GNNs from fitting long-range patterns in the data
- Provide theoretical lower bounds for the required hidden size given the problem radius (Section 5)
- Show, analytically and empirically, that GCN (Kipf and Welling, 2017) and GIN (Xu et al., 2019) are susceptible to over-squashing *more* than other types of GNNs such as GAT (Velickovic et al., 2018) and GGNN (Li et al., 2016)
- Show that prior work on real-world datasets suffers from over-squashing: breaking the bottleneck using a simple fully adjacent layer reduces the error rate by 42% in QM9, by 12% in ENZYMES, by 4.8% in NCI1, and improves accuracy in VARMISUSE, without any additional tuning

## Figure 1

**Figure 1** (p. 2): "The bottleneck that existed in RNN seq2seq models (before attention) is strictly more harmful in GNNs: information from a node's exponentially-growing receptive field is compressed into a fixed-size vector. Black arrows are graph edges; red curved arrows illustrate information flow."

The figure has two panels: (a) The bottleneck of RNN seq2seq models -- showing a linear chain of nodes with arrows flowing into a single bottleneck vector. (b) The bottleneck of graph neural networks -- showing a tree-like graph structure with many nodes funneling information through edges into a single node, illustrating how information from an exponentially-growing receptive field must be compressed.
