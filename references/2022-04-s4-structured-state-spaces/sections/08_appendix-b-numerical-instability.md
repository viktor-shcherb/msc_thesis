# B Numerical Instability of LSSL [p. 16-19]

[p. 16]

This section proves the claims made in Section 3.1 about prior work. The authors first derive the explicit diagonalization of the HiPPO matrix, confirming its instability because of exponentially large entries. They then discuss the proposed theoretically fast algorithm from [18] (Theorem 2) and show that it also involves exponentially large terms and thus cannot be implemented.

## B.1 HiPPO Diagonalization [p. 17-18]

[p. 17]

*Proof of Lemma 3.2.* The HiPPO matrix (2) is equal, up to sign and conjugation by a diagonal matrix, to:

$$\boldsymbol{A} = \begin{bmatrix} 1 \\ -1 & 2 \\ 1 & -3 & 3 \\ -1 & 3 & -5 & 4 \\ 1 & -3 & 5 & -7 & 5 \\ -1 & 3 & -5 & 7 & -9 & 6 \\ 1 & -3 & 5 & -7 & 9 & -11 & 7 \\ -1 & 3 & -5 & 7 & -9 & 11 & -13 & 8 \\ \vdots & & & & & & & \ddots \end{bmatrix}$$

with entries:

$$\boldsymbol{A}_{nk} = \begin{cases} (-1)^{n-k}(2k+1) & n > k \\ k+1 & n = k \\ 0 & n < k \end{cases}$$

The goal is to show that this **A** is diagonalized by the matrix:

$$\boldsymbol{V} = \binom{i+j}{i-j}_{ij} = \begin{bmatrix} 1 \\ 1 & 1 \\ 1 & 3 & 1 \\ 1 & 6 & 5 & 1 \\ 1 & 10 & 15 & 7 & 1 \\ 1 & 15 & 35 & 28 & 9 & 1 \\ \vdots & & & & & \ddots \end{bmatrix},$$

or in other words that columns of this matrix are eigenvectors of **A**.

Concretely, the proof shows that the j-th column of this matrix $\boldsymbol{v}^{(j)}$ with elements:

$$\boldsymbol{v}_i^{(j)} = \begin{cases} 0 & i < j \\ \binom{i+j}{i-j} = \binom{i+j}{2j} & i \geq j \end{cases}$$

is an eigenvector with eigenvalue $j + 1$. In other words, for all indices $k \in [N]$:

$$(\boldsymbol{A}\boldsymbol{v}^{(j)})_k = \sum_i \boldsymbol{A}_{ki}\boldsymbol{v}_i^{(j)} = (j+1)\boldsymbol{v}_k^{(j)}. \tag{7}$$

If $k < j$, then for all $i$ inside the sum, either $k < i$ or $i < j$. In the first case $\boldsymbol{A}_{ki} = 0$ and in the second case $\boldsymbol{v}_i^{(j)} = 0$, so both sides of equation (7) are equal to 0.

It remains to show the case $k \geq j$, which proceeds by induction on $k$. Expanding equation (7) using the formula for **A** yields:

$$(\boldsymbol{A}\boldsymbol{v})_k^{(j)} = \sum_i \boldsymbol{A}_{ki}\boldsymbol{v}_i^{(j)} = \sum_{i=j}^{k-1} (-1)^{k-i}(2i+1)\binom{i+j}{2j} + (k+1)\binom{k+j}{2j}.$$

In the base case $k = j$, the sum disappears and we are left with $(\boldsymbol{A}\boldsymbol{v}^{(j)})_j = (j+1)\binom{2j}{2j} = (j+1)\boldsymbol{v}_j^{(j)}$, as desired.

[p. 18]

Otherwise, the sum for $(\boldsymbol{A}\boldsymbol{v})_k^{(j)}$ is the same as the sum for $(\boldsymbol{A}\boldsymbol{v})_{k-1}^{(j)}$ but with sign reversed and a few edge terms. The result follows from applying the inductive hypothesis and algebraic simplification:

$$(\boldsymbol{A}\boldsymbol{v})_k^{(j)} = -(\boldsymbol{A}\boldsymbol{v})_{k-1}^{(j)} - (2k-1)\binom{k-1+j}{2j} + k\binom{k-1+j}{2j} + (k+1)\binom{k+j}{2j}$$

$$= -(j+1)\binom{k-1+j}{2j} - (k-1)\binom{k-1+j}{2j} + (k+1)\binom{k+j}{2j}$$

$$= -(j+k)\binom{k-1+j}{2j} + (k+1)\binom{k+j}{2j}$$

$$= -(j+k)\frac{(k-1+j)!}{(k-1-j)!(2j)!} + (k+1)\binom{k+j}{2j}$$

$$= -\frac{(k+j)!}{(k-1-j)!(2j)!} + (k+1)\binom{k+j}{2j}$$

$$= -(k-j)\frac{(k+j)!}{(k-j)!(2j)!} + (k+1)\binom{k+j}{2j}$$

$$= (j-k)\binom{k+j}{2j} + (k+1)\binom{k+j}{2j}$$

$$= (j+1)\boldsymbol{v}_k^{(j)}.$$

$\square$

## B.2 Fast but Unstable LSSL Algorithm [p. 18-19]

[p. 18]

Instead of diagonalization, Gu et al. [18, Theorem 2] proposed a sophisticated fast algorithm to compute:

$$K_L(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}) = (\overline{\boldsymbol{C}}\overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}\overline{\boldsymbol{A}}\overline{\boldsymbol{B}}, \ldots, \overline{\boldsymbol{C}}\overline{\boldsymbol{A}}^{L-1}\overline{\boldsymbol{B}}).$$

This algorithm runs in $O(N \log^2 N + L \log L)$ operations and $O(N + L)$ space. However, the authors now show that this algorithm is also numerically unstable.

There are several reasons for the instability of this algorithm, but most directly the authors can pinpoint a particular intermediate quantity that they use.

**Definition 1.** *The fast LSSL algorithm computes coefficients of $p(x)$, the characteristic polynomial of $A$, as an intermediate computation. Additionally, it computes the coefficients of its inverse, $p(x)^{-1}$ (mod $x^L$).*

The authors now claim that this quantity is numerically unfeasible. They narrow down to the case when $\overline{\boldsymbol{A}} = \boldsymbol{I}$ is the identity matrix. Note that this case is actually in some sense the most typical case: when discretizing the continuous-time SSM to discrete-time by a step-size $\Delta$, the discretized transition matrix $\overline{\boldsymbol{A}}$ is brought closer to the identity. For example, with the Euler discretization $\overline{\boldsymbol{A}} = \boldsymbol{I} + \Delta\boldsymbol{A}$, we have $\overline{\boldsymbol{A}} \to \boldsymbol{I}$ as the step size $\Delta \to 0$.

**Lemma B.1.** *When $\overline{\boldsymbol{A}} = \boldsymbol{I}$, the fast LSSL algorithm requires computing terms exponentially large in $N$.*

*Proof.* The characteristic polynomial of **I** is:

$$p(x) = \det |\boldsymbol{I} - x\boldsymbol{I}| = (1 - x)^N.$$

These coefficients have size up to $\binom{N}{N/2} \approx \frac{2^N}{\sqrt{\pi N/2}}$.

The inverse of $p(x)$ has even larger coefficients. It can be calculated in closed form by the generalized binomial formula:

$$(1 - x)^{-N} = \sum_{k=0}^{\infty} \binom{N+k-1}{k} x^k.$$

[p. 19]

Taking this (mod $x^L$), the largest coefficient is:

$$\binom{N+L-2}{L-1} = \binom{N+L-2}{N-1} = \frac{(L-1)(L-2)\ldots(L-N+1)}{(N-1)!}.$$

When $L = N - 1$ this is:

$$\binom{2(N-1)}{N-1} \approx \frac{2^{2N}}{\sqrt{\pi N}}$$

already larger than the coefficients of $(1-x)^N$, and only increases as $L$ grows. $\square$
