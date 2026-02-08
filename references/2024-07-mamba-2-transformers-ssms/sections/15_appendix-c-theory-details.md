# C Theory Details [p. 48–50]

## C.1 Extras: Closure Properties of SSMs

[p. 48] Additional properties of semiseparable matrices are presented to illustrate their flexibility and utility. This section is noted as not necessary to understand the core results.

**Proposition C.1** (Semiseparable Closure Properties). *Semiseparable matrices are closed under several primitive operations.*

- **Addition**: The sum of an N-SS and P-SS matrix is at most (N + P)-SS.
- **Multiplication**: The product of an N-SS and P-SS matrix is (N + P)-SS.
- **Inverse**: The inverse of an N-SS matrix is at most (N + 1)-SS.

The addition and multiplication properties are easily seen. The inverse property has many proofs; one approach follows immediately from the Woodbury inversion identity, which has also featured prominently in the structured SSM literature (Gu, Goel, and Re 2022).

[p. 48] These in turn imply closure properties of state space models:
- The addition property says that summing two parallel SSM models is still an SSM.
- The multiplication property says that sequentially composing or chaining two SSMs can still be viewed as an SSM, whose total state size is additive — a somewhat nontrivial fact.
- The inverse property can let SSMs be related to other types of models. For example, banded matrices are semiseparable, so their inverses are semiseparable. (In fact, the semiseparable family of structure is often motivated by taking inverses of banded matrices (Vandebril et al. 2005).) Moreover, the fast recurrence properties of semiseparable matrices can be viewed as a consequence of their inverse being banded.

**Remark 11.** *The fact that 1-SS matrices are simple recurrences (7) are equivalent to the fact that the inverse of a 1-SS matrix is a 2-banded matrix:* [p. 48–49]

$$M = \begin{bmatrix} 1 & & & \\ a_1 & 1 & & \\ a_2 a_1 & a_2 & 1 & \\ \vdots & \vdots & \ddots & \ddots \\ a_{T-1} \ldots a_1 & a_{T-1} \ldots a_2 & \cdots & a_{T-1} & 1 \end{bmatrix} = \begin{bmatrix} 1 & & & \\ -a_1 & 1 & & \\ 0 & -a_2 & 1 & \\ \vdots & \vdots & \ddots & \ddots \\ 0 & 0 & \cdots & -a_{T-1} & 1 \end{bmatrix}^{-1}$$

Thus $y = Mx \leftrightarrow M^{-1}y = x$, or

$$\begin{bmatrix} 1 & & & \\ -a_1 & 1 & & \\ 0 & -a_2 & 1 & \\ \vdots & \vdots & \ddots & \ddots \\ 0 & 0 & \cdots & -a_{T-1} & 1 \end{bmatrix} y = x.$$

Or elementwise,

$$y_t - a_t y_{t-1} = x_t$$

$$y_t = a_t y_{t-1} + x_t.$$

[p. 49] Conversely, the closure results are also used to prove that autoregressive structured attention (under certain assumptions) must be SSMs, allowing the authors to show that more general families of efficient sequence models including attention variants can be reduced to state space models (Appendix C.2).

## C.2 Autoregressive Masked Attention is Semiseparable-Structured Attention

[p. 49] This proves Theorem 5.2 from Section 5.2. In Section 4.3, structured attention was defined as a broad generalization of masked attention, where the property of efficiency (i.e. a linear-time form for the kernel attention) is abstracted into the efficiency of structured matrix multiplication. However, beyond computational efficiency, standard linear attention (Katharopoulos et al. 2020) also has two important properties. First, it is *causal*, which is required for settings such as autoregressive modeling. Moreover, it has *efficient autoregressive generation*. In other words, the cost of an autoregressive step — i.e. the incremental cost of computing the output $y_T$ upon seeing $x_T$, given that $x_{0:T}$ has already been seen and preprocessed — requires only constant time.

Here the authors characterize which instances of SMA have efficient autoregression.

In the framework of SMA, causality is equivalent to the constraint that the mask $L$ is a **lower-triangular** matrix.

Characterizing the space of $L$ matrices that have efficient autoregression is more difficult. The authors use a narrow technical definition of autoregressive processes, in the spirit of classical definitions from the time series literature (e.g. ARIMA processes (Box et al. 2015)).

**Definition C.2.** *We define an autoregressive transformation $x \in \mathbb{R}^T \mapsto y \in \mathbb{R}^T$ of order $k$ as one where each output $y_t$ depends only on the current input and last $k$ outputs:*

$$y_t = \mu_t x_t + \ell_{t1} y_{t-1} + \cdots + \ell_{tk} y_{t-k}. \tag{23}$$

Note that the case where $L$ is the cumsum matrix is a special case with $k = 1$ and thus $y_t = x_t + y_{t_1}$. With this definition, characterizing the space of efficient autoregressive linear transforms follows from the properties of semiseparable matrices. Theorem C.3 formalizes and proves Theorem 5.2.

**Theorem C.3.** *Let $L \in \mathbb{R}^{T \times T}$ be an efficient autoregressive transformation of order $k$. Then $L$ is a state space model of order $k + 1$.*

*Proof.* Let $(x, y)$ be input and output sequences, so that $y = Lx$. Rearranging the definition (23),

$$y_t - \ell_{t1} y_{t-1} - \cdots - \ell_{tk} y_{t-k} = \mu_t x_t.$$

[p. 50] Vectorizing over $t$, this can be expressed as a matrix transformation:

$$\begin{bmatrix} 1 & & & & \\ -\ell_{t1} & \ddots & \ddots & & \\ \vdots & & & & \\ -\ell_{tk} & \cdots & -\ell_{t1} & 1 & \\ \vdots & \ddots & \vdots & \ddots & \ddots \\ 0 & \cdots & -\ell_{T-1,k} & \cdots & -\ell_{T-1,1} & 1 \end{bmatrix} \begin{bmatrix} y_0 \\ y_1 \\ \vdots \\ y_k \\ \vdots \\ y_{T-1} \end{bmatrix} = \begin{bmatrix} \mu_0 & & & \\ & \mu_1 & & \\ & & \ddots & \\ & & & \mu_k \\ & & & & \ddots \\ & & & & & \mu_{T-1} \end{bmatrix} \begin{bmatrix} x_0 \\ x_1 \\ \vdots \\ x_k \\ \vdots \\ x_{T-1} \end{bmatrix}$$

The $\mu$ diagonal matrix can be moved to the left and folded into the matrix of $\ell$ coefficients, which remains a $k + 1$-band lower-triangular matrix. But we also have $L^{-1}y = x$, so $L$ is the inverse of this matrix.

Next, note that $k+1$-band matrices are $k+1$-semiseparable by the rank characterization of semiseparability (Definition 3.1). By Proposition C.1, the inverse $L$ is therefore at most $k+2$-semiseparable. A slightly stronger bound of $k+1$ can be obtained because of the additional structure of banded matrices. Finally, the characterization of $L$ as an order-$k+1$ state space model follows from Theorem 3.5.

> In other words, efficient autoregressive attention is **semiseparable SMA**. [p. 50]
