# 3 Method: Structured State Spaces (S4) [p. 5-6]

[p. 5]

The technical results focus on developing the S4 parameterization and showing how to efficiently compute all views of the SSM (Section 2): the continuous representation (**A**, **B**, **C**) (1), the recurrent representation (**A-bar**, **B-bar**, **C-bar**) (3), and the convolutional representation **K-bar** (4).

Section 3.1 motivates the approach, which is based on the linear algebraic concepts of conjugation and diagonalization, and discusses why the naive application of this approach does not work. Section 3.2 gives an overview of the key technical components and formally defines the S4 parameterization. Section 3.3 sketches the main results, showing that S4 is asymptotically efficient (up to log factors) for sequence models. Proofs are in Appendices B and C.

## 3.1 Motivation: Diagonalization

[p. 5]

The fundamental bottleneck in computing the discrete-time SSM (3) is that it involves repeated matrix multiplication by **A-bar**. For example, computing (5) naively as in the LSSL involves L successive multiplications by **A-bar**, requiring O(N^2 L) operations and O(NL) space.

To overcome this bottleneck, the authors use a structural result that allows simplification of SSMs.

**Lemma 3.1.** *Conjugation is an equivalence relation on SSMs* (**A**, **B**, **C**) ~ (**V**^{-1} **A** **V**, **V**^{-1} **B**, **C** **V**).

*Proof.* Write out the two SSMs with state denoted by x and x-tilde respectively:

x' = **A** x + **B** u , x-tilde' = **V**^{-1} **A** **V** x-tilde + **V**^{-1} **B** u

y = **C** x , y = **C** **V** x-tilde

After multiplying the right side SSM by **V**, the two SSMs become identical with x = **V** x-tilde. Therefore these compute the exact same operator u -> y, but with a change of basis by **V** in the state x.

Lemma 3.1 motivates putting **A** into a canonical form by conjugation, which is ideally more structured and allows faster computation. For example, if **A** were diagonal, the resulting computations become much more tractable. In particular, the desired **K-bar** (equation (4)) would be a **Vandermonde product** which theoretically only needs O((N + L) log^2(N + L)) arithmetic operations [29].

Unfortunately, the naive application of diagonalization does not work due to numerical issues. The authors derive the explicit diagonalization for the HiPPO matrix (2) and show it has entries exponentially large in the state size N, rendering the diagonalization numerically infeasible (e.g. **C** **V** in Lemma 3.1 would not be computable). They note that Gu et al. [18] proposed a different (unimplemented) algorithm to compute **K-bar** faster than the naive algorithm. In Appendix B, they prove that it is also numerically unstable for related reasons.

**Lemma 3.2.** *The HiPPO matrix **A** in equation (2) is diagonalized by the matrix **V**_{ij} = C(i+j, i-j). In particular, V_{3i,i} = C(4i, 2i) ~ 2^{4i}. Therefore **V** has entries of magnitude up to 2^{4N/3}.*

## 3.2 The S4 Parameterization: Normal Plus Low-Rank

[p. 5-6]

The previous discussion implies that one should only conjugate by well-conditioned matrices **V**. The ideal scenario is when the matrix **A** is diagonalizable by a perfectly conditioned (i.e., unitary) matrix. By the Spectral Theorem of linear algebra, this is exactly the class of **normal matrices**. However, this class of matrices is restrictive; in particular, it does not contain the HiPPO matrix (2).

The authors make the observation that although the HiPPO matrix is not normal, it can be decomposed as the *sum of a normal and low-rank matrix*. However, this is still not useful by itself: unlike a diagonal matrix, powering up this sum (in (5)) is still slow and not easily optimized. This bottleneck is overcome by simultaneously applying three new techniques.

[p. 6]

- Instead of computing **K-bar** directly, the spectrum is computed by evaluating its **truncated generating function** sum_{j=0}^{L-1} **K-bar**_j zeta^j at the roots of unity zeta. **K-bar** can then be found by applying an inverse FFT.
- This generating function is closely related to the matrix resolvent, and now involves a matrix *inverse* instead of *power*. The low-rank term can now be corrected by applying the **Woodbury identity** which reduces (**A** + **P** **Q**^*)^{-1} in terms of **A**^{-1}, truly reducing to the diagonal case.
- Finally, the diagonal matrix case is equivalent to the computation of a **Cauchy kernel** 1/(omega_j - zeta_k), a well-studied problem with stable near-linear algorithms [30, 31].

The techniques apply to any matrix that can be decomposed as **Normal Plus Low-Rank (NPLR)**.

**Theorem 1.** *All HiPPO matrices from [16] have a NPLR representation*

$$\boldsymbol{A} = \boldsymbol{V} \boldsymbol{\Lambda} \boldsymbol{V}^* - \boldsymbol{P} \boldsymbol{Q}^\top = \boldsymbol{V} \left( \boldsymbol{\Lambda} - (\boldsymbol{V}^* \boldsymbol{P})(\boldsymbol{V}^* \boldsymbol{Q})^* \right) \boldsymbol{V}^*$$
(6)

*for unitary V in C^{N x N}, diagonal Lambda, and low-rank factorization **P**, **Q** in R^{N x r}. These matrices HiPPO-LegS, LegT, LagT all satisfy r = 1 or r = 2. In particular, equation (2) is NPLR with r = 1.*

Equation (6) decomposes **A** as a unitary conjugation of a diagonal-plus-low-rank (DPLR) matrix. This is the key structural result enabling efficient computation.

## 3.3 S4 Algorithms and Computational Complexity

[p. 6]

By equation (6), NPLR matrices can be conjugated into *diagonal plus low-rank* (DPLR) form (now over C instead of R). Theorems 2 and 3 describe the complexities of SSMs where **A** is in DPLR form. S4 is optimal or near-optimal for both recurrent and convolutional representations.

**Theorem 2** (S4 Recurrence). *Given any step size Delta, computing one step of the recurrence (3) can be done in O(N) operations where N is the state size.*

Theorem 2 follows from the fact that the inverse of a DPLR matrix is also DPLR (e.g. also by the Woodbury identity). This implies that the discretized matrix **A-bar** is the product of two DPLR matrices and thus has O(N) matrix-vector multiplication. Appendix C.2 computes **A-bar** in closed DPLR form.

**Theorem 3** (S4 Convolution). *Given any step size Delta, computing the SSM convolution filter **K-bar** can be reduced to 4 Cauchy multiplies, requiring only O-tilde(N + L) operations and O(N + L) space.*

Appendix C, Definition 3 formally defines Cauchy matrices, which are related to rational interpolation problems. Computing with Cauchy matrices is an extremely well-studied problem in numerical analysis, with both fast arithmetic and numerical algorithms based on the famous Fast Multipole Method (FMM) [29, 30, 31]. The computational complexities of these algorithms under various settings are described in Appendix C, Proposition 5.

The authors reiterate that Theorem 3 is the core technical contribution, and its algorithm is the very motivation of the NPLR S4 parameterization. This algorithm is formally sketched in Algorithm 1.

## Algorithm 1: S4 Convolution Kernel (Sketch)

**Input:** S4 parameters Lambda, **P**, **Q**, **B**, **C** in C^N and step size Delta

**Output:** SSM convolution kernel **K-bar** = K_L(**A-bar**, **B-bar**, **C-bar**) for **A** = Lambda - **P** **Q**^* (equation (5))

1. **C-tilde** <- (**I** - **A-bar**^L)^* **C-bar** -- Truncate SSM generating function (SSMGF) to length L
2. [[k_00(omega), k_01(omega)], [k_10(omega), k_11(omega)]] <- [**C-tilde** **Q**]^* (2/Delta * (1-omega)/(1+omega) - Lambda)^{-1} [**B** **P**] -- Black-box Cauchy kernel
3. **K-hat**(omega) <- 2/(1+omega) [k_00(omega) - k_01(omega)(1 + k_11(omega))^{-1} k_10(omega)] -- Woodbury Identity
4. **K-hat** = {**K-hat**(omega) : omega = exp(2 pi i k/L)} -- Evaluate SSMGF at all roots of unity omega in Omega_L
5. **K-bar** <- iFFT(**K-hat**) -- Inverse Fourier Transform
