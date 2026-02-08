# C.3 Computing the Convolutional View [p. 22-25]

[p. 22]

The most involved part of using SSMs efficiently is computing $\overline{\boldsymbol{K}}$. This algorithm was sketched in Section 3.2 and is the main motivation for the S4 parameterization. This section defines the necessary intermediate quantities and proves the main technical result.

The algorithm for Theorem 3 falls in roughly three stages, leading to Algorithm 1. Assuming $\boldsymbol{A}$ has been conjugated into diagonal plus low-rank form, the problem of computing $\overline{\boldsymbol{K}}$ is successively simplified by applying the techniques outlined in Section 3.2.

**Remark C.1.** *We note that for the remainder of this section, we transpose $\boldsymbol{C}$ to be a column vector of shape $\mathbb{C}^N$ or $\mathbb{C}^{N \times 1}$ instead of matrix or row vector $\mathbb{C}^{1 \times N}$ as in (1). In other words the SSM is*

$$x'(t) = \boldsymbol{A}x(t) + \boldsymbol{B}u(t)$$
$$y(t) = \boldsymbol{C}^* x(t) + \boldsymbol{D}u(t).$$
(8)

Equation (8) restates the SSM with $\boldsymbol{C}$ as a column vector so that $\boldsymbol{C}$ has the same shape as $\boldsymbol{B}$, $\boldsymbol{P}$, $\boldsymbol{Q}$, simplifying the implementation of S4.

## Reduction 0: Diagonalization

[p. 22]

By Lemma 3.1, the representation can be switched by conjugating with any unitary matrix. For the remainder of this section, $\boldsymbol{A}$ is assumed to be (complex) diagonal plus low-rank (DPLR).

A DPLR matrix does not lend itself to efficient computation of $\overline{\boldsymbol{K}}$. The reason is that $\overline{\boldsymbol{K}}$ computes terms $\overline{\boldsymbol{C}}^* \overline{\boldsymbol{A}}^i \overline{\boldsymbol{B}}$ which involve powers of the matrix $\overline{\boldsymbol{A}}$. These are trivially computable when $\overline{\boldsymbol{A}}$ is diagonal, but it is no longer possible for even simple modifications to diagonal matrices such as DPLR.

## Reduction 1: SSM Generating Function

[p. 22]

To address the problem of computing powers of $\overline{\boldsymbol{A}}$, a generating function is introduced. Instead of computing the SSM convolution filter $\overline{\boldsymbol{K}}$ directly, a generating function on its coefficients is introduced and evaluations of it are computed.

**Definition 2** (SSM Generating Function). *We define the following quantities:*

- *The SSM convolution function is $\mathcal{K}(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}) = (\overline{\boldsymbol{C}}^* \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}^* \overline{\boldsymbol{A}} \overline{\boldsymbol{B}}, \ldots)$ and the (truncated) SSM filter of length L*

$$\mathcal{K}_L(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}) = (\overline{\boldsymbol{C}}^* \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}^* \overline{\boldsymbol{A}} \overline{\boldsymbol{B}}, \ldots, \overline{\boldsymbol{C}}^* \overline{\boldsymbol{A}}^{L-1} \overline{\boldsymbol{B}}) \in \mathbb{R}^L$$
(9)

- *The SSM generating function at node z is*

$$\hat{\mathcal{K}}(z; \overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}) \in \mathbb{C} := \sum_{i=0}^{\infty} \overline{\boldsymbol{C}}^* \overline{\boldsymbol{A}}^i \overline{\boldsymbol{B}} z^i = \overline{\boldsymbol{C}}^* (\boldsymbol{I} - \overline{\boldsymbol{A}} z)^{-1} \overline{\boldsymbol{B}}$$
(10)

- *and the truncated SSM generating function at node z is*

$$\hat{\mathcal{K}}_L(z; \overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}})^* \in \mathbb{C} := \sum_{i=0}^{L-1} \overline{\boldsymbol{C}}^* \overline{\boldsymbol{A}}^i \overline{\boldsymbol{B}} z^i = \overline{\boldsymbol{C}}^* (\boldsymbol{I} - \overline{\boldsymbol{A}}^L z^L)(\boldsymbol{I} - \overline{\boldsymbol{A}} z)^{-1} \overline{\boldsymbol{B}}$$
(11)

- *The truncated SSM generating function at nodes $\Omega \in \mathbb{C}^M$ is*

$$\hat{\mathcal{K}}_L(\Omega; \overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}) \in \mathbb{C}^M := \left( \hat{\mathcal{K}}_L(\omega_k; \overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}) \right)_{k \in [M]}$$
(12)

Intuitively, the generating function essentially converts the SSM convolution filter from the time domain to frequency domain. Importantly, it preserves the same information, and the desired SSM convolution filter can be recovered from evaluations of its generating function.

[p. 23]

**Lemma C.2.** *The SSM function $\mathcal{K}_L(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}})$ can be computed from the SSM generating function $\hat{\mathcal{K}}_L(\Omega; \overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}})$ at the roots of unity $\Omega = \{\exp(-2\pi i \frac{k}{L}) : k \in [L]\}$ stably in $O(L \log L)$ operations.*

*Proof.* For convenience define:

$$\overline{\boldsymbol{K}} = \mathcal{K}_L(\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}})$$

$$\hat{\boldsymbol{K}} = \hat{\mathcal{K}}_L(\Omega; \overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}})$$

$$\hat{\boldsymbol{K}}(z) = \hat{\mathcal{K}}_L(z; \overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}).$$

Note that:

$$\hat{\boldsymbol{K}}_j = \sum_{k=0}^{L-1} \overline{\boldsymbol{K}}_k \exp\left(-2\pi i \frac{jk}{L}\right).$$

This is exactly the same as the Discrete Fourier Transform (DFT):

$$\hat{\boldsymbol{K}} = \mathcal{F}_L \boldsymbol{K}.$$

Therefore $\boldsymbol{K}$ can be recovered from $\hat{\boldsymbol{K}}$ with a single inverse DFT, which requires $O(L \log L)$ operations with the Fast Fourier Transform (FFT) algorithm. $\square$

## Reduction 2: Woodbury Correction

[p. 23]

The primary motivation of Definition 2 is that it turns *powers* of $\overline{\boldsymbol{A}}$ into a single *inverse* of $\overline{\boldsymbol{A}}$ (equation (10)). While DPLR matrices cannot be powered efficiently due to the low-rank term, they can be inverted efficiently by the well-known Woodbury identity.

**Proposition 4** (Binomial Inverse Theorem or Woodbury matrix identity [15, 48]). *Over a commutative ring $\mathcal{R}$, let $\boldsymbol{A} \in \mathcal{R}^{N \times N}$ and $\boldsymbol{U}, \boldsymbol{V} \in \mathcal{R}^{N \times p}$. Suppose $\boldsymbol{A}$ and $\boldsymbol{A} + \boldsymbol{U}\boldsymbol{V}^*$ are invertible. Then $\boldsymbol{I}_p + \boldsymbol{V}^* \boldsymbol{A}^{-1} \boldsymbol{U} \in \mathcal{R}^{p \times p}$ is invertible and*

$$(\boldsymbol{A} + \boldsymbol{U}\boldsymbol{V}^*)^{-1} = \boldsymbol{A}^{-1} - \boldsymbol{A}^{-1}\boldsymbol{U}(\boldsymbol{I}_p + \boldsymbol{V}^*\boldsymbol{A}^{-1}\boldsymbol{U})^{-1}\boldsymbol{V}^*\boldsymbol{A}^{-1}$$

With this identity, the SSM generating function on a DPLR matrix $\boldsymbol{A}$ can be converted into one on just its diagonal component.

**Lemma C.3.** *Let $\boldsymbol{A} = \boldsymbol{\Lambda} - \boldsymbol{P}\boldsymbol{Q}^*$ be a diagonal plus low-rank representation. Then for any root of unity $z \in \Omega$, the truncated generating function satisfies*

$$\hat{\boldsymbol{K}}(z) = \frac{2}{1+z}\left[\tilde{\boldsymbol{C}}^* \boldsymbol{R}(z)\boldsymbol{B} - \tilde{\boldsymbol{C}}^* \boldsymbol{R}(z)\boldsymbol{P}\left(1 + \boldsymbol{Q}^*\boldsymbol{R}(z)\boldsymbol{P}\right)^{-1}\boldsymbol{Q}^*\boldsymbol{R}(z)\boldsymbol{B}\right]$$

$$\tilde{\boldsymbol{C}} = (\boldsymbol{I} - \overline{\boldsymbol{A}}^L)^*\boldsymbol{C}$$

$$\boldsymbol{R}(z; \boldsymbol{\Lambda}) = \left(\frac{2}{\Delta}\frac{1-z}{1+z} - \boldsymbol{\Lambda}\right)^{-1}.$$

*Proof.* Directly expanding Definition 2 yields:

$$\mathcal{K}_L(z; \overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}}) = \overline{\boldsymbol{C}}^* \overline{\boldsymbol{B}} + \overline{\boldsymbol{C}}^* \overline{\boldsymbol{A}} \overline{\boldsymbol{B}} z + \cdots + \overline{\boldsymbol{C}}^* \overline{\boldsymbol{A}}^{L-1} \overline{\boldsymbol{B}} z^{L-1}$$

$$= \overline{\boldsymbol{C}}^* \left(\boldsymbol{I} - \overline{\boldsymbol{A}}^L\right)(\boldsymbol{I} - \overline{\boldsymbol{A}} z)^{-1} \overline{\boldsymbol{B}}$$

$$= \tilde{\boldsymbol{C}}^* (\boldsymbol{I} - \overline{\boldsymbol{A}} z)^{-1} \overline{\boldsymbol{B}}$$

where $\tilde{\boldsymbol{C}}^* = \boldsymbol{C}^* \left(\boldsymbol{I} - \overline{\boldsymbol{A}}^L\right)$.

[p. 24]

The discretized SSM matrices $\overline{\boldsymbol{A}}$ and $\overline{\boldsymbol{B}}$ can be explicitly expanded back in terms of the original SSM parameters $\boldsymbol{A}$ and $\boldsymbol{B}$. Lemma C.4 provides an explicit formula, which allows further simplifying:

$$\tilde{\boldsymbol{C}}^* (\boldsymbol{I} - \overline{\boldsymbol{A}} z)^{-1} \overline{\boldsymbol{B}} = \frac{2}{1+z} \tilde{\boldsymbol{C}}^* \left(\frac{2}{\Delta}\frac{1-z}{1+z} - \boldsymbol{A}\right)^{-1} \boldsymbol{B}$$

$$= \frac{2}{1+z} \tilde{\boldsymbol{C}}^* \left(\frac{2}{\Delta}\frac{1-z}{1+z} - \boldsymbol{\Lambda} + \boldsymbol{P}\boldsymbol{Q}^*\right)^{-1} \boldsymbol{B}$$

$$= \frac{2}{1+z}\left[\tilde{\boldsymbol{C}}^* \boldsymbol{R}(z)\boldsymbol{B} - \tilde{\boldsymbol{C}}^* \boldsymbol{R}(z)\boldsymbol{P}\left(1 + \boldsymbol{Q}^*\boldsymbol{R}(z)\boldsymbol{P}\right)^{-1}\boldsymbol{Q}^*\boldsymbol{R}(z)\boldsymbol{B}\right].$$

The last line applies the Woodbury Identity (Proposition 4), where $\boldsymbol{R}(z) = \left(\frac{2}{\Delta}\frac{1-z}{1+z} - \boldsymbol{\Lambda}\right)^{-1}$. $\square$

**Lemma C.4.** *Let $\overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}$ be the SSM matrices $\boldsymbol{A}, \boldsymbol{B}$ discretized by the bilinear discretization with step size $\Delta$. Then*

$$\boldsymbol{C}^* (\boldsymbol{I} - \overline{\boldsymbol{A}} z)^{-1} \overline{\boldsymbol{B}} = \frac{2\Delta}{1+z} \boldsymbol{C}^* \left[2\frac{1-z}{1+z}\boldsymbol{I} - \Delta\boldsymbol{A}\right]^{-1} \boldsymbol{B}$$

*Proof.* Recall that the bilinear discretization (equation (3)) is:

$$\overline{\boldsymbol{A}} = \left(\boldsymbol{I} - \frac{\Delta}{2}\boldsymbol{A}\right)^{-1}\left(\boldsymbol{I} + \frac{\Delta}{2}\boldsymbol{A}\right)$$

$$\overline{\boldsymbol{B}} = \left(\boldsymbol{I} - \frac{\Delta}{2}\boldsymbol{A}\right)^{-1}\Delta\boldsymbol{B}$$

The result is proved by algebraic manipulations:

$$\boldsymbol{C}^* (\boldsymbol{I} - \overline{\boldsymbol{A}} z)^{-1} \overline{\boldsymbol{B}} = \boldsymbol{C}^* \left[\left(\boldsymbol{I} - \frac{\Delta}{2}\boldsymbol{A}\right)^{-1}\left(\boldsymbol{I} - \frac{\Delta}{2}\boldsymbol{A}\right) - \left(\boldsymbol{I} - \frac{\Delta}{2}\boldsymbol{A}\right)^{-1}\left(\boldsymbol{I} + \frac{\Delta}{2}\boldsymbol{A}\right)z\right]^{-1}\overline{\boldsymbol{B}}$$

$$= \boldsymbol{C}^* \left[\left(\boldsymbol{I} - \frac{\Delta}{2}\boldsymbol{A}\right) - \left(\boldsymbol{I} + \frac{\Delta}{2}\boldsymbol{A}\right)z\right]^{-1}\left(\boldsymbol{I} - \frac{\Delta}{2}\boldsymbol{A}\right)\overline{\boldsymbol{B}}$$

$$= \boldsymbol{C}^* \left[\boldsymbol{I}(1-z) - \frac{\Delta}{2}\boldsymbol{A}(1+z)\right]^{-1}\Delta\boldsymbol{B}$$

$$= \frac{\Delta}{1-z}\boldsymbol{C}^* \left[\boldsymbol{I} - \frac{\Delta\boldsymbol{A}}{2\frac{1-z}{1+z}}\right]^{-1}\boldsymbol{B}$$

$$= \frac{2\Delta}{1+z}\boldsymbol{C}^* \left[2\frac{1-z}{1+z}\boldsymbol{I} - \Delta\boldsymbol{A}\right]^{-1}\boldsymbol{B}$$

$\square$

Note that in the S4 parameterization, instead of constantly computing $\tilde{\boldsymbol{C}} = \left(\boldsymbol{I} - \overline{\boldsymbol{A}}^L\right)^* \boldsymbol{C}$, the parameters can simply be reparameterized to learn $\tilde{\boldsymbol{C}}$ directly instead of $\boldsymbol{C}$, saving a minor computation cost and simplifying the algorithm.

## Reduction 3: Cauchy Kernel

[p. 25]

The original problem of computing $\overline{\boldsymbol{K}}$ has been reduced to the problem of computing the SSM generating function $\hat{\mathcal{K}}_L(\Omega; \overline{\boldsymbol{A}}, \overline{\boldsymbol{B}}, \overline{\boldsymbol{C}})$ in the case that $\overline{\boldsymbol{A}}$ is a diagonal matrix. This is exactly the same as a Cauchy kernel, which is a well-studied problem with fast and stable numerical algorithms.

**Definition 3.** *A Cauchy matrix or kernel on nodes $\Omega = (\omega_i) \in \mathbb{C}^M$ and $\Lambda = (\lambda_j) \in \mathbb{C}^N$ is*

$$\boldsymbol{M} \in \mathbb{C}^{M \times N} = \boldsymbol{M}(\Omega, \Lambda) = (\boldsymbol{M}_{ij})_{i \in [M], j \in [N]} \qquad \boldsymbol{M}_{ij} = \frac{1}{\omega_i - \lambda_j}.$$

*The computation time of a Cauchy matrix-vector product of size $M \times N$ is denoted by $\mathcal{C}(M, N)$.*

Computing with Cauchy matrices is an extremely well-studied problem in numerical analysis, with both fast arithmetic algorithms and fast numerical algorithms based on the famous Fast Multipole Method (FMM) [29, 30, 31].

**Proposition 5** (Cauchy). *A Cauchy kernel requires $O(M + N)$ space, and operation count*

$$\mathcal{C}(M, N) = \begin{cases} O(MN) & \text{naively} \\ O\left((M + N) \log^2(M + N)\right) & \text{in exact arithmetic} \\ O\left((M + N) \log(M + N) \log \frac{1}{\varepsilon}\right) & \text{numerically to precision } \varepsilon. \end{cases}$$

**Corollary C.5.** *Evaluating $\boldsymbol{Q}^* \boldsymbol{R}(\Omega; \Lambda)\boldsymbol{P}$ (defined in Lemma C.3) for any set of nodes $\Omega \in \mathbb{C}^L$, diagonal matrix $\Lambda$, and vectors $\boldsymbol{P}$, $\boldsymbol{Q}$ can be computed in $\mathcal{C}(L, N)$ operations and $O(L + N)$ space, where $\mathcal{C}(L, N) = \tilde{O}(L + N)$ is the cost of a Cauchy matrix-vector multiplication.*

*Proof.* For any fixed $\omega \in \Omega$, the goal is to compute $\sum_j \frac{q_j^* p_j}{\omega - \lambda_j}$. Computing this over all $\omega_i$ is therefore exactly a Cauchy matrix-vector multiplication. $\square$

This completes the proof of Theorem 3. In Algorithm 1, the work is dominated by Step 2, which has a constant number of calls to a black-box Cauchy kernel, with complexity given by Proposition 5.
