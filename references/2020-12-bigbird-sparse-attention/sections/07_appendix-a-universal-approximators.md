# A Universal Approximators [p. 17-21]

## A.1 Notation [p. 17]

[p. 17] The notation follows Perez et al. [72] to formally describe the complete architecture of Transformers. A single layer of Transformer encoder is a parametric function Enc receiving a sequence **X** = (**x**_1, ..., **x**_n) of vectors in R^d and returning a sequence **Z** = (**z**_1, ..., **z**_n) of the same length. Each **z**_i is a d-dimensional vector. The sequence **X** is interchangeably treated as a matrix in R^{n x d}. Enc has two components:

1. An attention mechanism ATTN that takes in the sequence **X** and returns sequence (**a**_1, ..., **a**_n) of the same length and dimensionality; and
2. A two layer fully connected network O that takes in a vector in R^d and returns a vector in R^d.

Then the i-th output vector of Enc(**X**) is computed as follows:

**Equation (1):**

z_i = O(**a**_i) + **a**_i     where     **a**_i = ATTN(**X**)_i + **x**_i

[p. 17] As described in Sec. 2, an attention mechanism is parameterized by three functions: Q, K, V : R^d -> R^m. In this paper, they assume these are simply matrix products: Q(**x**) = **x**W_Q, K(**x**) = **x**W_K, and V(**x**) = **x**W_V, where W_Q, W_K, W_V in R^{d x m} and W_V in R^{d x d}. In reality a multi-headed attention is used, i.e. not only one, but H-sets of Query/Key/Value weight matrices, W_Q^h, W_V^h, W_K^h for h = 1, ..., H. Thus, for a directed graph D over [n], the i^th output vector of the generalized attention mechanism would be:

**Equation (AT):**

ATTN_D(**X**)_i = sum_{h=1}^{H} sigma( (**x**_i W_Q^h)(**X**_{N(i)} W_K^h)^T ) . (**X**_{N(i)} W_V^h)

where N(i) denotes the out-neighbors set of node i in D. In other words, the set of arcs (directed edges) in D represents the set of inner products that the attention mechanism will consider. sigma is a scoring function such as softmax or hardmax. [p. 17]

The output fully connected network is defined as follows:

**Equation (FF):**

O(**a**_i) = ReLU(**a**_i W_1 + b_1) W_2 + b_2

Here W_1 in R^{d x q}, W_2 in R^{q x d}, b_1 in R^p, and b_2 in R^d are parameters of output network O. [p. 17]

### Additional Notation

[p. 17] [a, b)_delta = {a, a + delta, ..., a + floor((b - a) / delta) . delta}. Therefore, [0, 1)_delta = {0, delta, 2*delta, ..., (1 - delta)}. **1**[E] is used to denote the indicator variable; it is 1 if the event E occurs and 0 otherwise.

## A.2 Proof [p. 17-20]

[p. 17] This section presents the full proof of Theorem 1. The proof contains three parts. The first and the third part largely follow standard techniques. The main innovation lies in the second part.

### A.2.1 Approximate F_{CD} by piece-wise constant functions [p. 17-18]

[p. 17] First, consider a suitable partition of the region (0, 1) into a grid of granularity delta, denoted by G_delta. This is done using Lemma 8 from Yun et al. [104], restated for completeness:

**Lemma 1** (Lemma 8 [104]). *For any given f in F_{CD} and 1 <= p <= infinity, there exists a delta > 0 such that there exists a piece-wise constant function f_hat with d_p(f, f_hat) <= epsilon/3. Concretely, f_hat is defined as*

f_hat(X) = sum_{P in G_delta} f(P) . **1**[||ReLU(X - P)||_infinity <= delta]

[p. 18] Since transformers can learn a positional embedding E, without any loss of generality, we can consider the translated function. In particular, define

E = [ 0           0              0            ...  0;
      delta^{-d}  delta^{-d}     delta^{-d}   ...  delta^{-d};
      delta^{-2d} delta^{-2d}    delta^{-2d}  ...  delta^{-2d};
      ...
      delta^{-(n-1)d}  delta^{-(n-1)d}  delta^{-(n-1)d}  ...  delta^{-(n-1)d} ]

We will try to approximate g(X) = f(X - E) where g is defined on the domain [0, 1]^d x [delta^{-d}, delta^{-d} + 1]^d x ... x [delta^{-(n-1)d}, delta^{-(n-1)d} + 1]^d. To do so, a suitable modification of Lemma 1 is applied, which will consider the discretized grid:

**G**_delta^E := [0, 1]_delta^d x [delta^{-d}, delta^{-d} + 1]_delta^d x ... x [delta^{-(n-1)d}, delta^{-(n-1)d} + 1]_delta^d

Therefore, it suffices to approximate a function f_hat : **G**_delta^E -> R^{n x d} defined as

f_hat(X) = sum_{P in **G**_delta^E} f(P - E) . **1**[||ReLU(X - P)||_infinity <= delta].

### A.2.2 Contextual Mappings and Sparse Attention Mechanisms [p. 18-20]

[p. 18] Throughout this section, the assumption is that there is a function that has an extra global token at index 0 and all vectors have an extra dimension appended to them. The latter assumption is without loss of generality as the Feed-Forward Network can be used to append sparse dimensions. In particular, associate X in R^{(n+1) x (d+1)} where we write X = (x_0, x_1, ..., x_n). Although the function is only defined for **G**_delta^E subset R^{n x d}, we can amend the function in a natural way by making it ignore the first column. To avoid excessive clutter, the assumption is that the function value is evaluated on the last n columns.

[p. 18] The main idea in this section is the use of contextual mapping to enable Transformers to compute any discretized function. A contextual mapping is a unique encoding of each tuple (X, x_i) where X in **G**_delta^E, and each column x_i in [delta^{-(i-1)d}, delta^{-(i-1)d} + 1]_delta^d for all i in [n]. The definition (restated from Defn 3.1 [104]) is adapted to this setting:

**Definition 2** (Defn 3.1 [104]). *(Contextual Mapping) A contextual mapping is a function mapping q : **G**_delta^E -> R^n if it satisfies the following:*

1. *For any P in **G**_delta^E, q(P) contains distinct entries.*
2. *For any two P, P' in **G**_delta^E with P != P', all entries of q(P) and q(P') are distinct.*

[p. 18] The key technical novelty of the proof is computing a contextual mapping using only the sparse attention mechanism. A "selective shift" operator is created which only shifts entries of a vector that lie in a certain range. This shift operator is used strategically to ensure that a contextual mapping is attained at the end of the process. The lemma below, based on parts of the proof of Lemma 6 of [104], states that a suitable "selective" shift operator can be implemented using a sparse attention mechanism.

**Lemma 2.** *Given a function psi : R^{(n+1) x (d+1)} x R^2 -> R^{(n+1) x 1} and a vector u in R^{d+1} and a sparse attention mechanism based on the directed graph D, we can implement a selective shift operator that receives as input a matrix X in R^{(n+1) x (d+1)} and outputs X + rho . psi_u(X, b_1, b_2) where*

psi_u(Z; b_1, b_2)_i = { (max_{j in N(i)} u^T Z_j - min_{j in N(i)} u^T Z_j) e_1    if b_1 <= u^T Z_j <= b_2
                        { 0                                                             else.

*Note that e_1 in R^{d+1} denotes (1, 0, ..., 0).* [p. 18]

*Proof.* [p. 18-19] Consider the function, which can be implemented by a sparse attention mechanism:

psi_tilde(X, b)_i = sigma_H [ (u^T . X_i)^T . (u^T X_{N(i)} - b **1**^T_{N(i)}) e^{(1)}(u^T X_{N(i)}) ]

This is because the Key, Query and Value functions are simply affine transformations of X. [p. 19]

Given any graph D, the above function will evaluate to the following:

psi_tilde(Z; b)_i = { (max_{j in N(i)} u^T Z_j) e_1    if u^T Z_j > b
                     { (min_{j in N(i)} u^T Z_j) e_1    if u^T Z_j < b

Therefore psi_tilde(Z; b_Q) - psi_tilde(Z; b_{Q'}) satisfies

psi(Z; b_1, b_2)_i = { (max_{j in N(i)} u^T Z_j - min_{j in N(i)} u^T Z_j) e_1    if b_1 <= u^T Z_j <= b_2
                      { 0                                                             else.

This completes the proof of Lemma 2. [p. 19]

**Lemma 3.** *There exists a function g_c : R^{(n+1) x (d+1)} -> R^{(n+1)} and a unique vector u, such that for all P in **G**_delta^E, g_c(P) := <u, g(P)> satisfies the property that g_c is a contextual mapping of P. Furthermore, g_c in T_D^{2,1} using a composition of sparse attention layers as long as D contains the star graph.* [p. 19]

*Proof.* [p. 19] Define u in R^{d+1} = [1, delta^{-1}, delta^{-2}, ..., delta^{-d+1}, delta^{-nd}] and let X_0 = (0, ..., 0, 1). We will assume that <x_i, x_0> = 0, by assuming that all the columns x_1, ..., x_n are appended by 0.

To successfully encode the entire context in each token, the shift operator is interleaved to target the original columns 1, ..., n and to target the global column 0. After a column i is targeted, its inner product with u will encode the entire context of the first i columns. Next, the global token is shifted to take this context into account. This can be subsequently used by the remaining columns.

[p. 19] For i in {0, 1, ..., n}, l_i denotes the inner products <u, x_i> at the beginning. For f_i = <u, x_i> after the i^th column has changed for i in {1, ..., n} and f_0^k is used to denote <u, x_0> after the k^th phase. Initially, given X in **G**_delta^E, the following are true:

delta^{-(i-1)d} <= <u, X_i> <= delta^{-id} - delta       for all i in [n]

delta^{-(n+1)d} = <u, X_0>

Note that all l_i are ordered in distinct buckets l_1 < l_2 < ... < l_n < l_0.

The operation is done in phases indexed from i in {1, ..., n}. Each phase consists of two distinct parts:

**The low shift operation:** These operations will be of the form

X <- X + delta^{-d} psi(X, v - delta/2, v + delta/2)

for values v in [delta^{-id}, delta^{-(i+1)d})_delta. The range is chosen so that only l_i will be in the range and no other l_j, j != i, is in the range. This will shift exactly the i^th column x_i so that the new inner product f_i = <u, x_i> is substantially larger than l_i. Furthermore, no other column of X will be affected. [p. 19]

**The high shift operation:** These operations will be of the form

X <- X + delta^{-nd} . psi(X, v - delta/2, v + delta/2)

for values v in [S_i, T_i]_delta. The range [S_i, T_i]_delta is chosen to only affect the column x_0 (corresponding to the global token) and no other column. In particular, this will shift the global token by a further delta^{-nd}. Let f_0^i denote the value of f_0^i = <u, x_0> at the end of i^th high operation. [p. 19]

Each phase interleaves a shift operation to column i and updates the global token. After each phase, the updated i^th column f_i = <u, x_i> will contain a unique token encoding the values of all the l_1, ..., l_i. After the high update, f_0^i = <u, x_0> will contain information about the first i tokens.

Finally, the following constants are defined for all k in {0, 1, ..., n}:

**Equation (UP):**

T_k = (delta^{-(n+1)d} + 1)^k . delta^{-nd} - sum_{t=2}^{k} (delta^{-(n+1)d} + 1)^{k-t} (2*delta^{-nd-d} + delta^{-nd} + 1) delta^{-td}
      - (delta^{-(n+1)d} + 1)^{k-1} (delta^{-nd-d} + delta^{-nd}) delta^{-d} - delta^{-(k+1)d}

[p. 20]

**Equation (LP):**

S_k = (delta^{-(n+1)d} + 1)^k . delta^{-nd} - sum_{t=2}^{k} (delta^{-(n+1)d} + 1)^{k-t} (2*delta^{-nd-d} + delta^{-nd} + 1) delta^{-(t-1)d}
      - (delta^{-(n+1)d} + 1)^{k-1} (delta^{-nd-d} + delta^{-nd}) - delta^{-kd}

After each k phases, the following invariants are maintained:

1. S_k < f_0^k < T_k for all k in {0, 1, ..., n}.
2. T_{k-1} <= f_k < S_k
3. The order of the inner products after k^th phase is

   l_{k+1} < l_{k+2} ... < l_n < f_1 < f_2 < ... < f_k < f_0^k.

**Base case** [p. 20] The case k = 0 is trivial as we simply set S_0 = delta^{-(n+1)d}, T_0 = delta^{-(n+1).d} + delta.

The first nontrivial case is k = 1.

**Inductive Step** [p. 20] First, in the low shift operation is performed in the range [delta^{-(k-1)d}, delta^{-kd})_delta. Due to the invariant, there exists only one column x_k that is affected by this shift. In particular, for column k, we will have max_{j in N(k)} <u, x_j> = <u, x_0> = f_0^{k-1}. The minimum is l_k. Thus the update will be f_k = delta^{-d}(f_0^{k-1} - l_k) + l_k. Observe that for small enough delta, f_k >= f_0^{k-1}. Hence the total ordering, after this operation is

**Equation (2):**

l_{k+1} < l_{k+2} ... < l_n < f_1 < f_2 < ... < f_0^{k-1} < f_k

[p. 20] Now when we operate a higher selective shift operator in the range [S_{k-1}, T_{k-1})_delta. Since only global token's innerproduct f_0^{k-1} is in this range, it will be the only column affected by the shift operator. The global token operates over the entire range, so from Eq. (2), f_k = max_{i in [n]} <u, x_i> and l_{k+1} = min_{i in [n]} <u, x_i>. The new value f_0^k = delta^{-nd} . (f_k - l_{k+1}) + f_0^{k-1}. Expanding and simplifying:

f_0^k = delta^{-nd} . (f_k - l_{k+1}) + f_0^{k-1}
      = delta^{-nd} . (delta^{-d}(f_0^{k-1} - l_k) + l_k - l_{k+1}) + f_0^{k-1}
      = delta^{-(n+1)d} . (f_0^{k-1} - l_k) + delta^{-nd}(l_k - l_{k+1}) + f_0^{k-1}
      = (delta^{-(n+1)d} + 1) f_0^{k-1} - (delta^{-nd-d} + delta^{-nd}) l_k - l_{k+1}

Expanding the above recursively:

f_0^k = (delta^{-(n+1)d} + 1)^k . f_0^0 - sum_{t=2}^{k} (delta^{-(n+1)d} + 1)^{k-t} (2*delta^{-nd-d} + delta^{-nd} + 1) l_t
        - (delta^{-(n+1)d} + 1)^{k-1} (delta^{-nd-d} + delta^{-nd}) l_1 - l_{k+1}

[p. 20] Since f_0^0 = delta^{-nd} and each l_i < delta^{-id}, we can substitute this to get Eq. (UP) and we can get a lower-bound Eq. (LP) by using l_i >= delta^{-(i-1)d}.

By construction, S_k <= f_0^k < T_k. For sufficiently small delta, observe that S_k <= f_0^k < T_k are all essentially the dominant term approx O(delta^{-n(k+1)d - kd}) and all the lower order terms do not matter. As a result it is immediate to see that f_k > delta^{-d}(f_0^{k-1} - l_k) > T_{k-1} and hence invariant 2 is also satisfied. Since only column k and the global token are affected, invariant 3 is also satisfied.

[p. 20] After n iterations, f_0^n contains a unique encoding for any P in **G**_delta^E. To ensure that all tokens are distinct, an additional layer is added: X = X + delta^{-n^2 d} psi(X, v - delta/2, v + delta/2) for all v in [S_1, T_n)_delta. This ensures that for all P, P' in **G**_delta^E, each entry of q(P) and q(P') are distinct.

## A.2.3 Approximating modified Transformers by Transformers [p. 21]

[p. 21] The previous lemma shows that a contextual mapping can be computed using only sparse transforms. The following lemma shows that a contextual mapping and feed-forward layers can be used to accurately map to the desired output of the function f_hat.

**Lemma 4** (Lemma 7 [104]). *Let g_c be the function in Lemma 3, we can construct a function g_v : R^{(n+1) x (d+1)} -> R^{(n+1) x d} composed of O(n delta^{-nd}) feed-forward layers (with hidden dimension q = 1) with activations in Phi such that g_v(Z) = [g_v^{tkn}(Z_1), ..., g_v^{tkn}(Z_n)], where for all j in {1, ..., n},*

g_v^{tkn}(g_c(L)_j) = f(L)_j

[p. 21] The previous section assumed Transformers that used hardmax operator sigma_H and activations functions belonging to the set Phi. This is without loss of generality as the following lemma shows.

**Lemma 5** (Lemma 9 [104]). *For each g in T^{2,1,1} and 1 <= p <= infinity, there exists g_bar in T^{2,1,4} such that d_p(g, g_bar) <= epsilon/3*

Combining Lemma 5 with Lemma 3, the main result is obtained:

**Theorem 2.** *Let 1 <= p <= infinity and epsilon > 0, there exists a transformer network g in T_D^{2,1,4} which achieves a ratio of d_p(f_hat, g) <= epsilon where D is the sparse graph.* [p. 21]

Since the sparsity graph associated with BIGBIRD contains a star network, we know that it can express any continuous function from a compact domain. [p. 21]

### Contemporary work on Universal Approximability of Sparse Transformers

[p. 21] Contemporary work done by Yun et al. [105] also parallelly explored the ability of sparse transformers with linear connections to capture sequence-to-sequence functions on the compact domain.
