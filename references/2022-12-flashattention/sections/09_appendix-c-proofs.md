# C Proofs [p. 22–24]

## Proof of Theorem 1

[p. 22]

First the number of FLOPs and extra memory are counted. The dominating FLOPs are from matrix multiplication. In the inner loop (Algorithm 1 line 9), $\mathbf{Q}_i \mathbf{K}_j^\top \in \mathbb{R}^{B_r \times B_c}$ is computed for $\mathbf{Q}_i \in \mathbb{R}^{B_r \times d}$ and $\mathbf{K}_j \in \mathbb{R}^{B_c \times d}$, which takes $O(B_r B_c d)$ FLOPs. Also $\tilde{\mathbf{P}}_{ij} \mathbf{V}_j \in \mathbb{R}^{B_r \times d}$ is computed (Algorithm 1 line 12) for $\tilde{\mathbf{P}}_{ij} \in \mathbb{R}^{B_r \times B_c}$ and $\mathbf{V}_j \in \mathbb{R}^{B_c \times d}$, which takes $O(B_r B_c d)$ FLOPs. The inner loops execute $T_c T_r = \lceil \frac{N}{B_c} \rceil \lceil \frac{N}{B_r} \rceil$ times. Therefore the total number of FLOPs is

$$O\left(\frac{N^2}{B_c B_r} B_r B_c d\right) = O(N^2 d).$$

In terms of extra memory required, $O(N)$ memory is needed to store the statistics $(\ell, m)$.

### Correctness Proof (by induction)

[p. 22–23]

The algorithm's correctness is proved by induction on $j$ for $0 \leq j \leq T_c$. Let $\mathbf{K}_{:,j} \in \mathbb{R}^{jB_c \times d}$ be the first $jB_c$ rows of $\mathbf{K}$, and similarly $\mathbf{V}_{:,j} \in \mathbb{R}^{jB_c \times d}$ the first $jB_c$ rows of $\mathbf{V}$. Let $\mathbf{S}_{:,:j} = \mathbf{Q}\mathbf{K}_{:,j}^\top \in \mathbb{R}^{N \times jB_c}$, and $\mathbf{P}_{:,:j} = \text{softmax}(\mathbf{S}_{:,:j}) \in \mathbb{R}^{N \times jB_c}$ (softmax applied row-wise). Let $m^j, \ell^{(j)}, \mathbf{O}^{(j)}$ be the values of $m, \ell, \mathbf{O}$ in HBM after the $j$-th iteration of the outer loop (Algorithm 1 line 5). (Note that these values of $m, \ell, \mathbf{O}$ are updated after each iteration of the outer loop.) The claim is that after the $j$-th iteration of the outer loop, the following holds in HBM:

$$m^{(j)} = \text{rowmax}(\mathbf{S}_{:,:j}) \in \mathbb{R}^N, \quad \ell^{(j)} = \text{rowsum}(\exp(\mathbf{S}_{:,:j} - m^{(j)})) \in \mathbb{R}^N, \quad \mathbf{O}^{(j)} = \mathbf{P}_{:,:j} \mathbf{V}_{:,j} \in \mathbb{R}^{N \times d}.$$

**Base case ($j = 0$):** Based on the initialization (Algorithm 1 line 2), the claim is true for $j = 0$ (before any iteration of the outer loop is executed).

**Inductive step ($j \to j+1$):** Suppose the claim holds for some $j = 0, \ldots, T_c - 1$. On the $(j+1)$-th iteration of the outer loop, when updating the statistics in the inner loop (Algorithm 1 line 10), $m^{(j+1)} = \max(m^{(j)}, \tilde{m})$ where $\tilde{m} \in \mathbb{R}^N$ is the row-max of $\mathbf{S}_{:,j:j+1}$, the slice of $\mathbf{S}$ from column $jB_c$ to column $(j+1)B_c - 1$. This implies that

$$m^{(j+1)} = \text{rowmax}(\mathbf{S}_{:,:j+1}) \in \mathbb{R}^N.$$

Similarly, the update for $\ell$:

$$\ell^{(j+1)} = e^{m^{(j)} - m^{(j+1)}} \ell^{(j)} + e^{\tilde{m} - m^{(j+1)}} \tilde{\ell},$$

where $\tilde{\ell} = \text{rowsum}(\exp(\mathbf{S}_{:,j:j+1} - \tilde{m})) \in \mathbb{R}^N$. By the same algebraic manipulation in Section 3.1, we obtain:

$$\ell^{(j+1)} = \text{rowsum}(\exp(\mathbf{S}_{:,:j+1} - m^{(j+1)})) \in \mathbb{R}^N.$$

[p. 23]

Let $\mathbf{V}_{j:j+1}$ be the slice of $\mathbf{V}$ from column $jB_c$ to column $(j+1)B_c - 1$, we also update:

$$\mathbf{O}^{(j+1)} = \text{diag}(\ell^{(j+1)})^{-1} (\text{diag}(\ell^{(j)}) e^{m^{(j)} - m^{(j+1)}} \mathbf{O}^{(j)} + e^{\tilde{m} - m^{(j+1)}} \exp(\mathbf{S}_{j:j+1} - \tilde{m}) \mathbf{V}_{j:j+1})$$

$$= \text{diag}(\ell^{(j+1)})^{-1} (\text{diag}(\ell^{(j)}) e^{m^{(j)} - m^{(j+1)}} \mathbf{P}_{:,:j} \mathbf{V}_{:,j} + e^{-m^{(j+1)}} \exp(\mathbf{S}_{j:j+1}) \mathbf{V}_{j:j+1})$$

$$= \text{diag}(\ell^{(j+1)})^{-1} (e^{-m^{(j+1)}} \text{diag}(\ell^{(j)}) \exp(\mathbf{S}_{:,:j} - m^{(j)}) \mathbf{V}_{:,j} + e^{-m^{(j+1)}} \exp(\mathbf{S}_{j:j+1}) \mathbf{V}_{j:j+1})$$

$$= \text{diag}(\ell^{(j+1)})^{-1} (e^{-m^{(j+1)}} \exp(\mathbf{S}_{:,:j}) \mathbf{V}_{:,j} + e^{-m^{(j+1)}} \exp(\mathbf{S}_{j:j+1}) \mathbf{V}_{j:j+1})$$

$$= \text{diag}(\ell^{(j+1)})^{-1} (\exp(\mathbf{S}_{:,:j} - m^{(j+1)}) \mathbf{V}_{:,j} + \exp(\mathbf{S}_{j:j+1} - m^{(j+1)}) \mathbf{V}_{j:j+1})$$

$$= \text{diag}(\ell^{(j+1)})^{-1} \left(\exp\left(\begin{bmatrix} \mathbf{S}_{:,:j} & \mathbf{S}_{j:j+1} \end{bmatrix} - m^{(j+1)}\right)\right) \begin{bmatrix} \mathbf{V}_{:,j} \\ \mathbf{V}_{j:j+1} \end{bmatrix}$$

$$= \text{softmax}(\mathbf{S}_{:,j+1}) \mathbf{V}_{:,j+1}.$$

The claim is then true for $j + 1$. By induction, the claim is true for all $j = 0, \ldots, T_c$.

When $j = T_c$, the final value of **O** in HBM is $\text{softmax}(\mathbf{S})\mathbf{V} = \text{softmax}(\mathbf{Q}\mathbf{K}^\top)\mathbf{V}$. $\square$

## Proof of Theorem 2

[p. 23–24]

### IO complexity of standard attention

The inputs $\mathbf{Q}, \mathbf{K}, \mathbf{V} \in \mathbb{R}^{N \times d}$ reside in HBM, and at the end of the algorithm the output $\mathbf{O} \in \mathbb{R}^{N \times d}$ is written to HBM.

- In the first step of computing $\mathbf{S} = \mathbf{Q}\mathbf{K}^\top$, the inputs $\mathbf{Q}, \mathbf{K}$ are read from HBM and the output $\mathbf{S} \in \mathbb{R}^{N \times N}$ is written to HBM (Algorithm 0 line 1). This incurs $\Theta(Nd + N^2)$ HBM accesses.
- In the second step of computing $\mathbf{P} = \text{softmax}(\mathbf{S})$, the input $\mathbf{S}$ is read from HBM and the output $\mathbf{P}$ is written to HBM (Algorithm 0 line 2). This incurs $\Theta(N^2)$ HBM accesses.
- In the last step of computing $\mathbf{O} = \mathbf{P}\mathbf{V}$, the inputs $\mathbf{P}, \mathbf{V}$ are read from global memory and the output $\mathbf{O}$ is written to HBM (Algorithm 0 line 3). This incurs $\Theta(Nd + N^2)$ HBM accesses.

Overall, standard attention implementation requires $\Theta(Nd + N^2)$ global memory accesses.

### IO complexity of streaming attention (FlashAttention)

Following Algorithm 1, each element of $\mathbf{K}$ and $\mathbf{V}$ is loaded from HBM once (Algorithm 1 line 6). We make $T_c$ passes over $\mathbf{Q}$ and $\mathbf{O}$, each pass loading all of $\mathbf{Q}$ and all of $\mathbf{O}$ to HBM (Algorithm 1 line 8). Therefore the number of HBM accesses is $\Theta(Nd + NdT_c) = \Theta(NdT_c)$.

The conditions on the block sizes $B_c$ and $B_r$ are derived. The blocks $\mathbf{K}_j$ and $\mathbf{V}_j$ of size $B_c \times d$ must fit into on-chip memory, which translates to:

$$B_c d = O(M) \Leftrightarrow B_c = O\left(\frac{M}{d}\right).$$

Similarly, the blocks $\mathbf{Q}_i$, $\mathbf{O}_i$ of size $B_r \times d$ must fit into on-chip memory, which translates to:

$$B_r d = O(M) \Leftrightarrow B_r = O\left(\frac{M}{d}\right).$$

Finally, the block $\mathbf{S}_{ij}$ of size $B_r \times B_c$ must fit into on-chip memory, which translates to:

$$B_r B_c = O(M).$$

[p. 24]

We therefore set:

$$B_c = \Theta\left(\frac{M}{d}\right), \quad B_r = \Theta\left(\min\left(\frac{M}{d}, \frac{M}{B_c}\right)\right) = \Theta\left(\min\left(\frac{M}{d}, d\right)\right).$$

We then have:

$$T_c = \frac{N}{B_c} = \Theta\left(\frac{Nd}{M}\right).$$

As a result, the number of HBM accesses is:

$$\Theta\left(NdT_c\right) = \Theta\left(\frac{N^2 d^2}{M}\right).$$

$\square$

## Proof of Proposition 3

[p. 24]

For contradiction, suppose that there exists an algorithm that computes exact attention where the number of HBM accesses for all $M \in [d, Nd]$ is

$$o\left(\frac{N^2 d^2}{M}\right).$$

In the regime of $M = \Theta(Nd)$, this results in the number of HBM accesses:

$$o\left(\frac{N^2 d^2}{Nd}\right) = o(Nd).$$

However, the input to attention (matrices $\mathbf{Q}, \mathbf{K}, \mathbf{V}$) and the output $\mathbf{O}$ have size $Nd$ and they start out being in HBM, so if the algorithm computes exact attention it must incur at least $\Omega(Nd)$ HBM accesses. This is a contradiction. $\square$

## Proof of Theorem 5

[p. 24]

The IO complexity of the attention backward is very similar to the IO complexity of the attention forward (Theorem 2). A sketch of the proof is provided.

### IO complexity of standard attention backward pass

The inputs $\mathbf{Q}, \mathbf{K}, \mathbf{V}, \mathbf{dO} \in \mathbb{R}^{N \times d}$ reside in HBM, and at the end of the algorithm the outputs $\mathbf{dQ}, \mathbf{dK}, \mathbf{dV} \in \mathbb{R}^{N \times d}$ are written to HBM. At each step of the standard attention backward pass, one needs to load inputs of size $Nd$ or $N^2$ from HBM, and needs to write the outputs of size $N^2$ or $Nd$ to HBM. This incurs $\Theta(Nd + N^2)$ HBM accesses.

### IO complexity of FlashAttention backward pass

Similar to Theorem 2, each element of $\mathbf{K}$ and $\mathbf{V}$ is loaded from HBM once. Each element of $\mathbf{dK}$ and $\mathbf{dV}$ is only written to HBM once. We make $T_c$ passes over $\mathbf{Q}, \mathbf{O}, \mathbf{dO}$, each pass loading all of $\mathbf{Q}, \mathbf{O}, \mathbf{dO}$ to HBM. We also make $T_c$ passes over $\mathbf{dQ}$, each pass reading/writing all of $\mathbf{dQ}$ from/to HBM. Therefore the number of HBM accesses is $\Theta(Nd + NdT_c) = \Theta(NdT_c)$.

As in the proof of Theorem 2, the constraints on the block sizes are that:

$$B_c = \Theta\left(\frac{M}{d}\right), \quad B_r = \Theta\left(\min\left(\frac{M}{d}, d\right)\right).$$

We then have:

$$T_c = \frac{N}{B_c} = \Theta\left(\frac{Nd}{M}\right).$$

As a result, the number of HBM accesses is:

$$\Theta\left(NdT_c\right) = \Theta\left(\frac{N^2 d^2}{M}\right).$$

$\square$
