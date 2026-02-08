# 2 BIGBIRD Architecture [p. 3-4]

## Generalized attention mechanism

[p. 3] The BIGBIRD model uses a **generalized attention mechanism** in each layer of the transformer operating on an input sequence X = (x_1, ..., x_n) in R^{n x d}.

The **generalized attention mechanism** is described by a directed graph D whose vertex set is |n| = {1, ..., n}. The set of arcs (directed edges) represent the set of inner products that the attention mechanism will consider. Let N(i) denote the out-neighbors set of node i in D, then the i-th output vector of the generalized attention mechanism is defined as:

**Equation (AT):**

ATTN_D(X)_i = x_i + sum_{h=1}^{H} sigma( Q_h(x_i) K_h(X_{N(i)})^T ) . V_h(X_{N(i)})

where Q_h, K_h : R^d -> R^m are query and key functions respectively, V_h : R^d -> R^d is a value function, sigma is a scoring function (e.g. softmax or hardmax), and H denotes the number of heads. X_{N(i)} corresponds to the matrix formed by only stacking {x_j : j in N(i)} and not all the inputs. [p. 3]

If D is the complete digraph, we recover the full quadratic attention mechanism of Vaswani et al. [91].

## Adjacency matrix formulation

[p. 3] To simplify exposition, the authors operate on the adjacency matrix A of graph D even though the underlying graph may be sparse. A in [0,1]^{n x n} with A(i,j) = 1 if query i attends to key j and is zero otherwise. When A is the ones matrix (as in BERT), it leads to quadratic complexity, since all tokens attend on every other token.

The problem of reducing the quadratic complexity of self-attention can now be seen as a **graph sparsification problem**.

## Component 1: Random attention

[p. 3] Random graphs are expanders and can approximate complete graphs in a number of different contexts including in their spectral properties [80, 38]. The authors consider the simplest random graph construction, known as the Erdos-Renyi model, where each edge is independently chosen with a fixed probability. In such a random graph with just Theta(n) edges, the shortest path between any two nodes is logarithmic in the number of nodes [17, 43]. As a consequence, such a random graph approximates the complete graph spectrally and its second eigenvalue (of the adjacency matrix) is quite far from the first eigenvalue [9, 10, 6]. This leads to rapid mixing time for random walks, informally suggesting that information can flow fast between any pair of nodes.

The authors propose a sparse attention where each query attends to r random number of keys, i.e. A(i, .) = 1 for r randomly chosen keys (see Fig. 1a). [p. 3]

## Component 2: Window (local) attention

[p. 4] The second viewpoint is that most contexts within NLP and computational biology display a great deal of **locality of reference**: a great deal of information about a token can be derived from its neighboring tokens. Clark et al. [19] investigated self-attention models in NLP tasks and concluded that neighboring inner-products are extremely important.

In the terminology of graph theory, clustering coefficient is a measure of locality of connectivity, and is high when the graph contains many cliques or near-cliques. Simple Erdos-Renyi random graphs do not have a high clustering coefficient [84], but small world graphs exhibit high clustering coefficient [94]. A particular model introduced by Watts and Strogatz [94] achieves a good balance between average shortest path and locality. The generative process: Construct a regular ring lattice, a graph with n nodes each connected to w neighbors, w/2 on each side.

A random subset (k%) of all connections is replaced with a random connection. The other (100 - k)% local connections are retained. However, deleting random edges might be inefficient on modern hardware, so BIGBIRD retains them.

BIGBIRD defines a sliding window attention of width w: query at location i attends from i - w/2 to i + w/2 keys. In notation: A(i, i - w/2 : i + w/2) = 1 (see Fig. 1b). [p. 4]

## Figure 1 (p. 3)

**Figure 1:** Building blocks of the attention mechanism used in BIGBIRD. White color indicates absence of attention. (a) random attention with r = 2, (b) sliding window attention with w = 3, (c) global attention with g = 2. (d) the combined BIGBIRD model.

The figure shows four adjacency matrices as heatmaps:
- (a) Random attention: scattered colored cells in a mostly white matrix
- (b) Window attention: a diagonal band of colored cells
- (c) Global attention: two full rows and two full columns highlighted
- (d) BIGBIRD: combination of all three patterns

## Table 1 (p. 4)

**Table 1:** Building block comparison @512

| Model      | MLM  | SQuAD | MNLI |
|------------|------|-------|------|
| BERT-base  | 64.2 | 88.5  | 83.4 |
| Random (R) | 60.1 | 83.0  | 80.2 |
| Window (W) | 58.3 | 76.4  | 73.1 |
| R + W      | 62.7 | 85.1  | 80.5 |

[p. 4] An initial sanity check: random blocks and local window alone were insufficient to capture all the context necessary to compete with BERT's performance, while keeping attention linear in the number of tokens.

## Component 3: Global tokens

[p. 4] The final piece of BIGBIRD is inspired from the theoretical analysis (Sec. 3), and is critical for empirical performance. The theory utilizes the importance of "global tokens" (tokens that attend to all tokens in the sequence and to whom all tokens attend; see Fig. 1c). These global tokens can be defined in two ways:

- **BIGBIRD-ITC (Internal Transformer Construction):** Make some existing tokens "global", which attend over the entire sequence. Concretely, choose a subset G of indices (with g := |G|), such that A(i, :) = 1 and A(:, i) = 1 for all i in G.

- **BIGBIRD-ETC (Extended Transformer Construction):** Include additional "global" tokens such as CLS. Concretely, add g global tokens that attend to all existing tokens. In notation, create a new matrix B in [0,1]^{(N+g) x (N+g)} by adding g rows to matrix A, such that B(i, :) = 1, and B(:, i) = 1 for all i in {1, 2, ... g}, and B(g + i, g + j) = A(i, j) for all i, j in {1, ..., N}. This adds extra location to store context and improves performance. [p. 4]

## Combined mechanism

[p. 4] The final attention mechanism for BIGBIRD (Fig. 1d) has all three properties: queries attend to r random keys, each query attends to w/2 tokens to the left and w/2 to the right of its location, and they contain g global tokens (either from existing tokens or extra added tokens). Implementation details in App. D.
