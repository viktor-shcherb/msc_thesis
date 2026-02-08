# C.1 NPLR Representations of HiPPO Matrices [p. 19-20]

[p. 19]

This subsection proves Theorem 1, showing that all HiPPO matrices for continuous-time memory fall under the S4 normal plus low-rank (NPLR) representation.

*Proof of Theorem 1.* The three cases HiPPO-LagT, HiPPO-LegT, and HiPPO-LegS are considered separately. Note that the primary HiPPO matrix defined in this work (equation (2)) is the HiPPO-LegT matrix.

## HiPPO-LagT

The HiPPO-LagT matrix is simply:

$$\boldsymbol{A}_{nk} = \begin{cases} 0 & n < k \\ -\frac{1}{2} & n = k \\ -1 & n > k \end{cases}$$

$$\boldsymbol{A} = -\begin{bmatrix} \frac{1}{2} \\ 1 & \frac{1}{2} \\ 1 & 1 & \frac{1}{2} \\ 1 & 1 & 1 & \frac{1}{2} \\ \vdots & & & \ddots \end{bmatrix}.$$

Adding the matrix of all $\frac{1}{2}$, which is rank 1, yields:

$$-\begin{bmatrix} & -\frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} \\ \frac{1}{2} & & -\frac{1}{2} & -\frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & & -\frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} & \end{bmatrix}.$$

This matrix is now skew-symmetric. Skew-symmetric matrices are a particular case of normal matrices with pure-imaginary eigenvalues.

Gu et al. [16] also consider a case of HiPPO corresponding to the generalized Laguerre polynomials that generalizes the above HiPPO-LagT case. In this case, the matrix **A** (up to conjugation by a diagonal matrix) ends up being close to the above matrix, but with a different element on the diagonal. After adding the rank-1 correction, it becomes the above skew-symmetric matrix plus a multiple of the identity. Thus after diagonalization by the same matrix as in the LagT case, it is still reduced to diagonal plus low-rank (DPLR) form, where the diagonal is now pure imaginary plus a real constant.

## HiPPO-LegS

[p. 20]

The formula from equation (2) is restated for convenience:

$$\boldsymbol{A}_{nk} = -\begin{cases} (2n+1)^{1/2}(2k+1)^{1/2} & \text{if } n > k \\ n+1 & \text{if } n = k \\ 0 & \text{if } n < k \end{cases}.$$

Adding $\frac{1}{2}(2n+1)^{1/2}(2k+1)^{1/2}$ to the whole matrix gives:

$$-\begin{cases} \frac{1}{2}(2n+1)^{1/2}(2k+1)^{1/2} & \text{if } n > k \\ \frac{1}{2} & \text{if } n = k \\ -\frac{1}{2}(2n+1)^{1/2}(2k+1)^{1/2} & \text{if } n < k \end{cases}$$

Note that this matrix is not skew-symmetric, but is $\frac{1}{2}\boldsymbol{I} + \boldsymbol{S}$ where $\boldsymbol{S}$ is a skew-symmetric matrix. This is diagonalizable by the same unitary matrix that diagonalizes **S**. This is sufficient for the NPLR representation.

## HiPPO-LegT

Up to the diagonal scaling, the LegT matrix is:

$$\boldsymbol{A} = -\begin{bmatrix} 1 & -1 & 1 & -1 & \ldots \\ 1 & 1 & -1 & 1 \\ 1 & 1 & 1 & -1 \\ 1 & 1 & 1 & 1 \\ \vdots & & & \ddots \end{bmatrix}.$$

By adding $-1$ to this matrix and then the matrix:

$$\begin{bmatrix} & & \\ 2 & & 2 \\ & & \\ 2 & & 2 \end{bmatrix}$$

the matrix becomes:

$$\begin{bmatrix} & -2 & & -2 \\ 2 & & & \\ & & & -2 \\ 2 & & 2 & \end{bmatrix}$$

which is skew-symmetric. In fact, this matrix is the inverse of the Chebyshev Jacobi.

An alternative way to see this is as follows. The LegT matrix is the inverse of the matrix:

$$\begin{bmatrix} -1 & 1 & & 0 \\ -1 & & 1 & \\ & -1 & & 1 \\ & & -1 & -1 \end{bmatrix}$$

This can obviously be converted to a skew-symmetric matrix by adding a rank 2 term. The inverses of these matrices are also rank-2 differences from each other by the Woodbury identity.

A final form is:

$$\begin{bmatrix} -1 & 1 & -1 & 1 \\ -1 & -1 & 1 & -1 \\ -1 & -1 & -1 & 1 \\ -1 & -1 & -1 & -1 \end{bmatrix} + \begin{bmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 & 1 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 1 \\ -1 & 0 & -1 & 0 \end{bmatrix}$$

This has the advantage that the rank-2 correction is symmetric (like the others), but the normal skew-symmetric matrix is now 2-quasiseparable instead of 1-quasiseparable. $\square$
