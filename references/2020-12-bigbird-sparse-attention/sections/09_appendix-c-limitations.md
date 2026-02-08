# C Limitations [p. 28-29]

[p. 28] This appendix shows that sparse attention mechanisms cannot universally replace dense attention mechanisms, i.e. there is no free lunch. A natural task is demonstrated which can be solved by the full attention mechanism in O(1)-layers. However, under standard complexity theoretic assumptions, this problem will require Omega_tilde(n)-layers for any sparse attention layers with O_tilde(n) edges (not just BIGBIRD). (The standard notation Omega_tilde(n) is used to hide the dependence on poly-logarithmic factors.)

The simple problem of finding the furthest vector for each vector in the given sequence of length n and dimension d in Omega(log^2 n) is considered. The assumption on the dimension is mild, as in many situations the dimension d = 768 is actually comparable to the number of n.

**Task 1.** *Given n unit vectors {u_1, ..., u_n}, each in R^d where d = Theta(log^2 n), compute f(u_1, ..., u_n) -> (u_{1*}, ..., u_{n*}) where for a fixed j in [n], we define j* = arg max_k ||u_k - u_j||_2^2.* [p. 28]

Finding vectors that are furthest apart boils down to minimizing inner product search in case of unit vectors. For a full-attention mechanism with appropriate query and keys, this task is very easy as we can evaluate all pair-wise inner products.

The impossibility for sparse-attention follows from hardness results stemming from Orthogonal Vector Conjecture (OVC) [2, 1, 96, 7], which is a widely used assumption in fine-grained complexity. Informally, it states that one cannot determine if the minimum inner product among n Boolean vectors is 0 in subquadratic time.

**Conjecture 1** (Orthogonal Vectors Conjecture). *For every epsilon > 0, there is a c >= 1 such that given n Boolean vectors in d dimension, cannot determine if there is a pair of orthogonal vectors in O(n^{2-epsilon}) time on instances with d >= c log n.* [p. 28]

Using conjecture 1, a reduction is shown to demonstrate that a transformer g in T_D^{H=O(d), m=O(d), q=O(d)} for any sparse directed graph D which completes Task 1 must require a superlinear number of layers.

**Proposition 2.** *There exists a single layer full-attention network g in T^{H=1, m=2d, q=0} that can evaluate Task 1, i.e. g(u_1, ..., u_n) = [u_{1*}, ..., u_{n*}], but for any sparse-attention network in T_D^{H=O(d), m=O(d), q=O(d)} with graph D having O_tilde(n) edges (i.e. inner product evaluations), would require Omega_tilde(n^{1-o(1)}) layers.* [p. 28]

*Proof.* The proof is broken into two parts:

## Part 1: The full attention mechanism can solve the problem in O(1) layer [p. 28]

An explicit construction of a single layer full self-attention that can evaluate Task 1 is provided.

**Step 1** Each u_i is embedded into R^{2d} as follows:

**Equation (9):**

x_i := E(u_i) = [u_i; 0]

**Step 2** Query, key, value functions are constructed as follows:

**Equation (10):**

Q([a; b]) = -a
K([a; b]) = a
V([a; b]) = [0; a]

Then Attn(Q(x_i), K(X), V(X)) = [0; u_{arg max_j <-u_i, u_j>}]. Then,

**Equation (11):**

a_i = Attn(Q(x_i), K(X), V(X)) + x_i = [u_i; u_{arg max_j <-u_i, u_j>}] = [u_i; u_{i*}]

**Step 3** Let O(a_i) = 0, then the output z_i = [u_i; u_{i*}] as desired.

To complete the argument, it now only takes O(n) inner products to check if there is a pair of orthogonal vectors as we need only compare <u_i, u_{i*}>. [p. 28]

## Part 2: Every Sparse Attention Mechanism will need Omega_tilde(n^{1-epsilon}) layers [p. 29]

[p. 29] It is proved by contradiction that it is impossible to solve Task 1 by any g in T_D^{H=O(d), m=O(d), q=O(d)} sparse-attention graph D with O_tilde(n) edges.

Suppose we can solve Task 1 using a network g in T_D^{H=O(d), m=O(d), q=O(d)} that has l layers. Recall that all the computation we do in one layer is:

**Equation (12):**

a_i = ATTN_D(Q(x_i), K(X_{N(i)}), V(X_{N(i)})) + x_i
x_i = O(a_i) + a_i

where ATTN_D is defined in eq. (AT). [p. 29]

Thus, total computation per layer is O_tilde(nd^3) and consequently O_tilde(nld^3) for the whole network consisting of l layers.

We can use the result of Task 1 to solve the orthogonal vector (OV) problem (defined in Conjecture 1) in linear time. So in total, we will be able to solve any instance of OV in O_tilde(nld^3) time.

Now if l = O(n^{1-epsilon}) for any epsilon > 0 and d = Theta(log^2 n), then it appears that we are able to solve OV in O_tilde(n^{2-epsilon}) which contradicts Conjecture 1. Therefore, we need at least Omega_tilde(n^{1-o(1)}) layers.
