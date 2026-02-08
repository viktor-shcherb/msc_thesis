# 6 A Hardware-Efficient Algorithm for SSD Models [p. 17-22]

[p. 17] The benefits of developing the theoretical SSD framework between SSMs, attention, and structured matrices lies in using the connections to improve the models and algorithms. This section shows how various algorithms for computing SSD models efficiently can be derived from various algorithms for computing structured matrix multiplication.

The main computational result is an algorithm for computing SSD models that combines both the linear (recurrent) mode and quadratic (attention) mode. This algorithm is as computation efficient as SSMs (linear scaling in sequence length) and as hardware-friendly as attention (primarily uses matrix multiplications).

**Theorem 6.1.** *Consider an SSD model with state expansion factor* N *and head dimension* P = N. *There exists an algorithm for computing the model on any input $X \in \mathbb{R}^{(\mathsf{T},\mathsf{P})}$ which only requires $O(\mathsf{TN}^2)$ training FLOPs, $O(\mathsf{TN})$ inference FLOPs, $O(\mathsf{N}^2)$ inference memory, and whose work is dominated by matrix multiplications.* [p. 17]

[p. 18] Note that all of these bounds are tight, because a state space model with state expansion N operating on a head of size N has total state size $\mathsf{N}^2$ (yielding the lower bounds for training and inference FLOPs of $O(\mathsf{TN}^2)$ and $O(\mathsf{N}^2)$ respectively). Furthermore the input $X$ itself has TN elements, yielding the memory lower bound.

## Block Decomposition Approach

[p. 18] The main idea behind Theorem 6.1 is once again viewing the problem of computing a state space model as a semiseparable matrix multiplication, but leveraging its structure in a new way. Instead of computing the whole matrix in either recurrent or attention mode, a **block decomposition** of the matrix is performed. The diagonal blocks can be computed using the dual attention mode, which can be efficiently done with matrix multiplications, while the off-diagonal blocks can be factored by the rank-structure of semiseparable matrices and reduced to a smaller recurrence. Listing 1 provides a self-contained implementation of the SSD algorithm. Compared to the general selective SSM of Gu and Dao (2023), this implementation is much simpler, and relatively efficient even in native PyTorch without requiring special low-level kernels.

The matrix $M$ is partitioned into a $\frac{\mathsf{T}}{\mathsf{Q}} \times \frac{\mathsf{T}}{\mathsf{Q}}$ grid of submatrices of size $\mathsf{Q} \times \mathsf{Q}$, for some block size Q. Note that the off-diagonal blocks are low-rank by the defining property of semiseparable matrices (Definition 3.1).[^5]

[^5]: Note that the block decomposition is valid even with partitions of varying size, e.g. if $\mathsf{Q} \nmid \mathsf{T}$, but even divisibility is assumed for simplicity.

**(Block Decomposition)**

$$M = \begin{bmatrix} M^{(0,0)} \\ M^{(1,0)} & M^{(1,1)} \\ \vdots & \vdots & \ddots \\ M^{(\mathsf{T}/\mathsf{Q}-1,0)} & M^{(\mathsf{T}/\mathsf{Q}-1,1)} & \cdots & M^{(\mathsf{T}/\mathsf{Q}-1,\mathsf{T}/\mathsf{Q}-1)} \end{bmatrix}$$

**(Diagonal Block)**

$$M^{(j,j)} = \text{SSM}(A_{j\mathsf{Q}:(j+1)\mathsf{Q}}, B_{j\mathsf{Q}:(j+1)\mathsf{Q}}, C_{j\mathsf{Q}:(j+1)\mathsf{Q}})$$

**(Low-Rank Block)**

$$M^{(j,i)} = \begin{bmatrix} C_{j\mathsf{Q}}^\top A_{j\mathsf{Q}:j\mathsf{Q}-1} \\ \vdots \\ C_{(j+1)\mathsf{Q}-1}^\top A_{(j+1)\mathsf{Q}-1:j\mathsf{Q}-1} \end{bmatrix} A_{j\mathsf{Q}-1:(i+1)\mathsf{Q}-1} \begin{bmatrix} B_{i\mathsf{Q}}^\top A_{(i+1)\mathsf{Q}-1:i\mathsf{Q}} \\ \vdots \\ B_{(i+1)\mathsf{Q}-1}^\top A_{(i+1)\mathsf{Q}-1:(i+1)\mathsf{Q}-1} \end{bmatrix}^\top$$

[p. 19] This is illustrated through an example for $\mathsf{T} = 9$ and decomposing into chunks of length $\mathsf{Q} = 3$. The shaded cells are low-rank factorizations of the off-diagonal blocks of the semiseparable matrix.

The full $9 \times 9$ matrix $M$ is shown with entries $C_i^\top A_{i:j} B_j$ for all $i \ge j$, decomposed into $3 \times 3$ diagonal blocks (upper-triangular entries within each block) and off-diagonal blocks factored as products of C-block-factors, A-block-factors, and B-block-factors.

The output of a "chunk" $y_{j\mathsf{Q}:(j+1)\mathsf{Q}}$ is divided into two components: the effect of inputs within the chunk $x_{j\mathsf{Q}:(j+1)\mathsf{Q}}$, and the effect of inputs before the chunk $x_{0:j\mathsf{Q}}$.

## 6.1 Diagonal Blocks

[p. 19] The diagonal blocks are easy to handle, because they are simply self-similar problems of a smaller size. The $j$-th block represents computing the answer $\text{SSM}(A_R, B_R, C_R)(x_R)$ for the range $R = j\mathsf{Q} : (j+1)\mathsf{Q} = (j\mathsf{Q}, j\mathsf{Q}+1, \ldots, j\mathsf{Q}+\mathsf{Q}-1)$. The key is that this block can be computed using any desired method. In particular, for small chunk lengths Q, this problem is computed more efficiently using the dual quadratic SMA form. Additionally, the chunks can be computed in parallel.

These subproblems can be interpreted as: what is the output per chunk *supposing that the initial state (to the chunk) is* 0. In other words for chunk $j$, this computes the correct outputs taking into account only the chunk inputs $x_{j\mathsf{Q}:(j+1)\mathsf{Q}}$.

## 6.2 Low-Rank Blocks

[p. 19] The low-rank factorizations consist of 3 terms, and there are correspondingly three pieces of the computation. The terminology used:

- The terms like $\begin{bmatrix} B_0^\top A_{2:0} \\ B_1^\top A_{2:1} \\ B_2^\top A_{2:2} \end{bmatrix}^\top$ are called the right factors or **B-block-factors**.

- The terms like $A_{5:2}$ are called the center factors or **A-block-factors**.

- The terms like $\begin{bmatrix} C_6^\top A_{6:5} \\ C_7^\top A_{7:5} \\ C_8^\top A_{8:5} \end{bmatrix}$ are called the left factors or **C-block-factors**.

**Figure 5** (p. 20): "(**SSD Algorithm.**) By using the matrix transformation viewpoint of state space models to write them as semiseparable matrices (Section 3), we develop a more hardware-efficient computation of the SSD model through a block-decomposition matrix multiplication algorithm. The matrix multiplication also has an interpretation as a state space model, where blocks represent chunking the input and output sequence. Diagonal blocks represent intra-chunk computations and the off-diagonal blocks represent inter-chunk computations, factored through the SSM's hidden state."

The figure shows the semiseparable matrix $M$ with its block decomposition. Below the matrix, three rows are labeled:
- **Inputs** $X$: input sequence chunks shown as blocks
- **States** $H$: hidden state vectors between chunks (shown with dashed borders)
- **Outputs** $Y$: output sequence chunks

Color-coded arrows indicate four types of operations:
- Diagonal Block: Input $\to$ Output (orange, within each chunk)
- Low-Rank Block: Input $\to$ State (green, computing B-block-factors)
- Low-Rank Block: State $\to$ State (blue, computing A-block-factors via inter-chunk recurrence)
- Low-Rank Block: State $\to$ Output (yellow, computing C-block-factors)

[p. 20] **Right Factors.** This step computes the multiplication by the right B-block-factors of the low-rank factorization. Note that for each chunk, this is a (N, Q) by (Q, P) matrix multiplication, where N is the state dimension and P is the head dimension. The result is a (N, P) tensor for each chunk, which has the same dimensionality as the expanded hidden state $h$.

This can be interpreted as: what is the final state per chunk *supposing that the initial state (to the chunk) is* 0. In other words this computes $h_{j\mathsf{Q}+\mathsf{Q}-1}$ assuming that $x_{0:j\mathsf{Q}} = 0$.

**Center Factors.** This step computes the effect of the center A-block-factors terms in the low-rank factorization. In the previous step, the final states per chunk have total shape (T/Q, N, P). This is now multiplied by a 1-SS matrix generated by $A_{2\mathsf{Q}-1:\mathsf{Q}-1}^{\times}, A_{3\mathsf{Q}-1:2\mathsf{Q}-1}^{\times}, \ldots, A_{\mathsf{T}-1:\mathsf{T}-\mathsf{Q}-1}^{\times}$.

This step can be computed by any algorithm for computing 1-SS multiplication (also known as the scalar SSM scan or `cumprodsum` operator).

This can be interpreted as: what is the actual final state per chunk *taking into account all previous inputs*; in other words, this computes the true hidden state $h_{j\mathsf{Q}}$ taking into account all of $x_{0:(j+1)\mathsf{Q}}$.

**Left Factors.** This step computes the multiplication by the left C-block-factors of the low-rank factorization. For each chunk, this can be represented by a matrix multiplication contract(QN, NP $\to$ QP).

This can be interpreted as: what is the output per chunk *taking into account the correct initial state* $h_{j\mathsf{Q}-1}$, *and supposing the inputs $x_{j\mathsf{Q}:(j+1)\mathsf{Q}}$ are* 0. In other words for chunk $j$, this computes the correct outputs taking into account only the prior inputs $x_{0:j\mathsf{Q}}$.

## 6.3 Computational Cost

[p. 20-21] The notation BMM(B, M, N, K) is defined to denote a batched matrix multiplication contract(MK, KN $\to$ MN) with batch dimension B. From this notation three aspects of efficiency can be inferred:

- *Computation cost*: total of $O(\mathsf{BMNK})$ FLOPs.
- *Memory cost*: total of $O(\mathsf{B}(\mathsf{MK} + \mathsf{KN} + \mathsf{MN}))$ space.
- *Parallelization*: larger M, N, K terms can leverage specialized matrix multiplication units on modern accelerators.

**Center Blocks.** The cost of the quadratic SMA computation consists of three steps (equation (16)):

- Computing the kernel matrix $C^\top B$, which has cost BMM(T/Q, Q, Q, N).
- Multiplying by the mask matrix, which is an elementwise operation on tensors of shape (T/Q, Q, Q).
- Multiplying by the $X$ values, which has cost BMM(T/Q, Q, P, N).

**Low-Rank Blocks: Right Factors.** This step is a single matrix multiplication with cost BMM(T/Q, N, P, Q). [p. 22]

**Low-Rank Blocks: Center Factors.** This step is a scalar SSM scan (or 1-SS multiplication) of length T/Q on (N, P) independent channels. The work of this scan is TNP/Q, which is negligible compared to the other factors. [p. 22]

Note that because of the blocking which reduces the length of the sequence from T to T/Q, this scan has Q times smaller cost than a pure SSM scan (e.g. the selective scan of Mamba). Thus the authors observe that on most problem lengths, other algorithms (Appendix B) may be more efficient or much easier to implement without a significant slowdown. For example, a naive implementation of this via 1-SS matrix multiplication has cost BMM(1, T/Q, NP, T/Q), which is much easier to implement and can be more efficient than a naive recurrence/scan implementation.

**Low-Rank Blocks: Left Factors.** This step is a single matrix multiplication with cost BMM(T/Q, Q, P, N). [p. 22]

## Total Cost

[p. 22] **Total Cost.** If N = P = Q (i.e., the state dimension, head dimension, and chunk length are equal), then all BMM terms above become BMM(T/N, N, N, N). The computational characteristics are:

- Total FLOP count of $O(\mathsf{TN}^2)$.
- Total memory of $O(\mathsf{TN})$.
- The work consists primarily of *matrix multiplications* on matrices of shape (N, N).

The memory consumption is tight; the inputs and outputs $x, y$ have shape $(\mathsf{T}, \mathsf{P}) = (\mathsf{T}, \mathsf{N})$. Meanwhile the FLOP count reflects an extra factor of N, which is cost incurred by the autoregressive state size and is common to all models.

Aside from the matmuls, there is a scalar SSM scan on $\mathsf{NP} = \mathsf{N}^2$ features and sequence length T/Q. This has cost $O(\mathsf{T/QN}^2)$ FLOPs and $O(\log(\mathsf{T/Q}))$ depth. Although it does not use matrix multiplications, it is still fully parallelizable and the total work done is negligible compared to the other steps; this has a negligible cost in the GPU implementation.

## Comparison to Pure SSM and Attention Models

[p. 22] Quadratic attention is also very hardware efficient by only leveraging matrix multiplications, but has $\mathsf{T}^2\mathsf{N}$ total FLOPs. Its slower computation speed at both training and inference can directly be seen as a consequence of having a larger state size -- standard attention has a state size scaling with sequence length T because it caches its history and does not compress its state.

Linear SSMs have $\mathsf{TNP} = \mathsf{TN}^2$ total FLOPs, which is the same as SSD. However, a naive implementation requires a state expansion (15a) that materializes extra memory, and a scalar operation (15b) that does not leverage matrix multiplications.

|                       | Attention      | SSM            | SSD            |
|-----------------------|----------------|----------------|----------------|
| State size            | T              | N              | N              |
| Training FLOPs        | $\mathsf{T}^2\mathsf{N}$ | $\mathsf{TN}^2$ | $\mathsf{TN}^2$ |
| Inference FLOPs       | TN             | $\mathsf{N}^2$ | $\mathsf{N}^2$ |
| (Naive) memory        | $\mathsf{T}^2$ | $\mathsf{TN}^2$ | TN             |
| Matrix multiplication | checkmark            |                | checkmark            |

[p. 22] The authors note that many other matrix decompositions are possible (for example, see Appendix B for a compendium of algorithms for 1-SS multiplication through different structured matrix decompositions) which may lead to more algorithms for SSDs that could be better for other specialized settings. Even more broadly, semiseparable matrices have a rich literature and many more representations besides the SSS form that they use (Definition 3.2), and even more efficient algorithms may be possible.

## Listing 1: PyTorch Implementation

[p. 21] **Listing 1** PyTorch example of the state space dual (SSD) model.

```python
def segsum(x):
    """Naive segment sum calculation. exp(segsum(A)) produces a 1-SS matrix,
       which is equivalent to a scalar SSM."""
    T = x.size(-1)
    x_cumsum = torch.cumsum(x, dim=-1)
    x_segsum = x_cumsum[..., :, None] - x_cumsum[..., None, :]
    mask = torch.tril(torch.ones(T, T, device=x.device, dtype=bool), diagonal=0)
    x_segsum = x_segsum.masked_fill(~mask, -torch.inf)
    return x_segsum

def ssd(X, A, B, C, block_len=64, initial_states=None):
    """
    Arguments:
        X: (batch, length, n_heads, d_head)
        A: (batch, length, n_heads)
        B: (batch, length, n_heads, d_state)
        C: (batch, length, n_heads, d_state)
    Return:
        Y: (batch, length, n_heads, d_head)
    """
    assert X.dtype == A.dtype == B.dtype == C.dtype
    assert X.shape[1] % block_len == 0

    # Rearrange into blocks/chunks
    X, A, B, C = [rearrange(x, "b (c l) ... -> b c l ...", l=block_len) for x in (X, A, B, C)]

    A = rearrange(A, "b c l h -> b h c l")
    A_cumsum = torch.cumsum(A, dim=-1)

    # 1. Compute the output for each intra-chunk (diagonal blocks)
    L = torch.exp(segsum(A))
    Y_diag = torch.einsum("bclhn,bcshn,bhcls,bclhp->bclhp", C, B, L, X)

    # 2. Compute the state for each intra-chunk
    # (right term of low-rank factorization of off-diagonal blocks; B terms)
    decay_states = torch.exp((A_cumsum[:, :, :, -1:] - A_cumsum))
    states = torch.einsum("bclhn,bhcl,bclhp->bchpn", B, decay_states, X)

    # 3. Compute the inter-chunk SSM recurrence; produces correct SSM states at chunk boundaries
    # (middle term of factorization of off-diag blocks; A terms)
    if initial_states is None:
        initial_states = torch.zeros_like(states[:, :1])
    states = torch.cat([initial_states, states], dim=1)
    decay_chunk = torch.exp(segsum(F.pad(A_cumsum[:, :, :, -1], (1, 0))))
    new_states = torch.einsum("bhzc,bchpn->bzhpn", decay_chunk, states)
    states, final_state = new_states[:, :-1], new_states[:, -1]

    # 4. Compute state -> output conversion per chunk
    # (left term of low-rank factorization of off-diagonal blocks; C terms)
    state_decay_out = torch.exp(A_cumsum)
    Y_off = torch.einsum("bclhn,bchpn,bhcl->bclhp", C, states, state_decay_out)

    # Add output of intra-chunk and inter-chunk terms (diagonal and off-diagonal blocks)
    Y = rearrange(Y_diag + Y_off, "b c l h p -> b (c l) h p")
    return Y, final_state
```

The implementation consists of four numbered steps corresponding to the four components of the block decomposition:
1. **Diagonal blocks (intra-chunk):** Computes output within each chunk using the quadratic SMA form via einsum.
2. **Right factors (B-block-factors):** Computes the state for each chunk assuming zero initial state, using decay factors derived from cumulative sums of $A$.
3. **Center factors (A-block-factors):** Computes the inter-chunk SSM recurrence to produce correct hidden states at chunk boundaries, using `segsum` to generate the 1-SS matrix.
4. **Left factors (C-block-factors):** Converts the corrected hidden states to output contributions per chunk.

The final output is the sum of intra-chunk (diagonal block) and inter-chunk (off-diagonal block) contributions.