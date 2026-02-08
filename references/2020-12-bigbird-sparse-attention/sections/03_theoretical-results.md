# 3 Theoretical Results about Sparse Attention Mechanism [p. 4-6]

[p. 4-5] The authors show that sparse attention mechanisms are as powerful and expressive as full-attention mechanisms in two respects:
1. When sparse attention mechanisms are used in a standalone encoder (such as BERT), they are Universal Approximators of sequence to sequence functions in the style of Yun et al. [104]. This property was also explored theoretically in contemporary work Yun et al. [105].
2. Unlike [105], they further show that sparse encoder-decoder transformers are Turing Complete (assuming the same conditions defined in [72]).

Complementing these positive results, they also show that moving to a sparse-attention mechanism incurs a cost (no free lunch): in Sec. 3.4 they exhibit a natural task where any sufficiently sparse mechanism will require polynomially more layers.

## 3.1 Notation [p. 5]

The complete Transformer *encoder* stack is the repeated application of a single-layer encoder (with independent parameters). The class of such Transformer encoder stacks, defined using the generalized encoder (Sec. 2), is denoted by T_D^{H,m,q} which consists of H-heads with head size m and q is the hidden layer size of the output network, and the attention layer is defined by the directed graph D.

The key difference from Vaswani et al. [91] and Yun et al. [104] is the addition of a special token at the beginning of each sequence, assigned a special vector. This is referred to as x_0. Therefore graph D will have vertex set {0} union |n| = {0, 1, 2, ..., n}. This extra node and its respective vector will be dropped at the final output layer of transformer. [p. 5]

To avoid cumbersome notation, they still treat transformer as mapping sequences X in R^{n x d} to R^{n x d}. They also allow the transformer to append position embeddings E in R^{d x n} to matrix X in the input layer.

### Function class for universal approximation

[p. 5] F_{CD} denotes the set of continuous functions f : [0,1]^{n x d} -> R^{n x d} which are continuous with respect to the topology defined by the l_p norm. For any p >= 1, the l_p distance is:

d_p(f_1, f_2) = ( integral ||f_1(X) - f_2(X)||_p^p dX )^{1/p}

## 3.2 Universal Approximators [p. 5]

**Definition 1.** *The star-graph S centered at 0 is the graph defined on {0, ..., n}. The neighborhood of all vertices i is N(i) = {0, i} for i in {1 ... n} and N(0) = {1, ... n}.* [p. 5]

The main theorem is that the sparse attention mechanism defined by any graph containing the star graph S is a universal approximator:

**Theorem 1.** *Given 1 < p < infinity and epsilon > 0, for any f in F_{CD}, there exists a transformer with sparse-attention, g in T_D^{H,m,q} such that d_p(f, g) <= epsilon where D is any graph containing star graph S.* [p. 5]

### Proof outline (three steps)

[p. 5-6]

**Step 1: Approximate F_{CD} by piece-wise constant functions.** Since f is a continuous function with bounded domain [0,1]^{n x d}, approximate it with a suitable piece-wise constant function. This is accomplished by a suitable partition of the region [0,1) into a grid of granularity delta to get a discrete set G_delta. Therefore they deal with a function f_hat : G_delta -> R^{n x d}, where d_p(f, f_hat) <= epsilon/3. [p. 5]

**Step 2: Approximate piece-wise constant functions by modified transformers.** This is the key step where the self-attention mechanism is used to generate a *contextual-mapping* of the input. A contextual mapping is a unique code for the pair consisting of a matrix (X, x_i) and a column. Its uniqueness allows the Feed forward layers to use each code to map it to a unique output column. [p. 5]

The main technical challenge is computing the contextual mapping using only sparse attention mechanism. This was done in [104] using a "selective" shift operator which shifts entries in a specific interval. Key to their proof was that the shift was exactly the range of the largest entry to the smallest entry.

Creating a contextual mapping with a sparse attention is a challenge because each query only attends to a few keys, so it is not clear that sufficient information can be corralled to make a contextual embedding of the entire matrix. The authors develop a sparse shift operator which shifts the entries of the matrices if they lie in a certain range. The exact amount of the shift is controlled by the directed sparse attention graph D. The second key ingredient is the use of additional global token. By carefully applying the operator to a set of chosen ranges, each column will contain a unique mapping of the full mapping. Therefore, they augment the loss of inner-products in the self attention mechanism by using multiple layers and an auxiliary global token. [p. 5]

**Step 3: Approximate modified transformers by original Transformers.** The final step is to approximate the modified transformers by the original transformer which uses ReLU and softmax. Full details in App. A. [p. 6]

## 3.3 Turing Completeness [p. 6]

[p. 6] Transformers are a very general class. In the original paper of Vaswani et al. [91], they were used in both an encoder and a decoder. Perez et al. [72] showed that the full transformer based on a quadratic attention mechanism is Turing Complete. This result makes one unrealistic assumption: the model works on arbitrary precision. This is necessary as otherwise, Transformers are bounded finite state machines and cannot be Turing Complete.

The authors show that a sparse attention mechanism can also be used to simulate any Turing Machine: they can use a sparse encoder and sparse decoder to simulate any Turing Machine.

To use the sparse attention mechanism in the transformer architecture, a suitable modification is needed where each token only reacts to previous tokens. Unlike BERT where the entire attention mechanism is applied once, in full transformers the sparse attention mechanism at the decoder side is used token by token. Perez et al. [72] uses each token as a representation of the tape history and uses the full attention to move and retrieve the correct tape symbol. Most of the construction of Perez et al. [72] goes through for sparse attentions, except for their addressing scheme to point back in history (Lemma B.4 in [72]). The authors show how to simulate this using a sparse attention mechanism and defer details to App. B. [p. 6]

## 3.4 Limitations [p. 6]

[p. 6] A natural task is demonstrated which can be solved by the full attention mechanism in O(1)-layers. However, under standard complexity theoretic assumptions, this problem requires Omega(n)-layers for any sparse attention layers with O_tilde(n) edges (not just BIGBIRD). (Here O_tilde hides poly-logarithmic factors.)

**Task 1.** Given n unit vectors {u_1, ..., u_n}, find f(u_1, ..., u_n) -> (u_{1*}, ..., u_{n*}) where for a fixed j in [n], we define j* = arg max_k ||u_k - u_j||_2^2. [p. 6]

Finding vectors that are furthest apart boils down to minimizing inner product search in the case of unit vectors. For a full-attention mechanism with appropriate query and keys, this task is very easy as we can evaluate all pair-wise inner products.

The impossibility for sparse-attention follows from hardness results stemming from the Orthogonal Vector Conjecture (OVC) [1, 2, 7, 96]. The OVC is a widely used assumption in fine-grained complexity. Informally, it states that one cannot determine if the minimum inner product among n boolean vectors is 0 in subquadratic time. In App. C, a reduction using OVC shows that if a transformer g in T_D^{H=1, m=2d, q=0} for any sparse directed graph D can evaluate Task 1, it can solve the orthogonal vector problem.

**Proposition 1.** *There exists a single layer full self-attention g in T^{H=1, m=2d, q=0} that can evaluate Task 1, i.e. g(u_1, ..., u_n) = [u_{1*}, ..., u_{n*}], but for any sparse-attention graph D with O_tilde(n) edges (i.e. inner product evaluations), would require Omega_tilde(n^{1-o(1)}) layers.* [p. 6]

A formal proof is given in App. C.
