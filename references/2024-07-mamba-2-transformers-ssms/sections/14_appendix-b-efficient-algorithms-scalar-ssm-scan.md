# B Efficient Algorithms for the Scalar SSM Scan (1-SS Multiplication) [p. 42-46]

[p. 42] This section fleshes out various algorithms for computing the scalar SSM scan, through the lens of structured matrix decompositions. The scalar SSM scan is defined as computing the recurrent part of the discrete SSM (7), in the case when $N = 1$ (i.e. $A$ is a scalar). This is commonly used to compute SSMs recurrently; in particular, the case of structured SSMs where $A$ is diagonally structured reduces down to this operation, such as in the S5 (J. T. Smith, Warrington, and Linderman 2023) and S6 (Gu and Dao 2023) models.

> The goal of this section is to support a central theme of this paper that *efficient algorithms for sequence models can be viewed as structured matrix multiplication algorithms*. [p. 42]

The various matrix decomposition ideas shown here are related to ideas used to derive fast SSM algorithms (Section 6), as well as directly used as a subroutine.

## B.1 Problem Definition

[p. 42] Let $a : (\mathsf{D},)$ and $b : (\mathsf{D},)$ be sequences of scalars. The **scalar SSM scan** is defined as

$$h_t = a_t h_{t-1} + b_t. \tag{21}$$

Here $h_{-1}$ can be an arbitrary value representing the previous *hidden state* to the SSM recurrence; unless otherwise specified, we assume $h_{-1} = 0$.

This is also called equation (21) the `cumprodsum` (cumulative product sum). Note that the `cumprodsum` reduces to the `cumprod` (cumulative product) when $b = 0$ is the additive identity and it reduces to the `cumsum` (cumulative sum) when $a = 1$ is the multiplicative identity.

[p. 43] In vectorized form:

$$h = Mb$$

$$M = \begin{bmatrix} 1 & & & \\ a_1 & 1 & & \\ a_2 a_1 & a_2 & 1 & \\ \vdots & \vdots & \ddots & \ddots \\ a_{T-1} \ldots a_1 & a_{T-1} \ldots a_2 & \cdots & a_{T-1} & 1 \end{bmatrix}$$

In other words, this is simply the matrix-vector product by a 1-SS matrix $M$.

Therefore there are three ways of viewing this fundamental primitive operation that are all equivalent:

- A (scalar) SSM scan.
- A `cumprodsum`.
- A 1-SS matrix-vector multiplication.

## B.2 Classical Algorithms

[p. 43] Two classical ways of computing the SSM scan (21), previously used by prior work.

### B.2.1 Sequential Recurrence

[p. 43] The recurrent mode simply computes (21) one timestep $t$ at a time. From the perspective of 1-SS multiplication, this was also described in Section 3.4.1.

### B.2.2 Parallel Associative Scan

[p. 43] An important observation is that this recurrence can be turned into an associative scan (E. Martin and Cundy 2018; J. T. Smith, Warrington, and Linderman 2023). This fact is not completely obvious. For example, S5 defined the correct associative scan operator and then showed associativity of the operator through rote calculation.

A slightly cleaner way to see that this is computable with an associative scan is to turn the multi-term recurrence into a single-term recurrence on a hidden state of size 2 instead of 1:

$$h_t = a_t h_{t-1} + b_t$$

$$\begin{bmatrix} h_t \\ 1 \end{bmatrix} = \begin{bmatrix} a_t & b_t \\ 0 & 1 \end{bmatrix} \begin{bmatrix} h_{t-1} \\ 1 \end{bmatrix}.$$

Then computing all the $h_t$ is the same as taking the cumulative products of these $2 \times 2$ matrices. Since matrix multiplication is associative, this can be computed with an associative scan. The associative binary operator is simply matrix multiplication on these particular matrices:

$$\begin{bmatrix} a_t & b_t \\ 0 & 1 \end{bmatrix} \begin{bmatrix} a_s & b_s \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} a_t a_s & a_t b_s + b_t \\ 0 & 1 \end{bmatrix}.$$

Equating the top row yields the same associative scan operator as defined by S5:

$$(a_t, b_t) \otimes (a_s, b_s) = (a_t a_s, a_t b_s + b_t). \tag{22}$$

[p. 43] The reason why associative scans are important is that they can be parallelized using a divide-and-conquer algorithm (Blelloch 1990). The details of this algorithm are omitted, and instead it is shown that the entire associative SSM scan algorithm can be derived from scratch through matrix decompositions (Appendix B.3.5).

## B.3 Efficient Algorithms via Structured Matrix Decompositions

[p. 44] Several algorithms for computing the SSM scan are discussed, all through the lens of finding structured matrix decompositions of the 1-SS matrix $M$. These algorithms or computation modes include:

- A *dilated* mode where information is propagated 1, 2, 4, 8, ... steps at a time.
- A *state-passing* mode where information is propagated forward in chunks.
- A *fully recurrent* mode that increments one step at a time, which is a special case of the state-passing mode.
- A *block decomposition* parallel mode where $M$ is divided into hierarchical blocks.
- A *scan* mode where $M$ is divided into equal size blocks and reduced recursively.

### B.3.1 Dilated Mode

[p. 44] This mode factors the 1-SS matrix in a particular way involving increasing "strides". This is best illustrated through a concrete example for $T = 8$:

The full 1-SS matrix $M$ (8x8 lower triangular with entries $a_{i,j}$) is factored into a product of three sparse lower-triangular matrices with increasing stride patterns:

- First factor: block-diagonal with 2x2 blocks along the diagonal (stride 1)
- Second factor: block-diagonal with 2x2 blocks at stride 2 positions
- Third factor: block-diagonal with 2x2 blocks at stride 4 positions

[p. 44] This closely resembles the computation of dilated convolutions.

1-SS matrices are a special case of butterfly matrices (Dao, Gu, et al. 2019; Dao, Sohoni, et al. 2020), which are another broad and fundamental type of structured matrix.

**Remark 8.** *This algorithm is sometimes described as a "work-inefficient but more parallelizable" prefix sum algorithm (Hillis and Steele Jr 1986), because it uses $O(T \log(T))$ operations but has half the depth/span as the work-efficient associative scan algorithm.* [p. 44]

### B.3.2 State-Passing (Chunkwise) Mode

[p. 44] This mode can be viewed as a generalization of the standard recurrent mode where instead of passing forward the recurrent state $h$ one step at a time, the answer is computed on chunks of arbitrary length $k$ and the state is passed through the chunk. This can also be derived from a simple block decomposition of the 1-SS matrix.

**Remark 9.** *While we call this "state-passing" to refer to how states are passed from one local segment to another, this is related to the "chunkwise" algorithms proposed by related models (Y. Sun et al. 2023; Yang et al. 2024).* [p. 44]

[p. 44-45] Consider computing $h = Mb$ in "chunks": for some index $k \in [T]$, the goal is to compute $h_{0:k}$ or the output up to index $k$, and have a way to reduce the problem to a smaller problem on indices $[k : T]$.

The matrix $M$ is written as:

$$M = \begin{bmatrix} a_{0:0} & & & \\ a_{1:0} & a_{1:1} & & \\ \vdots & & \ddots & \\ a_{k-1:0} & \cdots & \cdots & a_{k-1:k-1} \\ a_{k:0} & \cdots & \cdots & a_{k:k-1} & a_{k:k} \\ \vdots & & & \vdots & \vdots & \ddots \\ a_{T-1:0} & \cdots & \cdots & a_{T-1:k-1} & a_{T-1:k} & \cdots & a_{T-1:T-1} \end{bmatrix}$$

[p. 45] Let the upper-left triangle be $M_L$, lower-right be $M_R$ (left and right subproblems), and lower-left be $M_C$. Divide up $b$ into $b_L = b_{0:k}$ and $b_R = b_{k:T}$ in the same way. Note that

$$Mb = \begin{bmatrix} M_L b_L \\ M_R b_R + M_C b_L \end{bmatrix}$$

Also, $M_C$ has the rank-1 factorization (this is essentially the defining property of semiseparable matrices):

$$M_C = \begin{bmatrix} a_{k:k} \\ \vdots \\ a_{T-1:k} \end{bmatrix} a_k \begin{bmatrix} a_{k-1:0} & \cdots & a_{k-1:k-1} \end{bmatrix}$$

Thus

$$M_C b_L = \begin{bmatrix} a_{k:k} \\ \vdots \\ a_{T-1:k} \end{bmatrix} a_k \cdot (Mb)_{k-1}.$$

Here $(Mb)_{k-1} = h_{k-1}$ is thought of as the "final state" of the left chunk, because the row vector in $M_C$'s factorization is the same as the final row of $M_L$. Furthermore, the column vector in $M_C$'s factorization is the same as the final column of $M_R$.^7 Thus

$$M_R b_R + M_C b_L = M_R \begin{bmatrix} a_k h_{k-1} + b_k \\ b_{k+1} \\ \vdots \\ b_{T-1} \end{bmatrix}$$

^7 Both these facts can be seen from the Woodbury inverse...

[p. 45] Finally, $M_L$ and $M_R$ are self-similar to the original matrix $M$; the answers for these two smaller 1-SS matrix multiplications can be performed arbitrarily using any algorithm. In total, the algorithm proceeds as follows:

1. Compute the left half of the answer $h_{0:k}$ using any desired method (i.e. any of the methods for 1-SS multiplication from this section).
2. Compute the final state $h_{k-1}$.
3. Increment the state by one step to modify $b_k$.
4. Compute the right half of the answer $h_{k:T}$ using any desired method.

In other words, the left subproblem is computed as a black box, its final state is passed on to the right problem, and the right subproblem is computed as a black box.

[p. 45-46] The utility of this method comes from more complicated settings, such as in the general N-semiseparable case, and when the input $b$ has an additional "batch" dimension (or in other words this is a matrix-matrix instead of matrix-vector multiplication). In this case, an alternate algorithm for the chunks (corresponding to MM by $M_L$ and $M_R$) that does not materialize the full hidden states $h$ can be used. Instead, the hidden states are skipped and the final state $h_{k-1}$ is directly computed in an alternate way, then "pass" the state to the next chunk.

**Complexity.** [p. 46] This method can be very work-efficient because steps 2-3 takes only constant time. Therefore assuming the two subproblems (steps 1 and 4) are linear time, the whole method takes linear time.

The downside is that this is also sequential.

### B.3.3 Fully Recurrent Mode

[p. 46] The fully recurrent mode, where the recurrence is evolved one step at a time (21), is simply an instantiation of the state-passing mode with chunk size $k = 1$.

### B.3.4 (Parallel) Block Decomposition Mode

[p. 46] This uses the same matrix decomposition as the state-passing mode, but computes subproblems in a different order that trades off computation for parallelization.

As usual, the 1-SS matrix $M$ is written as:

$$M = \begin{bmatrix} 1 & & & \\ a_1 & 1 & & \\ a_2 a_1 & a_2 & 1 & \\ \vdots & \vdots & \ddots & \ddots \\ a_{T-1} \ldots a_1 & a_{T-1} \ldots a_2 & \cdots & a_{T-1} & 1 \end{bmatrix} = \begin{bmatrix} 1 & & & \\ -a_1 & 1 & & \\ 0 & -a_2 & 1 & \\ \vdots & \vdots & \ddots & \ddots \\ 0 & 0 & \cdots & -a_{T-1} & 1 \end{bmatrix}^{-1}$$

[p. 46] The key observation is again that the bottom-left quadrant of $M$ is rank-1. Aside from inspection, another way to see this is by using the RHS, observing that the bottom-left quadrant of it is a trivial rank-1 matrix (it is all 0 except the top-right corner is $-a_{T/2}$), and using the Woodbury inversion formula to see that the bottom-left corner of the LHS must also be rank 1. This also provides a way to deduce the rank-1 factorization, which can be verified through inspection:

$$M_{\text{lower-left-quadrant}} = \begin{bmatrix} (a_{T/2} \ldots a_1) & \cdots & a_{T/2} \\ \vdots & \ddots & \vdots \\ (a_{T-1} \ldots a_{T/2} a_{T/2-1} \ldots a_1) & \cdots & (a_{T-1} \ldots a_{T/2}) \end{bmatrix}$$

$$= \begin{bmatrix} a_{T/2} \\ \vdots \\ a_{T-1} \ldots a_{T/2} \end{bmatrix} \begin{bmatrix} (a_{T/2-1} \ldots a_1) & \cdots & a_{T/2-1} & 1 \end{bmatrix}.$$

[p. 46] A second observation is that *this matrix is self-similar*: any principle submatrix has the same form. In particular, the top-left and bottom-right quadrants are both 1-SS matrices.

This provides an easy way to perform the matrix multiplication by $M$: recurse on the two halves (i.e. top-left and bottom-right) in parallel, and then account for the bottom-left submatrix. This "combination" step in the divide-and-conquer algorithm is easy since the submatrix is rank 1. This leads to a parallel algorithm.

**Complexity.** Like the state-passing algorithm, this method uses the same block decompositions of the rank-structured semiseparable matrices. The difference is that both subproblems are recursed on in parallel, while the state-passing algorithm handles the left and then right subproblems. This lowers the depth/span of the algorithm from linear to $\log(T)$. The tradeoff is that the combination step (accounting for the rank-1 bottom-left submatrix) requires linear instead of constant work, so the total work is $O(T \log(T))$ instead of linear.

[p. 46] Note also that in the recursion, one can stop at any time and compute the subproblems in any other way. This is a main idea behind the SSD algorithm (Section 6), where the switch is made to the dual *quadratic attention* formulation on small subproblems.

### B.3.5 Associative Scan Mode

[p. 46] The state passing (chunkwise) algorithm has linear work, but also involves sequential operations.

[p. 46-47] The block matrix reduction and dilated modes are parallelizable: they have $\log(T)$ depth/span. However, they do extra work ($O(T \log(T))$).

As noted in Appendix B.2.2, there is an algorithm that achieves both $O(\log T)$ depth and $O(T)$ work by leveraging the associative scan (also called prefix scan) algorithm (Baker et al. 1996). This algorithm is most easily seen from the SSM scan or cumprodsum view, and even then is not obvious: it requires separately deriving an associative operator (22), and then leveraging the parallel/associative/prefix scan algorithm as a black box (Blelloch 1990).

Here it is shown that it is actually possible to derive this parallel scan from leveraging a different matrix decomposition.

[p. 47] For $T = 8$, the matrix $M$ is decomposed by partitioning into $2 \times 2$ blocks along the diagonal. The $8 \times 8$ 1-SS matrix $M$ (with entries $a_{i:j}$) is shown with block boundaries at rows/columns 2, 4, 6. The lower-triangular part below each diagonal block is factored as a rank-1 outer product of the left-side column vectors and the bottom row vectors from the diagonal blocks.

The resulting block factored form shows each off-diagonal block expressed as:

$$\begin{bmatrix} a_{i:j} \\ a_{i+1:j} \end{bmatrix} \begin{bmatrix} a_{k:l} \\ a_{k+1:l} \end{bmatrix}^\top$$

The algorithm proceeds in three stages:

**Stage 1.** First compute the answers for each of the diagonal blocks in the multiplication $Mb$. This produces two numbers, but the first element is unchanged. For example, the second block is going to compute $b_2$ and $a_3 b_2 + b_3$.

**Stage 2.** Now consider each of the $2 \times 2$ blocks factored as a rank-1 matrix in the strictly lower triangular part of the matrix. Note that each of the right side row vectors is the same as the bottom row vector in the diagonal block in its column: in particular the $[a_{1:0}\ a_{1:1}]$, $[a_{3:2}\ a_{3:3}]$, and $[a_{5:4}\ a_{5:5}]$ rows.

Therefore the answers are already available from Stage 1, which is the second element of all $T/2$ subproblems in Stage 1. If we call this array of elements $b'$ (of half the size of $b$), then we need to multiply $b'$ by the 1-SS matrix generated by $a_{3:-1}, a_{3:1}, a_{5:3}, a_{7:5}$.

**Stage 3.** Finally, each of the answers to Stage 2 can be broadcast into two final answers by multiplying by the left-side column vectors: in particular the $[a_{2:2}\ a_{3:2}]^\top$, $[a_{4:4}\ a_{5:4}]^\top$, and $[a_{6:6}\ a_{7:6}]^\top$ vectors.

Note that this can be slightly modified with some off-by-one shifting of the indices. An equivalent way to view this algorithm is as the three-step matrix factorization:

[p. 48] The $8 \times 8$ 1-SS matrix $M$ is factored as a product of three matrices:

$$M = \underbrace{\begin{bmatrix} a_{0:0} & & & & & & & \\ & a_{1:1} & & & & & & \\ & a_{2:1} & a_{2:2} & & & & & \\ & & & a_{3:3} & & & & \\ & & & a_{4:3} & a_{4:4} & & & \\ & & & & & a_{5:5} & & \\ & & & & & a_{6:5} & a_{6:6} & \\ & & & & & & & a_{7:7} \end{bmatrix}}_{\text{block-diagonal (Stage 3 broadcast)}} \underbrace{\begin{bmatrix} a_{0:0} & & & & \\ & a_{1:1} & & & \\ & & a_{2:2} & & \\ & a_{3:1} & a_{3:3} & & \\ & & & a_{4:4} & \\ & & a_{5:3} & a_{5:5} & \\ & & & & a_{6:6} \\ & & & a_{7:5} & a_{7:7} \end{bmatrix}}_{\text{1-SS of half size (Stage 2)}} \underbrace{\begin{bmatrix} a_{0:0} & & & & & & & \\ a_{1:0} & a_{1:1} & & & & & & \\ & & a_{2:2} & & & & & \\ & & a_{3:2} & a_{3:3} & & & & \\ & & & & a_{4:4} & & & \\ & & & & a_{5:4} & a_{5:5} & & \\ & & & & & & a_{6:6} & \\ & & & & & & a_{7:6} & a_{7:7} \end{bmatrix}}_{\text{block-diagonal (Stage 1)}}$$

Note that Stage 1 and Stage 3 require $O(T)$ work, while Stage 2 reduces to a self-similar problem of half the size. It is easy to check that this requires $O(T)$ total work and $O(\log T)$ depth/span.

**Remark 10.** *In fact, it is possible to see that the computation graph of this algorithm is identical to that of the associative scan algorithm described in Appendix B.2.2. The key takeaway is that instead of the steps of (1) recognizing that M defines a recurrence (2) observing that the recurrence can be defined with an associative binary operator; there is a completely different perspective of simply finding a structured matrix decomposition algorithm for M.* [p. 48]
