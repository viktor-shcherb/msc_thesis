# C Proof of Lower Bound for Small Alphabets [p. 30–31]

## C.1 Proof of Lemma 3 [p. 30]

**Lemma 3.** *Let $\mathbf{A}$ be chosen uniformly at random from the set $\mathcal{S}$. Then, with probability at least $(1 - 1/n)$ over the choice $\mathbf{A} \in \mathcal{S}$, any (randomized) algorithm that can distinguish the outputs from the model $\mathcal{M}(\mathbf{A})$ from the distribution over random examples $U_n$ with success probability greater than $2/3$ over the randomness of the examples and the algorithm needs $f(n)$ time or examples.*

[p. 30] *Proof.* Suppose $\mathbf{A} \in \{0, 1\}^{m \times n}$ is chosen at random with each entry being i.i.d. with its distribution uniform on $\{0, 1\}$. Recall that $\mathcal{S}$ is the set of all $(m \times n)$ matrices $\mathbf{A}$ which are full row rank. We claim that $P(\mathbf{A} \in \mathcal{S}) \geq 1 - m 2^{-n/6}$. To verify, consider the addition of each row one by one to $\mathbf{A}'$. The probability of the $i$th row being linearly dependent on the previous $(i - 1)$ rows is $2^{i-1-n}$. Hence by a union bound, $\mathbf{A}'$ is full row-rank with failure probability at most $m 2^{m-n} \leq m 2^{-n/2}$.

From Definition 2 and a union bound over all the $m \leq n/2$ parities, any algorithm that can distinguish the outputs from the model $\mathcal{M}(\mathbf{A})$ for uniformly chosen $\mathbf{A}$ from the distribution over random examples $U_n$ with probability at least $(1 - 1/(2n))$ over the choice of $\mathbf{A}$ needs $f(n)$ time or examples. As $P(\mathbf{A} \in \mathcal{S}) \geq 1 - m 2^{-n/2}$ for a uniformly randomly chosen $\mathbf{A}$, with probability at least $(1 - 1/(2n) - m 2^{-n/2}) \geq (1 - 1/n)$ over the choice $\mathbf{A} \in \mathcal{S}$ any algorithm which can distinguish the outputs from the model $\mathcal{M}(\mathbf{A})$ from the distribution over random examples $U_n$ with success probability greater than 2/3 over the randomness of the examples and the algorithm needs $f(n)$ time or examples. $\square$

## C.2 Proof of Proposition 2 [p. 30–31]

**Proposition 2.** *With $f(T)$ as defined in Definition 2, for all sufficiently large $T$ and $1/T^c < \epsilon \leq 0.1$ for some fixed constant $c$, there exists a family of HMMs with $T$ hidden states such that any algorithm that achieves average relative zero-one loss, average $\ell_1$ loss, or average KL loss less than $\epsilon$ with probability greater than $2/3$ for a randomly chosen HMM in the family, requires $f(\Omega(\log T / \epsilon))$ time or samples from the HMM.*

[p. 30–31] *Proof.* We describe how to choose the family of sequential models $\mathbf{A}_{m \times n}$ for each value of $\epsilon$ and $T$. Recall that the HMM has $T = 2^m(2n + m) + m$ hidden states. Let $T' = 2^{m+2}(n + m)$. Note that $T' \geq T$. Let $t = \log T'$. We choose $m = t - \log(1/\epsilon) - \log(t/5)$, and $n$ to be the solution of $t = m + \log(n + m) + 2$, hence $n = t/(5\epsilon) - m - 2$. Note that for $\epsilon \leq 0.1$, $n \geq m$. Let $\epsilon' = \frac{2}{9} \frac{m}{n+m}$. We claim $\epsilon \leq \epsilon'$. To verify, note that $n + m = t/(5\epsilon) - 2$. Therefore,

$$\epsilon' = \frac{2m}{9(n+m)} = \frac{10\epsilon(t - \log(1/\epsilon) - \log(t/5))}{9t(1 - 10\epsilon/t)} \geq \epsilon,$$

for sufficiently large $t$ and $\epsilon \geq 2^{-ct}$ for a fixed constant $c$. Hence proving hardness for obtaining error $\epsilon'$ implies hardness for obtaining error $\epsilon$. We choose the matrix $\mathbf{A}_{m \times n}$ as outlined earlier. The family is defined by the model $\mathcal{M}(\mathbf{A}_{m \times n})$ defined previously with the matrix $\mathbf{A}_{m \times n}$ chosen uniformly at random from the set $\mathcal{S}$.

### Relative zero-one loss [p. 31]

[p. 31] Let $\rho_{01}(\mathcal{A})$ be the average zero-one loss of some algorithm $\mathcal{A}$ for the output time steps $n$ through $(n + m - 1)$ and $\delta'_{01}(\mathcal{A})$ be the average relative zero-one loss of $\mathcal{A}$ for the output time steps $n$ through $(n + m - 1)$ with respect to the optimal predictions. For the distribution $U_n$ it is not possible to get $\rho_{01}(\mathcal{A}) < 0.5$ as the clauses and the label $\mathbf{y}$ are independent and $\mathbf{y}$ is chosen uniformly at random from $\{0, 1\}^m$. For $Q_{\mathbf{s}}^\eta$ it is information theoretically possible to get $\rho_{01}(\mathcal{A}) = \eta/2$. Hence any algorithm which gets error $\rho_{01}(\mathcal{A}) \leq 2/5$ can be used to distinguish between $U_n$ and $Q_{\mathbf{s}}^\eta$. Therefore by Lemma 3 any algorithm which gets $\rho_{01}(\mathcal{A}) \leq 2/5$ with probability greater than 2/3 over the choice of $\mathcal{M}(\mathbf{A})$ needs at least $f(n)$ time or samples.

Note that $\delta'_{01}(\mathcal{A}) = \rho_{01}(\mathcal{A}) - \eta/2$. As the optimal predictor $\mathcal{P}_\infty$ gets $\rho_{01}(\mathcal{P}_\infty) = \eta/2 < 0.05$, therefore $\delta'_{01}(\mathcal{A}) \leq 1/3 \implies \rho_{01}(\mathcal{A}) \leq 2/5$. Note that $\delta_{01}(\mathcal{A}) \geq \delta'_{01}(\mathcal{A}) \frac{m}{n+m}$. This is because $\delta_{01}(\mathcal{A})$ is the average error for all $(n + m)$ time steps, and the contribution to the error from time steps 0 to $(n - 1)$ is non-negative. Also, $\frac{1}{3} \frac{m}{n+m} > \epsilon'$, therefore, $\delta_{01}(\mathcal{A}) < \epsilon' \implies \delta'_{01}(\mathcal{A}) < \frac{1}{3} \implies \rho_{01}(\mathcal{A}) \leq 2/5$. Hence any algorithm which gets average relative zero-one loss less than $\epsilon'$ with probability greater than 2/3 over the choice of $\mathcal{M}(\mathbf{A})$ needs $f(n)$ time or samples. The result for $\ell_1$ loss follows directly from the result for relative zero-one loss, we next consider the KL loss.

### KL loss [p. 31]

[p. 31] Let $\delta'_{KL}(\mathcal{A})$ be the average KL error of the algorithm $\mathcal{A}$ from time steps $n$ through $(n + m - 1)$. By application of Jensen's inequality and Pinsker's inequality, $\delta'_{KL}(\mathcal{A}) \leq 2/9 \implies \delta'_{01}(\mathcal{A}) \leq 1/3$. Therefore, by the previous argument any algorithm which gets $\delta'_{KL}(\mathcal{A}) < 2/9$ needs $f(n)$ samples. But as before, $\delta_{KL}(\mathcal{A}) \leq \epsilon' \implies \delta'_{KL}(\mathcal{A}) \leq 2/9$. Hence any algorithm which gets average KL loss less than $\epsilon'$ needs $f(n)$ time or samples.

### Lower bounding $n$ in terms of $\log T / \epsilon$ [p. 31]

[p. 31] We lower bound $n$ by a linear function of $\log T / \epsilon$ to express the result directly in terms of $\log T / \epsilon$. We claim that $\log T / \epsilon$ is at most $10n$. This follows because:

$$\log T / \epsilon \leq t / \epsilon = 5(n + m) + 10 \leq 15n$$

Hence any algorithm needs $f(\Omega(\log T / \epsilon))$ samples and time to get average relative zero-one loss, $\ell_1$ loss, or KL loss less than $\epsilon$ with probability greater than 2/3 over the choice of $\mathcal{M}(\mathbf{A})$. $\square$
